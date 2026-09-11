.. include:: ../common/common_definitions.rst
.. Included via credential-issuance.rst at title level '=' (document title).


eID Substantial Authentication with MRTD Verification for IT-Wallet ID Issuance
===============================================================================

This Section defines an eID Substantial Authentication with MRTD Verification protocol that integrates within the IT-Wallet ID issuance flow as defined in the Section :ref:`credential-issuance-low-level:Credential Issuance Low-Level Flows` extending OAuth 2.0 flows to include:

	- Electronic identification with Level of Assurance "Substantial" (LoA3).
	- Electronic document verification as an additional identity verification layer.
	- Session correlation and security binding between authentication steps.
	- Integration with Credential issuance flows.

While CIEid with LoA High authentication remains the primary method for Wallet activation and IT-Wallet ID issuance, the eID Substantial Authentication with MRTD Verification mechanism defined in this Section provides an alternative approach to enhance service accessibility and usability, without compromising the overall security of the IT-Wallet ecosystem.

.. note::
  This Section currently only supports the CIE id card for the MRTD verification protocol, the protocol described in this Section MAY be extended to support other MRTD Documents such as Electronic Passports.

Design Principles
-----------------

The protocol adheres to the following design principles:

	- **Standard Compatibility**: Extends existing authorization frameworks without breaking changes to the standard OAuth 2.0 Authorization Framework.
	- **Multi-Step Authentication**: Implement progressive enforcement of authentication with MRTD verification.
	- **Session Integrity**: Maintains secure session correlation across authentication steps.
	- **Unified Flow**: Integrates multiple authentication factors in a single authorization session.

System Architecture
-------------------

The system architecture comprises the following main components:

	- **Wallet Instance:** It handles the IT-Wallet ID request according to IT-Wallet Specification, supporting additional cryptographic capabilities for MRTD/IAS Electronic Document reading according to `ICAO 9303`_ and `BSI-03110`_ specifications.
	- **eID Substantial Authentication with MRTD Verification System:** Orchestrates the authentication flow, integrating LoA3 Identity Providers, Electronic Document Verification Service, and performing all the identity correlation checks to guarantee that the User requesting an IT-Wallet ID matches with the authenticated one.

		- **EAA Authorization Server:** Handles the authorization flow for IT-Wallet ID Issuance, coordinating the User authentication and the remote identity proofing.
		- **MRTD PoP Service:** Handles electronic document proof of possession with cryptographic document validation.

	- **LoA3 Identity Provider:** Provides Electronic Identification Schemes with eIDAS LoA3 compliance (CIEid and SPID).
	- **CIE National Registry:** Acts as the authoritative source for the CIE. Provides information related to the validity status of the document. It also optionally provides the MRZ data (document number, date of birth, expiry date, citizenship and gender) to improve the User experience.

.. _fig_eID_MRTD_System_Architecture:
.. plantuml:: plantuml/l2plus-system-architecture.puml
    :width: 99%
    :alt: The figure illustrates the eID Substantial Authentication with MRTD Verification System Architecture.
    :caption: `eID Substantial Authentication with MRTD Verification System Architecture. <https://www.plantuml.com/plantuml/svg/dLHXRzis4FtkNt4r1iJnuZYjimyRkg2AhIq2uiQml1GT1WWqUOw9KgH6dk8wG__xICfH7JT0Wnhvm1nFZ-_klRjtZfYbkbHm_UPdcDQAv20dh22fQMsiV60aZOR4yhKav5HRx1ozeZMM21njhP3fWQb9IOsTLr9pLGk4j-FpuVYy69koCXerNNIkiabQv8jqdjuiFixItd7dw3hvUFFNelYGBQwAw_JFzFt4Hpj7CC6L1uDyDiyMQRu7IdN5X1qDkIbBeo-UkLaPJGEsGMTA7Fmo58pOaZbyGQf3Uu_s1ObI59nPyOBC3LCAwNk9GwaTIQf9Xf8w_gWmQe7P1F9wwOXfaan5GT0VUQF8Hj8QflF516xHofNapmZLQGKeqi_KQmYTGFT3F42c0pZ7hWzDpL8gXAIgmdzNJ0k53hB5u35t0XR_hT4HX8uAC1eydxqCGhxMHfcxBGHOmQm81_xf53A2offxAT11ly_jjY9pPrcrbXmugvX_MfBqbojZGqt3BCaXLSZ96krp9eRN9Me2Yqn8VTVlGoyR9pVmw-XiT0ANUJOu6xr-VNRSFVd9LLOI_jvjYkrwHrsQEh3PzgHpDLfVNfeaC6i8sUun_DS1_slJoZ04XIEi2kPx_k0_-34jygq7AKC_RxmgwCWoGWSHVn3mWJt5MIcp0QO5M2mD8KWHBcaRkcTMll2MRFYrulQGiOPg4MqSIdmwldaCHoRXuit1TFzXMOaROp_5ns-ooVdjEFkk3q8kQt5Q_jmOAwIEaJqzN4FX-1dwml2YCbKaBpdwTsClPsOMYSl6eRTCIH5Hs-WUG_pg5h5pIzCry7-LSGwTQwLwwi0s_pwySCXxD-yxubywNmwdIXasAgIeF9bhaumWUnIjTLXZ86_fU1-znCC23HUx9BTlzmQXjL6JxA0tpb8fOjlpMJRPD_lU3l543mXoYON5E-d8RlsB7WNUHsIcOBwBTtSNasPZHce99mVCnJ7VwKoCv3s2CxNb6ASrNFeFJw4jH6eVBnlg5XKZ540c9iO6IueBWchdfGdXLe2uA9Xo1apLy5FRTd74pEdyRmXB7NgjQBekbzxn8Om1S2ajhKy0FrVIRcFq1BWa-O3QhMKLstU7Mg0z3hHa6Hx0Y5uxjE53j18rnzEz1ejTNq9tvwZQLNeuUUs4DRFmJ-Z5q-d9dAiVb-wbDHk7TX0twY7qjrCnUMfiLozB6LqTrPfb0U6G4BmTN1n2mM_GxVTRdquPyNNSgjt8eBZqI_kPdR9dz3oPNW_zdXWVRB1dYseXlwdem9c94BBHlTtuhOE205_BV8TQrANw7m00>`_

High-Level Flow
---------------

The protocol consists of the following sequential phases:

1. **OAuth Authorization Request**: PAR and authorization request with eID Substantial Authentication with MRTD Verification.
2. **Primary Authentication**: LoA3 electronic identification (SPID/CIEid L2).
3. **MRTD Proof of Possession (PoP) Validation**: Electronic document reading and cryptographic verification (Proof of Possession, integrity, and authenticity checks).
4. **OAuth Authorization Response**: Final authorization code issuance.

