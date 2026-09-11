.. include:: ../common/common_definitions.rst
.. Included via credential-issuance.rst at title level '=' (document title).


Credential Issuance Low-Level Flows
====================================

Low-Level Issuance Flow
-----------------------

The Credential Issuance flow is based on [`OpenID4VCI`_] and the following main reference standards/specifications MUST be supported on top of `OpenID4VCI`_:

  * **The OAuth 2.0 Authorization Framework** [:rfc:`6749`], as recommended in Section 3 of [`OpenID4VCI`_].
  * **Pushed Authorization Requests** (PAR) [:rfc:`9126`], as recommended in Section 5 of [`OpenID4VCI`_].
  * **Proof Key for Code Exchange** (PKCE) [:rfc:`7636`], as recommended in Section 5 of [`OpenID4VCI`_].
  * **JWT Authorization Requests** (JAR) [:rfc:`9101`].
  * **Rich Authorization Requests** (RAR) [:rfc:`9396`].
  * **OAuth 2.0 Attestation-Based Client Authentication** [`OAUTH-ATTESTATION-CLIENT-AUTH`_].
  * **OpenID Federation 1.0** [`OID-FED`_].

The Credential Issuer MUST use *OAuth 2.0 Authorization Server* based on :rfc:`6749` to authorize the User to obtain a Credential. Credential Issuers MUST support:

  * **Authorization Code Flow**: The Credential Issuer requires User authentication and consent at the Authorization Endpoint before collecting User information to create and provide a Credential.
  * **Wallet Initiated Flow**: The request from the Wallet Instance is sent to the Credential Issuer without any input from the Credential Issuer or a third party (i.e. via Credential Offer support).
  * **Immediate Issuance Flow**: The Credential Issuer issues the Credential directly in response to the Credential Request.

In addition, the Credential Issuers MAY support:

  * **Third-Party Initiated Flow**: The Wallet Instance sends its request to the Credential Issuer based on the input provided by the Credential Issuer or a third party (for example an Authentic Source) supporting Credential Offer mechanism as defined in [`OpenID4VCI`_].

    * **Same-device Issuance Flow**: The User receives the Credential on the same device used to initiate the flow.
    * **Cross-device Issuance Flow**: The User receives the Credential on another device than the one that initiated the flow.

  * **Refresh Token Flow**: The Wallet Instance requests a new Access Token at the Token Endpoint of the PID/(Q)EEA Provider.
  * **Re-issuance Flow**: Following updates to an already stored Digital Credential, the Wallet Instance requests a refresh of the Digital Credential at the Credential Endpoint of the Credential Issuer.
  * **Deferred Issuance Flow**: The Credential Issuer may require time to issue the requested Digital Credential, due to the Authentic Sources data provisioning rules, and allows the Wallet to retrieve the requested Credential in the future.
  * **Batch Credential Issuance Flow**: It enables the issuance of a batch of one or more Digital Credential. Digital Credentials that are issued in a batch MUST share the same format and contain the same set of attributes about the Holder. Each Credential MUST contain different Cryptographic Data to achieve unlinkability between the Digital Credentials.


.. note::
    **Standard or Batch Credential Issuance:**

    The User can configure the Wallet Solution to issue Digital Credentials in either batch or standard mode and define the preferred batch size.

The entire Issuance flow can be divided into two sub-flows:

  - **User Request Flow**, describing the modes through which the User can request the Credential. It can be:

      1. On the initiative of the User (**Wallet Initiated**).

      2. Upon proposal of the Credential Issuer (**Issuer Initiated**).

  - **Issuance Flow**, describing interactions between Wallet Instance and Credential Issuer.

The following diagram shows the *User request flow*.

.. _fig_Low-Level-Flow-ITWallet-PID-QEAA-User-Request:
.. plantuml:: plantuml/credential-user-request-flow.puml
    :width: 99%
    :alt: The figure illustrates the Credential Request Flow by the User.
    :caption: `Credential Request by the User - Detailed flow. <https://www.plantuml.com/plantuml/svg/hLDDJzjC4BxFhnZ1WHSf8F4USq0KQDL8bTAIL5ouhDTZUyHwrzgFcFpxZjUaSGZgXzIB5Utky_4yCxa9KVcOMWCgHMTJMv37gyihW4xEMNEdRCIJxu7y2Qg02Q1mB-F1MS3GogkkSPPEyFGBrqsyDOaEiRVUzJjuuG_l7fKn575XnORLbD_qGBP4KJcKefT8tYg39MrO3tfBhspzIp7QKnsyMZViI_mgHrjXxga874Tn1b0c8bVuqnf7Lf5A_6HS3v3muXhxEIuxiXWRmZSHK7NTapLEYzCaJb0bUML5MqLs5fIEl14-YTaFL6cEheYABMvTydZFDKU1tdag1vGoW-8ekQK0uAqJiDkGnnvF7pylrXzXcGco6yCXegloxxLFGOnFk70HGY8VXbeo4K1_SIqMjBCL-pR30XdIWrVXESO29B4ZRjmpG4cJE40cqD3SfDsZ-YPRzhzisLWdZtLEWRkXFDd_ZYpCyCEkKrn9QPfc-42r9FVR6LBKb-V0VzCjvsvtavTx5mBUvpKRROzqXQSvDh4rsAcQiEVOuBU7ErVIqD-WmxQUDhQiAl8Wi5SpgyRrkU8HbMdsurrfPUK6yvNaJc6Wqwebhz3vznRj_0ytxGnxF1PvCxxz05UY-Mx-e_YDf-etuL-pQyFwEOVFc2B5A1xp0lopFzImrkFdHZwfDJy0>`_


**Steps 1.1-1.4 (Wallet Initiated Flow):** The User, using the Wallet Instance, selects the Credential Issuer from those listed in the list of trustworthy entities.

**Steps 2.1-2.3 (Third Party Initiated Flow):** The User while browsing the Credential Issuer website or a Third Party website supporting the Credential Offer mechanism (for example an Authentic Source) finds a link to obtain a Digital Credential.

**Steps 2.4-2.6 (Cross-Device):** The Credential Offer is presented as a QR Code. The User scans it with the device camera or with the Wallet Instance's built-in scanner, triggering the Wallet Instance to retrieve the parameters defined in the :ref:`Table of Credential Offer parameters <table_credential_offer_claim>` (:ref:`WP_047-048 <wallet-credential-issuance-testcases>`).

**Steps 2.7-2.10 (Same-Device):** The Credential Offer is presented as an href button containing the URL that allows the User to invoke the Wallet Instance using the Credential Offer Endpoint.

The Credential Offer can be sent by value (using the ``credential_offer`` parameter) or by reference (using the ``credential_offer_uri`` parameter) as defined in Section 4 of [`OpenID4VCI`_]. Additional details and non-normative examples are provided in Section :ref:`credential-issuance-low-level:Credential Offer Flow`.


The following diagram shows the *Issuance flow*.

.. _fig_Low-Level-Flow-ITWallet-PID-QEAA-Issuance:
.. plantuml:: plantuml/credential-issuance-flow.puml
    :width: 99%
    :alt: The figure illustrates the Credential Issuance Low-Level Flow.
    :caption: `Credential Issuance - Detailed flow. <https://www.plantuml.com/plantuml/svg/nLPVRzis47_NfpYq3xC0kTswFHN8KCVn6cEPwoNkyZB0eEMpJKGcDVwnctxw7K-MoJXAksm55WIMnFl_k-EFV6UTCCvlgqnufvNVBj1aMKrhifIrK0vUVBHeNe2muBDieJyr2zzPi5lIgZTQuGjuUINN6tTUUNneUsxq_cWk7ifkHLMXWx6Y55I9hBFFK2s1efpaC3IuHEMag61ihJzub1dz6QKTWjwXWNqXAPFn-ylP--lHQ98DDrZUmIDRa1Q2Tz0hS1k4NqXkX9DQWQ3eUk64L22TXIqwiHHEXAmu3iNRG_zdsCDRA0qAXp3zTJY2KYyHA0MvacZOo-sWFzNJWxeazUdW6gxnBu_MGUzF1L1M4fMRosKHlamZoY5yxANRm8U1Tvl-aBNw0-T86fDyIXY2WbHSroKAAYm5g0kUGnkcHk_ayelW70oiN2lXlC5MvQIHS98h8xaJbLnATmyfb1BwZ6KBZgsriWYz0nPpRsG1-AcM1krSgZoWpoPUl8K0W3RoCyU9o4PK8N6JPrwmfNosOIOgbyxGsHbCnnSFK2qylBoz7Cz6cRUX_HGWA9SSeMdcKEBu0gxq02vffq3lwiUSiIb3nOh2wpee4vBtj4PubawgDNZUQa7BYTBPFAA7bSMJjCQpVjkARvAVDX0MR_p2Ej546NIO_dOzku0_UFQRvNzJ67onijxl-MWmo9zR5FKf597YyXz1LyjsQhs0qr6A0npee82m1-WXhJsEt_vPHf5hrgZGa00kmlw-m_idPRNHUfKm4AoqwQ10f-zG0TLJQwbSbl3KZ2HnMp2EYMDchhKHoitTVOrCNPHuV9ctBCWh55SQB7ahCRLzKsRB96CGapvYASeIhPrpbM4_hmpQJVl9ZoRzb5qI32PQbNZ4u78scyBqmyqCNgiWIEAoOjh3EMiqJ7LoK4GKktkIhepQnZ3xtD1KLdXg8JWLWDC3gGb1_xMs5gqbx69Yu2qv8n2JKG8u5Xv3T4n02YgtAfsBycWvb_p29w4sa0XAhLPoxPlZX9cMZItq-Fb3dcVDxZyNhjnyhTuu-1FW_gO6L1UvdPoTBOAhkPMVCU-s_OTunIZiEWMDi_sVeJjylobUlNfLyEiapo5ZnZezmQG5iHEo4eiA8NlwVZ2ZefiR8Q6JEB310vL8hfm65xKoKYDqsjJgvagnXCLzrpqXqchSJp58kgbYv0B8u7ZG40wH95FZvBv1O3EdUWjbkBuSz3tf2tl7Ep7SPzip8VC7R-r2AD4wRJ1r7uDsoYADn5oxsIIHzqugAm1tgFX2c0pIW0UfuRlErfrVVHnbrxYMrj4g8SxGHmZx1YlXS0cPL5JybiCn3Bla27zjSASFYK5NezBIOgkujZVV_qHY66hb0g2FpdDfOV9X5aVmAzsNvCPGEmjmHYWhohRpQVM-aDdiyOWL85OCWmAnrLurjrgvHR0rbbH0Cvnj21wM_GOLXPBhDPeuks56-70splB2gj9x46iXrSFhmJlwyTlgRm00>`_


