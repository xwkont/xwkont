# XwkOnt Release and Versioning Policy

> **Status:** Repository-first governance baseline  
> **Date:** 2026-07-01 (tag-immutability rule added 2026-07-10 after the `ontology-core-v0.3.1` retraction)  
> **Scope:** Release tagging, versioning posture, tag immutability, and immutable ontology document IRI decision

## Purpose

This policy defines how XwkOnt should mark ontology milestones after the first publication package and records the governance decision on immutable versioned ontology document IRIs.

## Release Model

XwkOnt uses repository-first milestone releases. A release milestone is a reviewed repository state that identifies a coherent set of artifacts, validation results, known limitations, and follow-up work.

Release milestones should include:

- release notes;
- validation command results;
- relevant internal working record;
- changed artifact list;
- compatibility notes;
- known limitations and deferred questions.

## Tagging Expectations

Ontology milestones should be tagged after the repository state is accepted for publication.

Recommended tag pattern:

```text
ontology-core-vMAJOR.MINOR.PATCH
```

Examples:

```text
ontology-core-v0.1.0
ontology-core-v0.2.0
ontology-core-v1.0.0
```

Pre-release review tags may use a suffix when needed:

```text
ontology-core-v0.1.0-rc.1
```

A historical governance milestone tag candidate remains for early repository history, but future ontology releases should use ontology-specific milestone tags.

## Tag Immutability

**Published release tags are immutable.** Once a tag matching `ontology-core-vMAJOR.MINOR.PATCH` has been pushed to the public repository (or otherwise announced as a release), it MUST NOT be moved, force-updated, or deleted.

If a tagged release is incomplete, incorrect, or undersells in-flight work that belonged in that same milestone:

1. Prefer cutting a **new** tag (`PATCH` for corrections/clarifications; `MINOR` when scope actually expands) that supersedes the prior one.
2. Document the supersession in `CHANGELOG.md` and release notes, naming both tags and the reason.
3. Do **not** delete or retarget the prior tag after it has been published.

### Exception record: `ontology-core-v0.3.1` (2026-07-08)

On 2026-07-08, `ontology-core-v0.3.1` was tagged and then retracted the same day; `ontology-core-v0.3.0` was force-moved to a consolidated commit. That sequence is recorded in `CHANGELOG.md` and is the **only** accepted historical exception. It is not a precedent for future releases. This section exists so the next incomplete cut becomes a new tag, not another retag.

## Version Number Meaning

Until a `1.0.0` ontology milestone is accepted, version numbers are pre-1.0 project milestones and should be interpreted conservatively.

| Segment | Meaning before `1.0.0` | Meaning after `1.0.0` |
|---|---|---|
| MAJOR | Major milestone reset or incompatible public posture change. | Incompatible change to accepted public artifacts. |
| MINOR | New terms, mapping structures, publication capabilities, or reviewed crosswalk scope. | Backward-compatible additions or substantial non-breaking expansions. |
| PATCH | Corrections, clarifications, validation fixes, or non-semantic updates. | Backward-compatible fixes and clarifications. |

## Source Ontology Version Re-check Cadence

XwkOnt's own release versioning (above) is independent of each source ontology's (BFO, DOLCE, SUMO, UFO, GFO, YAMATO, TUpper, GUM) release cadence. XwkOnt does not track source ontologies' own version history and does not commit to updating a crosswalk every time a cited source ontology publishes a new release.

Once a year, the cited version of each of the eight source ontologies (as recorded in each crosswalk's Source Ontology Correspondence table and the corresponding `docs/references/ref-*.md` record) should be checked against that ontology's current published version. The outcome — no change, or a newer version now exists — should be recorded in a session journal entry; a version mismatch found this way is a trigger to evaluate whether the affected crosswalk needs re-verification, not an automatic obligation to re-verify immediately.

## Immutable Versioned Ontology Document IRI Decision

This policy defers minting immutable versioned ontology document IRIs.

The deferral is intentional. XwkOnt has a target current namespace, but it does not yet have the operational prerequisites needed to publish immutable versioned ontology documents without implying stronger public stability than the repository currently provides.

### Current Namespace

The current core namespace remains:

```text
https://w3id.org/xwkont/core#
```

This namespace identifies current core terms, not an immutable version snapshot.

### Future Versioned Document IRI Pattern

When prerequisites are complete, versioned ontology document IRIs should use this reserved pattern unless a later ADR changes it:

```text
https://w3id.org/xwkont/ontology/core/MAJOR.MINOR.PATCH
```

The hash term namespace for a versioned distribution may be documented as the ontology document plus fragment identifiers, for example:

```text
https://w3id.org/xwkont/ontology/core/0.1.0#Entity
```

This pattern is reserved guidance, not an active publication claim.

### Prerequisites Before Activation

Immutable versioned ontology document IRIs must not be advertised as active until all of the following exist:

1. An accepted release tag using the ontology milestone tag pattern.
2. A release artifact or repository path that exactly corresponds to the tagged Turtle file and documentation bundle.
3. Configured `w3id.org` redirects for the current namespace and versioned document path.
4. Documented content-negotiation or redirect behavior for HTML and Turtle retrieval.
5. Release notes that identify the immutable document IRI and tag.
6. Validation results for the tagged artifacts.

Activating immutable versioned ontology document IRIs after these prerequisites are met is an implementation of this policy. Changing the pattern or meaning requires ADR review.

## Current Release State

Tagged milestones through `ontology-core-v0.3.2` are published (`0.3.1` was retracted and is not a live tag). Immutable versioned ontology document IRIs remain deferred until the prerequisites above are met. Future incomplete cuts must follow the Tag Immutability rule (new tag + CHANGELOG supersession), not tag deletion or retargeting.

## Deprecation and Supersession

Future releases may deprecate terms, examples, or documentation sections. Deprecation should preserve historical records and explain migration guidance. Removal from current documentation should not erase release history.
