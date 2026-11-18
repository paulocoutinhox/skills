# Sources

Verified: 2026-11-05.

- [EditorConfig overview and examples](https://editorconfig.org/): standard properties and common syntax.
- [Formal specification](https://spec.editorconfig.org/): matching and precedence semantics.
- [Ruff formatting](https://docs.astral.sh/ruff/formatter/), [Prettier configuration](https://prettier.io/docs/configuration), and [gofmt](https://pkg.go.dev/cmd/gofmt): language-tool integration.

The bundled template is an owner-selected set of common defaults. Keep only the sections applicable to the actual repository, and verify required exceptions with its tools.

## Professional foundation and evidence scope

Reviewed: 2026-11-05. [EditorConfig Specification 0.17.2](https://spec.editorconfig.org/) defines actual precedence/properties. [Software Engineering at Google: Style Guides and Rules](https://abseil.io/resources/swe-book/html/ch08.html) supplies professional consistency context. [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259) distinguishes valid JSON whitespace from an owner-selected spaces convention.

## Line length and formatter ownership

Checked **2026-11-18**. [EditorConfig Specification 0.17.2](https://spec.editorconfig.org/) defines `indent_style`, `indent_size`, `tab_width`, `end_of_line`, `charset`, `spelling_language`, `trim_trailing_whitespace`, `insert_final_newline` and `root`, and does not define `max_line_length`. The [EditorConfig properties wiki](https://github.com/editorconfig/editorconfig/wiki/EditorConfig-Properties) lists `max_line_length` as supported by a limited set of editors, where it forces hard wrapping. [Prettier options](https://prettier.io/docs/options) state that `max_line_length` configures Prettier's print width unless overridden, with a default `printWidth` of 80.

## Command-line resolution

Checked **2026-11-18** against the [EditorConfig C core](https://github.com/editorconfig/editorconfig-core-c) source. Its usage text is `editorconfig [OPTIONS] FILEPATH1 [FILEPATH2 FILEPATH3 ...]`, `-` reads paths from standard input, and the library rejects a relative path with "Input file must be a full path name." It prints the effective `key=value` pairs, preceded by a `[path]` header when several paths are given. The [EditorConfig overview](https://editorconfig.org/) states that section names are case-sensitive filepath globs.

Stored content is maintained only when the user requests a revision. There is no automated source collector or refresh mechanism.
