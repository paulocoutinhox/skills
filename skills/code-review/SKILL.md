---
name: code-review
description: Review a change in depth, trace its impact on the whole project, and report concrete defects someone can act on, with evidence, severity and verification. Use for diffs, pull requests, staged work or a requested repository-wide engineering assessment.
license: MIT
---

# Code Review

Understand the change as a whole system before you judge single lines. Find defects that can happen in supported use, explain their effect, and drop guesses with no real path. Unless the user asks for fixes, the result is an assessment, not a rewrite nobody asked for.

A code review reports security defects it finds in the reviewed change. A requested security assessment of a whole system, with a threat model, authorization matrix and abuse testing across its entrypoints, is a separate security-audit scope. Both use the same four severity levels defined below.

## Establish exactly what is reviewed

Find the task, reviewed revision, base/head or merge base, complete file list and working-tree state. Tell a PR branch apart from its merged result. Tell staged, unstaged and untracked content apart. Read project instructions and acceptance criteria.

Read enough of the surrounding code to find the real entrypoints, helpers, rules and framework wiring. A diff may leave out an existing authorization check or lifecycle owner. Check them before you report a missing control. Generated files, deleted files, migrations, manifests and release configuration need careful review.

## Build the execution and impact map

Start from changed inputs or contracts, and trace both dependencies and consumers. Search symbols, imports, routes, event names, saved fields, configuration keys, cache prefixes and package exports. Check dynamic registries and framework wiring when text search cannot show whether code is reachable.

| Change | Follow through |
| --- | --- |
| Return type/error | Every caller, serializer, UI error state, CLI exit status and test double |
| Persisted field | Constraints, migration, reads/writes, imports, exports, jobs and indexes |
| Authorization | Lists, details, mutations, files, previews, exports, websocket/jobs and caches |
| Async behavior | Owner lifetime, cancellation, stale completion, shutdown and retries |
| Dependency/toolchain | Runtime, peers, lockfile, native ABI, build image and shipped entrypoints |
| Release | Identity, trigger trust, built artifact, final package, version and rollout |

A correct local refactor can fail during deployment if other running components still use the old event or schema. Find the real coordination or migration need without inventing a permanent compatibility layer.

## Inspect professional risk dimensions

Check behavior against real normal, empty, invalid and edge inputs. Tell a successful empty result apart from a hidden failure. Look for a partial change followed by an error that is reported as success.

Check state and data rules. For uniqueness, balances, stock and fulfillment, a read done first does not protect against concurrent requests. Find the source-of-truth constraint, transaction or idempotency mechanism, and check the order of durable writes and side effects.

Check resources and lifetime. Follow file handles, streams, threads, tasks, observers, timers, native objects and lock ownership. Check cleanup on failure and cancellation. Do not assume garbage collection or async syntax proves correct lifetime.

Check performance only against a real path and scale. Explain an N+1 query, unlimited allocation, repeated costly render or query complexity with what triggers it. Do not demand caching or abstraction without a proven need.

Check security at the source-of-truth boundary. A hidden button, opaque object ID or client type annotation does not authorize a server operation. Trace tenant scope into alternate routes, exports and background jobs.

Judge maintainability by concrete effects. Unclear ownership or repeated rules can make behavior drift apart, but a personal naming preference is not a defect by itself. Do not mix optional polish with findings that block a release.

Under this collection's owner convention, treat a single function or method call whose arguments wrap across continuation lines because of a narrow formatter width, such as clang-format `ColumnLimit: 80` or Prettier's default `printWidth` of 80, as a formatter-configuration finding, not acceptable style. Find the setting that causes it, including an `.editorconfig` `max_line_length` that Prettier reads as its print width or ktlint reads as its line width. Recommend each tool's no-wrap configuration: clang-format `ColumnLimit: 0`, Ruff `line-length = 320` with `skip-magic-trailing-comma = true`, rustfmt `max_width = 320` with `use_small_heuristics = "Max"`, and a width of 320 in each tool's own width setting for Prettier, StyLua, swift-format and ktlint. Also recommend named intermediate variables for complex arguments and joining calls that are already wrapped, because some formatters, including clang-format under a zero limit, keep existing breaks. Report it once at the configuration root with the affected paths, normally as Low. Splitting one string literal into adjacent literals across lines belongs to the same finding. If the project clearly documents the narrow limit as its convention, report the conflict for the owner to decide instead of rewriting the configuration without being asked.

## Worked finding and false-positive check

Suppose the modified download endpoint reads a report by ID and returns its file. Before you report a cross-tenant leak, check the middleware, the repository query and the storage policy. If the query already takes tenant scope from trusted session context, drop the suspicion.

If the real query has no scope, reproduce it with two controlled tenants or show the complete source path. Explain that tenant A can get tenant B's existing report by sending its ID. The fix belongs in the source-of-truth lookup or policy and must cover preview and export paths too. Replacing the ID with a UUID would not fix the root cause.

A useful finding contains:

1. A short title that names the real defect.
2. The exact current location and a trigger that can be reached.
3. Behavior that was observed or proven from source, and its effect on users or the system.
4. Relevant prerequisites, affected consumers and impact scope.
5. A direction for the fix and a useful verification case.
6. Confidence and missing evidence when they apply.

Do not claim run evidence for reasoning you did only by reading code. Do not repeat one root cause in many comments.

## Severity and validation

Critical means proven severe, broad compromise or corruption, or a catastrophic failure that can be reached. High means significant impact on an important path. Medium means real but limited impact under a supported condition. Low means a concrete minor defect or a clear requirement violation. Confidence is separate from severity.

Use focused existing tests, a minimal reproducer, build and type checks, isolated consumer tests or relevant native diagnostics. Tell failures that already existed apart from failures the change added. Do not run destructive production tests. Check each finding again against the final reviewed revision, including its line number.

See [the impact guide](references/impact.md), [assessment procedure](references/procedure.md), [finding guide](references/findings.md) and [report template](assets/impact-review.md) for more detail.

## Professional foundations and delivery

[Google Engineering Practices](https://google.github.io/eng-practices/review/reviewer/) gives a proven review framework. The publicly available code-review chapter of [Software Engineering at Google](https://abseil.io/resources/swe-book/html/ch09.html) gives broader engineering context. Bacchelli and Bird's ICSE 2013 study, [Expectations, Outcomes, and Challenges of Modern Code Review](https://www.microsoft.com/en-us/research/publication/expectations-outcomes-and-challenges-of-modern-code-review/), supports a focus on understanding the change and sharing knowledge, not on counting comments. Its findings from industry do not promise anything about how accurate AI review is.

Start the report with findings someone can act on. Give them in the conversation by default, and use the report template when the user asks for a written impact review. If you found none, say so without certifying the project free of defects. State the revision, covered paths, checks and limits. When fixes were authorized, fix the real issues, validate affected consumers, and report the final state. This descriptive skill bundles no review bots, scanners or auto-fix tools. See [sources](references/sources.md) and [license](LICENSE.md).
