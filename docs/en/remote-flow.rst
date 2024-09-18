.. include:: ../common/common_definitions.rst
.. _Wallet Attestation: wallet-attestation.html
.. _Trust Model: trust.html



Remote Flow
===========

In this flow the Relying Party MUST provide the URL where the signed presentation Request Object is available for download.

Depending on whether the User is using a mobile device or a workstation, the Relying Party MUST support the following remote flows:

* **Same Device**, the Relying Party MUST provide a HTTP redirect (302) location to the Wallet Instance;
* **Cross Device**, the Relying Party MUST provide a QR Code which the User frames with the Wallet Instance.

Once the Wallet Instance establishes the trust with the Relying Party and evaluates the request, the User gives the consent for the disclosure of the Digital Credentials, in the form of a Verifiable Presentation.

A High-Level description of the remote flow, from the User's perspective, is given below:

  1. the Wallet Instance obtains an URL in the Same Device flow or a QR Code containing the URL in Cross Device flow;
  2. the Wallet Instance extracts from the payload the following parameters: ``client_id``, ``request_uri``, ``state``, ``request_uri_method`` and ``client_id_scheme``;
  3. If the ``client_id_scheme`` is provided and set with the value ``entity_id``, the Wallet Instance MUST collect and validate the OpenID Federation Trust Chain related to the Relying Party. If the ``client_id_scheme`` is either not provided or is assigned a value different from ``entity_id``, the Wallet Instance MUST establish the trust by utilizing the ``client_id`` or an alternative ``client_id_scheme`` value. This alternative value MUST enable the Wallet Instance to establish trust with the Relying Party, ensuring compliance with the assurance levels mandated by the trust framework;
  4. If ``request_uri_method`` is provided and set with the value ``post``, the Wallet Instance SHOULD transmit its metadata to the Relying Party's ``request_uri`` endpoint using the HTTP POST method and obtain the signed Request Object. If ``request_uri_method`` is set with the value ``get`` or not present, the Wallet Instance MUST fetch the signed Request Object using an HTTP request with method GET to the endpoint provided in the ``request_uri`` parameter;
  5. the Wallet Instance verifies the signature of the signed Request Object, using the public key identifier within the Request Object JWT header parameter to select the correct public key obtained within Trust Chain related to the RP;
  6. the Wallet Instance verifies that the ``client_id`` contained in the Request Object issuer (RP) matches with the one obtained at the step number 2 and with the ``sub`` parameter contained in the RP's Entity Configuration within the Trust Chain;
  7. the Wallet Instance evaluates the requested Digital Credentials and checks the elegibility of the Relying Party in asking these by applying the policies related to that specific Relying Party, obtained with the trust chain;
  8. the Wallet Instance asks User disclosure and consent;
  9. the Wallet Instance presents the requested information to the Relying Party along with the Wallet Attestation. The Relying Party validates the presented Credentials checking the trust with their Issuers, and validates the Wallet Attestation by also checking that the Wallet Provider is trusted;
  10. the Wallet Instance informs the User about the successfull authentication with the Relying Party, the User continues the navigation.

Below a sequence diagram that summarizes the interactions between all the involved parties.

