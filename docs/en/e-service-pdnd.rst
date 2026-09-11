.. include:: ../common/common_definitions.rst
.. Included via appendix.rst at title level '=' (document title).


e-Service PDND
==============

The `EIDAS-ARF`_ framework empowers Member States to establish the interfaces, terms, and conditions governing communication between Credential Issuers and Authentic Sources. In the Italian context, interoperability is established by leveraging the following guidelines:

    - "Linee Guida sull'interoperabilità tecnica delle Pubbliche Amministrazioni" (`MODI`_);
    - "Linee Guida sull'infrastruttura tecnologica della Piattaforma Digitale Nazionale Dati per l'interoperabilità dei sistemi informativi e delle basi di dati" (`PDND`_).

To leverage the PDND, entities MUST formally be subscribed becoming **Participants** (*Aderenti*). Within the PDND infrastructure, Participants MUST assume at least one of the following roles:

    - **Providers** (*Erogatori*): expose e-Services to other Participants.
    - **Consumers** (*Fruitori*): utilize e-Services offered by Providers within the PDND infrastructure.

Access to an e-Service requires Consumers to obtain a specific Access Token, known within the PDND infrastructure as a Voucher.

Requirements and Security Patterns
-----------------------------------

This specification is based on the following set of requirements:

.. list-table::
  :class: longtable
  :widths: 10 70 20
  :header-rows: 1

  * - **ID**
    - **Description**
    - **Type**
  * - R1
    - The Consumer and the Provider have both subscribed to the PDND infrastructure.
    - Architectural
  * - R2
    - The communication between the Consumer and the Provider MUST ensure data integrity, authenticity, non-repudiation and replay protection.
    - Security
  * - R3
    - The Provider MAY require the Consumer to provide tracked data to complement the request. In that case, there MUST be a correlation between the tracked data and the Voucher.
    - Security
  * - R4
    - The e-Services MUST be implemented in REST, thus SOAP protocol MUST NOT be used.
    - Technical
  * - R5
    - The Provider MUST ensure, with a high degree of certainty, the Consumer's proof of possession of the Voucher.
    - Security

`PDND`_ and `MODI`_ define several security patterns designed to enhance specific security properties in interactions between Participants. This specification adopts the following applicable security patterns for the interaction between Participants:

.. list-table::
  :class: longtable
  :widths: 80 20
  :header-rows: 1

  * - **Security Pattern**
    - **Compliant With**
  * - **[REST_JWS_2021_POP]** JWS POP Voucher Issuing Profile (*Annex 3 - Standards and technical details used for Voucher Authorization* [`PDND`_]): REQUIRED. It adds a proof of possession on the Voucher. The Consumer using the Voucher to access an e-service MUST demonstrate the proof of possession of the private key whose public is attested on the Voucher.
    - R2, R4, R5
  * - **[ID_AUTH_CHANNEL_01]** Direct Trust Transport-Level Security (*Annex 2 - Security Patterns* [`MODI`_]): REQUIRED. It protects the communication between the Consumer and the Provider by ensuring confidentiality, integrity, identification of the Provider, and mitigation against replay attack and spoofing.
    - R1, R2
  * - **[INTEGRITY_REST_02]** REST Payload Integrity in PDND (*Annex 2 - Security Patterns* [`MODI`_]): CONDITIONAL. It ensures the integrity of the payload of the REST Consumer request and the REST Provider response, within the PDND Infrastructure. It is REQUIRED whenever the request/response carries a payload.
    - R2, R4
  * - **[AUDIT_REST_02]** Submission of audit data within the REST request with correlation (*Annex 2 - Security Patterns* [`MODI`_]): OPTIONAL. The Provider MAY request additional data tracked in the Consumer's domain, with a correlation between such data and the authentication method. In that case, this pattern MUST be used.
    - R3, R4
  * - **[ID_AUTH_REST_01]** Direct Trust based on PDND via Platform-issued JWT tokens (*Annex 2 - Security Patterns* [`MODI`_]).
    - R1, R2, R4, R5

.. note::
    In the current specifications, the ``REST_JWS_2021_POP`` security pattern is implemented in accordance with :rfc:`9449`.

    Alternatively, the proof of possession MAY be attested using the ``TrackingEvidence`` JWT to provide additional data. In this context, ``TrackingEvidence`` JWT acts as a proof of possession of the PDND Voucher. Such implementation choices will be referred to as ``POP_DPoP`` and ``POP_TPoP``, respectively.

The following security patterns defined in `PDND`_ and `MODI`_ MUST NOT be used as they do not comply with the requirements defined above:

    - The following patterns can only be used when the Consumer cannot subscribe to the PDND infrastructure (i.e., the trust between the Participants needs to be established in a direct form), thus not complying with **R1**:

      - **[ID_AUTH_CHANNEL_02]** Direct Trust mutual Transport-Level Security (*Annex 2 - Security Patterns* [`MODI`_])
      - **[ID_AUTH_REST_02]** Direct Trust based on PDND via Platform-issued JWT tokens and token/message uniqueness (*Annex 2 - Security Patterns* [`MODI`_]).
      - **[INTEGRITY_REST_01]** REST Payload Integrity (*Annex 2 - Security Patterns* [`MODI`_]).

    - The following pattern does not provide correlation between the tracked data and the Voucher, thus not complying with **R3**:

      - **[AUDIT_REST_01]** Submission of audit data within the REST request (*Annex 2 - Security Patterns* [`MODI`_]).

    - The following patterns are based on a SOAP architecture, thus not complying with **R4**:

      - **[ID_AUTH_SOAP_01]** Direct Trust based on X.509 certificate with SOAP (*Annex 2 - Security Patterns* [`MODI`_]).
      - **[ID_AUTH_SOAP_02]** Direct Trust based on X.509 certificate with SOAP and token/message uniqueness (*Annex 2 - Security Patterns* [`MODI`_]).
      - **[INTEGRITY_SOAP_01]** SOAP Payload Integrity (*Annex 2 - Security Patterns* [`MODI`_]).

    - The following pattern does not guarantee proof of possession of the Voucher, thus not complying with **R5**:

      - **[REST_JWS_2021_Bearer]** JWS Bearer Voucher Issuing Profile (*Annex 3 - Standards and technical details used for Voucher Authorization* [`PDND`_]).

.. note::
  In case of ``POP_TPoP`` implementation, the Voucher is issued as a Bearer token. However, since it is accompanied by a proof of possession, it still complies with the ``REST_JWS_2021_POP`` security pattern rather than ``REST_JWS_2021_Bearer``.

PDND Voucher Issuance
----------------------

The PDND infrastructure defines two different types of Vouchers:

  - **For e-Service**: allow Consumers to request data from an e-Service.
  - **For Interoperability API**: allow Participants to request data from the Interoperability API, exposed by the PDND Infrastructure.

The two flows are described below.

