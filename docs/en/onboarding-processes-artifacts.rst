.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '^' (level 2, under Onboarding Processes).

Certificate and Trust Artifact Issuance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section describes the processes that issue the Trust Artifacts.
Each process covers both the first issuance and the re-issuance, for example after a key rotation or a request for additional keys, and it is described with its Input, its Outcome and its Process.

Issuance of the X.509 Certificates through ACME and OpenID Federation
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The WRPAC, the Signature/Seal Certificate and the National Authentication Certificate are issued through ACME :rfc:`8555` with the OpenID Federation profile of [`ACME-OIDFED`_].

The Entity authenticates to the Certification Authority with its Federation Trust Chain, through the ``openid-federation-01`` challenge.
The authentication reuses the trust evaluation of the National Trust Framework, so the validation of the Trust Chain and the authentication of the Entity follow :ref:`trust-evaluation:Trust Chain Validation` and :ref:`trust-evaluation:Federation Entity Authentication`.

Once the Entity is authenticated, the Certification Authority applies its policy and reads the entitlements and the profile values first from the record of the Entity in the Register, through the :ref:`infrastructure-trust:Register Open APIs`, and, when the Entity has no record there, from the registration Trust Mark included in the Resolved Metadata of the Trust Chain.
Both sources provide the authorization data with the same logic of [`ETSI TS 119 475`_].

The issuance of these certificates is a process on its own, separate from the registration and performed machine-to-machine, so the Entity presents its ``certificate_signing_requests`` in the ACME order only after the registration process has been successfully completed.

A distinct ACME service is provided for each purpose, so the type of the certificate is determined by the service, and the profile of each certificate is fixed by its type.

Within IT-Wallet the lifecycle of these certificates is kept separate from the lifecycle of the Trust Chain.
A certificate has its own ``notBefore`` and ``notAfter`` and it is governed by the X.509 revocation, so the loss of the federation membership of an Entity is reflected by the revocation of its certificates, see :ref:`onboarding-system:Entity Suspension and Removal`, and not by the expiration of the Trust Chain.

The Wallet-Relying Party Registration Certificate and the registration Trust Mark do not certify keys, so they are not issued through ACME. The registration Trust Mark is issued during the registration of the Entity, while the Wallet-Relying Party Registration Certificate is requested by the Entity to its Provider after it has obtained its WRPAC, whose validity is one of the conditions of the issuance.

.. plantuml:: plantuml/acme-oidfed-x509-issuance.puml
   :width: 99%
   :caption: `Issuance of an X.509 certificate through ACME and the OpenID Federation profile. <https://www.plantuml.com/plantuml/svg/VLDDRzH03BtdLrZbiaWiAa95eeUg8GgSAggb1muhLMx6IKOxwmaUfqlxw_5aFqXLH0vHD7xFx_cDSvqKHSTjADB6yu22MtZ0PjD97DbLCKG15UHa9MATeLAFBkuyTz1YI3IhE6fn37f7lxKClkEj4Q6n5yaCLOh4tLxWpQVfcHLlpPHl_82iNw8uaWFmu_JCkpGQvVyGXueFcEXVg08p7sfMhq-02UfY-2iDPsLrKqCYUVGDGMn1UrfpHOPeVOFg8qCvQX_5w6UPNvN5KGzMrFbaG-VpLVsjA6fONXa2Be5fzpsxWOLt5enriszz6ana8FPksP9L9u6tXJ6MHgoDzwgwFFy0JOyX47Uq5yYuPB5dix0X6slly7aYh7ddjGTam6PBzqA_Haev0qFE39vwWb0Q8jiuYzmKTHGojeCx6PD2rQC_M3mm7p5uYu0c-HbepOkl9zl7n7DuUVvcDkfL3iiQ2Q63NDH0UONI93j8R7sWWgD9YEzwpVSoAP_oRhqaVRTccGuEYdihDoYRV1-sio7l-Ojmfnl9ilCaMiysqRFDN_rOlRYCd-ylpZ_ROX-tWOfhOfV_fJy0>`_
   

