.. include:: ../common/common_definitions.rst

.. _Wallet Attestation: wallet-attestation.html
.. _Trust Model: trust.html

.. _relying-party-solution:

Relying Party Solution
+++++++++++++++++++++++

This section describes how a Relying Party may request to a Wallet Instance the presentation of the PID and the (Q)EAAs, 
according to `OpenID for Verifiable Presentations - draft 20 <https://openid.net/specs/openid-4-verifiable-presentations-1_0.html>`_.

In this section the following flows are described:

- **Remote Same Device Flow**, where the user-agent and the Wallet Instance are used in the same device.
- **Remote Cross Device Flow**, where the user-agent and the Wallet Instance are used in different devices.
- **Proximity Flow**, where the User presents a Credential to a Verifier App according to ISO 18013-5. The User interacts with a Verifier using proximity connection technologies such as QR Code and Bluetooth Low Energy (BLE).

In the **Same Device** and **Cross Device** Flows described in this chapter, the User interacts with a remote Relying Party.

.. note::
    The provisioning of the Wallet Attestation from the Wallet Instace to the Relying Party is 
    under discussion within the international standardization working groups. At the current stage of the draft of this implementation profile,
    a mechanism based on `OAuth 2.0 Demonstrating Proof-of-Possession at the Application Layer (DPoP) <https://datatracker.ietf.org/doc/html/draft-ietf-oauth-dpop>`_
    is used.

Remote Protocol Flow
====================

In this scenario the Relying Party MUST provide the URL where the signed presentation Request Object is available for download.

Depending on whether the Relying Party client is on a mobile device or a workstation, 
the Relying Party MUST activate one of the supported remote flows:

* **Same Device**, the Relying Party MUST provide a HTTP redirect (302) location to the Wallet Instance;
* **Cross Device**, the Relying Party MUST provide a QR Code which the User frames with their Wallet Instance.

Once the Wallet Instance establishes the trust with the Relying Party, the User gives the consent for the release of the personal data, in the form of a Verifiable Presentation.

Below a sequence diagram that summarizes the interactions between all the involved parties.

.. image:: ../../images/cross_device_auth_seq_diagram.svg
  :align: center
  :target: //www.plantuml.com/plantuml/uml/XLLTJoCt57tthxXA7neGK7Rx5ebgMKg1tRPCax2y8277labS77lgZmbfrV_UQtkOJ4YaIWXfx7EFpxaVDvzyu2x4bMOy1clYQeQECNOfWdKmUF3e1i0zHCPczhKSVE_XPsoKG3-0xtvLYsNuh2EocdYKK3Kt0GQFN6iCS6U8tWZC7EjTI2IgKxv04yeBdA6HGA_imiQeDyeieAB3JKOso5Y4qvyeP0IFE8C9kYG736_KWWTb3OkS08GSmHZ_YkW3LCu6504bdNWRdI2MYmj8Xk0oXYKQUZC7mx1owEcxV5LBxl48BYuO5q4rF61IqE3R0rSEwInpMAV-pa7TgqzcU7pi0m6EZybR98V1mjOw26jV5D7l4xf2yHoT0jTApgXY_8_nbPK8zsEudKuhUb0gH_vW-EFvnoDOgx24iDnbeVpMLfd09FQjiAsnDMCBPsDD6gn_ApDOepTjHkC89akxpjIjWfgCf7hGxNe4zpMQVFkk0u3NzGbeAxW6lfDkjeOIEX7S42aarkxm-ZKuajSbz65yzsJcpguw9BbY16-JTtCzxR3tipzHf1hCDlruEaZfsLDu6GBwKdI2SB9VsGg2VK733jU-3I6_FFHDKwyrIg9xCg0yf7O6Ey-0Nv2EynDqnuqyc2gACJQ0muRUbYU4JFa2RBYE9A4V8tZDPqgheD2VaR2s3Bifs2zuoMwdVsV6OEgY3nta6pertxo3_8Q1Inxu5iMraed-o-CK9cfXU8WEzwzRNIZXMpNqHmKGjthdre6m9atVDkLnsrvNrioLMw7iMuhRybVta-dUAFewCL9DorWqzNCfwk6QNlVINDmhFjC8EqkX4Emr0esk98pY6kwyZ-XACjjQ7qvIZuNwHg3t-MNHKJ7cZAKesw0Z6EtSkvlRwStu-lftTZXYnE1gYU85RgsM5FGLD_1P6Ka5p48eYlgH_YhhFOMJ8mevXUW9aRdgEDDAm0i5bgsbJ6d3liLWeIdTaLFLpiePOp2bVkr6DrrAvOMs7YNm49oQnO1-H1LfTQevK3zt2qiv0gR-0kuGUCELfXBaKS-fOBsSFTIoBLRPvQqV69RD2Z7VooFOJaVUc3zyEFi07y_FuVuhoVXduCe2pPjoC89b2BM7w7Jf6TSsqRD8A-_VVlUjtqzNsQ0JliAT1RfkDpV9B7BxBoPh_xTx6-os_fV9gCtSxYu57vAAOJBujlgBWVPtfYIXwBWy5BfG3PeIaacINty2aN1K87ojSssi0nz5whnvr5dx9_eNL_e_