.. figure:: ../../images/cross_device_auth_seq_diagram.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/ZLPDRnit4BtpLmpKGst3Tftq9i157DUrdRIrQYdn8Gu4YZkIM5FabX-hk4N_UuQabk36EaG80fYQz-RDcnbIRvpdreUDOZnueyDcWPOnTY6yiJ3wuD2EW3i8Z2tCbtpmeuDViPC2tGX--5skrlwj2iXQuf52jbnx63rmfT33hIPwBJ1nR8SXWQXE-0grpnauGzq0PHc6tQDwbde54pfyJf4TCiQ5bnttIC82dFn2w34yu0AcQACoqBoJA-wbqLKePmtMG1wH7OxX7ly9w3nChF4eF3PquaomWZATdzCnEfAPw62ovWxX_BpmHZqTzbIN5kCPXwCZHmWyEeAEapsFUc42rUSDbC8z26EUv1wupOBcmKgmlPGE-qh_khyq3SBTFTpCPXCIsqXBkk7WvxFNXx2LVlseXPAKOIwRuvhj69AgO_XK7SutwDUc-GoV2cZkn1et-9aSg-kCdvKreIMXnlLp04QhvvsTOGpJjTc2NsCliwLQ1yxpRzf7iEqOxbhK2VRDx01lssDGHd05F520zbBarjQaXPFcR0kPSYgu9XKGPPJ3go_UKcnAHPF6gNYq3fRMRE9PYKVTi0B2s4GYT-1jS3vvdAABO_lCOrnva4juwJL81mvtF9ExwOm1VRRz6BJMTB91rtj18Dvmpy4RoZgS3zBP6gbzOgYR1VGfarLLK7diKMWPZHMyvGkff9Ve62g7to7x-ce6ne8s7jgy8QogeKVdV4wkD3Rz6PZ5toXyyNnlFRa17VRpiPVYnNo-RDZW0e4_UYUvRg0rIWg9hg0-efNBvvIA-s0HpBAIN-w9kvoxeBYIJRMs5FbnSk0ESq0O5zpIM116Hwlshi2bqKjfDzWC9xjO6WS5BW9rmif_qmeGjMiZ8ppgt9MkdNlpXBfiUblTNdCN5XlfN5oU_VVNrSwtM7QsG_A5mk4Tc18KK6L0DLeNtgFByQSaBlzP1qpoZ5iIBbtSHD-x_HlISKBITzIdlRU2T6doB7OafZcjrEnINLgYqLvo1RVE1RGmYwkxeooItptCODhtks8XUGAToqjUg1Ypb1N1T6WfZDw_s-kRsVNzrTMVR3zYpE1oZU89Reng2FGUd-6jr0sDP192A2gR_asCSvXQGv0J28uYyYKL5ZIcy4J0_8P87S_h0hs1BerkRjiaT-YKCPYjKGDMLruZdL36OGFSUoiNmQCRWqWIvHB8vRAHqb9KNXQBm3ikLPo5k9Z91LRPzQ4j0n1_8y2k53Z8Jno4z7rp26ouilrxCkKRh9-JQl7Z6_VJgzDNyFhi3ExUKmF_6zdyvAKROpI6jVUjWs1LtW6xMugvC0t2_xizvAJIPOarlDQp7VnQe3e7pzttwIk_Ayex_Muwtit0yFtA6me7aQ3SQwc0RDhXYntTbN6nZsObEzGPdWXZxUuO0iKfHIFGfdOQ2ow8EAVBe8Qlyh0ngVetz5_OgAy0


    Remote Protocol Flow


The details of each step shown in the previous picture are described in the table below.

.. list-table::
  :widths: 10 50
  :header-rows: 1

  * - **Id**
    - **Description**
  * - **1**, **2**
    - The User requests to access to a protected resource of the Relying Party.
  * - **3**, **4**,
    - The Relying Party provides the Wallet Instance with a URL where the information about the Relying Party are provided, along with the information about where the signed request is available for download.
  * - **5**, **6**, **7**, **8**, **9**
    - In the **Cross Device Flow**, the Request URI is presented as a QR Code displayed to the User. The User scans the QR Code using the Wallet Instance, which retrieves a URL with the parameters ``client_id``, ``request_uri``, ``state``, ``client_id_scheme``, and ``request_uri_method``. Conversely, in the Same Device Flow, the Relying Party supplies identical information as in the Cross-Device flow, but directly through a URL.
  * - **10**, 
    - The Wallet Instance evaluates the trust with the Relying Party.
  * - **11**, **12**
    - The Wallet Instance checks if the Relying Party has provided the ``request_uri_method`` within its signed Request Object. If provided and it is equal to ``post``, the Wallet Instance provides its metadata to the Relying Party. The Relying Party returns a signed Request Object compliant to the Wallet technical capabilities.
  * - **13**
    - When the Wallet Instance capabilities discovery is not supported by RP, the Wallet Instance request the signed Request Object using the HTTP method GET.
  * - **14**
    - The RP issues the Request Object signin it using one of its cryptographic private keys, where their public parts have been published within its Entity Configuration (`metadata.wallet_relying_party.jwks`). The Wallet Instance obtains the signed Request Object.
  * - **15**, **16**, **17**
    - The Request Object JWS is verified by the Wallet Instance. The Wallet Instance processes the Relying Party metadata and applies the policies related to the Relying Party, attesting whose Digital Credentials and User data the Relying Party is granted to request.
  * - **18**, **19**
    - The Wallet Instance requests the User's consent for the release of the Credentials. The User authorizes and consents the presentation of the Credentials by selecting/deselecting the personal data to release.
  * - **20**
    - The Wallet Instance provides the Authorization Response to the Relying Party using an HTTP request with the method POST (response mode "direct_post.jwt").
  * - **21**, **22**, **23**, **24**, **25** 
    - The Relying Party verifies the Authorization Response, extracts the Wallet Attestation to establish the trust with the Wallet Solution. The Relying Party extracts the Digital Credentials and attests the trust to the Credentials Issuer and the proof of possession of the Wallet Instance about the presented Digital Credentials. Finally, the Relying Party verifies the revocation status of the presented Digital Credentials.
  * - **26** (Same Device Flow only)
    - The Relying Party provides to the Wallet Instance a redirect URI with a response code to be used by the Wallet Instance to finalize the authentication.
  * - **27**, **28** and **29**
    - The User is informed by the Wallet Instance that the Autentication succeded, then the protected resource is made available to the User.


