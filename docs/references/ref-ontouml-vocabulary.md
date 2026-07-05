# OntoUML Vocabulary (OWL/Turtle)

> **Local reference identifier:** `xwkont:ref:ontouml-vocabulary`
> **Slug:** `ontouml-vocabulary`
> **Editorial status:** `candidate`
> **Created:** `2026-07-04`
> **Modified:** `2026-07-04`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | OntoUML Vocabulary | A Turtle/OWL vocabulary for the OntoUML conceptual-modeling profile — the stereotype/metamodel machinery (`ClassStereotype`, `RelationStereotype`, `PropertyStereotype`, etc.) used to annotate UFO-grounded conceptual models. Not a restatement of UFO's own theory. |
| Creator | unknown | Repository does not carry an explicit author/creator annotation distinct from the OntoUML project generally; do not attribute to a specific individual without checking further. |
| Contributor | unknown | Not verified in this pass. |
| Publisher | OntoUML project; hosted at `github.com/OntoUML/ontouml-vocabulary` | Namespace `https://w3id.org/ontouml`. |
| Source type | OWL/Turtle vocabulary (machine-readable, not a paper) | |
| Version or edition | unknown — no `owl:versionInfo` checked in this pass | |
| Identifier or URL | `https://w3id.org/ontouml`; fetched from `https://raw.githubusercontent.com/OntoUML/ontouml-vocabulary/master/ontouml.ttl` | No DOI. |
| Access date | 2026-07-04 | |
| Snapshot / Stable identifier | `unknown — not yet archived` | Not checked against the Wayback Machine in this pass; do not fabricate a snapshot URL per `ADR-0012`. |
| Rights/license | unknown | Not verified in this pass. |
| Archive mirror status | not applicable — license unknown or unverified | Per `ADR-0016`. |

## Source Relation Notes

This vocabulary is a **derived, non-primary artifact for UFO's own substantive theory**, the same status `xwkont:ref:ufo-2021`'s Source Relation Notes already assign to gUFO — cite it for OntoUML modeling-notation stereotypes (`ClassStereotype`, `RelationStereotype`, `PropertyStereotype` individuals), not as a restatement of UFO's Endurant/Perdurant/Moment theory. Where the UFO 2021 paper itself is paywalled and unreachable, this vocabulary is a usable fallback for OntoUML-specific stereotype content only, not a substitute for the paper's theoretical framing (per the existing note in `docs/evaluations/foundational-ontology-concept-terms-matrix.md`'s Cross-Cutting Observation 3).

## Rights and License Notes

Not verified in this pass. Treat as unknown rather than guessed.

## Citation and Locator Notes

Recommended citation: OntoUML Vocabulary, OntoUML project, `https://w3id.org/ontouml`, `https://github.com/OntoUML/ontouml-vocabulary`.

**Direct primary-source verification (2026-07-04):** `ontouml.ttl` was fetched directly and searched full-text for "time"/"temporal"/"interval"/"duration" while researching the `docs/crosswalks/concepts/time.md` crosswalk — zero occurrences of any of the four terms anywhere in the file. The file does define `ontouml:begin` and `ontouml:end`, but both are individuals of `ontouml:PropertyStereotype` (identical gloss for each: "An individual of the ontouml:PropertyStereotype used to assign the corresponding stereotype to a given ontouml:Property") — i.e., annotations for tagging a UML property as marking a start/end point, not classes denoting a temporal region, instant, or interval. `time.md` records this as `not applicable` for a UFO Time correspondence, consistent with [`candidate-concepts.md`](../crosswalks/candidate-concepts.md)'s existing tagging of `UFO.22 begin`/`UFO.23 end` as "Ungrouped — temporal-boundary property, not a class."

Locator: `https://raw.githubusercontent.com/OntoUML/ontouml-vocabulary/master/ontouml.ttl`, lines 1035–1043 (`begin`), 1141–1147 (`end`).
