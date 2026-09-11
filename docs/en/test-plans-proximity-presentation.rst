.. include:: ../common/common_definitions.rst
.. Included via test-plans-presentation.rst at title level '^' (level 2).


Proximity Credential Verifier Test Matrix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section provides the set of test cases designed for technical implementers and development teams responsible for creating and deploying Credential Verifiers solutions for proximity flows. It is also intended for assessment bodies inspecting and validating the implementations of Credential Verifiers solutions for proximity flows.

.. note::
  Further references about official ISO-18013-5 test plans, if available, will update this section in future releases.


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - **Test Case ID**
    - **Purpose**
    - **Description**
    - **Expected Result**

  * - PPR-001
    - Device Engagement
    - Test the initiation of device engagement using QR code.
    - Device engagement is successfully initiated and QR code is scanned.

  * - PPR-002
    - Session Establishment
    - Verify session establishment with correct session keys.
    - Session is established securely with correct session keys.

  * - PPR-003
    - Communication
    - Test the transmission of mdoc request over BLE.
    - mdoc request is transmitted securely over BLE.

  * - PPR-004
    - User Authentication
    - Validate user authentication via WSCA.
    - User is authenticated successfully using WSCA.

  * - PPR-005
    - Attribute Consent
    - Check user consent for attribute release.
    - User consents to release requested attributes.

  * - PPR-006
    - Data Retrieval
    - Test retrieval of mdoc Digital Credentials.
    - mdoc Digital Credentials are retrieved successfully.

  * - PPR-007
    - Session Termination
    - Verify session termination after data exchange.
    - Session is terminated and keys are destroyed.

  * - PPR-008
    - Error Handling
    - Test handling of invalid session keys.
    - Appropriate error message is displayed for invalid keys.

  * - PPR-009
    - BLE Connection
    - Test BLE connection stability during data exchange.
    - BLE connection remains stable throughout the exchange.

  * - PPR-010
    - Document Verification
    - Verify the integrity of received documents.
    - Documents are verified and integrity is confirmed.

  * - PPR-011
    - Security
    - Test encryption of mdoc requests and responses.
    - All mdoc requests and responses are encrypted correctly.

  * - PPR-012
    - User Interface
    - Check the user interface for attribute consent.
    - User interface displays attribute consent request clearly.

  * - PPR-013
    - Error Handling
    - Test response to unsupported document types.
    - System returns appropriate error for unsupported document types.

  * - PPR-014
    - Performance
    - Measure time taken for session establishment.
    - Session is established within acceptable time limits.

  * - PPR-015
    - Compatibility
    - Verify compatibility with different mobile devices.
    - System works seamlessly across various mobile devices.

  * - PPR-016
    - Data Integrity
    - Test integrity of data during transmission.
    - Data integrity is maintained during transmission.

  * - PPR-017
    - Session Management
    - Test session management under high load.
    - Sessions are managed effectively under high load conditions.

  * - PPR-018
    - BLE Connection
    - Test reconnection after BLE disconnection.
    - System reconnects successfully after BLE disconnection.

  * - PPR-019
    - User Experience
    - Evaluate user experience during the proximity flow.
    - Users report a positive experience with the proximity flow.

  * - PPR-020
    - Security
    - Test resistance to replay attacks.
    - System is resistant to replay attacks.

  * - PPR-021
    - Device Engagement
    - Verify that Device Engagement structure is CBOR encoded.
    - Device Engagement structure is correctly encoded in CBOR format.

  * - PPR-022
    - Device Engagement
    - Test that ephemeral public key is of type allowed by selected cipher suite.
    - Ephemeral public key meets the requirements of the selected cipher suite.

  * - PPR-023
    - BLE Configuration
    - Verify that only Central Client mode is supported.
    - Only Central Client mode is supported for BLE connections.

  * - PPR-024
    - Capabilities
    - Test that ``HandoverSessionEstablishmentSupport`` is set to ``true`` when present.
    - ``HandoverSessionEstablishmentSupport`` is correctly set to ``true``.

  * - PPR-025
    - Capabilities
    - Verify that ``ReaderAuthAllSupport`` is set to ``true`` when present.
    - ``ReaderAuthAllSupport`` is correctly set to ``true``.

  * - PPR-026
    - mdoc Request
    - Test that mdoc Request messages are CBOR encoded.
    - mdoc Request messages are correctly encoded in CBOR format.

  * - PPR-027
    - mdoc Request
    - Verify that mdoc request is encrypted with session key.
    - mdoc request is correctly encrypted with session key.

  * - PPR-028
    - mdoc Request
    - Test that mdoc request is transmitted via BLE protocol.
    - mdoc request is correctly transmitted via BLE protocol.

  * - PPR-029
    - mdoc Response
    - Verify that mdoc Response messages are CBOR encoded.
    - mdoc Response messages are correctly encoded in CBOR format.

  * - PPR-030
    - mdoc Response
    - Test that mdoc response is encrypted with session key.
    - mdoc response is correctly encrypted with session key.

  * - PPR-031
    - Key Management
    - Test that private ephemeral key is kept secret.
    - Private ephemeral key is properly secured and not exposed.

  * - PPR-032
    - Key Management
    - Test that public ephemeral key is used in session establishment.
    - Public ephemeral key is correctly used for session establishment.

  * - PPR-033
    - Session Key Derivation
    - Test that session keys are derived using key agreement protocol.
    - Session keys are correctly derived using the key agreement protocol.

  * - PPR-034
    - Session Establishment
    - Test that ``SessionEstablishment`` message is prepared correctly.
    - ``SessionEstablishment`` message is properly prepared with required components.

  * - PPR-035
    - Session Establishment
    - Test that ``SessionEstablishment`` message is signed by RP Instance.
    - ``SessionEstablishment`` message is correctly signed by Relying Party Instance.

  * - PPR-036
    - Session Establishment
    - Test that ``SessionEstablishment`` message is encrypted with session keys.
    - ``SessionEstablishment`` message is properly encrypted with session keys.

  * - PPR-037
    - Session Establishment
    - Test that ``SessionEstablishment`` includes ``EReaderKey.Pub`` and attribute request.
    - ``SessionEstablishment`` message includes required ``EReaderKey.Pub`` and attribute request.

  * - PPR-038
    - Message Transmission
    - Test that ``SessionEstablishment`` is transmitted over secure BLE connection.
    - ``SessionEstablishment`` message is transmitted over secure BLE connection.

  * - PPR-039
    - Session Key Computation
    - Test that Relying Party correctly handles Wallet Instance session key computation.
    - Wallet Instance correctly computes session key.

  * - PPR-040
    - Message Decryption
    - Test that Relying Party correctly handles Wallet Instance decrypting ``SessionEstablishment`` message.
    - Wallet Instance successfully decrypts ``SessionEstablishment`` message.

  * - PPR-041
    - Signature Verification
    - Test that Relying Party correctly handles Wallet Instance verifying RP Instance signature.
    - Wallet Instance correctly verifies Relying Party Instance signature.

  * - PPR-042
    - Attribute Request Processing
    - Test that Relying Party correctly handles Wallet Instance decrypting attribute request.
    - Wallet Instance successfully decrypts attribute request.

  * - PPR-043
    - User Consent
    - Test that Relying Party correctly handles Wallet Instance prompting user for consent.
    - Wallet Instance correctly prompts user for consent to release attributes.

  * - PPR-044
    - Certificate Display
    - Test that Relying Party correctly handles Wallet Instance displaying RP Registration Certificate.
    - Wallet Instance displays Relying Party Registration Certificate for transparency.

  * - PPR-045
    - Credential Retrieval
    - Test that Relying Party correctly handles Wallet Instance retrieving requested mdoc Digital Credentials.
    - Wallet Instance successfully retrieves requested mdoc Digital Credentials.

  * - PPR-046
    - SessionData Preparation
    - Test that Relying Party correctly handles Wallet Instance preparing ``SessionData`` message.
    - Wallet Instance correctly prepares ``SessionData`` message with Digital Credentials.

  * - PPR-047
    - Authentication Data Signing
    - Test that Relying Party correctly handles Wallet Instance signing required authentication data.
    - Wallet Instance correctly signs required authentication data.

  * - PPR-048
    - Message Encryption
    - Test that ``SessionData`` is encrypted with session keys.
    - ``SessionData`` message is properly encrypted with session keys.

  * - PPR-049
    - CBOR Encoding
    - Test that mdoc response is encoded in CBOR format.
    - mdoc response is correctly encoded in CBOR format.

  * - PPR-050
    - Data Verification
    - Test that RP Instance decrypts ``SessionData``.
    - Relying Party Instance successfully decrypts ``SessionData``.

  * - PPR-051
    - Signature Verification
    - Test that RP Instance verifies Wallet Instance signature.
    - Relying Party Instance correctly verifies Wallet Instance signature.

  * - PPR-052
    - Document Validation
    - Test that RP Instance checks mdoc validity and Issuer signature.
    - Relying Party Instance correctly validates mdoc and Issuer signature.

  * - PPR-053
    - BLE Disconnection
    - Test that GATT Client unsubscribes from characteristics.
    - GATT Client properly unsubscribes from characteristics.

  * - PPR-054
    - BLE Disconnection
    - Test that GATT Client disconnects from GATT server.
    - GATT Client properly disconnects from GATT server.

  * - PPR-055
    - Request Structure Compliance
    - Test that mdoc Request is compliant with required structure.
    - mdoc Request complies with required structure and includes necessary components.

  * - PPR-056
    - Response Structure Compliance
    - Test that mdoc Response is compliant with required structure.
    - mdoc Response complies with required structure and includes necessary components.

  * - PPR-057
    - Document Structure Compliance
    - Test that documents are compliant with required structure.
    - Documents comply with required structure and include necessary components.

  * - PPR-058
    - Document Type Validation
    - Test that mDL document type is correctly set.
    - mDL document type is correctly set to ``org.iso.18013.5.1.mDL``.

  * - PPR-059
    - DeviceSigned Structure
    - Test that deviceSigned structure is compliant.
    - deviceSigned structure complies with required format and includes necessary components.

  * - PPR-060
    - Device Authentication
    - Test that ``deviceAuth`` includes ``deviceSignature``.
    - ``deviceAuth`` structure includes required ``deviceSignature`` for authentication.

  * - PPR-061
    - Wallet Attestation Inclusion
    - Test that Relying Party correctly handles Wallet Instance including Wallet Attestation when requested.
    - Wallet Instance includes Wallet Attestation when requested by Relying Party.

  * - PPR-062
    - AAL Claim Inclusion
    - Test that Relying Party correctly handles Wallet Instance including ``aal`` claim in Wallet Attestation.
    - Wallet Instance includes ``aal`` claim as disclosure in Wallet Attestation.

  * - PPR-063
    - User Consent Bypass
    - Test that Relying Party correctly handles Wallet Instance not requesting user consent for Wallet Attestation.
    - Wallet Instance does not request user consent for technical Wallet Attestation attributes.

  * - PPR-064
    - Session Termination Conditions
    - Test that session is terminated under specified conditions.
    - Session is properly terminated when specified conditions occur.

  * - PPR-065
    - Session Termination Initiation
    - Test that session termination is initiated correctly.
    - Session termination is properly initiated when no further requests are sent.

  * - PPR-066
    - Key Destruction
    - Test that session keys are destroyed on termination.
    - Session keys and ephemeral key material are properly destroyed.

  * - PPR-067
    - Channel Closure
    - Test that communication channel is closed on termination.
    - Communication channel used for data retrieval is properly closed.


