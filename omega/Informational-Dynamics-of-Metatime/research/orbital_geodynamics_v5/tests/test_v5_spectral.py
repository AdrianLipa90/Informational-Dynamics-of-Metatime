from registry import load_system
from metrics import spectral_observables
from pathlib import Path


def test_spectral_observables_exist():
    root = Path(__file__).resolve().parents[1]
    system = load_system(root/'config'/'sectors_real_v4.json', root/'config'/'couplings_real_v4.json')
    spec = spectral_observables(system)
    assert 'spectral_radius_A' in spec
    assert 'fiedler_L' in spec
    assert spec['spectral_radius_A'] >= 0.0
    assert spec['fiedler_L'] >= 0.0
