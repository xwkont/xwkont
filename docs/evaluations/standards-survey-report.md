# Standards Survey Report

> **Status:** Discovery finding, not an adoption decision  
> **Date:** 2026-06-30

## Purpose

This report surveys established metadata, semantic web, citation, licensing, date/time, and normative-language standards that may be evaluated for future XwkOnt adoption. It records authoritative sources, purpose and scope, potentially relevant portions, and discovery observations.

## Scope and Method

The survey uses repository governance as the Single Source of Truth and compares standards against XwkOnt's documented goal to be a neutral, source-first, traceable, concept-centric crosswalk across foundational ontologies. Findings below separate standard facts from XwkOnt interpretation. No standard is adopted by this report.

## Provenance Classification

All surveyed standards are classified as **Referenced** at this discovery stage because they are external authoritative materials reviewed for possible future adoption, adaptation, reference-only use, or rejection during a later adoption decision.

## Survey Findings

### ISO/IEC 11179 — Metadata Registries

- **Authoritative source:** ISO/IEC 11179-1:2023, *Information technology — Metadata registries (MDR) — Part 1: Framework*, ISO, https://www.iso.org/standard/78914.html; ISO/IEC 11179-3:2023, *Part 3: Metamodel for registry common facilities*, ISO, https://www.iso.org/standard/78915.html.
- **Purpose and scope facts:** ISO describes Part 1 as the foundation for conceptual understanding of metadata and metadata registries and says ISO/IEC 11179 metadata means descriptions of data. ISO describes Part 3 as specifying information to be recorded in a metadata registry as a conceptual data model.
- **Potentially relevant portions:** Registry concepts, administered items, identification, registration status, naming and identification principles, data definitions, and common registry attributes may be relevant to future XwkOnt reference records, concept records, mapping records, and provenance metadata.
- **XwkOnt interpretation:** ISO/IEC 11179 appears relevant where XwkOnt needs reusable, traceable records about references, concepts, mappings, definitions, and registry status. It may be heavier than needed for early documentation artifacts.
- **Discovery notes:** A later adoption decision should decide whether XwkOnt references selected concepts, adapts a subset, or adopts a registry model.

### Dublin Core / DCMI Metadata Terms

- **Authoritative source:** DCMI Metadata Terms, Dublin Core Metadata Initiative, https://www.dublincore.org/specifications/dublin-core/dcmi-terms/; Dublin Core Metadata Element Set, Version 1.1, DCMI, https://www.dublincore.org/specifications/dublin-core/dces/.
- **Purpose and scope facts:** DCMI identifies DCMI Metadata Terms as the authoritative specification of metadata terms maintained by DCMI. The element set provides a compact descriptive metadata vocabulary.
- **Potentially relevant portions:** `title`, `creator`, `publisher`, `identifier`, `source`, `relation`, `references`, `license`, `rights`, `created`, `modified`, `issued`, `description`, `subject`, `type`, and `provenance` may be relevant to repository artifacts and external reference metadata.
- **XwkOnt interpretation:** Dublin Core appears well aligned with XwkOnt's editorial policy requirement that external references record title, publisher, URL, accessed date, version or edition, and license when known.
- **Discovery notes:** A later adoption decision should evaluate whether DCMI Terms become the baseline metadata vocabulary for reference and artifact records.

### W3C RDF — Resource Description Framework

- **Authoritative source:** RDF 1.1 Concepts and Abstract Syntax, W3C Recommendation, https://www.w3.org/TR/rdf11-concepts/.
- **Purpose and scope facts:** W3C defines RDF as a framework for representing information on the Web and defines an abstract data model linking RDF-based languages and specifications. RDF graphs are sets of subject-predicate-object triples.
- **Potentially relevant portions:** RDF graphs, IRIs, literals, blank nodes, datasets, datatypes, and graph equivalence may be relevant to future machine-readable crosswalk artifacts.
- **XwkOnt interpretation:** RDF appears foundational for graph-shaped representation of ontology concepts, references, and mappings. It does not by itself provide XwkOnt-specific modeling commitments.
- **Discovery notes:** A later adoption decision should decide whether RDF is adopted as a data model, referenced only for semantic web compatibility, or deferred until information architecture.

