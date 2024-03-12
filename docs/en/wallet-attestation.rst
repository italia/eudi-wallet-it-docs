.. include:: ../common/common_definitions.rst

.. _wallet-attestation.rst:

Wallet Attestation
++++++++++++++++++

The Wallet Attestation containing details about the Wallet Instance and the device's security level where the Wallet Instance is installed. It generally attests the **authenticity**, **integrity**, **security**, **privacy**, and **trust** of a specific Wallet Instance. The Wallet Attestation MUST contain a Wallet Instance public key.

General Properties
------------------

The Wallet Attestation:

- MUST be issued and MUST be signed by Wallet Provider;
- MUST give all the relevant information to attests the **integrity** and **security** of the device where the Wallet Instance is installed.
- MUST ensure that the Wallet Instance is genuine, preventing any attempts at manipulation or falsification by unauthorized third parties.
- MUST ensure that private keys have been generated and securely stored within a trusted execution environment.
- MUST have a mechanism in place for revoking the Wallet Instance, allowing the Wallet Provider to terminate service for a specific instance at any time.

It is necessary for each Wallet Instance to obtain a Wallet Attestation before entering the Operational state.

Requirements
------------

The following requirements for the Wallet Attestation are met:

1. The Wallet Attestation MUST use the signed JSON Web Token (JWT) format.
2. The Wallet Provider MUST offer a RESTful set of services for issuing the Wallet Attestations.
3. The Wallet Attestation MUST be securely bound to the Wallet Instance public key (**Holder Key Binding**).
4. The Wallet Attestation MUST be issued and signed by an accredited and reliable Wallet Provider, thereby providing integrity and authenticity to the attestation.
5. The Wallet Attestation MUST ensure the integrity and authenticity of the Wallet Instance, verifying that it was accurately created and provided by the Wallet Provider.
6. Each Wallet Instance SHOULD be able to request multiple attestations with different public keys associated to them. This requirement provides a privacy-preserving measure, as the public key MAY be used as a tracking tool during the presentation phase (see also the point number 10, listed below).
7. The Wallet Attestation SHOULD be usable multiple times during its validity period, allowing for repeated authentication and authorization without the need to request new attestations with each interaction.
8. The Wallet Attestation SHOULD have an expiration date time, after which it will no longer be considered valid.
9. The Wallet Attestation SHOULD no longer needs to be issued by the Wallet Provider if the Wallet Instance has been revoked.
10. The Wallet Attestation SHOULD be pseudo-anonymous (meaning they do not contain direct references to an individual), making it impossible to identify a person without additional information.
11. When the private key associated with the Wallet Instance is lost or deleted, the attestation MUST become invalid to prevent unauthorized use of the Wallet Instance.


Static Component View
---------------------

.. figure:: ../../images/static_view_wallet_instance_attestation.svg
   :name: Wallet Solution Schema
   :alt: The image illustrates the containment of Wallet Provider and Wallet Instances within the Wallet Solution, managed by the Wallet Provider.
   :target: https://www.plantuml.com/plantuml/uml/VP8nJyCm48Lt_ugdTexOCw22OCY0GAeGOsMSerWuliY-fEg_9mrEPTAqw-VtNLxEtaJHGRh6AMs40rRlaS8AEgAB533H3-qS2Tu2zxPEWSF8TcrYv-mJzTOGNfzVnXXJ0wKCDorxydAUjMNNYMMVpug9OTrR7i22LlaesXlADPiOraToZWyBsgCsF-JhtFhyGyZJgNlbXVR1oX5R2YSoUdQYEzrQO1seLcfUeGXs_ot5_VzqYM6lQlRXMz6hsTccIbGHhGu2_hhfP1tBwHuZqdOUH6WuEmrKIeqtNonvXhq4ThY3Dc9xBNJv_rSwQeyfawhcZsTPIpKLKuFYSa_JyOPytJNk5m00

Dynamic Component View
----------------------

The Wallet Attestation acquisition flow can be divided into two main phases. The first phase involves device initialization and registration, which occurs only during the initial launch of the Wallet Instance (after installation). The second phase pertains to the actual acquisition of the Wallet Attestation.

