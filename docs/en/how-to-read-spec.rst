.. include:: ../common/common_definitions.rst
.. Included via introduction.rst at title level '-' (level 1).

How to Read the Specification
-----------------------------

This specification is designed to fulfil the requirements from multiple stakeholders within the IT-Wallet System. Each role has different responsibilities and scopes, and therefore different information needs. This section provides tailored reading paths to help you navigate efficiently to the content most relevant to the implementation goals.

Specification Structure Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The specification is organized into the following major sections:

- **Section** :ref:`introduction:Introduction`:
  Establishes scope, and normative language for the IT-Wallet ecosystem.

- **Section** :ref:`architecture-overview:Architecture Overview`:
  Provides high-level view on the Architecture in terms of governance and operational processes enabled.

- **Section** :ref:`brand-identity:Brand Identity`:
  Provides the IT-Wallet Brand Identity requirements, guidance on the naming convention and on the application of the visual elements that identify the ecosystem.

- **Section** :ref:`functionalities:User Experience Design`:
  Provides design principles and high-level functional requirements to ensure a high-quality User Experience across all stages of interaction between the User and the service.

- **Section** :ref:`infrastructure-trust:Infrastructure of Trust`:
  Defines the federation-based trust model, entity relationships, and trust evaluation mechanisms that secure the entire ecosystem.

- **Section** :ref:`entities:Entities`:
  Comprehensive implementation requirements for each ecosystem participant: Wallet Solutions, Credential Issuers, Relying Parties, and Authentic Sources, including their components, interaction patterns, and configuration requirements.

- **Section** :ref:`digital-credential-management:Digital Credential Management`:
  Covers Digital Credential data models and formats, lifecycle management, validity verification, and the Credentials Catalog structure.

- **Section** :ref:`digital-credential-flows:Digital Credential Flows`:
  Detailed implementation guidance for Digital Credential issuance and presentation workflows, including both remote and proximity interaction flows.

- **Section** :ref:`endpoints:Endpoints`:
  Technical specifications for all API endpoints exposed by each entity type, including federation endpoints and specialized service integrations.

- **Section** :ref:`algorithms:Cryptographic Algorithms`, :ref:`security-privacy-considerations:Security and Privacy Considerations`, and :ref:`log-retention-policy:General Log Retention Policies` (**Implementation Support**):
  Cryptographic requirements, security and privacy considerations, and log retention policies essential for compliant implementations.

- **Section** :ref:`defined-terms-and-references:Defined Terms and References`, :ref:`official-resources:Official Resources`, :ref:`contribute:How to contribute`, and :ref:`open-source:Open Source Releases` (**Terminology and References**):
  Comprehensive terminology, normative references, additional documentation, tools, resources and contribution guidelines.

- **Section** :ref:`appendix:Appendix`:
  Provides supplementary technical details, implementation patterns, and testing frameworks including mobile application instance management, national platform integration specifications, and comprehensive test matrices for ecosystem validation.


Reading Paths by Role
^^^^^^^^^^^^^^^^^^^^^

For easier access to the topics covered in these specifications, role-based reading paths are presented below. Each path is organized according to the different stages of onboarding to and participation in the IT-Wallet System, with direct references to the sections most relevant to each role.

The proposed reading paths are intended as guidance and do not replace the need to consult other sections when a broader understanding of the system is required.

For entities interested in addressing multiple roles, it is recommended to deepen all the reading paths related to relevant roles.

Authentic Source
~~~~~~~~~~~~~~~~

The Authentic Source focuses on securely exposing, managing, and guaranteeing the absolute accuracy and integrity of the authoritative raw data underlying (Q)EAA.

**Phase 1: Discovery**

To understand the general functioning of the ecosystem, the technical architecture and the Infrastructure of Trust.

- **Section** :ref:`introduction:Introduction`: Scope and regulatory context of the IT-Wallet System.

- **Section** :ref:`architecture-overview:Architecture Overview`: Overview of the IT-Wallet System architecture in terms of governance and enabled operational processes.

- **Section** :ref:`infrastructure-trust:Infrastructure of Trust`: Key requirements of the federation-based trust model and trust evaluation mechanisms between entities.

