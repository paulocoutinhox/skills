# Publisher API coverage and operation selection

Written by hand from the official **Publisher v3 Discovery** and method reference. The list of operations matches revision **20261118** (149 operations), checked on **2026-11-18**. It covers the current functional resource families in that snapshot. It is written workflow guidance, not generated schemas or a bundled API client.

The ordinary service root is `https://androidpublisher.googleapis.com/androidpublisher/v3/`. Media uploads have their own documented upload path and protocol. The scope is `https://www.googleapis.com/auth/androidpublisher`, with the real Play app permissions. Read [authentication and requests](api-and-bootstrap.md) first. Use the exact method model for nested fields, permissions and state rules.

## Ordinary Play release and listing operations

| Family | Supported methods and how to use them |
| --- | --- |
| `edits` | `insert`, `get`, `validate`, `commit`, `delete`. Open an edit for an existing app, record its expiry, read the current state, stage changes, validate and commit only the intended scope. Delete throws away the edit, not the app. |
| `edits.details` | `get`, `patch`, `update`. Manage the default language and the real support email, phone and website. Keep values you did not set, and do not invent price or category fields. |
| `edits.listings` | `list`, `get`, `patch`, `update`, `delete`, `deleteall`. Manage the localized title, short and full descriptions and YouTube video. Deleting a whole listing is not a normal fix for a missing field. |
| `edits.images` | `list`, `upload`, `delete`, `deleteall`. Pick the real locale and type, send real media, read the returned hashes and IDs and check the gallery order. You cannot invent a reorder action or a new enum. |
| `edits.bundles` | `list`, `upload`. Upload the signed AAB through the supported media protocol and check the reserved version code that comes back. |
| `edits.apks` | `list`, `upload`, `addexternallyhosted`. Use AAB for new ordinary releases. APK and external-hosting support depends on conditions and does not make every new app eligible. |
| `edits.deobfuscationfiles` | `upload`. Attach the matching mapping or native-symbol type to the real artifact version, and keep symbol access restricted. |
| `edits.expansionfiles` | `get`, `patch`, `update`, `upload`. Only for an existing eligible APK expansion setup. Do not add OBB-era infrastructure to a new AAB project. |
| `edits.tracks` | `create`, `get`, `list`, `patch`, `update`. Use the real track and form-factor IDs, the intended version graph, notes, status, priority and the allowed fraction and targeting. Keep retained versions. |
| `edits.testers` | `get`, `patch`, `update`. Set up supported tester-group access for the chosen track. This does not allow you to invite random people or fake production-access testing. |
| `edits.countryavailability` | `get` only in this snapshot. Check availability and sync status. A GET resource does not mean a country-availability PATCH endpoint exists. |
| `applications.tracks.releases` | `list`. Check release history for the real app and track. Do not assume the active edit's bundle list is a full history of every version code used. |
| `applications.dataSafety` | `dataSafety` POST. Write the official CSV safety-label answers in the `safetyLabels` string. Check the facts and format, then check the real console declaration. |
| `applications.deviceTierConfigs` | `create`, `get`, `list`. Set up real device-tier targeting where the build or content design uses it. A config does not publish another track by itself. |

Read [listing field ownership/ASO](listing-and-marketing.md), [media](screenshots-and-media.md), [build allocation](build-and-versioning.md) and [edit/review transitions](edits-review-and-rollout.md) for the concrete steps.

## Commerce, customer purchases and financial changes

| Family | Supported methods and correct sequence |
| --- | --- |
| `monetization` | `convertRegionPrices`. Get supported regional price suggestions from a real `Money` amount, then review local currency, tax and business decisions before saving. It does not set the app download price by itself. |
| `monetization.onetimeproducts` | `get`, `list`, `batchGet`, `patch`, `batchUpdate`, `delete`, `batchDelete`. Create through the supported upsert with `allowMissing` when you mean to, keep the full intended nested options, and send the real update mask and regions version. |
| `monetization.onetimeproducts.purchaseOptions` | `batchUpdateStates`, `batchDelete`. Activate or deactivate through the documented state-action requests. You write purchase options in the parent product, not through a made-up standalone insert. |
| `monetization.onetimeproducts.purchaseOptions.offers` | `list`, `batchGet`, `batchUpdate`, `activate`, `deactivate`, `cancel`, `batchUpdateStates`, `batchDelete`. Create or update with the supported batch contract, then make the right state change. Tell discounted, preorder and game-reward offers apart. |
| `monetization.subscriptions` | `get`, `list`, `batchGet`, `create`, `patch`, `batchUpdate`, `delete`. Set up the real localized subscription and base plans. The retained `archive` method and archived field are deprecated, and subscription archiving is not supported. Do not use it as a new workflow. |
| `monetization.subscriptions.basePlans` | `activate`, `deactivate`, `batchUpdateStates`, `delete`, `migratePrices`, `batchMigratePrices`. You create and configure base plans in the subscription graph. State changes and moving existing prices have their own actions and different effects on customers. |
| `monetization.subscriptions.basePlans.offers` | `create`, `get`, `list`, `batchGet`, `patch`, `batchUpdate`, `activate`, `deactivate`, `batchUpdateStates`, `delete`. Set up eligibility, phases, region prices and tags, and activate only under an eligible active parent. |
| `purchases.productsv2` | `getproductpurchasev2`. Read the current one-time purchase state and context from the source of truth. A product catalog record is not proof of a purchase. |
| `purchases.products` | `get`, `acknowledge`, `consume`. Use supported purchase-token processing under the real owner of the transaction. Save a lasting, idempotent delivery before the app itself completes the purchase. |
| `purchases.subscriptionsv2` | `get`, `cancel`, `defer`, `revoke`, `schedulePlanTransition`, `cancelPlanTransition`, `activateOfferTargeting`, `deactivateOfferTargeting`. Read the current line items and entitlement, and apply only the intended, authorized customer operation. Cancel, defer and revoke do not mean the same thing. A scheduled plan transition needs the subscription `productId` and `earliestTransitionEffectiveTime`. It takes effect at a renewal on or after that time and accepts an optional `etag` from `get` to refuse an outdated state. Its `definiteTransition` mode cannot be canceled later, while `tentativeTransition` can be withdrawn with `cancelPlanTransition`. Read the returned plan transition details back. Offer targeting turns a specific discounted `offerId` on or off for that purchase token. These change one customer's subscription and need explicit authorization for that customer. |
| `purchases.subscriptions` | Retained `acknowledge`, `cancel`, `defer`. Use the real supported acknowledgment contract and the current v2 lifecycle operations for new work. Do not add removed or deprecated status paths. |
| `purchases.voidedpurchases` | `list`. Match real refunds, chargebacks and voided purchases using pagination and time filters and the entitlement and ledger policy. Never grant or remove access from an unchecked webhook alone. |
| `orders` | `get`, `batchget`, `refund`, `reviewrefund`. Read real orders and the specific refund or review contract. A refund can have money effects that cannot be undone, so keep the exact user or customer scope and idempotency evidence. |
| `externaltransactions` | `createexternaltransaction`, `getexternaltransaction`, `refundexternaltransaction`. Only for reporting eligible alternative or external billing, with the real program, region and account duties. It does not allow you to skip required Play Billing. |