Wallet Instance initialization and registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../images/wallet_instance_initialization.svg
   :name: Sequence Diagram for Wallet Instance Initialization
   :alt: The figure illustrates the sequence diagram for initializa a Wallet Instance, with the steps explained below.
   :target: https://www.plantuml.com/plantuml/uml/TLFHRjD047o_hrYb3xHM-84ye288QLMWY1HuNjiRPnNdpjfR1yBNisUd8RRY1rkdlPdPcR5y7nL5sttjiDNWstrEuhPS4cn2q3pySMyQ0t313Nfr3WiD0hCVaMG66A6rWxj0mEmNrZKfF7fJzWLrA6mQ6A8-qe4BCfHI9Qn7M9FOv0H7ZN0J6s5VLKBahsxu9k5WHWLoB7RaouwQ5pldAWbj0y7NHsYRu6734XNO71aJbMqKDg1RIiPSYl3sdPqMq9KHNs_WjYSQu2u5vmDgJx7dnFYmfM87l86fGC2Mvu1SOrwJS-A34eG3IHAQcrsu-VouUdXPVLyklxfURXpG9581hwO_aGtx6EXB2BaYUs0plYV54XMTrT5jSgxtQdiMi2A5B2ksITrNb6NdK5rjzfo1dYIDWoTGtbEgO4HDwBw3qKL90zLpLMTLmvy2Fg2Klr48dkWOiyn2idIHeWQPmC4BLbbsaaMD2q1LYcfNjsSRSvXWthd4-MyyZTzt_AvFyn2vybH2VeJdvPUByjPMwJ3f_2hVx4yRdwxy9zPSeevQlWeOBnt0rjFDnU5NUtwwygdiClqE2nZznNPWPRFmbyfBcb6S5UFkxTNkwty0

**Step 1:**: The User starts the Wallet Instance mobile app for the first time.

**Step 2:**: The Wallet Instance:

  * check if Device Integrity Service is available.
  * check whether the device meets the minimum security requirements.

.. note::

    **Federation Check:** The Wallet Instance needs to check if the Wallet Provider is part of the Federation, obtaining its protocol specific Metadata. A non-normative example of a response from the endpoint **.well-known/openid-federation** with the **Entity Configuration** and the **Metadata** of the Wallet Provider is represented within the section `Wallet Provider metadata`_.

**Steps 3-5:**: The Wallet Instance request and receive a one time ``challenge`` from the Wallet Provider Backend. The ``challenge`` is a ``nonce``, which MUST be unpredictable and it is the primary countermeasure against replay attack. The value of the ``nonce`` returned by the backend must be generated in such a way as to guarantee that it can only be used once and in a pre-established time interval.


.. code-block:: http

    GET /nonce HTTP/1.1
    Host: walletprovider.example.com

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "nonce": "d2JhY2NhbG91cmVqdWFuZGFt"
    }

**Step 6**: The Wallet Instance generates the Wallet Hardware Keys pair via the operating system and store the relative Wallet Hardware Key Tag in a local storage:

   1. It MUST ensure that Wallet Hardware Keys do not already exist, if they exist and the Wallet is in the initialization phase they must be deleted.
   2. It MUST generate a pair of asymmetric EC keys (Wallet Hardware Keys) via a local WSCD.
   3. It SHOULD obtain a unique identifier (Wallet Hardware Key Tag) of the generated Wallet Hardware Keys from the operating system. If the operating system allows you to define a tag when creating keys, then a random string for Wallet Hardware Key Tag must be chosen.
   4. It MUST store the relative Wallet Hardware Key Tag in a local storage.

.. note::

    **WSCD:** For key generation, the Wallet Instance will always rely on a local WSCD on devices that support it. For Android, Strongbox will be used or, if it is not available, a Trusted Execution Environment (TEE) while for iOS Secure Elements (SE). Since each OEM develops a different SDK for accessing the local WSCD, it will be treated in a generic manner below.


**Step 7**: The Wallet Instance: invokes the operating system attestation service (Device Integrity Service) passing ``challenge`` and Wallet Hardware Key Tag in order to obtain a Key Attestation.

.. note::

    **Device Integrity Service:** Below we will treat a Device Integrity Service as an abstract entity made available by device OEMs which allows us to certify via a signed payload (attestation) that a particular key is hardware backed in a safe and protected environment of the device. Furthermore, the service will also allow you to demonstrate via a signed payload (assertion) that that particular app instance (Wallet Instance) is intact and genuine and has not been tampered with. Furthermore, both within the attestation and the assertion, the service includes essential information to recover the type of device, the model, the app version, the operating system version, the bootloader status and other information that allows you to understand whether the device has been tampered with or not. For Android the service used is `Key Attestation`_ in addition to `Play Integrity API`_, while for iOS the `DeviceCheck`_ service.

