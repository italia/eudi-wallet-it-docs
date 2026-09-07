.. include:: ../common/common_definitions.rst
.. Included via endpoints.rst at title level '-' (level 1).

.. role:: raw-html(raw)
  :format: html


Wallet Provider Endpoints
-------------------------

The Wallet Provider, responsible for delivering a Wallet Solution, MUST expose the endpoints to support trust establishment and essential Wallet Instance functionalities. These include the ``/.well-known/openid-federation`` Federation Endpoint which MUST adhere to the OpenID Federation 1.0 specification to reliably establish trust with the Wallet Provider's as well as, endpoints for Wallet Instance registration, nonce generation (required for registration), attestation issuance, and revocation. Aside from the Federation endpoint, the implementation details of the others are left to the Wallet Provider's discretion.

.. note::
  Tests related to the use of Wallet Provider endpoints are defined in
  :ref:`test-plans-wallet-provider:Wallet Provider Test Matrix`, particularly
  :ref:`wallet-provider-backend-testcases`,
  :ref:`wallet-instance-testcases`, and
  :ref:`wallet-instance-optional-testcases`.

Federation Endpoint
^^^^^^^^^^^^^^^^^^^

The ``/.well-known/openid-federation`` endpoint serves as the discovery mechanism for trust establishment by retrieving the Wallet Provider Entity Configuration.

See Section :ref:`wallet-provider-entity-configuration:Wallet Provider Entity Configuration` for technical details (:ref:`WP_001–004 <wallet-provider-backend-testcases>`).


Wallet Solution Nonce Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a RESTful API endpoint that allows the Wallet Instance to request a cryptographic nonce from the Wallet Provider. The nonce serves as an unpredictable, single-use challenge to ensure freshness and prevent replay attacks.

See :ref:`mobile-application-instance:Mobile Application Nonce Request` and :ref:`mobile-application-instance:Mobile Application Nonce Response` for details on the Nonce Request and Nonce Response (:ref:`WP_131 <wallet-instance-optional-testcases>`).

Wallet Instance Management Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These are RESTful API endpoints provided by the Wallet Provider that enables Wallet Instance management, including registration, status retrieval, revocation upon request (e.g., by the User), and deletion.
The following sections describe the registration, status retrieval and revocation requests, along with their corresponding responses, handled by this endpoint, which are required for core :ref:`wallet-instance-functionalities:Wallet Instance Functionalities`.

Wallet Instance Registration Request
"""""""""""""""""""""""""""""""""""""

To register a Wallet Instance, the request to the Wallet Provider MUST use the HTTP POST method with ``Content-Type`` set to `application/json`. The request body MUST contain the claims described in :ref:`mobile-application-instance:Mobile Application Instance Initialization Request` (:ref:`WP_131–134 <wallet-instance-optional-testcases>`).

Wallet Instance Registration Response
"""""""""""""""""""""""""""""""""""""""""

If a Wallet Instance Registration Request is successfully validated, the Wallet Provider provides an HTTP Response with status code 204 (No Content). For detatails see :ref:`mobile-application-instance:Mobile Application Instance Initialization Response` (:ref:`WP_135–137 <wallet-instance-optional-testcases>`).

Wallet Instance Retrieval Request
"""""""""""""""""""""""""""""""""""

To retrieve all Wallet Instances associated with a User, a request MUST be sent using the HTTP GET method to the Wallet Provider (:ref:`WP_145 <wallet-instance-optional-testcases>`).

.. note::
  For retrieving a specific Wallet Instance, the request MUST include the Wallet Instance ID as a path parameter.


Wallet Instance Retrieval Response
"""""""""""""""""""""""""""""""""""

If a Wallet Instance Retrieval Request is successfully processed, the Wallet Provider MUST return an HTTP Response with a 200 (OK) status code.
The response body MUST be in JSON format and include the relevant Wallet Instance information, such as its unique ID, status, and issuance date.
When retrieving all Wallet Instances, the response MUST return an array containing the details of all associated instances (:ref:`WP_146 <wallet-instance-optional-testcases>`).

If any errors occur during the retrieval process, an error response MUST be returned. Refer to :ref:`wallet-provider-endpoint:Error Handling for Wallet Instance Management` for details on error codes and descriptions.

Below is a non-normative example of an error response:

.. code-block:: http

   HTTP/1.1 403 Forbidden
   Content-Type: application/json
   Cache-Control: no-store

   {
     "error": "forbidden",
     "error_description": "User is not authorized to retrieve Wallet Instances."
   }


Wallet Instance Revocation Request
""""""""""""""""""""""""""""""""""