The details of each step shown in the previous picture are described in the table below.


.. list-table::
  :widths: 50 50
  :header-rows: 1

  * - **Id**
    - **Description**
  * - **1**, **2**
    - The User asks for access to a protected resource, the Relying Party redirects the User to a discovery page in which the User selects the *Login with the Wallet* button. The Authorization flow starts.
  * - **3**, **4**, **5**
    - The Relying Party creates an Authorization Request which contains the scopes of the request and provides it to the requester.
  * - **6**, **7**, **8**, **9**
    - In the **Cross Device Flow**: the Request URI is provided in the form of a QR Code that is shown to the User. The User frames the QRCode with the Wallet Instance and extracts the Request URI. In the **Same Device Flow** the Relying Party responses with the Request URI in the form of HTTP Redirect Location (302). 
  * - **10**
    - The Wallet Instance requests the content of the Authorization Request by invoking the Request URI, passing an Authorization DPoP HTTP Header containing the Wallet Attestation and the DPoP proof HTTP Header.
  * - **11**
    - The Relying Party attests the trust to the Wallet Instance using the Wallet Attestation and evaluates the Wallet Instance capabilities.
  * - **12**
    - The Relying Party issues a signed Request Object, returning it as response. The ``exp`` value of the signed Request Object MUST be no more than 240 seconds.
  * - **13**, **14**, **15**, **16**
    - The Wallet Instance verifies the Request Object JWS. The Wallet Instance attests the trust to the Relying Party by verifying the Trust Chain. The Wallet Instance verifies the signature of the request and processes the Relying Party metadata to attest its capabilities and allowed scopes, attesting which Verifiable Credentials and personal attributes the Relying Party is granted to request.
  * - **17**, **18**
    - The Wallet Instance requests the User's consent for the release of the credentials. The User authorizes and consents the presentation of their credentials, by selecting/deselecting the personal data to release.
  * - **19**
    - The Wallet Instance provides the Authorization Response to the Relying Party using an HTTP request with the method POST (response mode "direct_post").
  * - **20**, **21**, **22**
    - The Relying Party verifies the Authorization Response, extracts the credential and attests the trust to the credentials Issuer. The Relying Party verifies the revocation status and the proof of possession of the presented credential.
  * - **23**
    - The Relying Party authenticates the User.
  * - **24**
    - The Relying Party notifies to the Wallet Instance that the operation ends successfully.


Authorization Request Details
-----------------------------

The Relying Party MUST create a Request Object in the format of signed JWT, then provide it to the Wallet Instance through an HTTP URL (request URI). The HTTP URL points to the web resource where the signed request object is available for download. The URL parameters contained in the Relying Party response, containing the request URI, are described in the Table below.

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **client_id**
    - Unique identifier of the Relying Party.
  * - **request_uri**
    - The HTTP URL used by the Wallet Instance to retrieve the signed Request Object from the Relying Party. The URL is intentionally extended with a random value that uniquely identifies the transaction.

Below a non-normative example of the response containing the required parameters previously described.

.. code-block:: javascript

  eudiw://authorize?client_id=`$client_id`&request_uri=`$request_uri`

