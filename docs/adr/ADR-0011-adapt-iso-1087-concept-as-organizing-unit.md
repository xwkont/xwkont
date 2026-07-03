# ADR-0011: Adapt ISO 1087 Concept/Term Distinction; Justify "Concept" as XwkOnt's Organizing Unit

- **Status:** Accepted
- **Date:** 2026-07-01

## Context

`ARCHITECTURAL_PRINCIPLES.md` Principle 3 ("Concept-Centric") already states that XwkOnt organizes around concepts rather than ontologies, and `ADR-0004`/`ADR-0007` already operationalize this (`skos:Concept`, `xwkont:concept:<slug>`, a template section separating "Labels, Alternate Labels, and Source Terminology" from the concept itself). None of this was previously justified against how the wider ontology ecosystem names its own organizing unit, or against a terminology-science standard for the concept/term distinction itself.

A candidate alternative, "Term," was considered and rejected in discussion: a crosswalk's purpose is to relate *multiple different source terms* (e.g., BFO's "Continuant," DOLCE's "Endurant") to a shared comparison point. If "Term" were the organizing unit, one source's term would have to be picked as the reference frame, implicitly privileging that source's vocabulary — a Neutrality (Principle 6) and Source First (Principle 4) violation.

This ADR does two things: (1) adapts **ISO 1087** (the vocabulary-of-terminology-work standard) to formally justify the Concept/Term split already implicit in the template, and (2) records a survey of how comparable ontology/terminology systems name their own organizing unit, to justify "Concept" as the correct choice rather than an arbitrary one.

## Survey: How Other Systems Name Their Organizing Unit

| System | Term used | What it implies |
|---|---|---|
| ISO 1087 (terminology-work vocabulary) | **Concept** (distinct from Term/Designation) | A unit of thought, language- and source-independent; a term is a linguistic designation *for* a concept. This is the standard XwkOnt's Concept/Term split is adapted from. |
| SKOS (already adopted, `ADR-0004`) | **Concept** (`skos:Concept`) | Same neutral, cross-vocabulary unit; SKOS was purpose-built to map between different classification systems' terms without asserting any one as authoritative — directly analogous to a crosswalk's job. |
| Description Logic (the formal foundation OWL is built on) | **Concept** | DL's native vocabulary; OWL's "Class" is the same notion renamed for a different audience. Confirms "Concept" already has long standing in formal ontology itself, not just library/terminology science. |
| OWL / RDFS | **Class** | Carries formal set-membership semantics (instances, domain/range, subsumption axioms) — a heavier formal commitment than XwkOnt's conservative RDF/RDFS/SKOS scope (`ADR-0004`) intends by default. |
| BFO | **Universal** (encoded as `owl:Class`, but the theory itself is described as "a taxonomy of universals that have real particulars as their instances") | A specific philosophical (realist) metaphysical claim: universals exist mind-independently. |
| UFO | **Universal** (further typed via OntoUML stereotypes: Kind, Role, Phase, Mixin, etc.) | Same realist tradition as BFO, elaborated into a typology. |
| SUMO | **Class** | Frame/KIF-style class, closer to OWL/DL "Class" than to a philosophical "Universal." |
| Cyc | **Collection** | Cyc-specific jargon avoiding "class"/"concept"/"universal" baggage, but not portable outside Cyc's own system. |

## Decision

XwkOnt SHALL adapt selected ISO 1087 concept/term/designation concepts as the formal justification for its existing Concept/Term split: **Concept** (`skos:Concept`, `xwkont:concept:<slug>`) is XwkOnt's language- and source-independent organizing unit; **Term** denotes a specific source ontology's label or designation for (candidate correspondence to) a concept, as already captured in `docs/INFORMATION_ARCHITECTURE.md` §2 and the crosswalk template's Source Definitions table.

XwkOnt SHALL NOT adopt "Class" (the OWL/RDFS/SUMO term) as the organizing-unit label, because it implies formal set-membership/instantiation semantics XwkOnt does not assert by default (`ADR-0004`).

XwkOnt SHALL NOT adopt "Universal" or "Category" (the BFO/UFO terms) as the organizing-unit label, because both carry a specific realist metaphysical commitment that XwkOnt must not assert as its own position — XwkOnt documents source ontologies' stances on universals (per `ADR-0010`'s `philosophical` dimension), it does not take one.

XwkOnt SHALL NOT introduce a project-specific label (e.g., "primitive," considered and rejected in discussion) where "Concept" — already adopted via SKOS and now further justified via ISO 1087 — is sufficient.

XwkOnt SHALL NOT implement the full ISO 1087 terminology-management apparatus (formal term records, equivalence relations, terminography workflow). The adaptation is scoped to the concept/term distinction as conceptual justification, consistent with how `ADR-0003` adapted ISO/IEC 11179 without implementing its full metamodel.

## Scope

This ADR does not change any identifier, template field, or artifact structure established by `ADR-0007`, `ADR-0009`, or `ADR-0010`. It records the rationale for terminology already in use and adds ISO 1087 to the standards baseline.

## Rationale

"Concept" is not an arbitrary choice among equally valid alternatives — the survey above shows the ecosystem splits into (a) formal/DL-descended labels (Concept/Class: SKOS, DL, OWL, SUMO) that are philosophically uncommitted but vary in how much formal semantics they imply, and (b) philosophically-committed labels (Universal/Category: BFO, UFO) that assert a realist metaphysical stance. XwkOnt's own constraints — no default OWL/formal semantics (`ADR-0004`), and Neutrality on philosophical stances it documents but does not adjudicate (`ADR-0010`) — rule out both "Class" (too much formal commitment) and "Universal"/"Category" (too much philosophical commitment). "Concept," as used by SKOS and grounded in ISO 1087, is the one label in the survey that satisfies both constraints simultaneously, and XwkOnt already uses it. This ADR makes that reasoning explicit and citable rather than assumed.

## Consequences

### Positive

- "Concept" as XwkOnt's organizing unit is now justified against a named standard (ISO 1087) and a documented ecosystem survey, not just asserted by `ARCHITECTURAL_PRINCIPLES.md` Principle 3 without support.
- Closes the "why not Term," "why not primitive," "is Concept justifiable" discussion with a citable answer instead of an ad hoc one.
- Reinforces, rather than changes, the existing Concept/Term split already implicit in the template — no artifact rework required.

### Trade-offs

- Adds one more standard (ISO 1087) to track in `docs/STANDARDS_BASELINE.md`, though at "Adapt" scope only (concept/term distinction, not the full terminology-management model).
- Future contributors proposing a different organizing-unit label will need to address this ADR's reasoning, not just assert a preference.

## References

- ISO 1087, Terminology work — Vocabulary
- SKOS (`ADR-0004`)
- `docs/ARCHITECTURAL_PRINCIPLES.md` (Principle 3, Concept-Centric; Principle 6, Neutrality)
- `docs/adr/ADR-0003-adapt-iso-11179-and-adopt-dcmi-metadata.md` (precedent for adapting a standard without implementing its full model)
- `docs/adr/ADR-0004-adopt-rdf-and-skos-adapt-rdfs-reference-owl.md`
- `docs/adr/ADR-0010-distinguish-technical-and-philosophical-dimensions.md`
