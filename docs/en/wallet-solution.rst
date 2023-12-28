.. include:: ../common/common_definitions.rst

.. _wallet-solution.rst:

Wallet Solution
-------------------

The Wallet Solution is a comprehensive product offered by the Wallet Provider to cater to the needs of Users in managing their digital assets securely. Designed to provide a seamless User experience, this solution enables Users to leverage the capabilities of the Wallet effectively.

The Wallet Solution is issued by the Wallet Provider in the form of a mobile app, it also consists of services and web interfaces for the exchange of data between the Wallet Provider and its Wallet Instances for the requirements of the trust model and in total respect of the user's privacy, in accordance with national and EU legislation.

The mobile app serves as the primary interface for Users, allowing them to access and interact with their digital assets conveniently. These digital assets, known as Attestations, include Personal Identification Data (PID[1]), a set of data that can uniquely identify a natural or a legal person, along with other Qualified and non-qualified Electronic Attestations of Attributes, also known as QEAAs and EAAs respectively, or (Q)EAAs for short[1]. Once a User installs the mobile app on their device, it is referred to such an installation as a Wallet Instance for the User.

By supporting the mobile app, the Wallet Provider plays a vital role in ensuring the security and reliability of the entire Wallet Solution, since it is responsible for issuing the Wallet Attestation, that is a cryptographic proof that allow the evaluation of the authenticity and the integrity of the Wallet Instance.


Requirements
^^^^^^^^^^^^^^^^^^^^

 - **Trustworthiness within the Wallet ecosystem**: the Wallet Instance MUST establish trust and reliability within the Wallet ecosystem.
 - **Compliance with Provider specifications for obtaining PID and (Q)EAA**: the Wallet Instance MUST adhere to the specifications set by Providers for obtaining Personal Identification (PID) and (Q)EAAs.
 - **Support for Android and iOS operating systems**: the Wallet Instance MUST be compatible and functional at least on both Android and iOS operating systems, as well as available on the Play Store and App Store respectively.
 - **Verification of device ownership by the User**: the Wallet Instance MUST provide a mechanism to verify the User's actual possession and full control of their personal device.

Wallet Instance
^^^^^^^^^^^^^^^
The Wallet Instance serves as a unique and secure device for authenticating the User within the Wallet ecosystem. It establishes a strong and reliable identity for the User, enabling them to engage in various digital transactions in a secure and privacy-preserving manner.

The Wallet Instance establishes the trust within the Wallet ecosystem by consistently presenting a Wallet Attestation during interactions with other ecosystem actors such as PID Providers, (Q)EAA Providers, and Relying Parties. These verifiable attestations, provided by the Wallet Provider, reference the public part of the asymmetric cryptographic key owned by the Wallet Instance. Their purpose is to authenticate the Wallet Instance itself, ensuring its realiability when engaging with other ecosystem actors.

To guarantee the utmost security, these cryptographic keys are securely stored within the device's Trusted Execution Environment (TEE)[3]. This ensures that only the User is allowed to access them, thus preventing unauthorized usage or tampering. For more detailed information, please refer to the `Wallet Attestation section`_ and the `Trust Model section`_ of this document.

Wallet Instance Lifecycle
^^^^^^^^^^^^^^^^^^^^^^^^^
The Wallet Instance has three distinct states: Operational, Valid, and Deactivated. Each state represents a specific functional status and determines the actions that can be performed[2].

Initialization Process
~~~~~~~~~~~~~~~~~~~~~~
To activate the Wallet Instance, the Users MUST install the mobile wallet application on their device and open it. Furthermore, Users will be asked to set their preferred method of unlocking their device; this can be accomplished by entering a personal identification number (PIN) or by utilizing biometric authentication, such as fingerprint or facial recognition, according to their personal preferences and device's capabilities.

After completing these steps, the Wallet Instance sets the Operational state.

Transition to Valid state
~~~~~~~~~~~~~~~~~~~~~~~~~
To transition from the Operational state to the Valid state, the Wallet Instance MUST obtain a valid Personal Identification (PID). Once a valid PID is acquired, the Wallet Instance becomes Valid.

In order to securely and unambiguously identify Users, the Wallet Instance adopts a Level of Assurance (LoA) 3 authentication, which guarantees a high level of confidence in the User's identity. The authentication method is chosen by the PID Provider from among the notified eID solutions at the national level.

Once the Wallet Instance is in the Operational state, Users can:

 - Obtain, view, and manage (Q)EAAs from trusted (Q)EAA Providers[1];
 - Authenticate to Relying Parties[1];
 - Authorize the presentation of their digital credentials with Relying Parties.

