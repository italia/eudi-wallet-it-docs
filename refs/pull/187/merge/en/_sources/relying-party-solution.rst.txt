.. include:: ../common/common_definitions.rst

.. _Wallet Attestation: wallet-attestation.html
.. _Trust Model: trust.html

.. _relying-party-solution:

Relying Party Solution
+++++++++++++++++++++++

This section describes how a Relying Party requests to a Wallet Instance the presentation of the PID/EAAs 
according to `OpenID for Verifiable Presentations - draft 20 <https://openid.net/specs/openid-4-verifiable-presentations-1_0.html>`_.

In this section the following flows are described:

- **Remote Same Device Flow**, where the user-agent and the Wallet Instance are used in the same device.
- **Remote Cross Device Flow**, where the user-agent and the Wallet Instance are used in different devices.
- **Proximity Flow**, where the User presents a Credential to a Verifier App according to ISO 18013-5. The User interacts with a Verifier using proximity connection technologies such as QR Code and Bluetooth Low Energy (BLE).

In the **Same Device** and **Cross Device** Flows described in this chapter, the User interacts with a remote Relying Party.

High Level Design
--------------------

From the User's perspective:

1. the Wallet Instance scans the QR Code and obtains the URL (Cross Device flow) or obtain directly an URL (Same Device flow);
2. the Wallet Instance extracts from the payload the ``client_id`` and the `request_uri` parameters;
3. the Wallet Instance establishes the Trust to the Relying Party by building the Federation Trust Chain. Implementations may evaluate the trust after having obtained the signed Request Object (see point 5);
4. the Wallet fetches the signed Request Object using an HTTP request with method GET to the endpoint provided in the ``request_uri`` parameter;
5. the Wallet verifies the signature of the signed Request Object and that its issuer matches the ``client_id`` obtained at the step number 2.
6. the Wallet checks the presence in the signed Request Object of the parameter `request_uri_method`, if this parameter is present and set with the ``post`` valueThe Wallet transmits its metadata to the request_uri endpoint of the Relying Party using an HTTP POST method and obtains an updated signed Request Object;
5. The Wallet Instance evaluates the requested PID/EAAs and checks the elegibility of the Relying Party in asking these by applying the policies related to that specific Relying Party;
6. the Wallet Instance asks User disclosure and consent;
7. the Wallet Instance presents the requested disclosure of P to the Relying Party;
8. the Wallet Instance informs the User about the successfull authentication with the Relying Party and give a good user experience to let the User continuing its navigation.


Remote Protocol Flow
====================

In this scenario the Relying Party MUST provide the URL where the signed presentation Request Object is available for download.

Depending on whether the User is using a mobile device or a workstation, the Relying Party MUST support the following remote flows:

* **Same Device**, the Relying Party MUST provide a HTTP redirect (302) location to the Wallet Instance;
* **Cross Device**, the Relying Party MUST provide a QR Code which the User frames with the Wallet Instance.

Once the Wallet Instance establishes the trust with the Relying Party and evaluates the request, the User gives the consent for the disclosure of the Digital Credentials, in the form of a Verifiable Presentation.

Below a sequence diagram that summarizes the interactions between all the involved parties.

.. image:: ../../images/cross_device_auth_seq_diagram.svg
  :align: center
  :target: https://www.plantuml.com/plantuml/svg/XLLTRo8t5xxthpZYlNWXIjBizWufrMRJT9FTjao1tTmW8UCvW1jZJ_qnX5RzxpssPuQX8ceK8OrzFfxdEH_-u3otFkmKuy4R7NOhj8onE-6DXS5NXtO0t45WR6LUyy7_7Vo8jHJe1l2_d-Lcwp-gWAoYE5B8YciFWsUk57fuqXHU2qmnzgScWK9TyGrgdpDmXhe4od9gDaLra7e31HqUacMDZ0Mu-e5Snl2CAvYXZN10yrfkk9T6iy2ZGOrZcE8V0Ps7mXgFmcD99yu4AoZAxIr4Gd0N_1OrvKpEC2miElhENyMMEnp1xItZmikQUum8QcmJt5kCPnmkBXovuCK5r9m4MUYL2SJ86pXI1M7CYppZRZFCPR0IR0kmnfRcRzDxKo9Cfl0udnT4ePIMsC3m-vlt8zXBlmMX92LOolAo7-mI4YXMOXyzEtBPCxQn9bG4nBYsic2qEZGYXZ7CjcOF954Beo8kiGHqkn_3f4ATRlzLTE1LTGdA2Aw0doZCzf1TPu9h2WenQdVuyEejmLleZj52znWjDDTbPhNGQsjsCNSNX7g8TP4m5eBi77WRdCywHUikCfasTMWok7Jlv4PZsPw1MVqUnUwIzOj52IiZjK_5ocdFUfFaoeDSzvsNE_HRKu9quB21LqncSyQ0_ZfebJMrBD6r0fCNBxdduCtRS6A4hikEIlGBvL5e6QiZUCLNKaalqNMEcKkeA1EMRt1wI-wJeOLVMhonS9LHKb2UpkiRMha-f0JS1ujWrhqQTFCxoHaxBwvaHDRUa-MtOkX6sI0SvtvjB0YZupmVcpuSk_VUwBMqEopx8nAEVH7haHQ4iVBFrBqKsbKn8YnqhbbTBRrvGVt6XdXeT8cqCbt9LmhXPCta09rJH_3iPDrvKZaxNXEA_DctB7BBM48e7SI5sihw4z9nygGxAiZP-EIZZGUBDQ4ghtkmcbIqjSeuprp1atC1BSpZXEMGH-oVd-SmQmlRYqBm13gNPx4BnPYbh0YcHajczBWyVNgSVve-FFpApdkC6TnlKRp0er542xxW0JvANLBl9I3aHRJflp3EaJkn9fSh28uiKgmghAWVuOKSyxgMKHUwwLFq1khSfQc2HIxMDMCmtw9k5rQwBAKJoZWiWNjlvIgGN6CgKOEJvf-axgPMKWx8es4HUCsbYfqHnof9mNgQVQtQTiYFLiC7Xlb9QITr1BrD51-BxzvTluFtDpSm-K8m_XhO_7QaTJ4OmzRxoa6mAhUoRNfxAUAY_xi_5FlJHwHzDsPyX_rdevb0JeXTXjlF6AdzrujJO_VWVPwD6-LENv2y_s4O2RPBAHF8Qeoo21d7tJdNZQon6TyK9F9rbn38ZWg4hrMgZR7WWeYTjmugOVz0Fs6d_W40

