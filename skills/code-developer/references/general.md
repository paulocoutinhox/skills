# General engineering contract

These are the collection owner's development preferences. They apply to all languages unless syntax or tools make a rule impossible. Clear code comes before clever code, simple code before needless complexity, and easy maintenance before short code.

## Readable flow

- Make each important operation visible on its own in a debugger. Store useful intermediate results in clearly named variables.
- Avoid long method chains, nested anonymous functions, implicit conversions, hidden side effects in getters or hooks, reflection, macros, and metaprogramming without a concrete need.
- Keep the validation, computation, state change, I/O, and return steps visually distinct. Separate groups of responsibility with blank lines. Never crowd several conditions, loops, changes, and returns together.
- Prefer clear control flow and familiar techniques. Avoid deep nesting and a needless `else` after an early return. A real exhaustive `else` is allowed. Unknown input must produce a named error, not an invented fallback.
- Keep functions focused. Extract code when responsibilities or repeated processes call for it. Do not break up simple code just to shorten functions or to add artificial abstraction layers.
- Order files from public entrypoints to related support behavior, while following language conventions. Keep dependencies visible and let the reader move forward step by step.
- Use complete, consistent domain names. Avoid vague names such as `data`, `temp`, `obj`, and `manager` when a concrete term exists.

## One call per line

Keep each function call, including its complete argument list, on one source line. Keep each function signature and each string literal on one line as well. Do not leave arguments on continuation lines lined up under the opening parenthesis. Do not split one message into adjacent literals or concatenations to fit a width. When a call becomes hard to read, store its argument expressions in named intermediate variables and pass those names.

A formatter's line-width setting usually produces wrapped calls. Examples are clang-format `ColumnLimit`, Prettier `printWidth`, Ruff `line-length`, rustfmt `max_width`, swift-format `lineLength` or ktlint `max_line_length`. Fix the configuration instead of accepting the output or turning off formatting around single calls:

1. Find the formatter that really rewrites the file. Include editor format-on-save and its fallback style when the repository has no configuration file.
2. Configure the repository file so ordinary calls are not wrapped. Use the exact setting from the language profile. Commit that configuration so every editor and CI run share it.
3. Join calls that an earlier configuration already wrapped. Some formatters keep existing breaks.
4. Run the formatter twice and confirm that the second run produces no diff.

Structural nesting is not a wrapped call. A trailing lambda or block body, a multi-line collection or object literal, a JSX/template element tree, a Compose content block and a fluent chain with named intermediate steps keep their normal block layout. The call that opens them still starts with its arguments on one line.

## Structure and reuse

Give each class, enum, component, screen, view, or page its own file. A second supporting class or
enum does not belong beside the main one. The filename names its symbol under the language's
conventions. Related implementation blocks can stay with their own type, and required language or
tool constructs keep a valid structure. Use hyphens where filenames can safely use them. Python
importable modules require underscores, Kotlin and Swift type files usually use the type's case, and
generated or tool-required names keep their exact spelling.

Share a useful repeated process through a helper class for one context, such as `CustomerHelper`. Keep its job narrow. Real reuse or a large, focused block of support behavior justifies a helper. Wanting another file does not. Do not create a generic utilities bucket. Do not turn normal framework hooks, composables, or required module functions into awkward classes only to follow a naming preference.

Start with concrete code. Add interfaces, generic parameters, traits, or extension points only when a real dependency boundary or proven variation needs them. Do not repeat business rules, validation, normalization, or state changes in several consumers.

## Final contract

Build the requested new behavior and move affected consumers to it at the same time. Remove outdated aliases, old-format detection, catch-all defaults, dual API support, and dead code. Do not add compatibility with earlier versions unless the user asks for it. Required input validation and clear error handling are part of the final contract, not legacy compatibility.

Changing a code contract does not allow you to drop production data, delete user work, rewrite Git history, or publish a package. Plan needed migrations and point out decisions that cannot be undone. Use a supported current API for the chosen runtime, not an API from an incompatible future version.

## Comments and language

Code, identifiers, comments, and technical documentation are in English. Do not split prose with semicolons. Programming-language semicolons stay where syntax or the formatter needs them.

Comments are rare and explain context or intent. Each sentence starts with a capital letter and ends with a period. Reword a sentence instead of starting it with a required lowercase identifier. Keep each sentence on one source line. A comment above a callable describes its purpose for callers, not its inner workings. Avoid obvious, decorative, story-like, and repeated comments. Do not add section markers such as “helpers” or “public methods.” A short comment about a block's intent fits only where that intent is truly hard to guess. Keep required formatter and tool directives exactly as they are.

## Integration and verification

Follow changed behavior through direct callers, external contracts, serialization, caches, background jobs, UI states, permissions, and deployment configuration. Check empty, invalid, edge, cancellation, retry, and concurrency behavior where relevant. Test real behavior that users can see and the important rules. Avoid tests that only repeat implementation details.

Do not swallow exceptions, turn all failures into empty data, retry operations that are not idempotent without care, or quietly return success after a partial failure. Use typed or contextual errors, limited resource use, predictable cleanup, and fitting cancellation. Make logs useful without exposing credentials or personal data.
