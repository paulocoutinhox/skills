# Web and API security catalog

This checklist combines current awareness categories with concrete engineering checks. It does not claim to list every possible vulnerability.

## Web risk families

| Risk | Check and verify |
| --- | --- |
| Broken access control | Object/function/property authorization, tenant isolation, file access, admin routes, CORS assumptions, cache scope. |
| Security misconfiguration | Debug endpoints, default credentials, exposed services, insecure headers, permissive origins, directory listing, verbose errors, public buckets. |
| Software supply chain failures | Untrusted actions, compromised build inputs, dependency confusion, unsigned updates, unreviewed install scripts, provenance and lockfile integrity. |
| Cryptographic failures | Secrets storage, outdated algorithms, weak randomness, key reuse, incorrect encryption mode, missing authentication, transport protection. |
| Injection | SQL/NoSQL/LDAP/template/OS commands, expression engines, unsafe deserialization, XSS, XML entity expansion, unsafe query composition. |
| Insecure design | Missing threat boundaries, trusting prices or ownership from clients, unlimited business flows, abuse-prone reset/recovery and sharing design. |
| Authentication failures | Session fixation, token validation, MFA and recovery gaps, credential stuffing, enumeration, reset replay, broken logout/revocation. |
| Software/data integrity failures | Unsigned payloads/updates, unsafe serialized objects, webhook forgery, unverified artifact transfer, replayable state changes. |
| Logging and alerting failures | Missing security events, secret/PII logging, log injection, missing useful alerts, logs shown to too many people. |
| Mishandled exceptional conditions | Fail-open authorization, ignored errors, partial transactions, timeout leaks, resource exhaustion and unsafe default state. |

## API-specific checks

Cover object-level authorization, authentication, property-level authorization, resource consumption, function-level authorization, abuse of sensitive business flows, SSRF, misconfiguration, inventory, and unsafe consumption of upstream APIs. Track all active routes, old deployments that are still exposed, debug versions, and deprecated endpoints that can still be reached.

Limit page size, body size, uploads, decompression, query complexity, recursion, concurrency, timeouts, and costly jobs. Rate-limit by identity and business risk, not just by a header that can be faked. Validate upstream responses and failures instead of trusting them as internal data. For outbound fetches, limit schemes and destinations, resolve DNS carefully, and handle redirect and private-network access paths.

## Daily implementation checks

- Parameterize queries. Do not construct SQL, shell commands, templates, or expression fragments with untrusted strings. Use typed allowlists for dynamic identifiers where needed.
- Encode output for its exact context. Review stored and reflected XSS, unsafe HTML sinks, template escape bypasses, script URLs, and content uploaded as active HTML/SVG.
- Protect cookie-authenticated state changes against CSRF. Apply secure, HttpOnly, and fitting SameSite settings. Check login CSRF and session rotation. CORS does not authenticate callers or protect non-browser clients.
- Verify tokens with the intended algorithm, issuer, audience, expiry, key, and the replay and revocation rules that apply. Do not trust an unsigned JWT or one that was only decoded.
- Use fitting adaptive password hashing and controlled recovery flows. Do not leak whether an account exists where the product requires that to stay hidden. Limit login and reset attempts, and invalidate one-time tokens.
- Validate file type from the real content where required, cap size, isolate storage, generate safe names, prevent traversal and archive extraction escape, and serve downloads with the right disposition and content type. Scan risky formats when the threat model calls for it.
- Authenticate webhooks through the provider's real configured method. Verify signatures and delivery-time tolerances when supported, and keep the raw bytes if that contract requires them. A configured authorization header needs its own validation. Do not invent unsupported signature headers, and do not accept a failed verification through another mode. Remove duplicate retries and check their real result on their own.
- Validate redirects, return URLs, embedded frames, and external navigation. Review clickjacking controls and a content security policy that fits the application.
- Use transactions and constraints for balances, inventory, entitlements, uniqueness, and ownership. Protect against duplicate checkout, race-based limit bypass, and replayed refunds.
- Make sure deletion, retention, backups, exports, and subject-access paths follow the product's real privacy rules. Do not expose private data through analytics or exception telemetry.

For a specific finding, read the detailed verification requirement and framework documentation that apply. Top-ten awareness lists alone are not a complete verification standard.
