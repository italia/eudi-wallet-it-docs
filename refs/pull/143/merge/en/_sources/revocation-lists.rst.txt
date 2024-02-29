.. include:: ../common/common_definitions.rst

.. _sec_revocation_intro:

Credential Lifecycle
++++++++++++++++++++

The value of a Digital Credential is conditional on its validity. A Credential that has been revoked, due to legal requirements, inaccuracy or compromise, is valueless and potentially harmful. 
For these reasons a robust mechanism for managing the life-cycle and the revocation of a Digital Credential is required.

This section outlines the key technical requirements and processes related to the revocation of Digital Credentials. 
Furthermore, it provides the technical details that the Verifiers MUST implement to verify, in a secure and reliable manner, the validity of a Digital Credential during the presentation phase.

The verification of the validity of a Digital Credential is based on the `[OAuth Status Attestation draft 01] <https://datatracker.ietf.org/doc/draft-demarco-status-attestations/01/>`_ specification. 

A Status Attestation is a signed document serving as proof of a Digital Credential's current validity status. The Issuer provides these attestations to Holders who can present them to Verifiers together with the corresponding Digital Credentials. 

The Status Attestations have the following features:

- automated issuance, as the User authentication is not required for the provisioning of the Status Attestation; 
- verification of the Digital Credential validity status in both online and offline scenarios;
- privacy-preserving, according to the following evidences:

  1. the Verifier cannot check over time the validity of a given  Digital Credential related to the User;
  2. the Issuers cannot track when and where a Digital Credential is verified;
  3. it doesn't reveal any information about the Users or the content of their Digital Credentials.

.. _sec_revocation_assumption:

Operational Requirements
-------------------

- **Internet Connection for Status Attestations**: Status Attestations can be obtained only when the Wallet Instance is connected to the internet and actively operated by the User.
- **Role of a Credential Issuer**: A Credential Issuer is responsible for creating and issuing Credentials, as well as managing their lifecycle and validity status.
- **Involvement of Authentic Sources**: When one or more Authentic Sources are involved in the issuance of a Digital Credential, the information exchanged between the Authentic Source and the Credential Issuer is crucial for the Digital Credential's issuance. Furthermore, in cases where the Authentic Source initiates a revocation or data changes, revoking the Digital Credential becomes necessary.


.. _sec_revocation_requirements:

Functional Requirements
------------

**The Status Attestation MUST:**

- be presented in conjunction with the Digital Credential; 
- be timestamped with the issuance datetime;
- contain the expiration datetime after which it SHOULD NOT be considered valid anymore and it MUST NOT be greater than the one contained in the Digital Credential which it refers to;
- have a validity period not greater than 24 hours;
- provide the proof about the non-revocation of the Digital Credential which is related to and MUST be validated using the cryptographic signature of the Issuer;
- not reveal any information about the Relying Party, the User's device or the User's data contained in the Digital Credential the attestation is related to;
- be non-repudiable even beyond its expiration time and even in the case of cryptographic keys rotation.


**The Issuer MUST:**

- ensure that the data contained in a Digital Credential is kept up to date, including the status of validity of the data from the Authentic Source;
- revoke a Digital Credential when the following circumstances occur:

  - the Digital Credential requires to be updated, whenever one or more attributes are changed; in this case the User will request a new issuance for that Digital Credential;
  - the Wallet Instance that holds the Digital Credential was issued is revoked;
  - the User deletes the Digital Credential from the Wallet Instance;

- provide a web service for allowing a Wallet Instance, with a proof of possession of a specific Digital Credential, to 

  - request a revocation of that Digital Credential;
  - obtain a related Status Attestation;

- provide out-of-band mechanisms through which the User can request the revocation of their Digital Credentials, using a robust procedure for identity proofing and User authentication, in particular when the User is unable to use the personal Wallet Instance. 


**The Wallet Instance MUST:**

- check periodically the validity status of the Digital Credential that is stored in it, requesting a Status Attestation for each Digital Credential;
- be able to present a Status Attestation if required by a Verifier, along with the corresponding Digital Credential;
- request a revocation of a Digital Credential when the Users delete it from the storage. 


**The Authentic Sources MUST:**

- provide web services for the providing of updated User data and the validity status;
- store in local databases only the minimum information required to provide the Issuer with the User data or a change in the validity status.


Revocation Use Cases
--------------------

The revocation of a Digital Credential MAY be triggered by: 

