# DOLCE-Lite OWL Translation

> **Local reference identifier:** `xwkont:ref:dolce-lite-owl`
> **Slug:** `dolce-lite-owl`
> **Editorial status:** `candidate`
> **Created:** `2026-07-01`
> **Modified:** `2026-07-01`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | DOLCE-Lite (OWL translation of DOLCE) | An OWL ontology, not a paper — cited as a primary source document per `ADR-0012`'s provisions for non-paper artifacts, following the same pattern as `xwkont:ref:gangemi-dul` and `xwkont:ref:iao-owl`. |
| Creator | Aldo Gangemi (OWL engineering), per the ontology's own `rdfs:comment`: "The DOLCE and DnS ontologies. OWL engineering by Aldo Gangemi." | Formalizes the theory of `xwkont:ref:dolce-wonderweb-d18` (Masolo et al., 2003) in OWL. |
| Contributor | unknown | |
| Publisher | Laboratory for Applied Ontology (LOA-CNR) | Canonical namespace: `http://www.loa-cnr.it/ontologies/DOLCE-Lite.owl#`. |
| Source type | OWL ontology (machine-readable, not a paper) | |
| Version or edition | version 397 (per the file's own `owl:versionInfo`), fetched via a GitHub mirror (`iddi/sofia`) since the canonical `loa-cnr.it`/`loa.istc.cnr.it` host did not serve the raw file directly in this pass | The mirrored copy's content was spot-checked for internal consistency (well-formed OWL, matching class names/definitions expected from `xwkont:ref:dolce-wonderweb-d18`) but the canonical host was not independently cross-checked byte-for-byte in this pass. |
| Identifier or URL | Canonical: `http://www.loa-cnr.it/ontologies/DOLCE-Lite.owl`; fetched from: `https://raw.githubusercontent.com/iddi/sofia/master/eu.sofia.adk.common/ontologies/foundational/DOLCE-Lite.owl` | |
| Access date | 2026-07-01 | |
| Snapshot / Stable identifier | <http://web.archive.org/web/20260628155343/http://www.loa-cnr.it/ontologies/DOLCE-Lite.owl> (2026-06-28) | Verified retrievable via the Internet Archive Wayback Machine at time of writing, per `ADR-0012`. This snapshots the canonical `loa-cnr.it` URL, not the GitHub mirror actually fetched in this pass (see Citation and Locator Notes) — the two were not independently diffed. |
| Rights/license | unknown | Not verified in this pass. |

## Source Relation Notes

This is the base DOLCE module (endurant/perdurant/quality/physical-object/process/state/event/achievement/accomplishment/immediate-relation/mediated-relation, etc.) — it does **not** include the later Role/Concept/Description/Information-Object extensions, which live in DOLCE-driven literature (`xwkont:ref:masolo-vieu-2004`) or DUL (`xwkont:ref:gangemi-dul`) instead. Use this reference only for base-DOLCE terms already covered by `xwkont:ref:dolce-wonderweb-d18`; it supplies exact class IRIs where the 2003 technical report's own prose does not.

## Rights and License Notes

Not verified in this pass. Treat as unknown rather than guessed.

## Citation and Locator Notes

Recommended citation: DOLCE-Lite (OWL translation). Laboratory for Applied Ontology (LOA-CNR). `http://www.loa-cnr.it/ontologies/DOLCE-Lite.owl`.

**Directly verified 2026-07-01** by fetching the OWL/XML source (via a GitHub mirror, since the canonical host did not serve the raw file directly when fetched in this pass) and grepping for class IRIs already discussed in `xwkont:ref:dolce-wonderweb-d18`.

Key finding used across several crosswalks: confirmed the exact IRIs for `endurant`, `perdurant`, `quality`, `quale`, `physical-object`, `process`, `state`, `event`, `achievement`, `accomplishment`, `immediate-relation`, and `mediated-relation`, all under the `http://www.loa-cnr.it/ontologies/DOLCE-Lite.owl#` namespace — resolving several crosswalks' previously-`unknown` "Source identifier or IRI" fields in their Source Ontology Correspondences tables.

**Reused for `time.md` (2026-07-04):** the same fetched file also supplies `temporal-region` ("A region at which only temporal qualities can be directly located. It assumes a metrics for time.") and `time-interval` ("A temporal region, measured according to a calendar."), the latter `rdfs:subClassOf` the former. `temporal-region` is `rdfs:subClassOf` `region` and `owl:disjointWith` `physical-region` — DOLCE's temporal category is a quality-space/region, not an endurant or perdurant, structurally parallel to `physical-region`. No `time-instant`/`time-point` class was found in this module — DOLCE's temporal apparatus does not subdivide into instant/interval the way BFO's does. See `time.md`'s Source Definitions and correspondence row 002.
