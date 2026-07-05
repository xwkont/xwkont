# ADR-0022: Reinforce the Eight-Source Scope Against Self-Classification

- **Status:** Accepted
- **Date:** 2026-07-05

## Context: Why This Review Happened

`ADR-0015` expanded XwkOnt's source-ontology scope from four to eight (BFO, DOLCE, SUMO, UFO, GFO, YAMATO, TUpper, GUM) on three grounds: Reuse Before Introduce (TUpper's ISO standing), fetchability of each new source's primary artifacts, and "coherence of the comparison set" — that Borgo, Galton & Kutz's 2022 comparative paper treats these eight as peers. None of those three grounds checked whether each source *classifies itself* as a foundational/upper/top-level ontology. Having just run exactly that kind of self-classification check for "core" (`ADR-0020`/`ADR-0021`), the maintainer asked whether XwkOnt's own 8-source scope should be checked the same way, rather than resting on a secondary paper's framing and practical considerations alone.

Before checking each source, a prior terminological question had to be settled: are "foundational ontology," "upper ontology," and "top-level ontology" actually synonyms, or is one of them doing different work — the same kind of Sense-1/Sense-2 split that mattered for "core"?

## Deliberation

**1. The terminology question resolved cleanly, with a single authoritative primary source — no split found.** `ISO/IEC 21838-1:2021` ("Top-level ontologies (TLO) — Part 1: Requirements," the standard BFO and TUpper are already published under) was fetched directly (`cdn.standards.iteh.ai`'s free preview PDF, extracted with `pdftotext` — see the correction this pass made to `docs/methodology/primary-source-verification.md`'s PDF-extraction note, which had wrongly assumed `pdftotext` unavailable). §3.20 defines the term formally and settles the question in its own words:

> "**top-level ontology, TLO** — ontology that is created to represent the categories that are shared across a maximally broad range of domains... Note 1 to entry: Top-level ontologies are 'reference ontologies'... A top-level ontology is sometimes referred to as a 'formal ontology', 'foundational ontology', 'upper level ontology', or 'domain-neutral ontology'."

Unlike "core" (where Scherp et al.'s domain-tier sense genuinely didn't fit XwkOnt), there is no analogous split here — the standard governing two of our own eight sources states the equivalence directly, and adds two further synonyms ("formal ontology," "domain-neutral ontology") neither the maintainer nor this investigation had raised.

**2. Checked each of the eight sources directly against this definition — self-classification, not inferred from secondary description.**

**3. A genuinely new finding surfaced along the way: DOLCE is also ISO-standardized.** `ADR-0015` and every existing DOLCE reference record cite BFO's ISO/IEC 21838-2:2021 and TUpper's ISO/IEC 21838-4:2023 status, but none mention that DOLCE itself was standardized as **ISO/IEC 21838-3:2023**, "Top-level ontologies (TLO) — Part 3: Descriptive ontology for linguistic and cognitive engineering (DOLCE)" — confirmed across multiple independent standards-body catalog listings (ISO, IEC, VDE, NEN, BSI, AFNOR), though the standard's own full text remains paywalled, consistent with BFO's and TUpper's ISO citations elsewhere in this repository. This means three of XwkOnt's eight sources (BFO, DOLCE, TUpper) are published as consecutive parts (2, 3, 4) of the same ISO 21838 TLO family — a stronger and more coherent pattern than `ADR-0015` itself recorded.

## Research Summary Table

| Source | Self-classification evidence | Which ISO-21838-1-§3.20 synonym it matches |
|---|---|---|
| BFO | Standardized as **ISO/IEC 21838-2:2021**, "Top-level ontologies (TLO) — Part 2: Basic Formal Ontology (BFO)" | top-level ontology (by ISO publication itself) |
| DOLCE | Standardized as **ISO/IEC 21838-3:2023**, "Top-level ontologies (TLO) — Part 3: DOLCE" (new finding this pass) | top-level ontology (by ISO publication itself) |
| TUpper | Standardized as **ISO/IEC 21838-4:2023**, "Top-level ontologies (TLO) — Part 4: TUpper" | top-level ontology (by ISO publication itself) |
| SUMO | Name itself: "**Suggested Upper** Merged Ontology" | upper (level) ontology |
| UFO | Name itself: "**Unified Foundational** Ontology" | foundational ontology |
| GFO | Name itself: "**General Formal** Ontology"; own `dc:description` (already fetched, `xwkont:ref:gfo`): "a **top-level ontology** for conceptual modeling" | formal ontology; top-level ontology (both, independently) |
| YAMATO | Name itself: "Yet Another More Advanced **Top-level Ontology**" | top-level ontology |
| GUM | Name itself: "Generalized **Upper** Model" | upper (level) ontology |

