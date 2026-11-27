# Properties, precedence, and language choices

Use `root = true` for the intended top-level configuration. Standard properties include `charset`, `end_of_line`, `indent_style`, `indent_size`, `tab_width`, `insert_final_newline`, and `trim_trailing_whitespace`. Specification 0.17.2 also defines `spelling_language`. A value of `unset` removes an inherited property where supported. Do not assume every editor supports a proprietary formatter setting.

Files are matched using case-sensitive forward-slash globs. Brace expansion can group extensions. A closer `.editorconfig` overrides matching parent properties, and later matching sections override earlier values. Check the effective result instead of assuming an extension section is the only matching rule.

| Language or file | Common starting point | Qualification |
| --- | --- | --- |
| Python | 4 spaces. | Match Ruff's chosen configuration. |
| JavaScript, TypeScript, JSON, Vue | 2 spaces. | Keep the existing formatter. JSON allows tab whitespace outside strings, but the project can choose spaces. Comments require a different format such as JSONC. |
| HTML, CSS, SCSS, Less, SVG | 2 spaces. | EditorConfig does not validate markup or CSS structure. |
| YAML | 2 spaces. | Tabs are not a substitute for YAML indentation. |
| TOML, INI | 4 spaces as the general preset. | Follow the project formatter. Many simple key/value lines have no indentation. |
| Swift, Kotlin, Java, C#, C/C++, Rust, Dart, PHP | 4 spaces. | This is a common convention, not a universal requirement. |
| Ruby | 2 spaces. | Keep framework conventions. |
| Shell | 2 spaces. | Match the chosen shfmt configuration. |
| Go | Tabs for indentation. | gofmt remains the source of truth. |
| Make | Tabs for recipes. | Some makefiles set another recipe prefix on purpose. Check before you change it. |
| Markdown | 2 spaces, keep trailing spaces. | Two trailing spaces can create a hard break on purpose. |
| Windows batch | CRLF when the toolchain requires it. | Do not apply CRLF to every file just because contributors use Windows. |
| Binary assets | Avoid text transformations. | EditorConfig should not rewrite binary data. |
| Golden files and fixtures | Match the exact bytes that matter. | Add narrow exceptions only where they are really needed. |

Keep a specific exception after broad extension sections. For example, a generated test fixture that leaves out final newlines on purpose needs an exception for its path, not a setting turned off everywhere. Configure generated files at the generator when possible.

Do not add a universal `max_line_length` and assume it makes every editor wrap code. It is outside the specification's defined keys, only some editors follow it by hard wrapping, and Prettier uses it as `printWidth` unless overridden. The source formatter controls line breaking through its own configuration. When that configuration is `.editorconfig` itself, as for ktlint, set `max_line_length = 320` in a section scoped to the formatter's files, such as `[*.{kt,kts}]`. Keep single calls on one line instead of choosing a narrow width that wraps their arguments. The language's exact required filenames and tabs take priority over a generic preference for hyphens and spaces.
