.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '^' (level 2, under Onboarding Processes).

Entity Onboarding
^^^^^^^^^^^^^^^^^

This section describes the processes that manage the lifecycle of the entities and of the Authentic Sources.
Each process is described with its Input, its Outcome and its Process, while the governance of the corresponding events, that is who is entitled to decide and within which conditions, is given in :ref:`onboarding-system:Registration Events and Their Governance`.

Entity Registration
"""""""""""""""""""

Entity Registration process takes as input the registration data of an Entity, verifies it, records it, and registers the Entity in the National Trust Framework and, where its role and its declaration require it, in the EUDIW Register.
The process is parameterized by the registration profile of the role, and its outcome is the transition of the Entity to the ``REGISTERED`` state.
It enables the :ref:`onboarding-system:Certificate and Trust Artifact Issuance` processes, that bring the Entity to ``OPERATIONAL``, and, for a Credential Issuer, the :ref:`onboarding-system:Credential Type Registration`.
The issuance of the certificates and of the registration Trust Mark, and the governance of the states, are described in the referenced processes and in :ref:`onboarding-system:Lifecycle Management`.

**Input**

The input is the registration data of the Entity, following the profile of its role defined in :ref:`onboarding-system:Registration Data Model` and in :ref:`onboarding-system:Registration Profiles`.
The data is organized in the three categories of registered data defined in :ref:`onboarding-system:Lifecycle Management`, and for each category a part is provided by the Entity and a part is derived by the Onboarding System.

- *Identity Information*, provided by the Entity: 

   - ``legal_name``,
   - ``identifier``, 
   - ``legal_nature``, 
   - ``contact_information``, 
   - ``service_policies``,
   - ``data_protection_authority``.
   
- *Technical Configuration*, provided by the Entity, in particular the ``federation_entity_identifier`` and the ``federation_entity_key`` of its Entity Configuration.
- *Authorization Information*, provided by the Entity, i.e.:

   - ``entitlements``, 
   - ``intended_use``, 
   - ``provided_attestations`` for a Credential Issuer, 
   - ``intermediary_relationship`` where applicable, 
   - ``conformity_assessment`` for the categories that need it.

The signed record, the certificates and their Trust Anchors are not an input but are derived from the registration.
In particular, the ``certificate_signing_requests`` are not a direct input of this process but of the :ref:`onboarding-system:Certificate and Trust Artifact Issuance` processes.
For a PID Provider and a Wallet Provider the ``signing_trust_anchor`` derives from the National issuance, and for a QEAA Provider and a PuB-EAA Provider it is provided within the eIDAS Trusted Lists, so it is not provided as an input by the Entity.

The eligibility and the compliance of the Entity are a precondition and not a part of this process, and they are described in :ref:`onboarding-system:Eligibility and Compliance Preconditions`.

**Outcome**

The outcome is the Entity in the ``REGISTERED`` state, that is the moment in which the registration record exists and has been verified, as defined in :ref:`onboarding-system:Lifecycle Management`.
The registration is recorded across the two Trust Frameworks according to the role and to the declaration of the Entity.

- In the National Trust Framework the Entity is registered in the federation, and its Subordinate Statement, that carries the registration Trust Mark, is published by the National Federation Management.
- In the EUDIW Trust Framework, for the Wallet-Relying Parties, a signed record is written in the Register, and it drives the later issuance of the WRPAC and of the WRPRC.

The National Trust Framework is always the registration layer, while the EUDIW Trust Framework is added for the notified categories and for the Entities that declare the cross-border operation, as described in :ref:`infrastructure-trust:Overview`.
The Register and the notification dataset are kept separate, as described in :ref:`onboarding-system:Registration Outcomes`.

**Process**

1. The eligibility and the compliance of the Entity MUST have been verified, including the identity proofing and the verification of the entitlements, as described in :ref:`onboarding-system:Eligibility and Compliance Preconditions`.
   This verification is the precondition of the registration.
2. The Onboarding System collects the registration data of the profile, validates it, and routes each part to the component responsible for it.
3. The National Federation Management registers the Entity in the federation.
   It validates the Entity Configuration published by the Entity, given by the ``federation_entity_identifier`` and the ``federation_entity_key``, and it prepares the metadata policy that binds the protocol metadata of the Entity to the values approved at onboarding.
   It then invokes the :ref:`onboarding-system:Registration Trust Mark Issuance` to obtain the registration Trust Mark, and it publishes the Subordinate Statement about the Entity, that carries the metadata policy and the Trust Mark.
   Then, the Entity MUST include the received Trust Mark in its Entity Configuration, that points to its immediate superior through the ``authority_hints``.
   During the same registration the Federation Trust Anchor public keys are made available to the Entity out-of-band, through the contact channel of the registration, and this bootstraps the trust of the Entity in the Trust Anchor, see :ref:`trust-evaluation:Federation Trust Anchor Distribution and Validation`.
   The structure of the Entity Configuration and of the Subordinate Statement is defined in :ref:`infrastructure-trust:National Trust Artifacts`.