To revoke an active Wallet Instance, a revocation request MUST be sent using the HTTP PATCH method with Content-Type set to ``application/json``. The request body MUST contain a ``status`` parameter set to ``REVOKED`` (:ref:`WP_147 <wallet-instance-optional-testcases>`).

.. note::
  While PATCH is the recommended method, the revocation request MAY also be sent using the POST method, depending on implementation preferences.

Wallet Instance Revocation Response
"""""""""""""""""""""""""""""""""""

If a Wallet Instance Revocation Request is successfully processed, the Wallet Provider provides an HTTP Response with a 204 (No Content) status code (:ref:`WP_148 <wallet-instance-optional-testcases>`).

If any errors occur during the Wallet Instance Revocation, an error response MUST be returned. Refer to :ref:`wallet-provider-endpoint:Error Handling for Wallet Instance Management` for details on error codes and descriptions (:ref:`WP_035–039, WP_043–044 <wallet-instance-testcases>`).

Below is a non-normative example of an error response:

.. code-block:: http

   HTTP/1.1 400 Bad Request
   Content-Type: application/json
   Cache-Control: no-store

   {
     "error": "bad_request",
     "error_description": "The request is missing status parameter."
   }

Error Handling for Wallet Instance Management
"""""""""""""""""""""""""""""""""""""""""""""""

To ensure robustness and security, the Wallet Provider MUST handle errors consistently across all Wallet Instance Management requests, including Registration, Retrieval, and Revocation.

In case of an error, the Wallet Provider MUST return an error response as defined in :rfc:`7231`, with additional details available in :rfc:`7807`. The response MUST use the Content-Type set to ``application/json`` and MUST include the following parameters:

- *error*. The error code.
- *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered.

The following sections categorize errors into **common errors**, which apply to all requests, and **request-specific errors**, which are relevant to particular operations (:ref:`WP_035–044 <wallet-instance-testcases>`, and :ref:`WP_150–155 <wallet-instance-optional-testcases>`).

Common Error Responses
"""""""""""""""""""""""

The following errors apply to all Wallet Instance Management operations (Registration, Retrieval, and Revocation), and MUST be supported for the error response, unless otherwise specified (:ref:`WP_035–039 <wallet-instance-testcases>`):

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
   * - ``422 Unprocessable Content`` [OPTIONAL]
     - ``validation_error``
     - The request does not adhere to the required format.
   * - ``500 Internal Server Error``
     - ``server_error``
     - An internal error occurred while processing the request.
   * - ``503 Service Unavailable``
     - ``temporarily_unavailable``
     - The service is unavailable. Please try again later.

Request-Specific Error Responses
"""""""""""""""""""""""""""""""""

The errors in :ref:`mobile-application-instance:Mobile Application Instance Initialization Error Response` MUST be supported for error responses related to **Wallet Instance Registration**.

The following errors MUST be supported for error responses related to **Wallet Instance Retrieval** (:ref:`WP_041–042 <wallet-instance-testcases>`):

.. list-table::
   :class: longtable
   :widths: 20 20 50
   :header-rows: 1

   * - **HTTP Status Code**
     - **Error Code**
     - **Description**
   * - ``403 Forbidden``
     - ``forbidden``
     - The user does not have permission to retrieve this Wallet Instance.
   * - ``401 Unauthorized``
     - ``unauthorized``
     - The request lacks valid authentication credentials.

The following errors MUST be supported for error responses related to **Wallet Instance Revocation** (:ref:`WP_043–044 <wallet-instance-testcases>`):

.. list-table::
   :class: longtable
   :widths: 20 20 50
   :header-rows: 1

   * - **HTTP Status Code**
     - **Error Code**
     - **Description**
   * - ``403 Forbidden``
     - ``invalid_request``
     - The user does not have permission to revoke this Wallet Instance.
   * - ``401 Unauthorized``
     - ``unauthorized``
     - The request cannot be authenticated or authorized.

Wallet Instance Attestation Issuance Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a RESTful API endpoint provided by the Wallet Provider that enables the Wallet Instance to obtain Wallet Instance Attestation, by sending a Wallet Instance Attestation Issuance Request.

