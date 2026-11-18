# Sources

Verified: 2026-11-05.

- [Writing pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/): project metadata and backend configuration.
- [PyPI trusted publication](https://docs.pypi.org/trusted-publishers/using-a-publisher/): OIDC permissions and the official publishing action.
- [Pending publishers](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/): first-publication project creation and name-reservation limitations.
- [uv projects](https://docs.astral.sh/uv/guides/projects/) and [Ruff](https://docs.astral.sh/ruff/): dependencies and development tooling.
- [Official publication action](https://github.com/pypa/gh-action-pypi-publish): supported execution environment, attestations, and configuration.

The concrete smoke tests, versioning source, backend constraints, Python matrix, and registry trust settings are project-specific decisions.

## Professional foundation and evidence scope

Reviewed: 2026-11-05. The official [src-layout discussion](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) supports installed-consumer isolation. [Site Reliability Engineering: Release Engineering](https://sre.google/sre-book/release-engineering/) is professional context for artifact control. The guide distinguishes dynamic built metadata from an assumed static TOML version. It bundles no workflow/helper implementation.

## Trusted publishing recheck

Checked **2026-11-18**. [Using a publisher](https://docs.pypi.org/trusted-publishers/using-a-publisher/) requires job-level `id-token: write`, strongly encourages an environment such as `pypi` and needs no username, password or token with the PyPA action. [Pending publishers](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/) do not reserve a name and are invalidated if another user registers it first. The [PyPA publish action](https://github.com/pypa/gh-action-pypi-publish) runs only in GNU/Linux jobs, cannot use trusted publishing from a reusable workflow, generates attestations by default for trusted publishing, offers best-effort self-hosted support and targets TestPyPI through `repository-url: https://test.pypi.org/legacy/`. Rechecked on 2026-11-18 through the repository's README and branch list: `release/v1` is a branch alongside tags such as `v1.14.3`, and the README advises pinning tagged versions or commit SHAs instead of branch pointers. [uv build](https://docs.astral.sh/uv/concepts/projects/build/) builds the sdist first and then the wheel from it, and the [uv packaging guide](https://docs.astral.sh/uv/guides/package/) recommends `uv build --no-sources` for publication builds.

Stored content is maintained only when the user requests a revision. There is no automated source collector or refresh mechanism.
