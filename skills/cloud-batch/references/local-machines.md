# The person's own machines

Read this when a batch uses the person's daily machine, a spare machine or a laptop reached over SSH. Own machines cost nothing per hour, so they come first. They are also the machines the person needs for daily work, so they must never freeze, fill up or show surprise windows.

## The daily machine must never freeze

Five parallel builds at about 14 jobs each once pushed the load average of a laptop to 130 and froze it. Rules for the daily machine:

- Run one build at a time behind a lock, at the lowest priority, with a small fixed number of compile jobs that the person chooses. One person chose 4 jobs on a 15-core daily machine.
  - macOS: `/usr/bin/lockf -k <lock file> nice -n 19 ninja -C <build folder> -j 4`.
  - Linux: `flock <lock file> nice -n 19 ninja -C <build folder> -j 4`.
- Reserve the lock for work that only this machine can do, such as Apple builds, simulators and a local emulator. Send everything else to the batch line. A lock queue full of Linux work once starved the Apple work.
- A line of work that needs fast test iterations can get a targeted incremental build of only its test targets under the lock, when the lock is free and no Apple work is waiting.

Quick checks need no lock. Check one file at a time with `nice -n 19 clang -fsyntax-only <file>`, using that file's flags from `compile_commands.json` plus the warnings that the CI compilers add, such as `-Wmissing-field-initializers`, `-Wmissing-designated-field-initializers` and `-Wshadow`. A syntax check finds many compile errors in seconds without a build.

## Disk

The local disk once filled up to 192 MB free with build folders of finished work. Rules:

- Delete the build folders of finished work as soon as its results are recorded.
- Check that at least 30 GB is free before a big build (`df -h <folder>`), and stop with a sentence if it is not.
- For day-to-day builds, keep no second build tree of the same code, and reuse one build folder per configuration. A gate still builds each commit in a fresh tree and build folder (see [batches](batches.md#fresh-trees-or-the-gate-is-a-lie)), and deletes it after.
- Report the free space after cleanup.

## Docker for Linux reproduction

Docker on the local machine reproduces most Linux CI failures cheaply, without a cloud run. Use the CI's own image or a matching distribution. Docker on an Apple silicon Mac runs arm64 Linux by default, so an x86-64-only failure still needs an x86-64 machine. Software rasterizers, such as Mesa lavapipe and llvmpipe, run in any container (see [Linux GPU and browsers](linux-gpu-and-browsers.md)).

## Devices and simulators on the daily machine

- Always name the device: `--device <id>`, `adb -s <serial>`, `ANDROID_SERIAL=<serial>`.
- Never touch a physical device that belongs to the person's daily use.
- Use only simulators and emulators that already exist, and shut down the ones the run booted.
- Check that another project on the same machine is not using the simulator.
- Uninstall what the tests installed.
- Never open app windows on the person's screen. Use headless runs, simulators without a window, the emulator with `-no-window`, headless browsers or the cloud.

[Device testing](device-testing.md) has the full rules.

## A person's own Windows laptop

A Windows laptop is great for MSVC builds and tests at no cost. Set it up once:

1. Ask the person to install the OpenSSH Server and add the controller's public key. For an account in the Administrators group, Windows reads `C:\ProgramData\ssh\administrators_authorized_keys`, whose permissions must allow only Administrators and SYSTEM. Then use `ssh -o BatchMode=yes <user>@<host>`.
2. If the person gave a password in the chat, never write it anywhere. Ask them to install the key instead.
3. Clean the disk before the first run. One laptop had 3 GB free.
4. Keep a clean clone in a fixed folder, detached at main.

Each run checks out the bundle, builds, tests and then deletes the build folder, the bundle, the logs and the test leftovers in `%TEMP%`. Report the free disk space at the end.

An SSH session on Windows has no desktop. Swapchain, OpenGL window and UI tests skip there. Tell the person which tests that leaves for a desktop VM or for a scheduled task in a signed-in session (see [Windows desktop tests](windows-desktop.md)). A full cold test build on such a laptop took about 56 minutes, which is a useful first estimate to replace with your own number.

Send code to Windows as git bundles. A tar made on macOS carries files that break a Windows build (see [Windows desktop tests](windows-desktop.md#files-from-macos)).

## A person's own Linux or Mac machine over SSH

Install the controller's public key once, then use `ssh -o BatchMode=yes <user>@<host>`. `BatchMode=yes` makes SSH fail at once instead of asking for a password. Keep a clean clone in a fixed folder, run the bundle in a fresh worktree, and clean up after it as above.

A Mac that someone is using is not a place for Mac UI tests, which move the pointer and type into the front app. Use it for builds, simulator tests and command-line tests only (see [Apple platforms](apple-platforms.md)).

## Sources

Checked on 2026-11-26: [flock](https://man7.org/linux/man-pages/man1/flock.1.html), [Clang command line](https://clang.llvm.org/docs/ClangCommandLineReference.html), [OpenSSH key management on Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement) and [git worktree](https://git-scm.com/docs/git-worktree). macOS `lockf` is described in `man lockf`. The freeze, disk and laptop lessons come from practice. See [sources](sources.md) for the full record.
