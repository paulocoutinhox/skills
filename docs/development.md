# Development

## Validate locally and in CI

Use `make help` to list the contributor commands. `make setup` installs the locked environment.
`make validate` (also `make valide`) runs skills-ref, the repository checks, contributor tests, Ruff
lint, and format checks. CI uses the same `make validate` target on pushes to `main`.

Install [uv](https://docs.astral.sh/uv/) and Python 3.11 or later, then run:

```bash
uv sync --locked
uv run --locked python scripts/validate-skills.py
```

The Python wrapper runs the official **skills-ref** command for every skill, locally and in CI. It
fails the same way in both places:

```bash
skills-ref validate skills/code-review
```

`pyproject.toml` and `uv.lock` pin the upstream revision and the exact tool dependencies. CI runs
on pushes to `main` and when started by hand. It also checks local links and how resources are
packaged, Python lint and formatting, the rules for text-only skill packages, and how the
contributor tools behave. It uses no model and no model API credentials. Format checks cover the
skill structure and metadata. They do not prove that the domain content is correct or how a model
will behave. Once the tools are installed, the checks work offline. The first dependency install
needs network access.

Run all repository checks with `make validate`. The general rules for writing, research, structure
and checks are in [AGENTS.md](../AGENTS.md).

## Organization

```text
skills/       Portable skill directories and their own resources
docs/         Installation, usage, development and task prompt documentation
scripts/      Repository validation commands
tests/        Contributor-tool behavior and packaging checks
extras/       Editable vector logo and project assets
.github/      Validation CI, issue templates, funding, and release notes template
AGENTS.md     Current authoring, architecture, and development contract
```

Each skill keeps its resources inside its own folder, so a skill still works when installed alone.
A skill does not need empty resource folders just to match the layout above. App code that runs in
a user's project and a vendor's own command are not the same as automation bundled in a skill.
