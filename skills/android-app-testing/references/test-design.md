# Forms, screens and interaction design

Read this when you turn a feature into cases you can observe, or choose how to observe the Android UI. These cases are original uses of well-known test-design techniques, not a copied certification syllabus or a universal product spec.

## Build cases from the real acceptance rules

Start with one normal journey and name what it saves or changes. Find the invalid categories and the real ordered limits. Add a decision table where two conditions affect each other, then model important state changes such as editing → validating → ready → submitting → success/error. Put first the combinations that change behavior, instead of every mathematical combination of device and input.

For a stated inclusive quantity range of 1–10, test 0, 1, 10 and 11, plus a typical middle value. For an action only premium users can take, cover both the account entitlement and input validity, so an invalid field cannot hide a missing entitlement check. These numbers and roles are examples. Replace them with the real contract.

The way you judge a test must tell accepted text apart from shown formatting. A currency field might show grouping and a decimal separator but submit an integer minor-unit value. Check the chosen currency's real fraction rule and negative/zero policy. Do not judge the value from a screenshot alone, and do not assume every currency has two decimal places.

## A practical form session

List field labels, hints, input types, masks, required state and submission behavior. Open the form with the real software keyboard on. A desktop hardware keyboard can hide layout bugs that show up when the IME covers the lower screen.

Try submitting untouched, with one missing field, with one invalid field, after a fix and with a valid form. For each error, check that it belongs to the right field, reads clearly, keeps valid input and handles focus/scroll well. Check that a summary and an inline error do not disagree. Turning off submission and field validation can be separate product choices.

Type, paste, select, replace and delete inside a value. Cover strings with accents, combining marks and supported scripts. Find out whether a limit counts Unicode code points, UTF-16 units, UTF-8 bytes or user-perceived characters. Use a known fixture with the right expected count, and do not make up an exact count by looking at emoji.

Use Next/Done/Search/Send as the real field action says. Press Back once to check that the keyboard closes, then again to check navigation. Test focus order with Tab/Shift+Tab where supported, and make sure a hardware Enter does not submit twice by surprise. Check autofill separately from typing, because it may fill several fields at once.

For masks, check the cursor while editing the middle, pasting a value that is already formatted, deleting near separators and the canonical submitted payload. Test phone country handling, postal-code country choice and date/time-zone rules only for supported regions. A generic regular expression does not show that all real names or addresses are accepted.

## Asynchronous and durable behavior

Hold a validation response for A, change to B and return A last. Look at the new field value, pending state and error/valid indicator. A safe implementation must tie a response to the right input/request, instead of applying whichever one finishes last.

Hold submission long enough to double-tap, leave the screen or lose connectivity. Check the real saved record count and returned identity through an approved test API/database view. A disabled button alone does not prove idempotency (that repeating a request has no extra effect). A timeout can mean the server saved the change but the response was lost. The expected retry/sync behavior must follow the app's contract.

Check field errors, general server failure, expired sign-in and rate limiting separately. Do not expect every error to be retryable. Keep useful draft input where required, and remove sensitive values where required. Write down whether a retry made a new request or matched up with the original operation.

Use separate accounts/data for each parallel case. Two shards that update the same profile can create stale-state failures or hide a real race. Cleanup removes only the records that case created, and never deletes another worker's evidence.

## Screens, transitions and system interaction

Test loading/content/empty/error/offline states with known fixture data. Test list scrolling, paging, refresh, repeated navigation and selection across reloads. Use stable item identities to check that recycled rows do not show another record's image or state.

Open the screen normally, by a supported deep link and after sign-in expires. Check back-stack behavior, and check that a link to a sensitive record still needs server permission. Test a second synthetic account after logout to catch cached account data. This focused isolation check is not a full security audit.

Use real device/window changes for final layout acceptance. Check fold/unfold, split-screen and rotation where supported. Check the keyboard, navigation/system bars, cutouts, long translations, RTL, font scaling and display scaling. Find the lowest required control instead of judging only the first screenful. Check that dialogs and menus still work when the keyboard is open.

