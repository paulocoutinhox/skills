# Web testing sources

Checked on 2026-11-05. No cloud account setup, upload, paid run or browser run was done while
writing.

| Source | Governing role |
| --- | --- |
| [Playwright Python pytest reference](https://playwright.dev/python/docs/test-runners) | Runner fixtures and CLI browser/trace/screenshot options. |
| [Playwright Python locators](https://playwright.dev/python/docs/locators) | Role/label/test-ID contracts and retryable locators. |
| [Playwright Python CI](https://playwright.dev/python/docs/ci) | Browser/system dependency install and prepared CI environments. |
| [Playwright Python authentication](https://playwright.dev/python/docs/auth) | Private saved browser state and the recommended ignored playwright/.auth folder. Rechecked on 2026-11-05. |
| [Azure Workspaces overview](https://learn.microsoft.com/en-us/azure/app-testing/playwright-workspaces/overview-run-playwright-tests-at-scale) | Current managed browser service and OS/browser surface. |
| [Azure provider repository](https://github.com/Azure/playwright-workspaces) | Real supported examples, current GA service and the separate Preview remote MCP. |
| [Azure Python sample](https://github.com/Azure/playwright-workspaces/blob/main/samples/playwright-python/Readme.md) | Workspace/endpoint/identity setup for Python. |
| [Azure pytest connection example](https://github.com/Azure/playwright-workspaces/blob/main/samples/playwright-pytest/conftest.py) | Real connection fixture and remote/private-network fields. Review its loose local fallback instead of copying it. |
| [Microsoft Playwright Testing retirement](https://learn.microsoft.com/en-us/rest/api/playwright/includes/retirement-banner) | March 8, 2026 retirement and the service that replaces it. |
| [AWS desktop testing](https://docs.aws.amazon.com/devicefarm/latest/testgrid/what-is-testgrid.html) | Selenium/WebDriver limit. |
| [AWS CodeBuild buildspec](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html) | Real build phases, running commands, reports/artifacts and container-based CI duties. |
| [AWS Synthetics Playwright runtime](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_playwright.html) | Node.js canary runtime, separate from pytest QA. |
| [Playwright CI provider guide](https://playwright.dev/docs/ci) | Google Cloud Build run example, not a promise of a managed grid. |
| [Cloud Run browser automation](https://docs.cloud.google.com/run/docs/browser-automation) | Browser workloads in containers and who is responsible for what. |

Check current offerings and their account-specific capacity at run time. A listed API,
container example or connected MCP server does not show that an app test ran and passed.

Rechecked on 2026-11-18: the [pytest reference](https://playwright.dev/python/docs/test-runners) for
`--base-url` relative navigation, repeatable `--browser`, and the `--output` default of
`test-results`, the [trace viewer guide](https://playwright.dev/python/docs/trace-viewer-intro) for `playwright show-trace`, and [AWS desktop testing](https://docs.aws.amazon.com/devicefarm/latest/testgrid/what-is-testgrid.html)
for its Selenium/W3C WebDriver-only access. No browser or cloud run was done for these checks.

Rechecked on 2026-11-18: the [Microsoft Playwright Testing retirement notice](https://learn.microsoft.com/en-us/rest/api/playwright/includes/retirement-banner)
gives March 8, 2026 and points users to Playwright Workspaces in Azure App Testing, described as
generally available. The [Azure provider repository](https://github.com/Azure/playwright-workspaces)
labels its remote MCP server Preview, separate from the GA service. The [pytest reference](https://playwright.dev/python/docs/test-runners)
lists `retain-on-failure` tracing and `only-on-failure` screenshots. The [Playwright CI guide](https://playwright.dev/docs/ci)
uses a JavaScript Playwright image for Google Cloud Build, and the [Python CI guide](https://playwright.dev/python/docs/ci)
has no Cloud Build section. The [Cloud Run browser automation page](https://docs.cloud.google.com/run/docs/browser-automation)
names Playwright only as a library option, not as a documented setup. No browser or cloud run was done.
