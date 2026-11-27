# Lua

## Runtime and project structure

Find the real interpreter, version, host application, available libraries, dependency manager, and deployment model before you write code. Standard Lua, LuaJIT, and Luau have different capabilities. The current official manual is for Lua 5.5, but an embedded host can require another runtime. Follow that chosen target without inventing branches for other versions.

Use focused modules with local implementation details and clear exports. Keep dependencies visible. Avoid accidental globals and import-time work that changes application state without warning. Follow the host's module layout and lookup paths instead of changing `package.path` as a generic workaround. File names can use hyphens only when the loader and repository conventions support them. Lua identifiers and module names the host requires keep their valid spelling.

Lua does not require a class system. Keep one object-like module per file when using that design. Use a focused helper module for real shared support logic. Do not add a metatable hierarchy only to copy classes from another language.

## Values and control flow

Use `local` for internal state. Tell `nil` apart from a valid `false` value. Zero and the empty string are truthy, so do not copy another language's truth tests without thinking. Do not use an `and`/`or` expression in place of a branch when a valid result can be false.

Keep sequences and maps apart. The length operator is not a reliable item count for a sparse table. `ipairs` stops at the first missing entry in the sequence, and `pairs` does not give a stable display order. Choose clear keys, ordering, and counts for the data contract. Document table changes and sharing that you intend.

Handle multiple return values on purpose, including values that hold `nil`. Do not quietly collapse a status/result tuple. Standard string lengths count bytes, not the Unicode characters a user sees. Choose fitting Unicode handling when the task needs it. Keep metatable behavior limited and easy to understand. Do not hide I/O, changes, or costly work in ordinary property access.

## Errors, resources, and host boundaries

Use a consistent error contract and check the protected-call status when you use `pcall` or `xpcall`. Do not swallow failures or replace them with an invented success value. Define which failures belong to the module and which the host handles.

Close the files you own and release host resources on purpose. Garbage collection is not a predictable way to manage resources. Use the chosen runtime's supported cleanup methods. Coroutines need a clear owner, resume and error handling, and cancellation or shutdown that fits the host. A coroutine is not a parallel worker by default.

Treat dynamic chunks, native modules, OS commands, and exposed host APIs as execution boundaries. Do not run untrusted text as code. Do not assume that a restricted environment table alone makes a secure sandbox. Limit external work and keep the application's authorization checks.

## Tooling and verification

Use the repository's dependency and test tools. Pin a compatible StyLua and Luacheck version when you choose them. Configure the exact syntax and allowed host globals. Do not merge globals from unrelated runtimes to hide an unsupported API. The tool documentation we reviewed does not show full Lua 5.5 syntax support, so check that support before you choose a tool for 5.5 code. Report unsupported syntax clearly instead of lowering the target or quietly skipping files.

For projects with compatible tools and a conventional source directory:

```bash
stylua --check src
luacheck src
```

StyLua wraps calls that exceed `column_width`, whose default is 120. Under the owner's single-line call convention, set `column_width = 320` in `stylua.toml` so ordinary calls stay on one line.

These are formatting and static checks. Run the real unit and integration suite under the intended interpreter. For embedded applications, also run the real host test harness. Check module loading, unexpected globals, false/nil cases, sequence gaps, passed-on errors, and resource cleanup when the change affects them. Do not claim that a standalone interpreter test proves host integration.

## Applied case: a valid false value and a callback owner

A settings table can hold `soundEnabled = false` on purpose. An `and/or` default expression can replace that valid false value by accident. Tell absence (`nil`) apart from a given false value and apply the chosen input contract clearly. Do not put an invented default in place of required input that is unknown.

An array-like table with a missing position is not a sequence you can count reliably. If order or count matters, define a dense sequence or clear ordered keys and a size. Keep useful multiple return values that have nil positions by using the chosen runtime's real features.

For a host timer or callback, track its handle and owner. A closure can keep a table or resource alive after a screen or game state ends. Cancel or unregister it through the host API, and stop an outdated callback from changing the state that replaced it. Garbage collection does not define the native timer's lifecycle.

Test false versus nil, sparse input, passed-on errors, repeated module loading and owner shutdown in the real host. Roberto Ierusalimschy's [Programming in Lua](https://www.lua.org/pil/) is good further reading. Name its edition and runtime, and do not let older examples override the [selected current reference manual](https://www.lua.org/manual/).
