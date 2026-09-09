.. include:: ../common/common_definitions.rst
.. Included via appendix.rst at title level '=' (document title).


Mobile Application Instance
===========================

The Wallet and Mobile Relying Party Instances share significant similarities, with particular respect to some aspects related to initialization and integrity validation. To eliminate redundancy, this section will use the term **Mobile Application Instance** to collectively refer to both. Within this framework, the **Application Provider** assumes the responsibilities of either the Wallet Provider or the Relying Party Backend, depending on the context.


Mobile Application Instance Initialization
------------------------------------------

The Initialization flow enables the Mobile Application Instance to register a long-lived key pair, securely stored in an appropriate secure storage within the device, with the Application Provider. This process occurs only after the Application Provider verifies the security and Key Attestation issued by the OS manufacturer.

The flow is displayed in :ref:`fig_MobileApplication_Instance_Initialization_Flow`, while a step-by-step description is provided below.

.. _fig_MobileApplication_Instance_Initialization_Flow:
.. plantuml:: plantuml/mobile-app-initialization.puml
    :width: 80%
    :alt: The figure illustrates the Mobile Application Instance Initialization Sequence Diagram.
    :caption: `Mobile Application Instance Initialization Sequence Diagram. <https://www.plantuml.com/plantuml/svg/VLFBRjiw4DtpAmQyYvi0xWy4Q94qYpPe2mJfOnN0695ZQM29L3b3j-xNbvHToBQ2R0XuT1vd7huLnQHvw0rcZI4F3INJiIVOnAXD_6tC_uy5mOv732e6dSO4zhjGie02MGfXd15WlyI6UuAxSUpPeN8Cy114CJYQ63YESCxuH7kuKoNH0_pkyK4EK5I1_sHC7Des4OLptgd5OuexzfJWFRej1J_n6xSrfYPyywwuti1dpC5re1q1pjpQ4-zGfw8nvJd2xpjoM-3DHF2qOqSm4AbCXO433ta08PSJwnuI_SoSQA2WyXmm-4fzgJV0H80xv1wRdewE9UiDF1M90WLhGwppidEsgPVo794VA52gzHawVJr6dwkUpYJczcQ9-xGVDRO9nuuTVCJaVs6Y6brWH4vmPMrthAwtj5-FkR5s1PVLn3jhhm-jYyRqcZ9ymtQXgzWMWNyPKQKsudgce6kFYkiEfOEtuBabqQkfnHLSIgpWCkprwI2hhZ7rFNgSph8IS5wNjS-XYJbuq0YJtO4vZtb10EFft6lUxxoMrP9QYyjvl782Fx1dlpY1vTUbqIdkQrtKYyQhvx3S-yMTrKq-KSkYQT8kFsICGSXS7fwdnT-iY6IXT0CFWPLBtZy73SdEaSWcz-QMWiz3_nS0>`_


.. .. figure:: ../../images/application_instance_initialization.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/VLFBRjiw4DtpAmQyYvi0xWy4Q94qYpPe2mJfOnN0695ZQM29L3b3j-xNbvHToBQ2R0XuT1vd7huLnQHvw0rcZI4F3INJiIVOnAXD_6tC_uy5mOv732e6dSO4zhjGie02MGfXd15WlyI6UuAxSUpPeN8Cy114CJYQ63YESCxuH7kuKoNH0_pkyK4EK5I1_sHC7Des4OLptgd5OuexzfJWFRej1J_n6xSrfYPyywwuti1dpC5re1q1pjpQ4-zGfw8nvJd2xpjoM-3DHF2qOqSm4AbCXO433ta08PSJwnuI_SoSQA2WyXmm-4fzgJV0H80xv1wRdewE9UiDF1M90WLhGwppidEsgPVo794VA52gzHawVJr6dwkUpYJczcQ9-xGVDRO9nuuTVCJaVs6Y6brWH4vmPMrthAwtj5-FkR5s1PVLn3jhhm-jYyRqcZ9ymtQXgzWMWNyPKQKsudgce6kFYkiEfOEtuBabqQkfnHLSIgpWCkprwI2hhZ7rFNgSph8IS5wNjS-XYJbuq0YJtO4vZtb10EFft6lUxxoMrP9QYyjvl782Fx1dlpY1vTUbqIdkQrtKYyQhvx3S-yMTrKq-KSkYQT8kFsICGSXS7fwdnT-iY6IXT0CFWPLBtZy73SdEaSWcz-QMWiz3_nS0

