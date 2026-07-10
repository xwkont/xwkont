# XwkOnt Core Glossary

> **Local identifier:** `xwkont:glossary:core`  
> **Editorial status:** `reviewed`  
> **Created:** `2026-07-01`  
> **Primary source:** `docs/ontology/core-ontology.md`  
> **Dependency graph:** `docs/ontology/core-glossary-dependencies.mmd`
> **Graph format:** Mermaid source (`.mmd`), matching the core ontology diagram-source convention

## Purpose and Scope

This glossary closes the terminology used by the core ontology specification. A term is included when it is needed to understand the definitions, relationship meanings, scope notes, uncertainty notes, validation notes, or representation choices in the core ontology.

The glossary is intentionally conservative. It defines terms for XwkOnt documentation and comparison work; it does not assert a new foundational ontology, settle disagreements among BFO, DOLCE, SUMO, UFO, or other source ontologies, or add OWL axioms and reasoner-grade constraints.

## Closure Method

A glossary entry is closed when its definition uses only:

- terms that also have entries in this glossary;
- ordinary English words used without XwkOnt-specific meaning;
- names of external standards or source ontologies used as references rather than as internal terms.

Where a term cannot be closed without premature modeling, the entry marks the uncertainty and assigns follow-up work.

## Status Vocabulary

| Status | Meaning |
|---|---|
| Core candidate | A concept or relationship included in the core ontology scaffold, but not yet a final foundational commitment. |
| Methodological | A term needed to understand XwkOnt process, documentation, comparison, or validation notes. |
| Representation | A term needed to understand the Markdown, RDF/RDFS/SKOS, Turtle, or diagram artifacts. |
| Provisional | A term whose meaning is sufficient for this glossary but whose detailed treatment is assigned to later work. |

## Glossary Entries

### Abstract

- **Preferred label:** Abstract
- **Local identifier:** `xwkont:core:Abstract`
- **Status:** Core candidate concept
- **Definition:** An entity considered for comparison as lacking spatiotemporal location or embodiment, such as a number or type, contrasted with Concrete.
- **Parent:** Entity
- **Editorial note:** Modeled as a class-pair sibling to Continuant/Occurrent; the boundary with Concrete is source-dependent.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### accepted

- **Preferred label:** accepted
- **Status:** Methodological
- **Definition:** Approved for use in the repository as a current XwkOnt artifact, decision, or status.
- **Editorial note:** Acceptance in XwkOnt does not make a source ontology claim true; it records a repository decision.
- **Traceability:** Used by ADR and roadmap status notes.

### Aggregate

- **Preferred label:** Aggregate
- **Local identifier:** `xwkont:core:Aggregate`
- **Status:** Core candidate concept
- **Definition:** A continuant considered for comparison as a plurality of member parts that together form a unit under a uniform membership criterion, contrasted with the more permissive Sum.
- **Parent:** Continuant
- **Editorial note:** One of two sibling sub-concepts with Sum, reflecting an even source split on unity-criterion strictness.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### alternate label

- **Preferred label:** alternate label
- **Alternate labels:** alternative label
- **Status:** Methodological
- **Definition:** A non-preferred name recorded to help readers find a glossary term, concept, relationship, or artifact.
- **Traceability:** Needed for glossary label normalization.

### artifact

- **Preferred label:** artifact
- **Status:** Methodological
- **Definition:** A repository item that records project content, such as a document, data file, diagram source, internal working record, or decision record.
- **Traceability:** Used by the core ontology specification and internal working records.

### axiomatization

- **Preferred label:** axiomatization
- **Alternate labels:** logical axiomatization
- **Status:** Provisional
- **Definition:** The activity of expressing definitions, relationships, or constraints as formal logical statements.
- **Editorial note:** Detailed axiomatization is assigned to later formal-axiom work.
- **Traceability:** Core ontology out-of-scope and deferred work notes.

### bearer

- **Preferred label:** bearer
- **Status:** Provisional
- **Definition:** An entity that has, carries, or is characterized by a quality or role.
- **Editorial note:** XwkOnt uses this as neutral documentation language; exact bearer-dependence axioms are deferred.
- **Traceability:** Used by `quality of`, `has quality`, `role of`, and `bears role` explanations.

### bears role

- **Preferred label:** bears role
- **Local identifier:** `xwkont:core:bearsRole`
- **Status:** Core candidate relationship
- **Definition:** Relates an entity to a role that the entity has in a context.
- **Domain note:** Candidate domain is Entity.
- **Range note:** Candidate range is Role.
- **Editorial note:** The context and dependence conditions are not formalized in this glossary.
- **Traceability:** Core ontology relationship table; Turtle property declaration.

### BFO

- **Preferred label:** BFO
- **Alternate labels:** Basic Formal Ontology
- **Status:** Methodological
- **Definition:** A source ontology considered by XwkOnt for comparison and crosswalk work.
- **Traceability:** Core ontology purpose and unresolved source-correspondence notes.

### BCP 14

- **Preferred label:** BCP 14
- **Status:** Representation
- **Definition:** The RFC 2119 and RFC 8174 convention for using requirement keywords in normative documents.
- **Traceability:** Standards baseline and ADR-0006.

### Boundary

