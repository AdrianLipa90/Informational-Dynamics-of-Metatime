"""Tests for tau helpers."""
from .code import CANONICAL_ORBITAL_TAU_TRIAD, effective_tau, tau_transport_factor


def test_tau_transport_factor_is_symmetric() -> None:
    sigma = 0.21
    a = tau_transport_factor(0.263, 0.353, sigma)
    b = tau_transport_factor(0.353, 0.263, sigma)
    assert abs(a - b) < 1e-12


def test_effective_tau_matches_weighted_average() -> None:
    value = effective_tau(CANONICAL_ORBITAL_TAU_TRIAD, (0.25, 0.5, 0.25))
    assert abs(value - 0.3645) < 1e-12
