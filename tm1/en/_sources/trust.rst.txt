.. include:: ../common/common_definitions.rst

.. _trust.rst:

The Infrastructure of Trust
+++++++++++++++++++++++++++

The EUDI Wallet Architecture Reference Framework (`EIDAS-ARF`_) defines the Trust Model as a *"collection of rules that ensure the legitimacy of the components and the entities involved in the EUDI Wallet ecosystem."*.

This section defines how the Trust Model is implemented in an infrastructure of Trust in fully compliace with OpenID Connect Federation 1.0 `OIDC-FED`_, where its Federation API is used for the distribution of metadata, metadata policies, trust marks, public keys,  X.509 certificates, and the revocation status of the participants (Federation Entities).

The infrastructure of Trust enables the trust assessment mechanism to be applied between the parties defined in the `EIDAS-ARF`_.

..  figure:: ../../images/trust-roles.svg
    :alt: federation portrain
    :width: 100%
   
    The roles of the Federation infrastructure, where a Trust Anchor has one or more Intermediates and Leafs and the Intermediates have their Leafs. In this representation both Trust Anchor and Intermediates play the role of Accreditation Body.


Federation Roles
------------------

All the participants are Federation Entities that must be accredited by an Accreditation Body, except the Wallet Instances that are personal devices and are certified by their Wallet Provider.

.. note::
    The Wallet Instance, as a personal device, is certified as trusted through a verifiable attestation issued and signed by its Wallet Provider.

    This is called *Wallet Instance Attestation* and is documented in `the dedicated section  <Wallet Instance Attestation>`_.


Therein a table with the summary of the Federation Entity roles mapped on the corresponding EUDI roles, as defined in the `EIDAS-ARF`_.

+-----------------------------------------+----------------+-----------------------------------+
|  EUDI Role                              | Federation Role| Notes                             |
+=========================================+================+===================================+
|  Public Key Infrastructure (PKI)        | Trust Anchor   | The Federation has PKI            |
|                                         | Intermediates  | capabilities and the              |
|                                         |                | Entity that configures            |
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
|                                         | Intermediates  | trust mark status endpoint        |
|                                         |                | and the fetch endpoint must       |
|                                         |                | be exposed by both Trust Anchors  |
|                                         |                | and their Intermediates, making   |
|                                         |                | the Trusted List distributed      |
|                                         |                | over multiple Federation Entities,|
|                                         |                | where each of these is responsible|
|                                         |                | of their accredited subordinates. |
|                                         |                |                                   |
+-----------------------------------------+----------------+-----------------------------------+
|  EUDI Wallet Provider                   | Leaf           |                                   |
+-----------------------------------------+----------------+-----------------------------------+


General Properties
------------------

OpenID Federation facilitates the building of an infrastructure that is:

- **Secure and Tamper-proof**, entities' attestations of metadata and keys are cryptographically signed in the chain of trust, comprised of attestations issued by multiple parties that cannot be forged or tampered with by an adversary;
- **Privacy-preserving**, the infrastructure is public and exposes public data such as public keys and metadata of the participants. It does not require authentication of the requesters and therefore does not track who is assessing trust against whom;
- **Guarantor of the non-repudiation of long-lived attestations**, historical keys endpoints and historical Trust Chains are saved for years according to data retention policies. This enables the certification of the validity of historical compliance, even in cases of revocation, expiration, or rotation of the keys used for signature verification;
- **Dynamic and flexible**, allowing any participant to modify parts of their metadata autonomously, as these are published within their domains and verified through the Trust Chain. Simultaneously, the Trust Anchor or its Intermediate may publish a metadata policy to dynamically modify the metadata of all participants—such as disabling a vulnerable signature algorithm—and obtain certainty of propagation within a configured period of time to all participants;
- **Efficient**, as JWT and JSON formats have been adopted on the web for years. They are cost-effective in terms of storage and processing and have a wide range of solutions available, such as libraries and software development kits, which enable rapid implementation of the solution;
- **Scalable**, the Trust Model can accommodate more than a single organization by using Intermediates.

Trust Model Requirements
------------------------

In the table below there’s the map of the components that the ARF defines within the Trust Model and their coverage in `OIDC-FED`_.

