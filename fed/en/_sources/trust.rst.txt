.. include:: ../common/common_definitions.rst

.. _trust.rst:

The Infrastructure of Trust
+++++++++++++++++++++++++++

The EUDI Wallet Architecture Reference Framework (`EIDAS-ARF`_) describes the Trust Model as a *"collection of rules that ensure the legitimacy of the components and the entities involved in the EUDI Wallet ecosystem"*.

This section outlines the implementation of the Trust Model in an infrastructure that complies with OpenID Federation 1.0 `OIDC-FED`_. This infrastructure involves a RESTful API for distributing metadata, metadata policies, trust marks, public keys, X.509 certificates, and the revocation status of the participants, also called Federation Entities.

The Infrastructure of trust facilitates the application of a trust assessment mechanism among the parties defined in the `EIDAS-ARF`_.

..  figure:: ../../images/trust-roles.svg
    :alt: federation portrait
    :width: 100%
   
    The roles within the Federation, where the Trust Anchor oversees its subordinates,
    which include one or more Intermediates and Leaves. In this
    representation, both the Trust Anchor and the Intermediates may assume the role of Accreditation Body.


Federation Roles
------------------

All the participants are Federation Entities that MUST be accredited by an Accreditation Body,
except for Wallet Instances which are End-User's personal devices certified by their Wallet Provider.

.. note::
    The Wallet Instance, as a personal device, is certified as reliable through a verifiable attestation issued and signed by a trusted third party.

    This is called *Wallet Instance Attestation* and is documented in `the dedicated section  <Wallet Instance Attestation>`_.


Below the table with the summary of the Federation Entity roles, mapped on the corresponding EUDI Wallet roles, as defined in the `EIDAS-ARF`_.

+-----------------------------------------+----------------+-----------------------------------+
|  EUDI Role                              | Federation Role| Notes                             |
+=========================================+================+===================================+
|  Public Key Infrastructure (PKI)        | Trust Anchor   | The Federation has PKI            |
|                                         |                | capabilities. The                 |
|                                         | Intermediates  | Entity that configures            |
|                                         |                | the entire infrastructure         |
|                                         |                | is the Trust Anchor.              |
|                                         |                |                                   |
+-----------------------------------------+----------------+-----------------------------------+
|  Qualified Trust Service Provider (QTSP)| Leaf           |                                   |
+-----------------------------------------+----------------+-----------------------------------+
|  Person Identification Data Provider    | Leaf           |                                   |
+-----------------------------------------+----------------+-----------------------------------+
|  Qualified Electronic Attestations      | Leaf           |                                   |
|  of Attributes Provider                 |                |                                   |
+-----------------------------------------+----------------+-----------------------------------+
|  Electronic Attestations of             | Leaf           |                                   |
|  Attributes Provider                    |                |                                   |
+-----------------------------------------+----------------+-----------------------------------+
|  Relying Party                          | Leaf           |                                   |
+-----------------------------------------+----------------+-----------------------------------+
|  Trust Service Provider (TSP)           | Leaf           |                                   |
+-----------------------------------------+----------------+-----------------------------------+
|  Trusted List                           | Trust Anchor   | The listing endpoint, the         |
|                                         |                | trust mark status endpoint        |
|                                         | Intermediates  | and the fetch endpoint must       |
|                                         |                | be exposed by both Trust Anchors  |
|                                         |                | and Intermediates, making         |
|                                         |                | the Trusted List distributed      |
|                                         |                | over multiple Federation Entities,|
|                                         |                | where each of these is responsible|
|                                         |                | for their accredited subordinates.|
+-----------------------------------------+----------------+-----------------------------------+
|  Wallet Provider                        | Leaf           |                                   |
+-----------------------------------------+----------------+-----------------------------------+


General Properties
------------------

OpenID Federation facilitates the building of an infrastructure that is:

