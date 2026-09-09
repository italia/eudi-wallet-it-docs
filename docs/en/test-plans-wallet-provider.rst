.. include:: ../common/common_definitions.rst
.. Included via test-plans.rst at title level '-' (level 1).

Wallet Provider Test Matrix
---------------------------

This section provides the set of test cases for verifying conformance of a Wallet Solution and Wallet Instance implementation to the technical rules defined in the IT-Wallet ecosystem.
The test plan is based on the requirements extracted from the following Sections:

- :ref:`infrastructure-trust:Infrastructure of Trust`
- :ref:`wallet-solution:Wallet Solution`
- :ref:`credential-issuance:Digital Credential Issuance`
- :ref:`credential-presentation:Digital Credential Presentation`
- :ref:`endpoints:Endpoints`
- :ref:`mobile-application-instance:Mobile Application Instance`


.. note::
   The test cases in this list vary in scope. Some are intentionally written at a high level to confirm the success of complete user flows and the conformance of core architectural and interoperability principles, while others are atomic, targeting single, detailed requirements and verifying specific functional behavior.

.. _wallet-provider-backend-testcases:

Test Cases for Wallet Provider Backend
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This section lists the test cases from Sections:

- :ref:`wallet-solution-requirements:Wallet Solution Requirements`
- :ref:`wallet-solution-components:Wallet Solution Components`
- :ref:`wallet-instance:Wallet Instance`
- :ref:`wallet-provider-entity-configuration:Wallet Provider Entity Configuration`
- :ref:`wallet-solution-metadata:Wallet Solution Metadata`
- `e-Service PDND Wallet Provider Catalogue <wallet-provider-endpoint.html#e-service-pdnd-wallet-provider-catalogue0>`_


.. list-table::
   :class: longtable
   :widths: 15 15 20 55
   :header-rows: 1

   * - **Test Case ID**
     - **Purpose**
     - **Description**
     - **Expected Result**
   * - WP_001
     - Trust, Security
     - Entity Configuration publication
     - An HTTP GET request to the ``.well-known/openid-federation`` endpoint retrieves the Wallet Provider Entity Configuration.
   * - WP_002
     - Trust, Security
     - Entity Configuration cryptography
     - The Wallet Provider Entity Configuration is a signed JWT that conforms to `OID-FED`_.
   * - WP_002a
     - Trust, Interoperability
     - Entity Configuration JWT ``alg`` header parameter
     - The Entity Configuration JWT header contains an ``alg`` set to a permitted signature algorithm (e.g., ``ES256``) and not ``none``.
   * - WP_002b
     - Trust, Interoperability
     - Entity Configuration JWT key identifier header parameter
     - The Entity Configuration JWT header contains a ``kid`` equal to the thumbprint of the public key used to sign the Entity Configuration.
   * - WP_002c
     - Trust, Interoperability
     - Entity Configuration JWT type header parameter
     - The Entity Configuration JWT header contains ``typ`` set to ``entity-statement+jwt``.
   * - WP_002d
     - Trust, Interoperability
     - Entity Configuration issuer and subject payload claims
     - The Entity Configuration JWT payload contains ``iss`` and ``sub``, both set to the public URL of the Wallet Provider.
   * - WP_002e
     - Trust, Interoperability
     - Entity Configuration validity
     - The Entity Configuration JWT payload contains ``iat`` and ``exp`` as valid Unix timestamps.
   * - WP_002f
     - Trust, Interoperability
     - Entity Configuration authority hints
     - The Entity Configuration JWT payload contains ``authority_hints`` as an array of valid URLs of immediate superior entities.
   * - WP_002g
     - Trust, Interoperability
     - Entity Configuration signing keys
     - The Entity Configuration JWT payload contains ``jwks`` with a valid JWKS of the Wallet Provider’s Federation Entity public signing keys.
   * - WP_002h
     - Trust, Interoperability
     - Entity Configuration metadata
     - The Entity Configuration JWT payload contains a ``metadata`` object that includes ``wallet_solution`` metadata and optionally ``federation_entity``, each following its schema.
   * - WP_003
     - Trust, Interoperability
     - Metadata key usage
     - The public keys in the metadata JSON Object are designated exclusively for signing and/or encryption when the entity acts as a Wallet Provider (e.g., for Wallet Attestations).
   * - WP_004
     - Trust, Interoperability
     - Metadata key reference
     - To reference public keys, the metadata JSON Object contains exactly one of the following claims: ``jwks``, ``jwks_uri``, or ``signed_jwks_uri``.
   * - WP_004a
     - Trust, Interoperability
     - JWKS by value
     - If ``jwks`` is present, it contains a valid JWKS document passed by value.
   * - WP_004b
     - Trust, Interoperability
     - JWKS by reference
     - If ``jwks_uri`` is present, the value is an HTTPS URL to a JWKS that resolves and validates.
   * - WP_004c
     - Trust, Interoperability
     - Signed JWKS URI
     - If ``signed_jwks_uri`` is present, the value is an HTTPS URL to a JWT whose payload is a JWKS and is signed with a Federation Entity Key.
       The ``signed_jwks_uri`` resource is served with content type ``application/jwk-set+jwt``. A successful ``signed_jwks_uri`` retrieval returns ``HTTP 200``.
   * - WP_005
     - Trust, UX
     - Portal 2FA enforcement
     - The Wallet Provider portal correctly enforces two-factor authentication (``2FA``) before allowing Users to perform any operation.
   * - WP_006
     - Wallet Revocation, Security
     - Portal Wallet Instances status view
     - The Wallet Provider portal correctly allows Users to view the current status of all Wallet Instances linked to their account.
   * - WP_007
     - Wallet Revocation, Security
     - User-initiated revocation trigger
     - Wallet Provider implements and supports revocation requests initiated by Users via its portal.
   * - WP_007a
     - Wallet Revocation, Security
     - Portal instance revocation
     - The Wallet Provider portal correctly allows Users to revoke a specific Wallet Instance or all Wallet Instances.
   * - WP_008
     - Wallet Revocation, Security
     - PID Provider-initiated revocation trigger
     - Wallet Provider implements and supports revocation requests triggered by PID Providers via the PDND Endpoint.
   * - WP_009
     - Wallet Revocation, Security
     - Legal Authorities-initiated revocation trigger
     - Wallet Provider implements and supports revocation requests triggered by Legal Authorities or Supervisory Bodies (e.g., illegal activities).
   * - WP_010
     - Trust, Interoperability
     - Wallet Instance revocation mechanism
     - When Wallet Provider triggers the revocation for a specific Wallet Instance at any time, that instance is terminated and can no longer perform any functions.
   * - WP_011
     - Trust, Security
     - Wallet Instance integrity verification
     - Wallet Provider periodically evaluates Wallet Instance's integrity, authenticity, and genuineness using the Play Integrity API (Android) or App Attest (iOS).
   * - WP_012
     - Lifecycle, Interoperability
     - Backend component architecture
     - The Wallet Provider Backend supports all the components (Frontend, API Interface, Wallet Instance Lifecycle Management, and Trust & Security) as shown in :ref:`Figure of Wallet Solution High Level Architecture <fig_wallet-solution-high-level-architecture>`.

.. _wallet-instance-testcases:

Test Cases for Wallet Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This section lists the test cases from Sections:

- `Configuration of the Federation <trust.html#configuration-of-the-federation>`_
- `Trust Evaluation Mechanism <trust.html#trust-evaluation-mechanism>`_
- :ref:`wallet-solution-requirements:Wallet Solution Requirements`
- :ref:`wallet-solution-components:Wallet Solution Components`
- :ref:`wallet-instance:Wallet Instance`
- `Error Handling for Wallet Instance Management <wallet-provider-endpoint.html#error-handling-for-wallet-instance-management>`__
- `Mobile Application Instance Initialization <mobile-application-instance.html#mobile-application-instance-initialization>`_


