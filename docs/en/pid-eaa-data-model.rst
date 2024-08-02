
.. include:: ../common/common_definitions.rst

.. _pid_eaa_data_model.rst:

PID/(Q)EAA Data Model
+++++++++++++++++++++

The Person Identification Data (PID) is issued by the PID Provider according to national laws. The main scope of the PID is allowing natural persons to be authenticated for the access to a service or to a protected resource. 
The User attributes provided within the Italian PID are the ones listed below:

    - Current Family Name
    - Current First Name
    - Date of Birth
    - Unique Identifier
    - Taxpayer identification number

The (Q)EAAs are issued by (Q)EAA Issuers to a Wallet Instance and MUST be provided in SD-JWT-VC or MDOC-CBOR data format. 

The PID/(Q)EAA data format and the mechanism through which a digital credential is issued to the Wallet Instance and presented to a Relying Party are described in the following sections. 

SD-JWT-VC Credential Format
===========================

The PID/(Q)EAA is issued in the form of a Digital Credential. The Digital Credential format is `SD-JWT`_ as specified in `SD-JWT-VC`_.

An SD-JWT is a JWT that MUST be signed using the Issuer's private key. The SD-JWT MUST be provided along with a Type Metadata related to the issued Digital Credential according to Sections 6 and 6.3 of [`SD-JWT-VC`_]. The payload MUST contain the **_sd_alg** claim described in the Section 5.1.1 `SD-JWT`_ and other claims specified in this section, some of them may be selectively disclosable claims. 

The claim **_sd_alg** indicates the hash algorithm used by the Issuer to generate the digests as described in Section 5.1.1 of `SD-JWT`_. The **_sd_alg** claim MUST be set to one of the specified algorithms in Section :ref:`Cryptographic Algorithms <supported_algs>`.

Claims that are not selectively disclosable MUST be included in the SD-JWT in plaintext.  The digests of the disclosures (and decoy digests, if any) related to an object element claim that is selectively disclosable MUST be contained in a new JWT claim, **_sd** as specified in Section 5.2.4.1 of `SD-JWT`_. 

Each digest value ensures the integrity of, and maps to, the respective Disclosure. Digest values are calculated using a hash function over the disclosures, each of which contains:

  - a random salt, 
  - the claim name (only when the claim is an object element), 
  - the claim value. 

In case of nested object in a SD-JWT payload each claim, on each level of the JSON, should be individually selectively disclosable or not. Therefore **_sd** claim containing digests MAY appear multiple times in the SD-JWT.

For each claim that is an array element the digests of the respective disclosures and decoy digests are added to the array in the same position of the original claim values as specified in Section 5.2.4.2 of `SD-JWT`_.

In case of array elements, digest values are calculated using a hash function over the disclosures, containing:

  - a random salt, 
  - the array element

In case of multiple array elements, the Issuer may wish to conceal presence of any statement while also	allowing the holder to reveal each of those	elements individually (Section 5.2.6 `SD-JWT`_). Both the entire array and the individuals entries could be selective disclosure.

The Disclosures are provided to the Holder together with the SD-JWT in the *Combined Format for Issuance* that MUST be an ordered series of base64url-encoded values, each separated from the next by a single tilde ('~') character as follows:

.. code-block::

  <Issuer-Signed-JWT>~<Disclosure 1>~<Disclosure 2>~...~<Disclosure N>

See `SD-JWT-VC`_ and `SD-JWT`_ for additional details. 


PID/(Q)EAA SD-JWT parameters
----------------------------

The JOSE header contains the following mandatory parameters:

.. _pid_jose_header:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **typ**
    - REQUIRED. It MUST be set to ``vc+sd-jwt`` as defined in `SD-JWT-VC`_. 
    - `[RFC7515, Section 4.1.9] <https://datatracker.ietf.org/doc/html/rfc7515#section-4.1.9>`_.
  * - **alg**
    - REQUIRED. Signature Algorithm. 
    - `[RFC7515, Section 4.1.1] <https://datatracker.ietf.org/doc/html/rfc7515#section-4.1.1>`_.
  * - **kid**
    - REQUIRED. Unique identifier of the public key. 
    - `[RFC7515, Section 4.1.8] <https://datatracker.ietf.org/doc/html/rfc7516.html#section-4.1.8>`_.
  * - **trust_chain**
    - OPTIONAL. JSON array containing the trust chain that proves the reliability of the issuer of the JWT. 
    - [`OID-FED`_] Section 3.2.1.
  * - **vctm**
    - OPTIONAL. JSON array of base64url-encoded Type Metadata JSON documents. In case of extended type metadata, this claim contains the entire chain of JSON documents. 
    - [`SD-JWT-VC`_] Section 6.3.5.