..     Mobile Application Instance Initialization Sequence Diagram


**Step 1**: The User starts the Mobile Application Instance for the first time.

**Step 2**: The Mobile Application Instance:

  * Checks whether the device meets the minimum security requirements (:ref:`WP_021 <wallet-instance-testcases>`).
  * Checks if the Key Attestation APIs is available (:ref:`WP_022 <wallet-instance-testcases>`).

.. note::
  **Federation Check**: The Mobile Application Instance needs to check if the Application Provider is part of the Federation, obtaining its protocol-specific Metadata (:ref:`WP_023 <wallet-instance-testcases>`). Non-normative examples of a response from the :ref:`wallet-provider-endpoint:Federation endpoint` with the **Entity Configuration** and the **Metadata** of the Application Provider are presented within the :ref:`wallet-provider-entity-configuration:Wallet Provider Entity Configuration` and :ref:`relying-party-entity-configuration:Relying Party Entity Configuration` sections.

**Steps 3-5 (Nonce Retrieval)**: The Mobile Application Instance requests a one-time ``nonce`` from the **Nonce Endpoint** of the Application Provider Backend (see :ref:`wallet-provider-endpoint:Wallet Solution Nonce Endpoint` or :ref:`relying-party-provider-backend-endpoint:Relying Party Provider Backend Nonce Endpoint`). This ``nonce`` MUST be unpredictable to serve as the main defense against replay attacks (:ref:`WP_131 <wallet-instance-optional-testcases>`).

Upon a successful request, the Application Provider generates and returns the ``nonce`` value to the Mobile Application Instance, as part of the :ref:`mobile-application-instance:Mobile Application Nonce Response`. The Application Provider MUST ensure that it is single-use and valid only within a specific time frame.

**Step 6**: The Mobile Application Instance, through the operating system, creates a pair of Cryptographic Hardware Keys and stores the corresponding Cryptographic Hardware Key Tag in local storage once the following requirements are met (:ref:`WP_132 <wallet-instance-optional-testcases>`):

  1. It MUST ensure that Cryptographic Hardware Keys do not already exist. If they do exist and the Application Instance is in the initialization phase, they MUST be deleted.
  2. It MUST generate a pair of asymmetric Elliptic Curve keys (``hardware_key_pub``, ``hardware_key_priv``) via a **Keystore**.
  3. It SHOULD obtain a unique identifier Cryptographic Hardware Key Tag (``hardware_key_tag``) for the generated Cryptographic Hardware Keys from the operating system. If the operating system permits specifying a tag during the creation of keys, then a random string for the ``hardware_key_tag`` MUST be selected. This random value MUST be collision-resistant and unpredictable to ensure security. To achieve this, consider using a cryptographic hash function or a secure random number generator provided by the operating system or a reputable cryptographic library.
  4. If the previous points are satisfied, it MUST store the ``hardware_key_tag`` in local storage.

.. note::
  **Keystore**: The Mobile Application Instance uses the device's hardware-backed **Keystore** for all cryptographic operations, including key generation, secure storage, and cryptographic processing. The Keystore is the default secure storage mechanism for all Digital Credentials except the PID:

  - **Android**: Strongbox Keymaster (a dedicated Hardware Security Module embedded in the device motherboard) is RECOMMENDED. The Trusted Execution Environment (TEE) MAY be used only when Strongbox is unavailable.
  - **iOS**: The Secure Enclave MUST be used.

  Given that each OEM offers a distinct SDK for accessing the Keystore, the discussion hereafter will address this topic in a general context.

  If the Keystore fails during any of these operations, for example due to hardware limitations, it will raise an error response to the Mobile Application Instance. The Mobile Application Instance MUST handle these errors accordingly to ensure secure operation. Details on error handling are left to the Mobile Application Instance implementation.

.. note::
  **WSCA/WSCD**: For PID issuance at Level of Assurance High, the Wallet Instance interacts with a **WSCA operating within a Remote WSCD** implemented as a remote Hardware Security Module (remote HSM) operated server-side. This ensures that PID private keys are generated and managed in a tamper-resistant remote hardware environment meeting the requirements for LoA High.

