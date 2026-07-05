# ADR-0018: Commit to Comprehensive Crosswalk-Concept Coverage, Staged via Minor Releases

- **Status:** Accepted
- **Date:** 2026-07-04

## Context

External review asked whether XwkOnt's existing eight crosswalk concepts (Continuant/Occurrent, Object, Event, Process, Role, Quality, Relation, Information Artifact) are considered complete for a `v1` release, whether the project intends to stay a small curated set, and what would justify accepting a new concept in the future. No prior repository artifact answered this — `docs/FOUNDING_PRINCIPLES.md` and `docs/ARCHITECTURAL_PRINCIPLES.md` describe an open-world posture in general terms (new material can always be incorporated) but do not state a position on the trajectory of concept-set *size*.

Separately, `docs/evaluations/foundational-ontology-concept-terms-matrix.md` built a primary-source-verified tree of each of the eight source ontologies' own top-level categories, and `TODO.md` derived a ranked, source-count-scored candidate-concept queue from it (originally 6 items, extended to 19 after review). A further exhaustive pass across every class named in that matrix (roughly 250+ raw class names across the eight hierarchies) confirmed the 19-item queue already captures the real cluster structure — most remaining raw classes are sub-species of an already-clustered concept, not evidence of additional undiscovered top-level concepts.

## Decision

XwkOnt's crosswalk-concept set is **not** considered complete at eight, and is **not** intentionally capped at a small curated size. The long-run goal is comprehensive coverage of the candidate space surfaced by `docs/evaluations/foundational-ontology-concept-terms-matrix.md` (currently 19 ranked candidates, itself expected to grow as new source ontologies or matrix passes surface more).

Coverage growth is staged incrementally, one `MINOR` version bump at a time (`docs/governance/release-versioning-policy.md`'s existing definition: "New terms, mapping structures, publication capabilities, or reviewed crosswalk scope"), not delivered as one large batch. Each concept added to a batch still goes through its own selection/sourcing/scoping/review pass — a matrix ranking is a **candidate justification**, not a shortcut past `docs/governance/contributing.md`'s existing per-concept process.

**First batch, targeting release `0.2.0`:** the nine candidates in the matrix-derived queue with a recognizable counterpart in at least three of the eight source ontologies — Time, Spatial Region/Space, Abstract vs. Concrete, Quantity/Amount of Matter, Situation/State of Affairs, Mereology/Parthood/Aggregate, Universal/Type, Boundary/Site, and Proposition/Content. The remaining ten queued candidates (two-source and one-source items) stay queued for later batches; no specific future release number is assigned to them by this decision.

**Concept-admission bar, going forward:** a candidate's source-count ranking in the class hierarchy matrix is the primary evidence for admitting it into a batch. The project's original seven-point concept-selection checklist (source accessibility, session-sized scope, likelihood of revealing real semantic differences, citability, template fit, etc. — see `TODO.md`) remains in force as secondary, per-concept scoping guidance — it decides whether a matrix-justified candidate is actually ready to be worked in a given session, not whether it belongs in the candidate space at all. That checklist's criterion #1 ("appears in, or has an identifiable counterpart in, multiple target foundational ontologies") is superseded by the matrix's own quantitative source-count evidence for any candidate already listed in `TODO.md`'s queue; it retains its original, narrower role only for concepts not yet run through the matrix.

## Scope

This decision does not select, source, or scope any of the nine `0.2.0`-batch concepts individually — each still requires its own session-sized selection/sourcing/scoping/review pass, the same process the original eight concepts went through. It does not reopen `ADR-0017`'s exclusion of Reality (Reality is not a Concept in the `ADR-0011` sense at all, regardless of matrix source-count, so this ADR's staging logic does not apply to it). It does not change the crosswalk template, the source-ontology roster (`ADR-0015`), or any existing `reviewed` crosswalk content.

## Rationale

Committing to comprehensive coverage, rather than declaring the current eight "done" or "intentionally small," follows directly from `docs/ARCHITECTURAL_PRINCIPLES.md`'s open-world philosophy and from what the class hierarchy matrix itself shows: every one of the eight source ontologies commits to dozens of top-level categories beyond the eight XwkOnt currently crosswalks, and there is no principled reason (beyond session-sized sequencing) to treat the original eight as a natural stopping point rather than the first tranche of a larger, evidence-ranked backlog.

Staging growth through ordinary `MINOR` releases, rather than announcing a fixed target concept count, keeps the decision compatible with `docs/governance/release-versioning-policy.md` as already written (no new versioning rule needed) and keeps each batch small enough to go through the same per-concept rigor (selection, primary-source citation, review-to-`reviewed`) the original eight received, rather than trading rigor for speed once a larger total is committed to.

Anchoring the admission bar in the matrix's source-count evidence, rather than re-running the original seven-point checklist's harder-to-verify criteria (methodological centrality, likelihood of revealing real semantic differences) for every future candidate, directly answers external review's "concept selection feels arbitrary" concern with a reusable, checkable number instead of a judgment call made fresh each time.

## Consequences

### Positive

- Gives a citable, evidence-based answer to "is the concept set finished?" and "what would justify adding a new one?" — both previously undocumented.
- Converts the `TODO.md` candidate queue from an inert backlog into an actual release plan, with a named next batch.
- Reuses the existing `MINOR`-release definition rather than inventing new versioning machinery.

### Trade-offs

- Nine concepts is a substantially larger commitment than any single prior batch (the original eight were built one or a few at a time across many sessions); scoping and reviewing all nine to the same rigor will take multiple sessions, not one.
- A quantitative source-count bar can admit a candidate that turns out, on closer sourcing, to be a weaker fit than its ranking suggested (the same risk criterion #1's original wording was flagged for) — this ADR accepts that risk in exchange for a checkable process, consistent with `TODO.md`'s existing note that even reworded criteria stay a judgment call, not a bright line.
- Committing to eventual comprehensive coverage raises the long-run maintenance surface (more crosswalks to keep in sync with source-ontology updates) — partially addressed by this session's separate source-ontology version re-check commitment in `docs/governance/release-versioning-policy.md`, but not eliminated.

## References

- `docs/evaluations/foundational-ontology-concept-terms-matrix.md`
- `TODO.md` (candidate-concept queue)
- `docs/governance/release-versioning-policy.md`
- `docs/governance/contributing.md`
- `docs/adr/ADR-0011-adapt-iso-1087-concept-as-organizing-unit.md`
- `docs/adr/ADR-0015-expand-source-ontology-scope-to-eight.md`
- `docs/adr/ADR-0017-exclude-reality-as-a-crosswalk-concept.md`
- `docs/ARCHITECTURAL_PRINCIPLES.md`
