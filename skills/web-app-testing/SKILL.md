---
name: web-app-testing
description: Test web applications locally with Playwright and remotely using current AWS, Azure, or Google Cloud capabilities. Use for forms, navigation, browser matrices, accessibility, failure diagnosis, and evidenced cloud execution.
license: MIT
---

# Web App Testing

Test observable web behavior through local Playwright and an explicitly selected current remote
execution service. This is descriptive guidance. Use available browser tools and existing suites.
Do not bundle a runner, generated test engine, or automatic service catalog. Newly requested test
scripts use Python and uv. Existing application-native suites retain their supported language.

## Establish target, scope, and evidence

Inspect project instructions, start/build/test commands, framework, authentication, API boundaries,
and existing tests. Confirm authorized URLs/environment, critical journeys, browsers/OS, viewports,
roles/tenants, test data, accessibility needs, and permitted side effects. Select synthetic accounts
and deterministic fixtures. Never exercise real payments or destructive production data by default.

Separate local interaction, deterministic regression assertions, remote browser infrastructure,
cloud CI execution, synthetic monitoring, load testing, and physical mobile browser testing. These
provide different evidence. A responsive Chromium viewport is not Safari on an actual iPhone.
A passing canary or HTTP probe does not establish complete form/business correctness.

## Run local Playwright with the actual environment

For an explicitly requested new Python test suite, use the supported pytest integration:

```bash
uv add --dev pytest-playwright
uv run playwright install chromium firefox webkit
uv run pytest tests/web --browser chromium --tracing retain-on-failure --screenshot only-on-failure
```

Replace `tests/web` with the actual suite directory. On appropriate Linux CI hosts, install browser
system dependencies with the documented `playwright install --with-deps` path and required host
permissions. Pin compatible browser/client versions in the project's dependency/container contract.
Do not assume a JavaScript Playwright image includes the Python runtime or Python package.

Start the application through its documented command in a separate owned process/session. Wait for
a meaningful ready state rather than a fixed sleep. Record the actual URL, port, build/configuration,
and artifact identity. Stop only processes created for this test. A preexisting server or database
does not become disposable because the test used it.

Use existing Playwright browser/MCP tools for exploratory interaction where available. Inspect their
actual tool schema and retain evidence. Reading a DOM snapshot is not evidence that an assertion or
whole suite executed. If tools/browsers are unavailable, report the missing prerequisite and complete
the independent test plan instead of inventing a run.

## Design stable cases and meaningful assertions

Prefer role/name, associated label, and stable test-ID locators. Avoid fragile layout CSS, long XPath,
arbitrary first-match selection, forced clicks that bypass interactability, and fixed sleeps.
Use Playwright's retrying assertions and actionability. Wait for the actual UI/network condition
that defines success, not a generic network-idle heuristic on an app with polling or sockets.

For a form, test valid entry, required/invalid/boundary values, normalization, keyboard order,
autofill/input types, password visibility, pending state, duplicate submit, server validation,
network failure, permission denial, and draft recovery where relevant. Assert user-visible results
and appropriate backend effects. A click resolving without error does not prove a record was saved.

Cover navigation/back/forward, deep links, reload/restoration, dialogs/focus, lists/search/paging,
empty/error/loading states, uploads/downloads, localization/long content, themes, responsive layout,
and account/tenant switching based on the app's actual features. Test that inaccessible objects stay
inaccessible through both UI and underlying requests. Route hiding alone is not authorization.

Use isolated browser contexts and independent data. Keep saved authenticated browser state under
`playwright/.auth/` and ignore that directory, or explicitly ignore the actual selected state path.
These files can contain reusable credentials and must not enter Git or public artifacts. An ignore
rule does not untrack an existing file. Do not reuse one mutable account/order across parallel tests.
Mock controlled UI dependencies when appropriate, then separately verify real integration contracts.
Do not claim a mocked payment or purchase validates a live provider.

## Worked local example

The following describes a Python test in the user's application, not a bundled executable:

```python
from playwright.sync_api import Page, expect


def test_required_email(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/signup")
    page.get_by_label("Email").fill("invalid-address")
    page.get_by_role("button", name="Create account").click()

    expect(page.get_by_text("Enter a valid email address.", exact=True)).to_be_visible()
```

Use actual routes, labels, and validation behavior. Native browser constraint validation may prevent
submission without this custom text, so inspect the real form before choosing the assertion. Verify
that no unintended account was created. Do not invent test messages just to make this example pass.

## Choose a current remote route

Baseline checked on 2026-11-05. Read [provider details](references/cloud-services.md) and
[sources](references/sources.md) before a paid/private upload.

| Provider/surface | Suitable use | Boundary |
| --- | --- | --- |
| Azure App Testing Playwright Workspaces | Managed remote Playwright browsers and parallel execution. | Current service. Inspect supported browsers/OS, client versions, identity, and private access. |
| Azure Pipelines | Run the existing suite on a suitable hosted/self-hosted agent or connect it to Workspaces. | CI execution is separate from a managed browser reservation. |
| AWS CodeBuild | Run a pinned Python/Playwright suite/container in an authorized build. | Team owns browser/container dependencies, networking, reports, and capacity. |
| AWS Device Farm desktop browser testing | Existing supported Selenium/WebDriver suites. | Not a drop-in native Playwright endpoint. Do not invent protocol compatibility. |
| AWS CloudWatch Synthetics | Bounded scheduled production-like canaries. | Node.js Playwright runtimes differ from Python pytest. Monitoring is not full release QA. |
| Google Cloud Build | Execute a suitable pinned Playwright test environment. | Cloud CI, not a native managed cross-browser/device grid. |
| Google Cloud Run browser automation/jobs | Controlled containerized browser workload. | Team owns browser dependencies, isolation, resources, assertions, and artifacts. |

Microsoft Playwright Testing retired on March 8, 2026. Use its current successor, Playwright
Workspaces in Azure App Testing. App Center Test is also retired and is not a web/device option.
Do not recommend a retired offering because an old tutorial remains searchable. Preview features
must be labeled separately from generally available services.

## Remote execution procedure

1. Verify the provider's actual current service, region, account entitlement, OS/browser/client
   compatibility, quotas, and expected billing. Choose finite parallelism, timeout, and attempts.
2. Identify the approved build, source/artifact upload, synthetic identities, backend/data scope,
   network route, retention, and cleanup owner. A remote browser's localhost is not the developer host.
3. Configure the documented identity and narrow permissions. Prefer supported short-lived identity
   over committing a service-account/token file. Do not print endpoint tokens or authenticated URLs.
4. Prepare the existing suite and environment. For a cloud browser, use its actual Playwright
   connection contract. For cloud CI, install matching browsers/dependencies or use a pinned image.
5. Submit once and retain the run/build/session identity. A lost client response needs state
   reconciliation before a retry that could launch another paid run or repeat a mutation.
6. Inspect per-browser/job/case outcomes, not just a completed build. Retrieve traces, screenshots,
   logs, and reports within authorized retention. Distinguish assertions from setup/infrastructure failure.
7. Stop owned sessions/tunnels/jobs, revoke temporary access when required, and retain/redact the
   agreed evidence. Do not delete a shared project or database as test cleanup.

## Diagnose and deliver

Open traces and relevant screenshots. Identify the actual route, role, browser/version, data, locator,
request/response, console failure, and timing that explain the result. Do not solve a flaky test by
adding long sleeps, increasing retries indefinitely, or automatically rewriting selectors until green.
Separate a product defect, test defect, data collision, unsupported feature, and provider outage.

Report executed/passed/failed/skipped/blocked cases with a meaningful denominator, reproducible
steps, evidence paths, and uncovered risks. Screenshots help visual review but do not certify
accessibility. Mobile emulation does not prove hardware behavior. Update app testing instructions
when actual commands/configuration change. No live cloud test is implied by writing this skill.
