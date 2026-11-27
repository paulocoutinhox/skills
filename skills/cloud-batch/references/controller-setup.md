# Controller setup: tools, keys and checks

Read this before the first batch on a new controller, the machine that drives the batches, and whenever a credential fails. Keys stay where they normally live, and each CLI signs in the standard way. Install commands and variable names were checked on **2026-11-26** against the docs in [the sources](sources.md).

## Where keys live

| What | macOS and Linux | Windows |
| --- | --- | --- |
| Secret values | `export NAME=value` lines in the shell profile the person already uses: `~/.zshrc` (macOS default) or `~/.bashrc` (most Linux). On Ubuntu and Debian, put them at the top of `~/.bashrc`, above the lines that stop a non-interactive shell, or they never load in the agent's commands. `chmod 600` on that file is a good habit | User environment variables, set in System Properties > Environment Variables. New terminals see them |
| SSH keys | `~/.ssh`, mode 600, with `~/.ssh/config` entries for hosts used often | `%USERPROFILE%\.ssh` |
| gcloud and az sign-ins | Their own config folders, after `gcloud auth login` and `az login` | The same |

Rules, each with its reason:

- **Load the profile inside each command,** such as `zsh -c 'source ~/.zshrc >/dev/null 2>&1; aws sts get-caller-identity'` on macOS or `bash -c 'source ~/.bashrc >/dev/null 2>&1; aws sts get-caller-identity'` on Linux. An agent's shell snapshot can hold stale values, and that once gave expired keys.
- **Secrets go nowhere else:** no script, log, repository, image, tracker, memory or chat message. Every copy is one more place to leak.
- **Never print a secret:** no `env`, `printenv` or `set -x` while secrets are loaded. Logs and chat keep what is printed.
- **Never put a secret on a command line,** because `ps` shows it to every user of the machine. Use a variable the tool reads by itself, or stdin. The one exception is the random, single-use admin password of `az vm create` (see [Azure](azure.md)). Presigned URLs count as secrets too.
- **Prefix variables by project,** such as `PROJECT_R2_KEY_ID` with `PROJECT` replaced by the project's name, so two projects never mix credentials.
- **Record names only** in the tracker and the agent's memory, never values.
- **Never commit the profile** or sync it to a public dotfiles repository while it holds secrets.

## Tools on the controller

| Tool | macOS | Linux (Debian or Ubuntu) | Windows |
| --- | --- | --- | --- |
| Git | `xcode-select --install`, or `brew install git` | `sudo apt install git` | `winget install --id Git.Git -e` |
| OpenSSH client | Built in | `sudo apt install openssh-client` | A feature on demand: check with `Get-WindowsCapability -Online \| Where-Object Name -like 'OpenSSH*'`, add with `Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0` |
| rsync | Built in, or `brew install rsync` | `sudo apt install rsync` | Not part of Windows. Use `scp`, or rsync in WSL 2 |
| jq | `brew install jq` | `sudo apt install jq` | `winget install --id jqlang.jq -e` |
| zstd | `brew install zstd` | `sudo apt install zstd` | `winget install --id Meta.Zstandard -e` |
| uv | `brew install uv` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` | `winget install --id=astral-sh.uv -e` |
| sccache | `brew install sccache` | A pinned release binary | `winget install --id Mozilla.sccache -e` |
| Docker | Docker Desktop | Docker Engine | Docker Desktop with WSL 2 |
| GitHub CLI | `brew install gh` | GitHub's apt repository, then `sudo apt install gh` | `winget install --id GitHub.cli --source winget` |

curl and OpenSSL are built into macOS and most Linux images. On Windows, curl is built in and OpenSSL comes with Git for Windows. The scripts are Python run with uv, so they run on every controller.

## AWS

**Install AWS CLI v2:**

- macOS: the official package, `curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"` then `sudo installer -pkg AWSCLIV2.pkg -target /`. Homebrew's `awscli` also works, but AWS does not maintain it.
- Linux: `curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"`, `unzip awscliv2.zip`, `sudo ./aws/install`. Use `awscli-exe-linux-aarch64.zip` on arm64.
- Windows: `msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi`, or `winget install --id Amazon.AWSCLI -e`.

