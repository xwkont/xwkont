# Comparable Public Projects Survey

> **Status:** Externally sourced discovery finding, not independently verified, not an adoption or abandonment decision
> **Produced:** 2026-07-01 12:01 EDT, via ChatGPT deep research (external tool), at the user's request
> **Filed:** 2026-07-01, as a companion to `docs/evaluations/prior-art-survey.md`
> **Provenance classification:** Referenced (external material under evaluation; not adopted, not independently verified claim-by-claim)

## Important caveat before reading

This report was produced by an external AI research tool (ChatGPT deep research), not by Claude working in this repository, and pasted into the repository by the maintainer. Its inline `citeturnNsearchM`-style markers are **ChatGPT-internal tool-call references** — they are not resolvable URLs and do not meet this project's citation standard (`docs/EDITORIAL_POLICY.md`, `ADR-0012`). They have **not** been independently verified by re-fetching each source.

Treat every specific factual claim below (project names, maintainers, dates, license status, "dormant" assessments) as **not yet verified** until an XwkOnt maintainer independently confirms it and creates a proper `xwkont:ref:*` reference record with a real URL/DOI/archival snapshot per `ADR-0012`. This document is filed for its research leads, not as a citable source in its own right.

## Why this matters

`docs/evaluations/prior-art-survey.md` (2026-07-01) surveyed academic literature and standards (Borgo/Galton/Kutz 2022, Trojahn et al. 2022, ISO/IEC 21838, SSSOM, COLORE) and concluded XwkOnt's niche — a living, concept-indexed, openly licensed public crosswalk of foundational ontologies — was not filled by existing work. That survey did **not** search specifically for prior *public projects* attempting the same crosswalk mission (as opposed to papers or standards). This report does, and finds two candidates materially closer to XwkOnt's actual brief than anything in the earlier survey:

- **WonderWeb Foundational Ontologies Library (WFOL)** — described as intended "as a reference point for easy and rigorous comparisons among different ontological approaches," covering DOLCE, OCHRE, and BFO with philosophical comparison and machine-readable encodings. Historical, not modern publication infrastructure.
- **ROMULUS** — described as the strongest near-exact operational match: an online repository of BFO/DOLCE/GFO with explicit comparison, alignment, mapping, merging, and mediation-metadata sections, plus a foundational-ontology-selection recommender. Reportedly legacy/dormant (visible activity clustering 2012-2015).

If accurate, these should have been surfaced in the original prior-art survey and materially inform (without necessarily reversing) the earlier "don't abandon" conclusion — see Assessment below.

## Report

### Executive summary

No currently active public project was found matching the full XwkOnt brief — a publication-first resource whose primary purpose is to crosswalk and document authoritative correspondences among foundational ontologies without becoming a new ontology itself. The two closest historical predecessors identified are **WonderWeb/WFOL** and **ROMULUS**. Other adjacent-but-different efforts identified: **ONSET** (ontology-selection recommender, not a crosswalk publication), **COLORE** (broad first-order ontology repository/verification in Common Logic — already covered in `prior-art-survey.md`), **OAEI foundational-ontology matching studies** (benchmark/evaluation, not a maintained reference library), **CoModIDE's Upper Ontology Alignment Tool** (domain-to-upper alignment engineering tool), **Ontohub + DOL** (heterogeneous-ontology repository/mapping infrastructure), and **DOLCE ergo SUMO / SWIntO** (a "near miss" that used comparison work to build a new hybrid ontology — the opposite of XwkOnt's stated non-goal).

### How the report defined a match

A project was treated as an exact/near-exact match only if its primary purpose was, at once: maintaining multiple foundational ontologies side by side; documenting concept-level correspondences; supporting explicit comparison/mediation; preserving or citing authoritative definitions; and publishing as a reusable reference resource rather than a new upper ontology. By that standard, WFOL and ROMULUS were judged the closest matches; everything else was judged adjacent-but-different (selection tooling, repository infrastructure, formal verification, benchmarks, or domain-engineering support).

### Closest matches

**WonderWeb Foundational Ontologies Library.** Per the report, official LOA/CNR pages describe DOLCE as one module within WFOL alongside OCHRE and BFO, containing reference modules, philosophical comparison, machine-readable encodings, formal semantic links between modules, and a DOLCE-WordNet mapping. FAIRsharing's summary reportedly frames the library explicitly as a basis for rigorous cross-approach comparison and for harmonizing/integrating existing ontologies and metadata standards by manual mapping — close to XwkOnt's stated objective. Difference: a historical research-program library, not a modern repo-centered publication project.