The following claims MUST be in the JWT payload. Some of these claims can be disclosed, these are listed in the following tables that specify whether a claim is selectively disclosable [SD] or not [NSD].

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - [NSD].URL string representing the PID/(Q)EAA Issuer unique identifier.
      - `[RFC7519, Section 4.1.1] <https://www.iana.org/go/rfc7519>`_.
    * - **sub**
      - [NSD]. The identifier of the subject of the Digital Credential, the User, MUST be opaque and MUST NOT correspond to any anagraphic data or be derived from the User's anagraphic data via pseudonymization. Additionally, it is required that two different Credentials issued MUST NOT use the same ``sub`` value.
      - `[RFC7519, Section 4.1.2] <https://www.iana.org/go/rfc7519>`_.
    * - **iat**
      - [SD].UNIX Timestamp with the time of JWT issuance, coded as NumericDate as indicated in :rfc:`7519`.
      - `[RFC7519, Section 4.1.6] <https://www.iana.org/go/rfc7519>`_.
    * - **exp**
      - [NSD].UNIX Timestamp with the expiry time of the JWT, coded as NumericDate as indicated in :rfc:`7519`.
      - `[RFC7519, Section 4.1.4] <https://www.iana.org/go/rfc7519>`_.
    * - **status**
      - [NSD].it MUST be a valid JSON object containing the information on how to read the status of the Verifiable Credential. It MUST contain the JSON member *status_attestation* set to a JSON Object containing the *credential_hash_alg* claim indicating the Algorithm used for hashing the Digital Credential to which the Status Attestation is bound. It is RECOMMENDED to use *sha-256*. 
      - Section 3.2.2.2 `SD-JWT-VC`_ and Section 11 `OAUTH-STATUS-ASSERTION`_.
    * - **cnf**
      - [NSD].JSON object containing the proof-of-possession key materials. By including a **cnf** (confirmation) claim in a JWT, the issuer of the JWT declares that the Holder is in control of the private key related to the public one defined in the **cnf** parameter. The recipient MUST cryptographically verify that the Holder is in control of that key.
      - `[RFC7800, Section 3.1] <https://www.iana.org/go/rfc7800>`_ and Section 3.2.2.2 `SD-JWT-VC`_.
    * - **vct**
      - [NSD].Credential type value MUST be a case-sensitive StringOrURI (see :rfc:`7519`) and MUST be set in accordance to the type obtained from the PID/(Q)EAA Issuer metadata. It serves as an identifier for the type of the SD-JWT VC and MUST be a Collision-Resistant Name as defined in Section 2 of :rfc:`7515`. It MUST contains also the number of version of the Credential type, for example, in the case of the PID, it is ``https://issuer.example.org/v1.0/personIdentificationData``.
      - Section 3.2.2.2 `SD-JWT-VC`_.
    * - **vct#integrity**
      - [NSD].The value MUST be an "integrity metadata" string as defined in Section 3 of [`W3C-SRI`_]. *SHA-256*, *SHA-384* and *SHA-512* MUST be supported as cryptographic hash functions. *MD5* and *SHA-1* MUST NOT be used. This claim MUST be verified according to Section 3.3.5 of [`W3C-SRI`_].
      - Section 6.1 `SD-JWT-VC`_, [`W3C-SRI`_]
    * - **verification**
      - [NSD].Object containing user authentication information. It MUST contain the following sub-value:

          * ``auth_trust_framework``: trust framework used for user digital authetication.
          * ``assurance_level``: level of identity assurance guarateed (LoA) during the authentication process.
          * ``auth_method``: digital identity system used for the authentication.
      - This specification

.. note::

    Credential Type Metadata JSON Document MAY be retrieved directly from URL contained in the claim **vct** using the HTTP GET method or using the vctm header parameter if provided. Unlike specified in Section 6.3.1 of `SD-JWT-VC`_ the **.well-known** endpoint is not supported in the current implementation profile.


Digital Credential Metadata Type
--------------------------------

The Type Metadata document MUST be a JSON object and contains the following parameters.

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **name**
      - A human-readable name of the Digital Credential type. In case of multiple language, the language tags are added to member name, delimited by a # character as defined in :rfc:`5646`.
      - [`SD-JWT-VC`_] Section 6.2 and [`OIDC`_] Section 5.2.
    * - **description**
      - A human-readable description of the Digital Credential type. In case of multiple language, the language tags are added to member name, delimited by a # character as defined in :rfc:`5646`.
      - [`SD-JWT-VC`_] Section 6.2 and [`OIDC`_] Section 5.2.
    * - **extends**
      - String Identitifier of an exteded metadata type document.
      - [`SD-JWT-VC`_] Section 6.2.
    * - **extends#integrity**
      - CONDITIONAL. REQUIRED if **extends** is present.
      - [`SD-JWT-VC`_] Section 6.2.
    * - **schema**
      - CONDITIONAL. REQUIRED if **schema_uri** is not present.
      - [`SD-JWT-VC`_] Section 6.2.
    * - **schema_uri**
      - CONDITIONAL. REQUIRED if **schema** is not present.
      - [`SD-JWT-VC`_] Section 6.2.
    * - **schema#integrity**
      - CONDITIONAL. REQUIRED if **schema_uri** is not present.
      - [`SD-JWT-VC`_] Section 6.2.
    * - **data_source**
      - Object containing information about the data origin. It MUST contain the object ``verification`` with this following sub-value:

          * ``trust_framework``: MUST cointain trust framework used for digital authentication towards authentic source system.
          * ``authentic_source``: MUST contain ``organization_name`` and ``organization_code`` cliam related to name and code identifier of the authentic source.
      - This specification
    * - **vc_claims**
      - Object containing useful information about the Digital credential graphical rappresentation. It MUST contain the for each credential claim the following objects:

          * ``display``: MUST cointain name human-readable display name.
          * ``graphics``: MUST contain position, font character, color, size.
      - This specification


A non-normative Digital Credential metadata type is provided below.

.. literalinclude:: ../../examples/vc-metadata-type.json
  :language: JSON  

.. _sec-pid-user-claims:   

PID Claims
----------

Depending on the Digital Credential type **vct**, additional claims data MAY be added. The PID MUST support the following data:

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **given_name**
      - [SD]. Current First Name.
      - `[OpenID Connect Core 1.0, Section 5.1] <http://openid.net/specs/openid-connect-core-1_0.html>`_
    * - **family_name**
      - [SD]. Current Family Name.
      - `[OpenID Connect Core 1.0, Section 5.1] <http://openid.net/specs/openid-connect-core-1_0.html>`_
    * - **birth_date**
      - [SD]. Date of Birth.
      - 
    * - **unique_id**
      - [SD]. Unique citizen identifier (ID ANPR) given by the National Register of the Resident Population (ANPR). It MUST be set according to `ANPR rules <https://www.anagrafenazionale.interno.it/anpr/notizie/identificativo-unico-nazionale-idanpr/>`_
      - 
    * - **tax_id_code**
      - [SD]. National tax identification code of natural person as a String format. It MUST be set according to ETSI EN 319 412-1. For example ``TINIT-<ItalianTaxIdentificationNumber>``
      - 

