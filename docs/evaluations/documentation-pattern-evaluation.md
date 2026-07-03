# Documentation Pattern Evaluation

> **Status:** Accepted
> **Date:** 2026-06-30

## Purpose

Evaluate established documentation frameworks before introducing XwkOnt-specific documentation structure.

## Evaluation Sources

| Source | Practice Observed | Relevance to XwkOnt |
|--------|-------------------|---------------------|
| Diátaxis | Documentation organized by user need: tutorials, how-to guides, reference, and explanation | Provides a mature structure for documentation purpose and audience |
| GitHub Community Standards | README, CONTRIBUTING, LICENSE, CODE_OF_CONDUCT, SECURITY, issue and pull request templates | Provides expected open-source entry points |
| W3C Manual of Style | Best-current-practice guidance for standards-oriented technical reports | Relevant to neutral, precise, standards-style prose |
| IETF RFC process and GitHub guidance | Separation of drafts, issues, consensus workflow, and authoritative publication | Relevant to SSOT, traceability, and change control |
| Architecture Decision Records | Lightweight records for important architectural decisions | Relevant to decision provenance and governance hierarchy |

## Findings

1. XwkOnt already contains multiple documentation types:
   - **Explanation:** `README.md`, founding principles, architectural principles.
   - **Reference:** editorial policy, project lifecycle, ADRs.
   - **Process records:** internal working log and TODO.

2. XwkOnt has not yet explicitly classified documentation by user need. Without classification, future documents may mix tutorials, how-to guidance, reference material, and explanatory rationale.

3. Diátaxis is suitable as an adopted organizing framework, but XwkOnt should adapt it carefully:
   - Governance documents and ADRs are best treated as reference and explanation.
   - Future contributor procedures belong in how-to guides.
   - Future onboarding or worked examples belong in tutorials.
   - Future concept pages and reference registries belong in reference documentation.

4. W3C and IETF practices reinforce neutral language, explicit provenance, versioned decisions, and traceable publication records, all of which align with XwkOnt's founding principles.

## Recommendation

Adopt Diátaxis as the primary documentation classification framework and combine it with existing ADR and internal-working-log practices:

| Documentation Type | XwkOnt Use |
|--------------------|------------|
| Tutorials | Future guided onboarding and worked crosswalk examples |
| How-to guides | Future contributor workflows, reference-entry creation, validation steps |
| Reference | Concept records, reference registry, standards matrix, metadata schemas, ADR index |
| Explanation | Founding rationale, architectural principles, evaluation reports, methodological notes |

## Immediate Documentation Structure

Keep the current structure and add explicit classification over time:

- Root `README.md`: concise entry point.
- Root `TODO.md`: living roadmap.
- `/docs`: project documentation.
- `/docs/adr`: authoritative architecture decisions.
- `/docs/evaluations`: discovery and evaluation reports.
- An internal, unpublished working log: chronological continuity records.

Future Phase 2 work should decide whether to add Diátaxis-aligned subdirectories such as `/docs/tutorials`, `/docs/how-to`, `/docs/reference`, and `/docs/explanation` after the standards discovery phase.

## Adoption Classification

| Pattern | Classification | Rationale |
|---------|----------------|-----------|
| Diátaxis documentation categories | Adopt | Established documentation framework organized around user needs |
| W3C standards-style prose guidance | Reference | Useful editorial model; not all W3C publication rules apply |
| IETF change-tracking and GitHub workflow guidance | Reference | Useful collaboration model; XwkOnt is not an IETF working group |
| ADRs for decisions | Adopt | Already accepted and directly supports provenance |
| Internal Working Log | Introduced | Project-specific record of work, subordinate to authoritative docs |

## Consequences

- Future documentation can be evaluated by user need before being created.
- README can remain concise while detailed material moves into appropriate docs.
- XwkOnt can grow without mixing governance, tutorial, reference, and explanatory content.

## References

- Diátaxis: https://diataxis.fr/
- Diátaxis, "Start here": https://diataxis.fr/start-here/
- GitHub Docs, "About community profiles for public repositories": https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories
- W3C Manual of Style: https://w3c.github.io/manual-of-style/
- IETF RFC 8874, "Working Group GitHub Usage Guidance": https://www.rfc-editor.org/rfc/rfc8874
- Architecture Decision Records: https://adr.github.io/