Certificate Signing Request Profile
"""""""""""""""""""""""""""""""""""

This section defines the profile that the ``certificate_signing_requests`` MUST follow, see :ref:`onboarding-system:Registration Data Model`.
The Entity provides one Certificate Signing Request for each X.509 certificate it needs, that is, depending on the role, the WRPAC, the Sign/Seal Certificate or the National Authentication Certificate, and it presents each of them in the ACME order of the corresponding service.
The Wallet-Relying Party Registration Certificate and the registration Trust Mark do not certify a key, so they are not requested through a Certificate Signing Request, see :ref:`onboarding-system:Wallet-Relying Party Registration Certificate Issuance` and :ref:`onboarding-system:Registration Trust Mark Issuance`.

A Certificate Signing Request carries the public key to be certified, proves possession of the corresponding private key, and requests the values of the certificate fields supplied by the Entity.
It does not determine the content of the issued certificate: the Certification Authority MUST validate the requested values against the registration data and the applicable certificate profile, and it MUST add or determine the issuer-dependent values required by that profile.

The Certificate Signing Request MUST be a ``CertificationRequest`` as defined in :rfc:`2986` (PKCS #10), DER-encoded, and it is carried in the ACME order as required by :rfc:`8555#section-7.4`.

.. list-table:: Certificate Signing Request Fields
   :class: longtable
   :header-rows: 1
   :widths: 20 60 20

   * - **Field**
     - **Description**
     - **Reference**

   * - ``certificationRequestInfo``
     - REQUIRED. It contains the version, subject, public key and attributes of the request.
     - :rfc:`2986#section-4.1`

   * - ``version``
     - REQUIRED. It MUST be ``0``, which denotes a PKCS #10 version 1 request.
     - :rfc:`2986#section-4.1`

   * - ``subject``
     - REQUIRED. Its attributes MUST be consistent with the registration data of the Entity and with [`ETSI EN 319 412-2`_] for natural persons or [`ETSI EN 319 412-3`_] for legal persons.
       The subject is not authoritative, so the Certification Authority MAY replace it with the value derived from the record of the Entity in the Register or, in its absence, from the registration Trust Mark.
     - :rfc:`2986#section-4.1`, [`ETSI EN 319 412-2`_], [`ETSI EN 319 412-3`_]

   * - ``subjectPKInfo``
     - REQUIRED. It carries the public key to be certified.
       The key MUST use one of the public-key algorithms defined in :ref:`algorithms:Cryptographic Algorithms`.
       It MUST be distinct from the Federation Entity Key, and a distinct key MUST be used for each requested certificate.
     - :rfc:`2986#section-4.1`

   * - ``attributes``
     - REQUIRED. It MUST contain exactly one ``extensionRequest`` attribute. Other attributes MAY be included only when supported by the applicable certificate profile.
     - :rfc:`2986#section-4.1`, :rfc:`2985#section-5.4.2`

   * - ``extensionRequest``
     - REQUIRED within ``attributes``. It MUST have the object identifier ``1.2.840.113549.1.9.14`` and a single value of type ``Extensions``. The requested extensions MUST be consistent with the applicable certificate profile and the authoritative registration data.
     - :rfc:`2985#section-5.4.2`

   * - ``signatureAlgorithm``
     - REQUIRED. It MUST be compatible with the private key corresponding to ``subjectPKInfo`` and it MUST be one of the signature algorithms defined in :ref:`algorithms:Cryptographic Algorithms`.
     - :rfc:`2986#section-4.2`

   * - ``signature``
     - REQUIRED. The request MUST be signed with the private key corresponding to ``subjectPKInfo``, which proves possession of that key.
     - :rfc:`2986#section-4.2`

The following table defines the extension values requested by the Entity and the extension values determined by the Certification Authority.
The criticality of each requested extension MUST follow the applicable certificate profile.

.. list-table:: Certificate Signing Request Extension Fields
   :class: longtable
   :header-rows: 1
   :widths: 25 55 20

   * - **Extension**
     - **Description**
     - **Reference**

   * - ``extensions``
     - REQUIRED as the value of ``extensionRequest``. It MUST contain the requested extension fields as a DER-encoded ``Extensions`` sequence.
       It MUST include ``keyUsage`` and ``subjectAltName`` and, when required by the applicable certificate profile, ``certificatePolicies``.
       Extensions whose values depend on the issuing Certification Authority SHOULD be omitted from the request.
     - :rfc:`2985#section-5.4.2`, :rfc:`5280#section-4.2`

   * - ``keyUsage``
     - REQUIRED. It MUST be marked critical and MUST contain exactly one of the key-usage settings permitted by the applicable certificate profile.
        For a WRPAC, National Authentication Certificate or Registrar Sign/Seal Certificate, it MUST contain one (and only one) of *Type A*, *Type B* or *Type F*.
        For an Entity Sign/Seal Certificate, it MUST contain one (and only one) of *Type A*, *Type B*, *Type C* or *Type F*.
        For a WRPAC, *Type A* SHOULD be used as per LEG-4.3.1-4 in Clause 4.3.1 [`ETSI EN 319 412-3`_].
     - :rfc:`5280#section-4.2.1.3`, :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`, :ref:`infrastructure-trust:Registrar Sign/Seal Certificate Profile`, :ref:`infrastructure-trust:Entity Sign/Seal Certificate Profile`

   * - ``subjectAltName``
     - REQUIRED. It MUST be marked non-critical and MUST contain at least one ``GeneralName`` permitted by the applicable certificate profile.
       For a WRPAC or National Authentication Certificate, it MUST contain at least one of the following contact values: a ``uniformResourceIdentifier`` for a helpdesk/support website, an ``otherName`` with ``type-id`` set to ``2.5.4.20`` (``id-at-telephoneNumber``), or an ``rfc822Name`` for a registration/usage email address.
     - :rfc:`5280#section-4.2.1.6`, :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`

Extensions not applicable to, or not listed in, the applicable certificate profile MUST NOT be included in the issued certificate, regardless of any value requested in the Certificate Signing Request.

.. note::
   The Certificate Signing Request certifies a key that is separate from the Federation Entity Key.
   The Federation Entity Key is bound to the Entity through the Entity Configuration and the Subordinate Statement, validated through the Federation Trust Chain and not through a certification path, see :ref:`infrastructure-trust:PKI Architecture`.

The following is a non-normative example of a Certificate Signing Request for a WRPAC, with test data.

.. literalinclude:: ../../examples/csr-wrpac.txt
  :language: text

Wallet-Relying Party Access Certificate Issuance
""""""""""""""""""""""""""""""""""""""""""""""""

Wallet-Relying Party Access Certificate Issuance process issues the WRPAC, defined in the :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`, through the mechanism of :ref:`onboarding-system:Issuance of the X.509 Certificates through ACME and OpenID Federation`.
The WRPAC belongs to the EUDIW Trust Framework, so its attributes MUST always be derived from the Register, as required by clause 5.1.2 of [`ETSI TS 119 475`_], and the fallback to the Trust Mark does not apply to it.

**Input**

The ``certificate_signing_requests`` of the Entity for the WRPAC, and the Federation Trust Chain used in the ``openid-federation-01`` challenge.
The attributes of the certificate come from the record of the Entity in the Register.

**Outcome**

The WRPAC, issued by the WRPAC Certification Authority, that the Entity uses to authenticate towards the Wallet Units.

**Process**

1. The Entity requests the WRPAC to the ACME service of the WRPAC Certification Authority, presenting its ``certificate_signing_requests`` and authenticating with its Federation Trust Chain, validated as in :ref:`trust-evaluation:Federation Entity Authentication`.
2. The Certification Authority checks that the Entity has a record in the Register and derives the attributes of the certificate from it.
3. The Certification Authority issues the WRPAC and the Entity retrieves it.

Wallet-Relying Party Registration Certificate Issuance
""""""""""""""""""""""""""""""""""""""""""""""""""""""

Wallet-Relying Party Registration Certificate Issuance issues the WRPRC, described in the :ref:`infrastructure-trust:Wallet-Relying Party Registration Certificate (WRPRC) Profile`.
The WRPRC is requested by the Entity to the Provider of WRPRC, which verifies the conditions of Annex V, point 3(c) of [`CIR2025/848`_] before issuing it.
The Provider of WRPRC monitors the Register, according to [`CIR2025/848`_], and revokes the WRPRC when the registration of the Entity changes, so that the Entity requests a new one. 

**Input**

The request of the Entity and its valid WRPAC.
The attributes of the certificate come from the record of the Entity in the Register.

**Outcome**

The WRPRC, signed by the Provider of WRPRC with its Sign/Seal Certificate, that the Entity presents to the Wallet Units together with its registration data.

**Process**

1. The Entity requests the WRPRC to its Provider of WRPRC, for the first issuance or after the revocation of the previous one.
2. The Provider of WRPRC verifies that the Entity has a record with a valid registration status in the Register, that the information the certificate carries is consistent with that record, and that the WRPAC of the Entity is valid, as required by Annex V, point 3(c) of [`CIR2025/848`_].
3. The Provider of WRPRC builds the WRPRC from the record of the Entity in the Register and signs it with its Sign/Seal Certificate, issued by the WRPRC Sign/Seal Certification Authority.
4. The Provider of WRPRC monitors any change of the Register in an automated manner and revokes the WRPRC where the registration of the Entity is modified, suspended or cancelled, or where the content of the certificate is no longer consistent with the record, as required by Annex V, point 3(d) of [`CIR2025/848`_]. The revocation is published through the :ref:`infrastructure-trust:Token Status List (WRPRC Profile)`.

Signature and Seal Certificate Issuance
"""""""""""""""""""""""""""""""""""""""

