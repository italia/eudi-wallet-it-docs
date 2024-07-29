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
  5. the Wallet Instance verifies the signature of the signed Request Object, using the public key obtained with the trust chain, and that its issuer matches the ``client_id`` obtained at the step number 2;
  6. the Wallet Instance evaluates the requested Digital Credentials and checks the elegibility of the Relying Party in asking these by applying the policies related to that specific Relying Party, obtained with the trust chain;
  7. the Wallet Instance asks User disclosure and consent;
  8. the Wallet Instance presents the requested information to the Relying Party along with the Wallet Attestation. The Relying Party validates the presented Credentials checking the trust with their Issuers, and validates the Wallet Attestation by also checking that the Wallet Provider is trusted;
  9. the Wallet Instance informs the User about the successfull authentication with the Relying Party, the User continues the navigation.

Below a sequence diagram that summarizes the interactions between all the involved parties.

.. figure:: ../../images/cross_device_auth_seq_diagram.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/ZLLRRnit4ttdhpZGz_3PXkCcwPi05t5SDvUqjMefoKCI21Ht9B6co2qlgxX5_tjdIUo2SWIqXc5Or5pEd3apyo94wMFQ6I5JT3RjLkI545SgEe_9-q1-0XcGX5Yvh-NX_m4_KgSLXGd-zxFUREDBaqYq74ShtKeRCVaeZQ68DvR3MqKvnlxG976e9t93DfOCKf1jm5aEpUx8F6YxmOmV7x9bHq985NKd8p6mX2S_iFSK7sc5EVaU6Qpiz4P6xMnbAaL3jQFiFJkQuex-I1GYPjv5Kf4QVWakUSMPBY_vcGB3pE4msyf0kBmSu_PuEXf2NNlgtoJEpW9xqDaPEidqVBOhbxY-w30M7g6SkzT7t7q1j4nUmmzGEXeg_UtksZM4spkyNYnc3BRHdd7ZvFkdpq-nrt7xsIgZESDID-Trj7DaLEVuL3qkTnIthlc2JwFJCgWjxUXBnLZcdNystgMMWRemw03EceT29z8KywtR8svfWDbohGVCoqVjOxVz5BSjsUpsI3kGRNiEuvGqa8aDB8kZjBOEEiPadUrHGiwLj8m2FOpnyUPhz6oRKx7I91TFFc3jtIw_3VPa6p4wKTz43XuGVGenSvojHyQEaIUaYT1hVCirT42W4WUps_b20C1-a47hNQSR2WCNx2GR6IMYorbhVJ3ErcaRSuIwMG0mAgkgeE8uahAw9rR9LgwqqL5J46G2_GVOhsuMS1xMHRHbGaHLm-1TyWMziTGCRt2htqd5aVFZzUG6T3JeusY8n_eyqh231O9V1YQbRT0wenLNF7fz8A_N3pcLZCaJtBg2F-w9sv9xz996DzNOikM7sKauBGPfElgjdOToDbDrR0IkdLrhlwFcKDa3fLaek4hS2Q__BEk85rNRHyHdMxhIjSlexicEazvMssiPqcgdG-1_Z-ylt1JUA9UTwT1oPUXm1-O4erD5G2MjgyZa5_iB1bS-rWQped7Fm7L0l_C7jdyYViwU_1ttwUXMq24hprF7O9gB2ar9rQ_IXX5hQV0cX4GUYtvqIyWHCjv-N60-zBkAml0KXQ9UDOOImdDMWkl8indVlpUlNYzUtTtS_2gEUqm5hhUaxl7QcOQTtj43NchRi2Gp4FRYilbtvaAWt1fsUO8KsA8igRHYcUAU7SiDqNbFrWL6XovBjxHjLZfq8GGMMxAWQkKrEYZZ0ZMGCNgzIapM52f3r6imo-D4Qaw0CYoU83kf3MiXRyRCWgZeUj-E0dWVo2EKKd1IJXnI_huvHJNH_V7wxjd5Cpn_-XItxxWpVqrykMLv5KocsCRO1YHlYhWz5RKlbMi8Vul7urzkqrpkwE0qxOV3oT0on3fB7MClwYl5TVxRkUjelCPlvzFIwKTNgimXJlfgn-sLgodKd7upYGKihew5sUYER77F0NiYmZaIsnd3ZMvpqvn7IAfNupgPmzjxI5ckyGN_IJlp3m00


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
    - The Wallet Instance obtains the signed Request Object.
  * - **15**, **16**, **17**
    - The Request Object JWS is verified by the Wallet Instance. The Wallet Instance processes the Relying Party metadata and applies the policies related to the Relying Party, attesting whose Digital Credentials and User data the Relying Party is granted to request.
  * - **18**, **19**
    - The Wallet Instance requests the User's consent for the release of the Credentials. The User authorizes and consents the presentation of the Credentials by selecting/deselecting the personal data to release.
  * - **20**
    - The Wallet Instance provides the Authorization Response to the Relying Party using an HTTP request with the method POST (response mode "direct_post.jwt").
  * - **21**, **22**, **23**, **24**, **25** 
    - The Relying Party verifies the Authorization Response, extracts the Wallet Attestation to establish the trust with the Wallet Solution. The Relying Party extracts the Digital Credentials and attests the trust to the Credentials Issuer and the proof of possession of the Wallet Instance about the presented Digital Credentials. Finally, the Relying Party verifies the revocation status of the presented Digital Credentials.
  * - **26**
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

