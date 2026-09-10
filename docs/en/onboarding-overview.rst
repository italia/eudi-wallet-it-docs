.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '-' (level 1).
 
Overview
--------
 
This Section introduces the actors that take part in onboarding, the components and services of the Onboarding System that realize them, and the way the two Trust Frameworks combine.
It gives the reader the context needed to follow the registration model, the processes and the lifecycle described in the Sections that follow.
 
System Actors and Roles
^^^^^^^^^^^^^^^^^^^^^^^
 
Two families of actors take part in onboarding, the entities that are onboarded, and the trust-infrastructure entities that operate the onboarding itself.
The trust-infrastructure roles are realized by the components and services of the Onboarding System, described in the next subsection.
 
**Entities being onboarded**
 
  - **Authentic Sources**: onboard to make their data available to the Credential Issuers, so that the data can be included in the Attestations.
  - **Wallet-Relying Parties**: onboard to be authorized to rely on the Wallet Units and to obtain the Trust Artifacts they need to operate. They are further split into:
 
    - **Credential Issuers**, which onboard to be authorized to issue the Credential types they declare;
    - **Relying Parties** and **Relying Party Intermediaries**, which onboard to be authorized to request User attributes from the Wallet Units.
 
  - **Wallet Providers**: onboard to have their Wallet Solution recognized in the ecosystem and to be notified.
 
**Trust-infrastructure entities**
 
  - **Supervisory Body**: during the onboarding it verifies the eligibility and the compliance of the entities, avails itself of the Registrar for technical registration, and acts as the National single point of contact for the notification to the European Commission.
  - **Registrar** and **Register**: the Registrar performs the technical registration of the Wallet-Relying Parties and writes their records into the **Register** as defined by [`CIR2025/848`_].
  - **Provider of WRPAC** and **Provider of WRPRC**: issue, respectively, the WRPAC and the WRPRC.
  - **National Federation Authorities**: the **Federation Trust Anchor** and its **Federation Intermediates**, which register Federation Entities and apply the metadata policies. Each Federation Authority issues the X.509 certificates and the Trust Marks for the Federation Entities it registers, while the registration Trust Mark is issued only by the Federation Trust Anchor, as described in :ref:`infrastructure-trust:Trust Mark registration-entity`.
    In IT-Wallet the National Trust Anchor also operates the root Certification Authority of the National X.509 signing PKI, whose root certificate and its distribution are described in :ref:`infrastructure-trust:PKI Architecture`.
 
**Entities that interact with the Onboarding System without being onboarded**

  - **Attestation Scheme Providers**: they own the Attestation Rulebook of a Credential type and they request the registration of the corresponding versioned entry in the Digital Credentials Catalog, providing the definition and the schema taken from the Rulebook, see :ref:`onboarding-system:Credential Type Registration`.
  An Attestation Scheme Provider is not registered as an Entity for this role. Within IT-Wallet the role is held by an orfanization that owns the Rulebook.

.. note::
   A single organization may perform several of these functions at once.
 
