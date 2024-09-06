.. include:: ../common/common_definitions.rst
.. _Entity_Configuration_Credential_Issuer:

Entity Configuration of PID/(Q)EAA Providers
--------------------------------------------

The PID/(Q)EAA Providers, as Federation Entity, are required to adhere to the guidelines outlined in Section :ref:`Configuration of the Federation`. Specifically, they MUST provide a well-known endpoint that hosts their Entity Configuration.
The Entity Configuration of PID/(Q)EAA Providers MUST contain the parameters defined in the Sections :ref:`Entity Configuration Leaves and Intermediates` and :ref:`Entity Configurations Common Parameters`. 

The PID/(Q)EAA Providers MUST provide the following metadata types:

  - `federation_entity`
  - `oauth_authorization_server`
  - `openid_credential_issuer`

In cases where the (Q)EAA Providers authenticate Users using their Wallet Instance, then the metadata for *wallet_relying_party* MUST be provided in addition to the metadata above. In case a national eID scheme is used by the PID/(Q)EAA Providers for the User authentication, they MAY include a metadata for *openid_relying_party* within their Entity Configuration. The *openid_relying_party* metadata MUST be compliant with the current version of `SPID/CIE id OIDC Technical Specification <https://github.com/italia/spid-cie-oidc-docs>`_.


Metadata for federation_entity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *federation_entity* metadata MUST contain the parameters as defined in Section :ref:`Metadata of federation_entity Leaves`.


Metadata for oauth_authorization_server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *oauth_authorization_server* metadata MUST contain the following parameters.

.. list-table:: 
  :widths: 20 60
  :header-rows: 1

  * - **Claim**
    - **Description**
  * - **issuer**
    - It MUST contain an HTTPS URL that uniquely identifies the PID/(Q)EAA Provider.
  * - **pushed_authorization_request_endpoint**
    - The URL of the pushed authorization request endpoint is where a Wallet Instance MUST submit an authorization request to obtain a *request_uri* value, which can then be used at the authorization endpoint. See :rfc:`9126#as_metadata`.
  * - **authorization_endpoint**
    - URL of the authorization server's authorization endpoint. See :rfc:`8414#section-2`.
  * - **token_endpoint**
    - URL of the authorization server's token endpoint. See :rfc:`8414#section-2`.
  * - **client_registration_types_supported**
    - Array specifying the registration types supported. The authorization server MUST support *automatic*. See  `OID-FED`_ Section 5.1.3.
  * - **code_challenge_methods_supported**
    - JSON array containing a list of Proof Key for Code Exchange (PKCE) :rfc:`7636` code challenge methods supported by the authorization server. The authorization server MUST support *S256*.
  * - **acr_values_supported**
    - See `OpenID Connect Discovery 1.0 Section 3 <https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata>`_. The supported values are:
      
      - `https://www.spid.gov.it/SpidL1`
      - `https://www.spid.gov.it/SpidL2`
      - `https://www.spid.gov.it/SpidL3`
  * - **scopes_supported**
    - JSON array containing a list of the supported *scope* values. See :rfc:`8414#section-2`.
  * - **response_modes_supported**
    - JSON array containing a list of the supported "response_mode" values, as specified in `OAuth 2.0 Multiple Response Type Encoding Practices <https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html>`_. The supported values MAY be *query* and *form_post.jwt* (see `[oauth-v2-jarm-03] <https://openid.net/specs/oauth-v2-jarm-03.html#name-response-mode-form_postjwt>`__).
  * - **authorization_signing_alg_values_supported**
    - JSON array containing a list of the JWS :rfc:`7515` supported signing algorithms (*alg* values). The values MUST be set according to Section :ref:`Cryptographic algorithms`. See Section 4 of `[oauth-v2-jarm-03] <https://openid.net/specs/oauth-v2-jarm-03.html>`__.
  * - **grant_types_supported**
    - JSON array containing a list of the supported grant type values. The authorization server MUST support *authorization_code*. 
  * - **token_endpoint_auth_methods_supported**
    - JSON array containing a list of supported client authentication methods. The Token Endpoint MUST support *attest_jwt_client_auth* as defined in `OAUTH-ATTESTATION-CLIENT-AUTH`_.
  * - **token_endpoint_auth_signing_alg_values_supported**
    - JSON array containing a list of the JWS signing algorithms ("*alg*" values) supported by the token endpoint for the signature on the JWT used to authenticate the client at the Token Endpoint. See :rfc:`8414#section-2`.
  * - **request_object_signing_alg_values_supported**
    - JSON array containing a list of the JWS signing algorithms ("*alg*" values) supported for Request Objects. See `[openid-connect-discovery-1_0] <https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata>`_.
  * - **jwks**
    - JSON Web Key Set containing the cryptographic keys for the authorization server. See `OID-FED`_ Section 5.2.1 and `JWK`_.

Metadata for openid_credential_issuer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *openid_credential_issuer* metadata MUST contain the following claims.

