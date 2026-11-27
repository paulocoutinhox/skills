# Sources, format ownership and evidence scope

External sources were verified on **2026-11-05**. The skill is an original operating
procedure for the owner's single-file board format. It does not reproduce an entire guide, book or
third-party implementation.

| Source | What was inspected and how it is used |
| --- | --- |
| Owner-provided Markdown Kanban prototype | README, the six-card and larger example boards, local skill instructions, manager source and workflow were inspected as design context. The single-file idea, six-column table, cell content, marker names, status and priority values and complexity range come from this prototype. Its scripts/workflow are not distributed here. No private machine path or attachment was copied. |
| [The Kanban Guide, May 2025](https://kanbanguides.org/the-kanban-guide/2025.5/) | Public workflow, WIP, service expectation and flow-measure sections were read. Supports separating a visual tracker from an actual operating practice. It does not require six columns, a 1–10 complexity scale or this file format. |
| [Kanban University official method guide](https://kanban.university/kanban-guide/) | Public explicit-policy and WIP/pull sections were read. Informs locally agreed capacity, pull criteria and visible working agreements. This is a distinct publication from the May 2025 guide. |
| [GitHub Flavored Markdown specification](https://github.github.com/gfm/#tables-extension-) | Table, inline-content, raw-HTML and escaping rules were inspected. The six-column board uses inline cells, not nested block content. GitHub adds sanitization beyond the syntax specification. |
| [GitHub tables](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables) | Actual table headers, delimiters and alignment. Does not promise a fixed column width, responsive layout or drag and drop. |
| [GitHub section links](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links) | Checked on 2026-11-25. GitHub makes a heading's link target by lowercasing it, turning spaces into hyphens, removing other punctuation and adding `-1`, `-2` to repeats. A GitHub render of this repository's `Git single-root snapshot` heading gave the id `user-content-git-single-root-snapshot`, so hyphens stay and `### KB-001` links as `#kb-001`. |
| [VS Code Markdown](https://code.visualstudio.com/docs/languages/markdown) and its [slugify source](https://github.com/microsoft/vscode/blob/main/extensions/markdown-language-features/src/slugify.ts) | Checked on 2026-11-25. The preview, outline, header completions and link checks use headings. The source copies GitHub's slug rules. Running its regex locally turned `KB-001` into `kb-001`, and a heading that also holds the title gets an id that changes with the title. |
| [VS Code issue 183343](https://github.com/microsoft/vscode/issues/183343) and [issue 215455](https://github.com/microsoft/vscode/issues/215455) | Checked on 2026-11-25. `<a name>` targets do not scroll in the VS Code preview, and the maintainer points to `id` instead. This is why card links target headings, not HTML anchors. |
| [Daniel S. Vacanti, Actionable Agile Metrics for Predictability](https://actionableagile.com/books/aamfp/) | The publisher description was inspected for author/title and further-reading scope on flow/predictability. The complete book was not read and is not quoted as proof of a particular rule. |
| [Agent Skills specification](https://agentskills.io/specification) | Portable frontmatter and supporting-resource structure. Skill installation is separate from editing a user's board. |

The owner's format opens with the fixed title `# Project Kanban` and the board, keeps every rule
after the card records and the archive as the last section, keeps the file out of version control
unless asked, accepts common terms without blocking, orders every column except DONE by priority and
ID and DONE by most recent completion, and moves done cards to the archive with a dated `Archived`
field more than 30 days after they finish. The empty template, explicit rough defaults,
one-cell-per-visible-card rule, manual ID reservation, conflict procedure, evidence labels and
same-file withdrawal records, and the mapping of common type, status and priority words, are this
skill's operating conventions. They are not certification requirements or universal Kanban rules.
Card links rely on heading link targets, which GitHub and the VS Code preview make the same way.
Renderers that do not make ids from headings, or make them differently, cannot follow those links,
and that was not tested beyond GitHub's renderer and VS Code's slug code.

The supplied worked board is fictional and contains no actual execution evidence. A renderer/parser
check cannot certify task completion, team agreement, historical metrics or freedom from concurrent
edits. Actual GitHub/editor appearance and jump behavior require their target preview. No external
tracker, production account, paid service or automated source-maintenance process is needed.

Only the user requests revisions to stored guidance. Native Git/editor tools can inspect real work,
but this skill includes no executable helper or synchronization service. See [license](../LICENSE.md).
