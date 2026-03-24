from pathlib import Path
import importlib.util


def _load_module(path: Path):
    spec = importlib.util.spec_from_file_location("public_relational_contract", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_top_level_relational_contract_loads_default_yaml():
    path = Path(__file__).resolve().parents[1] / "configs" / "relational_contract.py"
    module = _load_module(path)
    obj = module.RelationalContract()
    assert list(obj.tau) == [0.263, 0.353, 0.489]


def test_runtime_relational_contract_loads_default_yaml():
    path = Path(__file__).resolve().parent / "configs" / "relational_contract.py"
    module = _load_module(path)
    obj = module.RelationalContract()
    assert obj.euler_check(obj.gamma) >= 0.0
