# Findings and reporting

## Severity

| Level | Meaning |
| --- | --- |
| Critical | Demonstrated severe impact such as broad unauthorized access, destructive corruption, or a reliably reachable catastrophic failure. |
| High | A concrete significant correctness, security, or availability defect on an important path. |
| Medium | A real defect under a specific supported condition with limited but real impact. |
| Low | A concrete minor defect or a clear requirement violation, including formatter configuration that wraps single calls across lines. Do not present optional style suggestions as blockers. |

Severity follows impact, reachability, and prerequisites. Do not overstate a theoretical concern. Confidence is separate. A high-impact concern with missing evidence should state the uncertainty and the check needed to settle it.

## Finding structure

```text
[High] Reject another tenant's object before mutation — path/to/file:line

When a signed-in tenant-A user supplies a tenant-B object identifier, the update path loads it without tenant scope and changes its status. The detail route is scoped, but this separate mutation route is not. Add authorization to the authoritative lookup and cover the cross-tenant mutation with an integration test.

Evidence: exact caller/lookup/mutation path or minimal reproducer.
```

Use a short factual title, the real triggering condition, behavior that was observed or proven from source, the effect on users or the system, and a direction for the fix. Keep source locations precise and relevant. Do not write a whole replacement implementation in a review comment unless asked. Keep measured evidence, reasoning from reading code, assumptions, and open questions apart.

## Final review shape

Start with findings. If no defects worth acting on were found, say so. Then describe the reviewed revision and important affected paths, the checks you ran and their results, and the remaining coverage limits. Do not describe unrun tests as passed, infer complete security from scanner output, or claim all external consumers were checked when they were unavailable.

Keep the report short enough to act on. Group one root cause into one finding. Put optional, non-blocking suggestions after real defects and label them as suggestions. Source attribution belongs in research notes where useful, not in a Git commit message or an invented co-author trailer.
