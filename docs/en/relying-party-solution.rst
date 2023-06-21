.. include:: ../common/common_definitions.rst

.. _relying-party-solution.rst:

Relying Party Solution
+++++++++++++++++++++++

This document defines the implementation of the online presentation and verification flow of a credential (PID or (Q)EAA), in accordance with the "OpenID for Verifiable Credential Presentation - draft 19" specifications [OID4VCP], in the context of a Cross-Device flow scenario.


Cross Device Authentication
---------------------------

In the Cross Device Authentication, the user logs into the website and provides their consent for presenting their PID through the Wallet. 
Once authentication is performed, the end user can request the display of attributes provided by the Wallet.
Below is explained the Cross Device Authentication flow.

NOTE: Use Cases about other flows will be analysed in next sprints.


.. image:: ..\\images\\cross_device_auth_seq_diagram.svg
  :align: center
  :target: http://www.plantuml.com/plantuml/umla/TLFDZjem4BxxAKPKgjf3Ns0bgkrIMj5M8eKiU-7Y91DmrnbJ_soMFdtjiCOcY5iqy_rydntV6ykrTPrat5b5hgjGCtRmCr6B0oSBaqU3UWBSW6EiKgymMQ4y2jf1uL772Rpx9NPx-o0TNl8sg4KhKCE7RrgHdLFpSP1fR-8UUFryXbN8a1hmZgCyJrnAjB0W7vrg7C0zOzCfV75sZ-IHt0f50DCfS_3fC_HtmqffyG-X5tOF9mt6QojUk4LmwRDdVU2qU0VhS3PdwY3A6ap8H6gHjHXebQVDD8RP1GzM-DUXIPQXN-Kf9wkuXiVL8hUeecwRT7-lOAQQkEXzpBtg_JGCyngiZ_kQqvaLX_DNgpquDzvIgrMNaB7FztbvXYshF-XPMwgEEVMwLZ0PiKR5Of8Dbw89inzF9Qp5ZhXrEgqBhMeqPfpW_PQowqO8VscAN2pNvTK5c8CYWwCR7EKEz9kH4Y26kccHwxATLku0XP8oF1ld8qlG4TjYEkTHvk6KIyt913b5YwytyiwyakiGDWMKwXafMote9PR9bAwLyvzn-NFK0AbXRq5TzfQQ7DPUr7RitfDS9_y3

.. list-table:: 
  :widths: 25 25 50
  :header-rows: 1

  * - **Message**
    - **Source**
    - **Destination**
    - **Description**
  * - **1**
    - **User**
    - **Wallet Instance**
    - The User navigates the Verifier's website and clicks on the 'Login with IT Wallet' button
  * - **2**
    - **User**
    - **Wallet Instance**
    - The Authorization flow starts
  * - **3-4**
    - **Verifier (FE)**
    - **Verifier (BE)**     
    - Requests the generation of an Authorization Request which contains the Presentation Definition/Scope, Verifier metadata and information the wallet needs to generate the response.
  * - **5**
    - **Verifier (FE)**
    - **-**     
    - Inserts the reference to the previously generated object into a QR Code that is displayed on the screen
  * - **6**
    - **Verifier (FE)**
    - **Wallet**
    - QR Code is displayed ready to be scanned
  * - **7**
    - **Wallet**
    - **-**
    - Scans the QR Code
  * - **8**
    - **Wallet**
    - **-**
    - Extracts the Request URI from the payload of the QR Code
  * - **9-10**
    - **Wallet**
    - **Verifier (BE)**          
    - Requests the content of the Authorization Request by invoking the Request URI
  * - **11**
    - **Wallet**
    - **-**     
    - Verify the signature of the Request Object (JWT)
  * - **12**
    - **Wallet**
    - **-**     
    - Processes the content of the object and proceeds with the authentication
  * - **13**
    - **Wallet**
    - **Verifier (BE)**     
    - Generate an Authorization Response containing the VP Token
  * - **14**
    - **Verifier (BE)**
    - **-**     
    - Verify Authorization Response signature
  * - **15**
    - **Verifier (BE)**
    - **-**     
    - Process the content of the object, performs checks for integrity and tampering, and saves the Response to the persistence layer
  * - **16**
    - **Verifier (FE)**
    - **Verifier (BE)**     
    - Request a Session Cookie through polling, which will be available downstream after the checks performed in the previous step
  * - **17**
    - **Verifier (BE)**
    - **-**     
    - Consume the VP Token
  *  - **18**
    - **Verifier (BE)**
    - **-**     
    - Requests the invalidation of the current session as the transaction has been successfully completed
  * - **19**
    - **Verifier (FE)**
    - **User**     
    - The user is successfully authenticated on the Verifier's website