Request URI with HTTP POST
--------------------------

The Relying Party SHOULD provide the POST method with its ``request_uri`` endpoint
allowing the Wallet Instance to inform the Relying Party about its technical capabilities.

This feature can be useful when, for example, the Wallet Instance supports 
a restricted set of features, supported algorithms or a specific url for 
its ``authorization_endpoint``, and any other information that it deems necessary to
provide to the Relying Party for better interoperability.

.. warning::
    The Wallet Instance, when providing its technical capabilities to the 
    Relying Party, MUST NOT include any User information or other explicit 
    information regarding the hardware used or usage preferences of its User.

If both the Relying Party and the Wallet Instance
support the ``request_uri_method`` with HTTP POST,
the Wallet Instance capabilities (metadata) MUST 
be provided using an HTTP request to the `request_uri` endpoint of the Relying Party, 
with the method POST and content type set to `application/json`.

A non-normative example of the HTTP request is represented below:
    
.. code:: http

  POST /request-uri HTTP/1.1
  HOST: relying-party.example.org
  Content-Type: application/json

  {
      "authorization_endpoint": "https://wallet-solution.digital-strategy.europa.eu/authorization",
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
      "presentation_definition_uri_supported": false
  }

The response of the Relying Party is defined in the section below.


Authorization Request Details
-----------------------------

The Relying Party MUST create a Request Object in the form of a signed JWT and
MUST provide it to the Wallet Instance through an HTTP URL (request URI). 
The HTTP URL points to the web resource where the signed Request Object is 
available for download. The URL parameters contained in the Relying Party 
response, containing the request URI, are described in the Table below.

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **client_id**
    - REQUIRED. Unique identifier of the Relying Party.
  * - **request_uri**
    - REQUIRED. The HTTPs URL where the Relying Party provides the signed Request Object to the Wallet Instance.
  * - **client_id_scheme**
    - OPTIONAL. The scheme used by the Relying Party for the client_id, detailing the format and structure and the trust evaluation method. It SHOULD be set with ``entity_id``.
  * - **state**
    - OPTIONAL. A unique identifier for the current transaction generated by the Relying Party. The value SHOULD be opaque to the Wallet Instance.
  * - **request_uri_method**
    - OPTIONAL. The HTTP method MUST be set with ``get`` or ``post``. The Wallet Instance should use this method to obtain the signed Request Object from the request_uri. If not provided or equal to ``get``, the Wallet Instance SHOULD use the HTTP method ``get``. Otherwise, the Wallet Instance SHOULD provide its metadata within the HTTP POST body encoded in ``application/json``.    
    
Below a non-normative example of the response containing the required parameters previously described.

.. code-block:: javascript

  https://wallet-solution.digital-strategy.europa.eu/authorization?client_id=...&request_uri=...&client_id_scheme=entity_id&request_uri_method=post

