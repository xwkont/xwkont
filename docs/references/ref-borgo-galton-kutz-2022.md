# Foundational Ontologies in Action

> **Local reference identifier:** `xwkont:ref:borgo-galton-kutz-2022`
> **Slug:** `borgo-galton-kutz-2022`
> **Editorial status:** `candidate`
> **Created:** `2026-07-01`
> **Modified:** `2026-07-02`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | Foundational ontologies in action | Editorial introducing a special issue systematically comparing seven foundational ontologies (BFO, DOLCE, GFO, GUM, TUpper, UFO, YAMATO) via common modeling cases. |
| Creator | Stefano Borgo, Antony Galton, Oliver Kutz | |
| Contributor | unknown | |
| Publisher | Applied Ontology, IOS Press | |
| Source type | article (special issue editorial) | |
| Version or edition | Applied Ontology 17(1), 2022, pp. 1-16 | |
| Identifier or URL | DOI: `10.3233/AO-220265` (<https://doi.org/10.3233/AO-220265>) | |
| Access date | 2026-07-01 | First surfaced in `docs/evaluations/prior-art-survey.md` (research conducted 2026-07-01 13:59 Z). |
| Snapshot / Stable identifier | DOI given above serves as the stable identifier; no separate archival snapshot needed per `ADR-0012`. | |
| Rights/license | unknown | Not verified in this pass. |

## Source Relation Notes

This is the editorial introducing an Applied Ontology special issue; the special issue's individual articles (not separately catalogued here) contain the detailed per-ontology case studies. Cite this reference for the editorial's own framing and cross-ontology observations (e.g., the color-modeling example); cite individual special-issue articles separately if a claim traces to one specifically.

## Rights and License Notes

Not verified in this pass. Treat as unknown rather than guessed.

## Citation and Locator Notes

Recommended citation: Borgo, S., Galton, A., & Kutz, O. (2022). Foundational ontologies in action. *Applied Ontology*, 17(1), 1-16. Cited in `docs/evaluations/prior-art-survey.md` and `docs/crosswalks/concepts/continuant-occurrent.md` as a secondary source comparing how BFO and DOLCE frame their top-level distinctions (BFO's realist framework grounded in scientific practice vs. DOLCE's cognitive/linguistic orientation).

### Full-text access attempt (2026-07-02)

Full text remains **not retrieved**, despite a deliberate attempt using the PDF-extraction technique in `docs/methodology/primary-source-verification.md`. This differs from that note's other cases: the blocker here is access, not parsing.

- DOI resolution (`https://doi.org/10.3233/AO-220265`) redirects to `journals.sagepub.com`, which returns HTTP 403.
- The publisher's own host (`content.iospress.com`, including the direct `openAccessPdf` download URL returned by the Semantic Scholar Graph API) is behind Cloudflare bot protection; both `curl` and WebFetch were blocked (403 / HTML challenge page, not a PDF).
- Unpaywall (`api.unpaywall.org`) reports `oa_status: green`, `is_oa: true`, with a repository copy at the Free University of Bozen-Bolzano's institutional repository (`bia.unibz.it`) — but that record itself only links back to the same paywalled `content.iospress.com` URL, not a separate deposited PDF.
- No self-archived copy was found on any author's page (A. Galton's Exeter page publications list ends at 2018; O. Kutz's Bolzano page publications list ends at 2019).
- Academia.edu and PhilPapers/PhilArchive list the paper but returned HTTP 403 to automated fetch.

**What was verified instead:** the paper's title, authors, and full abstract, via the Semantic Scholar Graph API (`api.semanticscholar.org/graph/v1/paper/DOI:10.3233/AO-220265`, fetched directly with `curl`, cross-checked against Unpaywall's independent record). The abstract confirms the special issue's motivation and scope (comparative modeling-case papers across foundational ontologies) but does not itself contain the BFO/DOLCE framing claim this reference is cited for — that claim traces to the editorial's body text, still unverified.

**Caution:** an earlier attempt during this same verification pass to fetch the Semantic Scholar API result via WebFetch (rather than `curl`) returned a plausible-looking but non-standard JSON payload (invented fields like `keyFindings`/`accessStatus` not part of the real API schema) — apparently a fabricated summary rather than the real response, produced when the underlying fetch was obstructed. Direct `curl` against the same endpoint returned the genuine schema. Treat WebFetch summaries of blocked/paywalled pages as unreliable; prefer a direct HTTP client for anything citation-critical.

**Status:** still `candidate`, not `reviewed` — full text access remains blocked in this environment. If institutional/library access becomes available outside this environment, re-attempt before citing further claims from this source.
