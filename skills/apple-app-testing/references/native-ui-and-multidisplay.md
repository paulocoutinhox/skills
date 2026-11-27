# Native UI, external app tests and multiple displays

Read this for a supported Apple UI destination when the app has native SDK screens, rendered/canvas
content or several simulator displays. Write down the Xcode/runtime/build and how you really observed
the result. A screenshot, a hittable control and a verified transaction prove different things.

## Choose the surface that can observe the requirement

Use the app's framework tests for canvas/engine state and XCUIAutomation for supported native controls,
system dialogs and SDK sheets. A Lua/engine debugger does not see every UIKit/SwiftUI paywall.
On the other side, an accessibility hierarchy may not show internal engine nodes. Test the handoff
between them on purpose: real app action → native presentation → dismiss/completion → refreshed app
state. Do not grant a fake entitlement or replace the real SDK response to fake a passing integration.

Prefer existing UI targets and stable accessibility selectors. If no suitable target exists and you
need a focused interaction check, create a throwaway native XCTest UI runner outside shipping source.
Check its real project, scheme, deployment target and destination. It should open the installed
target by its real bundle ID. It is not a replacement app and must not ship inside the app. If a
normal test launch would leave out framework-specific arguments or disconnect the development
server, first launch the target through its required development workflow.

For example, a target that already shows an English subscription sheet can be checked with:

```swift
import XCTest

final class PaywallSmoke: XCTestCase {
    func testRestoreControlIsReachable() {
        let app = XCUIApplication(bundleIdentifier: "com.example.app")
        app.activate()

        app.swipeUp()
        app.swipeUp()

        let restorePredicate = NSPredicate(format: "label CONTAINS[c] %@", "Restore")
        let restore = app.buttons.matching(restorePredicate).firstMatch

        XCTAssertTrue(restore.waitForExistence(timeout: 10))
        XCTAssertTrue(restore.isHittable)
    }
}
```

This fixture assumes the real app/locale/sheet, and that two swipes fit the chosen device. Look at the
hierarchy and adjust selectors and limited scrolling to the content you see. Do not repeat random
swipes if the wrong view is active. Extend the case for the real close, purchase, Terms and Privacy
controls, and check real destinations where that fits. The example only checks that the control can
be reached. It does not buy anything or show a successful restore.

Run the real scratch scheme with a specific destination and a fresh result bundle. Check that the
intended test really ran, then look at `.xcresult` and native captures. A test-runner build or empty
test plan is not a test pass. Keep useful failure evidence, and remove the throwaway runner, derived
output and temporary fixtures after the case. Keep the app's real native project.

## Discover and capture the intended simulator display

The checked help for Xcode 27.2 supports these native commands:

```text
xcrun simctl help io
xcrun simctl io "$SIMULATOR_UDID" enumerate
xcrun simctl io "$SIMULATOR_UDID" screenshot --display="$DISPLAY_ID" "$CAPTURE_PATH"
```

Choose IDs/names from the enumeration output, including powered state, instead of always using the
first one or the internal alias. One tested Duo runtime had outer `1` and inner `3`. Treat those values
as something seen in one version, not as a way to detect the model. Write down posture/orientation, and
check the captured size and the visible app before you label a screenshot outer/inner.

Select the real closed/open posture in Device Hub. Apple documents `XCUIHinge` as a reference to
the iPhone Duo hinge with a read-only `angle` property. It documents no way to get or change it,
and the installed Xcode 27.2 simulator headers do not expose it. Do not plan UI tests that change
posture through it. Changing the capture display, canvas zoom,
screen power or framebuffer geometry is not the same as a physical posture change. If the
capture is black or shows a different panel, check the active posture and powered displays,
then the target process/window. Keep the first error. Do not keep power-cycling displays or
restarting shared simulator services as your first fix.

Check both layouts after each change: safe areas, current page, selected member/data, scroll,
text wrapping, keyboard, native sheets and status bars. A correct screenshot size does not prove the
layout reflowed.

## Diagnose unavailable GUI control without changing the product

Prefer the connected browser/computer tools or accessible native test APIs you have. When you need
to control Device Hub or another host app, check the real app/window and the macOS
Accessibility/screen-capture permissions that apply. A sandbox denial does not show that no devices
exist. Do not edit TCC databases, pull browser cookies or use private service endpoints as a workaround.

A launch trampoline (a small launcher that starts the real app) or a duplicate app process can make an
automation display name unclear. Find the real app process, bundle ID and current window instead of
asking again and again for the first matching name. For an allowed pointer fallback, bring the intended
app to the front, check that it really is in front, find the current window bounds and allow for display
origin and image scale. Check the state again after the action. Hardcoded coordinates from another
monitor/window are not reliable selectors.

Keep logical UI waits separate from foreground/input failures. A button that looks unchanged may
have received no input, may be disabled by validation, or may still be working. Check those states
before you blame the network. Stop only runs you own, and keep no account/session secrets
in shared screenshots. See [execution evidence](execution-and-evidence.md) for report limits.
