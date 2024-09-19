.. include:: ../common/common_definitions.rst

.. _trust.rst:

The Infrastructure of Trust
+++++++++++++++++++++++++++

The EUDI Wallet Architecture Reference Framework (`EIDAS-ARF`_) describes the Trust Model as a *"collection of rules that ensure the legitimacy of the components and the entities involved in the EUDI Wallet ecosystem"*.

This section outlines the implementation of the Trust Model in an infrastructure that complies with OpenID Federation 1.0 `OID-FED`_. This infrastructure involves a RESTful API for distributing metadata, metadata policies, trust marks, public keys, X.509 certificates, and the revocation status of the participants, also called Federation Entities.

The Infrastructure of trust facilitates the application of a trust assessment mechanism among the parties defined in the `EIDAS-ARF`_.

..  figure:: ../../images/trust-roles.svg
    :alt: federation portrait
    :width: 100%
   
    The roles within the Federation, where the Trust Anchor oversees its subordinates,
    which include one or more Intermediates and Leaves. In this
    representation, both the Trust Anchor and the Intermediates assume the role of Registration Authority.

Federation Roles
------------------

All the participants are Federation Entities that MUST be registered by an Registration Body,
except for Wallet Instances which are End-User's personal devices certified by their Wallet Provider.

.. note::
    The Wallet Instance, as a personal device, is certified as reliable through a verifiable attestation issued and signed by a trusted third party.

    This is called *Wallet Attestation* and is documented in `the dedicated section  <Wallet Attestation>`_.


Below the table with the summary of the Federation Entity roles, mapped on the corresponding EUDI Wallet roles, as defined in the `EIDAS-ARF`_.

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - EUDI Role
     - Federation Role
     - Notes
   * - Public Key Infrastructure (PKI)
     - Trust Anchor
     - The Federation has PKI capabilities. The Entity that configures the entire infrastructure is the Trust Anchor.
   * - Qualified Trust Service Provider (QTSP)
     - Leaf
     - 
   * - Person Identification Data Provider
     - Leaf
     - 
   * - Qualified Electronic Attestations of Attributes Provider
     - Leaf
     - 
   * - Electronic Attestations of Attributes Provider
     - Leaf
     - 
   * - Relying Party
     - Leaf
     - 
   * - Trust Service Provider (TSP)
     - Leaf
     - 
   * - Trusted List
     - Trust Anchor
     - The listing endpoint, the trust mark status endpoint, and the fetch endpoint must be exposed by both Trust Anchors and Intermediates, making the Trusted List distributed over multiple Federation Entities, where each of these is responsible for their registered subordinates.
   * - Wallet Provider
     - Leaf
     - 


General Properties
------------------

The architecture of the trust infrastructure based on OpenID Federation is built upon several core principles:

- [P1] **Security**: incorporates mechanisms to ensure the integrity, confidentiality, and authenticity of the trust relationships and interactions within the federation.
- [P2] **Privacy**: designed to respect and protect the privacy of the entities and individuals involved, minimal disclosure is part of this.
- [P3] **Interoperability**: supports seamless interaction and trust establishment between diverse systems and entities within the federation.
- [P4] **Transitive Trust**: trust established indirectly through a chain of trusted relationships, enabling entities to trust each other based on common authorities and trusted intermediaries.
- [P6] **Scalability**: designed to efficiently manage an increasing number of entities or interactions without a significant increase in trust management complexity.
- [P5] **Delegation**: technical ability/feature to delegate authority or responsibilities to other entities, allowing for a distributed trust mechanism.
- [P7] **Flexibility**: adaptable to various operational and organizational needs, allowing entities to define and adjust their trust relationships and policies.
- [P8] **Autonomy**: while part of a federated ecosystem, each entity retains control over its own definitions and configurations.
- [P9] **Decentralization**: unlike traditional centralized systems, the OpenID Federation model promotes a decentralized approach. This ensures that no single entity has control over the entire system, enhancing privacy and security for all participants. 

Trust Infrastructure Functional Requirements
----------------------------------------------

This section includes the requirements necessary for the successful implementation and operation of the infrastructure of trust.

