# Form design, selectors and meaningful UI assertions

Read this for field-level cases, asynchronous behavior, UI targeting and accessible acceptance. Apply the platform-specific input path from [platform scenarios](platform-scenarios.md).

## Establish the rule before deriving values

For each field, record required/optional status, accepted type/range, normalization, length unit, cross-field dependencies, error copy, persistence and server mapping. Distinguish an invalid value from a valid absent value and an untouched field from one the user cleared.

Use representative valid/invalid categories and real boundaries. An illustrative inclusive quantity contract of 1–10 produces 0, 1, an interior value, 10 and 11. A rule such as “valid address and consent required” needs the meaningful combinations of both conditions. These examples explain test construction, not product requirements.

Test invalid categories separately before combining them, so one error does not mask another. Name the oracle for every case: displayed validation, actual submitted value, durable state and subsequent reload. A screenshot alone cannot establish the server's accepted value.

## Exercise actual editing

Start with the real input method available on the selected platform. Type and paste supported text, edit in the middle, select/replace, delete near a mask separator and clear the field. Check that normalization is intentional and does not silently corrupt a legitimate value.

Use accents, combining sequences, emoji and supported writing systems. Confirm the contract's character unit. User-perceived characters, Unicode code points, UTF-16 code units and UTF-8 bytes are not equivalent. Do not invent an exact emoji length or change the product's rule to match a convenient string API.

Verify placeholder versus persistent label, secure-field behavior, visibility toggle if offered, input traits, autofill/password-manager behavior and validation timing. Autofill can populate several fields without the same sequence of keyboard events as typing. Programmatic text replacement is not enough to validate cursor behavior, IME composition or a formatting mask.

For numbers, dates and currency, use the supported region, decimal/grouping convention, sign and time zone. Check the stored canonical value. Do not assume every currency has two decimals or every “date” is an absolute timestamp. Test boundary dates and time-zone changes only against the declared domain rule.

For choices and attachments, verify default/unselected/disabled state, cancellation, reselecting and relevant file/type/size rejection. Confirm a canceled picker does not submit stale data. Use known synthetic files and an actual declared byte ceiling instead of an invented universal upload limit.

## Keyboard and focus acceptance

On iOS/iPadOS, show the software keyboard even when a Mac keyboard is connected. Inspect the focused field, error and final action above or through the keyboard. Test the configured return action and dismissal independently from navigation. Check that moving to the next field scrolls it into a usable region.

On Mac, exercise keyboard-only first-responder traversal, Tab/Shift-Tab, Return, Escape, command shortcuts, menu actions and undo where offered. A shortcut must act on the intended window/document. Confirm that an open sheet prevents unintended actions behind it.

On Apple TV, reach text entry and submission using directional focus. On Watch, choose the real supported entry method. In native visionOS, perform the spatial input path manually through supported simulator/device interactions. A direct field assignment cannot replace any of these usability checks.

## Test concurrent validation and submission

Use a controlled delayed response for value A. Change to B, finish B if appropriate, then deliver A last. Observe that field value, progress and validation still describe B. Also navigate away while a check is pending and return according to the screen's state-retention policy.

For submission, hold the response long enough to activate twice. Verify one intended durable operation through the authorized backend/test interface. A disabled control is useful UI evidence but cannot establish idempotency. If the response is lost after server commit, check the actual recovery/reconciliation behavior before retrying.

Exercise success, field error, general failure, expired authentication, offline and rate limiting as separate outcomes. Verify draft retention where required, safe handling of sensitive input and an understandable correction path. Do not treat every failure as retriable or navigate to success because the request was merely queued.

Use independent records/accounts per parallel case. Shared fixtures can manufacture a race or hide one. Cleanup removes only the case's own data and retains the evidence needed to investigate the first failure.

## Choose and verify UI queries

Use XCUIAutomation only for supported application/platform combinations. An existing UI test launches or attaches to the correct bundle through `XCUIApplication`, queries controls, performs an action and checks the expected result. Its execution is separate from the application process, so it cannot directly read a ViewModel as a postcondition.

Prefer stable `accessibilityIdentifier` values for localized or dynamic controls. Scope to the current window, sheet or identified row. Keep accessible labels meaningful for users. Do not replace a spoken label with an internal identifier or assume a SwiftUI source view maps one-to-one onto an accessibility node.

Distinguish `exists`, enabled state, hittability, selection/value and tvOS focus. Wait for the relevant state with a finite timeout using the selected XCTest expectation/wait API. Existence can be true for an element that cannot currently receive the intended input. App idleness does not establish that external work completed.

Reacquire elements after navigation or a state transition. Avoid index-based queries and absolute coordinates when a meaningful stable target exists. If a visual-only target requires coordinates, derive them from the current frame, record that evidence and inspect after each action.

Xcode UI recording proposes queries and interactions. Review the chosen queries and add real assertions. Apple's recorder documentation explicitly distinguishes a replay without errors from an asserted expected outcome. A workflow can navigate successfully while saving the wrong record.

Web content, custom rendering, game engines and third-party UI frameworks need their actual observable test surface. Do not invent a native element or claim a WebView DOM query is available through every native selector. Use the project's existing supported framework before adding another driver.

## Error, accessibility and visual assertions

Verify each error's label/association, focus or announcement, retained values and available recovery action. Check VoiceOver reading order, role/value/state, keyboard/focus navigation and whether a user can correct the form without color alone. Run Accessibility Inspector on the relevant screen and variant. Add `performAccessibilityAudit` only where its actual platform/API supports it, not as a substitute for native visionOS UI automation.

Inspect loading, content, empty and error states under supported language/region, appearance and text settings. Screen captures can reveal clipping and overlap, but not a working action, correct server ownership or complete accessibility. Keep a screenshot baseline tied to a real runtime/window/font/fixture profile and review intentional changes rather than updating every image until the suite passes.

Use a small acceptance example such as changing a synthetic profile name, returning a field error, correcting it, submitting twice during latency and reloading the record. Then repeat the meaningful input path on each affected platform instead of duplicating a phone tap sequence everywhere.

See [execution/evidence](execution-and-evidence.md) for result interpretation and [sources](sources.md) for the actual framework and professional test-design material.
