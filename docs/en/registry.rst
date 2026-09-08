.. include:: ../common/common_definitions.rst


Registry Infrastructure
==========================

The IT-Wallet ecosystem operates through a registry infrastructure that provides standardized data definitions, entity registration, and Credential discovery capabilities. The registry system consists of multiple interconnected components that support the complete lifecycle of digital Credential operations from entity onboarding to Credential presentation.

The registry architecture addresses semantic standardization, federation trust management, and Credential discovery requirements through specialized registry components that ensure interoperability and compliance across the ecosystem.

Registry Architecture Overview
------------------------------

The IT-Wallet System Register comprises six main components:

1. **Claims Registry**: Standardized semantic definitions for individual Credential attributes, data types, and validation rules.
2. **Authentic Source (AS) Registry**: Catalog of registered data providers with their declared capabilities and available claims.
3. **Federation Registry**: Authoritative list of trusted entities participating in the federation with their technical configurations.
4. **Digital Credentials Catalog**: Public discovery mechanism for available Credential types with their metadata and issuance information.
5. **Schema Registry**: Authoritative list of Credential Schemas.
6. **Taxonomy**: Hierarchical classification system organizing Credentials by domain and purpose.

These registry components are interconnected and maintained by the Supervisory Body to ensure consistency, security, and regulatory compliance across the ecosystem.

Registry Discovery Endpoint
-------------------------------

The Trust Anchor MUST provide a discovery mechanism for all registry components through standardized *well-known* endpoints providing metadata and REST API discovery information to handle complex operations like pagination and filtering.

The Trust Anchor MUST publish registry discovery metadata at the ``.well-known/it-wallet-registry`` endpoint with content negotiation support:

- **Default Content-Type**: ``application/jwt`` (signed JWT ensuring authenticity and integrity)
- **Alternative Content-Type**: ``application/json`` (plain JSON for development/debugging purposes)

Moreover, the IT-Wallet System Register MUST use two distinct access patterns:

- **Data Registry APIs**: MUST support pagination and filtering capabilities.
- **Federation Trust Infrastructure**: as defined in :ref:`trust-infrastructure:The Infrastructure of Trust`.

Below a non-normative example is given.

.. code-block:: http

    GET /.well-known/it-wallet-registry HTTP/1.1
    Host: trust-anchor.eid-wallet.example.it
    Accept: application/jwt

    HTTP/1.1 200 OK
    Content-Type: application/jwt

    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...

.. code-block:: http

    GET /.well-known/it-wallet-registry HTTP/1.1
    Host: trust-anchor.eid-wallet.example.it
    Accept: application/json

    HTTP/1.1 200 OK
    Content-Type: application/json

Registry Discovery Endpoint Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The JWT payload of the Registry Discovery response MUST contain the following parameters:

.. list-table:: Registry Discovery Endpoint — JWT Payload Parameters
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Field Name**
     - **Description**
   * - **id**
     - REQUIRED. Unique identifier of the discovery document (e.g., ``urn:it-wallet-registry:it-wallet``).
   * - **version**
     - REQUIRED. Version of the discovery document format (e.g., ``1.0.0``).
   * - **last_modified**
     - REQUIRED. Timestamp of the last modification to the discovery document (e.g., ``2024-03-15T10:30:00Z``).
   * - **endpoints**
     - REQUIRED. JSON object containing the URIs of all registry components. The following endpoint keys MUST be present:

       * **claims_registry**: URI of the Claims Registry API.
       * **authentic_sources**: URI of the Authentic Source Registry API.
       * **credential_catalog**: URI of the Digital Credentials Catalog well-known endpoint.
       * **taxonomy**: URI of the Taxonomy resource.
       * **schema_registry**: URI of the Schema Registry API.
       * **federation_list**: URI of the federation list endpoint (OpenID Federation ``/list``).
       * **federation_fetch**: URI of the federation fetch endpoint (OpenID Federation ``/fetch``).
       * **federation_resolve**: URI of the federation resolve endpoint (OpenID Federation ``/resolve``).
       * **federation_trust_mark_status**: URI of the Trust Mark status endpoint.
       * **federation_historical_keys**: URI of the historical JWKs endpoint.
   * - **content_negotiation**
     - REQUIRED. Array of content types supported by the discovery endpoint (e.g., ``["application/json", "application/jwt"]``).

JWT payload structure (when decoded):

.. code-block:: json

  {
    "id": "urn:it-wallet-registry:it-wallet",
    "version": "1.0.0",
    "last_modified": "2024-03-15T10:30:00Z",
    "endpoints": {
      "claims_registry": "https://trust-anchor.eid-wallet.example.it/api/v1/claims",
      "authentic_sources": "https://trust-anchor.eid-wallet.example.it/api/v1/authentic-sources",
      "credential_catalog": "https://trust-anchor.eid-wallet.example.it/api/v1/.well-known/credential-catalog",
      "taxonomy": "https://trust-anchor.eid-wallet.example.it/api/v1/taxonomy",
      "schema_registry": "https://trust-anchor.eid-wallet.example.it/api/v1/schemas",
      "federation_list_endpoint": "https://trust-anchor.eid-wallet.example.it/list",
      "federation_fetch_endpoint": "https://trust-anchor.eid-wallet.example.it/federation_fetch_endpoint",
      "federation_resolve_endpoint": "https://trust-anchor.eid-wallet.example.it/resolve",
      "federation_trust_mark_status_endpoint": "https://trust-anchor.eid-wallet.example.it/trust_mark_status",
      "federation_trust_mark_list_endpoint": "https://dev.ta.wallet.ipzs.it/trust_mark_listing",
      "federation_trust_mark_endpoint": "https://dev.ta.wallet.ipzs.it/trust_mark",
      "federation_historical_keys_endpoint": "https://trust-anchor.eid-wallet.example.it/federation_historical_keys"
    },
    "content_negotiation": ["application/json", "application/jwt"]
  }

Claims Registry
---------------

The **Claims Registry** provides standardized semantic definitions for individual Credential attributes, data types, and validation rules. This registry serves as the semantic foundation for Credential attribute standardization across the IT-Wallet ecosystem, working in coordination with the Taxonomy component for hierarchical classification.

The Supervisory Body MUST maintain the Claims Registry to ensure semantic consistency and regulatory compliance across the ecosystem. The registry MUST contain:

  - **Standardised Claims**: Semantic definitions for all Credential attributes with data types and validation rules.
  - **Interoperability Mappings**: Alias definitions for claims that use different terminology across standards (e.g., ISO18013-5 ``place_of_birth`` mapped to canonical ``birth_place``).
  - **Data Formats**: Standardised data types (string, date, numeric, boolean, email, url, image, array, object) with validation patterns.

The Claims Registry MUST ensure:

  - **Semantic Consistency**: Prevents conflicts between duplicate or overlapping claims across the ecosystem.
  - **Cross-border Interoperability**: Ensures EU compliance and consistent claim interpretation.
  - **Schema Validation**: Provides authoritative definitions for claim validation across all Credential scenarios.
  - **Regulatory Alignment**: Coordinates with national and EU regulatory framework.
  - **Credential-Agnostic Scenarios**: Supports scenarios where **user convenience** and **business operational efficiency** are prioritized over **regulatory compliance** and **audit trails**.

.. note::
  The Claims Registry defines semantic properties of individual attributes, but MUST NOT specify selective disclosure capabilities. Selective disclosure depends on Credential format implementations (SD-JWT, mDocs), issuer technical configurations, and presentation context. These capabilities are specified at the Credential type level within the Digital Credentials Catalog and implemented during Credential presentation flows.

Claims Registry Usage
^^^^^^^^^^^^^^^^^^^^^^^^

The Claims Registry MUST support the complete ecosystem lifecycle:

**During Onboarding Process**:

  - **AS Registration**: Authentic Sources declare available claims from standardized registry during capability registration.
  - **CI Registration**: Credential Issuers select AS entities based on required claims and register Credential types for catalog publication.
  - **RP Registration**: Relying Parties specify authorization requirements using domains/purposes for specific Credential types and/or User's attributes.

**During Operational Activities**:

  - **Credential Issuance**: Claims definitions ensure consistent data representation across different Credential types.
  - **Presentation Requests**: RPs reference claims for schema validation and authorization verification in both credential-specific and credential-agnostic scenarios.
  - **Policy Enforcement**: Authorization policies leverage domain/purpose classifications for access control.

Claims Registry Structure
^^^^^^^^^^^^^^^^^^^^^^^^^

The Claims Registry maintains language-neutral, technical definitions for semantic consistency across the ecosystem. User-facing localizations for claim names and descriptions are provided via dedicated localization bundles referenced through the ``localization.base_uri`` field, enabling efficient multilingual support without compromising the registry's structural integrity.

