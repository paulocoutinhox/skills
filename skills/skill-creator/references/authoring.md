# Authoring and maintenance

## Discovery

Collect a typical request and the output a user would accept. Find which inputs can come from repository context and which need questions. State your assumptions clearly. Leave out nearby capabilities when they would otherwise trigger by mistake. A thumbnail skill creates an image. It should not publish a social campaign just because both involve social media.

## Research record

For each important external rule, keep an original source URL, the access date, the mode or version it applies to, and the decision it supports. Record material you could not reach as not reachable. When sources disagree, prefer the source for the exact target surface or account and state the conflict. Do not turn a recommendation into an official requirement. Do not copy paid or copyrighted standards in full.

## Instruction design

Write plain, easy English with short sentences and the common, everyday term for each thing. Avoid jargon, rare words and invented labels when a common word works. Keep a precise technical term only when it is the name people actually use, such as an API field, a command or a standard, and explain it in plain words when a reader may not know it.

Start with the outcome. Branch by the mode the user chose. Describe required inputs, useful defaults, validation, failure handling, output names, and completion checks. Prefer action verbs and concrete acceptance conditions over persona claims. Explain when to read a reference. Do not load every language or platform manual for a narrow task.

Keep number rules, export limits, calculations and verification decisions in prose. Use worked examples and the real native tool or interface instead of bundling scripts or generated datasets. Create a Python/uv script only when the user clearly asks for separate automation, with real input, output and error behavior and relevant tests.

Keep each function or method call in a code example on one line, and use named intermediate variables for complex arguments instead of wrapping arguments across continuation lines. Finished user-facing content produced by a skill must read naturally, without narrating its production or mentioning AI, agents, tools or prompts unless the user asks. A required platform disclosure goes in that platform's own disclosure setting.

Templates must be usable starting points. Clearly mark the values the user needs to supply, and make the workflow replace them before release. Do not publish unfilled template tokens as a finished result. Keep runnable examples safe to read without contacting production systems.

## Evaluation

| Scenario | Observable acceptance |
| --- | --- |
| Normal task | Produces the requested result with correct structure and mode. |
| Missing decisive input | Asks a focused question and goes on with independent work when useful. |
| Out-of-scope request | Does not apply unrelated procedures or change unrelated files. |
| Boundary | Handles exact size, page, character, permission, or path boundaries. |
| Missing dependency | Names the missing dependency and does not fake a run. |
| Failure | Returns useful diagnostics and keeps existing user files. |
| Update | Keeps relevant resources and replaces outdated instructions. |

Use independent evaluation only when it is available and allowed. Never make handing work to other agents a required capability of a portable skill. Keep test files temporary, and do not publish anything live during evaluations.

## Maintenance

Change the source of truth once, then update the links, templates, documentation, and checks that depend on it. Remove broken links and unused files. Validate every affected skill again. Keep architecture guidance current instead of adding a change diary. Describe only current formats, versions and procedures, with no migration, compatibility, fallback or before/after guidance for earlier forms of a skill or for older product versions, deprecated APIs or retired services. Do not add permanent global rules for one-off failures that a narrow fix can solve.

Only the user starts content maintenance in this repository. Research the requested change and edit the written guidance. Do not create scheduled jobs, scrapers, automatic data collection, schema generators or self-updating processes. CI validates the committed collection without refreshing facts.

## Turn execution gaps into portable guidance

When a user asks to improve skills after a real task, list which packages were really read or
applied. Tell apart skills that are installed but unused, system packages outside the target
collection, and nearby capabilities chosen for a real gap. State the scope that results. Do not
change every package just because it is installed, or claim a package was used when only its name
was seen.

Map each problem you saw before drafting:

| Observation | Classify | Useful change |
| --- | --- | --- |
| Missing dependency sequence | Procedure gap | Ordered native operations, IDs carried forward and success checks |
| Incorrect flag/method or output assumption | Contract defect | Exact checked version/schema and a corrected example |
| Unsupported endpoint or service | Capability boundary | Supported alternative, exact handoff and the state of work not done |
| Credential/role conflict | Authorization or environment | Separate capabilities, safe diagnosis and a fix that keeps the scope |
| Failed input/focus/validation | Execution mistake or UI condition | Diagnose only if the lesson applies more widely. Do not blame missing docs by default |
| Locally successful preparation reported as release | Evidence gap | Clear difference between configured, tested, submitted, approved and available |
| Repeated retries or interrupted creates | Recovery gap | Check the real state by returned IDs before repeating an external action |

Read the whole affected workflow before you add a workaround. A topic already covered may need a
worked sequence or clearer links, not a second checklist. Do not fill a skill with project names,
user paths, credential values, device UDIDs, sample prices or coordinates from one successful task.
Use a made-up worked example, and mark version-specific observations as such.

For an important command, read the native help or schema or the maintainer source. Check that the
schema resolved to the intended path and that request, update and response models differ where
relevant. Some CLIs return a parent schema for an unknown child or wrap ordinary output differently
from a raw API. An exit code alone does not prove the guessed operation exists. Match the method,
arguments, environment, required fields and real response shape. Keep the uncertainty when you
cannot reach the surface.

Write the end-to-end dependency sequence once in the skill that owns it, then move large specialized
steps to focused references. Include a normal case, a missing key input, a partial or interrupted
run, a permission or state failure, an unavailable tool and a scope boundary. State both the
expected next action and the evidence that changes its status. Do not make external changes just to
show the documentation works.

Finding installed copies and versions is not permission to update a user's installed copies. Deliver
source changes, consistent references and templates and updated task prompts. Run format and link
checks and a manual scenario review. Report those separately from real domain execution and remote
CI. 'No gaps' is a goal for improvement, not proof that the skill is correct for every account,
platform version or future provider behavior. Name important open limits instead of certifying an
untested universal workflow.
