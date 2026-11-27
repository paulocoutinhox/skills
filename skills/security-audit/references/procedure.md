# Assessment procedure

## Inventory and threat model

Name assets such as user content, billing state, credentials, identity records, private files, executable updates, and administrative controls. Name actors: anonymous, normal user, another user, another tenant, administrator, service worker, external integration, compromised renderer, malicious local process, and dependency supplier.

Map network, process, tenant, role, storage, device, and build boundaries. Write down who controls each input and which component makes the authorization decision. A mobile or desktop UI is an untrusted client from the backend's perspective. Client-side hiding does not protect a server operation.

## Evidence collection

Use repository search, dependency manifests and lockfiles, generated API schemas, routing registries, migrations, access policies, build workflows, installer/update configuration, and deployment manifests. Check which code is really reachable. Dead sample code and an active production endpoint do not have the same exposure.

Record each finding's location, trigger, prerequisites, sensitive sink or data flow, attacker benefit, evidence, and corrective control. Keep confirmed findings apart from suspicious patterns and open questions. Do not print real credentials, personal data, or full sensitive responses in the report.

## Testing strategy

Use two controlled users and at least two tenants where tenancy exists. Run allowed and denied requests through real entrypoints. Include unauthenticated, expired, revoked, low-role, deleted-user, and stale-session cases when relevant. For stateful business flows, test duplicate requests, concurrent operations, replay, and interruption. Prefer harmless canary data and isolated local environments.

Use tools the project really supports: SAST, dependency audits, a redacting secret scanner, fuzzing, sanitizers, API integration tests, mobile platform tests, native diagnostics, and signed-update verification as appropriate. Do not install every scanner without a reason, and do not treat a passing scan as proof of a secure architecture.

## Reporting and fixes

Order findings by impact and reachability. Cite the exact affected code and explain the realistic scenario. Recommend a control at the source-of-truth boundary instead of a UI-only workaround. For defects that span many places, list the other paths that share the same flaw. Retest the fix with positive and negative evidence.

State the reviewed revision, platform versions, available environments, checks you ran, paths covered, and important exclusions. A full requested code audit can still leave dynamic infrastructure or unavailable integrations unverified. Never mark untested areas as passed.
