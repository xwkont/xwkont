# w3id Redirect Implementation Request for XwkOnt

> **Status:** Live; HTML targets retargeted to GitHub Pages — submitted 2026-07-10 as `perma-id/w3id.org#6343` (pending merge); prior merges `#6277`, `#6292`
> **Date:** 2026-07-01 (HTML Pages retarget 2026-07-10)
> **Scope:** Minimal public redirects for the current XwkOnt core namespace

## Decision

Redirect configuration for `https://w3id.org/xwkont/` cannot be implemented directly in this repository unless this repository is the deployed `w3id.org` configuration repository or an infrastructure repository consumed by `w3id.org`.

The required implementation is an external change request against the `w3id.org` persistent identifier configuration infrastructure, normally the public `perma-id/w3id.org` repository. This file records the exact request that should be submitted and the verification commands to run after it is merged and deployed.

## Requested w3id Path

```text
/xwkont/
```

## Canonical Targets

| Target role | URL | Notes |
|---|---|---|
| Project landing page | `https://xwkont.github.io/xwkont/` | Public MkDocs site ([site-hosting.md](site-hosting.md)) |
| Default branch | `main` | Confirmed |
| Turtle artifact | `https://raw.githubusercontent.com/xwkont/xwkont/main/data/ontology/core.ttl` | Unchanged |
| HTML documentation | `https://xwkont.github.io/xwkont/ontology/core-ontology/` | Replaces GitHub blob view |

## Proposed Minimal Apache Configuration

The following `.htaccess` fragment is the intended external w3id configuration for `/xwkont/` (as submitted in `#6343`):

```apache
Options +FollowSymLinks
RewriteEngine On

# Project entry point: public documentation site.
RewriteRule ^$ https://xwkont.github.io/xwkont/ [R=302,L]

# Current core namespace document: Turtle representation.
RewriteCond %{HTTP_ACCEPT} text/turtle [OR]
RewriteCond %{HTTP_ACCEPT} application/x-turtle
RewriteRule ^core$ https://raw.githubusercontent.com/xwkont/xwkont/main/data/ontology/core.ttl [R=302,L]

# Current core namespace document: human-readable representation (GitHub Pages).
RewriteRule ^core$ https://xwkont.github.io/xwkont/ontology/core-ontology/ [R=302,L]
```

## Expected Behavior After Deployment

| IRI | Expected behavior |
|---|---|
| `https://w3id.org/xwkont/` | Redirects to `https://xwkont.github.io/xwkont/` |
| `https://w3id.org/xwkont/core` with `Accept: text/turtle` | Redirects to raw `core.ttl` |
| `https://w3id.org/xwkont/core` with `Accept: application/x-turtle` | Redirects to raw `core.ttl` |
| `https://w3id.org/xwkont/core` with `Accept: text/html` | Redirects to Pages core-ontology page |
| `https://w3id.org/xwkont/core` with no useful `Accept` header | Redirects to Pages core-ontology page |

## Post-Deployment Verification Commands

```bash
curl -I -L https://w3id.org/xwkont/
curl -I -L -H 'Accept: text/turtle' https://w3id.org/xwkont/core
curl -I -L -H 'Accept: application/x-turtle' https://w3id.org/xwkont/core
curl -I -L -H 'Accept: text/html' https://w3id.org/xwkont/core
curl -L -H 'Accept: text/turtle' https://w3id.org/xwkont/core | head
curl -L -H 'Accept: text/html' https://w3id.org/xwkont/core | head
```

## Non-Goals

This request does not:

- activate immutable versioned ontology document IRIs;
- create redirects for `https://w3id.org/xwkont/ontology/core/0.1.0` or any other versioned ontology document;
- introduce OWL as the default modeling layer;
- create source-ontology correspondences;
- treat illustrative example data as authoritative.

## Submission and Verification Status

| Change | PR | Status |
|---|---|---|
| Initial `/xwkont/` namespace | `perma-id/w3id.org#6277` | Merged |
| `/core` content negotiation (blob HTML + raw Turtle) | `perma-id/w3id.org#6292` | Merged; verified live 2026-07-03 |
| HTML retarget to GitHub Pages | `perma-id/w3id.org#6343` | Submitted 2026-07-10; pending merge |
