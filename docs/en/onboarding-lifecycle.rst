.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '-' (level 1).

Lifecycle Management
--------------------

After the registration event, an Entity can be updated, suspended, reactivated or cancelled, and a Credential type can become issuable or stop being issuable, and these changes reflect on the Trust Artifacts and on the registries.

This section describes the states and events that cause an entity or credential type to change state.
It also maps each event to the registries and trust artifacts impacted by the event, see :ref:`onboarding-system:Events, Registries and Trust Artifacts`.

The formats, the parameters and the states of the Trust Artifacts are defined in :ref:`infrastructure-trust:Trust Artifacts Lifecycle State Machine`, and the revocation mechanisms are defined in :ref:`infrastructure-trust:Revocation Mechanisms`.
The lifecycle of the single Digital Credentials issued to the Users is a different matter and it is defined in :ref:`credential-revocation:Digital Credential Lifecycle`.

Entity Lifecycle State Machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section applies to WRPs and WPs as they are directly involved in the operational phases.
As shown in :numref:`fig_Entity_Lifecycle_States`, an Entity has five distinct and mutually exclusive states: ``UNREGISTERED``, ``REGISTERED``, ``OPERATIONAL``, ``SUSPENDED`` and ``CANCELLED``.
Each state determines the authorization level and the operational capabilities of the Entity.

.. _fig_Entity_Lifecycle_States:
.. plantuml:: plantuml/entity-lifecycle-states.puml
    :width: 70%
    :alt: The figure illustrates the lifecycle states of an Entity and the transitions between them.
    :caption: `Entity Lifecycle States. <https://www.plantuml.com/plantuml/svg/TP91RiCW44Ntd6BMbNA1BgfO3geYMKva9wkq2meJ1na3Od2IthxONSHrwkKmxy-V3wmfYX3xph2BLWZO-VWD2aa6xQDsbb6hhHT1TF0bPDi4rrkLE-C2n20ifHRQEA7e8fIxQTl0MHX2nauldx1QlS6nhFZxjZxmYcyOcrPZUrA-Gi16Kve_R03ITTvWHCLcajsULzbXkokp8cbYw2b22gFFGaO2JTGdpHHwyfbhyEvrGFLXKxo0LzUc0NFN-bZlURaPzTIJHql3FSrz5h37yJ-XqmxwEeP-SispCkT5CO9IM8d6_89ptqNmh_CYnXwTWKklnzPerV13VW00>`_

**Transition from UNREGISTERED to REGISTERED**

- ``UNREGISTERED``: the Entity does not hold a valid registration within the IT-Wallet ecosystem.
  This is the default baseline state.
  Entities in this state are outside the trust boundary and MUST NOT participate in any operation.
- ``REGISTERED``: the Entity has completed the registration process and its identity has been verified.

  - *EUDIW Trust Framework*: WRPs are in ``REGISTERED`` state when their information has been added to the Register.
    Wallet Providers become ``REGISTERED`` when the certification and the onboarding records have been collected and verified.
  - *National Trust Framework*: WRPs and Wallet Providers are in ``REGISTERED`` state when the onboarding records have been collected and verified.

**Transition from REGISTERED to OPERATIONAL**

``OPERATIONAL`` indicates that the Entity has been authorized to perform the operations related to its role.

- *EUDIW Trust Framework*: WRPs are ``OPERATIONAL`` if they were ``REGISTERED`` and they obtained a WRPAC, optionally a WRPRC and, depending on the role, a Sign/Seal Certificate.
  The signing Trust Anchor of that certificate MUST have been added to the LoTE or to the EUMS TL.
  Wallet Providers are ``OPERATIONAL`` if they were ``REGISTERED`` and they obtained a Sign/Seal Certificate whose signing Trust Anchor has been added to the LoTE.
- *National Trust Framework*: WRPs and Wallet Providers are ``OPERATIONAL`` if they were ``REGISTERED``, they obtained the Sign/Seal Certificates and the registration Trust Marks, and their Subordinate Statement has been published by the Federation Authority.

