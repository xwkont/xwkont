# ADR-0014: Define a Fixed Numeric Projection of Confidence for Tooling Export

- **Status:** Accepted
- **Date:** 2026-07-01

## Context

`ADR-0009` retained a categorical confidence vocabulary and explicitly declined SSSOM's numeric `0.0`-`1.0` confidence scale, reasoning that XwkOnt's manually curated, citation-based evidence model does not support the precision a hand-picked decimal implies. `ADR-0013` extended that vocabulary to six values (`high`/`medium-high`/`medium`/`low-medium`/`low`/`unknown`) rather than adopting numbers.

The maintainer now expects tooling — very likely a machine-readable mapping export (SSSOM/TSV, per `ADR-0009`'s stated future-export target) — soon after publication, likely before a further ADR cycle would naturally revisit confidence representation. SSSOM's `confidence` column is numeric by convention, and downstream tooling (filtering, sorting, aggregate reporting across mapping sets) is easier to build against a numeric field than a bespoke six-value enum.

Two options were considered: (1) start recording a numeric confidence per mapping assertion directly, alongside or instead of the category, or (2) keep the category as the sole authoritative, human-curated judgment, and define a fixed, static lookup table that projects each category to a number only at export time.

## Decision

XwkOnt SHALL adopt option 2. The categorical value remains the only field a contributor or reviewer sets by hand; it is what appears in every crosswalk's Mapping Assertions table and is what `ADR-0009`'s Review Checklist evaluates. A **fixed, static** category-to-number table, defined here, is used only when producing a numeric SSSOM-compatible export:

| Category | Numeric projection |
|---|---|
| `high` | `1.0` |
| `medium-high` | `0.8` |
| `medium` | `0.6` |
| `low-medium` | `0.4` |
| `low` | `0.2` |
| `unknown` | *(omitted from numeric export — see Rationale)* |

This table is a **fixed constant**, not a per-mapping judgment call. No contributor picks a number directly; no crosswalk file needs to record one. If this table's values are ever revised, that revision applies uniformly to every mapping assertion's export via the lookup, not by re-editing any of the 8 crosswalks' Markdown content.

`unknown` SHALL NOT be projected to `0.0` or any other number. `unknown` means "insufficient evidence to assign a confidence," not "confidently very low" — collapsing it to `0.0` would misrepresent an absence of judgment as a strong negative judgment. A numeric export SHOULD omit the `confidence` field entirely for `unknown`-confidence mappings (SSSOM's confidence column is optional) rather than emit a fabricated number.

## Scope

This ADR does not reopen `ADR-0009`'s or `ADR-0013`'s categorical vocabulary, and does not require any change to existing crosswalk content — the numeric table applies only at export time, to tooling not yet built. It should be read together with `ADR-0009`'s existing statement that a future machine-readable export should target SSSOM/TSV.

## Prior Art Considered

Per XwkOnt's "Reuse Before Introduce" principle, this decision was checked against how comparable systems actually handle confidence, not decided from first principles alone:

- **SSSOM** defines `confidence` as numeric but optional. In practice, numeric confidence tracks with `mapping_tool`/automated-matcher provenance; manually curated mappings are instead tracked via the categorical `mapping_justification` field (e.g., `semapv:ManualMappingCuration`), frequently *without* a numeric confidence recorded at all.
- **OAEI** (Ontology Alignment Evaluation Initiative), the standard ontology-matching benchmark, nominally uses continuous `0.0`-`1.0` confidence in its Alignment API format — but its own reference-alignment evaluation collapses this to a binary threshold in practice: a correspondence with confidence `>= 0.5` is treated as "fully correct," below `0.5` as "fully incorrect." Even where the stated convention is numeric, real usage is effectively categorical.
- **LLM- and embedding-based ontology matchers** (e.g., BERTMap, GenOM, Agent-OM) produce genuinely native numeric confidence, because it is a computed cosine-similarity or model score, not a human judgment expressed as a number.

The pattern across all three: numeric confidence is meaningful precisely when a machine computed it, and human-curated mapping efforts either avoid a numeric confidence or use it in a way that collapses back to a small number of effective buckets. This is independent confirmation, not just consistency by construction, that XwkOnt's approach — categorical as the sole human-authored judgment, numeric only as a fixed, mechanically-derived export projection — matches how this problem is handled elsewhere, rather than being an idiosyncratic XwkOnt invention.

## Rationale

This preserves `ADR-0009`'s original concern (no hand-picked false precision) while unblocking near-term tooling: the number is derived, not authored, so it carries exactly as much precision as the category it comes from — no more. Spacing the five non-`unknown` values evenly (0.2 increments) avoids implying any category is closer to its neighbor than the others; nothing about XwkOnt's evidence model justifies uneven spacing (e.g., "medium-high" being closer to "high" than to "medium").

The alternative — recording a numeric value per mapping by hand — was rejected because it reintroduces exactly the problem `ADR-0009` identified: a reviewer choosing `0.73` implies a level of reproducible precision that a manually curated, citation-based judgment does not have. A fixed lookup table sidesteps this entirely, since the number is mechanically derived from a category a human already chose for other (documented, checkable) reasons.

## Consequences

### Positive

- Tooling built soon after publication can consume a numeric SSSOM-compatible confidence field immediately, without waiting for a further ADR cycle or a re-edit of existing crosswalks.
- No existing crosswalk content changes; the categorical value remains authoritative and human-facing.
- The fixed table can be revised later (e.g., non-uniform spacing, if evidence emerges that it should not be uniform) without touching any of the 8 crosswalks, since the projection is applied only at export time.

### Trade-offs

- Any export tool implementing this projection needs to implement the `unknown`-omission rule correctly, or risk silently exporting a fabricated `0.0` — this should be called out in that tool's own documentation or tests when it is built.
- A fixed, evenly-spaced numeric table is itself a modeling choice (why 0.2 increments, why these five points) that a future maintainer might want to revisit once real tooling and real users exist; this ADR does not claim the spacing is empirically justified, only that it is a reasonable, non-arbitrary default given no better evidence exists yet.

## References

- `docs/adr/ADR-0009-adapt-sssom-for-mapping-assertions.md`
- `docs/adr/ADR-0013-extend-confidence-vocabulary-with-intermediate-values.md`
- `docs/methodology/crosswalk-methodology.md`
- SSSOM specification: <https://mapping-commons.github.io/sssom/>
- Ontology Alignment Evaluation Initiative (OAEI), reference-alignment confidence-threshold convention: <http://oaei.ontologymatching.org/>
- BERTMap (Jiaoyan Chen et al.), an embedding-based ontology alignment system with native numeric confidence: <https://arxiv.org/abs/2112.02682>