.. list-table::
   :class: longtable
   :widths: 15 15 20 55
   :header-rows: 1

   * - **Test Case ID**
     - **Purpose**
     - **Description**
     - **Expected Result**
   * - WP_013
     - Lifecycle, Interoperability
     - Frontend component architecture
     - Wallet Instance supports all the components (User Interface, Lifecycle Management, Issuer, Presentation, Backup/Restore, Keystore, and WSCA/WSCD Interface for PID) as shown in :ref:`Figure of Wallet Solution High Level Architecture <fig_wallet-solution-high-level-architecture>`.
   * - WP_014
     - Trust, Security
     - Keystore implementation
     - Wallet Instance uses the hardware-backed Keystore (Strongbox or TEE on Android; Secure Enclave on iOS) for all required cryptographic operations, such as generating signatures and performing key management. For PID issuance and management, the Wallet Instance interacts with the WSCA operating within the Remote WSCD (remote HSM) to conform with Level of Assurance High requirements.
   * - WP_015
     - Lifecycle, UX
     - Android/iOS compatibility
     - Wallet Instance installs and operates with full functionality on both Android and iOS devices and is available on the Play Store and App Store.
   * - WP_016
     - Trust, Issuance, Interoperability
     - Retrieve and maintain Trust Anchor metadata
     - Wallet Instance fetches and refreshes the Trust Anchor’s Entity Configuration before use and keeps it up-to-date.
   * - WP_017
     - Trust, Issuance, Interoperability
     - Validate Trust Anchor authenticity
     - Wallet Instance compares out-of-band public keys to those in the Trust Anchor’s Entity Configuration and discards non-matching keys, logs discrepancies, and uses only matches.
   * - WP_018
     - Lifecycle, Trust, Security
     - Periodic trust reestablishment
     - Wallet Instance periodically and successfully obtains a fresh Wallet Attestation from its Wallet Provider.
   * - WP_019
     - Trust, Security
     - Wallet Attestation content
     - The Wallet Attestation contains all required claims and data points that attest to the device's integrity and security status.
   * - WP_019a
     - Trust, Security
     - No attestation for unverified Wallet Instances
     - Wallet Provider rejects an attestation request from a Wallet Instance that fails authenticity, integrity, or genuineness checks.
   * - WP_019b
     - Trust, Security
     - Attestation-ephemeral key binding
     - The Wallet Attestation contains a cryptographic binding to Wallet Instance’s ephemeral public key that is successfully verified.
   * - WP_020
     - Trust, Security
     - Wallet Attestation signing
     - The Wallet Attestation is signed by its authorized Wallet Provider, as officially listed by the overseeing Registration Authority.
   * - WP_021
     - Wallet Initialization / Registration, Lifecycle, Security
     - Device security verification
     - Wallet Instance prevents activation on a device that does not meet the Wallet Provider's defined minimum security requirements.
   * - WP_022
     - Wallet Initialization / Registration, Lifecycle, Security
     - Key Attestation API availability
     - Wallet Instance checks and confirms the availability of the platform's Key Attestation APIs (StrongBox/TEE or Secure Enclave/DeviceCheck).
   * - WP_023
     - Wallet Initialization / Registration, Wallet Attestation Issuance, Lifecycle, Trust
     - Wallet Provider federation discovery
     - Wallet Instance successfully uses Federation API endpoints (``.well-known/openid-federation``, ``/fetch``) to retrieve current metadata and configurations of the Wallet Provider.
   * - WP_024
     - Wallet Initialization / Activation, Lifecycle, Security
     - User consent
     - During the Wallet initialization, Wallet Provider explicitly obtains the User’s consent before creating a User account.
   * - WP_025
     - Wallet Activation, Lifecycle, UX
     - Wallet unlock method setup
     - Wallet Instance prompts the User to set their preferred unlock method (PIN or biometric), and then successfully configures the chosen method.
   * - WP_026
     - Wallet Attestation Issuance, Lifecycle, Security
     - Ephemeral key pair for attestation
     - To perform a Wallet Attestation request, Wallet Instance successfully generates a new ephemeral asymmetric key pair.
   * - WP_027
     - Wallet Attestation Issuance, Lifecycle, Security
     - Device security flaw verification
     - Wallet Provider verifies the device meets its minimum security requirements and is free of known security flaws;  if not, the Wallet Attestation Request is rejected.
   * - WP_028
     - Wallet Attestation Issuance, Lifecycle, Security
     - Time-limited Wallet Attestation
     - When no revocation check methods are supported, the Wallet Provider issues a Wallet Attestation with a defined expiration time and a short validity period.
   * - WP_029
     - Wallet Attestation Issuance, Data Model and Lifecycle, Interoperability
     - HTTP 200 / JSON response envelope
     - Upon successful validation of the Wallet Attestation Issuance Request, the Wallet Provider returns 200 OK with Content-Type: application/json, containing the Wallet Attestation as its structure defined in `Wallet Attestation JWT <wallet-provider-endpoint.html#wallet-attestation-jwt>`_.
   * - WP_029a
     - Wallet Attestation Issuance, Data Model and Lifecycle, Security
     - Wallet Attestation format
     - Wallet Provider provides the Wallet Attestation in JWT format signed by the Wallet Provider, and confirming the structures defined in `Wallet Attestation JWT <wallet-provider-endpoint.html#wallet-attestation-jwt>`_.
   * - WP_029b
     - Wallet Attestation Issuance, Data Model and Lifecycle, Security
     - No PII in Wallet Attestation
     - The Wallet Attestation payload contains no personally identifiable information (PII) about the User.
   * - WP_030
     - Wallet Attestation Issuance, Lifecycle, Security
     - Wallet Attestation integrity verification
     - Wallet Instance verifies the signature of the received Wallet Attestation.
   * - WP_031
     - Wallet Attestation Issuance, Trust, Security
     - Wallet Attestation trust verification
     - Wallet Instance verifies and confirms that the Wallet Attestation issuer (i.e., Wallet Provider) is a trusted member of the Federation, before accepting the Wallet Attestation.
   * - WP_032
     - Wallet Revocation, Lifecycle, Security
     - User-initiated revocation
     - The User successfully initiates a revocation either through the Wallet Instance built-in revocation function or via an external user agent.
   * - WP_032a
     - Wallet Revocation, Lifecycle, Interoperability
     - User login to portal with 2FA
     - To perform a Wallet Instance revocation, the User successfully logs into the Wallet Provider web portal with ``2FA``.
   * - WP_032b
     - Wallet Revocation, Lifecycle, UX
     - User selection of a Wallet Instance to revoke
     - The User views the status of all their linked Wallet Instances, and chooses one to be revoked.
   * - WP_033
     - Wallet Revocation, Lifecycle, Interoperability
     - Wallet Instance Revocation Request
     - Wallet Instance requests revocation of a specified instance by sending a Wallet Instance Revocation Request to the Wallet Instance Management Endpoint.
   * - WP_034
     - Wallet Revocation, Lifecycle, Security
     - Timely revocation alerts
     - Wallet Provider informs the User within 24 hours of a Wallet Instance revocation.
   * - WP_034a
     - Wallet Revocation, Lifecycle, Security
     - Out-of-band revocation alerts
     - Wallet Provider notifies the User of a Wallet Instance revocation through an out-of-band channel (e.g., email or SMS).
   * - WP_034b
     - Wallet Revocation, Lifecycle, Security
     - Clear revocation notification with re-activation guidance
     - The revocation notification clearly explains the reason for revocation and provides actionable steps for re-activation, if applicable.
   * - WP_035
     - Lifecycle, Security
     - Error handling for Wallet Instance management
     - When any error occurs during Wallet Instance Registration/Initialization flow, or during Status Retrieval and Revocation requests, Wallet Provider returns an error response to Wallet Instance that conforms to the standards defined in :rfc:`7231` (for HTTP status code) and  :rfc:`7807` (for problem details).
   * - WP_035a
     - Lifecycle, Interoperability
     - Standard error response format
     - The error response returned by the Wallet Provider includes a ``Content-Type`` header of ``application/json`` and a JSON body containing the mandatory ``error`` and ``error_description`` parameters.
   * - WP_036
     - Lifecycle, Interoperability
     - Handling malformed requests (400)
     - When a request is malformed or missing required parameters, Wallet Provider returns a response with the HTTP status code (``400 Bad Request``) and with the error code ``bad_request``.
   * - WP_037
     - Lifecycle, Interoperability
     - Semantic validation error (422)
     - When a request is well-formed but fails semantic validation, Wallet Provider returns an optional response with the HTTP status code  (``422 Unprocessable Content``) and with the error code ``validation_error``.
   * - WP_038
     - Lifecycle, Interoperability
     - Internal server error (500)
     - In the event of an unhandled internal failure, Wallet Provider returns a response with the HTTP status code (``500 Internal Server Error``) and with the error code ``server_error``.
   * - WP_039
     - Lifecycle, Interoperability
     - Service unavailable (503)
     - When the service is temporarily offline or unable to handle requests, Wallet Provider returns a response with the HTTP status code (``503 Service Unavailable``) and with the error code ``temporarily_unavailable``.
   * - WP_040
     - Wallet Initialization / Registration, Lifecycle, Interoperability
     - Initialization failure (device integrity)
     - When a Wallet Instance Initialization request comes from a device that does not meet the provider's security requirements, the provider returns a ``403 Forbidden`` response with the error code ``integrity_check_error``.
   * - WP_041
     - Wallet Revocation, Lifecycle, Interoperability
     - Unauthorized retrieval request (401)
     - When a Wallet Instance status retrieval request is made without valid authentication credentials, Wallet Provider returns a response with the HTTP status code (``401 Unauthorized``) and with the error code ``unauthorized``.
   * - WP_042
     - Wallet Revocation, Lifecycle, Interoperability
     - Forbidden retrieval request (403)
     - When a User attempts to retrieve a Wallet Instance status they do not have permission for, Wallet Provider returns a response with the HTTP status code (``403 Forbidden``) and with the error code ``forbidden``.
   * - WP_043
     - Wallet Revocation, Lifecycle, Interoperability
     - Unauthorized revocation request (401)
     - When a Wallet Instance Revocation request is made without valid authentication credentials, Wallet Provider returns a response with the HTTP status code (``401 Unauthorized``) with the error code ``unauthorized``.
   * - WP_044
     - Wallet Revocation, Lifecycle, Interoperability
     - Forbidden revocation request (403)
     - When a User attempts to revoke a Wallet Instance they do not have permission for, Wallet Provider returns a response with the HTTP status code (``403 Forbidden``) and with the error code ``invalid_request``.


.. _wallet-credential-issuance-testcases:

Test Cases for Issuance Phase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This section lists the test cases from Sections:

- :ref:`credential-issuance:Digital Credential Issuance`
- `Trust Evaluation Mechanism <trust.html#trust-evaluation-mechanism>`_
- :ref:`credential-issuer-endpoint:Credential Issuer Endpoints`


