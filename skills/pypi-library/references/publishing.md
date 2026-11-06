# PyPI trusted publishing

## Registry setup

For an existing project, add a trusted publisher in its publishing settings. For a new project, create a pending publisher in account publishing settings with the intended project name. A pending publisher does not reserve the name. The first successful trusted publication creates the project and converts the publisher to a normal one.

For GitHub, provide the exact owner, repository, workflow filename, and optional environment. Use only the filename, and keep environment spelling identical. Set a `pypi` environment in the workflow if registered. For no-intervention releases, do not add required reviewers unless the user wants that control. Account setup and two-factor security remain distinct from per-release upload authentication.

TestPyPI has a separate account, publisher registration, project namespace, and upload endpoint. Use it for an authorized end-to-end rehearsal when appropriate. Do not assume a TestPyPI success grants permission or trust on production.

## Workflow

Run a protected version-tag or other deliberate release trigger. Verify metadata/tag agreement before building. Use an explicit version policy, including how prereleases are triggered. Do not let fork PRs or arbitrary branches publish. Build and test in a read-only job, transfer distributions within the same workflow, and use a separate hosted Linux publish job with the official PyPA action.

Grant `id-token: write` only to the publish job. Do not supply username, password, or API token. The action obtains short-lived upload credentials from the OIDC identity. Keep artifact attestations enabled where supported. A source archive and wheel should be published together after both have passed checks.

Pin the action by an inspected immutable revision. Do not rebuild packages in the privileged publish job. Keep repository credentials unpersisted and release caches out of the artifact chain. For native wheels, gather and verify the exact matrix artifacts before uploading any of them.

## Diagnostics and recovery

Check owner/repository/workflow/environment matching, event identity, OIDC permission, correct registry endpoint, project name, and pending-publisher status. Do not replace a trust failure with a fallback API token. Fail on a package-version collision and inspect existing artifact hashes. Do not use `skip-existing` to conceal a partial or mismatched release. Published filenames cannot simply be replaced. A bad release requires a deliberate corrective version, and yanking or deletion requires separate authorization.

Report the distinction between a locally validated pipeline, a successfully exercised TestPyPI pipeline, and an actual production publication. Provide exact remaining setup fields when an authenticated registry session is unavailable.