The value corresponding to the `request_uri` endpoint MUST be randomized, according to `RFC 9101, The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR) <https://www.rfc-editor.org/rfc/rfc9101.html#section-5.2.1>`_ Section 5.2.1.


In the **Same Device Flow** the Relying Party uses a HTTP response redirect (status code 302) as represented in the following non-normative example:

.. code:: text

    HTTP/1.1 /pre-authz-endpoint Found
    Location: https://wallet-providers.eudi.wallet.gov.it?
    client_id=https%3A%2F%2Frelying-party.example.org%2Fcb
    &request_uri=https%3A%2F%2Frelying-party.example.org%2Frequest_uri%3Fid%3Drandom-value


In the **Cross Device Flow**, a QR Code is shown by the Relying Party to the User in order to provide the Authorization Request. The User frames the QR Code using their Wallet Instance. The QR Code payload MUST be a **Base64 encoded string**.

Below is represented a non-normative example of a QR Code issued by the Relying Party.

.. image:: ../../images/verifier_qr_code.svg
  :align: center


Below is represented a non-normative example of the QR Code raw payload:

.. code-block:: text

  ZXVkaXc6Ly9hdXRob3JpemU/Y2xpZW50X2lkPWh0dHBzOi8vdmVyaWZpZXIuZXhhbXBsZS5vcmcmcmVxdWVzdF91cmk9aHR0cHM6Ly92ZXJpZmllci5leGFtcGxlLm9yZy9yZXF1ZXN0X3VyaS8=

The decoded content of the previous Base64 value is represented below:

.. code-block:: text

  eudiw://authorize?client_id=https%3A%2F%2Frelying-party.example.org&request_uri=https%3A%2F%2Frelying-party.example.org%2Frequest_uri%3Fid%3Drandom-value

.. note::
    The *error correction level* chosen for the QR Code MUST be Q (Quartily - up to 25%), since it offers a good balance between error correction capability and data density/space. This level of quality and error correction allows the QR Code to remain readable even if it is damaged or partially obscured.


Cross Device Flow Status Checks and Security
--------------------------------------------

When the flow is Cross Device, the user-agent needs to check the session status to the endpoint made available by Relying Party (status endpoint). This check MAY be implemented in the form of JavaScript code, within the page that shows the QRCode, then the user-agent checks the status with a polling strategy in seconds or a push strategy (eg: web socket).

Since the QRcode page and the status endpoint are implemented by the Relying Party, it is under its responsability the implementation details of this solution, since it is related to the Relying Party's internal API.

The Relying Party MUST bind the request of the user-agent, with a Secure and HttpOnly session cookie, with the issued request. The request url SHOULD include a parameter with a random value. The HTTP response returned by this specialized endpoint MAY contain the HTTP status codes listed below:

* **201 Created**. The signed Request Object was issued by the Relying Party that waits to be downloaded by the Wallet Instance at the **request_uri** endpoint.
* **202 Accepted**. This response is given when the signed Request Object was obtained by the Wallet Instance.
* **200 OK**. The Wallet Instance has provided the presentation to the Relying Party's  **redirect_uri** endpoint and the User authentication is successful. The Relying Party updates the session cookie allowing the user-agent to access to the protected resource. An URL is provided carrying the location where the user-agent is intended to navigate.
* **401 Unauthorized**. The Wallet Instance or its User have rejected the request, or the request is expired. The QRCode page SHOULD be updated with an error message.

Below a non-normative example of the HTTP Request to this specialized endpoint, where the parameter ``id`` contains an opaque and random value:

.. code::

  GET /session-state?id=3be39b69-6ac1-41aa-921b-3e6c07ddcb03
  HTTP/1.1
  HOST: relying-party.example.org


Request Object Details
----------------------
The following actions are made by the Wallet Instance:

- scan the QR Code (Cross Device only);
- extract from the payload the ``request_uri`` parameter;
- invoke the retrieved URI;
- provide in the request its Wallet Attestation, using :rfc:`9449` to proof the legitimate possession of it;
- obtain the signed Request Object from the Relying Party.
- evaluate the trust with the Relying Party, by evaluating the Trust Chain related to it.

Below a non-normative example of HTTP request made by the Wallet Instance to the Relying Party to provide the Wallet Instance Attestion and retrieve the signed Request Object:

