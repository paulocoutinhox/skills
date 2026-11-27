# Current cloud web-test surfaces

Baseline: 2026-11-05. At run time, confirm the real region, account, feature lifecycle, supported
client and network path. Only the user asks for maintenance of this stored guidance.

## Azure

Playwright Workspaces in Azure App Testing is the current managed browser service. Do not use the
retired Microsoft Playwright Testing name as a new setup target. Choose the real workspace
permissions, region and browser/OS availability. The provider has Python examples as well as JS/TS
and .NET. Do not assume JS-specific reporter/configuration APIs work unchanged with pytest.

The official Python/pytest samples use a regional WebSocket browser endpoint, run identity, target
OS, API version and an Authorization header. Read the current sample and identity guide. Check the
required configuration clearly. Do not quietly switch to local browsers when remote runs were
requested, and do not copy the sample's optional-import/catch-all branches into app tooling.
Use the pytest plugin's real connection fixture contract. Close contexts/connections and check
the service session after an interruption. A client timeout alone does not show that the session ended.

Private URLs need the documented network exposure/tunnel behavior and a narrow approved scope.
Exposing all localhost/network resources can reveal unrelated development services. Stored traces,
screenshots and sign-in state can contain private data. Managed browser OS coverage does not
prove native Safari on macOS/iOS hardware. Check the exact browser implementation.

The provider's remote MCP browser service is labeled Preview on its own in its README. Use it only
when it is available and suitable, with its own OAuth/RBAC/session contract. Do not mix up that preview
with the GA Workspaces service. Azure Pipelines can run the existing local suite on prepared agents
or coordinate remote connections, without becoming a device/browser farm itself.

## AWS

CodeBuild can run the chosen Playwright/Python environment and publish reports/artifacts. Pin
images that match the client/browser, install the real Python/system dependencies, set up app
readiness and use an isolated dataset. Choose VPC access on purpose for private backends. A build
container's network and the app's network are separate. Keep failure evidence and the exit status.

Device Farm's desktop offering documents Selenium WebDriver. A Selenium grid URL is not a native
Playwright WebSocket. Experimental adapters, if you evaluate them on purpose, have their own limited
browser/protocol contract, and you cannot assume they are equal. For native Playwright, prefer a suitable
CodeBuild/container route or a remote service that clearly supports it.

CloudWatch Synthetics has Node.js Playwright canary runtimes. Its monitoring model, run budget,
artifact permissions and supported runtime differ from Python pytest. Explain that limit instead
of generating JavaScript glue against the owner's Python-script rule. A scheduled production
canary needs its own approval and synthetic data that is safe to reuse on every run.

## Google Cloud

Cloud Build can run Playwright in a properly prepared container. Cloud Run documents browser
automation with libraries such as Playwright, and the app owns the resource/runtime/security
decisions. For a fixed test workload, choose the right job/build lifecycle instead of an
open-ended public web service. Set CPU/memory, browser sandbox policy, concurrency, timeout, network,
identity, artifact bucket and cleanup on purpose. Do not turn off browser security flags out of habit.

Neither service gives you a managed Safari/Windows/physical-device matrix by itself. Linux WebKit
is useful browser-engine evidence but not real Safari-device evidence. Keep the exact limits in
the test report.
