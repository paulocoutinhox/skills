# Other languages

The general contract applies to any language. A profile must be researched for a language not already covered before making consequential language-specific choices.

1. Inspect the language version, compiler or interpreter, framework, manifest, lockfile, build commands, formatter, linter, tests, and existing architecture.
2. Read the current official style, memory and concurrency guidance for that target. Resolve framework requirements before applying generic file or architecture conventions.
3. Establish naming exceptions to hyphens, ownership and cleanup, error handling, nullability, async cancellation, package structure, and verification commands.
4. Implement using the selected supported version and a single final contract. Do not introduce legacy support as a default.
5. When maintaining this collection, add a focused language reference and link it from `SKILL.md`. When simply using the skill in another project, record applicable decisions in that project's `AGENTS.md` without modifying an installed skill unexpectedly.

Examples of primary starting points include official language documentation for Go, Java, C#, PHP, Ruby, Dart, and the chosen database or shell. Rust, Lua, and Markdown have dedicated profiles linked from the entrypoint. Do not present a borrowed rule from another language as authoritative. Tests, build scripts, framework hooks, extension functions, and language entrypoints can require module-level functions or specific filenames.
