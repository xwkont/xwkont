# Publication-Time Validation Commands

> **Status:** Publication validation guide  
> **Date:** 2026-07-01  
> **Scope:** Minimal checks for the current core ontology publication package

## Purpose

This document defines the minimal command set maintainers should run before publishing the current core ontology milestone. The commands intentionally validate the conservative RDF/RDFS/SKOS scaffold without requiring OWL reasoning or source-ontology commitments.

## Required Commands

Run commands from the repository root.

### 1. Confirm working tree state

```bash
git status --short
```

Expected result: no uncommitted changes for a final release check.

### 2. Parse Turtle artifacts when RDFLib is available

```bash
python - <<'PY'
from rdflib import Graph
for path in [
    'data/ontology/core.ttl',
    'data/ontology/examples/core-validation-example.ttl',
]:
    graph = Graph()
    graph.parse(path, format='turtle')
    print(f'{path}: {len(graph)} triples')
PY
```

Expected result: both Turtle files parse successfully and print triple counts. If RDFLib is unavailable, record the limitation and run the structural fallback command below.

### 3. Structural fallback without external dependencies

```bash
python - <<'PY'
from pathlib import Path
core = Path('data/ontology/core.ttl').read_text()
example = Path('data/ontology/examples/core-validation-example.ttl').read_text()
required_terms = [
    'xwkont-core:Entity', 'xwkont-core:Continuant', 'xwkont-core:Occurrent',
    'xwkont-core:Object', 'xwkont-core:Quality', 'xwkont-core:Role',
    'xwkont-core:Process', 'xwkont-core:Event', 'xwkont-core:Relation',
    'xwkont-core:InformationArtifact', 'xwkont-core:hasPart',
    'xwkont-core:partOf', 'xwkont-core:participatesIn',
    'xwkont-core:hasParticipant', 'xwkont-core:hasQuality',
    'xwkont-core:qualityOf', 'xwkont-core:bearsRole',
    'xwkont-core:roleOf', 'xwkont-core:dependsOn',
    'xwkont-core:mapsTo', 'xwkont-core:documentedBy',
    'xwkont-core:Abstract', 'xwkont-core:Concrete', 'xwkont-core:Universal',
    'xwkont-core:Time', 'xwkont-core:Space', 'xwkont-core:Aggregate',
    'xwkont-core:Sum', 'xwkont-core:Boundary', 'xwkont-core:Site',
    'xwkont-core:Quantity', 'xwkont-core:Proposition',
    'xwkont-core:Change', 'xwkont-core:Continuous', 'xwkont-core:Discrete',
    'xwkont-core:OntologicalLevelStratum', 'xwkont-core:ListSequence',
    'xwkont-core:MindConsciousBeingAgent', 'xwkont-core:NonPhysicalObject',
    'xwkont-core:Disposition', 'xwkont-core:Modality',
    'xwkont-core:SymbolSignRepresentation', 'xwkont-core:symbolizes',
    'xwkont-core:symbolizedBy', 'xwkont-core:SituationStateOfAffairs',
]
missing = [term for term in required_terms if term not in core]
if missing:
    raise SystemExit(f'Missing required core terms: {missing}')
if 'xwkont-core:mapsTo a rdf:Property ;\n    rdfs:domain' in core or 'xwkont-core:mapsTo a rdf:Property ;\n    rdfs:range' in core:
    raise SystemExit('mapsTo must not reintroduce formal RDFS domain or range commitments')
for token in ['https://w3id.org/xwkont/core#', 'https://w3id.org/xwkont/examples/core-validation#']:
    if token not in core + example:
        raise SystemExit(f'Missing publication namespace token: {token}')
print('Structural fallback validation passed')
PY
```

Expected result: `Structural fallback validation passed`.

### 4. Check navigation references

```bash
python - <<'PY'
from pathlib import Path
required_paths = [
    'docs/publication/core-publication-guide.md',
    'docs/publication/uri-iri-policy.md',
    'docs/publication/validation-commands.md',
    'docs/publication/publication-operations.md',
    'docs/publication/redirects-content-negotiation.md',
    'docs/publication/release-tagging-checklist.md',
    'docs/publication/w3id-redirect-request.md',
    'docs/releases/core-ontology-release-notes.md',
]
missing = [path for path in required_paths if not Path(path).exists()]
if missing:
    raise SystemExit(f'Missing publication artifacts: {missing}')
print('Publication navigation artifacts present')
PY
```

Expected result: `Publication navigation artifacts present`.

## Non-Required Checks

OWL reasoner validation is not required for this milestone because XwkOnt has not adopted OWL as the default modeling layer and the current artifacts avoid OWL axioms.

SPARQL competency-query automation is not required for this milestone. The competency questions remain documented checks rather than a required executable suite.
