# XwkOnt Core Logical Axiom Notes

> **Local identifier:** `xwkont:ontology:core-axioms`  
> **Editorial status:** `draft`  
> **Created:** `2026-07-01`  
> **Inputs:** `docs/ontology/core-ontology.md`, `docs/ontology/core-glossary.md`, `data/ontology/core.ttl`  
> **Companion representation:** `data/ontology/core.ttl`

## Purpose

This artifact records the conservative logical-axiom review for the core ontology using the closed glossary. It distinguishes statements that are accepted as current lightweight formalization from statements that remain structural notes or are deferred.

XwkOnt remains a concept-centric crosswalk project. These notes do not create a new foundational ontology, settle disputes among BFO, DOLCE, SUMO, UFO, or other source ontologies, or invent source correspondences without crosswalk evidence.

## Formalization Policy

This review accepts only minimal axioms already justified by the core scaffold, closed glossary, and adopted representation standards.

The current formalization level is:

1. **RDF/SKOS identity and documentation statements** for the XwkOnt core concept scheme and vocabulary items.
2. **RDFS class declarations** for core comparison concepts.
3. **RDFS property declarations** for core relationship vocabulary.
4. **RDFS subclass links** only where the core ontology already used the parent relation as the organizing scaffold.
5. **RDFS domain and range hints** only where the relationship table and glossary provide enough support and where the inference is acceptable as a lightweight XwkOnt vocabulary constraint.

The current formalization level is not:

- OWL class definition or equivalence.
- Source-ontology reconciliation.
- Closed-world validation.
- A commitment that candidate XwkOnt classes are disjoint.
- A commitment that candidate XwkOnt properties are transitive, symmetric, asymmetric, reflexive, irreflexive, functional, inverse-functional, or cardinality-constrained.

## Candidate Inheritance Classification

Every candidate inheritance relationship from the core ontology was reviewed. All remain accepted as lightweight `rdfs:subClassOf` scaffold axioms because they organize XwkOnt comparison concepts without asserting source-ontology equivalence.

| Subject | Object | Classification | Treatment | Rationale |
|---|---|---|---|---|
| Continuant | Entity | Formalized | Keep `rdfs:subClassOf`. | Needed as a high-level comparison branch; uncertainty remains in labels and boundaries. |
| Occurrent | Entity | Formalized | Keep `rdfs:subClassOf`. | Needed as a high-level comparison branch; Process/Event treatment remains open. |
| Object | Continuant | Formalized | Keep `rdfs:subClassOf`. | The core ontology treats Object as a continuant-like comparison target. |
| Quality | Continuant | Formalized | Keep `rdfs:subClassOf`. | The core ontology and glossary treat Quality as a dependent continuant-like comparison target; dependence is not axiomatized. |
| Role | Continuant | Formalized | Keep `rdfs:subClassOf`. | The core ontology and glossary treat Role as a contextual continuant-like comparison target; context is not axiomatized. |
| Process | Occurrent | Formalized | Keep `rdfs:subClassOf`. | Needed to compare temporally extended activity or change; not asserted equivalent to Event. |
| Event | Occurrent | Formalized | Keep `rdfs:subClassOf`. | Needed to compare event-like categories; not asserted disjoint from or equivalent to Process. |
| Relation | Entity | Formalized, provisional | Keep `rdfs:subClassOf`; mark uncertainty. | Supports comparison of relationship concepts, but first-class relation status is source-dependent. |
| Information Artifact | Entity | Formalized, provisional | Keep `rdfs:subClassOf`; mark possible future refactor. | Supports repository provenance artifacts; metadata-layer migration remains open. |
| Abstract | Entity | Formalized, provisional | Keep `rdfs:subClassOf`. | Class-pair sibling of Continuant/Occurrent per maintainer-confirmed recommendation; boundary with Concrete deferred. |
| Concrete | Entity | Formalized, provisional | Keep `rdfs:subClassOf`. | Class-pair sibling of Continuant/Occurrent per the same recommendation; boundary with Abstract deferred. |
| Universal | Entity | Formalized, provisional | Keep `rdfs:subClassOf`. | Parallels GFO's top-level Category/Individual split; SUMO's narrower Abstract-subtype framing not formalized. |
| Time | Entity | Formalized, provisional | Keep `rdfs:subClassOf`. | Most sources treat Time as independent of Continuant/Occurrent; BFO alone classifies it as occurrent. |
| Space | Entity | Formalized, provisional | Keep `rdfs:subClassOf`. | Consistent with Time's placement; source classification diverges more (three-way split). |
| Aggregate | Continuant | Formalized, provisional | Keep `rdfs:subClassOf`. | Sibling of Object; one of two sibling sub-concepts with Sum, reflecting an even source split on unity-criterion strictness. |
| Sum | Continuant | Formalized, provisional | Keep `rdfs:subClassOf`. | Aggregate's sibling sub-concept. |
| Boundary | Continuant | Formalized, provisional | Keep `rdfs:subClassOf`. | One of two sibling sub-concepts with Site, reflecting BFO/DOLCE's independently-converging split. |
| Site | Continuant | Formalized, provisional | Keep `rdfs:subClassOf`. | Boundary's sibling sub-concept. |
| Quantity | Concrete | Formalized, provisional | Keep `rdfs:subClassOf`. | Modeled under Concrete per the DOLCE/UFO/GFO majority; covers multiple related but distinct source senses. |
| Proposition | Abstract | Formalized, provisional | Keep `rdfs:subClassOf`. | Follows DOLCE/SUMO/YAMATO's own treatment of Proposition/Content as an Abstract subtype. |

