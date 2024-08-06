.. include:: ../common/common_definitions.rst


Authentic Sources
+++++++++++++++++++

Authentic Sources are responsible for the authenticity of the User's attributes provided as Digital Credentials by the PID/(Q)EAA Provider. During the Issuance Flow, PID/(Q)EAA Providers, after authenticating the User, request from Authentic Sources the attributes required to provide the requested Credential. If PID/(Q)EAA Providers and Authentic Sources are both allowed to use PDND, the communication between them is accomplished in compliance with [`MODI`_] and [`PDND`_] and according to the rules defined within this specification. In particular, 

    - The Authentic Source MUST provide an e-service registered within the PDND catalogue which the PID/(Q)EAA Provider, as the recipient, MUST use to request the User's attributes.
    - In case of unavailability of the User's attributes, the Authentic Source MUST provide a response to the PID/(Q)EAA Provider with an estimation time when a new request can be sent. 
    - The PID/(Q)EAA Provider MUST provide to the Authentic Source an evidence that 
    
        - the request for Users attributes is related to data about themselves.
        - the request for User attributes comes from a valid Wallet Instance. 

    - The PID/(Q)EAA Provider MUST make available to the Authentic Source an e-service for notifications on attributes availability and validity status (revocation or updates). The Authentic Source MUST use this e-service to notify to the PID/(Q)EAA Provider the notifications on the availability of the User's attributes as well as those relating to the attributes updates. 
    - The protocol flow MUST ensure integrity, authenticity, and non-repudiation of the exchanged data between the Authentic Source and the PID/(Q)EAA Provider. 
    - The e-services MUST be implemented in REST. SOAP protocol MUST NOT be used.



Security Patterns
----------------------

The following security patterns and profiles are applicable: 

    - **[REST_JWS_2021_POP]** JWS POP Voucher Issuing Profile (*Annex 3 - Standards and technical details used for Voucher Authorization* [`PDND`_]): REQUIRED. It adds a proof of possession on the Voucher. The client using the Voucher to access an e-service MUST demonstrate the proof of possession of the private key whose public is attested on the Voucher.  

    - **[ID_AUTH_REST_02]** Client Authentication with X.509 certificate with uniqueness of the token/message (*Annex 2 - Security Pattern *[`MODI`_]): REQUIRED. It guarantees trust between the Authentic Source and the PID/(Q)EAA Provider and provides a mitigation against replay attacks.

    - **[INTEGRITY_REST_01]** REST message payload integrity (*Annex 2 - Security Pattern* [`MODI`_]): REQUIRED. It adds message payload integrity of the HTTP POST request.  

    - **[AUDIT_REST_02]** submission of audit data within the request (*Annex 2 - Security Pattern* [`MODI`_]): OPTIONAL. The Authentic Source MAY request an evidence about the User Authentication related to the User's attributes requested by the PID/(Q)EAA Provider and/or a proof that the Wallet Instance is valid. In this case this pattern MUST be used.

    - **[PROFILE_NON_REPUDIATION_01]** Profile for non-repudiation of transmission (*Annex 3 - Interoperability Profile* [`MODI`_]): REQUIRED. This profile uses the following security patterns:
        
        - **ID_AUTH_CHANNEL_01** or **ID_AUTH_CHANNEL_02**
        - **ID_AUTH_REST_02**
        - **INTEGRITY_REST_01**

