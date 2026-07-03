# ADR-0016: License-Gated Reference Archive as a Pointer Registry

- **Status:** Accepted
- **Date:** 2026-07-03

## Context

`TODO.md`'s "Future Infrastructure" section proposed building "XwkOnt's own reference archive" once the public repository and `ontology-core-v0.1.0` were live (both true as of 2026-07-03). As originally worded, the item described an XwkOnt-controlled mirror/snapshot of each cited source's *content*, addressable via a newly minted, XwkOnt-issued GUID per reference record, in addition to the DOI/Wayback Machine citation `ADR-0012` already requires.

Reviewing that proposal surfaced a problem `ADR-0012` did not have to face: `ADR-0012`'s Memento/Wayback adaptation relies on the Internet Archive's own library/archival legal basis for hosting third-party copyrighted content. An XwkOnt-controlled mirror has no equivalent basis. Most of `docs/references/ref-*.md`'s existing records carry `unknown` or unverified `Rights/license` values (journal articles, technical reports, project web pages); mirroring their full content on an XwkOnt-controlled host without a confirmed redistribution right would create real copyright exposure that DOI resolvers and the Internet Archive do not carry in the same way. Two records already have a verified, explicitly permissive license: `ref-gfo.md` (CC-BY-4.0) and `ref-tupper-colore.md` (CC-BY-SA-4.0).

Separately, `docs/INFORMATION_ARCHITECTURE.md` already defines a local identifier convention for reference records, `xwkont:ref:<slug>` (e.g. `xwkont:ref:bfo-2020`). The original TODO wording's "XwkOnt-issued GUID" would duplicate this without a stated reason.

## Decision

XwkOnt adopts a narrower scope than the original TODO item:

1. **No general content-mirroring archive is built now.** Full-content mirroring of a cited source requires that source's `Rights/license` field to be a verified, explicit license that permits redistribution (e.g. CC-BY, CC-BY-SA, or equivalent) before any local copy is made. `unknown`, unverified, or restrictive licenses are not mirrored, regardless of hosting readiness.
2. **No new identifier scheme is introduced.** The existing `xwkont:ref:<slug>` local identifier (`docs/INFORMATION_ARCHITECTURE.md`) is reused as the pointer-registry key. A separate XwkOnt-issued GUID is not needed and is not created.
3. **`docs/references/TEMPLATE.md` gains one new Descriptive Metadata field, `Archive mirror status`,** distinct from `ADR-0012`'s `Snapshot / Stable Identifier` field:
   - `not applicable — license unknown or unverified` (default; matches `ADR-0012`'s existing "do not guess" posture),
   - `not applicable — license does not permit redistribution`,
   - `eligible — license permits redistribution, not yet mirrored`,
   - `mirrored — <path or URL>` once an XwkOnt-controlled copy actually exists.
4. **Hosting location and domain remain deferred**, exactly as the original TODO item already flagged (`archive.xwkont` vs. a `w3id.org/xwkont/archive/` path is not decided by this ADR).
5. This ADR does not itself mirror any content. It only defines the license gate and the record-level field. Marking `ref-gfo.md` and `ref-tupper-colore.md` `eligible` (their licenses are already verified permissive) and any actual mirroring remain future work.

## Scope

This ADR amends `docs/references/TEMPLATE.md`'s Descriptive Metadata table, adding one field. It does not change `ADR-0012`'s DOI/Memento requirements, `docs/INFORMATION_ARCHITECTURE.md`'s `xwkont:ref:<slug>` identifier convention, or any existing reference record's `Snapshot / Stable Identifier` value. Existing reference records are not required to be retrofitted with the new field immediately; `unknown`/default values are acceptable until a record is next touched, consistent with how `ADR-0012`'s own retrofit list was handled.

## Rationale

"Reuse Before Introduce" applies twice here: reusing `xwkont:ref:<slug>` instead of minting a new GUID scheme, and reusing each reference record's already-required `Rights/license` field as the gating signal instead of building a separate licensing-review workflow. Gating on verified license status, rather than building the archive first and sorting out rights later, avoids taking on copyright exposure the Internet Archive's Memento-based approach (`ADR-0012`) does not have to carry for the same content.

## Consequences

### Positive

- No copyright risk is introduced: nothing is mirrored without a verified, explicit redistribution-permitting license.
- No duplicate identifier scheme: `xwkont:ref:<slug>` already uniquely keys every reference record.
- The two already-open-licensed sources (GFO, TUpper) give a concrete, low-risk starting point for eventual mirroring, once someone does the work.
- Keeps the field addition small and reversible; does not commit to a hosting decision prematurely.

### Trade-offs

- This is a materially smaller deliverable than the original TODO item's "reference archive" — most current reference records (all but two) will show `not applicable` indefinitely unless their license is separately verified.
- Citation permanence for `unknown`-license sources still depends entirely on DOI resolvers and Wayback snapshots (`ADR-0012`), not on any XwkOnt-controlled fallback. This ADR does not close that gap; it declines to close it via unauthorized mirroring.
- A future maintainer wanting the originally envisioned full-content archive would need a separate licensing-review pass per source (contacting rights holders, or restricting scope to only permissively-licensed sources) — not something this ADR performs.

## References

- `TODO.md` ("Future Infrastructure" — reference archive item, original wording)
- `docs/adr/ADR-0012-adapt-doi-and-memento-for-reference-stability.md`
- `docs/INFORMATION_ARCHITECTURE.md` (`xwkont:ref:<slug>` identifier convention)
- `docs/references/ref-gfo.md`, `docs/references/ref-tupper-colore.md` (currently the only verified-permissive-license reference records)
