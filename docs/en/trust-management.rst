.. include:: ../common/common_definitions.rst
.. Included via infrastructure-trust.rst at title level '-' (level 1).

Trust Management and Lifecycle
------------------------------
This section describes the lifecycle of the Trust Artifacts (:ref:`infrastructure-trust:Trust Artifacts Lifecycle State Machine`) and the mechanisms used to manage their status (:ref:`infrastructure-trust:Revocation Mechanisms`).
The lifecycle of the Entities, the events that change their registration and the effects that those events produce on the Trust Artifacts are described in :ref:`onboarding-system:Lifecycle Management`.

Trust Artifacts Lifecycle State Machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

State Machines for Trust Artifacts are described below:

- For WRPAC, WRPRC and Sign/Seal Certificates, the lifecycle states are ``VALID`` and ``REVOKED``.
  The transition from ``VALID`` to ``REVOKED`` is triggered by the revocation of the Trust Artifact, which can be initiated by the corresponding Trust Artifact provider due to various reasons such as key compromise, organizational changes, or non-compliance with framework policies.
  Once a Trust Artifact is in the ``REVOKED`` state, it MUST NOT be trusted for any operational use within the ecosystem, and any Entity relying on it MUST reject it for authentication, authorization, or any other trust-related operations.

  - A WRPAC in ``VALID`` state MUST NOT be present in the designated CRL and/or SHALL return a ``good`` status in the OCSP response.
    A WRPAC in ``REVOKED`` state MUST be present in the designated CRL and/or MUST return a ``revoked`` status in the OCSP response.
  - A WRPRC in ``VALID`` state MUST return a ``0x00`` status in the corresponding Status List Token.
    A WRPRC in ``REVOKED`` state MUST have status value ``0x01`` within the corresponding Status List Token.
- For Trust Lists (LoTE, LOTL, EUMS TL), the lifecycle states are ``CURRENT`` and ``HISTORICAL``.
  The transition from ``CURRENT`` to ``HISTORICAL`` is triggered by the publication of a new version of the Trust List that replaces the previous version.
  Once a Trust List is in the ``HISTORICAL`` state, it MUST NOT be used for any operational use within the ecosystem.
  Two exceptions apply: the validation of Trust List trustworthiness via the pivoting mechanism, and the validation of historical operations via the ``ServiceHistory`` component of the Trust List.
- Trust Marks: the status of a Trust Mark are ``ACTIVE``, ``EXPIRED``, ``REVOKED``.
  The status can be checked using the Trust Mark Status endpoint (see Section 8.4 of `OID-FED`_).

.. note::
  Register, Entity Configurations and Subordinate Statements are simply published or unpublished.
  During their publication they can be updated.

The diagram :numref:`fig_Trust_Artifacts_States` highlights the state machine of the aforementioned Trust Artifacts:

.. _fig_Trust_Artifacts_States:
.. plantuml:: plantuml/trust-artifacts-states.puml
    :width: 90%
    :caption: `Trust Artifacts States. <https://www.plantuml.com/plantuml/svg/PL5TRzCm57tFhpZQquOwyRu7j2eBB29RgyGK942Rbzmr5aaSNTk52l7ViLENj28lbdFl-JZ7jyPAjgxlabOr1Ef7kqT3fcOrMgM79F4Bbd2H4blrgcf_CRZyNAwNwGB-AFrHgUqWhMDwMv7ihYuW3SB-1zPknEy4mDSttt5z_GwRPP7VuGQvCKuEDVbP_1UcPRPPVSp2lAIThcLm0C5gkoN6j-4oBOi5LccrNa0pAkj53Gfbx5K2HFI1AUZTG13tQf3Tj4h9dtzf13jZ9wGFKsYHBL2iX2SNnMJVdxFvsRqedj9FPPaz2a--TY-TYXxrArB7J8F5XjY4uW8kgaLC93vI98XV0fmo1w7xl1AhCa-NXHUgtEWvgQ46Btiyqi-ZHgX4j0JTDT03GHb8hbkryvjMuxaYtgcQxdrCpVldKD8fS-pflreU9Fym1xCFnnQIEKsiEIuynUlf8ozJaM-o-P4XXmRZULqIivZ7Him4pxwiypAxkq78Hhz6nGUKLVsKaKdMBJNdgDbA1BwdXY9mwMohMTczBuofrrC_BPqxE24uRUQMXiRrtLy0>`_


