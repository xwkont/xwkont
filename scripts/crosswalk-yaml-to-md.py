#!/usr/bin/env python3
"""Render data/crosswalks/<slug>/<slug>.yaml -> docs/crosswalks/concepts/<slug>.md.

Per ADR-0024, once this generator is trusted, docs/crosswalks/concepts/*.md
becomes a generated projection of the YAML SSOT rather than a hand-authored
artifact. This script is being introduced in --dry-run mode first (the
default): it never writes to docs/crosswalks/concepts/ unless --write is
passed explicitly. Use --dry-run (or no flag) to render each concept and
diff it against the existing Markdown, to assess round-trip fidelity before
trusting this as the generation step in a real pipeline.

Usage:
    python3 scripts/crosswalk-yaml-to-md.py [slug ...]            # dry-run diff, default: all
    python3 scripts/crosswalk-yaml-to-md.py --summary             # dry-run, one line per concept
    python3 scripts/crosswalk-yaml-to-md.py --write [slug ...]    # actually overwrite the .md files
"""

import difflib
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data" / "crosswalks"
CONCEPTS_DIR = REPO_ROOT / "docs" / "crosswalks" / "concepts"


def bt(value):
    """Backtick-wrap a value for inline-code Markdown, as the corpus does
    for identifiers (predicate_id, relation_category, ref ids, etc.)."""
    return f"`{value}`"


REF_ID_RE = re.compile(r"^(xwkont:ref:[a-z0-9]+(?:-[a-z0-9]+)*|ADR-[0-9]{4})$")


def join_refs(ref_ids):
    """Backtick-wrap each clean 'xwkont:ref:<slug>' (or 'ADR-NNNN') id, but
    leave a prose fallback item untouched -- extract_ref_ids() in the
    migration falls back to the raw cell text (which may already contain
    its own backticks, e.g. a '*(cross-cutting ... `0.2.0`-batch ...)*'
    placeholder) when no ref id is present. Unconditionally wrapping every
    item would double-nest backticks around that already-formatted text."""
    return ", ".join(bt(r) if REF_ID_RE.match(r) else r for r in ref_ids)


def render_frontmatter(r):
    lines = [f"# {r['title']}", ""]
    lines.append(f"> **Local identifier:** `{r['local_identifier']}`")
    lines.append(f"> **Slug:** `{r['slug']}`")
    lines.append(f"> **Editorial status:** `{r['editorial_status']}`")
    lines.append(f"> **Created:** `{r['created']}`")
    if r.get("modified"):
        lines.append(f"> **Modified:** `{r['modified']}`")
    return "\n".join(lines)


def render_scope_note(r):
    paragraphs = r["scope_note"].split("\n\n\n")
    return "## Scope Note\n\n" + "\n\n".join(p.strip() for p in paragraphs)


def render_row(cells):
    """Join cells with markdown-table pipes, collapsing the double space a
    naive join produces around an empty cell (' | ' + '' + ' |' -> '  |')
    down to the single space the corpus's own tables use for an empty cell
    ('| |'), so an empty Notes/Locator/etc. cell round-trips exactly."""
    line = "| " + " | ".join(cells) + " |"
    return re.sub(r"(?<=\|) {2,}(?=\|)", " ", line)


def render_table(header, rows):
    lines = [render_row(header), "|" + "|".join("---" for _ in header) + "|"]
    for row in rows:
        lines.append(render_row(row))
    return "\n".join(lines)


def render_labels(r):
    header = ["Role", "Label or term", "Source", "Language", "Notes"]
    rows = [
        [e["role"], e["label"], e["label_source"], bt(e["language"]), e.get("entry_notes", "")]
        for e in r["labels"]
    ]
    return "## Labels, Alternate Labels, and Source Terminology\n\n" + render_table(header, rows)


def render_reference_cell(reference_ids, note):
    """Prefer the verbatim original cell text (note) when the migration
    found more than a plain ref-id list in it -- see reference_note's
    schema description for why this isn't reconstructed from the list."""
    return note if note else join_refs(reference_ids)


def render_source_definitions(r):
    header = ["Source", "Term or identifier", "Dimension", "Claim type",
              "Definition, quotation, or paraphrase", "Reference", "Locator", "Notes"]
    rows = [
        [e["source"], e["term_or_identifier"], e["dimension"], e["source_claim_type"],
         e["text"], render_reference_cell(e["reference"], e.get("reference_note")),
         e.get("locator", ""), e.get("entry_notes", "")]
        for e in r["source_definitions"]
    ]
    return "## Source Definitions and Contextual Notes\n\n" + render_table(header, rows)


def render_identifier_cell(value):
    """Corpus convention: a bare single-token identifier/IRI gets
    backtick-wrapped ('`BFO_0000030`'); a prose explanation ('not
    applicable -- ...') does not; a cell already containing backticks was
    left untouched by the migration's strip_cell() specifically because it
    has more than one backtick-wrapped token (e.g. multiple identifiers in
    one Source Identifier or IRI cell) and is reproduced verbatim."""
    if "`" in value or " " in value:
        return value
    return bt(value)


def render_correspondences(r):
    header = ["Correspondence ID", "Source ontology", "Source term",
              "Source identifier or IRI", "Source version", "Reference", "Inclusion rationale"]
    rows = [
        [bt(e["correspondence_id"]), e["source_ontology"], e["source_term"],
         render_identifier_cell(e["source_identifier_or_iri"]), e["source_version"],
         join_refs(e["reference"]), e["inclusion_rationale"]]
        for e in r["correspondences"]
    ]
    section = "## Source Ontology Correspondences\n\n" + render_table(header, rows)
    if r.get("correspondences_note"):
        section += "\n\n" + r["correspondences_note"]
    return section


