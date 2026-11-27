# Skill maintenance prompts

Creating skills and updating their researched knowledge in this repository. Read
[how to use the prompts](../task-prompts.md) before you copy one.

## Create a skill

```text
Use skill-creator from paulocoutinhox/skills.
First read [SKILLS_ROOT]/skill-creator/SKILL.md and the matching writing and research references.
Name the path you found, because a system skill may have this name too. Report a missing package.

In [PAULO_SKILLS_CHECKOUT], create a skill for [CAPABILITY_AND_AUDIENCE].
Required outcomes, inputs, platforms, limits, and realistic tasks: [BRIEF].

Read AGENTS.md and look at the current boundaries between skills. Research the primary docs and the
professional references that matter before writing. Keep required rules, project preferences, and
recommendations apart, with the dates you checked them and honest notes on source limits. Write the
professional steps, choices, examples, error handling, and quality checks directly in an English
SKILL.md. Use focused references and templates only where needed. Keep the package text-only and
installable on its own, with no scripts or helpers to run, generated catalogs, or automatic data
refresh.
Update the README catalog, the task prompts and the affected docs/ guides for the new skill or
group. Keep all general repository rules in AGENTS.md. Check with skills-ref and the repository
checks that apply.
Review success, missing-input, edge, and failure cases. Then report the evidence and the limits.
```

## Update skill knowledge

```text
Use skill-creator from paulocoutinhox/skills.
First read [SKILLS_ROOT]/skill-creator/SKILL.md and the matching maintenance and research references.
Name the path you found. Report a missing package. Do not use a system skill with the same name.

In [PAULO_SKILLS_CHECKOUT], review and update [SKILLS_AND_FACTS] at my request.
Reason or suspected changes: [CONTEXT]. Required scope and outcomes: [BRIEF].

Read AGENTS.md and all of the affected entrypoints and references. Research current primary sources
and professional guidance, check the important details, and explain conflicts or claims you could
not reach. Rewrite the instructions so they describe the final, current steps. Remove replaced
guidance and unused resources. Do not add history, migration or compatibility guidance anywhere.
Keep the main workflow, examples, choices, and quality checks clear in SKILL.md. Update source
notes, README, task prompts and the affected docs/ guides when their behavior or group coverage
changes. Keep each package installable on its own.
Do not add scripts, scrapers, datasets, scheduled refreshes, or background sync.
Run the format and repository checks that apply. Report fact checks, case review, and limits.
List the packages you really used and sort each gap you found into a type before editing. Check the
exact command schemas and response shapes as they resolved. Add worked cases for normal,
partial or interrupted, missing-input, permission or state, and missing-tool situations, without
copying private project details.
```