**Variables** of a dedicated IAM user for the batches: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_REGION`, such as `us-east-1`. AWS CLI v2 reads `AWS_REGION` before `AWS_DEFAULT_REGION`. Device Farm runs only in `us-west-2`, so its commands pass `--region us-west-2`.

Run `unset AWS_PROFILE` in each command. An empty `AWS_PROFILE` fails with "The config profile () could not be found".

**Permissions** of the IAM user, never administrator rights:

- EC2 instances, key pairs, security groups, images, snapshots and tags (`ec2:CreateTags`);
- dedicated hosts (`ec2:AllocateHosts`, `ec2:ReleaseHosts`, `ec2:DescribeHosts`), only for a cloud Mac day;
- `ssm:GetParameter` and `ssm:GetParameters` on the public `/aws/service/*` parameters, for AMI ids and `resolve:ssm:`;
- `s3:GetObject` on the `ec2-linux-nvidia-drivers` and `ec2-windows-nvidia-drivers` buckets, only for GPU machines;
- `ce:GetCostAndUsage`;
- the Device Farm actions the runs use;
- `servicequotas:Get*` and `servicequotas:List*`, plus `servicequotas:RequestServiceQuotaIncrease` only if the person wants the agent to file requests.

Turn on MFA for the console sign-in and rotate the access keys.

**Checks:**

- `aws sts get-caller-identity` shows the account and the user.
- `aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A` shows the on-demand standard vCPU quota. The other codes are in [budget and quotas](budget-and-quotas.md#quotas-ask-early).

## Google Cloud

From the docs only. The projects behind this skill never ran Google Cloud.

**Install the Google Cloud CLI:**

- macOS: Google's archive (`google-cloud-cli-darwin-arm.tar.gz` or `google-cloud-cli-darwin-x86_64.tar.gz`), unpacked, then `./google-cloud-sdk/install.sh`. Homebrew's cask is `gcloud-cli`, which Google does not maintain.
- Linux: Google's apt repository, then `sudo apt-get install google-cloud-cli`.
- Windows: Google's `GoogleCloudSDKInstaller.exe`, or `winget install --id Google.CloudSDK -e`.

**Sign in** with `gcloud auth login`. gcloud keeps the token in its own config folder.

**Variables:** gcloud reads properties from `CLOUDSDK_<SECTION>_<PROPERTY>` variables, such as `CLOUDSDK_CORE_PROJECT`, `CLOUDSDK_COMPUTE_REGION` and `CLOUDSDK_COMPUTE_ZONE`.

**Roles:** `roles/compute.instanceAdmin.v1` for instances, disks and images, `roles/compute.securityAdmin` for firewall rules, `roles/compute.osAdminLogin` for SSH through OS Login, and billing read access for spend checks.

**Enable the Compute API once,** with the person's go: `gcloud services enable compute.googleapis.com`.

**Checks:** `gcloud auth list`, `gcloud config list` and `gcloud compute zones list --limit=1`.

## Azure

**Install the Azure CLI:**

- macOS: `brew update && brew install azure-cli`.
- Linux (Debian or Ubuntu): `curl -fsSL 'https://azurecliprod.blob.core.windows.net/$root/deb_install.sh' | sudo bash`, or Microsoft's apt repository step by step.
- Windows: `winget install --exact --id Microsoft.AzureCLI`.

Add extensions when needed: `az extension add --name quota`.

**Sign in** with `az login`. az keeps a refreshable token in `~/.azure` (`%USERPROFILE%\.azure` on Windows), so the agent can work alone afterwards. Then `az account set --subscription <id>`.

**Register the providers once,** with the person's go: `az provider register --namespace Microsoft.Compute`, then `Microsoft.Network` and `Microsoft.Quota`.

**Roles:** Contributor on the batch resource group only, plus Reader and Cost Management Reader on the subscription, for quota usage and spend. Registering providers and raising quotas work at subscription scope, so the person does them, or grants the Quota Request Operator role for quota requests.

**Checks:** `az account show`, then `az vm list-usage --location <region> -o table` for the quotas.

## Other services

- **Cache bucket, such as Cloudflare R2:** `PROJECT_R2_ENDPOINT` (`https://<account id>.r2.cloudflarestorage.com`), `PROJECT_R2_KEY_ID` and `PROJECT_R2_SECRET`, from an R2 API token with **Object Read & Write** limited to that bucket alone. The scripts map them to sccache's variables only inside the build's environment (see [CI and caches](ci-and-cache.md)).
- **GitHub:** `gh auth login`, or `GH_TOKEN` in the profile, for starting workflows and reading runs. CI secrets live in the repository's secrets, never in a workflow file.
- **Apple:** Xcode and its Command Line Tools, the team id in a variable such as `APPLE_TEAM`, and the signing identities in the login keychain. To start Xcode Cloud workflows from a script, an App Store Connect API key: the `.p8` file in `~/.appstoreconnect/private_keys/` with mode 600, and `ASC_KEY_ID` and `ASC_ISSUER_ID` in the profile (see [Xcode Cloud](xcode-cloud.md#start-and-watch-a-build-from-a-script)).
- **Android:** the SDK with platform tools, the emulator and a system image, `ANDROID_HOME` pointing at the SDK (do not use the deprecated `ANDROID_SDK_ROOT`) and `JAVA_HOME` at a JDK that the project's Gradle supports.
- **The person's own machines:** the controller's public key on the remote machine, then `ssh -o BatchMode=yes <user>@<host>`. On Windows, an account in the Administrators group uses `C:\ProgramData\ssh\administrators_authorized_keys`, limited to Administrators and SYSTEM with `icacls.exe "$env:ProgramData\ssh\administrators_authorized_keys" /inheritance:r /grant "Administrators:F" /grant "SYSTEM:F"`. A password is a last resort for a machine that cannot take a key, kept in the profile like other secrets and never used on a command line.

## Checks for the other services

Run the checks of every service the plan uses:

| Service | Check |
| --- | --- |
| AWS Device Farm | `aws devicefarm list-projects --region us-west-2` |
| Google Device Run | `gcloud beta device-run devices list`, and `gcloud alpha device-run devices list` when iOS runs are planned |
| Xcode Cloud | `GET /v1/ciProducts` with the API key's token (see [Xcode Cloud](xcode-cloud.md#start-and-watch-a-build-from-a-script)) |
| GitHub | `gh auth status` |
| Cache bucket | `sccache --start-server` then `sccache --show-stats` with the bucket variables set. Its `Cache location` line names the bucket in use, and a wrong key fails at start |
| Own machines | `ssh -o BatchMode=yes <user>@<host> true` for each one |

## Letting the agent act alone

- **Suggest an allow list** for the person to approve in their agent client: the read-only and launch commands (`aws ec2 describe-*`, `aws ce get-cost-and-usage`, `aws devicefarm list-*` and `get-*`, `az vm show`, `gcloud compute instances list`, `gh run list` and `gh run view`), the batch scripts, and `ssh`, `scp` and `rsync` to the batch hosts. Never edit those settings without the person's request.
- **Deletions go only through the scripts,** which delete by tag and prove the result.
- **First run:** run every check above for the providers in the plan, list what is missing with the exact install step for the person's system, and stop until every check passes. No batch starts with an unchecked credential.
- **A credential failure** such as "ExpiredToken", "AuthorizationFailed" or "invalid_grant" stops the batch. Tell the person which variable or sign-in to renew. Never retry in a loop, and never ask for the secret in the chat.

## Sources

Checked on 2026-11-26: [AWS CLI install](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), [AWS CLI environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html), [Google Cloud CLI install](https://docs.cloud.google.com/sdk/docs/install), [gcloud properties](https://docs.cloud.google.com/sdk/docs/properties), [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam), [Azure CLI on Linux](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt), [Azure CLI sign-in](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli), [Azure built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles), [OpenSSH for Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse), [OpenSSH key management](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement), [uv install](https://docs.astral.sh/uv/getting-started/installation/), [GitHub CLI environment](https://cli.github.com/manual/gh_help_environment), [R2 API tokens](https://developers.cloudflare.com/r2/api/tokens/) and [Android environment variables](https://developer.android.com/tools/variables). Winget ids were checked in [winget-pkgs](https://github.com/microsoft/winget-pkgs). See [sources](sources.md) for the full record.
