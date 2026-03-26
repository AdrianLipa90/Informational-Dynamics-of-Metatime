# ARCHIVES

Status: canonical archive root on branch `agent3a`.

## Role
This folder is the designated landing zone for legacy, comparison, forensic, recovery, reconsolidation, and other archival artifacts that should not retain active canonical authority in the live repository tree.

## Intended archive classes
- `comparison_reports/`
- `comparison_reports_forensic/`
- `comparison_reports_last_merge/`
- `comparison_reports_recovery/`
- nested audit and reconsolidation artifacts under `omega/Informational-Dynamics-of-Metatime/reports/audit/`
- nested comparison/import reports such as `omega/Informational-Dynamics-of-Metatime/comparison_reports_todo_external_refs/`
- other files explicitly reclassified as legacy/reference-only

## Archive rule
Archived content may remain useful for provenance, diff evidence, or recovery, but it must not outrank the canonical live tree.

## Current stage
On `agent3a`, this archive root is established first.
Actual relocations should follow the manifest-driven sequence to avoid accidental loss of provenance.
