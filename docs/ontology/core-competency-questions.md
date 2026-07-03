# Core Ontology Competency Questions

> **Status:** Validation suite  
> **Date:** 2026-07-01  
> **Scope:** Conservative competency questions for the current XwkOnt core ontology scaffold.

## Purpose

This artifact records practical competency questions for validating whether the current core ontology is sufficient for near-term XwkOnt work. The questions test the lightweight RDF/RDFS/SKOS companion representation without converting XwkOnt into a new foundational ontology.

The suite is intentionally conservative:

- it tests XwkOnt's repository vocabulary, not any source ontology's final metaphysical commitments;
- it treats examples as illustrative and non-authoritative;
- it does not require OWL as the default modeling layer;
- it does not finalize URI/IRI publication policy;
- it uses competency questions to identify future modeling needs rather than answering them prematurely.

## Validation Assumptions

The questions assume the accepted logical-axiom policy:

1. Core classes and properties are declared in `data/ontology/core.ttl`.
2. Subclass relationships provide only a lightweight comparison scaffold.
3. RDFS domain and range statements support structural validation for core relationships.
4. `xwkont-core:mapsTo` is transitional and has no RDFS domain or range.
5. Relationship pairs such as `hasPart` / `partOf` are navigation pairs, not formal inverse-property axioms.
6. Process and Event remain sibling comparison concepts under Occurrent.
7. No disjointness, transitivity, cardinality, or other property-characteristic axioms are required for the current phase.

## Core Concept Group Questions

| ID | Concept group | Competency question | Expected behavior | Current status |
|---|---|---|---|---|
| CQ-C01 | Root comparison concept | Can XwkOnt identify the broad comparison root used for current core concepts? | `Entity` is declared as both `rdfs:Class` and `skos:Concept`. | Satisfied by current scaffold. |
| CQ-C02 | Continuant group | Can XwkOnt represent object-like, quality-like, and role-like comparison concepts as continuant-like without resolving source disputes? | `Object`, `Quality`, and `Role` are subclasses of `Continuant`; `Continuant` is a subclass of `Entity`. | Satisfied. |
| CQ-C03 | Occurrent group | Can XwkOnt represent process-like and event-like comparison concepts as occurrent-like without making them equivalent or disjoint? | `Process` and `Event` are subclasses of `Occurrent`; no equivalence, disjointness, or subclass relation between them is asserted. | Satisfied. |
| CQ-C04 | Relation support | Can XwkOnt discuss relationship types as comparison subjects while acknowledging source-dependent uncertainty? | `Relation` remains a subclass of `Entity` with editorial notes marking uncertainty. | Satisfied but should be revisited after relationship crosswalks. |
| CQ-C05 | Information artifact support | Can XwkOnt connect concepts, relationships, or claims to documentation artifacts? | `InformationArtifact` is available as a support concept and as the range of `documentedBy`. | Satisfied for lightweight provenance/documentation needs. |
| CQ-C06 | Candidate-concept neutrality | Can XwkOnt label concepts as candidates without treating them as final source-ontology categories? | SKOS definitions and editorial notes mark source-boundary uncertainty. | Satisfied. |

## Core Relationship Group Questions