Federation Entity Key Rotation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Federation Entity Key of an Entity is attested by the Subordinate Statement that its immediate superior publishes about it, and the Entity Configuration of the Entity MUST be signed with a key that the Subordinate Statement attests.
A new Federation Entity Key becomes trusted only when the superior attests it in the Subordinate Statement.

The Federation Entity key rotation MUST be perfomed as defined in the following steps:

- The Entity adds the new key to the ``jwks`` of its Entity Configuration and it MUST keep signing the Entity Configuration with the previous key, which is still attested.
- In the Entity Update process (see :ref:`onboarding-system:Entity Update`) the superior MUST read the ``jwks`` from the Entity Configuration, it MUST check that the Entity Configuration is signed with an attested key, and it MUST re-issue the Subordinate Statement attesting the new key.
- The previous key and the new key then coexist until the Trust Chains built with the previous Subordinate Statement have expired, and during the coexistence the Entity keeps signing with the previous key, so that both the previous and the new Subordinate Statement validate its Entity Configuration.
- Once that the validity windows of the Trust Chain has passed, the Entity MAY sign its Entity Configuration with the new key 
- Then, when the Entity wants to remove the old previous key, it MAY remove it from the ``jwks`` notifying this change to the superior through the Entity Update process (see :ref:`onboarding-system:Entity Update`), and the superior MUST remove it from the Subordinate Statement.
- The superior MUST register the event as a ``jwks_update`` published on the Federation Subordinate Events Endpoint.


Revocation Mechanisms
^^^^^^^^^^^^^^^^^^^^^

This section describes the artifacts that are employed in :ref:`infrastructure-trust:Trust Artifacts Lifecycle State Machine` to manage the status of certificates and entities by detailing respective formats and parameters.
The main distinction is the following:

- To manage Wallet-Relying Party Access Certificates and Sign/Seal Certificates, the entities acting as Trust Anchors for these certificates MUST:

  - make available at least one revocation mechanism among :ref:`infrastructure-trust:Certificate Revocation List (CRL)` and :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`;
  - issue WRPACs and Sign/Seal Certificates with at least an extension corresponding to the provided revocation mechanism.

- To manage Wallet-Relying Party Registration Certificates, each Provider of Wallet Relying Party Registration Certificates MUST:

  - make available an endpoint to request :ref:`infrastructure-trust:Token Status List (WRPRC Profile)`;
  - issue WRPRCs with the appropriate parameter ``status`` as described in :ref:`infrastructure-trust:Wallet-Relying Party Registration Certificate (WRPRC) Profile`.

.. note::
  `ETSI EN 319 411-1`_ recommends the support of OCSP, see clause CSS-6.3.10-06 and Note 2.

Certificate Revocation List (CRL)
"""""""""""""""""""""""""""""""""

**Certificate Revocation Lists (CRLs)** are used to check the revocation status of an X509 certificate.
A CRL is a digitally signed list of revoked certificates that have been issued by a CA.
The CRL is published and made available to any entity via a publicly accessible URI.
The CRL MUST be digitally signed by the **CRL issuer**.

CRLs MAY be used for the following types of certificates:

- Wallet Relying Party Access Certificates by including the ``cRLDistributionPoints`` extension in the certificate, as described in :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`.
- Sign/Seal Certificates by including the ``cRLDistributionPoints`` extension in the certificate, as described in :ref:`infrastructure-trust:Entity Sign/Seal Certificate Profile`.

