.. include:: ../common/common_definitions.rst
.. Included via digital-credential-management.rst at title level '=' (document title).


Digital Credential Data Model
==============================

A Digital Credential data model has the following structure:

- **Metadata attributes**:

  - **Format-Agnostic**: These are high-level metadata attributes that describe the Digital Credential independently of its encoding format. They represent the semantic information about the Credential (e.g., ``credential_type_identifier``, ``issuing_authority``, ``expiry_date``) and remain conceptually consistent across different formats. When a Credential is encoded, these common metadata attributes are mapped to format-specific technical parameters according to the encoding rules of each format (SD-JWT-VC or mdoc-CBOR).
  - **Format-Specific**: These are format-specific metadata parameters that support the security model and protocol requirements.

- **User attributes**: Information about the User, such as identity or qualifications.

The (Q)EAAs are issued by (Q)EAA Issuers to a Wallet Instance and MUST be provided in SD-JWT VC or mdoc-CBOR data format.
The (Q)EAA data model is use-case driven and may include different User attributes according to its specific purpose. The (Q)EAA metadata attributes are specific for each data format, as described in the following sections.

Format-Agnostic Credential Metadata Attributes
-----------------------------------------------

The following table defines the common metadata attributes that are applicable to Digital Credentials regardless of their encoding format. These attributes represent the semantic information about the Credential.

.. _table_format_agnostic_attributes:
.. list-table::
  :class: longtable
  :widths: 20 60
  :header-rows: 1

  * - **Data Identifier**
    - **Description**
  * - **credential_type_identifier**
    - REQUIRED. A unique and collision-resistant identifier that specifies the type and schema of the Digital Credential. It defines the set of claims/attributes that the Digital Credential contains and their structure.
  * - **issuing_authority**
    - REQUIRED. Name of the administrative authority that issued the Digital Credential.
  * - **issuing_country**
    - REQUIRED. Alpha-2 country code, as specified in ISO 3166-1, of the country or territory of the Credential Issuer.
  * - **issuance_date**
    - OPTIONAL. Date (and if possible time) when the Digital Credential was issued and/or the administrative validity period of the Digital Credential began.
  * - **expiry_date**
    - OPTIONAL. Date (and if possible time) when the Digital Credential will expire.
  * - **location_status**
    - OPTIONAL. The location of validity status information on the Digital Credential where the Credential Issuer revoke Digital Credential.
  * - **cryptographic_binding**
    - OPTIONAL. Object containing the proof-of-possession key materials.
  * - **verification**
    - OPTIONAL. Object containing Identity proofing and User data verification information.

The following sections provide format-specific attributes and a mapping of the above metadata attributes to format-specific technical parameters when the credential is encoded in SD-JWT VC or mdoc-CBOR format.

SD-JWT-VC Credential Format
---------------------------

When Digital Credentials are issued in the SD-JWT VC format, they MUST be compliant with the `SD-JWT`_ and `SD-JWT-VC`_ specifications.

SD-JWT-VC Digital Credentials MUST be signed using the Issuer's private key. SD-JWT VC Digital Credentials MAY be provided along with a Type Metadata Document related to the issued Credential according to Sections 6 and 6.3 of [`SD-JWT-VC`_]. The payload of Digital Credentials MUST contain the **_sd_alg** claim described in Section 4.1.1 `SD-JWT`_ and other claims specified in this section.

The claim **_sd_alg** indicates the hash algorithm used by the Issuer to generate the digests as described in Section 4.1.1 of `SD-JWT`_. **_sd_alg** MUST be set to one of the specified algorithms in Section :ref:`Cryptographic Algorithms <algorithms:Cryptographic Algorithms>`.

Claims that are not selectively disclosable MUST be included in the SD-JWT as they are. The digests of the disclosures, along with any decoy if present, MUST be contained in the **_sd** array, as specified in Section 4.2.4.1 of `SD-JWT`_.

