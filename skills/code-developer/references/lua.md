# Lua

## Runtime and project structure

Identify the actual interpreter, version, host application, available libraries, dependency manager, and deployment model before implementing. Standard Lua, LuaJIT, and Luau have different capabilities. The current official manual baseline is Lua 5.5, but an embedded host can require another runtime. Follow that selected target without inventing cross-version compatibility branches.

Use focused modules with local implementation details and explicit exports. Keep dependencies visible. Avoid accidental globals and import-time work that unexpectedly changes application state. Follow the host's module layout and lookup paths rather than mutating `package.path` as a generic workaround. File names can use hyphens only when the loader and repository conventions support them. Lua identifiers and host-required module names retain their valid spelling.

Lua does not require a class system. Keep one object-like module per file when using that design. Use a cohesive helper module for actual shared support logic rather than introducing a metatable hierarchy solely to imitate classes from another language.

## Values and control flow

Use `local` for internal state. Distinguish `nil` from a legitimate `false` value. Zero and the empty string are truthy, so do not translate another language's truth tests mechanically. Avoid an `and`/`or` expression as a substitute for a branch when a valid result can be false.

Separate sequences from maps. The length operator is not a reliable sparse-table item count. `ipairs` stops at the first absent sequential entry, and `pairs` does not establish a stable presentation order. Choose explicit keys, ordering, and counts for the data contract. Document intentional table mutation and sharing.

Handle multiple return values deliberately, including values containing `nil`. Do not silently collapse a status/result tuple. Standard string lengths describe bytes, not user-perceived Unicode characters. Choose appropriate Unicode handling when the task requires it. Keep metatable behavior limited and understandable rather than hiding I/O, mutation, or expensive work in ordinary property access.

## Errors, resources, and host boundaries

Use a consistent error contract and inspect protected-call status when using `pcall` or `xpcall`. Do not swallow failures or replace them with an invented success value. Define which failures belong to the module and which the host handles.

Close owned files and release host resources deliberately. Garbage collection is not a deterministic resource-management policy. Use the selected runtime's supported cleanup mechanisms. Coroutines need explicit ownership, resume/error handling, and cancellation or shutdown according to the host. A coroutine is not automatically a parallel worker.

Treat dynamic chunks, native modules, OS commands, and exposed host APIs as execution boundaries. Do not evaluate untrusted text as code or assume a restricted environment table alone creates a secure sandbox. Bound external work and preserve application authorization checks.

## Tooling and verification

Use the repository's dependency and test tools. Pin a compatible StyLua and Luacheck version when selecting them. Configure the exact syntax and permitted host globals. Do not use a union of unrelated runtime globals to conceal an unsupported API. The reviewed tool documentation does not establish full Lua 5.5 syntax support, so verify that support before selecting a tool for 5.5 code. Report unsupported syntax explicitly rather than lowering the target or silently skipping files.

For projects with compatible tools and a conventional source directory:

```bash
stylua --check src
luacheck src
```

These are formatting and static checks. Run the actual unit/integration suite under the intended interpreter and, for embedded applications, the real host test harness. Verify module loading, unexpected globals, false/nil cases, sequence gaps, propagated errors, and resource cleanup when affected. Do not claim that a standalone interpreter test proves host integration.

## Applied case: a valid false value and a callback owner

A settings table can deliberately contain `soundEnabled = false`. An `and/or` default expression can replace that valid false value accidentally. Distinguish absence (`nil`) from a supplied false value and apply the selected input contract explicitly. Do not substitute an invented default for required unknown input.

An array-like table with a missing position is not a dependable countable sequence. If order/count matters, define a dense sequence or explicit ordered keys and size. Preserve meaningful multiple-return values with nil positions using the selected runtime's actual facilities.

For a host timer or callback, track its handle and owner. A closure can retain a table/resource after a screen or game state ends. Cancel/unregister it through the host API and prevent an obsolete callback from mutating replacement state. Garbage collection does not define the native timer's lifecycle.

Test false versus nil, sparse input, propagated errors, repeated module loading and owner shutdown in the real host. Roberto Ierusalimschy's [Programming in Lua](https://www.lua.org/pil/) is professional further reading. Its edition/runtime must be identified, and historical examples do not override the [selected current reference manual](https://www.lua.org/manual/).