If a CRL is used to manage the status of the certificates, the CRL issuer MUST be the entity referenced in the Trust Anchor certificate ``subject`` field.

The CRL issuer MAY also generate delta CRLs.
A delta CRL only lists those certificates, within its scope, whose revocation status has changed since the issuance of a referenced complete CRL.
The referenced complete CRL is referred to as a base CRL.
The scope of a delta CRL MUST be the same as the base CRL that it references.

If supported by the CA, the CRL MUST be available at the URI specified in the ``cRLDistributionPoints.distributionPoint`` *[0] CHOICE* structure within the Wallet Relying Party Access Certificate (WRPAC).

An X.509 v2 CRL is represented as the ASN.1 DER encoding of the ``CertificateList`` SEQUENCE.
The ASN.1 DER encoding is a strictly defined tag, length, and value encoding system for each element.
The final bytes transmitted represent the DER encoding of the top-level SEQUENCE containing the fields in the following table:

.. list-table:: Top-Level CertificateList Structure
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``tbsCertList``
     - REQUIRED. *SEQUENCE*. Contains the core CRL information including the name of the issuer, issue date, next update date, the optional list of revoked certificates, and optional CRL extensions.
     - :rfc:`5280`, clause 5.1.1.1

   * - ``signatureAlgorithm``
     - REQUIRED. *SEQUENCE*. Contains the algorithm identifier for the algorithm used by the CRL issuer to sign the ``CertificateList``.
       Selection SHOULD align with relevant standards (e.g., [ETSI TS 119 312]).
     - :rfc:`5280`, clause 5.1.1.2

   * - ``signatureAlgorithm.algorithm``
     - REQUIRED. *OBJECT IDENTIFIER*. The OID of the signature algorithm.
     - [:rfc:`5280`, clause 4.1.1.2]

   * - ``signatureAlgorithm.parameters``
     - OPTIONAL. *ANY*. Algorithm-specific parameters, dependent on the signature algorithm used.
     - [:rfc:`5280`, clause 4.1.1.2]

   * - ``signatureValue``
     - REQUIRED. *BIT STRING*. Contains the digital signature computed upon the ASN.1 DER encoded ``tbsCertList``.
     - [:rfc:`5280`, clause 5.1.1.3]

Certificate List Content
.........................

The ``tbsCertList`` (To Be Signed Certificate List) is an ASN.1 SEQUENCE containing several fields and extensions.
The following table lists all such fields and extensions that are required in a CRL or conditionally required.

