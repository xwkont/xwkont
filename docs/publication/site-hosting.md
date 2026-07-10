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

## Relationship to w3id

Current live HTML negotiation for `https://w3id.org/xwkont/core` still targets the GitHub blob view of `docs/ontology/core-ontology.md`. After Pages is verified live, maintainers SHOULD update the external w3id HTML target to the corresponding Pages URL (for example `https://xwkont.github.io/xwkont/ontology/core-ontology/`) while leaving Turtle negotiation pointed at `core.ttl`.

That w3id HTML retarget is a separate `perma-id/w3id.org` change and is **not** performed by this repository's Pages workflow.

## Non-goals

- Custom web application or CMS
- Moving editorial SSOT out of Git
- Activating immutable versioned ontology document IRIs (still deferred)
- Replacing machine-readable exports under `data/crosswalks/`
