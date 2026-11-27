---
name: web-app-testing
description: Test web applications locally with Playwright and remotely with current AWS, Azure or Google Cloud services. Use for forms, navigation, browser matrices, accessibility, failure diagnosis and cloud runs backed by evidence.
license: MIT
---

# Web App Testing

Test web behavior you can observe, with local Playwright and a remote service you choose on purpose.
This is descriptive guidance. Use the browser tools and existing suites you have.
Do not bundle a runner, generated test engine or automatic service catalog. New test scripts that
the user asks for use Python and uv. Existing app-native suites keep their supported language.

## Establish target, scope, and evidence

Read the project instructions, start/build/test commands, framework, sign-in, API boundaries
and existing tests. Confirm the approved URLs/environment, critical journeys, browsers/OS, viewports,
roles/tenants, test data, accessibility needs and allowed side effects. Choose synthetic accounts
and fixtures that always give the same result. By default, never use real payments or destructive
production data.

Keep these apart: local interaction, regression assertions that give the same result each time,
remote browser infrastructure, cloud CI runs, synthetic monitoring, load testing and physical mobile
browser testing. Each gives different evidence. A responsive Chromium viewport is not Safari on a
real iPhone. A passing canary or HTTP probe does not show that every form and business rule works.

## Run local Playwright with the real environment

For a new Python test suite the user asked for, use the supported pytest integration:

```bash
uv add --dev pytest-playwright
uv run playwright install chromium firefox webkit
uv run pytest tests/web --base-url http://127.0.0.1:8000 --browser chromium --tracing retain-on-failure --screenshot only-on-failure --output artifacts/playwright
```

Replace `tests/web`, the base URL and the output folder with real values. Repeat `--browser`
for each chosen engine. Without `--output`, artifacts go to `test-results`. On suitable Linux
CI hosts, install browser system dependencies with `uv run playwright install --with-deps chromium`
for each chosen browser, with the host permissions this needs. Pin matching browser/client versions
in the project's dependency/container contract. Do not assume a JavaScript Playwright image includes
the Python runtime or Python package.

Start the app with its documented command in a separate process/session you own. Wait for
a real ready state instead of a fixed sleep. Write down the real URL, port, build/configuration
and artifact identity. Stop only processes you created for this test. A server or database that
already existed does not become throwaway just because the test used it.

Use existing Playwright browser/MCP tools for exploratory interaction where you have them. Check their
real tool schema and keep evidence. Reading a DOM snapshot does not show that an assertion or a
whole suite ran. If tools/browsers are not available, report the missing requirement and finish
the independent test plan instead of making up a run.

## Design stable cases and meaningful assertions

Prefer role/name, linked label and stable test-ID locators. Avoid fragile layout CSS, long XPath,
picking whatever matches first, forced clicks that skip actionability checks and fixed sleeps.
Use Playwright's retrying assertions and actionability. Wait for the real UI/network condition
that means success, not a generic network-idle guess on an app with polling or sockets.

For a form, test valid entry, required/invalid/boundary values, normalization, keyboard order,
autofill/input types, password visibility, pending state, double submit, server validation,
network failure, permission denial and draft recovery where they apply. Check results the user can
see and the right backend effects. A click that finishes without error does not prove a record was saved.

Cover navigation/back/forward, deep links, reload/restore, dialogs/focus, lists/search/paging,
empty/error/loading states, uploads/downloads, localization/long content, themes, responsive layout
and account/tenant switching, based on the app's real features. Test that objects a user must not
reach stay out of reach through both the UI and the requests behind it. Hiding a route alone is not
authorization.

Use isolated browser contexts and independent data. Keep saved signed-in browser state under
`playwright/.auth/` and ignore that folder, or clearly ignore the real chosen state path.
These files can contain reusable credentials and must not go into Git or public artifacts. An ignore
rule does not untrack a file that is already tracked. Do not reuse one changeable account/order across
parallel tests. Mock controlled UI dependencies when it fits, then check the real integration contracts
separately. Do not claim a mocked payment or purchase proves a live provider works.

## Worked local example

This shows a Python test in the user's app, not a bundled program:

```python
from playwright.sync_api import Page, expect


def test_required_email(page: Page) -> None:
    page.goto("/signup")
    page.get_by_label("Email").fill("invalid-address")
    page.get_by_role("button", name="Create account").click()

    expect(page.get_by_text("Enter a valid email address.", exact=True)).to_be_visible()
```

