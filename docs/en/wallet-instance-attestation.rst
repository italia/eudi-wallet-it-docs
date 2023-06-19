.. include:: ../common/common_definitions.rst

.. _wallet-instance-attestation.rst:

Wallet Instance Attestation
+++++++++++++++++++++++++++++++

Inside a **wallet solution** and, especially with regards
to the **wallet instance**, it is essential to ensure the **authenticity,
integrity, security, privacy and trust** in the use of the latter both
by the user and the services connected to it, such as the
**PID Provider** or one **relying party**.


General Properties
------------------

The goal is:

- Ensure that the wallet instance maintains a level of **integrity**,
  capable of preventing any attempts of manipulation or forgery
  by unauthorized third parties.
- Make sure the private keys have been generated and stored securely
  within a **trusted execution environment** (TEE).
- Verify that the wallet instance is **authentic**, i.e. made available
  by an accredited body that complies with the trust model.

To guarantee the above, it is necessary for each
wallet instance to issue a certificate of conformity,
guaranteeing its security and compliance with the trust model.

This attestation is called **Wallet Instance Attestation**
and must be electronically signed by its issuer.

.. hint::
  Considering that the wallet instance does not represent an accredited
  entity and does not belong to an organization,
  but resides on the user's device, the trust model,
  based on sustainability and scalability criteria,
  must delegate to the **Wallet provider** the task of
  issuing the **Wallet Instance Attestation**.


Requirements
------------

We assume the following requirements for the Wallet Instance Attestation:

1. **Efficiency**: The Wallet Instance Attestation should use an efficient
   format such as JSON Web Token (JWT) to ensure light and fast data management
   and be compliant with the various formats used for EUDIW solutions.
2. **Simplicity**: The Wallet Provider should be based on a REST architecture
   for issuing Wallet Instance Attestations.
3. **Public key holder binding**: The Wallet Instance Attestation must be
   securely linked to the Wallet Instance public key.
4. **Issued and signed by an accredited Wallet Provider**:
   The Wallet Instance Attestation must be issued and signed by an accredited
   and reliable Wallet Provider, thus conferring integrity and authenticity
   to the attestation itself.
5. **Authenticity/Genuineness of the wallet instance**:
   The Wallet Instance Attestation must guarantee the integrity
   and authenticity of the wallet instance, confirming that it was
   created and provided correctly by the Wallet Provider. ⚠️
6. **Ability to request multiple claims for several public keys**:
   Each single wallet instance should be able to request multiple attestations
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
9.  **Disability in case of loss/deletion of the public key**:
    If the public key associated with the wallet instance is lost or deleted,
    the attestation automatically becomes invalid to prevent unauthorized
    use of the wallet instance. ⚠️
10. **Pseudonymisation**:
    The attestations are designed to be pseudonymised
    (i.e. they do not contain direct references to the person, so that it
    is not possible to identify them in the absence of additional information
    \- see art. 4(5) GDPR for a comprehensive definition).
    In the absence of such a measure, the use of the attestation on multiple
    RPs would constitute an appreciable risk, as it would theoretically
    allow the RPs to merge databases and track users.
    This requirement enriches the measures adopted in accordance
    with art. 32 GDPR.

.. attention::
  ⚠️ Implementation of points no. 5 and 9 is still under discussion.
  This version assumes the authenticity and non-revocability of the wallet instance.



High-end design
---------------


Static view of the components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://www.plantuml.com/plantuml/svg/XP4nJuSm44VtVehBdxbnPp2iRYx6qTHIjR7SaVQ0-EqzaICDgN4ZBxpqzTUXiCkyJCaupvJXzbH2le4hiCW7A7rsAGM6ETCQn-E7RMSloi0OJzDC691FeL1QE1BMWZBeraW2Mbv4wK8VQayPT5yX9TgCQPclpdy676lnGF0ZN93DyVs3xVsrhOU70hCi0_JshwHXFJp-Rg4dIuECo96moD7xeBQbUKBEbE0EPEwuEWx6N2zj_uXqU8wbhVMhD3tjbAX1BYIl_mq0
   :name: wallet solution schema
   :alt: the image shows how the Wallet Provider's backend and the
         wallet instances are contained within the wallet
         solution which is managed by the Wallet Provider

`PlantUML <https://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000>`__


Dynamic view of the components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We do not go into the details of the Wallet Provider's backend as it will be the
subject of a subsequent design review. For now, we will just analyze the
format of the Wallet Instance Attestation and how it is issued by the
Wallet Provider's backend.

.. figure:: https://www.plantuml.com/plantuml/svg/XPB1RjH038RlynIc9v1OSU-XAk9GWSG50RtqucH-HLOJJ_1u6csVdcbsTqG85LVxy-VypjncP_CoZU7DR3nCJ8xqJ6u5WOidBLC72s6kbFGoipfT_SYmA-9CPLk_vt64qsUjKksn8elya-cuVuJ64zA5KEXmKzdhEYmkFCepQ3cXSjOzQ38o_2h8_c4sP5HVRuZGbuaS5ZdSBDqrtS4lixEb9uamck0SsJaitQ5ITT7NSuNwfCwYeiCVDlBZZFoU7d5STufXWdgjGEESHFsyhvf-yYZLXDrIjvATHibUsKl0EoYiqgjwPh4SGbDzChoq_ZeaVSmPvfAKlftoqvVxxu5xbwTrRxV9per--r_HktgGTNANGYup0xI8Gf7p7iuoA7injDPmoSSQr_PEsBwl_OpN0--F_BejOdkHwYvDtNXf3om-g87ZaJnHwfn5IR5idjGjD9Pf_0q0
   :name: sequence diagram for Wallet Instance Attestation request
   :alt: The figure shows the sequence diagram for issuing a Wallet Instance Attestation.
         The steps will be described below.