.. code-block:: javascript

  GET /request_uri HTTP/1.1
  HOST: relying-party.example.org
  Authorization: DPoP $WalletInstanceAttestation
  DPoP: $WalletInstanceAttestationProofOfPossession


More detailed information about the `Wallet Attestation`_ is available in its dedicated section of this technical specification.

To attest a high level of security, the Wallet Instance submits its Wallet Attestation to the Relying Party, disclosing its capabilities and the security level attested by its Wallet Provider.

Below the description of the parameters defined in *OAuth 2.0 Demonstration of Proof-of-Possession at the Application Layer (DPoP)*.

If the DPoP HTTP Header is missing, the Relying Party would assume the lowest attestable level of security to the Wallet Instance it is interacting with.

DPoP HTTP Header
^^^^^^^^^^^^^^^^

A **DPoP proof** is included in the request using the HTTP Header ``DPoP`` and containing a JWS. The JWS MUST be verified with the public key made available in the Wallet Attestation (``Authorization: DPoP``).

The JOSE header of the **DPoP JWS** MUST contain at least the following parameters:

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **typ** 
      - It MUST be equal to ``dpop+jwt``. 
      - [:rfc:`7515`] and [:rfc:`8725`. Section 3.11].
    * - **alg** 
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms in Section *Cryptographic Algorithms* <supported_algs>`* and MUST NOT be none or an identifier for a symmetric algorithm (MAC).
      - [:rfc:`7515`]
    * - **jwk** 
      - Representing the public key chosen by the client, in JSON Web Key (JWK) [RFC7517] format, as defined in Section 4.1.3 of [RFC7515]. It MUST NOT contain a private key.
      - [:rfc:`7517`] and [:rfc:`7515`]


The payload of a **DPoP proof** MUST contain at least the following claims:

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **jti**
      - Unique identifier for the DPoP proof JWT. The value SHOULD be set with a *UUID v4* value, according to [:rfc:`4122`].
      - [:rfc:`7519`. Section 4.1.7].
    * - **htm**
      - The value of the HTTP method of the request to which the JWT is attached.
      - [:rfc:`9110`. Section 9.1].
    * - **htu**
      - The HTTP target URI, without query and fragment parts, of the request to which the JWS is attached.
      - [:rfc:`9110`. Section 7.1].
    * - **iat**
      - UNIX Timestamp with the time of JWT issuance, coded as NumericDate as indicated in :rfc:`7519`. 
      - [:rfc:`7519`. Section 4.1.6].
    * - **ath**
      - Hash of the Wallet Attestation. 
      - [:rfc:`9449`. Section 4.2].


Therein a non-normative example of the DPoP decoded content:

.. code-block:: text

    {
      "typ": "dpop+jwt",
      "alg": "ES256",
      "jwk": {
        "kty": "EC",
        "x": "l8tFrhx-34tV3hRICRDY9zCkDlpBhF42UQUfWVAWBFs",
        "y": "9VE4jf_Ok_o64zbTTlcuNJajHmt6v9TDVrU0CdvGRDA",
        "crv": "P-256"
      }
    }
    .
    {
      "jti": "f47c96a1-f928-4768-aa30-ef32dc78aa69",
      "htm": "GET",
      "htu": "https://relying-party.example.org/request_uri",
      "iat": 1562262616,
      "ath": "fUHyO2r2Z3DZ53EsNrWBb0xWXoaNy59IiKCAqksmQEo"
    }


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
    "response_uri": "https://relying-party.example.org/callback",
    "nonce": "2c128e4d-fc91-4cd3-86b8-18bdea0988cb",
    "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
    "iss": "https://relying-party.example.org",
    "iat": 1672418465,
    "exp": 1672422065
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
  - ``presentation_definition_uri``: string containing an HTTPS URL pointing to a resource where a Presentation Definition JSON object can be retrieved. This parameter MUST be present when ``presentation_definition`` parameter or a ``scope`` value representing a Presentation Definition is not present.
  - ``client_metadata``: A JSON object containing the Relying Party metadata values. The ``client_metadata`` parameter MUST NOT be present when ``client_id_scheme`` is ``entity_id``. The ``client_metadata`` is taken from ``trust_chain``.
  - ``client_metadata_uri``: string containing an HTTPS URL pointing to a resource where a JSON object with the Relying Party metadata can be retrieved. The ``client_metadata_uri`` parameter MUST NOT be present when ``client_id_scheme`` is ``entity_id``.
  - ``redirect_uri``: the redirect URI to which the Wallet Instance MUST redirect the Authorization Response. This parameter MUST not be present when ``response_uri`` is present.


Authorization Response Details
------------------------------
After getting the User authorization and consent for the presentation of the credentials, the Wallet sends the Authorization Response to the Relying Party ``response_uri`` endpoint, the content should be encrypted according `OPENID4VP`_ Section 6.3, using the Relying Party public key.

.. note::
    **Why the response is encrypted?**

    The response sent from the Wallet Instance to the Relying Party is encrypted to prevent a malicious agent from gaining access to the plaintext information transmitted within the Relying Party's network. This is only possible if the network environment of the Relying Party employs `TLS termination <https://www.f5.com/glossary/ssl-termination>`_. Such technique employs a termination proxy that acts as an intermediary between the client and the webserver and handles all TLS-related operations. In this manner, the proxy deciphers the transmission's content and either forwards it in plaintext or by negotiates an internal TLS session with the actual webserver's intended target. In the first scenario, any malicious actor within the network segment could intercept the transmitted data and obtain sensitive information, such as an unencrypted response, by sniffing the transmitted data.

