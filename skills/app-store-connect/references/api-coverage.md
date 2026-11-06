# API coverage and task routing

This manually authored map covers the functional families in the official **OpenAPI 4.6** snapshot inspected on **2026-11-05**. A family ending in `*` groups the related named resources, not an HTTP wildcard endpoint. It explains when and how to use the surface. It is not a generated endpoint dump or a claim that every operation is available to every account.

Use [authentication/request guidance](api-and-bootstrap.md), then choose the relevant workflow below. Read the exact current method model when forming a request. Model-level optionality, account eligibility and state-dependent requirements all matter. Do not implement deprecated operations because they remain in the contract.

## App, build, media, commerce and review

| Functional family | Real resources and how to operate them |
| --- | --- |
| Identity and app graph | `apps`, `appInfos`, `appInfoLocalizations`, `appCategories`, `appTags`, `androidToIosAppMappingDetails`. Resolve actual app/platform/localization IDs, edit the owning resource and verify relationships. Initial app creation is a console boundary. |
| Versions and binary intake | `appStoreVersions`, `preReleaseVersions`, `builds`, `buildBundles`, `buildUploads`, `buildUploadFiles`. Allocate build, upload the actual signed package, await processing and associate the compatible build. Read [build instructions](build-and-release.md). |
| Current public media | `appAssetLibraries`, `appAssetLibraryImages`, `appAssetLibraryVideos`, `appAssetLibraryRefData`, `appAssetLibraryPlacements`, `appAssetLibraryPlacementOrderingRequests`. Discover specifications, upload once, commit, verify, place on the actual surface and order within its locale/group. Read [media instructions](screenshots-and-media.md). |
| Version text | `appStoreVersionLocalizations`. Create missing locales, PATCH intended fields and preserve others. Name/subtitle belong to AppInfo localizations. Read [all core fields](store-fields-and-localizations.md) and [ASO](metadata-and-marketing.md). |
| Compliance and documents | `ageRatingDeclarations`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appEncryptionDeclarationDocuments`, `endUserLicenseAgreements`, `routingAppCoverages`. Gather actual facts, select current enums, upload required supporting documents and associate the correct build/version/app. |
| Review graph | `appStoreReviewDetails`, `appStoreReviewAttachments`, `reviewSubmissions`, `reviewSubmissionItems`. Prepare working reviewer access, create the submission/items, submit, monitor, correct and resolve eligible items. Correspondence is a separate console operation. |
| Release | `appStoreVersionReleaseRequests`, `appStoreVersionPhasedReleases`, `endAppAvailabilityPreOrders`. Choose actual release scope and eligible state. Manual release, phase pause/completion and ending a preorder affect customers. |
| App pricing/countries | `territories`, `appPricePoints`, `appPriceSchedules`, `appAvailabilities`, `territoryAvailabilities`. Read returned price points and schedules, write intended base/manual prices and current v2 availability. Read [commercial instructions](pricing-and-availability.md). |
| IAP configuration | `inAppPurchases`, `inAppPurchaseVersions`, `inAppPurchaseLocalizations`, `inAppPurchaseAppStoreReviewScreenshots`, `inAppPurchaseImages`, `inAppPurchaseContents`. Create current parent/version resources, localized metadata and review media, then verify eligible review linkage. |
| IAP commerce | `inAppPurchasePricePoints`, `inAppPurchasePriceSchedules`, `inAppPurchaseAvailabilities`, `inAppPurchaseOfferCodes`, `inAppPurchaseOfferCodeCustomCodes`, `inAppPurchaseOfferCodeOneTimeUseCodes`, `promotedPurchases`. Configure prices/countries/codes and separately decide storefront promotion. |
| Subscription graph | `subscriptionGroups`, `subscriptionGroupVersions`, `subscriptionGroupLocalizations`, `subscriptions`, `subscriptionVersions`, `subscriptionLocalizations`, `subscriptionAppStoreReviewScreenshots`, `subscriptionImages`. Use current version-based localization/media/review relationships. |
| Subscription commerce | `subscriptionPricePoints`, `subscriptionPrices`, `subscriptionAvailabilities`, `subscriptionPlanAvailabilities`, `subscriptionIntroductoryOffers`, `subscriptionPromotionalOffers`, `subscriptionOfferCodes`, `subscriptionOfferCodeCustomCodes`, `subscriptionOfferCodeOneTimeUseCodes`, `winBackOffers`, `subscriptionGracePeriods`. Configure real plans/regions/offers and separate existing-subscriber consequences. |
| Retention surfaces | `retentionMessages`, `retentionMessageVersions`, `retentionMessageLocalizations`, `retentionOffers`. Create the eligible content/version/offer graph, localize and submit the supported review item. Do not conflate this with server-side cancellation/refund processing. |

The workflow pages provide request fields, ordered steps, examples and failure handling. Product sale state is not a writable shortcut to review approval. The separate App Store Server API owns customer-transaction operations.

## Testing, optimization and external distribution

| Functional family | Procedure and verification |
| --- | --- |
| TestFlight app/build metadata | `betaAppLocalizations`, `betaBuildLocalizations`, `betaLicenseAgreements`, `buildBetaDetails`. Provide testing description, feedback/contact/license and per-build test details. Verify build expiry/eligibility before distribution. |
| Beta review | `betaAppReviewDetails`, `betaAppReviewSubmissions`. Provide functioning access and submit eligible external beta review. This is distinct from App Store review. |
| Testers and groups | `betaGroups`, `betaTesters`, `betaTesterInvitations`, `buildBetaNotifications`, `betaRecruitmentCriteria`, `betaRecruitmentCriterionOptions`. Choose the authorized audience, attach actual builds, configure permitted public recruitment criteria and verify invitation/public-link effects. |
| Beta diagnostics | `betaFeedbackCrashSubmissions`, `betaFeedbackScreenshotSubmissions`, `betaCrashLogs`, `diagnosticSignatures`. Read the relevant build/tester evidence, protect personal data and correlate exact source/symbols. Do not treat a crash sample as the entire install population. |
| Sandbox accounts | `sandboxTesters`, `sandboxTestersClearPurchaseHistoryRequest`. Use legitimate test identities and scoped history resets for purchase testing. Never reset production customer history or confuse sandbox accounts with TestFlight app-user accounts. |
| App Clips | `appClips`, `appClipDefaultExperiences`, `appClipDefaultExperienceLocalizations`, `appClipHeaderImages`, `appClipAdvancedExperiences`, `appClipAdvancedExperienceImages`, `appClipAppStoreReviewDetails`, `betaAppClipInvocations`, `betaAppClipInvocationLocalizations`. Link actual invocation/domain/build configuration, metadata/media and review. Test invocation URLs and entitlement association. |
| Custom product pages | `appCustomProductPages`, `appCustomProductPageVersions`, `appCustomProductPageLocalizations`. Create an eligible page/version, localize truthful targeted messages, place media, set supported intent/keywords and submit the version before verifying its actual link. |
| Product-page experiments | `appStoreVersionExperiments`, `appStoreVersionExperimentTreatments`, `appStoreVersionExperimentTreatmentLocalizations`, `appStoreVersionPromotions`. Use the current nondeprecated version of the resource/operation, choose treatments/traffic and a success metric, submit where required and explicitly apply a winner only after evidence. |
| In-app events | `appEvents`, `appEventLocalizations` and current library placements. Define actual event type, dates, territories, deep link and truthful localized text/media, then submit and verify timing. |
| Featuring | `nominations`. Prepare accurate event/update pitch and supporting assets for the real date. A nomination is not an editorial placement or approval guarantee. |
| Apple-hosted assets | `backgroundAssets`, `backgroundAssetVersions`, `backgroundAssetUploadFiles`, `backgroundAssetVersionAppStoreReleases`, `backgroundAssetVersionInternalBetaReleases`, `backgroundAssetVersionExternalBetaReleases`. Upload/version actual packs, test beta delivery, review as applicable and release the correct pack independently of binary transfer. |
| Alternative distribution | `alternativeDistributionDomains`, `alternativeDistributionKeys`, `alternativeDistributionPackages`, `alternativeDistributionPackageVersions`, `alternativeDistributionPackageVariants`, `alternativeDistributionPackageDeltas`, `marketplaceSearchDetails`, `marketplaceWebhooks`. Verify regional/program/legal eligibility, ownership and notarization path, then manage the documented packages/keys/domains. Ordinary App Store approval does not authorize this route automatically. |

## Game Center

These families need their actual platform/Game Center eligibility and version/release graph. Do not enable every subsystem in a nongame release.

| Subsystem | Resources and how to use them |
| --- | --- |
| App/group setup | `gameCenterDetails`, `gameCenterEnabledVersions`, `gameCenterAppVersions`, `gameCenterGroups`, `gameCenterDetailPlayers`. Associate the actual app/version/group and supported player configuration before content releases. |
| Achievements | `gameCenterAchievements`, `gameCenterAchievementVersions`, `gameCenterAchievementLocalizations`, `gameCenterAchievementImages`, `gameCenterAchievementReleases`. Configure the real achievement/rules, current version, localized content/icon, review and release. |
| Leaderboards | `gameCenterLeaderboards`, `gameCenterLeaderboardVersions`, `gameCenterLeaderboardLocalizations`, `gameCenterLeaderboardImages`, `gameCenterLeaderboardReleases`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetVersions`, `gameCenterLeaderboardSetLocalizations`, `gameCenterLeaderboardSetMemberLocalizations`, `gameCenterLeaderboardSetImages`, `gameCenterLeaderboardSetReleases`. Choose score format/order/ranges and stable identifiers, group/localize, review and release eligible versions. |
| Activities and challenges | `gameCenterActivities`, `gameCenterActivityVersions`, `gameCenterActivityLocalizations`, `gameCenterActivityImages`, `gameCenterActivityVersionReleases`, `gameCenterChallenges`, `gameCenterChallengeVersions`, `gameCenterChallengeLocalizations`, `gameCenterChallengeImages`, `gameCenterChallengeVersionReleases`. Create actual content/version/localizations, submit supported items and verify the released experience. |
| Matchmaking | `gameCenterMatchmakingQueues`, `gameCenterMatchmakingRuleSets`, `gameCenterMatchmakingRules`, `gameCenterMatchmakingTeams`, `gameCenterMatchmakingRuleSetTests`. Define the concrete player constraints, validate with rule-set tests and attach only the intended production configuration. |
| Scores and moderation | `gameCenterLeaderboardEntrySubmissions`, `gameCenterPlayerAchievementSubmissions`, `gameCenterScoreModerations`. Use eligible authenticated operations for actual results/moderation. Never fabricate player activity or rankings. |

