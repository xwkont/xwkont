# XwkOnt Core Ontology Specification

> **Local identifier:** `xwkont:ontology:core`
> **Editorial status:** `draft`
> **Created:** `2026-07-01`
> **Canonical artifact:** this Markdown specification
> **Companion representation:** `data/ontology/core.ttl`
> **Diagram source:** `docs/ontology/core-ontology.mmd`
> **Closed glossary:** `docs/ontology/core-glossary.md`
> **Logical axiom notes:** `docs/ontology/core-axioms.md`

## Purpose and Scope

This document defines the first XwkOnt core ontology specification. "Core ontology" means a conservative XwkOnt working vocabulary for organizing top-level foundational-ontology comparison, not a replacement for BFO, DOLCE, SUMO, UFO, or any other source ontology.

The core is intentionally limited to concepts and relationships that are repeatedly needed to compare foundational ontologies at a high level. It is a scaffolding artifact for later glossary closure, logical axiom work, validation, publication, and governance.

## In Scope

- Candidate top-level concepts needed for crosswalk navigation and comparison.
- Candidate inheritance relationships among those concepts.
- Core relationship types with intended meanings.
- Domain and range notes where supportable from common foundational-ontology practice or prior XwkOnt crosswalk method.
- Explicit uncertainty where source ontologies diverge or evidence is insufficient.
- A lightweight RDF/RDFS/SKOS-compatible companion representation for structural review.
- A maintainable Mermaid diagram source.

## Out of Scope

- Declaring a new authoritative foundational ontology.
- Resolving disagreements among source ontologies.
- Logical axiom-level definitions for every term; closed glossary definitions are documented in `docs/ontology/core-glossary.md`.
- OWL logical axioms, disjointness, property characteristics, cardinalities, and reasoner-grade constraints beyond the conservative notes in `docs/ontology/core-axioms.md`.
- Exhaustive source-specific mappings; concept crosswalks remain the place for detailed source comparison.
- Final URI/IRI publication policy.

## Representation Decision

This Markdown document is the canonical ontology specification; `data/ontology/core.ttl` is an initial RDF/RDFS/SKOS-compatible companion representation.

Rationale:

- Markdown remains reviewable and repository-first, consistent with the information architecture's human-readable canonical approach.
- RDF was already adopted as the future graph data model, SKOS as the concept-centric vocabulary, and selected RDFS vocabulary as the lightweight vocabulary description layer.
- Turtle is compact, reviewable in Git, and structurally validatable without adopting OWL as the default modeling layer.
- OWL formalization is deferred to later logical-axiom work to avoid premature logical commitments.

This is an implementation-level decision rather than a new ADR because it applies the direction already accepted in ADR-0004 and does not change the project architecture.

## Top-Level Concepts

| Concept | Local identifier | Parent | Rationale | Status and uncertainty |
|---|---|---|---|---|
| Entity | `xwkont:core:Entity` | none | Broad comparison root needed because source foundational ontologies usually distinguish what exists or is modeled before subdividing it. | Candidate root; definition closure deferred. |
| Continuant | `xwkont:core:Continuant` | Entity | Needed to compare enduring entities such as objects, qualities, and roles across sources that distinguish continuants from occurrents or similar categories. | Candidate; not all source ontologies use this label or boundary. |
| Occurrent | `xwkont:core:Occurrent` | Entity | Needed to compare processes, events, and temporally unfolding entities across sources. | Candidate; event/process distinctions vary significantly. |
| Object | `xwkont:core:Object` | Continuant | A central comparison concept already identified in project scope and planned construction work. | Candidate; exact treatment differs across sources. |
| Quality | `xwkont:core:Quality` | Continuant | Needed because many foundational ontologies model dependent characteristics or qualities of bearers. | Candidate; dependence semantics deferred. |
| Role | `xwkont:core:Role` | Continuant | Needed because roles are prominent in applied ontology and differ from intrinsic object or quality categories. | Candidate; role, function, disposition, and relator boundaries deferred. |
| Process | `xwkont:core:Process` | Occurrent | Needed to compare temporally extended happenings, activities, or processes. | Candidate; process/event equivalence is not assumed. |
| Event | `xwkont:core:Event` | Occurrent | Needed because project scope explicitly names Event and several sources use event-like categories differently from process. | Candidate sibling of Process for now; formal relation to Process deferred. |
| Relation | `xwkont:core:Relation` | Entity | Needed to document first-class relation concepts and relationship types used in comparison. | Candidate; whether relations are entities is source-dependent and uncertain. |
| Information Artifact | `xwkont:core:InformationArtifact` | Entity | Needed for XwkOnt's own references, definitions, mappings, and specifications without treating them as source ontology commitments. | Candidate support concept; may move to metadata vocabulary later. |

## Candidate Inheritance Relationships