**Transition from OPERATIONAL to REGISTERED**

An Entity goes back to ``REGISTERED`` when it no longer holds valid Trust Artifacts.
This can be triggered by its expiration or revocation following an update of the Entity.
To return to ``OPERATIONAL`` a new issuance of the Trust Artifacts is required.

**Transition from REGISTERED or OPERATIONAL to SUSPENDED**

``SUSPENDED`` indicates that the registration is temporarily not valid.
Differently from the cancellation, the suspension is reversible.
A WRP whose registration is suspended MUST NOT issue Credentials to Wallet Units nor request attributes from them, and the Credentials it issued are not accepted by the Relying Parties, as described in Section 4.6.5 of [`EIDAS-ARF`_].

The events that lead to this state, and the parties entitled to decide them, are listed in :ref:`onboarding-system:Registration Events and Their Governance`.

**Transition from SUSPENDED to REGISTERED**

The suspension can be lifted by the same party that decided it.
Because the Trust Artifacts affected by the suspension have been revoked, the Entity returns to ``REGISTERED`` and not directly to ``OPERATIONAL``, and a new issuance of the Trust Artifacts is required to become ``OPERATIONAL`` again.

**Transition from REGISTERED, OPERATIONAL or SUSPENDED to CANCELLED**

``CANCELLED`` indicates that the registration has ended.
The state is the same whether the cancellation was requested by the Entity itself or decided by the competent authority, and only the triggering event differs.

- *EUDIW Trust Framework*: for WRPs it results in the revocation of the WRPAC, the WRPRC and, where applicable, the Sign/Seal Certificates, in the removal of the entry from the Register and in the update of the status of the signing Trust Anchor in the LoTE or in the EUMS TL.
  For Wallet Providers it results in the update of the Wallet Providers LoTE.
- *National Trust Framework*: for both WRPs and Wallet Providers it results in the removal of the Subordinate Statement and of the registration Trust Mark, and in the revocation of the National X509 Certificates.

An Entity MUST reject new interactions or transactions started by a ``CANCELLED`` Entity, and all the cryptographic keys, the active attestations and the operational capabilities associated with the Entity MUST be revoked.
Entities MAY however continue to validate historical data, signatures and Credentials generated before the cancellation timestamp, subject to local risk policies.
An Entity in ``CANCELLED`` state that wants to participate again in the ecosystem MUST complete a new registration.

.. note::
  Section 4.6.5 of [`EIDAS-ARF`_] describes for PID Providers and Attestation Providers the states **Registered**, **Suspended** and **Cancelled**.
  Within IT-Wallet the **Registered** state is split into ``REGISTERED`` and ``OPERATIONAL``, to distinguish the moment in which the registration record exists from the moment in which the Entity holds all the Trust Artifacts it needs to operate.

.. note::
  The lifecycle of the Authentic Sources and of the Trust-infrastructure Entities, such as the Registrar and the Providers of WRPACs and of WRPRCs, is not defined in this section.
  The Authentic Sources follow the PDND framework, and the effects that their lifecycle produces inside IT-Wallet are described in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.

Registration Events and Their Governance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Every transition of the state machine of the Entities is caused by an event.
For each event, this section states who is entitled to trigger it, who is responsible for it, and, when applicable, on which normative basis and within which conditions.
The events that concern the Credential types and the Authentic Sources are described in the dedicated sections below.

