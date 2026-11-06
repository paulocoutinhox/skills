# Publisher API coverage and operation selection

Manually authored from the official **Publisher v3 Discovery revision 20261105** and method reference, inspected on **2026-11-05**. This covers every functional resource family in that snapshot. It is written workflow guidance, not generated schemas or a bundled API client.

The ordinary service root is `https://androidpublisher.googleapis.com/androidpublisher/v3/`. Media uploads have a distinct documented upload path/protocol. Scope is `https://www.googleapis.com/auth/androidpublisher`, with actual Play app permissions. Read [authentication and requests](api-and-bootstrap.md) first. Use the precise method model for nested fields, permissions and state restrictions.

## Ordinary Play release and listing operations

| Family | Supported methods and how to use them |
| --- | --- |
| `edits` | `insert`, `get`, `validate`, `commit`, `delete`. Open an existing app's edit, record expiry, read current state, stage changes, validate and commit only the intended scope. Delete discards the edit, not the app. |
| `edits.details` | `get`, `patch`, `update`. Manage default language and actual support email/phone/website. Preserve unspecified values and do not invent price/category fields. |
| `edits.listings` | `list`, `get`, `patch`, `update`, `delete`, `deleteall`. Manage localized title, short/full descriptions and YouTube video. A whole listing deletion is not a routine missing-field repair. |
| `edits.images` | `list`, `upload`, `delete`, `deleteall`. Select actual locale/type, transfer real media, read returned hashes/IDs and verify gallery ordering. No arbitrary reorder or new enum can be invented. |
| `edits.bundles` | `list`, `upload`. Upload signed AAB through the supported media protocol and verify returned reserved version code. |
| `edits.apks` | `list`, `upload`, `addexternallyhosted`. Use AAB for new ordinary releases. APK/external-hosting support is conditional and does not make every new app eligible. |
| `edits.deobfuscationfiles` | `upload`. Attach the matching mapping/native-symbol type to the actual artifact version, preserving restricted symbol access. |
| `edits.expansionfiles` | `get`, `patch`, `update`, `upload`. Existing eligible APK expansion configuration only. Do not introduce OBB-era infrastructure to a new AAB project. |
| `edits.tracks` | `create`, `get`, `list`, `patch`, `update`. Use real track/form-factor identifiers, intended version graph, notes, status, priority and permitted fraction/targeting. Preserve retained versions. |
| `edits.testers` | `get`, `patch`, `update`. Configure supported tester-group access for the selected track. This is not permission to invite arbitrary people or fabricate production-access testing. |
| `edits.countryavailability` | `get` only in this snapshot. Inspect availability/synchronization. A GET resource does not imply a country-availability PATCH endpoint. |
| `applications.tracks.releases` | `list`. Inspect release history for the actual app/track. Do not assume the active edit's bundle list is a complete historical version allocation ledger. |
| `applications.dataSafety` | `dataSafety` POST. Write the official CSV safety-label responses in the `safetyLabels` string. Validate facts and format, then verify the actual console declaration. |
| `applications.deviceTierConfigs` | `create`, `get`, `list`. Configure actual device-tier targeting where used by the build/content design. A config does not automatically publish another track. |

Read [listing field ownership/ASO](listing-and-marketing.md), [media](screenshots-and-media.md), [build allocation](build-and-versioning.md) and [edit/review transitions](edits-review-and-rollout.md) for concrete execution.

## Commerce, customer purchases and financial changes

| Family | Supported methods and correct sequence |
| --- | --- |
| `monetization` | `convertRegionPrices`. Derive supported regional price suggestions from a real `Money` amount, then review local currency/tax/business decisions before saving. It does not set app-download pricing by itself. |
| `monetization.onetimeproducts` | `get`, `list`, `batchGet`, `patch`, `batchUpdate`, `delete`, `batchDelete`. Create through supported upsert with `allowMissing` when intended, preserve the full desired nested options, and supply actual update mask/regions version. |
| `monetization.onetimeproducts.purchaseOptions` | `batchUpdateStates`, `batchDelete`. Activate/deactivate through the documented state-action requests. Purchase options are authored in the parent product, not through an invented standalone insert. |
| `monetization.onetimeproducts.purchaseOptions.offers` | `list`, `batchGet`, `batchUpdate`, `activate`, `deactivate`, `cancel`, `batchUpdateStates`, `batchDelete`. Create/update with the supported batch contract, then perform the appropriate state transition. Distinguish discounted, preorder and game-reward offers. |
| `monetization.subscriptions` | `get`, `list`, `batchGet`, `create`, `patch`, `batchUpdate`, `delete`. Configure actual localized subscription and base plans. The retained `archive` method/archived field is deprecated and subscription archiving is not supported. Do not use it as a new workflow. |
| `monetization.subscriptions.basePlans` | `activate`, `deactivate`, `batchUpdateStates`, `delete`, `migratePrices`, `batchMigratePrices`. Creation/configuration belongs to the subscription graph. State and existing-price migrations have dedicated actions and different customer effects. |
| `monetization.subscriptions.basePlans.offers` | `create`, `get`, `list`, `batchGet`, `patch`, `batchUpdate`, `activate`, `deactivate`, `batchUpdateStates`, `delete`. Configure eligibility, phases, region prices/tags and activate only against an eligible active parent. |
| `inappproducts` | `get`, `list`, `batchGet`, `insert`, `patch`, `update`, `batchUpdate`, `delete`, `batchDelete`. Recognize existing catalog state. New catalog design uses current one-time products, without speculative legacy compatibility flags or duplicate replacement SKUs. |
| `purchases.productsv2` | `getproductpurchasev2`. Read authoritative current one-time purchase state/context. A product catalog record is not purchase evidence. |
| `purchases.products` | `get`, `acknowledge`, `consume`. Use supported purchase-token processing under the actual transaction owner. Durable idempotent fulfillment precedes application-owned completion. |
| `purchases.subscriptionsv2` | `get`, `cancel`, `defer`, `revoke`. Read current line items/entitlement and apply only the intended authorized customer operation. Cancel, defer and revoke are not synonyms. |
| `purchases.subscriptions` | Retained `acknowledge`, `cancel`, `defer`. Use the actual supported acknowledgment contract and current v2 lifecycle operations for new implementation. Do not introduce removed/deprecated status paths. |
| `purchases.voidedpurchases` | `list`. Reconcile actual refunds/chargebacks/voided purchases with pagination/time filters and entitlement/ledger policy. Never grant or remove access from an unverified webhook alone. |
| `orders` | `get`, `batchget`, `refund`, `reviewrefund`. Read actual orders and the specific refund/review contract. A refund can have irreversible financial consequences, so preserve exact user/customer scope and idempotency evidence. |
| `externaltransactions` | `createexternaltransaction`, `getexternaltransaction`, `refundexternaltransaction`. Eligible alternative/external billing reporting only, with actual program/region/account obligations. It is not permission to bypass required Play Billing. |

