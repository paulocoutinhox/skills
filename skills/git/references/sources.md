# Sources

Verified: 2026-11-05.

- [Git status](https://git-scm.com/docs/git-status): checking the index and working tree.
- [Git diff](https://git-scm.com/docs/git-diff): staged changes, whitespace checking, and review modes.
- [Git commit](https://git-scm.com/docs/git-commit): commit author, messages, and amend behavior.
- [Git ignore](https://git-scm.com/docs/gitignore): limits for tracked files and pattern meaning.
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/): no-identifier message vocabulary. Task-key messages are this collection's chosen convention.

## Professional foundation and evidence scope

Reviewed: 2026-11-05. Scott Chacon and Ben Straub's [Pro Git](https://git-scm.com/book/en/v2), particularly [Reset Demystified](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified), gives the working-tree/index/commit model used by the recovery and staging procedure. The Git reference still defines exact commands.

Stored content is maintained only when the user requests a revision. There is no automatic source collector or refresh process.

## Explicit root-snapshot operations

Checked **2026-11-05** against [commit-tree](https://git-scm.com/docs/git-commit-tree),
[update-ref](https://git-scm.com/docs/git-update-ref) and [push](https://git-scm.com/docs/git-push).
Leaving out parent arguments builds a root. Expected-old local ref updates catch concurrent changes.
An explicit remote SHA lease protects that observed branch tip no matter what background fetches do.
These mechanics do not authorize history replacement, skip hooks, erase all hosted objects or
rotate exposed credentials. Real repository or user instructions decide when to use the optional
snapshot procedure. No repository was rewritten to demonstrate it.

## Remote CI inspection

Checked **2026-11-18** against the GitHub CLI manual for [gh run list](https://cli.github.com/manual/gh_run_list) and [gh run watch](https://cli.github.com/manual/gh_run_watch). `--commit` filters runs by commit SHA and `--exit-status` makes the watch fail when the run fails. These commands require an authenticated GitHub CLI with access to the repository.
