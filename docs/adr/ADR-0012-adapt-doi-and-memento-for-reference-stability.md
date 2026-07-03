# ADR-0012: Adapt DOI and the Memento Protocol for Reference Stability

- **Status:** Accepted
- **Date:** 2026-07-01

## Context

`docs/references/TEMPLATE.md` (established by `ADR-0007`) records an `Access date` for web resources, and `docs/EDITORIAL_POLICY.md` requires Title/Publisher/URL/Accessed/Version/License for every external reference. This captures *when* a source was consulted, but not a guarantee that the cited content is still retrievable, or matches what was quoted, if the live URL later changes or disappears (a well-known problem generally called "link rot").

The first two concept crosswalks (`continuant-occurrent.md`, `object.md`) cite six reference records (`docs/references/ref-*.md`), several of which point at evolving web content (GitHub repositories, project websites, a personal academic page) with no fixed version, and none of which have a timestamped snapshot independent of the live URL.

## Decision

XwkOnt SHALL adapt two existing standards to close this gap, rather than inventing a bespoke archival mechanism:

1. **DOI (Digital Object Identifier, ISO 26324)** SHALL be used as the primary `Identifier or URL` value in a reference record whenever the cited work has one (formally published journal articles and conference papers). This refines, rather than replaces, the DCMI `identifier` field XwkOnt already adopted (`ADR-0003`) — DOIs are exactly what that field is for. A DOI resolves through `https://doi.org/<doi>` and is maintained by the publisher/CrossRef specifically to survive hosting changes.

2. **The Memento Protocol (RFC 7089)** SHALL be adapted, in practice, as: every reference record for web content without a DOI (project websites, GitHub repositories, technical reports without a DOI) SHALL include a timestamped archival snapshot URL (e.g., an Internet Archive Wayback Machine snapshot, which implements Memento) alongside the live URL, captured at or near the recorded access date. XwkOnt does NOT implement Memento's TimeGate/TimeMap content-negotiation infrastructure itself — that is an archive server's responsibility, not a citing project's. XwkOnt adapts only the underlying practice: cite a timestamped, independently retrievable snapshot, not only a live URL.

A new `Snapshot / Stable Identifier` field is added to `docs/references/TEMPLATE.md`'s Descriptive Metadata table, distinct from `Identifier or URL`.

## Scope

This ADR amends `docs/references/TEMPLATE.md`'s field list and `docs/EDITORIAL_POLICY.md`'s reference requirements. It does not change any other part of `ADR-0007`, `ADR-0009`, `ADR-0010`, or `ADR-0011`.

XwkOnt SHALL NOT fabricate a snapshot URL. If a snapshot could not be independently verified as actually existing and retrievable at the time a reference record was written, the `Snapshot / Stable Identifier` field SHALL record `unknown — not yet archived` rather than a guessed or unverified URL, consistent with the project's existing "do not guess" rule.

## Rationale

Both DOI and Memento/Wayback-Machine archival are established, widely used solutions to exactly this problem — DOI for formally published literature, web archiving for everything else. Adapting them satisfies "Reuse Before Introduce" directly: the alternative would be either ignoring the problem (current state) or inventing an XwkOnt-specific archival convention, which this ADR explicitly avoids.

## Consequences

### Positive

- Citations in concept crosswalks become verifiable independent of whether the original hosting URL still serves the same content.
- DOI usage costs nothing new to implement — it is a stricter, more correct use of a field XwkOnt already adopted.
- Snapshot archival is optional-but-required-when-no-DOI, keeping the rule simple: formally published work gets a DOI, everything else gets a timestamped snapshot.

### Trade-offs

- Not every source has a DOI (e.g., the DOLCE WonderWeb D18 technical report, ISO standard text, GitHub repository READMEs) — these require snapshot archival instead, which takes an extra verification step per reference.
- Creating a genuine, verifiable snapshot requires actually retrieving and confirming the archive exists; this cannot be done retroactively by assumption, and some existing reference records may need to carry `unknown — not yet archived` honestly until that verification happens.
- Existing reference records created before this ADR (`ref-bfo-2020.md`, `ref-dolce-wonderweb-d18.md`, `ref-ufo-2021.md`, `ref-sumo-niles-pease-2001.md`, `ref-borgo-galton-kutz-2022.md`, `ref-trojahn-2022.md`) need to be retrofitted.

## References

- ISO 26324 (DOI)
- Van de Sompel, H., et al. "Memento: Time Travel for the Web." RFC 7089 (IETF).
- `docs/adr/ADR-0003-adapt-iso-11179-and-adopt-dcmi-metadata.md` (DCMI `identifier` field)
- `docs/adr/ADR-0007-adopt-information-architecture-for-crosswalk-artifacts.md`
- `docs/crosswalks/concepts/continuant-occurrent.md`, `docs/crosswalks/concepts/object.md` (the citations motivating this ADR)