- **Secure and Tamper-proof**, Entities' attestations of metadata and keys are cryptographically signed in the Trust Chain, comprised of attestations issued by multiple parties. These attestations, called statements, cannot be forged or tampered by an adversary;
- **Privacy-preserving**, the infrastructure is public and exposes public data such as public keys and metadata of the participants. It does not require authentication of the consumers and therefore does not track who is assessing trust against whom;
- **Guarantor of the non-repudiation of long-lived attestations**, historical keys endpoints and historical Trust Chains are saved for years according to data retention policies. This enables the certification of the validity of historical compliance, even in cases of revocation, expiration, or rotation of the keys used for signature verification;
- **Dynamic and flexible**, any participants have the freedom to modify parts of their metadata autonomously, as these are published within their domains and verified through the Trust Chain. Simultaneously, the Trust Anchor or its Intermediate may publish a metadata policy to dynamically modify the metadata of all participants — such as disabling a vulnerable signature algorithm — and obtain certainty of propagation within a configured period of time within the federation;
- **Developer friendly**, JWT and JSON formats have been adopted on the web for years. They are cost-effective in terms of storage and processing and have a wide range of solutions available, such as libraries and software development kits, which enable rapid implementation of the solution;
- **Scalable**, the Trust Model can accommodate more than a single organization by using Intermediates and multiple Trust Anchors where needed.

Trust Model Requirements
------------------------

In the table below is provided the map of the components that the ARF defines within the Trust Model, in the same table is provided their coverage in `OIDC-FED`_.

+----------------------------------------------------+--------------+----------------+
|  Component                                         |  Satisfied   | how            |
+====================================================+==============+================+
|  Issuers identification                            | |check-icon| | Trust Chain    |
+----------------------------------------------------+--------------+----------------+
|  Issuers registration                              | |check-icon| | Trust Anchor   |
|                                                    |              |                |
|                                                    |              | Intermediates  |
|                                                    |              | accreditation  |
|                                                    |              | system         |
|                                                    |              |                |
+----------------------------------------------------+--------------+----------------+
|  Recognised data models and schemas                | |check-icon| | Entity         |
|                                                    |              | Configuration  |
|                                                    |              |                |
|                                                    |              | Entity         |
|                                                    |              | Statements     |
+----------------------------------------------------+--------------+----------------+
|  Relying Parties’ registration and authentication  | |check-icon| |                |
|                                                    |              | Trust Chains   |
|                                                    |              |                |
|                                                    |              | Federation     |
|                                                    |              | Entity         |
|                                                    |              | Discovery      |
+----------------------------------------------------+--------------+----------------+
|  Trust mechanisms in a cross-domain scenario       | |check-icon| |                |
|                                                    |              | Trust Chains   |
|                                                    |              |                |
|                                                    |              | Federation     |
|                                                    |              | Entity         |
|                                                    |              | Discovery      |
+----------------------------------------------------+--------------+----------------+


Federation API endpoints
------------------------

OpenID Federation 1.0 uses RESTful Web Services secured over
HTTPs. OpenID Federation 1.0 defines which are the web endpoints that the participants MUST make
publicly available. The table below summarises the endpoints and their scopes.

All the endpoints listed below are defined in the `OIDC-FED`_ specs.

+---------------------------+----------------------------------------------+--------------------------------+-----------------+
| endpoint name             | http request                                 |          scope                 |  required for   |
+===========================+==============================================+================================+=================+
|                           |                                              |                                |  Trust Anchor   |
|                           |                                              |                                |                 |
| federation metadata       | **GET** .well-known/openid-federation        |Metadata that an Entity         |  Intermediate   |
|                           |                                              |publishes about itself,         |                 |
|                           |                                              |verifiable with a trusted third |  Wallet Provider|
|                           |                                              |party (Superior Entity). It’s   |                 |
|                           |                                              |called Entity Configuration.    |  Relying Party  |
|                           |                                              |                                |                 |
|                           |                                              |                                |  Credential     |
|                           |                                              |                                |  Issuer         |
+---------------------------+----------------------------------------------+--------------------------------+-----------------+
| subordinate list endpoint | **GET** /list                                |Lists the Subordinates.         |  Trust Anchor   |
|                           |                                              |                                |                 |
|                           |                                              |                                |  Intermediate   |
+---------------------------+----------------------------------------------+--------------------------------+-----------------+
| fetch endpoint            | **GET** /fetch?sub=https://rp.example.org    |                                |  Trust Anchor   |
|                           |                                              |Returns a signed document (JWS) |                 |
|                           |                                              |about a specific subject, its   |  Intermediate   |
|                           |                                              |Subordinate. It’s called Entity |                 |
|                           |                                              |Statement.                      |                 |
+---------------------------+----------------------------------------------+--------------------------------+-----------------+
| trust mark status         | **POST** /status?sub=...&trust_mark_id=...   |                                |  Trust Anchor   |
|                           |                                              |Returns the status of the       |                 |
|                           |                                              |issuance (validity) of a Trust  |  Intermediate   |
|                           |                                              |Mark related to a specific      |                 |
|                           |                                              |subject.                        |                 |
+---------------------------+----------------------------------------------+--------------------------------+-----------------+
| historical keys           | **GET**                                      |                                |  Trust Anchor   |
|                           |                                              |Lists the expired and revoked   |                 |
|                           |                                              |keys, with the motivation of the|  Intermediate   |
|                           | .well-known/openid-federation-historical-jwks|revocation.                     |                 |
|                           |                                              |                                |                 |
+---------------------------+----------------------------------------------+--------------------------------+-----------------+

