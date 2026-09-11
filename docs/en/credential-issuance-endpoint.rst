.. include:: ../common/common_definitions.rst
.. Included via credential-issuer-endpoint.rst at title level '"' (level 3).


Pushed Authorization Request Endpoint
"""""""""""""""""""""""""""""""""""""

Pushed Authorization Request (PAR) Request
..........................................

.. _table_http_request_claim:

The request to the Credential Issuer authorization endpoint MUST use HTTP Headers parameters and HTTP POST parameters.

The HTTP POST method MUST use the parameters in the message body encoded in ``application/x-www-form-urlencoded`` format.

.. list-table:: PAR http request parameters
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **client_id**
      - MUST be set to the thumbprint of the ``jwk`` value in the ``cnf`` parameter inside the Wallet Instance Attestation.
      - :rfc:`6749`
    * - **request**
      - It MUST be a signed JWT. The private key corresponding to the public one in the ``cnf`` parameter inside the Wallet Instance Attestation MUST be used for signing the Request Object.
      - `OpenID Connect Core. Section 6 <https://openid.net/specs/openid-connect-core-1_0.html#JWTRequests>`_

The Pushed Authorization Endpoint is protected with OAuth 2.0 Attestation-based Client Authentication [`OAUTH-ATTESTATION-CLIENT-AUTH`_], therefore
the request to the Credential Issuer authorization endpoint MUST use the following HTTP Headers parameters:

.. list-table:: http request header parameters
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **OAuth-Client-Attestation**
      - **It MUST be set to a value containing the Wallet Instance Attestation JWT.**
      - **`OAUTH-ATTESTATION-CLIENT-AUTH`_.**
    * - **OAuth-Client-Attestation-PoP**
      - It MUST be set to a value containing the Wallet Instance Attestation JWT Proof of Possession.
      - `OAUTH-ATTESTATION-CLIENT-AUTH`_.

.. note::
  Clients SHOULD select the algorithms for the Wallet Instance Attestation and its proof of possession according to the Authorization Server metadata fields
  ``client_attestation_signing_alg_values_supported`` and ``client_attestation_pop_signing_alg_values_supported`` documented in :ref:`credential-issuer-metadata:Metadata for oauth_authorization_server`.


The JWT *Request Object* has the following JOSE header parameters:

.. _table_request_object_claim:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section :ref:`algorithms:Cryptographic Algorithms` and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      - Unique identifier of the ``jwk`` inside the ``cnf`` claim of Wallet Instance Attestation as base64url-encoded JWK Thumbprint value.
      - :rfc:`7638#section_3`.

.. note::
  The parameter **typ**, if omitted, assumes the implicit value **JWT**.


The ``request`` JWT payload contained in the HTTP POST message is given with the following parameters:

.. _table_jwt_request:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - It MUST be set to the ``client_id``.
      - :rfc:`9126` and :rfc:`7519`.
    * - **aud**
      - It MUST be set to the identifier of the Credential Issuer.
      - :rfc:`9126` and :rfc:`7519`.
    * - **exp**
      - UNIX Timestamp with the expiry time of the JWT. The claim value MUST be not greater than 300 seconds from the issuance time.
      - :rfc:`9126` and :rfc:`7519`.
    * - **iat**
      - UNIX Timestamp with the time of JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **response_type**
      - MUST be set to ``code``.
      - :rfc:`6749`
    * - **client_id**
      - It MUST be set as in the :ref:`Table of the HTTP parameters <table_http_request_claim>`.
      - See :ref:`Table of the HTTP parameters <table_http_request_claim>`.
    * - **state**
      - Unique session identifier at the client side. This value will be returned to the client in the response, at the end of the authentication. It MUST be a random string composed by alphanumeric characters and with a minimum length of 32 digits. Special characters MUST be considered non-alphanumeric characters as defined in `[NIST] <https://csrc.nist.gov/glossary/term/special_character>`__.
      - See [`OIDC`_] Section 3.1.2.1.
    * - **code_challenge**
      - A challenge derived from the **code verifier** that is sent in the authorization request.
      - :rfc:`7636#section-4.2`.
    * - **code_challenge_method**
      - A method that was used to derive **code challenge**. It MUST be set to ``S256``.
      - :rfc:`7636#section-4.3`.
    * - **scope**
      - JSON String. String specifying a unique identifier of the Credential regardless of its format. It MUST be mapped in the `credential_configurations_supported` metadata claim of the Credential Issuer. Unique identifier value MUST match the `credential_type` parameter of the :ref:`registry:Digital Credentials Catalog`. For instance, in the case of the PID, it may be set to ``pid``, for IT-Wallet ID it may be set to ``eid`` while in case of mobile driving licence ``mDL``. Since it may be multivalued, when this occurs each value MUST be separated by a space.
      - :rfc:`6749`
    * - **authorization_details**
      - Array of JSON Objects. Each JSON Object MUST include the following claims:

            - **type**: it MUST be set to ``openid_credential``,
            - **credential_configuration_id**: JSON String. String specifying a unique identifier of the Credential in a specific format that MUST be mapped in the `credential_configurations_supported` metadata claim of the Credential Issuer. For instance,``dc_sd_jwt_pid`` can be used for PID in SD-JWT VC format, ``dc_sd_jwt_mDL`` for mobile driving licence in SD-JWT VC format and ``mso_mdoc_mDL`` for mobile driving license in mdoc format.

        When eID Substantial Authentication with MRTD Verification is requested, an additional JSON Object MUST be included with the following claims:

            - **type**: REQUIRED. MUST be ``it_l2+document_proof``,
            - **idphinting**: REQUIRED. URL of the Identity Provider to be used as a hint,
            - **challenge_method**: REQUIRED. Specifies the MRTD verification method. The value MUST be ``mrtd+ias``. Additional verification methods MAY be defined in future releases of this Specification,
            - **challenge_redirect_uri**: REQUIRED. Redirect URI, recognized by Wallet Instance, for handling the challenge response.
      - See [RAR :rfc:`9396`], [`OpenID4VCI`_] and :ref:`credential-issuance-l2plus:eID Substantial Authentication with MRTD Verification for IT-Wallet ID Issuance`.
    * - **redirect_uri**
      - Redirection URI to which the response is intended to be sent. It MUST be a universal or app link registered with the local operating system, so this latter will provide the response to the Wallet Instance.
      - See [`OIDC`_] Section 3.1.2.1.
    * - **jti**
      - Unique identifier of the JWT that, together with the value contained in the ``iss`` claim, prevents the reuse of the JWT (replay attack). Since the `jti` value alone is not collision resistant, it MUST be identified uniquely together with its issuer.
      - [:rfc:`7519`].
    * - **issuer_state**
      - It MUST be present only in case of issuer initiated flow. It MUST contain the same value contained in the Credential Offer.
      - [:rfc:`7519`].

