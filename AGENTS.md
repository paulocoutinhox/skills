# Paulo Skills

## Purpose and operating contract

The canonical repository is `paulocoutinhox/skills`. Use that path in repository links, badges,
clone instructions and task prompt provenance. The collection's visual brand is Paulo Skills.

This repository distributes independent descriptive Agent Skills in English for Codex, Claude Code, and other clients implementing the shared Agent Skills format. The product is researched procedural knowledge, written in `SKILL.md` with focused reading references and document templates. The current skill inventory is the README catalog. There is no collection-wide application runtime or autonomous content maintenance service.

Read this file before editing. Inspect the relevant skill entrypoints, linked resources, README and current worktree before deciding the scope of a change. Follow the user's requested outcome and existing authorization. Complete independent work when an input is missing, and identify the exact decision or external capability blocking the remaining work. Do not claim that a skill, source, command or remote operation was used unless it actually was.

Keep this file an instruction manual for the present repository. Describe what the project contains, how it is organized, what maintainers must do, and how to verify their work. Replace obsolete instructions when behavior changes. Do not add task diaries, completed-work lists, before/after narratives, migration stories, or historical implementation notes. Report delivery history through Git and the task response.

## Repository map

- `skills/<skill-name>/SKILL.md` is the portable entrypoint for one capability.
- `skills/<skill-name>/references/` contains detailed guidance loaded only for the relevant task.
- `skills/<skill-name>/assets/` contains templates copied into user projects.
- Skills contain no executable helpers, parsers, counters, converters, generated API catalogs, or automatic data refresh machinery.
- `AGENTS.md` contains all collection-wide authoring, architecture, research, organization, validation and delivery rules, regardless of the skill being edited.
- `README.md` contains the public catalog, installation/update instructions, invocation guidance and ready-to-copy task prompts.
- `extras/images/logo.svg` is the editable vector brand asset.
- `extras/images/logo-dark.svg` is its dark-background variant. `logo-master.png` retains the generated raster concept. Keep bitmap provenance and editable vector assets distinct.
- Both vector logos use the approved `#22C7B5` teal wordmark and secondary module, with their respective indigo main module. Preserve geometry and spacing when changing palette.
- `scripts/` contains repository installation and validation utilities.
- `scripts/html-link-helper.py` is an internal standard-library HTML parser for the repository checker, not a standalone command or a distributed skill helper.
- `Makefile` provides help and thin targets for the existing Python/uv contributor commands. `make validate` is the local/CI aggregate, and `make valide` is its alias.
- `tests/` checks repository installation, validation, configuration and packaging using temporary directories.
- `.github/` contains validation CI, issue templates, and funding metadata. Do not configure bots to create pull requests.

Keep general rules in this file and skill-specific procedures inside the corresponding existing
skill package. Do not create a collection-level documentation directory, per-skill usage guides,
review archives or separate general-rule files. Do not move collection documentation into skills.
Focused skill references and document/configuration assets exist only for their actual domain task,
not for repository policies, installation manuals or task history. Keep task checklists and review
results in the conversation. The README is the public entrypoint and links directly to SKILL.md.

## Capability boundaries

Select the smallest set of skills that covers the task. Compose complementary capabilities through explicit inputs and handoffs. Do not duplicate an entire neighboring workflow or make one skill depend on another installed package.

