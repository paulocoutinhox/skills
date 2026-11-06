import tempfile
import unittest
from pathlib import Path

from process_helper import ProcessHelper


class InstallerTest(unittest.TestCase):
    def test_complete_independent_installation(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "skills with spaces"
            result = ProcessHelper.install(destination)
            self.assertEqual(result.returncode, 0, result.stderr)

            for source in (ProcessHelper.ROOT / "skills").iterdir():
                for source_file in source.rglob("*"):
                    if source_file.is_file():
                        installed = destination / source.name / source_file.relative_to(source)
                        self.assertEqual(installed.read_bytes(), source_file.read_bytes())

    def test_existing_destination_stops_before_any_copy(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory)
            existing = destination / "social-post"
            existing.mkdir()
            sentinel = existing / "keep.txt"
            sentinel.write_text("User content.")
            result = ProcessHelper.install(destination)

            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(sentinel.read_text(), "User content.")
            self.assertEqual(list(destination.iterdir()), [existing])

    def test_invalid_name_cannot_escape_source_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            result = ProcessHelper.install(Path(directory), "../docs")
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_unknown_skill_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            result = ProcessHelper.install(Path(directory), "nonexistent-skill")
            self.assertNotEqual(result.returncode, 0)

    def test_dangling_destination_link_is_not_followed(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory)
            (destination / "git").symlink_to(destination / "absent")
            result = ProcessHelper.install(destination, "git")
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse((destination / "absent").exists())