4. Where the role and the declaration of the Entity require the EUDIW Trust Framework, the EUDIW Registration Management verifies the Entity and writes its record in the Register, and the Registrar signs or seals it.
   The record drives the later issuance of the WRPAC and of the WRPRC, and its data model and its public API are defined in :ref:`infrastructure-trust:Register of WRPs`.
   For a Credential Issuer, the ``provided_attestations`` declared at registration add the Credential Issuer to the ``issuers`` field of the versioned entry of each declared Credential type, as described in :ref:`onboarding-system:Credential Type Registration`, and the same declaration is carried in the record and in the WRPRC.
5. The registration produces the ``registration`` event, that the Federation Authority publishes on the Federation Subordinate Events Endpoint as described in :ref:`onboarding-system:Registration Events and Their Governance`.
   At the end of the process the Entity is ``REGISTERED``, the record enables the :ref:`onboarding-system:Certificate and Trust Artifact Issuance` processes that bring it to ``OPERATIONAL``, and, for a Credential Issuer, the declaration can activate the declared Credential types, as described in :ref:`onboarding-system:Credential Type Activation and Deactivation`.

.. note::
   The Register is the National register of the Wallet-Relying Parties that each Member State establishes under Article 3 of [`CIR2025/848`_] and operates through the Registrar.
   It is distinct from the semantic components of the Registry Infrastructure, that hold the Credential semantics and the discovery data, and it is documented as :ref:`infrastructure-trust:Register of WRPs`.

Entity Update
"""""""""""""

Entity Update process changes the registered information of an Entity, in its Identity Information, its Technical Configuration, including the rotation and the request of keys, and its Authorization Information.
The Entity is responsible for the accuracy of its information and updates it without undue delay.
This process describes what the Entity submits and which steps the components execute, while the relationship between the categories of registered data and the Trust Artifacts is given in :ref:`onboarding-system:Entity Updates and Their Effects on Trust Artifacts`.

**Input**

The updated registration data defined in :ref:`onboarding-system:Registration Data Model`.
For a change of the Identity Information the input is the new ``legal_name``, ``identifier``, ``legal_nature``, ``contact_information``, ``service_policies`` or ``data_protection_authority``.
For a change of the Technical Configuration related to the new key material, the ``federation_entity_key`` and ``certificate_signing_requests`` are provided respectively for the federation identity and for the X.509 certificates.
For a change of the Authorization Information the input is the new ``entitlements``, ``intended_use``, ``provided_attestations`` or ``intermediary_relationship``, depending on the role.

**Outcome**

The updated registered information of the Entity.
A change that affects the Authorization Information triggers the re-verification of the eligibility, because a new entitlement is not self-declared, as described in :ref:`onboarding-system:Eligibility and Compliance Preconditions`.

**Process**

1. The Entity submits the change of one or more categories of its registration data.
2. For a change of the Identity Information or of the Authorization Information, the EUDIW Registration Management updates the record in the Register, the National Federation Management updates the Subordinate Statement and the registration Trust Mark, and the Certificate Management re-issues the WRPAC or the WRPRC where the changed data is provided by them. Where the Entity belongs to a notified category, the Notification Dataset Management updates the notification, as described in :ref:`onboarding-system:Notification and Publication`.
3. For a change of the ``federation_entity_key``, the rotation of the key is handled by the National Federation Management, that re-issues the Subordinate Statement attesting the new key, so the new key becomes trusted only when the superior attests it, following :ref:`infrastructure-trust:Federation Entity Key Rotation`. The rotation of the keys of the X.509 certificates is a re-issuance handled by the :ref:`onboarding-system:Certificate and Trust Artifact Issuance` processes, where the Entity provides the new ``certificate_signing_requests`` in the ACME order.
4. A change of the Authorization Information is subject to the re-verification of the eligibility by the Supervisory Body, and, for a Credential Issuer, a change of the Credential provision capabilities adds it to or removes it from the ``issuers`` field of the versioned entry of a Credential type, as described in :ref:`onboarding-system:Credential Type Registration`.
5. The update produces the corresponding event, a ``metadata_update`` for a change of the Identity Information or the Technical Configuration and a ``jwks_update`` for a key rotation, published on the Federation Subordinate Events Endpoint as described in :ref:`onboarding-system:Registration Events and Their Governance`.

