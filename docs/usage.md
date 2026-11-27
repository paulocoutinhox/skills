# Usage

Start with the [ready-to-use task prompts](task-prompts.md) for new projects, features, fixes,
reviews, Markdown Kanban boards, books, social content, animated videos, testing, publishing, and
skill upkeep. Each prompt names this collection and the skills to read. It also lists the inputs,
expected results, and checks.

In Codex, call a skill with `$skill-name`. In Claude Code, use `/skill-name`. Compatible clients can
also pick skills on their own when a request matches their descriptions. The
[Codex guide](https://learn.chatgpt.com/docs/build-skills) and the
[Claude Code guide](https://code.claude.com/docs/en/skills) explain how each client calls skills.

```text
$code-developer Implement account deletion in this repository and validate affected consumers.
$markdown-kanban Create KANBAN.md from these requested tasks, with linked card details and the board under the title.
$book-creator Create an A4 workbook for print and digital delivery from this manuscript.
$social-post Prepare YouTube, Instagram, X, and LinkedIn copy for this product demo.
$remotion Create and render a 15-second product video from this script and these brand assets, with synchronized narration and captions.
$security-audit Review tenant isolation across the API, file downloads, exports, and background jobs.
$android-app-testing Test this app's forms, keyboard, navigation and restoration on an emulator, then prepare a justified physical-device matrix.
$apple-app-testing Test this app across its Apple platforms, covering forms, remote/Crown/keyboard input, simulator limits and the actual cloud-device coverage.
$cloud-batch Plan where this engine builds and tests on Linux, Windows, Apple and Android within US$120 a month, then run today's batch and prove the cleanup.
$app-store-connect Prepare this app for iOS, macOS, tvOS, and visionOS, including subscriptions and localized screenshots.
$google-play Build a signed release bundle and prepare an internal-track release with a fresh version code.
$revenuecat Configure monthly and annual packages, restoration, a localized paywall, and sandbox tests.
$playgama Package this game, prepare all covers, and verify sandbox publication eligibility.
```

Give the real repository, manuscript, transcript, or brief. The skills ask you about choices that
change the result. They load only the reference pages that match the chosen language, platform, or
output.

Naming `paulocoutinhox` alone does not load the collection. Install the skills you want, check their
paths, and pick them by name or use the file-reading steps in the
[task prompts](task-prompts.md). This matters most when another skill has the same name.

The knowledge is written in each `SKILL.md`: researched steps, real limits, examples, choices,
quality checks and sources with notes. Skills do not include scripts or other helpers to run,
generated API dumps, counters, converters or background updaters. The agent updates facts only when
the user asks for upkeep in this repository. App-publishing guides explain the supported API/CLI
operations and the exact steps a person must do in the store console. They do not claim that every
account or legal step has an API.
