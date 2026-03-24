from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Sector:
    name: str
    orbital_level: int
    orbital_type: str
    dominant_spin: str
    theta: float
    phi: float
    rhythm_ratio: float
    amplitude: float
    coherence_weight: float
    info_mass: float
    q_target: int
    damping: float
    preference: float
    defect: float = 0.0
    berry_phase: float = 0.0
    tau: float = 0.353

@dataclass
class OrbitalSystem:
    sectors: Dict[str, Sector] = field(default_factory=dict)
    couplings: Dict[str, Dict[str, float]] = field(default_factory=dict)
    params: Dict[str, float] = field(default_factory=dict)

    def names(self):
        return list(self.sectors.keys())

    def coupling(self, a: str, b: str) -> float:
        if a == b:
            return 0.0
        return self.couplings.get(a, {}).get(b, self.couplings.get(b, {}).get(a, 0.0))
