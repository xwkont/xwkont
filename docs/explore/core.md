# Core hierarchy

Interactive Mermaid view of the XwkOnt core comparison scaffold (from [`core-ontology.mmd`](https://github.com/xwkont/xwkont/blob/main/docs/ontology/core-ontology.mmd)). This is a navigation vocabulary for crosswalks — not a replacement foundational ontology.

```mermaid
classDiagram
    Entity <|-- Continuant
    Entity <|-- Occurrent
    Entity <|-- Relation
    Entity <|-- InformationArtifact
    Entity <|-- Abstract
    Entity <|-- Concrete
    Entity <|-- Universal
    Entity <|-- Time
    Entity <|-- Space
    Entity <|-- Change
    Entity <|-- Continuous
    Entity <|-- Discrete
    Entity <|-- OntologicalLevelStratum
    Entity <|-- ListSequence
    Continuant <|-- Object
    Continuant <|-- Quality
    Continuant <|-- Role
    Continuant <|-- Aggregate
    Continuant <|-- Sum
    Continuant <|-- Boundary
    Continuant <|-- Site
    Continuant <|-- MindConsciousBeingAgent
    Continuant <|-- NonPhysicalObject
    Continuant <|-- Disposition
    Continuant <|-- SituationStateOfAffairs
    Occurrent <|-- Process
    Occurrent <|-- Event
    Concrete <|-- Quantity
    Abstract <|-- Proposition
    Quality <|-- Modality
    Universal <|-- SymbolSignRepresentation

    Entity --> Entity : hasPart / partOf
    Continuant --> Occurrent : participatesIn
    Occurrent --> Continuant : hasParticipant
    Entity --> Quality : hasQuality
    Quality --> Entity : qualityOf
    Entity --> Role : bearsRole
    Role --> Entity : roleOf
    Entity --> Entity : symbolizes / symbolizedBy
    Entity --> Entity : dependsOn
    Entity --> InformationArtifact : documentedBy
```

Human-readable specification: [core ontology](../ontology/core-ontology.md). Machine companion: [`core.ttl`](https://github.com/xwkont/xwkont/blob/main/data/ontology/core.ttl).