`PlantUML <https://www.plantuml.com/plantuml/uml/XPB1RjH038RlynIc9v1OSU-XAk9GWSG50RtqucH-HLOJJ_1u6csVdcbsTqG85LVxy-VypjncP_CoZU7DR3nCJ8xqJ6u5WOidBLC72s6kbFGoipfT_SYmA-9CPLk_vt64qsUjKksn8elya-cuVuJ64zA5KEXmKzdhEYmkFCepQ3cXSjOzQ38o_2h8_c4sP5HVRuZGbuaS5ZdSBDqrtS4lixEb9uamck0SsJaitQ5ITT7NSuNwfCwYeiCVDlBZZFoU7d5STufXWdgjGEESHFsyhvf-yYZLXDrIjvATHibUsKl0EoYiqgjwPh4SGbDzChoq_ZeaVSmPvfAKlftoqvVxxu5xbwTrRxV9per--r_HktgGTNANGYup0xI8Gf7p7iuoA7injDPmoSSQr_PEsBwl_OpN0--F_BejOdkHwYvDtNXf3om-g87ZaJnHwfn5IR5idjGjD9Pf_0q0>`__

- **Message 1**: The end user initializes the wallet instance.
  In particular, this process happens when the mobile application
  is launched and every time the end user wants to request or present
  (disclose) a credential.
- **Message 2-3**: The wallet instance obtains metadata about its wallet
  provider. Among these, we also find the list of supported algorithms,
  public keys, endpoints.
- **Message 4**: The wallet instance verifies that the Wallet Provider is
  trustworthy by resolving the provider's trust chain up to the anchor (⚠️
  this step is skipped in this version)
- **Message 5-7**: The wallet instance instantiates a new key pair on its TEE
  and requests a nonce from the Wallet Provider's backend (as a measure
  against replay attacks)
- **Message 8**: The wallet instance generates a Wallet Instance Attestation
  Request (JWT) signed with the private key associated with the public key
  for which it wants to obtain the attestation containing the nonce and
  other useful parameters.
- **Message 9-13**: The wallet instance sends the Wallet Instance Attestation
  Request to the Wallet Provider's backend which verifies its validity and
  issues the signed attestation.
- **Message 13-14**:The wallet instance receives the wallet instance
  attestation signed by the Wallet Provider and proceeds with a formal
  verification
- **Message 15**:The Wallet Instance Attestation is ready to be consumed


Detail design
---------------

Format of the Wallet Instance Attestation Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To obtain a Wallet Instance Attestation from the wallet
provider (backend) it is necessary to send a Wallet Instance Attestation
Request from the wallet instance containing the associated public key
and a nonce previously requested to avoid replay attacks.

Header
^^^^^^
+-----------------------------------+-----------------------------------+
| **key**                           | **value**                         |
+-----------------------------------+-----------------------------------+
| alg                               | Algorithm to verify the token     |
|                                   | signature (es. ES256)             |
+-----------------------------------+-----------------------------------+
| kid                               | Key id of the wallet instance     |
+-----------------------------------+-----------------------------------+
| type                              | Media type, in this case, we use  |
|                                   | the value var+jwt (Verifiable     |
|                                   | Assertion Request JWT).           |
+-----------------------------------+-----------------------------------+