- **Preferred label:** Boundary
- **Local identifier:** `xwkont:core:Boundary`
- **Status:** Core candidate concept
- **Definition:** A continuant considered for comparison as a lower-dimensional, fiat-demarcated part of its host entity, such as an edge or surface, contrasted with the not-part-of-host Site.
- **Parent:** Continuant
- **Editorial note:** One of two sibling sub-concepts with Site, reflecting a part-of-host/not-part-of-host split found across multiple source ontologies.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### candidate

- **Preferred label:** candidate
- **Status:** Methodological
- **Definition:** Proposed for current XwkOnt use but not yet treated as a final, stable, or fully validated project commitment.
- **Traceability:** Core ontology status and uncertainty column.

### cardinality

- **Preferred label:** cardinality
- **Status:** Provisional
- **Definition:** A constraint on how many values or related entities may, must, or may not occur for a relationship.
- **Editorial note:** Cardinality constraints are deferred to later formal-axiom work.
- **Traceability:** Core ontology out-of-scope notes.


### category

- **Preferred label:** category
- **Status:** Methodological
- **Definition:** A grouping used to organize terms, concepts, entities, or classes for description or comparison.
- **Traceability:** Used by class, domain, range, and ontology definitions.

### Change

- **Preferred label:** Change
- **Local identifier:** `xwkont:core:Change`
- **Status:** Core candidate concept
- **Definition:** An entity considered for comparison as an alteration, transition, or difference an entity undergoes, contrasted with the entity's own persisting or unfolding through time.
- **Parent:** Entity
- **Editorial note:** Modeled as a direct Entity subclass since source ontologies diverge on whether change belongs with continuants or occurrents.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### claim

- **Preferred label:** claim
- **Status:** Methodological
- **Definition:** A statement recorded in an XwkOnt artifact that may require evidence, provenance, or later validation.
- **Traceability:** Used by `documented by` relationship meaning.

### class

- **Preferred label:** class
- **Status:** Representation
- **Definition:** A category used to group entities or concepts for description, comparison, or lightweight RDF/RDFS representation.
- **Editorial note:** In this glossary, class does not imply full OWL class semantics.
- **Traceability:** Core ontology top-level concepts and Turtle `rdfs:Class` declarations.

### closed definition

- **Preferred label:** closed definition
- **Status:** Methodological
- **Definition:** A definition whose XwkOnt-specific terms are themselves defined in the same glossary or explicitly assigned to follow-up.
- **Traceability:** glossary-closure objective.

### concept

- **Preferred label:** concept
- **Status:** Methodological
- **Definition:** A unit of meaning that XwkOnt documents, compares, and connects across source ontologies.
- **Editorial note:** Concept is used for XwkOnt navigation and comparison; it does not require the concept to be a class in every source ontology.
- **Traceability:** README, information architecture, core ontology, and Turtle `skos:Concept` usage.

### concept scheme

- **Preferred label:** concept scheme
- **Status:** Representation
- **Definition:** A collection that organizes related concepts for documentation or SKOS-compatible representation.
- **Traceability:** Turtle `skos:ConceptScheme` declaration.

### Concrete

- **Preferred label:** Concrete
- **Local identifier:** `xwkont:core:Concrete`
- **Status:** Core candidate concept
- **Definition:** An entity considered for comparison as having spatiotemporal location or embodiment, such as a physical object, quality, or event, contrasted with Abstract.
- **Parent:** Entity
- **Editorial note:** Modeled as Abstract's sibling class pair; the boundary with Abstract is source-dependent.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### consistency

- **Preferred label:** consistency
- **Status:** Methodological
- **Definition:** Absence of a detected conflict under the rules being checked.
- **Editorial note:** Core ontology and glossary checks are structural and editorial, not reasoner-grade logical checks.
- **Traceability:** Structural consistency and validation notes.

### constraint

- **Preferred label:** constraint
- **Status:** Provisional
- **Definition:** A stated restriction on how a concept, relationship, property, value, or artifact may be used.
- **Editorial note:** Formal constraints are assigned to later formal-axiom work.
- **Traceability:** Core ontology out-of-scope and deferred work notes.


### context

- **Preferred label:** context
- **Status:** Provisional
- **Definition:** The situation, use, arrangement, participation, or other circumstance in which a role or relationship is considered.
- **Editorial note:** Context modeling is deferred to later formal-axiom work.
- **Traceability:** Role, bears role, and role of glossary entries.

### Continuant

- **Preferred label:** Continuant
- **Local identifier:** `xwkont:core:Continuant`
- **Status:** Core candidate concept
- **Definition:** An entity considered for comparison as persisting, enduring, or being present through time, such as an object, quality, or role.
- **Parent:** Entity
- **Editorial note:** Source ontologies differ on this label and boundary; XwkOnt does not make a final commitment in this glossary.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### Continuous

- **Preferred label:** Continuous
- **Local identifier:** `xwkont:core:Continuous`
- **Status:** Core candidate concept
- **Definition:** An entity considered for comparison as gapless or without discrete boundaries between its parts or values, contrasted with the gap-having Discrete.
- **Parent:** Entity
- **Editorial note:** One of two sibling sub-concepts with Discrete.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### core ontology

- **Preferred label:** core ontology
- **Status:** Methodological
- **Definition:** The core ontology's working vocabulary for organizing top-level foundational-ontology comparison.
- **Editorial note:** It is a scaffold for crosswalk work, not a replacement source ontology.
- **Traceability:** Core ontology purpose and scope.

