# Flow policies for a Markdown tracker

Read this when setting capacity, deciding what to pull or discussing delivery observations.
The six columns and complexity scale are the owner's board profile. Published Kanban guidance
does not prescribe this exact layout, taxonomy or display sort.

## State the operating boundary

Write the relevant service/project, unit of work, start/finish events, pull criteria and who can
change priorities or policies beside the board. Clarify whether done means verified implementation,
accepted document or actual production release. A repository merge is not automatically public
publication. Keep the boundary appropriate to the work rather than silently changing it mid-card.

A team can accept different gates for bugs, docs and research, provided their acceptance remains
explicit. Do not add ceremonies simply to imitate a framework. Use the board when replenishing
requested work, examining current obstacles and deciding a useful improvement.

## Capacity and pull

The template starts with an active-WIP limit of one for a single worker. It is an initial selected
constraint, not measured optimal capacity. For a shared team, agree actual limits and whether they
apply globally, by stage or to another explicit scope. If the board already exceeds its adopted
limit, make the excess visible and reduce started work rather than silently cancel cards or raise
the limit. Never move existing work backward merely to make the number look smaller.

Under the default start/finish boundary, active WIP includes started unfinished doing/review/testing
cards and started blocked cards. A blocked card retains the stage from which it was blocked and
still consumes that stage's capacity when stage limits are used. A pre-start blocker from todo is
waiting demand, not started work. If an imported blocked card's origin is unknown, flag the uncertain
membership and avoid claiming an exact active count until reconciled.

For example, with global limit two, one doing card and one blocked card that started in doing leave
no free slot. Moving the blocked card to a different column does not free capacity. A review of its
unblocking options may be more useful than starting a third task. A blocked pre-start request would
not consume that same active slot under the stated boundary.

Prioritization answers which requested result matters. Display sorting answers how the table is
organized. Selection also considers dependencies, feasibility, age and agreed service rules. Do not
interpret complexity descending as evidence that the largest task has the greatest value. If a
different ready-order/FIFO policy is selected, document its order explicitly instead of presenting
the prototype's sort as the actual pull queue.

An expedited request requires an explicit reason and tradeoff. Critical is a priority label, not
an unlimited bypass lane. Record an authorized WIP exception and the action to restore normal flow.
Never claim that adding an owner to a field supplied actual staffing or capacity.

## Observations and honest interpretation

Use observed events and the same stated time boundary for every comparable item. These common flow
measures have distinct inputs:

| Measure | Evidence and interpretation |
| --- | --- |
| Active WIP | Started unfinished items still inside the selected system. Do not count todo demand as execution. |
| Throughput | Actual completed items in an explicit time interval. Complexity totals are not this measure. |
| Work item age | Elapsed time from an observed start to now for an unfinished item. |
| Cycle time | Elapsed time from the agreed start to actual finish for a completed item. |

For an illustrative calendar-time calculation, an item started at 09:00 UTC on November 1 and
finished at 09:00 UTC on November 4 has three elapsed days of cycle time. One still open at the
same time on November 5 has four days of age. A blocked interval remains in that elapsed time.
Working-day/time conventions need their actual calendar and should not be mixed with these values.

Never backfill timestamps from the first Git commit that happened to mention an old card. Imported
state may be known while its historical timing is not. State the missing observations. Reopened,
withdrawn, split and parent/child items need an explicit inclusion rule before their counts support
an analysis. Do not count a canceled item as delivered value or double-count one result through
both an epic and its execution children.

An SLE combines a timeframe and a probability for comparable work. Use actual historical observations
when available and identify the population, period, time convention and uncertainty. If the owner
adopts an initial estimate without data, label it as a working hypothesis. The template intentionally
does not fabricate an SLE. Small/mixed or missing observations do not justify a measured forecast,
and a forecast does not become a guaranteed individual due date.

No metric collector, chart generator or historical reconstruction is bundled. If the user requests
a report, manually inspect the actual retained observations and state what they support. A static
snapshot alone cannot establish every historical transition or a causal improvement in performance.

## Review and improve deliberately

Examine aging started work, blockers without an actionable owner, overloaded review/testing and
large items that repeatedly stall. Improve a specific limiting condition, such as clarifying an
acceptance gate, splitting an oversized outcome or resolving a dependency. Record consequential
policy choices beside the board when authorized. Do not promise that WIP reduction or a daily
meeting guarantees a particular delivery speed. Source roles and access limits are in [sources](sources.md).
