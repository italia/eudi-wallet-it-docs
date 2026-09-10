.. include:: ../common/common_definitions.rst
.. Included via infrastructure-trust.rst at title level '-' (level 1).

Common Trust Artifacts
----------------------

This section details the common artifacts involved in both the EUDIW and National Trust Frameworks, including:

- :ref:`infrastructure-trust:Entity Sign/Seal Certificate Profile`;
- :ref:`infrastructure-trust:Trust Anchor Certificate Profile`.

Entity Sign/Seal Certificate Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section extends the general :ref:`infrastructure-trust:X.509 Certificate Profile` and specifies a **Certificate Profile** for **Entity Sign/Seal Certificates**, which are used for signing and sealing various Attestations.
This profile is originally defined in `ETSI TS 119 412-6`_.

.. warning::

  The Entity Sign/Seal Certificate Profiles defined in this specification assume that Entity Sign/Seal Certificates are issued by a CA and are not self-signed.
  A self-signed certificate intended to act as a Trust Anchor MAY be used in interoperability, however, National Sign/Seal Certificates MUST comply with the requirements defined in :ref:`infrastructure-trust:Trust Anchor Certificate Profile` and :ref:`infrastructure-trust:Certification Hierarchies` which requires National Trust Anchors to be bound to a common root.

PID Provider Sign/Seal Certificate
""""""""""""""""""""""""""""""""""

The specific requirements for PID Provider Sign/Seal Certificates are specified in Clause 4 of [`ETSI TS 119 412-6`_].

The following table defines the complete set of extensions applicable to the certificate profile.
Extensions not listed in the table MUST NOT be present.

.. list-table:: PID Provider Sign/Seal Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Description**

   * - ``authorityKeyIdentifier``
     - REQUIRED. The value of the ``keyIdentifier`` field SHOULD be derived from the public key using the methods defined in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - REQUIRED. Its value SHOULD be derived from the subject public key using the methods defined in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED. It MUST contain one (and only one) of the key-usage settings *Type A*, *Type B*, *Type C* or *Type F*.
       For additional details, see Clause 4.4.1 [`ETSI TS 119 412-6`_], Clause 4.3.2 [`ETSI EN 319 412-2`_] and Clause 4.3.1 [`ETSI EN 319 412-3`_].

   * - ``certificatePolicies``
     - REQUIRED. It MUST include a ``PolicyInformation`` structure with ``policyIdentifier`` set to the OID of a certificate policy including at least the requirements for *NCP+*, defined in `ETSI EN 319 411-1`_, to comply with `EIDAS-ARF`_ requirement ``AS-AP-10-098``.

   * - ``subjectAltName``
     - REQUIRED.

   * - ``cRLDistributionPoints``
     - CONDITIONAL. **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in `ETSI EN 319 412-1`_.

       If present, it MUST contain at least one reference to a publicly available CRL.

   * - ``authorityInfoAccess``
     - REQUIRED. It MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) and ``accessLocation`` specifying at least one access location of a valid CA certificate of the issuing CA.
       
       If OCSP is supported by the issuing CA, the extension MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) and ``accessLocation`` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - REQUIRED. It MUST contain a ``QCStatement`` structure with ``statementId`` set to ``0.4.0.1862.1.6`` (``id-etsi-qcs-QcType``); the corresponding ``statementInfo`` MUST contain a ``QcType`` structure including exactly one object identifier, namely ``0.4.0.194126.1.1`` (``id-etsi-qct-pid``), as defined in Clause 4.5 of [`ETSI TS 119 412-6`_].
     
       It MAY contain additional ``QCStatement`` structures among those defined in Clause 4.2 of [`ETSI EN 319 412-5`_]. In any case, it MUST NOT contain a ``QCStatement`` structure with ``statementId`` set to ``0.4.0.1862.1.7`` (``id-etsi-qcs-QcCClegislation``), referred to as ``esi4-qcStatement-7``.

The following is a non-normative example of a PID Provider Sign/Seal Certificate for legal persons.

.. literalinclude:: ../../examples/pid-sign-seal.txt
  :language: text

Wallet Provider Sign/Seal Certificate
"""""""""""""""""""""""""""""""""""""

The specific requirements for Wallet Provider Sign/Seal Certificates are specified in Clause 5 of [`ETSI TS 119 412-6`_].

The following table defines the complete set of extensions applicable to the certificate profile.
Extensions not listed in the table MUST NOT be present.

.. list-table:: Wallet Provider Sign/Seal Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Description**

   * - ``authorityKeyIdentifier``
     - REQUIRED. The value of the ``keyIdentifier`` SHOULD be derived from the public key using the methods defined in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - REQUIRED. Its value SHOULD be derived from the subject public key using the methods defined in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED. It MUST contain one (and only one) of the key-usage settings *Type A*, *Type B*, *Type C* or *Type F*.
       For additional details, see Clause 4.4.1 [`ETSI TS 119 412-6`_], Clause 4.3.2 [`ETSI EN 319 412-2`_] and Clause 4.3.1 [`ETSI EN 319 412-3`_].

   * - ``certificatePolicies``
     - REQUIRED. It MUST include a ``PolicyInformation`` structure with ``policyIdentifier`` set to the OID of a certificate policy including at least (as per `EIDAS-ARF`_ requirement ``EW-DM-38-001``):

       * The requirements for *NCP*, defined in `ETSI EN 319 411-1`_, for KAs describing a keystore.
       * The requirements for *NCP+*, defined in `ETSI EN 319 411-1`_, for KAs describing a WSCA/WSCD.

   * - ``subjectAltName``
     - REQUIRED.

   * - ``cRLDistributionPoints``
     - CONDITIONAL. **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in `ETSI EN 319 412-1`_.

       If present, it MUST contain at least one reference to a publicly available CRL.

   * - ``authorityInfoAccess``
     - REQUIRED. It MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) and ``accessLocation`` specifying at least one access location of a valid CA certificate of the issuing CA.

       If OCSP is supported by the issuing CA, the extension MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) and ``accessLocation`` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - REQUIRED. It MUST contain a ``QCStatement`` structure with ``statementId`` set to ``0.4.0.1862.1.6`` (``id-etsi-qcs-QcType``); the corresponding ``statementInfo`` SHALL contain a ``QcType`` structure including exactly one object identifier, namely ``0.4.0.194126.1.2`` (``id-etsi-qct-wal``), as defined in Clause 5.2 of [`ETSI TS 119 412-6`_].
     
       It MAY contain additional ``QCStatement`` structures among those defined in Clause 4.2 of [`ETSI EN 319 412-5`_]. In any case, it MUST NOT contain a ``QCStatement`` structure with ``statementId`` set to ``0.4.0.1862.1.7`` (``id-etsi-qcs-QcCClegislation``), referred to as ``esi4-qcStatement-7``.

The following is a non-normative example of a Wallet Provider Sign/Seal Certificate for legal persons.

.. literalinclude:: ../../examples/wp-sign-seal.txt
  :language: text

(Q)EAA Provider Sign/Seal Certificate
"""""""""""""""""""""""""""""""""""""

The specific requirements for EAA Provider and QEAA Provider Sign/Seal Certificates are specified in Clauses 6 and 7 of [`ETSI TS 119 412-6`_], respectively.

The following table defines the complete set of extensions applicable to the certificate profile.
Extensions not listed in the table MUST NOT be present.

.. list-table:: (Q)EAA Provider Sign/Seal Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Description**

   * - ``authorityKeyIdentifier``
     - REQUIRED. The value of the ``keyIdentifier`` field SHOULD be derived from the public key using the methods defined in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - OPTIONAL. If present, its value SHOULD be derived from the subject public key using the methods defined in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED. It MUST contain one (and only one) of the key-usage settings *Type A*, *Type B*, *Type C*, or *Type F*.
       For additional details, see Clause 4.3.2 [`ETSI EN 319 412-2`_] and Clause 4.3.1 [`ETSI EN 319 412-3`_].

   * - ``certificatePolicies``
     - REQUIRED (only for QEAA). As described in Clause 6.6.1 of [`ETSI EN 319 411-2`_].

   * - ``subjectAltName``
     - REQUIRED.

   * - ``cRLDistributionPoints``
     - CONDITIONAL. **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in `ETSI EN 319 412-1`_.

       If present, it MUST contain at least one reference to a publicly available CRL.

   * - ``authorityInfoAccess``
     - REQUIRED (only for QEAA). It MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) and ``accessLocation`` specifying at least one access location of a valid CA certificate of the issuing CA.

       If OCSP is supported by the issuing CA, the extension MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) and ``accessLocation`` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - REQUIRED (QEAA), OPTIONAL (EAA).
     
       For **QEAA**: It MUST contain a ``QCStatement`` structure with ``statementId`` set to ``0.4.0.1862.1.1`` (``id-etsi-qcs-QcCompliance``), referred to as ``esi4-qcStatement-1``.
            
       For **both**:
       
       * It MAY contain additional ``QCStatement`` structures among those defined in Clause 4.2 of [`ETSI EN 319 412-5`_].
       * In any case, it MUST NOT contain a ``QCStatement`` structure with ``statementId`` set to ``0.4.0.1862.1.7`` (``id-etsi-qcs-QcCClegislation``), referred to as ``esi4-qcStatement-7``.

For both QEAA and EAA Providers, if they manage the lifecycle of the Digital Credentials they issue and they use signed revocation lists such as Token Status List, they MUST use the same Sign/Seal Certificate to sign/seal the revocation list.

The following is a non-normative example of a QEAA Provider Sign/Seal Certificate for legal persons.

.. literalinclude:: ../../examples/qeaa-sign-seal.txt
  :language: text

PuB-EAA Provider Sign/Seal Certificate
""""""""""""""""""""""""""""""""""""""

.. warning::

    While the specific requirements for PuB-EAA Provider Sign/Seal Certificates that are specified in Clause 8 of [`ETSI TS 119 412-6`_] do not require this profile to be qualified, Art. 45f(1)(b) of [`EU_2024_1183`_] requires PuB-EAA type Attestations to be signed with a qualified certificate. To satisfy both requirements, although not stated either the [`EIDAS-ARF`_] or [`ETSI TS 119 412-6`_], this profile merges the QEAA and PuB-EAA Provider Sign/Seal Certificate profiles specified in Clauses 7 and 8 of [`ETSI TS 119 412-6`_].

The following table defines the complete set of extensions applicable to the certificate profile.
Extensions not listed in the table MUST NOT be present.

.. list-table:: PuB-EAA Provider Sign/Seal Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Description**

   * - ``authorityKeyIdentifier``
     - REQUIRED. The value of the ``keyIdentifier`` field SHOULD be derived from the public key using the methods defined in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - OPTIONAL. If present, its value SHOULD be derived from the subject public key using the methods defined in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED.

   * - ``certificatePolicies``
     - REQUIRED. As described in Clause 6.6.1 of [`ETSI EN 319 411-2`_].

   * - ``subjectAltName``
     - REQUIRED.

   * - ``cRLDistributionPoints``
     - CONDITIONAL. **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in `ETSI EN 319 412-1`_.

       If present, it SHALL contain at least one reference to a publicly available CRL.

   * - ``authorityInfoAccess``
     - REQUIRED. It MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) and ``accessLocation`` specifying at least one access location of a valid CA certificate of the issuing CA.

       If OCSP is supported by the issuing CA, the extension MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) and ``accessLocation`` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - REQUIRED. It MUST contain:
     
       * A ``QCStatement`` structure with ``statementId`` set to ``0.4.0.1862.1.1`` (``id-etsi-qcs-QcCompliance``), referred to as ``esi4-qcStatement-1``.
       * A ``QCStatement`` structure with ``statementId`` set to the OID corresponding to ``id-etsi-qcs-QcPSB``; the corresponding ``statementInfo`` MUST contain a ``QcPSB`` structure including the fields defined in Clause 8.3 of [`ETSI TS 119 412-6`_].
       
       It MAY contain additional ``QCStatement`` structures among those defined in Clause 4.2 of [`ETSI EN 319 412-5`_]. In any case, it MUST NOT contain a ``QCStatement`` structure with ``statementId`` set to ``0.4.0.1862.1.7`` (``id-etsi-qcs-QcCClegislation``), referred to as ``esi4-qcStatement-7``.

.. warning::

  Annex A of [`ETSI TS 119 412-6`_] does not define the specific OID of the ``id-etsi-qcs-QcPSB`` statement identifier.

The following is a non-normative example of a PuB-EAA Provider Sign/Seal Certificate for legal persons.

.. literalinclude:: ../../examples/pubeaa-sign-seal.txt
  :language: text

Trust Anchor Certificate Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section extends the general :ref:`infrastructure-trust:X.509 Certificate Profile` and specifies a **Certificate Profile** for **Trust Anchors**.
A Trust Anchor is a trusted public key (and associated data) used as an input to the :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`.
In this profile, the Trust Anchor MUST be represented and distributed as an **X.509 certificate**, which MAY be self-signed.

Relying Parties, Credential Issuers and Wallet Units validate a presented Access, Registration or Sign/Seal Certificate by building a certification path that MUST end with a certificate signed by the subject of a Trust Anchor certificate.
The Trust Anchor certificate is used as the trust termination point for the path validation process (i.e., it is the value of the ``trust_anchor`` variable in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`).
Implementations MUST support validating both self-signed and non-self-signed Trust Anchor certificates.

.. note::
  **Trust Anchor Location.**
  The location of the Trust Anchor Certificate is determined by the specific Trust Framework selected (see :ref:`trust-evaluation:EUDIW Trust Anchor Validation` and :ref:`trust-evaluation:Federation Trust Anchor Validation`).

The following table defines the profile-specific requirements for the certificate fields.
Fields not listed in the table remain subject to the requirements defined in the common :ref:`infrastructure-trust:X.509 Certificate Profile`.

.. list-table:: Trust Anchor Certificate Fields
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - **Field**
     - **Additional Requirements**

   * - ``issuer``
     - If the certificate is self-signed, the issuer's distinguished name MUST be identical to the subject's distinguished name.
       Otherwise, the issuer's distinguished name MUST identify the entity that signed and issued the certificate and MAY differ from the subject's distinguished name.

   * - ``subject``
     - The distinguished name MUST contain an ``organizationName`` attribute identifying that entity.


.. list-table:: Trust Anchor Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Description**

   * - ``authorityKeyIdentifier``
     - CONDITIONAL. **REQUIRED IF:** the certificate is not self-signed.
       For self-signed certificates, it is RECOMMENDED.
       If the extension is present, the value of the ``keyIdentifier`` field SHOULD be derived from the public key using the methods defined in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - REQUIRED. Provides a key identifier for the Trust Anchor public key.
       Its value SHOULD be derived from the subject public key using the methods defined in :rfc:`5280#section-4.2.1.2`.
       This extension SHOULD support reliable Certificate Path construction and certificate matching in LoTE- or TL-based deployments.

   * - ``keyUsage``
     - REQUIRED. It MUST assert the ``keyCertSign`` bit.
       It MAY assert the ``cRLSign`` bit if the Trust Anchor certificate is used by the CA to sign CRLs.
       It SHOULD be limited to usages consistent with the CA role of the Trust Anchor certificate.

   * - ``certificatePolicies``
     - OPTIONAL. It MAY include a ``PolicyInformation`` structure relevant to the issuing CA's practices.

   * - ``basicConstraints``
     - REQUIRED. The ``cA`` field MUST be set to ``TRUE``, signalling CA capability for X.509 path validation.
       The ``pathLenConstraint`` MAY be present; in that case, it MUST limit the number of non-self-issued intermediate CA certificates below this Trust Anchor.
       It is RECOMMENDED to set ``pathLenConstraint`` to 0 to prevent subordinate CA layers, unless a documented operational need exists to support additional intermediate CA tiers.

   * - ``cRLDistributionPoints``
     - OPTIONAL. It MAY include CRL distribution point URIs, when CRL-based revocation is used.

   * - ``authorityInfoAccess``
     - OPTIONAL. If applicable, it MAY include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) and an ``accessLocation`` specifying at least one access location of a valid CA certificate of the issuing CA.

       It MAY also include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) and ``accessLocation`` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, when OCSP-based revocation is used.

   * - ``qcStatements``
     - OPTIONAL. It MAY contain ``QCStatement`` structures among those defined in Clause 4.2 of [`ETSI EN 319 412-5`_].
     
       In any case, it MUST NOT contain a ``QCStatement`` structure with ``statementId`` set to ``0.4.0.1862.1.7`` (``id-etsi-qcs-QcCClegislation``), referred to as ``esi4-qcStatement-7``.

.. note::
  **Trust Anchor Signature.**
  A Trust Anchor certificate MAY be self-signed (representing a root CA) or non-self-signed (representing an intermediate CA designated as a Trust Anchor by policy).
  Relying Parties MUST NOT require an additional issuer above a Trust Anchor retrieved as specified by the applicable Trust Framework, even if it is not self-signed, because the Trust Anchor is an authoritative input to the path validation algorithm designated by policy.

.. note::

  As described in Section 4.3.1 of [`EUDI-TS 12`_], the Trust Anchor of an EAA Sign/Seal Certificate is referenced in the ``trustedAuthority`` attribute of the machine-readable Attestation Rulebook for the specific EAA.

The following is a non-normative example of a Trust Anchor Certificate.

.. literalinclude:: ../../examples/trust-anchor-cert.txt
  :language: text