**Step 8**: The Device Integrity Service:

  * generate a Key Attestation holder binded with ``challenge`` and Wallet Hardware public key.
  * adds relevant information on the security of the device.
  * sign the Key Attestation with an OEM certificate which in addition to certifying the integrity of the Wallet Instance also certifies that the Wallet Hardware Keys is secure stored by the OS (hardware backed).

**Step 9**: The Wallet Instance send the ``challenge`` with Key Attestation and Wallet Hardware Key Tag to the Wallet Provider Backend in order to register the Wallet Instance identified by the Wallet Hardware Key public key.

.. note::

  The Key Attestation (``key_attestation``) must always be encoded in base64 as the format is different between the various operating systems.


.. code-block:: http

    PUT /wallet-instance HTTP/1.1
    Host: walletprovider.example.com
    Content-Type: application/json

    {
      "challenge": "0fe3cbe0-646d-44b5-8808-917dd5391bd9",
      "key_attestation": "o2NmbXRvYXBwbGUtYXBw... redacted",
      "hardware_key_tag": "WQhyDymFKsP95iFqpzdEDWW4l7aVna2Fn4JCeWHYtbU="
    }

.. note::
  It is not necessary to send the Wallet Hardware public key as it is already included in the ``key_attestation``.

**Steps 10-12**: The Wallet Provider validate the ``challenge`` and ``key_attestation`` signature:

  1. It MUST verify that the ``challenge`` was generated by  Wallet Provider and has not already been used.
  2. It MUST validate the ``key_attestation`` as defined by the device manufacturers' guidelines.
  3. It MUST verify that the device in use has no security flaws and reflects the minimum security requirements defined by the Wallet Provider.
  4. If these checks are passed, it MUST register the Wallet Instance, keeping the Wallet Hardware Key Tag and all useful information related to the device.
  5. It SHULD associate the Wallet Instance with a specific user uniquely identified within the Wallet Provider's systems. This will be useful for the lifecycle of the Wallet Instance and for a future revocation.

.. code-block:: http

    HTTP/1.1 201 Created
    Content-Type: application/json

If any errors occur during the Wallet Instance registration, the Wallet Provider MUST return an error response. The response MUST use *application/json* as the content type and MUST include the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered.

**Steps 13-14**: The Wallet Instance has been initialized and becomes operational.

.. note:: **Threat Model:** Although the registration endpoint does not require any authentication, it is protected by the presence of the ``key_attestation`` which, if validated correctly, only allows the registration of valid and intact instances of the app. Any other claims sent will not be validated and therefore the endpoint will return an error. The presence of a ``challenge`` also avoids reply attacks. Finally, the integrity of the ``challenge`` and the ``hardware_key_tag`` is guaranteed by the signature present within the ``key_attestation``.


Wallet Attestation acquisition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section describes the Wallet Attestation format and how the Wallet Provider issues it.

.. figure:: ../../images/wallet_instance_acquisition.svg
   :name: Sequence Diagram for Wallet Attestation acquisition
   :alt: The figure illustrates the sequence diagram for issuing a Wallet Attestation, with the steps explained below.
   :target: https://www.plantuml.com/plantuml/uml/VLHFJzjE4BtlfnZ1uGTHVfTAxG6f5OXIe5GL0bekID7O7knfd5rtT-oKVlhEEdySXsqFbbZspNjltixaD0XwQHUrmLQSRHSPULDnGV3id6Jkb_clKG3dtA0LOp0Nv-7WMo1_01YW3OhVGS318zOr2LnRPROvzIXi6XYZFbB7EIbAgFGiBt1FlkCD72N0OMWysxBqH3QfSEjTfqOzP9ZFoHPzQPRFZJ7HrVyVLFK4xkXdIq40mT8IN4CUXPq5gL2UhDTRzgIIC9ciUSz4jA17JIQnOUvGAFPWz5lJdbUKpu6VXx8hzCKIFS4DlOJ915X9E-GQivhCJkKbsUWXQbgWfgA57ckOqmiqo5u9Fp_UgB3nrgciwyX7xQbs1eTVhY-l7YxlBYw-cfM3_InKDMO5xbax9FX4nQPXj0MuJ90ji0HOa621WaQJwvNCsgJgH9EYHl8gijkITdE82UlN0uTkm5a2uGN5YTWhZUXry-EBWaQi9XLJBAcPhCoYsrc5eT9mCS3zrTcRj--EjdnJQDgivdpsOpa_JZ6bdqh9RjtjapvrjVxlB71fKLfFUlSUukbety8KbZtLR5kaxpSJBBVAAE44ohNqTipFGY0lx5up7fjOCkJ4cv8PRchKJhAlrtExdVebI_KtiYcaUvwENsdwP9F1mGEMA_2GkpgCH5JqmiDqRuTwcB1xiiK_d8_dRLY5U4olGbp6lT-Uk0riMHXh_ar5lmAT_bsODh0j8TMLODdZqjaCspAimFV8Y9AQ-Z4W_H1fQ5e-ZTHeLrEySttkQNNvEkBnHgOGYTNSEMkPETKSsaNz1m00

