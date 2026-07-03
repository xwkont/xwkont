# Security Policy

<!-- updated at: 2026-07-03 12:57 Z   (2026-07-03 08:57 EDT) -->

## Scope

XwkOnt is a documentation- and RDF-artifact-based project (Markdown and Turtle files); it has no build system, server, or deployed application in this repository. Most conventional application security concerns (injection, auth, etc.) do not apply directly to the repository content itself.

This policy covers two categories of report:

1. **Vulnerabilities in any executable code or tooling** added to this repository (validation scripts, generators — see [LICENSE-CODE](LICENSE-CODE) for scope). This now includes the [.github/workflows/validate.yml](.github/workflows/validate.yml) CI workflow.
2. **Integrity concerns with published content** — for example, a pull request or issue introducing content designed to mislead (falsified citations, fabricated source-ontology claims, or content intended to manipulate downstream tooling that consumes this repository's Markdown or Turtle files).

Content-quality issues that are not security-relevant (typos, disagreements about crosswalk interpretation, incomplete definitions) should be filed as regular issues per [docs/governance/contributing.md](docs/governance/contributing.md), not reported through this policy.

## Reporting a Vulnerability or Integrity Concern

Report privately using GitHub's private vulnerability reporting feature (repository **Security** tab → **Report a vulnerability**) rather than opening a public issue. Please include:

- A description of the concern and why it's security- or integrity-relevant.
- The affected file(s) or artifact(s).
- Any suggested remediation.

You should expect an initial response within a reasonable time. Confirmed issues will be addressed following the project's repository-first governance process ([docs/governance/governance.md](docs/governance/governance.md)) and, if the fix changes accepted publication artifacts, the change-management policy ([docs/governance/change-management.md](docs/governance/change-management.md)).

## Supported Scope

The first tagged release, `ontology-core-v0.1.0`, is now published (see [docs/publication/release-tagging-checklist.md](docs/publication/release-tagging-checklist.md)). The release/versioning policy ([docs/governance/release-versioning-policy.md](docs/governance/release-versioning-policy.md)) governs which tagged versions remain supported; absent a later tag deprecating it, the current default branch and the latest tagged release are both supported.