The relative route resolves against `--base-url`. Use the real routes, labels and validation
behavior. Native browser constraint validation may block submission without this custom text, so
look at the real form before you choose the assertion. Check that no unintended account was created.
Do not make up test messages just to make this example pass.

## Choose a current remote route

Baseline checked on 2026-11-05. Read [provider details](references/cloud-services.md) and
[sources](references/sources.md) before a paid/private upload.

| Provider/surface | Suitable use | Boundary |
| --- | --- | --- |
| Azure App Testing Playwright Workspaces | Managed remote Playwright browsers and parallel runs. | Current service. Check supported browsers/OS, client versions, identity and private access. |
| Azure Pipelines | Run the existing suite on a suitable hosted/self-hosted agent or connect it to Workspaces. | A CI run is separate from a managed browser reservation. |
| AWS CodeBuild | Run a pinned Python/Playwright suite/container in an approved build. | The team owns browser/container dependencies, networking, reports and capacity. |
| AWS Device Farm desktop browser testing | Existing supported Selenium/WebDriver suites. | Not a drop-in native Playwright endpoint. Do not make up protocol compatibility. |
| AWS CloudWatch Synthetics | Limited scheduled canaries that act like production use. | Node.js Playwright runtimes differ from Python pytest. Monitoring is not full release QA. |
| Google Cloud Build | Run a suitable pinned Playwright test environment. | Cloud CI, not a native managed cross-browser/device grid. |
| Google Cloud Run browser automation/jobs | Controlled browser workload in a container. | The team owns browser dependencies, isolation, resources, assertions and artifacts. |

Use Playwright Workspaces in Azure App Testing for Azure-hosted Playwright browsers. Do not set up
Microsoft Playwright Testing, which is retired. Label Preview features separately from generally
available services.

## Remote execution procedure

1. Check the provider's real current service, region, account entitlement, OS/browser/client
   compatibility, quotas and expected billing. Choose fixed parallelism, timeout and attempts.
2. Name the approved build, source/artifact upload, synthetic identities, backend/data scope,
   network route, retention and who owns cleanup. A remote browser's localhost is not the
   developer's machine.
3. Set up the documented identity and narrow permissions. Prefer supported short-lived identity
   over committing a service-account/token file. Do not print endpoint tokens or signed-in URLs.
4. Prepare the existing suite and environment. For a cloud browser, use its real Playwright
   connection contract. For cloud CI, install matching browsers/dependencies or use a pinned image.
5. Submit once and keep the run/build/session identity. If the client response is lost, check the
   real state before a retry that could start another paid run or repeat a change.
6. Check the outcome for each browser/job/case, not just a finished build. Get traces, screenshots,
   logs and reports within the approved retention. Tell assertion failures apart from
   setup/infrastructure failure.
7. Stop the sessions/tunnels/jobs you own, revoke temporary access when required, and keep/clean the
   agreed evidence. Do not delete a shared project or database as test cleanup.

## Diagnose and deliver

Open a kept trace with `uv run playwright show-trace PATH_TO_TRACE_ZIP`, using the path that the
failed test wrote under the output folder, and look at the screenshots that matter. Find the real
route, role, browser/version, data, locator, request/response, console failure and timing that
explain the result. Do not fix a flaky test by adding long sleeps, raising retries
without limit or rewriting selectors automatically until the run is green. Tell apart a product bug,
test bug, data collision, unsupported feature and provider outage.

Report the URL/environment, build or artifact identity, browser engines and versions, viewports,
roles, provider run IDs, and every case with one status: Passed, Failed, Blocked, Infrastructure
error, Skipped/not run, or Flaky/inconclusive. Count a case as passed only if it ran and its assertions
succeeded. For each failure, give the shortest steps to reproduce it, expected and actual results, the
first attempt's outcome and cleaned trace/screenshot paths. List the browsers, devices and risks not
covered. Screenshots help visual review but do not certify accessibility. Mobile emulation does not
prove hardware behavior. When real mobile browser behavior is required, test a physical device or
a provider that documents real mobile browsers, and report it as a separate configuration. Otherwise
mark it not covered. Update the app's testing instructions when the real commands/configuration change.
Writing this skill does not mean any live cloud test ran.
