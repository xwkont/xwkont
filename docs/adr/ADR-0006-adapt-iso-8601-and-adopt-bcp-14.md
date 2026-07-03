# ADR-0006: Adapt ISO 8601 Dates and Adopt BCP 14 Normative Language

- **Status:** Accepted
- **Date:** 2026-06-30

## Context

XwkOnt needs unambiguous dates for project records, access dates, and future metadata. It also needs precise requirement language in normative governance, architecture, policy, and specification documents.

Standards discovery identified ISO 8601 for date and time representation and RFC 2119 / RFC 8174 for normative keywords.

## Decision

XwkOnt SHALL adapt ISO 8601 through a constrained project profile:

1. Calendar dates SHALL use `YYYY-MM-DD`.
2. Date-times SHALL use UTC and end with `Z` when a time of day is required.
3. Reduced precision, intervals, durations, repeating intervals, seasons, and uncertain or approximate date extensions SHALL NOT be used unless a later ADR explicitly permits them for a defined use case.

XwkOnt SHALL adopt RFC 2119 and RFC 8174 BCP 14 normative language for documents that intentionally define requirements.

Normative documents using BCP 14 keywords SHALL include the RFC 8174 boilerplate or an equivalent project-approved statement that uppercase keywords have normative meaning.

## Scope

The ISO 8601 profile applies to project-controlled metadata, internal working records, access dates, and future machine-readable artifacts. It does not rewrite quotations or source-native date strings except where XwkOnt separately records normalized metadata.

The BCP 14 adoption applies to normative project documents. It does not require internal working records, explanatory reports, or roadmap notes to use normative keywords.

## Rationale

A narrow ISO 8601 profile provides interoperability and readability while avoiding ambiguity and unnecessary complexity. BCP 14 gives XwkOnt precise requirement language when requirements are intentional, while RFC 8174 prevents accidental lowercase or casual usage from becoming normative.

Both decisions reuse established standards and introduce only scoped project profiles needed for consistency.

## Consequences

### Positive

- Reduces date ambiguity across project metadata.
- Gives future specifications clear requirement semantics.
- Prevents accidental normative force in non-normative prose.

### Trade-offs

- Historical or source-specific dates may need separate raw and normalized forms.
- Contributors must avoid casual uppercase requirement keywords in non-normative documents.
- Documents using BCP 14 need explicit boilerplate.

## References

- ISO 8601-1:2019, *Date and time — Representations for information interchange — Part 1: Basic rules*.
- ISO 8601-2:2019, *Date and time — Representations for information interchange — Part 2: Extensions*.
- RFC 2119, *Key words for use in RFCs to Indicate Requirement Levels*.
- RFC 8174, *Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words*.
- `docs/evaluations/standards-survey-report.md`
- `docs/evaluations/standards-adoption-matrix.md`