The details of each step shown in the previous picture are described in the table below.


.. list-table::
  :widths: 50 50
  :header-rows: 1

  * - **Id**
    - **Description**
  * - **1**, **2**
    - The User requests to access to a protected resource, the Relying Party redirects the User to a discovery page in which the User selects the *Login with the Wallet* button. The Authorization flow starts.
  * - **3**, **4**,
    - The Relying Party provides the Wallet Instance with a URL where a generic signed Request Object can be downloaded.
  * - **5**, **6**, **7**, **8**, **9**
    - In the **Cross Device Flow**: the Request URI is provided in the form of a QR Code that is shown to the User. The User frames the QRCode with the Wallet Instance and extracts  ``client_id``, ``request_uri`` and ``state``. In the **Same Device Flow** the Relying Party provides the same information of the Cross-Device flow but in the form of HTTP Redirect Location (302). 
  * - **10**, **11**, **12**
    - The Wallet Instance obtains the signed Request Object.
  * - **13**, **14** and **15**
    - The Wallet Instance checks if the Relying Party has provided the ``request_uri_method`` within its signed Request Object. If true, the Wallet provides its metadata in the to the Relying Party. The Relying PArty produces a new signed Request Object compliant to the Wallet technical capabilities.
  * - **13**, **14**, **15**, **16**, **17**, **18**
    - The Request Object JWS is verified by the Wallet Instance. The Wallet processes the Relying Party metadata and applies the policies related to the Relying Party, attesting whose Digital Credentials and User data the Relying Party is granted to request.
  * - **19**, **20**
    - The Wallet Instance requests the User's consent for the release of the Credentials. The User authorizes and consents the presentation of the Credentials by selecting/deselecting the personal data to release.
  * - **21**
    - The Wallet Instance provides the Authorization Response to the Relying Party using an HTTP request with the method POST (response mode "direct_post").
  * - **22**, **23**, **24**, **25** and **26**
    - The Relying Party verifies the Authorization Response, extracts the Wallet Attestation to establish the trust with the Wallet Solution. The Relying Party extracts the Digital Credentials and attests the trust to the Credentials Issuer and the proof of possession of the Wallet Instance about the presented Digital Credentials. Finally, the Relying Party verifies the revocation status of the presented Digital Credentials.
  * - **27** and **28**
    - The Relying Party provides to the Wallet a redirect URI with a response code to be used by the Wallet to finalize the authentication.
  * - **29**
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
supports the ``request_uri_method`` with HTTP POST,
the Wallet Instance capabilities MUST 
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
it MUST provide it to the Wallet Instance through an HTTP URL (request URI). 
The HTTP URL points to the web resource where the signed request object is 
available for download. The URL parameters contained in the Relying Party 
response, containing the request URI, are described in the Table below.

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **client_id**
    - Unique identifier of the Relying Party.
  * - **request_uri**
    - The HTTPs URL where the Relying Party provides the signed Request Object to the Wallet Instance. 
    
    
.. This is under discussion: The URL is intentionally extended with a random URI fragment value, that uniquely identifies the transaction. Eg: `https://relying-party.example.org/request_uri#that-random-fragment-we-mentioned`. It is RECOMMENDED that the length of the random fragment value is longer than 12 characters.

Below a non-normative example of the response containing the required parameters previously described.

.. code-block:: javascript

  https://wallet-solution.digital-strategy.europa.eu/authorization?client_id=...&request_uri=...

The value corresponding to the `request_uri` endpoint SHOULD be randomized, according to `RFC 9101, The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR) <https://www.rfc-editor.org/rfc/rfc9101.html#section-5.2.1>`_ Section 5.2.1.


In the **Same Device Flow** the Relying Party uses an HTTP response redirect (with status code set to 302) as represented in the following non-normative example:

.. code:: text

    HTTP/1.1 /authorization Found
    Location: https://wallet-solution.digital-strategy.europa.eu?
    client_id=https%3A%2F%2Frelying-party.example.org%2Fcb
    &request_uri=https%3A%2F%2Frelying-party.example.org%2Frequest_uri


In the **Cross Device Flow**, a QR Code is shown by the Relying Party to the User in order to provide the Authorization Request. The User frames the QR Code using their Wallet Instance.

Below is represented a non-normative example of a QR Code issued by the Relying Party.

.. image:: ../../images/verifier_qr_code.svg
  :align: center


Below is represented a non-normative example of the QR Code raw payload:

.. code-block:: text

  https://wallet-solution.digital-strategy.europa.eu/authorization?client_id=https%3A%2F%2Frelying-party.example.org&request_uri=https%3A%2F%2Frelying-party.example.org

.. note::
    The *error correction level* chosen for the QR Code MUST be Q (Quartily - up to 25%), since it offers a good balance between error correction capability and data density/space. This level of quality and error correction allows the QR Code to remain readable even if it is damaged or partially obscured.


Cross Device Flow Status Checks and Security
--------------------------------------------

When the flow is Cross Device, the user-agent needs to check the session status to the endpoint made available by Relying Party (status endpoint). This check MAY be implemented in the form of JavaScript code, within the page that shows the QRCode, then the user-agent checks the status with a polling strategy in seconds or a push strategy (eg: web socket).

Since the QRcode page and the status endpoint are implemented by the Relying Party, it is under its responsability the implementation details of this solution, since it is related to the Relying Party's internal API.

The Relying Party MUST bind the request of the user-agent, with a Secure and HttpOnly session cookie, with the issued request. The request url SHOULD include a parameter with a random value. The HTTP response returned by this specialized endpoint MAY contain the HTTP status codes listed below:

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
    "scope": "eu.europa.ec.eudiw.pid.it.1 tax_id_number",
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
    - Aliases for well-defined Presentation Definitions IDs. It is used to identify which required credentials and User attributes are requested by the Relying Party, according to the Section "Using scope Parameter to Request Verifiable Credential(s)" of [OID4VP].
  * - **client_id_scheme**
    - String identifying the scheme of the value in the ``client_id``. It MUST be set to the value ``entity_id``.
  * - **client_id**
    - Unique Identifier of the Relying Party.
  * - **response_mode**
    - It MUST be set to ``direct_post.jwt``.
  * - **response_type**
    - It MUST be set to``vp_token``.
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
            "limit_discolusre": "preferred"
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

