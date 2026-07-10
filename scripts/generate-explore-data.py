#!/usr/bin/env python3
"""Generate docs/explore/data/*.json for the public Explore visualizations.

Reads LinkML crosswalk YAML (SSOT) and the core ontology Mermaid hierarchy.
Safe to run repeatedly; output is deterministic for a given input set.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CROSSWALKS = ROOT / "data" / "crosswalks"
CORE_MMD = ROOT / "docs" / "ontology" / "core-ontology.mmd"
OUT_DIR = ROOT / "docs" / "explore" / "data"

SOURCE_ORDER = ["BFO", "DOLCE", "SUMO", "UFO", "GFO", "YAMATO", "TUpper", "GUM"]


def load_yaml(path: Path) -> dict:
    import yaml

    return yaml.safe_load(path.read_text(encoding="utf-8"))


def parse_core_hierarchy(mmd: str) -> dict:
    inheritance: list[dict] = []
    relations: list[dict] = []
    classes: set[str] = set()
    for line in mmd.splitlines():
        line = line.strip()
        if not line or line.startswith("classDiagram"):
            continue
        if "<|--" in line:
            parent, child = [p.strip() for p in line.split("<|--", 1)]
            classes.update([parent, child])
            inheritance.append({"parent": parent, "child": child})
        elif "-->" in line:
            left, rest = [p.strip() for p in line.split("-->", 1)]
            if ":" in rest:
                right, label = [p.strip() for p in rest.split(":", 1)]
            else:
                right, label = rest, ""
            classes.update([left, right])
            relations.append({"source": left, "target": right, "label": label})
    return {
        "classes": sorted(classes),
        "inheritance": inheritance,
        "relations": relations,
    }


def ontology_from_term(term: str) -> str | None:
    if not term or ":" not in term:
        return None
    prefix = term.split(":", 1)[0].strip()
    # Normalize common prefixes to ADR-0015 labels
    mapping = {
        "BFO": "BFO",
        "DOLCE": "DOLCE",
        "SUMO": "SUMO",
        "UFO": "UFO",
        "GFO": "GFO",
        "YAMATO": "YAMATO",
        "TUpper": "TUpper",
        "TUPPER": "TUpper",
        "GUM": "GUM",
        "IAO": "IAO",
    }
    return mapping.get(prefix, prefix)


def build_crosswalk_payload() -> dict:
    concepts = []
    for path in sorted(CROSSWALKS.glob("*/*.yaml")):
        if path.parent.name == "schema":
            continue
        record = load_yaml(path)
        slug = record["slug"]
        title = record["title"]
        correspondences = []
        ontologies_present: set[str] = set()
        for row in record.get("correspondences") or []:
            ont = row.get("source_ontology")
            if ont:
                ontologies_present.add(ont)
            correspondences.append(
                {
                    "id": row.get("correspondence_id"),
                    "ontology": ont,
                    "term": row.get("source_term"),
                    "identifier": row.get("source_identifier_or_iri"),
                }
            )

        mappings = []
        for row in record.get("mapping_assertions") or []:
            subject = row.get("subject") or ""
            obj = row.get("object") or ""
            mappings.append(
                {
                    "id": row.get("mapping_id"),
                    "subject": subject,
                    "object": obj,
                    "subject_ontology": ontology_from_term(subject),
                    "object_ontology": ontology_from_term(obj),
                    "relation": row.get("relation_category"),
                    "confidence": row.get("confidence"),
                    "predicate": row.get("predicate_id"),
                }
            )

        concepts.append(
            {
                "slug": slug,
                "title": title,
                "status": record.get("editorial_status"),
                "ontologies": sorted(ontologies_present, key=lambda o: SOURCE_ORDER.index(o) if o in SOURCE_ORDER else 99),
                "correspondence_count": len(correspondences),
                "mapping_count": len(mappings),
                "correspondences": correspondences,
                "mappings": mappings,
            }
        )

    # Coverage matrix: concept × ontology → correspondence count
    matrix = []
    for concept in concepts:
        counts = defaultdict(int)
        for c in concept["correspondences"]:
            if c["ontology"]:
                counts[c["ontology"]] += 1
        matrix.append(
            {
                "slug": concept["slug"],
                "title": concept["title"],
                "counts": {ont: counts.get(ont, 0) for ont in SOURCE_ORDER},
            }
        )

    return {
        "generated_from": "data/crosswalks/*/*.yaml",
        "source_order": SOURCE_ORDER,
        "concept_count": len(concepts),
        "concepts": concepts,
        "coverage_matrix": matrix,
    }


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    core = parse_core_hierarchy(CORE_MMD.read_text(encoding="utf-8"))
    crosswalks = build_crosswalk_payload()

    (OUT_DIR / "core-hierarchy.json").write_text(
        json.dumps(core, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (OUT_DIR / "crosswalks.json").write_text(
        json.dumps(crosswalks, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        f"Wrote {OUT_DIR / 'core-hierarchy.json'} "
        f"({len(core['classes'])} classes) and "
        f"{OUT_DIR / 'crosswalks.json'} ({crosswalks['concept_count']} concepts)"
    )


if __name__ == "__main__":
    main()