All eight self-classify using at least one of ISO/IEC 21838-1's own five listed synonyms — three by the strongest possible evidence (ISO standardization itself, which requires meeting §4's TLO requirements), the other five by their own chosen name.

## Decision

**XwkOnt's eight-source scope (`ADR-0015`) is reinforced, not revised, by direct self-classification evidence.** Every one of the eight sources classifies itself — via ISO standardization or its own chosen name — as a foundational/upper/top-level/formal ontology, terms `ISO/IEC 21838-1:2021` §3.20 confirms are synonymous, not competing categories. This closes the gap `ADR-0015` left open (scope decided on secondary-literature and practical grounds, not self-classification) with the same rigor `ADR-0020`/`ADR-0021` applied to "core," using existing evidence already fetched in this repository wherever possible (GFO's `dc:description`, already quoted in `ref-gfo.md`) rather than re-deriving it.

**This ADR does not establish a new admission criterion requiring self-classification for any future ninth source** — it confirms the existing eight against one, as a check, not a rule for what comes next. Whether self-classification should become a formal requirement for adding a ninth source is a separate question this ADR does not decide.

## Scope

This ADR does **not**:

- Reopen `ADR-0015`'s Decision, Scope, or Rationale — it reinforces the same eight-source conclusion with evidence the original decision did not check, the same relationship `ADR-0019` has to `ADR-0011`.
- Change any crosswalk content, reference record status, or mapping assertion.
- Decide whether future source-ontology additions must pass a self-classification check as a formal admission criterion (separate from `ADR-0018`'s existing source-count-threshold criterion for concept admission, which is unrelated).
- Independently verify ISO/IEC 21838-3:2023's own full text (paywalled) — its existence and title are confirmed via multiple independent standards-body catalog listings, not a direct read of the standard itself, consistent with how this repository already cites BFO's and TUpper's ISO standing.

## Consequences

### Positive

- Closes a real gap in `ADR-0015` with direct evidence, cleanly resolved (unlike "core," no Sense-1/Sense-2 split muddies the terminology here) — a stronger and faster investigation than the "core" one it mirrors.
- Surfaces a previously undocumented fact (DOLCE's ISO/IEC 21838-3:2023 status) that strengthens `ADR-0015`'s own "Reuse Before Introduce" rationale for TUpper — now three of eight sources, not one, carry ISO standardization.
- Corrects an outdated claim in `docs/methodology/primary-source-verification.md` (that this environment lacks `pdftotext`) discovered as a side effect of fetching ISO/IEC 21838-1 directly — a process improvement independent of the scope question itself.

### Trade-offs

- Confirms the existing scope rather than testing whether a stricter or different criterion might have excluded any of the eight — this was a reinforcement exercise, not an adversarial one, so it cannot be read as ruling out that a different criterion might someday suggest a different scope.
- SUMO, UFO, GFO, YAMATO, and GUM's self-classification rests on their own chosen name, not third-party standardization the way BFO/DOLCE/TUpper's does — a real evidentiary tier difference within the eight, worth keeping visible rather than treating all eight as equally strong on this specific criterion.

## References

- `docs/adr/ADR-0015-expand-source-ontology-scope-to-eight.md` (reinforced, not reopened)
- `docs/adr/ADR-0019-reinforce-concept-against-practitioner-usage.md`, `docs/adr/ADR-0020-define-core-as-base-module-not-domain-tier.md`, `docs/adr/ADR-0021-source-classified-core-placement-criterion.md` (same reinforcement method, applied here)
- ISO/IEC 21838-1:2021, *Information technology — Top-level ontologies (TLO) — Part 1: Requirements*, §3.20 (directly fetched, `pdftotext`-extracted)
- ISO/IEC 21838-2:2021 (BFO), ISO/IEC 21838-3:2023 (DOLCE), ISO/IEC 21838-4:2023 (TUpper)
- `docs/references/ref-gfo.md`, `docs/references/ref-dolce-borgo-2022.md` (updated this session with the ISO/IEC 21838-3:2023 finding)
- `docs/methodology/primary-source-verification.md` (§1 corrected: `pdftotext` availability)
