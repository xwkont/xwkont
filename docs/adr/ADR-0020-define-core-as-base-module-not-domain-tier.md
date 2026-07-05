# ADR-0020: Define "Core" as XwkOnt's Base Module, Not a Domain-Tier Ontology

- **Status:** Accepted
- **Date:** 2026-07-05

## Context: Why This Review Happened

`data/ontology/core.ttl` and the `xwkont-core:` namespace have existed since the project's initial core-ontology design (2026-06-30/07-01), but no prior work or ADR ever defined what "core" actually means for this project — the name was chosen without a documented rationale. This went unnoticed while `core.ttl` held exactly the original 8 concepts, all added together at `0.1.0`. It stopped being avoidable once the `0.2.0` batch pushed the reviewed-crosswalk count to 17 while `core.ttl` still held only 10 classes (the original 8 concepts, `Continuant`/`Occurrent` counting as 2, plus `Entity`): a real gap opened between "reviewed crosswalk" and "in `core.ttl`," and there was no documented criterion to close it by. An internal candidate-concept inventory had already flagged this explicitly on 2026-07-04 when it dropped "core" from its own filename: *"'core' is dropped for now, pending a future pass that actually defines what would qualify a candidate as 'core.'"* This ADR is that pass — done, per `FOUNDING_PRINCIPLES.md` Principle 2 ("Reuse Before Introduce"), by checking whether "core" already has an established meaning in the ontology-engineering field before inventing an XwkOnt-specific one.

## Deliberation: How the Investigation Actually Went

**1. The first framing was judgment-based, and the maintainer rejected it before any research happened.** The initial approach considered was: sort the 17 concepts by structural position (does this concept define a top-level partition, or does it specialize under one?) and/or by cross-source recurrence, then place each into "core" or "not core" by that judgment. The maintainer stopped this immediately — the request was to ground "core" in what the term means to XwkOnt's actual audience (working ontologists), not to make a fresh set of per-concept editorial calls.

**2. That reframing surfaced two distinct, competing meanings already active in the field, and they point in opposite directions for XwkOnt.**

- **Sense 1 — "core ontology" as a stack tier.** Scherp, Saathoff, Franz & Staab's "Designing Core Ontologies" (Applied Ontology, 2011) and the related Scherp & Franz Event-Model-F work position ontologies on a three-level stack: *foundational* (**"a high-level, abstract vocabulary of concepts and relations that are likely to be used in current and future application domains"**) → *core* (**"establish[es] a common understanding in a particular domain in order to ensure interoperability"**, built "by basing on a foundational ontology") → *domain*. A core ontology in this sense specializes **one** foundational ontology toward **a domain**.
- **Sense 2 — "core module" as internal base/extension modularization.** Independently verified directly against three of XwkOnt's own eight source ontologies' own primary artifacts (already-fetched, already-cited reference records — no new fetching needed for this): BFO's own GitHub repository literally names its foundational file `bfo-core.ttl` (`21838-2/owl/bfo-core.ttl`), distinct from separate relation/IAO extension files; DOLCE's own 2022 comprehensive paper documents the 2009 relabeling explicitly named **"DOLCE-CORE"** by its own authors (Borgo & Masolo), with Role/OntoClean treatment noted as *"external to core DOLCE"*; GFO's own root `README.md` states *"[modules/gfo-base.owl] forms the core module of GFO... we are going to continually provide further modules/extensions... There may be parallel extensions... not all... consistent with each other."* All three use "core" the same way: the base/foundational module a project's own vocabulary is built from, contrasted with "external"/"extension"/"parallel" modules — no domain-tier claim, no specialization-toward-a-domain claim.

**3. Sense 1 was checked seriously, not dismissed on sight, and it fails to fit on its own stated terms.** A core ontology in Scherp et al.'s sense is built by specializing *one* foundational ontology into *a domain*. XwkOnt does neither: it does not pick one of its eight source ontologies as a base to specialize, and it does not model a domain — it compares foundational ontologies against each other. Reading `xwkont-core:` as a Sense-1 "core ontology" would mean XwkOnt has quietly become a new foundational-ontology-adjacent artifact of its own, which cuts directly against `FOUNDING_PRINCIPLES.md`'s Source First / Neutrality commitment (XwkOnt "does not advocate for one [source ontology], or replace them") and the project's own top-level self-description ("It does not create a new foundational ontology").

**4. Sense 2 fits both the evidence and the existing naming, without requiring any new decision to be invented.** Three of XwkOnt's own eight crosswalked sources independently use "core"/"core module" this exact way — a convergent pattern that happens to already clear `ADR-0018`'s own ≥3-source bar for "this is a genuine recurring pattern, not a one-off." `xwkont-core:` and `data/ontology/core.ttl` already read this way structurally (a single base vocabulary file, not a domain specialization of one source), even though no one had stated it as a rule until now.

## Research Summary Table

