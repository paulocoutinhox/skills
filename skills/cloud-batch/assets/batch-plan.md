# 🗺️ Batch Plan

## ❓ Decisions For The Person

- List each open decision with its options and the cost of each option.

## 🖥️ Machines And Services

| Platform | Check | Runs on (service and machine) | Why there | Market | Price |
| --- | --- | --- | --- | --- | --- |
| 🐧 | | | | | |

## 💰 Budget

| Service | Monthly share | What it pays for |
| --- | --- | --- |
| 🔶 AWS EC2 | | |
| 🔷 Azure | | |
| 🌥️ Google Cloud | | |
| 📱 AWS Device Farm | | |
| 📲 Google Device Run | | |
| 🛠️ Xcode Cloud | Included hours, or a paid plan | |
| ⚙️ CI | Included minutes | |
| Cache bucket | | |
| **Total** | | |

## 🗓️ Batch Schedule

| Batch | When | Service and machine | Platforms | Jobs | Estimated duration | Timer (estimate + margin) | Estimated cost |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

## 🧪 Device Matrix

| Platform | Cheapest place that shows it | What only real hardware shows, and where | One-time setup | Per-run steps | Cleanup | Cost |
| --- | --- | --- | --- | --- | --- | --- |
| 🍎 iPhone and iPad | | | | | | |
| 🍎 Apple TV | | | | | | |
| 🍎 Mac | | | | | | |
| 🤖 Android | | | | | | |
| 🪟 Windows desktop | | | | | | |
| 🐧 Linux GPU | | | | | | |
| 🌐 Browsers | | | | | | |

No cloud rents an Apple TV, an Apple Vision Pro or an Apple Watch. Needs the person's own device: list here.

## 📏 Quotas To Request Before The First Batch

| Service | Quota | Needed | Current | Request filed on |
| --- | --- | --- | --- | --- |
| | | | | |

## 🔑 Credentials Setup

| Service | Method | Variable or sign-in names | Least-privilege scope | Check command |
| --- | --- | --- | --- | --- |
| | | | | |

## 🗃️ Caches

| Cache | Where | Key | Expiry | Monthly cost |
| --- | --- | --- | --- | --- |
| | | | | |

## 🧹 Cleanup Checks

| Service | What each session deletes | Listing that proves it |
| --- | --- | --- |
| | | |

## 👤 The Person's Case

| Question | Answer |
| --- | --- |
| Platforms to build and test | |
| GPU, emulator or desktop session needed | |
| Own machines (cores, memory, disk, OS, CPU kind, daily use or spare) | |
| Own devices that may be used (by role) | |
| Cloud accounts, regions and known quotas | |
| Monthly limit and hard rules | |
| Lines of work in parallel | |
| Controller OS | |
| Repositories public or private, existing CI and its free minutes | |
| Report language and time zone | |
| Agent acts alone with keys from the shell profile | |
| Apple Developer Program, repository admin rights, App Store Connect API key (for Xcode Cloud) | |
| Preview terms accepted (for Google Device Run) | |
| Tracker wanted, and its path | |
| Script language | Python run with uv |

## 📋 Notes

- **Layout:** The decisions for the person open the plan, the plan's sections follow, most important first, then these notes, and the 🚦 Legend closes the file.
- **Dates and prices:** Prepared on YYYY-MM-DD. Prices were checked on YYYY-MM-DD against each provider's current price page. Every figure is an estimate.
- **Machine order:** Own machines, existing CI and Xcode Cloud's included hours, spot Linux, a prepared deallocated Windows VM, GPU machines, a cloud Mac. Device labs only for what real hardware alone shows.
- **Budget:** Daily allowance: share left ÷ days left. A batch above it waits, or goes to the person with its estimate.
- **Unused rows:** Remove the rows of services and platforms the plan does not use.
- **Credentials:** Names only, never values.

## 🚦 Legend

Platforms: 🐧 Linux, 🪟 Windows, 🍎 Apple, 🤖 Android, 🌐 Web, 🎮 GPU work.

Services: 🔶 AWS EC2, 🔷 Azure, 🌥️ Google Cloud, 🏠 Own Machines, 📱 AWS Device Farm, 📲 Google Device Run, 🛠️ Xcode Cloud, ⚙️ CI.

These match the tracker.