.. list-table:: tbsCertList Fields and Extensions
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``version``
     - OPTIONAL. *INTEGER*. Describes the version of the encoded CRL.
       When extensions are used (as is standard practice), this field MUST be present and MUST specify version 2 (the integer value is ``1``).
     - [:rfc:`5280`, clause 5.1.2.1]

   * - ``signature``
     - REQUIRED. *SEQUENCE*. The algorithm identifier for the algorithm used to sign the CRL.
     - [:rfc:`5280`, clause 5.1.2.2]

   * - ``signature.algorithm``
     - REQUIRED. *OBJECT IDENTIFIER*. The OID of the signature algorithm.
       MUST match the ``signatureAlgorithm`` field in the parent ``CertificateList`` sequence.
     - [:rfc:`5280`, clause 4.1.1.2]

   * - ``signature.parameters``
     - OPTIONAL. *ANY*. Algorithm-specific parameters, dependent on the algorithm used.
     - [:rfc:`5280`, clause 4.1.1.2]

   * - ``issuer``
     - REQUIRED. *Name*. Identifies the entity that has signed and issued the CRL.
       It MUST contain a non-empty X.500 distinguished name (DN) composed of ``AttributeType`` (OID) and ``AttributeValue`` sequences.
     - [:rfc:`5280`, clause 5.1.2.3]

   * - ``thisUpdate``
     - REQUIRED. *UTCTime* or *GeneralizedTime*. Indicates the issue date of this CRL.
       Dates through 2049 MUST use ``UTCTime``; dates in 2050 or later MUST use ``GeneralizedTime``.
     - [:rfc:`5280`, clause 5.1.2.4]

   * - ``nextUpdate``
     - REQUIRED. *UTCTime* or *GeneralizedTime*. Indicates the date by which the next CRL will be issued.
       Dates through 2049 MUST use ``UTCTime``; dates in 2050 or later MUST use ``GeneralizedTime``.
     - [:rfc:`5280`, clause 5.1.2.5]

   * - ``revokedCertificates``
     - OPTIONAL. *SEQUENCE OF*. A sequence of revoked certificates.
       When there are no revoked certificates, this field MUST be absent.
     - [:rfc:`5280`, clause 5.1.2.6]

   * - ``revokedCertificates.userCertificate``
     - REQUIRED. *INTEGER*. The ``CertificateSerialNumber`` of the revoked certificate.
     - [:rfc:`5280`, clause 5.1.2.6]

   * - ``revokedCertificates.revocationDate``
     - REQUIRED. *UTCTime* or *GeneralizedTime*. The date on which the revocation occurred.
     - [:rfc:`5280`, clause 5.1.2.6]

   * - ``revokedCertificates.crlEntryExtensions``
     - OPTIONAL. *SEQUENCE OF*. Extensions specific to this revoked certificate entry.
       If present, the CRL ``version`` MUST be ``v2``.
     - [:rfc:`5280`, clause 5.1.2.6]

   * - ``crlExtensions``
     - OPTIONAL. *[0] EXPLICIT SEQUENCE OF*. A sequence of one or more CRL extensions.
       If present, the CRL ``version`` MUST be ``v2``.
     - [:rfc:`5280`, clause 5.1.2.7]

The ``crlExtensions`` field MAY contain various extensions.
Notable standard extensions include:

.. list-table:: Notable crlExtensions
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``authorityKeyIdentifier``
     - REQUIRED. *SEQUENCE*. Provides a means of identifying the public key corresponding to the private key used to sign the CRL.
       Contains ``keyIdentifier`` (OCTET STRING), ``authorityCertIssuer``, or ``authorityCertSerialNumber``.
     - :rfc:`5280`, clause 5.2.1

   * - ``cRLNumber``
     - REQUIRED. *INTEGER*. A non-critical extension conveying a monotonically increasing sequence number for a given CRL scope and issuer.
       Both base CRLs and delta CRLs share the same monotonically increasing sequence; the delta CRL's number MUST be greater than the base CRL's number it references.
     - :rfc:`5280`, clause 5.2.3

   * - ``deltaCRLIndicator``
     - REQUIRED for delta CRLs; MUST NOT appear in base CRLs. *INTEGER* (``BaseCRLNumber``). A **critical** extension that marks the CRL as a delta CRL and identifies the base CRL it is relative to.
       The integer value is the ``cRLNumber`` of the base CRL on which this delta is built.
       A relying party that does not understand this extension MUST reject the CRL.
       The base CRL MUST still be reachable (cached or retrievable) for the delta to be useful.
       If this extension is absent, the CRL is a full (base) CRL.
     - :rfc:`5280`, clause 5.2.4

   * - ``freshestCRL`` (a.k.a.
       *CRL Distribution Points* on a CRL)
     - OPTIONAL; RECOMMENDED on base CRLs in deployments that issue delta CRLs. *SEQUENCE OF DistributionPointName*. A non-critical extension indicating where the most recently issued delta CRL for the same scope can be retrieved.
       Each ``DistributionPointName`` carries one or more URIs (typically ``uniformResourceIdentifier``).
       When present on a base CRL, it MUST point to the delta CRL distribution location; when present on a delta CRL, it points to the next delta CRL.
       A relying party uses this to discover deltas without additional out-of-band configuration.
     - :rfc:`5280`, clause 5.2.6

   * - ``issuingDistributionPoint``
     - OPTIONAL; REQUIRED when the CRL scope is restricted (e.g., only-CA, only-end-entity, only-some-reasons) or when the CRL is indirect. *SEQUENCE* (``IssuingDistributionPoint``). A **critical** extension describing the scope of the CRL.
       Contains flags ``distributionPoint``, ``onlyContainsUserCerts``, ``onlyContainsCACerts``, ``onlySomeReasons``, ``indirectCRL``, and ``onlyContainsAttributeCerts``.
       For delta-CRL deployments, the ``indirectCRL`` bit is set to TRUE when the delta is signed by a CRL issuer other than the Certificate Authority that issued the certificates (common when a delegated revocation service is used), and ``onlySomeReasons`` MAY restrict the delta CRL to specific revocation reasons (e.g., ``keyCompromise`` only).
       The base CRL and corresponding delta CRLs MUST share the same scope (same ``onlyContains*`` flags and ``distributionPoint``).
     - :rfc:`5280`, clause 5.2.5