### crosswalk

- **Preferred label:** crosswalk
- **Status:** Methodological
- **Definition:** An XwkOnt artifact or activity that compares concepts, relationships, definitions, and mappings across source ontologies.
- **Traceability:** README, crosswalk methodology, information architecture.

### declared

- **Preferred label:** declared
- **Status:** Representation
- **Definition:** Explicitly recorded in an artifact as a class, property, concept, relationship, or other named item.
- **Traceability:** Structural consistency rules.

### definition

- **Preferred label:** definition
- **Status:** Methodological
- **Definition:** A statement that explains the intended meaning of a term for XwkOnt use.
- **Traceability:** Glossary closure objective and core ontology notes.

### dependence

- **Preferred label:** dependence
- **Status:** Provisional
- **Definition:** A relationship in which one entity requires another entity in some stated or unstated way.
- **Editorial note:** Kinds of dependence are deferred to later formal-axiom work.
- **Traceability:** Quality, role, and `depends on` notes.

### depends on

- **Preferred label:** depends on
- **Local identifier:** `xwkont:core:dependsOn`
- **Status:** Core candidate relationship
- **Definition:** Relates one entity to another entity that it requires in some sense.
- **Domain note:** Candidate domain is Entity.
- **Range note:** Candidate range is Entity.
- **Editorial note:** Existential, generic, specific, historical, and contextual dependence are not separated in this glossary.
- **Traceability:** Core ontology relationship table; Turtle property declaration.

### diagram source

- **Preferred label:** diagram source
- **Status:** Representation
- **Definition:** A maintainable text file used to produce or review a diagram.
- **Traceability:** Core ontology Mermaid source.

### Discrete

- **Preferred label:** Discrete
- **Local identifier:** `xwkont:core:Discrete`
- **Status:** Core candidate concept
- **Definition:** An entity considered for comparison as separated into distinct, countable, gap-bounded units or values, contrasted with the gapless Continuous.
- **Parent:** Entity
- **Editorial note:** Continuous's sibling sub-concept.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### disjointness

- **Preferred label:** disjointness
- **Status:** Provisional
- **Definition:** A formal statement that categories cannot share the same members.
- **Editorial note:** Disjointness is assigned to later formal-axiom work and is not asserted by this glossary.
- **Traceability:** Core ontology out-of-scope notes.

### Disposition

- **Preferred label:** Disposition
- **Local identifier:** `xwkont:core:Disposition`
- **Status:** Core candidate concept
- **Definition:** A continuant considered for comparison as a tendency, capacity, or potential an entity has to behave or be realized in a certain way under certain conditions.
- **Parent:** Continuant
- **Editorial note:** Modeled as a sibling of Role under Continuant.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### DOLCE

- **Preferred label:** DOLCE
- **Status:** Methodological
- **Definition:** A source ontology considered by XwkOnt for comparison and crosswalk work.
- **Traceability:** Core ontology purpose and unresolved source-correspondence notes.


### documented by

- **Preferred label:** documented by
- **Local identifier:** `xwkont:core:documentedBy`
- **Status:** Core candidate relationship
- **Definition:** Relates a concept, relationship, or claim to an information artifact that documents it.
- **Domain note:** Candidate domain is Entity.
- **Range note:** Candidate range is Information Artifact.
- **Editorial note:** Exact provenance model is deferred to publication or governance work.
- **Traceability:** Core ontology relationship table; Turtle property declaration.

### domain

- **Preferred label:** domain
- **Status:** Representation
- **Definition:** The category from which the subject of a relationship is expected to come in a stated representation.
- **Editorial note:** These domain notes are candidate structural guidance, not complete logical restrictions.
- **Traceability:** Core ontology relationship table and Turtle `rdfs:domain` declarations.

### Entity

- **Preferred label:** Entity
- **Local identifier:** `xwkont:core:Entity`
- **Status:** Core candidate concept
- **Definition:** The broad comparison root for something that exists, is treated as existing, or is modeled as a subject of description by XwkOnt or a source ontology.
- **Parent:** none
- **Editorial note:** Entity is a comparison root, not a final claim that all source ontologies use the same top category.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### Event

- **Preferred label:** Event
- **Local identifier:** `xwkont:core:Event`
- **Status:** Core candidate concept
- **Definition:** An occurrent considered for comparison as a happening, occurrence, or temporally located unit.
- **Parent:** Occurrent
- **Editorial note:** The distinction between Event and Process remains unsettled across source ontologies.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### evidence

- **Preferred label:** evidence
- **Status:** Methodological
- **Definition:** Information used to support a definition, mapping, claim, or editorial decision.
- **Traceability:** Editorial policy, crosswalk methodology, core ontology rationale notes.

### formalization

- **Preferred label:** formalization
- **Status:** Provisional
- **Definition:** The activity of making a definition, relationship, or rule more precise in a representation that supports systematic checking or reasoning.
- **Editorial note:** Logical formalization is assigned to later formal-axiom work.
- **Traceability:** Core ontology out-of-scope and deferred work notes.

### foundational ontology

- **Preferred label:** foundational ontology
- **Alternate labels:** upper ontology
- **Status:** Methodological
- **Definition:** A broad ontology that provides general categories and relationships intended to organize knowledge across domains.
- **Traceability:** README and core ontology scope.

