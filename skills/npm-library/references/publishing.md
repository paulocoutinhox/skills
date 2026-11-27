# Automatic trusted publication

## One-time registry setup

Confirm who owns the package and the registry's supported path for the first publish. npm trust is set up on an existing package, and the `npm trust` documentation says the package must already exist on the registry. npm has nothing like PyPI's pending publisher. For a brand-new name, the owner does the first publish through an authorized interactive path, such as `npm login` and `npm publish` with account 2FA, or explicitly authorizes another path. Then set up trust. Report that first publish as a separate owner step. Never quietly fall back to a long-lived token in CI.

For GitHub Actions, register the exact owner, repository, workflow filename including `.yml` or `.yaml`, and environment if one is chosen. The filename is not the full workflow path, and the file must live in `.github/workflows/`. Set it up in the package settings on npmjs.com or with `npm trust github <package> --file <workflow.yml> --repo <owner>/<repo> --env <environment> --allow-publish`, which requires account 2FA and write access to the package. Use `--allow-stage-publish` instead when the release should be staged for approval. Use exactly the same environment name in the registry and the workflow.

Allowed actions are set separately. `npm stage publish` is always allowed from the web form, while direct `npm publish` must be chosen explicitly, or passed as `--allow-publish` to `npm trust`. A staged publish stays unavailable until a maintainer approves it with interactive 2FA through `npm stage approve` or the website. OIDC tokens cannot approve it. Choose direct publishing when the user explicitly asks for a release path with no manual step. For fully automatic releases, do not add a required-reviewer gate nobody asked for.

A new trust configuration must finish its first successful publish within two days. Otherwise it expires and can no longer be used or edited. Schedule the first trusted release inside that window and check it.

Use the current npm 12 line. npm 12 requires Node `^22.22.2`, `^24.15.0` or `>=26.0.0`. Managing dist-tags through OIDC needs npm 12.2.0 or later. The npm documentation's GitHub example uses Node 24 through `actions/setup-node`. The npm bundled with a Node release can be older than 12, so install the pinned npm 12 release and print both versions in the job log. Trusted publishing supports GitHub Actions, GitLab CI/CD and CircleCI on cloud-hosted runners only. Self-hosted runners are not supported. The identity fields described here are for GitHub Actions. Other providers need their own real supported setup.

## Workflow outline

1. Trigger on the chosen protected release event, such as a pushed `v*` tag.
2. In a verify job with `contents: read`, check out with persisted credentials turned off, and set up Node with `registry-url: https://registry.npmjs.org`. Install the pinned npm 12 release with `npm install -g npm@<version>`, and print `node --version` and `npm --version`. Then run `npm ci`, the build, lint and type checks, and tests. The publish job installs the same npm version.
3. Compare the tag with the `package.json` version, run `npm pack --json`, inspect the file list, and upload the tarball as a workflow artifact. Read the JSON fields that the installed npm 12 prints.
4. In a publish job that depends on the verify job, use the registered environment and grant `id-token: write` with `contents: read`. Download the exact tarball and confirm that its integrity matches the verify job's record.
5. Run `npm publish <name>-<version>.tgz --ignore-scripts`. Add `--access public` only when a scoped package is meant to be public. When staging was chosen instead, run `npm stage publish <name>-<version>.tgz --ignore-scripts`, and report the version as staged until a maintainer approves it. With no argument, `npm stage publish` packs the current working directory, which would skip the reviewed tarball. Its synopsis takes a `<package-spec>`, and npm's package-spec definition includes a local tarball file such as `./my-package.tgz`. `npm stage publish` leaves 2FA until approval. Read the stage ID it reports. Compare the staged artifact with the reviewed integrity through `npm stage view <stage-id>` or `npm stage download <stage-id>`. If the CLI rejects the tarball, stop instead of repacking in the publish job. A maintainer then runs `npm stage approve <stage-id>` with 2FA, or `npm stage reject <stage-id>`.
6. Read back the result with `npm view <name>@<version> dist.integrity` and compare it with the reviewed tarball. Check provenance on the package page when you expect it.

## Release boundaries

Use a protected version-tag trigger or another explicit, authenticated release policy. Pull requests and arbitrary forks must never get the ability to publish. Check the tag against the manifest version using environment variables, not shell interpolation of untrusted event text. Require the version to be new. Document whether release versions are changed by a release bot or by an explicit version commit. A CI pipeline must not make up version bumps from prose without a chosen policy.

Give `id-token: write` only to the publish job. Build and test in a job with read-only repository access. Pin action references, do not keep checkout credentials, avoid caches for release builds, pass the reviewed artifact within the same workflow, and do not run untrusted pull request code in a privileged context. OIDC authorization does not make package lifecycle code safe.

Publish the tarball with lifecycle scripts turned off, after the build and tests have finished. Use public access when that is the intent. Set repository metadata correctly, and check provenance support for the real repository and package visibility. Trusted publishing creates provenance automatically only from a public repository for a public package, on GitHub Actions or GitLab CI/CD. CircleCI trusted publishing does not create it. Do not claim provenance for a private repository based on this rule.

## Failure and recovery

For OIDC errors, inspect the exact identity fields, environment, workflow name, permissions, supported runner, package ownership, Node and npm versions, and the allowed-action setting. Remove a stray `NODE_AUTH_TOKEN` or `.npmrc` write credential instead of allowing a token fallback. A read token for private dependencies, if needed, must have its own scope and must not be present when publishing.

If the registry reports that the version already exists, compare its integrity with the intended artifact before deciding anything. Never overwrite or unpublish automatically. If it is identical, report the existing release. If it differs, or the publish was wrong, follow the registry's supported correction policy and release a new version. Do not retry forever or fake success. After the OIDC publish is confirmed and the user authorizes the account change, the owner can select "Require two-factor authentication and disallow tokens" under the package's publishing access settings and revoke automation tokens that are no longer needed.