### W3C RDFS — RDF Schema

- **Authoritative source:** RDF Schema 1.1, W3C Recommendation, https://www.w3.org/TR/rdf-schema/.
- **Purpose and scope facts:** W3C describes RDF Schema as a data-modeling vocabulary for RDF data and an extension of the basic RDF vocabulary.
- **Potentially relevant portions:** `rdfs:Class`, `rdfs:subClassOf`, `rdfs:subPropertyOf`, `rdfs:domain`, `rdfs:range`, `rdfs:label`, `rdfs:comment`, `rdfs:seeAlso`, and `rdfs:isDefinedBy` may be relevant to describing future vocabularies and documentation metadata.
- **XwkOnt interpretation:** RDFS could support lightweight vocabulary description for XwkOnt artifacts without requiring the stronger expressivity of OWL.
- **Discovery notes:** A later adoption decision should evaluate whether RDFS is adopted together with RDF or deferred until ontology artifact design.

### W3C OWL — Web Ontology Language

- **Authoritative source:** OWL 2 Web Ontology Language Document Overview, W3C Recommendation, https://www.w3.org/TR/owl2-overview/; OWL 2 Web Ontology Language Primer, W3C Recommendation, https://www.w3.org/TR/owl2-primer/.
- **Purpose and scope facts:** W3C describes OWL 2 as an ontology language for the Semantic Web with formally defined meaning. OWL 2 ontologies provide classes, properties, individuals, and data values and are primarily exchanged as RDF documents.
- **Potentially relevant portions:** ontology declarations, classes, object properties, annotation properties, imports, equivalence and disjointness constructs, and profiles may be relevant to future ontology-aligned artifacts.
- **XwkOnt interpretation:** OWL may be relevant where XwkOnt needs formal ontology representations or precise relationships, but XwkOnt's current scope is to document and compare existing ontologies rather than create a new foundational ontology.
- **Discovery notes:** A later adoption decision should distinguish possible OWL use for artifact representation from prohibited creation of a new foundational ontology.

### W3C SKOS — Simple Knowledge Organization System

- **Authoritative source:** SKOS Simple Knowledge Organization System Reference, W3C Recommendation, https://www.w3.org/TR/skos-reference/.
- **Purpose and scope facts:** W3C defines SKOS as a common data model for sharing and linking knowledge organization systems such as thesauri, taxonomies, classification schemes, and subject-heading systems via the Web.
- **Potentially relevant portions:** `skos:Concept`, `skos:ConceptScheme`, preferred and alternative labels, definitions, notes, broader/narrower/related relationships, semantic relations, collections, and mapping properties may be relevant to concept-centric crosswalks.
- **XwkOnt interpretation:** SKOS appears highly aligned with XwkOnt's concept-centric navigation and crosswalk mapping needs, especially for labels, definitions, concept schemes, and mapping relationships.
- **Discovery notes:** A later adoption decision should evaluate whether SKOS mapping properties are sufficient for crosswalk semantics or need adaptation/reference alongside RDF/RDFS/OWL.

### SPDX — License Identification and License Metadata

- **Authoritative source:** SPDX License List, SPDX, https://spdx.org/licenses/; SPDX Specification v2.3 License Expressions, https://spdx.github.io/spdx-spec/v2.3/SPDX-license-expressions/.
- **Purpose and scope facts:** SPDX states that the SPDX License List is part of the SPDX Specification and provides standardized short identifiers, full names, license text, and canonical permanent URLs for commonly found licenses and exceptions. SPDX license expressions define combinations of identifiers, exceptions, and operators.
- **Potentially relevant portions:** SPDX license identifiers, license list entries, exceptions, `LicenseRef`, and license expression operators may be relevant to repository licensing and reference metadata.
- **XwkOnt interpretation:** SPDX appears useful for unambiguous license metadata, but it does not decide which license XwkOnt should use.
- **Discovery notes:** A later adoption decision should treat project license choice as a separate ADR topic from any decision to use SPDX identifiers in metadata.

### CSL — Citation Style Language