.. _table_registration_events:
.. list-table:: Registration Events
   :class: longtable
   :widths: 16 26 16 22 20
   :header-rows: 1

   * - **Event**
     - **Trigger**
     - **Responsible**
     - **Normative reference**
     - **Condition**

   * - Registration
     - Request of the Entity, after the verification of the eligibility conditions applicable to its role.
     - Registrar, for the Register entry. Federation Authority, for the federation registration.
     - Articles 5 and 6 of [`CIR2025/848`_].
     - Not defined.

   * - Update
     - Change of the registered information. The WRP is responsible for the accuracy of its information and updates it.
     - Registrar, for the Register entry. Federation Authority, for the Subordinate Statement and the registration Trust Mark.
     - Article 5(2) and 5(3) of [`CIR2025/848`_].
     - Without undue delay.

   * - Suspension
     - Request from a Supervisory Body, request from the WRP itself, or initiative of the Registrar in the cases listed after this table.
     - Registrar for the EUDIW Trust Framework, Federation Authority for the National Trust Framework.
     - Article 9(1), 9(2), 9(3) and 9(5) of [`CIR2025/848`_].
     - Information of the WRP and of the Providers of its certificates within 24 hours.

   * - Reactivation
     - Removal of the condition that caused the suspension.
     - The same party that decided the suspension.
     - Section 4.6.5 of [`EIDAS-ARF`_].
     - Not defined.

   * - Cancellation
     - Request from a Supervisory Body, request from the WRP itself including when it no longer intends to rely upon Wallet Units, or initiative of the Registrar in the cases listed after this table.
     - Registrar for the EUDIW Trust Framework, Federation Authority for the National Trust Framework.
     - Article 9(1), 9(2), 9(3) and 9(5) of [`CIR2025/848`_].
     - Information of the WRP and of the Providers of its certificates within 24 hours.

Two roles carry out an event, one for each Trust Framework.
Within the EUDIW Trust Framework the Registrar acts on the Register and notifies the Providers of the affected Trust Artifacts.
Within the National Trust Framework the Federation Authority acts on the Subordinate Statement and on the registration Trust Mark, and publishes the event on the Federation Subordinate Events Endpoint.
The decision that triggers the event is the same for both, and it is described below with reference to the Registrar, as the obligations are set on the Registrar by [`CIR2025/848`_].

The Registrar MUST suspend or cancel the registration of a WRP where the suspension or the cancellation is requested by a Supervisory Body, and where it is requested by the same WRP.
The Registrar MAY suspend or cancel the registration on its own initiative where:

  - the registration contains information which is inaccurate, out of date or misleading;
  - the WRP is not compliant with the registration policy;
  - the WRP is requesting more attributes than the ones it registered;
  - the WRP is otherwise acting in breach of Union or National law in a manner related to its role.

Before suspending or cancelling a registration on its own initiative, the Registrar MUST conduct a proportionality assessment, taking into account the impact on the fundamental rights, the privacy, the security and the confidentiality of the Users of the ecosystem, the severity of the disruption caused by the measure and the associated costs, both for the WRP and for the User.

The Registrar MUST inform the WRP and the relevant Providers of WRPACs and of WRPRCs without undue delay, and in any case not later than 24 hours after the suspension or the cancellation, as set by Article 9(5) of [`CIR2025/848`_].
The information MUST include the reasons for the suspension or the cancellation and the available means of redress or appeal.
After the notification, the Providers MUST revoke the affected certificates without undue delay, where applicable, as set by Article 9(6) of [`CIR2025/848`_].

The Registrar MUST keep the records of the registration, of the issuance data and of the changes for 10 years.
Within IT-Wallet the same retention applies to the Federation Authority for the records of the National Trust Framework, by analogy.

.. note::
  The obligations described above are set by Articles 9 and 10 of [`CIR2025/848`_] and apply to the Registrar and to the registration of the WRPs.
  Within IT-Wallet the retention obligation is extended by analogy to the Federation Authority for the records it keeps for the National Trust Framework, since [`CIR2025/848`_] does not address the National Trust Framework.
  Wallet Providers are not registered as WRPs, so the suspension and cancellation of a Wallet Provider follow from the certification of its Wallet Solution and from the notification, and not from Article 9.

