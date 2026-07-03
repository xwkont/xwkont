# Social Roles and their Descriptions (2004)

> **Local reference identifier:** `xwkont:ref:masolo-vieu-2004`
> **Slug:** `masolo-vieu-2004`
> **Editorial status:** `candidate`
> **Created:** `2026-07-01`
> **Modified:** `2026-07-01`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | Social Roles and their Descriptions | |
| Creator | Claudio Masolo, Laure Vieu, Emanuele Bottazzi, Carola Catenacci, Roberta Ferrario, Aldo Gangemi, Nicola Guarino | Confirmed via direct primary-source read (AAAI-hosted PDF), 2026-07-01. |
| Contributor | unknown | |
| Publisher | AAAI Press | |
| Source type | conference paper | Proceedings of the 9th International Conference on the Principles of Knowledge Representation and Reasoning (KR2004), pp. 267-277. |
| Version or edition | KR2004 | |
| Identifier or URL | <https://cdn.aaai.org/KR/2004/KR04-029.pdf> (mirrors also at `irit.fr` and `loa.istc.cnr.it`) | |
| Access date | 2026-07-01 | |
| Snapshot / Stable identifier | <http://web.archive.org/web/20260303055257/https://cdn.aaai.org/KR/2004/KR04-029.pdf> (2026-03-03) | Verified retrievable via the Internet Archive Wayback Machine at time of writing, per `ADR-0012`. |
| Rights/license | unknown | Not verified in this pass. |

## Source Relation Notes

This is the DOLCE-*driven* extension paper (not core DOLCE) that `docs/crosswalks/concepts/role.md` and `xwkont:ref:dolce-borgo-2022` both cite as the source of DOLCE's Role/Concept/classification apparatus. It builds on core DOLCE's `Non-Agentive Social Object` category (from `xwkont:ref:dolce-wonderweb-d18`) by introducing `Description`, `Concept`, `Role`, and the `classification` (`CF`) relation as a reified extension. `xwkont:ref:dolce-borgo-2022` reports this paper's axioms (A11-A15, D1-D3) accurately, as confirmed by comparing them directly against this paper's own numbering (A11-A15, D1-D3) in this pass.

## Rights and License Notes

Not verified in this pass. Treat as unknown rather than guessed.

## Citation and Locator Notes

Recommended citation: Masolo, C., Vieu, L., Bottazzi, E., Catenacci, C., Ferrario, R., Gangemi, A., & Guarino, N. (2004). Social Roles and their Descriptions. In *Proceedings of the 9th International Conference on the Principles of Knowledge Representation and Reasoning (KR2004)*, pp. 267-277. AAAI Press.

**Directly verified 2026-07-01** by fetching the AAAI-hosted PDF and extracting text manually (Python `zlib` stream decompression + PDF content-stream `Tj`/`TJ` operator parsing, since no PDF-text-extraction tool was available in this environment and WebFetch could not parse the compressed PDF streams directly — same technique used for the DOLCE 2022 and UFO 2021 papers elsewhere in this repository).

Key finding used in `docs/crosswalks/concepts/role.md`: this paper's apparatus for social roles (`Description`, `Concept`, `Role`, and the `classification` relation `CF(x, y, t)`) has **no term equivalent to UFO's `Relator`**. The paper's own literature review (section 2.1) surveys many role frameworks and never introduces a reified entity that mediates or is a truthmaker for a relationship between two specific bearers — the closest construct, `Description`, plays a different role: it is the "context" or "social convention" that *defines* a `Concept`/`Role` in general (via the `defined-by`/`DF` and `used-by`/`US` relations), not a particular instance-level mediator of a specific relationship the way a UFO `Relator` (e.g., a specific marriage) is. Roles here are unary predicates that classify entities (`CF`), not binary/relational reified particulars. This resolves `role.md`'s `uncertainty-003` as a confirmed negative finding, based on direct reading of this paper itself (not just `xwkont:ref:dolce-borgo-2022`'s report about it).