.. .. figure:: ../../images/Low-Level-Flow-ITWallet-PID-QEAA-Issuance.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/hLPVRo8t47_tfnZb7XeaKAgsJoTTTOJG2sgKq9HJNYeXnpl0A8kzjSTmwQUlFLdmGaYhg9MYxAxd_-ytC-PpOEqvhckb8piRru_ebMhI6Hbgj6Ku-nhGdu4E49LwTDzU3huB4DP9gravYsVmuOQMAxwi8nxQNdgttPlhGzc3hcjacDZ0sXeKdQr2Mq6ASfJ3o6E5badNC0aXjXv9AMyT8xWDUjZsAUKn-N8z-t8_7j-gqGhD4xoo10gGVODR0AyGVabohvcS1PrYkqVMP84um1fPLvfrpadYABM5mS-mXOzWF6f6cFuw6eDn5KBAW1Q4Nfmy30TJDstLAQbFX_TmZtz630pdVrW0KnDQdbFLpr_-HTI3_B4bNi7TCF9gC1AjmP0vIKkERmbpK20hPLsZJdLryJc5Jil1rBiDLV-8JMiGQ6arHu-joix3KOg2tqRNL14_GmT0HJ0G27UOXCRPW73UGZ2Fdlg0tnho6EPaUqfGJ2PHVuHSj_FqbyGfW1OmeUEcfw8MItgteT8rTpldqoUOJguEmEn7-F1mFPcDLGoPzHGWAvkN2CBXY71o1JTk2DTfEk3yviUUO6DonJQ5TqrMJW0-fxC4es6oIuWoNbcBjU7GA-XX7V0ehVFVUkFXiFVUr58r_p4LM-suZ1gE0IwqvjdeG-wCzA0GzgHitsLK1c-95dqIm5LkzYTyVbFMUESMdN64XVCdrW6x9xIGwcaSMLQTePqbIMaMmQtZMCPuwRNbEJytA7ES4YylyzrAQ4Uy8ez66apc_7yTSqM2GKbwZwKs1aEOIvMvonSUmshtAGz9_t3c2WQtpXhSOt0zcqrXUlVx32vi5fIuEyN2uLmqUgzsPWjV-cjS21W2ENkeVgHVC7-3GRC_AJIM2eh-2Igxw0ZcNOABtpd9Y-ntrmquDyukQ1cz42EBH8nVhn0Ae3UQQlrO8wW2N5Ude5SYX3vObqERNOWkf6cEBrvMGDcsgGoPdHZ0v9tTgiUahiEJO9XlyDtigzWwsnq0EmZiF4g3bKnAM14VYKh3b6HFzarNVdvKMXzmWrRkmGv9Go7ffRFLgHljykRhMDtZaWAdKrtNHvaFFDQQiG95DfM_bd02HFAoZt_XSUFQnCgLLPWwAArm9RNzyFrFIGmZPpb3MZPrOV_sRbOwu5_ehr5NSwOrze6zja6R7VVTycEVr2mLUlH3gWzw8JXOq6iNhTpcsHc41arkuWeUds4VGnfckq8Bx6cvH2_o3A7qYInYpq4E5hNRWbvgieTNmUVqBwxhlm40

..     PID/(Q)EAA Issuance - Detailed flow


Once *User Request flow* is completed, the Wallet Instance processes the Metadata of the Credential Issuer as defined in Section :ref:`trust-evaluation:Trust Evaluation Process`. Additionally, in the case of Batch Credential issuance, the Wallet Instance MUST check the support of batch issuance by looking for the ``batch_credential_issuance`` object in the Credential Issuer metadata, from where the Wallet Instance can get the ``batch_size`` value.

.. note::
  **Federation Check:** The Wallet Instance must verify whether the Credential Issuer is a member of the Federation, obtaining its protocol specific Metadata (:ref:`WP_046 <wallet-credential-issuance-testcases>`). A non-normative example of a response from the endpoint **.well-known/openid-federation** with the **Entity Configuration** and the **Metadata** of the Credential Issuer is represented within the section :ref:`credential-issuer-entity-configuration:Credential Issuer Entity Configuration`.

In case of Issuer Initiated flow, in addition to the Federation Check defined above, the Wallet Instance MUST execute the following checks on the Credential Offer parameters:

  * For each Credential identifier contained in the ``credential_configuration_ids`` array verify if it is supported by the Credential Issuer (:ref:`WP_050 <wallet-credential-issuance-testcases>`).
  * The Authorization Server identifier (if present) is contained in the ``authorization_servers`` Credential Issuer metadata parameter (:ref:`WP_049 <wallet-credential-issuance-testcases>`).


**Steps 1-2 (PAR Request)**: The Wallet Instance:

  * Creates a fresh PKCE code verifier, Wallet Instance Attestation Proof of Possession, and ``state`` parameter for the *Pushed Authorization Request* (:ref:`WP_052 <wallet-credential-issuance-testcases>`).
  * Provides to the Credential Issuer PAR endpoint the parameters previously listed above, using the ``request`` parameter (hereafter Request Object) according to :rfc:`9126` Section 3 to prevent Request URI swapping attack (:ref:`WP_052 <wallet-credential-issuance-testcases>`). The Pushed Authorization Request enables client authentication prior to any User interaction. This step allows for the early rejection of illegitimate requests, effectively preventing spoofing attacks, tampering, and improper use of authorization requests.
  * MUST create the ``code_verifier`` with enough entropy random string using the unreserved characters with a minimum length of 43 characters and a maximum length of 128 characters, making it impractical for an attacker to guess its value. The value MUST be generated following the recommendation in Section 4.1 of :rfc:`7636`  (:ref:`WP_052a <wallet-credential-issuance-testcases>`).
  * Signs this request using the private key that is created during the setup phase to obtain the Wallet Instance Attestation. The related public key that is attested by the Wallet Provider is provided within the Wallet Instance Attestation ``cnf.jwk`` claim  (:ref:`WP_052c <wallet-credential-issuance-testcases>`).
  * MUST use the ``OAuth-Client-Attestation`` and ``OAuth-Client-Attestation-PoP`` parameters according to OAuth 2.0 Attestation-based Client Authentication [`OAUTH-ATTESTATION-CLIENT-AUTH`_], since in this flow the Pushed Authorization Endpoint is a protected endpoint  (:ref:`WP_052b <wallet-credential-issuance-testcases>`).
  * Specifies the types of the requested credentials using the ``authorization_details`` [RAR :rfc:`9396`] parameter and or ``scope`` parameter (:ref:`WP_052d <wallet-credential-issuance-testcases>`).

.. note::
  This specification uses JAR [:rfc:`9101`] to ensure end-to-end integrity of authorization requests for all Request Object parameters.
  When interacting with cross-border Credential Issuers whose Authorization Servers may not support JAR, Wallet Instances SHOULD check the ``require_signed_request_object`` parameter in the Authorization Server metadata to determine whether to sign the Request Object.
  Wallet Solutions supporting both JAR-compliant and non-compliant Authorization Servers may duplicate parameters in both the request body and the signed Request Object. Section 10.7 of :rfc:`9101` provides the security requirements on how to manage this duplication properly.

.. note::
   For eID Substantial Authentication with MRTD Verification, the ``authorization_details`` object MUST contain the type ``"it_l2+document_proof"``. For complete protocol specifications, see :ref:`credential-issuance-l2plus:eID Substantial Authentication with MRTD Verification for IT-Wallet ID Issuance`.

The Credential Issuer performs the following checks upon the receipt of the PAR request:

    1. It MUST validate the signature of the Request Object using the algorithm specified in the ``alg`` header parameter (:rfc:`9126`, :rfc:`9101`) and the public key retrieved from the Wallet Instance Attestation (``cnf.jwk``) referenced in the Request Object, using the ``kid`` JWT header parameter.
    2. It MUST check that the used algorithm for signing the request in the ``alg`` header is one of the listed within the Section :ref:`algorithms:Cryptographic Algorithms`.
    3. It MUST check that the ``client_id`` in the request body of the PAR request matches the ``client_id`` claim included in the Request Object.
    4. It MUST check that the ``iss`` claim in the Request Object matches the ``client_id`` claim in the Request Object (:rfc:`9126`, :rfc:`9101`).
    5. It MUST check that the ``aud`` claim in the Request Object is equal to the identifier of the Credential Issuer (:rfc:`9126`, :rfc:`9101`).
    6. It MUST reject the PAR request, if it contains the ``request_uri`` parameter (:rfc:`9126`).
    7. It MUST check that the Request Object contains all the mandatory parameters which values are validated according to :ref:`Table of the HTTP parameters <table_request_object_claim>` [derived from :rfc:`9126`].
    8. It MUST check that the Request Object is not expired, checking the ``exp`` claim.
    9. It MUST check that the Request Object was issued in a previous time than the value exposed in the ``iat`` claim. It SHOULD reject the request if the ``iat`` claim is far from the current time (:rfc:`9126`) of more than `5` minutes.
    10. It MUST check that the ``jti`` claim in the Request Object has not been used before by the Wallet Instance identified by the ``client_id``. This allows the Credential Issuer to mitigate replay attacks (:rfc:`7519`).
    11. It MUST validate the ``OAuth-Client-Attestation-PoP`` parameter based on Section 5 of [`OAUTH-ATTESTATION-CLIENT-AUTH`_].
    12. It MUST verify, if present, the validity of the ``issuer_state`` and the coherence with the ``credential_configuration_id`` requested in the Request Object.


