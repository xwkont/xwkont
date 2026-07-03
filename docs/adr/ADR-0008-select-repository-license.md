# ADR-0008: Select a Dual Repository License (CC BY 4.0 for Content, MIT for Code)

- **Status:** Accepted
- **Date:** 2026-07-01

## Context

`ADR-0005` adopted SPDX identifiers and expressions for describing license metadata about references and source materials, but explicitly deferred the separate decision of what license governs the XwkOnt repository itself. No later decision resolved that deferral, and no `LICENSE` file exists. This is a blocker for publishing a public `xwkont/xwkont` repository: an unlicensed public repository does not, by default, grant reuse rights.

XwkOnt's repository content is split in kind:

- Documentation, governance policy, ontology specification prose, glossary, axiom notes, internal working records, and the RDF/Turtle vocabulary itself (`data/ontology/*.ttl`) — reference/content artifacts, not software.
- Potential future tooling (validation scripts, generators) — software artifacts. None exist yet, but `docs/publication/validation-commands.md` already anticipates Python validation snippets, and future work may formalize them as repository scripts.

A single license does not cleanly fit both kinds: content licenses (e.g., Creative Commons) are not designed for software reuse semantics (patent grants, linking, etc.), and software licenses (e.g., MIT) are not the established convention for citable reference/vocabulary content.

## Decision

XwkOnt SHALL use a dual-license structure:

- **CC BY 4.0** (`LICENSE`) governs documentation, governance policy, ontology specification content, and RDF/Turtle vocabulary artifacts (`docs/**`, `data/**`, root-level Markdown).
- **MIT** (`LICENSE-CODE`) governs any executable code or tooling added to the repository (e.g., validation scripts), present or future.

Per `ADR-0005`, SPDX identifiers `CC-BY-4.0` and `MIT` SHALL be used when referring to these licenses in metadata.

## Scope

This decision selects the repository's own license(s). It does not change `ADR-0005`'s scope (license metadata for external references and source materials remains governed separately per source).

## Rationale

CC BY 4.0 is the established convention for citable reference and vocabulary projects (attribution-preserving, permits adaptation — consistent with XwkOnt being built for reuse and citation). MIT is the established convention for small utility code. Splitting by artifact kind follows "Reuse Before Introduce": both are widely recognized standard licenses; no project-specific license text is introduced.

## Consequences

### Positive

- Removes the last blocker to public repository publication that was fully within maintainer control.
- Matches license type to artifact kind rather than forcing one license to cover both content and code.
- Resolves the `ADR-0005` deferral explicitly, closing an open governance question.

### Trade-offs

- Two license files must be kept present and correctly scoped as the repository grows; a future contribution guideline should state which license applies to a new file by directory/kind if the split becomes ambiguous.
- Contributors must understand the split applies by artifact kind, not by directory alone, until such guidance exists.

### Correction (2026-07-03)

The initial `LICENSE`/`LICENSE-CODE` files prepended a project-specific "Scope" paragraph and `SPDX-License-Identifier` line before the canonical license text. GitHub's license detector (`licensee`) does full-text matching against unmodified templates, and the prepended text pushed both files below its confidence threshold — the public repository showed "Unknown, Unknown licenses found" instead of the intended CC BY 4.0 / MIT. Fixed by restoring both files to unmodified canonical text; the scope split and SPDX identifiers (already documented here and in `README.md`'s License section) did not need to live inside the license files themselves.

## References

- Creative Commons Attribution 4.0 International (CC BY 4.0).
- MIT License.
- `docs/adr/ADR-0005-adopt-spdx-license-metadata.md`
