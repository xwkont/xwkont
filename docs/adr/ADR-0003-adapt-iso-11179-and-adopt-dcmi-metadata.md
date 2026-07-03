# ADR-0003: Adapt ISO/IEC 11179 Concepts and Adopt DCMI Metadata Terms

- **Status:** Accepted
- **Date:** 2026-06-30

## Context

Standards discovery identified two complementary metadata standards for XwkOnt. ISO/IEC 11179 provides metadata-registry concepts that are relevant to traceable records, identifiers, definitions, designations, and status. Dublin Core / DCMI Terms provide broadly used descriptive metadata for resources.

XwkOnt needs a conservative metadata baseline for the information architecture work, but it should not design the full concept template or implement a metadata registry at this stage.

## Decision

XwkOnt SHALL adopt selected Dublin Core / DCMI Terms as the baseline descriptive metadata vocabulary for references and future repository artifacts.

XwkOnt SHALL adapt selected ISO/IEC 11179 concepts as conceptual guidance for future metadata architecture, especially where XwkOnt needs records for administered items, identifiers, definitions, designations, provenance, and registration or review status.

XwkOnt SHALL NOT implement the complete ISO/IEC 11179 metamodel at this stage.

## Scope

The DCMI adoption covers metadata semantics only. It does not yet require a specific file format, serialization, field list, or validation mechanism.

The ISO/IEC 11179 adaptation covers reusable registry concepts only. The information architecture work may translate these concepts into a smaller XwkOnt information architecture.

## Rationale

DCMI Terms satisfy many near-term descriptive metadata needs with less project-specific vocabulary. ISO/IEC 11179 is useful for disciplined registry thinking, but adopting it wholesale would be too heavy for the current maturity of the repository.

This combination follows the reuse-before-introduce rule: reuse DCMI where it directly fits, adapt ISO/IEC 11179 where its full model is larger than the immediate need, and avoid inventing XwkOnt-specific metadata concepts prematurely.

## Consequences

### Positive

- Provides the information architecture work with a standards-based metadata baseline.
- Keeps reference and artifact metadata aligned with common descriptive metadata practice.
- Preserves registry discipline without forcing a complete metadata registry implementation.

### Trade-offs

- The information architecture work must still define exact metadata fields and cardinality.
- Some ISO/IEC 11179 concepts may need simplified XwkOnt names or mappings.
- DCMI Terms may need complementary provenance or status metadata from other standards or project policy.

## References

- ISO/IEC 11179-1:2023, *Information technology — Metadata registries (MDR) — Part 1: Framework*.
- ISO/IEC 11179-3:2023, *Information technology — Metadata registries (MDR) — Part 3: Metamodel for registry common facilities*.
- DCMI Metadata Terms.
- Dublin Core Metadata Element Set, Version 1.1.
- `docs/evaluations/standards-survey-report.md`
- `docs/evaluations/standards-adoption-matrix.md`