Wallet Instance Attestation Issuance Request
"""""""""""""""""""""""""""""""""""""""""""""

The Wallet Instance Attestation Issuance Request uses the HTTP POST method with ``Content-Type`` set to ``application/json``. (:ref:`WP_026 <wallet-instance-testcases>` and :ref:`WP_140–142 <wallet-instance-optional-testcases>`).

The ``typ`` header of the Wallet Instance Attestation Issuance Request JWT assumes the value ``wia-request+jwt``.

The Wallet Instance Attestation Issuance Request body contains an ``assertion`` parameter whose value is a signed JWT including all header parameters and body claims described below.

Below is a non-normative example of a Wallet Instance Attestation Request.

.. code-block:: http

    POST /wallet-instance-attestation HTTP/1.1
    Host: application-provider.example.org
    Content-Type: application/json

    {
      "assertion": "eyJpc3MiOiJPbnNpYW5kcklqcDdJbU55ZGlJNklsQ..."
    }

In particular, the Wallet Instance Attestation Issuance JWT includes the following HTTP header parameters:

.. _table_wia_request_claim:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the :ref:`algorithms:cryptographic algorithms` and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - [:rfc:`7516#section-4.1.1`]
    * - **kid**
      - Thumbprint of the Wallet Instance's JWK contained in the ``cnf`` claim.
      - [:rfc:`7638#section_3`]
    * - **typ**
      - The type of the JWT, it MUST set to ``wia-request+jwt``.
      -

The Wallet Instance Attestation Request JWT includes the following body claims:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - String containing the unique identifier of the Wallet Instance.
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
      - The signature of ``client_data_hash`` obtained using the Cryptographic Hardware Key, encoded in the ``base64url`` format.
      -
    * - **integrity_assertion**
      - The Integrity Assertion for Wallet Instance Attestation obtained from the **Device Integrity Service APIs** with the holder binding of ``client_data_hash``.
      -
    * - **hardware_key_tag**
      - The value of the Cryptographic Hardware Key Tag.
      -
    * - **cnf**
      - JSON object containing the public part of an asymmetric key pair owned by the Wallet Instance.
      - :rfc:`7800`.
    * - **platform**
      - String containing the value of the device operating system.
      -
    * - **wallet_solution_id**
      - String containing the identifier of the Wallet Solution.
      -
    * - **wallet_solution_version**
      - String containing the version of the Wallet Solution.
      -


Below is a non-normative example of a Wallet Instance Attestation Request JWT header and payload.

.. code-block:: json

    {
      "alg": "ES256",
      "kid": "OnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiL",
      "typ": "wia-request+jwt"
    }

.. code-block:: json

    {
      "iss": "OnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiL",
      "nonce": "f3b29a81-45c7-4d12-b8b5-e1f6c9327aef",
      "hardware_signature": "KoZIhvcNAQcCoIAwgAIB...",
      "integrity_assertion": "o2NmbXRvYXBwbGUtYXBwYXNzZXJ0aW9uLXBheWxvYWQtYXBw...",
      "hardware_key_tag": "QW12DylRTmF89iGkpydNDWW7m8bVpa2Fn9KBeXGYtfX",
      "cnf": {
        "jwk": {
          "crv": "P-256",
          "kty": "EC",
          "x": "8FJtI-yr3pjyRKGMnz4WmdnQD_uJSq4R95Nj98b44",
          "y": "MKZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg"
        }
      },
      "platform": "iOS",
      "wallet_solution_id": "Wallet-mobile",
      "wallet_solution_version": "1.1.0"
    }


Wallet Instance Attestation Issuance Response
""""""""""""""""""""""""""""""""""""""""""""""

If the Wallet Instance Attestation Issuance Request is successfully validated, the Wallet Provider returns an HTTP response with a status code of ``200 OK`` and ``Content-Type`` ``application/json``. The returned JSON Object includes ``wallet_instance_attestation`` (see :ref:`wallet-instance-attestation-issuance:Wallet Instance Attestation Issuance`). ``wallet_instance_attestation`` is signed by the Wallet Provider (:ref:`WP_027–029 <wallet-instance-testcases>` and :ref:`WP_143–144 <wallet-instance-optional-testcases>`). The JWT formatted Wallet Instance Attestation is to be used for the Issuance phase, as an OAuth Client Attestation, and will be sent to the Credential Issuer as discussed in :ref:`credential-issuance:Digital Credential Issuance`.


The JSON Object returned in the response has the following claim:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **wallet_instance_attestation**
      - REQUIRED. A String containing of the issued Wallet Instance Attestation.
      - This specification.

The value of ``wallet_instance_attestation`` parameter is a string representing the Wallet Instance Attestation in a JWT.

If any errors occur during the process, an error response is returned. The response uses ``application/json`` as the ``Content-Type`` and includes the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered (:ref:`WP_035 <wallet-instance-testcases>`).

Below is a non-normative example of a Wallet Instance Attestation Issuance Response.

