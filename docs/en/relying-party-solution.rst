.. include:: ../common/common_definitions.rst

.. _relying-party-solution:

Relying Party Solution
+++++++++++++++++++++++

This section defines the implementation of the online presentation and verification flow of a credential (PID or EAA), in accordance with the "OpenID for Verifiable Presentations - draft 19" specifications [OID4VP].


The specification supports two different scenarios, that are:

- Same Device Flow: Verifier and Wallet Instance acts in the same device
- Cross Device Flow: Verifier and Wallet Instance acts in different devices


Both of the scenarios will be discussed and analyzed in this section, taking into account differences between.


Same Device Flow
----------------
In a Same Device Authorization Flow, the User interacts with a Verifier that resides in the same device on which the Wallet Instance (and VCs) are stored.
This scenario utilizes HTTP redirects to finalize the authorization phase and obtain Verifiable Presentation(s).

Once authentication is performed, the User requests the display of attributes provided by the Wallet Instance.

⚠️ This flow will be described more in detail.


Cross Device Flow
-----------------
In a Cross Device Authorization Flow, the User interacts with a Verifier that resides in a different device on which the Wallet Instance (and VCs) are stored.
This scenario requests the Verifier to show a QR Code which the User will scan with his Wallet Instance.

Once authentication is performed, the User requests the display of attributes provided by the Wallet Instance.

.. image:: ../../images/cross_device_auth_seq_diagram.svg
  :align: center
  :target: https://www.plantuml.com/plantuml/umla/ZLB1ZXen3BtdAwmzLAtK_O6Lg7Q5UjXM5HJOtGkNC36GTd2eup2bNr-78LDc459lCo_FptxsUunYMTAkDZP9eBHR8HkpLynNVcz9uEub8j-1ZP3w-9kjQnHu9fMW2a-Kfa-PONtqj86fWiSJuO36Z4Rmb6IBf4GhFX30Q6GIt7_IvmUOuQ-4KM3AGR0IT8h4aBX2Ooln1okOPGvO2iQC6SkQWVsVLlAiSatxFeDnSAM-UO3vDZIAda27boswxyQOfh0hIqMZ0p__5bPoD_hBx7b9QmwxFZDFCPtC5nrlilg1MhQarR5VstZPmc31y2IYX9Ez6vje6LU52qxdJRJZzjiFJ1TFhxRsBcDVtXOmznkoahWyTwrw5putwXIG_Veue7n3iIfhh_gKgT31w_Hz_D0Iqhzfru6X2hJsl1li89bKh8rR0hfBLwbhffcgCCRX0TujwIAH23doWvCDqnNtWUADHDxQNI5qSznIfQ2ruO3S8--tDYAmZkuP8qXuqEJSmw4qyoIuOI_7Zs2Bc_QF76n3xP1XvSdbOuHrk-KiW1GJ8sXeMWoi_jMUVgA37CJsa1xvlyXLOaOIY3foDaM1AXnMZdCbTmVtQauj8LscTFBryeQDCOEWFYAvjAl_0W00