**ROMULUS.** Per the report, described on its own site as "a repository of foundational ontologies" with explicit sections for comparison, alignment, mapping, merging, alignment metadata, ontology metadata, downloads, and ontology selection. A 2015/2016 Journal on Data Semantics article reportedly describes it as "the first online library of machine-processable, modularised, aligned, and logic-based merged foundational ontologies," including a catalogue of mappable/non-mappable elements among BFO, GFO, and DOLCE, plus a recommender spanning six foundational ontologies. Reportedly legacy/dormant based on visible site-edit dates (clustering 2012-2014) and repository activity. Maintainers reportedly Zubeida Casmod Khan and C. Maria Keet (South African academic/CAIR-affiliated work).

### Related but materially different efforts

- **ONSET** — questionnaire-based foundational-ontology *selection and explanation* tool (reportedly covering DOLCE, BFO, GFO, SUMO, YAMATO, GIST in v2), integrated with ROMULUS; answers "which ontology should I use," not "here is a maintained crosswalk."
- **COLORE** — already covered independently in `prior-art-survey.md`; this report adds that a 2017 paper ("Upper Ontologies in COLORE") specifically discusses verification/modularization of DOLCE and SUMO and specification of mappings between upper ontologies.
- **OAEI foundational-ontology matching studies** — a 2019 study reportedly evaluated matcher performance on BFO/DOLCE/GFO/SUMO using manually curated reference alignments from ROMULUS and DOLCE-SUMO literature, concluding current matchers perform poorly on foundational ontologies. Benchmark-centric, not a maintained reference library.
- **CoModIDE's Upper Ontology Alignment Tool** — a Protégé extension for aligning *domain* ontology elements to upper-ontology concepts (BFO/DOLCE/SUMO); engineering tooling, not upper-to-upper crosswalk publication. Reportedly low recent activity (latest release cited as 2021).
- **Ontohub + DOL** — heterogeneous-ontology repository and mapping metalanguage infrastructure; enabling technology, not a curated crosswalk product itself. Reportedly low recent OSS activity (latest release cited as 2016).
- **DOLCE ergo SUMO / SWIntO** — used foundational-ontology comparison to build **SmartSUMO**, a hybrid ontology combining DOLCE and SUMO. Explicitly the opposite move from XwkOnt's non-goal (XwkOnt does not create a new foundational ontology).
- **LOV / NCBO BioPortal** — vocabulary/ontology discovery registries with mapping features at scale; registries, not curated foundational-ontology crosswalk publications.

### Coverage asymmetry noted in the report

The best-documented prior crosswalk efforts (WFOL, ROMULUS) centered on **DOLCE, BFO, and GFO**; SUMO appears mainly in ONSET/COLORE/OAEI/DOLCE-SUMO integration work. **UFO** appears in the broader landscape and OntoUML/UFO documentation but, per this report, not as part of any of the closest-match projects surveyed. If accurate, XwkOnt documenting UFO alongside BFO/DOLCE/SUMO would extend beyond what the nearest public predecessors maintained.

## Assessment (Claude, filing this document)

This report does not overturn `prior-art-survey.md`'s "don't abandon" conclusion, but it does sharpen it and adds a genuine research obligation:

1. **ROMULUS is the most serious prior-art candidate found across both surveys.** If the report's characterization is accurate, it did most of what XwkOnt aims to do — for a narrower ontology set (BFO/DOLCE/GFO, not UFO), with a heavier emphasis on formal merge/interchange tooling than XwkOnt intends, and is reportedly dormant. A dormant, narrower-scope, more-formal predecessor is a "gap XwkOnt could legitimately fill or revive," not evidence XwkOnt is redundant with an active project.
2. **This needs independent verification before it changes anything concrete.** Every specific claim here (maintainers, dates, license, dormancy) came from an external tool's unverified citations. Before citing ROMULUS or WFOL in `README.md`, an ADR, or any crosswalk, someone needs to actually visit the real ROMULUS/WFOL sites, confirm they still exist and are dormant, and create proper `xwkont:ref:*` records.
3. **No immediate action is forced.** The two concept crosswalks already written (`continuant-occurrent.md`, `object.md`) do not reference ROMULUS/WFOL and don't need to be redone. But future work — especially any README/scope-statement language about XwkOnt being novel — should acknowledge ROMULUS/WFOL once verified, rather than implying no comparable effort ever existed.

### Independent verification update (2026-07-01, Claude)

