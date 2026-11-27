# Play Console tasks without an API

Read this when a release needs Play Console forms that the Publisher API does not offer: app
creation, App content declarations, IARC rating, target audience, trader status, category and tags,
app pricing, production countries, Publishing overview submission and app deletion. Data safety has
an API operation, but for an app that collects nothing its CSV contract is easier to get wrong than
the console form.

When the owner has authorized browser use of the Play Console for this task, the agent fills in
these forms itself in the owner's own signed-in browser, and the owner signs in only once.
Without that authorization, every console-only step becomes an exact owner handoff that names the
page, the values to enter and the evidence to send back. Never ask for the password, never store
cookies and never call private Console endpoints.

## Actions that need their own authorization

Browser use covers reading the Console and filling in its forms within the authorized endpoint.
These actions also need the owner's explicit authorization for that exact action in the
current task:

- **Send N changes for review** only within the authorized scope, when the task's authorized endpoint
  includes review submission or production release.
- **Remove changes**, **Unpublish** and **Delete app**, each authorized by name.
- Reading the owner's Gmail or Google Payments history, for example to find the registration
  transaction ID.

Without that authorization, stop before the action and record it as BLOCKED in the release evidence
with the exact console step for the owner, such as "Publishing overview → Send 7 changes for review →
confirm". Do not take a broader instruction to finish the release as permission to unpublish,
delete or read private mail.

## Pricing rules

1. **Read the commercial model before you touch App pricing.** Search the project's plan, release
   brief, store docs and the other store's live price (App Store Connect `appPriceSchedules`)
   for the intended price. If any source says paid, the Play app is paid. Ask when no source
   answers. Never pick Free as a default to clear the dashboard.
2. **Sending a free app for review locks it as free, before it is published.** The console text says
   the choice can change "until publication", but the first **Send changes for review** of a free
   app sets App pricing to "The app is available for free on Google Play and can't be changed to
   paid", even for an app that was never published. Remove changes does not unlock it.
3. **Before Send changes for review, check App pricing again** against the brief, together with
   countries, version code and declarations. Record it in the release evidence.
4. The only way back is deleting the app, with the owner's authorization for deletion, and creating
   it again (below). The package name of a deleted app stays taken until the deletion becomes
   permanent seven days later. Then it is freed for reuse only when the app had zero installs
   ever. Otherwise a new package name is required.

## Prepare the evidence table first

Collect every answer before you open the forms, from the binary and the owner's documents:

| Form | Evidence |
| --- | --- |
| Privacy policy | Public URL for this app that returns 200 |
| App access | Whether any feature needs login, payment, codes or another device |
| Ads | Ad SDKs and ad code in the final build |
| Advertising ID | `com.google.android.gms.permission.AD_ID` in the final merged manifest and SDK use |
| Content rating | Violence, fear, sexuality, gambling, language, drugs, crude humor, real-money purchases, user interaction, location sharing, prohibited symbols, terrorism, crime techniques |
| Target audience | Intended age groups. Groups under 13 add Families policy duties |
| Data safety | Everything the app, SDKs, backend and web views send off the device |
| Government, financial, health | Real affiliation and features |
| Trader status | The account-level trader declaration and a public terms URL |
| Category, tags, contacts | App or Game and the category from the brief (for a game, its main mechanic), up to five honest tags, support email and website |
| Pricing | Free or paid from the brief, payments profile and price |
| Countries | Intended markets |

Before you answer Ads, Advertising ID and Data safety, inspect the merged manifest at
`app/build/intermediates/merged_manifests/release/processReleaseManifest/AndroidManifest.xml` (with
the real module and variant names, or the AAB manifest) for permissions, services and SDK
components.

## Open a browser that Google allows to sign in