Below a non-normative example of the request:

.. code-block:: http

  POST /callback HTTP/1.1
  HOST: relying-party.example.org
  Content-Type: application/x-www-form-urlencoded
  
  response=eyJhbGciOiJFUzI1NiIs...9t2LQ
  

Below is a non-normative example of the decrypted JSON ``response`` content:

.. code-block:: JSON

  {
    "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
    "vp_token": "eyJhbGciOiJFUzI1NiIs...PT0iXX0",
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
    - JWS containing a single or an array of Verifiable Presentation(s) in the form of signed JWT.
  * - **presentation_submission**
    - JSON Object containing the mappings between the requested Verifiable Credentials and where to find them within the returned VP Token.
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
    "iss": "https://wallet-provider.example.org/instance/vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "jti": "3978344f-8596-4c3a-a978-8fcaba3903c5",
    "aud": "https://relying-party.example.org/callback",
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
    - The digital credential in its original state. The public key contained in the digital credential MUST be used to verify the entire VP JWS as Proof of Possession of the private key which the public part is carried in the digital credential (Holder Key Binding).
  * - **jti**
    - JWS Unique identifier.
  * - **iat**
    - Unix timestamp of the issuance datetime.
  * - **exp**
    - Unix timestamp beyond which the presentation of the digital credential will no longer be considered valid.
  * - **aud**
    - Audience of the VP, corresponding to the ``redirect_uri`` within the Authorization request issued by the Relying Party.
  * - **nonce**
    - Nonce provided by the Relying Party within the Authorization Request.

Relying Party Entity Configuration
---------------------------------------------
According to the `Trust Model`_ section, the Relying Party is a Federation Entity and MUST expose a well-known endpoint containing its Entity Configuration. 

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
                "redirect_uris": [
                    "https://relying-party.example.org/callback"
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
                    "RS256",
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
                    "RS256",
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

This section describes how a Relying Party requests the presentation of an *mDoc-CBOR* Credential to a Wallet Instance according to the *ISO 18013-5 Specification*. Only *Supervised Device Retrieval flow* is supported in this technical implementation profile. 

The presentation phase is divided into three sub-phases: 
 
  1. **Device Engagement**: This subphase starts when the User is asked to disclose some attributes from their mDoc(s). The objective of this subphase is to establish a secure communication channel between the Wallet Instance and the Verifier App, so that the mDoc requests and responses can be exchanged during the communication subphase.
  The messages exchanged in this subphase are transmitted through short-range technologies to limit the possibility of interception and eavesdropping.
  This technical implementation profile only support QR code for the Device Engagement.

  2. **Session establishment**: In session establishment, the Verifier App establishes a connection on a secure channels. 
  The data transmitted in such a connection will all be encrypted with the session key that both the Wallet Instance and the verifier know at this point in time. 
  The established session MAY be terminated based on the conditions as detailed in [ISO18013-5#9.1.1.4].

  3. **Communication - Device Retrieval**: The Verifier App encrypts the mdoc request with the appropriate session key and sends it to the Wallet Instance together with its public key in a session establishment message. The mdoc uses the data from the session establishment message to derive the session key and decrypt the mdoc request.
  In communication subphase, the Verifier App MAY ask the Wallet for information about the holder using mDoc requests and responses. 
  The main channel for communication is the secure channel that has been established with the session establishment. The Wallet Instance encrypts the mdoc response with the appropriate session key and sends it to the Verifier App in a session data message.  
  For the communication sub-phase, only BLE is supported by this technical implementation profile. 


The Figure below presents the flow diagram of ISO 18013-5 compliant proximity flow.

.. _fig_High-Level-Flow-ITWallet-Presentation-ISO:
.. figure:: ../../images/High-Level-Flow-ITWallet-Presentation-ISO.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/bL9BZnCn3BxFhx3A0H3q3_ImMlOXXBJYqGguzE9ct2RQn0bvJDb_ZoSP3QFI2xab_Xx-xDocZ34NPpiisNDn1ufT1t9GPH_XUw88cA3KjuF_3QlnwNM2dHDYq9vf1Q-Up4ddErkeme9KZ381ESFg9rfB6JwnEB4IiAYTAuou7nN_Al-WQ8xcVzHd2dm8eKeFI-cMfApNDpVd3Nm9n90rmKLBa3s4I8b441dSWrTm7wcNkq7RD3xxJE07CIhlXmqyq624-CWdF94RYQaSWiP4iAweRzjr1vLvRkOVYIcYY32TWO8c9rSBp_GYWKoSe88LzPtsvx5HKO5xtnCSVVpNibA6ATjE8IyfKr7aBgptVDry0WlPXIBOH2aPpoEcbgzDOJTXIEPui2PfrqROZogki56OfNuvcxkdHv5N9H8eZSnaPLRJwUPU95JTn9P-5J60Tn2AcAZQjJ_MiCljxndUN6texN8Dr-ErSjd0roZrNEUjFDSVaJqaZP6gOMpDK0-61UHglkcJjJL75Cx4NHflAKT30xLGH_41wnLQIDb7FD6C7URSAOZCSfCjxyjSWcHEZBb4slCuTQL9FJVsWDRq9akuxfQuByx-0G00

    High-Level Proximity Flow

**Step 1-3**: The Verifier asks the User to disclose some attributes from their mdoc(s) stored in the Wallet Instance. The User opens the Wallet Instance. The Wallet Instance MUST generate a new ephemeral key pair (EDeviceKey.Priv, EDeviceKey.Pub), and includes the cipher suite identifier, the identifier of the elliptic curve to be used for key agreement and the EDeviceKey public point, as part of the device engagement structure (see [ISO18013-5#9.1.1.4]). This pair of keys is ephemeral and MUST be invalidated as soon as the secure channel is established. Finally, the Walle Instance shows the QR Code for the Device Engagement.

Following is an example of a device engagement structure for QR device engagement and BLE as the data retrieval mode.

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



**Step 4-6**: The Verifier App scan the QR Code, generates its own set of ephemeral keys (EReaderKey. Priv, EReaderKey.Pub) and computes the session key, involving the public key received in the Engagement Structure and its newly-generated private key as specified in [ISO18013-5#9.1.1.5]. Finally, generates its session key that MUST be derived independently by the Wallet Instance and the Verifier App.

**Step 7**: The Verifier App generates the mdoc request that MUST be encrypted with the appropriate session key, and sends it to the Wallet Instance together with EReaderKey.Pub in a session establishment message. The mdoc request MUST be encoded as CBOR as in the following  non-normative example.

CBOR data: 
.. code-block::

  a26776657273696f6e63312e306b646f63526571756573747381a26c6974656d7352657175657374d818590152a267646f6354797065756f72672e69736f2e31383031332e352e312e6d444c6a6e616d65537061636573a2746f72672e69736f2e31383031332e352e312e4954a375766572696669636174696f6e2e65766964656e6365f4781c766572696669636174696f6e2e6173737572616e63655f6c6576656cf4781c766572696669636174696f6e2e74727573745f6672616d65776f726bf4716f72672e69736f2e31383031332e352e31ab76756e5f64697374696e6775697368696e675f7369676ef47264726976696e675f70726976696c65676573f46f646f63756d656e745f6e756d626572f46a69737375655f64617465f46f69737375696e675f636f756e747279f47169737375696e675f617574686f72697479f46a62697274685f64617465f46b6578706972795f64617465f46a676976656e5f6e616d65f468706f727472616974f46b66616d696c795f6e616d65f46a726561646572417574688443a10126a11821590129308201253081cda00302010202012a300a06082a8648ce3d0403023020311e301c06035504030c15536f6d652052656164657220417574686f72697479301e170d3233313132343130323832325a170d3238313132323130323832325a301a3118301606035504030c0f536f6d6520526561646572204b65793059301306072a8648ce3d020106082a8648ce3d03010703420004aa1092fb59e26ddd182cfdbc85f1aa8217a4f0fae6a6a5536b57c5ef7be2fb6d0dfd319839e6c24d087cd26499ec4f87c8c766200ba4c6218c74de50cd1243b1300a06082a8648ce3d0403020347003044022048466e92226e042add073b8cdc43df5a19401e1d95ab226e142947e435af9db30220043af7a8e7d31646a424e02ea0c853ec9c293791f930bf589bee557370a4c97bf6584058a0d421a7e53b7db0412a196fea50ca6d4c8a530a47dd84d88588ab145374bd0ab2a724cf2ed2facf32c7184591c5969efd53f5aba63194105440bc1904e1b9

The above CBOR data in diagnostic notation: 
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

**Step 8**: The Wallet Instance uses the session establishment message to derive the session keys and decrypt the mdoc request. It computes the session key using the public key received from the Verifier App and its private key.

**Step 9-10**: Upon receiving the mDoc request, the Wallet Instance identifies the documents containing the requested attributes and prompts the User for permission to share this information with the Verifier. If the User consents, the Wallet produces an mDoc response and sends it to the Verifier App via the secure channel.

**Step 11-12**: In case of User consent, the Wallet Instance generates an mDoc response and sends it to the Verifier App through the secure channel. The mDoc response MUST be CBOR encoded, and its structure is defined in [ISO18013-5#8.3.2.1.2.2]. A non-normative example of a mDoc response is given below.

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

**Step 13**: The Verifier App MUST verify that the signatures in the mDoc **issuerSigned** field are valid using the public key of the Credential Issuer declared in the mDoc itself.  At this point, the verifier MUST check the signature in the **deviceSigned** field. If the check of these signatures is successful, the verifier can trust that the information it received is valid.





Device Engagement
-----------------

The Device Engagement structure MUST be have at least the following components:

  - **Version**: *tstr*. Version of the data structure being used.
  - **Security**: an array that contains two mandatory values
  
    - the cipher identifier: see Table 22 of [ISO18013-5]
    - the mDL public ephemeral key generated by the Wallet Instance and required by the Verifier App to derive the Session Key. The mDL public ephemeral key MUST be of a type allowed by the indicated cipher suite.
  - **TransferMethod**: an array that contains one or more transferMethod arrays when performing device engagement using the QR code. This array is for offline data retrieval methods. A transferMethod array holds two mandatory values (type and version). Only the BLE option is supported by this technical implementation profile, then the type value MUST be set to '2'. 
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

  - After a time-out of no activity of receiving or sending session establishment or session data messages occurs. The time-out for no activity implemented by the Wallet Instance and the Verifier App SHOULD be no less than 300 s.
  - If the Wallet Instance does not want to receive any further requests. 
  - If the Verifier App does not want to send any further requests. 

If the Wallet Instance and the Verifier App does not want to send or receive any further requests, it MUST initiate session termination as follows. 

  - to send the status code for session termination or 
  - to send the "End" command defined in [ISO18013-5#8.3.3.1.1.5].

When a session is terminated, the Wallet Instance and the Verifier App MUST perform at least the following actions: 

  - destruction of session keys and related ephemeral key material; 
  - closure of the communication channel used for data retrieval.