Payload
^^^^^^^
+---------+--------------------------------------------+
| **key** | **value**                                  |
+---------+--------------------------------------------+
|| iss    || The public URL of the issuer              |
||        || concatenated with the thumbprint          |
||        || of the JWK of the wallet instance         |
||        || for which the attestation is              |
||        || being requested                           |
+---------+--------------------------------------------+
|| sub    || The public url of the wallet              |
||        || instance attestation issuer.              |
+---------+--------------------------------------------+
|| jti    || Unique identifier of the request.         |
||        || This parameter will be used to            |
||        || avoid replay attacks                      |
+---------+--------------------------------------------+
| type    | WalletInstanceAttestationRequest           |
+---------+--------------------------------------------+
|| cnf    || This parameter will contain the           |
||        || configuration of the wallet               |
||        || instance in JSON format. Among            |
||        || the mandatory attributes there            |
||        || will be the jwk parameter                 |
||        || containing the public key of the          |
||        || wallet instance. It will also             |
||        || contain all the information               |
||        || useful for the Wallet Provider            |
||        || backend to verify that the app is genuine |
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
    "iss": "https://wallet.italia.it/instance/vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "sub": "https://wallet.italia.it/",
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

  eyJhbGciOiJFUzI1NiIsImtpZCI6InZiZVhKa3NNNDV4cGh0QU5uQ2lHNm1DeXVVNGpmR056b3BHdUt2b2dnOWMiLCJ0eXAiOiJ2YXIrand0In0.eyJpc3MiOiJodHRwczovL3dhbGxldC5pdGFsaWEuaXQvaW5zdGFuY2UvdmJlWEprc000NXhwaHRBTm5DaUc2bUN5dVU0amZHTnpvcEd1S3ZvZ2c5YyIsInN1YiI6Imh0dHBzOi8vd2FsbGV0Lml0YWxpYS5pdC8iLCJqdGkiOiI2ZWM2OTMyNC02MGE4LTRlNWItYTY5Ny1hNzY2ZDg1NzkwZWEiLCJ0eXBlIjoiV2FsbGV0SW5zdGFuY2VBdHRlc3RhdGlvblJlcXVlc3QiLCJjbmYiOnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoiNEhOcHRJLXhyMnBqeVJKS0dNbno0V21kblFEX3VKU3E0Ujk1Tmo5OGI0NCIsInkiOiJMSVpuU0IzOXZGSmhZZ1MzazdqWEU0cjMtQ29HRlF3WnRQQklScXBObHJnIiwia2lkIjoidmJlWEprc000NXhwaHRBTm5DaUc2bUN5dVU0amZHTnpvcEd1S3ZvZ2c5YyJ9fSwiaWF0IjoxNjg2NjQ1MTE1LCJleHAiOjE2ODY2NTIzMTV9.3KInOD_N4zh5PmXj9QhS5aIVFF8zxMl6326KxDTAFYMPJbweD2ny95Nk6y_xTCOioail2WHDLpF3Rju16Q7Z7Q

Verifiable through the public key of the wallet instance present in the JWT.


Format of the Wallet Instance Attestation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure the above requirements, a JWT was chosen as the format for the
Wallet Instance Attestation. Let's see below the various fields that
compose it

Header
^^^^^^

+-----------------------------------+-----------------------------------+
| **key**                           | **value**                         |
+-----------------------------------+-----------------------------------+
| alg                               | Algorithm to verify the token     |
|                                   | signature (es. ES256)             |
+-----------------------------------+-----------------------------------+
| kid                               | Key id used by the wallet         |
|                                   | provider to sign the attestation  |
+-----------------------------------+-----------------------------------+
| type                              | Media type, in this case we use   |
|                                   | the value va+jwt (Verifiable      |
|                                   | Assertion JWT).                   |
|                                   | This parameter is currently       |
|                                   | non-standard as it is not yet     |
|                                   | registered as `IANA Media         |
|                                   | Types <https://www.iana.org/assig |
|                                   | nments/media-types/media-types.xh |
|                                   | tml>`__                           |
+-----------------------------------+-----------------------------------+
| x5c                               | Array containing the X.509        |
|                                   | certificate (and the entire chain |
|                                   | of certificates) used to certify  |
|                                   | the public key of the issuer.     |
+-----------------------------------+-----------------------------------+
| trust_chain                       | | Array containing the JWS of the |
|                                   |   trust chain relating to its     |
|                                   |   issuer (Wallet Provider).       |
|                                   | | ⚠️ This topic will be addressed |
|                                   |   at a later stage                |
+-----------------------------------+-----------------------------------+

Payload
^^^^^^^

+-----------------------------------+-----------------------------------+
| **key**                           | **value**                         |
+-----------------------------------+-----------------------------------+
| iss                               | The public url of the wallet      |
|                                   | instance attestation issuer. (see |
|                                   | example below)                    |
+-----------------------------------+-----------------------------------+
| sub                               | The public url of the issuer      |
|                                   | concatenated with the thumbprint  |
|                                   | of the JWK of the wallet instance |
|                                   | for which the attestation is      |
|                                   | being issued                      |
+-----------------------------------+-----------------------------------+
| iat                               | Timestamp of issue of the         |
|                                   | attestation                       |
+-----------------------------------+-----------------------------------+
| exp                               | Attestation expiration timestamp. |
|                                   | A good practice to avoid security |
|                                   | problems is to have a limited     |
|                                   | duration of the attestation.      |
+-----------------------------------+-----------------------------------+
| type                              | String:                           |
|                                   | "WalletInstanceAttestation"       |
+-----------------------------------+-----------------------------------+
| policy_uri                        | Url to the privacy policy         |
|                                   | of the wallet                     |
+-----------------------------------+-----------------------------------+
| tos_uri                           | Url to the terms                  |
|                                   | of use of the Wallet Provider     |
+-----------------------------------+-----------------------------------+
| logo_uri                          | Logo url of the Wallet Provider   |
+-----------------------------------+-----------------------------------+
| asc                               | Attested security context:        |
|                                   | Represents a level of "trust" of  |
|                                   | the service containing a Level Of |
|                                   | Agreement defined in the metadata |
|                                   | of the Wallet Provider            |
+-----------------------------------+-----------------------------------+
| cnf                               | This parameter contains the JSON  |
|                                   | the payload of which is shown     |
|                                   | below                             |
+-----------------------------------+-----------------------------------+

