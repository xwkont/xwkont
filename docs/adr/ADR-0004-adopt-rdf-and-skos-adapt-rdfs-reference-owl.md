# ADR-0004: Adopt RDF and SKOS, Adapt RDFS, and Reference OWL

- **Status:** Accepted
- **Date:** 2026-06-30

## Context

Standards discovery identified RDF, RDFS, OWL, and SKOS as the primary semantic-web standards relevant to XwkOnt. XwkOnt is concept-centric and crosswalk-oriented, but it is not intended to create a new foundational ontology.

Standards adoption must provide enough guidance for later information architecture work without implementing RDF, OWL, SKOS, JSON-LD, Turtle, or other machine-readable artifacts.

## Decision

XwkOnt SHALL adopt RDF as the future graph data model for machine-readable crosswalk and semantic-web interoperability artifacts.

XwkOnt SHALL adopt SKOS as the baseline concept-scheme and mapping vocabulary for future concept-centric crosswalk artifacts.

XwkOnt SHALL adapt selected RDFS vocabulary for lightweight vocabulary description when RDF vocabularies are designed.

XwkOnt SHALL reference OWL for imported ontology semantics and future constrained formalization decisions, but SHALL NOT adopt OWL as the default modeling layer for XwkOnt artifacts at this time.

## Scope

This decision establishes representation direction only. It does not create a concept template, crosswalk, ontology, RDF schema, SKOS concept scheme, OWL ontology, URI policy, or serialization requirement.

## Rationale

RDF provides the graph foundation needed for future machine-readable artifacts. SKOS directly fits XwkOnt's concept-centric and mapping-oriented purpose. RDFS offers useful lightweight vocabulary description without requiring stronger commitments. OWL is important to understand source ontologies, but default OWL modeling could make XwkOnt appear to assert a new formal ontology rather than document and compare existing ones.

This decision follows the reuse-before-introduce rule by adopting existing W3C standards for graph and concept representation while constraining their use to avoid premature implementation and scope expansion.

## Consequences

### Positive

- Gives later information architecture work a clear semantic-web target.
- Aligns future crosswalks with widely used web standards.
- Keeps XwkOnt neutral by not making OWL the default assertion layer.

### Trade-offs

- Later information architecture work must still define URI/IRI policy, artifact boundaries, and human-readable to machine-readable relationships.
- SKOS mapping properties may be too coarse for some ontology comparison cases and may require notes or future extensions.
- OWL handling remains a deferred governance issue for formal source ontology semantics.

## References

- RDF 1.1 Concepts and Abstract Syntax, W3C Recommendation.
- RDF Schema 1.1, W3C Recommendation.
- OWL 2 Web Ontology Language Document Overview, W3C Recommendation.
- SKOS Simple Knowledge Organization System Reference, W3C Recommendation.
- `docs/evaluations/standards-survey-report.md`
- `docs/evaluations/standards-adoption-matrix.md`
