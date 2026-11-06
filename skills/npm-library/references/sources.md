# Sources

Verified: 2026-11-05.

- [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/): OIDC identity, minimum client versions, hosted-runner support, current allowed-action configuration, and provenance conditions.
- [npm trust CLI](https://docs.npmjs.com/cli/v11/commands/npm-trust/): current administrative interface, subject to authentication and ownership.
- [Package manifest](https://docs.npmjs.com/cli/v11/configuring-npm/package-json/): exports, files, engines, dependency metadata, and publication configuration.
- [npm pack](https://docs.npmjs.com/cli/v11/commands/npm-pack/): package archive inspection.
- [GitHub workflow security](https://docs.github.com/en/actions/reference/security/secure-use): least permissions, pinned actions, and untrusted input.

The actual consumer verification, release version policy, protected trigger and direct-publish selection must be defined for the target project. This descriptive skill does not bundle a release workflow or smoke-test script, and does not configure registry trust.

## Professional foundation and evidence scope

Reviewed for this revision: 2026-11-05. The official [Node package reference](https://nodejs.org/api/packages.html) supports export/module resolution. Dinah McNutt's chapter [Release Engineering](https://sre.google/sre-book/release-engineering/) in Site Reliability Engineering is professional context for controlled artifacts and releases, not an npm authentication specification. The skill is descriptive and bundles no workflow/helper implementation.

Stored content is maintained only when the user requests a revision. There is no automated source collector or refresh mechanism.
