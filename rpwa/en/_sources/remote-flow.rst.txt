.. include:: ../common/common_definitions.rst
.. _Wallet Attestation: wallet-attestation.html
.. _Trust Model: trust.html

.. _remote_flow_sec:

Remote Flow
===========

In this flow the Relying Party MUST provide the URL where the signed presentation Request Object is available for download.

Depending on whether the User is using a mobile device or a workstation, the Relying Party MUST support the following remote flows:

* **Same Device**, the Relying Party MUST provide a HTTP redirect (302) location to the Wallet Instance;
* **Cross Device**, the Relying Party MUST provide a QR Code which the User frames with the Wallet Instance.

Once the Wallet Instance establishes the trust with the Relying Party and evaluates the request, the User gives the consent for the disclosure of the Digital Credentials, in the form of a Verifiable Presentation.

A High-Level description of the remote flow, from the User's perspective, is given below:

  1. the Wallet Instance scans the QR Code and obtains the URL (Cross Device flow) or obtain directly an URL (Same Device flow);
  2. the Wallet Instance extracts from the payload the following parameters: ``client_id``, ``request_uri``, ``request_uri_methods`` and ``client_id_scheme``;
  3. If the ``client_id_scheme`` is provided and set with the value ``entity_id``, the Wallet Instance MUST collect and validate the OpenID Federation Trust Chain related to the Relying Party. If the ``client_id_scheme`` is either not provided or is assigned a value different from ``entity_id``, the Wallet MUST establish the trust by utilizing the ``client_id`` or an alternative ``client_id_scheme`` value. This alternative value MUST enable the Wallet Instance to establish trust with the Relying Party, ensuring compliance with the assurance levels mandated by the trust framework;
  4. If ``request_uri_methods`` is provided and set with the value ``post``, the Wallet SHOULD transmit its metadata to the Relying Party's ``request_uri`` endpoint using the HTTP POST method and obtain the signed Request Object. If ``request_uri_methods`` is set with the value ``get`` or not present, the Wallet Instance MUST fetch the signed Request Object using an HTTP request with method GET to the endpoint provided in the ``request_uri`` parameter;
  5. the Wallet verifies the signature of the signed Request Object, using the public key obtained with the trust chain, and that its issuer matches the ``client_id`` obtained at the step number 2;
  6. The Wallet Instance evaluates the requested Digital Credentials and checks the elegibility of the Relying Party in asking these by applying the policies related to that specific Relying Party, obtained with the trust chain;
  7. the Wallet Instance asks User disclosure and consent;
  8. the Wallet Instance presents the requested information to the Relying Party along with the Wallet Attestation. the Relying Party validates the presented Credentials checking the trust with their Issuers, and validates the Wallet Attestation by also checking that the Wallet Provider is trusted;
  9. the Wallet Instance informs the User about the successfull authentication with the Relying Party, the User continues the navigation.

Below a sequence diagram that summarizes the interactions between all the involved parties.

