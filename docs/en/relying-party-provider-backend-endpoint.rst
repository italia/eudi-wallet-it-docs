.. include:: ../common/common_definitions.rst
.. Included via relying-party-endpoints.rst at title level '"' (level 3).

The Relying Party MUST expose a set of endpoints for handling the lifecycle of Verifier Apps that use a remote backend service provided by their Relying Party Provider Backend. These endpoints support proximity presentation flows by providing nonce generation, hardware key registration, integrity validation, and Access Certificate issuance. The specific implementation details are left to the Relying Party's discretion.

.. note::
  Tests related to Relying Party endpoints are defined in the remote presentation test matrix (:ref:`test-plans-remote-presentation:Remote Credential Verifier Test Matrix`) and proximity presentation test matrix (:ref:`test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix`).


Relying Party Provider Backend Federation Endpoint
""""""""""""""""""""""""""""""""""""""""""""""""""

The Relying Party MUST provide its Entity Configuration through the ``/.well-known/openid-federation`` endpoint, according to Section :ref:`infrastructure-trust:Entity Configuration`. Technical details are provided in Section :ref:`relying-party-entity-configuration:Relying Party Entity Configuration`.


Relying Party Provider Backend Nonce Endpoint
"""""""""""""""""""""""""""""""""""""""""""""

The Relying Party Nonce Endpoint allows the Verifier App to request a cryptographic ``nonce`` from the Relying Party Provider Backend. The ``nonce`` serves as an unpredictable, single-use challenge to ensure freshness and prevent replay attacks.

Further details on the Nonce Request and Response are provided in the :ref:`mobile-application-instance:Mobile Application Nonce Request` and :ref:`mobile-application-instance:Mobile Application Nonce Request` Sections, respectively.

Relying Party Verifier App Initialization Endpoint
""""""""""""""""""""""""""""""""""""""""""""""""""

The Verifier App Initialization Endpoint allows for the initialization of Verifier Apps, consisting in the registration of a pair of long-lived, securely stored Cryptographic Hardware Keys.

Further details on the Verifier App Initialization Request and Response are provided in the :ref:`mobile-application-instance:Mobile Application Instance Initialization Request` and :ref:`mobile-application-instance:Mobile Application Instance Initialization Response` Sections, respectively.

Relying Party Provider Backend Key Binding Endpoint
"""""""""""""""""""""""""""""""""""""""""""""""""""

The Relying Party Key Binding Endpoint enables Verifier Apps to bind the newly created pair of keys, which will be associated with an Access Certificate, to the Verifier App, by relying on a proof of possession of the Cryptographic Hardware Keys generated during the :ref:`mobile-application-instance:Mobile Application Instance Initialization` phase. Before completing the process, the Relying Party Provider Backend also needs to verify the integrity of the Verifier App.

Relying Party Provider Backend Key Binding Request
..................................................

Further details on the Relying Party Key Binding Request are provided in the :ref:`wallet-provider-endpoint:Wallet Instance Attestation Issuance Request` section.


The only difference are the following:

- The ``typ`` header of the Integrity Request JWT assumes the value ``rp-kb+jwt``, and
- The ``hardware_signature`` claim value is obtained based on only ``client_data_hash`` value.


Relying Party Provider Backend Key Binding Response
....................................................

Upon a successful request, the Relying Party Provider Backend provides an HTTP Response with a ``204 No Content`` status code.

Below is a non-normative example of a Key Binding Request Response.

.. code-block:: http

    HTTP/1.1 204 No content

If any errors occur during the process, an error response is returned. The response uses ``application/json`` as the ``Content-Type`` and includes the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered (:ref:`WP_035 <wallet-instance-testcases>`).

Below is a non-normative example of a Key Binding Error Response.

.. code-block:: http

    HTTP/1.1 403 Forbidden
    Content-Type: application/json

    {
      "error": "invalid_request",
      "error_description": "The provided challenge is invalid, expired, or already used."
    }

The following table lists HTTP Status Codes and related error codes that are supported for the error response, unless otherwise specified  (:ref:`WP_036–0339 <wallet-instance-testcases>` and :ref:`WP_150–155 <wallet-instance-optional-testcases>`):

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
      - The Verifier App has been revoked.
    * - ``403 Forbidden``
      - ``integrity_check_error``
      - The device does not meet the Relying Party Provider's minimum security requirements.
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
      - The ``iss`` parameter does not match the Relying Party Provider's expected URL identifier.
    * - ``404 Not Found``
      - ``not_found``
      - The Verifier App Instance was not found.
    * - ``422 Unprocessable Content`` [OPTIONAL]
      - ``validation_error``
      - The request does not adhere to the required format.
    * - ``500 Internal Server Error``
      - ``server_error``
      - An internal server error occurred while processing the request.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The service is unavailable. Please try again later.


Relying Party Provider Backend Access Certificate Endpoint
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The Relying Party Access Certificate Endpoint enables Verifier Apps to obtain an Access Certificate.


Relying Party Provider Backend Access Certificate Request
.........................................................

The Access Certificate Request uses the HTTP POST method with ``Content-Type`` set to ``application/json``.

The request includes the following body parameter:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **csr**
      - The CSR generated by the Verifier App, encoded in the ``base64url`` format as defined in :rfc:`2511`.
      -

Below is a non-normative example of an Access Certificate Request.

.. code-block:: http

    POST /access-certificate HTTP/1.1
    Host: relying-party.example.org
    Content-Type: application/json

    {
      "csr": "MIIBvzCCAa..."
    }


Relying Party Provider Backend Access Certificate Response
..........................................................

Upon a successful request, the Relying Party Access Certificate Endpoint provides an HTTP Response with a ``200 OK`` status code and the Access Certificate. The Access Certificate Response, which uses ``application/json`` as the ``Content-Type``, includes the following body parameters:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **access_certificate**
      - The Access Certificate generated by the CSR.
      - This specification.

Below is a non-normative example of an Access Certificate Response.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "access_certificate": "hajdnhaghSDGns..."
    }

If any errors occur, the Relying Party Access Certificate Endpoint returns an error response. The response uses ``application/json`` as the content type and includes the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered.

Below is a non-normative example of an Access Certificate Error Response.

.. code-block:: http

    HTTP/1.1 403 Forbidden
    Content-Type: application/json

    {
        "error": "invalid_request",
        "error_description": "The public key in the CSR is different from the one associated with the Cryptographic Hardware Keys."
    }

The following table lists HTTP Status Codes and related error codes that MUST be supported for the error response, unless otherwise specified:

.. list-table::
    :class: longtable
    :widths: 30 20 50
    :header-rows: 1

    * - **HTTP Status Code**
      - **Error Code**
      - **Description**
    * - ``400 Bad Request``
      - ``bad_request``
      - The request is malformed, missing required parameters (e.g., header parameters or integrity assertion), or includes invalid and unknown parameters.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The public key in the CSR does not match the public key associated with the Cryptographic Hardware Keys.
    * - ``500 Internal Server Error``
      - ``server_error``
      - The request cannot be fulfilled because the Endpoint encountered an internal problem.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The request cannot be fulfilled because the Endpoint is temporarily unavailable (e.g., due to maintenance or overload).

Relying Party Provider Backend Erasure Endpoint
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The Erasure Endpoint allows Wallet Instances to request deletion of attributes presented to the Relying Party, supporting user privacy rights and regulatory compliance.

For detailed implementation requirements, see :ref:`relying-party-remote-flow-endpoints:Relying Party Erasure Endpoint`.


