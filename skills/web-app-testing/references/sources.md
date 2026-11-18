# Web testing sources

Verified on 2026-11-05. No cloud account provisioning, upload, billable run, or browser execution was
performed during authoring.

| Source | Governing role |
| --- | --- |
| [Playwright Python pytest reference](https://playwright.dev/python/docs/test-runners) | Runner fixtures and CLI browser/trace/screenshot options. |
| [Playwright Python locators](https://playwright.dev/python/docs/locators) | Role/label/test-ID contracts and retryable locators. |
| [Playwright Python CI](https://playwright.dev/python/docs/ci) | Browser/system dependency installation and prepared CI environments. |
| [Playwright Python authentication](https://playwright.dev/python/docs/auth) | Private saved browser state and the recommended ignored playwright/.auth directory. Rechecked on 2026-11-05. |
| [Azure Workspaces overview](https://learn.microsoft.com/en-us/azure/app-testing/playwright-workspaces/overview-run-playwright-tests-at-scale) | Current managed browser service and OS/browser surface. |
| [Azure provider repository](https://github.com/Azure/playwright-workspaces) | Actual supported examples, current GA service, and separately Preview remote MCP. |
| [Azure Python sample](https://github.com/Azure/playwright-workspaces/blob/main/samples/playwright-python/Readme.md) | Workspace/endpoint/identity setup for Python. |
| [Azure pytest connection example](https://github.com/Azure/playwright-workspaces/blob/main/samples/playwright-pytest/conftest.py) | Real connection fixture and remote/private-network fields. Evaluate rather than copy its permissive local fallback. |
| [Microsoft Playwright Testing retirement](https://learn.microsoft.com/en-us/rest/api/playwright/includes/retirement-banner) | March 8, 2026 retirement and successor. |
| [AWS desktop testing](https://docs.aws.amazon.com/devicefarm/latest/testgrid/what-is-testgrid.html) | Selenium/WebDriver boundary. |
| [AWS CodeBuild buildspec](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html) | Actual build phases, command execution, reports/artifacts, and container-based CI responsibilities. |
| [AWS Synthetics Playwright runtime](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_playwright.html) | Node.js canary runtime, distinct from pytest QA. |
| [Playwright CI provider guide](https://playwright.dev/docs/ci) | Google Cloud Build execution example, not a managed grid guarantee. |
| [Cloud Run browser automation](https://docs.cloud.google.com/run/docs/browser-automation) | Containerized browser workloads and responsibility boundaries. |

Current offerings and their account-specific capacity must be checked at execution. A listed API,
container example, or connected MCP server does not demonstrate a completed passing application test.

Rechecked on 2026-11-18: the [pytest reference](https://playwright.dev/python/docs/test-runners) for
`--base-url` relative navigation, repeatable `--browser`, and the `--output` default of
`test-results`, the [trace viewer guide](https://playwright.dev/python/docs/trace-viewer-intro) for `playwright show-trace`, and [AWS desktop testing](https://docs.aws.amazon.com/devicefarm/latest/testgrid/what-is-testgrid.html)
for its Selenium/W3C WebDriver-only access. No browser or cloud run was executed for these checks.

Rechecked on 2026-11-18: the [Microsoft Playwright Testing retirement notice](https://learn.microsoft.com/en-us/rest/api/playwright/includes/retirement-banner)
gives March 8, 2026 and directs users to Playwright Workspaces in Azure App Testing, described as
generally available. The [Azure provider repository](https://github.com/Azure/playwright-workspaces)
labels its remote MCP server Preview, separate from the GA service. The [pytest reference](https://playwright.dev/python/docs/test-runners)
lists `retain-on-failure` tracing and `only-on-failure` screenshots. The [Playwright CI guide](https://playwright.dev/docs/ci)
uses a JavaScript Playwright image for Google Cloud Build, and the [Python CI guide](https://playwright.dev/python/docs/ci)
has no Cloud Build section. The [Cloud Run browser automation page](https://docs.cloud.google.com/run/docs/browser-automation)
names Playwright only as a library option, not as a documented setup. No browser or cloud run was executed.
