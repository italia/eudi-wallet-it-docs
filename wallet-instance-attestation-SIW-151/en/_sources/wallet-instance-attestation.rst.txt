.. include:: ../common/common_definitions.rst

.. _wallet-instance-attestation.rst:

Wallet Instance Attestation
+++++++++++++++++++++++++++

Inside a **Wallet Solution** and, especially with regards
to the **Wallet Instance**, it is essential to ensure the **authenticity,
integrity, security, privacy and trust** in the use of the latter both
by the User and the services connected to it, such as the
**PID Provider** or one **Relying Party**.


General Properties
------------------

The goal is:

- Ensure that the Wallet Instance maintains a level of **integrity**,
  capable of preventing any attempts of manipulation or forgery
  by unauthorized third parties.
- The Wallet Provider issues a certificate of conformity,
  assuring that the above mentioned security and trust
  goals are fulfilled.


In compliance of the above mentioned requirements, it is necessary for each
Wallet Instance to issue a certificate of conformity,
guaranteeing its security and compliance with the Trust Model.

This attestation is called **Wallet Instance Attestation**
and must be electronically signed by its issuer.

.. hint::
  Considering that the Wallet Instance does not represent an accredited
  entity and does not belong to an organization,
  but resides on the User's device, the Trust Model,
  based on sustainability and scalability criteria,
  must delegate to the **Wallet Provider** the task of
  issuing the **Wallet Instance Attestation**.


Requirements
------------

We assume the following requirements for the Wallet Instance Attestation:

1. **Efficiency**: The Wallet Instance Attestation should use an efficient
   format such as JSON Web Token (JWT) to ensure light and fast data management
   and be compliant with the various formats used for eudiw solutions.
2. **Simplicity**: The Wallet Provider should be based on a REST architecture
   for issuing Wallet Instance Attestations.
3. **Public key holder binding**: The Wallet Instance Attestation must be
   securely linked to the Wallet Instance public key.
4. **Issued and signed by an accredited Wallet Provider**:
   The Wallet Instance Attestation must be issued and signed by an accredited
   and reliable Wallet Provider, thus conferring integrity and authenticity
   to the attestation itself.
5. **Authenticity/Genuineness of the Wallet Instance**:
   The Wallet Instance Attestation must guarantee the integrity
   and authenticity of the Wallet Instance, confirming that it was
   created and provided correctly by the Wallet Provider. ⚠️
6. **Ability to request multiple claims for several public keys**:
   Each single Wallet Instance should be able to request multiple attestations
   for different public keys associated with it. This requirement constitutes
   a privacy-preserving measure since the public key may be exploited as a
   tracking tool in the credentials’ disclosure phase
   (see also point 10 below).
7. **Can be used multiple times**:
   The Wallet Instance Attestation should be used multiple times
   during the validity period of the attestation, allowing for repeated
   authentication and authorization without the need to request
   new attestations with each interaction.
8. **Expiration**:
   The Wallet Instance Attestation should have a well-defined expiration date,
   after which it will no longer be considered valid, thus ensuring
   the security and updating of the attestations over time.
9.  **Revocation in case of loss/deletion of the private key**:
    If the private key associated with the Wallet Instance is lost or deleted,
    the attestation automatically becomes invalid to prevent unauthorized
    use of the Wallet Instance. ⚠️
10. **Pseudonymisation**:
    The attestations are designed to be pseudonymised
    (i.e. they do not contain direct references to the person, so that it
    is not possible to identify them in the absence of additional information
    \- see art. 4(5) GDPR for a comprehensive definition).
    In the absence of such a measure, the use of the attestation on multiple
    RPs would constitute an appreciable risk, as it would theoretically
    allow the RPs to merge databases and track Users.
    This requirement enriches the measures adopted in accordance
    with art. 32 GDPR.

.. attention::
  ⚠️ Implementation of points no. 5 and 9 is still under discussion.
  This version assumes the authenticity and non-revocability of the Wallet Instance.



High-end design
---------------


