# ADR-0013: Extend the Confidence Vocabulary with Intermediate Values

- **Status:** Accepted; numeric export projection for this vocabulary defined by `ADR-0014` on 2026-07-01
- **Date:** 2026-07-01

## Context

`ADR-0009` retained a categorical confidence vocabulary of exactly `high`/`medium`/`low`/`unknown` for mapping assertions, explicitly declining SSSOM's numeric `0.0`-`1.0` scale because it "implies a precision XwkOnt's manually curated, citation-based evidence model does not have."

A 2026-07-01 review pass across all 8 concept crosswalks — performed against `docs/governance/contributing.md`'s Review Checklist as part of moving the crosswalks toward `candidate`/`reviewed` editorial status — found that practice had already drifted from this: 5 mapping-assertion rows, across `process.md`, `role.md`, `relation.md`, and `information-artifact.md`, use `medium-high` or `low-medium` instead of one of the four approved values. One instance (`process.md` mapping-001) predates this review pass; the rest were added during this review pass, following that existing (non-compliant) pattern without checking it against `docs/methodology/crosswalk-methodology.md`'s stated vocabulary.

In each case, the compound value was recording a specific, recurring situation: a mapping's confidence was raised or lowered by a *sourcing* change (e.g., a claim moving from secondary-sourced to directly primary-source-verified) without the underlying *metaphysical* judgment moving a full category. Forcing these into `medium` or `high` loses that distinction; forcing them all one direction or the other is an arbitrary rounding decision with no principled rule to apply consistently.

## Decision

XwkOnt SHALL extend the confidence vocabulary to six categorical values: `high`, `medium-high`, `medium`, `low-medium`, `low`, `unknown`. This amends `ADR-0009`'s point 3 and `docs/methodology/crosswalk-methodology.md`'s "Confidence values are..." statement.

`medium-high` and `low-medium` SHALL be used only to record that a confidence shift occurred for a *sourcing* reason (e.g., a claim was independently verified against a primary source it previously lacked, or two frameworks were confirmed to differ in formal apparatus despite matching informally) without a full-category change in the underlying *substantive* judgment. They are not a general-purpose way to hedge between two values without a stated reason — every use of an intermediate value SHALL include, in the mapping's `rationale` prose, why the full adjacent category was not reached.

The numeric-scale rejection in `ADR-0009` point 3 is otherwise unchanged: this remains a small, fixed, categorical extension (six values, not a continuum), not an adoption of SSSOM's `0.0`-`1.0` scale or any other numeric precision.

## Scope

This ADR amends `ADR-0009`'s point 3 only. It does not change `ADR-0009`'s `predicate_id`/`mapping_justification` provisions, `docs/INFORMATION_ARCHITECTURE.md`'s mapping-record schema, or any relation-category vocabulary.

## Rationale

The alternative to formalizing this was either (a) retrofitting 5 rows to a coarser 4-value scale, discarding information the review process had already produced and taking a step backward in the crosswalks' evidentiary precision, or (b) leaving the drift unaddressed, so the methodology document and actual practice continue to silently disagree. Given the drift had already occurred independently in two separate places (once before this review pass, four times during it) for the same underlying reason, formalizing it is more honest than either retrofitting away real distinctions or ignoring an already-established practice.

## Consequences

### Positive

- The confidence vocabulary now matches actual crosswalk practice; no crosswalk needs its confidence values rounded away from what the evidence actually supports.
- The rule restricting intermediate values to sourcing-driven shifts (not general hedging) keeps the vocabulary from creeping further toward a false-precision numeric scale, preserving `ADR-0009`'s original concern.

### Trade-offs

- Six categorical values are marginally more to learn than four, though the two new values are self-explanatory extensions of the existing ones.
- Future review passes must check that `medium-high`/`low-medium` usage still cites a sourcing-driven reason in `rationale`, not just a vague "somewhere between" hedge — this ADR's restriction is a norm to enforce in review, not something the file format alone guarantees.

## References

- `docs/adr/ADR-0009-adapt-sssom-for-mapping-assertions.md`
- `docs/methodology/crosswalk-methodology.md`
- `docs/governance/contributing.md` (Review Checklist)
- Affected crosswalks: `docs/crosswalks/concepts/process.md`, `docs/crosswalks/concepts/role.md`, `docs/crosswalks/concepts/relation.md`, `docs/crosswalks/concepts/information-artifact.md`
