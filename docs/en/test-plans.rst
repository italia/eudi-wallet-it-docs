.. include:: ../common/common_definitions.rst
.. Included via appendix.rst at title level '=' (document title).


Test Plans
==========

The purpose of the test plans is to support implementers, auditors, and conformance test environments in validating the behavior of the Wallet Solutions, Relying Parties and Credential Issuers under various operational and security scenarios.

All test cases are derived from normative rules defined in the above specifications, with no assumptions or extensions.

.. note::
  Please note that the test plans matrix may be subject to future changes.

Structure of the Test Matrix
-----------------------------

Each test case is identified by a unique test ID (e.g., WS-001) and categorized using the functional domains defined below. Other category identifiers can be used as well.

- **Discovery**
- **Security**
- **Privacy**
- **Authorization**
- **Authentication**
- **User Experience**
- **Credential Issuance**
- **Credential Presentation**
- **Credential Status**
- **Backup & Restore**

For each test case, the table specifies:

- **Test Case ID**: a unique identifier.
- **Purpose**: the functional area covered by the test.
- **Description**: the requirement being tested, always based on a normative MUST from the specification.
- **Expected Result**: the expected outcome when the solution is implemented correctly.


.. toctree::
  :caption: Test Plans by Context
  :maxdepth: 3

  test-plans-signature.rst
  test-plans-trust.rst
  test-plans-federation-authority.rst
  test-plans-wallet-provider.rst
  test-plans-credential-issuer.rst
  test-plans-presentation.rst


