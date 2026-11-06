---
name: code-developer
description: Implement and refactor production code with explicit contracts, readable responsibilities, current architecture guidance, and language-specific engineering. Use for real source changes in Python, Swift, Kotlin, C++, Rust, Lua, Markdown, JavaScript, TypeScript, Vue, React, and Angular.
license: MIT
---

# Code Developer

Implement the requested final behavior in the actual source files. Professional quality means the next maintainer can understand the contract, follow the execution, identify failures and change the system safely. Brevity, pattern counts and a large number of files are not quality metrics.

## Establish the contract and impact

Read repository instructions, manifests, architecture, relevant source, direct callers and existing tests. Identify the selected language/runtime, supported platform, public API and actual user acceptance criteria. Follow a coherent existing architecture. New Swift and Android projects without an architecture use the owner's MVVM default with separate models, views and view models.

Before editing, describe the important invariant in concrete terms. Examples include “a paid transaction grants this benefit at most once” or “only the active search request can replace the visible results.” Identify which component owns that invariant and where its authoritative state lives.

Trace the change through inputs, validation, domain operations, storage, background work and output. Include unchanged consumers. Removing source-level compatibility does not authorize corrupting persisted records or ignoring binaries still running during deployment. Choose an explicit migration/coordinated rollout when the final contract needs one.

## Write readable responsibilities

Use meaningful names and explicit intermediate values. Keep validation, calculation, mutation, I/O and return stages visually separated by blank lines. Prefer early returns when they make the path easier to follow. Do not use an unnecessary `else` after `return`, but retain a real exhaustive branch when the domain requires it.

Keep functions cohesive. Extract a responsibility when it is independently meaningful or genuinely shared. Do not fragment a simple flow into many one-line helpers or introduce interfaces, factories and generic layers for hypothetical future variation. A context-specific helper such as `CustomerHelper` is appropriate only when its responsibility is clear and justified.

Give each class, enum, component, screen or view its own appropriately named file. A supporting class
or enum also gets its own file, rather than becoming a second type beside a nominal primary class.
Follow valid language/tool filenames and required constructs. Hyphens are the default where legal,
but Python/Rust modules and framework-required names retain their idiomatic spelling. Avoid
duplicated business rules and generic utility buckets.

Comments are rare, in English, and explain necessary intention or context. Use complete sentences with a capital initial and final period. Rephrase instead of beginning a sentence with a required lowercase identifier. Do not split prose with semicolons or add decorative section comments. Required language punctuation, licenses, type-system safety notes and tooling directives retain their actual syntax.

## Errors, state and concurrency

Validate untrusted inputs at the actual boundary. Model expected failures explicitly and preserve useful context. Do not return empty collections, success values or a different product merely because an operation failed. Avoid generic fallback behavior, swallowed exceptions and old-format detection when the requested final contract does not need them.

Separate absence, loading, invalid input, failure and successful empty results. A network timeout does not prove a payment or upload was never accepted. Reconcile by a durable operation identifier before retrying a non-idempotent action.

Identify owners for tasks, streams, listeners, file handles, locks and native resources. Define cancellation and cleanup. Async/await, actors and memory-safe languages do not make a multi-step business operation atomic. Use the actual database constraint, transaction, lock or idempotency record that protects the invariant.

For replacement UI requests, cancellation alone may be insufficient if a response already completed. Bind results to the currently selected request/state generation and ignore an obsolete result deliberately. For shared file output, checking existence before writing does not prevent another writer from creating it. Use the supported atomic/no-overwrite operation and test the real race when relevant.

## Worked change: canceling an export

A request to cancel an export affects more than the button. Inspect the UI command, job creation, worker, temporary output, download route and completion notification. Define when cancellation becomes effective and what happens to an already committed result.

Keep the worker's state transition authoritative. Prevent a late completion from converting a canceled job back to success. Clean up only that job's owned temporary data. Preserve user source files. Ensure a stale notification cannot reveal a download belonging to another account. Update affected callers and statuses together, without retaining the old state model as a silent compatibility branch.

Meaningful verification covers cancellation before work, during work, after completion, and a completion/cancellation race. It also checks an unrelated user's request and source preservation. A test that merely repeats the same assignment as the implementation adds little confidence.

## Language-specific engineering

Read the profile for every changed language and the framework layer actually used:

| Target | Profile |
| --- | --- |
| Python | [Python](references/python.md) |
| Swift/Apple | [Swift](references/swift.md) |
| Kotlin/Android | [Kotlin](references/kotlin.md) |
| C++ | [C++](references/cpp.md) |
| Rust | [Rust](references/rust.md) |
| Lua | [Lua](references/lua.md) |
| Markdown | [Markdown](references/markdown.md) |
| JavaScript/TypeScript | [JavaScript and TypeScript](references/javascript-typescript.md) |
| React | [React](references/react.md) |
| Vue | [Vue](references/vue.md) |
| Angular | [Angular](references/angular.md) |
| Other language | [Profile research procedure](references/other-languages.md) |

The [general contract](references/general.md) gives detailed owner preferences. Empty Python `__init__.py` files, no `TYPE_CHECKING`, MVVM defaults, class-owned C++ functions and lambda format guards are owner conventions, not universal language requirements. Do not produce invalid framework code merely to imitate another language.

## Verification and delivery

Use the project's formatter, linter, type checker, compiler and focused behavioral tests. A transpiler is not necessarily a type checker. A successful build is not a memory, security or concurrency proof. Use release-mode/device/sanitizer/installed-consumer checks when the changed behavior makes them relevant.

Create or update root `AGENTS.md` with the current purpose, capabilities, layout, architecture, commands and boundaries. Use [the project template](assets/agents-template.md). Remove stale guidance and obsolete code within scope. Do not append task history.

Report the final behavior, affected consumers, checks executed, baseline/unresolved failures and material limitations. Keep dependencies current and compatible with the selected target, without gratuitous whole-project upgrades.

This skill contains descriptive engineering guidance. Do not create automation merely to demonstrate activity. Explicitly requested scripts use Python with uv and documented dependencies. Actual applications use their required implementation languages and native tooling.

## Professional foundations

[Software Engineering at Google](https://abseil.io/resources/swe-book/html/toc.html), edited by Titus Winters, Tom Manshreck and Hyrum Wright, supports reasoning about maintainable change and verification. The [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) offer concrete ownership and resource rules, applied only where relevant to C++. The official [Rust book](https://doc.rust-lang.org/book/) and [Python task/cancellation documentation](https://docs.python.org/3/library/asyncio-task.html) inform their respective language boundaries. Consult [source notes](references/sources.md) for targeted sources and rule ownership. [License](LICENSE.md).