.. code-block:: JSON

  {
    "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
    "vp_token": [
        "eyJhbGciOiJFUzI1NiIs...PT0iXX0",
        $WalletInstanceAttestation-JWT
    ],
    "presentation_submission": {
        "definition_id": "32f54163-7166-48f1-93d8-ff217bdb0653",
        "id": "04a98be3-7fb0-4cf5-af9a-31579c8b0e7d",
        "descriptor_map": [
            {
                "id": "eu.europa.ec.eudiw.pid.it.1",
                "path": "$.vp_token.verified_claims.claims._sd[0]",
                "format": "vc+sd-jwt"
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
    - JSON Object containing the mappings between the requested Verifiable Credentials and where to find them within the returned Verifiable Presentation Token.
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
    - The Digital Credential in its original state. The public key contained in the Digital Credential MUST be used to verify the entire VP JWS as Proof of Possession of the private key which the public key is included in the Digital Credential. Eg: for SD-JWT VC the pblic key is provided within the ``cnf.jwk`` claim.
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

The following is a non-normative example of the response from the Relying Party  to the Wallet upon receiving the Authorization Response at the Response Endpoint.


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
        "alg": "RS256",
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
                    "kty": "RSA",
                    "n": "5s4qi ...",
                    "e": "AQAB",
                    "kid": "2HnoFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs"
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
                            "kty": "RSA",
                            "use": "sig",
                            "n": "1Ta-sE ...",
                            "e": "AQAB",
                            "kid": "YhNFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs",
                            "x5c": [ "..." ]
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
                        "id": "eu.europa.ec.eudiw.pid.it.1",
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
    

The Entity Configuration is a JWS, where its header parameters are defined below: 

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **alg**
    - Algorithm used to sign the JWT
  * - **typ**
    - Media Type of the JWT
  * - **kid**
    - Key ID used identifying the key used to sign the JWS


.. note:
    The Relying Party specific metadata parameter are experimental 
    and still under discussion `here <https://github.com/openid/OpenID4VP/issues/17>`_.


Proximity Flow
==============

This section describes how a Verifier requests the presentation of an *mDoc-CBOR* Credential to a Wallet Instance according to the *ISO 18013-5 Specification*. Only *Supervised Device Retrieval flow* is supported in this technical implementation profile. 

The presentation phase is divided into three sub-phases: 
 
  1. **Device Engagement**: This subphase begins when the User is prompted to disclose certain attributes from the mDoc(s). The objective of this subphase is to establish a secure communication channel between the Wallet Instance and the Verifier App, so that the mDoc requests and responses can be exchanged during the communication subphase.
  The messages exchanged in this subphase are transmitted through short-range technologies to limit the possibility of interception and eavesdropping.
  This technical implementation profile exclusively supports QR code for Device Engagement.

  2. **Session establishment**: During the session establishment phase, the Verifier App sets up a secure connection. All data transmitted over this connection is encrypted using a session key, which is known to both the Wallet Instance and the Verifier at this stage.
  The established session MAY be terminated based on the conditions as detailed in [ISO18013-5#9.1.1.4].

  3. **Communication - Device Retrieval**: The Verifier App encrypts the mDoc request with the appropriate session key and sends it to the Wallet Instance together with its public key in a session establishment message. The mDoc uses the data from the session establishment message to derive the session key and decrypt the mDoc request.
  During the communication subphase, the Verifier App has the option to request information from the Wallet using mDoc requests and responses. The primary mode of communication is the secure channel established during the session setup. The Wallet Instance encrypts the mDoc response using the session key and transmits it to the Verifier App via a session data message. This technical implementation profile only supports Bluetooth Low Energy (BLE) for the communication sub-phase.


The following figure illustrates the flow diagram compliant with ISO 18013-5 for proximity flow.

.. _fig_High-Level-Flow-ITWallet-Presentation-ISO:
.. figure:: ../../images/High-Level-Flow-ITWallet-Presentation-ISO.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/bL9BZnCn3BxFhx3A0H3q3_ImMlOXXBJYqGguzE9ct2RQn0bvJDb_ZoSP3QFI2xab_Xx-xDocZ34NPpiisNDn1ufT1t9GPH_XUw88cA3KjuF_3QlnwNM2dHDYq9vf1Q-Up4ddErkeme9KZ381ESFg9rfB6JwnEB4IiAYTAuou7nN_Al-WQ8xcVzHd2dm8eKeFI-cMfApNDpVd3Nm9n90rmKLBa3s4I8b441dSWrTm7wcNkq7RD3xxJE07CIhlXmqyq624-CWdF94RYQaSWiP4iAweRzjr1vLvRkOVYIcYY32TWO8c9rSBp_GYWKoSe88LzPtsvx5HKO5xtnCSVVpNibA6ATjE8IyfKr7aBgptVDry0WlPXIBOH2aPpoEcbgzDOJTXIEPui2PfrqROZogki56OfNuvcxkdHv5N9H8eZSnaPLRJwUPU95JTn9P-5J60Tn2AcAZQjJ_MiCljxndUN6texN8Dr-ErSjd0roZrNEUjFDSVaJqaZP6gOMpDK0-61UHglkcJjJL75Cx4NHflAKT30xLGH_41wnLQIDb7FD6C7URSAOZCSfCjxyjSWcHEZBb4slCuTQL9FJVsWDRq9akuxfQuByx-0G00

    High-Level Proximity Flow

**Step 1-3**: The Verifier requests the User to reveal certain attributes from their mDoc(s) stored in the Wallet Instance. The User initiates the Wallet Instance. The Wallet Instance MUST create a new temporary key pair (EDeviceKey.Priv, EDeviceKey.Pub), and incorporate the cipher suite identifier, the identifier of the elliptic curve for key agreement, and the EDeviceKey public point into the device engagement structure (refer to [ISO18013-5#9.1.1.4]). This key pair is temporary and MUST be invalidated immediately after the secure channel is established. Finally, the Wallet Instance displays the QR Code for Device Engagement.

Below an example of a device engagement structure that utilizes QR for device engagement and Bluetooth Low Energy (BLE) for data retrieval.

CBOR data:

.. code-block:: 

  a30063312e30018201d818584ba4010220012158205a88d182bce5f42efa59943f33359d2e8a968ff289d93e5fa444b624343167fe225820b16e8cf858ddc7690407ba61d4c338237a8cfcf3de6aa672fc60a557aa32fc670281830201a300f401f50b5045efef742b2c4837a9a3b0e1d05a6917 

In diagnostic notation:

.. code-block:: 

  { 
    0: "1.0", % Version

    1:        % Security
    [ 
        1,     % defines the cipher suite 1 which contains only EC curves
        24(<<  % embedded CBOR data item
          { 
            1: 2, % kty:EC2 (Elliptic curves with x and y coordinate pairs)
          -1: 1, % crv:p256
  -2:h'5A88D182BCE5F42EFA59943F33359D2E8A968FF289D93E5FA444B624343  167FE',% x-coordinate
  -3:h'B16E8CF858DDC7690407BA61D4C338237A8CFCF3DE6AA672FC60A557AA32FC67' % y-coordinate
          }
        >>)
      ],
  
      2: %DeviceRetrievalMethods(Device engagement using QR code)
      [ 
        [
          2, %BLE
          1, % Version
        {    %BLE options
            0: false, % no support for mdoc peripheral server mode
            1: true, % support mdoc central client mode
            11: h'45EFEF742B2C4837A9A3B0E1D05A6917' % UUID of mdoc client central mode
          }
        ]
      ]
  }



**Step 4-6**: The Verifier App scans the QR Code and generates its own ephemeral key pair (EReaderKey.Priv, EReaderKey.Pub). It then calculates the session key, using the public key received in the Engagement Structure and its newly-generated private key, as outlined in [ISO18013-5#9.1.1.5]. Finally, it generates its session key, which must be independently derived by both the Wallet Instance and the Verifier App.

**Step 7**: The Verifier App creates an mDoc request that MUST be encrypted using the relevant session key, and transmits it to the Wallet Instance along with EReaderKey.Pub within a session establishment message. The mDoc request MUST be encoded in CBOR, as demonstrated in the following non-normative example.

CBOR data: 
.. code-block::

  a26776657273696f6e63312e306b646f63526571756573747381a26c6974656d7352657175657374d818590152a267646f6354797065756f72672e69736f2e31383031332e352e312e6d444c6a6e616d65537061636573a2746f72672e69736f2e31383031332e352e312e4954a375766572696669636174696f6e2e65766964656e6365f4781c766572696669636174696f6e2e6173737572616e63655f6c6576656cf4781c766572696669636174696f6e2e74727573745f6672616d65776f726bf4716f72672e69736f2e31383031332e352e31ab76756e5f64697374696e6775697368696e675f7369676ef47264726976696e675f70726976696c65676573f46f646f63756d656e745f6e756d626572f46a69737375655f64617465f46f69737375696e675f636f756e747279f47169737375696e675f617574686f72697479f46a62697274685f64617465f46b6578706972795f64617465f46a676976656e5f6e616d65f468706f727472616974f46b66616d696c795f6e616d65f46a726561646572417574688443a10126a11821590129308201253081cda00302010202012a300a06082a8648ce3d0403023020311e301c06035504030c15536f6d652052656164657220417574686f72697479301e170d3233313132343130323832325a170d3238313132323130323832325a301a3118301606035504030c0f536f6d6520526561646572204b65793059301306072a8648ce3d020106082a8648ce3d03010703420004aa1092fb59e26ddd182cfdbc85f1aa8217a4f0fae6a6a5536b57c5ef7be2fb6d0dfd319839e6c24d087cd26499ec4f87c8c766200ba4c6218c74de50cd1243b1300a06082a8648ce3d0403020347003044022048466e92226e042add073b8cdc43df5a19401e1d95ab226e142947e435af9db30220043af7a8e7d31646a424e02ea0c853ec9c293791f930bf589bee557370a4c97bf6584058a0d421a7e53b7db0412a196fea50ca6d4c8a530a47dd84d88588ab145374bd0ab2a724cf2ed2facf32c7184591c5969efd53f5aba63194105440bc1904e1b9

The above CBOR data is represented in diagnostic notation as follows:
.. code-block::

  {
    "version": "1.0",
    "docRequests": [
    {
      "itemsRequest": 24(<< {
        "docType": "org.iso.18013.5.1.mDL",
        "nameSpaces": {
          "org.iso.18013.5.1.IT": {
            "verification.evidence": false,
            "verification.assurance_level": false,
            "verification.trust_framework": false
          },
          "org.iso.18013.5.1": {
            "un_distinguishing_sign": false,
            "driving_privileges": false,
            "document_number": false,
            "issue_date": false,
            "issuing_country": false,
            "issuing_authority": false,
            "birth_date": false,
            "expiry_date": false,
            "given_name": false,
            "portrait": false,
            "family_name": false
          }
        }
      } >>),
      "readerAuth": [
        h'a10126',
        {
          33: h'308201253081cda00302010202012a300a06082a8648ce3d0403023020311e301c06035504030c15536f6d652052656164657220417574686f72697479301e170d3233313132343130323832325a170d3238313132323130323832325a301a3118301606035504030c0f536f6d6520526561646572204b65793059301306072a8648ce3d020106082a8648ce3d03010703420004aa1092fb59e26ddd182cfdbc85f1aa8217a4f0fae6a6a5536b57c5ef7be2fb6d0dfd319839e6c24d087cd26499ec4f87c8c766200ba4c6218c74de50cd1243b1300a06082a8648ce3d0403020347003044022048466e92226e042add073b8cdc43df5a19401e1d95ab226e142947e435af9db30220043af7a8e7d31646a424e02ea0c853ec9c293791f930bf589bee557370a4c97b'
        },
        null,
        h'58a0d421a7e53b7db0412a196fea50ca6d4c8a530a47dd84d88588ab145374bd0ab2a724cf2ed2facf32c7184591c5969efd53f5aba63194105440bc1904e1b9'
      ]
    }
    ]
  }

**Step 8**: The Wallet Instance uses the session establishment message to derive the session keys and decrypt the mDoc request. It computes the session key using the public key received from the Verifier App and its private key.

**Step 9-10**: When the Wallet Instance receives the mDoc request, it locates the documents that contain the requested attributes and asks the User for permission to provide this information to the Verifier. If the User agrees, the Wallet generates an mDoc response and transmits it to the Verifier App through the secure channel.

**Step 11-12**: If the User gives consent, the Wallet Instance creates an mDoc response and transmits it to the Verifier App via the secure channel. The mDoc response MUST be encoded in CBOR, with its structure outlined in [ISO18013-5#8.3.2.1.2.2]. Below is a non-normative example of an mDoc response.

CBOR Data:
.. code-block::

  a36776657273696f6e63312e3069646f63756d656e747381a367646f6354797065756f72672e69736f2e31383031332e352e312e6d444c6c6973737565725369676e6564a26a6e616d65537061636573a2746f72672e69736f2e31383031332e352e312e495483d81858f7a46864696765737449440b6672616e646f6d506d44f21ee875f2c1d502b43198e5a15271656c656d656e744964656e74696669657275766572696669636174696f6e2e65766964656e63656c656c656d656e7456616c756581a2647479706571656c656374726f6e69635f7265636f7264667265636f7264bf6474797065781f68747470733a2f2f657564692e77616c6c65742e70646e642e676f762e697466736f75726365bf716f7267616e697a6174696f6e5f6e616d65754d6f746f72697a7a617a696f6e6520436976696c656f6f7267616e697a6174696f6e5f6964656d5f696e666c636f756e7472795f636f6465626974ffffd8185866a4686469676573744944046672616e646f6d50185d84dfb71ce9b173010ddd62174fbe71656c656d656e744964656e746966696572781c766572696669636174696f6e2e74727573745f6672616d65776f726b6c656c656d656e7456616c7565656569646173d8185865a4686469676573744944006672616e646f6d50137f903174253c4585358267aae2ea4e71656c656d656e744964656e746966696572781c766572696669636174696f6e2e6173737572616e63655f6c6576656c6c656c656d656e7456616c75656468696768716f72672e69736f2e31383031332e352e318bd8185852a46864696765737449440c6672616e646f6d5053e29d0ddbbc7d2306a32bdbe2e56e5171656c656d656e744964656e7469666965726b66616d696c795f6e616d656c656c656d656e7456616c756563446f65d8185855a4686469676573744944036672616e646f6d50990cba2069fa1b33b8d6ae910b6549dc71656c656d656e744964656e7469666965726a676976656e5f6e616d656c656c656d656e7456616c756567416e746f6e696fd818585ba46864696765737449440a6672616e646f6d504086c1379975f805f1b1f4975e6a126571656c656d656e744964656e7469666965726a69737375655f646174656c656c656d656e7456616c7565d903ec6a323031392d31302d3230d818585ca4686469676573744944016672616e646f6d50ab4ca30c918dd2fd0bf35242c15fa2d871656c656d656e744964656e7469666965726b6578706972795f646174656c656c656d656e7456616c7565d903ec6a323032342d31302d3230d8185855a4686469676573744944076672616e646f6d508d9066f6c8da16619867cd4e2fab0c8871656c656d656e744964656e7469666965726f69737375696e675f636f756e7472796c656c656d656e7456616c7565624954d818587ea4686469676573744944056672616e646f6d5059fe68db795dee4c20976380ea24770571656c656d656e744964656e7469666965727169737375696e675f617574686f726974796c656c656d656e7456616c75657828497374697475746f20506f6c696772616669636f2065205a656363612064656c6c6f20537461746fd818585ba4686469676573744944026672616e646f6d5008b3f1ca5517019767be3dee3bb0614571656c656d656e744964656e7469666965726a62697274685f646174656c656c656d656e7456616c7565d903ec6a313935362d30312d3230d818585ca4686469676573744944096672616e646f6d50a2395ec214350c26066306e23279b3ae71656c656d656e744964656e7469666965726f646f63756d656e745f6e756d6265726c656c656d656e7456616c756569393837363534333231d8185850a4686469676573744944066672616e646f6d50a25e1a5b915d2d6eafee9674e023293971656c656d656e744964656e74696669657268706f7274726169746c656c656d656e7456616c75654420212223d81858eea46864696765737449440d6672616e646f6d50eeed6a3b856563627589a360939d12f771656c656d656e744964656e7469666965727264726976696e675f70726976696c656765736c656c656d656e7456616c756582a37576656869636c655f63617465676f72795f636f646561416a69737375655f64617465d903ec6a323031382d30382d30396b6578706972795f64617465d903ec6a323032342d31302d3230a37576656869636c655f63617465676f72795f636f646561426a69737375655f64617465d903ec6a323031372d30322d32336b6578706972795f64617465d903ec6a323032342d31302d3230d818585ba4686469676573744944086672616e646f6d50c0ef486b2a194ed3cbf7f354fd40092171656c656d656e744964656e74696669657276756e5f64697374696e6775697368696e675f7369676e6c656c656d656e7456616c756561496a697373756572417574688443a10126a118215901423082013e3081e5a00302010202012a300a06082a8648ce3d040302301a3118301606035504030c0f5374617465204f662055746f706961301e170d3233313132343134353430345a170d3238313132323134353430345a30383136303406035504030c2d5374617465204f662055746f7069612049737375696e6720417574686f72697479205369676e696e67204b65793059301306072a8648ce3d020106082a8648ce3d03010703420004c338ec1000b351ce8bcdfc167450aeceb

In diagnostic notation:
.. code-block::

  {
    "version": "1.0",
    "documents": [
    {
      "docType": "org.iso.18013.5.1.mDL",
      "issuerSigned": {
        "nameSpaces": {
          "org.iso.18013.5.1.IT": [
            24(<< {
              "digestID": 11,
              "random": h'6d44f21ee875f2c1d502b43198e5a152',
              "elementIdentifier": "verification.evidence",
              "elementValue": [
                {
                  "type": "electronic_record",
                  "record": {
                    "type": "https://eudi.wallet.pdnd.gov.it",
                    "source": {
                      "organization_name": "Motorizzazione Civile",
                      "organization_id": "m_inf",
                      "country_code": "it"
                    }
                  }
                }
              ]
            } >>),
            24(<< {
              "digestID": 4,
              "random": h'185d84dfb71ce9b173010ddd62174fbe',
              "elementIdentifier": "verification.trust_framework",
              "elementValue": "eidas"
            } >>),
            24(<< {
              "digestID": 0,
              "random": h'137f903174253c4585358267aae2ea4e',
              "elementIdentifier": "verification.assurance_level",
              "elementValue": "high"
            } >>)
          ],
          "org.iso.18013.5.1": [
            24(<< {
              "digestID": 12,
              "random": h'53e29d0ddbbc7d2306a32bdbe2e56e51',
              "elementIdentifier": "family_name",
              "elementValue": "Doe"
            } >>),
            24(<< {
              "digestID": 3,
              "random": h'990cba2069fa1b33b8d6ae910b6549dc',
              "elementIdentifier": "given_name",
              "elementValue": "Antonio"
            } >>),
            24(<< {
              "digestID": 10,
              "random": h'4086c1379975f805f1b1f4975e6a1265',
              "elementIdentifier": "issue_date",
              "elementValue": 1004("2019-10-20")
            } >>),
            24(<< {
              "digestID": 1,
              "random": h'ab4ca30c918dd2fd0bf35242c15fa2d8',
              "elementIdentifier": "expiry_date",
              "elementValue": 1004("2024-10-20")
            } >>),
            24(<< {
              "digestID": 7,
              "random": h'8d9066f6c8da16619867cd4e2fab0c88',
              "elementIdentifier": "issuing_country",
              "elementValue": "IT"
            } >>),
            24(<< {
              "digestID": 5,
              "random": h'59fe68db795dee4c20976380ea247705',
              "elementIdentifier": "issuing_authority",
              "elementValue": "Istituto Poligrafico e Zecca dello Stato"
            } >>),
            24(<< {
              "digestID": 2,
              "random": h'08b3f1ca5517019767be3dee3bb06145',
              "elementIdentifier": "birth_date",
              "elementValue": 1004("1956-01-20")
            } >>),
            24(<< {
              "digestID": 9,
              "random": h'a2395ec214350c26066306e23279b3ae',
              "elementIdentifier": "document_number",
              "elementValue": "987654321"
            } >>),
            24(<< {
              "digestID": 6,
              "random": h'a25e1a5b915d2d6eafee9674e0232939',
              "elementIdentifier": "portrait",
              "elementValue": h'20212223'
            } >>),
            24(<< {
              "digestID": 13,
              "random": h'eeed6a3b856563627589a360939d12f7',
              "elementIdentifier": "driving_privileges",
              "elementValue": [
                {
                  "vehicle_category_code": "A",
                  "issue_date": 1004("2018-08-09"),
                  "expiry_date": 1004("2024-10-20")
                },
                {
                  "vehicle_category_code": "B",
                  "issue_date": 1004("2017-02-23"),
                  "expiry_date": 1004("2024-10-20")
                }
              ]
            } >>),
            24(<< {
              "digestID": 8,
              "random": h'c0ef486b2a194ed3cbf7f354fd400921',
              "elementIdentifier": "un_distinguishing_sign",
              "elementValue": "I"
            } >>)
          ]
        },
        "issuerAuth": [
          h'a10126',
          {
            33: h'3082013e3081e5a00302010202012a300a06082a8648ce3d040302301a3118301606035504030c0f5374617465204f662055746f706961301e170d3233313132343134353430345a170d3238313132323134353430345a30383136303406035504030c2d5374617465204f662055746f7069612049737375696e6720417574686f72697479205369676e696e67204b65793059301306072a8648ce3d020106082a8648ce3d03010703420004c338ec1000b351ce8bcdfc167450aeceb7d518bd9a519583e082d67effff06565804fc09abf0e4a08e699c9dba3796285a15f68e40ac7f9fc7700a15153a4065300a06082a8648ce3d040302034800304502210099b7d62e6bf7b1823db3713df889bf73e70bb4d9c58c21e92c58d2f1beffe932022058d039747a00d70e6d66be4797e6142b3608a014ee09b7b79af2cae2aaf27788'
          },
          24(<< {
        "version": "1.0",
        "digestAlgorithm": "SHA-256",
        "docType": "org.iso.18013.5.1.mDL",
        "valueDigests": {
          "org.iso.18013.5.1": {
          1: h'0E5F0B6B33418E508740771E82F893372EAF5B2445BC4C84DCF08B005E9493FC',
          2: h'DE21BB62FF2897D8B986D2CDA9F9BC5865C02807F7B4D9DD1FA4A79DF4C0D37F',
          3: h'BC5568239E35CE9FF8798C27FFDCD757B134B679F0FE05729AA3491381912E65',
          5: h'E6048BDC7FD6454296F1E3F54536107C9C5B24C4064DE46A98121E3630EECCA2',
          6: h'73690D92DCAA61B0203870F67C6AA9FDFEA889B6F0C720DE757B4B0A8516A206',
          7: h'E353EA0B0FD92B6BE90C64CC3B2EE1284153A8F0F5066B99AAC599200E6EEEB2',
          8: h'29227872CEB49923D267B5F4BADE6D387B42AC2DC4B2AE26C9013067FEE7018A',
          9: h'A6A119F7CACAC0B8C6AACAC747FD3FE7E50B6D9BB8A507FDA79F0DF6646F285D',
          10: h'6D8025D2F02A5E7E1406FB6AAEB67F9EDE9B07191A53F3E23B77C528223A94E2',
          12: h'B0D43E4E2EA534E4D5304E64BCF7A0F13E2C8EE8304B9CD23ABA4909652A4647',
          13: h'FBF4DE318982F2DBAD43C601CAEB22628B301AC18AA8264C5831B2AAAC89C486'
          },
          "org.iso.18013.5.1.IT": {
          0: h'CF57377B675F64F37314739592C1E8A911A7DDAF341CE2902FE877C5A835E4C1',
          4: h'4A4B4CC64EC9299C1A2501EA449F577005E9F7A60408057C07A7C67FB151E5F5',
          11: h'78824FBD6FBBA88A2AAB44DF8B6F5E9759126D87D1F4415995E658FD9239E1FE'
          }
        },
        "deviceKeyInfo": {
          "deviceKey": {
          1: 2,
          -1: 1,
          -2: h'AFD09E720B918CEDC2B8A881950BAB6A1051E18AE16A814D51E609938663D5E1',
          -3: h'61FBC6C8AD24EC86A78BB4E9AC377DD2B7C711D9F2EB9AFD4AA0963662847AED'}},
          "validityInfo": {
            "signed": 0("2023-11-24T14:54:05Z"),
            "validFrom": 0("2023-11-24T14:54:05Z"),
            "validUntil": 0("2024-11-24T14:54:05Z")}
          }  >>),
          h'f2461e4fab69e9f7bcffe552395424514524d1679440036213173101448d1b1ab4a293859b389ffa8b47aeed10e9b0c1545412ac37c51a76482cd9bbbe110152'
        ]
      },
      "deviceSigned": {
        "nameSpaces": 24(<< {} >>),
        "deviceAuth": {
          "deviceSignature": [
            h'a10126',
            {},
            null,
            h'1fed7190d2975ab79c072e6f1d9d52436059d1fc959d55baf74f057d89b10fcc0dc77a50d433d4c76ddf26223c5560c4ab123b5cb5eb805a90036aa147493076'
          ]
        }
      }
    }
    ],
    "status": 0
  }

**Step 13**: The Verifier App is required to validate the signatures in the mDoc's issuerSigned field using the public key of the Credential Issuer specified within the mDoc. Subsequently, the Verifier MUST validate the signature in the deviceSigned field. If these signature checks pass, the Verifier can confidently consider the received information as valid.

Device Engagement
-----------------

The Device Engagement structure MUST be have at least the following components:

  - **Version**: *tstr*. Version of the data structure being used.
  - **Security**: an array that contains two mandatory values
  
    - the cipher identifier: see Table 22 of [ISO18013-5]
    - the mDL public ephemeral key generated by the Wallet Instance and required by the Verifier App to derive the Session Key. The mDL public ephemeral key MUST be of a type allowed by the indicated cipher suite.
  - **transferMethod**: an array that contains one or more transferMethod arrays when performing device engagement using the QR code. This array is for offline data retrieval methods. A transferMethod array holds two mandatory values (type and version). Only the BLE option is supported by this technical implementation profile, then the type value MUST be set to ``2``. 
  - **BleOptions**: this elements MUST provide options for the BLE connection (support for Peripheral Server or Central Client Mode, and the device UUID).


mDoc Request
------------

The messages in the mDoc Request MUST be encoded using CBOR. The resulting CBOR byte string for the mDoc Request MUST be encrypted with the Session Key obtained after the Device Engagement phase and MUST be transmitted using the BLE protocol.
The details on the structure of mDoc Request, including identifier and format of the data elements, are provided below. 

  - **version**: (tstr). Version of the data structure.
  - **docRequests**: Requested DocType, NameSpace and data elements.

    - **itemsRequest**: #6.24(bstr .cbor ItemsRequest).

      - **docType**: (tstr). The DocType element contains the type of document requested. See :ref:`Data Model Section <pid_eaa_data_model.rst>`.
      - **nameSpaces**: (tstr). See :ref:`Data Model Section <pid_eaa_data_model.rst>` for more details.

        - **dataElements**: (tstr). Requested data elements with *Intent to Retain* value for each requested element.

          - **IntentToRetain**: (bool). It indicates that the Verifier App intends to retain the received data element.
    - **readerAuth**: *COSE_Sign1*. It is required for the Verifier App authentication. 

.. note::
  
  The domestic data elements MUST not be returned unless specifically requested by the Verifier App.

mDoc Response
-------------

The messages in the mDoc Response MUST be encoded using CBOR and MUST be encrypted with the Session Key obtained after the Device Engagement phase.
The details on the structure of mDoc Response are provided below. 

  - **version**: (tstr). Version of the data structure.
  - **documents**: Returned *DocType*, and *ResponseData*.

    - **docType**: (tstr). The DocType element contains the type of document returned. See :ref:`Data Model Section <pid_eaa_data_model.rst>`.
    - **ResponseData**:

      - **IssuerSigned**: Responded data elements signed by the issuer.

        - **nameSpaces**: (tstr). See :ref:`Data Model Section <pid_eaa_data_model.rst>` for more details.

          - **IssuerSignedItemBytes**: #6.24(bstr .cbor). 

            - **digestID**: (uint).  Reference value to one of the **ValueDigests** provided in the *Mobile Security Object* (`issuerAuth`).
            - **random**: (bstr). Random byte value used as salt for the hash function. This value SHALL be different for each *IssuerSignedItem* and it SHALL have a minimum length of 16 bytes.
            - **elementIdentifier**: (tstr). Identifier of User attribute name contained in the Credential.
            - **elementValue**: (any). User attribute value
      - **DeviceSigned**: Responded data elements signed by the Wallet Instance.

        - **NameSpaces**: #6.24(bstr .cbor DeviceNameSpaces). The DeviceNameSpaces structure MAY be an empty structure. DeviceNameSpaces contains the data element identifiers and values. It is returned as part of the corresponding namespace in DeviceNameSpace.

          - **DataItemName**: (tstr). The identifier of the element.
          - **DataItemValue**: (any). The value of the element.
        - **DeviceAuth**:  The DeviceAuth structure MUST contain the DeviceSignature elements.

          - **DeviceSignature**: It MUST contain the device signature for the Wallet Instance authentication. 
  - **status**: It contains a status code. For detailed description and action required refer to to Table 8 (ResponseStatus) of the [ISO18013-5]


Session Termination
-------------------

The session MUST be terminated if at least one of the following conditions occur. 

  - After a time-out of no activity of receiving or sending session establishment or session data messages occurs. The time-out for no activity implemented by the Wallet Instance and the Verifier App SHOULD be no less than 300 seconds.
  - When the Wallet Instance doesn't accept any more requests.
  - When the Verifier App does not send any further requests. 

If the Wallet Instance and the Verifier App does not send or receive any further requests, the session termination MUST be initiated as follows. 

 - Send the status code for session termination, or
 - dispatch the "End" command as outlined in [ISO18013-5#8.3.3.1.1.5].

When a session is terminated, the Wallet Instance and the Verifier App MUST perform at least the following actions: 

  - destruction of session keys and related ephemeral key material; 
  - closure of the communication channel used for data retrieval.