Payload of `cnf`
''''''''''''''''

+-----------------------+-------------------------------------------------+
| **key**               | **value**                                       |
+-----------------------+-------------------------------------------------+
|| jwk                  || The public key of the Wallet                   |
||                      || instance necessary for the                     |
||                      || holder binding                                 |
+-----------------------+-------------------------------------------------+
|| vp_formats_supported || The Verifiable Credential and                  |
||                      || Verifiable Presentation formats                |
||                      || supported by the Wallet                        |
||                      || See paragraph. 8.1 of                          |
||                      || OpenID for Verifiable Presentations - draft 19 |
+-----------------------+-------------------------------------------------+

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
    "trust_chain": [],
    "typ": "va+jwt",
    "x5c": ["MIIBjDCCATGgAwIBAgIUZiFoj7bvmhTQvDQtCOY19fMVq/gwCgYIKoZIzj0EAwIwGzEZMBcGA1UEAwwQd2FsbGV0Lml0YWxpYS5pdDAeFw0yMzA2MTMxNDI1NDRaFw0yNjAzMDkxNDI1NDRaMBsxGTAXBgNVBAMMEHdhbGxldC5pdGFsaWEuaXQwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASqsmuPcB/8Hnuxs4hGtwEztuvvA5zzKePuUcU9N599SdR9HFg8hoL1PMPpDylP8cnDglDU9qNG8LJSELZz1Oojo1MwUTAdBgNVHQ4EFgQUj5fkXeflngzbABlwT6ra1bOQ11cwHwYDVR0jBBgwFoAUj5fkXeflngzbABlwT6ra1bOQ11cwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNJADBGAiEA+avjz/CVnxq+50iAxKLjyRvK/W9XgCp6cKDXs7Y4tugCIQDMWGYL0adwYKhKitYsk8HRIKFDGOZmqZFI35XFehgKQA=="]
  }
  .
  {
    "iss": "https://wallet.italia.it",
    "sub": "https://wallet.italia.it/instance/vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "type": "WalletInstanceAttestation",
    "policy_uri": "https://wallet.italia.it/privacy_policy",
    "tos_uri": "https://wallet.italia.it/info_policy",
    "logo_uri": "https://wallet.italia.it/logo.svg",
    "asc": "https://wallet.italia.it/LoA/basic",
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
      "vp_formats_supported": {
        "jwt_vc_json": {
          "alg_values_supported": ["ES256K", "ES384"],
        },
        "jwt_vp_json": {
          "alg_values_supported": ["ES256K", "EdDSA"],
        },
      },
    "iat": 1686666443,
    "exp": 1686673643
  }


Whose corresponding JWS is as follows:

.. code-block:: javascript

  eyJhbGciOiJFUzI1NiIsImtpZCI6IjV0NVlZcEJoTi1FZ0lFRUk1aVV6cjZyME1SMDJMblZRME9tZWttTktjalkiLCJ0cnVzdF9jaGFpbiI6W10sInR5cCI6InZhK2p3dCIsIng1YyI6WyJNSUlCakRDQ0FUR2dBd0lCQWdJVVppRm9qN2J2bWhUUXZEUXRDT1kxOWZNVnEvZ3dDZ1lJS29aSXpqMEVBd0l3R3pFWk1CY0dBMVVFQXd3UWQyRnNiR1YwTG1sMFlXeHBZUzVwZERBZUZ3MHlNekEyTVRNeE5ESTFORFJhRncweU5qQXpNRGt4TkRJMU5EUmFNQnN4R1RBWEJnTlZCQU1NRUhkaGJHeGxkQzVwZEdGc2FXRXVhWFF3V1RBVEJnY3Foa2pPUFFJQkJnZ3Foa2pPUFFNQkJ3TkNBQVNxc211UGNCLzhIbnV4czRoR3R3RXp0dXZ2QTV6ektlUHVVY1U5TjU5OVNkUjlIRmc4aG9MMVBNUHBEeWxQOGNuRGdsRFU5cU5HOExKU0VMWnoxT29qbzFNd1VUQWRCZ05WSFE0RUZnUVVqNWZrWGVmbG5nemJBQmx3VDZyYTFiT1ExMWN3SHdZRFZSMGpCQmd3Rm9BVWo1ZmtYZWZsbmd6YkFCbHdUNnJhMWJPUTExY3dEd1lEVlIwVEFRSC9CQVV3QXdFQi96QUtCZ2dxaGtqT1BRUURBZ05KQURCR0FpRUErYXZqei9DVm54cSs1MGlBeEtManlSdksvVzlYZ0NwNmNLRFhzN1k0dHVnQ0lRRE1XR1lMMGFkd1lLaEtpdFlzazhIUklLRkRHT1ptcVpGSTM1WEZlaGdLUUE9PSJdfQ.eyJpc3MiOiJodHRwczovL3dhbGxldC5pdGFsaWEuaXQiLCJzdWIiOiJodHRwczovL3dhbGxldC5pdGFsaWEuaXQvaW5zdGFuY2UvdmJlWEprc000NXhwaHRBTm5DaUc2bUN5dVU0amZHTnpvcEd1S3ZvZ2c5YyIsInR5cGUiOiJXYWxsZXRJbnN0YW5jZUF0dGVzdGF0aW9uIiwicG9saWN5X3VyaSI6Imh0dHBzOi8vd2FsbGV0Lml0YWxpYS5pdC9wcml2YWN5X3BvbGljeSIsInRvc191cmkiOiJodHRwczovL3dhbGxldC5pdGFsaWEuaXQvaW5mb19wb2xpY3kiLCJsb2dvX3VyaSI6Imh0dHBzOi8vd2FsbGV0Lml0YWxpYS5pdC9sb2dvLnN2ZyIsImFzYyI6Imh0dHBzOi8vd2FsbGV0Lml0YWxpYS5pdC9Mb0EvYmFzaWMiLCJjbmYiOnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoiNEhOcHRJLXhyMnBqeVJKS0dNbno0V21kblFEX3VKU3E0Ujk1Tmo5OGI0NCIsInkiOiJMSVpuU0IzOXZGSmhZZ1MzazdqWEU0cjMtQ29HRlF3WnRQQklScXBObHJnIiwia2lkIjoidmJlWEprc000NXhwaHRBTm5DaUc2bUN5dVU0amZHTnpvcEd1S3ZvZ2c5YyJ9LCJ2cF9mb3JtYXRzX3N1cHBvcnRlZCI6eyJqd3RfdmNfanNvbiI6eyJhbGdfdmFsdWVzX3N1cHBvcnRlZCI6WyJFUzI1NksiLCJFUzM4NCJdfSwiand0X3ZwX2pzb24iOnsiYWxnX3ZhbHVlc19zdXBwb3J0ZWQiOlsiRVMyNTZLIiwiRWREU0EiXX19fSwiaWF0IjoxNjg3MTYzOTUyLCJleHAiOjE2ODcxNzExNTJ9.piIg2QCRNG4sXsjdX1Q7oOQYL1f2urzE46CPiDUpdiGn0BmQ64DdL_mQUgCTS9rifgQB27qtG1mmklXYM8Hmpg

Verifiable through the following public key (Wallet Provider Public Key)
obtained within the Entity Configuration of the Wallet Provider,
attested in the related Trust Chain

.. code-block:: javascript

  {
  "kty": "EC",
  "x": "qrJrj3Af_B57sbOIRrcBM7br7wOc8ynj7lHFPTeffUk",
  "y": "1H0cWDyGgvU8w-kPKU_xycOCUNT2o0bwslIQtnPU6iM",
  "crv": "P-256"
  }


Format of the Wallet Provider Entity Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Wallet Provider Entity Configuration is a JWT containing all the metadata
relating to the Wallet Provider such as the public keys, the supported algorithms,
the type of entity (in addition to the Wallet Provider, for example, it could also
be a relying party) and the list of the available endpoints.
It broadly implements openid-federation protocol.

Header
^^^^^^
+---------+----------------------------------------------------------------+
| **key** | **value**                                                      |
+---------+----------------------------------------------------------------+
| alg     | Algorithm to verify the token signature (es. ES256)            |
+---------+----------------------------------------------------------------+
| kid     | Thumbprint of the public key used for signing                  |
+---------+----------------------------------------------------------------+
| type    | Media type, in this case, we use the entity-statement+jwt value|
+---------+----------------------------------------------------------------+

Payload
^^^^^^^
+-----------------------------------+-----------------------------------+
| **key**                           | **value**                         |
+-----------------------------------+-----------------------------------+
| iss                               | The public url of the wallet      |
|                                   | provider                          |
+-----------------------------------+-----------------------------------+
| sub                               | The public url of the wallet      |
|                                   | provider                          |
+-----------------------------------+-----------------------------------+
| iat                               | Configuration release timestamp   |
+-----------------------------------+-----------------------------------+
| exp                               | Configuration expiration          |
|                                   | timestamp.                        |
+-----------------------------------+-----------------------------------+
| jwks                              | Containing the keys attribute     |
|                                   | which is an array of all the      |
|                                   | public keys associated with the   |
|                                   | domain (they could also match     |
|                                   | those of the Wallet Provider)     |
+-----------------------------------+-----------------------------------+
| metadata                          | This attribute will contain for   |
|                                   | each entity its own               |
|                                   | configuration. In our case we     |
|                                   | will have for now the wallet      |
|                                   | provider entity contained within  |
|                                   | the `eudi_wallet_provider`        |
|                                   | attribute and the more generic    |
|                                   | entity `federation_entity`        |
+-----------------------------------+-----------------------------------+

Payload `eudi_wallet_provider`
''''''''''''''''''''''''''''''
+-----------------------------------+-----------------------------------+
| **key**                           | **value**                         |
+-----------------------------------+-----------------------------------+
| jwks                              | Containing the keys attribute     |
|                                   | which is an array of all the      |
|                                   | Wallet Provider's public keys     |
+-----------------------------------+-----------------------------------+
| token_endpoint                    | Endpoint for obtaining the Wallet |
|                                   | Instance Attestation              |
+-----------------------------------+-----------------------------------+
| asc_values_supported              | List of supported values for      |
|                                   | the certified security context.   |
|                                   | These values define a level of    |
|                                   | assurance about the security of   |
|                                   | the app. In particular we will    |
|                                   | mainly have 3 values associated   |
|                                   | with low, medium and high         |
|                                   | security. An attested security    |
|                                   | context is defined according to   |
|                                   | the proof that the wallet         |
|                                   | instance is able to send to the   |
|                                   | Wallet Provider.                  |
+-----------------------------------+-----------------------------------+
| grant_types_supported             | The type of grants supported by   |
|                                   | the endpoint token. Therefore,    |
|                                   | for the Wallet Provider the token |
|                                   | is equivalent only to the wallet  |
|                                   | instance attestation, therefore   |
|                                   | this attribute will contain an    |
|                                   | array with only one element:      |
|                                   | urn:ietf:params:oauth:grant-type: |
|                                   | wallet-instance-attestation       |
+-----------------------------------+-----------------------------------+
| token_endpoint_auth_methods_suppo | Supported authentication method   |
| rted                              | for the endpoint token. In our    |
|                                   | case it's just private_key_jwt    |
+-----------------------------------+-----------------------------------+
| token_endpoint_auth_signing_alg_v | List of supported signature       |
| alues_supported                   | algorithms                        |
+-----------------------------------+-----------------------------------+

Payload `federation_entity`
'''''''''''''''''''''''''''
+-------------------+----------------------------------------+
| **key**           | **value**                              |
+-------------------+----------------------------------------+
| organization_name | Organization name                      |
+-------------------+----------------------------------------+
| homepage_uri      | Organization website                   |
+-------------------+----------------------------------------+
| tos_uri           | Url to the terms of use                |
+-------------------+----------------------------------------+
| policy_uri        | Url to the privacy policy              |
+-------------------+----------------------------------------+
| logo_uri          | URL of the organization logo           |
+-------------------+----------------------------------------+

