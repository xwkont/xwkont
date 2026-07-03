# XwkOnt Standards Baseline

> **Status:** Accepted baseline, in active use  
> **Date:** 2026-06-30  

## Purpose

This document converts standards-discovery research into explicit, traceable dispositions for XwkOnt. It is a planning baseline for information architecture work, not an implementation specification.

The baseline follows ADR-0001's reuse-before-introduce rule. Project-specific conventions are introduced only where the surveyed standards do not by themselves answer an XwkOnt governance or documentation need.

## Disposition Vocabulary

- **Adopt:** Use the standard directly for the stated scope.
- **Adapt:** Use selected parts of the standard with documented XwkOnt constraints.
- **Reference:** Treat the standard as background or interoperability context, but do not make it a current project requirement.
- **Defer:** Make no current adoption decision; revisit at a named later milestone.
- **Reject:** Decide not to use the standard for the stated scope.

## Standards Disposition Matrix

| Standard | Disposition | Scope for XwkOnt | Decision record |
|---|---|---|---|
| ISO/IEC 11179 | Adapt | Use selected registry concepts such as administered item, identifier, definition, designation, provenance, and registration/status as conceptual guidance for future metadata records; do not implement the full metamodel now. | ADR-0003 |
| Dublin Core / DCMI Terms | Adopt | Use selected DCMI terms as the baseline descriptive metadata vocabulary for references and future repository artifacts, including title, creator/contributor where known, publisher, identifier, source/relation, rights/license, and dates. | ADR-0003 |
| RDF | Adopt | Use RDF as the future graph data model for machine-readable crosswalk artifacts and semantic-web interoperability; no RDF artifact implementation is required immediately. | ADR-0004 |
| RDFS | Adapt | Use selected RDFS vocabulary for lightweight class, property, label, comment, domain/range, and subclass/subproperty descriptions when RDF vocabularies are defined; do not require a complete schema immediately. | ADR-0004 |
| OWL | Reference | Reference OWL for imported ontology semantics and for future constrained formalization decisions; do not adopt OWL as the default modeling layer for XwkOnt artifacts now. | ADR-0004 |
| SKOS | Adopt | Use SKOS as the baseline concept-scheme and mapping vocabulary for future concept-centric crosswalk artifacts, especially labels, notes, concept schemes, and mapping relationships. | ADR-0004 |
| SPDX | Adopt | Use SPDX identifiers and expressions for license metadata when a license is known; this does not choose the repository license. | ADR-0005 |
| CSL | Defer | Defer citation-rendering style decisions until publication workflow or bibliography tooling is designed. | This baseline |
| BibTeX | Reference | Reference BibTeX as an academic bibliography interchange format; do not make it the canonical metadata model. | This baseline |
| ISO 8601 | Adapt | Use a constrained ISO 8601 profile for dates and timestamps in project metadata: calendar dates as `YYYY-MM-DD`; timestamps as UTC date-times with `Z` when time of day is required. | ADR-0006 |
| RFC 2119 / RFC 8174 | Adopt | Use BCP 14 normative keywords in normative project specifications and policies only when the RFC 8174 boilerplate is included and uppercase keywords are intentional. | ADR-0006 |
| MOF | Reference | Background for understanding ODM's meta-modeling foundation; XwkOnt uses no MOF-based tooling. | `docs/evaluations/meta-ontology-standards-evaluation.md` |
| ODM | Reference | Background only; XwkOnt authors Turtle directly rather than through a MOF/UML-based ontology metamodel. | `docs/evaluations/meta-ontology-standards-evaluation.md` |
| DOL | Reference | Related art for formally linking ontologies across logics; heavier formalization (OWL/Common Logic theory interpretation) than XwkOnt's current conservative RDF/RDFS/SKOS scope. | `docs/evaluations/meta-ontology-standards-evaluation.md` |
| Common Logic | Reference | Consistent with the existing OWL disposition in ADR-0004; XwkOnt does not adopt a formal logic layer. | `docs/evaluations/meta-ontology-standards-evaluation.md` |
| OMV | Defer | Revisit closed 2026-07-03: all 8 crosswalks and 16 reference records confirm DCMI-based fields plus prose are sufficient; no OMV-specific structured field has been needed. | `docs/evaluations/meta-ontology-standards-evaluation.md` |
| VoID | Reference | Relevant only if XwkOnt later produces multiple interlinked machine-readable datasets; explicitly deferred per the Information Architecture's machine-readable companion decision. | `docs/evaluations/meta-ontology-standards-evaluation.md` |
| SSSOM | Adapt | Use SSSOM's `predicate_id` and `mapping_justification` (SEMAPV) vocabulary for mapping assertions; retain XwkOnt's categorical confidence scale and human-readable Markdown records rather than SSSOM's numeric confidence or TSV serialization. | ADR-0009 |
| ISO 1087 | Adapt | Use the concept/term/designation distinction as justification for "Concept" as XwkOnt's organizing unit, distinct from source-specific "Term"; do not implement the full terminology-management apparatus (term records, equivalence relations, terminography workflow). | ADR-0011 |
| DOI (ISO 26324) | Adopt | Use DOIs as the preferred `Identifier or URL` value in reference records for formally published literature, refining the DCMI `identifier` field already adopted in ADR-0003. | ADR-0012 |
| Memento Protocol (RFC 7089) | Adapt | Use the underlying practice (timestamped, independently retrievable snapshots, e.g. Internet Archive Wayback Machine) for reference records without a DOI; do not implement Memento's TimeGate/TimeMap negotiation infrastructure. | ADR-0012 |

