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

This section describes, for each process, its prerequisites, the dependencies, the triggers and what it enables, together with the preconditions that are external to the Onboarding System.

The processes are carried out by the components described in :ref:`onboarding-system:System Components and Services`.
The table below maps the dependencies between the onboarding processes where what a process enables is another process that becomes possible after it.

.. list-table:: Process Dependency Map
   :class: longtable
   :widths: 25 25 25 25
   :header-rows: 1

   * - **Process**
     - **Depends on**
     - **Trigger**
     - **Enables**
   * - :ref:`onboarding-system:Entity Registration`
     - None
     - An entity that passed the eligibility and compliance verification requests the registration.
     - The Certificate and Trust Artifact Issuance processes, and for a Credential Issuer the activation of the Credential types it declares.
   * - :ref:`onboarding-system:Authentic Source Registration`
     - None
     - An Authentic Source that passed the eligibility verification requests the registration.
     - The Credential Type Registration, as the data source a Credential type references.
   * - :ref:`onboarding-system:Claim Registration`
     - None
     - A claim that a Credential type or an Authentic Source needs is not yet in the Claims Registry.
     - The Schema Provisioning and the Credential Type Registration that use the claim.
   * - :ref:`onboarding-system:Wallet-Relying Party Access Certificate Issuance`
     - :ref:`onboarding-system:Entity Registration`
     - The first registration, or a new issuance or re-issuance, for example after a key rotation.
     - The authentication of the entity towards the Wallet Units.
   * - :ref:`onboarding-system:Wallet-Relying Party Registration Certificate Issuance`
     - :ref:`onboarding-system:Entity Registration`
     - The first registration, or a re-issuance, where the certificate applies to the role.
     - The presentation of the registration data of the entity to the Wallet Units.
   * - :ref:`onboarding-system:Signature and Seal Certificate Issuance`
     - :ref:`onboarding-system:Entity Registration`
     - The first registration, or a re-issuance, for the categories whose Sign/Seal Certificate is issued by the National PKI.
     - The signature of the Attestations or of the Wallet Unit Attestations the entity issues.
   * - :ref:`onboarding-system:National Authentication Certificate Issuance`
     - :ref:`onboarding-system:Entity Registration`
     - An entity that operates in the Proximity Flow.
     - The authentication of the entity in the Proximity Flow.
   * - :ref:`onboarding-system:Registration Trust Mark Issuance`
     - :ref:`onboarding-system:Entity Registration`
     - The completion of the federation registration.
     - The recognition of the entity as a registered participant of the National Trust Framework.
   * - :ref:`onboarding-system:Schema Provisioning`
     - :ref:`onboarding-system:Claim Registration`
     - A Credential type needs its schema to be available.
     - The activation of a Credential type, as one of its requirements.
   * - :ref:`onboarding-system:Credential Type Registration`
     - :ref:`onboarding-system:Authentic Source Registration`, :ref:`onboarding-system:Schema Provisioning`, :ref:`onboarding-system:Claim Registration`
     - An Attestation Scheme Provider requests the registration of a Credential type defined in an Attestation Rulebook.
     - The declaration of the Credential type by a Credential Issuer, the Credential Type Activation, and the Notification and Publication for the notified categories.
   * - :ref:`onboarding-system:Credential Type Activation and Deactivation`
     - :ref:`onboarding-system:Credential Type Registration`
     - The verification of the issuance conditions of the Credential type.
     - The issuance of the Credential type by the Credential Issuer.
   * - :ref:`onboarding-system:Credential Type Update`
     - :ref:`onboarding-system:Credential Type Registration`
     - The publication of a new version of a Credential type by its Attestation Scheme Provider.
     - The activation of the new version.
   * - :ref:`onboarding-system:Entity Update`
     - :ref:`onboarding-system:Entity Registration`
     - A change of the registered information, that is the identity, the technical configuration, or the authorization information.
     - The re-issuance of a certificate, or the re-verification of the eligibility where the change affects the authorization information.
   * - :ref:`onboarding-system:Entity Suspension and Removal`
     - :ref:`onboarding-system:Entity Registration`
     - A request of the competent authority or of the entity.
     - The revocation of the Trust Artifacts of the entity, and the deactivation of its Credential types where it is a Credential Issuer.
   * - :ref:`onboarding-system:Authentic Source Update`
     - :ref:`onboarding-system:Authentic Source Registration`
     - A change of the AS Registry entry.
     - The update of the Credential types that depend on the Authentic Source.
   * - :ref:`onboarding-system:Authentic Source Removal`
     - :ref:`onboarding-system:Authentic Source Registration`
     - A request of removal.
     - The deactivation of the Credential types that lose the Authentic Source as their data source.