- **Section** :ref:`defined-terms-and-references:Defined Terms and References`: Comprehensive terminology, normative references, additional documentation, tools, resources and contribution guidelines.

**Phase 2: Design**

To understand the requirements and design the features, functionalities and specific characteristics underlying a (Q)EAA to be issued.

- **Section** :ref:`functionalities:User Experience Design`: Key requirements on how to enable Users to obtain (Q)EAAs, (Q)EAA structures, status and management over time.

- **Section** :ref:`digital-credential-management:Digital Credential Management`: Technical and functional requirements related to (Q)EAA lifecycle.

- **Section** :ref:`e-service-pdnd-template:PDND e-Service Template`: Standardized blueprint containing all necessary technical and descriptive metadata for the e-service definition.

**Phase 3: Implementation**

To implement the technological interfaces required to communicate with Credential Issuers and to manage the entire (Q)EAA data lifecycle.

- **Section** :ref:`authentic-sources:Authentic Sources`: Authentic Source role and responsibilities.

- **Section** :ref:`e-service-pdnd:e-Service PDND`: Mandatory integration specifications with the PDND (National Digital Data Platform) and the associated interoperability requirements for publishing an e-service.

- **Section** :ref:`authentic-source-endpoint:Authentic Source Endpoints`: Key requirements for the implementation of APIs enabling the Credential Issuer to securely and consistently retrieve authoritative data and to manage the data lifecycle through Signal Hub endpoints.

- **Section** :ref:`registry:Registry Infrastructure`: Focus on Registry components of interest to the Authentic Source.

- **Section** :ref:`log-retention-policy:General Log Retention Policies`: General log retention requirements and specific requirements for Authentic Sources in accordance with ISO/IEC 27001.

- **Section** :ref:`test-plans:Test Plans`: Guide to set up the test environment and validate backend interactions with the test matrices provided by the ecosystem.

**Phase 4: Registration**

To become registered as an Authentic Source within the system by completing the administrative and technical procedures required.

- **Section** :ref:`onboarding-system:Overview`: Overview of the onboarding system architecture and the Authentic Source registration process.

- **Section** :ref:`onboarding-system:Authentic Source Registration`: Focus on technical implementation procedures for Authentic Source registration.

- **Section** :ref:`infrastructure-trust:X.509 Certificate Profile`: Operational procedures for managing X.509 Certificates within the IT-Wallet federation.


Wallet Provider
~~~~~~~~~~~~~~~

The Wallet Provider focuses on designing and developing the Wallet Solution that enables the User to store, manage, and present their PID and (Q)EAAs.

**Phase 1: Discovery**

To understand the general functioning of the ecosystem, the technical architecture and the Infrastructure of Trust.

- **Section** :ref:`introduction:Introduction`: Scope and regulatory context of the IT-Wallet System.

- **Section** :ref:`architecture-overview:Architecture Overview`: Overview of the IT-Wallet System architecture in terms of governance and enabled operational processes.

- **Section** :ref:`infrastructure-trust:Infrastructure of Trust`: Key requirements of the federation-based trust model and trust evaluation mechanisms between entities.

- **Section** :ref:`defined-terms-and-references:Defined Terms and References`: Comprehensive terminology, normative references, additional documentation, tools, resources and contribution guidelines.

**Phase 2: Design**

To understand the User Experience requirements and design the Wallet Solution following common patterns to ensure the usability and accessibility of the solutions.

- **Section** :ref:`brand-identity:Brand Identity`: Overview of the IT-Wallet Brand Identity and indications on assets to be adopted by the Wallet Provider.

- **Section** :ref:`functionalities:User Experience Design`: Key requirements on Interaction Models and Interface layouts and graphic assets to ensure an effective and seamless User Experience and coherence among Wallet Solutions.

- **Section** :ref:`digital-credential-management:Digital Credential Management`: Technical and functional requirements related to (Q)EAA lifecycle.

**Phase 3: Implementation**

To implement the Wallet Solution in line with specific technological standards to ensure the communication between the Wallet Solution and other actors.

