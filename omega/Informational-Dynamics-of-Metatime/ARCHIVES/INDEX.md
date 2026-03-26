# ARCHIVES Index

Branch: `agent3b`
Repository: `AdrianLipa90/Informational-Dynamics-of-Metatime`

## Role
This index is the navigation layer for archival sectors created during cleaning and segregation.
It records which legacy or mirror-derived layers have already been demoted into `ARCHIVES/` and which still remain to be fully relocated.

## Archive sectors already established
- [`comparison_reports/`](comparison_reports/) — historical comparison outputs
- [`comparison_reports_last_merge/`](comparison_reports_last_merge/) — last-merge reconciliation outputs
- [`comparison_reports_forensic/`](comparison_reports_forensic/) — forensic sieve / clean inventory outputs
- [`comparison_reports_recovery/`](comparison_reports_recovery/) — recovery comparison outputs
- [`omega_reports_audit/`](omega_reports_audit/) — nested mirror audit artifacts
- [`omega_reports_debug/`](omega_reports_debug/) — nested mirror debug artifacts
- [`omega_logs/`](omega_logs/) — nested mirror execution logs

## Canonical archive rule
Anything placed here is treated as legacy/reference/provenance material unless explicitly promoted back into the live tree by a later audited decision.

## Still pending
- full relocation of additional nested `omega/...` comparison/import audit sectors
- demotion or removal of live duplicate paths once archive landing zones are fully confirmed
- registry/index synchronization so that archive sectors are visible in the machine-readable navigation graph
