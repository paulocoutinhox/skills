---
name: pypi-library
description: Design and verify a Python library's package metadata, public imports, wheel/sdist artifacts and OIDC trusted release process with uv and Ruff. Use for library authoring or a complete PyPI publication review.
license: MIT
---

# PyPI Library

Create a library that can be installed and used independently of its source checkout. Explain the build and release contract precisely. Do not replace the knowledge with bundled publication scripts or automatic account configuration.

## Identity and architecture

Distinguish the distribution name, import package, public module and installed command. A distribution named `example-tools` can provide `example_tools`, but the names are not interchangeable. Check ownership and intended consumers before selecting a public identity.

Use the actual supported Python version and existing coherent build backend. A `src/` layout helps prevent the source directory from masking an incomplete installation. Keep one class/enum per focused module. Every `__init__.py` remains completely empty under the owner's convention. Use public imports from real defining modules and place version data in an explicit source when needed.

Do not resolve circular dependencies with `TYPE_CHECKING` import branches. Correct ownership/shared types and use annotation facilities supported by the selected runtime. This owner convention does not make every annotation/circular dependency a packaging defect.

## Metadata and dependencies

Declare build-system requirements, project name, static or intentionally dynamic version source, README, supported Python range, license expression/files, authors, URLs and actual dependencies. A console entrypoint must reference a real importable callable. Include `py.typed` if inline typing is part of the distribution contract.

Runtime dependency ranges and `uv.lock` serve different consumers. The lock fixes contributor/CI resolution. Library metadata describes compatible installed requirements. Do not embed a local environment, editable path, machine-specific credential or developer checkout into published metadata.

Prefer a small explicit API and meaningful errors. Do not reexport everything through an initializer merely to create a short import, and do not expose internal modules accidentally. Remove superseded aliases when the requested final API replaces them, while communicating release/migration impact.

## Build the distributions you intend to publish

Run the repository's Ruff, relevant type/behavior checks and actual tests. Use uv and the project's documented build frontend/backend. A reproducible release pins the selected build tooling and requirements rather than assuming a contributor lock automatically freezes every isolated backend dependency.

Build both a wheel and source distribution. Inspect archive filenames, metadata, public modules, typing information, data assets, license and README. Reject environment files, signing/credential material, logs, caches, private test records and local paths.

If the version is dynamic, inspect the built metadata rather than assuming `project.version` exists in TOML. Compare the wheel and sdist name/version with one another and with the release tag. A valid filename does not prove the embedded metadata agrees.

## Worked consumer verification

Suppose the public API is `from example_tools.parser import Parser`. Install the built wheel into a clean temporary environment outside the repository and execute a representative parse plus an invalid-input case. Ensure the import resolves from the installed environment rather than the checkout.

Then build a wheel from the sdist in isolation and repeat the consumer check. This detects a missing source/data/build input that a wheel built directly from the checkout can hide. A file-exists assertion or an import executed from the source root cannot establish this property.

Test installed console entrypoints and type consumers where claimed. A pure-Python universal wheel is different from a compiled wheel. Native extensions need the selected OS/architecture/interpreter matrix, compatible tags and actual installed-artifact testing. Do not claim a single host build covers every platform.

Use existing tooling for these checks. Do not generate automation merely to show activity. If separately requested, a smoke/release helper must be Python run with uv, accept explicit artifact paths and exercise real behavior.

## Trusted publication and bootstrap

For an existing PyPI project, register the precise trusted publisher. For a new project, a pending publisher can create the project on the first successful trusted publication. It does not reserve the name. Check exact owner/repository/workflow filename and optional environment through the authenticated owner path.

TestPyPI is a separate registry, identity and namespace. Its successful test publication does not configure production trust or authorize a real release. Owner enrollment, 2FA and legal/account decisions remain separate from routine short-lived upload authentication.

In CI, build/test with read-only access. Transfer only the reviewed distributions, then publish through the official supported PyPA action from a dedicated job with `id-token: write`. Do not pass a username/password/API token as a fallback. Pin reviewed action/tool versions. Restrict the release trigger and environment to the chosen policy, without granting fork PR code publication identity.

Build once. Do not rebuild in the privileged publication job. Verify the gathered artifact set before uploading, especially for a native-wheel matrix. A partially uploaded version may need reconciliation rather than rerunning a build that produces different bytes.

## Failure and recovery

Check exact identity claims, environment spelling, workflow filename, registry URL, project name, pending-publisher status and OIDC permission when trust fails. Separate authentication failures from package metadata or distribution-content errors.

An existing filename/version cannot be overwritten as a routine retry. After a timeout, read registry state and compare hashes. If the intended bytes already exist, report that evidence. If the wrong artifact was published, choose an authorized corrective version/yank policy. Do not use `skip-existing` to conceal an unexpected mismatch or publish an unreviewed rebuild.

Deliver source, documentation, built metadata/content evidence, isolated wheel/sdist consumer results, publisher setup status, release design and actual publication state. Update current `AGENTS.md` without a change diary.

## Foundations

The [Python Packaging User Guide](https://packaging.python.org/) and [src-layout discussion](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) govern modern packaging practice. [PyPI trusted publishing](https://docs.pypi.org/trusted-publishers/using-a-publisher/) governs authentication and bootstrap. [uv build guidance](https://docs.astral.sh/uv/guides/package/) explains actual build behavior. The release-engineering chapter of [Site Reliability Engineering](https://sre.google/sre-book/release-engineering/) is broader professional reading on controlled artifact delivery.

See [package detail](references/packaging.md), [publishing detail](references/publishing.md), [sources](references/sources.md) and [license](LICENSE.md).