+----------------------------------------------------+--------------+----------------+
|  Component                                         |  Satisfied   | how            |
+====================================================+==============+================+
|  Issuers identification                            | |check-icon| | Trust Chain    |
+----------------------------------------------------+--------------+----------------+
|  Issuers registration                              | |check-icon| | Trust Anchor   |
|                                                    |              |                |
|                                                    |              | Intermediate   |
|                                                    |              | OnBoarding     |
|                                                    |              | systems        |
|                                                    |              |                |
+----------------------------------------------------+--------------+----------------+
|  Recognised data models and schemas                | |check-icon| | Entity         |
|                                                    |              | Configuration  |
|                                                    |              |                |
|                                                    |              |                |
|                                                    |              |                |
|                                                    |              | Entity         |
|                                                    |              | Statements     |
+----------------------------------------------------+--------------+----------------+
|  Relying Parties’ registration and authentication  | |check-icon| | static         |
|                                                    |              | Trust Chains   |
|                                                    |              |                |
|                                                    |              |                |
|                                                    |              |                |
|                                                    |              | Federation     |
|                                                    |              | Entity         |
|                                                    |              | Discovery      |
+----------------------------------------------------+--------------+----------------+
|  Trust mechanisms in a cross-domain scenario       | |check-icon| | static         |
|                                                    |              | Trust Chains   |
|                                                    |              |                |
|                                                    |              |                |
|                                                    |              |                |
|                                                    |              | Federation     |
|                                                    |              | Entity         |
|                                                    |              | Discovery      |
+----------------------------------------------------+--------------+----------------+


Federation API endpoints
------------------------

OpenID Connect Federation is similar to a PKI that uses RESTful Web Services secured over HTTPs. OpenID Connect Federation defines which are the web endpoints that the participants made publicly available. In the table below the summary of these and their scopes.

All the endpoints listed below are defined in the `OIDC-FED`_ specs.

+---------------------------+----------------------------------------------+--------------------------------+-----------------+
| endpoint name             | http request                                 |          scope                 |  required by    |
+===========================+==============================================+================================+=================+
|                           |                                              |                                |  Trust Anchor   |
|                           |                                              |                                |                 |
| federation metadata       | **GET** .well-known/openid-federation        |Metadata that an Entity         |  Intermediate   |
|                           |                                              |publishes about itself,         |                 |
|                           |                                              |verifiable with a trusted third |  Wallet Provider|
|                           |                                              |party (Superior Entity). It’s   |                 |
|                           |                                              |called Entity Configuration.    |  Relying Party  |
|                           |                                              |                                |                 |
|                           |                                              |                                |                 |
+---------------------------+----------------------------------------------+--------------------------------+-----------------+
| subordinate list endpoint | **GET** /list                                |Lists the Subordinates.         |  Trust Anchor   |
|                           |                                              |                                |                 |
|                           |                                              |                                |  Intermediate   |
+---------------------------+----------------------------------------------+--------------------------------+-----------------+
| fetch endpoint            | **GET** /fetch?sub=https://rp.example.org    |                                |  Trust Anchor   |
|                           |                                              |Returns a document (JWS)        |                 |
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
|                           |                                              |Lists its expired and revoked   |                 |
|                           |                                              |keys, with the motivation of the|  Intermediate   |
|                           | .well-known/openid-federation-historical-jwks|revocation.                     |                 |
|                           |                                              |                                |                 |
+---------------------------+----------------------------------------------+--------------------------------+-----------------+

All the responses of the Federation endpoints are JWS, with the exception of the **Subordinate Listing endpoint** and the **Trust Mark Status endpoint** that are served as plain JSON by default, however these may be signed if required.


Configuration of the Federation
-------------------------------

The configuration of the Federation is published by the Trust Anchor within its Entity Configuration, available at a well-known web path corresponding to **.well-known/openid-federation**.

All entities MUST obtain the Federation configuration before entering the operational phase, and they
MUST keep it up-to-date. The Federation configuration contains the Trust Anchor
public keys for signature operations and the maximum number of Intermediates allowed between a Leaf and the Trust Anchor (**max_path length**).