Online Certificate Status Protocol (OCSP)
""""""""""""""""""""""""""""""""""""""""""""

The Online Certificate Status Protocol (OCSP) (:rfc:`6960`) enables applications to determine the exact revocation state of identified certificates.
It provides more timely revocation information than is typically possible with CRLs and MAY also be used to obtain additional status information.

An OCSP client issues a status request to an OCSP responder and MUST suspend the acceptance of the certificates in question until the responder provides a valid response.

If supported by the Certificate Authority, the URI to which the OCSP Responder can be invoked MUST be present in the ``authorityInfoAccess.accessLocation`` extension of the Wallet Relying Party Access Certificate (WRPAC).

This protocol specifies the data that MUST be exchanged between the OCSP client (which checks the status of one or more certificates) and the OCSP server (which provides the corresponding status).

The following table sums up the roles of the OCSP client and server in the EUDIW ecosystem.

.. list-table:: OCSP roles in the EUDIW ecosystem
   :class: longtable
   :widths: 28 28 44
   :header-rows: 1

   * - **OCSP Client**
     - **OCSP Server**
     - **Use case**
   * - Wallet Unit
     - WRPAC Provider
     - WRPAC Status Check
   * - Wallet Unit or Relying Party
     - PID Provider Trust Anchor
     - PID Sign/Seal Certificate Status Check
   * - Wallet Unit or Relying Party
     - PuB-EAA Provider Trust Anchor
     - PuB-EAA Sign/Seal Certificate Status Check
   * - Wallet Unit or Relying Party
     - (Q)EAA Provider Trust Anchor
     - (Q)EAA Sign/Seal Certificate Status Check

.. note::
    The Status check on Sign/Seal Certificates is needed only in case the Sign/Seal Certificate is not referenced directly as a Trust Anchor Certificate, in which case it is trusted a priori and does not need a separate status check.

Online Certificate Status Protocol Request Format
....................................................

The OCSP request MUST be the ASN.1 DER encoding of the ``OCSPRequest`` SEQUENCE, which contains the ``tbsRequest`` (To-Be-Signed Request) and an optional signature.
The following table lists the parameters found within the ``tbsRequest`` structure.

.. list-table:: tbsRequest Structure Parameters
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``version``
     - OPTIONAL. *[0] EXPLICIT INTEGER*. Indicates the version of the protocol.
       If omitted, the default value is ``v1`` (0).
     - [:rfc:`6960`, clause 4.1.1]

   * - ``requestList``
     - REQUIRED. *SEQUENCE OF*. Contains one or more single certificate status requests.
     - [:rfc:`6960`, clause 4.1.1]

   * - ``requestList.reqCert``
     - REQUIRED. *SEQUENCE*. The ``CertID`` structure carrying the identifier of a target certificate.
     - [:rfc:`6960`, clause 4.1.1]

   * - ``requestList.singleRequestExtensions``
     - OPTIONAL. *[0] EXPLICIT SEQUENCE*. Includes extensions applicable to this single certificate status request.
     - [:rfc:`6960`, clause 4.1.1]

   * - ``requestExtensions``
     - OPTIONAL. *[2] EXPLICIT SEQUENCE*. Includes extensions applicable to the overall requests found within the ``requestList``.
     - [:rfc:`6960`, clause 4.1.1]