Keep component saved-state tests separate from full app restoration. Compose's `StateRestorationTester` can test saveable composition state. It does not certify storage, background jobs, navigation tasks or a really killed process. For process tests, write down how the app went to the background, how its process ended and how the existing task came back. Do not treat force-stop, uninstall, rotation and background death as the same thing.

For permissions, test the current API's grant choices that apply, denial/dismissal, explanation/retry, revocation in settings and returning to the app. Check partial photo access, notification permission, location precision or background access only where the app uses them. The system owns the permission UI, and you may need a cross-app test surface to reach it.

## Pick selectors and synchronization

Compose UI tests look at semantic nodes through finders, actions and assertions. Look at the real tree before you choose. Merged semantics may show a parent label instead of a child's expected text. Use an unmerged query only when it suits the intended assertion. A test tag helps targeting, but the user's accessible label still needs a real meaning for a person.

Espresso targets app Views. Use scoped resource IDs and specific matchers when repeated rows or dialogs contain the same text. Register the idling resources that matter before the async operation starts to matter, and clean them up afterward. Longer sleeps hide timing assumptions and slow down every successful run.

UI Automator can work across apps and system windows. The modern 2.4 API is still in development at the baseline. Check the chosen release before you use its DSL. Built-in element waits or tree-stability checks do not show that background business work finished.

Appium's UiAutomator2 driver is a different product from the AndroidX UI Automator test library. Choose the intended device, W3C capabilities and real server/driver/client compatibility. Prefer scoped IDs/accessibility selectors over positional XPath. Find elements again after navigation or recomposition instead of using stale handles. For hybrid screens, look at and select the right WebView context on purpose, with a matching browser driver and an allowed debugging setup.

For agent-guided exploration, look at a live hierarchy or a fresh screenshot before every meaningful interaction. Android CLI supports device-selected `input` commands with accessibility selectors, `android layout` for the live hierarchy and screen capture with explicit PNG output. Check current command help instead of making up selector keys. Coordinate targeting should use the current image and frame, not screen positions remembered from before scrolling.

For a form whose checked resource IDs really are `display_name` and `save_button`, the native commands below replace the text and tap the selected control. Replace `SERIAL` and the IDs with the real target, then run each action on its own and check the state in between:

```text
android input --device=SERIAL text --match=single --wait=5000 'Ana' 'id=/:id\/display_name$/'
android input --device=SERIAL tap --match=single 'id=/:id\/save_button$/'
```

String selectors match case-insensitive substrings by default, so `id=display_name` would also match `display_name_hint`. The slash-delimited regular expression pins the full resource-name ending. `--match=single` fails and lists the candidates when several elements match. Treat that error as a selector problem to fix, not a reason to switch to `--match=first`. The five-second element wait is a sample value, not proof that validation or saving finished. The text command replaces a value, so it does not replace a real mask/cursor/IME typing case.

## Accessibility and visual acceptance

Explore with TalkBack by hand alongside any accessibility checks you have. Check reading order, labels, role/state, heading/group behavior, focus after an error/dialog closes and a reachable way to fix the problem. Contrast or target-size scanners cannot tell whether a confusing label explains the action.

Check light/dark and large text on the real rendered UI. A screenshot baseline needs a recorded API, density, window, font, locale, theme and a fixture that always gives the same result. Compare differences against intended design changes. Do not approve every new reference image or loosen thresholds until an unexplained regression goes away.

Keep UI correctness, accessibility, visual comparison and performance as separate outcomes. A rendered preview can show clipping, but it cannot check keyboard interaction, real system dialogs or server saving.

See [sources](sources.md) for selected ISTQB sections, Android test APIs, state and accessibility guidance. See [execution and evidence](execution-and-evidence.md) for artifacts and result classification.
