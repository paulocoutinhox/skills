# Evidence-based review procedure

## Establish scope

Inspect repository guidance, task intent, base/head identity, the full changed-file list, and the complete diff. For a PR, prefer the correct merge-base comparison and understand whether the task asks for the head branch or integration result. For uncommitted work, distinguish staged, unstaged, and untracked changes. Do not silently include unrelated modifications in the review result.

Read enough of each implementation to understand its contracts. Diff hunks can omit an existing helper, invariant, or import. Verify those before flagging missing functionality. Generated files, deleted files, configuration, migrations, and lockfiles can be more consequential than source additions and need deliberate review.

## Review dimensions

| Dimension | Questions |
| --- | --- |
| Behavior | Does the actual execution satisfy the task for normal, empty, boundary, and invalid input? |
| Integration | Which unchanged callers depend on the old return value, event shape, import, lifecycle, or timing? |
| Data | Are transactions, constraints, schema changes, migrations, serialization, caches, and deletion semantics consistent? |
| Permissions | Can another user or tenant access, mutate, enumerate, export, or subscribe to data? |
| Resources | Are files, network clients, tasks, subscriptions, native memory, and locks owned and cleaned up? |
| Concurrency | Can cancellation, stale responses, races, duplicate work, retries, or deadlocks change the result? |
| Failure | Are errors visible and meaningful? Can partial success be mistaken for full success? |
| Performance | Are there unbounded loops, N+1 requests, expensive queries, excessive memory, or UI-thread work? |
| API | Are public entrypoints, types, errors, status codes, payloads, and version requirements coherent? |
| Delivery | Does the real build, package, environment, and deployment include what the new behavior needs? |
| Maintenance | Is the architecture understandable and consistent with actual project instructions? |

Prioritize defects and material requirements. A personal style preference is not a correctness bug. Mention an architecture concern only when its actual maintenance or behavior impact is supported. Avoid automated-review noise about harmless formatting, speculative edge cases without a path, or refactors unrelated to the change.

## Validation

Use real inputs and isolated fixtures. Run focused tests, builds, type checks, linters, or a minimal reproducer appropriate to the concern. Do not perform destructive production tests. Reuse the existing environment where possible. Inspect unexpected failures and distinguish baseline failures from introduced ones. Record unavailable environments explicitly.

Recheck a proposed finding against the latest reviewed head before delivery. A line number from an obsolete revision can mislead a reviewer. Do not duplicate the same root cause across many comments. Include the other affected call sites in the finding or impact summary.
