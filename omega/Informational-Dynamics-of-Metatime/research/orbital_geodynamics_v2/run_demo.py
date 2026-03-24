from __future__ import annotations
import json
from pathlib import Path
from registry import load_system
from metrics import holonomy_defect, global_coherence, chord_tension, global_chirality, local_vorticity, effective_mass
from dynamics import step


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
    system = load_system(root / 'config' / 'sectors.json', root / 'config' / 'couplings.json')
    initial = snapshot(system)
    for _ in range(20):
        system = step(system, dt=0.03)
    final = snapshot(system)
    payload = {
        'engine': 'Euler-Berry-Poincare-421',
        'steps': 20,
        'dt': 0.03,
        'initial': initial,
        'final_after_20_steps': final,
    }
    out = root / 'results' / 'demo_results.json'
    out.write_text(json.dumps(payload, indent=2), encoding='utf-8')
    print(out)


if __name__ == '__main__':
    main()