**Step 7**: The Mobile Application Instance uses the Key Attestation APIs, providing the ``client_data_hash`` to acquire the Key Attestation (:ref:`WP_133b <wallet-instance-optional-testcases>`).

.. note::
  **Key Attestation APIs**: In this section, the Key Attestation APIs is assumed to be provided by device manufacturers. This service allows the verification of a key being securely stored within the device's hardware through a signed object. Additionally, it offers verifiable proof that a specific Mobile Application Instance is authentic, unaltered, and in its original state using a specialized signed document made for this purpose.

  The service also incorporates details in the signed object, such as the device type, model, app version, operating system version, bootloader status, and other relevant information to assess whether the device has been compromised. Additionally Android devices may possess the *Key Attestation API*, a feature supported by *StrongBox Keymaster* (a physical HSM installed directly on the motherboard) or by the *TEE* (Trusted Execution Environment, a secure area of the main processor). *Key Attestation* aims to provide a way to strongly determine if a key pair is hardware-backed, what the properties of the key are, and what constraints are applied to its usage. For Apple devices, the Key Attestation API is represented by *DeviceCheck*, which provides a framework and server interface to manage device-specific data securely. *DeviceCheck* is used in combination with the *Secure Enclave*, a dedicated HSM integrated into Apple's SoCs. *DeviceCheck* can be used to attest to the integrity of the device, apps, and/or encryption keys generated on the device, ensuring they were created in a secure environment like *Secure Enclave*. Developers can leverage *DeviceCheck* functionality by using the framework itself.
  These services, specifically developed by the manufacturer, are integrated within the Android or iOS SDKs, eliminating the need for a predefined endpoint to access them. Additionally, as they are specifically developed for mobile architecture, they do not need to be registered as Federation Entities through national registration systems.
  *Secure Enclave* has been available on Apple devices since the iPhone 5s (2013).
  For Android devices, the inclusion of **Strongbox Keymaster** may vary by manufacturer, who decides whether to include it or not.

If any errors occur in the Key Attestation APIs process, such as device integrity verification, for example, due to unavailable Key Attestation APIss, an internal error, or an invalid nonce in the integrity request, the Key Attestation APIs raise an error response. The Mobile Application Instance MUST process these errors accordingly. Details on error handling are left to the Mobile Application Instance implementation.


**Step 8**: The Key Attestation APIs performs the following actions:

* Creates a Key Attestation that is linked with the provided ``client_data_hash`` and the public key of the Application Instance Hardware.
* Incorporates information pertaining to the device's security.
* Uses an OEM private key to sign the Key Attestation, therefore verifiable with the related OEM certificate, confirming that the Cryptographic Hardware Keys are securely managed by the operating system.

**Step 9 (Mobile Application Instance Initialization Request)**: The Mobile Application Instance sends a :ref:`mobile-application-instance:Mobile Application Instance Initialization Request` to the Application Provider, to initialize the Mobile Application Instance, identified by the Cryptographic Hardware Key public key. The request body includes the following claims: the ``nonce``, Key Attestation (``key_attestation``), and Cryptographic Hardware Key Tag (``hardware_key_tag``) as :ref:`WP_133 <wallet-instance-optional-testcases>`.

.. note::
  It is not necessary to send the Application Instance Hardware public key because it is already included in the ``key_attestation``.
  As seen in the previous steps, the Key Attestation APIs creates a Key Attestation linked to the provided ``client_data_hash`` which is the digest of the Application Provider's ``nonce``, the public key of the Application Instance Hardware and its Hardware Key Tag (:ref:`WP_133a <wallet-instance-optional-testcases>`).
  This process eliminates the need to send the Application Instance Hardware public key directly, as it is already included in the Key Attestation.

**Steps 10-12 (Mobile Application Instance Initialization Response)**: The Application Provider validates the ``nonce`` and ``key_attestation`` signature (:ref:`WP_135–137 <wallet-instance-optional-testcases>`), therefore:

  1. It MUST verify that the ``nonce`` was generated by Application Provider and has not already been used (:ref:`WP_135a <wallet-instance-optional-testcases>`).
  2. It MUST validate the ``key_attestation`` as defined by the device manufacturers' guidelines (:ref:`WP_135b <wallet-instance-optional-testcases>`). The Application Provider MUST also verify the binding between the received ``hardware_key_tag``, ``hardware_key_pub`` and ``nonce`` with the ``client_data_hash`` provided in the Key Attestation (:ref:`WP_136 <wallet-instance-optional-testcases>`).
  3. It MUST verify that the device in use has no security flaws and reflects the minimum security requirements defined by the Application Provider (:ref:`WP_135b <wallet-instance-optional-testcases>`).
  4. If these checks are passed, it MUST register the Mobile Application Instance, keeping the Cryptographic Hardware Key Tag (``hardware_key_tag``), the Public Hardware Key (``hardware_key_pub``) and possibly other useful information related to the device (:ref:`WP_137 <wallet-instance-optional-testcases>`).