**Step 1:**: The user requests a new operation which requires obtaining a Wallet Attestation.

**Steps 2-3:**: The Wallet Instance check if a Wallet Hardware Key exist and generates an ephemeral asymmetric key pair.

  1. It MUST ensure that Wallet Hardware Keys exist. If they do not exist, it is necessary to reinitialize the wallet.
  2. It MUST generates an ephemeral asymmetric key pair whose public key will be linked with the Wallet Attestation.
  3. it MUST check if Wallet Provider is part of the federation and obtain its metadata.


**Steps 4-6:**: The Wallet Instance request and receive a one time ``challenge`` from the Wallet Provider Backend. The ``challenge`` is a ``nonce``, which MUST be unpredictable and it is the primary countermeasure against replay attack. The value of the ``nonce`` returned by the backend must be generated in such a way as to guarantee that it can only be used once and in a pre-established time interval.

.. code-block:: http

    GET /nonce HTTP/1.1
    Host: walletprovider.example.com

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "nonce": "d2JhY2NhbG91cmVqdWFuZGFt"
    }

**Step 7**: The Wallet Instance:

  * generate a ``client_data`` which is a JSON containing ``challenge`` and ephemeral public ``jwk``.
  * generate a ``client_data_hash`` as SHA256 of ``client_data``.

Below a non-normative example of the ``client_data``.

.. code-block:: json

  {
    "challenge": "0fe3cbe0-646d-44b5-8808-917dd5391bd9",
    "jwk": {
        "crv": "P-256",
        "kty": "EC",
        "x": "4HNptI-xr2pjyRJKGMnz4WmdnQD_uJSq4R95Nj98b44",
        "y": "LIZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg",
        "kid": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"
      }
  }

**Steps 8-10**: The Wallet Instance:

  * generate an ``hardware_signature`` signing ``client_data_hash`` with Wallet Hardware private key. It will be used as a **PoP** of the Wallet Hardware Keys.
  * ask to Device Integrity Service to generate an ``integrity_assertion`` bounded with ``client_data_hash``.
  * obtain from Device Integrity Service an ``integrity_assertion`` signed by OEM.

.. note:: ``integrity_assertion`` is a custom payload generated by Device Integrity Service, signed by device OEM and encoded in base64 to have uniformity between different devices.

**Steps 11-12**: The Wallet Instance:
  * generate the Wallet Attestation Request as a JWT containing ``integrity_assertion``, ``hardware_signature``, ``challenge``, ``wallet_hardware_key_tag``, ``public_jwk`` signed with the private key associated with the public key of the ephemeral key pair generated initially.
  * send the Wallet Attestation Request to Wallet Provider backend via token endpoint.

Below an non-normative example of the Wallet Attestation Request JWT without encoding and signature applied:

.. code-block::

  {
    "alg": "ES256",
    "kid": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "typ": "var+jwt"
  }
  .
  {
    "iss": "https://wallet-provider.example.org/instance/vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "sub": "https://wallet-provider.example.org/",
    "challenge": "6ec69324-60a8-4e5b-a697-a766d85790ea",
    "type": "WalletAttestationRequest",
    "hardware_signature": "KoZIhvcNAQcCoIAwgAIB...redacted",
    "integrity_assertion": "o2NmbXRvYXBwbGUtYXBwYX...redacted",
    "hardware_key_tag": "WQhyDymFKsP95iFqpzdEDWW4l7aVna2Fn4JCeWHYtbU=",
    "cnf": {
      "jwk": {
        "crv": "P-256",
        "kty": "EC",
        "x": "4HNptI-xr2pjyRJKGMnz4WmdnQD_uJSq4R95Nj98b44",
        "y": "LIZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg",
        "kid": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"
      },
      "vp_formats_supported": {
          "jwt_vc_json": {
            "alg_values_supported": ["ES256K", "ES384"],
          },
          "jwt_vp_json": {
            "alg_values_supported": ["ES256K", "EdDSA"],
          },
        },
    },
    "iat": 1686645115,
    "exp": 1686652315
  }

