.. include:: ../common/common_definitions.rst
.. Included via digital-credential-management.rst at title level '=' (document title).


PID Data Model
==============================

The Person Identification Data (PID) is issued by the PID Provider according to national laws and it MUST be provided in both SD-JWT VC and mdoc-CBOR data format.

.. note::
  The PID will be issued when the IT-Wallet will be fully operational and notified as EUDIW, the **IT-Wallet ID** is intended for access online services of national RPs only.
  

The main scope of the PID is allowing natural persons to be authenticated for access to a service or to a protected resource.
The PID MUST be provided according to data model requirements defined in  `EU_2024/2977`_ and **Section 2 of the ARF PID Rulebook v1.3** [`EIDAS-ARF`_], the User attributes provided within the Italian PID are the ones listed below:

- Current Family Name
- Current First Name
- Date of Birth
- Place of Birth
- Nationality
- Portrait
- Personal administrative number

In addition to the User attributes listed above, the PID includes also the following metadata attributes (`EU_2024/2977`_ and **Section 2 of the ARF PID Rulebook v1.3** [`EIDAS-ARF`_]):

- Issuing authority
- Issuing country
- Expiry Date
- Validity status information
- Identity and data proofing information

Some attributes, such as the *identity and data proofing information*, are provided as **domestic extensions** defined by the Italian IT-Wallet specification. It is NOT part of the ARF PID Rulebook (Annex 3.01, PID Rulebook v1.3), but is **permitted under ARF requirement PID_06**, which allows Member States to define additional domestic attributes beyond those specified in Commission Implementing Regulation (CIR) 2024/2977 (`EU_2024/2977`_). In particular, the identity proofing information is REQUIRED for Italian PIDs to ensure:

- The evaluation of User authentication method used.
- The level of Assurance compliance of identity proofing during the enrollment process, according to the LoA defined by the eIDAS Regulation.
- The auditability upon the User attributes verification processes.

Attributes that are **domestic extensions** MUST be included in the **domestic namespaces** that are defined in Section :ref:`credential-data-model-pid:PID Data Model in SD-JWT VC Format` and Section :ref:`credential-data-model-pid:PID Data Model in mdoc-CBOR Format` for SD-JWT VC and mdoc-CBOR PIDs respectively.

PID Data Model in SD-JWT VC Format
-----------------------------------

The SD-JWT VC PID defined in this specification MUST use the ``vct`` claim value set with ``urn:eudi:pid:it:1``, according to the domestic PID extensions defined in the ARF PID Rulebook v1.3 (see also ARF HLR **PID_14**, Section 4.2, extending the base type ``urn:eudi:pid:``).

.. note::
   **Transitional Phase:**

   During the transitional phase before full EUDIW operability, national implementations MAY use the ``vct`` value ``urn:it-wallet:pid:1``. Upon reaching full EUDIW operability, all implementations MUST transition to the EUDI-compliant identifier ``urn:eudi:pid:it:1`` specified above.

According to `EU_2024/2977`_ and **Section 4 of the ARF PID Rulebook v1.3** [`EIDAS-ARF`_], the PID in SD-JWT VC format includes the following User Attributes:

.. _table_sd-jwt-vc_pid_parameters:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **given_name**
      - REQUIRED. *String*. Current First Name.
      - Section 5.1 of `OIDC`_ and Commission Implementing Regulation `EU_2024/2977`_
    * - **family_name**
      - REQUIRED. *String*. Current Family Name.
      - Section 5.1 of `OIDC`_ and Commission Implementing Regulation `EU_2024/2977`_
    * - **birthdate**
      - REQUIRED. *String*. Date of Birth. It MUST be set according to ISO8601-1 (YYYY-MM-DD format).
      - Commission Implementing Regulation `EU_2024/2977`_
    * - **place_of_birth**
      - REQUIRED. *JSON Object*. Place of Birth. At least one of `country`, `region`, `locality` MUST be present.
      - Commission Implementing Regulation `EU_2024/2977`_
    * - **nationalities**
      - REQUIRED. *Array of strings*. One or more alpha-2 country codes as specified in ISO 3166-1.
      - Commission Implementing Regulation `EU_2024/2977`_
    * - **picture**
      - REQUIRED. *String*. Facial image encoded as a data URL containing the base64-encoded JPEG portrait, compliant with the quality requirements for a full frontal image type as set out in ISO/IEC 39794-5 or, for backward compatibility, ISO/IEC 19794-5, clauses 8.2, 8.3 and 8.4. It MUST NOT include the headers or blocks specified in clause 5 of ISO/IEC 19794-5, except for the image data itself. Except where the User explicitly opts out, where applicable; in case of opt-out, the value MUST be empty, as specified in ARF HLR **PID_03**. Mandatory inclusion of the portrait attribute applies as of 24 months after entry into force of the Regulation amending `EU_2024/2977`_.
      - Commission Implementing Regulation `EU_2024/2977`_ and ARF PID Rulebook
    * - **personal_administrative_number**
      - OPTIONAL. *String*. National unique identifier of a natural person. It MUST be set according to ETSI EN 319 412-1 Section 5.1.3. The only natural person semantic identifiers (**NAT-5.1.3-03**) supported whithin IT-Wallet are ``PNO`` and ``TIN``. For IDANPR, ``PNO`` MUST be used, while for Fiscal Code, ``TIN`` MUST be used. 
      - Commission Implementing Regulation `EU_2024/2977`_

.. note::
   **Identity Matching and Identity Reconciliation**

   Identity matching is not a specific EUDI Wallet feature. It is the same practical approach used in any legacy authentication and authorization infrastructure.

   The Relying Party MUST first perform **identity matching**, to establish that the person identification attributes presented in the current transaction refer to the same natural person. Only after a successful identity matching, the Relying Party MAY perform **identity reconciliation**, linking that natural person to a previous User session or stored User record.

   Different Digital Credential types MAY define different identity matching patterns. This Section defines the pattern for the PID. For the IT-Wallet ID pattern, see Section :ref:`credential-data-model-it-wallet-id:IT-Wallet ID Data Model`.

   For the PID, ``personal_administrative_number`` is OPTIONAL. Relying Parties MUST NOT assume that a unique national identifier is always available. When it is presented, the Relying Party SHOULD use it for identity matching. When it is not presented, the Relying Party MUST perform identity matching using one or more of the following ways:

   - *Attribute-Based Binding*: comparing the person identification attributes available in the PID presentation (for example ``given_name``, ``family_name`` and ``birthdate`` / ``birth_date``);
   - *Session-Based Binding*: treating attributes released in the same presentation response as belonging to the same User;
   - *Issuer-Attested Binding* or *Relying Party-Specific Identifiers*: using an identifier attested by the Issuer or previously established with the Relying Party;
   - *Cryptographic Binding*: proving that the private keys of the presented Digital Credentials are managed by the same WSCA/WSCD, when available.

   Selective disclosure MUST be used so that identifying attributes needed only for matching are not released when not required for the specific transaction, in line with Article 5a of the European Digital Identity Regulation and the privacy-preserving combined presentation principles of the ARF, to be fully applicable when the IT-Wallet will be notified as an EUDIW solution.

All the User attributed listed above MUST be selectively disclosable.
In addition to the mandatory metadata attributes defined in :ref:`SD-JWT header JOSE Parameters Table <table_sd-jwt-vc_jose_header>` and :ref:`SD-JWT Parameters Table <table_sd-jwt-vc_parameters>`, the following metadata attributes are REQUIRED for a PID:

  - **date_of_expiry**
  - **sub** (domestic extension)
  - **iat**
  - **cnf**
  - **status**
  - **verification** (domestic extension)

SD-JWT-VC PID Non-Normative Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the following, the non-normative example of the payload of a PID represented in JSON format.

.. literalinclude:: ../../examples/pid-json-example-payload.json
  :language: JSON

The corresponding SD-JWT version for PID is given by

.. literalinclude:: ../../examples/pid-sd-jwt-example-header.json
  :language: JSON

