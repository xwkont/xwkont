# DOLCE+DnS Ultralite (DUL) OWL Ontology

> **Local reference identifier:** `xwkont:ref:gangemi-dul`
> **Slug:** `gangemi-dul`
> **Editorial status:** `candidate`
> **Created:** `2026-07-01`
> **Modified:** `2026-07-01`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | DOLCE+DnS Ultralite (DUL) | An OWL ontology, not a paper — cited as a primary source document per `ADR-0012`'s provisions for non-paper artifacts. |
| Creator | Aldo Gangemi | Per the ontology's own `owl:versionInfo` annotation: "Created by Aldo Gangemi as both a simplification and extension of DOLCE and Descriptions and Situations ontologies." |
| Contributor | unknown | |
| Publisher | Ontology Design Patterns (ontologydesignpatterns.org) | |
| Source type | OWL ontology (machine-readable, not a paper) | |
| Version or edition | 4.2 (fetched 2026-07-01) | The file's own revision log (embedded `owl:versionInfo` comments) documents changes from version 3.2 through 4.2+. |
| Identifier or URL | <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl> | The `InformationObject` extension module is at <http://www.ontologydesignpatterns.org/ont/dul/IOLite.owl>. |
| Access date | 2026-07-01 | |
| Snapshot / Stable identifier | <http://web.archive.org/web/20260628191619/http://www.ontologydesignpatterns.org/ont/dul/DUL.owl> (2026-06-28) | Verified retrievable via the Internet Archive Wayback Machine at time of writing, per `ADR-0012`. |
| Rights/license | unknown | Not verified in this pass. |

## Source Relation Notes

**DUL is the actively-maintained successor to "DOLCE Lite-Plus" (DLP), not a separate or unrelated artifact.** The ontology's own header states this explicitly: "The DOLCE+DnS Ultralite ontology... is a simplification of some parts of the DOLCE Lite-Plus library (cf. `http://www.ontologydesignpatterns.org/ont/dul/DLP397.owl`)." `docs/crosswalks/concepts/information-artifact.md` and `docs/crosswalks/concepts/quality.md` both previously cited "DOLCE Lite Plus" as the (unconfirmed, un-fetched) source of DOLCE's `Information Object` term; the original `DLP397.owl` file itself returned an ODP wiki page rather than the raw ontology when fetched in this pass, but DUL — built by the same DOLCE lineage (Aldo Gangemi is also a co-author of `xwkont:ref:dolce-borgo-2022`) as an explicit simplification of DLP — provides a directly fetchable, directly quotable primary source for the same `InformationObject`/`InformationEntity` apparatus. Treat DUL as citable evidence for "the DOLCE-driven Information Object lineage" generally; if DLP397.owl's own text is fetched in a future pass and differs in some detail, note the discrepancy rather than assuming identity.

## Rights and License Notes

Not verified in this pass. Treat as unknown rather than guessed.

## Citation and Locator Notes

Recommended citation: Gangemi, A. *DOLCE+DnS Ultralite (DUL)*. OWL ontology. Ontology Design Patterns. <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl>.

**Directly verified 2026-07-01** by fetching the OWL/Turtle source directly (plain-text RDF, no PDF-extraction workaround needed) and grepping for the relevant class definitions.

Key findings used in `docs/crosswalks/concepts/information-artifact.md`:
- `InformationEntity rdfs:subClassOf Entity`, comment: "A piece of information, be it concretely realized or not. It is a catchall class, intended to bypass the ambiguities of many data or text that could denote either a an expression or a concrete realization of that expression."
- `InformationObject rdfs:subClassOf InformationEntity, SocialObject`, `owl:disjointWith SocialAgent`, comment: "A piece of information, such as a musical composition, a text, a word, a picture, independently from how it is concretely realized."
- `InformationRealization rdfs:subClassOf InformationEntity` and the union of `Event`, `PhysicalObject`, `Quality` — the concrete-realization counterpart to the abstract `InformationObject`, connected via the `realizes` relation.

This confirms the crosswalk's paraphrase that "Information Object... [is a] subclass of Social Object, itself a subclass of Non-Physical Object" is broadly right in spirit (generic dependence, non-physical/social classification) but imprecise in the exact class-name chain — DUL's actual hierarchy is `InformationObject` → `InformationEntity` (and separately `SocialObject`), not through a class literally named "Non-Physical Object."
