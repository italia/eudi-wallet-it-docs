.. include:: ../common/common_definitions.rst

.. _security-privacy-considerations.rst:

Security and Privacy Considerations
+++++++++++++++++++++++++++++++++++

This section provides an informal security analysis of the IT Wallet specification by analyzing the compliance with the security and privacy requirements identified in [`OpenID4VC-SecTrust`_]. 

.. note::

  As [`OpenID4VC-SecTrust`_] is still a work in progress, the security and privacy considerations described here are not yet complete and may change in the future. 

.. note::

    The focus of the analysis is the compliance of the design choices in the IT Wallet specification with respect to the OpenID4VC protocols. 
    It is currently out-of-scope *(i)* the analysis of the design of the proximity flow based on ISO 18013-5, and *(ii)* the analysis of the implementation; 
    as a consequence 7 requirements specifically related to the implementation are not considered (e.g., SV-00: The Verifier must implement the protocol securely and correctly).

As in [`OpenID4VC-SecTrust`_], all requirements are numbered for reference. Together with the respective component that needs to implement the requirement:

* **CF**: Credential Format;
* **P**: Protocol;
* **E**: Ecosystem;
* **I**: Issuer;
* **V**: Verifier;
* **W**: Wallet.

This specification adds the requirement category as a prefix:

* **SR**: Security Requirements;
* **PR**: Privacy Requirements;
* **SPR**: Security and Privacy Requirements.

The final identifier uses the following name space: *requirement_category-component-id*. 

For each requirement defined below, this section uses the description defined in [`OpenID4VC-SecTrust`_], specifying whether the requirement is satisfied (fully satisfied: |check-icon|, partially satisfied: |partially-check-icon|, and not satisfied: |uncheck-icon|).
In the following, the requirements are grouped based on their category.

Security Requirements
---------------------

SR-CF-10 and SR-E-10
~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - For any presentation, the Credential format and Trust Framework must be designed in a secure way to determine the Issuer and to check that the original Credential was issued by this Issuer (e.g., by using a cryptographic signature).

The IT Wallet specification supports both SD-JWT-VC and  mDOC-CBOR Credential formats. The authenticity and integrity of a Credential is checked by verifying the Issuer's signature. 

- For SD-JWT, the verification is performed using the algorithm specified in the **alg** header parameter of SD-JWT and the public key that is identified using the **kid** header of the SD-JWT, and extracted from the Trust Chain for the relevant Issuer specified in **iss** claim.  
- For mDOC, the Issuer's signature is contained in the *Mobile Security Object* (MSO) and can be validated using the Issuer's public key through a trusted certificate chain contained in the **x5chain** header parameter.

SR-CF-20
~~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - For any presentation, the Credential format must ensure that the data that is tied to the original Credential cannot be altered. (E.g., by using a cryptographic signature.)

The cryptographic signature included in the Credential format ensures that any tampering with the Credential will result in a failed verification.

SR-CF-21
~~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - For cryptographic Holder binding, the presentation format must allow that a Holder must prove possession of the private key that is bound to the Credential, usually by signing over a challenge consisting of a nonce and an identifier for the Verifier.

Both SD-JWT and mDOC-CBOR support cryptographic Holder binding defining how a Holder can present a Credential to a Verifier proving with a cryptographic proof
the legitimate possession of the Credential.

Currently, for the remote flow the IT Wallet specification supports only SD-JWT presentations. In this case, the KB-JWT (Key-Bound JWT) parameter is used to 
prove that the Holder possesses the private key bound to the Credential. The Holder signs the KB-JWT using a **nonce** and a Verifier identifier (**aud** claim) as a challenge.

SR-E-20
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - The Trust Framework must ensure that the identification of an Issuer is unique and unambiguous. If there are multiple instances of the same Issuer using the same key material, the Verifier must trust all instances equally.

The IT Wallet Trust Framework, compliant with OpenID Federation 1.0 [`OID-FED`_], ensures that each entity (e.g., an Issuer) is uniquely identified through cryptographic 
keys and metadata distributed via the Entity Configuration well-known endpoint. 