Partial verification of the "why abandoned" question was performed directly (not via the external report):

- **WonderWeb/WFOL — confirmed, and the reason is mundane.** Per CORDIS (the EU's own project database), WonderWeb was EU Framework Programme 5 grant **IST-2001-33052**, running **2002-01-01 to 2004-06-30**, coordinated by Ian Horrocks. It was a fixed-term research contract that delivered its contracted outputs (DOLCE, deliverables D17/D18) and then formally concluded — not a failure, just the normal lifecycle of a term-limited EU grant with no built-in mechanism for continued maintenance afterward. DOLCE itself continued to be used/cited independently of the library's own upkeep.
- **ROMULUS — genuinely unresolved.** The live site (`thezfiles.co.za/ROMULUS/`) was fetched directly: it is still technically online, but its most recent dated content is **March 2014** (a source-code release announcement); nothing since. A targeted search for any retrospective or explicit statement from the authors (Khan/Keet) about why development stopped found **none published**. This is a confirmed negative finding, not filled in by inference.
- **Best-supported inference (labeled as inference, not fact):** ROMULUS originated from Zubeida Khan's PhD research under Maria Keet at UCT. The pattern — a thesis produces a working artifact and papers, the student graduates, and no funding mechanism exists specifically for *maintaining* (as opposed to *producing*) the software afterward — is extremely common in ontology/semantic-web research generally, not specific to ROMULUS.
- **Relevance to XwkOnt:** both closest prior-art matches died from the same underlying cause — research/grant funding pays for producing results, not for indefinite hosting and maintenance. XwkOnt, run without institutional backing, carries the same structural exposure. See the new "Continuity and Sustainability" question this raised in `docs/governance/governance.md`.

### License and exact-coverage verification (2026-07-03)

Direct verification, closing the remaining gap the 2026-07-01 update left open:

- **ROMULUS — license: no explicit terms stated.** The live site (`thezfiles.co.za/ROMULUS/`) was fetched directly again. It offers source-code and ontology-module downloads and references the "SUGOI" interchangeability tool, but states no license or copyright terms anywhere on the page — not CC, not an OSI license, nothing. Recorded as `unknown`, per the project's "do not guess" rule, not inferred as open from the mere fact that downloads are offered.
- **ROMULUS — exact ontology coverage confirmed: three, not more.** The site states directly: "Currently there are three foundational ontologies in the repository: DOLCE, BFO and GFO." No UFO, no SUMO, no YAMATO/TUpper/GUM. This is narrower than XwkOnt's 8-source scope (`ADR-0015`) even before considering XwkOnt's non-goal of formal merging.
- **WFOL — license: no explicit terms stated.** Both the LOA/CNR DOLCE page and the WonderWeb D17/D18 deliverable citations were checked; none states an explicit license for the DOLCE files or the library as a whole.
- **WFOL — exact ontology coverage confirmed: DOLCE, OCHRE, and BFO** (not GFO) — "DOLCE was originally developed within the WonderWeb project and was conceived as the first module of the WonderWeb Foundational Ontologies Library (WFOL) together with OCHRE and BFO." Different trio from ROMULUS's DOLCE/BFO/GFO — the two predecessors do not have identical coverage, despite both often being cited together.
- **Dormancy reconfirmed, maintainer's independent assessment matches:** both projects remain closed/inactive as of this check — WFOL by confirmed grant conclusion (2004-06-30, see 2026-07-01 update above), ROMULUS by no dated activity found past March 2014. Consistent with the 2026-07-01 finding; no new activity discovered.

## Deferred Questions

1. ~~Independently verify ROMULUS's and WFOL's current status (active/dormant, license, exact ontology coverage)~~ — **done, 2026-07-03** (see verification section above). Both projects' licenses are confirmed unstated/unknown (not guessable as open or closed); exact coverage differs between the two (ROMULUS: BFO/DOLCE/GFO; WFOL: DOLCE/OCHRE/BFO). A proper `xwkont:ref:*` record is still needed only if either is cited directly in a crosswalk or README — not yet done, tracked below.
2. Decide whether `README.md` or `docs/FOUNDING_PRINCIPLES.md` should acknowledge ROMULUS/WFOL as historical predecessors now that verification is complete — not decided by this document.
3. Consider whether ROMULUS's "mappable and non-mappable elements" catalogue methodology (now verified to exist, scoped to BFO/DOLCE/GFO) offers a reusable pattern for XwkOnt's own mapping-assertion / uncertainty sections, beyond what SSSOM (`ADR-0009`) already provides.
