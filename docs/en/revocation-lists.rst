.. include:: ../common/common_definitions.rst

.. _revocation-lists:

Credential validity and non-revocation attestations
+++++++++++++++++++++++++++++++++++++++++++++++++++

This section outlines the key technical requirements and processes related to the validity and non-revocation of digital credentials. It provides a comprehensive guide on how to manage, verify, and revoke digital credentials in a secure and reliable manner. 

The value of verifiable credentials is contingent on their validity. A credential that has been revoked, due to legal requirements, inaccuracy or compromise, is not only valueless but potentially harmful. Therefore, robust mechanisms for managing the validity and revocation of credentials are crucial.

This section is structured into several subsections, each addressing a different aspect of credential validity and revocation.

The "Key Technical Requirements" subsection outlines the fundamental requirements for managing credential validity and revocation. These requirements define the roles and responsibilities of the Authentic Source, the Issuer, and the Wallet Instance in ensuring the validity of credentials and managing their revocation.

The "Presentation" and "Issuance" subsections describe the processes by which a Wallet Instance responds to a presentation request and initiates a request for a digital credential, respectively. These subsections detail how a non-revocation attestation, a proof that the credential has not been revoked, is created, presented, and validated.

The "Non-Revocation Attestation Renewal Flow" and "Credential Revocation Flow" subsections provide detailed workflows for renewing a non-revocation attestation and revoking a credential, respectively. These workflows include the generation and verification of a Proof of Possession (PoP) JWT, which proves that the Wallet Instance possesses the private key associated with the VC.


Key Technical Requirements
---------------------------

- The Authentic Source MUST be the only source of truth for credential validity. All revocation requests MUST be communicated to the Authentic Source using appropriate channels. These requests MAY come from:
    - The citizen (Holder) via their personal Wallet Instance.
    - The citizen via a legal entity (e.g., Police for reporting).
    - The citizen directly via the Authentic Source.
    - The Authentic Source itself (e.g., for attribute updates).
    - A legal entity (e.g., Police for seizure).
- The Authentic Source MUST maintain a record of the issuers who have issued a certain credential. 
- The Issuer MUST provide information about a callback hook for revocation.
- The Authentic Source MUST manage the revocation of issued credentials by notifying the respective issuers.
- The Authentic Source MUST maintain a mapping between ID_CREDENTIAL and ID_ISSUER to facilitate credential revocation even in case of Wallet Instance loss.
- The revocation MUST be verifiable via a cryptographic signature.


Presentation
------------

The Wallet Instance responds to a presentation request from the Relying Party. It produces a Verifiable Presentation (VP) token with the digital credential and a non-revocation attestation. This attestation is a proof that the credential has not been revoked.

It is timestamped with the request date and always refers to a previous period. Importantly, this attestation does not reveal any information about the Relying Party. The Relying Party then evaluates and validates the response, the VP token, and the non-revocation attestation.

Issuance
--------

The Wallet Instance initiates a request for a digital credential from the Credential Issuer.

Upon successful request, the Wallet Instance receives:
- The digital credential
- A non-revocation attestation

The non-revocation attestation is presented in conjunction with the credential. The attestation is timestamped with the request date, not the authentication date, and always refers to a previous period.
Relying Parties determine the validity duration of this attestation based on the specific use case.
By default, an attestation is considered valid if issued within the previous 350 hours. This provision supports offline use cases and potential disruptions or incidents in the certification systems. Note that this delay only refers to the non-revocation of the credential, while the validity of the credential itself can always be verified.

Non-Revocation Attestation Renewal Flow
---------------------------------------

.. code-block:: mermaid

    sequenceDiagram
        participant WalletInstance as Wallet Instance
        participant VCIssuer as VC Issuer
        WalletInstance->>VCIssuer: Send Non-Revocation Attestation Renewal Request
        VCIssuer->>VCIssuer: Verify credential PoP
        VCIssuer->>VCIssuer: Renew Non-Revocation Attestation (if PoP is valid)
        VCIssuer->>WalletInstance: Send Response

