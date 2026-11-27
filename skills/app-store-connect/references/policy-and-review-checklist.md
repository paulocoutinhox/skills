# Policy and review readiness

Checked on **2026-11-05** against the [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) and current Connect submission and help pages. Apply the full current rule to the real app, territory and distribution route. This table points to the guideline families and the practical evidence. It does not copy every exception or certify legal compliance.

## Review the implementation, not just the forms

Check the release binary, backend, entitlements, embedded SDKs, account flows, all visible features, paywalls and every locale and platform you claim. A declaration must match the code. For each area that applies, record the real guideline or requirement, source date, owner answer, file and test evidence. Mark **PASSED**, **FAILED**, **BLOCKED** or **NOT APPLICABLE with reason** in [the evidence template](../assets/release-evidence.md).

| Guideline family | What to verify and how |
| --- | --- |
| 1.1 Objectionable content | Check text, game scenes, generated content and public art for banned abusive, hateful, sexual, misleading or dangerous material. Age ratings do not excuse banned content. |
| 1.2 UGC/creator content | Test filtering, reporting, blocking, moderation response and the published contact. Include AI content creation and hosted user experiences where they apply. Test age limits for content above the app rating. |
| 1.3 Kids | Apply the real Kids-category contract, parental gates, limits on data, advertising and analytics, and an experience that fits the age. Do not pick Kids as an ASO trick or assume that unselecting it removes duties you already have. |
| 1.4 Physical harm | Back up real medical, measurement and safety features, licenses that apply and warnings. Do not make up how well a diagnosis works. Check dangerous activities and limits on controlled content. |
| 1.5–1.7 Developer contact, security, crime reporting | Reachable in-app or support contact, suitable data protection and the required involvement of local authorities for crime-reporting apps. |
| 2.1 Completeness | No placeholders, dead links, unfinished visible features or crashes. Backend and demo access work for the whole review. Every IAP can be reached or is explained accurately. |
| 2.2 Beta testing | Use TestFlight for beta distribution and follow its real review and audience rules. Do not market a beta or demo as a finished store release. |
| 2.3 Accurate metadata | Name, subtitle, descriptions, price claims, categories, ratings and media match how the shipped app behaves. Explain important changes and paid features. Do not hide new features from review. |
| 2.4 Hardware compatibility | Test real supported hardware and input, resource use and target-specific behavior, including native Mac requirements and relevant accessibility. A quick test on a phone does not justify devices you did not test. |
| 2.5 Software requirements | Public supported APIs, correct entitlement, background and extension behavior, privacy manifests and reason APIs, and SDK compliance. No private API or downloaded code that breaks the current rules on allowed software. |
| 3.1 Payments | Sort digital from physical goods and services and find the allowed purchase routes. Check the real store, program and entitlement exceptions before adding outside payment links. Use store purchases where required and show what is paid. |
| 3.1.2 Subscriptions | Real ongoing value, clear plan, price, period, trial, renewal and cancellation information, correct group and upgrade behavior and restore. Prevent unwanted parallel variants of the same service. |
| 3.2 Business models | Review real-money schemes, regulated finance, donations, gifts, advertising rewards and other real model limits. Do not lock features behind ratings or downloads or manipulate engagement. |
| 4.1–4.3 Originality, utility, spam | Real usefulness or entertainment specific to the app, allowed branding and its own content. No flood of reskins, impersonation, low-value wrapper or duplicate bundle IDs used to get around review. |
| 4.4–4.6 Extensions, services, alternate icons | Check the real host and extension duties, Apple service use, notifications, branding and alternate-icon content and claims. Test the real extension or service integration. |
| 4.7 Mini apps, streaming software, plug-ins and emulators | Apply the current scope of allowed software, content index and deep links, moderation, age limits, payments and consent for each piece of software. Do not assume this allows exposing any native API. |
| 4.8 Login services | Check third-party login for the main account against the required equal option that protects privacy and the documented exceptions. Do not say Sign in with Apple is required for every app with its own accounts or for every enterprise app. |
| 4.9–4.10 Apple Pay and built-in capabilities | Show the real payment, renewal and cancellation terms and use the right branding. Do not sell plain access to built-in hardware or OS services against the rule. |
| 5.1 Privacy | Public policy and access in the app, real consent, collecting only the data needed, purpose strings, tracking/ATT, account deletion and SDK disclosures. Check the data use, health and research, children and location rules where they apply. |
| 5.1.2 Data sharing | Disclose who really receives personal data and why, including third-party AI, and get the required clear permission before sending it. A plain policy link is not enough consent. |
| 5.2 Intellectual property | Check distribution, content, music and brand rights and allowed access to third-party services. Keep evidence for review instead of assuming that public availability means permission. |
| 5.3–5.5 Games of chance, VPN and device management | Check the current special licensing, territory, data-use and organization or program requirements for the real feature. Do not answer these as for a general utility. |
| 5.6 Developer conduct | Accurate identity, honest discovery, ratings and support behavior and a response to real quality complaints. Do not manipulate review, hide behavior or mislead customers. |

## Complete factual Connect declarations

Use [the field guide](store-fields-and-localizations.md) for age ratings, export encryption, accessibility, content rights, policy URLs and EULA. Complete owner, legal and account forms the API does not support in the real console, including App Privacy publishing, tax and trader facts and any regional, medical-device or distribution declarations that apply. A filled API field does not prove a console task is done.

Keep a list of data flows for the app, backend and every third-party SDK. Compare App Privacy answers, tracking consent, real network behavior, privacy manifests and policy text. An app with no advertising SDK may still collect account, payment or diagnostic data. Do not quietly answer “no data collected”.

For account creation, check real in-app deletion and how records kept for legal reasons are handled. For restricted content or review-only access, give a stable working path that does not depend on the reviewer getting a private SMS, joining a waitlist, buying hardware they cannot get without instructions or waiting for manual account approval.

## Release acceptance cases

- Install and launch the signed release on supported platform and device types. Check login/logout, permissions accepted and denied, account deletion, empty, error and network states and complete core flows.
- Check every visible paid product, localized price, trial or offer disclosure, purchase, pending/cancel/error behavior, restore and entitlement expiry or revocation against the real owner of the integration.
- Go through every first-session feature and every feature that is not obvious using only the reviewer notes you gave. Keep the backend and test account working for the whole review period.
- Compare every metadata claim and screenshot with how the release really behaves. Check all URLs and required capture families, translations and store placement processing.
- Check app download price, territories, preorder and release timing and the effects on existing subscribers separately from binary processing.
- For an update, test existing customer data and service behavior as well as a clean install. Removing source compatibility layers you do not need does not allow losing existing users' data or entitlements.

Static validation, an approved TestFlight build and a complete set of submission items cannot replace these real checks. Record real gaps and do not call a release ready when a required item is known to fail. Apple makes the final decision.
