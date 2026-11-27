# Project Kanban

<!-- KANBAN:BOARD:START -->

| TODO (0 tasks) | DOING (0 tasks) | BLOCKED (0 tasks) | REVIEW (0 tasks) | TESTING (0 tasks) | DONE (0 tasks, 30 days) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| — | — | — | — | — | — |

<!-- KANBAN:BOARD:END -->

## Cards

<!-- KANBAN:CARDS:START -->

<!-- KANBAN:CARDS:END -->

## Working agreements

### Scope and flow

- **Scope:** Not specified yet. Ask the owner, and add the requested cards meanwhile.
- **Start boundary:** First actual entry into doing.
- **Finish boundary:** Accepted outcome and applicable verification recorded before done.
- **Active WIP limit:** 1, an initial single-worker policy. Agree shared-team capacity explicitly.
- **WIP membership:** Started, unfinished cards in doing, review and testing, plus started blocked cards. Archived cards never count.
- **Service expectation:** Not established. No measured forecast is available.
- **Time convention:** UTC unless the project agrees another explicit timezone.
- **Version control:** Excluded locally. KANBAN.md is listed in the local exclude file and is not committed unless the owner explicitly asks. Record the actual state here: excluded locally, already tracked, versioned at the owner's request, or not in a Git repository.
- **Updates:** The board changes right after every change of work on a card, before the report and the next task, with the record and its cell in the same edit. A worker who is not the agreed board writer reports the change to that writer at once.
- **Sensitive data:** None. No credentials, keys, tokens, passwords, connection strings, IP addresses, internal or private host names, signed or expiring URLs, personal or customer data, e-mail addresses, account ids or private absolute paths. Name things by role or variable name. The name or handle of a card's owner, contact or decision maker is allowed.

### Board rules

- **Layout:** The title `# Project Kanban` and the board open the file. Active card records follow in numeric ID order, then these agreements, then the archive as the last section.
- **Next ID:** KB-001. A new card takes the larger of the highest retained ID plus one and this value. Advance it with every new card and never reuse or renumber an ID, even after the archive is cleared.
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
