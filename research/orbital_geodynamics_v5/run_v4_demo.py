from __future__ import annotations
import json
from pathlib import Path
from registry import load_system
from dynamics import step
from metrics import (
    holonomy_defect, global_coherence, chord_tension, global_chirality,
    local_vorticity, effective_mass, closure_penalty, closure_residuals, A_matrix
)
from extract_real_geometry_v3 import build


def snapshot(system):
    delta = holonomy_defect(system)
    return {
        'R_H': global_coherence(system),
        'T_glob': chord_tension(system),
        'Lambda_glob': global_chirality(system),
        'closure_penalty': closure_penalty(system),
        'closure_residuals': closure_residuals(system),
        'Delta_H': {'real': delta.real, 'imag': delta.imag},
        'vorticity': local_vorticity(system),
        'masses': effective_mass(system),
        'theta': {k: v.theta for k, v in system.sectors.items()},
        'phases': {k: v.phi for k, v in system.sectors.items()},
        'berry_phase': {k: v.berry_phase for k, v in system.sectors.items()},
        'amplitudes': {k: v.amplitude for k, v in system.sectors.items()},
        'defects': {k: v.defect for k, v in system.sectors.items()},
        'taus': {k: v.tau for k, v in system.sectors.items()},
    }


def main():
    root = Path(__file__).resolve().parent
    repo_root = root.parents[1]
    payload = build(repo_root)
    (root/'config'/'sectors_real_v4.json').write_text(json.dumps(payload['sectors'], indent=2), encoding='utf-8')
    (root/'config'/'couplings_real_v4.json').write_text(json.dumps(payload['couplings'], indent=2), encoding='utf-8')

    system = load_system(root/'config'/'sectors_real_v4.json', root/'config'/'couplings_real_v4.json')
    initial = snapshot(system)
    A0 = A_matrix(system)
    for _ in range(20):
        system = step(system, dt=0.025, tau_eta=0.01, tau_reg=0.0)
    final = snapshot(system)
    A1 = A_matrix(system)

    out = {
        'engine': 'Euler-Berry-Poincare-421-AijTau-global-v4-tauadaptive',
        'steps': 20,
        'dt': 0.025,
        'tau_eta': 0.01,
        'tau_reg': 0.0,
        'initial': initial,
        'final_after_20_steps': final,
        'A_initial': A0,
        'A_final': A1,
    }
    out_dir = root/'results'
    out_dir.mkdir(exist_ok=True)
    (out_dir/'v4_demo_results.json').write_text(json.dumps(out, indent=2), encoding='utf-8')
    print(out_dir/'v4_demo_results.json')


if __name__ == '__main__':
    main()