Below is a non-normative example of the PAR Request.

.. code-block:: http

    POST /as/par HTTP/1.1
    Host: eaa-provider.example.org
    Content-Type: application/x-www-form-urlencoded
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtpZCI6IjBiNDk4ZGRlMDkxNzJhZGE3MDFkMDdlYjZmOTg2N2FkIiwidHlwIjoib2F1dGgtY2xpZW50LWF0dGVzdGF0aW9uK2p3dCIsIng1YyI6WyJNSUlEcWpDQ0FwS2dBd0lCQWdJRVNMTkV2REEgLi4uIiwiTUlJQ3d6Q0NBYXNDQ1FDS1Z5OWVLanZpK2pBIC4uLiIsIk1JSURURENDQWpTZ0F3SUJBZ0lKQVBsblFZSC4uLiJdfQ.eyJzdWIiOiJodHRwczovL3dhbGxldC1zb2x1dGlvbi5leGFtcGxlLm9yZy9kZDc2MmU2ZjhiNjEzMTkzIiwiY25mIjp7Imp3ayI6eyJjcnYiOiJQLTI1NiIsImt0eSI6IkVDIiwieCI6IjRITnB0SS14cjJwanlSSktHTW56NFdtZG5RRF91SlNxNFI5NU5qOThiNDQiLCJ5IjoiTElablNCMzl2RkpoWWdTM2s3alhFNHIzLUNvR0ZRd1p0UEJJUnFwTmxyZyJ9fSwid2FsbGV0X25hbWUiOiJXYWxsZXRfdjEiLCJ3YWxsZXRfbGluayI6Imh0dHBzOi8vZXhhbXBsZS5jb20vd2FsbGV0L2RldGFpbF9pbmZvLmh0bWwiLCJ3YWxsZXRfdmVyc2lvbiI6IjEuMC4wIiwiY2xpZW50X3N0YXR1cyI6eyJzdGF0dXMiOnsic3RhdHVzX2xpc3QiOnsiaWR4IjoxMzM3LCJ1cmkiOiJodHRwczovL3Jldm9jYXRpb25fdXJsL3dpYS1zdGF0dXNsaXN0cy80MiJ9fSwiZXhwIjoxMzAzNDk3NzgwfSwiZXhwIjoxNzQwMTU4MTY3fQ.XOv01xkHC-_h-bZFcXgkEffs3xk8WezKWs8KA4yZD8aNabDq81Y80wkOuHCM25zSGHbABszaSDsyYaJv9bh40w
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUzI1NiIsInR5cCI6Im9hdXRoLWNsaWVudC1hdHRlc3RhdGlvbi1wb3Arand0In0.ew0KICAiaXNzIjogIiA0N2I5ODIzNjk3OTFkMDgwMDNhNzI4M2YwNTljYjBkMSIsDQogICJhdWQiOiAiaHR0cHM6Ly9hcy5leGFtcGxlLmNvbSIsDQogICJqdGkiOiAiZDI1ZDAwYWItNTUyYi00NmZjLWFlMTktOThmNDQwZjI1MDY0IiwNCiAgImlhdCI6IDE3NDAxNTg2MTcNCn0.B0KOkGi9vMxf3H2Y8rrF-mdLNsuluTvAUbjFfL1Hi-gdaPW7-8ziS9uVh7aTnSAHKWzMfkZLv5q-bxhkglR4PA

    client_id=$thumbprint-of-the-jwk-in-the-cnf-wallet-instance-attestation$&
    request=$SIGNED-JWT

Below is a non-normative example of the Wallet Instance Attestation Proof of Possession (WIA-PoP) header and body:

.. literalinclude:: ../../examples/wa-pop-header.json
  :language: JSON

.. literalinclude:: ../../examples/wa-pop-payload.json
  :language: JSON


Below is a non-normative example of the signed Request Object without encoding and signature applied:

.. literalinclude:: ../../examples/request-object-header.json
  :language: JSON

.. literalinclude:: ../../examples/request-object-payload.json
  :language: JSON


.. note::
  **Federation Check**: The Credential Issuer MUST check that the Wallet Provider is part of the federation.


.. note::
  The Credential Issuer MUST validate the signature of the Wallet Instance Attestation and that it is not expired.

**Step 3 (PAR Response)**: The Credential Issuer provides a one-time use ``request_uri`` value. The issued ``request_uri`` value MUST be bound to the client identifier (``client_id``) that was provided in the Request Object.


.. note::
  The entropy of the ``request_uri`` MUST be sufficiently large. The adequate shortness of the validity and the entropy of the ``request_uri`` depends on the risk calculation based on the value of the resource being protected. The validity time SHOULD be less than a minute, and the ``request_uri`` MUST include a cryptographic random value of 128 bits or more (:rfc:`9101`). The entire ``request_uri`` SHOULD NOT exceed 512 ASCII characters due to the following two main reasons (:rfc:`9101`):

    1. Many phones on the market still do not accept large payloads. The restriction is typically either 512 or 1024 ASCII characters.
    2. On a slow connection such as a 2G mobile connection, a large URL would cause a slow response; therefore, the use of such is not advisable from the user-experience point of view.

The Credential Issuer returns the issued ``request_uri`` to the Wallet Instance. A non-normative example of the response is shown below.

.. code-block:: http

  HTTP/1.1 201 Created
  Cache-Control: no-cache, no-store
  Content-Type: application/json

.. literalinclude:: ../../examples/par-response.json
  :language: JSON

**Steps 4-5 (Authorization Request)**: The Wallet Instance sends an authorization request to the Credential Issuer Authorization Endpoint (:ref:`WP_053 <wallet-credential-issuance-testcases>`). Since parts of this Authorization Request content, e.g., the ``code_challenge`` parameter value, are unique to a particular Authorization Request, the Wallet Instance MUST use a ``request_uri`` value once (:rfc:`9126`) as per :ref:`WP_053a <wallet-credential-issuance-testcases>`. The Credential Issuer performs the following checks upon the receipt of the Authorization Request:

    1. It MUST treat ``request_uri`` values as one-time use and MUST reject an expired request. However, it MAY allow for duplicate requests due to a User reloading/refreshing their user-agent (derived from :rfc:`9126`).
    2. It MUST identify the request as a result of the submitted PAR (derived from :rfc:`9126`).
    3. It MUST reject all the Authorization Requests that do not contain the ``request_uri`` parameter as the PAR is the only way to pass the Authorization Request from the Wallet Instance (derived from :rfc:`9126`).


.. code-block:: http

    GET /authorize?client_id=$thumprint-of-the-jwk-in-the-cnf-wallet-instance-attestation$&request_uri=urn%3Aietf%3Aparams%3Aoauth%3Arequest_uri%3Abwc4JK-ESC0w8acc191e-Y1LTC2 HTTP/1.1
    Host: eaa-provider.example.org


.. note::
   **User Authentication and Consent**: The PID Provider performs the User authentication based on CieID scheme with LoA High (CIE L3), while the EAA Provider of IT-Wallet ID in addition to CieID LoA High supports also the eID Substantial Authentication with MRTD Verification as defined in :ref:`credential-issuance-l2plus:eID Substantial Authentication with MRTD Verification for IT-Wallet ID Issuance`.
   The (Q)EAA Provider performs the User authentication requesting a valid PID or IT-Wallet ID to the Wallet Instance. The (Q)EAA Provider MUST use [`OpenID4VP`_] to request the presentation of the PID or the IT-Wallet ID. In this circumstance, the (Q)EAA Provider acts as a Relying Party, providing the presentation request to the Wallet Instance. The Wallet Instance MUST have a valid PID or IT-Wallet ID, obtained beforehand. During this step, Credential Issuers MAY ask the User's contact details (e.g., their email address) to send notifications about the issued Digital Credential(s).


**Steps 6-7 (Authorization Response)**: The Credential Issuer sends an authorization ``code`` together with ``state`` and ``iss`` parameters to the Wallet Instance. The Wallet Instance performs the following checks on the Authorization Response:

    1. It MUST check the Authorization Response contains all the defined parameters according to :ref:`Table of the HTTP Response parameters <table_http_response_claim>` (:ref:`WP_054 <wallet-credential-issuance-testcases>`).
    2. It MUST check the returned value by the Credential Issuer for ``state`` parameter is equal to the value sent by Wallet Instance in the Request Object (:rfc:`6749`) as per :ref:`WP_054a <wallet-credential-issuance-testcases>`.
    3. It MUST check that the URL of Credential Issuer in ``iss`` parameter is equal to the URL identifier of intended Credential Issuer that the Wallet Instance starts the communication with (:rfc:`9027`)  as per :ref:`WP_054b <wallet-credential-issuance-testcases>`.

.. note::
    The Wallet Instance redirect URI is a universal or app link registered with the local operating system, so this latter will resolve it and pass the response to the Wallet Instance.

.. code-block:: http

    HTTP/1.1 302 Found
    Location: https://start.wallet.example.org?code=SplxlOBeZQQYbYS6WxSbIA&state=fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd&iss=https%3A%2F%2Feaa-provider.example.org

**Steps 8-9 (DPoP Proof for Token Endpoint)**: The Wallet Instance MUST create a new key pair for the DPoP and a fresh DPoP Proof JWT following the instruction provided in the Section 4 of (:rfc:`9449`) for the token request to the Credential Issuer (:ref:`WP_055b <wallet-credential-issuance-testcases>`). The DPoP Proof JWT is signed using the private key for DPoP created by Wallet Instance for this scope (:ref:`WP_055c <wallet-credential-issuance-testcases>`). DPoP binds the Access Token, and optionally the Refresh Token, to a certain Wallet Instance (:rfc:`9449`) and mitigates the misuse of leaked or stolen tokens at the Credential Endpoint.

