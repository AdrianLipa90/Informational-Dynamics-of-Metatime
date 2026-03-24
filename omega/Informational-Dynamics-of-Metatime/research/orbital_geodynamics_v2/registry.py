from __future__ import annotations
import json
from pathlib import Path
from model import Sector, OrbitalSystem


def load_system(sectors_path: str | Path, couplings_path: str | Path) -> OrbitalSystem:
    sectors_raw = json.loads(Path(sectors_path).read_text(encoding='utf-8'))
    couplings_raw = json.loads(Path(couplings_path).read_text(encoding='utf-8'))
    sectors = {name: Sector(name=name, **payload) for name, payload in sectors_raw['sectors'].items()}
    return OrbitalSystem(sectors=sectors, couplings=couplings_raw['couplings'])
