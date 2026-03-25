# Agent3 Informational Dynamics Audit Plan

Repository: `AdrianLipa90/Informational-Dynamics-of-Metatime`
Branch: `Agent3`
Scope: Informational Dynamics, repository identity, indexing, canonical routing, duplicate control.

## Primary diagnosis
This repository is already rich and operational, but it is not yet fully closed as a single-authority canonical graph.
The main risks are:
- split repository identity,
- layered but insufficiently indexed authority,
- duplicate or nested tree signals,
- incomplete conversion of documentation into routing/control infrastructure.

## Immediate goals
1. Establish one global navigation authority on this branch.
2. Seed a machine-readable object registry.
3. Mark canonical vs reference vs imported vs duplicate-candidate content.
4. Prevent downstream code from outrunning upstream formal objects.
5. Prepare duplicate cleanup without deleting evidence prematurely.

## Phase 1 — navigation authority
Deliverables:
- `docs/INDEX.md` as the global navigation layer
- explicit role split between root bundle, formal layer, runtime layer, and nonlocal routing layer

Success condition:
- a reader can determine where to start and what each top-level authority does

## Phase 2 — seed registry
Deliverables:
- `manifests/index_registry.yaml`
- first object IDs
- first status labels
- first upstream/downstream relations

Minimum fields per object:
- `id`
- `name`
- `layer`
- `status`
- `provenance_type`
- `owner_layer`
- `upstream`
- `downstream`
- `path`
- `placeholder`

## Phase 3 — duplicate and nested-tree audit
Target concern:
- root content appears to have mirrored or nested counterparts under `omega/Informational-Dynamics-of-Metatime/...`

Deliverables:
- explicit duplicate-candidate records in the registry
- canonical path decision notes
- no destructive cleanup until duplicates are fully classified

## Phase 4 — validator layer
Deliverables:
- existence check for every registered path
- duplicate-candidate check
- missing-upstream check
- code-without-formal-upstream check
- placeholder discipline check

## Phase 5 — branch-local documentation repairs
Deliverables:
- crossrefs from root README / report / hypergraph sector into the registry
- branch-local notes for canonical entry points
- explicit distinction between executable truth and formal truth

## Current high-priority candidate objects
- `README.md`
- `reports/CONSOLIDATION_REPORT.md`
- `docs/procedures/CRITICAL_REPO_IDENTIFICATION_AND_WRITE_HYGIENE.md`
- `NONLOCAL_REPO_HYPERSPACE/README.md`
- `systems/CIEL_FOUNDATIONS/README.md`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/README.md`
- `integrations/run_all_checks.py`
- duplicate-candidate mirror paths under `omega/Informational-Dynamics-of-Metatime/...`

## Agent3 rule
Agent3 does not yet delete or reclassify canonical content on `main`.
Agent3 first builds the audit graph, then proposes the cleanup sequence.
