# Portable format contract

Verified: 2026-11-05. The shared interchange format is Agent Skills. Requirements below are format rules unless explicitly labeled otherwise.

| Item | Status | Rule |
| --- | --- | --- |
| Skill directory | Required | Contains `SKILL.md`. |
| YAML frontmatter | Required | Delimited by `---` before the Markdown body. |
| `name` | Required | 1–64 characters, lowercase letters, digits, and single hyphens. No leading, trailing, or consecutive hyphens. Matches the directory name. This collection chooses ASCII for portability. |
| `description` | Required | 1–1,024 characters describing the capability and when to activate it. |
| Markdown body | Required for a useful skill | The specification leaves its structure open. Describe actions and decisions. |
| `license` | Optional | License identifier or reference to a supplied license. Preserve notices for reused material. |
| `compatibility` | Optional | At most 500 characters describing actual environment requirements. |
| `metadata` | Optional | Mapping of string keys to string values. Quote versions and dates. |
| `allowed-tools` | Optional, experimental | Space-separated tool expressions. Support varies by client. It does not override runtime authorization. |
| `references/` | Optional convention | Conditional instructions and domain details. |
| `scripts/` | Optional in the shared format | This collection deliberately does not bundle skill execution helpers. Explicitly requested separate automation uses Python/uv. |
| `assets/` | Optional convention | Templates and resources copied into the produced output. |
| `agents/openai.yaml` | Optional client extension | UI metadata and dependency declarations. Not required by the shared format. |
| Client-specific frontmatter | Optional client extension | Keep out of the portable core unless deliberately targeting that client. |

Minimal metadata example:

```yaml
---
name: report-builder
description: Produce monthly reports from supplied metrics. Use when assembling or updating a monthly performance report.
---
```

Progressive disclosure keeps discovery metadata small, loads the entrypoint on activation, and reads only relevant resources afterward. The specification recommends a body below 5,000 tokens and an entrypoint under 500 lines. This collection enforces fewer than 500 lines for the complete SKILL.md file, including frontmatter, through its repository checker. The token budget remains a recommendation, not a separate mandatory metadata field.

Avoid deep reference chains and duplicated rules. Markdown resource links are relative to the file containing the link. In SKILL.md, use `references/detail.md`. In that reference, use `sources.md` for its sibling or `../assets/template.md` for an asset. Keep every required target inside the same skill package. Use forward slashes and exact case. A directory need not contain every optional folder.

Do not invent mandatory fields such as `version`, `author`, `model`, `tools`, or `category`. Metadata does not enforce sandboxing, scheduling, installation, or publishing permissions.
