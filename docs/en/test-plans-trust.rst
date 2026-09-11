.. include:: ../common/common_definitions.rst
.. Included via test-plans.rst at title level '-' (level 1).


Trust Evaluation Test Matrix
-----------------------------

This section provides the common set of test cases for Wallet Solutions, Relying Parties and Credential Issuers.


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - **Test Case ID**
    - **Purpose**
    - **Description**
    - **Expected Result**
  * - ALL-001
    - Security
    - Obtaining Trust Anchors public cryptographic materials
    - Entities obtain the list of Trust Anchors or Certificate Authorities and their public cryptographic key materials, periodically ensuring that these are not expired, revoked or updated. Infrastructure of Trust provides these information through web endpoints and other out of band mechanisms, to facilitate comparison of the provided information to all the entities.
  * - ALL-002
    - Security
    - Compliance self evaluation
    - Entities periodically evaluate their compliance and presence within the federation, checking the trust chain about themselves as still valid, not revoked and compliant with the technical specification. Entities apply the policies, checking that their current configuration is valid with the active policies about them within the federation. Trust chain, evaluated and stored in multiple formats to facilitate interoperability in trust discovery with other entities, are stored by entities and used on occurrence during the data exchange flows. Trust chain about entities are fetched or discovered using the entities' issued assertions.
  * - ALL-003
    - Discovery
    - Publication of information about itself
    - Entities sign and publish all the information about them, containing all the protocol metadata, cryptographic material, trust marks, using the well-known endpoint defined in this specification, making these information publicly discoverable by other entities.
  * - ALL-004
    - Security
    - Publication of the historical key registry
    - Entities sign and publish all the information about the unused or revoked cryptographic material using well known endpoints defined in this specification, making this information publicly discoverable by other entities.
  * - ALL-005
    - Security
    - Evaluation of compliance with entities before exchanging data about the User
    - Entities evaluate trust and compliance with other entities before any information related to a natural or legal person might be exchanged. Bogus configurations don't allow data exchanges.
  * - ALL-006
    - Security
    - Evaluation of proof of possession during the use of a signed assertion according to the configured usage ownership confirmation method.
    - Entities evaluate the confirmation method and apply its protocol to consider valid the signed statement.
  * - ALL-007
    - Security
    - Supported cryptography algorithms
    - Entities evaluate cryptographic usage for compliance with the allowed algorithms.
  * - ALL-008
    - Security
    - Replay attacks
    - Signed statements using unique identifiers are stored until their expiration time and checked against any replay of them.


