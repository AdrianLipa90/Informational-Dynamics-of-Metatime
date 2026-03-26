# Last copies merge report

## Inputs
- base clean snapshot: `CIEL_CANON_MERGED.zip`
- newer but dirty snapshot: `CIEL_MASTER_CONSOLIDATED_with_nonlocal_hyperspace.zip`
- latest loose spec: `BLOCH_NETWORK_COMMAND_QUANTIZATION.md`

## Method
- base = clean canon
- compare same relative paths
- ignore `__pycache__`, `.pyc`, `.pytest_cache`
- if newer snapshot contains a missing file, add it
- if same-path text differs, keep fuller text; otherwise preserve alternate master copy in `TODO/from_last_master_conflicts/`
- promote latest loose Bloch spec into root and also keep copy in `TODO/latest_loose/`

## Cleanliness
- junk/cache entries present in newer snapshot and excluded: **338**

## Added from newer snapshot / latest loose file
- count: **7**
  - `NONLOCAL_REPO_HYPERSPACE/README.md` — missing_in_base_added_from_master
  - `NONLOCAL_REPO_HYPERSPACE/registry.yaml` — missing_in_base_added_from_master
  - `NONLOCAL_REPO_HYPERSPACE/maps/repo_hypergraph.yaml` — missing_in_base_added_from_master
  - `NONLOCAL_REPO_HYPERSPACE/maps/semantic_bloch_localization.yaml` — missing_in_base_added_from_master
  - `NONLOCAL_REPO_HYPERSPACE/indices/README.md` — missing_in_base_added_from_master
  - `NONLOCAL_REPO_HYPERSPACE/TODO/README.md` — missing_in_base_added_from_master
  - `BLOCH_NETWORK_COMMAND_QUANTIZATION.md` — latest_loose_copy_promoted_to_root

## Same-path text decisions
- count: **1**
  - `README.md` — replaced_with_fuller_master (base chars 970, master chars 1186)

## Key result
- merged bundle keeps the clean canon as structural base
- newer `NONLOCAL_REPO_HYPERSPACE/` content is included
- latest `BLOCH_NETWORK_COMMAND_QUANTIZATION.md` is promoted to root
- comparison reports are preserved
- dirty cache artifacts from the newer snapshot are not propagated

Archived from source path: `comparison_reports_last_merge/SUMMARY.md`