PDND Voucher for e-Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PDND Voucher for e-Services Prerequisites
"""""""""""""""""""""""""""""""""""""""""

The **Consumer** MUST comply with the following prerequisites:

    - Has successfully subscribed to the PDND Infrastructure (as per R1).
    - Has created a new `Client e-service` to interact with the intended e-Service. Upon creation, it has been assigned a ``client_id`` by the PDND Platform.
    - Has registered a key pair associated with the `Client e-service`.
    - Has requested to enroll in the intended e-Service.
    - Has defined a new purpose for the e-Service. Upon definition, it has been assigned a ``purposeId`` by the PDND Platform.
    - Has associated the `Client e-service` with the defined purpose.

The **Provider** MUST comply with the following prerequisites:

    - Has successfully subscribed to the PDND Infrastructure (as per R1).
    - Has created a new e-Service and published it within the PDND API Catalog.
    - Has approved the Consumer's request to enroll in the e-Service.


PDND Voucher for e-Services Flow
""""""""""""""""""""""""""""""""

.. _fig_VoucherIssuance_eService_Flow:
.. plantuml:: plantuml/pdnd-voucher-issuance.puml
    :width: 80%
    :alt: The figure illustrates the Voucher Issuance for e-Service - Detailed flow.
    :caption: `Voucher Issuance for e-Service - Detailed flow. <https://www.plantuml.com/plantuml/svg/VP71RjH0343lynLMUcaZLaALuD03QfHjrKK8ecQ1O-HEtCqeoJXuF4ktNqycj5s42fSeTkpdP-SoA8h6SO1l76r70fiG8dfBi09QrIHxPycequ7-Ns8mAliutf4OSySFaESb-n17aZo7aysUvM009XHrrate5R8y_r94xQ0S77dDymmmG7bjoBSm8vuvrVhpEZ6AnoZqBqPwiBX7LCSUaXN94x6eZqIU5AvPeFYwtcoRswjwsxmzDp1FNNqehoygePbEyF7x5dww6Mjvd0OQoIlA0LfKXDCismhQtldTrTwrv2rbsPavGigv9of1VLESltiF7OOE-1vUQqkmczE_ysU9DoiRyqmKGYLOLrn1JmUOq0cWRs4IvlkbggWlNdxGBVs853J1xNBQnhLPzWPUGWo191tgzMoZXub-Vze9UbtYPKVnh0Iy9u6YXfDFRjTfvNoVbk_8zY5fBqN65FLgaJzQXObzeAI5rb88ZN9FJmxfzS_1z30veT0udmPVpjWu3hy0>`_


.. .. figure:: ../../images/Low-Level-Flow-AuthenticSource-Voucher-Issuance-eService.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/TT5HRzCm40VmTt-AK_QoHLH2a-1X3sXHkcf52AAbm6FakRV6Ik8pvtDPz-cnGxSYjBr4iMF_xd-Nwo2Q9KwZ4YiZmW-AfaU6TGXHEuEm05oqo7jhK2aTXLoSxf6LkgT7ACkQN8WJSbd2sNfFV500FedMMA-TG56MtweeFTIZHITbMO0EKAyKkYqaujbfbb-NsQYU8kDRHduGsoSjbXpaLCX7iMfF8dc15J5KtvVhJNTtqswwzvSAKjN5ftfrrJ0c7U7ppmtyjearDFaH9tIY-G1RBHhEYsB3sWpMxMxsTelEO55Sg1DIfpjH4DhRwlB3H-Xrw84UuBLh6Riz_t__8davibBF8gDEuBAX1WOyWDUMGQUUF1CzpAUgzkhb1ztXhuX1CcxcqNPsMnJlu6MfGq3EWtfzjvE3nx-VTgoT7DUfHtOa2BH7Xgg5iozsrqjZtP2Rxz4C8SUU3obLjOiv_2bLyEG2vbZQ60oX4nhmc26__biO7xrb39rrkV1rOkCq_W40

..     Voucher Issuance for e-Service - Detailed flow

**Steps 1-2 (Preparation of Tracked Data):** The Consumer prepares a JWT (``TrackingEvidence``) containing the tracked data that have to be sent to the Provider. Finally, it computes the SHA-256 hash of ``TrackingEvidence``.

.. code-block:: json
  :caption: Non-normative example of the ``TrackingEvidence`` header
  :name: code_VoucherIssuance_eService_Flow_TrackingEvidence_Header

  {
    "alg": "ES256",
    "kid": "d4c3b2a1-9876-5432-10fe-dcba98765432",
    "typ": "JWT"
  }


.. code-block:: json
  :caption: Non-normative example of the ``TrackingEvidence`` payload
  :name: code_VoucherIssuance_eService_Flow_TrackingEvidence_Payload

  {
    "iss": "82914b3f-60b2-4529-b4d6-3d4e67f0a933",
    "aud": "https://erogatore.example/ente-example/v1",
    "exp": 1733052600,
    "nbf": 1733036450,
    "iat": 1733036400,
    "jti": "a4b5c6d7-e8f9-abcd-ef12-345678901234",
    "dnonce": 6528424213685,
    "purposeId": "b2c3d4e5-f6g7-h8i9-j0k1-lmno12345678",
    "userID": "a8b7c6d5-e4f3-g2h1-i9j0-klmnopqrstuv",
    "loa": "substantial"
  }

.. note::
  Steps 1-2 are required only when complying with the ``AUDIT_REST_02`` security pattern or the ``POP_TPoP`` implementation.

**Step 3 (DPoP Key Pair and Proof)**: The Consumer MUST create a new key pair for the DPoP and a fresh DPoP proof JWT following the instruction provided in the Section 4 of :rfc:`9449` for the token request to the PDND Authorization Server.

.. note::
  Step 3 is required only when complying with the ``POP_DPoP`` implementation.

**Step 4 (Voucher Request)**: The Consumer creates a Voucher Request and sends it to the PDND Authorization Server.

.. code-block:: http
    :caption: Non-normative example of the Voucher Request
    :name: code_VoucherIssuance_eService_Flow_Request

    POST /authorization-server/token HTTP/1.1
    Host: interop.pagopa.it
    DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6IkVDIiwia2V5X29wcyI6WyJzaWduIl0sImtpZCI6IjM5ZmE5NjBiLTc3M2YtNDllZi04YTBlLWU3NzNlOWI5N2FlOCIsImNydiI6IlAtMjU2IiwieCI6Imh1eVhJUU52OTAyb0xzcFg0X3pvbkM5NEc2eUVsbjZsc2RtLTF3TTczMm8iLCJ5IjoiSTlQREVhd1dIcWFGREd4MVprTmstMlBWNldkcGNhSDNBZk9iQlNMaWhndyJ9fQ.eyJqdGkiOiI1NTBlODQwMC1lMjliLTQxZDQtYTcxNi00NDY2NTU0NDAwMDAiLCJodG0iOiJQT1NUIiwiaHR1IjoiaHR0cHM6Ly9pbnRlcm9wLnBhZ29wYS5pdC9hdXRob3JpemF0aW9uLXNlcnZlciIsImlhdCI6MTc2MjI2MDYxNn0.D0ZUDkfGHx_rQBdYi_3VSXkdbJM-7FSWN88LWICQImMWtIWd2mbxGb7v8udfM_c4_ase8x7I3I1JZm01Us3QEA
    Content-Type: application/x-www-form-urlencoded

    grant_type=client_credentials&
    client_id=82914b3f-60b2-4529-b4d6-3d4e67f0a933&
    client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&
    client_assertion=eyJhbGciOiJFUzI1NiIsImtpZCI6ImQ0YzNiMmExLTk4NzYtNTQzMi0xMGZlLWRjYmE5ODc2NTQzMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI4MjkxNGIzZi02MGIyLTQ1MjktYjRkNi0zZDRlNjdmMGE5MzMiLCJzdWIiOiI4MjkxNGIzZi02MGIyLTQ1MjktYjRkNi0zZDRlNjdmMGE5MzMiLCJhdWQiOiJpbnRlcm9wLnBhZ29wYS5pdC9hdXRob3JpemF0aW9uLXNlcnZlciIsImV4cCI6MTczMzA0MTQ0MCwiaWF0IjoxNzMzMDM3ODQwLCJqdGkiOiI3ZTlmM2E0ZC1jOWIyLTQyZjYtYTZkNC0zOGUxMmZiNmI4YWIiLCJwdXJwb3NlSWQiOiJkMmI5YTY1My1jNDk3LTQ1YzYtYjhmMS01YmRmMTI0YzlkM2EiLCJkaWdlc3QiOnsiYWxnIjoiU0hBMjU2IiwidmFsdWUiOiI5Yzc4OTRhMGE1YTkxMDU4MGI5NjdmMzg0Y2RmYmExN2IxYWI2Zjg2NjcwZTViMGRmMThhMGM0NTNiNWViMjE1In19.cl-wvwJF3WLgywoq9qULVKCajleqz0jpD82QTZZAxHSjoGeA7l7n0LNC8eDfIM4F-rzMU5qfC9eW6UDxMwJrdg


.. code-block:: json
    :caption: Non-normative example of the ``client_assertion`` JOSE header
    :name: code_VoucherIssuance_eService_Flow_ClientAssertion_Header

    {
        "alg": "ES256",
        "kid": "d4c3b2a1-9876-5432-10fe-dcba98765432",
        "typ": "JWT"
    }


.. code-block:: json
    :caption: Non-normative example of the ``client_assertion`` payload
    :name: code_VoucherIssuance_eService_Flow_ClientAssertion_Payload

    {
        "iss": "82914b3f-60b2-4529-b4d6-3d4e67f0a933",
        "sub": "82914b3f-60b2-4529-b4d6-3d4e67f0a933",
        "aud": "https://interop.pagopa.it/authorization-server",
        "exp": 1733041440,
        "iat": 1733037840,
        "jti": "7e9f3a4d-c9b2-42f6-a6d4-38e12fb6b8ab",
        "purposeId": "d2b9a653-c497-45c6-b8f1-5bdf124c9d3a",
        "digest": {
            "alg": "SHA256",
            "value": "9c7894a0a5a910580b967f384cdfba17b1ab6f86670e5b0df18a0c453b5eb215"
        }
    }

.. note::
  The ``purposeId`` claim in the ``client_assertion`` payload is required only when requesting a Voucher for e-Service.

.. note::
  The ``digest`` claim in the ``client_assertion`` payload is required only when complying with the ``AUDIT_REST_02`` security pattern or the ``POP_TPoP`` implementation.

Upon the receipt of the Voucher Request, the PDND Authorization Server MUST perform the following checks on the Voucher Request body parameters:

    - The claim ``client_assertion_type`` is set to ``urn:ietf:params:oauth:client-assertion-type:jwt-bearer``.
    - The claim ``grant_type`` is set to ``client_credentials``.

The PDND Authorization Server MUST also validate the ``client_assertion`` JWT as follows:

    Header:

      - Ensure that the ``typ`` claim is present and that its value is ``JWT``.

    Signature:

      - Obtain the Consumer's public key corresponding to the ``kid`` header parameter, by interacting with the PDND Interoperability API.
      - Validate the signature of the JWT using the retrieved Consumer's public key and the algorithm specified by the ``alg`` header parameter.

    Payload:

      - The ``iss`` and ``sub`` claims MUST identify a Client registered in the PDND Infrastructure.
      - The ``aud`` claim MUST represent the PDND Authorization Server.
      - The ``exp`` claim MUST represent a time instant after the current time.
      - If the ``nbf`` claim is present, it MUST represent a time instant prior to the current time.
      - The ``iat`` claim MUST represent a time instant prior to the current time.
      - The ``jti`` claim MUST NOT have been previously used.
      - The ``purposeId`` claim MUST identify a purpose registered in the PDND Infrastructure and associated to the Client.

.. note::
  The PDND Authorization Server does not need to perform any checks on the ``digest`` claim.

.. note::
  Verification of the ``exp``, ``nbf``, ``iat``, and ``jti`` claims, as detailed above, MUST be performed for all JWTs described within this section. These checks will not be explicitly mentioned in subsequent references.

**Step 6 (Voucher Issuance)**: In case of successful checks, the PDND Authorization Server issues a Voucher, which is included in the Voucher Response to the Consumer.

.. code-block:: http
    :caption: Non-normative example of the Voucher Response
    :name: code_VoucherIssuance_eService_Flow_Response

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store

    {
        "access_token": "eyJhbGciOiJFUzI1NiIsImtpZCI6ImI4MzlmNGM3LTFlNWQtNGE4YS05ZmM2LTcyZDNiN2YwOTFlYyIsInR5cCI6ImF0K2p3dCJ9.eyJpc3MiOiJpbnRlcm9wLnBhZ29wYS5pdCIsInN1YiI6IjgyOTE0YjNmLTYwYjItNDUyOS1iNGQ2LTNkNGU2N2YwYTkzMyIsImF1ZCI6Imh0dHBzOi8vZXJvZ2F0b3JlLmV4YW1wbGUvZW50ZS1leGFtcGxlL3YxIiwiZXhwIjoxNzMzMDQyMTUwLCJuYmYiOjE3MzMwNDE5NDUsImlhdCI6MTczMzA0MTkyMCwianRpIjoiYzRmNWQ3ZTItYjdjOC00MGY2LTliNmEtZGM5YTRmNWFlYjU3IiwiY2xpZW50X2lkIjoiODI5MTRiM2YtNjBiMi00NTI5LWI0ZDYtM2Q0ZTY3ZjBhOTMzIiwicHVycG9zZUlkIjoiZDJiOWE2NTMtYzQ5Ny00NWM2LWI4ZjEtNWJkZjEyNGM5ZDNhIiwiZGlnZXN0Ijp7ImFsZyI6IlNIQTI1NiIsInZhbHVlIjoiOTkwOGQ5NGI4ZmViMjY4YzAzNzEwNmQ3Yzg5ZTcwNjBjMmNjMWY2YjJiNGViY2I4MDViZmVlNTNhNTM5MzA3YiJ9LCJjbmYiOnsiamt0IjoiMFpjT0NPUlpOWXktRFdwcXEzMGpaeUpHSFROMGQySGdsQlYzdWlndUE0SSJ9fQ.sGhaHEOfMTB7r4_8ZILM_a9eTBGawWn3kL-dxYoZggFIzyrXDOZcQWt0zr00lMk2iYAMWxS32e4cUedmAsBXGw",
        "token_type": "DPoP",
        "expires_in": 3600
    }

.. code-block:: json
    :caption: Non-normative example of the ``access_token`` JOSE header
    :name: code_VoucherIssuance_eService_Flow_AccessToken_Header

    {
        "alg": "ES256",
        "kid": "b839f4c7-1e5d-4a8a-9fc6-72d3b7f091ec",
        "typ": "at+jwt"
    }

.. code-block:: json
    :caption: Non-normative example of the ``access_token`` payload
    :name: code_VoucherIssuance_eService_Flow_AccessToken_Payload

    {
        "iss": "https://interop.pagopa.it",
        "sub": "82914b3f-60b2-4529-b4d6-3d4e67f0a933",
        "aud": "https://erogatore.example/ente-example/v1",
        "exp": 1733042150,
        "nbf": 1733041945,
        "iat": 1733041920,
        "jti": "c4f5d7e2-b7c8-40f6-9b6a-dc9a4f5aeb57",
        "client_id": "82914b3f-60b2-4529-b4d6-3d4e67f0a933",
        "purposeId": "d2b9a653-c497-45c6-b8f1-5bdf124c9d3a",
        "digest": {
            "alg": "SHA256",
            "value": "9c7894a0a5a910580b967f384cdfba17b1ab6f86670e5b0df18a0c453b5eb215"
        },
        "cnf": {
            "jkt": "0ZcOCORZNYy-DWpqq30jZyJGHTN0d2HglBV3uiguA4I"
        }
    }

.. note::
  The ``digest`` claim in the ``access_token`` payload is required only when complying with the ``AUDIT_REST_02`` security pattern or the ``POP_TPoP`` implementation. If present, it corresponds to the value of the ``digest`` claim contained in the ``client_assertion``.

PDND Voucher for Interoperability API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PDND Voucher for Interoperability API Prerequisites
"""""""""""""""""""""""""""""""""""""""""""""""""""""

