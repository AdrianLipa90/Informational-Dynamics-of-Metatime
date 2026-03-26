# P0.2 Closeout and P1 Handoff

Date: 2026-03-24
Scope: whole repository with canonical focus on `systems/CIEL_OMEGA_COMPLETE_SYSTEM`
Status: completed

## Purpose

This document closes **P0: canonical integrity and hygiene** and hands forward the remaining structural problem to **P1: memory/storage boundary formalization**.

## P0 facts now established

1. The canonical runtime is **executable**.
   - `UnifiedSystem.create()` works.
   - `run_text_cycle(...)` works.
   - `pytest -q` passed during P0 validation.

2. Volatile validation residue is **not** part of the canonical payload.
   - `__pycache__/`, `.pyc`, `.pyo`, `.pytest_cache/` are excluded by policy.
   - Repository state at closeout contains **0** `__pycache__` directories, **0** `.pyc` files, and **0** `.pytest_cache` directories.

3. The packaged manifest is now **synchronized** to a real payload scope.
   - The self-referential manifest problem was removed.
   - The payload fingerprint and file count now refer to an explicit scope.

4. Persistent data artifacts were **classified rather than concealed**.
   - `CIEL_MEMORY_SYSTEM/TSM/ledger/memory_ledger.db`
   - `CIEL_MEMORY_SYSTEM/WPM/wave_snapshots/wave_archive.h5`
   - `ciel_omega/CIEL_MEMORY_SYSTEM/TSM/ledger/memory_ledger.db`

5. The two packaged ledger databases are **not identical**.
   - This divergence remains open by design.
   - P0 intentionally did not overwrite, merge, or silently delete them.

## Final P0 decisions

### Canonical hygiene decisions

- Volatile residue is disposable and must be removed after validation runs.
- Manifest claims must be recomputed against explicit scope rules.
- Missing files, disappearing files, and divergent stateful artifacts must be reported explicitly.

### Data-layer classification decisions

- Top-level `CIEL_MEMORY_SYSTEM/` is the **authoritative packaged runtime data layer**.
- Package-embedded `ciel_omega/CIEL_MEMORY_SYSTEM/.../memory_ledger.db` is a **legacy compatibility mirror** pending P1.
- `wave_archive.h5` is treated as a real persistent artifact, not noise.

## What P0 does NOT solve

P0 does not perform structural storage refactors.
It therefore leaves the following unresolved on purpose:

- duplicate non-identical ledger databases inside one packaged system
- mixed placement of logical memory code and physical storage artifacts
- lack of explicit storage ports between runtime logic and persistence layer
- absence of a single formal data contract for ledger / semantic / tensor stores

These are P1 problems, not hygiene problems.

## P1 entry conditions now satisfied

P1 may begin because the following are now true:

- the canonical payload is executable
- volatile residue policy is explicit
- packaged manifest scope is honest
- persistent artifacts are inventoried
- the authoritative data layer has been classified
- the legacy mirror has been named as a migration target rather than hidden duplicate

## P1 required objectives

1. Separate **logical memory operators** from **physical storage adapters**.
2. Introduce explicit ports for:
   - ledger storage
   - semantic/document storage
   - tensor/archive storage
   - graph/provenance storage
3. Decide the fate of the package-embedded legacy ledger:
   - compatibility shim,
   - migration target,
   - or removable artifact.
4. Preserve runtime behavior while removing ambiguous storage ownership.

## Acceptance criterion for P0 closeout

P0 is considered complete when all of the following are true:

- canonical runtime can run
- volatile residue is cleaned and excluded by policy
- manifest is synchronized to explicit scope
- divergent persistent artifacts are inventoried and classified
- unresolved storage conflict is formally handed to P1

All of those conditions are now satisfied.
