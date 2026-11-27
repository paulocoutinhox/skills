#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["skills-ref @ git+https://github.com/agentskills/agentskills.git@83021e2be457a9b6679148719c1f6074f0ad975e#subdirectory=skills-ref"]
# ///
import shutil
import subprocess
from pathlib import Path


class SkillValidationHelper:
    @staticmethod
    def run() -> int:
        root = Path(__file__).resolve().parents[1]
        executable = shutil.which("skills-ref")

        if executable is None:
            raise SystemExit("skills-ref is missing. Run through the locked uv environment.")

        skills = sorted(path for path in (root / "skills").iterdir() if path.is_dir())

        if not skills:
            raise SystemExit("No skills were found.")

        for skill in skills:
            result = subprocess.run([executable, "validate", str(skill)], cwd=root, check=False)

            if result.returncode:
                return result.returncode

        return 0


if __name__ == "__main__":
    raise SystemExit(SkillValidationHelper.run())
