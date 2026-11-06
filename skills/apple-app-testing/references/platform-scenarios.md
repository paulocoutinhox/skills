# Platform-specific acceptance scenarios

Read only the sections relevant to the requested platforms. Share acceptance rules where appropriate, but retain each platform's real interaction, lifecycle and hardware evidence.

## iOS and iPadOS

Exercise first launch, authentication, main navigation, sheets/popovers, keyboard-visible forms and supported deep links/notification entry. Check safe areas, system bars, presentation dismissal, interactive back gestures and the state after canceling a picker or authentication flow.

Use compact and large layouts, supported rotation, iPad window resizing/multitasking and actual keyboard/pointer input where relevant. Confirm selected record, draft and navigation state when layouts change. Where the product supports posture/hinge behavior, test that transition explicitly on a supported simulated/physical configuration. A resized screenshot alone does not prove posture-specific behavior.

Keep software keyboard testing separate from a Mac hardware keyboard connection. Exercise return-key behavior, focus progression, autofill, pasted values and error correction while controls are partly covered. Confirm the last required control remains reachable with large text.

Test permission and data-access states that the app actually uses, including limited choices and later revocation. Use synthetic media and accounts. A simulated permission or location event does not establish camera quality, Bluetooth/radio behavior, secure hardware or background scheduling on a real phone.

Distinguish returning from another app, scene disconnection, OS process termination, explicit user termination, restart and preserved-data upgrade. Use the declared draft restoration policy. Never label `terminate()` followed by `launch()` as proof of the OS's memory-pressure behavior.

## tvOS

Map the screen's focus graph before testing actions. Starting at the default focus, move Up/Down/Left/Right to every important control and inspect the focused item, visible focus indication and scroll movement. Confirm no focus trap and no unreachable primary action. Test returning from a detail view, dialog or keyboard to the expected focused item.

Use Select, Back/Menu-equivalent and Play/Pause according to the selected remote/OS interaction. Cover short versus long press where the app defines different behavior. Apple's `XCUIRemote` supplies button press and press-and-hold APIs for UI tests. Prefer a real directional path over a direct element click that skips focus navigation.

For text entry, open the system keyboard with the remote and exercise correction, cancellation and submission. Test any advertised phone-assisted entry or dictation on the actual supported device/account/network. Do not assume those services exist in a cloud session or simulator.

For media apps, test loading, buffering, error, playback position, pause/resume, seeking, captions/audio options and return from background. Inspect entitlement/authentication expiry and resumption without accidentally restarting a purchase. DRM, HDMI/display/audio behavior, real remote feel and living-room readability require appropriate hardware evidence.

Capture the selected focus state and control sequence in the report. A screenshot of a visible button does not prove that a remote user can reach it.

## macOS

Test application launch versus document open, file association, Open/Save/Export panels, cancel, overwrite confirmation, invalid/unwritable destinations and sandbox access lifetime where used. Use a temporary test folder with known files. Avoid testing destructive overwrite against a user's real documents.

Check keyboard-only traversal, first responder, Tab/Shift-Tab, Return/default action, Escape/cancel, shortcuts and menu validation. Verify text selection, copy/paste, undo/redo and contextual actions where part of the product. Mouse-click success does not establish keyboard usability.

Exercise multiple windows/documents, window resize/fullscreen, toolbar/sidebar state, menu-bar items and display-scale changes where supported. Confirm an action targets the correct active document/window. A stale query that finds a similarly titled control in another window is a test defect unless the app itself routes the action incorrectly.

Close the last window, reopen the application, quit/relaunch and restore a session according to the app's policy. Closing a window may leave the process running. Test unsaved-change handling and canceled quit, not only a clean restart.

Inspect real permission prompts and later revocation for camera/microphone, files, screen recording or automation where used. Separate the test runner's authorization from the application's permissions. A locally debug-signed app, a notarized direct-download app and a store-sandboxed app can exercise different distribution contracts. Test the variant relevant to the request without disabling protections as a shortcut.

Check Apple silicon and any still-supported Intel build/dependency behavior with appropriate evidence. Translation or a cross-compiled binary alone is not proof of a tested hardware/OS combination.

## visionOS

First classify the binary: native visionOS SDK app or compatible iPhone/iPad app built with the iOS SDK. Apple's XCUIAutomation framework explicitly limits visionOS UI testing to the latter. Do not create a fictitious native visionOS UI-test success or imply that installing a general mobile automation tool removes that limit.

For native apps, combine supported component/model/resource checks with simulator and on-device spatial acceptance. A rendered entity test can validate selected scene logic/assets without validating gaze acquisition, comfort or the entire compositor. Use the actual framework's testable surface and record what it cannot observe.

In Device Hub, select the visionOS run destination. Interaction mode uses the Mac pointer to simulate gaze. Click simulates a tap, click-and-hold a held pinch, drag a lateral pinch-drag and Shift-drag a forward/back drag. Camera-navigation mode is different from content interaction. Record which mode produced the action rather than mistaking viewpoint motion for a product drag defect.

Exercise window, volume and immersive-space entry/exit only where the app offers them. Cancel an immersion request, dismiss/reopen content, change viewing distance/angle and inspect occlusion, layering, text readability, target placement and scale. Test multiple simulated surroundings/light conditions as a layout aid.

Verify the real device's gaze/pinch interaction, supported direct touch/controller/keyboard input, spatial audio, tracking permissions and session interruption. Physical comfort, motion, depth perception, passthrough and real-world safety cannot be certified from a flat capture. Do not request raw gaze data or unsupported sensor access to invent a test oracle.

Use a controlled operator and the actual device capture mechanism. Do not cover or bypass presence/security sensors to keep a session alive. State that a simulator gesture is simulated evidence and a human physical acceptance case is manual evidence.

## watchOS

Use the actual Watch scheme/test target and supported runtime/device size. Apple's watchOS testing article documents unit and UI testing bundles. Its historical target-name examples do not require a new project to recreate an obsolete extension structure.

Test Crown-driven scrolling/value adjustment, focus/selection, the primary action and navigation back through the actual screen stack. Verify small/large Watch layouts and supported accessibility text settings. Controls must remain reachable without precisely targeting tiny geometry.

Exercise the text-entry methods actually offered for the selected Watch model, locale and OS: keyboard, dictation, Scribble or phone-assisted entry as available. Check cancellation, correction and submission. Do not claim every method exists on every configuration, and do not replace the entire field programmatically when editing behavior is the requirement.

Separate standalone operation from a phone-companion journey. Establish phone/Watch account identity and connectivity, perform a change, disconnect, reconnect and verify the product's specified transfer/reconciliation behavior. A deferred transfer is not necessarily an immediate request/response. Verify no duplicate record or another account's state after reconnection.

Exercise background/foreground, wrist-down/always-on presentation where supported, interrupted operations, notifications and complication/widget timelines used by the app. A simulated lifecycle event cannot certify real power/thermal scheduling. Haptics, sensor accuracy, workouts, Health data, cellular connectivity and actual wrist comfort need controlled physical-device evidence and authorized synthetic test conditions.

Record both OS versions and pair identities when the phone matters. One Watch screenshot or a passed phone UI suite does not certify the companion flow.

## Cross-platform regression selection

Trace a changed shared rule into every consumer: validation copy, formatting, persistence, background/companion transport and each platform's action state. Run the shared rule's component tests plus a representative supported UI/manual path per affected platform. Do not duplicate every low-level case into every slow UI matrix, or omit platform interaction because the model test passed.

See [forms/UI](forms-and-ui.md), [execution/evidence](execution-and-evidence.md) and [sources](sources.md) for the applicable tools and evidence boundaries.
