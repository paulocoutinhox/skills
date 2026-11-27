---
name: git
description: Check repository state, prepare branches named after the task, stage only intended changes, fix local Git issues, and create one reviewed commit with a human author. Use for Git organization and commit preparation without an implied push or history rewrite.
license: MIT
---

# Git

Produce a planned repository snapshot. A correct commit holds the intended change, uses the correct identity and task context, passes the relevant checks, and keeps unrelated user work.

## Understand the three states

The working tree contains current files. The index contains the proposed next snapshot. `HEAD` identifies the current commit. These can all differ. A commit records the index, so a file edited after staging may hold changes that the commit will not include.

Check `git status --short --branch`, unstaged `git diff`, staged `git diff --cached`, and untracked filenames before acting. Use `git rev-parse --show-toplevel` when you are not sure which repository you are in. Never assume the open editor file, current branch name, or last shown diff defines the whole scope.

Read repository instructions and the user's intended deliverable. Find existing changes, already staged changes, merge or rebase state, and the configured author. Do not reset, clean, stash, switch branches, or amend just to make the working tree easier to handle.

Respect a stated main-only or no-pull-request workflow. In that case, work on the authorized main
branch and create the requested single local commit without creating a feature branch, PR, merge
commit, or dependency-update bot. The branch examples below apply only where branch creation is part
of the target repository's requested workflow. They do not override local instructions.

## Task-aware naming

Use an issue or task ID that was already given. Ask once, and only if it is truly unknown and matters. Keep its exact case. Keep the rest lowercase, short and imperative.

| Context | Branch example | Commit example |
| --- | --- | --- |
| Task key | `UBKMI-1234-fix-player` | `UBKMI-1234 fix player` |
| Numeric issue | `123-fix-player` | `123 fix player` |
| No task key | `fix-player-stop` | `fix: stop player correctly` |
| New capability | `feat-book-export` | `feat: add book export` |

Choose the conventional type for the real final result, including `feat`, `fix`, `docs`, `build`, `ci`, `refactor`, `perf`, or `test`. Do not put tool names, research sources, generated attribution, or co-author trailers in commits. Use the real configured human identity.

## Build and inspect the intended snapshot

Review changed filenames before you open contents that may be sensitive. Sort source, documentation, configuration, generated output and private material. Look for environment files, logs, signing keys, credentials, runtime databases, screenshots with personal information and package or build archives. Do not print secret values during review.

Stage explicit paths. Use partial staging only when unrelated changes share a file and the chosen hunks form a complete, consistent result. Read the staged diff again after every real edit. `git diff --cached --check` finds whitespace errors, not missing functionality or private data.

Run the checks that fit the staged behavior. If tests use unstaged changes, the checkout that passed may differ from the proposed commit. Fix that mismatch through careful staging or a check on an isolated snapshot. Do not claim the committed content was tested just because some version of the working tree passed.

Before committing, check staged names, content, deletions, file modes, submodule references and lockfiles. An unexpected executable bit or a deleted shared configuration can matter a lot even when the source code is correct.

## Common decisions

If a temporary build file was staged accidentally, `git restore --staged -- path` removes it from the proposed snapshot and keeps the working file. Confirm the path and check the new index state. Do not use a hard reset for an index-only correction.

If a private file is already tracked, `.gitignore` does not untrack it. `git rm --cached -- <path>` stages its removal from the index and keeps the local file. Plain `git rm` deletes the working copy too, so confirm the exact path and command before running it. An exposed credential also needs rotation and approved incident handling. Deleting a line from the next commit does not revoke a leaked key.

If there is a merge conflict, understand both intended behaviors and the common base. Resolve the contract instead of picking “ours” or “theirs” for everything. Check for leftover markers, removed validation, repeated sections and changed tests. Validate the combined result, including callers outside the conflict hunk.

If another operation changes the branch or index while you prepare, stop making changes and read the state again. Do not overwrite another process's index lock, or delete a lock without knowing who owns it. Separate worktrees help with truly independent work. They are not a reason to lose the user's current changes.

## Commit and recovery

Create one short commit per delivery. Check the new commit and the remaining working tree. A failed hook or failed commit is a failure to look into, not permission to skip safeguards. An amend needs ownership and authorization, especially when you are not sure whether the commit was published.

For a local mistake, first find out whether the fix concerns the working tree, index, commit, or branch reference. Keep content you can recover and use the smallest fitting operation. Reflog can help find earlier references, but it does not justify careless destructive commands.

A commit does not authorize push, tag, release, force push or rewriting published history. Report the hash, subject, relevant checks and whether changes remain. Do not state that GitHub CI passed when only local checks ran.

## Explicit single-root history and repository cleanup

Tell one commit for a normal change apart from a clear request to replace all branch history
with one parentless snapshot. The second needs rewrite authorization that applies, and remote
publication needs its real named scope. Keep the complete source and owner changes, check
incoming remote state, update refs with expected-old checks and publish only with an explicit SHA
lease when authorized. Do not remove `.git` or treat rewriting as credential erasure.

Follow [the single-snapshot procedure](references/single-snapshot.md) only for that requested mode.
It covers a reviewed index, amending an existing root versus building a new root, hook boundaries,
concurrent changes, publication and recovery and exact remote CI verification. Follow main-only
rules and keep existing authorization without inventing a branch, a PR or an extra confirmation
step.

## Foundations and further detail

Scott Chacon and Ben Straub's [Pro Git](https://git-scm.com/book/en/v2), especially [Reset Demystified](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified), explains the working-tree/index/commit model used here. The [Git reference](https://git-scm.com/docs) defines exact command behavior. For safe recovery, these help more than memorized command recipes without a model of the state.

Read [the workflow reference](references/workflow.md) for additional examples and [sources](references/sources.md) for the research base. [License](LICENSE.md).
