.. include:: ../common/common_definitions.rst

.. _sec_revocation_intro:

Credential Revocations
++++++++++++++++++++++

The value of digital credentials is contingent on their validity.
A credential that has been revoked, due to legal requirements, inaccuracy or compromise, is not only valueless but potentially harmful. 
For these reasons a robust mechanism for managing the validity and revocation of digital credentials is required.

This section outlines the key technical requirements and processes related to the revocation of the digital credentials. 
Furthermore, it provides the technical details that the Relying Parties MUST implement to verify, in a secure and reliable manner, 
the validity of a digital credential during the presentation phase.

This section is structured into several subsections, these are listed below.

* The :ref:`"General Assumptions" <sec_revocation_assumption>` subsection outlines the main assumptions relevant to the design of a suitable solution for the main revocation scenarios.
* The :ref:`"Requirements" <sec_revocation_requirements>` subsection outlines basic requirements, particularly regarding security and privacy aspects.
* The :ref:`"Entities Relationship" <sec_revocation_entity_relationship>` describes the roles and responsibilities of the main entities involved in ensuring the validity of credentials and managing their revocation.
* The :ref:`"High Level Revocation Flow" <sec_revocation_high_level_flow>` subsection outlines the main revocation scanarios and relevant processes.   
* The :ref:`"Wallet Instance Initiated Revocation Flow" <sec_revocation_wi_initiated_flow>` subsections outline how Wallet Instances request a revocation of a given credential to Issuers.
* The :ref:`"Non-Revocation Attestation Request" <sec_revocation_nra_request>` subsections decribe how the Wallet Instance interacts with the Issuer to obtain a Non-Revocation Attestation related to a credential own by the Holder. 
* The :ref:`"Non-Revocation Proof during the Presentation Phase" <sec_revocation_nra_presentation>` subsection details how a Non-Revocation Attestation, in the form of a cryptographic proof that the credential has not been revoked, is provided by the Wallet Instance to the Verifier requesting a credential.



.. _sec_revocation_assumption:

General Assumptions
-------------------

A Credential Issuer is in charge of the creation and the issuance of credentials, its lifecycle, and ultimately, its validity status. Some credentials may have regulatory value given by national or european laws, therefore also revocations of credentials MUST be non-repudiable.
Some credentials may be a digital representation of a physical document issued, under a well defined national law, by an Authentic Source which, in the Wallet Ecosystem, acts as a repository or system that contains attributes and provides them to the Issuer. For this reason, an exchange of information between the two entities is required not only for the issuing the credential but also for the proper handling of its revocation.
Moreover, due to digital signature of the credentials, any updates on them MUST result in a re-issuance.
Finally, it is assumed that, to facilitate the association between physical document and digital credentials, the identifier of the physical document is always present as an attribute within the digital credentials.



.. _sec_revocation_requirements:

Requirements
------------

General Requirements
^^^^^^^^^^^^^^^^^^^^
 
- The Issuer MUST be the only responsible for the lifecycle of credentials including the revocation status.
- Credentials SHOULD be updates whenever one or more attributes are changed.
- Any credential update MUST result in a new fresh issuance of it, following the principle that the credential SHOULD always have updated data. In this case, the old Credentials of the same type MUST be revoked. 
- The revocation of a credential for technical reasons (loss or theft of the device, compromise of cryptographic keys) MAY not have an impact on any other digital credentials issued of the same type and MUST NOT lead to the revocation of a physical document associated with it.
- The revocation of a physical document which one or more Credentials are associated with MUST result in their revocation.
- The revocation requests of a credential MAY be communicated to the Issuer by 

    - Holders using their personal Wallet Instance.
    - Authentic Sources (e.g., for attribute updates) following administrative purposes. 
    - Law-Enforcing Bodies for the fulfillment of their functions and any other judicial reasons (e.g., Police).
- The revocation requests of a physical document MAY be communicated to Authentic Source by:

    - A Law-Enforcing Body (e.g., Police) on behalf of the User or directly for the fulfillment of their functions and any other judicial reasons.
    - The Holder using any out-of-band procedure in force by national regulations.
