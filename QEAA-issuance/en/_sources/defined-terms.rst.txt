.. include:: ../common/common_definitions.rst

.. _defined-terms.rst:


Normative Language and Conventions
++++++++++++++++++++++++++++++++++

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.


Defined Terms
+++++++++++++

The terms *User*, *Trust Service*, *Trust Model*, *Trusted List*, *Trust Framework*, *Attribute*, *Electronic Attestations of Attributes Provider* or *Trust Service Provider (TSP)*, *Person Identification Data (PID)*, *Revocation List*, *Qualified Electronic Attestations of Attributes Provider* or *Qualified Trust Service Provider (QTSP)*, *Electronic Attestation of Attributes (EAA)*, are defined in the `EIDAS-ARF`_.

Below are the description of acronyms and definitions which are useful for further insights into topics that complement the it-wallet and the interacting components.


.. list-table:: 
   :widths: 20 60
   :header-rows: 1

   * - **Claim**
     - **Description**
   * - Accreditation Body
     - An entity accredited by the Federation Authority, responsible for managing the process of verification and certification of accreditation requirements for ecosystem roles.
   * - Digital Identity Provider
     - An entity, recognized and accredited by the State, responsible for identifying citizens for the issuance of an Electronic Identity Certificate.
   * - Electronic Attestation of Identity
     - Electronic attestation of attributes referring to master data already present in Italian digital identity systems.
   * - Federation Authority
     - A public governance entity that issues guidelines and technical rules, and administers - directly or through its intermediary - Trusted Lists, services, and accreditation processes, the status of participants, and their eligibility evaluation. It also performs oversight functions.
   * - Wallet Instance
     - An instance of the Wallet Solution, installed on a personal mobile device and controlled by a specific User who is its sole owner. It is the application that enables citizens to fully and autonomously manage their digital identity and EAAs.
   * - Wallet Provider
     - All public and/or private entities, conforming to a technical profile and accredited by the Federation Authority, that provide citizens with an IT Wallet Instance.
   * - Wallet Instance Attestation
     - Verifiable Attestation, issued by the Wallet Provider, that proves the security compliace of the Wallet Instance.
   * - Qualified Electronic Attestation of Attributes (QEAA)
     - A digitally verifiable attestation in electronic form, issued by a QTSP, that substantiates a person's possession of attributes.
   * - Qualified Electronic Signature Provider
     - The Electronic Trust Service Provider responsible for the issuing of Qualified Electronic Signature certificates to the User.
   * - Relying Party
     - A natural or legal person that implements an authentication system requiring electronic attribute attestation submissions as an authentication mechanism.
   * - Trust Attestation
     - Electronic attestation of an entity's compliance with the national regulatory framework, which is cryptographically verifiable and cannot be repudiated over time by the entity that issued it. A Trust Attestation is always related to a particular Trust Framework.
   * - Trust Layer
     - An architectural component that enables IT Wallet system participants to establish trust, in terms of reliability and compliance of all participants with the regulatory framework governing the digital identity system.
   * - Level of Assurance
     - The degree of confidence in the vetting process used to establish the identity of the User and the degree of confidence that the User who presents the credential is the same User to whom the credential was issued.

Acronyms
--------

.. list-table:: 
  :widths: 20 80
  :header-rows: 1

  * - **Acronym**
    - **Description**
  * - **OID4VP**
    - OpenID for Verifiable Presentation 
  * - **PID** 
    - Person Identification Data
  * - **VC**
    - Verifiable Credential
  * - **VP**
    - Verifiable Presentation
  * - **API**
    - Application Programming Interface
  * - **LoA**
    - Level of Assurance

