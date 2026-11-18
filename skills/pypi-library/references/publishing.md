# PyPI trusted publishing

## Registry setup

For an existing project, add a trusted publisher in its publishing settings. For a new project, create a pending publisher in account publishing settings with the intended project name. A pending publisher does not reserve the name, and it is invalidated if someone else registers that name first. The first successful trusted publication creates the project and converts the publisher to a normal one. npm has no equivalent, so a new npm package needs a first owner publication before trust can be configured.

For GitHub, provide the exact owner, repository, workflow filename, and optional environment. Use only the filename, and keep environment spelling identical. Set a `pypi` environment in the workflow if registered. For no-intervention releases, do not add required reviewers unless the user wants that control. Account setup and two-factor security remain distinct from per-release upload authentication.

TestPyPI has a separate account, publisher registration, project namespace, and upload endpoint. Use it for an authorized end-to-end rehearsal when appropriate, with `repository-url: https://test.pypi.org/legacy/` on the action and a separate environment such as `testpypi`. Do not assume a TestPyPI success grants permission or trust on production.

## Workflow

Run a protected version-tag or other deliberate release trigger. Verify metadata/tag agreement before building. Use an explicit version policy, including how prereleases are triggered. Do not let fork PRs or arbitrary branches publish. Build and test in a read-only job, transfer distributions within the same workflow, and use a separate hosted Linux publish job with the official PyPA action.

1. In a build job with `contents: read`, check out with persisted credentials disabled, run Ruff and the tests, then run `uv build --no-sources`. By default it builds the sdist and then the wheel from that sdist into `dist/`.
2. Inspect the archives, check metadata with Twine from the pinned release dependency group, such as `uv run --group <release-group> twine check dist/*`, compare names and versions with the tag, run the installed-consumer checks and upload `dist/` as a workflow artifact.
3. In a publish job that depends on the build job, set `environment: pypi`, grant `id-token: write`, download the same `dist/` and run `pypa/gh-action-pypi-publish` with no credentials.
4. Read back the release files on the project page or the PyPI JSON API and compare their hashes with the reviewed archives.

The action is Docker-based and runs only in GNU/Linux jobs. Self-hosted runners are best effort, so build there if needed and publish from a GitHub-hosted runner. Trusted publishing cannot run from inside a reusable workflow. Put the publish job in the calling workflow instead.

Grant `id-token: write` only to the publish job. Do not supply username, password, or API token. The action obtains short-lived upload credentials from the OIDC identity. It generates attestations by default for trusted publishing, so do not set `attestations: false` without a stated reason. A source archive and wheel should be published together after both have passed checks.

Pin the action by an inspected immutable revision. The documented `release/v1` reference is a moving branch, so a full commit SHA or tagged version is the reproducible choice. Do not rebuild packages in the privileged publish job. Keep repository credentials unpersisted and release caches out of the artifact chain. For native wheels, gather and verify the exact matrix artifacts before uploading any of them.

## Diagnostics and recovery

Check owner/repository/workflow/environment matching, event identity, OIDC permission, correct registry endpoint, project name, and pending-publisher status. Do not replace a trust failure with a fallback API token. Fail on a package-version collision and inspect existing artifact hashes. Do not use `skip-existing` to conceal a partial or mismatched release. Published filenames cannot simply be replaced. A bad release requires a deliberate corrective version, and yanking or deletion requires separate authorization.

Report the distinction between a locally validated pipeline, a successfully exercised TestPyPI pipeline, and an actual production publication. Provide exact remaining setup fields when an authenticated registry session is unavailable.
