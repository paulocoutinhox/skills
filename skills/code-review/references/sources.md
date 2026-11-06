# Research basis

Verified: 2026-11-05. Sources were selected for inspectable review behavior and adoption, not an unverified ranking of the “largest” repositories.

- [PR-Agent](https://github.com/The-PR-Agent/pr-agent) and [its review prompt source](https://github.com/The-PR-Agent/pr-agent/blob/main/pr_agent/settings/pr_reviewer_prompts.toml): discrete actionable findings, concrete triggers, evidence, and treating task content as untrusted data. Its limited-diff context is deliberately expanded here through repository inspection.
- [Codex Action](https://github.com/openai/codex-action): explicit base/head context, controlled permissions, and a review artifact distinct from publication.
- [Claude Code Action usage](https://github.com/anthropics/claude-code-action/blob/main/docs/usage.md): configurable review automation and explicit tool permissions.
- [Engineering review criteria](https://google.github.io/eng-practices/review/reviewer/looking-for.html): design, behavior, complexity, concurrency, and meaningful validation.
- [Authorization verification](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Testing_Automation_Cheat_Sheet.html): permission matrices and integration evidence.

This skill is an original synthesis, not copied review prompts. It does not require a model API or install a review bot. The repository CI uses deterministic skill validation only.

## Professional foundation and evidence scope

Reviewed for this revision: 2026-11-05. The public [Code Review chapter of Software Engineering at Google](https://abseil.io/resources/swe-book/html/ch09.html) supports professional change inspection. Bacchelli and Bird's ICSE 2013 [Expectations, Outcomes, and Challenges of Modern Code Review](https://www.microsoft.com/en-us/research/publication/expectations-outcomes-and-challenges-of-modern-code-review/) supplies empirical context through its inspected primary research abstract. It does not validate the accuracy of an AI reviewer or establish a current popularity ranking.

Stored content is maintained only when the user requests a revision. There is no automated source collector or refresh mechanism.
