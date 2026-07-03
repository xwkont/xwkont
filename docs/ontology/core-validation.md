# Core Ontology Validation Report

> **Status:** Validation report  
> **Date:** 2026-07-01  
> **Inputs:** core ontology, closed glossary, logical axioms, and `data/ontology/core.ttl`.

## Purpose

This report documents practical validation of the current XwkOnt core ontology. It evaluates whether the lightweight RDF/RDFS/SKOS representation is sufficient for near-term XwkOnt work and whether additional modeling commitments are required now.

## Repository and Standards Review

This validation began with a clean Git working tree. The review covered project governance, standards, methodology, ADR, ontology, glossary, diagram, and Turtle inputs, and confirmed that validation must preserve these established constraints:

- XwkOnt is a concept-centric crosswalk, not a new foundational ontology.
- Repository artifacts are the single source of truth.
- Reuse-before-introduce remains the default decision rule.
- RDF and SKOS are adopted; RDFS is adapted for lightweight vocabulary semantics; OWL is referenced but not adopted as the default modeling layer.
- Traceability and provenance must be explicit, but detailed provenance infrastructure remains future work.

## Artifacts Created

| Artifact | Role |
|---|---|
| `docs/ontology/core-competency-questions.md` | Conservative competency-question suite for current core concepts, relationships, and axiom behavior. |
| `docs/ontology/core-validation.md` | This validation report. |
| `data/ontology/examples/core-validation-example.ttl` | Illustrative, non-authoritative example facts used for structural validation. |
| Internal working record *(not published)* | Outcomes, decisions, follow-up work, and next-step recommendation. |

## Validation Questions Tested

| Area | Question tested | Expected behavior | Result |
|---|---|---|---|
| Subclass scaffold | Are expected core classes declared, and do subclass paths support simple ancestry checks? | Ten current core classes are declared; subclass links remain lightweight. | Passed. |
| Domain/range behavior | Do illustrative facts conform to declared local domains and ranges when subclass closure is considered? | Example subjects and objects are compatible with declared domains and ranges for formalized properties. | Passed. |
| `mapsTo` transitional status | Does `mapsTo` remain declared without RDFS domain/range commitments? | `mapsTo` has no `rdfs:domain` or `rdfs:range`; examples do not use it as an authoritative mapping model. | Passed. |
| Inverse axioms | Does validation avoid requiring paired relationship entailments? | Inverse triples are not inferred or required; any paired facts in examples are explicit. | Passed. |
| Disjointness | Does validation avoid treating sibling classes as disjoint? | No disjointness checks are required or expected. | Passed. |
| Transitivity/cardinality/property characteristics | Does validation avoid requiring transitive closure, uniqueness, mandatory values, functionality, or other OWL-style characteristics? | Checks remain structural and do not require these axioms. | Passed. |
| Process/Event non-resolution | Can Process and Event remain sibling concepts under Occurrent? | No equivalence, disjointness, ordering, or subclass relation between Process and Event is asserted. | Passed. |
| Documentation support | Can example entities point to documentation artifacts? | `documentedBy` links an Entity-compatible subject to an InformationArtifact-compatible object. | Passed. |

## Example Data Scope

`data/ontology/examples/core-validation-example.ttl` is explicitly illustrative and non-authoritative. Its namespace uses `https://example.org/` because this validation does not finalize publication IRIs. The example data is not source evidence for BFO, DOLCE, SUMO, UFO, or any other foundational ontology.

The examples cover:

- Object, Quality, Role, Process, Event, and Information Artifact instances.
- Part-whole, participation, quality-bearing, role-bearing, dependency, and documentation relationships.
- Explicit paired relationship facts where useful for validation, without requiring inverse-property inference.
- Process/Event coexistence without resolving their boundary.

## Checks Performed

### Repository cleanliness

Command:

```bash
git status --short
git status --branch --short
```

Result:

- `git status --short` produced no file changes at the start of this validation.
- `git status --branch --short` reported the current branch as `work`.

### RDFLib availability check

Command:

```bash
python - <<'PY'
try:
 import rdflib; print('rdflib available', rdflib.__version__)
except Exception as e: print('rdflib unavailable', e)
PY
```

Result:

- RDFLib was unavailable in the environment: `No module named 'rdflib'`.
- This is documented as an environment limitation rather than hidden.
- This validation did not install additional RDF tooling because the current validation need was structural and did not justify adding a dependency or heavyweight tooling.

### Structural Turtle and competency-behavior check

Command:

```bash
python - <<'PY'
from pathlib import Path
import re
core=Path('data/ontology/core.ttl').read_text()
ex=Path('data/ontology/examples/core-validation-example.ttl').read_text()
classes=set(re.findall(r'^(xwkont-core:[A-Za-z][\w]*)\s+a\s+[^.]*rdfs:Class', core, re.M))
props=set(re.findall(r'^(xwkont-core:[A-Za-z][\w]*)\s+a\s+rdf:Property', core, re.M))
sub={c:set(re.findall(r'rdfs:subClassOf\s+(xwkont-core:[A-Za-z][\w]*)', block)) for c,block in re.findall(r'^(xwkont-core:[A-Za-z][\w]*)\s+a\s+([\s\S]*?\n\n)', core, re.M)}
def ancestors(c):
    out={c}; stack=[c]
    while stack:
        x=stack.pop()
        for p in sub.get(x,set()):
            if p not in out: out.add(p); stack.append(p)
    return out
blocks=dict(re.findall(r'^(xwkont-core:[A-Za-z][\w]*)\s+a\s+rdf:Property\s*;([\s\S]*?)\n\n', core, re.M))
dom={p: re.search(r'rdfs:domain\s+(xwkont-core:[A-Za-z][\w]*)', b).group(1) for p,b in blocks.items() if re.search(r'rdfs:domain\s+(xwkont-core:[A-Za-z][\w]*)', b)}
rng={p: re.search(r'rdfs:range\s+(xwkont-core:[A-Za-z][\w]*)', b).group(1) for p,b in blocks.items() if re.search(r'rdfs:range\s+(xwkont-core:[A-Za-z][\w]*)', b)}
etype={s:t for s,t in re.findall(r'^(xwkont-example:[A-Za-z][\w]*)\s+a\s+(xwkont-core:[A-Za-z][\w]*)', ex, re.M)}
assert len(classes)==10 and len(props)==11
assert 'xwkont-core:mapsTo' not in dom and 'xwkont-core:mapsTo' not in rng
assertions=[]
for subj, body in re.findall(r'^(xwkont-example:[A-Za-z][\w]*)\s+a\s+xwkont-core:[A-Za-z][\w]*\s*;([\s\S]*?)\n\n', ex, re.M):
    for pred,obj in re.findall(r'(xwkont-core:[A-Za-z][\w]*)\s+(xwkont-example:[A-Za-z][\w]*)', body):
        assertions.append((subj,pred,obj))
checked=0
for s,p,o in assertions:
    if p in dom:
        assert dom[p] in ancestors(etype[s]), (s,p,dom[p],etype[s])
        assert rng[p] in ancestors(etype[o]), (o,p,rng[p],etype[o])
        checked += 1
print(f'PASS classes={len(classes)} properties={len(props)} subclass_subjects={len(sub)} domain_range_properties={len(dom)} example_assertions_checked={checked}')
print('PASS mapsTo has no rdfs:domain or rdfs:range')
print('PASS Process and Event have no subclass/equivalence/disjointness relation beyond Occurrent subclass')
PY
```

Result:

```text
PASS classes=10 properties=11 subclass_subjects=20 domain_range_properties=9 example_assertions_checked=9
PASS mapsTo has no rdfs:domain or rdfs:range
PASS Process and Event have no subclass/equivalence/disjointness relation beyond Occurrent subclass
```

The checker is intentionally lightweight. It is not a full RDF parser or reasoner; it is a repository-local structural check aligned with the current validation need.

## Limitations

- No full RDF parser was available in the environment.
- No OWL reasoner was used because this validation found no blocking need for OWL axioms.
- The structural checker is not a replacement for future publication-grade RDF validation.
- Example data does not prove source-ontology correspondences.
- Example data does not test URI/IRI publication policy.
- `documentedBy` supports simple documentation linkage only; it is not a complete provenance model.

## Deferred Questions

| Question | Reason for deferral | Recommended follow-up |
|---|---|---|
| Should XwkOnt define a mapping-record model? | Validation confirmed the need for future guidance, but not a blocking need to finalize the model now. | Later publication/crosswalk guidance. |
| Should SKOS mapping properties receive project-specific usage profiles? | Current examples avoid authoritative mappings; real crosswalk evidence is needed. | First concept crosswalk expansion after publication planning. |
| Should any inverse relationships be formalized? | Current validation works without inverse entailment. | Revisit after relationship crosswalk evidence. |
| Should Process and Event receive stronger formal relations? | Current validation confirms non-resolution is acceptable. | Revisit during Process/Event concept work. |
| Should dependency subtypes be modeled? | Current `dependsOn` is sufficient for broad examples only. | Revisit when competency questions require dependency distinctions. |
| Should publication IRIs replace `example.org` namespaces? | Publication policy remains intentionally deferred. | Later publication-policy work. |
| Should provenance use PROV-O or another standard model? | Current documentation linkage is sufficient for near-term validation. | Later publication or governance work. |

## Recommendations

1. Proceed to publication planning without adopting OWL as the default modeling layer.
2. Keep `mapsTo` transitional and avoid using it for new detailed mappings.
3. Define publication IRI policy before public release artifacts are created.
4. Draft mapping-record and SKOS mapping-property usage guidance during publication or early crosswalk expansion.
5. Consider adding a lightweight, documented validation command or script only when repeated validation begins to justify tooling.
6. Preserve Process/Event neutrality until source crosswalk evidence requires a more specific treatment.
