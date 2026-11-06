# Native UI, external app tests and multiple displays

Read this for a supported Apple UI destination when the app has native SDK screens, rendered/canvas
content or multiple simulator displays. Record Xcode/runtime/build and the actual observation method.
A screenshot, a hittable control and a verified transaction prove different things.

## Choose the surface that can observe the requirement

Use the app's framework tests for canvas/engine state and XCUIAutomation for supported native controls,
system dialogs and SDK sheets. A Lua/engine debugger does not inspect every UIKit/SwiftUI paywall.
Conversely, an accessibility hierarchy may not expose internal engine nodes. Test the boundary between
them deliberately: real app action → native presentation → dismiss/completion → refreshed app state.
Do not grant a fake entitlement or replace the real SDK response to manufacture a passing integration.

Prefer existing UI targets and stable accessibility selectors. If no suitable target exists and a
focused interaction check is needed, create a disposable native XCTest UI runner outside shipping
source. Inspect its actual project, scheme, deployment target and destination. It should activate the
installed target by its real bundle ID. It is not a replacement app and must not ship inside the app.
Launch the target through its required development workflow first if a normal test launch would omit
framework-specific arguments or disconnect its development server.

For example, a target already showing an English subscription sheet can be checked with:

```swift
import XCTest

final class PaywallSmoke: XCTestCase {
    func testRestoreControlIsReachable() {
        let app = XCUIApplication(bundleIdentifier: "com.example.app")
        app.activate()

        app.swipeUp()
        app.swipeUp()

        let restore = app.buttons.matching(
            NSPredicate(format: "label CONTAINS[c] %@", "Restore")
        ).firstMatch

        XCTAssertTrue(restore.waitForExistence(timeout: 10))
        XCTAssertTrue(restore.isHittable)
    }
}
```

This fixture assumes the actual app/locale/sheet and two swipes fit the chosen device. Inspect the
hierarchy and adapt selectors and bounded scrolling to observed content. Do not repeat arbitrary
swipes if the wrong view is active. Extend the case for the actual close, purchase, Terms and Privacy
controls and verify real destinations where appropriate. The example checks reachability only.
It neither purchases nor demonstrates a successful restoration.

Run the real scratch scheme with a concrete destination and fresh result bundle. Check that its
intended test actually executed, then inspect `.xcresult` and native captures. A test-runner build
or empty test plan is not a test pass. Keep useful failure evidence and remove the disposable runner,
derived output and temporary fixtures after the case. Preserve the app's real native project.

## Discover and capture the intended simulator display

Xcode 27.2's inspected help supports these native commands:

```text
xcrun simctl help io
xcrun simctl io "$SIMULATOR_UDID" enumerate
xcrun simctl io "$SIMULATOR_UDID" screenshot --display="$DISPLAY_ID" "$CAPTURE_PATH"
```

Choose IDs/names from enumeration, including powered state, rather than always using the first or
internal alias. A particular exercised Duo runtime had outer `1` and inner `3`. Treat those values as
a version-specific observation, not model detection logic. Record posture/orientation and validate the
captured dimensions and visible app before labeling a screenshot outer/inner.

Select the actual closed/open posture in Device Hub. Changing the capture display, canvas zoom,
screen power or framebuffer geometry is not the same as a physical posture transition. If the
capture is black or belongs to a different panel, inspect the active posture and powered displays,
then the target process/window. Preserve the first error. Do not repeatedly power-cycle displays or
restart shared simulator services as the first repair.

Inspect both layouts after each transition: safe areas, current page, selected member/data, scroll,
text wrapping, keyboard, native sheets and status bars. A correct screenshot size does not prove that
layout reflow happened. Store-export opacity and slot placement belong to the actual delivery check.

## Diagnose unavailable GUI control without changing the product

Prefer available connected browser/computer tools or accessible native test APIs. When control of
Device Hub or another host application is needed, inspect the actual application/window and relevant
macOS Accessibility/screen-capture permissions. A sandbox denial is not evidence that no devices exist.
Do not edit TCC databases, extract browser cookies or use private service endpoints as a workaround.

A launch trampoline or duplicate application process can make an automation display name ambiguous.
Identify the real application process, bundle ID and current window rather than repeatedly asking for
the first matching name. For a permitted pointer fallback, activate the intended app, verify foreground
identity, discover current window bounds and account for display origin and image scale. Reinspect
state after the action. Hardcoded coordinates from another monitor/window are not reliable selectors.

Keep logical UI waits distinct from foreground/input failures. A button that appears unchanged may
have received no input, may be disabled by validation, or may still be processing. Inspect those states
before attributing it to network failure. Stop only owned runs and retain no account/session secrets
in shared screenshots. See [execution evidence](execution-and-evidence.md) for report boundaries.