All the responses of the federation endpoints are in the form of JWS, with the exception of the **Subordinate Listing endpoint** and the **Trust Mark Status endpoint** that are served as plain JSON by default.


Configuration of the Federation
-------------------------------

The configuration of the federation is published by the Trust Anchor within its Entity Configuration, it is available at the well-known web path corresponding to **.well-known/openid-federation**.

All the participants in the federation MUST obtain the federation configuration before entering the operational phase, and they
MUST keep it up-to-date. The federation configuration is the Trust Anchor's Entity Configuration, it contains the 
public keys for signature operations and the maximum number of Intermediates allowed between a Leaf and the Trust Anchor (**max_path_length**).

Below is a non-normative example of a Trust Anchor Entity Configuration, where each parameter is documented in the `OpenID Federation <OIDC-FED>`_ specification:

.. code-block:: text

    {
        "alg": "RS256",
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
                    "kty": "RSA",
                    "n": "3i5vV-_ …",
                    "e": "AQAB",
                    "kid": "FifYx03bnosD8m6gYQIfNHNP9cM_Sam9Tc5nLloIIrc",
                    "x5c": [ <X.509 Root CA certificate> ]
                },
                {
                    "kty": "EC",
                    "kid": "X2ZOMHNGSDc4ZlBrcXhMT3MzRmRZOG9Jd3o2QjZDam51cUhhUFRuOWd0WQ",
                    "crv": "P-256",
                    "x": "1kNR9Ar3MzMokYTY8BRvRIue85NIXrYX4XD3K4JW7vI",
                    "y": "slT14644zbYXYF-xmw7aPdlbMuw3T1URwI4nafMtKrY",
                    "x5c": [ <X.509 Root CA certificate> ]
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

+------------------+-----------------------------+--------------+
| Entity           | metadata type               | references   |
+==================+=============================+==============+
| Trust Anchor     | ``federation_entity``       | `OIDC-FED`_  |
+------------------+-----------------------------+--------------+
| Intermediate     | ``federation_entity``       | `OIDC-FED`_  |
+------------------+-----------------------------+--------------+
|                  |                             |              |
| Wallet Provider  | ``federation_entity``       | --           |
|                  |                             |              |
|                  | ``wallet_provider``         |              |
|                  |                             |              |
|                  |                             |              |
+------------------+-----------------------------+--------------+
|                  |                             |              |
| Credential Issuer| ``federation_entity``       |              |
|                  |                             |              |
|                  | ``openid_credential_issuer``| `OPENID4VCI`_|
+------------------+-----------------------------+--------------+
|                  |                             |              |
| Relying Party    | ``federation_entity``       |              |
|                  |                             |              |
|                  | ``wallet_relying_party``    | `OIDC-FED`_  |
|                  |                             |              |
|                  |                             | `OpenID4VP`_ |
+------------------+-----------------------------+--------------+

.. note::
    Wallet Provider metadata is defined in the section below.

    `Wallet Solution section <wallet-solution.html>`_. 


Entity Statements
-----------------

Trust Anchors and Intermediates publish Entity Statements related to their immediate Subordinates.
The Entity Statement MAY contain a metadata policy and the Trust Marks related to a Subordinate.

The metadata policy, when applied, makes one or more changes to the final metadata of the Leaf. The final metadata of a Leaf is derived from the Trust Chain that contains all the statements, starting from the Entity Configuration up to the Entity Statement issued by the Trust Anchor.

Trust Anchors and Intermediates MUST expose the Federation Fetch endpoint, where the Entity Statements are requested to validate the Leaf's Entity Configuration signature. 

.. note:: 
    The Federation Fetch endpoint MAY also publish X.509 certificates for each of the public keys of the Subordinate. Making the distribution of the issued X.509 certificates via a RESTful service.

Below there is a non-normative example of an Entity Statement issued by an Accreditation Body (such as the Trust Anchor or its Intermediate) in relation to one of its Subordinates.

.. code-block:: text

    {
        "alg": "RS256",
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
     - See `OIDC-FED`_ Section 3.1 for further details.
     - |check-icon|
   * - **sub**
     - See `OIDC-FED`_ Section 3.1 for further details.
     - |check-icon|
   * - **iat**
     - See `OIDC-FED`_ Section 3.1 for further details.
     - |check-icon|
   * - **exp**
     - See `OIDC-FED`_ Section 3.1 for further details.
     - |check-icon|
   * - **jwks**
     - Federation JWKS of the *sub* entity. See `OIDC-FED`_ Section 3.1 for further details.
     - |check-icon|
   * - **metadata_policy**
     - JSON Object that describes the Metadata policy. Each key of the JSON Object represent an identifier of the metadata type and each value MUST be a JSON Object that represents the metadata policy according to that metadata type. Please refer to the `OIDC-FED`_ specifications, Section-5.1, for the implementation details.
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
    Since the Wallet Instance is not a Federation Entity, the Trust Evaluation Mechanism related to it **requires the presentation of the Wallet Instance Attestation during the credential issuance and presentation phases**.

    The Wallet Instance Attestation conveys all the required information pertaining to the instance, such as its public key and any other technical or administrative information, without any User's personal data.


Relying Party Attestation
^^^^^^^^^^^^^^^^^^^^^^^^^^

The Relying Party is accredited by a Trust Anchor or its Intermediate and obtains a Trust Mark to be included in its Entity Configuration. In its Entity Configuration the Relying Party publishes its specific metadata, including the supported signature and encryption algorithms and any other necessary information for the interoperability requirements.

Any requests for User attributes, such as PID or (Q)EAA, from the Relying Party to Wallet Instances are signed and SHOULD contain the verifiable Trust Chain regarding the Relying Party.

The Wallet Instance verifies that the Trust Chain related to the Relying Party is still active, proving that the Relying Party is still part of the Federation and not revoked.

The Trust Chain SHOULD be contained within the signed request in the form of a JWS header parameter.

In offline flows, Trust Chain verification enables the assessment of the reliability of Trust Marks and Attestations contained within.


Wallet Instance Attestation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Wallet Provider issues the Wallet Instance Attestation, certifying the operational status of its Wallet Instances and including one of their public keys. 

The Wallet Instance Attestation contains the Trust Chain that attests the reliability for its issuer (Wallet Provider) at the time of issuance.

The Wallet Instance provides its Wallet Instance Attestation within the signed request during the PID issuance phase, containing the Trust Chain related to the Wallet Provider. 


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

    The entire Trust Chain is verifiable by only possessing the Trust Anchor’s public keys.


Offline Trust Attestation Mechanisms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The offline flows do not allow for real-time evaluation of an Entity's status, such as its revocation. At the same time, using short-lived Trust Chains enables the attainment of trust attestations compatible with the required revocation administrative protocols (e.g., a revocation must be propagated in less than 24 hours, thus the Trust Chain must not be valid for more than that period).


Offline EUDI Wallet Trust Attestation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given that the Wallet Instance cannot publish its metadata online at the *.well-known/openid-federation* endpoint, 
it MUST obtain a Wallet Instance Attestation issued by its Wallet Provider. The Wallet Instance Attestation MUST contain all the relevant information regarding the security capabilities of the Wallet Instance and its protocol related configuration. It SHOULD contain the Trust Chain related to its issuer (Wallet Provider).


Offline Relying Party Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since the Federation Entity Discovery is only applicable in online scenarios, it is possible to include the Trust Chain in the presentation requests that the Relying Party may issue for a Wallet Instance.

The Relying Party MUST sign the presentation request, the request SHOULD include the `trust_chain` claim in its JWS header parameters, containing the Federation Trust Chain related to itself.

The Wallet Instance that verifies the request issued by the Relying Party MUST use the Trust Anchor's public keys to validate the entire Trust Chain related to the Relying Party before attesting its reliability.

Furthermore, the Wallet Instance applies the metadata policy, if any.


Non-repudiability of the Long Lived Attestations
--------------------------------------------------

The Trust Anchor and its Intermediate MUST expose the Federation Historical Keys endpoint, where are published all the public part of the Federation Entity Keys that are no longer used, whether expired or revoked.

The details of this endpoint are defined in the `OIDC-FED`_ Section 7.6.

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