Wallet Instances are not Federation Entities and are not onboarded directly.
A Wallet Instance is registered indirectly, through its Wallet Provider, see :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`, and it is deemed reliable through a Wallet Instance Attestation issued and signed by that Wallet Provider, see :ref:`wallet-instance-attestation-issuance:Wallet Instance Attestation Issuance`.
 
The notification of a notified entity is a Member State process defined by [`CIR2024/2980`_], described in :ref:`onboarding-system:Notification and Publication`.
 
System Components and Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
The trust-infrastructure roles are realized, within the Onboarding System, by a set of components, each providing one or more services.
An onboarding entity interacts with the system through a single entry point, the Onboarding UI, which orchestrates the flow and routes each request to the responsible component, and which is therefore not shown as a separate component in the diagram below.

The table below lists the components, the services each of them provides, and the onboarding process that each service realizes.
 
.. list-table:: Components, Services and Processes
   :class: longtable
   :widths: 24 30 46
   :header-rows: 1
 
   * - **Component**
     - **Services**
     - **Realized process**
   * - National Federation Management
     - Federation registration, issuance of Trust Marks, publication of the signed registries
     - :ref:`onboarding-system:Entity Registration`, :ref:`onboarding-system:Entity Update`, :ref:`onboarding-system:Entity Suspension and Removal`, :ref:`onboarding-system:Registration Trust Mark Issuance`
   * - EUDIW Registration Management
     - Verification and registration of the Wallet-Relying Parties in the Register
     - :ref:`onboarding-system:Entity Registration`, :ref:`onboarding-system:Entity Update`, :ref:`onboarding-system:Entity Suspension and Removal`
   * - Certificate Management
     - Issuance and update of WRPAC, WRPRC, Sign/Seal and National Authentication certificates
     - :ref:`onboarding-system:Certificate and Trust Artifact Issuance`, :ref:`onboarding-system:Entity Update`
   * - Notification Dataset Management
     - Collection and maintenance, in the notification dataset, of the information subject to notification
     - :ref:`onboarding-system:Notification and Publication`
   * - Authentic Source Management
     - Registration, update and removal of the Authentic Sources in the AS Registry
     - :ref:`onboarding-system:Authentic Source Registration`, :ref:`onboarding-system:Authentic Source Update`, :ref:`onboarding-system:Authentic Source Removal`
   * - Claims and Schema Management
     - Registration of the claims and provisioning of the schemas
     - :ref:`onboarding-system:Claim Registration`, :ref:`onboarding-system:Schema Provisioning`
   * - Catalog Management
     - Registration, activation and versioning of the Credential types in the Digital Credentials Catalog
     - :ref:`onboarding-system:Credential Type Registration`, :ref:`onboarding-system:Credential Type Activation and Deactivation`, :ref:`onboarding-system:Credential Type Update`

The components write to the National registries and data stores described in :ref:`registry:Registry Infrastructure`, which are grouped by purpose as in :ref:`registry:Registries and Catalogues of the Ecosystem`.

Two data stores are kept separate on purpose, the Register, which holds the Wallet-Relying Party registration records defined by [`CIR2025/848`_] and drives the issuance of the certificates, and the notification dataset, which holds the notifiable information defined by [`CIR2024/2980`_] and feeds the Publication Service.
They overlap only in the identification data, so the split keeps the registration distinct from the notification.
 
The diagram below groups the components by responsibility and shows the data stores they interact with.
A component can realize processes of more than one family, so the groups of the diagram do not coincide with the families of :ref:`onboarding-system:Onboarding Processes`, and the correspondence is the one given by the table above.
The Authentic Sources register only in the AS Registry, without a Register record and without Trust Artifacts, since they are neither Wallet-Relying Parties nor Federation Entities.
The Credential Issuers, instead, register as Entities and also declare the Credential types they issue, and they are added to the issuers of the types they declare in the Digital Credentials Catalog.

.. plantuml:: plantuml/onboarding-system-overview.puml
    :width: 99%
    :caption: `IT-Wallet Onboarding System. <https://www.plantuml.com/plantuml/svg/XLRVRzis47xNNt587WO4YRiiIz42Gr77iO4yh0ki37tn2osTPCxKKJXISxoX_tj9YX9OntOLm3_8--w-k_lkdC_62hPTe-3fvUQhK0ej_4LhBRYKL4E-DnQRJ65bmMfWMMyib9Ani59JPhQIMi6Y0RCHfTvvI2MKmUIcn4fqohxWgvqgMLE3PA5mByY9LIkAhQWnjtk5uDqBgbNgPigiTpEjDCFb-_0SNYuqsLp-Xt1xcrmfIMZtBO9ckz791UaI3RPm-o4vP45RV_ZxVN8uqddGN2974dVXISrqH-LCCo53whCKLgo5-GbQ55RpCPCibWOkpdJe0lxFCe3HT8crD9Q5xz8520FjjcQiuN9nx_-SDG2CYJd0rTMNO2mKBB347Wb_2dBkVCUkhbOqcQnegdumc9ELLgAvNb7UhRMd92n2ReKDC0E2IdZXpbZdZBScaAcmXClvtUAtnUDR7lE_7v--GapW58s-3ZTBL7jVX6V1dWNeDX2ZUaMIm6uGWhT8OC6YmPtcRI31M9ycCUqSsELMGAuxBl08XKEJFZLXcfeJlzz-QCiC7SzA5hv6JyPqWWeSsbEuktFzIR372h9ydiwkmRqjtLikQtgNer2-_2iQMpjo3WTGZ2uZ-zVxNp-U93-rpimUTcIWB-nvzah8fbT3Ncom4KToI6ncZAKdwZYRO1xu-Sz9UOz44LOeNH_ndJXqso2cwn8_rwqlEbOd6IBIPzDC8V3es1YqnzW8YxLcBrdJhV_18cnNUXElMvya5mT4OYXOY0MvrOnceEhtJiBLWHDuFn5jnwqsemIjFtIGyCJqODXVOqpa5UdAIwqFjUCspDB3m-DyyV06b6oBwVCJpAbijIJhLqRO7ljaMwpenBeu3F3j89qS6n5cqUDBQGhzB_B-C3-3pPdiXYbnevqF-sSVXph4dtsOlvzzF8c3gDztAueITqucr_0YNZNfPZzidRkVUahbQY2AUb1iYevrI5oa0bnHL6201dKvEOKdoCc12wMxCXrj1rfs2jTQnosv7Y7Hjj-eaLI7e2jmS9Rhpc9iO7hPZtjK9NQEsUWm-mLkt0CS0m9ZXOnKO3ZFNEp9v5DSBgDrePjM4r8O6UCL3xsvamdySNFpAUebyprpNwC-ix2Pmq5ePnPtYJi8JSaSi-6x-vYvsGkVGzd6u6By3sOdxIR-ma0nv6jw9b5gZdpCUCGd6nTa_07eCP5jMC6PV_6v3D8V3s8oeyEuCyHQENzKQMv24qSQWrUNJPPzHYgxHdq7>`_