.. note::
   The informational parameters of the ``federation_entity`` metadata, with the exception of the ``organization_name``, are not included in the ``metadata_policy`` and can be managed autonomously by the Entity in its self-signed Entity Configuration.
   The protocol signature keys (``jwks``), the service endpoints and the request, response and redirect URIs are instead bound by the ``metadata_policy`` of the Subordinate Statement to the values approved at onboarding, as defined in :ref:`infrastructure-trust:National Trust Artifacts`, then a change of them is an Entity Update that re-issues the Subordinate Statement.

.. note::
   A change of the registered identity attributes of an Entity is an Entity Update, including a change of its ``legal_name``, of its ``legal_nature`` or of its ``identifier``, where the legal person stays the same.
   Where the legal person itself changes, such as in a merger or in a demerger, the registration of the previous Entity MUST be cancelled and the new legal person MUST be registered as a new Entity, because the identity proofing is bound to the legal person.

.. note::
   The rotation of a protocol key, the one provided within the protocol metadata, is carried out through the update of the ``metadata_policy`` and MUST follow the common practice: the new key is added to the fixed ``jwks`` and it coexists with the previous one until the Trust Chains built before the rotation have expired, and only then the previous key is removed.
   The coexistence covers the validity window of those Trust Chains, so that a verifier that still relies on a Trust Chain with the old key can validate until it rebuilds it.

Entity Suspension and Removal
"""""""""""""""""""""""""""""

Entity Suspension and Removal process suspends, reactivates or cancels the registration of an Entity, on the request of a Supervisory Body, of the Entity itself, or of another external party entitled to it as described in :ref:`onboarding-system:Registration Events and Their Governance`, across the two Trust Frameworks.
This process describes the steps that the components execute, while who is entitled to trigger each event, on which normative basis and within which conditions, is given in :ref:`onboarding-system:Registration Events and Their Governance`.

**Input**

The request of suspension, reactivation or cancellation, from the competent authority or from the Entity, with the reason for it.

**Outcome**

The Entity changed the status to ``SUSPENDED`` on a suspension, returns to its previous state on a reactivation, and moves to ``CANCELLED`` on a cancellation, as described in :ref:`onboarding-system:Lifecycle Management`.
A suspension and a cancellation revoke the Trust Artifacts of the Entity and, for a Credential Issuer, deactivate its Credential types.

**Process**

1. The request of suspension, reactivation or cancellation is received from the competent authority or from the Entity.
2. On a suspension, the EUDIW Registration Management suspends the record in the Register where the Entity is a Wallet-Relying Party, the National Federation Management withdraws the valid Subordinate Statement of the Entity, so that its Trust Artifacts are no longer relied upon, and the Entity moves to ``SUSPENDED``.
3. On a reactivation, once the condition that caused the suspension is removed, the same party that decided the suspension restores the registration, and the Entity returns to ``REGISTERED``.
4. On a cancellation, the EUDIW Registration Management cancels the record in the Register where the Entity is a Wallet-Relying Party, the National Federation Management withdraws the Subordinate Statement, the Trust Artifacts of the Entity are revoked, and the Entity moves to ``CANCELLED``.
5. For a Credential Issuer, a suspension or a cancellation deactivates its Credential types, and the Credential Issuer notifies the Authentic Sources so that they can withdraw the corresponding authorizations within PDND, as described in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.
6. After a suspension, a reactivation or a cancellation, where the Entity belongs to a notified category, the Notification Dataset Management updates the notification, so that the status of the Entity in the corresponding List of Trusted Entities is updated accordingly, as described in :ref:`onboarding-system:Notification and Publication`.
7. Each event, a ``suspension`` or a ``revocation``, is published on the Federation Subordinate Events Endpoint as described in :ref:`onboarding-system:Registration Events and Their Governance`.

Authentic Source Registration
"""""""""""""""""""""""""""""

Authentic Source Registration process writes Authentic Source information into the AS Registry so that Credential Issuers can discover which data is available and through which e-Service.
An Authentic Source is neither a Wallet-Relying Party nor a Federation Entity, so it does not go through the federation registration nor the Wallet-Relying Party registration, and it obtains no Trust Artifact.
Its trust, its authorization and its operational aspects are governed by the PDND framework, see :ref:`e-service-pdnd:e-Service PDND`, and IT-Wallet does not define a lifecycle of the Authentic Sources, so this process does not produce a state transition.
It enables the :ref:`onboarding-system:Credential Type Registration`, as the data source a Credential type references, and it can activate the :ref:`onboarding-system:Claim Registration` when a declared claim is not yet in the Claims Registry.

