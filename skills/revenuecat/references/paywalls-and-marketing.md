# Paywalls, images, copy, and offer presentation

## Design brief

Collect app style, audience, entry point, value already experienced, feature evidence, subscription versus lifetime/consumable model, locales, accessibility, platform, design assets, and actual package/offer graph. The objective is an informed purchase from a relevant audience, not obscuring cost or cancellation.

Develop a headline around a concrete user outcome. Add a concise supporting line and a few specific benefits connected to real features. For a game, show the actual cosmetic/gameplay benefit without implying pay-to-win behavior the game does not have. For professional/creative tools, clarify unlocked workflows and restrictions. For educational/health/finance products, avoid unsupported performance or medical/financial guarantees.

Use a clear action label matching the actual transaction. Display the full localized recurring price and interval, trial/introductory length and eligibility, subsequent renewal price, cancellation information, restore/manage options, and privacy/terms links. Do not label a paid trial conversion simply "free" without the required surrounding disclosure. Never replace SDK/store prices with a stale marketing string.

## API and CLI design lifecycle

Inspect current `rc paywalls` and asset command schemas. Supported operations include generation/editing, preview/session flows, publishing/unpublishing, attachment, and deletion according to current capability. A generated draft is not a published paywall. Version the reviewed design, link it to the correct offering, and verify compatibility with each target SDK/platform.

Use the supported asset upload contracts. The researched CLI documents image media up to 2 MiB in accepted JPEG/PNG/WebP/AVIF/HEIC/HEIF formats and font uploads up to 5 MiB in TTF/OTF. Recheck the selected endpoint's current format/byte constraints before export. App-store listing media has different rules and is not covered by these paywall upload limits.

Generate supporting artwork with the available image model when useful. Preserve proportions, skin/product realism where relevant, consistent lighting/style, and licensing. Do not fabricate app UI or testimonials. Use genuine app captures when illustrating a feature. Resize/crop intentionally, avoid text embedded in artwork when localization requires live text, and inspect small-screen readability and all supported device orientations.

## Worked CLI lifecycle

These commands were inspected with CLI 0.1.7. Supply actual project/offering IDs and existing app
assets. Inspect `rc commands --json` and each exact schema before use. An unknown nested schema query
can resolve to its parent command in this version. Confirm the returned `path`, runnable command and
arguments. A zero exit status alone does not establish that `paywalls create` or `products import`
exists.

1. Read the app's theme, supported features, font licenses and screenshots. Upload reusable brand
   assets before generation. Record each returned `font_key` and image URL:

   ```text
   rc fonts upload ./Brand-Regular.ttf --project-id "$RC_PROJECT_ID" --json --no-input
   rc fonts upload ./Brand-Semibold.ttf --project-id "$RC_PROJECT_ID" --json --no-input
   rc media-assets upload ./app-logo.png --project-id "$RC_PROJECT_ID" --json --no-input
   ```

   Use the actual `.ttf`/`.otf` files. The font key is the editor reference, not simply the family
   name. Uploading registers the font in the project. Image attachments are visual references only.
   An image must be uploaded and its returned URL supplied to place that real asset in the design.

2. Generate a draft linked to the intended offering. Set `PAYWALL_SESSION` to an ignored local
   session-file path and use that same path across edits:

   ```text
   rc paywalls generate --project-id "$RC_PROJECT_ID" --offering-id "$OFFERING_ID" --name "Plus" --session "$PAYWALL_SESSION" --prompt "A clear monthly and annual paywall matching the app. Use the uploaded brand font keys and logo URL supplied in the context, actual product-price variables, and visible renewal, restore, Terms and Privacy controls." --context "$PAYWALL_CONTEXT" --image ./app-home.png --json --no-input
   ```

   Build `PAYWALL_CONTEXT` from actual non-secret feature/brand facts, uploaded font keys, image URL,
   intended locales and published legal URLs. Keep prompts short and concrete. Do not promise cloud
   sync, invitations or collaboration because a local app happens to support named groups.
   An offering supports one attached paywall. If it already has one, inspect/edit that design rather
   than detaching a published paywall to make a generation command succeed.

