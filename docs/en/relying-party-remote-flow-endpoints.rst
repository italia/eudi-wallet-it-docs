.. include:: ../common/common_definitions.rst
.. Included via relying-party-endpoints.rst at title level '"' (level 3).

The Relying Party MUST expose a set of endpoints to support remote presentation flows as defined in OpenID4VP 1.0. These endpoints enable secure credential verification, trust establishment, and user authentication for cross-device and same-device interaction patterns.

.. note::
  Tests related to Relying Party remote flow endpoints are defined in the remote presentation test matrix (:ref:`test-plans-remote-presentation:Remote Credential Verifier Test Matrix`).


Federation Endpoint
"""""""""""""""""""""""

The Relying Party MUST provide its Entity Configuration through the ``/.well-known/openid-federation`` endpoint, according to Section :ref:`infrastructure-trust:Entity Configuration`. This endpoint enables trust establishment and discovery of the Relying Party's capabilities.

Technical details are provided in Section :ref:`relying-party-entity-configuration:Relying Party Entity Configuration`.


OpenID4VP Remote Flow Endpoints
"""""""""""""""""""""""""""""""

The following endpoints are required for OpenID4VP 1.0 remote presentation flows as described in :ref:`remote-flow:Remote Flow`. These endpoints support both Same Device and Cross Device flows:

Request URI Endpoint
....................

The Request URI Endpoint is where the Relying Party provides the signed Request Object to the Wallet Instance. This endpoint supports both GET and POST methods as defined in the OpenID4VP 1.0 specification.

For detailed implementation requirements, see :ref:`remote-flow:Request URI Request` and :ref:`remote-flow:Request URI Response`.


Response URI Endpoint
.....................

The Response URI Endpoint receives the Authorization Response from the Wallet Instance containing the Verifiable Presentation. This endpoint processes the presentation and validates the credentials.

For detailed implementation requirements, see :ref:`remote-flow:Authorization Response` and :ref:`remote-flow:Relying Party Response`.


Status Endpoint (Optional)
..........................

The Status Endpoint is an optional endpoint that allows the user-agent to monitor the progress of the presentation flow. This endpoint is particularly useful for Same Device flows where the user-agent needs to know when the Wallet Instance has completed the presentation.

For detailed implementation requirements, see :ref:`remote-flow:Status Endpoint` and :ref:`remote-flow:Status Endpoint Errors`.


User Data Management Endpoints
""""""""""""""""""""""""""""""

The following endpoint supports user data management and privacy compliance requirements for remote flows:

Relying Party Erasure Endpoint
..............................

The Erasure Endpoint, which is described in :ref:`relying-party-metadata:Relying Party Metadata`, allows Wallet Instances to request deletion of attributes presented to the Relying Party. The Relying Party MUST request User authentication before proceeding with the attribute deletion.

Erasure Request
................

The Erasure Request MUST be a GET request to the Erasure Endpoint. The Wallet Instance MUST also support a call back mechanism which enables the User-Agent to notify the Wallet Instance (and thus the User) once the Erasure Response is returned.

Below is a non-normative example of an Erasure Request where the call back URL is passed as a query parameter.

.. code-block:: http

  GET /erasure-endpoint?callback_url=https://wallet-instance/erasure_response HTTP/1.1
  Host: relying-party.example.org

Erasure Response
.................

If the deletion of all attributes bound to the User have been successful, the Erasure Response MUST return a 204 HTTP status code.

If instead the attributes deletion procedure fails due any circumstances, the Relying Party MUST return an error response with ``application/json`` as the content type and MUST include the following parameters:

    - ``error``: The error code.
    - ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

The following table lists the HTTP Status Codes and related error codes that MUST be supported for the error response:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **Error Code**
      - **Description**
    * - ``400 Bad Request``
      - ``bad_request``
      - The request is malformed, missing required parameters (e.g., header parameters or integrity assertion), or includes invalid and unknown parameters.
    * - ``401 Unauthorized``
      - ``unauthorized``
      - The request could not be fulfilled due to invalid authentication by the User.
    * - ``500 Internal Server Error``
      - ``server_error``
      - The request cannot be fulfilled because the Erasure Endpoint encountered an internal problem. (:rfc:`6749#section-4.1.2.1`).
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The request cannot be fulfilled because the Erasure Endpoint is temporarily unavailable (e.g., due to maintenance or overload). (:rfc:`6749#section-4.1.2.1`).


The following is an example of an error response from Erasure Endpoint:

.. code-block:: http

  HTTP/1.1 500 Internal Server Error
  Content-Type: application/json

  {
   "error": "server_error",
   "error_description": "The request cannot be fulfilled due to an internal server error."
  }

Upon receiving an error response, the Wallet Instance which made the Erasure Request MUST inform the User of the error condition in an appropriate manner.


Security Considerations
"""""""""""""""""""""""

All Relying Party endpoints MUST implement appropriate security measures:

- **HTTPS Only**: All endpoints MUST be accessible only over HTTPS
- **Endpoint Mix-up Protection**: Endpoint URLs MUST be attested by trusted third parties through the Trust Chain
- **Input Validation**: All endpoints MUST validate input parameters and reject malformed requests
- **Rate Limiting**: Endpoints SHOULD implement rate limiting to prevent abuse
- **Audit Logging**: All endpoint interactions SHOULD be logged for security monitoring

For detailed security requirements, see :ref:`remote-flow:Remote Flow` and the relevant test cases in :ref:`test-plans-remote-presentation:Remote Credential Verifier Test Matrix`.


Implementation Notes
""""""""""""""""""""

- The specific implementation details for most endpoints are left to the Relying Party's discretion
- Endpoints MUST comply with the OpenID4VP 1.0 specification for remote flows
- Proximity flow endpoints MUST support the lifecycle management of Verifier Apps
- All endpoints MUST be discoverable through the Relying Party's Entity Configuration
- Error responses MUST follow the standard HTTP status codes and include appropriate error descriptions

For comprehensive implementation guidance, refer to the individual endpoint sections and the test matrices for validation requirements.