**Step 10 (Token Request):** The Wallet Instance sends a token request to the Credential Issuer Token Endpoint with a *DPoP Proof JWT* and the parameters: ``code``, ``code_verifier``, and OAuth 2.0 Attestation based Client Authentication (``OAuth-Client-Attestation`` and ``OAuth-Client-Attestation-PoP``) as per :ref:`WP_055 <wallet-credential-issuance-testcases>`.

The ``OAuth-Client-Attestation`` is signed using the private key bound to the Wallet Instance (:ref:`WP_055a <wallet-credential-issuance-testcases>`). The related public key that is attested by the Wallet Provider is provided within the Wallet Instance Attestation (``cnf.jwk`` claim) as per :ref:`WP_055d <wallet-credential-issuance-testcases>`. The Credential Issuer performs the following checks on the Token Request:

   1. It MUST ensure that the Authorization ``code`` is issued to the authenticated Wallet Instance (:rfc:`6749`) and was not replied.
   2. It MUST ensure the Authorization ``code`` is valid and has not been previously used (:rfc:`6749`).
   3. It MUST ensure the ``redirect_uri`` matches the value included in the previous Request Object (see Section 3.1.3.1. of [`OIDC`_]).
   4. It MUST validate the DPoP Proof JWT, according to (:rfc:`9449`) Section 4.3.
   5. It MUST verify the ``code_verifier`` parameter according to the PKCE mechanism, ensuring it matches the ``code_challenge`` associated with the authorization code as defined in Section 4.6 of :rfc:`7636`; otherwise, the request MUST be rejected (:ref:`CI_061a <test-plans-credential-issuer:Credential Issuer Test Matrix>`).

.. code-block:: http

    POST /token HTTP/1.1
    Host: eaa-provider.example.org
    Content-Type: application/x-www-form-urlencoded
    DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6IkVDIiwieCI6IjR2dDhNdEFISmlsMzBDNnpUTmt2c0VVcnlHTEUtQW5BNkc5LV8xa3l5Rk0iLCJ5IjoiTWdiNTFfbjNSRjNtbHNtS3dMd0xtRUFqVmlJM3Q1bTVWNTI2MFA5MzR3RSIsImNydiI6IlAtMjU2In19.eyJqdGkiOiItQndDM0VTYzZhY2MybFRjIiwiaHRtIjoiR0VUIiwiaHR1IjoiaHR0cHM6Ly9yZXNvdXJjZS5leGFtcGxlLm9yZy9wcm90ZWN0ZWRyZXNvdXJjZSIsImlhdCI6MTU2MjI2MjYxOH0.3Tp1ZlZ05PQYeZUHhiZwaQ1etqnwYwoiJHFR_JHb32381lMJL-8o2rE3VZ8X3yuqrGFfCVeP90Ln4J5r8ASIBg
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtpZCI6IjBiNDk4ZGRlMDkxNzJhZGE3MDFkMDdlYjZmOTg2N2FkIiwidHlwIjoib2F1dGgtY2xpZW50LWF0dGVzdGF0aW9uK2p3dCIsIng1YyI6WyJNSUlEcWpDQ0FwS2dBd0lCQWdJRVNMTkV2REEgLi4uIiwiTUlJQ3d6Q0NBYXNDQ1FDS1Z5OWVLanZpK2pBIC4uLiIsIk1JSURURENDQWpTZ0F3SUJBZ0lKQVBsblFZSC4uLiJdfQ.eyJzdWIiOiJodHRwczovL3dhbGxldC1zb2x1dGlvbi5leGFtcGxlLm9yZy9kZDc2MmU2ZjhiNjEzMTkzIiwiY25mIjp7Imp3ayI6eyJjcnYiOiJQLTI1NiIsImt0eSI6IkVDIiwieCI6IjRITnB0SS14cjJwanlSSktHTW56NFdtZG5RRF91SlNxNFI5NU5qOThiNDQiLCJ5IjoiTElablNCMzl2RkpoWWdTM2s3alhFNHIzLUNvR0ZRd1p0UEJJUnFwTmxyZyJ9fSwid2FsbGV0X25hbWUiOiJXYWxsZXRfdjEiLCJ3YWxsZXRfbGluayI6Imh0dHBzOi8vZXhhbXBsZS5jb20vd2FsbGV0L2RldGFpbF9pbmZvLmh0bWwiLCJ3YWxsZXRfdmVyc2lvbiI6IjEuMC4wIiwiY2xpZW50X3N0YXR1cyI6eyJzdGF0dXMiOnsic3RhdHVzX2xpc3QiOnsiaWR4IjoxMzM3LCJ1cmkiOiJodHRwczovL3Jldm9jYXRpb25fdXJsL3dpYS1zdGF0dXNsaXN0cy80MiJ9fSwiZXhwIjoxMzAzNDk3NzgwfSwiZXhwIjoxNzQwMTU4MTY3fQ.XOv01xkHC-_h-bZFcXgkEffs3xk8WezKWs8KA4yZD8aNabDq81Y80wkOuHCM25zSGHbABszaSDsyYaJv9bh40w
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUzI1NiIsInR5cCI6Im9hdXRoLWNsaWVudC1hdHRlc3RhdGlvbi1wb3Arand0In0.ew0KICAiaXNzIjogIiA0N2I5ODIzNjk3OTFkMDgwMDNhNzI4M2YwNTljYjBkMSIsDQogICJhdWQiOiAiaHR0cHM6Ly9hcy5leGFtcGxlLmNvbSIsDQogICJqdGkiOiAiZDI1ZDAwYWItNTUyYi00NmZjLWFlMTktOThmNDQwZjI1MDY0IiwNCiAgImlhdCI6IDE3NDAxNTg2MTcNCn0.B0KOkGi9vMxf3H2Y8rrF-mdLNsuluTvAUbjFfL1Hi-gdaPW7-8ziS9uVh7aTnSAHKWzMfkZLv5q-bxhkglR4PA

    grant_type=authorization_code
    &code=SplxlOBeZQQYbYS6WxSbIA
    &code_verifier=dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk
    &redirect_uri=https://start.wallet.example.org/cb

**Step 11 (Token Response)**: The Credential Issuer validates the request. If successful, the Issuer provides the Wallet Instance with an Access Token and, optionally, a Refresh Token, both bound to the DPoP key.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store

.. literalinclude:: ../../examples/token-response.json
  :language: JSON

A non-normative example of the DPoP Access Token is given below.

.. literalinclude:: ../../examples/at-dpop-header.json
  :language: JSON

.. literalinclude:: ../../examples/at-dpop-payload.json
  :language: JSON

A non-normative example of the DPoP Refresh Token is given below.

.. literalinclude:: ../../examples/rt-dpop-header.json
  :language: JSON

.. literalinclude:: ../../examples/rt-dpop-payload.json
  :language: JSON

**Step 12 (Nonce Request)**: According to Section 7.1 of [`OpenID4VCI`_], the Wallet Instance sends an HTTP POST request to the Nonce Endpoint to obtain a fresh ``c_nonce`` that can be used to create the proof of possession of key material for the subsequent request to the Credential Endpoint (:ref:`WP_056a <wallet-credential-issuance-testcases>`).

Below is a non-normative example of a Nonce Request:

.. code-block:: http

    POST /nonce HTTP/1.1
    Host: eaa-provider.example.org
    Content-Length: 0

**Step 13 (Nonce Response)**: The Credential Issuer provides the ``c_nonce`` to the Wallet Instance. The parameter ``c_nonce`` is a string value, which MUST be unpredictable and is used later by the Wallet Instance in Step 16 to create the proof(s) of possession of the key (``proofs`` claim) and it is the primary countermeasure against key proof replay attack.
Note that, the received ``c_nonce`` value can be used to create the proof(s) as long as the Issuer
provides the Wallet Instance with a new ``c_nonce`` value.

Below is a non-normative example of a Nonce Response:

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store

.. literalinclude:: ../../examples/nonce-response.json
  :language: JSON


**Step 14 (DPoP Proof for Credential Endpoint)**: The Wallet Instance creates a DPoP Proof JWT using the same key in **Step 8** and according to (:rfc:`9449`) Section 4 (:ref:`WP_056b <wallet-credential-issuance-testcases>`).

.. note::
   If the Wallet Instance requests a batch issuance of Digital Credentials, the flow continues with **Step 17**. Otherwise Steps **15-16** are performed.

**Step 15 (Proof of Possession of Credential)**: The Wallet Instance for requesting the Digital Credential creates a proof of possession with ``c_nonce`` obtained in **Step 13** using the private key used for the DPoP. The ``jwk`` value in the proof parameter MUST be equal to the public key referenced in the DPoP (:ref:`WP_056c <wallet-credential-issuance-testcases>`).

**Step 16 (Credential Request)**: The Wallet Instance sends a request for the Digital Credential to the Credential endpoint. This request MUST include the Access Token, DPoP Proof JWT, Credential type, proof (which demonstrates possession of the key) as per :ref:`WP_056 <wallet-credential-issuance-testcases>`. The ``proofs`` parameter MUST be an object that contains evidence of possession of the cryptographic key material to which the issued Digital Credential will be bound. To verify the proof, the Credential Issuer conducts the following checks at the Credential endpoint:

 1. The JWT proof MUST include all required claims as specified in the table of Section :ref:`credential-issuance-endpoint:Token Request`.
 2. The key proof MUST be explicitly typed using header parameters as defined for the respective proof type.
 3. The header parameter ``alg`` MUST indicate a registered asymmetric digital signature algorithm, and MUST NOT be set to `none`.
 4. The signature on the key proof MUST be verified using the public key specified in the header parameter.
 5. The header parameter MUST NOT contain a private key.
 6. The signature on the Key Attestation JWT as the value of the ``key_attestation`` header parameter MUST be verified using the Wallet Provider's public key which is identified by the ``kid`` header parameter inside the Key Attestation JWT.
 7. If a ``c_nonce`` value was previously provided by the server, the ``nonce`` claim in the JWT MUST match this ``c_nonce`` value. Furthermore, the creation time of the JWT, as indicated by the ``iat`` claim or a server-managed timestamp via the ``nonce`` claim, MUST be within an acceptable window of time as determined by the server.