## Account, automation interfaces and reports

| Functional family | Procedure and boundary |
| --- | --- |
| Access | `users`, `userInvitations`, `actors`. Read actual identity/access, invite only authorized people, apply minimum roles/app scope and verify results. Actor records are not arbitrary credentials. |
| Signing/services | `bundleIds`, `bundleIdCapabilities`, `certificates`, `profiles`, `devices`, `merchantIds`, `passTypeIds`. Provision only actual app/extensions/payment/wallet needs, match entitlements and treat revocation as a dependent-build impact. |
| Xcode Cloud | `ciProducts`, `ciWorkflows`, `ciBuildRuns`, `ciBuildActions`, `ciArtifacts`, `ciIssues`, `ciTestResults`, `ciMacOsVersions`, `ciXcodeVersions`. Select real product/workflow/toolchain, start only authorized runs and inspect actions/artifacts/test results. A successful CI job is not a submitted release. |
| SCM for Xcode Cloud | `scmProviders`, `scmRepositories`, `scmGitReferences`, `scmPullRequests`. Resolve connected repository and actual revision. Read-only SCM discovery does not authorize branches or pull requests. Respect the user's repository workflow. |
| Store customer reviews | `customerReviews`, `customerReviewResponses`. Read/filter by actual app/version/territory, draft a relevant public answer and post only when messaging is authorized. These are customer reviews, not App Review correspondence. |
| App Analytics | `analyticsReportRequests`, `analyticsReports`, `analyticsReportInstances`, `analyticsReportSegments`. Request eligible report access, enumerate instances/segments and download the intended date range. Observe freshness/retention/privacy and distinguish counts, cohorts and proceeds. |
| Sales and finance | `salesReports`, `financeReports`. Use authorized vendor/report/period/region parameters, handle compressed report delivery and reconcile the correct fiscal versus calendar period. Do not expose financial reports publicly. |
| App-scoped webhooks | `webhooks`, `webhookPings`, `webhookDeliveries`. Configure actual URL, event types, secret and enabled state, verify according to the documented authentication contract and inspect delivery/ping status. These are not App Store Server Notifications for purchases. |

## Deprecated surfaces and actual gaps

The snapshot retains `appScreenshotSets`, `appScreenshots`, `appPreviewSets`, `appPreviews`, `appEventScreenshots` and `appEventVideoClips`. New public media work uses Asset Library, not a compatibility implementation around those old resources. Product review screenshots and dedicated attachment endpoints are separate supported contracts.

`appStoreVersionSubmissions`, `inAppPurchaseSubmissions`, `subscriptionSubmissions` and `subscriptionGroupSubmissions` also require checking deprecation and current review guidance. Prefer current `reviewSubmissions` / `reviewSubmissionItems` and version relationships for new work. A retained path is not a recommendation to call it.

The contract does not expose every Connect screen. Initial ordinary app records, owner agreements/banking/tax/trader attestations, App Privacy questionnaire publication, app tax-category choices and App Review correspondence/appeals have documented console/owner handoffs. App transfers, business-distribution enrollment and account setup must use their actual supported surface, not a guessed `/transfer` endpoint.

For a task outside this snapshot, retrieve its actual official operation and state restrictions before execution, update the requested work's field inventory and identify the exact unsupported step. Do not create a generic private-console REST client, scrape a logged-in browser or claim full execution from this routing map.
