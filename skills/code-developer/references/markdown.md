# Markdown

## Dialect and document purpose

Identify the audience, publishing surface, renderer, and dialect before editing. CommonMark is the portable baseline. GitHub Flavored Markdown adds features such as tables and task lists. MDX, documentation-site directives, frontmatter, mathematical notation, and diagrams require their actual renderer and configuration. Do not assume every extension works on every surface.

Keep one document focused on a coherent reader task. Use descriptive hyphenated filenames unless a tool requires an exact name such as `README.md`, `AGENTS.md`, or `SKILL.md`. Preserve existing document URLs and heading anchors when possible. If a heading or path must change, update the affected links, navigation, and generated contents together.

## Structure and readability

Use a clear heading hierarchy and normally one document title. Prefer ATX headings and do not use bold paragraphs as a substitute for semantic headings. Separate headings, paragraphs, lists, tables, and code blocks with blank lines for readable source and predictable rendering. These spacing and title choices are project conventions, not a claim that every blank line is required by the Markdown grammar.

Use lists for genuinely parallel or sequential information. Align nested content with its parent item's content indentation and inspect the rendered result. Use a table only when comparisons are easier to read that way. Keep cells concise and use another structure for content that needs complex nesting or long code blocks.

Use descriptive link text, exact path case, and document-relative links for bundled resources. Resolve a link from its containing file, rather than assuming the repository or skill root is its base. Verify destination files and renderer-specific heading anchors. Do not wrap a clickable link in backticks. Use reference-style links when they materially improve source readability. Supply meaningful alternative text for informative images and an appropriate empty alternative for decorative images where the renderer supports it.

Preserve meaningful whitespace. Two trailing spaces can intentionally create a hard break. Do not strip them indiscriminately or add them to every line. Prefer ordinary paragraphs over manual line breaks unless the content needs them. Keep UTF-8, consistent line endings, and a final newline according to the repository configuration.

## Code, HTML, and extensions

Use fenced code blocks with an appropriate language identifier for code and `text` for plain-text examples. Choose a fence longer than any matching fence sequence inside the example. Close every fence and preserve the language's required indentation. Use the relevant language profile for code examples as well as this Markdown profile.

Keep commands copyable and internally consistent. Identify placeholders and replace them before labeling an example ready to execute. Do not put live secrets or private endpoints into examples. Explain consequential prerequisites and effects near the command. Syntax highlighting does not validate code or make a shell command safe.

Use raw HTML only when the publishing surface supports the required behavior. GitHub applies sanitization beyond the GFM grammar. Scripts, styling, arbitrary attributes, and embedded content cannot be assumed to survive. Preserve intentional repository branding, including centered logo markup, while checking its actual output.

Edit YAML frontmatter as structured metadata using the target tool's schema. Do not introduce new fields merely because another documentation system uses them. Keep renderer-specific components or executable documentation outside a portable document unless the project deliberately uses that system. Rendering untrusted HTML or executable MDX needs an appropriate security boundary.

## Verification

Run the existing Markdown linter and formatter with the project's configuration when available. Markdownlint rules encode configurable style decisions, not a universal language specification. Use narrow justified exceptions for requirements such as repository logos rather than disabling an entire rule set.

Check local files, anchors, images, reference definitions, navigation, tables, nested lists, code fences, and frontmatter. Build documentation with the actual site generator or preview the actual publishing surface when available. Validate changed executable examples with their relevant tools when the change warrants it. Inspect rendered readability and accessibility. A regex link check cannot prove complete Markdown correctness or renderer compatibility.

## Applied case: a valid source file with a broken reader path

A renamed guide can leave reference-style links and navigation entries pointing to its old path even when inline-link regex checks pass. Resolve links through the selected Markdown parser and inspect the actual rendering surface. Code-fenced examples should not be mistaken for live document links.

Relative paths inside a skill must continue to resolve after copying that package alone. A link to the collection's root README can work in the source checkout but break portability. Keep required guidance inside the package, with external citations explicitly identified as sources.

Check meaningful image alternative text, table reading order, nested lists, executable examples and frontmatter schema. For heading changes, inspect actual renderer anchors and duplicates instead of assuming a generic slug formula proves GitHub compatibility. [CommonMark](https://spec.commonmark.org/) defines portable syntax. [GFM](https://github.github.com/gfm/) and GitHub sanitization add separate behavior. A parser/link check is not a full visual/accessibility proof.
