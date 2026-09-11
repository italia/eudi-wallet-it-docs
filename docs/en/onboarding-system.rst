.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst
.. Included via index.rst at title level '=' (document title).

Onboarding System and Lifecycle Management
==========================================

.. warning::
   This section is a work in progress and it is published in draft form.
   The general structure is in place, while several parts are still to be written and the content may change.
   The subsections marked as draft below contain only a short description of what they will provide.

The Onboarding System is the set of components, services, processes and procedures that admits an Entity into the IT-Wallet ecosystem, publishes the information that other participants need to recognize it, and manages what happens after the registration.

The Onboarding System covers:

  - **Entities**: the Wallet-Relying Parties, the Wallet Providers and the Authentic Sources, from their registration until the cancellation of that registration. An Entity is registered, updated, possibly suspended and reactivated, and finally removed.
  - **Trust Artifacts**: the certificates, the registration certificates and the federation statements that are issued as a result of a registration, and that are always derived from it.
  - **Credential types**: the versioned definitions published in the Digital Credentials Catalog, with the claims, the schemas and the Authentic Sources they depend on. A Credential type is registered, activated, versioned and deactivated.
  - **Registries and catalogs**: the National registries that the system writes, and the European catalogs and Lists of Trusted Entities towards which the system aligns or notifies.

For each of these, the Onboarding System covers the whole lifecycle and not only the first onboarding.

All events related to Entities and Credential types produce effects on the Trust Artifacts and on the registries, and those effects are described in this Section, together with the events that cause them.

As defined in :ref:`infrastructure-trust:Infrastructure of Trust`, two Trust Frameworks coexist in IT-Wallet, EUDIW and National Trust Framework, and the Onboarding System makes the registered Entities able to operate on both of them.

The National Trust Framework is the registration layer for all the Entities of the ecosystem and provides the mechanisms that the components of the Onboarding System use to authenticate each other.

The data structures of the registries are defined in :ref:`registry:Registry Infrastructure`, the profiles of the Trust Artifacts in :ref:`infrastructure-trust:Infrastructure of Trust`, the technical mechanisms that publish the status of a certificate in :ref:`infrastructure-trust:Revocation Mechanisms`, and the way the artifacts are consumed at runtime in :ref:`trust-evaluation:Trust Evaluation Process`.

The section is organized in five parts.
The **Overview** gives the actors, the components and the way the two Trust Frameworks are used.
The **Registration Model** gives the static view, that is what each role provides and what it obtains.
The **Onboarding Processes** give the dynamic view, that is how each procedure is carried out.
The **Notification and Publication** provides the procedure that brings the notified categories into the Lists of Trusted Entities, of which the Onboarding System handles the collection of the data.
The **Lifecycle Management** gives the states, the events and their effects on the registries and on the Trust Artifacts.

.. include:: onboarding-overview.rst
.. include:: onboarding-registration-model.rst
.. include:: onboarding-processes.rst
.. include:: onboarding-processes-entities.rst
.. include:: onboarding-processes-artifacts.rst
.. include:: onboarding-processes-credentials.rst
.. include:: onboarding-notification.rst
.. include:: onboarding-lifecycle.rst
