---
name: npm-library
description: Design, package, verify and release a Node.js npm library with explicit exports, proof from an installed consumer and OIDC trusted publishing. Use to build a publishable library or to review its release contract.
license: MIT
---

# npm Library

Create a library that works from its published package, with an explicit public contract and an authenticated release path. This skill explains the process. It does not bundle release scripts, and it does not set up account trust for you.

## Define the real package contract

Identify who owns the name or scope, and the registry, repository, license, intended consumers, runtime and browser targets, module format, public entrypoints, types, errors and version policy. Read the existing manifests, lockfiles and consumers before choosing changes. New work prefers one current ESM contract unless the user needs another target.

Keep Node-only features apart from browser-safe code. Do not claim browser support just because the bundler transpiled the source. A runtime import of filesystem or process APIs can still break the browser consumer. Do not publish extra compatibility builds out of habit.

Choose public imports on purpose. Every export becomes part of the API that consumers can depend on. Do not expose internal source paths by accident through wildcard exports. Removing a path that looks internal but was publicly exported can still need a breaking release under the project's policy.

## Manifest and output design

Declare real package metadata, supported `engines`, SPDX licensing, repository/homepage/issue URLs and where the version comes from. Use `files` as a deliberate allowlist. Also review the files npm always includes or excludes, not just the allowlist. `.gitignore` does not prove what goes into the tarball.

For a typed ESM package, make sure every `exports` branch and declaration path points to a real built file. A `types` condition must describe the runtime contract of that entrypoint. Working types in the editor from source do not prove that declarations resolve once installed.

Use runtime dependencies for code the package needs when it runs, development dependencies for build and test tools, and peer dependencies for real host integration contracts. A plugin that depends on the host both as a private, incompatible runtime copy and as a peer can create duplicate instances. Inspect how the real framework or library behaves.

npm 12 blocks dependency lifecycle scripts by default unless the consumer's root package allows them through its `allowScripts` policy. So a library must work without its own `install` or `postinstall` script running. Ship built output instead of building on install. npm 12 also ignores `npm-shrinkwrap.json`, so do not publish one to lock a dependency tree.

Use `sideEffects: false` only when import-time behavior really allows code to be removed. If you set it to false when imports do have side effects, a consumer's bundler can wrongly remove CSS registration, polyfill setup or global setup.

## Worked artifact verification

Suppose `@example/format-kit` exposes `.` and `./dates`, with JavaScript and declarations under `dist/`. Check both imports from a separate consumer installed from the real archive. Run a normal operation and a meaningful failure. If you claim TypeScript support, compile that consumer against the declared supported target and module resolution.

An import from `src/` inside the source checkout can pass while the tarball is missing `dist/dates.js`, a declaration or a required data file. That is why source tests and package tests answer different questions.

Run the real project's lint, type checking, behavior tests and build. Use `npm ci` for a matching npm lockfile, or the existing package manager's frozen-lockfile equivalent. Transpiling alone may not type-check. Inspect the `npm pack --json` output and the paths in the archive. Read the JSON fields that the installed npm 12 prints. Reject credentials, local config, logs, private fixtures and files that are not needed. Check that the license and README are included.

Do not add helper scripts just to run these checks. Use the existing package and tool interfaces. If the user separately asks for automation glue, it must be Python with uv and follow the real documented behavior.

## Release version and immutable artifact

Choose how versions are written and how stable and prerelease channels are chosen. Compare the tag or release ID with the real package metadata. A tag such as `v1.4.0` must not publish metadata version `1.3.9`. Run release operations for the package one at a time, so two workflows do not race to publish the same version.

Build once, inspect and test that tarball, keep its integrity hash, and publish the same bytes. Do not rebuild a package that may differ in a privileged publish job. A successful build does not prove that every intended export or asset is present.

If publishing times out, check the registry state before retrying. An existing version can mean the first attempt worked. Compare its integrity with the reviewed artifact. Never overwrite, automatically unpublish, invent a new version or blindly retry the publish. A different artifact under an existing version is an incident. It is not a reason to get around immutability.

## Trusted publishing and CI responsibilities

Set up the exact registry trust link through the owner's authorized interface: repository owner/name, workflow filename, optional environment and allowed action. The workflow filename is not the whole path. `npm stage publish` is always allowed, while direct `npm publish` must be chosen explicitly. A staged version waits for a maintainer's interactive 2FA approval. Choose direct publishing when the user explicitly asks for a release path with no manual step.

Trust is set up on a package that already exists on the registry. Unlike PyPI, npm has no pending publisher. So a brand-new package needs a first publish by the owner, through an authorized interactive path, before trust can be added. A new trust configuration must finish its first successful publish within two days, or it expires.

Use the current npm 12 line, which requires Node `^22.22.2`, `^24.15.0` or `>=26.0.0`. Managing dist-tags through OIDC needs npm 12.2.0 or later. Trusted publishing runs only on cloud-hosted GitHub Actions, GitLab CI/CD or CircleCI runners. A Node release can bundle an older npm, so install the pinned npm 12 release in CI and record `node --version` and `npm --version`. Check the current requirements during an authorized release. Account ownership, the first package publish, 2FA and publisher setup are separate from an ordinary CI release. Do not pretend that a workflow file sets up registry trust.

| Stage | Permission and evidence |
| --- | --- |
| Verify/build | Read-only repository access, trusted inputs, locked dependencies and tests |
| Artifact transfer | Exact reviewed tarball and integrity evidence from the same release run |
| Publish | Narrow OIDC identity, `id-token: write`, intended environment/registry/package |
| Verify | Actual registry version, integrity, access and provenance where supported |

Limit triggers to the chosen protected release policy. Pull requests from forks and arbitrary branches must not get the ability to publish. Pin reviewed action revisions, do not keep checkout credentials, and keep read access for private dependencies apart from publish permission. OIDC removes a long-lived upload token, but it does not make untrusted build code safe.

When the build has already finished, publish the reviewed tarball with `npm publish <tarball> --ignore-scripts`. Then compare `npm view <name>@<version> dist.integrity` with the reviewed artifact. The [publication detail](references/publishing.md#workflow-outline) gives the ordered job outline. Do not let a stray `NODE_AUTH_TOKEN` or write credential become a fallback for a broken trust setup. Do not add a reviewer gate nobody asked for if fully automatic routine releases are the chosen goal. Automatic provenance requires a public repository, a public package and GitHub Actions or GitLab CI/CD. Do not assume it for every visibility and provider combination.

## Delivery and foundations

Deliver the source, public API documentation, real evidence of the artifact contents and consumer checks, the release design, and the exact one-time account fields and their status. Create, configure or publish anything outside the repository only within the user's scope. Document the current commands and architecture in `AGENTS.md`.

The [Node package reference](https://nodejs.org/api/packages.html) is the source of truth for module and export behavior. [npm package metadata](https://docs.npmjs.com/cli/v12/configuring-npm/package-json/) is the source of truth for archive and publish declarations. [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/) is the source of truth for registry identity. Dinah McNutt's chapter in [Site Reliability Engineering: Release Engineering](https://sre.google/sre-book/release-engineering/) gives wider professional background on repeatable releases. Each source covers its own area.

See [package design](references/package-design.md), [publication detail](references/publishing.md), [sources](references/sources.md) and [license](LICENSE.md).
