# API coverage and task routing

This hand-written map covers the functional families in the official **OpenAPI 4.6** snapshot checked on **2026-11-05**. A family ending in `*` groups related named resources. It is not an HTTP wildcard endpoint. The map explains when and how to use each area. It is not a generated endpoint dump or a claim that every operation is open to every account.

Use [authentication/request guidance](api-and-bootstrap.md), then choose the matching workflow below. Read the exact current method model when you build a request. Optional fields in the model, account eligibility and requirements that depend on state all matter. Do not build on deprecated operations just because they are still in the contract.

## App, build, media, commerce and review

| Functional family | Real resources and how to operate them |
| --- | --- |
| Identity and app graph | `apps`, `appInfos`, `appInfoLocalizations`, `appCategories`, `appTags`, `androidToIosAppMappingDetails`. Find the real app, platform and localization IDs, edit the resource that owns the field and check relationships. Creating the first app record must be done in the console. |
| Versions and binary intake | `appStoreVersions`, `preReleaseVersions`, `builds`, `buildBundles`, `buildUploads`, `buildUploadFiles`. Reserve a build number, upload the real signed package, wait for processing and link the compatible build. Read [build instructions](build-and-release.md). |
| Current public media | `appAssetLibraries`, `appAssetLibraryImages`, `appAssetLibraryVideos`, `appAssetLibraryRefData`, `appAssetLibraryPlacements`, `appAssetLibraryPlacementOrderingRequests`. Find specifications, upload once, commit, check, place on the real surface and order within its locale and group. Read [media instructions](screenshots-and-media.md). |
| Version text | `appStoreVersionLocalizations`. Create missing locales, PATCH the intended fields and keep the others. Name and subtitle belong to AppInfo localizations. Read [all core fields](store-fields-and-localizations.md) and [ASO](metadata-and-marketing.md). |
| Compliance and documents | `ageRatingDeclarations`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appEncryptionDeclarationDocuments`, `endUserLicenseAgreements`, `routingAppCoverages`. Gather the real facts, choose current enums, upload required supporting documents and link the correct build, version or app. |
| Review graph | `appStoreReviewDetails`, `appStoreReviewAttachments`, `reviewSubmissions`, `reviewSubmissionItems`. Prepare working reviewer access, create the submission and items, submit, watch, fix and resolve eligible items. Messages with App Review are a separate console operation. |
| Release | `appStoreVersionReleaseRequests`, `appStoreVersionPhasedReleases`, `endAppAvailabilityPreOrders`. Choose the real release scope and an eligible state. Manual release, pausing or completing a phase and ending a preorder affect customers. |
| App pricing/countries | `territories`, `appPricePoints`, `appPriceSchedules`, `appAvailabilities`, `territoryAvailabilities`. Read the returned price points and schedules, write the intended base and manual prices and the current v2 availability. Read [commercial instructions](pricing-and-availability.md). |
| IAP configuration | `inAppPurchases`, `inAppPurchaseVersions`, `inAppPurchaseLocalizations`, `inAppPurchaseAppStoreReviewScreenshots`, `inAppPurchaseImages`, `inAppPurchaseContents`. Create the current parent and version resources, localized metadata and review media, then check the eligible review link. |
| IAP commerce | `inAppPurchasePricePoints`, `inAppPurchasePriceSchedules`, `inAppPurchaseAvailabilities`, `inAppPurchaseOfferCodes`, `inAppPurchaseOfferCodeCustomCodes`, `inAppPurchaseOfferCodeOneTimeUseCodes`, `promotedPurchases`. Set prices, countries and codes, and decide store promotion separately. |
| Subscription graph | `subscriptionGroups`, `subscriptionGroupVersions`, `subscriptionGroupLocalizations`, `subscriptions`, `subscriptionVersions`, `subscriptionLocalizations`, `subscriptionAppStoreReviewScreenshots`, `subscriptionImages`. Use the current version-based localization, media and review relationships. |
| Subscription commerce | `subscriptionPricePoints`, `subscriptionPrices`, `subscriptionAvailabilities`, `subscriptionPlanAvailabilities`, `subscriptionIntroductoryOffers`, `subscriptionPromotionalOffers`, `subscriptionOfferCodes`, `subscriptionOfferCodeCustomCodes`, `subscriptionOfferCodeOneTimeUseCodes`, `winBackOffers`, `subscriptionGracePeriods`. Set up real plans, regions and offers, and keep the effects on existing subscribers separate. |
| Retention surfaces | `retentionMessages`, `retentionMessageVersions`, `retentionMessageLocalizations`, `retentionOffers`. Create the eligible content, version and offer set, localize it and submit the supported review item. Do not mix this up with server-side cancellation or refund processing. |

The workflow pages give request fields, ordered steps, examples and how to handle failures. A product's sale state is not a writable shortcut to review approval. The separate App Store Server API owns customer transaction operations.

## Testing, optimization and external distribution

| Functional family | Procedure and verification |
| --- | --- |
| TestFlight app/build metadata | `betaAppLocalizations`, `betaBuildLocalizations`, `betaLicenseAgreements`, `buildBetaDetails`. Give the testing description, feedback, contact and license and the test details for each build. Check build expiry and eligibility before distribution. |
| Beta review | `betaAppReviewDetails`, `betaAppReviewSubmissions`. Give working access and submit an eligible external beta review. This is not App Store review. |
| Testers and groups | `betaGroups`, `betaTesters`, `betaTesterInvitations`, `buildBetaNotifications`, `betaRecruitmentCriteria`, `betaRecruitmentCriterionOptions`. Choose the allowed audience, attach real builds, set allowed public recruitment criteria and check what invitations and public links do. |
| Beta diagnostics | `betaFeedbackCrashSubmissions`, `betaFeedbackScreenshotSubmissions`, `betaCrashLogs`, `diagnosticSignatures`. Read the relevant build and tester evidence, protect personal data and match it to the exact source and symbols. Do not treat a crash sample as every install. |
| Sandbox accounts | `sandboxTesters`, `sandboxTestersClearPurchaseHistoryRequest`. Use real test identities and limited history resets for purchase testing. Never reset production customer history or confuse sandbox accounts with TestFlight user accounts. |
| App Clips | `appClips`, `appClipDefaultExperiences`, `appClipDefaultExperienceLocalizations`, `appClipHeaderImages`, `appClipAdvancedExperiences`, `appClipAdvancedExperienceImages`, `appClipAppStoreReviewDetails`, `betaAppClipInvocations`, `betaAppClipInvocationLocalizations`. Link the real invocation, domain and build setup, metadata, media and review. Test invocation URLs and the entitlement link. |
| Custom product pages | `appCustomProductPages`, `appCustomProductPageVersions`, `appCustomProductPageLocalizations`. Create an eligible page and version, localize honest targeted messages, place media, set supported intent and keywords and submit the version before checking its real link. |
| Product-page experiments | `appStoreVersionExperiments`, `appStoreVersionExperimentTreatments`, `appStoreVersionExperimentTreatmentLocalizations`, `appStoreVersionPromotions`. Use the current version of the resource and operation that is not deprecated, choose treatments, traffic and a success metric, submit where required and apply a winner only after you have evidence. |
| In-app events | `appEvents`, `appEventLocalizations` and current library placements. Set the real event type, dates, territories, deep link and honest localized text and media, then submit and check the timing. |
| Featuring | `nominations`. Prepare an accurate pitch for the event or update and supporting assets for the real date. A nomination does not promise an editorial placement or approval. |
| Apple-hosted assets | `backgroundAssets`, `backgroundAssetVersions`, `backgroundAssetUploadFiles`, `backgroundAssetVersionAppStoreReleases`, `backgroundAssetVersionInternalBetaReleases`, `backgroundAssetVersionExternalBetaReleases`. Upload and version real packs, test beta delivery, review where needed and release the correct pack separately from the binary upload. |
| Alternative distribution | `alternativeDistributionDomains`, `alternativeDistributionKeys`, `alternativeDistributionPackages`, `alternativeDistributionPackageVersions`, `alternativeDistributionPackageVariants`, `alternativeDistributionPackageDeltas`, `marketplaceSearchDetails`, `marketplaceWebhooks`. Check regional, program and legal eligibility, ownership and the notarization path, then manage the documented packages, keys and domains. Normal App Store approval does not allow this route automatically. |

## Game Center

These families need the real platform and Game Center eligibility and the right version and release setup. Do not turn on every part in a release that is not a game.

| Subsystem | Resources and how to use them |
| --- | --- |
| App/group setup | `gameCenterDetails`, `gameCenterEnabledVersions`, `gameCenterAppVersions`, `gameCenterGroups`, `gameCenterDetailPlayers`. Link the real app, version and group and the supported player setup before releasing content. |
| Achievements | `gameCenterAchievements`, `gameCenterAchievementVersions`, `gameCenterAchievementLocalizations`, `gameCenterAchievementImages`, `gameCenterAchievementReleases`. Set up the real achievement and rules, the current version, localized content and icon, review and release. |
| Leaderboards | `gameCenterLeaderboards`, `gameCenterLeaderboardVersions`, `gameCenterLeaderboardLocalizations`, `gameCenterLeaderboardImages`, `gameCenterLeaderboardReleases`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetVersions`, `gameCenterLeaderboardSetLocalizations`, `gameCenterLeaderboardSetMemberLocalizations`, `gameCenterLeaderboardSetImages`, `gameCenterLeaderboardSetReleases`. Choose score format, order and ranges and stable identifiers, group and localize, then review and release eligible versions. |
| Activities and challenges | `gameCenterActivities`, `gameCenterActivityVersions`, `gameCenterActivityLocalizations`, `gameCenterActivityImages`, `gameCenterActivityVersionReleases`, `gameCenterChallenges`, `gameCenterChallengeVersions`, `gameCenterChallengeLocalizations`, `gameCenterChallengeImages`, `gameCenterChallengeVersionReleases`. Create the real content, version and localizations, submit supported items and check the released experience. |
| Matchmaking | `gameCenterMatchmakingQueues`, `gameCenterMatchmakingRuleSets`, `gameCenterMatchmakingRules`, `gameCenterMatchmakingTeams`, `gameCenterMatchmakingRuleSetTests`. Define concrete player limits, check them with rule-set tests and attach only the intended production setup. |
| Scores and moderation | `gameCenterLeaderboardEntrySubmissions`, `gameCenterPlayerAchievementSubmissions`, `gameCenterScoreModerations`. Use eligible authenticated operations for real results and moderation. Never fake player activity or rankings. |