- The Authentic Source MUST provide an interface for the data sharing regarding the attributes update and revocation status of a physical document the credential is associated with.
- The Issuer MUST provide an interface handling the revocation flows (Revocation request/response, data access regarding the revocation status of a credential, etc.).
- The Issuer MUST provide the Wallet Instance with a proof of non-revocation of a given Holder's credential (Non-Revocation Attestation).
- The Holders MAY provide the Verifiers with a proof of non-revocation of their Credentials (Non-Revocation Attestations).
- The Verifiers MAY require a proof of non-revocation, even in the future after the credential presentation, for the fulfillment of their functions and for any other regulatory reasons (deferred).


Security Requirements
^^^^^^^^^^^^^^^^^^^^^

- The proof of non-revocation (Non-Revocation Attestation) MUST be cryptographically verifiable, so that it can be shown to have been issued by the Issuer and not to have been tampered with.
- The Non-Revocation Attestation MUST be non-repudiable even beyond its expiration time and even in the face of any rotations of the cryptographic keys.
- Granting of the proof of non-revocation (Non-Revocation Attestation) MUST be allowed only to authorized entities (e.g. by the Holder or by law).


Privacy Requirements
^^^^^^^^^^^^^^^^^^^^

- The Authentic Source MUST store in local databases only the minimum information required to notify the Issuer of a change in attributes or a change in the validity status of a physical document associated with one or more credentials.
- Access to credential status information by a Verifier MUST be authorized by the Holder, except for checks carried out by Law-Enforcement Bodies on a regulatory basis. 
- The Issuer SHOULD not directly or indirectly have any information related to the Verifier, type of credentials, and Holder such that it is impossible to track the Holder's usage of the Credentials.
- A proof of non-revocation (Non-Revocation Attestation) provided by the Issuer, in whatever format it is, SHOULD NOT reveal any information about the Verifier nor the User's attributes contained in the credential the attestation is related to.



.. _sec_revocation_entity_relationship:

Entities Relationship
---------------------

The entities involved in the main revocation processes are depicted in the diagram below. 

.. _fig_revocation_entity_relationship:
.. figure:: ../../images/revocation-entity-relationship.svg
    :figwidth: 80%
    :align: center

    Entity-Relationship diagram in the revocation scenario

The revocation scenarios involve two main flows:

    - The Revocation Request flow: this flow describes how an entity requests for a credential revocation to the Issuer of that credential. 
    - The Non-Revocation Attestation Request flow: this flow defines the technical protocol for requesting and obtaining a Non-Revocation Attestation and how the Wallet Instance will share it with a Verifier as a proof of validity of a credential.



.. _sec_revocation_high_level_flow:

High Level Revocation Flow
--------------------------

A Credential Revocation Flow can start under different scenarios:

    - The Holders report the loss or theft of their own physical document to the Law-Enforcement Authorities: this implies that the credentials, if any, shall be revoked.
    - The Holders notify an Authentic Source that one or more attributes are changed (e.g. the current resident address): in this case the Credentials shall be revoked, as they are no longer valid due to the change in attributes. 
    - The Holders who no longer have access to their Wallet Instance (e.g. theft or loss of the device), may request the Issuer of the credentials to revoke them.
    - The Law-Enforcing Authorities, for the fulfillment of their functions and any other judicial reasons, may request the Authentic Source to revoke entitlements, licences, certificates, identification documents, etc., which in turn leads to the revocation of any linked Credentials.
    - The Authentic Sources that for any administrative reasons update one or more attributes of a Holder, shall inform the Issuer of related Credentials. 
    - The Issuers, for technical security reasons (e.g. in the case of compromised cryptographic keys), can decide to revoke the Credentials.

The Figure below shows the main processes involved in the scenarios described above

.. _fig_revocation_processes:
.. figure:: ../../images/revocation-processes.svg
    :figwidth: 100%
    :align: center

    High-Level Revocation Processes and main scenarios

Some of the sub-processes involved in the above scenarios are already well defined by national laws. 
The susequent section defines the protocol interface between the Wallet Instance and the Issuer during the revocation request. The communication between the Authenitc Source and the Issuer is out of scope of this technical implementation profile.



.. _sec_revocation_wi_initiated_flow:

Wallet Instance Initiated Revocation Flow
-----------------------------------------

A Wallet Instance MUST request the revocation of a credential as defined below.