- Users using their personal Wallet Instance or by some out-of-band touchpoints.
- Revocation of the Wallet Instance.
- Authentic Sources (e.g., for attribute updates) following administrative purposes. 
- Law-Enforcing Bodies for the fulfillment of their functions and any other judicial reasons (e.g., Police).

Credential Revocation Flows can start under different scenarios, such as:

    - The User reports the loss or theft of their own physical document to the Law-Enforcement Authorities: this implies that the Credentials, if any, shall be revoked.
    - The User notifies an Authentic Source that one or more attributes are changed (e.g. the current resident address): in this case the Credentials SHALL be revoked, as they are no longer valid due to the change in attributes. 
    - Users who lose access to their Wallet Instance (e.g., due to theft or loss of the device) can request the Credential Issuer to revoke their Credentials or ask the Wallet Provider to revoke the Wallet Instance. If the Wallet Provider is authorized by the User and is aware of the types of Credentials and their issuers stored in the Wallet, it can then initiate the revocation of all Digital Credentials contained within the Wallet Instance on behalf of the User.
    - The Law-Enforcing Authorities, for the fulfillment of their functions and any other judicial reasons, may request the Authentic Source to revoke entitlements, licenses, certificates, identification documents, etc., which in turn leads to the revocation of any linked Credentials.
    - The Authentic Sources that for any administrative reasons update one or more attributes of a User, shall inform the Issuer of related Credentials. 
    - The Issuers, for technical security reasons (e.g. in the case of compromised cryptographic keys, death of the User, etc.), can decide to revoke the Credentials.


The revocation scenarios involve two main flows:

    - The **Revocation flows**: these flows describe how an Entity requests for a Digital Credential revocation. 
    - The **Status Attestation flows**: these flows define the technical protocols for requesting and obtaining a Status Attestation and how the Wallet Instance will provide it to a Verifier as a proof of validity of a corresponding Digital Credential.


.. _sec_revocation_high_level_flow:

Revocation Flows
----------------

Depending on the different scenarios that may involve the revocation of a Digital Credential, different processes and technical flows may be implemented, according to national laws or Regulations of specific domains.
The subsequent sections define the protocol interface between the Wallet Instances and the Issuers during the revocation request. The communication between the Issuers and other Entities is out-of-scope of this technical implementation profile.


.. _sec_revocation_wi_initiated_flow:

Revocation Request by Wallet Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Wallet Instance MUST request the revocation of a Digital Credential as defined below.

.. _fig_Low-Level-Flow-Revocation:
.. figure:: ../../images/Low-Level-Flow-Revocation.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/NP31IaD134Nt-OfGNEX2t0jAmLNTTD1YDuB4zoA6JfDnal7zlkE05eMixZqdWQmzg4OxPg0MfktuoXLAZsIIGXgusbFE7BZHJkh4AoJ7HVuo6_V6TLG2i0XUtg9SOze-xl2gygST62j_DFOudohFh26KNqerUxivk_jDagNx_Uu2u6V34sMPAHZZdV74FMlwLh5FCdTs5zEJzJ0k_dD6tVjb05vCdN5x05Ypplq1Nm00
    
    Wallet Instance Initiated Revocation Flow

**Step 1 (Credential Revocation Request)**: The Wallet Instance initiates the process by creating a Credential Revocation Request. This request includes a Digital Credential Proof of Possession as a JWT. It MUST be signed with the private key related to the public key contained within the Credential (such as the Issuer Signed JWT in the case of SD-JWT, or the MSO in the case of Mdoc CBOR). Then, the Wallet Instance sends the request to the Issuer as in the following non-normative example.

.. _credential_revocation_request_ex:
.. code-block::
    
    POST /revoke HTTP/1.1
    Host: pid-provider.example.org
    Content-Type: application/x-www-form-urlencoded

    credential_pop=$CredentialPoPJWT


Below, is given a non-normative example of a Credential PoP with decoded JWT headers and payload and without signature for better readability:

.. _credential_pop_jwt_ex:
.. code-block::

    {
      "alg": "ES256",
      "typ": "status-attestation-request+jwt",
      "kid": $CREDENTIAL-CNF-JWKID
    }
    .
    {
      "iss": "0b434530-e151-4c40-98b7-74c75a5ef760",
      "aud": "https://pid-provider.example.org/revoke",
      "iat": 1698744039,
      "exp": 1698744139, 
      "jti": "6f204f7e-e453-4dfd-814e-9d155319408c",
      "credential_hash": $Issuer-Signed-JWT-Hash
      "credential_hash_alg": "sha-256",
    }