Since the QRcode page and the status endpoint are implemented by the Relying Party, it is under the Relying Party responsability the implementation details of this solution, since it is related to the Relying Party's internal API. However, the text below offers an implementation solution.

The Relying Party MUST bind the request of the user-agent, with a session cookie marked as ``Secure`` and ``HttpOnly`` , with the issued request. The request url SHOULD include a parameter with a random value. The HTTP response returned by this specialized endpoint MAY contain the HTTP status codes listed below:

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

The Relying Party issues the signed Request Object, where a non-normative example in the form of decoded header and payload is shown below:

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
  - ``client_metadata``: A JSON object containing the Relying Party metadata values. The ``client_metadata`` parameter MUST NOT be present when ``client_id_scheme`` is ``entity_id``. Since the ``client_metadata`` is taken from ``trust_chain``, this parameter is intended to not be used.
  - ``client_metadata_uri``: string containing an HTTPS URL pointing to a resource where a JSON object with the Relying Party metadata can be retrieved. The ``client_metadata_uri`` parameter MUST NOT be present when ``client_id_scheme`` is ``entity_id``. Since the ``client_metadata`` is taken from ``trust_chain``, this parameter is intended to not be used.


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
  

Below is a non-normative example of the decrypted JSON ``response`` content:

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
                "path": "$.vp_token[0].vp",
                "format": "vc+sd-jwt"
            },
            {
                "id": "WalletAttestation",
                "path": "$.vp_token[1].vp",
                "format": "jwt"
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
    - JSON Object containing the mappings between the requested Verifiable Credentials and where to find them within the returned Verifiable Presentation Token, according to the `Presentation Exchange <https://identity.foundation/presentation-exchange/spec/v2.0.0/>`_.
  * - **state**
    - Unique identifier provided by the Relying Party within the Authorization Request.


Below is a non-normative example of the ``vp_token`` decoded content, represented in the form of JWS header and payload, separated by a period:

.. code-block:: text

   {
     "alg": "ES256",
     "typ": "JWT"
   }
   .
   {
     "iss": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
     "jti": "3978344f-8596-4c3a-a978-8fcaba3903c5",
     "aud": "https://relying-party.example.org/response_uri",
     "iat": 1541493724,
     "exp": 1573029723,
     "nonce": "2c128e4d-fc91-4cd3-86b8-18bdea0988cb",
     "vp": "<Issuer-Signed-JWT>~<Disclosure 1>~<Disclosure 2>~...~<Disclosure N>"
   }

Where the following parameters are used:

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **vp**
    - The Digital Credential in its original state. The public key contained in the Digital Credential MUST be used to verify the entire VP JWS as Proof of Possession of the private key which the public key is included in the Digital Credential. Eg: for SD-JWT VC the public key is provided within the ``cnf.jwk`` claim.
  * - **jti**
    - JWS unique identifier.
  * - **iat**
    - Unix timestamp of the time of issuance of this presentation.
  * - **exp**
    - Unix timestamp beyond which this presentation will no longer be considered valid.
  * - **aud**
    - Audience of the VP, corresponding to the ``response_uri`` within the Authorization request issued by the Relying Party.
  * - **nonce**
    - The nonce value provided by the Relying Party within the Authorization Request.


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
  Content-Type: application/json;charset=UTF-8

  {
    "redirect_uri": "https://relying-party.example.org/cb#response_code=091535f699ea575c7937fa5f0f454aee"
  }

The ``redirect_uri`` value MUST be used with an HTTP method GET by either the Wallet Instance or the user-agent to redirect the User to the Relying Party in order to complete the process. The specific entity that performs this action depends on whether the flow is Same device or Cross device.

Redirect URI Errors
-------------------

When the Wallet Instance sends the user-agent to the Redirect URI provided by the Relying Party, several errors may occur that prevent the successful completion of the process. These errors are critical as they directly impact the User experience by hindering the seamless flow of information between the Wallet Instance and the Relying Party. Below are potential errors related to the Redirect URI and their implications:

- **Mismatched Redirect URI**: This error occurs when the Redirect URI provided by the Relying Party does not match any of the URIs linked with the User session. This mismatch can lead to a HTTP status error code set to 403 (Forbidden), indicating that the request cannot be processed due session/URI mismatch.

- **Redirect URI Security Issues**: If the Relying Party incurs in security issues when evaluating the User session with the provided URI, the Relying Party MUST raise an error. In such cases, an HTTP status code set to 403 (Forbidden) MUST be returned, indicating that the request is valid but the server is refusing action due to security precautions.

Handling these errors requires clear communication to the User within the returned navigation web page. It is crucial for the Relying Party to implement robust error handling and validation mechanisms for Redirect URIs to ensure a secure implementation.