Below is a non-normative example of a Trust Anchor Entity Configuration, where each parameter is documented in the `OpenID Connect Federation <OIDC-FED>`_ specifications, Section 3.1 for the Federation statements and Section 4 for the Metadata identifiers:

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
        "iss": "https://registry.eidas.trust-anchor.example.eu/",
        "sub": "https://registry.eidas.trust-anchor.example.eu/",
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
                "homepage_uri": "https://registry.eidas.trust-anchor.example.eu/",
                "logo_uri":"https://registry.eidas.trust-anchor.example.eu/static/svg/logo.svg",
                "federation_fetch_endpoint": "https://registry.eidas.trust-anchor.example.eu/fetch/",
                "federation_resolve_endpoint": "https://registry.eidas.trust-anchor.example.eu/resolve/",
                "federation_list_endpoint": "https://registry.eidas.trust-anchor.example.eu/list/",
                "federation_trust_mark_status_endpoint": "https://registry.eidas.trust-anchor.example.eu/trust_mark_status/"
            }
        },
        "trust_marks_issuers": {
            "https://registry.eidas.trust-anchor.example.eu/openid_relying_party/public/": [
                "https://registry.spid.eidas.trust-anchor.example.eu/",
                "https://public.intermediary.spid.org/"
            ],
    "https://registry.eidas.trust-anchor.example.eu/openid_relying_party/private/": [
                "https://registry.spid.eidas.trust-anchor.example.eu/",
                "https://private.other.intermediary.org/"
            ]
        },
        "constraints": {
            "max_path_length": 1
        }
    }


Entity Configuration
--------------------

The Entity Configuration is the verifiable document that each Federation Entity must publish on its own behalf.
The Entity Configuration must be cryptographycally signed, and it must be verified with one of the public keys contained within it and one of the public keys within the Entity Statement issued by the Trust Anchor or its Intermediate.

The Entity Configuration may also contain one or more Trust Marks.

.. note::
  **Entity Configuration Signature**

  All the signature-check operations regarding the Entity Configurations, Entity Statements and Trust Marks, are carried out with the Federation public keys. For the supported algorithms refer to Section `Cryptografic Algorithm`.

Entity Configurations Common Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Entity Configurations of all the participants have in common the parameters listed below.


.. list-table::
   :widths: 20 60
   :header-rows: 1

   * - **Claim**
     - **Description**
   * - **iss**
     - String. Identifier of the issuing Entity.
   * - **sub**
     - String. Identifier of the Entity to which it is referred.
   * - **iat**
     - UNIX Timestamp with the time of generation of the JWT, coded as NumericDate as indicated at :rfc:`7519`
   * - **exp**
     - UNIX Timestamp with the expiry time of the JWT, coded as NumericDate as indicated at :rfc:`7519`.
   * - **jwks**
     - A JSON Web Key Set (JWKS) :rfc:`7517` that represents the public part of the signing keys of the Entity at issue. Each JWK in the JWK set MUST have a key ID (claim kid) and MAY have a `x5c` parameter, as defined in :rfc:`7517`.
   * - **metadata**
     - JSON Object. Each key of the JSON Object represents a metadata type identifier
       containing JSON Object representing the Metadata, according to the Metadata 
       schema of that type. An Entity Configuration MAY contain more Metadata statements, but only   one for each type of
       Metadata (<**entity_type**>). the metadata types are defined in the section `Metadata Types <Metadata Types>`_.

.. note::
  Inside the Entity Configuration the claims **iss** e **sub** contain the same value (URL).

Entity Configuration Trust Anchor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Trust Anchor Entity Configuration, in addition of the common parameters listed above, also contains the followings parameters:

.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Required**
   * - **constraints**
     - JSON Object that describes the Trust Chain bounds and MUST contain the attribute **max_path_length**.
       It represents the maximum number of Intermediate between a Leaf and the Trust Anchor.
     - |check-icon|
   * - **trust_marks_issuers**
     - JSON Array that indicates which Federation authorities are considered trustworthy
       for issuing specific Trust Marks, assigned with their unique identifiers.
     - |uncheck-icon|


Entity Configuration Leaves and Intermediates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to the previously defined claims, the Entity Configuration of the Leaf and the Intermediate Entities, contain also the parameters listed below:


.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Required**
   * - **authority_hints**
     - Array of URLs (String). It contains a list of URLs of the superior Entities, such as the Trust Anchor or an Intermediate, that MAY issue an Entity Statement related to this subject.
     - |check-icon|
   * - **trust_marks**
     - A JSON Array containing the Trust Marks.
     - |uncheck-icon|

Metadata Types
^^^^^^^^^^^^^^^^

In this section are defined the main metadata types mapped to the roles of the ecosystem,
giving the references of the metadata protocol for each of these.


.. note::
    
    The entities that doesn't have any references to a known draft or standard are intended to be defined in this technical reference.

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

Trust Anchors and Intermediates publish an Entity Statement related to a Subordinate.
The Entity Statement MAY contain a metadata policy and the Trust Marks related to a Subordinate.

The metadata policy, when applied, makes one or more changes to the final metadata of the Leaf. The final metadata of a Leaf is derived from the Trust Chain that contains all the statements, starting from the Entity Configuration up to the Trust Anchor.

Trust Anchors and Intermediates must expose the Federation Fetch endpoint, where the Entity Statements are requested to validate the Leaf's Entity Configurations signature. 

.. note:: 
    The Federation Fetch endpoint may also issue X.509 certificates for each of the public keys of the Subordinate. Making the issuance of the X.509 certificates completely automatic. 

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
            "openid_relying_party": {
                "scope": {
                    "subset_of": [
                         "eu.europa.ec.eudiw.pid.1",  
                         "eu.europa.ec.eudiw.pid.1:given_name",
                         "email"
                      ]
                },
               "request_authentication_methods_supported": {
                "one_of": ["request_object"]
                },
               "request_authentication_signing_alg_values_supported": {
                    "subset_of": ["RS256", "RS512", "ES256", "ES512", "PS256", "PS512"]
               }
            },
            "client": {
                "vp_formats": {
                    "jwt_vp": {
                        "alg":
                            "subset_of": [
                                "EdDSA",
                                "ES256K"
                            ]
                        }
                    }
                }
            }
        }
    }


.. note::

  **Entity Statement Signature**

  The same considerations and requirements made for the Entity Configuration must be applied for the Entity Statements.


Entity Statement
^^^^^^^^^^^^^^^^^^

The Entity Statement issued by Trust Anchors and Intermediates contain the following attributes:


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
     - JSON Object that describes the Metadata policy. Each key of the JSON Object represents an identifier of the type of Metadata and each value MUST be a JSON Object that represents the Metadata policy according to that Metadata type. Please refer to the `OIDC-FED`_ specifications, Section-5.1, for the implementation details.
     - |uncheck-icon|
   * - **trust_marks**
     - JSON Array containing the Trust Marks issued by itself for the subordinate subject.
     - |uncheck-icon|
   * - **constraints**
     - It MAY contain the **allowed_leaf_entity_types**, that restricts what types of metadata a subject is allowed to publish.
     - |check-icon|


Trust Evaluation Mechanism
--------------------------

The Trust Anchor publishes the list of its Intermediates (Federation Subordinate Listing endpoint) and the attestations of their metadata and public keys (Entity Statements).

Each participant, including Trust Anchor, Intermediate, Credential Issuer, Wallet Provider, and Relying Party, publishes its own metadata and public keys (Entity Configuration endpoint) on the well-known web resource **.well-known/openid-federation**.

Each of these can be verified using the Entity Statement issued by a superior, Trust Anchor, or Intermediate.

Each Entity Statement is verifiable over time and has an expiration date. The revocation of each statement is verifiable in real time and online (only for remote flows) through the federation endpoints.

.. note::
    The revocation of an Entity is made with the unavailability of the Entity Statement related to it. If the Trust Anchor or its Intermediates doesn't publish a valid Entity Statement, or if they publish an expired/invalid Entity Configuration, the subject of the Entity Statement must be intended as not valid or revoked.

The concatenation of the statements, through the combination of these signing mechanisms and the binding of claims and public keys, creates the Trust Chain.

The Trust Chains can also be verified offline, using only the Trust Anchor's public keys.

