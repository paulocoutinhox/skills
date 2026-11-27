# Worked single-file board

Everything in this example is fictional, including work state, dates and verification statements.
It shows the layout, not a real project delivery. For real initialization, use the
[empty template](../assets/KANBAN.md) and actual requested work.

The board was last edited on 2026-11-24 (UTC). Its eight cards cover all six statuses and an uneven
column. KB-006 finished more than 30 days earlier, so it is archived: its cell has left the board
and its record sits in the archive at the end of the file. No edit happened between the end of
KB-006's window and this edit, which also recorded KB-008's completion on 2026-11-18, the date the
owner reported. The example team limit
of four differs from the empty template's single-worker limit of one.

```markdown
# Project Kanban

<!-- KANBAN:BOARD:START -->

| TODO (2 tasks) | DOING (1 task) | BLOCKED (1 task) | REVIEW (1 task) | TESTING (1 task) | DONE (1 task, 30 days) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **[KB-001 · Add a recovery screen](#kb-001)**<br>🟠 high · `feature` · 4/10 | **[KB-002 · Fix the startup crash](#kb-002)**<br>🔴 critical · `fix` · 3/10 | **[KB-003 · Integrate payment responses](#kb-003)**<br>🟠 high · `feature` · 5/10 | **[KB-004 · Clarify setup instructions](#kb-004)**<br>🟡 medium · `docs` · 2/10 | **[KB-005 · Verify session isolation](#kb-005)**<br>🟠 high · `test` · 6/10 | **[KB-008 · Document the release checklist](#kb-008)**<br>🟡 medium · `docs` · 2/10 |
| **[KB-007 · Explain saved preferences](#kb-007)**<br>🟢 low · `docs` · 2/10 | — | — | — | — | — |

<!-- KANBAN:BOARD:END -->

## Cards

<!-- KANBAN:CARDS:START -->

### KB-001

- **Title:** Add a recovery screen
- **Status:** todo
- **Type:** feature
- **Priority:** high
- **Complexity:** 4

#### Description

Give a signed-out user a clear recovery path after a login link expires. This card concerns the
screen and navigation. Server verification remains a separate implementation boundary.

#### Acceptance criteria

- [ ] The screen explains that the link expired without revealing another user's data.
- [ ] The user can request another link and retain the intended destination.
- [ ] Loading, success and error states are readable with keyboard and assistive technology.

#### Attachments

- None

### KB-002

- **Title:** Fix the startup crash
- **Status:** doing
- **Type:** fix
- **Priority:** critical
- **Complexity:** 3
- **Started:** unknown, already in progress when the board was created.

#### Description

The app crashes when a clean installation opens its settings store. Reproduce that path, identify
the failing rule and repair it without silently discarding valid existing settings.

#### Acceptance criteria

- [ ] A clean installation opens successfully.
- [ ] An existing installation retains its valid settings.
- [ ] The reproduced failure has a relevant regression check.

#### Verification

No successful final verification is claimed. Investigation is in progress.

#### Attachments

- None

### KB-003

- **Title:** Integrate payment responses
- **Status:** blocked
- **Type:** feature
- **Priority:** high
- **Complexity:** 5
- **Started:** unknown, already in progress when the board was created.
- **Blocked from:** doing
- **Blocker:** The provider's response contract for uncertain payment outcomes is not confirmed.
- **Unblock action:** The integration owner must obtain the supported reconciliation contract.

#### Description

The adapter implementation started before the unknown-outcome contract was resolved. Preserve
its active state and keep it in the WIP count. This does not authorize a real payment.

#### Acceptance criteria

- [ ] Success, rejection and uncertain outcomes have explicit supported behavior.
- [ ] A retry cannot silently duplicate a charge.
- [ ] Reconciliation uses the actual provider operation identity.

#### Attachments

- None

### KB-004

- **Title:** Clarify setup instructions
- **Status:** review
- **Type:** docs
- **Priority:** medium
- **Complexity:** 2
- **Started:** unknown, already in progress when the board was created.

#### Description

A draft explains runtime selection, environment setup and the documented launch sequence. The
maintainer has made the draft available for review. Reader acceptance remains pending, so review
does not mean this card is complete.

#### Acceptance criteria

- [ ] Prerequisites match the actual project manifest.
- [ ] A new reader can identify the setup and launch commands in order.
- [ ] Documented commands have relevant execution evidence or explicit limits.

#### Attachments

- None

### KB-005

- **Title:** Verify session isolation
- **Status:** testing
- **Type:** test
- **Priority:** high
- **Complexity:** 6
- **Started:** unknown, already in progress when the board was created.

#### Description

The test environment and controlled accounts are ready. Verify that one account cannot read another
account's private saved preferences through lists, details or exports.

#### Acceptance criteria

- [ ] Owner access works for each relevant path.
- [ ] Another controlled account cannot read the protected records or exported files.
- [ ] Logout/revocation does not leave stale private content available.

#### Verification

Execution is pending. Environment readiness is not a passed test result.

#### Attachments

- None

### KB-007

- **Title:** Explain saved preferences
- **Status:** todo
- **Type:** docs
- **Priority:** low
- **Complexity:** 2
- **Dependencies:** [KB-002](#kb-002) must establish the actual settings behavior before final wording.

#### Description

Explain where user preferences are stored and what happens after reinstall or account changes.
Keep the final description aligned with the repaired settings behavior.

#### Acceptance criteria

- [ ] Persistence and reset behavior agree with the accepted implementation.
- [ ] The document distinguishes local storage from server-backed account data.
- [ ] No credential or private local machine path appears in the explanation.

#### Attachments

- None

### KB-008

- **Title:** Document the release checklist
- **Status:** done
- **Type:** docs
- **Priority:** medium
- **Complexity:** 2
- **Finished:** 2026-11-18

#### Description

Write the ordered release checklist the maintainers already follow, including who approves each
step, so a new maintainer can run a release without verbal handoff.

#### Acceptance criteria

- [x] Every release step names its owner and the evidence it produces.
- [x] A second maintainer followed the checklist on a staging release without asking for help.

#### Verification

Owner-reported: the second maintainer confirmed the staging walk-through.

#### Attachments

- None

<!-- KANBAN:CARDS:END -->

## Working agreements

### Scope and flow

- **Scope:** Example application maintenance.
- **Start boundary:** First actual entry into doing.
- **Finish boundary:** Accepted artifact and applicable checks recorded before done.
- **Active WIP limit:** 4 for this team.
- **WIP membership:** Started, unfinished cards in doing, review and testing, plus started blocked cards. Archived cards never count.
- **Service expectation:** Not established from measured data.
- **Time convention:** UTC. Missing historical timestamps remain unknown.
- **Version control:** Excluded locally. KANBAN.md is listed in the local exclude file and is not committed unless the owner explicitly asks. Record the actual state here: excluded locally, already tracked, versioned at the owner's request, or not in a Git repository.
- **Updates:** The board changes right after every change of work on a card, before the report and the next task, with the record and its cell in the same edit. A worker who is not the agreed board writer reports the change to that writer at once.
- **Sensitive data:** None. No credentials, keys, tokens, passwords, connection strings, IP addresses, internal or private host names, signed or expiring URLs, personal or customer data, e-mail addresses, account ids or private absolute paths. Name things by role or variable name. The name or handle of a card's owner, contact or decision maker is allowed.

### Board rules

- **Layout:** The title `# Project Kanban` and the board open the file. Active card records follow in numeric ID order, then these agreements, then the archive as the last section.
- **Next ID:** KB-009. A new card takes the larger of the highest retained ID plus one and this value. Advance it with every new card and never reuse or renumber an ID, even after the archive is cleared.
- **Records:** Card records are the source of truth. Update the board and records together through direct Markdown edits.
- **Cells:** One card per cell with its linked ID and title, priority, type and complexity. Unused cells hold `—`.
- **Column counts:** Each column header shows its number of cards on the board, such as `TODO (3 tasks)`, `TODO (1 task)` or `TODO (0 tasks)`. DONE also shows the window, such as `DONE (12 tasks, 30 days)`, or only the count with `Done window: all`. Archived cards are not counted. Every edit that changes a column updates its count in the same edit.
- **Card links:** Each card heading is `### KB-nnn` alone, followed by its `Title` field. Links use the lowercase ID, such as `#kb-001`, so a title change breaks no link. No HTML anchors.
- **Terms:** Types use common work-item words such as feature, bug, fix or hotfix. Common status and priority words map to the six statuses and four priorities. Canceled or duplicate work is a withdrawal, not done. A word never blocks an edit.
- **Column order:** TODO, DOING, BLOCKED, REVIEW and TESTING put the highest priority on top: critical → high → medium → low, then numeric ID ascending.
- **DONE order:** Most recently finished on top: Finished date descending, then numeric ID descending. `unknown` dates go at the bottom.
- **Unblock:** A blocked card returns to the column in its Blocked from field, and its blocked fields are removed.
- **Moves:** Only the affected columns change, with their header counts, plus done-window archiving. Cells below a departing card move up one row, and cells below an inserted card move down one row.
- **Done window:** 30 calendar days, shown in the DONE header. A card finished on 2026-10-25 stays through 2026-11-24. The first edit on or after 2026-11-25 archives it. Check the window on every edit. An older done card gets `Archived` with the date, loses its cell and moves to the end of the archive. A shorter window archives more cards at once. A longer one does not restore archived cards.
- **Finished:** Required on every done card, with the actual completion date or `unknown`. A completion reported or observed today uses today's date, unless the person gives an earlier actual date. Unknown dates keep the card on the board, at the bottom of DONE.
- **Priority change:** Move the cell to its new priority position within its column. A done card keeps its place.
- **Reopen:** Remove Finished and any Archived field, move an archived record back to Cards, record why and place the cell by its new column's rule.
- **Priority labels:** 🔴 critical, 🟠 high, 🟡 medium, 🟢 low.
- **Archive:** Archived records live only below `## Archive`, each added at the end when archived. Deleting everything below that heading clears old work, and the next edit restores the marker. Delete archived records only on request.
- **Withdrawal:** A canceled, duplicate or replaced card keeps its last status, gets Archived with the date, a `Closed as` value and the reason, and moves to the archive.
- **Restore:** Only on request. Remove Archived, and `Closed as` for a withdrawn card, move the record back to Cards in ID order and place the cell by its column's rule. A done card still outside the window stays archived.

