.. include:: ../common/common_definitions.rst

.. _wallet-solution.rst:

Wallet Solution
-------------------

The Wallet Solution is a comprehensive product offered by the Wallet Provider to cater to the needs of Users in managing their digital assets securely. Designed to provide a seamless User experience, this solution enables Users to leverage the capabilities of the Wallet effectively.

The Wallet Solution is issued by the Wallet Provider in the form of a mobile app, it also consists of services and web interfaces for the exchange of data between the Wallet Provider and its Wallet Instances for the requirements of the trust model and in total respect of the user's privacy, in accordance with national and EU legislation.

The mobile app serves as the primary interface for Users, allowing them to access and interact with their digital assets conveniently. These digital assets, known as Attestations, include Personal Identification Data (PID¹), a set of data that can uniquely identify a natural or a legal person, along with other Qualified and non-qualified Electronic Attestations of Attributes, also known as QEAAs and EAAs respectively, or (Q)EAAs for short¹. Once a User installs the mobile app on their device, we refer to such an installation as a Wallet Instance for the User.

Supporting the mobile app, the Wallet Provider plays a vital role in ensuring the security and reliability of the Wallet Solution. The Wallet Provider is responsible for issuing the Wallet Instance Attestation — a cryptographic proof that verifies the authenticity and integrity of the Wallet Instance.


Requirements
^^^^^^^^^^^^^^^^^^^^

 - **Trustworthiness within the Wallet ecosystem**: the Wallet Instance must establish trust and reliability within the Wallet ecosystem.
 - **Compliance with Provider specifications for obtaining PID and (Q)EAA**: the Wallet Instance must adhere to the specifications set by Providers for obtaining Personal Identification (PID) and Qualified or non-qualified Electronic Address Authentication (Q)EAA.
 - **Support for Android and iOS operating systems**: the Wallet Instance must be compatible and functional at least on both Android and iOS operating systems, as well as available on the Play Store and App Store respectively.
 - **Verification of device ownership by the User**: the Wallet Instance must provide a mechanism to verify the User's actual possession of the device and its control.

Wallet Instance
^^^^^^^^^^^^^^^^^^^^
The Wallet Instance serves as a unique and secure representation of the User within the Wallet ecosystem. It establishes a strong and reliable identity for the User, enabling them to engage in various digital transactions in a secure and privacy-preserving manner.

The Wallet Instance establishes the trust within the Wallet ecosystem by consistently presenting a Wallet Instance Attestation during interactions with other ecosystem actors such as PID Providers, (Q)EAA Providers, and Relying Parties. These attestations, provided by the underlying Wallet Provider operated by the Wallet Provider, reference a pair of asymmetric cryptographic keys exclusively owned by the Wallet Instance. Their purpose is to authenticate the Wallet Instance itself, ensuring its legitimacy when engaging with other ecosystem actors.

To guarantee the utmost security, these cryptographic keys are securely stored within the device's Trusted Execution Environment (TEE)³. This ensures that only the User can access them, thus preventing unauthorized usage or tampering. For more detailed information, please refer to the `Wallet Instance Attestation section`_ and the `Trust Model section`_ of this document.

Wallet Instance Lifecycle
^^^^^^^^^^^^^^^^^^^^
The Wallet Instance can exist in three distinct states: Operational, Valid, and Deactivated. Each state represents a specific functional status and determines the actions that can be performed².

Initialization Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To activate the Wallet Instance, Users must install the mobile application on their device and open it. Furthermore, Users will be asked to set their preferred method of unlocking their device; this can be accomplished by entering a personal identification number (PIN) or by utilizing biometric authentication, such as fingerprint or facial recognition, according to their personal preferences and device's capabilities.

After completing these steps, the Wallet Instance is in the Operational state.

Transition to Valid state
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To transition from the Operational state to the Valid state, the Wallet Instance must obtain a valid Personal Identification (PID). Once a valid PID is acquired, the Wallet Instance becomes active, enabling secure transaction execution.

In order to securely and unambiguously identify Users, the Wallet Instance adopts a Level of Assurance (LoA) 3 authentication, which guarantees a high level of confidence in the User's identity. The authentication method is chosen by the PID provider from among the notified eID solutions at the national level.

Once the Wallet Instance is in the Operational state, Users can:

 - Obtain, view, and manage (Q)EAAs from trusted (Q)EAA Providers¹
 - Authenticate to Relying Parties¹
 - Authorize the sharing of their data with Relying Parties

Please refer to the relative sections for further information about PID and (Q)EAAs issuance and attestation presentation.

Return to Operational state
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A Valid Wallet Instance may revert to the Operational state under specific circumstances. These circumstances include the expiration or revocation of the associated PID by the relevant PID Provider.

Deactivation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Users have the ability to deactivate the Wallet Instance voluntarily. This action removes the operational capabilities of the Wallet Instance and sets it to the deactivated state. Deactivation provides Users with control over access and usage according to their preferences.

External references
^^^^^^^^^^^^^^^^^^^^
¹ Definitions are inherited from the EUDI Wallet Architecture and Reference Framework, version 1.1.0 at the time of writing. Please refer to `this page <https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/9647a408f628569449af6b30a15fed82cd41129a/arf.md#2-definitions>`_ for extended definitions and details.

² Wallet Instance states adhere to the EUDI Wallet Architecture and Reference Framework, as defined `here <https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/9647a408f628569449af6b30a15fed82cd41129a/arf.md#424-eudi-wallet-instance-lifecycle>`_.

³ Depending on the device operating system, TEE is defined by `Trusty`_ or `Secure Enclave`_ for Android and iOS devices, respectively.

.. _Trust Model section: trust.html 
.. _Wallet Instance Attestation section: wallet-instance-attestation.html
.. _Trusty: https://source.android.com/docs/security/features/trusty
.. _Secure Enclave: https://support.apple.com/en-gb/guide/security/sec59b0b31ff/web
