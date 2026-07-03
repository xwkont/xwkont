# Prior Art Survey: Foundational Ontology Comparison and Mapping

> **Status:** Discovery finding, not an adoption decision
> **Research conducted:** 2026-07-01 13:59 Z (2026-07-01 09:59 EDT)
> **Trigger:** User request to verify whether XwkOnt duplicates existing work before writing the first concept crosswalks, following `~20260701-0944-meta-ontology.md`'s discovery-phase question ("are we reinventing the wheel?")
> **Method:** Web search (no fixed corpus; snapshot of what was findable on the date above). Findings should be re-verified if cited as adoption evidence in a later ADR — web content changes.

## Purpose

Before writing the first concept crosswalks (Object, Event) and before extending `ADR-0007`'s mapping-record identifier scheme, this survey checks whether comparable prior art already exists for (a) comparing foundational ontologies concept-by-concept, and (b) representing ontology-to-ontology mappings as structured records.

Provenance classification for all sources below: **Referenced** (external authoritative materials reviewed for relevance; no adoption/adaptation decision is made by this document).

## Survey Findings

### Concept-level comparisons of multiple foundational ontologies

- Borgo, Galton, Kutz, "Foundational ontologies in action," *Applied Ontology* 17(1), 2022, pp. 1-16 — editorial introducing a special issue that systematically compares seven foundational ontologies (BFO, DOLCE, GFO, GUM, TUpper, UFO, YAMATO) through common modeling cases (e.g., how each treats "color"). Methodologically close to XwkOnt's concept-centric crosswalk approach. Source: <https://journals.sagepub.com/doi/10.3233/AO-220265>
- Trojahn, Vieira, Schmidt, Pease, Guizzardi, "Foundational Ontologies meet Ontology Matching: A Survey," *Semantic Web Journal*, 2022 — systematic survey of ontology-matching approaches applied specifically to foundational ontologies. Source: <https://www.semantic-web-journal.net/system/files/swj2650.pdf>
- Semy, Pulvermacher, Obrst (or similar authorship), "A Comparison of Upper Ontologies" — earlier comparison paper. Source: <https://www.researchgate.net/publication/220866366_A_Comparison_of_Upper_Ontologies>

### Pairwise formal mappings between specific foundational ontologies

- "Mapping BFO and DOLCE" — framework mapping BFO and DOLCE categories via equivalence and subsumption. Source: <https://www.researchgate.net/publication/46273581_Mapping_BFO_and_DOLCE>
- DOLCE-SUMO alignment work (SmartDOLCE / SmartSUMO).

### Standards infrastructure for top-level ontology interoperability

- ISO/IEC 21838, multi-part standard: Part 1 defines requirements for top-level ontologies (TLOs); Parts 2-4 certify BFO, DOLCE, and TUpper as conformant against those requirements. Explicitly intended to promote interoperability among TLOs and support mapping domain ontologies through a common hub. Source: <https://en.wikipedia.org/wiki/ISO/IEC_21838>, <https://www.iso.org/standard/71954.html>

### Mapping-record / mapping-metadata standards

- **SSSOM (Simple Standard for Sharing Ontological Mappings)** — mature, actively maintained, tooled standard for representing ontology mappings: predicates, confidence, mapping justification, provenance, table-based serialization. Source: <https://github.com/mapping-commons/sssom/>, spec at `http://w3id.org/sssom/spec`, <https://arxiv.org/abs/2112.07051>
- **OxO / OxO2** — a live, maintained, SSSOM-based "crosswalk browser," proving the browsable-crosswalk pattern works in production, for biomedical/OBO ontologies (not foundational ontologies). Source: <https://arxiv.org/pdf/2506.04286>

### Formal verification infrastructure (different use case, adjacent domain)

- **COLORE** (Common Logic Ontology Repository, Grüninger, University of Toronto) — repository of first-order ontologies specified in Common Logic (ISO 24707), with automated-reasoning-verified equivalence/interpretation relationships between ontologies. More rigorous than XwkOnt's conservative RDF/RDFS/SKOS scaffold; aimed at formal verification rather than human-readable comparison. Source: <https://github.com/gruninger/colore>

## Assessment

No prior-art item found is a living, continuously maintained, openly licensed, concept-indexed public reference specifically comparing foundational/upper ontologies that a newcomer can browse by concept. The closest analog (Borgo/Galton/Kutz 2022) is a frozen, journal-published special issue covering a fixed set of worked examples, not an extensible ongoing reference. OxO/OxO2 demonstrates the target architecture (browsable, SSSOM-based crosswalk) but for a different content domain (biomedical ontologies).

**Conclusion: XwkOnt's stated niche is not filled by existing work and does not need to be abandoned.** However, two concrete follow-ups exist:

**Update (2026-07-01):** `docs/evaluations/comparable-projects-survey.md` — a separate, externally sourced (ChatGPT deep research) survey specifically of prior public *projects* rather than academic literature — identified two closer candidates this survey missed: **WonderWeb Foundational Ontologies Library (WFOL)** and, more seriously, **ROMULUS**, described as a near-exact operational match (BFO/DOLCE/GFO comparison/alignment/mapping/merging repository, reportedly dormant since ~2015). That survey's claims are not independently verified — see its caveats — but it sharpens rather than reverses this survey's conclusion; see that document's Assessment section.

1. **Likely reinvention risk:** `ADR-0007`'s mapping-record identifier scheme (`xwkont:mapping:<concept-slug>:<nnn>`) should be checked against SSSOM's predicate/confidence/provenance model before the first real mapping assertion is recorded. This is the one place this survey found where XwkOnt may have introduced a project-specific convention that a maintained standard already addresses — a direct violation risk of "Reuse Before Introduce" that a wider prior-art check would have caught earlier.
2. **Citation obligation:** the first concept crosswalks (Object, Event) should cite and build on Borgo/Galton/Kutz 2022 and Trojahn et al. 2022 as primary sources where applicable, per `docs/EDITORIAL_POLICY.md`'s requirement that every claim be traceable to an authoritative reference, rather than re-deriving comparisons from raw source-ontology documentation in isolation.

## Deferred Questions

- Should SSSOM be adopted, adapted, or only referenced for XwkOnt's mapping-record schema? This requires dedicated evaluation and, if adopted/adapted, an ADR — this survey does not decide it.
- Should ISO/IEC 21838's TLO requirements (Part 1) inform how XwkOnt frames its "Entity" comparison root? Not evaluated in this pass.
- Has `~20260701-0944-meta-ontology.md`'s own candidate list (MOF, ODM, DOL, Common Logic, OMV, VoID) been reconciled with this survey and the existing `docs/STANDARDS_BASELINE.md` disposition vocabulary? Not yet — that file still needs its own cleanup/relocation (see review feedback from this survey's own review pass).
