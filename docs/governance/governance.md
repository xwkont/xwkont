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

**Status:** Open question, not resolved.

`docs/evaluations/comparable-projects-survey.md` found that XwkOnt's two closest identified prior-art predecessors — the WonderWeb Foundational Ontologies Library and ROMULUS — both went dormant for the same underlying, structural reason: research/grant funding pays for *producing* results (papers, initial releases), not for indefinite *maintenance* of the resulting infrastructure. WonderWeb ended because its EU grant had a fixed term (2002-2004) with no continuation mechanism. ROMULUS appears to have gone dormant after its originating PhD research concluded, with no institutional mandate to keep it running afterward.

XwkOnt currently has no institutional backing, grant funding, or organizational mandate either. It is maintained on a repository-first, incremental basis with no defined mechanism for continuity if attention or maintainer availability lapses. This is an acknowledged structural risk, not a hypothetical one — it is the exact failure mode that ended both of the closest comparable projects.

This governance document does not resolve the question of how XwkOnt avoids the same fate. It records the question so it isn't silently repeated:

- What happens to XwkOnt if the current maintainer's attention lapses for an extended period?
- Does the planned XwkOnt-owned reference archive (`TODO.md`, "Future Infrastructure") mitigate the dependency risk on *external* services, without addressing the dependency risk on the *project's own* continuity?
- Is there a lighter-weight continuity mechanism (e.g., a clear "if abandoned, do X" note; a designated point of contact; a license and repository structure that makes a fork/revival straightforward) worth adopting now, while the project is small, rather than after it has gone quiet?

## Relationship to Other Governance Policies

This governance baseline is implemented through:

- `docs/governance/contributing.md` for contribution workflow;
- `docs/governance/release-versioning-policy.md` for release and version decisions;
- `docs/governance/change-management.md` for compatibility expectations.