AuthorizationRequest Details
----------------------------
The AuthorizationRequest object is required by the Relying Party FrontEnd in order to show the QR Code. 
The User will scan the QR Code using the Wallet granting the attributes to the RP.

.. code-block:: javascript
  POST /oid4vp HTTP/1.1
  HOST: <VERIFIER_RELYING_PARTY_HOST>

  HTTP/1.1 201 OK


Below a non-normative response example

.. code-block:: javascript

  {
    "alg": "ES256",
    "typ": "JWT",
    "x5c": [ "MIICajCCAdOgAwIBAgIC...20a" ],
    "kid": "e0bbf2f1-8c3a-4eab-a8ac-2e8f34db8a47",
    "trust_chain":[
      "MIICajCCAdOgAwIBAgIC...awz",
      "MIICajCCAdOgAwIBAgIC...2w3",
      "MIICajCCAdOgAwIBAgIC...sf2"
    ]
  }
  .
  { 
    "transactionId": "e9673f90-a652-4c47-8039-f60096cabafb",
    "state": "a1252f90-a652-4c47-8039-f60096cavzqw",
    "nonce": "o1923f90-a652-4c47-8039-f60096cabcza",
    "requestUri": "oid4vp-wallet://authorize?client_id=https://<VERIFIER_RELYING_PARTY_HOST>&request_uri=https://<VERIFIER_RELYING_PARTY_HOST>/oid4vp/a1252f90-a652-4c47-8039-f60096cavzqw",
    "iss": "https://<VERIFIER_RELYING_PARTY_HOST>",
    "aud": "https://<VERIFIER_RELYING_PARTY_HOST>",
    "iat": "1686823112",
    "exp": "1686823812"
  }
  .
  SIGNATURE


Header
^^^^^^

.. list-table:: 
  :widths: 25 50
  :header-rows: 1

  * - **Param**
    - **Description**
  * - **alg**
    - Algorithm used to sign the JWT
  * - **typ**
    - Media Type of the JWT
  * - **x5c**
    - X.509 Certitifcate Chain containing the Key used to sign the JWT
  * - **kid**
    - Key ID used identifying the Key used to sign the JWT. Required if trust_chain is used
  * - **trust_chain**
    - Sequence of verified Entity Statements that validates a participant's compliance with the Federation


Payload
^^^^^^
.. list-table:: 
  :widths: 25 50
  :header-rows: 1

  * - **Param**
    - **Description**
  * - **transactionId**
    - Unique identifier of the authorization transaction
  * - **state**
    - Unique identifier of the AuthorizationRequest
  * - **nonce**
    - Fresh cryptographically random number with sufficient entropy used for Security Reason
  * - **requestUri**
    - The payload of the QR Code from where the Wallet can obtain the Request Object containing Authorization Request parameters
  * - **iat**
    - The timestamp when the JWT was issued
  * - **exp**
    - The timestamp when the JWT is set to expire
  * - **iss**
    - The entity that issued the JWT. It will be populated with the Verifier URI
  * - **aud**
    - The audience of the JWT. It will be equal to iss value


RequestObject Details
---------------------
The "requestUri" claim provided in AuthorizationRequest response object will be the payload of QR Code.
The Wallet will invoke the Relying Party using the "request_uri" param found in QR Code in order to obtain the entire Authorization Request Object.