.. code-block:: http

    HTTP/1.1 403 Forbidden
    Content-Type: application/json

    {
      "error": "invalid_request",
      "error_description": "The provided challenge is invalid, expired, or already used."
    }

The following table lists HTTP Status Codes and related error codes that are supported for the error response, unless otherwise specified  (:ref:`WP_036–039 <wallet-instance-testcases>` and :ref:`WP_150–155 <wallet-instance-optional-testcases>`):

.. list-table::
    :class: longtable
    :widths: 30 20 50
    :header-rows: 1

    * - **HTTP Status Code**
      - **Error Code**
      - **Description**
    * - ``400 Bad Request``
      - ``bad_request``
      - The request is malformed, missing required parameters (e.g., header parameters, or Integrity Assertion), or includes invalid and unknown parameters.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The Wallet Instance has been revoked.
    * - ``403 Forbidden``
      - ``integrity_check_error``
      - The device does not meet the Wallet Provider's minimum security requirements.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The signature of the Wallet Instance Attestation Request is invalid or does not match the associated public key (JWK).
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
      - The ``iss`` parameter does not match the Wallet Provider's expected URL identifier.
    * - ``404 Not Found``
      - ``not_found``
      - The Wallet Instance was not found.
    * - ``422 Unprocessable Content`` [OPTIONAL]
      - ``validation_error``
      - The request does not adhere to the required format.
    * - ``500 Internal Server Error``
      - ``server_error``
      - An internal server error occurred while processing the request.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The service is unavailable. Please try again later.


Wallet Instance Attestation JWT
""""""""""""""""""""""""""""""""

The JOSE header of the Wallet Instance Attestation JWT contains the following parameters:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **alg**
      - REQUIRED. A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section :ref:`algorithms:cryptographic algorithms` and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      - REQUIRED. Unique identifier of the public key associated to the private key the Wallet Provider used to sign the Wallet Instance Attestation.
      - :rfc:`7638#section_3`.
    * - **typ**
      - REQUIRED. It MUST be set to ``oauth-client-attestation+jwt``
      - `OPENID4VC-HAIP`_.
    * - **trust_chain**
      - OPTIONAL. Sequence of Entity Statements that composes the Trust Chain related to the Wallet Provider.
      - `OID-FED`_ Section 4.3 *Trust Chain Header Parameter*.
    * - **x5c**
      - REQUIRED. Contains the X.509 public key certificate or certificate chain (:rfc:`5280`) corresponding to the key used to digitally sign the JWT.
      - :rfc:`7515` Section 4.1.8, `SD-JWT-VC`_ Section 3.5 and `OPENID4VC-HAIP`_.

The body of the Wallet Instance Attestation JWT contains the following claims:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **exp**
      - REQUIRED. UNIX Timestamp with the expiry time of the JWT. This should be set to the maximum of 24 hours.
      - :rfc:`9126` and :rfc:`7519` and `EUDI-TS 3`_.
    * - **nbf**
      - OPTIONAL. UNIX Timestamp with the start time of validity of the JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **cnf**
      - REQUIRED. JSON object, containing the public part of an asymmetric key pair owned by the Wallet Instance.
      - :rfc:`7800`.
    * - **wallet_link**
      - REQUIRED. String containing a URL to get further information about the Wallet and the Wallet Provider.
      - `OpenID4VCI`_.
    * - **wallet_name**
      - REQUIRED. String containing a human-readable name of the Wallet.
      - `OpenID4VCI`_.
    * - **wallet_version**
      - REQUIRED. String value of the Wallet Solution version.
      - `OpenID4VCI`_ and `EUDI-TS 3`_.
    * - **wallet_solution_certification_information**
      - OPTIONAL. String value that contains a URL that links to the certification of the Wallet Solution.
      - `EUDI-TS 3`_.
    * - **client_status**
      - REQUIRED. Status mechanism for the Wallet Attestation.

        - **status**: REQUIRED. a status list reference as specified in Appendix E of `OpenID4VCI`_. The value represents the revocation state of the Wallet Instance.
        - **exp**: REQUIRED. UNIX Timestamp specifying the time until which the Wallet Provider commits to maintaining the revocation status at the status list index referenced in ``status``.
      - `EUDI-TS 3`_.
    * - **sub**
      - REQUIRED. Identifier of the Wallet Instance, which is the unique identifier of Wallet Solution in URL format.
      - `EUDI-TS 3`_.


Below is a non-normative example of the Wallet Instance Attestation JWT header and payload, without encoding and signature applied:

.. literalinclude:: ../../examples/wa-jwt_example_header.json
  :language: JSON

.. literalinclude:: ../../examples/wa-jwt_example_payload.json
  :language: JSON


