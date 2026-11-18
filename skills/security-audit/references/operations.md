# Dependencies, delivery, and runtime security

## Secrets and supply chain

Review manifests, lockfiles, registry configuration, dependency ownership, install scripts, transitive packages, native plugins, and update policy. Investigate dependency confusion, typosquatting, unpinned remote build scripts, unexpected binary downloads, and unsafe code generation. Record reachable vulnerable usage rather than treating every advisory as identical risk.

Keep credentials out of source, logs, examples, crash reports, screenshots, artifacts, images, and frontend bundles. Ignore local secret files, but also inspect tracked paths and prior exposure when in scope. Use a redacting scanner and avoid displaying secret values. Rotation, revocation, and history remediation are distinct actions.

## CI and publication

Use minimal workflow permissions and inspected immutable action references. Keep untrusted PR execution away from privileged contexts and secrets. Review `pull_request_target`, workflow-dispatch parameters, cache poisoning, artifact substitution, shell injection, and automatic execution from issue/comment text. Treat names, bodies, branches, filenames, and logs as untrusted data.

Use registry OIDC trusted publication where supported. Limit the identity to the exact repository, workflow, and environment. Give OIDC write capability only to the publish job. Build and test first, then publish the same verified artifact. Inspect release tags, manifest/version agreement, provenance, package contents, and signing key handling.

## Runtime and infrastructure

Review service identity, cloud permissions, public storage, database/network exposure, tenant partitioning, TLS configuration, backup access, encryption key lifecycle, environment injection, and administrator interfaces. Apply bounded retries, timeouts, quotas, request size limits, and safe degradation. Authorization failures must never become success through a fallback.

Check monitoring for authentication abuse, authorization denial patterns, privileged changes, data exports, sensitive configuration changes, and failed integrity checks. Keep audit events attributable and tamper-resistant as appropriate, with privacy-aware retention. Logs must not become a second unauthorized database.

## Business and data flows

Reconcile payments, entitlements, inventory, resource ownership, account deletion, recovery, sharing, notifications, and integration callbacks. Verify idempotency under replay and concurrency. Validate amounts, currency, actor, resource, and transition on the authoritative server. An opaque URL does not prevent a cross-account charge, export, or entitlement mutation.

Review environment-specific exposure. Local development defaults do not justify production debug settings. Conversely, do not create irrelevant production infrastructure requirements for a local-only tool. Apply controls to the system actually being assessed.
