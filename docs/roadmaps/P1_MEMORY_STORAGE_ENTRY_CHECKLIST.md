# P1 Memory/Storage Entry Checklist

Date: 2026-03-24
Status: active next-step checklist
Depends on: P0 closeout

## Goal

Start P1 from a clean canonical state and refactor memory/storage boundaries without corrupting runtime behavior.

## Inputs from P0

- `reports/audit/P0_CANONICAL_INTEGRITY_AUDIT_2026-03-24.md`
- `reports/audit/P0_1_MANIFEST_SYNC_2026-03-24.md`
- `reports/audit/P0_2_CLOSEOUT_AND_P1_HANDOFF_2026-03-24.md`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/DATA_LAYER_POLICY.md`

## Mandatory starting facts

- top-level `CIEL_MEMORY_SYSTEM/` is the authoritative packaged runtime data layer
- package-embedded ledger mirror is legacy and non-identical
- logical memory and physical persistence are currently mixed
- runtime behavior must remain reproducible during refactor

## P1 work packages

### P1.1 Inventory and boundary map
- identify logical memory modules
- identify physical storage modules
- identify direct backend calls (`sqlite3`, `h5py`, file writes, JSON persistence)
- map current ownership of ledger, tensor archive, and audit logs

### P1.2 Extract storage namespace
- introduce `storage/`
- define first-class subareas:
  - `storage/ledger/`
  - `storage/semantic/`
  - `storage/tensor/`
  - `storage/graph/`

### P1.3 Port interfaces
- define `LedgerPort`
- define `SemanticStorePort`
- define `TensorStorePort`
- define `GraphStorePort`

### P1.4 Compatibility strategy
- keep runtime functioning with adapters and shims
- explicitly decide treatment of package-embedded legacy ledger
- do not silently merge stateful artifacts

### P1.5 Validation
- smoke run `UnifiedSystem`
- targeted tests for memory orchestration
- re-audit persistent artifacts
- confirm no new ambiguous ownership paths were introduced

## P1 done condition

P1 is complete when:

- logical memory no longer owns raw backend details directly
- physical persistence lives behind explicit storage adapters/ports
- authoritative data-layer ownership is unambiguous
- legacy ledger handling is explicitly resolved or wrapped as compatibility
- runtime behavior remains verified
