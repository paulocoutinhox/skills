# Policy and review readiness

Verified on **2026-11-05** against the [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) and current Connect submission/help surfaces. Apply the current full rule to the actual app, territory and distribution route. This matrix routes the guideline families and practical evidence. It does not reproduce every exception or certify legal compliance.

## Review the implementation, not just the forms

Inspect the release binary, backend, entitlements, embedded SDKs, account flows, all visible features, paywalls and every claimed locale/platform. A declaration must match that implementation. For each applicable area record the actual guideline/requirement, source date, owner answer, artifact and test evidence. Mark **PASSED**, **FAILED**, **BLOCKED** or **NOT APPLICABLE with reason** in [the evidence template](../assets/release-evidence.md).

| Guideline family | What to verify and how |
| --- | --- |
| 1.1 Objectionable content | Inspect text, game scenes, generated content and public art for prohibited abuse, hateful/sexual/deceptive/dangerous material. Age ratings do not excuse prohibited content. |
| 1.2 UGC/creator content | Exercise filtering, report, block, moderation response and published contact. Include AI content creation and hosted user experiences where applicable. Test age restriction for content exceeding the app rating. |
| 1.3 Kids | Apply the actual Kids-category contract, parental gates, data/advertising/analytics constraints and age-appropriate experience. Do not select Kids as an ASO tactic or assume deselecting it erases established obligations. |
| 1.4 Physical harm | Substantiate actual medical/measurement/safety capabilities, applicable licenses and warnings. Do not invent diagnostic efficacy. Check dangerous activities and controlled-content restrictions. |
| 1.5–1.7 Developer contact, security, crime reporting | Reachable in-app/support contact, appropriate data protection and required local-authority involvement for crime-reporting apps. |
| 2.1 Completeness | No placeholders, dead links, unfinished visible features or crashes. Backend and demo access work throughout review. Every IAP is accessible or explained accurately. |
| 2.2 Beta testing | Use TestFlight for beta distribution and its actual review/audience rules. Do not market a beta/demo as a finished store release. |
| 2.3 Accurate metadata | Name, subtitle, descriptions, price claims, categories, ratings and media match shipped behavior. Explain material changes and paid features. Do not hide new functionality from review. |
| 2.4 Hardware compatibility | Test actual supported hardware/input, resource use and target-specific behavior, including native Mac requirements and relevant accessibility. Unsupported devices are not justified by a phone-only smoke test. |
| 2.5 Software requirements | Public supported APIs, correct entitlement/background/extension behavior, privacy manifests/reason APIs and SDK compliance. No private API or downloaded code that violates the current permitted-software rules. |
| 3.1 Payments | Classify digital versus physical goods/services and permitted purchase routes. Check actual storefront/program/entitlement exceptions before external payment links. Use store purchases where required and disclose paid boundaries. |
| 3.1.2 Subscriptions | Genuine ongoing value, clear plan/price/period/trial/renewal/cancellation information, correct group/upgrade behavior and restoration. Prevent unintended simultaneous variants of the same service. |
| 3.2 Business models | Review real-money schemes, regulated finance, donations, gifts, advertising incentives and other actual model restrictions. Do not gate functionality on ratings/downloads or manipulate engagement. |
| 4.1–4.3 Originality, utility, spam | Meaningful app-specific utility/entertainment, authorized branding and distinct content. No reskin flood, impersonation, low-value wrapper or duplicate bundle IDs used to evade review. |
| 4.4–4.6 Extensions, services, alternate icons | Check actual host/extension responsibilities, Apple service use, notifications, branding and alternate-icon content/claims. Test the real extension/service integration. |
| 4.7 Mini apps, streaming software, plug-ins and emulators | Apply the current allowed-software scope, content index/deep links, moderation, age restrictions, payments and per-software consent. Do not assume this permits arbitrary native API exposure. |
| 4.8 Login services | Evaluate third-party primary-account login against the required equivalent privacy-preserving option and documented exceptions. Do not declare Sign in with Apple universally mandatory for every own-account or enterprise app. |
| 4.9–4.10 Apple Pay and built-in capabilities | Disclose actual payment/renewal/cancellation terms and use appropriate branding. Do not sell bare access to built-in hardware/OS services contrary to the rule. |
| 5.1 Privacy | Public policy and in-app access, actual consent, data minimization, purpose strings, tracking/ATT, account deletion and SDK disclosures. Check data use, health/research, children and location branches as applicable. |
| 5.1.2 Data sharing | Disclose the actual recipients/purposes of personal-data sharing, including third-party AI, and obtain required explicit permission before transfer. A generic policy link alone is insufficient consent. |
| 5.2 Intellectual property | Verify distribution/content/music/brand rights and authorized third-party service access. Keep evidence for review rather than assuming public availability means permission. |
| 5.3–5.5 Games of chance, VPN and device management | Check the current specialized licensing, territorial, data-use and organization/program requirements for the actual feature. Do not answer these as a generic utility. |
| 5.6 Developer conduct | Accurate identity, honest discovery/ratings/support behavior and response to actual quality complaints. Do not manipulate review, hide behavior or mislead customers. |

## Complete factual Connect declarations

Use [the field guide](store-fields-and-localizations.md) for age ratings, export encryption, accessibility, content rights, policy URLs and EULA. Complete unsupported owner/legal/account forms in the actual console, including App Privacy publication, tax/trader facts and applicable regional/medical-device/distribution declarations. A filled API field is not evidence of a completed console task.

Maintain a data-flow inventory for app, backend and every third-party SDK. Compare App Privacy answers, tracking consent, actual network behavior, privacy manifests and policy text. An app with no advertising SDK may still collect account/payment/diagnostic data. Do not silently answer “no data collected”.

For account creation, verify actual in-app deletion and the treatment of legally retained records. For restricted content or review-only access, provide a stable working path that does not depend on a reviewer receiving private SMS, joining a waitlist, buying inaccessible hardware without instructions or waiting for manual account approval.

## Release acceptance cases

- Install and launch the signed release on supported platform/device types. Check login/logout, permissions accepted/denied, account deletion, empty/error/network states and complete core flows.
- Verify every visible paid product, localized price, trial/offer disclosure, purchase, pending/cancel/error behavior, restore and entitlement expiry/revocation against the actual integration owner.
- Navigate every first-session and nonobvious feature using only supplied reviewer notes. Keep the backend and test account functional for the entire review window.
- Compare every metadata claim and screenshot with actual release behavior. Verify all URLs and required capture families, translations and store placement processing.
- Verify app-download price, territories, preorder/release timing and existing subscriber consequences independently from binary processing.
- For an update, test existing customer data and service behavior in addition to clean installation. Removing unnecessary source compatibility layers does not authorize loss of existing users' data or entitlements.

Static validation, an approved TestFlight build and a complete submission graph cannot replace these execution checks. Record actual gaps and block a release-ready conclusion for known mandatory failures. Final acceptance remains Apple's decision.
