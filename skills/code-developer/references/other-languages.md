# Other languages

The general contract applies to any language. For a language that has no profile yet, research a profile before you make important language-specific choices.

1. Check the language version, compiler or interpreter, framework, manifest, lockfile, build commands, formatter, linter, tests, and existing architecture.
2. Read the current official style, memory and concurrency guidance for that target. Settle framework requirements before you apply generic file or architecture conventions.
3. Decide naming exceptions to hyphens, ownership and cleanup, error handling, nullability, async cancellation, package structure, and verification commands.
4. Build with the chosen supported version and one final contract. Do not add legacy support by default.
5. When maintaining this collection, add a focused language reference and link it from `SKILL.md`. When you only use the skill in another project, record the decisions that apply in that project's `AGENTS.md`. Do not change an installed skill without warning.

Good starting points include official language documentation for Go, Java, C#, PHP, Ruby, Dart, and the chosen database or shell. Rust, Lua, and Markdown have dedicated profiles linked from the entrypoint. Do not present a rule borrowed from another language as the source of truth. Tests, build scripts, framework hooks, extension functions, and language entrypoints can require module-level functions or specific filenames.