The Disclosures are provided to the Holder together with the SD-JWT in the *Combined Format for Issuance* that is an ordered series of base64url-encoded values, each separated from the next by a single tilde ('~') character as follows:

.. code-block:: text

  <Issuer-Signed-JWT>~<Disclosure 1>~<Disclosure 2>~...~<Disclosure N>~

See `SD-JWT-VC`_ and `SD-JWT`_ for additional details.


Digital Credential SD-JWT Metadata Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The JOSE header contains the following mandatory parameters:

.. _table_sd-jwt-vc_jose_header:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **typ**
    - REQUIRED. It MUST be set to ``dc+sd-jwt`` as defined in `SD-JWT-VC`_.
    - :rfc:`7515` Section 4.1.9.
  * - **alg**
    - REQUIRED. Signature Algorithm.
    - :rfc:`7515` Section 4.1.1.
  * - **kid**
    - REQUIRED. Unique identifier of the public key.
    - :rfc:`7515` Section 4.1.8.
  * - **trust_chain**
    - OPTIONAL. JSON array containing the trust chain that proves the reliability of the issuer of the JWT.
    - [`OID-FED`_] Section 4.3.
  * - **x5c**
    - REQUIRED. Contains the X.509 public key certificate or certificate chain [:rfc:`5280`] corresponding to the key used to digitally sign the JWT.
    - :rfc:`7515` Section 4.1.8 and [`SD-JWT-VC`_] Section 3.5.

The JWT payload contains the following claims. Unless otherwise specified, the following claims MUST NOT be selectively disclosable.

