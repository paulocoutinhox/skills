---
name: security-audit
description: Assess web/API, mobile and desktop security through trust boundaries, realistic abuse cases, authorization matrices and evidence-based findings. Use for requested security reviews, tenant isolation checks and concrete remediation verification.
license: MIT
---

# Security Audit

Assess whether realistic actors can cross the system's intended security boundaries. An audit is an evidence-based investigation, not a list of vulnerability names or a guarantee that a scanner found everything.

## Scope and threat model

Identify the reviewed revision, architecture, deployments, platforms, sensitive data, valuable operations, exposed interfaces, update/distribution path and permitted tests. Use harmless controlled fixtures. Do not perform destructive external tests, use third-party accounts without authorization, or print real secrets/customer records.

Map actors and assets. Include anonymous users, a normal user, another user in the same tenant, another tenant, low-role members, administrators, service integrations, compromised clients, malicious local processes and dependency suppliers as relevant. Identify which actor controls each input and where a trusted component makes the decision.

A UI running on a user's device is not a trusted authority for ownership, paid access, price or administrative rights. A signed binary does not make a client-supplied tenant ID authoritative.

## Select standards with the correct scope

Use OWASP ASVS 5.0.0 as the researched web verification baseline, API Security Top 10:2023 for API awareness, and current MASVS/MASTG/MASWE for mobile controls/testing. Top-ten lists summarize risk families and are not complete verification standards. The desktop awareness project has an older incubator baseline, so complement it with actual OS/runtime guidance.

For formal control mapping, cite exact requirement IDs from the selected version after reading them. Do not invent ASVS/MASVS identifiers from memory. Compliance claims require an explicit scope and evidence, not a passing source scan.

## Authorization and tenant isolation

Authenticate the caller, derive identity/tenant from trusted context, and authorize every object, operation and sensitive property. Scope the authoritative lookup or policy before returning data or mutating state. Child resources must belong to the authorized parent, not merely exist.

Opaque IDs can reduce casual enumeration, but a UUID or slug does not replace authorization. A slug is often discoverable. Do not put login/API tokens in resource URLs. Explicit share links are limited capabilities requiring randomness, narrow scope, expiry/revocation and leak-aware handling.

Test at least these paths with controlled owner/non-owner/other-tenant/anonymous/low-role identities:

| Path | Required evidence |
| --- | --- |
| List/search/count/facets | No unauthorized rows, counts, cursor or aggregate leakage |
| Detail/preview/file | Policy applies to the actual returned object/storage capability |
| Create/update/delete | Owner/tenant/role and writable properties cannot be impersonated |
| Batch/import/export | Every item is authorized, mixed-tenant payloads have defined behavior |
| Job/webhook/websocket | Trusted scope propagates, replay/old membership cannot leak data |
| Cache | Keys and invalidation include the relevant authorization dimensions |

A denied response must not occur after an unauthorized side effect. Test archived/deleted objects, alternate methods, aliases, stale sessions and revoked memberships where reachable.

## Web and API checks

Trace untrusted inputs to SQL/NoSQL queries, commands, templates, HTML, redirects, file paths, deserialization, XML and outbound requests. Use parameterization or typed allowlists for the actual sink. Escaping for HTML text does not automatically protect a JavaScript/URL context.

Review authentication and session rotation, password recovery, MFA, token issuer/audience/algorithm/expiry, revocation and one-time-token reuse. Decoding a JWT is not signature verification. Cookie-authenticated mutations need their appropriate CSRF defenses. CORS does not authenticate a non-browser caller.

Review uploads for content/size, archive traversal/decompression, active formats, storage isolation, safe names, download disposition and access. For SSRF, inspect schemes, destination policy, redirects, DNS resolution and private-network access. A URL regex alone does not establish a safe outbound request.

Bound expensive queries, payloads, pages, recursion, uploads, concurrent jobs and retries. Look for race-based duplicate fulfillment, overspending, uniqueness bypass and replayed refunds. Validate webhook authentication and raw-body requirements, then deduplicate and reconcile actual state.

Audit debug configuration, secrets, dependency/build trust, unsigned updates, error disclosure, sensitive logs, retention/deletion and actionable monitoring. Unhandled exceptional conditions can cause authorization to fail open or resources to remain allocated.

## Mobile and desktop checks

On mobile, inspect platform-backed secret storage, backups, logs/screenshots/clipboard, TLS validation, permissions, app links/intents, exported components, file providers and WebView/native bridges. A malicious client can inspect embedded secrets. Server authorization remains necessary.

On Apple targets, review Keychain accessibility/access groups, entitlements, transport exceptions, associated domains, extensions, snapshots and file protection. On Android, review exported flags, pending-intent mutability, URI grants, backup rules, cleartext/network settings and Activity/context lifetime.

On desktop, inspect privileged helpers, IPC sender/operation authorization, path/symlink races, temporary files, shell composition, DLL/plugin loading, writable execution paths, installer/update identity and local credential storage. In embedded browsers, restrict renderer capabilities and validate bridge origin, payload and operation. Do not expose a generic shell/filesystem bridge.

For native/FFI paths, inspect bounds, arithmetic, initialization, ownership, use-after-free, unsafe casts, shared state, lock order and callback reentrancy. Use relevant native diagnostics if the environment supports them. Launch success is not a proof of memory safety.

## Worked case and reporting

A report export job may pass the HTTP authorization test and still be unsafe if the queue stores an arbitrary client-supplied owner or the worker reads an unscoped object. Trace request → job → worker → storage → notification/download. Test another tenant's object, membership revocation before execution, repeated requests and a canceled job's late completion. The repair belongs at each authoritative boundary, not in a less predictable URL.

Report verified findings, plausible risks awaiting evidence and unavailable areas separately. Each finding needs location, actor/prerequisites, reachable flow, impact, evidence, remediation and retest. Prioritize impact and reachability. Do not inflate a hypothetical issue or hide residual limitations after fixes.

Use [procedure](references/procedure.md), [authorization](references/authorization.md), [web/API](references/web-api.md), [mobile](references/mobile.md), [desktop](references/desktop.md), [operations](references/operations.md) and [report template](assets/security-report.md) for focused detail.

Ross Anderson's [Security Engineering, third edition](https://www.cl.cam.ac.uk/archive/rja14/book.html) is professional further reading on adversaries, access control, protocols and system boundaries. The inspected author index identifies those chapters, not a claim that the whole book was read for this task. [ASVS](https://asvs.owasp.org/), [MASVS](https://mas.owasp.org/MASVS/) and [OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) supply applicable control/testing references. See [source notes](references/sources.md) and [license](LICENSE.md).

This descriptive skill does not create an audit engine, vulnerability scraper or scheduled scanner. Use existing authorized tools only when they answer a concrete assessment question.