The Wallet Instance MUST do an HTTP request to the Wallet Provider's `token endpoint`_,
using the method `POST <https://datatracker.ietf.org/doc/html/rfc6749#section-3.2>`__.

The **token** endpoint (as defined in `RFC 7523 section 4`_) requires the following parameters
encoded in ``application/x-www-form-urlencoded`` format:

* ``grant_type`` set to ``urn:ietf:params:oauth:grant-type:jwt-bearer``;
* ``assertion`` containing the signed JWT of the Wallet Attestation Request.

.. code-block:: http

    POST /token HTTP/1.1
    Host: wallet-provider.example.org
    Content-Type: application/x-www-form-urlencoded

    grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer
    &assertion=eyJhbGciOiJFUzI1NiIsImtpZCI6ImtoakZWTE9nRjNHeG...redacted

**Steps 13-17**: The Wallet Provider backend validate the Wallet Attestation Request and if it passes the checks, a Wallet Attestation is issued:

    1. It MUST check the Wallet Attestation Request contains all the defined parameters according to :ref:`Table of the Wallet Attestation Request parameters <table_wallet_attestation_request_claim>`.
    2. It MUST verify that the signature of the received Wallet Attestation Request is valid and associated with public ``jwk``.
    3. It MUST verify that the ``challenge`` was generated by  Wallet Provider and has not already been used.
    4. It MUST check that there is a Wallet Instance registered with that ``hardware_key_tag`` and that it is still valid.
    5. It MUST reconstruct the ``client_data`` via the ``challenge`` and the ``jwk`` public key, to validate ``hardware_signature`` via the Wallet Hardware Key public key registered and associated with the Wallet Instance.
    6. It MUST validate the ``integrity_assertion`` as defined by the device manufacturers' guidelines.
    7. It MUST verify that the device in use has no security flaws and reflects the minimum security requirements defined by the Wallet Provider.
    8. It MUST check that the URL in ``iss`` parameter is equal to the URL identifier of Wallet Provider.

If all checks are passed, Wallet Provider issues a Wallet Attestation with an expiration limited to 24 hours.

Below an non-normative example of the Wallet Attestation without encoding and signature applied:

.. code-block::

    {
    "alg": "ES256",
    "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
    "trust_chain": [
      "eyJhbGciOiJFUz...6S0A",
      "eyJhbGciOiJFUz...jJLA",
      "eyJhbGciOiJFUz...H9gw",
    ],
    "typ": "wallet-attestation+jwt",
  }
  .
  {
    "iss": "https://wallet-provider.example.org",
    "sub": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "aal": "https://trust-list.eu/aal/high",
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
    "response_modes_supported": [
      "form_post.jwt"
    ],
    "vp_formats_supported": {
        "vc+sd-jwt": {
            "sd-jwt_alg_values": [
                "ES256",
                "ES384"
            ]
        }
    },
    "request_object_signing_alg_values_supported": [
      "ES256"
    ],
    "presentation_definition_uri_supported": false,
    "iat": 1687281195,
    "exp": 1687288395
  }

**Step 18**: The Wallet Instance receives the Wallet Attestation signed by the Wallet Provider and performs security and integrity verifications.

.. code-block:: http

    HTTP/1.1 201 OK
    Content-Type: application/jwt

    eyJhbGciOiJFUzI1NiIsInR5cCI6IndhbGx... redacted



.. _table_wallet_attestation_request_claim:

Wallet Attestation Request
~~~~~~~~~~~~~~~~~~~~~~~~~~

The JOSE header of the Wallet Attestation Request JWT MUST contain:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section `Cryptographic Algorithms <algorithms.html>`_ and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      -  Unique identifier of the ``jwk`` inside the ``cnf`` claim of Wallet Instance as base64url-encoded JWK Thumbprint value.
      - :rfc:`7638#section_3`.
    * - **typ**
      -  It MUST be set to ``var+jwt``
      -

