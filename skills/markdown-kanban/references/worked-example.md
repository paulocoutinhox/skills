# Worked single-file board

Everything in this example is fictional, including work state and verification statements. It
demonstrates the requested layout, not a real project delivery. For real initialization, use the
[empty template](../assets/KANBAN.md) and actual requested work. The seven cards deliberately include
all six statuses and an uneven column. The illustrative team limit of four differs from the empty
template's single-worker initial limit of one.

## Example working agreements

- **Scope:** Example application maintenance.
- **Next ID:** KB-008
- **Start boundary:** First actual entry into doing.
- **Finish boundary:** Accepted artifact and applicable checks recorded before done.
- **Active WIP limit:** 4 for this fictional team.
- **WIP membership:** KB-002, KB-003, KB-004 and KB-005. The started blocked card still counts.
- **Display order:** Priority critical → high → medium → low, complexity descending, numeric ID ascending.
- **Time convention:** UTC. Missing historical timestamps remain unknown.
- **Service expectation:** Not established from measured data.
- **Visibility:** All records appear once. No card is archived.

<!-- KANBAN:BOARD:START -->

| TODO | DOING | BLOCKED | REVIEW | TESTING | DONE |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **[KB-001 · Add a recovery screen](#kb-001)**<br>🟠 high · `feature` · 4/10 | **[KB-002 · Fix the startup crash](#kb-002)**<br>🔴 critical · `bug` · 3/10 | **[KB-003 · Integrate payment responses](#kb-003)**<br>🟠 high · `feature` · 5/10 | **[KB-004 · Clarify setup instructions](#kb-004)**<br>🟡 medium · `docs` · 2/10 | **[KB-005 · Verify session isolation](#kb-005)**<br>🟠 high · `test` · 6/10 | **[KB-006 · Record supported runtimes](#kb-006)**<br>🟢 low · `chore` · 1/10 |
| **[KB-007 · Explain saved preferences](#kb-007)**<br>🟢 low · `docs` · 2/10 | — | — | — | — | — |

<!-- KANBAN:BOARD:END -->

## Cards

<!-- KANBAN:CARDS:START -->

<a name="kb-001"></a>
### KB-001 — Add a recovery screen

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

<a name="kb-002"></a>
### KB-002 — Fix the startup crash

- **Status:** doing
- **Type:** bug
- **Priority:** critical
- **Complexity:** 3
- **Started:** unknown, imported active work.

#### Description

The fictional app crashes when a clean installation opens its settings store. Reproduce that path,
identify the failing invariant and repair it without silently discarding valid existing settings.

#### Acceptance criteria

- [ ] A clean installation opens successfully.
- [ ] An existing installation retains its valid settings.
- [ ] The reproduced failure has a relevant regression check.

#### Verification

No successful final verification is claimed. Investigation is in progress in this fictional record.

#### Attachments

- None

<a name="kb-003"></a>
### KB-003 — Integrate payment responses

- **Status:** blocked
- **Type:** feature
- **Priority:** high
- **Complexity:** 5
- **Started:** unknown, imported active work.
- **Blocked from:** doing
- **Blocker:** The provider's response contract for uncertain payment outcomes is not confirmed.
- **Unblock action:** The integration owner must obtain the supported reconciliation contract.

#### Description

The adapter implementation started before the unknown-outcome contract was resolved. Preserve
its actual active state and keep it in the WIP count. This does not authorize a real payment.

#### Acceptance criteria

- [ ] Success, rejection and uncertain outcomes have explicit supported behavior.
- [ ] A retry cannot silently duplicate a charge.
- [ ] Reconciliation uses the actual provider operation identity.

#### Attachments

- None

<a name="kb-004"></a>
### KB-004 — Clarify setup instructions

- **Status:** review
- **Type:** docs
- **Priority:** medium
- **Complexity:** 2
- **Started:** unknown, imported active work.

#### Description

A draft explains runtime selection, environment setup and the application's documented launch
sequence. The fictional maintainer has made the draft available for review. Reader acceptance
remains pending, so review does not mean this card is complete.

#### Acceptance criteria

- [ ] Prerequisites match the actual project manifest.
- [ ] A new reader can identify the setup and launch commands in order.
- [ ] Documented commands have relevant execution evidence or explicit limits.

#### Attachments

- None

<a name="kb-005"></a>
### KB-005 — Verify session isolation

- **Status:** testing
- **Type:** test
- **Priority:** high
- **Complexity:** 6
- **Started:** unknown, imported active work.

#### Description

The fictional test environment and controlled accounts are ready. Verify that one account cannot
read another account's private saved preferences through lists, details or exports.

#### Acceptance criteria

- [ ] Owner access works for each relevant path.
- [ ] Another controlled account cannot read the protected records or exported files.
- [ ] Logout/revocation does not leave stale private content available.

#### Verification

Execution is pending in this example. Environment readiness is not a passed test result.

#### Attachments

- None

<a name="kb-006"></a>
### KB-006 — Record supported runtimes

- **Status:** done
- **Type:** chore
- **Priority:** low
- **Complexity:** 1
- **Finished:** unknown, imported accepted work.

#### Description

Record the selected runtime and the compatible dependency/toolchain boundary in the fictional
project's development instructions. No timestamp is inferred from the import.

#### Acceptance criteria

- [x] The selected runtime agrees with the project manifest.
- [x] Setup instructions identify the chosen toolchain and compatible dependencies.

#### Verification

Example-only evidence: the fictional responsible maintainer reported checking the manifest and
accepting the instruction update. This is owner-reported completion, not an actual check performed
while authoring this skill. No real artifact path or command output is invented.

#### Attachments

- None

<a name="kb-007"></a>
### KB-007 — Explain saved preferences

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

<!-- KANBAN:CARDS:END -->

## Decisions this example exposes

The global limit is full even though only one card is doing. Blocking KB-003 does not make room
for KB-001. A request to start another card requires a capacity decision or finishing existing work.
KB-007 can be researched, but its final acceptance depends on actual settings behavior.

When KB-003 is unblocked, return it to the appropriate originating state and preserve its start.
When a required session-isolation case fails, keep KB-005 unfinished with the finding. When the
setup review is accepted, apply only the gates relevant to that documentation outcome.

The overview and seven records agree, but missing historical event times prevent measured cycle
times or an SLE. Do not infer those values from this file's creation date or complexity totals.
