# Web and API security catalog

The following checklist combines current awareness categories and concrete engineering checks. It is not a claim to enumerate every possible vulnerability.

## Web risk families

| Risk | Inspect and verify |
| --- | --- |
| Broken access control | Object/function/property authorization, tenant isolation, file access, admin routes, CORS assumptions, cache scope. |
| Security misconfiguration | Debug endpoints, default credentials, exposed services, insecure headers, permissive origins, directory listing, verbose errors, public buckets. |
| Software supply chain failures | Untrusted actions, compromised build inputs, dependency confusion, unsigned updates, unreviewed install scripts, provenance and lockfile integrity. |
| Cryptographic failures | Secrets storage, obsolete algorithms, weak randomness, key reuse, incorrect encryption mode, missing authentication, transport protection. |
| Injection | SQL/NoSQL/LDAP/template/OS commands, expression engines, unsafe deserialization, XSS, XML entity expansion, unsafe query composition. |
| Insecure design | Missing threat boundaries, trusting prices or ownership from clients, unlimited business flows, abuse-prone reset/recovery and sharing design. |
| Authentication failures | Session fixation, token validation, MFA and recovery gaps, credential stuffing, enumeration, reset replay, broken logout/revocation. |
| Software/data integrity failures | Unsigned payloads/updates, unsafe serialized objects, webhook forgery, unverified artifact transfer, replayable state changes. |
| Logging and alerting failures | Missing security events, secret/PII logging, log injection, absent actionable alerts, overexposed logs. |
| Mishandled exceptional conditions | Fail-open authorization, ignored errors, partial transactions, timeout leaks, resource exhaustion and unsafe default state. |

## API-specific checks

Cover object-level authorization, authentication, property-level authorization, resource consumption, function-level authorization, abuse of sensitive business flows, SSRF, misconfiguration, inventory, and unsafe consumption of upstream APIs. Track all active routes, legacy exposed deployments, debug versions, and deprecated endpoints that remain reachable.

Bound page size, body size, uploads, decompression, query complexity, recursion, concurrency, timeouts, and expensive jobs. Rate-limit according to identity and business risk, not just a spoofable header. Validate upstream responses and failures rather than trusting them as internal data. For outbound fetches, constrain schemes and destinations, resolve DNS carefully, and address redirect and private-network access paths.

## Daily implementation checks

- Parameterize queries. Do not construct SQL, shell commands, templates, or expression fragments with untrusted strings. Use typed allowlists for dynamic identifiers where needed.
- Encode output for its exact context. Review stored and reflected XSS, unsafe HTML sinks, template escape bypasses, script URLs, and content uploaded as active HTML/SVG.
- Protect cookie-authenticated state changes against CSRF. Apply secure, HttpOnly, and appropriate SameSite settings. Check login CSRF and session rotation. CORS does not authenticate callers or protect non-browser clients.
- Verify tokens with the intended algorithm, issuer, audience, expiry, key, and applicable replay/revocation semantics. Do not trust an unsigned or merely decoded JWT.
- Use appropriate adaptive password hashing and controlled recovery flows. Avoid leaking whether an account exists where the product requires nondisclosure. Bound login/reset attempts and invalidate one-time tokens.
- Validate file type using real content where required, cap size, isolate storage, generate safe names, prevent traversal and archive extraction escape, and serve downloads with appropriate disposition/content type. Scan risky formats when the threat model warrants it.
- Authenticate webhooks through the provider's actual configured mechanism. Verify signatures and delivery-time tolerances when supported, preserving raw bytes if that contract requires them. A configured authorization header needs its own validation. Do not invent unsupported signature headers or accept failed verification through another mode. Deduplicate and reconcile retries independently.
- Validate redirects, return URLs, embedded frames, and external navigation. Review clickjacking controls and content security policy appropriate to the application.
- Use transactions and constraints for balances, inventory, entitlements, uniqueness, and ownership. Protect against duplicate checkout, race-based limit bypass, and replayed refunds.
- Ensure deletion, retention, backups, exports, and subject-access paths obey the product's actual privacy rules. Do not expose private data through analytics or exception telemetry.

For a particular finding, inspect the applicable detailed verification requirement and framework documentation. Top-ten awareness lists alone are not a complete verification standard.
