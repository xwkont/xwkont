# ADR-0023: Machine-Readable Crosswalk Export — SSSOM/TSV as SSOT, Generated Turtle

- **Status:** Accepted
- **Date:** 2026-07-05

## Context

`ADR-0009` adapted SSSOM's predicate and justification vocabulary for mapping assertions recorded in each crosswalk's Markdown Mapping Assertions table, but its point 4 explicitly declined to adopt SSSOM's TSV serialization "at this time," reasoning that no real mapping content existed yet to justify committing to an export format. It named SSSOM/TSV as the format any future export SHOULD target, rather than a bespoke serialization.

`TODO.md` has long tracked the resulting trigger conditions: a full mapping-record/SKOS-property usage guide and tooling (including a crosswalk visualizer, `TODO.md` "Publication & Release" section) become required "once reviewed public crosswalk mappings, public machine-readable mapping exports, accepted mapping assertions, or non-illustrative public SKOS mapping-property use are introduced." As of this ADR, all 17 planned crosswalk concepts (`docs/crosswalks/concepts/`) have reached `reviewed` status. `data/crosswalks/` currently contains only a `.gitkeep` placeholder — no real machine-readable content exists yet.

Two questions were open: (1) whether the "not at this time" condition in `ADR-0009` point 4 still holds now that 17 reviewed crosswalks exist, and (2) whether a machine-readable export should be SSSOM/TSV only, a hand-authored parallel RDF/Turtle vocabulary, or something else — given XwkOnt is otherwise an RDF-artifact project (`data/ontology/core.ttl`).

## Decision

1. **The condition in `ADR-0009` point 4 no longer holds.** With all 17 crosswalk concepts `reviewed`, XwkOnt SHALL begin producing a machine-readable mapping export, populating `data/crosswalks/` for real.

2. **SSSOM/TSV is the single source of truth (SSOT).** Each concept's mapping assertions SHALL be recorded as one SSSOM-conformant TSV mapping set under `data/crosswalks/` (one file per concept, named after the concept slug, e.g. `data/crosswalks/object.tsv`), using the `predicate_id`, `mapping_justification`, and other fields `ADR-0009` and `ADR-0014` already define. This TSV is hand/agent-authored and is the canonical machine-readable record — it is derived from, and must stay consistent with, each concept's Markdown Mapping Assertions table, which remains the canonical human-readable record per `ADR-0007`.

3. **RDF/Turtle is a generated, non-canonical export of the TSV**, not a second hand-authored artifact. It SHALL be produced using SSSOM's own defined RDF/OWL representation of a mapping set (the `sssom:` vocabulary at `https://w3id.org/sssom/schema/`), not a bespoke XwkOnt mapping vocabulary — this is a direct application of "Reuse Before Introduce": XwkOnt does not need to invent RDF predicates for concepts SSSOM already models. Generated Turtle files live alongside their source TSV (e.g. `data/crosswalks/object.ttl`, generated from `data/crosswalks/object.tsv`) and are regenerated whenever the TSV changes; a generated `.ttl` that is stale relative to its `.tsv` is a validation failure, not a merge conflict to hand-resolve.

4. **Generated crosswalk Turtle stays separate from `core.ttl`.** `data/ontology/core.ttl` continues to hold only XwkOnt's own core concepts and properties (`xwkont-core:` classes/properties, per `ADR-0020`). Crosswalk mapping graphs are a distinct set of files whose subjects are `xwkont:concept:<slug>` IRIs (already minted per `docs/INFORMATION_ARCHITECTURE.md`) and whose objects are external source-ontology term IRIs — related via SSSOM/SKOS predicates. `core.ttl` does not grow as crosswalks gain machine-readable form, and this pattern is expected to scale directly as further concepts (beyond the current 17) or further source ontologies (beyond `ADR-0015`'s eight) are added: one TSV + one generated TTL per concept, not a monolithic file.

