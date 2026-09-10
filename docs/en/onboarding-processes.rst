.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '-' (level 1).

Onboarding Processes
--------------------

This part gives the dynamic view of the onboarding.
Each process is described with its Input, its Outcome and its Process, that is the sequence of steps.

The processes are organized in three families.

- The :ref:`onboarding-system:Entity Onboarding` covers the registration of an entity and of an Authentic Source, and their update, suspension and removal.
- The :ref:`onboarding-system:Certificate and Trust Artifact Issuance` covers the issuance of the certificates and of the Trust Marks an entity obtains.
- The :ref:`onboarding-system:Attestation Onboarding` covers the registration of the claims, of the schemas and of the Credential types, and the lifecycle of the Credential types.

The Sections :ref:`onboarding-system:Process Dependency Map` and :ref:`onboarding-system:Notification and Publication` below provide respectively the order of the processes and the dependencies between them, and the notification process of the entities that are subject to it.

Process Dependency Map
^^^^^^^^^^^^^^^^^^^^^^

This section maps every onboarding process against four relations:

- **Preconditions** are the conditions that MUST hold before the process can run. They include the completion of another process and the conditions that are external to the Onboarding System, such as the certification of a Wallet Solution or the qualified status of a Qualified Trust Service Provider.
- **Started by** is who or what starts the process. A process is started by an external party that requests it, or it is invoked by another process, or it has no explicit request and it is a re-evaluation of conditions.
- **Activates** are the processes that start as a consequence of this one.
- **Enables** are the capabilities that become possible afterwards, which are not processes of the Onboarding System.

The processes are carried out by the components described in :ref:`onboarding-system:System Components and Services`, and one table is given for each family of :ref:`onboarding-system:Onboarding Processes`.

.. _table_map_entity:
.. list-table:: Process Map of the Entity Onboarding Processes
   :class: longtable
   :widths: 18 22 22 20 18
   :header-rows: 1

   * - **Process**
     - **Preconditions**
     - **Started by**
     - **Activates**
     - **Enables**
   * - :ref:`onboarding-system:Entity Registration`
     - Eligibility and compliance verification, including the identity proofing and the verification of the entitlements
     - The Entity, which requests the registration
     - Registration Trust Mark Issuance; the update of the notification dataset of the Notification and Publication, ``if notified category``; Credential Type Activation and Deactivation, ``if it completes a versioned entry``
     - The request, by the Entity, of the WRPAC and of the WRPRC ``if EUDIW Trust Framework``, of the Sign/Seal Certificate ``if National PKI``, and of the National Authentication Certificate ``if Proximity Flow``
   * - :ref:`onboarding-system:Entity Update`
     - :ref:`onboarding-system:Entity Registration`
     - The Entity, which submits a change of one or more categories of its registration data
     - Registration Trust Mark Issuance, where the change affects the data it carries; the update of the notification dataset of the Notification and Publication, ``if notified category``
     - The request, by the Entity, of the re-issuance of the certificates that carry the changed data, after the revocation of the WRPRC by its Provider, and the re-verification of the eligibility where the change affects the Authorization Information
   * - :ref:`onboarding-system:Entity Suspension and Removal`
     - :ref:`onboarding-system:Entity Registration`
     - The competent authority or the Entity, which requests a suspension, a reactivation or a cancellation
     - Credential Type Activation and Deactivation, ``if Credential Issuer``; the update of the notification dataset of the Notification and Publication, ``if notified category``
     - —
   * - :ref:`onboarding-system:Authentic Source Registration`
     - Eligibility and compliance verification by the Supervisory Body; the subscription of the Authentic Source to PDND and the publication of its e-Service
     - The Authentic Source, which declares its registration data
     - Claim Registration, ``if a claim is missing``
     - The registration of the Credential types that reference the Authentic Source as their data source
   * - :ref:`onboarding-system:Authentic Source Update`
     - :ref:`onboarding-system:Authentic Source Registration`
     - The Authentic Source, or the notification through PDND of the change of an e-Service
     - Credential Type Activation and Deactivation, ``if a type loses its data source``
     - —
   * - :ref:`onboarding-system:Authentic Source Removal`
     - :ref:`onboarding-system:Authentic Source Registration`
     - A request of removal
     - Credential Type Activation and Deactivation, ``if a type loses its data source``
     - —

