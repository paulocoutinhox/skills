# Azure: the persistent Windows GPU VM, Linux GPU and spot

Read this when the plan uses Azure. The persistent Windows VM pattern ran in practice, and the commands were rechecked on **2026-11-26** against Microsoft Learn and the Azure Retail Prices API (see [sources](sources.md)). Where the docs and practice disagree, both are stated. Sign-in and roles are in [controller setup](controller-setup.md).

## Why a persistent, deallocated VM

A Windows GPU machine takes long to prepare: drivers, Build Tools, SDKs, the OpenSSH server and autologon. So it is created once, prepared once, and deallocated between batches. A deallocated VM bills only its disks, and the OS disk is Standard HDD, so it waits for a few dollars a month.

## One-time creation

- **A resource group of its own,** tagged, holding the VM and its network.
- **Size example:** `Standard_NG8ads_V620_v1`, a quarter of an AMD Radeon PRO V620, with 8 vCPU and 16 GiB. It was the cheapest GPU size the subscription had quota for. Prices seen in East US 2: US$0.635 an hour for Linux and US$1.003 an hour with the Windows Server license included. The size is not offered in every region (East US 2, West US 3, Central US, West Europe, Sweden Central, UK South and Japan East had it), so check the region first. It does not support nested virtualization.
- **Windows 11** needs an image from `MicrosoftWindowsDesktop` and `--license-type Windows_Client`, which states that the person holds eligible rights (see [licensing](budget-and-quotas.md#licensing)). With those rights, the VM ran at about the Linux price in practice. Microsoft's multitenant hosting page lists Windows 11 Enterprise as the supported edition, so match the image to the rights. Without the rights, use a Windows Server image at the Windows price. List the current images with `az vm image list --publisher MicrosoftWindowsDesktop --offer windows-11 --all -o table`.
- **Trusted launch** with secure boot and vTPM. It worked in practice on this size, though the Trusted Launch size table does not list the NG family. Check it at creation.
- **OS disk:** Standard HDD (`Standard_LRS`). A 128 GiB S10 disk was US$5.888 a month, and it bills while the VM is deallocated. Builds run on the size's temporary SSD, whose data can be lost on a stop, a redeploy or maintenance, so it holds nothing that must survive.
- **No public IP** while deallocated. A Standard public IP bills US$0.005 an hour while it exists, attached or not.

Then create the VM:

```bash
az vm create -g <group> -n <vm> --image <Windows 11 image URN> --size Standard_NG8ads_V620_v1 --license-type Windows_Client --security-type TrustedLaunch --enable-secure-boot true --enable-vtpm true --storage-sku Standard_LRS --public-ip-address "" --nsg-rule NONE --admin-username <user> --admin-password "$ADMIN_PASSWORD" --tags <project>-batch=persistent
```

`--nsg-rule NONE` stops Azure from adding its default rule that opens RDP to any address, which would also take priority 1000 from the SSH rule below. The admin password is the one secret that goes on a command line, because `az vm create` takes it there. So it is random (`ADMIN_PASSWORD=$(openssl rand -base64 30)`), used for this one call, unset right after, and replaced by the setup script.

**GPU driver:** the project installed it with `az vm extension set --resource-group <group> --vm-name <vm> --name AmdGpuDriverWindows --publisher Microsoft.HpcCompute`. Microsoft's driver page is inconsistent about this size: one note lists it, while its V620 section says the extension does not support NGads V620 during preview and gives a manual install of the AMD package. If the extension fails, install the driver version that page names for the size.

## Setup through Run Command, as SYSTEM

`az vm run-command invoke -g <group> -n <vm> --command-id RunPowerShellScript --scripts @setup.ps1` runs a script as SYSTEM. It returns only the last 4,096 bytes of output, runs at most 90 minutes, runs one script at a time and cannot be cancelled, so split long setup into steps that write their own logs. The setup steps:

- **OpenSSH server, key only:** `Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0`, `Set-Service -Name sshd -StartupType Automatic`, the key in `C:\ProgramData\ssh\administrators_authorized_keys` limited to Administrators and SYSTEM, and `PasswordAuthentication no` in `C:\ProgramData\ssh\sshd_config`.
- **The Windows firewall rule for SSH open on every network profile,** because Windows treats Azure networks as public. The NSG limits the source address.
- **Tools,** each download checked against its published SHA-256: Build Tools with the C++ workload, Git, CMake, Perl, NASM, Ninja, sccache, uv (which runs the batch runner) and the graphics debug layers.
- **Autologon of the batch user,** with the password stored only as the LSA secret (see [Windows desktop tests](windows-desktop.md)).

## Each batch

1. `az vm start -g <group> -n <vm>`.
2. `az vm auto-shutdown -g <group> -n <vm> --time <UTC HHMM>`, set to the estimate plus a margin.
3. Create a Standard static public IP and attach it: `az network public-ip create -g <group> -n <session>-ip --sku Standard --allocation-method Static --tags <project>-batch=<session>`, then `az network nic ip-config update -g <group> --nic-name <nic> -n ipconfig1 --public-ip-address <session>-ip`.
4. Add the SSH rule from the caller's address: `az network nsg rule create -g <group> --nsg-name <nsg> -n <session>-ssh --priority 1000 --source-address-prefixes <caller ip>/32 --destination-port-ranges 22 --access Allow --protocol Tcp`. Set the port and protocol explicitly, since their defaults are 80 and `*`.
5. Wait for SSH, with a bound.
6. Run the jobs.
7. Clean the build folders and temporary files.
8. `az vm deallocate -g <group> -n <vm>`. A plain `az vm stop` keeps billing compute.
9. Detach and delete the IP: `az network nic ip-config update -g <group> --nic-name <nic> -n ipconfig1 --remove publicIpAddress`, then `az network public-ip delete -g <group> -n <session>-ip`. Delete the rule with `az network nsg rule delete -g <group> --nsg-name <nsg> -n <session>-ssh`.
10. Prove it: `az vm get-instance-view -g <group> -n <vm> --query "instanceView.statuses[?starts_with(code,'PowerState/')].code" -o tsv` prints `PowerState/deallocated`, and `az resource list -g <group> -o table` shows only the expected resources.

The docs do not say whether auto-shutdown deallocates, so step 8 always runs and step 10 always checks.

Leave the Network Watcher that Azure creates by itself in `NetworkWatcherRG`. It adds no charge. Delete everything else a session created.

## Tests that need a desktop

Swapchain, OpenGL window and UI tests need a signed-in desktop. SSH sessions have none. So they run in the autologon console session through a scheduled task, and SSH only builds the programs and reads the logs. See [Windows desktop tests](windows-desktop.md).

Schedule Windows updates outside batch times, and let the VM update when it starts between batches.

## Linux on the AMD V620

- Microsoft supports Ubuntu 24.04 with a `6.8.*-azure` kernel and an OS disk of at least 100 GB for this size. The AMD driver extension does not support it on Linux, so the driver is installed by hand.
- The details that came up in practice are in [Linux GPU and browsers](linux-gpu-and-browsers.md#amd-on-azure-ng-v620-linux).

## Spot VMs

Azure Spot VMs suit Linux batches: `az vm create ... --priority Spot --eviction-policy Deallocate --max-price -1`. With `-1`, the VM is never evicted for price and never billed above the standard rate. Eviction comes with up to 30 seconds of notice through Scheduled Events. A deallocated Spot VM still bills its disks and counts against quota. The persistent Windows VM stays a regular VM, because it must not vanish in the middle of a batch.

## Smaller Azure sizes

- **Android emulator:** use a size whose page lists nested virtualization as supported, such as the Dv5 and Ev5 series, with enough cores and memory for the emulator.
- **Windows UI tests with software rendering (WARP):** a small size without a GPU, such as D2s_v5, is enough. About US$0.15 to 0.20 an hour was seen in practice. Read the current price.

## GPU quota

Register `Microsoft.Compute` and `Microsoft.Quota` once, then raise the family quota with `az quota update` (see [budget and quotas](budget-and-quotas.md#quotas-ask-early)). A quota of 8 vCPUs holds one 8-vCPU GPU machine at a time, so Linux and Windows GPU runs go one after the other.

## Sources

Checked on 2026-11-26: [NGads V620 series](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/ngadsv620-series), [AMD driver setup](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/n-series-amd-driver-setup), [trusted launch](https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch), [multitenant hosting rights](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/windows-desktop-multitenant-hosting-deployment), [states and billing](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing), [Run Command](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/run-command), [public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses), [NSG rules](https://learn.microsoft.com/en-us/cli/azure/network/nsg/rule), [Spot VMs](https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms), [Network Watcher](https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-create) and the [Azure Retail Prices API](https://prices.azure.com/api/retail/prices). See [sources](sources.md) for the full record.
