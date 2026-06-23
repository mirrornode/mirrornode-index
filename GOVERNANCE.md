# MIRRORNODE — Governance (mirrornode-index)

**Authority:** `mirrornode/MIRRORNODE-CORE-HUB`

## Principles

1. This repo contains governance documents, not runnable code.
2. Canon is never deleted silently — deletions require a `CANON_DIFF_REPORT.md` entry.
3. `MASTER_CANON.md` is the source of truth; `PUBLIC_CANON.md` and `INTERNAL_CANON.md` must be consistent with it.
4. Speculative or aspirational claims must not appear in canon documents.

## Change Protocol

- All changes to `MASTER_CANON.md` require a new or updated `CANON_DIFF_REPORT.md` entry.
- `BOUNDARY_LEDGER.md` changes must document what boundary changed and why.
- Do not delete canon files without a recorded audit trail.

## Build Gate

- [ ] `CANON_DIFF_REPORT.md` updated if `MASTER_CANON.md` changed
- [ ] No speculative claims in any canon file
- [ ] `BOUNDARY_LEDGER.md` consistent with current scope