.. list-table:: Functional Requirements
   :header-rows: 1

   * - ID
     - Description
   * - [FR #1]
     - **Federation Trust Establishment**: the system must be able to establish trust between different entities (Credential Issuers, Relying Parties, etc.) within a federation, using cryptographic signatures for secure information exchange about the participants in the ecosystem.
   * - [FR #2]
     - **Entity Authentication**: the system must implement mechanisms for authenticating entities within the federation, ensuring compliance with the shared rules.
   * - [FR #3]
     - **Signature Validation**: the system must support the creation, verification, and validation of electronic signatures and provide standard and secure mechanisms to obtain the public keys required for the signature validation.
   * - [FR #4]
     - **Time Stamping**: the signed artifacts must contain time stamps to ensure the integrity and non-repudiation of transactions over time, thanks to the interfaces, services, storage model and approaches defined within the federation.
   * - [FR #5]
     - **Certificate Validation**: the system requires confidential transmission, secured via TLS over HTTP, and validation of certificates for website authentication, ensuring they meet eIDAS criteria.
   * - [FR #6]
     - **Interoperability and Standards Compliance**: ensure interoperability between federation members by adhering to technical standards, facilitating cross-border electronic transactions.
   * - [FR #7]
     - **Data Protection and Privacy**: implement data protection measures in compliance with GDPR and eIDAS regulations, ensuring the privacy and security of personal data processed within the federation.
   * - [FR #8]
     - **User Consent and Control**: design mechanisms for obtaining and managing user consent, empowering users with control over their personal information.
   * - [FR #9]
     - **Audit and Logging**: the system must minimize data, anonymize if possible, define retention periods, secure access, and storage encryption. This protects privacy while enabling security and accountability.
   * - [FR #10]
     - **Dispute Resolution and Liability**: establish clear procedures for dispute resolution and define liability among federation members, in accordance with eIDAS provisions.
   * - [FR #11]
     - **Accessibility**: ensure that the system is accessible to all users, including those with disabilities, aligning with eIDAS and local accessibility standards.
   * - [FR #12]
     - **Emergency and Revocation Services**: implement mechanisms for the immediate revocation of electronic identification means and participants in case of security breaches or other emergencies.
   * - [FR #13]
     - **Scalable Trust Infrastructure**: the system must support scalable trust establishment mechanisms, leveraging approaches and technical solutions that complement delegation transitive approaches to efficiently manage trust relationships as the federation grows, removing central registries that might technically or administratively fail.
   * - [FR #14]
     - **Efficient Storage Scalability**: implement a storage solution that scales horizontally to accommodate increasing data volumes while minimizing central storage and administrative costs. The system should enable members to independently store and present historical trust attestations and signed artifacts during dispute resolutions, with the federation infrastructure maintaining only a registry of historical keys to validate the historical data, stored and provided by the participants.
   * - [FR #15]
     - **Verifiable Attestation (Trust Mark)**: incorporate a mechanism for issuing and verifying verifiable attestations that serve as proof of compliance with specific profiles or standards. This allows entities within the federation to demonstrate adherence to agreed-upon security, privacy, and operational standards.
   * - [FR #16]
     - **Dynamic Policy Language**: develop and implement a dynamic, extensible policy language that allows for the creation and modification of federation policies in response to evolving requirements, technological advancements, and regulatory changes. This policy language should support the specification of rules governing entity behavior, metadata handling, and trust validation within the federation.
   * - [FR #17]
     - **Automated Policy Enforcement**: the system must automatically enforce federation policies as defined by policy language and verifiable attestations, ensuring that all operations and transactions comply with current rules and standards.
   * - [FR #18]
     - **Decentralized Dispute Resolution Mechanism**: design a decentralized mechanism for dispute resolution that allows federation members to independently verify historical trust establishment and signed artifacts, reducing reliance on central authorities and streamlining the resolution process.
   * - [FR #19]
     - **Adaptive Load Management**: implement adaptive load management strategies to ensure the system remains responsive and efficient under varying loads, particularly during peak usage times or when processing complex tasks.
   * - [FR #20]
     - **Cross-Federation Interoperability**: ensure the system is capable of interoperating with other federations or trust frameworks, facilitating cross-federation transactions and trust establishment without compromising security or compliance.
   * - [FR #21]
     - **Future-Proof Cryptography**: the system should employ a flexible cryptographic framework that can be updated in response to new threats or advancements in cryptographic research, ensuring long-term security and integrity of federation operations.
   * - [FR #23]
     - **Autonomous Registration Bodies**: the system must facilitate the integration of autonomous registration bodies that operate in compliance with federation rules. These bodies are tasked with evaluating and registering entities within the federation, according to the pre-established rules and their compliance that must be periodically asserted.
   * - [FR #24]
     - **Compliance Evaluation for Federation Entity Candidates**: registration bodies must evaluate the compliance of candidate entities against federation standards before their registration in the federation.
   * - [FR #25]
     - **Periodic Auditing of Registration Bodies and Entities**: implement mechanisms for the periodic auditing and monitoring of the compliance status of both registration bodies and their registered entities. This ensures ongoing adherence to federation standards and policies.
   * - [FR #26]
     - **Certification of Compliance for Personal Devices**: trusted bodies, in the form of federation entities, should issue certifications of compliance and provide signed proof of such compliance for the hardware of personal devices used within the federation. These certifications should be attested and periodically renewed to ensure the devices meet current security standards.
   * - [FR #27]
     - **Certification of Compliance for Cryptographic Devices**: similar to personal devices, personal cryptographic devices used within the federation must also receive certifications of compliance and signed proof thereof from trusted bodies. These certifications should be subject to periodic renewal to reflect the latest security and compliance standards.
   * - [FR #28]
     - **Transparent Compliance Reporting**: develop a system for transparent reporting and publication of compliance statuses, audit results, and certification renewals for all federation entities. This transparency fosters trust within the federation and with external stakeholders.
   * - [FR #29]
     - **Automated Compliance Monitoring**: the system should include automated tools for monitoring the compliance of entities with federation standards. This automation aids in the early detection of potential compliance issues.
   * - [FR #30]
     - **Secure Protocol Capabilities Binding**: the secure protocol must enable the exchange of protocol-specific capabilities data as cryptographically-bound metadata attached to a specific identity. This metadata should define the technical capabilities associated with the identity, ensuring verifiable proof and tamper-proof association for robust trust establishment and access control.


Federation API endpoints
------------------------

OpenID Federation 1.0 uses RESTful Web Services secured over
HTTPs. OpenID Federation 1.0 defines which are the web endpoints that the participants MUST make
publicly available. The table below summarises the endpoints and their scopes.

All the endpoints listed below are defined in the `OID-FED`_ specs.

.. list-table::
   :widths: 20 20 20 20
   :header-rows: 1

   * - endpoint name
     - http request
     - scope
     - required for
   * - federation metadata
     - **GET** .well-known/openid-federation
     - Metadata that an Entity publishes about itself, verifiable with a trusted third party (Superior Entity). It's called Entity Configuration.
     - Trust Anchor, Intermediate, Wallet Provider, Relying Party, Credential Issuer
   * - subordinate list endpoint
     - **GET** /list
     - Lists the Subordinates.
     - Trust Anchor, Intermediate
   * - fetch endpoint
     - **GET** /fetch?sub=https://rp.example.org
     - Returns a signed document (JWS) about a specific subject, its Subordinate. It's called Entity Statement.
     - Trust Anchor, Intermediate
   * - trust mark status
     - **POST** /status?sub=...&trust_mark_id=...
     - Returns the status of the issuance (validity) of a Trust Mark related to a specific subject.
     - Trust Anchor, Intermediate
   * - historical keys
     - **GET** /historical-jwks
     - Lists the expired and revoked keys, with the motivation of the revocation.
     - Trust Anchor, Intermediate


All the responses of the federation endpoints are in the form of JWS, with the exception of the **Subordinate Listing endpoint** and the **Trust Mark Status endpoint** that are served as plain JSON by default.


Configuration of the Federation
-------------------------------

The configuration of the federation is published by the Trust Anchor within its Entity Configuration, it is available at the well-known web path corresponding to **.well-known/openid-federation**.

All the participants in the federation MUST obtain the federation configuration before entering the operational phase, and they
MUST keep it up-to-date. The federation configuration is the Trust Anchor's Entity Configuration, it contains the 
public keys for signature operations and the maximum number of Intermediates allowed between a Leaf and the Trust Anchor (**max_path_length**).

Below is a non-normative example of a Trust Anchor Entity Configuration, where each parameter is documented in the `OpenID Federation <OID-FED>`_ specification:

.. code-block:: text

    {
        "alg": "ES256",
        "kid": "FifYx03bnosD8m6gYQIfNHNP9cM_Sam9Tc5nLloIIrc",
        "typ": "entity-statement+jwt"
    }
    .
    {
        "exp": 1649375259,
        "iat": 1649373279,
        "iss": "https://registry.eidas.trust-anchor.example.eu",
        "sub": "https://registry.eidas.trust-anchor.example.eu",
        "jwks": {
            "keys": [
                {

                    "kty": "EC",
                    "kid": "X2ZOMHNGSDc4ZlBrcXhMT3MzRmRZOG9Jd3o2QjZDam51cUhhUFRuOWd0WQ",
                    "crv": "P-256",
                    "x": "1kNR9Ar3MzMokYTY8BRvRIue85NIXrYX4XD3K4JW7vI",
                    "y": "slT14644zbYXYF-xmw7aPdlbMuw3T1URwI4nafMtKrY"
                }
            ]
        },
        "metadata": {
            "federation_entity": {
                "organization_name": "example TA",
                "contacts":[
                    "tech@eidas.trust-anchor.example.eu"
                ],
                "homepage_uri": "https://registry.eidas.trust-anchor.example.eu",
                "logo_uri":"https://registry.eidas.trust-anchor.example.eu/static/svg/logo.svg",
                "federation_fetch_endpoint": "https://registry.eidas.trust-anchor.example.eu/fetch",
                "federation_resolve_endpoint": "https://registry.eidas.trust-anchor.example.eu/resolve",
                "federation_list_endpoint": "https://registry.eidas.trust-anchor.example.eu/list",
                "federation_trust_mark_status_endpoint": "https://registry.eidas.trust-anchor.example.eu/trust_mark_status"
            }
        },
        "trust_mark_issuers": {
            "https://registry.eidas.trust-anchor.example.eu/openid_relying_party/public": [
                "https://registry.spid.eidas.trust-anchor.example.eu",
                "https://public.intermediary.spid.org"
            ],
            "https://registry.eidas.trust-anchor.example.eu/openid_relying_party/private": [
                "https://registry.spid.eidas.trust-anchor.example.eu",
                "https://private.other.intermediary.org"
            ]
        },
        "constraints": {
            "max_path_length": 1
        }
    }


Entity Configuration
--------------------

The Entity Configuration is the verifiable document that each Federation Entity MUST publish on its own behalf, in the **.well-known/openid-federation** endpoint.

The Entity Configuration HTTP Response MUST set the media type to `application/entity-statement+jwt`.

The Entity Configuration MUST be cryptographically signed. The public part of this key MUST be provided in the
Entity Configuration and within the Entity Statement issued by a immediate superior and related to its subordinate Federation Entity.

The Entity Configuration MAY also contain one or more Trust Marks.

.. note::
  **Entity Configuration Signature**

  All the signature-check operations regarding the Entity Configurations, Entity Statements and Trust Marks, are carried out with the Federation public keys. For the supported algorithms refer to Section `Cryptografic Algorithm`.

Entity Configurations Common Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Entity Configurations of all the participants in the federation MUST have in common the parameters listed below.


.. list-table::
   :widths: 20 60
   :header-rows: 1

   * - **Claim**
     - **Description**
   * - **iss**
     - String. Identifier of the issuing Entity.
   * - **sub**
     - String. Identifier of the Entity to which it is referred. It MUST be equal to ``iss``.
   * - **iat**
     - UNIX Timestamp with the time of generation of the JWT, coded as NumericDate as indicated at :rfc:`7519`.
   * - **exp**
     - UNIX Timestamp with the expiry time of the JWT, coded as NumericDate as indicated at :rfc:`7519`.
   * - **jwks**
     - A JSON Web Key Set (JWKS) :rfc:`7517` that represents the public part of the signing keys of the Entity at issue. Each JWK in the JWK set MUST have a key ID (claim kid) and MAY have a `x5c` parameter, as defined in :rfc:`7517`. It contains the Federation Entity Keys required for the operations of trust evaluation.
   * - **metadata**
     - JSON Object. Each key of the JSON Object represents a metadata type identifier
       containing JSON Object representing the metadata, according to the metadata 
       schema of that type. An Entity Configuration MAY contain more metadata statements, but only one for each type of
       metadata (<**entity_type**>). the metadata types are defined in the section `Metadata Types <Metadata Types>`_.


Entity Configuration Trust Anchor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Trust Anchor Entity Configuration, in addition of the common parameters listed above, MAY contain the following parameters:

.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Required**
   * - **constraints**
     - JSON Object that describes the trust evaluation mechanisms bounds. It MUST contain the attribute **max_path_length** that
       defines the maximum number of Intermediates between a Leaf and the Trust Anchor.
     - |check-icon|
   * - **trust_mark_issuers**
     - JSON Array that defines which Federation authorities are considered trustworthy
       for issuing specific Trust Marks, assigned with their unique identifiers.
     - |uncheck-icon|
   * - **trust_mark_owners**
     - JSON Array that lists which entities are considered to be the owners of
       specific Trust Marks.
     - |uncheck-icon|


Entity Configuration Leaves and Intermediates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to the previously defined claims, the Entity Configuration of the Leaf and of the Intermediate Entities, MUST contain the parameters listed below:


.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Required**
   * - **authority_hints**
     - Array of URLs (String). It contains a list of URLs of the immediate superior entities, such as the Trust Anchor or
       an Intermediate, that issues an Entity Statement related to this subject.
     - |check-icon|
   * - **trust_marks**
     - A JSON Array containing the Trust Marks.
     - |uncheck-icon|

Metadata Types
^^^^^^^^^^^^^^^^

In this section are defined the main metadata types mapped to the roles of the ecosystem,
giving the references of the metadata protocol for each of these.


.. note::
    
    The entries that don't have any reference to a known draft or standard are intended to be defined in this technical reference.

.. list-table::
   :widths: 20 20 20 60
   :header-rows: 1

   * - OpenID Entity
     - EUDI Entity
     - Metadata Type
     - References
   * - Trust Anchor
     - Trust Anchor
     - ``federation_entity``
     - `OID-FED`_
   * - Intermediate
     - Intermediate
     - ``federation_entity``
     - `OID-FED`_
   * - Wallet Provider
     - Wallet Provider
     - ``federation_entity``, ``wallet_provider``
     - --
   * - Authorization Server
     - 
     - ``federation_entity``, ``oauth_authorization_server``
     - `OPENID4VCI`_
   * - Credential Issuer
     - PID Provider, (Q)EAA Provider
     - ``federation_entity``, ``openid_credential_issuer``, [``oauth_authorization_server``]
     - `OPENID4VCI`_
   * - Relying Party
     - Relying Party
     - ``federation_entity``, ``wallet_relying_party``
     - `OID-FED`_, `OpenID4VP`_


.. note::
    Wallet Provider metadata is defined in the section below.

    `Wallet Solution section <wallet-solution.html>`_. 


.. note::
    In instances where a PID/EAA Provider implements both the Credential Issuer and the Authorization Server, 
    it MUST incorporate both 
    ``oauth_authorization_server`` and ``openid_credential_issuer`` within its metadata types.
    Other implementations may divide the Credential Issuer from the Authorization Server, when this happens the Credential Issuer metadata MUST contain the `authorization_servers` parameters, including the Authorization Server unique identifier.
    Furthermore, should there be a necessity for User Authentication by the Credential Issuer,
    it could be necessary to include the relevant metadata type, either ``openid_relying_party`` 
    or ``wallet_relying_party``.


Metadata of federation_entity Leaves
-------------------------------------

The *federation_entity* metadata for Leaves MUST contain the following claims.


.. list-table:: 
  :widths: 20 60
  :header-rows: 1

  * - **Claim**
    - **Description**
  * - **organization_name**
    - See `OID-FED`_ Draft 36 Section 5.2.2
  * - **homepage_uri**
    - See `OID-FED`_ Draft 36 Section 5.2.2
  * - **policy_uri**
    - See `OID-FED`_ Draft 36 Section 5.2.2
  * - **logo_uri**
    - URL of the entity's logo; it MUST be in SVG format. See `OID-FED`_ Draft 36 Section 5.2.2
  * - **contacts**
    - Institutional certified email address (PEC) of the entity. See `OID-FED`_ Draft 36 Section 5.2.2
  * - **federation_resolve_endpoint**
    - See `OID-FED`_ Draft 36 Section 5.1.1

Entity Statements
-----------------

Trust Anchors and Intermediates publish Entity Statements related to their immediate Subordinates.
The Entity Statement MAY contain a metadata policy and the Trust Marks related to a Subordinate.

The metadata policy, when applied, makes one or more changes to the final metadata of the Leaf. The final metadata of a Leaf is derived from the Trust Chain that contains all the statements, starting from the Entity Configuration up to the Entity Statement issued by the Trust Anchor.

Trust Anchors and Intermediates MUST expose the Federation Fetch endpoint, where the Entity Statements are requested to validate the Leaf's Entity Configuration signature. 

.. note:: 
    The Federation Fetch endpoint MAY also publish X.509 certificates for each of the public keys of the Subordinate. Making the distribution of the issued X.509 certificates via a RESTful service.

Below there is a non-normative example of an Entity Statement issued by an Registration Body (such as the Trust Anchor or its Intermediate) in relation to one of its Subordinates.

.. code-block:: text

    {
        "alg": "ES256",
        "kid": "em3cmnZgHIYFsQ090N6B3Op7LAAqj8rghMhxGmJstqg",
        "typ": "entity-statement+jwt"
    }
    .
    {
        "exp": 1649623546,
        "iat": 1649450746,
        "iss": "https://intermediate.eidas.example.org",
        "sub": "https://rp.example.it",
        "jwks": {
            "keys": [
                {
                    "kty": "EC",
                    "kid": "2HnoFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs",
                    "crv": "P-256",
                    "x": "1kNR9Ar3MzMokYTY8BRvRIue85NIXrYX4XD3K4JW7vI",
                    "y": "slT14644zbYXYF-xmw7aPdlbMuw3T1URwI4nafMtKrY",
                    "x5c": [ <X.509 certificate> ]
                }
            ]
        },
        "metadata_policy": {
            "wallet_relying_party": {
                "scope": {
                    "subset_of": [
                         "eu.europa.ec.eudiw.pid.1",
                         "given_name",
                         "family_name",
                         "email"
                      ]
                },
                "vp_formats": {
                    "vc+sd-jwt": {
                        "sd-jwt_alg_values": [
                            "ES256",
                            "ES384"
                        ],
                        "kb-jwt_alg_values": [
                            "ES256",
                            "ES384"
                        ]
                    }
                }
            }
         }
    }


.. note::

  **Entity Statement Signature**

  The same considerations and requirements made for the Entity Configuration
  and in relation to the signature mechanisms MUST be applied for the Entity Statements.


Entity Statement
^^^^^^^^^^^^^^^^^^

The Entity Statement issued by Trust Anchors and Intermediates contains the following attributes:


.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Required**
   * - **iss**
     - See `OID-FED`_ Section 3.1 for further details.
     - |check-icon|
   * - **sub**
     - See `OID-FED`_ Section 3.1 for further details.
     - |check-icon|
   * - **iat**
     - See `OID-FED`_ Section 3.1 for further details.
     - |check-icon|
   * - **exp**
     - See `OID-FED`_ Section 3.1 for further details.
     - |check-icon|
   * - **jwks**
     - Federation JWKS of the *sub* entity. See `OID-FED`_ Section 3.1 for further details.
     - |check-icon|
   * - **metadata_policy**
     - JSON Object that describes the Metadata policy. Each key of the JSON Object represents an identifier of the metadata type and each value MUST be a JSON Object that represents the metadata policy according to that metadata type. Please refer to the `OID-FED`_ specifications, Section-5.1, for the implementation details.
     - |uncheck-icon|
   * - **trust_marks**
     - JSON Array containing the Trust Marks issued by itself for the subordinate subject.
     - |uncheck-icon|
   * - **constraints**
     - It MAY contain the **allowed_leaf_entity_types**, that restricts what types of metadata the subject is allowed to publish.
     - |check-icon|


Trust Evaluation Mechanism
--------------------------

The Trust Anchor publishes the list of its Subordinates (Federation Subordinate Listing endpoint) and the attestations of their metadata and public keys (Entity Statements).

Each participant, including Trust Anchor, Intermediate, Credential Issuer, Wallet Provider, and Relying Party, publishes its own metadata and public keys (Entity Configuration endpoint) in the well-known web resource **.well-known/openid-federation**.

Each of these can be verified using the Entity Statement issued by a superior, such as the Trust Anchor or an Intermediate.

Each Entity Statement is verifiable over time and MUST have an expiration date. The revocation of each statement is verifiable in real time and online (only for remote flows) through the federation endpoints.

.. note::
    The revocation of an Entity is made with the unavailability of the Entity Statement related to it. If the Trust Anchor or its Intermediate doesn't publish a valid Entity Statement, or if it publishes an expired/invalid Entity Statement, the subject of the Entity Statement MUST be intended as not valid or revoked.

The concatenation of the statements, through the combination of these signing mechanisms and the binding of claims and public keys, forms the Trust Chain.

The Trust Chains can also be verified offline, using one of the Trust Anchor's public keys.

.. note::
    Since the Wallet Instance is not a Federation Entity, the Trust Evaluation Mechanism related to it **requires the presentation of the Wallet Attestation during the credential issuance and presentation phases**.

    The Wallet Attestation conveys all the required information pertaining to the instance, such as its public key and any other technical or administrative information, without any User's personal data.


Relying Party Trust Evaluation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Relying Party is registered by a Trust Anchor or its Intermediate and obtains a Trust Mark to be included in its Entity Configuration. In its Entity Configuration the Relying Party publishes its specific metadata, including the supported signature and encryption algorithms and any other necessary information for the interoperability requirements.

Any requests for User attributes, such as PID or (Q)EAA, from the Relying Party to Wallet Instances are signed and SHOULD contain the verifiable Trust Chain regarding the Relying Party.

The Wallet Instance verifies that the Trust Chain related to the Relying Party is still active, proving that the Relying Party is still part of the Federation and not revoked.

The Trust Chain SHOULD be contained within the signed request in the form of a JWS header parameter.

In offline flows, Trust Chain verification enables the assessment of the reliability of Trust Marks and Attestations contained within.


Wallet Attestation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Wallet Provider issues the Wallet Attestation, certifying the operational status of its Wallet Instances and including one of their public keys. 

The Wallet Attestation contains the Trust Chain that attests the reliability for its issuer (Wallet Provider) at the time of issuance.

The Wallet Instance provides its Wallet Attestation within the signed request during the PID issuance phase, containing the Trust Chain related to the Wallet Provider. 


Trust Chain
^^^^^^^^^^^^^^^

The Trust Chain is a sequence of verified statements that validates a participant's compliance with the Federation. It has an expiration date time, beyond which it MUST be renewed to obtain the fresh and updated metadata. The expiration date of the Trust Chain is determined by the earliest expiration timestamp among all the expiration timestamp contained in the statements. No Entity can force the expiration date of the Trust Chain to be higher than the one configured by the Trust Anchor.

Below is an abstract representation of a Trust Chain.

.. code-block:: python

    [
        "EntityConfiguration-as-SignedJWT-selfissued-byLeaf",
        "EntityStatement-as-SignedJWT-issued-byTrustAnchor"
    ]

Below is a non-normative example of a Trust Chain in its original format (JSON Array containing JWS as strings) with an Intermediate involved.

.. code-block:: python

    [
      "eyJhbGciOiJFUzI1NiIsImtpZCI6Ik5GTTFXVVZpVWxZelVXcExhbWxmY0VwUFJWWTJWWFpJUmpCblFYWm1SSGhLWVVWWVVsZFRRbkEyTkEiLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk1OTA2MDIsImlhdCI6MTY0OTQxNzg2MiwiaXNzIjoiaHR0cHM6Ly9ycC5leGFtcGxlLm9yZyIsInN1YiI6Imh0dHBzOi8vcnAuZXhhbXBsZS5vcmciLCJqd2tzIjp7ImtleXMiOlt7Imt0eSI6IkVDIiwia2lkIjoiTkZNMVdVVmlVbFl6VVdwTGFtbGZjRXBQUlZZMlZYWklSakJuUVhabVJIaEtZVVZZVWxkVFFuQTJOQSIsImNydiI6IlAtMjU2IiwieCI6InVzbEMzd2QtcFgzd3o0YlJZbnd5M2x6cGJHWkZoTjk2aEwyQUhBM01RNlkiLCJ5IjoiVkxDQlhGV2xkTlNOSXo4a0gyOXZMUjROMThCa3dHT1gyNnpRb3J1UTFNNCJ9XX0sIm1ldGFkYXRhIjp7Im9wZW5pZF9yZWx5aW5nX3BhcnR5Ijp7ImFwcGxpY2F0aW9uX3R5cGUiOiJ3ZWIiLCJjbGllbnRfaWQiOiJodHRwczovL3JwLmV4YW1wbGUub3JnLyIsImNsaWVudF9yZWdpc3RyYXRpb25fdHlwZXMiOlsiYXV0b21hdGljIl0sImp3a3MiOnsia2V5cyI6W3sia3R5IjoiRUMiLCJraWQiOiJORk0xV1VWaVVsWXpVV3BMYW1sZmNFcFBSVlkyVlhaSVJqQm5RWFptUkhoS1lVVllVbGRUUW5BMk5BIiwiY3J2IjoiUC0yNTYiLCJ4IjoidXNsQzN3ZC1wWDN3ejRiUllud3kzbHpwYkdaRmhOOTZoTDJBSEEzTVE2WSIsInkiOiJWTENCWEZXbGROU05JejhrSDI5dkxSNE4xOEJrd0dPWDI2elFvcnVRMU00In1dfSwiY2xpZW50X25hbWUiOiJOYW1lIG9mIGFuIGV4YW1wbGUgb3JnYW5pemF0aW9uIiwiY29udGFjdHMiOlsib3BzQHJwLmV4YW1wbGUuaXQiXSwiZ3JhbnRfdHlwZXMiOlsicmVmcmVzaF90b2tlbiIsImF1dGhvcml6YXRpb25fY29kZSJdLCJyZWRpcmVjdF91cmlzIjpbImh0dHBzOi8vcnAuZXhhbXBsZS5vcmcvb2lkYy9ycC9jYWxsYmFjay8iXSwicmVzcG9uc2VfdHlwZXMiOlsiY29kZSJdLCJzY29wZSI6ImV1LmV1cm9wYS5lYy5ldWRpdy5waWQuMSBldS5ldXJvcGEuZWMuZXVkaXcucGlkLml0LjEgZW1haWwiLCJzdWJqZWN0X3R5cGUiOiJwYWlyd2lzZSJ9LCJmZWRlcmF0aW9uX2VudGl0eSI6eyJmZWRlcmF0aW9uX3Jlc29sdmVfZW5kcG9pbnQiOiJodHRwczovL3JwLmV4YW1wbGUub3JnL3Jlc29sdmUvIiwib3JnYW5pemF0aW9uX25hbWUiOiJFeGFtcGxlIFJQIiwiaG9tZXBhZ2VfdXJpIjoiaHR0cHM6Ly9ycC5leGFtcGxlLml0IiwicG9saWN5X3VyaSI6Imh0dHBzOi8vcnAuZXhhbXBsZS5pdC9wb2xpY3kiLCJsb2dvX3VyaSI6Imh0dHBzOi8vcnAuZXhhbXBsZS5pdC9zdGF0aWMvbG9nby5zdmciLCJjb250YWN0cyI6WyJ0ZWNoQGV4YW1wbGUuaXQiXX19LCJ0cnVzdF9tYXJrcyI6W3siaWQiOiJodHRwczovL3JlZ2lzdHJ5LmVpZGFzLnRydXN0LWFuY2hvci5leGFtcGxlLmV1L29wZW5pZF9yZWx5aW5nX3BhcnR5L3B1YmxpYy8iLCJ0cnVzdF9tYXJrIjoiZXlKaCBcdTIwMjYifV0sImF1dGhvcml0eV9oaW50cyI6WyJodHRwczovL2ludGVybWVkaWF0ZS5laWRhcy5leGFtcGxlLm9yZyJdfQ.Un315HdckvhYA-iRregZAmL7pnfjQH2APz82blQO5S0sl1JR0TEFp5E1T913g8GnuwgGtMQUqHPZwV6BvTLA8g",
      "eyJhbGciOiJFUzI1NiIsImtpZCI6IlNURkRXV2hKY0dWWFgzQjNSVmRaYWtsQ0xUTnVNa000WTNGNlFUTk9kRXRyZFhGWVlYWjJjWGN0UVEiLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk2MjM1NDYsImlhdCI6MTY0OTQ1MDc0NiwiaXNzIjoiaHR0cHM6Ly9pbnRlcm1lZGlhdGUuZWlkYXMuZXhhbXBsZS5vcmciLCJzdWIiOiJodHRwczovL3JwLmV4YW1wbGUub3JnIiwiandrcyI6eyJrZXlzIjpbeyJrdHkiOiJFQyIsImtpZCI6Ik5GTTFXVVZpVWxZelVXcExhbWxmY0VwUFJWWTJWWFpJUmpCblFYWm1SSGhLWVVWWVVsZFRRbkEyTkEiLCJjcnYiOiJQLTI1NiIsIngiOiJ1c2xDM3dkLXBYM3d6NGJSWW53eTNsenBiR1pGaE45NmhMMkFIQTNNUTZZIiwieSI6IlZMQ0JYRldsZE5TTkl6OGtIMjl2TFI0TjE4Qmt3R09YMjZ6UW9ydVExTTQifV19LCJtZXRhZGF0YV9wb2xpY3kiOnsib3BlbmlkX3JlbHlpbmdfcGFydHkiOnsic2NvcGUiOnsic3Vic2V0X29mIjpbImV1LmV1cm9wYS5lYy5ldWRpdy5waWQuMSwgIGV1LmV1cm9wYS5lYy5ldWRpdy5waWQuaXQuMSJdfSwicmVxdWVzdF9hdXRoZW50aWNhdGlvbl9tZXRob2RzX3N1cHBvcnRlZCI6eyJvbmVfb2YiOlsicmVxdWVzdF9vYmplY3QiXX0sInJlcXVlc3RfYXV0aGVudGljYXRpb25fc2lnbmluZ19hbGdfdmFsdWVzX3N1cHBvcnRlZCI6eyJzdWJzZXRfb2YiOlsiUlMyNTYiLCJSUzUxMiIsIkVTMjU2IiwiRVM1MTIiLCJQUzI1NiIsIlBTNTEyIl19fX0sInRydXN0X21hcmtzIjpbeyJpZCI6Imh0dHBzOi8vdHJ1c3QtYW5jaG9yLmV4YW1wbGUuZXUvb3BlbmlkX3JlbHlpbmdfcGFydHkvcHVibGljLyIsInRydXN0X21hcmsiOiJleUpoYiBcdTIwMjYifV19._qt5-T6DahP3TuWa_27klE8I9Z_sPK2FtQlKY6pGMPchbSI2aHXY3aAXDUrObPo4CHtqgg3J2XcrghDFUCFGEQ",
      "eyJhbGciOiJFUzI1NiIsImtpZCI6ImVXa3pUbWt0WW5kblZHMWxhMjU1ZDJkQ2RVZERSazQwUWt0WVlVMWFhRFZYT1RobFpHdFdXSGQ1WnciLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk2MjM1NDYsImlhdCI6MTY0OTQ1MDc0NiwiaXNzIjoiaHR0cHM6Ly90cnVzdC1hbmNob3IuZXhhbXBsZS5ldSIsInN1YiI6Imh0dHBzOi8vaW50ZXJtZWRpYXRlLmVpZGFzLmV4YW1wbGUub3JnIiwiandrcyI6eyJrZXlzIjpbeyJrdHkiOiJFQyIsImtpZCI6IlNURkRXV2hKY0dWWFgzQjNSVmRaYWtsQ0xUTnVNa000WTNGNlFUTk9kRXRyZFhGWVlYWjJjWGN0UVEiLCJjcnYiOiJQLTI1NiIsIngiOiJyQl9BOGdCUnh5NjhVTkxZRkZLR0ZMR2VmWU5XYmgtSzh1OS1GYlQyZkZJIiwieSI6IlNuWVk2Y3NjZnkxcjBISFhLTGJuVFZsamFndzhOZzNRUEs2WFVoc2UzdkUifV19LCJ0cnVzdF9tYXJrcyI6W3siaWQiOiJodHRwczovL3RydXN0LWFuY2hvci5leGFtcGxlLmV1L2ZlZGVyYXRpb25fZW50aXR5L3RoYXQtcHJvZmlsZSIsInRydXN0X21hcmsiOiJleUpoYiBcdTIwMjYifV19.r3uoi-U0tx0gDFlnDdITbcwZNUpy7M2tnh08jlD-Ej9vMzWMCXOCCuwIn0ZT0jS4M_sHneiG6tLxRqj-htI70g"
    ]


.. note::

    The entire Trust Chain is verifiable by only possessing the Trust Anchor's public keys.
There are events where keys are unavailable to verify the entire trust chain:

 - **Key Change by Credential Issuer**: If the credential issuer updates its keys, the previous keys MUST be valid for their originally designated validity period. This MUST be managed using the Federation Historical Keys Endpoint.

 - **Change in Credential Types**: If the credential issuer changes the credential issued, for example deciding not to issue one or more credential types, the related keys MUST be available for the originally designated validity period.

 - **Credential Issuers Merge**: If a credential issuer merges with another, the previousòly available federation configuration MUST be available throught both Federation Historical Keys Endpoint and Federation Historical Entity Endpoint. 

 - **Credential Issuer Becomes Inactive**: If a credential issuer becomes inactive for any reason, a Federation Historical Entity Endpoint MUST be available, managed by a higher authority. This situation may not only apply to the credential issuer (leaf) but could also occur at an intermediate or root entity level. In such cases the root or trust anchor may be the entity responsible for managing the Federation Historical Entity Endpoint.

In the latter scenarios, the root authority, or an entity authorized by the root authority, MUST retain the keys and trust chain end points for a period established by law.


Offline Trust Attestation Mechanisms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The offline flows do not allow for real-time evaluation of an Entity's status, such as its revocation. At the same time, using short-lived Trust Chains enables the attainment of trust attestations compatible with the required revocation administrative protocols (e.g., a revocation must be propagated in less than 24 hours, thus the Trust Chain must not be valid for more than that period).


Offline Wallet Trust Attestation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given that the Wallet Instance cannot publish its metadata online at the *.well-known/openid-federation* endpoint, 
it MUST obtain a Wallet Attestation issued by its Wallet Provider. The Wallet Attestation MUST contain all the relevant information regarding the security capabilities of the Wallet Instance and its protocol related configuration. It SHOULD contain the Trust Chain related to its issuer (Wallet Provider).


Offline Relying Party Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since the Federation Entity Discovery is only applicable in online scenarios, it is possible to include the Trust Chain in the presentation requests that the Relying Party may issue for a Wallet Instance.

The Relying Party MUST sign the presentation request, the request SHOULD include the `trust_chain` claim in its JWS header parameters, containing the Federation Trust Chain related to itself.

The Wallet Instance that verifies the request issued by the Relying Party MUST use the Trust Anchor's public keys to validate the entire Trust Chain related to the Relying Party before attesting its reliability.

Furthermore, the Wallet Instance applies the metadata policy, if any.

Trust Chain Fast Renewal
------------------------

The Trust Chain fast renewal method offers a streamlined way to maintain the validity of a trust chain without undergoing the full discovery
process again. It's particularly useful for quickly updating trust relationships when minor changes occur or when the
Trust Chain is close to expiration but the overall structure of the federation hasn't changed significantly.

The Trust Chain fast renewal process is initiated by fetching the leaf's Entity Configuration anew. However, unlike the federation discovery process that may involve fetching Entity Configurations starting from the authority hints, the fast renewal focuses on directly obtaining the Subordinate Statements. These statements are requested using the `source_endpoint` provided within them, which points to the location where the statements can be fetched.


Non-repudiability of the Long Lived Attestations
--------------------------------------------------

The Trust Anchor and its Intermediate MUST expose the Federation Historical Keys endpoint, where are published all the public part of the Federation Entity Keys that are no longer used, whether expired or revoked.

The details of this endpoint are defined in the `OID-FED`_ Section 7.6.

Each JWS containing a Trust Chain in the form of a JWS header parameter can be verified over time, since the entire Trust Chain is verifiable using the Trust Anchor's public key.

Even if the Trust Anchor has changed its cryptographic keys for digital signature, the Federation Historical Keys endpoint always makes the keys no longer used available for historical signature verifications.


Privacy Remarks
---------------

- Wallet Instances MUST NOT publish their metadata through an online service.
- The trust infrastructure MUST be public, with all endpoints publicly accessible without any client credentials that may disclose who is requesting access.
- When a Wallet Instance requests the Entity Statements to build the Trust Chain for a specific Relying Party or validates a Trust Mark online, issued for a specific Relying Party, the Trust Anchor or its Intermediate do not know that a particular Wallet Instance is inquiring about a specific Relying Party; instead, they only serve the statements related to that Relying Party as a public resource.
- The Wallet Instance metadata MUST not contain information that may disclose technical information about the hardware used.
- Leaf entity, Intermediate, and Trust Anchor metadata may include the necessary amount of data as part of administrative, technical, and security contact information. It is generally not recommended to use personal contact details in such cases. From a legal perspective, the publication of such information is needed for operational support concerning technical and security matters and the GDPR regulation.


Considerations about Decentralization
-------------------------------------

- There may be more than a single Trust Anchor.
- In some cases, a trust verifier may trust an Intermediate, especially when the Intermediate acts as a Trust Anchor within a specific perimeter, such as cases where the Leafs are both in the same perimeter like a Member State jurisdiction (eg: an Italian Relying Party with an Italian Wallet Instance may consider the Italian Intermediate as a Trust Anchor for the scopes of their interactions).
- Trust attestations (Trust Chain) should be included in the JWS issued by Credential Issuers, and the Presentation Requests of RPs should contain the Trust Chain related to them (issuers of the presentation requests).
- Since the credential presentation must be signed, storing the signed presentation requests and responses, which include the Trust Chain, the Wallet Instance may have the snapshot of the federation configuration (Trust Anchor Entity Configuration in the Trust Chain) and the verifiable reliability of the Relying Party it has interacted with. 
- Each signed attestation is long-lived since it can be cryptographically validated even when the federation configuration changes or the keys of its issuers are renewed.
- Each participant should be able to update its Entity Configuration without notifying the changes to any third party. The metadata policy contained within a Trust Chain must be applied to overload any information related to protocol specific metadata.
