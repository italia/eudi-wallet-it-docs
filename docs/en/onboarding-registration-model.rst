.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '-' (level 1).

Registration Model
------------------

This section provides the static view of the registration with the aim of defining the information each entity has to provide, which conditions it has to meet and which artifacts and registry entries it obtains.
It is organized as a common part and a profile for each role.

Registration Data Model
^^^^^^^^^^^^^^^^^^^^^^^

This section defines the complete set of the data the entities provide to the Onboarding System, together with the data that defines a Credential type, with its semantics and, where applicable, its normative reference.
The data is identified by a format-agnostic **Data Identifier**.

The following tables provide:

- *Base registration data* provided by every entity, whatever its role.
- *Extended registration data* provided by an entity depending on its role, where each :ref:`onboarding-system:Registration Profiles` instance specifies which extended data the role provides and how the entity populates it.
- *Credential type definition data* that describes a Credential type.

Depending on the role, the registration data is then encoded in a different data model, the ``WalletRelyingParty`` schema of the Register for a Wallet-Relying Party (:ref:`infrastructure-trust:Register of WRPs`), the entry of the AS Registry for an Authentic Source (:ref:`registry:Authentic Source Registry`), and the notification dataset for a notifiable Entity.
The Credential type definition data is encoded in the versioned entry of the Digital Credentials Catalog (:ref:`registry:Digital Credentials Catalog`).
The mapping to the destination data models is given in :ref:`onboarding-system:Mapping to the Registry Data Models`.

.. list-table:: Base Registration Data
   :class: longtable
   :widths: 26 46 28
   :header-rows: 1

   * - **Data Identifier**
     - **Description**
     - **Normative reference**
   * - `legal_name`
     - The name of the organization as it appears in the official records.
     - [`CIR2025/848`_], Annex I
   * - `identifier`
     - One or more official identifiers of the organization. Within IT-Wallet the Value Added Tax Identification Number (VATIN) is REQUIRED for every entity, and a public body additionally MUST provide its national identifier of type ``NTR``, valued with its IPA code, that is the code of the Italian Index of Public Administrations. An organization that has a European Unique Identifier (EUID) MUST provide it. The other identifier types of Table 2, such as Legal Entity Identifier (LEI), are OPTIONAL and are not supported in the current version. For more details refer to the syntax of the ``organizationIdentifier`` defined in clause 5.1.4 of [`ETSI EN 319 412-1`_].
     - [`ETSI TS 119 475`_], Table 2
   * - `legal_nature`
     - Whether the entity is a public sector body or a private entity.
     - [`CIR2025/848`_], Annex I
   * - `contact_information`
     - The postal address, the information web page and the contacts of the organization. The contacts include at least an institutional contact for the administrative communications, for which a certified electronic mail address (PEC) is RECOMMENDED, and a technical contact for the user support of the service.
     - [`CIR2025/848`_], Annex I
   * - `service_policies`
     - The terms and conditions and the privacy policy of the service, each published at its own URL.
     - [`CIR2025/848`_], Annex I
   * - `data_protection_authority`
     - The authority contact email competent for the supervision of the entity under the data-protection law. It MUST be provided for each intended use of the Wallet-Relying Party.
     - [`CIR2025/848`_], Annex I, in compliance with Regulation (EU) 2016/679.

The extended registration data is provided in the table below.
A given entity provides only the subset that applies to its role, as defined in the corresponding profile in :ref:`onboarding-system:Registration Profiles`.