Static view of the components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../images/static_view_wallet_instance_attestation.svg
   :name: Wallet Solution schema
   :alt: the image shows how the Wallet Provider and the
         Wallet Instances are contained within the Wallet
         Solution which is managed by the Wallet Provider
   :target: https://www.plantuml.com/plantuml/uml/XP4nJuSm44VtVehBdxbnPp2iRYx6qTHIjR7SaVQ0-EqzaICDgN4ZBxpqzTUXiCkyJCaupvJXzbH2le4hiCW7A7rsAGM6ETCQn-E7RMSloi0OJzDC691FeL1QE1BMWZBeraW2Mbv4wK8VQayPT5yX9TgCQPclpdy676lnGF0ZN93DyVs3xVsrhOU70hCi0_JshwHXFJp-Rg4dIuECo96moD7xeBQbUKBEbE0EPEwuEWx6N2zj_uXqU8wbhVMhD3tjbAX1BYIl_mq0

Dynamic view of the components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In this section is described the format of the Wallet Instance Attestation and
how it is issued by the Wallet Provider.

.. figure:: ../../images/dynamic_view_sequence_wallet_instance_attestation.svg
   :name: sequence diagram for Wallet Instance Attestation request
   :alt: The figure shows the sequence diagram for issuing a Wallet Instance Attestation.
         The steps will be described below.
   :target: https://www.plantuml.com/plantuml/uml/XPB1RzKm3CRl-IlCJY3nn7s7QOZ3118IGi0kkxYDLLcqJd2SLMz_FLvV6r7AnDN-_Fi-ExajXcfr6iEhh3XC24Rf2Kmh1QoMf4uTQGZPLTnpHZ6u-bv8hm0Br7tz7iUH33wAGwMdHJBpFpLVD3roN35p5qA5qusBhtsQZN7a9uBvekMLzo19GUbNfMBlib8X1_PAaUHveeIPJpTpTmrtPDjiNdrW8iE8Xc7kJgvoeyzh1VeaXYmimnyqi7EcyXP-qddnPAN9EruXYJcnsEhdf1yUrqbqC3MjnM3aOgxT5hmZ8NNrWix8MhQcH_zwMGyaIK-U5KwNgRNGB3yeFIF-kZYyBuNKE4a3VRh_5h0tVbpoTRiROLE__Y_eZOTP9W_RyZOpa5GM4YhbA2uy25fLQgrXkmDANDe7OClN7ktbXO-FyJ8jqluYpguDtVJSFc9y42MCPx04gJDa0Q5vz_LkIMATnjy0

- **Message 1**: The User initializes the Wallet Instance.
  In particular, this process happens after the Wallet Instance installation and after the expiration of the Wallet Instance Attestation
  is launched and every time the User wants to request or present
  (disclose) a credential.
- **Message 2-3**: The Wallet Instance obtains metadata about its Wallet
  Provider. Among these, we also find the list of supported algorithms,
  public keys, endpoints.
- **Message 4**: The Wallet Instance verifies that the Wallet Provider is
  trustworthy by resolving the provider's trust chain up to the anchor
- **Message 5-7**: The Wallet Instance instantiates a new key pair on its TEE
  and requests a ``nonce`` from the Wallet Provider (as a measure
  against replay attacks).
- **Message 8**: The Wallet Instance generates a Wallet Instance Attestation
  Request, in JWS format, signed with the private key associated with the
  public key for which it wants to obtain the attestation containing
  the ``nonce`` and all the required parameters.
- **Message 9-13**: The Wallet Instance sends the Wallet Instance Attestation
  Request to the Wallet Provider which verifies its validity and
  issues the signed attestation.
- **Message 13-14**:The Wallet Instance receives the Wallet Instance
  Attestation signed by the Wallet Provider and proceeds with a formal
  verification.
- **Message 15**:The Wallet Instance Attestation is ready to be consumed.


Detail design
---------------
We will go into the detail design below.

Format of the Wallet Provider Entity Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Wallet Provider Entity Configuration is a JWS containing
the public keys and the supported algorithms
within the Wallet Provider metadata definition.
It is defined according to `OpenID Connect Federation <https://openid.net/specs/openid-connect-federation-1_0.html>`_
and Section Trust Model of this specification.