Google rejects sign-in in a browser launched by an automation framework ("This browser or app may
not be secure"), because Playwright and similar tools add flags such as `--no-sandbox` and
`--enable-automation`. Start the installed Chrome normally with only a remote-debugging port and a
separate profile directory, then attach to it over the Chrome DevTools Protocol. Chrome refuses
remote debugging on the default profile, so the separate `--user-data-dir` is required.

macOS:

```sh
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --user-data-dir="$TMPDIR/play-console-profile" --remote-debugging-port=9333 --no-first-run --no-default-browser-check "https://play.google.com/console/"
```

Windows (PowerShell):

```powershell
& "$env:ProgramFiles\Google\Chrome\Application\chrome.exe" --user-data-dir="$env:TEMP\play-console-profile" --remote-debugging-port=9333 --no-first-run --no-default-browser-check "https://play.google.com/console/"
```

Linux:

```sh
google-chrome --user-data-dir="${TMPDIR:-/tmp}/play-console-profile" --remote-debugging-port=9333 --no-first-run --no-default-browser-check "https://play.google.com/console/"
```

Check `http://127.0.0.1:9333/json/version` and ask the owner to sign in once in that window. Then
wait for a page whose URL matches `https://play.google.com/console/u/0/developers/<developer id>/` by
polling `http://127.0.0.1:9333/json`, instead of asking the owner to report back. Attach with
Playwright `chromium.connect_over_cdp('http://127.0.0.1:9333')` and pick the page whose URL contains
`play.google.com`. Do not close the browser when the script ends. Delete the profile directory when
the work is done.

## Talking to the tabs

Every tab of that Chrome is a DevTools target. `curl -s http://127.0.0.1:9333/json` lists them with
`type`, `title` and `url`. Internal targets such as `chrome://omnibox-popup` also show up, so never
take "the last page". Pick the tab by URL every time a script attaches.

Attach, act and detach in short scripts. Each script connects, finds its tab, does a few steps,
prints what it sees and exits without closing the browser. The owner can watch the window, and a
failed step leaves the page exactly where it stopped so you can inspect it.

```python
import asyncio

from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:9333")
        context = browser.contexts[0]
        console = [page for page in context.pages if "play.google.com/console" in page.url][0]
        await console.goto("https://play.google.com/console/u/0/developers/DEVELOPER_ID/app/APP_ID/app-dashboard", wait_until="domcontentloaded")
        await console.wait_for_timeout(4000)
        print(await console.evaluate("document.title"))
        print(await console.inner_text("body"))


asyncio.run(main())
```

Run each script with uv. Attaching over CDP uses the installed Chrome, so you do not need to download
a Playwright browser:

```sh
uv run --with playwright python console-step.py
```

- Keep one tab for the Console. Open a second tab with `context.new_page()` for an authorized side
  lookup, such as the Gmail search for the registration receipt, and find it again later by its URL.
  A dialog left open in the Console tab stays open while you use another tab.
- Open Gmail or Google Payments only with the owner's explicit authorization to read them in this
  task. Otherwise record the lookup as a BLOCKED owner handoff that names the receipt to find.
- Gmail search works through the URL:
  `https://mail.google.com/mail/u/0/#search/%22Developer+Registration+Fee%22`. Result rows are
  `tr.zA`. Clicking the first row opens the message, whose text is in `div[role=main]`.
- Google Payments draws its content inside iframes. Read `page.frames` and each frame's
  `body.innerText`, not only the top document.
- Read only what the task needs from the owner's mail and payments history, and never repeat other
  personal entries in reports.
- Page and app IDs come from the URL after navigation, for example
  `/developers/<developer id>/app/<app id>/`. Read them from the app list links
  (`a[href*="/app/"]`) and confirm the app by `document.title` before you change anything.

## Driving the Console reliably

The Console is an Angular Material application. These behaviors decide whether a click works:

- After every action, read the page as text (`document.body.innerText`) and list the visible buttons
  with their disabled state. Take a screenshot when the text does not explain the state.
- Wizards keep earlier steps in the DOM, hidden. Click only visible elements (Playwright
  `locator('visible=true')`), or you will pick "No" in a hidden step.
- `material-radio` and `material-checkbox` hosts often do not toggle when clicked. Click the visible
  label text, or the row's `mat-checkbox`, then check the real `input.checked` values.
- Dropdowns are `dropdown-button` elements. Open the one whose text is its current value, then choose
  the visible `role=option` by exact name.
- A dialog has its own Save. The page Save behind it is a different button. After saving, reload
  the page and read the value back.
- A disabled Next usually means the section needs Save first (the IARC questionnaire turns on Next
  only after Save).
- Check the "change was saved" confirmation for every form before you move on.

## Form procedures

Start each task from the app Dashboard, under "Set up your app".

1. **Privacy policy**: fill in the URL field and Save.
2. **App access**: choose that no part is restricted only when every feature works without login,
   payment, codes or another device. Otherwise give real reviewer instructions.
3. **Ads**: answer from the binary.
4. **Content rating**: enter the contact email, pick the IARC category that matches the app type in
   the brief (for example Game for a game), accept the IARC terms, Next. Sections appear one at a
   time after each answer. Answer each question from the evidence table and log the question text.
   Save, then Next to the summary, review the per-territory ratings, Save.
5. **Target audience**: tick the age groups. With only 13+ groups, the wizard can jump straight to
   the summary. Save there.
6. **Data safety**: Next through the overview, answer whether any required data type is collected or
   shared, follow the remaining steps, review the store preview and Save.
7. **Government apps, financial features, health**: choose the matching answer, for example "My app
   doesn't offer financial features" and "My app has no health features", go through the documentation
   or regional step and Save.
8. **Trader status**: when the account is already a trader, confirm that the status applies to the app
   and add the terms URL. Save.
9. **Category and contact details** (Store settings): Edit the category, pick App or Game and the
   category from the brief, and Save the dialog. Use Manage tags to tick at most five honest tags and
   Apply. Check the contact email and website.
10. **App pricing**: apply pricing rules 1 and 3. For a paid app, choose Paid, set the price and review
    the generated local prices before Save. A payments profile is required.
11. **Advertising ID**: this declaration is not in the dashboard list. The Publishing overview quick
    checks block the submission until it is filled in ("Advertising ID declaration incomplete"). Answer
    from the merged manifest.

## Release, countries and submission

1. Upload the AAB and set the production release through the Publisher API (edit, upload, track
   update, validate, commit). In zsh, write `"$BASE/edits/${EDIT}:commit"` with braces, because
   zsh reads `$EDIT:c` as a history modifier and the request goes to the wrong URL.
2. Production → Countries/regions: the Edit button stays disabled until rows are selected. Tick the
   header checkbox "Select all rows" (or the intended countries) and Save.
3. Production → Releases → Edit release → Next. Expand every warning. A missing native debug symbol
   file is a warning, not a blocker. Save.
4. Publishing overview: read the whole change set. Check App pricing again (pricing rule 3). Within the
   authorized scope, click "Send N changes for review" and confirm the dialog. Otherwise stop and
   record that click as the BLOCKED owner step.
5. Quick checks then run for up to about 15 minutes and can still block the submission. Come back and
   read the result, fix any finding (such as the Advertising ID declaration) and send again.

## Deleting an app to start over

Remove changes, Unpublish and Delete app each need the owner's explicit authorization for that exact
action in the current task. Without it, record each one as a BLOCKED owner step with the console
path below and stop.

Only the account owner can delete an app. The app must be unpublished, with no changes in review,
fewer than 1000 active devices, and not rejected, blocked or suspended. A monetized app qualifies
only with zero installs ever.

1. Publishing overview → Remove changes, and confirm the dialog.
2. Advanced settings → App availability → Unpublished → Unpublish, and confirm.
3. The Delete app section then appears on the same tab. It asks for the developer account's
   registration transaction ID and the package name, then for the word `delete`.
4. The transaction ID is the Google order number of the "Developer Registration Fee" receipt
   (sender `payments-noreply@google.com`), for example `PDS.1234-5678-9012-34567`. With the owner's
   authorization to read them, search the owner's Gmail for "Developer Registration Fee" in the same
   signed-in browser, or Google Payments → Activity. Otherwise ask the owner for the order number.
5. After confirmation, App availability shows "You have until <date> to recover this deleted app",
   seven days later. Until that date you can restore the app from the same page, and its package
   name is still "already in use" in Create app, which asks for the package name and has a
   check-availability button.
6. After that date the deletion is permanent. An app with zero installs ever frees its package
   name for anyone to reuse, so create the new app on that day before anyone else can claim it. If
   the app ever had any installs, the package name can never be reused, even by the same account.
7. Let the owner choose: wait for the date and keep the package name, or publish earlier with a
   new package name. Record the date in the project's release docs so the work starts again on time.

## Create the app

Home → Create app: app name (at most 30 characters, matching the listing), package name with a
check-availability button, default language, App or Game, **Free or Paid from the brief**, Developer
Program Policies and US export law declarations. Then give the service account access to the new
app under Users and permissions before you use the Publisher API, and repeat every form above.