.. list-table::
   :class: longtable
   :widths: 15 15 20 55
   :header-rows: 1

   * - **Test Case ID**
     - **Purpose**
     - **Description**
     - **Expected Result**
   * - WP_045
     - Issuance, Interoperability
     - Credential Issuer Discovery
     - Wallet Instance successfully discovers trusted Digital Credential Issuers using the Credential Catalogue.
   * - WP_045a
     - Trust, Issuance, Interoperability
     - Fetch the Digital Credential catalogue
     - Wallet Instance successfully sends an HTTP GET request to the Digital Credentials Catalogue Endpoint, using either the ``application/jwt`` (signed) or the ``application/json`` (plain) media type.
   * - WP_046
     - Issuance, Interoperability
     - Discover Credential Issuer dynamically from federation metadata
     - Wallet Instance successfully uses Federation API endpoints (``.well-known/openid-federation``, ``/fetch``) to retrieve current metadata and configurations of the Credential Issuer.
   * - WP_046a
     - Trust, Issuance, Security
     - Validate Credential Issuer’s full Trust Chain to the Trust Anchor
     - Wallet Instance builds and verifies the full Trust Chain from the Credential Issuer through Intermediaries to the root Trust Anchor, ensuring each signature is valid and confirms the root.
   * - WP_047
     - Issuance, Interoperability
     - Third-Party-Initiated flow: Credential Offer QR scan & decode
     - In a Third-Party-Initiated cross-device flow, Wallet Instance successfully scans the QR code, and retrieves the ``credential_offer`` or the ``credential_offer_uri`` parameter.
   * - WP_048
     - Issuance, Interoperability
     - Third-Party-Initiated flow: Credential Offer parsing
     - In a Third-Party-Initiated flow, Wallet Instance extracts and validates all required parameters present in the Credential Offer.
   * - WP_049
     - Issuance, Interoperability
     - Issuer-Initiated flow: Authorization Server identifier check
     - Wallet Instance reads the Credential Issuer’s metadata ``authorization_servers`` and finds the configured Authorization Server identifier in ``authorization_servers``.
   * - WP_050
     - Issuance, Interoperability
     - Issuer-Initiated flow: Digital Credential IDs validation
     - Wallet Instance verifies whether each Digital Credential identifier in the ``credential_configuration_ids`` is supported by the Credential Issuer; any unsupported causes rejection.
   * - WP_050a
     - Trust, Issuance, Interoperability
     - Policy & Trust Marks enforcement
     - Wallet Instance verifies that the Credential Issuer is authorized to issue the requested Digital Credential through the application of metadata policies and the verification of Trust Marks.
   * - WP_050b
     - Trust, Issuance, Interoperability
     - Supported ID confirmation
     - Wallet Instance verifies that every requested ``credential_configuration_id`` appears in the Credential Issuer’s ``credential_configurations_supported`` metadata; missing IDs cause the offer to fail.
   * - WP_051
     - Issuance, Interoperability
     - Credential Request using OAuth 2.0 code flow
     - Wallet Instance successfully requests PID/(Q)EAA from the PID/(Q)EAA Provider using the Authorization Code Flow per `OpenID4VCI`_.
   * - WP_052
     - Issuance, Interoperability
     - PAR Request: payload construction
     - Wallet Instance generates a fresh PKCE ``code_verifier``, Wallet Attestation PoP JWT, and ``state`` value, then wraps them into a Request Object signed with its private key per :rfc:`9126`, and posts it to the PAR Endpoint.
   * - WP_052a
     - Issuance, Interoperability
     - Secure PKCE ``code_verifier`` generation
     - Wallet Instance creates the ``code_verifier`` following  :rfc:`7636` recommendations, as a high-entropy random string using unreserved characters with a length between 43 and 128.
   * - WP_052b
     - Issuance, Interoperability
     - Wallet Attestation PoP JWT creation
     - Wallet Instance generates the Wallet Attestation PoP JWT (per OAuth-Client-Attestation-PoP parameters as defined in `OAUTH-ATTESTATION-CLIENT-AUTH`_) and binds it to the same ephemeral public key referenced in the Wallet Attestation’s ``cnf.jwk``.
   * - WP_052c
     - Issuance, Security
     - Wallet Attestation PoP JWT signing
     - Wallet Instance signs the PoP JWT with the ephemeral private key corresponding to the public key in the Wallet Attestation’s ``cnf.jwk``.
   * - WP_052d
     - Issuance, Interoperability
     - Specify Digital Credential types
     - Wallet Instance embeds correct Digital Credential types in the Request Object using the ``authorization_details`` (or ``scope``) parameter (per RAR :rfc:`9396`).
   * - WP_053
     - Issuance, Security
     - Authorization Request
     - Wallet Instance sends an Authorization Request to the Credential Issuer Authorization Endpoint using the received ``request_uri`` and ``client_id``.
   * - WP_053a
     - Issuance, Security
     - Enforce one-time ``request_uri``
     - Wallet Instance submits the Authorization Request with a freshly obtained ``request_uri``, and that ``request_uri`` is accepted only once.
   * - WP_054
     - Issuance, Interoperability
     - Validate Authorization Response: required parameter
     - Wallet Instance checks that the Authorization Response contains all required parameters (``code``, ``state``, and ``iss``); missing parameters trigger error handling.
   * - WP_054a
     - Issuance, Security
     - Validate Authorization Response: verify state matching
     - Wallet Instance compares the returned ``state`` value with the one originally sent in the Request Object (:rfc:`6749`) and continues only if they match exactly.
   * - WP_054b
     - Issuance, Security
     - Validate Authorization Response: confirm Credential Issuer identity
     - Wallet Instance checks that the ``iss`` parameter in the Authorization Response matches the identifier of the Credential Issuer with which it initiated the communication (:rfc:`9207`).
   * - WP_055
     - Issuance, Interoperability
     - Send a Token Request
     - Wallet Instance sends a POST request to the Token Endpoint with a URL-encoded body, including the received ``code`` (in the Authorization Response), the same ``redirect_uri`` (in the Request Object), and the ``code_verifier``.
   * - WP_055a
     - Issuance, Interoperability
     - Token request proof parameters
     - The Token Request carries the required proofs in headers: a DPoP proof JWT, a Wallet Attestation JWT, and Wallet Instance’s PoP JWT (per OAuth-Client-Attestation and OAuth-Client-Attestation-PoP as defined in `OAUTH-ATTESTATION-CLIENT-AUTH`_).
   * - WP_055b
     - Issuance, Interoperability
     - Generate DPoP key pair/proof
     - Wallet Instance generates a fresh DPoP key pair and its DPoP proof JWT following the instructions provided in :rfc:`9449#section-4` for the Token Request to the Credential Issuer.
   * - WP_055c
     - Issuance, Security
     - Sign DPoP proof
     - Wallet Instance signs the DPoP proof JWT with the DPoP private key generated for this scope.
   * - WP_055d
     - Issuance, Interoperability
     - Token request proof parameters
     - The Wallet Attestation JWT is signed using the private key bound to Wallet Instance, where its related public key is provided within the Wallet Attestation (``cnf.jwk`` claim).
   * - WP_056
     - Issuance, Interoperability
     - Credential Request
     - Wallet Instance sends a POST request to the Credential Endpoint including the Access Token, DPoP Proof JWT, Credential type, and the valid PoP of Credential-bound key.
   * - WP_056a
     - Issuance, Security
     - Fetch nonce for the Digital Credential key proof
     - Wallet Instance sends a POST request to the Credential Issuer’s Nonce Endpoint and obtains a fresh nonce, which is then used to generate the PoP of the key material bound to the issued Digital Credential.
   * - WP_056b
     - Issuance, Security
     - Fresh DPoP proof
     - Wallet Instance generates a fresh DPoP proof with the same key used for the Token Request DPoP proof, and in accordance with :rfc:`9449#section-4`.
   * - WP_056c
     - Issuance, Security
     - Match the Credential key proof to the DPoP key
     - Wallet Instance includes a ``proofs`` object of type ``jwt`` in the Credential Request that demonstrates possession of the cryptographic key material; the ``jwk`` value in this object matches the public key referenced in the DPoP proof.
   * - WP_057
     - Issuance, Interoperability
     - Multiple Digital Credential request
     - When a Credential Issuer offers multiple Digital Credentials, Wallet Instance makes a separate and correctly formatted Credential Request for each Digital Credential it intends to accept.
   * - WP_058
     - Issuance, Interoperability
     - Batch Credential Request
     - In case of Batch Issuance, Wallet Instance sends a batch Credential request to the Credential Endpoint that includes: the Access Token, a DPoP proof JWT, the credential type, and a ``proofs`` parameter containing all key proofs.
   * - WP_058a
     - Issuance, Security
     - Batch Issuance: key generation
     - In case of Batch Issuance, Wallet Instance generates a number of fresh Digital Credential key pairs equal to the ``batch_size`` value.
   * - WP_058b
     - Issuance, Interoperability
     - Batch Issuance: PoP of batch Credential keys
     - In case of Batch Issuance, Wallet Instance generates N key proofs using the provided ``c_nonce``, one for each Digital Credential in the batch, where N equals the ``batch_size`` value.
   * - WP_059
     - Issuance, Interoperability
     - Validate Credential Response for required parameters
     - Wallet Instance inspects the Credential Response payload, verifying all mandatory PID/(Q)EAA parameters are present and valid as defined in :ref:`Table of Credential Response <table_credential_response_claim>`; if any parameter is missing or invalid, it rejects the response with an error.
   * - WP_060
     - Issuance, Interoperability
     - Verify Digital Credential type/schema
     - Wallet Instance retrieves the issued Digital Credential from the response’s ``credential`` claim, verifies that its type matches the requested type, and validates the schema against :ref:`credential-data-model:Digital Credential Data Model`; if either check fails, it rejects the Digital Credential.
   * - WP_061
     - Issuance, Security
     - Validate Credential Issuer Trust Chain
     - Wallet Instance verifies the Digital Credential’s Trust Chain from its header to confirm that the Credential Issuer is trusted.
   * - WP_062
     - Issuance, Interoperability
     - Format-specific Digital Credential verification
     - Wallet Instance verifies whether a Digital Credential is in SD-JWT VC or mdoc-CBOR format, and then runs the appropriate verification. If it fails, it rejects the Credential.
   * - WP_062a
     - Issuance, Security, Interoperability
     - Verify SD-JWT Credential integrity
     - Wallet Instance obtains the ``alg`` and ``kid`` values from the SD-JWT header, retrieves the corresponding public key, and verifies the signature; if invalid, the SD-JWT Credential is rejected.
   * - WP_062b
     - Issuance, Security, Interoperability
     - Verify mdoc-CBOR Credential integrity
     - Wallet Instance extracts the signature algorithm from the protected header of the mdoc-CBOR ``COSE_Sign1``, retrieves the Credential Issuer’s public key from the ``kid`` or ``x5chain`` in the unprotected header, and verifies the COSE signature over the MSO; if invalid, the Credential is rejected.
   * - WP_063
     - Issuance, Privacy
     - User consent for credential storage
     - Wallet Instance prompts the User for consent and stores the Digital Credential only after explicit approval.
   * - WP_064
     - Issuance, Interoperability
     - Notification Handling
     - Wallet Instance sends an HTTP POST request to the Notification Endpoint with ``Content-Type: application/json``.
   * - WP_064a
     - Issuance, Interoperability
     - Notification Parameters
     - The Notification Request payload contains the ``notification_id`` from the Credential Response and an ``event`` value of either ``credential_accepted``, ``credential_deleted``, or ``credential_failure``; it may also include a valid ASCII ``event_description``.
   * - WP_064b
     - Issuance, Privacy
     - Protect User privacy in notification content
     - The ``event_description`` contains only generic, user-neutral text and does not disclose User behavior or device status.
   * - WP_065
     - Issuance, Security
     - Handle deferred issuance
     - Wallet Instance evaluates the Credential Response; if it contains both ``transaction_id`` and ``interval``, Wallet Instance recognizes the flow as deferred issuance.
   * - WP_066
     - Issuance, Interoperability
     - Deferred issuance request after interval
     - Wallet Instance submits a Deferred Credential Request only after the required ``interval`` has passed.
   * - WP_066a
     - Issuance, Interoperability
     - Deferred issuance request with transaction_id
     - Wallet Instance sends a Deferred Credential Request as an HTTP POST with ``Content-Type: application/json``, and the request body contains the required ``transaction_id``.
   * - WP_066b
     - Issuance, Interoperability
     - Deferred request with still-valid Access Token
     - Wallet Instance includes the existing Access Token in the deferred request if the ``interval`` parameter value is less than the expiration time set for the Access Token.
   * - WP_066c
     - Issuance, Interoperability
     - Fresh DPoP-bound Access Token via the Refresh
     - When the existing Access Token would expire before the deferred request can be made, Wallet Instance obtains a new DPoP-bound Access Token via the Refresh Token flow.
   * - WP_067
     - Issuance, Interoperability
     - New Credential Issuance flow
     - When Wallet Instance fails to refresh an expiring Access Token, it initiates an entirely new Credential Issuance flow.
   * - WP_068
     - Issuance, Interoperability
     - Refresh Token Request
     - Wallet Instance sends a POST request to the Credential Issuer’s Token Endpoint with ``grant_type=refresh_token``, a valid refresh_token, a DPoP header with a fresh DPoP proof JWT, and OAuth headers carrying the Wallet Attestation JWT and its PoP.
   * - WP_068a
     - Issuance, Security
     - Refresh Token: generate proofs
     - For a refresh Access Token request, Wallet Instance generates a new DPoP JWT and a new Wallet Attestation PoP, and includes them in the request.
   * - WP_068b
     - Issuance, Interoperability
     - Refresh Token: maintain binding
     - Wallet Instance reuses the same key bound to the Wallet Attestation PoP and the DPoP proof from the original Access Token request, ensuring the refreshed Access Token remains cryptographically bound and valid.
   * - WP_069
     - Issuance, Security
     - Check Digital Credential status
     - Wallet Instance verifies the status of each stored Digital Credential by retrieving and validating a Status List Token as described in `TOKEN-STATUS-LIST`_ and the profiles specified in `:ref:`credential-revocation:Token Status List (Digital Credentials Profile)`.
   * - WP_070
     - Issuance, Security
     - Re-issuance flow: detect re-issuance necessity (update status)
     - Wallet Instance updates a Digital Credential when the Status List shows ``0x03`` (``UPDATE``) or ``0x0F`` (``ATTRIBUTE_UPDATE``) for that Credential.
   * - WP_071
     - Issuance, Security
     - Re-issuance flow: verify Access Token validity for re-issuance
     - When an update is detected for a Digital Credential, Wallet Instance verifies the validity of the associated Access Token. If the token is valid, Wallet Instance proceeds with Credential re-issuance.
   * - WP_071a
     - Issuance, Security
     - Re-issuance flow: refresh expired Access Token
     - If the Access Token is expired but a valid Refresh Token is available, Wallet Instance initiates a Refresh Token flow to obtain a new DPoP-bound Access Token, following the Refresh Token Flow.
   * - WP_071b
     - Issuance, Security
     - Restart issuance on full expiry
     - Wallet Instance re-authenticates the User when initiating  a new Credential Issuance flow.
   * - WP_072
     - Issuance, Security
     - Retrieve refreshed Credential
     - Wallet Instance, with a valid DPoP-bound Access Token, sends a request to the Credential Endpoint and successfully retrieves the updated Digital Credential.
   * - WP_073
     - Issuance, Security and Privacy
     - Delete old Digital Credentials
     - After storing a new Digital Credential, Wallet Instance deletes the previous version so that only the latest Digital Credential remains stored.
   * - WP_073a
     - Issuance, Security and Privacy
     - Delete old batch Credentials
     - When the Wallet Instance receives and stores a new batch of the same Credential with the same claims, it deletes the previous Credentials.
   * - WP_074
     - Issuance, UX
     - Consent on new Digital Credential store with ``user_attribute`` update
     - If the Digital Credential update involves changes to the User's attribute values (``attribute_update``), Wallet Instance prompts the User for consent before storing the new refreshed Digital Credential.
   * - WP_075
     - Issuance, UX
     - No consent on new Digital Credential store without ``user_attribute`` update
     - If the Digital Credential update only concerns credential metadata changes (``update``), Wallet Instance automatically stores the new refreshed Digital Credential without requesting additional consent from the User.

.. _wallet-credential-presentation-testcases:

Test Cases for Presentation Phase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This section lists the test cases from Section :ref:`credential-presentation:Digital Credential Presentation`,
covering both the **Remote Flow** and the **Proximity Flow** presentation phases.


.. list-table::
   :class: longtable
   :widths: 15 15 20 55
   :header-rows: 1

   * - **Test Case ID**
     - **Purpose**
     - **Description**
     - **Expected Result**
   * - WP_076
     - Remote-flow, Presentation, Interoperability
     - Obtain Authorization Request URL in Same Device flow
     - In the Same Device flow, Wallet Instance successfully obtains a URL and extracts the following parameters: ``client_id``, ``request_uri``, ``state``, and ``request_uri_method``.
   * - WP_077
     - Remote-flow, Presentation, Interoperability
     - Obtain Authorization Request URL in Cross Device flow
     - In the Cross Device flow, Wallet Instance successfully scans and parses a QR Code to extract the following parameters: ``client_id``, ``request_uri``, ``state``, and ``request_uri_method``.
   * - WP_078
     - Remote-flow, Trust, Presentation, Interoperability
     - Relying Party identity discovery
     - Wallet Instance successfully uses Federation API endpoints (``.well-known/openid-federation``, ``/fetch``) to retrieve current metadata and configurations of the Relying Party.
   * - WP_079
     - Remote-flow, Trust, Presentation, Interoperability
     - Relying Party Trust Chain evaluation
     - Wallet Instance successfully validates the Trust Chain of the Relying Party (provided statically or built through a Federation Entity Discovery process) from the Trust Anchor down to the Relying Party itself, confirming that the Relying Party is a recognized and trusted member of the federation.
   * - WP_080
     - Remote-flow, Trust, Presentation, Interoperability
     - Relying Party Trust Mark check
     - Wallet Instance successfully evaluates any Trust Marks included in the Relying Party’s Entity Configuration to ensure they are valid and indicate compliance with federation policies.
   * - WP_081
     - Remote-flow, Trust, Presentation, Security
     - Validate ``request_uri``
     - Wallet Instance checks the ``request_uri`` against its locally cached list of allowed URIs (from the ``openid_credential_verifier.request_uris`` in the Trust Chain) and only proceeds when it finds an exact match; if no match is found, it rejects the request.
   * - WP_082
     - Remote-flow, Presentation, Interoperability
     - GET Request Object
     - If the ``request_uri_method`` in the initial request is ``get`` or is absent, Wallet Instance sends an HTTP GET request to the Relying Party's ``request_uri`` endpoint, and successfully retrieves a signed Request Object JWT.
   * - WP_083
     - Remote-flow, Presentation, Interoperability
     - POST Request Object
     - If the ``request_uri_method`` in the initial request is ``post``, Wallet Instance sends an HTTP POST request to the Relying Party's ``request_uri`` endpoint, including its metadata as ``wallet_metadata`` and ``wallet_nonce`` parameters, with content type ``application/x-www-form-urlencoded``, and successfully retrieves a signed Request Object JWT.
   * - WP_083a
     - Remote-flow, Presentation, Interoperability
     - Construct ``wallet_metadata``
     - Wallet Instance formats the ``wallet_metadata`` as a JSON object that includes the ``vp_formats_supported``, and optionally ``client_id_prefixes_supported`` and ``request_object_signing_alg_values_supported`` per Section 10.1 of [`OpenID4VP`_].
   * - WP_083b
     - Remote-flow, Presentation, Privacy
     - Exclude PII in ``wallet_metadata``
     - The ``wallet_metadata`` JSON contains no User-identifiable or device-specific fields (e.g. names, hardware details).
   * - WP_083c
     - Remote-flow, Presentation, Security
     - Generate replay nonce
     - A fresh ``wallet_nonce`` is generated and included in the POST request payload alongside the ``wallet_metadata`` to mitigate replay attacks.
   * - WP_084
     - Remote-flow, Trust, Presentation, Security
     - Relying Party public key retrieval
     - Wallet Instance fetches the correct Relying Party’s public key exclusively from the ``metadata.openid_credential_verifier.jwks`` field located within the Relying Party's Entity Configuration provided by the Trust Chain, and using the key identifier (``kid``) from the request JWT header.
   * - WP_085
     - Remote-flow, Presentation, Security
     - Request Object signature verification
     - Wallet Instance confirms the integrity of the signed Request Object by successfully performing the cryptographic signature validation against the Relying Party’s public key.
   * - WP_086
     - Remote-flow, Presentation, Security
     - Match ``client_id`` across contexts
     - Wallet Instance confirms that the ``iss`` claim in the signed Request Object exactly equals both the ``client_id`` it originally extracted from the Authorization Request URL and the ``sub`` value in the Relying Party’s Entity Configuration. Any discrepancy causes the request to be rejected.
   * - WP_087
     - Remote-flow, Presentation, Security
     - Check Relying Party eligibility
     - Wallet Instance authorizes the request and proceeds with the flow when the Relying Party's metadata, policies, and a valid Trust Mark collectively confirm its permission to request the specified credential.
   * - WP_088
     - Remote-flow, Presentation, Privacy
     - User consent for disclosure
     - Wallet Instance requests the User's consent by presenting a UI screen that clearly displays the verified identity of the Relying Party and a list of all requested data attributes.
   * - WP_089
     - Remote-flow, Presentation, UX
     - Handle ``request_uri`` endpoint errors
     - When the Relying Party's ``request_uri`` endpoint responds with an error, Wallet Instance displays a clear, human-readable message to the User explaining the failure and securely terminates the flow.
   * - WP_089a
     - Remote-flow, Presentation, UX
     - Logging ``request_uri`` errors
     - Wallet Instance internally logs the detailed error information.
   * - WP_089b
     - Remote-flow, Presentation, UX
     - Recovering from ``request_uri`` errors
     - For a recoverable error, such as ``server_error``, Wallet Instance prompts the User with a specific recovery action, such as suggesting a retry or “Scan QR again” option, if applicable.
   * - WP_090
     - Remote-flow, Presentation, Interoperability
     - Notify Relying Party on invalid request
     - If the Request Object is invalid or fails verification, Wallet Instance sends an Authorization Error Response via HTTP POST to the Relying Party’s ``response_uri`` Endpoint.
   * - WP_091
     - Remote-flow, Presentation, Interoperability
     - Send Authorization Response
     - If the Request Object verification is valid, Wallet Instance sends an Authorization Response via HTTP POST to the Relying Party’s ``response_uri`` as per ``response_mode=direct_post.jwt``.
   * - WP_091a
     - Remote-flow, Presentation, Security
     - Validate ``response_uri``
     - Before sending the Authorization Response, Wallet Instance confirms the ``response_uri`` exactly matches one of the Relying Party’s attested ``response_uris`` in its metadata; a mismatch aborts the request.
   * - WP_092
     - Remote-flow, Presentation, Security
     - Encrypt Authorization Response
     - Wallet Instance encrypts the Authorization Response JWT per Section 8.3 of [`OpenID4VP`_] using the Relying Party’s public key.
   * - WP_093
     - Remote-flow, Presentation, Security
     - Construct ``vp_token`` with ``state``
     - The Authorization Response JWT payload includes the original ``state`` value and a ``vp_token`` object with entries for each requested Credential presentation.
   * - WP_093a
     - Remote-flow, Presentation, Interoperability
     - Include signed presentations
     - Within that ``vp_token``, there are the requested Credential(s) in SD JWT VC format.
   * - WP_093b
     - Remote-flow, Presentation, Security
     - Append Key Binding JWT
     - Wallet Instance generates for every individual SD-JWT presentation within the ``vp_token``, its own corresponding Key Binding JWT.
   * - WP_093c
     - Remote-flow, Presentation, Security
     - Key Binding JWT format
     - The JOSE header of each generated Key Binding JWT includes ``"typ":"kb+jwt"`` and an ``alg`` to one of the supported signature algorithms, as well as a payload including the ``iat``, ``aud``, ``nonce``, and ``sd_hash`` claims per `OpenID4VP`_ .
   * - WP_094
     - Remote-flow, Presentation, Interoperability
     - Perform user-agent redirect
     - Upon receiving the ``redirect_uri``, Wallet Instance successfully performs a user-agent redirect to the ``redirect_uri`` supplied by the Relying Party, so the Relying Party can resume the interaction on the same device that initiated the flow.
   * - WP_094a
     - Remote-flow, Trust, Presentation, Security
     - Validate ``redirect_uri``
     - Wallet Instance verifies that the ``redirect_uri`` exactly matches one of the URIs listed in the Relying Party’s ``redirect_uris`` metadata. If it does not match, aborts the flow.
   * - WP_095
     - Proximity-flow, Presentation, Security
     - Support supervised/unsupervised retrieval
     - Wallet Instance supports a Credential presentation using the Supervised Device Retrieval method for an in-person verification scenario and via Device Retrieval (unsupervised) for automated verification without human oversight.
   * - WP_096
     - Proximity-flow, Presentation, Security
     - Device retrieval support
     - Wallet Instance supports Device Retrieval mechanisms via the Bluetooth Low Energy (BLE) or NFC.
   * - WP_096a
     - Proximity-flow, Presentation, Security
     - Enforce device retrieval only
     - Wallet Instance rejects any request to initiate a proximity flow using the Server Retrieval mechanism.
   * - WP_096b
     - Proximity-flow, Presentation, Security
     - Support BLE/NFC retrieval (conditional)
     - Wallet Instance completes the BLE or NFC retrieval flow successfully. BLE support is mandatory, while NFC support is RECOMMENDED. Support for at least one device retrieval method (BLE or NFC) is mandatory; failure constitutes non-compliance.
   * - WP_097
     - Proximity-flow, Presentation, UX
     - Supported DeviceEngagement mechanisms
     - Wallet Instance supports DeviceEngagement based on QR code or NFC Connection Handover.
   * - WP_097a
     - Proximity-flow, Presentation, Security
     - Support QR/NFC engagement (conditional)
     - Wallet Instance completes a full data-retrieval transaction over BLE and over NFC (where hardware is available). QR code support is mandatory, while NFC support is RECOMMENDED. Support for at least one engagement method (QR or NFC) is mandatory; failure constitutes non-compliance.
   * - WP_098
     - Proximity-flow, Presentation, Security
     - Relying Party authentication
     - Wallet Instance supports and performs Relying Party Instance Authentication in accordance with `ISO18013-5`_ reader-authentication.
   * - WP_099
     - Proximity-flow, Presentation, Interoperability
     - Domestic mDL support
     - Wallet Instance supports and processes mDL Credentials using both the IT Wallet domestic document type and namespaces and the standard `ISO18013-5`_ definitions without error (see `mdoc-CBOR Credential Format <credential-data-model.html#mdoc-cbor-credential-format>`_ for more details).
   * - WP_100
     - Proximity-flow, Presentation, Security
     - WSCA authentication
     - Wallet Instance prompts the User to perform a WSCA-based authentication, directly or by unlocking the application, and does not proceed with the proximity flow until it succeeds. Note: WSCA authentication applies when the PID (LoA High) is involved in the proximity flow.
   * - WP_101
     - Proximity-flow, Presentation, Security
     - Generate ephemeral EC key pair
     - Wallet Instance successfully generates a fresh ephemeral elliptic-curve key pair (per the chosen `ISO18013-5`_ cipher suite).
   * - WP_102
     - Proximity-flow, Presentation, Interoperability
     - CBOR encoding of DeviceEngagement data
     - DeviceEngagement is CBOR encoded and contains Version, Security, Capabilities, and OriginInfos (may be empty). For QR engagement it also includes DeviceRetrievalMode-BLEOptions and/or DeviceRetrievalMode-NFCOptions. For NFC engagement, these options are omitted.
   * - WP_102a
     - Proximity-flow, Presentation, Interoperability
     - DeviceEngagement over QR
     - The QR mdoc: URI encodes the valid CBOR DeviceEngagement encoded (per Section 9.1 of [ISO18013-5_]) using base64url-without-padding (:rfc:`4648`).
   * - WP_102b
     - Proximity-flow, Presentation, Interoperability
     - Verify Security component
     - The Security component within the DeviceEngagement data contains a supported cipher suite identifier and the Wallet Instance’s ephemeral public key per `ISO18013-5`_ Table 22.
   * - WP_102c
     - Proximity-flow, Presentation, Interoperability
     - Verify DeviceRetrievalMode-BLEOptions component
     - The DeviceRetrievalMode-BLEOptions component within the DeviceEngagement data indicates Central Client Mode and carries the correct device UUID.
   * - WP_102d
     - Proximity-flow, Presentation, Interoperability
     - Verify DeviceRetrievalMode-NFCOptions component
     - The DeviceRetrievalMode-NFCOptions component declares supported role (PICC for Wallet Instance) and maximum APDU command/response sizes per ISO mapping.
   * - WP_102e
     - Proximity-flow, Presentation, Interoperability
     - Verify Capabilities component
     - The Capabilities component within the DeviceEngagement data correctly sets both the ``HandoverSessionEstablishmentSupport`` and ``ReaderAuthAllSupport`` flags to ``true``.
   * - WP_102f
     - Proximity-flow, Presentation, Interoperability
     - Verify OriginInfos component
     - If the OriginInfos component, is present within the DeviceEngagement data, is correctly encoded as an array (which may be empty).
   * - WP_103
     - Proximity-flow, Presentation, UX
     - DeviceEngagement over NFC (Connection Handover)
     - Wallet Instance exposes DeviceEngagement via NFC Connection Handover either Static or Negotiated.
   * - WP_103a
     - Proximity-flow, Presentation, Interoperability
     - NFC Connection Handover (Static)
     - Wallet Instance acts as NFC Tag (Type 4) and provides a Handover Select with at least one Alternative Carrier Record and associated Carrier Configuration Record; an Auxiliary Data Record carries the DeviceEngagement (type iso.org:18013:deviceengagement, id “mdoc”).
   * - WP_103b
     - Proximity-flow, Presentation, Interoperability
     - NFC Connection Handover (Negotiated)
     - Wallet Instance exposes the service ``urn:nfc:sn:handover``; upon Handover Request, it returns Handover Select with exactly one selected carrier and the auxiliary DeviceEngagement.
   * - WP_103c
     - Proximity-flow, Presentation, Security, Interoperability
     - Early SessionEstablishment via TNEP
     - If ``HandoverSessionEstablishmentSupport`` set to ``true`` in DeviceEngagement, Wallet Instance accepts early ``SessionEstablishment`` over the announced TNEP service during negotiated handover and later verifies it matches the ``SessionEstablishment`` received during data retrieval.
   * - WP_103d
     - Proximity-flow, Presentation, Interoperability
     - Carrier Configuration Record encoding
     - Wallet Instance successfully includes a Carrier Configuration Record for each supported carrier. For NFC, type ``iso.org:18013:nfc``, ID ``nfc``, content per  Section 9.2.2 of [`ISO18013-5`_]. For BLE, content per Section 11.1.2 of [`ISO18013-5`_].
   * - WP_103e
     - Proximity-flow, Presentation, Interoperability
     - Auxiliary Data Record for DeviceEngagement
     - Wallet Instance successfully provides an Auxiliary Data Record carrying DeviceEngagement with type ``iso.org:18013:deviceengagement``, ID ``mdoc``, using NFC Forum external type (0x04). Each Alternative Carrier Record MUST reference this record.
   * - WP_103f
     - Proximity-flow, Presentation, Interoperability
     - Alternative Carrier Records
     - In Static Handover, Handover Select includes one oe more Alternative Carrier Records; in Negotiated Handover, Handover Select contains exactly one selected carrier. The NFC Alternative Carrier references the ``nfc`` Carrier Configuration Record.
   * - WP_103g
     - Proximity-flow, Presentation, Security
     - Early SessionEstablishment mismatch
     - If early SessionEstablishment is received during Negotiated Handover, Wallet Instance successfully verifies that it matches the SessionEstablishment received during Device Retrieval; on mismatch Wallet Instance terminates the flow
   * - WP_103h
     - Proximity-flow, Presentation, Interoperability
     - No early SessionEstablishment
     - If no early SessionEstablishment is received during Negotiated Handover, the Wallet Instance proceeds with Device Retrieval as normal (no failure), per the NFC DeviceEngagement note.
   * - WP_104
     - Proximity-flow, Presentation, Security
     - Derive session keys
     - Wallet Instance successfully derives session keys by performing the negotiated key-agreement protocol with its ephemeral private key and the Relying Party's ephemeral public key.
   * - WP_105
     - Proximity-flow, Presentation, Security
     - Decrypt & verify ``SessionEstablishment``
     - Wallet Instance successfully decrypts the ``SessionEstablishment`` message using the derived session key and validates the Relying Party's signature.
   * - WP_106
     - Proximity-flow, Presentation, Security
     - Validate ``SessionEstablishment`` contents
     - Wallet Instance verifies the ``SessionEstablishment`` message includes the Relying Party’s Pub Key and a request for specific attribute(s) from the Relying Party.
   * - WP_107
     - Proximity-flow, Presentation, Privacy
     - Prompt attribute consent
     - Wallet Instance decrypts and displays the requested attributes to the User in a consent screen and proceeds only after receiving explicit User approval.
   * - WP_107a
     - Proximity-flow, Presentation, Privacy
     - Display Relying Party certificate
     - Wallet Instance displays the full, parsed Relying Party Registration Certificate to the User for transparency before User consent and data disclosure.
   * - WP_108
     - Proximity-flow, Presentation, Interoperability
     - Retrieve mdoc Credentials
     - Wallet Instance successfully retrieves each requested mdoc Credential from storage, preparing it for the mdoc Response.
   * - WP_109
     - Proximity-flow, Presentation, Interoperability
     - Prepare mdoc Response
     - Wallet Instance successfully builds the CBOR-encoded ``SessionData`` message (the mdoc Response) including a ``documents`` array populated with the requested Credentials.
   * - WP_110
     - Proximity-flow, Presentation, Security, Interoperability
     - mdoc authentication
     - Wallet Instance correctly signs the ``deviceSigned`` authentication data for each presented Credential, following the mdoc authentication process as specified in Section 12.4 of [`ISO18013-5`_].
   * - WP_111
     - Proximity-flow, Presentation, Interoperability
     - Validate mdoc Response structure
     - Wallet Instance constructs the mdoc Response as a CBOR-encoded object that includes a ``version`` component at its root and ensures each document within the ``documents`` array contains the mandatory ``docType`` component.
   * - WP_111a
     - Proximity-flow, Presentation, Security
     - Validate ``deviceSigned`` component
     - Within each document, the ``deviceSigned`` component includes a ``deviceNameSpaces`` structure (possibly empty) plus a ``deviceAuth`` ``COSE_Sign1`` containing the required ``deviceSignature`` over the device-authentication data.
   * - WP_112
     - Proximity-flow, Presentation, Security
     - Encrypt ``SessionData``
     - Wallet Instance encrypts the ``SessionData`` message with the derived session keys.
   * - WP_112a
     - Proximity-flow, Presentation, Interoperability
     - BLE transport of messages
     - Over BLE (using the ISO GATT characteristics), Wallet Instance correctly receives the Relying Party’s encrypted ``SessionEstablishment`` and transmits its encrypted ``SessionData`` (and any status/termination codes).
   * - WP_112b
     - Proximity-flow, Presentation, Interoperability
     - NFC transport of messages
     - Over NFC (using the APDU flow), the Wallet Instance correctly receives the Relying Party’s encrypted ``SessionEstablishment`` and transmits its encrypted ``SessionData``, handling status words and fragmentation without errors.
   * - WP_112c
     - Proximity-flow, Presentation, Interoperability
     - BLE UUID/MTU consistency
     - The Wallet’s BLE service/characteristic `UUIDs` and effective MTU used on the link are consistent with the values advertised in DeviceEngagement (and/or Carrier Configuration), and the Wallet segments messages accordingly.
   * - WP_112d
     - Proximity-flow, Presentation, Security
     - BLE Ident characteristic (optional)
     - If the Ident characteristic is implemented, Wallet Instance verifies the Relying Party’s Ident value before data retrieval and terminates the BLE connection on mismatch, per Section 11.1.3 of [`ISO18013-5`_].
   * - WP_112e
     - Proximity-flow, Presentation, Interoperability
     - NFC SELECT AID handling
     - Wallet Instance successfully exposes `AID` and, upon SELECT `APDU`, returns valid `FCI` with correct `SW1/SW2`; subsequent ENVELOPE/GET RESPONSE exchanges.
   * - WP_112f
     - Proximity-flow, Presentation, Interoperability
     - NFC APDU size consistency
     - The Wallet’s `APDU` command/response sizing (including fragmentation and SW1=61 handling) is consistent with the max `PDU` sizes it advertised (Carrier Configuration / NFCOptions) during Device Engagement.
   * - WP_113
     - Proximity-flow, Presentation, Security
     - Terminate session/ inactivity timeout
     - Wallet Instance automatically terminates the session if no session-related messages are sent or received for the duration of its configured inactivity timeout.
   * - WP_113a
     - Proximity-flow, Presentation, Security
     - Terminate session/ no further request
     - Wallet Instance terminates the session once either it or the Relying Party has concluded the data exchange.
   * - WP_113b
     - Proximity-flow, Presentation, Security
     - Send termination signal
     - Wallet Instance transmits End command (or termination code) over BLE to signal session closure.
   * - WP_113c
     - Proximity-flow, Presentation, Security
     - Send termination over NFC
     - Wallet Instance signals end via a status code in ``SessionData`` and/or completes the APDU exchange per ISO; no further APDUs are accepted for the session.
   * - WP_114
     - Proximity-flow, Presentation, Security
     - Destroy session keys
     - When a session is terminated, Wallet Instance wipes all session keys and related ephemeral material from memory and storage.
   * - WP_114a
     - Proximity-flow, Presentation, Security
     - Close communication channel
     - Wallet Instance closes the active communication channel by disconnecting the BLE link or ending the NFC APDU exchange.