The value corresponding to the `request_uri` endpoint SHOULD be randomized, according to `RFC 9101, The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR) <https://www.rfc-editor.org/rfc/rfc9101.html#section-5.2.1>`_ Section 5.2.1.


In the **Same Device Flow** the Relying Party uses an HTTP response redirect (with status code set to 302) as represented in the following non-normative example:

.. code:: text

    HTTP/1.1 /authorization Found
    Location: https://wallet-solution.digital-strategy.europa.eu?
    client_id=https%3A%2F%2Frelying-party.example.org%2Fcb
    &request_uri=https%3A%2F%2Frelying-party.example.org%2Frequest_uri
    &client_id_scheme=entity_id
    &request_uri_method=post


In the **Cross Device Flow**, a QR Code is shown by the Relying Party to the User in order to provide the Authorization Request. The User frames the QR Code using their Wallet Instance.

Below is represented a non-normative example of a QR Code issued by the Relying Party.

.. figure:: ../../images/verifier_qr_code.svg
    :figwidth: 50%
    :align: center


Below is represented a non-normative example of the QR Code raw payload:

.. code-block:: text

  https://wallet-solution.digital-strategy.europa.eu/authorization?client_id=https%3A%2F%2Frelying-party.example.org&request_uri=https%3A%2F%2Frelying-party.example.org&client_id_scheme=entity_id&request_uri_method=post

.. note::
    The *error correction level* chosen for the QR Code MUST be Q (Quartily - up to 25%), since it offers a good balance between error correction capability and data density/space. This level of quality and error correction allows the QR Code to remain readable even if it is damaged or partially obscured.


Cross Device Flow Status Checks and Security
--------------------------------------------

When the flow is Cross Device, the user-agent needs to check the session status to the endpoint made available by Relying Party (status endpoint). This check MAY be implemented in the form of JavaScript code, within the page that shows the QRCode, then the user-agent checks the status with a polling strategy in seconds or a push strategy (eg: web socket).

Since the QRcode page and the status endpoint are implemented by the Relying Party, it is under the Relying Party responsability the implementation details of this solution, since it is related to the Relying Party's internal API. However, the text below describes an implementation example.

The Relying Party binds the request of the user-agent, with a session cookie marked as ``Secure`` and ``HttpOnly``, with the issued request. The request url SHOULD include a parameter with a random value. The HTTP response returned by this specialized endpoint MAY contain the HTTP status codes listed below:

* **201 Created**. The signed Request Object was issued by the Relying Party that waits to be downloaded by the Wallet Instance at the **request_uri** endpoint.
* **202 Accepted**. This response is given when the signed Request Object was obtained by the Wallet Instance.
* **200 OK**. The Wallet Instance has provided the presentation to the Relying Party's  **response_uri** endpoint and the User authentication is successful. The Relying Party updates the session cookie allowing the user-agent to access to the protected resource. An URL is provided carrying the location where the user-agent is intended to navigate.
* **401 Unauthorized**. The Wallet Instance or its User have rejected the request, or the request is expired. The QRCode page SHOULD be updated with an error message.

Below a non-normative example of the HTTP Request to this specialized endpoint, where the parameter ``id`` contains an opaque and random value:

.. code::

  GET /session-state?id=3be39b69-6ac1-41aa-921b-3e6c07ddcb03
  HTTP/1.1
  HOST: relying-party.example.org


Request Object Details
----------------------

Below a non-normative example of HTTP request made by the Wallet Instance to the Relying Party.

.. code-block:: javascript

  GET /request_uri HTTP/1.1
  HOST: relying-party.example.org


Request URI Response
--------------------

The Relying Party issues the signed Request Object using the content type set to ``application/oauth-authz-req+jwt``,
where a non-normative example in the form of decoded header and payload is shown below:

