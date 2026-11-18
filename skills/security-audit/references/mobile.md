# Mobile security catalog

Use the current MASVS control families with the actual mobile platform and backend architecture. A mobile binary can be inspected or modified by an adversary. Do not store a privileged shared backend secret in the app and assume obfuscation protects it.

| Family | Concrete checks |
| --- | --- |
| Storage | Keychain/Keystore-backed secrets, local database protection where needed, file permissions, screenshots, clipboard, keyboard caches, logs, backups, logout cleanup. |
| Cryptography | Platform primitives, key generation and lifecycle, authenticated encryption, nonces, no hard-coded shared keys, suitable random sources. |
| Authentication | Server enforcement, session expiry/revocation, biometric authorization bound to a protected operation, secure recovery, no client-only premium/admin decisions. |
| Network | TLS and certificate validation, no “accept all” trust handlers, cleartext restrictions, endpoint validation, credential redaction, scoped downloads. |
| Platform interaction | Exported components, intents, URL schemes, app links, WebViews, permissions, interprocess calls, share extensions, file providers. |
| Code quality | Safe deserialization, dependency versions, memory/FFI boundaries, resource limits, cancellation, update and signing integrity. |
| Resilience | Tamper and reverse-engineering resistance appropriate to risk, signed distribution, integrity signals where justified, no security based solely on root/jailbreak detection. |
| Privacy | Data minimization, permission purpose, analytics/SDK behavior, consent where applicable, retention/deletion, background collection, accessibility of sensitive content. |

## Android

Inspect manifest exported flags, intent filters, pending-intent mutability, content providers, URI grants, file providers, backup rules, debuggable status, network-security configuration, and runtime permissions. Validate all data from intents and deep links. Do not grant broad file access merely to make sharing work.

Review WebView JavaScript bridges, allowed navigation, file access, mixed content, and remote content. Keep authentication in supported secure flows. Store sensitive key material with the platform keystore capabilities required by the threat model. Do not retain Activity contexts, screen contents, or token-bearing objects after their intended lifetime.

## Apple platforms

Inspect Keychain accessibility, access groups, entitlements, app transport security exceptions, universal/custom links, pasteboard handling, backup exclusions, file protection, extensions, WebKit message bridges, and release signing. Validate associated domains and incoming URLs. Review background tasks and snapshots for private data exposure.

## Verification

Test offline and restored sessions, logout, account switching, revoked memberships, background transitions, process recreation, and local backup/restore where relevant. Capture controlled traffic in an authorized test environment to verify transport behavior. A client that hides another user's document still fails if the backend returns that document when its identifier is supplied.

Certificate pinning, hardware-backed keys, integrity APIs, and anti-tamper measures require explicit lifecycle and recovery plans. They are risk-based controls, not automatic requirements for every app. Pinning without rotation planning can create an availability failure.
