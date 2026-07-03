# Meta-Ontology and Mapping Standards Evaluation

> **Status:** Discovery finding, not an adoption decision (dispositions below are recommendations)
> **Date:** 2026-07-01
> **Trigger:** Follow-up from `docs/evaluations/prior-art-survey.md` and a removed scratch note that first raised these candidates. Runs the existing standards-discovery evaluation process (`docs/STANDARDS_BASELINE.md` disposition vocabulary) against standards relevant to how XwkOnt represents ontologies, ontology metadata, and ontology-to-ontology mappings — not source-ontology content itself.

## Purpose

This is a standards evaluation, not a concept crosswalk. It uses the disposition vocabulary already defined in `docs/STANDARDS_BASELINE.md` (`Adopt`/`Adapt`/`Reference`/`Defer`/`Reject`) rather than the concept-crosswalk methodology (`docs/methodology/crosswalk-methodology.md`), which is reserved for comparing how source ontologies (BFO, DOLCE, SUMO, UFO) treat a shared concept. Applying the crosswalk template to standards like MOF or Common Logic would conflate two different artifact types; this document keeps them separate.

Provenance classification: **Referenced** for every standard below, per the same rule `docs/evaluations/standards-survey-report.md` used at its discovery stage — these are external authoritative materials under evaluation, not yet adopted by this document.

## Candidates Evaluated

### MOF (Meta Object Facility, OMG standard)

Defines a four-layer meta-modeling architecture (M3/M2/M1/M0) used to define metamodels such as UML and ODM.

**Recommended disposition: Reference.** XwkOnt's artifacts are direct RDF/RDFS/SKOS Turtle plus Markdown; there is no MOF-based modeling tool in XwkOnt's toolchain and no plan to introduce one. MOF is useful background for understanding ODM's foundation, not a current requirement.

### ODM (Ontology Definition Metamodel, OMG standard)

A MOF-based metamodel bridging UML/MDA tooling and OWL/RDFS ontology representation.

**Recommended disposition: Reference.** XwkOnt does not use UML-based ontology modeling tools; `data/ontology/core.ttl` is authored directly in Turtle. Adopting ODM would introduce a modeling layer XwkOnt doesn't need.

### DOL (Distributed Ontology Language, ISO/IEC 17347, OntoIOp)

A meta-level language for expressing heterogeneous ontologies (formalized in OWL, Common Logic, or other logics), modules, and formal links between them — imports, alignments, conservative extensions, and theory interpretations with provable semantics.

**Recommended disposition: Reference.** DOL is conceptually the closest of these candidates to "crosswalk" in spirit — it formally expresses links between ontologies in different logics. But it requires formalizing source ontologies in OWL or Common Logic and proving theory interpretations, which is a different and much heavier undertaking than XwkOnt's current scope (conservative RDF/RDFS/SKOS, `ADR-0004`'s explicit deferral of OWL as a default modeling layer). This is the kind of formal-verification work COLORE does (see `docs/evaluations/prior-art-survey.md`), not what XwkOnt's human-readable, citation-first crosswalk is for. Worth citing as related art in future crosswalk documents; not adopted.

### Common Logic (ISO/IEC 24707)

First-order logic standard; one of the logics DOL can build on.

**Recommended disposition: Reference.** Same rationale as `ADR-0004`'s existing OWL disposition, one level heavier (full first-order logic rather than description logic). Consistent with XwkOnt's repeated, deliberate choice not to adopt a formal logic layer.

### OMV (Ontology Metadata Vocabulary)

A modular vocabulary (OMV Core + extensions) specifically for describing ontologies and related entities: 16 classes, 33 object properties, 29 data properties, covering identification, provenance, engineering methodology, and — via extensions — mappings and evaluation metadata.