Beyond the Supervisory Body, the Registrar and the Entity itself, a suspension or a cancellation of an Entity MAY also be requested or triggered by other parties external to the Onboarding System, for example a judicial authority, an administrative authority competent for the Entity, an authority competent for cybersecurity, a conformity assessment body that withdraws a certification, or the Member State that withdraws a notification.
In every case the suspension or the cancellation is carried out through the mechanisms described above, where the Federation Authority that registered the Entity acts on its Subordinate Statement and on the registration Trust Mark, and the Trust Artifacts of the Entity are revoked.
For an Entity registered through a Federation Intermediate, the Subordinate Statement is served by the Intermediate, which withdraws it to suspend or cancel the Entity, while the registration Trust Mark remains issued by the Federation Trust Anchor which is responsible for any effects on the lifecycle of the registration Trust Mark.
The suspension or the cancellation of a Federation Intermediate MUST propagate to its affiliated Entities, whose Trust Chain runs through it, as described in :ref:`trust-evaluation:Federation Trust Chain`.

Independently of the notification described above, the Providers of WRPACs and the Providers of WRPRCs monitor the changes in the Register on a continuous basis, and revoke or reissue the certificates when the changes require it.
This is set by Annex IV of [`CIR2025/848`_] for the Providers of WRPACs and by Annex V of [`CIR2025/848`_] for the Providers of WRPRCs.

Within the National Trust Framework the events that change the registration of an Entity MUST be published by the Federation Authority as signed events on the Federation Subordinate Events Endpoint (``federation_subordinate_events_endpoint``), so that other participants can track the lifecycle of an Entity over time.
The endpoint and the format of its response are described in :ref:`infrastructure-trust:Federation API Endpoints`.

Each event of the state machine MUST be published as an object of the ``federation_registration_events`` array, using the event types defined in [`OID-FED-SUBORDINATE-EVENTS`_].
The table below gives, for each event, the value of the ``event`` parameter and how the parameters of the event object are populated.

.. _table_subordinate_events_mapping:
.. list-table:: Mapping of the Lifecycle Events to the Subordinate Events
   :class: longtable
   :widths: 26 24 22 28
   :header-rows: 1

   * - **Lifecycle event**
     - **event**
     - **iat**
     - **event_description**

   * - Registration
     - ``registration``
     - Time the registration is related to.
     - Not used.

   * - Update of Identity Information or Technical Configuration
     - ``metadata_update``
     - Time the update is related to.
     - MAY be used to provide further details about the update.

   * - Key rotation/update of a Federation Entity Key
     - ``jwks_update``
     - Time the key rotation/update is related to.
     - Not used.

   * - Suspension
     - ``suspension``
     - Time the suspension is related to.
     - MAY be used to provide further details about the suspension.

   * - Cancellation
     - ``revocation``
     - Time the cancellation is related to.
     - MAY be used to provide further details about the revocation.

When a ``registration`` event is present, the ``metadata_update`` and ``jwks_update`` events MUST NOT be provided at the same time, since the registration is assumed to configure the initial state of the Entity, as specified in [`OID-FED-SUBORDINATE-EVENTS`_].


Entity Updates and Their Effects on Trust Artifacts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Entities are characterized by three main categories of registered data.

- *Identity Information*: the name of the organization, the contact information and the organizational policies.
- *Technical Configuration*: the cryptographic material, meaning the signature and seal keys and the authentication keys, and the technical endpoints necessary for the interactions in the ecosystem.
- *Authorization Information*: the entitlements of the Entity, the Credential provision capabilities, the attribute request capabilities, the Intermediary use permissions, the intended uses, the embedded disclosure policies and the compliance with the certification schemes.

The Trust Framework infrastructure MUST propagate these changes to the relevant Trust Artifacts.
The specific effects depend on the role of the Entity and on the Trust Artifacts it uses.

The procedures that carry out an update, meaning what the Entity submits and which steps the Registrar, the Federation Authority and the Certificate Authorities execute, are described in the Entity Update process.
This section provides the relationship between the categories of registered data and the Trust Artifacts that contain them.

**Registered Data and Associated Trust Artifact**

The table below provides the relationship between the categories of registered data and the Trust Artifacts in which they are contained, for each type of Entity.