.. _table_sd-jwt-vc_parameters:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - REQUIRED. *String*. URL string representing the Credential Issuer unique identifier.
      - `[RFC7519, Section 4.1.1] <https://www.iana.org/go/rfc7519>`_.
    * - **sub**
      - OPTIONAL. *String*. The identifier of the subject of the Digital Credential, the User, MUST be opaque and MUST NOT correspond to any anagraphic data or be derived from the User's anagraphic data via pseudonymization. Additionally, it is required that two different Credentials issued MUST NOT use the same ``sub`` value.
      - `[RFC7519, Section 4.1.2] <https://www.iana.org/go/rfc7519>`_.
    * - **iat**
      - OPTIONAL. UNIX Timestamp with the time of JWT issuance, coded as NumericDate as indicated in :rfc:`7519`.
      - `[RFC7519, Section 4.1.6] <https://www.iana.org/go/rfc7519>`_.
    * - **exp**
      - REQUIRED. UNIX Timestamp with the expiry time of the JWT, coded as NumericDate as indicated in :rfc:`7519`. In accordance with [`EIDAS-ARF`_] HLR **ISSU_12c** and **ISSU_12d** it MUST NOT be later than the expiration date of the Wallet Unit Attestation presented as part of the Digital Credential issuance process.
      - `[RFC7519, Section 4.1.4] <https://www.iana.org/go/rfc7519>`_.
    * - **nbf**
      - OPTIONAL. UNIX Timestamp with the start time of validity of the JWT, coded as NumericDate as indicated in :rfc:`7519`.
      - `[RFC7519, Section 4.1.4] <https://www.iana.org/go/rfc7519>`_.
    * - **issuing_authority**
      - REQUIRED. *String*. Format-encoded data identifier `issuing_authority` as defined in Section :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`.
      - Commission Implementing Regulation `EU_2024/2977`_.
    * - **issuing_country**
      - REQUIRED. *String*. Format-encoded data identifier `issuing_country` as defined in Section :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`.
      - Commission Implementing Regulation `EU_2024/2977`_.
    * - **issuance_date**
      - OPTIONAL. *String*. Format-encoded data identifier `issuance_date` as defined in Section :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`.  This attribute pertains to the administrative issuance date, which is typically different from the technical issuance date expressed by the JWT ``iat`` claim.
      - Section 2.6 of the ARF PID Rulebook v1.3 [`EIDAS-ARF`_].
    * - **date_of_expiry**
      - OPTIONAL. *String*. Format-encoded data identifier `expiry_date` as defined in Section :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`.  This attribute pertains to the administrative validity period of the Digital Credential, which is typically different from the technical validity period expressed by the JWT ``exp`` claim.
      - Commission Implementing Regulation `EU_2024/2977`_.
    * - **status**
      - OPTIONAL. REQUIRED only if the Digital Credential is long-lived. *JSON object*. Format-encoded data identifier `location_status` as defined in Section :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`. It MUST contain either the JSON member `status_list`.
      - Section 3.2.2.2 `SD-JWT-VC`_.
    * - **cnf**
      - OPTIONAL. *JSON object*. Format-encoded data identifier `cryptographic_binding` as defined in Section :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`, containing the proof-of-possession key materials. By including a **cnf** (confirmation) claim in a JWT, the Issuer of the JWT declares that the Holder is in control of the private key related to the public one defined in the **cnf** parameter. The recipient MUST cryptographically verify that the Holder is in control of that key.
      - `[RFC7800, Section 3.1] <https://www.iana.org/go/rfc7800>`_ and Section 3.2.2.2 `SD-JWT-VC`_.
    * - **vct**
      - REQUIRED. *String*. Format-encoded data identifier `credential_type_identifier` as defined in Section :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`. Credential type value MUST be a URN and it MUST be set using one of the values obtained from the Credential Issuer metadata, matching of the literals included in this URN MUST be performed in a case-sensitive manner. It is the identifier of the SD-JWT VC type and it MUST be set with a collision-resistant value as defined in Section 2 of :rfc:`7515`. It MUST contain also the number of version of the Credential type. Unless otherwise specified by `EIDAS-ARF`_ and EUDI Rulebooks, the `vct` SHOULD follow a structure like `urn:it-wallet:{credential_type}:{credential_type_version}`.
      - Section 3.2.2.2 `SD-JWT-VC`_.
    * - **vct#integrity**
      - OPTIONAL. *String*. The value MUST be an "integrity metadata" string as defined in Section 3 of [`W3C-SRI`_]. *SHA-256*, *SHA-384* and *SHA-512* MUST be supported as cryptographic hash functions. *MD5* and *SHA-1* MUST NOT be used. This claim MUST be verified according to Section 3.3.5 of [`W3C-SRI`_].
      - Section 6.1 `SD-JWT-VC`_, [`W3C-SRI`_]
    * - **verification**
      - OPTIONAL. *JSON object*. Format-encoded data identifier `verification` as defined in Section :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`. It includes the following sub-value:

          * ``trust_framework``: REQUIRED. *String* identifying the trust framework used for User authentication. It MUST be set using one of the values described in the `trust_frameworks_supported` map provided within the Credential Issuer Metadata.
          * ``assurance_level``: REQUIRED. *String* identifying the level of identity assurance guaranteed during the User authentication process. The value MUST match with one of the values mapped in the ``acr_values_supported`` array of the :ref:`credential-issuer-metadata:Credential Issuer Metadata`.

      - Domestic extension.
    * - **_sd**
      - REQUIRED. *Array of strings*, where each string represents a digest of a Disclosure.
      - 4.2.4.1 `SD-JWT`_
    * - **_sd_alg**
      - REQUIRED. *String*. Hash algorithm used by the Issuer to generate the digests.
      - 4.1.1 `SD-JWT`_


.. note::
  The standard JWT claims ``nbf`` and ``exp`` are used to express the technical validity period of a SD-JWT VC-compliant Digital Credential.

The ``status`` parameter ``status_list``, it MUST be a *JSON object* compliant with Section 6.2 of TOKEN-STATUS-LIST_.

(Q)EAA non-normative Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below is a non-normative example of (Q)EAA in JSON.

.. literalinclude:: ../../examples/qeaa-json-example-payload.json
  :language: JSON

