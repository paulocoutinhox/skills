<p align="center">
  <a href="https://github.com/paulocoutinhox/skills">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="extras/images/logo-dark.svg">
      <img width="560" src="extras/images/logo.svg" alt="Paulo Skills">
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://github.com/paulocoutinhox/skills/actions/workflows/validate.yml"><img src="https://github.com/paulocoutinhox/skills/actions/workflows/validate.yml/badge.svg" alt="Validate"></a>
  <a href="LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://agentskills.io/specification"><img src="https://img.shields.io/badge/Agent%20Skills-compatible-14b8a6" alt="Agent Skills compatible"></a>
</p>

<p align="center">
Researched, reusable workflows for planning work, building software, creating publications, and preparing social content.
</p>

<br>

## 🚀 Project

Paulo Skills is a collection of **independent skills in English** using the shared
[Agent Skills format](https://agentskills.io/specification). Each skill combines a focused `SKILL.md`
with focused reading references and document templates where useful. Copy one skill or install the collection
into Codex, Claude Code, or another compatible client.

The instructions distinguish official requirements, selected working defaults, and recommendations.
Platform limits and print specifications include verification notes and must be checked for the exact
job before publication. These skills prepare and validate work. External publication follows the
user's authorization.

Created by [Paulo Coutinho](https://paulox.dev/), a software developer with **more than 20 years of
experience** building software. The collection emphasizes clear architecture, focused responsibilities,
readable code, and practical verification.

## ✨ Skills

| Skill | What it does | Instructions |
| --- | --- | --- |
| `skill-creator` | Research, author, update, and validate portable skills. | [SKILL.md](skills/skill-creator/SKILL.md) |
| `markdown-kanban` | Maintain a single KANBAN.md with six columns, linked cards, priorities, blockers and completion evidence. | [SKILL.md](skills/markdown-kanban/SKILL.md) |
| `book-creator` | Typeset books and A4 workbooks, prepare white-page interiors and complete cover packages. | [SKILL.md](skills/book-creator/SKILL.md) |
| `code-developer` | Implement clear production code and documentation, including Rust, Lua, and Markdown profiles. | [SKILL.md](skills/code-developer/SKILL.md) |
| `vue-app` | Build modular Vue apps with components, composables, clear state, and production checks. | [SKILL.md](skills/vue-app/SKILL.md) |
| `react-app` | Build modular React apps with components/hooks, clear state, and async lifecycle checks. | [SKILL.md](skills/react-app/SKILL.md) |
| `tailwind-css` | Design maintainable Tailwind interfaces with tokens, variants, accessibility, and CSS checks. | [SKILL.md](skills/tailwind-css/SKILL.md) |
| `queuefy` | Integrate Python queues and schedules with durable stores, retries, leases, and idempotency. | [SKILL.md](skills/queuefy/SKILL.md) |
| `cachefy` | Integrate Python caching with scoped spaces, memoization, freshness, and invalidation. | [SKILL.md](skills/cachefy/SKILL.md) |
| `kaktos-site` | Create local static Kaktos sites with Jinja, integrated assets, frozen routes, and native commands. | [SKILL.md](skills/kaktos-site/SKILL.md) |
| `fastkit-app` | Extend Fastkit site/admin/API through its resource, tenant, service, and command contracts. | [SKILL.md](skills/fastkit-app/SKILL.md) |
| `xplpc-mobile` | Connect native apps to a shared C++ core with XPLPC mappings, ownership, and platform builds. | [SKILL.md](skills/xplpc-mobile/SKILL.md) |
| `haylen-app` | Build Haylen apps with screen navigation, games with focused systems, native plugins, and template-based project upgrades. | [SKILL.md](skills/haylen-app/SKILL.md) |
| `reliable-information` | Answer factual questions with inspected evidence, precise citations, and explicit uncertainty. | [SKILL.md](skills/reliable-information/SKILL.md) |
| `web-app-testing` | Test locally with Playwright and use current AWS, Azure, or Google cloud execution surfaces. | [SKILL.md](skills/web-app-testing/SKILL.md) |
| `git` | Prepare branches and one reviewed commit with task-aware naming. | [SKILL.md](skills/git/SKILL.md) |
| `npm-library` | Build and test npm libraries with automatic OIDC publication. | [SKILL.md](skills/npm-library/SKILL.md) |
| `pypi-library` | Build and test Python distributions with automatic trusted publication. | [SKILL.md](skills/pypi-library/SKILL.md) |
| `social-post` | Fill publishing fields for YouTube, Shorts, TikTok, Instagram, X, and LinkedIn. | [SKILL.md](skills/social-post/SKILL.md) |
| `social-thumbnail` | Generate readable thumbnail artwork and checked export derivatives. | [SKILL.md](skills/social-thumbnail/SKILL.md) |
| `editor-config` | Configure editing conventions for the repository's actual file types. | [SKILL.md](skills/editor-config/SKILL.md) |
| `git-ignore` | Exclude private and generated files while preserving source and lockfiles. | [SKILL.md](skills/git-ignore/SKILL.md) |
| `code-review` | Review changes and trace their impact across the system. | [SKILL.md](skills/code-review/SKILL.md) |
| `android-app-testing` | Test Android forms, screens and lifecycle from Windows, macOS or Linux with emulators, physical devices and cloud labs. | [SKILL.md](skills/android-app-testing/SKILL.md) |
| `apple-app-testing` | Test iOS/iPadOS, tvOS, macOS, visionOS and watchOS apps from macOS with platform-specific input, simulators, hardware and cloud coverage. | [SKILL.md](skills/apple-app-testing/SKILL.md) |
| `security-audit` | Assess web, API, mobile, desktop, authorization, and delivery risks. | [SKILL.md](skills/security-audit/SKILL.md) |
| `app-store-connect` | Build Apple apps and administer store fields, ASO, media, prices, products, review and release. | [SKILL.md](skills/app-store-connect/SKILL.md) |
| `google-play` | Build Android bundles and administer listings, ASO, media, prices, billing, review and rollout. | [SKILL.md](skills/google-play/SKILL.md) |
| `revenuecat` | Create projects and store apps, connect credentials, configure products and paywalls, and verify SDK/purchase lifecycles. | [SKILL.md](skills/revenuecat/SKILL.md) |
| `playgama` | Build HTML5 games, integrate Bridge, review numbered release requirements, and manage monetization, media and publication. | [SKILL.md](skills/playgama/SKILL.md) |

## 📦 Install

Clone the repository:

```bash
git clone https://github.com/paulocoutinhox/skills.git
cd skills
```

For an existing local checkout, point its remote to the canonical repository:

```bash
git remote set-url origin https://github.com/paulocoutinhox/skills.git
```

Install all skills for one client:

```bash
uv run --script scripts/install-skills.py codex
uv run --script scripts/install-skills.py claude
```

| Client | User installation | Project installation |
| --- | --- | --- |
| Codex | `~/.agents/skills/` | `.agents/skills/` |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |

Install one skill or choose a project destination:

```bash
uv run --script scripts/install-skills.py codex code-review
uv run --script scripts/install-skills.py claude book-creator --destination /path/to/project/.claude/skills
```

The installer copies complete skill directories and refuses existing destinations. Follow the update
procedure below when replacing an installed version.
For manual installation, copy the entire selected skill directory, including its references, assets
and license, into the client root above. Existing same-name system skills can affect selection, so
verify the actual loaded path. The installer rejects symlinks and existing destinations.

## 🔄 Update installed skills

Installed skills are independent copies. Updating this Git clone does not update those copies.
Run these steps whenever you choose to install a newer revision. There is no background updater.

1. This repository publishes `main` as a single-commit snapshot and replaces that history on each
   delivery. Before updating your local clone, preserve unfinished edits and any local-only commits
   in an independent backup outside the checkout. Confirm `git status --short` is empty and that
   every local change you want to keep is backed up before resetting. Run each command only after
   the preceding command succeeds:

   ```bash
   git fetch origin
   git switch main
   git reset --hard origin/main
   uv sync --locked
   uv run --locked python scripts/validate-skills.py
   ```

   The reset replaces tracked checkout files and discards local commits from main. Do not use it
   before preserving wanted local work. Alternatively, clone the repository into a fresh directory
   and leave your existing checkout intact. Review the downloaded snapshot and compare any edits
   made directly to your installed skill copies.

2. Move the installed skill into a backup directory outside the client's discovery roots, then
   install the replacement. For example, update `code-review` in Codex:

   ```bash
   backupdir=$(mktemp -d "$HOME/paulo-skills-backup.XXXXXX")
   mv "$HOME/.agents/skills/code-review" "$backupdir/code-review"
   uv run --script scripts/install-skills.py codex code-review
   ```

   For Claude Code, use its own installation root instead:

   ```bash
   backupdir=$(mktemp -d "$HOME/paulo-skills-backup.XXXXXX")
   mv "$HOME/.claude/skills/code-review" "$backupdir/code-review"
   uv run --script scripts/install-skills.py claude code-review
   ```

   Replace `code-review` with the skill you want to update. Continue to installation only after the
   backup move succeeds. Keep the backup until you have checked the replacement. If installation
   fails, move the saved package back to its original path before using it again.

3. Start a new client session and verify that it selects the updated skill from the intended path.
   Reapply any wanted local customizations after comparing them with the new version.

To update the whole collection, first move **only this collection's installed skill directories**
into a fresh backup outside discovery. Use the names in the catalog above and leave unrelated skills
in place. Then reinstall the collection for the chosen client:

```bash
uv run --script scripts/install-skills.py codex all
```

Use `claude all` for Claude Code. Every existing destination with a matching name must be moved first,
because the installer refuses overwrites. For a project installation, move the old copies from that
project's `.agents/skills/` or `.claude/skills/` and pass the same destination when reinstalling:

```bash
uv run --script scripts/install-skills.py codex all --destination /path/to/project/.agents/skills
```

## 💡 How to use

Start with the [ready-to-use task prompts](#-task-prompts) for new projects, features, fixes,
reviews, Markdown Kanban boards, books, social content, testing, publishing, and skill maintenance.
Each prompt names this collection, identifies the skills to read, and defines the inputs,
deliverables, and checks.

In Codex, mention a skill with `$skill-name`. In Claude Code, use `/skill-name`. Compatible clients can
also select skills when a request matches their descriptions. Client-specific invocation behavior is
documented in the [Codex guide](https://learn.chatgpt.com/docs/build-skills) and
[Claude Code guide](https://code.claude.com/docs/en/skills).

```text
$code-developer Implement account deletion in this repository and validate affected consumers.
$markdown-kanban Create KANBAN.md from these requested tasks, with six columns and complete linked card details in the same file.
$book-creator Create an A4 workbook for print and digital delivery from this manuscript.
$social-post Prepare YouTube, Instagram, X, and LinkedIn copy for this product demo.
$security-audit Review tenant isolation across the API, file downloads, exports, and background jobs.
$android-app-testing Test this app's forms, keyboard, navigation and restoration on an emulator, then prepare a justified physical-device matrix.
$apple-app-testing Test this app across its Apple platforms, covering forms, remote/Crown/keyboard input, simulator limits and the actual cloud-device coverage.
$app-store-connect Prepare this app for iOS, macOS, tvOS, and visionOS, including subscriptions and localized screenshots.
$google-play Build a signed release bundle and prepare an internal-track release with a fresh version code.
$revenuecat Configure monthly and annual packages, restoration, a localized paywall, and sandbox tests.
$playgama Package this game, prepare all covers, and verify sandbox publication eligibility.
```

Use `/code-developer`, `/book-creator`, or the corresponding slash name in Claude Code. Provide the
actual repository, manuscript, transcript, or brief. The skills ask for decisions that affect the result
and load only the references relevant to the chosen language, platform, or output.

Naming `paulocoutinhox` alone does not load the collection. Install the intended skills, verify their
paths, and use explicit selection or the file-reading instructions in the
[task prompts](#-task-prompts), especially when another skill shares a name.

The knowledge is written in each `SKILL.md`: researched procedures, actual limits, examples, decisions,
quality criteria and annotated sources. Skills do not bundle executable helpers, generated API dumps,
counters, converters or background refreshers. Facts are updated by the agent only when the user
requests maintenance in this repository. App-publishing guides explain supported API/CLI operations
and exact console handoffs without claiming that every account/legal step has an API.

## ✅ Validate locally and in CI

Use `make help` to list the contributor commands. `make setup` installs the locked environment, and
`make validate` (also `make valide`) runs skills-ref, repository integrity, contributor tests, Ruff
lint, and formatting checks. CI uses the same `make validate` target on pushes to `main`.

Install [uv](https://docs.astral.sh/uv/) and Python 3.11 or later, then run:

```bash
uv sync --locked
uv run --locked python scripts/validate-skills.py
```

The Python wrapper invokes the official **skills-ref** command for every skill locally and in CI,
with the same failure behavior:

```bash
skills-ref validate skills/code-review
```

The upstream revision and resolved tooling dependencies are pinned in `pyproject.toml` and `uv.lock`.
CI runs on pushes to `main` and manual dispatch. It also checks local links and resource packaging, Python lint
and formatting, descriptive-package rules, and contributor-tool behavior. It uses no model or model API
credentials. Format validation checks the skill structure and metadata. It does not certify domain
accuracy or model behavior. Installed validation works offline. Initial dependency installation needs
network access.

Run all repository checks with `make validate`. General authoring, research, architecture and
validation rules are in [AGENTS.md](AGENTS.md).

## 🧱 Organization

```text
skills/       Portable skill directories and their own resources
scripts/      Collection installer and validation commands
tests/        Contributor-tool behavior and packaging checks
extras/       Editable vector logo and project assets
.github/      Validation CI, issue templates, funding, and release notes template
AGENTS.md     Current authoring, architecture, and development contract
```

Resources are kept inside their skill so individual installation remains useful. A skill does not
need empty resource directories just to match a diagram. Runtime application code and a native
vendor command are distinct from bundled skill automation.

## 📝 Task prompts

Copy a prompt, replace the bracketed inputs and paste it into the agent handling your task.
Set `[SKILLS_ROOT]` to the absolute directory containing this collection's installed packages, or
its readable local `skills/` directory. Expand `~` explicitly. Reading a checkout does not install
or register a skill. Verify the actual loaded path when another package has the same name.

Each prompt identifies `paulocoutinhox/skills`, the files to read, expected deliverables and checks.
Naming the owner alone does not load the skills or override client permissions. General repository
rules are maintained in [AGENTS.md](AGENTS.md). The catalog links directly to each skill's procedure.

<details>
<summary>New project</summary>

```text
Use code-developer, editor-config, and git-ignore from paulocoutinhox/skills.
Before editing, read these files and their relevant references:
- [SKILLS_ROOT]/code-developer/SKILL.md
- [SKILLS_ROOT]/editor-config/SKILL.md
- [SKILLS_ROOT]/git-ignore/SKILL.md
Briefly identify the resolved skill paths. Report any missing skill without substituting another source.

Create a new [PROJECT_TYPE] project in [TARGET_DIRECTORY] using [LANGUAGE_AND_FRAMEWORK].
Product goal: [PROBLEM_AND_USERS]. Required capabilities: [FEATURES].
Target platforms and supported toolchain: [PLATFORMS_AND_VERSIONS].
Constraints and external integrations: [CONSTRAINTS].

Inspect the directory and existing project instructions first. Resolve only decisions that block
implementation. Use the relevant language profile and the skill's architecture defaults when no
architecture exists. Implement the working scope with clear responsibility boundaries and explicit
error handling. Create appropriate .editorconfig and .gitignore files and a current-state AGENTS.md.
Document setup, configuration, execution, architecture, and meaningful verification commands.
Run the checks relevant to the implemented behavior and report actual results and remaining setup.
Do not add unsolicited automation or compatibility layers. Do not publish or deploy this project.
```

</details>

<details>
<summary>Implement a feature</summary>

```text
Use code-developer from paulocoutinhox/skills.
Read [SKILLS_ROOT]/code-developer/SKILL.md and the applicable language/framework references first.
Briefly identify the resolved skill path. Report it if unavailable instead of claiming it was loaded.

Implement [FEATURE] directly in [REPOSITORY_OR_DIRECTORY].
Expected behavior and acceptance criteria: [OBSERVABLE_RESULTS_AND_EDGE_CASES].
Relevant entrypoints, integrations, and constraints: [CONTEXT].

Read the project's AGENTS.md and inspect the affected callers, state, persistence, and UI/API contracts.
Follow the existing architecture and selected toolchain. Make the final implementation clear and
complete, with explicit failures, readable control flow, and no generic fallback or legacy branches.
Keep code and necessary comments in English. Update affected documentation and current AGENTS.md
guidance when architecture or commands change. Verify affected consumers and meaningful failure paths.
Report changed behavior, validation evidence, and any unresolved dependency on external configuration.
```

</details>

<details>
<summary>Fix or refactor</summary>

```text
Use code-developer from paulocoutinhox/skills.
Read [SKILLS_ROOT]/code-developer/SKILL.md and the relevant language references before changing code.
Briefly identify the resolved skill path and report it if unavailable.

In [REPOSITORY], [FIX_OR_REFACTOR] the following behavior: [ISSUE].
Reproduction or current evidence: [STEPS_LOGS_OR_CODE_PATH].
Expected final behavior and scope: [ACCEPTANCE_CRITERIA].

Trace the cause and affected consumers before editing. Address real failures supported by evidence.
For a refactor, preserve the stated behavior unless the task explicitly changes it. Remove obsolete
branches and resources made unnecessary by this change. Avoid speculative rewrites and compatibility
layers. Validate the reproduction, relevant failure paths, and integrations affected by the change.
Update documentation and AGENTS.md when their current instructions change. Explain the cause, final
behavior, and actual verification results. Preserve unrelated work.
```

</details>

<details>
<summary>Documentation</summary>

```text
Use code-developer from paulocoutinhox/skills.
Read [SKILLS_ROOT]/code-developer/SKILL.md and its Markdown reference before editing.
Briefly identify the resolved skill path and report it if unavailable.

Create or improve [DOCUMENTS] in [REPOSITORY] for [AUDIENCE_AND_PURPOSE].
Required topics and real examples: [TOPICS].

Verify the documented behavior against the actual project. Explain prerequisites, inputs, commands,
expected outputs, errors, and relevant limits in a natural reading order. Use working relative links,
correct code fences, and accurate examples. Keep AGENTS.md instructional and limited to the current
architecture, conventions, and commands. Remove conflicting guidance from affected documents.
Check local links and appropriate examples. Report checks performed and examples that could not run.
```

</details>

<details>
<summary>Code review</summary>

```text
Use code-review from paulocoutinhox/skills.
Read [SKILLS_ROOT]/code-review/SKILL.md and its relevant references before reviewing.
Briefly identify the resolved skill path and report it if unavailable.

Review [DIFF_COMMIT_RANGE_OR_FILES] in [REPOSITORY].
Intended behavior: [TASK_AND_ACCEPTANCE_CRITERIA]. Relevant constraints: [CONTEXT].

Inspect the change and its callers, consumers, schemas, state transitions, and deployment assumptions.
Trace credible regressions across the project rather than reviewing changed lines in isolation.
Prioritize correctness, security, concurrency, data integrity, and missing verification of real risks.
For each finding, give severity, file/line, trigger, user impact, evidence, and a concrete correction.
Separate confirmed findings from questions and coverage gaps. Do not invent findings to fill a quota.
Report the checks actually run and residual uncertainty. This task is assessment only, without edits.
```

</details>

<details>
<summary>Security audit</summary>

```text
Use security-audit from paulocoutinhox/skills.
Read [SKILLS_ROOT]/security-audit/SKILL.md and the relevant platform references first.
Briefly identify the resolved skill path and report it if unavailable.

Audit [REPOSITORY_OR_SYSTEM] within [AUTHORIZED_TARGETS_AND_ENVIRONMENT].
Platforms, sensitive assets, user roles, and tenant boundaries: [CONTEXT].

Map entrypoints and trust boundaries, then investigate applicable authentication, authorization,
input/output handling, secrets, storage, dependencies, and release risks. Trace access to another
user's records, files, exports, jobs, and subscription state. An opaque URL identifier does not
replace object-level authorization. Use controlled local or otherwise authorized verification.
Provide evidenced findings with exploit prerequisites, impact, affected paths, remediation, and
regression checks. Identify untested boundaries. Do not expose secrets or run destructive probes.
Deliver an audit report. Implement fixes only if separately included in the authorized task.
```

</details>

<details>
<summary>Editor configuration</summary>

```text
Use editor-config from paulocoutinhox/skills.
Read [SKILLS_ROOT]/editor-config/SKILL.md and its applicable file-type rules first.
Briefly identify the resolved skill path and report it if unavailable.

Create or correct .editorconfig in [REPOSITORY].
Inspect the actual languages, generated files, formatters, and current conventions. Set appropriate
encoding, newlines, final newline, whitespace, and indentation rules, including meaningful file-type
exceptions. Preserve syntax-sensitive whitespace. Align the file with real formatter behavior and
document intentional choices. Verify representative files and explain any unresolved conflict.
Do not reformat unrelated files as part of this task.
```

</details>

<details>
<summary>Ignore rules</summary>

```text
Use git-ignore from paulocoutinhox/skills.
Read [SKILLS_ROOT]/git-ignore/SKILL.md and its relevant ecosystem guidance first.
Briefly identify the resolved skill path and report it if unavailable.

Create or correct .gitignore in [REPOSITORY].
Inspect the actual toolchains and distinguish source, lockfiles, required wrappers, generated output,
caches, environments, test artifacts, runtime data, system files, and private configuration.
Use precise rules that exclude the unwanted files while retaining required project assets and examples.
Check representative paths and inspect already tracked sensitive/generated files. Do not print secrets.
Report tracked material requiring separate remediation. Ignore rules alone do not remove tracked files.
Do not delete local files or rewrite history.
```

</details>

<details>
<summary>Git delivery</summary>

```text
Use git from paulocoutinhox/skills.
Read [SKILLS_ROOT]/git/SKILL.md and its workflow reference before changing the index or branch.
Briefly identify the resolved skill path and report it if unavailable.

Prepare one reviewed commit for [COMPLETED_TASK] in [REPOSITORY].
Issue/task identifier: [IDENTIFIER_OR_NONE]. Branch action: [USE_CURRENT_OR_CREATE_NEW].
Intended files and exclusions: [SCOPE].

Inspect the worktree and preserve unrelated changes. Follow the skill's branch and commit naming,
keeping an existing task identifier's exact case. Check the staged diff and verify that credentials,
logs, build output, and runtime artifacts are excluded. Use the real configured author and a concise
English message. Add no co-author or generated attribution. Report the commit and validation evidence.
This task authorizes the local commit, without push, tag, release, or history rewriting.
Honor a main-only repository policy. Do not create a branch or pull request when that policy applies.
For explicit whole-history replacement, use the separate single-root snapshot task below.
```

</details>

<details>
<summary>Git single-root snapshot</summary>

```text
Use git from paulocoutinhox/skills.
Read [SKILLS_ROOT]/git/SKILL.md and references/single-snapshot.md before changing refs.

In [REPOSITORY], deliver the complete reviewed tree as one parentless commit on [EXISTING_BRANCH].
Authorized scope: [LOCAL_REWRITE_ONLY_OR_EXACT_REMOTE_AND_BRANCH_REPLACEMENT].
Owner changes to include/preserve, message and author policy: [REPOSITORY_CONTRACT].

Inspect the complete worktree/index and applicable instructions. Preserve intended owner source and
review all removals and private/generated exclusions. This mode is a whole-history replacement,
not an ordinary one-commit change. Do not delete .git, create unsolicited branches or bypass hooks.
Record original local/remote tips and inspect incoming changes. Construct the reviewed root and
update the local branch with its expected-old SHA. If remote replacement is explicitly authorized,
push only that named branch using an explicit observed-SHA lease. Stop and inspect a rejected lease.
Verify complete tree, human metadata, one reachable commit and actual local/remote/CI state.
Do not claim rewriting erases every retained object or revokes a leaked credential.
```

</details>

<details>
<summary>npm library</summary>

```text
Use npm-library and code-developer from paulocoutinhox/skills.
Before editing, read these files and their relevant references:
- [SKILLS_ROOT]/npm-library/SKILL.md
- [SKILLS_ROOT]/code-developer/SKILL.md
Briefly identify the resolved skill paths and report any unavailable package.

Create or prepare [PACKAGE_NAME] in [REPOSITORY] for [PUBLIC_API_AND_CONSUMERS].
Supported runtimes, module formats, license, and release policy: [CONSTRAINTS].
Registry account/scope and GitHub repository/environment: [NON_SECRET_IDENTIFIERS].

Implement the requested API and document installation and usage. Verify package exports, declarations,
published file contents, and installation in a realistic consumer. Configure CI checks and automatic
release through npm trusted publishing with the required OIDC permissions and compatible tooling.
Explain the exact registry-side trust setup and release trigger. Do not substitute a long-lived token.
Validate locally what can be validated, and distinguish it from account setup and an actual publish.
This task prepares the package and workflow. It does not authorize a registry publication.
```

</details>

<details>
<summary>Python library</summary>

```text
Use pypi-library and code-developer from paulocoutinhox/skills.
Before editing, read these files and their relevant references, including the Python profile:
- [SKILLS_ROOT]/pypi-library/SKILL.md
- [SKILLS_ROOT]/code-developer/SKILL.md
Briefly identify the resolved skill paths and report any unavailable package.

Create or prepare [DISTRIBUTION_NAME] in [REPOSITORY] for [PUBLIC_API_AND_CONSUMERS].
Supported Python versions, import name, license, and release policy: [CONSTRAINTS].
PyPI/TestPyPI project and GitHub repository/environment: [NON_SECRET_IDENTIFIERS].

Use uv and the appropriate pyproject/build configuration. Keep __init__.py files empty and use Ruff.
Build and inspect the wheel and source distribution, then verify installation and imports in a clean
consumer environment. Configure CI verification and automatic publication through PyPI trusted
publishing with the appropriate OIDC identity and environment. Explain required registry setup and
release triggers. Distinguish local package evidence from a real registry upload.
This task prepares the package and workflow. It does not authorize a registry publication.
```

</details>

<details>
<summary>Book</summary>

```text
Use book-creator from paulocoutinhox/skills.
Read [SKILLS_ROOT]/book-creator/SKILL.md and the references for the chosen production mode first.
Briefly identify the resolved skill path and report it if unavailable.

Create [PRINT_DIGITAL_OR_BOTH] editions from [MANUSCRIPT_AND_SOURCES] for [AUDIENCE].
Title, author, language, trim size, and target length: [BOOK_BRIEF].
Citation/layout standard: [ABNT_OR_OTHER]. Production provider/template: [DETAILS_OR_UNDECIDED].
Paper, binding, cover stock/finish, color mode, and ISBN: [DETAILS_OR_UNDECIDED].

Clarify production decisions that affect geometry or exports, including front/back matter, cover
inclusion in the interior PDF, image titles/list of figures, and pagination position. Define consistent
styles for headings, body, quotations, notes, citations, bibliography, tables, and figures.
Keep interior page backgrounds white. Build working navigation and reliable bibliography/notes.
Generate requested artwork with an available image model, preserve proportions, and inspect page
breaks, overlaps, readability, bleed/safe areas, and image placement. Derive the spine from the final
page count and actual paper/binding rules, including author/title where feasible. Do not invent an ISBN.
Deliver the requested interior PDF and separate front, back, and full-cover PNGs, plus any required
production PDF, editable sources, and a production checklist. Report actual checks and missing inputs.
```

</details>

<details>
<summary>Workbook</summary>

```text
Use book-creator from paulocoutinhox/skills.
Read [SKILLS_ROOT]/book-creator/SKILL.md and its workbook/layout references first.
Briefly identify the resolved skill path and report it if unavailable.

Create an A4 workbook from [CONTENT] for [AUDIENCE_AND_LEARNING_GOALS].
Delivery: [PRINT_DIGITAL_OR_BOTH]. Style/citation standard: [ABNT_OR_OTHER].
Exercises, answer space/key, illustrations, and production requirements: [DETAILS].

Clarify whether the cover belongs in the same PDF and which internal sections are required.
Define readable styles, page margins, spacing, pagination, notes, citations, and bibliography.
Keep page backgrounds white, provide working navigation, and keep exercises, figures, and tables
readable across page breaks. Generate requested illustrations without distortion. Prepare the chosen
cover/binding files using actual production geometry. Inspect the rendered pages and deliver PDFs,
requested cover images, editable sources, and an explicit list of checks and unresolved inputs.
```

</details>

<details>
<summary>Social post</summary>

```text
Use social-post from paulocoutinhox/skills.
Read [SKILLS_ROOT]/social-post/SKILL.md and the references for the chosen platforms first.
Briefly identify the resolved skill path and report it if unavailable.

Prepare copy for [YOUTUBE_SHORTS_TIKTOK_INSTAGRAM_X_LINKEDIN_SELECTION].
Source material and destination link: [TRANSCRIPT_PRODUCT_OR_ARTICLE_AND_URL].
Audience, language, brand voice, goal, and call to action: [BRIEF].
Post formats and required variants: [FORMATS_AND_VARIANTS].

Adapt the hook, promise, structure, searchable wording, and CTA to each platform and audience.
Return a separate labeled package with every applicable publishing field, including titles,
descriptions/captions, tags, hashtags, links, and accessibility text. Apply the skill's documented
field limits, distinguishing limits from recommendations. Support claims with the supplied material,
avoid misleading hooks and irrelevant hashtags, and identify any limit needing current confirmation.
Provide the copy directly. Do not create counters, datasets, scripts, or automatic updates.
This task prepares content without posting it.
```

</details>

<details>
<summary>Social thumbnail</summary>

```text
Use social-thumbnail from paulocoutinhox/skills.
Read [SKILLS_ROOT]/social-thumbnail/SKILL.md and the relevant platform/design references first.
Briefly identify the resolved skill path and report it if unavailable.

Create thumbnail artwork for [PLATFORM_AND_CONTENT].
Audience, language, main promise, visual identity, and text: [BRIEF].
Reference images, required subjects, and restrictions: [ASSETS_AND_CONSTRAINTS].
Aspect ratio: [RATIO_OR_16:9]. Export format, dimensions, and byte limit: [REQUIREMENTS_OR_ASK].

Clarify missing export constraints. Design a truthful, focused composition with readable typography,
appropriate contrast and theme, safe placement, and proportional subjects. Generate a high-resolution
PNG master using an available image model. Inspect text, faces, hands, perspective, and small-size
readability. Prepare requested derivatives using available native tools, respecting actual format and
file-size requirements. Keep the master. Report actual output properties and any unavailable tool.
Do not bundle converters, counters, or automatic refresh scripts. Do not publish the artwork.
```

</details>

<details>
<summary>Android testing</summary>

```text
Use android-app-testing from paulocoutinhox/skills.
Read [SKILLS_ROOT]/android-app-testing/SKILL.md and the relevant host/device/lab references first.
Briefly identify the resolved skill path and report it if unavailable.

Test [APP_OR_REPOSITORY] from [WINDOWS_MACOS_OR_LINUX].
Build/install inputs, supported Android versions, and key user journeys: [CONTEXT].
Test accounts and deterministic test-data setup: [NON_SECRET_DETAILS].
Available local devices and authorized cloud provider/budget: [RESOURCES_OR_NONE].

Inspect the app and choose a justified emulator/physical-device matrix. Cover forms, input validation,
keyboard/focus, navigation, permissions, accessibility, rotation/resizing, lifecycle/restoration,
network failures, and applicable purchase or deep-link flows. Execute feasible authorized checks
with existing native tools and test frameworks. Explain artifact/framework requirements before any
cloud run, without claiming all providers offer the same devices or services.
Deliver evidence, reproducible failures, coverage, and a clear distinction between executed, planned,
and blocked cases. Do not create unsolicited runners or upload private builds without authorization.
If testing a release AAB, read references/release-bundle-testing.md. Generate/install the exact
bundle-derived APK set, record signing provenance, isolate writable device data, and distinguish
billing-account limits from transaction success.
```

</details>

<details>
<summary>Apple testing</summary>

```text
Use apple-app-testing from paulocoutinhox/skills.
Read [SKILLS_ROOT]/apple-app-testing/SKILL.md and relevant platform/tool/lab references first.
Briefly identify the resolved skill path and report it if unavailable.

Test [APP_OR_REPOSITORY] on macOS for [IOS_IPADOS_TVOS_MACOS_VISIONOS_WATCHOS_SELECTION].
Project/schemes, Xcode/toolchain, supported OS versions, and key journeys: [CONTEXT].
Test-data setup, available hardware, and authorized cloud resources/budget: [NON_SECRET_DETAILS].

Inspect actual destinations and select a justified simulator, native-Mac, and physical-device matrix.
Cover forms, keyboard/focus, remote/Crown/spatial interaction as applicable, navigation, accessibility,
permissions, resizing/lifecycle, restoration, and relevant purchase flows. Use supported test
frameworks and identify platform-specific automation limits. Distinguish native macOS, Catalyst,
compatible iOS apps, and native spatial apps. Verify actual cloud device/artifact support.
Execute feasible authorized checks and deliver reproducible evidence, coverage, and blocked/planned
cases. Do not present simulator checks as hardware proof, invent unsupported automation, create
unsolicited runners, or upload private artifacts without authorization.
For engine/native SDK boundaries or multiple displays, read
references/native-ui-and-multidisplay.md. Verify the active app/sheet, actual executed native
assertions, enumerated display/posture and real captures. Keep control reachability distinct from
completed transactions.
```

</details>

<details>
<summary>Apple app delivery</summary>

```text
Use app-store-connect from paulocoutinhox/skills.
Read [SKILLS_ROOT]/app-store-connect/SKILL.md and references for the selected platforms and stage first.
Briefly identify the resolved skill path and report it if unavailable.

Deliver [APP] from [REPOSITORY] for [IOS_MACOS_TVOS_VISIONOS_SELECTION].
Requested stage: [LOCAL_PREPARATION_BUILD_UPLOAD_TESTFLIGHT_REVIEW_OR_PUBLIC_RELEASE].
Account/app identifiers, signing setup, current version/builds, and locales: [NON_SECRET_CONTEXT].
Audience, positioning, categories, monetization/products, and assets: [BRIEF].

Inventory current/requested fields by owning API/console resource, platform, locale and territory.
Preserve unrequested values and identify exact owner/legal handoffs. Build/sign actual targets and
reserve a fresh build number for each new upload, accounting for concurrent CI allocation.
Use meaningful near-capacity name/subtitle text, complementary keywords and truthful descriptions.
Explain each phrase's intent/feature fit. Prepare actual required captures and current Asset Library
uploads/placements/order, URLs, privacy/reviewer access and applicable product/version/offer graphs.
Verify download/product prices, base/manual schedules, sale countries and existing-subscriber policy.
Apply the current review checklist, submit eligible version/items only within the requested stage,
and handle rejection/cancellation/resubmission with exact build/resource evidence.
Complete assets/release-evidence.md with readback, actual tests, blocked checks and console actions.
Report identifiers and actual review/release/storefront states. Keep credentials out of output.
Diagnose export credential/cloud-signing permission separately from metadata API access. Reconcile
pending uploads before retry. For queued-version replacement, preserve the whole app/product/group
review graph and verify the replacement submission plus complete media placement order.
```

</details>

<details>
<summary>Google Play delivery</summary>

```text
Use google-play from paulocoutinhox/skills.
Read [SKILLS_ROOT]/google-play/SKILL.md and the references for the requested stage first.
Briefly identify the resolved skill path and report it if unavailable.

Deliver [APP] from [REPOSITORY] to [TRACK_AND_REQUESTED_RELEASE_STAGE].
Account/package identifiers, signing, current releases/version codes, and locales: [NON_SECRET_CONTEXT].
Audience, positioning, categories/tags, monetization/products, and assets: [BRIEF].

Inventory current/requested fields, assets, products and review/publishing state before mutation.
Build/inspect the correctly signed bundle and reserve a fresh version code under CI allocation control.
Use meaningful available title/short-description space with actual limits, per-term rationale and
truthful localized descriptions/images. Google has no ordinary App Store subtitle/keywords field.
Verify paid/free download choices, regional Money prices, option/plan/offer activation, region versions,
update masks, countries and existing-subscriber policy. Preserve unrequested settings.
Apply the policy/reviewer checklist and supported Data safety CSV flow, with exact console handoffs.
Choose commit review-conflict behavior explicitly, preserving current review unless replacement is
intended. Handle metadata-only versus binary corrections and actual resubmission/release controls.
Complete assets/release-evidence.md with readback, actual tests, blockers and separate app/update/item
states. Perform only the authorized endpoint and report results without exposing credentials.
For a first draft app, follow references/first-production-release.md through saved prerequisites,
exact production draft confirmation, countries and the full Publishing overview change set. Record
submission acknowledgment, pending quick checks and actual availability separately.
```

</details>

<details>
<summary>RevenueCat</summary>

```text
Use revenuecat from paulocoutinhox/skills.
Read [SKILLS_ROOT]/revenuecat/SKILL.md and relevant store, SDK, and API references first.
Briefly identify the resolved skill path and report it if unavailable.

Prepare or configure [REQUESTED_SCOPE] for [APP_AND_PLATFORMS].
Existing or missing account/project/platform apps, store records and product identifiers: [NON_SECRET_CONTEXT].
Products, billing periods, access rights, paywall goals, and user identity model: [BRIEF].
Authorized environment and changes: [SANDBOX_OR_PRODUCTION_AND_SCOPE].

If the app is absent from RevenueCat, follow references/first-app-setup.md: authenticate, inspect/create
the project and separate platform apps, retrieve public SDK keys, and connect authorized store
credentials through their original protected paths. Distinguish that from creating store app records.
Map store products to entitlements, offerings, packages, and paywalls without conflating their roles.
Explain store prerequisites and supported synchronization boundaries. Use supported APIs/CLI for the
authorized configuration and existing SDK/tooling for integration. Define purchase, restore, account
switch, cancellation, refund, expiration, pending payment, and offline/error behavior as applicable.
Address backend verification, webhook authentication/idempotency, and secret/public key separation.
Distinguish automatic store completion from custom consumable delivery and prevent duplicate credits.
Preserve one paywall editing session, inspect localized previews and native prices/controls, and
publish the reviewed design only within the authorized scope. Verify SDK-visible configuration per app.
Validate sandbox behavior and report actual state/evidence, unexecuted cases, and remaining handoffs.
Do not claim configuration alone publishes store products or an app release.
Use the layer-by-layer diagnosis in references/testing-and-operations.md for partial setup. Record
store notifications and app webhook status separately, with actual native UI and transaction
evidence.
```

</details>

<details>
<summary>Mobile release with subscriptions</summary>

```text
Use app-store-connect, google-play and revenuecat from paulocoutinhox/skills.
Read their actual SKILL.md files and relevant references under [SKILLS_ROOT].
Use apple-app-testing/android-app-testing for the requested native checks, and haylen-app only when
[APP_REPOSITORY] actually uses Haylen. Report a missing skill rather than inventing its tooling.

Deliver [APP_REPOSITORY] to [PREPARE_UPLOAD_REVIEW_OR_PUBLIC_RELEASE] on [PLATFORMS].
App/store identities, account access and approved credential references: [NON_SECRET_CONTEXT].
Plans, entitlement, prices, countries, locales and reviewer access: [APPROVED_PRODUCT_SCOPE].

Inventory existing store/RevenueCat resources before creating missing ones. Reuse original approved
credentials and public SDK keys in the correct clients. Complete products, entitlement, packages and
the reviewed localized paywall, then verify each app's SDK-visible configuration.
Build the final native artifacts with reserved integer build numbers and inspect actual signatures,
versions and packaged configuration. Test real UI and appropriate store-backed transactions, marking
unavailable accounts/hardware cases explicitly. Capture real localized layouts and verify delivery.
For Apple, preserve complete review-item graphs through any authorized replacement. For first Google
publication, complete the production draft and Console prerequisites before sending the whole set.
Report final build hashes, actual remote states, pending checks and remaining gates separately.
Keep private credentials and temporary tooling out of the app source. Existing publication approval
covers its ordinary prerequisites, but does not authorize unrelated commercial/account changes.
```

</details>

<details>
<summary>Playgama</summary>

```text
Use playgama from paulocoutinhox/skills.
Read [SKILLS_ROOT]/playgama/SKILL.md and relevant review, Bridge, tool, media and publication references.
Briefly identify the resolved skill path and report it if unavailable.

Prepare [GAME] from [REPOSITORY_OR_EXPORT] for [REQUESTED_PLATFORM_STAGE].
Engine/export details, target devices, languages, and account/game identifiers: [NON_SECRET_CONTEXT].
Gameplay promise, audience, monetization, saves, achievements, and assets: [BRIEF].

Review every applicable numbered technical, ads/payments, UX, content and engine requirement,
plus the actual destination restrictions and distribution availability.
Inspect host detection, initialization/error states, restored Bridge saves and exact game-ready timing.
Check no game-triggered opening ad, natural-break/SDK scheduling, rewarded opt-in and single grants.
Verify menu/pause mute, initial host mute, overlapping focus/ad/pause states and saved preference.
Test complete progression, clear action/resource limits, repeated consumable purchases, permanent
ownership and transaction recovery. Include desktop/mobile layouts, inputs, localization and rights.
Prepare truthful localized metadata, covers, screenshots, links, and required artwork.
Use supported API/CLI/MCP tools when available and explain exact unsupported or manual handoffs.
Complete assets/review-report.md with exact archive/hash, requirement IDs, actual test evidence,
FAILED defects, BLOCKED unexecuted checks and justified NOT APPLICABLE exclusions.
For corrections, reproduce each finding and retest related flows against the replacement archive.
Perform only the requested authorized upload, sandbox, moderation, or publication stage and verify
its actual state. Report artifacts, evidence, identifiers, outstanding decisions, and tool limitations.
```

</details>

<details>
<summary>Create a skill</summary>

```text
Use skill-creator from paulocoutinhox/skills.
Read [SKILLS_ROOT]/skill-creator/SKILL.md and relevant authoring/research references first.
Identify the resolved path, because a system skill may share this name. Report a missing package.

In [PAULO_SKILLS_CHECKOUT], create a skill for [CAPABILITY_AND_AUDIENCE].
Required outcomes, inputs, platforms, limits, and realistic tasks: [BRIEF].

Read AGENTS.md and inspect existing capability boundaries. Research primary documentation and
relevant professional references before authoring. Distinguish mandatory rules, project preferences,
and recommendations, with verification dates and honest source limitations. Write the professional
procedure, decisions, examples, failure handling, and quality criteria directly in English SKILL.md.
Use focused references/templates only where needed. Keep the package independently installable and
descriptive, with no executable helpers, generated catalogs, or automatic data refresh.
Update the README catalog and task prompts for the new capability or group. Keep all general
repository rules in AGENTS.md. Validate with skills-ref and relevant repository checks.
Review success, missing-input, boundary, and failure scenarios, then report evidence and limitations.
```

</details>

<details>
<summary>Update skill knowledge</summary>

```text
Use skill-creator from paulocoutinhox/skills.
Read [SKILLS_ROOT]/skill-creator/SKILL.md and relevant maintenance/research references first.
Identify the resolved path and report a missing package instead of using a same-name system skill.

In [PAULO_SKILLS_CHECKOUT], review and update [SKILLS_AND_FACTS] at my request.
Reason or suspected changes: [CONTEXT]. Required scope and outcomes: [BRIEF].

Read AGENTS.md and the complete affected entrypoints/references. Research current primary sources
and professional guidance, verify consequential details, and explain conflicts or inaccessible claims.
Rewrite instructions to describe the final current procedure. Remove superseded guidance and unused
resources without adding history to AGENTS.md. Keep the main workflow, examples, decisions, and
quality criteria explicit in SKILL.md. Update source notes, README and task prompts when
their behavior or group coverage changes. Keep independently installable package boundaries intact.
Do not add scripts, scrapers, datasets, scheduled refreshes, or background synchronization.
Run relevant format/repository checks and report factual verification, scenario review, and limits.
Inventory the packages actually used and classify each observed gap before editing. Verify exact
resolved command schemas and response shapes. Add worked normal, partial/interrupted, missing-input,
permission/state and unavailable-tool cases without copying private project details.
```

</details>

<details>
<summary>Python queue</summary>

```text
Use queuefy from paulocoutinhox/skills.
Read [SKILLS_ROOT]/queuefy/SKILL.md and relevant references. Identify the actual loaded path.

Implement [BACKGROUND_WORK_AND_SCHEDULES] in [PYTHON_REPOSITORY].
Framework, package versions, store, and process topology: [CONTEXT].
Durability, latency, retry, timezone, and side-effect requirements: [CONTRACT].

Separate queue composition, task handlers, business services, and lifecycle. Choose the supported
store and async driver, finite deadlines, stable operation keys, explicit retry policies, and graceful
shutdown. Explain transaction/outbox and external-effect boundaries. Verify duplicate enqueue,
concurrent workers, interrupted execution, and recovery against the actual backend. Deliver readable
changes, configuration and architecture notes, and actual evidence without exactly-once claims.
```

</details>

<details>
<summary>Python cache</summary>

```text
Use cachefy from paulocoutinhox/skills.
Read [SKILLS_ROOT]/cachefy/SKILL.md and relevant references. Identify the actual loaded path.

Implement caching for [READS_OR_FUNCTIONS] in [PYTHON_REPOSITORY].
Framework/package versions, source of truth, writers, store, and topology: [CONTEXT].
Allowed staleness, authorization scope, and invalidation requirements: [CONTRACT].

Separate cache composition, producers, business services, and resource lifecycle. Define scoped keys,
TTL/freshness, leases, invalidation, finite client/pool deadlines, and runtime failure behavior.
Keep authorization and critical quotas authoritative. Verify stored None, concurrent misses, stale
refresh, invalidation races, tenant separation, and store outage. Deliver readable changes, current
architecture/configuration docs, actual checks, and consistency limits. Do not add unsolicited
execution wrappers or fact-refresh scripts. The requested cache lifecycle remains application code.
```

</details>

<details>
<summary>Vue application</summary>

```text
Use vue-app from paulocoutinhox/skills.
Read [SKILLS_ROOT]/vue-app/SKILL.md and relevant references. Identify the actual loaded path.

Create or evolve [VUE_APP_OR_FEATURE] in [REPOSITORY].
Language, rendering mode, framework/toolchain, browser targets, and design: [CONTEXT].
Journeys, routes, API contracts, and acceptance criteria: [REQUIREMENTS].

Use focused feature components, composables, services, and domain rules. Keep route composition,
draft, URL, server, and shared state ownership explicit. Add Pinia only where actual shared state
warrants it. Handle forms, accessible errors/focus, cancellation, stale responses, and cleanup.
Keep code readable and one component per file. Run appropriate type/lint/component/browser/build
checks. Document current architecture and commands, and report actual results and remaining inputs.
```

</details>

<details>
<summary>React application</summary>

```text
Use react-app from paulocoutinhox/skills.
Read [SKILLS_ROOT]/react-app/SKILL.md and relevant references. Identify the actual loaded path.

Create or evolve [REACT_APP_OR_FEATURE] in [REPOSITORY].
Language, rendering mode, framework/toolchain, browser targets, and design: [CONTEXT].
Journeys, routes, API contracts, and acceptance criteria: [REQUIREMENTS].

Use focused components, hooks, services, and domain rules. Keep draft, URL, server, and shared state
ownership explicit. Use effects for external synchronization with real cleanup, not mirrored derived
state. Handle accessible forms/errors, stale fetch/save responses, and operation idempotency where
needed. Avoid giant hooks, speculative stores, and unnecessary abstraction. Run relevant type/lint/
behavior/browser/build checks and document current architecture, commands, and actual results.
```

</details>

<details>
<summary>Tailwind interface</summary>

```text
Use tailwind-css from paulocoutinhox/skills.
Read [SKILLS_ROOT]/tailwind-css/SKILL.md and relevant references. Identify the actual loaded path.

Implement [INTERFACE] in [REPOSITORY] with [FRAMEWORK_AND_TAILWIND_MAJOR].
Brand/tokens, supported browsers, themes, responsive contexts, and required states: [BRIEF].

Inspect the actual integration. Use clear semantic tokens, focused components, bounded static variant
maps, and intentional CSS ownership. Check production class detection and external source paths.
Use semantic HTML, labels, keyboard/focus behavior, and readable responsive layout. Verify long
content, localization, dark mode, zoom, and production CSS. Deliver clear code and architecture/setup
notes with actual visual/interaction/build evidence. Do not mix obsolete major-version recipes.
```

</details>

<details>
<summary>Kaktos site</summary>

```text
Use kaktos-site from paulocoutinhox/skills.
Read [SKILLS_ROOT]/kaktos-site/SKILL.md and identify the actual loaded path.

Create [SITE_AND_PAGES] in [KAKTOS_CHECKOUT] for [AUDIENCE_LANGUAGES_AND_DESIGN].
Read the current Kaktos README/features and actual command/configuration/route contracts first.
Organize Jinja layouts/pages/fragments, Python modules/data, processed frontend assets, and raw
root files correctly. Use native build/dev/serve commands. Explain any external form/commerce
service required by the brief. Add custom Python commands only if requested through the real
dispatcher. Inspect production links/assets, SEO metadata, responsive/keyboard behavior, and actual
build output. Deliver source, current AGENTS.md instructions, checks, and unresolved integrations.
```

</details>

<details>
<summary>Fastkit application</summary>

```text
Use fastkit-app from paulocoutinhox/skills.
Read [SKILLS_ROOT]/fastkit-app/SKILL.md and identify the actual loaded path.

Implement [FEATURE] in [FASTKIT_CHECKOUT] for [SURFACES_TENANTS_ROLES_AND_LOCALES].
Read current README/features, architecture, domain guides, and manage.py help. Extend actual
models/schemas/services/routes/resource definitions rather than rebuilding existing systems.
Reuse the real queue/cache, upload, account, and gateway contracts. Keep code modular and readable.
Treat environment selection and destructive seeding explicitly. Add a native Python command only
through the documented extension mechanism if needed. Verify authorization, tenant isolation,
locale behavior, background/cached effects, and site/admin/API consumers. Deliver code, current
architecture/commands, actual test evidence, and remaining external setup.
```

</details>

<details>
<summary>XPLPC mobile</summary>

```text
Use xplpc-mobile from paulocoutinhox/skills.
Read [SKILLS_ROOT]/xplpc-mobile/SKILL.md and identify the actual loaded path.

Implement [APP_AND_SHARED_CPP_FEATURE] in [REPOSITORY] for [NATIVE_PLATFORMS_AND_TOOLCHAINS].
Read current upstream README, language/target guides, and task help. Separate views/view models,
bridge adapters, native mappings, and C++ domain services. Define parameters/results/errors,
initialization, callback thread, owner lifetime, cancellation, and buffer ownership. Use actual
native build/package tasks. Verify delayed calls, teardown, invalid responses, release DTO
serialization, and artifact platform slices. Deliver readable code, mapping/architecture docs,
current commands, actual evidence, and hardware/signing limits without inventing bridge APIs.
```

</details>

<details>
<summary>Haylen application</summary>

```text
Use haylen-app from paulocoutinhox/skills.
Read [SKILLS_ROOT]/haylen-app/SKILL.md and identify the actual loaded path.

Create [APPLICATION] in [REPOSITORY] for [PLATFORMS] using [ENGINE_REVISION_AND_LUA_CPP_SCOPE].
Read the current README/features, matching samples/apps implementation and linked app architecture,
scene/UI/lifecycle and distribution references. Use a Shell for routes/tabs/back, Page/screens for
retained UI and focused domain/service modules. Define list/detail navigation, forms, draft/query
state and the tab restoration policy. Do not build the ordinary app as a simulated game world.
Use physical responsive UI where appropriate, stable widget/item IDs, native text input,
accessible focus, meaningful loading/error/submission states and lifecycle-owned work. Handle
deferred navigation, duplicate taps and obsolete async responses deliberately. Place source,
content, plugins and developer-owned native projects correctly. Build/check actual requested
targets and exercise navigation, forms, resize, failure and background/resume. Deliver source,
present-state AGENTS.md, command/artifact evidence and explicit hardware/signing/service limits.
For runtime diagnosis, read references/debugging-and-release-evidence.md. Launch the Debug session
through Haylen, inspect the actual top scene/owner, test native SDK screens through native UI tools,
and verify the protected content in the final artifact.
```

</details>

<details>
<summary>Haylen game</summary>

```text
Use haylen-app from paulocoutinhox/skills.
Read [SKILLS_ROOT]/haylen-app/SKILL.md and identify the actual loaded path.

Create [GAME] in [REPOSITORY] for [PLATFORMS] using [ENGINE_REVISION_AND_LUA_CPP_SCOPE].
Read the current README/features, game sample and linked game/scene/input/assets/lifecycle guides.
Build a playable boot/menu/gameplay/pause/results slice. Separate world/entities/rules, rendering,
input adaptation, retained HUD, persistence and audio preferences. Choose an explicit timing model,
preload ownership and supported device actions. Avoid a giant scene or speculative abstractions.
Verify a complete run, pause/resume, replay/save/restart, UI/input conflicts, failed loading,
background/audio interruption and actual requested Debug/Release builds. Deliver focused source,
present-state AGENTS.md, actual check/runtime evidence and unexecuted hardware/native-service needs.
```

</details>

<details>
<summary>Haylen plugin</summary>

```text
Use haylen-app from paulocoutinhox/skills.
Read [SKILLS_ROOT]/haylen-app/SKILL.md and identify the actual loaded path.

Create [PLUGIN_ID] for [REAL_CAPABILITY_OR_SDK] on [PLATFORMS] in [PLUGIN_REPOSITORY], and integrate
the reviewed version into [APP_REPOSITORY] at [ENGINE_REVISION]. Read the linked plugin guide,
current template/features and actual SDK contracts. Generate an ID-matching plugin folder and
define manifest parameters/dependencies, public Lua methods/results/events and native handlers.
Use the engine's permission, dispatch, stream/buffer and native-screen lifecycle contracts. Keep
ordinary app page navigation separate. Document unsupported targets and explicit denied/error
outcomes. Do not pass generated echo/banner behavior off as real provider functionality. Test
fresh-host registration, repeated calls, cancellation/denial, teardown and Release retention on
actual supported targets. Deliver source, plugin README, app configuration, present-state AGENTS.md,
build/check/runtime evidence and remaining account/hardware requirements. Do not publish without
authorization or discard modifications in an already installed plugin copy.
```

</details>

<details>
<summary>Haylen upgrade</summary>

```text
Use haylen-app from paulocoutinhox/skills.
Read [SKILLS_ROOT]/haylen-app/SKILL.md and identify the actual loaded path.

Upgrade [APP_AND_OR_PLUGIN_REPOSITORIES] from [CURRENT_REVISION] to [TARGET_ENGINE_REVISION] for
[PLATFORMS]. Read the linked project/plugin upgrade guidance and current templates/CLI contracts.
Inspect the worktree, app kind, plugin graph and developer-owned platform projects. Generate
isolated references of the correct kind and plugin ID/features. Use read-only platform diffs,
then merge required source changes while preserving intentional customization and user data.
Update plugin/native protocols and callers to the final API without compatibility shims. Do not
overwrite customized plugins with plugin add or patch generated haylen/ as source. Regenerate
integration, build requested configurations, check those artifacts and run the actual app/game/
plugin regression paths. Deliver reviewed source changes, present-state AGENTS.md, exact commands,
merge decisions and actual verification gaps. Do not infer runtime success from a last-build check.
```

</details>

<details>
<summary>Reliable information</summary>

```text
Use reliable-information from paulocoutinhox/skills.
Read [SKILLS_ROOT]/reliable-information/SKILL.md and identify the actual loaded path.

Investigate [QUESTION] for [AUDIENCE_AND_DECISION], within [TIMEFRAME_JURISDICTION_OR_VERSION].
Use relevant primary sources, scholarly discovery such as Google Scholar, qualified professional
material, authoritative books, and reputable reporting as appropriate. Inspect actual evidence,
methods, scope, dates, corrections/retractions, and important contradictions. Cite direct sources
beside claims, distinguish inference and uncertainty, and do not imply full access to unread works.
If no reliable support can be verified, state that limitation and withhold the unsupported conclusion
or recommendation. Do not invent facts, sources, credentials, citations, or a consensus.
```

</details>

<details>
<summary>Web testing</summary>

```text
Use web-app-testing from paulocoutinhox/skills.
Read [SKILLS_ROOT]/web-app-testing/SKILL.md and identify the actual loaded path.

Test [WEB_APP] at [AUTHORIZED_LOCAL_OR_STAGING_URLS] for [JOURNEYS_BROWSERS_AND_ROLES].
Start/build commands, fixtures, and constraints: [CONTEXT]. Cloud scope/budget: [AUTHORIZATION_OR_NONE].
Use local Playwright and existing suites/tools. Cover forms, keyboard/focus, navigation, errors,
responsive behavior, and applicable tenant isolation. Select an actually current AWS/Azure/Google
service for the requested remote coverage. Distinguish managed browsers, CI containers, monitoring,
and real device coverage. Use Python/uv for newly requested scripts and no unsolicited runner.
Execute within scope, retain per-case evidence, clean up owned sessions, and report failures,
blocked/planned coverage, and real limitations. Do not use retired services or claim unperformed runs.
Keep saved browser login state in an explicitly ignored path and out of shared artifacts.
```

</details>

<details>
<summary>Markdown Kanban</summary>

### Create a board

```text
Use markdown-kanban from paulocoutinhox/skills.
Read [SKILLS_ROOT]/markdown-kanban/SKILL.md and the references relevant to this task.
Identify the actual loaded path. Report it if unavailable instead of substituting a same-name skill.

Create or initialize [REPOSITORY]/KANBAN.md from this real requested work: [TASKS_AND_OUTCOMES].
Existing workflow, owners, capacity, language and renderer: [KNOWN_CONTEXT_OR_UNSPECIFIED].
Known priorities, dependencies, attachments and evidence: [INPUTS_OR_NONE].

Inspect the repository instructions and any existing board first. Keep TODO, DOING, BLOCKED,
REVIEW, TESTING and DONE side by side with full linked card records in the same Markdown file.
Use stable KB IDs, priorities, complexity, acceptance criteria and truthful evidence. Start from
the empty template only for a new board, preserve existing work and do not import fictional cards.
Make defaults and unknowns explicit. Keep the overview consistent with the authoritative records.
Verify markers, uniqueness, column placement, links, WIP membership and the actual preview when
available. Deliver the file, added IDs, decisions, checks and unresolved inputs. Do not add a
renderer, CLI, CI job, tracker synchronization or start implementing the tasks.
```

### Maintain an existing board

```text
Use markdown-kanban from paulocoutinhox/skills.
Read [SKILLS_ROOT]/markdown-kanban/SKILL.md and relevant operations/flow guidance.
Identify the actual loaded path and report it if unavailable.

Update [REPOSITORY]/KANBAN.md for [CARD_IDS_AND_REQUESTED_CHANGES].
Actual work-state/completion evidence and blockers: [OBSERVATIONS_OR_OWNER_REPORT].

Read the current file before editing. Preserve established IDs, anchors, details and unrelated
changes. Allocate new IDs only when requested and advance Next ID in the same edit. Check the
actual lifecycle and capacity rules before moves, record blocker origin/unblocking action and
distinguish owner-reported evidence from independently executed checks. Keep all records in this
file and synchronize the six-column overview manually. Reconcile concurrent edits instead of
overwriting them. Do not delete/archive work or execute cards without the corresponding request.
Report affected IDs/statuses, actual checks and unresolved conflicts without inventing progress.
```

</details>

## 🤝 Contributing

Read [AGENTS.md](AGENTS.md) for all repository-wide authoring, research, organization, architecture,
validation and delivery rules.

## ☕ Buy me a coffee

Support the continuous development of this project.

<a href="https://ko-fi.com/A0A412XEV"><img height="36" src="https://storage.ko-fi.com/cdn/kofi2.png?v=6" alt="Buy Me a Coffee at ko-fi.com"></a>

## 📄 License

[MIT](LICENSE.md)

Copyright (c) 2026, Paulo Coutinho

---

Made with ❤️ by [Paulo Coutinho](https://github.com/paulocoutinhox)
