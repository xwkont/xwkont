#!/usr/bin/env python3
"""Generate a Turtle mapping-set graph from each SSSOM/TSV in data/crosswalks/.

Per ADR-0024: data/crosswalks/<slug>/<slug>.yaml is the SSOT for a concept;
data/crosswalks/<slug>/<slug>.tsv (see scripts/crosswalk-to-sssom-tsv.py) is
a derived SSSOM/TSV projection of it, and this generated Turtle is in turn a
derived, non-canonical projection of that TSV, reusing SSSOM's own RDF
vocabulary (https://w3id.org/sssom/schema/) rather than a bespoke XwkOnt
mapping schema. It is kept separate from data/ontology/core.ttl, which holds
only XwkOnt's own xwkont-core: classes.

Requires only rdflib (already the project's sole soft dependency, per
docs/publication/validation-commands.md).

Usage:
    python3 scripts/sssom-tsv-to-ttl.py [--check]

    --check   Exit non-zero if any generated .ttl would differ from what's
              already on disk, without writing anything.
"""

import csv
import re
import sys
from pathlib import Path

from rdflib import Graph, Literal, Namespace, RDF
from rdflib.namespace import DCTERMS, RDFS

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data" / "crosswalks"

XWKONT = Namespace("https://w3id.org/xwkont/id#")
XWKONT_SOURCE_TERM = Namespace("https://w3id.org/xwkont/source-term#")
SSSOM = Namespace("https://w3id.org/sssom/schema/")

PREDICATE_NAMESPACES = {
    "skos": Namespace("http://www.w3.org/2004/02/skos/core#"),
}


def slugify(term):
    slug = re.sub(r"[^A-Za-z0-9]+", "_", term).strip("_")
    return slug or "unnamed"


def resolve_term_uri(cell):
    """Return a (uri, ontology, term_label) triple, or None if `cell` isn't
    in 'Ontology:Term' form (the explicit-non-equivalence / no-counterpart
    rows -- see ADR-0023 discussion; these are skipped from the RDF
    projection, not force-fit into it)."""
    ontology, sep, term = cell.partition(":")
    if not sep or not term:
        return None
    uri = XWKONT_SOURCE_TERM[f"{ontology}-{slugify(term)}"]
    return uri, ontology, term


def resolve_predicate_uri(predicate_id):
    if not predicate_id:
        return None
    prefix, sep, local = predicate_id.partition(":")
    ns = PREDICATE_NAMESPACES.get(prefix)
    if ns is None or not sep:
        raise ValueError(f"Unknown predicate_id prefix: {predicate_id!r}")
    return ns[local]


def build_graph(tsv_path):
    graph = Graph()
    graph.bind("xwkont", XWKONT)
    graph.bind("xwkont-source-term", XWKONT_SOURCE_TERM)
    graph.bind("sssom", SSSOM)
    graph.bind("skos", PREDICATE_NAMESPACES["skos"])

    skipped = 0
    with tsv_path.open(newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            subject = resolve_term_uri(row["subject_id"])
            obj = resolve_term_uri(row["object_id"])
            if subject is None or obj is None:
                skipped += 1
                continue

            subject_uri, subject_ontology, subject_term = subject
            object_uri, object_ontology, object_term = obj

            mapping_uri = XWKONT[row["mapping_id"].removeprefix("xwkont:")]
            graph.add((mapping_uri, RDF.type, SSSOM.Mapping))
            graph.add((mapping_uri, SSSOM.subject_id, subject_uri))
            graph.add((mapping_uri, SSSOM.object_id, object_uri))
            graph.add((subject_uri, RDFS.label, Literal(subject_term, lang="en")))
            graph.add((subject_uri, DCTERMS.source, Literal(subject_ontology)))
            graph.add((object_uri, RDFS.label, Literal(object_term, lang="en")))
            graph.add((object_uri, DCTERMS.source, Literal(object_ontology)))

            predicate_uri = resolve_predicate_uri(row["predicate_id"])
            if predicate_uri is not None:
                graph.add((mapping_uri, SSSOM.predicate_id, predicate_uri))

            if row["mapping_justification"]:
                graph.add((mapping_uri, SSSOM.mapping_justification,
                           Literal(row["mapping_justification"])))
            if row["confidence"]:
                graph.add((mapping_uri, SSSOM.confidence, Literal(float(row["confidence"]))))
            if row["comment"]:
                graph.add((mapping_uri, RDFS.comment, Literal(row["comment"], lang="en")))

    return graph, skipped


def main():
    check_only = "--check" in sys.argv[1:]
    mismatches = []
    written = []
    total_skipped = 0

    for tsv_path in sorted(DATA_DIR.glob("*/*.tsv")):
        slug = tsv_path.stem
        graph, skipped = build_graph(tsv_path)
        total_skipped += skipped
        ttl_text = graph.serialize(format="turtle")

        out_path = tsv_path.parent / f"{slug}.ttl"
        if check_only:
            existing = out_path.read_text() if out_path.exists() else None
            if existing != ttl_text:
                mismatches.append(slug)
        else:
            out_path.write_text(ttl_text)
            written.append(slug)

    if check_only:
        if mismatches:
            print(f"Stale/missing generated TTL for: {', '.join(mismatches)}", file=sys.stderr)
            sys.exit(1)
        print(f"All generated TTL files are up to date ({total_skipped} rows skipped, no counterpart term).")
    else:
        print(f"Wrote {len(written)} TTL files to {DATA_DIR} ({total_skipped} rows skipped, no counterpart term).")


if __name__ == "__main__":
    main()