1. **Non-Revocation Attestation Renewal Request**: The Wallet Instance initiates the process by creating a Non-Revocation Attestation Renewal Request. This request includes the ID of the VC for which the non-revocation attestation is to be renewed and a PoP JWT. The PoP JWT is signed with the private key associated with the VC, and includes claims such as `iss`, `aud`, `exp`, `iat`, and `jti`.

2. **Send Request to VC Issuer**: The Wallet Instance sends the Non-Revocation Attestation Renewal Request to the VC Issuer's renewal endpoint. The request is authenticated using the PoP JWT (see [Proof of Possession (PoP) JWT generation process](#proof-of-possession-pop-jwt-generation-process)), which proves that the Wallet Instance possesses the private key associated with the VC.

3. **Verify PoP**: The VC Issuer verifies the PoP by checking the signature of the PoP JWT using the public key that was used when the VC was issued. If the verification is successful, it means that the Wallet Instance possesses the private key associated with the VC, and therefore has the authority to request its renewal.

4. **Renew Non-Revocation Attestation**: If the PoP is verified successfully, the VC Issuer renews the non-revocation attestation for the VC identified by the ID in the Non-Revocation Attestation Renewal Request.

5. **Send Response**: The VC Issuer sends a response back to the Wallet Instance indicating the result of the renewal request. If the renewal was successful, the response includes the renewed non-revocation attestation.

.. code-block:: python

    # Step 1: Create Non-Revocation Attestation Renewal Request
    attestation_renewal_request = {
        "vc_id": "ID of the VC to be renewed",
        "pop_jwt": "PoP JWT signed with the private key associated with the VC"
    }

    # Step 2: Send Request to VC Issuer
    response = send_request_to_vc_issuer(attestation_renewal_request)

    # Step 3: VC Issuer verifies the PoP
    is_pop_valid = verify_pop(attestation_renewal_request["pop_jwt"])

    if is_pop_valid:
        # Step 4: Renew Non-Revocation Attestation
        renew_attestation(attestation_renewal_request["vc_id"])
        
        # Step 5: Send Response
        response = {
            "status": "success",
            "message": "Non-revocation attestation renewed successfully"
        }
    else:
               response = {
            "status": "failure",
            "message": "PoP verification failed"
        }


Upon successful request, the Wallet Instance receives:
- The renewed non-revocation attestation

This process ensures that the Wallet Instance is the legitimate owner of the digital credential and has the authority to request its renewal. It does so by signing the request and having the Issuer verify this signature using the corresponding public key. This ensures that the Wallet Instance is authenticated and has a PID.

Proof of Possession (PoP) JWT generation process
------------------------------------------------

The Wallet Instance generates a Proof of Possession (PoP) JWT as follows:

1. **Create PKCE code verifier**: The Wallet Instance creates a fresh PKCE code verifier, Wallet Instance Attestation Proof of Possession, and ``state`` parameter for the *Pushed Authorization Request*.

2. **Send parameters to PID/(Q)EAA Provider**: The Wallet Instance provides these parameters to the PID/(Q)EAA Provider PAR endpoint using the ``request`` parameter to prevent Request URI swapping attack.

3. **Generate code_verifier**: The Wallet Instance must create the ``code_verifier`` with enough entropy random string using the unreserved characters with a minimum length of 43 characters and a maximum length of 128 characters. This makes it impractical for an attacker to guess its value. The value must be generated following the recommendation in Section 4.1 of :rfc:`7636`. 

4. **Sign the request**: The Wallet Instance signs this request using the private key that was created during the setup phase to obtain the Wallet Instance Attestation. The related public key that is attested by the Wallet Provider is provided within the Wallet Instance Attestation ``cnf`` claim.