See [commercial configuration](pricing-and-availability.md) and [billing lifecycle](products-and-subscriptions.md). Deleting an edit, or an edit that fails, does not undo any of these standalone writes.

## Distribution, operations and account access

| Family | Use and boundary |
| --- | --- |
| `internalappsharingartifacts` | `uploadapk`, `uploadbundle`. Return real sharing artifacts and links with their real test signature and access rules. This is separate from publishing an internal test-track release. |
| `generatedapks` | `list`, `download`. Get the generated APKs for the real bundle, version and signing key. Downloaded artifacts do not create a new production release. |
| `systemapks.variants` | `create`, `get`, `list`, `download`. Only for eligible system or preinstall distribution. Match the real device, signing and program contract. |
| `apprecovery` | `create`, `list`, `addTargeting`, `deploy`, `cancel`. Create a draft recovery action with explicit target versions and devices, inspect it and deploy only the intended recovery that customers will see. A draft is not a deployed action. |
| `appsigning` | `enrollApp`, `rotateAppSigningKey`. Current self-hosted Cloud KMS signing enrollment and rotation. Before any change, confirm real program eligibility, key ownership and the fingerprints used downstream. It is not a shortcut for resetting an upload key. |
| `reviews` | `get`, `list`, `reply`. Read customer feedback from the store, and post public replies only when messaging is authorized. These are not policy-review messages or an appeal API. |
| `users` | `create`, `list`, `patch`, `delete`. Manage the real developer-account principal, expiry and permissions. Do not widen access because release credentials are missing a needed grant. |
| `grants` | `create`, `patch`, `delete`. Give the intended identity only the app access it needs. Read the principal and app scope and check the changed permissions. |

## Specialized app-store-hosted review surface

The current Discovery includes `appstoreappsreview`. Its paths are under `appstore/{appStorePackageName}/...` and need the real eligible app-store program and host identity. They are **not** ordinary Google Play app creation or the Play Console publishing overview.

The supported sequence is:

1. `createappstorehostedapp` creates the host's app record from its real package name, before any other operation for that hosted app.
2. `uploadapk`, `uploadimage` and `uploadappstoreapppolicydeclarationfile` return artifact IDs for the real APK, icons and screenshots, and declaration files. Follow each method's supported transfer contract. Do not copy the ordinary edit image endpoint.
3. `updateappstorehostedapp` sends `packageName`, general `appDetails`, `activeApks`, `activeLocalizedStoreListings` and `policyDeclarations`. Its current documented effect sends the update for review right away.
4. `updateappstorehostedapppublishstatus` controls the supported published or unpublished state. The update operation's default publishing behavior is important, so understand it before you call it.

`appstorecatalog.recentAppViews.get` and `appstorecatalog.recentUpdateEvents.list` give the eligible catalog's app metadata and update events. The Discovery family IDs are `appstorecatalog.recentappviews` and `appstorecatalog.recentupdateevents`, while the reference shows camelCase. Look up the real method path instead of inventing a normal `applications.insert`.

Do not use this program-specific workflow just to get around a missing ordinary Play API. Check the current service description and account permissions, collect the real host and app context, and explain why it applies before you run it.

## Separate services and actual console gaps

Play Developer Reporting, Play Integrity, Google Cloud Pub/Sub, Billing client and Play Games Services have their own contracts. Publisher access does not authorize them by itself. Set up the real service, identity and role when the task needs it.

Some work has console steps that the ordinary Listing/AppDetails models do not cover: first app creation, app or game, category and tags, the main paid download price and free or paid choice, general country distribution setup, app content and reviewer forms, managed-publishing controls, policy messages and appeals, and custom listings and experiments. Check the current exact surface before you decide something is missing, but never invent JSON properties or private endpoints. When the owner authorized browser use for this task, the agent does these console-only steps in the owner's signed-in browser through [the Console browser procedure](play-console-browser.md). Otherwise each one becomes an exact owner handoff.

The current Play Console also has an Asset Library and newer promotion areas. Seeing them in the UI does not prove ordinary Publisher upload or placement methods exist. When no documented API exists, prepare the right assets and do the supported console step under the same browser-or-handoff model.
