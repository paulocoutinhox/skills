# First production release through API and Play Console

Read this when an app record exists but its first production release is still a draft. This sequence
complements edit transactions. API upload, a completed track release, policy submission and public
availability remain different facts. Use current Console labels/permissions and the actual account's
production eligibility. Do not fabricate testers or bypass account gates.

## Establish the intended release before changing forms

Record package, developer/app identity, reserved version code, signed AAB hash, existing tracks,
store listing/locales, catalog, download price, countries and requested endpoint. Reuse the correct
uploaded artifact if available. Do not choose a new build merely to complete missing declarations.
A browser/console change can invalidate an API edit, so finish one transaction before editing in
the console. Read current state again instead of replaying a stale full-track array.

If the API reports `Only releases with status draft may be created on draft app`, preserve the
uploaded artifact and configure the intended track release as `draft`. Validate and commit the edit
with deliberate review-conflict behavior. This records a draft; it does not send the first app for
policy review. Do not work around the error by inventing a status, creating a different package or
moving the requested production build only to internal testing.

## Finish the app's actual dashboard prerequisites

Open the app Dashboard and inspect remaining tasks, then App content's Needs attention and saved
Actioned entries. Use real source/binary/owner facts. Prepare a table before filling the forms:

| Surface | Evidence that determines the answer |
| --- | --- |
| Privacy policy and Data safety | Actual SDK/backend collection, consent, sharing, retention and public app-specific policy |
| App access | Every restricted screen, authentication and a working full-feature reviewer route |
| Ads | Actual advertising behavior/SDKs, independently of whether subscriptions are sold |
| Advertising ID | Final merged manifest plus embedded SDK use and purposes, independently of Contains ads |
| Content rating | Actual bundled/remote content, user interaction, digital purchases and other questionnaire facts |
| Target audience | Product design, intended age groups and policy. A rating result is not an audience selection |
| Government, financial and health declarations | Actual affiliation/features and owner evidence. Do not guess from app name or category |
| Trader/terms and account facts | Existing verified owner status and applicable legal choices |
| Category, contact and listing | Primary user task, actual support contacts, localized copy and required media |
| Pricing/countries | Owner's real initial market and free/paid model, separate from subscription regional prices |

Use official APIs only for the supported declarations, such as the actual Data safety CSV operation.
For console-only forms, use the authenticated visible UI. A save in a child instruction dialog can be
separate from the parent form's Save. Scroll the entire form, inspect required acknowledgments and
confirm the saved result. After two unchanged failed attempts, preserve the error/state and inspect
validation, focus, scroll position and pending requests. Do not attribute an unrelated network error
to the form or replay identical clicks indefinitely.

For a paid app without account login, do not invent reviewer credentials. Provide the app's actual
supported access path if one exists and fully exposes the relevant content. Disclose any developer
content mode clearly. It cannot fake a store purchase, override actual customer info or hide a broken
paid flow. Verify the instructions from a clean reviewer state. If there is no suitable route, identify
that missing access rather than declaring all functionality unrestricted.

IARC ratings are calculated from factual answers. Preserve the returned per-territory ratings,
including a higher local rating caused by a genuine product attribute. Do not change answers merely
to obtain a lower age label. Target audience and optional age-blocking controls are separate decisions.

## Confirm the production draft and send the complete change set

1. Confirm all mandatory setup tasks, not only App content. A missing category/contact selection can
   keep Send for review disabled even when the content declarations are complete.
2. Open Production, inspect Countries/regions and set only the intended availability. Do not infer
   global launch from a multilingual app or automatically copy every subscription pricing region.
3. Open the existing production draft through Edit release. Confirm the exact version code and
   display version, app-signing choice, notes and retained artifacts. Do not upload the same AAB again.
4. Advance to Review and confirm. Expand every error/warning. Fix blocking errors. Distinguish optional
   diagnostic-symbol warnings from an invalid binary. Upload matching native symbols/mappings when
   available, without recompiling or fabricating symbols from a different build.
5. Save the confirmed release. Open Publishing overview and inspect the **whole** pending change
   set. It must include the intended production release and countries, plus required listing and
   declaration changes. Sending only metadata while the binary remains draft is incomplete.
6. Within the user's existing submission/publication scope, use Send changes for review and confirm
   the actual dialog. Record the acknowledged count, build and timestamp. Do not cancel an unrelated
   current review to make this operation succeed.
7. Read the resulting Console state. Automatic quick checks can still run after submission is
   acknowledged. Record them as pending rather than claiming reviewer acceptance or public launch.
   If a check exposes a blocking issue, correct that actual issue through the supported path.

Where managed publishing is unavailable for a first launch, approval can lead to availability under
the selected release flow. Explain that effect before the authorized final transition. Do not promise
that managed publishing will hold the first app or change its release intent without authorization.

## Readback and interruption recovery

A fresh Publisher read context can confirm production `versionCodes` and track release status. If
an edit was created solely for reading, delete that unused edit afterward. A `completed` track release
can coexist with an app still in review. It is not a public-availability receipt. Keep these separate:

| Layer | Record |
| --- | --- |
| Artifact | Package, version code/name, hash, upload result and exact track association |
| API release graph | Track, release status, retained codes and fresh readback |
| Console | Pending, submitted/in review, quick checks, rejected or approved state |
| Distribution | Actual countries, serving version, eligible installation and public storefront |

After an interruption, inspect Publishing overview and the existing draft/release before sending or
uploading again. If submission was acknowledged but quick checks remain pending, monitor the known
change set. Do not interpret a lost local screenshot as a failed submission. Preserve one sanitized
receipt and useful final evidence. Remove temporary GUI drivers, browsing captures and login logs.
No browser cookies, private Console endpoints or invented Publisher declaration fields are needed.