The corresponding SD-JWT for the previous data is represented as follow, as decoded JSON for both header and payload.

.. literalinclude:: ../../examples/qeaa-sd-jwt-example-header.json
  :language: JSON

.. literalinclude:: ../../examples/qeaa-sd-jwt-example-payload.json
  :language: JSON

In the following the disclosure list is given:

**Claim** ``document_number``:

 * SHA-256 Hash: ``D4VkWjnA0WON7HdCGFtU869MSvORHPf8p5fQRD5gNj0``
 * Disclosure:
   ``WyJrZ2h0ZTVNRE5IYlFmZEpIcDg4cENBIiwgImRvY3VtZW50X251bWJlciIs``
   ``ICJYWFhYWFhYWFhYIl0``
 * Contents:
   ``["kghte5MDNHbQfdJHp88pCA", "document_number", "XXXXXXXXXX"]``


**Claim** ``given_name``:

 * SHA-256 Hash: ``qbRtUHp9Oax9dm5GeKnw_W12Yu1E2DoU6wrFPee7aBo``
 * Disclosure:
   ``WyJoWDFURXpfejg3N19YQXRyM0NPYVdnIiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
 * Contents:
   ``["hX1TEz_z877_XAtr3COaWg", "given_name", "Mario"]``


**Claim** ``family_name``:

 * SHA-256 Hash: ``Q7TX7kL8CNUp3BFBKP5xxIuPu5gRgkO6HplM3E1iMIc``
 * Disclosure:
   ``WyJZV3RJMDZ4RGRDeXZUYWxjSW5URTNBIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
 * Contents:
   ``["YWtI06xDdCyvTalcInTE3A", "family_name", "Rossi"]``


**Claim** ``birth_date``:

 * SHA-256 Hash: ``oF2qeWAbKO_qWGQ5z-HGKeifl2PMIEMbJe8L-PJ-wko``
 * Disclosure:
   ``WyItejM0Y0oxZ0M1VUJQQ0l4OE9oTmlRIiwgImJpcnRoX2RhdGUiLCAiMTk4``
   ``MC0wMS0xMCJd``
 * Contents:
   ``["-z34cJ1gC5UBPCIx8OhNiQ", "birth_date", "1980-01-10"]``


**Claim** ``tax_id_code``:

 * SHA-256 Hash: ``Wq3gFfmC0I9Lefw1mh-Bk5XPRtoSCg9aE23uOhxakas``
 * Disclosure:
   ``WyJLTmM1LUdrOUNRaF9UZEdicUJLSTdBIiwgInRheF9pZF9jb2RlIiwgIlRJ``
   ``TklULVhYWFhYWFhYWFhYWFhYWFgiXQ``
 * Contents:
   ``["KNc5-Gk9CQh_TdGbqBKI7A", "tax_id_code",``
   ``"TINIT-XXXXXXXXXXXXXXXX"]``


**Claim** ``constant_attendance_allowance``:

 * SHA-256 Hash: ``JOQk0kuBSVk80rFlv9VGY-yiIzsfzEJKk3d4RROfzkM``
 * Disclosure:
   ``WyIyaFFtWXBIeVgtbVpKaHoyeHNVWWNRIiwgImNvbnN0YW50X2F0dGVuZGFu``
   ``Y2VfYWxsb3dhbmNlIiwgdHJ1ZV0``
 * Contents:
   ``["2hQmYpHyX-mZJhz2xsUYcQ", "constant_attendance_allowance",``
   ``true]``


The combined format for the (Q)EAA issuance is represented below:

.. literalinclude:: ../../examples/qeaa-sd-jwt-example-combined.txt
  :language: text

Digital Credential Type Metadata Document
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When provided, the Type Metadata Document MUST be a *JSON object* compliant with Section 6.2 of [`SD-JWT-VC`_].

