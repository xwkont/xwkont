# XwkOnt Editorial Policy

## Purpose

This document defines how XwkOnt documents, cites, compares, and maintains information.

## Guiding Principle

XwkOnt does not reinvent foundational ontologies.

XwkOnt documents, compares, and connects them.

## Vocabulary

XwkOnt introduces as little project-specific terminology as possible.

General English terms should use established dictionary meanings.

Project-specific terms are defined only when necessary.

## References

Every external reference SHALL include:

- Title
- Publisher
- URL
- Accessed (UTC)
- Version/Edition (if available)
- License (if known)
- A stable citation per `ADR-0012`: a DOI when the work has one, or a timestamped archival snapshot (e.g., Internet Archive Wayback Machine, implementing the Memento Protocol/RFC 7089) for web content without a DOI. Never fabricate a snapshot; record it as unverified rather than guessed.

The live URL remains the authoritative source for retrieving current content, but is not sufficient on its own for verifying what was originally cited — see `ADR-0012`.

## Reference Records

References are treated as reusable repository artifacts.

Each reference receives a stable identifier and metadata record.

Concept pages reference Reference IDs rather than duplicating metadata.

## Copyright

- Link to official sources.
- Cite official sources.
- Record metadata.
- Prefer original XwkOnt commentary.
- Do not reproduce copyrighted works except where permitted by license or applicable law.

## Traceability

Every mapping should be traceable to one or more authoritative references.

## Open-World Philosophy

XwkOnt assumes knowledge evolves.

New ontologies, references, mappings, and concepts can be incorporated without changing the project's core philosophy.

## Future Work

A future Reference Registry will maintain versioned metadata for all external references used throughout XwkOnt.