The ``reqCert`` parameter utilizes the ``CertID`` structure, MUST be an ASN.1 *SEQUENCE* containing the following parameters:

.. list-table:: CertID Structure Parameters
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``hashAlgorithm``
     - REQUIRED. *SEQUENCE*. Identifies the hash algorithm used to generate the issuer name and key hashes.
     - [:rfc:`6960`, clause 4.1.1]

   * - ``hashAlgorithm.algorithm``
     - REQUIRED. *OBJECT IDENTIFIER*. The OID of the hash function (e.g., SHA-256, depending on the profile).
     - [:rfc:`6960`, clause 4.1.1]

   * - ``hashAlgorithm.parameters``
     - OPTIONAL. *ANY*. Algorithm-specific parameters, dependent on the hash algorithm used.
     - [:rfc:`6960`, clause 4.1.1]

   * - ``issuerNameHash``
     - REQUIRED. *OCTET STRING*. The hash of the issuer's distinguished name (DN), calculated over the DER encoding of the issuer's name field.
     - [:rfc:`6960`, clause 4.1.1]

   * - ``issuerKeyHash``
     - REQUIRED. *OCTET STRING*. The hash of the issuer's public key, calculated over the value (excluding tag and length) of the subject public key field.
     - [:rfc:`6960`, clause 4.1.1]

   * - ``serialNumber``
     - REQUIRED. *INTEGER*. The serial number of the target certificate for which the status is being requested.
     - [:rfc:`6960`, clause 4.1.1]

The ``requestExtensions`` and ``singleRequestExtensions`` structures MAY contain various extensions.
The following table lists the requested ones:

.. list-table:: OCSP Nonce Extension
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``nonce``
     - REQUIRED. *OCTET STRING*. Cryptographically fresh value used to bind a request and a response to prevent replay attacks.
       Identifier OID is ``id-pkix-ocsp-nonce``.
     - [:rfc:`6960`, clause 4.4.1]

When sent over HTTP using POST, the body of this request MUST contain the raw DER encoding of this ``OCSPRequest`` SEQUENCE and MUST have MIME type ``application/ocsp-request``.

Below is a non-normative example of an OCSP request:

.. literalinclude:: ../../examples/ocsp-request.txt
  :language: text

Online Certificate Status Protocol Response Format
...................................................

An OCSP response MUST be the ASN.1 DER encoding of the ``OCSPResponse`` *SEQUENCE*.
When transported over HTTP, the body of the HTTP response MUST contain the raw DER encoding of this ``OCSPResponse``, with the MIME type ``application/ocsp-response``.
The ``OCSPResponse`` *SEQUENCE* contains the following parameters:

.. list-table:: OCSPResponse Structure Parameters
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``responseStatus``
     - REQUIRED. *ENUMERATED*. Indicates the processing status of the prior request.
       Supported values are: ``successful`` (0), ``malformedRequest`` (1), ``internalError`` (2), ``tryLater`` (3), ``sigRequired`` (5), and ``unauthorized`` (6).
     - [:rfc:`6960`, clause 4.2.1]

   * - ``responseBytes``
     - OPTIONAL. *[0] EXPLICIT SEQUENCE*. Present only when the ``responseStatus`` is ``successful`` (0).
       Contains the response type and the encoded response data.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``responseBytes.responseType``
     - REQUIRED. *OBJECT IDENTIFIER*. Identifier for the response type.
       For a basic OCSP responder, this value MUST be ``id-pkix-ocsp-basic``.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``responseBytes.response``
     - REQUIRED. *OCTET STRING*. Contains the DER encoding of the response syntax identified by ``responseType`` (e.g., the ``BasicOCSPResponse`` structure).
     - [:rfc:`6960`, clause 4.2.1]

