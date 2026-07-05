# ADR-0024: LinkML-Schema-Validated Data as SSOT for Crosswalk Concepts; Markdown/TSV/TTL Generated

- **Status:** Accepted
- **Date:** 2026-07-05

## Context

### Why this reopens a decision made the same day

`ADR-0007` established Markdown (`docs/crosswalks/concepts/*.md`) as the canonical, human-authored record for a crosswalk concept. `ADR-0023`, decided earlier in this same session, kept that unchanged and added a narrower decision on top: `data/crosswalks/*.tsv` (SSSOM-conformant) would be the machine-readable SSOT for one section of a crosswalk — its Mapping Assertions table — generated *from* the Markdown, with RDF/Turtle generated one step further from the TSV. At the time, that was a reasonable scope: 17 concepts existed, all human/agent-authored and reviewed one at a time, with no stated plan to change how concepts get authored going forward.

That premise changed within the same session, not because the earlier reasoning was wrong for its scope, but because new information changed the actual scale in play: an internal candidate-concept inventory (not itself a public repository artifact) records **540 candidate crosswalk concepts** total, and the maintainer's explicit intent is to delegate crosswalk authoring to AI agents to make working through that backlog tractable. Revisiting `ADR-0023`'s direction on the same day it was made is not indecision for its own sake — it is `docs/ARCHITECTURAL_PRINCIPLES.md`'s own Open-World Philosophy ("assumes knowledge evolves") applied honestly: the 17-concept, single-author-at-a-time premise `ADR-0023` was scoped against no longer describes the actual near-term plan, so the decision built on that premise needed re-examining before more concepts were built against it, not after.

### What changed the analysis

Two things, considered directly rather than assumed:

1. **Reviewability does not scale the way `ADR-0007` assumed.** `TODO.md` already records a concrete failure at far smaller scale than 540: a 3-pass audit of internal working documents (including the candidate-concept inventory itself) found a headline total undercounting its own row count by 3, a "most/large majority" prose claim contradicted by the actual verified count (51 of 193, ~26%), and a status-summary table claiming 14 resolved items while listing 13 — all shipped in already-committed files, caught only by an ad hoc audit, not by any built-in check. At 17 concepts, a human review pass (`docs/governance/contributing.md`'s Review Checklist) could plausibly catch this class of error by inspection. At 540, relying on the same unaided human-inspection process is not a credible plan.

2. **"Prose-heavy content forces Markdown-first" was a false tradeoff.** Structured, schema-validated data does not mean flattening long-form content into short atomic fields — a schema can define a field as an arbitrarily long text block (a quotation, a rationale, an uncertainty narrative) exactly as free-form as it is today. What a schema adds is *validation* of the metadata around that prose (does this reference identifier resolve, is this confidence value one of the six allowed categories, is this claim type one of the four defined types, are correspondence/mapping IDs sequential with no gaps) — mechanically, for every concept, before a human reviewer ever looks at it. This is not a reason to prefer Markdown; if anything it is a reason a schema-validated format should have been considered from `ADR-0007` onward, and is now being adopted once the actual cost of not having it (540 concepts, delegated authorship) is concrete enough to justify the tooling investment.

### Why LinkML, specifically ("Reuse Before Introduce")

Per `FOUNDING_PRINCIPLES.md`'s "Reuse Before Introduce," the standard/tooling question was checked before deciding to introduce a new one. **SSSOM itself — already adopted by `ADR-0009` — is defined in LinkML** (Linked Data Modeling Language, `linkml/linkml`): its metaschema, validators, and generators (Markdown documentation, JSON Schema, SHACL, RDF/OWL, SQL DDL) all come from that toolchain. Adopting LinkML for the crosswalk-concept schema is not introducing a new paradigm alongside SSSOM; it completes the same stack the project already stands partly on. No separate schema-definition language was evaluated as a serious alternative for this reason — LinkML is the one already load-bearing one step removed.

## Decision

1. **A single LinkML schema SHALL model the full crosswalk-concept record** — all nine sections `docs/INFORMATION_ARCHITECTURE.md` currently defines for Markdown crosswalks (Scope Note; Labels/Alternate Labels/Source Terminology; Source Definitions and Contextual Notes; Source Ontology Correspondences; Semantic Comparison Notes; Mapping Assertions; Uncertainty/Non-Equivalence/Open Questions; Provenance and References; Review History and Future Work). Long-form fields (quotations, rationale, uncertainty narrative, scope prose) remain arbitrary-length text fields in the schema — this is a schema for validating structure and controlled vocabulary, not for shortening prose.

2. **Each concept gets one directory, not flat files:** `data/crosswalks/<slug>/`, containing:
   - `<slug>.yaml` — the LinkML-conformant structured record. This is the only hand/agent-authored file and is the SSOT for the concept as a whole.
   - `<slug>.tsv` — generated SSSOM mapping-assertions export (superseding `ADR-0023`'s flat `data/crosswalks/<slug>.tsv` path).
   - `<slug>.ttl` — generated RDF mapping graph (superseding `ADR-0023`'s flat `data/crosswalks/<slug>.ttl` path).

   Grouping every representation of one concept together scales to 540 concepts far better than one flat directory of 1,000+ files, and makes a single concept a self-contained unit of delegated work: one folder in (the YAML), a fixed set of generated outputs out.

3. **`docs/crosswalks/concepts/<slug>.md` becomes generated output**, rendered from `<slug>.yaml` (LinkML's own documentation generation, or a thin template pass over the validated data — an implementation choice left open per point 6 below). It remains in `docs/crosswalks/concepts/`, not moved into the per-concept data folder, since it is still the human-facing published artifact `docs/` already exists to hold and link from.

4. **`ADR-0007`'s designation of Markdown as canonical for crosswalk-concept artifacts is superseded by this ADR.** The YAML record is now canonical; Markdown, TSV, and Turtle are all generated projections of it, regenerated whenever the YAML changes, the same "stale generated output is a validation failure, not a merge conflict" rule `ADR-0023` already established for TSV→TTL now applies uniformly to YAML→Markdown/TSV/TTL.

5. **`ADR-0009`'s predicate/justification/confidence vocabulary and `ADR-0014`'s numeric confidence projection are not reopened.** They become enum/field definitions inside the LinkML schema rather than prose conventions documented only in `docs/methodology/crosswalk-methodology.md` — the vocabulary itself is unchanged, only where it is formally declared changes.

6. **The schema's exact field-by-field design, the Markdown-rendering mechanism, and the migration of the 17 already-`reviewed` concepts from Markdown-first to YAML-first are deferred to implementation**, not fixed by this ADR — consistent with how `ADR-0023` deferred its own generation-script specifics. This ADR fixes the SSOT relationship (YAML canonical; Markdown/TSV/TTL generated), the tooling foundation (LinkML), and the file-layout pattern (per-concept directory); it does not fix a schema file, a generator implementation, or a migration script.

## Scope

This ADR supersedes `ADR-0007`'s Markdown-canonical decision **for crosswalk-concept artifacts specifically** (`docs/crosswalks/concepts/*.md` / `data/crosswalks/`). It does not extend to other Markdown artifact classes `ADR-0007`/`ADR-0002` cover elsewhere in the repository — ADRs themselves, reference records (`docs/references/`), governance and methodology documentation, and session journal entries all remain Markdown-authored and canonical as-is; nothing about this ADR implies those should also move to a schema-first model, and no case for that has been made. It supersedes `ADR-0023`'s flat `data/crosswalks/<slug>.tsv`/`<slug>.ttl` file-layout naming (now nested under `data/crosswalks/<slug>/`) and its statement that the TSV is generated from Markdown (now: generated from YAML, with Markdown itself also generated from YAML, as a sibling output rather than the TSV's source). It does not reopen `ADR-0009`, `ADR-0013`, or `ADR-0014`'s vocabulary decisions, and does not resolve the previously-deferred UUID/identifier-scheme question (`TODO.md`, checked and closed 2026-07-05) — `subject_id`/`object_id` conventions established there carry over unchanged into the LinkML schema's corresponding fields.

## Rationale

The core justification is the same "Reuse Before Introduce" reasoning already applied to SSSOM/SEMAPV (`ADR-0009`) and to the SSSOM RDF vocabulary (`ADR-0023`), extended one layer further: rather than inventing a bespoke schema language, validator, and Markdown-generation approach for crosswalk concepts, this adopts the schema toolchain the project's own already-adopted mapping standard is itself built on. The per-concept directory layout is a direct, unavoidable consequence of scale (540 candidates vs. 17 built) rather than a stylistic preference. Reversing `ADR-0007` rather than layering a second machine-readable format on top of Markdown (the `ADR-0023` pattern) is justified specifically because `ADR-0023`'s pattern only worked for the one section (Mapping Assertions) that was already naturally tabular — extending that same "TSV mirrors Markdown" pattern to all nine sections would mean maintaining full parity between two independently hand-editable representations of the *entire* record, which is a materially worse drift risk than the single-section case `ADR-0023` accepted.

## Consequences

### Positive

- Every crosswalk concept gains mechanical validation (reference resolution, controlled-vocabulary compliance, ID sequentiality, required-field completeness) at authoring time, closing the exact gap that produced the row-count and total errors `TODO.md` already recorded.
- A single per-concept YAML file is a clean, self-contained unit to delegate to an AI agent — schema validation gives the agent (and the reviewer) an immediate, mechanical pass/fail signal before human review, rather than a Review Checklist applied only after the fact.
- Markdown, TSV, and Turtle all stay in lockstep by construction (all generated from one source), removing the two-copies-can-drift risk `ADR-0023` had accepted for the one section it covered.
- Builds directly on tooling the project already depends on indirectly (LinkML underlies SSSOM), rather than introducing an unrelated new dependency.

### Trade-offs

- LinkML is a materially heavier dependency than the plain `rdflib` used for `ADR-0023`'s TSV→TTL generator — this is a real, larger commitment for a repository that otherwise describes itself as having "no build system, package manager... in the conventional sense." That framing will need updating once this is implemented, not glossed over.
- The 17 already-`reviewed` concepts need a migration pass (Markdown → YAML, verified for full-fidelity round-trip) before they're on the new model; until that migration happens, this ADR's decision and the repository's actual state are not yet consistent, the same "decided but not yet implemented" gap `ADR-0018` and others have carried before.
- The full schema design is nontrivial: nine sections, several free-text-plus-controlled-vocabulary hybrid fields, and citation/claim-typing rules that must be exactly as expressive in YAML as they are today in Markdown prose — a real design task, not a mechanical transcription, and not yet done.
- Contributors and reviewers now review structured YAML (or its rendered Markdown, or both) rather than editing Markdown directly — a workflow change worth testing on one concept before applying to the full backlog.

## References

- `docs/adr/ADR-0007-adopt-information-architecture-for-crosswalk-artifacts.md`
- `docs/adr/ADR-0009-adapt-sssom-for-mapping-assertions.md`
- `docs/adr/ADR-0014-fixed-numeric-projection-for-confidence-export.md`
- `docs/adr/ADR-0023-machine-readable-crosswalk-export-sssom-tsv-generated-ttl.md`
- `docs/INFORMATION_ARCHITECTURE.md`
- `TODO.md` (recorded numeric-consistency-check gap; closed UUID/identifier-scheme question)
- LinkML: <https://linkml.io/>, <https://github.com/linkml/linkml>
- SSSOM's LinkML schema: <https://github.com/mapping-commons/sssom/blob/master/src/sssom_schema/schema/sssom_schema.yaml>