Signature and Seal Certificate Issuance covers the certificates issued by the National PKI, namely the Sign/Seal Certificate of the PID Provider, of the Wallet Provider and of the EAA Provider, through the mechanism of :ref:`onboarding-system:Issuance of the X.509 Certificates through ACME and OpenID Federation`.
The Sign/Seal Certificate of a QEAA Provider and of a PuB-EAA Provider is a qualified certificate issued by a Qualified Trust Service Provider, outside the National Root and outside this process, and its qualified status is evaluated in the eligibility, see :ref:`onboarding-system:Eligibility and Compliance Preconditions`.

**Input**

The ``certificate_signing_requests`` of the Entity for the Sign/Seal Certificate, and the Federation Trust Chain used in the ``openid-federation-01`` challenge.
The attributes of the certificate come from the record of the Entity in the Register or, in its absence, from the registration Trust Mark.

**Outcome**

The Sign/Seal Certificate, issued by the Certification Authority of the role of the Entity, that the Entity uses to sign or seal the Attestations it issues.

**Process**

1. The Entity requests the Sign/Seal Certificate to the ACME service of the Certification Authority of its role, presenting its ``certificate_signing_requests`` and authenticating with its Federation Trust Chain, validated as in :ref:`trust-evaluation:Federation Entity Authentication`.
2. The Certification Authority applies its policy, reading the attributes from the record in the Register or, in its absence, from the registration Trust Mark.
3. The Certification Authority issues the Sign/Seal Certificate and the Entity retrieves it.