.. figure:: ../../images/cross_device_auth_seq_diagram.svg
    :align: center
    :target: https://www.plantuml.com/plantuml/uml/ZLLRRnit4ttdhpZmz_3PXkCcwPi05t5SDvUqjMefoKCI61Ht9B6co2qlgxX5_tjdIN6zAbIqW21WoRcSSsQ6yo94wMFQ625JT3Pj5kI549SgEe-Zzu7y4MH04cBXlfQ3_mTyJvrM58xmln_rQXrVcaIYvJXQwLRQYAEFqXYAU6Cvl5MKOsptJHA7UY9NP6F980NP1fnbt-oMp8EsAqpvy25RTYH4mfFls6M2ZxJ0Z7mF1rPsUYMZTbOasHjqDC4j_POeH4ozYwGYDNmINFAAernSe2U4onJNP3bdTiRnr5FWx_8rNSj09xYu4595tSb8FOAEQe8hJ_sPnEbfO1SwFKKdJQBFTk4ICueEZrIXdBlN1znzWNcNl8Ql03kgD7-vlN8DuUOMh-VpALDej6SsEFxswVCJR7LSVxRAQCvmfvkpSRGpP5Hd-5GFDnJNhkdllk3Ju7GNr9esz4KqDEOf7bblXLXvbrg6x4Bj0JXh7dPofmbcQxS5Yra1jyowBnRVRYUuQSdcsx-r1sJRdi4u9GtaNYt45iLrfgJbeEYZ3eVNNwDdU3baAxraPkG3bjvjybcr9zk8mOdwwZ2VWEXJY5cyR3r8SKWL8Ks4NewLtGa97H1e5sTwCviB0DZM-hRUTRgXK3cpasnab8YEi-uNdd6sJjkO8zGM6I4UQnT9MTqBfcGh5zheg2a8Ce7-0ynNrtCu3-iYsjBhOeIvUfTyGQyiDVKCRl4hgLWrFeo_2DvHhVl14E9GIVQc7JzLhQHjq3gZ5NCSl3wGryk775p6v0bkEGPS1_-cP1kyfD4Sa-ezMtwO7eUJOf0cWz_IUIXdipZ33AJ7PhvoTgdzXfhnn2HHHSoja5yMv_NlkPavT6ZxYFXiInswzYwwUxB_yBHSxtJfQHMwMYuCOUzzAW6gquZWg5akOwHGxCyvUVaS6qnBbte6faC_Ix6g-GFnSVRaEwx3mVdL8VUIfux1DESZDBjKLvwQVggbmPiG4ddC--7RXHmWl_qunwpMSnI5uIaAeOpf44e8pra9hYFFPhoCthnwFNzrUttzipZiCH6uMfEwnsjdc1RUqGDUQjjmosKWxCMq-JTr8R0xisQN9qY1BSepanP6AzopOtdUjStd8uBHeSkjMSesBHKw5mBpDTczHwlHGHaNg86CqUj5YXGcK1cYNe9L7cPCSmAKOV04sKbj-bxeHosh84PolMzh0vJzjgE2ux9zaF9zSuBHZFPxvPjdvy_m_EbJtBpZolnnvCkQoSDzDC4wnZOWULEQr--w-KwvXl3dU0os-rkaBewPtD3UtjZM_SOm2zDHnfxQlwsSZeRT-7OssHLtVuMK_OVZdc1zWWg1eiP94Q7Wk3pakj8TsUAIW_HymnaIsna3-jhcsZYFa5JVTCjaClON_9SsvYy0
    Remote Protocol Flow

The details of each step shown in the previous picture are described in the table below.


.. list-table::
  :widths: 10 50
  :header-rows: 1

  * - **Id**
    - **Description**
  * - **1**, **2**
    - The User requests to access to a protected resource, the Relying Party redirects the User to a discovery page in which the User selects the *Login with the Wallet* button. The Authorization flow starts.
  * - **3**, **4**,
    - The Relying Party provides the Wallet Instance with a URL where the information about the Relying Party are provided, along with the information about where the signed request is available for download.
  * - **5**, **6**, **7**, **8**, **9**
    - In the **Cross Device Flow**: the Request URI is provided in the form of a QR Code that is shown to the User. The User frames the QRCode with the Wallet Instance that extracts  ``client_id``, ``request_uri``, ``state``, ``client_id_scheme`` and ``request_uri_method``. In the **Same Device Flow** the Relying Party provides the same information of the Cross-Device flow but in the form of HTTP Redirect Location (302). 
  * - **10**, 
    - The Wallet Instance evaluates the trust with the Relying Party.
  * - **11**, **12**
    - The Wallet Instance checks if the Relying Party has provided the ``request_uri_method`` within its signed Request Object. If true, the Wallet provides its metadata in the to the Relying Party. The Relying Party returns a signed Request Object compliant to the Wallet technical capabilities.
  * - **13**
    - When the Wallet capabilities discovery is not supported by RP, the Wallet Instance request the signed Request Object using the HTTP method GET.
  * - **14**
    - The Wallet Instance obtains the signed Request Object.
  * - **15**, **16**, **17**
    - The Request Object JWS is verified by the Wallet Instance. The Wallet processes the Relying Party metadata and applies the policies related to the Relying Party, attesting whose Digital Credentials and User data the Relying Party is granted to request.
  * - **18**, **19**
    - The Wallet Instance requests the User's consent for the release of the Credentials. The User authorizes and consents the presentation of the Credentials by selecting/deselecting the personal data to release.
  * - **20**
    - The Wallet Instance provides the Authorization Response to the Relying Party using an HTTP request with the method POST (response mode "direct_post").
  * - **21**, **22**, **23**, **24**, **25** 
    - The Relying Party verifies the Authorization Response, extracts the Wallet Attestation to establish the trust with the Wallet Solution. The Relying Party extracts the Digital Credentials and attests the trust to the Credentials Issuer and the proof of possession of the Wallet Instance about the presented Digital Credentials. Finally, the Relying Party verifies the revocation status of the presented Digital Credentials.
  * - **26**
    - The Relying Party provides to the Wallet a redirect URI with a response code to be used by the Wallet to finalize the authentication.
  * - **27**, **28** and **29**
    - The User is informed by the Wallet Instance that the Autentication succeded, then the protected resource is made available to the User.


