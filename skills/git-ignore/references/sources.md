# Sources

Verified: 2026-11-05.

- [Git ignore specification](https://git-scm.com/docs/gitignore): precedence, negation, directories, and tracked-file limitations. Rechecked on 2026-11-05 to distinguish anchoring by a leading/middle slash from directory-only matching by a trailing slash.
- [Git check-ignore](https://git-scm.com/docs/git-check-ignore): verbose diagnostics and index-aware behavior.
- [GitHub ecosystem templates](https://github.com/github/gitignore): useful stack-specific comparison source. Inspect relevant templates before adapting. Preserve licenses if copying their contents.
- [GitHub removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository): exposure remediation beyond ignore rules.
- [Playwright Python authentication](https://playwright.dev/python/docs/auth): recommends ignoring `playwright/.auth/` because saved browser state can contain reusable cookies and headers. Rechecked on 2026-11-05 for the browser-state exclusion.

Ignore patterns are repository-specific hygiene. They are neither access controls nor a substitute for secret scanning and rotation.

## Professional foundation and evidence scope

Reviewed for this revision: 2026-11-05. [Pro Git: Recording Changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) supports the tracked/index distinction. The [gitignore manual](https://git-scm.com/docs/gitignore) governs actual negation/precedence. Borrowed ecosystem patterns do not supersede these semantics or the repository's real source/lockfile needs.

Stored content is maintained only when the user requests a revision. There is no automated source collector or refresh mechanism.