.. _user-attribute-deletion-testcases:

Test Cases for User Attribute Deletion on Relying Party Side
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section lists the test cases from Sections:

- :ref:`user-attribute-deletion:User's Attributes Deletion`
- `Relying Party Provider Backend Erasure Endpoint <relying-party-provider-backend-endpoint.html#relying-party-provider-backend-erasure-endpoint>`_

.. list-table::
   :class: longtable
   :widths: 15 15 20 55
   :header-rows: 1

   * - **Test Case ID**
     - **Purpose**
     - **Description**
     - **Expected Results**
   * - WP_115
     - Attribute Deletion, Lifecycle, Privacy
     - Attribute deletion function
     - Wallet Instance UI provides functions for the User to request attribute deletion, view transaction logs, and see a list of Relying Parties that hold their attributes.
   * - WP_115a
     - Attribute Deletion, Lifecycle, Privacy
     - Transaction logs for attribute deletion
     - The transaction log view shows Relying Parties in possession of the User's attributes.
   * - WP_116
     - Attribute Deletion, Lifecycle, Security
     - Relying Party metadata validation for deletion
     - When a User selects a Relying Party for attribute deletion, Wallet Instance fetches and validates its federation metadata, confirming the presence of an Erasure Endpoint.
   * - WP_117
     - Attribute Deletion, Lifecycle, Interoperability
     - Erasure Request
     - Wallet Instance correctly constructs, and sends a valid Erasure Request destined for the Relying Party's Erasure Endpoint.
   * - WP_117a
     - Attribute Deletion, Lifecycle, Privacy
     - Erasure Request logging
     - A log entry is created for each Erasure Request, containing the timestamp, the Relying Party's identifier, and the specific attributes requested for deletion.
   * - WP_118
     - Attribute Deletion, Lifecycle, UX
     - User redirection and callback for erasure
     - Wallet Instance successfully redirects the User to the Relying Party’s Erasure Endpoint and receives the Erasure Response via its callback mechanism.
   * - WP_119
     - Attribute Deletion, Lifecycle, Interoperability
     - Handles deletion/error response
     - Wallet Instance correctly processes both success and error responses for the Erasure Response from the Relying Party.
   * - WP_119a
     - Attribute Deletion, Lifecycle, UX
     - User notification on erasure
     - Wallet Instance displays a clear notification to the User indicating the success or failure of the Erasure Request.

