.. include:: ../common/common_definitions.rst
.. Included via credential-issuer-solution.rst at title level '-' (level 1).


Credential Issuer Entity Configuration
--------------------------------------

The Credential Issuers, as Federation Entity, MUST adhere to the guidelines outlined in Section :ref:`infrastructure-trust:Entity Configuration`. Specifically, they MUST provide a *well-known* endpoint that hosts their Entity Configuration.
The Entity Configuration of Credential Issuers MUST contain the parameters defined in the Sections :ref:`infrastructure-trust:Entity Configuration of a Leaf` and :ref:`infrastructure-trust:Entity Statement Parameters`.

The Credential Issuers MUST provide, at least, the following metadata types:

- `federation_entity`
- `oauth_authorization_server`
- `openid_credential_issuer`

In cases where the (Q)EAA Providers authenticate Users using their Wallet Instance, then the metadata for *openid_credential_verifier* MUST be provided in addition to the metadata above. In case a national eID scheme is used by the Credential Issuers for the User authentication, they MAY include a metadata for *openid_relying_party* within their Entity Configuration. The *openid_relying_party* metadata MUST be compliant with the Technical Specification `SPID/CIE-OpenID-Connect-Specifications`_.


The *federation_entity* metadata MUST contain the parameters as defined in Section :ref:`infrastructure-trust:Entity Type Identifiers and Metadata`.

The *oauth_authorization_server* metadata MUST contain the parameters as defined in Section :ref:`credential-issuer-metadata:Metadata for oauth_authorization_server`.

The *openid_credential_issuer* metadata MUST contain the parameters as defined in Section :ref:`credential-issuer-metadata:Metadata for openid_credential_issuer`.

The *openid_credential_verifier* metadata MUST contain the parameters as defined in Section :ref:`relying-party-entity-configuration:Relying Party Entity Configuration`.

Example of a (Q)EAA Provider Entity Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below is a non-normative example of an Entity Configuration of a (Q)EAA Provider containing a metadata for

- `federation_entity`
- `oauth_authorization_server`
- `openid_credential_issuer`
- `openid_credential_verifier`

.. literalinclude:: ../../examples/ec-eaa.json
  :language: JSON


