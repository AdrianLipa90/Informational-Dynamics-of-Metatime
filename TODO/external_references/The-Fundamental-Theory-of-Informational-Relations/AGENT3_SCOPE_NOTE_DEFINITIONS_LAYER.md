# AGENT3 scope note — definitions layer

Source repository: `The-Fundamental-Theory-of-Informational-Relations`
Recorded on branch: `agent3a`
Recorded by: `AGENT3`

## Status
Pending execution item.
This note is a saved operational scope item, not a claim that the target repository has already been repaired.

## Source audit summary
An external audit of the `definitions/` layer reports:

### Confirmed strengths
- `definitions/registry.yaml` contains real object records with IDs, paths, and dependencies.
- `definitions/metatime/` is real and contains at least:
  - `metatime_manifold.md`
  - `metatime_field.md`
  - `fermion_cycles.md`
- these files are epistemically honest: imported/transcribed status, scope guards, no false claim of full re-derivation.

### Detected problems
1. `definitions/INDEX.md` is partially outdated and still describes `definitions/registry.yaml` as mostly empty.
2. at least part of the declared foundation paths in the registry do not resolve cleanly in direct verification.
3. ownership metadata is inconsistent:
   - `definitions/AGENT7.md` declares local AGENT7 scope
   - `definitions/registry.yaml` uses `branch_owner: Agent5`

## Operational reading for AGENT3
Until repaired, the `definitions/` layer in that repository should not be treated as a fully closed single source of truth.

Temporary handling rule:
- `definitions/metatime/` -> partially stable
- `definitions/foundations/` -> validate before downstream coupling
- `definitions/INDEX.md` -> correctable document, not fully authoritative live description

## Priority repair queue
1. synchronize `definitions/registry.yaml` with real files
2. confirm or restore missing files in `definitions/foundations/`
3. update `definitions/INDEX.md`
4. add `registry/path/ID` validation

## AGENT3 rule
If AGENT3 later performs cross-reference, navigation, or index consolidation touching this external repository, this note must be treated as a blocking caution:
no downstream binding should assume that semantically declared objects are already physically resolved until the above checks pass.