.. code-block:: text

  {
    "alg": "ES256",
    "typ": "JWT",
    "kid": "9tjiCaivhWLVUJ3AxwGGz_9",
    "trust_chain": [
      "MIICajCCAdOgAwIBAgIC...awz",
      "MIICajCCAdOgAwIBAgIC...2w3",
      "MIICajCCAdOgAwIBAgIC...sf2"
    ]
  }
  .
  {
    "scope": "PersonIdentificationData WalletAttestation",
    "client_id_scheme": "entity_id",
    "client_id": "https://relying-party.example.org",
    "response_mode": "direct_post.jwt",
    "response_type": "vp_token",
    "response_uri": "https://relying-party.example.org/response_uri",
    "nonce": "2c128e4d-fc91-4cd3-86b8-18bdea0988cb",
    "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
    "iss": "https://relying-party.example.org",
    "iat": 1672418465,
    "exp": 1672422065,
    "request_uri_method": "post"
  }

The JWS header parameters are described below:

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **alg**
    - Algorithm used to sign the JWT, according to [:rfc:`7516#section-4.1.1`]. It MUST be one of the supported algorithms in Section *Cryptographic Algorithms* and MUST NOT be set to ``none`` or to a symmetric algorithm (MAC) identifier.
  * - **typ**
    - Media Type of the JWT, as defined in [:rfc:`7519`].
  * - **kid**
    - Key ID of the public key needed to verify the JWS signature, as defined in [:rfc:`7517`]. REQUIRED when ``trust_chain`` is used.
  * - **trust_chain**
    - Sequence of Entity Statements that composes the Trust Chain related to the Relying Party, as defined in `OID-FED`_ Section *3.2.1. Trust Chain Header Parameter*.


The JWS payload parameters are described herein:

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **scope**
    - Aliases for well-defined Presentation Definitions IDs. It is used to identify which required Credentials and User attributes are requested by the Relying Party, according to the Section "Using scope Parameter to Request Verifiable Credential(s)" of [OID4VP].
  * - **client_id_scheme**
    - String identifying the scheme of the value in the ``client_id``. It MUST be set to the value ``entity_id``.
  * - **client_id**
    - Unique Identifier of the Relying Party.
  * - **response_mode**
    - It MUST be set to ``direct_post.jwt``.
  * - **response_type**
    - It MUST be set to ``vp_token``.
  * - **response_uri**
    - The Response URI to which the Wallet Instance MUST send the Authorization Response using an HTTP request using the method POST.
  * - **nonce**
    - Fresh cryptographically random number with sufficient entropy, which length MUST be at least 32 digits.
  * - **state**
    - Unique identifier of the Authorization Request.
  * - **iss**
    - The entity that has issued the JWT. It will be populated with the Relying Party client id.
  * - **iat**
    - Unix Timestamp, representing the time at which the JWT was issued.
  * - **exp**
    - Unix Timestamp, representing the expiration time on or after which the JWT MUST NOT be valid anymore.
  * - **request_uri_method**
    - String determining the HTTP method to be used with the `request_uri` endpoint to provide the Wallet Instance metadata to the Relying Party. The value is case-insensitive and can be set to: `get` or `post`. The GET method, as defined in [@RFC9101], involves the Wallet Instance  sending a GET request to retrieve a Request Object. The POST method involves the Wallet Instance requesting the creation of a new Request Object by sending an HTTP POST request, with its metadata, to the request URI of the Relying Party.

.. warning::

    Using the parameter ``scope`` requires that the Relying Party Metadata MUST contain the ``presentation_definition``, where a non-normative example of it is given below:

.. literalinclude:: ../../examples/presentation-definition.json
  :language: JSON

.. note::

  The following parameters, even if defined in [OID4VP], are not mentioned in the previous non-normative example, since their usage is conditional and may change in future release of this documentation.

  - ``presentation_definition``: JSON object according to `Presentation Exchange <https://identity.foundation/presentation-exchange/spec/v2.0.0/>`_. This parameter MUST not be present when ``presentation_definition_uri`` or ``scope`` are present.
  - ``presentation_definition_uri``: Not supported. String containing an HTTPS URL pointing to a resource where a Presentation Definition JSON object can be retrieved. This parameter MUST be present when ``presentation_definition`` parameter or a ``scope`` value representing a Presentation Definition is not present. 
  - ``client_metadata``: A JSON object containing the Relying Party metadata values. If the ``client_metadata`` parameter is present when ``client_id_scheme`` is ``entity_id``, the Wallet Instance MUST consider the client metadata obtained through the OpenID Federation Trust Chain.


