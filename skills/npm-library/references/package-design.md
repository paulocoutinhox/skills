# Package design and verification

## Manifest

Set the real name, version, description, SPDX license, repository URL, homepage, issue URL, keywords, supported Node engine, module type, and public entrypoints. Use `files` to allowlist distributed output, README, license, and any required assets. Review files npm always includes or excludes. Do not assume `.gitignore` alone determines the tarball.

For a typed ESM library, point `exports` and type metadata at real built files. Add only entrypoints intended as public API. Verify extension and resolution behavior from a consumer. Do not expose `src/` or arbitrary deep imports accidentally. Do not publish a browser bundle that imports Node-only APIs unintentionally. Use `sideEffects: false` only if import-time behavior truly permits it.

Runtime requirements belong in `dependencies`, build and test tools in development dependencies, and integration contracts in `peerDependencies` where genuinely appropriate. Commit the development lockfile and use `npm ci` for the corresponding package manager. Do not replace an existing package manager casually. Avoid unnecessary runtime dependencies and install lifecycle scripts.

## API and quality

Use explicit errors and stable public types. Document usage, inputs, outputs, failure behavior, runtime requirements, and examples. Include the current project architecture and commands in `AGENTS.md`. Remove obsolete exports and compatibility paths when the new final contract replaces them, and communicate version impact through the actual release policy.

Run checks against supported declared targets, not an invented matrix. For a new package, choose the currently compatible runtime before pinning it. Type checking and transpilation are different checks. Use a formatter and linter consistent with the codebase.

## Artifact test

Build, run `npm pack --json`, inspect the tarball's file list, and verify that the intended code, declarations, assets, license, and README are present. Reject `.env`, keys, logs, tests containing private data, local configuration, caches, and unnecessary sources or source maps.

Install the produced tarball into a clean temporary consumer. Import each public entrypoint and execute representative functionality. Compile a TypeScript consumer if types are part of the contract. Test browser loading if browser support is claimed. Use existing native tools and the exact reviewed archive. Do not require a new smoke-test program for this check. Separately requested automation uses Python/uv and accepts an explicit artifact path. A source-tree unit test is not a substitute.

Keep `dist/` ignored in Git when generated, while explicitly including it in the published package. Version files, lockfiles, wrappers, and reproducibility inputs should remain tracked. Publishing the archive rather than rebuilding in the publish job keeps the validated and released artifact identical.
