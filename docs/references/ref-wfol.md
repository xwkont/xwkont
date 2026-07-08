# WonderWeb Foundational Ontologies Library (WFOL)

> **Local reference identifier:** `xwkont:ref:wfol`
> **Slug:** `wfol`
> **Editorial status:** `candidate`
> **Created:** `2026-07-08`
> **Modified:** `2026-07-08`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | WonderWeb Foundational Ontologies Library (WFOL) | Covers the library as a whole (its three-module structure and stated purpose), distinct from `xwkont:ref:dolce-wonderweb-d18`, which covers Deliverable D18's DOLCE-specific ontology-definition content. |
| Creator | unknown (WonderWeb project consortium) | The library's three modules have separate authorship: DOLCE by Masolo, Borgo, Gangemi, Guarino & Oltramari (per `xwkont:ref:dolce-wonderweb-d18`); OCHRE by Luc Schneider (University of Geneva); BFO adopted by the IFOMIS research lab (University of Leipzig) — per the primary source cited below. No single named author for the library structure itself. |
| Contributor | Ian Horrocks | WonderWeb project coordinator, per CORDIS (the EU's own project database), already recorded in `docs/evaluations/comparable-projects-survey.md`. |
| Publisher | WonderWeb: Ontology Infrastructure for the Semantic Web (EU Framework Programme 5, IST Project 2001-33052); pages hosted by the Laboratory for Applied Ontology (LOA), ISTC-CNR | Project ran 2002-01-01 to 2004-06-30 per CORDIS, already independently confirmed in the prior survey. |
| Source type | web page | LOA's own DOLCE.html description page, distinct from the D18 PDF deliverable already covered by `xwkont:ref:dolce-wonderweb-d18`. |
| Version or edition | unknown | No version metadata on the page. |
| Identifier or URL | <http://www.loa.istc.cnr.it/old/Papers/DOLCE.html> | No DOI. |
| Access date | 2026-07-08 | |
| Snapshot / Stable identifier | <https://web.archive.org/web/20260708103006/https://www.loa.istc.cnr.it/old/Papers/DOLCE.html> (2026-07-08) | No pre-existing Wayback snapshot was found for this exact page (checked via the Wayback availability API and CDX search, both empty); a fresh snapshot was captured this session via Wayback's Save Page Now and independently verified retrievable (HTTP 200), per `ADR-0012`. |
| Rights/license | unknown | No license statement found on the page. |
| Archive mirror status | not applicable — license unknown or unverified | Per `ADR-0016`. |

## Source Relation Notes

Related to `xwkont:ref:dolce-wonderweb-d18` (WonderWeb Deliverable D18, the DOLCE-specific final ontology specification) and the untraced WonderWeb Deliverable D17 ("The WonderWeb Library of Foundational Ontologies and the DOLCE ontology") — D17 is the library-level deliverable one would expect to cite for WFOL's own structure and purpose, but it is **not reachable**: absent from the LOA's own `/old/Papers/` directory listing (only `D18.pdf` is present), 404s at the same path pattern as D18, and has no Wayback Machine snapshot under any URL checked. This record cites the LOA's own DOLCE.html page instead, which independently confirms the same library-structure claims in the LOA's own words. D17 is known only via secondary citations (ResearchGate abstract page, `docs/evaluations/comparable-projects-survey.md`'s external-tool-sourced report) not independently fetched in this pass.

Not a source XwkOnt crosswalks against — WFOL is cited only as comparable prior art (`README.md`'s "Related Prior Art" section), not as an ontology-definition source for any `docs/crosswalks/concepts/*.md` correspondence row (DOLCE's own definitions are cited via `xwkont:ref:dolce-wonderweb-d18` and other DOLCE-specific reference records instead).

## Rights and License Notes

No explicit license statement found on the cited page. Not verified against any separate WonderWeb project-level licensing terms.

## Citation and Locator Notes

Recommended citation: Laboratory for Applied Ontology (LOA), ISTC-CNR. *DOLCE and the WonderWeb Foundational Ontologies Library*. `http://www.loa.istc.cnr.it/old/Papers/DOLCE.html`.

**Direct primary-source verification (2026-07-08):** the page was fetched directly and confirms, in the LOA's own words: DOLCE is "the first module of the WonderWeb Foundational Ontologies Library (WFOL)"; the library's Library of Foundational Ontologies contains "three reference modules (DOLCE, OCHRE, BFO) and their philosophical comparison," plus extensions (DnS, a preliminary Ontology of Plans, an ontology of Web Services), machine-readable encodings, an example of formal semantic links between modules, and a DOLCE–WordNet mapping. This independently confirms `docs/evaluations/comparable-projects-survey.md`'s exact-coverage finding (DOLCE, OCHRE, BFO — not GFO, the point of difference from ROMULUS's DOLCE/BFO/GFO trio) against a primary LOA source rather than only the prior external-tool-sourced report. No license statement, author byline, or publication date found on the page itself. Formalizes the `xwkont:ref:*` record flagged outstanding in `TODO.md`'s "Standards & Prior Art Follow-up" section.
