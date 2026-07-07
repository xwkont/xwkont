#!/usr/bin/env python3
"""Convert _private/<slug>-draft.md -> data/crosswalks/<slug>/<slug>.yaml.

Bootstraps the LinkML-validated YAML SSOT (per ADR-0024) from an
AI-delegated crosswalk draft, per the Codex-delegation process recorded in
_private/codex-delegation-process.md: a delegated author (e.g. Codex) writes
a TEMPLATE.md-shaped Markdown draft to _private/<slug>-draft.md only, never
to docs/crosswalks/concepts/ (which is generated-only); this script performs
the mechanical Markdown -> YAML field transcription so a human/Claude
reviewer doesn't have to hand-transcribe every table row, but the reviewer
is still expected to independently re-verify every citation against primary
sources and hand-edit the YAML before it is trusted, validated, or used to
generate the real docs/crosswalks/concepts/<slug>.md.

This is a deliberately mechanical, deterministic transcription -- it does
not infer, normalize, or invent content beyond what parse_*() functions
below extract directly from the Markdown tables. It is the direct successor
of scripts/crosswalk-md-to-yaml.py (the one-off migration tool used for the
original 17 concepts, added and removed from this repo multiple times per
its own "one-off, not continuously run" framing -- see git history). This
version is intentionally scoped to a disjoint source directory
(_private/*-draft.md, never docs/crosswalks/concepts/*.md) specifically so
it can be a standing, persistent tool without reintroducing the
docs/crosswalks/concepts/ bidirectional-editing risk that motivated
repeatedly deleting its predecessor: it structurally cannot overwrite a
generated Markdown projection, because it never reads from that directory.

Usage:
    python3 scripts/crosswalk-draft-md-to-yaml.py [slug ...]   # default: all drafts
    python3 scripts/crosswalk-draft-md-to-yaml.py --check       # exit non-zero on any diff
"""

import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DRAFTS_DIR = REPO_ROOT / "_private"
OUTPUT_DIR = REPO_ROOT / "data" / "crosswalks"

DRAFT_SUFFIX = "-draft.md"

STRIKETHROUGH_ANNOTATION = re.compile(r"^~~(?P<base>.+?)~~\s*\*\*(?P<note>.+?)\*\*\s*$")
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


def strip_cell(cell):
    """Strip a cell's own outer whitespace and, when the whole cell is
    exactly one backtick-wrapped token (e.g. '`BFO_0000030`'), its wrapping
    backticks too.

    Only fires when the cell has exactly one backtick pair (cell.count('`')
    == 2). A cell with more backticks than that (e.g.
    '`BFO_0000140`, `BFO_0000147`, `BFO_0000142`' -- several separately
    backtick-wrapped identifiers in one Source Identifier or IRI cell, a
    real corpus pattern in space.md/time.md/etc.) is left completely
    untouched: naively stripping only the first and last backtick would
    corrupt the interior, turning '`a`, `b`' into 'a`, `b' -- a real bug
    caught by round-tripping this migration's output back to Markdown and
    diffing against the original (see docs/methodology/
    crosswalk-concept-linkml-schema.md)."""
    cell = cell.strip()
    if cell.startswith("`") and cell.endswith("`") and cell.count("`") == 2:
        cell = cell[1:-1]
    return cell


def none_if_literal_none(value):
    return None if value.strip().lower() == "none" else value


REF_ID_RE = re.compile(r"xwkont:ref:[a-z0-9]+(?:-[a-z0-9]+)*")


def extract_ref_ids(cell):
    """Extract every 'xwkont:ref:<slug>' token from a Reference/Provenance/
    Supporting-references cell, in order. Regex extraction (rather than
    comma-splitting the already-strip_cell()-mangled text) is deliberate:
    corpus rows sometimes backtick-wrap each ref id separately (e.g.
    '`xwkont:ref:a`, `xwkont:ref:b`'), and parse_table()'s whole-cell
    strip_cell() only strips the outermost pair of backticks, leaving stray
    backticks around interior tokens that a naive comma-split would not
    clean up.

    Falls back to the raw cell text as a single-item list when no ref id is
    present -- corpus practice includes a small number of prose placeholders
    here that a strict xwkont:ref:* requirement would otherwise force this
    migration to drop or fail on."""
    ids = REF_ID_RE.findall(cell)
    return ids if ids else [cell.strip()]


