#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["markdown-it-py==4.2.0"]
# ///
from importlib import import_module
from pathlib import Path
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt

HtmlLinkHelper = import_module("html-link-helper").HtmlLinkHelper


class RepositoryCheckHelper:
    ROOT = Path(__file__).resolve().parents[1]
    EXECUTABLE_SUFFIXES = {".py", ".sh", ".bash", ".zsh", ".js", ".cjs", ".mjs", ".ps1", ".bat", ".cmd"}

    @classmethod
    def links(cls, content: str) -> list[str]:
        links = []
        pending = list(MarkdownIt("commonmark").enable("table").parse(content))

        while pending:
            token = pending.pop()

            if token.type == "link_open":
                links.append(token.attrGet("href"))

            if token.type == "image":
                links.append(token.attrGet("src"))

            if token.type in {"html_inline", "html_block"}:
                links.extend(HtmlLinkHelper.links(token.content))

            if token.children:
                pending.extend(token.children)

        return links

    @classmethod
    def local_targets(cls, document: Path, content: str) -> tuple[list[tuple[str, Path]], list[str]]:
        targets = []
        failures = []

        for raw in cls.links(content):
            try:
                parsed = urlsplit(raw)
            except ValueError:
                relative = document.resolve().relative_to(cls.ROOT.resolve())
                failures.append(f"Invalid link: {relative} -> {raw}")
                continue

            if parsed.scheme or parsed.netloc or not parsed.path:
                continue

            target = (document.parent / unquote(parsed.path)).resolve()
            targets.append((raw, target))

        return targets, failures

    @classmethod
    def check_document(cls, document: Path) -> list[str]:
        failures = []
        relative = document.relative_to(cls.ROOT)

        if document.is_symlink():
            return [f"Nonportable symlink: {relative}"]

        try:
            content = document.read_bytes().decode("utf-8")
        except UnicodeError:
            return [f"Invalid UTF-8 document: {relative}"]

        if "\r" in content or not content.endswith("\n"):
            failures.append(f"Invalid text newline policy: {relative}")

        targets, link_failures = cls.local_targets(document, content)
        failures.extend(link_failures)

        for raw, target in targets:
            if not target.is_relative_to(cls.ROOT.resolve()) or not target.exists():
                failures.append(f"Broken local link: {relative} -> {raw}")

            if relative.parts[0] == "skills":
                skill_root = cls.ROOT / "skills" / relative.parts[1]

                if not target.is_relative_to(skill_root.resolve()):
                    failures.append(f"Skill link escapes its package: {relative} -> {raw}")

        return failures

    @classmethod
    def check_package(cls, skill: Path) -> list[str]:
        failures = []
        entrypoint = skill / "SKILL.md"

        if skill.is_symlink() or entrypoint.is_symlink() or not entrypoint.is_file():
            return [f"Missing or nonportable skill entrypoint: {skill.name}"]

        if len(entrypoint.read_text(encoding="utf-8").splitlines()) >= 500:
            failures.append(f"Entrypoint exceeds the project limit: {skill.name}")

        resources = []
        has_symlinks = False

        for path in skill.rglob("*"):
            relative = path.relative_to(skill)

            if path.is_symlink():
                failures.append(f"Nonportable symlink: {path.relative_to(cls.ROOT)}")
                has_symlinks = True
                continue

            if path.is_dir() and not any(path.iterdir()):
                failures.append(f"Empty resource directory: {path.relative_to(cls.ROOT)}")

            if relative.parts[0] == "scripts" or path.suffix in cls.EXECUTABLE_SUFFIXES:
                failures.append(f"Executable content in descriptive skill: {path.relative_to(cls.ROOT)}")

            if path.is_file() and relative.parts[0] in {"references", "assets"}:
                resources.append(path.resolve())

        if has_symlinks:
            return failures

        reachable = set()
        pending = [entrypoint.resolve()]

        while pending:
            current = pending.pop()

            if current in reachable:
                continue

            reachable.add(current)

            if current.suffix != ".md":
                continue

            targets, link_failures = cls.local_targets(current, current.read_text(encoding="utf-8"))
            failures.extend(link_failures)

            for _, target in targets:
                if target.is_file() and target.is_relative_to(skill.resolve()):
                    pending.append(target)

        for resource in resources:
            if resource not in reachable:
                failures.append(f"Unrouted skill resource: {resource.relative_to(cls.ROOT.resolve())}")

        return failures

    @classmethod
    def run(cls) -> None:
        failures = []
        skills = sorted(path for path in (cls.ROOT / "skills").iterdir() if path.is_dir())

        if not skills:
            failures.append("No skills were found.")

        for skill in skills:
            try:
                failures.extend(cls.check_package(skill))
            except UnicodeError:
                failures.append(f"Invalid UTF-8 skill package: {skill.name}")

        for path in (cls.ROOT / "scripts").iterdir():
            if path.is_file() and path.suffix != ".py":
                failures.append(f"Contributor scripts must be Python: {path.name}")

        documents = [cls.ROOT / name for name in ["README.md", "AGENTS.md", "LICENSE.md"]]

        for directory in ["skills", ".github"]:
            documents.extend((cls.ROOT / directory).rglob("*.md"))

        for document in documents:
            failures.extend(cls.check_document(document))

        if failures:
            raise SystemExit("\n".join(dict.fromkeys(failures)))

        print(f"Checked {len(skills)} descriptive skill packages and {len(documents)} Markdown files.")


if __name__ == "__main__":
    RepositoryCheckHelper.run()
