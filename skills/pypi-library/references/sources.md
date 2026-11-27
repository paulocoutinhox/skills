# Sources

Checked: 2026-11-05.

- [Writing pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/): project metadata and backend configuration.
- [PyPI trusted publication](https://docs.pypi.org/trusted-publishers/using-a-publisher/): OIDC permissions and the official publishing action.
- [Pending publishers](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/): creating the project on the first publish, and the limits on reserving names.
- [uv projects](https://docs.astral.sh/uv/guides/projects/) and [Ruff](https://docs.astral.sh/ruff/): dependencies and development tools.
- [Official publication action](https://github.com/pypa/gh-action-pypi-publish): supported run environment, attestations, and configuration.

The specific smoke tests, version source, backend limits, Python matrix, and registry trust settings are decisions for each project.

## Professional foundation and evidence scope

Reviewed: 2026-11-05. The official [src-layout discussion](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) supports testing an installed consumer in isolation. [Site Reliability Engineering: Release Engineering](https://sre.google/sre-book/release-engineering/) gives professional background on controlling artifacts. The guide tells apart dynamic built metadata and an assumed static TOML version. It bundles no workflow or helper code.

## Trusted publishing recheck

Checked **2026-11-18**. [Using a publisher](https://docs.pypi.org/trusted-publishers/using-a-publisher/) requires job-level `id-token: write`, strongly encourages an environment such as `pypi`, and needs no username, password or token with the PyPA action. [Pending publishers](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/) do not reserve a name, and they stop working if another user registers it first. The [PyPA publish action](https://github.com/pypa/gh-action-pypi-publish) runs only in GNU/Linux jobs and cannot use trusted publishing from a reusable workflow. It creates attestations by default for trusted publishing, offers best-effort self-hosted support, and targets TestPyPI through `repository-url: https://test.pypi.org/legacy/`. Checked again on 2026-11-18 through the repository's README and branch list: `release/v1` is a branch next to tags such as `v1.14.3`, and the README advises pinning tagged versions or commit SHAs instead of branch pointers. [uv build](https://docs.astral.sh/uv/concepts/projects/build/) builds the sdist first and then the wheel from it, and the [uv packaging guide](https://docs.astral.sh/uv/guides/package/) recommends `uv build --no-sources` for publish builds.

Stored content is updated only when the user asks for a revision. There is no automatic source collector or refresh mechanism.