### glossary

- **Preferred label:** glossary
- **Status:** Methodological
- **Definition:** A controlled list of terms with definitions and related editorial information.
- **Traceability:** glossary-closure objective.

### glossary closure

- **Preferred label:** glossary closure
- **Status:** Methodological
- **Definition:** The process of ensuring that XwkOnt-specific terms used in definitions are also defined or explicitly deferred.
- **Traceability:** glossary-closure objective and validation notes.

### has participant

- **Preferred label:** has participant
- **Local identifier:** `xwkont:core:hasParticipant`
- **Status:** Core candidate relationship
- **Definition:** Relates an occurrent to a continuant involved in it.
- **Domain note:** Candidate domain is Occurrent.
- **Range note:** Candidate range is Continuant.
- **Editorial note:** Inverse formalization with `participates in` is deferred.
- **Traceability:** Core ontology relationship table; Turtle property declaration.

### has part

- **Preferred label:** has part
- **Local identifier:** `xwkont:core:hasPart`
- **Status:** Core candidate relationship
- **Definition:** Relates a whole entity to another entity included as its part.
- **Domain note:** Candidate domain is Entity.
- **Range note:** Candidate range is Entity.
- **Editorial note:** Mereological axioms are deferred.
- **Traceability:** Core ontology relationship table; Turtle property declaration.

### has quality

- **Preferred label:** has quality
- **Local identifier:** `xwkont:core:hasQuality`
- **Status:** Core candidate relationship
- **Definition:** Relates an entity to a quality that characterizes it.
- **Domain note:** Candidate domain is Entity.
- **Range note:** Candidate range is Quality.
- **Editorial note:** Whether all entities can have qualities is deferred.
- **Traceability:** Core ontology relationship table; Turtle property declaration.

### identifier

- **Preferred label:** identifier
- **Status:** Methodological
- **Definition:** A string or name used to refer to an artifact, concept, relationship, or term within an agreed scope.
- **Traceability:** Information architecture and local identifiers in core ontology.

### Information Artifact

- **Preferred label:** Information Artifact
- **Alternate labels:** information artifact
- **Local identifier:** `xwkont:core:InformationArtifact`
- **Status:** Core candidate concept
- **Definition:** An entity that records or carries information for XwkOnt use, such as a specification, reference, mapping, diagram source, or validation note.
- **Parent:** Entity
- **Editorial note:** This support concept may later move to metadata or provenance infrastructure.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### inheritance relationship

- **Preferred label:** inheritance relationship
- **Alternate labels:** subclass relationship
- **Status:** Representation
- **Definition:** A relationship stating that one class or concept is organized under a broader class or concept.
- **Traceability:** Core ontology candidate inheritance table.

### inverse formalization

- **Preferred label:** inverse formalization
- **Status:** Provisional
- **Definition:** A formal statement that one relationship goes in the opposite direction of another relationship.
- **Editorial note:** Inverse formalization is assigned to later formal-axiom work.
- **Traceability:** Relationship uncertainty notes.

### IRI

- **Preferred label:** IRI
- **Alternate labels:** Internationalized Resource Identifier
- **Status:** Representation
- **Definition:** An identifier form used on the web and in RDF to identify resources.
- **Editorial note:** XwkOnt URI/IRI publication policy is deferred to later publication-policy work.
- **Traceability:** Core ontology out-of-scope notes and ADR-0007.

### label

- **Preferred label:** label
- **Status:** Methodological
- **Definition:** A human-readable name for a term, concept, relationship, property, or artifact.
- **Traceability:** SKOS/RDFS labels and glossary normalization objective.

### List / Sequence

- **Preferred label:** List / Sequence
- **Local identifier:** `xwkont:core:ListSequence`
- **Status:** Core candidate concept
- **Definition:** An entity considered for comparison as an ordered collection whose members have an intrinsic sequence or position, such as a list or ordered set.
- **Parent:** Entity
- **Editorial note:** Modeled as a direct Entity subclass since source ontologies diverge on whether ordered collections belong with abstract or concrete entities.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### local identifier

- **Preferred label:** local identifier
- **Status:** Methodological
- **Definition:** An identifier controlled by XwkOnt for repository use and not necessarily published as a dereferenceable web IRI.
- **Traceability:** Information architecture and core ontology tables.

### logical axiom

- **Preferred label:** logical axiom
- **Status:** Provisional
- **Definition:** A formal statement intended to support logical interpretation, consistency checking, or inference.
- **Editorial note:** Logical axioms are assigned to later formal-axiom work.
- **Traceability:** Core ontology out-of-scope and deferred work notes.

### mapping

- **Preferred label:** mapping
- **Status:** Methodological
- **Definition:** A recorded relationship between an XwkOnt concept or relationship and a concept or relationship in another source or artifact.
- **Traceability:** Crosswalk methodology and `maps to`.

### maps to

- **Preferred label:** maps to
- **Local identifier:** `xwkont:core:mapsTo`
- **Status:** Core candidate relationship
- **Definition:** Relates an XwkOnt concept or relationship to another concept or relationship as a candidate mapping.
- **Domain note:** Candidate domain is Entity.
- **Range note:** Candidate range is Entity.
- **Editorial note:** Detailed mapping categories belong in crosswalk artifacts; replacement by SKOS mapping properties remains open.
- **Traceability:** Core ontology relationship table; Turtle property declaration.