- **Section** :ref:`wallet-solution:Wallet Solution`: Technical and functional requirements on components, functionalities and lifecycle to configure the Wallet Solution.

- **Section** :ref:`digital-credential-flows:Digital Credential Flows`: Technical and functional requirements on (Q)EAA issuance and presentation flows.

- **Section** :ref:`wallet-provider-endpoint:Wallet Provider Endpoints`: Key requirements for the implementation of the Wallet Provider interfaces (APIs) required for interoperability among entities.

- **Section** :ref:`registry:Registry Infrastructure`: Overview of Registry infrastructure and federation Registry.

- **Section** :ref:`algorithms:Cryptographic Algorithms`: Selection and implementation of cryptographic standards required to secure keys and transactions.

- **Section** :ref:`security-privacy-considerations:Security and Privacy Considerations`: Security and compliance requirements for Wallet Solutions.

- **Section** :ref:`log-retention-policy:General Log Retention Policies`: General log retention requirements and requirements specific for Wallet Providers, in accordance with ISO/IEC 27001.

- **Section** :ref:`mobile-application-instance:Mobile Application Instance`: Requirements for mobile application instance, related to initialization request and response.

- **Section** :ref:`test-plans:Test Plans`: Guide to set up the test environment and validate backend interactions with the test matrices provided by the ecosystem.

**Phase 4: Registration**

To become registered as a Wallet Provider within the system by completing the administrative and technical procedures so that the Wallet Solution is recognized by the system.

- **Section** :ref:`onboarding-system:Overview`: Overview of the onboarding system architecture and the Wallet Provider registration process.

- **Section** :ref:`onboarding-system:Entity Registration`: Focus on technical implementation procedures for Wallet Provider registration.

- **Section** :ref:`infrastructure-trust:X.509 Certificate Profile`: Operational procedures for managing X.509 Certificates within the IT-Wallet federation.


Credential Issuer
~~~~~~~~~~~~~~~~~

The Credential Issuer focuses on transforming authoritative raw data from Authentic Sources into (Q)EAAs, and managing their entire lifecycle from issuance to revocation or expiration.

**Phase 1: Discovery**

To understand the general functioning of the ecosystem, the technical architecture and the Infrastructure of Trust.

- **Section** :ref:`introduction:Introduction`: Scope and regulatory context of the IT-Wallet System.

- **Section** :ref:`architecture-overview:Architecture Overview`: Overview of the IT-Wallet System architecture in terms of governance and enabled operational processes.

- **Section** :ref:`infrastructure-trust:Infrastructure of Trust`: Key requirements of the federation-based trust model and trust evaluation mechanisms between entities.

- **Section** :ref:`defined-terms-and-references:Defined Terms and References`: Comprehensive terminology, normative references, additional documentation, tools, resources and contribution guidelines.

**Phase 2: Design**

To understand the requirements and technically design (Q)EAA by structuring metadata to meet technical and regulatory requirements.

- **Section** :ref:`functionalities:User Experience Design`: Key requirements on (Q)EAA structure, issuance, status and management over time.

- **Section** :ref:`digital-credential-management:Digital Credential Management`: Technical and functional requirements related to (Q)EAA lifecycle.

**Phase 3: Implementation**

To develop endpoints based on specific protocols, and to implement (Q)EAA issuance, renewal, revocation and all the technical lifecycle management functions.

- **Section** :ref:`credential-issuer-solution:Credential Issuer Solution`: Technical and functional requirements on components and interaction patterns to issue and manage (Q)EAAs lifecycle.

- **Section** :ref:`digital-credential-flows:Digital Credential Flows`: Technical and functional requirements on (Q)EAA issuance and presentation flows.

- **Section** :ref:`credential-issuer-endpoint:Credential Issuer Endpoints`: Key requirements for the implementation of Credential Issuer metadata and authorization endpoints.

- **Section** :ref:`algorithms:Cryptographic Algorithms`: Selection and implementation of cryptographic standards required to secure keys and transactions.

- **Section** :ref:`e-service-pdnd:e-Service PDND`: Mandatory integration specifications with the PDND (National Digital Data Platform) and the associated interoperability requirements for accessing authoritative data required for (Q)EAA issuance.

