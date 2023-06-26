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
- Make sure the private keys have been generated and stored securely
  within a **trusted execution environment** (TEE).
- Verify that the Wallet Instance is **authentic**, i.e. made available
  by an accredited body that complies with the Trust Model.

To guarantee the above, it is necessary for each
Wallet Instance to issue a certificate of conformity,
guaranteeing its security and compliance with the Trust Model.

This attestation is called **Wallet Instance Attestation**
and must be electronically signed by its issuer.

.. hint::
  Considering that the Wallet Instance does not represent an accredited
  entity and does not belong to an organization,
  but resides on the User's device, the Trust Model,
  based on sustainability and scalability criteria,
  must delegate to the **Wallet provider** the task of
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
   :alt: the image shows how the Wallet Provider's backend and the
         Wallet Instances are contained within the wallet
         solution which is managed by the Wallet Provider
   :target: https://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000

Dynamic view of the components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We do not go into the details of the Wallet Provider's backend as
it will be the subject of a subsequent design review. For now, we
will just analyze the format of the Wallet Instance Attestation and
how it is issued by the Wallet Provider's backend.

.. figure:: ../../images/dynamic_view_sequence_wallet_instance_attestation.svg
   :name: sequence diagram for Wallet Instance Attestation request
   :alt: The figure shows the sequence diagram for issuing a Wallet Instance Attestation.
         The steps will be described below.
   :target: https://www.plantuml.com/plantuml/uml/XPB1RjH038RlynIc9v1OSU-XAk9GWSG50RtqucH-HLOJJ_1u6csVdcbsTqG85LVxy-VypjncP_CoZU7DR3nCJ8xqJ6u5WOidBLC72s6kbFGoipfT_SYmA-9CPLk_vt64qsUjKksn8elya-cuVuJ64zA5KEXmKzdhEYmkFCepQ3cXSjOzQ38o_2h8_c4sP5HVRuZGbuaS5ZdSBDqrtS4lixEb9uamck0SsJaitQ5ITT7NSuNwfCwYeiCVDlBZZFoU7d5STufXWdgjGEESHFsyhvf-yYZLXDrIjvATHibUsKl0EoYiqgjwPh4SGbDzChoq_ZeaVSmPvfAKlftoqvVxxu5xbwTrRxV9per--r_HktgGTNANGYup0xI8Gf7p7iuoA7injDPmoSSQr_PEsBwl_OpN0--F_BejOdkHwYvDtNXf3om-g87ZaJnHwfn5IR5idjGjD9Pf_0q0

- **Message 1**: The end User initializes the Wallet Instance.
  In particular, this process happens when the mobile application
  is launched and every time the end User wants to request or present
  (disclose) a credential.
- **Message 2-3**: The Wallet Instance obtains metadata about its wallet
  provider. Among these, we also find the list of supported algorithms,
  public keys, endpoints.
- **Message 4**: The Wallet Instance verifies that the Wallet Provider is
  trustworthy by resolving the provider's trust chain up to the anchor (⚠️
  this step is skipped in this version).
- **Message 5-7**: The Wallet Instance instantiates a new key pair on its TEE
  and requests a ``nonce`` from the Wallet Provider's backend (as a measure
  against replay attacks).
- **Message 8**: The Wallet Instance generates a Wallet Instance Attestation
  Request (JWT) signed with the private key associated with the public key
  for which it wants to obtain the attestation containing the ``nonce`` and
  other useful parameters.
- **Message 9-13**: The Wallet Instance sends the Wallet Instance Attestation
  Request to the Wallet Provider's backend which verifies its validity and
  issues the signed attestation.
- **Message 13-14**:The Wallet Instance receives the Wallet Instance
  attestation signed by the Wallet Provider and proceeds with a formal
  verification.
- **Message 15**:The Wallet Instance Attestation is ready to be consumed.


Detail design
---------------

