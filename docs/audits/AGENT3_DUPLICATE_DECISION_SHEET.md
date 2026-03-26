# Agent3 Duplicate Decision Sheet

Repository: `AdrianLipa90/Informational-Dynamics-of-Metatime`
Branch: `Agent3`

Purpose: classify duplicate or nested-tree candidates without destructive cleanup.

## Decision statuses
- `keep_canonical_root`
- `keep_nested_only`
- `merge_then_prune`
- `needs_manual_review`
- `reference_copy_only`

## Current candidate table

| Candidate ID | Canonical candidate path | Duplicate candidate path | Current decision | Reason | Action status |
|---|---|---|---|---|---|
| DUP-IDM-0001 | `reports/CONSOLIDATION_REPORT.md` | `omega/Informational-Dynamics-of-Metatime/reports/CONSOLIDATION_REPORT.md` | `keep_canonical_root` | Root report is already referenced by root README and functions as the visible top-level report; nested copy risks splitting authority. | pending |
| DUP-IDM-0002 | `comparison_reports/cleaned_canon_inventory.tsv` | `omega/Informational-Dynamics-of-Metatime/comparison_reports/cleaned_canon_inventory.tsv` | `needs_manual_review` | Inventory files may be products of a prior merge/mirror sequence and should be compared before pruning. | pending |
| DUP-IDM-0003 | `comparison_reports_forensic/clean_inventory.tsv` | `omega/Informational-Dynamics-of-Metatime/comparison_reports_forensic/clean_inventory.tsv` | `needs_manual_review` | Forensic inventories must be checked for path drift and timestamp drift before classification. | pending |

## Rules
1. No duplicate candidate may be deleted only because it is nested.
2. A root-level file has priority only when it is already used as the visible canonical entry point.
3. Any duplicate tied to comparison or forensic evidence should be reviewed before pruning.
4. If contents differ materially, decision must become `merge_then_prune` or `reference_copy_only`, not blind removal.
5. Every resolved decision should later be mirrored into the machine-readable registry.
