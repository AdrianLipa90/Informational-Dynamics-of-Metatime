# Audit Index

Branch: `Agent3`
Repository: `AdrianLipa90/Informational-Dynamics-of-Metatime`

Purpose: local navigation layer for Agent3 audit artifacts.

## Core audit documents
- [`AGENT3_INFORMATIONAL_DYNAMICS_AUDIT_PLAN.md`](AGENT3_INFORMATIONAL_DYNAMICS_AUDIT_PLAN.md) — main repair plan and phase sequence
- [`AGENT3_DUPLICATE_DECISION_SHEET.md`](AGENT3_DUPLICATE_DECISION_SHEET.md) — human-readable duplicate classification decisions

## Machine-readable audit state
- [`../../manifests/index_registry.yaml`](../../manifests/index_registry.yaml) — object registry for canonical routing and duplicate candidates
- [`../../manifests/duplicate_decisions.yaml`](../../manifests/duplicate_decisions.yaml) — machine-readable duplicate decisions

## Validators and runners
- [`../../integrations/validate_index_registry.py`](../../integrations/validate_index_registry.py) — validates object registry structure and path existence
- [`../../integrations/validate_duplicate_decisions.py`](../../integrations/validate_duplicate_decisions.py) — validates duplicate decision consistency against the registry
- [`../../integrations/run_agent3_index_audit.py`](../../integrations/run_agent3_index_audit.py) — minimal index registry audit runner
- [`../../integrations/run_agent3_full_audit.py`](../../integrations/run_agent3_full_audit.py) — combined Agent3 audit runner

## Current Agent3 audit chain
Global index -> audit plan -> object registry -> duplicate decisions -> validator(s) -> runner
