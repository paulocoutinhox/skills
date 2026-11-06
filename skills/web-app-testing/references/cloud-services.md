# Current cloud web-test surfaces

Baseline: 2026-11-05. Confirm the actual region, account, feature lifecycle, supported client, and
network path at execution. Only the user requests maintenance of this stored guidance.

## Azure

Playwright Workspaces in Azure App Testing is the current managed browser service. The retired
Microsoft Playwright Testing name must not become a new setup target. Select actual workspace
permissions, region and browser/OS availability. The provider has Python examples as well as JS/TS
and .NET. Do not assume JS-specific reporter/configuration APIs apply unchanged to pytest.

The official Python/pytest samples use a regional WebSocket browser endpoint, run identity, target
OS, API version, and an Authorization header. Read the current sample and identity guide. Validate
required configuration explicitly. Do not silently switch to local browsers when remote execution
was requested, and do not copy optional-import/catch-all sample branches into application tooling.
Use the pytest plugin's actual connection fixture contract. Close contexts/connections and inspect
the service session after interruption. A client timeout alone does not establish session termination.

Private URLs need the documented network exposure/tunnel behavior and a narrowly approved scope.
Exposing all localhost/network resources can reveal unrelated development services. Stored traces,
screenshots, and authentication state can contain private data. Managed browser OS coverage is not
proof of native Safari on macOS/iOS hardware. Inspect the exact browser implementation.

The provider's remote MCP browser service is separately labeled Preview in its README. Use it only
when available and appropriate, with its own OAuth/RBAC/session contract. Do not conflate that preview
with the GA Workspaces service. Azure Pipelines can run the existing local suite on prepared agents
or orchestrate remote connections without becoming a device/browser farm itself.

## AWS

CodeBuild can run the selected Playwright/Python environment and publish reports/artifacts. Pin
client/browser-compatible images, install actual Python/system dependencies, configure application
readiness, and use an isolated dataset. Select VPC access deliberately for private backends. A build
container's network and the application's network are distinct. Retain failure evidence and exit status.

Device Farm's desktop offering documents Selenium WebDriver. A Selenium grid URL is not a native
Playwright WebSocket. Experimental adapters, if evaluated explicitly, need their actual limited
browser/protocol contract and cannot be assumed equivalent. For native Playwright, prefer a suitable
CodeBuild/container route or an explicitly supported remote service.

CloudWatch Synthetics has Node.js Playwright canary runtimes. Its monitoring model, execution budget,
artifact permissions, and supported runtime differ from Python pytest. Explain that boundary rather
than generating JavaScript glue against the owner's Python-script rule. A scheduled production
canary requires its own authorization and repeat-safe synthetic data.

## Google Cloud

Cloud Build can execute Playwright in an appropriately prepared container. Cloud Run documents browser
automation with libraries such as Playwright, with resource/runtime/security decisions owned by the
application. For a finite test workload, choose the appropriate job/build lifecycle rather than an
unbounded public web service. Set CPU/memory, browser sandbox policy, concurrency, timeout, network,
identity, artifact bucket, and cleanup deliberately. Do not disable browser security flags by habit.

Neither service inherently supplies a managed Safari/Windows/physical-device matrix. Linux WebKit
is useful browser-engine evidence but not real Safari-device evidence. Firebase/mobile lab branding
does not establish a desktop Playwright service. Preserve exact limitations in the test report.
