.. include:: ../common/common_definitions.rst
.. Included via test-plans.rst at title level '-' (level 1).


Credential Issuer Test Matrix
---------------------------------

This section provides the set of test cases designed for technical implementers and development teams responsible for creating and deploying Credential Issuer solutions. It is also intended for assessment bodies inspecting and validating the implementations of Credential Issuer solutions.


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - **Test Case ID**
    - **Purpose**
    - **Description**
    - **Expected Result**
  * - CI_001
    - Trust, Security
    - Entity Configuration publication
    - Federation Entity publishes its own Entity Configuration in the .well-known/openid-federation endpoint.
  * - CI_002
    - Trust, Interoperability
    - Entity Configuration response media type check
    - The Entity Configuration HTTP Response is set to media type to application/entity-statement+jwt.
  * - CI_003
    - Trust, Security
    - Entity Configuration cryptography
    - The Entity Configuration is cryptographically signed
  * - CI_004
    - Trust, Security
    - Public Key inclusion in Entity Configuration and Subordinate Statement
    - The Entity Configuration and the Subordinate Statement issued by the immediate superior both include the public part of the key.
  * - CI_005
    - Trust, Security
    - Entity Configuration's Trust Marks
    - The Entity Configuration contains one or more Trust Marks.
  * - CI_006
    - Trust, Interoperability
    - Entity Configurations parameters
    - Entity Configurations have in common these parameters: iss, sub, iat, exp, jwks, metadata.
  * - CI_007
    - Voided
    - Voided
    - Voided
  * - CI_008
    - Trust, Interoperability
    - Credential Issuer metadata
    - Credential Issuer successfully provides the following metadata types: *federation_entity*, *Oauth_authorization_server* and *openid_credential_issuer*
  * - CI_009
    - Trust, Interoperability
    - Inclusion of *openid_credential_verifier* Metadata in User Authentication via Wallet
    - When the (Q)EAA Providers authenticate users through their Wallet Instance, the *openid_credential_verifier* metadata is included in addition to the required metadata parameters.
  * - CI_010
    - Issuance, Interoperability
    - Credential Offer URI Structure
    - Credential Issuer generates a Credential Offer consisting of a single URI query parameter named "credential_offer"ensuring the URL is well-formed and contains only this parameter for the offer data.
  * - CI_011
    - Issuance, Interoperability
    - Credential Offer Delivery Methods
    - Credential Offer URL is successfully embedded in QR codes or included as clickable href buttons in HTML pages.
  * - CI_012
    - Issuance, Interoperability
    - Credential Offer Mandatory Parameters
    - Credential Offer contains all three mandatory parameters (credential_issuer, credential_configuration_ids, and grants) with valid values
  * - CI_013
    - Issuance, Interoperability
    - Credential Offer Grants Parameter Structure
    - The grants parameter successfully contains an ``authorization_code`` object that includes both required sub-parameters (``issuer_state`` and ``authorization_server``) with appropriate values.
  * - CI_014
    - Issuance, Interoperability
    - Credential Object Compilation
    - Credential Issuer ensures the Credential Object is properly compiled with all required fields, correct formatting, and valid data structures before delivery
  * - CI_015
    - Issuance, Security
    - PAR Request Object Signature Validation
    - Credential Issuer successfully validates the Request Object signature
  * - CI_015a
    - Issuance, Security
    - PAR Request Object Algorithm Header Processing
    - Credential Issuer uses the algorithm specified in the alg header parameter (:rfc:`9126`/:rfc:`9101`) to validate the Request Object Signature
  * - CI_015b
    - Issuance, Security
    - PAR Wallet Attestation Public Key Retrieval
    - Credential Issuer successfully retrieves the public key from the Wallet Attestation's cnf.jwk claim
  * - CI_015c
    - Issuance, Security
    - PAR JWT Key Identifier Reference
    - The Credential Issuer successfully references the correct key via the kid JWT header parameter
  * - CI_015d
    - Issuance, Security
    - PAR Cryptographic Signature Integrity Validation
    - The Credential Issuer successfully complete cryptographic signature integrity before proceeding with any further validations
  * - CI_016
    - Issuance, Interoperability
    - PAR HTTP POST Parameter Encoding
    - Credential Issuer successfully processes HTTP POST requests with message body parameters encoded in application/x-www-form-urlencoded format;
  * - CI_017
    - Issuance, Interoperability
    - PAR Scope and Authorization Details Interpretation
    - When a request contains both scope value and authorization_details parameter, Credential Issuer processes each parameter independently
  * - CI_017a
    - Issuance, Interoperability
    - PAR Authorization Details
    - When both scope and authorization_details request the same Credential type, Credential Issuer follows the specifications given by the authorization_details object
  * - CI_018
    - Voided
    - Voided
    - Voided
  * - CI_019
    - Issuance, Security
    - PAR Algorithm Compliance Check
    - Credential Issuer verifies the signing algorithm in the alg header matches one of the approved algorithms listed in the Cryptographic Algorithms section; rejects requests with non-compliant algorithms and returns appropriate error.
  * - CI_020
    - Issuance, Security
    - PAR Client ID Consistency Validation
    - Credential Issuer confirms the client_id in the PAR request body exactly matches the client_id claim in the Request Object; mismatched values trigger request rejection with clear error message.
  * - CI_021
    - Issuance, Security
    - Issuer-Client ID Matching in the PAR request
    - Credential Issuer validates that the iss claim in the Request Object matches the client_id claim within the same Request Object (:rfc:`9126`/:rfc:`9101`); discrepancies result in request denial.
  * - CI_022
    - Issuance, Security
    - PAR Audience Claim Verification
    - Credential Issuer confirms the aud claim in the Request Object equals the Credential Issuer's own identifier (:rfc:`9126`/:rfc:`9101`); incorrect audience values cause immediate request rejection.
  * - CI_023
    - Issuance, Security
    - PAR Request URI Parameter Rejection
    - Credential Issuer detects and rejects any PAR request containing the request_uri parameter (:rfc:`9126`), returning an appropriate error response indicating the parameter is not supported.
  * - CI_024
    - Issuance, Security
    - PAR Mandatory Parameters Validation
    - Credential Issuer verifies all mandatory HTTP parameters are present in the Request Object and validates their values against the defined Table specifications (derived from :rfc:`9126`); missing or invalid parameters trigger structured error responses.
  * - CI_025
    - Issuance, Security
    - PAR Token Expiration Check
    - Credential Issuer validates the Request Object has not expired by checking the exp claim against current time; expired tokens are rejected with timestamp-related error messages.
  * - CI_026
    - Issuance, Security
    - PAR Token Issuance Time Validation
    - Credential Issuer confirms the iat claim represents a past timestamp
  * - CI_026a
    - Issuance, Security
    - Recommended PAR Token Issuance Time rejection
    - Credential Issuer reject requests where iat is more than 5 minutes from current time (:rfc:`9126`); timing violations result in "invalid_request" errors.
  * - CI_027
    - Issuance, Security
    - PAR Replay Attack Prevention
    - Credential Issuer successfully checks that the jti claim in the Request Object has not been used before by the Wallet Instance identified by the client_id.
  * - CI_028
    - Issuance, Security, Interoperability
    - OAuth Client Attestation PoP Validation
    - .Credential Issuer successfully validates the OAuth-Client-Attestation-PoP parameter according to Section 5 of [`OAUTH-ATTESTATION-CLIENT-AUTH`_], confirming proof-of-possession and rejecting invalid attestations with detailed error responses.
  * - CI_029
    - Issuance, Trust
    - Wallet Instance Trustworthiness Verification
    - Credential Issuer successfully verifies the trustworthiness and indirect Federation membership of the Wallet Instance through comprehensive Wallet Attestation validation
  * - CI_030
    - Issuance, Trust
    - Wallet Provider Federation Membership Validation
    - Credential Issuer confirms the Wallet Provider (issuer of the Wallet Attestation) is a recognized and trusted Federation member by checking Federation registries and trust lists;
  * - CI_031
    - Issuance, Security
    - Wallet Attestation Cryptographic Signature Validation
    - Credential Issuer successfully validates the cryptographic signature of the Wallet Attestation using the Wallet Provider's public key, ensuring signature integrity and authenticity;
  * - CI_032
    - Issuance, Security
    - Wallet Attestation Expiration Check
    - Credential Issuer verifies the Wallet Attestation has not expired at verification time by checking timestamp claims against current time
  * - CI_033
    - Issuance, Security
    - Wallet Attestation Attested Cryptographic Key Acceptance
    - Credential Issuer accepts and uses only cryptographic keys that are properly derived from the attested Wallet Instance during the credential issuance process;
  * - CI_034
    - Issuance, Security
    - Wallet Attestation Device Security and Compliance Verification
    - Credential Issuer relies on Wallet Attestation claims to confirm the Wallet Instance operates on a secure, trusted device that meets the Issuer's required security standards;
  * - CI_035
    - Issuance, Trust
    - Wallet Provider Trust Chain Evaluation
    - Credential Issuer successfully evaluates the complete Trust Chain of the Wallet Attestation's issuer (Wallet Provider)
  * - CI_036
    - Issuance, Trust, Interoperability
    - Federation Metadata Retrieval
    - Credential Issuer successfully uses Federation API endpoints (.well-known/openid-federation, /fetch) to retrieve current metadata and configurations of Federation participants, including Wallet Providers
  * - CI_037
    - Issuance, Trust, Interoperability
    - Wallet Provider Trust Establishment
    - Credential Issuer establishes trust in the Wallet Provider as an authorized Federation entity by querying Federation API endpoints (e.g., .well-known/openid-federation, /fetch) and validating the provider's federation status through official channels and trust verification processes.
  * - CI_038
    - Voided
    - Voided
    - Voided
  * - CI_039
    - Voided
    - Voided
    - Voided
  * - CI_040
    - Issuance, Security
    - Recommended PAR Response Request URI Validity Duration
    - request_uri validity time is set to less than one minute
  * - CI_041
    - Issuance, Security
    - PAR response Request URI Cryptographic Random Value Integration
    - Generated request_uri includes a cryptographic random value of at least 128 bits
  * - CI_042
    - Issuance, Security
    - Recommended PAR response Request URI Length Limitation
    - Complete request_uri doesn't exceed 512 ASCII characters
  * - CI_043
    - Issuance, Interoperability
    - PAR Response Successful Verification Response
    - When verification is successful, Credential Issuer returns an HTTP response with 201 status code
  * - CI_044
    - Issuance, Interoperability
    - JSON PAR Response Structure
    - HTTP response message body uses application/json media type (:rfc:`8259`) and includes the required top-level parameters
  * - CI_044a
    - Issuance, Security
    - PAR Response request_uri Parameter
    - HTTP response includes request_uri parameter containing the generated one-time authorization URI
  * - CI_044b
    - Issuance, Security
    - PAR Response expires_in Parameter
    - HTTP response includes expires_in parameter specifying the validity duration in seconds
  * - CI_045
    - Issuance, Interoperability
    - PAR Response HTTP Status Code table
    - When PAR request processing encounters errors, the Credential Issuer responds as defined in :rfc:`9126`, according to the :ref:`Table of HTTP Status Codes <table_par_error_code>`.
  * - CI_046
    - Issuance, Security and Privacy
    - User Identity Verification during authorization request
    - Authorization Server successfully verifies the identity of the User who owns the credential through appropriate authentication mechanisms, confirming user ownership before proceeding with credential authorization
  * - CI_047
    - Issuance, Security
    - Request URI One-Time Use and Expiration in the Authorization Request
    - Credential Issuer treats each request_uri value as single-use only and successfully rejects any expired requests
  * - CI_048
    - Issuance, Security
    - Optional Duplicate Request Tolerance in the Authorization Request
    - Credential Issuer allow duplicate requests when they result from User reloading or refreshing their user-agent (derived from :rfc:`9126`)
  * - CI_049
    - Issuance, Security
    - PAR Request Identification in the Authorization Request
    - Credential Issuer successfully identifies and correlates each authorization request as a direct result of a previously submitted PAR (derived from :rfc:`9126`)
  * - CI_050
    - Issuance, Security
    - Request URI Parameter Requirement of the Authorization Request
    - Credential Issuer rejects all Authorization Requests that do not contain the request_uri parameter, since PAR is the exclusive method for passing Authorization Requests from the Wallet Instance (derived from :rfc:`9126`).
  * - CI_051
    - Issuance, Security
    - CieID High-Level Authentication
    - PID Provider successfully performs User authentication based on CieID scheme with LoAHigh (CIE L3)
  * - CI_052
    - Issuance, Security and Privacy
    - User Consent for PID Issuance
    - PID Provider obtains explicit User consent before proceeding with PID issuance
  * - CI_053
    - Issuance, Privacy
    - Optional Contact Details Collection
    - PID Provider MAY request User's contact details (email, phone number) for sending notifications about the issued PID
  * - CI_054
    - Presentation, Issuance Security
    - PID-Based User Authentication
    - (Q)EAA Provider successfully performs User authentication by requesting and validating a valid PID from the Wallet Instance
  * - CI_055
    - Presentation, Issuance, Interoperability
    - OpenID4VP Protocol Usage
    - (Q)EAA Provider uses OpenID4VP protocol to request PID presentation from the Wallet Instance
  * - CI_056
    - Presentation, Issuance, Security
    - Presentation Request Delivery
    - (Q)EAA Provider successfully provides the presentation request to the Wallet
  * - CI_057
    - Issuance, Privacy
    - Optional Contact Details Collection for Credentials
    - Credential Issuers request User's contact details (email, phone number) for sending notifications about issued Digital Credential(s)
  * - CI_058
    - Issuance, Interoperability
    - Authorization Response parameters validation
    - Credential Issuer successfully sends an authorization code response to the Wallet Instance that includes all three required parameters
  * - CI_058a
    - Issuance, Security
    - Authorization Response code parameter validation
    - Authorization code response includes the authorization code parameter
  * - CI_058b
    - Issuance, Security
    - Authorization Response state parameter validation
    - Authorization code response includes the state parameter matching the original request
  * - CI_058c
    - Issuance, Security
    - Authorization Response iss parameter validation
    - Authorization code response includes the iss parameter identifying the issuer
  * - CI_059
    - Issuance, Interoperability
    - Authorization Response HTTP Status Code table
    - When Authorization Response encounter errors, the Authorization Server redirects the User to the redirect_uri HTTP status code 302 according to the HTTP Status Code table
  * - CI_060
    - Issuance, Security
    - Authorization Code Issuance Verification of the Token request
    - Credential Issuer ensures the Authorization code is issued to the authenticated Wallet Instance (:rfc:`6749`) and has not been replayed
  * - CI_061
    - Issuance, Security
    - Authorization Code Validity and Usage Check of the Token Request
    - Credential Issuer verifies the Authorization code is valid and has not been previously used (:rfc:`6749`).
  * - CI_061a
    - Issuance, Security
    - PKCE ``code_verifier`` Verification in Token Request
    - The Credential Issuer verifies that the ``code_verifier`` parameter is present and matches the ``code_challenge`` associated with the authorization code (:rfc:`7636`); in case of mismatch, the request is rejected.
  * - CI_062
    - Issuance, Security
    - Redirect URI Matching Validation of the Token Request
    - Credential Issuer confirms the redirect_uri exactly matches the value included in the previous Request Object (see Section 3.1.3.1. of [`OIDC`_]).
  * - CI_063
    - Issuance, Security
    - DPoP Proof JWT Validation of the Token Request
    - Credential Issuer successfully validates the DPoP Proof JWT, according to (:rfc:`9449`) Section 4.3.
  * - CI_064
    - Issuance, Interoperability
    - Access Token Provision in the token response
    - Credential Issuer provides the Wallet Instance with a valid Access Token upon successful authorization
  * - CI_065
    - Issuance, Interoperability
    - Optional Refresh Token Provision
    - If supported by the Credential Issuer, a Refresh Token is provided to the Wallet Instance
  * - CI_066
    - Issuance, Security
    - DPoP Key Binding for Access Token and Refresh Token
    - Both Access Token and Refresh Token (when issued) are cryptographically bound to the DPoP key
  * - CI_067
    - Issuance, Interoperability
    - Token Response HTTP Status Code table
    - When any errors occur during the validation of the Token Request, the Authorization Server return an error response as defined in :rfc:`6749`, according to the HTTP Status Code Table
  * - CI_068
    - Issuance, Interoperability
    - c_nonce Provision
    - Credential Issuer provides a c_nonce value to the Wallet Instance
  * - CI_069
    - Issuance, Security
    - C_nonce Format and Security
    - The c_nonce parameter is provided as a string value with sufficient unpredictability to prevent guessing attacks, serving as a cryptographic challenge that the Wallet Instance uses to create proof of possession of the key (proofs claim)
  * - CI_070
    - Issuance, Security
    - C_nonce Reusability and Renewal
    - The received c_nonce value can be reused by the Wallet Instance to create multiple proofs until the Credential Issuer provides a new c_nonce value
  * - CI_071
    - Issuance, Interoperability
    - JWT Proof Required Claims Validation
    - JWT proof successfully includes all required claims as specified in the Token Request table
  * - CI_072
    - Issuance, Security
    - Batch JWT Proof Required Claims Validation
    - Credential Issuer successfully verify that the jwk attribute in each key proof is unique
  * - CI_073
    - Issuance, Interoperability
    - Credential Request Key Proof Type Declaration
    - Key proof is explicitly typed using appropriate header parameters defined for the respective proof type
  * - CI_074
    - Issuance, Security
    - Asymmetric Algorithm Requirement in the Credential Request
    - The header parameter alg indicates a registered asymmetric digital signature algorithm and is never set to none
  * - CI_075
    - Issuance, Security
    - Credential Request Public Key Signature Verification
    - Signature on the key proof is successfully verified using the public key specified in the header parameter
  * - CI_076
    - Issuance, Security
    - Private Key Header Exclusion in the Credential Request
    - Header parameters do not contain any private key material
  * - CI_077
    - Issuance, Security
    - c_nonce Matching in the Credential Request
    - When a c_nonce value was previously provided by the server, the nonce claim in the JWT exactly matches this c_nonce value
  * - CI_078
    - Issuance, Security
    - JWT Temporal Validity in the Credential Request
    - The creation time of the JWT (via iat claim or server-managed timestamp through nonce claim) falls within the server's acceptable time window
  * - CI_079
    - Voided
    - Voided
    - Voided
  * - CI_080
    - Issuance, Interoperability
    - Recommended Fresh Cryptographic Key Generation in the Credential Request
    - Credential Issuer registers all issued Credentials in a revocation registry for potential future revocation needs
  * - CI_081
    - Issuance, Security
    - Recommended Deferred Flow support
    - When the requested Credential cannot be issued immediately and requires more time, the Credential Issuer supports the Deferred Flow
  * - CI_081a
    - Issuance, Security
    - Deferred Flow batch issuance consistency
    - When using the Deferred Flow for batch issuance, the same transaction_id allows retrieval of all Credentials requested in the batch.
  * - CI_082
    - Issuance, Security
    - DPoP JWT Proof and Access Token Validation in the Credential Response
    - Credential Issuer successfully validates the DPoP JWT Proof based on the steps defined in Section 4.3 of (:rfc:`9449`) procedures and confirms the Access Token is valid and suitable for the requested Credent
  * - CI_083
    - Issuance, Security
    - Key Material Proof of Possession Validation in the Credential Response
    - Credential Issuer validates the proof of possession for the key material to which the new Credential will be bound, according to `OpenID4VCI`_ Appendix F.4.
  * - CI_084
    - Issuance, Security
    - Credential Creation and Binding in the Credential Response
    - When all validation checks succeed, Credential Issuer creates a new Credential cryptographically bound to the validated key material and provides it to the Wallet Instance
  * - CI_084a
    - Issuance, Security
    - Credential type check
    - Credential Issuer ensure the credential type matches the request before issuing the new Credential
  * - CI_085
    - Issuance, Interoperability
    - Credential Response Table of HTTP Status Codes
    - When the Credential Request does not contain a valid Access Token, the Credential Endpoint returns an error response such as defined in Section 3 of [:rfc:`6750`], according to the :ref:`Table of HTTP Status Codes <table_credential_error_code>`.
  * - CI_086
    - Issuance, Interoperability
    - Unified Notification ID for Batch Operations
    - For batch-issued Digital Credentials, a single notification_id covers the entire batch-issued Credentials. The notification response applies to all Credentials, any partial failure is treated as a batch failure.
  * - CI_087
    - Issuance, Interoperability
    - Notification Response Table of HTTP Status Codes
    - When the Notification Request does not contain a valid Access Token, the Notification Endpoint returns an error response such as defined in Section 3 of [:rfc:`6750`], according to the :ref:`Table of HTTP Status Codes <table_notification_error_code>`.
  * - CI_088
    - Issuance, Security
    - Access Token Scope Restriction
    - Access Token obtained through a Refresh Token flow is successfully limited to three specific endpoints: Deferred endpoint, Notification endpoint and Credential endpoint
  * - CI_088a
    - Issuance, Security
    - Deferred Endpoint Access Authorization
    - Access Token allows access to Deferred endpoint for obtaining new Digital Credentials after interval or readiness notification
  * - CI_088b
    - Issuance, Security
    - Notification Endpoint Access Authorization
    - Access Token allows access to Notification endpoint for notifying Digital Credential deletion to the Credential Issuer
  * - CI_089c
    - Issuance, Security
    - Credential Endpoint Access Authorization
    - Access Token allows access to Credential endpoint for Digital Credential refresh/re-issuance of existing credentials
  * - CI_090
    - Voided
    - Voided
    - Voided
  * - CI_091
    - Issuance,Interoperability
    - OAuth Client Attestation PoP Validation for Refresh
    - Credential Issuer successfully validates the OAuth-Client-Attestation-PoP parameter based on Section 5 of [`OAUTH-ATTESTATION-CLIENT-AUTH`_]
  * - CI_092
    - Issuance, Security
    - DPoP Proof JWT Validation for Refresh
    - Credential Issuer validates the DPoP Proof JWT according to (:rfc:`6949`) Section 4.3.
  * - CI_093
    - Issuance, Security
    - Refresh Token Validity and Key Binding Check
    - Credential Issuer verifies the Refresh Token is not expired, not revoked, and is bound to the same DPoP keys used in the DPoP Proof JWT
  * - CI_094
    - Issuance, Security
    - Access Token Generation and Bound
    - When all validation checks succeed, Credential Issuer generates new Access Token and new Refresh Token, both bound to the DPoP key
  * - CI_095
    - Issuance, Security
    - Successful Refresh Token Response
    - Both the Access Token and the Refresh Token are sent back to the Wallet Instance
  * - CI_096
    - Issuance, Security
    - Invalid Refresh Token Error Handling
    - When the Refresh Token is expired or invalid, Credential Issuer issues an error response with error type member set to invalid_grant
  * - CI_097
    - Issuance, Security
    - Refresh Token Confidentiality Protection
    - Confidentiality of Refresh Tokens is guaranteed both in transit and storage through appropriate encryption and secure handling mechanisms
  * - CI_098
    - Issuance, Security
    - TLS-Protected Refresh Token Transmission
    - All token transmissions use TLS-protected connections, ensuring encrypted communication channels for token exchange
  * - CI_099
    - Issuance, Security
    - Refresh Token Security Properties
    - Refresh tokens are generated with unguessable values and protected from modification through cryptographic integrity mechanisms
  * - CI_100
    - Voided
    - Voided
    - Voided
  * - CI_101
    - Issuance, Security
    - Consistent DPoP Key Binding between Refresh and Access token
    - Access Tokens and Refresh Tokens are bound to the same DPoP key
  * - CI_102
    - Issuance, Security
    - DPoP Proof Requirement for Refresh Token
    - DPoP Proof is required for all refresh token operations to obtain new Access Tokens
  * - CI_103
    - Issuance, Security
    - Consistent DPoP Key Usage for Refresh Token
    - The same DPoP key is used to generate Access Token DPoP Proofs across all Credential Requests
  * - CI_104
    - Issuance, Security
    - Refresh Token Usage Duration Management
    - Credential Issuers manage and limit the duration for which refresh tokens can be used to refresh credentials versus requiring complete re-issuance flow restart. As specified in `OPENID4VC-HAIP`_
  * - CI_105
    - Issuance, Security
    - Recommended Re-issued Credential Expiration Alignment
    - New Digital Credentials obtained through re-issuance flow maintain the same expiration as the refreshed credential
  * - CI_106
    - Issuance, Security
    - Post-Expiration Issuance Requirement
    - Once a Digital Credential expires, Users complete the entire issuance process again to obtain new Digital Credentials
  * - CI_107
    - Issuance, Security
    - Consistent Issuer Requirement for Re-Issuance
    - New Digital Credentials are issued exclusively by the same Credential Issuers that originally provided the existing credentials to the same Wallet Instance
  * - CI_108
    - Issuance, Security
    - Refresh Token Scope Limitation for Re-issuance
    - Access Tokens obtained through Refresh Token flows are restricted from issuing Digital Credentials not already present in the Wallet Instance (first-time-issuance)
  * - CI_109
    - Issuance, Security
    - Re-issuance Process Scope Limitation
    - The re-issuance process is limited to two specific update types: Data model/format technical updates and User's attribute set updates
  * - CI_110
    - Issuance, Security
    - Not Recommended Technical Update User Interaction
    - For data model/format technical updates, the replacement and storage of Digital Credentials don't require direct user involvement
  * - CI_111
    - Issuance, Security and Privacy
    - Attribute Update User Authorization
    - For User's attribute set updates, the Wallet Instance informs the User about attribute data set changes and requests explicit User authorization before storing the new Digital Credential
  * - CI_112
    - Issuance, Security
    - Expiry Date Consistency for Re-Issuance
    - Newly issued Digital Credentials maintain the same expiry date as the previous credential version
  * - CI_113
    - Issuance, Privacy
    - Optional Out-of-Band Re-Issuance Update Notification
    - When a Digital Credential requires updating, Credential Issuers send notifications to Users through registered out-of-band communication channels (email, SMS, push notifications)
  * - CI_114
    - Issuance, Security
    - First-Time Issuance Restriction for Refresh Tokens
    - Access Tokens obtained through Refresh Token flows are prohibited from being used for first-time issuance of Digital Credentials
  * - CI_115
    - Voided
    - Voided
    - Voided
  * - CI_116
    - Issuance, Privacy
    - User Consent for Attribute-Based Re-issuance
    - For re-issuance processes triggered by attribute changes, User consent is obtained before storing the new Digital Credential
  * - CI_117
    - Data Model and lifecycle, Interoperability
    - Italian PID User attributes
    - The Italian PID is successfully provided with the User attributes defined in the :ref:`PID parameters table <table_sd-jwt-vc_pid_parameters>`.
  * - CI_118
    - Data Model and lifecycle, Issuance, Interoperability
    - (Q)EAA Credential Formats
    - (Q)EAA are Issued to a Wallet Instance in SD-JWT VC or mdoc-CBOR data format.
  * - CI_119
    - Voided
    - Voided
    - Voided
  * - CI_120
    - Data Model and lifecycle, Security
    - Signature of the SD-JWT credential
    - The Credential in SD-JWT format is signed using the Issuer's private key.
  * - CI_121
    - Data Model and lifecycle, Interoperability
    - SD-JWT Type Metadata Provision
    - SD-JWT is successfully provided with complete Type Metadata for the issued Digital Credential, conforming to Sections 6 and 6.3 of `SD-JWT-VC`_ specifications.
  * - CI_122
    - Data Model and lifecycle, Security
    - SD-JWT Payload Structure Validation
    - SD-JWT payload contains the required *_sd_alg* claim and all other mandatory claims as specified, with proper formatting and structure.
  * - CI_123
    - Data Model and lifecycle, Security
    - SD-JWT Hash Algorithm Declaration
    - The *_sd_alg* claim is present and set to a supported algorithm defined in Section Cryptographic Algorithms, indicating the hash algorithm used by the Issuer to generate digests as described in `SD-JWT`_ Section 4.1.1.
  * - CI_124
    - Data Model and lifecycle, Interoperability
    - SD-JWT Selective Disclosure Organization
    - Non-selectively disclosable claims appear directly in the SD-JWT payload as they are, while selectively disclosable claim digests (plus any decoys) are properly organized within *_sd* arrays as described in Section 4.2.4.1.
  * - CI_125
    - Data Model and lifecycle, Interoperability
    - SD-JWT Disclosure Integrity Verification
    - Each digest value successfully validates against its corresponding disclosure, with disclosures containing the required components: random salt, claim name (for object elements), and claim value.
  * - CI_126
    - Data Model and lifecycle, Interoperability
    - Recommendation on SD-JWT Nested Object Selective Disclosure
    - In a nested SD-JWT payload, every claim at each level of the JSON structure is explicitly marked as either selectively disclosable or not. As a consequence, the  ``_sd`` claim containing digests can legitimately appear multiple times at different levels within the SD-JWT.
  * - CI_127
    - Data Model and lifecycle, Interoperability
    - SD-JWT Disclosure digests positioning
    - Array element disclosures are correctly positioned, with digests and decoy digests replacing original claim values in their exact array positions, maintaining structural integrity as specified in Section 4.2.4.2 of `SD-JWT`_.
  * - CI_128
    - Data Model and lifecycle, Security
    - SD-JWT Array Element Digest Calculation
    - Array elements digest values are calculated using a hash function over the disclosures, containing: a random salt and the array element.
  * - CI_129
    - Data Model and lifecycle, Privacy
    - SD-JWT Array Disclosures
    - Array-level selective disclosure operates correctly, allowing Holders to selectively disclose entire arrays or individual entries within arrays, as defined in Section 4.2.6 of `SD-JWT`_.
  * - CI_130
    - Data Model and lifecycle, Interoperability
    - SD-JWT Combined Format Disclosure Delivery
    - The Disclosures are successfully provided to the Holder together with the SD-JWT in the Combined Format for Issuance, formatted as an ordered series of base64url-encoded values with each value properly separated by a single tilde ('~') character.
  * - CI_131
    - Data Model and lifecycle, Interoperability
    - SD-JWT JOSE Header Parameter
    - The JOSE header contains the parameter in the Credential :ref:`SD-JWT Parameters Table <table_sd-jwt-vc_jose_header>`.
  * - CI_132
    - Data Model and lifecycle, Interoperability
    - SD-JWT Payload Claims
    - The JWT payload contains claims in the Credential :ref:`SD-JWT Parameters Table <table_sd-jwt-vc_parameters>`.
  * - CI_133
    - Data Model and lifecycle, Interoperability
    - SD-JWT Status List Parameter Structure
    - When status parameter is set to status_list, it is a JSON Object containing the following sub-parameters: *idx* and *uri*.
  * - CI_134
    - Data Model and lifecycle, Interoperability
    - SD-JWT Optional Credential Type Metadata Retrieval
    - The Credential Type Metadata JSON Document is successfully retrieved directly from the *well-known* endpoint.
  * - CI_134a
    - Data Model and lifecycle, Interoperability
    - SD-JWT Case-Insensitive URI Matching
    - When retrieving Credential Type Metadata via vct, URN string literal matching is performed in a case-sensitive manner, while the system operates without requiring the .well-known endpoint (as specified in Section 6.3.3 of `SD-JWT-VC`_), maintaining compatibility options for implementers who choose to use it for interoperability with other systems.
  * - CI_135
    - Data Model and lifecycle, Interoperability
    - Metadata Document JSON Object Structure
    - The Type Metadata document, if provided, is a JSON object containing the parameters defined in Section 6.2 of `SD-JWT-VC`_.
  * - CI_136
    - Data Model and lifecycle, Interoperability
    - Additional PID Claims
    - Depending on the Digital Credential type specified in vct, additional claims data is successfully incorporated when required
  * - CI_137
    - Data Model and lifecycle, Interoperability
    - Mdoc Credential Format
    - The mdoc data elements are successfully encoded in CBOR format according to :rfc:`8949` specifications, ensuring proper binary serialization and compatibility with ISO/IEC 18013-5 standard.
  * - CI_138
    - Data Model and lifecycle, Interoperability
    - Mdoc Component Structure Organization
    - The mdoc Digital Credential is properly structured into distinct components including namespaces (*nameSpaces*) and cryptographic proof (*issuerAuth*)
  * - CI_139
    - Data Model and lifecycle, Privacy
    - Mdoc Mobile Security Object Integrity Verification
    - The Mobile Security Object (MSO) correctly stores cryptographic digests of attributes within nameSpaces, enabling Relying Parties to validate disclosed attributes against corresponding digestID values while maintaining privacy of undisclosed information. See :ref:`credential-data-model:Mobile Security Object` for details
  * - CI_140
    - Data Model and lifecycle, Interoperability
    - Mdoc-CBOR Structure Compliance
    - The mdoc-CBOR Digital Credential successfully conforms to the required structure as specified in the compliance :ref:`table <table_mdoc_structure>`.
  * - CI_141
    - Data Model and lifecycle, Interoperability
    - Namespace Structure Organization
    - The nameSpaces correctly contains one or more nameSpace entries, each properly identified by a unique name for organized data categorization.
  * - CI_142
    - Data Model and lifecycle, Interoperability
    - Namespaces IssuerSignedItemBytes Encoding
    - Within each nameSpace, one or more IssuerSignedItemBytes are correctly encoded as CBOR byte strings with Tag 24 (#6.24(bstr .cbor)), appearing as 24(\<\<\... \>\>) in diagnostic notation.
  * - CI_143
    - Data Model and lifecycle, Interoperability
    - Namespace Disclosure Information Attributes
    - Each IssuerSignedItemBytes successfully represents the disclosure information for corresponding digests within the *Mobile Security Object* and contain all the attributes as specified in the compliance :ref:`table <table_attribute_namespaces>`.
  * - CI_144
    - Data Model and lifecycle, Interoperability
    - Namespace ElementIdentifier Inclusion
    - All elementIdentifiers in the elementIdentifiers attribute :ref:`table <table_element_identifiers_mdoc>` are properly included in the Digital Credential encoded in mdoc-CBOR within their respective nameSpaces, unless, otherwise specified.
  * - CI_145
    - Data Model and lifecycle, Interoperability
    - Mobile Security Object COSE Structure
    - The issuerAuth successfully represents the Mobile Security Object as a properly formatted COSE Sign1 Document according to :rfc:`9052`, containing the complete required data structure with: protected header, unprotected header, payload and signature components.
  * - CI_146
    - Data Model and lifecycle, Interoperability
    - Mobile Security Object Protected Header Parameter Encoding
    - The protected header successfully contains the parameters properly encoded in CBOR format according to the corresponding :ref:`table <table_protected_headers_mdoc>`.
  * - CI_147
    - Data Model and lifecycle, Interoperability
    - Mobile Security Object Protected Header Algorithm
    - The protected header successfully contains the required signature algorithm parameter.
  * - CI_147a
    - Data Model and lifecycle, Interoperability
    - Not Recommended elements in the Mobile Security Object Protected Header
    - The protected header does not contain elements different from the signature algorithm
  * - CI_148
    - Data Model and lifecycle, Interoperability
    - Mobile Security Object Unprotected Header Parameter Encoding
    - Unless otherwise specified, the unprotected header contain the parameters according to the corresponding :ref:`table <table_unprotected_headers_mdoc>`.
  * - CI_148a
    - Data Model and lifecycle, Interoperability
    - Mobile Security Object x5chain inclusion
    - The *x5chain* is correctly included in the unprotected header
  * - CI_149
    - Data Model and lifecycle, Interoperability
    - Mobile Security Object Payload Structure
    - The payload successfully contains the MobileSecurityObject properly encoded as a byte string (bstr) using CBOR Tag 24, with the content-type COSE Sign header parameter correctly excluded from the structure.
  * - CI_150
    - Data Model and lifecycle, Interoperability
    - Mobile Security Object Attributes Compliance
    - The MobileSecurityObject successfully contains all required attributes as specified in the compliance :ref:`table <table_MobileSecurityObject_attributes>`, with proper formatting and values unless explicitly exempted by specification requirements.
  * - CI_151
    - Issuance, Interoperability
    - Wallet Instance State verification
    - Credential Issuer successfully verifies that Wallet Instance is in Operational or Valid state and proceeds with Digital Credential issuance.
  * - CI_152
    - Data Model and lifecycle, Interoperability
    - Credential State Management for Activation
    - A Digital Credential successfully transitions to Valid state when start date of validity is reached, or when unsuspension process is completed for a previously suspended (Q)EAA.
  * - CI_153
    - Data Model and lifecycle, Interoperability
    - Automatic Credential Expiration Management
    - A Digital Credential successfully transitions to the Expired state when it automatically expires upon reaching its end date of validity (PID/(Q)EAA EXP),
  * - CI_154
    - Data Model and lifecycle, Interoperability
    - Credential Revocation Process Management
    - A Digital Credential successfully changes from Issued, Valid or Suspended states to Revoked state when it is actively revoked by the Credential Issuer by a revocation process (PID/(Q)EAA REV).
  * - CI_155
    - Data Model and lifecycle, Interoperability
    - Digital Credential Revocation Use Cases
    - Digital Credential Revocation is correctly implemented for every use case
  * - CI_155a
    - Data Model and lifecycle, Interoperability
    - Digital Credential Revocation - Technical Security Compromise
    - Digital Credential is successfully revoked when cryptographic material compromise is detected, with immediate invalidation and status update in revocation registries.
  * - CI_155b
    - Data Model and lifecycle, Interoperability
    - Digital Credential Revocation - User Request
    - Digital Credential is successfully revoked upon explicit User request
  * - CI_155c
    - Data Model and lifecycle, Interoperability
    - Digital Credential Revocation - Attribute Updates
    - Digital Credential is automatically revoked when Authentic Sources notify attribute changes that invalidate the Credential, triggering re-issuance process if applicable.
  * - CI_155d
    - Data Model and lifecycle, Interoperability
    - Digital Credential Revocation - Source-Initiated Revocation
    - Digital Credential is immediately revoked when Authentic Source notifies revocation of underlying attributes
  * - CI_155e
    - Data Model and lifecycle, Interoperability
    - Digital Credential Revocation - Wallet Instance Revocation
    - All Digital Credentials are revoked when the containing Wallet Instance is revoked
  * - CI_155f
    - Data Model and lifecycle, Interoperability
    - Digital Credential Revocation - Judicial/Supervisory Order
    - Digital Credential is immediately revoked when illegal activities are reported by Judicial or Supervisory Bodies
  * - CI_155g
    - Data Model and lifecycle, Interoperability
    - PID Revocation - Identity Provider Breach
    - PID is revoked when breach detection occurs in the Identity Provider used for User authentication during PID issuance
  * - CI_156
    - Data Model and lifecycle, Interoperability
    - Optional (Q)EAA Revocation Following PID Revocation
    - (Q)EAA Provider successfully evaluates PID revocation status and revoke associated (Q)EAA credentials
  * - CI_157
    - Data Model and lifecycle, Interoperability
    - (Q)EAA State Change to Suspended
    - (Q)EAA successfully transitions from Issued or Valid state to Suspended state when it is suspended by the Credential Issuer ((Q)EAA SUSP)
  * - CI_158
    - Data Model and lifecycle, Interoperability
    - (Q)EAA Suspension Duration and State Recovery
    - Suspended (Q)EAA remains in Suspended state until suspension conditions are resolved and credential is restored to previous state Issued or Valid, or transitions to Revoked, Expired, or deleted
  * - CI_158a
    - Data Model and lifecycle, Interoperability
    - (Q)EAA Suspension - Attribute Validity Changes
    - The suspension of a (Q)EAA is based on the validity status of its contained attributes
  * - CI_158b
    - Data Model and lifecycle, Interoperability
    - (Q)EAA Suspension - User Request
    - (Q)EAA successfully transitions to Suspended state upon explicit User request.
  * - CI_159
    - Data Model and lifecycle, Interoperability
    - Batch-Issued Digital Credentials Individual Lifecycle Management
    - Each Digital Credential from a batch issuance successfully enters its own independent lifecycle state machine. All state transitions (Issued → Valid → Expired/Suspended/Revoked) still occur on a per Credential basis, using Credential's individual parameters
  * - CI_160
    - Data Model and lifecycle, Interoperability
    - Digital Credential Generation and Storage
    - Credential Issuer successfully generates Digital Credential following issuance request completion and stores it in local storage immediately after successful issuance.
  * - CI_160a
    - Data Model and lifecycle, Interoperability
    - Digital Credential State Management
    - Credential Issuer successfully updates Digital Credential state locally for revocation, suspension, or unsuspension events triggered by technical security reasons, User requests, or by external entities (e.g., Users and Authentic Sources)
  * - CI_160b
    - Data Model and lifecycle, Interoperability
    - Digital Credential Data Purging
    - Credential Issuer successfully removes Digital Credentials from local storage after reaching the Expired state or based on Credential Issuer retention policies.
  * - CI_161
    - Data Model and lifecycle, Interoperability
    - Credential Issuer Direct Validity Status Management
    - Credential Issuer directly manages the validity status of issued Digital Credentials and correctly manages the triggering of the Digital Credential revocation or suspension process by other actors.
  * - CI_161a
    - Data Model and lifecycle, Interoperability
    - User-Initiated Revocation via Issuer Web Service
    - User successfully initiates Digital Credential revocation/suspension through Credential Issuer's web service, with authentication verification and revocation request processing.
  * - CI_161b
    - Data Model and lifecycle, Interoperability
    - Authentic Source-Triggered Revocation
    - Authentic Source successfully triggers Digital Credential revocation/suspension process when Credential attributes are updated or change validity status.
  * - CI_162
    - Data Model and lifecycle, Security
    - User Access to Issuer Web Portal with LoA Authentication
    - Credential Issuer ensures that users can successfully access the secure area of its web portal. This access requires authentication with a Level of Assurance that is at least equal to the Level of Assurance used during the initial credential issuance.
  * - CI_162a
    - Data Model and lifecycle, Interoperability
    - User Access to Digital Credentials Database View
    - Credential Issuer successfully provides Users with complete view of all their Digital Credentials contained in the Issuer's database through the web portal
  * - CI_162b
    - Data Model and lifecycle, Interoperability
    - User Data Authenticity Verification via Web Portal
    - Credential Issuer successfully enables Users to verify data authenticity of their Digital Credentials through the web portal
  * - CI_162c
    - Data Model and lifecycle, Interoperability
    - User Validity Status Management via Web Portal
    - Credential Issuer successfully allows Users to view and update validity status of their Digital Credentials through the web portal (revoke their Digital Credentials and, if it is supported by the Issuer, suspend them).
  * - CI_163
    - Data Model and lifecycle, Interoperability
    - PID Revocation and Wallet Instance Status Update on New PID Issuance
    - When User activates another Wallet Instance from the same Wallet Provider using the same Wallet Solution and obtains a new PID, the previous PID is successfully revoked and the previous Wallet Instance successfully transitions to operational status, ensuring single active PID per User per Wallet Provider.
  * - CI_164
    - Data Model and lifecycle, Interoperability
    - PID Revocation Following User Death and ANPR Status Change
    - User's death successfully triggers change in validity status of User's identification attributes in the public registry (ANPR), which automatically produces PID revocation.
  * - CI_165
    - Data Model and lifecycle, Interoperability
    - PID Revocation Notification Requirement
    - Credential Issuer successfully sends notification of PID revocation event to the User within 24 hours of revocation occurrence
  * - CI_166
    - Data Model and lifecycle, Interoperability
    - Recommended Non-PID Credential Revocation Notification
    - Credential Issuer sends notification of revocation event to the User for any Digital Credential other than PID
  * - CI_167
    - Data Model and lifecycle, Interoperability
    - Multi-Channel Revocation Notification Delivery
    - Credential Issuer successfully delivers revocation notifications through verified and secure communication channels (email, telephone, or other authenticated channels), including complete information about the Credential revocation status and reason.
  * - CI_168
    - Data Model and lifecycle, Interoperability
    - Digital Credential Status Update on Revocation
    - Credential Issuer successfully updates Digital Credential status immediately when revocation occurs
  * - CI_169
    - Data Model and lifecycle, Interoperability
    - Wallet Instance Status Monitoring for the Digital Credential Status Update
    - Credential Issuer establishes a monitoring mechanism of the current statuses of all the Key Attestations related to the Wallet Instances to which the Credentials were issued.
  * - CI_170
    - Data Model and lifecycle, Interoperability
    - Credential Status Update Following Data Change Notification
    - Credential Issuer successfully updates Credential Status according to the validity mechanism's defined mode upon receiving notification from Authentic Source
  * - CI_170a
    - Data Model and lifecycle, Interoperability
    - User Notification of Credential Update
    - Credential Issuer successfully notifies User of credential changes through registered out-of-band communication channel
  * - CI_171
    - Data Model and lifecycle, Interoperability
    - User Notification on Credential Status INVALID
    - Credential Issuer successfully informs User when Credential Status changes to INVALID
  * - CI_172
    - Data Model and lifecycle, Interoperability
    - Batch Status Update Processing as Individual Changes
    - Credential Issuer successfully handles single batch status update request (referencing batch notification_id) from authorized entities (e.g. Wallet Instance via Notification Endpoint with event=credential_deleted, or Wallet Provider via PDND) as N separate individual status changes, with each Credential's status updated independently (for example, flipping its status-list bit to INVALID or SUSPENDED).
  * - CI_173
    - Data Model and lifecycle, Interoperability
    - Batch revocation upon credential Update Request
    - Credential Issuer successfully processes batch update request as revoke all requests, marking every Credential in the batch as revoked and emitting single notification covering the entire batch.
  * - CI_174
    - Data Model and lifecycle, Interoperability
    - Batch Credential Deletion
    - User-driven deletion successfully removes the entire batch as Wallet UI surfaces a batch as one Credential, with deletion request using the batch's notification_id applying to all Credentials in that batch, as it is not possible to delete or revoke just one Credential.
  * - CI_175
    - Data Model and lifecycle, Interoperability
    - OAuth Status List Support for Long-Lived Digital Credentials
    - OAuth Status List (`TOKEN-STATUS-LIST`_) is successfully supported for verification of validity status of long-lived Digital Credentials in both remote and proximity scenarios.
  * - CI_176
    - Data Model and lifecycle, Interoperability
    - Digital Credential Index Allocation and Status Mapping
    - Each Digital Credential is successfully allocated an index during issuance that represents its position within the bit array, with the value of the bit(s) at this index corresponding to the Digital Credential's status.
  * - CI_177
    - Data Model and lifecycle, Interoperability
    - Status List Token Cryptographic Format
    - Status List is successfully provided within a cryptographically signed Status List Token in JWT or CWT format.
  * - CI_178
    - Data Model and lifecycle, Interoperability
    - Status List Bit Configuration for Digital Credentials
    - Credential Issuer successfully sets the ``bits`` parameter to ``4``; each Digital Credential is represented by 4 bits, allowing 16 status values.
  * - CI_179
    - Data Model and lifecycle, Interoperability
    - Status List Byte Array Creation and Credential Position Assignment
    - Credential Issuer successfully creates a byte array of size = (number of Digital Credentials) * 4 / 8 or greater, with each byte corresponding to two 4-bit status values, and assigns each issued Digital Credential to a position in the array.
  * - CI_180
    - Data Model and lifecycle, Interoperability
    - Status List Digital Credential Status Values Setting in Byte Array
    - Credential Issuer successfully sets status values for all issued Digital Credentials within the byte array, with each status identified by an index that maps to four bits within the byte array, indices counting from 0 to (number of Digital Credentials) - 1, bits counted from least significant bit ("0") to most significant bit ("7"), and each four-bit value set to the corresponding status.
  * - CI_181
    - Data Model and lifecycle, Interoperability
    - Status List Digital Credential Byte Array Compression
    - Credential Issuer successfully compresses the byte array using DEFLATE [:rfc:`1951`] with the ZLIB [:rfc:`1950`] data format
  * - CI_181a
    - Data Model and lifecycle, Interoperability
    - Status List Digital Credential Recommended Compression Level
    - Implementations successfully use the highest compression level available for byte array compression.
  * - CI_182
    - Data Model and lifecycle, Interoperability
    - Status List Endpoint Availability
    - Credential Issuer successfully makes available to Relying Parties and Wallet Instances an endpoint to request Status Lists.
  * - CI_183
    - Data Model and lifecycle, Interoperability
    - Status List Digital Credential Status Values Definition
    - Credential Issuer successfully uses the status values defined in the :ref:`credential-revocation:Token Status List (Digital Credentials Profile)`.
  * - CI_184
    - Data Model and lifecycle, Interoperability
    - Status List Optional Digital Credential Status States Definition
    - Credential Issuer successfully defines additional application-specific statuses within the range supported by ``bits``, with careful consideration for the information disclosed to Relying Parties about the Digital Credential lifecycle.
  * - CI_185
    - Data Model and lifecycle, Interoperability
    - Status List Token Parameters at Endpoint
    - The Status List Token is successfully available at the Status List Endpoint and conforms to `TOKEN-STATUS-LIST`_ and the profiles specified in :ref:`credential-revocation:Token Status List (Digital Credentials Profile)`.
  * - CI_186
    - Data Model and lifecycle, Interoperability
    - Recommended Status List Token Short-Lived Expiration Setting
    - Credential Issuer successfully sets exp claim so that Status List Token is short-lived, typically with exp claim not exceeding iat claim by more than 24 hours.
  * - CI_187
    - Data Model and lifecycle, Interoperability
    - JSON-Encoded Status List Structure
    - The structure of the JSON-encoded Status List correctly conforms to `TOKEN-STATUS-LIST`_ and the profiles specified in :ref:`credential-revocation:Token Status List (Digital Credentials Profile)`.
  * - CI_188
    - Data Model and lifecycle, Interoperability
    - Status List Digital Credential Local Storage
    - Credential Issuers successfully store generated Digital Credential locally with minimum set of data required to manage its lifecycle, including the validity status of that Digital Credential.
  * - CI_189
    - Data Model and lifecycle, Interoperability
    - Digital Credential Status List Claim Inclusion
    - Credential Issuers successfully include *status_list* claim within the JSON Object value of the status claim of the Digital Credential once generated.
  * - CI_190
    - Data Model and lifecycle, Interoperability
    - Status List Claim JSON Object Parameters
    - The value of the *status_list* claim is a JSON object with the parameters defined in `TOKEN-STATUS-LIST`_ and the profiles specified in :ref:`credential-revocation:Token Status List (Digital Credentials Profile)`.
  * - CI_191
    - Data Model and lifecycle, Interoperability
    - Status List Endpoint Successful Response
    - Status List Endpoint successfully responds with a Status List Token using an HTTP status code in the 2xx range, with the Status Provider using ``application/statuslist+jwt`` for a JWT Status List Token or ``application/statuslist+cwt`` for a CWT Status List Token.
  * - CI_192
    - Data Model and lifecycle, Interoperability
    - HTTP Status List Response Gzip Content-Encoding
    - HTTP response successfully uses gzip Content-Encoding as defined in [:rfc:`9110`].
  * - CI_193
    - Data Model and lifecycle, Interoperability
    - Digital Credential Issuer Authorization and Registration
    - Credential Issuer successfully registers its own Digital Credentials in the catalogue.
  * - CI_194
    - Data Model and lifecycle, Interoperability
    - Digital Credential Catalogue Required Information
    - Credential Issuer provides its credentials in the catalogue, along with the information in the corresponding :ref:`table <table_catalog_parameters>`.
  * - CI_195
    - Data Model and lifecycle, Interoperability
    - Credentials Array Element Information
    - Each element of the *Credentials* array correctly contains all the information defined in the First-level Fields :ref:`table <table_catalog_parameters_first_level>`.
