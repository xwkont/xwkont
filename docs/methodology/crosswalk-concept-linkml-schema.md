# Crosswalk-Concept LinkML Schema

> **Status:** Schema designed; all 17 `reviewed` concepts migrated Markdown → YAML and validated; the YAML → Markdown renderer is now trusted and run for real (`--write`); `docs/crosswalks/concepts/*.md` is a generated artifact. TSV/TTL generation now also reads from YAML and writes the nested `data/crosswalks/<slug>/<slug>.{tsv,ttl}` layout. See 2026-07-05 (second pass) addendum below.
> **Date:** 2026-07-05
> **Related:** `docs/adr/ADR-0024-linkml-schema-validated-data-as-ssot-for-crosswalk-concepts.md`, `docs/INFORMATION_ARCHITECTURE.md`

## Purpose

`ADR-0024` decided that a LinkML schema-validated YAML record becomes the SSOT for a crosswalk concept, with Markdown/TSV/TTL as generated projections, but explicitly deferred both the schema's field-by-field design and the 17-concept migration to implementation. This document records that design and the completed migration.

## Schema Location

`data/crosswalks/schema/crosswalk-concept.yaml` — a single LinkML schema modeling the full nine-section structure `docs/INFORMATION_ARCHITECTURE.md` defines for a concept crosswalk (Identity/Editorial Status through Review History and Future Work). One `CrosswalkConcept` root class holds eight repeatable-row classes (`LabelEntry`, `SourceDefinition`, `Correspondence`, `ComparisonNote`, `MappingAssertion`, `UncertaintyItem`, `ReferenceCitation`, `ReviewEvent`), one per Markdown table.

Per `ADR-0024` point 1, all long-form fields (`scope_note`, `text`, `note`, `rationale`, `description`, etc.) remain arbitrary-length free-text strings — the schema validates structure and controlled vocabulary, not prose length or content.

## Migration Tool

`scripts/crosswalk-md-to-yaml.py` is a **one-off migration script**, not a continuously-run generator (unlike `scripts/crosswalk-to-sssom-tsv.py`, which `ADR-0023` intends to keep re-running). It parses each `docs/crosswalks/concepts/<slug>.md` and writes `data/crosswalks/<slug>/<slug>.yaml`. Run once per concept to produce the initial YAML; edit the YAML directly afterward. Re-running it against a concept whose YAML has since diverged from its Markdown would silently discard the YAML-only edits — `--check` guards against exactly that (content diff, not just file-presence) for whichever concepts haven't yet had their Markdown retired.

```bash
python3 scripts/crosswalk-md-to-yaml.py               # migrate all 17
python3 scripts/crosswalk-md-to-yaml.py object time    # migrate specific slugs
python3 scripts/crosswalk-md-to-yaml.py --check        # exit non-zero on any diff
```

## Controlled Vocabulary Reused, Not Reinvented

Every enum's permissible values are the literal strings `docs/INFORMATION_ARCHITECTURE.md` and its amending ADRs already define, not a new naming convention:

