# Windows UI tests and GPU tests that need a desktop

Read this for Windows UI tests, OpenGL and windowed swapchain tests, and input-method tests on a cloud VM or a person's own Windows machine. The procedure ran in practice on an Azure Windows 11 VM and on EC2 Windows with NVIDIA. Registry names, cmdlets and command options were checked on **2026-11-26** against Microsoft Learn, and undocumented switches are marked.

## Why SSH is not enough

`SendInput` reaches only the window in front of the desktop of a signed-in, unlocked user. An SSH session has no desktop. So SSH builds the programs and reads the logs, and the tests run inside a signed-in session. Offscreen GPU tests do not need that session. OpenGL and windowed swapchain tests do.

## Prepare the signed-in session once

1. **Autologon of the batch user:** set `AutoAdminLogon` and `DefaultUserName` under `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`, and store the password as the LSA secret `DefaultPassword`, as Sysinternals Autologon does. A plain `DefaultPassword` registry value would be readable text. The password is random and no copy leaves the machine.
2. **Nothing may cover the desktop:** turn off the lock screen and the screen saver, the first sign-in privacy screen (policy `DisablePrivacyExperience` under `HKLM\SOFTWARE\Policies\Microsoft\Windows\OOBE`) and the consumer offers (`DisableWindowsConsumerFeatures` and `DisableSoftLanding` under `HKLM\SOFTWARE\Policies\Microsoft\Windows\CloudContent`). The two CloudContent policies apply only to Enterprise, Education and IoT Enterprise editions, so on Pro, check the desktop after sign-in instead of trusting them.
3. **Restart twice.** The first sign-in of a new user can leave the Start menu open.
4. **Check that no window covers the desktop** before the first test.

The Windows desktop edition opens no Server Manager at sign-in, which is one reason to prefer it over Windows Server for desktop tests when the licensing allows (see [budget and quotas](budget-and-quotas.md#licensing)).

## Run the tests in that session

- Create a scheduled task that runs only while the user is signed in: `schtasks /create /tn <name> /tr "<command>" /sc once /st 00:00 /ru <user> /it`, then start it with `schtasks /run /tn <name>`. `/it` makes it run in the user's interactive session.
- Start the test program through `conhost.exe --headless`, so no console window covers the app. The switch is not on Microsoft Learn, but it is in Microsoft's open-source console host and worked in practice.
- Write the log to a file and read it over SSH. `schtasks /run` returns as soon as the task starts, so the task also writes its exit code to a file when it ends. The runner step waits for that file with a time limit and exits with the code it holds, so a failed desktop test fails the step.
- Set the console resolution to 1920×1080 with `ChangeDisplaySettings` of `user32`, called from a PowerShell script in the user's session. The cloud console starts at 1024×768, and Windows 11 has no `Set-DisplayResolution` cmdlet.

## Rules for the tests

- Windows lets a newly started app come to the front only after input from the user, so a test clicks the app before it types.
- A click must fail with the name of the covering window when another window covers the element.
- Find elements through UI Automation by their names, which the app exposes for screen readers.
- A Windows server has no touch screen, so touch keyboard tests need a tablet or a touch laptop.

## Input methods

- `Install-Language ja-JP` run from a service does not add the language to the user's list.
- Add it in the user's session with `Set-WinUserLanguageList`, from the list of `Get-WinUserLanguageList` plus `ja-JP`.
- A new app gets the input method the person used last, so a test switches the layout first and back after. The Japanese keyboard layout is `00000411`, and the Microsoft IME input tip is `0411:{03B5835F-F03C-411B-9CE2-AA23E1171E36}{A76C93D9-5523-4E90-AAFA-4DB112F9AC76}`.

## NVIDIA on EC2 Windows

- Turn off the basic display adapter before the OpenGL tests, or the window gets the software driver.
- The GRID driver then shows two displays.
- Give the machine at least 80 GB of disk for the driver installer.
- The driver comes from the `ec2-windows-nvidia-drivers` bucket, as the EC2 NVIDIA driver guide describes.

## Files from macOS

A tar made on macOS holds `._<name>` metadata files unless `COPYFILE_DISABLE=1` is set when it is created, and those files break a Windows build. Prefer git bundles.

## Driver shader caches

Clear the driver's shader cache before a batch that checks shader compilation (see [Linux GPU and browsers](linux-gpu-and-browsers.md#driver-shader-caches), which lists the Windows folder too).

## Sources

Checked on 2026-11-26: [automatic logon](https://learn.microsoft.com/en-us/troubleshoot/windows-server/user-profiles-and-logon/turn-on-automatic-logon), [protecting the autologon password](https://learn.microsoft.com/en-us/windows/win32/secauthn/protecting-the-automatic-logon-password), [Privacy policy CSP](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-privacy), [Experience policy CSP](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-experience), [schtasks create](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks-create), [Install-Language](https://learn.microsoft.com/en-us/powershell/module/languagepackmanagement/install-language), [Set-WinUserLanguageList](https://learn.microsoft.com/en-us/powershell/module/international/set-winuserlanguagelist), [input locales](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/default-input-locales-for-windows-language-packs), [ChangeDisplaySettings](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-changedisplaysettingsw), [SendInput](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-sendinput) and [NVIDIA GRID drivers on EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nvidia-GRID-driver.html). `conhost.exe --headless` is in Microsoft's [console host source](https://github.com/microsoft/terminal), not in the docs. See [sources](sources.md) for the full record.