5. **The generation step itself (script, its location, invocation, and validation) is deferred to implementation and is not specified by this ADR.** This ADR fixes the SSOT relationship (TSV canonical, TTL generated using SSSOM's own RDF vocabulary) and the file-layout pattern (per-concept, alongside `core.ttl` but not merged into it); it does not fix a specific script path, language, or CI wiring.

## Scope

This ADR acts on `ADR-0009` point 4's own deferred condition ("if a machine-readable mapping export is implemented in the future, it SHOULD target SSSOM/TSV") — it does not reopen `ADR-0009`'s predicate/justification/confidence decisions, `ADR-0013`'s confidence vocabulary, or `ADR-0014`'s numeric export projection, all of which apply unchanged to the new TSV export. It does not change `ADR-0007`'s Markdown-as-canonical-human-readable-record decision. It does not resolve the separate open identifier-scheme question tracked in `TODO.md` (whether each `data/crosswalks/` entry additionally needs an RFC 4122 UUID beyond the existing `xwkont:mapping:<concept-slug>:<nnn>` identifier) — that remains open and is not required to proceed with this ADR's TSV/TTL decision.

## Rationale

Adopting SSSOM/TSV as canonical rather than inventing a bespoke tabular or RDF format is the direct continuation of the "Reuse Before Introduce" reasoning `ADR-0009` already established for predicates and justification — extending it to serialization is not a new kind of decision, just closing out the one `ADR-0009` explicitly deferred. Generating Turtle from the TSV via SSSOM's own RDF vocabulary, rather than hand-authoring a second XwkOnt-specific mapping schema in parallel, avoids maintaining two independently-authored representations of the same facts (a drift risk with no corresponding benefit) while still giving XwkOnt a queryable RDF form consistent with its identity as an RDF-artifact project and with `ADR-0004`'s RDF/SKOS adoption.

## Consequences

### Positive

- `data/crosswalks/` gains real, standard-conformant machine-readable content, unblocking the `TODO.md`-tracked mapping-record/SKOS-property usage guide and crosswalk-visualizer work.
- One canonical machine-readable file per concept (the TSV) avoids drift between a hand-authored TSV and a hand-authored TTL — the TTL is mechanically derived and regenerable.
- Reusing SSSOM's own RDF vocabulary means XwkOnt does not need to design, document, or maintain a bespoke crosswalk-mapping ontology.
- The per-concept file pattern scales cleanly as concept count or source-ontology count grows, without `core.ttl` itself growing.

### Trade-offs

- A generation step (script or tool) now needs to exist and be kept working; a stale generated `.ttl` is a new class of validation failure contributors need to know to check for (see `docs/publication/validation-commands.md`, to be updated when the generator is implemented).
- Contributors and delegated agents authoring mapping content now work primarily in TSV rather than directly in Markdown or Turtle, which is a different authoring surface than any existing XwkOnt artifact class.
- This ADR does not itself resolve the `TODO.md` UUID-scheme question; whoever implements `data/crosswalks/` content next should check it explicitly rather than assume TSV `subject_id`/`object_id` fields settle it by default.

## References

- `docs/adr/ADR-0007-adopt-information-architecture-for-crosswalk-artifacts.md`
- `docs/adr/ADR-0009-adapt-sssom-for-mapping-assertions.md`
- `docs/adr/ADR-0013-extend-confidence-vocabulary-with-intermediate-values.md`
- `docs/adr/ADR-0014-fixed-numeric-projection-for-confidence-export.md`
- `docs/adr/ADR-0015-expand-source-ontology-scope-to-eight.md`
- `docs/adr/ADR-0020-define-core-as-base-module-not-domain-tier.md`
- `docs/evaluations/meta-ontology-standards-evaluation.md`
- `TODO.md` (machine-readable-export trigger; UUID-scheme open question)
- SSSOM specification: <https://mapping-commons.github.io/sssom/>
- SSSOM RDF/OWL schema: <https://w3id.org/sssom/schema/>