.. note::
  The Credential Issuer MUST register all the issued Credentials for their later revocation, if needed.


.. note::
  It is RECOMMENDED that the public key contained in the ``jwt_proof`` be specifically generated for the requested Credential (fresh cryptographic key) to ensure that different issued Credentials do not share the same public key, thereby remaining unlinkable to each other.


A non-normative example of the Credential Request is provided below.


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

.. literalinclude:: ../../examples/credential-request.json
  :language: JSON

Where a non-normative example of the decoded content of the ``jwt`` parameter is represented below, without encoding and signature.

.. literalinclude:: ../../examples/credential-jwt-proof-header.json
  :language: JSON

.. literalinclude:: ../../examples/credential-jwt-proof-payload.json
  :language: JSON

**Step 17 (Fresh Digital Credential Keys Generation)**: The Wallet Instance generates N fresh Credential key pairs, where the number of key pairs (N) is determined by the value defined in the ``batch_size`` (:ref:`WP_058a <wallet-credential-issuance-testcases>`).

**Step 18 (Proofs of Possession of Credentials)**: The Wallet Instance MUST generate N key proofs using provided ``c_nonce`` in **Step 13** and one for each Credential in the batch. The number of key proofs (N) is defined by the ``batch_size`` value (:ref:`WP_058b <wallet-credential-issuance-testcases>`).

.. note::
  The ``c_nonce`` value in all the jwt proofs is identical and it is not needed to obtain separate nonce values per proof.


**Step 19 (Batch Credential Request)**: The Wallet Instance sends a request for the batch of Digital Credential to the Credential endpoint. This request MUST include the Access Token, DPoP Proof JWT, Credential type, proofs (which demonstrates possession of the keys). The proofs parameter MUST set using a JSON object containing two or more evidence of possession of the cryptographic key materials to which the issued batch of Digital Credential will be bound. To verify the proofs, the Credential Issuer, in addition to the predefined checks in **Step 16**, must ensure the ``jwk`` attribute in each key proofs is unique (:ref:`WP_058 <wallet-credential-issuance-testcases>`).


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

.. literalinclude:: ../../examples/batch-credential-request.json
  :language: JSON


The decoded content of ``jwt`` elements in the ``jwt`` array is similar to what is explained in **Step 16**.


**Steps 20-24 (Credential Response)**: The Credential Issuer MUST validate the *DPoP JWT Proof* based on the steps defined in Section 4.3 of (:rfc:`9449`) and whether the *Access Token* is valid and suitable for the requested Credential. The Credential Issuer MUST validate all the key proofs that are provided within ``proofs`` (**Step 15** and **Step 18**) parameter that the new Credentials MUST be bound to, according to `OpenID4VCI`_ Appendix F1. If all checks succeed, the Credential Issuer returns the issued Credential inside the ``credentials`` parameter. The number of elements in the Credentials array matches the number of the keys that the Wallet Instance has provided either via the ``proofs`` parameter (**Step 16** and **Step 19**). The Wallet Instance MUST perform the following checks before proceeding with the secure storage of the Credential(s):

    1. It MUST check that the PID/(Q)EAA contained in the Credential Response contains all the mandatory parameters and values are validated according to :ref:`Table of the Credential response parameters <table_credential_response_claim>` (:ref:`WP_059 <wallet-credential-issuance-testcases>`).
    2. It MUST check the Credential integrity by verifying the signature using the algorithm specified in the ``alg`` header parameter of SD-JWT (:ref:`credential-data-model:Digital Credential Data Model`) and the public key that is identified using the ``kid`` header of the SD-JWT (:ref:`WP_062a <wallet-credential-issuance-testcases>`).
    3. It MUST check that the received Digital Credential(s) (in the ``credential`` claim) matches the requested Credential type and complies with the specific schema of that Credential defined in :ref:`credential-data-model:Digital Credential Data Model` (:ref:`WP_060 <wallet-credential-issuance-testcases>`).
    4. It MUST process and verify the Credential in SD-JWT VC format (according to `SD-JWT`_ Section 4.) or mdoc-CBOR format (:ref:`WP_062 <wallet-credential-issuance-testcases>`).
    5. It MUST verify the Trust Chain in the header of SD-JWT VC to verify that the Credential Issuer is trusted (:ref:`WP_061 <wallet-credential-issuance-testcases>`).

If the checks above are successful, the Wallet Instance requests the User's consent to store the Digital Credential(s). Upon receiving consent, the Wallet Instance securely stores the Digital Credential(s) (:ref:`WP_063 <wallet-credential-issuance-testcases>`).

Below is a non-normative example of a successful response containing a Credential in SD-JWT VC format.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store
    Pragma: no-cache

.. literalinclude:: ../../examples/sd-jwt-credential-response.json
  :language: JSON


Below is a non-normative example of a successful response containing a Credential in mdoc format.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store
    Pragma: no-cache

.. literalinclude:: ../../examples/mdoc-credential-response.json
  :language: JSON


Below is a non-normative example of a successful response containing a batch of Credentials in SD-JWT VC format:

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store
    Pragma: no-cache

.. literalinclude:: ../../examples/sd-jwt-batch-credential-response.json
  :language: JSON


.. note::
  When the Wallet Instance receives a new batch of the same Credential with the same claims, the Wallet MUST delete previous Credentials (:ref:`WP_073a <wallet-credential-issuance-testcases>`).


.. note::
  If the requested Credential cannot be issued immediately and requires more time, the Credential Issuer SHOULD support the Deferred Flow (step 27) as specified in Section :ref:`credential-issuance-endpoint:Deferred Endpoint` (:ref:`WP_065–067 <wallet-credential-issuance-testcases>`). Additionally, in the case of batch issuance, the same ``transaction_id`` retrieves all Credentials that are requested in the batch.


**Step 25 (Notification Request)**: According to Section 11.1 of [`OpenID4VCI`_], the Wallet sends an HTTP POST request to the Notification Endpoint using the *application/json* media type as in the following non-normative example (:ref:`WP_064 <wallet-credential-issuance-testcases>`).

.. code-block:: http

  POST /notification HTTP/1.1
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
.. literalinclude:: ../../examples/notification-request.json
  :language: JSON


**Step 26 (Notification Response)**: When the Credential Issuer has successfully received the Notification Request from the Wallet, it MUST respond with an HTTP status code *204* as recommended in Section 11.2 of [`OpenID4VCI`_]. Below is a non-normative example of response to a successful Notification Request:


.. code-block:: http

  HTTP/1.1 204 No Content

.. note::
   In some cases there are multiple sets of Credential data available in the Authentic Source system, and the User may be interested in obtaining more than one Credential. In these cases the Issuance Flow remains the same as described in :ref:`credential-issuance-low-level:Low-Level Issuance Flow`. In the Token Response (**Step 11**), the Credential Issuer generates a unique identifier (``credential_identifier``) for each Credential Dataset provided in the `AttributeClaims` parameter of the e-service PDND :ref:`authentic-source-endpoint:Get Attribute Claims`. Therefore, the ``credential_identifiers`` array within the ``authorization_details`` object contains the identifiers of all Credentials available for issuance. The Wallet sends a Credential Request (**Step 16**) for each identifier, obtaining multiple distinct Credentials that are individually shown to the User for the acceptance. Finally, the Credential Issuer is notified by the Wallet of the outcome through the :ref:`credential-issuance-endpoint:Notification Endpoint` (:ref:`WP_057 <wallet-credential-issuance-testcases>`).


.. note::
   For batch-issued Digital Credentials, a single ``notification_id`` covers the entire batch-issued Credentials. The notification response (e.g. ``credential_accepted`` or ``credential_stored``) applies to all Credentials, any partial failure is treated as a batch failure.


Refresh Token Flow
------------------

To use the Deferred, Credential Request, and Notification endpoints, the Wallet Instance MUST present a valid DPoP Access Token to the Credential Issuer. However, when these endpoints are used in the Deferred Flow, for re-issuing or notifying the deletion of a Digital Credential, the Access Token might expire, as it is designed to be short-lived and these actions MAY occur days later (:ref:`WP_066b <wallet-credential-issuance-testcases>`). To address this, the specification RECOMMENDS the use of Refresh Tokens.

An Access Token obtained as a result of a Refresh Token flow MUST be limited to:

  - the Deferred endpoint to obtain a new Digital Credential after time set in the parameter ``interval`` or when it is notified as ready to be issued  (:ref:`WP_066 <wallet-credential-issuance-testcases>`);
  - the Notification endpoint, to notify the deletion of a Digital Credential to the Credential Issuer;
  - the Credential endpoint, to refresh a Digital Credential that is already present in the Wallet Instance (also called Digital Credential re-issuance, see section :ref:`credential-issuance-low-level:Re-Issuance Flow`).

To mitigate the impact of a stolen Refresh Token, the Refresh Tokens MUST be DPoP. These aspects are detailed and discussed in Section :ref:`credential-issuance-low-level:Security Considerations`.

Figure below shows how to obtain a new DPoP Access Token and a new DPoP Refresh Token to the Token Endpoint.

.. _fig_refresh_token_flow:
.. plantuml:: plantuml/pid-issuance-high-level-flow.puml
    :width: 99%
    :alt: The figure illustrates the Refresh Token Flow.
    :caption: `Refresh Token Flow. <https://www.plantuml.com/plantuml/svg/TPBDQkim48NtUef3xYQ1cEpleYIaXMRLK0BP588gZ-EXpiYLnhXz-yfoJ1jAbvwVpzySj8vgWtQNnjXElNINLmh6jAd6ZbihYjdHDWqfTf96nT4CDgA_7Ta6AacKRODTZ1s5FCJ6z2ZkqEC_pYGKh1BkztwFDdXVmKg9uwOO2fKF-0M1-ZSIa9IjPz4hZHFja1lFzDvHLFIizK_k_4M0Sx2Y9_riQJby1ge2nVgKaGkaKjvwsdHQ5zk6IRJOg2QSLVQItVvgPcCMQ4seoPP3OZmTEgd5raiapArp5EFut-Mjnd8yS9G4VRISUYUMXJ6rU2LO5toC-7Tyt1qU4hecL8tluRmeIxfzFC8YN9DGdwLAgYW4AbU9mXMxRBrot_bEaKun34j2_HZYQ3owcNKQJQ_Z2m00>`_