.. _credential-backup-testcases:

Test Cases for Digital Credential’s Backup and Restore
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section lists the test cases from Section :ref:`backup-restore:Backup and Restore`.

.. list-table::
   :class: longtable
   :widths: 15 15 20 55
   :header-rows: 1

   * - **Test Case ID**
     - **Purpose**
     - **Description**
     - **Expected Results**
   * - WP_120
     - Backup and Restore, UX
     - Credential backup initiation
     - The User successfully triggers the Credential backup operation on Wallet Instance.
   * - WP_120a
     - Backup and Restore, Security
     - Random key phrase display
     - Wallet Instance invokes the backup APIs, selects 10 random key phrases from a pre-generated list and displays them to the User.
   * - WP_120b
     - Backup and Restore, Security
     - Secure key phrase storage instruction
     - Wallet Instance displays a clear instruction for the User to securely store the generated key phrases.
   * - WP_121
     - Backup and Restore, Security
     - Key derivation from key phrases
     - Wallet Instance derives an encryption key from the User’s key phrases using a key derivation function (e.g., ``PBKDF2``, ``Bcrypt``, ``Scrypt``, ``Argon2``).
   * - WP_121a
     - Backup and Restore, Security
     - Key derivation function configuration
     - If ``PBKDF2`` with ``SHA-256`` is used, the function is configured with an iteration count of at least ``600,000``.
   * - WP_122
     - Backup and Restore, Interoperability
     - Signed backup JWT creation
     - Wallet Instance creates a backup file containing a signed JWT that encapsulates the backup data.
   * - WP_122a
     - Backup and Restore, Interoperability
     - JOSE header for backup JWT
     - The backup JWT header contains the correct ``alg`` and a ``typ`` of ``wallet-unit-credentials-backup+jwt``.
   * - WP_122b
     - Backup and Restore, Interoperability
     - Backup JWT payload contents
     - The backup JWT payload includes the required claims: ``timestamp``, ``wallet_provider_id``, ``wallet_instance_version``, ``wallet_attestation``, and ``credentials_backup``.
   * - WP_122c
     - Backup and Restore, Security
     - Optional transaction history in backup JWT
     - The ``credentials_backup`` claim contains the transaction history for each Credential, if supported.
   * - WP_122d
     - Backup and Restore, Security
     - Credential identifiers in backup JWT
     - The ``credentials_backup`` claim contains entries keyed by the Issuer identifier, and each entry lists one or more ``credential_configuration_ids`` corresponding to the issued credentials.
   * - WP_123
     - Backup and Restore, Security
     - Backup JWT signing with attested key
     - Wallet Instance signs the backup JWT with the private key corresponding to the public key found in the ``cnf`` claim of the Wallet Attestation JWT.
   * - WP_123a
     - Backup and Restore, Security
     - Attestation validity check for backup JWT
     - Before signing the backup JWT, Wallet Instance verifies the validity of its own Wallet Attestation.
   * - WP_124
     - Backup and Restore, Security
     - Backup file encryption with User key
     - Wallet Instance encrypts the backup using the key derived from the User's key phrases.
   * - WP_125
     - Backup and Restore, UX
     - Secure storage location selection prompt
     - Wallet Instance prompts the User to select a location to save the encrypted backup file, offering options such as local or cloud storage.
   * - WP_126
     - Backup and Restore, UX
     - Credential restore initiation
     - The User successfully triggers the Credential restore operation on Wallet Instance.
   * - WP_127
     - Backup and Restore, UX
     - Backup file/key phrase selection for restore
     - The User successfully selects a backup file from the storage and enters their recovery key phrases.
   * - WP_128
     - Backup and Restore, Interoperability
     - Wallet Attestation extraction from backup JWT
     - Wallet Instance extracts the Wallet Attestation JWT from the ``wallet_attestation`` claim of backup JWT found within the backup file.
   * - WP_128a
     - Backup and Restore, Security
     - Ignore Wallet Attestation expiration during restore
     - The restore process continues successfully even if the Wallet Attestation JWT in the backup file is expired.
   * - WP_129
     - Backup and Restore, Security
     - Backup JWT signature verification
     - Wallet Instance successfully verifies the signature of the backup JWT using the Wallet Attestation public key from the ``cnf.jwk`` claim within the ``wallet_attestation`` claim.
   * - WP_130
     - Backup and Restore, Interoperability
     - Credential issuance from restored backup
     - For each Credential entry in the backup JWT, Wallet Instance successfully extracts the Issuer URL, and the ``credential_configuration_id``.
   * - WP_130a
     - Backup and Restore, Interoperability
     - Retrieve the Issuer metadata
     - For each Issuer URL, Wallet Instance successfully fetches the corresponding Issuer metadata.
   * - WP_130b
     - Backup and Restore, Interoperability
     - Credential issuance request
     - For each Credential, Wallet Instance successfully initiates a new Wallet-Initiated Authorization Code Issuance Flow bound to the new Wallet Instance key (fresh Holder Key Binding), and not a token renewal or a Re-Issuance Flow request.