.. list-table::
  :widths: 25 25 25 25
  :header-rows: 1

  * - **Id**
    - **Source**
    - **Destination**
    - **Description**
  * - **1**
    - **User**
    - **Relying Party**
    - The user tries to access to a protected resource, the Relying Party redirect it to a discovery page in which the User selects the Login with Wallet button. The Authorization flow starts.
  * - **2**
    - **Relying Party**
    - **-**
    - The Relying Party creates an Authorization Request which contains the Presentation Definition/Scope, metadata and information the Wallet Instance needs to generate the response.
  * - **3**
    - **Relying Party**
    - **-**
    - Inserts the reference URI of the previously generated object into a QR Code
  * - **4**
    - **Relying Party**
    - **Wallet Instance**
    - QR Code is displayed on the screen, ready to be scanned
  * - **5**
    - **Wallet Instance**
    - **-**
    - The Wallet Instance Scans the QR Code
  * - **6**
    - **Wallet Instance**
    - **-**
    - Extracts the Request URI from the payload of the QR Code
  * - **7**
    - **Wallet Instance**
    - **Relying Party**
    - Requests the content of the Authorization Request (Request Object) by invoking the Request URI, passing as RequestBody the Wallet Instance Attestation
  * - **8**
    - **Relying Party**
    - **-**
    - The Relying Party attests the trust of the Wallet Instance using the Wallet Instance Attestation and verifies its metadata
  * - **9**
    - **Relying Party**
    - **Wallet Instance**
    - The Relying Party build the Request Object and returns it as response
  * - **10**
    - **Wallet Instance**
    - **-**
    - Verifies Request Object JWT signature
  * - **11**
    - **Wallet Instance**
    - **-**
    - The Wallet Instance attests the Relying Party Trust verifying the ``trust_chain``
  * - **12**
    - **Wallet Instance**
    - **-**
    - Verifies the Relying Party metadata to finalize the handshake
  * - **13**
    - **Wallet Instance**
    - **-**
    - Checks which Verifiable Presentation(s) the Relying Party is allowed to request
  * - **14**
    - **Wallet Instance**
    - **User**
    - The Wallet Instance requests the User for consent to finalize the transaction
  * - **15**
    - **User**
    - **Wallet Instance**
    - User confirms the request
  * - **16**
    - **Wallet Instance**
    - **-**
    - Process the Request Object and create an Authorization Response
  * - **17**
    - **Wallet Instance**
    - **Relying Party**
    - The Wallet provides the Authorization Response to the Relying Party
  * - **18**
    - **Relying Party**
    - **-**
    - Verifies Authorization Response JWT signature
  * - **19**
    - **Relying Party**
    - **-**
    - Process the content of Authorization Response, performs checks for integrity and tampering, and saves the Response to the persistence layer
  * - **20**
    - **Relying Party**
    - **Wallet Instance**
    - Relying Party notifies the Wallet Instance that the operation ends successfully

Authorization Request Details
-----------------------------
In a Cross Device Flow, The Authorization Request is required by the Relying Party in order to show the QR Code.
The User will scan it using the Wallet Instance that will grant the attributes to the RP.

The payload of the QR Code is a Base64 encoded string based on the following format:

.. code-block:: html

  eudiw://authorize?client_id=`client_id`&request_uri=`request_uri`


Where:

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **client_id**
    - Client Identifier of the Verifier
  * - **request_uri**
    - The Verifier's request URI used by the Wallet Instance to retrieve the Request Object


The Error Correction Level chosen for the QR Code is Q (Quartily - up to 25%), that offers a good balance between error correction capability and data density/space and it will allow the QR Code to remain readable even if it is damaged or partially obscured.


Below is a non-normative example of a QR Code displayed by the Verifier:

.. image:: ../../images/verifier_qr_code.svg
  :align: center


Below is a non-normative example of the payload and its Base64 decoded content:

.. code-block:: html

  ZXVkaXc6Ly9hdXRob3JpemU/Y2xpZW50X2lkPWh0dHBzOi8vdmVyaWZpZXIuZXhhbXBsZS5vcmcmcmVxdWVzdF91cmk9aHR0cHM6Ly92ZXJpZmllci5leGFtcGxlLm9yZy9hMTI1MmY5MC1hNjUyLTRjNDctODAzOS1mNjAwOTZjYXZ6cXc=

  eudiw://authorize?client_id=https://verifier.example.org&request_uri=https://verifier.example.org/a1252f90-a652-4c47-8039-f60096cavzqw



Request Object Details
----------------------
Once the Wallet Instance scan the QR Code, it extracts from the payload the ``request_uri`` parameter, then it will invoke the retrieved URI providing a Wallet instance Attestation in order to obtain the entire Request Object.

The following is a non-normative example of this interaction:

.. code-block:: javascript

  POST /{id} HTTP/1.1
  HOST: verifier.example.org
  Content-Type: application/json
  
  {
    "wallet_instance_attestation"="eyJhbGciOiJFUzI1NiIs...PT0iXX0"
  }

  

For more detailed information, please refer to the `Wallet Instance Attestation`_ section of this document.

⚠️ The right step in which the Wallet Instance should send the Wallet Instance Attestation to the Verifier is still under discussion.