.. list-table:: First-level Fields of the Claims Registry
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Field Name**
     - **Description**
   * - **id**
     - REQUIRED. Unique identifier of the Claims Registry (e.g., ``urn:claims:it-wallet``).
   * - **version**
     - REQUIRED. The version of the Claims Registry (e.g., ``1.0.0``).
   * - **last_modified**
     - REQUIRED. The timestamp indicating when the Claims Registry was last updated (e.g., ``2026-03-06T00:00:00Z``).
   * - **localization**
     - REQUIRED. Localization configuration object containing:

       * **default_locale**: Default locale code (e.g., ``it``).
       * **available_locales**: Array of supported locale codes (e.g., ``["en", "it"]``).
       * **base_uri**: Base URI for localization bundle retrieval (e.g., ``https://trust-registry.eid-wallet.example.it/.well-known/l10n/claims/``).
       * **version**: Version of the localization bundle format.
   * - **claims**
     - REQUIRED. A JSON Object where each key is a claim name and each value is a JSON Object describing that claim. Each claim object contains the parameters defined in the "Claim Entry Parameters" table below.

.. list-table:: Claim Entry Parameters
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Field Name**
     - **Description**
   * - **description_l10n_id**
     - REQUIRED. Localization key referencing the human-readable description of the claim in the localization bundle (e.g., ``claim.given_name.description``).
   * - **type**
     - REQUIRED. Data type of the claim. Supported values: ``string``, ``boolean``, ``array``, ``object``.
   * - **format**
     - OPTIONAL. Semantic format qualifier for string types (e.g., ``date`` for ISO 8601 dates, ``uri``, ``data`` for Base64-encoded binary).
   * - **encoding**
     - OPTIONAL. Encoding applied to the value (e.g., ``base64``). Present when ``format`` is ``data``.
   * - **aliases**
     - OPTIONAL. Array of alternative claim names used in other standards that map to this canonical claim (e.g., ``["birthdate"]`` for ``birth_date``, ``["date_of_expiry"]`` for ``expiry_date``).
   * - **nested_claims**
     - OPTIONAL. Array of claim names that form the properties of an ``object`` type claim (e.g., ``["country", "locality", "region"]`` for ``place_of_birth``).
   * - **nested_item_claims**
     - OPTIONAL. Array of claim names representing the properties of each item in an ``array`` type claim (e.g., ``["vehicle_category_code", "issue_date", "expiry_date", "codes"]`` for ``driving_privileges``).
   * - **items**
     - OPTIONAL. JSON object describing the schema of each element in a simple ``array`` type claim (e.g., ``{"type": "string"}`` for ``nationalities``).

A non-normative example of Claims Registry structure is given below:

.. literalinclude:: ../../examples/claims-registry-example.json
  :language: JSON

.. note::
  For a better and more efficient management of the localization of the information contained in the Claims Registry, an Entity consulting it SHOULD:

  - Download the basic version of the Claims Registry (compact, without localizations) using the ``.well-known/claims`` endpoint.
  - Determine the User's preferred language.
  - Download only the necessary localization bundles.
  - Dynamically merge localised content with the Claims Registry structure.

A non-normative example of a localization bundle output is given below:

.. code-block:: json

  {
    "claim.given_name.description": "Person's given name(s) as they appear on official documents.",
    "claim.birth_date.description": "Date of birth, in ISO 8601 format (YYYY-MM-DD). Also known as birthdate.",
    "claim.driving_privileges.description": "Array of authorized vehicle categories with details.",
    "...": "..."
  }

Localization bundles MUST be available at the URI composed by appending the locale code and ``.json`` to the ``localization.base_uri`` value (e.g., ``https://trust-registry.eid-wallet.example.it/.well-known/l10n/claims/it.json``).

Authentic Source Registry
-------------------------

The Supervisory Body MUST maintain the Authentic Source Registry to enable coordinated data access and Credential issuance across the ecosystem. The AS Registry MUST contain at least:

  - **Organization Information**: Legal entity details, regulatory status, and authoritative role within specific domains.
  - **Data Capabilities**: Declared claims availability referencing standardized definitions from the Claims Registry with corresponding Taxonomy classifications.
  - **Integration Methods**: Technical access mechanisms (PDND).
  - **Intended Purposes**: Supported Credential types and business contexts for AS-CI coordination.
  - **Data Quality Assurance**: Authoritative status, update frequency, and audit trail capabilities.

The AS Registry MUST ensure:

  - **Coordinated Data Access**: Enables CI discovery of appropriate data from Authentic Sources for Credential issuance.
  - **AS-CI Integration**: Facilitates approval workflows and data access coordination between entities.
  - **Quality Assurance**: Maintains authoritative status and data reliability across different domains.
  - **Regulatory Compliance**: Supports public administration transparency and private sector coordination requirements.

.. note::
   The Authentic Source Registry is a public registry that provides the Credential Issuer with guidance for Credential provisioning.

Authentic Source Registry Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The AS Registry supports ecosystem coordination throughout the operational lifecycle:

**During Onboarding Process**:
  - **AS Self-Declaration**: Authentic Sources register capabilities before any Credential types exist in the catalog.
  - **CI Discovery**: Credential Issuers search for AS entities based on required claims and intended Credential types.
  - **Approval Coordination**: AS entities evaluate and approve CI access requests for data provision.

**During Operational Activities**:
  - **Data Source Resolution**: CI systems reference AS Registry for real-time data access during Credential issuance.
  - **Quality Validation**: AS Registry information supports data origin verification and audit requirements.
  - **Integration Management**: Technical endpoints and access methods enable standardized AS-CI communication.

Public vs Private AS Coordination
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The AS Registry architecture supports different coordination patterns reflecting distinct operational requirements:

  1. **Public Administration AS** (Standardized Integration): Government entities provide authoritative data through regulated mechanisms:

    - **PDND Integration**: ``"integration_method": "pdnd"`` for standardized government data access.
    - **Regulatory Compliance**: Full transparency requirements with public catalog publication.
    - **Audit Requirements**: Complete traceability for government Credential issuance processes.

  2. **Private Sector AS** (Flexible Integration): Private entities provide specialized data through custom arrangements:

    - **Custom APIs**: ``"integration_method": "pdnd"``  for business-specific data access.
    - **Regulatory Compliance**: Full transparency requirements with public catalog publication.
    - **Selective Disclosure**: Limited public visibility with CI-specific approval workflows.
    - **Business Flexibility**: Tailored integration supporting diverse private sector use cases.

This approach enables both **regulatory transparency** for public administration and **business flexibility** for private sector entities while maintaining coordinated data access across the ecosystem.

AS Registry Structure
^^^^^^^^^^^^^^^^^^^^^

During registration, Authentic Sources declare their capabilities before Credential types exist in the catalog. This declaration establishes the foundation for subsequent CI registration and Credential type creation.

AS Unique Identifier Schema
"""""""""""""""""""""""""""

Each Authentic Source MUST be assigned a unique identifier that follows the HTTPS URL schema defined below. This identifier is used for referencing AS entities across the registry system and in the Digital Credentials Catalog, ensuring consistency with OpenID Federation entity identification patterns.

**AS Identifier Schema:**

.. code-block:: text

  https://{organization_domain}[/{optional_path}]

**Schema Components:**

- **organization_domain**: DNS domain controlled by the organization
- **optional_path**: Additional path component for specific services or departments

The AS identifier MUST follow these normative rules:

1. **HTTPS Protocol**: MUST use HTTPS scheme for security and trust verification
2. **Domain Ownership**: Organization MUST control the DNS domain used in the identifier
3. **Uniqueness**: Guaranteed through DNS namespace uniqueness
4. **Stability**: SHOULD remain stable over time to avoid reference breakage
5. **Resolvability**: The URL SHOULD be resolvable (though not required to serve content)

**Examples of compliant AS identifiers:**

- ``https://motorizzazione.gov.example``: Public - Ministry of Transport, Motorization Dept
- ``https://registry.anpr.example``: Public - National Registry of Resident Population
- ``https://api.bank.example/auth-source``: Private - Example Bank Financial Services

Authentic Source Registry Parameters
""""""""""""""""""""""""""""""""""""""

The Authentic Source Registry MUST contain the following parameters for each registered Authentic Source:

.. list-table:: First-level Fields of the Authentic Source Registry
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Field Name**
     - **Description**
   * - **id**
     - REQUIRED. Unique identifier of the Authentic Source Registry (e.g., ``urn:authentic-sources:it-wallet``).
   * - **version**
     - REQUIRED. The version of the Authentic Source Registry (e.g., ``1.0.0``).
   * - **last_modified**
     - REQUIRED. The timestamp indicating when the Authentic Source Registry was last updated (e.g., ``2025-03-15T12:00:00Z``).
   * - **localization**
     - REQUIRED. Localization configuration object containing:

       * **default_locale**: Default locale code (e.g., ``it``).
       * **available_locales**: Array of supported locale codes (e.g., ``["en", "it"]``).
       * **base_uri**: Base URI for localization bundle retrieval (e.g., ``https://trust-registry.eid-wallet.example.it/.well-known/l10n/authentic-sources/``).
       * **version**: Version of the localization bundle format.
   * - **authentic_sources**
     - REQUIRED. A JSON Array where each entry is a JSON Object representing an Authentic Source entity. Each object contains the parameters defined in the "Authentic Sources Parameters" table below, including entity identification, organizational information, data capabilities, and integration methods.

.. list-table:: Authentic Sources Parameters
   :class: longtable
   :widths: 25 15 60
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **entity_id**
     - string
     - REQUIRED. Unique identifier following the normative schema: ``https://{organization_domain}[/{optional_path}]``.
   * - **organization_info**
     - JSON object
     - REQUIRED. Legal entity details and organizational metadata.
   * - **organization_info.organization_name_l10n_id**
     - string
     - REQUIRED. Localization key referencing the localized organization name in the localization bundle (e.g., ``authentic_source1.name``).
   * - **organization_info.organization_type**
     - string
     - REQUIRED. Entity classification: ``"public"`` or ``"private"``.
   * - **organization_info.ipa_code**
     - string
     - REQUIRED only for Public AS. IPA registration code for government entities.
   * - **organization_info.legal_identifier**
     - string
     - REQUIRED. Legal registration identifier (Fiscal Code/VAT Number, or equivalent national identifier for foreign entities).
   * - **organization_info.homepage_uri**
     - string
     - REQUIRED. URL pointing to the organization's homepage.
   * - **organization_info.contacts**
     - String Array
     - REQUIRED. Array of contact email addresses for at least one user-support, one application, and one systems specialist.
   * - **organization_info.dpa_contact**
     - string
     - REQUIRED. An e-mail address of Authentic Source DPA.
   * - **organization_info.policy_uri**
     - string
     - REQUIRED. URL to privacy policy document.
   * - **organization_info.tos_uri**
     - string
     - OPTIONAL. URL to terms of service document.
   * - **organization_info.organization_country**
     - string
     - REQUIRED. Two-letter ISO 3166-1 alpha-2 country code of the organization.
   * - **organization_info.logo_uri**
     - string
     - OPTIONAL. URL to the organization's logo image.
   * - **organization_info.logo_uri#integrity**
     - string
     - CONDITIONAL. Cryptographic digest of the logo image resource for integrity verification. REQUIRED if ``logo_uri`` is present. Format: ``{digest_method}-{digest_value}`` (e.g., ``"sha-256-abc123..."``).
   * - **organization_info.logo_alt_text_l10n_id**
     - string
     - OPTIONAL. Alternative text for the organization's logo image.
   * - **organization_info.logo_extended_uri**
     - string
     - OPTIONAL. URL to the organization's extended logo image.
   * - **organization_info.logo_extended_uri#integrity**
     - string
     - CONDITIONAL. Cryptographic digest of the extended logo image resource for integrity verification. REQUIRED if ``logo_extended_uri`` is present. Format: ``{digest_method}-{digest_value}`` (e.g., ``"sha-256-abc123..."``).
   * - **organization_info.logo_extended_alt_text_l10n_id**
     - string
     - OPTIONAL. Alternative text for the organization's extended logo image.
   * - **data_capabilities**
     - JSON Objects Array
     - REQUIRED. Array containing data capability specifications.
   * - **data_capabilities[].dataset_id**
     - string
     - REQUIRED. The :term:`Dataset_id` within the scope of the Authentic Source, which MAY be used as a query parameter for the ``GetAttributeClaims`` service.
   * - **data_capabilities[].data_origin_l10n_id**
     - string
     - REQUIRED. Localization key referencing the human-readable name of the data origin or department providing the data (e.g., ``authentic_source1.dataset1.origin``).
   * - **data_capabilities[].intended_purposes**
     - String Array
     - REQUIRED. Business purposes served, using taxonomy purpose identifiers (e.g., ``["IDENTITY_VERIFICATION", "DRIVING_RIGHTS_VERIFICATION"]``).
   * - **data_capabilities[].available_claims**
     - String Array
     - REQUIRED. Claims available from this data capability.
   * - **data_capabilities[].available_claims.claim_name**
     - string
     - REQUIRED. It Contains the name of the claim.
   * - **data_capabilities[].available_claims.order**
     - number
     - REQUIRED. Defines the order in which the information would be shown.
   * - **data_capabilities[].available_claims.mandatory**
     - boolean
     - REQUIRED. Defines if a claim is always available or not.
   * - **data_capabilities[].integration_method**
     - string
     - REQUIRED. Authorization framework used for data access. MUST be ``"pdnd"``.
   * - **data_capabilities[].integration_endpoint**
     - string
     - OPTIONAL. Service access point (PDND endpoint).
   * - **data_capabilities[].api_specification**
     - string
     - OPTIONAL. URL to `OAS3`_ specification document for this data capability.
   * - **data_capabilities[].data_provision**
     - JSON object
     - OPTIONAL. Data provision capabilities and timing specifications.
   * - **data_capabilities[].data_provision.immediate_flow**
     - boolean
     - REQUIRED. Indicates if the Authentic Source supports immediate data provision.
   * - **data_capabilities[].data_provision.deferred_flow**
     - boolean
     - REQUIRED. Indicates if the Authentic Source supports deferred data provision.
   * - **data_capabilities[].data_provision.max_response_time_minutes**
     - integer
     - CONDITIONAL. Maximum time in minutes for the Authentic Source to respond to a deferred data provision request. REQUIRED if ``deferred_flow`` is ``true``.
   * - **data_capabilities[].data_provision.notification_methods**
     - String Array
     - CONDITIONAL. Array of notification methods supported by the Authentic Source for deferred data provision, such as ``"push"``, ``"poll"``. REQUIRED if ``deferred_flow`` is ``true``.
   * - **data_capabilities[].user_information_l10n_id**
     - string
     - OPTIONAL. Localization key referencing a Markdown-formatted string with human-readable information about the data capability relevant to the User (e.g., ``authentic_source1.dataset1.userinfo``). This string MUST be provided by the Authentic Source to the Trust Anchor during onboarding. The Markdown formatting can be plain text or a combination of text and links. For example, if the Authentic Source's database only contains data registered *after* a specific date, this information MUST be conveyed through this key.
   * - **data_capabilities[].service_documentation_uri**
     - string
     - OPTIONAL. URL pointing to the Authentic Source service documentation.
   * - **data_capabilities[].update_frequency**
     - string
     - OPTIONAL. Indicates how frequently the Authentic Source updates its data. Possible values: ``"real_time"`` (near real-time updates, typically within minutes), ``"daily"``, ``"weekly"``, ``"monthly"``, ``"on_demand"``.
   * - **data_capabilities[].logo_uri**
     - string
     - OPTIONAL. URL to the logo image related to the data.
   * - **data_capabilities[].logo_uri#integrity**
     - string
     - CONDITIONAL. Cryptographic digest of the logo image resource for integrity verification. REQUIRED if ``logo_uri`` is present. Format: ``{digest_method}-{digest_value}`` (e.g., ``"sha-256-abc123..."``).
   * - **data_capabilities[].logo_alt_text_l10n_id**
     - string
     - OPTIONAL. Alternative text for the organization's logo image.
   * - **data_capabilities[].background_color**
     - string
     - OPTIONAL. String value of the background color related to be displayed together with the data.
   * - **data_capabilities[].contacts**
     - JSON Object Array
     - OPTIONAL. Array containing customer service contacts or user support channels. Each object contains:
    
        - **type**: REQUIRED. Indicates the type of contact information and MUST be set to ``email``, ``telephone`` or ``url``.
        - **value**: REQUIRED. Contains the value of the contact information corresponding to the specified type.
        - **description**: OPTIONAL. A textual description associated with the contact information.

.. note::
  For further details on the required features and the expected outcome in terms of user experience, see the Section :ref:`functionalities:Issuance from the Wallet Instance Catalog` for the parameter `data_capabilities.user_information` and Section :ref:`functionalities:Focus on Electronic Attestations of Attributes` for the parameters `organization_info.logo_uri`, `organization_info.logo_extended_uri`, `data_capabilities.logo_uri`, `data_capabilities.background_color` and `data_capabilities.available_claims.order`.

AS Registry Example
"""""""""""""""""""

A non-normative example of AS Registry structure is given below:

.. literalinclude:: ../../examples/as-registry-example.json
  :language: JSON

.. note::
  For a better and more efficient management of the localization of the information contained in the Authentic Source Registry, an Entity consulting it SHOULD:

  - Download the basic version of the Authentic Source Registry (compact, without localizations) using the ``.well-known/authentic-sources`` endpoint.
  - Determine the User's preferred language.
  - Download only the necessary localization bundles.
  - Dynamically merge localised content with the Authentic Source Registry structure.

A non-normative example of a localization bundle output is given below:

.. code-block:: json

  {
    "authentic_source1.name": "Ministero delle infrastrutture e dei trasporti",
    "authentic_source1.dataset1.origin": "MIT -- Direzione Generale per la Motorizzazione",
    "authentic_source1.dataset1.userinfo": "###### Patente di Guida\nSono disponibili le patenti rilasciate dopo il 1° gennaio 2020. Per le patenti più vecchie, contattare l'ufficio motorizzazione locale.",
    "authentic_source2.name": "Banca Esempio SpA",
    "authentic_source2.dataset1.origin": "Esempio origine dei dati 1",
    "authentic_source2.dataset1.userinfo": "###### Informazioni sulla disponibilità dei dati\nL'accesso ai dati finanziari richiede il consenso del cliente ed è soggetto alla normativa PSD2. Le informazioni sui conti sono disponibili solo per i conti attivi.",
    "...": "..."
  }

Localization bundles MUST be available at the URI composed by appending the locale code and ``.json`` to the ``localization.base_uri`` value defined in the registry. Each locale bundle MUST be accessible following the naming pattern **{locale_code}.json**, where **{locale_code}** is replaced with the corresponding locale code from the **available_locales** array.

A non-normative example of the Italian localization URI for the bundle would be **https://trust-registry.eid-wallet.example.it/.well-known/l10n/authentic-sources/it.json**.

AS-CI Coordination
^^^^^^^^^^^^^^^^^^

Following AS registration, the AS Registry enables Credential Issuers to discover suitable AS entities and request integration approval. This coordination process is detailed in :ref:`entity-onboarding:Authentic Source to Credential Issuer Authorization Process`.

Federation Registry
-------------------

The **Federation Registry** provides the cryptographic trust infrastructure for all IT-Wallet ecosystem participants. The Federation Registry maintains the authoritative list of trusted entities and their operational status using federation-specific endpoints as defined in :ref:`trust-infrastructure:Federation API endpoints`.

Registry Integration Role
^^^^^^^^^^^^^^^^^^^^^^^^^

Within the IT-Wallet System Register architecture, the Federation Registry serves as the **trust validation layer** for:

1. **Entity Authentication**: Validates the cryptographic identity of all participants before registry operations
2. **Trust Chain Verification**: Provides the cryptographic foundation for Credential Issuers, Relying Parties, and Wallet Providers entity validation
3. **Compliance Verification**: Maintains Trust Marks that attest regulatory compliance and operational status

Federation Registry Access
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Federation Registry operations are accessed through the Trust Anchor's federation endpoints as detailed in :ref:`trust-infrastructure:Federation API endpoints`. The registry discovery architecture provides federation endpoint information via the registry discovery endpoint described in `Registry Discovery Endpoint`_.

.. note::
   Federation endpoints are available through both the registry discovery mechanism (for unified registry access) and the Trust Anchor's Entity Configuration at ``.well-known/openid-federation`` (for federation-specific operations). Both sources provide the same endpoint URLs but serve different discovery patterns: registry discovery for initial ecosystem orientation, Entity Configuration for standard OpenID Federation 1.0 compliance.

   For complete technical specifications of federation protocols, entity configurations, trust evaluation mechanisms, and trust chain validation, see :ref:`trust-infrastructure:The Infrastructure of Trust`.

Digital Credentials Catalog
-----------------------------

The Digital Credentials Catalog is the registry of all available Digital Credentials recognized within the IT-Wallet ecosystem. It is published by the Trust Anchor and publicly available by all Entities through a specialized Federation endpoint. It acts as a single reference point for all actors involved in the process of issuing, verifying and using Digital Credentials.

The Digital Credential Catalog aims to:

  1. Facilitate Digital Credential discovery for Users.
  2. Standardize the technical and functional description of Digital Credentials.
  3. Enable interoperability between different Issuers and Relying Parties.
  4. Simplify the integration process for Wallet Providers and Relying Parties.
  5. Ensure trust in the ecosystem through verifiable and trustworthy information.
  6. Provide transparency on the ecosystem of available Digital Credentials.

The main Entities involved in the Digital Credential Catalog are:

  - **Trust Anchor**: It manages and maintains the Digital Credential Catalog, guaranteeing its authenticity and integrity.
  - **Supervisory Body**: It interacts with the Trust Anchor and the Digital Credential Catalog to monitor the registration phase ensuring security and privacy according to national/European regulations, keeping all the information reliable and updated.
  - **Digital Credential Issuers**: The entities authorized to issue Digital Credentials, registering them in the Catalog.
  - **Relying Parties**: They use the Digital Credential Catalog to gather all the information needed about the Digital Credentials they intend to request during the presentation phase.
  - **Wallet Providers**: They access the Digital Credential Catalog to identify the available Digital Credentials and to retrieve all necessary information for integrating them into their Wallet Solutions.
  - **Users**: The Users who indirectly use the Digital Credentials Catalog through their Wallet Instances to discover and request Digital Credentials.
  - **Authentic Sources**: The Entities that hold the original data that is attested in the Digital Credentials. They provide support to Issuers in registering the Digital Credentials in the Catalog.

.. _fig_catalog:
.. plantuml:: plantuml/credential-catalog-entities.puml
    :width: 99%
    :alt: The figure illustrates the Digital Credential Entities.
    :caption: `Entity-Relationship diagram of Digital Credential Catalog. <https://www.plantuml.com/plantuml/svg/ZLJ1Rkis4BpxAxP6WQP00X-QtjeWgPEsFXGmuXGz6ZIvbeb8fCfTEbM__YrDELAUb6ST34khuSnmESjxOXKuLYKysiAoAc4PqA1ZcnwL57mH4Pwam1Pfzfrrkem6uPVbxM9vkrtwglPEy7UpsG_mY7lh43RhvzNBqwO7vbWh4tvQQ5zLtjsDVDbxnpVg3SbNUFFpGcDWkxTQCKv06p6wKpG5MdhzEW4M2GDDyUcBAJ1XEsAO07p5PgAx2J1hjbe5Cm69_-c3SWLkLSbJ-etqohwUW7nJPOaNAHVM4LkER5CuPhFtL5tfSmIlOJvCA7KHdGlW6GjB79hql1H4471eQ-3t85v07PKjrQv46A6JXTzJ7IpZh_DpfkO_Yg4r1lBkAlLTkF-MlvE6PVi_EeAtWmTZINivP53EYEg_4OalQIG-uU-soo4IFpXzy4dd9Rr1VarwwVUNSgf0EgbKoZgM7m4Vy9i3t1ULY8dcfY76wefYBT6qv4FpcpUD26ow2gJIITGxopxGkPig7HJK1qK8w2W6wmeWrFB0pScQQ1sLRlgwlP7kz2rHn42Zfmkh_34vU8WiJP1k6y3sBf9DAuP4SF4isq7eP0EMZNXUgv2OKdHo0ThAF9_ogQ_l4GJsK2Wf1R1kxqELsw1sFZBeSUN-O7NoUIhMmH-joRl_vrI1jjJkMMia6dgmZh48Yh4lcgeUCl471xdKQIlfP5gZDpu64KX2vnAqjQJ-foyD-22DTTBOD0sWc54uZ6XTx7Wtq6c0fBqVijrjg8lqTPVd7A6uAoqTiflVHQMD7JfJUm4Ahz0E4_nnXbQEPQ5c6LBBX_4rVJkVXZtuT1gPe8jjVs6-VZ2CzGQiQvSE-tyc6pSxo6fVyezFuZXc8TCDizVnTP7pO4_BzatlmjG3hdmV3XZJw12qaLuvOkKqGfq11dPDNhvzR0dw3bREs82Qo-RzHgN-bKfVsRYNECIg_080>`_

The following table summarizes the main information that MUST be provided by the Digital Credential Catalog:

.. list-table:: Digital Credential Catalog - Main information
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Information related to**
     - **Description**
   * - Digital Credential Metadata
     - Essential identifying information and characteristics of the Digital Credential, including:

       - **Credential Unique identifier**: A unique identifier string of each Digital Credential.
       - **User authentication methods**: User authentication mechanisms used to request the Digital Credential, if required by Issuers or Authentic Sources.
       - **Minimum Level of Assurance**: The minimum Level of Assurance required for the Digital Credential's reliability. It MUST take into account the Level of Assurance of User authentication, when applicable, and Wallet Instance.
   * - Digital Credential Issuers
     - Details about the organization authorized to issue the Digital Credential, such as:

       - **Issuer identifiers**: Unique identifier for the Digital Credential issuer.
       - **Issuer type**: Classification as PID, (Q)EAA, or Pub-EAA Provider.
       - **Additional information**: Organizational details including name, code, and contact information.
   * - Authentic Sources
     - Information about the authoritative data source.
   * - Technical Specification
     - Technical details, including:

       - **Digital Credential schemes**: Framework and structure specifications.
       - **Digital Credential formats**: Data format and encoding standards.
       - **Authentication policy**: Methods and requirements for verification.
   * - Terms of Use
     - Conditions and limitations for Digital Credential usage, such as:

       - **Credential validity**: Time period during which the Digital Credential is valid and, when applicable, mechanisms and technical details for invalidating Digital Credentials (revocation/suspension methods).
       - **Restriction policy**: If applicable, rules governing the Digital Credential's use and limitations according to national regulations. It is used, for example, to specify if only specific legal type Entities, for example Pub-EAA Provider and public Wallet Solutions, are allowed to issue and obtain the Digital Credential.
       - **Pricing policy**: Information related to pricing models of Digital Credential, such as `free`, `issuance_based`, `verification_based`.
       - **Digital Credential purposes**: Information related to the allowed purposes for which the Digital Credential can be used. Each Digital Credential type can be used for multiple purposes.

The Trust Anchor MUST publish and keep up to date all the information at the Digital Credential Catalog `.well-known` endpoint ensuring data reliability, authenticity and integrity. In particular, the Digital Credential Catalog MUST be available through the ``.well-known/credential-catalog`` endpoint. It MUST support ``application/jose`` as content-type.

Below a non-normative example is given.

.. code-block:: http

    GET /.well-known/credential-catalog HTTP/1.1
    Host: trust-anchor.eid-wallet.example.it
    Accept: application/jose

    HTTP/1.1 200 OK
    Content-Type: application/jose

    eyJhbGciOiJSUzI1NiIsImtpZCI6ImV4YW1w...

In the section :ref:`registry:Digital Credentials Catalog Structure` an example of Digital Credentials Catalog is given as decoded in JSON.

Digital Credentials Hierarchy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Digital Credentials recognized within the IT-Wallet ecosystem are classified and standardized according to the following multi-level hierarchical model designed to improve semantic clarity, credential discovery, and compatibility with both credential-specific and claim-based verification workflows.

The hierarchy is defined as follows:

**Domain**

A **Domain** represents a high-level thematic area grouping Credential families that relate to the same broad context (e.g., Identity, Health, Education, Mobility).
Domains provide a top-level organizational layer.

**Credential Class**

A **Credential Class** represents a family of Credentials sharing similar nature, function, or structure (e.g., Identification Documents, Civil Status Certificates).

Each Class SHOULD define:

- a stable Class identifier (URI),
- the expected semantics of the Credential Family.

Classes enable Relying Parties and Wallet Solutions to request or match Credentials based on their type category.

**Credential Type**

A **Credential Type** represents a specific Credential within a Class (e.g. Digital Travel Credential, Birth Certificate, Mobile Driving License).
Each Credential Type MUST include:

- a unique identifier,
- the Credential Issuer identifier,
- the set of Attributes that may be included in presentations.

Credential Types enable precise targeting for compliance-driven or regulation-mandated verification flows.

**Purpose (Verification Intent)**

A **Purpose (Verification Intent)** describes *why* a credential may be requested by a Relying Party (e.g., Identity Verification, Age Verification, Eligibility for specific services).
Purposes MUST describe **verification outcomes**.
Each Credential Type MUST declare its Domain, Class, and supported Purposes.

The following tables provide non-exhaustive examples illustrating the relationships between Domains, Credential Classes, and Credential Types, followed by their mapping to verification Purposes.
Additional Domains, Classes, specific Credentials, and verification Purposes **MAY** be added over time as the IT-Wallet ecosystem evolves.

.. list-table:: Digital Credential Taxonomy: Hierarchy and Classification
   :class: longtable
   :header-rows: 1
   :widths: 15 25 30 30

   * - **Domain**
     - **Description**
     - **Credential Class**
     - **Credential Type**

   * - *IDENTITY*
     - Credentials that establish or confirm a person's legal identity and personal, civil or legal status.
     -
       * Identification Documents
       * Civil Registry and Personal Status Certificates
       * Economic and Legal Status
     -
       * Digital Travel Credential
       * Mobile Driving License (Italy only)
       * Tax Code / Health Insurance Card
       * Age Certification
       * Birth Certificate
       * Residence Certificate
       * Family Status Certificate
       * Marriage Certificate
       * Citizenship Certificate
       * ISEE (Equivalent Economic Situation Indicator)
       * Residence Permit
       * Certificate of Pending Charges
       * Criminal Record Certificate

   * - *HOME AND FAMILY*
     - Credentials that attest household composition, residence, and housing-related legal or fiscal relationships.
     -
       * Property and Cadastral Documents
       * Family Documents
       * Local Tax Documents
     -
       * Deed of Sale
       * Cadastral Survey
       * Cadastral Floor Plan
       * Cadastral Certificate
       * Children's Tax Code / Health Card
       * Birth Certificate
       * Family Status Certificate
       * IMU (Property Tax)
       * TARI (Waste Tax)

   * - *EDUCATION*
     - Credentials that attest educational achievements, academic qualifications, and professional training.
     -
       * Educational Qualifications
       * Professional Certifications
     -
       * Lower Secondary School Diploma
       * Upper Secondary School Diploma
       * Bachelor's Degree
       * Master's Degree
       * University Master
       * PhD
       * Professional Licenses (e.g. architect, lawyer)
       * Vocational Training Certificates
       * Language Certifications (e.g. IELTS)
       * Academic Qualifications (e.g. Europass)

   * - *HEALTH*
     - Credentials related to healthcare coverage, medical status, and health-related certifications.
     -
       * Certifications and Eligibility
       * Medical Records
     -
       * Health Insurance Card (TEAM)
       * European Health Card (CED)
       * Disability Certificate
       * Vaccination Certificate
       * Sports Fitness Certificate
       * Work Fitness Certificate
       * Medical Prescriptions
       * Digital Medical Report

   * - *FINANCIAL*
     - Credentials related to payment instruments, financial authorizations, and proof of payments.
     -
       * Payment Instruments
       * Payment Credentials and Authorisations
       * Public Payments and Fees
       * Recurring Payments and Subscriptions
     -
       * Digital Payment Card (debit / credit / prepaid)
       * Virtual Card
       * Bank Account (IBAN)
       * Strong Customer Authentication (SCA) Credential
       * Payment Receipt
       * Digital Stamp Duty (Bollo digitale)
       * Tax and Fee Payment Certificate
       * Subscription Mandate
       * Recurring Payment Credential

   * - *CULTURE AND LEISURE*
     - Credentials that attest membership, affiliation, or participation in cultural or recreational programs.
     -
       * Cultural Cards and Benefits
       * Membership and Loyalty Programs
     -
       * Culture Card
       * Annual Museum Passes
       * Cinema Card
       * Museum Card
       * Association Membership Cards
       * Library Card
       * City Pass

   * - *EMPLOYMENT*
     - Credentials that attest employment relationships, professional status, and contribution records.
     -
       * Employment Documents
       * Employment Status
       * Employment Affiliation
     -
       * Digital Employment Contract
       * Curriculum Vitae (CV)
       * Residence Permit
       * Employment Status Certificate
       * INPS Contribution Record
       * Physical Access Badge

   * - *MOBILITY AND TRAVEL*
     - Credentials that attest mobility rights, vehicle-related status, and travel-related entitlements.
     -
       * Licenses and Authorizations
       * Vehicle Documents
       * Transport Subscriptions
       * Travel Documents
       * Travel Insurance
       * Bookings
       * Discounts and Benefits
     -
       * Mobile Driving License
       * Boating License
       * Vehicle Registration Certificate
       * Digital RCA Insurance
       * Vehicle Inspection Certificate
       * Green Card / International Insurance
       * Public Transport Pass
       * Road Charging Subscription
       * Digital Travel Credential
       * Travel Tickets (air, train, etc.)
       * Travel Insurance Policy
       * Hotel Reservation
       * Discount Cards
       * Tourist Benefits

   * - *BONUSES*
     - Credentials that attest entitlement to economic benefits, incentives, or vouchers.
     -
       * Economic Benefits and Allowances
       * Incentives and Vouchers
       * Health and Wellbeing Bonuses
     -
       * Family Allowance Credential
       * Unemployment Benefit Credential
       * Digital Voucher
       * Purchase Incentive Credential
       * Cashback Eligibility Credential
       * Healthcare Bonus Credential
       * Mental Health Support Voucher
       * Sports and Physical Activity Bonus

.. list-table:: Table 2: Mapping between Credential Classes and Purposes
   :class: longtable
   :header-rows: 1
   :widths: 40 60

   * - **Credential Class**
     - **Supported Purposes**

   * - Identification Documents
     -
       * Identity verification
       * Age verification
       * Person identification
   * - Civil Registry and Personal Status Certificates
     -
       * Civil status verification
       * Right of residence
       * Household composition verification
   * - Economic and Legal Status
     -
       * Eligibility for services or benefits
       * Legal status verification
       * Criminal record check
   * - Property and Cadastral Documents
     -
       * Residence and household verification
       * Property ownership verification
       * Real estate compliance
   * - Family Documents
     -
       * Household composition verification
       * Eligibility for family-based social services
   * - Local Tax Documents
     -
       * Compliance with local tax obligations
       * Verification of property tax status
   * - Educational Qualifications
     -
       * Qualification and degree verification
       * Eligibility for education pathways
   * - Professional Certifications
     -
       * Professional license verification
       * Skills assessment for work
   * - Certifications and Eligibility
     -
       * Verification of vaccination status
       * Verification of fitness status
       * Access to health-restricted areas
   * - Medical Records
     -
       * Access to healthcare services
       * Sharing of medical records
       * Medical history validation
   * - Payment Instruments
     -
       * Payment authorization
       * Payment execution
       * Proof of payment
   * - Payment Credentials and Authorisations
     -
       * Management of financial authorizations
       * Strong Customer Authentication (SCA)
   * - Public Payments and Fees
     -
       * Proof of tax payment
       * Proof of fee payment
       * Digital stamp duty validation
   * - Recurring Payments and Subscriptions
     -
       * Management of recurring payments
       * Subscription mandate verification
   * - Cultural Cards and Benefits
     -
       * Access to cultural services
       * Access to leisure services
       * Application of member discounts
   * - Membership and Loyalty Programs
     -
       * Verification of affiliation
       * Verification of participation
       * Use of loyalty benefits
   * - Employment Documents
     -
       * Employment status verification
       * Professional profile validation
   * - Employment Status
     -
       * Verification of contribution records
       * Eligibility for employment-related benefits
   * - Licenses and Authorizations
     -
       * Driving rights verification
       * Navigation rights verification
       * Law enforcement controls
   * - Vehicle Documents
     -
       * Vehicle registration verification
       * Vehicle inspection verification
       * Insurance status check
   * - Transport Subscriptions
     -
       * Access to transport services
       * Public transport pass verification
   * - Travel Documents
     -
       * Right to travel or circulate
       * Cross-border mobility identity check
   * - Travel Insurance and Bookings
     -
       * Verification of travel insurance coverage
       * Accommodation reservation check
       * Transport reservation check
   * - Discounts and Benefits
     -
       * Application of member discounts
       * Access to tourist benefits
   * - Economic Benefits and Allowances
     -
       * Eligibility verification for family benefits
       * Eligibility verification for unemployment benefits
       * Allocation of economic support
   * - Incentives and Vouchers
     -
       * Use of digital vouchers
       * Use of purchase incentives
       * Cashback eligibility verification
   * - Health and Wellbeing Bonuses
     -
       * Access to healthcare bonuses
       * Use of mental health vouchers
       * Use of sports vouchers
   * - Employment Affiliation
     -
       * Access permit verification

Each Credential MUST specify domains, classes and purposes to enable both **Credential-Specific Scenarios** and **Credential-Agnostic Scenarios** according to Relying Party's requirements and presentation request patterns, as defined in the mapping tables above.

  1. **Credential-Specific Scenarios** (Primary for Government/Regulated Sectors): RPs request specific Credential types for compliance and audit requirements, including for example:

    - **Government Services**: ``"credential_type":"pid"`` for PID-specific identity verification or ``"credential_type":"eid"`` for IT-Wallet ID-specific identity verification.
    - **Police Controls**: ``"credential_type":"mDL"`` for driving license verification.
    - **Banking KYC**: Specific credential types mandated by financial regulations.
    - **Healthcare Services**: ``"credential_type":"european_disability_card"`` for EU-compliant disability benefit access.

  2. **Credential-Agnostic Scenarios** (Typical for Private Business): RPs request specific claims regardless of Credential source for operational efficiency, such as:

    - **E-commerce Delivery**: Any credential, among those to which he is authorized to access, containing ``given_name``, ``family_name``, ``address`` for shipping.
    - **Subscriptions**: Any credential, among those to which he is authorized to access, with ``given_name``, ``email`` for personalization.
    - **Service Personalization**: Business applications requiring basic personal data without strong source requirements.

This approach allows:

  - **Policy-based authorization** by using **Domain / Class / Credential Type / Purpose** mappings.
  - **Flexible RP registration** supporting both government compliance needs and business operational requirements.

Digital Credentials Catalog Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Digital Credentials Catalog contents is secured in a JWS that contains the following JOSE header parameters:

.. _table_catalog_parameters:
.. list-table::
   :class: longtable
   :header-rows: 1
   :widths: 25 50 25

   * - **JOSE header**
     - **Description**
     - **Reference**
   * - **typ**
     - REQUIRED. It MUST be set to ``JOSE``.
     - [:rfc:`7515` Section 4.1.9].
   * - **alg**
     - REQUIRED. A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms in Section :ref:`algorithms:Cryptographic Algorithms` and MUST NOT be set to ``none`` or with a symmetric algorithm (MAC) identifier.
     - [:rfc:`7515` Section 4.1.1].
   * - **kid**
     - REQUIRED. Unique identifier of the public key.
     - [:rfc:`7515` Section 4.1.4].
   * - **x5c**
     - OPTIONAL. Contains the X.509 public key Certificate or Certificate chain [:rfc:`5280`] corresponding to the key used to digitally sign the JWS. When the header parameter `kid` value is present, it MUST refer to the same leaf's cryptographic public key used with the X.509 Certificate.
     - [:rfc:`7515` Section 4.1.6.].
   * - **cty**
     - REQUIRED. It MUST be set to ``application/json``.
     - [:rfc:`7515` Section 4.1.6.].

The JWS payload contains the following parameters:

.. list-table:: First-level Fields of the Digital Credentials Catalog
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - **Field Name**
     - **Description**
   * - **id**
     - REQUIRED. Unique identifier of the Digital Credentials Catalog (e.g., ``urn:credential-catalog:it-wallet``).
   * - **version**
     - REQUIRED. Version of the Digital Credential Catalog format.
   * - **last_modified**
     - REQUIRED. Timestamp of the last modification to the Digital Credential Catalog (e.g., ``2025-03-15T12:00:00Z``).
   * - **iss**
     - REQUIRED. Issuer identifier of the Digital Credential Catalog.
   * - **localization**
     - REQUIRED. Localization configuration object containing:

       * **default_locale**: Default locale code (e.g., ``it``).
       * **available_locales**: Array of supported locale codes (e.g., ``["en", "it"]``).
       * **base_uri**: Base URI for localization bundle retrieval (e.g., ``https://trust-registry.eid-wallet.example.it/.well-known/l10n/credential-catalog/``).
       * **version**: Version of the localization bundle format.
   * - **credentials**
     - REQUIRED. Array containing Digital Credential definitions.

Each element of the ``credentials`` array contains at least the following information:

.. _table_catalog_parameters_first_level:
.. list-table:: First-level Fields of Each Credential Entry
  :class: longtable
  :header-rows: 1
  :widths: 30 70

  * - **Field Name**
    - **Description**
  * - **version**
    - REQUIRED. Version of the Digital Credential definition.
  * - **credential_type**
    - REQUIRED. Unique identifier of the Digital Credential type. For PID it MUST be ``pid`` and for IT-Wallet ID MUST be ``eid``.
  * - **credential_name_l10n_id**
    - REQUIRED. Localization key referencing the human-readable name of the Digital Credential in the localization bundle (e.g., ``mDL.name``).
  * - **legal_type**
    - REQUIRED. Legal classification of the Credential (e.g., ``pub-eaa``, ``qeaa``, ``eaa``).
  * - **restriction_policy**
    - OPTIONAL. Legal restrictions on Wallet Solutions and/or Credential Issuers allowed to request/issue the Digital Credential.

      * **allowed_wallet_ids**: List of allowed Wallet Solutions identifiers.
      * **allowed_issuer_ids**: List of allowed Credential Issuers identifiers. If present, it represents a whitelist of Credential Issuers that may be added by the Trust Anchor in the **issuers** field of the corresponding Digital Credential.
      * **presentation_flows**: Type of presentation flows supported; remote and/or proximity flow.
  * - **pricing_policy**
    - OPTIONAL. Information about Digital Credential pricing, including:

      * **models**: REQUIRED. Array of pricing models applicable to the Digital Credential, each containing

        - **pricing_type**: Type of pricing model, such as ``issuance_based``, ``verification_based``, ``subscription_based``, ``other``.
        - **price**: Cost associated with the model.
        - **currency**: Currency of the price.

      * **pricing_model_uri**: URI to the detailed pricing model documentation.
  * - **validity_info**
    - Information about Digital Credential validity, including at least:

      * **max_validity_days**: Maximum validity period in days.
      * **status_methods**: Supported status verification methods (e.g. ``status_list``).
      * **allowed_states**: Array of objects representing allowed Digital Credential states. Each object contains a hex status code (e.g., ``0x00`` for ``VALID``, ``0x01`` for ``INVALID``, ``0x02`` for ``SUSPENDED``, ``0x03`` for ``UPDATE``, ``0x0F`` for ``ATTRIBUTE_UPDATE``), a ``title_l10n_id`` localization key, and a ``description_l10n_id`` localization key for UI display.
      * **administrative_expiration_user_info**: OPTIONAL. Object containing ``title_l10n_id`` and ``description_l10n_id`` keys for displaying administrative expiration information to the User.
  * - **authentication**
    - REQUIRED. Digital Credential authentication requirements.

      * **user_auth_required**: REQUIRED. Flag indicating if User authentication is required during the issuance of the Digital Credential.
      * **min_loa**: REQUIRED. Minimum Level of Assurance required for Digital Credential authentication. It MUST include the Level of Assurance of the User authentication and the Wallet Instance requesting the Digital Credential.
      * **supported_schemes**: REQUIRED if ``user_auth_required`` is ``true``. Supported digital identity authentication schemes (e.g., ``["it_wallet"]``).
  * - **domains**
    - REQUIRED. Array of domain IDs to which Digital Credential belongs (e.g., ``"IDENTITY"``, ``"MOBILITY_TRAVEL"``).
  * - **classes**
    - REQUIRED. Array of class IDs to which Digital Credential belongs (e.g., ``"IDENTIFICATION_DOCUMENTS"``, ``"LICENSES_AUTHORIZATIONS"``).
  * - **purposes**
    - REQUIRED. Array of usage purpose IDs for which the Digital Credential can be used, defining specific usage contexts and required claims for each purpose (e.g., ``"IDENTITY_VERIFICATION"``, ``"AGE_VERIFICATION"``, ``"DRIVING_RIGHTS_VERIFICATION"``).
  * - **issuers**
    - REQUIRED. Array of relevant information about authorized Credential Issuers, including administrative and technical data such as Organization name, a reference to the API specification document and supported issuance mechanisms. Each array element contains:

       * **entity_id**: REQUIRED. String. Unique identifier of the Credential Issuer. It MUST match with the value contained in the ``iss`` parameter of the Credential Issuer Entity Configuration.
       * **organization_name_l10n_id**: REQUIRED. String. Localization key referencing the localized organization name in the localization bundle (e.g., ``issuer1.name``).
       * **organization_code**: REQUIRED. String. Credential Issuer IPA code for government entities or VAT number for private entities.
       * **organization_country**: REQUIRED. String. Two-letter ISO 3166-1 alpha-2 country code of the organization.
       * **contacts**: REQUIRED. String. Array of contact email addresses for at least one user-support, one application, and one systems specialist.
       * **legal_type**: REQUIRED. String. Legal classification of the Credential Issuer (e.g., pub-eaa, qeaa, eaa).
       * **homepage_uri**: REQUIRED. String. URL pointing to the organization's homepage.
       * **logo_uri**: OPTIONAL. String. URL to the organization's logo image.
       * **policy_uri**: REQUIRED. String. URL to privacy policy document.
       * **tos_uri**: OPTIONAL. String. URL to terms of service document.
       * **service_documentation_uri**: OPTIONAL. String. URL pointing to the Credential Issuer service documentation.
       * **issuance_flows**: REQUIRED. Object. It contains the following parameters:

          * **deferred_flow**: REQUIRED. Boolean. Indicates if the deferred issuance is supported.
          * **immediate_flows**: REQUIRED. Boolean. Indicates if the immediate issuance is supported.
          * **wallet_initiated**: REQUIRED. Boolean. Indicates if the Wallet-Initiated flow is supported.
          * **issuer_initiated**: REQUIRED. Boolean. Indicates if the Issuer-Initiated flow issuance is supported (Third Party Initiated Flow).
          * **max_deferred_issuance_time_minutes**: CONDITIONAL. Integer. Maximum time in minutes for the availability of the issuance of the Credential. REQUIRED if ``deferred_flow`` is ``true``.
          * **notification_methods**: CONDITIONAL. String Array. Contains the notification methods supported by the Credential issuer for the deferred issuance, such as ``"push"``, ``"poll"``. REQUIRED if ``deferred_flow`` is ``true``.

  * - **authentic_sources**
    - CONDITIONAL. It is REQUIRED only if ``parent_credentials`` is absent. Array of Authentic Source JSON objects referencing authorized Authentic Sources. Each object MUST contain the AS entity identifier and the specific data capability identifier:

      * **id**: String identifier referencing the Authentic Source entity_id as registered in the :ref:`registry:Authentic Source Registry`.
      * **dataset_id**: String identifier of the specific data capability/dataset used by the Issuer from the AS.
  * - **parent_credentials**
    - CONDITIONAL. It is REQUIRED only if ``authentic_sources`` is absent. Array of ``credential_type`` identifier corresponding to Credentials designated as data sources. Each element identifies a Credential that acts as an Authentic Source during the Digital Credential Issuance process.

.. note::
  The union of ``credential_type`` and ``version`` MUST be unique in the Credential Catalog.

The corresponding example of Digital Credentials Catalog as decoded in JSON for both header and payload is the following:

.. literalinclude:: ../../examples/catalog-example-header.json
  :language: JSON

.. literalinclude:: ../../examples/catalog-example-payload.json
  :language: JSON

.. note::
  For a better and more efficient management of the localization of the information contained in the Digital Credentials Catalog, an Entity consulting it SHOULD:

  - Download the basic version of the Digital Credentials Catalog (compact, without localizations) using the ``.well-known/credential-catalog`` endpoint.
  - Determine the User's preferred language.
  - Download only the necessary localization bundles.
  - Dynamically merge localised content with the Digital Credentials Catalog structure.

A non-normative example of a localization bundle output is given below:

.. code-block:: json

  {
    "mDL.name": "Patente di Guida",
    "mDL.issuer1.name": "Esempio di Credential Issuer",
    "...": "..."
  }

Localization bundles MUST be available at the URI composed by appending the locale code and ``.json`` to the ``localization.base_uri`` value defined in the catalog. Each locale bundle MUST be accessible following the naming pattern **{locale_code}.json**, where **{locale_code}** is replaced with the corresponding locale code from the **available_locales** array.

A non-normative example of the Italian localization URI for the bundle would be **https://trust-registry.eid-wallet.example.it/.well-known/l10n/credential-catalog/it.json**.

Decentralization of Display and Claim Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The canonical source for display characteristics and claim structure is determined by the **Credential Issuer's Metadata (Entity Configuration)**.

The overall logic for presenting a Credential is:

1. The Wallet/Relying Party retrieves the lightweight **Digital Credentials Catalog** to discover the available `credential_type` and the `entity_id` of their Credential Issuers.
2. It retrieves the full **Credential Issuer Metadata** (Entity Configuration) from the discovered `entity_id`.
3. The Credential Issuer Metadata MUST contain the full display characteristics (logos, colors) and the detailed schema information (via links to the appropriate Type Metadata or directly in the configuration). The Issuer builds this metadata based on the suggestions provided by the Authentic Source (via the AS Registry) and the standard schema specifications (via the Schema Registry).

Taxonomy
--------

The **Taxonomy** provides the semantic foundation for Digital Credential interoperability by maintaining the authoritative vocabulary for organizing Credentials within the IT-Wallet ecosystem. The taxonomy is neutral with respect to the Credential format.

The Taxonomy provides, in a single resource, the hierarchical classification system organizing Domains, Classes and Purposes that can be applied to Credential Types, supporting authorization policy evaluation and ecosystem-wide standardization.

**Taxonomy Objectives:**

1. **Semantic Foundation**: Establish standardized vocabulary for domains and purposes across the ecosystem
2. **Policy Framework**: Enable structured authorization decisions based on hierarchical classification
3. **Interoperability**: Ensure consistent interpretation of credential classifications
4. **Extensibility**: Support evolution of the ecosystem with new Domains, Classes, Credential Types and Purposes
5. **Cross-Border Compliance**: Align with EU regulatory requirements and international standards

**Taxonomy Structure:**

The taxonomy maintains a four level hierarchical structure:

- **Domains**: Top-level classification representing broad functional areas (e.g., IDENTITY, HEALTH, FINANCIAL)
- **Class (Credential Family)**: Family of Credentials sharing similar function, structure, or legal meaning (e.g., Identification Documents, Civil Status Certificates, Professional Licenses, Access)
- **Credential Type**: Specific Credential definition issued by an authority (e.g., Digital Travel Credential, Birth Certificate, Mobile Driving License).
- **Purpose (Verification Intent)**: Verification objectives that a Credential can satisfy (e.g., Identity Verification, Age Verification, Eligibility for specific services, Access permit verification).

.. note::
  Credential Type is a concept defined at the Digital Credentials Catalog level, not within the Taxonomy. The Taxonomy provides the classification vocabulary (Domains, Classes, Purposes) that Credential Types in the Catalog reference.

**Localization Support:**

The taxonomy supports multilingual environments through the ``_l10n_id`` suffix pattern, enabling efficient localization management for user interfaces and cross-border implementations.

**Taxonomy Usage:**

- **Claims Registry**: Individual claims catalog
- **AS Registry**: Authentic Sources declare capabilities using taxonomy classifications
- **Digital Credentials Catalog**: Credential Types specify Domains, Classes and Purposes
- **Authorization Policies**: Policy evaluation leverages taxonomy structure for access control decisions

The Taxonomy is accessible through the dedicated taxonomy endpoint as defined in the registry discovery mechanism and is maintained by the Supervisory Body to ensure regulatory compliance and semantic consistency.

**Taxonomy JSON Structure:**

.. list-table:: First-level Fields of the Taxonomy
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Field Name**
     - **Description**
   * - **id**
     - REQUIRED. Unique identifier of the Taxonomy (e.g., ``urn:taxonomy:it-wallet``).
   * - **version**
     - REQUIRED. The version of the Taxonomy (e.g., ``1.0.0``).
   * - **last_modified**
     - REQUIRED. The timestamp indicating when the Taxonomy was last updated (e.g., ``2026-03-11T00:00:00Z``).
   * - **name_l10n_id**
     - REQUIRED. Localization key referencing the human-readable name of the Taxonomy (e.g., ``taxonomy.name``).
   * - **description_l10n_id**
     - REQUIRED. Localization key referencing the human-readable description of the Taxonomy (e.g., ``taxonomy.description``).
   * - **localization**
     - REQUIRED. Localization configuration object containing:

       * **default_locale**: Default locale code (e.g., ``it``).
       * **available_locales**: Array of supported locale codes (e.g., ``["en", "it"]``).
       * **base_uri**: Base URI for localization bundle retrieval (e.g., ``https://trust-registry.eid-wallet.example.it/.well-known/l10n/taxonomy/``).
       * **version**: Version of the localization bundle format.
   * - **domains**
     - REQUIRED. Array of Domain objects, each containing:

       * **id**: Unique Domain identifier in SCREAMING_SNAKE_CASE (e.g., ``IDENTITY``).
       * **name_l10n_id**: Localization key for the domain name (e.g., ``domain.identity.name``).
       * **description_l10n_id**: Localization key for the domain description (e.g., ``domain.identity.description``).
       * **classes**: Array of Class objects. Each class contains ``id``, ``name_l10n_id``, and ``supported_purposes`` (array of purpose ID strings).
   * - **purposes**
     - REQUIRED. Flat array of all Purpose objects defined across the taxonomy, each containing:

       * **id**: Unique Purpose identifier in SCREAMING_SNAKE_CASE (e.g., ``IDENTITY_VERIFICATION``, ``ACCESS_PERMIT``).
       * **name_l10n_id**: Localization key for the purpose name (e.g., ``purpose.identity_verification.name``).

A non-normative example of Taxonomy structure is given below:

.. literalinclude:: ../../examples/taxonomy-example.json
  :language: JSON

.. note::
  For a better and more efficient management of the localization of the Taxonomy, an Entity consulting it SHOULD:

  - Download the basic version of the Taxonomy (compact, without localizations) using the ``.well-known/taxonomy`` endpoint.
  - Determine the User's preferred language.
  - Download only the necessary localization bundles.
  - Dynamically merge localised content with the Taxonomy structure.

A non-normative example of a localization bundle output is given below:

.. code-block:: json

  {
    "taxonomy.name": "IT-Wallet Taxonomy",
    "taxonomy.description": "Hierarchical classification system for Digital Credentials in the IT-Wallet ecosystem",
    "domain.identity.name": "Identity",
    "domain.identity.description": "Credentials that establish or confirm a person's legal identity and personal, civil or legal status.",
    "class.identification_documents.name": "Identification Documents",
    "purpose.identity_verification.name": "Identity verification",
    "domain.authentication.name": "Authentication",
    "domain.authentication.description": "Credentials that attest authorisation to access restricted physical or digital spaces, services or resources.",
    "class.access.name": "Access",
    "purpose.access_permit.name": "Access permit verification",
    "...": "..."
  }

Localization bundles MUST be available at the URI composed by appending the locale code and ``.json`` to the ``localization.base_uri`` value defined in the taxonomy. Each locale bundle MUST be accessible following the naming pattern **{locale_code}.json**, where **{locale_code}** is replaced with the corresponding locale code from the **available_locales** array.

A non-normative example of the Italian localization URI for the bundle would be **https://trust-registry.eid-wallet.example.it/.well-known/l10n/taxonomy/it.json**.

Schema Registry
-----------------

The **Schema Registry** is the authoritative inventory of all known and accepted **Credential Schemas** (JSON Schema for SD-JWT, CBOR Schema for mDOC) within the IT-Wallet ecosystem. It is managed by the Trust Anchor and provides a single, verifiable source for retrieving the technical specifications required for parsing, validating, and displaying Digital Credentials.

**Schema Registry Objectives:**

1. **Schema Centralization**: Provide a centralized access point for all technical schemata used by Digital Credentials.
2. **Integrity and Authenticity**: Ensure the integrity and authenticity of the schema documents through cryptographic digests.
3. **Interoperability**: Facilitate the seamless integration of Wallet Providers and Relying Parties by providing consistent schema versions.
4. **Credential Lifecycle Support**: Act as a verifiable reference point for schema validation during issuance and presentation.

**Schema Registry Structure and Access:**

The Schema Registry is accessible via the ``.well-known/it-wallet-registry`` discovery endpoint under the `schema_registry` field. It allows for the discovery of schema URIs and their cryptographic integrity checks.

.. list-table:: First-level Fields of the Schema Registry
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Field Name**
     - **Description**
   * - **id**
     - REQUIRED. Unique identifier of the Schema Registry (e.g., ``urn:schemas:it-wallet``).
   * - **version**
     - REQUIRED. The version of the Schema Registry (e.g., ``1.0.0``).
   * - **last_modified**
     - REQUIRED. The timestamp indicating when the Schema Registry was last updated (e.g., ``2025-03-15T12:00:00Z``).
   * - **schemas**
     - REQUIRED. A JSON Array where each entry is a JSON Object representing a Credential Schema definition. Each object contains the parameters defined in the "Schema Definition Parameters" table below, including schema identification, format specifications, URIs, and integrity verification data.

.. list-table:: Schema Definition Parameters
   :widths: 25 75
   :header-rows: 1

   * - **Field Name**
     - **Description**
   * - **id**
     - REQUIRED. The unique identifier of the scheme (e.g., ``mDL+mso_mdoc+org.iso.18013.5.1.mDL``).
   * - **version**
     - REQUIRED. The version of the schema definition (e.g., ``1.0.0``).
   * - **credential_type**
     - REQUIRED. The unique identifier of the Digital Credential type (e.g., ``mDL``, ``pid``, ``eid``).
   * - **format**
     - REQUIRED. The technical format of the schema (e.g., ``mso_mdoc``, ``dc+sd-jwt``).
   * - **vct**
     - CONDITIONAL. It is REQUIRED if the ``format`` is ``dc+sd-jwt``, indicating the Verifiable Credential Type (e.g., ``urn:eudi:mDL:it:1``).
   * - **docType**
     - CONDITIONAL. It is REQUIRED if the ``format`` is ``mso_mdoc``, indicating the document type used (e.g., ``org.iso.18013.5.1.mDL``).
   * - **schema_uri**
     - REQUIRED. The URI where the schema document can be retrieved (e.g., ``https://trust-registry.it-wallet.example.it/.well-known/schemas/mdoc/mDL``).
   * - **schema_uri#integrity**
     - REQUIRED. Cryptographic digest of the schema document for integrity verification. Format: ``{digest_method}-{digest_value}`` (e.g., ``sha256-c8b708728e4c5756e35c03aeac257ca878d1f717d7b61f621be4d36dbd9b9c16``).
   * - **description**
     - OPTIONAL. A human-readable description of the schema, which may be localized (e.g., "Schema tecnico per la mobile Driving License in formato mdoc.").

**Schema Registry Example:**

A non-normative example of the Schema Registry payload:

.. literalinclude:: ../../examples/schema-registry-example-payload.json
  :language: JSON

Registry Integration and Cross-References
------------------------------------------

The registry components are interconnected and work together to support the complete Credential ecosystem:

1. **AS Registry** ↔ **Taxonomy**: AS entities declare capabilities using taxonomy classifications for standardized categorization.
2. **AS Registry** ↔ **Catalog**: Credential types reference AS capabilities for data source validation.
3. **Catalog** ↔ **Taxonomy**: Credential entries specify domains and purposes from the taxonomy for discovery and authorization.
4. **Federation Registry** ↔ **All Components**: Provides cryptographic trust validation for all registry operations and entity authentication.
5. **Schema Registry** ↔ **Issuer/RPs**: Provides the verifiable link to all known Credential format specifications used in the ecosystem.

Registry Infrastructure Usage Journeys
------------------------------------------

The components of the Registry Infrastructure are designed to support various operational phases of the IT-Wallet ecosystem, each involving specific interactions between entities.
The main Journeys below illustrate the interactions with the Registry Infrastructure.

Catalog Browsing
^^^^^^^^^^^^^^^^^^^^^^^

This *Catalog Browsing* journey supports Users (both human users via a **Wallet Instance** and automated systems like **Relying Parties** or web portals) in discovering and selecting available Digital Credentials.

1.  **Accessing the Discovery Endpoint**: The entity (e.g., a Wallet Provider or informational portal) accesses the `Registry Discovery Endpoint` (``.well-known/it-wallet-registry``) to obtain the URI of the **Digital Credentials Catalog** and of the **Taxonomy**.

2.  **Navigation and Selection**:

  * **Credential Discovery**: The entity browses the list of Credentials (``credentials`` field) to identify relevant Credential types (e.g., ``pid``, ``eid``, ``mDL``) and, if needed, uses the information on the **Taxonomy** to navigate their hierarchy and to provide different localizations.
  * **Issuer Metadata**: The entity extracts the **Issuer Identifier** (`entity_id` within the `issuers` field) associated with the desired Credential.
  * **Detail Consultation**: To obtain complete information oand specific technical requirements, the entity accesses the **Entity Configuration** (Issuer Metadata) using the retrieved identifier.

3.  **Final Action**: The entity can then can use the metadata to display the catalog information to a User (or use the information in other way).

Credential Issuance
^^^^^^^^^^^^^^^^^^^^^^^^

This journey defines how a Credential Issuer uses the Registry Infrastructure to prepare and issue a compliant Digital Credential.

1.  **Identifying Requirements**: The CI consults the **Digital Credentials Catalog** for the technical requirements of the Credential type to be issued (e.g., ``max_validity_days``, ``min_loa``).

2.  **Schema and Claim Resolution**:

  * The CI consults the **Schema Registry** to retrieve the technical specification of the format and schema (e.g., JSON Schema for SD-JWT) required by the Catalog, ensuring validity and integrity via the hash (`schema_uri#integrity`).
  * The CI accesses the **Claims Registry** to retrieve the standardized semantic definitions and data formats (data types) of the necessary attributes (claims).

3.  **Authentic Data Retrieval**:

  * The CI consults the **Authentic Source (AS) Registry** to identify the authorized **Authentic Source** (AS) for the required dataset. The AS Registry provides the AS's ``entity_id`` and the technical details of the interface (`integration_endpoint`, `integration_method`).
  * The CI consults the AS endpoint specification to implement the integration needed to retrieve the User data required to populate the Digital Credential.

4.  **Credential Issuance**: The CI uses the retrieved data, validated schemas, and specified formats to generate and sign the Digital Credential in the correct format (e.g., SD-JWT or mDOC).

Credential Presentation and Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This journey describes how a **Wallet Instance** and a **Relying Party (RP)** interact with the Registry Infrastructure when a Digital Credential needs to be presented by a User.

1.  **Wallet Authorization and Selection**:

  * The Wallet receives a Presentation Request from the RP, verifies the validity of the request comparing the requested *claims* with the *Authorization Policies* related to the RP .
  * The Wallet consults the **Digital Credentials Catalog** and the **Taxonomy** to verify the *Domains*, the *Classes* and *Purposes* associated with the Credential types it holds, evaluating which Credentials are suitable for the request.
  * The Wallet verifies if the required attributes (claims) are available and authorized for disclosure based on the request policy (**Credential-Specific** or **Credential-Agnostic** scenarios).
  * The User authorizes the release of the selected, selectively disclosed attributes. The Wallet then packages and presents the Digital Credential to the RP.

2.  **Discovery and Integrity**:

  * The RP receives the Digital Credential from the User.
  * The RP consults the **Federation Registry** via the Trust Anchor's endpoint (`federation_resolve`, `federation_trust_mark_status`) to verify the **cryptographic trust** (Trust Mark) of the Issuer and Wallet Provider as defined in Section :ref:`trust-infrastructure:The Infrastructure of Trust`.
  * The RP consults the **Schema Registry** to download the schema of the presented Credential (`schema_uri`), verifying its integrity (`schema_uri#integrity`).

3.  **Schema and Final Policy Validation**:

  * The RP uses the retrieved schema to validate the structure of the Credential and the data types of the revealed attributes.
  * The RP performs the final check to ensure that the attributes presented comply with the specific requirements of the initial request and authorization policy.

4.  **Acceptance or Rejection**: Based on cryptographic validation, schema compliance, and policy-based authorization, the RP accepts or rejects the Credential for service access.