- `EditorialStatus` — the six values from `docs/INFORMATION_ARCHITECTURE.md`'s Editorial Status Values table.
- `Dimension` — `technical`/`philosophical`/`both` (`ADR-0010`).
- `ClaimType` — used by both Source Definitions and Semantic Comparison Notes (see "A Real Finding" below for why these were merged into one five-value enum rather than IA's originally documented two-value/four-value split).
- `RelationCategory` — the nine categories from `docs/methodology/crosswalk-methodology.md`.
- `ConfidenceLevel` — the six-value scale from `ADR-0009`/`ADR-0013` (`high` through `unknown`, including the two sourcing-shift intermediate values). The numeric export projection (`ADR-0014`) is deliberately not a schema field — it stays a generation-time computation, never hand-authored, consistent with `ADR-0014`'s "contributors never pick a number by hand" rule.
- `MappingStatus` — `candidate`/`reviewed`/`rejected` (concept-level `EditorialStatus` is separate from a single mapping's own status).
- `UncertaintyType` — the four values from `docs/INFORMATION_ARCHITECTURE.md` section 7.

Enum permissible-value names intentionally keep spaces and hyphens (e.g. `"direct quotation"`, `"close-match"`) rather than following LinkML's own `snake_case`/`PascalCase` naming-convention lint suggestions — `linkml-lint` flags this (`standard_naming` warnings, not errors) but round-trip fidelity to the exact strings already used across 17 Markdown files was judged more valuable than lint-style compliance. This is a deliberate choice, not an oversight.

One convention change from the Markdown status quo: Uncertainty items no longer encode "resolved" via inline `~~strikethrough~~`/prose in the `Type` cell (e.g. `~~uncertainty~~ **resolved 2026-07-01**`). The schema adds explicit `resolved` (boolean) and `resolved_date` fields instead.

## Validation Toolchain

LinkML, PyYAML, and RDFLib (pinned versions verified working as of 2026-07-05) are tracked in `scripts/requirements.txt` — install into a virtualenv, not system Python (this project's own "no build system, package manager... in the conventional sense" framing per `CLAUDE.md` still holds for the repository as a whole; this covers only the scripts under `scripts/`):

```bash
python3 -m venv /tmp/xwkont-scripts-venv && source /tmp/xwkont-scripts-venv/bin/activate
pip install -r scripts/requirements.txt

# Schema self-check (structural lint; standard_naming warnings on the
# deliberately-literal enum values above are expected and not defects):
linkml-lint data/crosswalks/schema/crosswalk-concept.yaml

# Validate a concept instance against the schema:
linkml-validate -s data/crosswalks/schema/crosswalk-concept.yaml data/crosswalks/<slug>/<slug>.yaml
```

`gen-json-schema data/crosswalks/schema/crosswalk-concept.yaml` also succeeds, confirming the schema is self-consistent LinkML (no undeclared slots, no broken class/slot/enum references).

## Migration Results: All 17 Concepts

Every `reviewed` concept in `docs/crosswalks/concepts/` (`object` first as a hand-authored test-fit, then all 17 via the script once it existed) now has a `data/crosswalks/<slug>/<slug>.yaml` record, and every one validates clean:

```
$ for f in data/crosswalks/*/*.yaml; do linkml-validate -s data/crosswalks/schema/crosswalk-concept.yaml "$f"; done
No issues found   (x17)
```

Row counts were checked programmatically against each Markdown source for all nine sections (Labels, Source Definitions, Correspondences, Comparison Notes, Mapping Assertions, Uncertainties, References, Review History, Future Work) across all 17 concepts, not spot-checked — per this project's own recorded practice of catching numeric-consistency errors by counting rather than inspection (`TODO.md`'s large-enumeration-document lesson). **Every count matches exactly; zero discrepancies found.**

`docs/crosswalks/concepts/*.md` files themselves were not touched by this migration — Markdown remains the human-facing published artifact (see Deferred).

## A Real Finding: Corpus Practice Already Diverges From `docs/INFORMATION_ARCHITECTURE.md`

Writing a mechanical parser against all 17 concepts (rather than hand-transcribing one, as the initial `object`-only pass did) surfaced drift a single-concept test-fit couldn't have found:

- **Claim types in Source Definitions.** IA restricts this section to `direct quotation`/`paraphrase` only. Actual practice across the corpus uses `editorial observation` (7 rows), `inference` (1 row), and a fifth value not documented anywhere in IA at all, `non-equivalence` (39 rows) — most commonly to record a verified *absence* of a source-ontology category (e.g. "full-text search... returned zero matches"). That's 47 of 212 Source Definitions rows (~22%) outside IA's stated two-value restriction. Resolved the same way `ADR-0013` resolved an analogous confidence-vocabulary drift: the schema's `ClaimType` enum now has five values, shared by both Source Definitions and Semantic Comparison Notes, rather than enforcing a restriction actual practice already exceeded at scale. **This is a finding for a maintainer decision** (whether to amend `docs/INFORMATION_ARCHITECTURE.md` itself), not one this schema/migration makes unilaterally.
- **Multi-reference cells.** `docs/adr/ADR-0009` and IA describe a `Reference`/`reference` field as if single-valued. In practice, 10 Correspondence rows and 7 Source Definitions rows cite two or three `xwkont:ref:*` records in one cell (e.g. a primary paper plus its OWL translation). The schema's `reference` slot is multivalued to match.
- **Strikethrough re-classification markup.** Three Semantic Comparison Notes rows (`event.md` note-003, `process.md` note-002, `quality.md` note-002) use `~~inference~~ **checked and unconfirmed, 2026-07-01**`-style markup to record that a claim's original classification was later revisited. The schema's `claim_type` field holds the unwrapped base value; a new optional `claim_type_annotation` field holds the revisiting note verbatim. Two Semantic Comparison Notes rows do the same for `confidence` (e.g. `high (verified directly against each source's own text)`); a matching `confidence_annotation` field was added.
- **One non-`xwkont:ref:*` provenance citation.** `continuant-occurrent.md`'s References list cites `ADR-0015` directly (the scope-expansion decision driving that crosswalk's own content buildout) alongside its normal `xwkont:ref:*` entries. The `reference_id` pattern now accepts both forms.
- **One free-text placeholder in `supporting_references`.** `proposition-content.md` note-003 cites `*(cross-cutting across this crosswalk and the other 8 0.2.0-batch concepts)*` instead of a specific reference, for a genuinely cross-cutting batch-level observation. `supporting_references` is no longer pattern-constrained for this reason.

None of these were silently normalized away or dropped — each is preserved in the migrated YAML and documented here and inline in the schema's own field descriptions, so a maintainer can decide whether `docs/INFORMATION_ARCHITECTURE.md` itself should be amended to match observed practice (the `ADR-0013` precedent) or whether some of this drift should instead be corrected in the source Markdown.

## Findings (Schema Fit)

- The schema holds all 17 concepts' content with **zero information loss** once the drift above was accommodated — every row, every free-text field, and every controlled-vocabulary value (including the five real deviations found) had a schema slot to land in.
- The nine-section Markdown structure and the nine-class LinkML structure remain a clean 1:1 correspondence at the table level; the divergences found were all within individual cell values, not structural.
- The `resolved`/`resolved_date` (Uncertainty), `claim_type_annotation`/`confidence_annotation` (Comparison Notes) fields are genuine structural improvements found during migration, not just transcription artifacts: each replaces prose-embedded markup with a real, independently-queryable field.

## Dry-Run Results: YAML → Markdown

`scripts/crosswalk-yaml-to-md.py` renders `data/crosswalks/<slug>/<slug>.yaml` back to Markdown and, by default (no `--write` flag), only diffs the result against the existing `docs/crosswalks/concepts/<slug>.md` — it has never overwritten any Markdown file. Building this renderer and diffing it against all 17 concepts (not just eyeballing one) is what actually validated the migration, catching real bugs a Markdown → YAML-only pass had no way to surface:

```bash
python3 scripts/crosswalk-yaml-to-md.py --summary      # one line per concept: IDENTICAL or DIFF (+n/-n)
python3 scripts/crosswalk-yaml-to-md.py <slug>          # full diff for one concept
python3 scripts/crosswalk-yaml-to-md.py --write <slug>  # actually overwrite -- not run in this pass
```

**Four real bugs found and fixed, not just cosmetic mismatches:**

1. **Silent content loss:** 12 of 17 concepts have a prose sentence trailing the Correspondences table (e.g. `abstract-concrete.md`: "No UFO or TUpper correspondence is recorded — see Source Definitions and Uncertainty."), which the original migration script never parsed at all — it only read the table, so this sentence existed in the Markdown but nowhere in the YAML. Fixed with a new `correspondences_note` field, migration script updated to capture it, all 17 re-migrated and re-validated.
2. **Data corruption, not just loss:** `strip_cell()` blindly stripped the first and last backtick off any cell that happened to start and end with one, which corrupts a cell containing *multiple* separately-backtick-wrapped tokens (e.g. `` `https://w3id.org/gfo/base/Property`, `Property_value`, `Value_space` `` in `quality.md`'s GFO correspondence) into a mangled string with stray backticks in the middle. Affected 9 files' `source_identifier_or_iri` cells. Fixed by only stripping when a cell has exactly one backtick pair; the renderer now also re-wraps bare single-token identifiers on the way back out, so both directions agree.
3. **Double-nested backticks on render:** the renderer's `join_refs()` unconditionally backtick-wrapped every item in a reference list, including the rare prose-placeholder fallback item that already contains its own backticks (`proposition-content.md` note-003's `*(cross-cutting ... `0.2.0`-batch ...)*`), producing a mangled double-backtick render. Fixed by only wrapping items that are actually a clean `xwkont:ref:*`/`ADR-NNNN` id.
4. **Fabricated markup for a bare `resolved` cell:** two Uncertainty rows in `situation-state-of-affairs.md` (`uncertainty-002`/`003`) have a Type cell that is literally just the word `resolved`, with no strikethrough/bold markup and no recoverable original `uncertainty_type`. The migration was storing this as a fake `resolution_note`, which made the renderer reproduce a fuller `~~uncertainty~~ **resolved**` form the original never had. Fixed by leaving `resolution_note` unset for this case, so the renderer reproduces the bare word.

**Residual, documented, not fixed** (all confirmed to be connector prose or formatting variants, not lost claims/evidence/mappings):

- Two Review History header variants exist in the corpus (`Review Event`/`Participant(s)` — used by the original 8 concepts — vs. `Review ID`/`Reviewer` — used by the 9 `0.2.0`-batch concepts and `TEMPLATE.md`); the renderer always emits the latter. Same for two placeholder-token styles for "no review ID yet" (`*(unreviewed)*` vs. `—`) — renderer always emits `—`. Column labels and placeholder tokens only; no data affected. This is now the only remaining difference in 16 of the 17 concepts.
- 6 rows across the corpus have short connector prose mixed into an otherwise-comma-separated reference list (e.g. `` `xwkont:ref:a`, confirmed against `xwkont:ref:b` directly ``, or `(all verified)` trailing a list). The migration extracts the `xwkont:ref:*` ids correctly but drops the connector phrase. Judged not worth a fifth annotation field for 6 rows of non-substantive text.
- One file (`continuant-occurrent.md`) has an intro sentence before its Mapping Assertions table; one file (`quality.md`) has a trailing bare paragraph (not a `- ` bullet) in Future Work. Both single-occurrence formatting quirks, not repeated patterns.

**Net result after all four fixes:** aggregate diff across all 17 concepts dropped from >600 changed lines to 97 (mostly the header/placeholder variant above, repeated per file) — on files totaling roughly 2,000 Markdown lines combined. Every one of the 17 YAML records still validates clean against the schema after these fixes.

## Deferred (Not Done by This Pass)

- **Amending `docs/INFORMATION_ARCHITECTURE.md`** to formally document the `ClaimType` five-value vocabulary, multi-reference cells, or the annotation-markup convention — left as a maintainer decision per "A Real Finding" above, not made by this pass.

## Addendum, 2026-07-05 (second pass): Both Previously-Deferred Items Now Done

The maintainer confirmed both items deferred above (trusting the Markdown renderer to write, and switching TSV/TTL generation to the YAML source) should happen now rather than stay deferred further.

**Markdown renderer trusted and run for real.** `python3 scripts/crosswalk-yaml-to-md.py --write` was run for all 17 concepts. Since the previous pass's fixes had already brought every concept to `IDENTICAL` against the renderer's dry-run output (re-confirmed with `--summary` immediately before writing), the aggregate diff from this write was **0 lines across all 17 files** — `git diff docs/crosswalks/concepts/` was empty after the write. `docs/crosswalks/concepts/*.md` is now a real generated artifact, not hand-maintained; the residual Review History header/placeholder cosmetics and connector-prose gaps documented above under Dry-Run Results had already been absorbed into the committed Markdown by the time this pass ran, so there was nothing left to change.

**TSV/TTL generation switched to YAML, nested layout.** `scripts/crosswalk-to-sssom-tsv.py` now parses `data/crosswalks/<slug>/<slug>.yaml` directly (via PyYAML, no LinkML runtime dependency) instead of the Markdown Mapping Assertions table, and writes `data/crosswalks/<slug>/<slug>.tsv` (nested) instead of the flat `data/crosswalks/<slug>.tsv`. `scripts/sssom-tsv-to-ttl.py` likewise now reads/writes the nested `data/crosswalks/<slug>/<slug>.{tsv,ttl}` paths; its TSV-to-RDF logic is unchanged. Both scripts' docstrings now cite ADR-0024 (YAML SSOT) rather than ADR-0023 alone. The old flat `data/crosswalks/<slug>.tsv`/`.ttl` files were removed (`git rm`) and regenerated fresh in the nested layout.

All 17 concepts regenerated cleanly with both scripts (`--check` passes on both afterward, confirming idempotency). Diffing each new nested TSV against its prior flat version found exactly one systematic difference, confined to the `xwkont_provenance` column: the old Markdown-table parser's `strip_cell()` only stripped a leading/trailing backtick pair from the *whole joined cell*, leaving stray internal backticks in any cell citing more than one reference (e.g. `` xwkont:ref:bfo-2020`, `xwkont:ref:dolce-wonderweb-d18 ``, cf. Dry-Run Results bug #2 above, which fixed the analogous bug in the Markdown renderer but the flat TSV script was never patched to match). Reading each reference id directly out of the YAML's `provenance` list and joining with `", "` produces the clean form (`xwkont:ref:bfo-2020, xwkont:ref:dolce-wonderweb-d18`) with no stray backticks. Verified column-by-column across all 17 files: columns 1–10 are byte-identical between old flat and new nested TSVs; column 11 differs only by this backtick artifact (confirmed by stripping backticks from the old value and diffing against the new — zero remaining mismatches). All 17 TTL files are **byte-identical** old-vs-new (the Turtle builder never touches the provenance column), so only their file location changed.

No LinkML-vs-Markdown-vs-old-TSV data discrepancy requiring a judgment call was found beyond the backtick artifact above, which is a bug-fix (same underlying data, corrected serialization), not a genuine content conflict.

**New runtime dependency note: PyYAML.** `scripts/crosswalk-yaml-to-md.py` (prior pass) and `scripts/crosswalk-to-sssom-tsv.py` (this pass) both `import yaml` directly — this is a lighter dependency than the full LinkML toolchain (no schema validation happens in either script, just structured reads), but it is a real dependency beyond the RDFLib-only baseline `docs/publication/validation-commands.md` currently documents. Confirmed: PyYAML is **not** present in this machine's system Python (blocked from installing via `pip` by Homebrew's PEP 668 externally-managed-environment guard); verifying these scripts required building a throwaway venv, the same pattern this document already recommends for LinkML itself.

## Addendum, 2026-07-05 (third pass): dependency-pinning file added

`scripts/requirements.txt` now tracks `linkml==1.11.1`, `PyYAML==6.0.3`, and `rdflib==7.6.0` — the exact versions verified working in this pass's throwaway venv. This closes both previously-deferred dependency items (the LinkML pinning file and the smaller PyYAML note above) with a single file, per `ADR-0024`'s own trade-off note that the project's "no build system" framing "will need updating... not glossed over." The pinning is scoped to `scripts/` tooling only — `docs/publication/validation-commands.md`'s repository-wide validation commands still assume only RDFLib, which remains true (its own commands never import `linkml` or `yaml`).