Upon successful initialization of the Mobile Application Instance, the Application Provider responds with a confirmation of success (:ref:`mobile-application-instance:Mobile Application Instance Initialization Response` and :ref:`WP_135 <wallet-instance-optional-testcases>`).

.. note::
  The Application Provider might associate the Mobile Application Instance (through the ``hardware_key_tag`` identifier) with a specific User or Device  (:ref:`WP_138 <wallet-instance-optional-testcases>`). This uniquely identifies the User/Device within the Application Provider's systems and can be used for future revocations in the lifecycle of the Mobile Application Instance.

**Steps 13-14**: The Mobile Application Instance has been initialized.

.. note::
  **Threat Model**: while the initialization endpoint does not necessitate authenticating the client, it is safeguarded through the use of `key_attestation`. Proper validation of this attestation permits the initialization of authentic and unaltered app instances. Any other claims submitted will not undergo validation, leading the endpoint to respond with an error. Additionally, the inclusion of a nonce helps prevent replay attacks. The authenticity of both the nonce and the ``hardware_key_tag`` is ensured by the signature found within the ``key_attestation``.

Mobile Application Nonce Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Nonce Request uses the HTTP GET method.

Below is a non-normative example of a Nonce Request.

.. code-block:: http

    GET /nonce HTTP/1.1
    Host: application-provider.example.com

Mobile Application Nonce Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upon a successful request, the Application Provider returns an HTTP Response with a ``200 OK`` status code, with ``Content-Type`` set to ``application/json``.

The Nonce Response body contains the ``nonce`` value.

Below is a non-normative example of a Nonce Response.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "nonce": "d2JhY2NhbG91cmVqdWFuZGFt"
    }

