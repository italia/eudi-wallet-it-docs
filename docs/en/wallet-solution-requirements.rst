.. include:: ../common/common_definitions.rst
.. Included via wallet-solution.rst at title level '^' (level 2).

Wallet Solution Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section lists the requirements about Wallet Providers and Wallet Solutions with their Wallet Instances, as well as the corresponding Wallet Instance Attestation, Key Attestation and the secure storage components: the **Keystore** (used for all Digital Credentials) and the **WSCA/Remote WSCD** (used exclusively for PID at Level of Assurance High).

- The Wallet Solution MUST adhere to the specifications set by this document for obtaining Personal Identification (PID) and (Q)EAAs.
- The Wallet Provider MUST expose a set of endpoints, exclusively available to its Wallet Solution instances, supporting the core functionalities of the Wallet Instances.
- The Wallet Instance MUST periodically reestablish trust with its Wallet Provider, obtaining a fresh Wallet Instance Attestation (:ref:`WP_018 <wallet-instance-testcases>`).
- The Wallet Instance MUST establish trust with other participants of the Wallet ecosystem, such as Credential Issuers. In case of Credential Issuers, Wallet Instance presents both Wallet Instance and Key Attestations.
- The Wallet Instance MUST be compatible and functional on both Android and iOS operating systems and available on the Play Store and App Store, respectively (:ref:`WP_015 <wallet-instance-testcases>`).
- The Wallet Instance MUST provide a mechanism to verify the User's actual possession and full control of their personal device.
- The Wallet Instance MUST provide Users with an up-to-date list of Relying Parties with which the User has established a connection and, where applicable, all data exchanged;
- The Wallet Instance MUST provide Users with a mechanism to request the erasure of personal attributes by a Relying Party pursuant to Article 17 of Regulation (EU) 2016/679, and to log each Erasure Request made.

.. note::
   There is no strict one-to-one mapping between the requirements in this section and the test cases in :ref:`test-plans-wallet-provider:Wallet Provider Test Matrix`. Some requirements are expressed at too high a level to be represented as atomic test cases, while others are already addressed in greater detail within related flows (e.g., :ref:`wallet-instance-attestation-issuance:Wallet Instance Attestation Issuance`).