def extra_prose_note(cell, ids):
    """Returns the original cell text verbatim if it contains more than a
    plain comma-separated list of the given ref ids, else None.

    A handful of corpus cells mix a real evidentiary qualifier into an
    otherwise ref-id list -- e.g. '`xwkont:ref:a` (BFO only),
    `xwkont:ref:b`' or '`xwkont:ref:a`, confirmed against `xwkont:ref:b`
    directly'. Reconstructing just the leftover phrase via string-
    subtraction is fragile (punctuation/spacing artifacts); storing the
    whole original cell verbatim and letting the renderer prefer it over
    the plain list is exact instead of approximate."""
    residue = cell
    for ref_id in ids:
        residue = residue.replace(ref_id, "")
    residue = re.sub(r"[`,\s]+", "", residue)
    return cell.strip() if residue else None


CONFIDENCE_LEVELS = ("high", "medium-high", "medium", "low-medium", "low", "unknown")
CONFIDENCE_ANNOTATION_RE = re.compile(
    r"^(?P<base>" + "|".join(re.escape(v) for v in CONFIDENCE_LEVELS) + r")\s*(?P<rest>.*)$"
)


def parse_confidence_cell(cell):
    """Returns (base_confidence, annotation_or_None), unwrapping a trailing
    free-text qualifier like 'high (verified directly against ...)'."""
    m = CONFIDENCE_ANNOTATION_RE.match(cell.strip())
    if not m:
        raise ValueError(f"unrecognized confidence value: {cell!r}")
    rest = m.group("rest").strip().strip(";").strip()
    return m.group("base"), (rest if rest else None)


