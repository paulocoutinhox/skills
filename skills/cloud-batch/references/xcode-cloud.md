# Xcode Cloud

Read this when Apple builds and simulator tests should run in Apple's own CI instead of on the local Mac or a rented Mac. Facts were checked on **2026-11-26** against Apple's Xcode Cloud documentation and the App Store Connect API reference (see the sources at the end). This reference comes from the docs. The projects behind this skill ran Apple work on the local Mac and in other CI, so treat the first Xcode Cloud workflow as a trial.

## When it fits

| Use Xcode Cloud for | Use something else for |
| --- | --- |
| Apple builds, analyze and archive for iOS, iPadOS, macOS, Mac Catalyst, tvOS, watchOS and visionOS | Physical devices: the docs name only simulator test destinations. Use the person's own devices or [Device Farm](device-farm.md) |
| UI and unit tests on simulators, many in parallel, while the local Mac is busy | visionOS test actions: a known issue says they are not supported. Test visionOS on the local Mac |
| Work that fits the included 25 compute hours a month | Real GPU numbers: use a real Mac or device |
| A full Apple matrix started by hand at the end of a block of work | Anything that needs `sudo`, SSH access or a long custom job |

Xcode Cloud is not for release work in this skill. Leave TestFlight and App Store post-actions off unless the person asks for them, because that is store delivery.

## Requirements

- Apple Developer Program membership, Xcode 15 or later, and the person's Apple Account in Xcode Settings > Accounts.
- A remote Git repository on GitHub, GitHub Enterprise, GitLab, self-managed GitLab, Bitbucket Cloud or Bitbucket Server. Granting access needs admin rights on the repository (GitHub organization owner or repository admin, GitLab maintainer, Bitbucket administrator). A self-hosted Git server must accept Apple's HTTPS connections on port 443 from Apple's published address ranges.
- An app record in App Store Connect. Xcode offers to create one during onboarding, which needs the App Manager, Admin or Account Holder role, or the Developer role with the Create Apps permission. A framework needs no app record.
- Shared schemes, automatic signing, and a project file that exists in the repository. A project generated at build time (for example with XcodeGen) may fail, so commit the generated project or generate it in `ci_post_clone.sh`.
- Paid compute plans need the Account Holder role.

Creating the first workflow is a person's step in Xcode, because it grants Apple access to the repository: **Integrate > Create Workflow**, or the Cloud button in the Report navigator, then Select a Product, Review Workflow, Grant Access, Complete and Start Build. After the first build, workflows can be edited in Xcode (**Integrate > Manage Workflows**) or in App Store Connect.

## Design the workflows like batches