.. _fig_Low-Level-Flow-Revocation:
.. figure:: ../../images/Low-Level-Flow-Revocation.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/PP11ImD134Rlyoj2yQ1WyIvKAfxgPGSjxaLOucw4q6bcd6HSlFZRZHLRnEjx7xoGjHfMQ_iKi5cMjd-X6eeZ7hcW62nwJ8aCDk9B6Ma1g33ptyr6jL4zA0vXPbZU05z3x1wtS5NfFUy8AhqrKZiVAqqanfY6KdD-NPtT7KdCyRxVNiAOsC60gkILB8Dz5FgFL_tczZDsyIBy5fymyOH6u6Rf1fu5PO9J0HmUrmy_bvtijt4r7voMB4hGxSAQPF8NVG40
    
    Wallet Instance Initiated Revocation Flow

**Step 1 (Credential Revocation Request)**: The Wallet Instance initiates the process by creating a Credential Revocation Request. This request includes the Wallet Instance Attestation with its Proof of Possession and a Credential Proof of Possession as a JWT. It MUST be signed with the private key related to the public key contained within the credential (Issuer Signed JWT). Then, the Wallet Instance sends the request to the Issuer as in the following non-normative example.

.. _credential_revocation_request_ex:
.. code-block::
    
    POST /revoke HTTP/1.1
    Host: pid-provider.example.org
    Content-Type: application/x-www-form-urlencoded

    credential_proof=$CredentialPoPJWT
    &client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-client-attestation
    &client_assertion=$WIA~WIA-PoP

where a non-normative example of a Credential PoP JWT is given by

.. _credential_pop_jwt_ex:
.. code-block::

    {
        "alg": "ES256",
        "typ": "revocation-request+jwt",
        "kid": "$WIA-CNF-JWKID"

    }
    .
    {
        "iss": "0b434530-e151-4c40-98b7-74c75a5ef760",
        "aud": "https://pid-provider.example.org",
        "iat": 1698744039,
        "exp": 1698744139, 
        "jti": "6f204f7e-e453-4dfd-814e-9d155319408c",
        "format": "vc+sd-jwt",
        "credential": "$Issuer-Signed-JWT"
    }

**Step 2 (PoP verification)**: The Issuer verifies the signature of the PoP JWTs using the public key that was attested in the Wallet Instance Attestation and the credential. If the verification is successful, it means that the Wallet Instance owns the private keys associated with the Wallet Instance Attestation and credential, and therefore is entitled to request its revocation.

**Step 3 (Credential Revocation)**: The Issuer revokes the credential provided in the Credential PoP JWT. After the revocation, the Issuer MAY also send a notification to the Holder (e.g. using a Holder contact certified during the issuance phase), with all needed information related to the credential revocation status update. This communication is out of scope of the current technical implemetation profile. 

**Step 4 (Credential Revocation Response)**: The Issuer sends a response back to the Wallet Instance with the result of the revocation request.

.. code::

    .. code-block:: http

    HTTP/1.1 204 No Content


Credential Revocation HTTP Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The requests to the *Issuer Revocation endpoint* MUST be HTTP with method POST, using the mandatory parameters listed below within the HTTP request message body. These MUST be encoded in ``application/x-www-form-urlencoded`` format.

.. _table_revocation_request_params: 
.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **credential_proof**
      - It MUST contain a JWT proof of possession of the cryptographic key the credential to be revoked shall be bound to. 
      - This specification
    * - **client_assertion_type**
      - It MUST be set to ``urn:ietf:params:oauth:client-assertion-type:jwt-client-attestation``.
      - `oauth-attestation-draft <https://vcstuff.github.io/draft-ietf-oauth-attestation-based-client-auth/draft-ietf-oauth-attestation-based-client-auth.html>`_.
    * - **client_assertion**
      - It MUST be set to a value containing the Wallet Instance Attestation JWT and the Proof of Possession, separated with the ``~`` character. 
      - `oauth-attestation-draft <https://vcstuff.github.io/draft-ietf-oauth-attestation-based-client-auth/draft-ietf-oauth-attestation-based-client-auth.html>`_.

The Revocation Endpoint MUST be provided by the Issuer within its Metadata. 