Request URI with HTTP POST
--------------------------

The Relying Party SHOULD provide the POST method with its ``request_uri`` endpoint
allowing the Wallet Instance to inform the Relying Party about its technical capabilities.

This feature can be useful when, for example, the Wallet Instance supports 
a restricted set of features, supported algorithms or a specific url for 
its ``authorization_endpoint``, and any other information that it deems necessary to 
provide to the Relying Party the parameters necessary for better interoperability.

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
      "presentation_definition_uri_supported": false,
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
  * - **request_uri_method**
    - OPTIONAL. The HTTP method MUST be set with ``get`` or ``post``. The Wallet Instance should use this method obtain the signed Request Object from the request_uri. If not provided, the Wallet Instance SHOULD use the HTTP method ``get``. If provided, the Wallet Instance SHOULD provide its metadata within the HTTP POST body encoded in ``application/json``.    
    
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


Request URI response
--------------------

The Relying Party issues the signed Request Object, where a non-normative example in the form of decoded header and payload is shown below:

.. code-block:: text

  {
    "alg": "ES256",
    "typ": "JWT",
    "kid": "e0bbf2f1-8c3a-4eab-a8ac-2e8f34db8a47",
    "trust_chain": [
      "MIICajCCAdOgAwIBAgIC...awz",
      "MIICajCCAdOgAwIBAgIC...2w3",
      "MIICajCCAdOgAwIBAgIC...sf2"
    ]
  }
  .
  {
    "scope": "eu.europa.ec.eudiw.pid.it.1 WalletTrustEvidence",
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
    - Sequence of Entity Statements that composes the Trust Chain related to the Relying Party, as defined in `OIDC-FED`_ Section *3.2.1. Trust Chain Header Parameter*.


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
    - String determining the HTTP method to be used with the `request_uri` endpoint to provide the Wallet metadata to the Relying Party. The value is case-insensitive and can be set to: `get` or `post`. The GET method, as defined in [@RFC9101], involves the Wallet sending a GET request to retrieve a Request Object. The POST method involves the Wallet requesting the creation of a new Request Object by sending an HTTP POST request, with its metadata, to the request URI of the Relying Party.

.. warning::

    Using the parameter ``scope`` requires that the Relying Party Metadata MUST contain the ``presentation_definition``, where a non-normative example of it is given below:

.. code-block:: JSON

  {
    "presentation_definition": {
      "id": "presentation definitions",
      "input_descriptors": [
        {
          "id": "eu.europa.ec.eudiw.pid.it.1",
          "name": "Person Identification Data",
          "purpose": "User authentication",
          "format": "vc+sd-jwt",
          "constraints": {
            "fields": [
              {
                "path": [
                  "$.credentialSubject.unique_id",
                  "$.credentialSubject.given_name",
                  "$.credentialSubject.family_name",
                ]
              }
            ],
            "limit_disclosure": "preferred"
          }
        },
        {
          "id": "WalletTrustEvidence",
          "name": "Wallet Trust Evidence",
          "purpose": "Wallet Authentication",
          "format": "jwt",
          "constraints": {
            "fields": [
              {
                "path": [
                  "$.iss",
                  "$.exp",
                  "$.iat",
                  "$.cnf.jwk",
                  "$.aal",
                ]
              }
            ]
          }
        }
      ]
    }
  }


.. note::

  The following parameters, even if defined in [OID4VP], are not mentioned in the previous non-normative example, since their usage is conditional and may change in future release of this documentation.

  - ``presentation_definition``: JSON object according to `Presentation Exchange <https://identity.foundation/presentation-exchange/spec/v2.0.0/>`_. This parameter MUST not be present when ``presentation_definition_uri`` or ``scope`` are present.
  - ``presentation_definition_uri``: Not supported. String containing an HTTPS URL pointing to a resource where a Presentation Definition JSON object can be retrieved. This parameter MUST be present when ``presentation_definition`` parameter or a ``scope`` value representing a Presentation Definition is not present. 
  - ``client_metadata``: A JSON object containing the Relying Party metadata values. The ``client_metadata`` parameter MUST NOT be present when ``client_id_scheme`` is ``entity_id``. Since the ``client_metadata`` is taken from ``trust_chain``, this parameter is intended to not be used.
  - ``client_metadata_uri``: string containing an HTTPS URL pointing to a resource where a JSON object with the Relying Party metadata can be retrieved. The ``client_metadata_uri`` parameter MUST NOT be present when ``client_id_scheme`` is ``entity_id``. Since the ``client_metadata`` is taken from ``trust_chain``, this parameter is intended to not be used.


Authorization Response Details
------------------------------

After getting the User authorization and consent for the presentation of the Credentials, the Wallet sends the Authorization Response to the Relying Party ``response_uri`` endpoint, the content SHOULD be encrypted according `OPENID4VP`_ Section 6.3, using the Relying Party public key.

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
                "id": "eu.europa.ec.eudiw.pid.it.1",
                "path": "$.vp_token.verified_claims.claims._sd[0]",
                "format": "vc+sd-jwt"
            },
            {
                "id": "WalletTrustEvidence",
                "path": "$",
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
      - The Requested Digital Credential (one or more, if in format SD-JWT VC or MDOC CBOR)
      - The Wallet Instance Attestation
  * - **presentation_submission**
    - JSON Object containing the mappings between the requested Verifiable Credentials and where to find them within the returned Verifiable Presentation Token, according to the `Presentation Exchange <https://identity.foundation/presentation-exchange/spec/v2.0.0/>`_.
  * - **state**
    - Unique identifier provided by the Relying Party within the Authorization Request.


Below is a non-normative example of the ``vp_token`` decoded content, represented in the form of JWS header and payload, separated by a period:

.. code-block:: text

   {
     "alg": "ES256",
     "typ": "JWT",
     "kid": "e0bbf2f1-8c3a-4eab-a8ac-2e8f34db8a47"
   }
   .
   {
     "iss": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
     "jti": "3978344f-8596-4c3a-a978-8fcaba3903c5",
     "aud": "https://relying-party.example.org/response_uri",
     "iat": 1541493724,
     "exp": 1573029723,
     "nonce": "2c128e4d-fc91-4cd3-86b8-18bdea0988cb"
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


Redirect URI
------------

When the Relying Party provides the redirect URI, the Wallet MUST send the user-agent to this redirect URI. The redirect URI allows the Relying Party to continue the interaction with the End-User on the device where the Wallet resides after the Wallet has sent the Authorization Response to the response URI.

The Relying Party MUST include a response code withing the redirect URI. The response code is a fresh, cryptographically random number used to ensure only the receiver of the redirect can fetch and process the Authorization Response. The number could be added as a path component, as a parameter or as a fragment to the URL. It is RECOMMENDED to use a cryptographic random value of 128 bits or more at the time of the writing of this specification.

The following is a non-normative example of the response from the Relying Party to the Wallet upon receiving the Authorization Response at the Response Endpoint.


.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8

  {
    "redirect_uri": "https://relying-party.example.org/cb#response_code=091535f699ea575c7937fa5f0f454aee"
  }

The ``redirect_uri`` value MUST be used with an HTTP method GET by either the Wallet or the user-agent to redirect the User to the Relying Party in order to complete the authentication process. The specific entity that performs this action depends on whether the flow is Same device or Cross device.


Relying Party Entity Configuration
-----------------------------------
According to the `Trust Model`_ section, the Relying Party is a Federation Entity and MUST expose a *well-known* endpoint containing its Entity Configuration. 

Below a non-normative example of the request made by the Wallet Instance to the *openid-federation* well-known endpoint to obtain the Relying Party Entity Configuration:

.. code-block:: http

  GET /.well-known/openid-federation HTTP/1.1
  HOST: relying-party.example.org


Below is a non-normative response example:

.. code-block:: text

    {
        "alg": "ES256",
        "kid": "2HnoFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs",
        "typ": "entity-statement+jwt"
    }
    .
    {
        "exp": 1649590602,
        "iat": 1649417862,
        "iss": "https://rp.example.it",
        "sub": "https://rp.example.it",
        "jwks": {
            "keys": [
                {
                    "kty": "EC",
                    "crv": "P-256",
                    "x": "5s4qi ...",
                    "y": "AQAB",
                    "kid": "2HnoFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs", 
                }
            ]
        },
        "metadata": {
            "wallet_relying_party": {
                "application_type": "web",
                "client_id": "https://rp.example.it",
                "client_name": "Name of an example organization",
                "jwks": {
                    "keys": [
                        {
                            "kty": "EC",
                            "crv": "P-256",
                            "x": "5s4qi ...",
                            "y": "AQAB",
                            "kid": "9tjiCaivhWLVUJ3AxwGGz_9", 
                        }
                    ]
                },
                
                "contacts": [
                    "ops@relying-party.example.org"
                ],
                
                "request_uris": [
                    "https://relying-party.example.org/request_uri"
                ],
                "response_uris": [
                    "https://relying-party.example.org/response_uri"
                ],
                "default_acr_values": [
                    "https://www.spid.gov.it/SpidL2",
                    "https://www.spid.gov.it/SpidL3"
                ],
                "vp_formats": {
                    "vc+sd-jwt": {
                        "sd-jwt_alg_values": [
                            "ES256",
                            "ES384"
                        ],
                        "kb-jwt_alg_values": [
                            "ES256",
                            "ES384"
                        ]
                    }
                },
                  "presentation_definitions": [
                      {
                        "id": "32f54163-7166-48f1-93d8-ff217bdb0653",
                        "input_descriptors": [
                            {
                                "id": "IdentityCredential",
                                "format": {
                                    "vc+sd-jwt": {}
                                },
                                "constraints": {
                                    "limit_disclosure": "required",
                                    "fields": [
                                        {
                                            "path": [
                                                "$.type"
                                            ],
                                            "filter": {
                                                "type": "string",
                                                "const": "IdentityCredential"
                                            }
                                        },
                                        {
                                            "path": [
                                                "$.family_name"
                                            ]
                                        },
                                        {
                                            "path": [
                                                "$.given_name"
                                            ]
                                        },
                                        {
                                            "path": [
                                                "$.unique_id"
                                            ],
                                            "intent_to_retain": "true"
                                        }
                                    ]
                                }
                            },
                        {
                            "id": "WalletTrustEvidence",
                            "format": {
                                "jwt": {}
                            },
                            "constraints": {
                                "fields": [
                                    {
                                        "path": [
                                            "$.iss"
                                        ],
                                        "filter": {
                                            "type": "string",
                                            "enum": [
                                                "https://issuer.example.org", 
                                                "https://issuer2.example.org", 
                                                "https://issuer3.example.org"
                                            ]
                                        }
                                    },
                                    {
                                        "path": [
                                            "$.iat"
                                        ],
                                        "filter": {
                                            "type": "number",
                                            "minimum": 1504699136
                                        }
                                    },
                                    {
                                        "path": [
                                            "$.exp"
                                        ],
                                        "filter": {
                                            "type": "number",
                                            "minimum": 1504700136
                                        }
                                    },
                                    {
                                        "path": [
                                            "$.cnf.jwk"
                                        ],
                                        "filter": {
                                            "type": "object"
                                        }
                                    }
                                ]
                            }
                        }
                        ]
                    },
                      {
                        "id": "mDL-sample-req",
                        "input_descriptors": [
                            {
                                "id": "mDL",
                                "format": {
                                    "mso_mdoc": {
                                        "alg": [
                                            "EdDSA",
                                            "ES256"
                                        ]
                                    },
                                    "constraints": {
                                        "limit_disclosure": "required",
                                        "fields": [
                                            {
                                                "path": [
                                                    "$.mdoc.doctype"
                                                ],
                                                "filter": {
                                                    "type": "string",
                                                    "const": "org.iso.18013.5.1.mDL"
                                                }
                                            },
                                            {
                                                "path": [
                                                    "$.mdoc.namespace"
                                                ],
                                                "filter": {
                                                    "type": "string",
                                                    "const": "org.iso.18013.5.1"
                                                }
                                            },
                                            {
                                                "path": [
                                                    "$.mdoc.family_name"
                                                ],
                                                "intent_to_retain": "false"
                                            },
                                            {
                                                "path": [
                                                    "$.mdoc.portrait"
                                                ],
                                                "intent_to_retain": "false"
                                            },
                                            {
                                                "path": [
                                                    "$.mdoc.driving_privileges"
                                                ],
                                                "intent_to_retain": "false"
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    }
                ],

                "default_max_age": 1111,
                
                // JARM related
                "authorization_signed_response_alg": [[
                    "ES256"
                ],
                "authorization_encrypted_response_alg": [
                    "RSA-OAEP",
                    "RSA-OAEP-256"
                ],
                "authorization_encrypted_response_enc": [
                    "A128CBC-HS256",
                    "A192CBC-HS384",
                    "A256CBC-HS512",
                    "A128GCM",
                    "A192GCM",
                    "A256GCM"
                ],

                // SIOPv2 related
                "subject_type": "pairwise",
                "require_auth_time": true,
                "id_token_signed_response_alg": [
                    "ES256"
                ],
                "id_token_encrypted_response_alg": [
                    "RSA-OAEP",
                    "RSA-OAEP-256"
                ],
                "id_token_encrypted_response_enc": [
                    "A128CBC-HS256",
                    "A192CBC-HS384",
                    "A256CBC-HS512",
                    "A128GCM",
                    "A192GCM",
                    "A256GCM"
                ],
            },
            "federation_entity": {
                "organization_name": "OpenID Wallet Relying Party example",
                "homepage_uri": "https://relying-party.example.org/home",
                "policy_uri": "https://relying-party.example.org/policy",
                "logo_uri": "https://relying-party.example.org/static/logo.svg",
                "contacts": [
                   "tech@relying-party.example.org"
                 ]
            }
        },
        "authority_hints": [
            "https://registry.eudi-wallet.example.it"
        ]
      }
    }
    

The Entity Configuration is a JWS, where its header and payload parameters are defined below, based on the provided OpenID Federation Entity Configuration example:

**JWT Header Parameters**

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **alg**
    - The digital signature algorithm used to sign the JWT. For example, "ES256" for ECDSA using P-256 and SHA-256.
  * - **typ**
    - The Media Type of the JWT, it MUST be set to "entity-statement+jwt".
  * - **kid**
    - The Key ID used for identifying the key used to sign the JWS.

**JWT Payload Parameters**

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **iss**
    - The issuer of the Entity Configuration, identifying the entity that issued the Entity Configuration.
  * - **sub**
    - The subject of the Entity Configuration, identifying the principal that is the subject of the Entity Configuration.
  * - **jwks**
    - JSON Web Key Set representing the cryptographic keys used for trust evaluation operations and for signing this Entity Configuration.
  * - **metadata**
    - Metadata describing the entity, including information about the wallet relying party, client ID, client name, contacts, request URIs, response URIs, default ACR values, and VP formats.
  * - **authority_hints**
    - URLs hinting at the authority or authorities that the entity trusts and which the public keys for verifieng this Entity Confgiuration are intended to be available within a Subordinate Statement.
  * - **exp**
    - Unix Timestamp representing the expiration time of the Entity Configuration, after which the Entity Configuration MUST NOT be accepted for processing.
  * - **iat**
    - Unix Timestamp representing the issued at time of the Entity Configuration, representing the time at which the Entity Configuration was issued.

