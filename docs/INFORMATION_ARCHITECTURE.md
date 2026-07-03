# XwkOnt Information Architecture

> **Status:** Accepted specification, in active use  
> **Date:** 2026-06-30  
> **Standards baseline:** `docs/STANDARDS_BASELINE.md`, ADR-0003 through ADR-0006

## Normative Language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** in this document are to be interpreted as described in BCP 14, RFC 2119 and RFC 8174, when, and only when, they appear in all capitals.

## Purpose

This specification defines the repository information architecture XwkOnt needs before authoring its first complete concept crosswalk. It keeps XwkOnt neutral: XwkOnt documents relationships among source ontologies and terminology systems; it does not create a new foundational ontology.

## Repository Layout

The following layout is the canonical organization for crosswalk work:

| Path | Purpose | Initial status |
|---|---|---|
| `docs/crosswalks/concepts/` | Human-readable concept crosswalk artifacts. | Populated; see `docs/crosswalks/concepts/`. |
| `docs/methodology/` | Crosswalk method, metadata rules, and editorial guidance. | In use. |
| `docs/references/` | Repository-local reference records for sources cited by crosswalks. | In use. |
| `data/` | Future machine-readable companion artifacts. | Planned, with implementation deferred. |
| `data/crosswalks/` | Future RDF/SKOS/JSON-LD or other graph-compatible crosswalk companions. | Deferred. |
| `data/references/` | Future machine-readable reference metadata companions. | Deferred. |

Human-readable Markdown is canonical for crosswalk content. Machine-readable companions are planned so file identity and field names remain export-friendly, but no RDF, JSON-LD, OWL, Turtle, or validation implementation is required yet.

## Artifact Identity Rules

### Slugs and File Names

- Artifact slugs **MUST** use lowercase ASCII letters, digits, and hyphens only: `^[a-z0-9]+(-[a-z0-9]+)*$`.
- Concept crosswalk files **MUST** be named `<concept-slug>.md` and stored in `docs/crosswalks/concepts/`.
- Methodology documents **SHOULD** use descriptive lowercase hyphenated names in `docs/methodology/`.
- Reference records **MUST** use repository-local reference identifiers as file names, such as `ref-bfo-2020.md`.
- Future machine-readable companions **SHOULD** reuse the same base slug or reference identifier as the human-readable canonical artifact.

### Stable Local Identifiers

| Artifact type | Identifier pattern | Example |
|---|---|---|
| Concept crosswalk | `xwkont:concept:<slug>` | `xwkont:concept:continuant` |
| Mapping assertion | `xwkont:mapping:<concept-slug>:<nnn>` | `xwkont:mapping:continuant:001` |
| Source correspondence | `xwkont:correspondence:<concept-slug>:<nnn>` | `xwkont:correspondence:continuant:001` |
| Reference record | `xwkont:ref:<slug>` | `xwkont:ref:bfo-2020` |
| Review event | `xwkont:review:<concept-slug>:<YYYY-MM-DD>:<nn>` | `xwkont:review:continuant:2026-07-01:01` |

These identifiers are local project identifiers, not web IRIs. A future URI/IRI policy may map them to dereferenceable identifiers without changing the local identity semantics.

### Editorial Status Values

Concept crosswalks and reference records **MUST** use one of these status values:

| Status | Meaning |
|---|---|
| `draft` | Work is incomplete and not ready for crosswalk review. |
| `candidate` | Content is complete enough for substantive review. |
| `reviewed` | Content has passed project review for its stated scope. |
| `accepted` | Content is accepted as the current XwkOnt record for its scope. |
| `superseded` | Content has been replaced by a newer artifact. |
| `deprecated` | Content is retained for history but should not guide new work. |

Status values adapt ISO/IEC 11179 registration-status thinking without implementing the full registry model.

### Date Fields

Project-controlled date fields **MUST** follow the ISO 8601 profile adopted in ADR-0006:

- Calendar dates use `YYYY-MM-DD`.
- Timestamps use UTC date-times ending in `Z` when a time of day is required.
- Approximate, uncertain, reduced-precision, interval, duration, season, and repeating date forms are not used in normalized project fields unless a later ADR permits them.

When a source provides an ambiguous or non-profile date, record the source-native date as a quoted or paraphrased note and leave the normalized date unknown unless it can be established without guessing.