.. _fig_eID_MRTD_High_Level_Flow:
.. plantuml:: plantuml/l2plus-high-level-flow.puml
    :width: 99%
    :alt: The figure illustrates the eID Substantial Authentication with MRTD Verification High-Level Flow.
    :caption: `eID Substantial Authentication with MRTD Verification High-Level Flow. <https://www.plantuml.com/plantuml/png/ZPHnY-984CN_zrFKUGSp0piuYN6Lmv4Tr6M5MLPK5kulwQGhiRbETwwxCfxxwJUTQ2QACW4HxRp-zUkgb_fYYHdAKma_NdBQmVTSadXS4sRW_gCY4J4IMi4taUmUN_4D9NoLUj_vGwX8vXnXF0rwqs0xrMcc5IgQTBujPlFjUZDVpNzi_bdExnyQOiepnas_5sj5ZsoFLgVuEEZb5itaOrcgGo5nooIr4DkTGCbRYl_5GmjLtFxq20s9s5KFMwWv8nOoYst0Eh4jP89l8sPu2oN-7-sOIjfURC-an0-5FQ4i2SfTTYQTpXrCSqiw1Ki7YS0n5aguPnPYRI0k4WNPZbcqdHVEvn9JLBHXoNstNFMwd-2lC9bggSrpzq_F-pmAkLjpHnvNzpj1MEgquMXEsgSm68s2xiDLhd_E7OO-7s4xxe1vyUTHmRsx1kwVW_cmFtZosu7PapzyyWfm2sxiZU92sueRUSEdczpWdElp0VE7xRWUzhaN5jmE2PBO6Lln2__sHfDnEC753DPvQ8af4anUpfIzS2DdjPd1JpGYFYwFU-5at7EKoGaMJ1hZPsaqwKWNFyh0dAIeE5GEEdSIOmBIO8fT15mOZ1pPvN3ceeTG-801f4oeO-w0MSZGW51PJc0pZ6f3dNgstLTf_0JTycnmfUzMazDzQID-LJTRuNyvMkewvSiAcEB0pWIc4bGbICkfQztKZNRkzL89bWfXoZvPLtMR6K7ut7qVQswLM6AVgnwwtbvQzMkhVkd5Y9IPmqKVt9DN_T87b1YHqKf483WggYi0z-lbOjQRBkQ2mwl_qFHJJCuB8xupSdVXf5yxwRlpflKz6wMQwIXtzuNCQ1r3yScqjMYjiz2eH_FuuvoxiD1t5cuxE3jigPVmaqd1wsBCt-l0Jog3Z0kLbAsCp24ZdHYMxGh9MoExLvrzP2oeZGMtysIB7HRTywz2CNaHfqXp165jpbI4jzBIz16KFOArAtxrRfOpE4JQ8whJB5wXtAxgqBydokW8aGFfAqdwVYtCvRHdXBpxq80wMDsQHPauEXnd0N87snYH96Y0DvjLOztqRT3wHrhGxEwgYar9MnCp5UAjxdV1k85evABQxjecaR1P-nBm1HNFK_aR>`_

Session Management
------------------

The Authorization Server MUST maintain a unified session across all authentication steps, ensuring:

	- **Session Continuity**: Single session identifier throughout the authentication flow.
	- **State Correlation**: Authentication results from each step are correlated.
	- **Security Binding**: Binding between authentication steps.

Since the EAA Authorization Server and the MRTD PoP Service operate within the EAA Provider boundary implementation, it is RECOMMENDED that the OAuth 2.0 session and the nonces used within the protocol flow are properly handled by both components seamlessly.

When both services operate within the same trust boundary, the following mechanisms are available for session correlation:

	- Direct memory access to shared session stores.
	- Internal service-to-service authentication using pre-shared keys.
	- Synchronized nonce validation without external communication overhead.
	- Unified audit logging and security event correlation.

When the EAA Authorization Server or MRTD PoP Service is deployed outside the EAA Provider boundary implementation, the :ref:`credential-issuance-l2plus:Security Considerations` MUST be taken into account to harden the User authentication sessions management. These measures include but are not limited to secure session token handling, distributed session validation, and enhanced audit trail mechanisms.

Low-Level Flow
--------------

This section provides technical details about the IT-Wallet ID Issuance using Level of Assurance Substantial and remote identity proofing through verification of the electronic document using a MRTD Verification service.

.. _fig_eID_MRTD_Detailed_Flow:
.. plantuml:: plantuml/l2plus-detailed-flow.puml
    :width: 99%
    :alt: The figure illustrates the eID Substantial Authentication with MRTD Verification Detailed Flow.
    :caption: `eID Substantial Authentication with MRTD Verification Detailed Flow. <https://www.plantuml.com/plantuml/svg/nLPjRnf74Fw-lsBgAAbDV13R-L2X4ES2sAPAx1FWH6rTeULkW6sEtUlk7ZRzzTtPEuwNzA98hLG98RYRbsUUcNrctndBjSsNAVln1xl09KACEa-Hoq3bDXKI6S-jalboYffbpbR48kFImj6zGNq4tC3z_lFFF4tHma2wq396RnBkctG7VV-uowRg2U2e7uOGQRKI2OLyza7C5_PzckE-5rc5kLqeBVxYLYW98zIh4aGusZV-E1pt85AHjn4bZ5vq5uqOoWHStgyWmQsFobCOubmOgzVUwUFWTjzqO_OW1mbAA-ow0kyT1hs8CUQUfmWuwC475Lvuu6GS5yXVWiQbiWXY4oBJIis4d8EGC1W76nPxC30c9oBXAbMFZDr3y1R2DdmcB5O1ZwrOSOlWuaFfzI1pGw4e-oYVKYEiu2ay2hi0pymdr69MWc6iq-b0jE06uQmDTmJrWEWX_fcZiT3fiD3d7q4Red1OlJW6Y5E1qav4SWgwU7et_GDZU-BWG97QXmwwtZ08hNKsHNmkazgN0NLHI5_V3NB7CfbJp4R3H-MxK2S9MYvIiEiCuKZOINh-Cb5nlYHidkEZHeCnLq10TLHbc4n9Wt1SGf_aMfm2FcL2eva8URAfkxtNd1gQ2DnrVmoj3JIyhDZfD9lD5pjPw3_PtoXZsu2S1ravJ4ryuiiinQRIyzqUdJlCMYovNXzELU0xJWVpy0qHHOEuDmxKpP4hYoQsJQxxNbKzpBs7DyJNVRk8pW-dEIRsP67fUQg9Lz2yMyr56wgp-ecd8l6c5JOQzPlnE6gTDS_WujKvNAdST_-3AeAsOM5jPjgjbfUovgFlpIvthNX1p-GSBnkDfRP9CGUTDzlVavy_Zz_wkQ2KNYRQRhmgO2KHZSQ3ZEv6hh6Og3ZmhYqXXQqWEc3VRkI3_2zF0cCgimm0F6RYY-Ig3GwmrG9NwBZzrRdCb5xw46HB9X1iwpmqGPamLiQZ1kmpKRQGgAZwSkxw4iOnPXQJii22MvLDf98ndaBLWrFNhvo-bhxMOvKLQfgkJpmIrt_E64yj36O5D0DIMU0hBb8-JH6iyWmSx1bVMGX-I3Vz8bFXm6eBtV3MMspaSx1zZAb145KoDRLSI4o0MnXPpE3ih8fDdlqdgtbiFL2OQRKanuAqkLPvLkwlNp1rUWstLrsNooAvL0UHuFjpv4Y7NgbE4D4uWVj4oXWqnfdJCwjYbNhn9nGRAByzcsj4-VjRw4BLe33BqgqMH66tJsqQ8a-WTtrsIb_kUtJNcv2v3zM5e8hbzV2VB87LfHs4ezsiLRgG3dsg96sXA9-wz_05rqL4ygd9_Lrk-p3sdJpLagS7olCWZRygRCUm1i1m50Rdhrx_14RC9RUvHcg82xNrf5RN2iLMmRwf6IjQl-l_JJK0sBvU490DO3-KAwg3hYKK93SR4XxaPfVIfboL4koumVZB2MC7mhAZ3w_Wxakzg6nP-svzqPW8ZR5VeRvyBpWEzbPqg4a-bM_cDmny2zzhzMXG1rDkC84hGKFKLN8czB8QRRVJgsrJrwfMFBtyEjM4863oGj7cd9IdkrZzntQXLJvVmBH0SBAx7L_NtSSAbhPhqXDQVpNPUdZsVCYkIZpD_tAzNZhhs8Kgge4ND37L7s5CnmTuVX4-Fxzod_eRZfRA8YWwfk5fE78wEhY-6LyF-_rRDbuWp4W2OoMja3aQu76iT4A7tggQ6xFtu0OId7b5Bq_1rjXa66_lmIWJZu6zSx_oPVet>`_