.. list-table:: Extended Registration Data
   :class: longtable
   :widths: 26 46 28
   :header-rows: 1

   * - **Data Identifier**
     - **Description**
     - **Normative reference**
   * - `entitlements`
     - The entitlements the entity requests, which state the roles it intends to play in the ecosystem.
     - [`ETSI TS 119 475`_], Annex A.2
   * - `service_description`
     - The trade name and the localized description of the service, provided by the entities that offer a service to the Wallet Units.
     - [`CIR2025/848`_], Annex I
   * - `intended_use`
     - The attributes a Relying Party intends to request from the Wallet Units. 
     - [`CIR2025/848`_], Annex I
   * - `provided_attestations`
     - The Attestation types a Credential Issuer intends to issue. Within IT-Wallet each of them references a versioned entry already present in the Digital Credentials Catalog, and the declaration adds the Credential Issuer to the ``issuers`` field of that entry, together with the issuance capabilities offered for that Credential type (the supported issuance flows, the parameters of the deferred issuance and the documentation of the issuance service), see :ref:`registry:Digital Credentials Catalog`.
     - [`CIR2025/848`_], Annex I
   * - `intermediary_relationship`
     - For a Relying Party Intermediary, the declaration that it acts as an intermediary. For an intermediated Relying Party, the reference to the Intermediary it uses.
     - [`ETSI TS 119 475`_], Table 10
   * - `trust_framework_scope`
     - The declaration of the Trust Framework in which the entity intends to operate (the EUDIW Trust Framework for the cross-border operation or the National Trust Framework alone). It is provided by the roles for which this choice is not already fixed by the notification, and it determines the Trust Artifacts the entity obtains and the way the other Data Identifiers of the profile are provided, see :ref:`infrastructure-trust:Overview`. It applies to the entity, while ``trustedAuthorities`` of a Credential type applies to the validation of an Attestation of that type.
     - This specification
   * - `federation_entity_identifier`
     - The identifier of the Federation Entity in the National Trust Framework, that is the ``iss`` and ``sub`` of its Entity Configuration.
     - `OID-FED`_, Section 3
   * - `federation_entity_key`
     - The public key with which the Federation Entity signs its Entity Configuration. It MUST be provided in JWK format. The rest of the federation configuration is published in the Entity Configuration reachable at the ``.well-known/openid-federation`` endpoint.
     - `OID-FED`_, Section 3
   * - `certificate_signing_requests`
     - An array of Certificate Signing Requests in PKCS #10 format, one for each X.509 certificate the entity needs to obtain, that is, depending on the role, the WRPAC, the Sign/Seal Certificate or the National Authentication Certificate. Each request carries the public key to be certified. It MUST be distinct from the Federation Entity Key. Their profile is defined in :ref:`onboarding-system:Certificate Signing Request Profile` and they are the input of the :ref:`onboarding-system:Certificate and Trust Artifact Issuance`, where they are presented in the ACME order.
     - :rfc:`2986`
   * - `provided_claims_purposes`
     - The claims composing an Attestation, selected from the Claims Registry, and the purposes it uses, selected from the Taxonomy, together with the data-provision capabilities. It groups the ``data_capabilities`` of the AS Registry entry, see :ref:`registry:Authentic Source Registry`.
     - This specification
   * - `visual_identity`
     - The visual assets of an Authentic Source, that is the logo of the organization and the logo and the background color associated with a provided dataset, each with its integrity digest and its alternative text.
     - This specification
   * - `conformity_assessment`
     - The outcome of the conformity assessment of the entity, such as the Conformity Assessment Report or the assessments performed under the National certification scheme operated by the Italian National Cybersecurity Agency (ACN) and the functional testing under the EU functional conformity assessment framework (FCAF). It MUST be provided by the notified categories.
     - [`EIDAS-ARF`_], Annex 2
   * - `service_supply_point`
     - The URL at which a Wallet Unit starts the process of requesting and obtaining an Attestation from the Issuer. It MUST be provided by the notified categories that issue an Attestation requested by the Wallet Unit.
     - [`EIDAS-ARF`_], Annex 2
   * - `signing_trust_anchor`
     - The trust anchor supporting the validation of the Attestations the entity issues, that is the public key and the name. It MUST be provided as an input only by the categories whose Sign/Seal Certificate is not issued by the National Root Certification Authority, see :ref:`infrastructure-trust:PKI Architecture`. For the other categories the trust anchor derives from the Sign/Seal Certificate issued through the Certificate Signing Requests.
     - [`EIDAS-ARF`_], Annex 2
   * - `verification_endpoint`
     - The cross-border verification interface exposed to Qualified Trust Service Providers for the Annex VI attributes exported to the EUDIW Catalogue of Attributes, conformant to ETSI TS 119 478 and declared in the ``data_capabilities`` of the entry of the Authentic Source Registry, see :ref:`registry:Authentic Source Registry`. It is provided by the Authentic Source.
     - [`EUDI-TS 11`_], Section 2.1

