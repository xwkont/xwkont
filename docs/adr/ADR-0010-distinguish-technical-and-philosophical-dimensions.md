# ADR-0010: Distinguish Technical and Philosophical Dimensions in Crosswalk Artifacts

- **Status:** Accepted
- **Date:** 2026-07-01

## Context

`ADR-0007` (amended by `ADR-0009`) established the concept-crosswalk template's Source Definitions, Semantic Comparison Notes, and Mapping Assertion tables. None of them explicitly distinguish a source ontology's **technical/formal representation** (class hierarchy, properties, domain/range, formalism used) from its **philosophical/metaphysical commitments** (realism vs. conceptualism, endurantism vs. perdurantism, cognitive/linguistic orientation, stance on universals, etc.).

Foundational ontologies are not purely engineering artifacts. `docs/evaluations/prior-art-survey.md` cites Borgo, Galton, and Kutz (2022), which frames differences between BFO, DOLCE, GFO, GUM, TUpper, UFO, and YAMATO precisely along this axis — e.g., BFO's realist framework grounded in scientific practice versus DOLCE's cognitive and linguistic orientation. `docs/ARCHITECTURAL_PRINCIPLES.md` already requires XwkOnt to document, not adjudicate, philosophical disagreements (Principle 4, Source First; Principle 6, Neutrality), but the template has no structured place to record a source's philosophical stance separately from its technical representation, risking that this dimension is omitted or blended untraceably into general prose.

## Decision

XwkOnt SHALL add a `Dimension` field to the **Source Definitions and Contextual Notes** table and the **Semantic Comparison Notes** table in `docs/crosswalks/concepts/TEMPLATE.md`, amending `ADR-0007` / `docs/INFORMATION_ARCHITECTURE.md` §3 and §5.

`Dimension` takes one of:

- `technical` — formal/engineering representation: class hierarchy position, properties, domain/range, the formalism used (OWL, RDFS, first-order logic, etc.), engineering intent.
- `philosophical` — metaphysical/theoretical commitments: realism vs. conceptualism, endurantism vs. perdurantism, stance on universals, cognitive or linguistic orientation, and other theoretical grounding the source ontology's own documentation discusses.
- `both` — used when a single citation addresses both inseparably (common in foundational-ontology source papers, which often justify formal choices by philosophical argument in the same passage).

Crosswalk authors SHOULD attempt at least one `philosophical`-dimension row per source ontology where the source's own documentation discusses its theoretical grounding. Per the project's existing "do not guess" rule (`docs/EDITORIAL_POLICY.md`, `docs/INFORMATION_ARCHITECTURE.md`), XwkOnt SHALL NOT infer or invent a philosophical stance a source does not document — an absent or `unknown` row is correct when the source is silent, not a fabricated one.

This field records **what stance a source takes**, citation-linked like every other claim. It never asserts which stance is correct, per `ARCHITECTURAL_PRINCIPLES.md` Principle 6 (Neutrality) and Principle 4 (Source First).

## Scope

This ADR amends `docs/INFORMATION_ARCHITECTURE.md` §3 (Source Definitions and Contextual Notes) and §5 (Semantic Comparison Notes), and `docs/crosswalks/concepts/TEMPLATE.md`. It does not change Mapping Assertions (`ADR-0009`'s territory), identifiers, reference-record requirements, or repository layout.

## Rationale

Making the technical/philosophical distinction explicit and citation-linked, rather than leaving it implicit in prose, matches how the existing peer-reviewed literature already compares these ontologies (Borgo/Galton/Kutz 2022) and directly serves XwkOnt's stated purpose: helping a reader understand not just how a concept is *encoded* differently across ontologies, but *why* — the theoretical commitment driving that encoding. Without this field, a crosswalk risks reading as a comparison of class hierarchies alone, missing the reason the hierarchies differ.

## Consequences

### Positive

- Crosswalk entries can show a source's formal representation and its philosophical grounding as separately traceable, separately cited claims.
- Reinforces existing neutrality and source-first principles with a concrete template mechanism rather than leaving them as prose guidance alone.
- Aligns with how the strongest existing prior art (the Applied Ontology special issue) already frames these comparisons.

### Trade-offs

- Adds a required field contributors must populate per source-definition and comparison-note row.
- Some source ontologies (e.g., more engineering-first ones like SUMO or CCO) may have thin or absent philosophical documentation, leading to legitimately sparse `philosophical`-dimension rows — this is expected and should not be treated as a gap to fill by inference.
- Requires editorial judgment on `technical` vs. `philosophical` vs. `both` classification; some ambiguity is unavoidable and should be resolved with an explicit note rather than silently picking one.

## References

- `docs/evaluations/prior-art-survey.md` (Borgo, Galton, Kutz, "Foundational ontologies in action," *Applied Ontology* 17(1), 2022)
- `docs/ARCHITECTURAL_PRINCIPLES.md`
- `docs/adr/ADR-0007-adopt-information-architecture-for-crosswalk-artifacts.md`
- `docs/adr/ADR-0009-adapt-sssom-for-mapping-assertions.md`
