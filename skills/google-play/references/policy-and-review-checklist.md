# Policy, app content and review readiness

Checked on **2026-11-05** against the [Policy Center](https://play.google/developer-content-policy/), [review preparation](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en) and [publishing statuses](https://support.google.com/googleplay/android-developer/answer/9859751?hl=en). Apply the real current policy and the console tasks for this app. This guide points to policy families and the evidence they need. It does not cover every regional exception or legal requirement.

## Establish factual coverage

Inspect the real signed release, backend, SDKs, permissions, account and payment flows, audience and every declared device, locale and country. List the requirements that apply, the facts, owners and tests in [the evidence template](../assets/release-evidence.md). Use PASSED, FAILED, BLOCKED or NOT APPLICABLE with a reason. API validation does not prove policy compliance.

| Policy area | What to inspect and demonstrate |
| --- | --- |
| Child safety and inappropriate content | Real content and assets, age access, protection from exploitation, banned sexual, violent, hateful or dangerous material and the social or dating duties that apply. A high age rating does not allow banned content. |
| Age-restricted features | Real access controls and the age-check and territory rules that apply. Do not guess a user's age from an unchecked account flag or a marketing target. |
| Financial services | Real provider identity, permissions and licenses, and honest disclosures for finance, loans and investments. Pick the specific financial-feature declarations instead of a generic category answer. |
| Gambling, games, contests, illegal activity | Real business model, allowed countries and licenses. Tell ordinary in-game currency apart from real-money or outside-value schemes. |
| UGC | Terms acceptance, moderation, report and block controls, quick action and protection against abusive or illegal content. Test the real reporting and blocking flows. |
| Health and medical content | Accurate claims, the medical-device or health-app declarations that apply, handling of sensitive data and required evidence. Do not claim a feature can diagnose anything unless you can back it up. |
| Blockchain and tokenized assets | Real financial and compliance declarations, allowed sale and reward mechanics and honest product metadata. Do not turn on such flags without a real product reason. |
| AI-generated content | Prevent banned generated content and provide the required in-app reporting or flagging where the policy applies. Inspect the generated-content workflows, not only the static store artwork. |
| Impersonation and IP | Authorized developer and brand identity, assets and access to third-party services. No copying a competitor's icon or title, and no false official affiliation. |
| User data | An accurate public policy, a clear in-app disclosure and consent where required, secure handling and the real SDK and backend collection and sharing. Make every answer match the behavior you observe. |
| Account deletion | Where users can create accounts, provide the required in-app and outside deletion request paths, describe how data is really treated and kept, and test the flow. A support email alone does not prove compliance. |
| Permissions and sensitive APIs | A reason tied to the core use, scoped permissions, denied states and the real approvals and declarations for sensitive access. Check SMS and call logs, background location, accessibility, broad files and photos, health, VPN, full-screen intents and any other privileges the app really requests. |
| Device/network abuse and deceptive behavior | No hidden features, unauthorized installs or actions, abusive background behavior, fake system UI, misleading billing or attempts to dodge review. |
| SDK and target/platform requirements | Check every embedded SDK, current target API and Billing deadlines, native compatibility and the quality of supported form factors. An SDK vendor's claim does not move the responsibility away from the developer. |
| Payments and subscriptions | Required Play Billing or a real eligible alternative program, honest paid limits, total recurring price, period and trial, cancellation and restored access. No misleading subscription purchase path. |
| Ads | An accurate Contains ads declaration, suitable content, placement and close behavior, and no deceptive or disruptive interaction. Check launch, navigation, gameplay and focus flows and all ad SDK behavior. |
| Families | Real target age groups, data and content suitable for children, eligible ad SDKs and parental and age-related controls. Do not choose an adults-only audience to hide a design aimed at children. |
| Metadata and promotion | Honest title, descriptions and art, suitable public content, and no ranking or price badges, keyword stuffing, misleading affiliation or unsupported claims in any locale. |
| Ratings, reviews, installs and content rating | Honest rating prompts and acquisition, and the real rating questionnaire. Do not buy ratings, make up testers or reward misleading feedback. |
| News/government/other regulated identities | Real sourcing, publisher or official affiliation, app content declarations and the licensing that applies. Do not suggest a link to an institution through generic branding. |
| Spam, functionality and UX | Useful features or content specific to the app, a stable install, load, input and core flow, accessible and readable screens and no dead visible features. Better listing copy alone cannot fix repeated reskins or broken apps. |
| Malware and unwanted software | No harmful code, ad fraud, hostile download behavior, social engineering or unauthorized imitation of system functions. Inspect included dependencies and the behavior you ship. |
| Device programs | Apply the real active Wear OS, TV, Auto/Automotive, large-screen/PC and XR requirements only for supported release targets. Do not add discontinued programs because an old policy link still exists. |
| Enforcement and account standing | Current account identity and verification, policy status, deadlines and the real action type. Update rejection, app removal and suspension each have different fix and appeal paths. |

## Complete App content and supported declarations

The current App content page splits tasks into Needs attention and Actioned. Look at both the open requirements that apply and the saved answers. Tasks can include privacy policy, ads, sign-in details and app access, audience, content rating, Data safety, sensitive permissions, health and financial features and regional requirements. Do not call a task complete because you prepared an answer locally.

For the privacy policy, provide a public webpage for this app and in-app access to it, even when you claim no personal data is collected. The current review guidance requires access from everywhere without login or geofencing, and a normal webpage instead of a PDF or download. Match the real collection, use, sharing, retention and contact information. Keep required deletion URLs separate from an ordinary marketing site.

For ads, include the real third-party SDK, house, native, banner and interstitial behavior. In-app purchase prompts alone do not automatically count as advertising for the declaration. Use the current rule instead of guessing from a UI label.

For restricted access, set up stable reviewer credentials and exact instructions for every protected feature. Explain real MFA/OTP, multiple-field, location or hardware requirements through the supported sign-in instructions. Do not require personal social accounts, payment or a waitlist to see core features. Keep sensitive credentials out of public release records.

Data safety has a supported standalone API: `applications.dataSafety`, using the current official CSV contents in `safetyLabels`. Other ordinary App content tasks are not fields in `Listing` or `AppDetails`. Prepare the full factual answer, and do the supported console step when no method exists.

### Advertising ID, audience and actual saved state

Read the **final merged release manifest**, not only the app's source manifest. SDK manifests can
add `com.google.android.gms.permission.AD_ID`. Inspect how the identifier is really used and why,
including SDK behavior after consent. Contains ads is a separate declaration. An app with no ads can
still use an identifier for analytics. On the other hand, a permission string alone does not prove
every possible collection or advertising purpose. Trace the embedded SDK setup and the real data flows.

For Firebase Analytics, inspect the current platform-specific collection and identifier controls
instead of assuming that turning off collection at first launch means no collection later. If the
behavior or permission changes, rebuild and repeat the factual declaration review. Do not remove a
permission only to avoid answering a form, or declare no data because the SDK was idle during one
launch.

Complete the IARC questionnaire honestly and keep the regional results it produces. Choose target
age groups from the real product and audience, separately from the generated rating. Optional
controls that block minors, and trader and legal answers, each need their own facts. Do not reuse
another app's chosen answers as a list of defaults.

After saving a restricted-access instruction, check that both its child dialog and the parent page
saved. Confirm every relevant task is actioned, then check the Dashboard prerequisites and Publishing
overview. This ties the factual policy work to the real [first-release flow](first-production-release.md).

## Reviewer and release verification

1. Check the exact AAB, version and signature, and install the release-equivalent build on the device families you claim. Check a clean install, an update from the current production version and the real core flows.
2. Test account access and deletion, allowed and denied permissions, empty, loading and error states, offline and recovery behavior and backend availability. Keep existing customers' data and entitlements.
3. Try products, localized prices, eligibility, pending, cancel, error and restore, and the real fulfillment and renewal state. A catalog ACTIVE response does not prove the client handles entitlements correctly.
4. Compare every localized claim and image with the real shipped app. Check the support, privacy and deletion links, target requirements and all required form-factor assets.
5. Inspect the pre-review checks and pre-launch reports and fix crashes, access problems and policy failures you can act on. A clean automated report does not cover every user workflow.
6. Check the account's production-access eligibility, the intended track and countries, managed publishing and every separate product, price and declaration change.
7. Inspect the real Publishing overview and review messages and the submission state. Keep app, update and per-item status separate. Use [the correction/resubmission procedure](edits-review-and-rollout.md) for failures.

For each defect, record the requirement or message, how to reproduce it, the change that fixes it, the replacement artifact or resource and the retest result you saw. A fix that only touches metadata or access can keep an eligible existing binary. A code fix needs a fresh reserved higher version code. A suspended app may need the real appeal route instead of another ordinary release commit.

Customer reviews are a different surface: `reviews.reply` is a public message and does not answer a policy reviewer. Draft policy responses and appeals with concrete evidence, and send them only within the user's real messaging authorization. Do not make up an approval receipt or guarantee how long review takes.
