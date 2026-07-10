# XwkOnt Governance

> **Status:** Repository-first governance baseline  
> **Date:** 2026-07-01  
> **Scope:** Repository-first maintenance after the first core ontology publication package

## Purpose

This document defines the practical governance posture for maintaining XwkOnt after the first core ontology publication package. It keeps governance minimal while making contribution, review, release, and change-management expectations explicit.

XwkOnt remains a concept-centric crosswalk project. It is not a new foundational ontology, does not replace source ontologies, and does not resolve foundational-ontology disputes without traceable crosswalk evidence.

## Governance Posture

XwkOnt is governed as a repository-first reference project:

1. The Git repository is the single source of truth.
2. Accepted Architecture Decision Records define material standards, representation, publication, and direction decisions.
3. Human-readable Markdown remains the canonical form for current governance, crosswalk, and methodology records unless a later decision changes a specific artifact class.
4. RDF/RDFS/SKOS-compatible Turtle artifacts are maintained as lightweight machine-readable companions for the core ontology package.
5. Project process should remain proportional to project maturity.

## Governance Hierarchy

When guidance conflicts, use this order:

1. Founding Principles.
2. Accepted ADRs.
3. Architectural Principles.
4. Editorial Policy.
5. Governance and change-management policies.
6. Project lifecycle, roadmap, internal working records, and TODOs.
7. Individual implementation artifacts.

Internal working records document outcomes and pointers. They do not override higher-precedence governance documents.

## Maintained Artifact Areas

| Area | Examples | Governance expectation |
|---|---|---|
| Core ontology documentation | `docs/ontology/core-ontology.md`, glossary, axiom notes, validation notes | Changes require consistency review across the ontology package. |
| Core RDF companion | `data/ontology/core.ttl` | Changes require Turtle parse validation and compatibility review. |
| Illustrative examples | `data/ontology/examples/` | Examples must remain explicitly non-authoritative. |
| Publication policy | `docs/publication/` | Changes require release and URI/IRI policy review. |
| Crosswalk methodology | `docs/methodology/`, `docs/crosswalks/` | Changes require source-first traceability review. |
| Governance records | `docs/governance/`, ADRs, lifecycle docs | Material policy changes may require an ADR. |
| Internal working records | *(not published)* | Summarize actual work and deferred decisions for maintainer continuity. |

## Decision Types

### Routine Editorial Changes

Routine editorial changes include typo fixes, wording clarifications that do not change meaning, and navigation updates. They do not require an ADR.

### Managed Content Changes

Managed content changes include adding or revising ontology terms, changing RDF representation, adding crosswalk mappings, modifying examples, or updating release artifacts. They require documented review against the contribution and change-management guides.

### ADR-Level Changes

Create an ADR when a decision materially changes any of the following:

- representation policy;
- standards adoption or adaptation posture;
- URI/IRI publication policy;
- release or versioning policy;
- project scope or direction;
- default modeling layer;
- governance hierarchy.

An ADR is also required before adopting OWL as the default modeling layer. Bounded OWL experiments may be documented as non-default exploration only if they do not change accepted artifacts or publication policy.

## Review Expectations

Every substantive change should answer:

1. What artifact class is changed?
2. Is the change source-first and traceable?
3. Does it preserve neutrality?
4. Does it preserve reuse-before-introduce?
5. Does it alter RDF, SKOS, RDFS, URI/IRI, release, or standards posture?
6. Does it require an ADR?
7. What validation or consistency checks were run?

## Neutrality Requirements

Contributors and maintainers must not:

- present XwkOnt as a foundational ontology;
- invent BFO, DOLCE, SUMO, UFO, or other source-ontology correspondences without cited evidence;
- treat example data as source-ontology evidence;
- collapse unresolved disputes such as Process/Event boundaries for convenience;
- infer equivalence from similar labels alone.

## Repository-First Publication Model

Accepted repository artifacts precede external publication. External websites, redirects, tags, release archives, or generated files should be treated as publication channels for repository-reviewed content, not as independent sources of authority.

