# General Formal Ontology (GFO)

> **Local reference identifier:** `xwkont:ref:gfo`
> **Slug:** `gfo`
> **Editorial status:** `candidate`
> **Created:** `2026-07-02`
> **Modified:** `2026-07-03`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | General Formal Ontology (GFO) | Top-level ontology for conceptual modeling; per the ontology's own `dc:description`. |
| Creator | Heinrich Herre (lead); Onto-Med research group, University of Leipzig | Multiple contributors across the ontology's history since 2006; do not treat as a complete author list. |
| Contributor | unknown | Full contributor list not verified in this pass. |
| Publisher | Onto-Med research group; hosted at `github.com/Onto-Med/GFO` and dereferenceable at `https://w3id.org/gfo` | |
| Source type | ontology specification (OWL) | Modular: root `gfo.owl` imports `modules/gfo-base.owl`; a `situation` module also exists but was not consulted in this pass. |
| Version or edition | 2024-11-18 release (`versionIRI` `https://w3id.org/gfo/release/2024-11-18`); prior version 2024-07-05 | Both root and base module carry this same version date. |
| Identifier or URL | <https://w3id.org/gfo> (root); <https://github.com/Onto-Med/GFO> (repository); DOI `10.5281/zenodo.5205419` (per the ontology's own `bibo:doi` annotation, not independently resolved in this pass) | |
| Access date | 2026-07-02 | |
| Snapshot / Stable identifier | `https://github.com/Onto-Med/GFO` → <http://web.archive.org/web/20250902115637/https://github.com/Onto-Med/GFO> (2025-09-02), verified retrievable via the Internet Archive Wayback Machine at time of writing, per `ADR-0012`. No snapshot found for the raw `modules/gfo-base.owl` file specifically (`wayback/available` returned no result for that exact URL) — the repository-level snapshot is the fallback, consistent with `xwkont:ref:bfo-2020`'s precedent for GitHub-hosted OWL sources. | |
| Rights/license | CC-BY-4.0 | Per the ontology's own `terms:license` annotation (`http://creativecommons.org/licenses/by/4.0/`), not independently checked against a separate repository LICENSE file. |
| Archive mirror status | eligible — license permits redistribution, not yet mirrored | Per `ADR-0016`. CC-BY-4.0 is verified from the ontology's own metadata (see Rights/license), which is sufficient to make this record eligible; actual mirroring (hosting location, fetch, publish) is separate future work not yet started. |

## Source Relation Notes

`gfo.owl` (the root ontology document, fetched from `raw.githubusercontent.com/Onto-Med/GFO/main/gfo.owl`) is a thin wrapper that `owl:imports` `https://w3id.org/gfo/base`; the substantive class definitions relevant to this crosswalk (`Occurrent`, `Presential`, `Process`) live in the imported base module, fetched separately from `raw.githubusercontent.com/Onto-Med/GFO/main/modules/gfo-base.owl`. Both were fetched directly as plain-text OWL/XML — no PDF extraction needed, consistent with the assessment that GFO has the most straightforward fetch path of any source ontology added by `ADR-0015`.

## Rights and License Notes

CC-BY-4.0 per the ontology document's own metadata; not cross-checked against a separate repository LICENSE file in this pass.

## Citation and Locator Notes

Recommended citation: General Formal Ontology (GFO), Onto-Med research group, version 2024-11-18, `https://w3id.org/gfo` (root), `https://w3id.org/gfo/base` (base module), DOI `10.5281/zenodo.5205419`.

**Direct primary-source verification (2026-07-02):** `gfo.owl` and `modules/gfo-base.owl` were fetched directly from the `Onto-Med/GFO` GitHub repository (`main` branch — note this differs from `xwkont:ref:bfo-2020`'s `master` branch; GFO's default branch is `main`) and read directly to verify `continuant-occurrent.md`'s GFO correspondences. Used classes and their exact `skos:definition` text:

