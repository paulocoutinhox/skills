import importlib.util
import sys
from pathlib import Path
from unittest.mock import patch


class ModuleHelper:
    @staticmethod
    def load(name: str):
        path = Path(__file__).resolve().parents[1] / "scripts" / name
        specification = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
        module = importlib.util.module_from_spec(specification)

        with patch.object(sys, "path", [str(path.parent), *sys.path]):
            specification.loader.exec_module(module)

        return module