| ID | Relationship group | Competency question | Expected behavior | Current status |
|---|---|---|---|---|
| CQ-R01 | Part-whole navigation | Can XwkOnt record broad part-whole examples for validation without adopting a complete mereology? | `hasPart` and `partOf` accept Entity-to-Entity structure; no transitivity or inverse entailment is required. | Satisfied. |
| CQ-R02 | Participation navigation | Can XwkOnt record that a continuant participates in an occurrent and that an occurrent has a participant? | `participatesIn` has Continuant domain and Occurrent range; `hasParticipant` has Occurrent domain and Continuant range. | Satisfied. |
| CQ-R03 | Quality-bearing navigation | Can XwkOnt record quality-bearing examples without asserting bearer uniqueness or existential dependence? | `hasQuality` and `qualityOf` provide structural direction only. | Satisfied; dependence refinements deferred. |
| CQ-R04 | Role-bearing navigation | Can XwkOnt record role-bearing examples without formalizing context, function, or disposition distinctions? | `bearsRole` and `roleOf` provide structural direction only. | Satisfied; context modeling deferred. |
| CQ-R05 | Dependency navigation | Can XwkOnt record that one entity depends on another without selecting a dependency subtype? | `dependsOn` accepts Entity-to-Entity examples; no transitivity, asymmetry, irreflexivity, or subtype taxonomy is asserted. | Satisfied; dependency taxonomy deferred. |
| CQ-R06 | Transitional mapping | Can XwkOnt avoid using `mapsTo` as a formal source mapping shortcut? | `mapsTo` remains declared but has no RDFS domain or range; new detailed mapping should prefer SKOS mapping properties or explicit mapping records. | Satisfied; mapping-record guidance still needed. |
| CQ-R07 | Documentation/provenance | Can XwkOnt attach documentation artifacts to concepts or example claims? | `documentedBy` links Entity to InformationArtifact. | Satisfied for current documentation support. |

## Axiom-Behavior Questions

| ID | Topic | Competency question | Expected behavior | Current status |
|---|---|---|---|---|
| CQ-A01 | Subclass scaffold | Do current subclass links allow simple class ancestry checks? | Direct and transitive superclass paths can be computed externally from `rdfs:subClassOf` triples. | Satisfied by structural check. |
| CQ-A02 | Domain/range behavior | Can validation identify property assertions whose subjects or objects are compatible with declared RDFS domains and ranges? | Example facts using formalized properties match declared local domain/range classes, with subclass closure considered. | Satisfied by illustrative example check. |
| CQ-A03 | No inverse axioms | Does asserting one direction of a paired relationship avoid automatically asserting the other direction? | Example validation must not require inverse triples unless explicitly present. | Satisfied; no inverse axioms exist. |
| CQ-A04 | No disjointness | Can examples remain valid even when a resource is typed in ways that would be controversial under some foundational ontologies? | No disjointness checks are performed or required. | Satisfied. |
| CQ-A05 | No transitivity/cardinality/property characteristics | Does validation avoid requiring inferred part chains, dependency chains, uniqueness, functionality, or mandatory values? | Checks are structural only and do not require property-characteristic entailments. | Satisfied. |
| CQ-A06 | Process/Event non-resolution | Can a validation example include both process-like and event-like resources without deciding their relationship? | Both can be typed under Occurrent subclasses; no equivalence, disjointness, or exhaustive partition is expected. | Satisfied. |
| CQ-A07 | OWL non-requirement | Is OWL unnecessary for current validation? | No blocking validation need requires OWL axioms or an OWL reasoner. | Satisfied. |

## Deferred Competency Questions

| ID | Deferred question | Why deferred | Recommended follow-up |
|---|---|---|---|
| DQ-01 | What is the project-standard mapping-record shape? | Mapping evidence, status, confidence, references, and source-specific claims need a dedicated design. | Later publication or crosswalk tooling work. |
| DQ-02 | Should any relationship pair become a formal inverse? | Source evidence and crosswalk requirements are not yet sufficient. | Revisit after first concept and relationship crosswalks. |
| DQ-03 | Should `hasPart` or `dependsOn` gain transitive or subtype semantics? | Broad core properties are too underspecified for safe global axioms. | Revisit after concrete crosswalk evidence. |
| DQ-04 | Should Process and Event be related more strongly? | Source ontologies differ; current project goal is comparison rather than resolution. | Revisit during Process/Event concept crosswalks. |
| DQ-05 | Should URI/IRI publication policy change current example namespace usage? | Publication policy is explicitly deferred. | Later publication-policy work. |
| DQ-06 | Should provenance use PROV-O or a custom record? | Current `documentedBy` is enough for documentation linkage, but not complete provenance. | Publication/governance planning after release needs are clearer. |

## Conclusion

The current lightweight RDFS/SKOS scaffold is sufficient for near-term repository validation, example-data checks, and concept-centric documentation. No blocking need was found for OWL as the default modeling layer, formal inverse properties, disjointness axioms, cardinality restrictions, transitive property axioms, or finalized URI/IRI publication policy.
