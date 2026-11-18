# Automatic trusted publication

## One-time registry setup

Confirm package ownership and the registry's supported bootstrap path. npm trust is configured on an existing package, and the `npm trust` documentation states that the package must already exist on the registry. npm has no pending publisher equivalent to PyPI's. For a brand-new name, the owner performs the first publication through an authorized interactive path, such as `npm login` and `npm publish` with account 2FA, or explicitly authorizes another path. Then configure trust. Report that first publication as a separate owner step. Never silently fall back to a long-lived token in CI.

For GitHub Actions, register the exact owner, repository, workflow filename including `.yml` or `.yaml`, and environment if selected. The filename is not the full workflow path, and the file must live in `.github/workflows/`. Configure it in the package settings on npmjs.com or with `npm trust github <package> --file <workflow.yml> --repo <owner>/<repo> --env <environment> --allow-publish`, which requires npm 11.15.0 or later, account 2FA and write access to the package. Use `--allow-stage-publish` instead when the release should be staged for approval. Keep the environment name identical in the registry and the workflow.

Allowed actions are independent. `npm stage publish` is always allowed from the web form, while direct `npm publish` must be selected explicitly, or passed as `--allow-publish` to `npm trust`. A staged publication stays unavailable until a maintainer approves it with interactive 2FA through `npm stage approve` or the website. OIDC tokens cannot approve it. Select direct publication for an explicitly requested no-intervention release path. For fully automatic releases, do not add an unrequested required-reviewer gate.

A new trust configuration must complete its first successful publication within two days, or it expires and can no longer be used or edited. Schedule the first trusted release inside that window and verify it.

Use the current npm 12 line. npm 12 requires Node `^22.22.2`, `^24.15.0` or `>=26.0.0`, which is above trusted publishing's documented floor of npm 11.5.1 with Node 22.14.0. Managing dist-tags through OIDC needs npm 12.2.0 or later. The npm documentation's GitHub example uses Node 24 through `actions/setup-node`. The npm bundled with a Node release can be older than 12, so install the pinned npm 12 release and print both versions in the job log. Trusted publishing supports GitHub Actions, GitLab CI/CD and CircleCI on cloud-hosted runners only. Self-hosted runners are not supported. The described identity tuple targets GitHub Actions. Other providers require their actual supported configuration.

## Workflow outline

1. Trigger on the selected protected release event, such as a pushed `v*` tag.
2. In a verify job with `contents: read`, check out with persisted credentials disabled, set up Node with `registry-url: https://registry.npmjs.org`, install the pinned npm 12 release with `npm install -g npm@<version>`, print `node --version` and `npm --version`, then run `npm ci`, the build, lint/type checks and tests. The publish job installs the same npm version.
3. Compare the tag with `package.json` version, run `npm pack --json`, inspect the file list and upload the tarball as a workflow artifact. Read the JSON fields that npm 12 prints, because its `pack` and `publish` JSON shape differs from npm 11.
4. In a publish job that depends on the verify job, use the registered environment and grant `id-token: write` with `contents: read`. Download the exact tarball and confirm its integrity matches the verify job's record.
5. Run `npm publish <name>-<version>.tgz --ignore-scripts`, adding `--access public` only when a scoped package is intended to be public. When staging was selected instead, run `npm stage publish <name>-<version>.tgz --ignore-scripts` and report the version as staged until a maintainer approves it. Without an argument, `npm stage publish` packs the current working directory, which would bypass the reviewed tarball. Its synopsis takes a `<package-spec>`, and npm's package-spec definition includes a local tarball file such as `./my-package.tgz`. `npm stage publish` defers 2FA to approval. Read the stage ID it reports, compare the staged artifact through `npm stage view <stage-id>` or `npm stage download <stage-id>` with the reviewed integrity, and stop rather than repack in the publish job if the CLI rejects the tarball. A maintainer then runs `npm stage approve <stage-id>` with 2FA, or `npm stage reject <stage-id>`.
6. Read back the result with `npm view <name>@<version> dist.integrity` and compare it with the reviewed tarball. Check provenance on the package page when it is expected.

## Release boundaries

Use a protected version-tag trigger or another explicit authenticated release policy. PRs and arbitrary forks must never receive publish capability. Validate the tag against manifest version using environment variables, not shell interpolation of untrusted event text. Require the version to be new. Document whether release versions are changed by a release bot or an explicit version commit. A CI pipeline must not invent version increments from prose without a chosen policy.

Give only the publish job `id-token: write`. Build and test in a job with read-only repository access. Pin action references, do not persist checkout credentials, avoid release-build caches, transfer the reviewed artifact within the same workflow, and do not execute untrusted PR code in a privileged context. OIDC authorization does not make package lifecycle code safe.

Publish the tarball with lifecycle scripts disabled after build and tests have completed. Use public access when intended. Set repository metadata correctly and verify provenance support for the actual repository/package visibility. Trusted publication generates provenance automatically only from a public repository for a public package, on GitHub Actions or GitLab CI/CD. CircleCI trusted publication does not generate it. Do not claim private-repository provenance from that baseline.

## Failure and recovery

For OIDC errors, inspect the exact identity tuple, environment, workflow name, permissions, supported runner, package ownership, Node/npm versions, and allowed-action setting. Remove accidental `NODE_AUTH_TOKEN` or `.npmrc` write credentials rather than allowing token fallback. A private-dependency read token, if necessary, must be scoped separately and absent from publication.

If the registry reports the version already exists, compare its integrity with the intended artifact before deciding anything. Never overwrite or unpublish automatically. If it is identical, report the existing release. If it differs or publication was incorrect, follow the registry's supported corrective policy and release a new version. Do not retry endlessly or fabricate success. After OIDC publication is verified and the user authorizes the account change, the owner can select "Require two-factor authentication and disallow tokens" under the package's publishing access settings and revoke superseded automation tokens.
