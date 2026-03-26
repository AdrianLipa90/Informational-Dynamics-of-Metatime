from pathlib import Path
import importlib.util

MODULE_PATH = Path(__file__).resolve().parents[2] / "constants" / "tau" / "code.py"
spec = importlib.util.spec_from_file_location("tau_code", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def test_tau_transport_factor_is_symmetric() -> None:
    sigma = 0.21
    a = module.tau_transport_factor(0.263, 0.353, sigma)
    b = module.tau_transport_factor(0.353, 0.263, sigma)
    assert abs(a - b) < 1e-12


def test_effective_tau_matches_repo_zeta_value() -> None:
    value = module.effective_tau(module.CANONICAL_ORBITAL_TAU_TRIAD, (0.25, 0.25, 0.50))
    assert 0.33 < value < 0.41