.. _table_map_artifacts:
.. list-table:: Process Map of the Certificate and Trust Artifact Issuance Processes
   :class: longtable
   :widths: 18 22 22 20 18
   :header-rows: 1

   * - **Process**
     - **Preconditions**
     - **Started by**
     - **Activates**
     - **Enables**
   * - :ref:`onboarding-system:Wallet-Relying Party Access Certificate Issuance`
     - :ref:`onboarding-system:Entity Registration`, with a record of the Entity in the Register, ``if EUDIW Trust Framework``
     - The Entity, with an ACME order, for the first issuance or for a re-issuance
     - —
     - The authentication of the Entity towards the Wallet Units
   * - :ref:`onboarding-system:Wallet-Relying Party Registration Certificate Issuance`
     - :ref:`onboarding-system:Entity Registration`, with a record with a valid registration status in the Register and a valid WRPAC, ``if EUDIW Trust Framework``
     - The Entity, which requests the certificate to its Provider of WRPRC, for the first issuance or after the revocation of the previous one
     - —
     - The presentation of the registration data of the Entity to the Wallet Units
   * - :ref:`onboarding-system:Signature and Seal Certificate Issuance`
     - :ref:`onboarding-system:Entity Registration`, ``if National PKI``. For a QEAA Provider and a PuB-EAA Provider the certificate is qualified and it is issued by a Qualified Trust Service Provider outside this process
     - The Entity, with an ACME order, for the first issuance or for a re-issuance
     - —
     - The signature or the seal of the Attestations the Entity issues
   * - :ref:`onboarding-system:National Authentication Certificate Issuance`
     - :ref:`onboarding-system:Entity Registration`, ``if Proximity Flow``
     - The Entity, with an ACME order, for the first issuance or for a re-issuance
     - —
     - The authentication of the Entity in the Proximity Flow
   * - :ref:`onboarding-system:Registration Trust Mark Issuance`
     - The completion of the federation registration of the Entity
     - Invoked by the Entity Registration, and by the Entity Update where the change affects the data the Trust Mark carries
     - —
     - The recognition of the Entity as a registered participant of the National Trust Framework, and the reading of its authorization data where it has no record in the Register

.. _table_map_attestation:
.. list-table:: Process Map of the Attestation Onboarding Processes
   :class: longtable
   :widths: 18 22 22 20 18
   :header-rows: 1

   * - **Process**
     - **Preconditions**
     - **Started by**
     - **Activates**
     - **Enables**
   * - :ref:`onboarding-system:Claim Registration`
     - —
     - Invoked by the Authentic Source Registration, by the Schema Provisioning or by the Credential Type Registration, ``if a claim is missing``
     - —
     - The Schema Provisioning and the Credential Type Registration that use the claim
   * - :ref:`onboarding-system:Schema Provisioning`
     - The claims that compose the schema are available in the Claims Registry
     - Invoked by the Credential Type Registration, ``if the schema is missing``
     - Claim Registration, ``if a claim is missing``
     - The activation of a Credential type, as one of its conditions
   * - :ref:`onboarding-system:Credential Type Registration`
     - The definition and the availability of the applicable Attestation Rulebook; the Authentic Source Registration, or a parent Credential type, as the data source
     - The Attestation Scheme Provider, which requests the registration
     - Claim Registration, ``if a claim is missing``; Schema Provisioning, ``if the schema is missing``; Credential Type Activation and Deactivation
     - The declaration of the Credential type by a Credential Issuer at its Entity Registration
   * - :ref:`onboarding-system:Credential Type Activation and Deactivation`
     - :ref:`onboarding-system:Credential Type Registration`
     - No explicit request. The versioned entry is re-evaluated whenever one of its three conditions changes
     - —
     - The issuance of the Credential type by the Credential Issuers listed in the versioned entry
   * - :ref:`onboarding-system:Credential Type Update`
     - :ref:`onboarding-system:Credential Type Registration`
     - The Attestation Scheme Provider, which publishes a new version
     - Credential Type Registration for the new versioned entry; Credential Type Activation and Deactivation
     - —

.. _table_map_notification:
.. list-table:: Process Map of the Notification and Publication
   :class: longtable
   :widths: 18 22 22 20 18
   :header-rows: 1

   * - **Process**
     - **Preconditions**
     - **Started by**
     - **Activates**
     - **Enables**
   * - :ref:`onboarding-system:Notification and Publication`
     - :ref:`onboarding-system:Entity Registration`, and the conformity assessment for the notified categories
     - Invoked by the Entity Registration, by the Entity Update or by the Entity Suspension and Removal, ``if notified category``, for the collection of the notifiable information. The submission to the European Commission is an act of the Supervisory Body
     - —
     - The inclusion of the Entity in the List of Trusted Entities of its category

