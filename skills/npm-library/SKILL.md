---
name: npm-library
description: Design, package, verify and release a Node.js npm library with explicit exports, installed-consumer evidence and OIDC trusted publishing. Use for publishable library implementation or review of its release contract.
license: MIT
---

# npm Library

Create a library that works from its published artifact, with an explicit public contract and an authenticated release path. This skill explains the process. It does not bundle release scripts or create account trust automatically.

## Define the actual package contract

Identify name/scope ownership, registry, repository, license, intended consumers, runtime/browser targets, module format, public entrypoints, types, errors and version policy. Read existing manifests, lockfiles and consumers before choosing changes. New work favors one current ESM contract unless the user requires another target.

Separate Node-only capabilities from browser-safe code. Do not claim browser support because the bundler transpiled the source. A runtime import of filesystem/process APIs can still break the browser consumer. Do not publish duplicate compatibility builds merely by habit.

Use public imports deliberately. Every export becomes an API surface consumers can depend on. Avoid accidentally exposing internal source paths through wildcard exports. Removing an internal-looking path that was publicly exported can still require a breaking release under the project's policy.

## Manifest and output design

Declare real package metadata, supported `engines`, SPDX licensing, repository/homepage/issue URLs and the version source. Use `files` as an intentional allowlist. Review npm's mandatory inclusions/exclusions as well as the allowlist. `.gitignore` does not prove what enters the tarball.

For a typed ESM package, ensure every `exports` branch and declaration path points to an actual built file. A `types` condition must describe that entrypoint's runtime contract. Do not assume editor success from source proves installed declaration resolution.

Use runtime dependencies for required shipped code, development dependencies for build/test tooling, and peer dependencies for genuine host integration contracts. A plugin depending on the host as both an incompatible private runtime and a peer can create duplicate instances. Inspect the actual framework/library semantics.

Use `sideEffects: false` only when import-time behavior really permits elimination. CSS registration, polyfill setup or global initialization can be removed incorrectly by a consumer bundler when that declaration is false.

## Worked artifact verification

Suppose `@example/format-kit` exposes `.` and `./dates`, with JavaScript/declarations under `dist/`. Verify both imports from an isolated consumer installed from the actual archive. Exercise a normal operation and a meaningful failure. If TypeScript support is claimed, compile that consumer against the declared supported target/module resolution.

An import from `src/` inside the source checkout can pass while the tarball omits `dist/dates.js`, a declaration or a required data file. That is why source tests and package tests answer different questions.

Run the actual project's lint, type checking, behavioral tests and build. Use `npm ci` for a matching npm lockfile, or the existing package manager's frozen equivalent. Transpilation alone may not type-check. Inspect `npm pack --json` output and archived paths. Reject credentials, local config, logs, private fixtures and unnecessary files. Check license and README inclusion.

Do not add helper scripts solely to perform these checks. Use existing package/tool interfaces. If the user separately requests automation glue, it must be Python with uv and actual documented behavior.

## Release version and immutable artifact

Choose how versions are authored and how stable/prerelease channels are selected. Compare the tag/release identifier with the actual package metadata. A tag such as `v1.4.0` must not publish metadata version `1.3.9`. Serialize release operations for the package so two workflows do not compete to publish one version.

Build once, inspect/test that tarball, preserve its integrity hash, and publish the same bytes. Do not rebuild a potentially different package in a privileged publication job. A successful build is not proof that every intended export or asset is present.

If publication times out, inspect registry state before retrying. An existing version can mean the first attempt succeeded. Compare its integrity with the reviewed artifact. Never overwrite, automatically unpublish, invent a new version or blindly retry a financial/distribution operation. A different artifact under an existing version is an incident, not an invitation to bypass immutability.

## Trusted publishing and CI responsibilities

Configure the exact registry trust relationship through the owner's authorized interface: repository owner/name, workflow filename, optional environment and allowed action. The workflow filename is not the whole path. Current npm settings distinguish staged versus direct publication. Select direct publication for an explicitly requested no-intervention release path.

The researched baseline requires npm 11.5.1+ and Node 22.14.0+, with supported hosted runners. Pin a compatible actual toolchain and inspect current requirements during an authorized release. Account ownership, first package bootstrap, 2FA and publisher configuration are separate from an ordinary CI release. Do not pretend a workflow file configures registry trust.

| Stage | Permission and evidence |
| --- | --- |
| Verify/build | Read-only repository access, trusted inputs, locked dependencies and tests |
| Artifact transfer | Exact reviewed tarball and integrity evidence from the same release run |
| Publish | Narrow OIDC identity, `id-token: write`, intended environment/registry/package |
| Verify | Actual registry version, integrity, access and provenance where supported |

Restrict triggers to the chosen protected release policy. Fork PRs and arbitrary branches must not receive publication capability. Pin reviewed action revisions, avoid persisted checkout credentials, and separate private-dependency read access from publish authorization. OIDC removes a standing upload token but does not make untrusted build code safe.

Publish the reviewed tarball with lifecycle scripts disabled when the explicit build already completed. Do not allow an accidental `NODE_AUTH_TOKEN` or write credential to become a fallback for a broken trust configuration. Avoid an unrequested reviewer gate if fully automatic routine releases are the selected goal. Public-repository provenance conditions must not be generalized to every visibility/provider combination.

## Delivery and foundations

Deliver source, public API documentation, actual artifact-content/consumer evidence, the release design and exact one-time account fields/status. Only create/configure/publish externally within the user's scope. Document current commands and architecture in `AGENTS.md`.

The [Node package reference](https://nodejs.org/api/packages.html) governs module/export behavior. [npm package metadata](https://docs.npmjs.com/cli/v11/configuring-npm/package-json/) governs archive/publication declarations. [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/) governs registry identity. Dinah McNutt's chapter in [Site Reliability Engineering: Release Engineering](https://sre.google/sre-book/release-engineering/) provides broader professional context for repeatable releases. These sources have separate authority.

See [package design](references/package-design.md), [publication detail](references/publishing.md), [sources](references/sources.md) and [license](LICENSE.md).