Phase 1: OAuth Authorization Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Wallet Instance initiates the eID Substantial Authentication with MRTD Verification flow by submitting a Pushed Authorization Request (PAR), using a JWT-secured Authorization Request (JAR) and Rich Authorization Requests (RAR) as specified below.

Authorization Details
"""""""""""""""""""""

The JWT Request Object MUST contain the same parameters as defined in :ref:`credential-issuance-endpoint:Pushed Authorization Request Endpoint`. When the User requests a IT-Wallet ID using eID Substantial Authentication with MRTD Verification, the Wallet Instance MUST include an additional **Authorization Details Object** in the ``authorization_details`` parameter, with the structure and claims as defined in the Table of the JWT Request parameters of Section :ref:`credential-issuance-endpoint:Pushed Authorization Request Endpoint`

Below a non-normative example of PAR:

.. code-block:: http

    POST /as/par HTTP/1.1
    Host: eaa-provider.example.org
    Content-Type: application/x-www-form-urlencoded
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtp…
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUz…

    client_id=47b982369791d08003a7283f059cb0d1&
    request=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJmODU1NWNlYi1jNjVjLTQwMjUtOTM3OC1iNjY3MmI2MTQ5YWYiLCJhdWQiOiJodHRwczovL3BpZC1wcm92aWRlci5leGFtcGxlLm9yZyIsImlhdCI6MTcxNTg0MjU2MCwiZXhwIjoxNzE1ODQyODYwLCJyZXNwb25zZV90eXBlIjoiY29kZSIsInJlc3BvbnNlX21vZGUiOiJmb3JtX3Bvc3Quand0IiwiY2xpZW50X2lkIjoiNDdiOTgyMzY5NzkxZDA4MDAzYTcyODNmMDU5Y2IwZDEiLCJpc3MiOiI0N2I5ODIzNjk3OTFkMDgwMDNhNzI4M2YwNTljYjBkMSIsInN0YXRlIjoiZnlaaU9MOUxmMkNlS3VOVDJKenhpTFJEaW5rMHVQY2QiLCJjb2RlX2NoYWxsZW5nZSI6IkU5TWVsaG9hMk93dkZyRU1USmd1Q0hhb2VLMXQ4VVJXYnVHSlNzdHctY00iLCJjb2RlX2NoYWxsZW5nZV9tZXRob2QiOiJTMjU2Iiwic2NvcGUiOiJwaWQiLCJhdXRob3JpemF0aW9uX2RldGFpbHMiOlt7InR5cGUiOiJvcGVuaWRfY3JlZGVudGlhbCIsImNyZWRlbnRpYWxfY29uZmlndXJhdGlvbl9pZCI6ImRjX3NkX2p3dF9waWQifSx7InR5cGUiOiJpdF9sMitkb2N1bWVudF9wcm9vZiIsIm11bHRpX3N0ZXBfbWV0aG9kIjoibXJ0ZCtpYXMiLCJpZHBoaW50aW5nIjoiaHR0cHM6Ly9pZHAuZXhhbXBsZS5vcmciLCJtdWx0aV9zdGVwX3JlZGlyZWN0X3VyaSI6Imh0dHBzOi8vc3RhcnQud2FsbGV0LmV4YW1wbGUub3JnL2NoYWxsZW5nZSJ9XSwicmVkaXJlY3RfdXJpIjoiaHR0cHM6Ly9zdGFydC53YWxsZXQuZXhhbXBsZS5vcmcifQ.AuthRequestSign456_NoKidJWTSignature-abc123def456ghi789jkl012mno345pqr678stu901vwx234yz567

When the ``it_l2+document_proof`` object is not present in the authorization_details array, the EAA Provider MUST authenticate the User with CIEid LoA High.
The PAR Response and the Authorization Request are the same as in the IT-Wallet Specification.

Phase 2: Primary Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upon successful processing of the PAR, the Authorization Server redirects the User Agent to the configured LoA3 Identity Provider for primary authentication. The User completes the LoA3 authentication flow (SPID or CIEid Substantial) and the Authorization Server correlates the authenticated identity with the active OAuth session.

The EAA Authorization Server MUST ensure that the ``mrtd_auth_session`` parameter is maintained throughout this phase for proper session correlation with subsequent authentication steps.

.. note::
  In the case the User performs a LoA High authentication the phase 3 MUST be skipped.

Phase 3: MRTD PoP Validation Flow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Following successful primary authentication, the Authorization Server initiates the electronic document proof of possession flow by providing the Wallet Instance with the necessary parameters for MRTD validation.

MRTD Proof JWT
""""""""""""""

The Authorization Server MUST provide a signed JWT containing the challenge requirements for document validation. The JWT structure is defined as follows:

.. _table_eID_MRTD_Proof_JWT_Header:
.. list-table:: MRTD Proof JWT Header
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **alg**
     - string
     - REQUIRED. Signature algorithm.
   * - **typ**
     - string
     - REQUIRED. It MUST be ``mrtd-ias+jwt``.
   * - **kid**
     - string
     - REQUIRED. Identifier of the EAA Provider's key that MUST be used to verify the signature of this JWT.

.. _table_eID_MRTD_Proof_JWT_Payload:
.. list-table:: MRTD Proof JWT Payload
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **iss**
     - string
     - REQUIRED. EAA Provider identifier.
   * - **aud**
     - string
     - REQUIRED. Wallet Instance identifier.
   * - **iat**
     - integer
     - REQUIRED. Issuance time (Unix timestamp).
   * - **exp**
     - integer
     - REQUIRED. Expiration time (Unix timestamp).
   * - **status**
     - string
     - REQUIRED. Challenge status. MUST be ``require_interaction``.
   * - **type**
     - string
     - REQUIRED. Type of the required interaction. It MUST be set to ``mrtd+ias``.
   * - **mrtd_auth_session**
     - string
     - REQUIRED. Session identifier.
   * - **state**
     - string
     - REQUIRED. MUST be the same value as in the initial Request Object.
   * - **mrtd_pop_jwt_nonce**
     - string
     - REQUIRED. Nonce value for replay protection. It MUST be obtained by the MRTD PoP Service that MUST have direct control over this value.
   * - **htu**
     - string
     - REQUIRED. HTTP URI of the MRTD PoP initialization endpoint.
   * - **htm**
     - string
     - REQUIRED. HTTP method for the MRTD PoP initialization request. MUST be ``POST``.

A non-normative example is provided below:

.. code-block:: http

    HTTP/1.1 302 Found
    Location: https://start.wallet.example.org/challenge?challenge_info=eyJhbGciOiJFUzI1NiIsInR5cCI6Im1ydGQtaWFzK2p3dCIsImtpZCI6ImQ0ZjhlMDJlZWJhMDdhNTM3MmUxOGVjYzU4NzA5ZDA2In0.eyJpc3MiOiJodHRwczovL3BpZC1wcm92aWRlci5leGFtcGxlLm9yZyIsImF1ZCI6IjQ3Yjk4MjM2OTc5MWQwODAwM2E3MjgzZjA1OWNiMGQxIiwiaWF0IjoxNzUzNTU1MzU4LCJleHAiOjE3NTM1NTU2NTgsInN0YXR1cyI6InJlcXVpcmVfaW50ZXJhY3Rpb24iLCJ0eXBlIjoibXJ0ZCtpYXMiLCJtcnRkX2F1dGhfc2Vzc2lvbiI6Ind4cm9WckJZMk1DcTRkRE5HWEFDUyIsInN0YXRlIjoiZnlaaU9MOUxmMkNlS3VOVDJKenhpTFJEaW5rMHVQY2QiLCJtcnRkX3BvcF9qd3Rfbm9uY2UiOiJub25jZTEiLCJodHUiOiJodHRwczovL2Vkb2MtcHJvb2YvaW5pdCIsImh0bSI6IlBPU1QifQ.i6p_FN7qNNawyL4KnOV1r8FrNVjzd-7Ve1wEGASHNnlXwuJ1f216v0Ml_KpVrq9yXkmOo_M2xZwih2SlHVfrzkuG3Pn7LWRL7dsyCtqEY2e58rFHjCa2miBnnKr0NU4wcBMMYe2_qKCOkA7SOa7usNTBluBLMQ28GfiMbr3tcpfpM4rD0POKQcfijvNkNbh-VdOxM8GdHb6IQO_xfpsaSzd8cc0k5yIYCWjDTeINVKebIz4m9Rm2JStvRrWUq8OCqkv-8dTJH9q-JXx0PzJC998RMwe6tqSL-kkE3dZLWwCJdP8Z7bITtowU49rEe-AkrGxVma4ANPq317umEfUwmw

The Authorization Server MUST:

- Generate a unique challenge identifier with sufficient entropy (minimum 128 bits) for cryptographic security.
- Create MRTD Proof JWT with proper header (``alg``, ``typ``, ``kid``) and payload parameters (as defined in the table above).
- Sign the MRTD Proof JWT using its private key with the cryptographic algorithm chosen. See Section :ref:`algorithms:Cryptographic Algorithms`.
- Construct a secure redirect URL with proper encoding to the Wallet Instance universal link.
- Set the redirect timeout to prevent indefinite waiting and handle timeout scenarios
- Optionally request MRZ information directly from the CIE National Registry using the authenticated User's taxpayer identification number.
- Maintain session correlation between the LoA High result and the document proof challenge

The Wallet Instance MUST:

- Validate the JWT signature using the EAA Provider's public key obtained through trust evaluation.
- Verify ``aud`` claim matches its ``client_id``.
- Verify ``iat`` and ``exp`` claims indicate the token has a correct issuance date and has not expired.
- Verify that the ``status`` field is set to "require_interaction".
- Verify the authentication type matches the expected value ``mrtd+ias``.
- Extract HTTP target URI (``htu``) and method (``htm``) for the next step.
- Handle JWT validation and network errors, and provide user feedback with appropriate retry mechanisms.
- Extract correlation parameters (``mrtd_auth_session``, ``state``, ``mrtd_pop_jwt_nonce``) for subsequent requests.

MRTD PoP Request
""""""""""""""""