**Input**

The input is the registration data of the Authentic Source, following its profile in :ref:`onboarding-system:Registration Data Model` and in :ref:`onboarding-system:Registration Profiles`, that is the base registration data and, in addition, the ``provided_claims_purposes`` and the ``visual_identity``.
The Authentic Source selects from the :ref:`registry:Claims Registry` the standardized claim identifiers it provides, and from the Taxonomy the purposes it serves.
An Authentic Source does not provide the federation data nor the ``certificate_signing_requests``, and it has no ``entitlements``.
From this data the Authentic Source Management composes the entry of the Authentic Source in the AS Registry, whose structure is defined in :ref:`registry:Authentic Source Registry`, and it generates the registry-level fields, i.e. the identifier of the registry, its version, its last-modification time and its localization configuration.
The eligibility of the Authentic Source, that validates its legal standing and its data authority and classifies it as public or private, is a precondition and is described in :ref:`onboarding-system:Eligibility and Compliance Preconditions`.

**Outcome**

An entry in the AS Registry, that makes the Authentic Source discoverable by the Credential Issuers, with its organization information, its declared data capabilities, its integration method and its intended purposes.
The registration of the Authentic Source is complete and independent of the integration of any Credential Issuer, because an Authentic Source declares its capabilities before any Credential type exists.
The process does not produce a state in IT-Wallet, because the trust, the authorization and the operational aspects of the Authentic Source stay within the PDND framework, and the effects that the PDND lifecycle produces inside IT-Wallet are described in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.

**Process**

1. The eligibility and the compliance of the Authentic Source MUST have been verified by the Supervisory Body, that validates its legal standing and its data authority and classifies it as public or private, as described in :ref:`onboarding-system:Eligibility and Compliance Preconditions`.
   This verification is the precondition of the registration.
2. The Authentic Source declares its registration data.
3. The declared claims are verified against the :ref:`registry:Claims Registry` and the declared purposes against the Taxonomy.
   A claim that is not yet in the Claims Registry activates the :ref:`onboarding-system:Claim Registration`.
4. The Authentic Source Management writes the entry in the AS Registry, whose structure is defined in :ref:`registry:Authentic Source Registry`.
   The Authentic Source becomes discoverable by the Credential Issuers.

The entry enables the :ref:`onboarding-system:Credential Type Registration`, as the Authentic Source is the data source that a Credential type references.

.. note::
   The integration between an Authentic Source and a Credential Issuer takes place within PDND and is a precondition for the activation of a Credential type, not a process of the Onboarding System.
   Its effect on the lifecycle of the Credential type is described in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.

Authentic Source Update
"""""""""""""""""""""""

Authentic Source Update changes the entry of an Authentic Source in the AS Registry, with the effect on the versioned entries of the Credential types that depend on it.
An Authentic Source has no lifecycle in IT-Wallet, so the effect that a change produces on the Credential types is the one described in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.

**Input**

The changed registration data of the Authentic Source, that is a change of its ``provided_claims_purposes`` or of its ``visual_identity``, following its profile in :ref:`onboarding-system:Registration Data Model`.

**Outcome**

The entry of the Authentic Source in the AS Registry is updated.
When the change reduces the availability of the data on which a Credential type depends, the condition for the activation of that Credential type is no longer satisfied and the Credential type moves to ``INACTIVE``, as described in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.

**Process**

1. The Authentic Source, or the notification through PDND of the change of an e-Service, submits the change of the entry.
2. The Authentic Source Management updates the entry in the AS Registry, whose structure is defined in :ref:`registry:Authentic Source Registry`.
3. The Credential types that depend on the Authentic Source are updated, and a Credential type that loses the availability of the data it depends on moves to ``INACTIVE``, as described in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.

Authentic Source Removal
""""""""""""""""""""""""

Authentic Source Removal process removes the entry of an Authentic Source from the AS Registry, with the deactivation of the versioned entries of the Credential types that depend on it.

**Input**

The request for removal of the Authentic Source.

**Outcome**

The entry of the Authentic Source is removed from the AS Registry.
The Credential types that lose the Authentic Source as their data source move to ``INACTIVE``, and they stay registered so that they can be activated again if the data source is restored, as described in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.

**Process**

1. The request of removal of the Authentic Source is received.
2. The Authentic Source Management removes the entry from the AS Registry.
3. The Credential types that depend on the Authentic Source lose their data source and move to ``INACTIVE``, and they stay registered and can be activated again if the integration is restored, as described in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.