The PID attribute schema, which encompasses all potential User data, is defined in `ARF v1.4 <https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/arf.md#21-identification-and-authentication-to-access-online-services>`_, and furthermore detailed in the `PID Rulebook <https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/annexes/annex-3/annex-3.01-pid-rulebook.md#23-pid-attributes>`_.


PID Non-Normative Examples
--------------------------

In the following, the non-normative example of the payload of a PID represented in JSON format.

.. literalinclude:: ../../examples/pid-json-example-payload.json
  :language: JSON  

The corresponding SD-JWT version for PID is given by

.. literalinclude:: ../../examples/pid-sd-jwt-example-header.json
  :language: JSON    

.. literalinclude:: ../../examples/pid-sd-jwt-example-payload.json
  :language: JSON  

In the following the disclosure list is given

**Claim** ``iat``:

-  SHA-256 Hash: ``7WG4nT6K26_R3975zcwnVwgoHA7b988_3-vJzbZf6Yc``
-  Disclosure:
   ``WyI1N212eWNUaDV5WkNyS0xaNXhuZlV3IiwgImlhdCIsIDE2ODMwMDAwMDBd``
-  Contents: ``["57mvycTh5yZCrKLZ5xnfUw", "iat", 1683000000]``

**Claim** ``unique_id``:

-  SHA-256 Hash: ``NOxVzjUJg667iBdeDwmr6tZ46X-jchKwIVxMAfv43yc``
-  Disclosure:
   ``WyJrdWNyQm1sb19oTWFJRkY1ODVSemFRIiwgInVuaXF1ZV9pZCIsICJ4eHh4``
   ``eHh4eC14eHh4LXh4eHgteHh4eC14eHh4eHh4eHh4eHgiXQ``
