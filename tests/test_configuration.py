import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import editorconfig
from process_helper import ProcessHelper


class ConfigurationTest(unittest.TestCase):
    def test_editorconfig_template_preserves_sensitive_whitespace(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            template = ProcessHelper.ROOT / "skills/editor-config/assets/editorconfig"
            shutil.copy(template, root / ".editorconfig")

            for name, expected in [("app.py", "4"), ("app.ts", "2"), ("config.yaml", "2")]:
                properties = editorconfig.get_properties(str(root / name))
                self.assertEqual(properties["indent_size"], expected)

            self.assertEqual(editorconfig.get_properties(str(root / "Makefile"))["indent_style"], "tab")
            self.assertEqual(editorconfig.get_properties(str(root / "main.go"))["indent_style"], "tab")
            markdown = editorconfig.get_properties(str(root / "guide.md"))
            self.assertEqual(markdown["trim_trailing_whitespace"], "false")

    def test_ignore_template_excludes_artifacts_but_keeps_sources(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "--quiet", str(root)], check=True, capture_output=True)
            shutil.copy(ProcessHelper.ROOT / "skills/git-ignore/assets/gitignore", root / ".gitignore")

            ignored = [
                ".env",
                ".env.production",
                ".venv/lib/module.py",
                "node_modules/pkg/index.js",
                "dist/bundle.js",
                "runtime.log",
                "credentials.json",
                "signing/AuthKey_test.p8",
                "signing/release.jks",
                "signing/release.mobileprovision",
                "playwright/.auth/user.json",
                "apps/web/playwright/.auth/user.json",
                ".DS_Store",
            ]
            retained = [
                "src/module.py",
                "uv.lock",
                "package-lock.json",
                ".env.example",
                "assets/logo.svg",
                "docs/layout.pdf",
                "tests/fixtures/auth-response.json",
                "src/auth/session.py",
            ]

            for path, expected in [(path, 0) for path in ignored] + [(path, 1) for path in retained]:
                result = subprocess.run(
                    ["git", "-C", str(root), "check-ignore", "--no-index", "-q", path],
                    check=False,
                    capture_output=True,
                )
                self.assertEqual(result.returncode, expected, path)

    def test_nested_editorconfig_overrides_without_changing_other_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".editorconfig").write_text(
                "root = true\n[*]\nindent_style = space\nindent_size = 4\n"
                "[*.md]\ntrim_trailing_whitespace = false\n"
            )
            nested = root / "web"
            nested.mkdir()
            (nested / ".editorconfig").write_text("[*.json]\nindent_size = 2\n")
            self.assertEqual(editorconfig.get_properties(str(nested / "config.json"))["indent_size"], "2")
            self.assertEqual(editorconfig.get_properties(str(root / "config.json"))["indent_size"], "4")
            self.assertEqual(
                editorconfig.get_properties(str(nested / "guide.md"))["trim_trailing_whitespace"], "false"
            )

    def test_ignored_parent_prevents_a_file_only_negation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "--quiet", str(root)], check=True, capture_output=True)
            rules = root / ".gitignore"
            rules.write_text("assets/\n!assets/logo.svg\n")
            result = subprocess.run(
                ["git", "-C", str(root), "check-ignore", "--no-index", "-q", "assets/logo.svg"],
                check=False,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0)
            rules.write_text("assets/*\n!assets/logo.svg\n")
            result = subprocess.run(
                ["git", "-C", str(root), "check-ignore", "--no-index", "-q", "assets/logo.svg"],
                check=False,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 1)