3. Inspect the returned preview path, draft ID, activity and builder URL. If the editor asks a
   clarification, answer in an edit on the same session. Make a focused change per turn:

   ```text
   rc paywalls edit --project-id "$RC_PROJECT_ID" --session "$PAYWALL_SESSION" --prompt "Add complete English, Brazilian Portuguese and Spanish localizations, preserving the uploaded fonts, product-price variables and the real Terms and Privacy URLs." --json --no-input
   ```

   Inspect every required localization's benefits, billing period, annual full price, renewal terms,
   purchase label, restore action and legal links. Use actual required locale keys from the current
   paywall contract. Do not infer success from one English preview. Read session/design JSON for
   inspection, but change the draft through the editor or documented builder. Hand-editing the local
   session can lose work or conflict with revision guards. Reuse returned IDs after interruptions.

4. Account for preview limits before requesting more design changes. The 0.1.7 renderer deliberately
   omits Restore Purchases buttons. Inspect the `restore_purchases` action in the design and verify
   the control in the native app. CLI previews may also omit custom font rendering. Inspect the
   builder and the integrated SDK before treating a fallback font as a design defect. Any sample
   prices in a preview are illustrative. Verify product-price variables and actual store prices.

5. Present the concrete preview and builder URL for the user's design approval, as required by the
   CLI's publish guidance. Honor an existing approval of that same design and audience. Explain
   illustrative prices and known preview omissions. After approval, publish the actual returned
   paywall ID:

   ```text
   rc paywalls publish "$PAYWALL_ID" --project-id "$RC_PROJECT_ID" --yes --json --no-input
   rc paywalls show "$PAYWALL_ID" --project-id "$RC_PROJECT_ID" --json --no-input
   rc offerings verify "$OFFERING_ID" --project-id "$RC_PROJECT_ID" --json --no-input
   ```

   Verify its actual attachment, publication state and SDK-visible components for each app. If the
   design was generated standalone, use `rc paywalls attach` with the intended paywall/offering IDs
   within the authorized customer-facing scope. Publishing a standalone design does not establish
   that the current offering serves it. Setting an offering current is a separate operation.

6. Rebuild/reinstall if the client's public keys or integration changed, then present the actual
   native paywall. Verify real store prices, locale fallback, font rendering, folded/unfolded layouts,
   scrolling to the footer, accessible close/restore/purchase controls and real legal destinations.
   Record native UI checks separately from a completed sandbox purchase or restoration. Follow
   [testing and operations](testing-and-operations.md) for transaction and lifecycle coverage.

## Accessibility and layout

Check Dynamic Type/font scaling, VoiceOver/TalkBack labels and order, keyboard/remote focus, contrast, reduced motion, localization expansion, right-to-left layout, and safe areas. Use platform-appropriate purchase UI for macOS, TV, and spatial devices rather than stretching a phone design. Ensure close/restore/terms controls remain usable and are not covered by artwork.

Review portrait, landscape, tablet, folded/unfolded, and other actual supported target layouts. No overlapping text, clipped price, deceptive preselection, hidden renewal terms, or distorted icons. A design preview must be checked in the real integrated app with real localized product data.

## Experiments and launch

Choose one hypothesis, target audience, primary metric, observation period, and guardrails such as refunds, retention, cancellation and support issues. Use available targeting/experimentation tools with actual account support. Avoid changing price, audience, and copy simultaneously without a plan to interpret the result.

Publishing a paywall or setting a current offering can affect existing production clients without a binary release. Verify product readiness, SDK compatibility, localization, audience targeting, and user authorization before those transitions. Re-read current SDK-visible configuration afterward. Report conversion evidence honestly and do not guarantee revenue or ranking improvements.

Store title/subtitle/description/keywords/tags/promotional text belong to the corresponding Apple/Google listing workflow. RevenueCat product identifiers, offering metadata, and paywall text are not substitutes for store ASO fields. Keep names and promises consistent across these surfaces.