.. note::
  If the request contains scope value and the *authorization_details* parameter the Credential Issuer MUST interpret these individually. However, if both request the same Credential type, then the Credential Issuer MUST follow the request as given by the authorization details object.

The JOSE header of the Wallet Instance Attestation proof of possession, contained in the HTTP Request headers, MUST contain:

.. _table_jwt_pop:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **typ**
      - It MUST be set to ``oauth-client-attestation-pop+jwt``
      - `OAUTH-ATTESTATION-CLIENT-AUTH`_.
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section :ref:`algorithms:Cryptographic Algorithms` and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.

The body of the Wallet Instance Attestation proof of possession JWT, contained in the HTTP Request headers, contains:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - REQUIRED. Thumbprint of the JWK in the ``cnf`` parameter.
      - :rfc:`9126` and :rfc:`7519`.
    * - **aud**
      - REQUIRED. It MUST be set to the identifier of the Credential Issuer.
      - :rfc:`9126` and :rfc:`7519`.
    * - **iat**
      - REQUIRED. UNIX Timestamp with the time of JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **jti**
      - REQUIRED. Unique identifier for the DPoP proof JWT. The value SHOULD be set using a *UUID v4* value according to [:rfc:`4122`].
      - [:rfc:`7519`. Section 4.1.7].
    * - **nbf**
      - OPTIONAL. UNIX Timestamp with the start time of validity of the JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.


Pushed Authorization Request (PAR) Response
...........................................

If the verification is successful, the Credential Issuer MUST provide the response with a *201 HTTP status code*. The following parameters are included as top-level members in the HTTP response message body, using the ``application/json`` media type as defined in [:rfc:`8259`].

.. _table_http_response_claim:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **request_uri**
      - The request URI corresponding to the authorization request posted. This URI MUST be a single-use reference to the respective authorization request. It MUST contain some part generated using a cryptographically strong pseudorandom algorithm. The value format MUST be ``urn:ietf:params:oauth:request_uri:<reference-value>`` with ``<reference-value>`` as the random part of the URI that references the respective authorization request data.
      - [:rfc:`9126`].
    * - **expires_in**
      - A JSON number that represents the lifetime of the request URI in seconds as a positive integer.
      - [:rfc:`9126`].

If any errors occur during the PAR Request, the Authorization Server MUST return an error response as defined in :rfc:`9126#section-2.3`. The response MUST use *application/json* as the content type and MUST include the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered.

Below is a non-normative example of an error response.

.. code-block:: http

  HTTP/1.1 400 Bad Request
  Content-Type: application/json

.. literalinclude:: ../../examples/par-error.json
  :language: JSON

In the following table are listed HTTP Status Codes and related error codes that are supported for the error response:

.. _table_par_error_code:
.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **error code**
      - **Description**
    * - *400 Bad Request* [REQUIRED]
      - ``invalid_request``
      - The Credential Issuer cannot fulfill the request because of missing parameters, invalid parameters or request malformed. (:rfc:`6749#section-5.2`).
    * - *400 Bad Request* [REQUIRED]
      - ``invalid_scope``
      - The Credential Issuer cannot fulfill the request because the requested scope is invalid or unknown. (:rfc:`6749#section-5.2`).
    * - *400 Bad Request* [REQUIRED]
      - ``use_fresh_attestation``
      - The Wallet Instance Attestation JWT is not fresh enough to be acceptable by the server.  Section 6.2 of `OAUTH-ATTESTATION-CLIENT-AUTH`_.
    * - *401 Unauthorized* [REQUIRED]
      - ``invalid_client``
      - The Credential Issuer cannot fulfill the request because of Client Authentication failed (for example in case of unknown client, no parameters Client Authentication included, or unsupported authentication method). (:rfc:`6749#section-5.2`).
    * - *405 Method not allowed* [OPTIONAL]
      - `-`
      - The Credential Issuer cannot fulfill the request because POST method was not used in the request. (:rfc:`9126#section-2.3`).
    * - *413 Payload Too Large* [OPTIONAL]
      - `-`
      - The Credential Issuer cannot fulfill the request because of the size of the request is higher than permitted limit.(:rfc:`9126#section-2.3`).
    * - *429 Too Many Requests* [OPTIONAL]
      - `-`
      - The Credential Issuer cannot fulfill the request because of the numbers requests received is higher than permitted limit.(:rfc:`9126#section-2.3`).
    * - *500 Internal Server Error* [REQUIRED]
      - ``server_error``
      - The Credential Issuer encountered an internal problem. (:rfc:`6749#section-4.1.2.1`).
    * - *503 Service Unavailable* [REQUIRED]
      - ``temporarily_unavailable``
      - The Credential Issuer is temporary unavailable. (:rfc:`6749#section-4.1.2.1`).
    * - *504 Gateway Timeout* [OPTIONAL]
      - `-`
      - The Credential Issuer cannot fulfill the request within the defined time interval.


