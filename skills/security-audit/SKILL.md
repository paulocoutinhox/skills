---
name: security-audit
description: Assess web/API, mobile and desktop security through trust boundaries, realistic abuse cases, authorization matrices and findings backed by evidence. Use for requested security reviews, tenant isolation checks and checking that concrete fixes work.
license: MIT
---

# Security Audit

Check whether realistic actors can cross the system's intended security boundaries. An audit is an investigation backed by evidence. It is not a list of vulnerability names or a promise that a scanner found everything.

The result is an assessment with guidance on how to fix the issues. Make fixes only when the user asks for them, then retest each fix with positive and negative evidence. Reviewing a single change belongs to code review. This skill covers a requested assessment of the system's trust boundaries, entrypoints and abuse cases.

## Scope and threat model

Name the reviewed revision, architecture, deployments, platforms, sensitive data, valuable operations, exposed interfaces, update and distribution path and the tests you are allowed to run. Use harmless test data that you control. Do not run destructive external tests, use third-party accounts without permission, or print real secrets or customer records.

Map actors and assets. Include anonymous users, a normal user, another user in the same tenant, another tenant, low-role members, administrators, service integrations, compromised clients, malicious local processes and dependency suppliers as relevant. Find which actor controls each input and where a trusted component makes the decision.

A UI running on a user's device is not a trusted source of truth for ownership, paid access, price or admin rights. A signed binary does not make a tenant ID sent by the client trustworthy.

## Select standards with the correct scope

Use OWASP ASVS 5.0.0 as the researched web verification base, OWASP Top 10:2025 for web awareness, API Security Top 10:2023 for API awareness, and current MASVS/MASTG/MASWE for mobile controls/testing. Top-ten lists sum up risk families and are not complete verification standards. The desktop awareness project is an incubator project, so pair it with current OS and runtime guidance.

For formal control mapping, cite exact requirement IDs from the chosen version after you read them. Do not invent ASVS/MASVS IDs from memory. A compliance claim needs a clear scope and evidence, not a passing source scan.

## Authorization and tenant isolation

Authenticate the caller, take identity and tenant from trusted context, and authorize every object, operation and sensitive property. Limit the source-of-truth lookup or policy to the right scope before you return data or change state. Child resources must belong to the authorized parent, not just exist.

Opaque IDs can make casual guessing of IDs harder, but a UUID or slug does not replace authorization. A slug is often easy to find. Do not put login or API tokens in resource URLs. Explicit share links are limited capabilities. They need randomness, narrow scope, expiry and revocation, and handling that expects leaks.

Test at least these paths with test identities you control: owner, non-owner, other tenant, anonymous and low role:

| Path | Required evidence |
| --- | --- |
| List/search/count/facets | No unauthorized rows, counts, cursor or aggregate leakage |
| Detail/preview/file | Policy applies to the real returned object or storage capability |
| Create/update/delete | Owner, tenant, role and writable properties cannot be faked |
| Batch/import/export | Every item is authorized, and mixed-tenant payloads have defined behavior |
| Job/webhook/websocket | Trusted scope carries through, and replay or old membership cannot leak data |
| Cache | Keys and invalidation include the relevant authorization dimensions |

A denied response must not come after an unauthorized side effect. Test archived and deleted objects, alternate methods, aliases, stale sessions and revoked memberships where reachable.

## Web and API checks

Trace untrusted inputs to SQL/NoSQL queries, commands, templates, HTML, redirects, file paths, deserialization, XML and outbound requests. Use parameterized queries or typed allowlists for the real sink (the place where input is used). Escaping for HTML text does not by itself protect a JavaScript or URL context.

Review authentication and session rotation, password recovery, MFA, token issuer, audience, algorithm and expiry, revocation and one-time-token reuse. Decoding a JWT is not signature verification. Changes made with cookie authentication need the right CSRF defenses. CORS does not authenticate a non-browser caller.

Review uploads for content and size, archive traversal and decompression, active formats, storage isolation, safe names, download disposition and access. For SSRF, check schemes, destination policy, redirects, DNS resolution and private-network access. A URL regex alone does not make an outbound request safe.

Limit costly queries, payloads, pages, recursion, uploads, concurrent jobs and retries. Look for races that cause duplicate fulfillment, overspending, bypassed uniqueness and replayed refunds. Validate webhook authentication and raw-body requirements, then remove duplicates and check the real state.

Audit debug configuration, secrets, dependency and build trust, unsigned updates, error disclosure, sensitive logs, retention and deletion and useful monitoring. Unhandled error conditions can make authorization fail open or leave resources allocated.

## Mobile and desktop checks

On mobile, check platform-backed secret storage, backups, logs, screenshots and clipboard, TLS validation, permissions, app links/intents, exported components, file providers and WebView/native bridges. A malicious client can read embedded secrets. Server authorization is still needed.

On Apple targets, review Keychain accessibility and access groups, entitlements, transport exceptions, associated domains, extensions, snapshots and file protection. On Android, review exported flags, pending-intent mutability, URI grants, backup rules, cleartext and network settings and Activity and context lifetime.

On desktop, check privileged helpers, IPC sender and operation authorization, path and symlink races, temporary files, shell command building, DLL and plugin loading, writable execution paths, installer and update identity and local credential storage. In embedded browsers, restrict renderer capabilities and validate the bridge origin, payload and operation. Do not expose a generic shell or filesystem bridge.

For native and FFI paths, check bounds, arithmetic, initialization, ownership, use-after-free, unsafe casts, shared state, lock order and callback reentrancy. Use relevant native diagnostics if the environment supports them. A successful launch does not prove memory safety.

## Worked case and reporting

A report export job may pass the HTTP authorization test and still be unsafe if the queue stores any owner the client sends or the worker reads an object without a scope check. Trace request → job → worker → storage → notification/download. Test another tenant's object, membership revocation before execution, repeated requests and a canceled job's late completion. The fix belongs at each source-of-truth boundary, not in a harder-to-guess URL.

Report verified findings, likely risks that still need evidence and areas you could not reach as separate groups. Each finding needs its location, actor and prerequisites, reachable flow, impact, evidence, fix and retest. Rank by impact and reachability.

Use four severity levels. Critical means demonstrated severe impact such as broad unauthorized access, destructive corruption or a reliably reachable catastrophic failure. High means a concrete significant security defect on an important path. Medium means a real defect under a specific supported condition with limited impact. Low means a concrete minor weakness or a clear requirement violation. Confidence is separate from severity, so an unconfirmed high-impact guess stays in the likely-risk section with the check that would confirm it. Do not overstate a guessed issue or hide remaining limits after fixes.

Use [procedure](references/procedure.md), [authorization](references/authorization.md), [web/API](references/web-api.md), [mobile](references/mobile.md), [desktop](references/desktop.md), [operations](references/operations.md) and [report template](assets/security-report.md) for focused detail.

Ross Anderson's [Security Engineering, third edition](https://www.cl.cam.ac.uk/archive/rja14/book.html) is professional further reading on adversaries, access control, protocols and system boundaries. The author index we checked names those chapters. This does not claim that the whole book was read for this task. [ASVS](https://asvs.owasp.org/), [MASVS](https://mas.owasp.org/MASVS/) and [OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) give control and testing references that apply. See [source notes](references/sources.md) and [license](LICENSE.md).

This descriptive skill does not create an audit engine, vulnerability scraper or scheduled scanner. Use existing approved tools only when they answer a concrete assessment question.