.. note::
   OCSP responders MUST be capable of producing responses of the ``id-pkix-ocsp-basic`` response type.
   Correspondingly, OCSP clients MUST be capable of receiving and processing responses of the ``id-pkix-ocsp-basic`` response type.

``BasicOCSPResponse`` is an ASN.1 SEQUENCE containing the following parameters:

.. list-table:: BasicOCSPResponse Structure Parameters
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``tbsResponseData``
     - REQUIRED. *SEQUENCE*. Contains the core response data to be signed by the responder.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``tbsResponseData.version``
     - OPTIONAL. *[0] EXPLICIT INTEGER*. The version of the response syntax.
       If omitted, the default value is ``v1`` (0).
     - [:rfc:`6960`, clause 4.2.1]

   * - ``tbsResponseData.responderID``
     - REQUIRED. *CHOICE*. Identifies the OCSP responder.
       It MUST contain either ``byName`` or ``byKey``.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``tbsResponseData.responderID.byName``
     - OPTIONAL. *[1] EXPLICIT Name*. The ``Name`` from the responder’s certificate subject.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``tbsResponseData.responderID.byKey``
     - OPTIONAL. *[2] EXPLICIT OCTET STRING*. The SHA-1 hash of the responder’s ``subjectPublicKey`` (excluding the tag and length fields).
     - [:rfc:`6960`, clause 4.2.1]

   * - ``tbsResponseData.producedAt``
     - REQUIRED. *GeneralizedTime*. The time at which the OCSP response was generated.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``tbsResponseData.responses``
     - REQUIRED. *SEQUENCE OF*. A sequence of ``SingleResponse`` structures, providing the status of each requested certificate.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``tbsResponseData.responseExtensions``
     - OPTIONAL. *[1] EXPLICIT SEQUENCE OF*. Contains extensions applicable to the overall OCSP response.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``signatureAlgorithm``
     - REQUIRED. *SEQUENCE*. Identifies the cryptographic algorithm used to sign the response.
     - [:rfc:`5280`, clause 4.1.1.2]

   * - ``signatureAlgorithm.algorithm``
     - REQUIRED. *OBJECT IDENTIFIER*. The OID of the signature algorithm.
       Selection SHOULD align with relevant standards (e.g., [ETSI TS 119 312]).
     - [:rfc:`5280`, clause 4.1.1.2]

   * - ``signatureAlgorithm.parameters``
     - OPTIONAL. *ANY*. Algorithm-specific parameters, dependent on the OID defined in ``algorithm``.
     - [:rfc:`5280`, clause 4.1.1.2]

   * - ``signature``
     - REQUIRED. *BIT STRING*. The digital signature computed over the hash of the DER-encoded ``tbsResponseData``.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``certs``
     - OPTIONAL. *[0] EXPLICIT SEQUENCE OF*. Certificate chain to help the client verify the responder's signature.
       If no certificates are included, this field SHOULD be absent.
     - [:rfc:`6960`, clause 4.2.1]

The ``responseExtensions`` structure MAY contain various extensions.
The following table lists the requested ones:

.. list-table:: Response Extensions Nonce
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``nonce``
     - REQUIRED. *OCTET STRING*. Cryptographically fresh value used to bind a request and a response to prevent replay attacks.
       If included in the request, responders SHOULD include it in the response.
       Identifier OID is ``id-pkix-ocsp-nonce``.
     - [:rfc:`6960`, clause 4.4.1]

In the OCSP Response there MUST be at least a ``SingleResponse`` for each ``CertID`` in the request.
Each ``SingleResponse`` is an ASN.1 *SEQUENCE* that carries the following parameters:

