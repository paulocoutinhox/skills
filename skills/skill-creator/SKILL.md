---
name: skill-creator
description: Research, write, and revise descriptive Agent Skills with precise procedures, evidence, examples, standard metadata, and quality criteria you can check. Use when creating a SKILL.md or improving the professional depth of an existing skill.
license: MIT
---

# Skill Creator

Write a working guide that passes on professional judgment. The result is knowledge another agent can apply. It is not a persona, a list of slogans, a set of scripts, or an instruction to research the subject from scratch later.

## Establish the task contract

Find the user's goal, the files or content they expect, the target environment, and what counts as finished. Read the available project context before you ask questions. Tell a missing preference, which can use a stated default, apart from a missing fact, which would make the result false or unusable.

Write down these decisions before drafting:

| Decision | Required detail |
| --- | --- |
| Activation | Real requests that should select the skill, plus adjacent requests that should not |
| Inputs | Which facts come from the user, project, source material, or current service account |
| Output | Files or content, format, intended audience, and the evidence that it is accepted |
| Modes | Real alternatives such as print/digital or preparation/publication |
| Boundaries | Real permissions, unavailable tools, legal facts, and unsupported capabilities |
| Failure | How to explain an unresolved input while completing independent work |

For example, “make a professional book” is not enough. A useful contract states the trim, delivery mode, manuscript language, editorial standard, front matter, navigation, paper and binding, ISBN status, and the real production template. It does not invent missing print dimensions.

## Research before prescribing

Use the source that controls the exact operation. A product's API schema controls fields, its policy guide controls approval, and an editorial book can explain communication or composition. None of them replaces the others.

For each important claim, record the URL, the material you checked, the date, the version or surface it applies to, the decision it supports, and the uncertainty. A source note should explain what the evidence changed in the procedure. Do not add impressive book titles without tying them to a decision.

Prefer this evidence order for technical requirements:

1. Applicable specification, official API contract, standard, or tool behavior.
2. Maintainer guidance and a relevant implementation or example.
3. Original research with real data for claims about how well something works.
4. Professional books and named practitioners for reasoning frameworks.
5. Secondhand summaries when the original is not available, with that limit stated.

This order ranks how relevant a source is. It does not let you accept every official marketing claim as proof from experiments. When sources disagree, compare the date, product, account tier, region, and interface. Record the conflict and choose the rule for the real target. If you checked a publisher page, describe it as a bibliographic check or further reading. Do not claim to have read the full book.

A concrete example is a description field that a publishing UI measures in characters and its API measures in bytes. Explain the two contracts and the correct check for each. Do not average the limits, and do not call one source wrong without checking its surface.

## Write procedures that support decisions

Keep the main workflow and important knowledge in `SKILL.md`. Describe what to check, why it matters, what decision follows, and how to verify the result. Replace “follow best practices” with a decision the agent can act on, written in prose, such as “query all active release tracks and pending allocations before reserving the next upload number.”

Use direct steps when each step really depends on the one before. Use decision tables for alternatives. Use examples to show a hard boundary, not to repeat the sentence before them. Keep required rules, owner preferences, and recommendations apart. Explain what happens if someone ignores a rule when that result is not obvious.

Include normal, invalid, incomplete, and interrupted workflows. State how to recognize an error that ends the task, and when a retry could repeat an external action. A skill must not invent successful work because a tool or source is unavailable.

When the skill produces finished user-facing content, such as a post, image, document or message, require the output to read as natural content. It must not narrate how it was produced or mention AI, agents, tools or prompts unless the user asks for that. When a platform policy requires an AI or synthetic-content disclosure, direct it to the platform's own disclosure setting or label, not into the copy.

Keep each function or method call in a code example on one line instead of wrapping its arguments across continuation lines, and add named intermediate variables for complex arguments. Do not split one string literal into adjacent literals across lines.