The **Participant** MUST comply with the following prerequisites:

  - Has successfully subscribed to the PDND Infrastructure.
  - Has created a new `Client interop api` to interact with the Interoperability API. Upon creation, it has been assigned a ``client_id`` by the PDND Platform.
  - Has registered a key pair associated with the `Client interop api`.

Voucher for Interoperability API Flow
"""""""""""""""""""""""""""""""""""""""

.. _fig_VoucherIssuance_InteroperabilityAPI_Flow:
.. plantuml:: plantuml/pdnd-voucher-issuance-interoperability.puml
    :width: 80%
    :alt: The figure illustrates the Voucher Issuance for Interoperability API - Detailed flow.
    :caption: `Voucher Issuance for Interoperability API - Detailed flow. <https://www.plantuml.com/plantuml/svg/ZP11ozf048Rl-ok6UD7GqFOg4WmH8L3Qq41FXR0cWrbCTjEPsQ3--heQr4CBtoLavXsUzs6tB9h43ptyShxfaA1Wzjes20aKLf3SYAGFfZToWQmib1ZfySFNIdjnrWy79AKExWnH79UQn3Hcr5RY-BVTiBdY-kkNT9axotv00aURps6RlgKbkScqIAivYc1HJ8uk2c1y0GF_H-QbWxmt60eYq0pvNg5juIRmiBX9xBxluXWMsTKJ_eyHFexCLOjn5Yga2MacPjMBcE-JDAlMpqVvYNyyii0oYfgxHMtQAFe4pr4p8mNclxUrN4PyH4VILkPvfHHP9mXkGhe9mEARENPI6djI07c7pOc3rFr8gQnAaZJVhrzMF3hB6BHqqo1pBUw4iqFuVI_6ysW8kJOs56_Hjdxe_m80>`_


.. .. figure:: ../../images/Low-Level-Flow-AuthenticSource-Voucher-Issuance-InteroperabilityAPI.svg
..   :figwidth: 100%
..   :align: center
..   :target: https://www.plantuml.com/plantuml/svg/TP51ozf048Rl-ok6UD7GqFOg4WmH8L3Qq41FXR36mIp6tNHcLjHVtrqDwk7xBY4px_Ay3xjh5atYJuCI8mF27-Ux7WagPgzjXv11PGN9ZKXwPmOZLoZgIYdjnLb_sY4fjNCNIDAq3YJJcL5RITE_TiNcXillt_9vwIpxKw0wMdsDs_mjhScTpHvfCKK9pAgpewi265_0oFzLUEcX70p6WWGqGxbLQFSG11uMGMBpSvEcC2jkdl0pHlmuCZSjnbbeaCv84x5eNiHoc-L5itnUoc_yvv45vadItIrQiq-IB_0SDJDIP7wyRUKwuYCwK12QveLIP9qWkA0H163smnnwgOqzAe2on-x8KUf-IAcYoRAyt2vVLZmwonYrTDSXSolkY9D3_7qlnije2BarDXQl0pOy_dy0

..   Voucher Issuance for Interoperability API - Detailed flow

**Step 1 (Voucher Request)**: The Participant creates a Voucher Request and sends it to the PDND Authorization Server.

.. code-block:: http
  :caption: Non-normative example of the Voucher Request
  :name: code_VoucherIssuance_InteroperabilityAPI_Flow_Request

  POST /authorization-server/token HTTP/1.1
  Host: interop.pagopa.it
  Content-Type: application/x-www-form-urlencoded

  grant_type=client_credentials&
  client_id=5a3c7f28-91b9-4c4e-89a9-6e2f85d9262b&
  client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&
  client_assertion=eyJhbGciOiJFUzI1NiIsImtpZCI6IjlhNGQ4ZTNmLThiN2QtNGM5OC05MjZmLTI3NDVjNmIxZjgzMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI1YTNjN2YyOC05MWI5LTRjNGUtODlhOS02ZTJmODVkOTI2MmIiLCJzdWIiOiI1YTNjN2YyOC05MWI5LTRjNGUtODlhOS02ZTJmODVkOTI2MmIiLCJhdWQiOiJpbnRlcm9wLnBhZ29wYS5pdC9hdXRob3JpemF0aW9uLXNlcnZlciIsImV4cCI6MTczMzIzMzUwMCwiaWF0IjoxNzMzMjMyMzAwLCJqdGkiOiJkMmM5YTdiNC0zZTgxLTRkMjctYjZmNy01MWE4YzlmMGEzYzYifQ.YDX7ekvvY3gPHTfZeqa3IcurU7kNBZPy3OHAdljdXSFLoC5cVVyIzl43aMbwLouI43ylxWktaf0-pXabmye1qA

.. code-block:: json
  :caption: Non-normative example of the ``client_assertion`` JOSE header
  :name: code_VoucherIssuance_InteroperabilityAPI_Flow_ClientAssertion_Header

  {
      "alg": "ES256",
      "kid": "9a4d8e3f-8b7d-4c98-926f-2745c6b1f832",
       "typ": "JWT"
  }

.. code-block:: json
  :caption: Non-normative example of the ``client_assertion`` payload
  :name: code_VoucherIssuance_InteroperabilityAPI_Flow_ClientAssertion_Payload

  {
      "iss": "5a3c7f28-91b9-4c4e-89a9-6e2f85d9262b",
      "sub": "5a3c7f28-91b9-4c4e-89a9-6e2f85d9262b",
      "aud": "https://interop.pagopa.it/authorization-server",
      "exp": 1733233500,
      "iat": 1733232300,
      "jti": "d2c9a7b4-3e81-4d27-b6f7-51a8c9f0a3c6"
  }

Upon the receipt of the Voucher Request, the PDND Authorization Server MUST perform the following checks on the Voucher Request body parameters:

  - The claim ``client_assertion_type`` is set to ``urn:ietf:params:oauth:client-assertion-type:jwt-bearer``.
  - The claim ``grant_type`` is set to ``client_credentials``.

The PDND Authorization Server MUST also validate the ``client_assertion`` JWT as follows:

  Header:

  - Ensure that the ``typ`` claim is present and that its value is ``JWT``.

  Signature:

  - Obtain the Participant's public key corresponding to the ``kid`` header parameter, by interacting with the PDND Interoperability API.
  - Validate the signature of the JWT using the retrieved Participant's public key and the algorithm specified by the ``alg`` header parameter.

  Payload:

  - The ``iss`` and ``sub`` claims MUST identify a Client registered in the PDND Infrastructure.
  - The ``aud`` claim MUST represent the PDND Authorization Server.


**Step 2 (Voucher Issuance)**: In case of successful checks, the PDND Authorization Server issues a Voucher, which is included in the Voucher Response to the Participant.

.. code-block:: http
  :caption: Non-normative example of the Voucher Response
  :name: code_VoucherIssuance_InteroperabilityAPI_Flow_Response

  HTTP/1.1 200 OK
  Content-Type: application/json
  Cache-Control: no-store

  {
    "access_token": "eyJhbGciOiJFUzI1NiIsImtpZCI6ImI4MzlmNGM3LTFlNWQtNGE4YS05ZmM2LTcyZDNiN2YwOTFlYyIsInR5cCI6ImF0K2p3dCJ9.eyJpc3MiOiJpbnRlcm9wLnBhZ29wYS5pdCIsInN1YiI6IjVhM2M3ZjI4LTkxYjktNGM0ZS04OWE5LTZlMmY4NWQ5MjYyYiIsImF1ZCI6Imh0dHBzOi8vaW50ZXJvcC5wYWdvcGEuaXQvYXBpL3YxIiwiZXhwIjoxNzMzMjM2NjgwLCJuYmYiOjE3MzMyMzMxNTgsImlhdCI6MTczMzIzMzA4MCwianRpIjoiZjg3ZTJkNWItOWY2NS00ZjBmLThhZDQtOTJlNThlNmIxM2M3IiwiY2xpZW50X2lkIjoiNWEzYzdmMjgtOTFiOS00YzRlLTg5YTktNmUyZjg1ZDkyNjJiIn0.SKDDap16Ubi6gYwpKVdBcuhmhF_XnGiHeoxkF8F4IAualYORu_TxnDZqeP_RCcBAxSRkJTFbMihPCLA7DoRQOw",
    "token_type": "Bearer",
    "expires_in": 3600
  }

.. code-block:: json
  :caption: Non-normative example of the ``access_token`` JOSE header
  :name: code_VoucherIssuance_InteroperabilityAPI_Flow_AccessToken_Header

  {
    "alg": "ES256",
    "kid": "b839f4c7-1e5d-4a8a-9fc6-72d3b7f091ec",
    "typ": "at+jwt"
  }

.. code-block:: json
  :caption: Non-normative example of the ``access_token`` payload
  :name: code_VoucherIssuance_InteroperabilityAPI_Flow_AccessToken_Payload

  {
    "iss": "https://interop.pagopa.it",
    "sub": "5a3c7f28-91b9-4c4e-89a9-6e2f85d9262b",
    "aud": "https://interop.pagopa.it/api/v1",
    "exp": 1733236680,
    "nbf": 1733233158,
    "iat": 1733233080,
    "jti": "f87e2d5b-9f65-4f0f-8ad4-92e58e6b13c7",
    "client_id": "5a3c7f28-91b9-4c4e-89a9-6e2f85d9262b"
  }


PDND Authorization Server Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The PDND Authorization Server Endpoint issues Vouchers to Participants. These Vouchers allow Consumers to access e-Service resources and enable Participants to interact with the Interoperability API.

PDND Voucher Request
"""""""""""""""""""""

