# w3id Redirect Implementation Request for XwkOnt

> **Status:** Maintainer-ready external implementation request; submitted 2026-07-02, `perma-id/w3id.org#6277` merged
> **Date:** 2026-07-01
> **Scope:** Minimal public redirects for the current XwkOnt core namespace

## Decision

Redirect configuration for `https://w3id.org/xwkont/` cannot be implemented directly in this repository unless this repository is the deployed `w3id.org` configuration repository or an infrastructure repository consumed by `w3id.org`.

The required implementation is an external change request against the `w3id.org` persistent identifier configuration infrastructure, normally the public `perma-id/w3id.org` repository. This file records the exact request that should be submitted and the verification commands to run after it is merged and deployed.

## Blocker

The local XwkOnt repository does not contain the active `w3id.org` Apache rewrite configuration, and no deployed project web endpoint was available to update from this repository. Therefore, XwkOnt must not advertise dereferenceability yet.

A maintainer must submit the redirect rules below to the external w3id configuration location and confirm the final repository landing-page URL used by the project. At the time this request was drafted, the canonical GitHub landing page could not be confirmed from local Git metadata because this checkout had no `origin` remote configured (`git remote get-url origin` reported no such remote). This checkout's `origin` remote is now configured to `https://github.com/xwkont/xwkont.git`, confirming the landing page and default-branch targets below — though as of this writing that URL still returns `404 Not Found`, so the repository itself has not yet been created or made public.

## Requested w3id Path

Create or update the external w3id path:

```text
/xwkont/
```

## Canonical Target Confirmation Status

The current maintainer-ready targets remain:

| Target role | Proposed URL | Confirmation state |
|---|---|---|
| Project landing page | `https://github.com/xwkont/xwkont` | Confirmed from this checkout's `origin` remote metadata. Repository still returns `404 Not Found` as of this writing — not yet created or not yet public. |
| Default branch | `main` | Confirmed from this checkout's local branch. |
| Turtle artifact | `https://raw.githubusercontent.com/xwkont/xwkont/main/data/ontology/core.ttl` | Target confirmed; not yet verified reachable since the repository is not yet public. |
| HTML documentation | `https://github.com/xwkont/xwkont/blob/main/docs/ontology/core-ontology.md` | Target confirmed; not yet verified reachable since the repository is not yet public. |

Exact maintainer question before submission or merge: **Is the canonical public repository `https://github.com/xwkont/xwkont`, and is `main` the default branch that should be used for w3id redirect targets?** If yes, use the configuration below unchanged. If no, replace only the repository owner/name and branch in the target URLs; keep the requested w3id scope limited to `/xwkont/` and `/xwkont/core`.

## Proposed Minimal Apache Configuration

The following `.htaccess` fragment is intended for the external w3id configuration directory for `/xwkont/`.

```apache
Options +FollowSymLinks
RewriteEngine On

# Project entry point.
RewriteRule ^$ https://github.com/xwkont/xwkont [R=302,L]

# Current core namespace document: Turtle representation.
RewriteCond %{HTTP_ACCEPT} text/turtle [OR]
RewriteCond %{HTTP_ACCEPT} application/x-turtle
RewriteRule ^core$ https://raw.githubusercontent.com/xwkont/xwkont/main/data/ontology/core.ttl [R=302,L]

# Current core namespace document: human-readable representation.
RewriteRule ^core$ https://github.com/xwkont/xwkont/blob/main/docs/ontology/core-ontology.md [R=302,L]
```

If the canonical GitHub organization, repository name, or default branch differs, replace the `github.com/xwkont/xwkont` and `raw.githubusercontent.com/xwkont/xwkont/main` targets before submission. Do not add versioned ontology document redirects in this request.

## Expected Behavior After Deployment

| IRI | Expected behavior |
|---|---|
| `https://w3id.org/xwkont/` | Redirects to the project entry point or repository landing page. |
| `https://w3id.org/xwkont/core` with `Accept: text/turtle` | Redirects to the current `data/ontology/core.ttl` Turtle artifact. |
| `https://w3id.org/xwkont/core` with `Accept: application/x-turtle` | Redirects to the current `data/ontology/core.ttl` Turtle artifact. |
| `https://w3id.org/xwkont/core` with `Accept: text/html` | Redirects to human-readable core ontology documentation. |
| `https://w3id.org/xwkont/core` with no useful `Accept` header | Redirects to human-readable core ontology documentation. |

## Post-Deployment Verification Commands

Run these commands after the external w3id change is merged and deployed:

```bash
curl -I -L https://w3id.org/xwkont/
curl -I -L -H 'Accept: text/turtle' https://w3id.org/xwkont/core
curl -I -L -H 'Accept: application/x-turtle' https://w3id.org/xwkont/core
curl -I -L -H 'Accept: text/html' https://w3id.org/xwkont/core
curl -L -H 'Accept: text/turtle' https://w3id.org/xwkont/core | head
curl -L -H 'Accept: text/html' https://w3id.org/xwkont/core | head
```

Record the redirect chain, final target URLs, content types, and any deployment limitations in the release notes before advertising dereferenceability or creating `ontology-core-v0.1.0`.

## Non-Goals

This request does not:

- activate immutable versioned ontology document IRIs;
- create redirects for `https://w3id.org/xwkont/ontology/core/0.1.0` or any other versioned ontology document;
- introduce OWL as the default modeling layer;
- create source-ontology correspondences;
- treat illustrative example data as authoritative.

## Submission and Verification Status

This request was not submitted from this environment when originally drafted; a maintainer subsequently submitted `perma-id/w3id.org#6277`, which has since been merged. Deployed redirect behavior is not yet verified from this environment — the post-deployment verification commands above still need to be run and their results recorded in `docs/releases/core-ontology-release-notes.md` before dereferenceability is advertised or `ontology-core-v0.1.0` is tagged.