.. note::
    As the certification scheme has not yet been defined, the exact content of ``wallet_solution_certification_information`` is undefined. This content will be defined in a future update.


.. note::
    As a revocation mechanism for WIA, the per-issuer reuse option described in Section 2.5.1 of `EUDI-TS 3`_ is preferred.


.. note::
    The ``iss`` claim is not needed anymore in the WIA body as Wallet Provider identity is now inferred from the signing certificate in the ``x5c`` JOSE header parameter.




Key Attestation Issuance Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a RESTful API endpoint provided by the Wallet Provider that enables the Wallet Instance to obtain Key Attestation, by sending a Key Attestation Issuance Request.

Key Attestation Issuance Request
"""""""""""""""""""""""""""""""""""""""""""""

The Key Attestation Issuance Request uses the HTTP POST method with ``Content-Type`` set to ``application/json``. (:ref:`WP_026 <wallet-instance-testcases>` and :ref:`WP_140–142 <wallet-instance-optional-testcases>`).

The ``typ`` header of the Key Attestation Issuance Request JWT assumes the value ``ka-request+jwt``.

The Key Attestation Issuance Request body contains an ``assertion`` parameter whose value is a signed JWT including all header parameters and body claims described below.

Below is a non-normative example of a Key Attestation Request.

.. code-block:: http

    POST /key-attestation HTTP/1.1
    Host: application-provider.example.org
    Content-Type: application/json

    {
      "assertion": "eyJpc3MiOiJPbnNpYW5kcklqcDdJbU55ZGlJNklsQ..."
    }

In particular, the Key Attestation Issuance JWT includes the following HTTP header parameters:

.. _table_ka_request_claim:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the :ref:`algorithms:cryptographic algorithms` and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - [:rfc:`7516#section-4.1.1`]
    * - **kid**
      - Thumbprint of the Wallet Instance's JWK contained in the ``cnf`` claim.
      - [:rfc:`7638#section_3`]
    * - **typ**
      - The type of the JWT, it MUST be set to ``ka-request+jwt``.
      -

The Key Attestation Request JWT includes the following body claims:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - String containing the unique identifier of the Wallet Instance.
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
    * - **keys_to_attest**
      - JSON array of JWT strings, each representing a ``Key_Attestation_Requests``.
      -
    * - **hardware_signature**
      - The signature of ``client_data_hash`` obtained using the Cryptographic Hardware Key, encoded in the ``base64url`` format.
      -
    * - **integrity_assertion**
      - The Integrity Assertion for Wallet Instance Attestation obtained from the **Device Integrity Service APIs** with the holder binding of ``client_data_hash``.
      -
    * - **hardware_key_tag**
      - The value of the Cryptographic Hardware Key Tag.
      -
    * - **cnf**
      - JSON object containing the public part of the first asymmetric key pair (first element of ``keys_to_attest``) owned by the Wallet Instance.
      - :rfc:`7800`.
    * - **platform**
      - String containing the value of the device operating system.
      -
    * - **wallet_solution_id**
      - String containing the identifier of the Wallet Solution.
      -
    * - **wallet_solution_version**
      - String containing the version of the Wallet Solution.
      -


Below is a non-normative example of a Key Attestation Request JWT header and payload.


.. code-block:: json

    {
      "alg": "ES256",
      "kid": "OnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiL",
      "typ": "ka-request+jwt"
    }

.. code-block:: json

    {
      "iss": "OnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiL",
      "nonce": "f3b29a81-45c7-4d12-b8b5-e1f6c9327aef",
      "hardware_signature": "KoZIhvcNAQcCoIAwgAIB...",
      "integrity_assertion": "o2NmbXRvYXBwbGUtYXBwYXNzZXJ0aW9uLXBheWxvYWQtYXBw...",
      "hardware_key_tag": "QW12DylRTmF89iGkpydNDWW7m8bVpa2Fn9KBeXGYtfX",
      "cnf": {
        "jwk": {
          "crv": "P-256",
          "kty": "EC",
          "x": "8FJtI-yr3pjyRKGMnz4WmdnQD_uJSq4R95Nj98b44",
          "y": "MKZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg"
        }
      },
      "keys_to_attest": [
        "eyJ0eXAiOiJrZXktYXR0ZXN0YXRpb24tcmVxdWVzdCtqd3QiLCJhbGciOiJFUzI1NiIsImtpZCI6Ik9LSEhrVk5PckthUFZKdWZsREt3MVNRSEZOWTVpeTlPaXdBdHBBMGNvSUEifQ.eyJ3c2NkX2tleV9hdHRlc3RhdGlvbiI6eyJzdG9yYWdlX3R5cGUiOiJMT0NBTF9OQVRJVkUifSwiY25mIjp7Imp3ayI6eyJrdHkiOiJFQyIsIngiOiJ4QUg5U05mYXE5SjVkbWt6WFlRTGVrNVlmcFBjOGlfUHBNUlQzMTVoak1rIiwieSI6IlBFMlhMY3BXNmVYSDRGbFlHTlA5Qmh3UVFkRWlaRTF0QWRULUVpaEFDQzgiLCJjcnYiOiJQLTI1NiIsImtpZCI6Ik9LSEhrVk5PckthUFZKdWZsREt3MVNRSEZOWTVpeTlPaXdBdHBBMGNvSUEifX0sImlhdCI6MTc3MzA1Mzg2MSwiZXhwIjoxNzczMDU3NDYxfQ.Rn3D0GwYYZJaupzJ6617V0xav_HH6bGnttoGrD4lwY8ICPH9NiEbTF9ZBYD3aHh20Z9GCjQ8Fhit5Fbps8v9Aw",
        "eyJ0eXAiOiJrZXktYXR0ZXN0YXRpb24tcmVxdWVzdCtqd3QiLCJhbGciOiJFUzI1NiIsImtpZCI6IkViUUJSQ2dLNWJrVzlZNU1idGEwZlpzMVdhVTBLZVpiek9iTXVvY2NLb28ifQ.eyJ3c2NkX2tleV9hdHRlc3RhdGlvbiI6eyJzdG9yYWdlX3R5cGUiOiJMT0NBTF9OQVRJVkUifSwiY25mIjp7Imp3ayI6eyJrdHkiOiJFQyIsIngiOiJEVVFWTGhLMUtRUmQtZ3g3UU5jYVNhWENnOXg0S3R6QmstNWIxWTNkeWU0IiwieSI6IkZxVjk0TWVrVm5fQ05mNTIxdm1vLVFIcWZObk12eGdIR3NFeDlCTlc4aFEiLCJjcnYiOiJQLTI1NiIsImtpZCI6IkViUUJSQ2dLNWJrVzlZNU1idGEwZlpzMVdhVTBLZVpiek9iTXVvY2NLb28ifX0sImlhdCI6MTc3MzA1Mzg2MSwiZXhwIjoxNzczMDU3NDYxfQ.wIYOmX8-dmuRnuaCVg1kFoTHhsvv01vbapQ8-3er-HIiAF819Kt3Uy0PUN_WgxP7eWMGwhkn_9tQnnhdgXLYyw"
      ],
      "platform": "iOS",
      "wallet_solution_id": "Wallet-mobile",
      "wallet_solution_version": "1.1.0"
    }


Key Attestation Issuance Response
""""""""""""""""""""""""""""""""""""""""""

If the Key Attestation Issuance Request is successfully validated, the Wallet Provider returns an HTTP response with a status code of ``200 OK`` and ``Content-Type`` ``application/json``. The returned JSON Object includes ``key_attestation`` (see :ref:`wallet-attestation-issuance:Key Attestation Issuance`). ``key_attestation`` is signed by the Wallet Provider (:ref:`WP_027–029 <wallet-instance-testcases>` and :ref:`WP_143–144 <wallet-instance-optional-testcases>`). The JWT formatted Key Attestation is to be used for the Issuance phase, as an ``key_attestation`` JOSE header in JWT ``proof`` type, and will be sent to the Credential Issuer as discussed in :ref:`credential-issuance:Digital Credential Issuance`.


The JSON Object returned in the response has the following claim:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **key_attestation**
      - REQUIRED. A String representing the issued Key Attestation.
      - This specification.

The value of ``key_attestation`` parameter is a string representing the Key Attestation in a JWT.

If any errors occur during the process, an error response is returned as it is defined in the previous section.


The following table lists HTTP Status Codes and related error codes for the ones that are different from what is already reported:

.. list-table::
    :class: longtable
    :widths: 30 20 50
    :header-rows: 1

    * - **HTTP Status Code**
      - **Error Code**
      - **Description**
    * - ``400 Bad Request``
      - ``bad_request``
      - The request is malformed, missing required parameters (e.g., header parameters, Integrity Assertion, or ``keys_to_attest``), or includes invalid and unknown parameters.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The Integrity Assertion or Key Attestation (``keys_to_attest``) validation failed; the Integrity Assertion or Key Attestation (``keys_to_attest``) is tampered with or improperly signed.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The signature of the Key Attestation Request is invalid or does not match the associated public key (JWK).

Key Attestation JWT
""""""""""""""""""""""""""""