Please refer to the relative sections for further information about PID and (Q)EAAs issuance and presentation.

Return to Operational state
~~~~~~~~~~~~~~~~~~~~~~~~~~~
A Valid Wallet Instance may revert to the Operational state under specific circumstances. These circumstances include the expiration or the revocation of the associated PID by its PID Provider.


Deactivation
~~~~~~~~~~~~
Users have the ability to deactivate the Wallet Instance voluntarily. This action removes the operational capabilities of the Wallet Instance and sets it to the Deactivated state. Deactivation provides Users with control over access and usage according to their preferences.


Wallet Provider Endpoints
^^^^^^^^^^^^^^^^^^^^^^^^^

The Wallet Provider that issues the Wallet Attestations MUST
made available its APIs in the form of RESTful services, as listed below.

Wallet Provider Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
An HTTP GET request to the **/.well-known/openid-federation** endpoint allows the retrieval of the Wallet
Provider Entity Configuration.

The Wallet Provider Entity Configuration is a JWS containing the public keys and supported algorithms of the Wallet Provider metadata definition. It is structured in accordance with the `OpenID Connect Federation <https://openid.net/specs/openid-connect-federation-1_0.html>`_ and the Trust Model section outlined in this specification.

The returning Entity Configuration of the Wallet Provider MUST contain the
attributes listed below:

Header
^^^^^^
+---------+-----------------------------------------------------------------+
| **Key** | **Value**                                                       |
+---------+-----------------------------------------------------------------+
| alg     | Algorithm used to verify the token signature (e.g., ES256).     |
+---------+-----------------------------------------------------------------+
| kid     | Thumbprint of the public key used for signing.                  |
+---------+-----------------------------------------------------------------+
| typ     | Media type, set to ``entity-statement+jwt``.                    |
+---------+-----------------------------------------------------------------+

Payload
^^^^^^^
+-----------------------------------+-----------------------------------+
| **Key**                           | **Value**                         |
+-----------------------------------+-----------------------------------+
| iss                               | Public URL of the Wallet          |
|                                   | Provider.                         |
+-----------------------------------+-----------------------------------+
| sub                               | Public URL of the Wallet          |
|                                   | Provider.                         |
+-----------------------------------+-----------------------------------+
| iat                               | Issuance datetime in              |
|                                   |  Unix Timestamp format.           |
+-----------------------------------+-----------------------------------+
| exp                               | Expiration datetime               |
|                                   | in Unix Timestamp format.         |
+-----------------------------------+-----------------------------------+
| authority_hints                   | Array of URLs (String) containing |
|                                   | the list of URLs of the           |
|                                   | immediate superior Entities, such |
|                                   | as the Trust Anchor or an         |
|                                   | Intermediate, that MAY issue an   |
|                                   | Entity Statement related to this  |
|                                   | subject.                          |
+-----------------------------------+-----------------------------------+
| jwks                              | A JSON Web Key Set (JWKS) `RFC    |
|                                   | 7517 <http://tools.ietf.org/html  |
|                                   | rfc7517.html>`_                   |
|                                   | that represents the public part   |
|                                   | of the signing keys of the Entity |
|                                   | at issue. Each JWK in the JWK set |
|                                   | MUST have a key ID (claim kid).   |
+-----------------------------------+-----------------------------------+
| metadata                          | Contains the                      |
|                                   | metadata                          |
|                                   | ``wallet_provider``               |
|                                   | and the                           |
|                                   | ``federation_entity`` metadata.   |
+-----------------------------------+-----------------------------------+

`wallet_provider` metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+---------------------------------------------------------------------+
| **Key**                                     | **Value**                                                           |
+---------------------------------------------+---------------------------------------------------------------------+
| jwks                                        | A JSON Web Key Set (JWKS)                                           |
|                                             | that represents the  Wallet                                         |
|                                             | Provider's public keys.                                             |
+---------------------------------------------+---------------------------------------------------------------------+
| token_endpoint                              | Endpoint for obtaining the Wallet                                   |
|                                             | Instance Attestation.                                               |
+---------------------------------------------+---------------------------------------------------------------------+
| aal_values_supported                        | List of supported values for the                                    |
|                                             | certifiable security context. These                                 |
|                                             | values specify the security level                                   |
|                                             | of the app, according to the levels: low, medium, or high.          |
|                                             | Authenticator Assurance Level values supported.                     |
+---------------------------------------------+---------------------------------------------------------------------+
| grant_types_supported                       | The types of grants supported by                                    |
|                                             | the token endpoint. It MUST be set to                               |
|                                             | ``urn:ietf:params:oauth:client-assertion-type:                      |
|                                             | jwt-client-attestation``.                                           |
+---------------------------------------------+---------------------------------------------------------------------+
| token_endpoint_auth_methods_suppor          | Supported authentication methods for                                |
| ted                                         | the token endpoint.                                                 |
+---------------------------------------------+---------------------------------------------------------------------+
| token_endpoint_auth_signing_alg_va          | Supported signature                                                 |
| lues_supported                              | algorithms for the token endpoint.                                  |
+---------------------------------------------+---------------------------------------------------------------------+

