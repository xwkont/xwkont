# DOLCE: A Descriptive Ontology for Linguistic and Cognitive Engineering (2022)

> **Local reference identifier:** `xwkont:ref:dolce-borgo-2022`
> **Slug:** `dolce-borgo-2022`
> **Editorial status:** `candidate`
> **Created:** `2026-07-01`
> **Modified:** `2026-07-01`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | DOLCE: A Descriptive Ontology for Linguistic and Cognitive Engineering | Comprehensive modern restatement of DOLCE theory, "mainly based on the work of Masolo et al. (2003)" per the paper's own text, plus later refinements (roles, DOLCE-CORE). |
| Creator | Stefano Borgo, Roberta Ferrario, Aldo Gangemi, Nicola Guarino, Claudio Masolo, Daniele Porello, Emilio M. Sanfilippo, Laure Vieu | Confirmed via direct primary-source read (arXiv preprint), 2026-07-01. |
| Contributor | unknown | |
| Publisher | Applied Ontology, IOS Press | |
| Source type | journal article | |
| Version or edition | Applied Ontology, 2022 | |
| Identifier or URL | DOI: `10.3233/AO-210259` (<https://doi.org/10.3233/AO-210259>); arXiv preprint: <https://arxiv.org/abs/2308.01597> | |
| Access date | 2026-07-01 | |
| Snapshot / Stable identifier | DOI given above serves as the stable identifier; arXiv preprint additionally has its own permanent arXiv ID (2308.01597). | |
| Rights/license | unknown | Not verified in this pass. |

## Source Relation Notes

This paper is a later, more comprehensive companion to `xwkont:ref:dolce-wonderweb-d18` (Masolo et al., 2003) — it explicitly restates and extends the 2003 theory, incorporating later refinements: OntoClean-based role treatment (Borgo et al., 2010; Masolo et al., 2004, both external to core DOLCE — see Citation and Locator Notes), and the 2009 DOLCE-CORE relabeling of `endurant`/`perdurant` to `object`/`event`. Cite this paper (not the 2003 D18) for any claim about DOLCE's *current* comprehensive theory, including explicit statements about what DOLCE does and does not formalize.

## Rights and License Notes

Not verified in this pass. Treat as unknown rather than guessed.

## Citation and Locator Notes

Recommended citation: Borgo, S., Ferrario, R., Gangemi, A., Guarino, N., Masolo, C., Porello, D., Sanfilippo, E.M., & Vieu, L. (2022). DOLCE: A Descriptive Ontology for Linguistic and Cognitive Engineering. *Applied Ontology*, IOS Press.

**Directly verified 2026-07-01** by fetching the arXiv preprint PDF (`arxiv.org/pdf/2308.01597`) and extracting text manually (Python `zlib` stream decompression + `TJ`-array parsing, since no PDF-text-extraction tool was available in this environment and the WebFetch tool could not parse the compressed PDF streams directly).

Key findings used across crosswalks:
- **"DOLCE does not formalize functions and roles"** — a direct quotation confirming that DOLCE's Role treatment (as cited in `docs/crosswalks/concepts/role.md`) comes from DOLCE-*driven* approaches (Borgo et al., 2010; Masolo et al., 2004), not core DOLCE itself.
- Roles in those DOLCE-driven approaches are "concepts that are anti-rigid and founded" — confirms `role.md`'s OntoClean-based characterization, but the source is external extension literature, not core DOLCE.
- DOLCE-CORE (2009, Borgo & Masolo) relabeled `endurant`/`perdurant` to `object`/`event`, distinguished by whether they have space or time as their main dimension — relevant context for `continuant-occurrent.md`.
- `Quale` confirmed: "the position occupied by an individual quality within a quality space" (e.g., two qualities of the same color shade occupy the same position/quale within the color space, while remaining numerically distinct qualities) — confirms `quality.md`'s Quale definition closely.
- `InformationObject` appears as part of DUL (DOLCE Ultra Lite), an OWL-oriented extension pattern — not confirmed as the same thing as "DOLCE Lite Plus" cited in `docs/crosswalks/concepts/information-artifact.md`; the exact relationship between DUL and DOLCE Lite Plus was not confirmed in this pass and needs further checking.
