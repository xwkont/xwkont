# Standards Adoption Matrix

> **Status:** Discovery matrix, not an adoption decision  
> **Date:** 2026-06-30

## Purpose

This matrix compares surveyed standards against XwkOnt's documented purpose, scope, principles, and lifecycle. It records observations and candidate future dispositions only. It does not adopt standards.

## Matrix

| Standard | Candidate use area | Possible future disposition to evaluate | Rationale / observation | Evidence source |
|---|---|---|---|---|
| ISO/IEC 11179 | Metadata registry concepts for references, concepts, mappings, definitions, identifiers, and registration status | Reference or adapt selected concepts | Aligns with reusable registry-style metadata and provenance, but may be too broad for initial artifacts | ISO/IEC 11179-1:2023; ISO/IEC 11179-3:2023; `docs/EDITORIAL_POLICY.md`; `docs/ARCHITECTURAL_PRINCIPLES.md` |
| Dublin Core / DCMI Terms | Descriptive metadata for repository artifacts and reference records | Adopt or adapt selected terms | Aligns with editorial metadata needs for title, publisher, identifier, source, relation, rights, license, and dates | DCMI Metadata Terms; Dublin Core Metadata Element Set; `docs/EDITORIAL_POLICY.md` |
| W3C RDF | Graph data model for future crosswalk artifacts | Adopt, reference, or defer | Provides web graph foundations; relevant to concepts, references, ontologies, and mappings; not itself an XwkOnt model | RDF 1.1 Concepts and Abstract Syntax; `README.md`; `docs/ARCHITECTURAL_PRINCIPLES.md` |
| W3C RDFS | Vocabulary/schema description for RDF data | Adopt with RDF, reference, or defer | Provides lightweight vocabulary description capabilities that may support artifact schemas | RDF Schema 1.1; `docs/ARCHITECTURAL_PRINCIPLES.md` |
| W3C OWL | Formal ontology representation and ontology-aligned artifacts | Reference, adopt constrained use, or defer | Powerful formal semantics; must be bounded by XwkOnt's non-goal of creating a new foundational ontology | OWL 2 Overview; OWL 2 Primer; `README.md` |
| W3C SKOS | Concept schemes, labels, notes, and mapping relationships | Adopt, adapt selected properties, or reference | Strong apparent alignment with concept-centric crosswalks and mapping observations | SKOS Reference; `README.md`; `docs/ARCHITECTURAL_PRINCIPLES.md` |
| SPDX | License identifiers and license expression metadata | Adopt identifiers/expressions for metadata; separate project license ADR | Supports precise license metadata; does not decide the repository license | SPDX License List; SPDX License Expressions; `docs/EDITORIAL_POLICY.md` |
| CSL | Citation rendering styles | Reference or defer until publication workflow | Useful for formatting citations and bibliographies; less central to canonical metadata storage | CSL 1.0.2 Specification; `docs/EDITORIAL_POLICY.md` |
| BibTeX | Bibliographic import/export and academic interoperability | Reference, import/export support, or defer | Common academic format; may not satisfy all provenance/access metadata needs alone | BibTeXing; BibTeX project information; `docs/EDITORIAL_POLICY.md` |
| ISO 8601 | Dates, times, timestamps, access dates, artifact metadata | Adopt profile or adapt constrained usage | Supports unambiguous dates/times and aligns with UTC access-date requirement | ISO 8601-1:2019; ISO 8601-2:2019; `docs/EDITORIAL_POLICY.md` |
| RFC 2119 / RFC 8174 | Normative language in policies, specifications, templates, and contribution rules | Adopt BCP 14 language for normative docs or reference only | Improves requirement precision if boilerplate and uppercase rules are used deliberately | RFC 2119; RFC 8174; `docs/PROJECT_LIFECYCLE.md`; `docs/EDITORIAL_POLICY.md` |

## Comparison Against XwkOnt Goals and Principles

| Repository goal/principle | Relevant standards | Observation only |
|---|---|---|
| Concept-centric crosswalk | SKOS, RDF, RDFS, OWL | SKOS directly models concepts and mappings; RDF/RDFS provide graph and vocabulary foundations; OWL adds formal semantics that may exceed current documentation needs. |
| Source first and traceability | Dublin Core, ISO/IEC 11179, SPDX, ISO 8601, CSL, BibTeX | These standards cover metadata, provenance, licensing, dates, and citations that can help trace artifacts to authoritative references. |
| Neutrality and not creating a new foundational ontology | OWL, SKOS, RDF | Semantic web standards can represent crosswalk knowledge, but future adoption decisions must avoid turning XwkOnt into a new upper ontology. |
| Reuse before introduce | All surveyed standards | Every surveyed area has existing standards available for future evaluation before project-specific conventions are introduced. |
| Everything has provenance | Dublin Core, ISO/IEC 11179, SPDX, ISO 8601 | These standards may support future artifact provenance metadata. |
| Discovery before adoption | All surveyed standards | This survey records discovery only; a later adoption decision is the appropriate venue for disposition decisions. |

## Candidate ADR Topics for Future Work

1. Decide the baseline metadata vocabulary for XwkOnt reference and artifact records.
2. Decide whether RDF is adopted as the future graph data model for machine-readable crosswalk artifacts.
3. Decide whether SKOS is adopted or adapted for concept schemes and mapping relationships.
4. Decide the relationship among RDF, RDFS, SKOS, and OWL in future ontology-aligned artifacts.
5. Decide whether SPDX identifiers and expressions are used for license metadata.
6. Decide the repository license separately from SPDX metadata usage.
7. Decide a date/time representation profile for access dates and artifact metadata.
8. Decide whether BCP 14 normative language from RFC 2119 and RFC 8174 is used in normative project documents.
9. Decide whether CSL and/or BibTeX are supported for citation rendering, import, or export.

## Non-Adoption Statement

The possible dispositions above are candidate evaluation paths for a later adoption decision. They are not decisions and do not authorize implementation.
