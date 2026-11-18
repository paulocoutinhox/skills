# General engineering contract

These are the collection owner's development preferences. They apply across languages unless syntax or tooling makes a rule impossible. Clarity takes priority over cleverness, simplicity over unnecessary complexity, and maintainability over brevity.

## Readable flow

- Make each important operation independently observable in a debugger. Store meaningful intermediate results in clearly named variables.
- Avoid excessive method chains, nested anonymous functions, implicit conversions, hidden effects in getters or hooks, reflection, macros, and metaprogramming without a concrete need.
- Keep validation, computation, state mutation, I/O, and return stages visually distinguishable. Separate responsibility groups with blank lines. Never crowd multiple conditions, loops, mutations, and returns together.
- Prefer explicit control flow and familiar techniques. Avoid deep nesting and unnecessary `else` after an early return. A legitimate exhaustive `else` is allowed. Unknown input must produce a named error rather than an invented fallback.
- Keep functions focused. Extract when responsibilities or repeated processes warrant it. Do not fragment straightforward code merely to shorten functions or introduce artificial abstraction layers.
- Organize files from public entrypoints to related support behavior, while respecting language conventions. Keep dependencies visible and reading progressive.
- Use complete, consistent domain names. Avoid ambiguous `data`, `temp`, `obj`, and `manager` names when a concrete term exists.

## One call per line

Keep each function call, including its complete argument list, on one source line. Keep each function signature and each string literal on one line as well. Do not leave arguments on continuation lines aligned under the opening parenthesis, and do not split one message into adjacent literals or concatenations to fit a width. When a call becomes hard to read, store its argument expressions in named intermediate variables and pass those names.

Wrapped calls are normally produced by a formatter's line-width setting, such as clang-format `ColumnLimit`, Prettier `printWidth`, Ruff `line-length`, rustfmt `max_width`, swift-format `lineLength` or ktlint `max_line_length`. Fix the configuration rather than accepting the output or disabling formatting around individual calls:

1. Identify the formatter that actually rewrites the file, including editor format-on-save and its fallback style when the repository has no configuration file.
2. Configure the repository file so ordinary calls are not wrapped. Use the language profile's exact setting. Commit that configuration so every editor and CI run share it.
3. Join calls that an earlier configuration already wrapped. Some formatters preserve existing breaks.
4. Run the formatter twice and confirm the second run produces no diff.

Structural nesting is not a wrapped call. A trailing lambda or block body, a multi-line collection or object literal, a JSX/template element tree, a Compose content block and a fluent chain with named intermediate steps keep their normal block layout. The call that opens them still starts with its arguments on one line.

## Structure and reuse

Give each class, enum, component, screen, view, or page its own file. A second supporting class/enum
does not belong beside the primary one. The filename identifies its symbol under the language's
conventions. Related implementation blocks can stay with their own type, and mandatory language/tool
constructs retain a valid structure. Use hyphens where filenames can safely use them. Python importable
modules require underscores, Kotlin and Swift type files generally use the type's case, and
generated/tool-required names keep their exact spelling.

Share a meaningful repeated process through a context-specific helper class such as `CustomerHelper`. Keep its responsibility narrow. A helper is justified by actual reuse or substantial cohesive support behavior, not by the desire to create another file. Do not create a generic utilities bucket. Do not turn idiomatic framework hooks, composables, or required module functions into awkward classes solely to satisfy a naming preference.

Start with concrete implementations. Introduce interfaces, generic parameters, traits, or extensibility points only when an actual dependency boundary or demonstrated variation needs them. Do not duplicate business rules, validation, normalization, or state transformations in multiple consumers.

## Final contract

Implement the requested new behavior and migrate affected consumers together. Remove obsolete aliases, old-format detection, permissive catch-all defaults, dual API support, and dead code. Do not add compatibility with previous versions unless explicitly requested. Required input validation and explicit error handling are part of the final contract, not legacy compatibility.

Changing a code contract does not authorize dropping production data, deleting user work, rewriting Git history, or publishing a package. Plan necessary migrations and surface irreversible decisions. Use a supported current API for the selected runtime rather than an API from an incompatible future version.

## Comments and language

Code, identifiers, comments, and technical documentation are in English. Do not split prose with semicolons. Programming-language semicolons remain where syntax or the formatter requires them.

Comments are rare and explain context or intent. Each sentence starts with a capital letter and ends with a period. Rephrase rather than begin with a mandatory lowercase identifier. Keep each sentence on one source line. A comment above a callable describes its caller-facing purpose rather than its internal implementation. Avoid obvious, decorative, narrative, and redundant comments. Do not add section markers such as “helpers” or “public methods.” A short block-intent comment is appropriate only where the intent is genuinely difficult to infer. Preserve exact required formatter and tooling directives.

## Integration and verification

Trace changed behavior through direct callers, external contracts, serialization, caches, background jobs, UI states, permissions, and deployment configuration. Check empty, invalid, boundary, cancellation, retry, and concurrency behavior where relevant. Test actual user-observable behavior and important invariants. Avoid tests that merely repeat implementation details.

Do not swallow exceptions, turn all failures into empty data, retry non-idempotent operations indiscriminately, or silently return success after partial failure. Use typed or contextual errors, bounded resource usage, deterministic cleanup, and appropriate cancellation. Make logs useful without exposing credentials or personal data.
