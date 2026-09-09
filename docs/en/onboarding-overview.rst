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
   * - Supervisory Body
     - Eligibility and compliance verification, approval of claims, schemas and Credential types
     - Precondition to every registration, see :ref:`onboarding-system:Eligibility and Compliance Preconditions`
   * - National Federation Management
     - Federation registration, issuance of Trust Marks, publication of the signed registries
     - :ref:`onboarding-system:Entity Registration`
   * - EUDIW Registration Management
     - Verification and registration of the Wallet-Relying Parties in the Register
     - :ref:`onboarding-system:Entity Registration`
   * - Certificate Management
     - Issuance and update of WRPAC, WRPRC, Sign/Seal and National Authentication certificates
     - :ref:`onboarding-system:Certificate and Trust Artifact Issuance`
   * - EU Notification Management
     - Signature of the EU Member State Trusted List and notification to the European Commission
     - :ref:`onboarding-system:Notification and Publication`
   * - Authentic Source Management
     - Registration of the Authentic Sources in the AS Registry
     - :ref:`onboarding-system:Authentic Source Registration`
   * - Claims and Schema Management
     - Registration of the claims and provisioning of the schemas
     - :ref:`onboarding-system:Attestation Onboarding`
   * - Catalog Management
     - Registration, activation and versioning of the Credential types in the Digital Credentials Catalog
     - :ref:`onboarding-system:Attestation Onboarding`

The components write to the National registries and data stores described in :ref:`registry:Registry Infrastructure`.
At the EU level, they interact with the European Commission for catalog notification and alignment.

Two data stores are kept separate on purpose, the Register, which holds the Wallet-Relying Party registration records defined by [`CIR2025/848`_] and drives the issuance of the certificates, and the notification dataset, which holds the notifiable information defined by [`CIR2024/2980`_] and feeds the Publication Service.
They overlap only in the identification data, so the split keeps the registration distinct from the notification.
 
The diagram below shows the components, the actors that interact with them and the data stores they write.
The Authentic Sources register only in the AS Registry, without a Register record and without Trust Artifacts, since they are neither Wallet-Relying Parties nor Federation Entities.
The Credential Issuers, instead, register as Entities and also declare the Credential types they issue, and they are added to the issuers of the types they declare in the Digital Credentials Catalog.

.. plantuml:: plantuml/onboarding-system-overview.puml
    :width: 99%
    :caption: `IT-Wallet Onboarding System. <https://www.plantuml.com/plantuml/svg/bLPBRnen4Bv7odyOaKDR54YZD7qTgi9c8wLIMnHIfGSkPZqi5bvxPNkJqAh_lJFUXIoF9ggH4FOyFT_CPpxx85oe2WrNDxrReJK6-6wcLZYfJ0xZfGzO71ved0K85fpAvm6aSfW5PStXWLyeKmed2l1p8Uqz6ys4zjWMIPo9IeSRV0W3hN9Je0cGqHUwjbefieN8SHoM6e4Z29Fh3KS3v-nzOhLrSFGshXtffJLXh7uXd9wsPLeP3CiImRemjss9iH8zbd3wldtgX5dmwPlpZTDLKaFh9BecaxEuDlHiPMHYdK476swb268g_7Fs8WlMxTKvF8Wow8oh4jsTyjOjOMZbiWF2Wv057AMdmpHznwfDGQ7p1BOT-Csg06lbGGX8NS7ujjIZ_tAHYn3WwFASFsm9jDPLWKwtEwZ2d91L6OnjvJBiTc5Ykjslmf1p1hxRdPX-VsAs5Nrz0r_aTDtaVVes-R37VQA5AaZDI1XdSop4V_htsVoP08IGjZbxWRrkjOR4eMJNWgR6-mfTxJiJOSltdwtIfcGKbdkgoWFnL5M_HJWetYL5TZKs-tEB8LHpsndA9wwQ_hYukeLhp9KF__IvUzTZCj5Bxg0HKGU5EfwOziaIhdYo2vHAE19FZ2rZpYHN1kgeKvuGuUgsTPZ3qN1uaLuEzo6256McgBgu9x-V_VFN7s8_VBcz8GeWLPeG3ozlhqU3v8I-hvDNCSe3AxR2DE1ibGI-sIRQ_dgChYxW14RLi9SE1Z1ozav9Bih4D1EsFggnhQQFCJTweQax5IXcVq5z1sCQxGOwQWecY-skM148T5OjGR2FLo0sBE1ZGTkuxvf1Cqad4rCF4lle7yEDUB365cjWpfvpr6uH3ytuhERXNyQn2RXjE6rqKVtUbJkDi6EnWGxNp6E8reO5M_16X3DjAxd1QXItqZYrTb5VaX1AurehfvMZdXMacTYYKDwJLTJ5x57tyE05z6Y1Rr7nbAWOY2G9LPOHNHCbztgVLjJv4UmTzGRMg4zCpblZD_IO33u2qakffaepOKJLp1QbLi9as8hjcfiGL3DqIC8cBjsgt__KS5BBWBrOmo7eEVVSR_3otYbA-DKguqZ1d4ji97gNQixa4su8gb9DT7n0FoaMmSQR6a5wTwZfUHyngRUS2sRjF5fJJGMkn6FgBo9liGCUsKVtzOxyrIMArQgcVF8PZQJ_C7y1>`_