The data below defines a Credential type and not an entity.
For this reason it is not registration data, it does not follow a profile of :ref:`onboarding-system:Registration Profiles`, and it is the input of the :ref:`onboarding-system:Credential Type Registration`.
It is provided by the Attestation Scheme Provider, which owns the Attestation Rulebook of the Credential type, and it is taken from the Rulebook itself.
The same criterion applies to the definition of a claim, registered through the :ref:`onboarding-system:Claim Registration`.

.. list-table:: Credential Type Definition Data
   :class: longtable
   :widths: 26 46 28
   :header-rows: 1

   * - **Data Identifier**
     - **Description**
     - **Normative reference**
   * - `credential_type_declaration`
     - The Credential type, anchored to its Rulebook. It creates the versioned entry of the Digital Credentials Catalog and it groups the Digital Credential Metadata of the type (the unique identifier and the version, the human-readable name, the classification by domains and classes, the User authentication methods and the minimum Level of Assurance), together with the reference to the Authentic Sources, or to the parent Credential types, that provide its data, see :ref:`registry:Digital Credentials Catalog`.
     - [`CIR2025/848`_], Annex I
   * - `credential_technical_specification`
     - Technical definition of a Credential type, that groups the Technical Specification fields of the Digital Credentials Catalog, that is the Credential schemes, the Credential formats and the authentication policy, see :ref:`registry:Digital Credentials Catalog`.
     - [`CIR2025/848`_], Annex I
   * - `credential_policies`
     - Conditions of use of a Credential type, that group the Terms of Use fields of the Digital Credentials Catalog, that is the Credential validity, the restriction policy, the pricing policy and the Credential purposes, see :ref:`registry:Digital Credentials Catalog`.
     - [`CIR2025/848`_], Annex I
   * - `trustedAuthorities`
     - The trusted authorities that define the trust framework of the Credential type in the Digital Credentials Catalog, that is the trust anchors a verifier relies on to validate the Attestation, see :ref:`registry:Digital Credentials Catalog`.
     - [`EUDI-TS 11`_], Section 4.3
   * - `rulebookURI`
     - The URI of the human-readable Attestation Rulebook that defines the non-machine-readable aspects of the Credential type in the Digital Credentials Catalog, see :ref:`registry:Digital Credentials Catalog`.
     - [`EUDI-TS 11`_], Section 4.3
   * - `bindingType`
     - The type of cryptographic key binding required for the issuance of the Credential type in the Digital Credentials Catalog, one of ``claim``, ``key``, ``biometric`` or ``none``, see :ref:`registry:Digital Credentials Catalog`.
     - [`EUDI-TS 11`_], Section 4.3
   * - `attestationLoS`
     - The attestation Level of Security of the Credential type in the Digital Credentials Catalog, that is the attack potential resistance required for user authentication and key storage, see :ref:`registry:Digital Credentials Catalog`.
     - [`EUDI-TS 11`_], Section 4.3

.. note::
   The `provided_attestations` remains part of the registration data of a Credential Issuer, because it is the declaration of the Credential types the Credential Issuer intends to issue and not the definition of those types.
   The two are distinct: the definition creates the versioned entry, the declaration adds the Credential Issuer to its ``issuers`` field.

Mapping to the Registry Data Models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Onboarding System collects the registration data and the Credential type definition data, and they are then encoded in the data model of the destination, that for the registration data depends on the role.
The table below maps each Data Identifier to the fields of the destination data models, for the Data Identifiers whose mapping is not one-to-one with a single field.

