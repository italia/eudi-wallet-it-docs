.. include:: ../common/common_definitions.rst

.. _revocation-lists:

Credential Revocations
++++++++++++++++++++++

The value of digital credentials is contingent on their validity.
A credential that has been revoked, due to legal requirements, inaccuracy or compromise, is not only valueless but potentially harmful. 
For these reason a robust mechanism for managing the validity and revocation of digital credentials is required.

This section outlines the key technical requirements and processes related to the revocation of the digital credentials. 
Furthermore, it provides the technical details that the Relying Parties MUST implement to verify, in a secure and reliable manner, 
the validity of a digital credential during the presentation phase.

This section is structured into several subsections, these are listed below.

* The "Key Technical Requirements" subsection outlines the fundamental requirements for managing digital credential revocation. These requirements define the roles and responsibilities of the Authentic Source, the Issuer, and the Wallet Instance in ensuring the validity of credentials and managing their revocation.
* The "Presentation" subsection describe the processes by which a Wallet Instance and a Relying Party interacts with each other to demonstrate and verify the non-revocation status of the presented digital credentials. These subsections detail how a Non-Revocation Attestation, in the form of a cryptographic proof that the credential has not been revoked, is created, provided, and validated.
* The "Non-Revocation Attestation Renewal Flow" and "Credential Revocation Flow" subsections provide detailed workflows for renewing a Non-Revocation Attestation and revoking a credential, respectively. These workflows include the generation and verification of a Proof of Possession (PoP) JWT, which proves that the Wallet Instance possesses the private key associated with the digital credential.


Key Technical Requirements
---------------------------

- The Authentic Source is the provider of the data necessary for the issuance of a digital credential requested by PID/(Q)EAA Provider. 
- The revocation requests MAY be communicated to PID/(Q)EAA Provider by Users using their personal Wallet Instance (Holder).
- The revocation requests MAY be communicated to Authentic Source from the following entities:
    - A legal entity (e.g., Police for reporting) on behalf of the User.
    - The Authentic Source itself (e.g., for attribute updates) following administrative purposes.
    - A legal entity for the performance of their functions and any other judicial reasons (e.g., Police).
- The Authentic Source MUST maintain a record of the PID/(Q)EAA Provider who have requested the User's data for the issuance of the digital credential related to the User. 
- The PID/(Q)EAA Provider MUST provide a protected web endpoint where the Authentic Source MAY notify any updates related to the User's data, having the Authentic Source the record of PID/(Q)EAA Providers that have requested Users data for the issuance of the digital credentials.
- The PID/(Q)EAA Provider MUST provide to the Holder the non-revocations attestation related to the digital credential it has issued to the Holder.
- The Non-Revocation Attestation provides the proof about the non-revocation of the digital credential which is related to.
- The Non-Revocation Attestation MUST be verifiable with a cryptographic signature.
- The Non-Revocation Attestation does not reveal any information about the Relying Party or the User's data contained in the digital credential the attestation is related to.


Presentation Phase
------------------

The Wallet Instance, according to the presentation request from the Relying Party, 
produces a Verifiable Presentation (VP) token with the digital credential 
and a Non-Revocation Attestation. This attestation is the proof that the credential has not been revoked.

The Relying Party MUST validate the VP token and the Non-Revocation Attestation to certify the validity of a digital credential.

Non-revocation Attestation Issuance
-----------------------------------

The Wallet Instance sends a request for a digital credential to the PID/(Q)EAA Provider.

Upon successful request, the Wallet Instance receives:
* The digital credential;
* a Non-Revocation Attestation.

The Non-Revocation Attestation MUST be presented in conjunction with the digital credential. The Non-Revocation Attestation MUST be timestamped with its issuance datetime, always referring to a previous period.
The Non-Revocation Attestation MUST contain the expiration datetime after which the digital credential MUST NOT be considered valid anymore.
Relying Parties determine the validity duration of the Non-Revocation Attestation based.
The Non-Revocation Attestation enables offline use cases and potential unavailability of the in the non-revocation certification systems.

Non-Revocation Attestation Flow
-------------------------------

.. code-block:: mermaid

    sequenceDiagram
        participant WalletInstance as Wallet Instance
        participant digital credentialIssuer as PID/(Q)EAA Provider
        WalletInstance->>digital credentialIssuer: Send Non-Revocation Attestation Request<br> providing the digital credentials and<br> the cryptoghraphic proof of possession of it.
        digital credentialIssuer->>digital credentialIssuer: Verify digital credential PoP
        digital credentialIssuer->>digital credentialIssuer: Creates the Non-Revocation Attestation<br> (if the previous step is valid)
        digital credentialIssuer->>WalletInstance: Send Response containing the Non-Revocation Attestation

1. **Non-Revocation Attestation Request**: The Wallet Instance initiates the process by creating a Non-Revocation Attestation Request. This request includes the digital credential for which the Non-Revocation Attestation is related to and a PoP JWT. The PoP JWT is signed with the private key associated with the digital credential, and MUST include claims such as `iss`, `aud`, `exp`, `iat`, and `jti`.