The JOSE header of the Key Attestation JWT contains the following parameters:


.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **alg**
      - REQUIRED. A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section :ref:`algorithms:cryptographic algorithms` and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      - REQUIRED. Unique identifier of the public key associated to the private key the Wallet Provider used to sign the Key Attestation.
      - :rfc:`7638#section_3`.
    * - **typ**
      - REQUIRED. It MUST be set to ``key-attestation+jwt``
      - `OPENID4VC-HAIP`_.
    * - **trust_chain**
      - OPTIONAL. Sequence of Entity Statements that composes the Trust Chain related to the Wallet Provider.
      - `OID-FED`_ Section 4.3 *Trust Chain Header Parameter*.
    * - **x5c**
      - REQUIRED. Contains the X.509 public key certificate or certificate chain (:rfc:`5280`) corresponding to the key used to digitally sign the JWT.
      - :rfc:`7515` Section 4.1.8.

The body of the Key Attestation JWT contains the following claims:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **exp**
      - REQUIRED. UNIX Timestamp with the expiry time of the JWT.
      - :rfc:`9126` and :rfc:`7519`.
    * - **iat**
      - REQUIRED. UNIX Timestamp with the time of JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **attested_keys**
      - REQUIRED. A non-empty array of attested keys from the same key storage component using the syntax of JWK, containing the public part of an asymmetric key pair owned by the Wallet Instance.
      - :rfc:`7517`.
    * - **key_storage**
      - REQUIRED. A non-empty array of case sensitive strings that assert the attack potential resistance of the key storage component and its keys attested in the ``attested_keys`` parameter. The following values are defined as a value for this claim:

        - ``iso_18045_high``: It MUST be used when key storage is resistant to attack with attack potential ``High``.
        - ``iso_18045_moderate``: It MUST be used when key storage is resistant to attack with attack potential ``Moderate``.
        - ``iso_18045_enhanced-basic``: It MUST be used when key storage is resistant to attack with attack potential ``Enhanced-Basic``.
        - ``iso_18045_basic``: It MUST be used when key storage is resistant to attack with attack potential ``Basic``.
      - `OpenID4VCI`_.
    * - **user_authentication**
      - REQUIRED. A non-empty array of case sensitive strings that assert the attack potential resistance of the user authentication methods allowed to access the private keys from the ``attested_keys`` parameter. The following values are defined as a value for this claim:

        - ``iso_18045_high``: It MUST be used when user authentication is resistant to attack with attack potential ``High``.
        - ``iso_18045_moderate``: It MUST be used when user authentication is resistant to attack with attack potential ``Moderate``.
        - ``iso_18045_enhanced-basic``: It MUST be used when user authentication is resistant to attack with attack potential ``Enhanced-Basic``.
        - ``iso_18045_basic``: It MUST be used when user authentication is resistant to attack with attack potential ``Basic``.
      - `OpenID4VCI`_.
    * - **key_storage_status**
      - REQUIRED. Status mechanism for the Key Attestation.

        - **status**: REQUIRED. a status list reference as specified in Appendix D of `OpenID4VCI`_. The value represents the revocation state of the WSCD or Keystore.
        - **exp**: REQUIRED. UNIX Timestamp specifying the time until which the Wallet Provider commits to maintaining the revocation status at the status list index referenced in ``status``.
      - `EUDI-TS 3`_.
    * - **certification**
      - OPTIONAL. A String that contains a URL that links to the certification of the key storage component.
      - `OpenID4VCI`_.