The processes that act on the lifecycle of an entity or of a Credential type are governed as described in :ref:`onboarding-system:Lifecycle Management`, and the effects of each event on the registries and on the Trust Artifacts are given in :ref:`onboarding-system:Events, Registries and Trust Artifacts`.

Notification and Publication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This Section describes the notification to the European Commission of the entities that are subject to it, and the resulting publication in the Lists of Trusted Entities.
This process applies to more than one family of processes.

The notification is an act of the Member State to the Commission, and not of the entity itself.
Within IT-Wallet the Supervisory Body is the National point of contact with the Commission and it relies on the Registrar for the entities the Registrar registers.
Its outcome is the inclusion of the entity in the List of Trusted Entities of its type, whose structure and signature are described in :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`.

The categories subject to notification according to Articles 4 and 5 of [`CIR2024/2980`_], adopted under Article 5a(23) of [`EIDAS`_], are the following:

- Wallet Providers;
- PID Providers;
- Providers of WRPAC;
- Providers of WRPRC, where applicable;
- Registrars of the Wallet-Relying Parties, together with the registers.

The PuB-EAA Providers are notified under Article 45f(3) of [`EIDAS`_], and the detailed rules are laid down in [`CIR2025/1569`_].
The Wallet-Relying Parties that do not belong to a notified category are not notified individually, and they are made available through their register.


**Input**

The input is the notifiable information of the entity, that is the subset of its registration data that applies to the category, defined by Annex II of [`CIR2024/2980`_] and, for the PuB-EAA Providers, by Annex III of [`CIR2025/1569`_].
The information is a projection of the :ref:`onboarding-system:Registration Data Model`:

- ``legal_name``
- ``identifier``
- ``contact_information``
- ``service_policies``
- ``signing_trust_anchor``
- ``conformity_assessment``

For a PID Provider and a Wallet Provider the Sign/Seal Certificate is issued by the National PKI, so the ``signing_trust_anchor`` is not provided as an input by the entity but derives from the issuance described in :ref:`onboarding-system:Signature and Seal Certificate Issuance`.

For a PuB-EAA Provider the Sign/Seal Certificate is a qualified certificate issued by a Qualified Trust Service Provider, and its Trust Anchor is conveyed by the eIDAS Trusted Lists that are outside of this process.
Therefore, the Sign/Seal Trust Anchor is not required as an input for a PuB-EAA Provider, and the qualified status of its certificate is evaluated in the conformity assessment required for eligibility and compliance, see :ref:`onboarding-system:Eligibility and Compliance Preconditions`.

The notifiable information is collected in the notification dataset, that is kept separate from the Register as described in :ref:`onboarding-system:Trust Artifacts Registration Outcomes`.

.. note::
   The Sign/Seal Trust Anchor is not the certificate the entity uses to sign, whose public key is conveyed by the ``certificate_signing_requests``.

**Outcome**

The outcome is the inclusion of the entity in the List of Trusted Entities of its type.
The inclusion is the assertion, at Union level, of the role and of the authorization of the entity, and it is what allows a Wallet Unit or a Wallet-Relying Party of another Member State to validate the entity.

**Process**

1. The entity MUST have completed its :ref:`onboarding-system:Entity Registration`, and for the notified categories the conformity assessment MUST have been verified as described in :ref:`onboarding-system:Eligibility and Compliance Preconditions`.
   The completion of the registration is the precondition of the notification.
2. The Onboarding System collects the notifiable information of the category from the notification dataset, following Annex II of [`CIR2024/2980`_] or, for the PuB-EAA Providers, Annex III of [`CIR2025/1569`_].
3. The Supervisory Body, as the National point of contact, submits the information to the secure electronic notification system that the Commission makes available. The submission MUST be made at least in English.
   The system and its requirements are defined in Annex I of [`CIR2024/2980`_].
4. The Commission may request additional information or clarifications to verify the completeness and the consistency of the notified information.
5. The Commission publishes the List of Trusted Entities that compiles the notified information.
   The entity appears in the List of Trusted Entities of its type, whose data model, format and signature are described in :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`.
6. Where the registration of the entity changes, in particular where it is suspended or cancelled, the Onboarding System MUST reflect the change in the notification.

.. note::
   The Lists of Trusted Entities defined by [`CIR2024/2980`_] and the Trusted Lists defined by [`CID2015/1505`_] are two different artifacts.
   They are described together in :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`.
