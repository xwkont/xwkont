# <Concept Crosswalk Title>

> **Local identifier:** `xwkont:concept:<slug>`  
> **Slug:** `<slug>`  
> **Editorial status:** `draft`  
> **Created:** `YYYY-MM-DD`  
> **Modified:** `YYYY-MM-DD`

## Scope Note

State the scoped comparison question for this concept crosswalk. Identify source ontologies included and important exclusions.

## Labels, Alternate Labels, and Source Terminology

| Role | Label or term | Source | Language | Notes |
|---|---|---|---|---|
| XwkOnt working label | `<label>` | XwkOnt | `en` | Required. |
| Source term | `<term>` | `<source>` | `en` | Repeat for each source term. |
| Alternate label | `<label>` | `<source or XwkOnt>` | `en` | Optional. |

## Source Definitions and Contextual Notes

Per `ADR-0010`, each row records a `Dimension`: `technical` (formal/engineering representation), `philosophical` (metaphysical/theoretical commitments), or `both`. Attempt at least one `philosophical` row per source where the source's own documentation discusses its theoretical grounding; leave absent or `unknown` rather than inferring one.

| Source | Term or identifier | Dimension | Claim type | Definition, quotation, or paraphrase | Reference | Locator | Notes |
|---|---|---|---|---|---|---|---|
| `<source>` | `<term/id>` | `technical/philosophical/both` | `direct quotation/paraphrase` | `<text>` | `xwkont:ref:<slug>` | `<section/page/IRI>` | `<context>` |

## Source Ontology Correspondences

| Correspondence ID | Source ontology | Source term | Source identifier or IRI | Source version | Reference | Inclusion rationale |
|---|---|---|---|---|---|---|
| `xwkont:correspondence:<slug>:001` | `<ontology>` | `<term>` | `<id/IRI/unknown>` | `<version/unknown>` | `xwkont:ref:<slug>` | `<why included>` |

## Semantic Comparison Notes

Per `ADR-0010`, each note also records a `Dimension`: `technical`, `philosophical`, or `both`.

| Note ID | Dimension | Claim type | Note | Supporting references | Confidence |
|---|---|---|---|---|---|
| `note-001` | `technical/philosophical/both` | `editorial observation/inference/paraphrase/direct quotation` | `<comparison note>` | `xwkont:ref:<slug>` | `high/medium/low/unknown` |

## Mapping Assertions or Candidate Relations

Per `ADR-0009`, each mapping records a `predicate_id` (SSSOM/SKOS predicate, or none for XwkOnt-only categories) and a `mapping_justification` (SEMAPV term, e.g. `semapv:ManualMappingCuration`) in addition to the free-text rationale.

| Mapping ID | Subject | Relation category | Object | `predicate_id` | `mapping_justification` | Status | Confidence | Rationale | Provenance |
|---|---|---|---|---|---|---|---|---|---|
| `xwkont:mapping:<slug>:001` | `<source term>` | `<category>` | `<source term>` | `<skos:exactMatch or none>` | `semapv:ManualMappingCuration` | `candidate/reviewed/rejected` | `high/medium/low/unknown` | `<why>` | `xwkont:ref:<slug>` |

## Uncertainty, Non-Equivalence, and Open Questions

| Item ID | Type | Description | Impact | Follow-up |
|---|---|---|---|---|
| `uncertainty-001` | `uncertainty/non-equivalence/incompatibility/open-question` | `<description>` | `<mapping or review impact>` | `<next action>` |

## Provenance and References

List repository-local reference identifiers used by this crosswalk. Every quotation, paraphrase, editorial observation, inference, and mapping assertion should point to a reference record.

- `xwkont:ref:<slug>` — `<short label>`

## Review History

| Review ID | Date | Outcome | Notes |
|---|---|---|---|
| `xwkont:review:<slug>:YYYY-MM-DD:01` | `YYYY-MM-DD` | `<outcome>` | `<notes>` |

## Future Work

- `<future work item>`