Keep supporting language profiles and source notes focused. Required reading must stay inside the package. The skill must still make sense when it is installed on its own. Use [the format contract](references/format.md), [the maintenance guide](references/authoring.md), and [the entrypoint template](assets/skill-template.md).

## Descriptive-content rule

Do not bundle counters, converters, scrapers, parsers, generated schema dumps, refresh jobs, or automatic maintenance. Explain the work and its checks in the skill. Only the user asks for updates to this collection's facts. Read sources and update the written knowledge when asked, without creating a self-updating process.

If the user clearly asks for an automation script for a separate task, it must be Python run with uv. Declare the supported Python version and dependencies, keep inputs intact, and document what happens on failure. Native application languages and direct vendor CLI commands are not reasons to create wrapper scripts.

## Validate quality and format separately

Use the official `skills-ref validate` for naming and frontmatter. Check resource links and that the package works when copied. These checks cannot prove that the content is professionally correct.

Test the written workflow against at least these scenarios:

- A normal request has enough inputs and should produce a concrete finished result.
- A key fact is missing, so the agent must ask a focused question without inventing it.
- A nearby request is outside scope and should not trigger unrelated work.
- A real boundary such as file size, authorization, regional availability, or page count changes the decision.
- A requested tool is unavailable, so the result must distinguish prepared work from unperformed execution.
- An update changes a rule, so its examples, templates, affected references and any catalog or prompt documentation must agree.

Record observed results only when the task was really run. A desk review on paper is useful, but it is not an independent model evaluation or a live platform test. Hand work to other agents only when that is available and allowed.

## Improve skills from real run evidence

For a requested improvement after a task, list the skills that were really used. Map each problem to
a missing procedure, wrong contract, capability boundary, evidence gap or execution mistake. Do not
call every failed click a skill defect, or change installed but unused packages just to widen the
scope. Check important commands against their exact resolved schemas or help, then add portable
worked sequences and checks for interruption and recovery. Keep useful existing guidance instead of
repeating it.

Use [the execution-gap authoring procedure](references/authoring.md#turn-execution-gaps-into-portable-guidance)
for normal, missing-input, partial, failed, unavailable-tool and authorization scenarios. Keep facts
and examples consistent across entrypoints, references, templates and task prompts. Keep source
maintenance apart from installing copies or repeating live production operations. Report the checks
you really ran and the open scope. No mechanical check proves a skill complete for every future
environment.

## Delivery and foundations

Write in plain, easy English with short sentences and the common, everyday term for each thing. Avoid jargon, rare words and invented labels when a common word works. Keep a precise technical term only when it is the name people actually use, such as an API field, a command or a standard, and explain it in plain words when a reader may not know it.

Deliver the revised entrypoint, consistent supporting references, a task prompt example, source notes, and an honest verification report. Update the current project architecture guidance. Keep required licenses and remove resources that were replaced. Describe only current formats, versions and procedures. Do not add conversion or migration procedures, compatibility rules, old-format detection, fallback handling or before/after explanations, whether for an earlier form of the skill or for older versions, deprecated APIs or retired services of the products it covers. Direct the agent to the current supported version, API or service. Moving a project to a newer revision through fresh references and careful merges is current maintenance.

When the target repository maintains a skill catalog and ready-to-copy task prompts, update their
affected names, paths, inputs, outputs, and task-group coverage in the same change. New groups need
a usable prompt. Keep AGENTS.md a current instruction manual for architecture, layout,
commands, and rules. Do not append a history of the authoring task or make a portable skill depend
on collection-only documentation outside its package.

The [Agent Skills specification](https://agentskills.io/specification) defines the shared file structure. Anthropic's [Agent Skills engineering article](https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills) explains progressive disclosure (loading detail only when needed) and procedural knowledge. [Google's code-review practice](https://google.github.io/eng-practices/review/reviewer/) gives a useful model for understanding a change before judging it. These support the design of this guide. They do not promise that a given prompt will work reliably.

See [source notes](references/sources.md) for the evidence base and [the license](LICENSE.md) for distribution terms.
