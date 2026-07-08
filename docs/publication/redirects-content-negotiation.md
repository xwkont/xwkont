# Redirects and Content Negotiation Policy

> **Status:** Deployed and verified live (`perma-id/w3id.org#6277`, `#6292`); re-verified 2026-07-08 — see Verification Result below  
> **Date:** 2026-07-01 (re-verified 2026-07-08)  
> **Scope:** Current XwkOnt core ontology namespace and first ontology milestone preparation

## Purpose

This document specifies the minimal public redirect and content-negotiation behavior needed before XwkOnt advertises dereferenceable public IRIs for the current core ontology namespace.

The behavior is intentionally small and practical. It does not activate immutable versioned ontology document IRIs.

## Decision Summary

| Question | Decision |
|---|---|
| Are public IRI redirects ready to specify? | Yes. Expected behavior is specified here, but deployment must still be configured and verified. |
| Is content negotiation ready to specify? | Yes. Minimal HTML/Turtle behavior is specified here, but deployment must still be configured and verified. |
| Should dereferenceability be advertised now? | No. It may be advertised only after deployed behavior is tested. |
| Are immutable versioned ontology document IRIs active? | No. They remain deferred. |

## Current Core Namespace

The current core term namespace is:

```text
https://w3id.org/xwkont/core#
```

Because it is a hash namespace, clients retrieve the namespace document at:

```text
https://w3id.org/xwkont/core
```

## Expected Retrieval Behavior

Requests to the current namespace document should support these outcomes:

| Request | Expected response |
|---|---|
| `GET https://w3id.org/xwkont/core` with `Accept: text/turtle` | Redirect or serve Turtle for `data/ontology/core.ttl`. |
| `GET https://w3id.org/xwkont/core` with `Accept: application/x-turtle` | Redirect or serve Turtle for `data/ontology/core.ttl`. |
| `GET https://w3id.org/xwkont/core` with `Accept: text/html` | Redirect or serve human-readable documentation for `docs/ontology/core-ontology.md` or the repository-rendered equivalent. |
| `GET https://w3id.org/xwkont/core` with no explicit useful `Accept` header | Prefer human-readable documentation. |

Redirects may point to repository-hosted raw Turtle and repository-rendered documentation while the project remains repository-first.

## Minimal w3id Configuration Expectation

The persistent base should be configured so that:

- `https://w3id.org/xwkont/core` resolves to current core ontology documentation or Turtle based on content negotiation.
- Fragment IRIs such as `https://w3id.org/xwkont/core#Entity` remain term IRIs and rely on retrieval of the fragmentless namespace document.
- `https://w3id.org/xwkont/` resolves to the project entry point or repository landing page.

Implementation should use the external request in `docs/publication/w3id-redirect-request.md` unless maintainers choose another w3id-supported mechanism. This repository has no active w3id deployment configuration of its own, so deployment ownership remains external to this repository.

## Non-Goals

This policy does not:

- create source-ontology correspondences;
- treat example data as authoritative;
- adopt OWL as the default modeling layer;
- define persistent IRIs for source ontology terms;
- activate immutable versioned ontology document IRIs;
- require a full web application or documentation site.

## Verification Commands

After redirects are deployed, maintainers should verify behavior with commands equivalent to:

```bash
curl -I -L -H 'Accept: text/turtle' https://w3id.org/xwkont/core
curl -I -L -H 'Accept: text/html' https://w3id.org/xwkont/core
curl -L -H 'Accept: text/turtle' https://w3id.org/xwkont/core | head
curl -L -H 'Accept: text/html' https://w3id.org/xwkont/core | head
```

Expected results:

- Turtle requests ultimately return Turtle content for the current `data/ontology/core.ttl` artifact.
- HTML requests ultimately return human-readable core ontology documentation.
- Redirect chains are stable enough to document in release notes.
- No versioned ontology document IRI is claimed unless the release-versioning prerequisites are complete.

## Verification Result

**Superseded — this section described the pre-deployment state.** An earlier attempt to check `https://w3id.org/xwkont/` and `https://w3id.org/xwkont/core` on 2026-07-01 returned `curl: (56) CONNECT tunnel failed, response 403` from that environment; a 2026-07-02 recheck found `https://w3id.org/xwkont/` live but `https://w3id.org/xwkont/core` still `404` pending the content-negotiation rules described above. Both gaps have since closed: `perma-id/w3id.org#6292` (merged 2026-07-03) added the `/core` content-negotiation rules, and `docs/releases/core-ontology-release-notes.md`'s "Content-Negotiation Verification" section recorded the 2026-07-03 verified-live result. This document's own status line above simply hadn't been updated to match — fixed 2026-07-08.

**Re-verified live, 2026-07-08** (this session, real `curl` against the deployed redirect, no changes needed):

- `curl -I -L -H 'Accept: text/turtle' https://w3id.org/xwkont/core` → `302` → `https://raw.githubusercontent.com/xwkont/xwkont/main/data/ontology/core.ttl` → final `200`.
- `curl -I -L -H 'Accept: text/html' https://w3id.org/xwkont/core` → `302` → `https://github.com/xwkont/xwkont/blob/main/docs/ontology/core-ontology.md` → final `200`.
- `curl -I -L https://w3id.org/xwkont/core#Entity` → same `302`/`200` as the fragmentless namespace document, confirming fragment IRIs resolve correctly.
- `curl -I -L https://w3id.org/xwkont/` → `302` → `https://github.com/xwkont` → final `200`.
- Served Turtle body's class count (`grep -c 'a owl:Class'`) matches `data/ontology/core.ttl`'s local count (30) exactly — the deployed content reflects the current `0.3.0`-era `core.ttl`, not a stale cached copy.
- `https://w3id.org/xwkont/ontology/core/0.1.0` (the immutable versioned document path) still returns `404`, consistent with "Blockers Before Advertising Dereferenceability" below — versioned IRIs remain correctly un-activated.

Full dereferenceability of the current (non-versioned) namespace is live and verified; only immutable versioned document IRIs remain deferred.

The implementation blockers are tracked in `docs/publication/w3id-redirect-request.md`: the canonical repository target must be confirmed by a maintainer, the redirect configuration must be submitted to external w3id infrastructure, and deployed behavior must be verified after deployment.

## Blockers Before Advertising Dereferenceability

XwkOnt must not advertise public dereferenceability until:

1. `w3id.org` redirect configuration is merged or otherwise deployed.
2. Turtle retrieval is verified.
3. HTML retrieval is verified.
4. Verification results are recorded in release notes.
5. The README and publication guide are updated from target-namespace language to verified-dereferenceability language.

All five are satisfied for the current (non-versioned) namespace as of the 2026-07-08 re-verification above. This does not extend to immutable versioned ontology document IRIs, which remain a separate, still-deferred decision (see `TODO.md`'s "Publication & Release" section).
