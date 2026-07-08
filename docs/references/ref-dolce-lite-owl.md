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

**Reused for `list-sequence.md` (2026-07-07):** the same `DOLCE-Lite.owl` was re-fetched and directly grepped for "list," "sequence," "tuple," and "ordered." Found only the informal verb "sequenced," used in prose about events/situations lacking a unifying description ("they can be sequenced by some course, but they do not require a description as a unifying criterion"), not a dedicated ordered-collection class. Recorded as a scoped absence. See `list-sequence.md`'s Source Definitions.

**Reused for `continuous-discrete.md` (2026-07-07):** the same `DOLCE-Lite.owl` was re-fetched and grepped for "continuous," "discrete," "atomic," and "granular." Found only local adjective/property usage: `atomic-part-of`/`atomic-part` (object properties), `"An atomic region."` (a comment on a quality-region class), `"A quality having a q-location at an atomic region"`, and the `constituent` comment's mention of "scientific granularities or ontological 'strata'." No dedicated continuous/discrete class or axis exists in this file. Confirms the crosswalk's draft finding exactly. See `continuous-discrete.md`'s Source Definitions.

**Reused for `modality.md` (2026-07-07):** the same `DOLCE-Lite.owl` was re-fetched and grepped directly for "modal," "modality," "necessity," "possibility," "necessary," "possible," "deontic," and "alethic." Found only ordinary-language wording: "possibilia," "as large as possible," and one unrelated comment's "necessary axiom of compresence." No dedicated modal class or operator exists in this file. See `modality.md`'s Source Definitions.

**Reused for `non-physical-social-object.md` (2026-07-07, session-048), this crosswalk's primary source:** the same `DOLCE-Lite.owl` was re-fetched and its `non-physical-endurant`/`non-physical-object` class blocks read directly. This corrected a citation-fidelity defect in the Codex draft: the draft's `non-physical-endurant` quotation was truncated to "An endurant with no mass," dropping the actual full `rdfs:comment` — "An endurant with no mass, generically constantly depending on some agent. Non-physical endurants can have physical constituents (e.g. in the case of members of a collection)." Confirmed `non-physical-object`'s comment exactly as drafted ("Formerly known as description..."), and confirmed no further subclasses exist beneath `non-physical-object` in this base module — the classic DOLCE-family `Mental-Object`/`Social-Object`/`Agentive-Social-Object`/`Non-Agentive-Social-Object` leaf split is not present here, consistent with the draft's claim. See `non-physical-social-object.md`'s Source Definitions and correspondence row 001.

**Reused for `symbol-sign-representation.md` (2026-07-07, session-049):** the same `DOLCE-Lite.owl` was re-fetched and grepped directly for "symbol," "sign," "signifier," "representation," "name," and "word." The only hits were incidental uses inside relation-composition comments (e.g. "a participation relation composed with a representation relation"), not a dedicated sign/symbol/representation class. Confirms the crosswalk's draft finding of a clean absence exactly. See `symbol-sign-representation.md`'s Source Definitions.
