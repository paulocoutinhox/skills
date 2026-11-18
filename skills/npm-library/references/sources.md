# Sources

Verified: 2026-11-05.

- [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/): OIDC identity, minimum client versions, hosted-runner support, current allowed-action configuration, and provenance conditions.
- [npm trust CLI](https://docs.npmjs.com/cli/v12/commands/npm-trust/): current administrative interface, subject to authentication and ownership.
- [Package manifest](https://docs.npmjs.com/cli/v12/configuring-npm/package-json/): exports, files, engines, dependency metadata, and publication configuration.
- [npm pack](https://docs.npmjs.com/cli/v12/commands/npm-pack/): package archive inspection.
- [GitHub workflow security](https://docs.github.com/en/actions/reference/security/secure-use): least permissions, pinned actions, and untrusted input.

The actual consumer verification, release version policy, protected trigger and direct-publish selection must be defined for the target project. This descriptive skill does not bundle a release workflow or smoke-test script, and does not configure registry trust.

## Professional foundation and evidence scope

Reviewed: 2026-11-05. The official [Node package reference](https://nodejs.org/api/packages.html) supports export/module resolution. Dinah McNutt's chapter [Release Engineering](https://sre.google/sre-book/release-engineering/) in Site Reliability Engineering is professional context for controlled artifacts and releases, not an npm authentication specification. The skill is descriptive and bundles no workflow/helper implementation.

## Trusted publishing recheck

Checked **2026-11-18**. [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/) lists npm 11.5.1 and Node 22.14.0 as minimums, GitHub Actions, GitLab CI/CD and CircleCI on cloud-hosted runners, independent allowed actions where `npm stage publish` is always allowed and direct `npm publish` is optional, the two-day first-publication window, automatic provenance only for public repositories and public packages on GitHub Actions or GitLab CI/CD, and the "Require two-factor authentication and disallow tokens" setting. Staged approval through `npm stage approve` needs interactive authentication. [npm trust](https://docs.npmjs.com/cli/v12/commands/npm-trust/) requires npm 11.15.0, account 2FA, write access and a package that already exists on the registry, with `--allow-publish` or `--allow-stage-publish` required when creating a configuration.

## Staged publication argument

Checked **2026-11-18**. The [npm stage reference](https://docs.npmjs.com/cli/v12/commands/npm-stage/) gives `npm stage publish [<package-spec>]`, says the command packs the current working directory, states parity with `npm publish`, lists `list`, `view`, `approve`, `reject` and `download` subcommands, and requires 2FA only for approval and rejection. It does not show a tarball example. The [npm publish reference](https://docs.npmjs.com/cli/v12/commands/npm-publish/) lists a gzipped tarball as an accepted package form. The [package-spec reference](https://docs.npmjs.com/cli/v12/using-npm/package-spec/) defines a local tarball file, such as `./my-package.tgz`, as a package spec, so `npm stage publish` accepts the reviewed tarball through its documented argument.

## npm 12 baseline

Checked **2026-11-18**. The npm documentation's current CLI pages are the `/cli/v12/` reference, version 12.2.2 when read, while the v11 pages are labeled legacy. The [npm CLI releases](https://github.com/npm/cli/releases) list 12.2.3 as the latest release, published 2026-11-11 according to its changelog. The [12.0.0 release notes](https://github.com/npm/cli/releases/tag/v12.0.0), dated 2026-07-08, list the breaking changes used here: Node `^22.22.2 || ^24.15.0 || >=26.0.0`, consistent new `--json` output for `npm pack` and `npm publish`, dependency lifecycle scripts blocked by default unless the root package's `allowScripts` policy allows them, removal of `npm shrinkwrap` and of loading `npm-shrinkwrap.json`, and removal of `npm adduser`. [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/) states that dist-tags with OIDC need npm 11.21.0 or 12.2.0 and later, and links its command reference to the v12 pages. The v12 [npm trust](https://docs.npmjs.com/cli/v12/commands/npm-trust/) page keeps the npm 11.15.0 floor, account 2FA, an existing package and the `--allow-publish`/`--allow-stage-publish` requirement.

Stored content is maintained only when the user requests a revision. There is no automated source collector or refresh mechanism.