.. note::
    Since the Wallet Instance is not a Federation Entity, the Trust Evaluation Mechanism related to **it requires the presentation of the Wallet Instance Attestation during the credential issuance and presentation phases**.

    The Wallet Instance Attestation conveys all the required information pertaining to the instance, such as its public key and any other technical or administrative information, without any User's personal data.


Relying Party Attestation
^^^^^^^^^^^^^^^^^^^^^^^^^^

The Relying Party is accredited by a Trust Anchor or its Intermediate and obtains a Trust Mark to be included in its Entity Configuration. In its Entity Configuration the Relying Party publishes its specific metadata, including signature and encryption algorithms and any other necessary information for the interoperability requirements.

Any requests for user attributes, such as PID or (Q)EAA, from the Relying Party to Wallet Instances are signed and contain the verifiable Trust Chain regarding the Relying Party.

The Wallet Instance verifies that the Trust Chain related to the Relying Party is still active, having the proof that the Relying Party is still part of the Federation and not revoked.

The Trust Chain should be contained within the signed request in the form of a JWS header parameter.

In offline flows, Trust Chain verification enables the assessment of the reliability of Trust Marks and Attestations contained within.


Wallet Instance Attestation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Wallet Provider issues a Wallet Instance Attestation, certifying the operational status of its Wallet Instances, including one or more of their public keys. 

The Wallet Instance Attestation contains the Trust Chain that attests to the required public key's validity for itself and its issuer (Wallet Provider).

The Wallet Instance presents its Wallet Instance Attestation within the signed request during the PID issuance phase, containing the Trust Chain related to the Wallet Provider. The PID Provider issues a PID for each public key contained in the Wallet Instance Attestation, producing the Holder key Binding within the issued PID.

Trust Chain
^^^^^^^^^^^^^^^

The Trust Chain is the sequence of verified statements that validates a participant's compliance with the eIDAS Federation. It has an expiration date, beyond which it should be renewed to obtain updated metadata. The expiration date of the Trust Chain is determined by the earliest expiration date among all the expiration dates contained in the statements. No Entity can force the expiration date of the Trust Chain to be higher than the one configured by the Trust Anchor.

Below is an abstract representation of a Trust Chain.

.. code-block:: python

    [
        "EntityConfiguration-as-SignedJWT-selfissued-byLeaf",
        "EntityStatement-as-SignedJWT-issued-byTrustAnchor"
    ]

Below is a non-normative example of a Trust Chain in its original format (JSON Array containing JWS as strings) with an Intermediate involved.