## Adopted Standards

### Dublin Core / DCMI Terms

XwkOnt adopts selected DCMI terms for baseline descriptive metadata. This adoption is scoped to metadata semantics, not to a required serialization. Which terms are mandatory, recommended, or optional for each artifact type is decided in the information architecture work (`docs/INFORMATION_ARCHITECTURE.md`).

### RDF

XwkOnt adopts RDF as the future graph data model for machine-readable semantic artifacts. This gives the information architecture work a stable interoperability target while preserving freedom to design human-readable documentation first.

### SKOS

XwkOnt adopts SKOS as the baseline vocabulary for concept schemes, labels, documentation notes, and mapping relationships. How SKOS concepts relate to repository pages, ontology references, and source-specific concept records is decided in the information architecture work (`docs/INFORMATION_ARCHITECTURE.md`).

### SPDX

XwkOnt adopts SPDX identifiers and expressions for license metadata where license information is known. Unknown, unclear, or custom license cases must remain explicit and traceable rather than guessed.

### RFC 2119 / RFC 8174

XwkOnt adopts BCP 14 requirement keywords for documents that intentionally define normative requirements. Informal roadmap, journal, and explanatory documents should avoid accidental uppercase normative keywords.

## Adapted Standards

### ISO/IEC 11179

XwkOnt adapts selected metadata-registry ideas from ISO/IEC 11179 rather than implementing the full standard. The adaptation is justified because XwkOnt needs traceable reference and concept records but does not yet need a complete metadata registry system.

### RDFS

XwkOnt adapts selected RDFS vocabulary as a lightweight description layer for future RDF vocabularies. The adaptation is justified because RDFS is useful for basic vocabulary documentation, while a complete schema belongs to later implementation work.

### ISO 8601

XwkOnt adapts ISO 8601 through a narrow project profile. Dates use `YYYY-MM-DD`; timestamps use UTC with `Z` when a time of day is needed. This avoids ambiguous local dates and overuse of rarely needed ISO 8601 extensions.

## Referenced Standards

### OWL

XwkOnt references OWL for understanding and potentially representing source ontologies with formal semantics. OWL is not currently adopted as XwkOnt's default modeling layer because the project must remain a neutral crosswalk and must not become a new foundational ontology.

### BibTeX

XwkOnt references BibTeX for import/export and academic interoperability. It is not the canonical metadata model because the editorial policy requires provenance, access, license, and relation metadata that may exceed a simple BibTeX record.

## Deferred Standards

### CSL

CSL is deferred because citation rendering is downstream of canonical reference metadata. The information architecture work does not need CSL, but a later publication-workflow decision may revisit it.

## Rejected Standards

No surveyed standard is rejected in this baseline.

## Project-Specific Conventions Introduced

This baseline introduces one project-specific convention: the disposition vocabulary `adopt`, `adapt`, `reference`, `defer`, and `reject`. This convention is justified because the surveyed standards do not provide a shared decision taxonomy for repository standards governance, and the vocabulary is needed to make standards-adoption decisions explicit and traceable.

## Deferred Questions

1. Which DCMI terms are mandatory, recommended, or optional for each artifact type?
2. How should ISO/IEC 11179-inspired status and identifier concepts appear in concept, reference, and mapping records?
3. What URI/IRI policy should XwkOnt use for concepts, source ontology terms, mappings, and repository artifacts?
4. What is the relationship between human-readable concept pages and future RDF/SKOS machine-readable artifacts?
5. Which SKOS mapping properties are acceptable for initial crosswalks, and when is a richer mapping note required?
6. When should OWL axioms be preserved, quoted, summarized, or represented in XwkOnt artifacts?
7. How should unknown, mixed, or custom licenses be represented with SPDX `LicenseRef` or explanatory metadata?
8. Should CSL be adopted for rendered bibliographies during later publication workflow?
9. Should BibTeX import/export be supported, and if so, how is it reconciled with DCMI-based canonical metadata?