## Canonical Concept Crosswalk Template

The canonical template lives at `docs/crosswalks/concepts/TEMPLATE.md`. A new concept crosswalk copies it to `docs/crosswalks/concepts/<concept-slug>.md` and replaces placeholders without deleting required sections.

## Metadata Rules by Template Section

### 1. Identity and Editorial Status

| Field | Level | Cardinality | Expected content | Standards relationship |
|---|---|---:|---|---|
| Local identifier | Required | 1 | `xwkont:concept:<slug>`. | ISO/IEC 11179-inspired identifier. |
| Slug | Required | 1 | File-name-safe slug. | Project identity rule. |
| Title | Required | 1 | Human-readable title. | DCMI `title`; SKOS `prefLabel` candidate. |
| Editorial status | Required | 1 | Controlled status value. | ISO/IEC 11179-inspired registration status. |
| Created | Required | 1 | ISO-profile date. | DCMI `created`; ADR-0006. |
| Modified | Recommended | 0..1 | ISO-profile date for latest substantive edit. | DCMI `modified`; ADR-0006. |
| Contributors | Recommended | 0..n | Names or handles when known. | DCMI `contributor`. |
| Scope note | Required | 1 | What the crosswalk compares and what it does not compare. | SKOS `scopeNote`. |

### 2. Labels, Alternate Labels, and Source Terminology

Required content includes the XwkOnt working label and source-specific terms being compared. Recommended content includes alternate labels and source language tags. Optional content includes editorial abbreviations. Deferred content includes final multilingual label policy.

Use SKOS label concepts as guidance: preferred labels correspond to `skos:prefLabel`, alternate labels to `skos:altLabel`, and hidden search forms to `skos:hiddenLabel` only in future machine-readable companions.

### 3. Source Definitions and Contextual Notes

Each source definition entry is repeatable and includes source ontology, term identifier or locator, quotation or paraphrase type, definition text or summary, citation, and contextual notes. Direct quotations require a reference record and location detail when available. Paraphrases and summaries identify the cited source but do not use quotation marks.

Per `ADR-0010`, each entry also records a `Dimension`: `technical` (formal/engineering representation — class hierarchy, properties, domain/range, formalism used), `philosophical` (metaphysical/theoretical commitments — realism vs. conceptualism, endurantism vs. perdurantism, cognitive/linguistic orientation, stance on universals, etc.), or `both`. At least one `philosophical`-dimension entry is expected per source where the source's own documentation discusses its theoretical grounding; do not infer a stance the source does not document.

### 4. Source Ontology Correspondences

Each correspondence records a source term, source-local identifier or IRI if known, source version, source reference, and the reason it is included. Correspondence records do not by themselves assert equivalence.

### 5. Semantic Comparison Notes

Semantic comparison notes capture editorial observations about similarities, differences, assumptions, modeling context, and relevant source axioms. Notes are repeatable and classify the claim type as `direct quotation`, `paraphrase`, `editorial observation`, or `inference`.

Per `ADR-0010`, each note also records a `Dimension` (`technical`/`philosophical`/`both`), distinguishing observations about formal representation from observations about underlying metaphysical commitments. This records what a source's stance is, never which stance is correct (`docs/ARCHITECTURAL_PRINCIPLES.md`, Neutrality).

### 6. Mapping Assertions or Candidate Relations

Each mapping assertion has a local mapping identifier, subject source term, object source term, relation category, `predicate_id`, `mapping_justification`, status, confidence, rationale, provenance, and reviewer notes. SKOS mapping properties are used when they are appropriate, but richer notes are required whenever SKOS alone is too coarse.

Per `ADR-0009` (amending this section): `predicate_id` records the SSSOM/SKOS predicate corresponding to the relation category where one exists (see `docs/methodology/crosswalk-methodology.md`); XwkOnt-only categories (`overlap`, `incompatible`, `unknown`, `explicit-non-equivalence`) have no `predicate_id`. `mapping_justification` records a SEMAPV vocabulary term describing how the mapping was derived (commonly `semapv:ManualMappingCuration`), distinct from the prose `rationale` field. Confidence remains the existing categorical scale (`high`/`medium`/`low`/`unknown`), not SSSOM's numeric scale.

### 7. Uncertainty, Non-Equivalence, and Open Questions