SR-E-30
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - The way in which the Verifier determines the trustworthiness of the Issuer defined in the Trust Framework must be secured from influence by a malicious party that can, for example, introduce untrustworthy entities into a directory.

Issuers are registered by a Trust Anchor or its Intermediate. To verify the trust of an Issuer, a Verifier must verify that the Trust Chain (i.e. a concatenation of statements) related to the Issuer is valid and still active. This validation process ensures that only trusted entities are permitted to participate in the system, preventing the introduction of untrustworthy actors.

SR-E-40
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - The Trust Framework must ensure that there is a way for Verifiers to keep their information on trusted Issuers up to date and that there is a way to revoke trust in an Issuer.

If an Issuer's Entity Statement is revoked or unavailable, means that Issuer is no longer considered valid within the federation. This ensures that Verifiers have real-time access to the status of trusted entities and can revoke trust if necessary. However, Verifiers must actively check the Issuer's status by querying federation endpoints (i.e., the fetch endpoint for obtaining the Entity Statement). 

SR-I-10
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - The Issuer must authenticate/identify the User properly according to the expectations of the Verifier (which may be defined in a specification, Trust Framework, or by convention).

The issuance process utilizes OAuth 2.0-based flows, specifically the Authorization Code Flow, to securely authenticate the User. Moreover, the User authentication is performed using eIDAS-notified schemes or the PID, ensuring a high LoA. 

SR-I-20
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - The Issuer must only put correct and up-to-date claims about the User into the Credential where verified data is expected.

When verified data is expected, the Issuer obtains the correct and up-to-date claims from the relevant Authentic Sources, ensuring their accuracy at the time of issuance. 

SR-I-30
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - The Issuer must revoke a Credential once the Issuer learns about potential abuse of the Credential.

The Issuer is the entity responsible for revoking a Credential. The specification describes several use cases that may trigger a revocation process and details the revocation flow in which the Issuer revokes Credentials at the User's request (through the Wallet Instance) after verifying possession of the Credentials. 

SR-I-40
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - The Issuer must only include Holder-binding data into the Credential that is tied to the actual User (and not, e.g., include a cryptographic key under control by a third party).

The issuance process securely binds the Credential to the User as follows (see :numref:`fig_Low-Level-Flow-ITWallet-PID-QEAA-Issuance`):

* Authorization (Steps 8-10): The Wallet Instance sends an authorization request, and the Issuer authenticates the User using a secure eIDAS scheme or a valid PID, providing the Access Token to the User.
* Proof of Key Possession (Steps 12-13, 16-17): The Wallet creates a DPoP Proof JWT, binding the Access Token to the Wallet Instance. The same key is then used later to request the Credential, ensuring continuity of ownership.
* Credential Issuance (Steps 18-21): The Credential request is verified using proof of possession, which is cryptographically bound to the User. The use of the same key in the DPoP ensures that the key material is controlled by the Wallet Instance, and not by a third party.

SR-I-50
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - (conditional w.r.t I-10) The Issuer must ensure that the Credential was stored in a secure Wallet.

A trusted Wallet Attestation ensures that the Wallet Instance is secure and meets the required security standards before any Credentials are issued or stored. 
In Steps 5-6 of :numref:`fig_Low-Level-Flow-ITWallet-PID-QEAA-Issuance`, the Wallet Instance provides a Wallet Attestation, which includes a proof of possession 
signed with the Wallet's private key. This attestation confirms that the Wallet Instance is genuine and has been verified by the Wallet Provider.

The Issuer verifies this attestation before allowing the Wallet to participate in the issuance process, ensuring that the Wallet adheres to specific security standards. 
Afterward, all cryptographic keys generated and used in the process come from this attested Wallet Instance, and the Wallet's identity (client ID) is included in the 
relevant tokens, ensuring continuity and trust in the Credential storage process. 

