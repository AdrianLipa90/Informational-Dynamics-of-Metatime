from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from extract_real_geometry_v3 import build
from registry import load_system
from metrics import A_ij, closure_penalty, global_coherence
from dynamics import step


def _system():
    repo_root = ROOT.parents[1]
    payload = build(repo_root)
    (ROOT/'config'/'sectors_real_v3.json').write_text(__import__('json').dumps(payload['sectors'], indent=2), encoding='utf-8')
    (ROOT/'config'/'couplings_real_v3.json').write_text(__import__('json').dumps(payload['couplings'], indent=2), encoding='utf-8')
    return load_system(ROOT/'config'/'sectors_real_v3.json', ROOT/'config'/'couplings_real_v3.json')


def test_Aij_nontrivial_and_bounded():
    system = _system()
    z = A_ij(system, 'runtime', 'memory')
    assert abs(z) > 0.1
    assert abs(z) < 2.0


def test_closure_penalty_nonnegative():
    system = _system()
    assert closure_penalty(system) >= 0.0


def test_v3_stays_better_than_naive_explosion_window():
    system = _system()
    initial = global_coherence(system)
    for _ in range(20):
        system = step(system, dt=0.025)
    final = global_coherence(system)
    assert initial < 0.05
    assert final < 2.0