Authorization endpoint
""""""""""""""""""""""

The authorization endpoint is used to interact with the Credential Issuer and obtain an authorization grant.
The authorization server MUST first verify the identity of the User that own the credential.


Authorization Request
.....................

The Authorization request is issued by the Web Browser in use by the Wallet Instance, the HTTP methods **POST** or **GET** are used. When the method **POST** is used, the parameters MUST be sent using the *Form Serialization*. When the method **GET** is used, the parameters MUST be sent using the *Query String Serialization*. For more details see Section 13 of [`OIDC`_].

The mandatory parameters in the HTTP authentication request are specified in the following table.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **client_id**
      - It MUST be set as in the :ref:`Table of the HTTP parameters <table_http_request_claim>`.
      - See :ref:`Table of the HTTP parameters <table_http_request_claim>`.
    * - **request_uri**
      - It MUST be set to the same value as obtained by PAR Response. See :ref:`Table of the HTTP PAR Response parameters <table_http_response_claim>`.
      - [:rfc:`9126`].

Authorization Response
......................

The authentication response is returned by the Credential issuer authorization endpoint at the end of the authentication flow.

If the authentication is successful the Credential Issuer redirects the User by adding the following query parameters as required to the *redirect_uri*. The redirect URI MUST be a universal or app link registered with the local operating system, so this latter is able to provide the response to the Wallet Instance.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **code**
      - Unique *Authorization Code* that the Wallet Instance submits to the Token Endpoint.
      - [:rfc:`6749#section-4.1.2`], [:rfc:`7521`].
    * - **state**
      - The Wallet Instance MUST check the correspondence with the ``state`` parameter value in the Request Object. It is defined as in the :ref:`Table of the JWT Request parameters <table_jwt_request>`.
      - [:rfc:`6749#section-4.1.2`].
    * - **iss**
      - Unique identifier of the Credential Issuer who created the Authentication Response. The Wallet Instance MUST validate this parameter.
      - [:rfc:`9207`], [:rfc:`7519`, Section 4.1.1.].

If any errors occur during the Authorization Request, the Authorization Server MUST return an error response as defined in :rfc:`6749#section-4.1.2.1`.
In case of invalid/missing ``redirect_uri`` or ``client_id`` Authorization Server MUST inform the User with the error and MUST NOT redirect the User to the redirection URI.
If any other error occurs the Authorization Server MUST redirect the User by adding the following query parameters as required to the *redirect_uri* using the *application/x-www-form-urlencoded* format:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered.
  - *state*. The exact value of ``state`` parameter contained in the Request Object.

Below is a non-normative example of an error response.

.. code-block:: http

  HTTP/1.1 302 Found
  Location: https://client.example.com/cb?
   error=invalid_request
   &error_description=Unsupported%20response_type%20value
   &state=fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd

In case of Authorization Server redirects the User to the *redirect_uri* HTTP status code *302 (Found)* MUST be used. The following error codes are supported for the error response:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **error code**
      - **Description**
    * - *302 Found* [REQUIRED]
      - ``invalid_request``
      - The Credential Issuer cannot fulfill the request because of missing parameters, invalid parameters or request malformed. (:rfc:`6749#section-4.1.2.1`).
    * - *302 Found* [REQUIRED]
      - ``unauthorized_client``
      - The Credential Issuer cannot fulfill the request because the client is not authorized to request an authorization code. (:rfc:`6749#section-4.1.2.1`).
    * - *302 Found* [REQUIRED]
      - ``server_error``
      - The Credential Issuer encountered an internal problem. (:rfc:`6749#section-4.1.2.1`).
    * - *302 Found* [REQUIRED]
      - ``temporarily_unavailable``
      - The Credential Issuer is temporary unavailable. (:rfc:`6749#section-4.1.2.1`).

In case of Authorization Server doesn't redirect the User to the *redirect_uri* the following HTTP Status Codes are supported for the error response:

.. list-table::
    :class: longtable
    :widths: 20 80
    :header-rows: 1

    * - **Status Code**
      - **Description**
    * - *400 Bad Request* [REQUIRED]
      - The Credential Issuer cannot fulfill the request because of invalid/missing ``redirect_uri`` or ``client_id`` parameter.
    * - *500 Internal Server Error* [REQUIRED]
      - The Credential Issuer encountered an internal problem.
    * - *503 Service Unavailable* [REQUIRED]
      - The Credential Issuer is temporary unavailable.
    * - *504 Gateway Timeout* [OPTIONAL]
      - The Credential Issuer cannot fulfill the request within the defined time interval.


Token endpoint
""""""""""""""

The token endpoint is used by the Wallet Instance to obtain an Access Token by presenting an authorization grant, as
defined in :rfc:`6749`. The Token Endpoint is a protected endpoint with a client authentication based on the model defined in OAuth 2.0 Attestation-based Client Authentication [`OAUTH-ATTESTATION-CLIENT-AUTH`_ ].


Token Request
.............

The request to the Credential Issuer Token endpoint MUST be an HTTP request with method POST, with the body message encoded in ``application/x-www-form-urlencoded`` format. The Wallet Instance sends the Token endpoint request with ``OAuth-Client-Attestation`` and ``OAuth-Client-Attestation-PoP`` as header parameters according to `OAUTH-ATTESTATION-CLIENT-AUTH`_.

The Token endpoint is protected with *OAuth 2.0 Attestation-based Client Authentication* [`OAUTH-ATTESTATION-CLIENT-AUTH`_], therefore
the request to the Credential Issuer authorization endpoint MUST use the following HTTP Headers parameters **OAuth-Client-Attestation** as **OAuth-Client-Attestation-PoP**
as defined in the :ref:`credential-issuance-endpoint:Pushed Authorization Request Endpoint`"

The Token endpoint issues DPoP tokens, therefore it is REQUIRED that the request includes in its HTTP header the DPoP proof parameter.
The Authorization Server MUST validate the DPoP proof received at the Token endpoint, according to :rfc:`9449` Section 4.3. This mitigates the misuse of leaked or stolen Access Tokens/Refresh Tokens at the Credential/Token endpoint. If the DPoP proof is invalid, the Token endpoint returns an error response, according to Section 5.2 of [:rfc:`6749`] with ``invalid_dpop_proof`` as the value of the error parameter.

The token request contains the following claims:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **grant_type**
      - REQUIRED. It MUST be set to ``authorization_code`` or ``refresh_token``.
      - [:rfc:`6749`].
    * - **code**
      - REQUIRED only if the grant type is ``authorization_code``. Authorization code returned in the Authentication Response. It MUST NOT be present if grant type is ``refresh_token``.
      - [:rfc:`6749`].
    * - **redirect_uri**
      - REQUIRED only if the grant type is ``authorization_code``. It MUST be set as in the Request Object :ref:`Table of the JWT Request parameters <table_jwt_request>`. It MUST NOT be present if grant type is ``refresh_token``.
      - [:rfc:`67491`].
    * - **code_verifier**
      - REQUIRED only if the grant type is ``authorization_code``. Verification code of the **code_challenge**.
      - `Proof Key for Code Exchange by OAuth Public Clients <https://datatracker.ietf.org/doc/html/rfc7636>`_. It MUST NOT be present if grant type is ``refresh_token``.
    * - **refresh_token**
      - REQUIRED only if the grant type is ``refresh_token``. The Refresh Token previously issued to the Wallet Instance. It MUST NOT be present if grant type is ``authorization_code``.
      - [:rfc:`6749`].
    * - **scope**
      - OPTIONAL only if the grant type is ``refresh_token``. The requested scope MUST NOT include any scope not originally granted by the User, and if omitted is treated as equal to the scope originally granted by the User. It MUST NOT be present if grant type is ``authorization_code``.
      - [:rfc:`6749`].


A **DPoP Proof JWT** is included in the HTTP request using the ``DPoP`` header parameter containing a DPoP JWT.

The JOSE header of a **DPoP JWT** MUST contain at least the following parameters:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **typ**
      - It MUST be equal to ``dpop+jwt``.
      - [:rfc:`7515`] and [:rfc:`8725`. Section 3.11].
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms in Section :ref:`algorithms:Cryptographic Algorithms` and MUST NOT be set to ``none`` or with a symmetric algorithm (MAC) identifier.
      - [:rfc:`7515`].
    * - **jwk**
      - It represents the public key chosen by the Wallet Instance, in JSON Web Key (JWK) [:rfc:`7517`] format that the Access Token MUST be bound to, as defined in [:rfc:`7515`] Section 4.1.3. It MUST NOT contain a private key.
      - [:rfc:`7517`] and [:rfc:`7515`].


The payload of a **DPoP JWT Proof** MUST contain the following claims:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **jti**
      - Unique identifier for the DPoP proof JWT. The value SHOULD be set using a *UUID v4* value according to [:rfc:`4122`].
      - [:rfc:`7519`. Section 4.1.7].
    * - **htm**
      - The value of the HTTP method of the request to which the JWT is attached.
      - [:rfc:`9110`. Section 9.1].
    * - **htu**
      - The HTTP target URI, without query and fragment parts, of the request to which the JWT is attached.
      - [:rfc:`9110`. Section 7.1].
    * - **iat**
      - UNIX Timestamp with the time of JWT issuance, coded as NumericDate as indicated in :rfc:`7519`.
      - [:rfc:`7519`. Section 4.1.6].


Token Response
..............

If the Token Request is successfully validated, the Authorization Server provides an HTTP Token Response with a *200 (OK)* status code. The Token Response contains the following claims.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **access_token**
      - REQUIRED. The *DPoP-bound Access Token*, in signed JWT format, allows accessing the Credential Endpoint for obtaining the Credential.
      - [:rfc:`6749`].
    * - **refresh_token**
      - OPTIONAL. The *DPoP-bound Refresh Token*, in signed JWT format, which can be used to obtain a new Access Token at the Credential Issuer Token Endpoint.
      - [:rfc:`6749`].
    * - **token_type**
      - REQUIRED. Type of *Access Token* returned. It MUST be equal to ``DPoP``.
      - [:rfc:`6749`].
    * - **expires_in**
      - REQUIRED. Expiry time of the *Access Token* in seconds.
      - [:rfc:`6749`].
    * - **authorization_details**
      - REQUIRED when ``authorization_details`` parameter is used to request issuance of a Credential. OPTIONAL when ``scope`` parameter is used to request issuance of a Credential. Array of JSON Objects, used to identify Credentials with the same metadata but different claimset/claim values and/or simplify the Credential request even when only one Credential is being issued. In addition to the claim defined in :ref:`Table of the JWT Request parameters <table_jwt_request>` it MUST include the following claim:

            - **credential_identifiers**: Array of strings, each uniquely identifying a Credential dataset that is available for the issuance.
      - [`OpenID4VCI`_].

If any errors occur during the validation of the Token Request, the Authorization Server MUST return an error response as defined in :rfc:`6749#section-5.2`. The response MUST use the HTTP Content-Type set to *application/json* and MUST include the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered.

Below is a non-normative example of an error response.

.. code-block:: http

  HTTP/1.1 401 Unauthorized
  Content-Type: application/json;charset=UTF-8
  Cache-Control: no-store
  Pragma: no-cache

.. literalinclude:: ../../examples/token-error.json
  :language: JSON

In the following table are listed HTTP Status Codes and related error codes that are supported for the error response:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **error code**
      - **Description**
    * - *400 Bad Request* [REQUIRED]
      - ``invalid_request``
      - The Credential Issuer cannot fulfill the request because of missing parameters, invalid parameters or request malformed. (:rfc:`6749#section-5.2`).
    * - *400 Bad Request* [REQUIRED]
      - ``invalid_grant``
      - The Credential Issuer cannot fulfill the request because the provided authorization code or Refresh Token is invalid, expired, revoked, or does not match the redirection URI used in the authorization request, or was issued to another client. (:rfc:`6749#section-5.2`).
    * - *400 Bad Request* [REQUIRED]
      - ``unsupported_grant_type``
      - The Credential Issuer cannot fulfill the request because the authorization grant type is not supported. (:rfc:`6749#section-5.2`).
    * - *400 Bad Request* [REQUIRED]
      - ``invalid_dpop_proof``
      - The Credential Issuer cannot fulfill the request because of invalid *DPoP proof*. Section 5 of [:rfc:`9449`].
    * - *400 Bad Request* [REQUIRED]
      - ``use_fresh_attestation``
      - The Wallet Instance Attestation JWT is not fresh enough to be acceptable by the server.  Section 6.2 of `OAUTH-ATTESTATION-CLIENT-AUTH`_.
    * - *401 Unauthorized* [REQUIRED]
      - ``invalid_client``
      - The Credential Issuer cannot fulfill the request because of invalid parameters Client Authentication failed (for example in case of unknown client, no parameters Client Authentication included, or unsupported authentication method). (:rfc:`6749#section-5.2`).
    * - *500 Internal Server Error* [REQUIRED]
      - ``server_error``
      - The Credential Issuer encountered an internal problem.
    * - *503 Service Unavailable* [REQUIRED]
      - ``temporarily_unavailable``
      - The Credential Issuer is temporary unavailable.
    * - *504 Gateway Timeout* [OPTIONAL]
      - `-`
      - The Credential Issuer cannot fulfill the request within the defined time interval.

Access Token
............

A DPoP-bound Access Token is provided by the Credential Issuer Token endpoint as a result of a successful token request. The Access Token is encoded in JWT format, according to [:rfc:`7519`]. The Access Token MUST have at least the following mandatory claims and it MUST be bound to the public key that is provided by the DPoP proof. This binding can be accomplished based on the methodology defined in Section 6 of (:rfc:`9449`).

The **DPoP JWT** contains the following JOSE header parameters and claims.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **typ**
      - REQUIRED. It MUST be equal to ``at+jwt``.
      - [:rfc:`7515`].
    * - **alg**
      - REQUIRED. A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms in Section :ref:`Cryptographic Algorithms <algorithms:Cryptographic Algorithms>` and MUST NOT be set to ``none`` or with a symmetric algorithm (MAC) identifier.
      - [:rfc:`7515`].
    * - **kid**
      - REQUIRED. Unique identifier of the ``jwk`` used by the Credential Issuer to sign the Access Token.
      - :rfc:`7638#section_3`.


.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **iss**
    - REQUIRED. It MUST be an HTTPS URL that uniquely identifies the Credential Issuer. The Wallet Instance MUST verify that this value matches the Credential Issuer where it has requested the credential.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **sub**
    - REQUIRED. It identifies the subject of the JWT.
    - [:rfc:`9068`], [:rfc:`7519`] and Section 8 of [`OIDC`_].
  * - **client_id**
    - REQUIRED. The identifier for the Wallet Instance that requested the Access Token; it MUST be equal to the to kid of the public key of the Wallet Instance specified into the Wallet Instance Attestation (``cnf.jwk``).
    - [:rfc:`9068`], [:rfc:`7519`] and Section 8 of [`OIDC`_].
  * - **aud**
    - REQUIRED. It MUST be set to the identifier of the Credential Issuer.
    - [:rfc:`9068`].
  * - **iat**
    - REQUIRED. UNIX Timestamp with the time of JWT issuance, coded as NumericDate as indicated in :rfc:`7519`.
    - [:rfc:`9068`], [:rfc:`7519`. Section 4.1.6].
  * - **exp**
    - REQUIRED. UNIX Timestamp with the expiry time of the JWT, coded as NumericDate as indicated in :rfc:`7519`.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **jti**
    - OPTIONAL. It MUST be a String in *uuid4* format. Unique Token ID identifier that the RP SHOULD use to prevent reuse by rejecting the Token ID if already processed.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **cnf**
    - REQUIRED. It MUST contain a **jkt** claim being JWK SHA-256 Thumbprint Confirmation Method. The value of the *jkt* member MUST be the base64url encoding (as defined in [:rfc:`7515`]) of the JWK SHA-256 Thumbprint of the DPoP public key (in JWK format) to which the Access Token is bound.
    - [:rfc:`9449`. Section 6.1] and [:rfc:`7638`].

Refresh Token
.............

A *DPoP-bound Refresh Token* is provided by the Credential Issuer Token endpoint as a result of a successful token request. The Refresh Token is encoded in JWT format, according to [:rfc:`7519`]. The Refresh Token MUST have at least the following mandatory claims and it MUST be bound to the public key that is provided by the DPoP proof. This binding can be accomplished based on the methodology defined in Section 6 of (:rfc:`9449`).

The **DPoP JWT** MUST contain the following JOSE header parameters and claims.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **typ**
      - It MUST be equal to ``rt+jwt``.
      - [:rfc:`7515`].
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms in Section :ref:`algorithms:Cryptographic Algorithms` and MUST NOT be set to ``none`` or with a symmetric algorithm (MAC) identifier.
      - [:rfc:`7515`].
    * - **kid**
      - Unique identifier of the ``jwk`` used by the Credential Issuer to sign the Access Token.
      - :rfc:`7638#section_3`.


.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **iss**
    - It MUST be an HTTPS URL that uniquely identifies the Credential Issuer. The Wallet Instance MUST verify that this value matches the Credential Issuer where it has requested the Credential.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **sub**
    - It identifies the subject of the JWT. It MUST be set to the value of the ``sub`` field in the SD-JWT VC Credential.
    - [:rfc:`9068`], [:rfc:`7519`] and Section 8 of [`OIDC`_].
  * - **client_id**
    - The identifier for the Wallet Instance that requested the Access Token; it MUST be equal to the to `kid` value identifying the public key used in the Wallet Instance, used in the Wallet Instance Attestation (``cnf.jwk``).
    - [:rfc:`9068`], [:rfc:`7519`] and Section 8 of [`OIDC`_].
  * - **aud**
    - It MUST be set to the identifier of the Credential Issuer.
    - [:rfc:`9068`].
  * - **iat**
    - UNIX Timestamp with the time of JWT issuance, coded as NumericDate as indicated in :rfc:`7519`.
    - [:rfc:`9068`], [:rfc:`7519`. Section 4.1.6].
  * - **nbf**
    - UNIX Timestamp with the time before which the JWT MUST NOT be accepted for processing, coded as NumericDate as indicated in :rfc:`7519`. It SHOULD be set to the ``exp`` claim of the corresponding Access Token.
    - [:rfc:`7519`. Section 4.1.7].
  * - **exp**
    - UNIX Timestamp with the expiry time of the JWT, coded as NumericDate as indicated in :rfc:`7519`.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **jti**
    - It MUST be a String in *uuid4* format. Unique Token ID identifier that the RP SHOULD use to prevent reuse by rejecting the Token ID if already processed.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **cnf**
    - It MUST contain a **jkt** claim being JWK SHA-256 Thumbprint Confirmation Method. The value of the *jkt* member MUST be the base64url encoding (as defined in [:rfc:`7515`]) of the JWK SHA-256 Thumbprint of the DPoP public key (in JWK format) to which the Access Token is bound.
    - [:rfc:`9449`. Section 6.1] and [:rfc:`7638`].

Nonce Endpoint
""""""""""""""

The Nonce Endpoint provides a ``c_nonce`` value useful to create a proof of possession of key material for the request to the Credential Endpoint, as defined in Section 7 of `OpenID4VCI`_.

Nonce Request
.............

The request for a nonce MUST be an HTTP POST without a body addressed to the Credential Issuer Nonce Endpoint mapped in the Credential Issuer Metadata.


Nonce Response
..............

Nonce Response to the Wallet Instance MUST be sent using `application/json` media type. In case of Nonce Request successful, the Credential Issuer MUST return HTTP response with a *200 (OK)* status code.

As defined in Section 7.2 of `OpenID4VCI`_, the Credential Issuer MUST make the response uncacheable by adding a ``Cache-Control`` header field valued with *no-store*.

The Nonce Response contains the following parameter:

.. list-table::
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **c_nonce**
    - REQUIRED. String containing the nonce value. This value MUST be unpredictable.
    - Section 7.2 of [`OpenID4VCI`_].

Credential endpoint
"""""""""""""""""""

The Credential Endpoint issues a Credential upon the presentation of a valid Access Token, as defined in `OpenID4VCI`_.


Credential Request
..................

The Wallet Instance when requests the Digital Credential to the Credential endpoint, MUST use the following parameters in the message body of the HTTP POST request, using the `application/json` media type.

The Credential endpoint MUST accept and validate the *DPoP proof* sent in the DPoP HTTP Header parameter, according to the steps defined in (:rfc:`9449`) Section 4.3. The *DPoP proof* in addition to the values that are defined in the Token Endpoint section MUST contain the following claim:

  - **ath**: hash value of the Access Token encoded in ASCII. The value MUST use the base64url encoding (as defined in Section 2 of (:rfc:`7515`) with the SHA-256 algorithm.

.. warning::
  The Wallet Instance MUST create a **new DPoP proof** for the Credential request and MUST NOT use the previously created proof for the Token Endpoint.


.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **credential_identifier**
    - REQUIRED when an Authorization Details of type *openid_credential* was returned from the Token Response. It MUST NOT be used otherwise. This MUST be set with one of the value obtained in the ``credential_identifiers`` claim of the Token Response. It MUST NOT be used if ``credential_configuration_id`` is present.
    - Section 8.2 of [`OpenID4VCI`_].
  * - **credential_configuration_id**
    - REQUIRED if ``credential_identifiers`` parameter is absent in the Token Response. It MUST NOT be used otherwise. String specifying a unique identifier of the Credential being described in the `credential_configurations_supported` map in the Credential Issuer Metadata. For example, in the case of the PID in SD-JWT VC format, it can be set to ``dc_sd_jwt_pid``.
    - Section 8.2 of [`OpenID4VCI`_].
  * - **proofs**
    - REQUIRED. Object providing one or more proofs of possession of the cryptographic key material to which the issued Credential instances will be bound to. The ``proofs`` object MUST contain an array parameter named ``jwt`` containing an array of JWT, where each element within the array is used as proof of possession.
    - [`OpenID4VCI`_].


The JWT proof type MUST contain the following parameters for the JOSE header and the JWT body:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **JOSE Header**
    - **Description**
    - **Reference**
  * - **alg**
    - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms in Section :ref:`algorithms:Cryptographic Algorithms` and MUST NOT be set to ``none`` or to a symmetric algorithm (MAC) identifier.
    - [`OpenID4VCI`_], [:rfc:`7515`], [:rfc:`7517`].
  * - **typ**
    - It MUST be set to `openid4vci-proof+jwt`.
    - [`OpenID4VCI`_], [:rfc:`7515`], [:rfc:`7517`].
  * - **jwk**
    - Representing the public key chosen by the Wallet Instance, in JSON Web Key (JWK) [:rfc:`7517`] format that the Digital Credential shall be bound to, as defined in Section 4.1.3 of [:rfc:`7515`].
    - [`OpenID4VCI`_], [:rfc:`7515`], [:rfc:`7517`].
  * - **key_attestation**
    - Representing the Key Attestation.
    - [`OpenID4VCI`_].

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **iss**
    - The value of this claim MUST be the **client_id** of the Wallet Instance.
    - [`OpenID4VCI`_], [:rfc:`7519`, Section 4.1.1].
  * - **aud**
    - It MUST be set to the identifier of the Credential Issuer.
    - [`OpenID4VCI`_].
  * - **iat**
    - UNIX Timestamp with the time of JWT issuance, coded as NumericDate as indicated in :rfc:`7519`.
    - [`OpenID4VCI`_], [:rfc:`7519`. Section 4.1.6].
  * - **nonce**
    - The value type of this claim MUST be a string, where the value is a **c_nonce** provided by the Credential Issuer in the Nonce Response.
    - [`OpenID4VCI`_].


Credential Response
...................

Credential Response to the Wallet Instance MUST be sent using `application/json` media type. If the Credential Request is successfully validated, and the Credential is immediately available, the Credential Issuer MUST return HTTP response with a *200 (OK)* status code. If the Credential is not available and the deferred flow is supported by the Credential Issuer, an HTTP status code *202* MUST be returned.

The Credential Response contains the following parameters:

.. _table_credential_response_claim:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **credentials**
    - REQUIRED if ``interval`` and ``transaction_id`` are not present, otherwise it MUST NOT be present. It is an array of one or more issued Credentials. The number of elements in the Credentials array matches the number of keys that the Wallet Instance has provided either via the ``proofs`` parameter of the Credential Request. The array MUST contain JSON objects, where each object MUST have exactly one member with the key ``credential``. The value of the ``credential`` member MUST be a string containing the encoded Credential, as further described below:

          - **credential**: REQUIRED. String containing one issued Digital Credential. If the requested format identifier is ``dc+sd-jwt`` then the ``credential`` parameter MUST NOT be re-encoded. If the requested format identifier is ``mso_mdoc`` then the ``credential`` parameter MUST be a base64url-encoded representation of the CBOR-encoded IssuerSigned structure, as defined in [ISO 18013-5]. This structure SHOULD contain all Namespaces and IssuerSignedItems that are included in the AuthorizedNamespaces of the MobileSecurityObject.
    - Section 8.3, Annex A2.4 and Annex A3.4 of [`OpenID4VCI`_].
  * - **interval**
    - REQUIRED if ``transaction_id`` is present, otherwise it MUST NOT be present. The amount of time (in seconds) required before making a Deferred Credential Request (:ref:`WP_065 <wallet-credential-issuance-testcases>`).
    - Section 8.3 of [`OpenID4VCI`_].
  * - **notification_id**
    - OPTIONAL. String identifying an issued Credential that the Wallet includes in the Notification Request as defined in Section :ref:`credential-issuance-endpoint:Notification Request`. It MUST NOT be present if the ``credentials`` parameter is not present.
    - Section 8.3 of [`OpenID4VCI`_].
  * - **transaction_id**
    - REQUIRED if ``credentials`` is not present, otherwise it MUST NOT be present. String identifying a deferred issuance transaction that the Wallet includes in the subsequent Credential Request as defined in Section :ref:`credential-issuance-endpoint:Deferred Endpoint` as per (:ref:`WP_065 <wallet-credential-issuance-testcases>`). It MUST be invalidated after the User obtains the Credential.
    - Section 8.3 of [`OpenID4VCI`_].

In case of the Credential Request does not contain a valid Access Token, the Credential Endpoint returns an error response such as defined in Section 3 of [:rfc:`6750`].
If any other error occurs, the Credential Issuer MUST return an error response as defined in Section 8.3.1 of [`OpenID4VCI`_]. The response MUST use the content type *application/json* and MUST include the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered.

Below is a non-normative example of an error response.

.. code-block:: http

  HTTP/1.1 400 Bad Request
  Content-Type: application/json
  Cache-Control: no-store

.. literalinclude:: ../../examples/credential-error.json
  :language: JSON

In the following table are listed HTTP Status Codes and related error codes that are supported for the error response:

.. _table_credential_error_code:
.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **error code**
      - **Description**
    * - *400 Bad Request* [REQUIRED]
      - ``invalid_credential_request``
      - The Credential Issuer cannot fulfill the request because of missing parameters, invalid parameters or request malformed. Section 8.3.1 of [`OpenID4VCI`_].
    * - *400 Bad Request* [REQUIRED]
      - ``unknown_credential_configuration``
      - The Credential Issuer cannot fulfill the request because the requested Credential Configuration is unknown. Section 8.3.1 of [`OpenID4VCI`_].
    * - *400 Bad Request* [REQUIRED]
      - ``unknown_credential_identifier``
      - The Credential Issuer cannot fulfill the request because the requested Credential identifier is unknown. Section 8.3.1 of [`OpenID4VCI`_].
    * - *400 Bad Request* [REQUIRED]
      - ``invalid_proof``
      - The Credential Issuer cannot fulfill the request because the ``proofs`` parameter in the Credential Request is invalid or absent or the key proof(s) does not contain the ``c_nonce`` value. Section 8.3.1 of [`OpenID4VCI`_].
    * - *400 Bad Request* [REQUIRED]
      - ``invalid_nonce``
      - The Credential Issuer cannot fulfill the request because the ``proofs`` parameter in the Credential Request uses an invalid nonce. Section 8.3.1 of [`OpenID4VCI`_].
    * - *400 Bad Request* [REQUIRED]
      - ``invalid_encryption_parameters``
      - The Credential Issuer cannot fulfill the request because the encryption parameters in the Credential Request are invalid or missing. Section 8.3.1 of [`OpenID4VCI`_].
    * - *400 Bad Request* [REQUIRED]
      - ``credential_request_denied``
      - The Credential Request has not been accepted by the Credential Issuer. The Wallet SHOULD treat this error as unrecoverable, meaning if received from a Credential Issuer the Credential(s) cannot be issued. Section 8.3.1 of [`OpenID4VCI`_].
    * - *400 Bad Request* [REQUIRED]
      - ``invalid_transaction_id``
      - Only in case of deferred flow. The Credential Issuer cannot fulfill the request because the Credential Request contains an invalid ``transaction_id``. Section 9.3 of [`OpenID4VCI`_].
    * - *400 Bad Request* [REQUIRED]
      - ``invalid_dpop_proof``
      - The Credential Issuer cannot fulfill the request because of invalid *DPoP proof*. Section 7 of [:rfc:`9449`].
    * - *500 Internal Server Error* [REQUIRED]
      - ``server_error``
      - The Credential Issuer encountered an internal problem.
    * - *503 Service Unavailable* [REQUIRED]
      - ``temporarily_unavailable``
      - The Credential Issuer is temporary unavailable.
    * - *504 Gateway Timeout* [OPTIONAL]
      - `-`
      - The Credential Issuer cannot fulfill the request within the defined time interval.

Deferred Endpoint
"""""""""""""""""