.. code-block:: javascript
  GET /oid4vp/{id} HTTP/1.1
  HOST: <VERIFIER_RELYING_PARTY_HOST>

  HTTP/1.1 200 OK


Below a non-normative response example

.. code-block:: javascript

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
  .
  { 
    "presentation_definition": null,
    "presentation_definition_uri": null,
    "scope": "eu.europa.ec.eudiw.pid.it.1 eu.europa.ec.eudiw.pid.it.1:give eu.europa.ec.eudiw.pid.it.1:email",
    "client_id_scheme": "entity_id",
    "client_id": "https://<VERIFIER_RELYING_PARTY_HOST>",
    "client_metadata": null,
    "client_metadata_uri": null,
    "response_mode": "direct_post.jwt",
    "response_type": "vp_token",
    "response_uri": "https://<VERIFIER_RELYING_PARTY_HOST>/oid4vp/callback",
    "redirect_uri": null,
    "nonce": "2c128e4d-fc91-4cd3-86b8-18bdea0988cb",
    "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
    "iss": "https://<VERIFIER_RELYING_PARTY_HOST>",
    "aud": "https://<VERIFIER_RELYING_PARTY_HOST>",
    "iat": 1672418465,
    "exp": 1672422065
  }
  .
  SIGNATURE



Header
^^^^^^

.. list-table:: 
  :widths: 25 50
  :header-rows: 1

  * - **Param**
    - **Description**
  * - **alg**
    - Algorithm used to sign the JWT
  * - **typ**
    - Media Type of the JWT
  * - **x5c**
    - X.509 Certitifcate Chain containing the Key used to sign the JWT
  * - **kid**
    - Key ID used identifying the Key used to sign the JWT. Required if trust_chain is used
  * - **trust_chain**
    - Sequence of verified Entity Statements that validates a participant's compliance with the Federation


Payload
^^^^^^
.. list-table:: 
  :widths: 25 50
  :header-rows: 1

  * - **Param**
    - **Description**
  * - **presentation_definition**
    - String containing a Presentation Definition JSON object that articulate what proofs a Verifier requires. It will be null if presentation_definition_uri or scope is present
  * - **presentation_definition_uri**
    - A string containing an HTTPS URL pointing to a resource where a Presentation Definition JSON object can be retrieved. It will be null if presentation_definition or scope is present
  * - **scope**
    - Alias for a well-defined Presentation Definition. It will be used to identify PID Presentation Definition request. It will be null if presentation_definition or presentation_definition_uri is present.
  * - **client_id_scheme**
    - String identifying the scheme of the value in the client_id. It will be 'entity_id'
  * - **client_id**
    - Client Identifier
  * - **client_metadata**
    - JSON object containing the Verifier metadata. It will be 'null' since we will use entity_id client_id_scheme. Client metadata will be present in the trust_chain Statements
  * - **client_metadata_uri**
    - String containing an HTTPS URL pointing to a resource where a JSON object with the Verifier metadata can be retrieved
  * - **response_mode**
    - Used to ask the Wallet in which way it has to send the response. It will be 'direct_post.jwt'
  * - **response_type**
    - Used to ask the Wallet what it has to provide in AuthorizationResponse. We will be 'vp_token'
  * - **response_uri**
    - The Response URI to which the Wallet must send the Authorization Response using an HTTPS POST
  * - **redirect_uri**
    - The Redirect URI to which the Wallet must redirect the Authorization Response. if will be 'null' since response_uri is present
  * - **nonce**
    - Fresh cryptographically random number with sufficient entropy used for Security Reason
  * - **state**
    - Unique identifier of the AuthorizationRequest
  * - **iss**
    - The entity that issued the JWT. It will be populated with the Verifier URI
  * - **aud**
    - The audience of the JWT. It will be equal to iss value
  * - **iat**
    - The timestamp when the JWT was issued
  * - **exp**
    - The timestamp when the JWT is set to expire