Below is a non-normative response example:

Header
^^^^^^

.. code-block:: JSON

  {
    "alg": "ES256",
    "typ": "JWT",
    "x5c": [ "MIICajCCAdOgAwIBAgIC...20a" ],
    "kid": "e0bbf2f1-8c3a-4eab-a8ac-2e8f34db8a47",
    "trust_chain": [
      "MIICajCCAdOgAwIBAgIC...awz",
      "MIICajCCAdOgAwIBAgIC...2w3",
      "MIICajCCAdOgAwIBAgIC...sf2"
    ]
  }

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **alg**
    - Algorithm used to sign the JWT
  * - **typ**
    - Media Type of the JWT
  * - **x5c**
    - X.509 Certificate Chain containing the key used to sign the JWT
  * - **kid**
    - Key ID used identifying the key used to sign the JWT. Required if ``trust_chain`` is used
  * - **trust_chain**
    - Sequence of verified Entity Statements that validates a participant's compliance with the Federation


Payload
^^^^^^^

.. code-block:: JSON

  {
    "scope": "eu.europa.ec.eudiw.pid.it.1 eu.europa.ec.eudiw.pid.it.1:unique_id eu.europa.ec.eudiw.pid.it.1:given_name",
    "client_id_scheme": "entity_id",
    "client_id": "https://verifier.example.org",
    "client_metadata": "TBD",
    "response_mode": "direct_post.jwt",
    "response_type": "vp_token",
    "response_uri": "https://verifier.example.org/callback",
    "nonce": "2c128e4d-fc91-4cd3-86b8-18bdea0988cb",
    "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
    "iss": "https://verifier.example.org",
    "iat": 1672418465,
    "exp": 1672422065
  }


.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **scope**
    - Alias for a well-defined Presentation Definition. It will be used to identify PID Presentation Definition request.
  * - **client_id_scheme**
    - String identifying the scheme of the value in the ``client_id``. It will be ``entity_id``
  * - **client_id**
    - Client Identifier
  * - **client_metadata**
    - JSON object containing the Verifier metadata. It will be ``null`` since we will use ``entity_id`` as ``client_id_scheme``. Relying Party metadata will be present in the ``trust_chain`` statements
  * - **response_mode**
    - Used to ask the Wallet Instance in which way it has to send the response. It will be ``direct_post.jwt``
  * - **response_type**
    - Used to ask the Wallet Instance what it has to provide in Authorization Response. We will be ``vp_token``
  * - **response_uri**
    - The Response URI to which the Wallet Instance must send the Authorization Response using an HTTPS POST
  * - **nonce**
    - Fresh cryptographically random number with sufficient entropy used for security reason
  * - **state**
    - Unique identifier of the Authorization Request
  * - **iss**
    - The entity that issued the JWT. It will be populated with the Verifier URI
  * - **iat**
    - The NumericDate representing the time at which the JWT was issued
  * - **exp**
    - The NumericDate representing the expiration time on or after which the JWT MUST NOT be accepted for processing


⚠ The usage of ``scope`` instead of ``presentation_definition`` is still under discussion.

Here a non-normative example of ``presentation_definition`` that can be used instead of the ``scope`` example:


.. code-block:: JSON

  {
    "presentation_definition": {
      "id": "32f54163-7166-48f1-93d8-ff217bdb0653",
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
                  "$.credentialSubject.given_name"
                ]
              }
            ],
            "limit_discolusre": "preferred"
          }
        }
      ]
    }
  }

  

ℹ️ Note:

The following parameters, even if defined in [OID4VP], are not mentioned in the previous non-normative example, since their usage is conditional to the presence of other ones.

- ``presentation_definition``: string containing a Presentation Definition JSON object that articulate what proofs a Verifier requires. This parameter MUST not be present when ``presentation_definition_uri`` or ``scope`` are present
- ``presentation_definition_uri``: string containing an HTTPS URL pointing to a resource where a Presentation Definition JSON object can be retrieved. This parameter MUST not be present when ``presentation_definition`` or ``scope`` are present
- ``client_metadata_uri``: string containing an HTTPS URL pointing to a resource where a JSON object with the Verifier metadata can be retrieved. This parameter MUST not be present when ``client_metadata`` is present
- ``redirect_uri``: the redirect URI to which the Wallet Instance must redirect the Authorization Response. This parameter MUST not be present when ``response_uri`` is present
- ``aud``: the audience of the JWT. Since it would be equal to ``iss`` value, it is omitted