.. code-block:: python

    [
     "eyJhbGciOiJFUzI1NiIsImtpZCI6ImVEUkNOSGhWYXpWd01VRlpjMVU0UlRremMxSjRNMGRVYUU4MWVVWk5VMVUyWkdSM1lqRmZTV2h1UVEiLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk1OTA2MDIsImlhdCI6MTY0OTQxNzg2MiwiaXNzIjoiaHR0cHM6Ly9ycC5leGFtcGxlLm9yZyIsInN1YiI6Imh0dHBzOi8vcnAuZXhhbXBsZS5vcmciLCJqd2tzIjp7ImtleXMiOlt7Imt0eSI6IkVDIiwia2lkIjoiZURSQ05IaFZhelZ3TVVGWmMxVTRSVGt6YzFKNE0wZFVhRTgxZVVaTlUxVTJaR1IzWWpGZlNXaHVRUSIsImNydiI6IlAtMjU2IiwieCI6Ik1wVlVHeUhlOGhQVHh5dklZRFd2NnJpZHN5aDFDUFB2TG94ZU0wUWhaN3ciLCJ5IjoidF95ZlBRd1Z1am5oS25fNVZnT05WcW93UzJvZGZwVWxfWnNvV1UzTDRHTSJ9XX0sIm1ldGFkYXRhIjp7Im9wZW5pZF9yZWx5aW5nX3BhcnR5Ijp7ImFwcGxpY2F0aW9uX3R5cGUiOiJ3ZWIiLCJjbGllbnRfaWQiOiJodHRwczovL3JwLmV4YW1wbGUub3JnLyIsImNsaWVudF9yZWdpc3RyYXRpb25fdHlwZXMiOlsiYXV0b21hdGljIl0sImp3a3MiOnsia2V5cyI6W3sia3R5IjoiRUMiLCJraWQiOiJlRFJDTkhoVmF6VndNVUZaYzFVNFJUa3pjMUo0TTBkVWFFODFlVVpOVTFVMlpHUjNZakZmU1dodVFRIiwiY3J2IjoiUC0yNTYiLCJ4IjoiTXBWVUd5SGU4aFBUeHl2SVlEV3Y2cmlkc3loMUNQUHZMb3hlTTBRaFo3dyIsInkiOiJ0X3lmUFF3VnVqbmhLbl81VmdPTlZxb3dTMm9kZnBVbF9ac29XVTNMNEdNIn1dfSwiY2xpZW50X25hbWUiOiJOYW1lIG9mIGFuIGV4YW1wbGUgb3JnYW5pemF0aW9uIiwiY29udGFjdHMiOlsib3BzQHJwLmV4YW1wbGUuaXQiXSwiZ3JhbnRfdHlwZXMiOlsicmVmcmVzaF90b2tlbiIsImF1dGhvcml6YXRpb25fY29kZSJdLCJyZWRpcmVjdF91cmlzIjpbImh0dHBzOi8vcnAuZXhhbXBsZS5vcmcvb2lkYy9ycC9jYWxsYmFjay8iXSwicmVzcG9uc2VfdHlwZXMiOlsiY29kZSJdLCJzY29wZXMiOiJldS5ldXJvcGEuZWMuZXVkaXcucGlkLjEgZXUuZXVyb3BhLmVjLmV1ZGl3LnBpZC5pdC4xIGVtYWlsIiwic3ViamVjdF90eXBlIjoicGFpcndpc2UifSwiZmVkZXJhdGlvbl9lbnRpdHkiOnsiZmVkZXJhdGlvbl9yZXNvbHZlX2VuZHBvaW50IjoiaHR0cHM6Ly9ycC5leGFtcGxlLm9yZy9yZXNvbHZlLyIsIm9yZ2FuaXphdGlvbl9uYW1lIjoiRXhhbXBsZSBSUCIsImhvbWVwYWdlX3VyaSI6Imh0dHBzOi8vcnAuZXhhbXBsZS5pdCIsInBvbGljeV91cmkiOiJodHRwczovL3JwLmV4YW1wbGUuaXQvcG9saWN5IiwibG9nb191cmkiOiJodHRwczovL3JwLmV4YW1wbGUuaXQvc3RhdGljL2xvZ28uc3ZnIiwiY29udGFjdHMiOlsidGVjaEBleGFtcGxlLml0Il19fSwidHJ1c3RfbWFya3MiOlt7ImlkIjoiaHR0cHM6Ly9yZWdpc3RyeS5laWRhcy50cnVzdC1hbmNob3IuZXhhbXBsZS5ldS9vcGVuaWRfcmVseWluZ19wYXJ0eS9wdWJsaWMvIiwidHJ1c3RfbWFyayI6ImV5SmggXHUyMDI2In1dLCJhdXRob3JpdHlfaGludHMiOlsiaHR0cHM6Ly9pbnRlcm1lZGlhdGUuZWlkYXMuZXhhbXBsZS5vcmciXX0.dIRBRyfEsmi_6oGrJAHaYUPCtXSvBZBMdokVZtjyYgzMKEP6eSLixa8nUU9BWBWP_ELNgdKbPquSbWIGx66D5w",
     "eyJhbGciOiJFUzI1NiIsImtpZCI6IlFWUnVXSE5FWTJzMFdHNW5hSHB3VjJKVGRtd3hiRUpVY2pCdk9FeHNWMFExT0dnMFZWQnhhbTUyT0EiLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk2MjM1NDYsImlhdCI6MTY0OTQ1MDc0NiwiaXNzIjoiaHR0cHM6Ly9pbnRlcm1lZGlhdGUuZWlkYXMuZXhhbXBsZS5vcmciLCJzdWIiOiJodHRwczovL3JwLmV4YW1wbGUub3JnIiwiandrcyI6eyJrZXlzIjpbeyJrdHkiOiJFQyIsImtpZCI6ImVEUkNOSGhWYXpWd01VRlpjMVU0UlRremMxSjRNMGRVYUU4MWVVWk5VMVUyWkdSM1lqRmZTV2h1UVEiLCJjcnYiOiJQLTI1NiIsIngiOiJNcFZVR3lIZThoUFR4eXZJWURXdjZyaWRzeWgxQ1BQdkxveGVNMFFoWjd3IiwieSI6InRfeWZQUXdWdWpuaEtuXzVWZ09OVnFvd1Myb2RmcFVsX1pzb1dVM0w0R00ifV19LCJtZXRhZGF0YV9wb2xpY3kiOnsib3BlbmlkX3JlbHlpbmdfcGFydHkiOnsic2NvcGVzIjp7InN1YnNldF9vZiI6WyJldS5ldXJvcGEuZWMuZXVkaXcucGlkLjEsICBldS5ldXJvcGEuZWMuZXVkaXcucGlkLml0LjEiXX0sInJlcXVlc3RfYXV0aGVudGljYXRpb25fbWV0aG9kc19zdXBwb3J0ZWQiOnsib25lX29mIjpbInJlcXVlc3Rfb2JqZWN0Il19LCJyZXF1ZXN0X2F1dGhlbnRpY2F0aW9uX3NpZ25pbmdfYWxnX3ZhbHVlc19zdXBwb3J0ZWQiOnsic3Vic2V0X29mIjpbIlJTMjU2IiwiUlM1MTIiLCJFUzI1NiIsIkVTNTEyIiwiUFMyNTYiLCJQUzUxMiJdfX19LCJ0cnVzdF9tYXJrcyI6W3siaWQiOiJodHRwczovL3RydXN0LWFuY2hvci5leGFtcGxlLmV1L29wZW5pZF9yZWx5aW5nX3BhcnR5L3B1YmxpYy8iLCJ0cnVzdF9tYXJrIjoiZXlKaGIgXHUyMDI2In1dfQ.rIgdHa7CoaP3SO3ZNsjDWt7-8Tea41An3YBw-qaWFNdQMUzcTqRwcD4vtX6TZEEoRO3KEu8bJeaKlikHRHzoBg",
     "eyJhbGciOiJFUzI1NiIsImtpZCI6ImVVRldSakJKYlhVeU5TMHRhV1JrYlhCMWVURlBjazV6UzBGRVFTMWFNVFpEYTNOWk1WUktURTR5Y3ciLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk2MjM1NDYsImlhdCI6MTY0OTQ1MDc0NiwiaXNzIjoiaHR0cHM6Ly90cnVzdC1hbmNob3IuZXhhbXBsZS5ldSIsInN1YiI6Imh0dHBzOi8vaW50ZXJtZWRpYXRlLmVpZGFzLmV4YW1wbGUub3JnIiwiandrcyI6eyJrZXlzIjpbeyJrdHkiOiJFQyIsImtpZCI6IlFWUnVXSE5FWTJzMFdHNW5hSHB3VjJKVGRtd3hiRUpVY2pCdk9FeHNWMFExT0dnMFZWQnhhbTUyT0EiLCJjcnYiOiJQLTI1NiIsIngiOiJCR1VOOXN6ZG0xT1RxVWhUQ3JkcWRmQjhtTUJqb2JCYk5Nd2JxZnd4c3pZIiwieSI6IkdnMUhCNGVJRWJhQjA4NEJiUW5QX0lseFJZYTNhVVRHSTF0aW5qTmVSdmMifV19LCJ0cnVzdF9tYXJrcyI6W3siaWQiOiJodHRwczovL3RydXN0LWFuY2hvci5leGFtcGxlLmV1L2ZlZGVyYXRpb25fZW50aXR5L3RoYXQtcHJvZmlsZSIsInRydXN0X21hcmsiOiJleUpoYiBcdTIwMjYifV19.KR2oBDMfqLGCZ2ZqN0FgOP7cWsW4ClxBaj4-j_c3HC-YEecK6SLlNk00bGqoEe2NCMy2lqk9dYQO1IauB_ZG7A"
    ]