The Wallet Instance MUST send an HTTP POST Request to the MRTD PoP Service initialization endpoint with ``application/json`` as content type, including Wallet Attestation and Wallet Attestation JWT PoP in the header according to `OAUTH-ATTESTATION-CLIENT-AUTH`_. The payload of the Request contains the following parameters:

.. _table_eID_MRTD_PoP_Request:
.. list-table:: MRTD PoP Request Parameters
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **mrtd_auth_session**
     - string
     - REQUIRED. Session identifier for session binding.
   * - **mrtd_pop_jwt_nonce**
     - string
     - REQUIRED. Nonce value obtained from the MRTD Proof JWT.

Below a non-normative example of an MRTD PoP Request:

.. code-block:: http

    POST /edoc-proof/init HTTP/1.1
    Host: eaa-provider.example.org
    Content-Type: application/json
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtp…
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUz…

    {
      "mrtd_auth_session": "wxroVrBY2MCq4dDNGXACS",
      "mrtd_pop_jwt_nonce": "f42cccb7f1c8269f9d4aeefe339c6b13"
    }

**The Wallet Instance MUST:**

- Validate the MRTD Proof JWT signature using the EAA Provider's public key.
- Verify the JWT ``aud`` claim matches its ``client_id``.
- Ensure the JWT ``exp`` claim indicates the token has not expired.
- Extract the ``mrtd_auth_session`` and ``mrtd_pop_jwt_nonce`` values for correlation.
- Include valid Wallet Attestation according to `OAUTH-ATTESTATION-CLIENT-AUTH`_.
- Handle network errors and implement appropriate retry mechanisms.

**The MRTD PoP Service MUST:**

- Validate the Wallet Attestation according to `OAUTH-ATTESTATION-CLIENT-AUTH`_.
- Verify the ``mrtd_auth_session`` parameter matches an active session.
- Validate the ``mrtd_pop_jwt_nonce`` parameter corresponds to the one issued at the previous step.

The MRTD PoP Service MAY request the MRZ information (document number, date of birth, expiry date, citizenship and gender) directly to the CIE National Registry using the Tax payer's identification number of the authenticated User. In this case, the MRTD PoP Service is able to check if the authenticated User owns a valid CIE and If this is not the case, it MUST send an HTTP Error Response with HTTP Error code ``access_denied``.

