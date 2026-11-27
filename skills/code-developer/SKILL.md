---
name: code-developer
description: Implement and refactor production code with clear contracts, readable responsibilities, current architecture guidance and language-specific engineering. Use for real source changes in Python, Swift, Kotlin, C++, Rust, Lua, Markdown, JavaScript, TypeScript, Vue, React, and Angular.
license: MIT
---

# Code Developer

Build the requested final behavior in the real source files. Good quality means the next maintainer can understand the contract, follow how the code runs, find failures and change the system safely. Short code, pattern counts and many files are not measures of quality.

## Establish the contract and impact

Read the repository instructions, manifests, architecture, related source, direct callers and existing tests. Find the chosen language and runtime, the supported platform, the public API and the user's real acceptance criteria. Follow an existing architecture when it is consistent. New Swift and Android projects without an architecture use the owner's MVVM default with separate models, views and view models.

Before editing, state the important rule in concrete terms. Examples include “a paid transaction grants this benefit at most once” or “only the active search request can replace the visible results.” Find which component owns that rule and where its source-of-truth state lives.

Follow the change through inputs, validation, domain operations, storage, background work and output. Include consumers that do not change. Removing source-level compatibility does not allow you to corrupt saved records or ignore binaries that still run during deployment. Choose a clear migration or coordinated rollout when the final contract needs one.

## Write readable responsibilities

Use meaningful names and clear intermediate values. Keep the validation, calculation, change, I/O and return steps visually apart with blank lines. Keep each function call with its whole argument list, each signature and each string literal on one line. Name long argument expressions first instead of wrapping arguments under the opening parenthesis. When a formatter wraps calls, fix its width setting as described in the [general contract](references/general.md#one-call-per-line) and the language profile, then join the calls it already wrapped. Prefer early returns when they make the path easier to follow. Do not use a needless `else` after `return`, but keep a real exhaustive branch when the domain needs it.

Keep each function focused on one job. Extract a responsibility when it has meaning on its own or is truly shared. Do not break a simple flow into many one-line helpers. Do not add interfaces, factories and generic layers for imagined future changes. A helper for one context, such as `CustomerHelper`, fits only when its job is clear and has a real reason.

Give each class, enum, component, screen or view its own file with a fitting name. A supporting
class or enum also gets its own file. It does not become a second type beside a main class. Follow
valid language and tool filenames and required constructs. Hyphens are the default where legal, but
Python and Rust modules and names a framework requires keep their usual spelling. Avoid repeated
business rules and generic utility buckets.

Comments are rare, in English, and explain needed intent or context. Use complete sentences that start with a capital letter and end with a period. Reword a sentence instead of starting it with a required lowercase identifier. Do not split prose with semicolons or add decorative section comments. Required language punctuation, licenses, type-system safety notes and tool directives keep their real syntax.

## Errors, state and concurrency

Check untrusted inputs at the real boundary. Model expected failures clearly and keep useful context. Do not return empty collections, success values or a different product just because an operation failed. Avoid generic fallback behavior, swallowed exceptions and old-format detection when the requested final contract does not need them.

Keep absence, loading, invalid input, failure and a successful empty result apart. A network timeout does not prove that a payment or upload was never accepted. Check the result by a durable operation ID before you retry an action that is not idempotent (safe to repeat).

Name an owner for tasks, streams, listeners, file handles, locks and native resources. Define cancellation and cleanup. Async/await, actors and memory-safe languages do not make a multi-step business operation atomic. Use the real database constraint, transaction, lock or idempotency record that protects the rule.

For requests that replace UI content, canceling may not be enough if a response already finished. Tie results to the currently selected request or state generation, and ignore an outdated result on purpose. For shared file output, checking that a file exists before writing does not stop another writer from creating it. Use the supported atomic or no-overwrite operation and test the real race when it matters.

## Worked change: canceling an export

A request to cancel an export affects more than the button. Check the UI command, job creation, worker, temporary output, download route and completion notice. Define when cancellation takes effect and what happens to a result that was already committed.

Keep the worker's state change as the source of truth. Do not let a late completion turn a canceled job back into success. Clean up only the temporary data that this job owns. Keep the user's source files. Make sure an outdated notice cannot reveal a download that belongs to another account. Update affected callers and statuses together. Do not keep the old state model as a silent compatibility branch.

Useful checks cover cancellation before work, during work, after completion, and a race between completion and cancellation. They also check an unrelated user's request and that source files stay intact. A test that only repeats the same assignment as the code adds little confidence.

## Language-specific engineering

Read the profile for every changed language and the framework layer you actually use:

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

The [general contract](references/general.md) gives the owner's detailed preferences. Empty Python `__init__.py` files, no `TYPE_CHECKING`, MVVM defaults, class-owned C++ functions, formatter-off directives around lambdas and single-line calls with a wide or unlimited formatter width are owner conventions. They are not universal language rules. Do not write invalid framework code just to copy another language.

## Verification and delivery

Use the project's formatter, linter, type checker, compiler and focused behavior tests. After formatting, check the diff for calls broken across continuation lines. Such a break means the formatter width still needs fixing. A transpiler is not always a type checker. A successful build does not prove memory safety, security or correct concurrency. Use release-mode, device, sanitizer or installed-consumer checks when the changed behavior makes them relevant.

Create or update the root `AGENTS.md` with the current purpose, capabilities, layout, architecture, commands and boundaries. Use [the project template](assets/agents-template.md). Remove outdated guidance and unused code within scope. Do not add task history.

Report the final behavior, affected consumers, checks you ran, existing or unresolved failures and important limits. Keep dependencies current and compatible with the chosen target, without needless whole-project upgrades.

This skill holds descriptive engineering guidance. Do not create automation just to show activity. Scripts the user asks for use Python with uv and documented dependencies. Real applications use the languages and native tools they require.

## Professional foundations

[Software Engineering at Google](https://abseil.io/resources/swe-book/html/toc.html), edited by Titus Winters, Tom Manshreck and Hyrum Wright, supports reasoning about maintainable change and verification. The [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) give concrete ownership and resource rules, used only where they apply to C++. The official [Rust book](https://doc.rust-lang.org/book/) and [Python task/cancellation documentation](https://docs.python.org/3/library/asyncio-task.html) inform the boundaries of their languages. See the [source notes](references/sources.md) for targeted sources and who owns each rule. [License](LICENSE.md).
