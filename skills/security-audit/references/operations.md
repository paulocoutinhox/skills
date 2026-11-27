# Dependencies, delivery, and runtime security

## Secrets and supply chain

Review manifests, lockfiles, registry configuration, dependency ownership, install scripts, transitive packages, native plugins, and update policy. Investigate dependency confusion, typosquatting, unpinned remote build scripts, unexpected binary downloads, and unsafe code generation. Record vulnerable code that can really be reached, instead of treating every advisory as the same risk.

Keep credentials out of source, logs, examples, crash reports, screenshots, artifacts, images, and frontend bundles. Ignore local secret files, but also check tracked paths and earlier exposure when in scope. Use a redacting scanner and do not show secret values. Rotation, revocation, and cleaning up history are separate actions.

## CI and publication

Use minimal workflow permissions and reviewed, immutable action references. Keep untrusted PR execution away from privileged contexts and secrets. Review `pull_request_target`, workflow-dispatch parameters, cache poisoning, artifact substitution, shell injection, and automatic execution from issue/comment text. Treat names, bodies, branches, filenames, and logs as untrusted data.

Use registry OIDC trusted publication where supported. Limit the identity to the exact repository, workflow, and environment. Give OIDC write capability only to the publish job. Build and test first, then publish the same verified artifact. Check release tags, that manifest and version match, provenance, package contents, and signing key handling.

## Runtime and infrastructure

Review service identity, cloud permissions, public storage, database/network exposure, tenant partitioning, TLS configuration, backup access, encryption key lifecycle, environment injection, and administrator interfaces. Apply limited retries, timeouts, quotas, request size limits, and safe degradation. Authorization failures must never turn into success through a fallback.

Check monitoring for authentication abuse, authorization denial patterns, privileged changes, data exports, sensitive configuration changes, and failed integrity checks. Keep audit events traceable to who did them and hard to tamper with, as fits, with retention that respects privacy. Logs must not become a second unauthorized database.

## Business and data flows

Check that payments, entitlements, inventory, resource ownership, account deletion, recovery, sharing, notifications, and integration callbacks match their real state. Verify idempotency under replay and concurrency. Validate amounts, currency, actor, resource, and state change on the source-of-truth server. An opaque URL does not prevent a cross-account charge, export, or entitlement mutation.

Review environment-specific exposure. Local development defaults do not justify production debug settings. In the other direction, do not add irrelevant production infrastructure requirements to a local-only tool. Apply controls to the system you are really assessing.