Uncertainty records are first-class content, not defects. Record unresolved ambiguity, explicit non-equivalence, incompatible modeling assumptions, missing evidence, and questions for future review. Do not convert uncertainty into equivalence for convenience.

### 8. Provenance and References

Every source claim, quotation, paraphrase, mapping assertion, and inference links to one or more repository-local reference identifiers. Unknown, ambiguous, or missing metadata is recorded as `unknown` with an explanatory note; contributors do not guess.

### 9. Review History and Future Work

Review history records review event identifiers, dates, participants, outcome, and notes. Future work distinguishes required fixes for acceptance from optional improvements and later machine-readable representation tasks.

## Provenance and Reference Requirements

Reference records live in `docs/references/` and use the template at `docs/references/TEMPLATE.md`. Each reference record includes:

- local reference identifier;
- title;
- creator, contributor, and publisher when known;
- source type;
- version or edition when known;
- source identifier or URL when available;
- access date for web resources;
- rights or license metadata using SPDX identifiers or expressions when known;
- explicit notes for unknown, ambiguous, mixed, or custom rights information;
- source relation notes when one reference supersedes, translates, republishes, or quotes another.

Claim typing rules:

| Claim type | Use when | Required provenance |
|---|---|---|
| `direct quotation` | Text is copied verbatim from a source. | Reference identifier, locator when available, quotation boundaries. |
| `paraphrase` | Source meaning is restated without verbatim wording. | Reference identifier and note that wording is editorial. |
| `editorial observation` | XwkOnt records a comparison visible from cited evidence. | References supporting the observation and reviewer identity/date when available. |
| `inference` | XwkOnt derives a conclusion from multiple pieces of evidence. | References, inference rationale, uncertainty/confidence. |

## Crosswalk Methodology

Mapping categories are defined in `docs/methodology/crosswalk-methodology.md`. Concept crosswalks use these categories:

| XwkOnt category | SKOS relationship | Meaning |
|---|---|---|
| `exact-equivalence-candidate` | `skos:exactMatch` candidate | Evidence suggests interchangeability in the scoped context, pending review. |
| `close-match` | `skos:closeMatch` | Concepts are substantially similar but not safely interchangeable. |
| `broader-than` | `skos:broadMatch` from narrower to broader target, or inverse note | One concept is broader in the compared context. |
| `narrower-than` | `skos:narrowMatch` from broader to narrower target, or inverse note | One concept is narrower in the compared context. |
| `related` | `skos:relatedMatch` | Concepts are associated but not hierarchical or equivalent. |
| `overlap` | No direct SKOS mapping property; use note. | Concepts share some extension or intent but each has unmatched parts. |
| `incompatible` | No direct SKOS mapping property; use explicit note. | Modeling assumptions conflict for the scoped comparison. |
| `unknown` | No SKOS assertion. | Evidence is insufficient to classify relation. |
| `explicit-non-equivalence` | No SKOS mapping property; use note. | XwkOnt records that equivalence should not be asserted. |

Confidence values are `high`, `medium`, `low`, and `unknown`. Confidence is not a substitute for evidence; it summarizes review judgment for a scoped assertion.

## Machine-Readable Companion Decision

Machine-readable companion artifacts are **planned and deferred**. The human-readable Markdown crosswalk is canonical. Future companion artifacts should target RDF/SKOS-compatible representation and may use JSON-LD, Turtle, or another RDF serialization after a later implementation decision. This specification does not prototype machine-readable exports because the template is feasible without them and premature serialization could constrain crosswalk work unnecessarily.

## Crosswalk Readiness Checklist

Before starting a new concept crosswalk, confirm:

1. The crosswalk concept slug and local identifier are chosen.
2. The canonical template has been copied without removing required sections.
3. Candidate source ontologies and source terms are listed.
4. Repository-local reference records exist for every source expected to be quoted or paraphrased.
5. Source version, access date, and rights/license metadata have been recorded where known.
6. Unknown metadata has been marked explicitly rather than guessed.
7. The mapping categories and confidence values in the methodology are sufficient for the chosen concept.
8. Any direct quotations include locator information where available and remain copyright-conscious.
9. Open questions and non-equivalence risks have a place in the artifact before mapping assertions are drafted.
10. Machine-readable export work remains out of scope unless a later decision explicitly changes that scope.
