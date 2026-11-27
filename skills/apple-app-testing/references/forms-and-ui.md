# Form design, selectors and meaningful UI assertions

Read this for field-level cases, async behavior, UI targeting and accessible acceptance. Use the platform-specific input path from [platform scenarios](platform-scenarios.md).

## Establish the rule before deriving values

For each field, write down whether it is required or optional, the accepted type/range, normalization, length unit, cross-field rules, error text, saving and server mapping. Tell an invalid value apart from a valid empty value, and an untouched field from one the user cleared.

Use typical valid/invalid categories and real limits. A sample quantity rule of 1–10, inclusive, gives 0, 1, a middle value, 10 and 11. A rule such as “valid address and consent required” needs the meaningful combinations of both conditions. These examples show how to build tests. They are not product requirements.

Test invalid categories one at a time before you combine them, so one error does not hide another. Name how you judge every case: shown validation, the value actually submitted, saved state and the next reload. A screenshot alone cannot show the value the server accepted.

## Try real editing

Start with the real input method on the selected platform. Type and paste supported text, edit in the middle, select/replace, delete near a mask separator and clear the field. Check that normalization is intended and does not quietly damage a valid value.

Use accents, combining sequences, emoji and supported writing systems. Confirm the character unit in the rule. User-perceived characters, Unicode code points, UTF-16 code units and UTF-8 bytes are not the same. Do not make up an exact emoji length, and do not change the product's rule to fit a handy string API.

Check placeholder versus a label that stays visible, secure-field behavior, the visibility toggle if there is one, input traits, autofill/password-manager behavior and when validation runs. Autofill can fill several fields without the same keyboard events as typing. Setting text from code is not enough to check cursor behavior, IME composition or a formatting mask.

For numbers, dates and currency, use the supported region, decimal/grouping style, sign and time zone. Check the saved canonical value. Do not assume every currency has two decimals or every “date” is an absolute timestamp. Test boundary dates and time-zone changes only against the stated domain rule.

For choices and attachments, check default/unselected/disabled state, cancellation, choosing again and the file/type/size rejections that apply. Confirm a canceled picker does not submit old data. Use known synthetic files and the real stated byte limit, not a made-up universal upload limit.

## Keyboard and focus acceptance

On iOS/iPadOS, show the software keyboard even when a Mac keyboard is connected. Check the focused field, error and final action above or through the keyboard. Test the set return action and dismissal separately from navigation. Check that moving to the next field scrolls it into a usable area.

On Mac, test keyboard-only first-responder movement, Tab/Shift-Tab, Return, Escape, command shortcuts, menu actions and undo where offered. A shortcut must act on the intended window/document. Confirm that an open sheet blocks unintended actions behind it.

On Apple TV, reach text entry and submission through directional focus. On Watch, choose the real supported entry method. In native visionOS, do the spatial input path by hand through supported simulator/device interactions. Setting a field directly cannot replace any of these usability checks.

## Test concurrent validation and submission

Use a controlled delayed response for value A. Change to B, finish B if that fits, then return A last. Check that the field value, progress and validation still describe B. Also leave the screen while a check is pending and come back, as the screen's state-keeping policy says.

For submission, hold the response long enough to press twice. Check through the approved backend/test interface that only one intended saved operation happened. A disabled control is useful UI evidence, but it cannot prove idempotency (that repeating a request has no extra effect). If the response is lost after the server commits, check the real recovery/sync behavior before retrying.

Test success, field error, general failure, expired sign-in, offline and rate limiting as separate outcomes. Check that drafts are kept where required, that sensitive input is handled safely and that the user can understand how to fix the problem. Do not treat every failure as retryable. Do not go to a success screen just because the request was queued.

Use separate records/accounts for each parallel case. Shared fixtures can create a race or hide one. Cleanup removes only the case's own data and keeps the evidence needed to look into the first failure.

## Choose and verify UI queries

Use XCUIAutomation only for supported app/platform combinations. An existing UI test launches or attaches to the right bundle through `XCUIApplication`, queries controls, performs an action and checks the expected result. It runs apart from the app process, so it cannot read a ViewModel directly as a postcondition.

Prefer stable `accessibilityIdentifier` values for localized or dynamic controls. Limit queries to the current window, sheet or identified row. Keep accessible labels meaningful for users. Do not replace a spoken label with an internal identifier. Do not assume a SwiftUI source view maps one-to-one to an accessibility node.

Tell apart `exists`, enabled state, hittability, selection/value and tvOS focus. Wait for the right state with a finite timeout using the chosen XCTest expectation/wait API. An element can exist and still be unable to take the intended input. An idle app does not mean outside work has finished.

Find elements again after navigation or a state change. Avoid index-based queries and absolute coordinates when a meaningful stable target exists. If a visual-only target needs coordinates, take them from the current frame, record that evidence and check after each action.

Xcode UI recording suggests queries and interactions. Review the chosen queries and add real assertions. Apple's recorder documentation clearly separates a replay with no errors from a checked expected outcome. A workflow can navigate fine while saving the wrong record.

Web content, custom rendering, game engines and third-party UI frameworks need the test surface they really expose. Do not invent a native element. Do not claim that a WebView DOM query works through every native selector. Use the project's existing supported framework before you add another driver.

## Error, accessibility and visual assertions

Check each error's label/link to its field, focus or announcement, kept values and the recovery action offered. Check VoiceOver reading order, role/value/state, keyboard/focus navigation and whether a user can fix the form without relying on color alone. Run Accessibility Inspector on the right screen and variant. Add `performAccessibilityAudit` only where its real platform/API supports it, not as a stand-in for native visionOS UI automation.

Check loading, content, empty and error states under supported language/region, appearance and text settings. Screen captures can show clipping and overlap. They cannot show a working action, correct server ownership or full accessibility. Tie a screenshot baseline to a real runtime/window/font/fixture profile. Review intended changes instead of updating every image until the suite passes.

Use a small acceptance example, such as changing a synthetic profile name, getting a field error, fixing it, submitting twice during a slow response and reloading the record. Then repeat the meaningful input path on each affected platform instead of copying a phone tap sequence everywhere.

See [execution/evidence](execution-and-evidence.md) for reading results and [sources](sources.md) for the real framework and professional test-design material.