Header
^^^^^^
+---------+-----------------------------------------------------------------+
| **key** | **value**                                                       |
+---------+-----------------------------------------------------------------+
| alg     | Algorithm to verify the token signature (es. ES256).            |
+---------+-----------------------------------------------------------------+
| kid     | Thumbprint of the public key used for signing.                  |
+---------+-----------------------------------------------------------------+
| typ     | Media type, in this case, we use the entity-statement+jwt value.|
+---------+-----------------------------------------------------------------+

Payload
^^^^^^^
+-----------------------------------+-----------------------------------+
| **key**                           | **value**                         |
+-----------------------------------+-----------------------------------+
| iss                               | The public url of the Wallet      |
|                                   | Provider.                         |
+-----------------------------------+-----------------------------------+
| sub                               | The public url of the Wallet      |
|                                   | Provider.                         |
+-----------------------------------+-----------------------------------+
| iat                               | Configuration release timestamp.  |
+-----------------------------------+-----------------------------------+
| exp                               | Configuration expiration          |
|                                   | timestamp.                        |
+-----------------------------------+-----------------------------------+
| jwks                              | Containing the keys attribute     |
|                                   | which is an array of all the      |
|                                   | public keys associated with the   |
|                                   | domain (they could also match     |
|                                   | those of the Wallet Provider).    |
+-----------------------------------+-----------------------------------+
| metadata                          | This attribute will contain for   |
|                                   | each entity its own               |
|                                   | metadata. In this case we         |
|                                   | will have the Wallet              |
|                                   | Provider metadata contained within|
|                                   | the ``eudi_wallet_provider``      |
|                                   | attribute and the more generic    |
|                                   | entity ``federation_entity``.     |
+-----------------------------------+-----------------------------------+

Payload `eudi_wallet_provider`
''''''''''''''''''''''''''''''
+------------------------------------+------------------------------------+
| **key**                            | **value**                          |
+------------------------------------+------------------------------------+
|| jwks                              || Containing the keys attribute     |
||                                   || which is an array of all the      |
||                                   || Wallet Provider's public keys.    |
+------------------------------------+------------------------------------+
|| token_endpoint                    || Endpoint for obtaining the Wallet |
||                                   || Instance Attestation.             |
+------------------------------------+------------------------------------+
|| asc_values_supported              || List of supported values for      |
||                                   || the certified security context.   |
||                                   || These values define a level of    |
||                                   || assurance about the security of   |
||                                   || the app. In particular we will    |
||                                   || mainly have 3 values associated   |
||                                   || with low, medium and high         |
||                                   || security. An attested security    |
||                                   || context is defined according to   |
||                                   || the proof that the Wallet         |
||                                   || Instance is able to send to the   |
||                                   || Wallet Provider.                  |
||                                   || ⚠️ This parameter is not standard |
||                                   || and is still under discussion.    |
+------------------------------------+------------------------------------+
|| grant_types_supported             || The type of grants supported by   |
||                                   || the endpoint token. Therefore,    |
||                                   || for the Wallet Provider the token |
||                                   || is equivalent only to the Wallet  |
||                                   || Instance attestation, therefore   |
||                                   || this attribute will contain an    |
||                                   || array with only one element.      |
+------------------------------------+------------------------------------+
|| token_endpoint_auth_methods_suppo || Supported authentication method   |
|| rted                              || for the endpoint token.           |
||                                   ||                                   |
+------------------------------------+------------------------------------+
|| token_endpoint_auth_signing_alg_v || List of supported signature       |
|| alues_supported                   || algorithms.                       |
+------------------------------------+------------------------------------+

.. note::
   The parameter `asc_values_supported` is experimental and still
   under discussion.