Wallet Instance Attestation Requirements
"""""""""""""""""""""""""""""""""""""""""

Wallet Instance Attestation contains information regarding the security level of the device hosting the Wallet Instance.
It primarily proves the **authenticity**, **integrity**, **security**, and in general the **trustworthiness** of a particular Wallet Instance.

The requirements for the Wallet Instance Attestation are defined below:

- The Wallet Instance Attestation MUST provide all the relevant information to attest to the **integrity** and **security** of the device where the Wallet Instance is installed  (:ref:`WP_019 <wallet-instance-testcases>`).
- The Wallet Instance Attestation MUST be signed by the Wallet Provider that has authority over and is the owner of the Wallet Solution, as specified by the overseeing Registration Authority. This ensures that the Wallet Instance Attestation uniquely links the Wallet Provider to this particular Wallet Instance (:ref:`WP_020 <wallet-instance-testcases>`).
- The Wallet Provider MUST periodically evaluate and guarantee the integrity, the authenticity, and the genuineness of the Wallet Instance. The Wallet Provider verifies the Wallet Instance using the most secure flow made available by OS Provider's API, such as the *Play Integrity API* for Android and *App Attest* for iOS (:ref:`WP_011 <wallet-provider-backend-testcases>`).
- The Wallet Instance Attestation MUST be securely bound to the Wallet Instance's ephemeral public key (:ref:`WP_019b <wallet-instance-testcases>`).
- The Wallet Instance Attestation MAY be used multiple times during its validity period, allowing for repeated authentication and authorization without the need to request new attestations with each interaction. However, it is RECOMMENDED that Wallet Instances avoid using the same attestation repeatedly, due to privacy concerns such as linkability between different interactions.
- The Wallet Instance Attestation MUST be short-lived and MUST have an expiration time, after which it MUST no longer be considered valid.
- The Wallet Instance Attestation MUST NOT be issued by the Wallet Provider if the authenticity, integrity, and genuineness of the Wallet Instance requesting it cannot be guaranteed (:ref:`WP_019a <wallet-instance-testcases>`).
- Each Wallet Instance SHOULD be able to request multiple Wallet Instance Attestations using different cryptographic public keys associated with them.
- The Wallet Instance Attestation MUST NOT contain information about the User in control of the Wallet Instance (:ref:`WP_029b <wallet-instance-testcases>`).
- The Wallet Instance MUST secure a Wallet Instance Attestation as a prerequisite for transitioning to the Operational state, as defined by `EIDAS-ARF`_.
- A Wallet Provider SHALL ensure that a non-revoked Wallet Unit at all times presents a temporally valid and non-revoked Wallet Instance Attestation to a PID Provider or Attestation Provider during the issuance process of a PID or attestation. Note: This requirement applies to both device-bound and non-device-bound attestations, as defined by `EIDAS-ARF`_.
- A Wallet Unit SHALL present a Wallet Instance Attestation only to a PID Provider or Attestation Provider, as part of the issuance process of a PID or an attestation, and not to a Relying Party or any other entity.

.. note::
  Throughout this section, the services used to attest genuineness of the Wallet Instance and the device in which it is installed are referred to as **Device Integrity Service API**. The Device Integrity Service API is considered in an abstract fashion and it is assumed to be a service provided by a trusted third party (i.e., the OS Provider's API) which is able to perform integrity checks on the Wallet Instance as well as on the device where it is installed.


Key Attestation Requirements
""""""""""""""""""""""""""""""""""""

Key Attestation contains information to ensure that keys used for Digital Credential key binding are securely generated and stored in a trustworthy hardware-backed environment: a **Keystore** for standard device-bound Digital Credentials, or a **WSCA** operating within a **Remote WSCD** (remote HSM) exclusively for the PID at Level of Assurance High. It also provides a method to authenticate the key storage environment with the Credential Issuer and verifies that the Wallet Unit has not been revoked.

The requirements for the Key Attestation are defined below:

- The Key Attestation SHALL provide a PID Provider or Attestation Provider with information about the properties of the Keystore or the WSCA/WSCD of the Wallet Unit, such that they are able to take a well-grounded decision on whether to issue a PID or attestation to the Wallet Unit.
- The Key Attestation SHALL enable PID Providers and Attestation Providers to verify the authenticity and revocation status of the Wallet Unit.
- A Wallet Provider SHALL ensure that a non-revoked Wallet Unit at all times can present a Key Attestation, when requested by a PID Provider or Attestation Provider.
- During issuance of a PID, the Wallet Unit SHALL provide the PID Provider with a valid Key Attestation (KA) describing the WSCA and the Remote WSCD that generated the new PID private key. Note: A PID private key is always generated and managed by the WSCA operating within the Remote WSCD (remote HSM), which by definition complies with requirements for Level of Assurance High.
- During issuance of a device-bound attestation other than a PID, the Wallet Unit SHALL provide the Attestation Provider with a valid Key Attestation (KA) describing the Keystore in which the new credential private key was generated and is stored. The Wallet Unit SHALL retrieve the key storage requirements of the Attestation Provider from the Issuer metadata (as specified in `OpenID4VCI`_) and SHALL determine which of its Keystores, if any, comply with these requirements. Note: A KA for a device-bound attestation describes the properties of the Keystore as attested by the OEM Key Attestation APIs, and contains one or more public key(s) corresponding to private key(s) generated by and stored in that Keystore.
- If a Wallet Unit contains multiple Keystores or WSCAs, it SHALL, internally and securely, keep track of which PIDs and attestations are bound to which Keystore or WSCA.
- A Wallet Unit SHALL present a Key Attestation only as part of the issuance of a PID or a key-bound attestation.
- The Key Attestation SHALL enable PID Providers to request a Wallet Provider to revoke a Wallet Unit, by including an identifier for the Wallet Unit in the KA (e.g., a URI and index to an Attestation Status List). The Wallet Provider SHALL ensure that this Wallet Unit identifier does not enable tracking of the User.
- The Key Attestation MUST contain one or multiple attested Credential's public key(s) that are bound to the same Keystore or WSCA/WSCD.
- The Key Attestation MUST be signed by the Wallet Provider that has authority over and is the owner of the Wallet Solution, as specified by the overseeing Registration Authority. Wallet Providers SHALL ensure that the certificates they use for signing KAs and WIAs comply with all applicable requirements in `ETSI TS 119 412-6`_, in particular Clause 5.
- An Attestation Provider issuing non-device-bound attestations SHALL indicate in its Credential Issuer metadata that it does not need a KA. A Wallet Unit SHALL NOT send a KA to an Attestation Provider when requesting a non-device-bound attestation. Note: A Wallet Unit sends a WIA to the Attestation Provider regardless of whether the attestations it issues are device-bound or not.
- A Wallet Provider SHALL ensure that the presentation of a KA is cryptographically bound to the specific context it is intended to be used in. Note: As specified in `OpenID4VCI`_, this is achieved by letting the signed KA itself contain a nonce provided by the PID Provider or Attestation Provider during the issuance process. Alternatively, the Wallet Unit presents the KA along with a Proof-of-Possession consisting of a signature over that nonce, created by the private key corresponding to one of the public keys attested in the KA.
- During issuance of a PID or a device-bound attestation, the PID Provider or Attestation Provider SHALL verify the KA in accordance with the requirements in `OpenID4VCI`_ Appendix F.4.
- During issuance of a PID or a device-bound attestation, the PID Provider or Attestation Provider SHALL receive a proof that the Wallet Unit possesses the private keys corresponding to all public keys in the KA.
- If the Keystore or the WSCA/WSCD is able to export a private key, the Wallet Provider SHALL specify this capability as an attribute in the KA.
- A Wallet Provider SHALL consider all relevant factors, including offline usage, interoperability, and the risk of a KA becoming a vector to track the User, when deciding on the validity period of a KA.
- The Key Attestation MUST NOT be issued by the Wallet Provider if the trustworthiness of the Keystore or WSCA/WSCD cannot be guaranteed. In this case, the Wallet Instance MUST be revoked.


Keystore Requirements
"""""""""""""""""""""

