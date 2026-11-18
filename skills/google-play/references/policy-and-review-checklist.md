# Policy, app content and review readiness

Verified on **2026-11-05** against the [Policy Center](https://play.google/developer-content-policy/), [review preparation](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en) and [publishing statuses](https://support.google.com/googleplay/android-developer/answer/9859751?hl=en). Apply the actual current policy and app-specific console tasks. This routes policy families and evidence, not every regional exception or legal requirement.

## Establish factual coverage

Inspect the actual signed release, backend, SDKs, permissions, account/payment flows, audience and every declared device/locale/country. List applicable requirements, facts, owners and tests in [the evidence template](../assets/release-evidence.md). Use PASSED, FAILED, BLOCKED or NOT APPLICABLE with a reason. API validation does not certify policy compliance.

| Policy area | What to inspect and demonstrate |
| --- | --- |
| Child safety and inappropriate content | Actual content/assets, age access, protection from exploitation, prohibited sexual/violent/hateful/dangerous material and applicable social/dating obligations. A high age rating does not permit prohibited content. |
| Age-restricted features | Real access controls and applicable age-assurance/territorial requirements. Do not infer a user's age from an unverified account flag or a marketing target. |
| Financial services | Actual provider identity, permissions/licenses and truthful disclosures for finance/loans/investments. Select the specific financial-feature declarations rather than a generic category answer. |
| Gambling, games, contests, illegal activity | Actual business model, permitted countries and licenses. Distinguish ordinary in-game currency from real-money or external-value schemes. |
| UGC | Terms acceptance, moderation/report/block controls, timely action and protection against abusive/illegal content. Test the actual reporting and blocking flows. |
| Health and medical content | Accurate claims, applicable medical-device/health-app declarations, handling of sensitive data and required evidence. Do not claim diagnostic efficacy from unsupported features. |
| Blockchain and tokenized assets | Actual financial/compliance declarations, permitted sale/reward mechanics and truthful product metadata. Do not enable such flags without a real product reason. |
| AI-generated content | Prevent prohibited generated content and provide the required in-app reporting/flagging where the policy applies. Inspect generated-content workflows, not only static store artwork. |
| Impersonation and IP | Authorized developer/brand identity, assets and third-party service access. No competitor icon/title imitation or false official affiliation. |
| User data | Accurate public policy, prominent in-app disclosure/consent where required, secure handling and actual SDK/backend collection/sharing. Reconcile all answers with observed behavior. |
| Account deletion | Where accounts can be created, provide the required in-app and external deletion request paths, describe actual data treatment/retention and test the flow. A support email alone is not proof of compliance. |
| Permissions and sensitive APIs | Core-use justification, scoped permissions, denied states and actual approvals/declarations for sensitive access. Check SMS/call logs, background location, accessibility, broad files/photos, health, VPN, full-screen intents and other actual requested privileges. |
| Device/network abuse and deceptive behavior | No hidden functionality, unauthorized installs/actions, abusive background behavior, fake system UI, misleading billing or attempts to evade review. |
| SDK and target/platform requirements | Audit every embedded SDK, current target API/Billing deadlines, native compatibility and supported form-factor quality. An SDK vendor's claim does not transfer developer responsibility. |
| Payments and subscriptions | Required Play Billing or actual eligible alternative program, truthful paid boundaries, total recurring price/period/trial, cancellation and restored access. No misleading subscription purchase path. |
| Ads | Accurate Contains ads declaration, appropriate content/placement/close behavior and no deceptive/disruptive interaction. Audit launch/navigation/gameplay/focus flows and all ad SDK behavior. |
| Families | Actual target age groups, child-appropriate data/content, eligible ad SDKs and parental/age-related controls. Do not choose an adult-only audience to hide child-directed design. |
| Metadata and promotion | Truthful title/descriptions/art, suitable public content, no ranking/price badges, keyword stuffing, misleading affiliation or unsupported claims in any locale. |
| Ratings, reviews, installs and content rating | Honest rating prompts/acquisition and actual rating questionnaire. Do not buy ratings, fabricate testers or incentivize misleading feedback. |
| News/government/other regulated identities | Actual sourcing, publisher/official affiliation, app-content declarations and applicable licensing. Do not imply an institutional relationship from generic branding. |
| Spam, functionality and UX | Meaningful app-specific utility/content, stable install/load/input/core flow, accessible/readable screens and no dead visible features. Repeated reskins or broken apps cannot be repaired with better listing copy alone. |
| Malware and unwanted software | No harmful code, ad fraud, hostile download behavior, social engineering or unauthorized imitation of system functions. Inspect included dependencies and delivered behavior. |
| Device programs | Apply actual active Wear OS, TV, Auto/Automotive, large-screen/PC and XR requirements only for supported release targets. Do not add discontinued programs because an old policy link still exists. |
| Enforcement and account standing | Current account identity/verification, policy status, deadlines and actual action type. Update rejection, app removal and suspension have different correction/appeal paths. |

## Complete App content and supported declarations

The current App content page separates Needs attention and Actioned tasks. Inspect both relevant outstanding requirements and the saved answers. Tasks can include privacy policy, ads, sign-in details/app access, audience, content rating, Data safety, sensitive permissions, health/financial features and regional requirements. Do not declare a task complete from a locally prepared answer.

For privacy policy, provide a publicly reachable app-specific webpage and in-app access even when claiming no personal-data collection. The current review guidance requires global access without login/geofencing and a normal webpage rather than a PDF/download. Match actual collection/use/sharing/retention/contact information. Keep required deletion URLs distinct from an ordinary marketing site.

For ads, include actual third-party SDK, house/native/banner/interstitial behavior. In-app purchase prompts alone do not automatically constitute an advertising declaration. Use the current rule rather than guessing from a UI label.

For restricted access, configure stable reviewer credentials and precise instructions for every protected feature. Explain actual MFA/OTP/multiple-field or geographic/hardware requirements through the supported sign-in instructions. Do not require personal social accounts, payment or a waitlist to inspect core features. Keep sensitive credentials out of public release records.

Data safety has a supported standalone API: `applications.dataSafety`, using the current official CSV contents in `safetyLabels`. Other ordinary App content tasks are not fields in `Listing` or `AppDetails`. Prepare the complete factual answer and perform the supported console step when no method exists.

### Advertising ID, audience and actual saved state

Read the **final merged release manifest**, not only the app's source manifest. SDK manifests can
contribute `com.google.android.gms.permission.AD_ID`. Inspect actual identifier use and purpose,
including SDK behavior after consent. Contains ads is a separate declaration. A no-ads app can still
use an identifier for analytics. Conversely, a permission string alone does not prove all possible
collection or advertising purposes. Trace the embedded SDK configuration and real data flows.

For Firebase Analytics, inspect the current platform-specific collection/identifier controls rather
than assuming that initial collection disabled means no future collection. If behavior or permission
is changed, rebuild and repeat the factual declaration review. Do not remove a permission solely to
avoid answering a form or declare no data because the SDK was inactive during one launch.

Complete the IARC questionnaire truthfully and retain its generated regional outcomes. Choose target
age groups from the actual product/audience independently of the generated rating. Optional minor-
blocking controls and trader/legal answers require their own applicable facts. Do not reuse another
app's selected answers as a checklist of defaults.

After saving a restricted-access instruction, verify both its child dialog and the parent page saved.
Confirm every relevant task is actioned, then inspect Dashboard prerequisites and Publishing overview.
This links factual policy work to the actual [first-release flow](first-production-release.md).

## Reviewer and release verification

1. Verify the exact AAB/version/signature and install the release-equivalent build on the claimed device families. Check clean install, update from the current production version and actual core flows.
2. Test account access/deletion, allowed/denied permissions, empty/loading/error states, offline/recovery behavior and backend availability. Preserve existing customers' data/entitlements.
3. Exercise products, localized prices, eligibility, pending/cancel/error/restore and actual fulfillment/renewal state. A catalog ACTIVE response does not establish correct client entitlement behavior.
4. Compare every localized claim/image with the actual shipped app. Verify support/privacy/deletion links, target requirements and all required form-factor assets.
5. Inspect pre-review checks/pre-launch reports and address actionable crashes/access/policy failures. A clean automated report does not cover every user workflow.
6. Verify account production-access eligibility, intended track/countries, managed publishing and all independent product/price/declaration mutations.
7. Inspect actual Publishing overview/review messages and submission state. Keep app, update and individual item status separate. Use [the correction/resubmission procedure](edits-review-and-rollout.md) for failures.

For each defect, record requirement/message, reproducible flow, underlying change, replacement artifact/resource and observed retest. Metadata/access-only correction can retain an eligible existing binary. An implementation fix requires a fresh reserved higher version code. A suspended app may need the actual appeal route rather than another ordinary release commit.

Customer reviews are a different surface: `reviews.reply` is a public message and does not answer a policy reviewer. Draft policy responses/appeals with concrete evidence and send only within the user's actual messaging authorization. Do not invent an approval receipt or guarantee review duration.
