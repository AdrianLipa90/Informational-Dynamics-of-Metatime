# P0.1 Manifest Synchronization Audit

Date: 2026-03-24
Scope: `systems/CIEL_OMEGA_COMPLETE_SYSTEM`
Status: completed

## What was done

- Recomputed canonical payload counts and fingerprints against the actual packaged tree.
- Defined explicit fingerprint scope rules so the manifest is no longer self-referential.
- Classified persistent data artifacts separately from volatile validation residue.
- Recorded a P0 policy decision for divergent memory artifacts.
- Updated the packaged README to clarify Python-file counts with and without `TODO/`.
- Re-ran manifest synchronization after documentation edits to eliminate post-edit drift.

## Main correction

Previous manifest claim:
- File count: 539
- Fingerprint: `736a1576d7186517826581d9c7e4c88846bb397d835e763f21b3a69e5ad012f1`

Synchronized manifest claim:
- Whole-system payload file count: 307
- Whole-system payload fingerprint: `b701c02d9d5f706ea39861d1b6acf23bae3dcd0bd831757e18a4c5f3b4e73d6b`

## Scope rules used

Excluded:
- `CANONICAL_BUILD_MANIFEST.md`
- `__pycache__/`
- `.pytest_cache/`
- `*.pyc`
- `*.pyo`

Included:
- code, docs, configs, tests, demos
- top-level runtime data layer
- package-embedded legacy ledger mirror

## Persistent data findings

- Data artifact count: 3
- Data fingerprint: `cbe0887bb7b105422ad7eb92a9bbff5de2fa1303f48be182806f91eb45aae696`
- Top-level packaged runtime data tree file count: 2
- Top-level packaged runtime data fingerprint: `3380f1b67a639012a2bacd59ee318a1447beacb732a57eb319f46756e8336d91`
- Package subtree file count: 298
- Package subtree fingerprint: `e1291cf480c14ccfa96ef1318ece36e019a61404446e5793346532df66026d8a`

### Divergent persistent artifacts

| path | size_bytes | sha256 |
|---|---:|---|
| `CIEL_MEMORY_SYSTEM/TSM/ledger/memory_ledger.db` | 12288 | `a34926b730016cc6b0b897680421127d51d65b3021a6dba079f0d368b37c2700` |
| `CIEL_MEMORY_SYSTEM/WPM/wave_snapshots/wave_archive.h5` | 1832 | `7859c8aaf311c22e68f5c754b1a0bf31f26c1fcba902da4710d48f46446e8ea8` |
| `ciel_omega/CIEL_MEMORY_SYSTEM/TSM/ledger/memory_ledger.db` | 12288 | `1131d054a13e88f00911c71c1e48f33727ca3f0f7d93f6516cb9ea11e97bdfb9` |


## Policy result

P0 does **not** silently delete or overwrite divergent `.db` files.
Instead:
- top-level `CIEL_MEMORY_SYSTEM/` is treated as the authoritative packaged runtime data layer
- package-embedded `ciel_omega/CIEL_MEMORY_SYSTEM/.../memory_ledger.db` is classified as a legacy compatibility mirror pending P1

## Open issue left intentionally unresolved in P0

The package still carries two non-identical ledger databases. This is documented, not concealed. Actual structural resolution belongs to P1 (memory/storage boundary formalization).