## Account, automation interfaces and reports

| Functional family | Procedure and boundary |
| --- | --- |
| Access | `users`, `userInvitations`, `actors`. Read real identity and access, invite only allowed people, give the lowest roles and app scope and check the results. Actor records are not credentials you can use. |
| Signing/services | `bundleIds`, `bundleIdCapabilities`, `certificates`, `profiles`, `devices`, `merchantIds`, `passTypeIds`. Set up only what the real app, extensions, payments and wallet need, match entitlements and treat a revocation as something that affects builds that depend on it. |
| Xcode Cloud | `ciProducts`, `ciWorkflows`, `ciBuildRuns`, `ciBuildActions`, `ciArtifacts`, `ciIssues`, `ciTestResults`, `ciMacOsVersions`, `ciXcodeVersions`. Pick the real product, workflow and toolchain, start only allowed runs and check actions, artifacts and test results. A successful CI job is not a submitted release. |
| SCM for Xcode Cloud | `scmProviders`, `scmRepositories`, `scmGitReferences`, `scmPullRequests`. Find the connected repository and the real revision. Read-only SCM lookups do not allow creating branches or pull requests. Follow the user's repository workflow. |
| Store customer reviews | `customerReviews`, `customerReviewResponses`. Read and filter by real app, version and territory, write a relevant public answer and post it only when sending messages is allowed. These are customer reviews, not App Review messages. |
| App Analytics | `analyticsReportRequests`, `analyticsReports`, `analyticsReportInstances`, `analyticsReportSegments`. Request access to eligible reports, list instances and segments and download the intended date range. Watch freshness, retention and privacy, and keep counts, cohorts and proceeds apart. |
| Sales and finance | `salesReports`, `financeReports`. Use allowed vendor, report, period and region parameters, handle compressed report files and match the correct fiscal or calendar period. Do not make financial reports public. |
| App-scoped webhooks | `webhooks`, `webhookPings`, `webhookDeliveries`. Set the real URL, event types, secret and enabled state, check them with the documented authentication contract and look at delivery and ping status. These are not App Store Server Notifications for purchases. |

## Deprecated surfaces and real gaps

The snapshot still has `appScreenshotSets`, `appScreenshots`, `appPreviewSets`, `appPreviews`, `appEventScreenshots` and `appEventVideoClips`. New public media work uses Asset Library, not compatibility code around those old resources. Product review screenshots and dedicated attachment endpoints are separate supported contracts.

`appStoreVersionSubmissions`, `inAppPurchaseSubmissions`, `subscriptionSubmissions` and `subscriptionGroupSubmissions` also need a check of deprecation and current review guidance. Prefer the current `reviewSubmissions` / `reviewSubmissionItems` and version relationships for new work. A path that still exists is not advice to call it.

The contract does not cover every Connect screen. Normal first app records, owner agreements, banking, tax and trader statements, App Privacy questionnaire publishing, app tax-category choices and App Review messages and appeals have documented console or owner handoffs. App transfers, business-distribution enrollment and account setup must use their real supported screens, not a guessed `/transfer` endpoint.

For a task outside this snapshot, find its real official operation and state limits before running it, update the field list for the requested work and name the exact step that is not supported. Do not build a general REST client for the private console, scrape a logged-in browser or claim full execution from this routing map.