-  Contents: ``["kucrBmlo_hMaIFF585RzaQ", "unique_id",``
   ``"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]``

**Claim** ``given_name``:

-  SHA-256 Hash: ``wyfxVqq9BosPT7tN4SHOI4E48P19aVA1ktW5Zf0E-fc``
-  Disclosure:
   ``WyJOVE5Sb09pdVZWUnRGNkNFenRkOVp3IiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
-  Contents: ``["NTNRoOiuVVRtF6CEztd9Zw", "given_name", "Mario"]``

**Claim** ``family_name``:

-  SHA-256 Hash: ``UHChpGtNF2bj1FvAfBby1rnf7WXkxelFJ5a4vSj2FO4``
-  Disclosure:
   ``WyJGRFNTUGdnekdCVXdRTEhEU0U2d1FRIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
-  Contents: ``["FDSSPggzGBUwQLHDSE6wQQ", "family_name", "Rossi"]``

**Claim** ``birth_date``:

-  SHA-256 Hash: ``TK2RguPYoXzCx0vv5hbN9u5M2mHlWBt41qGWlLXCNu8``
-  Disclosure:
   ``WyJLWjhlNXdWRXREdmIxemlTUEE0RHpBIiwgImJpcnRoX2RhdGUiLCAiMTk4``
   ``MC0wMS0xMCJd``
-  Contents: ``["KZ8e5wVEtDvb1ziSPA4DzA", "birth_date", "1980-01-10"]``

**Claim** ``tax_id_code``:

-  SHA-256 Hash: ``q6Tqnxau97tu-MqUDg0fSAmLGZdSuMUMk6a2s3bcsC0``
-  Disclosure:
   ``WyJwWjVNUnlPeHBWV1p1SExvSi15alJnIiwgInRheF9pZF9jb2RlIiwgIlRJ``
   ``TklULVhYWFhYWFhYWFhYWFhYWFgiXQ``
-  Contents: ``["pZ5MRyOxpVWZuHLoJ-yjRg", "tax_id_code",``
   ``"TINIT-XXXXXXXXXXXXXXXX"]``



The combined format for the PID issuance is given by

.. code-block::

  eyJhbGciOiAiRVMyNTYiLCAidHlwIjogImV4YW1wbGUrc2Qtand0In0.eyJfc2QiOiBb
  IjdXRzRuVDZLMjZfUjM5NzV6Y3duVndnb0hBN2I5ODhfMy12SnpiWmY2WWMiLCAiTk94
  VnpqVUpnNjY3aUJkZUR3bXI2dFo0NlgtamNoS3dJVnhNQWZ2NDN5YyIsICJUSzJSZ3VQ
  WW9YekN4MHZ2NWhiTjl1NU0ybUhsV0J0NDFxR1dsTFhDTnU4IiwgIlVIQ2hwR3RORjJi
  ajFGdkFmQmJ5MXJuZjdXWGt4ZWxGSjVhNHZTajJGTzQiLCAicTZUcW54YXU5N3R1LU1x
  VURnMGZTQW1MR1pkU3VNVU1rNmEyczNiY3NDMCIsICJ3eWZ4VnFxOUJvc1BUN3RONFNI
  T0k0RTQ4UDE5YVZBMWt0VzVaZjBFLWZjIl0sICJleHAiOiAxODgzMDAwMDAwLCAiaXNz
  IjogImh0dHBzOi8vcGlkcHJvdmlkZXIuZXhhbXBsZS5vcmciLCAic3ViIjogIk56Ykxz
  WGg4dURDY2Q3bm9XWEZaQWZIa3hac1JHQzlYcyIsICJzdGF0dXMiOiB7InN0YXR1c19h
  dHRlc3RhdGlvbiI6IHsiY3JlZGVudGlhbF9oYXNoX2FsZyI6ICJzaGEtMjU2In19LCAi
  dmN0IjogIlBlcnNvbklkZW50aWZpY2F0aW9uRGF0YSIsICJfc2RfYWxnIjogInNoYS0y
  NTYiLCAiY25mIjogeyJqd2siOiB7Imt0eSI6ICJFQyIsICJjcnYiOiAiUC0yNTYiLCAi
  eCI6ICJUQ0FFUjE5WnZ1M09IRjRqNFc0dmZTVm9ISVAxSUxpbERsczd2Q2VHZW1jIiwg
  InkiOiAiWnhqaVdXYlpNUUdIVldLVlE0aGJTSWlyc1ZmdWVjQ0U2dDRqVDlGMkhaUSJ9
  fX0.A36ovweqpCpPkYHX75dg-HIib7zQKlfmMCaixlpOCmEl1CxlX-NtZbFn_kdN0nlJ
  YMLay4xSeetmic_ScLTxdg~WyI1N212eWNUaDV5WkNyS0xaNXhuZlV3IiwgImlhdCIsI
  DE2ODMwMDAwMDBd~WyJrdWNyQm1sb19oTWFJRkY1ODVSemFRIiwgInVuaXF1ZV9pZCIs
  ICJ4eHh4eHh4eC14eHh4LXh4eHgteHh4eC14eHh4eHh4eHh4eHgiXQ~WyJOVE5Sb09pd
  VZWUnRGNkNFenRkOVp3IiwgImdpdmVuX25hbWUiLCAiTWFyaW8iXQ~WyJGRFNTUGdnek
  dCVXdRTEhEU0U2d1FRIiwgImZhbWlseV9uYW1lIiwgIlJvc3NpIl0~WyJLWjhlNXdWRX
  REdmIxemlTUEE0RHpBIiwgImJpcnRoX2RhdGUiLCAiMTk4MC0wMS0xMCJd~WyJwWjVNU
  nlPeHBWV1p1SExvSi15alJnIiwgInRheF9pZF9jb2RlIiwgIlRJTklULVhYWFhYWFhYW
  FhYWFhYWFgiXQ~

(Q)EAA non-normative examples
-----------------------------

In the following, we provide a non-normative example of (Q)EAA in JSON.

.. literalinclude:: ../../examples/qeaa-json-example-payload.json
  :language: JSON  

The corresponding SD-JWT for the previous data is represented as follow, as decoded JSON for both header and payload.

.. literalinclude:: ../../examples/qeaa-sd-jwt-example-header.json
  :language: JSON  

.. literalinclude:: ../../examples/qeaa-sd-jwt-example-payload.json
  :language: JSON  

In the following the disclosure list is given:

**Claim** ``iat``:

-  SHA-256 Hash: ``7WG4nT6K26_R3975zcwnVwgoHA7b988_3-vJzbZf6Yc``
-  Disclosure:
   ``WyI1N212eWNUaDV5WkNyS0xaNXhuZlV3IiwgImlhdCIsIDE2ODMwMDAwMDBd``
-  Contents: ``["57mvycTh5yZCrKLZ5xnfUw", "iat", 1683000000]``

**Claim** ``document_number``:

-  SHA-256 Hash: ``AFRJaRPZTMaNxYu5IIWPifOAXJCnK-_h1eJt7MymcgM``
-  Disclosure:
   ``WyJrdWNyQm1sb19oTWFJRkY1ODVSemFRIiwgImRvY3VtZW50X251bWJlciIs``
   ``ICJYWFhYWFhYWFhYIl0``
-  Contents:
   ``["kucrBmlo_hMaIFF585RzaQ", "document_number", "XXXXXXXXXX"]``

**Claim** ``given_name``:

-  SHA-256 Hash: ``wyfxVqq9BosPT7tN4SHOI4E48P19aVA1ktW5Zf0E-fc``
-  Disclosure:
   ``WyJOVE5Sb09pdVZWUnRGNkNFenRkOVp3IiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
-  Contents: ``["NTNRoOiuVVRtF6CEztd9Zw", "given_name", "Mario"]``

**Claim** ``family_name``:

-  SHA-256 Hash: ``UHChpGtNF2bj1FvAfBby1rnf7WXkxelFJ5a4vSj2FO4``
-  Disclosure:
   ``WyJGRFNTUGdnekdCVXdRTEhEU0U2d1FRIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
-  Contents: ``["FDSSPggzGBUwQLHDSE6wQQ", "family_name", "Rossi"]``

**Claim** ``birth_date``:

-  SHA-256 Hash: ``TK2RguPYoXzCx0vv5hbN9u5M2mHlWBt41qGWlLXCNu8``
-  Disclosure:
   ``WyJLWjhlNXdWRXREdmIxemlTUEE0RHpBIiwgImJpcnRoX2RhdGUiLCAiMTk4``
   ``MC0wMS0xMCJd``
-  Contents: ``["KZ8e5wVEtDvb1ziSPA4DzA", "birth_date", "1980-01-10"]``

**Claim** ``expiry_date``:

-  SHA-256 Hash: ``i9XHLePHyV8OM35l3nf1MKqfpWuD7OFpRamSAsX0-5g``
-  Disclosure:
   ``WyJwWjVNUnlPeHBWV1p1SExvSi15alJnIiwgImV4cGlyeV9kYXRlIiwgIjIw``
   ``MjQtMDEtMDEiXQ``
-  Contents: ``["pZ5MRyOxpVWZuHLoJ-yjRg", "expiry_date", "2024-01-01"]``

**Claim** ``tax_id_code``:

-  SHA-256 Hash: ``-LLA7MCh-YWWYNzFfwZsJBGGiE096fN8d60a-ml3sgo``
-  Disclosure:
   ``WyJqdFZ1S0NwbjdiVGNIckFnX3NlVWJRIiwgInRheF9pZF9jb2RlIiwgIlRJ``
   ``TklULVhYWFhYWFhYWFhYWFhYWFgiXQ``
-  Contents: ``["jtVuKCpn7bTcHrAg_seUbQ", "tax_id_code",``
   ``"TINIT-XXXXXXXXXXXXXXXX"]``

**Claim** ``constant_attendance_allowance``:

-  SHA-256 Hash: ``rhPkItz7BGGpjnWX2SGVH_OV9VhRjz9Hx_INXwBbz6o``
-  Disclosure:
   ``WyJXRGtkNkpzTmhERnZMUDRzMWhRZHlBIiwgImNvbnN0YW50X2F0dGVuZGFu``
   ``Y2VfYWxsb3dhbmNlIiwgdHJ1ZV0``
-  Contents:
   ``["WDkd6JsNhDFvLP4s1hQdyA", "constant_attendance_allowance",``
   ``true]``


The combined format for the PID issuance is represented below:

.. code-block::

  eyJhbGciOiAiRVMyNTYiLCAidHlwIjogImV4YW1wbGUrc2Qtand0In0.eyJfc2QiOiBb
  Ii1MTEE3TUNoLVlXV1lOekZmd1pzSkJHR2lFMDk2Zk44ZDYwYS1tbDNzZ28iLCAiN1dH
  NG5UNksyNl9SMzk3NXpjd25Wd2dvSEE3Yjk4OF8zLXZKemJaZjZZYyIsICJBRlJKYVJQ
  WlRNYU54WXU1SUlXUGlmT0FYSkNuSy1faDFlSnQ3TXltY2dNIiwgIlRLMlJndVBZb1h6
  Q3gwdnY1aGJOOXU1TTJtSGxXQnQ0MXFHV2xMWENOdTgiLCAiVUhDaHBHdE5GMmJqMUZ2
  QWZCYnkxcm5mN1dYa3hlbEZKNWE0dlNqMkZPNCIsICJpOVhITGVQSHlWOE9NMzVsM25m
  MU1LcWZwV3VEN09GcFJhbVNBc1gwLTVnIiwgInJoUGtJdHo3QkdHcGpuV1gyU0dWSF9P
  VjlWaFJqejlIeF9JTlh3QmJ6Nm8iLCAid3lmeFZxcTlCb3NQVDd0TjRTSE9JNEU0OFAx
  OWFWQTFrdFc1WmYwRS1mYyJdLCAiZXhwIjogMTg4MzAwMDAwMCwgImlzcyI6ICJodHRw
  czovL2lzc3Vlci5leGFtcGxlLm9yZyIsICJzdWIiOiAiTnpiTHNYaDh1RENjZDdub1dY
  RlpBZkhreFpzUkdDOVhzIiwgInN0YXR1cyI6IHsic3RhdHVzX2F0dGVzdGF0aW9uIjog
  eyJjcmVkZW50aWFsX2hhc2hfYWxnIjogInNoYS0yNTYifX0sICJ2Y3QiOiAiRGlzYWJp
  bGl0eUNhcmQiLCAiX3NkX2FsZyI6ICJzaGEtMjU2IiwgImNuZiI6IHsiandrIjogeyJr
  dHkiOiAiRUMiLCAiY3J2IjogIlAtMjU2IiwgIngiOiAiVENBRVIxOVp2dTNPSEY0ajRX
  NHZmU1ZvSElQMUlMaWxEbHM3dkNlR2VtYyIsICJ5IjogIlp4amlXV2JaTVFHSFZXS1ZR
  NGhiU0lpcnNWZnVlY0NFNnQ0alQ5RjJIWlEifX19.1kOe6IgFxgbb_jtaLUhM_bgjmby
  j6B63rm_WjaOwpOBsiPSKJY7hBHd2a83euSI8JqbSkVHJS3wcr0kd9ppZRw~WyI1N212
  eWNUaDV5WkNyS0xaNXhuZlV3IiwgImlhdCIsIDE2ODMwMDAwMDBd~WyJrdWNyQm1sb19
  oTWFJRkY1ODVSemFRIiwgImRvY3VtZW50X251bWJlciIsICJYWFhYWFhYWFhYIl0~WyJ
  OVE5Sb09pdVZWUnRGNkNFenRkOVp3IiwgImdpdmVuX25hbWUiLCAiTWFyaW8iXQ~WyJG
  RFNTUGdnekdCVXdRTEhEU0U2d1FRIiwgImZhbWlseV9uYW1lIiwgIlJvc3NpIl0~WyJL
  WjhlNXdWRXREdmIxemlTUEE0RHpBIiwgImJpcnRoX2RhdGUiLCAiMTk4MC0wMS0xMCJd
  ~WyJwWjVNUnlPeHBWV1p1SExvSi15alJnIiwgImV4cGlyeV9kYXRlIiwgIjIwMjQtMDE
  tMDEiXQ~WyJqdFZ1S0NwbjdiVGNIckFnX3NlVWJRIiwgInRheF9pZF9jb2RlIiwgIlRJ
  TklULVhYWFhYWFhYWFhYWFhYWFgiXQ~WyJXRGtkNkpzTmhERnZMUDRzMWhRZHlBIiwgI
  mNvbnN0YW50X2F0dGVuZGFuY2VfYWxsb3dhbmNlIiwgdHJ1ZV0~

MDOC-CBOR
=========

The PID/(Q)EAA MDOC-CBOR data model is defined in ISO/IEC 18013-5, the standard born for the the mobile driving license (mDL) use case. 

The MDOC data elements MUST be encoded as defined in `RFC 8949 - Concise Binary Object Representation (CBOR) <RFC 8949 - Concise Binary Object Representation (CBOR)>`_.

The PID encoded in MDOC-CBOR format uses the document type set to `eu.europa.ec.eudiw.pid.1`, according to the reverse domain approach defined in the 
`EIDAS-ARF`_ and ISO/IEC 18013-5.

The document's data elements utilize a consistent namespace for the mandatory Mobile Driving License attributes, while the national PID attributes use the domestic namespace `eu.europa.ec.eudiw.pid.it.1`, as outlined in this implementation profile.

In compliance with ISO/IEC 18013-5, the MDOC data model in the domestic namespace `eu.europa.ec.eudiw.pid.it.1`, requires the following attributes:

.. _table-mdoc-attributes:

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Attribute name**
      - **Description**
      - **Reference**
    * - **version**
      - *tstr (text string)*. Version of the data structure being used. It's a way to track changes and updates to the standard or to a specific implementation profile. This allows for backward compatibility and understanding of the data if the standard or implementation evolves over time.
      - [ISO 18013-5#8.3.2.1.2]
    * - **status**
      - *uint (unsigned int)*. Status code. For example ``"status":0`` means OK (normal processing).
      - [ISO 18013-5#8.3.2.1.2.3]
    * - **documents**
      - *bstr (byte string)*. The collection of digital documents. Each document in this collection represents a specific type of data or information related to the Digital Credential.
      - [ISO 18013-5#8.3.2.1.2]

Each document within the **documents** collection MUST have the following structure:

.. _table-mdoc-documents-attributes:

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Attribute name**
      - **Description**
      - **Reference**
    * - **docType**
      - *tstr (text string)*. Document type. For the PID, the value MUST be set to ``eu.europa.ec.eudiw.pid.1.`` For an mDL, the value MUST be ``org.iso.18013-5.1.mDL``.
      - [ISO 18013-5#8.3.2.1.2]
    * - **issuerSigned**
      - *bstr (byte string)*. It MUST contain the Mobile Security Object for Issuer data authentication and the data elements protected by Issuer data authentication.
      - [ISO 18013-5#8.3.2.1.2]

The **issuerSigned** object MUST have the following structure:

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Attribute name**
      - **Description**
      - **Reference**
    * - **nameSpaces** 
      - *bstr (byte string)* with *tag* 24 and *major type* 6. Returned data elements for the namespaces. It MAY be possible to have one or more namespaces. The `nameSpaces` MUST use the same value for the document type. However, it MAY have a domestic namespace to include attributes defined in this implementation profile. The value MUST be set to ``eu.europa.ec.eudiw.pid.it.1``.
      - [ISO 18013-5#8.3.2.1.2]
    * - **issuerAuth**
      - *bstr (byte string)*. Contains *Mobile Security Object* (MSO), a COSE Sign1 Document, issued by the Credential Issuer.
      - [ISO 18013-5#9.1.2.4]

During the presentation of the MDOC-CBOR credential, in addition to the objects in the table above, a **deviceSigned** object MUST also be added. **deviceSigned** MUST NOT be included in the issued credential provided by the PID/(Q)EAA Issuer.

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Attribute name**
      - **Description**
      - **Reference**
    * - **deviceSigned**
      - *bstr (byte string)*. Data elements signed by the Wallet Instance during the presentation phase.
      - [ISO 18013-5#8.3.2.1.2]

Where the **deviceSigned** MUST have the following structure:

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Attribute name**
      - **Description**
      - **Reference**
    * - **nameSpaces**
      - *tstr (text string)*. Returned data elements for the namespaces. It MAY be possible to have one or more namespaces. It MAY be used for self-attested claims.
      - [ISO 18013-5#8.3.2.1.2]
    * - **deviceAuth**
      - *bstr (byte string)*. It MUST contain either the *DeviceSignature* or the *DeviceMac* element.
      - [ISO 18013-5#8.3.2.1.2]


.. note::
  
  A **deviceSigned** object given during the presentation phase has two purposes:

    1. It provides optional self-attested attributes in the ``nameSpaces`` object. If no self-attested attributes are provided by the Wallet Instance, the ``nameSpaces`` object MUST be included with an empty structure.
    2. Provide a cryptographic proof attesting that the Holder is the legitimate owner of the Credential, by means of a ``deviceAuth`` object. 


.. note::

    The ``issuerSigned`` and the ``deviceSigned`` objects contain the ``nameSpaces`` object and the *Mobile Security Object*. The latter is the only signed object, while the ``nameSpaces`` object is not signed.



nameSpaces
----------

The **nameSpaces** object contains one or more *IssuerSignedItemBytes* that are encoded using CBOR bitsring 24 tag (#6.24(bstr .cbor), marked with the CBOR Tag 24(<<... >>) and represented in the example using the diagnostic format). It represents the disclosure information for each digest within the `Mobile Security Object` and MUST contain the following attributes:

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Name**
      - **Encoding**
      - **Description**
    * - **digestID**
      - *integer*
      - Reference value to one of the ``ValueDigests`` provided in the *Mobile Security Object* (`issuerAuth`).
    * - **random**
      - *bstr (byte string)*
      - Random byte value used as salt for the hash function. This value SHALL be different for each *IssuerSignedItem* and it SHALL have a minimum length of 16 bytes.
    * - **elementIdentifier**
      - *tstr (text string)*
      - Data element identifier.
    * - **elementValue**
      - depends by the value, see the next table.
      - Data element value.

The **elementIdentifier** data that MUST be included in a PID/(Q)EAA are: 

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Namespace**
      - **Element identifier**
      - **Description**
    * - **eu.europa.ec.eudiw.pid.1**
      - **issue_date**
      - *full-date (CBORTag 1004)*. Date when the PID/(Q)EAA was issued.
    * - **eu.europa.ec.eudiw.pid.1**
      - **expiry_date**
      - *full-date (CBORTag 1004)*. Date when the PID/(Q)EAA will expire.
    * - **eu.europa.ec.eudiw.pid.1**
      - **issuing_authority**
      - *tstr (text string)*. Name of administrative authority that has issued the PID/(Q)EAA.
    * - **eu.europa.ec.eudiw.pid.1**
      - **issuing_country**
      - *tstr (text string)*. Alpha-2 country code as defined in [ISO 3166].


Depending on the Digital Credential type, additional **elementIdentifier** data MAY be added. The PID MUST support the following data:

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Namespace**
      - **Element identifier**
      - **Description**
    * - **eu.europa.ec.eudiw.pid.1**
      - **given_name**
      - *tstr (text string)*. See :ref:`PID Claims fields Section <sec-pid-user-claims>`.
    * - **eu.europa.ec.eudiw.pid.1**      
      - **family_name**
      - *tstr (text string)*. See :ref:`PID Claims fields Section <sec-pid-user-claims>`.
    * - **eu.europa.ec.eudiw.pid.1**
      - **birth_date**
      - *full-date (CBORTag 1004)*. See :ref:`PID Claims fields Section <sec-pid-user-claims>`.
    * - **eu.europa.ec.eudiw.pid.1**
      - **unique_id**
      - *tstr (text string)*. See :ref:`PID Claims fields Section <sec-pid-user-claims>`.
    * - **eu.europa.ec.eudiw.pid.it.1**
      - **tax_id_code**
      - *tstr (text string)*. See :ref:`PID Claims fields Section <sec-pid-user-claims>`.


Mobile Security Object
----------------------

The **issuerAuth** represents the `Mobile Security Object` which is a `COSE Sign1 Document` defined in `RFC 9052 - CBOR Object Signing and Encryption (COSE): Structures and Process <https://www.rfc-editor.org/rfc/rfc9052.html>`_. It has the following data structure:

* protected header
* unprotected header
* payload
* signature.

The **protected header** MUST contain the following parameter encoded in CBOR format:

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Element**
      - **Description**
      - **Reference**
    * - **Signature algorithm**
      - `-7` means ES256, SHA-256. 
      - RFC8152

.. note::
    
    Only the Signature Algorithm MUST be present in the protected headers, other elements SHOULD not be present in the protected header.


The **unprotected header** MUST contain the following parameter:

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Element**
      - **Description**
      - **Reference**
    * - **x5chain**
      - Identified with the label 33
      - `RFC 9360 CBOR Object Signing and Encryption (COSE) - Header Parameters for Carrying and Referencing X.509 Certificates <RFC 9360 CBOR Object Signing and Encryption (COSE) - Header Parameters for Carrying and Referencing X.509 Certificates>`_.

.. note::
    The `x5chain` is included in the unprotected header with the aim to make the Holder able to update the X.509 certificate chain, related to the `Mobile Security Object` issuer, without invalidating the signature.

The **payload** MUST contain the *MobileSecurityObject*, without the `content-type` COSE Sign header parameter and encoded as a *byte string* (bstr) using the *CBOR Tag* 24.

The `MobileSecurityObjectBytes` MUST have the following attributes:

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Element**
      - **Description**
      - **Reference**
    * - **docType**
      - See :ref:`Table <table-mdoc-documents-attributes>`.
      - [ISO 18013-5#9.1.2.4]
    * - **version**
      - See :ref:`Table <table-mdoc-attributes>`.
      - [ISO 18013-5#9.1.2.4]
    * - **validityInfo**
      - Object containing issuance and expiration datetimes. It MUST contain the following sub-value:

          * *signed*
          * *validFrom*
          * *validUntil*
      - [ISO 18013-5#9.1.2.4]
    * - **digestAlgorithm**
      - According to the algorithm defined in the protected header.
      - [ISO 18013-5#9.1.2.4]
    * - **valueDigests**
      - Mapped digest by unique id, grouped by namespace.
      - [ISO 18013-5#9.1.2.4]
    * - **deviceKeyInfo**
      - It MUST contain the Wallet Instance's public key containing the following sub-values.

          * *deviceKey* (REQUIRED).
          * *keyAuthorizations* (OPTIONAL).
          * *keyInfo* (OPTIONAL).
      - [ISO 18013-5#9.1.2.4]

.. note::
    The private key related to the public key stored in the `deviceKey` object is used to sign the `DeviceSignedItems` object and proof the possession of the PID during the presentation phase (see the presentation phase with MDOC-CBOR).


MDOC-CBOR Examples
------------------

A non-normative example of a PID in MDOC-CBOR format is represented below using the AF Binary encoding:

.. code-block:: text
    
  a366737461747573006776657273696f6e63312e3069646f63756d656e747381a267646f6354797065781865752e6575726f70612e65632e65756469772e7069642e316c6973737565725369676e6564a26a697373756572417574688443a10126a1182159021930820215308201bca003020102021404ad06a30c1a6dc6e93be0e2e8f78dcafa7907c2300a06082a8648ce3d040302305b310b3009060355040613025a45312e302c060355040a0c25465053204d6f62696c69747920616e64205472616e73706f7274206f66205a65746f706961311c301a06035504030c1349414341205a65746573436f6e666964656e73301e170d3231303932393033333034355a170d3232313130333033333034345a3050311a301806035504030c114453205a65746573436f6e666964656e7331253023060355040a0c1c5a65746f70696120436974792044657074206f662054726166666963310b3009060355040613025a453059301306072a8648ce3d020106082a8648ce3d030107034200047c5545e9a0b15f4ff3ce5015121e8ad3257c28d541c1cd0d604fc9d1e352ccc38adef5f7902d44b7a6fc1f99f06eedf7b0018fd9da716aec2f1ffac173356c7da3693067301f0603551d23041830168014bba2a53201700d3c97542ef42889556d15b7ac4630150603551d250101ff040b3009060728818c5d050102301d0603551d0e04160414ce5fd758a8e88563e625cf056bfe9f692f4296fd300e0603551d0f0101ff040403020780300a06082a8648ce3d0403020347003044022012b06a3813ffec5679f3b8cddb51eaa4b95b0cbb1786b09405e2000e9c46618c02202c1f778ad252285ed05d9b55469f1cb78d773671f30fe7ab815371942328317c59032ad818590325a667646f6354797065781865752e6575726f70612e65632e65756469772e7069642e316776657273696f6e63312e306c76616c6964697479496e666fa3667369676e6564c074323032332d30322d32325430363a32333a35365a6976616c696446726f6dc074323032332d30322d32325430363a32333a35365a6a76616c6964556e74696cc074323032342d30322d32325430303a30303a30305a6c76616c756544696765737473a2781865752e6575726f70612e65632e65756469772e7069642e31ac015820a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a025820cd372fb85148700fa88095e3492d3f9f5beb43e555e5ff26d95f5a6adc36f8e6035820e67e72111b363d80c8124d28193926000980e1211c7986cacbd26aacc5528d48045820f7d062d662826ed95869851db06bb539b402047baee53a00e0aa35bfbe98265d0658202a132dbfe4784627b86aa3807cd19cfeff487aab3dd7a60d0ab119a72e736936075820bdca9e8dbca354e824e67bfe1533fa4a238b9ea832f23fb4271ebeb3a5a8f7200858202c0eaec2f05b6c7fe7982683e3773b5d8d7a01e33d04dfcb162add8bd99bee9a095820bfe220d85657ccec3c67e7db1df747e9148a152334bb6d4b65b273279bcc36ec0a582018e38144f5044301d6a0b4ec9d5f98d4cd950e6ea2c29b849cbd457da29b6ad30b58203c71d2f0efa09d9e3fbbdffd29204f6b292c9f79570aef72dd86c91f7a3aa5c50c582065743d58d89d45e52044758f546034fd13a4f994bc270cdfa7844f74eb3f4b6e0d5820b4a8eb5d523bffa17b41bda12ddc7da32ae1e5f7ff3dcc394a35401f16919bbf781b65752e6575726f70612e65632e65756469772e7069642e69742e31a10e58209d6c11644651126c94acdaf0803e86d4c71d15d3b2712a14295416734efd514d6d6465766963654b6579496e666fa1696465766963654b6579a401022001215820ba01aea44eee1e338eb2f04e279dbd51b34655783ee185150838c9a7a7c4db7122582025ba0044439a3871a7b975a0994a85e79b705a9ac263b3fe899b0a93412ee8c96f646967657374416c676f726974686d675348412d32353658400813c28fd62f2602cbc14724e5865733c44a0fca589b55c085ec9d5c725d6cce25ba0044439a3871a7b975a0994a85e79b705a9ac263b3fe899b0a93412ee8c96a6e616d65537061636573a2781865752e6575726f70612e65632e65756469772e7069642e3188d818586da4686469676573744944016672616e646f6d5820156df9227ad341eaa61aabd301106fd21bdc18820e01dfc16bcf5fecc447111b71656c656d656e744964656e7469666965726b6578706972795f646174656c656c656d656e7456616c7565d903ec6a323032342d30322d3232d818586fa4686469676573744944026672616e646f6d5820a3a1f13f05544d03a5b50b5fdb78465808393bcf3b7953a345fe28f820c7be0d71656c656d656e744964656e7469666965726d69737375616e63655f646174656c656c656d656e7456616c7565d903ec6a323032332d30322d3232d8185866a4686469676573744944036672616e646f6d5820852591f90f2c9ded57a03632e2c1322ab52a082a431e71a4149a6830c8f1ad0c71656c656d656e744964656e7469666965726f69737375696e675f636f756e7472796c656c656d656e7456616c7565624954d818587ca4686469676573744944046672616e646f6d5820d1d587b3512acce15c4f6b20944ceb002a464e4a158389788563408873c3fce571656c656d656e744964656e7469666965727169737375696e675f617574686f726974796c656c656d656e7456616c7565764d696e69737465726f2064656c6c27496e7465726e6fd8185864a4686469676573744944056672616e646f6d582094fdd7609c0e73dc8589b5cab11e1d9058cf8bff8a336da5f81fcba055396a0f71656c656d656e744964656e7469666965726a676976656e5f6e616d656c656c656d656e7456616c7565654d6172696fd8185865a4686469676573744944066672616e646f6d5820660c0a7bf79e0e0261ca1547a4294fb808aa70738f424b13ab1b9440b566ae1371656c656d656e744964656e7469666965726b66616d696c795f6e616d656c656c656d656e7456616c756565526f737369d818586ba4686469676573744944076672616e646f6d5820315c53491286488fa07f5c2ce67135ef5c9959c3469c99a14e9b6dc924f9eba571656c656d656e744964656e746966696572696269727468646174656c656c656d656e7456616c7565d903ec6a313935362d30312d3132d818587da4686469676573744944086672616e646f6d5820764ef39c9d01f3aa6a87f441603cfe853fba3cee3bc2c168bcc9e96271d6e06371656c656d656e744964656e74696669657269756e697175655f69646c656c656d656e7456616c7565781e78787878787878782d7878782d787878782d787878787878787878787878781b65752e6575726f70612e65632e65756469772e7069642e69742e3181d8185877a46864696765737449440d6672616e646f6d5820717df3f583b1484366c33a1f869f2b5d201d466a8b589c79ab1a2d85e595432571656c656d656e744964656e7469666965726d7461785f69645f6e756d6265726c656c656d656e7456616c75657554494e49542d585858585858585858585858585858

The `Diagnostic Notation` of the above MDOC-CBOR is given below:

.. literalinclude:: ../../examples/pid-mdoc-cbor-example.txt
  :language: text


