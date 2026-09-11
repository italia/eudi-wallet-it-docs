.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst
.. Included via index.rst at title level '=' (document title).

Infrastructure of Trust
=======================

The IT-Wallet ecosystem operates within a federated trust infrastructure where participating entities establish cryptographic trust relationships and maintain compliance with common security standards.
This infrastructure provides the foundation for secure Digital Credential operations across the ecosystem participants.

Two trust frameworks coexist in IT-Wallet.

  - The **EUDIW Trust Framework** is defined by the eIDAS2 Regulation (`EU_2024_1183`_), its Implementing Regulations and the ARF (`EIDAS-ARF`_).
    It is mandatory and authoritative for the notified entities and for cross-border interoperability.
  - The **National Trust Framework** is based on OpenID Federation (`OID-FED`_) combined with an X.509 PKI dedicated to the signature of Digital Credentials requiring X.509 PKI.
    It is the registration and onboarding layer for all the entities of the ecosystem, and it provides trust evaluation mechanisms for the operational phases where the EUDIW Trust Framework is not required.

This section provides first an overview of the entities and processes involved in the trust infrastructure (:ref:`infrastructure-trust:Overview`).
Then, it defines the general :ref:`infrastructure-trust:X.509 Certificate Profile` and the :ref:`infrastructure-trust:Common Trust Artifacts` shared by both frameworks, followed by the framework-specific artifacts (:ref:`infrastructure-trust:EUDIW Trust Artifacts` and :ref:`infrastructure-trust:National Trust Artifacts`).
Finally, it describes the related lifecycle (:ref:`infrastructure-trust:Trust Management and Lifecycle`).

Overview
--------

The IT-Wallet ecosystem operates on a federated trust infrastructure, requiring participating entities to establish mutual trust before engaging in any interaction involving User attributes.
To be able to perform a trust evaluation process, entities first need to onboard in the ecosystem (see :ref:`onboarding-system:Onboarding System and Lifecycle Management`).
During this phase, Non-Qualified EAA Providers and Relying Parties MUST declare whether they need to interoperate with European entities or they operate only within the national boundary.

This choice affects both the onboarding and the trust evaluation procedures.
If only the national boundary is requested, the infrastructure of trust complies with the National Trust Framework.
Otherwise, the EUDIW Trust Framework is necessary.
For example, the national-scope IT-Wallet ID is issued and validated under the National Trust Framework, whereas the EUDI Person Identification Data belongs to the EUDIW Trust Framework (see :term:`IT-Wallet ID`).

.. note::
    As the Wallet cannot know in advance whether it will be used to interact with national or European services, both the National and the EUDIW Trust Frameworks MUST be supported.
    PID Providers, QEAA Providers and PuB-EAA Providers MUST support the EUDIW Trust Framework, as they issue Credentials regulated by eIDAS 2.0.

In both cases, the onboarding and, where applicable, the European notification processes result in the release or update of the trust artifacts (detailed in sections :ref:`infrastructure-trust:Common Trust Artifacts`, :ref:`infrastructure-trust:EUDIW Trust Artifacts` and :ref:`infrastructure-trust:National Trust Artifacts`), then used during the trust evaluation processes (detailed in section :ref:`trust-evaluation:Trust Evaluation Process`).


.. include:: trust-pki-architecture.rst
.. include:: x509-certificate-profile.rst
.. include:: trust-artifact-common.rst
.. include:: trust-artifact-eudiw.rst
.. include:: trust-artifact-oidfed.rst
.. include:: trust-management.rst