## Continuity and Sustainability

**Status:** Resolved (2026-07-03) — lightweight mechanism adopted; heavier mechanisms explicitly declined for now.

`docs/evaluations/comparable-projects-survey.md` found that XwkOnt's two closest identified prior-art predecessors — the WonderWeb Foundational Ontologies Library and ROMULUS — both went dormant for the same underlying, structural reason: research/grant funding pays for *producing* results (papers, initial releases), not for indefinite *maintenance* of the resulting infrastructure. WonderWeb ended because its EU grant had a fixed term (2002-2004) with no continuation mechanism. ROMULUS appears to have gone dormant after its originating PhD research concluded, with no institutional mandate to keep it running afterward.

XwkOnt currently has no institutional backing, grant funding, or organizational mandate either. It is maintained on a repository-first, incremental basis with no defined mechanism for continuity if attention or maintainer availability lapses. This is an acknowledged structural risk, not a hypothetical one — it is the exact failure mode that ended both of the closest comparable projects.

### Decision

XwkOnt already has the two structural pieces that make fork/revival straightforward without any new action, and this governance document now says so explicitly rather than leaving it implicit:

1. **The dual CC-BY-4.0/MIT license (`ADR-0008`)** is itself a continuity mechanism — both licenses explicitly permit copying, modification, and redistribution. Unlike WFOL and ROMULUS, whose license status is unstated even after direct verification (`docs/evaluations/comparable-projects-survey.md`), anyone finding XwkOnt dormant has an unambiguous, already-granted right to fork and continue it. No successor needs to track down a maintainer for permission first.
2. **Repository-first governance (`docs/PROJECT_LIFECYCLE.md`, this document's own Governance Posture)** already means the Git repository — not any person, chat log, or external service — is the single source of truth for project state. A fork loses nothing by not having access to the current maintainer; everything needed to continue the project (ADRs, the public candidate backlog at `docs/crosswalks/candidate-concepts.md`, methodology docs, and any maintainer-local internal working records) is already available by construction. The public contribution backlog is `docs/crosswalks/candidate-concepts.md`; unpublished internal working records (historically referenced as `TODO.md`) are not required for fork continuity.

What XwkOnt explicitly does **not** adopt, as disproportionate to current project size and maturity (Governance Posture principle 5):

- A designated backup maintainer, succession plan, or organizational mandate. XwkOnt remains single-maintainer; this is an accepted risk, not a hidden one.
- A formal "if abandoned, do X" procedural note beyond what the license and repository-first posture already establish — the license itself already says what a successor is permitted to do; a procedural checklist on top of that would be process disproportionate to a documentation project with no active users depending on uptime.

This decision does not eliminate the structural risk WFOL and ROMULUS demonstrate — a maintainer's attention lapsing remains possible for XwkOnt exactly as it was for both predecessors. It closes the open question by choosing which mitigations are worth adopting now (license clarity, repository-first practice — both already in place) versus which are not (formal succession planning) at this project's current scale, rather than leaving the question unaddressed.

The originally listed open questions are answered as follows:

- *What happens to XwkOnt if the current maintainer's attention lapses for an extended period?* — Nothing automatic; no successor is pre-designated. But per the Decision above, anything the project needs to continue (permission via license, project state via the repository) is already available to any interested party, unlike either predecessor.
- *Does the planned XwkOnt-owned reference archive mitigate this?* — No, and it was never meant to. `ADR-0016` itself narrowed that item to a license-gated pointer registry, not a general archive; it addresses citation permanence against *external* link rot, not the project's own continuity risk. These are separate problems with separate mitigations.
- *Is a lighter-weight continuity mechanism worth adopting now?* — Yes, and it already exists: the permissive dual license plus repository-first governance. No additional mechanism (designated contact, formal succession note) is adopted at this time.

## Relationship to Other Governance Policies

This governance baseline is implemented through:

- `docs/governance/contributing.md` for contribution workflow;
- `docs/governance/release-versioning-policy.md` for release and version decisions;
- `docs/governance/change-management.md` for compatibility expectations.