Follow the same two levels as other CI (see [CI and caches](ci-and-cache.md#keep-ci-fast-and-cheap)):

1. **A small push workflow:** start condition Branch Changes or Pull Request Changes on the default branch, one Build or Test action on the most important platform, and Required To Pass on. Auto-cancel of superseded builds is on by default. A commit message with `[ci skip]` skips a build.
2. **A full matrix workflow with Manual Start:** one Test action per platform, each with its simulator destinations and test plan, plus Analyze if the project uses it. Start it by hand, or through the API, once per block of work. It is the Apple part of the batch line.

Workflow parts, as Apple names them:

- **Start conditions:** Branch Changes, Pull Request Changes, Tag Changes, On a Schedule for a Branch and Manual Start, optionally limited to files and folders.
- **Environment:** the Xcode and macOS versions, the Clean option (no cached derived data, slower) and custom environment variables.
- **Actions:** Build, Analyze, Test and Archive, each with a platform and a scheme.
- **Post-actions:** notifications by e-mail or Slack, TestFlight and App Store delivery. Use notifications only.

Rules for the Test action:

- It builds for testing by itself, so it needs no separate Build action.
- It runs `xcodebuild build-for-testing`, then `xcodebuild test-without-building` in a second phase **without the source code**. Test fixtures must be test resources, not files beside the sources.
- Every action runs in its own temporary environment, and actions do not share files.
- Platforms run in parallel, and every test run gets a fresh simulator, so the shared-simulator problems of a local Mac do not happen there.
- Set a test plan with test timeouts (the plan's default execution time allowance is 600 seconds) and keep Retry on Failure off. A flaky test is fixed, not retried until it passes (see [batches](batches.md#flaky-tests-prove-the-cause-never-hide-it)).
- The local simulator tricks in [Apple platforms](apple-platforms.md) still apply inside the tests: launch arguments per test, alerts by button position, keyboard settings and log checks.

## Custom build scripts

Xcode Cloud runs three optional scripts from a `ci_scripts` folder next to the project or workspace. The names are fixed:

| Script | Runs | Typical use |
| --- | --- | --- |
| `ci_scripts/ci_post_clone.sh` | After the clone | Install tools with Homebrew, generate the project, `pod install`, install Carthage |
| `ci_scripts/ci_pre_xcodebuild.sh` | Before each `xcodebuild` | Write a config file from environment variables |
| `ci_scripts/ci_post_xcodebuild.sh` | After each `xcodebuild`, also when it failed | Print a summary, collect extra logs |

They are shell scripts because Xcode Cloud requires that form. Keep them short and make them exit non-zero on any failure (`set -euo pipefail`), since a script that ends with `echo` hides the failure, as in [batches](batches.md#the-batch-runner-reports-failures-honestly).

- Make them executable with `chmod +x` and commit that bit.
- `sudo` is not allowed. Homebrew, Python, Git LFS and CocoaPods are installed. Carthage is not.
- Files a script creates are deleted afterwards and are not seen by other scripts. Keep any helper files inside `ci_scripts`, since the source may not be present in every phase. Do not name helper files with a `ci_` prefix.
- Builds reach the internet through an HTTP proxy, set in `HTTP_PROXY` and `HTTPS_PROXY`.

Variables a script can read include `CI_XCODEBUILD_ACTION` (`build`, `build-for-testing`, `test-without-building`, `analyze`, `archive`), `CI_XCODEBUILD_EXIT_CODE` (after the action), `CI_PRODUCT_PLATFORM`, `CI_START_CONDITION`, `CI_BRANCH`, `CI_TAG`, `CI_PULL_REQUEST_NUMBER`, `CI_COMMIT`, `CI_PRIMARY_REPOSITORY_PATH`, `CI_WORKSPACE_PATH`, `CI_DERIVED_DATA_PATH`, and for tests `CI_RESULT_BUNDLE_PATH`, `CI_TEST_DESTINATION_UDID` and `CI_TEST_PLAN`. Variables with the `TEST_RUNNER_` prefix reach the test runner without the prefix, which is how a test gets a launch setting.

## Secrets and dependencies

- Put secrets in the workflow's environment variables with **Secret** (App Store Connect) or **Keep value redacted** (Xcode) turned on. Logs then show `**********`. Never commit them.
- Swift packages and Git submodules work when public. Commit `Package.resolved`, because Xcode Cloud does not resolve package versions by itself.
- Private dependencies must be on a supported Git host, and Xcode Cloud asks for access to each of them (Manage Repositories > Additional).
- A remote compiler cache from [CI and caches](ci-and-cache.md) is possible through the scripts and secrets, but each action starts in a new environment, so measure whether it helps before keeping it.

## Compute hours and budget

- The Apple Developer Program includes **25 compute hours a month**. Paid plans seen on 2026-11-26: 100 hours for US$49.99, 250 for US$99.99, 1,000 for US$399.99 and 10,000 for US$3,999.99 a month.
- Hours count the time of each task, not wall time. Apple's example: 5 tests of 12 minutes each use one compute hour. Parallel test actions therefore use hours faster than the clock shows.
- Unused hours do not carry over.
- For one build, estimate its hours as the sum of its actions' durations, from the `startedDate` and `finishedDate` of `GET /v1/ciBuildRuns/{id}/actions`, and mark it as an estimate until the usage page confirms it.
- Read the usage in App Store Connect, under Users and Access > Xcode Cloud for the team or the app's Xcode Cloud tab, with CSV export. Record it in the tracker like any other spend, and plan the full matrix workflow so it fits the month's hours.

## Start and watch a build from a script

The person starts workflows in Xcode or App Store Connect. To let the agent start the full matrix workflow alone, use the App Store Connect API with an API key:

- The person creates a team API key in App Store Connect > Users and Access > Integrations, with a role that allows Xcode Cloud. The `.p8` file downloads once. Keep it where Apple's tools look for it, `~/.appstoreconnect/private_keys/AuthKey_<key id>.p8`, with mode 600.
- Put the key id and issuer id in the shell profile, such as `ASC_KEY_ID` and `ASC_ISSUER_ID`.
- Each request carries a JWT signed with ES256: header `kid` (key id) and `typ` `JWT`, payload `iss` (issuer id), `iat`, `exp` at most 20 minutes later, and `aud` `appstoreconnect-v1`.

| Step | Request |
| --- | --- |
| Find the workflow | `GET /v1/ciProducts`, then `GET /v1/ciProducts/{id}/workflows` |
| Start it | `POST /v1/ciBuildRuns` with the workflow relationship, optionally `sourceBranchOrTag` and `"clean": true` |
| Watch it | `GET /v1/ciBuildRuns/{id}`: `executionProgress` is `PENDING`, `RUNNING` or `COMPLETE`, then `completionStatus` is `SUCCEEDED`, `FAILED`, `ERRORED`, `CANCELED` or `SKIPPED` |
| Read each action | `GET /v1/ciBuildRuns/{id}/actions`, then `GET /v1/ciBuildActions/{id}/issues` and `/testResults` |
| Get the files | `GET /v1/ciBuildActions/{id}/artifacts`, then each artifact's `downloadUrl`, valid only for a short time. Types include `LOG_BUNDLE`, `RESULT_BUNDLE` and `TEST_PRODUCTS` |

The API reference lists no request that cancels a build run. Cancel one in Xcode or App Store Connect. If a start request times out, list the workflow's recent runs with `GET /v1/ciWorkflows/{id}/buildRuns` before starting again, so the matrix does not run twice.

An example in Python with uv. It starts the workflow, waits with a bound and downloads the log and result bundles:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyjwt[crypto]"]
# ///

import json
import os
import sys
import time
import urllib.request
from pathlib import Path

import jwt

API = "https://api.appstoreconnect.apple.com"


def make_token() -> str:
    key_id = os.environ["ASC_KEY_ID"]
    key_path = Path.home() / ".appstoreconnect" / "private_keys" / f"AuthKey_{key_id}.p8"
    now = int(time.time())
    claims = {"iss": os.environ["ASC_ISSUER_ID"], "iat": now, "exp": now + 900, "aud": "appstoreconnect-v1"}
    return jwt.encode(claims, key_path.read_text(), algorithm="ES256", headers={"kid": key_id, "typ": "JWT"})


def call(method: str, path: str, body: dict | None = None) -> dict:
    data = json.dumps(body).encode() if body else None
    headers = {"Authorization": f"Bearer {make_token()}", "Content-Type": "application/json"}
    request = urllib.request.Request(f"{API}{path}", data=data, headers=headers, method=method)

    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def start(workflow_id: str) -> str:
    workflow = {"data": {"type": "ciWorkflows", "id": workflow_id}}
    body = {"data": {"type": "ciBuildRuns", "attributes": {}, "relationships": {"workflow": workflow}}}
    return call("POST", "/v1/ciBuildRuns", body)["data"]["id"]


def wait(run_id: str, limit_minutes: int) -> dict:
    deadline = time.monotonic() + limit_minutes * 60

    while time.monotonic() < deadline:
        attributes = call("GET", f"/v1/ciBuildRuns/{run_id}")["data"]["attributes"]

        if attributes["executionProgress"] == "COMPLETE":
            return attributes

        time.sleep(120)

    raise TimeoutError(f"Build run {run_id} did not finish within {limit_minutes} minutes.")


def download(run_id: str, folder: Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    wanted = {"LOG_BUNDLE", "RESULT_BUNDLE"}

    for action in call("GET", f"/v1/ciBuildRuns/{run_id}/actions")["data"]:
        for artifact in call("GET", f"/v1/ciBuildActions/{action['id']}/artifacts")["data"]:
            details = artifact["attributes"]

            if details["fileType"] in wanted:
                urllib.request.urlretrieve(details["downloadUrl"], folder / details["fileName"])


def main() -> int:
    workflow_id = sys.argv[1]
    folder = Path(sys.argv[2]).resolve()
    run_id = start(workflow_id)
    print(f"Started build run {run_id}.", flush=True)
    result = wait(run_id, limit_minutes=180)
    download(run_id, folder)
    print(f"Build run {run_id}: {result['completionStatus']}.", flush=True)
    return 0 if result["completionStatus"] == "SUCCEEDED" else 1


if __name__ == "__main__":
    sys.exit(main())
```

It was checked for syntax, not run against the API. Before relying on it, run it once on a small workflow and compare its result with App Store Connect.

## Results

- Results show in Xcode's Report navigator and in App Store Connect (the app's Xcode Cloud tab, Builds). The e-mail notification links to both.
- Artifacts are kept for up to 30 days. Download the result bundles you need for the batch report within that time.
- Read the failed tests from the result bundle with `xcrun xcresulttool`, and send each line of work its own findings, as for any batch.

## Sources

Checked on 2026-11-26: [Xcode Cloud overview](https://developer.apple.com/xcode-cloud/), [getting started and plans](https://developer.apple.com/xcode-cloud/get-started/), [setting up a project](https://developer.apple.com/documentation/xcode/setting-up-your-project-to-use-xcode-cloud), [configuring the first workflow](https://developer.apple.com/documentation/xcode/configuring-your-first-xcode-cloud-workflow), [developing a workflow strategy](https://developer.apple.com/documentation/xcode/developing-a-workflow-strategy-for-xcode-cloud), [workflow reference](https://developer.apple.com/documentation/xcode/xcode-cloud-workflow-reference), [start conditions](https://developer.apple.com/documentation/xcode/configuring-start-conditions), [actions](https://developer.apple.com/documentation/xcode/configuring-your-xcode-cloud-workflow-s-actions), [custom build scripts](https://developer.apple.com/documentation/xcode/writing-custom-build-scripts), [environment variables](https://developer.apple.com/documentation/xcode/environment-variable-reference), [dependencies](https://developer.apple.com/documentation/xcode/making-dependencies-available-to-xcode-cloud), [usage data](https://developer.apple.com/documentation/xcode/reviewing-xcode-cloud-usage-data), [release notes](https://developer.apple.com/xcode-cloud/release-notes/), [App Store Connect API for Xcode Cloud](https://developer.apple.com/documentation/appstoreconnectapi/xcode-cloud-workflows-and-builds) and [API tokens](https://developer.apple.com/documentation/appstoreconnectapi/generating-tokens-for-api-requests). The maximum run time per action, concurrency limits and the exact key role were not stated in the docs. See [sources](sources.md) for the full record.