.. list-table:: SingleResponse Structure Parameters
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``certID``
     - REQUIRED. *SEQUENCE*. Identifier of the certificate whose status is determined in ``certStatus``.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``certStatus``
     - REQUIRED. *CHOICE*. The value of the certificate's status.
       It MUST be exactly one of: ``good``, ``revoked``, or ``unknown``.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``certStatus.good``
     - OPTIONAL. *[0] IMPLICIT NULL*. Indicates the certificate is valid.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``certStatus.revoked``
     - OPTIONAL. *[1] IMPLICIT SEQUENCE*. Indicates the certificate has been revoked.
       Contains the ``RevokedInfo`` structure.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``certStatus.revoked.revocationTime``
     - REQUIRED. *GeneralizedTime*. The time at which the certificate was revoked.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``certStatus.revoked.revocationReason``
     - OPTIONAL. *[0] EXPLICIT ENUMERATED*. Contains the ``CRLReason`` indicating why the certificate was revoked.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``certStatus.unknown``
     - OPTIONAL. *[2] IMPLICIT NULL*. Indicates the responder does not know the status of the certificate.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``thisUpdate``
     - REQUIRED. *GeneralizedTime*. Indicates the issue date and time of this OCSP Response.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``nextUpdate``
     - OPTIONAL. *[0] EXPLICIT GeneralizedTime*. Indicates the date and time by which the next update to the OCSP Responder database will be in place.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``singleExtensions``
     - OPTIONAL. *[1] EXPLICIT SEQUENCE*. Includes extensions applicable to this single certificate status response.
     - [:rfc:`6960`, clause 4.2.1]

Below is a non-normative example of an OCSP response with a single ``good`` status.

.. literalinclude:: ../../examples/ocsp-response.txt
  :language: text

Token Status List (WRPRC Profile)
""""""""""""""""""""""""""""""""""

This section profiles the Token Status List (TSL) mechanism of `TOKEN-STATUS-LIST`_ for Wallet-Relying Party Registration Certificates (WRPRCs). A TSL conveys the current status of many WRPRCs in a compact, signed Status List Token (SLT).

The SLT Provider MAY be the Provider of WRPRC or a designated entity.

**Status List**

A Status List contains a compressed byte array whose entries represent the statuses of many WRPRCs. The Provider of WRPRC MUST allocate a distinct, non-negative ``idx`` value to each issued WRPRC and include it, together with the SLT ``uri``, in the WRPRC's ``status.status_list`` member. For a JWT-encoded WRPRC, ``idx`` is a JSON integer and ``uri`` is a JSON string; for a CWT-encoded WRPRC, ``idx`` is a CBOR unsigned integer and ``uri`` is a CBOR text string. In both cases, ``uri`` MUST be a URI conforming to :rfc:`3986`.

According to the ARF and [`ETSI TS 119 475`_], the WRPRC status is either ``VALID`` or ``INVALID``; therefore, the Provider of WRPRC MUST set the ``bits`` parameter in the SLT's ``status_list`` object to ``1``. The value ``0x00`` represents ``VALID``, and ``0x01`` represents ``INVALID``.

The SLT Provider MUST pack entries starting with the least significant bit of each byte, compress the byte array using DEFLATE with the ZLIB data format, and publish the resulting Status List in the SLT.

**Status List Token**

The SLT Provider MUST act as both the Status Issuer and the Status Provider. It MUST make each SLT available via HTTP GET at the URI specified by the WRPRC's ``status.status_list.uri`` member, using ``application/statuslist+jwt`` for a JWT SLT or ``application/statuslist+cwt`` for a CWT SLT. The SLT format MAY be either a JWT or a CWT and MUST be protected by a cryptographic signature.

A JWT SLT MUST be formatted as described in Section 5.1, and a CWT SLT as described in Section 5.2, of `TOKEN-STATUS-LIST`_.

Regardless of the format, the SLT Provider for WRPRCs MUST sign each SLT using a valid X.509 certificate whose trust chain terminates at the Trust Anchor published in the Providers of WRPRC LoTE.

For a JWT SLT, the signing certificate chain MUST be carried in the ``x5c`` JOSE header; for a CWT SLT, it MUST be carried in the ``x5chain`` COSE header (label ``33``).