.. .. figure:: ../../images/Refresh-Token-Flow.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/TPBDQkim48NtUef3xYQ1cEpleYIaXMRLK0BP588gZ-EXpiYLnhXz-yfoJ1jAbvwVpzySj8vgWtQNnjXElNINLmh6jAd6ZbihYjdHDWqfTf96nT4CDgA_7Ta6AacKRODTZ1s5FCJ6z2ZkqEC_pYGKh1BkztwFDdXVmKg9uwOO2fKF-0M1-ZSIa9IjPz4hZHFja1lFzDvHLFIizK_k_4M0Sx2Y9_riQJby1ge2nVgKaGkaKjvwsdHQ5zk6IRJOg2QSLVQItVvgPcCMQ4seoPP3OZmTEgd5raiapArp5EFut-Mjnd8yS9G4VRISUYUMXJ6rU2LO5toC-7Tyt1qU4hecL8tluRmeIxfzFC8YN9DGdwLAgYW4AbU9mXMxRBrot_bEaKun34j2_HZYQ3owcNKQJQ_Z2m00

..     Refresh Token Flow

.. note::
  The refresh of a Token may be triggered by different actions (e.g., User deletion of a Digital Credential). In each case, Wallet Instances are supposed to be running and the corresponding cryptographic material unlocked.

**Step 1**: The Wallet Instance MUST create a fresh DPoP Proof JWT and a fresh Wallet Instance Attestation proof of possession for the token request of the Credential Issuer (:ref:`WP_068a <wallet-credential-issuance-testcases>`).

**Step 2**: To refresh a DPoP-bound Access Token, the Wallet Instance sends a token request using the parameter ``grant_type`` set to ``refresh_token``, including the DPoP header and the OAuth Client Attestation headers (:ref:`WP_068 <wallet-credential-issuance-testcases>`).
A non-normative example of the token request for a DPoP Access Token using a Refresh Token is shown below.

.. code-block:: http

  POST /token HTTP/1.1
  Host: eaa-provider.example.org
  Content-Type: application/x-www-form-urlencoded
  DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6IkVDIiwieCI6IjR2dDhNdEFISmlsMzBDNnpUTmt2c0VVcnlHTEUtQW5BNkc5LV8xa3l5Rk0iLCJ5IjoiTWdiNTFfbjNSRjNtbHNtS3dMd0xtRUFqVmlJM3Q1bTVWNTI2MFA5MzR3RSIsImNydiI6IlAtMjU2In19.eyJqdGkiOiItQndDM0VTYzZhY2MybFRjIiwiaHRtIjoiR0VUIiwiaHR1IjoiaHR0cHM6Ly9yZXNvdXJjZS5leGFtcGxlLm9yZy9wcm90ZWN0ZWRyZXNvdXJjZSIsImlhdCI6MTU2MjI2MjYxOH0.3Tp1ZlZ05PQYeZUHhiZwaQ1etqnwYwoiJHFR_JHb32381lMJL-8o2rE3VZ8X3yuqrGFfCVeP90Ln4J5r8ASIBg
  OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtpZCI6IjBiNDk4ZGRlMDkxNzJhZGE3MDFkMDdlYjZmOTg2N2FkIiwidHlwIjoib2F1dGgtY2xpZW50LWF0dGVzdGF0aW9uK2p3dCIsIng1YyI6WyJNSUlEcWpDQ0FwS2dBd0lCQWdJRVNMTkV2REEgLi4uIiwiTUlJQ3d6Q0NBYXNDQ1FDS1Z5OWVLanZpK2pBIC4uLiIsIk1JSURURENDQWpTZ0F3SUJBZ0lKQVBsblFZSC4uLiJdfQ.eyJzdWIiOiJodHRwczovL3dhbGxldC1zb2x1dGlvbi5leGFtcGxlLm9yZy9kZDc2MmU2ZjhiNjEzMTkzIiwiY25mIjp7Imp3ayI6eyJjcnYiOiJQLTI1NiIsImt0eSI6IkVDIiwieCI6IjRITnB0SS14cjJwanlSSktHTW56NFdtZG5RRF91SlNxNFI5NU5qOThiNDQiLCJ5IjoiTElablNCMzl2RkpoWWdTM2s3alhFNHIzLUNvR0ZRd1p0UEJJUnFwTmxyZyJ9fSwid2FsbGV0X25hbWUiOiJXYWxsZXRfdjEiLCJ3YWxsZXRfbGluayI6Imh0dHBzOi8vZXhhbXBsZS5jb20vd2FsbGV0L2RldGFpbF9pbmZvLmh0bWwiLCJ3YWxsZXRfdmVyc2lvbiI6IjEuMC4wIiwiY2xpZW50X3N0YXR1cyI6eyJzdGF0dXMiOnsic3RhdHVzX2xpc3QiOnsiaWR4IjoxMzM3LCJ1cmkiOiJodHRwczovL3Jldm9jYXRpb25fdXJsL3dpYS1zdGF0dXNsaXN0cy80MiJ9fSwiZXhwIjoxMzAzNDk3NzgwfSwiZXhwIjoxNzQwMTU4MTY3fQ.XOv01xkHC-_h-bZFcXgkEffs3xk8WezKWs8KA4yZD8aNabDq81Y80wkOuHCM25zSGHbABszaSDsyYaJv9bh40w
  OAuth-Client-Attestation-PoP: eyJhbGciOiJFUzI1NiIsInR5cCI6Im9hdXRoLWNsaWVudC1hdHRlc3RhdGlvbi1wb3Arand0In0.ew0KICAiaXNzIjogIiA0N2I5ODIzNjk3OTFkMDgwMDNhNzI4M2YwNTljYjBkMSIsDQogICJhdWQiOiAiaHR0cHM6Ly9hcy5leGFtcGxlLmNvbSIsDQogICJqdGkiOiAiZDI1ZDAwYWItNTUyYi00NmZjLWFlMTktOThmNDQwZjI1MDY0IiwNCiAgImlhdCI6IDE3NDAxNTg2MTcNCn0.B0KOkGi9vMxf3H2Y8rrF-mdLNsuluTvAUbjFfL1Hi-gdaPW7-8ziS9uVh7aTnSAHKWzMfkZLv5q-bxhkglR4PA

  grant_type=refresh_token
  &refresh_token=eyJ0eXAiOiJydCtqd3QiLCJhbGciOiJFUzI1NiIsImtpZCI6ImM5NTBjMGU2ZmRlYjVkZTUwYTUwMDk2YjI0N2FmMDNjIn0.eyJpc3MiOiJodHRwczovL2VhYS1wcm92aWRlci53YWxsZXQuaXB6cy5pdCIsImNsaWVudF9pZCI6IjQ3Yjk4MjM2OTc5MWQwODAwM2E3MjgzZjA1OWNiMGQxIiwiYXVkIjoiaHR0cHM6Ly9lYWEtcHJvdmlkZXIud2FsbGV0LmlwenMuaXQiLCJpYXQiOjE3Mzk5NTI5NDgsIm5iZiI6MTczOTk1MzU0OCwiZXhwIjoxNzQyMzcyNzQ4LCJhdGgiOiJmVUh5TzJyMlozRFo1M0VzTnJXQmIweFdYb2FOeTU5SWlLQ0Fxa3NtUUVvIiwianRpIjoiYzY5NTVjZWItYzY1Zi00MDI1LTkzNzgtYjY2NzJiNjE0NWNmIiwiY25mIjp7ImprdCI6Ijk1MTU3NGFlZTFiYjc5MDdhZTFlYzMxMDlkYjJiMjI1In19.qiGM6E-7zci2-3Nnk4OMD7Tv_leUcRPsFsqaBHDHxEEzsGXLNh9qDbLIBk9sujZGVT9xs-28jZhwD6VT-MGTGw

**Step 3**: The Credential Issuer validates the request according to the following checks:

  - It MUST validate the OAuth-Client-Attestation-PoP parameter based on Section 5 of [`OAUTH-ATTESTATION-CLIENT-AUTH`_].
  - It MUST validate the DPoP Proof JWT, according to (:RFC:`9449`) Section 4.3.
  - It MUST check that the Refresh Token is not expired, not revoked and is bound to the same set of DPoP key as the ones used in the DPoP Proof JWT.

If the request checks are successful, the Credential Issuer generates a new Access Token and a new Refresh Token and these MUST be both bound to the DPoP key. Both the Access Token and the Refresh Token are then sent back to the Wallet Instance.

A non-normative example of a successful response is shown below.

.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json
  Cache-Control: no-store

  {
      "access_token": "eyJ0eXAiOiJhdCtqd3QiLCJhbGciOiJFU..",
      "refresh_token": "eyC3fiLdCtqd3QiLCJhbGciOiCL3..",
      "token_type": "DPoP",
      "expires_in": 3600
  }

If the Refresh Token is expired or invalid, the Credential Issuer MUST issue an error, using the error type member set to ``invalid_grant``. Therefore, to obtain the Digital Credential an issuance flow authenticating the User is required, as defined in Section :ref:`credential-issuance-low-level:Low-Level Issuance Flow`.

Security Considerations
^^^^^^^^^^^^^^^^^^^^^^^

