# ADR-0002: Adopt Hybrid Repository and Diátaxis Documentation Patterns

- **Status:** Accepted
- **Date:** 2026-06-30

## Context

Early discovery work evaluated established repository organization, documentation frameworks, standards-project practices, and ontology-project repositories before introducing XwkOnt-specific structures.

XwkOnt needs a repository and documentation pattern that supports:

- Public open-source contribution.
- Governance and decision traceability.
- Neutral standards-style documentation.
- Concept-centric ontology crosswalk artifacts.
- Repository-first Single Source of Truth (SSOT) operation.

## Decision

XwkOnt SHALL adopt a hybrid repository and documentation pattern:

1. Use GitHub Community Standards as the baseline for public repository health files.
2. Continue using Architecture Decision Records for significant architectural and standards-adoption decisions.
3. Keep governance, lifecycle, evaluations, editorial policy, and internal working records under `/docs`.
4. Use Diátaxis as the documentation classification framework for future documentation planning.
5. Reference W3C and IETF practices for standards-style prose, traceability, and collaborative change control where applicable.
6. Defer ontology artifact and concept-crosswalk layout decisions until standards discovery and information architecture work are complete.

## Consequences

### Positive

- Reuses established repository and documentation practices.
- Maintains a concise root README while allowing detailed documentation under `/docs`.
- Gives future documents a clear purpose based on user need.
- Preserves decision traceability through ADRs.
- Avoids copying ontology repository layouts before XwkOnt's crosswalk information architecture is defined.

### Trade-offs

- The repository will need additional community health files before public contribution work is mature.
- Diátaxis classification may require refactoring existing documents during Phase 2.
- Some W3C and IETF practices must be referenced selectively because XwkOnt is not itself a W3C or IETF standards process.

## References

- Repository Pattern Evaluation: `docs/evaluations/repository-pattern-evaluation.md`
- Documentation Pattern Evaluation: `docs/evaluations/documentation-pattern-evaluation.md`
- GitHub Community Standards: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories
- Diátaxis: https://diataxis.fr/
- W3C Manual of Style: https://w3c.github.io/manual-of-style/
- IETF RFC 8874: https://www.rfc-editor.org/rfc/rfc8874
- IETF RFC 8875: https://www.rfc-editor.org/rfc/rfc8875
