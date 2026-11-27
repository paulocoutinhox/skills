# Sources

Checked: 2026-11-05.

- [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/): OIDC identity, minimum client versions, hosted-runner support, current allowed-action setup, and provenance conditions.
- [npm trust CLI](https://docs.npmjs.com/cli/v12/commands/npm-trust/): current admin interface, which needs authentication and ownership.
- [Package manifest](https://docs.npmjs.com/cli/v12/configuring-npm/package-json/): exports, files, engines, dependency metadata, and publish configuration.
- [npm pack](https://docs.npmjs.com/cli/v12/commands/npm-pack/): inspecting the package archive.
- [GitHub workflow security](https://docs.github.com/en/actions/reference/security/secure-use): least permissions, pinned actions, and untrusted input.

The real consumer checks, release version policy, protected trigger and choice of direct publishing must be defined for the target project. This descriptive skill does not bundle a release workflow or smoke-test script, and it does not set up registry trust.

## Professional foundation and evidence scope

Reviewed: 2026-11-05. The official [Node package reference](https://nodejs.org/api/packages.html) supports export and module resolution. Dinah McNutt's chapter [Release Engineering](https://sre.google/sre-book/release-engineering/) in Site Reliability Engineering gives professional background on controlled artifacts and releases. It is not an npm authentication specification. The skill is descriptive and bundles no workflow or helper code.

## Trusted publishing recheck

Checked **2026-11-18**. [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/) lists these points. The minimums are npm 11.5.1 and Node 22.14.0. Supported runners are GitHub Actions, GitLab CI/CD and CircleCI on cloud-hosted runners. Allowed actions are set separately: `npm stage publish` is always allowed and direct `npm publish` is optional. The first publish must happen within two days. Provenance is automatic only for public repositories and public packages on GitHub Actions or GitLab CI/CD. The page also describes the "Require two-factor authentication and disallow tokens" setting. Staged approval through `npm stage approve` needs interactive authentication. [npm trust](https://docs.npmjs.com/cli/v12/commands/npm-trust/) requires npm 11.15.0, account 2FA, write access and a package that already exists on the registry. Creating a configuration requires `--allow-publish` or `--allow-stage-publish`.

## Staged publication argument

Checked **2026-11-18**. The [npm stage reference](https://docs.npmjs.com/cli/v12/commands/npm-stage/) gives `npm stage publish [<package-spec>]` and says the command packs the current working directory. It states that it matches `npm publish`, lists the `list`, `view`, `approve`, `reject` and `download` subcommands, and requires 2FA only for approval and rejection. It does not show a tarball example. The [npm publish reference](https://docs.npmjs.com/cli/v12/commands/npm-publish/) lists a gzipped tarball as an accepted package form. The [package-spec reference](https://docs.npmjs.com/cli/v12/using-npm/package-spec/) defines a local tarball file, such as `./my-package.tgz`, as a package spec. So `npm stage publish` accepts the reviewed tarball through its documented argument.

## npm 12 baseline

Checked **2026-11-18**. The npm documentation's current CLI pages are the `/cli/v12/` reference, version 12.2.2 when read. The [npm CLI releases](https://github.com/npm/cli/releases) list 12.2.3 as the latest release, published 2026-11-11 according to its changelog. The [12.0.0 release notes](https://github.com/npm/cli/releases/tag/v12.0.0), dated 2026-07-08, list the breaking changes used here: Node `^22.22.2 || ^24.15.0 || >=26.0.0`, consistent new `--json` output for `npm pack` and `npm publish`, dependency lifecycle scripts blocked by default unless the root package's `allowScripts` policy allows them, removal of `npm shrinkwrap` and of loading `npm-shrinkwrap.json`, and removal of `npm adduser`. [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/) states that dist-tags with OIDC need npm 11.21.0 or 12.2.0 and later, and links its command reference to the v12 pages. The v12 [npm trust](https://docs.npmjs.com/cli/v12/commands/npm-trust/) page keeps the npm 11.15.0 minimum, account 2FA, an existing package and the `--allow-publish`/`--allow-stage-publish` requirement.

Stored content is updated only when the user asks for a revision. There is no automatic source collector or refresh mechanism.
