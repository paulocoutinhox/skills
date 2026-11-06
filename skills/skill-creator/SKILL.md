---
name: skill-creator
description: Research, write, and revise descriptive Agent Skills with precise procedures, evidence, examples, standard metadata, and observable quality criteria. Use when creating a SKILL.md or improving an existing skill's professional depth.
license: MIT
---

# Skill Creator

Write an operational guide that transfers professional judgment. The deliverable is knowledge another agent can apply, not a persona, a list of slogans, a collection of scripts, or an instruction to research the subject from scratch later.

## Establish the task contract

Identify the user's outcome, the artifacts they expect, the target environment, and what counts as finished. Inspect available project context before asking questions. Separate a missing preference that can use a stated default from a missing fact that would make the result false or unusable.

Write down these decisions before drafting:

| Decision | Required detail |
| --- | --- |
| Activation | Real requests that should select the skill, plus adjacent requests that should not |
| Inputs | Which facts come from the user, project, source material, or current service account |
| Output | Files/content, format, intended audience, and acceptance evidence |
| Modes | Meaningful alternatives such as print/digital or preparation/publication |
| Boundaries | Actual permissions, unavailable tools, legal facts, and unsupported capabilities |
| Failure | How to explain an unresolved input while completing independent work |

For example, “make a professional book” is insufficient. A useful contract specifies trim, delivery mode, manuscript language, editorial standard, front matter, navigation, paper/binding, ISBN status, and the actual production template. It does not invent missing manufacturing dimensions.

## Research before prescribing

Use the source that governs the exact operation. A product's API schema governs fields, its policy guide governs approval, and an editorial book can explain communication or composition. None substitutes for the others.

For each consequential claim, record the URL, inspected material, date, applicable version/surface, supported decision, and uncertainty. A source note should explain what changed in the procedure because of the evidence. Do not add impressive book titles without connecting them to a decision.

Prefer this evidence order for technical requirements:

1. Applicable specification, official API contract, standard, or tool behavior.
2. Maintainer guidance and a relevant implementation/example.
3. Primary empirical research for claims about effectiveness.
4. Professional books and named practitioners for reasoning frameworks.
5. Secondary summaries when primary access is unavailable, with that limitation stated.

This is a relevance hierarchy, not permission to accept every official marketing claim as experimental proof. When sources conflict, compare date, product, account tier, region, and interface. Record the conflict and choose the rule for the actual target. If a publisher page was inspected, describe it as bibliographic verification or further reading. Do not claim to have read the full book.

A concrete example is a description field described in characters by a publishing UI and bytes by its API. Explain the two contracts and the correct check for each. Do not average the limits or declare one source wrong without investigating its surface.

## Write procedures that support decisions

Keep the main workflow and consequential knowledge in `SKILL.md`. Describe what to inspect, why it matters, what decision follows, and how to verify the result. Replace “follow best practices” with an executable decision in prose, such as “query all active release tracks and pending allocations before reserving the next upload number.”

Use imperative steps for a genuine dependency sequence. Use decision tables for alternatives. Use examples to expose a difficult boundary, not to repeat the preceding sentence. Distinguish mandatory rules, owner preferences, and recommendations. Explain the consequence of ignoring a rule when that consequence is not obvious.

Include normal, invalid, incomplete, and interrupted workflows. State how to recognize a terminal error and when retrying could duplicate an external action. A skill must not invent successful work because a tool or source is unavailable.

Keep supporting language profiles and source notes focused. Required reading must stay within the package. The skill must remain understandable after independent installation. Use [the format contract](references/format.md), [the maintenance guide](references/authoring.md), and [the entrypoint template](assets/skill-template.md).

## Descriptive-content rule

Do not bundle counters, converters, scrapers, parsers, generated schema dumps, refresh jobs, or automatic maintenance. Explain the work and its checks in the skill. Only the user requests updates to this collection's facts. Consult sources and update the written knowledge when requested, without creating a self-updating mechanism.

If the user explicitly requests an automation script for a separate task, it must be Python run with uv. Declare the supported Python version and dependencies, preserve inputs, and document failure behavior. Native application languages and direct vendor CLI commands are not reasons to create wrapper scripts.

## Validate quality and format separately

Use the official `skills-ref validate` for naming and frontmatter. Inspect resource links and copyability. These checks cannot establish professional correctness.

Evaluate the written workflow against at least these scenarios:

- A normal request has sufficient inputs and should produce a concrete finished artifact.
- A decisive fact is missing, so the agent must ask a focused question without inventing it.
- A nearby request is outside scope and should not trigger unrelated work.
- A genuine boundary such as file size, authorization, regional availability, or page count changes the decision.
- A requested tool is unavailable, so the result must distinguish prepared work from unperformed execution.
- An update changes a rule, so its examples, template, usage guide, and affected references must agree.

Record observed outcomes only when the task was actually exercised. A tabletop review is useful but is not an independent model evaluation or a live platform test. Use delegation only when available and authorized.

## Improve skills from actual execution evidence

For a requested post-task improvement, inventory the skills actually used and map each difficulty to
missing procedure, wrong contract, capability boundary, evidence gap or execution mistake. Do not
label every failed click a skill defect or modify installed-but-unused packages just to increase scope.
Verify consequential commands against their exact resolved schemas/help, then add portable worked
sequences and interruption/recovery checks. Preserve useful existing guidance instead of repeating it.

Use [the execution-gap authoring procedure](references/authoring.md#turn-execution-gaps-into-portable-guidance)
for normal, missing-input, partial, failed, unavailable-tool and authorization scenarios. Keep facts
and examples coherent across entrypoints, references, templates and README prompts. Separate source
maintenance from installing copies or repeating live production operations. Report actual validation
and unresolved scope. No mechanical check proves a skill complete for every future environment.

## Delivery and foundations

Deliver the revised entrypoint, coherent supporting references, a usage example, source notes, and an honest verification report. Update current project architecture guidance. Preserve required licenses and remove superseded resources.

When the target repository maintains a skill catalog, per-skill guides, and ready-to-copy task
prompts, update their affected names, paths, inputs, outputs, and task-group coverage in the same
change. New groups need a usable prompt. Keep AGENTS.md a current instruction manual for architecture,
organization, commands, and rules. Do not append a history of the authoring task or make a portable
skill depend on collection-only documentation outside its package.

The [Agent Skills specification](https://agentskills.io/specification) defines interchange structure. Anthropic's [Agent Skills engineering article](https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills) explains progressive disclosure and procedural knowledge. [Google's code-review practice](https://google.github.io/eng-practices/review/reviewer/) supplies a useful inspection model for understanding a change before judging it. These support the design of this guide, not a guarantee that a particular prompt will perform reliably.

See [source notes](references/sources.md) for the evidence baseline and [the license](LICENSE.md) for distribution terms.