.. _table_entity_data_and_trust_artifacts:
.. list-table:: Entity Data and Trust Artifacts
   :class: longtable
   :widths: 18 26 28 28
   :header-rows: 1

   * - **Entity Type**
     - **Data Category**
     - **EUDIW Trust Artifacts**
     - **National Trust Artifacts**

   * - WRP (all)
     - Identity Information
     - Register, WRPAC, WRPRC, LoTE (only for PID, PuB-EAA and notified non-qualified EAA Provider)
     - Entity Configuration, registration Trust Mark

   * - WRP (all)
     - Technical Configuration (Authentication key)
     - WRPAC
     - Entity Configuration, Subordinate Statement

   * - WRP (all)
     - Authorization Information (Entitlements, Intermediary, Service descriptions, Supervision information)
     - Register, WRPRC, LoTE (only for PID, PuB-EAA and notified non-qualified EAA Provider)
     - Entity Configuration, registration Trust Mark

   * - Credential Issuer or Wallet Provider
     - Technical Configuration (Signature/Seal key)
     - X.509 Sign/Seal Certificate
     - X.509 Sign/Seal Certificate

   * - Credential Issuer or Wallet Provider
     - Technical Configuration (Metadata, Signature/Seal Trust Anchor)
     - LoTE
     - Trust Anchor Entity Configuration

   * - Credential Issuer
     - Authorization Information (RP permissions)
     - EDP in the Credential Issuer metadata
     - n/a

   * - Credential Issuer
     - Authorization Information (Credential provision capabilities)
     - Register, WRPRC
     - Subordinate Statement, registration Trust Mark

   * - Relying Party or Relying Party Intermediary
     - Authorization Information (Attribute request capabilities)
     - Register, WRPRC
     - Subordinate Statement, registration Trust Mark

   * - Wallet Provider
     - Identity Information
     - LoTE
     - Entity Configuration, registration Trust Mark

   * - Wallet Provider
     - Authorization Information (Service status)
     - LoTE
     - Subordinate Statement, registration Trust Mark

.. note::
  The inclusion of Wallet Providers and Credential Issuers in the LoTE is an implicit assertion of their role and of their authorization within the ecosystem.
  In particular, their inclusion is the result of the successful completion of the registration and notification procedures as defined in [`CIR2025/848`_] for the registration of the WRPs and in [`CIR2024/2980`_] for the notification of WRPs and Wallet Providers.
  Similarly, the ability to fetch the Subordinate Statement of an Entity means that the Entity is currently part of the National ecosystem.

.. note::
  QEAAs are provided by Qualified Trust Service Providers.
  Their identity, technical and authorization information are available in the dedicated EUMS TL.

  The identity, technical and authorization information of Registrars, Providers of WRPAC and Providers of WRPRC are available in dedicated LoTE.


Credential Type Lifecycle
^^^^^^^^^^^^^^^^^^^^^^^^^

A Credential type is registered in the Digital Credentials Catalog as a versioned entry.
The union of ``credential_type`` and ``version`` MUST be unique in the catalog, as specified in :ref:`registry:Digital Credentials Catalog Structure`, so different versions of the same Credential type exist in the catalog as separate entries.

For this reason the lifecycle applies to the single versioned entry, meaning the pair given by ``credential_type`` and ``version``, and not to the Credential type as a whole.
Each versioned entry has two states, ``ACTIVE`` and ``INACTIVE``, whose semantics is defined in :ref:`registry:Digital Credentials Catalog Structure`.
In short, a Credential type can be issued from a versioned entry only while that entry is ``ACTIVE``.

.. note::
  The state of the versioned entry is a different thing from the state of the single Digital Credentials issued to the Users, which is defined in :ref:`credential-revocation:Digital Credential Lifecycle`.

Within IT-Wallet, a versioned entry is ``ACTIVE`` only while all the following conditions are satisfied, and it moves back to ``INACTIVE`` as soon as one of them stops holding.

  - At least one Credential Issuer is listed in the ``issuers`` field of the entry, and each of them holds the entitlement corresponding to the ``legal_type`` of the Credential type.
  - The Authentic Source that provides the data, or the parent Credential type, is registered and available.
    For an Authentic Source integrated through PDND, this means that the e-Service is published and that the enrolment of the Credential Issuer has been approved.
  - The schema of the Credential type is registered in the Schema Registry for at least one of the supported formats.

