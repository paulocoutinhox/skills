# First production release through API and Play Console

Read this when an app record exists but its first production release is still a draft. This sequence
works alongside edit transactions. An API upload, a completed track release, a policy submission and
public availability are still different facts. Use the current Console labels and permissions and the
real account's production eligibility. Do not make up testers or get around account gates.

## Establish the intended release before changing forms

Record the package, developer and app identity, reserved version code, signed AAB hash, existing tracks,
store listing and locales, catalog, download price, countries and requested endpoint. Reuse the right
uploaded artifact if there is one. Do not pick a new build only to fill in missing declarations.
A change in the browser or console can make an API edit out of date, so finish one transaction before
you edit in the console. Read the current state again instead of replaying an outdated full-track array.

If the API reports `Only releases with status draft may be created on draft app`, keep the
uploaded artifact and set the intended track release to `draft`. Validate and commit the edit
with a review-conflict behavior you chose on purpose. This records a draft. It does not send the first
app for policy review. Do not get around the error by inventing a status, creating a different package
or moving the requested production build to internal testing only.

## Finish the app's actual dashboard prerequisites

Open the app Dashboard and look at the remaining tasks, then App content's Needs attention and saved
Actioned entries. Use real facts from the source, binary and owner. Prepare a table before you fill in
the forms:

| Surface | Evidence that determines the answer |
| --- | --- |
| Privacy policy and Data safety | Real SDK and backend collection, consent, sharing, retention and a public policy for this app |
| App access | Every restricted screen, authentication and a working reviewer route to all features |
| Ads | Real advertising behavior and SDKs, whether or not subscriptions are sold |
| Advertising ID | Final merged manifest plus embedded SDK use and purposes, separate from Contains ads |
| Content rating | Real bundled and remote content, user interaction, digital purchases and other questionnaire facts |
| Target audience | Product design, intended age groups and policy. A rating result is not an audience choice |
| Government, financial and health declarations | Real affiliation and features and owner evidence. Do not guess from the app name or category |
| Trader/terms and account facts | The owner's existing verified status and the legal choices that apply |
| Category, contact and listing | Main user task, real support contacts, localized copy and required media |
| Pricing/countries | The owner's real first market and free or paid model, separate from subscription regional prices |

Use official APIs only for the declarations they support, such as the real Data safety CSV operation.
For console-only forms, use the signed-in visible UI through [the Console browser procedure](play-console-browser.md). A save in a child instruction dialog can be
separate from the parent form's Save. Scroll through the whole form, check the required
acknowledgments and confirm the saved result. After two failed attempts with no change, keep the error
and state, and check validation, focus, scroll position and pending requests. Do not blame an
unrelated network error on the form, or repeat the same clicks forever.

For a paid app without account login, do not make up reviewer credentials. Give the app's real
supported access path if one exists and it fully shows the relevant content. Clearly disclose any
developer content mode. It cannot fake a store purchase, override real customer info or hide a broken
paid flow. Check the instructions from a clean reviewer state. If there is no suitable route, name the
missing access instead of saying all features are unrestricted.

IARC ratings are worked out from factual answers. Keep the per-territory ratings that come back,
including a higher local rating caused by a real product feature. Do not change answers just to
get a lower age label. Target audience and optional age-blocking controls are separate decisions.

## Confirm the production draft and send the complete change set

1. Confirm all required setup tasks, not only App content. A missing category or contact choice can
   keep Send for review disabled even when the content declarations are complete.
2. Open Production, check Countries/regions and set only the intended availability. Do not assume
   a global launch because the app has many languages, and do not copy every subscription pricing
   region automatically.
3. Open the existing production draft through Edit release. Confirm the exact version code and
   display version, app-signing choice, notes and retained artifacts. Do not upload the same AAB again.
4. Go on to Review and confirm. Expand every error and warning. Fix blocking errors. Tell optional
   diagnostic-symbol warnings apart from an invalid binary. Upload matching native symbols or mappings
   when you have them, without rebuilding or making up symbols from a different build.
5. Save the confirmed release. Open App pricing and check the free or paid model against the brief,
   because the submission locks a free app as free. Open Publishing overview and look at the **whole** pending change
   set. It must include the intended production release and countries, plus the required listing and
   declaration changes. Sending only metadata while the binary is still a draft is incomplete.
6. Within the user's existing submission and publishing scope, use Send changes for review and confirm
   the real dialog. Record the acknowledged count, build and time. Do not cancel an unrelated
   current review to make this operation succeed.
7. Read the Console state that results. Automatic quick checks can still run after the submission is
   acknowledged. Record them as pending instead of claiming reviewer acceptance or a public launch.
   If a check finds a blocking issue, fix that real issue through the supported path. The
   Advertising ID declaration is not listed among the dashboard tasks, but it blocks the quick checks
   until you fill it in from the merged manifest.

Where managed publishing is not available for a first launch, approval can lead to availability under
the chosen release flow. Explain that effect before the final authorized step. Do not promise
that managed publishing will hold the first app, or change its release intent, without authorization.

## Readback and interruption recovery

A fresh Publisher read context can confirm the production `versionCodes` and track release status. If
you created an edit only for reading, delete that unused edit afterward. A `completed` track release
can exist while the app is still in review. It is not proof of public availability. Keep these apart:

| Layer | Record |
| --- | --- |
| Artifact | Package, version code/name, hash, upload result and exact track association |
| API release graph | Track, release status, retained codes and fresh readback |
| Console | Pending, submitted/in review, quick checks, rejected or approved state |
| Distribution | Real countries, serving version, eligible installation and public store page |

After an interruption, check Publishing overview and the existing draft or release before you send or
upload again. If the submission was acknowledged but quick checks are still pending, keep watching the
known change set. Do not read a lost local screenshot as a failed submission. Keep one cleaned
receipt and the useful final evidence. Remove temporary GUI drivers, browsing captures and login logs.
You need no browser cookies, private Console endpoints or made-up Publisher declaration fields.