The **Keystore** is the default hardware-backed secure storage mechanism used by the Wallet Unit for all cryptographic operations related to Digital Credentials (other than the PID). Cryptographic keys associated with a Wallet Instance (e.g., used to generate the Wallet Instance Attestation) and with device-bound attestations MUST be securely generated and stored within the Keystore. Only the legitimate User can access the private cryptographic keys, preventing unauthorized usage or tampering.

The Keystore relies on the device's native cryptographic hardware provided by the OEM:

- **Android**: Strongbox Keymaster (a dedicated Hardware Security Module embedded in the device) is RECOMMENDED. The Trusted Execution Environment (TEE) MAY be used as a fallback only when Strongbox is unavailable.
- **iOS**: The Secure Enclave MUST be used.

The properties of the Keystore are attested by the OEM Key Attestation APIs (e.g., Android Key Attestation API, Apple DeviceCheck) and reported in the Key Attestation issued by the Wallet Provider (:ref:`WP_014 <wallet-instance-testcases>`).

For more detailed information, please refer to :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`, :ref:`wallet-instance-attestation-issuance:Wallet Instance Attestation Issuance`, and :ref:`wallet-attestation-issuance:Key Attestation Issuance` of this document.


WSCA/WSCD Requirements
""""""""""""""""""""""

The **WSCA/WSCD** used for the PID consists of a WSCA operating within a **Remote WSCD** implemented as a remote Hardware Security Module (remote HSM) operated server-side. This combination is used exclusively for the issuance and management of the PID at Level of Assurance High. The PID private key MUST be generated and managed by the WSCA operating within the Remote WSCD (remote HSM), which by definition satisfies the requirements for Level of Assurance High.

.. note::
  In the current implementation profile, the WSCA/WSCD is exclusively required for PID issuance. Future versions of this specification MAY extend this requirement to other Digital Credentials that require Level of Assurance High.

For more detailed information, please refer to :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`, :ref:`wallet-instance-attestation-issuance:Wallet Instance Attestation Issuance`, and :ref:`wallet-attestation-issuance:Key Attestation Issuance` of this document.