To mitigate the risks of Refresh Token compromise, the following protections are required:

  - **Confidentiality** of Refresh Tokens MUST be guaranteed in transit and storage.
  - **TLS-protected** connections MUST be used for token transmission.
  - Refresh tokens MUST be **unguessable and secure from modification**.
  - Authorization Servers MUST implement the following mechanism to **detect replay attacks**:

    - **Sender-Constrained Tokens**: Crypto-graphically bind the Refresh Token to the Wallet Instance according to :rfc:`9449`. Access Tokens and Refresh Tokens MUST be bound to the same DPoP key. The DPoP Proof of the refresh token is required to refresh an Access Token. The same DPoP key MUST be used to generate Access Token DPoP Proofs in all the Credential Requests.

  - **Limiting the use of Refresh Token**: As specified in `OPENID4VC-HAIP`_: “Credential Issuers should be mindful of how long the usage of the refresh token is allowed to refresh a Credential, as opposed to starting the issuance flow from the beginning. For example, if the User is trying to refresh a Credential more than a year after its original issuance, the usage of the refresh tokens is NOT RECOMMENDED.” In this specification a new Digital Credential obtained performing the re-issuance flow SHOULD have the same expiration of the refreshed one. Thus, this specification does not allow for infinite refresh of Digital Credential with a Refresh Token. Once a Digital Credential expires, the User MUST complete the entire issuance process again, to obtain a new Digital Credential. This specification recommends to set a Refresh Token expiration duration, based on the sensitivity of the associated grant.

.. note::
  *Short-lived Wallet Instance Attestations and DPoP*: Following the specification draft *OAuth 2.0 Attestation Based Client Authentication* (`OAUTH-ATTESTATION-CLIENT-AUTH`_), the Authorization Server MUST bind the Refresh Token to the Client Instance. To prove this binding the Client Instance MUST use the Client Attestation mechanism when refreshing the Access Token and the Client Instance MUST use the same key that was presented in the ``cnf.jwk`` claim of the Client Attestation that was used when the Refresh Token was issued. However this requires that all issued Client Attestations MUST be bound to the same key, thus opening to unlinkability issues. In this specification, both `OAUTH-ATTESTATION-CLIENT-AUTH`_ and *OAuth 2.0 Demonstrating Proof of Possession (DPoP)* (:rfc:`9449`) MUST be used. Using DPoP guarantees the binding of the Refresh Token with the Client Instance as stated in section 5 of :rfc:`9449` *"the Refresh Token MUST be bound to the respective public key [...] a Client MUST present a DPoP proof for the same key that was used to obtain the Refresh Token each time that Refresh Token is used to obtain a new Access Token"* (:ref:`WP_068b <wallet-credential-issuance-testcases>`). DPoP ensures that the Refresh Token is bound to the Wallet Instance.


Re-Issuance Flow
----------------

Re-issuance involves replacing Digital Credentials already stored in a Wallet Instance with new ones of the same document type. The new Digital Credentials MUST be issued by the same Credential Issuers that originally provided the existing ones to the same Wallet Instance.

To facilitate this, particularly in scenarios where User authentication is not strictly required, a Refresh Token (RT) flow MAY be used (see Section :ref:`credential-issuance-low-level:Refresh Token Flow` for more details). An Access Token obtained as a result of a Refresh Token flow MUST NOT be used to issue a Digital Credential that is not present in the Wallet Instance (first-time-issuance). The Refresh Token mechanism enables automated Credential replacement, streamlining the process for both the Credential Issuer and the User.

The re-issuance process outlined in this section is limited to the following scenarios:

  - Data model/format technical update;
  - User's attribute set update.

This flow does not apply to device migration or backup restore. In those cases the Wallet Instance MUST perform a Wallet-Initiated Authorization Code Issuance Flow as defined in Section :ref:`credential-issuance-low-level:Low-Level Issuance Flow` (see Section :ref:`backup-restore:Restore flow for Hardware Binding Credential`).

In the first case, the new Digital Credential's Users attribute set will match the original one. For example, a Credential Issuer may need to update the Digital Credential metadata or data format without changing the User's attribute set. In this case, the direct involvement of the User is not mandatory for the replacement and storage of a Digital Credential.

In the second case, Credential Issuers may also need to modify one or more User's attribute values during re-issuance. In this case, the Wallet Instance MUST inform the User that the attribute data set has been changed and MUST then request the User's authorization to store the new Digital Credential.

In both cases, the newly issued Digital Credential MUST have the same expiry date as the previous one.

Re-issuance after Digital Credential expiration MUST always require User authentication.

The following diagram describes the Digital Credential re-issuance flow.

.. _fig_reissuance_flow:
.. plantuml:: plantuml/credential-reissuance-flow.puml
    :width: 99%
    :alt: The figure illustrates the Re-Issuance Flow Diagram.
    :caption: `Re-Issuance Flow Diagram. <https://www.plantuml.com/plantuml/svg/ZLFVYnCn47xFN_6zsSAT7FYsXtZL8Xme75KvH7p8xSvsWsbICvEs-jURfEtQbOZEmp93vfjlVdnxnwA3n8rLnL7E2o6OzI3gSI07ZQLP6z4MRm9rvCGarn5r3F5u8iHjfuMwAyX0bpdtp942u_tYCvXS1urKs_IcrMAyI-Y2-CGK4DcuDJG2hGqBfIBmKQvzV_sa4xBrcqrqPs0xQEV8FbUvQ6vNgQPKyLjoZ4TjBGdk7OjsBTqgA03DYYGOsX4-Y9R8U9U8yD5_8uVUXvm25f-OBsRW10OA1oprKg8LVOycv-tpUfp7JblJvQTAQJeadylZs6qEJ8_PRvupq3XykJdSlBX2-hx--ceEoHop7yJp0WDP9ioSdqFXqbZyLk54OtfL_3FHecs9-THHwRPI-MGbk6GQdyToA-e3yV1_zO0c3HS4KzHRw_V7vTRuwfCL6--XCBKZYtPmj2_QoyT7dtZ-pDmR6OhidZ4MCVSjPsbDKwSdApOkk1wDJXOabW_-0PFbYqSuwN1CJVrMVh7ZSYfIuQDKNXQ9_7tlJPOfiPH1ovW-c9zbojlQlKUgIJvnXM5wMn-eZ51hlNxN-cN7NTQ1_sQigRzPaYKXR0FjZ8yymQZIm5s2n8tz1G00>`_


.. .. figure:: ../../images/Re-Issuance-Flow.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/ZLJRRXen47ttLqoVcaXS8ZLFH553GoeX9HMYqAXAAcHsPrchNfjwPY7frtTjBiAuJV73QctFcSlncRaXbexhIejtocIwpX5AvYNrkbqdrvs5uhAUruGkiuRHS2UpLNUffV6ODd6krRnxUzaU-QFfmtstaiJecgFPuDN8IcMTfVVUh1196Ci8JYrA5eyb6f0mK4qKgU7MOOw6LVDh47C2jZ17g9UvPCnRm2KUsWo9QdG43_tlG6Xoa60igq9bafKr7kqHKq87DIcp00aE5ygdXpdOcjksQCzbWsnggcgp0sQbD0PrHtYdFbqXUi6BNQ8XU9HQ8yFG44kJuPKGge2pCQxi5b-Xzw2eWcS3r_2L9TS4zueOFfu3-wBFNf7E1GW0w8sHdS8LHeOJ-nCD5DPv4o2s3lE3ukagd0SkDHOSTcFyLIjlj_OXZ8MLr2eFLwbhV6d-ALpko_GRNyi1oLkWCl1qyNBneGNDz_B7KHb-eIQ4CsFFGS3X8hPB0TimgX2HhV3Rb84-4JfF9Pt6W5VJAHJ4llzAmHiSNCFmoxV-_N2GLhy3PNlGZ09ebYDBfJj-Xw3CtlffEXhq9tSjw4ycu-6dwUHkjZb9kJs9tfZXqvzZyusAw6SP4crb4lXBKjgl9B_uUjCOXKCgJ_C7q6lOTWmnwhEswyrxln4lvGDWBn41yTf4aGOChiCayQqCHHFds7Ajk0n3v3r1l_PvysvGnAPn7wLlakxsFtwym61aHn2HpnRSjZNsfZxVT61koKcrIplj-hvjWNNmRFwZqkj4a_z-hvvlE2GE10Lwh5E_0pjNXtQ9AY9xf2J2iIQiGrzwNFBRUeWLaRv80Zmzub7Nz0QeaH6M3bVArXHXH4ZWfe7KbVu3

..     Re-Issuance Flow Diagram


**Step 1**: The flow starts when the User opens the Wallet Instance: this step MAY be triggered either by a notification sent by the Credential Issuer (using e.g., one of the out-of-band communication contacts registered during the Issuance flow).

**Step 2**: The Wallet Instance MUST check the status of any stored Digital Credential by retrieving a valid Status List Token if one is not already available, following the profile in :ref:`credential-revocation:Token Status List (Digital Credentials Profile)` and the checking procedure in :ref:`credential-revocation:Checking Credentials Statuses`, as covered by :ref:`WP_069 <wallet-credential-issuance-testcases>`.
Then, the Wallet Instance MUST check  (:ref:`WP_070 <wallet-credential-issuance-testcases>`) if any Digital Credential has status set to ``0x03`` - ``UPDATE`` or ``0x0F`` - ``ATTRIBUTE_UPDATE``.

If the conditions above are not met, the flow MUST be interrupted.

Otherwise, the Wallet Instance MUST check the related Access Tokens. If they are still valid, then Step 3 MAY be skipped  (:ref:`WP_071 <wallet-credential-issuance-testcases>`).

**Step 3**: If the Access Token is expired and the Wallet Instance still has a valid Refresh Token, the Wallet Instance MUST obtain a new Access Token starting a Refresh Token Flow, according to Section :ref:`credential-issuance-low-level:Refresh Token Flow`  (:ref:`WP_071a <wallet-credential-issuance-testcases>`).
The Refresh Token Flow enables the Wallet Instance to obtain a new Refresh Token and a new DPoP Access Token to refresh the Digital Credential. If the Refresh Token is expired, a new Issuance Flow authenticating the User is required (:ref:`WP_067 <wallet-credential-issuance-testcases>` and :ref:`WP_071b <wallet-credential-issuance-testcases>`).

