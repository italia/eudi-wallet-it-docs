.. include:: ../common/common_definitions.rst
.. Included via index.rst at title level '=' (document title).

Registry Infrastructure
=======================

The IT-Wallet ecosystem operates through a registry infrastructure that provides standardized data definitions and Credential discovery capabilities. The registry system consists of multiple interconnected components that support the complete lifecycle of Digital Credential operations from entity onboarding to Digital Credential presentation.
The registry architecture addresses semantic standardization and Credential discovery requirements through specialized registry components that ensure interoperability and compliance across the ecosystem.

At EU level the European Commission maintains two EUDIW catalogues that are the cross-border counterparts of the national semantic registries to which the national registries align, defined in ARF TS11 (`EUDI-TS 11`_) (Interfaces and formats for the Catalogue of Attributes and the Catalogue of Schemes):

 - **Catalogue of Attributes** is the EU-level catalogue of standardized attribute definitions and namespaces used across Attestations.
 - **Catalogue of Schemes** is the EU-level catalogue of Attestation schemes (``SchemaMeta``): the machine-readable metadata that binds an Attestation type to its Rulebook and schema.

The registries and the catalogues used within the IT-Wallet ecosystem have different purposes and scopes. The registries whose content is evidence of a trust decision, such as the **Register of WRPs** operated by a national Registrar under `CIR2025/848`_ and the **Federation API Endpoints** of the National Trust Framework, are specified in :ref:`infrastructure-trust:Infrastructure of Trust`.
The registries for the semantic definition and the discovery of data are detailed in this Section.

In particular, this section provides first an overview of the IT-Wallet registry infrastructure (:ref:`registry:Registries and Catalogues of the Ecosystem`) and its discovery mechanism (:ref:`registry:Registry Discovery Endpoint`).
Then, it details its components: :ref:`registry:Taxonomy`, :ref:`registry:Claims Registry`, :ref:`registry:Authentic Source Registry`, :ref:`registry:Schema Registry` and :ref:`registry:Digital Credentials Catalog`.
Finally, it describes their relationships (:ref:`registry:Registry Integration and Cross-References`) and usage journeys (:ref:`registry:Registry Infrastructure Usage Journeys`).

Registries and Catalogues of the Ecosystem
-------------------------------------------

The IT-Wallet ecosystem uses several registries and catalogues, at national and at EU level, and they serve two different purposes.

- **Trust purpose**: the content of the registry is consumed by a Trust Evaluator to accept or to reject an entity or an artifact.
  These registries are Trust Artifacts, they are defined in :ref:`infrastructure-trust:Infrastructure of Trust` and the way they are consumed is defined in :ref:`trust-evaluation:Trust Evaluation Process`.
- **Semantic and discovery purpose**: the content of the registry defines the attributes, the schemas and the Credential types, or it makes them discoverable. These registries are defined in this Section.

.. note::
  The distinction between trust and semantic/discovery registries is on the purpose and not on the content. For example, a registry of the semantic and discovery purpose may carry a parameter that points to a trust framework, as the ``trustedAuthorities`` of the Digital Credentials Catalog does, but such a parameter identifies the applicable trust framework and it is not itself the evidence of a trust decision.

.. _table_registries_and_catalogues:
.. list-table:: Registries and Catalogues of the Ecosystem
   :class: longtable
   :widths: 32 18 26 24
   :header-rows: 1

   * - **Registry or Catalogue**
     - **Purpose**
     - **Maintained by**
     - **Specified in**
   * - Taxonomy, Claims Registry, Schema Registry, Authentic Source Registry, Digital Credentials Catalog
     - Semantic and discovery
     - Federation Trust Anchor, under the Supervisory Body
     - This Section
   * - Register of WRPs
     - Trust
     - Registrar
     - :ref:`infrastructure-trust:Register of WRPs`
   * - Federation API Endpoints, Entity Statements and Trust Marks
     - Trust
     - Federation Trust Anchor and Federation Intermediates
     - :ref:`infrastructure-trust:National Trust Artifacts`
   * - Catalogue of Attributes and Catalogue of Schemes
     - Semantic and discovery
     - European Commission
     - [`EUDI-TS 11`_]. The alignment of the national registries is described in :ref:`registry:Registry Integration and Cross-References`
   * - Lists of Trusted Entities, Trusted Lists and List of Trusted Lists
     - Trust
     - European Commission and Member States
     - :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`

.. note::
  The mechanisms that publish the status of a certificate or of an Attestation, such as the Certificate Revocation Lists, the OCSP responders and the Token Status Lists, are not registries and they are not listed in the table above.
  They are described in :ref:`infrastructure-trust:Revocation Mechanisms`.

Five national semantic and discovery registries provide the standardized definitions and discovery data:

1. **Taxonomy**: Hierarchical classification system organizing Credentials by domain and purpose.
2. **Claims Registry**: Standardized semantic definitions for individual Credential attributes and data types.
3. **Authentic Source Registry**: Registered Authentic Source (AS) with their declared capabilities, available claims and verification endpoints.
4. **Schema Registry**: Authoritative list of Credential Schemas.
5. **Digital Credentials Catalog**: Available Credential types with their metadata and issuance information.

The national registries are maintained by the Federation Trust Anchor under the Supervisory Body to ensure consistency, security, and regulatory compliance.
They are populated by the onboarding processes described in :ref:`onboarding-system:Onboarding Processes`, and they are read both during the onboarding and during the operational phases.

The Entities that **provide** the information are the following:

  - the Attestation Scheme Provider, for the definition of a Credential type and its scheme;
  - the Authentic Sources, for their declared data capabilities;
  - the Wallet-Relying Parties and the Wallet Providers, for their registration data.

These roles are described in :ref:`onboarding-system:System Actors and Roles`.

None of these Entities writes in a registry directly. They provide the information through the onboarding processes, which verify it and write it.
Each registry is then signed and published by the Federation Trust Anchor for the national registries and for the federation statements, by the Registrar for the Register of WRPs, and by the European Commission for the EU catalogues and lists.

.. note::
  Not all the content of a registry is provided by an Entity. Some of it is set by the Onboarding System itself, such as the state of a Credential type in the Digital Credentials Catalog, which derives from the conditions of the versioned entry. The internal components of the Onboarding System and the process each of them realizes are described in :ref:`onboarding-system:System Components and Services`.

.. note::
  An Entity that provides an information is not necessarily the Entity that decides it, because the decisions on a Credential type are taken in its Attestation Rulebook, which is an input of the Onboarding System.

Figure :ref:`fig_registry_infrastructure` shows the whole set of the registries and catalogues, grouped by purpose and by level, with the Entities that provide their content and the authorities that publish them.

.. _fig_registry_infrastructure:
.. plantuml:: plantuml/registry-infrastructure.puml
    :width: 99%
    :alt: The figure illustrates all the registries and catalogues of the ecosystem, grouped by purpose and by level, with the Entities that provide their content and the authorities that publish them.
    :caption: `Registries and Catalogues of the Ecosystem <https://www.plantuml.com/plantuml/svg/ZLRRRjiu47tNLqoD0fi0IVEmxKkm6zHria20tSAmKlJHOAInJPGY1LwIQel-UuUaBfJYr39WG29dpioPgpuQoxHrbSYoDrmMmfK8VwtUNwtURrUggfL4QM-ox0-unHsN2FbwS_zmboV2rjMir7zU5QggbBmvShDJqbwoPpIgmiiFLmLgotUyO1PdI9VCiaTcveX-msQ652-t1TFb3Cbd9WJQ6OBulJWmkSSj4tF4TrpC5JK7ZgASAUmCQdDAxefBOxbrbljaPP-KaoNJpPbaTckmOjBouW8MdvaNO08skEV6Qexc0lBs7fWiuPQRGZsXRc3jTAqCBixXHzONpPbbtvLKLKDW3-tZuWBUcbfpYtylkhmkpXETGZ1URNKqwJLN_i1qJfm6CCM1V4mHyd0o7u6PL7lfx043vLmvNU1y72fl9jJU8Q7SyZsdDrXfB3qQ4mPMtVqhI3ydkR7Q6VjQOXxyvIjvY6nGa-wcVGIrWw-RjKbD3vKseh53EgivAVz3lkjW79RhUxYJPQsuj6JzZYZP1d9B7LsHaWdr4NtwZ-blhzj9IQBR2dn2GQRklWpXYM3_ajzcGemYl6MM8l3eh0_2ejVn_9RzpPnKRKFXl4J9u_592A6iJtHmq-i5ybZ6q0mfmfP9pocLZHn_4wgy8RdgpBWQzHCtIZUVL1bgV3W1VvI29DEMK3g8G6kjrHEdf7hM52waLH3I6qb3Vvt2TRDhm69TYyGECKUwPeIGp1y2wTF_h6lI_1f6xkK6HSFb7jQqcoXw8V6jEMwCYow_x2guZvSZSt7S3_xgYDr2XwuO6qkKqy4USj1YnCsGnYywVZncKNfKBw6Rbx8uA3rkhTWryIR5eDqs0cXd51lQcfvFvjtlQ0eW6V9TvhIgaKbOzQSfGDWcf4gx_v9-y7nGK4Tw1YY_KD1M8LV2RJQfA3gyWNIbN7UX2Qgb_vZWWJ0r04jJQ9iQGtjmQfCuphDfYPr0LthF9Fy_1fJBdT9LVFQmmJorC1IiPezSXFRCgFfwq92RCM8NxO3YjREs38DIF-glwIk9LfYEIXDI8MWD1CLiKa01fXsrOykxeJI2tKdp7ud4ilPPckJ87fWbqz0j0ooF8WtrSGsVbQ-V5WVREURJvTzbl2mzTzmhluL6XMBuNiOfLxj7mSqX98tg92dy8xxdBzLUQFHXEYRSjqKGxTWUbnt81k5k_rpJpgAzHl-fGaUG2KAh-j9FAS2xTodIifViujPjxw432FSZoj9_Wly2>`_

