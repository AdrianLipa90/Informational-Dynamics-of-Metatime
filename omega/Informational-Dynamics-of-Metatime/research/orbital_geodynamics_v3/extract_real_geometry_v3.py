from __future__ import annotations
import json
from pathlib import Path

# reuse v2 extraction
import sys
sys.path.append(str(Path(__file__).resolve().parents[1] / 'orbital_geodynamics_v2'))
from extract_real_geometry import build as build_v2  # type: ignore

TAU_MAP = {1: 0.263, 2: 0.353, 4: 0.489}


def build(repo_root: Path):
    payload = build_v2(repo_root)
    sectors = payload['sectors']['sectors']
    for name, sec in sectors.items():
        sec['tau'] = TAU_MAP.get(sec['q_target'], 0.353)
    payload['sectors'] = {'sectors': sectors}
    return payload


if __name__ == '__main__':
    repo_root = Path(__file__).resolve().parents[2]
    payload = build(repo_root)
    out_dir = Path(__file__).resolve().parent / 'results'
    out_dir.mkdir(exist_ok=True)
    (out_dir/'real_geometry_extraction_v3.json').write_text(json.dumps(payload, indent=2), encoding='utf-8')
    (Path(__file__).resolve().parent/'config'/'sectors_real_v3.json').write_text(json.dumps(payload['sectors'], indent=2), encoding='utf-8')
    (Path(__file__).resolve().parent/'config'/'couplings_real_v3.json').write_text(json.dumps(payload['couplings'], indent=2), encoding='utf-8')
    print(out_dir/'real_geometry_extraction_v3.json')
