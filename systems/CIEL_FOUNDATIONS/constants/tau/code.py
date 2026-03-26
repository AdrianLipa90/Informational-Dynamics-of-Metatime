"""Canonical helpers for tau-mode handling in CIEL Foundations."""
from __future__ import annotations

import math
from typing import Iterable, Tuple

CANONICAL_ORBITAL_TAU_TRIAD: Tuple[float, float, float] = (0.263, 0.353, 0.489)
NEUTRINO_SEED_TAU_TRIAD: Tuple[float, float, float] = (0.02, 0.05, 0.10)


def tau_transport_factor(tau_i: float, tau_j: float, sigma: float) -> float:
    """Return the Gaussian resonance factor used by the orbital transport kernel."""
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    ratio = math.log(max(1e-12, tau_i / tau_j))
    return math.exp(-0.5 * (ratio / sigma) ** 2)


def effective_tau(values: Iterable[float], weights: Iterable[float]) -> float:
    """Compute a weighted effective tau mode."""
    vals = list(values)
    wts = list(weights)
    if len(vals) != len(wts):
        raise ValueError("values and weights must have the same length")
    total = sum(wts)
    if total == 0:
        raise ValueError("weight sum must be nonzero")
    return sum(v * w for v, w in zip(vals, wts)) / total
