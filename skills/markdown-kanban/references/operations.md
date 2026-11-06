# Card operations and integrity

Read this for detailed edits, dependency changes, rework, withdrawal, archiving or conflicts.
The entrypoint owns the default schema and ordinary update sequence.

## Create useful work units

Choose the type by its intended result, not its priority:

| Type | Useful boundary |
| --- | --- |
| task | A concrete operational result not better described by another type. |
| bug | An observed deviation with actual versus expected behavior and known reproduction/evidence. |
| feature | A new user or service capability with observable acceptance. |
| improvement | An enhancement to an existing capability without a claimed defect. |
| refactor | A structural change with an explicit behavior-preservation boundary. |
| docs | A reader outcome and sources/commands to verify. |
| test | A stated risk, environment, cases and expected evidence. |
| chore | Necessary maintenance with a defined completion condition. |
| spike | A bounded question, timebox and decision/report as its deliverable. |
| epic | A grouping outcome with linked children and an explicit aggregate acceptance rule. |

Describe what is known separately from investigation still required. Do not write an imagined root
cause as a confirmed bug. For a discovery task, accepting a supported negative finding can be the
correct outcome. A feature's acceptance should describe behavior rather than prescribe an arbitrary
implementation that the project has not selected.

Use critical for an actually justified urgent impact, high for important near-term work, medium for
ordinary sequencing and low for work that can reasonably wait. Severity, priority and complexity
answer different questions. A large task is not automatically high priority. A deadline is factual
only when someone authorized it, and a critical label is not automatically permission to exceed WIP.

## Identity and optional fields

Maintain the board's Next ID and inspect all retained IDs. For existing boards without allocation
metadata, establish it from known records/reservations before adding work. If deletions make prior
allocation uncertain, inspect available Git evidence or ask about the conflicting range. Do not
invent assurance that a previously published ID was never used. Keep archived IDs allocated.

| Optional field/section | Use and boundary |
| --- | --- |
| Owner | Real accountable person/team when known. Unassigned is an honest state. |
| Parent / Dependencies | Links to actual card anchors and the precise gate each dependency imposes. |
| Created / Started / Finished | Observed event timestamps with an explicit offset, or an explicitly unknown value. |
| Blocked from / Blocker / Unblock action | Required while blocked. Preserve the original active-stage/start information. |
| Blocked since | Observed time, not the moment someone happened to edit an old imported card. |
| Verification | Checks actually run, result, relevant artifact/revision and unavailable coverage. |
| Decision notes | Consequential scope, priority or policy decisions with attribution where needed. |
| Archived | Boolean true only when withdrawal/archiving has been authorized. Absent means false. |
| Disposition | canceled, duplicate or superseded only for a documented withdrawal, not a new status. |

Do not add every optional field to every card. An unknown timestamp differs from not-started work.
For example, an imported doing card establishes an active state but may not establish its start time.
Do not stamp import time as its historical start. If an observed start event is recorded, use an
unambiguous value such as `2026-11-05T12:00:00Z`, with the actual event time rather than this example.

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

Do these operations only within the user's request. By default preserve all cards, including done.
Do not turn a canceled or duplicate task into successfully done work just to clear a column.

For an authorized withdrawal, keep the last valid Status, set Archived to true, record the factual
Disposition and reason, and link the surviving card where applicable. State in Working agreements
that archived records are excluded from the overview. Keep every full record inside the cards region.
The invariant then becomes one cell per nonarchived card and zero cells per archived card.

For ordinary archiving of genuinely completed work, retain Status done, its acceptance/evidence and
ID. Excluding it from the overview does not erase its actual historical completion. For withdrawal
of unfinished work, report the departure separately from successful delivery and exclude it from
completed throughput/cycle-time samples. Do not hide capacity or aging problems by silently canceling
work. A board without event history cannot reconstruct a truthful historical flow chart.

If a user explicitly requests deletion, check inbound dependencies, preserve required allocation
metadata and explain references that must be updated. Do not erase other cards as a cleanup shortcut.

## Concurrent edits and repair

Markdown does not provide transactions across competing editors. Before writing, compare the current
file with the version inspected. Use a single agreed board writer or existing project coordination.
Do not introduce a new lock daemon or synchronization script. When coordinated editing is unavailable,
stop the conflicting mutation and identify the exact cards/fields needing reconciliation.

If a change landed elsewhere, preserve it and apply a fresh narrow patch. If two editors changed the
same status, do not select the later timestamp blindly. Establish the actual work state. If both
created KB-008, preserve the already established ID, allocate a fresh ID for the unpublished addition
and update its cell, anchor, dependencies and Next ID together. Escalate a collision between two
already published identities instead of silently breaking one set of references.

For a stale overview, use trustworthy records to reconstruct just the affected projection. For a
missing marker, duplicated ID or conflicting record, inspect the file and available Git versions
before changing it. Do not overwrite the whole board from the empty template. Unrelated sections,
attachments and accepted evidence remain intact. A reread alone is not proof that no writer raced it.

## Markdown and attachments

Resolve attachment paths from KANBAN.md, not the skill installation directory. Use meaningful labels
and existing repository-relative files or approved HTTPS URLs. A URL is not proof its content was
opened or access granted. Avoid private absolute paths, expiring signed URLs, customer data and secrets.
A missing file is a reported missing attachment, not a reason to manufacture an unrelated image.

Escape table titles so literal pipes/brackets/backslashes/angle brackets remain text. Prefer a short
plain title to nested Markdown inside the overview. The GFM table extension does not accept block
elements inside cells. Keep checklists, multiline descriptions and image previews below the table.
Keep text labels beside priority colors. Inspect an empty board, uneven columns and narrow preview.

The named anchors used for new boards follow GitHub's documented custom-anchor form. Preserve
working existing ID anchors rather than replacing them without checking incoming links. Opening
the source is not equivalent to clicking links in the actual target preview.
