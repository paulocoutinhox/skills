import subprocess
import sys
from pathlib import Path


class ProcessHelper:
    ROOT = Path(__file__).resolve().parents[1]

    @classmethod
    def python(cls, script: str, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(cls.ROOT / script), *arguments],
            text=True,
            capture_output=True,
            check=False,
            timeout=30,
        )

    @classmethod
    def install(cls, destination: Path, selection: str = "all") -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(cls.ROOT / "scripts/install-skills.py"),
                "codex",
                selection,
                "--destination",
                str(destination),
            ],
            text=True,
            capture_output=True,
            check=False,
            timeout=30,
        )