**Step 4**: The Wallet Instance MUST use a valid DPoP Access Token to retrieve the new Digital Credential requesting it to the Credential endpoint following the steps from 12 to 22 of Figure 9 in Section :ref:`credential-issuance-low-level:Low-Level Issuance Flow`  (:ref:`WP_072 <wallet-credential-issuance-testcases>`).
When the new Digital Credential is successfully stored in the secure storage, the Wallet Instance MUST delete the previous one  (:ref:`WP_073 <wallet-credential-issuance-testcases>`).

.. note::
  Regardless of the Digital Credential revocation mechanism supported, if the Digital Credential status is set to ``ATTRIBUTE_UPDATE``, the User's attribute set, in the refreshed Digital Credential, doesn't match the one in the stored Digital Credential. In this case, the Wallet Instance MUST request the User's authorization to store the new refreshed Digital Credential  (:ref:`WP_074 <wallet-credential-issuance-testcases>`).

  If instead, either the Digital Credential status is set to ``UPDATE``, only the Credential metadata parameters have changed. In this case, the Wallet Instance SHOULD store the new Digital Credential without requiring explicit user authorization and consent  (:ref:`WP_075 <wallet-credential-issuance-testcases>`).


Re-Issuance Flow: Security Considerations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To ensure the integrity and security of the re-issuance process, the following security considerations apply.

  - Access Token limitations: An Access Token obtained as a result of a Refresh Token flow MUST NOT be used for the first-time issuance of a Digital Credential. This ensures that only existing Credentials in the Wallet Instance are updated.
  - Credential expiry: The Credential Issuer MUST set the same expiry date for the re-issued Digital Credential as the previous one. This prevents indefinite Credential renewals without proper User authentication.
  - User consent: For re-issuance processes triggered by attribute changes, User consent MUST be obtained before storing the new Digital Credential. This ensures that the User is aware of and agrees to the updated information.
  - Sender-constrained Refresh Token: Refresh Tokens MUST be cryptographically bound to the Wallet Instance using DPoP protocol. This mitigates the risk of token misuse by ensuring that only the intended Wallet Instance (the same that originally has obtained the Digital Credential) can use that Refresh Token.

.. note::
    During each credential issuance and, where supported, each re-issuance/refresh transaction executed through the flows described in this section, the Wallet Instance MUST create and maintain a corresponding transaction record in the Wallet Instance transaction log (see :ref:`wallet-instance-dashboard:Wallet Instance Dashboard and Transaction Logging`).

    The Wallet Instance MUST create a transaction record for each credential issuance process. The record MUST capture relevant contextual information necessary to ensure traceability and accountability of the transaction.

    The record MUST be updated as the flow progresses to reflect the evolving transaction state and outcome context (e.g., the issued credential type(s) and quantity). In cases where the transaction does not complete successfully, the record MUST indicate the corresponding reason for non-completion.


Credential Offer Flow
-----------------------

A Credential Issuer or third party (e.g., Authentic Source, Registry, Catalogue) initiates Credential Issuance by sending a Credential Offer to the Wallet Instance.

To invoke the correct Wallet Instance, they need to know which Wallet Instance is installed on the User's device and the User wishes to use.
This information SHOULD be obtained using the Selection Page described in :ref:`functionalities:User Experience Design`.

- If the Selection Page is supported, the User selects the Wallet, and then the Credential Issuer or third party retrieves the Wallet metadata as described in :ref:`wallet-metadata-retrieval:Wallet Metadata Retrieval Flow`. The Wallet Instance invocation mechanism depends on the ``credential_offer_endpoint`` parameter in the Wallet metadata:

  - If ``credential_offer_endpoint`` is available and contains an HTTPS URL (Universal Link), the Credential Issuer or third party SHOULD use that endpoint.
  - Otherwise, the Credential Issuer or third party MUST use one of the custom URL schemes: ``openid-credential-offer://`` (as defined in Section 4 of [`OpenID4VCI`_]) or ``haip-vci://`` (as defined in Section 4.2 of [`OPENID4VC-HAIP`_]). The Wallet Instance MUST support both custom URL schemes.

- In the case when the Credential Issuer or third party does not support the Selection Page, or the retrieval of the Wallet metadata may fail for some reason, the Credential Issuer or third party invokes the Wallet Instance using the custom URL scheme described above.

The Credential Offer can be transmitted by value or by reference:

- **By value** (``credential_offer`` parameter): the Credential Offer object is directly embedded in the URI as a JSON-encoded string.
- **By reference** (``credential_offer_uri`` parameter): the URI points to a resource hosted by the Credential Issuer or third party. The Wallet Instance retrieves the Credential Offer object by sending an HTTP GET request to that URI.

The Credential Offer object is a JSON object containing the parameters defined in Section 4.1.1 of [`OpenID4VCI`_]. The table below specifies the parameters with IT-Wallet specific requirements:

.. _table_credential_offer_claim:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **credential_issuer**
    - It MUST be set with an HTTPS URL that uniquely identifies the Credential Issuer. The Wallet uses this parameter value to obtain the Credential Issuer's metadata.
    - Section 4.1.1 of [`OpenID4VCI`_].
  * - **credential_configuration_ids**
    - Array of Strings, each of them specifying a unique identifier of the Credential being described in the ``credential_configurations_supported`` map in the Credential Issuer Metadata (:ref:`WP_050b <wallet-credential-issuance-testcases>`).
    - Section 4.1.1 of [`OpenID4VCI`_].
  * - **grants**
    - REQUIRED. It MUST contain ``authorization_code`` object with the following parameters:

        - **issuer_state**: OPTIONAL. Opaque string used to bind the subsequent Authorization Request with the Credential Issuer. It MAY be bound to a specific Credential Dataset provided by a certain Authentic Source. The Wallet MUST include it in the subsequent Authorization Request when present. It MUST be a URN and contain the following information:

            - *authenticSourceId:* REQUIRED. It MUST correspond to the ``entity_id`` value of the Authentic Source that provides the Credential Dataset(s) as registered in the :ref:`registry:Authentic Source Registry`.

            - *datasetId:* REQUIRED. The unique identifier of the dataset provided by the Authentic Source as registered in the :ref:`registry:Authentic Source Registry`.

            - *objectId:* OPTIONAL. Unique identifier of the Credential Dataset available from the Authentic Source.

        The ``issuer_state`` MUST follow the structure ``urn:it-wallet:credential-offer:{authenticSourceId}:{datasetId}`` when ``objectId`` is absent, or ``urn:it-wallet:credential-offer:{authenticSourceId}:{datasetId}:{objectId}`` when ``objectId`` is present. The optional ``objectId`` segment MUST be omitted when not available; an empty trailing segment MUST NOT be used. This URN value MUST be encrypted using the PDND public key related to the ``GetAttributeClaims`` e-service Consumer.

        - **authorization_server**: REQUIRED when the Credential Issuer uses more than one authorization server in its Issuer Solution. This string identifies the Authorization Server to use. The value MUST match with one of the values mapped in the ``authorization_servers`` array of the Credential Issuer metadata. It MUST NOT be used if ``authorization_servers`` is absent or it has no multiple entries.
    - Section 4.1.1 of [`OpenID4VCI`_] and Section 4.1 of [`OPENID4VC-HAIP`_].

.. note::
  When using ``credential_offer_uri`` (by reference), the Credential Issuer or third party SHOULD use a unique URI for each Credential Offer or otherwise prevent caching of the URI, as recommended in Section 4.1.3 of [`OpenID4VCI`_].

Non-normative Examples
^^^^^^^^^^^^^^^^^^^^^^^

**Example 1: Credential Offer by value**

The Credential Offer can be transmitted by value using any supported invocation method (custom URL scheme or Universal Link):

.. code-block:: text

  openid-credential-offer://?credential_offer=%7B%22credential_issuer%22%3A%22https%3A//credential-issuer.example.org%22%2C%22credential_configuration_ids%22%3A%5B%22dc_sd_jwt_Education_degree%22%5D%2C%22grants%22%3A%7B%22authorization_code%22%3A%7B%issuer_state%22%3A%22eyJhbGciOiJSU0Et...F77QK8%22%7D%7D%7D

The decoded Credential Offer object:

.. code-block:: json

  {
    "credential_issuer": "https://credential-issuer.example.org",
    "credential_configuration_ids": ["dc_sd_jwt_Education_degree"],
    "grants": {
      "authorization_code": {
        "issuer_state": "eyJhbGciOiJSU0Et...F77QK8",
      }
    }
  }

**Example 2: Credential Offer by reference from Credential Issuer**

The QR Code or the href button contains:

.. code-block:: text

  openid-credential-offer://?credential_offer_uri=https%3A%2F%2Fcredential-issuer.example.org%2Foffers%2F8f3a2b1c

The Wallet Instance sends an HTTP GET request:

.. code-block:: http

  GET /offers/8f3a2b1c HTTP/1.1
  Host: credential-issuer.example.org
  Accept: application/json

The Credential Issuer responds:

.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json
  Cache-Control: no-store

  {
    "credential_issuer": "https://credential-issuer.example.org",
    "credential_configuration_ids": ["dc_sd_jwt_EuropeanDisabilityCard"],
    "grants": {
      "authorization_code": {
        "issuer_state": "eyJhbGciOiJSU0Et...F77QK8",
      }
    }
  }

**Example 3: Credential Offer by reference from third party**

A third party, such as an Authentic Source, generates a Credential Offer for a Credential Issuer.

The QR Code contains:

.. code-block:: text

  openid-credential-offer://?credential_offer_uri=https%3A%2F%2Fauthentic-source.gov.example%2Fcredential-offers%2Fabc123

The Wallet Instance sends:

.. code-block:: http

  GET /credential-offers/abc123 HTTP/1.1
  Host: authentic-source.gov.example
  Accept: application/json

The Authentic Source responds:

.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json
  Cache-Control: no-store

  {
    "credential_issuer": "https://credential-issuer.example.org",
    "credential_configuration_ids": ["mso_mdoc_mDL"],
    "grants": {
      "authorization_code": {
        "issuer_state": "eyJhbGciOiJSU0Et...F77QK8",
      }
    }
  }


