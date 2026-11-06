# Sources

Verified: 2026-11-05.

- [Writing pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/): project metadata and backend configuration.
- [PyPI trusted publication](https://docs.pypi.org/trusted-publishers/using-a-publisher/): OIDC permissions and the official publishing action.
- [Pending publishers](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/): first-publication project creation and name-reservation limitations.
- [uv projects](https://docs.astral.sh/uv/guides/projects/) and [Ruff](https://docs.astral.sh/ruff/): dependencies and development tooling.
- [Official publication action](https://github.com/pypa/gh-action-pypi-publish): supported execution environment, attestations, and configuration.

The concrete smoke tests, versioning source, backend constraints, Python matrix, and registry trust settings are project-specific decisions.

## Professional foundation and evidence scope

Reviewed for this revision: 2026-11-05. The official [src-layout discussion](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) supports installed-consumer isolation. [Site Reliability Engineering: Release Engineering](https://sre.google/sre-book/release-engineering/) is professional context for artifact control. The expanded guide distinguishes dynamic built metadata from an assumed static TOML version. It bundles no workflow/helper implementation.

Stored content is maintained only when the user requests a revision. There is no automated source collector or refresh mechanism.
