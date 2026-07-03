# XwkOnt Change Management and Compatibility Policy

> **Status:** Repository-first governance baseline  
> **Date:** 2026-07-01  
> **Scope:** Compatibility expectations for ontology, publication, examples, documentation, and crosswalk artifacts

## Purpose

This policy defines how XwkOnt evaluates changes for compatibility and review impact. It is intentionally lightweight and practical for the project's current maturity.

## Compatibility Principles

1. Preserve repository-first authority.
2. Prefer additive changes over breaking changes.
3. Keep source-ontology evidence separate from illustrative examples.
4. Record uncertainty instead of over-formalizing unresolved questions.
5. Treat public identifiers and mapping assertions as higher-risk changes than prose clarification.

## Change Classes

| Class | Description | Examples | Review expectation |
|---|---|---|---|
| Patch-compatible | Clarifies or fixes without changing meaning. | typos, broken links, formatting, non-semantic notes | Standard review. |
| Additive-compatible | Adds content without invalidating existing accepted content. | new glossary note, new competency question, new non-authoritative example | Consistency review. |
| Potentially incompatible | Changes interpretation, identifiers, representation, or review status. | rename term, remove property, alter namespace, change mapping category | Change-management review and possible ADR. |
| Policy-changing | Alters standards, publication, governance, or project direction. | default OWL adoption, new IRI policy, release semantics change | ADR required. |

## Core Ontology Term Compatibility

Adding a core term is additive only when it:

- has a documented purpose;
- fits the current glossary and axiom posture;
- does not resolve source-ontology disputes by assumption;
- does not imply unsupported source correspondences;
- updates human-readable docs and RDF companion consistently when both are affected.

Renaming, deleting, merging, splitting, or redefining a core term is potentially incompatible and requires explicit migration notes.

## RDF, SKOS, and RDFS Compatibility

RDF/SKOS/RDFS changes must preserve the standards posture adopted by ADR-0004 unless a new ADR changes it.

Compatible changes may include:

- adding `skos:note`, `skos:scopeNote`, or documentation links;
- adding new terms with conservative labels and definitions;
- correcting metadata that does not change term semantics.

Potentially incompatible changes include:

- changing public term IRIs;
- changing class hierarchy commitments;
- adding formal domain or range commitments to properties that intentionally lack them;
- reintroducing formal RDFS domain or range commitments for `xwkont-core:mapsTo`;
- adding inverse, disjointness, transitivity, cardinality, or dependency-subtype commitments not supported by accepted policy;
- using OWL as the default modeling layer.

## URI/IRI Compatibility

The current namespace `https://w3id.org/xwkont/core#` should remain stable for current core terms. Changes to namespace policy, active versioned document IRI semantics, or dereferenceability promises require publication-policy review and may require an ADR if they change accepted policy.

Versioned ontology document IRIs remain deferred until the prerequisites in `docs/governance/release-versioning-policy.md` are complete.

## Example Data Compatibility

Example data is compatible when it remains:

- clearly illustrative;
- under an example namespace;
- free of authoritative source-ontology correspondence claims;
- aligned with current validation questions.

Example data must not be cited as evidence for BFO, DOLCE, SUMO, UFO, or any other source ontology.

## Documentation Compatibility

Documentation changes should keep navigation, status, dates, and artifact lists current. If a document changes the meaning of an accepted policy, the change should be treated as policy-changing rather than editorial.

## Crosswalk and Mapping Compatibility

Crosswalk mappings are high-traceability artifacts. A mapping change is compatible only when the relation category, evidence, confidence, and review status remain clear.

Mapping-record and SKOS mapping-property usage guidance becomes required when any of the following trigger conditions occurs:

1. XwkOnt publishes a public concept crosswalk containing reviewed source-to-source mapping assertions.
2. XwkOnt exports crosswalk mappings as RDF, SKOS, JSON-LD, or another machine-readable public companion.
3. XwkOnt promotes any mapping assertion to `reviewed` or `accepted` status.
4. XwkOnt uses SKOS mapping properties in public crosswalk artifacts beyond illustrative examples.

Until one of these triggers occurs, detailed mapping-record guidance remains scheduled follow-up work rather than a blocker for core ontology maintenance. When triggered, guidance should define required fields, provenance, evidence levels, relation categories, confidence, status, reviewer history, and SKOS property usage rules.

## Release Compatibility Notes

Every ontology milestone release should include compatibility notes that identify whether changes are patch-compatible, additive-compatible, potentially incompatible, or policy-changing.