### Mermaid

- **Preferred label:** Mermaid
- **Status:** Representation
- **Definition:** A text-based diagram notation used by XwkOnt for maintainable diagram sources.
- **Traceability:** Core ontology Mermaid diagram source.

### metadata

- **Preferred label:** metadata
- **Status:** Methodological
- **Definition:** Information that describes an artifact, source, term, concept, relationship, or record.
- **Traceability:** Information architecture and Information Artifact uncertainty note.

### Mind / Conscious Being / Agent

- **Preferred label:** Mind / Conscious Being / Agent
- **Local identifier:** `xwkont:core:MindConsciousBeingAgent`
- **Status:** Core candidate concept
- **Definition:** A continuant considered for comparison as a mind, conscious being, or agent capable of cognition, intention, or autonomous action, contrasted with the more generic Object.
- **Parent:** Continuant
- **Editorial note:** Modeled as a sibling of Object under Continuant.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### Modality

- **Preferred label:** Modality
- **Local identifier:** `xwkont:core:Modality`
- **Status:** Core candidate concept
- **Definition:** A quality considered for comparison as a way of qualifying necessity, possibility, or contingency.
- **Parent:** Quality
- **Editorial note:** Modeled under Quality.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### model

- **Preferred label:** model
- **Status:** Methodological
- **Definition:** To represent something for XwkOnt comparison, documentation, or validation.
- **Editorial note:** The verb model does not imply a final metaphysical commitment.
- **Traceability:** Core ontology rationale and uncertainty notes.

### namespace

- **Preferred label:** namespace
- **Status:** Representation
- **Definition:** A naming context used to keep identifiers distinct.
- **Traceability:** Turtle prefixes and URI/IRI deferral notes.

### neutrality

- **Preferred label:** neutrality
- **Status:** Methodological
- **Definition:** XwkOnt's practice of documenting and comparing source ontologies without advocating one source ontology or resolving foundational disputes as project doctrine.
- **Traceability:** Founding principles, architectural principles, and glossary constraints.

### Non-physical Object

- **Preferred label:** Non-physical Object
- **Local identifier:** `xwkont:core:NonPhysicalObject`
- **Status:** Core candidate concept
- **Definition:** A continuant considered for comparison as an entity that is neither a physical object nor an amount of matter, such as a mental or social object.
- **Parent:** Continuant
- **Editorial note:** Modeled under Continuant as a single umbrella class, not split into a separate social-object branch.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### Object

- **Preferred label:** Object
- **Local identifier:** `xwkont:core:Object`
- **Status:** Core candidate concept
- **Definition:** A continuant considered for comparison as an individual thing, body, system, or object-like entity.
- **Parent:** Continuant
- **Editorial note:** Exact source-specific boundaries are deferred to concept crosswalk work.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### Occurrent

- **Preferred label:** Occurrent
- **Local identifier:** `xwkont:core:Occurrent`
- **Status:** Core candidate concept
- **Definition:** An entity considered for comparison as unfolding, occurring, happening, or extending through time, such as a process or event.
- **Parent:** Entity
- **Editorial note:** Source ontologies differ on this label and boundary.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### Ontological Level / Stratum

- **Preferred label:** Ontological Level / Stratum
- **Local identifier:** `xwkont:core:OntologicalLevelStratum`
- **Status:** Core candidate concept
- **Definition:** An entity considered for comparison as a level, stratum, or layer used to classify other entities by kind of reality, such as material, mental, or social strata.
- **Parent:** Entity
- **Editorial note:** Modeled as a direct Entity subclass and single umbrella class, a meta-level classifier orthogonal to the Continuant/Occurrent split.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### ontology

- **Preferred label:** ontology
- **Status:** Methodological
- **Definition:** A structured representation of categories, relationships, and meanings for a subject matter or level of generality.
- **Traceability:** README and core ontology scope.

### OWL

- **Preferred label:** OWL
- **Alternate labels:** Web Ontology Language
- **Status:** Representation
- **Definition:** A W3C standard used for formal ontology representation and reasoning.
- **Editorial note:** XwkOnt references OWL but does not use it as the default modeling layer.
- **Traceability:** ADR-0004 and core ontology out-of-scope notes.

### part

- **Preferred label:** part
- **Status:** Provisional
- **Definition:** An entity included in another entity considered as a whole.
- **Editorial note:** Detailed mereology is deferred to later formal-axiom work.
- **Traceability:** `has part` and `part of` definitions.

### part of

- **Preferred label:** part of
- **Local identifier:** `xwkont:core:partOf`
- **Status:** Core candidate relationship
- **Definition:** Relates an entity to a larger entity that includes it as a part.
- **Domain note:** Candidate domain is Entity.
- **Range note:** Candidate range is Entity.
- **Editorial note:** Inverse formalization with `has part` is deferred.
- **Traceability:** Core ontology relationship table; Turtle property declaration.

### participates in

- **Preferred label:** participates in
- **Local identifier:** `xwkont:core:participatesIn`
- **Status:** Core candidate relationship
- **Definition:** Relates a continuant to an occurrent in which the continuant is involved.
- **Domain note:** Candidate domain is Continuant.
- **Range note:** Candidate range is Occurrent.
- **Editorial note:** Participation conditions are deferred.
- **Traceability:** Core ontology relationship table; Turtle property declaration.