Payload `federation_entity`
'''''''''''''''''''''''''''
+-------------------+----------------------------------------+
| **key**           | **value**                              |
+-------------------+----------------------------------------+
| organization_name | Organization name.                     |
+-------------------+----------------------------------------+
| homepage_uri      | Organization website.                  |
+-------------------+----------------------------------------+
| tos_uri           | Url to the terms of use.               |
+-------------------+----------------------------------------+
| policy_uri        | Url to the privacy policy.             |
+-------------------+----------------------------------------+
| logo_uri          | URL of the organization logo.          |
+-------------------+----------------------------------------+

Below a non-normative example of the Entity Configuration.

.. code-block:: javascript

  {
    "alg": "ES256",
    "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
    "typ": "entity-statement+jwt"
  }
  .
  {
  "iss": "https://wallet-provider.example.org",
  "sub": "https://wallet-provider.example.org",
  "jwks": {
    "keys": [
      {
        "crv": "P-256",
        "kty": "EC",
        "x": "qrJrj3Af_B57sbOIRrcBM7br7wOc8ynj7lHFPTeffUk",
        "y": "1H0cWDyGgvU8w-kPKU_xycOCUNT2o0bwslIQtnPU6iM",
        "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY"
      }
    ]
  },
  "metadata": {
    "eudi_wallet_provider": {
      "jwks": {
        "keys": [
          {
            "crv": "P-256",
            "kty": "EC",
            "x": "qrJrj3Af_B57sbOIRrcBM7br7wOc8ynj7lHFPTeffUk",
            "y": "1H0cWDyGgvU8w-kPKU_xycOCUNT2o0bwslIQtnPU6iM",
            "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY"
          }
        ]
      },
      "token_endpoint": "https://wallet-provider.example.org/token",
      "asc_values_supported": [
        "https://wallet-provider.example.org/LoA/basic",
        "https://wallet-provider.example.org/LoA/medium",
        "https://wallet-provider.example.org/LoA/high"
      ],
      "grant_types_supported": [
        "urn:ietf:params:oauth:client-assertion-type:jwt-key-attestation"
      ],
      "token_endpoint_auth_methods_supported": [
        "private_key_jwt"
      ],
      "token_endpoint_auth_signing_alg_values_supported": [
        "ES256",
        "ES384",
        "ES512"
      ]
    },
    "federation_entity": {
      "organization_name": "PagoPa S.p.A.",
      "homepage_uri": "https://wallet-provider.example.org",
      "policy_uri": "https://wallet-provider.example.org/privacy_policy",
      "tos_uri": "https://wallet-provider.example.org/info_policy",
      "logo_uri": "https://wallet-provider.example.org/logo.svg"
    }
  },
  "iat": 1687171759,
  "exp": 1709290159
  }


Format of the Wallet Instance Attestation Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To obtain a Wallet Instance Attestation from the Wallet
Provider it is necessary to send a Wallet Instance Attestation
Request from the Wallet Instance containing the associated public key
and a ``nonce`` previously requested to avoid replay attacks.

Header
^^^^^^
+-----------------------------------+-----------------------------------+
| **key**                           | **value**                         |
+-----------------------------------+-----------------------------------+
| alg                               | Algorithm to verify the token     |
|                                   | signature (es. ES256)             |
+-----------------------------------+-----------------------------------+
| kid                               | Key id of the Wallet Instance     |
+-----------------------------------+-----------------------------------+
| typ                               | Media type, in this case we use   |
|                                   | the value var+jwt (Verifiable     |
|                                   | Assertion Request JWT)            |
+-----------------------------------+-----------------------------------+

Payload
^^^^^^^
+---------+---------------------------------------+
| **key** | **value**                             |
+---------+---------------------------------------+
|| iss    || The thumbprint                       |
||        || of the JWK of the Wallet Instance    |
||        || for which the attestation is         |
||        || being requested.                     |
+---------+---------------------------------------+
|| sub    || The public url of the Wallet         |
||        || Provider                             |
+---------+---------------------------------------+
|| jti    || Unique identifier of the request.    |
||        || This parameter will be used to       |
||        || avoid replay attacks.                |
+---------+---------------------------------------+
|| type   || String. It must be set to            |
||        || ``WalletInstanceAttestationRequest`` |
+---------+---------------------------------------+
|| cnf    || This parameter will contain the      |
||        || configuration of the Wallet          |
||        || Instance in JSON format. Among       |
||        || the mandatory attributes there       |
||        || will be the jwk parameter            |
||        || containing the public key of the     |
||        || Wallet Instance. It will also        |
||        || contain all the information          |
||        || useful for the Wallet Provider       |
||        || to verify that the app is genuine.   |
+---------+---------------------------------------+

Below a non-normative example of the Wallet Instance Attestation
request where the decoded JWS headers and payload are separated by a comma:

.. code-block:: javascript

  {
    "alg": "ES256",
    "kid": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "typ": "var+jwt"
  }
  .
  {
    "iss": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "sub": "https://wallet-provider.example.org",
    "jti": "6ec69324-60a8-4e5b-a697-a766d85790ea",
    "type": "WalletInstanceAttestationRequest",
    "cnf": {
      "jwk": {
        "crv": "P-256",
        "kty": "EC",
        "x": "4HNptI-xr2pjyRJKGMnz4WmdnQD_uJSq4R95Nj98b44",
        "y": "LIZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg",
        "kid": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"
      }
    },
    "iat": 1686645115,
    "exp": 1686652315
  }

Whose corresponding JWS is verifiable through the public key
of the Wallet Instance present.


Format of the Wallet Instance Attestation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A JWT was chosen as the format for the Wallet Instance Attestation.
Let's see below the various fields that compose it.

Header
^^^^^^

+-----------------------------------+-----------------------------------+
| **key**                           | **value**                         |
+-----------------------------------+-----------------------------------+
| alg                               | Algorithm to verify the token     |
|                                   | signature (es. ES256).            |
+-----------------------------------+-----------------------------------+
| kid                               | Key id used by the Wallet         |
|                                   | Provider to sign the attestation. |
+-----------------------------------+-----------------------------------+
| typ                               | Media type, in this case we use   |
|                                   | the value va+jwt (Verifiable      |
|                                   | Assertion JWT).                   |
|                                   | This parameter is currently       |
|                                   | non-standard as it is not yet     |
|                                   | registered as `IANA Media         |
|                                   | Types <https://www.iana.org/assig |
|                                   | nments/media-types/media-types.xh |
|                                   | tml>`__.                          |
+-----------------------------------+-----------------------------------+
| x5c                               | Array containing the X.509        |
|                                   | certificate (and the entire chain |
|                                   | of certificates) used to certify  |
|                                   | the public key of the issuer.     |
+-----------------------------------+-----------------------------------+
| trust_chain                       | Array containing the JWS of the   |
|                                   | trust chain relating to its       |
|                                   | issuer (Wallet Provider).         |
+-----------------------------------+-----------------------------------+

Payload
^^^^^^^

+---------------------------+-------------------------------------------+
| **key**                   | **value**                                 |
+---------------------------+-------------------------------------------+
|| iss                      || The public url of the Wallet             |
||                          || Instance attestation issuer. See         |
||                          || the example below in this section.       |
+---------------------------+-------------------------------------------+
|| sub                      || The public url of the issuer             |
||                          || concatenated with the thumbprint         |
||                          || of the JWK of the Wallet Instance        |
||                          || for which the attestation is             |
||                          || being issued.                            |
+---------------------------+-------------------------------------------+
|| iat                      || Unix timestamp of attestation            |
||                          || issuance time.                           |
+---------------------------+-------------------------------------------+
|| exp                      || Unix timestamp regarding the             |
||                          || expiration date time.                    |
||                          || A good practice to avoid security        |
||                          || problems is to have a limited            |
||                          || duration of the attestation.             |
+---------------------------+-------------------------------------------+
|| type                     || String:                                  |
||                          || "WalletInstanceAttestation".             |
+---------------------------+-------------------------------------------+
|| policy_uri               || Url to the privacy policy                |
||                          || of the wallet.                           |
+---------------------------+-------------------------------------------+
|| tos_uri                  || Url to the terms                         |
||                          || of use of the Wallet Provider.           |
+---------------------------+-------------------------------------------+
|| logo_uri                 || Logo url of the Wallet Provider.         |
+---------------------------+-------------------------------------------+
|| asc                      || Attested security context:               |
||                          || Represents a level of "trust" of         |
||                          || the service containing a Level Of        |
||                          || Agreement defined in the metadata        |
||                          || of the Wallet Provider.                  |
+---------------------------+-------------------------------------------+
|| cnf                      || This parameter contains the ``jwk``      |
||                          || parameter                                |
||                          || with the public key of the Wallet        |
||                          || necessary for the holder binding.        |
+---------------------------+-------------------------------------------+
|| authorization_endpoint   || URL of the OP's OAuth 2.0                |
||                          || Authorization Endpoint.                  |
+---------------------------+-------------------------------------------+
|| response_types_supported || JSON array containing a list of          |
||                          || the OAuth 2.0 response_type values       |
||                          || that this OP supports.                   |
+---------------------------+-------------------------------------------+
|| vp_formats_supported     || JSON object containing                   |
||                          || ``jwt_vp_json`` and ``jwt_vc_json``      |
||                          || supported algorithms array.              |
+---------------------------+-------------------------------------------+
|| request_object_signing   || JSON array containing a list of the      |
|| _alg_values_supported    || JWS signing algorithms (alg values)      |
||                          || supported by the OP for Request Objects. |
+---------------------------+-------------------------------------------+
|| presentation_definition  || Boolean value specifying whether the     |
|| _uri_supported           || Wallet Instance supports the transfer of |
||                          || presentation_definition by               |
||                          || reference, with true indicating support. |
+---------------------------+-------------------------------------------+

.. note::
   The claim ``asc`` (Attested Security Context) is under discussion
   and must be intended as experimental.

Signature
^^^^^^^^^

The Wallet Instance Attestation JWS is signed using the
private key of the Wallet Provider.

Below is an example of Wallet Instance Attestation:

.. code-block:: javascript

  {
    "alg": "ES256",
    "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
    "trust_chain": [
      "eyJhbGciOiJFUz...6S0A",
      "eyJhbGciOiJFUz...jJLA",
      "eyJhbGciOiJFUz...H9gw",
    ],
    "typ": "va+jwt",
    "x5c": ["MIIBjDCC ... XFehgKQA=="]
  }
  .
  {
    "iss": "https://wallet-provider.example.org",
    "sub": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "type": "WalletInstanceAttestation",
    "policy_uri": "https://wallet-provider.example.org/privacy_policy",
    "tos_uri": "https://wallet-provider.example.org/info_policy",
    "logo_uri": "https://wallet-provider.example.org/logo.svg",
    "asc": "https://wallet-provider.example.org/LoA/basic",
    "cnf":
    {
      "jwk":
      {
        "crv": "P-256",
        "kty": "EC",
        "x": "4HNptI-xr2pjyRJKGMnz4WmdnQD_uJSq4R95Nj98b44",
        "y": "LIZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg",
        "kid": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"
      }
    },
    "authorization_endpoint": "eudiw:",
    "response_types_supported": [
      "vp_token"
    ],
    "vp_formats_supported": {
      "jwt_vp_json": {
        "alg_values_supported": ["ES256"]
      },
      "jwt_vc_json": {
        "alg_values_supported": ["ES256"]
      }
    },
    "request_object_signing_alg_values_supported": [
      "ES256"
    ],
    "presentation_definition_uri_supported": false,
    "iat": 1687281195,
    "exp": 1687288395
  }


Endpoints
~~~~~~~~~
The Wallet Provider that issues the Wallet Instance Attestations must
make available a series of APIs in REST format that follow the OpenID
Federation standard.

Metadata
^^^^^^^^
A **GET /.well-known/openid-federation endpoint** for retrieving the Wallet
Provider Entity Configuration.

Wallet Instance Attestation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

A second **POST /token** endpoint that takes two parameters as input:

``grant_type`` which in our case is a string:
``urn:ietf:params:oauth:client-assertion-type:jwt-key-attestation``

``assertion``` which contains the signed JWT of the Wallet Instance Attestation
Request.

The response will then contain the Wallet Instance Attestation.