The request to the PDND Authorization Server Endpoint adheres to the Client Credentials Grant flow specified in :rfc:`6749`. The client authenticates itself by presenting a JWT-based client assertion as defined in :rfc:`7521` and :rfc:`7523`.

Following the specifications above, the request MUST be an HTTP POST request with a body encoded in ``application/x-www-form-urlencoded`` format.

The Voucher Request MUST include the following HTTP header parameters (unless otherwise specified):

.. list-table::
  :widths: 20 60 20
  :header-rows: 1

  * - **Parameter**
    - **Description**
    - **Reference**
  * - **DPoP**
    - DPoP proof JWT, to comply with the ``REST_JWS_2021_POP`` security pattern. It is mandatory only if the requested Voucher is for e-Service (i.e., not for Interoperability API) and follows the ``POP_DPoP`` implementation.
    - [:rfc:`9449`], [`PDND`_]

The Voucher Request MUST include the following body parameters:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parameter**
    - **Description**
    - **Reference**
  * - **client_id**
    - The unique identifier of the Participant Client, assigned by the PDND.
    - [:rfc:`6749`], [:rfc:`7521`], [:rfc:`7523`], [`PDND`_]
  * - **client_assertion**
    - A JWT representing the client assertion.
    - [:rfc:`7521`], [:rfc:`7523`], [`PDND`_]
  * - **client_assertion_type**
    - MUST be set to ``urn:ietf:params:oauth:client-assertion-type:jwt-bearer``.
    - [:rfc:`7521`], [:rfc:`7523`]
  * - **grant_type**
    - MUST be set to ``client_credentials``.
    - [:rfc:`6749`], [:rfc:`7523`]

The ``client_assertion`` JWT MUST include the following JOSE header parameters:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parameter**
    - **Description**
    - **Reference**
  * - **alg**
    - A digital signature algorithm identifier.
    - [:rfc:`7515`]
  * - **kid**
    - Unique identifier of the JWK used by the Participant to sign the ``client_assertion``.
    - [:rfc:`7515`]
  * - **typ**
    - MUST be set to ``JWT``.
    - [:rfc:`7515`], [:rfc:`7519`]

The ``client_assertion`` JWT MUST include the following payload claims (unless otherwise specified):

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **iss**
    - MUST be set to the same value as ``client_id``.
    - [:rfc:`7523`]
  * - **sub**
    - MUST be set to the same value as ``client_id``.
    - [:rfc:`7523`]
  * - **aud**
    - The identifier of the PDND Authorization Server Endpoint.
    - [:rfc:`7523`]
  * - **exp**
    - UNIX timestamp representing the JWT expiration time.
    - [:rfc:`7523`]
  * - **nbf**
    - UNIX timestamp representing the JWT first validity time (optional).
    - [:rfc:`7519`]
  * - **iat**
    - UNIX timestamp representing the JWT issuance time.
    - [:rfc:`7523`]
  * - **jti**
    - Unique identifier of the JWT to prevent replay attacks.
    - [:rfc:`7523`]
  * - **purposeId**
    - The identifier of the purpose registered in the PDND Platform, associated with the intended e-Service. It is mandatory only if the requested Voucher is for e-Service (i.e., not for Interoperability API).
    - [`MODI`_], [`PDND`_]
  * - **digest**
    - JSON object containing the digest of the ``TrackingEvidence`` JWT. It is mandatory only if the requested Voucher is for e-Service (i.e., not for Interoperability API), and when complying with ``AUDIT_REST_02`` or the ``POP_TPoP`` implementation. If present, it MUST contain the following claims:

      - **alg**: JSON string representing the hashing algorithm;
      - **value**: JSON string representing the value of the digest.
    - [`MODI`_]

PDND Voucher Response
"""""""""""""""""""""""

The Voucher Response MUST include the following body parameters:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parameter**
    - **Description**
    - **Reference**
  * - **access_token**
    - A JWT representing the access token issued by the PDND Authorization Server Endpoint.
    - [:rfc:`6749`], [:rfc:`9449`], [`PDND`_]
  * - **token_type**
    - It MUST be set to:

      - ``DPoP`` in case of Voucher for e-Service following the ``POP_DPoP`` implementation;
      - ``Bearer`` in case of Voucher for Interoperability API, or Voucher for e-Service following the ``POP_TPoP`` implementation.
    - [:rfc:`6749`], [:rfc:`9449`]
  * - **expires_in**
    - Number that represents the lifetime of the access token in seconds as a positive integer.
    - [:rfc:`6749`], [:rfc:`9449`]

The ``access_token`` JWT MUST include the following JOSE header parameters:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parameter**
    - **Description**
    - **Reference**
  * - **alg**
    - A digital signature algorithm identifier.
    - [:rfc:`7515`]
  * - **kid**
    - Unique identifier of the JWK used by the PDND Authorization Server Endpoint to sign the ``access_token``.
    - [:rfc:`7515`]
  * - **typ**
    - MUST be set to ``at+jwt``.
    - [:rfc:`9068`]

The ``access_token`` JWT MUST include the following payload claims (unless otherwise specified):

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **iss**
    - The identifier of the PDND Authorization Server.
    - [:rfc:`7519`], [:rfc:`9068`]
  * - **sub**
    - The identifier of the Participant, corresponding to the ``client_id`` body parameter in the Voucher Request.
    - [:rfc:`7519`], [:rfc:`9068`]
  * - **aud**
    - The identifier of the e-Service.
    - [:rfc:`7519`], [:rfc:`9068`]
  * - **exp**
    - UNIX timestamp representing the JWT expiration time.
    - [:rfc:`7519`], [:rfc:`9068`]
  * - **nbf**
    - UNIX timestamp representing the JWT first validity time (optional).
    - [:rfc:`7519`]
  * - **iat**
    - UNIX timestamp representing the JWT issuance time.
    - [:rfc:`7519`], [:rfc:`9068`]
  * - **jti**
    - Unique identifier of the JWT to prevent replay attacks.
    - [:rfc:`7519`], [:rfc:`9068`]
  * - **client_id**
    - MUST correspond to the ``client_id`` contained in the Voucher Request.
    - [:rfc:`7519`], [:rfc:`8963`], [:rfc:`9068`], [`PDND`_]
  * - **purposeId**
    - MUST correspond to the value of the ``purposeId`` claim contained in the Voucher Request. It is mandatory only if the requested Voucher is for e-Service (i.e., not for Interoperability API).
    - [`MODI`_], [`PDND`_]
  * - **digest**
    - MUST correspond to the value of the ``digest`` object contained in the Voucher Request. It is mandatory only when complying with ``AUDIT_REST_02`` or the ``POP_TPoP`` implementation.
    - [`MODI`_]
  * - **cnf**
    - It MUST contain a **jkt** claim being JWK SHA-256 Thumbprint Confirmation Method. The value of the *jkt* member MUST be the base64url encoding (as defined in [:rfc:`7515`]) of the JWK SHA-256 Thumbprint of the DPoP public key (in JWK format) to which the Access Token is bound. It is mandatory only when complying with the ``POP_DPoP`` implementation.
    - [:rfc:`9449`. Section 6.1] and [:rfc:`7638`].

If any errors occur during the validation of the Voucher Request, the PDND Authorization Server Endpoint MUST return an error response as defined in :rfc:`6749#section-5.2`. The response MUST use ``application/json`` as the content type and MUST include the following parameters:

  - ``error``: The error code.
  - ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

.. code-block:: http
  :caption: Non-normative example of a Voucher Error Response
  :name: code_VoucherIssuance_Endpoint_AuthorizationServer_Error

  HTTP/1.1 400 Bad Request
  Content-Type: application/json
  Cache-Control: no-store

  {
    "error": "invalid_request",
    "error_description": "The client_assertion_type parameter is missing."
  }


The following table lists the HTTP Status Codes and related error codes that MUST be supported for the error response:

.. list-table::
  :class: longtable
  :widths: 20 20 60
  :header-rows: 1

  * - **Status Code**
    - **Error Code**
    - **Description**
  * - ``400 Bad Request``
    - ``invalid_request``
    - The request cannot be fulfilled because it is missing required parameters, contains invalid parameters, or is otherwise malformed [:rfc:`6749#section-5.2`].
  * - ``400 Bad Request``
    - ``invalid_grant``
    - The request cannot be fulfilled because the provided grant (i.e., ``client_assertion``) is expired, revoked, already used, or otherwise malformed [:rfc:`6749#section-5.2`].
  * - ``400 Bad Request``
    - ``unsupported_grant_type``
    - The request cannot be fulfilled because the provided grant type is not supported by the PDND Authorization Server [:rfc:`6749#section-5.2`].
  * - ``400 Bad Request``
    - ``invalid_scope``
    - The request cannot be fulfilled because the provided ``purposeId`` is invalid, unknown, malformed, or not associated to the Client [:rfc:`6749#section-5.2`].
  * - ``400 Bad Request``
    - ``invalid_dpop_proof``
    - The request cannot be fulfilled because it contains an invalid *DPoP proof* [:rfc:`9449#section-5`].
  * - ``401 Unauthorized``
    - ``invalid_client``
    - The request cannot be fulfilled because Client Authentication failed (i.e., the ``client_assertion`` is malformed, incorrectly signed, missing, or unverifiable) [:rfc:`6749#section-5.2`].
  * - ``500 Internal Server Error``
    - ``server_error``
    - The request cannot be fulfilled because the PDND Authorization Server encountered an internal problem.
  * - ``503 Service Unavailable``
    - ``temporarily_unavailable``
    - The request cannot be fulfilled because the PDND Authorization Server is temporarily unavailable (e.g., due to maintenance or overload).

Key Retrieval
----------------------

PDND Authorization Server Keys
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_KeyRetrieval_PDND_Flow:
.. plantuml:: plantuml/pdnd-key-retrieval.puml
    :width: 80%
    :alt: The figure illustrates the Key Retrieval for PDND Keys - Detailed flow.
    :caption: `Key Retrieval for PDND Keys - Detailed flow. <https://www.plantuml.com/plantuml/svg/RSx1IWCn58NXVPxYK7U1-01Tb1Qw40ILp6BMQNl4q4nIRsvc79_UgOWAkZsN_-DkgmRHDYJSSuQdIkGO4XoUzWzxer4J_p-PqBJaDXmenXpA6wozxjRYPlVUX0QuB7Gynal8YfMrjnDJSkTSfcpj2g6YDymdBF6t86MC9yfLkIkPyvxJN-Xnr_G5dhKqEH8TPQHyaRxxCNtdDlqQdg-DLV5SvFDrd3bNOthdDhvR_vgsIzc6z040>`_


.. .. figure:: ../../images/Low-Level-Flow-AuthenticSource-KeyRetrieval-PDND.svg
..   :figwidth: 100%
..   :align: center
..   :target: https://www.plantuml.com/plantuml/svg/PS_1IWCn58NXVPxYK7U1-01Tb1Pc8GWgcSMiq_Q8eMbIRsvc79_UgOWAtHxuF-xTLWsYxPoCHat48sTugaIE8S7XfNlgZ0bDIsxdFSMOVVc0jTVTMjpjFflG09T5YOTu2LcnilP-OahkbCkKhLqXL0o6-OWb_XMaZF58kIeF9NFkEDr2pxkcR_2ifSc1w2aZvOVq_P_fUxSPrl1yRwoAroBVf-F4kHepEBVn_VhVj5tAvUil

..   Key Retrieval for PDND Keys - Detailed flow

**Step 1 (Keys Request)**: The Provider requests for the keys used by the PDND to sign Vouchers.

.. code-block:: http
  :caption: Non-normative example of the Keys Request
  :name: _code_KeyRetrieval_PDND_Flow_Request

  GET /.well-known/jwks.json HTTP/1.1
  Host: interop.pagopa.it

**Step 2 (Keys Response)**: The .well-known Endpoint returns the list of keys used by the PDND to sign Vouchers, as a ``JWK Set`` [:rfc:`7517`].

.. code-block:: http
  :caption: Non-normative example of the Keys Response
  :name: _code_KeyRetrieval_PDND_Flow_Response

  HTTP/1.1 200 OK
  Content-Type: application/json

  {
    "keys": [
      {
        "kty": "RSA",
        "n": "qU2Bp7xgkXBQI2w2PZ5LZGo34TIjoir-ul0x4jZ_d9hN6q...",
        "e": "AQAB",
        "alg": "ES256",
        "kid": "b839f4c7-1e5d-4a8a-9fc6-72d3b7f091ec"
      },
      {
        "kty": "RSA",
        "n": "05VukHBwiE1W_kgUS0zkOyHCrRivgw5cfSTmcvD_phieEY...",
        "e": "AQAB",
        "alg": "ES256",
        "kid": "9432c16b-7aae-49df-b9c4-ea61b556652b"
      }
    ]
  }

PDND Authorization Server .well-known Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The .well-known Endpoint is part of the PDND Infrastructure and used to retrieve the public keys used by the PDND Authorization Server to sign the Vouchers.

PDND Authorization Server Keys Request
""""""""""""""""""""""""""""""""""""""

The Keys Request is a ``GET`` HTTP request sent to the .well-known Endpoint. This endpoint allows Participants to retrieve the public keys necessary to verify digital signatures on Vouchers issued by the PDND Authorization Server.

PDND Authorization Server Keys Response
"""""""""""""""""""""""""""""""""""""""