Credential Issuers MAY support the *Deferred Endpoint* aiming to satisfy the cases where an immediate issuance might be not possible, due to errors during the communication between the Credential Issuer and the Authentic Source (for example the Authentic Source is temporarily unavailable, etc.) or due to administrative or technical processes.

In the case where the Authentic Source and the Credential Issuer are both enabled to use *PDND*, what is described in Section :ref:`authentic-sources:Authentic Sources` MUST apply.


The following requirements apply:

 1. The Deferred Credential request MAY also happen several days after the initial Credential request.
 2. The User MUST be informed that the Credential is available and ready to be issued.
 3. The Wallet Provider MUST NOT be informed about which Credential is available to be issued or which Credential Issuer the User needs to contact.
 4. The Wallet Instance MUST be informed about the amount of time to wait before making a new Credential request.
 5. As, in general, an unavailability may be an unexpected event, the Credential Issuer MUST be able to switch on the fly between a *immediate* and an *deferred* flow. This decision MUST be taken after the authorization step.


If Credential Issuers, supporting this flow, are not able to immediately issue a requested Credential, they MUST provide the Wallet Instance with an HTTP Credential Response containing the amount of time to wait before making a new Credential request and an identifier of the deferred issuance transaction (*transaction_id*). The HTTP status code MUST be *202* (see Section 15.3.3 of [:rfc:`9110`]). Below a non-normative example is given.

