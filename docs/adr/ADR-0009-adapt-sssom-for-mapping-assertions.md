# ADR-0009: Adapt SSSOM Predicate and Justification Vocabulary for Mapping Assertions

- **Status:** Accepted; point 3 (confidence vocabulary) amended by `ADR-0013`, and given a fixed numeric export projection by `ADR-0014`, both on 2026-07-01
- **Date:** 2026-07-01

## Context

`ADR-0007` adopted `docs/INFORMATION_ARCHITECTURE.md` as the information architecture for concept crosswalk artifacts, including a mapping-assertion record (§6: local mapping identifier, subject source term, object source term, relation category, status, confidence, rationale, provenance, reviewer notes) and a bespoke relation-category vocabulary in `docs/methodology/crosswalk-methodology.md` (`exact-equivalence-candidate`, `close-match`, `broader-than`, `narrower-than`, `related`, `overlap`, `incompatible`, `unknown`, `explicit-non-equivalence`), each with a loosely noted SKOS correspondence.

`docs/evaluations/prior-art-survey.md` and `docs/evaluations/meta-ontology-standards-evaluation.md` identified **SSSOM** (Simple Standard for Sharing Ontological Mappings, `mapping-commons/sssom`) as a mature, actively maintained standard purpose-built for exactly this problem: a `subject_id`/`predicate_id`/`object_id` mapping record with a `mapping_justification` field drawn from the **SEMAPV** (Semantic Mapping Vocabulary) enumeration (e.g., `semapv:ManualMappingCuration`, `semapv:LexicalMatching`, `semapv:LogicalReasoning`, `semapv:MappingReview`), plus a confidence field and provenance metadata. XwkOnt's category vocabulary was designed without checking SSSOM, which is a "Reuse Before Introduce" gap the evaluation flagged as needing an ADR before implementation.

## Decision

XwkOnt SHALL **adapt** (not fully adopt) SSSOM for mapping assertions, amending `docs/INFORMATION_ARCHITECTURE.md` §6 and `docs/methodology/crosswalk-methodology.md`:

1. Each mapping assertion SHALL record an explicit `predicate_id` alongside its existing XwkOnt relation category, using the SSSOM/SKOS predicate where one exists:

   | XwkOnt category | `predicate_id` |
   |---|---|
   | `exact-equivalence-candidate` | `skos:exactMatch` |
   | `close-match` | `skos:closeMatch` |
   | `broader-than` | `skos:broadMatch` (direction noted explicitly) |
   | `narrower-than` | `skos:narrowMatch` (direction noted explicitly) |
   | `related` | `skos:relatedMatch` |
   | `overlap`, `incompatible`, `unknown`, `explicit-non-equivalence` | none — remain explicit XwkOnt extensions; SSSOM itself permits mappings with no formal predicate for exactly this kind of case |

2. Each mapping assertion SHALL record a `mapping_justification` value from the SEMAPV vocabulary (e.g., `semapv:ManualMappingCuration` for the manually reviewed, citation-based mappings XwkOnt currently produces), in addition to the existing free-text `rationale` field. `mapping_justification` records *how* the mapping was derived (a controlled vocabulary term); `rationale` continues to record *why*, in prose, as XwkOnt's evidence-linked review already requires.

3. XwkOnt's existing categorical confidence values (`high`/`medium`/`low`/`unknown`) are **retained as-is**. SSSOM's numeric `0.0`-`1.0` confidence scale is designed for automated/semi-automated matching pipelines; it implies a precision XwkOnt's manually curated, citation-based evidence model does not have. This is the one part of SSSOM this ADR deliberately does not adopt.

4. XwkOnt SHALL NOT adopt SSSOM's TSV/machine-readable mapping-set serialization at this time. Human-readable Markdown mapping assertions remain canonical per `ADR-0007`. If a machine-readable mapping export is implemented in the future, it SHOULD target SSSOM/TSV as the export format rather than a bespoke serialization, since the record now carries `predicate_id` and `mapping_justification` fields that map directly onto it.

## Scope

This ADR amends the mapping-assertion portion of `ADR-0007` and its dependent specifications (`docs/INFORMATION_ARCHITECTURE.md` §6, `docs/methodology/crosswalk-methodology.md`). It does not change `ADR-0007`'s repository layout, identifier scheme, reference-record model, or artifact-status vocabulary, which remain in effect unchanged.

## Rationale

SSSOM is a widely used, actively maintained, purpose-built standard for ontology mapping metadata (Mapping Commons / OBO community, FAIR-mappings goal). Adapting its predicate and justification vocabulary is a direct application of XwkOnt's own "Reuse Before Introduce" principle, and closes the specific gap `docs/evaluations/meta-ontology-standards-evaluation.md` identified. A partial adaptation — rather than full adoption of SSSOM's numeric confidence and TSV serialization — is justified because those parts assume an automated-matching workflow XwkOnt does not have; forcing them now would imply false precision or premature tooling commitments.

## Consequences

### Positive

- Mapping assertions gain an explicit, externally checkable `predicate_id` instead of only a loosely noted SKOS correspondence.
- `mapping_justification` cleanly separates *how* a mapping was derived from *why* it's believed correct, improving review quality without new prose conventions.
- A future machine-readable mapping export has a clear, standard target (SSSOM/TSV) instead of requiring a bespoke format decision later.

### Trade-offs

- Contributors recording a mapping assertion now need one more required field (`mapping_justification`) and must learn the small SEMAPV vocabulary in addition to XwkOnt's existing categories.
- Full SSSOM interoperability (tooling, TSV export, OxO2-style browsing) remains future work; this ADR only changes the human-readable record schema.
- `docs/methodology/crosswalk-methodology.md`'s category table needs a new column and must be kept in sync with this ADR if SSSOM's predicate vocabulary changes upstream.

## References

- `docs/evaluations/prior-art-survey.md`
- `docs/evaluations/meta-ontology-standards-evaluation.md`
- `docs/adr/ADR-0007-adopt-information-architecture-for-crosswalk-artifacts.md`
- SSSOM specification: <https://mapping-commons.github.io/sssom/>, <https://github.com/mapping-commons/sssom/>
- SEMAPV (Semantic Mapping Vocabulary): <https://github.com/mapping-commons/semantic-mapping-vocabulary>