Format of the Wallet Instance Attestation Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To obtain a Wallet Instance Attestation from the wallet
provider (backend) it is necessary to send a Wallet Instance Attestation
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
+---------+--------------------------------------------+
| **key** | **value**                                  |
+---------+--------------------------------------------+
|| iss    || The public URL of the issuer              |
||        || concatenated with the thumbprint          |
||        || of the JWK of the Wallet Instance         |
||        || for which the attestation is              |
||        || being requested.                          |
+---------+--------------------------------------------+
|| sub    || The public url of the Wallet              |
||        || Instance attestation issuer.              |
+---------+--------------------------------------------+
|| jti    || Unique identifier of the request.         |
||        || This parameter will be used to            |
||        || avoid replay attacks.                     |
+---------+--------------------------------------------+
| type    | WalletInstanceAttestationRequest           |
+---------+--------------------------------------------+
|| cnf    || This parameter will contain the           |
||        || configuration of the wallet               |
||        || instance in JSON format. Among            |
||        || the mandatory attributes there            |
||        || will be the jwk parameter                 |
||        || containing the public key of the          |
||        || Wallet Instance. It will also             |
||        || contain all the information               |
||        || useful for the Wallet Provider            |
||        || backend to verify that the app is genuine.|
+---------+--------------------------------------------+

