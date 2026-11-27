# Markdown

## Dialect and document purpose

Find the audience, publishing surface, renderer, and dialect before you edit. CommonMark is the portable base. GitHub Flavored Markdown adds features such as tables and task lists. MDX, documentation-site directives, frontmatter, math notation, and diagrams need their real renderer and configuration. Do not assume every extension works on every surface.

Keep each document focused on one reader task. Use descriptive hyphenated filenames unless a tool requires an exact name such as `README.md`, `AGENTS.md`, or `SKILL.md`. Keep existing document URLs and heading anchors when you can. If a heading or path must change, update the affected links, navigation, and generated contents together.

## Structure and readability

Use a clear heading hierarchy and normally one document title. Prefer ATX headings, and do not use bold paragraphs in place of real headings. Separate headings, paragraphs, lists, tables, and code blocks with blank lines for readable source and predictable rendering. These spacing and title choices are project conventions. They do not claim that the Markdown grammar requires every blank line.

Use lists for information that is truly parallel or in sequence. Line up nested content with the content indent of its parent item, and check the rendered result. Use a table only when comparisons are easier to read that way. Keep cells short, and use another structure for content that needs complex nesting or long code blocks.

Use descriptive link text, exact path case, and document-relative links for bundled resources. Resolve a link from the file that holds it. Do not assume the repository or skill root is its base. Check destination files and renderer-specific heading anchors. Do not wrap a clickable link in backticks. Use reference-style links when they clearly make the source easier to read. Give useful alternative text for images that carry information, and an empty alternative for decorative images where the renderer supports it.

Keep whitespace that has meaning. Two trailing spaces can create a hard break on purpose. Do not strip them everywhere or add them to every line. Prefer ordinary paragraphs over manual line breaks unless the content needs them. Keep UTF-8, consistent line endings, and a final newline according to the repository configuration.

## Code, HTML, and extensions

Use fenced code blocks with a fitting language identifier for code and `text` for plain-text examples. Choose a fence longer than any matching fence inside the example. Close every fence and keep the language's required indentation. Use the relevant language profile for code examples as well as this Markdown profile.

Keep commands easy to copy and consistent with each other. Mark placeholders, and replace them before you call an example ready to run. Do not put live secrets or private endpoints into examples. Explain important prerequisites and effects near the command. Syntax highlighting does not validate code or make a shell command safe.

Use raw HTML only when the publishing surface supports the required behavior. GitHub applies sanitization beyond the GFM grammar. Do not assume that scripts, styling, arbitrary attributes, and embedded content survive. Keep intended repository branding, including centered logo markup, and check its real output.

Edit YAML frontmatter as structured metadata using the target tool's schema. Do not add new fields just because another documentation system uses them. Keep renderer-specific components or executable documentation out of a portable document unless the project chose that system on purpose. Rendering untrusted HTML or executable MDX needs a fitting security boundary.

## Verification

Run the existing Markdown linter and formatter with the project's configuration when available. Markdownlint rules hold configurable style choices, not a universal language specification. Use narrow exceptions with a clear reason for needs such as repository logos, instead of turning off a whole rule set.

Check local files, anchors, images, reference definitions, navigation, tables, nested lists, code fences, and frontmatter. Build documentation with the real site generator, or preview the real publishing surface when you can. Check changed runnable examples with their tools when the change calls for it. Check that the rendered page is readable and accessible. A regex link check cannot prove complete Markdown correctness or renderer compatibility.

## Applied case: a valid source file with a broken reader path

A renamed guide can leave reference-style links and navigation entries pointing to its old path even when inline-link regex checks pass. Resolve links through the chosen Markdown parser and check the real rendering surface. Do not mistake examples inside code fences for live document links.

Relative paths inside a skill must still resolve after you copy that package alone. A link to the collection's root README can work in the source checkout but break portability. Keep required guidance inside the package, and mark external citations clearly as sources.

Check image alternative text, table reading order, nested lists, runnable examples and frontmatter schema. For heading changes, check the real renderer anchors and duplicates. Do not assume a generic slug formula proves it works on GitHub. [CommonMark](https://spec.commonmark.org/) defines portable syntax. [GFM](https://github.github.com/gfm/) and GitHub sanitization add separate behavior. A parser or link check is not full proof of visual quality or accessibility.