- **Section** :ref:`security-privacy-considerations:Security and Privacy Considerations`: Security and compliance requirements for implemented solutions.

- **Section** :ref:`log-retention-policy:General Log Retention Policies`: General log retention requirements and requirements specific for Credential Issuers in accordance with ISO/IEC 27001.

- **Section** :ref:`test-plans:Test Plans`: Guide to set up the test environment and validate backend interactions with the test matrices provided by the ecosystem.

**Phase 4: Registration**

To become registered as a Credential Issuer within the system, by completing the administrative and technical procedure so that (Q)EAA issued to the Wallet are officially trusted.

- **Section** :ref:`onboarding-system:Overview`: Overview of the onboarding system architecture and the Credential Issuer registration process.

- **Section** :ref:`onboarding-system:Entity Registration`: Focus on technical implementation procedures for Credential Issuer registration.

- **Section** :ref:`infrastructure-trust:X.509 Certificate Profile`: Operational procedures for managing X.509 Certificates within the IT-Wallet federation.


Relying Party
~~~~~~~~~~~~~

The Relying Party focuses on securely requesting, receiving, and verifying the authenticity and validity of the PID and (Q)EAAs presented by the User to grant access to online and offline services.

**Phase 1: Discovery**

To understand the general functioning of the ecosystem, the technical architecture and the Infrastructure of Trust.

- **Section** :ref:`introduction:Introduction`: Scope and regulatory context of the IT-Wallet System.

- **Section** :ref:`architecture-overview:Architecture Overview`: Overview of the IT-Wallet System architecture in terms of governance and enabled operational processes.

- **Section** :ref:`infrastructure-trust:Infrastructure of Trust`: Key requirements of the federation-based trust model and trust evaluation mechanisms between entities.

- **Section** :ref:`defined-terms-and-references:Defined Terms and References`: Comprehensive terminology, normative references, additional documentation, tools, resources and contribution guidelines.

**Phase 2: Design**

To understand the User Experience requirements and design the verification functionalities necessary to provide the service to the end User.

- **Section** :ref:`brand-identity:Brand Identity`: Overview of the IT-Wallet Brand Identity and indications on assets to be adopted by the Relying Party.

- **Section** :ref:`functionalities:User Experience Design`: Key requirements on Interaction Models, Interface layouts and graphic assets to ensure an effective and seamless User Experience, and coherence among presentation and verification systems.

- **Section** :ref:`digital-credential-management:Digital Credential Management`: Technical and functional requirements related to (Q)EAA lifecycle.

**Phase 3: Implementation**

To implement verification functionalities following specific protocols, to send verification requests to the Wallet and receive a response with the User authorization.

- **Section** :ref:`relying-party-solution:Relying Party Solution`: Technical and functional requirements on components and functionalities for PID and (Q)EAA verification.

- **Section** :ref:`digital-credential-flows:Digital Credential Flows`: Technical and functional requirements on (Q)EAA presentation and verification flows.

- **Section** :ref:`relying-party-endpoints:Relying Party Endpoints`: Key requirements for the implementation of (Q)EAA verification endpoints.

- **Section** :ref:`security-privacy-considerations:Security and Privacy Considerations`: Security and compliance requirements for implemented solutions.

- **Section** :ref:`log-retention-policy:General Log Retention Policies`: General log retention requirements and requirements specific for Relying Parties, in accordance with ISO/IEC 27001.

- **Section** :ref:`test-plans:Test Plans`: Guide to set up the test environment and validate backend interactions with the test matrices provided by the ecosystem.

**Phase 4: Registration**

To become registered as a Relying Party within the system, by completing the administrative and technical procedure and becoming a reliable actor when requesting User data.

- **Section** :ref:`onboarding-system:Overview`: Overview of the onboarding system architecture and the Relying Party registration process.

- **Section** :ref:`onboarding-system:Entity Registration`: Focus on implementation procedures for Relying Party registration.

- **Section** :ref:`infrastructure-trust:X.509 Certificate Profile`: Operational procedures for managing X.509 Certificates within the IT-Wallet federation.