**Recommended disposition: Defer.** `ADR-0003` already adopted DCMI terms as the baseline descriptive metadata vocabulary for references. OMV is more specific to describing *ontologies themselves* (e.g., BFO, DOLCE, SUMO, UFO as artifacts — ontology language, engineering methodology, version) than DCMI is, and could be a good fit once XwkOnt needs structured metadata records about the four source ontologies rather than freeform prose citations. That need doesn't exist yet — defer until the first concept crosswalks (Object, Event) reveal whether DCMI-based reference records are sufficient or whether OMV's ontology-specific fields are actually needed.

### VoID (Vocabulary of Interlinked Datasets, W3C Note)

Vocabulary for describing RDF datasets: linksets, statistics, access endpoints.

**Recommended disposition: Reference.** XwkOnt's Turtle artifact is one small vocabulary file, not a dataset requiring linkset/statistics description. Relevant only if XwkOnt later produces multiple interlinked machine-readable crosswalk exports — explicitly deferred per `docs/INFORMATION_ARCHITECTURE.md`'s "Machine-Readable Companion Decision." Not needed now.

### SSSOM (Simple Standard for Sharing Ontological Mappings)

Already flagged in `docs/evaluations/prior-art-survey.md` as the standard most likely to overlap with `ADR-0007`'s bespoke `xwkont:mapping:<concept-slug>:<nnn>` scheme. Mature, actively maintained, provides a predicate vocabulary, confidence model, and mapping-set metadata (justification, provenance, mapping tool/date).

**Recommended disposition: Adapt.** XwkOnt's mapping content is currently human-readable Markdown, not machine-readable SSSOM TSV — a full `Adopt` (committing to SSSOM's exact serialization now) would be premature before any real mapping content exists. But SSSOM's *predicate vocabulary and confidence/provenance model* are a better fit than inventing project-specific categories from scratch, and reusing them satisfies "Reuse Before Introduce" more directly than the current `docs/methodology/crosswalk-methodology.md` category list. This is a governance/representation-level change to `ADR-0007` and needs its own ADR before it's final — this document recommends the disposition but does not implement it.

## Updated Disposition Summary

| Standard | Disposition | Decision record |
|---|---|---|
| MOF | Reference | This evaluation |
| ODM | Reference | This evaluation |
| DOL | Reference | This evaluation |
| Common Logic | Reference | This evaluation |
| OMV | Defer | This evaluation |
| VoID | Reference | This evaluation |
| SSSOM | Adapt (recommended; pending ADR) | This evaluation; ADR required before final |

## Deferred Questions

1. Should `ADR-0007` be amended (or superseded) to adapt SSSOM's predicate/confidence/provenance model for mapping assertions? This is the one actionable decision from this evaluation and needs explicit sign-off before implementation, since it changes an existing accepted ADR's representation policy.
2. ~~Should OMV be revisited once the first concept crosswalks reveal whether DCMI-based reference records adequately describe BFO/DOLCE/SUMO/UFO as source ontologies?~~ **Revisited and closed, 2026-07-03 — disposition remains Defer.** All 8 concept crosswalks are now `reviewed` and all 16 `docs/references/ref-*.md` records (covering all 8 source ontologies, `ADR-0015`) use only DCMI-based fields plus freeform prose (Source Relation Notes, Rights and License Notes, Citation and Locator Notes). A scan of every reference record and crosswalk found exactly one incidental mention of an ontology-engineering-specific term ("OWL DL" in `ref-gum-owl.md`'s prose, describing a dead PURL, not a structured field), and no case where a DCMI field was insufficient to capture what a crosswalk needed to cite. No concrete need for OMV's ontology-specific structured fields (engineering methodology, expressivity, mapping/evaluation metadata classes) has materialized. Re-open only if XwkOnt begins producing structured per-source-ontology artifact records beyond `docs/references/ref-*.md`'s current prose-plus-DCMI-fields pattern — not expected under the current RDF/RDFS/SKOS-scaffold, documentation-first approach.
3. No disposition here is final. Per `docs/STANDARDS_BASELINE.md`'s convention, only an ADR makes a standards decision authoritative.
