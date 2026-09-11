.. include:: ../common/common_definitions.rst
.. Included via test-plans-presentation.rst at title level '^' (level 2).


Remote Credential Verifier Test Matrix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section provides the set of test cases designed for technical implementers and development teams responsible for creating and deploying Credential Verifiers solutions for remote flows. It is also intended for assessment bodies inspecting and validating the implementations of Credential Verifiers solutions for remote flows.

.. note::
  References about official OpenID4VP test plans will update this section in future releases.

.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - **Test Case ID**
    - **Purpose**
    - **Description**
    - **Expected Result**
  * - RPR-01
    - Same Device Flow
    - Verify HTTP redirect (302) URL.
    - Relying Party issues a correct URL using the base url provided within its metadata.
  * - RPR-02
    - Cross Device Flow
    - Verify QR Code generation for Wallet Instance.
    - Relying Party issues QR Code successfully.
  * - RPR-03
    - Cross Device Flow
    - Verify QR Code contains correct URL parameters.
    - Relying Party issues the QR-Code containing an URL using the base url provided within its metadata.
  * - RPR-04
    - Cross Device Flow
    - Test QR Code scanning in low light.
    - QR Code is scanned successfully.
  * - RPR-05
    - Cross Device Flow
    - Verify QR Code error correction level.
    - QR Code remains readable if damaged.
  * - RPR-06
    - Cross Device Flow
    - Test QR Code scanning with different devices.
    - QR Code is scanned successfully.
  * - RPR-07
    - Request URI Method
    - Test ``request_uri_method`` as ``post``.
    - Relying Party accepts Wallet Instance metadata via POST and replies with an updated Request Object.
  * - RPR-08
    - Request URI Method
    - Test ``request_uri_method`` as ``get``.
    - Relying Party issues the Request Object via HTTP GET response.
  * - RPR-09
    - Request URI Method
    - Test absence of ``request_uri_method``.
    - Relying Party accepts defaults to GET method.
  * - RPR-10
    - Metadata
    - Verify parameters match OpenID Credential Verifier metadata.
    - Only allowed parameters will be considered.
  * - RPR-11
    - User Consent
    - Test eligibility of a Credential Verifier in requesting User attributes.
    - User can modify data selection about optional attributes.
  * - RPR-12
    - Authorization Response
    - Test sending of Presentation Response.
    - Relying Party receives and validates response with ``state`` and ``nonce`` values.
  * - RPR-13
    - Authorization Response
    - Verify response encryption.
    - Relying Party evaluates the encrypted response using its public key (one of its keys).
  * - RPR-14
    - Error Handling
    - Test invalid Request Object handling.
    - Error Response is sent.
  * - RPR-15
    - Error Handling
    - Verify error logging.
    - Errors are logged appropriately.
  * - RPR-16
    - Error Handling
    - Test recovery from Authorization Request Error.
    - Relying Party prompts the User to retry or scan new QR code.
  * - RPR-17
    - Error Handling
    - Test fake HTTP Cookie.
    - Relying Party checks the User session consistency coupling the session http cookie and the state and nonces provided.
  * - RPR-19
    - Redirect URI
    - Test redirection to Relying Party's endpoint.
    - User is redirected correctly, the endpoint works.
  * - RPR-20
    - Redirect URI
    - Verify handling of invalid `redirect_uri`.
    - Error response is returned.
  * - RPR-23
    - Credential Presentation
    - Verify response format compliance.
    - Relying Party supports all the Credential format included within its ``vp_formats_supported`` metadata parameter.
  * - RPR-24
    - Authorization Response
    - Test handling of response timeouts.
    - Retries must be successful unless response is acquired.
  * - RPR-25
    - Error Handling
    - Verify handling of malformed claims in presentation payload.
    - Authorization Error Response is sent.
  * - RPR-26
    - Error Handling
    - Verify handling of malformed claims in presented credentials.
    - Authorization Error Response is sent.
  * - RPR-27
    - Error Handling
    - Test handling of expired requests.
    - Holder is notified of expiration.
  * - RPR-28
    - Relying Party Response
    - Verify inclusion of response code.
    - Response code is cryptographically random.
  * - RPR-29
    - Relying Party Response
    - Test handling of invalid response codes.
    - Error response is returned.
  * - RPR-30
    - Status Endpoint
    - Verify handling of unauthorized access.
    - Unauthorized access is denied.
  * - RPR-31
    - Status Endpoint
    - Test handling of invalid session IDs.
    - Error response is returned.
  * - RPR-32
    - Redirect URI
    - Verify handling of expired sessions.
    - Error response is returned.
  * - RPR-33
    - Redirect URI
    - Test handling of server errors.
    - Error response is returned.
  * - RPR-34
    - Same and Cross Device Flow
    - Verify handling of slow network conditions.
    - Relying Party provides the http response within the maximum limit of 2 seconds.
  * - RPR-36
    - Presentation Response
    - Verify handling of large response payloads.
    - Response is evaluated within appropriate security thresholds.
  * - RPR-37
    - Presentation Response
    - Test handling of response encryption failures.
    - Error response is returned.
  * - RPR-38
    - Error Handling
    - Verify handling of invalid signatures.
    - Authorization Error Response is sent.
  * - RPR-39
    - Error Handling
    - Test handling of invalid nonce values.
    - Error response is returned.
  * - RPR-40
    - Relying Party Response
    - Verify handling of malformed responses.
    - Error response is returned.
  * - RPR-41
    - Relying Party Response
    - Test handling of missing response parameters.
    - Error response is returned.
  * - RPR-42
    - Status Endpoint
    - Verify handling of session timeouts.
    - Error response is returned.
  * - RPR-43
    - Status Endpoint
    - Test handling of invalid status codes.
    - Error response is returned.
  * - RPR-44
    - Redirect URI
    - Verify handling of invalid user sessions.
    - Error response is returned.
  * - RPR-45
    - Redirect URI
    - Test handling of unavailable services.
    - Error response is returned.
  * - RPR-46
    - Same Device Flow
    - Verify handling of user cancellations.
    - User can cancel the process.
  * - RPR-47
    - Cross Device Flow
    - Test QR Code scanning with different apps.
    - QR Code is scanned successfully.
  * - RPR-48
    - Cross Device Flow
    - Verify QR Code scanning with different lighting.
    - QR Code is scanned successfully.
  * - RPR-49
    - Request URI Method
    - Test handling of unsupported content types.
    - Error response is returned.
  * - RPR-50
    - User Consent
    - Verify user notification of consent changes.
    - User is informed about consent changes.
  * - RPR-51
    - User Consent
    - Test user consent for sensitive data.
    - User can consent to sensitive data.
  * - RPR-52
    - Authorization Response
    - Verify handling of response decryption failures.
    - Error response is returned.
  * - RPR-53
    - Authorization Response
    - Test handling of response integrity checks.
    - Response integrity is verified.
  * - RPR-54
    - Relying Party Response
    - Verify handling of response validation failures.
    - Error response is returned.
  * - RPR-55
    - Relying Party Response
    - Test handling of response processing errors.
    - Error response is returned.
  * - RPR-56
    - Protected Resource Endpoint
    - Verify handling of unauthorized session access.
    - Unauthorized access is denied.
  * - RPR-57
    - Redirect URI
    - Verify handling of invalid redirect parameters.
    - Error response is returned.
  * - RPR-58
    - Redirect URI
    - Test handling of redirect failures.
    - Error response is returned.
  * - RPR-59
    - Same Device Flow
    - Verify handling of user interruptions.
    - User can resume or cancel the process.
  * - RPR-60
    - Request URI Method
    - Test handling of invalid HTTP methods.
    - Error response is returned.
  * - RPR-61
    - User Consent
    - Verify user notification of consent revocation.
    - User is informed about consent revocation.
  * - RPR-62
    - User Consent
    - Test user consent for optional data.
    - User can consent to optional data.
  * - RPR-63
    - Authorization Response
    - Verify handling of response signature failures.
    - Error response is returned.
  * - RPR-64
    - Authorization Response
    - Test handling of response format errors.
    - Error response is returned.
  * - RPR-65
    - Error Handling
    - Verify handling of invalid JWT signatures.
    - Authorization Error Response is sent.
  * - RPR-66
    - Error Handling
    - Test handling of invalid JWT claims.
    - Error response is returned.
  * - RPR-67
    - Relying Party Response
    - Verify handling of response parsing errors.
    - Error response is returned.
  * - RPR-68
    - Relying Party Response
    - Test handling of response timeout errors.
    - Error response is returned.
  * - RPR-69
    - Status Endpoint
    - Verify handling of session expiration.
    - Error response is returned.
  * - RPR-70
    - Status Endpoint
    - Test handling of session renewal errors.
    - Error response is returned.
  * - RPR-71
    - Redirect URI
    - Verify handling of redirect loop errors.
    - Error response is returned.
  * - RPR-72
    - Redirect URI
    - Test handling of redirect security errors.
    - Error response is returned.
  * - RPR-73
    - Same Device Flow
    - Verify handling of user timeouts.
    - User is notified of timeout.
  * - RPR-74
    - Cross Device Flow
    - Test QR Code scanning with different devices.
    - QR Code is scanned successfully.
  * - RPR-75
    - Cross Device Flow
    - Verify QR Code scanning with different apps.
    - QR Code is scanned successfully.
  * - RPR-76
    - Request URI Method
    - Test handling of unsupported HTTP methods.
    - Error response is returned.

  * - RPR-77
    - QR Code Generation
    - Verify that QR Code error correction level is Q (Quartile - up to 25%).
    - QR Code uses the required Q error correction level.

  * - RPR-78
    - Wallet Attestation Request
    - Test that Wallet Attestation request uses standard DCQL query.
    - Wallet Attestation request correctly uses standard DCQL query.

  * - RPR-79
    - Wallet Attestation Request
    - Verify that ``claims`` parameter is not included in DCQL query for Wallet Attestation.
    - ``claims`` parameter is not included in DCQL query for Wallet Attestation.

  * - RPR-80
    - Wallet Attestation Request
    - Test that ``vct_values`` parameter is required in DCQL query for Wallet Attestation.
    - ``vct_values`` parameter is correctly required in DCQL query.

  * - RPR-81
    - Wallet Nonce
    - Test that Relying Party checks ``wallet_nonce`` when present.
    - Relying Party correctly checks ``wallet_nonce`` when present.

  * - RPR-82
    - Response Types
    - Verify that ``response_types_supported`` is set to ``vp_token`` when present.
    - ``response_types_supported`` is correctly set to ``vp_token``.

  * - RPR-83
    - Redirect URI
    - Test that Relying Party correctly provides ``redirect_uri`` parameter to Wallet Instance.
    - Relying Party correctly provides and handles ``redirect_uri``.

  * - RPR-84
    - Flow Support
    - Test that Relying Party supports required remote flows.
    - Relying Party supports both Same Device and Cross Device flows.

  * - RPR-85
    - Endpoint Security
    - Test that ``request_uri`` is attested by trusted third party.
    - ``request_uri`` parameter is properly attested by trusted third party.

  * - RPR-86
    - Privacy Protection
    - Test that Relying Party correctly validates Wallet Instance metadata without User information.
    - Relying Party correctly evaluates Wallet Instance technical capabilities.

  * - RPR-87
    - Request URI POST Method
    - Test that Relying Party supports receiving Wallet Instance metadata via POST to ``request_uri`` endpoint with content type ``application/x-www-form-urlencoded``.
    - Relying Party correctly accepts and processes Wallet Instance metadata sent via POST with the required content type.

  * - RPR-88
    - Algorithm Validation
    - Test that JWT algorithm is supported and not ``none`` or MAC.
    - JWT algorithm is from supported list and not ``none`` or MAC identifier.

  * - RPR-89
    - Media Type Validation
    - Test that JWT typ is set to ``oauth-authz-req+jwt``.
    - JWT typ parameter is correctly set to ``oauth-authz-req+jwt``.

  * - RPR-90
    - Response Mode Validation
    - Test that ``response_mode`` is set to ``direct_post.jwt`` in both Same Device and Cross Device flows.
    - ``response_mode`` parameter is correctly set to ``direct_post.jwt`` for every remote presentation transaction.

  * - RPR-91
    - Response Type Validation
    - Test that ``response_type`` is set to ``vp_token``.
    - ``response_type`` parameter is correctly set to ``vp_token``.

  * - RPR-92
    - Response URI Usage
    - Test that Relying Party correctly provides ``response_uri`` parameter to Wallet Instance.
    - Relying Party sends Authorization Response to correct ``response_uri`` endpoint.

  * - RPR-93
    - Nonce Entropy
    - Test that nonce has sufficient entropy (32+ digits).
    - nonce parameter has sufficient entropy with at least 32 digits.

  * - RPR-94
    - JWT Expiration
    - Test that JWT ``exp`` is set correctly.
    - JWT ``exp`` parameter is correctly set and not expired.

  * - RPR-95
    - Response URI Security
    - Test that ``response_uri`` is attested by trusted third party.
    - ``response_uri`` parameter is properly attested by trusted third party.

  * - RPR-96
    - Client Metadata Handling
    - Test that Relying Party correctly handles Wallet Instance ``client_metadata``.
    - The ``client_metadata`` is correctly aligned with Trust Chain metadata.

  * - RPR-97
    - Wallet Attestation Request
    - Test that Relying Party requests Wallet Attestation via DCQL.
    - Relying Party correctly requests Wallet Attestation using DCQL query.

  * - RPR-98
    - Error Response Format
    - Test that error response uses ``application/json`` content type.
    - Error response correctly uses ``application/json`` content type.

  * - RPR-99
    - Error Response Parameters
    - Test that error response includes required parameters.
    - Error response includes error and ``error_description`` parameters.

  * - RPR-100
    - Wallet Attestation Presentation
    - Test that Relying Party correctly requests Wallet Attestation from Wallet Instance.
    - Relying Party correctly evaluates Wallet Attestation when requested.

  * - RPR-101
    - Presentation Array
    - Test that ``vp_token`` contains the requested signed presentations.
    - ``vp_token`` contains the requested signed presentations as required.

  * - RPR-102
    - KB-JWT Inclusion
    - Test that Holder includes KB-JWT in SD-JWT.
    - Holder correctly includes KB-JWT in SD-JWT presentation.

  * - RPR-103
    - KB-JWT Validation
    - Test that Relying Party validates KB-JWT signature.
    - Relying Party correctly validates KB-JWT signature using public key.

  * - RPR-104
    - KB-JWT Header
    - Test that KB-JWT contains required header parameters.
    - KB-JWT contains required ``typ`` and ``alg`` header parameters.

  * - RPR-105
    - KB-JWT Payload
    - Test that KB-JWT contains required payload parameters.
    - KB-JWT contains required ``iat``, ``aud``, ``nonce``, and ``sd_hash`` parameters.

  * - RPR-106
    - KB-JWT Audience
    - Test that KB-JWT ``aud`` matches Relying Party identifier.
    - KB-JWT ``aud`` parameter matches Relying Party unique entity identifier.

  * - RPR-107
    - KB-JWT Nonce
    - Test that KB-JWT ``nonce`` matches request object ``nonce``.
    - KB-JWT ``nonce`` parameter matches ``nonce`` from request object.

  * - RPR-108
    - Authorization Error Response
    - Test that Relying Party correctly handles Wallet Instance Authorization Error Response on validation failure.
    - Relying Party correctly evaluates Authorization Error Response when validation fails.

  * - RPR-109
    - Error Response Encoding
    - Test that Authorization Error Response is encoded correctly.
    - Authorization Error Response is encoded in ``application/x-www-form-urlencoded`` format.

  * - RPR-110
    - Response Processing
    - Test that Response URI returns HTTP 200 on successful processing.
    - Response URI returns HTTP 200 with ``application/json`` content type.

  * - RPR-111
    - Error Code Consistency
    - Test that error codes are consistent across different endpoints.
    - Error codes are consistent across all Relying Party endpoints.

  * - RPR-112
    - Response Code Inclusion
    - Test that Relying Party includes response code in ``redirect_uri``.
    - Relying Party includes fresh response code in ``redirect_uri``.

  * - RPR-113
    - Redirect URI Security
    - Test that ``redirect_uri`` is attested by trusted third party.
    - ``redirect_uri`` parameter is properly attested by trusted third party.

  * - RPR-114
    - Validation Error Response
    - Test that Response URI returns error response on validation failure.
    - Response URI returns error response when validation checks fail.


