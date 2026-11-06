#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["filelock==3.32.7"]
# ///
import argparse
import os
import re
import shutil
import tempfile
from pathlib import Path

from filelock import FileLock, Timeout


class SkillInstallationHelper:
    ROOT = Path(__file__).resolve().parents[1] / "skills"

    @classmethod
    def sources(cls, selection: str) -> list[Path]:
        if selection != "all" and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", selection):
            raise ValueError("Invalid skill name.")

        sources = sorted(cls.ROOT.iterdir()) if selection == "all" else [cls.ROOT / selection]
        sources = [path for path in sources if path.is_dir() or path.is_symlink()]

        if not sources:
            raise ValueError("No matching skills were found.")

        for source in sources:
            if source.is_symlink() or not (source / "SKILL.md").is_file():
                raise ValueError(f"Not a regular skill package: {source.name}")

            for resource in source.rglob("*"):
                if resource.is_symlink():
                    raise ValueError(f"Skill resources must not be symlinks: {source.name}/{resource.name}")

        return sources

    @staticmethod
    def publish(staged: Path, destination: Path, sources: list[Path]) -> None:
        created = []
        completed = False

        try:
            for source in sources:
                target = destination / source.name
                target.mkdir()
                created.append(target)

            for source in sources:
                package = staged / source.name
                target = destination / source.name
                resources = sorted(package.iterdir(), key=lambda path: path.name == "SKILL.md")

                for resource in resources:
                    resource.rename(target / resource.name)

            completed = True
        finally:
            if not completed:
                for target in reversed(created):
                    shutil.rmtree(target)

    @classmethod
    def install(cls, selection: str, destination: Path) -> list[Path]:
        if os.name not in {"posix", "nt"}:
            raise ValueError("Installation requires a supported native filesystem-lock platform.")

        sources = cls.sources(selection)
        destination = destination.expanduser().absolute()

        if destination.is_symlink() or destination.resolve().is_relative_to(cls.ROOT.resolve()):
            raise ValueError("The destination must be a separate directory, not a symlink or source package.")

        destination.parent.mkdir(parents=True, exist_ok=True)
        lock_path = destination.parent / f".{destination.name}.paulo-skills.lock"

        with FileLock(lock_path, timeout=0):
            for source in sources:
                target = destination / source.name

                if target.exists() or target.is_symlink():
                    raise FileExistsError(f"Destination already exists: {target}")

            destination.mkdir(exist_ok=True)

            with tempfile.TemporaryDirectory(prefix=".paulo-skills-", dir=destination.parent) as directory:
                staged = Path(directory)

                for source in sources:
                    shutil.copytree(source, staged / source.name)

                cls.publish(staged, destination, sources)

        return [destination / source.name for source in sources]

    @classmethod
    def run(cls) -> None:
        parser = argparse.ArgumentParser(
            description="Install complete skills without overwriting user files."
        )
        parser.add_argument("client", choices=["codex", "claude"])
        parser.add_argument("selection", nargs="?", default="all")
        parser.add_argument("--destination", type=Path)
        arguments = parser.parse_args()
        client_directory = ".agents" if arguments.client == "codex" else ".claude"
        destination = arguments.destination or Path.home() / client_directory / "skills"

        try:
            installed = cls.install(arguments.selection, destination)
        except Timeout:
            parser.exit(1, "Another installation is using this destination. Retry after it finishes.\n")
        except (OSError, ValueError) as error:
            parser.exit(1, f"Installation failed: {error}\n")

        for path in installed:
            print(f"Installed {path.name} into {path}")


if __name__ == "__main__":
    SkillInstallationHelper.run()