.. note:: 
  There is currently an open issue on this aspect (https://github.com/openid/OpenID4VCI/issues/355) in the OpenID4VCI spec.

SR-P-20
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - The protocol must ensure that no third party can interfere with the issuance process such that the Issuer issues Credentials for the third party to the User.

This requirement is addressed by secure identification of the Issuer. The "iss" parameter in the authorization response assures the Wallet that the response is coming from the expected Issuer, plus the use of PKCE avoids injection of the code from another session to the User session. 

SR-P-30
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - The protocol must ensure that the interaction between the Wallet and Verifier is protected such that no third party can interfere with the interaction by modifying the information transmitted.

The presentation process occurs through different flows, including remote and proximity. In the case of the remote flow, a combination of signed Request Objects, **nonce** usage, Trust Chain validation, Wallet Attestation, and Holder binding ensures that no third party can interfere with or modify the information transmitted between the Wallet and the Verifier. These mechanisms align with Security Requirement P-30, protecting the interaction from tampering or injection attacks. 

SR-P-40
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |partially-check-icon|
     - The protocol must ensure that the interaction between an attacker and a Verifier cannot be forwarded to and successfully completed by a User.

In the case of the same device flow, this can be prevented by using and properly checking the **nonce** value, which is created and sent by the Verifier in the authorization request. 
The Verifier should maintain a mapping between User sessions and the **nonce** that is expected in the flow. The Verifier should only accept a presentation if the **nonce** in the presentation 
matches the **nonce** that is expected for the User session. With this countermeasure, the Verifier can detect if a presentation is sent that was not bound to the User's session or if no 
User session exists at all, preventing the attack.

For cross-device flow the requirement is partially satisfied as the flow is vulnerable to Cross-Device Consent Phishing attacks (an attacker could initiate the presentation flow, 
obtain the signed Request Object and QR code, and forward it to the victim). 

Some security measures are already in place, such as the use of **nonce** and state. The **nonce** ensures freshness of the request, and the state binds the flow to a unique transaction, 
thus reducing the opportunity for a successful attack. 

.. note::
  Other security measures are currently under evaluation in issue #117 (https://github.com/italia/eudi-wallet-it-docs/issues/117), 
  where a list of mitigations from [`OAuthCrossDeviceSec`_] are discussed. Two examples are:
  
  - Short Lived/Timebound QR Codes: Reducing the lifetime of the QR code (e.g., 2-3 mins) is fundamental to restrict the time window available for the attacks. 
  - One-Time QR Codes: One-Time QR codes restrict the possibility of attacks when the same QR code is sent to multiple victims. 

SR-P-41
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - The protocol must ensure that an attacker cannot successfully forward an interaction between a Wallet and a Verifier to a Verifier under the control of the attacker.

A prerequisite for a successful attack of this kind is that the attacker has access to some messages between the Wallet and the Verifier, for example, 
the attacker might have access to the presentation contained in the VP Token. Given that, the proper implementation of TLS guarrantes confidentiality, avoiding the leakage of the response. 
In addition to TLS, the existing implementation of **nonce** and audience checks in the presentation protocol should help to meet the P-41 security requirement. 
Regarding the **nonce** claim, the Verifier MUST check that the **nonce** value in the VP Token matches the **nonce** value that is created by the Verifier during the authorization request.
Regarding the **aud** value, the Verifier must check that the audience of the presentation matches the Verifier's identifier. 

SR-P-50
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |partially-check-iconcheck-icon| 
     - The protocol must ensure that third parties cannot interfere with the binding process.

In the issuance phase, the Holder binding happens at the Credential request to the protected Credential endpoint. This means that the attacker needs to obtain the access token 
first and therefore send the request to the Credential endpoint and bind the Credentials to the keys under his control. The IT Wallet specification requires the use of a sender-constrained 
access token, which means that the access token binds to the device using cryptographic materials. 

The second surface for the attack is related to key management. In the case of using software-based keys, it is possible to clone the keys and move them to a device under 
attacker control, and in the case of stealing the Credentials as well, the attacker can easily create proof of possession of the keys. Therefore, it is highly dependent on 
the secure storage of the keys. In the case of the IT Wallet, it only supports the local internal WSCD that is providing Hardware bound keys that could mitigate the key cloning 
attack, but it does not provide a high enough level of assurance to meet stringent eIDAS requirements (local internal WSCD has been shown to be insufficiently secure against 
highly capable attackers). Therefore, the current implementation only partially satisfies it. 

SR-V-10
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |partially-check-icon|
     - (conditional w.r.t  I-50+V-20) The Verifier must ensure that the Credential was stored in a secure Wallet.

Verifier checks the Wallet Attestation during exchanges (sent with the authorization response), ensuring that it meets the security criteria required by the Verifier and that it is issued by a trusted Wallet Provider.  

.. note::
 Currently, no explicit security and privacy measures related to this requirement are specified in [`OpenID4VC-SecTrust`_] and it is not clearly defined what "stored in a secure Wallet" means. Without this detail, this requirement is considered only partially satisfied. Indeed, the Wallet Attestation guarantees 
 that the Wallet Instance is operating on a secure, trusted device and adheres to the strict security policies set by the Wallet Provider. However, the attestation does not directly guarantee that each 
 Credential within the Wallet is stored securely; it verifies the overall security of the Wallet environment, within which the Credentials reside. Therefore, while the attestation supports the Verifier's 
 confidence that the Credential comes from a secure source, it is ultimately a broad assurance of the Wallet's security, rather than a specific validation of individual Credential storage. 

SR-V-20
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - (conditional w.r.t.  I-10) The Verifier must ensure that the Credential was issued by an Issuer that only issues Credentials to trustworthy Wallets.

By checking the trust of the Issuer, the Verifier ensures that the Credential was issued by a trusted Issuer committed to issuing Credentials only to secure Wallets (as for SR-I-50).

.. note::
  Currently, no explicit security and privacy measures related to this requirement are specified in [`OpenID4VC-SecTrust`_], it remains a TODO. 

SR-W-20
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - The Wallet must provide trustworthy and complete information about Issuers to the User.

The Wallet Instance discovers the trusted Issuers using trusted third party resources, such as the Federation API (e.g., using the Subordinate Listing Endpoint of the Trust Anchor and its Intermediates), 
inspecting the Issuer metadata and Trust Marks for filtering the PID Provider.

The Issuer's information is displayed to the User during the issuance process and can be subsequently read by the User as it is inside the issued Credential. 
In addition to the Issuer's information, the Digital Credential Metadata Type also contains information on the Authentic Source.

SR-W-30
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - The Wallet must provide trustworthy and complete information about Verifiers to the User.

The Wallet validates the Trust Chain related to the Verifier and its information is displayed to the User before the presentation.

Privacy Requirements
--------------------

PR-CF-30
~~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon|
     - The Credential Format must ensure that there is a robust mechanism to ensure that data that is not to be released to a Verifier cannot be extracted by the Verifier (selective disclosure).

Both SD-JWT and mDOC-CBOR provide selective disclosure capability, allowing Holders to reveal only specific fields to the Verifier. 

PR-CF-40
~~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |partially-check-icon|
     - The Credential Format must support correlation protection.

While selective disclosure is a strong tool for preventing correlation, full unlinkability is not guaranteed in all cases. Issues like Verifier collusion or Issuer tracking can arise, especially if sensitive identifiers (e.g., taxpayer ID) are disclosed. 

.. tip::
  Batch issuance, using different key binding keys and salts for each Credential, can mitigate Verifier/Verifier and presentation unlinkability risks. 

PR-E-60
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon| 
     - The Trust Framework must ensure that the Issuer cannot learn where the User uses the Credential.

When a Verifier performs the Trust Evaluation of the Issuer of a Credential following [`OID-FED`_], the Issuer cannot know who is the User presenting the Credential.
In addition, privacy is protected also during the check of the Credential's status. By using Status Assertion [`OAUTH-STATUS-ASSERTION`_], the IT Wallet specification ensures 
that while the Verifier checks the Credential's validity, the Issuer does not learn where or when the Credential is being used.

PR-E-70
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |partially-check-icon|
     - The Trust Framework must support correlation protection.

In the case of IT Wallet, as the Trust Framework uses OpenID Federation [`OID-FED`_], the IT Wallet specification has the following mechanisms in place that could help to reduce the correlation:

- *Verifier-Verifier*: OpenID Federation provides the evaluation mechanisms to verify whether the Verifier is asking from the Wallet the information that is authorized to ask or not.  Thus, it will minimize the data exchange and consequently avoid User profiling by colluding between two Verifiers;
- *Issuer-Verifier*: The Issuer does not require the authentication of the Verifier during the trust evaluation. In principle, the Issuer does not know which Verifiers the User is accessing and will avoid User activity profiling based on the Verifier's access.

.. note::
 Even if metadata policies and Trust Marks are features offered by OpenID Federation, the current version of the IT Wallet specification makes them optional and does not provide details on their use.

PR-W-40
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon| 
     - The Wallet must ask the User for meaningful consent before a Credential is used. The Wallet must provide the User the opportunity to review any data that is released to a Verifier.

After establishing trust with the Verifier, the Wallet asks for the User's consent and provides the User the opportunity to review and select the data to be presented to the Verifier.

PR-W-60
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon| 
     - The Wallet must ensure that the Issuer cannot learn where the User uses the Credential.

Same as for SR-P-80.

PR-W-70
~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |uncheck-icon| 
     - The Wallet must ensure that the Verifier cannot learn that the same User is using other Verifiers.

To mitigate Verifier/Verifier linkability for SD-JWT Credentials, one proposed solution is batch issuance, which involves using different key binding keys and salts for each Credential. However, the effectiveness of these methods has not yet been thoroughly evaluated, and is not available for IT Wallet yet.  

Security and Privacy Requirements
---------------------------------

SPR-E-50
~~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon| 
     - The Trust Framework must ensure that lifecycles of keys, certificates, and Credentials are designed such that the impact of a compromise is minimized.

The Credential lifecycle includes a Credential revocation mechanism based on Status Assertion [`OAUTH-STATUS-ASSERTION`_] that ensures that Credentials are properly revoked when compromised or outdated. 

The revocation of a Federation Entity (i.e., Issuer, Verifier, Wallet Provider) is instead possible by removing the corresponding Entity Statement, thus preventing misuse during compromise. 

.. tip::
  In addition, [`OID-FED`_] supports a historical key endpoint to retrieve the list of expired and revoked keys, with the motivation of the revocation. 

SPR-P-10
~~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon| 
     - The protocol must ensure that no third party can read the Credential issued by the Issuer.

To mitigate this threat, the IT Wallet specification requires the following security mechanisms in the issuance process:

- *TLS*: Used in all communication between the Wallet and the Issuer, ensuring that data in transit is encrypted and protected from interception by attackers.
- *Wallet Attestation*: Ensures that the Wallet operates on a secure, trusted device and complies with the security standards required by the Issuer, providing additional assurance that the Issuer is interacting with a legitimate Wallet Instance.
- *DPoP*: Ensures that the Holder of the access token possesses the private key associated with it, preventing attackers from reusing intercepted tokens.
- *Holder binding*: Ties the Credential to a specific Holder, ensuring that only the legitimate Holder can use a Credential to authenticate with the Issuer.
- *redirect_uri validation*: This validation ensures that the authorization response is sent to the correct and authorized endpoint, thereby preventing unauthorized interception by malicious actors. Ensuring the integrity of the **redirect_uri** is critical to avoid any manipulation or misdirection of the URI.  
- *PKCE*:  Avoids injection of a legit authorization **code** in another session. 

SPR-P-60
~~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon| 
     - The protocol must ensure that during an interaction with a Verifier, an attacker cannot read PII.

The IT Wallet complies with the requirements of P-60 by ensuring that all network connections are secured by TLS.

In addition, as the Authorization Response contains PII is important that it is not sent to an attacker-controlled endpoint. 
In the IT Wallet specification the **response_uri**, which is the endpoint where the Wallet sends the Authorization Response, is included in the signed Request Object, 
which is verified by the Wallet using the Verifier's public key and Trust Chain. This guarantees that the Authorization Response is being sent to the correct endpoint. 
Additionally, the Authorization Response is encrypted with the Verifier's public key, ensuring that only the intended recipient can decrypt and read the sensitive information, 
further securing the transmission.

Another endpoint to be validated is the **redirect_uri**, which is used to redirect the User back to the Verifier after the Credential presentation is complete. 
In the IT Wallet specification, the **redirect_uri** is registered and validated beforehand during the Verifier onboarding using OpenID Federation. During the presentation 
phase, the Wallet is able to validate this value by verifying the OpenID Federation Trust Chain related to the Verifier. 

In order to be sure that the **redirect_uri** is received from a legit Wallet and not from the attacker, the Verifier response endpoint upon the recipient of a valid 
authorization response creates a fresh cryptographic value that is linked to the authorization response and attaches it to the **redirect_uri** that is sent to the Wallet. 
When the Verifier receives the redirect, it can extract the response code and check with its response endpoint whether the response code was associated with this Authorization 
Response. (See :ref:`Redirect URI Section <Redirect URI>`).  

SPR-P-70
~~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon| 
     - The protocol must ensure that during an interaction with an Issuer, an attacker cannot read PII.

In the issuance process, as the Credential inside a Credential Response contains PII, it is required that the Credential is not sent to or intercepted by an attacker. 
To mitigate these threats, the IT Wallet specification requires the following security mechanisms:

- *TLS*: Used in all communication between the Wallet and the Issuer, ensuring that data in transit is encrypted and protected from interception by attackers.
- *Wallet Instance Attestation*: Ensures that the Wallet operates on a secure, trusted device and complies with the security standards required by the Issuer, providing additional assurance that the Issuer is interacting with a legitimate Wallet Instance.
- *DPoP*: Ensures that the Holder of the access token possesses the private key associated with it, preventing attackers from reusing intercepted tokens.
- *Holder binding*: Ties the Credential to a specific Holder, ensuring that only the legitimate Holder can use a Credential to authenticate with the Issuer.
- *redirect_uri validation*: This validation ensures that the authorization response is sent to the correct and authorized endpoint, thereby preventing unauthorized interception by malicious actors. Ensuring the integrity of the **redirect_uri** is critical to avoid any manipulation or misdirection of the URI.  
- *PKCE*:  Avoids injection of a legit authorization **code** in another session. 

.. tip::
  A further security enhancement that could be applied to add an extra layer of protection for sensitive User information is the encryption of Credential responses. 
  OpenID4VCI standard provides the option for the Wallet to request encrypted Credentials containing PII by including a **credential_response_encryption** object in its request. 

.. note::
  Currently, no explicit security and privacy measures related to this requirement are specified in [`OpenID4VC-SecTrust`_], it remains a TODO. 

SPR-P-80
~~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon| 
     - The protocol must ensure that the Issuer cannot learn where the User uses the Credential.

The exchange protocol does not require any interactions between Verifiers and Issuers. In addition, privacy-preserving Status Assertions, presented along with Credentials, 
ensure that while the Verifier checks the Credential's validity, the Issuer does not learn where or when the Credential is being used.

SPR-W-50
~~~~~~~~
.. list-table:: 
   :widths: 8 92

   * - |check-icon| 
     - The Wallet must ensure that the Credentials and private keys are protected from unauthorized access.

To prevent unauthorized access to the Wallet, it is unlocked on the User's device by entering a personal identification number (PIN) or using biometric authentication, such as fingerprint or facial recognition, based on the User's preferences and the device's capabilities. Additionally, the cryptographic keys are securely stored within the WSCD, ensuring that only the User can access them, thereby preventing unauthorized use or tampering.