### preferred label

- **Preferred label:** preferred label
- **Status:** Methodological
- **Definition:** The primary human-readable name selected by XwkOnt for a term, concept, relationship, property, or artifact.
- **Traceability:** Glossary label normalization and SKOS `prefLabel` usage.

### Process

- **Preferred label:** Process
- **Local identifier:** `xwkont:core:Process`
- **Status:** Core candidate concept
- **Definition:** An occurrent considered for comparison as temporally extended activity, happening, or change.
- **Parent:** Occurrent
- **Editorial note:** XwkOnt does not assume that Process and Event are equivalent.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### property

- **Preferred label:** property
- **Status:** Representation
- **Definition:** A named relationship used in RDF/RDFS-style representation to connect a subject to an object or value.
- **Editorial note:** In this glossary, property does not imply OWL object-property or datatype-property commitments.
- **Traceability:** Core ontology relationship types and Turtle `rdf:Property` declarations.

### Proposition

- **Preferred label:** Proposition
- **Local identifier:** `xwkont:core:Proposition`
- **Status:** Core candidate concept
- **Definition:** An abstract entity considered for comparison as a purely combinatorial content that can be borne by multiple concrete representations, such as strings, sounds, or icons expressing the same claim.
- **Parent:** Abstract
- **Editorial note:** Modeled under Abstract.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### provenance

- **Preferred label:** provenance
- **Status:** Methodological
- **Definition:** Information about the origin, source, evidence, authorship, or decision path for an artifact, claim, definition, or mapping.
- **Traceability:** Founding principles, architectural principles, `documented by`.

### Quality

- **Preferred label:** Quality
- **Local identifier:** `xwkont:core:Quality`
- **Status:** Core candidate concept
- **Definition:** A continuant considered for comparison as a characteristic, feature, or way an entity is, usually understood as requiring a bearer.
- **Parent:** Continuant
- **Editorial note:** Dependence semantics are deferred.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### quality of

- **Preferred label:** quality of
- **Local identifier:** `xwkont:core:qualityOf`
- **Status:** Core candidate relationship
- **Definition:** Relates a quality to the entity it characterizes or requires as bearer.
- **Domain note:** Candidate domain is Quality.
- **Range note:** Candidate range is Entity.
- **Editorial note:** Dependence formalization is deferred.
- **Traceability:** Core ontology relationship table; Turtle property declaration.

### Quantity

- **Preferred label:** Quantity
- **Local identifier:** `xwkont:core:Quantity`
- **Status:** Core candidate concept
- **Definition:** A concrete entity considered for comparison as an amount, portion, or quantity of matter or stuff, such as a mass of gold.
- **Parent:** Concrete
- **Editorial note:** Modeled under Concrete; covers several related but distinct source-ontology senses.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### range

- **Preferred label:** range
- **Status:** Representation
- **Definition:** The category from which the object or value of a relationship is expected to come in a stated representation.
- **Editorial note:** These range notes are candidate structural guidance, not complete logical restrictions.
- **Traceability:** Core ontology relationship table and Turtle `rdfs:range` declarations.

### RDF

- **Preferred label:** RDF
- **Alternate labels:** Resource Description Framework
- **Status:** Representation
- **Definition:** A W3C graph data model used by XwkOnt for machine-readable companion artifacts.
- **Traceability:** ADR-0004 and Turtle companion representation.

### RDFS

- **Preferred label:** RDFS
- **Alternate labels:** RDF Schema
- **Status:** Representation
- **Definition:** A W3C vocabulary used by XwkOnt for lightweight descriptions of classes, properties, labels, domains, ranges, and subclass relationships.
- **Traceability:** ADR-0004 and Turtle companion representation.

### reasoner-grade constraint

- **Preferred label:** reasoner-grade constraint
- **Status:** Provisional
- **Definition:** A formal constraint intended to be processed by an automated reasoning tool.
- **Editorial note:** Such constraints are assigned to later formal-axiom work.
- **Traceability:** Core ontology out-of-scope notes.

### Relation

- **Preferred label:** Relation
- **Local identifier:** `xwkont:core:Relation`
- **Status:** Core candidate concept
- **Definition:** An entity considered for comparison as a connection, association, or relationship type among entities.
- **Parent:** Entity
- **Editorial note:** Whether relations should be first-class entities is source-dependent and remains uncertain.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### relationship

- **Preferred label:** relationship
- **Status:** Methodological
- **Definition:** A connection or association between terms, concepts, entities, classes, artifacts, or values.
- **Traceability:** Core ontology relationship table and methodology documents.


### representation

- **Preferred label:** representation
- **Status:** Methodological
- **Definition:** A form in which XwkOnt records content, such as Markdown prose, RDF/Turtle data, SKOS vocabulary, RDFS structure, or Mermaid diagram source.
- **Traceability:** Core ontology representation decision and glossary status vocabulary.

### repository-first

- **Preferred label:** repository-first
- **Status:** Methodological
- **Definition:** The practice that project records become authoritative only when captured in the Git repository.
- **Traceability:** Founding principles and project workflow.

### Role

- **Preferred label:** Role
- **Local identifier:** `xwkont:core:Role`
- **Status:** Core candidate concept
- **Definition:** A continuant considered for comparison as something an entity has because of context, use, participation, or social or organizational arrangement.
- **Parent:** Continuant
- **Editorial note:** Role, function, disposition, and relator boundaries are deferred.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### role of

