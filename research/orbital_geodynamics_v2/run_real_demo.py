
from __future__ import annotations
import json
from pathlib import Path
from registry import load_system
from metrics import holonomy_defect, global_coherence, chord_tension, global_chirality, local_vorticity, effective_mass
from dynamics import step
from extract_real_geometry import build


def snapshot(system):
    delta = holonomy_defect(system)
    return {
        'R_H': global_coherence(system),
        'T_glob': chord_tension(system),
        'Lambda_glob': global_chirality(system),
        'Delta_H': {'real': delta.real, 'imag': delta.imag},
        'vorticity': local_vorticity(system),
        'masses': effective_mass(system),
        'theta': {k: v.theta for k, v in system.sectors.items()},
        'phases': {k: v.phi for k, v in system.sectors.items()},
        'berry_phase': {k: v.berry_phase for k, v in system.sectors.items()},
        'amplitudes': {k: v.amplitude for k, v in system.sectors.items()},
        'defects': {k: v.defect for k, v in system.sectors.items()},
    }


def main():
    root = Path(__file__).resolve().parent
    repo_root = root.parents[1]
    payload = build(repo_root)
    # write derived configs
    (root/'config'/'sectors_real.json').write_text(json.dumps(payload['sectors'], indent=2), encoding='utf-8')
    (root/'config'/'couplings_real.json').write_text(json.dumps(payload['couplings'], indent=2), encoding='utf-8')

    system = load_system(root/'config'/'sectors_real.json', root/'config'/'couplings_real.json')
    initial = snapshot(system)
    for _ in range(20):
        system = step(system, dt=0.03)
    final = snapshot(system)
    out = {
        'engine': 'Euler-Berry-Poincare-421-real-mesh',
        'mesh_inputs': {
            'imports': payload['imports'],
            'readme_mesh': payload['readme_mesh'],
            'agent_mesh': payload['agent_mesh'],
            'manifest_bonus': payload['manifest_bonus'],
            'pair_scores': payload['pair_scores'],
            'sector_centrality': payload['sector_centrality'],
        },
        'steps': 20,
        'dt': 0.03,
        'initial': initial,
        'final_after_20_steps': final,
    }
    out_dir = root/'results'
    out_dir.mkdir(exist_ok=True)
    (out_dir/'real_demo_results.json').write_text(json.dumps(out, indent=2), encoding='utf-8')
    print(out_dir/'real_demo_results.json')


if __name__ == '__main__':
    main()