MRTD PoP Response
"""""""""""""""""

If the HTTP Request is successfully processed, the MRTD PoP Service MUST send a HTTP Response with code *202 Accepted* and ``application/jwt`` as content type. The JWT structure is defined as follows:

.. _table_eID_MRTD_PoP_Response_Header:
.. list-table:: MRTD PoP Response Parameters
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **alg**
     - string
     - REQUIRED. Signature algorithm.
   * - **typ**
     - string
     - REQUIRED. It MUST be ``mrtd-ias-pop+jwt``.
   * - **kid**
     - string
     - REQUIRED. Identifier of the EAA Provider's key that MUST be used to verify the signature of this JWT.

.. _table_eID_MRTD_PoP_Response_Payload:
.. list-table:: MRTD PoP Response Parameters
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **iss**
     - string
     - REQUIRED. EAA Provider identifier.
   * - **aud**
     - string
     - REQUIRED. Wallet Instance identifier.
   * - **iat**
     - integer
     - REQUIRED. Issuance time (Unix timestamp).
   * - **exp**
     - integer
     - REQUIRED. Expiration time (Unix timestamp).
   * - **challenge**
     - string
     - REQUIRED. Challenge data for cryptographic document validation. It SHOULD be the SHA-256 hash value of a random value with the ``mrtd_auth_session`` and timestamp for cryptographic binding.
   * - **mrtd_pop_nonce**
     - string
     - REQUIRED. Unique nonce value for the next step, preventing replay attacks.
   * - **mrz**
     - string
     - OPTIONAL. Machine Readable Zone information including document number, date of birth, expiry date, citizenship and gender.
   * - **htu**
     - string
     - REQUIRED. HTTP URI of the MRTD PoP validation endpoint.
   * - **htm**
     - string
     - REQUIRED. HTTP method for the MRTD PoP validation request. MUST be ``POST``.

Below a non-normative example of an MRTD PoP Response:

.. code-block:: http

    HTTP/1.1 202 Accepted
    Content-Type: application/jwt; charset=utf-8

    eyJhbGciOiJFUzI1NiIsInR5cCI6Im1ydGQtaWFzLXBvcCtqd3QiLCJraWQiOiJiM2YxYTZjMmU5ZDU0YThmOWMzZTdkMWEyZjRiNmM3OCJ9.eyJpc3MiOiJodHRwczovL3BpZC1wcm92aWRlci5leGFtcGxlLm9yZyIsImF1ZCI6Imh0dHBzOi8vd2FsbGV0LmV4YW1wbGUub3JnL2luc3RhbmNlLzEyMzQ1IiwiaWF0IjoxNzUzNTU1ODAwLCJleHAiOjE3NTM1NTYwMDAsIm1ydGRfcG9wX25vbmNlIjoiOWYyYzRhN2UzYjFkOGM5YTZlNWY0YjJhMWMzZDdlOGYiLCJtcnoiOiIuLi4iLCJjaGFsbGVuZ2UiOiIuLi4iLCJodHUiOiIuLi4iLCJodG0iOiIuLi4ifQ.signature

JWT decoded header:

.. code-block:: json

    {
      "alg":"ES256",
      "typ":"mrtd-ias-pop+jwt",
      "kid":"b3f1a6c2e9d54a8f9c3e7d1a2f4b6c78"
    }

JWT decoded body:

.. code-block:: json

    {
      "iss":"https://eaa-provider.example.org",
      "aud":"https://wallet.example.org/instance/12345",
      "iat": 1753555800,
      "exp": 1753556000,
      "mrtd_pop_nonce":"9f2c4a7e3b1d8c9a6e5f4b2a1c3d7e8f",
      "mrz":"...",
      "challenge":"...",
      "htu":"...",
      "htm":"..."
    }

**The MRTD PoP Service MUST:**

- Generate cryptographically secure challenge data with sufficient entropy (to be used in Anti-Cloning Internal Authentication protocol by the Wallet Instance), storing it with an appropriate expiration time. Moreover, the MRTD PoP Service MUST ensure challenge uniqueness to prevent reuse attacks.
- Create a new unique ``mrtd_pop_nonce`` for the next step to prevent replay attacks.
- Validate session continuity by ensuring the ``mrtd_auth_session`` parameter corresponds to an active session.
- Return HTTP *202 Accepted* status to indicate asynchronous processing initiation.
- Include proper Content-Type header (``application/jwt; charset=utf-8``).
- Handle service errors and return appropriate error responses.
- Extract and validate MRZ information if provided from external registry services.

**The Wallet Instance MUST:**

- Validate HTTP response status (*202 Accepted*) and content type.
- Parse JSON response and validate required parameters (``challenge``, ``mrtd_pop_nonce``).
- Extract challenge data for cryptographic document validation.
- Store new ``mrtd_pop_nonce`` value securely for subsequent validation requests.
- Validate optional MRZ information if present in the response.
- Extract HTTP target URI (htu) and method (htm) for the next step.
- Handle errors, providing relative user feedback.
- Store challenge data temporarily.
- Prepare NFC reading session.

The Wallet Instance performs NFC-based electronic document reading and validation, then submits the evidence to the EAA Provider for final verification and identity correlation with the LoA3 authentication result.

MRTD PoP Validation Request
"""""""""""""""""""""""""""

Upon all the evidence has been collected through NFC interaction with the Electronic Document, the Wallet Instance MUST send all data to the EAA Provider Authorization Server for the final validation and identity cross checks. The Wallet Instance MUST send a HTTP POST Request with ``application/json`` as content type, including Wallet Attestation and Wallet Attestation JWT PoP in the header according to `OAUTH-ATTESTATION-CLIENT-AUTH`_. The payload of the Request contains the following parameters.

.. _table_eID_MRTD_PoP_Validation_Request:
.. list-table:: MRTD PoP Validation Request Parameters
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **mrtd_validation_jwt**
     - string
     - REQUIRED. JWT containing document evidence, cryptographic proofs, Data Groups (DGs), and validation results.
   * - **mrtd_auth_session**
     - string
     - REQUIRED. Session identifier for session binding.
   * - **mrtd_pop_nonce**
     - string
     - REQUIRED. MUST match the value obtained from the MRTD PoP Response.

Validation JWT Structure
""""""""""""""""""""""""

The Validation JWT (``mrtd_validation_jwt``) structure is given in the following table.

.. _table_eID_MRTD_Validation_JWT_Header:
.. list-table:: Validation JWT Header Parameters
   :widths: 20 15 65
   :header-rows: 1

   * - **Header Parameter**
     - **Type**
     - **Description**
   * - **alg**
     - string
     - REQUIRED. Signature algorithm.
   * - **typ**
     - string
     - REQUIRED. It MUST be ``mrtd-ias+jwt``.
   * - **kid**
     - string
     - REQUIRED. Identifier of the Wallet Instance's key that MUST be used to verify the signature of this JWT.

.. _table_eID_MRTD_Validation_JWT_Payload:
.. list-table:: Validation JWT Payload Parameters
   :widths: 20 15 65
   :header-rows: 1

   * - **Payload Parameter**
     - **Type**
     - **Description**
   * - **iss**
     - string
     - REQUIRED. Wallet Instance identifier.
   * - **aud**
     - string
     - REQUIRED. EAA Provider identifier.
   * - **iat**
     - integer
     - REQUIRED. Issuance time (Unix timestamp).
   * - **exp**
     - integer
     - REQUIRED. Expiration time (Unix timestamp).
   * - **document_type**
     - string
     - REQUIRED. Type of document validated. MUST be set to ``cie``.
   * - **mrtd**
     - JSON Object
     - REQUIRED. MRTD validation data containing Data Groups and SOD.
   * - **ias**
     - JSON Object
     - REQUIRED. IAS validation data containing Anti-Cloning Public Key, and SOD.