.. note::

    The entire Trust Chain is verifiable by possessing only the Trust Anchor’s public key.


Offline Trust Attestation Mechanisms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this section, we describe the implementation requirements to enable
offline trust evaluation mechanisms.

.. note::
  The offline flows do not allow for real-time evaluation of an Entity's status, such as its revocation. At the same time, using short-lived Trust Chains enables the attainment of trust attestations compatible with the required revocation administrative protocols (e.g., a revocation must be propagated in less than 24 hours, thus the Trust Chain must not be valid for more than that period).


Offline EUDI Wallet Trust Attestation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given that a mobile device should not publish its metadata online at the *.well-known/openid-federation* endpoint, or in any other way, it is not mandatory for the Wallet Instance to publish its metadata if the User does not want this. As a result, the Wallet Instance does not need to publish its federation metadata online.

However, the Wallet Instance should obtain a Wallet Attestation Instance issued by its Wallet Provider, which should contain a Trust Chain related to its issuer (Wallet Provider).

Offline Relying Party Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since the Federation Entity Discovery is only applicable in online scenarios, it is possible to include the Trust Chain in the presentation requests that a Relying Party may issue for a Wallet Instance.

The Relying Party must sign the presentation request, which should include the `trust_chain` claim in its header parameter, containing the Federation Trust Chain related to itself.