def render_claim_type_cell(e):
    if e.get("claim_type_annotation"):
        return f"~~{e['claim_type']}~~ **{e['claim_type_annotation']}**"
    return e["claim_type"]


def render_confidence_cell(e):
    if e.get("confidence_annotation"):
        return f"{e['confidence']} {e['confidence_annotation']}"
    return e["confidence"]


def render_comparison_notes(r):
    header = ["Note ID", "Dimension", "Claim type", "Note", "Supporting references", "Confidence"]
    rows = [
        [bt(e["note_id"]), e["dimension"], render_claim_type_cell(e), e["note"],
         render_reference_cell(e["supporting_references"], e.get("supporting_references_note")),
         render_confidence_cell(e)]
        for e in r["comparison_notes"]
    ]
    return "## Semantic Comparison Notes\n\n" + render_table(header, rows)


def render_mapping_assertions(r):
    header = ["Mapping ID", "Subject", "Relation category", "Object", "`predicate_id`",
              "`mapping_justification`", "Status", "Confidence", "Rationale", "Provenance"]
    rows = []
    for e in r["mapping_assertions"]:
        predicate_id = bt(e["predicate_id"]) if e.get("predicate_id") else "none"
        rows.append([
            bt(e["mapping_id"]), e["subject"], bt(e["relation_category"]), e["object"],
            predicate_id, bt(e["mapping_justification"]), e["status"], e["confidence"],
            e["rationale"], join_refs(e["provenance"]),
        ])
    lead_in = f"{r['mapping_assertions_note']}\n\n" if r.get("mapping_assertions_note") else ""
    return "## Mapping Assertions or Candidate Relations\n\n" + lead_in + render_table(header, rows)


def render_uncertainty_type_cell(e):
    if e.get("resolved"):
        if not e.get("resolution_note") and not e.get("resolved_date"):
            # Bare 'resolved' cell in the original -- no strikethrough/bold
            # markup, no recoverable original uncertainty_type. Reproduce
            # that literally rather than fabricating '~~uncertainty~~
            # **resolved**' markup the source never had.
            return "resolved"
        note = e.get("resolution_note") or f"resolved {e['resolved_date']}"
        return f"~~{e['uncertainty_type']}~~ **{note}**"
    return e["uncertainty_type"]


def render_uncertainties(r):
    header = ["Item ID", "Type", "Description", "Impact", "Follow-up"]
    rows = [
        [bt(e["item_id"]), render_uncertainty_type_cell(e), e["description"], e["impact"],
         e["follow_up"]]
        for e in r["uncertainties"]
    ]
    return "## Uncertainty, Non-Equivalence, and Open Questions\n\n" + render_table(header, rows)


def render_references(r):
    lines = ["## Provenance and References", ""]
    for e in r["references"]:
        lines.append(f"- {bt(e['reference_id'])} — {e['short_label']} — {e['verification_note']}")
    return "\n".join(lines)


def render_review_history(r):
    header = ["Review ID", "Date", "Outcome", "Notes"]
    rows = []
    for e in r.get("review_history", []):
        review_id = bt(e["review_id"]) if e.get("review_id") else "—"
        rows.append([review_id, e["review_date"], e["outcome"],
                     e.get("review_notes", "")])
    return "## Review History\n\n" + render_table(header, rows)


def render_future_work(r):
    lines = ["## Future Work", ""]
    for item in r.get("future_work", []):
        lines.append(f"- {item}")
    return "\n".join(lines)


def render(record):
    sections = [
        render_frontmatter(record),
        render_scope_note(record),
        render_labels(record),
        render_source_definitions(record),
        render_correspondences(record),
        render_comparison_notes(record),
        render_mapping_assertions(record),
        render_uncertainties(record),
        render_references(record),
        render_review_history(record),
        render_future_work(record),
    ]
    return "\n\n".join(sections) + "\n"


def main():
    args = sys.argv[1:]
    write = "--write" in args
    summary = "--summary" in args
    slugs = [a for a in args if a not in ("--write", "--summary", "--dry-run")]

    yaml_paths = sorted(
        p for p in DATA_DIR.glob("*/*.yaml") if p.parent.name != "schema"
    )
    if slugs:
        yaml_paths = [p for p in yaml_paths if p.stem in slugs]

    for yaml_path in yaml_paths:
        slug = yaml_path.stem
        record = yaml.safe_load(yaml_path.read_text())
        rendered = render(record)
        md_path = CONCEPTS_DIR / f"{slug}.md"

        if write:
            md_path.write_text(rendered)
            print(f"Wrote {md_path}")
            continue

        existing = md_path.read_text() if md_path.exists() else ""
        diff = list(difflib.unified_diff(
            existing.splitlines(keepends=True),
            rendered.splitlines(keepends=True),
            fromfile=str(md_path),
            tofile=f"{yaml_path} (rendered)",
        ))
        if summary:
            added = sum(1 for l in diff if l.startswith("+") and not l.startswith("+++"))
            removed = sum(1 for l in diff if l.startswith("-") and not l.startswith("---"))
            status = "IDENTICAL" if not diff else f"DIFF (+{added}/-{removed} lines)"
            print(f"{slug}: {status}")
        else:
            if diff:
                print(f"=== {slug} ===")
                sys.stdout.writelines(diff)
            else:
                print(f"=== {slug}: IDENTICAL ===")


if __name__ == "__main__":
    main()
