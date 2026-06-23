# MIRRORNODE — Architecture (mirrornode-index)

**Repo role:** Canon index — ground truth documents, diff reports, boundary ledger  
**Authority:** `mirrornode/MIRRORNODE-CORE-HUB`

## Structure

```
canon/
  MASTER_CANON.md          — authoritative system canon
  PUBLIC_CANON.md          — external-facing canon
  INTERNAL_CANON.md        — internal-facing canon
  CANON_DIFF_REPORT.md     — adversarial audit record
  BOUNDARY_LEDGER.md       — boundary and scope ledger
  scripts/
    build_index.py         — index build script
    update_index.sh        — index update script
```

## Purpose

This repo is the canonical index of MIRRORNODE system truth. It does not contain runnable code or agent runtimes. Its documents are the reference point for governance audits, canon diffs, and boundary enforcement across all MIRRORNODE repos.

## Canon Diff Protocol

Before finalizing any canon update, a diff report (`CANON_DIFF_REPORT.md`) must be produced documenting:
- Aligned claims
- Corrected risk areas
- Outcome determination
