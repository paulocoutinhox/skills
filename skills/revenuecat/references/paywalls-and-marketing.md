# Paywalls, images, copy, and offer presentation

## Design brief

Collect the app style, audience, entry point, value the user has already seen, evidence for features, the subscription versus lifetime or consumable model, locales, accessibility, platform, design assets, and the real package and offer setup. The goal is an informed purchase by a relevant audience, not hiding cost or cancellation.

Build the headline around a concrete result for the user. Add a short supporting line and a few specific benefits tied to real features. For a game, show the real cosmetic or gameplay benefit without hinting at pay-to-win behavior the game does not have. For professional and creative tools, make clear which workflows unlock and what the limits are. For education, health and finance products, avoid performance, medical or financial promises you cannot back up.

Write paywall copy as the app talking to its customers about the product. Generation prompts, context files and design reasons stay internal. The published text never describes how it was made and never mentions AI, agents, tools or prompts unless the owner clearly asks. Check every generated locale for leaked prompt wording, placeholders or meta comments before approval.

Use a clear action label that matches the real transaction. Show the full localized recurring price and interval, the trial or introductory length and eligibility, the renewal price after that, cancellation information, restore and manage options, and privacy and terms links. Do not call a paid trial conversion simply "free" without the required disclosure around it. Never replace SDK or store prices with an old marketing string.

## API and CLI design lifecycle

Check the current `rc paywalls` and asset command schemas. Supported operations include generating and editing, preview and session flows, publishing and unpublishing, attaching, and deleting, depending on current capability. A generated draft is not a published paywall. Version the reviewed design, link it to the correct offering, and check that it works with each target SDK and platform.

Use the supported asset upload contracts. The researched CLI documents image media up to 2 MiB in accepted JPEG/PNG/WebP/AVIF/HEIC/HEIF formats and font uploads up to 5 MiB in TTF/OTF. Check the chosen endpoint's current format and byte limits again before export. App-store listing media has different rules and is not covered by these paywall upload limits.

Generate supporting artwork with the available image model when it helps. Keep proportions, realistic skin and products where relevant, consistent lighting and style, and licensing. Do not fake app UI or testimonials. Use real app captures when showing a feature. Resize and crop on purpose, avoid text baked into artwork when localization needs live text, and check readability on small screens and in all supported device orientations.

## Worked CLI lifecycle

These commands target CLI 0.1.8. Give the real project and offering IDs and existing app
assets. Check `rc commands --json` and each exact schema before use. In this version, an unknown
nested schema query can resolve to its parent command. Confirm the returned `path`, runnable command
and arguments. A zero exit status alone does not show that `paywalls create` or `products import`
exists.

1. Read the app's theme, supported features, font licenses and screenshots. Upload reusable brand
   assets before generating. Record each returned `font_key` and image URL:

   ```text
   rc fonts upload ./Brand-Regular.ttf --project-id "$RC_PROJECT_ID" --json --no-input
   rc fonts upload ./Brand-Semibold.ttf --project-id "$RC_PROJECT_ID" --json --no-input
   rc media-assets upload ./app-logo.png --project-id "$RC_PROJECT_ID" --json --no-input
   ```

   Use the real `.ttf`/`.otf` files. The font key is what the editor refers to, not just the family
   name. Uploading adds the font to the project. Image attachments are only visual references.
   To place a real image in the design, upload it and give its returned URL.

2. Generate a draft linked to the intended offering. Set `PAYWALL_SESSION` to an ignored local
   session-file path and use that same path for all edits:

   ```text
   rc paywalls generate --project-id "$RC_PROJECT_ID" --offering-id "$OFFERING_ID" --name "Plus" --session "$PAYWALL_SESSION" --prompt "A clear monthly and annual paywall matching the app. Use the uploaded brand font keys and logo URL supplied in the context, actual product-price variables, and visible renewal, restore, Terms and Privacy controls." --context "$PAYWALL_CONTEXT" --image ./app-home.png --json --no-input
   ```

   Build `PAYWALL_CONTEXT` from real non-secret facts about features and brand, uploaded font keys,
   the image URL, intended locales and published legal URLs. Keep prompts short and concrete. Do not
   promise cloud sync, invitations or collaboration just because a local app supports named groups.
   An offering can have one attached paywall. If it already has one, check and edit that design
   instead of detaching a published paywall to make a generate command work.