5. **Create PoP**: The Proof of Possession JWT contains a JOSE header with ``alg``, ``kid``, and ``typ`` parameters, and a body with ``iss``, ``aud``, ``exp``, ``iat``, and ``jti`` claims.

    - ``alg``: A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section `Cryptographic Algorithms <algorithms.html>`_ and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
    - ``kid``: Unique identifier of the ``jwk`` inside the ``cnf`` claim of Wallet Instance Attestation as base64url-encoded JWK Thumbprint value.
    - ``typ``: It MUST be set to ``jwt-client-attestation-pop``
    - ``iss``: Thumbprint of the JWK in the ``cnf`` parameter.
    - ``aud``: It MUST be set to the identifier of the PID/(Q)EAA Provider.
    - ``exp``: UNIX Timestamp with the expiry time of the JWT.
    - ``iat``: UNIX Timestamp with the time of JWT issuance.
    - ``jti``: Unique identifier for the DPoP proof JWT. The value SHOULD be set using a *UUID v4* value according to RFC 4122.

6. **Set client_assertion parameter**: The ``client_assertion`` parameter in the Token Request is set to a value containing the Wallet Instance Attestation and the Proof of Possession, separated with the ``~`` character.

7. **Verify PoP**: The PID/(Q)EAA Provider then verifies the Proof of Possession by checking the signature of the request using the public key provided in the Wallet Instance Attestation ``cnf`` claim.
    
Credential Revocation Flow
--------------------------

.. code-block:: mermaid

    sequenceDiagram
        participant WalletInstance as Wallet Instance
        participant VCIssuer as Issuer
        WalletInstance->>VCIssuer: Send Credential Revocation Request
        VCIssuer->>VCIssuer: Verify credential PoP
        VCIssuer->>VCIssuer: Revoke VC (if PoP is valid)
        VCIssuer->>WalletInstance: Send Response

1. **Credential Revocation Request**: The Wallet Instance initiates the process by creating a Credential Revocation Request. This request includes the ID of the VC to be revoked and a PoP JWT. The PoP JWT is signed with the private key associated with the VC to be revoked, and includes claims such as `iss`, `aud`, `exp`, `iat`, and `jti`.

2. **Send Request to VC Issuer**: The Wallet Instance sends the Credential Revocation Request to the VC Issuer's revocation endpoint. The request is authenticated using the PoP JWT, which proves that the Wallet Instance possesses the private key associated with the VC.

3. **Verify PoP**: The VC Issuer verifies the PoP by checking the signature of the PoP JWT using the public key that was used when the VC was issued. If the verification is successful, it means that the Wallet Instance possesses the private key associated with the VC, and therefore has the authority to request its revocation.

4. **Revoke VC**: If the PoP is verified successfully, the VC Issuer revokes the VC identified by the ID in the Credential Revocation Request.

5. **Send Response**: The VC Issuer sends a response back to the Wallet Instance indicating the result of the revocation request. If the revocation was successful, the response includes a confirmation of the revocation.

Here's a code block that outlines the flow:

.. code-block:: python

    # Step 1: Create Credential Revocation Request
    credential_revocation_request = {
        "vc_id": "ID of the VC to be revoked",
        "pop_jwt": "PoP JWT signed with the private key associated with the VC"
    }

    # Step 2: Send Request to VC Issuer
    response = send_request_to_vc_issuer(credential_revocation_request)

    # Step 3: VC Issuer verifies the PoP
    is_pop_valid = verify_pop(credential_revocation_request["pop_jwt"])

    if is_pop_valid:
        # Step 4: Revoke VC
        revoke_vc(credential_revocation_request["vc_id"])
        
        # Step 5: Send Response
        response = {
            "status": "success",
            "message": "VC revoked successfully"
        }
    else:
        response = {
            "status": "failure",
            "message": "PoP verification failed"
        }




External references
-------------------

- OpenID for Verifiable Presentations - draft 20 <https://openid.net/specs/openid-4-verifiable-presentations-1_0.html>_
- OAuth 2.0 Demonstrating Proof-of-Possession at the Application Layer (DPoP) <https://datatracker.ietf.org/doc/html/draft-ietf-oauth-dpop>_
- Dynamic status lists <https://api-pilot.ebsi.eu/docs/specs/credential-status-framework/credential-status-vc-schemas>_
- JWT and CWT Status List <https://vcstuff.github.io/draft-looker-oauth-jwt-cwt-status-list/draft-looker-oauth-jwt-cwt-status-list.html>_