.. note::
   The `aal_values_supported` parameter is experimental and under review.

Payload `federation_entity`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------+----------------------------------------------+
| **Key**           | **Value**                                    |
+-------------------+----------------------------------------------+
| organization_name | Organization name.                           |
+-------------------+----------------------------------------------+
| homepage_uri      | Organization's website URL.                  |
+-------------------+----------------------------------------------+
| tos_uri           | URL to the terms of service.                 |
+-------------------+----------------------------------------------+
| policy_uri        | URL to the privacy policy.                   |
+-------------------+----------------------------------------------+
| logo_uri          | URL of the organization's logo in SVG format.|
+-------------------+----------------------------------------------+

Below a non-normative example of the Entity Configuration.

.. code-block:: javascript

  {
    "alg": "ES256",
    "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
    "typ": "entity-statement+jwt"
  }
  .
  {
  "iss": "https://wallet-provider.example.org",
  "sub": "https://wallet-provider.example.org",
  "jwks": {
    "keys": [
      {
        "crv": "P-256",
        "kty": "EC",
        "x": "qrJrj3Af_B57sbOIRrcBM7br7wOc8ynj7lHFPTeffUk",
        "y": "1H0cWDyGgvU8w-kPKU_xycOCUNT2o0bwslIQtnPU6iM",
        "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY"
      }
    ]
  },
  "metadata": {
    "wallet_provider": {
      "jwks": {
        "keys": [
          {
            "crv": "P-256",
            "kty": "EC",
            "x": "qrJrj3Af_B57sbOIRrcBM7br7wOc8ynj7lHFPTeffUk",
            "y": "1H0cWDyGgvU8w-kPKU_xycOCUNT2o0bwslIQtnPU6iM",
            "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY"
          }
        ]
      },
      "token_endpoint": "https://wallet-provider.example.org/token",
      "aal_values_supported": [
        "https://wallet-provider.example.org/LoA/basic",
        "https://wallet-provider.example.org/LoA/medium",
        "https://wallet-provider.example.org/LoA/high"
      ],
      "grant_types_supported": [
        "urn:ietf:params:oauth:client-assertion-type:jwt-client-attestation"
      ],
      "token_endpoint_auth_methods_supported": [
        "private_key_jwt"
      ],
      "token_endpoint_auth_signing_alg_values_supported": [
        "ES256",
        "ES384",
        "ES512"
      ]
    },
    "federation_entity": {
      "organization_name": "IT Wallet Provider",
      "homepage_uri": "https://wallet-provider.example.org",
      "policy_uri": "https://wallet-provider.example.org/privacy_policy",
      "tos_uri": "https://wallet-provider.example.org/info_policy",
      "logo_uri": "https://wallet-provider.example.org/logo.svg"
    }
  },
  "authority_hints": [
    "https://registry.eudi-wallet.example.it"
  ]
  "iat": 1687171759,
  "exp": 1709290159
  }


Wallet Attestation
~~~~~~~~~~~~~~~~~~

Please refer to the `Wallet Attestation section`_.


External references
^^^^^^^^^^^^^^^^^^^^
.. [1] Definitions are inherited from the EUDI Wallet Architecture and Reference Framework, version 1.1.0 at the time of writing. Please refer to `this page <https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/9647a408f628569449af6b30a15fed82cd41129a/arf.md#2-definitions>`_ for extended definitions and details.

.. [2] Wallet Instance states adhere to the EUDI Wallet Architecture and Reference Framework, as defined `here <https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/9647a408f628569449af6b30a15fed82cd41129a/arf.md#424-eudi-wallet-instance-lifecycle>`_.

.. [3] Depending on the device operating system, TEE is defined by `Trusty`_ or `Secure Enclave`_ for Android and iOS devices, respectively.

.. _Trust Model section: trust.html
.. _Wallet Attestation section: wallet-instance-attestation.html
.. _Trusty: https://source.android.com/docs/security/features/trusty
.. _Secure Enclave: https://support.apple.com/en-gb/guide/security/sec59b0b31ff/web