The .well-known Endpoint responds with a ``200 OK`` status code and a ``JWK Set`` [:rfc:`7517`] containing the public keys employed by the PDND Authorization Server to sign Vouchers.

If any errors occur during the retrieval of the keys, the .well-known Endpoint MUST return an error response. The response MUST use ``application/json`` as the content type and MUST include the following parameters:

  - ``error``: The error code.
  - ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

.. code-block:: http
  :caption: Non-normative example of a Keys Error Response
  :name: code_KeyRetrieval_Endpoint_WellKnown_Error

  HTTP/1.1 500 Internal Server Error
  Content-Type: application/json

  {
    "error": "server_error",
    "error_description": "The server encountered an unexpected error."
  }


The following table lists the HTTP Status Codes and related error codes that MUST be supported for the error response:

.. list-table::
  :class: longtable
  :widths: 20 20 60
  :header-rows: 1

  * - **Status Code**
    - **Error Code**
    - **Description**
  * - ``500 Internal Server Error``
    - ``server_error``
    - The request cannot be fulfilled because the .well-known Endpoint encountered an internal problem.
  * - ``503 Service Unavailable``
    - ``temporarily_unavailable``
    - The request cannot be fulfilled because the .well-known Endpoint is temporarily unavailable (e.g., due to maintenance or overload).

Participants' Keys
^^^^^^^^^^^^^^^^^^

