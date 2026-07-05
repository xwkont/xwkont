#!/usr/bin/env python3
"""Extract each crosswalk's Mapping Assertions into an SSSOM-style TSV.

Per ADR-0024: data/crosswalks/<slug>/<slug>.yaml (LinkML schema-validated) is
the SSOT for a concept, including its Mapping Assertions. This script reads
that YAML directly and writes data/crosswalks/<slug>/<slug>.tsv, a derived,
machine-readable SSSOM/TSV projection -- superseding ADR-0023's Markdown-
sourced, flat-path generation (docs/crosswalks/concepts/<slug>.md is itself
now only a generated projection of the same YAML; see
scripts/crosswalk-yaml-to-md.py).

Usage:
    python3 scripts/crosswalk-to-sssom-tsv.py [--check]

    --check   Exit non-zero if any generated TSV would differ from what's
              already on disk, without writing anything. For validation.
"""

import csv
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data" / "crosswalks"

# ADR-0014's fixed, static category-to-number projection. `unknown` is
# deliberately omitted from the export rather than projected to 0.0.
CONFIDENCE_PROJECTION = {
    "high": "1.0",
    "medium-high": "0.8",
    "medium": "0.6",
    "low-medium": "0.4",
    "low": "0.2",
    "unknown": "",
}

TSV_HEADER = [
    "mapping_id",
    "subject_id",
    "predicate_id",
    "object_id",
    "mapping_justification",
    "confidence",
    "xwkont_confidence_category",
    "xwkont_relation_category",
    "xwkont_status",
    "comment",
    "xwkont_provenance",
]


def build_curie(source_ontology, term):
    """Mirror the YAML's own '<SourceOntology>:<Term>' subject/object
    notation directly as the CURIE, since that is the level of identifier
    fidelity the crosswalks themselves record today (several sources have
    no confirmed IRI at all -- see each concept's own Future Work section
    and TODO.md's deferred UUID/identifier-scheme note)."""
    return f"{source_ontology}:{term}"


def resolve_id(cell):
    """Most subject/object values are '<SourceOntology>:<Term>'; a handful of
    'explicit-non-equivalence'-style rows instead name only a source ontology
    (no counterpart term exists at all) or a free-text placeholder like
    '*(no counterpart in any other of the 8 sources)*'. Those are passed
    through verbatim rather than forced into a CURIE they don't fit -- the
    absence of a comparable term is itself the fact being recorded."""
    ontology, sep, term = cell.partition(":")
    if not sep or not term:
        return cell
    return build_curie(ontology, term)


def join_provenance(provenance):
    return ", ".join(provenance)


def mapping_to_tsv_record(mapping, slug):
    mapping_id = mapping["mapping_id"]
    subject = mapping["subject"]
    if ":" not in subject:
        raise ValueError(f"{slug}: Subject not in 'Ontology:Term' form: {mapping}")
    subject_id = resolve_id(subject)
    object_id = resolve_id(mapping["object"])

    predicate_id = mapping.get("predicate_id") or ""

    category = mapping["confidence"].strip()
    if category not in CONFIDENCE_PROJECTION:
        raise ValueError(f"{slug}: unknown confidence category '{category}' in {mapping_id}")

    return {
        "mapping_id": mapping_id,
        "subject_id": subject_id,
        "predicate_id": predicate_id,
        "object_id": object_id,
        "mapping_justification": mapping["mapping_justification"],
        "confidence": CONFIDENCE_PROJECTION[category],
        "xwkont_confidence_category": category,
        "xwkont_relation_category": mapping["relation_category"],
        "xwkont_status": mapping["status"],
        "comment": mapping["rationale"],
        "xwkont_provenance": join_provenance(mapping["provenance"]),
    }


def generate_tsv_text(records):
    from io import StringIO

    buf = StringIO()
    writer = csv.DictWriter(buf, fieldnames=TSV_HEADER, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    for record in records:
        writer.writerow(record)
    return buf.getvalue()


def main():
    check_only = "--check" in sys.argv[1:]
    mismatches = []
    written = []

    yaml_paths = sorted(
        p for p in DATA_DIR.glob("*/*.yaml") if p.parent.name != "schema"
    )
    for yaml_path in yaml_paths:
        slug = yaml_path.stem
        record = yaml.safe_load(yaml_path.read_text())
        records = [
            mapping_to_tsv_record(mapping, slug)
            for mapping in record["mapping_assertions"]
        ]
        tsv_text = generate_tsv_text(records)

        out_path = yaml_path.parent / f"{slug}.tsv"
        if check_only:
            existing = out_path.read_text() if out_path.exists() else None
            if existing != tsv_text:
                mismatches.append(slug)
        else:
            out_path.write_text(tsv_text)
            written.append(slug)

    if check_only:
        if mismatches:
            print(f"Stale/missing generated TSV for: {', '.join(mismatches)}", file=sys.stderr)
            sys.exit(1)
        print(f"All {len(yaml_paths)} generated TSV files are up to date.")
    else:
        print(f"Wrote {len(written)} TSV files to {DATA_DIR}/<slug>/")


if __name__ == "__main__":
    main()
