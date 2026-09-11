.. include:: ../common/common_definitions.rst
.. Included via index.rst at title level '=' (document title).


Open Source Releases
=====================

1. General Principles
^^^^^^^^^^^^^^^^^^^^^

The IT-Wallet ecosystem is built upon principles of openness and transparency. In accordance with the **Italian Digital Administration Code (CAD)** and the **European eIDAS 2.0 Regulation**, the adoption of open source frameworks, including during the experimentation phase, is strongly encouraged as a key enabler to ensure trust, collaboration, peer review and shared improvements across the ecosystem. This framework aligns with the **Interoperable Europe Act**, aiming to maximize public value and security through transparency.

2. Standard Requirements
^^^^^^^^^^^^^^^^^^^^^^^^

All entities (Wallet Providers, Credential Issuers, Relying Parties) involved within the IT-Wallet ecosystem (hereinafter "Project Owners") **SHOULD** adhere to industry best practices to ensure the software is usable, compliant, and secure, following at least those listed in the sections below.

2.1 Licensing
"""""""""""""

- Project Owners **MUST** use an Open Source Initiative (OSI) approved license.
- Project Owners **SHOULD** prioritize the **EUPL-1.2** (European Union Public License version 1.2) to ensure legal compatibility within the EU public sector, or permissive licenses (e.g., Apache 2.0, MIT) for SDKs and libraries to maximize adoption.

2.2 Code Management & Transparency
""""""""""""""""""""""""""""""""""

- **Version Control**: Project Owners **MUST** use code hosting platforms that allow public access without requiring a login (e.g., GitHub, GitLab), ensuring a transparent history of changes.
- **Documentation**: Repositories **MUST** include clear documentation, such as:

  - ``README.md``: Project overview and setup instructions.
  - ``LICENSE.md``: Terms under which the copyright holder allows the recipient to use the software (as described in the *Licensing* section above).
  - ``CONTRIBUTING.md``: Guidelines for contributions to the codebase made by externals (e.g., community contributors).

- **Community**: Project Owners **SHOULD** actively engage with the community for development and support, managing issues and requests for contributions in a timely manner.

2.3 Security & Quality
""""""""""""""""""""""

- **Code Quality**: Project Owners **SHOULD** implement automated testing (e.g., E2E and integration tests) and Continuous Integration pipelines. Such pipelines **SHOULD** be public to allow inspection.
- **Security Audits**: Project Owners **SHOULD** perform regular code audits and static analysis.
- **SBOM**: Project Owners **SHOULD** provide a Software Bill of Materials (SBOM) to facilitate vulnerability management, in line with the **Cyber Resilience Act (CRA)**.

3. Wallet Providers
^^^^^^^^^^^^^^^^^^^

3.1 Mandatory Open Source
"""""""""""""""""""""""""

Pursuant to the **Consolidated Regulation (EU) No 910/2014 (eIDAS 2.0)**, Art. 5a par. 3, the source code of the application software components of IT-Wallet solutions **MUST** be open-source licensed.

For duly justified security reasons, the source code of specific components, other than those installed on user devices, **MAY** remain closed, provided this does not compromise the overall auditability of the solution.

4. Credential Issuers and Relying Parties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

4.1 Integration components
""""""""""""""""""""""""""

To foster ecosystem interoperability and reduce integration costs:

- Credential Issuers and Relying Parties **SHOULD** release Software Development Kits (SDKs), client libraries, and API specifications under an open-source license.

4.2 Backend infrastructure
""""""""""""""""""""""""""

Credential Issuers and Relying Parties **SHOULD** release their backend core logic under an open-source license, starting from the experimentation phase, to promote transparency and reuse.

5. Responsible Disclosure and Vulnerability Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In compliance with the **Cyber Resilience Act (CRA)** and **NIS2 Directive (EU) 2022/2555**:

- **Security Policy**: All Open Source repositories **SHOULD** contain a ``SECURITY.md`` file outlining the procedure for reporting vulnerabilities.
- **Reporting**: Project Owners **SHOULD** establish a channel for responsible disclosure to handle security issues privately before public release.
- **Exploited vulnerabilities**: Project Owners **MUST** cooperate with National Computer Security Incident Response Teams (CSIRTs) regarding actively exploited vulnerabilities and strictly follow coordinated disclosure protocols to mitigate threats derived from irresponsible disclosure.