Figure :ref:`fig_registry_discovery` shows, for the registries defined in this Section, the onboarding or operational phase in which each of them is read and by whom. More details are provided in each section.
The way the registries with a trust purpose are read is described in :ref:`trust-evaluation:Trust Evaluation Process`.

.. _fig_registry_discovery:
.. plantuml:: plantuml/registry-discovery.puml
    :width: 99%
    :alt: The figure illustrates who reads the national semantic and discovery registries and in which phase.
    :caption: `Discovery on the Registry Infrastructure <https://www.plantuml.com/plantuml/svg/dLR1Rjim3BtxAxXWm58WQGxhBiDMT4jtw6K8cWux1ep4909ioPFafCQmVnybnucIEassNcfJvECZ-IZdpdcqlYhoB7kZjCWhIV1fV3CQtyp6fYYD9krli-mTtDD2QOBfvF7XwTiqSVPLYTA-7mbJ54RVTfmiZFP3t90p1Gq_Z2HwdAEZ2rmhH_O2DoLd0gsym9EUnGhracQO-mlSDvZdTDPnfBJpobTUXVgphwRI4ctTr-XdZWhKNea1zBvZSC0S7ccfdBUAt02cstD0BU5UEM7MP6kOLBOqZdfNy3lRpQ7lyTbeKzGCzhHzx0tWhIkjylIvrpQsTvN4Y1nLCRDDoX0v3WRNaZWFW2wD_bBv5KN2KrDPGPVZEB7YMbEiQRHSZY3Oc9jbHHnxhvQAts1iIGO-c3iOj-SdaFvasOIiCxeVTCKWF_XVwXlCx3UjdQUYhvohsBqp6JmqXsdqLeLx04jvhVHomWiMPzrxR0omjQJ1gJ3t2DXskscswnZ08OMz4FSWZOWdrgoLREhv6IsmCwKGZJT7yyuF-GysAmEMK3gGbGtiEJyOFJTSQtWjhM4MBZfdnuHXM9N3MpWKuSUTq2DMc108B76kSXNw0drSeyfndbCJwQx06t1CUM7iYVodKhSxSpwfqfwq90bbitmNPJsSSLjkAyGagT8B0tswNbuFaWIl8B_U_v9iUvsWy6hTr11d45JCJzqqzftjsA0iEzBA_y74ga8tbmt7y6m2RMLXAxsfoQDANMV6ewlYQ7JDAPX5VElAp_PwHu3uwLJoRBlZ9-iC6SGEUURhak9D7U9Gy_LdwLUbB1NiuDhn5lWyMsEkfFBrJ6BDSsQos47r8F-bLNS1mKRv5PyirPhqCUF3Ai-k8a-lG1_BbE6Zh-8CER6c84p-iW5w_dpDAq_k6kuRLIOAZbkJa_0HyyM5DMY5l6iY1v1sbULUyrIO6FitN2oLbXo_HY4T599ybv8gDYibLYzoXWmCxNbLObqhiuaYnRZUeQUxWhBkbJuzd7InryAFf15FtFJzRgSLx6xBm899HPa4ZNPjO_VTScf-aSS_vKoBlkEhB_mA_0i0>`_


Registry Discovery Endpoint
---------------------------

The Federation Trust Anchor MUST provide a discovery mechanism for registry components through standardized *well-known* endpoints providing metadata and REST API discovery information to handle complex operations like pagination and filtering.

The Federation Trust Anchor MUST publish registry discovery metadata at the ``.well-known/it-wallet-registry`` endpoint with content negotiation support:

- **Default Content-Type**: ``application/jwt`` (signed JWT ensuring authenticity and integrity)
- **Alternative Content-Type**: ``application/json`` (plain JSON for development/debugging purposes)

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The JWT payload of the Registry Discovery response MUST contain the following parameters:

.. list-table:: Registry Discovery Endpoint JWT Payload Parameters
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Field Name**
     - **Description**
   * - **id**
     - REQUIRED. Unique identifier of the Registry Discovery document (e.g., ``urn:it-wallet-registry:it-wallet``).
   * - **version**
     - REQUIRED. The version of the Registry Discovery document (e.g., ``1.0.0``).
   * - **last_modified**
     - REQUIRED. The timestamp indicating when the list was last updated (e.g., ``2025-03-15T12:00:00Z``).
   * - **endpoints**
     - REQUIRED. JSON object containing the URIs of all registry components. The following endpoint keys MUST be present:

       * **claims_registry**: URI of the Claims Registry API.
       * **authentic_sources**: URI of the Authentic Source Registry API.
       * **credential_catalog**: URI of the Digital Credentials Catalog well-known endpoint.
       * **taxonomy**: URI of the Taxonomy resource.
       * **schema_registry**: URI of the Schema Registry API.
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
      "schema_registry": "https://trust-anchor.eid-wallet.example.it/api/v1/schemas"
    },
    "content_negotiation": ["application/json", "application/jwt"]
  }

Content Negotiation and Signed Representation
---------------------------------------------

Every endpoint of the Registry Infrastructure MUST support content negotiation and serve its content in two representations:

- **Default Content-Type**: ``application/jwt`` (signed JWT that provides authenticity and integrity)
- **Alternative Content-Type**: ``application/json`` (plain JSON for development and debugging)