.. list-table:: Mapping of the Data Identifiers to the destination data models
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Data Identifier**
     - **Destination fields**
   * - `legal_name`
     - In the Register, the ``legalName`` of the ``legalPerson``. In the AS Registry, the ``organization_name_l10n_id``. In the registration Trust Mark, the ``organization_name``. In the Digital Credentials Catalog, the ``organization_name_l10n_id`` of the ``issuers`` element of the Credential Issuer.
   * - `identifier`
     - In the Register, the ``identifier`` array, each element carrying its ``type`` and its value. In the registration Trust Mark, the ``vat_number`` for a private entity, the ``ipa_code`` for a public body and the ``legal_identifier``. In the Digital Credentials Catalog, the ``organization_code`` of the ``issuers`` element of the Credential Issuer.
   * - `legal_nature`
     - In the Register, the ``isPSB`` flag. In the AS Registry, the ``organization_type``. In the registration Trust Mark, the ``public_body``.
   * - `contact_information`
     - In the Register: 
     
         - ``postalAddress``, 
         - ``email``,
         - ``phone``,
         - ``infoURI``,
         - ``supportURI``. 
       
       In the AS Registry: 
         
         - ``contacts``, 
         - ``homepage_uri``.
       
       In the registration Trust Mark, the ``email`` and the ``support_uri``. In the Entity Configuration, the ``contacts`` and the ``homepage_uri`` of the ``federation_entity`` metadata. In the Digital Credentials Catalog, the ``contacts`` and the ``homepage_uri`` of the ``issuers`` element of the Credential Issuer.
   * - `service_policies`
     - In the Register, the ``policyURI`` of each element of the ``policy`` array, distinguished by its ``type``. In the registration Trust Mark, the ``privacy_policy``. In the Entity Configuration, the ``policy_uri`` and the ``tos_uri`` of the ``federation_entity`` metadata. In the Digital Credentials Catalog, the ``policy_uri`` and the ``tos_uri`` of the ``issuers`` element of the Credential Issuer.
   * - `data_protection_authority`
     - In the Register, the ``supervisoryAuthority``. In the AS Registry, the ``dpa_contact``. In the registration Trust Mark, the ``supervisory_authority``.
   * - `entitlements`
     - In the Register, the ``entitlement``. In the registration Trust Mark, the ``entitlements``. In the Digital Credentials Catalog, the ``legal_type`` of the ``issuers`` element of the Credential Issuer.
   * - `service_description`
     - In the Register, the ``tradeName`` and the ``srvDescription``. In the registration Trust Mark, the ``srv_description``.
   * - `intended_use`
     - In the Register, the ``intendedUse`` array, each element carrying its ``intendedUseIdentifier``, ``purpose``, ``privacyPolicy`` and ``credential``. In the registration Trust Mark, the ``credentials`` and the ``purpose``.
   * - `provided_attestations`
     - In the Register, the ``providesAttestations``. In the registration Trust Mark, the ``provides_attestations``. In the Digital Credentials Catalog, the element of the ``issuers`` array of each declared Credential type, including its ``issuance_flows`` and its ``service_documentation_uri``.
   * - `provided_claims_purposes`
     - In the AS Registry, the ``data_capabilities``, that is 
     
         - ``available_claims``, 
         - ``intended_purposes``, 
         - ``integration_method``, 
         - ``integration_endpoint``, 
         - ``api_specification``, 
         - ``data_provision``, 
         - ``update_frequency``, 
         - ``service_documentation_uri``.
   * - `visual_identity`
     - In the AS Registry the 
     
         - ``logo_uri`` of the ``organization_info``,
         - ``background_color`` of the ``data_capabilities``, 
       
       each with its integrity digest and its alternative text.
   * - `credential_type_declaration`
     - In the Digital Credentials Catalog: 
     
         - ``credential_type``, 
         - ``version``, 
         - ``credential_name_l10n_id``, 
         - ``domains``, 
         - ``classes``, 
         - ``authentication``,
       
       and the ``authentic_sources``, or the ``parent_credentials``, that provide the data of the Credential type.
   * - `credential_technical_specification`
     - In the Digital Credentials Catalog:
     
         - ``schema_uri``, 
         - ``format``, 
         - ``vct``,
         - ``docType``.
   * - `credential_policies`
     - In the Digital Credentials Catalog:
     
         - ``validity_info``, 
         - ``restriction_policy``, 
         - ``pricing_policy``, 
         - ``purposes``, 
         - ``legal_type``.
   * - `conformity_assessment`
     - In the notification dataset, the conformity assessment report.
   * - `service_supply_point`
     - In the notification dataset, the service supply point.
   * - `signing_trust_anchor`
     - In the notification dataset, the trust anchor.