Non-normative example
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

  {
    "alg": "ES256",
    "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
    "typ": "entity-statement+jwt"
  }
  .
  {
    "iss": "https://wallet.italia.it",
    "sub": "https://wallet.italia.it",
    "jwk": {
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
        "jwk": {
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
        "token_endpoint": "https://wallet.italia.it/token",
        "asc_values_supported": [
          "https://wallet.italia.it/LoA/basic",
          "https://wallet.italia.it/LoA/medium",
          "https://wallet.italia.it/LoA/high"
        ],
        "grant_types_supported": [
          "urn:ietf:params:oauth:grant-type:wallet-instance-attestation"
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
        "homepage_uri": "https://wallet.italia.it",
        "policy_uri": "https://wallet.italia.it/privacy_policy",
        "tos_uri": "https://wallet.italia.it/info_policy",
        "logo_uri": "https://wallet.italia.it/logo.svg"
      }
    },
    "iat": 1686667326,
    "exp": 1708785726
  }

Whose corresponding JWS is as follows:

.. code-block:: javascript

  eyJhbGciOiJFUzI1NiIsImtpZCI6IjV0NVlZcEJoTi1FZ0lFRUk1aVV6cjZyME1SMDJMblZRME9tZWttTktjalkiLCJ0eXAiOiJlbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC5pdGFsaWEuaXQiLCJzdWIiOiJodHRwczovL3dhbGxldC5pdGFsaWEuaXQiLCJqd2siOnsia2V5cyI6W3siY3J2IjoiUC0yNTYiLCJrdHkiOiJFQyIsIngiOiJxckpyajNBZl9CNTdzYk9JUnJjQk03YnI3d09jOHluajdsSEZQVGVmZlVrIiwieSI6IjFIMGNXRHlHZ3ZVOHcta1BLVV94eWNPQ1VOVDJvMGJ3c2xJUXRuUFU2aU0iLCJraWQiOiI1dDVZWXBCaE4tRWdJRUVJNWlVenI2cjBNUjAyTG5WUTBPbWVrbU5LY2pZIn1dfSwibWV0YWRhdGEiOnsiZXVkaV93YWxsZXRfcHJvdmlkZXIiOnsiandrIjp7ImtleXMiOlt7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoicXJKcmozQWZfQjU3c2JPSVJyY0JNN2JyN3dPYzh5bmo3bEhGUFRlZmZVayIsInkiOiIxSDBjV0R5R2d2VTh3LWtQS1VfeHljT0NVTlQybzBid3NsSVF0blBVNmlNIiwia2lkIjoiNXQ1WVlwQmhOLUVnSUVFSTVpVXpyNnIwTVIwMkxuVlEwT21la21OS2NqWSJ9XX0sInRva2VuX2VuZHBvaW50IjoiaHR0cHM6Ly93YWxsZXQuaXRhbGlhLml0L3Rva2VuIiwiYXNjX3ZhbHVlc19zdXBwb3J0ZWQiOlsiaHR0cHM6Ly93YWxsZXQuaXRhbGlhLml0L0xvQS9iYXNpYyIsImh0dHBzOi8vd2FsbGV0Lml0YWxpYS5pdC9Mb0EvbWVkaXVtIiwiaHR0cHM6Ly93YWxsZXQuaXRhbGlhLml0L0xvQS9oaWdoIl0sImdyYW50X3R5cGVzX3N1cHBvcnRlZCI6WyJ1cm46aWV0ZjpwYXJhbXM6b2F1dGg6Z3JhbnQtdHlwZTp3YWxsZXQtaW5zdGFuY2UtYXR0ZXN0YXRpb24iXSwidG9rZW5fZW5kcG9pbnRfYXV0aF9tZXRob2RzX3N1cHBvcnRlZCI6WyJwcml2YXRlX2tleV9qd3QiXSwidG9rZW5fZW5kcG9pbnRfYXV0aF9zaWduaW5nX2FsZ192YWx1ZXNfc3VwcG9ydGVkIjpbIkVTMjU2IiwiRVMzODQiLCJFUzUxMiJdfSwiZmVkZXJhdGlvbl9lbnRpdHkiOnsib3JnYW5pemF0aW9uX25hbWUiOiJQYWdvUGEgUy5wLkEuIiwiaG9tZXBhZ2VfdXJpIjoiaHR0cHM6Ly93YWxsZXQuaXRhbGlhLml0IiwicG9saWN5X3VyaSI6Imh0dHBzOi8vd2FsbGV0Lml0YWxpYS5pdC9wcml2YWN5X3BvbGljeSIsInRvc191cmkiOiJodHRwczovL3dhbGxldC5pdGFsaWEuaXQvaW5mb19wb2xpY3kiLCJsb2dvX3VyaSI6Imh0dHBzOi8vd2FsbGV0Lml0YWxpYS5pdC9sb2dvLnN2ZyJ9fSwiaWF0IjoxNjg2NjY3MzI2LCJleHAiOjE3MDg3ODU3MjZ9.GiPss36QHS29YRmKkxPDNdS6lHmlNLLaLYQIVMGupXiTmQlhLANulePcKFkVBzq7tj1UUKu7zxfPfZMcuCo_EQ

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
``urn:ietf:params:oauth:grant-type:wallet-instance-attestation``

``assertion``` which contains the signed JWT of the Wallet Instance Attestation
Request

The response will then contain the Wallet Instance Attestation

Open API specifications
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

  openapi: 3.0.0
  info:
    title: Wallet Backend
    version: 1.0.0
  servers:
    - url: https://wallet.italia.it
  paths:
    /.well-known/openid-federation:
      get:
        summary: Get Wallet Provider metadata
        responses:
          '200':
            description: Successful response
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Jwt'
                example:
                  "eyJhbGciOiJFUzI1NiIsImtpZCI6IjV0NVlZcEJoTi1FZ0lFRUk1aVV6cjZyME1SMDJMblZRME9tZWttTktjalkiLCJ0eXAiOiJlbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC5pdGFsaWEuaXQiLCJzdWIiOiJodHRwczovL3dhbGxldC5pdGFsaWEuaXQiLCJqd2siOnsia2V5cyI6W3siY3J2IjoiUC0yNTYiLCJrdHkiOiJFQyIsIngiOiI0SE5wdEkteHIycGp5UkpLR01uejRXbWRuUURfdUpTcTRSOTVOajk4YjQ0IiwieSI6IkxJWm5TQjM5dkZKaFlnUzNrN2pYRTRyMy1Db0dGUXdadFBCSVJxcE5scmciLCJraWQiOiJ2YmVYSmtzTTQ1eHBodEFObkNpRzZtQ3l1VTRqZkdOem9wR3VLdm9nZzljIn1dfSwibWV0YWRhdGEiOnsiZXVkaV93YWxsZXRfcHJvdmlkZXIiOnsiandrIjp7ImtleXMiOlt7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoiNEhOcHRJLXhyMnBqeVJKS0dNbno0V21kblFEX3VKU3E0Ujk1Tmo5OGI0NCIsInkiOiJMSVpuU0IzOXZGSmhZZ1MzazdqWEU0cjMtQ29HRlF3WnRQQklScXBObHJnIiwia2lkIjoidmJlWEprc000NXhwaHRBTm5DaUc2bUN5dVU0amZHTnpvcEd1S3ZvZ2c5YyJ9XX0sInRva2VuX2VuZHBvaW50IjoiaHR0cHM6Ly93YWxsZXQuaXRhbGlhLml0L3Rva2VuIiwiYWNyX3ZhbHVlc19zdXBwb3J0ZWQiOlsiaHR0cHM6Ly93YWxsZXQuaXRhbGlhLml0L0xvQS9iYXNpYyIsImh0dHBzOi8vd2FsbGV0Lml0YWxpYS5pdC9Mb0EvbWVkaXVtIiwiaHR0cHM6Ly93YWxsZXQuaXRhbGlhLml0L0xvQS9oaWdoIl0sImdyYW50X3R5cGVzX3N1cHBvcnRlZCI6WyJ1cm46aWV0ZjpwYXJhbXM6b2F1dGg6Z3JhbnQtdHlwZTp3YWxsZXQtaW5zdGFuY2UtYXR0ZXN0YXRpb24iXSwidG9rZW5fZW5kcG9pbnRfYXV0aF9tZXRob2RzX3N1cHBvcnRlZCI6WyJwcml2YXRlX2tleV9qd3QiXSwidG9rZW5fZW5kcG9pbnRfYXV0aF9zaWduaW5nX2FsZ192YWx1ZXNfc3VwcG9ydGVkIjpbIkVTMjU2IiwiRVMzODQiLCJFUzUxMiJdfSwiZmVkZXJhdGlvbl9lbnRpdHkiOnsib3JnYW5pemF0aW9uX25hbWUiOiJQYWdvUGEgUy5wLkEuIiwiaG9tZXBhZ2VfdXJpIjoiaHR0cHM6Ly93YWxsZXQuaXRhbGlhLml0IiwicG9saWN5X3VyaSI6Imh0dHBzOi8vd2FsbGV0Lml0YWxpYS5pdC9wcml2YWN5X3BvbGljeSIsInRvc191cmkiOiJodHRwczovL3dhbGxldC5pdGFsaWEuaXQvaW5mb19wb2xpY3kiLCJsb2dvX3VyaSI6Imh0dHBzOi8vd2FsbGV0Lml0YWxpYS5pdC9sb2dvLnN2ZyJ9fSwiaWF0IjoxNjg2NjYzODg0LCJleHAiOjE3MDg3ODIyODR9.cvL5gH1Wm6A9ii2iQ-TNsQnccY7MMPdlDb57jPwGqCMTM9JGygu_nzObjqADvMO2hcbLMKjb17WA5okdn9x9Aw"

    /token:
      post:
        summary: Create Wallet Instance Attestation
        requestBody:
          required: true
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateWalletInstanceAttestation'
        responses:
          '200':
            description: Successful response
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Jwt'
                example:
                  "eyJhbGciOiJFUzI1NiIsImtpZCI6IjV0NVlZcEJoTi1FZ0lFRUk1aVV6cjZyME1SMDJMblZRME9tZWttTktjalkiLCJ0cnVzdF9jaGFpbiI6W10sInR5cCI6InZhK2p3dCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC5pdGFsaWEuaXQiLCJzdWIiOiJodHRwczovL3dhbGxldC5pdGFsaWEuaXQvaW5zdGFuY2UvdmJlWEprc000NXhwaHRBTm5DaUc2bUN5dVU0amZHTnpvcEd1S3ZvZ2c5YyIsInR5cGUiOiJXYWxsZXRJbnN0YW5jZUF0dGVzdGF0aW9uIiwicG9saWN5X3VyaSI6Imh0dHBzOi8vd2FsbGV0Lml0YWxpYS5pdC9wcml2YWN5X3BvbGljeSIsInRvc191cmkiOiJodHRwczovL3dhbGxldC5pdGFsaWEuaXQvaW5mb19wb2xpY3kiLCJsb2dvX3VyaSI6Imh0dHBzOi8vd2FsbGV0Lml0YWxpYS5pdC9sb2dvLnN2ZyIsImFzYyI6Imh0dHBzOi8vd2FsbGV0Lml0YWxpYS5pdC9Mb0EvYmFzaWMiLCJjbmYiOnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoiNEhOcHRJLXhyMnBqeVJKS0dNbno0V21kblFEX3VKU3E0Ujk1Tmo5OGI0NCIsInkiOiJMSVpuU0IzOXZGSmhZZ1MzazdqWEU0cjMtQ29HRlF3WnRQQklScXBObHJnIiwia2lkIjoidmJlWEprc000NXhwaHRBTm5DaUc2bUN5dVU0amZHTnpvcEd1S3ZvZ2c5YyJ9fSwiaWF0IjoxNjg2NjQ1MTE1LCJleHAiOjE2ODY2NTIzMTV9.hJ7oGn3RYO8ctF1Orl10zdFKjTk9-oowPZ3QeKuJC5tgdEPjesaZImQKjTOcx8v0IwSMMQ4YHX63hIGBMtnRFA"
  components:
    schemas:
      CreateWalletInstanceAttestation:
        type: object
        properties:
          grant_type:
            type: string
          assertion:
            $ref: '#/components/schemas/Jwt'
        example:
          grant_type: "urn:ietf:params:oauth:grant-type:wallet-instance-attestation"
          assertion: "eyJhbGciOiJFUzI1NiIsImtpZCI6InZiZVhKa3NNNDV4cGh0QU5uQ2lHNm1DeXVVNGpmR056b3BHdUt2b2dnOWMiLCJ0eXAiOiJ2YXIrand0In0.eyJpc3MiOiJodHRwczovL3dhbGxldC5pdGFsaWEuaXQvaW5zdGFuY2UvdmJlWEprc000NXhwaHRBTm5DaUc2bUN5dVU0amZHTnpvcEd1S3ZvZ2c5YyIsInN1YiI6Imh0dHBzOi8vd2FsbGV0Lml0YWxpYS5pdC8iLCJqdGkiOiI2ZWM2OTMyNC02MGE4LTRlNWItYTY5Ny1hNzY2ZDg1NzkwZWEiLCJ0eXBlIjoiV2FsbGV0SW5zdGFuY2VBdHRlc3RhdGlvblJlcXVlc3QiLCJjbmYiOnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoiNEhOcHRJLXhyMnBqeVJKS0dNbno0V21kblFEX3VKU3E0Ujk1Tmo5OGI0NCIsInkiOiJMSVpuU0IzOXZGSmhZZ1MzazdqWEU0cjMtQ29HRlF3WnRQQklScXBObHJnIiwia2lkIjoidmJlWEprc000NXhwaHRBTm5DaUc2bUN5dVU0amZHTnpvcEd1S3ZvZ2c5YyJ9fSwiaWF0IjoxNjg2NjQ1MTE1LCJleHAiOjE2ODY2NTIzMTV9.3KInOD_N4zh5PmXj9QhS5aIVFF8zxMl6326KxDTAFYMPJbweD2ny95Nk6y_xTCOioail2WHDLpF3Rju16Q7Z7Q"

      Jwt:
        type: "string"
        format: "application/jwt"
        pattern: ^([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_\-\+\/=]+)$

