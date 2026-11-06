# Authoring and maintenance

## Discovery

Collect a representative request and the output a user would accept. Identify which inputs can come from repository context and which need questions. Describe explicit assumptions. Exclude adjacent capabilities when otherwise likely to trigger incorrectly. A thumbnail skill creates an image. It should not publish a social campaign just because both involve social media.

## Research record

For each consequential external rule, keep a primary source URL, access date, applicable mode or version, and the decision it supports. Record inaccessible material as inaccessible. When sources disagree, prefer the source for the exact target surface or account and disclose the conflict. Do not turn a recommendation into an official requirement. Do not reproduce paid or copyrighted standards in full.

## Instruction design

Lead with the outcome. Route by the user's selected mode. Describe required inputs, meaningful defaults, validation, failure handling, output names, and completion checks. Prefer action verbs and concrete acceptance conditions over persona claims. Explain when to read a reference. Do not load every language or platform manual for a narrow task.

Keep numeric rules, export limits, calculations and verification decisions descriptive. Use worked examples and the actual native tool/interface, rather than bundling scripts or generated datasets. Only when the user explicitly requests separate automation should a Python/uv script be created, with real input/output/error behavior and relevant tests.

Templates must be usable starting points. Clearly mark values the user needs to supply, and make the workflow replace them before release. Do not publish unresolved template tokens as a finished implementation. Keep executable examples safe to inspect without contacting production systems.

## Evaluation

| Scenario | Observable acceptance |
| --- | --- |
| Normal task | Produces the requested artifact with correct structure and mode. |
| Missing decisive input | Asks a focused question and continues independent work when useful. |
| Out-of-scope request | Does not apply unrelated procedures or mutate unrelated files. |
| Boundary | Handles exact size, page, character, permission, or path boundaries. |
| Missing dependency | Names the missing dependency and does not fabricate execution. |
| Failure | Returns actionable diagnostics and preserves existing user artifacts. |
| Update | Preserves relevant resources and replaces superseded instructions. |

Use independent evaluation only when available and authorized. Never make delegation a mandatory capability of a portable skill. Keep fixture files temporary and avoid live publication during evaluations.

## Maintenance

Change the source of truth once, then update routes, templates, documentation, and checks that depend on it. Remove broken links and unused files. Revalidate every affected skill. Keep architecture guidance current rather than appending a change diary. Avoid adding permanent global rules for isolated failures that a narrow correction can solve.

Only the user initiates content maintenance in this repository. Research the requested change and edit the written guidance. Do not create scheduled jobs, scrapers, automatic data collection, schema generators or self-updating mechanisms. CI validates the committed collection without refreshing facts.

## Turn execution gaps into portable guidance

When a user asks to improve skills after a real task, inventory which packages were actually read
or applied. Distinguish installed-but-unused skills, system packages outside the target collection,
and neighboring capabilities selected for a justified gap. State the resulting scope. Do not modify
every package just because it is installed or claim a package was used when only its name was seen.

Map each observed friction point before drafting:

| Observation | Classify | Useful change |
| --- | --- | --- |
| Missing dependency sequence | Procedure gap | Ordered native operations, IDs carried forward and success checks |
| Incorrect flag/method or output assumption | Contract defect | Exact inspected version/schema and a corrected example |
| Unsupported endpoint or service | Capability boundary | Supported alternative, exact handoff and unperformed state |
| Credential/role conflict | Authorization or environment | Distinct capabilities, safe diagnosis and scope-preserving repair |
| Failed input/focus/validation | Execution mistake or UI condition | Diagnose only if the lesson generalizes. Do not blame absent docs automatically |
| Locally successful preparation reported as release | Evidence gap | Explicit distinction between configured, tested, submitted, approved and available |
| Repeated retries or interrupted creates | Recovery gap | Reconciliation by returned IDs before repeating an external action |

Read the whole affected workflow before appending a workaround. A topic already covered may need a
worked sequence or clearer routing, not a duplicate checklist. Do not fill a skill with project names,
user paths, credential values, device UDIDs, sample prices or coordinates from one successful task.
Use a fictitious worked example and identify version-specific observations as such.

For a consequential command, inspect native help/schema or maintainer source. Verify that the schema
resolved to the intended path and that request/update/response models differ where relevant. Some
CLIs return a parent schema for an unknown child or wrap ordinary output differently from a raw API.
An exit code alone does not prove the guessed operation exists. Match method, arguments, environment,
required fields and actual response shape. Preserve uncertainty when the surface is inaccessible.

Write the end-to-end dependency sequence once in the owning skill, then route substantial specialized
steps to focused references. Include a normal case, absent decisive input, partial/interrupted run,
permission/state failure, unavailable tool and scope boundary. State both the expected next action and
the evidence that changes its status. Avoid external mutations just to demonstrate documentation.

Keep installation/version discovery distinct from permission to update a user's installed copies.
Deliver source changes, coherent references/templates and updated README prompts. Run format/link
checks and manual scenario review. Report those separately from actual domain execution and remote
CI. 'No gaps' is an improvement objective, not proof of exhaustive correctness for every account,
platform version or future provider behavior. Name material unresolved limits instead of certifying
an untested universal workflow.
