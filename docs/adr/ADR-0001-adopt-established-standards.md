# ADR-0001: Adopt Established Standards Before Introducing New Conventions

- **Status:** Accepted
- **Date:** 2026-06-30

## Context

XwkOnt is a reference and crosswalk project. Its mission is to organize and compare existing knowledge rather than create new foundational models.

To maximize interoperability, maintainability, and contributor familiarity, XwkOnt should avoid introducing project-specific conventions whenever established standards, specifications, repository patterns, or accepted practices already satisfy the project's needs.

## Decision

For every significant design decision, XwkOnt SHALL follow this decision order:

1. Reuse
2. Reference
3. Adapt
4. Introduce

Project-specific conventions SHALL be introduced only after existing standards and accepted practices have been evaluated and determined to be insufficient.

## Consequences

### Positive

- Maximizes interoperability.
- Minimizes project-specific conventions.
- Simplifies contributor onboarding.
- Improves long-term maintainability.
- Encourages standards-based design.

### Trade-offs

- Discovery and evaluation require additional effort before implementation.
- Some standards may require documented adaptation.

## References

This ADR intentionally defers adoption decisions until the Standards Discovery phase.

Candidate references include:

- ISO/IEC 11179 (Metadata Registry)
- W3C Recommendations (RDF, SKOS, OWL)
- GitHub Community Standards
- Architecture Decision Records (ADR)
- Dublin Core Metadata Initiative