## Archive

<!-- KANBAN:ARCHIVE -->

### KB-006

- **Title:** Record supported runtimes
- **Status:** done
- **Type:** chore
- **Priority:** low
- **Complexity:** 1
- **Finished:** 2026-10-09
- **Archived:** 2026-11-24

#### Description

Record the selected runtime and the compatible dependency/toolchain boundary in the project's
development instructions.

#### Acceptance criteria

- [x] The selected runtime agrees with the project manifest.
- [x] Setup instructions identify the chosen toolchain and compatible dependencies.

#### Verification

Owner-reported: the responsible maintainer checked the manifest and accepted the instruction update.

#### Attachments

- None
```

## What this board shows

Active WIP is KB-002, KB-003, KB-004 and KB-005, so the limit of four is full. Blocking KB-003 does
not make room for KB-001. A request to start another card needs a capacity decision or finishing
existing work first. KB-007 can be researched, but its final acceptance depends on KB-002.

KB-006 finished on 2026-10-09, which is 46 days before 2026-11-24. The 2026-11-24 edit archived it,
removing its cell and moving its full record, still done, to the archive. It still counts as
completed work in any throughput report. KB-008 finished on 2026-11-18 and stays on the board
through 2026-12-18. When KB-002 later reaches done, its cell goes on top of DONE, above KB-008,
because the most recent completion is read first.

## A move on this board

The setup review for KB-004 is accepted and the card moves to testing. The record's status changes
to `testing`. Its cell leaves REVIEW, which becomes `—`, and goes into TESTING below KB-005, whose
high priority outranks KB-004's medium. TESTING now needs two cells, and the second row already
exists, so the table keeps two rows. The REVIEW header becomes `REVIEW (0 tasks)` and the TESTING
header `TESTING (2 tasks)`. TODO, DOING, BLOCKED and DONE are untouched, and active WIP
stays at four:

```markdown
| TODO (2 tasks) | DOING (1 task) | BLOCKED (1 task) | REVIEW (0 tasks) | TESTING (2 tasks) | DONE (1 task, 30 days) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **[KB-001 · Add a recovery screen](#kb-001)**<br>🟠 high · `feature` · 4/10 | **[KB-002 · Fix the startup crash](#kb-002)**<br>🔴 critical · `fix` · 3/10 | **[KB-003 · Integrate payment responses](#kb-003)**<br>🟠 high · `feature` · 5/10 | — | **[KB-005 · Verify session isolation](#kb-005)**<br>🟠 high · `test` · 6/10 | **[KB-008 · Document the release checklist](#kb-008)**<br>🟡 medium · `docs` · 2/10 |
| **[KB-007 · Explain saved preferences](#kb-007)**<br>🟢 low · `docs` · 2/10 | — | — | — | **[KB-004 · Clarify setup instructions](#kb-004)**<br>🟡 medium · `docs` · 2/10 | — |
```

## Failure and boundary cases

- When KB-003 is unblocked, it returns to DOING, its origin, below the critical KB-002. Its start
  is preserved.
- When a required session-isolation case fails, KB-005 stays unfinished with the finding, or returns to
  doing when repair starts. No duplicate card hides the rework.
- If KB-008 had `Finished: unknown`, it would stay on the board and the edit report would ask the owner
  for the actual date instead of inferring one.
- Missing historical start times prevent measured cycle times or a service expectation. Do not infer
  them from this file's creation date or complexity totals.