- **Preferred label:** role of
- **Local identifier:** `xwkont:core:roleOf`
- **Status:** Core candidate relationship
- **Definition:** Relates a role to the entity that bears it.
- **Domain note:** Candidate domain is Role.
- **Range note:** Candidate range is Entity.
- **Editorial note:** Context and dependence axioms are deferred.
- **Traceability:** Core ontology relationship table; Turtle property declaration.

### scope note

- **Preferred label:** scope note
- **Status:** Methodological
- **Definition:** An explanatory note that describes intended use, limits, or interpretation of a term, concept, relationship, or artifact.
- **Traceability:** Core ontology SKOS and Markdown notes.

### Site

- **Preferred label:** Site
- **Local identifier:** `xwkont:core:Site`
- **Status:** Core candidate concept
- **Definition:** A continuant considered for comparison as a dependent place or region whose location is determined by a host entity without being part of it, such as a hole or a shadow, contrasted with the part-of-host Boundary.
- **Parent:** Continuant
- **Editorial note:** Boundary's sibling sub-concept.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### SKOS

- **Preferred label:** SKOS
- **Alternate labels:** Simple Knowledge Organization System
- **Status:** Representation
- **Definition:** A W3C vocabulary used by XwkOnt for concept-centric labels, definitions, notes, schemes, and mappings.
- **Traceability:** ADR-0004 and Turtle companion representation.

### source ontology

- **Preferred label:** source ontology
- **Status:** Methodological
- **Definition:** An external ontology that XwkOnt documents, compares, or maps without replacing it.
- **Traceability:** README, core ontology purpose, crosswalk methodology.

### Space

- **Preferred label:** Space
- **Local identifier:** `xwkont:core:Space`
- **Status:** Core candidate concept
- **Definition:** An entity considered for comparison as a spatial region, place, or extent used to locate other entities in space.
- **Parent:** Entity
- **Editorial note:** Modeled as a direct Entity subclass, consistent with Time's placement.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### SPDX

- **Preferred label:** SPDX
- **Status:** Representation
- **Definition:** A standard vocabulary and expression syntax used by XwkOnt for known license metadata.
- **Traceability:** ADR-0005 and standards baseline.

### structural consistency

- **Preferred label:** structural consistency
- **Status:** Methodological
- **Definition:** Consistency checked against artifact-structure rules, such as declared classes, declared properties, valid subclass references, valid domain and range references, and parseable Turtle.
- **Editorial note:** Structural consistency does not prove logical consistency.
- **Traceability:** Core ontology structural consistency rules and validation notes.

### subclass

- **Preferred label:** subclass
- **Alternate labels:** subclass of
- **Status:** Representation
- **Definition:** A class or concept organized under a broader class or concept.
- **Editorial note:** In this glossary, subclass is used as lightweight RDFS-style structure and not as a complete OWL commitment.
- **Traceability:** Core ontology candidate inheritance relationships and Turtle `rdfs:subClassOf` declarations.

### Sum

- **Preferred label:** Sum
- **Local identifier:** `xwkont:core:Sum`
- **Status:** Core candidate concept
- **Definition:** A continuant considered for comparison as a criterion-free sum of two or more entities, with no unity requirement on its members, contrasted with the stricter Aggregate.
- **Parent:** Continuant
- **Editorial note:** Aggregate's sibling sub-concept.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### SUMO

- **Preferred label:** SUMO
- **Alternate labels:** Suggested Upper Merged Ontology
- **Status:** Methodological
- **Definition:** A source ontology considered by XwkOnt for comparison and crosswalk work.
- **Traceability:** Core ontology purpose and unresolved source-correspondence notes.

### term

- **Preferred label:** term
- **Status:** Methodological
- **Definition:** A word or phrase used with a meaning relevant to XwkOnt documentation, representation, or comparison.
- **Traceability:** Glossary closure objective.

### Time

- **Preferred label:** Time
- **Local identifier:** `xwkont:core:Time`
- **Status:** Core candidate concept
- **Definition:** An entity considered for comparison as a temporal region, instant, or interval used to locate other entities in time.
- **Parent:** Entity
- **Editorial note:** Modeled as a direct Entity subclass rather than under Continuant or Occurrent.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### traceability

- **Preferred label:** traceability
- **Status:** Methodological
- **Definition:** The ability to follow a term, definition, mapping, claim, decision, or artifact back to supporting sources or project records.
- **Traceability:** Architectural principles and glossary entries.

### Turtle

- **Preferred label:** Turtle
- **Status:** Representation
- **Definition:** A compact RDF serialization used for the core ontology companion file.
- **Traceability:** Core ontology representation decision and `data/ontology/core.ttl`.

### UFO

- **Preferred label:** UFO
- **Alternate labels:** Unified Foundational Ontology
- **Status:** Methodological
- **Definition:** A source ontology considered by XwkOnt for comparison and crosswalk work.
- **Traceability:** Core ontology purpose and unresolved source-correspondence notes.

### uncertainty

- **Preferred label:** uncertainty
- **Status:** Methodological
- **Definition:** An explicitly recorded lack of final confidence, evidence, agreement, or modeling decision.
- **Traceability:** Core ontology status notes and glossary constraints.

