# AGENT3B duplicate cleanup first

Branch: `agent3b`

## Rule
Duplicate cleanup is the highest current priority.
No broader indexing, authority promotion, or downstream consolidation should outrun the removal of split authority between the root tree and the nested `omega/Informational-Dynamics-of-Metatime/` mirror.

## Immediate priority classes
1. `TODO/` vs nested `omega/.../TODO/`
2. `NONLOCAL_REPO_HYPERSPACE/` vs nested mirror
3. `systems/CIEL_FOUNDATIONS/` vs nested mirror
4. `systems/CIEL_OMEGA_COMPLETE_SYSTEM/` vs nested mirror
5. root comparison layers vs nested mirror comparison layers
6. root `reports/` and `logs/` vs nested mirror `reports/` and `logs/`

## Current working rule
- root tree is canonical unless explicitly reclassified
- nested mirror is legacy by default unless it contains missing evidence not yet promoted
- archive copies preserve provenance but do not become new live authority

## Execution order
1. declare duplicate pair
2. classify canonical side
3. preserve evidence in `ARCHIVES/` if needed
4. demote nested authority
5. update manifests and indices
6. only then continue other consolidation work

## Control file
See: `manifests/duplicate_cleanup_priority.yaml`