| Subject | Relationship | Object | Rationale | Uncertainty |
|---|---|---|---|---|
| Continuant | `rdfs:subClassOf` | Entity | Common high-level organizing distinction for comparison. | Label and formal semantics vary by source. |
| Occurrent | `rdfs:subClassOf` | Entity | Common high-level organizing distinction for comparison. | Label and formal semantics vary by source. |
| Object | `rdfs:subClassOf` | Continuant | Objects are treated as continuant-like comparison targets in the first core. | Source-specific boundaries require crosswalk evidence. |
| Quality | `rdfs:subClassOf` | Continuant | Qualities are compared as dependent continuant-like entities in the first core. | Dependence axioms deferred. |
| Role | `rdfs:subClassOf` | Continuant | Roles are compared as dependent/contextual continuant-like entities in the first core. | Role/function/disposition distinctions deferred. |
| Process | `rdfs:subClassOf` | Occurrent | Processes are treated as occurrent-like comparison targets. | Relation to Event remains open. |
| Event | `rdfs:subClassOf` | Occurrent | Events are treated as occurrent-like comparison targets. | Relation to Process remains open. |
| Relation | `rdfs:subClassOf` | Entity | Lets relationship concepts be discussed in the same scaffold. | Some source ontologies may not reify relations this way. |
| Information Artifact | `rdfs:subClassOf` | Entity | Supports XwkOnt records and evidence artifacts. | May be refactored into a separate metadata layer. |

## Core Relationship Types

| Relationship | Local identifier | Intended meaning | Candidate domain | Candidate range | Rationale | Status and uncertainty |
|---|---|---|---|---|---|---|
| has part | `xwkont:core:hasPart` | A whole includes another entity as a part. | Entity | Entity | Part-whole comparison is broadly needed across foundational ontologies. | Structural only; mereological axioms deferred. |
| part of | `xwkont:core:partOf` | An entity is part of a larger entity. | Entity | Entity | Inverse navigation for part-whole notes. | Inverse formalization deferred. |
| participates in | `xwkont:core:participatesIn` | A continuant is involved in an occurrent. | Continuant | Occurrent | Needed to relate objects, roles, and other continuants to processes/events. | Domain/range are candidate only. |
| has participant | `xwkont:core:hasParticipant` | An occurrent involves a continuant. | Occurrent | Continuant | Inverse navigation for participation. | Inverse formalization deferred. |
| has quality | `xwkont:core:hasQuality` | An entity bears or is characterized by a quality. | Entity | Quality | Needed to compare quality-bearing patterns. | Whether all entities can bear qualities is deferred. |
| quality of | `xwkont:core:qualityOf` | A quality characterizes or depends on a bearer. | Quality | Entity | Inverse navigation for quality comparison. | Dependence semantics deferred. |
| bears role | `xwkont:core:bearsRole` | An entity has a role in some context. | Entity | Role | Needed for role comparison. | Context qualification deferred. |
| role of | `xwkont:core:roleOf` | A role is borne by an entity. | Role | Entity | Inverse navigation for role comparison. | Dependence and context axioms deferred. |
| depends on | `xwkont:core:dependsOn` | One entity depends on another in some sense. | Entity | Entity | Captures common dependency language without committing to a subtype. | Dependency kinds deferred. |
| maps to | `xwkont:core:mapsTo` | An XwkOnt concept or relationship has a candidate mapping to another concept or relationship. | Entity | Entity | Bridges core ontology work with crosswalk methodology. | Use detailed mapping categories in crosswalk artifacts. |
| documented by | `xwkont:core:documentedBy` | A concept, relationship, or claim is documented by an information artifact. | Entity | Information Artifact | Supports repository-first provenance. | Exact provenance model deferred to publication/governance work. |

## Structural Consistency Rules

The initial representation is considered structurally consistent when:

1. Every local class used as a domain, range, or superclass is declared.
2. Every local property referenced in the specification is declared.
3. Every subclass edge connects declared classes.
4. Every property with a candidate domain or range points to a declared class.
5. The Turtle companion parses as RDF.
6. No OWL-only constructs are required for this artifact.

## Unresolved Modeling Questions

| Question | Impact | Assigned follow-up |
|---|---|---|
| Are Process and Event siblings, overlapping concepts, or should one specialize the other? | Affects top-level hierarchy and source crosswalks. | Glossary for evidence; axiom review for formalization. |
| Should Relation remain under Entity or move into a separate vocabulary layer? | Affects whether relationship concepts are modeled as first-class core concepts. | Later architecture review. |
| Should Information Artifact be part of the core ontology or only metadata/provenance infrastructure? | Affects boundary between ontology content and repository metadata. | Validation work or publication planning. |
| Which dependency subtypes are needed: existential, generic, specific, historical, or contextual? | Affects qualities, roles, and participation semantics. | Later logical-axiom work. |
| What are the exact source correspondences for each top-level concept across BFO, DOLCE, SUMO, and UFO? | Affects confidence and acceptance of candidate concepts. | Glossary and concept crosswalk work. |
| Should `mapsTo` be retained in the core ontology or replaced entirely by SKOS and crosswalk mapping records? | Affects machine-readable export design. | Later logical-axiom work or publication planning. |

## Deferred Formalization Work

A conservative logical review was completed in `docs/ontology/core-axioms.md`. The following remain deferred:

- OWL class axioms, disjointness, property inverses, transitivity, and constraints.
- Competency questions and example knowledge base validation.
- URI/IRI publication policy and namespace governance.
- Rendered diagrams and publication-ready documentation.

## Validation Notes

This specification validates the companion Turtle file for parseability and verifies that all local domain, range, and subclass references resolve to declared local classes. This validation is structural only; it does not prove logical consistency. The closed glossary adds a dependency graph for the terms used in this specification. The axiom review adds conservative logical axiom notes, classifies candidate inheritance and relationship axioms, and removes RDFS domain/range commitments from the transitional `mapsTo` property.
