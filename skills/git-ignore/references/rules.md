# Ignore semantics and privacy

Patterns with no slash except an optional trailing slash can match at any depth below the configuration directory. A slash at the beginning or in the middle ties the path to that directory. A trailing slash limits matching to directories, but does not tie it to a depth by itself. In a root ignore file, `build/` matches root and nested build directories, `/build/` matches only the root build directory, and `apps/web/build/` matches that exact relative directory, not `examples/apps/web/build/`.

`**` can span directories. A leading `!` reverses an earlier rule, but a file inside an ignored parent cannot be brought back unless Git can enter that parent. Later applicable patterns win at the same precedence level. Escape literal `#` or `!` where needed.

Use repository `.gitignore` for shared generated paths. Use `.git/info/exclude` or a global ignore file for personal machine preferences that do not belong in the shared project. Check nested ignore files, because they can override parent rules.

## Keep important files

Do not broadly ignore all dotfiles, all `config/`, all JSON/YAML, or all dependency lockfiles. Keep `uv.lock`, `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`, Cargo.lock where the project tracks it, and other real inputs needed to rebuild the project the same way. Application and library policies can differ. Do not remove an existing policy without a reason.

Extension rules for private material can collide with legitimate source. `*.key` also matches Apple Keynote documents, and `*.pem` can match a certificate that is public on purpose. Add a path-specific exception for such tracked source after confirming it contains no private key.

Keep Gradle wrapper scripts and required wrapper JARs. Do not ignore every JAR without checking. Keep shared Xcode project metadata while excluding per-user state. For JetBrains IDEs, keep shared `.idea/` files such as code styles and run configurations, and exclude per-user files such as `workspace.xml`, `tasks.xml`, `usage.statistics.xml`, `shelf`, `dictionaries` and local data-source files. A project `.npmrc` is shared configuration, so keep registry tokens out of it by referencing an environment variable such as `${NPM_TOKEN}` instead of ignoring the file. Keep `.env.example` only after you check that it holds sanitized names or placeholders, not live credentials. An exception rule is not a privacy review.

Generated `dist/` can stay out of Git and still be in an npm package's `files` allowlist. A docs or demo repository may track generated output on purpose. Check that purpose before you add broad rules. Do not ignore publication source PDFs, PNGs, fonts, or fixtures just because files with the same extension can be generated elsewhere.

## Existing exposure

`git ls-files` lists tracked paths, even when a new ignore pattern matches them. `git check-ignore --no-index` is useful for testing what a rule intends, but it does not mean a tracked file has become untracked. Review the index and history separately.

If a real secret is tracked, stop it from entering the next delivery, do not print it, find the affected credential, and arrange rotation through the authorized owner or tooling. Removing the current file or editing `.gitignore` does not revoke a leaked key. History rewriting, remote deletion, or account changes need the right task scope.

## Verification

Create typical temporary paths in an isolated copy when you test patterns. Check that `.venv/`, `node_modules/`, build output, logs, credential files, and OS metadata are excluded. Check that source modules, lockfiles, examples, wrappers, and shared settings are still visible. Use rules for exact paths when a broad extension would hide valid source fixtures.
