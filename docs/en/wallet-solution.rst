.. include:: ../common/common_definitions.rst

.. _wallet-solution.rst:

wallet-solution.rst
+++++++++++++++++++++++++++

The Wallet Solution is a comprehensive product offered by the Wallet Provider to cater to the needs of users in managing their digital assets securely. Designed to provide a seamless user experience, this solution enables users to leverage the capabilities of the Wallet effectively. 
  
    
Requirements
------------

 - Trustworthiness within the Wallet ecosystem: the Wallet Instance must establish trust and reliability within the Wallet ecosystem.
 - Compliance with Provider specifications for obtaining PID and (Q)EAA: the Wallet Instance must adhere to the specifications set by Providers for obtaining Personal Identification (PID) and Qualified or non-qualified Electronic Address Authentication (Q)EAA.
 - Support for Android and iOS operating systems: the Wallet Instance should be compatible and functional on both Android and iOS operating systems, as well as available on Play Store and App Store respectively.
 - Verification of device ownership by the user: the Wallet Instance must provide a mechanism to verify the user's actual possession of the device.


          
Wallet Solution
-----------------------------
It comprises a mobile app and backend services that work together to deliver a holistic Wallet experience.

The mobile app serves as the primary interface for users, allowing them to access and interact with their digital assets conveniently; such digital assets are the Attestations, that include Personal Identification Data (PID¹), a set of data that can uniquely identify a natural or a legal person, along with other Qualified and non-qualified Electronic Attestations of Attributes (QEAAs and EAAs respectively, or (Q)EAAs in a more concise fashion¹).
Once a user installs the mobile app on its device, we refer to such an installation as Wallet Instance for the user.

Supporting the mobile app, the backend services play a vital role in ensuring the security and reliability of the Wallet Solution. These services are responsible for issuing the wallet instance attestation, a cryptographic proof that verifies the authenticity and integrity of the Wallet Instance. Additionally, the backend services handle revocation requests, allowing users to securely revoke access or privileges associated with their Wallet instance when needed.


Wallet Instance
-----------------------------
The Wallet Instance serves as a unique and secure representation of the user within the Wallet ecosystem. It establishes a strong and reliable identity for the user, enabling them to engage in various digital transactions in a secure and privacy-preserving fashion.

The Wallet Instance establishes trust within the Wallet ecosystem by consistently presenting a Wallet Instance Attestation during interactions with other ecosystem actors such as PID Providers, (Q)EAA Providers, and Relying Parties. These attestations, provided by the underlying backend services operated by the Wallet Provider, reference a pair of asymmetric cryptographic keys exclusively owned by the Wallet Instance. Their purpose is to authenticate the Wallet Instance itself, ensuring its legitimacy when engaging with other ecosystem actors.

To guarantee the utmost security, these cryptographic keys are securely stored within the device's Trusted Execution Environment (TEE)⁴. This ensures that only the User can access them, thus preventing unauthorized usage or tampering. For more detailed information, please refer to the Wallet Instance Attestation section² and the Trust Model section⁵ of this document.


Wallet Instance Lifecycle
-----------------------------
The Wallet Instance can exist in three distinct states: Operational, Valid and Deactivated. Each state represents a specific functional status and determines the actions that can be performed³.

Initialization Process:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To activate the Wallet Instance, users must install the mobile application on their device and open it. Furthermore, users will be asked to set their preferred method of unlocking their device; this can be accomplished by entering a personal identification number (PIN) or by utilizing biometric authentication, such as fingerprint or facial recognition, according to their device capabilities.

After completing these steps, the Wallet Instance is in the Operational state.

Transition to Valid state:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To transition from the Operational state to the Valid state, the Wallet Instance must obtain a valid Personal Identification (PID). Once a valid PID is acquired, the Wallet Instance becomes active, enabling secure transaction execution.

In order to securely and unambiguously identify users, the Wallet Instance adopts a Level of Assurance (LoA) 3 authentication, which guarantees a high level of confidence in the user's identity. The authentication method is chosen by the PID provider among the notified eID solutions at national level. 

Once in the Wallet Instance is in the Operational state, Users are empowered to:
obtain, view and manage (Q)EAAs from trusted (Q)EEA Providers¹
authenticate to Relying Parties¹
authorize sharing their data with Relying Parties

Please refer to the relative sections for further information about PID and (Q)EAAs issuing and attestation presentation.

Return to Operational state:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A Valid  Wallet Instance may revert to the Operational state under specific circumstances. These circumstances include the expiration or revocation of the associated PID by the relevant PID Provider.

Deactivation:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Users have the ability to deactivate the Wallet Instance voluntarily. This action removes the Operational capabilities of the Wallet Instance and sets it to the deactivated state. Deactivation provides users with control over access and usage based on their preferences.



External references
-------------------
¹ Definitions are inherited by the EUDI Wallet Architecture and Reference Framework, version 1.1.0 at the time of writing; please refer to https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/9647a408f628569449af6b30a15fed82cd41129a/arf.md#2-definitions for extended definitions and details.
² TODO: link to https://github.com/italia/eidas-it-wallet-docs/blob/versione-corrente/docs/en/wallet-instance-attestation.rst
³ Wallet Instance states adhere to the EUDI Wallet Architecture and Reference Framework, see https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/arf.md#424-eudi-wallet-instance-lifecycle
⁴ Depending on the device operating system, TEE is defined by https://source.android.com/docs/security/features/trusty or https://support.apple.com/en-gb/guide/security/sec59b0b31ff/web for Android and iOS devices respectively.
⁵ TODO: link to https://github.com/italia/eidas-it-wallet-docs/blob/versione-corrente/docs/en/trust.rst