Some information are present both in the registered data and in the self-signed Entity Configuration of the Entity.
The registered value is authoritative, asserted by the Registrar in the Register and by the Federation Trust Anchor in the registration Trust Mark, while the informational parameters of the ``federation_entity`` metadata are published under the responsibility of the Entity.
Where the Onboarding System requires a value that the Entity also publishes in its Entity Configuration, it MUST read the Entity Configuration and MUST verify the match. A mismatch MUST block the registration, and after the registration it MUST be solved through an :ref:`onboarding-system:Entity Update`.
Within IT-Wallet the ``metadata_policy`` of the Subordinate Statement fixes the ``organization_name`` of the ``federation_entity`` metadata to the registered value, so the name shown to the User cannot diverge from the one carried by the WRPAC and by the WRPRC. The other informational parameters are not fixed.

Eligibility and Compliance Preconditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before any technical registration, the eligibility and the compliance of an entity MUST be verified by the Supervisory Body, which relies on the Registrar for the entities it registers and, for the notified categories, acts as the National point of contact toward the European Commission.
Where a National and an EUDIW obligation overlap, the EUDIW obligation is authoritative.

The verification applies to Authentic Sources, Wallet Providers and Wallet-Relying Parties, and its content depends on the role.

  - **Authentic Sources**: the Supervisory Body validates the legal standing and the data authority of the organization and classifies it as public or private.
    The trust of an Authentic Source is governed by the PDND framework and it is out of EUDIW and National Trust Frameworks.
  - **Wallet Providers**: the eligibility is established and the conformity assessment of the Wallet Solution is driven.
    The assessment covers the security of the wallet architecture, its data-protection mechanisms and its user-privacy features, and it is the precondition for the Wallet Solution to be certified.
    The certification of the Wallet Solution is an external process, and this phase uses its outcome as an input.
    The certification follows the National certification scheme operated by the Italian National Cybersecurity Agency (ACN), and the functional testing follows the EU functional conformity assessment framework (FCAF).
  - **PID Providers**: validated per National designation as providers of Person Identification Data, subject to the National certification scheme operated by the Italian National Cybersecurity Agency (ACN), and to the functional testing under the EU functional conformity assessment framework (FCAF).
  - **QEAA Providers**: validated through the qualification and the supervision of the issuing Qualified Trust Service Provider.
  - **PuB-EAA Providers**: validated through the conformity assessment required by Article 45f of the eIDAS2 Regulation.
  - **Non-qualified EAA Providers**: validated for the eligibility to issue.
    Their trust anchor is distributed through the National Trust Framework and it is defined in the applicable Attestation Rulebook.
  - **Relying Parties**: the Supervisory Body performs a policy-based authorization, evaluating the organizational type, that is public administration or private entity, the business-sector classification, and the legitimate requirements of the service.
  - **Relying Party Intermediaries**: additionally demonstrate their eligibility to act on behalf of Relying Parties, pursuant to Article 5b(8) of the eIDAS2 Regulation ([`EU_2024_1183`_]).
  
  .. note::
   The Credential Issuer declares the Credential types it intends to issue, each anchored to its Rulebook, and its integration with the relevant Authentic Sources is authorized where needed.

The Supervisory Body also approves the claims, the schemas and the Credential types before they are registered in the registries, and that approval is a precondition of the :ref:`onboarding-system:Claim Registration`, of the :ref:`onboarding-system:Schema Provisioning` and of the :ref:`onboarding-system:Credential Type Registration`.

The identity proofing of the Wallet-Relying Parties MUST be carried out by the Registrar according to [`ETSI TS 119 461`_], and the verification of the entitlements MUST follow Annex III of [`CIR2025/848`_].
Within IT-Wallet the identity proofing is applied to every entity that onboards, including the entities that do not operate in the EUDIW Trust Framework, even where it is not strictly required for them.

For the notified entities the certifications are a mandatory input to the onboarding, and in every case the eligibility and compliance verification is a mandatory precondition for the technical registration.


Trust Artifacts Registration Outcomes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A successful registration produces, depending on the role and on the scope of operation, the entry in the Register and the Trust Artifacts. For the notified categories, the entry in a List of Trusted Entities follows from the :ref:`onboarding-system:Notification and Publication`, which is a separate process.
The way each artifact is produced is described in :ref:`onboarding-system:Onboarding Processes`, and the effects of the later changes in :ref:`onboarding-system:Events, Registries and Trust Artifacts`.

The table shows the artifacts that vary by role.
The X.509 certificate column groups the X.509 certificates the entity obtains, in particular the WRPAC, the Sign/Seal Certificate and the national Authentication Certificate, while the WRPRC is shown on its own because it is not an X.509 certificate but a JSON Web Token or a CBOR Web Token.