.. list-table:: 
  :widths: 20 60
  :header-rows: 1

  * - **Claim**
    - **Description**
  * - **credential_issuer**
    - The PID/(Q)EAA Provider identifier. It MUST be a case sensitive URL using HTTPS scheme as defined in `OpenID4VCI`_ Sections 11.2.1 and 11.2.3.
  * - **credential_endpoint**
    - URL of the credential endpoint. See `OpenID4VCI`_ Section 11.2.3.
  * - **revocation_endpoint**
    - URL of the revocation endpoint. See :rfc:`8414#section-2`.
  * - **status_attestation_endpoint**
    - It MUST be an HTTPs URL indicating the endpoint where the Wallet Instances can request Status Attestations. See Section :ref:`Credential Lifecycle` for more details.
  * - **notification_endpoint**
    - It MUST be an HTTPs URL indicating the notification endpoint. See Section 11.2.3 of [`OpenID4VCI`_].
  * - **authorization_servers**
    - OPTIONAL. Array of strings, where each string is an identifier of the OAuth 2.0 Authorization Server (as defined in [:rfc:`8414`]) the PID/(Q)EAA Provider relies on for authorization. If this parameter is omitted, the entity providing the PID/(Q)EAA Provider is also acting as the Authorization Server.
  * - **display**
    - See `OpenID4VCI`_ Section 11.2.3. Array of objects containing display language properties. The parameters that MUST be included are:
        
        - **name**: String value of a display name for the PID/(Q)EAA Provider.
        - **locale**: String value that identifies the language of this object represented as a language tag taken from values defined in *BCP47* :rfc:`5646`. There MUST be only one object for each language identifier. 

  * - **credential_configurations_supported**
    - JSON object that outlines the details of the Credential supported by the PID/(Q)EAA Provider. It includes a list of name/value pairs, where each name uniquely identifies a specific supported Credential. This identifier is utilized to inform the Wallet Instance which Credential can be provided by the PID/(Q)EAA Provider. The associated value within the object MUST contain metadata specific to that Credential, as defined following. See `OpenID4VCI`_ Sections 11.2.3 and A.3.2.

        - **format**:  String identifying the format of this Credential. The PID/(Q)EAA MUST support the value string "*vc+sd-jwt*". See `OpenID4VCI`_ Section A.3.1.
        - **scope**: String identifying the supported *scope* value. The Wallet Instance MUST use this value in the Pushed Authorization Request. Scope values MUST be the entire set or a subset of the *scope* values in the *scopes_supported* parameter of the Authorization Server.
        - **cryptographic_binding_methods_supported**: JSON Array of case sensitive strings that identify the representation of the cryptographic key material that the issued Credential is bound to. The PID/(Q)EAA Provider MUST support the value "*jwk*".
        - **credential_signing_alg_values_supported**: JSON Array of case sensitive strings that identify the algorithms that the PID/(Q)EAA Provider MUST support to sign the issued Credential. See Section :ref:`Cryptographic algorithms` for more details.
        - **proof_types_supported**: JSON object which provide detailed information about the key proof(s) supported by the PID/(Q)EAA Provider. It consists of a list of name/value pairs, where each name uniquely identifies a supported proof type. The PID/(Q)EAA Provider MUST support at least "*jwt*" as defined in `OpenID4VCI`_ Section 7.2. The value associated with each name/value pair is a JSON object containing metadata related to the key proof. The PID/(Q)EAA Provider MUST support at least the parameter **proof_signing_alg_values_supported** which MUST be a JSON Array of case sensitive strings that identify the supported algorithms (see Section :ref:`Cryptographic algorithms` for more details about the supported algorithms).
        - **display**: Array of objects containing display language properties. The parameters that MUST be included are:   
                
                - **name**: String value of a display name for the Credential.
                - **locale**: String value that identifies the language of this object represented as a language tag taken from values defined in *BCP47* :rfc:`5646`. There MUST be only one object for each language identifier.

        - **vct**: As defined in [:ref:`SD-JWT-VC Credential Format`].
        - **claims**: JSON object comprising a collection of name/value pairs, where each name represents a claim related to the subject described in the Credential. The value associated with each name MAY be either another nested object or an array of objects. To provide detailed information about the claim, the innermost value MUST contain at least the following parameters. See `OpenID4VCI`_ Section A.3.2.
            
            - **value_type**: String value determining the type of value of the claim. The values that MUST be supported by the PID/(Q)EAA Provider are *String* and *Boolean*.
            - **display**: Array of objects containing display language properties. The parameters that MUST be included are:   
                
                - **name**: String value of a display name for the claim.
                - **locale**: String value that identifies the language of this object represented as a language tag taken from values defined in *BCP47* :rfc:`5646`. There MUST be only one object for each language identifier.

  * - **jwks**
    - JSON Web Key Set document, passed by value, containing the protocol specific keys for the Credential Issuer. See `OID-FED`_ Section 5.2.1 and `JWK`_.



Metadata for wallet_relying_party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *wallet_relying_party* metadata MUST contain the parameters as defined in Section :ref:`Metadata for wallet_relying_party`.


Example of a (Q)EAA Provider Entity Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below is a non-normative example of an Entity Configuration of a (Q)EAA Provider containing a metadata for 

  - `federation_entity`
  - `oauth_authorization_server`
  - `openid_credential_issuer`
  - `wallet_relying_party`

.. literalinclude:: ../../examples/ec-eaa.json
  :language: JSON