The Credential Type Metadata JSON Document MAY be retrieved through a *well-known* endpoint. See Section 6.3.3 of `SD-JWT-VC`_.
This endpoint, provided by the Credential Issuer, MUST have the following format: ``https://{Credential Issuer Domain}/.well-known/type-metadata``. The ``vct`` query parameter MUST be added to that endpoint.
The Endpoint returns a ``200 OK`` status code and supports ``application/json`` as content type.

Below a non-normative example is given.

.. code-block:: http

    GET /.well-known/type-metadata?vct=urn%3Aeudi%3Apid%3Ait%3A1 HTTP/1.1
    Host: pidprovider.example.it
    Accept: application/json

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "vct": "urn:eudi:pid:it:1",
      "name": "Person Identification Data",
      "description": "Digital version of Person Identification Data",
      ...
    }

mdoc-CBOR Credential Format
---------------------------

When Digital Credentials are issued in mdoc-CBOR format, they MUST be based on the ISO/IEC 18013-5 standard.

The mdoc data elements MUST be encoded in CBOR as defined in :rfc:`8949`.

This data model structures mdoc Digital Credentials into distinct components: namespaces (**nameSpaces**), and cryptographic proof (**issuerAuth**).
Namespaces categorize and structure data elements (or attributes, see :ref:`credential-data-model:Attribute Namespaces`). While the cryptographic proof ensures integrity and authenticity through the Mobile Security Object (MSO).

The MSO securely stores cryptographic digests of attributes within the `nameSpaces`. This allows Relying Parties to validate disclosed attributes against corresponding **digestID** values without revealing the entire Credential.
See :ref:`credential-data-model:Mobile Security Object` for details.

An mdoc-CBOR Digital Credential MUST be compliant with the following structure:

.. _table_mdoc_structure:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **nameSpaces**
      - *(map)*. The namespaces within which the data elements are defined. A Digital Credential MAY include multiple namespaces.
      - [ISO 18013-5#8.3.2.1.2]
    * - **issuerAuth**
      - *(COSE_Sign1)*. Contains *Mobile Security Object* (MSO), a COSE Sign1 Document, issued by the Credential Issuer.
      - [ISO 18013-5#9.1.2.4]


.. note::
  Mandatory mDL attributes utilize the standard namespace `org.iso.18013.5.1`. However, it MAY have a domestic namespace, such as `org.iso.18013.5.1.IT`, to include additional attributes defined in this implementation profile. Each namespace within the `nameSpaces` MUST share the same issued document type (`docType`) value, which identifies the nature of the Digital Credential, as defined in the `issuerAuth`.

The structure of an mdoc-CBOR Credential is further elaborated in the following sections.

Mobile Security Object
^^^^^^^^^^^^^^^^^^^^^^

The **issuerAuth** represents the `Mobile Security Object` which is a `COSE Sign1 Document` defined in :rfc:`9052`. It has the following data structure:

   * protected header
   * unprotected header
   * payload
   * signature.

The **protected header** MUST contain the following parameter encoded in CBOR format:

.. _table_protected_headers_mdoc:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Element**
      - **Description**
      - **Reference**
    * - **1**
      - *(int)*. Algorithm used to verify the cryptographic signature of the mdoc Digital Credential.
      - :rfc:`9053`

.. note::
  Only the signature algorithm MUST be present in the protected header, other elements SHOULD NOT be present in the protected header.

The **unprotected header** MUST contain the following parameters, unless otherwise specified:

.. _table_unprotected_headers_mdoc:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Element**
      - **Description**
      - **Reference**
    * - **4**
      - *(tstr, OPTIONAL)*. Unique identifier of the Issuer JWK. Required when the Issuer of mdoc uses OpenID Federation.
      - :ref:`infrastructure-trust:Infrastructure of Trust`
    * - **33**
      - *(array)*. X.509 certificate chain about the Issuer. Required for X.509 certificate-based authentication.
      - :rfc:`9360`

.. note::
  The `x5chain` is included in the unprotected header with the aim to allow the Holder to update the X.509 certificate chain, related to the `Mobile Security Object` issuer, without invalidating the signature.

The **payload** MUST contain the *MobileSecurityObject*, without the `content-type` COSE Sign header parameter and encoded as a *byte string* (bstr) using the *CBOR Tag* 24.

The `MobileSecurityObject` MUST have the following attributes, unless otherwise specified:

.. _table_MobileSecurityObject_attributes:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Element**
      - **Description**
      - **Reference**
    * - **docType**
      - *(tstr)*. Format-encoded data identifier `credential_type_identifier` as defined in Section :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`.

        - When defined by an ISO standard, It MUST be a string of the form ``iso.org.{iso-number}.{part}.{version}.{credential_type}`` (e.g. for an mDL, the value MUST be ``org.iso.18013.5.1.mDL``).

        - When defined at the european level, it MUST be a string of the form ``eu.europa.ec.eudi.{credential_type}.{version}`` (e.g., ``eu.europa.ec.eudi.pid.1``).

        - When defined at national level, it MUST be a string of the form ``{Trust Anchor reverse domain}.{credential_type}.{version}`` (e.g., ``it.wallet.trust-registry.pid.1``).

      - [ISO 18013-5#9.1.2.4]
    * - **version**
      - *(tstr)*. Version of the `MobileSecurityObject`.
      - [ISO 18013-5#9.1.2.4]
    * - **validityInfo**
      - *(map, REQUIRED)*. Contains the `MobileSecurityObject` issuance and expiration datetimes. It includes the following sub-values:

          * **signed** *(tdate, OPTIONAL)*. The timestamp indicating when the `MobileSecurityObject` was signed.
          * **validFrom** *(tdate, OPTIONAL)*. Timestamp before which the `MobileSecurityObject` is not considered valid. When present, it MUST be equal to or later than the `signed` time.
          * **validUntil** *(tdate, REQUIRED)*. Timestamp after which the `MobileSecurityObject` is no longer considered valid. In accordance with [`EIDAS-ARF`_] HLR **ISSU_12c** and **ISSU_12d** it MUST NOT be later than the expiration date of the Wallet Unit Attestation presented as part of the Digital Credential issuance process.

      - [ISO 18013-5#9.1.2.4]
    * - **digestAlgorithm**
      - *(tstr)*. Identifier of the digest algorithm, which MUST match the algorithm defined in the protected header.
      - [ISO 18013-5#9.1.2.4]
    * - **valueDigests**
      - *(map)*. Maps each namespace identifier to a set of digests, where each digest is keyed by a unique `digestID` and holds the digest value.
      - [ISO 18013-5#9.1.2.4]
    * - **deviceKeyInfo**
      - *(map)*. Contains metadata about the Wallet Instance's public key. It MUST include the following sub-fields, unless otherwise specified:

          * **deviceKey** *(COSE_Key)*. Contains the public key parameters.
          * **keyAuthorizations** *(map, OPTIONAL)*. Defines authorizations for either full namespaces or individual data elements.
          * **keyInfo** *(map, OPTIONAL)*. Contains additional metadata about the key.

      - [ISO 18013-5#9.1.2.4]
    * - **status**
      - *(map, OPTIONAL)*. REQUIRED only if the Digital Credential is long-lived. Format-encoded data identifier `location_status` as defined in Section :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`. Contains the MSO revocation information. If present, it includes a *status_list* based on the TOKEN-STATUS-LIST_ mechanism as defined in Section 6.3 of TOKEN-STATUS-LIST_.
      - [ISO 18013-5#9.1.2.6]

.. note::
  The private key related to the public key stored in the `deviceKey` map is used to sign the `DeviceSignedItems` and to prove the possession of the Digital Credential during the presentation phase (see the presentation phase with mdoc-CBOR).

Attribute Namespaces
^^^^^^^^^^^^^^^^^^^^

The **nameSpaces** contains one or more *nameSpace* entries, each identified by a name. Within each **nameSpace**, it includes one or more *IssuerSignedItemBytes*, each encoded as a CBOR byte string with Tag 24 (#6.24(bstr .cbor)), which appears as 24(<<... >>) in diagnostic notation. It represents the disclosure information for each digest within the `Mobile Security Object` and MUST contain the following attributes:

.. _table_attribute_namespaces:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Name**
      - **Description**
      - **Reference**
    * - **digestID**
      - *(uint)*. Reference value to one of the ``ValueDigests`` provided in the *Mobile Security Object*.
      - [ISO 18013-5#9.1.2.5]
    * - **random**
      - *(bstr)*. Random byte value used as salt for the hash function. This value MUST be different for each *IssuerSignedItem* and it MUST have a minimum length of 16 bytes.
      - [ISO 18013-5#9.1.2.5]
    * - **elementIdentifier**
      - *(tstr)*. Data element identifier.
      - [ISO 18013-5#8.3.2.1.2.3]
    * - **elementValue**
      - *(any)*. Data element value.
      - [ISO 18013-5#8.3.2.1.2.3]

Digital Credential mdoc-CBOR Metadata Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following **elementIdentifiers** representing format-encoded metadata attributes are defined for Digital Credentials in mdoc-CBOR format within the respective *nameSpace*:

.. _table_element_identifiers_mdoc:
.. list-table::
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Element Identifier**
     - **Description**
     - **Reference**

   * - **issuing_country**
     - *(tstr, REQUIRED)*. Format-encoded data identifier `issuing_country` as defined in Section :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`. Alpha-2 country code as defined in [ISO 3166-1].
     - [ISO 18013-5#7.2]

   * - **issuing_authority**
     - *(tstr, REQUIRED)*. Format-encoded data identifier `issuing_authority` as defined in Section :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`. The value MUST only use Latin1b characters and MUST have a maximum length of 150 characters.
     - [ISO 18013-5#7.2]

   * - **issuance_date**
     - *(tdate or full-date, OPTIONAL)*. Format-encoded data identifier `issuance_date` as defined in Section :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`.  This attribute pertains to the administrative issuance date, which is typically different from the technical issuance date expressed by the `MobileSecurityObject` parameters ``signed`` or ``validFrom``.
     - Section 2.6 of the ARF PID Rulebook v1.3 [`EIDAS-ARF`_].

   * - **expiry_date**
     - *(tdate or full-date, OPTIONAL)*. Format-encoded data identifier `expiry_date` as defined in Section :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`. It MUST be according to ISO 8601-1 YYYY-MM-DD format.
     - Section 3 of the ARF PID Rulebook v1.3 [`EIDAS-ARF`_]

   * - **sub**
     - *(uuid, OPTIONAL)*. Identifies the subject of the mdoc Digital Credential (the User). The identifier MUST be opaque, MUST NOT correspond to any anagraphic data, and MUST NOT be derived from the User's anagraphic data through pseudonymization. Additionally, different Credentials issued to the same User or to different Users MUST NOT use the same `sub` value.
     - Domestic extension.

   * - **verification**
     - *(map, OPTIONAL)*. Format-encoded data identifier `verification` as defined in Section :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`. The CBOR map includes the following members:

         * ``trust_framework`` *(tstr, REQUIRED)*: trust framework used for User authentication.
         * ``assurance_level`` *(tstr, REQUIRED)*: level of identity assurance guaranteed during User authentication. The value MUST match with one of the values mapped in the ``acr_values_supported`` array of the :ref:`credential-issuer-metadata:Credential Issuer Metadata`.

     - Domestic extension.

.. note::
  Digital Credential User-specific attributes are defined in the Catalog of Digital Credentials.
  User-specific attributes for mdoc Digital Credentials such as those used in mDL or PID are also included by referencing the appropriate `elementIdentifiers` defined in ISO/IEC 18013-5 or the `EIDAS-ARF`_ specification.

.. note::
  Regardless of the Digital Credential type, the `sub` value MUST NOT be shown to the User, as it is not a User attribute. It is used for identification purposes by the Credential Issuers.


mdoc-CBOR Examples
^^^^^^^^^^^^^^^^^^

A non-normative example of an mDL encoded in CBOR is shown below in binary encoding.

.. literalinclude:: ../../examples/mDL-cbor-encoded-example.txt
  :language: text

The Diagnostic Notation of the CBOR-encoded mDL is given below.

.. literalinclude:: ../../examples/mDL-mdoc-cbor-example.txt
  :language: text

CBOR Acronyms
^^^^^^^^^^^^^

.. list-table::
   :class: longtable
   :widths: 20 80
   :header-rows: 1

   * - **Acronym**
     - **Meaning**
   * - `tstr`
     - Text String
   * - `bstr`
     - Byte String
   * - `int`
     - Signed Integer
   * - `uint`
     - Unsigned Integer
   * - `uuid`
     - Universally Unique Identifier
   * - `bool`
     - Boolean (true/false)
   * - `tdate`
     - Tagged Date (for example, Tag `0` is used to indicate a date/time string in :RFC:`3339` format)

Cross-Format Credential Parameters Mapping
------------------------------------------

The following table provides a comparative mapping between the data structures of SD-JWT VC and mdoc-CBOR Digital Credentials.
It outlines the key data elements and parameters used in each format, highlighting both commonalities and differences.
In particular, it shows how core concepts - such as Credential Issuer information, validity, Cryptographic Binding, and disclosures - are represented in these Credential formats.

For SD-JWT-VC, parameters are marked with `(hdr)` if they are located in the JOSE header, and `(pld)` if they appear in the payload of the JWT. In mdoc-CBOR, these parameters are identified within the issuerAuth or nameSpaces structures.

.. list-table::
   :class: longtable
   :widths: 20 40 40
   :header-rows: 1

   * - **Information Related To**
     - **SD-JWT-VC Parameters**
     - **mdoc-CBOR Parameters**
   * - Digital Credential type definition
     - vct (pld)
     - | issuerAuth.doctype
   * - Issuer
     - | iss (pld)
       | issuing_authority (pld)
       | issuing_country (pld)
     - | -
       | nameSpaces.elementIdentifier.issuing_authority
       | nameSpaces.elementIdentifier.issuing_country
   * - Subject
     - sub (pld)
     - nameSpaces.elementIdentifier.sub
   * - Validity period
     - | iat (pld)
       | exp (pld)
       | nbf (pld)
       | expiry_date (pld)
     - | issuerAuth.validityInfo.signed
       | issuerAuth.validityInfo.validUntil
       | issuerAuth.validityInfo.validFrom
       | nameSpaces.elementIdentifier.expiry_date
   * - Status mechanism
     - | status_list (pld)
     - | issuerAuth.status_list
   * - Signature
     - | alg (hdr)
       | kid (hdr)
     - | issuerAuth.1 (alg)
       | issuerAuth.4 (kid)
   * - Trust anchors
     - | trust_chain (OID-FED) (hdr)
       | x5c (hdr)
     - | -
       | issuerAuth.33 (x5chain)
   * - Cryptographic Binding
     - cnf.jwk (pld)
     - issuerAuth.deviceKeyInfo.deviceKey
   * - Selective Disclosure
     - | _sd_alg (pld)
       | _sd (pld)
     - | issuerAuth.digestAlgorithm
       | issuerAuth.valueDigests
   * - Integrity
     - | vct#integrity (pld)
       | Type_Metadata.extends#integrity (hdr)
     - |
       | -
   * - Digital Credential format
     - typ (hdr)
     - |
       | -
       |
   * - Digital Credential auditability
     - verification (pld)
     - nameSpaces.elementIdentifier.verification
   * - Disclosures
     - | salt
       | claim name
       | claim value
     - |
       | nameSpaces
       |