## Core Relationship Classification

| Relationship | Domain/range treatment | Inverse treatment | Property-characteristic treatment | Decision |
|---|---|---|---|---|
| `hasPart` | Formalized as Entity to Entity. | Structural note only with `partOf`; no formal inverse. | No transitivity, reflexivity, asymmetry, or cardinality. | Keep lightweight RDFS domain/range; defer mereology. |
| `partOf` | Formalized as Entity to Entity. | Structural note only with `hasPart`; no formal inverse. | No transitivity, reflexivity, asymmetry, or cardinality. | Keep lightweight RDFS domain/range; defer mereology. |
| `participatesIn` | Formalized as Continuant to Occurrent. | Structural note only with `hasParticipant`; no formal inverse. | No functionality or cardinality. | Keep lightweight RDFS domain/range; defer participation conditions. |
| `hasParticipant` | Formalized as Occurrent to Continuant. | Structural note only with `participatesIn`; no formal inverse. | No functionality or cardinality. | Keep lightweight RDFS domain/range; defer participation conditions. |
| `hasQuality` | Formalized as Entity to Quality. | Structural note only with `qualityOf`; no formal inverse. | No existential or cardinality constraint. | Keep lightweight RDFS domain/range; defer bearer-dependence axioms. |
| `qualityOf` | Formalized as Quality to Entity. | Structural note only with `hasQuality`; no formal inverse. | No functionality, existential dependence, or cardinality. | Keep lightweight RDFS domain/range; defer dependence semantics. |
| `bearsRole` | Formalized as Entity to Role. | Structural note only with `roleOf`; no formal inverse. | No context, functionality, or cardinality. | Keep lightweight RDFS domain/range; defer role context modeling. |
| `roleOf` | Formalized as Role to Entity. | Structural note only with `bearsRole`; no formal inverse. | No functionality, context, or cardinality. | Keep lightweight RDFS domain/range; defer role context modeling. |
| `dependsOn` | Formalized as Entity to Entity. | No inverse proposed. | No transitivity, asymmetry, irreflexivity, or dependency subtype axioms. | Keep lightweight RDFS domain/range; defer dependency taxonomy. |
| `mapsTo` | Deferred; no RDFS domain/range in the companion representation. | No inverse proposed. | No mapping strength, symmetry, transitivity, or equivalence characteristic. | Retain only as a deprecated-or-transitional documentation property while preferring SKOS mapping properties and crosswalk mapping records. |
| `documentedBy` | Formalized as Entity to Information Artifact. | No inverse proposed. | No functionality or cardinality. | Keep lightweight RDFS domain/range; defer provenance model. |

## Accepted Axioms

The accepted axioms for this review are the RDFS class, property, subclass, domain, and range statements now present in `data/ontology/core.ttl`, except that `mapsTo` deliberately has no accepted domain or range axiom. This includes the eleven classes added for the `0.2.0` batch (Abstract, Concrete, Universal, Time, Space, Aggregate, Sum, Boundary, Site, Quantity, Proposition) — see `docs/ontology/core-ontology.md`'s Top-Level Concepts table for their per-class rationale and each concept's own crosswalk (linked via `dcterms:relation`) for the underlying source-ontology evidence.