MRTD Object Structure
"""""""""""""""""""""

The ``mrtd`` object contains the following fields:

.. _table_eID_MRTD_Object:
.. list-table:: MRTD Object Structure
   :widths: 20 15 65
   :header-rows: 1

   * - **Field**
     - **Type**
     - **Description**
   * - **dg1**
     - string
     - REQUIRED. Base64-encoded Data Group 1 (MRZ information:document number, date of birth, expiry date, citizenship and gender).
   * - **dg11**
     - string
     - REQUIRED. Base64-encoded Data Group 11 (additional personal data).
   * - **sod_mrtd**
     - string
     - REQUIRED. Base64-encoded Security Object of Document for MRTD.

IAS Object Structure
""""""""""""""""""""

The ``ias`` object contains the following fields:

.. _table_eID_MRTD_IAS_Object:
.. list-table:: IAS Object Structure
   :widths: 20 15 65
   :header-rows: 1

   * - **Field**
     - **Type**
     - **Description**
   * - **ias_pk**
     - string
     - REQUIRED. Base64-encoded IAS public key in DER format.
   * - **sod_ias**
     - string
     - REQUIRED. Base64-encoded Security Object of Document for IAS.
   * - **challenge_signed**
     - string
     - REQUIRED. Base64-encoded signed challenge response.

Below a non-normative example of an MRTD PoP Validation Request:

.. code-block:: http

    POST /edoc-proof/verify HTTP/1.1
    Host: eaa-provider.example.org
    Content-Type: application/json
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtp…
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUz…

    {
      "mrtd_validation_jwt":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC5leGFtcGxlLm9yZy9pbnN0YW5jZS8xMjM0NSIsImF1ZCI6Imh0dHBzOi8vcGlkLXByb3ZpZGVyLmV4YW1wbGUub3JnIiwiaWF0IjoxNzUzNTU1NDAwLCJleHAiOjE3NTM1NTU3MDAsImRvY3VtZW50X3R5cGUiOiJjaWUiLCJtcnRkIjp7ImRnMSI6IlVEeEpWRUU4VTAxSlZFZzhQRXBQU0U0OFBFcFBTRTRnVTAxSlZFZzhQREU1T0RBME1UVThUVDxQTnpjM056SXpNUT09IiwiZGcxMSI6Ik1USXpORFUyTnpnNVFVSkRSRVZHUjBoSlNrdE1UVTVQVUVGT1IxSlRWRlZXV0ZsYVUwRkVSVVU9Iiwic29kX21ydGQiOiJNSUlGempDQ0JMYWdBd0lCQWdJSVFPWTJLSkdGVFVJd0RRWUpLb1pJaHZjTkFRRUxCUUF3WHpFTE1Baz0ifSwiaWFzIjp7Imlhc19wayI6Ik1JSUJJakFOQmdrcWhraUc5dzBCQVFFRkFBT0NBUThBTUlJQkNnS0NBUUVBejEyMzQ1Njc4OTA9Iiwic29kX2lhcyI6Ik1JSUZhRENDQkZDZ0F3SUJBZ0lKQUwyS0pHRlRVSXdEUVlKS29aSWh2Y05BUUVMQlFBd1h6RUxNQT09IiwiY2hhbGxlbmdlX3NpZ25lZCI6ImExYjJjM2Q0ZTVmNjc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MGFiY2RlZjEyMzQ1Njc4OTBhYmNkZWY9PSJ9fQ.xyz456abc789def012ghi345jkl678mno901pqr234stu567vwx890yz123",
      "mrtd_auth_session":"wxroVrBY2MCq4dDNGXACS",
      "mrtd_pop_nonce":"9f2c4a7e3b1d8c9a6e5f4b2a1c3d7e8f"
    }

**The Wallet Instance MUST:**

- Perform `ICAO 9303`_ compliant NFC document reading (PACE, etc.).
- Validate document cryptographic signatures and certificate chains.
- Extract identity attributes (DG1 and DG11), Anti-Cloning Public Key from document data groups, and SODs (form MRTD and IAS Applications).
- Perform the Anti-Cloning Internal Authentication.
- Generate validation evidence in the JWT.
- Authenticate using a valid Wallet Instance Attestation.
- Include the exact ``mrtd_auth_session`` and ``mrtd_pop_nonce`` from the init response.
- Sign the ``mrtd_validation_jwt`` with its private key.
- Handle document reading errors and provide appropriate feedback.

**The MRTD PoP Service MUST:**

- Validate Wallet Instance Attestation according to IT-Wallet specifications.
- Verify OAuth-Client-Attestation-PoP signature.
- Validate the ``mrtd_auth_session`` parameter matches an active session.
- Verify the ``mrtd_pop_nonce`` matches the value sent in the previous response.
- Parse and validate the ``mrtd_validation_jwt`` signature (using Wallet Instance's public key) and structure.
- Extract and verify document evidence from the ``mrtd_validation_jwt``.
- Validate document authenticity using `ICAO 9303`_ standards.
- Verify Anti-Cloning challenge response.
- Validate document cryptographic proofs and certificate chains.
- Perform identity correlation between document data and LoA3 result.
- Check document validity (non revocation status).
- Verify the binding between IAS and MRTD applications by checking that the NUN extracted from DG1 is present (as hashed value) in the IAS SOD, and the DG1 itself is present (as hashed value) in the MRTD SOD. This dual verification ensures both applications reside on the same physical chip.

MRTD PoP Validation Response
""""""""""""""""""""""""""""

Upon successful completion of all checks by the MRTD PoP Service, it MUST send to the Wallet Instance an HTTP Response with code *202 Accepted* including the following parameters:

.. _table_eID_MRTD_PoP_Validation_Response:
.. list-table:: MRTD PoP Validation Response Parameters
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **status**
     - string
     - REQUIRED. It MUST be `require_interaction`.
   * - **type**
     - string
     - REQUIRED. It MUST be `redirect_to_web`.
   * - **mrtd_val_pop_nonce**
     - string
     - REQUIRED. New nonce for final confirmation.
   * - **redirect_uri**
     - string
     - REQUIRED. Browser redirect URI for completion of the Authorization Flow.

Below a non-normative example of an MRTD PoP Validation Response:

.. code-block:: http

    HTTP/1.1 202 Accepted
    Content-Type: application/json; charset=utf-8

    {
      "status": "require_interaction",
 	    "type": "redirect_to_web",
      "mrtd_val_pop_nonce": "0f2bff024317345b6927ce17e776361d",
      "redirect_uri":"https://eaa-provider.example.org/cb"
    }

**The MRTD PoP Service MUST:**

- Generate a new nonce  ``mrtd_val_pop_nonce`` for browser-based final confirmation.
- Return HTTP 202 status to indicate async processing completion.

**The Wallet Instance MUST:**

- Validate the response.
- Extracts the parameters nonce  ``mrtd_val_pop_nonce`` and  ``redirect_uri`` to prepare the next browser-based GET Request.