.. code-block:: http

  HTTP/1.1 202 Accepted
  Content-Type: application/json
  Cache-Control: no-store

.. literalinclude:: ../../examples/credential-response-deferred.json
  :language: JSON

The Wallet Instance MUST use the value given in the *interval* parameter to inform the User when the Credential becomes available (e.g. using a local notification triggered by the *interval* time value). Credential Issuers MAY send a notification to the User through a communication channel (e.g. email address), if previously provided by the User to the Credential Issuer.

Deferred Request
................

Upon receipt of the notification (by the Wallet Instance and/or by the Credential Issuer), the User accesses the Wallet Instance.

The Wallet Instance MUST present to the Deferred Endpoint an Access Token that is valid for the issuance of the Digital Credential previously requested at the Credential Endpoint.

If the ``interval`` parameter value results as less than the expiration time set for the Access Token, the Wallet Instance SHOULD use the Access Token  (:ref:`WP_066b <wallet-credential-issuance-testcases>`). Otherwise, the Wallet Instance MAY obtain a new Access Token following the Refresh Token flow (see Section :ref:`credential-issuance-low-level:Refresh Token Flow` for more details as per :ref:`WP_066c <wallet-credential-issuance-testcases>`). If the Refresh Token flow fails, the Wallet Instance needs to submit a new authentication request  (:ref:`WP_067 <wallet-credential-issuance-testcases>`).