| Meaning checked | Source | What it actually says | Fits XwkOnt? |
|---|---|---|---|
| Sense 1: core ontology = domain-tier, specializes one foundational ontology | Scherp, Saathoff, Franz & Staab, "Designing Core Ontologies" (Applied Ontology, 2011) | "Core ontologies are characterized by a high degree of axiomatization... achieved by basing on a foundational ontology... pattern-oriented design... modular and extensible." (confirmed via search-engine-mediated snippet; direct fetch blocked by IOS Press/SAGE paywall, ResearchGate 403) | No — XwkOnt doesn't specialize one source or model a domain. |
| Sense 1, same lineage | Scherp & Franz, "F — A Model of Events based on the Foundational Ontology DOLCE+DnS Ultralite" (arXiv, directly fetched 2026-07-05) | Foundational = "high-level, abstract vocabulary... used in current and future application domains"; core = "establish a common understanding in a particular domain... interoperability"; domain ontology sits below that. | No — same reason. |
| Sense 2: core module = base vocabulary vs. extension modules | BFO's own GitHub repository (already fetched, `xwkont:ref:bfo-2020`) | Literal filename `bfo-core.ttl` for the foundational OWL file, separate from relation/IAO extensions. | Yes — matches `xwkont-core:`'s existing structural role. |
| Sense 2, independent confirmation | DOLCE 2022 comprehensive paper (already fetched, `xwkont:ref:dolce-borgo-2022`) | "DOLCE-CORE" (2009, Borgo & Masolo) is the base module name; Role/OntoClean literature is explicitly "external to core DOLCE." | Yes. |
| Sense 2, independent confirmation | GFO's own root `README.md` (fetched 2026-07-05, `xwkont:ref:gfo`) | "[modules/gfo-base.owl] forms the core module of GFO... parallel extensions... not all... consistent with each other." | Yes — this is the third and clinching independent hit. |

## Decision

**"Core" means, for XwkOnt: the base module XwkOnt's own crosswalk vocabulary is built from, as distinct from optional/parallel extension modules — not a domain-tier claim, not a specialization-of-one-source claim.** This is Sense 2 above, adopted because three of XwkOnt's own eight crosswalked source ontologies (BFO, DOLCE, GFO) independently use the word this way in their own primary documentation, and because Sense 1 does not fit what XwkOnt structurally is or does.

This definition is reused, not invented — per `FOUNDING_PRINCIPLES.md` Principle 2, XwkOnt adopts the same base-module/extension-module convention its own source ontologies already use for themselves, rather than inventing a project-specific meaning or importing Scherp et al.'s domain-tier sense where it doesn't fit.

## Scope

This ADR defines the term "core" as used in `xwkont-core:` and `data/ontology/core.ttl`. It does **not**:

- Decide which of the 17 currently-`reviewed` concepts belong in the base module versus a future extension module — that is a separate, subsequent decision this ADR unblocks (by giving it a real criterion to apply) but does not make. Per the maintainer's own framing, that placement work is explicitly out of scope for this ADR.
- Decide the physical file, directory, or namespace structure of any future extension module(s) (e.g., whether XwkOnt gains a `data/ontology/extensions/` directory or additional `xwkont-ext:`-style namespaces mirroring BFO/DOLCE/GFO's own patterns). That is implementation work for whenever the placement decision above is made.
- Reopen `ADR-0018`'s admission bar (source-count threshold for what gets crosswalked at all) — that governs entry into the crosswalk process, not placement within `core.ttl` once reviewed. The two are independent questions this ADR keeps separate.
- Change any existing `core.ttl` content, identifier, or the 10 classes already placed there from `0.1.0`.

## Consequences

### Positive

- Closes a real, self-flagged gap (an internal candidate-concept inventory's dropped-"core" note) with practitioner-literature evidence directly checked against primary sources already sitting in this repository's own reference records — three of eight source ontologies confirmed independently, clearing the same ≥3-source bar `ADR-0018` already uses elsewhere.
- Avoids a credibility risk analogous to the one `ADR-0019` addressed for "Concept": reading `xwkont-core:` as a Sense-1 domain-tier "core ontology" would misrepresent what XwkOnt is to any ontologist familiar with that literature, and would sit awkwardly against `FOUNDING_PRINCIPLES.md`'s Neutrality commitment.
- Gives the still-open "where do the 9 new `0.2.0` concepts go" question (deferred across all 9 crosswalks' Review History entries as separate Turtle-change work) an actual criterion to be resolved against, next time it's picked up.

### Trade-offs

- The definition alone doesn't sort any of the 17 concepts — the practical gap between "17 reviewed" and "10 in `core.ttl`" remains open until a follow-on pass applies this criterion concept-by-concept. This ADR intentionally stops short of that.
- Ontologists who know Scherp et al.'s stack terminology specifically may initially expect `xwkont-core:` to mean a Sense-1 "core ontology" (since that's the more citation-heavy, canonically-named sense in the alignment/core-ontology literature); documentation should stay precise about which sense is meant, the same discipline `ADR-0019` already committed to for "Concept."

## References

- `docs/adr/ADR-0018-comprehensive-concept-coverage-staged-via-minor-releases.md` (≥3-source admission-bar precedent, reused here as the bar for "genuine recurring pattern")
- `docs/adr/ADR-0019-reinforce-concept-against-practitioner-usage.md` (same practitioner-usage-grounding method, applied to "Concept")
- `docs/FOUNDING_PRINCIPLES.md` (Principle 2 — Reuse Before Introduce; Source First / Neutrality)
- `docs/references/ref-bfo-2020.md` (`bfo-core.ttl` filename, directly fetched)
- `docs/references/ref-dolce-borgo-2022.md` ("DOLCE-CORE," "external to core DOLCE," directly fetched)
- `docs/references/ref-gfo.md` (GFO root `README.md` "core module" quote, directly fetched 2026-07-05)
- Scherp, A., Saathoff, C., Franz, T., & Staab, S., "Designing Core Ontologies," *Applied Ontology*, 2011
- Scherp, A. & Franz, T., "F — A Model of Events based on the Foundational Ontology DOLCE+DnS Ultralite," K-CAP 2009 (arXiv:2411.16609)
