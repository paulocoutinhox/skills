# Sources

Verified: 2026-11-05.

- [Git ignore specification](https://git-scm.com/docs/gitignore): precedence, negation, directories, and tracked-file limitations. Rechecked on 2026-11-05 to tell anchoring by a leading or middle slash apart from directory-only matching by a trailing slash.
- [Git check-ignore](https://git-scm.com/docs/git-check-ignore): verbose diagnostics and index-aware behavior.
- [GitHub ecosystem templates](https://github.com/github/gitignore): a useful source to compare stacks. Read the relevant templates before adapting them. Keep their licenses if you copy their contents.
- [GitHub removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository): exposure remediation beyond ignore rules.
- [Playwright Python authentication](https://playwright.dev/python/docs/auth): recommends ignoring `playwright/.auth/` because saved browser state can contain reusable cookies and headers. Rechecked on 2026-11-05 for the browser-state exclusion.

Ignore patterns are housekeeping for one repository. They are not access controls, and they do not replace secret scanning and rotation.

## Professional foundation and evidence scope

Reviewed: 2026-11-05. [Pro Git: Recording Changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) supports the tracked/index distinction. The [gitignore manual](https://git-scm.com/docs/gitignore) defines the real negation and precedence. Patterns borrowed from other ecosystems do not override these rules or the repository's real source and lockfile needs.

Stored content is maintained only when the user requests a revision. There is no automatic source collector or refresh process.

Checked 2026-11-18. GitHub's maintained [JetBrains ignore template](https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore), which cites JetBrains' version-control support article, lists the per-user `.idea/` files the asset excludes while shared project files remain tracked. The [npm configuration documentation](https://docs.npmjs.com/cli/v12/configuring-npm/npmrc/) supports environment-variable replacement in `.npmrc` values.
