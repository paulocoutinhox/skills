# Evidence-based review procedure

## Establish scope

Read the repository guidance, the task's intent, the base/head identity, the full changed-file list, and the complete diff. For a PR, prefer the correct merge-base comparison, and understand whether the task asks about the head branch or the merged result. For uncommitted work, tell staged, unstaged, and untracked changes apart. Do not quietly include unrelated changes in the review result.

Read enough of each implementation to understand its contracts. Diff hunks can leave out an existing helper, rule, or import. Check those before you flag missing behavior. Generated files, deleted files, configuration, migrations, and lockfiles can matter more than added source and need careful review.

## Review dimensions

| Dimension | Questions |
| --- | --- |
| Behavior | Does the code, as it really runs, meet the task for normal, empty, edge, and invalid input? |
| Integration | Which unchanged callers depend on the old return value, event shape, import, lifecycle, or timing? |
| Data | Are transactions, constraints, schema changes, migrations, serialization, caches, and deletion semantics consistent? |
| Permissions | Can another user or tenant access, mutate, enumerate, export, or subscribe to data? |
| Resources | Are files, network clients, tasks, subscriptions, native memory, and locks owned and cleaned up? |
| Concurrency | Can cancellation, stale responses, races, duplicate work, retries, or deadlocks change the result? |
| Failure | Are errors visible and meaningful? Can partial success be mistaken for full success? |
| Performance | Are there unlimited loops, N+1 requests, expensive queries, excessive memory, or UI-thread work? |
| API | Are public entrypoints, types, errors, status codes, payloads, and version requirements consistent? |
| Delivery | Does the real build, package, environment, and deployment include what the new behavior needs? |
| Maintenance | Is the architecture easy to understand and consistent with the real project instructions? |

Put defects and important requirements first. A personal style preference is not a correctness bug. Raise an architecture concern only when you can support its real effect on maintenance or behavior. Avoid automated-review noise about harmless formatting, guessed edge cases with no path, or refactors unrelated to the change. One formatting pattern is not harmless noise under this collection's convention: a single call wrapped across continuation lines because the formatter width is narrow, for example clang-format `ColumnLimit: 80` or Prettier `printWidth: 80`. Report it once against the formatter configuration, as described in the entrypoint.

## Validation

Use real inputs and isolated fixtures. Run focused tests, builds, type checks, linters, or a minimal reproducer that fits the concern. Do not run destructive production tests. Reuse the existing environment where possible. Look into unexpected failures, and tell failures that already existed apart from new ones. Record clearly which environments were not available.

Check a proposed finding again against the latest reviewed head before delivery. A line number from an outdated revision can mislead a reviewer. Do not repeat the same root cause across many comments. Include the other affected call sites in the finding or impact summary.