Request URI Endpoint Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the Relying Party encounters errors while issuing the Request Object from the ``request_uri`` endpoint, the following error responses are applicable:

- **invalid_request**: The ``request_uri`` URL is missing in some part within its webpath or urlparams, therefore it does not point to a valid Request Object and then it cannot be retrieved. This error is returned when the Request Object is not well referenced in the ``request_uri``.

- **server_error**: The server encountered an unexpected condition that prevented it from fulfilling the request. This error is returned when the Relying Party's server is unable to process the Request Object due to a server-side issue, such as a malfunction or maintenance. The Wallet Instance should advise the User to try again later.

The following is an example of an error response from ``request_uri`` endpoint:

.. code-block:: 

  HTTP/1.1 400 Bad Request
  Content-Type: application/json

  {
   "error": "invalid_request",
   "error_description": "The request_uri is malformed or does not point to a valid Request Object."
  }


Another example:

.. code-block:: 

  HTTP/1.1 500 Internal Server Error
  Content-Type: application/json

  {
   "error": "server_error",
   "error_description": "The request_uri cannot be retrieved due to an internal server error."
  }

There are cases where the Wallet Instance cannot validate the Request Object or the Request Object results invalid. This error occurs if the Request Object is successfully fetched from the ``request_uri`` but fails validation checks by the Wallet Instance. This could be due to incorrect signatures, malformed claims, or other validation failures, such as the revocation of its issuer (Relying Party). 

Upon receiving an error response, the Wallet Instance SHOULD inform the User of the error condition in an appropriate manner. Additionally, the Wallet Instance SHOULD log the error and MAY attempt to recover from certain errors if feasible. For example, if the error is ``server_error``, the Wallet Instance MAY prompt the User to re-enter or scan a new QR code, if applicable.

It is crucial for Wallet Instances to implement robust error handling to maintain a secure and user-friendly experience. Adhering to the specified error responses ensures interoperability and helps in diagnosing issues during the interaction with the Relying Party's endpoints.

.. warning::

  The current OpenID4VP specification outlines various error responses that a Wallet Instance may return to the Relying Party (Verifier) in case of faulty requests (OpenID4VP, Section 6.4. Error Response). For privacy enhancement, Wallet Instances SHOULD NOT notify the Relying Party of faulty requests in certain scenarios. This is to prevent any potential misuse of error responses that could lead to gather informations that could be exploited.


Authorization Response Details
------------------------------

After getting the User authorization and consent for the presentation of the Credentials, the Wallet Instance sends the Authorization Response to the Relying Party ``response_uri`` endpoint, the content SHOULD be encrypted according `OpenID4VP`_ Section 6.3, using the Relying Party public key.

.. note::
    **Why the response is encrypted?**

    The response sent from the Wallet Instance to the Relying Party is encrypted to prevent a malicious agent from gaining access to the plaintext information transmitted within the Relying Party's network. This is only possible if the network environment of the Relying Party employs `TLS termination <https://www.f5.com/glossary/ssl-termination>`_. Such technique employs a termination proxy that acts as an intermediary between the client and the webserver and handles all TLS-related operations. In this manner, the proxy deciphers the transmission's content and either forwards it in plaintext or by negotiates an internal TLS session with the actual webserver's intended target. In the first scenario, any malicious actor within the network segment could intercept the transmitted data and obtain sensitive information, such as an unencrypted response, by sniffing the transmitted data.

Below a non-normative example of the request:

.. code-block:: http

  POST /response_uri HTTP/1.1
  HOST: relying-party.example.org
  Content-Type: application/x-www-form-urlencoded
  
  response=eyJhbGciOiJFUzI1NiIs...9t2LQ
  

Below is a non-normative example of the decrypted payload of the JWT contained in the ``response``, before base64url encoding:

.. code-block:: 

  {
    "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
    "vp_token": [
        "eyJhbGciOiJFUzI1NiIs...PT0iXX0",
        $WalletAttestation-JWT
    ],
    "presentation_submission": {
        "definition_id": "32f54163-7166-48f1-93d8-ff217bdb0653",
        "id": "04a98be3-7fb0-4cf5-af9a-31579c8b0e7d",
        "descriptor_map": [
            {
                "id": "PersonIdentificationData",
                "path": "$.vp_token[0]",
                "format": "vc+sd-jwt"
            },
            {
                "id": "WalletAttestation",
                "path": "$.vp_token[1]",
                "format": "wallet-attestation+jwt"
            }
        ]
    }
  }

