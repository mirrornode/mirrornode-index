<!--
CANON: MASTER (INTERNAL TECHNICAL/HISTORICAL REFERENCE)
Describes: recorded system state, capabilities, boundaries, roles, success criteria.
PUBLIC_CANON.md is derived from this file; derivation is not current verification.

Governance source: MIRRORNODE-CORE-HUB, as designated in its CANONICAL_SOURCES.md.
Pillars of ROTAN (Copilot Space Instructions) is a supporting behavioral reference;
this header grants it no cross-repository precedence.
This file does not override CORE-HUB governance or establish agent authority.
Preserve conflicting claims and escalate to the human Operator for disposition
within applicable review and security boundaries.
-->

# MIRRORNODE — Master Canon (v1.0)

## Authority and evidence boundary

This file is a technical/historical reference in the cross-repository index. [CORE-HUB's source mapping](https://github.com/mirrornode/MIRRORNODE-CORE-HUB/blob/aac3b5b473b12e3134224b316b6810de9a15f416/CANONICAL_SOURCES.md) designates MIRRORNODE-CORE-HUB as the governance source and this repository as the cross-repository index. The human Operator holds final conflict-disposition authority within applicable governance and security boundaries; this index cannot ratify policy, expand agent authority, or authorize execution or release.

The conflicting global-precedence header is preserved as historical evidence in prior blob `a24796659196239ddb980fca9e7b742864c2831d`. GOV-01 is tracked in [CORE-HUB PR #67](https://github.com/mirrornode/MIRRORNODE-CORE-HUB/pull/67); that proposal is not treated as merged or ratified here. GOV-01 remains open until the separate reviewed corrections receive the required dispositions, are merged, and are verified on their destination branches.

This authority correction does not re-verify the implementation, deployment, commerce, or snapshot claims below. Their historical verification labels do not establish current operational status. If evidence conflicts, retain both claims and seek an explicit Operator disposition rather than giving this file automatic precedence.

## What MIRRORNODE Is

MIRRORNODE is a governed execution system that coordinates multiple AI agents and development tools through a unified HTTP bridge. It provides metric exposure, state management, and inter-agent communication infrastructure for complex software projects requiring multi-model collaboration. The system operates as a Python–TypeScript hybrid with clearly defined integration surfaces and audit-oriented discipline.

## What Exists Today (Verified)

The following components are operational as described:

- **HTTP Bridge**: A live Python-based server exposing endpoints for agent interaction, metric collection, and state queries.
- **Metrics Surface**: A `/metrics` endpoint exposing `mirrornode:*` prefixed metrics in a Prometheus-compatible format.
- **Node Client Integration**: A TypeScript client capable of interacting with the bridge without error in local development environments.
- **Osiris Audit Tool**: A sellable product available as both a hosted interface and a downloadable ZIP package, designed for system state inspection and verification.
- **Agent Adapters**: Defined adapter interfaces exist for multiple AI models (GPT, Claude, Grok, Perplexity, Gemini), with verified interaction in local development contexts.

Transitional behaviors observed during development include metric duplication and namespace collisions. These behaviors are documented and treated as non-blocking during the current phase.

## Frozen Reference State

A complete system snapshot has been generated, hash-verified, and sealed as an immutable reference state. This snapshot serves as:

- A rollback point for development
- A verification baseline for system integrity
- A reference implementation for deployment validation
- An audit trail anchor for the Osiris Audit Tool

The reference state is treated as read-only. Modifications require explicit versioning and re-verification.

## Operational Roles

**Human Operator**  
Provides strategic direction, final decision authority, and system governance. Responsible for quality gates, deployment approval, and commercial decisions.

**AI Agent Collaborators**  
Execute discrete tasks within defined scope. Each agent operates according to specialized capabilities and produces advisory output subject to human review.

**External Tooling**  
Task management systems, version control, deployment platforms, and browser-based assistants may be used alongside MIRRORNODE but remain external to core execution.

## Integration Surfaces

**Verified Interfaces**
- HTTP endpoints for agent message passing
- Metrics endpoint for observability
- JSON-based request/response protocol
- Local development runtime

**Potential Interfaces (Not Yet Verified)**
- Remote deployment endpoints
- Persistent storage backends
- Third-party service webhooks
- Real-time websocket connections

Core integration surfaces are designed to enforce input validation and logging; this behavior is verified for HTTP and metrics endpoints. No interface accepts arbitrary code execution.

## Public vs Internal Boundary

**Publicly Visible**
- Osiris Audit Tool functionality and interface
- Product documentation and usage guides
- High-level architectural descriptions
- API specifications for verified integrations

**Intentionally Constrained**
- Internal coordination protocols between agents
- Detailed metric schemas and naming conventions
- Development environment configurations
- Strategic roadmap and unverified capabilities
- Governance policies and decision-making mechanics

This boundary protects operational integrity while maintaining transparency about confirmed capabilities.

## Definition of Production Success

Production success is defined by the following criteria:

1. **Commercial Validation**: At least one paying customer using the Osiris Audit Tool.
2. **Technical Stability**: Zero critical failures across verified integration surfaces over a 30-day observation period.
3. **Operational Clarity**: All participants can accurately describe current system state without contradiction.
4. **Audit Compliance**: All production deployments traceable to a sealed reference snapshot.
5. **Revenue Generation**: Confirmed revenue sufficient to cover the subsequent development cycle.

Success is measured by deployed capability and customer outcomes, not feature count.