Below is a non-normative example of the Key Attestation JWT header and payload, without encoding and signature applied:

.. literalinclude:: ../../examples/ka-jwt_example_header.json
  :language: JSON

.. literalinclude:: ../../examples/ka-jwt_example_payload.json
  :language: JSON


.. note::
    As the certification scheme has not yet been defined, the exact content of ``certification`` is undefined and will be specified in a future update.


.. note::
    As a revocation mechanism for KA, the Type-shared index described in Section 2.5.2 of `EUDI-TS 3`_ is preferred.


.. note::
    A Wallet Provider SHALL choose the technical validity period of the KA and SHALL maintain the revocation status list for the whole validity period of this list as identified by ``key_storage_status.exp``.


Token Status List (Wallet Unit Attestation Profile)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section profiles the Token Status List (TSL) mechanism of `TOKEN-STATUS-LIST`_ for Wallet Unit Attestations. A TSL conveys the current status of many Wallet Unit Attestations in a compact, signed Status List Token (SLT).

The SLT Provider MUST be the Wallet Provider.

**Status List**

A Status List contains a compressed byte array whose entries represent the statuses of many Wallet Instance Attestations (WIAs) or Key Attestations (KAs). A WIA MUST include its Status List reference in ``client_status.status.status_list``, and a KA MUST include its Status List reference in ``key_storage_status.status.status_list``. Each Status List reference MUST contain ``idx`` and ``uri``. Both WIAs and KAs are JWTs; therefore, ``idx`` is a JSON integer and ``uri`` is a JSON string in each reference. In both cases, ``uri`` MUST be a URI conforming to :rfc:`3986`.