Participants' Key Retrieval Prerequisites
"""""""""""""""""""""""""""""""""""""""""

The **Participant** who requests the key MUST comply with the following prerequisites:

    - Has successfully subscribed to the PDND Infrastructure (as per R1).
    - Has created a new `Client api interop` to interact with the PDND Interoperability API. Upon creation, it has been assigned a ``client_id`` by the PDND Platform.
    - Has registered a key pair associated with the `Client api interop`.
    - Has obtained a valid Voucher to query the PDND Interoperability API, related to the specific `Client api interop`.

Participants' Key Retrieval Flow
""""""""""""""""""""""""""""""""

.. _fig_KeyRetrieval_Participant_Flow:
.. plantuml:: plantuml/pdnd-key-retrieval-participant.puml
    :width: 80%
    :alt: The figure illustrates the Key Retrieval for Participant's Key - Detailed flow.
    :caption: `Key Retrieval for Participant's Key - Detailed flow. <https://www.plantuml.com/plantuml/svg/fSp1IiGm4CRnUvxY8nw4mBx07fOjRS4YQDcpbxITrM7J92OJjJwz5SGAWXUlC__lTynYavJPuPOMd4WIqujrsA5Vxpnoj5wo4XP7VoVA5Wc-p0CbfORm1cFwvgun1bVLUqcaWBZrqCPqNYY5ICaEx5WML7rdZ8RDw1Jv2QloJMtJJ_4cU5eQUlsDtbT5db0x9YzVMDrkMjtk3jt-HC-5ik0S4dx8rncn38v7N6Xvy6D8YN8CVcB_20d8aKO-hs-jBpnfhQ2wtQ5kz_ynZkIdChiF>`_


.. .. figure:: ../../images/Low-Level-Flow-AuthenticSource-KeyRetrieval-Participant.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/fSp1IlGm5CNnVPxYa6_nGQ0lC8jXIbkm25fcxIPjx-XbqYGcDsfzUYk85Low_f_pEsMnIShYbB0umYsjE9CafXVhK67OAayShPUib2qIV5b6IagDuGt63ErTQmp-rUybaGBYleSsflT2AKHATcJ7ig8UUcCqR4QloC_Ob6zgltwADy7JsjBhR_I-BlA4nZ5v-SAQRjUQhZhsXpCz5yg2IqZu8V_FY6LqFE5AwuEVGagKO_0p-qT8G8uqyMNBMbzvrbf1zTMnwGv_CKxavxAu3m00

..     Key Retrieval for Participant's Key - Detailed flow

**Step 1 (Key Request)**: The Participant requests for the key used by another Participant, corresponding to a specific ``kid``, to the PDND Interoperability API.

.. code-block:: http
    :caption: Non-normative example of the Key Request
    :name: _code_KeyRetrieval_Participant_Flow_Request

    GET /keys/c7e3d6a4-5b99-4298-9b84-d8f3a61279f1 HTTP/1.1
    Host: interop.pagopa.it
    Authorization: Bearer eyJhbGciOiJFUzI1NiIsImtpZCI6ImI4MzlmNGM3LTFlNWQtNGE4YS05ZmM2LTcyZDNiN2YwOTFlYyIsInR5cCI6ImF0K2p3dCJ9.eyJpc3MiOiJpbnRlcm9wLnBhZ29wYS5pdCIsInN1YiI6IjVhM2M3ZjI4LTkxYjktNGM0ZS04OWE5LTZlMmY4NWQ5MjYyYiIsImF1ZCI6Imh0dHBzOi8vaW50ZXJvcC5wYWdvcGEuaXQvYXBpL3YxIiwiZXhwIjoxNzMzMjM2NjgwLCJuYmYiOjE3MzMyMzMxNTgsImlhdCI6MTczMzIzMzA4MCwianRpIjoiZjg3ZTJkNWItOWY2NS00ZjBmLThhZDQtOTJlNThlNmIxM2M3IiwiY2xpZW50X2lkIjoiNWEzYzdmMjgtOTFiOS00YzRlLTg5YTktNmUyZjg1ZDkyNjJiIn0.SKDDap16Ubi6gYwpKVdBcuhmhF_XnGiHeoxkF8F4IAualYORu_TxnDZqeP_RCcBAxSRkJTFbMihPCLA7DoRQOw

**Step 2 (Key Response)**: The Interoperability API Endpoint returns the requested key, as a ``JWK`` [:rfc:`7517`].

.. code-block:: http
  :caption: Non-normative example of the Key Response
  :name: _code_KeyRetrieval_Participant_Flow_Response

  HTTP/1.1 200 OK
  Content-Type: application/json

  {
    "kty": "EC",
    "key_ops": [
      "sign"
    ],
    "kid": "b839f4c7-1e5d-4a8a-9fc6-72d3b7f091ec",
    "crv": "P-256",
    "x": "huyXIQNv902oLspX4_zonC94G6yEln6lsdm-1wM732o",
    "y": "I9PDEawWHqaFDGx1ZkNk-2PV6WdpcaH3AfObBSLihgw"
  }


.. note::
  The Interoperability API includes an event notification endpoint that alerts subscribed Participants about changes within the PDND Infrastructure. Among these notifications, the ``/events/keys`` endpoint provides updates on modifications to cryptographic material, such as additions or deletions of keys. By leveraging this mechanism, Participants can implement a periodic polling strategy to retrieve all changed keys and update their local cache. This eliminates the need to request each key individually during the workflow.

PDND Interoperability API Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Interoperability API Endpoint is part of the PDND Infrastructure and used to retrieve the public keys of other parties enrolled in the PDND.

PDND Interoperability API Key Request
"""""""""""""""""""""""""""""""""""""

The Key Request is a ``GET`` HTTP request sent to the ``/keys/<kid>`` API. This request is used to retrieve a specific key identified by its unique ``kid``.

The Key Request MUST include the following HTTP header parameters:

.. list-table::
  :widths: 20 60 20
  :header-rows: 1

  * - **Parameter**
    - **Description**
    - **Reference**
  * - **Authorization**
    - Voucher released by the PDND Authorization Server.
    - [:rfc:`9449`]

PDND Interoperability API Key Response
""""""""""""""""""""""""""""""""""""""

In case a public key with the provided ``kid`` exists, the Interoperability API Endpoint responds with a ``200 OK`` status code and a ``JWK`` [:rfc:`7517`] representing that key.

If any errors occur during the retrieval of the key, the Interoperability API Endpoint MUST return an error response, whose structure depends on the nature of the error.

In case of authentication issues (i.e., invalid or expired Voucher), the response MUST adhere to the error format defined in :rfc:`6750#section-3`, with specific reference to the use of the ``WWW-Authenticate`` header parameter.

.. code-block:: http
    :caption: Non-normative example of a Key Error Response in case of 401 errors
    :name: code_KeyRetrieval_Endpoint_InteroperabilityAPI_Error_401

    HTTP/1.1 401 Unauthorized
    WWW-Authenticate: Bearer error="invalid_token", error_description="The access token expired"

For all other errors, the response MUST adhere to the error format defined in :rfc:`6749#section-5.2`. The response MUST use ``application/json`` as the content type and MUST include the following parameters:

    - ``error``: The error code.
    - ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

.. code-block:: http
    :caption: Non-normative example of a Key Error Response in case of other errors
    :name: code_KeyRetrieval_Endpoint_InteroperabilityAPI_Error_Others

    HTTP/1.1 400 Bad Request
    Content-Type: application/json

    {
        "error": "invalid_request",
        "error_description": "The kid parameter is missing."
    }


The following table lists the HTTP Status Codes and related error codes that MUST be supported for the error response:

.. list-table::
  :class: longtable
  :widths: 20 20 60
  :header-rows: 1

  * - **Status Code**
    - **Error Code**
    - **Description**
  * - ``400 Bad Request``
    - ``invalid_request``
    - The request cannot be fulfilled because it is missing required parameters, contains invalid parameters or is otherwise malformed [:rfc:`6750#section-3.1`].
  * - ``401 Unauthorized``
    - ``invalid_token``
    - The request cannot be fulfilled because the Voucher is expired, revoked, malformed, or otherwise invalid [:rfc:`6750#section-3.1`].
  * - ``404 Not Found``
    - ``not_found``
    - The request cannot be fulfilled because no public key corresponding to the provided ``kid`` has been found.
  * - ``500 Internal Server Error``
    - ``server_error``
    - The request cannot be fulfilled because the Interoperability API Endpoint encountered an internal problem.
  * - ``503 Service Unavailable``
    - ``temporarily_unavailable``
    - The request cannot be fulfilled because the Interoperability API Endpoint is temporarily unavailable (e.g., due to maintenance or overload).

e-Service Usage
-----------------

e-Service Usage Prerequisites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **Consumer** MUST comply with the following prerequisites:

  - Has obtained a valid Voucher to interact with the intended e-Service, related to a specific `Client e-service`.

The **Provider** MUST comply with the following prerequisites:

  - Has created a new key ring associated with the specific e-Service.
  - Has registered a key pair associated with the key ring.

.. note::
  The Provider's key ring is the counterpart to the Client on the Consumer's side. It stores cryptographic material, allowing Consumers to verify the integrity of responses from Providers.


e-Service Usage Flow
^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_Usage_Flow:
.. plantuml:: plantuml/pdnd-eservice-usage.puml
    :width: 80%
    :alt: The figure illustrates the e-Service Usage - Detailed flow.
    :caption: `e-Service Usage - Detailed flow. <https://www.plantuml.com/plantuml/svg/ZP31RjGm48RlVegHUm5BAo6EFQ2kaYuK8RfAjd1SkSwGM9jumdYyPVlqE4sxiAfQzHB5zlpVVFelebYMDFI0Ynfvxnt2JRGjAl7IuxDRPPDGICCjibAtz0UCAIZ4D20R0sTNU-A30XWpr3i_sY2WZRbU9kcWw3q6CKQ3ZL2i58O6CkA9iow_bnDZUPyONs9C7s9_RyLJWCaD-P6uh9yHcVQ-cSs-KC13YNSlWIkCbDZXARFwZrci5f-ArVcQCGCGllxSm9tFoUZRO2KnmZkjwwU3rk-F4IWOhI2KQrh3o4I_vgUgFeVIYitBVoUCClD-K7BTL2y7oY7ADja3phxvjfFFZ1WKGD6Xsu7M4rBhIV9X-cqXwnp6k1NQOJW9qoXm7Vh3BABrygQyscohotgp_V0nJmAyXl-tOCFMxNneBwVwWyE7w75D_dcRvx7C4ycgNiojFhQ63JHMhBh88sde_m80>`_


.. .. figure:: ../../images/Low-Level-Flow-AuthenticSource-Usage.svg
..     :figwidth: 100%
..     :align: center
..     :target: https////www.plantuml.com/plantuml/svg/ZP1HRzCm4CVV_IbEtWjOgeHut0DQbQmmX5YLTF1OUSwHM4ryuNpkw3uzph8LAZJK5ykMx_-xd_vNKInB6debNde4NDJ8U-yGxg9jKIcRX48Qxf6LkgTVO4n18QO1sHYukDaJ7nJ0c27U-T460MtCxJ991qNlCOWn6co4OgKmD90HBvnr-RMS6Cl7nFWQOpg8_QCLJm4cD-HduhB-XyYqzyrizea27afyU0rSOQJ43a-PrL_COhNuKAmkrumPWF3v-mOUV4v6tmOhYH7UQ5s_FBH-Uun0mMW5eLpJ6aOc-Z5_LVKbb5PiNlupOPIPzusIwwPwEL0EKRR97d3nnRUTV6J4e02A3jqEj9wGMa-IJzFdXQnp6EDMQ8VX94oZm6te3xE8rikxycQphQxhpVRT-pm9y3_ydmKRjcxdGtizrHySFaMFQ_BbFCzZcIUILRsOMtrk3Hjeh5XrbKVIqFy6

..     e-Service Usage - Detailed flow

**Step 1 (Signature Preparation):** The Consumer prepares a JWT (``Signature``) containing the signed headers of the message, to ensure integrity.

.. code-block:: json
    :caption: Non-normative example of the ``Signature`` header
    :name: _code_Usage_Flow_Signature_Header

    {
        "alg": "ES256",
        "kid": "d4c3b2a1-9876-5432-10fe-dcba98765432",
        "typ": "JWT"
    }

.. code-block:: json
    :caption: Non-normative example of the ``Signature`` payload
    :name: _code_Usage_Flow_Signature_Payload

    {
        "iss": "9a8b7c6d-e5f4-g3h2-i1j0-klmnopqrstuv",
        "sub": "9a8b7c6d-e5f4-g3h2-i1j0-klmnopqrstuv",
        "aud": "https://erogatore.example/ente-example/v1",
        "iat": 1733397840,
        "nbf": 1733401628,
        "exp": 1733401440,
        "jti": "d3f7b2c9-274a-42b7-8f8d-2e9d8b1734b0",
        "signed_headers": [
            {"digest": "SHA-256=72e18bdddf13c911b4dd562ee21979a5c9f235c3a01bd1426e857d8c1a282f41"},
            {"content-type": "application/json"}
        ]
    }

.. note::
  Step 1 is required to comply with the ``INTEGRITY_REST_02`` security pattern.

**Step 2 (DPoP Proof for e-Service Endpoint)**: The Consumer MUST create a fresh DPoP Proof JWT following the instruction provided in the Section 4 of [:rfc:`9449`] for the token presentation to the e-Service Endpoint.

.. note::
  Step 2 is required only when complying with the ``POP_DPoP`` implementation.

**Step 3 (e-Service Request):** The Consumer sends an e-Service Request to the Provider, including the Voucher.

.. code-block:: http
    :caption: Non-normative example of the e-Service Request
    :name: _code_Usage_Flow_Request

    POST /ente-example/v1/hello/echo/ HTTP/1.1
    Host: erogatore.example
    Authorization: DPoP eyJhbGciOiJFUzI1NiIsImtpZCI6ImI4MzlmNGM3LTFlNWQtNGE4YS05ZmM2LTcyZDNiN2YwOTFlYyIsInR5cCI6ImF0K2p3dCJ9.eyJpc3MiOiJpbnRlcm9wLnBhZ29wYS5pdCIsInN1YiI6IjgyOTE0YjNmLTYwYjItNDUyOS1iNGQ2LTNkNGU2N2YwYTkzMyIsImF1ZCI6Imh0dHBzOi8vZXJvZ2F0b3JlLmV4YW1wbGUvZW50ZS1leGFtcGxlL3YxIiwiZXhwIjoxNzMzMDQyMTUwLCJuYmYiOjE3MzMwNDE5NDUsImlhdCI6MTczMzA0MTkyMCwianRpIjoiYzRmNWQ3ZTItYjdjOC00MGY2LTliNmEtZGM5YTRmNWFlYjU3IiwiY2xpZW50X2lkIjoiODI5MTRiM2YtNjBiMi00NTI5LWI0ZDYtM2Q0ZTY3ZjBhOTMzIiwicHVycG9zZUlkIjoiZDJiOWE2NTMtYzQ5Ny00NWM2LWI4ZjEtNWJkZjEyNGM5ZDNhIiwiZGlnZXN0Ijp7ImFsZyI6IlNIQTI1NiIsInZhbHVlIjoiOTkwOGQ5NGI4ZmViMjY4YzAzNzEwNmQ3Yzg5ZTcwNjBjMmNjMWY2YjJiNGViY2I4MDViZmVlNTNhNTM5MzA3YiJ9LCJjbmYiOnsiamt0IjoiMFpjT0NPUlpOWXktRFdwcXEzMGpaeUpHSFROMGQySGdsQlYzdWlndUE0SSJ9fQ.sGhaHEOfMTB7r4_8ZILM_a9eTBGawWn3kL-dxYoZggFIzyrXDOZcQWt0zr00lMk2iYAMWxS32e4cUedmAsBXGw
    DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6IkVDIiwia2V5X29wcyI6WyJzaWduIl0sImtpZCI6IjM5ZmE5NjBiLTc3M2YtNDllZi04YTBlLWU3NzNlOWI5N2FlOCIsImNydiI6IlAtMjU2IiwieCI6Imh1eVhJUU52OTAyb0xzcFg0X3pvbkM5NEc2eUVsbjZsc2RtLTF3TTczMm8iLCJ5IjoiSTlQREVhd1dIcWFGREd4MVprTmstMlBWNldkcGNhSDNBZk9iQlNMaWhndyJ9fQ.eyJqdGkiOiIyYzc2ZmNhMy1jYjRlLTQzMTItOGI2ZS05NzQ5NDYyZjQyMGQiLCJodG0iOiJQT1NUIiwiYXRoIjoiM2UwOGRlMWQwYTNkZjIzNWZjZmNjZjYyNjdmYTUwYTU5YmEyYTk1NTI2YzdjZTY3MDY1YjhlMjZkYmI5NDQ1MSIsImh0dSI6Imh0dHBzOi8vZXJvZ2F0b3JlLmV4YW1wbGUvZW50ZS1leGFtcGxlL3YxIiwiaWF0IjoxNzYyMjYyNjE2fQ.kvXh8H9B5DWCNlWyNB_PzRH217j1NHnIkE_55WnEixt2RbQTGrCS6AFAznREA85dzqwAAaHb_qHtDc5BR0lLmQ
    Agid-JWT-Signature: eyJhbGciOiJFUzI1NiIsImtpZCI6ImQ0YzNiMmExLTk4NzYtNTQzMi0xMGZlLWRjYmE5ODc2NTQzMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI5YThiN2M2ZC1lNWY0LWczaDItaTFqMC1rbG1ub3BxcnN0dXYiLCJzdWIiOiI5YThiN2M2ZC1lNWY0LWczaDItaTFqMC1rbG1ub3BxcnN0dXYiLCJhdWQiOiJodHRwczovL2Vyb2dhdG9yZS5leGFtcGxlL2VudGUtZXhhbXBsZS92MSIsImlhdCI6MTczMzM5Nzg0MCwibmJmIjoxNzMzNDAxNjI4LCJleHAiOjE3MzM0MDE0NDAsImp0aSI6ImQzZjdiMmM5LTI3NGEtNDJiNy04ZjhkLTJlOWQ4YjE3MzRiMCIsInNpZ25lZF9oZWFkZXJzIjpbeyJkaWdlc3QiOiJTSEEtMjU2PTcyZTE4YmRkZGYxM2M5MTFiNGRkNTYyZWUyMTk3OWE1YzlmMjM1YzNhMDFiZDE0MjZlODU3ZDhjMWEyODJmNDEifSx7ImNvbnRlbnQtdHlwZSI6ImFwcGxpY2F0aW9uL2pzb24ifV19.DpuBNo2UgQhL7WLin4mpdZrbIpQq3tPvCX6HfktkxG7L5mk6a8OK1Hg0mQcZfFi3gelS-aL9kFS-6MoSy4csBg
    Digest: SHA-256=72e18bdddf13c911b4dd562ee21979a5c9f235c3a01bd1426e857d8c1a282f41
    Agid-JWT-TrackingEvidence: eyJhbGciOiJFUzI1NiIsImtpZCI6ImQ0YzNiMmExLTk4NzYtNTQzMi0xMGZlLWRjYmE5ODc2NTQzMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI4MjkxNGIzZi02MGIyLTQ1MjktYjRkNi0zZDRlNjdmMGE5MzMiLCJhdWQiOiJodHRwczovL2Vyb2dhdG9yZS5leGFtcGxlL2VudGUtZXhhbXBsZS92MSIsImV4cCI6MTczMzA1MjYwMCwibmJmIjoxNzMzMDM2NDUwLCJpYXQiOjE3MzMwMzY0MDAsImp0aSI6ImE0YjVjNmQ3LWU4ZjktYWJjZC1lZjEyLTM0NTY3ODkwMTIzNCIsImRub25jZSI6NjUyODQyNDIxMzY4NSwicHVycG9zZUlkIjoiYjJjM2Q0ZTUtZjZnNy1oOGk5LWowazEtbG1ubzEyMzQ1Njc4IiwidXNlcklEIjoiYThiN2M2ZDUtZTRmMy1nMmgxLWk5ajAta2xtbm9wcXJzdHV2IiwibG9hIjoic3Vic3RhbnRpYWwifQ.bhb3f3aWEuK-bZWjyKRWrJ4hYUWhw2SQ-yRz0kUFjPQTVagjXuTqyhxsHO4KXeSX9SivgaLSvw4n9BeZa7APbQ
    Content-Type: application/json

    {
        "parameter1": "value1",
        "parameter2": "value2"
    }

The Provider MUST validate the DPoP proof [:rfc:`9449`].

.. note::
  DPoP proof validation is required only when complying with the ``POP_DPoP`` implementation.

The Provider MUST validate the Voucher as follows:

    Header:

      - Ensure that the ``typ`` claim is present and that its value is ``at+jwt``.

    Signature:

      - Retrieve the collection of public keys published at the .well-known endpoint. From this collection, select the public key whose identifier corresponds to the value of the ``kid`` header parameter in the Voucher.
      - Validate the signature of the ``access_token`` using the retrieved public key and the algorithm specified by the ``alg`` header parameter.

    Payload:

      - The ``iss`` claim MUST identify the domain of the PDND Authorization Server.
      - The ``sub`` claim MUST correspond to the ``client_id`` claim.
      - The ``aud`` claim MUST match the intended e-Service.
      - In case of ``POP_DPoP`` implementation, the ``cnf.jkt`` claim MUST correspond to the SHA-256 Thumbprint of the DPoP public key in the ``jwk`` claim in the DPoP proof.

.. note::
  If the Provider requires additional context about the request, it can interact with the PDND Interoperability API by passing the value of the ``purposeId`` as a parameter.

The Provider MUST validate the ``TrackingEvidence`` JWT as follows:

  Header:

    - Ensure that the ``typ`` claim is present and that its value is ``JWT``.

  Signature:

    - Obtains the Consumer's public key corresponding to the ``kid`` header parameter, by interacting with the PDND Interoperability API.
    - Validate the signature of the JWT using the retrieved Consumer's public key and the algorithm specified by the ``alg`` header parameter.

  Payload:

    - The ``iss`` claim MUST identify the Consumer Client.
    - The ``aud`` claim MUST identify the Provider.

In addition, the Provider MUST ensure that the hash of the ``TrackingEvidence`` JWT matches the value of the ``digest.value`` claim contained in the ``access_token`` payload.

.. note::
  The validation of the ``TrackingEvidence`` JWT is required only when complying with the ``AUDIT_REST_02`` security pattern or the ``POP_TPoP`` implementation.

The Provider MUST validate the ``Signature`` JWT as follows:

  Header:

    - Ensure that the ``typ`` claim is present and that its value is ``JWT``.

  Signature:

    - Validate the signature of the JWT using the retrieved Consumer's public key and the algorithm specified by the ``alg`` header parameter.

  Payload:

    - The ``iss`` and ``sub`` claims MUST identify the Consumer Client.
    - The ``aud`` claim MUST identify the Provider.

In addition, the Provider MUST validate the integrity of the e-Service Request, by checking that:

  - The ``signed_headers.content-type`` claim matches the value of the ``Content-Type`` HTTP header of the e-Service Request.
  - The ``signed_headers.digest`` claim matches the value of the digest of the payload of the e-Service Request, as well as the value of the ``Digest`` HTTP header of the e-Service Request.


If any of the previous checks fail, the Provider MUST reject the Request.

**Step 4 (e-Service Response):** Upon successful checks, the Provider provides the Consumer with the requested data. In The Response header MUST be present the JWT (``Signature``) to ensure integrity.

.. code-block:: http
  :caption: Non-normative example of the e-Service Response
  :name: _code_Usage_Flow_Response

  HTTP/1.1 200 OK
  Content-Type: application/json
  Agid-JWT-Signature: ew0KICAiYWxnIjogIkVTMjU2IiwNCiAgImtpZCI6ICJhMWY1YzhkMi00YjM3LTRlOTEtYjBkMi03OWUzZjBjNGE4ZWYiLA0KICAidHlwIjogIkpXVCINCn0.ew0KICAiaXNzIjogIjEyMzRhYmNkLWVmNTYtZ2g3OC1pOWowLWtsbW5vcHFyc3R3eCIsDQogICJzdWIiOiAiMTIzNGFiY2QtZWY1Ni1naDc4LWk5ajAta2xtbm9wcXJzdHd4IiwNCiAgImF1ZCI6ICJodHRwczovL2ZydWl0b3JlLmV4YW1wbGUvZW50ZS1leGFtcGxlL3YxIiwNCiAgImlhdCI6IDE3MzMzOTc4NDAsDQogICJuYmYiOiAxNzMzNDAxNjI4LA0KICAiZXhwIjogMTczMzQwMTQ0MCwNCiAgImp0aSI6ICI4ZTEyZjRiNy05YzNhLTRmODMtOWI4ZC01MWEyYzdmNmU5ZDQiLA0KICAic2lnbmVkX2hlYWRlcnMiOiBbDQogICAgew0KICAgICAgImRpZ2VzdCI6ICJTSEEtMjU2PTc5YTIwYTc0NDMzNjQyMDMwMTgzMDYwMGFkOWJkY2E5OTM1OTNmODc2MjA5YTAwNGI1OTliNTgzMDk1YjBhNjEiDQogICAgfSwNCiAgICB7DQogICAgICAiY29udGVudC10eXBlIjogImFwcGxpY2F0aW9uL2pzb24iDQogICAgfQ0KICBdDQp9.DpuBNo2UgQhL7WLin4mpdZrbIpQq3tPvCX6HfktkxG7L5mk6a8OK1Hg0mQcZfFi3gelS-aL9kFS-6MoSy4csBg
  Digest: SHA-256=79a20a744336420301830600ad9bdca993593f876209a004b599b583095b0a61

  {
    "requestedField1": "value1",
    "requestedField2": "value2",
    "requestedField3": "value3"
  }

The Consumer MUST validate the ``Signature`` JWT as follows:

  Header:

    - Ensure that the ``typ`` claim is present and that its value is ``JWT``.

  Signature:

    - Validate the signature of the JWT using the retrieved Provider's public key and the algorithm specified by the ``alg`` header parameter.

  Payload:

    - The ``iss`` and ``sub`` claims MUST identify the Provider.
    - The ``aud`` claim MUST identify the Consumer Client itself.

In addition, the Consumer MUST validate the integrity of the e-Service Response, by checking that:

  - The ``signed_headers.content-type`` claim matches the value of the ``Content-Type`` HTTP header of the e-Service Response.
  - The ``signed_headers.digest`` claim matches the value of the digest of the payload of the e-Service Response, as well as the value of the ``Digest`` HTTP header of the e-Service Response.

If any of the previous checks fail, the Consumer MUST reject the Response.

e-Service Endpoint
^^^^^^^^^^^^^^^^^^^^^^

e-Service Request
"""""""""""""""""""""