The body of the Wallet Attestation Request JWT MUST contain:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - Identifier of the Wallet Provider concatenated with thumbprint of the JWK in the ``cnf`` parameter.
      - :rfc:`9126` and :rfc:`7519`.
    * - **aud**
      - It MUST be set to the identifier of the Wallet Provider.
      - :rfc:`9126` and :rfc:`7519`.
    * - **exp**
      - UNIX Timestamp with the expiry time of the JWT.
      - :rfc:`9126` and :rfc:`7519`.
    * - **iat**
      - UNIX Timestamp with the time of JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **challenge**
      - Challenge data obtained from ``nonce`` endpoint
      -
    * - **type**
      - It MUST be set to string "WalletAttestationRequest".
      -
    * - **hardware_signature**
      - The signature of ``client_data`` obtained using Wallet Hardware Key base64 encoded.
      -
    * - **integrity_assertion**
      - The integrity assertion obtained from the **Device Integrity Service** with the holder binding of ``client_data``.
      -
    * - **hardware_key_tag**
      - Unique identifier of the **Wallet Hardware Keys**
      -
    * - **cnf**
      - JSON object, containing the public part of an asymmetric key pair owned by the Wallet Instance.
      - :rfc:`7800`

.. _table_wallet_attestation_claim:

Wallet Attestation
~~~~~~~~~~~~~~~~~~

The JOSE header of the Wallet Attestation JWT MUST contain:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section `Cryptographic Algorithms <algorithms.html>`_ and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      -  Unique identifier of the ``jwk`` inside the ``cnf`` claim of Wallet Instance as base64url-encoded JWK Thumbprint value.
      - :rfc:`7638#section_3`.
    * - **typ**
      -  It MUST be set to ``wallet-attestation+jwt``
      -  `OPENID4VC-HAIP`_
    * - **trust_chain**
      - Sequence of Entity Statements that composes the Trust Chain related to the Relying Party.
      - `OIDC-FED`_ Section *3.2.1. Trust Chain Header Parameter*.

The body of the Wallet Attestation JWT MUST contain:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - Identifier of the Wallet Provider
      - :rfc:`9126` and :rfc:`7519`.
    * - **aud**
      - Identifier of the Wallet Provider concatenated with thumbprint of the Wallet Instance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **exp**
      - UNIX Timestamp with the expiry time of the JWT.
      - :rfc:`9126` and :rfc:`7519`.
    * - **iat**
      - UNIX Timestamp with the time of JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **type**
      - It MUST be set to string "WalletAttestation".
      -
    * - **cnf**
      - JSON object, containing the public part of an asymmetric key pair owned by the Wallet Instance.
      - :rfc:`7800`
    * - **aal**
      - JSON String asserting the authentication level of the Wallet and the key as asserted in the cnf claim.
      -
    * - **authorization_endpoint**
      - URL of the SIOPv2 Authorization Endpoint.
      -
    * - **response_types_supported**
      - JSON array containing a list of the OAuth 2.0 ``response_type`` values.
      -
    * - **response_modes_supported**
      - JSON array containing a list of the OAuth 2.0 "response_mode" values that this authorization server supports.
      - :rfc:`8414`
    * - **vp_formats_supported**
      - JSON object with name/value pairs, identifying a Credential format supported by the Wallet.
      -
    * - **request_object_signing_alg_values_supported**
      - JSON array containing a list of the JWS signing algorithms (alg values) supported.
      -
    * - **presentation_definition_uri_supported**
      - Boolean value specifying whether the Wallet Instance supports the transfer of presentation_definition by reference. MUST be set to false.
      -


.. _token endpoint: wallet-solution.html#wallet-attestation
.. _Wallet Attestation Request: wallet-attestation.html#format-of-the-wallet-attestation-request
.. _Wallet Attestation: wallet-attestation.html#format-of-the-wallet-attestation
.. _RFC 7523 section 4: https://www.rfc-editor.org/rfc/rfc7523.html#section-4
.. _RFC 8414 section 2: https://www.rfc-editor.org/rfc/rfc8414.html#section-2
.. _Wallet Provider metadata: wallet-solution.html#wallet-provider-metadata
.. _Key Attestation: https://developer.android.com/privacy-and-security/security-key-attestation
.. _Play Integrity API: https://developer.android.com/google/play/integrity?hl=it
.. _DeviceCheck: https://developer.apple.com/documentation/devicecheck