The Credential Proof of Possession MUST be a JWT that MUST contain the paramters (JOSE Header and claims) in the following table.

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **typ**
      - It MUST be set to ``revocation-request+jwt``
      - :rfc:`7516#section-4.1.1`, the value is defined within this specification
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section `Cryptographic Algorithms <algorithms.html>`_ and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      -  Unique identifier of the ``jwk`` inside the ``cnf`` claim of the credential to be revoked, as base64url-encoded JWK Thumbprint value.
      - :rfc:`7638#section_3`. 

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - Thumbprint of the JWK in the ``cnf`` parameter of the Wallet Instance Attestation.
      - :rfc:`9126` and :rfc:`7519`.
    * - **aud**
      - It MUST be set to the identifier of the Issuer.
      - :rfc:`9126` and :rfc:`7519`.
    * - **exp**
      - UNIX Timestamp with the expiry time of the JWT.
      - :rfc:`9126` and :rfc:`7519`.
    * - **iat**
      - UNIX Timestamp with the time of JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **jti**
      - Unique identifier for the PoP proof JWT. The value SHOULD be set using a *UUID v4* value according to [:rfc:`4122`].
      - [:rfc:`7519`. Section 4.1.7].
    * - **credential_format**
      - The data format of the credential to be revoked. It MUST be set to ``vc+sd-jwt`` or ``vc+mdoc``
      - This specification.
    * - **credential**
      - It MUST contain the credential to be revoked encoded according to the data format given in the ``credential_format`` claim.
      - [:rfc:`7519`. Section 4.1.7].


Credential Revocation HTTP Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TBD.



.. _sec_revocation_nra_request:

Non-Revocation Attestation Request
----------------------------------

The presentation of a credential to a Verifier may occur long after it has been issued by the Issuer. During this time interval, the credential can be invalidated for any reason and therefore the Verifier also needs to verify its revocation or suspension status. To address this scenario, the Issuer provides the Wallet Instance with a *Non-Revocation Attestation*. This Attestation is bound to a credential so that the Wallet Instance can share it to a Verifier, along with the credential itself, as a proof of non-revocation status of the credential.

