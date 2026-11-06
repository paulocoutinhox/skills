# First project and first iOS/Android apps

Read this when the product is absent from RevenueCat or only some of its platform connections exist.
The workflow below was exercised with the official CLI **0.1.7**. Examples use fictitious identifiers.
They are individual native commands, not a script to replay over an existing project.

## 1. Establish what is missing

Distinguish these resources before creating anything:

| Resource | Where it exists | Completion evidence |
| --- | --- | --- |
| RevenueCat account | RevenueCat identity and organization | Authenticated owner/collaborator and actual access |
| Project | RevenueCat customer/catalog boundary | Returned project ID and project readback |
| iOS app connection | RevenueCat `app_store` app | Returned app ID, matching bundle ID, public SDK key |
| Android app connection | RevenueCat `play_store` app | Different app ID, matching package name, public SDK key |
| Store app records | App Store Connect and Play Console | Actual store IDs and matching binary identities |
| Store products | Apple subscriptions and Google subscriptions/base plans | Actual IDs, periods, prices, availability and review/activation state |

Creating a RevenueCat app connection does not create the binary or publish a store listing. A missing
RevenueCat project does not imply the owner needs a new account. For an existing account, authenticate
and create only the missing project/apps. If the account itself is missing, use the supported signup
flow with the owner's real identity and required verification. Report account enrollment separately.

Record the real bundle/package identities from native project configuration, paid benefit, monthly/
annual commercial choices, locales, identity/restore policy and requested endpoint. If store products
already exist, preserve their identifiers, prices, regions and subscribers. If store records or products
are missing, complete the applicable supported store workflow before claiming real purchase readiness.

## 2. Authenticate, inspect and create the project

Verify the official executable first. The inspected version also runs as
`npx --yes @revenuecat/cli@0.1.7 <command>`. This pins a researched example, not a permanent latest version.

```text
rc version
rc commands --json
rc schema projects create
rc schema apps create
rc auth status
rc auth login
rc projects list --json --no-input
```

Run `auth login` only when the existing session is absent or unsuitable. Use the supported browser OAuth
flow or approved secret mechanism. Select the intended owner/organization and inspect granted access.
Do not read credential-profile contents, copy OAuth callback codes into reports or create an unnecessary
server key merely to configure a client. Some OAuth scopes can require an owner-controlled grant after
creating a new project. Reauthorize only the needed project if a real scope error requires it.

Inspect all accessible candidate projects and apps. A project name match is not identity proof. When
it is genuinely absent, create it once:

```text
rc projects create --name "Example App" --json --no-input
rc projects use "$RC_PROJECT_ID" --json --no-input
rc apps list --project-id "$RC_PROJECT_ID" --json --no-input
```

Set `RC_PROJECT_ID` to the actual returned project ID before the second command. Use the explicit
`--project-id` on subsequent configuration commands. Read the command's output before extracting IDs:
in 0.1.7 ordinary JSON commands wrap the result under `data`, while `rc api` returns the API JSON
body directly. Do not apply `.data.id` to both. Verify the returned object's identity and type.

Before retrying a timed-out create, list and reconcile the resources. A missing local receipt is not
proof that the remote create failed. Check accessible cross-project app matches where appropriate:
`rc apps list --all-projects --bundle-id com.example.app --json --no-input`, and the corresponding
`--package-name` filter. A permission-limited empty result is not proof of global absence.

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

Assign `IOS_APP_ID` and `ANDROID_APP_ID` from their respective create responses. These are RevenueCat
resource IDs, not `com.example.app` and not the stores' numeric app IDs. Public platform SDK keys are
created with each app. Retrieve them instead of inventing `appl_`/`goog_` values or creating secret keys.
Read the returned key type and app association. Store only the matching public key in each client.

## 4. Connect the original store credentials