- **Authoritative source:** CSL 1.0.2 Specification, Citation Style Language, https://docs.citationstyles.org/en/stable/specification.html; Citation Style Language project site, https://citationstyles.org/.
- **Purpose and scope facts:** CSL describes itself as an XML-based format for formatting citations, notes, and bibliographies, with support for style requirements, localization, distribution, and updating.
- **Potentially relevant portions:** citation item variables, bibliographic metadata expectations, style definitions, locale support, and processor-independent citation formatting may be relevant to rendered reference lists.
- **XwkOnt interpretation:** CSL appears relevant to formatting references for publication, but not necessarily to storing canonical reference metadata.
- **Discovery notes:** A later adoption decision should evaluate whether CSL is needed now, or whether reference metadata decisions should precede citation rendering decisions.

### BibTeX — Bibliographic Records

- **Authoritative source:** BibTeXing, Oren Patashnik, CTAN, https://ctan.org/pkg/bibtex; BibTeX project information, https://www.bibtex.org/.
- **Purpose and scope facts:** BibTeX is a long-standing TeX/LaTeX bibliography tool and flat-file bibliographic database format for storing bibliographic entries and formatting them with bibliography styles.
- **Potentially relevant portions:** entry types, citation keys, and common fields such as author, title, publisher, year, URL, and note may be relevant to importing or exporting bibliographic references.
- **XwkOnt interpretation:** BibTeX may be useful for interoperability with academic workflows, but its field model may not cover all provenance and access metadata required by the editorial policy without extensions or complementary metadata.
- **Discovery notes:** A later adoption decision should decide whether BibTeX is an exchange/import/export format, a reference-only format, or out of scope for initial implementation.

### ISO 8601 — Date and Time Representation

- **Authoritative source:** ISO 8601-1:2019, *Date and time — Representations for information interchange — Part 1: Basic rules*, ISO, https://www.iso.org/standard/70907.html; ISO 8601-2:2019, *Part 2: Extensions*, ISO, https://www.iso.org/standard/70908.html.
- **Purpose and scope facts:** ISO 8601 covers representations of dates and times for information interchange. It is intended to reduce ambiguity in date and time communication.
- **Potentially relevant portions:** calendar dates, local time, UTC designator, offsets, date-time combinations, intervals, durations, and recurring intervals may be relevant to reference access dates, publication dates, modification dates, and artifact metadata.
- **XwkOnt interpretation:** ISO 8601 appears relevant to XwkOnt's editorial policy requirement for accessed dates in UTC and to future metadata timestamps.
- **Discovery notes:** A later adoption decision should decide which ISO 8601 profiles or date granularity expectations, if any, are adopted.

### RFC 2119 and RFC 8174 — Normative Language

- **Authoritative source:** RFC 2119, *Key words for use in RFCs to Indicate Requirement Levels*, IETF, https://www.rfc-editor.org/rfc/rfc2119; RFC 8174, *Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words*, IETF, https://www.rfc-editor.org/rfc/rfc8174.
- **Purpose and scope facts:** RFC 2119 defines requirement-level keywords such as MUST, SHOULD, and MAY for use in standards-track documents. RFC 8174 clarifies that only uppercase usage has the defined special meaning when the BCP 14 boilerplate is included.
- **Potentially relevant portions:** keyword definitions, capitalization rules, and BCP 14 boilerplate may be relevant to future normative XwkOnt specifications, policies, templates, and contribution rules.
- **XwkOnt interpretation:** BCP 14 language could improve precision in normative repository documents, but casual use of uppercase keywords without boilerplate may create ambiguity.
- **Discovery notes:** A later adoption decision should decide whether and where BCP 14 normative language is adopted.

## Cross-Standard Observations

- Metadata needs may span ISO/IEC 11179, Dublin Core, SPDX, ISO 8601, CSL, and BibTeX.
- Semantic representation needs may span RDF, RDFS, OWL, and SKOS.
- SKOS appears closest to the current concept-centric crosswalk purpose, while RDF appears foundational for graph representation.
- OWL appears powerful but requires careful governance because XwkOnt is not intended to create a new foundational ontology.
- Normative-language precision is a governance/documentation concern, not an ontology modeling concern.

## Non-Adoption Statement

This report does not adopt, adapt, reject, or implement any surveyed standard. It provides evidence for a later standards-adoption decision.
