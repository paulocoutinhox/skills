# Sources

Verified: 2026-11-05.

- [Git status](https://git-scm.com/docs/git-status): index and working-tree inspection.
- [Git diff](https://git-scm.com/docs/git-diff): staged changes, whitespace checking, and review modes.
- [Git commit](https://git-scm.com/docs/git-commit): commit author, messages, and amend behavior.
- [Git ignore](https://git-scm.com/docs/gitignore): tracked-file limitations and pattern semantics.
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/): no-identifier message vocabulary. Task-key messages are this collection's chosen convention.

## Professional foundation and evidence scope

Reviewed for this revision: 2026-11-05. Scott Chacon and Ben Straub's [Pro Git](https://git-scm.com/book/en/v2), particularly [Reset Demystified](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified), provides the working-tree/index/commit model used by the expanded recovery and staging procedure. Exact commands remain governed by the Git reference.

Stored content is maintained only when the user requests a revision. There is no automated source collector or refresh mechanism.

## Explicit root-snapshot operations

Checked **2026-11-05** against [commit-tree](https://git-scm.com/docs/git-commit-tree),
[update-ref](https://git-scm.com/docs/git-update-ref) and [push](https://git-scm.com/docs/git-push).
Omitting parent arguments constructs a root. Expected-old local ref updates detect concurrency.
An explicit remote SHA lease protects that observed branch tip independently of background fetches.
These mechanics do not authorize history replacement, bypass hooks, erase all hosted objects or
rotate exposed credentials. The optional snapshot procedure is selected by actual repository/user
instructions. This authoring pass did not rewrite another repository to demonstrate it.