Only one versioned entry of the same Credential type is ``ACTIVE`` at a given time.

**Versioning**

A Credential type is never modified in place.
When its definition changes, a new versioned entry is registered and activated, and the entry of the previous version is moved to ``INACTIVE``.

The Credentials already issued from the previous version keep their own status and are not revoked by the versioning.
Where the Credential Issuer needs the Users to obtain the new version, it can drive the re-issuance through the ``0x03`` (``UPDATE``) or the ``0x0F`` (``ATTRIBUTE_UPDATE``) status of the single Digital Credentials, as described in :ref:`credential-revocation:Digital Credential Lifecycle`.

The registration of a Credential type and its versioning are described in the registration processes, and the structure of the catalog entry in :ref:`registry:Digital Credentials Catalog Structure`.

.. note::
  Registering the Credential type first, in ``INACTIVE`` state and without Credential Issuers, makes the identifier of the Credential type available before the registration of the Credential Issuer, as it MUST declare at registration time the Credential types it intends to issue, and this declaration ends up in the Register and in the WRPRC.
  
  Moreover, changing a versioned entry to ``INACTIVE`` prevents any Wallet Unit to request a new issuance from that entry.
  It does not revoke the Credentials already issued from it, which keep their own status.
  Where the reason that caused the deactivation also requires the revocation of the Credentials already issued, the revocation is a separate decision, taken by the Credential Issuer as described in :ref:`credential-revocation:Digital Credential Lifecycle`.


Claims and Schemas Lifecycle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As described above for updating the credential type, claims and schemas registered in the respective registries are not removed, as the Credentials already issued keep referencing them, so removing a claim or a schema would make those Credentials impossible to interpret.

When a claim or a schema is deprecated, a new version of it is registered, and the Credential types that use it move to a new version as described above.

Authentic Source Lifecycle and PDND Alignment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An Authentic Source is not a WRP and it is not a Federation Entity, and its trust, authorization and operational aspects are governed by the PDND framework, as described in :ref:`e-service-pdnd:e-Service PDND`, and IT-Wallet relies on PDND for all of them.
Within IT-Wallet an Authentic Source is only registered in the Authentic Source Registry, described in :ref:`registry:Authentic Source Registry`, so that the Credential Issuers can discover which data are available and through which e-Service.

For this reason the IT-Wallet specification profile does not define a lifecycle of the Authentic Sources.
What this section defines is the effect that the PDND lifecycle produces inside IT-Wallet, because Credential types and Credential Issuers depend on it.

When an Authentic Source stops providing, through PDND, the data on which a Credential type depends, for example because the e-Service is no longer published or because the enrolment of the Credential Issuer has been withdrawn, the condition for the activation of that Credential type is no longer satisfied and the Credential type MUST be moved to ``INACTIVE``.
The Credential type stays registered and its identifier remains valid, so that the type can be activated again when the integration is restored.

The alignment process is not automatic and it works in both directions.

- From PDND to IT-Wallet, an Authentic Source that changes the availability of an e-Service used by a Credential type MUST notify the change, so that the state of the Credential type can be updated.
- From IT-Wallet to PDND, a Credential Issuer whose registration is suspended or cancelled MUST notify the change to the Authentic Source which may then decide to withdraw the corresponding authorizations within the PDND framework.

.. warning::
  The suspension or the cancellation of a registration in IT-Wallet does not produce any effect inside PDND.
  Until the authorizations are withdrawn on the PDND side, a Credential Issuer whose registration is no longer valid can still obtain a Voucher and access the e-Service of an Authentic Source, even if it can no longer issue Credentials to the Wallet Units.
  Within IT-Wallet the notification is therefore an obligation of the Credential Issuer and of the Authentic Source.