.. list-table:: Trust Artifacts Registration Outcomes by Entity Type
   :class: longtable
   :widths: 20 12 10 34 24
   :header-rows: 1

   * - **Entity type**
     - **Register record**
     - **WRPRC**
     - **X.509 certificate**
     - **LoTE entry**
   * - PID Provider
     - yes
     - yes
     - the WRPAC, and the Sign/Seal Certificate
     - PID Providers LoTE
   * - QEAA Provider
     - yes
     - yes
     - the WRPAC. The Sign/Seal Certificate is the qualified certificate issued by the QTSP
     - EUMS TL, referenced in the LOTL
   * - PuB-EAA Provider
     - yes
     - yes
     - the WRPAC. The Sign/Seal Certificate is the qualified certificate issued by the QTSP
     - PuB-EAA Providers LoTE
   * - Non-qualified EAA Provider
     - yes only if it issues an Attestation published in a EU Rulebook
     - yes only if it issues an Attestation published in a EU Rulebook
     - the WRPAC only if it issues an Attestation published in a EU Rulebook, and the Sign/Seal Certificate
     - None, trust anchor distribution defined in the applicable Attestation Rulebook
   * - Relying Party
     - yes, only for RP operating in EUDIW
     - yes, only for RP operating in EUDIW
     - the WRPAC if it has a register record, and the Authentication Certificate where the RP has no register record and it operates in the Proximity Flow
     - None
   * - Relying Party Intermediary
     - yes
     - No
     - the WRPAC
     - None
   * - Wallet Provider
     - no
     - no
     - the Sign/Seal Certificate
     - Wallet Providers LoTE

.. note::
   The federation registration is common to every entity and, as a result of it, every entity obtains a Subordinate Statement issued by its Federation Authority, and a registration Trust Mark.

.. note::
   An entity operating only at national level obtains no Register record, no WRPAC and no WRPRC.
   It holds its Entity Statement and its registration Trust Mark from the federation registration, and, where its role requires it, its X.509 certificate, that is the Sign/Seal Certificate for a National Credential Issuer or the Authentication Certificate for a Relying Party operating in the Proximity Flow.

Registration Profiles
^^^^^^^^^^^^^^^^^^^^^

This Section describes the registration of each role as a profile.
Every profile provides the base registration data defined in :ref:`onboarding-system:Registration Data Model`, and each profile below states only the extended registration data the role provides and how the entity populates it, together with any specialization of the base data.
An entity can hold more than one entitlement in a single registration record and for more than one role, so the profiles are not mutually exclusive and they compose.
For example, an entity can be at the same time a Relying Party and a QEAA Provider, and in that case its input is the union of the two profiles and its outcome is the union of the two.

.. note::
   The definition of a Credential type is not part of any registration profile, as described in :ref:`onboarding-system:Registration Data Model`.
   It is provided by the Attestation Scheme Provider, see :ref:`onboarding-system:System Actors and Roles`, through the :ref:`onboarding-system:Credential Type Registration`.

PID Provider
""""""""""""

A PID Provider is a Federation Entity that is notified and registered in the EUDIW Trust Framework, and its Sign/Seal trust anchor is published in the PID Providers LoTE.
In addition to the base registration data, a PID Provider provides the following extended registration data, as defined in :ref:`onboarding-system:Registration Data Model`:

- `entitlements`
- `service_description`
- `provided_attestations`
- `federation_entity_identifier`
- `federation_entity_key`
- `certificate_signing_requests`

  - One Certificate Signing Request for the WRPAC, with which the PID Provider authenticates towards the Wallet Units.
  - One Certificate Signing Request for the Sign/Seal Certificate, with which it signs the issued PID.
- `conformity_assessment`
- `service_supply_point`


QEAA Provider
"""""""""""""

A QEAA Provider is a Federation Entity that issues Qualified Electronic Attestations of Attributes, and its Sign/Seal Certificate is the qualified certificate issued by the Qualified Trust Service Provider it belongs to.
In addition to the base registration data, a QEAA Provider provides the following extended registration data, as defined in :ref:`onboarding-system:Registration Data Model`:

