# Card operations and integrity

Read this for detailed edits, dependency changes, rework, withdrawal, archiving or conflicts.
The entrypoint owns the default schema, layout and update sequence.

## Create useful work units

Choose the type by its intended result, not its priority. These are frequent types and what each
needs. Any other common work-item word is valid too:

| Type | Useful boundary |
| --- | --- |
| task | A concrete operational result not better described by another type. |
| bug | An observed deviation with actual versus expected behavior and known reproduction/evidence. |
| fix | The repair of a known defect, linked to its bug card when one exists, with the regression check. |
| hotfix | An urgent fix for released software, with the affected release and the verification it shipped with. |
| security | A vulnerability or hardening outcome with its exposure boundary and verification. |
| performance | A measurable speed or resource target with its baseline measurement. |
| design | A user-facing design outcome with the screens or states it covers and who approves it. |
| research | A question, the sources to check and the written finding as its deliverable. |
| feature | A new user or service capability with observable acceptance. |
| improvement | An enhancement to an existing capability without a claimed defect. |
| refactor | A structural change with an explicit behavior-preservation boundary. |
| docs | A reader outcome and sources/commands to verify. |
| test | A stated risk, environment, cases and expected evidence. |
| chore | Necessary maintenance with a defined completion condition. |
| spike | A limited question, timebox and decision/report as its deliverable. |
| epic | A grouping outcome with linked children and an explicit combined acceptance rule. |

Describe what is known separately from investigation still required. Do not write an imagined root
cause as a confirmed bug. For a discovery task, accepting a supported negative finding can be the
correct outcome. A feature's acceptance should describe behavior rather than prescribe an arbitrary
implementation that the project has not selected.

Use critical for an actually justified urgent impact, high for important near-term work, medium for
ordinary sequencing and low for work that can reasonably wait. Severity, priority and complexity
answer different questions. A large task is not automatically high priority. A deadline is factual
only when someone authorized it, and a critical label is not automatically permission to exceed WIP.

## Identity and optional fields

Keep the Next ID in the working agreements and check all retained IDs. A new card takes the larger
of the Next ID and the highest retained ID plus one. If the Next ID is missing or doubtful, for
example after the archive was cleared, ask the owner for the highest ID ever used and do not guess.
Look at Git or editor history only when the board is tracked or a backup exists. Archived and
deleted IDs stay used.

| Optional field/section | Use and boundary |
| --- | --- |
| Owner | Real accountable person/team when known. Unassigned is an honest state. |
| Parent / Dependencies | Links to the real card headings, such as `[KB-002](#kb-002)`, and the precise gate each dependency imposes. |
| Created / Started | Observed event timestamps with an explicit offset, or an explicitly unknown value. |
| Finished | Required on done cards. The actual completion date or timestamp, or `unknown` when it was never recorded. It drives the done window. |
| Blocked from / Blocker / Unblock action | Required while blocked. Preserve the original active-stage/start information. |
| Blocked since | Observed time, not the moment someone happened to edit the card. |
| Verification | Checks actually run, result, relevant artifact/revision and unavailable coverage. |
| Progress | The current state of started work, rewritten at each substantial step, never a dated log. |
| Decision notes | Important scope, priority or policy decisions with attribution where needed. |
| Archived | The date the card left the board, set by the done window or an authorized request. Present only on records in the archive. |
| Closed as | canceled, duplicate or replaced only for a documented withdrawal, not a new status. |

Do not add every optional field to every card. An unknown timestamp differs from not-started work.
For example, a card already in progress when the board was created establishes an active state but
not its start time. Do not stamp the board's creation time as its historical start. If an observed
start event is recorded, use an unambiguous value such as `2026-11-05T12:00:00Z`, with the actual
event time rather than this example.

## Moves, dependencies and rework

Move the existing card rather than duplicate it. Update acceptance/evidence as the work changes.
Review means a reviewer has an inspectable result. Testing means the intended artifact and cases
are available for verification. Neither state proves review or tests passed.

