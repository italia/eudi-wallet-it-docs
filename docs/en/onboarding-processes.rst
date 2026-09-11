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
     - Registration Trust Mark Issuance; Credential Type Activation and Deactivation, ``if it completes a versioned entry``
     - The request, by the Entity, of the WRPAC and of the WRPRC ``if EUDIW Trust Framework``, of the Sign/Seal Certificate ``if National PKI``, and of the National Authentication Certificate ``if Proximity Flow``; the :ref:`onboarding-system:Notification and Publication` of the Entity, ``if notified category``, for which the Onboarding System maintains the notifiable information
   * - :ref:`onboarding-system:Entity Update`
     - :ref:`onboarding-system:Entity Registration`
     - The Entity, which submits a change of one or more categories of its registration data
     - Registration Trust Mark Issuance, where the change affects the data it carries
     - The request, by the Entity, of the re-issuance of the certificates that carry the changed data, after the revocation of the WRPRC by its Provider, the re-verification of the eligibility where the change affects the Authorization Information, and the :ref:`onboarding-system:Notification and Publication` of the change, ``if notified category``
   * - :ref:`onboarding-system:Entity Suspension and Removal`
     - :ref:`onboarding-system:Entity Registration`
     - The competent authority or the Entity, which requests a suspension, a reactivation or a cancellation
     - Credential Type Activation and Deactivation, ``if Credential Issuer``
     - The :ref:`onboarding-system:Notification and Publication` of the new status of the Entity, ``if notified category``
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

The processes that act on the lifecycle of an entity or of a Credential type are governed as described in :ref:`onboarding-system:Lifecycle Management`, and the effects of each event on the registries and on the Trust Artifacts are given in :ref:`onboarding-system:Events, Registries and Trust Artifacts`.