.. literalinclude:: ../../examples/pid-sd-jwt-example-payload.json
  :language: JSON

The disclosure list is presented below.

**Claim** ``given_name``:

 * SHA-256 Hash: ``Jkbj8aLr-z2_c-HVxCbiw6YXFNHiyLSv1xGjN8lRogI``
 * Disclosure:
   ``WyJrZ2h0ZTVNRE5IYlFmZEpIcDg4cENBIiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
 * Contents:
   ``["kghte5MDNHbQfdJHp88pCA", "given_name", "Mario"]``


**Claim** ``family_name``:

 * SHA-256 Hash: ``MWJufQz_DFWc9cR4yxq8XqmTZfglkg2D2Sxa3UFN4Qk``
 * Disclosure:
   ``WyJoWDFURXpfejg3N19YQXRyM0NPYVdnIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
 * Contents:
   ``["hX1TEz_z877_XAtr3COaWg", "family_name", "Rossi"]``


**Claim** ``birthdate``:

 * SHA-256 Hash: ``uIapUlDTKsB5wN7BF6xuBNTtl74gl5iCu_aQ5nj3YL8``
 * Disclosure:
   ``WyJZV3RJMDZ4RGRDeXZUYWxjSW5URTNBIiwgImJpcnRoZGF0ZSIsICIxOTgw``
   ``LTAxLTEwIl0``
 * Contents:
   ``["YWtI06xDdCyvTalcInTE3A", "birthdate", "1980-01-10"]``


**Claim** ``place_of_birth``:

 * SHA-256 Hash: ``tI5s2A_Ez6oZv6plZzUPjYAL-SJGiAUFyRbhzLsluGU``
 * Disclosure:
   ``WyJYY1hsUFZDcWpITnZlQkNubFZQWWdBIiwgInBsYWNlX29mX2JpcnRoIiwg``
   ``eyJsb2NhbGl0eSI6ICJSb21hIn1d``
 * Contents:
   ``["XcXlPVCqjHNveBCnlVPYgA", "place_of_birth", {"locality":``
   ``"Roma"}]``


**Claim** ``nationalities``:

 * SHA-256 Hash: ``GHYjuGUthjtB4q4Oz_ZSGPmCokLOpv2kpFNzz1LfFUY``
 * Disclosure:
   ``WyJLTmM1LUdrOUNRaF9UZEdicUJLSTdBIiwgIm5hdGlvbmFsaXRpZXMiLCBb``
   ``IklUIl1d``
 * Contents:
   ``["KNc5-Gk9CQh_TdGbqBKI7A", "nationalities", ["IT"]]``

**Claim** ``picture``:

 * SHA-256 Hash: ``R6x9o0j4m3L4Pq6xYdK3rP4nNq8vJ2b7sFqT9cUwI7A``
 * Disclosure:
   ``WyJRaDhMbU40eFI3dlAyY0tqVDVzWllBIiwgInBpY3R1cmUiLCAiZGF0YTppbWFn``
   ``ZS9qcGVnO2Jhc2U2NCwvOWovNEFBUVNrWkpSZ0FCQVFBQUFRQUJBQUQuLi4iXQ``
 * Contents:
   ``["Qh8LmN4xR7vP2cKjT5sZYA", "picture",``
   ``"data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."]``

The combined format for the PID issuance is given by:

.. literalinclude:: ../../examples/pid-sd-jwt-example-combined.txt
  :language: text


PID Data Model in mdoc-CBOR Format
----------------------------------------

The PID in mdoc-CBOR format MUST use the **docType** ``eu.europa.ec.eudi.pid.1`` in compliance with ARF HLR **PID_04**.

The PID attributes MUST be encoded as specified in **Section 3 of the ARF PID Rulebook v1.3** [`EIDAS-ARF`_] and organized in the following namespaces:

- **Standard ARF PID attributes**: namespace ``eu.europa.ec.eudi.pid.1``
- **Italian domestic extensions**: namespace ``eu.europa.ec.eudi.pid.it.1``

According to `EU_2024/2977`_ and **Section 3 of the ARF PID Rulebook v1.3** [`EIDAS-ARF`_], the PID in mdoc-CBOR format includes the following User Attributes:

.. _table_mdoc-cbor_pid_attributes:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **elementIdentifier**
      - **Description**
      - **Namespace**
    * - **given_name**
      - REQUIRED. *(tstr)*. Current First Name.
      - ``eu.europa.ec.eudi.pid.1``
    * - **family_name**
      - REQUIRED. *(tstr)*. Current Family Name.
      - ``eu.europa.ec.eudi.pid.1``
    * - **birth_date**
      - REQUIRED. *(full-date)*. Date of Birth. It MUST be encoded as full-date string according to :rfc:`8949`.
      - ``eu.europa.ec.eudi.pid.1``
    * - **place_of_birth**
      - REQUIRED. *(map)*. Place of Birth. At least one of ``country``, ``region``, ``locality`` MUST be present.
      - ``eu.europa.ec.eudi.pid.1``
    * - **nationality**
      - REQUIRED. *(array of tstr)*. One or more Alpha-2 country codes as specified in ISO 3166-1. Encoded as CDDL type ``nationalities`` (array of country codes).
      - ``eu.europa.ec.eudi.pid.1``
    * - **portrait**
      - REQUIRED. *(bstr)*. Facial image in JPEG format, compliant with the quality requirements for a full frontal image type as set out in ISO/IEC 39794-5 or, for backward compatibility, ISO/IEC 19794-5, clauses 8.2, 8.3 and 8.4. It MUST NOT include the headers or blocks specified in clause 5 of ISO/IEC 19794-5, except for the image data itself. Except where the User explicitly opts out, where applicable; in case of opt-out, the value MUST be empty, as specified in ARF HLR **PID_03**. Mandatory inclusion of the portrait attribute applies as of 24 months after entry into force of the Regulation amending `EU_2024/2977`_.
      - ``eu.europa.ec.eudi.pid.1``
    * - **personal_administrative_number**
      - OPTIONAL. *(tstr)*. National unique identifier of a natural person generated by ANPR.
      - ``eu.europa.ec.eudi.pid.1``


In addition to the mandatory metadata attributes defined in :ref:`MobileSecurityObject Table <table_MobileSecurityObject_attributes>` and :ref:`mdoc-CBOR Metadata Attributes Table <table_element_identifiers_mdoc>`, the following metadata attributes are REQUIRED for a PID:

.. list-table::
    :class: longtable
    :widths: 50 50
    :header-rows: 1

    * - **Attribute**
      - **Location**
    * - **expiry_date**
      - ``eu.europa.ec.eudi.pid.1`` namespace
    * - **sub**
      - ``eu.europa.ec.eudi.pid.it.1`` namespace
    * - **validityInfo.signed**
      - MobileSecurityObject
    * - **verification**
      - ``eu.europa.ec.eudi.pid.it.1`` namespace
    * - **status**
      - MobileSecurityObject (as defined in Section 6.3 of `TOKEN-STATUS-LIST`_)

.. note::
   **Key differences from SD-JWT encoding:**

   The ARF PID Rulebook v1.3 uses different claim names between SD-JWT and mdoc-CBOR formats:

   - mdoc uses ``birth_date`` (not ``birthdate`` as in SD-JWT)
   - mdoc uses ``expiry_date`` (not ``date_of_expiry`` as in SD-JWT)
   - mdoc uses ``nationality`` (not ``nationalities`` as in SD-JWT). Note: both formats encode the value as an array of country codes.
   - mdoc uses ``portrait`` (not ``picture`` as in SD-JWT). Note: SD-JWT encodes the value as a data URL; mdoc encodes the JPEG bytes as ``bstr``.

   See Section 3.1.1 (mdoc encoding) and Section 4.1.1 (SD-JWT encoding) of the ARF PID Rulebook v1.3 for the complete mapping.


mdoc-CBOR PID Non-Normative Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A non-normative example of a PID in mdoc-CBOR format (diagnostic notation) is shown below:

.. literalinclude:: ../../examples/pid-mdoc-cbor-example.txt
  :language: text


