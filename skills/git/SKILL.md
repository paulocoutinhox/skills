---
name: git
description: Inspect repository state, prepare task-aware branches, stage only intended changes, resolve local Git issues, and create one reviewed human-authored commit. Use for Git organization and commit preparation without implied push or history rewriting.
license: MIT
---

# Git

Produce an intentional repository snapshot. A correct commit contains the intended change, uses the correct identity and task context, passes relevant checks, and preserves unrelated user work.

## Understand the three states

The working tree contains current files. The index contains the proposed next snapshot. `HEAD` identifies the current commit. These can all differ. A commit records the index, so a file edited after staging may contain changes that the commit will not include.

Inspect `git status --short --branch`, unstaged `git diff`, staged `git diff --cached`, and untracked filenames before acting. Use `git rev-parse --show-toplevel` when the repository is uncertain. Never assume the active editor file, current branch name, or last displayed diff defines the entire scope.

Read repository instructions and the user's intended deliverable. Identify existing modifications, already staged changes, merge/rebase state, and the configured author. Do not reset, clean, stash, switch branches, or amend simply to make the working tree convenient.

Respect an explicit main-only or no-pull-request workflow. In that case, work on the authorized main
branch and create the requested single local commit without creating a feature branch, PR, merge
commit, or dependency-update bot. The branch examples below apply only where branch creation is part
of the target repository's requested workflow. They do not override local instructions.

## Task-aware naming

Use an existing supplied issue/task identifier. Ask once only if it is genuinely unknown and consequential. Preserve its exact case. Keep the rest lowercase, short and imperative.

| Context | Branch example | Commit example |
| --- | --- | --- |
| Task key | `UBKMI-1234-fix-player` | `UBKMI-1234 fix player` |
| Numeric issue | `123-fix-player` | `123 fix player` |
| No task key | `fix-player-stop` | `fix: stop player correctly` |
| New capability | `feat-book-export` | `feat: add book export` |

Choose the conventional type for the actual final result, including `feat`, `fix`, `docs`, `build`, `ci`, `refactor`, `perf`, or `test`. Do not put tool names, research sources, generated attribution, or co-author trailers in commits. Use the real configured human identity.

## Build and inspect the intended snapshot

Review changed filenames before opening potentially sensitive contents. Identify source, documentation, configuration, generated output and private material. Look for environment files, logs, signing keys, credentials, runtime databases, screenshots with personal information and package/build archives. Avoid printing secret values during review.

Stage explicit paths. Use partial staging only when unrelated changes share a file and the selected hunks can form a coherent result. Re-read the staged diff after every meaningful edit. `git diff --cached --check` finds whitespace errors, not missing functionality or private data.

Run the checks appropriate to the staged behavior. If tests use unstaged changes, the passing checkout may differ from the proposed commit. Resolve that mismatch through deliberate staging or an isolated snapshot check. Do not claim the committed content was tested merely because some version of the working tree passed.

Before committing, inspect staged names, content, deletions, file modes, submodule references and lockfiles. An unexpected executable bit or a deleted shared configuration can be consequential even when source code is correct.

## Common decisions

If a temporary build file was staged accidentally, `git restore --staged -- path` removes it from the proposed snapshot while preserving the working file. Confirm the path and inspect the new index state. Do not use a hard reset for an index-only correction.

If a private file is already tracked, `.gitignore` does not untrack it. Removing it from the index preserves the local file only when the actual command and path are chosen correctly. Credential exposure also requires rotation and authorized incident handling. Deleting a line from the next commit does not revoke a leaked key.

If a merge conflict exists, understand both intended behaviors and the common base. Resolve the contract rather than selecting “ours” or “theirs” globally. Check for unresolved markers, removed validation, duplicated sections and changed tests. Validate the integrated result, including callers outside the conflict hunk.

If another operation changes the branch/index during preparation, stop the mutation sequence and re-read state. Do not overwrite another process's index lock or delete a lock without understanding its owner. Separate worktrees are useful for genuinely independent work, not a reason to lose the user's current changes.

## Commit and recovery

Create one concise commit per delivery. Inspect the resulting commit and remaining working tree. A failed hook or failed commit is a failure to investigate, not permission to bypass safeguards. An amend requires ownership and authorization, especially when publication state is uncertain.

For a local mistake, first identify whether the desired correction concerns the working tree, index, commit, or branch reference. Preserve recoverable content and use the smallest appropriate operation. Reflog can help locate prior references, but does not justify careless destructive commands.

A commit does not authorize push, tag, release, force push or rewriting published history. Report the hash, subject, relevant validation and whether changes remain. Do not state that GitHub CI passed when only local checks ran.

## Explicit single-root history and repository cleanup

Distinguish one commit for a normal change from an explicit request to replace all branch history
with one parentless snapshot. The latter needs applicable rewrite authorization, and remote
publication needs its actual named scope. Preserve complete source and owner changes, inspect
incoming remote state, update refs with expected-old checks and publish only with an explicit SHA
lease when authorized. Do not remove `.git` or treat rewriting as credential erasure.

Follow [the single-snapshot procedure](references/single-snapshot.md) only for that requested mode.
It covers a reviewed index, existing-root amend versus root construction, hook boundaries, concurrent
changes, publication/recovery and exact remote CI verification. Honor main-only rules and preserve
existing authorization without inventing a branch/PR or redundant confirmation flow.

## Foundations and further detail

Scott Chacon and Ben Straub's [Pro Git](https://git-scm.com/book/en/v2), especially [Reset Demystified](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified), explains the working-tree/index/commit model used here. The [Git reference](https://git-scm.com/docs) governs exact command behavior. These are more useful for safe recovery than memorized command recipes without a state model.

Read [the workflow reference](references/workflow.md) for additional examples and [sources](references/sources.md) for the research baseline. [License](LICENSE.md).
