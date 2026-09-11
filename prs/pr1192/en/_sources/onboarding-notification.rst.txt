.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '-' (level 1).

Notification and Publication
----------------------------

This Section describes the notification to the European Commission of the entities that are subject to it, and the resulting publication in the Lists of Trusted Entities. The submission is an act of the Member State (through the Single Point Of Contact) and the publication is an act of the European Commission, so the notification is not one of the :ref:`onboarding-system:Onboarding Processes`. The Onboarding System handles only the collection and the maintenance of the notifiable information.

Within IT-Wallet the Supervisory Body is the National Single Point Of Contact with the Commission and it relies on the Registrar for the entities the Registrar registers.
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
The dataset is written and kept up to date by the Notification Dataset Management during the :ref:`onboarding-system:Entity Registration`, the :ref:`onboarding-system:Entity Update` and the :ref:`onboarding-system:Entity Suspension and Removal`.

.. note::
   The Sign/Seal Trust Anchor is not the certificate the entity uses to sign, whose public key is conveyed by the ``certificate_signing_requests``.

**Outcome**

The outcome is the inclusion of the entity in the List of Trusted Entities of its type.
The inclusion is the assertion, at EU level, of the role and of the authorization of the entity, and it is what allows a Wallet Unit or a Wallet-Relying Party of another Member State to validate the entity.

**Process**

1. The entity MUST have completed its :ref:`onboarding-system:Entity Registration`, and for the notified categories the conformity assessment MUST have been verified as described in :ref:`onboarding-system:Eligibility and Compliance Preconditions`.
   The completion of the registration is the precondition of the notification.
2. The Onboarding System collects the notifiable information of the category from the notification dataset, following Annex II of [`CIR2024/2980`_] or, for the PuB-EAA Providers, Annex III of [`CIR2025/1569`_].
3. The Supervisory Body, as the National Single Point Of Contact, submits the information to the secure electronic notification system that the Commission makes available. The submission MUST be made at least in English.
   The system and its requirements are defined in Annex I of [`CIR2024/2980`_].
4. The Commission may request additional information or clarifications to verify the completeness and the consistency of the notified information.
5. The Commission publishes the List of Trusted Entities that compiles the notified information.
   The entity appears in the List of Trusted Entities of its type, whose data model, format and signature are described in :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`.
6. Where the registration of the entity changes, in particular where it is suspended or cancelled, the Onboarding System MUST reflect the change in the notification dataset.

.. note::
   The Lists of Trusted Entities defined by [`CIR2024/2980`_] and the Trusted Lists defined by [`CID2015/1505`_] are described in :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`.