The e-Service Request MUST include the following HTTP header parameters (unless otherwise specified):

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parameter**
    - **Description**
    - **Reference**
  * - **Authorization**
    - Voucher released by the PDND Authorization Server.
    - [:rfc:`9449`], [`MODI`_], [`PDND`_]
  * - **DPoP**
    - DPoP proof JWT, to comply with the ``REST_JWS_2021_POP`` security pattern. It is mandatory only when following the ``POP_DPoP`` implementation.
    - [:rfc:`9449`], [`PDND`_]
  * - **Agid-JWT-Signature**
    - JWT containing the signature of the message headers whose integrity needs to be guaranteed, to comply with the ``INTEGRITY_REST_02`` security pattern.
    - [`MODI`_]
  * - **Digest**
    - Digest of the message payload, to comply with the ``INTEGRITY_REST_02`` security pattern. According to :rfc:`3230`, the format MUST be the following: ``<digest-algorithm>=<encoded digest output>``.
    - [:rfc:`3230`], [`MODI`_]
  * - **Agid-JWT-TrackingEvidence**
    - JWT containing the data tracker in the Consumer's domain. It is mandatory only when complying with ``AUDIT_REST_02`` or the ``POP_TPoP`` implementation.
    - [`MODI`_]

The ``Signature`` JWT, contained in the ``Agid-JWT-Signature`` HTTP header, MUST include the following JOSE header parameters:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parameter**
    - **Description**
    - **Reference**
  * - **alg**
    - A digital signature algorithm identifier.
    - [:rfc:`7515`]
  * - **kid**
    - Unique identifier of the JWK used by the Consumer to sign the JWT.
    - [:rfc:`7515`]
  * - **typ**
    - MUST be set to ``JWT``.
    - [:rfc:`7515`], [:rfc:`7519`]

