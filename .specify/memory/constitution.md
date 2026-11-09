<!--
Sync Impact Report
==================
Version change: (unratified scaffold) → 1.0.0
Bump rationale: Initial ratification. The previous file contained only unresolved template
placeholders and no adopted governance, so this is a MAJOR-equivalent first adoption rather
than an amendment of prior rules.

Modified principles:
- N/A (all principles newly ratified)

Added principles:
- I. AI-First Document Understanding
- II. Evidence-Based Information
- III. Historical Integrity
- IV. Deterministic Domain Logic
- V. Explicit Uncertainty
- VI. Modular and Extensible Architecture
- VII. Idempotent and Reprocessable Pipelines
- VIII. Domain Accuracy
- IX. Testability and Quality
- X. Provider Independence

Added sections:
- Additional Constraints
- Development Workflow & Quality Gates
- Governance

Removed sections:
- None

Deferred TODOs:
- None
-->

# Concurso Intelligence Constitution

## Core Principles

### I. AI-First Document Understanding

Large language models MUST be the primary semantic interpretation layer for heterogeneous,
unstructured official documents. Document-specific parsers built on rigid formatting assumptions
are prohibited. Generic extraction, OCR, and document-processing tools MAY be used for text and
structure recovery, but semantic interpretation MUST be delegated to AI.

Rationale: Official publications vary across institutions, examination boards, and publication
eras. Format-aware parsers break on every layout change and encode brittle assumptions that are
hard to audit. AI interpretation generalizes across sources and makes semantic decisions
inspectable.

### II. Evidence-Based Information

Every extracted fact MUST be traceable to its original document and supporting evidence. Each
fact MUST retain source references, publication date, page reference, and the relevant text
excerpt. An AI inference MUST never be presented as an officially confirmed fact.

Rationale: Concurso outcomes carry legal and personal consequences. Traceability lets users
verify claims, supports audits, and separates what a document says from what the system
concludes.

### III. Historical Integrity

Official documents and extracted historical events MUST be preserved. New events MUST NOT
silently overwrite or erase previous events. Corrections, cancellations, revocations, and
invalidations MUST be represented as new historical events with explicit relationships to the
events they affect.

Rationale: A candidate's trajectory depends on the full sequence of official acts, including
those later annulled. Destructive updates would make past states unreconstructable and undermine
accountability.

### IV. Deterministic Domain Logic

LLMs are responsible for understanding documents, extracting information, and identifying
semantic relationships. Business rules, candidate ranking calculations, chronological ordering,
list progression, and distance-to-appointment calculations MUST be implemented as deterministic,
testable logic. Domain calculations MUST NOT depend on model output at runtime.

Rationale: Rankings and progression are rule-bound and contestable. They must produce identical
results for identical inputs and be explainable step by step.

### V. Explicit Uncertainty

The system MUST distinguish confirmed facts, inferred relationships, incomplete information, and
unresolved contradictions. Missing information MUST NOT be interpreted as proof that an event
did not happen.

Rationale: Absence of a document is not evidence of absence. Conflating "unknown" with "did not
occur" produces incorrect candidate histories and false conclusions.

### VI. Modular and Extensible Architecture

Document sources, AI providers, extraction workflows, domain logic, and presentation layers MUST
remain independent. Adding a new institution, examination board, or document source MUST NOT
require rewriting the core domain.

Rationale: The set of sources grows continuously and each source has its own publication habits.
Stable boundaries keep source-specific change from leaking into domain rules.

### VII. Idempotent and Reprocessable Pipelines

Document ingestion and processing MUST be safe to execute repeatedly. Duplicate documents and
events MUST be detected. Documents MUST be reprocessable when extraction strategies, models, or
schemas evolve, without losing historical records.

Rationale: Sources republish, retry, and revise content. Reprocessing is routine, so pipelines
must converge on the same state and must never discard earlier extraction results.

### VIII. Domain Accuracy

The domain model MUST maintain explicit distinctions between candidate classification, summons,
appointment, taking office, commencement of duties, withdrawal, absence, resignation, and
appointment invalidation. Candidate progression across different ranking lists MUST respect the
examination notice and applicable rules.

Rationale: These are legally distinct states with different consequences. Treating them as
interchangeable produces incorrect timelines and misleading appointment tracking.

### IX. Testability and Quality

Critical domain calculations MUST have automated tests. AI extraction MUST be evaluated against
manually validated reference documents, and the evaluation MUST measure precision, recall, false
positives, and false negatives.

Rationale: Deterministic logic earns trust through tests; AI extraction earns trust through
measured accuracy on representative, human-verified documents.

### X. Provider Independence

The domain model MUST NOT be coupled to a particular LLM provider, embedding model, or
orchestration framework. AI capabilities MUST be replaceable through well-defined interfaces.

Rationale: Model quality, cost, and availability change quickly. Interfaces keep provider
choices reversible and prevent lock-in from dictating domain design.

## Additional Constraints

- **Immutable source records**: Raw documents and their checksums MUST be stored unaltered.
  Derived extractions MUST reference the immutable source version they were produced from.
- **Extraction provenance**: Every extraction run MUST record the model, prompt or strategy
  version, extraction schema version, and timestamp used to produce it.
- **Schema evolution**: Extraction schemas MUST be versioned. Changing a schema MUST NOT mutate
  previously stored extraction results.
- **Audit trail**: All state changes to extracted events, relationships, and their review status
  MUST be attributable and time-stamped.
- **Personal data**: Data about candidates MUST be limited to what is publicly published in
  official documents and handled according to applicable data protection law.
- **Source respect**: Ingestion MUST honor source availability, rate limits, and terms of use,
  and MUST identify itself where required.

## Development Workflow & Quality Gates

- Every feature MUST begin with a specification that identifies which principles it touches and
  how compliance is demonstrated.
- Changes to domain calculations MUST include tests that cover boundary cases, cross-list
  progression, and correction/invalidation scenarios.
- Changes to extraction behavior MUST be validated against the maintained reference corpus before
  merge; precision, recall, false positives, and false negatives MUST be reported when they
  change materially.
- New document sources MUST be added through existing source interfaces and MUST NOT introduce
  source-specific branches in the core domain.
- Reviews MUST verify historical integrity: no destructive updates, no silent overwrites, and
  explicit relationships for corrections and invalidations.
- Architectural complexity MUST be justified against a simpler alternative; unnecessary
  abstraction is a review defect.
- Reprocessing and migration paths MUST be documented for any change that affects stored
  extraction results or derived domain events.

## Governance

This constitution supersedes conflicting practices, conventions, and prior decisions. All
features and technical decisions MUST comply with these principles.

**Amendment procedure**: Amendments MUST be proposed in writing, state the affected principles,
explain the motivation, and describe the migration impact on existing data and derived events.
An amendment takes effect only after explicit approval and MUST be recorded in the Sync Impact
Report for that change.

**Versioning policy**: The constitution follows semantic versioning.
- MAJOR: removal or backward-incompatible redefinition of a principle or governance rule.
- MINOR: addition of a principle or section, or materially expanded guidance.
- PATCH: clarifications, wording fixes, and non-semantic refinements.

**Compliance review**: Every change MUST be reviewed for compliance with the current version.
Any intentional deviation MUST be documented, justified, and time-bound. When guidance here is
insufficient, the specification artifacts under `.specify/` provide runtime development guidance.

**Version**: 1.0.0 | **Ratified**: 2026-11-09 | **Last Amended**: 2026-11-09
