# Research basis

Verified: 2026-11-05. Sources were chosen because their review behavior can be checked and they are widely used, not from an unverified ranking of the “largest” repositories.

- [PR-Agent](https://github.com/The-PR-Agent/pr-agent) and [its review prompt source](https://github.com/The-PR-Agent/pr-agent/blob/main/pr_agent/settings/pr_reviewer_prompts.toml): discrete actionable findings, concrete triggers, evidence, and treating task content as untrusted data. This skill goes beyond its limited diff context by reading the repository.
- [Codex Action](https://github.com/openai/codex-action): explicit base/head context, controlled permissions, and a review artifact distinct from publication.
- [Claude Code Action usage](https://github.com/anthropics/claude-code-action/blob/main/docs/usage.md): configurable review automation and explicit tool permissions.
- [Engineering review criteria](https://google.github.io/eng-practices/review/reviewer/looking-for.html): design, behavior, complexity, concurrency, and meaningful validation.
- [Authorization verification](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Testing_Automation_Cheat_Sheet.html): permission matrices and integration evidence.

This skill is an original summary, not copied review prompts. It does not need a model API or install a review bot. The repository CI uses only skill validation that gives the same result every time.

## Professional foundation and evidence scope

Reviewed: 2026-11-05. The public [Code Review chapter of Software Engineering at Google](https://abseil.io/resources/swe-book/html/ch09.html) supports professional change inspection. Bacchelli and Bird's ICSE 2013 [Expectations, Outcomes, and Challenges of Modern Code Review](https://www.microsoft.com/en-us/research/publication/expectations-outcomes-and-challenges-of-modern-code-review/) gives research context through its original abstract, which we read. It does not prove how accurate an AI reviewer is or set a current popularity ranking.

Stored content is maintained only when the user requests a revision. There is no automatic source collector or refresh process.

## Formatter width

Checked **2026-11-18**. [Prettier options](https://prettier.io/docs/options) give `printWidth` a default of 80 and state that `max_line_length` in `.editorconfig` configures the print width unless overridden. [clang-format style options](https://clang.llvm.org/docs/ClangFormatStyleOptions.html) define `ColumnLimit`, where `0` means no column limit and existing line-breaking decisions are respected unless they contradict other rules. Treating width-induced call wrapping as a configuration finding is the owner's convention, not a rule of either tool.