| Capability | Responsibility |
| --- | --- |
| Skill Creator | Research, portable authoring, instruction quality, execution-gap diagnosis and user-requested knowledge maintenance. |
| Markdown Kanban | Single-file KANBAN.md layout, stable card identity, manual overview/detail consistency, work state, blockers, capacity and evidence. Tracking does not authorize executing the cards. |
| Code Developer | Implementation and language/framework guidance, including technical Markdown. |
| Vue App / React App | Feature/component architecture, state ownership, forms, data boundaries, lifecycle, and production verification. |
| Tailwind CSS | Tokens, semantic variants, responsive/theme behavior, class generation, and accessible presentation. |
| Queuefy / Cachefy | Python queue/cache integration, actual upstream contracts, lifecycle, concurrency, and consistency boundaries. |
| Kaktos Site / Fastkit App | Application creation with the exact upstream purpose, layout, feature contracts, and native Python commands. |
| XPLPC Mobile | Framework-specific shared C++/native architecture, callback/data ownership, actual targets, build/package and runtime verification. |
| Haylen App | Separate app Shell/Page/retained-UI navigation from game simulation and plugin-native screens. Own real project/plugin generation, native integration, deliberate template upgrades and target verification. |
| Reliable Information | Verifiable source selection, claim appraisal, citations, uncertainty, and withholding unsupported conclusions. |
| Web App Testing | Local Playwright, actual cloud-browser/CI/monitoring distinctions, supported current services, and execution evidence. |
| Code Review | Evidence-based assessment and cross-project impact analysis. Implement fixes only when requested. |
| Security Audit | Platform-specific trust boundaries, vulnerability investigation, evidence, and remediation guidance. |
| Editor Config / Git Ignore | Actual repository file conventions and generated/private file exclusions. |
| Git | Branch naming, a reviewed index and the intended commit mode. Root snapshots and remote rewrites require their actual explicit scope. |
| npm Library / PyPI Library | Package design, consumer verification, CI, and trusted registry publication. Account-side trust remains explicit. |
| Book Creator | Editorial structure, typography, navigation, citations, production geometry, and print/digital deliverables. |
| Social Post / Social Thumbnail | Platform-specific copy, visual design, export requirements, and content quality. |
| Android App Testing | QA from Windows, macOS, and Linux, actual emulator/hardware/lab coverage, and execution evidence. |
| Apple App Testing | QA from macOS across iOS/iPadOS, tvOS, macOS, visionOS, and watchOS with supported inputs and destinations. |
| App Store Connect / Google Play | Supported API-family and field ownership, build/sign/upload, ASO, media, pricing/availability, billing, policy readiness, review correction and release controls with exact evidence and console handoffs. |
| RevenueCat | Products, entitlements, offerings, packages, paywalls, SDK integration, and subscription operations. |
| Playgama | HTML5 packaging, Bridge lifecycle, supported tools, monetization/media, numbered moderation requirements, engine/destination scope, regression evidence and publication stages. |

Domain-specific limits and platform support belong in the responsible skill and its source notes. Describe actual simulator/device and cloud coverage, API/CLI availability, account/legal prerequisites, and lifecycle states. Testing is distinct from store release. Subscription infrastructure does not replace store app records, binaries, review, or initial account setup. Keep private uploads, paid runs, account mutations, and publication within the user's actual authorization.

For Haylen, derive application guidance from current `samples/apps` and game guidance from actual
game samples. App screens use the engine scene stack and retained UI, with explicit routes, tabs,
back policy and state ownership. They are not a simulated game world. Treat native SDK screens as
plugin foreground flows, not ordinary page navigation. Explain actual template generation and
developer-owned `platform/` versus generated `haylen/` source boundaries. Upgrade projects/plugins
through comparisons and deliberate merges, preserving intentional customization. Never invent an
upgrade command, claim per-tab history from root replacement or call a last-build check runtime QA.

## Portable package structure

Use the shared Agent Skills specification. Every skill directory must contain `SKILL.md` with YAML frontmatter containing `name` and `description`. The name matches the directory, uses lowercase ASCII letters, digits, and single hyphens, and is at most 64 characters. The description states the capability and activation conditions, is nonempty, and is at most 1,024 characters. Use only standard frontmatter for portable entrypoints. Optional standard fields must satisfy the specification. Client-specific metadata is optional and must never be required for the workflow.

Keep the principal professional procedure, decisions, worked examples and quality criteria in the entrypoint. Keep it below 500 lines and preferably below 5,000 tokens. These are project limits and specification recommendations, not additional mandatory format fields. Link focused references and document templates with a clear purpose. Do not create empty directories or unfinished implementation scaffolds. A skill must work when copied independently. Never link outside its directory for required guidance.

Use relative links inside the package for required references and assets. Every supporting resource must be reachable from the entrypoint through relevant guidance. Assets are usable document or configuration templates. Keep licenses, examples, metadata, and resource names consistent with the actual package. Remove obsolete resources and their callers together.

Resolve each Markdown link relative to its containing document. A sibling reference uses its filename,
and an asset linked from a reference uses `../assets/`. Do not prepend `references/` again inside that
directory. This file-relative rule and the independent-package boundary apply together.

## Research and professional instruction quality

Research before creating or materially updating a skill. Prefer current official specifications, vendor/API documentation, language references, and authoritative standards. Use relevant professional books, research, and engineering material to substantiate judgment when they add practical value. Do not present a popularity list or bibliography as a substitute for explaining the procedure. Never imply that an inaccessible standard or unread book was consulted in full.