The Deferred Credential Request MUST be an HTTP POST request. It MUST be sent using the ``application/json`` media type.
The following parameter is used in the Deferred Credential Request:

  - ``transaction_id``: REQUIRED. String identifying a Deferred Issuance transaction (:ref:`WP_066a <wallet-credential-issuance-testcases>`).

The Credential Issuer MUST invalidate the ``transaction_id`` after the Credential for which it was meant has been obtained by the Wallet Instance.
The following is a non-normative example of a Deferred Credential Request:

.. code-block:: http

  POST /credential HTTP/1.1
  Host: eaa-provider.example.org
  Content-Type: application/json
  Authorization: DPoP Kz~8mXK1EalYznwH-LC-1fBAo.4Ljp~zsPE_NeO.gxU
  DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6Ik
      VDIiwieCI6Imw4dEZyaHgtMzR0VjNoUklDUkRZOXpDa0RscEJoRjQyVVFVZldWQVdCR
      nMiLCJ5IjoiOVZFNGpmX09rX282NHpiVFRsY3VOSmFqSG10NnY5VERWclUwQ2R2R
      1JEQSIsImNydiI6IlAtMjU2In19.eyJqdGkiOiJlMWozVl9iS2ljOC1MQUVCIiwiaHRtIj
      oiR0VUIiwiaHR1IjoiaHR0cHM6Ly9yZXNvdXJjZS5leGFtcGxlLm9yZy9wcm90ZWN0Z
      WRyZXNvdXJjZSIsImlhdCI6MTU2MjI2MjYxOCwiYXRoIjoiZlVIeU8ycjJaM0RaNTNF
      c05yV0JiMHhXWG9hTnk1OUlpS0NBcWtzbVFFbyJ9.2oW9RP35yRqzhrtNP86L-Ey71E
      OptxRimPPToA1plemAgR6pxHF8y6-yqyVnmcw6Fy1dqd-jfxSYoMxhAJpLjA


  {
    "transaction_id": "8xLOxBtZp8"
  }

