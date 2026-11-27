# Sources, experience and research limits

Two kinds of knowledge are in this skill, and the references keep them apart:

- **Practice:** lessons from long multi-platform C++ projects that ran batches on local machines, AWS, Azure, AWS Device Farm and the person's own devices. The mistakes, measured durations, memory peaks and device behavior come from those runs. No project names, hosts, accounts or credentials are kept.
- **Docs:** every provider command, price, limit and variable name was checked against the official pages below on **2026-11-26**. Google Cloud comes from the docs only and was never run.

No provider command, paid run or device run was made while writing. The dates record this editorial check. They do not promise that prices or limits stay the same. Only maintenance the user asks for changes the stored facts.

## AWS EC2 and account services

| Source | Used for |
| --- | --- |
| [SpotMarketOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotMarketOptions.html), [interruption behavior](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interruption-behavior.html) | One-time spot with terminate, no maximum price |
| [Instance-initiated shutdown](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_ChangingInstanceInitiatedShutdownBehavior.html) | `shutdown` terminates, `halt` does not |
| [Key pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html) | ed25519 for Linux only, tags on key pairs |
| [Nested virtualization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nested-virtualization.html) | `NestedVirtualization=enabled`, supported families, Android emulator use |
| [EC2 error codes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html), [spot limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-limits.html), [instance quotas](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-quotas.html) | Fallback errors, quota names, codes and defaults |
| [describe-spot-price-history](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-spot-price-history.html) | Zone price ordering |
| [Ubuntu images on AWS](https://ubuntu.com/aws/docs/aws-how-to/instances/find-ubuntu-images/), [SSM parameters for AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-systems-manager-parameter-to-find-AMI.html) | The public parameter path and `resolve:ssm:` |
| [gp3 volumes](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html) | Baseline and limits of IOPS and throughput |
| [Deregister an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/deregister-ami.html) | `--delete-associated-snapshots` |
| [GetCostAndUsage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostAndUsage.html), [Cost Explorer pricing](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/pricing/), [Cost Explorer data](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-exploring-data.html) | Exclusive end date, US$0.01 per request, data up to the previous day |
| [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html), [Budgets pricing](https://aws.amazon.com/aws-cost-management/aws-budgets/pricing/) | Alerts are delayed and free |
| [EC2 Mac](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html), [stopping a Mac](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mac-instance-stop.html) | 24-hour minimum, families, scrubbing time |
| [EC2 pricing](https://aws.amazon.com/ec2/pricing/), [VPC pricing](https://aws.amazon.com/vpc/pricing/) | Per-second billing, Mac host prices, c8i and g4dn on-demand prices, US$0.005 per public IPv4 hour |
| [Spot interruption notices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-instance-termination-notices.html) | Two-minute best-effort warning |
| [NVIDIA GRID drivers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nvidia-GRID-driver.html) | The driver buckets and supported families |
| [ECS setup guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/get-set-up-for-amazon-ecs.html) | `checkip.amazonaws.com` for the caller's `/32` |
| [authorize-security-group-ingress](https://docs.aws.amazon.com/cli/latest/reference/ec2/authorize-security-group-ingress.html) | SSH rule syntax and where tags apply |
| [AWS CLI environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html), [install](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) | Variable names, `AWS_REGION` order, install commands |

## AWS Device Farm

| Source | Used for |
| --- | --- |
| [Developer guide](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html), [endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/devicefarm.html) | `us-west-2`, concurrency, 150-minute limits, upload size, retention |
| [Pricing](https://aws.amazon.com/device-farm/pricing/) | Device minute, slot, trial and desktop browser prices |
| [Create a run](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-create-test-run.html), [schedule-run](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/schedule-run.html), [CreateUpload](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateUpload.html), [Upload](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Upload.html), [Run](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Run.html), [StopRun](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_StopRun.html), [DeleteProject](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeleteProject.html) | The self-cleaning run, statuses and results, billing of stopped runs |
| [ListDevices](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListDevices.html), [virtual devices](https://docs.aws.amazon.com/devicefarm/latest/developerguide/virtual-devices.html) | Filters, availability values, physical and virtual devices |
| [XCTest UI](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-ios-xctest-ui.html), [custom environment hosts](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-hosts.html), [test spec](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environment-test-spec.html), [variables](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environment-variables.html) | IPA layouts, re-signing, hosts, `DEVICEFARM_*` variables |
| [Desktop browser testing](https://docs.aws.amazon.com/devicefarm/latest/testgrid/what-is-testgrid.html) | Selenium desktop browsers |

## Azure

| Source | Used for |
| --- | --- |
| [NGads V620 series](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/ngadsv620-series), [Azure Retail Prices API](https://prices.azure.com/api/retail/prices) | Size facts, regions, Linux, Windows and spot prices, disk and IP prices |
| [AMD driver setup for Windows](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/n-series-amd-driver-setup), [AMD GPU extension](https://learn.microsoft.com/en-us/azure/virtual-machines/extensions/hpccompute-amd-gpu-windows), [Linux AMD driver](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/azure-n-series-amd-gpu-driver-linux-installation-guide) | Driver paths and the extension's conflicting notes |
| [Trusted launch](https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch), [multitenant hosting rights](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/windows-desktop-multitenant-hosting-deployment) | Trusted launch flags, Windows 11 license rights |
| [States and billing](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing), [az vm](https://learn.microsoft.com/en-us/cli/azure/vm) | Deallocate against stop, power state codes, auto-shutdown |
| [Run Command](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/run-command) | Runs as SYSTEM, output and time limits |
| [Public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses), [NIC IP config](https://learn.microsoft.com/en-us/cli/azure/network/nic/ip-config), [NSG rules](https://learn.microsoft.com/en-us/cli/azure/network/nsg/rule) | IP and rule commands and defaults |
| [Cost Management Query API](https://learn.microsoft.com/en-us/rest/api/cost-management/query/usage), [budgets tutorial](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets) | Spend queries and budgets |
| [az quota](https://learn.microsoft.com/en-us/cli/azure/quota), [Spot VMs](https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms), [Dv5](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dv5-series), [Network Watcher](https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-create) | Quota updates, spot, nested virtualization, automatic Network Watcher |
| [OpenSSH for Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse), [key management](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement) | Server install and administrators' keys |
| [Automatic logon](https://learn.microsoft.com/en-us/troubleshoot/windows-server/user-profiles-and-logon/turn-on-automatic-logon), [Autologon](https://learn.microsoft.com/en-us/sysinternals/downloads/autologon), [Privacy CSP](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-privacy), [Experience CSP](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-experience) | Autologon values, the LSA secret and the policies with their editions |
| [schtasks create](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks-create), [Set-WinUserLanguageList](https://learn.microsoft.com/en-us/powershell/module/international/set-winuserlanguagelist), [input locales](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/default-input-locales-for-windows-language-packs), [Dev Drive](https://learn.microsoft.com/en-us/windows/dev-drive/) | Interactive tasks, language lists, IME ids, Dev Drive |
| [Azure CLI install](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt), [built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles) | Install commands and role names |

## Google Cloud (docs only)

| Source | Used for |
| --- | --- |
| [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot), [limit VM run time](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime), [instances create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) | Spot, termination action, time limit, notice |
| [G-series GPU VMs](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-g-series), [N1 GPU VMs](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-general-purpose) | GPU flags and maintenance policy |
| [Nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview) | Supported series and limits |
| [Custom images](https://docs.cloud.google.com/compute/docs/images/create-custom), [labels](https://docs.cloud.google.com/compute/docs/labeling-resources), [firewall rules create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create), [OS Login](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin) | Images, labels, firewall syntax, expiring keys |
| [VM pricing](https://cloud.google.com/compute/vm-instance-pricing), [Spot pricing](https://cloud.google.com/spot-vms/pricing), [network pricing](https://cloud.google.com/vpc/network-pricing), [disk and image pricing](https://cloud.google.com/compute/disks-image-pricing) | Billing granularity and prices |
| [Budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets), [BigQuery export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) | Alerts and spend queries |
| [OS details](https://docs.cloud.google.com/compute/docs/images/os-details), [gcloud properties](https://docs.cloud.google.com/sdk/docs/properties), [install](https://docs.cloud.google.com/sdk/docs/install) | No Windows client images, `CLOUDSDK_*` variables, install |
| [Test Lab deprecation FAQ](https://firebase.google.com/docs/test-lab/migrate-faq), [Developer Device Platform](https://cloud.google.com/products/developer-device-platform) | Test Lab shutdown date and its Preview replacement |

## Xcode Cloud and Device Run (docs only), GitHub-hosted runners

| Source | Used for |
| --- | --- |
| [Xcode Cloud overview](https://developer.apple.com/xcode-cloud/), [plans](https://developer.apple.com/xcode-cloud/get-started/), [usage data](https://developer.apple.com/documentation/xcode/reviewing-xcode-cloud-usage-data) | Included hours, paid plans, how hours count |
| [Setting up a project](https://developer.apple.com/documentation/xcode/setting-up-your-project-to-use-xcode-cloud), [first workflow](https://developer.apple.com/documentation/xcode/configuring-your-first-xcode-cloud-workflow), [workflow strategy](https://developer.apple.com/documentation/xcode/developing-a-workflow-strategy-for-xcode-cloud) | Requirements, repository hosts, roles, Integrate menu |
| [Workflow reference](https://developer.apple.com/documentation/xcode/xcode-cloud-workflow-reference), [start conditions](https://developer.apple.com/documentation/xcode/configuring-start-conditions), [actions](https://developer.apple.com/documentation/xcode/configuring-your-xcode-cloud-workflow-s-actions) | Workflow parts, two test phases, secrets |
| [Custom build scripts](https://developer.apple.com/documentation/xcode/writing-custom-build-scripts), [environment variables](https://developer.apple.com/documentation/xcode/environment-variable-reference), [dependencies](https://developer.apple.com/documentation/xcode/making-dependencies-available-to-xcode-cloud) | `ci_scripts` names and limits, variables, packages |
| [Xcode Cloud release notes](https://developer.apple.com/xcode-cloud/release-notes/) | The visionOS test known issue, address ranges |
| [Xcode Cloud API](https://developer.apple.com/documentation/appstoreconnectapi/xcode-cloud-workflows-and-builds), [API tokens](https://developer.apple.com/documentation/appstoreconnectapi/generating-tokens-for-api-requests) | Build runs, actions, artifacts, JWT claims |
| [WWDC22 session 110361](https://developer.apple.com/videos/play/wwdc2022/110361/) | Parallel platforms, fresh simulators, test plan timeouts |
| [GitHub-hosted runners](https://docs.github.com/en/actions/reference/runners/github-hosted-runners), [larger runners](https://docs.github.com/en/actions/reference/runners/larger-runners), [runner pricing](https://docs.github.com/en/billing/reference/actions-runner-pricing), [limits](https://docs.github.com/en/actions/reference/limits), [runner-images](https://github.com/actions/runner-images) | Labels, hardware, prices, 6-hour jobs, concurrency, Xcode versions, no nested virtualization on Apple silicon |
| [Device Run Android](https://docs.cloud.google.com/developer-device-platform/device-run/android-instrument), [Device Run iOS](https://docs.cloud.google.com/developer-device-platform/device-run/ios), [quickstart](https://docs.cloud.google.com/developer-device-platform/quickstart), [gcloud release notes](https://docs.cloud.google.com/sdk/docs/release-notes) | Commands, tracks, roles, `--target-app`, result bucket |

## Caches, CI and tools

| Source | Used for |
| --- | --- |
| [sccache S3](https://github.com/mozilla/sccache/blob/main/docs/S3.md), [configuration](https://github.com/mozilla/sccache/blob/main/docs/Configuration.md), [v0.14.0 release](https://github.com/mozilla/sccache/releases/tag/v0.14.0) | Variables, R2 settings, `SCCACHE_BASEDIRS` |
| [R2 pricing](https://developers.cloudflare.com/r2/pricing/), [lifecycles](https://developers.cloudflare.com/r2/buckets/object-lifecycles/), [API tokens](https://developers.cloudflare.com/r2/api/tokens/) | Prices, no egress fee, expiry rules, bucket-scoped tokens |
| [CMAKE_LANG_COMPILER_LAUNCHER](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_COMPILER_LAUNCHER.html), [JOB_POOLS](https://cmake.org/cmake/help/latest/prop_gbl/JOB_POOLS.html) | Launcher generators, link pools |
| [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions), [secure use](https://docs.github.com/en/actions/reference/security/secure-use), [gh environment](https://cli.github.com/manual/gh_help_environment) | Per-minute rates, self-hosted runners and public repositories, `GH_TOKEN` |
| [Xcode Cloud](https://developer.apple.com/xcode-cloud/), [macOS Tahoe license](https://www.apple.com/legal/sla/docs/macOSTahoe.pdf) | 25 included hours, macOS virtualization and leasing terms |
| [uv install](https://docs.astral.sh/uv/getting-started/installation/), [Android variables](https://developer.android.com/tools/variables) | uv install commands, `ANDROID_HOME` |
| [Emulator command line](https://developer.android.com/studio/run/emulator-commandline), [emulator console](https://developer.android.com/studio/run/emulator-console), [ADB](https://developer.android.com/tools/adb), [permission controller layout](https://android.googlesource.com/platform/packages/modules/Permission/+/refs/heads/main/PermissionController/res/layout/grant_permissions.xml) | Headless flags and GPU modes, console sensors, shell commands, button ids |
| [Vulkan loader architecture](https://github.com/KhronosGroup/Vulkan-Loader/blob/main/docs/LoaderInterfaceArchitecture.md), [running Weston](https://wayland.pages.freedesktop.org/weston/toc/running-weston.html) | `VK_DRIVER_FILES`, Weston backends and idle time |
| [SwiftShader in Chrome](https://chromium.googlesource.com/chromium/src/+/main/docs/gpu/swiftshader.md), [GPU in headless Chrome](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/docs/gpu/using-gpu-hardware-in-headless-chrome.md) | Software WebGL opt-in, `--enable-gpu` |
| [Preparing for iPhone Duo](https://developer.apple.com/documentation/technologyoverviews/preparing-your-app-for-iphone-duo) | Device Hub sets the fold posture, Xcode 27.1 |
| [actions/runner-images issue 9491](https://github.com/actions/runner-images/issues/9491) | The `vm.mmap_rnd_bits=28` sanitizer workaround |
| [botocore issue 3110](https://github.com/boto/botocore/issues/3110) | The empty `AWS_PROFILE` error, which no AWS page documents |

## General tool references

These pages describe well-known commands that the references use. They were opened on 2026-11-26 to confirm that the links resolve and name the commands used. They were not the subject of a separate fact check.

| Source | Used for |
| --- | --- |
| [git bundle](https://git-scm.com/docs/git-bundle), [git worktree](https://git-scm.com/docs/git-worktree) | Bundles, `verify`, `list-heads`, fresh worktrees |
| [Ninja manual](https://ninja-build.org/manual.html), [CMAKE_JOB_POOL_LINK](https://cmake.org/cmake/help/latest/variable/CMAKE_JOB_POOL_LINK.html) | `-k 0`, link pools |
| [uv scripts](https://docs.astral.sh/uv/guides/scripts/) | The inline `requires-python` header of the examples |
| [GCC overall options](https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html), [Clang command line](https://clang.llvm.org/docs/ClangCommandLineReference.html) | `-ffile-prefix-map`, `-fsyntax-only` and warning flags |
| [flock](https://man7.org/linux/man-pages/man1/flock.1.html) | The Linux build lock |
| [workflow_dispatch](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows), [gh run](https://cli.github.com/manual/gh_run) | Manual runs and watching them |
| [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam), [Azure CLI sign-in](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli) | Roles and standard sign-in |
| [XCUIAutomation](https://developer.apple.com/documentation/xcuiautomation), [GCVirtualController](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller), [UI Automator](https://developer.android.com/training/testing/other-components/ui-automator), [UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Test frameworks named in device testing |
| [SendInput](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-sendinput), [ChangeDisplaySettings](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-changedisplaysettingsw), [Install-Language](https://learn.microsoft.com/en-us/powershell/module/languagepackmanagement/install-language), [protecting the autologon password](https://learn.microsoft.com/en-us/windows/win32/secauthn/protecting-the-automatic-logon-password) | Windows desktop session details |
| [Microsoft console host source](https://github.com/microsoft/terminal) | The undocumented `conhost.exe --headless` switch |

Apple command names (`simctl`, `devicectl`, `xcodebuild`, `automationmodetool`) and XCUITest API availability were read from the help text, man pages and SDK headers of Xcode 27.2.

## Unresolved limits

- Device Farm's public pages name no device models. The phones named in [Device Farm](device-farm.md) come from practice and must be confirmed with `list-devices`.
- `am stack remove`, `appops ... android:mock_location`, the `immersive_mode_confirmations` setting and `conhost.exe --headless` are not in the public docs. They worked in practice, and the references say to check them on the target version.
- Azure does not document whether auto-shutdown deallocates, or a per-second billing rule for current sizes. The scripts deallocate and check explicitly.
- Microsoft's driver pages disagree on whether the AMD extension supports NGads V620. Both paths are given.
- The g4dn Windows price and the D2s_v5 price come from practice and were not rechecked.
- The SwiftShader 4 and 5 versions of the emulator images, the `notificationSourcesDidInstall` log record and `--idle-time=0` disabling Weston's idle timeout come from practice, not from docs.
- AWS publishes no current spot price list, so spot prices come from `describe-spot-price-history` on the day.
- Xcode Cloud's docs state no maximum run time per action, no concurrency limit and no exact API key role for starting builds, and list no API request that cancels a build. The Xcode Cloud example script was checked for syntax, not run.
- Device Run prices come from search extracts of a product page that did not render, and the service is in Preview.
- Apple's Xcode Cloud pages were read through Apple's own Markdown and JSON versions of the same pages, since the HTML pages need JavaScript.
