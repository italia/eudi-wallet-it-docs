.. include:: ../common/common_definitions.rst
.. Included via relying-party-solution.rst at title level '-' (level 1).


Relying Party Entity Configuration
------------------------------------------

According to Section :ref:`infrastructure-trust:Entity Configuration`, as a Federation Entity, the Relying Party is required to maintain a well-known endpoint that hosts its Entity Configuration.
The Entity Configuration of Relying Parties MUST contain the parameters defined in the Sections :ref:`infrastructure-trust:Entity Configuration of a Leaf` and :ref:`infrastructure-trust:Entity Statement Parameters`.

The Relying Parties MUST provide the following metadata types:

  - `federation_entity`
  - `openid_credential_verifier`

The *federation_entity* metadata MUST contain the claims as defined in Section :ref:`infrastructure-trust:Entity Type Identifiers and Metadata`.


Example of a Relying Party Entity Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below a non-normative example of the request made by the Wallet Instance to the *openid-federation* well-known endpoint to obtain the Relying Party Entity Configuration:

.. code-block:: http

  GET /.well-known/openid-federation HTTP/1.1
  HOST: relying-party.example.org


Below is a non-normative response example:

.. literalinclude:: ../../examples/ec-rp.json
  :language: JSON