The Wallet Instance that verifies the request issued by the Relying Party can then use the Trust Anchor public keys to validate the entire Trust Chain related to the Relying Party and attest to its reliability.

Furthermore, the Wallet Instance applies the metadata policy, if available, to filter out any User attributes not attested in the Relying Party metadata, as derived from the Trust Chain made available in the Relying Party's signed request.

Non-repudiability of the Long Lived Attestations
--------------------------------------------------

The Trust Anchor and its Intermediate MUST expose the Historical keys endpoint, where are published all the public keys that are no longer used, whether expired or revoked.

The details of this endpoint are defined in the `OIDC-FED`_ Section 7.6.

Each JWS containing a Trust Chain in the form of a JWS header parameter can be verified over time, since the entire Trust Chain is verifiable using the Trust Anchor's public key.

Even if the Trust Anchor has changed its cryptographic keys for digital signature, the historical keys endpoint always makes the keys no longer used available for historical signature verifications.


Privacy Considerations
----------------------

- Wallet Instances do not publish their metadata through an online service.
- The trust infrastructure is public, with all endpoints publicly accessible without any client credentials that may disclose who is requesting access.
- When a Wallet Instance requests the Entity Statements to build the Trust Chain for a specific Relying Party or validates a Trust Mark online, issued for a specific Relying Party, the Trust Anchor or its Intermediate do not know that a particular Wallet Instance is inquiring about a specific Relying Party; instead, they only serve the statements related to that Relying Party as a public resource.
- The Wallet instance metadata must not contain information that may disclose technical information about the hardware used.
- Leaf entity, Intermediate, and Trust Anchor metadata may include the necessary amount of data as part of administrative, technical, and security contact information. It is generally not recommended to use personal contact details in such cases. From a legal perspective, the publication of such information is needed for operational support concerning technical and security matters and is in line with GDPR.

Considerations about Decentralization
-------------------------------------

- There should be more than one Trust Anchor.
- In some cases, a trust verifier may trust an Intermediate, especially when the Intermediate may represent itself as a Trust Anchor within a specific perimeter, such as cases where the Leafs are both in the same perimeter like a Member State jurisdiction (eg: Italian RP with an Italian Wallet Instance may consider the Italian Accreditation Body as Trust Anchor).
- Trust attestations (Trust Chain) should be included in the JWS issued by Credential Issuers, and the Presentation Requests of RPs should contain the Trust Chain related to them (issuers of the presentation requests).
- Since the credential presentation must be signed, saving the signed presentation requests and responses, which include the Trust Chain, the Wallet Instance has a snapshot of the federation configuration (Trust Anchor Entity Configuration in the Trust Chain) and the verifiable reliability of the Relying Party it has interacted with. This information must be stored on the Wallet Device and backed up in a remote and secure cloud storage, with the explicit permission of its User.
- Each signed attestation is long-lived since it can be cryptographically validated even when the federation configuration changes or the keys of its issuers are renewed.
- Each participant should be able to update its Entity Configuration without notifying the changes to any third party. The Metadata Policy of a Trust Chain must be applied to overload any information related to protocol metadata and allowed grants of the participants.