The ``Signature`` JWT, contained in the ``Agid-JWT-Signature`` HTTP header, MUST include the following payload claims:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **iss**
    - MUST be set to the same value as ``client_id``.
    - [:rfc:`7519`]
  * - **sub**
    - MUST be set to the same value as ``client_id``.
    - [:rfc:`7519`]
  * - **aud**
    - The identifier of the Provider.
    - [:rfc:`7519`]
  * - **exp**
    - UNIX timestamp representing the JWT expiration time.
    - [:rfc:`7519`]
  * - **nbf**
    - UNIX timestamp representing the JWT first validity time (optional).
    - [:rfc:`7519`]
  * - **iat**
    - UNIX timestamp representing the JWT issuance time.
    - [:rfc:`7519`]
  * - **jti**
    - Unique identifier of the JWT to prevent replay attacks.
    - [:rfc:`7519`]
  * - **signed_headers**
    - JSON object containing the signed headers whose integrity needs to be protected, to with ``INTEGRITY_REST_02``. It MUST contain the following claims:

      - **digest**: JSON string representing the signature of the ``Digest`` HTTP header
      - **content-type**: JSON string representing the signature of the ``Content-Type`` HTTP header
    - [`MODI`_]

If present, the ``TrackingEvidence`` JWT, contained in the ``Agid-JWT-TrackingEvidence`` HTTP header, MUST include the following JOSE header parameters:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parameter**
    - **Description**
    - **Reference**
  * - **alg**
    - A digital signature algorithm identifier.
    - [:rfc:`7515`]
  * - **kid**
    - Unique identifier of the JWK used by the Consumer to sign the JWT.
    - [:rfc:`7515`]
  * - **typ**
    - MUST be set to ``JWT``.
    - [:rfc:`7515`], [:rfc:`7519`]

If present, the ``TrackingEvidence`` JWT, contained in the ``Agid-JWT-TrackingEvidence`` HTTP header, MUST include the following payload claims:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **iss**
    - MUST be set to the same value as ``client_id``.
    - [:rfc:`7519`]
  * - **aud**
    - The identifier of the Provider.
    - [:rfc:`7519`]
  * - **exp**
    - UNIX timestamp representing the JWT expiration time.
    - [:rfc:`7519`]
  * - **nbf**
    - UNIX timestamp representing the JWT first validity time (optional).
    - [:rfc:`7519`]
  * - **iat**
    - UNIX timestamp representing the JWT issuance time.
    - [:rfc:`7519`]
  * - **jti**
    - Unique identifier of the JWT to prevent replay attacks.
    - [:rfc:`7519`]
  * - **purposeId**
    - The identifier of the purpose registered in the PDND Platform, associated with the intended e-Service.
    - [`MODI`_]
  * - **dnonce**
    - It MUST be a random string composed by integer numbers and with a length of 13 digits.
    - [`MODI`_]

When complying with the ``AUDIT_REST_02`` security pattern, the ``TrackingEvidence`` payload MUST also contain the tracked data agreed upon with the Provider.

e-Service Response
"""""""""""""""""""

The e-Service Response MUST use HTTP Content-Type set to ``application/json``.

The e-Service Response MUST include the following HTTP header parameters:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parameter**
    - **Description**
    - **Reference**
  * - **Agid-JWT-Signature**
    - JWT containing the signature of the message headers whose integrity needs to be guaranteed, to comply with the ``INTEGRITY_REST_02`` security pattern.
    - [`MODI`_]
  * - **Digest**
    - Digest of the message payload, to comply with the ``INTEGRITY_REST_02`` security pattern. According to :rfc:`3230`, the format MUST be the following: ``<digest-algorithm>=<encoded digest output>``.
    - [:rfc:`3230`], [`MODI`_]

The ``Signature`` JWT, contained in the ``Agid-JWT-Signature`` HTTP header, MUST include the following payload claims:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **iss**
    - The identifier of the Provider.
    - [:rfc:`7519`]
  * - **sub**
    - The identifier of the Provider.
    - [:rfc:`7519`]
  * - **aud**
    - The identifier of the Consumer.
    - [:rfc:`7519`]
  * - **exp**
    - UNIX timestamp representing the JWT expiration time.
    - [:rfc:`7519`]
  * - **nbf**
    - UNIX timestamp representing the JWT first validity time (optional).
    - [:rfc:`7519`]
  * - **iat**
    - UNIX timestamp representing the JWT issuance time.
    - [:rfc:`7519`]
  * - **jti**
    - Unique identifier of the JWT to prevent replay attacks.
    - [:rfc:`7519`]
  * - **signed_headers**
    - JSON object containing the signed headers whose integrity needs to be protected, to with ``INTEGRITY_REST_02``. It MUST contain the following claims:

      - **digest**: JSON string representing the signature of the ``Digest`` HTTP header
      - **content-type**: JSON string representing the signature of the ``Content-Type`` HTTP header
    - [`MODI`_]

The e-Service Response payload includes specific claims related to the data elements provided to the Consumer.

If any errors occur during the validation of the e-Service Request, the e-Service Endpoint MUST return an error response, whose structure depends on the nature of the error.

In case of authentication issues (i.e., invalid or expired Voucher), the response MUST adhere to the error format defined in :rfc:`6750#section-3` and :rfc:`9449#section-7.1`, with specific reference to the use of the ``WWW-Authenticate`` header parameter.

.. code-block:: http
    :caption: Non-normative example of an e-Service Error Response in case of 401 errors
    :name: code_Usage_Endpoint_eService_Error_401

    HTTP/1.1 401 Unauthorized
    WWW-Authenticate: DPoP error="invalid_token", error_description="The access token expired"

For all other errors, the response MUST adhere to the error format defined in :rfc:`9457`. The response MUST use ``application/problem+json`` (according to MODI ``RAC_GEN_FORMAT_002``) as the content type and includes the following parameters:

    - ``type``: [OPTIONAL] URI reference that identifies the problem type.
    - ``title``:  [REQUIRED] String containing a short, human-readable summary of the problem type.
    - ``status``: [REQUIRED] Number indicating the HTTP status code for this occurrence of the problem.
    - ``detail``: [REQUIRED] String containing a human-readable explanation specific to this occurrence of the problem.
    - ``instance``: [OPTIONAL] string containing a URI reference that identifies the specific occurrence of the problem.

.. code-block:: http
    :caption: Non-normative example of an e-Service Error Response in case of other errors
    :name: code_Usage_Endpoint_eService_Error

    HTTP/1.1 400 Bad Request
    Content-Type: application/problem+json

    {
        "title": "invalid_request",
        "status": 400,
        "detail": "The Agid-JWT-Signature header parameter is missing."
    }


The following table lists the HTTP Status Codes that MUST be supported for the error response:

.. list-table::
  :class: longtable
  :widths: 50 50
  :header-rows: 1

  * - **Status Code**
    - **Description**
  * - ``400 Bad Request``
    - The request cannot be fulfilled because it is missing required parameters, contains invalid parameters, or is otherwise malformed.
  * - ``401 Unauthorized``
    - The request cannot be fulfilled because the Voucher is expired, revoked, or otherwise malformed.
  * - ``500 Internal Server Error``
    - The request cannot be fulfilled because the e-Service Endpoint encountered an internal problem.
  * - ``503 Service Unavailable``
    - The request cannot be fulfilled because the e-Service Endpoint is temporarily unavailable (e.g., due to maintenance or overload).


