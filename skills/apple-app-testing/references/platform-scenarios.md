# Platform-specific acceptance scenarios

Read only the sections for the platforms you were asked to test. Share acceptance rules where it makes sense, but keep each platform's real interaction, lifecycle and hardware evidence.

## iOS and iPadOS

Test first launch, sign-in, main navigation, sheets/popovers, forms with the keyboard showing and supported deep links/notification entry. Check safe areas, system bars, closing presented views, interactive back gestures and the state after canceling a picker or sign-in flow.

Use compact and large layouts, supported rotation, iPad window resizing/multitasking and real keyboard/pointer input where it matters. Confirm the selected record, draft and navigation state when layouts change. Where the product supports posture/hinge behavior, test that change directly on a supported simulated/physical setup. A resized screenshot alone does not prove posture-specific behavior.

Test the software keyboard separately from a connected Mac hardware keyboard. Test return-key behavior, moving focus forward, autofill, pasted values and error correction while controls are partly covered. Confirm the last required control stays reachable with large text.

Test the permission and data-access states the app really uses, including limited choices and later revocation. Use synthetic media and accounts. A simulated permission or location event does not prove camera quality, Bluetooth/radio behavior, secure hardware or background scheduling on a real phone.

Keep these apart: returning from another app, scene disconnection, OS process termination, user termination, restart and upgrade that keeps data. Follow the stated draft restoration policy. Never call `terminate()` followed by `launch()` proof of the OS's memory-pressure behavior.

## tvOS

Map how focus moves on the screen before you test actions. Start at the default focus and move Up/Down/Left/Right to every important control. Check the focused item, the visible focus highlight and scroll movement. Confirm that focus never gets stuck and that every main action is reachable. Test that returning from a detail view, dialog or keyboard puts focus on the expected item.

Use Select, Back/Menu-equivalent and Play/Pause as the selected remote/OS works. Cover short versus long press where the app gives them different behavior. Apple's `XCUIRemote` provides button press and press-and-hold APIs for UI tests. Prefer a real directional path over a direct element click that skips focus navigation.

For text entry, open the system keyboard with the remote and test correction, cancellation and submission. Test any advertised phone-assisted entry or dictation on the real supported device/account/network. Do not assume those services exist in a cloud session or simulator.

For media apps, test loading, buffering, error, playback position, pause/resume, seeking, captions/audio options and return from background. Check entitlement/sign-in expiry and resuming without starting a purchase again by accident. DRM, HDMI/display/audio behavior, real remote feel and readability from across a living room need evidence from suitable hardware.

Record the selected focus state and control sequence in the report. A screenshot of a visible button does not prove a remote user can reach it.

## macOS

Test app launch versus document open, file association, Open/Save/Export panels, cancel, overwrite confirmation, invalid/unwritable destinations and how long sandbox access lasts where used. Use a temporary test folder with known files. Do not test destructive overwrite on a user's real documents.

Check keyboard-only movement, first responder, Tab/Shift-Tab, Return/default action, Escape/cancel, shortcuts and menu validation. Check text selection, copy/paste, undo/redo and context actions where the product has them. A working mouse click does not show the app is usable by keyboard.

Test multiple windows/documents, window resize/fullscreen, toolbar/sidebar state, menu-bar items and display-scale changes where supported. Confirm an action reaches the right active document/window. If a stale query finds a control with a similar title in another window, that is a test bug, unless the app itself sends the action to the wrong place.

Close the last window, reopen the app, quit/relaunch and restore a session as the app's policy says. Closing a window may leave the process running. Test unsaved-change handling and a canceled quit, not only a clean restart.

Check real permission prompts and later revocation for camera/microphone, files, screen recording or automation where used. Keep the test runner's permission separate from the app's permissions. A locally debug-signed app, a notarized direct-download app and a store-sandboxed app can follow different distribution contracts. Test the variant the request needs, and do not turn off protections as a shortcut.

Check Apple silicon and any still-supported Intel build/dependency behavior with suitable evidence. Translation or a cross-compiled binary alone does not prove a tested hardware/OS combination.

## visionOS

First find out what kind of binary it is: a native visionOS SDK app or a compatible iPhone/iPad app built with the iOS SDK. Apple's XCUIAutomation framework clearly limits visionOS UI testing to the second kind. Do not make up a native visionOS UI-test pass, and do not suggest that installing a general mobile automation tool removes that limit.

For native apps, combine supported component/model/resource checks with spatial acceptance on the simulator and the device. A rendered entity test can check chosen scene logic/assets, but it does not check gaze pickup, comfort or the whole compositor. Use the parts the real framework can test, and write down what it cannot see.

In Device Hub, select the visionOS run destination. Interaction mode uses the Mac pointer to simulate gaze. Click simulates a tap, click-and-hold a held pinch, drag a sideways pinch-drag and Shift-drag a forward/back drag. Camera-navigation mode is not the same as content interaction. Write down which mode made the action, so you do not mistake viewpoint motion for a product drag bug.

Test window, volume and immersive-space entry/exit only where the app offers them. Cancel an immersion request, close/reopen content, change viewing distance/angle and check occlusion, layering, text readability, target placement and scale. Try several simulated surroundings/light conditions to help check layout.

On the real device, check gaze/pinch interaction, supported direct touch/controller/keyboard input, spatial audio, tracking permissions and session interruption. A flat capture cannot certify physical comfort, motion, depth perception, passthrough or real-world safety. Do not ask for raw gaze data or unsupported sensor access to invent a way to judge the test.

Use a controlled operator and the device's real capture method. Do not cover or bypass presence/security sensors to keep a session alive. State that a simulator gesture is simulated evidence and that a human physical acceptance case is manual evidence.

## watchOS

Use the real Watch scheme/test target and a supported runtime/device size. Apple's watchOS testing article documents unit and UI testing bundles. Use the project's real target names instead of rebuilding the article's example target structure.

Test Crown scrolling/value changes, focus/selection, the main action and navigating back through the real screen stack. Check small/large Watch layouts and supported accessibility text settings. Controls must stay reachable without hitting tiny shapes exactly.

Test the text-entry methods the selected Watch model, locale and OS really offer: keyboard, dictation, Scribble or phone-assisted entry, as available. Check cancellation, correction and submission. Do not claim every method exists on every setup. Do not replace the whole field from code when the requirement is about editing behavior.

Keep standalone use separate from a phone-companion journey. Set up phone/Watch account identity and connectivity, make a change, disconnect, reconnect and check the product's stated transfer/sync behavior. A delayed transfer is not always an immediate request/response. Check that there is no duplicate record and no other account's state after reconnecting.

Test background/foreground, wrist-down/always-on display where supported, interrupted operations, notifications and the complication/widget timelines the app uses. A simulated lifecycle event cannot certify real power/thermal scheduling. Haptics, sensor accuracy, workouts, Health data, cellular connectivity and real wrist comfort need controlled physical-device evidence and approved synthetic test conditions.

Write down both OS versions and pair identities when the phone matters. One Watch screenshot or a passing phone UI suite does not certify the companion flow.

## Cross-platform regression selection

Follow a changed shared rule into everything that uses it: validation text, formatting, saving, background/companion transport and each platform's action state. Run the shared rule's component tests plus one typical supported UI/manual path for each affected platform. Do not copy every low-level case into every slow UI matrix. Do not skip platform interaction because the model test passed.

See [forms/UI](forms-and-ui.md), [execution/evidence](execution-and-evidence.md) and [sources](sources.md) for the tools and evidence limits that apply.