The Non-Revocation Attestation MUST be presented in conjunction with the digital credential. The Non-Revocation Attestation MUST be timestamped with its issuance datetime, always referring to a previous period.
The Non-Revocation Attestation MUST contain the expiration datetime after which the digital credential MUST NOT be considered valid anymore.
The Non-Revocation Attestation enables offline use cases as it MUST be statically validated using the cryptographic signature of the Issuer. 
Relying Parties MUST reject an expired Non-Revocation Attestation and, in the case of valid Attestations, they MAY still reject them according to their own policies (e.g., if the issue date doesn't meet their security requirements). 

The following diagram shows how the Wallet Instance MUST request a Non-Revocation Attestation to the Issuer.

.. _fig_Low-Level-Flow-Revocation-Attestation:
.. figure:: ../../images/Low-Level-Flow-Revocation-Attestation.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/PSr1ImCn40NWUtx5K3mek7WNAYsUreDTQd4lmZ9cHmna9p4pSV7YRtTQiANqEE_bork9Oj4wHOTL4zVfdOhB5WKVChB2eiSOIQ5bKMHF2q21EPo_QKKgbKCLd9i3D0yGxg7RlEpWpfnMWK9VbKIlVQ6HM0F68PUKFfPNZyUaIzrJlxi57uC50ugGhIGUz2VJPRpis_Llj-bkdFkVVCKOHbG2gnghtXYGHpXDW6s0ZPo8TNlmdBZPqdVokF_Qt5gLH0_N4PYOZMn9Sc8XE_JpN5ww5V5Of_W7
    
    Non-Revocation Attestation Request Flow

**Step 1 (Non-Revocation Attestation Request)**: The Wallet Instance sends the Non-Revocation Attestation Request to the Issuer. The request MUST contain the Wallet Instance Attestation with its Proof of Possession and a Credential Proof of Possession JWT, signed  with the private key related to the public key contained within the credential.

.. code::

    POST /status HTTP/1.1
    Host: pid-provider.example.org
    Content-Type: application/x-www-form-urlencoded

    credential_proof=$CredentialPoPJWT
    &client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-client-attestation
    &client_assertion=$WIA~WIA-PoP

For a non-normative example of Credential Proof of Possession see :ref:`the one provided in the prevoius section <credential_pop_jwt_ex>`.

**Step 2 (PoP verification)**: The Issuer verifies the signature of the PoP JWTs using the public key that was attested in the Wallet Instance Attestation and the credential, which is the proof that the Wallet Instance owns the private keys associated with the Wallet Instance Attestation and credential. Therefore the Wallet Instance is entitled to request its Non-Revocation Attestation.

**Step 3 (Non-Revocation Attestation Creation)**: The Issuer checks the status of the credential and creates a Non-Revocation Attestation bound to it. Then it creates a new Non-Revocation Attestation, a non-normative example of which is given below.

.. code::

    {
        "alg": "ES256",
        "typ": "non-revocation-attestation+jwt",
        "kid": "$ISSUER-JWKID"
    }
    .
    {
        "iss": "https://pid-provider.example.org",
        "iat": 1504699136,
        "exp": 1504700136,
        "credential_hash": "$CREDENTIAL-HASH",
        "credential_hash_alg": "sha-256",
        "cnf": {
            "jwk": {...} 
            }
    }

**Step 4 (Non-Revocation Attestation Response)**: The Issuer then returns the Non-Revocation Attestation to the Wallet Instance, as in the following non-normative example.

.. code::

    HTTP/1.1 201 OK
    Content-Type: application/json
    
    {
        "non_revocation_attestation": "eyJhbGciOiJFUzI1NiIsInR5cCI6IndhbGxldC1...",
    }


Non-Revocation Attestation HTTP Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The requests to the *Credential status endpoint* of the Issuers MUST be HTTP with method POST, using the same mandatory parameters as in the :ref:`Table of Credential Request parameters <table_revocation_request_params>`. These MUST be encoded in ``application/x-www-form-urlencoded`` format.

The *Credential status endpoint* MUST be provided by the Issuer within its Metadata. 


Non-Revocation Attestation HTTP Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *Credential status endpoint* MUST return a response with a *HTTP status code 201 OK* if the credential is valid at the time of the request, otherwise a *HTTP status code 404 Not Found* MUST be given by the Issuer. The responses MUST be encoded in ``application/json`` format. It MUST contain the following mandatory claims.

.. _table_http_response_claim:
.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **non_revocation_attestation**
      - It MUST contain the Non-Revocation Attestation as a signed JWT. 
      - This specification.


Non-Revocation Attestation
^^^^^^^^^^^^^^^^^^^^^^^^^^

The Non-Revocation Attestation MUST contain the following claims. 

.. _table_non_revocation_attestation_header: 
.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **JOSE Header**
    - **Description**
    - **Reference**
  * - **alg**
    - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms in Section :ref:`Cryptographic Algorithms <supported_algs>` and MUST NOT be set to ``none`` or to a symmetric algorithm (MAC) identifier.
    - `[OIDC4VCI. Draft 13] <https://openid.bitbucket.io/connect/openid-4-verifiable-credential-issuance-1_0.html>`_, [:rfc:`7515`], [:rfc:`7517`].
  * -  **typ** 
    - It MUST be set to `non-revocation-attestation+jwt`.
    - [:rfc:`7515`], [:rfc:`7517`], this specification.
  * - **kid**
    -  Unique identifier of the Issuer ``jwk`` as base64url-encoded JWK Thumbprint value.
    - :rfc:`7638#section_3`. 

.. _table_non_revocation_attestation_claim:
.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - It MUST be set to the identifier of the Issuer.
      - :rfc:`9126` and :rfc:`7519`.
    * - **iat**
      - UNIX Timestamp with the time of JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **exp**
      - UNIX Timestamp with the expiry time of the JWT.
      - :rfc:`9126` and :rfc:`7519`.
    * - **credential_hash**
      - Hash value of the credential the Non-Revocation Attestation is bound to.
      - This specification.
    * - **credential_hash_alg**
      - The Algorithm used of hashing the credential to which the Non-Revocation Attestation is bound. The value MUST be set to ``S256``.
      - This specification.
    * - **cnf**
      - JSON object containing the proof-of-possession key materials. The ``cnf`` jwk value MUST match with the one provided within the related credential. 
      - `[RFC7800, Section 3.1] <https://www.iana.org/go/rfc7800>`_.



.. _sec_revocation_nra_presentation:

Non-Revocation Proof during the Presentation Phase
--------------------------------------------------

During the presentation phase, a Verifier MAY request the Wallet Instance to provide a Non-Revocation Attestation along with the requested credential (e.g. using the ``scope`` parameter). The Wallet Instance MUST provide the Verifier with a most recent Non-Revocation Attestation. If the Attestation is requested by the Verifier and the Wallet Instance is not able to provide it or it is expired the Verifier MUST reject the credential. If the Attestation is issued far back in time, the Verifier MAY decide to accept or reject the credential according to its security policy.

Law-Enforcement Authorities or Third Parties authorized by national law, MAY require deferred non-revocation status verification but the definition of these protocols is currently out-of-scope for this technical implementation profile.