Where the following parameters are used:

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **vp_token**
    - JSON Array containing the Verifiable Presentation(s). There MUST be at least two signed presentations in this Array:

      - The requested Digital Credential (one or more, in format of SD-JWT VC or MDOC CBOR)
      - The Wallet Attestation
  * - **presentation_submission**
    - JSON Object containing the mappings between the requested Verifiable Credentials and where to find them within the returned Verifiable Presentation Token, according to the `Presentation Exchange <https://identity.foundation/presentation-exchange/spec/v2.0.0/>`_. This is expressed via elements in the ``descriptor_map`` array (Input Descriptor Mapping Objects) that contain a field called ``path``, which MUST have the value $ (top level root path) when only one Verifiable Presentation is contained in the VP Token, and MUST have the value $[n] (indexed path from root) when there are multiple Verifiable Presentations, where ``n`` is the index to select. The Relyingh PArty receiving the `presentation_submission` descriptor therefore is able to use the corred method to decode each credential data format provided withi nthe ``vp_token``.
  * - **state**
    - Unique identifier provided by the Relying Party within the Authorization Request.


The items contained in the ``vp_token`` array are Verifiable Presentations of Credentials.
Both SD-JWT and mdoc CBOR provide indications for the presentation, according to their specifications.

SD-JWT Presentation
-------------------

SD-JWT defines how an Holder can present a Credential to a Verifier proving the legitimate possession
of the Credential. For doing this the Holder MUST include the ``KB-JWT`` in the SD-JWT,
by appending the ``KB-JWT`` at the end of the of the SD-JWT, as represented in the example below:

.. code-block::

  <Issuer-Signed-JWT>~<Disclosure 1>~<Disclosure 2>~...~<Disclosure N>~<KB-JWT>

To validate the signature on the Key Binding JWT, the Verifier MUST use the key material included in the Issuer-Signed-JWT.
The Key Binding JWT MUST specify which key material the Verifier needs to use to validate the Key Binding JWT signature,
using JOSE header parameter ``kid``.

When an SD-JWT is presented, its KB-JWT MUST contain the following parameters in the JWS header:

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Claim**
    - **Description**
  * - **typ**
    - REQUIRED. MUST be ``kb+jwt``, which explicitly types the Key Binding JWT as recommended in Section 3.11 of [RFC8725].
  * - **alg**
    - REQUIRED. Signature Algorithm using one of the specified in the section Cryptographic Algorithms. 
  * - **kid**
    - REQUIRED. Unique identifier of the public key to be used to verify the signature.


When an SD-JWT is presented, its KB-JWT MUST contain the following parameters in the JWS payload:

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Claim**
    - **Description**
  * - **iat**
    - REQUIRED. The value of this claim MUST be the time at which the Key Binding JWT was issued, using the syntax defined in [RFC7519].
  * - **aud**
    - REQUIRED. The intended receiver of the Key Binding JWT. How the value is represented is up to the protocol used and out of scope of this specification.
  * - **nonce**
    - REQUIRED. Ensures the freshness of the signature. The value type of this claim MUST be a string. The value MUST match with the one provided in the request object.
  * - **sd_hash**
    - REQUIRED. The base64url-encoded hash digest over the Issuer-signed JWT and the selected disclosures.


MDOC-CBOR Presentation
----------------------

TBD.


