# MIRRORNODE — Boundary Ledger

This file declares what this Copilot Space **contains** and what it **explicitly does not contain**.
Responses and claims are governed by this ledger to prevent drift.

## In scope (this Space contains)

- `canon/MASTER_CANON.md` — Internal technical/historical reference for recorded system state, capabilities, and boundaries; no overriding governance precedence
- `canon/PUBLIC_CANON.md` — External-facing summary derived from MASTER
- Pillars of ROTAN (Copilot Space Instructions) — Behavioral policy, invariants, contracts, output style
- `canon/BOUNDARY_LEDGER.md` — This scope guardrail
- `README.md` — How to use this Space and reference the canon (if included as a Space source)

## Out of scope (do not claim unless present in Space sources)

- Runtime implementation code, deployed endpoints, live service configs
- Production credentials, secrets, API keys, tokens, Authorization headers
- Unverified system descriptions, folklore, hidden assumptions
- Breaking changes without explicit operator confirmation
- Inferred schemas/fields/APIs not present in canon or other Space sources
- Third-party dependencies/integrations unless verified in canon or other Space sources
- Generated artifacts (diff reports, build outputs) unless explicitly added as Space sources

## Governance boundary

MIRRORNODE-CORE-HUB is the designated governance source. This Space indexes supporting evidence; source inclusion does not ratify policy or expand agent authority. Preserve conflicts and seek human Operator disposition within applicable review and security boundaries. The precedence correction does not re-verify recorded capabilities or deployments.

## Boundary rule

If a claim would reference anything outside these lists:
- Stop and ask the operator for the missing artifact or confirmation.

If a file/API/behavior is not present in Space sources:
- Respond “not specified (not in sources)” and ask for the source.
