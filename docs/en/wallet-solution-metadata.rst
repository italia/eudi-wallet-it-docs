.. include:: ../common/common_definitions.rst
.. Included via wallet-solution.rst at title level '-' (level 1).


Wallet Solution Metadata
------------------------

The metadata JSON Object whose key is ``wallet_solution`` contains the following parameters. The public keys found in this object are exclusively used for signing and/or encryption operations required by this Entity when acting as a component of the Wallet Provider (e.g., sign the Wallet Attestations to the Wallet Instance).

.. list-table::
    :class: longtable
    :widths: 30 70
    :header-rows: 1

    * - **Key**
      - **Value**
    * - ``jwks``
      - CONDITIONAL. JSON Web Key Set document, passed by value, containing the Entity's keys for that Entity Type. It MUST be present if ``jwks_uri`` and ``signed_jwks_uri`` are absent.
    * - ``jwks_uri``
      - CONDITIONAL. URL referencing a JWK Set document containing the Wallet Solution's keys for that Entity Type. This URL MUST use the https scheme. It MUST be present if ``jwks`` and ``signed_jwks_uri`` are absent.
    * - ``signed_jwks_uri``
      - CONDITIONAL. URL referencing a signed JWT having the Entity's JWK Set document for that Entity Type as its payload. This URL MUST use the https scheme. The JWT MUST be signed using a Federation Entity Key. A successful response from the URL MUST use the HTTP status code 200 with the Content Type ``application/jwk-set+jwt``. It MUST be present if ``jwks`` and ``jwks_uri`` are absent.
    * - ``logo_uri``
      - REQUIRED. URL of the entity's logo that will be shown to the User. The logo mime type MUST be ``application/svg``.
    * - ``wallet_name``
      - REQUIRED. String containing a human-readable name of the Wallet.
    * - ``authorization_endpoint``
      - REQUIRED. URL of the authorization server's endpoint, see `OAUTH2`_. Using a universal link is preferable for enhanced security and fallback support; custom URL schemes can also be used if necessary.
    * - ``credential_offer_endpoint``
      - REQUIRED. Credential Offer Endpoint of a Wallet.
    * - ``response_types_supported``
      - OPTIONAL. JSON array of OAuth 2.0 ``response_type`` values. If present it MUST be set to ``vp_token`` (:ref:`RPR-82 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).
    * - ``response_modes_supported``
      - OPTIONAL. JSON array of OAuth 2.0 "response_mode" values as specified in `OAUTH-MULT-RESP-TYPE`_. The supported value MUST be *query*.
    * - ``vp_formats_supported``
      - REQUIRED. Object containing a list of name/value pairs, where the name is a Credential Format Identifier and the value defines format-specific parameters that a Wallet supports. See `OpenID4VP`_ Appendix B. Wallet Instances MUST support the Credential Format Identifiers required by `OPENID4VC-HAIP`_ (including ``dc+sd-jwt`` and ``mso_mdoc``).
    * - ``client_id_prefixes_supported``
      - RECOMMENDED. A non-empty array of the Client Identifier Prefixes that the Wallet Instance supports.  Valid values include ``openid_federation`` and ``x509_hash``; if omitted, the default is ``pre-registered``.
    * - ``request_object_signing_alg_values_supported``
      - OPTIONAL. See OpenID Connect Discovery.


.. note::
  There are Digital Credential flows that require retrieving Wallet Solution metadata before interacting with the Wallet itself. The flow is described in :ref:`wallet-metadata-retrieval:Wallet Metadata Retrieval Flow`.

.. note::
  For the ``authorization_endpoint``, the use of universal links is preferred over custom URL schemes because, when properly configured using Assetlinks JSON for Android and Apple App Site Association for iOS, they provide enhanced security by reducing the risk of URL hijacking.
  Furthermore, universal links offer fallback mechanisms, allowing the flow to continue seamlessly in a browser even if the Wallet Instance is not installed, ensuring a smoother User experience. To ensure interoperability, support for custom URL schemes is also RECOMMENDED according to HAIP `OPENID4VC-HAIP`_, and in particular the custom URL ``haip://``.