2. **Send Request to PID/(Q)EAA Provider**: The Wallet Instance sends the Non-Revocation Attestation Request to the PID/(Q)EAA Provider Non-Revocation issuance endpoint. The Holder is authenticated using the PoP JWT (see [Proof of Possession (PoP) JWT generation process](#proof-of-possession-pop-jwt-generation-process)), which proves that the Wallet Instance possesses the private key associated with the digital credential.

3. **Verify PoP**: The PID/(Q)EAA Provider verifies the PoP by checking the signature of the PoP JWT using the public key that was used when the digital credential was issued. If the verification is successful, it means that the Wallet Instance possesses the private key associated with the digital credential, and therefore has the authority to request its renewal.

4. **Renew Non-Revocation Attestation**: If the PoP is verified successfully, the PID/(Q)EAA Provider renews the Non-Revocation Attestation with the digital credential included in the Non-Revocation Attestation Renewal Request.

5. **Send Response**: The PID/(Q)EAA Provider sends a response back to the Wallet Instance indicating the result of the request. If the renewal is successful, the response includes the renewed Non-Revocation Attestation. If not, the response includes an error message describing the unavailability of the Non-Revocation Attestation and any additional information about the cause of that MAY be included in the `error_description`.

Upon successful request, the Wallet Instance receives the Non-Revocation Attestation.

This process ensures that the Wallet Instance is the legitimate owner of the digital credential and has the authority to request its Non-Revocation Attestation. It does so by signing the request and having the Issuer verify this signature using the corresponding public key boun with the related digital credetial. This ensures that the Wallet Instance is authenticated and has the digital credential which is requesting the Non-Revocation Attestation.

Non-Revocation Attestation Request
----------------------------------

The Wallet Instance provides the parameters listed below to the PID/(Q)EAA Provider Non-Revocation Attestation endpoint using the ``request`` parameter to prevent Request URI swapping attack.

The Wallet Instance signs the signed request using the private key that was created to obtain the digital credential, as provided within the digital credential ``cnf.jwk`` claim.

The signed request JWT contains a JOSE header with ``alg``, ``kid``, and ``typ`` parameters, and a body with ``iss``, ``aud``, ``exp``, ``iat``, and ``jti`` claims.

    - ``alg``: A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section `Cryptographic Algorithms <algorithms.html>`_ and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
    - ``kid``: Unique identifier of the ``jwk`` inside the ``cnf`` claim of Wallet Instance Attestation as base64url-encoded JWK Thumbprint value.
    - ``typ``: It MUST be set to ``jwt-client-attestation-pop``
    - ``iss``: Thumbprint of the JWK in the ``cnf`` parameter.
    - ``aud``: It MUST be set to the identifier of the PID/(Q)EAA Provider.
    - ``exp``: UNIX Timestamp with the expiry time of the JWT.
    - ``iat``: UNIX Timestamp with the time of JWT issuance.
    - ``jti``: Unique identifier for the DPoP proof JWT. The value SHOULD be set using a *UUID v4* value according to RFC 4122.

The PID/(Q)EAA Provider MUST verify the Proof of Possession by checking the signature of the request using the public key provided in the digital credential ``cnf.jwk`` claim.

TBD: the typ value in the JWT header configuring the content type of the request (Non-Revocation Attestation request).

Credential Revocation Request Flow
----------------------------------

.. code-block:: mermaid

    sequenceDiagram
        participant WalletInstance as Wallet Instance
        participant digital credentialIssuer as PID/(Q)EAA Provider
        WalletInstance->>digital credentialIssuer: Send Non-Revocation Attestation Request
        digital credentialIssuer->>digital credentialIssuer: Verify credential PoP
        digital credentialIssuer->>digital credentialIssuer: Revoke digital credential (if PoP is valid)
        digital credentialIssuer->>WalletInstance: Send Response

1. **Credential Revocation Request**: The Wallet Instance initiates the process by creating a Credential Revocation Request. This request includes the ID of the digital credential to be revoked and a PoP JWT. The PoP JWT is signed with the private key associated with the digital credential to be revoked, and includes claims such as `iss`, `aud`, `exp`, `iat`, and `jti`.

2. **Send Request to PID/(Q)EAA Provider**: The Wallet Instance sends the Credential Revocation Request to the PID/(Q)EAA Provider's revocation endpoint. The request is authenticated using the PoP JWT, which proves that the Wallet Instance possesses the private key associated with the digital credential.

3. **Verify PoP**: The PID/(Q)EAA Provider verifies the PoP by checking the signature of the PoP JWT using the public key that was used when the digital credential was issued. If the verification is successful, it means that the Wallet Instance possesses the private key associated with the digital credential, and therefore has the authority to request its revocation.

4. **Revoke digital credential**: If the PoP is verified successfully, the PID/(Q)EAA Provider revokes the digital credential identified by the ID in the Credential Revocation Request.

5. **Send Response**: The PID/(Q)EAA Provider sends a response back to the Wallet Instance indicating the result of the revocation request. If the revocation was successful, the response includes a confirmation of the revocation.


Digital Credential Revocation Request
-------------------------------------

TBD.


External references
-------------------

- OpenID for Verifiable Presentations - draft 20 <https://openid.net/specs/openid-4-verifiable-presentations-1_0.html>_
- OAuth 2.0 Demonstrating Proof-of-Possession at the Application Layer (DPoP) <https://datatracker.ietf.org/doc/html/draft-ietf-oauth-dpop>_
- Dynamic status lists <https://api-pilot.ebsi.eu/docs/specs/credential-status-framework/credential-status-vc-schemas>_
- JWT and CWT Status List <https://vcstuff.github.io/draft-looker-oauth-jwt-cwt-status-list/draft-looker-oauth-jwt-cwt-status-list.html>_
