# XwkOnt Contribution Workflow

> **Status:** Repository-first governance baseline  
> **Date:** 2026-07-01  
> **Scope:** Practical contribution and review workflow for current XwkOnt artifacts

## Purpose

This guide explains how to propose, review, and accept changes to XwkOnt while preserving repository-first governance, reuse-before-introduce, source-first traceability, and neutrality.

## Before Contributing

Contributors should read:

1. `README.md` for project scope.
2. `docs/FOUNDING_PRINCIPLES.md` and `docs/ARCHITECTURAL_PRINCIPLES.md` for project principles.
3. `docs/EDITORIAL_POLICY.md` for citation, source, and copyright expectations.
4. `docs/governance/governance.md` for decision types.
5. `docs/governance/change-management.md` for compatibility expectations.

## Contribution Categories

| Category | Examples | Minimum expectation |
|---|---|---|
| Editorial | typos, navigation, formatting | Preserve meaning and links. |
| Ontology documentation | glossary, axiom notes, competency questions | Check related ontology docs for consistency. |
| RDF companion | `data/ontology/core.ttl` | Parse Turtle and review compatibility. |
| Examples | validation or tutorial data | Mark as illustrative and non-authoritative. |
| Publication | URI/IRI, validation, release docs | Review release/versioning policy. |
| Crosswalk content | concept pages, mapping records, source comparison | Provide authoritative source evidence. |
| Governance | contribution, release, change-management, lifecycle | Determine whether an ADR is required. |

## General Workflow

1. Identify the artifact class and scope of the change.
2. Check existing standards and repository patterns before introducing a new convention.
3. Make the smallest coherent change.
4. Update navigation or internal working records when a new durable artifact is added.
5. Run the relevant validation checks.
6. Record deferred questions rather than resolving uncertain issues by assumption.
7. Submit the change with a clear summary, validation results, and compatibility notes.

## Review Checklist

A substantive review should confirm that the change:

- preserves XwkOnt's scope as a crosswalk project;
- cites or points to authoritative sources for source-ontology claims;
- keeps examples clearly non-authoritative;
- avoids unsupported equivalence or correspondence claims;
- does not reintroduce formal domain or range commitments for `xwkont-core:mapsTo`;
- does not adopt OWL as the default modeling layer without an ADR;
- updates related docs when a term, property, namespace, or release rule changes;
- includes validation output or an explanation of why a check was not applicable.

## Required Validation by Change Type

| Change type | Required or recommended checks |
|---|---|
| Markdown-only editorial change | Link/path review for touched navigation where practical. |
| Core ontology documentation change | Cross-check glossary, axioms, competency questions, validation notes, and diagrams as applicable. |
| Turtle change | Parse `data/ontology/core.ttl`; parse examples if affected; run structural fallback from `docs/publication/validation-commands.md`. |
| Example-data change | Confirm examples remain in the example namespace and do not claim source authority. |
| Publication or release-policy change | Review `docs/publication/uri-iri-policy.md`, `docs/governance/release-versioning-policy.md`, and release notes. |
| Crosswalk mapping change | Confirm evidence, reference records, relation category, confidence, and reviewer notes. |

## Crosswalk Evidence Expectations

Public crosswalk work must be source-first. A mapping or correspondence should not be accepted unless it identifies the source terms being compared, evidence used, relation category, confidence, and review status.

SKOS mapping properties may be used only when their semantics fit the reviewed evidence. If SKOS is too coarse, use an explicit mapping record and notes rather than forcing a SKOS assertion.

## Internal Working Records

Major changes are tracked in an internal, unpublished working record summarizing actual outcomes, validation, decisions, deferred questions, and recommended next work. It should not duplicate every detail from authoritative policy documents.
