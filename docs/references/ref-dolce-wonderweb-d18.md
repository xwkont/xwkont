# WonderWeb Deliverable D18: Ontology Library (final) — DOLCE

> **Local reference identifier:** `xwkont:ref:dolce-wonderweb-d18`
> **Slug:** `dolce-wonderweb-d18`
> **Editorial status:** `candidate`
> **Created:** `2026-07-01`
> **Modified:** `2026-07-01`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | WonderWeb Deliverable D18: Ontology Library (final) | Defines DOLCE (Descriptive Ontology for Linguistic and Cognitive Engineering). |
| Creator | Claudio Masolo, Stefano Borgo, Aldo Gangemi, Nicola Guarino, Alessandro Oltramari | |
| Contributor | unknown | |
| Publisher | WonderWeb: Ontology Infrastructure for the Semantic Web (IST Project 2001-33052) | EU-funded project deliverable. |
| Source type | technical report | |
| Version or edition | final, 2003 | |
| Identifier or URL | <https://www.loa.istc.cnr.it/old/Papers/D18.pdf> | No DOI; this is an EU project technical report, not a DOI-bearing publication. |
| Access date | 2026-07-01 | |
| Snapshot / Stable identifier | <http://web.archive.org/web/20260313084611/http://www.loa.istc.cnr.it/old/Papers/D18.pdf> (2026-03-13) | Verified retrievable via the Internet Archive Wayback Machine at time of writing, per `ADR-0012`. |
| Rights/license | unknown | Not verified in this pass. |

## Source Relation Notes

Related to WonderWeb Deliverable D17 (an earlier/companion deliverable on the WonderWeb library of foundational ontologies). Later DOLCE variants (DOLCE-Lite, DOLCE+DnS Ultralite, DOLCE in OWL) derive from this original specification; cite D18 for the original Endurant/Perdurant definitions and note explicitly if a claim instead comes from a later variant.

## Rights and License Notes

Not verified in this pass. Treat as unknown rather than guessed.

## Citation and Locator Notes

Recommended citation: Masolo, C., Borgo, S., Gangemi, A., Guarino, N., & Oltramari, A. (2003). *WonderWeb Deliverable D18: Ontology Library (final)*. Endurant/Perdurant definitions used in `docs/crosswalks/concepts/continuant-occurrent.md` are cited to this document's core theory of Endurants and Perdurants.

**Direct primary-source verification (2026-07-01):** the PDF was fetched directly and its text extracted manually — WebFetch could not parse the compressed PDF stream objects, and no PDF-text-extraction tool (`pdftotext`, `pdfplumber`, etc.) was otherwise available in this environment, so a custom Python extractor was used (`zlib` stream decompression + PDF `TJ`-array text-showing-operator parsing, with large negative kerning values treated as word-space markers). This confirmed exact quotations for Endurant/Perdurant ("Endurants are wholly present... at any time they are present. Perdurants... extend in time by accumulating different temporal parts...") and Physical Object ("endurants with unity... no common unity criterion, since different subtypes of objects may have different unity criteria"), and confirmed the Quale/quality-space distinction cites Gärdenfors (2000), *Conceptual Spaces: the Geometry of Thought*, and Goodman (1951), *The Structure of Appearance*, for trope theory — resolving an open uncertainty in `docs/crosswalks/concepts/quality.md`. Used in `continuant-occurrent.md`, `object.md`, and `quality.md`.

In a later pass (2026-07-01), the same extraction was used to check `docs/crosswalks/concepts/relation.md`'s `immediate-relation`/`mediated-relation` split, including the accompanying DOLCE-Lite+ KIF source embedded in the same PDF. Two findings: (1) D18's own text explicitly equates `immediate-relation` with "internal relation" ("Formal relations are called equivalently immediate relations, since they hold of their relata without mediating additional individuals... This notion also equivalent to that of internal relation"), confirming rather than merely suggesting the pairing with UFO's formal/internal-relation terminology; (2) `mediated-relation` is formalized as a pure logical-composition device (`MEDIATED-RELATION(a,b) ⟺ ∃c (IMMEDIATE-RELATION(a,c) ∧ IMMEDIATE-RELATION(c,b))`, documented as "a relation that composes other relations. For example, a participation relation composed with a representation relation") — it does not require or entail a reified, existentially-dependent mediating particular, unlike UFO's Relator-based material relation. This corrected `relation.md`'s earlier "plausibly analogous" framing of mediated-relation and UFO's material relation.

Reused again (2026-07-01) for `docs/crosswalks/concepts/continuant-occurrent.md`: confirmed the exact endurant/perdurant definitions ("Endurants are wholly present... Perdurants... extend in time by accumulating different temporal parts...") and, notably, found the primary source's own disclaimer behind that crosswalk's `note-002` characterization of DOLCE's "cognitive/linguistic orientation": "we must emphasise that this distinction is motivated by our cognitive bias, and we do not commit to the fact that both these kinds of entity really exist."

Reused again (2026-07-01) for `docs/crosswalks/concepts/process.md` and `docs/crosswalks/concepts/event.md`: confirmed DOLCE's Process/Achievement/Accomplishment definitions directly ("An occurrence-type is stative [or] eventive according to whether it holds of the mereological sum of two of its instances, i.e. if it is cumulative or not"; "eventive occurrences (events) are called achievements if they are atomic, otherwise they are accomplishments"). Also directly checked D18's own 90-item bibliography for a Vendler (1957) citation, motivated by both crosswalks' long-standing "plausible but unconfirmed" Vendler-parallel notes — **no such citation exists**. This resolves `process.md`'s `uncertainty-002` and `event.md`'s `uncertainty-003` as confirmed-absent findings rather than open questions.

Reused again (2026-07-01) for `docs/crosswalks/concepts/quality.md`, closing a gap the 2022-paper extraction hadn't (that pass verified the *Quale* definition via the 2022 restatement but left D18's own base Quality definition and Gärdenfors citation as an open item, `uncertainty-002`). Direct reading of D18 confirms the Quality/Quale definitions closely and, critically, the exact citation sentences: quality space is footnoted to Gärdenfors (2000), *Conceptual Spaces: the Geometry of Thought* (D18 reference [39]), and "this distinction between qualities and qualia" is footnoted to Goodman (1951), *The Structure of Appearance* (reference [40]), alongside Campbell (1990), *Abstract Particulars* (reference [9]), for trope theory generally. This upgrades that claim from an editorial paraphrase (via `xwkont:ref:borgo-galton-kutz-2022`) to a direct primary-source quotation.
