# First project and first iOS/Android apps

Read this when the product is not in RevenueCat yet, or when only some of its platform connections
exist. The workflow below targets the official CLI **0.1.8**. Examples use made-up identifiers.
They are separate native commands, not a script to run again over an existing project.

## 1. Establish what is missing

Tell these resources apart before you create anything:

| Resource | Where it exists | Completion evidence |
| --- | --- | --- |
| RevenueCat account | RevenueCat identity and organization | Signed-in owner or collaborator and real access |
| Project | The RevenueCat boundary for customers and catalog | Returned project ID and project read-back |
| iOS app connection | RevenueCat `app_store` app | Returned app ID, matching bundle ID, public SDK key |
| Android app connection | RevenueCat `play_store` app | A different app ID, matching package name, public SDK key |
| Store app records | App Store Connect and Play Console | Real store IDs and matching binary identities |
| Store products | Apple subscriptions and Google subscriptions/base plans | Real IDs, periods, prices, availability and review or activation state |

Creating a RevenueCat app connection does not create the binary or publish a store listing. A missing
RevenueCat project does not mean the owner needs a new account. For an existing account, sign in and
create only the missing project and apps. If the account itself is missing, use the supported signup
flow with the owner's real identity and the required checks. Report account enrollment separately.

Record the real bundle and package identities from the native project settings, the paid benefit, the
monthly and annual business choices, locales, the identity and restore policy and the requested
endpoint. If store products already exist, keep their identifiers, prices, regions and subscribers.
If store records or products are missing, finish the supported store workflow that applies before you
claim real purchases are ready.

## 2. Authenticate, inspect and create the project

Check the official executable first. The checked version also runs as
`npx --yes @revenuecat/cli@0.1.8 <command>`. This pins a researched example, not a permanent latest
version.

```text
rc version
rc commands --json
rc schema projects create
rc schema apps create
rc auth status
rc auth login
rc projects list --json --no-input
```

Run `auth login` only when there is no session or the existing one does not fit. Use the supported
browser OAuth flow or the approved secret store. Select the intended owner and organization and check
the access granted. Do not read credential-profile contents, copy OAuth callback codes into reports or
create a server key you do not need just to set up a client. Some OAuth scopes can need a grant from
the owner after a new project is created. Sign in again only for the project you need, and only if a
real scope error requires it.

Check all candidate projects and apps you can reach. A matching project name does not prove identity.
When it is really missing, create it once:

```text
rc projects create --name "Example App" --json --no-input
rc projects use "$RC_PROJECT_ID" --json --no-input
rc apps list --project-id "$RC_PROJECT_ID" --json --no-input
```

Set `RC_PROJECT_ID` to the real returned project ID before the second command. Use the explicit
`--project-id` on later configuration commands. Read the command's output before you pull out IDs:
in 0.1.8 normal JSON commands wrap the result under `data`, while `rc api` returns the API JSON
body directly. Do not apply `.data.id` to both. Check the returned object's identity and type.

Before retrying a create that timed out, list the resources and check what exists. A missing local
receipt does not prove the remote create failed. Check app matches across projects you can reach
where it makes sense:
`rc apps list --all-projects --bundle-id com.example.app --json --no-input`, and the matching
`--package-name` filter. An empty result limited by permissions does not prove the app exists nowhere.

## 3. Create the two platform connections and obtain public keys

Create only the missing connection in the selected project:

```text
rc apps create --project-id "$RC_PROJECT_ID" --name "Example iOS" --type app_store --bundle-id com.example.app --json --no-input
rc apps create --project-id "$RC_PROJECT_ID" --name "Example Android" --type play_store --package-name com.example.app --json --no-input
rc apps show "$IOS_APP_ID" --project-id "$RC_PROJECT_ID" --json --no-input
rc apps show "$ANDROID_APP_ID" --project-id "$RC_PROJECT_ID" --json --no-input
rc apps keys "$IOS_APP_ID" --project-id "$RC_PROJECT_ID" --json --no-input
rc apps keys "$ANDROID_APP_ID" --project-id "$RC_PROJECT_ID" --json --no-input
```

