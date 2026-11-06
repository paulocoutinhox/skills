# Sources, format ownership and evidence scope

Verified: **2026-11-05**. The skill is an original operating procedure for the owner's single-file
board format. It does not reproduce an entire guide, book or third-party implementation.

| Source | What was inspected and how it is used |
| --- | --- |
| Owner-provided Markdown Kanban prototype | README, the six-card and larger example boards, local skill instructions, manager source and workflow were inspected as design context. The single-file layout, marker names, status/type/priority values, complexity range and display ordering come from this prototype. Its scripts/workflow are not distributed here. No private machine path or attachment was copied. |
| [The Kanban Guide, May 2025](https://kanbanguides.org/the-kanban-guide/2025.5/) | Public workflow, WIP, service expectation and flow-measure sections were read. Supports separating a visual tracker from an actual operating practice. It does not require six columns, a 1–10 complexity scale or this file format. |
| [Kanban University official method guide](https://kanban.university/kanban-guide/) | Public explicit-policy and WIP/pull sections were read. Informs locally agreed capacity, pull criteria and visible working agreements. This is a distinct publication from the May 2025 guide. |
| [GitHub Flavored Markdown specification](https://github.github.com/gfm/#tables-extension-) | Table, inline-content, raw-HTML and escaping rules were inspected. A six-column overview uses inline cells, not nested block content. GitHub adds sanitization beyond the syntax specification. |
| [GitHub tables](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables) | Actual table headers, delimiters and alignment. Does not promise a fixed column width, responsive layout or drag and drop. |
| [GitHub basic formatting and custom anchors](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#custom-anchors) | Stable named anchors, relative links and line breaks. New-board examples use the documented name attribute. Existing working ID anchors are preserved when maintaining the owner's format. |
| [Daniel S. Vacanti, Actionable Agile Metrics for Predictability](https://actionableagile.com/books/aamfp/) | The publisher description was inspected for author/title and further-reading scope on flow/predictability. The complete book was not read and is not quoted as proof of a particular rule. |
| [Agent Skills specification](https://agentskills.io/specification) | Portable frontmatter and supporting-resource structure. Skill installation is separate from editing a user's board. |

The empty template, explicit provisional defaults, one-cell-per-visible-card invariant, manual ID
reservation, conflict procedure, evidence labels and optional same-file archiving are this skill's
operating conventions. They are not certification requirements or universal Kanban rules. Named
anchors follow GitHub documentation rather than promising that every Markdown renderer honors them.

The supplied worked board is fictional and contains no actual execution evidence. A renderer/parser
check cannot certify task completion, team agreement, historical metrics or freedom from concurrent
edits. Actual GitHub/editor appearance and jump behavior require their target preview. No external
tracker, production account, paid service or automated source-maintenance process is needed.

Only the user requests revisions to stored guidance. Native Git/editor tools can inspect real work,
but this skill includes no executable helper or synchronization service. See [license](../LICENSE.md).