- `entitlements`
- `service_description`
- `provided_attestations`
- `federation_entity_identifier`
- `federation_entity_key`
- `certificate_signing_requests`

  - One Certificate Signing Request for the WRPAC, with which the QEAA Provider authenticates towards the Wallet Units.
- `conformity_assessment`
- `service_supply_point`
- `signing_trust_anchor`

  - Provided as an input because the Qualified Certification Authority of the QEAA Provider is not subordinate to the National Root Certification Authority but belongs to the perimeter of a Qualified Trust Service Provider.


PuB-EAA Provider
""""""""""""""""

A PuB-EAA Provider is a Federation Entity that is notified and registered in the EUDIW Trust Framework, and its Sign/Seal trust anchor is published in the PuB-EAA Providers LoTE.
In addition to the base registration data, a PuB-EAA Provider provides the following extended registration data, as defined in :ref:`onboarding-system:Registration Data Model`:

- `entitlements`
- `service_description`
- `provided_attestations`
- `federation_entity_identifier`
- `federation_entity_key`
- `certificate_signing_requests`

  - One Certificate Signing Request for the WRPAC, with which the PuB-EAA Provider authenticates towards the Wallet Units.
- `conformity_assessment`:

  - The Conformity Assessment Report issued by a Conformity Assessment Body under Article 45f of [`EIDAS`_].
- `service_supply_point`
- `signing_trust_anchor`

  - Provided as an input because the Qualified Certification Authority of the PuB-EAA Provider is not subordinate to the National Root Certification Authority but belongs to the perimeter of a Qualified Trust Service Provider.


Non-Qualified EAA Provider
""""""""""""""""""""""""""

In addition to the base registration data, a Non-Qualified EAA Provider provides the following extended registration data, as defined in :ref:`onboarding-system:Registration Data Model`:

- `entitlements`
- `service_description`
- `provided_attestations`
- `federation_entity_identifier`
- `federation_entity_key`
- `certificate_signing_requests`

  - One Certificate Signing Request for the Sign/Seal Certificate, with which the Non-Qualified EAA Provider signs the issued EAA.
  - A Non-Qualified EAA Provider that operates in the EUDIW Trust Framework additionally provides one Certificate Signing Request for the WRPAC, with which it authenticates towards the Wallet Units.
- `service_supply_point`
- `trust_framework_scope`
  
  - A Non-Qualified EAA Provider declares, at onboarding, whether it operates in the EUDIW Trust Framework or only within the national boundary, and this choice affects the artifacts it obtains, as described in :ref:`infrastructure-trust:Infrastructure of Trust`. A Non-Qualified EAA Provider that operates in the EUDIW Trust Framework obtains the Register record, the WRPAC and the Sign/Seal Certificate, while a Non-Qualified EAA Provider that operates only within the national boundary obtains the Sign/Seal Certificate alone, is authenticated by the Wallet Unit through the National Trust Framework, and its Attestations are validated against the trust anchor distributed by the Entity Configuration of the Federation TA. The IT-Wallet ID, the national-scope Electronic Attestation of Person Identification Data, is an example of an Attestation issued by a Non-Qualified EAA Provider that operates within the national boundary, see :ref:`credential-data-model-it-wallet-id:IT-Wallet ID Data Model` and :term:`IT-Wallet ID`. It is an EAA and MUST NOT be confused with the EUDI Person Identification Data, which is not an EAA.


Relying Party
"""""""""""""

Besides the base registration data, a Relying Party provides the following extended registration data, as defined in :ref:`onboarding-system:Registration Data Model`:

- `entitlements`
- `service_description`
- `intended_use`:

  - The Attestation type and optionally attributes the Relying Party intends to request from the Wallet Units, with one intended-use definition per service.
- `intermediary_relationship`

  - In the EUDIW Trust Framework, REQUIRED where the Relying Party operates through a RP Intermediary, and in that case it references its RP Intermediary identifier. In the National Trust Framework the Relying Party does not declare it, because the relationship with the RP Intermediary is established through the federation, as the Relying Party sets its ``authority_hints`` to the RP Intermediary that federates it. The RP Intermediary side is described in :ref:`onboarding-system:Relying Party Intermediary`.
- `federation_entity_identifier`
- `federation_entity_key`:

  - REQUIRED for a Relying Party that operates without an intermediary. A Relying Party operating through a RP Intermediary MUST NOT provide it, because it is registered by its RP Intermediary according to the National Trust Framework.
- `certificate_signing_requests`

  - One Certificate Signing Request for each X.509 certificate the Relying Party needs, that is the WRPAC when it operates in the EUDIW Trust Framework, and the National Authentication Certificate when it operates only in National Trust Framework and supports the Proximity Flow.
- `trust_framework_scope`

  - The Relying Party declares whether it operates within the EUDIW Trust Framework for cross-border operations or only within national boundaries. This choice affects the artifacts it obtains, as detailed in :ref:`infrastructure-trust:Infrastructure of Trust`.

.. note::
   A Relying Party (intermediated or not) MUST register through the Onboarding System to obtain a registration Trust Mark (see :ref:`infrastructure-trust:Trust Mark registration-entity`), and in case of a Mobile Relying Party Instance, to obtain an Authentication X.509 Certificate. 
   Only if it operates in the EUDIW Trust Framework, it MUST have a record in the Register of WRP and it MUST obtain its WRPAC and its WRPRC.

Relying Party Intermediary
""""""""""""""""""""""""""

A Relying Party Intermediary declares that it acts as an intermediary in both the National and EUDIW Trust Frameworks.
In the National Trust Framework the Relying Party Intermediary is a Federation Intermediate, that is it onboards its intermediated Relying Parties autonomously, publishing their Subordinate Statements, as described in :ref:`infrastructure-trust:Trust Mark registration-entity`.
In the EUDIW Trust Framework it is registered with ``isIntermediary`` set, and it federates its intermediated Relying Parties that operate cross-border.
It provides the same Data Identifiers as a :ref:`onboarding-system:Relying Party`, with the differences in the table below.
The Data Identifiers not listed here are provided as for a Relying Party.

.. list-table:: Relying Party Intermediary Registration Data, differences from the Relying Party
   :class: longtable
   :widths: 34 66
   :header-rows: 1

   * - **Data Identifier**
     - **Value**
   * - `intended_use`
     - It MUST NOT be provided. A Relying Party Intermediary does not request attributes for itself, but on behalf of the intermediated Relying Parties.
   * - `intermediary_relationship`
     - Set on the intermediary side, that is the Relying Party declares that it is a designated intermediary. It is declared in both the frameworks.
   * - `federation_entity_identifier`
     - The Federation Entity Identifier of the Relying Party Intermediary within the National Trust Framework.
   * - `federation_entity_key`
     - The Federation Entity Key of the Relying Party Intermediary.

.. note::
  The registration of a Relying Party Intermediary and the registration of its intermediated Relying Parties are linked, the Intermediary declares that it acts as an intermediary, and each intermediated Relying Party references it in its own :ref:`onboarding-system:Relying Party` profile.


Wallet Provider
"""""""""""""""