**Step 2 (PoP verification)**: The Issuer verifies the signature of the PoP JWTs using the public key that was attested in the issued Digital Credential. If the verification is successful, it means that the Wallet Instance owns the private keys associated with the Digital Credential, and therefore is entitled to request its revocation.

**Step 3 (Credential Revocation)**: The Issuer revokes the Credential provided in the Credential PoP JWT. After the revocation, the Issuer MAY also send a notification to the User (e.g. using a User's email address, telephone number, or any other verified and secure communication channel), with all needed information related to the Credential revocation status update. This communication is out of scope of the current technical implementation profile. 

**Step 4 (Credential Revocation Response)**: The Issuer sends a response back to the Wallet Instance with the result of the revocation request.

.. code::

    .. code-block:: http

    HTTP/1.1 204 No Content


Credential Revocation HTTP Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The requests to the *Issuer Revocation endpoint* MUST be HTTP with method POST, using the mandatory parameters listed below within the HTTP request message body. These MUST be encoded in ``application/x-www-form-urlencoded`` format.

.. _table_revocation_request_params: 
.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **credential_proof**
      - It MUST contain a JWT proof of possession of the cryptographic key the Credential to be revoked shall be bound to. See Section :ref:`Credential Proof of Possession <sec_revocation_credential_pop>` for more details. 
      - `[OAuth Status Attestation draft 00] <https://datatracker.ietf.org/doc/draft-demarco-oauth-status-attestations/00/>`_

The Revocation Endpoint MUST be provided by the Issuer within its Metadata. 


Credential Revocation HTTP Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The response MUST be an HTTP Response using the status code set to *204 (No-Content)* in the case of successful revocation. If the Digital Credential could not be found by the Issuer, an HTTP Response with status code *404 (Not Found)* MUST be returned. Otherwise an HTTP error response MUST be provided by the Issuer to the Wallet Instance. This response MUST use *application/json* as the content type and MUST include the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered.

Below a non-normative example of an HTTP Response with an error.

.. code::

  HTTP/1.1 400 Bad Request
  Content-Type: application/json;charset=UTF-8

  {
    "error": "invalid_request"
    "error_description": "The signature of credential_pop JWT is not valid"
  }

The following HTTP Status Codes and Error Codes MUST be supported:

.. list-table:: 
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **Error Code**
      - **Description**
    * - *400 Bad Request*
      - *invalid_request*
      - The request is not valid due to the lack or incorrectness of one or more parameters. (:rfc:`6749#section-5.2`).
    * - *500 Internal Server Error*
      - *server_error*
      - The Issuer encountered an internal problem. (:rfc:`6749#section-5.2`).
    * - *503 Service Unavailable*
      - *temporarily_unavailable*
      - The Issuer is temporary unavailable. (:rfc:`6749#section-5.2`).



Status Attestation Flows
------------------------

The Status Attestation process is divided into the following phases:

  1. The Status Attestation Request by a Wallet Instance: it involves the Wallet Instance and the Issuer.
  2. The Status Attestation Presentation to a Verifier: it involves the Wallet Instance and the Verifier.


.. figure:: ../../images/High-Level-Flow-Status-Attestation.svg
    :figwidth: 100%
    :align: center
    
    High-Level Status Attestation Flows


.. _sec_revocation_status_attestation_request:

Status Attestation Request by Wallet Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The presentation of a Credential to a Verifier may occur long after it has been issued by the Issuer. During this time interval, the Credential can be invalidated for any reason and therefore the Verifier also needs to verify its revocation or suspension status. To address this scenario, the Issuer provides the Wallet Instance with a *Status Attestation*. This Attestation is bound to a Credential so that the Wallet Instance can present it to a Verifier, along with the Credential itself, as proof of non-revocation status of the Credential.

The following diagram shows how the Wallet Instance requests a Status Attestation to the Issuer.

.. _fig_Low-Level-Flow-Status-Attestation:
.. figure:: ../../images/Low-Level-Flow-Revocation-Attestation.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/NP11wzf04CNl-oaUqeE2shlGekZ57jfGfLw4iaacPccoa-xEAdxxpXAg_eLSPjxlJNx9EeeDalhEs2JiKrzIC8EkNEK6wmMJa-qw4kozahwY2Mp4pNrazZ4c2Zd2Mx99qfBN-UmFdCBOryUOcyFYAzmAnO_34P_rkgI8G7yJHPbMWUhSiztl8J0tNpvj7vk2Ys-duyoO_nT-sSxLLWXF1Wf1AMCyQy1N2d1p6rSujeJH5roATJwY2Tn3FV6mnIYBiy_hDEJhDQn8S6KIYh2-Hewk-TLExXZzjS1D3lAzmEdIAWbEik1cKUPIJrLhlOlzNDafBIzB9JEOMoXsttVO5Fk8U8z2_GpFhzosLFr1m-75u-n7j-ppS7cf1ChX8Rifkn6XxEdOZ_z6EGLlIlwaEB2Ff8Eq60juvzVawzHt_m00
    
    Status Attestation Request Flow

**Step 1 (Status Attestation Request)**: The Wallet Instance sends the Status Attestation Request to the Issuer. The request MUST contain the Credential Proof of Possession JWT, signed  with the private key related to the public key contained within the Credential.

.. code::

    POST /status HTTP/1.1
    Host: pid-provider.example.org
    Content-Type: application/x-www-form-urlencoded

    credential_pop=$CredentialPoPJWT

A non-normative example of Credential Proof of Possession is provided :ref:`in the previous section <credential_pop_jwt_ex>`.

**Step 2 (PoP verification)**: The Issuer verifies the signature of the PoP JWTs using the public key that was attested in the Digital Credential, which is proof that the Wallet Instance owns the private keys associated with the Digital Credential. Therefore the Wallet Instance is entitled to request its Status Attestation.

**Step 3 (Check for validity)**: The Issuer checks that the User's attributes are not updated by the Authentic Source or that the latter has not revoked them. The technical mechanisms for obtaining this information are out-of-scope of this technical implementation profile. 


**Step 4 (Status Attestation Creation)**: The Issuer creates the corresponding Status Attestation. A non-normative example of a Status Attestation is given below.

.. code::

    {
        "alg": "ES256",
        "typ": "status-attestation+jwt,
        "kid": $ISSUER-JWKID
    }
    .
    {
        "iss": "https://pid-provider.example.org",
        "iat": 1504699136,
        "exp": 1504700136,
        "credential_hash": $CREDENTIAL-HASH,
        "credential_hash_alg": "sha-256",
        "cnf": {
            "jwk": $CREDENTIAL-CNF-JWK
            }
    }

**Step 4 (Status Attestation Response)**: The Issuer then returns the Status Attestation to the Wallet Instance, as in the following non-normative example.

.. code::

    HTTP/1.1 201 OK
    Content-Type: application/json
    
    {
        "status_attestation": "eyJhbGciOiJFUzI1NiIsInR5cCI6IndhbGxldC1...",
    }


Status Attestation HTTP Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The requests to the *Credential status endpoint* of the Issuers MUST be HTTP with method POST, using the same mandatory parameters as in the :ref:`Table of Credential Request parameters <table_revocation_request_params>`. These MUST be encoded in ``application/x-www-form-urlencoded`` format. 

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **credential_proof**
      - It MUST contain a signed JWT as a cryptographic proof of possession of the Digital Credential. See Section :ref:`Credential Proof of Possession <sec_revocation_credential_pop>` for more details. 
      - `[OAuth Status Attestation draft 00] <https://datatracker.ietf.org/doc/draft-demarco-oauth-status-attestations/00/>`_

The *typ* value in the *credential_pop* JWT MUST be set to **status-attestation+jwt**

The *Credential status endpoint* MUST be provided by the Issuers within their Metadata. The Issuers MUST include in the issued Digital Credentials the object *status* with the JSON member *status_attestation* set to a JSON Object containing the *credential_hash_alg* claim. It MUST contain the algorithm used for hashing the Digital Credential. Among the hash algorithms, the value ``sha-256`` is RECOMMENDED .


Status Attestation HTTP Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The *Credential status endpoint* MUST return a response with a *HTTP status code 201 OK* if the Credential is valid at the time of the request. The responses MUST be encoded in ``application/json`` format. It MUST contain the following mandatory claims.

.. _table_http_response_claim:
.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **status_attestation**
      - It MUST contain the Status Attestation as a signed JWT. 
      - `[OAuth Status Attestation draft 00] <https://datatracker.ietf.org/doc/draft-demarco-oauth-status-attestations/00/>`_.

If the Digital Credential could not be found by the Issuer, an HTTP Response with status code 404 (Not Found) MUST be returned. In all other cases the Issuer MUST return an HTTP Response Error using *application/json* as the content type, and including the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form that offers more details to clarify the nature of the error encountered (for instance, changes in some attributes, reasons for revocation, other).

Below a non-normative example of an HTTP Response with an error.

.. code::

  HTTP/1.1 400 Bad Request
  Content-Type: application/json;charset=UTF-8

  {
    "error": "invalid_request"
    "error_description": "The signature of credential_pop JWT is not valid"
  }

The following HTTP Status Codes and Error Codes MUST be supported:

.. list-table:: 
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **Error Code**
      - **Description**
    * - *400 Bad Request*
      - *invalid_request*
      - The request is not valid due to the lack or incorrectness of one or more parameters. (:rfc:`6749#section-5.2`).
    * - *500 Internal Server Error*
      - *server_error*
      - The Issuer encountered an internal problem. (:rfc:`6749#section-5.2`).
    * - *503 Service Unavailable*
      - *temporarily_unavailable*
      - The Issuer is temporary unavailable. (:rfc:`6749#section-5.2`).
    * - *400 Bad Request*
      - *credential_revoked*
      - The Digital Credential is revoked. The reason of revocation MUST be provided in the *error_description* field.
    * - *400 Bad Request*
      - *credential_updated*
      - One or more attributes contained in the Digital Credential are changed. The *error_description* field MUST contain a list of updated attributes.


.. _sec_revocation_nra_presentation:

Status Attestation Presentation to the Verifiers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

During the presentation phase, a Verifier MAY request the Wallet Instance to provide a Non-Revocation Attestation along with the requested Credential. If a Verifier requests a Status Attestation for a requested Digital Credential, the Wallet Instance MUST provide the Status Attestations in the *vp_token* JSON array. If the Status Attestation is requested by the Verifier and the Wallet Instance is not able to provide it or it is expired or it is issued far back in time, the Verifier MAY decide to accept or reject the Credential according to its security policy.

Law-Enforcement Authorities or Third Parties authorized by national law, MAY require deferred non-revocation status verification but the definition of these protocols is currently out-of-scope for this technical implementation profile.



.. _sec_revocation_credential_pop:

Credential Proof of Possession
------------------------------

The Credential Proof of Possession (**credential_proof**) MUST be a JWT that MUST contain the parameters (JOSE Header and claims) in the following table.

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **typ**
      - In case of revocation request it MUST be set to ``revocation-request+jwt``. In case of Status Attestation request it MUST be set to ``status-attestation-request+jwt``, according to `[OAuth Status Attestation draft 00] <https://datatracker.ietf.org/doc/draft-demarco-oauth-status-attestations/00/>`_.
      - :rfc:`7516#section-4.1.1`.
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section `Cryptographic Algorithms <algorithms.html>`_ and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      -  Unique identifier of the ``jwk`` inside the ``cnf`` claim of the Credential to be revoked, as base64url-encoded JWK Thumbprint value.
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
    * - **credential_hash**
      - It MUST contain the hash value of a Digital Credential, derived by computing the base64url encoded hash of the Digital Credential.
      - `[OAuth Status Attestation draft 00] <https://datatracker.ietf.org/doc/draft-demarco-oauth-status-attestations/00/>`_.
    * - **credential_hash_alg**
      - It MUST contain the Algorithm used for hashing the Digital Credential. The value SHOULD be set to `S256`.
      - `[OAuth Status Attestation draft 00] <https://datatracker.ietf.org/doc/draft-demarco-oauth-status-attestations/00/>`_.



Status Attestation
------------------

The Status Attestation MUST contain the following claims. 

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
    - It MUST be set to `status-attestation+jwt`.
    - [:rfc:`7515`], [:rfc:`7517`], `[OAuth Status Attestation draft 00] <https://datatracker.ietf.org/doc/draft-demarco-oauth-status-attestations/00/>`_..
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
      - Hash value of the Credential the Status Attestation is bound to.
      - `[OAuth Status Attestation draft 00] <https://datatracker.ietf.org/doc/draft-demarco-oauth-status-attestations/00/>`_.
    * - **credential_hash_alg**
      - The Algorithm used for hashing the Credential to which the Status Attestation is bound. The value SHOULD be set to ``S256``.
      - `[OAuth Status Attestation draft 00] <https://datatracker.ietf.org/doc/draft-demarco-oauth-status-attestations/00/>`_.
    * - **cnf**
      - JSON object containing the proof-of-possession key materials. The ``cnf`` jwk value MUST match with the one provided within the related Credential. 
      - `[RFC7800, Section 3.1] <https://www.iana.org/go/rfc7800>`_.

