# Package design and verification

## Manifest

Set the real name, version, description, SPDX license, repository URL, homepage, issue URL, keywords, supported Node engine, module type, and public entrypoints. Use `files` to allowlist the built output, README, license, and any required assets. Review the files npm always includes or excludes. Do not assume `.gitignore` alone decides what goes into the tarball.

For a typed ESM library, point `exports` and type metadata at real built files. Add only entrypoints meant to be public API. Check extension and resolution behavior from a consumer. Do not expose `src/` or random deep imports by accident. Do not publish a browser bundle that imports Node-only APIs by mistake. Use `sideEffects: false` only if import-time behavior really allows it.

Put runtime requirements in `dependencies`, build and test tools in development dependencies, and integration contracts in `peerDependencies` where that truly fits. Commit the development lockfile and use `npm ci` for the matching package manager. Do not switch away from an existing package manager without a good reason. Avoid runtime dependencies and install lifecycle scripts you do not need.

## API and quality

Use explicit errors and stable public types. Document usage, inputs, outputs, failure behavior, runtime requirements, and examples. Include the current project architecture and commands in `AGENTS.md`. When the new final contract replaces old exports and compatibility paths, remove them, and communicate the version impact through the real release policy.

Run checks against the supported targets you declared, not an invented matrix. For a new package, choose the runtime that is compatible today before pinning it. Type checking and transpiling are different checks. Use a formatter and linter that match the codebase.

## Artifact test

Build, run `npm pack --json`, read the fields the installed npm version prints, and inspect the tarball's file list. Check that the intended code, declarations, assets, license, and README are there. Reject `.env`, keys, logs, tests with private data, local configuration, caches, and unneeded sources or source maps.

Install the built tarball into a clean temporary consumer with npm 12 defaults. Dependency lifecycle scripts are blocked there unless the consumer allows them, so the library must import and run without an install-time script. Import each public entrypoint and run typical features. Compile a TypeScript consumer if types are part of the contract. Test browser loading if you claim browser support. Use existing native tools and the exact reviewed archive. This check does not need a new smoke-test program. Automation requested separately uses Python/uv and takes an explicit artifact path. A unit test run from the source tree does not replace this check.

Keep `dist/` ignored in Git when it is generated, but include it explicitly in the published package. Version files, lockfiles, wrappers, and inputs needed to reproduce the build should stay tracked. Publishing the archive instead of rebuilding in the publish job keeps the checked artifact and the released artifact identical.
