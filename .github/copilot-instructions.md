# Copilot Instructions — mirrornode-index

## System Context

This is the canon index repo for MIRRORNODE. It contains governance documents only — no runnable code, no agent runtimes.

## Hard Rules

- **This repo is documentation only.** Do not add runnable services or agent dispatch logic.
- **Never speculate.** All canon documents must reflect verified system behavior.
- **Deletions require audit trails.** Do not delete `MASTER_CANON.md`, `BOUNDARY_LEDGER.md`, or `CANON_DIFF_REPORT.md` without a recorded reason.
- **Never reference non-real routes:** `/system/execute`, `/system/replay`, `/execute-task`.

## Conventions

- All changes to canon documents should be accompanied by a `CANON_DIFF_REPORT.md` update
- Markdown only — no code files at the repo root
- Scripts in `canon/scripts/` are build/index utilities only
