# XwkOnt Core Ontology Publication Guide

> **Status:** Publication guide  
> **Date:** 2026-07-01  
> **Audience:** Readers, contributors, maintainers, and implementers using the current core ontology package

## What Is Being Published

The current package publishes the first XwkOnt core ontology milestone as a repository-first release candidate package. It includes human-readable documentation, lightweight Turtle artifacts, diagrams, validation notes, and illustrative examples.

The package is a comparison scaffold for foundational-ontology crosswalk work. It is not a new foundational ontology and does not replace BFO, DOLCE, SUMO, UFO, or any other source ontology.

## Included Artifacts

| Artifact | Role |
|---|---|
| `docs/ontology/core-ontology.md` | Human-readable core ontology specification. |
| `docs/ontology/core-glossary.md` | Closed glossary for current core terms. |
| `docs/ontology/core-axioms.md` | Conservative axiom and non-axiom commitments. |
| `docs/ontology/core-competency-questions.md` | Competency questions for validation and review. |
| `docs/ontology/core-validation.md` | Validation report for the current scaffold. |
| `docs/ontology/core-ontology.mmd` | Mermaid diagram source for the core ontology. |
| `docs/ontology/core-glossary-dependencies.mmd` | Mermaid glossary dependency graph. |
| `data/ontology/core.ttl` | RDF/RDFS/SKOS-compatible core vocabulary companion. |
| `data/ontology/examples/core-validation-example.ttl` | Non-authoritative validation example data. |
| `docs/publication/uri-iri-policy.md` | URI/IRI publication policy. |
| `docs/publication/validation-commands.md` | Minimal publication-time validation commands. |
| `docs/publication/publication-operations.md` | Operational posture for public IRI publication. |
| `docs/publication/redirects-content-negotiation.md` | Expected redirect and HTML/Turtle content-negotiation behavior. |
| `docs/publication/release-tagging-checklist.md` | Pre-tag checklist for the first external ontology milestone. |
| `docs/releases/core-ontology-release-notes.md` | Release notes for the current milestone. |

## How to Read the Core Ontology

Start with the documents in this order:

1. `docs/ontology/core-ontology.md` for scope, concepts, and relationships.
2. `docs/ontology/core-glossary.md` for closed term definitions.
3. `docs/ontology/core-axioms.md` for what is and is not formalized.
4. `docs/ontology/core-competency-questions.md` and `docs/ontology/core-validation.md` for validation intent and outcomes.
5. `data/ontology/core.ttl` only after reading the documentation, because the Turtle file is a lightweight companion and not a complete formal ontology.

## User Guidance

Users may use the current package to:

- Understand the XwkOnt comparison vocabulary.
- See how top-level concepts such as Entity, Continuant, Occurrent, Object, Quality, Role, Process, Event, Relation, and Information Artifact are organized for crosswalk work.
- Inspect conservative relationship vocabulary such as `hasPart`, `participatesIn`, `hasQuality`, `dependsOn`, and `documentedBy`.
- Review validation questions and examples before relying on the scaffold in tooling or documentation.

Users should not use the current package to:

- Infer source-ontology commitments.
- Treat examples as evidence for BFO, DOLCE, SUMO, UFO, or other source ontologies.
- Resolve foundational disputes such as Process/Event boundaries.
- Assume inverse, disjointness, transitivity, cardinality, or dependency subtyping axioms that are not documented.

## Developer Guidance

Developers may load `data/ontology/core.ttl` as a Turtle RDF graph using the current namespace:

```text
https://w3id.org/xwkont/core#
```

The RDF companion uses RDF, SKOS, and selected RDFS vocabulary. It intentionally avoids OWL as the default modeling layer.

Before publication, developers should run the command set in `docs/publication/validation-commands.md`. If RDFLib is not available, the documented structural fallback is acceptable for the current milestone.

## URI/IRI Guidance

The publication namespace policy is defined in `docs/publication/uri-iri-policy.md`. Operational guidance is in `docs/publication/publication-operations.md` and redirect/content-negotiation expectations are in `docs/publication/redirects-content-negotiation.md`. The current namespace is stable for the milestone, but public dereferenceability must not be advertised until redirects and content negotiation are deployed and verified. Immutable versioned ontology document IRIs remain deferred under the governance prerequisites.

## Mapping Guidance Decision

This guide does not create full mapping-record or SKOS mapping-property usage guidance for the first publication milestone. This is deferred because detailed mapping guidance requires real crosswalk evidence, mapping statuses, provenance requirements, and review workflow decisions that belong to subsequent concept-crosswalk and governance work.

For this milestone:

- `xwkont-core:mapsTo` remains transitional and non-preferred for detailed evidence.
- New detailed mappings should not be invented in publication documentation.
- SKOS mapping properties may be considered in future crosswalk artifacts only when their semantics fit and evidence is traceable.
- Rich mapping records remain follow-up work.

## Publication Limitations

The current release package intentionally leaves the following open:

- Active immutable versioned ontology document IRIs.
- Deployed and verified redirect and content-negotiation behavior for public IRIs.
- Mapping-record schema and SKOS mapping-property usage rules.
- Automated SPARQL competency-query suite.
- OWL formalization, unless a future ADR adopts it for a bounded purpose.
- Source-specific concept correspondences.

## Recommended Next Work

Next work should deploy and verify public IRI redirects and content negotiation, record the results, and prepare the first external ontology milestone tag `ontology-core-v0.1.0` using `docs/publication/release-tagging-checklist.md`.
