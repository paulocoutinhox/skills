import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from module_helper import ModuleHelper
from process_helper import ProcessHelper


class RepositoryCheckTest(unittest.TestCase):
    CHECKER = ModuleHelper.load("check-repository.py").RepositoryCheckHelper

    def test_reference_links_are_checked_but_code_examples_are_ignored(self):
        content = (
            "[Guide][guide]\n\n[guide]: missing.md\n\n"
            "`[Not a link](inline.md)`\n\n```markdown\n[Example](example.md)\n```\n"
        )

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document = root / "README.md"
            document.write_text(content)

            with patch.object(self.CHECKER, "ROOT", root):
                failures = self.CHECKER.check_document(document)

        self.assertEqual(len(failures), 1)
        self.assertIn("missing.md", failures[0])

    def test_crlf_is_detected_before_universal_newline_translation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document = root / "README.md"
            document.write_bytes(b"# Title\r\n\r\nText.\r\n")

            with patch.object(self.CHECKER, "ROOT", root):
                failures = self.CHECKER.check_document(document)

        self.assertEqual(len(failures), 1)
        self.assertIn("newline", failures[0])

    def test_invalid_url_does_not_hide_independent_local_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document = root / "README.md"
            document.write_text(
                '<a href="https://[::1">Invalid</a>\n\n'
                '<a href="https://[::1]/guide">Valid external</a>\n\n'
                "[Missing](missing.md)\n"
            )

            with patch.object(self.CHECKER, "ROOT", root):
                failures = self.CHECKER.check_document(document)

        self.assertEqual(len(failures), 2)
        self.assertTrue(any("Invalid link: README.md -> https://[::1" in item for item in failures))
        self.assertTrue(any("Broken local link: README.md -> missing.md" in item for item in failures))

    def test_invalid_url_in_reference_preserves_valid_resource_routing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "skills" / "demo"
            references = skill / "references"
            references.mkdir(parents=True)
            (skill / "SKILL.md").write_text("[Guide](references/guide.md)\n")
            (references / "guide.md").write_text(
                '<a href="https://[::1">Invalid</a>\n\n[Sources](sources.md)\n'
            )
            (references / "sources.md").write_text("# Sources\n")

            with patch.object(self.CHECKER, "ROOT", root):
                failures = self.CHECKER.check_package(skill)

            expected_document = (references / "guide.md").relative_to(root)

        self.assertEqual(failures, [f"Invalid link: {expected_document} -> https://[::1"])

    def test_dangling_markdown_symlink_is_rejected_before_reading(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document = root / "README.md"
            document.symlink_to(root / "absent.md")

            with patch.object(self.CHECKER, "ROOT", root):
                failures = self.CHECKER.check_document(document)

        self.assertEqual(failures, ["Nonportable symlink: README.md"])

    def test_symbolic_entrypoint_is_rejected_before_decoding_its_target(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "skills" / "demo"
            skill.mkdir(parents=True)
            external = root / "external.md"
            external.write_bytes(b"\xff\n")
            (skill / "SKILL.md").symlink_to(external)

            with patch.object(self.CHECKER, "ROOT", root):
                failures = self.CHECKER.check_package(skill)

        self.assertEqual(failures, ["Missing or nonportable skill entrypoint: demo"])

    def test_nested_unused_resource_is_not_missed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "skills" / "demo"
            resource = skill / "references" / "nested" / "unused.md"
            resource.parent.mkdir(parents=True)
            resource.write_text("Unused material.\n")
            (skill / "SKILL.md").write_text("# Demo\n")

            with patch.object(self.CHECKER, "ROOT", root):
                failures = self.CHECKER.check_package(skill)

        self.assertEqual(len(failures), 1)
        self.assertIn("unused.md", failures[0])

    def test_linked_reference_resolves_sibling_and_asset_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "skills" / "demo"
            references = skill / "references"
            assets = skill / "assets"
            references.mkdir(parents=True)
            assets.mkdir()
            (skill / "SKILL.md").write_text("[Guide](references/guide.md)\n")
            (references / "guide.md").write_text("[Sources](sources.md)\n\n[Brief](../assets/brief.md)\n")
            (references / "sources.md").write_text("[Guide](guide.md)\n")
            (assets / "brief.md").write_text("# Brief\n")

            with patch.object(self.CHECKER, "ROOT", root):
                failures = self.CHECKER.check_package(skill)

        self.assertEqual(failures, [])

    def test_code_example_does_not_route_an_unused_resource(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "skills" / "demo"
            resource = skill / "references" / "unused.md"
            resource.parent.mkdir(parents=True)
            resource.write_text("Unused material.\n")
            (skill / "SKILL.md").write_text("# Demo\n\n```markdown\n[Example](references/unused.md)\n```\n")

            with patch.object(self.CHECKER, "ROOT", root):
                failures = self.CHECKER.check_package(skill)

        self.assertEqual(len(failures), 1)
        self.assertIn("unused.md", failures[0])

    def test_skill_cannot_link_to_collection_only_resources(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document = root / "skills" / "demo" / "SKILL.md"
            document.parent.mkdir(parents=True)
            document.write_text("[Collection](../../README.md)\n")
            (root / "README.md").write_text("# Collection\n")

            with patch.object(self.CHECKER, "ROOT", root):
                failures = self.CHECKER.check_document(document)

        self.assertEqual(len(failures), 1)
        self.assertIn("escapes", failures[0])

    def test_html_image_and_reference_image_paths_are_extracted(self):
        content = '<img src="logo.svg" alt="Logo">\n\n![Diagram][diagram]\n\n[diagram]: chart.png\n'
        self.assertEqual(set(self.CHECKER.links(content)), {"logo.svg", "chart.png"})

    def test_html_attributes_resolve_actual_targets(self):
        content = (
            '<IMG SRC = "logo&amp;mark.svg" data-src="deferred.svg" ALT="Logo" />\n\n'
            '<a href = guide.md>Guide</a>\n\n<a HREF = "missing.md">Missing guide</a>\n'
        )

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document = root / "README.md"
            document.write_text(content)
            (root / "logo&mark.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"/>\n')
            (root / "guide.md").write_text("# Guide\n")

            with patch.object(self.CHECKER, "ROOT", root):
                failures = self.CHECKER.check_document(document)

        self.assertEqual(len(failures), 1)
        self.assertIn("missing.md", failures[0])

    def test_html_comment_does_not_route_an_unused_resource(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "skills" / "demo"
            resource = skill / "assets" / "unused.svg"
            resource.parent.mkdir(parents=True)
            resource.write_text('<svg xmlns="http://www.w3.org/2000/svg"/>\n')
            (skill / "SKILL.md").write_text('<!-- <img src="assets/unused.svg"> -->\n')

            with patch.object(self.CHECKER, "ROOT", root):
                failures = self.CHECKER.check_package(skill)

        self.assertEqual(len(failures), 1)
        self.assertIn("unused.svg", failures[0])

    def test_invalid_utf8_does_not_abort_other_document_checks(self):
        for invalid in ["SKILL.md", "references/guide.md"]:
            with self.subTest(invalid=invalid), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                skill = root / "skills" / "demo"
                (skill / "references").mkdir(parents=True)
                (skill / "SKILL.md").write_text("[Guide](references/guide.md)\n")
                (skill / "references" / "guide.md").write_text("# Guide\n")
                (skill / invalid).write_bytes(b"# Invalid\n\xff\n")
                (root / "scripts").mkdir()
                (root / ".github").mkdir()

                for name in ["README.md", "AGENTS.md", "LICENSE.md"]:
                    (root / name).write_text("[Missing](missing.md)\n")

                for name in ["check-repository.py", "html-link-helper.py"]:
                    shutil.copy(ProcessHelper.ROOT / "scripts" / name, root / "scripts" / name)

                result = subprocess.run(
                    [sys.executable, str(root / "scripts" / "check-repository.py")],
                    cwd=root.parent,
                    text=True,
                    capture_output=True,
                    timeout=30,
                    check=False,
                )

                relative_document = (skill / invalid).relative_to(root)
                self.assertEqual(result.returncode, 1)
                self.assertIn(f"Invalid UTF-8 document: {relative_document}", result.stderr)
                self.assertIn("Broken local link: README.md -> missing.md", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_executable_skill_resource_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "skills" / "demo"
            script = skill / "scripts" / "count.py"
            script.parent.mkdir(parents=True)
            script.write_text("print(1)\n")
            (skill / "SKILL.md").write_text("# Demo\n")

            with patch.object(self.CHECKER, "ROOT", root):
                failures = self.CHECKER.check_package(skill)

        self.assertTrue(any("Executable content" in failure for failure in failures))
