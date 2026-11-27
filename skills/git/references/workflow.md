# Branches, commits, and staged-file review

## Naming

| Context | Branch | Commit |
| --- | --- | --- |
| Issue key | `UBKMI-1234-fix-player` | `UBKMI-1234 fix player` |
| Numeric issue in a repository | `123-fix-player` | `123 fix player` |
| No issue | `fix-player-stop` | `fix: stop player correctly` |
| New capability without issue | `feat-book-export` | `feat: add book export` |
| Documentation without issue | `docs-installation` | `docs: explain installation` |

Use `feat`, `fix`, `build`, `ci`, `docs`, `style`, `refactor`, `perf`, `test`, or `chore` according to the real change. Keep wording short, imperative, and lowercase outside the task key. Use hyphens in branch descriptions. Do not replace an issue key with an invented lowercase version. Do not switch branches if that would mix or lose unrelated changes. Existing task authorization and an ID already given stay valid.

## Precommit procedure

```bash
git status --short --branch
git diff --stat
git diff
git ls-files --others --exclude-standard
git status --ignored --short
```

Review filenames before you open contents that may be private. Check relevant tracked and untracked text for credentials without printing secret values. Prefer a configured redacting secret scanner. Look for `.env`, private keys, signing stores, cloud credentials, access tokens, service accounts, database dumps, screenshots with personal data, local connection strings, crash reports, and logs. A scanner gives evidence, not proof that nothing is there.

Stage explicit paths, then check:

```bash
git diff --cached --name-status
git diff --cached --stat
git diff --cached --check
git diff --cached
```

Run the project's format, lint, build, and behavior checks that fit the changes. Do not hide failing checks or skip hooks to claim the work is done. If existing failures are unrelated, document their evidence and scope.

A single delivery gets one commit. If a local unfinished commit must be amended, check who owns it and whether it was published first, and amend only within your authorization. Do not amend somebody else's work. A published change usually gets a new fixing commit unless rewriting is clearly authorized.

## Sensitive files already tracked

Ignore rules apply to untracked paths. When you remove a tracked local-only file from version control, check the path and use `git rm --cached -- <path>` only for the intended file, keeping its local copy. An exposed credential also needs rotation and a properly authorized plan to clean up history. Never claim adding an ignore pattern revokes a credential.

## Delivery

Report what the commit changes, its hash and subject, the checks that really ran, and whether unrelated modifications remain. No agent attribution belongs in the commit subject, body, trailers, or author fields. Attribution required by a source license belongs in the repository's license notices, not an invented commit footer.
