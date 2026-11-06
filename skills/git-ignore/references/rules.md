# Ignore semantics and privacy

Patterns with no slash except an optional trailing slash can match at any depth below the configuration directory. A slash at the beginning or in the middle anchors the path to that directory. A trailing slash restricts matching to directories, without itself anchoring depth. In a root ignore file, `build/` matches root and nested build directories, `/build/` matches only the root build directory, and `apps/web/build/` matches that specific relative directory rather than `examples/apps/web/build/`.

`**` can span directories. A leading `!` negates an earlier rule, but a file inside an ignored parent cannot be restored without making the relevant parent traversable. Later applicable patterns win at the same precedence level. Escape literal `#` or `!` where needed.

Use repository `.gitignore` for shared generated paths. Use `.git/info/exclude` or a global ignore file for personal machine preferences that do not belong in the shared project. Inspect nested ignore files because they can override parent rules.

## Keep important files

Do not broadly ignore all dotfiles, all `config/`, all JSON/YAML, or all dependency lockfiles. Preserve `uv.lock`, `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`, Cargo.lock where the project tracks it, and other actual reproducibility inputs. Application and library policies can differ. Do not erase an existing policy without a reason.

Preserve Gradle wrapper scripts and required wrapper JARs. Do not ignore every JAR indiscriminately. Preserve shared Xcode project metadata while excluding per-user state. Preserve `.env.example` only after verifying that it contains sanitized names or placeholders rather than live credentials. An exception rule is not a privacy review.

Generated `dist/` can stay out of Git while remaining in an npm package's `files` allowlist. A docs or demo repository may intentionally track generated output. Inspect that purpose before adding broad rules. Do not ignore publication source PDFs, PNGs, fonts, or fixtures merely because the same extension can be generated elsewhere.

## Existing exposure

`git ls-files` identifies tracked paths, even when a new ignore pattern matches them. `git check-ignore --no-index` is useful for testing rule intent, but does not mean a tracked file has become untracked. Review the index and history separately.

If an actual secret is tracked, stop it from entering the next delivery, avoid echoing it, identify the affected credential, and arrange rotation through the authorized owner or tooling. Removing the current file or editing `.gitignore` does not revoke a leaked key. History rewriting, remote deletion, or account changes require the appropriate task scope.

## Verification

Create representative temporary paths in an isolated copy when testing patterns. Check that `.venv/`, `node_modules/`, build output, logs, credential files, and OS metadata are excluded. Check that source modules, lockfiles, examples, wrappers, and shared settings are still visible. Use path-specific rules when a broad extension would hide legitimate source fixtures.