Events, Registries and Trust Artifacts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The table below summarises, for each event, which registries and catalogs are impacted and where the effects on the Trust Artifacts are described.
It covers both the initial registration and the subsequent lifecycle events.
The relationship between an Entity update and the Trust Artifacts it affects is given in :ref:`onboarding-system:Entity Updates and Their Effects on Trust Artifacts`, and the technical mechanisms that publish the status of a Trust Artifact in :ref:`infrastructure-trust:Revocation Mechanisms`.

.. _table_events_registries_artifacts:
.. list-table:: Events and Impacted Registries
   :class: longtable
   :widths: 22 20 34 24
   :header-rows: 1

   * - **Event**
     - **Decided by**
     - **Impacted registries and catalogs**
     - **Effects on Trust Artifacts**

   * - Registration of an Entity
     - Registrar, Federation Authority
     - Register (new entry). Notification to the Commission for the notified categories.
     - The Entity obtains its Trust Artifacts, see :ref:`table_entity_data_and_trust_artifacts`.

   * - Update of an Entity
     - Registrar, Federation Authority
     - Register (updated entry).
     - Depending on the updated data category, see :ref:`table_entity_data_and_trust_artifacts`.

   * - Key rotation of an Entity
     - Certificate Authority, Provider of WRPAC, Federation Authority
     - No registry is impacted, unless the key is a Trust Anchor key, in which case the LoTE.
     - Revocation and re-issuance of the certificate holding the key, see :ref:`table_entity_data_and_trust_artifacts`.

   * - Suspension of an Entity
     - Registrar, Federation Authority
     - Register (registration status no longer valid). Update of the LoTE or of the EUMS TL for the notified categories.
     - Revocation of the affected WRPAC, WRPRC and registration Trust Mark, and update of the Subordinate Statement.

   * - Reactivation of an Entity
     - Registrar, Federation Authority
     - Register (registration status valid again). Update of the LoTE or of the EUMS TL for the notified categories.
     - New issuance of the Trust Artifacts revoked at suspension time.

   * - Cancellation of an Entity
     - Registrar, Federation Authority
     - Register (entry removed). Update of the LoTE or of the EUMS TL for the notified categories.
     - Revocation of the WRPAC, WRPRC and Sign/Seal Certificates, and removal of the Subordinate Statement and of the registration Trust Mark.

   * - Registration of a Credential type version
     - Supervisory Body, published by the Federation Trust Anchor
     - Digital Credentials Catalog (new versioned entry, ``INACTIVE``). Schema Registry, for the schema of the new version.
     - None.

   * - Activation or deactivation of a Credential type version
     - Supervisory Body, published by the Federation Trust Anchor
     - Digital Credentials Catalog (state of the versioned entry).
     - None.

   * - New version of a Credential type
     - Supervisory Body, published by the Federation Trust Anchor
     - Digital Credentials Catalog (new versioned entry ``ACTIVE``, previous versioned entry ``INACTIVE``). Schema Registry.
     - None.

   * - Registration of a new claim or of a new schema
     - Supervisory Body, published by the Federation Trust Anchor
     - Claims Registry or Schema Registry (new entry). Alignment towards the Catalogue of Attributes or the Catalogue of Schemes.
     - None.

   * - Registration of an Authentic Source
     - Supervisory Body, published by the Federation Trust Anchor
     - Authentic Source Registry (new entry).
     - None.

   * - Change of availability of an Authentic Source
     - Authentic Source, through PDND
     - Authentic Source Registry. Digital Credentials Catalog, for the versioned entries that depend on it.
     - None.

.. note::
  The cancellation of a registration is the event, while the complete exit of an Entity from the ecosystem, which covers both Trust Frameworks, is the Entity Removal process described in the onboarding processes.
  The obligation of the Registrar to keep the records for 10 years survives the cancellation, so the removal of the entry from the Register is not a removal of the records of that registration.

.. note::
  The Register is a set of records per WRP, so an event impacts only the record of the Entity concerned.
  The Digital Credentials Catalog, the Authentic Source Registry, the Claims Registry, the Schema Registry and the Taxonomy are instead single signed documents, so every write requires a new signature and a new publication of the whole document.

