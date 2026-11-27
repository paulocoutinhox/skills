# Planning prompts

Markdown Kanban boards. Read [how to use the prompts](../task-prompts.md) before you copy one.

## Markdown Kanban

### Create a board

```text
Use markdown-kanban from paulocoutinhox/skills.
Read [SKILLS_ROOT]/markdown-kanban/SKILL.md and the references that apply to this task.
Name the path really loaded. If it is missing, say so. Do not use a skill with the same name instead.

Create or set up [REPOSITORY]/KANBAN.md from this real requested work: [TASKS_AND_OUTCOMES].
Current workflow, owners, capacity, language and renderer: [KNOWN_CONTEXT_OR_UNSPECIFIED].
Known priorities, dependencies, attachments and evidence: [INPUTS_OR_NONE].

First read the repository instructions and any existing board. Start the file with the title
`# Project Kanban` and the TODO, DOING, BLOCKED, REVIEW, TESTING and DONE table, each header with
its card count, such as `TODO (3 tasks)` and `DONE (12 tasks, 30 days)`. Then add the full linked
card records, the working agreements and board rules, and the archive as the last section. Keep
KANBAN.md out of version control through the local exclude file, found with
`git rev-parse --git-path info/exclude`, and do not commit it. Leave an already tracked board
tracked and say so. Use common terms for types, statuses and priorities, and do not get stuck on
wording. Use stable KB IDs, priorities, complexity, acceptance criteria and honest evidence. Start
from the empty template only for a new board. Keep existing work and do not add made-up cards. State
defaults and unknowns clearly. Keep the board in line with the card records. Put no sensitive data
in the file: no credentials, IPs, private host names, signed URLs, personal data, account ids or
private paths. Check markers, that IDs are unique, column order rules, links, WIP membership and the
real preview when you can. Deliver the file, the IDs you added, your choices, checks and inputs
still open. Do not add a renderer, CLI, CI job or sync with a tracker, and do not start doing the
tasks.
```

### Maintain an existing board

```text
Use markdown-kanban from paulocoutinhox/skills.
Read [SKILLS_ROOT]/markdown-kanban/SKILL.md and the operations and flow guidance that apply.
Name the path really loaded, or say it is missing.

Update [REPOSITORY]/KANBAN.md for [CARD_IDS_AND_REQUESTED_CHANGES].
Real work state, proof of completion and blockers: [OBSERVATIONS_OR_OWNER_REPORT].

Read the current file before editing. Keep existing IDs, card headings, links, details and unrelated
changes. Give out new IDs only when asked, and raise the Next ID in the working agreements in the
same edit. Check the real lifecycle and capacity rules before moving cards. Record where a blocker
came from and what will unblock it. Keep evidence the owner reported apart from checks you ran
yourself. Keep all records in this file. Update the board by hand following its column order rules,
change only the affected columns, and update their header counts. Record the real Finished date on
done cards. When it is not known, write `Finished: unknown` and ask the owner. Archive done cards
past the agreed window: add `Archived` with today's date, remove their cells and move their records
to the end of the archive section. Update the board right after every change of work, before
reporting it, and put no sensitive data in it. Merge edits made at the same time instead of
overwriting them. Do not delete or withdraw work, or carry out cards, unless asked to. Report the
affected IDs and statuses, archived cards, real checks and conflicts still open. Do not make up
progress. Do not commit KANBAN.md unless I clearly ask.
```
