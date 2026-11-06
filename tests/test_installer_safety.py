import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from filelock import FileLock
from module_helper import ModuleHelper
from process_helper import ProcessHelper


class InstallerSafetyTest(unittest.TestCase):
    INSTALLER = ModuleHelper.load("install-skills.py").SkillInstallationHelper

    def test_concurrent_installers_do_not_overwrite_or_nest_packages(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "installed"
            command = [
                sys.executable,
                str(ProcessHelper.ROOT / "scripts/install-skills.py"),
                "codex",
                "git",
                "--destination",
                str(destination),
            ]
            processes = [
                subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE) for _ in range(2)
            ]
            results = [process.communicate(timeout=30) for process in processes]
            self.assertEqual(sorted(process.returncode for process in processes), [0, 1], results)
            expected = ProcessHelper.ROOT / "skills" / "git" / "SKILL.md"
            self.assertEqual((destination / "git" / "SKILL.md").read_bytes(), expected.read_bytes())
            self.assertFalse((destination / "git" / "git").exists())

    def test_active_destination_lock_fails_without_copying(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "installed"
            lock = destination.parent / f".{destination.name}.paulo-skills.lock"

            with FileLock(lock):
                result = ProcessHelper.install(destination, "git")

            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(destination.exists())

    def test_source_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "source" / "demo"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("# Demo\n")
            secret = root / "private.txt"
            secret.write_text("Private fixture.\n")
            (skill / "copied.txt").symlink_to(secret)

            with patch.object(self.INSTALLER, "ROOT", skill.parent):
                with self.assertRaisesRegex(ValueError, "symlinks"):
                    self.INSTALLER.install("demo", root / "installed")

            self.assertFalse((root / "installed").exists())

    def test_staging_failure_preserves_preexisting_content(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "installed"
            destination.mkdir()
            sentinel = destination / "keep.txt"
            sentinel.write_text("User file.\n")

            with patch.object(shutil, "copytree", side_effect=OSError("Fixture copy failure.")):
                with self.assertRaises(OSError):
                    self.INSTALLER.install("git", destination)

            self.assertEqual(list(destination.iterdir()), [sentinel])
            self.assertEqual(sentinel.read_text(), "User file.\n")

    def test_publish_failure_rolls_back_only_new_package_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            destination = root / "installed"
            destination.mkdir()
            sentinel = destination / "keep.txt"
            sentinel.write_text("Keep.\n")
            staged = root / "staged"
            sources = [Path("alpha"), Path("beta")]

            for source in sources:
                package = staged / source.name
                package.mkdir(parents=True)
                (package / "SKILL.md").write_text("# Example\n")

            original = Path.rename
            completed = 0

            def rename(path, target):
                nonlocal completed
                completed += 1

                if completed == 2:
                    raise OSError("Fixture publication failure.")

                return original(path, target)

            with patch.object(Path, "rename", rename):
                with self.assertRaises(OSError):
                    self.INSTALLER.publish(staged, destination, sources)

            self.assertEqual(list(destination.iterdir()), [sentinel])
            self.assertEqual(sentinel.read_text(), "Keep.\n")
