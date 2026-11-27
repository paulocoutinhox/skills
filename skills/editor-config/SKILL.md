---
name: editor-config
description: Create and review .editorconfig using the repository's real languages, whitespace rules, which formatter owns each setting, and property precedence. Use for editing conventions or finding the cause of inconsistent formatting across editors.
license: MIT
---

# Editor Config

Create a configuration that helps editors keep the repository's files in their intended text form. The goal is a saved file you can predict, not a list of every property or a forced rewrite of the repository.

## Inspect ownership before choosing values

Find the real file types, nested `.editorconfig` files, formatter configuration, generated paths, fixtures and contributor tools. Work out which tool owns each decision. EditorConfig can supply indentation and newline preferences, but Ruff, gofmt, rustfmt, a framework formatter or a file format can set stronger rules.

For example, a four-space default must not convert Make recipe tabs to spaces. A Markdown cleanup must not erase meaningful hard breaks. A generated binary must not be treated as UTF-8 text. An exception for one tool should be narrow enough to keep the general convention everywhere else.

## Precedence and matching

A core (the library that reads EditorConfig files) searches the relevant configuration files toward the root until it reaches the declared boundary. Closer configuration and later matching sections can override inherited properties. Check the effective result for a real path instead of reading one extension block on its own.

Globs are case-sensitive and use forward slashes. A pattern's slash and directory scope matter. Brace expansion can group relevant extensions. Use `unset` to remove an inherited property where the implementation supports it. Put a specific exception after broad rules.

Use portable properties: `charset`, `end_of_line`, `indent_style`, `indent_size`, `tab_width`, `insert_final_newline` and `trim_trailing_whitespace`. Specification 0.17.2 also defines `spelling_language`, which few editors apply. Do not invent an EditorConfig property for a formatter setting.

Line breaking belongs to the source formatter, not to EditorConfig. `max_line_length` is not one of the specification's defined keys. The EditorConfig project lists it as a property that only some editors support, where it forces hard wrapping, and Prettier reads it as its print width unless the Prettier configuration overrides it. Do not add it to control code layout for formatters that have their own configuration. A narrow value such as 80 can make Prettier wrap a single call's arguments across lines. Configure the width in the formatter's own configuration, keep each call on one line and use named intermediate variables for complex arguments. When a formatter such as ktlint reads `max_line_length` from `.editorconfig`, that file is the formatter's own configuration. Set it there in a section scoped to that formatter's files, such as `[*.{kt,kts}]`, with the owner's wide value of 320 so ordinary calls stay on one line. If an existing file already sets `max_line_length`, check which formatter reads it before you keep or remove it.

## Build a minimal coherent profile

| Target | Starting convention | Decision to verify |
| --- | --- | --- |
| Ordinary source text | UTF-8, LF, final newline | Existing tooling and fixtures whose exact bytes matter |
| Python | Four spaces | Ruff/project settings |
| JSON/YAML/frontend markup | Usually two spaces | Existing formatter and valid syntax |
| Go | Tabs | gofmt controls the real formatting |
| Make recipes | Hard tabs | Check for a declared alternative recipe prefix |
| Markdown | Keep trailing spaces | Hard breaks and real rendering |
| Swift/Kotlin/C++/Rust | Existing project convention | Native formatter configuration, including ktlint's `max_line_length` here |
| Windows command files | CRLF when required | Do not impose it on unrelated source |
| Generated/golden files | Narrow path exception | Generator output and bytes that matter |

Start with [the template](assets/editorconfig), keep the relevant sections, and remove unrelated language blocks. A mixed repository can need many sections, but a small Python package should not get a long list of unused settings without a reason.

## Worked resolution example

Suppose `[*]` sets four spaces and trimming, `[*.md]` disables trimming, and `[docs/generated/*.md]` disables final-newline insertion because an external producer owns those bytes. A Markdown file elsewhere still gets ordinary final-newline behavior. The generated exception must not turn off trimming everywhere or change all documentation.

If the formatter keeps producing two-space JSON while the editor inserts four, find the formatter's real configuration and match the editor property to it. Do not switch back and forth between reformatting tools, or add an exception that hides the disagreement.

For fixtures where whitespace matters, explain which bytes are tested. A “no final newline” fixture is on purpose only when a real behavior depends on it. Avoid special cases made up only to justify more configuration.

## Verification and delivery

Resolve typical real paths through an EditorConfig implementation. An EditorConfig core command-line tool, invoked as `editorconfig <absolute-file-path>`, prints the effective properties for that path. Include overrides that should apply, overlapping matches, nested configuration and important cases that should not match. Stop and report when no core or plugin is available instead of claiming the resolution was checked. Open and save a typical file with the intended editor when possible, and run the real formatter. Parsing the configuration alone does not prove plugin support.

Check the resulting diff for mass reformatting nobody asked for. Changing configuration does not by itself allow you to change every source file. Deliver the file, the reasons for important exceptions, how it matches the formatter and the checks you really ran.

This skill is descriptive and does not create format-enforcement scripts or background updaters. Existing native formatter commands can be used directly when the user asked for validation.

## Foundations

The [EditorConfig specification](https://spec.editorconfig.org/) defines matching and properties. Its distinction between cores, plugins and editors explains why a valid file may still have no effect in an unsupported editor. [Software Engineering at Google: Style Guides and Rules](https://abseil.io/resources/swe-book/html/ch08.html) gives professional context for consistency and conventions that tools enforce. It does not make one indentation width correct everywhere.

See [detailed property guidance](references/rules.md), [source notes](references/sources.md) and [the license](LICENSE.md).