National Authentication Certificate Issuance
""""""""""""""""""""""""""""""""""""""""""""

National Authentication Certificate Issuance process issues the X.509 certificate that a Relying Party uses to authenticate in the Proximity Flow, through the mdoc reader authentication of [`ISO18013-5`_].
The certificate follows the same profile of the WRPAC and it is issued by the National Authentication Certification Authority, through the mechanism of :ref:`onboarding-system:Issuance of the X.509 Certificates through ACME and OpenID Federation`.

**Input**

The ``certificate_signing_requests`` of the Entity for the National Authentication Certificate, and the Federation Trust Chain used in the ``openid-federation-01`` challenge.

**Outcome**

The National Authentication Certificate, issued by the National Authentication Certification Authority, that the Entity uses to authenticate in the Proximity Flow.

**Process**

1. The Entity requests the certificate to the ACME service of the National Authentication Certification Authority, presenting its ``certificate_signing_requests`` and authenticating with its Federation Trust Chain, validated as in :ref:`trust-evaluation:Federation Entity Authentication`.
2. The Certification Authority applies its policy, reading the attributes from the record in the Register or, in its absence, from the registration Trust Mark.
3. The Certification Authority issues the National Authentication Certificate and the Entity retrieves it.

Registration Trust Mark Issuance
""""""""""""""""""""""""""""""""

Registration Trust Mark Issuance issues the registration Trust Mark, defined in :ref:`infrastructure-trust:Trust Mark registration-entity`.
The Trust Mark is issued during the registration of the Entity and not through ACME, and it is invoked by the Entity Registration at the completion of the federation registration.

**Input**

The authorization data of the Entity: its entitlements and, where applicable, the Credentials and the attributes it is authorized to issue or to request, following the logic of [`ETSI TS 119 475`_].

**Outcome**

The registration Trust Mark, issued by the Federation Trust Anchor and carried in the Subordinate Statement about the Entity.
It makes the Entity recognizable as a registered participant of the National Trust Framework, and it is the source of the authorization data when the Entity has no record in the Register.

**Process**

1. At the completion of the federation registration, the National Federation Management builds the registration Trust Mark with the authorization data of the Entity.
2. The Federation Trust Anchor signs the Trust Mark, which is carried in the Subordinate Statement, as described in :ref:`onboarding-system:Entity Registration`.