First determine whether credentials are already configured and usable for the intended app/team.
If the owner supplied existing Apple `.p8` files and Google service-account JSON, use the documented
app-update API and read their original paths. Do not rerun key-creation assistants or rotate keys just
because the RevenueCat app is new. See the exact payloads and transport in
[existing-credential connection](api-cli-and-setup.md#connect-existing-store-credentials).

Record the three independent configured flags: Apple subscription key, Apple App Store Connect API
key and Google service-account credential. Configured flags show stored configuration. They do not
prove every store permission, product state or transaction works. Complete actual supported checks,
server-notification setup and SDK product requests. Preserve an explicit untested/blocked state when
those checks need owner participation.

If credentials do not exist, use the actual human-required setup flow for the installed CLI. Version
0.1.7's Apple flow accepts a RevenueCat app ID. Its Google flow uses Cloud project/developer/package
flags and produces credentials for a separate upload. Do not infer arguments from another version.

## 5. Reconcile four products and one access benefit

For a concrete two-plan design, suppose the stores already contain these owner-approved products:

| Platform | Store product | Base plan | RevenueCat `store_identifier` | Logical package |
| --- | --- | --- | --- | --- |
| Apple | `com.example.plus.monthly` | Not applicable | `com.example.plus.monthly` | `$rc_monthly` |
| Apple | `com.example.plus.annual` | Not applicable | `com.example.plus.annual` | `$rc_annual` |
| Google | `com.example.plus.monthly` | `monthly` | `com.example.plus.monthly:monthly` | `$rc_monthly` |
| Google | `com.example.plus.annual` | `annual` | `com.example.plus.annual:annual` | `$rc_annual` |

The Google entries are an example of the subscription/base-plan mapping used in this setup. Read the
actual store and RevenueCat model, preserve exact case and use existing IDs. A colon-qualified ID is
not a new Play subscription SKU. Check the base-plan periods and active status. Apple subscription
review and regional availability are separate. Do not infer activation from a RevenueCat product row.

Inspect existing products first. For each missing RevenueCat catalog record, use the corresponding
app and exact store identifier. The native command creates a RevenueCat record, not an Apple/Google
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

Assign all product and entitlement resource IDs from the actual responses. Reuse `plus` if it already
exists. The runtime checks the stable entitlement lookup key `plus`, not the internal `entl...` ID or
the offering name. All four products grant that same benefit. Never create four independent access
rules just to represent two stores and two billing periods.

If products are absent from the stores, use supported store APIs or authorized RevenueCat connected-
store creation/plans, with the owner's real commercial choices. Read both sides back after partial
failures. Do not guess an import command or mistake catalog creation for store creation.

## 6. Create the offering and cross-store packages

Inspect existing offerings/packages first. For a new graph:

```text
rc offerings create --project-id "$RC_PROJECT_ID" --lookup-key default --display-name "Default" --json --no-input
rc packages create "$OFFERING_ID" --project-id "$RC_PROJECT_ID" --lookup-key '$rc_monthly' --display-name "Monthly" --json --no-input
rc packages create "$OFFERING_ID" --project-id "$RC_PROJECT_ID" --lookup-key '$rc_annual' --display-name "Annual" --json --no-input
rc packages attach "$MONTHLY_PACKAGE_ID" "$IOS_MONTHLY_ID" "$ANDROID_MONTHLY_ID" --project-id "$RC_PROJECT_ID" --json --no-input
rc packages attach "$ANNUAL_PACKAGE_ID" "$IOS_ANNUAL_ID" "$ANDROID_ANNUAL_ID" --project-id "$RC_PROJECT_ID" --json --no-input
rc offerings verify "$OFFERING_ID" --project-id "$RC_PROJECT_ID" --json --no-input
```

Single-quote `$rc_monthly` and `$rc_annual` so the shell does not expand them as variables. Populate the
returned offering/package IDs before the dependent commands. A monthly package links the iOS and
Android monthly products, not both durations from one store. Inspect eligibility and every reported
issue before making the offering current.

## 7. Integrate, design and publish at the intended stage

Replace client placeholders with the platform public keys and configure the real SDK once. Keep the
stable entitlement key aligned with code. Rebuild, reinstall and restart after the final source change.
A downloaded paywall cannot repair a binary that still embeds placeholder keys.

Follow the [worked paywall lifecycle](paywalls-and-marketing.md#worked-cli-lifecycle) for uploaded brand
fonts/images, concise generation prompts, locale-specific edits, preview inspection and native checks.
Keep publication within the existing task authorization and the CLI's design-review requirement. A
CLI preview can contain illustrative prices and does not prove store-backed prices or purchases.

When selecting this offering for customers is authorized, make that explicit transition and read the
SDK-facing result separately for each platform:

```text
rc offerings set-current "$OFFERING_ID" --project-id "$RC_PROJECT_ID" --yes --json --no-input
rc offerings preview "$IOS_APP_ID" --project-id "$RC_PROJECT_ID" --app-user-id setup-validation --json --no-input
rc offerings preview "$ANDROID_APP_ID" --project-id "$RC_PROJECT_ID" --app-user-id setup-validation --json --no-input
```

Use a harmless dedicated test identity rather than a real customer's ID. Confirm the intended current
offering, the two correct platform products and published `paywall_components`. A null components
value can mean a fallback presentation rather than the published design. Treat preview access as a
configuration check, not a customer purchase or entitlement grant.

## 8. Verify in the actual app and deliver exact state

Open the integrated native paywall and inspect store-returned prices/periods, all locales, scrolling,
close, purchase, restore, Terms and Privacy controls. Keep premium access closed for inactive/error
states. A reachable restore control is not proof that a previous transaction was restored.

Run genuine sandbox/test-track purchases and restoration with suitable store accounts when available.
An isolated Android emulator without an eligible Play account may fail billing even when the catalog
is linked. Diagnose the account, installation source, track eligibility, product state, credentials and
SDK error together. Do not infer the cause from a numeric code alone or grant a fake entitlement.

Finish with a sanitized mapping of project, two apps, four products, entitlement, offering, packages,
paywall, credential flags and original credential references without file contents. Record SDK/build
versions, actual prices observed, notification/webhook status, test evidence and remaining store review.
Keep configuration verification, native UI verification, transaction verification and public launch
separate. Continue a partially completed setup from these returned resource IDs rather than deleting
and recreating everything. See [operations](testing-and-operations.md) for lifecycle coverage.
