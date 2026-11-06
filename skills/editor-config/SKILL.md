---
name: editor-config
description: Create and review .editorconfig using the repository's actual languages, whitespace semantics, formatter ownership, and property precedence. Use for editing conventions or diagnosing inconsistent formatting across editors.
license: MIT
---

# Editor Config

Create a configuration that helps editors preserve the repository's intended text representation. The goal is a predictable saved file, not a collection of every property or a forced rewrite of the repository.

## Inspect ownership before choosing values

Identify actual file types, nested `.editorconfig` files, formatter configuration, generated paths, fixtures and contributor tools. Determine which tool owns each decision. EditorConfig can supply indentation/newline preferences, but Ruff, gofmt, rustfmt, a framework formatter or a file format can impose stronger rules.

For example, a four-space default must not convert Make recipe tabs to spaces. A Markdown cleanup must not erase meaningful hard breaks. A generated binary must not be treated as UTF-8 text. A tool-specific exception should be narrow enough to preserve the general convention elsewhere.

## Precedence and matching

A core searches relevant configuration files toward the root until the declared boundary. More local configuration and later matching sections can override inherited properties. Inspect the effective result for an actual path rather than reading a single extension block in isolation.

Globs are case-sensitive and use forward slashes. A pattern's slash and directory scope matter. Brace expansion can group relevant extensions. Use `unset` to remove a previously inherited property where the implementation supports it. Put a specific exception after broad rules.

Use portable properties: `charset`, `end_of_line`, `indent_style`, `indent_size`, `tab_width`, `insert_final_newline` and `trim_trailing_whitespace`. Do not invent an EditorConfig property for a formatter setting. Do not assume a proprietary `max_line_length` changes every editor's wrapping behavior.

## Build a minimal coherent profile

| Target | Starting convention | Decision to verify |
| --- | --- | --- |
| Ordinary source text | UTF-8, LF, final newline | Existing tooling and meaningful exact-byte fixtures |
| Python | Four spaces | Ruff/project settings |
| JSON/YAML/frontend markup | Usually two spaces | Existing formatter and valid syntax |
| Go | Tabs | gofmt controls actual formatting |
| Make recipes | Hard tabs | Inspect a declared alternative recipe prefix |
| Markdown | Preserve trailing spaces | Hard breaks and actual rendering |
| Swift/Kotlin/C++/Rust | Existing project convention | Native formatter configuration |
| Windows command files | CRLF when required | Do not impose it on unrelated source |
| Generated/golden files | Narrow path exception | Generator output and significant byte behavior |

Start with [the template](assets/editorconfig), keep relevant sections, and remove unrelated language blocks. A mixed repository can need many sections, but a small Python package should not inherit a catalog of unused settings without reason.

## Worked resolution example

Suppose `[*]` sets four spaces and trimming, `[*.md]` disables trimming, and `[docs/generated/*.md]` disables final-newline insertion because an external producer owns those bytes. A Markdown file elsewhere still receives ordinary final-newline behavior. The generated exception must not disable trimming globally or alter all documentation.

If the formatter keeps producing two-space JSON while the editor inserts four, identify the formatter's actual configuration and align the editor property. Do not alternate between reformatting tools or add an exception that hides the disagreement.

For significant whitespace fixtures, explain which bytes are tested. A “no final newline” fixture is intentional only when a real behavior depends on it. Avoid special cases invented solely to justify more configuration.

## Verification and delivery

Resolve representative real paths through an EditorConfig implementation. Include positive overrides, overlapping matches, nested configuration and important negative cases. Open/save a representative file with the intended editor when possible and run the actual formatter. Configuration parsing alone does not prove plugin support.

Inspect the resulting diff for unrequested mass reformatting. Changing configuration does not automatically authorize changing every source file. Deliver the file, rationale for consequential exceptions, formatter alignment and checks actually run.

This skill is descriptive and does not create format-enforcement scripts or background updaters. Existing native formatter commands can be used directly when the user requested validation.

## Foundations

The [EditorConfig specification](https://spec.editorconfig.org/) defines matching and properties. Its distinction between cores, plugins and editors explains why a valid file may still have no effect in an unsupported editor. [Software Engineering at Google: Style Guides and Rules](https://abseil.io/resources/swe-book/html/ch08.html) provides professional context for consistency and tool-supported conventions. It does not make one indentation width universally correct.

See [detailed property guidance](references/rules.md), [source notes](references/sources.md) and [the license](LICENSE.md).
