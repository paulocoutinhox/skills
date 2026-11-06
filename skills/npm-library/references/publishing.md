# Automatic trusted publication

## One-time registry setup

Confirm package ownership and the registry's supported bootstrap path. Current npm trust configuration applies to a package's settings. Do not assume a pending-publisher feature identical to another registry. If a brand-new name cannot configure trust yet, surface the initial setup requirement and obtain an authorized path. Never silently fall back to a long-lived token.

For GitHub Actions, register the exact owner, repository, workflow filename including `.yml` or `.yaml`, and environment if selected. The filename is not the full workflow path. Current publisher settings distinguish staged publication and direct `npm publish`. Enable direct publication when the desired workflow has no staging/promote intervention. Keep the environment name identical in the registry and the workflow. For fully automatic releases, do not add an unrequested required-reviewer gate.

The current documented client floor is npm 11.5.1 and Node 22.14.0. A supported current Node 24 toolchain is one starting point, but pin and verify the actual Node/npm pair for the target project. Trusted publishing currently uses supported hosted runners. Do not move it to a self-hosted runner without verifying support. Supported providers have different identity claims and configuration. The described identity tuple targets GitHub Actions. Other providers require their actual supported configuration.

## Release boundaries

Use a protected version-tag trigger or another explicit authenticated release policy. PRs and arbitrary forks must never receive publish capability. Validate the tag against manifest version using environment variables, not shell interpolation of untrusted event text. Require the version to be new. Document whether release versions are changed by a release bot or an explicit version commit. A CI pipeline must not invent version increments from prose without a chosen policy.

Give only the publish job `id-token: write`. Build and test in a job with read-only repository access. Pin action references, do not persist checkout credentials, avoid release-build caches, transfer the reviewed artifact within the same workflow, and do not execute untrusted PR code in a privileged context. OIDC authorization does not make package lifecycle code safe.

Publish the tarball with lifecycle scripts disabled after build and tests have completed. Use public access when intended. Set repository metadata correctly and verify provenance support for the actual repository/package visibility. Public-repository public-package GitHub OIDC publication normally creates provenance automatically. Do not claim private-repository provenance support from that baseline.

## Failure and recovery

For OIDC errors, inspect the exact identity tuple, environment, workflow name, permissions, supported runner, package ownership, Node/npm versions, and allowed-action setting. Remove accidental `NODE_AUTH_TOKEN` or `.npmrc` write credentials rather than allowing token fallback. A private-dependency read token, if necessary, must be scoped separately and absent from publication.

If the registry reports the version already exists, compare its integrity with the intended artifact before deciding anything. Never overwrite or unpublish automatically. If it is identical, report the existing release. If it differs or publication was incorrect, follow the registry's supported corrective policy and release a new version. Do not retry endlessly or fabricate success. Revoke superseded automation tokens after OIDC publication is verified and the user authorizes the account change.