Authorization Response Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the Wallet sends a response using ``direct_post.jwt`` to the Relying Party, several errors may occur, including:

  - **Invalid Credential**: This error occurs when one or more Credentials or VPs, included in the ``vp_token``, fail validation because they are malformed. The correct HTTP status code for this error is 400 (Bad Request). The error should be set to ``invalid_request``, and the ``error_description`` SHOULD identify the malformed Credentials.
  - **Issuer Credential Trust Failure**: This error arises when the Relying Party cannot establish trust with the issuer of a presented Credential, included in the ``vp_token``. The appropriate HTTP status code for this error is 403 (Forbidden). The ``error`` should be labeled as ``invalid_request``, and the ``error_description`` SHOULD specify the issuer for which trust could not be established.
  - **Invalid Nonce**: This error happens when the nonce provided in the request is incorrect. The HTTP status code for this error should be 403 (Forbidden). The error SHOULD be labeled as ``invalid_request``, with an ``error_description`` indicating that the nonce is incorrect.
  - **Invalid Wallet Attestation**: This error occours when it's not possible to establish trust with the Wallet Attestation's issuer (Wallet Provider), or if the Wallet Attestation is invalid or does not meet the Relying Party's minimum security criteria. The correct HTTP status code for this error is 403 (Forbidden). The ``error`` SHOULD be marked as ``invalid_request``, and the ``error_description`` should clarify that the issue stems from the Wallet Attestation's failure to establish trust with its issuer or its non-compliance with required security standards.
  - **Invalid Presentation Submission**: This error occurs when the presentation submission is not valid. The appropriate HTTP status code for this error is 400 Bad Request. The ``error`` should be labeled as ``invalid_request``, and the ``error_description`` should specify the invalid aspects of the presentation submission.
  
  To enhance clarity and ensure proper error handling, it's crucial to provide detailed error responses. Below are two examples of HTTP responses using ``application/json`` that include both the ``error`` and ``error_description`` members:

.. code-block:: text

  HTTP/1.1 403 Forbidden
  Content-Type: application/json

  {
    "error": "invalid_request",
    "error_description": "Trust cannot be established with the issuer: https://issuer.example.com"
  }


.. code-block:: text

  HTTP/1.1 400 Bad Request
  Content-Type: application/json

  {
    "error": "invalid_request",
    "error_description": "The following Credentials/VP are malformed: [CredentialX, vp_token[2]]"
  }

Redirect URI
------------

When the Relying Party provides the redirect URI, the Wallet Instance MUST send the user-agent to this redirect URI. The redirect URI allows the Relying Party to continue the interaction with the End-User on the device where the Wallet Instance resides after the Wallet Instance has sent the Authorization Response to the response URI.

The Relying Party MUST include a response code within the redirect URI. The response code is a fresh, cryptographically random number used to ensure only the receiver of the redirect can fetch and process the Authorization Response. The number could be added as a path component, as a parameter or as a fragment to the URL. It is RECOMMENDED to use a cryptographic random value of 128 bits or more at the time of the writing of this specification.

The following is a non-normative example of the response from the Relying Party to the Wallet Instance upon receiving the Authorization Response at the Response Endpoint.


.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json

  {
    "redirect_uri": "https://relying-party.example.org/cb?response_code=091535f699ea575c7937fa5f0f454aee"
  }

The ``redirect_uri`` value MUST be used with an HTTP method GET by either the Wallet Instance or the user-agent to redirect the User to the Relying Party in order to complete the process. The value can be added as a path component, as a fragment or as a parameter to the URL according to Section 6.2 of `OpenID4VP`_. The specific entity that performs this action depends on whether the flow is Same device or Cross device.

Redirect URI Errors
-------------------

When the Wallet Instance sends the user-agent to the Redirect URI provided by the Relying Party, several errors may occur that prevent the successful completion of the process. These errors are critical as they directly impact the User experience by hindering the seamless flow of information between the Wallet Instance and the Relying Party. Below are potential errors related to the Redirect URI and their implications:

- **Mismatched Redirect URI**: This error occurs when the Redirect URI provided by the Relying Party does not match any of the URIs linked with the User session. This mismatch can lead to a HTTP status error code set to 403 (Forbidden), indicating that the request cannot be processed due session/URI mismatch.

- **Redirect URI Security Issues**: If the Relying Party incurs in security issues when evaluating the User session with the provided URI, the Relying Party MUST raise an error. In such cases, an HTTP status code set to 403 (Forbidden) MUST be returned, indicating that the request is valid but the server is refusing action due to security precautions.

Handling these errors requires clear communication to the User within the returned navigation web page. It is crucial for the Relying Party to implement robust error handling and validation mechanisms for Redirect URIs to ensure a secure implementation.


