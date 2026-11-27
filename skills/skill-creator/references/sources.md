# Sources

Verified: 2026-11-05. Check again before you change cross-client or installation instructions.

- [Agent Skills specification](https://agentskills.io/specification): portable metadata, optional directories, disclosure, and validation. Rechecked on 2026-11-18 for field limits, the 500-line and 5,000-token recommendations, and its skill-root wording for file references, which the format contract matches up with file-relative Markdown links.
- [Reference validator](https://github.com/agentskills/agentskills/tree/main/skills-ref): real CLI behavior. Repository tooling pins revision `83021e2be457a9b6679148719c1f6074f0ad975e`.
- [Codex skill authoring and locations](https://learn.chatgpt.com/docs/build-skills): discovery, installation directories, invocation, and optional metadata. Rechecked on 2026-11-18.
- [Claude Code skills](https://code.claude.com/docs/en/skills): personal and project scope, slash invocation, and client extensions.

The shared format does not imply identical UI, permission handling, supported tools, or metadata extensions in every client.

## Professional foundation and evidence scope

Reviewed: 2026-11-05. The descriptive authoring procedure also uses [Anthropic's Agent Skills article](https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills) for procedural knowledge and progressive disclosure. The collection's rules against executable content and for maintenance started only by the user are owner requirements, not universal Agent Skills format rules.

Stored content is maintained only when the user requests a revision. There is no automatic source collector or refresh process.

## Execution-based maintenance scope

Reviewed **2026-11-05** using the collection's descriptive-content/portability contract and
[Anthropic's authoring guidance](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices),
especially short progressive disclosure, conditional workflows and evaluation and iteration. The
maintenance procedure sorts real problems before adding instructions and checks the exact interface.
This collection keeps evaluations descriptive unless separate automation is requested. It does not
claim that a manual scenario review proves universal model reliability or replaces independent model
evaluation, native execution or remote CI.
