# Sources and versions

Verified: 2026-11-05. Refresh standard versions before a formal assessment.

- [OWASP Top 10:2025](https://top10.owasp.org/2025/): current web awareness families. This replaces an assumed 2021-only baseline.
- [OWASP ASVS](https://asvs.owasp.org/): version 5.0.0 verification requirements. Use precise requirement IDs from the chosen version for a formal control mapping.
- [API Security Top 10:2023](https://api-security.owasp.org/editions/2023/en/0x11-t10/): API authorization, consumption, inventory, and upstream trust risks.
- [OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) and [authorization testing](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Testing_Automation_Cheat_Sheet.html): object checks and permission matrices.
- [MASVS](https://mas.owasp.org/MASVS/) and its linked MASTG/MASWE resources: mobile control families and testing detail.
- [Desktop security project](https://owasp.org/projects/desktop-app-security-top-10): incubator awareness list with a 2021 baseline. It is not represented as a new 2025 desktop verification standard.
- [Electron security guide](https://www.electronjs.org/docs/latest/tutorial/security): renderer, bridge, navigation, and process boundary protections.
- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines): memory, ownership, and concurrency considerations.
- [GitHub workflow security](https://docs.github.com/en/actions/reference/security/secure-use): event trust, permissions, and workflow inputs.
- [RevenueCat webhooks](https://www.revenuecat.com/docs/integrations/webhooks): an example of configured authorization plus optional signing, not a universal signature protocol. Rechecked on 2026-11-05.

The catalogs are an original operational synthesis. They do not reproduce entire standards, certify compliance, or guarantee complete coverage. Detailed controls depend on the exact platform, language, architecture, and authorized scope.

## Professional foundation and evidence scope

Reviewed for this revision: 2026-11-05. Ross Anderson's [Security Engineering, third edition](https://www.cl.cam.ac.uk/archive/rja14/book.html) is professional further reading. Its author-hosted index identifies adversary, access-control, protocol, distributed-system and assurance chapters. The revision does not claim a full-book reading. Actual audit controls/tests remain tied to the applicable ASVS/MASVS/platform documentation and observed evidence.

Stored content is maintained only when the user requests a revision. There is no automated source collector or refresh mechanism.
