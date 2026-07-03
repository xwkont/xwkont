# XwkOnt Architectural Principles

## Purpose

This document defines the architectural principles that govern XwkOnt.

These principles take precedence over implementation details.

---

# Principle 1 — Reuse Established Standards

XwkOnt adopts established standards, specifications, and accepted practices whenever they satisfy the project's requirements.

Project-specific conventions are introduced only when no suitable standard exists.

Decision order:

1. Reuse
2. Reference
3. Adapt
4. Introduce

---

# Principle 2 — Everything Has Provenance

Every significant artifact shall identify its origin.

Possible provenance classifications:

- Adopted
- Adapted
- Referenced
- Introduced

Introduced artifacts should include a rationale.

---

# Principle 3 — Concept-Centric

XwkOnt is organized around concepts rather than ontologies.

Concepts are the primary means by which users navigate and compare foundational ontologies.

See `docs/adr/ADR-0011-adapt-iso-1087-concept-as-organizing-unit.md` for why "Concept" (not "Term," "Class," "Universal," or "primitive") is the correct organizing-unit label.

---

# Principle 4 — Source First

Authoritative sources remain authoritative.

XwkOnt links to, cites, and compares them.

---

# Principle 5 — Traceability

Definitions, mappings, and comparisons should always be traceable to authoritative references.

---

# Principle 6 — Neutrality

XwkOnt documents and compares.

It does not advocate or replace existing foundational ontologies.

---

# Principle 7 — Open-World Philosophy

The project assumes knowledge evolves.

New ontologies, concepts, references, and mappings can be incorporated without changing these principles.

---

# Future Work

Before introducing any project-specific structure, XwkOnt will evaluate existing standards for possible adoption, including metadata, identifiers, provenance, citations, and terminology.