def split_section(text, heading):
    """Return the body text between '## {heading}' and the next '## ' heading."""
    pattern = re.compile(
        r"^## " + re.escape(heading) + r"\s*$\n(.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    if match is None:
        raise ValueError(f"section not found: {heading}")
    return match.group(1)


def parse_table(section_text, expected_header):
    lines = [line for line in section_text.splitlines() if line.strip().startswith("|")]
    if not lines:
        return []
    header = [strip_cell(c) for c in lines[0].strip().strip("|").split("|")]
    if header != expected_header:
        raise ValueError(f"unexpected header {header!r}, expected {expected_header!r}")
    rows = []
    for line in lines[2:]:
        cells = [strip_cell(c) for c in line.strip().strip("|").split("|")]
        if len(cells) != len(expected_header):
            raise ValueError(f"row/header length mismatch: {line!r}")
        rows.append(dict(zip(expected_header, cells)))
    return rows


def parse_bullets(section_text):
    """Each top-level '- ' line, or non-bullet paragraph line, is one entry."""
    entries = []
    for line in section_text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("- "):
            entries.append(line[2:].strip())
        else:
            entries.append(line)
    return entries


def parse_frontmatter(text):
    header_match = re.search(r"^# (.+)$", text, re.MULTILINE)
    title = header_match.group(1).strip()

    def field(name):
        m = re.search(rf"^> \*\*{name}:\*\* (.+)$", text, re.MULTILINE)
        return m.group(1).strip() if m else None

    local_identifier = strip_cell(field("Local identifier"))
    slug = strip_cell(field("Slug"))
    editorial_status = strip_cell(field("Editorial status"))
    created = strip_cell(field("Created"))
    modified_raw = field("Modified")
    modified = strip_cell(modified_raw) if modified_raw else None

    return {
        "title": title,
        "local_identifier": local_identifier,
        "slug": slug,
        "editorial_status": editorial_status,
        "created": created,
        "modified": modified,
    }


def parse_scope_note(text):
    body = split_section(text, "Scope Note").strip("\n")
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    return "\n\n\n".join(paragraphs)


def parse_labels(text):
    rows = parse_table(
        split_section(text, "Labels, Alternate Labels, and Source Terminology"),
        ["Role", "Label or term", "Source", "Language", "Notes"],
    )
    out = []
    for r in rows:
        entry = {
            "role": r["Role"],
            "label": r["Label or term"],
            "label_source": r["Source"],
            "language": r["Language"] or "en",
        }
        if r["Notes"]:
            entry["entry_notes"] = r["Notes"]
        out.append(entry)
    return out


def parse_source_definitions(text):
    rows = parse_table(
        split_section(text, "Source Definitions and Contextual Notes"),
        ["Source", "Term or identifier", "Dimension", "Claim type",
         "Definition, quotation, or paraphrase", "Reference", "Locator", "Notes"],
    )
    out = []
    for r in rows:
        ref_ids = extract_ref_ids(r["Reference"])
        entry = {
            "source": r["Source"],
            "term_or_identifier": r["Term or identifier"],
            "dimension": r["Dimension"],
            "source_claim_type": r["Claim type"],
            "text": r["Definition, quotation, or paraphrase"],
            "reference": ref_ids,
        }
        reference_note = extra_prose_note(r["Reference"], ref_ids)
        if reference_note:
            entry["reference_note"] = reference_note
        if r["Locator"]:
            entry["locator"] = r["Locator"]
        if r["Notes"]:
            entry["entry_notes"] = r["Notes"]
        out.append(entry)
    return out


def parse_correspondences(text):
    section_text = split_section(text, "Source Ontology Correspondences")
    rows = parse_table(
        section_text,
        ["Correspondence ID", "Source ontology", "Source term",
         "Source identifier or IRI", "Source version", "Reference", "Inclusion rationale"],
    )
    entries = [
        {
            "correspondence_id": r["Correspondence ID"],
            "source_ontology": r["Source ontology"],
            "source_term": r["Source term"],
            "source_identifier_or_iri": r["Source identifier or IRI"],
            "source_version": r["Source version"],
            "reference": extract_ref_ids(r["Reference"]),
            "inclusion_rationale": r["Inclusion rationale"],
        }
        for r in rows
    ]

    # Prose trailing the table itself (before the next '## ' heading) -- not
    # part of any table row, so parse_table() alone would silently drop it.
    lines = section_text.splitlines()
    table_line_indices = [i for i, l in enumerate(lines) if l.strip().startswith("|")]
    trailing_lines = lines[max(table_line_indices) + 1:] if table_line_indices else lines
    note = "\n".join(trailing_lines).strip() or None

    return entries, note


def parse_claim_type_cell(cell):
    """Returns (base_claim_type, annotation_or_None), unwrapping
    '~~inference~~ **checked and unconfirmed, 2026-07-01**' style markup."""
    m = STRIKETHROUGH_ANNOTATION.match(cell)
    if m:
        return m.group("base").strip(), m.group("note").strip()
    return cell, None


def parse_comparison_notes(text):
    rows = parse_table(
        split_section(text, "Semantic Comparison Notes"),
        ["Note ID", "Dimension", "Claim type", "Note", "Supporting references", "Confidence"],
    )
    out = []
    for r in rows:
        claim_type, claim_annotation = parse_claim_type_cell(r["Claim type"])
        confidence, confidence_annotation = parse_confidence_cell(r["Confidence"])
        supporting_refs = extract_ref_ids(r["Supporting references"])
        entry = {
            "note_id": r["Note ID"],
            "dimension": r["Dimension"],
            "claim_type": claim_type,
            "note": r["Note"],
            "supporting_references": supporting_refs,
            "confidence": confidence,
        }
        supporting_refs_note = extra_prose_note(r["Supporting references"], supporting_refs)
        if supporting_refs_note:
            entry["supporting_references_note"] = supporting_refs_note
        if claim_annotation:
            entry["claim_type_annotation"] = claim_annotation
        if confidence_annotation:
            entry["confidence_annotation"] = confidence_annotation
        out.append(entry)
    return out


def parse_mapping_assertions(text):
    section_text = split_section(text, "Mapping Assertions or Candidate Relations")
    rows = parse_table(
        section_text,
        ["Mapping ID", "Subject", "Relation category", "Object", "predicate_id",
         "mapping_justification", "Status", "Confidence", "Rationale", "Provenance"],
    )
    out = []
    for r in rows:
        entry = {
            "mapping_id": r["Mapping ID"],
            "subject": r["Subject"],
            "relation_category": r["Relation category"],
            "object": r["Object"],
            "mapping_justification": r["mapping_justification"],
            "status": r["Status"],
            "confidence": r["Confidence"],
            "rationale": r["Rationale"],
            "provenance": extract_ref_ids(r["Provenance"]),
        }
        predicate_id = none_if_literal_none(r["predicate_id"])
        if predicate_id:
            entry["predicate_id"] = predicate_id
        out.append(entry)

    # Prose preceding the table itself (after the section heading, before
    # the first '|' line) -- not part of any table row, so parse_table()
    # alone would silently drop it.
    lines = section_text.splitlines()
    first_table_idx = next(
        (i for i, l in enumerate(lines) if l.strip().startswith("|")), len(lines)
    )
    leading_lines = lines[:first_table_idx]
    note = "\n".join(leading_lines).strip() or None

    return out, note


def parse_uncertainty_type_cell(cell):
    """Returns (base_type, resolved: bool, resolved_date_or_None,
    resolution_note_or_None)."""
    m = STRIKETHROUGH_ANNOTATION.match(cell)
    if m:
        base = m.group("base").strip()
        note = m.group("note").strip()
        dates = DATE_RE.findall(note)
        return base, True, (dates[0] if dates else None), note
    if cell.strip().lower() == "resolved":
        # Bare 'resolved' cell with no strikethrough/bold markup and no
        # separate base type recoverable from the cell alone. note is
        # deliberately None, not cell.strip(): a non-None resolution_note
        # would make the renderer reproduce the fuller '~~type~~ **note**'
        # form, which doesn't match this cell's actual bare-word original.
        return "uncertainty", True, None, None
    return cell, False, None, None


def parse_uncertainties(text):
    rows = parse_table(
        split_section(text, "Uncertainty, Non-Equivalence, and Open Questions"),
        ["Item ID", "Type", "Description", "Impact", "Follow-up"],
    )
    out = []
    for r in rows:
        base_type, resolved, resolved_date, note = parse_uncertainty_type_cell(r["Type"])
        entry = {
            "item_id": r["Item ID"],
            "uncertainty_type": base_type,
            "resolved": resolved,
            "description": r["Description"],
            "impact": r["Impact"],
            "follow_up": r["Follow-up"],
        }
        if resolved_date:
            entry["resolved_date"] = resolved_date
        if note:
            entry["resolution_note"] = note
        out.append(entry)
    return out


REFERENCE_BULLET = re.compile(
    r"^-\s*`(?P<ref_id>xwkont:ref:[a-z0-9-]+|ADR-[0-9]{4})`\s*[—-]\s*(?P<rest>.+)$"
)


def parse_references(text):
    body = split_section(text, "Provenance and References")
    out = []
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        m = REFERENCE_BULLET.match(line)
        if not m:
            raise ValueError(f"unrecognized reference bullet: {line!r}")
        rest = m.group("rest")
        if " — " in rest:
            short_label, verification_note = rest.split(" — ", 1)
        elif " - " in rest:
            short_label, verification_note = rest.split(" - ", 1)
        else:
            short_label, verification_note = rest, None
        entry = {
            "reference_id": m.group("ref_id"),
            "short_label": short_label.strip(),
        }
        if verification_note:
            entry["verification_note"] = verification_note.strip()
        out.append(entry)
    return out


def parse_review_history(text):
    section = split_section(text, "Review History")
    lines = [line for line in section.splitlines() if line.strip().startswith("|")]
    if not lines:
        return []
    header = [strip_cell(c) for c in lines[0].strip().strip("|").split("|")]
    if header not in (
        ["Review ID", "Date", "Outcome", "Notes"],
    ):
        raise ValueError(f"unexpected Review History header: {header}")
    id_key = header[0]
    out = []
    for line in lines[2:]:
        cells = [strip_cell(c) for c in line.strip().strip("|").split("|")]
        row = dict(zip(header, cells))
        review_id = row[id_key]
        if review_id in ("", "—", "*(unreviewed)*", "pending"):
            review_id = None
        entry = {
            "review_date": row["Date"],
            "outcome": row["Outcome"],
        }
        if review_id:
            entry["review_id"] = review_id
        if row["Notes"]:
            entry["review_notes"] = row["Notes"]
        out.append(entry)
    return out


def parse_future_work(text):
    body = split_section(text, "Future Work")
    return parse_bullets(body)


def convert(md_path, slug):
    text = md_path.read_text()
    frontmatter = parse_frontmatter(text)

    record = {
        "local_identifier": frontmatter["local_identifier"] or f"xwkont:concept:{slug}",
        "slug": frontmatter["slug"] or slug,
        "title": frontmatter["title"],
        "editorial_status": frontmatter["editorial_status"] or "draft",
        "created": frontmatter["created"],
    }
    if frontmatter["modified"]:
        record["modified"] = frontmatter["modified"]

    record["scope_note"] = parse_scope_note(text)
    record["labels"] = parse_labels(text)
    record["source_definitions"] = parse_source_definitions(text)
    correspondences, correspondences_note = parse_correspondences(text)
    record["correspondences"] = correspondences
    if correspondences_note:
        record["correspondences_note"] = correspondences_note
    record["comparison_notes"] = parse_comparison_notes(text)
    mapping_assertions, mapping_assertions_note = parse_mapping_assertions(text)
    record["mapping_assertions"] = mapping_assertions
    if mapping_assertions_note:
        record["mapping_assertions_note"] = mapping_assertions_note
    record["uncertainties"] = parse_uncertainties(text)
    record["references"] = parse_references(text)

    review_history = parse_review_history(text)
    if review_history:
        record["review_history"] = review_history

    future_work = parse_future_work(text)
    if future_work:
        record["future_work"] = future_work

    return record


class QuotedDate(str):
    pass


def represent_quoted(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", str(data), style='"')


yaml.add_representer(QuotedDate, represent_quoted)

DATE_FIELDS = {"created", "modified", "review_date", "resolved_date"}


def quote_dates(obj):
    """Force ISO date-looking strings to be emitted quoted, so a YAML loader
    doesn't coerce them to date/datetime objects behind the schema's back."""
    if isinstance(obj, dict):
        return {
            k: (QuotedDate(v) if k in DATE_FIELDS and isinstance(v, str) else quote_dates(v))
            for k, v in obj.items()
        }
    if isinstance(obj, list):
        return [quote_dates(v) for v in obj]
    return obj


def to_yaml_text(record):
    return yaml.dump(
        quote_dates(record),
        sort_keys=False,
        allow_unicode=True,
        width=88,
        default_flow_style=False,
    )


def main():
    args = sys.argv[1:]
    check_only = "--check" in args
    slugs = [a for a in args if a != "--check"]

    draft_files = sorted(DRAFTS_DIR.glob(f"*{DRAFT_SUFFIX}"))
    draft_by_slug = {f.name[: -len(DRAFT_SUFFIX)]: f for f in draft_files}

    if slugs:
        missing = set(slugs) - set(draft_by_slug)
        if missing:
            print(f"No such draft file(s): {sorted(missing)}", file=sys.stderr)
            sys.exit(2)
        draft_by_slug = {s: draft_by_slug[s] for s in slugs}

    mismatches = []
    written = []
    failed = []

    for slug, md_path in sorted(draft_by_slug.items()):
        try:
            record = convert(md_path, slug)
        except Exception as exc:  # noqa: BLE001 -- report and continue, don't abort the batch
            failed.append((slug, str(exc)))
            continue

        yaml_text = to_yaml_text(record)
        out_dir = OUTPUT_DIR / slug
        out_path = out_dir / f"{slug}.yaml"

        if check_only:
            existing = out_path.read_text() if out_path.exists() else None
            if existing != yaml_text:
                mismatches.append(slug)
        else:
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path.write_text(yaml_text)
            written.append(slug)

    if failed:
        print("Failed to convert:", file=sys.stderr)
        for slug, err in failed:
            print(f"  {slug}: {err}", file=sys.stderr)

    if check_only:
        if mismatches or failed:
            if mismatches:
                print(f"Stale/missing generated YAML for: {', '.join(mismatches)}", file=sys.stderr)
            sys.exit(1)
        print(f"All {len(draft_by_slug)} draft-derived YAML files are up to date.")
    else:
        print(f"Wrote {len(written)} YAML file(s) to {OUTPUT_DIR} ({len(failed)} failed).")
        if failed:
            sys.exit(1)


if __name__ == "__main__":
    main()