.. _wallet-instance-optional-testcases:

Optional Test Cases for Wallet Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section lists the test cases from Sections:

- :ref:`wallet-instance:Wallet Instance`
- `Request-Specific Error Responses <wallet-provider-endpoint.html#request-specific-error-responses>`_
- `Mobile Application Instance Initialization <mobile-application-instance.html#mobile-application-instance-initialization>`_

These test cases are optional and have been designed for the IT Wallet implementation, managed by PagoPA. They are intended for implementers who need to verify compatibility with the specific features of this reference model.

.. list-table::
   :class: longtable
   :widths: 15 15 20 55
   :header-rows: 1

   * - **Test Case ID**
     - **Purpose**
     - **Description**
     - **Expected Results**
   * - WP_131
     - Wallet Initialization / Registration, Lifecycle, Security
     - Nonce request for replay protection
     - Wallet Instance requests and receives a single-use, short-lived nonce from the Wallet Provider's Nonce Endpoint.
   * - WP_132
     - Wallet Initialization / Registration, Lifecycle, Interoperability
     - Hardware-backed EC key pair generation/storage
     - Wallet Instance successfully generates a fresh hardware-backed EC key pair and stores its associated ``hardware_key_tag`` in the local secure storage.
   * - WP_132a
     - Wallet Initialization / Registration, Lifecycle, Security
     - Pre-existing key deletion during initialization
     - Wallet Instance checks for the presence of pre-existing Cryptographic Hardware Keys during initialization, and successfully deletes them.
   * - WP_133
     - Wallet Initialization / Registration, Lifecycle, Interoperability
     - Wallet Initialization Request submission
     - Wallet Instance successfully sends to the Wallet Provider an Initialization request with the required ``nonce``, ``key_attestation``, and ``hardware_key_tag`` parameters.
   * - WP_133a
     - Wallet Initialization / Registration, Lifecycle, Interoperability
     - SHA-256 hash computation
     - Wallet Instance successfully computes a SHA-256 digest (``client_data_hash``) over the ``nonce``, the ``hardware_key_pub``, and the ``hardware_key_tag``,
   * - WP_133b
     - Wallet Initialization / Registration, Lifecycle, Interoperability
     - Key Attestation
     - Wallet Instance successfully invokes the Key Attestation API with the ``client_data_hash`` and obtains a signed attestation from the Key Attestation API.
   * - WP_134
     - Wallet Initialization / Registration, Lifecycle, Security
     - Key Binding request
     - Wallet Instance sends a Key Binding request that contains an ``assertion`` parameter whose value is a signed JWT.
   * - WP_134a
     - Wallet Initialization / Registration, Lifecycle, Security
     - Signing Key Binding JWT
     - Wallet Instance successfully signs the Key Binding request JWT with the Wallet Hardware public key.
   * - WP_135
     - Wallet Initialization / Registration, Lifecycle, Security
     - Wallet Initialization Request validation
     - Wallet Provider successfully checks the Initialization Request parameters: the ``nonce`` and ``key_attestation``, and, if valid, returns a confirmation response.
   * - WP_135a
     - Wallet Initialization / Registration, Lifecycle, Security
     - Nonce uniqueness verification
     - Wallet Provider rejects any Initialization Request containing a nonce that it did not generate or that has already been used.
   * - WP_135b
     - Wallet Initialization / Registration, Lifecycle, Security
     - Key Attestation validation per guidelines
     - Wallet Provider validates the ``key_attestation`` against manufacturer guidelines and confirms the device meets its minimum security requirements.
   * - WP_136
     - Wallet Initialization / Registration, Lifecycle, Security
     - Cryptographic binding verification
     - Wallet Provider successfully verifies the cryptographic binding between the ``hardware_key_tag``, ``hardware_key_pub``, nonce, and the ``client_data_hash`` provided in the key_attestation.
   * - WP_137
     - Wallet Initialization / Registration, Lifecycle, Interoperability
     - Wallet Instance Registration
     - Wallet Provider successfully registers Wallet Instance, storing its ``hardware_key_tag``, ``hardware_key_pub``, and other device information.
   * - WP_138
     - Wallet Initialization / Activation, Lifecycle, Security
     - User account creation
     - Wallet Provider creates a User account associated with Wallet Instance's ``hardware_key_tag``.
   * - WP_139
     - Wallet  Uninstallation, Lifecycle, Security
     - Key/state deletion on uninstallation
     - Wallet Instance uninstalls itself and removes all local keys and application data.
   * - WP_140
     - Wallet Attestation Issuance, Lifecycle, Security
     - Wallet Attestation Request
     - Wallet Instance successfully constructs the Wallet Attestation Request JWT with the required claims: ``integrity_assertion``, ``hardware_signature``, ``nonce``, ``hardware_key_tag``, ``cnf``, and other configuration related parameters.
   * - WP_140a
     - Wallet Attestation Issuance, Lifecycle, Security
     - Hardware key existence check/re-initialization
     - Wallet Instance checks for the existence of Cryptographic Hardware Keys; if they are not found, it triggers the re-initialization process.
   * - WP_140b
     - Wallet Attestation Issuance, Lifecycle, Interoperability
     - Requests nonce for Wallet Attestation Request
     - Wallet Instance successfully requests and receives a fresh nonce from the Wallet Provider’s Nonce Endpoint, before requesting the Wallet Attestation.
   * - WP_140c
     - Wallet Attestation Issuance, Lifecycle, Interoperability
     - Computes hash for Wallet Attestation Request
     - Wallet Instance computes a SHA-256 digest (``client_data_hash``) of the nonce and the thumbprint of the ``ephemeral_key_pub`` JWK.
   * - WP_140d
     - Wallet Attestation Issuance, Lifecycle, Interoperability
     - Signs hash with hardware private key
     - Wallet Instance signs the ``client_data_hash`` with the hardware private key and produces a valid ``hardware_signature``.
   * - WP_140e
     - Wallet Attestation Issuance, Lifecycle, Interoperability
     - Obtains signed Integrity Assertion from Device Integrity Service.
     - Wallet Instance successfully requests and receives a signed ``integrity_assertion`` from the Device Integrity Service that is bound to the ``client_data_hash``.
   * - WP_140f
     - Wallet Attestation Issuance, Lifecycle, Security
     - Include ``cnf`` claim
     - The ``cnf`` claim contains the ephemeral public key, linking the key to the attestation.
   * - WP_141
     - Wallet Attestation Issuance, Lifecycle, Security
     - Signing JWT Wallet Attestation Request
     - Wallet Instance signs the Wallet Attestation Request JWT with the ephemeral private key.
   * - WP_142
     - Wallet Attestation Issuance, Lifecycle, Security
     - Submitting Wallet Attestation Request JWT to Wallet Provider
     - The Wallet Instance submits the signed request JWT as an ``assertion`` parameter to the Wallet Provider’s Attestation Issuance Endpoint.
   * - WP_143
     - Wallet Attestation Issuance, Lifecycle, Security
     - Attestation Request JWT verification
     - Wallet Provider successfully performs a comprehensive validation of the Wallet Attestation Request JWT, including its signature, claims, and cryptographic proofs.
   * - WP_143a
     - Wallet Attestation Issuance, Lifecycle, Security
     - HTTP header validation for Wallet Attestation Request
     - Wallet Provider successfully validates the Wallet Attestation Request JWT header to contain valid ``alg``, ``kid``, and ``typ`` parameters.
   * - WP_143b
     - Wallet Attestation Issuance, Lifecycle, Security
     - JWT signature verification in Wallet Attestation Request
     - Wallet Provider successfully verifies the signature of the Wallet Attestation Request JWT using the public key in the provided JWK.
   * - WP_143c
     - Wallet Attestation Issuance, Lifecycle, Security
     - Nonce uniqueness verification for Wallet Attestation
     - Wallet Provider rejects the Wallet Attestation Request JWT if the nonce was not generated by itself or has been previously used.
   * - WP_143d
     - Wallet Attestation Issuance, Lifecycle, Security
     - Registered Wallet Instance verification
     - Wallet Provider confirms that the Wallet Attestation Request originates from a valid and currently registered Wallet Instance; if not rejects the request.
   * - WP_143e
     - Wallet Attestation Issuance, Lifecycle, Interoperability
     - Hardware signature validation
     - Wallet Provider successfully reconstructs the client_data, and validates the ``hardware_signature`` using Wallet Instance's registered Hardware public key.
   * - WP_143f
     - Wallet Attestation Issuance, Lifecycle, Security
     - Integrity Assertion validation per guidelines
     - Wallet Provider successfully validates the ``integrity_assertion`` according to the device manufacturer’s guidelines.
   * - WP_143g
     - Wallet Attestation Issuance, Lifecycle, Security
     - ``iss`` parameter verification
     - Wallet Provider verifies that the ``iss`` parameter in the Wallet Attestation Request JWT matches its own URL identifier.
   * - WP_144
     - Wallet Attestation Issuance, Lifecycle, Security
     - Attestation Issuance
     - After successful validation of the Wallet Attestation Request, Wallet Provider issues a Wallet Attestation with an expiration time not exceeding 24 hours from issuance.
   * - WP_145
     - Wallet Revocation, Lifecycle, Interoperability
     - Wallet Instance status retrieval
     - Wallet Instance sends a Wallet Instances Retrieval Request to the Wallet Provider’s Wallet Instance Management Endpoint.
   * - WP_146
     - Wallet Revocation, Lifecycle, Interoperability
     - Wallet Instance status response
     - Wallet Provider validates the request and returns Wallet Instance a list of the authenticated User’s linked Wallet Instances, including each instance’s ``ID``, ``status``, and ``issued_at`` fields.
   * - WP_147
     - Wallet Revocation, Lifecycle, Interoperability
     - Wallet Instance Revocation Request body
     - Wallet Instance Revocation Request includes a body with ``{"status":"REVOKED"}``.
   * - WP_148
     - Wallet Revocation, Lifecycle, Interoperability
     - Wallet Instance Revocation Response
     - Wallet Provider updates the specified Wallet Instance state to ``REVOKED`` and returns a confirmation.
   * - WP_149
     - Wallet Revocation, Lifecycle, Security
     - Clears keys upon revocation
     - As part of its revocation, Wallet Instance removes all associated Wallet Cryptographic Hardware Key pairs from the device.
   * - WP_150
     - Wallet Initialization / Registration, Lifecycle, Interoperability
     - Initialization failure (invalid nonce)
     - When a Wallet Instance Initialization request contains a nonce that is invalid, expired, or already used, Wallet Provider returns a ``403 Forbidden`` response with the error code ``invalid_request``.
   * - WP_151
     - Wallet Initialization / Registration, Lifecycle, Interoperability
     - Initialization failure (Key Attestation signature)
     - When a Wallet Instance Initialization request contains an invalid Key Attestation signature, Wallet Provider returns a ``403 Forbidden`` response with the error code ``invalid_request``.
   * - WP_152
     - Wallet Initialization / Registration, Lifecycle, Interoperability
     - Key Binding failure (Wallet Instance not found)
     - When a Key Binding request references a Wallet Instance that is not found, Wallet Provider returns a ``404 Not Found`` response with the error code ``not_found``.
   * - WP_153
     - Wallet Initialization / Registration, Lifecycle, Interoperability
     - Key Binding failure (Wallet Instance revoked)
     - When a Key Binding request is made for a Wallet Instance that has been revoked, Wallet Provider returns a ``403 Forbidden`` response with the error code ``invalid_request``.
   * - WP_154
     - Wallet Initialization / Registration, Lifecycle, Interoperability
     - Key Binding failure (invalid PoP)
     - When a Key Binding request contains an invalid Proof of Possession (``hardware_signature``), Wallet Provider returns a ``403 Forbidden`` response with the error code ``invalid_request``.
   * - WP_155
     - Wallet Initialization / Registration, Lifecycle, Interoperability
     - Key Binding failure (Integrity Assertion failure)
     - When the Integrity Assertion in a Key Binding request fails validation (e.g., is tampered with), Wallet Provider returns a ``403 Forbidden`` response with the error code ``invalid_request``.


