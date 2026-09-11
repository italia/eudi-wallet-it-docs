.. include:: ../common/common_definitions.rst
.. Included via test-plans.rst at title level '-' (level 1).


Signature Evaluation Test Matrix
------------------------------------------

This section provides the common set of test cases for Wallet Solutions, Relying Parties and Credential Issuers evaluating any signed statements, be these assertions, requests, attestation or Credentials.


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - **Test Case ID**
    - **Purpose**
    - **Description**
    - **Expected Result**
  * - ATT-001
    - Discovery, Security
    - Evaluation of the issuer
    - Entities evaluating signed statements establish trust with the issuer and assess its compliance. Undiscoverable Issuers within the federation or unlinkable to any known Trust Anchor, halt any protocol communications.
  * - ATT-002
    - Discovery, Security
    - Evaluation of the signature
    - Entities evaluate signed statements by verifying the signature with the issuer's cryptographic material, provided it is trusted through a well-known Trust Anchor. Any untrusted cryptographic material or invalid signatures halt protocol communications.
  * - ATT-003
    - Algorithm Verification
    - Verify that the algorithm specified in the header matches the one used for cryptographic operations.
    - The algorithm in the header must match the cryptographic operation.
  * - ATT-004
    - Appropriate Algorithms
    - Ensure only cryptographically current algorithms are used.
    - Only approved algorithms are accepted; deprecated ones are rejected.
  * - ATT-005
    - Signature Validation
    - Validate all cryptographic operations and reject if any fail.
    - All signatures must be valid; any failure results in rejection.
  * - ATT-006
    - Key Entropy
    - Ensure cryptographic keys have sufficient entropy.
    - Keys must meet entropy requirements; weak keys are rejected.
  * - ATT-007
    - Issuer Validation
    - Validate that the cryptographic keys belong to the issuer.
    - Keys must be verified as belonging to the issuer.
  * - ATT-008
    - Audience Validation
    - Validate the audience claim to ensure the token is used by the intended party.
    - Audience claim must match the intended recipient.
  * - ATT-009
    - Claim Trust
    - Do not trust received claims without validation.
    - Claims must be validated; untrusted claims are rejected.
  * - ATT-010
    - Explicit Typing
    - Use explicit typing to prevent COSE/JOSE confusion.
    - Typing must be explicit and validated.
  * - ATT-011
    - Cross-JWT Confusion
    - Prevent COSE/JOSE from being used in unintended contexts.
    - COSE/JOSE must be contextually validated to prevent misuse.
  * - ATT-012
    - Substitution Attacks
    - Ensure COSE/JOSE are not substituted across different contexts.
    - COSE/JOSE must be validated for context-specific use.
  * - ATT-013
    - Issued At Validation
    - Verify that the `issued at` parameter is set to the current time, allowing a grace period not exceeding 120 seconds.
    - The `issued at` value must be within 120 seconds of the current time.
  * - ATT-014
    - Expiration Validation
    - Ensure the `expiration` time is greater than the `issued at` time.
    - The `expiration` time must be later than the `issued at` time.
  * - ATT-015
    - Data Model validation
    - Ensure JOSE/COSE type matches with the defined data model.
    - The parameters or claims, their values and the schema used to represent them are compliant with the data model.


