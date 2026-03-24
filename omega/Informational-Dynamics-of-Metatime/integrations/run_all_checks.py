#!/usr/bin/env python3
from __future__ import annotations
import subprocess
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def run(cmd, cwd):
    print(f"\n=== RUNNING: {' '.join(cmd)} (cwd={cwd}) ===")
    return subprocess.run(cmd, cwd=str(cwd), check=False)

if __name__ == '__main__':
    tasks = [
        ([sys.executable, '-m', 'pytest', '-q'], ROOT / 'systems' / 'CIEL_OMEGA_COMPLETE_SYSTEM'),
        ([sys.executable, 'ciel_omega/demo_unified_euler.py'], ROOT / 'systems' / 'CIEL_OMEGA_COMPLETE_SYSTEM'),
        ([sys.executable, 'ciel_omega/demo_vocabulary_resolve.py'], ROOT / 'systems' / 'CIEL_OMEGA_COMPLETE_SYSTEM'),
        ([sys.executable, 'simulate_holonomic_relations.py'], ROOT / 'research' / 'holonomic_relations_research_grade' / 'code'),
        ([sys.executable, 'analyze_observed_holonomic.py'], ROOT / 'research' / 'holonomic_observed_end_to_end' / 'code'),
    ]
    rc=0
    for cmd, cwd in tasks:
        res = run(cmd, cwd)
        rc = rc or res.returncode
    raise SystemExit(rc)