A Wallet Provider is a Federation Entity that is notified, but it is not registered in the Register, because it does not act as a Wallet-Relying Party.
Its registration data is part of the notification dataset, and its Sign/Seal trust anchor is published in the Wallet Providers LoTE.
Besides the base registration data, a Wallet Provider provides the following extended registration data, as defined in :ref:`onboarding-system:Registration Data Model`:

- `entitlements`
- `service_description`
- `federation_entity_identifier`
- `federation_entity_key`
- `certificate_signing_requests`

  - One Certificate Signing Request for the Sign/Seal Certificate, with which the Wallet Provider signs the Wallet Unit Attestations.
- `conformity_assessment`


Authentic Source
""""""""""""""""

An Authentic Source is out of the EUDIW and the National Trust Frameworks, and its trust is governed by the PDND framework.
It is not registered in the Register and it is not a Federation Entity, so it does not provide the federation data and it obtains no Trust Artifact.
Its registration data is the entry of the AS Registry.
In addition to the base registration data, an Authentic Source provides the following extended registration data, as defined in :ref:`onboarding-system:Registration Data Model`:

- `provided_claims_purposes`
- `visual_identity`
- `verification_endpoint`

  - Provided only where the Authentic Source is responsible for an attribute exported to the EUDIW Catalogue of Attributes, so that a Qualified Trust Service Provider of another Member State can reach its verification interface.
