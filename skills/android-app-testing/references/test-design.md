# Forms, screens and interaction design

Read this when translating a feature into observable cases or choosing the Android UI observation surface. These cases are original applications of established test-design techniques, not a copied certification syllabus or a universal product specification.

## Derive cases from actual acceptance rules

Start with one normal journey and name its durable outcome. Identify invalid categories and real ordered boundaries. Add a decision table where two conditions interact, then model important transitions such as editing → validating → ready → submitting → success/error. Prioritize combinations that change behavior rather than producing every mathematical combination of device and input.

For a declared inclusive quantity range of 1–10, test 0, 1, 10 and 11, plus a representative interior value. For a premium-only action, cover both account entitlement and input validity so an invalid field cannot hide a missing entitlement check. These numbers and roles are examples that must be replaced by the actual contract.

A test oracle must distinguish accepted text from the displayed formatting. A currency field might display grouping and a decimal separator but submit an integer minor-unit value. Verify the selected currency's actual fraction rule and negative/zero policy. Do not infer value from a screenshot alone or assume every currency has two decimal places.

## A practical form session

Inventory field labels, hints, input types, masks, required state and submission behavior. Open the form with the real software keyboard active. A desktop hardware keyboard can hide layout failures that appear when the IME covers the lower screen.

Exercise untouched submit, one missing field, one invalid field, correction and valid submit. For each error, verify its association with the correct field, readable wording, retained valid input and focus/scroll behavior. Check that a summary and inline error do not contradict one another. Disabled submission and field validation can be separate product choices.

Type, paste, select, replace and delete within a value. Cover strings with accents, combining marks and supported scripts. Determine whether a boundary counts Unicode code points, UTF-16 units, UTF-8 bytes or user-perceived characters. Use a known fixture with the appropriate expected count, and do not invent an exact count by visually inspecting emoji.

Use Next/Done/Search/Send according to the actual field action. Press Back once to inspect keyboard dismissal, then again to inspect navigation. Test focus order with Tab/Shift+Tab where supported, and ensure a hardware Enter does not unexpectedly submit twice. Check autofill separately from typing because it may populate multiple fields together.

For masks, verify the cursor while editing the middle, paste of an already formatted value, deletion near separators and the canonical submitted payload. Test phone country handling, postal-code country selection and date/timezone rules only for supported regions. A generic regular expression is not evidence that all real names or addresses are accepted.

## Asynchronous and durable behavior

Hold a validation response for A, change to B and deliver A last. Observe the new field value, pending state and error/valid indicator. A safe implementation must associate a response with the intended input/request instead of applying whichever finishes last.

Hold submission long enough to double-tap, navigate away or lose connectivity. Check the actual durable record count and returned identity through an authorized test API/database view. A disabled button alone does not prove idempotency. A timeout can mean that the server committed but the response was lost. The expected retry/reconciliation behavior must follow the application's contract.

Verify field errors, general server failure, expired authentication and rate limiting separately. Do not expect every error to be retriable. Preserve useful draft input where required and remove sensitive values where required. Record whether a retry created a new request or reconciled the original operation.

Use independent accounts/data per parallel case. Two shards that update the same profile can manufacture stale-state failures or conceal a real race. Cleanup removes only records created by that case and never deletes another worker's evidence.

## Screens, transitions and system interaction

Test loading/content/empty/error/offline states with known fixture data. Exercise list scrolling, pagination, refresh, repeated navigation and selection across reloads. Use stable item identities to verify that recycled rows do not display another record's image or state.

Open the screen normally, by a supported deep link and after authentication expiry. Check back-stack behavior and that a link to a sensitive record still requires server authorization. Test a second synthetic account after logout to detect cached account data. This focused isolation check is not a complete security audit.

Use real device/window changes for final layout acceptance. Check fold/unfold, split-screen and rotation where supported. Inspect the keyboard, navigation/system bars, cutouts, long translations, RTL, font scaling and display scaling. Find the bottommost required control rather than judging only the first viewport. Verify dialogs and menus remain operable when the keyboard is open.

Separate component saved-state tests from full application restoration. Compose's `StateRestorationTester` can exercise saveable composition state. It does not certify storage, background jobs, navigation tasks or an actual killed process. For process tests, document how the app was backgrounded, how its process ended and how the existing task resumed. Do not equate force-stop, uninstall, rotation and background death.

For permissions, test the current API's applicable grant choices, denial/dismissal, explanation/retry, revocation in settings and return to the app. Check partial photo access, notification permission, location precision or background access only where the app uses them. System permission UI belongs to the system and may need a cross-app test surface.

## Pick selectors and synchronization

Compose UI tests inspect semantic nodes through finders, actions and assertions. Inspect the actual tree before selecting. Merged semantics may expose a parent label instead of a child's expected text. Use an unmerged query only when appropriate to the intended assertion. A test tag supports targeting, but the user's accessible label still needs a real human meaning.

Espresso targets application Views. Use scoped resource IDs and specific matchers when repeated rows or dialogs contain identical text. Register relevant idling resources before the asynchronous operation matters and clean them up afterward. Increasing sleep durations hides timing assumptions and slows every successful run.

UI Automator can interact across applications and system windows. The modern 2.4 API is still under development at the baseline. Verify the selected release before using its DSL. Built-in element waits or tree-stability checks do not establish that background business work completed.

Appium's UiAutomator2 driver is a separate product from the AndroidX UI Automator test library. Select the intended device, W3C capabilities and actual server/driver/client compatibility. Prefer scoped IDs/accessibility selectors over positional XPath. Reacquire elements after navigation or recomposition rather than using stale handles. For hybrid screens, explicitly inspect and select the correct WebView context, with a compatible browser driver and allowed debugging configuration.

For agent-guided exploration, inspect a live hierarchy or a fresh screenshot before every meaningful interaction. Android CLI supports device-selected `input` commands with accessibility selectors and screen capture with explicit PNG output. Inspect current command help rather than inventing selector keys. Coordinate targeting should use the current image and frame, not remembered screen positions after scrolling.

For a form whose inspected resource IDs really are `display_name` and `save_button`, the following native commands replace the text and tap the selected control. Replace `SERIAL` and IDs with the actual target, then run each action separately and inspect the intervening state:

```text
android input --device=SERIAL text --match=single --wait=5000 'Ana' 'id=display_name'
android input --device=SERIAL tap 'id=save_button'
```

String selectors match substrings by default, so short IDs can be ambiguous. Require a unique target and scope it to the inspected screen. The five-second element wait is an explicit example, not proof that validation or saving completed. The text command replaces a value, so it does not replace a real mask/cursor/IME typing case.

## Accessibility and visual acceptance

Run manual TalkBack exploration alongside available accessibility checks. Verify reading order, labels, role/state, heading/group behavior, focus after error/dialog dismissal and a reachable correction path. Contrast or target-size scanners cannot determine whether a confusing label explains the action.

Inspect light/dark and large text on the actual rendered UI. A screenshot baseline needs a recorded API, density, window, font, locale, theme and deterministic fixture. Review differences with intended design changes. Do not approve every new reference image or loosen thresholds until an unexplained regression disappears.

Keep UI correctness, accessibility, visual comparison and performance as separate outcomes. A rendered preview can expose clipping but cannot validate keyboard interaction, actual system dialogs or server persistence.

See [sources](sources.md) for selected ISTQB sections, Android test APIs, state and accessibility guidance. See [execution and evidence](execution-and-evidence.md) for artifacts and result classification.