Non-normative example
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

  {
    "alg": "ES256",
    "kid": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "typ": "var+jwt"
  }
  .
  {
    "iss": "https://wallet-provider.example.org/instance/vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "sub": "https://wallet-provider.example.org/",
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

Whose corresponding JWS is as follows:

.. code-block:: javascript

  eyJhbGciOiJFUzI1NiIsImtpZCI6InZiZVhKa3NNNDV4cGh0QU5uQ2lHNm1DeXVVNGpmR056b3BHdUt2b2dnOWMiLCJ0eXAiOiJ2YXIrand0In0.eyJpc3MiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZy9pbnN0YW5jZS92YmVYSmtzTTQ1eHBodEFObkNpRzZtQ3l1VTRqZkdOem9wR3VLdm9nZzljIiwic3ViIjoiaHR0cHM6Ly93YWxsZXQtcHJvdmlkZXIuZXhhbXBsZS5vcmcvIiwianRpIjoiMzhjZTczMDUtMWEyYi00MTc1LWJkOGUtZmRjNTY0ZDZkYzVlIiwidHlwZSI6IldhbGxldEluc3RhbmNlQXR0ZXN0YXRpb25SZXF1ZXN0IiwiY25mIjp7Imp3ayI6eyJjcnYiOiJQLTI1NiIsImt0eSI6IkVDIiwieCI6IjRITnB0SS14cjJwanlSSktHTW56NFdtZG5RRF91SlNxNFI5NU5qOThiNDQiLCJ5IjoiTElablNCMzl2RkpoWWdTM2s3alhFNHIzLUNvR0ZRd1p0UEJJUnFwTmxyZyIsImtpZCI6InZiZVhKa3NNNDV4cGh0QU5uQ2lHNm1DeXVVNGpmR056b3BHdUt2b2dnOWMifX0sImlhdCI6MTY4Nzc5MjE3NywiZXhwIjoxNjg3Nzk5Mzc3fQ.t3HL_nrqe_3L8C1XrtgEFdb8M2q1_Nmwa-Ij6vL2digbu34JF2N5GB3dc_XIRPjZbG7BeQJOW6OZ1sSiWJWgjA

Verifiable through the public key of the Wallet Instance present in the JWT.


Format of the Wallet Instance Attestation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure the above requirements, a JWT was chosen as the format for the
Wallet Instance Attestation. Let's see below the various fields that
compose it.

Header
^^^^^^

+-----------------------------------+-----------------------------------+
| **key**                           | **value**                         |
+-----------------------------------+-----------------------------------+
| alg                               | Algorithm to verify the token     |
|                                   | signature (es. ES256).            |
+-----------------------------------+-----------------------------------+
| kid                               | Key id used by the wallet         |
|                                   | provider to sign the attestation. |
+-----------------------------------+-----------------------------------+
| type                              | Media type, in this case we use   |
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
| trust_chain                       | | Array containing the JWS of the |
|                                   |   trust chain relating to its     |
|                                   |   issuer (Wallet Provider).       |
+-----------------------------------+-----------------------------------+

Payload
^^^^^^^

+---------------------------+-------------------------------------------+
| **key**                   | **value**                                 |
+---------------------------+-------------------------------------------+
|| iss                      || The public url of the Wallet             |
||                          || Instance attestation issuer. (see        |
||                          || example below)                           |
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
| logo_uri                  | Logo url of the Wallet Provider.          |
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
||                          || ecessary for the holder binding.         |
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
||                          || supported algoithms array                |
+---------------------------+-------------------------------------------+
|| request_object_signing   || JSON array containing a list of the      |
|| _alg_values_supported    || JWS signing algorithms (alg values)      |
||                          || supported by the OP for Request Objects  |
+---------------------------+-------------------------------------------+
|| presentation_definition  || Boolean value specifying whether the OP  |
|| _uri_supported           || supports the transfer of                 |
||                          || presentation_definition by               |
||                          || reference, with true indicating support. |
+---------------------------+-------------------------------------------+

Signature
^^^^^^^^^

The JWT (Wallet Instance Attestation) thus composed is signed using the
private key of the Wallet Provider present to which the Wallet Provider's
backend has access.

Non-normative example
^^^^^^^^^^^^^^^^^^^^^
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
    "x5c": ["MIIBjDCCATGgAwIBAgIUZiFoj7bvmhTQvDQtCOY19fMVq/gwCgYIKoZIzj0EAwIwGzEZMBcGA1UEAwwQd2FsbGV0Lml0YWxpYS5pdDAeFw0yMzA2MTMxNDI1NDRaFw0yNjAzMDkxNDI1NDRaMBsxGTAXBgNVBAMMEHdhbGxldC5pdGFsaWEuaXQwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASqsmuPcB/8Hnuxs4hGtwEztuvvA5zzKePuUcU9N599SdR9HFg8hoL1PMPpDylP8cnDglDU9qNG8LJSELZz1Oojo1MwUTAdBgNVHQ4EFgQUj5fkXeflngzbABlwT6ra1bOQ11cwHwYDVR0jBBgwFoAUj5fkXeflngzbABlwT6ra1bOQ11cwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNJADBGAiEA+avjz/CVnxq+50iAxKLjyRvK/W9XgCp6cKDXs7Y4tugCIQDMWGYL0adwYKhKitYsk8HRIKFDGOZmqZFI35XFehgKQA=="]
  }
  .
  {
    "iss": "https://wallet-provider.example.org",
    "sub": "https://wallet-provider.example.org/instance/vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
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


Whose corresponding JWS is as follows:

.. code-block:: javascript

  eyJhbGciOiJFUzI1NiIsImtpZCI6IjV0NVlZcEJoTi1FZ0lFRUk1aVV6cjZyME1SMDJMblZRME9tZWttTktjalkiLCJ0cnVzdF9jaGFpbiI6WyJleUpoYkdjaU9pSkZVekkxTmlJc0luUjVjQ0k2SW1Gd2NHeHBZMkYwYVc5dUwyVnVkR2wwZVMxemRHRjBaVzFsYm5RcmFuZDBJbjAuZXlKcGMzTWlPaUpvZEhSd2N6b3ZMM2RoYkd4bGRDNXBkR0ZzYVdFdWFYUWlMQ0p6ZFdJaU9pSm9kSFJ3Y3pvdkwzZGhiR3hsZEM1cGRHRnNhV0V1YVhRaUxDSnFkMnR6SWpwN0ltdGxlWE1pT2x0N0ltdDBlU0k2SWtWRElpd2lZM0oySWpvaVVDMHlOVFlpTENKNElqb2ljWEpLY21velFXWmZRalUzYzJKUFNWSnlZMEpOTjJKeU4zZFBZemg1Ym1vM2JFaEdVRlJsWm1aVmF5SXNJbmtpT2lJeFNEQmpWMFI1UjJkMlZUaDNMV3RRUzFWZmVIbGpUME5WVGxReWJ6QmlkM05zU1ZGMGJsQlZObWxOSW4xZGZTd2liV1YwWVdSaGRHRWlPbnNpWlhWa2FWOTNZV3hzWlhSZmNISnZkbWxrWlhJaU9uc2lhbmRyY3lJNmV5SnJaWGx6SWpwYmV5SnJkSGtpT2lKRlF5SXNJbU55ZGlJNklsQXRNalUySWl3aWVDSTZJbkZ5U25KcU0wRm1YMEkxTjNOaVQwbFNjbU5DVFRkaWNqZDNUMk00ZVc1cU4yeElSbEJVWldabVZXc2lMQ0o1SWpvaU1VZ3dZMWRFZVVkbmRsVTRkeTFyVUV0VlgzaDVZMDlEVlU1VU1tOHdZbmR6YkVsUmRHNVFWVFpwVFNKOVhYMHNJblJ2YTJWdVgyVnVaSEJ2YVc1MElqb2lhSFIwY0hNNkx5OTNZV3hzWlhRdWFYUmhiR2xoTG1sMEwzUnZhMlZ1SWl3aVlYTmpYM1poYkhWbGMxOXpkWEJ3YjNKMFpXUWlPbHNpYUhSMGNITTZMeTkzWVd4c1pYUXVhWFJoYkdsaExtbDBMMHh2UVM5aVlYTnBZeUlzSW1oMGRIQnpPaTh2ZDJGc2JHVjBMbWwwWVd4cFlTNXBkQzlNYjBFdmJXVmthWFZ0SWl3aWFIUjBjSE02THk5M1lXeHNaWFF1YVhSaGJHbGhMbWwwTDB4dlFTOW9hV2RvSWwwc0ltZHlZVzUwWDNSNWNHVnpYM04xY0hCdmNuUmxaQ0k2V3lKMWNtNDZhV1YwWmpwd1lYSmhiWE02YjJGMWRHZzZZMnhwWlc1MExXRnpjMlZ5ZEdsdmJpMTBlWEJsT21wM2RDMXJaWGt0WVhSMFpYTjBZWFJwYjI0aVhTd2lkRzlyWlc1ZlpXNWtjRzlwYm5SZllYVjBhRjl0WlhSb2IyUnpYM04xY0hCdmNuUmxaQ0k2V3lKd2NtbDJZWFJsWDJ0bGVWOXFkM1FpWFN3aWRHOXJaVzVmWlc1a2NHOXBiblJmWVhWMGFGOXphV2R1YVc1blgyRnNaMTkyWVd4MVpYTmZjM1Z3Y0c5eWRHVmtJanBiSWtWVE1qVTJJaXdpUlZNek9EUWlMQ0pGVXpVeE1pSmRmU3dpWm1Wa1pYSmhkR2x2Ymw5bGJuUnBkSGtpT25zaWIzSm5ZVzVwZW1GMGFXOXVYMjVoYldVaU9pSlFZV2R2VUdFZ1V5NXdMa0V1SWl3aWFHOXRaWEJoWjJWZmRYSnBJam9pYUhSMGNITTZMeTkzWVd4c1pYUXVhWFJoYkdsaExtbDBJaXdpY0c5c2FXTjVYM1Z5YVNJNkltaDBkSEJ6T2k4dmQyRnNiR1YwTG1sMFlXeHBZUzVwZEM5d2NtbDJZV041WDNCdmJHbGplU0lzSW5SdmMxOTFjbWtpT2lKb2RIUndjem92TDNkaGJHeGxkQzVwZEdGc2FXRXVhWFF2YVc1bWIxOXdiMnhwWTNraUxDSnNiMmR2WDNWeWFTSTZJbWgwZEhCek9pOHZkMkZzYkdWMExtbDBZV3hwWVM1cGRDOXNiMmR2TG5OMlp5SjlmU3dpYVdGMElqb3hOamczTWpneE1EQXpMQ0psZUhBaU9qRTNNRGt6T1RrME1ETjkuUHFIbzBpMklGZUhBTkxpQlBnZmRuaElfS0xGTGplV2xRVVhGandBcHRDRERfcTlhUkJxNjJPTEF5U081OUZqZ0kwWGNwSlUyaDBMTTBHRjdkM1lpU1EiLCJleUpoYkdjaU9pSkZVekkxTmlJc0ltdHBaQ0k2SWxaSGVFdGhNVnBIWW10ak1GUXdiRFJsYlRsVFdsVXhWV0pJVmxsU01uQkhZVVpTUldSWGNESmhiRlpzWkVkNFIwOVdXakpTYTJ4NFkzY2lMQ0owZVhBaU9pSmhjSEJzYVdOaGRHbHZiaTlsYm5ScGRIa3RjM1JoZEdWdFpXNTBLMnAzZENKOS5leUpsZUhBaU9qRTJORGsyTWpNMU5EWXNJbWxoZENJNk1UWTBPVFExTURjME5pd2lhWE56SWpvaWFIUjBjSE02THk5cGJuUmxjbTFsWkdsaGRHVXVaV2xrWVhNdVpYaGhiWEJzWlM1dmNtY2lMQ0p6ZFdJaU9pSm9kSFJ3Y3pvdkwzSndMbVY0WVcxd2JHVXViM0puSWl3aWFuZHJjeUk2ZXlKclpYbHpJanBiZXlKcmRIa2lPaUpGUXlJc0ltdHBaQ0k2SWxaSGVFdGhNVnBIWW10ak1GUXdiRFJsYlRsVFdsVXhWV0pJVmxsU01uQkhZVVpTUldSWGNESmhiRlpzWkVkNFIwOVdXakpTYTJ4NFkzY2lMQ0pqY25ZaU9pSlFMVEkxTmlJc0luZ2lPaUpTY1ZsNU1qTnViVTV2T1VZekxVVXRjVFZoUVZwVVVDMVFZa1ozWmtsYVZWZGplSGhwWjFKS05UYzBJaXdpZVNJNklrZDFWRE5DTW5kNk0yNUNjVXBOZERoaU9HeFlWbTlTYjNZeldsVnNVM0YxTmw5c0xWQmFhRzVrUm5NaWZWMTlMQ0p0WlhSaFpHRjBZVjl3YjJ4cFkza2lPbnNpYjNCbGJtbGtYM0psYkhscGJtZGZjR0Z5ZEhraU9uc2ljMk52Y0dWeklqcDdJbk4xWW5ObGRGOXZaaUk2V3lKbGRTNWxkWEp2Y0dFdVpXTXVaWFZrYVhjdWNHbGtMakVzSUNCbGRTNWxkWEp2Y0dFdVpXTXVaWFZrYVhjdWNHbGtMbWwwTGpFaVhYMHNJbkpsY1hWbGMzUmZZWFYwYUdWdWRHbGpZWFJwYjI1ZmJXVjBhRzlrYzE5emRYQndiM0owWldRaU9uc2liMjVsWDI5bUlqcGJJbkpsY1hWbGMzUmZiMkpxWldOMElsMTlMQ0p5WlhGMVpYTjBYMkYxZEdobGJuUnBZMkYwYVc5dVgzTnBaMjVwYm1kZllXeG5YM1poYkhWbGMxOXpkWEJ3YjNKMFpXUWlPbnNpYzNWaWMyVjBYMjltSWpwYklsSlRNalUySWl3aVVsTTFNVElpTENKRlV6STFOaUlzSWtWVE5URXlJaXdpVUZNeU5UWWlMQ0pRVXpVeE1pSmRmWDE5TENKMGNuVnpkRjl0WVhKcmN5STZXM3NpYVdRaU9pSm9kSFJ3Y3pvdkwzUnlkWE4wTFdGdVkyaHZjaTVsZUdGdGNHeGxMbVYxTDI5d1pXNXBaRjl5Wld4NWFXNW5YM0JoY25SNUwzQjFZbXhwWXk4aUxDSjBjblZ6ZEY5dFlYSnJJam9pWlhsS2FHSWdYSFV5TURJMkluMWRmUS5OdWE5TFFqNmt6UnN2ZzFUQ2l1TzVmcjhQT0ZMeUUzUURaWXBTRzZxMW9vRG8zNUlsUi1FcGRyZ25tamdoZUVLakxPcGEtTWxnQjBjU0hFUXFFaDFLZyIsImV5SmhiR2NpT2lKRlV6STFOaUlzSW10cFpDSTZJbVZGU21aYU1rbDVVekZrWm1GSWNHdFdNVnAyVjFWb1VtTnJjRE5STVZWNFVrWm9VbGRGUmpaVVZHc3lUakZPU1U1VVp6UlVSamxwVTFFaUxDSjBlWEFpT2lKaGNIQnNhV05oZEdsdmJpOWxiblJwZEhrdGMzUmhkR1Z0Wlc1MEsycDNkQ0o5LmV5SmxlSEFpT2pFMk5EazJNak0xTkRZc0ltbGhkQ0k2TVRZME9UUTFNRGMwTml3aWFYTnpJam9pYUhSMGNITTZMeTkwY25WemRDMWhibU5vYjNJdVpYaGhiWEJzWlM1bGRTSXNJbk4xWWlJNkltaDBkSEJ6T2k4dmFXNTBaWEp0WldScFlYUmxMbVZwWkdGekxtVjRZVzF3YkdVdWIzSm5JaXdpYW5kcmN5STZleUpyWlhseklqcGJleUpyZEhraU9pSkZReUlzSW10cFpDSTZJbFpIZUV0aE1WcEhZbXRqTUZRd2JEUmxiVGxUV2xVeFZXSklWbGxTTW5CSFlVWlNSV1JYY0RKaGJGWnNaRWQ0UjA5V1dqSlNhMng0WTNjaUxDSmpjbllpT2lKUUxUSTFOaUlzSW5naU9pSlNjVmw1TWpOdWJVNXZPVVl6TFVVdGNUVmhRVnBVVUMxUVlrWjNaa2xhVlZkamVIaHBaMUpLTlRjMElpd2llU0k2SWtkMVZETkNNbmQ2TTI1Q2NVcE5kRGhpT0d4WVZtOVNiM1l6V2xWc1UzRjFObDlzTFZCYWFHNWtSbk1pZlYxOUxDSjBjblZ6ZEY5dFlYSnJjeUk2VzNzaWFXUWlPaUpvZEhSd2N6b3ZMM1J5ZFhOMExXRnVZMmh2Y2k1bGVHRnRjR3hsTG1WMUwyWmxaR1Z5WVhScGIyNWZaVzUwYVhSNUwzUm9ZWFF0Y0hKdlptbHNaU0lzSW5SeWRYTjBYMjFoY21zaU9pSmxlVXBvWWlCY2RUSXdNallpZlYxOS5qaWVHQWhwcVNuWEtMeldCYy11N0N4QzFkNkFxQVFiMkNNYUF5ZElTc3B3aVlPWmhPOGI0b1dGdzVLaVotblYtbC1EajVwU0FDa3lXY0xXSzV3eHFvdyJdLCJ0eXAiOiJ2YStqd3QiLCJ4NWMiOlsiTUlJQmpEQ0NBVEdnQXdJQkFnSVVaaUZvajdidm1oVFF2RFF0Q09ZMTlmTVZxL2d3Q2dZSUtvWkl6ajBFQXdJd0d6RVpNQmNHQTFVRUF3d1FkMkZzYkdWMExtbDBZV3hwWVM1cGREQWVGdzB5TXpBMk1UTXhOREkxTkRSYUZ3MHlOakF6TURreE5ESTFORFJhTUJzeEdUQVhCZ05WQkFNTUVIZGhiR3hsZEM1cGRHRnNhV0V1YVhRd1dUQVRCZ2NxaGtqT1BRSUJCZ2dxaGtqT1BRTUJCd05DQUFTcXNtdVBjQi84SG51eHM0aEd0d0V6dHV2dkE1enpLZVB1VWNVOU41OTlTZFI5SEZnOGhvTDFQTVBwRHlsUDhjbkRnbERVOXFORzhMSlNFTFp6MU9vam8xTXdVVEFkQmdOVkhRNEVGZ1FVajVma1hlZmxuZ3piQUJsd1Q2cmExYk9RMTFjd0h3WURWUjBqQkJnd0ZvQVVqNWZrWGVmbG5nemJBQmx3VDZyYTFiT1ExMWN3RHdZRFZSMFRBUUgvQkFVd0F3RUIvekFLQmdncWhrak9QUVFEQWdOSkFEQkdBaUVBK2F2anovQ1ZueHErNTBpQXhLTGp5UnZLL1c5WGdDcDZjS0RYczdZNHR1Z0NJUURNV0dZTDBhZHdZS2hLaXRZc2s4SFJJS0ZER09abXFaRkkzNVhGZWhnS1FBPT0iXX0.eyJpc3MiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZyIsInN1YiI6Imh0dHBzOi8vd2FsbGV0LXByb3ZpZGVyLmV4YW1wbGUub3JnL2luc3RhbmNlL3ZiZVhKa3NNNDV4cGh0QU5uQ2lHNm1DeXVVNGpmR056b3BHdUt2b2dnOWMiLCJ0eXBlIjoiV2FsbGV0SW5zdGFuY2VBdHRlc3RhdGlvbiIsInBvbGljeV91cmkiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZy9wcml2YWN5X3BvbGljeSIsInRvc191cmkiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZy9pbmZvX3BvbGljeSIsImxvZ29fdXJpIjoiaHR0cHM6Ly93YWxsZXQtcHJvdmlkZXIuZXhhbXBsZS5vcmcvbG9nby5zdmciLCJhc2MiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZy9Mb0EvYmFzaWMiLCJjbmYiOnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoiNEhOcHRJLXhyMnBqeVJKS0dNbno0V21kblFEX3VKU3E0Ujk1Tmo5OGI0NCIsInkiOiJMSVpuU0IzOXZGSmhZZ1MzazdqWEU0cjMtQ29HRlF3WnRQQklScXBObHJnIiwia2lkIjoidmJlWEprc000NXhwaHRBTm5DaUc2bUN5dVU0amZHTnpvcEd1S3ZvZ2c5YyJ9fSwiYXV0aG9yaXphdGlvbl9lbmRwb2ludCI6ImV1ZGl3OiIsInJlc3BvbnNlX3R5cGVzX3N1cHBvcnRlZCI6WyJ2cF90b2tlbiJdLCJ2cF9mb3JtYXRzX3N1cHBvcnRlZCI6eyJqd3RfdnBfanNvbiI6eyJhbGdfdmFsdWVzX3N1cHBvcnRlZCI6WyJFUzI1NiJdfSwiand0X3ZjX2pzb24iOnsiYWxnX3ZhbHVlc19zdXBwb3J0ZWQiOlsiRVMyNTYiXX19LCJyZXF1ZXN0X29iamVjdF9zaWduaW5nX2FsZ192YWx1ZXNfc3VwcG9ydGVkIjpbIkVTMjU2Il0sInByZXNlbnRhdGlvbl9kZWZpbml0aW9uX3VyaV9zdXBwb3J0ZWQiOmZhbHNlLCJpYXQiOjE2ODc3OTIxNzcsImV4cCI6MTY4Nzc5OTM3N30.RHSJ_-xKa43HqgN155yqfxJ0Tp6sTE34yJX6KQuvpuOsASYXnE880q_nlI2lrjDeD9lvP3_5Q9UPodZlxMsy4A

Verifiable through the following public key (Wallet Provider Public Key)
obtained within the Entity Configuration of the Wallet Provider,
attested in the related trust chain.

.. code-block:: javascript

  {
  "kty": "EC",
  "x": "qrJrj3Af_B57sbOIRrcBM7br7wOc8ynj7lHFPTeffUk",
  "y": "1H0cWDyGgvU8w-kPKU_xycOCUNT2o0bwslIQtnPU6iM",
  "crv": "P-256"
  }


Format of the Wallet Provider Entity Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Wallet Provider Entity Configuration is a JWS containing
the public keys and the supported algorithms
within the Wallet Provider metadata definition.
It broadly implements ``OIDC-FED`` protocol.

Header
^^^^^^
+---------+-----------------------------------------------------------------+
| **key** | **value**                                                       |
+---------+-----------------------------------------------------------------+
| alg     | Algorithm to verify the token signature (es. ES256).            |
+---------+-----------------------------------------------------------------+
| kid     | Thumbprint of the public key used for signing.                  |
+---------+-----------------------------------------------------------------+
| type    | Media type, in this case, we use the entity-statement+jwt value.|
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
|                                   | configuration. In our case we     |
|                                   | will have for now the wallet      |
|                                   | provider entity contained within  |
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
||                                   || the proof that the wallet         |
||                                   || instance is able to send to the   |
||                                   || Wallet Provider.                  |
||                                   || ⚠️ This parameter is not standard |
||                                   || and is still under discussion.    |
+------------------------------------+------------------------------------+
|| grant_types_supported             || The type of grants supported by   |
||                                   || the endpoint token. Therefore,    |
||                                   || for the Wallet Provider the token |
||                                   || is equivalent only to the wallet  |
||                                   || instance attestation, therefore   |
||                                   || this attribute will contain an    |
||                                   || array with only one element:      |
||                                   || client-assertion-type:            |
||                                   || ``jwt-key-attestation``.          |
+------------------------------------+------------------------------------+
|| token_endpoint_auth_methods_suppo || Supported authentication method   |
|| rted                              || for the endpoint token. In our    |
||                                   ||                                   |
+------------------------------------+------------------------------------+
|| token_endpoint_auth_signing_alg_v || List of supported signature       |
|| alues_supported                   || algorithms.                       |
+------------------------------------+------------------------------------+

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

Non-normative example
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

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

Whose corresponding JWS is as follows:

.. code-block:: javascript

  eyJhbGciOiJFUzI1NiIsImtpZCI6IjV0NVlZcEJoTi1FZ0lFRUk1aVV6cjZyME1SMDJMblZRME9tZWttTktjalkiLCJ0eXAiOiJlbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZyIsInN1YiI6Imh0dHBzOi8vd2FsbGV0LXByb3ZpZGVyLmV4YW1wbGUub3JnIiwiandrcyI6eyJrZXlzIjpbeyJjcnYiOiJQLTI1NiIsImt0eSI6IkVDIiwieCI6InFySnJqM0FmX0I1N3NiT0lScmNCTTdicjd3T2M4eW5qN2xIRlBUZWZmVWsiLCJ5IjoiMUgwY1dEeUdndlU4dy1rUEtVX3h5Y09DVU5UMm8wYndzbElRdG5QVTZpTSIsImtpZCI6IjV0NVlZcEJoTi1FZ0lFRUk1aVV6cjZyME1SMDJMblZRME9tZWttTktjalkifV19LCJtZXRhZGF0YSI6eyJldWRpX3dhbGxldF9wcm92aWRlciI6eyJqd2tzIjp7ImtleXMiOlt7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoicXJKcmozQWZfQjU3c2JPSVJyY0JNN2JyN3dPYzh5bmo3bEhGUFRlZmZVayIsInkiOiIxSDBjV0R5R2d2VTh3LWtQS1VfeHljT0NVTlQybzBid3NsSVF0blBVNmlNIiwia2lkIjoiNXQ1WVlwQmhOLUVnSUVFSTVpVXpyNnIwTVIwMkxuVlEwT21la21OS2NqWSJ9XX0sInRva2VuX2VuZHBvaW50IjoiaHR0cHM6Ly93YWxsZXQtcHJvdmlkZXIuZXhhbXBsZS5vcmcvdG9rZW4iLCJhc2NfdmFsdWVzX3N1cHBvcnRlZCI6WyJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZy9Mb0EvYmFzaWMiLCJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZy9Mb0EvbWVkaXVtIiwiaHR0cHM6Ly93YWxsZXQtcHJvdmlkZXIuZXhhbXBsZS5vcmcvTG9BL2hpZ2giXSwiZ3JhbnRfdHlwZXNfc3VwcG9ydGVkIjpbInVybjppZXRmOnBhcmFtczpvYXV0aDpjbGllbnQtYXNzZXJ0aW9uLXR5cGU6and0LWtleS1hdHRlc3RhdGlvbiJdLCJ0b2tlbl9lbmRwb2ludF9hdXRoX21ldGhvZHNfc3VwcG9ydGVkIjpbInByaXZhdGVfa2V5X2p3dCJdLCJ0b2tlbl9lbmRwb2ludF9hdXRoX3NpZ25pbmdfYWxnX3ZhbHVlc19zdXBwb3J0ZWQiOlsiRVMyNTYiLCJFUzM4NCIsIkVTNTEyIl19LCJmZWRlcmF0aW9uX2VudGl0eSI6eyJvcmdhbml6YXRpb25fbmFtZSI6IlBhZ29QYSBTLnAuQS4iLCJob21lcGFnZV91cmkiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZyIsInBvbGljeV91cmkiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZy9wcml2YWN5X3BvbGljeSIsInRvc191cmkiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZy9pbmZvX3BvbGljeSIsImxvZ29fdXJpIjoiaHR0cHM6Ly93YWxsZXQtcHJvdmlkZXIuZXhhbXBsZS5vcmcvbG9nby5zdmcifX0sImlhdCI6MTY4Nzc5MjE3NywiZXhwIjoxNzA5OTEwNTc3fQ.hGG7WvGdP1jXO39WZ5WxnN62MLI4XsW2Wr4a809MoRqNTlW6DjzKJotk2SpT2Xq6qcxcctTFnmEMYUuRrJRnXA

Verifiable through the public key of the Wallet Provider itself.

Endpoints
~~~~~~~~~
The Wallet Provider's backend that issues the Wallet Instance Attestations must
make available a series of APIs in REST format that follow the OpenId
Federation standard.

Metadata
^^^^^^^^
A **GET /.well-known/openid-federation endpoint** for retrieving the Wallet
Provider Entity Configuration

Wallet Instance Attestation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

A second **POST /token** endpoint that takes two parameters as input:

``grant_type`` which in our case is a string:
``urn:ietf:params:oauth:client-assertion-type:jwt-key-attestation``

``assertion``` which contains the signed JWT of the Wallet Instance Attestation
Request

The response will then contain the Wallet Instance Attestation
