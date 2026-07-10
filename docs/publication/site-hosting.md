# Public Site Hosting (GitHub Pages)

> **Status:** Accepted operational posture  
> **Date:** 2026-07-10  
> **Scope:** Human-readable public documentation site for XwkOnt

## Decision

XwkOnt publishes a static documentation site with **Material for MkDocs** on **GitHub Pages**.

| Layer | Role |
|---|---|
| Git repository | Single source of truth (Markdown, YAML, Turtle) |
| GitHub Pages (`https://xwkont.github.io/xwkont/`) | Human-readable documentation site |
| `w3id.org/xwkont/` | Persistent identifiers and content negotiation |
| `raw.githubusercontent.com` (via w3id) | Turtle retrieval for `core.ttl` |

The site is a **projection** of repository docs. It does not become a second editorial SSOT.

## Build and deploy

- Config: [`mkdocs.yml`](https://github.com/xwkont/xwkont/blob/main/mkdocs.yml) (repository root)
- Python deps: [`requirements-docs.txt`](https://github.com/xwkont/xwkont/blob/main/requirements-docs.txt)
- Workflow: [`.github/workflows/pages.yml`](https://github.com/xwkont/xwkont/blob/main/.github/workflows/pages.yml)
- Trigger: push to `main`, plus manual `workflow_dispatch`
- Local preview: `pip install -r requirements-docs.txt && mkdocs serve`
- Public URL: [https://xwkont.github.io/xwkont/](https://xwkont.github.io/xwkont/)

## Repository settings required once

In GitHub → **Settings → Pages**:

1. Source: **GitHub Actions**
2. Confirm the first successful `pages.yml` run publishes the site

No `gh-pages` branch is used.

## Relationship to Explore visualizations

The [Explore](../explore/index.md) section renders interactive coverage and mapping views from JSON generated at build time (`scripts/generate-explore-data.py`). Those views are projections only; they do not replace Markdown/YAML editorial artifacts.

## Relationship to w3id

HTML negotiation for `https://w3id.org/xwkont/` and `https://w3id.org/xwkont/core` is retargeted to this Pages site via `perma-id/w3id.org#6343` (pending merge as of 2026-07-10):

| Request | Target after `#6343` |
|---|---|
| `https://w3id.org/xwkont/` | `https://xwkont.github.io/xwkont/` |
| `https://w3id.org/xwkont/core` (`Accept: text/html` / default) | `https://xwkont.github.io/xwkont/ontology/core-ontology/` |
| `https://w3id.org/xwkont/core` (`Accept: text/turtle`) | raw `core.ttl` (unchanged) |

See [w3id-redirect-request.md](w3id-redirect-request.md) for the Apache fragment and verification commands. Turtle negotiation remains on `raw.githubusercontent.com`.


## Non-goals

- Custom web application or CMS
- Moving editorial SSOT out of Git
- Activating immutable versioned ontology document IRIs (still deferred)
- Replacing machine-readable exports under `data/crosswalks/`
