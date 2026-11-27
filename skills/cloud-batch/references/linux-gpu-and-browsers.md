# Linux GPU machines, software rendering and browsers

Read this for GPU tests on Linux cloud machines, windowed runs without a monitor, software rasterizers and browser runs. Driver details come from real runs on AWS and Azure. Commands were checked on **2026-11-26** where public docs exist, and [the sources](sources.md) say which.

## NVIDIA on EC2 (such as g4dn)

- Install the GRID driver from Amazon's buckets, `ec2-linux-nvidia-drivers` (and `ec2-windows-nvidia-drivers` for Windows), as the EC2 NVIDIA driver guide describes. Download it from a presigned URL with a short expiry made on the controller (`aws s3 presign s3://ec2-linux-nvidia-drivers/<key> --expires-in 600`), so no AWS key reaches the machine.
- The driver has headless display heads. An X server device section with `Option "ConnectedMonitor" "DFP-0, DFP-1"`, `NoEdidModes` mode validation and two `MetaModes` gives two displays for windowed and multi-display runs.
- Close windows through the window manager with `wmctrl -c <title>`, not `xdotool windowclose`, which destroys the window under the app.

## Wayland

Run Weston as an X client: `weston --backend=x11 --idle-time=0`. Weston's default idle time is 300 seconds. Without `--idle-time=0`, its outputs turned off after 5 idle minutes in practice, and a Vulkan swapchain waited forever for a frame.

## Japanese input on Linux

IBus with Mozc starts in direct input mode. After `ibus engine mozc-jp`, press `Hiragana` before typing.

## Software rasterizers

- Mesa lavapipe for Vulkan and llvmpipe for OpenGL, under `xvfb-run --auto-servernum`, are cheap and run in any container. Use them for correctness, never for performance numbers.
- On an arm64 Docker host, the Mesa packages also bring hardware Vulkan drivers whose loader prints errors. Point the Vulkan loader at lavapipe alone with `VK_DRIVER_FILES=<path>`. The file is named after the CPU, such as `lvp_icd.x86_64.json` or `lvp_icd.aarch64.json`, in the distribution's ICD folder, often `/usr/share/vulkan/icd.d/`. List that folder to get the exact path.

## AMD on Azure (NG V620, Linux)

- The GPU is a virtual function that loads its firmware through the host.
- Azure's Ubuntu image blacklists `amdgpu`, and the newest kernel failed with `PSP firmware loading failed`. A specific Azure kernel worked (`6.8.0-1071-azure` at the time). Pin the kernel that the driver supports.
- `amdgpu-dkms` did not compile for that kernel, so the kernel's own module was used.
- The AMD OpenGL driver takes over EGL, so Mesa radeonsi cannot run beside it.
- Check the driver version that Azure supports for the size before renting (see [Azure](azure.md)).

## Ubuntu machines and sanitizers

The Ubuntu notes (`/tmp` emptied at boot, the timer from a systemd unit, unattended upgrades) and the GCC ThreadSanitizer setting `vm.mmap_rnd_bits=28` are in [AWS](aws.md#the-self-destruct-timer-on-ubuntu).

## Driver shader caches

Drivers cache compiled shaders on disk, so a shader compile bug shows only with an empty cache. Clear the cache before such a batch, such as `~/.cache/AMD` on Linux and `%LOCALAPPDATA%\AMD` on Windows, and the matching NVIDIA and Mesa cache folders.

## Browsers

- Headless Chrome forces software rendering, so its GPU times measure the CPU.
- Without a GPU, Chrome does not fall back to SwiftShader for WebGL by itself, and WebGL context creation fails. For software WebGL, opt in with `--enable-unsafe-swiftshader`.
- For a real GPU, start Chrome with `--enable-gpu`. On Linux that needs an X display (`DISPLAY`). On a Mac, `--use-angle=metal` selects ANGLE's Metal backend.
- WebGPU in headless Chrome on Linux depends on the GPU and driver and was not reliable in practice: a WebGPU canvas could not present. Use WebGL2 there, or a machine with a supported GPU.
- Safari and Firefox can open the same served page for a look. Automated cross-browser runs can go to AWS Device Farm's desktop browsers through Selenium (see [Device Farm](device-farm.md)).
- Stop web servers and headless browsers as soon as a run ends.

## Sources

Checked on 2026-11-26: [NVIDIA GRID drivers on EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nvidia-GRID-driver.html), [Linux AMD driver on Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/azure-n-series-amd-gpu-driver-linux-installation-guide), [running Weston](https://wayland.pages.freedesktop.org/weston/toc/running-weston.html), [Weston man page](https://manpages.debian.org/unstable/weston/weston.1.en.html), [Vulkan loader architecture](https://github.com/KhronosGroup/Vulkan-Loader/blob/main/docs/LoaderInterfaceArchitecture.md), [SwiftShader in Chrome](https://chromium.googlesource.com/chromium/src/+/main/docs/gpu/swiftshader.md), [GPU in headless Chrome](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/docs/gpu/using-gpu-hardware-in-headless-chrome.md) and the [sanitizer workaround issue](https://github.com/actions/runner-images/issues/9491). The X server, AMD kernel and IBus details come from practice. See [sources](sources.md) for the full record.
