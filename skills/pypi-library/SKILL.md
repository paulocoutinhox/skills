---
name: pypi-library
description: Design and verify a Python library's package metadata, public imports, wheel/sdist artifacts and OIDC trusted release process with uv and Ruff. Use to write a library or to fully review its PyPI publishing.
license: MIT
---

# PyPI Library

Create a library that can be installed and used without its source checkout. Explain the build and release contract exactly. Do not replace this knowledge with bundled publishing scripts or automatic account setup.

## Identity and architecture

Tell apart the distribution name, the import package, the public module and the installed command. A distribution named `example-tools` can provide `example_tools`, but the names are not interchangeable. Check ownership and the intended consumers before choosing a public identity.

Use the real supported Python version and the existing build backend if it is sound. A `src/` layout helps stop the source directory from hiding an incomplete install. Keep one class or enum per focused module. Under the owner's convention, every `__init__.py` stays completely empty. Use public imports from the real modules that define things, and put version data in an explicit source when needed.

Do not fix circular dependencies with `TYPE_CHECKING` import branches. Fix ownership and shared types instead, and use annotation features that the chosen runtime supports. This owner convention does not make every annotation or circular dependency a packaging bug.

## Metadata and dependencies

Declare the build-system requirements, project name, a static version or a deliberate dynamic version source, README, supported Python range, license expression and files, authors, URLs and the real dependencies. A console entrypoint must point to a real importable callable. Include `py.typed` if inline typing is part of what the distribution promises.

Runtime dependency ranges and `uv.lock` serve different users. The lock fixes the resolution for contributors and CI. Library metadata describes which installed requirements are compatible. Do not put a local environment, editable path, machine-specific credential or developer checkout into published metadata.

Prefer a small, explicit API and useful errors. Do not re-export everything through an initializer just to get a short import, and do not expose internal modules by accident. When the requested final API replaces old aliases, remove them, and explain the impact on releases and on users who must update their code.

## Build the distributions you intend to publish

Run the repository's Ruff, the relevant type and behavior checks, and the real tests. Use uv and the project's documented build frontend and backend. A reproducible release pins the chosen build tools and requirements. Do not assume a contributor lock also freezes every dependency of an isolated backend.

Build both a wheel and a source distribution. Inspect archive filenames, metadata, public modules, typing information, data files, license and README. Reject environment files, signing or credential material, logs, caches, private test records and local paths.

If the version is dynamic, inspect the built metadata instead of assuming `project.version` exists in TOML. Compare the wheel and sdist name and version with each other and with the release tag. A valid filename does not prove that the metadata inside agrees.

## Worked consumer verification

Suppose the public API is `from example_tools.parser import Parser`. Install the built wheel into a clean temporary environment outside the repository, and run a typical parse plus an invalid-input case. Make sure the import resolves from the installed environment, not from the checkout.

`uv build --no-sources` builds the sdist first and then the wheel from that sdist, which is the release shape to test. If another frontend built the wheel straight from the checkout, build a wheel from the sdist in isolation and repeat the consumer check. This catches a missing source, data file or build input that a wheel built straight from the checkout can hide. For the clean environment, create a temporary virtual environment outside the repository with `uv venv <temp-dir>/venv`. Install the wheel with `uv pip install --python <temp-dir>/venv <wheel-path>`, and run the consumer code with that interpreter from a directory outside the checkout. A check that a file exists, or an import run from the source root, cannot prove this.

Test installed console entrypoints and type consumers where you claim them. A pure-Python universal wheel is different from a compiled wheel. Native extensions need the chosen OS, architecture and interpreter matrix, compatible tags and real tests of the installed artifact. Do not claim that one host build covers every platform.

Use existing tools for these checks. Do not generate automation just to look busy. If it is requested separately, a smoke or release helper must be Python run with uv, take explicit artifact paths and test real behavior.

## Trusted publication and bootstrap

For an existing PyPI project, register the exact trusted publisher. For a new project, a pending publisher can create the project on the first successful trusted publish. It does not reserve the name, and it stops working if another account registers the name first. This differs from npm, where trust can be set up only on a package that already exists. Check the exact owner, repository, workflow filename and optional environment through the authenticated owner path.

TestPyPI is a separate registry, identity and namespace. A successful test publish there does not set up production trust or authorize a real release. Owner sign-up, 2FA and legal or account decisions stay separate from routine short-lived upload authentication.

In CI, build and test with read-only access. Pass along only the reviewed distributions. Then publish through the official supported PyPA action from a dedicated GitHub-hosted Linux job with `id-token: write`, outside any reusable workflow. The [publishing detail](references/publishing.md#workflow) lists the jobs in order. Do not pass a username, password or API token as a fallback. Pin reviewed action and tool versions. Limit the release trigger and environment to the chosen policy, and do not give pull request code from forks a publishing identity.

Build once. Do not rebuild in the privileged publish job. Check the collected artifact set before uploading, especially for a native-wheel matrix. If only some files of a version were uploaded, upload the missing files from the same reviewed set. Do not rebuild, because a new build produces different bytes.

## Failure and recovery

When trust fails, check the exact identity claims, environment spelling, workflow filename, registry URL, project name, pending-publisher status and OIDC permission. Keep authentication failures apart from package metadata or distribution-content errors.

An existing filename or version cannot be overwritten as a routine retry. After a timeout, read the registry state and compare hashes. If the intended bytes already exist, report that evidence. If the wrong artifact was published, choose an authorized fix through a new version or a yank policy. Do not use `skip-existing` to hide an unexpected mismatch or to publish an unreviewed rebuild.

Deliver the source, documentation, evidence of the built metadata and contents, results of the isolated wheel and sdist consumer checks, the publisher setup status, the release design and the real publish state. Update the current `AGENTS.md` without a change diary.

## Foundations

The [Python Packaging User Guide](https://packaging.python.org/) and the [src-layout discussion](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) are the source of truth for modern packaging practice. [PyPI trusted publishing](https://docs.pypi.org/trusted-publishers/using-a-publisher/) is the source of truth for authentication and the first publish. [uv build guidance](https://docs.astral.sh/uv/guides/package/) explains real build behavior. The release-engineering chapter of [Site Reliability Engineering](https://sre.google/sre-book/release-engineering/) is wider professional reading on controlled artifact delivery.

See [package detail](references/packaging.md), [publishing detail](references/publishing.md), [sources](references/sources.md) and [license](LICENSE.md).
