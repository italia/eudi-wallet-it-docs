.. include:: ../common/common_definitions.rst
.. Included via wallet-solution.rst at title level '-' (level 1).


Wallet Provider Entity Configuration
--------------------------------------

An HTTP GET request to the Federation endpoint allows the retrieval of the Wallet Provider Entity Configuration (:ref:`WP_001 <wallet-provider-backend-testcases>`).

The returned Entity Configuration of the Wallet Provider MUST contain the attributes described in the sections below.

The Wallet Provider Entity Configuration is a signed JWT containing the public keys and supported algorithms of the Wallet Solution as a component of the Wallet Provider. It is structured in accordance with the `OID-FED`_ and :ref:`infrastructure-trust:Infrastructure of Trust` outlined in this specification (:ref:`WP_002 <wallet-provider-backend-testcases>`).


Wallet Provider Entity Configuration JWT Header
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :class: longtable
    :widths: 30 70
    :header-rows: 1

    * - **Key**
      - **Value**
    * - alg
      - Algorithm used to verify the token signature. It MUST be one of the possible values indicated in :ref:`algorithms:Cryptographic Algorithms` (e.g., ES256).
    * - kid
      - Thumbprint of the public key used for the signature.
    * - typ
      - Media type, set to ``entity-statement+jwt``.

Wallet Provider Entity Configuration JWT Payload
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :class: longtable
    :widths: 30 70
    :header-rows: 1

    * - **Key**
      - **Value**
    * - ``iss``
      - REQUIRED. Public URL of the Wallet Solution.
    * - ``sub``
      - REQUIRED. Public URL of the Wallet Solution.
    * - ``iat``
      - REQUIRED. Issuance datetime in Unix Timestamp format.
    * - ``exp``
      - REQUIRED. Expiration datetime in Unix Timestamp format.
    * - ``authority_hints``
      - REQUIRED. Array of URLs (String) containing the list of URLs of the immediate superior Entities, such as the Trust Anchor or an Intermediate, that MAY issue an Entity Statement related to the Wallet Solution.
    * - ``jwks``
      - REQUIRED. A JSON Web Key Set (JWKS) representing the public part of the Federation Entity signing keys. The corresponding private key is used by the Wallet Solution to sign the Entity Configuration about itself.
    * - ``metadata``
      - REQUIRED.JSON object that represents the Entity's Types and the metadata for those Entity Types. Each member name of the JSON object is an Entity Type Identifier, and each value MUST be a JSON object containing metadata parameters according to the metadata schema of the Entity Type. It MUST contain the ``wallet_solution`` and the ``federation_entity`` metadata.


.. note::
    Tests covering the Entity Configuration structure (header and payload) are provided in :ref:`WP_002a–002h <wallet-provider-backend-testcases>`.


Example of a Wallet Provider Entity Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below is a non-normative example of a payload of a Wallet Provider Entity Configuration containing a metadata for

- `federation_entity`
- `wallet_solution`

.. literalinclude:: ../../examples/ec-wp.json
  :language: JSON