Record source links, actual verification dates, applicable versions/platforms, consequential claims, and unresolved limitations in focused source notes. Explain conflicts instead of silently combining incompatible requirements. Separate official requirements, user/project conventions, and recommendations. Identify configurable defaults and when they should change. Do not copy entire standards, manuals, prompts, or third-party source files.

Write instructions an agent can act on. Explain:

- Scope, triggers, exclusions, required inputs, sensible defaults, and decisions that require clarification.
- Prerequisites, supported environments, real tools, authentication boundaries, and authorized operations.
- Ordered steps, intermediate artifacts/states, decision criteria, and relevant alternatives with their selection conditions.
- Concrete examples with realistic inputs and outputs, including at least one meaningful failure or boundary case.
- Actual error handling, partial completion, recovery, unsupported operations, and exact human or console handoffs.
- Deliverable formats, acceptance criteria, inspection procedures, and evidence needed to claim completion.

Cover the supported cases with appropriate depth. Route conditional language, platform, production, or service details into focused references without making the main workflow superficial. Do not claim exhaustive support for cases that have not been researched. Recheck volatile platform limits, registry contracts, tool versions, and production templates for the actual operational task. Keep that verification distinct from authorization to update this repository's stored facts.

## Mandatory descriptive-content rules

Write the researched procedure, decisions, actual limits, examples, quality criteria, and explanations in each `SKILL.md`. A skill must teach the agent how to perform the work professionally. Do not replace that knowledge with scripts, parsers, generated data files, large schema dumps, or a request to research everything later. Focused language references and bibliographic source notes can support the entrypoint, but must not leave its principal workflow unexplained.

Only the user initiates content maintenance through a request in this repository. Research and edit the affected instructions when requested. Do not add scheduled refreshes, web scrapers, background updates, self-updating scripts, automatic synchronization, or CI jobs that change skill facts. Verification dates describe what was actually checked, not a promise that data remains current. Operational consultation of a vendor's API contract does not authorize rewriting this collection's content.

Social publishing and thumbnail skills are descriptive. Explain text limits, visual decisions, export settings and checks in prose. Use native publishing/editor tools where available. Do not bundle character counters, image converters, regex datasets or similar automation. Other skills follow the same knowledge-first rule.

The repository's existing installation and static-validation commands are contributor tooling, separate from skill content. They must not refresh provider information or perform user-domain tasks. If the user explicitly requests an automation script, write it in Python and run it with uv. Do not introduce Bash or JavaScript wrappers. Native application code can use its required language, and direct vendor CLI commands remain appropriate examples. Explain this distinction rather than turning frontend implementation or a Git command into an artificial Python wrapper.

Do not invent APIs, copy private credentials, flatten lifecycle states, or represent unsupported console steps as available API operations. Document supported resource groups, request semantics, authentication, ordered state transitions and exact human handoffs in the skill text.

For store/API skills, distinguish create/update/response models, edit-scoped versus standalone writes,
repeated-field replacement, current versus deprecated resources and state-dependent permissions.
Document consequential defaults, commercial/customer effects and verification of saved fields.
Keep the readable workflow and examples in Markdown. Do not substitute a generated contract dump.
ASO guidance explains intent and truthful relevant wording. Meaningful near-capacity title/subtitle
or short-description use is an owner preference, not a store minimum or ranking guarantee.

## Creating and updating skills

1. Inspect the current package boundaries and related documentation. Identify the requested outcome, realistic users/tasks, inputs, exclusions, and authorization boundaries. Resolve whether the work belongs in an existing skill or a distinct capability.
2. Research the consequential details before drafting. Establish supported cases, official requirements, configurable defaults, professional recommendations, source limitations, and a source record.
3. For a new skill, choose a narrow hyphenated name and a discriminating activation description. For an update, inspect the complete affected procedure and its references so edits do not leave contradictions elsewhere.
4. Write the actionable entrypoint with the principal workflow, decisions, examples, errors, and quality checks. Explain the actual native tools and supported operations. Extract substantial conditional details into focused references.
5. Add only resources that materially support the written procedure. Keep the package independently installable, resources reachable, and terminology consistent. Do not bundle executable helpers or generated API data.
6. Update the README catalog, links and task prompts, plus any general instructions in this file affected by the change. Keep the skill's procedure self-contained instead of creating a separate usage guide. Remove superseded guidance and unused resources in the same scope.
7. Run official `skills-ref` validation and relevant repository checks. Inspect local links and standalone package boundaries. Verify installer behavior when packaging or installer logic changes.
8. Review realistic success, missing-input, conflicting/default, unsupported-operation, authorization, and failure scenarios. Check that an agent can identify the next action and expected result from the instructions. Format validation does not establish domain correctness.
9. Inspect the final diff for consistency, researched claims, current documentation, unintended changes, and private/generated artifacts. Report actual verification and unresolved limits. Follow the Git delivery rules when committing.

