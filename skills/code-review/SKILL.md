---
name: code-review
description: Review a change deeply, trace its whole-project impact, and report concrete actionable defects with evidence, severity and verification. Use for diffs, pull requests, staged work or requested repository-wide engineering assessment.
license: MIT
---

# Code Review

Understand the change as a system before judging individual lines. Find defects that can occur in supported execution, explain their effect, and reject speculative noise. Unless fixes are requested, the result is an assessment rather than an unsolicited rewrite.

## Establish exactly what is reviewed

Identify the task, reviewed revision, base/head or merge base, complete file list and working-tree state. Distinguish a PR branch from its integrated merge result. Distinguish staged, unstaged and untracked content. Read project instructions and acceptance criteria.

Read enough surrounding implementation to identify actual entrypoints, helpers, invariants and framework wiring. A diff may omit an existing authorization check or lifecycle owner. Verify them before reporting a missing control. Generated files, deleted files, migrations, manifests and release configuration need deliberate review.

## Build the execution and impact map

Start from changed inputs or contracts and trace both dependencies and consumers. Search symbols, imports, routes, event names, persisted fields, configuration keys, cache prefixes and package exports. Inspect dynamic registries/framework wiring when text search cannot establish reachability.

| Change | Follow through |
| --- | --- |
| Return type/error | Every caller, serializer, UI error state, CLI exit status and test double |
| Persisted field | Constraints, migration, reads/writes, imports, exports, jobs and indexes |
| Authorization | Lists, details, mutations, files, previews, exports, websocket/jobs and caches |
| Async behavior | Owner lifetime, cancellation, stale completion, shutdown and retries |
| Dependency/toolchain | Runtime, peers, lockfile, native ABI, build image and shipped entrypoints |
| Release | Identity, trigger trust, built artifact, final package, version and rollout |

A correct local refactor can fail during deployment if other running components still consume the old event or schema. Identify the actual coordination/migration requirement without inventing a permanent compatibility layer.

## Inspect professional risk dimensions

Check functionality against real normal, empty, invalid and boundary inputs. Separate a successful empty result from a suppressed failure. Look for partial mutation followed by an error reported as success.

Check state and data invariants. For uniqueness, balances, stock and fulfillment, a preceding read is not sufficient protection against concurrent requests. Locate the authoritative constraint/transaction/idempotency mechanism and inspect ordering of durable writes and side effects.

Check resources and lifetime. Follow file handles, streams, threads, tasks, observers, timers, native objects and lock ownership. Inspect cleanup on failure and cancellation. Avoid assuming garbage collection or async syntax proves correct lifetime.

Check performance only against an actual path and scale. Explain an N+1 query, unbounded allocation, repeated expensive render or query complexity with a trigger. Do not demand caching or abstraction without demonstrated need.

Check security at the authoritative boundary. A hidden button, opaque object ID or client type annotation does not authorize a server operation. Trace tenant scope into alternate routes, exports and background jobs.

Check maintainability through concrete consequences. Difficult ownership or duplicated rules can cause divergent behavior, but a personal naming preference is not automatically a defect. Do not mix optional polish with release-blocking findings.

## Worked finding and false-positive check

Suppose the modified download endpoint reads a report by ID and returns its file. Before reporting a cross-tenant disclosure, inspect middleware, the repository query and storage policy. If the query already derives tenant scope from trusted session context, reject the suspicion.

If the actual query is unscoped, reproduce with two controlled tenants or establish the complete source path. Explain that tenant A can obtain tenant B's existing report by supplying its ID. The remedy belongs in the authoritative lookup/policy and must cover preview/export paths too. Replacing the ID with a UUID would not fix the root cause.

A useful finding contains:

1. A short title identifying the actual defect.
2. Exact current location and reachable trigger.
3. Observed or source-proven behavior and user/system consequence.
4. Relevant prerequisites, affected consumers and impact scope.
5. A corrective direction and a meaningful verification case.
6. Confidence and missing evidence when applicable.

Do not claim execution evidence for static reasoning. Do not duplicate one root cause into many comments.

## Severity and validation

Critical means demonstrated severe broad compromise/corruption or catastrophic reachable failure. High means significant impact on an important path. Medium means meaningful bounded impact under a supported condition. Low means a concrete minor defect or explicit requirement violation. Confidence is separate from severity.

Use focused existing tests, a minimal reproducer, build/type checks, isolated consumer tests or relevant native diagnostics. Distinguish baseline failures from introduced failures. Do not run destructive production tests. Recheck each finding against the final reviewed revision, including its line number.

Use [the impact guide](references/impact.md), [assessment procedure](references/procedure.md), [finding guide](references/findings.md) and [report template](assets/impact-review.md) for additional detail.

## Professional foundations and delivery

[Google Engineering Practices](https://google.github.io/eng-practices/review/reviewer/) provides an experienced inspection framework. The publicly available code-review chapter of [Software Engineering at Google](https://abseil.io/resources/swe-book/html/ch09.html) gives broader engineering context. Bacchelli and Bird's ICSE 2013 study, [Expectations, Outcomes, and Challenges of Modern Code Review](https://www.microsoft.com/en-us/research/publication/expectations-outcomes-and-challenges-of-modern-code-review/), supports emphasizing change understanding and knowledge transfer rather than counting comments. Its industrial observations are not a guarantee about AI review accuracy.

Lead the report with actionable findings. If none were found, say so without certifying the project defect-free. State revision, covered paths, checks and limitations. When fixes were authorized, correct justified issues, validate affected consumers, and report the final state. No review bots, scanners or auto-fix machinery are bundled with this descriptive skill. See [sources](references/sources.md) and [license](LICENSE.md).
