# Repository Pattern Evaluation

> **Status:** Accepted
> **Date:** 2026-06-30

## Purpose

Evaluate established repository organization practices before introducing XwkOnt-specific structure.

## Evaluation Sources

| Source | Practice Observed | Relevance to XwkOnt |
|--------|-------------------|---------------------|
| GitHub Community Standards | Root-level community health files: README, LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, issue templates, pull request template | Provides familiar open-source repository entry points and contribution governance |
| W3C specification repositories and guidance | Root README, CONTRIBUTING, CODE_OF_CONDUCT, LICENSE; `/docs` or generated publication artifacts; explicit editor and publication workflows | Relevant because XwkOnt is a reference project aligned with standards-style documentation |
| IETF RFC 8874 / RFC 8875 GitHub guidance | GitHub used as an issue, change-tracking, collaboration, and working-group administration tool while authoritative publication remains governed | Relevant to separating working material from authoritative records |
| BFO 2020 repository | Ontology artifacts organized by source format/profile with README and release-oriented repository structure | Relevant to later ontology artifact references, but XwkOnt is not itself an ontology |
| DOLCE repository | Ontology files and documentation held together with repository README and license | Relevant to linking documentation with formal artifacts |
| SUMO repository | Knowledge-base source files and translations organized in repository directories | Relevant to source-first ontology artifact handling |
| OntoUML/UFO Catalog and gUFO repositories | Structured catalog/model repositories with machine-readable assets and documentation | Relevant to future catalog and concept-crosswalk structures |

## Findings

1. XwkOnt already follows several common repository patterns:
   - Root `README.md` as the public entry point.
   - Root `TODO.md` as the living roadmap.
   - `/docs` for governance, principles, ADRs, and internal working records.
   - `/docs/adr` for Architecture Decision Records.
   - An internal, unpublished working log for chronological continuity.

2. XwkOnt is missing several GitHub Community Standards files that should be considered before public contribution work:
   - `LICENSE`
   - `CONTRIBUTING.md`
   - `CODE_OF_CONDUCT.md`
   - `SECURITY.md`
   - Issue templates
   - Pull request template

3. Standards organizations and ontology projects commonly keep authoritative project records close to source artifacts. XwkOnt should continue keeping governance, evaluations, ADRs, and future crosswalk data in the repository.

4. Existing ontology repositories are useful reference targets but should not be copied wholesale. They primarily publish ontology artifacts; XwkOnt publishes comparisons, provenance, and crosswalk documentation.

## Recommendation

Adopt a hybrid repository pattern:

1. **GitHub Community Standards** for public open-source health files.
2. **ADR practice** for significant architectural and standards-adoption decisions.
3. **Standards-project documentation pattern** using `/docs` for governance, lifecycle, decisions, evaluations, and editorial policy.
4. **Ontology-project source-first pattern** for future ontology references and crosswalk artifacts, without turning XwkOnt into a new ontology repository.

## Adoption Classification

| Pattern | Classification | Rationale |
|---------|----------------|-----------|
| GitHub Community Standards files | Adopt | Established open-source repository convention |
| ADR decision records | Adopt | Already adopted by ADR-0001 and suitable for traceability |
| `/docs` governance and evaluations | Adapt | Common documentation pattern adapted to XwkOnt governance hierarchy |
| Internal Working Log | Introduced | Project-specific continuity mechanism justified by Repository First / SSOT |
| Future ontology artifact layout | Defer | Requires standards discovery and information architecture work |

## Consequences

- Contributors will find familiar repository entry points.
- Architectural decisions remain traceable.
- XwkOnt avoids prematurely inventing a custom repository layout.
- Community files become a concrete Phase 2 adoption task.

## References

- GitHub Docs, "About community profiles for public repositories": https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories
- W3C Manual of Style: https://w3c.github.io/manual-of-style/
- W3C on GitHub: https://www.w3.org/guide/github/
- IETF RFC 8874, "Working Group GitHub Usage Guidance": https://www.rfc-editor.org/rfc/rfc8874
- IETF RFC 8875, "Working Group GitHub Administration": https://www.rfc-editor.org/rfc/rfc8875
- BFO 2020 repository: https://github.com/BFO-ontology/BFO-2020
- DOLCE repository: https://github.com/appliedontolab/DOLCE
- SUMO repository: https://github.com/ontologyportal/sumo
- OntoUML/UFO Catalog: https://github.com/OntoUML/ontouml-models
- gUFO repository: https://github.com/nemo-ufes/gufo