Both representations are served at the same endpoint URL, not as separate resources or paths. The client selects the representation with the ``Accept`` request header, and the Federation Trust Anchor states the returned representation in the ``Content-Type`` response header. If the request does not ask for a supported type (``Accept`` absent, ``*/*``, or only unsupported types), the endpoint MUST return the ``application/jwt`` representation.

This requirement applies to all the endpoints of the Registry Infrastructure listed in the following table:

.. _table_registry_content_negotiation:
.. list-table:: Registry endpoints supporting content negotiation
   :class: longtable
   :header-rows: 1
   :widths: 40 60

   * - **Registry component**
     - **How the endpoint is located**
   * - Registry Discovery
     - Fixed well-known path ``.well-known/it-wallet-registry``.
   * - Claims Registry
     - Absolute URL published under the ``claims_registry`` key of the discovery document.
   * - Authentic Source Registry
     - Absolute URL published under the ``authentic_sources`` key of the discovery document.
   * - Schema Registry
     - Absolute URL published under the ``schema_registry`` key of the discovery document.
   * - Taxonomy
     - Absolute URL published under the ``taxonomy`` key of the discovery document.
   * - Digital Credentials Catalog
     - Absolute URL published under the ``credential_catalog`` key of the discovery document.

The Registry Discovery Endpoint is the only one at a fixed well-known path. A client reads it first to obtain the URL of every other component from its signed ``endpoints`` object (see :ref:`registry:Registry Discovery Endpoint`). A client MUST NOT assume a fixed path for the other components. Content negotiation applies to the discovery endpoint and to every component URL it publishes.

All these endpoints handle content negotiation in the same way: the same request, the same two ``Content-Type`` values, and the same signed representation.

The signed representation is a JWT in compact serialization, served as ``application/jwt``. Its header MUST contain the parameters in the following table.

.. _table_catalog_parameters:
.. list-table:: JWT header parameters of the signed representation
   :class: longtable
   :header-rows: 1
   :widths: 25 50 25

   * - **Header parameter**
     - **Description**
     - **Reference**
   * - **typ**
     - REQUIRED. It MUST be set to ``JWT``.
     - [:rfc:`7515` Section 4.1.9].
   * - **alg**
     - REQUIRED. A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms in Section :ref:`algorithms:Cryptographic Algorithms` and MUST NOT be set to ``none`` or with a symmetric algorithm (MAC) identifier.
     - [:rfc:`7515` Section 4.1.1].
   * - **kid**
     - REQUIRED. Unique identifier of the public key.
     - [:rfc:`7515` Section 4.1.4].
   * - **x5c**
     - OPTIONAL. Contains the X.509 public key Certificate or Certificate chain [:rfc:`5280`] corresponding to the key used to digitally sign the JWT. When the header parameter `kid` value is present, it MUST refer to the same leaf's cryptographic public key used with the X.509 Certificate.
     - [:rfc:`7515` Section 4.1.6.].
   * - **cty**
     - REQUIRED. It MUST be set to ``application/json``.
     - [:rfc:`7515` Section 4.1.6.].

The plain representation is the same content, served as a plain JSON object instead of a signed JWT.

The following non-normative example requests both representations from the Digital Credentials Catalog endpoint. The URL is the one resolved from the discovery document, shortened here for readability.

.. code-block:: http

    GET /.well-known/credential-catalog HTTP/1.1
    Host: trust-anchor.eid-wallet.example.it
    Accept: application/jwt

    HTTP/1.1 200 OK
    Content-Type: application/jwt

    eyJhbGciOiJSUzI1NiIsImtpZCI6ImV4YW1w...

.. code-block:: http

    GET /.well-known/credential-catalog HTTP/1.1
    Host: trust-anchor.eid-wallet.example.it
    Accept: application/json

    HTTP/1.1 200 OK
    Content-Type: application/json

Taxonomy
--------

The **Taxonomy** is the authoritative vocabulary that organizes Credentials in the IT-Wallet ecosystem, and it is the semantic foundation of their interoperability. It is independent of the Credential format.

In a single resource, it defines the hierarchy of Domains, Classes and Purposes that Credential Types reference, supporting authorization policy evaluation and ecosystem-wide standardization.

The Taxonomy endpoint URL is published under the ``taxonomy`` key of the Registry Discovery document. The endpoint supports the content negotiation and signed representation common to all Registry Infrastructure endpoints (see :ref:`registry:Content Negotiation and Signed Representation`).

**Taxonomy Objectives:**

1. **Semantic Foundation**: Establish standardized vocabulary for domains and purposes across the ecosystem
2. **Policy Framework**: Enable structured authorization decisions based on hierarchical classification
3. **Interoperability**: Ensure consistent interpretation of credential classifications
4. **Extensibility**: Support evolution of the ecosystem with new Domains, Classes, Credential Types and Purposes
5. **Cross-Border Compliance**: Align with EU regulatory requirements and international standards


Taxonomy Usage
^^^^^^^^^^^^^^

- **Authentic Source Registry**: Authentic Sources declare capabilities using taxonomy classifications
- **Digital Credentials Catalog**: Credential Types specify Domains, Classes and Purposes
- **Authorization Policies**: Policy evaluation leverages taxonomy structure for access control decisions


Digital Credentials Hierarchy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

.. list-table:: Mapping between Credential Classes and Purposes
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

Taxonomy Structure
^^^^^^^^^^^^^^^^^^

The taxonomy maintains a four level hierarchical structure, that is the Domains, the Classes, the Credential Types and the Purposes defined in :ref:`registry:Digital Credentials Hierarchy` above.

.. note::
  Credential Type is a concept defined at the Digital Credentials Catalog level, not within the Taxonomy. The Taxonomy provides the classification vocabulary (Domains, Classes, Purposes) that Credential Types in the Catalog reference.

**Localization Support:**

The taxonomy supports multilingual environments through the ``_l10n_id`` suffix pattern, enabling efficient localization management for user interfaces and cross-border implementations.


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
     - REQUIRED. The timestamp indicating when the list was last updated (e.g., ``2025-03-15T12:00:00Z``).
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

Claims Registry
---------------

The Claims Registry endpoint URL is published under the ``claims_registry`` key of the Registry Discovery document. The endpoint supports the content negotiation and signed representation common to all Registry Infrastructure endpoints (see :ref:`registry:Content Negotiation and Signed Representation`).

The Claims Registry MUST contain:

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
^^^^^^^^^^^^^^^^^^^^^

As shown in Figure :ref:`fig_registry_infrastructure` and Figure :ref:`fig_registry_discovery`, the Claims Registry MUST support the complete ecosystem lifecycle:

**During Onboarding Process**:

  - **AS Registration**: Authentic Sources declare available claims from standardized registry during capability registration.
  - **CI Registration**: Credential Issuers select Authentic Source entities based on required claims. The Credential types that use those claims are registered in the catalog by the Attestation Scheme Provider, see :ref:`onboarding-system:Credential Type Registration`.
  - **RP Registration**: Relying Parties specify authorization requirements using domains/purposes for specific User's attributes.

**During Operational Activities**:

  - **Credential Issuance**: Claims definitions ensure consistent data representation across different Credential types.
  - **Presentation Requests**: Relying Parties reference claims for schema validation and authorization verification in both credential-specific and credential-agnostic scenarios.

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
     - REQUIRED. The timestamp indicating when the list was last updated (e.g., ``2025-03-15T12:00:00Z``).
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

The Authentic Source Registry endpoint URL is published under the ``authentic_sources`` key of the Registry Discovery document. The endpoint supports the content negotiation and signed representation common to all Registry Infrastructure endpoints (see :ref:`registry:Content Negotiation and Signed Representation`).

The Authentic Source Registry MUST contain at least:

  - **Organization Information**: Legal entity details, regulatory status, and authoritative role within specific domains.
  - **Data Capabilities**: Declared claims availability referencing standardized definitions from the Claims Registry with corresponding Taxonomy classifications.
  - **Integration Methods**: Technical access mechanisms (PDND).
  - **Intended Purposes**: Supported Credential types and business contexts for AS-CI coordination.
  - **Data Quality Assurance**: Authoritative status, update frequency, and audit trail capabilities.

The Authentic Source Registry MUST ensure:

  - **Coordinated Data Access**: Enables CI discovery of appropriate data from Authentic Sources for Credential issuance.
  - **AS-CI Integration**: Technical endpoints and access methods enable standardized AS-CI communication. It facilitates approval workflows and data access coordination between entities.
  - **Regulatory Compliance**: Supports public administration transparency and private sector coordination requirements.

.. note::
   The Authentic Source Registry is a public registry that provides the Credential Issuer with guidance for Credential provisioning.

Authentic Source Registry Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As shown in Figure :ref:`fig_registry_infrastructure` and Figure :ref:`fig_registry_discovery`, the Authentic Source Registry supports ecosystem coordination throughout the operational lifecycle:

**During Onboarding Process**:
  - **AS Self-Declaration**: Authentic Sources register capabilities before any Credential types exist in the catalog.
  - **CI Discovery**: Credential Issuers search for Authentic Source entities based on required claims and intended Credential types.

**During Operational Activities**:
  - **Credential Issuance**: Credential Issuer systems reference Authentic Source Registry for real-time data access during Credential issuance.

Authentic Source Registry Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

During registration, Authentic Sources declare their capabilities before Credential types exist in the catalog. This declaration establishes the foundation for subsequent CI registration and Credential type creation.

**Authentic Source Unique Identifier Schema**

Each Authentic Source MUST be assigned a unique identifier that follows the HTTPS URL schema defined below. This identifier is used for referencing AS entities across the registry system and in the Digital Credentials Catalog, ensuring consistency with OpenID Federation entity identification patterns.

*AS Identifier Schema:*

.. code-block:: text

  https://{organization_domain}[/{optional_path}]

*Schema Components:*

- **organization_domain**: DNS domain controlled by the organization
- **optional_path**: Additional path component for specific services or departments

The AS identifier MUST follow these normative rules:

1. **HTTPS Protocol**: MUST use HTTPS scheme for security and trust verification
2. **Domain Ownership**: Organization MUST control the DNS domain used in the identifier
3. **Uniqueness**: Guaranteed through DNS namespace uniqueness
4. **Stability**: SHOULD remain stable over time to avoid reference breakage
5. **Resolvability**: The URL SHOULD be resolvable (though not required to serve content)

*Examples of compliant AS identifiers:*

- ``https://motorizzazione.gov.example``: Public - Ministry of Transport, Motorization Dept
- ``https://registry.anpr.example``: Public - National Registry of Resident Population
- ``https://api.bank.example/auth-source``: Private - Example Bank Financial Services

**Authentic Source Registry Parameters**

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
     - REQUIRED. The timestamp indicating when the list was last updated (e.g., ``2025-03-15T12:00:00Z``).
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
     - String Array
     - OPTIONAL. Array of customer service contacts or user support channels (e.g., email address).
   * - **data_capabilities[].verification_endpoint**
     - JSON object
     - OPTIONAL. Present only for Annex VI attributes relying on a public-sector Authentic Source that are exported to the EUDIW Catalogue of Attributes. Describes the cross-border verification interface exposed to Qualified Trust Service Providers, distinct from the domestic PDND e-Service and conformant to ETSI TS 119 478. It contains ``method`` (one of ``oots_edelivery`` for the ISO 15000/eDelivery interface of ETSI TS 119 478 Section 6.2, or ``rest_oauth2`` for the REST + OAuth 2.0 interface of ETSI TS 119 478 Section 6.1) and ``endpoint`` (the eDelivery party identifier or REST endpoint). The interface MAY be exposed by the Authentic Source directly or by a designated national intermediary (e.g. an OOTS access point).

.. note::
  For further details on the required features and the expected outcome in terms of user experience, see the Section :ref:`functionalities:Issuance from the Wallet Instance Catalog` for the parameter `data_capabilities.user_information` and Section :ref:`functionalities:Focus on Electronic Attestations of Attributes` for the parameters `organization_info.logo_uri`, `organization_info.logo_extended_uri`, `data_capabilities.logo_uri`, `data_capabilities.background_color` and `data_capabilities.available_claims.order`.

**Authentic Source Registry Example**

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

Schema Registry
---------------

The **Schema Registry** is the authoritative inventory of all known and accepted **Credential Schemas** (JSON Schema for SD-JWT, CBOR Schema for mDOC) within the IT-Wallet ecosystem.

**Schema Registry Objectives:**

1. **Schema Centralization**: Provide a centralized access point for all technical schemata used by Digital Credentials.
2. **Integrity and Authenticity**: Ensure the integrity and authenticity of the schema documents through cryptographic digests.
3. **Interoperability**: Facilitate the seamless integration of Wallet Providers and Relying Parties by providing consistent schema versions.
4. **Credential Lifecycle Support**: Act as a verifiable reference point for schema validation during issuance and presentation.


Schema Registry Usage
^^^^^^^^^^^^^^^^^^^^^

As shown in Figure :ref:`fig_registry_infrastructure` and Figure :ref:`fig_registry_discovery`, the main Entities interacting with the Schema Registry are:

  - **Attestation Scheme Providers**: They provide the schema of a Credential type, or its alignment to the schema of an external Rulebook, and the Onboarding System registers it with its integrity digest during the :ref:`onboarding-system:Schema Provisioning`.
  - **Credential Issuers**: They use the Schema Registry to build their metadata and to issue the Digital Credentials according to the registered schema.
  - **Relying Parties**: They use the Schema Registry to gather all the information needed about the Digital Credentials they intend to request during the presentation phase.
  - **Wallet Providers**: They access the Schema Registry to retrieve all necessary information for integrating them into their Wallet Solutions.

Schema Registry Structure
^^^^^^^^^^^^^^^^^^^^^^^^^

The Schema Registry endpoint URL is published under the ``schema_registry`` key of the Registry Discovery document. The endpoint supports the content negotiation and signed representation common to all Registry Infrastructure endpoints (see :ref:`registry:Content Negotiation and Signed Representation`).
It allows the discovery of schema URIs and their cryptographic integrity checks.

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
     - REQUIRED. The timestamp indicating when the list was last updated (e.g., ``2025-03-15T12:00:00Z``).
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

Digital Credentials Catalog
---------------------------

The Digital Credentials Catalog is the registry of all available Digital Credentials recognized within the IT-Wallet ecosystem. It acts as a single reference point for all actors involved in the process of issuing, verifying and using Digital Credentials.
The Digital Credential Catalog MUST contain at least:

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

The Digital Credential Catalog MUST ensure to:

  1. Facilitate Digital Credential discovery for Users.
  2. Standardize the technical and functional description of Digital Credentials.
  3. Enable interoperability between different Issuers and Relying Parties.
  4. Simplify the integration process for Wallet Providers and Relying Parties.
  5. Ensure trust in the ecosystem through verifiable and trustworthy information.
  6. Provide transparency on the ecosystem of available Digital Credentials.

Digital Credentials Catalog Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As shown in Figure :ref:`fig_registry_infrastructure` and Figure :ref:`fig_registry_discovery`, the main Entities involved in the Digital Credential Catalog are:

  - **Attestation Scheme Providers**: The Entities that own the Attestation Rulebook of a Digital Credential and that request the registration of the corresponding versioned entry, see Attestation Scheme Provider.
  - **Digital Credential Issuers**: They are added to the ``issuers`` field of a versioned entry as a result of the Digital Credentials they declare in their registration data.
  - **Relying Parties**: They use the Digital Credential Catalog to gather all the information needed about the Digital Credentials they intend to request during the presentation phase.
  - **Wallet Providers**: They access the Digital Credential Catalog to identify the available Digital Credentials and to retrieve all necessary information for integrating them into their Wallet Solutions.
  - **Users**: The Users who indirectly use the Digital Credentials Catalog through their Wallet Instances to discover and request Digital Credentials.
  - **Authentic Sources**: They are referenced by the versioned entry as its data source and they act as Attestation Scheme Provider when they own the Attestation Rulebook.

A versioned entry is not provided by a single Entity.
Its fields come from different sources and they are written in different onboarding phases, as summarized in the table below.
The Data Identifiers that carry this information through the onboarding, and their mapping to the fields of the entry, are defined in :ref:`onboarding-system:Registration Data Model`.

.. _table_catalog_entry_provision:
.. list-table:: Provision of a Versioned Entry of the Digital Credentials Catalog
   :class: longtable
   :widths: 40 32 28
   :header-rows: 1

   * - **Fields**
     - **Provided by**
     - **Process**
   * - ``credential_type``, ``version``, ``credential_name_l10n_id``, ``legal_type``, ``domains``, ``classes``, ``purposes``, ``authentication``, ``validity_info``, ``restriction_policy``, ``pricing_policy``, ``rulebookURI``, ``bindingType``, ``attestationLoS``, ``trustedAuthorities``
     - The Attestation Scheme Provider, that takes the values from the Attestation Rulebook it owns
     - :ref:`onboarding-system:Credential Type Registration`
   * - ``authentic_sources`` or ``parent_credentials``
     - The Attestation Scheme Provider, referencing the entries of the :ref:`registry:Authentic Source Registry` or an already registered Credential type
     - :ref:`onboarding-system:Credential Type Registration`
   * - ``schema_uri``, ``format``, ``vct``, ``docType``
     - The Attestation Scheme Provider, through the schema it makes available in the :ref:`registry:Schema Registry`
     - :ref:`onboarding-system:Schema Provisioning`
   * - ``issuers``
     - Each element derives from the Digital Credentials that a Credential Issuer declares in its registration data, with the issuance capabilities it offers for each of them
     - :ref:`onboarding-system:Entity Registration` and :ref:`onboarding-system:Entity Update`
   * - ``state``
     - Not provided. It derives from the conditions of the versioned entry
     - :ref:`onboarding-system:Credential Type Activation and Deactivation`

The registration of the versioned entry is approved by the Supervisory Body, as described in :ref:`onboarding-system:Eligibility and Compliance Preconditions`, it is written by the Onboarding System and it is published by the Federation Trust Anchor with the rest of the catalog.

.. note::
  The scheme is the machine-readable definition of an Attestation type, that at EU level is registered in the Catalogue of Schemes and that at national level corresponds to the versioned entry of the Digital Credentials Catalog.
  The Credential Schema is the JSON Schema or the CBOR Schema that validates the structure of the Digital Credential, and it is registered in the :ref:`registry:Schema Registry`.
  The Attestation Scheme Provider owns the first one and provides the second one as part of the technical specification of the Credential type.

Digital Credentials Catalog Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Digital Credentials Catalog endpoint URL is published under the ``credential_catalog`` key of the Registry Discovery document. The endpoint supports the content negotiation and signed representation common to all Registry Infrastructure endpoints (see :ref:`registry:Content Negotiation and Signed Representation`).
Its signed representation is a JWT. The header parameters MUST be as defined in the :ref:`corresponding table <table_catalog_parameters>`, and the payload contains the following parameters:

.. list-table:: First-level Fields of the Digital Credentials Catalog
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - **Field Name**
     - **Description**
   * - **id**
     - REQUIRED. Unique identifier of the Digital Credentials Catalog (e.g., ``urn:credential-catalog:it-wallet``).
   * - **version**
     - REQUIRED. The version of the Digital Credentials Catalog (e.g., ``1.0.0``).
   * - **last_modified**
     - REQUIRED. The timestamp indicating when the list was last updated (e.g., ``2025-03-15T12:00:00Z``).
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
  * - **state**
    - REQUIRED. State of this versioned entry of the Credential type. It MUST be one of:

      * ``ACTIVE``: the Credential type can be issued from this versioned entry. An entry can be ``ACTIVE`` only while at least one Credential Issuer is listed in the **issuers** field, the referenced Authentic Source or parent Credential type is available, and the schema is registered for at least one supported format.
      * ``INACTIVE``: the Credential type MUST NOT be issued from this versioned entry. An entry is ``INACTIVE`` when it has just been registered, when one of the conditions for the ``ACTIVE`` state stops holding, or when it has been superseded by a more recent version.

      Only one versioned entry of the same ``credential_type`` MUST be ``ACTIVE`` at a given time.
  * - **credential_name_l10n_id**
    - REQUIRED. Localization key referencing the human-readable name of the Digital Credential in the localization bundle (e.g., ``mDL.name``).
  * - **legal_type**
    - REQUIRED. Legal classification of the Credential (e.g., ``pub-eaa``, ``qeaa``, ``eaa``).
  * - **restriction_policy**
    - OPTIONAL. Legal restrictions on Wallet Solutions and/or Credential Issuers allowed to request/issue the Digital Credential.

      * **allowed_wallet_ids**: List of allowed Wallet Solutions identifiers.
      * **allowed_issuer_ids**: List of allowed Credential Issuers identifiers. If present, it represents a whitelist of Credential Issuers that may be added to the **issuers** field of the corresponding Digital Credential, as described in :ref:`onboarding-system:Credential Type Registration`.
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
    - CONDITIONAL. It is REQUIRED only if **state** is ``ACTIVE``. Array of relevant information about authorized Credential Issuers, including administrative and technical data such as Organization name, a reference to the API specification document and supported issuance mechanisms. Each array element contains:

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
          * **immediate_flow**: REQUIRED. Boolean. Indicates if the immediate issuance is supported.
          * **wallet_initiated**: REQUIRED. Boolean. Indicates if the Wallet-Initiated flow is supported.
          * **issuer_initiated**: REQUIRED. Boolean. Indicates if the Issuer-Initiated flow issuance is supported (Third Party Initiated Flow).
          * **max_deferred_issuance_time_minutes**: CONDITIONAL. Integer. Maximum time in minutes for the availability of the issuance of the Credential. REQUIRED if ``deferred_flow`` is ``true``.
          * **notification_methods**: CONDITIONAL. String Array. Contains the notification methods supported by the Credential issuer for the deferred issuance, such as ``"push"``, ``"polling"``. REQUIRED if ``deferred_flow`` is ``true``.

  * - **authentic_sources**
    - CONDITIONAL. It is REQUIRED only if ``parent_credentials`` is absent. Array of Authentic Source JSON objects referencing authorized Authentic Sources. Each object MUST contain the AS entity identifier and the specific data capability identifier:

      * **id**: String identifier referencing the Authentic Source entity_id as registered in the :ref:`registry:Authentic Source Registry`.
      * **dataset_id**: String identifier of the specific data capability/dataset used by the Issuer from the AS.
  * - **parent_credentials**
    - CONDITIONAL. It is REQUIRED only if ``authentic_sources`` is absent. Array of ``credential_type`` identifier corresponding to Credentials designated as data sources. Each element identifies a Credential that acts as an Authentic Source during the Digital Credential Issuance process.
  * - **trustedAuthorities**
    - REQUIRED. Array of JSON objects that resolve to the applicable trust anchor(s), containing:

       * **frameworkType**: type of the applicable trust model. A string from the set of ``etsi_tl`` or ``openid_federation``.
       * **value**: standard URI-formatted identifier for the Trusted List (for type ``etsi_tl``) or Entity Identifier (for type ``openid_federation``).
       * **isLoTE**: a boolean value that MUST be TRUE when the applicable trust framework type is an ETSI Trusted List (``etsi_tl``) but the trusted list behind the value URI is a list of trusted entities (LoTE) according to ETSI TS 119 602. Value MUST be FALSE if the applicable trusted list specification is ETSI TS 119 612. Attribute MUST NOT be used with other framework types.

      OpenID Federation MAY only be used in context of non-qualified EAA types. For the others the trust model is based on European Commission managed Lists of Trusted Lists.

      .. note::
        Use of ``isLoTE`` will become unnecessary and must be deprecated once OpenID4VCI specifies a new enumeration for Lists of Trusted Entities according to ETSI TS 119 602, the tentative enumeration is ``etsi_lote``.

  * - **rulebookURI**
    - REQUIRED. URI to the human-readable Attestation Rulebook that defines all the non-machine-readable aspects of the Digital Credential type.
  * - **bindingType**
    - REQUIRED. Indicates the type of cryptographic key binding required for issuance of the Digital Credential. Allowed value is a string from the set of: ``claim`` (binding to a cryptographic claim presented by the User), ``key`` (binding to a key possessed by the User), ``biometric`` (binding to presented biometrics of the User) or ``none`` (no cryptographic binding).
  * - **attestationLoS**
    - REQUIRED. Level of security (LoS) the Digital Credential is to be provided at. Allowed value is a string from the set of: ``iso_18045_high``, ``iso_18045_moderate``, ``iso_18045_enhanced-basic`` or ``iso_18045_basic`` (see Annex D.2 of `OpenID4VCI`_ for more details).

.. note::
  While ``min_loa`` in the claim ``authentication`` specifies the Digital Credential authentication requirements referring to the eID mean level of assurance required during user authentication in the issuance process, the claim ``attestationLoS`` complements this requirement by specifying the attack potential resistance for both user authentication and key storage.

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The canonical source for display characteristics and claim structure is determined by the **Credential Issuer's Metadata**.

The overall logic for presenting a Digital Credential is the following:

1. Depending on the required Trust Framework, the Wallet or Relying Party retrieves the :ref:`registry:Digital Credentials Catalog` (for both Digital Credentials managed by Credential Issuers anchored in the National or EUDIW Trust Framework) to discover the available `credential_type` and the `entity_id` of their Credential Issuers.
2. It retrieves the full Credential Issuer Metadata (see :ref:`credential-issuer-solution:Metadata for openid_credential_issuer`) as described in Section 12.2.2 of `OpenID4VCI`_.
3. The Credential Issuer Metadata MUST contain the full display characteristics (logos, colors) and the detailed schema information (via links to the appropriate Type Metadata or directly in the configuration). The Issuer builds this metadata based on the suggestions provided by the Authentic Source (via the AS Registry) and the standard schema specifications (via the Schema Registry).

Registry Integration and Cross-References
------------------------------------------

As shown in Figure :ref:`fig_registry_relationships`, the registry components are interconnected and work together to support the complete Credential ecosystem:

1. **AS Registry** ↔ **Taxonomy**: Authentic Sources declare capabilities using taxonomy classifications for standardized categorization.
2. **AS Registry** ↔ **Claims Registry**: Authentic Sources declare capabilities on available claims using the Claim Registry.
3. **AS Registry** ↔ **DC Catalog**: Credential types reference AS capabilities for data source validation.
4. **DC Catalog** ↔ **Taxonomy**: Credential entries specify domains and purposes from the taxonomy for discovery and authorization.
5. **Schema Registry** ↔ **DC Catalog**: Credential types reference to the Schema Registry for data discovery and validation.

.. _fig_registry_relationships:
.. plantuml:: plantuml/registry-relationships.puml
    :width: 99%
    :alt: The figure illustrates the national registry relationships.
    :caption: `Relationships between National Registries <https://www.plantuml.com/plantuml/svg/ZL9BRzD04BxxLmmH4gtKg0VAfOAenUNG2q9DxzLaT-oCj0zhPpQG8luxVZJM4a3DoTRiVe_lsxaHnQJPk-eD1-Eo9VXONrtMLqzrz5qC57HLLU_WZXeE1Ejl3_UFNzR5PSqTslJ-qaJlOrZzuwI9GPVudIHwMdwujAYuGQ6UzdFCmMBQdmLKZW7TKwAMHTF-0XPVNsRmy3A3-z0axF-oqPneSGu_gzdacK555zjCFVIEMzOUMIUo59JH2TI7yyK5l9KkiTAdnS7BuhnWGYbjt6RT3Xm6rZ4dGxETLtd4RCbZoRKU9wSp68ViIu9w6CZf18e_OeX-W3vEl__3_Agg8ZSiLt30NiDn1G86EzomOsKIi6GS9hAGXKCxuw2VYd33Pdn8WIOc4CNXnIq_amM3IcrC_3nUEDR_C_ohBc80t24xt3YQi7yxsnAC3Su5LbKrxmqiSzVB5YwkYmK2tNSaaAYXHC4GtAvB_IdTq2V8j2OxT6odOAL6udQhPRkbHlz90vTqPBZPWuqUEGXWiD3br4KPX5BqGvIPOf9cCN57QJzUngpRgTXZVKVD83_jvcb9DOvoHyix1pwIBdFVKB3Pkzy0>`_

Figure :ref:`fig_eudiw_national_registry_relationships` shows instead the mapping between the EUDIW catalogues and the national counterparts:

- **EUDIW Catalogue of Attributes** corresponds to the national **Claims Registry** for the semantic definition of the attributes and to the **Authentic Source Registry** for the discovery of the verification point. Note that national attribute definitions align to the EU-level catalogue for cross-border interoperability.
- **EUDIW Catalogue of Schemes** corresponds to the national **Schema Registry** for the discovery of the attestation schemes and to the **Digital Credentials Catalog** for the discovery of the issuance and presentation requirements. Note that the national registries contain all the information provided in the EUDIW one plus additional information (e.g., pricing model and validity information).

.. _fig_eudiw_national_registry_relationships:
.. plantuml:: plantuml/eudiw-national-registry-relationships.puml
    :width: 99%
    :alt: The figure illustrates the relationships between National Registries and EUDIW Catalogues.
    :caption: `Relationships between National Registries and EUDIW Catalogues <https://www.plantuml.com/plantuml/svg/bL9DRnCn4BtxLmm1YI8QHOHoer7BfeTS46f0712Afkj9OiaVmH-AAjJ_pcIJBXEBY7OFQy-RcUVtxBbA6MCkpgeNnhUsQ8AFpSMekLWqmMs29vydIhs6AIsD9vX_kPrzlPcBubmsgEFxKHkS2txoZymo-3p4BQNWQFXXf37Z7IPYsa-XU8tn_inZDi6ZNKHQcPJZ_JaCFXymk3rWCFFBYBmhRIwH1c_Wj-f5dc6IpTSbhnarBSn3YItr98DpU9KsqMIw71oKC9FWQIqQ9wcQ7P2UJh2n9RtZlhT7Q6hNv53opZla6S8Oj65LY7kdPcKuWYQItjb4cw1vp3z9uVYWy4691FqgQ7VQBpbJmUCzB1wDYZPRwUZcstJs_Q-ELB_GGbheoo0iuJhdQEvAflHVyUaqItUZ9oaUrBErxtg4QXZ2_eRKVk7uU5hKSSZvRXXKz-T8p2XKp3fi_O-NspMh_ZcSW71PazQbrMGfJAThUzBUGLNGmMEbL9BY7k7zmd5zfeY5yN5ddEl5kVnTaTV5sJy0>`_

.. note::
  As specified in `EIDAS-ARF`_, the registration of an attestation scheme in the EUDIW Catalogue of Schemes does not create any obligation for acceptance of the relevant type of attestation by any actor in the EUDI Wallet ecosystem. Neither does it automatically imply cross-border recognition of the type of attestation. It is used to discover the corresponding trust framework.

Registry Infrastructure Usage Journeys
--------------------------------------

The components of the Registry Infrastructure are designed to support various operational phases of the IT-Wallet ecosystem, each involving specific interactions between entities.
The main Journeys below illustrate the operational interactions that read the Registry Infrastructure.
The complementary journey that populates the registries is the onboarding registration, which registers the entities, the Authentic Sources, the claims, the schemas and the Credential types, as shown in Figure :ref:`fig_registry_infrastructure` and described in :ref:`onboarding-system:Onboarding Processes`.

Catalog Browsing
^^^^^^^^^^^^^^^^

This *Catalog Browsing* journey supports Users (both human users via a **Wallet Instance** and automated systems like **Relying Parties** or web portals) in discovering and selecting available Digital Credentials.

1.  **Accessing the Discovery Endpoint**: The entity (e.g., a Wallet Provider or informational portal) accesses the `Registry Discovery Endpoint` (``.well-known/it-wallet-registry``) to obtain the URI of the **Digital Credentials Catalog** and of the **Taxonomy**.

2.  **Navigation and Selection**:

    * **Credential Discovery**: The entity browses the list of Credentials (``credentials`` field) to identify relevant Credential types (e.g., ``pid``, ``eid``, ``mDL``) and, if needed, uses the information on the **Taxonomy** to navigate their hierarchy and to provide different localizations.
    * **Issuer Metadata**: The entity extracts the Credential Issuer Metadata (see :ref:`credential-issuer-solution:Metadata for openid_credential_issuer`) as described in Section 12.2.2 of `OpenID4VCI`_.
    * **Detail Consultation**: To obtain complete information and specific technical requirements, the entity accesses the **Entity Configuration** using the retrieved identifier.

3.  **Final Action**: The entity can then use the metadata to display the catalog information to a User, or use it in other ways.

Credential Issuance
^^^^^^^^^^^^^^^^^^^

This journey defines how a Credential Issuer uses the Registry Infrastructure to prepare and issue a compliant Digital Credential.

1.  **Identifying Requirements**: The Credential Issuer consults the **Digital Credentials Catalog** for the technical requirements of the Credential type to be issued (e.g., ``max_validity_days``, ``min_loa``).

2.  **Schema and Claim Resolution**:

  The Credential Issuer consults:

    * EUDIW Catalogue of Schemes to obtain the schema of the sought EUDIW-anchored Digital Credential (``schemaURIs``), or
    * :ref:`registry:Schema Registry` to obtain the schema of the sought National-anchored Digital Credential (``schema_uri``).

  and, in both cases, verifies its integrity. Then, depending on the Trust Framework anchoring the Digital Credential, it accesses the EUDIW Catalogue of Attributes or :ref:`registry:Claims Registry` to retrieve the standardized semantic definitions and data formats of the necessary attributes (claims).

3.  **Authentic Data Retrieval**:

  * The Credential Issuer consults the **Authentic Source (AS) Registry** to identify the authorized **Authentic Source** (AS) for the required dataset. The AS Registry provides the AS's ``entity_id`` and the technical details of the interface (`integration_endpoint`, `integration_method`).
  * The Credential Issuer consults the AS endpoint specification to implement the integration needed to retrieve the User data required to populate the Digital Credential.

4.  **Credential Issuance**: The Credential Issuer uses the retrieved data, validated schemas, and specified formats to generate and sign the Digital Credential in the correct format (e.g., SD-JWT or mDOC).

Credential Presentation and Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This journey describes how a **Wallet Instance** and a **Relying Party (RP)** interact with the Registry Infrastructure when a Digital Credential needs to be presented by a User.

1.  **Wallet Unit Authorization and Selection**:

  * The Wallet Unit receives a Presentation Request from the RP. The Wallet Unit MUST evaluate trust with the RP issuing the Presentation Request as follows:

    * **(EUDIW Trust Framework)**:

      * The Wallet Unit validates the Presentation Request signature and evaluates trust with the Relying Party producing it as described in :ref:`trust-evaluation:EUDIW Authentication`.
      * The Wallet Unit validates whether the RP is entitled to this presentation as described in :ref:`trust-evaluation:EUDIW Authorization`.

    * **(National Trust Framework)**:

      * The Wallet Unit validates the Presentation Request signature and evaluates trust with the Relying Party producing it as described in :ref:`trust-evaluation:Authentication`.
      * The Wallet Unit validates whether the RP is entitled to this presentation as described in :ref:`trust-evaluation:Authorization`.

   Regardless of the Trust Framework, the final decision on whether the RP is Authorized during presentation is made according to :ref:`trust-evaluation:Authorization Decision and Override Rules`.

  * The User authorizes the release of the selected, selectively disclosed attributes. The Wallet then packages and presents the Digital Credential to the RP.

2.  **Discovery and Integrity**:

  * The RP receives the Digital Credential from the User.
  * Depending on the trust framework the RP subscribes to (i.e., the National or EUDIW Trust Framework):

    * **(EUDIW Trust Framework)**:

      * The RP validates the Digital Credential signature and evaluates trust with its issuer as described in :ref:`trust-evaluation:EUDIW Attestation Signature Validation`.
      * The RP consults the EUDIW Catalogue of Schemes to download the schema of the presented Credential (`schema_uri`), verifying its integrity (`schema_uri#integrity`).

    * **(National Trust Framework)**:

      * The RP validates the Digital Credential signature and evaluates trust with its issuer as described in :ref:`trust-evaluation:Signing Trust Anchor Validation Procedure`.
      * The RP consults the :ref:`registry:Schema Registry` to download the schema of the presented Credential (`schema_uri`), verifying its integrity (`schema_uri#integrity`).

3.  **Schema and Final Policy Validation**:

  * The RP uses the retrieved schema to validate the structure of the Credential and the data types of the revealed attributes.
  * The RP performs the final check to ensure that the attributes presented comply with the specific requirements of the initial request and authorization policy.

4.  **Acceptance or Rejection**: Based on cryptographic validation, schema compliance, and policy-based authorization, the RP accepts or rejects the Digital Credential for service access.

Cross-border Attribute Verification by a QTSP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This journey describes how a Qualified Trust Service Provider (QTSP), possibly established in another Member State, verifies the value of an Annex VI attribute against an Italian public-sector Authentic Source to issue a QEAA.
It exercises the EUDIW Catalogue of Attributes and the ``verification_endpoint`` of the :ref:`registry:Authentic Source Registry`, and it does not use the national OpenID Federation trust evaluation nor the domestic PDND e-Service.

1.  **Verification-point discovery**: The QTSP queries the EUDIW Catalogue of Attributes for the required attribute and resolves the responsible Italian ``Attribute`` entry, obtaining the ``authenticSources[].DataService.endpointURL`` (the ETSI TS 119 478 verification interface declared in the AS Registry ``verification_endpoint``), the ``legalBasis`` and the description of how to initiate the verification request. The national counterpart of the Catalogue of Attributes is the pair Claims Registry, for the semantics, and Authentic Source Registry, for the verification point, see :ref:`registry:Registry Integration and Cross-References`.

2.  **Interface selection**: Depending on ``verification_endpoint.method``, the QTSP uses the ISO 15000/eDelivery interface (``oots_edelivery``) or the REST + OAuth 2.0 interface (``rest_oauth2``) of ETSI TS 119 478 Section 6.

3.  **Verification request**: The QTSP submits the verification request to the endpoint, exposed by the Authentic Source or by the designated national intermediary, which returns the authentic confirmation of the attribute value for the User. As foreseen by Article 45e of [`EIDAS`_], this is an authenticity verification of the attribute and not an access to the underlying data.

4.  **Issuance**: The QTSP issues the QEAA under its own Rulebook and trust anchors, that is the EUDIW Trusted Lists. The trust anchoring of the resulting QEAA does not derive from the presence of any scheme in the Catalogue of Schemes, see the note in :ref:`registry:Registry Integration and Cross-References`.