These axioms are accepted as lightweight vocabulary semantics only. They should be interpreted under RDF/RDFS open-world assumptions and should not be read as OWL definitions or source-ontology commitments.

## Deliberately Not Formalized

### Disjointness

No class disjointness is asserted. In particular, this review does not assert that Continuant and Occurrent are disjoint, that Process and Event are disjoint, or that Object, Quality, and Role are pairwise disjoint. Such axioms would resolve foundational-ontology disputes prematurely.

### Process/Event Relation

Process and Event remain sibling comparison concepts under Occurrent. This review does not assert equivalence, subclassing between them, overlap, disjointness, or exhaustive partitioning. The glossary confirms that both are occurrent-like but records unsettled source boundaries.

### Property Inverses

No formal inverse property axioms are asserted. Relationship pairs remain useful navigation and documentation pairs, but formal inverses are deferred until competency questions and crosswalk evidence show that inverse entailments are safe.

### Transitivity and Other Property Characteristics

No property is asserted transitive, symmetric, asymmetric, reflexive, irreflexive, functional, inverse-functional, or cardinality-constrained. The main risk is overloading broad comparison properties such as `hasPart` and `dependsOn` with source-specific semantics.

### Cardinality and Existential Restrictions

No class is required to have any relationship value. For example, this review does not assert that every Quality has exactly one bearer, every Role has a bearer, every Occurrent has a participant, or every Information Artifact documents something.

### Source Correspondences

No new correspondences to BFO, DOLCE, SUMO, UFO, or another source ontology are introduced. Source-specific mapping remains assigned to concept crosswalk artifacts.

## `mapsTo` Review

This review finds that `mapsTo` should not carry core RDFS domain and range axioms. The project has already adopted SKOS for concept-centric representation and crosswalk records for mapping evidence. A broad core property named `mapsTo` risks becoming an untyped shortcut for multiple mapping strengths and evidence states.

Decision:

- Keep `xwkont-core:mapsTo` declared for backward traceability to the core ontology and glossary.
- Remove its RDFS domain and range from the Turtle companion representation.
- Mark it as transitional and non-preferred for new detailed mapping work.
- Prefer SKOS mapping properties for concept-level mappings where their semantics fit.
- Prefer explicit crosswalk mapping records when evidence, source references, mapping status, uncertainty, or non-concept relationships must be documented.

No ADR is required now because this applies ADR-0004 and the accepted information architecture rather than changing project direction. A future ADR may be needed if XwkOnt defines a custom mapping-record model that materially changes representation policy.

## Validation Notes

This review's validation was structural and representation-level:

1. Confirmed repository cleanliness before this review.
2. Reviewed required governance, standards, methodology, ADR, core ontology, glossary, Turtle, and diagram inputs.
3. Attempted RDFLib Turtle parsing; RDFLib was unavailable and package installation was blocked by the environment.
4. Ran a local structural Turtle checker for declarations and references.
5. Checked that every local class used in `rdfs:subClassOf`, `rdfs:domain`, and `rdfs:range` is declared as an `rdfs:Class`.
6. Checked that every local property expected from the core ontology and glossary is declared as `rdf:Property`.
7. Checked that `mapsTo` no longer has RDFS domain or range axioms.

Reasoner-grade OWL consistency checking remains deferred because this review intentionally avoids OWL axioms.

## Open Modeling Questions and Follow-up

| Question | Current answer | Follow-up |
|---|---|---|
| Should Process and Event be related more strongly? | No; keep siblings under Occurrent. | Revisit during concept crosswalk and competency-question work. |
| Should `mapsTo` remain in core? | Only as transitional documentation; avoid formal domain/range. | Define mapping records and SKOS usage in crosswalk/publication work. |
| Should `Relation` remain under Entity? | Keep provisional subclass scaffold. | Revisit after relationship concept crosswalks. |
| Should `Information Artifact` remain under Entity? | Keep provisional support concept. | Revisit during publication/provenance planning. |
| Which dependency subtypes are needed? | None formalized now. | Revisit after competency questions identify required distinctions. |
| Should XwkOnt adopt OWL axioms? | Not now. | Revisit only when validation requirements require OWL semantics. |
