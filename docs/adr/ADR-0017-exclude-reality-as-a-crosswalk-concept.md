# ADR-0017: Exclude "Reality" as a Standalone Crosswalk Concept

- **Status:** Accepted
- **Date:** 2026-07-03

## Context

An external reviewer, exploring XwkOnt's design decisions rather than proposing a change, asked why "Reality" is not among XwkOnt's crosswalk concepts (Object, Event, Process, Role, Quality, Relation, Information Artifact — plus Continuant/Occurrent), whether the exclusion is intentional, and how BFO/DOLCE/UFO/SUMO/etc. each treat Reality. No prior repository artifact answered this directly; it had never been decided one way or the other.

`ADR-0011` already establishes that XwkOnt's organizing unit is **Concept** in the ISO 1087 / SKOS sense: a language- and source-independent unit of thought that multiple source ontologies each give their own term for (BFO's "Continuant," DOLCE's "Endurant"). `ADR-0010` already establishes a `philosophical` dimension field on every crosswalk's Source Definitions and Semantic Comparison tables, specifically to record a source ontology's metaphysical/theoretical commitments (realism vs. conceptualism, stance on universals, cognitive/linguistic orientation) separately from its technical representation.

## Decision

XwkOnt SHALL NOT create a standalone "Reality" crosswalk concept.

Reality is not a **Concept** in the `ADR-0011` sense — it is not a nameable unit of thought that different source ontologies classify or relate differently the way Object, Event, or Role are. It is the metaphysical presupposition each source ontology's entire category system sits on top of (e.g., BFO's realist commitment that "universals have real particulars as their instances"; DOLCE's cognitive/linguistic orientation toward how language and common sense already categorize the world). A source ontology does not have a class called "Reality" to crosswalk against another source's class called "Reality" — it has a background stance on whether/how reality exists mind-independently, which conditions every one of its actual categories at once.

`ADR-0010`'s `philosophical` dimension field already exists to capture exactly this, per source ontology, distributed across every concept crosswalk where the source's own documentation discusses its theoretical grounding — rather than concentrated in one artificial "Reality" entry.

## Scope

This ADR does not change the crosswalk template (`ADR-0007`, amended by `ADR-0009` and `ADR-0010`), the concept-selection criteria used to admit past or future concepts, or any existing crosswalk content. It settles one specific inclusion/exclusion question raised by external review; it does not establish a general test for admitting or excluding other candidate concepts (e.g., Time, Agent, Function) — those remain open and are not resolved by this decision.

## Rationale

Treating "Reality" as its own crosswalk concept would require XwkOnt to assert that "reality" is itself a comparable class each source ontology defines and can be mapped against — which is not true of any of the eight source ontologies (`ADR-0015`) and would mean inventing a category that does not exist in the source material, contrary to Source First (`docs/ARCHITECTURAL_PRINCIPLES.md` Principle 4). It would also risk XwkOnt taking an implicit position on realism versus conceptualism by the mere act of giving "Reality" a single crosswalk entry with one settled definition — the opposite of Neutrality (Principle 6), which requires XwkOnt to document philosophical disagreement, not resolve it.

`ADR-0010`'s `philosophical` dimension field is the correct existing mechanism for this material: it lets each concept crosswalk (Object, Event, etc.) show why a source ontology's technical representation is the way it is, tied to that source's own stance on reality/existence, exactly where it's relevant to that concept — rather than a duplicate, decontextualized "Reality" artifact competing with it.

## Consequences

### Positive

- Closes a specific, recurring external-review question ("why no Reality crosswalk?") with a citable, principled answer instead of silence or an ad hoc reply.
- Reinforces, rather than duplicates, `ADR-0010`'s existing philosophical-dimension mechanism.
- Establishes a reusable distinction — Concept (nameable, cross-source unit of thought) versus metaphysical presupposition (background stance conditioning all of a source's concepts) — that can be applied if a similar question arises for another abstract candidate.

### Trade-offs

- Does not itself resolve whether "Time" or any other candidate concept should be included or excluded; a separate decision is needed if that question is taken up.
- Relies on crosswalk authors actually populating `philosophical`-dimension rows where relevant (per `ADR-0010`, this is a SHOULD, not a MUST, and may be legitimately sparse for engineering-first sources) — if that population is inconsistent, the claim that "Reality is covered via the philosophical dimension" is weaker in practice than in principle. Not evaluated by this ADR.

## References

- `docs/adr/ADR-0010-distinguish-technical-and-philosophical-dimensions.md`
- `docs/adr/ADR-0011-adapt-iso-1087-concept-as-organizing-unit.md`
- `docs/adr/ADR-0015-expand-source-ontology-scope-to-eight.md`
- `docs/ARCHITECTURAL_PRINCIPLES.md` (Principle 4, Source First; Principle 6, Neutrality)
