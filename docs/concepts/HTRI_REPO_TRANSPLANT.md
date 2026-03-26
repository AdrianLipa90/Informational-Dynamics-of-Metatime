# HTRI_REPO_TRANSPLANT

This note maps selected ideas from the HTRI hardware concept into repository-scale software architecture.

## Transferable ideas

### 1. Beat / phase control loop
Hardware concept:
- measure phase drift
- compute beat error
- apply bounded correction

Repo transplant:
- read global orbital metrics
- compute coherence error
- propose bounded parameter corrections
- export control/state/health manifests

### 2. Topological local API
Hardware concept:
- local block can query topological charge and coherence status

Repo transplant:
- node/module/folder can query:
  - topological charge
  - coherence index
  - phase
  - loop integrity
  - sync-to-phase recommendation

### 3. Coherence-aware execution policy
Hardware concept:
- local quality influences execution mode

Repo transplant:
- low coherence => safer, read-only, extra diagnostics
- medium coherence => standard diagnostics
- high coherence => allow deeper passes and stronger integration

### 4. Register map -> manifest/state map
Hardware concept:
- explicit control/status registers

Repo transplant:
- `manifests/orbital/state.json`
- `manifests/orbital/control.json`
- `manifests/orbital/health.json`

## Non-transferable directly
The following remain hardware-specific and are not transplanted literally:
- on-die oscillator mesh
- PDN routing
- MMIO register fabric
- package-level synchronization
- H200 / GB300 silicon layout assumptions