### undefined term

- **Preferred label:** undefined term
- **Status:** Methodological
- **Definition:** A term used with XwkOnt-specific meaning that lacks a glossary entry or explicit deferral.
- **Traceability:** Glossary validation notes.

### Universal

- **Preferred label:** Universal
- **Local identifier:** `xwkont:core:Universal`
- **Status:** Core candidate concept
- **Definition:** An entity considered for comparison as a type, kind, category, or universal that classifies or is instantiated by individuals, contrasted with a particular individual.
- **Parent:** Entity
- **Editorial note:** Modeled as a direct Entity subclass paralleling a top-level category/individual split found in one source ontology.
- **Traceability:** Core ontology top-level concepts; Turtle class declaration.

### URI

- **Preferred label:** URI
- **Alternate labels:** Uniform Resource Identifier
- **Status:** Representation
- **Definition:** An identifier form used to identify a resource.
- **Editorial note:** XwkOnt URI/IRI publication policy is deferred to later publication-policy work.
- **Traceability:** Core ontology out-of-scope notes and ADR-0007.

### validation

- **Preferred label:** validation
- **Status:** Methodological
- **Definition:** Checking an artifact against stated rules, expectations, or requirements.
- **Traceability:** Core ontology validation notes and glossary report.

### whole

- **Preferred label:** whole
- **Status:** Provisional
- **Definition:** An entity considered as including one or more parts.
- **Editorial note:** Detailed mereology is deferred to later formal-axiom work.
- **Traceability:** `has part` and `part of` definitions.

### XwkOnt

- **Preferred label:** XwkOnt
- **Status:** Methodological
- **Definition:** The repository-first project that documents, compares, and connects concepts across source foundational ontologies.
- **Traceability:** README and all project governance documents.

## Validation Report

### Undefined Terms Found and Resolved

This glossary closure found that the core ontology used several internal or semi-technical terms without a local glossary entry. The following groups were resolved by adding glossary entries:

- Core concepts: Entity, Continuant, Occurrent, Object, Quality, Role, Process, Event, Relation, Information Artifact.
- Core relationships: has part, part of, participates in, has participant, has quality, quality of, bears role, role of, depends on, maps to, documented by.
- Representation terms: class, property, subclass, domain, range, RDF, RDFS, SKOS, OWL, Turtle, IRI, URI, concept scheme, namespace.
- Methodological terms: candidate, source ontology, crosswalk, mapping, glossary closure, structural consistency, provenance, uncertainty, formalization, validation, traceability.
- Deferred formalization terms: logical axiom, axiomatization, disjointness, cardinality, reasoner-grade constraint, inverse formalization.
- `0.2.0`-batch core concepts (closed 2026-07-07, session-051): Abstract, Concrete, Universal, Time, Space, Aggregate, Sum, Boundary, Site, Quantity, Proposition.
- `0.3.0`-batch core concepts (closed 2026-07-07, session-051): Change, Continuous, Discrete, Ontological Level / Stratum, List / Sequence, Mind / Conscious Being / Agent, Non-physical Object, Disposition, Modality. Symbol / Sign / Representation is not included — it remains deliberately unplaced in `core.ttl`, so it has no glossary entry either.

### Circular Definitions

No unresolved circular definition is intentionally used as a definition. This glossary found relationship-pair cycles that are expected in the core scaffold but are not used as definitional dependencies:

| Pair | Resolution |
|---|---|
| `has part` / `part of` | Both definitions depend on the separately defined terms Entity, part, and whole; inverse formalization is deferred. |
| `participates in` / `has participant` | Both definitions depend on Continuant, Occurrent, and involved; inverse formalization is deferred. |
| `has quality` / `quality of` | Both definitions depend on Entity, Quality, characterizes, and bearer; dependence formalization is deferred. |
| `bears role` / `role of` | Both definitions depend on Entity, Role, context, and bearer; context/dependence axioms are deferred. |

### Provisional Terms

The following terms remain intentionally provisional because resolving them would exceed glossary closure and enter later formal-axiom work or later publication/governance work:

- dependence and dependence subtypes;
- part, whole, and mereological axioms;
- inverse formalization;
- disjointness, cardinality, and reasoner-grade constraints;
- Relation as a first-class Entity;
- Information Artifact as core ontology content versus metadata/provenance infrastructure;
- URI/IRI publication policy.

### Terms Assigned to Later Work

| Term or issue | Assigned to |
|---|---|
| Logical axioms, disjointness, inverse properties, transitivity, cardinality, and constraints | Later formal-axiom work |
| Process/Event relation and candidate axioms | Later formal-axiom work, with concept crosswalk evidence |
| Dependency subtypes for Quality, Role, and participation | Later formal-axiom work |
| Competency questions and example knowledge base validation | Competency-question and validation work |
| URI/IRI publication policy and namespace governance | Publication-policy work |
| Long-term status and change governance for glossary entries | Governance work |

## Editorial Normalization Notes

- Core concept preferred labels retain Title Case to match the core ontology's tables and Turtle labels.
- Core relationship preferred labels use lower-case verb phrases to match the core ontology's relationship labels.
- Local identifiers remain unchanged from the core ontology.
- This glossary does not add final SKOS mapping categories or source-specific correspondences; those remain in crosswalk artifacts.