Mobile Application Nonce Error Response
"""""""""""""""""""""""""""""""""""""""

If any errors occur, the Application Provider returns an error response. The response uses ``application/json`` as the ``Content-Type`` and includes the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered.

Below is a non-normative example of a Nonce Error Response.

.. code-block:: http

    HTTP/1.1 500 Internal Server Error
    Content-Type: application/json

    {
        "error": "server_error",
        "error_description": "The server encountered an unexpected error."
    }

The following table lists HTTP Status Codes and related error codes that are supported for the error response:

.. list-table::
    :class: longtable
    :widths: 30 20 50
    :header-rows: 1

    * - **HTTP Status Code**
      - **Error Code**
      - **Description**
    * - ``500 Internal Server Error``
      - ``server_error``
      - The request cannot be fulfilled because the Nonce Endpoint encountered an internal problem.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The request cannot be fulfilled because the Nonce Endpoint is temporarily unavailable (e.g., due to maintenance or overload).

Mobile Application Instance Initialization Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Instance Initialization Request uses the HTTP POST method with ``Content-Type`` set to ``application/json``.

The Instance Initialization Request body contains the following claims:


.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **nonce**
      - It MUST be set to the value obtained from the Application Provider through the Nonce Endpoint.
      - This specification.
    * - **hardware_key_tag**
      - The unique identifier of the **Cryptographic Hardware Keys** and encoded in ``base64url``.
      - This specification.
    * - **key_attestation**
      - An attestation that guarantees the secure generation, storage and usage of the key pair generated by the Mobile Application Instance. This can be an array containing a certificate chain whose leaf certificate is the Key Attestation obtained from the device **Key Attestation APIs**, signed with the device hardware key.
      - This specification.

Below is a non-normative example of an Instance Initialization Request.

.. code-block:: http

    POST /instance-initialization HTTP/1.1
    Host: application-provider.example.com
    Content-Type: application/json

    {
      "nonce": "d2JhY2NhbG91cmVqdWFuZGFt",
      "key_attestation": "o2NmbXRvYXBwbGUtYXBw... redacted",
      "hardware_key_tag": "WQhyDymFKsP95iFqpzdEDWW4l7aVna2Fn4JCeWHYtbU="
    }


Mobile Application Instance Initialization Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If an Instance Initialization Request is successfully validated, the Application Provider provides an HTTP Response with status code ``204 No Content``.

Below is a non-normative example of an Instance Initialization Response.

.. code-block:: http

    HTTP/1.1 204 No content


Mobile Application Instance Initialization Error Response
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

If any errors occur, the Application Provider returns an error response. The response uses ``application/json`` as the ``Content-Type`` and includes the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered (:ref:`WP_035 <wallet-instance-testcases>`).

Below is a non-normative example of an Instance Initialization Error Response.

.. code-block:: http

    HTTP/1.1 403 Forbidden
    Content-Type: application/json
    Cache-Control: no-store

    {
        "error": "forbidden",
        "error_description": "The provided nonce is invalid, expired, or already used."
    }

The following table lists HTTP Status Codes and related error codes that are supported for the error response (:ref:`WP_036–040 <wallet-instance-testcases>`):

.. list-table::
    :class: longtable
    :widths: 20 20 50
    :header-rows: 1

    * - **HTTP Status Code**
      - **Error Code**
      - **Description**
    * - ``400 Bad Request``
      - ``bad_request``
      - The request is malformed, missing required parameters, or includes invalid and unknown parameters.
    * - ``403 Forbidden``
      - ``integrity_check_error``
      - The device does not meet the Application Provider's minimum security requirements.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The provided nonce is invalid, expired, or already used.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The signature of the Key Attestation is invalid.
    * - ``422 Unprocessable Content`` [OPTIONAL]
      - ``validation_error``
      - The request does not adhere to the required format.
    * - ``500 Internal Server Error``
      - ``server_error``
      - An internal error occurred while processing the request.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The service is unavailable. Please try again later.


.. Mobile Application Key Binding
.. ------------------------------

.. The Key Binding flow enables the Mobile Application Instance to bind a newly created pair of keys to the Mobile Application Instance, by relying on a proof of possession of the Cryptographic Hardware Keys generated during the :ref:`mobile-application-instance:Mobile Application Instance Initialization` phase. Before completing the process, the Application Provider also needs to verify the integrity of the Mobile Application Instance.

.. Although the exact flow differs depending on the context (see the :ref:`relying-party-instance:Mobile Relying Party Instance Registration` and :ref:`wallet-attestation-issuance:Wallet App Attestation Issuance` sections), the Mobile Application Integrity Request and Error Response are consistent.


.. Mobile Application Key Binding Request
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. The Key Binding Request uses the HTTP POST method with ``Content-Type`` set to ``application/json``.

.. The Key Binding Request body contains an ``assertion`` parameter whose value is a signed JWT including all header parameters and body claims described below (:ref:`WP_134 <wallet-instance-optional-testcases>`).

.. Below is a non-normative example of a Key Binding Request.

.. .. code-block:: http

 ..   POST /key-binding HTTP/1.1
    Host: application-provider.example.org
    Content-Type: application/json

    {
      "assertion": "eyJhbGciOiJFUzI1NiIsImtpZCI6ImtoakZWTE9nRjNHeG..."
    }

.. In particular, the Key Binding Request JWT includes the following HTTP header parameters:

.. .. _table_key_binding_request_claim:
 .. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

..    * - **Parameter**
      - **Description**
      - **Reference**
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the :ref:`algorithms:cryptographic algorithms` and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - [:rfc:`7516#section-4.1.1`]
    * - **kid**
      - Thumbprint of the Mobile Application Instance's JWK contained in the ``cnf`` claim.
      - [:rfc:`7638#section_3`]
    * - **typ**
      - The type of the JWT, which can assume different values depending on the context.
      -

.. The Key Binding Request JWT includes the following body claims:

..
  .. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - The identifier of the Application Provider concatenated with the thumbprint of the JWK in the ``cnf`` claim.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **aud**
      - The identifier of the Application Provider.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **exp**
      - UNIX timestamp representing the JWT expiration time.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **iat**
      - UNIX timestamp representing the JWT issuance time.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **nonce**
      - The ``nonce`` obtained from the Nonce Endpoint.
      -
    * - **hardware_signature**
      - The signature of ``client_data`` obtained using the Cryptographic Hardware Key, encoded in the ``base64url`` format.
      -
    * - **integrity_assertion**
      - The Integrity Assertion obtained from the **Device Integrity Service APIs** with the holder binding of ``client_data``.
      -
    * - **hardware_key_tag**
      - The value of the Cryptographic Hardware Key Tag.
      -
    * - **cnf**
      - JSON object containing the public part of an asymmetric key pair owned by the Mobile Application Instance.
      - :rfc:`7800`.

.. Below is a non-normative example of a Key Binding Request JWT header and payload.


..
 .. code-block:: json

 ..   {
      "alg": "ES256",
      "kid": "hT3v7KQjFZy6GvDkYgOZ1u2F6T4Nz5bPjX8o1MZ3dJY",
      "typ": "..."
    }

.. .. code-block:: json

 ..   {
      "iss": "https://application-provider.example.org/instance/hT3v7KQjFZy6GvDkYgOZ1u2F6T4Nz5bPjX8o1MZ3dJY",
      "sub": "https://application-provider.example.org/",
      "nonce": "f3b29a81-45c7-4d12-b8b5-e1f6c9327aef",
      "hardware_signature": "KoZIhvcNAQcCoIAwgAIB...",
      "integrity_assertion": "o2NmbXRvYXBwbGUtYXBwYXNzZXJ0aW9uLXBheWxvYWQtYXBw...",
      "hardware_key_tag": "QW12DylRTmF89iGkpydNDWW7m8bVpa2Fn9KBeXGYtfX"
      "cnf": {
        "jwk": {
          "crv": "P-256",
          "kty": "EC",
          "x": "8FJtI-yr3pjyRKGMnz4WmdnQD_uJSq4R95Nj98b44",
          "y": "MKZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg"
        }
      }
    }


.. Mobile Application Key Binding Response
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. The Key Binding Response strictly depends on the context of the request; further details are provided in the :ref:`relying-party-provider-backend-endpoint:Relying Party Provider Backend Key Binding Response` and :ref:`wallet-provider-endpoint:Wallet App Attestation Issuance Response` sections.


.. Mobile Application Key Binding Error Response
.. """""""""""""""""""""""""""""""""""""""""""""

