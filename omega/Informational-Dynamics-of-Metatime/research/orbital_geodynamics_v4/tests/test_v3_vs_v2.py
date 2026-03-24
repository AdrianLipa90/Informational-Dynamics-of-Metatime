from __future__ import annotations
import json
from pathlib import Path


def test_v3_improves_global_coherence_over_v2():
    root_v2 = Path('/mnt/data/_repo_global_impl/research/orbital_geodynamics_v2/results/real_demo_results.json')
    root_v3 = Path('/mnt/data/_repo_global_impl/research/orbital_geodynamics_v3/results/v3_demo_results.json')
    v2 = json.loads(root_v2.read_text())
    v3 = json.loads(root_v3.read_text())
    assert v3['final_after_20_steps']['R_H'] < v2['final_after_20_steps']['R_H']
