# Findings and reporting

## Severity

| Level | Meaning |
| --- | --- |
| Critical | Demonstrated severe impact such as broad unauthorized access, destructive corruption, or a reliably reachable catastrophic failure. |
| High | A concrete significant correctness, security, or availability defect on an important path. |
| Medium | A real defect under a specific supported condition with bounded but meaningful impact. |
| Low | A concrete minor defect or explicit requirement violation. Avoid presenting optional style suggestions as blockers. |

Severity follows impact, reachability, and prerequisites. Do not inflate a theoretical concern. Confidence is separate: a high-impact concern with missing evidence should state the uncertainty and the check needed to resolve it.

## Finding structure

```text
[High] Reject another tenant's object before mutation — path/to/file:line

When a signed-in tenant-A user supplies a tenant-B object identifier, the update path loads it without tenant scope and changes its status. The detail route is scoped, but this separate mutation route is not. Add authorization to the authoritative lookup and cover the cross-tenant mutation with an integration test.

Evidence: exact caller/lookup/mutation path or minimal reproducer.
```

Use a short factual title, the actual triggering condition, observed or source-proven behavior, affected user/system outcome, and a corrective direction. Keep source locations precise and relevant. Do not write an entire replacement implementation in a review comment unless requested. Distinguish measured evidence, static reasoning, assumptions, and unanswered questions.

## Final review shape

Lead with findings. State that no actionable defects were found if that is the actual result. Then describe the reviewed revision and important affected paths, checks executed and results, and remaining coverage limits. Do not describe unrun tests as passed, infer complete security from scanner output, or claim all external consumers were checked when they were unavailable.

Keep the report concise enough to act on. Group one root cause into one finding. Place optional nonblocking suggestions after real defects and label them as suggestions. Source attribution belongs in research notes where useful, not in a Git commit message or an invented co-author trailer.
