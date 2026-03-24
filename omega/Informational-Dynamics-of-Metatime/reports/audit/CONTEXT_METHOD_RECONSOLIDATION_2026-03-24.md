# Context-derived reconsolidation method

## Method reconstructed from project context
1. Treat the clean canonical bundle as the structural base.
2. Compare newer/supplementary snapshots by relative path.
3. Ignore volatile residue (`__pycache__`, `.pyc`, `.pytest_cache`).
4. If a supplementary snapshot contains a missing file, add it.
5. If the same-path text differs, keep the fuller text; preserve alternate copies only when the shorter snapshot would otherwise be lost.
6. Keep non-canonical but relevant incoming projects under `TODO/external_references/`.
7. Explicitly record missing/disappearing files, build inconsistencies, and merge decisions in audit reports.

## Applied in this edit
- base: `CIEL_COMPLETE_REPO_CANONICAL_QE_FIXED_DEBUGGED_GGUF_THREEPROMPT_HTRI_PATCH_WITH_TODO_BOTH.zip`
- overlay: `CIEL_REPO_SNAPSHOT_P0_COMPLETE_2026-03-24.zip`
- imported reference intake: `Metatime-main.zip`