See [commercial configuration](pricing-and-availability.md) and [billing lifecycle](products-and-subscriptions.md). None of these standalone writes is rolled back by deleting or failing an edit.

## Distribution, operations and account access

| Family | Use and boundary |
| --- | --- |
| `internalappsharingartifacts` | `uploadapk`, `uploadbundle`. Return real sharing artifacts/links with their actual test signature/access rules. This is separate from publishing an internal test-track release. |
| `generatedapks` | `list`, `download`. Retrieve generated APKs for actual bundle/version and signing key. Downloaded artifacts do not create a new production release. |
| `systemapks.variants` | `create`, `get`, `list`, `download`. Eligible system/preinstallation distribution only. Match the real device/signing/program contract. |
| `apprecovery` | `create`, `list`, `addTargeting`, `deploy`, `cancel`. Create a draft recovery action with explicit target versions/devices, inspect it and deploy only the intended customer-facing recovery. A draft is not a deployed action. |
| `appsigning` | `enrollApp`, `rotateAppSigningKey`. Current self-hosted Cloud KMS signing enrollment/rotation. Confirm actual program eligibility, key ownership and downstream fingerprints before mutation. Not a generic upload-key-reset shortcut. |
| `reviews` | `get`, `list`, `reply`. Read store customer feedback and post public replies only when messaging is authorized. These are not policy-review messages or an appeal API. |
| `users` | `create`, `list`, `patch`, `delete`. Manage the actual developer-account principal, expiry and permissions. Do not broaden access because release credentials lack a necessary grant. |
| `grants` | `create`, `patch`, `delete`. Apply least-privilege app access to the intended identity. Read principal/app scope and verify the changed permissions. |

## Specialized app-store-hosted review surface

The current Discovery includes `appstoreappsreview`. Its paths are under `appstore/{appStorePackageName}/...` and require the actual eligible app-store program and host identity. They are **not** ordinary Google Play app creation or the Play Console publishing overview.

The supported sequence is:

1. `createappstorehostedapp` creates the host's app record from its actual package name, before other operations for that hosted app.
2. `uploadapk`, `uploadimage` and `uploadappstoreapppolicydeclarationfile` return artifact IDs for the actual APK, icons/screenshots and declaration files. Follow each method's supported transfer contract, not the ordinary edit image endpoint by analogy.
3. `updateappstorehostedapp` supplies `packageName`, general `appDetails`, `activeApks`, `activeLocalizedStoreListings` and `policyDeclarations`. Its current documented effect sends the update for review immediately.
4. `updateappstorehostedapppublishstatus` controls the supported published/unpublished state. The update operation's default publication behavior is consequential and must be understood before calling it.

`appstorecatalog.recentAppViews.get` and `appstorecatalog.recentUpdateEvents.list` provide the eligible catalog's app metadata/update events. Discovery family identifiers are `appstorecatalog.recentappviews` and `appstorecatalog.recentupdateevents`, while the reference displays camelCase. Resolve the actual method path instead of inventing a normal `applications.insert`.

Do not enter this program-specific workflow merely to work around a missing ordinary Play API. Check the current service description and account permissions, collect the actual host/app context and explain why it applies before executing it.

## Separate services and actual console gaps

Play Developer Reporting, Play Integrity, Google Cloud Pub/Sub, Billing client and Play Games Services have separate contracts. Publisher access does not automatically authorize them. Configure the actual service, identity and role when the requested task needs it.

Ordinary initial app creation, app/game/category/tags, main paid-download price/free-paid choice, general country-distribution setup, app-content/reviewer forms, managed-publishing controls, policy correspondence/appeals and custom listings/experiments have console steps not implied by ordinary Listing/AppDetails models. Check the current exact surface before concluding a gap, but never invent JSON properties or private endpoints.

The current Play Console also has an Asset Library and newer promotional surfaces. Their presence in the UI is not evidence of ordinary Publisher upload/placement methods. Prepare correct assets and the explicit supported console handoff when no documented API exists.
