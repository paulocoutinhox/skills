# Software development prompts

Projects, features, fixes, documentation, reviews, security audits, editor and ignore settings, and
Git delivery. Read [how to use the prompts](../task-prompts.md) before you copy one.

## New project

```text
Use code-developer, editor-config, and git-ignore from paulocoutinhox/skills.
Before editing, read these files and the references that apply:
- [SKILLS_ROOT]/code-developer/SKILL.md
- [SKILLS_ROOT]/editor-config/SKILL.md
- [SKILLS_ROOT]/git-ignore/SKILL.md
Briefly list the skill paths you found. Report any missing skill. Do not use another source instead.

Create a new [PROJECT_TYPE] project in [TARGET_DIRECTORY] using [LANGUAGE_AND_FRAMEWORK].
Product goal: [PROBLEM_AND_USERS]. Required features: [FEATURES].
Target platforms and supported toolchain: [PLATFORMS_AND_VERSIONS].
Limits and outside services: [CONSTRAINTS].

First look at the directory and any existing project instructions. Settle only the choices that
block the work. Use the matching language profile. When there is no existing structure, use the
skill's default structure. Build the working scope with clear responsibilities and explicit error
handling. Create fitting .editorconfig and .gitignore files and an AGENTS.md that describes the
project as it is now.
Set formatter widths in each formatter's own settings so every call stays on one line. For
ktlint, that setting is max_line_length in the Kotlin section of .editorconfig.
Document setup, settings, how to run it, the structure, and the useful check commands.
Run the checks that match what you built. Report the real results and any setup still needed.
Do not add automation nobody asked for or compatibility layers. Do not publish or deploy this
project.
```

## Implement a feature

```text
Use code-developer from paulocoutinhox/skills.
First read [SKILLS_ROOT]/code-developer/SKILL.md and the matching language/framework references.
Briefly list the skill path you found. If it is missing, say so. Do not claim it was loaded.

Implement [FEATURE] directly in [REPOSITORY_OR_DIRECTORY].
Expected behavior and acceptance criteria: [OBSERVABLE_RESULTS_AND_EDGE_CASES].
Related entrypoints, integrations, and limits: [CONTEXT].

Read the project's AGENTS.md. Look at the affected callers, state, storage, and UI/API contracts.
Follow the existing structure and the chosen toolchain. Make the final code clear and complete, with
explicit errors, easy-to-follow control flow, and no generic fallback or legacy branches.
Keep each call on one line. Fix any formatter width that wraps calls.
Keep code and needed comments in English. Update the affected docs and the AGENTS.md guidance when
the structure or commands change. Check the affected consumers and the failure paths that matter.
Report what behavior changed, the check results, and anything still waiting on outside settings.
```

## Fix or refactor

```text
Use code-developer from paulocoutinhox/skills.
Read [SKILLS_ROOT]/code-developer/SKILL.md and the matching language references before changing code.
Briefly list the skill path you found. If it is missing, say so.

In [REPOSITORY], [FIX_OR_REFACTOR] the following behavior: [ISSUE].
Steps to reproduce or current evidence: [STEPS_LOGS_OR_CODE_PATH].
Expected final behavior and scope: [ACCEPTANCE_CRITERIA].

Find the cause and the affected consumers before editing. Fix real failures that the evidence shows.
For a refactor, keep the stated behavior unless the task clearly changes it. Remove old branches and
resources that this change makes unneeded. Avoid guesswork rewrites and compatibility layers. Check
the reproduction, the failure paths that matter, and the integrations this change touches.
Update the docs and AGENTS.md when their current instructions change. Explain the cause, the final
behavior, and the real check results. Leave unrelated work as it is.
```

## Documentation

```text
Use code-developer from paulocoutinhox/skills.
Read [SKILLS_ROOT]/code-developer/SKILL.md and its Markdown reference before editing.
Briefly list the skill path you found. If it is missing, say so.

Create or improve [DOCUMENTS] in [REPOSITORY] for [AUDIENCE_AND_PURPOSE].
Required topics and real examples: [TOPICS].

Check the documented behavior against the real project. Explain what is needed first, inputs,
commands, expected output, errors, and the limits that matter, in a natural reading order. Use
working relative links, correct code fences, and correct examples. Keep AGENTS.md as instructions
that cover only the current structure, conventions, and commands. Remove guidance that conflicts in
the affected documents. Check local links and the examples that can run. Report the checks you ran
and the examples that could not run.
```

## Code review

```text
Use code-review from paulocoutinhox/skills.
Read [SKILLS_ROOT]/code-review/SKILL.md and the references that apply before reviewing.
Briefly list the skill path you found. If it is missing, say so.

Review [DIFF_COMMIT_RANGE_OR_FILES] in [REPOSITORY].
Intended behavior: [TASK_AND_ACCEPTANCE_CRITERIA]. Related limits: [CONTEXT].

Look at the change and its callers, consumers, schemas, state changes, and deployment assumptions.
Follow likely regressions across the project. Do not review the changed lines on their own.
Focus first on correctness, security, concurrency, data safety, and missing checks for real risks.
For each finding, give the severity, file/line, trigger, effect on users, evidence, and a concrete
fix. Keep confirmed findings apart from questions and gaps in coverage. Do not make up findings to
reach a number. Report the checks you really ran and what is still uncertain. This task is review
only, with no edits.
```

