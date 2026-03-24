from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[4]


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_code_map_has_multiple_records():
    data = load_yaml(ROOT / 'systems/CIEL_FOUNDATIONS/derivations/code_map.yaml')
    assert 'records' in data
    assert len(data['records']) >= 5


def test_diff_registry_is_not_empty():
    data = load_yaml(ROOT / 'systems/CIEL_FOUNDATIONS/verification/diff_registry.yaml')
    assert 'records' in data
    assert len(data['records']) >= 5


def test_operator_registry_has_expected_objects():
    data = load_yaml(ROOT / 'systems/CIEL_FOUNDATIONS/definitions/operators/registry.yaml')
    ids = {record['id'] for record in data['records']}
    assert {'OP-0100', 'OP-0101', 'OP-0102', 'OP-0103', 'OP-0104'} <= ids


def test_sector_registry_has_five_sectors():
    data = load_yaml(ROOT / 'systems/CIEL_FOUNDATIONS/sectors/registry.yaml')
    sectors = {record['sector'] for record in data['records']}
    assert sectors == {'neutrino', 'lepton', 'quark', 'hadron', 'cosmology'}