Authorization Response Details
------------------------------
After authenticating the User and getting her consent to share the request Credentials, the Wallet sends the Authorization Response to the Verifier using the ``response_uri`` endpoint (See Request Object Details).

The following is a non-normative example of this interaction:

.. code-block:: javascript

  POST /callback HTTP/1.1
  HOST: verifier.example.org
  Content-Type: application/x-www-form-urlencoded
  
  response=eyJhbGciOiJFUzI1NiIs...9t2LQ
  

Below is a non-normative example of the ``response`` JWS content:

.. code-block:: JSON

  {
    "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
    "vp_token": "eyJhbGciOiJFUzI1NiIs...PT0iXX0",
    "presentation_submission": {
        "definition_id": "32f54163-7166-48f1-93d8-ff217bdb0653",
        "id": "04a98be3-7fb0-4cf5-af9a-31579c8b0e7d",
        "descriptor_map": [
            {
                "id": "eu.europa.ec.eudiw.pid.it.1:unique_id",
                "path": "$.vp_token.verified_claims.claims._sd[0]",
                "format": "vc+sd-jwt"
            },
            {
                "id": "eu.europa.ec.eudiw.pid.it.1:given_name",
                "path": "$.vp_token.verified_claims.claims._sd[1]",
                "format": "vc+sd-jwt"
            }
        ]
    }
  }

Where: 

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **vp_token**
    - JWS containing a single (or an array) of Verifiable Presentation(s)
  * - **presentation_submission**
    - JSON Object contains mappings between the requested Verifiable Credentials and where to find them within the returned VP Token
  * - **state**
    - Unique identifier provided by the Verifier inside the Authorization Request


Below is a non-normative example of the ``vp_token`` JWS content:

⚠️ TBD, the following example is under analysis, not ready

.. code-block:: JSON

  {
    "iss": "https://pidprovider.example.org",
    "sub": "NzbLsXh8uDCcd7noWXFZAfHkxZsRGC9Xs...",
    "jti": "urn:uuid:6c5c0a49-b589-431d-bae7-219122a9ec2c",
    "iat": 1541493724,
    "exp": 1541493724,
    "status": "https://pidprovider.example.org/status",
    "cnf": {
      "jwk": {
        "kty": "RSA",
        "use": "sig",
        "n": "1Ta-sE …",
        "e": "AQAB",
        "kid": "YhNFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs"
      }
    },
    "type": "eu.eudiw.pid.it",
    "verified_claims": {
      "verification": {
        "_sd": [
          "OGm7ryXgt5Xzlevp-Hu-UTk0a-TxAaPAobqv1pIWMfw"
        ],
        "trust_framework": "eidas",
        "assurance_level": "high"
      },
      "claims": {
        "_sd": [
          "8JjozBfovMNvQ3HflmPWy4O19Gpxs61FWHjZebU589E",
          "BoMGktW1rbikntw8Fzx_BeL4YbAndr6AHsdgpatFCig"
        ]
      }
    },
    "_sd_alg": "sha-256"
  }


Entity Configuration Details
----------------------------
According to `Trust Model`_ section, the Verifier as Federation participant, needs to expose a well-known endpoint. 

The following is a non-normative example of this endpoint:

.. code-block:: javascript

  GET /.well-known/openid-federation HTTP/1.1
  HOST: verifier.example.org


Below is a non-normative response example:

Header
^^^^^^

.. code-block:: JSON

  {
    "alg": "ES256",
    "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
    "typ": "entity-statement+jwt"
  }

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
    - Key ID used identifying the key used to sign the JWT


Payload
^^^^^^^

.. code-block:: JSON

{
}


.. _Wallet Instance Attestation: wallet-instance-attestation.html
.. _Trust Model: trust.html