The :ref:`onboarding-system:Notification and Publication` process is transversal and follows the registration of the notified categories.

The following conditions are external to the Onboarding System and are not processes defined within IT-Wallet, but they are preconditions or triggers.

- The subscription of an Authentic Source to PDND and the publication of its e-Service.
- The qualified status of a Qualified Trust Service Provider, for a QEAA Provider and a PuB-EAA Provider.
- The certification of a Wallet Solution.
- The definition and the availability of the applicable Attestation Rulebook, for a Credential Type Registration. The Rulebook is an input of the Onboarding System and its definition is not a process of it.
- The identity proofing and the eligibility and compliance verification, described in :ref:`onboarding-system:Eligibility and Compliance Preconditions`, that precede every registration.

The diagram below shows the activations between the various processes.
Those on the left are the *starting processes*, triggered from outside the Onboarding System.
Those on the right are activated by a starting process or by a lifecycle process.
The processes that act on the lifecycle of an entity or of a Credential type are governed as described in :ref:`onboarding-system:Lifecycle Management`, and the effects of an update are described there as well.

.. _fig_onboarding_dep_map:
.. plantuml:: plantuml/onboarding-dependency-map.puml
    :width: 99%
    :align: center
    :alt: The figure illustrates the activations between the various processes. On the left the *starting processes* are illustrated, triggered from outside the Onboarding System. Those on the right are activated by a starting process or by a lifecycle process.
    :caption: `Onboarding Process Dependency Map. <https://www.plantuml.com/plantuml/svg/ZLRRQXin47qt-1-6vA5FfabBqpJG4dkpRWEnCRikUV6BiZjUYsWb8sdZk2N_tj5ginTVaifWp5pEp9mv4husbcbRv09cMYLe30mJov-OvKh2XAtxFO5B2rQ1vjdAGier9ixPxvb7BjTCinmUMFAOQLN8D512QR2QIKCkbBOTPbOiLHikCrWoOR3jId792c7d-6o7WcSofrH8w0jrEsnDXLY6iTqA1DS8avde00srLXlVnUb5UVQyOoLjpFyWd9-tVJNSIEaKTONnkJoTE3-dbgZXij_hzpx0TtTA8jrmQqya6c_lzsfaE0cbvNQxa15ct11DZicFlzSfitW2p40OmUbeT1EEHvsqOM5NH0PF85Q5Jh0BK6OEuyEfWSRKfJ81y-qQZvSEvWGGN8ONmRVMLC2y733TdwlQ1fpCTM4iaMlvai99DfBCReKbyDqPd8w_k0_yxVU0JgkzTZTGuYpaXEb7k3McO3BnlSqd134EpqQVzW3kezamw4Pxqx64cEJ5RA4Hc4mXHYOMCa3NEqzepYvK7BzLEDel71qlF2s7f3tKsomDRrIVjiTuQH5UiROjHmYOPK9bZhSkx-Tly1u8nlC3CWfQ8jWbBbbXpXQI7eedRYY1nEv9cXtDsL5Vwt5PIDVx3RBQKgbms82zT9GyLHLBJYgKJ9qK3w8oUBweaV1y58PVsmgERd_-cb-1u4jCjWaXlNz18IxC6gMf-ummLqzC-3jwvAOTkgHD5jtFIPFckXiC1b2LEt0deI76kD1-Zzw6mU27kmjNmCI6RKrjyug_0hvqFsipgRUqSH8LlLPAB-Gz4m8jb3jCtUFQ84G74AQli9Jmp7FNwrYeJUEVURSiTuDfxN1xzBNf7LVvcegY8Ix1aWoQ-NSvwp2nJu5xv4hqo8CpIBoEkO6SfYH5DjYxslilajqh-6w5rw1uzXfaghjnAEe85JJu3XbtjKBtTn_lOfKhRHpxYoW5rydnv2-aK4xxt1em9UckWskKAVqB-0S0>`_


Notification and Publication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This Section describes the notification to the European Commission of the entities that are subject to it, and the resulting publication in the Lists of Trusted Entities.
This process applies to more than one family of processes.

The notification is an act of the Member State to the Commission, and not of the entity itself.
Within IT-Wallet the Supervisory Body is the National point of contact with the Commission, as described in :ref:`onboarding-system:Eligibility and Compliance Preconditions`, and it relies on the Registrar for the entities the Registrar registers.
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

The notifiable information is collected in the notification dataset, that is kept separate from the Register as described in :ref:`onboarding-system:Registration Outcomes`.

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
