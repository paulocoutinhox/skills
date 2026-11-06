# Properties, precedence, and language choices

Use `root = true` for the intended top-level configuration. Standard properties include `charset`, `end_of_line`, `indent_style`, `indent_size`, `tab_width`, `insert_final_newline`, and `trim_trailing_whitespace`. A value of `unset` removes a previously inherited property where supported. Do not assume every editor supports a proprietary formatter setting.

Files are matched using case-sensitive forward-slash globs. Brace expansion can group extensions. A closer `.editorconfig` overrides matching parent properties, and later matching sections override earlier values. Inspect the effective result rather than assuming an extension section is the only matching rule.

| Language or file | Common starting point | Qualification |
| --- | --- | --- |
| Python | 4 spaces. | Align with Ruff's selected configuration. |
| JavaScript, TypeScript, JSON, Vue | 2 spaces. | Preserve the established formatter. JSON allows tab whitespace outside strings, but the project can choose spaces. Comments require a different format such as JSONC. |
| HTML, CSS, SCSS, Less, SVG | 2 spaces. | EditorConfig does not validate markup or CSS structure. |
| YAML | 2 spaces. | Tabs are not a substitute for YAML indentation. |
| TOML, INI | 4 spaces as the general preset. | Follow the project formatter. Many simple key/value lines have no indentation. |
| Swift, Kotlin, Java, C#, C/C++, Rust, Dart, PHP | 4 spaces. | This is a common convention, not a universal requirement. |
| Ruby | 2 spaces. | Keep framework conventions. |
| Shell | 2 spaces. | Align with the chosen shfmt configuration. |
| Go | Tabs for indentation. | gofmt remains the source of truth. |
| Make | Tabs for recipes. | Some makefiles explicitly set another recipe prefix. Inspect before changing it. |
| Markdown | 2 spaces, preserve trailing spaces. | Two trailing spaces can intentionally create a hard break. |
| Windows batch | CRLF when required by the toolchain. | Do not apply CRLF to every file merely because contributors use Windows. |
| Binary assets | Avoid text transformations. | EditorConfig should not rewrite binary data. |
| Golden files and fixtures | Match their meaningful exact bytes. | Add narrowly scoped exceptions only where actually needed. |

Keep a specific exception after broad extension sections. For example, a generated test fixture containing intentionally missing final newlines needs a path-specific exception, not a global disablement. Configure generated files at the generator when possible.

Do not add a universal `max_line_length` and assume it makes every editor wrap code. Property support varies, and a source formatter should control line breaking. The language's exact required filenames and tabs take priority over a generic preference for hyphens and spaces.