Browser-based Final Confirmation
"""""""""""""""""""""""""""""""""

Upon successful MRTD PoP validation, the Wallet Instance MUST redirect the User Agent to the ``challenge_redirect_uri`` specified in the initial Authorization Details Object, including the ``mrtd_val_pop_nonce`` and ``mrtd_auth_session`` as a query parameter:

.. code-block:: text

    https://eaa-provider.example.org/l2plus-callback?mrtd_val_pop_nonce=0f2bff024317345b6927ce17e776361d_signed&mrtd_auth_session=wxroVrBY2MCq4dDNGXACS

The Wallet Instance MUST validate that the ``mrtd_val_pop_nonce`` matches the value received from the MRTD PoP Validation Response.

**The Authorization Server MUST:**

- Validate the ``mrtd_val_pop_nonce`` matches the value sent in the verification response, and that it is signed using the Wallet Instance’s private key.
- Verify the ``mrtd_auth_session`` parameter matches an active session.
- Verify all authentication steps (LoA3 + MRTD PoP) have been completed successfully (including the identity correlation between LoA3 and document evidence).
- Generate the final authorization code.

Phase 4: OAuth Authorization Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upon successful completion of all authentication steps and identity matching, the Authorization Server MUST issue the final OAuth Authorization Response. If all validation checks have been passed, the Authorization Server MUST redirect the User Agent to the Wallet Instance with an OAuth Authorization Response including the authorization code as defined in steps 6-7 of :ref:`credential-issuance-low-level:Low-Level Issuance Flow`, and in Section :ref:`credential-issuance-endpoint:Authorization Response`. The Authorization Server MUST use the ``redirect_uri`` included in the initial Request Object by the Wallet Instance.

Error Management
----------------

The error management MUST follow the same rules as defined in the Section :ref:`credential-issuer-endpoint:Credential Issuance Endpoints`, regarding the formats and the related standard references.

During the MRTD PoP Validation flow, when recoverable errors occur, the MRTD PoP Service MAY generate and return a fresh nonce to enable the User to retry attempts while maintaining session security and preventing replay attacks.

In addition to the error codes already defined in the Section :ref:`credential-issuer-endpoint:Credential Issuance Endpoints`, at least the following error codes MUST be supported.

MRTD PoP Response Errors
^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_eID_MRTD_PoP_Response_Errors:
.. list-table:: MRTD PoP Response Error Codes
   :widths: 30 70
   :header-rows: 1

   * - **Error Code**
     - **Description**
   * - **invalid_client**
     - Wallet Instance authentication failed.
   * - **invalid_request**
     - HTTP Request is invalid or malformed (malformed structure, missing data, etc.) or required session parameters are missing or invalid.
   * - **access_denied**
     - User is not eligible for eID Substantial Authentication with MRTD Verification mechanism (e.g. CIE not found in the CIE Registry)
   * - **temporarily_unavailable**
     - Document validation service or CIE Registry service is temporarily unavailable.

MRTD PoP Validation Response Errors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_eID_MRTD_PoP_Validation_Response_Errors:
.. list-table:: MRTD PoP Validation Response Error Codes
   :widths: 30 70
   :header-rows: 1

   * - **Error Code**
     - **Description**
   * - **invalid_client**
     - Wallet Instance authentication failed.
   * - **invalid_request**
     - HTTP Validation Request or Validation JWT is invalid or malformed (due to a malformed structure, missing data, signature failure, request timeout, etc.).
   * - **access_denied**
     - User authentication or document validation failed.
   * - **invalid_document**
     - Document cryptographic validation failed (SOD validation, IAS/MRTD binding, revocation status, etc.).
   * - **id_matching_failed**
     - The matching between the identity obtained during primary authentication (eID LoA3) and the one obtained from the PoP of the Electronic Document failed.
   * - **temporarily_unavailable**
     - Document validation service or CIE Registry service is temporarily unavailable.

HTTP Status Code Mapping
^^^^^^^^^^^^^^^^^^^^^^^^^

Error responses MUST use appropriate HTTP status codes:

- **400 Bad Request**: For ``invalid_request`` errors.
- **401 Unauthorized**: For ``invalid_client`` errors.
- **403 Forbidden**: For ``access_denied`` errors.
- **422 Unprocessable Entity**: For ``invalid_document`` or ``id_matching_failed`` errors.
- **503 Service Unavailable**: For ``temporarily_unavailable`` errors.

Security Considerations
-----------------------

Secure Session Management
^^^^^^^^^^^^^^^^^^^^^^^^^

The ``mrtd_auth_session`` parameter serves as the primary correlation mechanism between authentication steps. Implementations MUST ensure this identifier has sufficient entropy (minimum 128 bits) and is cryptographically secure. The session identifier MUST be validated at each step to prevent session fixation attacks.

Each authentication step MUST be cryptographically bound to the OAuth session through signed JWT validation to prevent session fixation, session confusion, and identity substitution attacks. The Authorization Server MUST maintain the correlation between the LoA3 identity and the document proof within a single session context.

In particular, each authentication step MUST validate the correlation between:

- Session identifier consistency across all protocol phases.
- LoA3 identity attributes binding to the session context.
- Document evidence correlation with authenticated identity.
- Temporal sequence validation to prevent out-of-order attacks.

When components operate outside the EAA Provider boundary, the following additional security measures MUST be implemented:

- Secure Inter-Service Communication (for example, through Certificate pinning, mutual TLS, etc.).
- Encryption and integrity of sensitive session data and/or personal identity information (for example, using JWE/JWS tokens).
- Distributed locks for session state updates.

.. _fig_eID_MRTD_Security_Controls:
.. plantuml:: plantuml/l2plus-security-controls.puml
    :width: 99%
    :alt: The figure illustrates the eID Substantial Authentication with MRTD Verification Security Controls.
    :caption: `eID Substantial Authentication with MRTD Verification Security Controls. <https://www.plantuml.com/plantuml/svg/nLTzRzks4_vVd-9-ATfVuiP9dNHRPzH9LJil7jh4Y9mMsp8Oj7IskSgaHb9Eiay_tacMxAGkCcp004EmgNjvxdcEH_gTTSAuV9u6__-Vc-4S8KQJfoXKK-SkbGe3aJkjylaOJP1vMndBJ2W7MzSMpHO82zVhwvz5cgA3llAXLOni4gwRTFidlDmDnleEOEia365Wz48c5FBP1pcTkVTfZkjUP1NcRgQD_5CugHL4Q1ObY31QD_vuDUp1G0_OHfOmUeFBGHIWIi3dVGG9BZYgIE4Afz8wSyzE7_iNwwPBinlLJr0vwUvhyEJGxms28F3hAGBsU_11XuSCd8pZ0lbBC3ZN3a4kGsH6wubKKv0A-iFcaiKUzAtDYKWuJVLj45n3ymZ2DdmcB4w3Y9rS28VWuqFfTQDoIw4eUvIFIGWdHVeGnArqCs2YFg6Hat8v23gT3WncmYAqsd19JWzuly8_ShGEEfqWP3WHj64GNbKljW7YLA9o8vdiWYbMByU_O-nsF3eeKdFePfSDcw5ptgQ8BrIoyMMJH9MAopr7uKadSuhPQ71KiGfrbA0JCWLtdo5iIJTA3rucEixdX8qftseqWi0NqAGwgZ9iffL5s2wXZt8ZTm7lCcdGZgJQMTRTNjDg0qq4xkna2FjBQ7XSiTFPszjxiPA5VfFzkRQk3IX4CojxQm_ln3nBSK-RwQf61nwpaNDXxX_gs-G6e7twDUMfBrUxWzGqYdfIByWZyXjHB53vr7ulsbaGTGzfxx0DCtP4hTwc9Elngye3_nxU4hFNxGA7UBWDOk9PiMN1w8PuXI1F1xZAq64Rgd7mIQGouQ3SlL6vcyw7my5-Qwy5XwyEu5Jdt54VT96-3JFdCjlUt-TfkNVBUg_giH_FQ4rDyRZHc1kN5BtLULj_7_tqUNX4lRPQmkCAVbYfW7kCPrRRDtTLGabket6Z1fUHRojCTDpa9FjIILSLuqluTXlTg7zp7wwLnh0Vb_VzBaJTD_JuSQLGdRa00DY95A6PsmPVg3CI5-ZL-mMaccWpvzHaIoRGhFXvQ4B1Ww2CHnAlCbYr4r5OAN_WbG_Z63E7IKbCePxEHagh67UXKfcPsTPPSH2azpkSFn5E18587VGd1I0BIZiG2o5JCKuHd6Q-7XoHN4y8l4sMwfAfz12DWsvumHRBoT-lbp6r2B9AfiTEI8K920UHmmnQhIesUPxSEIDYnq1XOlIS70kgfaRdMNdq_eofFshWuhJhSpaabsfe47pUoPvgw9MJ50RKVE0_0sqjMalcVitfMATyRX6A9PHVdqqDelhj2BfGoH9cMLhFhK7OFI5nhb0aq3jhxTB3FwFBteZCELGNcdKicjrViuHWKzf-6ArchTA5D7PIhUW07UHZ_nw-u7qHaNmsv7wIspgCTIUcMZqwfM-KvLjEtNmR05n5OVFWrUitOELK2PSR945ygDgJfDuuLkh9-Cq9iw2hmlr_DcC0_jwKeOVlXy0_3_Zx8JzVhqoVzQb3XIq9u2PV42zqGoDGkLsIUgEMzmYw9IpAey9pZV6NdI1uC9vMfimhkFpob57P-ewHSYsj-bZOFDLg0Pyyu0mcqc3CDmzMWYUUhxYUUjmld8hwwXi6t4tlZRwrQ9fZOJ61KqdztDLg8isyscLq5LeUg9kwPZyU7tFqpkE48mA2oGjDbubHEMxu7aKAON63sdOpe_Ff3CO5eftrW_V9HrDzYtYzwIvSK5rV9rYLpTV2seCbu91TdR1M__0QSkojOvsK543D1_sGrdOumFF3yFd1gVzi8d-TgbqcgtzsFZoxEZcv28OpX0cDz5Wh9rME5aGSQvFG47DwmvyNzX0M4fpG2RNSrRMnpJ2k_eFK0hppt_9v-XS0>`_

Cryptographic Challenge Generation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The MRTD PoP Service MUST generate cryptographically secure challenges with sufficient entropy (minimum 256 bits) for document validation. Challenge values MUST be unique and MUST NOT be reused across different sessions (cryptographically bound to the specific OAuth session context) or authentication attempts. The challenge generation algorithm SHOULD incorporate the ``mrtd_auth_session`` identifier and timestamp to ensure proper cryptographic binding.

Nonce Lifecycle Management
^^^^^^^^^^^^^^^^^^^^^^^^^^

Each step in the eID Substantial Authentication with MRTD Verification flow MUST use unique nonce values (minimum 128 bits) to prevent replay attacks. Nonce values MUST have appropriate expiration times and MUST be invalidated after successful use. The EAA Authorization Server and MRTD PoP Service MUST maintain synchronized nonce validation to ensure session integrity.

Moreover, each nonce serves a specific security purpose.
- ``mrtd_pop_jwt_nonce`` MUST be correlated with the MRTD Proof JWT.
- ``mrtd_pop_nonce`` MUST:

- Be cryptographically independent from ``mrtd_pop_jwt_nonce``.
- Incorporate the ``mrtd_pop_jwt_nonce`` as input to maintain the chain of trust.
- Use a different entropy source to prevent correlation attacks.

 - ``mrtd_val_pop_nonce`` MUST:

- Be signed by the Wallet Instance private key.
- Include anti-replay timestamp validation.
- Be verified against the entire nonce chain for integrity.

EAA Provider Metadata
^^^^^^^^^^^^^^^^^^^^^^

In addition to the ``trust_frameworks_supported`` values defined in section :ref:`credential-issuer-metadata:Metadata for openid_credential_issuer`, the EAA Provider Metadata for ``openid_credential_issuer`` MUST also support the value ``it_l2+document_proof`` indicating the multi-step Authentication protocol described in this Specification.

Security Controls
^^^^^^^^^^^^^^^^^

The following security controls MUST be implemented in the protocol:

.. _table_eID_MRTD_Security_Controls:
.. list-table:: eID Substantial Authentication with MRTD Verification Security Controls
   :widths: 10 60 30
   :header-rows: 1

   * - **#**
     - **Description**
     - **Phase**
   * - **SC1**
     - The network communication channels are protected by using TLS with secure ciphers (at the time of this release, it is at least TLS v1.2).
     - All
   * - **SC2**
     - The Wallet Instance ensures the authenticity of the EAA Provider and the eID Identity Provider by pinning the leaf certificate of each server.
     - All
   * - **SC3**
     - The EAA Authorization Server verifies that the eID Identity Provider used within the *eID LoA3* phase is trustworthy.
     - Phase 2
   * - **SC4**
     - The EAA Authorization Server verifies the authenticity and integrity of the data extracted from the *eID LoA3* assertion, by checking the digital signature.
     - Phase 2
   * - **SC5**
     - The challenge value and all nonce values are generated with safeguards to prevent bruteforce or guessing attacks.
     - Phase 3
   * - **SC6**
     - The EAA Provider verifies all the nonce values to detect replay attacks.
     - Phase 3
   * - **SC7**
     - The Wallet Instance verifies that ``challenge_info`` is properly signed by the EAA Authorization Server. Moreover, it checks that ``challenge_info`` contains: an ``iss`` value corresponding to the value of the EAA Authorization Server; an ``aud`` value equal to the ``client_id`` of the Wallet Instance; and a ``state`` value equal to the one in the PAR request, to be sure that the response is bound to the initial request that is made by the Wallet Instance in Step 2. Therefore the information provided as part of ``challenge_info``, in particular the ``htu`` that corresponds to the redirect url to follow for the *MRTD PoP*, is not tampered with.
     - Phase 3
   * - **SC8**
     - The EAA Provider checks that the ``mrtd_auth_session`` is associated with the same Wallet Instance in all the requests within the *MRTD PoP* phase. Therefore the EAA Provider can be sure that the Wallet Instance performing the *MRTD PoP* phase: is trusted; is always the same across the protocol; and has previously started the IT-Wallet ID issuance (PAR request). This can be implemented by requesting the Wallet Instance to perform a proof of possession of its private key (e.g., within OAuth-Client-Attestation or by signing a nonce value).
     - Phase 3
   * - **SC9**
     - The EAA Provider checks that the ``mrtd_auth_session`` is not expired (validity timeout typically of 5 minutes), i.e., that the operation has been concluded within a certain amount of time.
     - Phase 3
   * - **SC10**
     - The integrity and confidentiality of the channel between the *physical CIE* and the *physical device_wallet* is secured with the PACE protocol (via the algorithm and key derivation functions supported by the card).
     - Phase 3
   * - **SC11**
     - The MRTD PoP Service verifies the authenticity and integrity of the ``mrtd_validation_jwt`` by checking that it is signed with the Wallet Instance private key associated with the ``mrtd_auth_session``.
     - Phase 3
   * - **SC12**
     - The MRTD PoP Service verifies that challenge_signed contained in ``mrtd_validation_jwt`` corresponds to the original challenge signed with the CIE AntiClone private key (``SDO.Servizi_Int_Kpriv``). This demonstrates the Wallet Instance and the CIE performed the Internal Authentication (in line with Sec. 5.2.3.5.1 in IAS ECC, but with randomness value ``RND.IFD`` provided by the MRTD PoP Service instead of generating it in the Wallet Instance).
     - Phase 3
   * - **SC13**
     - The MRTD PoP Service verifies the authenticity of the data extracted from the CIE by checking the SOD elements (both IAS and MRTD) and the related signature certificate chains.
     - Phase 3
   * - **SC14**
     - The MRTD PoP Service verifies the integrity of the data extracted from the CIE by checking the SOD elements (both IAS and MRTD) and the related hashes.
     - Phase 3
   * - **SC15**
     - The MRTD PoP Service verifies that the binding between IAS and MRTD applications by checking that the NUN extracted from DG1 is present (as hashed value) in the IAS SOD, and the DG1 itself is present (as hashed value) in the MRTD SOD. This dual verification ensures both applications reside on the same physical chip.
     - Phase 3
   * - **SC16**
     - The MRTD PoP Service verifies that the identity proven during the eID LoA3 phase is correlated with the identity proven during the MRTD PoP phase.
     - Phase 3
   * - **SC17**
     - The MRTD PoP Service verifies that the CIE used during the MRTD PoP phase has not expired and not revoked by interacting with the CIE National Registry.
     - Phase 3

Additional implementation requirements:

	- **Rate limiting**: Protection against automated attacks and brute force attempts.
	- **Session timeout**: Automatic cleanup of incomplete authentication sessions.
	- **Audit logging**: Comprehensive logging of all authentication events with correlation identifiers.
	- **Error handling**: Secure error responses that do not leak sensitive information.
	- **Cryptographic material cleanup**: Secure deletion of temporary keys and challenges.

Implementation Considerations
-----------------------------

Implementations SHOULD incorporate rate-limiting mechanisms to protect against automated attacks and resource exhaustion, and a timeout configuration balancing user experience and security posture, accommodating the variability inherent in NFC-based document reading.

EAA Provider SHOULD implement session timeouts approach with proper cleanup mechanisms, ensuring session resources are released and temporary cryptographic material is securely deleted when sessions expire.

All security-relevant events throughout the eID Substantial Authentication with MRTD Verification flow MUST be logged with sufficient detail for auditing purposes while preserving the privacy of the User, ensuring that personally identifiable information, when stored, is appropriately hashed. The audit logs SHOULD have consistent correlation identifiers, enabling end-to-end tracing across all protocol phases, with cryptographic integrity protection to prevent tampering.