.. If any errors occur, the Application Provider returns an error response. The response uses ``application/json`` as the ``Content-Type`` and includes the following parameters:

  .. - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered (:ref:`WP_035 <wallet-instance-testcases>`).

.. Below is a non-normative example of a Key Binding Error Response.

.. .. code-block:: http
..
    HTTP/1.1 403 Forbidden
    Content-Type: application/json

    {
      "error": "invalid_request",
      "error_description": "The provided challenge is invalid, expired, or already used."
    }

.. The following table lists HTTP Status Codes and related error codes that are supported for the error response, unless otherwise specified  (:ref:`WP_036–0339 <wallet-instance-testcases>` and :ref:`WP_150–155 <wallet-instance-optional-testcases>`):
..
 .. list-table::
    :class: longtable
    :widths: 30 20 50
    :header-rows: 1

    * - **HTTP Status Code**
      - **Error Code**
      - **Description**
    * - ``400 Bad Request``
      - ``bad_request``
      - The request is malformed, missing required parameters (e.g., header parameters or Integrity Assertion), or includes invalid and unknown parameters.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The Mobile Application Instance has been revoked.
    * - ``403 Forbidden``
      - ``integrity_check_error``
      - The device does not meet the Application Provider's minimum security requirements.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The signature of the Integrity Request is invalid or does not match the associated public key (JWK).
    * - ``403 Forbidden``
      - ``invalid_request``
      - The Integrity Assertion validation failed; the Integrity Assertion is tampered with or improperly signed.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The provided ``nonce`` is invalid, expired, or already used.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The Proof of Possession (``hardware_signature``) is invalid.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The ``iss`` parameter does not match the Application Provider's expected URL identifier.
    * - ``404 Not Found``
      - ``not_found``
      - The Mobile Application Instance was not found.
    * - ``422 Unprocessable Content`` [OPTIONAL]
      - ``validation_error``
      - The request does not adhere to the required format.
    * - ``500 Internal Server Error``
      - ``server_error``
      - An internal server error occurred while processing the request.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The service is unavailable. Please try again later.


