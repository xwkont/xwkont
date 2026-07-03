# ADR-0005: Adopt SPDX Identifiers and Expressions for License Metadata

- **Status:** Accepted
- **Date:** 2026-06-30

## Context

XwkOnt must track licenses and rights for references, source materials, and future artifacts where known. Standards discovery identified SPDX as the relevant standard for license identifiers and license expressions.

This standards-adoption decision is not authorized to choose the repository license.

## Decision

XwkOnt SHALL use SPDX license identifiers and SPDX license expressions for license metadata when a known license can be represented accurately.

XwkOnt SHALL treat repository license selection as a separate decision.

XwkOnt SHALL NOT infer or guess a license when source license information is unclear. Unknown, ambiguous, custom, or mixed-license cases must remain explicit and traceable.

## Scope

This decision applies to metadata about licenses. It does not select, change, or recommend the license for the XwkOnt repository.

## Rationale

SPDX provides a widely used controlled vocabulary for license metadata and reduces ambiguity. Adopting SPDX for metadata satisfies the reuse-before-introduce rule without overstepping into a repository license decision.

## Consequences

### Positive

- Creates consistent license metadata for future references and artifacts.
- Separates metadata representation from license governance.
- Reduces project-specific license labels.

### Trade-offs

- Later information architecture or governance work must define how to record unknown, custom, or compound license cases.
- Contributors must distinguish source license metadata from the repository's own license.

## References

- SPDX License List.
- SPDX Specification v2.3 License Expressions.
- `docs/evaluations/standards-survey-report.md`
- `docs/evaluations/standards-adoption-matrix.md`