When blocking, retain the originating state, a concrete condition for resuming and the next action.
For an API-credential blocker, record who can grant access and the approved secret-delivery channel.
Never attach credentials to the board. A card depending on a blocker is not automatically blocked
if useful independent work remains. Conversely, do not start a supposedly independent task whose
acceptance is impossible under its unresolved prerequisite.

Unblock to the appropriate originating stage after observing the condition cleared. Do not reset
Started, discard failed-test findings or mark dependent cards done. A dependency ending in done
does not prove the consuming integration works. Cycles require a scope/sequence decision, not
arbitrary status shuffling.

For a failure in review/testing, record the relevant finding and return to doing when repair starts.
Retain the original identity and timing. Use a new linked bug for a distinct issue rather than
rewriting an unrelated card. When splitting an oversized card, retain its identity as the parent or
scope record, allocate new child IDs and remove any claim that the children are already delivered.
Check that the parent and children do not double-count WIP or completed throughput units.

## Cancel, deduplicate and archive

The done window archives completed work automatically during authorized edits. Withdrawal,
deduplication, early archiving, restoring and deletion happen only within the user's request. Do not
turn a canceled or duplicate task into successfully done work just to clear a column.

For an authorized withdrawal, keep the last valid Status, set `Archived` to the date, record the
`Closed as` value and the reason, and link the surviving card where applicable. Move the full record
to the end of the archive. Remove the archived card's cell and move that column's lower cells up as
in an ordinary move. An archived card never counts toward active WIP. Report the departure
separately from successful delivery and exclude it from completed throughput and cycle-time samples.
Do not hide capacity or aging problems by silently canceling work.

Archive a done card before its window ends only when the user explicitly asks to hide it. Its record
moves to the archive and keeps Status done, its acceptance/evidence and ID. Excluding it from the
board does not erase its actual completion. A board without event history cannot reconstruct a
true historical flow chart.

Delete records only on an explicit request. Deleting archived cards follows the entrypoint's
procedure. When the user explicitly asks to delete a card that still has a cell, remove its cell as
well, check inbound dependencies, keep `Next ID` unchanged and explain references that must be
updated. Do not erase other cards as a cleanup shortcut.

## Concurrent edits and repair

Markdown does not provide transactions across competing editors. Before writing, compare the current
file with the version inspected. Use a single agreed board writer or existing project coordination.
Do not introduce a new lock daemon or synchronization script. When coordinated editing is unavailable,
stop the conflicting change and identify the exact cards and fields that need to be matched up.

If a change landed elsewhere, preserve it and apply a fresh narrow patch. If two editors changed the
same status, do not select the later timestamp blindly. Establish the actual work state. If both
created KB-008, preserve the already established ID, allocate a fresh ID for the unpublished addition
and update its cell, heading, links, dependencies and Next ID together. Escalate a collision between two
already published identities instead of silently breaking one set of references.

For a stale board, use trustworthy records to rebuild just the affected cells and their header
counts. For a missing marker, duplicated ID or conflicting record, inspect the file, and its Git or
backup history when one exists, before changing it. Do not overwrite the whole board from the empty
template. Unrelated sections, attachments and accepted evidence remain intact. A reread alone is not
proof that no writer raced it.

## Markdown and attachments

Resolve attachment paths from KANBAN.md, not the skill installation directory. Use meaningful labels
and existing repository-relative files or approved HTTPS URLs. A URL is not proof its content was
opened or access granted. Never use private absolute paths, signed or expiring URLs, customer data or secrets.
A missing file is a reported missing attachment, not a reason to manufacture an unrelated image.

Escape table titles so literal pipes/brackets/backslashes/angle brackets remain text. Prefer a short
plain title to nested Markdown inside the board. The GFM table extension does not accept block
elements inside cells. Keep checklists, multiline descriptions and image previews below the table.
Keep text labels beside priority colors. Inspect an empty board, uneven columns and narrow preview.

Card links point at the ID-only card headings, as the entrypoint's card-links rules describe. Opening
the source is not the same as clicking links in the real target preview.