Do not broaden authorization, auto-publish content, or install into user directories merely because a skill is being authored. A source URL, prompt example, or documented command is not evidence that an operation executed.

## Task prompts and group coverage

Maintain the [README task prompts](README.md#-task-prompts) as practical, copyable examples. Every skill must appear in the README catalog and in at least one usable prompt. Every new task group needs a dedicated prompt. When adding, removing, renaming or materially changing a skill or group, update the affected catalog links and prompt examples in the same change. Keep prompt-maintenance rules here and public examples in the README.

Prompts must identify `paulocoutinhox/skills` as the intended source, name the applicable skills, and direct the agent to read their actual `SKILL.md` files and relevant references. Provide an explicit root/path input and handle missing or same-name packages honestly. Naming a GitHub owner does not install or activate skills. Do not invent a universal command namespace or promise that prompts override client permissions or higher-priority instructions.

Keep prompts ready to copy with clearly marked inputs, a concrete task, observable deliverables, appropriate checks and relevant authorization boundaries. Explain client-specific selection separately from portable file-reading instructions. Choose the smallest applicable skill set. Combined tasks must define stage order and handoffs rather than loading unrelated skills. Keep factual procedures in the skills and link their entrypoints instead of duplicating volatile limits in prompt examples. Confirm official client invocation behavior when changing that guidance.

## Code and content conventions

Write instructions, code, identifiers, comments, commit messages, and documentation in English. Use hyphens for filenames unless a language or tool requires another form, such as Python imports, `SKILL.md`, `AGENTS.md`, or GitHub's template filenames. Give each class, enum, component, view, or page its own appropriately named source file. Do not hide a second class/enum in a file by calling it supporting code. Language-required constructs keep their valid structure. Keep responsibilities visually separated with blank lines. Prefer readable concrete code, explicit errors, early returns, and named intermediate results. Avoid compatibility layers, generic fallbacks, dead code, speculative abstractions, and duplicated processes. Extract a context-specific helper class only when shared support logic warrants it, in its own file.

Comments are rare, explain necessary intent, use complete English sentences, and end with a period. Do not join prose sentences with semicolons or add decorative section comments. Required syntax, shebangs, formatter directives, and declarative configuration headings are exceptions to prose rules. Python `__init__.py` files remain completely empty. Do not use `TYPE_CHECKING` imports. Use uv for dependencies and Ruff for Python formatting and linting.

Every Python filename under `scripts/` uses hyphens between words, including internal helper
modules. Load a hyphenated sibling module with standard-library `importlib.import_module` using
its exact stem. Do not retain underscore aliases or duplicate module files. Test filenames and
imports under `tests/` retain Python's normal unittest discovery conventions.

Preserve the requested development preferences in the code-developer references. Distinguish them from universal language rules. Do not claim that a slug replaces authorization, a print PNG replaces a required press PDF, an Arial choice is mandated by ABNT, or one spine multiplier fits every paper and binding.

## Commands and verification

Use Python 3.11+ and uv for contributor tooling. The locked environment supplies skills-ref,
Ruff, EditorConfig, filelock and the CommonMark parser. The installer copies complete packages,
refuses existing destinations and symbolic sources/resources, and uses a native destination-scoped
filesystem lock. Stage copies before publication and roll back only owned new directories after a
handled failure. Preserve existing user files. Do not bypass an active lock or claim distributed
filesystem safety or whole-collection atomicity after forced process termination.

The checker validates self-contained skill packages and real repository Markdown links. A skill
must not depend on a collection-level usage guide. Exercise contributor tools using isolated
temporary fixtures, including actual subprocess invocation from another working directory when
module loading or CLI behavior changes. These checks do not execute every described domain task,
verify remote URL availability or certify a model's compliance with the written instructions.

```bash
uv sync --locked
uv run --locked python scripts/validate-skills.py
uv run --locked python scripts/check-repository.py
uv run --locked python -m unittest discover -s tests -v
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --script scripts/install-skills.py codex code-review --destination /tmp/paulo-skills-preview
```

`pyproject.toml` and `uv.lock` pin the validation environment. The `skills-ref` upstream revision is immutable. Local validation and CI use `make validate`, whose skill-format step calls `scripts/validate-skills.py` and invokes `skills-ref validate` for every immediate skill directory, stopping on failure. CI runs on pushes to main and manual dispatch, with read-only repository permissions and no model calls or model credentials. Network is required to install tools, not to validate installed skills. The Makefile contains direct tool invocations, not domain automation or a separate validation implementation.

Run only checks warranted by the change. Documentation changes need local-link/integrity checks and manual review of the affected guidance and examples. Skill changes also need reference format validation and scenario review. For contributor-tool changes, test actual output, invalid inputs, concurrent access and protection against overwrites, then run applicable lint/format checks. Do not add tests that assert editorial wording or mirror the implementation. Do not claim that CI ran remotely when only local commands ran.

Keep Markdown link parsing and HTML attribute parsing separate. Use CommonMark tokens for actual
Markdown links and the standard-library HTML parser for src/href attributes. HTML comments and
data-src attributes do not route resources. Invalid UTF-8 must fail aggregate validation with
file-specific diagnostics while allowing other documents to be checked. Do not replace decoding
errors with lossy text or suppress a failed package as successful validation.

Use the repository checker's shared local-target parser for both document checks and resource
reachability. Report malformed URLs as validation failures and continue checking independent links.
Reject symbolic Markdown documents and entrypoints before reading their targets. A package with
symbolic resources fails its portability inventory before link traversal. Keep repeated diagnostics
from the package and document passes consolidated in the aggregate result.

Before delivery, confirm that the requested scope is implemented, affected guidance describes current behavior, new/changed groups have usable prompts, referenced resources resolve, and reported checks actually ran. Distinguish mechanical validation, researched factual confidence, manual scenario review, and actual domain execution. State remaining external setup or blocked verification concretely rather than declaring unsupported completeness.

## Git, privacy, and delivery

Work directly on `main`. This repository has no feature-branch or pull-request workflow. Do not create branches, worktree branches, pull requests, automated dependency PRs or merge commits. Keep exactly one parentless commit reachable from `main`, containing the complete reviewed repository snapshot. Each requested delivery replaces that snapshot rather than adding a child commit. Use the real configured human author and a simple, short English subject such as `update skills`. Do not add a message body, co-author trailers, generated-by footers, agent names, research source names or third-party attribution. These repository-specific rules take precedence over optional branch and conventional-message workflows in the portable Git skill.

The owner explicitly authorizes rewriting and force-pushing `main` to maintain this single-commit
snapshot for requested repository deliveries. This standing authorization includes the owner's
pending repository edits, even when they were made before the current task. Review the entire
worktree, including tracked changes and legitimate new source files, and include those owner edits
in the same snapshot unless the owner explicitly excludes them. Do not leave a reviewed owner
change unpublished merely because it was not authored during the agent's task. Exclude private,
generated and temporary artifacts under the rules below.

Record the actual remote main SHA, inspect incoming changes and stage the reviewed delivery files.
Create the replacement root commit from the reviewed index without parents, preserving the complete
existing source tree and including the authorized pending owner changes. Always finish a repository
delivery with the push, rather than stopping at a local commit.
Update local main with an expected-old-SHA check. Push only main with an explicit
`--force-with-lease=refs/heads/main:<observed-remote-sha>`. Never use an unconditional force push or
silently advance a rejected lease. Inspect and preserve unexpected remote changes before retrying.
Verify local and remote main resolve to the replacement root, its reachable commit count is one,
its message/author meet this contract and actual CI succeeds before reporting success.

Stage only reviewed files. Check the staged diff, ignored files, temporary artifacts, logs, credentials, signing material, personal data and package archives. Never commit `.venv`, caches, build output, runtime files or secrets. Keep lockfiles, sanitized examples, source assets and required wrapper tooling. A `.gitignore` cannot protect an already tracked secret. Never erase unrelated user changes. The main-snapshot authorization above applies only to `paulocoutinhox/skills`. Other repositories, tags, releases, deletion and publication still require their own task authorization. Keep the final report factual about validation and any remaining external setup.