According to this specification, a WIA or KA can have one of the following statuses:

  - ``VALID``. The WIA or KA is valid. This status is represented by ``0x00`` in the SLT.
  - ``INVALID``. The WIA or KA is revoked. This status is represented by ``0x01`` in the SLT.

As a result, the Wallet Provider MUST set the ``bits`` parameter in the SLT's ``status_list`` object to ``1``.

The Wallet Provider MUST pack entries starting with the least significant bit of each byte, compress the byte array using DEFLATE with the ZLIB data format, and publish the resulting Status List in the SLT.

**Key Attestation Index Assignment**

According to R_KA_1 of `CIR2026/1731`_, a Wallet Provider MUST choose one of the following index-assignment options for the ``key_storage_status.status`` claim in a KA. The selected option determines whether the status-list index is shared by KAs for the same type of key storage or is specific to an individual KA:

* **Type-shared index.** All KAs attesting keys stored in the same type of WSCD or keystore MUST contain the same index value in ``key_storage_status.status``. Consequently, the status represented by that index is shared by all such KAs.
* **Per-key-attestation index.** A KA attesting keys stored in an individual WSCD or keystore MUST contain a pairwise-unique index value in ``key_storage_status.status``. Consequently, each KA has a distinct status-list entry and its revocation status can be managed independently.

The requirement for distinct ``idx`` values applies only to the per-key-attestation option. KAs using a type-shared index are exempt.

**Status List Token**

The Wallet Provider MUST act as both the Status Issuer and the Status Provider. It MUST make each SLT available via HTTP GET at the URI specified by either the WIA's ``client_status.status.status_list.uri`` member or the KA's ``key_storage_status.status.status_list.uri`` member, using ``application/statuslist+jwt`` for a JWT SLT or ``application/statuslist+cwt`` for a CWT SLT.

The SLT format MAY be either a JWT or a CWT and MUST be protected by a cryptographic signature. Regardless of the chosen format, the SLT MUST conform to Section 5.1 for JWTs or Section 5.2 for CWTs of `TOKEN-STATUS-LIST`_.

Regardless of the format, the Wallet Provider MUST sign the SLT using one of the following:

- a valid X.509 certificate whose trust chain terminates at the Trust Anchor published in the Wallet Providers LoTE when it is registered in the EUDIW Trust Framework; or
- a valid key attested by the Wallet Provider's Entity Configuration when it is registered in the National Trust Framework.

**Privacy Considerations**

To prevent Wallet Providers from tracking or profiling users based on their use of Wallet Unit Attestations, Wallet Providers MUST aggregate the status information for multiple WIAs or KAs using per-key-attestation indexes in the same Status List and MUST publish the SLT at the same ``uri`` for those attestations. Where appropriate, each Status List SHOULD contain approximately 10,000 entries, in accordance with `EUDI-TS 3`_ and `CIR2026/1731`_. These aggregation and size requirements do not apply to KAs using a type-shared index.

e-Service PDND Wallet Provider Catalog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User's death leads to the revocation of the Wallet Instances of the User and the deletion of the User account at the Wallet Provider. For this reason, the Wallet Provider provides the following e-service through PDND.
A PID/IT-Wallet ID Provider that has been notified by the Authentic Source of the PID/IT-Wallet ID of the User's death MUST send a notification to Wallet Providers using this endpoint.

.. only:: html

  .. note::
    A complete OpenAPI Specification is available :raw-html:`<a href="OAS3-PDND-WP.html" target="_blank">here</a>`.

.. only:: latex

  .. note::
    A complete OpenAPI Specification is available :ref:`appendix-oas-pdnd-wp:Wallet Provider PDND OpenAPI Specification`.

Notify User Death
"""""""""""""""""

.. list-table::
    :class: longtable
    :widths: 20 80
    :stub-columns: 1

    * - **Description**
      - This service is used to notify the Wallet Provider of the need to revoke the Wallet Instance and delete the User's account due to the User's death.
    * - **Provider**
      - Wallet Provider
    * - **Consumer**
      - PID Provider

