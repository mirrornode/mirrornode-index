# Repository Source Map — mirrornode-index

Status: descriptive source map for review; no authority or release grant.
Observed baseline: `b6f3ed700f95251b8276c7f79c789ae7319450eb`.
Prepared: 2026-10-22.

## Repository boundaries

| Surface | Documented purpose | Evidence |
|---|---|---|
| mirrornode/mirrornode-index | Cross-repository index and technical/historical reference; no resident runtime | `AGENTS.md`, `ARCHITECTURE.md`, `GOVERNANCE.md` at the observed baseline |
| mirrornode/MIRRORNODE-CORE-HUB | Designated governance source | [Pinned CANONICAL_SOURCES.md](https://github.com/mirrornode/MIRRORNODE-CORE-HUB/blob/aac3b5b473b12e3134224b316b6810de9a15f416/CANONICAL_SOURCES.md) |

This is a bounded source map, not a complete organization inventory. References do not prove current deployment, implementation, ratification, or security clearance. The index may reference agents but cannot define or expand their authority.

## Local source locations

- `AGENTS.md`: resident-runtime and authority boundary.
- `ARCHITECTURE.md`: index architecture and CORE-HUB governance relationship.
- `GOVERNANCE.md`: repository change and evidence rules.
- `canon/MASTER_CANON.md`: recorded technical/historical system descriptions.
- `canon/INTERNAL_CANON.md`: internal reference descriptions and boundaries.
- `canon/PUBLIC_CANON.md`: derived public reference; claims require current verification before use.
- `canon/BOUNDARY_LEDGER.md`: scope guardrail for included sources.
- `SYSTEM_CONTRACT.md` and `AGENTS_TODO.md`: existing records consumed by Canon Gate; file presence does not establish current runtime or authority.
- `.github/workflows/canon-gate.yml` and `scripts/canon_gate.py`: existing automated contract checks.

## Provenance and unresolved work

Canon Gate requires this filename. It was absent at the observed baseline; GOV-01 PR #2's first check failed for that pre-existing absence. This map supplies evidenced documentation without changing the workflow or checker.

GOV-01 remains OPEN pending separate reviewed dispositions, merges, and destination-branch verification. CORE-HUB PR #67 is a proposal until its disposition is recorded; this map does not promote it. Preserve conflicting source claims and escalate for human Operator disposition within applicable review and security boundaries.
