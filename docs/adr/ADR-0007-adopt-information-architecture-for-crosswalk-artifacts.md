# ADR-0007: Adopt Information Architecture for Crosswalk Artifacts

- **Status:** Accepted; mapping-assertion fields (§6 of `docs/INFORMATION_ARCHITECTURE.md`) amended by `ADR-0009`, and source-definition/comparison-note fields (§3, §5) amended by `ADR-0010`, both on 2026-07-01
- **Date:** 2026-06-30

## Context

This information architecture work needed to decide the repository layout, artifact identity rules, provenance model, reference-record expectations, and mapping categories required before the first complete concept crosswalk could be authored.

The standards baseline adopted DCMI Terms, RDF, SKOS, SPDX, and BCP 14, and adapted ISO/IEC 11179, RDFS, and ISO 8601. It also deferred exact metadata fields, URI/IRI policy, human-readable to machine-readable relationships, SKOS mapping-property usage, OWL handling, and unknown license handling to this information architecture work or later.

## Decision

XwkOnt adopts `docs/INFORMATION_ARCHITECTURE.md` as the authoritative pre-implementation specification for concept crosswalk artifacts.

Human-readable Markdown concept crosswalks in `docs/crosswalks/concepts/` are the canonical artifacts for concept crosswalk work.

Reference records are stored in `docs/references/`, methodology documents in `docs/methodology/`, and future machine-readable companion artifacts are planned under `data/` but deferred until a later implementation decision.

Stable local identifiers use the `xwkont:` local prefix patterns defined in the information architecture. These local identifiers are not dereferenceable web IRIs unless a future URI/IRI policy explicitly maps them.

## Rationale

A human-readable canonical artifact supports careful review before machine-readable implementation. Planning, but deferring, RDF/SKOS companions preserves the direction established by ADR-0004 without forcing premature serialization decisions.

The layout separates crosswalk content, method, reference evidence, and future data artifacts. The identity model adapts ISO/IEC 11179 registry discipline while remaining lightweight enough for early crosswalk work.

## Consequences

### Positive

- Concept crosswalk work has a concrete template and readiness checklist.
- Crosswalk evidence and mapping assertions can be reviewed before export tooling exists.
- Repository-local identifiers are stable while leaving future URI/IRI design open.
- Unknown or ambiguous source metadata is represented explicitly rather than guessed.

### Trade-offs

- Human-readable Markdown remains the source of truth until later tooling exists.
- Future machine-readable exports will need a separate implementation decision and validation approach.
- Some mapping categories, such as overlap and incompatibility, have no direct SKOS property and require notes or future extension modeling.

## References

- `docs/INFORMATION_ARCHITECTURE.md`
- `docs/STANDARDS_BASELINE.md`
- `docs/adr/ADR-0003-adapt-iso-11179-and-adopt-dcmi-metadata.md`
- `docs/adr/ADR-0004-adopt-rdf-and-skos-adapt-rdfs-reference-owl.md`
- `docs/adr/ADR-0005-adopt-spdx-license-metadata.md`
- `docs/adr/ADR-0006-adapt-iso-8601-and-adopt-bcp-14.md`