Deferred Response
.................

The Deferred Credential Response MUST be sent using the ``application/json`` media type.

If the Digital Credential(s) is(are) available, the Deferred Credential Response MUST use the ``credentials`` and ``notification_id`` parameters as defined in Section :ref:`credential-issuance-endpoint:Credential Response` and MUST respond with the HTTP status code 200 (see Section 15.3.3 of :rfc:`9110`]).

If the Credential Issuer still requires more time, the Deferred Credential Response MUST use the ``interval`` and ``transaction_id`` parameters as defined in Section :ref:`credential-issuance-endpoint:Credential Response` and it MUST respond with the HTTP status code 202 (see Section 15.3.3 of :rfc:`9110`]).

The value of ``transaction_id`` MUST be same as the value of ``transaction_id`` in the Deferred Credential Request.

If the Deferred Credential Request is invalid or the Digital Credential is not available, the Deferred Credential Error Response MUST be sent to the Wallet Instance according to :ref:`credential-issuance-endpoint:Credential Response`.

Notification endpoint
"""""""""""""""""""""

The Notification Endpoint is used by the Wallet to notify the Credential Issuer of certain events for issued Credentials, such as if the Credential was successfully stored in the Wallet Instance.

To uphold privacy, the ``event_description`` in the notification SHOULD NOT contain any information that could disclose User behavior or reveal the status of the personal device (e.g., storage space full).

This endpoint MUST be protected using a DPoP Access Token. TLS for the confidentiality of the HTTP transport is REQUIRED according to Section 11 of [`OpenID4VCI`_].


Notification Request
....................

The Notification Request MUST be an HTTP POST using the *application/json* media type with the following parameters.

.. list-table::
  :class: longtable
  :widths: 20 60 25
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **notification_id**
    - REQUIRED. It MUST be equal to the ``notification_id`` value returned in the Credential Response by the Credential Issuer.
    - Section 11.1 of [`OpenID4VCI`_].
  * - **event**
    - REQUIRED. Type of the notification event. It MUST be a case sensitive string and it MUST support the following values:

      - *credential_accepted*: when the Credential was successfully stored in the Wallet Instance.
      - *credential_deleted*: when the unsuccessful Credential issuance was caused by a user action.
      - *credential_failure*: in all other unsuccessful cases.


    - Section 11.1 of [`OpenID4VCI`_].
  * - **event_description**
    - OPTIONAL. Human-readable ASCII [USASCII] text providing additional information, used to inform about the event that occurred. Values for the event_description parameter MUST NOT include characters outside the set *%x20-21 / %x23-5B / %x5D-7E*.
    - Section 11.1 of [`OpenID4VCI`_].

Notification Response
.....................

The Notification Response MUST be use an HTTP status code *204 (No Content)*, as recommended in Section 11.2 of [`OpenID4VCI`_].

In case of errors, what is described in Section 11.3 of [`OpenID4VCI`_] MUST apply.

In case of the Notification Request does not contain a valid Access Token, the Notification Endpoint returns an error response such as defined in Section 3 of [:rfc:`6750`].
If any other error occurs, the Credential Issuer MUST return an error response as defined in Section 11.3 of [`OpenID4VCI`_]. The response MUST use the content type *application/json* and MUST include the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered.

Below is a non-normative example of an error response.

.. code-block:: http

  HTTP/1.1 400 Bad Request
  Content-Type: application/json
  Cache-Control: no-store

.. literalinclude:: ../../examples/notification-error.json
  :language: JSON

In the following table are listed HTTP Status Codes and related error codes that are supported for the error response:

.. _table_notification_error_code:
.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **error code**
      - **Description**
    * - *400 Bad Request* [REQUIRED]
      - ``invalid_notification_id``
      - The Credential Issuer cannot fulfill the request because of invalid ``notification_id`` parameter. Section 11.3 of [`OpenID4VCI`_].
    * - *400 Bad Request* [REQUIRED]
      - ``invalid_notification_request``
      - The Credential Issuer cannot fulfill the request because of missing parameters, invalid parameter or request malformed. Section 11.3 of [`OpenID4VCI`_].
    * - *500 Internal Server Error* [REQUIRED]
      - ``server_error``
      - The Credential Issuer encountered an internal problem.
    * - *503 Service Unavailable* [REQUIRED]
      - ``temporarily_unavailable``
      - The Credential Issuer is temporary unavailable.
    * - *504 Gateway Timeout* [OPTIONAL]
      - `-`
      - The Credential Issuer cannot fulfill the request within the defined time interval.


Data Correction using credential_failure
........................................

According to `OpenID4VCI`_ Section 11, in all other unsuccessful cases ``event`` MUST use ``credential_failure`` and additional Notification Request parameters MAY be defined and used. The Credential Issuer MUST ignore any unrecognized parameters.

For holder-initiated data correction, the Wallet Instance SHOULD send a Notification Request with ``event=credential_deleted`` and include additional parameters to signal the data correction context. At minimum:

- ``event_description``: concise human-readable description of the discrepancy.
- ``failure_reason`` (OPTIONAL): a short machine-readable code, e.g., ``data_correction_requested``.
- ``correction_details`` (OPTIONAL): object with minimal fields indicating impacted attributes without sensitive values (e.g., attribute identifiers only).

In the case of receiving a Credential failure that includes a stated reason, the Credential Issuer SHOULD forward the User's message containing that reason to the Authentic Source. It is RECOMMENDED to use PDND specific endpoints, provided by Authentic Source, to facilitate this data exchange.