- `Occurrent` (`https://w3id.org/gfo/base/Occurrent`): "Occurrents have temporal parts and thus cannot be present at a time-boundary. Time belongs to them, because they happen in time and the time of the occurrent is built into it. The relation between an occurrent and a chronoid is determined by the projection relation. Occurrents are also called generalized processes in the GFO." `owl:disjointWith` `Presential`.
- `Presential` (`https://w3id.org/gfo/base/Presential`): "A presential exists wholly at exactly one time boundary." Subclass of `Concrete` and `Individual`; `owl:disjointWith` `Occurrent`.
- `Process` (`https://w3id.org/gfo/base/Process`): "Processes are a special kind of occurrent. Processes are directly in time, they have characteristics which cannot be captured by a collection of time boundaries." Subclass of `Occurrent`.

Note that GFO's own top-level pair is **Presential/Occurrent**, not "Continuant/Occurrent" — GFO does not use the term "continuant" anywhere in the base module. See `continuant-occurrent.md`'s Uncertainty section for how this terminology gap is handled.

**Reused for `object.md` (2026-07-02):** the same fetched `modules/gfo-base.owl` also supplies `Material_object` (subclass of `Discrete_presential`) and `Material_persistant` — the latter's own definition text glosses this lineage as "those entities which are called sometimes continuants or objects, as apples, cars or houses." See `object.md`'s Source Definitions and correspondence rows 006-007.

**Reused for `event.md` (2026-07-02):** the same fetched `modules/gfo-base.owl` also supplies `Change` (whose own definition text glosses one technical sense as "instantaneous event") and its subtype `Instantaneous_change`. GFO has no class literally named "Event"; `Change`/`Instantaneous_change` are the closest analogs found. See `event.md`'s Source Definitions and correspondence rows 006-007.

**Reused for `process.md` (2026-07-02):** the same fetched `modules/gfo-base.owl` also supplies `Process` (subclass of `Occurrent`, `owl:disjointWith` `Change` and `History`) — "Processes are a special kind of occurrent. Processes are directly in time, they have characteristics which cannot be captured by a collection of time boundaries." The closest structural match to BFO's Process of any `ADR-0015` source. See `process.md`'s Source Definitions and correspondence row 005.

**Reused for `information-artifact.md` (2026-07-02):** the same fetched `modules/gfo-base.owl` also supplies `Symbol`/`Symbol_structure`, considered and rejected as an Information-Artifact correspondence — they sit on GFO's `Category` (universal/type) side, disjoint from `Individual`, a formal-language-symbol concept rather than a content-bearing individual artifact. No correspondence recorded; GFO's separate `situation` module was not checked (see `information-artifact.md`'s `uncertainty-004`). See `information-artifact.md`'s Source Definitions.

**Reused for `quality.md` (2026-07-02):** the same fetched `modules/gfo-base.owl` also supplies `Property` (a `Concrete`, `Dependent` individual — trope-theoretic, joining BFO/DOLCE/UFO's camp rather than SUMO's abstracta), `Property_value`, and `Value_space`. `Value_space`'s own definition text independently cites both Gärdenfors (2000) *and* DOLCE (Masolo, 2003) by name for the value-space/quality-space parallel — the first case in this repository of one source ontology's own primary text citing another already-covered source. See `quality.md`'s Source Definitions and correspondence row 005.

**Reused for `relation.md` (2026-07-02):** the same fetched `modules/gfo-base.owl` also supplies `Relator` (`rdfs:subClassOf` `Individual`, `owl:disjointWith` `Property`, no `skos:definition` of its own) and `Relational_role` (`role_of` some `Relator`). GFO independently uses the exact term "Relator" — the same word UFO's own relation theory uses for a dependent, existentially-linked mediating individual — the strongest terminological convergence found in this crosswalk. See `relation.md`'s Source Definitions and correspondence row 005.

**Reused for `role.md` (2026-07-02):** the same fetched `modules/gfo-base.owl` also supplies `Role` (`rdfs:subClassOf` `Concrete`), `Processual_role` ("dependent processes... roles with a process as context"), `Social_role` (`rdfs:subClassOf` `Independent`, `owl:disjointWith` `Dependent`), and `Relational_role` (already covered for `relation.md`, reused here as the Role-specific correspondence). `Social_role`'s `Independent` classification is the only case in the whole `ADR-0015` buildout of a source treating a role subtype as bearer-independent, directly contradicting BFO/DOLCE-driven/UFO's shared dependent-particular assumption. See `role.md`'s Source Definitions and correspondence row 005.
