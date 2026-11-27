# PyPI trusted publishing

## Registry setup

For an existing project, add a trusted publisher in its publishing settings. For a new project, create a pending publisher in the account publishing settings with the intended project name. A pending publisher does not reserve the name, and it stops working if someone else registers that name first. The first successful trusted publish creates the project and turns the publisher into a normal one. npm has nothing like this, so a new npm package needs a first publish by the owner before trust can be set up.

For GitHub, give the exact owner, repository, workflow filename, and optional environment. Use only the filename, and spell the environment exactly the same way. Set a `pypi` environment in the workflow if one is registered. For releases with no manual step, do not add required reviewers unless the user wants that control. Account setup and two-factor security stay separate from the upload authentication for each release.

TestPyPI has its own account, publisher registration, project namespace, and upload endpoint. Use it for an authorized end-to-end trial run when that fits, with `repository-url: https://test.pypi.org/legacy/` on the action and a separate environment such as `testpypi`. Do not assume that a TestPyPI success gives permission or trust on production.

## Workflow

Use a protected version-tag trigger or another deliberate release trigger. Check that the metadata and the tag agree before building. Use an explicit version policy, including how prereleases are triggered. Do not let pull requests from forks or arbitrary branches publish. Build and test in a read-only job, pass the distributions within the same workflow, and use a separate hosted Linux publish job with the official PyPA action.

1. In a build job with `contents: read`, check out with persisted credentials turned off, run Ruff and the tests, then run `uv build --no-sources`. By default it builds the sdist, and then the wheel from that sdist, into `dist/`.
2. Inspect the archives, and check metadata with Twine from the pinned release dependency group, such as `uv run --group <release-group> twine check dist/*`. Compare names and versions with the tag, run the installed-consumer checks, and upload `dist/` as a workflow artifact.
3. In a publish job that depends on the build job, set `environment: pypi`, grant `id-token: write`, download the same `dist/` and run `pypa/gh-action-pypi-publish` with no credentials.
4. Read back the release files on the project page or through the PyPI JSON API, and compare their hashes with the reviewed archives.

The action is Docker-based and runs only in GNU/Linux jobs. Self-hosted runners are best effort, so build there if needed and publish from a GitHub-hosted runner. Trusted publishing cannot run from inside a reusable workflow. Put the publish job in the calling workflow instead.

Grant `id-token: write` only to the publish job. Do not supply a username, password, or API token. The action gets short-lived upload credentials from the OIDC identity. It creates attestations by default for trusted publishing, so do not set `attestations: false` without a stated reason. Publish a source archive and a wheel together, after both have passed the checks.

Pin the action to an inspected, unchangeable revision. The documented `release/v1` reference is a branch that moves, so a full commit SHA or a tagged version is the reproducible choice. Do not rebuild packages in the privileged publish job. Do not keep repository credentials after checkout, and keep release caches out of the artifact chain. For native wheels, collect and check the exact matrix artifacts before uploading any of them.

## Diagnostics and recovery

Check that the owner, repository, workflow and environment match, and check the event identity, OIDC permission, the correct registry endpoint, the project name, and the pending-publisher status. Do not replace a trust failure with a fallback API token. Fail on a package-version clash and inspect the existing artifact hashes. Do not use `skip-existing` to hide a partial or mismatched release. Published filenames cannot simply be replaced. A bad release needs a deliberate fix through a new version. Yanking or deleting needs separate authorization.

Report the difference between a pipeline checked only locally, a TestPyPI pipeline that ran successfully, and a real production publish. Give the exact setup fields that remain when no authenticated registry session is available.