## Security audit

```text
Use security-audit from paulocoutinhox/skills.
First read [SKILLS_ROOT]/security-audit/SKILL.md and the matching platform references.
Briefly list the skill path you found. If it is missing, say so.

Audit [REPOSITORY_OR_SYSTEM] within [AUTHORIZED_TARGETS_AND_ENVIRONMENT].
Platforms, sensitive assets, user roles, and tenant boundaries: [CONTEXT].

Map the entrypoints and trust boundaries. Then look into the authentication, authorization,
input/output handling, secrets, storage, dependencies, and release risks that apply. Check whether
one user can reach another user's records, files, exports, jobs, and subscription state. A
hard-to-guess ID in a URL does not replace a per-record permission check. Check only in a local
environment or one you are allowed to test.
Give findings with evidence, what an attacker needs, the effect, the affected paths, the fix, and
checks that stop it coming back. Name the boundaries you did not test. Do not expose secrets or run
probes that can destroy data.
Deliver an audit report. Implement fixes only if the allowed task clearly includes them.
```

## Editor configuration

```text
Use editor-config from paulocoutinhox/skills.
First read [SKILLS_ROOT]/editor-config/SKILL.md and its rules for the file types that apply.
Briefly list the skill path you found. If it is missing, say so.

Create or fix .editorconfig in [REPOSITORY].
Look at the real languages, generated files, formatters, and current conventions. Set fitting
encoding, line ending, final newline, whitespace, and indentation rules, including the file-type
exceptions that matter. Keep whitespace that the syntax depends on. Match the file to how the
formatters really behave and leave line width to each formatter's own settings. Set
max_line_length only for a formatter such as ktlint that reads it from .editorconfig, using the
wide value from the Code Developer Kotlin profile. Document deliberate choices. Check a few typical
files and explain any conflict you could not settle.
Do not reformat unrelated files as part of this task.
```

## Ignore rules

```text
Use git-ignore from paulocoutinhox/skills.
First read [SKILLS_ROOT]/git-ignore/SKILL.md and the guidance for the matching ecosystem.
Briefly list the skill path you found. If it is missing, say so.

Create or fix .gitignore in [REPOSITORY].
Look at the real toolchains. Tell apart source, lockfiles, required wrappers, generated output,
caches, environments, test files, runtime data, system files, and private settings.
Use exact rules that leave out the unwanted files and keep the needed project files and examples.
Check a few typical paths and look for sensitive or generated files that are already tracked. Do
not print secrets. Report tracked files that need separate cleanup. Ignore rules alone do not
remove tracked files.
Do not delete local files or rewrite history.
```

## Git delivery

```text
Use git from paulocoutinhox/skills.
Read [SKILLS_ROOT]/git/SKILL.md and its workflow reference before changing the index or branch.
Briefly list the skill path you found. If it is missing, say so.

Prepare one reviewed commit for [COMPLETED_TASK] in [REPOSITORY].
Issue/task ID: [IDENTIFIER_OR_NONE]. Branch action: [USE_CURRENT_OR_CREATE_NEW].
Files to include and leave out: [SCOPE].

Look at the worktree and keep unrelated changes. Follow the skill's branch and commit naming, and
keep the exact letter case of an existing task ID. Check the staged diff. Make sure credentials,
logs, build output, and runtime files are left out. Use the real configured author and a short
English message. Add no co-author or generated attribution. Report the commit and the check results.
This task allows the local commit only, with no push, tag, release, or history rewrite.
Follow a main-only repository policy. When that policy applies, do not create a branch or pull
request.
To replace the whole history on purpose, use the separate single-root snapshot task below.
```

## Git single-root snapshot

```text
Use git from paulocoutinhox/skills.
Read [SKILLS_ROOT]/git/SKILL.md and [SKILLS_ROOT]/git/references/single-snapshot.md before
changing refs.
Briefly list the skill path you found. If it is missing, say so.

In [REPOSITORY], deliver the whole reviewed tree as one commit with no parent on [EXISTING_BRANCH].
Allowed scope: [LOCAL_REWRITE_ONLY_OR_EXACT_REMOTE_AND_BRANCH_REPLACEMENT].
Owner changes to include or keep, message and author rules: [REPOSITORY_CONTRACT].

Look at the whole worktree and index and the instructions that apply. Keep the owner's intended
source. Review every removal and every private or generated file you leave out. This mode replaces
the whole history. It is not a normal one-commit change. Do not delete .git, create branches nobody
asked for or skip hooks.
Write down the original local and remote tips and look at incoming changes. Build the reviewed root
commit and update the local branch with a check on its expected old SHA. If you are clearly allowed
to replace the remote, push only that named branch with an explicit lease on the SHA you saw. If the
lease is rejected, stop and look into it.
Check the whole tree, the human author details, that one commit is reachable, and the real local,
remote and CI state.
Do not claim that rewriting erases every kept object or cancels a leaked credential.
```
