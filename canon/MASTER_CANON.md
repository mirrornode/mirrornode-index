<!--
CANON: MASTER (INTERNAL, AUTHORITATIVE)
Describes: system state, verified capabilities, boundaries, roles, success criteria.
PUBLIC_CANON.md is derived from this file.

Pillars of ROTAN (Copilot Space Instructions) governs assistant behavior and runtime contract style.
If conflict: MASTER_CANON.md content wins; otherwise ask operator.
-->

# MIRRORNODE — Master Canon (v1.0)

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