3. Look at the returned preview path, draft ID, activity and builder URL. If the editor asks a
   question, answer it in an edit on the same session. Make one focused change per turn:

   ```text
   rc paywalls edit --project-id "$RC_PROJECT_ID" --session "$PAYWALL_SESSION" --prompt "Add complete English, Brazilian Portuguese and Spanish localizations, preserving the uploaded fonts, product-price variables and the real Terms and Privacy URLs." --json --no-input
   ```

   Check every required localization's benefits, billing period, full annual price, renewal terms,
   purchase label, restore action and legal links. Use the real required locale keys from the current
   paywall contract. Do not assume success from one English preview. Read the session and design JSON
   to check them, but change the draft through the editor or the documented builder. Hand-editing the
   local session can lose work or clash with revision guards. Reuse returned IDs after an
   interruption.

4. Allow for preview limits before asking for more design changes. CLI previews leave out
   Restore Purchases buttons on purpose. Check the `restore_purchases` action in the design and test
   the control in the native app. CLI previews may also not show custom fonts. Check the builder and
   the integrated SDK before treating a fallback font as a design defect. Any sample prices in a
   preview are only examples. Check product-price variables and real store prices.

5. Show the concrete preview and builder URL to the user for design approval, as the CLI's publish
   guidance requires. Respect an existing approval of that same design and audience. Explain sample
   prices and known preview gaps. After approval, publish the real returned paywall ID:

   ```text
   rc paywalls publish "$PAYWALL_ID" --project-id "$RC_PROJECT_ID" --yes --json --no-input
   rc paywalls show "$PAYWALL_ID" --project-id "$RC_PROJECT_ID" --json --no-input
   rc offerings verify "$OFFERING_ID" --project-id "$RC_PROJECT_ID" --json --no-input
   ```

   Check its real attachment, publish state and the components the SDK sees for each app. If the
   design was generated on its own, use `rc paywalls attach` with the intended paywall and offering
   IDs, within the allowed scope for changes customers see. Publishing a standalone design does not
   mean the current offering serves it. Setting an offering current is a separate operation.

6. Rebuild and reinstall if the client's public keys or integration changed, then show the real
   native paywall. Check real store prices, locale fallback, font rendering, folded and unfolded
   layouts, scrolling to the footer, accessible close, restore and purchase controls and real legal
   pages. Record native UI checks apart from a completed sandbox purchase or restore. Follow
   [testing and operations](testing-and-operations.md) for transaction and lifecycle coverage.

## Accessibility and layout

Check Dynamic Type and font scaling, VoiceOver/TalkBack labels and order, keyboard and remote focus, contrast, reduced motion, text growth in other languages, right-to-left layout, and safe areas. Use purchase UI that suits macOS, TV, and spatial devices instead of stretching a phone design. Make sure close, restore and terms controls stay usable and are not covered by artwork.

Review portrait, landscape, tablet, folded and unfolded, and any other real supported target layouts. No overlapping text, cut-off price, misleading preselection, hidden renewal terms, or distorted icons. Check a design preview in the real integrated app with real localized product data.

## Experiments and launch

Choose one hypothesis, target audience, main metric, observation period, and guardrails such as refunds, retention, cancellation and support issues. Use the targeting and experiment tools your account really supports. Avoid changing price, audience, and copy at the same time without a plan for reading the result.

Publishing a paywall or setting a current offering can change existing production apps without a binary release. Check product readiness, SDK compatibility, localization, audience targeting, and the user's permission before those changes. Read the current configuration the SDK sees again afterward. Report conversion evidence honestly and do not promise more revenue or better rankings.

Store title, subtitle, description, keywords, tags and promotional text belong to the matching Apple or Google listing workflow. RevenueCat product identifiers, offering metadata, and paywall text do not replace store ASO fields. Keep names and promises consistent across all of them.