Set `IOS_APP_ID` and `ANDROID_APP_ID` from their own create responses. These are RevenueCat
resource IDs, not `com.example.app` and not the stores' numeric app IDs. Public platform SDK keys are
created with each app. Fetch them instead of making up `appl_`/`goog_` values or creating secret keys.
Read the returned key type and which app it belongs to. Store only the matching public key in each
client.

## 4. Connect the original store credentials

First find out whether credentials are already set up and usable for the intended app and team.
If the owner gave existing Apple `.p8` files and Google service-account JSON, use the documented
app-update API and read them from their original paths. Do not run key-creation assistants again or
rotate keys just because the RevenueCat app is new. See the exact payloads and transport in
[existing-credential connection](api-cli-and-setup.md#connect-existing-store-credentials).

Record the three separate configured flags: Apple subscription key, Apple App Store Connect API
key and Google service-account credential. Configured flags show what is stored. They do not prove
that every store permission, product state or transaction works. Complete the real supported checks,
server-notification setup and SDK product requests. Keep a clear untested or blocked state when those
checks need the owner.

If credentials do not exist, use the real setup flow that needs a person for the installed CLI.
Version 0.1.8's Apple flow takes a RevenueCat app ID. Its Google flow takes an optional RevenueCat
Play app ID with Cloud project, developer and package flags, uploads the new key itself or writes it
out for a separate upload, and removes older service-account keys unless told to keep them. See
[the setup assistant details](api-cli-and-setup.md#when-keys-must-be-created-instead). Do not guess
arguments from another version.

## 5. Match four products to one access benefit

For a concrete two-plan design, suppose the stores already have these products approved by the owner:

| Platform | Store product | Base plan | RevenueCat `store_identifier` | Logical package |
| --- | --- | --- | --- | --- |
| Apple | `com.example.plus.monthly` | Not applicable | `com.example.plus.monthly` | `$rc_monthly` |
| Apple | `com.example.plus.annual` | Not applicable | `com.example.plus.annual` | `$rc_annual` |
| Google | `com.example.plus.monthly` | `monthly` | `com.example.plus.monthly:monthly` | `$rc_monthly` |
| Google | `com.example.plus.annual` | `annual` | `com.example.plus.annual:annual` | `$rc_annual` |

The Google rows are an example of the subscription and base-plan mapping used in this setup. Read
the real store and RevenueCat model, keep the exact case and use existing IDs. An ID with a colon is
not a new Play subscription SKU. Check the base-plan periods and active status. Apple subscription
review and regional availability are separate. Do not assume a product is active because it has a
RevenueCat product row.

Check existing products first. For each missing RevenueCat catalog record, use the matching app and
the exact store identifier. The native command creates a RevenueCat record, not an Apple or Google
product:

```text
rc products list --project-id "$RC_PROJECT_ID" --json --no-input
rc products create --project-id "$RC_PROJECT_ID" --app-id "$IOS_APP_ID" --store-id com.example.plus.monthly --type subscription --display-name "Plus Monthly" --json --no-input
rc products create --project-id "$RC_PROJECT_ID" --app-id "$IOS_APP_ID" --store-id com.example.plus.annual --type subscription --display-name "Plus Annual" --json --no-input
rc products create --project-id "$RC_PROJECT_ID" --app-id "$ANDROID_APP_ID" --store-id com.example.plus.monthly:monthly --type subscription --display-name "Plus Monthly" --json --no-input
rc products create --project-id "$RC_PROJECT_ID" --app-id "$ANDROID_APP_ID" --store-id com.example.plus.annual:annual --type subscription --display-name "Plus Annual" --json --no-input
rc entitlements create --project-id "$RC_PROJECT_ID" --lookup-key plus --display-name "Plus" --json --no-input
rc entitlements attach "$ENTITLEMENT_ID" "$IOS_MONTHLY_ID" "$IOS_ANNUAL_ID" "$ANDROID_MONTHLY_ID" "$ANDROID_ANNUAL_ID" --project-id "$RC_PROJECT_ID" --json --no-input
```

Set all product and entitlement resource IDs from the real responses. Reuse `plus` if it already
exists. The app checks the stable entitlement lookup key `plus`, not the internal `entl...` ID or
the offering name. All four products grant the same benefit. Never create four separate access
rules just to cover two stores and two billing periods.

If the products are not in the stores, use supported store APIs or allowed RevenueCat connected-store
creation or plans, with the owner's real business choices. Read both sides back after a partial
failure. Do not guess an import command or confuse creating a catalog record with creating a store
product.

## 6. Create the offering and cross-store packages

Check existing offerings and packages first. For a new setup:

```text
rc offerings create --project-id "$RC_PROJECT_ID" --lookup-key default --display-name "Default" --json --no-input
rc packages create "$OFFERING_ID" --project-id "$RC_PROJECT_ID" --lookup-key '$rc_monthly' --display-name "Monthly" --json --no-input
rc packages create "$OFFERING_ID" --project-id "$RC_PROJECT_ID" --lookup-key '$rc_annual' --display-name "Annual" --json --no-input
rc packages attach "$MONTHLY_PACKAGE_ID" "$IOS_MONTHLY_ID" "$ANDROID_MONTHLY_ID" --project-id "$RC_PROJECT_ID" --json --no-input
rc packages attach "$ANNUAL_PACKAGE_ID" "$IOS_ANNUAL_ID" "$ANDROID_ANNUAL_ID" --project-id "$RC_PROJECT_ID" --json --no-input
rc offerings verify "$OFFERING_ID" --project-id "$RC_PROJECT_ID" --json --no-input
```

Put `$rc_monthly` and `$rc_annual` in single quotes so the shell does not treat them as variables.
Fill in the returned offering and package IDs before the commands that depend on them. A monthly
package links the iOS and Android monthly products, not both lengths from one store. Check
eligibility and every reported issue before making the offering current.

## 7. Integrate, design and publish at the intended stage

Replace client placeholders with the platform public keys and configure the real SDK once. Keep the
stable entitlement key in line with the code. Rebuild, reinstall and restart after the last source
change. A downloaded paywall cannot fix a binary that still has placeholder keys built in.

Follow the [worked paywall lifecycle](paywalls-and-marketing.md#worked-cli-lifecycle) for uploaded brand
fonts and images, short generation prompts, edits for each locale, preview checks and native checks.
Keep publishing within the existing task permission and the CLI's design-review requirement. A
CLI preview can contain sample prices and does not prove store-backed prices or purchases.

When you are allowed to select this offering for customers, make that change on purpose and read the
result the SDK sees separately for each platform:

```text
rc offerings set-current "$OFFERING_ID" --project-id "$RC_PROJECT_ID" --yes --json --no-input
rc offerings preview "$IOS_APP_ID" --project-id "$RC_PROJECT_ID" --app-user-id setup-validation --json --no-input
rc offerings preview "$ANDROID_APP_ID" --project-id "$RC_PROJECT_ID" --app-user-id setup-validation --json --no-input
```

Use a harmless test identity made for this, not a real customer's ID. Confirm the intended current
offering, the two correct platform products and the published `paywall_components`. A null components
value can mean a fallback screen instead of the published design. Treat preview access as a
configuration check, not a customer purchase or an entitlement grant.

## 8. Check in the real app and report the exact state

Open the integrated native paywall and check the prices and periods from the store, all locales,
scrolling, close, purchase, restore, Terms and Privacy controls. Keep premium access closed for
inactive and error states. A restore button you can reach does not prove a past transaction was
restored.

Run real sandbox or test-track purchases and restores with suitable store accounts when available.
A separate Android emulator without an eligible Play account may fail billing even when the catalog
is linked. Look at the account, install source, track eligibility, product state, credentials and SDK
error together. Do not guess the cause from a numeric code alone or grant a fake entitlement.

Finish with a cleaned mapping of the project, two apps, four products, entitlement, offering,
packages, paywall, credential flags and original credential references without file contents.
Record SDK and build versions, the real prices you saw, notification and webhook status, test
evidence and store review still left. Keep configuration checks, native UI checks, transaction checks
and public launch separate. Continue a partly done setup from these returned resource IDs instead of
deleting and recreating everything. See [operations](testing-and-operations.md) for lifecycle
coverage.
