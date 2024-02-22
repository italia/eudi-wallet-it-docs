
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

The Italian digital Credentials, like the PID and the (Q)EAA, contains additional claims and according to the `OpenID Identity Assurance Profile [OIDC.IDA] <https://openid.net/specs/openid-connect-4-identity-assurance-1_0-13.html>`_, these carries the national trust framework and the identity proofing procedures underlying the issuance. In particular, these carries some relevant information about the Authentic Sources of the subject's attributes. 

The (Q)EAAs are issued by (Q)EAA Issuers to a Wallet Instance and MUST be provided in SD-JWT-VC or MDOC-CBOR data format. 

The PID/(Q)EAA data format and the mechanism through which a digital credential is issued to the Wallet Instance and presented to a Relying Party are described in the following sections. 

SD-JWT
======

The PID/(Q)EAA is issued in the form of a digital credential. The digital credential format is `Selective Disclosure JWT format <https://datatracker.ietf.org/doc/html/draft-ietf-oauth-selective-disclosure-jwt-04>`_ as specified in `[draft-terbu-sd-jwt-vc-latest] <https://vcstuff.github.io/draft-terbu-sd-jwt-vc/draft-terbu-oauth-sd-jwt-vc.html>`__.

An SD-JWT is a JWT that MUST be signed using the Issuer's private key. The SD-JWT payload of the MUST contain the **_sd_alg** claim described in `[SD-JWT]. Section 5.1.2. <https://datatracker.ietf.org/doc/html/draft-ietf-oauth-selective-disclosure-jwt-04>`_ and other claims specified in this section, some of them may be selectively disclosable claims. 

The claim **_sd_alg** indicates the hash algorithm used by the Issuer to generate the digests over the salts and the claim values. The **_sd_alg** claim MUST be set to one of the specified algorithms in Section :ref:`Cryptographic Algorithms <supported_algs>`.

Selectively disclosable claims are omitted from the SD-JWT. Instead, the digests of the respective disclosures and decoy digests are contained as an array in a new JWT claim, **_sd**. 

Each digest value ensures the integrity of, and maps to, the respective Disclosure. Digest values are calculated using a hash function over the disclosures, each of which contains 

  - a random salt, 
  - the claim name (only when the claim is an object property), 
  - the claim value. 
  
The Disclosures are sent to the Holder together with the SD-JWT in the *Combined Format for Issuance* that MUST be an ordered series of base64url-encoded values, each separated from the next by a single tilde ('~') character as follows:

.. code-block::

  <Issuer-Signed-JWT>~<Disclosure 1>~<Disclosure 2>~...~<Disclosure N>

See `[draft-terbu-sd-jwt-vc-latest] <https://vcstuff.github.io/draft-terbu-sd-jwt-vc/draft-terbu-oauth-sd-jwt-vc.html>`_ and `[SD-JWT] <https://datatracker.ietf.org/doc/html/draft-ietf-oauth-selective-disclosure-jwt-04>`__ for more details. 


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
    - MUST be set to ``vc+sd-jwt`` as defined in `[draft-terbu-sd-jwt-vc-latest] <https://www.ietf.org/archive/id/draft-terbu-sd-jwt-vc-02.html>`__. 
    - `[RFC7515, Section 4.1.9] <https://datatracker.ietf.org/doc/html/rfc7515#section-4.1.9>`_.
  * - **alg**
    - Signature Algorithm. 
    - `[RFC7515, Section 4.1.1] <https://datatracker.ietf.org/doc/html/rfc7515#section-4.1.1>`_.
  * - **kid**
    - Unique identifier of the public key. 
    - `[RFC7515, Section 4.1.8] <https://datatracker.ietf.org/doc/html/rfc7516.html#section-4.1.8>`_.
  * - **trust_chain**
    - JSON array containing the trust chain that proves the reliability of the issuer of the JWT. 
    - `[OIDC-FED, Section 3.2.1] <https://openid.net/specs/openid-connect-federation-1_0.html#name-trust-chain-header-paramete>`_.

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
      - [NSD].Thumbprint of the JWK in the ``cnf`` parameter.
      - `[RFC7519, Section 4.1.2] <https://www.iana.org/go/rfc7519>`_.
    * - **jti**
      - [NSD].Unique Token ID identifier of this JWT. It SHOULD be a String in *uuid4* format.
      - `[RFC7519, Section 4.1.7] <https://www.iana.org/go/rfc7519>`_.
    * - **iat**
      - [SD].UNIX Timestamp with the time of JWT issuance, coded as NumericDate as indicated in :rfc:`7519`.
      - `[RFC7519, Section 4.1.6] <https://www.iana.org/go/rfc7519>`_.
    * - **exp**
      - [NSD].UNIX Timestamp with the expiry time of the JWT, coded as NumericDate as indicated in :rfc:`7519`.
      - `[RFC7519, Section 4.1.4] <https://www.iana.org/go/rfc7519>`_.
    * - **status**
      - [NSD].HTTPS URL where the credential validity status is available. 
      - `[SD-JWT-VC. Section 4.2.2.2] <https://vcstuff.github.io/draft-terbu-sd-jwt-vc/draft-terbu-sd-jwt-vc.html#section-4.2.2.2>`_.
    * - **cnf**
      - [NSD].JSON object containing the proof-of-possession key materials. By including a **cnf** (confirmation) claim in a JWT, the issuer of the JWT declares that the Holder is in control of the private key related to the public one defined in the **cnf** parameter. The recipient MUST cryptographically verify that the Holder is in control of that key.
      - `[RFC7800, Section 3.1] <https://www.iana.org/go/rfc7800>`_.
    * - **vct**
      - [NSD].Credential type as a string, MUST be set in accordance to the type obtained from the PID/(Q)EAA Issuer metadata. For example, in the case of the PID, it MUST be set to ``PersonIdentificationData``.
      - `[draft-terbu-sd-jwt-vc-latest. Section Type Claim] <https://drafts.oauth.net/oauth-sd-jwt-vc/draft-ietf-oauth-sd-jwt-vc.html#type-claim>`__.
    * - **verified_claims**
      - [NSD].JSON object containing the following sub-elements: 

            -   **verification**; 
            -   **claims**.
      - `[OIDC.IDA. Section 5] <https://openid.net/specs/openid-connect-4-identity-assurance-1_0-13.html#section-5>`_.

.. _sec-pid-eaa-verification-field:

PID/(Q)EAA Verification field 
-----------------------------

The ``verification`` claim contains the information regarding the trust framework used by the PID/(Q)EAA Issuer to provide the User attributes (claims).  

The ``verification`` claim is a JSON structure with all the following mandatory sub-claims.

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **trust_framework**
      - [NSD]. It MUST be set to ``eidas``.
      - `[OID.IDA. Section 5.1] <https://openid.net/specs/openid-connect-4-identity-assurance-1_0-13.html#section-5.1>`_
    * - **assurance_level**
      - [NSD]. MUST be set according to the LoA required. For PID credential it MUST be set to ``high``.
      - `[OID.IDA. Section 5.1] <https://openid.net/specs/openid-connect-4-identity-assurance-1_0-13.html#section-5.1>`_
    * - **evidence**
      - [SD]. JSON Array. Each element is the electronic evidence of the User identification during the PID issuance or, in the case of (Q)EAA, with this evidence the Authentic Source assures the authenticity of the data conveyed in the (Q)EAA. It MUST contain at least the following claims:

            - **type**: MUST be set to ``electronic_record``
            - **record**: JSON object (see the table below)
      - `[OID.IDA. Section 5.1] <https://openid.net/specs/openid-connect-4-identity-assurance-1_0-13.html#section-5.1>`_


The ``record`` MUST have at least the following sub parameters:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **type** 
    - It uniquely identifies the trust framework used for the provisioning of the credential. For example, in case of PID, the value ``https://eudi.wallet.cie.gov.it`` means that the CIE id identification scheme is used. 
    - `[OID.IDA. Section 5.1.1.2] <https://openid.net/specs/openid-connect-4-identity-assurance-1_0-13.html#section-5.1.1.2>`_
  * - **source**
    - JSON Object cointaining the following mandatory claims:

      - **organization_name**: Name of the Organization acting as Authentic Source.
      - **organization_id**: Identification code for the Organization. For public Organization, it MUST be set to the *IPA Code*, following the URN namespace ``urn:eudi:it:organization_id:ipa_code:<that-value>``.
      - **country_code**: String representing country in `[ISO3166-1] Alpha-2 (e.g., IT) or [ISO3166-3] syntax <https://www.iso.org/iso-3166-country-codes.html>`_.
    - `[OID.IDA. Section 5.1.1.2] <https://openid.net/specs/openid-connect-4-identity-assurance-1_0-13.html#section-5.1.1.2>`_

.. warning::
  Note that the sub-claims of the **evidence** parameter are not selectively disclosable separately, thus, for example, the User cannot give only the *record type* without the disclosure of the *record source* value (organization name, identifier and country). 

.. _sec-pid-user-claims:

PID Claims field 
----------------

The ``claims`` parameter contains the User attributes with the following mandatory fields:

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



PID Non-normative Examples
--------------------------

In the following, the non-normative example of a PID in JSON format.

.. code-block:: JSON

  {
    "iss": "https://issuer.example.org",
    "sub": "NzbLsXh8uDCcd7noWXFZAfHkxZsRGC9Xs",
    "jti": "urn:uuid:6c5c0a49-b589-431d-bae7-219122a9ec2c",
    "iat": 1683000000,
    "exp": 1883000000,
    "status": "https://pidprovider.example.org/status",
    "vct": "PersonIdentificationData",
    "verified_claims": {
      "verification": {
        "trust_framework": "eidas",
        "assurance_level": "high",
        "evidence": [
          {
            "type": "electronic_record",
            "record": {
              "type": "https://eudi.wallet.cie.gov.it",
              "source": {
                "organization_name": "Ministero dell'Interno",
                "organization_id":
                  "urn:eudi:it:organization_id:ipa_code:m_it",
                "country_code": "IT"
              }
            }
          }
        ]
      },
      "claims": {
        "unique_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "given_name": "Mario",
        "family_name": "Rossi",
        "birth_date": "1980-01-10",
        "tax_id_code": "TINIT-XXXXXXXXXXXXXXXX"
      }
    }
  }

The corresponding SD-JWT verson for PID is given by

.. code-block:: JSON

  {
     "typ":"vc+sd-jwt",
     "alg":"RS512",
     "kid":"dB67gL7ck3TFiIAf7N6_7SHvqk0MDYMEQcoGGlkUAAw",
     "trust_chain" : [
      "NEhRdERpYnlHY3M5WldWTWZ2aUhm ...",
      "eyJhbGciOiJSUzI1NiIsImtpZCI6 ...",
      "IkJYdmZybG5oQU11SFIwN2FqVW1B ..."
     ]
  }

.. code-block:: JSON

  {
    "_sd": [
      "7WG4nT6K26_R3975zcwnVwgoHA7b988_3-vJzbZf6Yc"
    ],
    "iss": "https://issuer.example.org",
    "exp": 1883000000,
    "sub": "NzbLsXh8uDCcd7noWXFZAfHkxZsRGC9Xs",
    "jti": "urn:uuid:6c5c0a49-b589-431d-bae7-219122a9ec2c",
    "status": "https://pidprovider.example.org/status",
    "vct": "PersonIdentificationData",
    "verified_claims": {
      "verification": {
        "_sd": [
          "gd8gRxKT1hg8ptnvR5fPGhae0VXllDblsiJT9adxiS8"
        ],
        "trust_framework": "eidas",
        "assurance_level": "high"
      },
      "claims": {
        "_sd": [
          "4g9lBt38U1EeTA1zlvvGfFgPPcoe3zmbQ_zSRDgHQaE",
          "EYgzJ1hTYWJjhBK2V3b8HV3e_fEf-Udffc5ymY77WtQ",
          "IcYHQydT_C3U1IqaJlFicxLlaHTHvElyFZ6Jxia27qQ",
          "KxIG8rWXmtR884xTV7eXuHICfPYPw6gFvfr07v-d5oc",
          "lXgxEDAuPeUvmkcNGr9FZuqodwFqUT01gJj7xd4yEPA"
        ]
      }
    },
    "_sd_alg": "sha-256",
    "cnf": {
      "jwk": {
        "kty": "EC",
        "crv": "P-256",
        "x": "TCAER19Zvu3OHF4j4W4vfSVoHIP1ILilDls7vCeGemc",
        "y": "ZxjiWWbZMQGHVWKVQ4hbSIirsVfuecCE6t4jT9F2HZQ"
      }
    }
  }

In the following the disclosure list is given

**Claim** ``iat``:

-  SHA-256 Hash: ``7WG4nT6K26_R3975zcwnVwgoHA7b988_3-vJzbZf6Yc``
-  Disclosure:
   ``WyI1N212eWNUaDV5WkNyS0xaNXhuZlV3IiwgImlhdCIsIDE2ODMwMDAwMDBd``
-  Contents: ``["57mvycTh5yZCrKLZ5xnfUw", "iat", 1683000000]``

**Claim** ``source``:

-  SHA-256 Hash: ``ZMHbFH9SeT9CZQaOMVrXDMGWIouzXRKspKp9fDhvJ3I``
-  Disclosure:
   ``WyJrdWNyQm1sb19oTWFJRkY1ODVSemFRIiwgInNvdXJjZSIsIHsib3JnYW5p``
   ``emF0aW9uX25hbWUiOiAiTWluaXN0ZXJvIGRlbGwnSW50ZXJubyIsICJvcmdh``
   ``bml6YXRpb25faWQiOiAidXJuOmV1ZGk6aXQ6b3JnYW5pemF0aW9uX2lkOmlw``
   ``YV9jb2RlOm1faXQiLCAiY291bnRyeV9jb2RlIjogIklUIn1d``
-  Contents:
   ``["kucrBmlo_hMaIFF585RzaQ", "source", {"organization_name":``
   ``"Ministero dell'Interno", "organization_id":``
   ``"urn:eudi:it:organization_id:ipa_code:m_it", "country_code":``
   ``"IT"}]``

**Claim** ``evidence``:

-  SHA-256 Hash: ``gd8gRxKT1hg8ptnvR5fPGhae0VXllDblsiJT9adxiS8``
-  Disclosure:
   ``WyJOVE5Sb09pdVZWUnRGNkNFenRkOVp3IiwgImV2aWRlbmNlIiwgW3sidHlw``
   ``ZSI6ICJlbGVjdHJvbmljX3JlY29yZCIsICJyZWNvcmQiOiB7Il9zZCI6IFsi``
   ``Wk1IYkZIOVNlVDlDWlFhT01WclhETUdXSW91elhSS3NwS3A5ZkRodkozSSJd``
   ``LCAidHlwZSI6ICJodHRwczovL2V1ZGkud2FsbGV0LmNpZS5nb3YuaXQifX1d``
   ``XQ``
-  Contents: ``["NTNRoOiuVVRtF6CEztd9Zw", "evidence", [{"type":``
   ``"electronic_record", "record": {"_sd":``
   ``["ZMHbFH9SeT9CZQaOMVrXDMGWIouzXRKspKp9fDhvJ3I"], "type":``
   ``"https://eudi.wallet.cie.gov.it"}}]]``

**Claim** ``unique_id``:

-  SHA-256 Hash: ``4g9lBt38U1EeTA1zlvvGfFgPPcoe3zmbQ_zSRDgHQaE``
-  Disclosure:
   ``WyJGRFNTUGdnekdCVXdRTEhEU0U2d1FRIiwgInVuaXF1ZV9pZCIsICJ4eHh4``
   ``eHh4eC14eHh4LXh4eHgteHh4eC14eHh4eHh4eHh4eHgiXQ``
-  Contents: ``["FDSSPggzGBUwQLHDSE6wQQ", "unique_id",``
   ``"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]``

**Claim** ``given_name``:

-  SHA-256 Hash: ``lXgxEDAuPeUvmkcNGr9FZuqodwFqUT01gJj7xd4yEPA``
-  Disclosure:
   ``WyJLWjhlNXdWRXREdmIxemlTUEE0RHpBIiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
-  Contents: ``["KZ8e5wVEtDvb1ziSPA4DzA", "given_name", "Mario"]``

**Claim** ``family_name``:

-  SHA-256 Hash: ``IcYHQydT_C3U1IqaJlFicxLlaHTHvElyFZ6Jxia27qQ``
-  Disclosure:
   ``WyJwWjVNUnlPeHBWV1p1SExvSi15alJnIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
-  Contents: ``["pZ5MRyOxpVWZuHLoJ-yjRg", "family_name", "Rossi"]``

**Claim** ``birth_date``:

-  SHA-256 Hash: ``EYgzJ1hTYWJjhBK2V3b8HV3e_fEf-Udffc5ymY77WtQ``
-  Disclosure:
   ``WyJqdFZ1S0NwbjdiVGNIckFnX3NlVWJRIiwgImJpcnRoX2RhdGUiLCAiMTk4``
   ``MC0wMS0xMCJd``
-  Contents: ``["jtVuKCpn7bTcHrAg_seUbQ", "birth_date", "1980-01-10"]``

**Claim** ``tax_id_code``:

-  SHA-256 Hash: ``KxIG8rWXmtR884xTV7eXuHICfPYPw6gFvfr07v-d5oc``
-  Disclosure:
   ``WyI0a3NBejZiTVVLeTZadk4xaDhIRHVRIiwgInRheF9pZF9jb2RlIiwgIlRJ``
   ``TklULVhYWFhYWFhYWFhYWFhYWFgiXQ``
-  Contents: ``["4ksAz6bMUKy6ZvN1h8HDuQ", "tax_id_code",``
   ``"TINIT-XXXXXXXXXXXXXXXX"]``



The combined format for the PID issuance is given by

.. code-block::

  eyJhbGciOiAiRVMyNTYiLCAidHlwIjogImV4YW1wbGUrc2Qtand0In0.eyJfc2QiOiBb
  IjdXRzRuVDZLMjZfUjM5NzV6Y3duVndnb0hBN2I5ODhfMy12SnpiWmY2WWMiXSwgImlz
  cyI6ICJodHRwczovL3BpZHByb3ZpZGVyLmV4YW1wbGUub3JnIiwgImV4cCI6IDE4ODMw
  MDAwMDAsICJzdWIiOiAiTnpiTHNYaDh1RENjZDdub1dYRlpBZkhreFpzUkdDOVhzIiwg
  Imp0aSI6ICJ1cm46dXVpZDo2YzVjMGE0OS1iNTg5LTQzMWQtYmFlNy0yMTkxMjJhOWVj
  MmMiLCAic3RhdHVzIjogImh0dHBzOi8vcGlkcHJvdmlkZXIuZXhhbXBsZS5vcmcvc3Rh
  dHVzIiwgInZjdCI6ICJQaWRJZGVudGlmaWNhdGlvbkRhdGEiLCAidmVyaWZpZWRfY2xh
  aW1zIjogeyJ2ZXJpZmljYXRpb24iOiB7Il9zZCI6IFsiZ2Q4Z1J4S1QxaGc4cHRudlI1
  ZlBHaGFlMFZYbGxEYmxzaUpUOWFkeGlTOCJdLCAidHJ1c3RfZnJhbWV3b3JrIjogImVp
  ZGFzIiwgImFzc3VyYW5jZV9sZXZlbCI6ICJoaWdoIn0sICJjbGFpbXMiOiB7Il9zZCI6
  IFsiNGc5bEJ0MzhVMUVlVEExemx2dkdmRmdQUGNvZTN6bWJRX3pTUkRnSFFhRSIsICJF
  WWd6SjFoVFlXSmpoQksyVjNiOEhWM2VfZkVmLVVkZmZjNXltWTc3V3RRIiwgIkljWUhR
  eWRUX0MzVTFJcWFKbEZpY3hMbGFIVEh2RWx5Rlo2SnhpYTI3cVEiLCAiS3hJRzhyV1ht
  dFI4ODR4VFY3ZVh1SElDZlBZUHc2Z0Z2ZnIwN3YtZDVvYyIsICJsWGd4RURBdVBlVXZt
  a2NOR3I5Rlp1cW9kd0ZxVVQwMWdKajd4ZDR5RVBBIl19fSwgIl9zZF9hbGciOiAic2hh
  LTI1NiIsICJjbmYiOiB7Imp3ayI6IHsia3R5IjogIkVDIiwgImNydiI6ICJQLTI1NiIs
  ICJ4IjogIlRDQUVSMTladnUzT0hGNGo0VzR2ZlNWb0hJUDFJTGlsRGxzN3ZDZUdlbWMi
  LCAieSI6ICJaeGppV1diWk1RR0hWV0tWUTRoYlNJaXJzVmZ1ZWNDRTZ0NGpUOUYySFpR
  In19fQ.1xdAqLpgMM0bBDQrYv0thRwtgRikZq75JJVhGyfWAsu8SopmhumzsTA4ohJKC
  le1MV3UB6DYMFkEnoal8R1Yrw~WyI1N212eWNUaDV5WkNyS0xaNXhuZlV3IiwgImlhdC
  IsIDE2ODMwMDAwMDBd~WyJrdWNyQm1sb19oTWFJRkY1ODVSemFRIiwgInNvdXJjZSIsI
  Hsib3JnYW5pemF0aW9uX25hbWUiOiAiTWluaXN0ZXJvIGRlbGwnSW50ZXJubyIsICJvc
  mdhbml6YXRpb25faWQiOiAidXJuOmV1ZGk6aXQ6b3JnYW5pemF0aW9uX2lkOmlwYV9jb
  2RlOm1faXQiLCAiY291bnRyeV9jb2RlIjogIklUIn1d~WyJOVE5Sb09pdVZWUnRGNkNF
  enRkOVp3IiwgImV2aWRlbmNlIiwgW3sidHlwZSI6ICJlbGVjdHJvbmljX3JlY29yZCIs
  ICJyZWNvcmQiOiB7Il9zZCI6IFsiWk1IYkZIOVNlVDlDWlFhT01WclhETUdXSW91elhS
  S3NwS3A5ZkRodkozSSJdLCAidHlwZSI6ICJodHRwczovL2V1ZGkud2FsbGV0LmNpZS5n
  b3YuaXQifX1dXQ~WyJGRFNTUGdnekdCVXdRTEhEU0U2d1FRIiwgInVuaXF1ZV9pZCIsI
  CJ4eHh4eHh4eC14eHh4LXh4eHgteHh4eC14eHh4eHh4eHh4eHgiXQ~WyJLWjhlNXdWRX
  REdmIxemlTUEE0RHpBIiwgImdpdmVuX25hbWUiLCAiTWFyaW8iXQ~WyJwWjVNUnlPeHB
  WV1p1SExvSi15alJnIiwgImZhbWlseV9uYW1lIiwgIlJvc3NpIl0~WyJqdFZ1S0Nwbjd
  iVGNIckFnX3NlVWJRIiwgImJpcnRoX2RhdGUiLCAiMTk4MC0wMS0xMCJd~WyJXRGtkNk
  pzTmhERnZMUDRzMWhRZHlBIiwgInRheF9pZF9jb2RlIiwgIlRJTklULVhYWFhYWFhYWF
  hYWFhYWFgiXQ~

(Q)EAA Non-normative examples
-----------------------------

In the following, we provide a non-normative example of (Q)EAA in JSON.

.. code-block:: JSON

  {
    "iss": "https://issuer.example.org",
    "sub": "NzbLsXh8uDCcd7noWXFZAfHkxZsRGC9Xs",
    "jti": "urn:uuid:6c5c0a49-b589-431d-bae7-219122a9ec2c",
    "iat": 1683000000,
    "exp": 1883000000,
    "status": "https://issuer.example.org/status",
    "vct": "DisabilityCard",
    "verified_claims": {
      "verification": {
        "trust_framework": "eidas",
        "assurance_level": "high",
        "evidence": [
          {
            "type": "electronic_record",
            "record": {
              "type": "https://eudi.wallet.pdnd.gov.it",
              "source": {
                "organization_name": "Istituto Nazionale della Previdenza Sociale",
                "organization_id":
                  "urn:eudi:it:organization_id:ipa_code:inps",
                "country_code": "IT"
              }
            }
          }
        ]
      },
      "claims": {
        "document_number": "XXXXXXXXXX",
        "given_name": "Mario",
        "family_name": "Rossi",
        "birth_date": "1980-01-10",
        "expiry_date": "2024-01-01",
        "tax_id_code": "TINIT-XXXXXXXXXXXXXXXX",
        "constant_attendance_allowance": true
      }
    }
  }

The corresponding SD-JWT for the previous data is represented as follow, as decoded JSON for both header and payload.

.. code-block:: JSON

  {
     "typ":"vc+sd-jwt",
     "alg":"RS512",
     "kid":"d126a6a856f7724560484fa9dc59d195",
     "trust_chain" : [
      "NEhRdERpYnlHY3M5WldWTWZ2aUhm ...",
      "eyJhbGciOiJSUzI1NiIsImtpZCI6 ...",
      "IkJYdmZybG5oQU11SFIwN2FqVW1B ..."
     ]
  }

.. code-block:: JSON

  {
    "_sd": [
      "7WG4nT6K26_R3975zcwnVwgoHA7b988_3-vJzbZf6Yc"
    ],
    "iss": "https://issuer.example.org",
    "exp": 1883000000,
    "sub": "NzbLsXh8uDCcd7noWXFZAfHkxZsRGC9Xs",
    "jti": "urn:uuid:6c5c0a49-b589-431d-bae7-219122a9ec2c",
    "status": "https://issuer.example.org/status",
    "vct": "DisabilityCard",
    "verified_claims": {
      "verification": {
        "_sd": [
          "sTskq0yFy31ZH3YP2nN_nFnd7H9q18dU3oEa1DC5LRc"
        ],
        "trust_framework": "eidas",
        "assurance_level": "high"
      },
      "claims": {
        "_sd": [
          "3humFjiCYHdHzjL-OEd1vKnQa10ivaYEd1dCCkfRuaA",
          "EYgzJ1hTYWJjhBK2V3b8HV3e_fEf-Udffc5ymY77WtQ",
          "F90SKK9nIQcHIElkHY_ult_9FGqYe-RydvY3E0qR96s",
          "IcYHQydT_C3U1IqaJlFicxLlaHTHvElyFZ6Jxia27qQ",
          "dfrmUvonZDgealZCGwk3ufmc_4ept3y9N7xhWZlCyxo",
          "ji86HS1v3D41tU5JqW4oWCwTJDuTUwp1ewqoCUzzEXk",
          "lXgxEDAuPeUvmkcNGr9FZuqodwFqUT01gJj7xd4yEPA"
        ]
      }
    },
    "_sd_alg": "sha-256",
    "cnf": {
      "jwk": {
        "kty": "EC",
        "crv": "P-256",
        "x": "TCAER19Zvu3OHF4j4W4vfSVoHIP1ILilDls7vCeGemc",
        "y": "ZxjiWWbZMQGHVWKVQ4hbSIirsVfuecCE6t4jT9F2HZQ"
      }
    }
  }

In the following the disclosure list is given:

**Claim** ``iat``:

-  SHA-256 Hash: ``7WG4nT6K26_R3975zcwnVwgoHA7b988_3-vJzbZf6Yc``
-  Disclosure:
   ``WyI1N212eWNUaDV5WkNyS0xaNXhuZlV3IiwgImlhdCIsIDE2ODMwMDAwMDBd``
-  Contents: ``["57mvycTh5yZCrKLZ5xnfUw", "iat", 1683000000]``

**Claim** ``source``:

-  SHA-256 Hash: ``qfuzrQuGcbBBKaE4Q9eqVCSznzJ2rNndLG8q606RLsM``
-  Disclosure:
   ``WyJrdWNyQm1sb19oTWFJRkY1ODVSemFRIiwgInNvdXJjZSIsIHsib3JnYW5p``
   ``emF0aW9uX25hbWUiOiAiSXN0aXR1dG8gTmF6aW9uYWxlIGRlbGxhIFByZXZp``
   ``ZGVuemEgU29jaWFsZSIsICJvcmdhbml6YXRpb25faWQiOiAidXJuOmV1ZGk6``
   ``aXQ6b3JnYW5pemF0aW9uX2lkOmlwYV9jb2RlOmlucHMiLCAiY291bnRyeV9j``
   ``b2RlIjogIklUIn1d``
-  Contents:
   ``["kucrBmlo_hMaIFF585RzaQ", "source", {"organization_name":``
   ``"Istituto Nazionale della Previdenza Sociale",``
   ``"organization_id":``
   ``"urn:eudi:it:organization_id:ipa_code:inps", "country_code":``
   ``"IT"}]``

**Claim** ``evidence``:

-  SHA-256 Hash: ``sTskq0yFy31ZH3YP2nN_nFnd7H9q18dU3oEa1DC5LRc``
-  Disclosure:
   ``WyJOVE5Sb09pdVZWUnRGNkNFenRkOVp3IiwgImV2aWRlbmNlIiwgW3sidHlw``
   ``ZSI6ICJlbGVjdHJvbmljX3JlY29yZCIsICJyZWNvcmQiOiB7Il9zZCI6IFsi``
   ``cWZ1enJRdUdjYkJCS2FFNFE5ZXFWQ1N6bnpKMnJObmRMRzhxNjA2UkxzTSJd``
   ``LCAidHlwZSI6ICJodHRwczovL2V1ZGkud2FsbGV0LnBkbmQuZ292Lml0In19``
   ``XV0``
-  Contents: ``["NTNRoOiuVVRtF6CEztd9Zw", "evidence", [{"type":``
   ``"electronic_record", "record": {"_sd":``
   ``["qfuzrQuGcbBBKaE4Q9eqVCSznzJ2rNndLG8q606RLsM"], "type":``
   ``"https://eudi.wallet.pdnd.gov.it"}}]]``

**Claim** ``document_number``:

-  SHA-256 Hash: ``3humFjiCYHdHzjL-OEd1vKnQa10ivaYEd1dCCkfRuaA``
-  Disclosure:
   ``WyJGRFNTUGdnekdCVXdRTEhEU0U2d1FRIiwgImRvY3VtZW50X251bWJlciIs``
   ``ICJYWFhYWFhYWFhYIl0``
-  Contents:
   ``["FDSSPggzGBUwQLHDSE6wQQ", "document_number", "XXXXXXXXXX"]``

**Claim** ``given_name``:

-  SHA-256 Hash: ``lXgxEDAuPeUvmkcNGr9FZuqodwFqUT01gJj7xd4yEPA``
-  Disclosure:
   ``WyJLWjhlNXdWRXREdmIxemlTUEE0RHpBIiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
-  Contents: ``["KZ8e5wVEtDvb1ziSPA4DzA", "given_name", "Mario"]``

**Claim** ``family_name``:

-  SHA-256 Hash: ``IcYHQydT_C3U1IqaJlFicxLlaHTHvElyFZ6Jxia27qQ``
-  Disclosure:
   ``WyJwWjVNUnlPeHBWV1p1SExvSi15alJnIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
-  Contents: ``["pZ5MRyOxpVWZuHLoJ-yjRg", "family_name", "Rossi"]``

**Claim** ``birth_date``:

-  SHA-256 Hash: ``EYgzJ1hTYWJjhBK2V3b8HV3e_fEf-Udffc5ymY77WtQ``
-  Disclosure:
   ``WyJqdFZ1S0NwbjdiVGNIckFnX3NlVWJRIiwgImJpcnRoX2RhdGUiLCAiMTk4``
   ``MC0wMS0xMCJd``
-  Contents: ``["jtVuKCpn7bTcHrAg_seUbQ", "birth_date", "1980-01-10"]``

**Claim** ``expiry_date``:

-  SHA-256 Hash: ``dfrmUvonZDgealZCGwk3ufmc_4ept3y9N7xhWZlCyxo``
-  Disclosure:
   ``WyJXRGtkNkpzTmhERnZMUDRzMWhRZHlBIiwgImV4cGlyeV9kYXRlIiwgIjIw``
   ``MjQtMDEtMDEiXQ``
-  Contents: ``["WDkd6JsNhDFvLP4s1hQdyA", "expiry_date", "2024-01-01"]``

**Claim** ``tax_id_code``:

-  SHA-256 Hash: ``F90SKK9nIQcHIElkHY_ult_9FGqYe-RydvY3E0qR96s``
-  Disclosure:
   ``WyI0a3NBejZiTVVLeTZadk4xaDhIRHVRIiwgInRheF9pZF9jb2RlIiwgIlRJ``
   ``TklULVhYWFhYWFhYWFhYWFhYWFgiXQ``
-  Contents: ``["4ksAz6bMUKy6ZvN1h8HDuQ", "tax_id_code",``
   ``"TINIT-XXXXXXXXXXXXXXXX"]``

**Claim** ``constant_attendance_allowance``:

-  SHA-256 Hash: ``ji86HS1v3D41tU5JqW4oWCwTJDuTUwp1ewqoCUzzEXk``
-  Disclosure:
   ``WyJEZFdxS2g3d2RJNVZBeEtTdnhzWFZRIiwgImNvbnN0YW50X2F0dGVuZGFu``
   ``Y2VfYWxsb3dhbmNlIiwgdHJ1ZV0``
-  Contents:
   ``["DdWqKh7wdI5VAxKSvxsXVQ", "constant_attendance_allowance",``
   ``true]``



The combined format for the PID issuance is represented below:

.. code-block::

  eyJhbGciOiAiRVMyNTYiLCAidHlwIjogImV4YW1wbGUrc2Qtand0In0.eyJfc2QiOiBb
  IjdXRzRuVDZLMjZfUjM5NzV6Y3duVndnb0hBN2I5ODhfMy12SnpiWmY2WWMiXSwgImlz
  cyI6ICJodHRwczovL2lzc3Vlci5leGFtcGxlLm9yZyIsICJleHAiOiAxODgzMDAwMDAw
  LCAic3ViIjogIk56YkxzWGg4dURDY2Q3bm9XWEZaQWZIa3hac1JHQzlYcyIsICJqdGki
  OiAidXJuOnV1aWQ6NmM1YzBhNDktYjU4OS00MzFkLWJhZTctMjE5MTIyYTllYzJjIiwg
  InN0YXR1cyI6ICJodHRwczovL2lzc3Vlci5leGFtcGxlLm9yZy9zdGF0dXMiLCAidmN0
  IjogIkRpc2FiaWxpdHlDYXJkIiwgInZlcmlmaWVkX2NsYWltcyI6IHsidmVyaWZpY2F0
  aW9uIjogeyJfc2QiOiBbInNUc2txMHlGeTMxWkgzWVAybk5fbkZuZDdIOXExOGRVM29F
  YTFEQzVMUmMiXSwgInRydXN0X2ZyYW1ld29yayI6ICJlaWRhcyIsICJhc3N1cmFuY2Vf
  bGV2ZWwiOiAiaGlnaCJ9LCAiY2xhaW1zIjogeyJfc2QiOiBbIjNodW1GamlDWUhkSHpq
  TC1PRWQxdktuUWExMGl2YVlFZDFkQ0NrZlJ1YUEiLCAiRVlnekoxaFRZV0pqaEJLMlYz
  YjhIVjNlX2ZFZi1VZGZmYzV5bVk3N1d0USIsICJGOTBTS0s5bklRY0hJRWxrSFlfdWx0
  XzlGR3FZZS1SeWR2WTNFMHFSOTZzIiwgIkljWUhReWRUX0MzVTFJcWFKbEZpY3hMbGFI
  VEh2RWx5Rlo2SnhpYTI3cVEiLCAiZGZybVV2b25aRGdlYWxaQ0d3azN1Zm1jXzRlcHQz
  eTlON3hoV1psQ3l4byIsICJqaTg2SFMxdjNENDF0VTVKcVc0b1dDd1RKRHVUVXdwMWV3
  cW9DVXp6RVhrIiwgImxYZ3hFREF1UGVVdm1rY05HcjlGWnVxb2R3RnFVVDAxZ0pqN3hk
  NHlFUEEiXX19LCAiX3NkX2FsZyI6ICJzaGEtMjU2IiwgImNuZiI6IHsiandrIjogeyJr
  dHkiOiAiRUMiLCAiY3J2IjogIlAtMjU2IiwgIngiOiAiVENBRVIxOVp2dTNPSEY0ajRX
  NHZmU1ZvSElQMUlMaWxEbHM3dkNlR2VtYyIsICJ5IjogIlp4amlXV2JaTVFHSFZXS1ZR
  NGhiU0lpcnNWZnVlY0NFNnQ0alQ5RjJIWlEifX19.hbgWxBoQtLVpTfygYVDhrgnoCkw
  aw_hqY9GpxG4oXixejLEMvTOAwYFtqiNnYSuNaaGD6aemJW7jLSHDm9NOGA~WyI1N212
  eWNUaDV5WkNyS0xaNXhuZlV3IiwgImlhdCIsIDE2ODMwMDAwMDBd~WyJrdWNyQm1sb19
  oTWFJRkY1ODVSemFRIiwgInNvdXJjZSIsIHsib3JnYW5pemF0aW9uX25hbWUiOiAiSXN
  0aXR1dG8gTmF6aW9uYWxlIGRlbGxhIFByZXZpZGVuemEgU29jaWFsZSIsICJvcmdhbml
  6YXRpb25faWQiOiAidXJuOmV1ZGk6aXQ6b3JnYW5pemF0aW9uX2lkOmlwYV9jb2RlOml
  ucHMiLCAiY291bnRyeV9jb2RlIjogIklUIn1d~WyJOVE5Sb09pdVZWUnRGNkNFenRkOV
  p3IiwgImV2aWRlbmNlIiwgW3sidHlwZSI6ICJlbGVjdHJvbmljX3JlY29yZCIsICJyZW
  NvcmQiOiB7Il9zZCI6IFsicWZ1enJRdUdjYkJCS2FFNFE5ZXFWQ1N6bnpKMnJObmRMRz
  hxNjA2UkxzTSJdLCAidHlwZSI6ICJodHRwczovL2V1ZGkud2FsbGV0LnBkbmQuZ292Lm
  l0In19XV0~WyJGRFNTUGdnekdCVXdRTEhEU0U2d1FRIiwgImRvY3VtZW50X251bWJlci
  IsICJYWFhYWFhYWFhYIl0~WyJLWjhlNXdWRXREdmIxemlTUEE0RHpBIiwgImdpdmVuX2
  5hbWUiLCAiTWFyaW8iXQ~WyJwWjVNUnlPeHBWV1p1SExvSi15alJnIiwgImZhbWlseV9
  uYW1lIiwgIlJvc3NpIl0~WyJqdFZ1S0NwbjdiVGNIckFnX3NlVWJRIiwgImJpcnRoX2R
  hdGUiLCAiMTk4MC0wMS0xMCJd~WyJXRGtkNkpzTmhERnZMUDRzMWhRZHlBIiwgImV4cG
  lyeV9kYXRlIiwgIjIwMjQtMDEtMDEiXQ~WyI0a3NBejZiTVVLeTZadk4xaDhIRHVRIiw
  gInRheF9pZF9jb2RlIiwgIlRJTklULVhYWFhYWFhYWFhYWFhYWFgiXQ~WyJEZFdxS2g3
  d2RJNVZBeEtTdnhzWFZRIiwgImNvbnN0YW50X2F0dGVuZGFuY2VfYWxsb3dhbmNlIiwg
  dHJ1ZV0~

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
    * - **eu.europa.ec.eudiw.pid.it.1**
      - **verification.evidence**
      - *bstr (byte string)*. As defined in the :ref:`PID/(Q)EAA Verification field Section <sec-pid-eaa-verification-field>`.
    * - **eu.europa.ec.eudiw.pid.it.1**
      - **verification.trust_framework**
      - *tstr (text string)*. As defined in the :ref:`PID/(Q)EAA Verification field Section <sec-pid-eaa-verification-field>`.
    * - **eu.europa.ec.eudiw.pid.it.1**
      - **verification.assurance_level**
      - *tstr (text string)*. As defined in the :ref:`PID/(Q)EAA Verification field Section <sec-pid-eaa-verification-field>`.
    * - **eu.europa.ec.eudiw.pid.it.1**
      - **status**
      - *tstr (text string)*. HTTPS URL where the credential validity status is available.


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
    * - **validityInfo**. 
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
    
  a366737461747573006776657273696f6e63312e3069646f63756d656e747381a267646f6354797065781865752e6575726f70612e65632e65756469772e7069642e316c6973737565725369676e6564a26a697373756572417574688443a10126a1182159021930820215308201bca003020102021404ad06a30c1a6dc6e93be0e2e8f78dcafa7907c2300a06082a8648ce3d040302305b310b3009060355040613025a45312e302c060355040a0c25465053204d6f62696c69747920616e64205472616e73706f7274206f66205a65746f706961311c301a06035504030c1349414341205a65746573436f6e666964656e73301e170d3231303932393033333034355a170d3232313130333033333034345a3050311a301806035504030c114453205a65746573436f6e666964656e7331253023060355040a0c1c5a65746f70696120436974792044657074206f662054726166666963310b3009060355040613025a453059301306072a8648ce3d020106082a8648ce3d030107034200047c5545e9a0b15f4ff3ce5015121e8ad3257c28d541c1cd0d604fc9d1e352ccc38adef5f7902d44b7a6fc1f99f06eedf7b0018fd9da716aec2f1ffac173356c7da3693067301f0603551d23041830168014bba2a53201700d3c97542ef42889556d15b7ac4630150603551d250101ff040b3009060728818c5d050102301d0603551d0e04160414ce5fd758a8e88563e625cf056bfe9f692f4296fd300e0603551d0f0101ff040403020780300a06082a8648ce3d0403020347003044022012b06a3813ffec5679f3b8cddb51eaa4b95b0cbb1786b09405e2000e9c46618c02202c1f778ad252285ed05d9b55469f1cb78d773671f30fe7ab815371942328317c59032ad818590325a667646f6354797065781865752e6575726f70612e65632e65756469772e7069642e316776657273696f6e63312e306c76616c6964697479496e666fa3667369676e6564c074323032332d30322d32325430363a32333a35365a6976616c696446726f6dc074323032332d30322d32325430363a32333a35365a6a76616c6964556e74696cc074323032342d30322d32325430303a30303a30305a6c76616c756544696765737473a2781865752e6575726f70612e65632e65756469772e7069642e31ac015820a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a025820cd372fb85148700fa88095e3492d3f9f5beb43e555e5ff26d95f5a6adc36f8e6035820e67e72111b363d80c8124d28193926000980e1211c7986cacbd26aacc5528d48045820f7d062d662826ed95869851db06bb539b402047baee53a00e0aa35bfbe98265d0658202a132dbfe4784627b86aa3807cd19cfeff487aab3dd7a60d0ab119a72e736936075820bdca9e8dbca354e824e67bfe1533fa4a238b9ea832f23fb4271ebeb3a5a8f7200858202c0eaec2f05b6c7fe7982683e3773b5d8d7a01e33d04dfcb162add8bd99bee9a095820bfe220d85657ccec3c67e7db1df747e9148a152334bb6d4b65b273279bcc36ec0a582018e38144f5044301d6a0b4ec9d5f98d4cd950e6ea2c29b849cbd457da29b6ad30b58203c71d2f0efa09d9e3fbbdffd29204f6b292c9f79570aef72dd86c91f7a3aa5c50c582065743d58d89d45e52044758f546034fd13a4f994bc270cdfa7844f74eb3f4b6e0d5820b4a8eb5d523bffa17b41bda12ddc7da32ae1e5f7ff3dcc394a35401f16919bbf781b65752e6575726f70612e65632e65756469772e7069642e69742e31a10e58209d6c11644651126c94acdaf0803e86d4c71d15d3b2712a14295416734efd514d6d6465766963654b6579496e666fa1696465766963654b6579a401022001215820ba01aea44eee1e338eb2f04e279dbd51b34655783ee185150838c9a7a7c4db7122582025ba0044439a3871a7b975a0994a85e79b705a9ac263b3fe899b0a93412ee8c96f646967657374416c676f726974686d675348412d32353658400813c28fd62f2602cbc14724e5865733c44a0fca589b55c085ec9d5c725d6cce25ba0044439a3871a7b975a0994a85e79b705a9ac263b3fe899b0a93412ee8c96a6e616d65537061636573a2781865752e6575726f70612e65632e65756469772e7069642e318cd818586da4686469676573744944016672616e646f6d5820156df9227ad341eaa61aabd301106fd21bdc18820e01dfc16bcf5fecc447111b71656c656d656e744964656e7469666965726b6578706972795f646174656c656c656d656e7456616c7565d903ec6a323032342d30322d3232d818586fa4686469676573744944026672616e646f6d5820a3a1f13f05544d03a5b50b5fdb78465808393bcf3b7953a345fe28f820c7be0d71656c656d656e744964656e7469666965726d69737375616e63655f646174656c656c656d656e7456616c7565d903ec6a323032332d30322d3232d8185866a4686469676573744944036672616e646f6d5820852591f90f2c9ded57a03632e2c1322ab52a082a431e71a4149a6830c8f1ad0c71656c656d656e744964656e7469666965726f69737375696e675f636f756e7472796c656c656d656e7456616c7565624954d818587ca4686469676573744944046672616e646f6d5820d1d587b3512acce15c4f6b20944ceb002a464e4a158389788563408873c3fce571656c656d656e744964656e7469666965727169737375696e675f617574686f726974796c656c656d656e7456616c7565764d696e69737465726f2064656c6c27496e7465726e6fd8185864a4686469676573744944056672616e646f6d582094fdd7609c0e73dc8589b5cab11e1d9058cf8bff8a336da5f81fcba055396a0f71656c656d656e744964656e7469666965726a676976656e5f6e616d656c656c656d656e7456616c7565654d6172696fd8185865a4686469676573744944066672616e646f6d5820660c0a7bf79e0e0261ca1547a4294fb808aa70738f424b13ab1b9440b566ae1371656c656d656e744964656e7469666965726b66616d696c795f6e616d656c656c656d656e7456616c756565526f737369d818586ba4686469676573744944076672616e646f6d5820315c53491286488fa07f5c2ce67135ef5c9959c3469c99a14e9b6dc924f9eba571656c656d656e744964656e746966696572696269727468646174656c656c656d656e7456616c7565d903ec6a313935362d30312d3132d818587da4686469676573744944086672616e646f6d5820764ef39c9d01f3aa6a87f441603cfe853fba3cee3bc2c168bcc9e96271d6e06371656c656d656e744964656e74696669657269756e697175655f69646c656c656d656e7456616c7565781e78787878787878782d7878782d787878782d787878787878787878787878d81858e8a4686469676573744944096672616e646f6d5820ad20b3b9c67aed8089ff33ecdc108781c3b49b81cd7a3f059d2fe236977037b271656c656d656e744964656e74696669657275766572696669636174696f6e2e65766964656e63656c656c656d656e7456616c756581a2647479706571656c656374726f6e69635f7265636f7264667265636f7264a264747970656c65696461732e69742e63696566736f75726365a3716f7267616e697a6174696f6e5f6e616d656c65696461732e69742e6369656f6f7267616e697a6174696f6e5f6964646d5f69746c636f756e7472795f636f6465626974d8185879a46864696765737449440a6672616e646f6d5820c12314b3695d1401505187e2113115e2f7b4a14b135dee320f5e6df81275f17671656c656d656e744964656e746966696572667374617475736c656c656d656e7456616c7565781d68747470733a2f2f70696470726f76696465722e69742f737461747573d8185877a46864696765737449440b6672616e646f6d5820a7b6a9027ed97f25df96dd0eab8093b264a3bd6a1d5b24228f3fc5b18ef835fb71656c656d656e744964656e746966696572781c766572696669636174696f6e2e74727573745f6672616d65776f726b6c656c656d656e7456616c7565656569646173d8185876a46864696765737449440c6672616e646f6d5820c76ce2ae4e9be1db07a5cb397b54ace3eccc786d3f85e4348b923dee059783db71656c656d656e744964656e746966696572781c766572696669636174696f6e2e6173737572616e63655f6c6576656c6c656c656d656e7456616c75656468696768781b65752e6575726f70612e65632e65756469772e7069642e69742e3181d8185877a46864696765737449440d6672616e646f6d5820717df3f583b1484366c33a1f869f2b5d201d466a8b589c79ab1a2d85e595432571656c656d656e744964656e7469666965726d7461785f69645f6e756d6265726c656c656d656e7456616c75657554494e49542d585858585858585858585858585858

The `Diagnostic Notation` of the above MDOC-CBOR is given below:

.. code-block:: text
    
  {     
    "status": 0,     
    "version": "1.0",     
    "documents": [        
      {             
      "docType": "eu.europa.ec.eudiw.pid.1",                         
      "issuerSigned": {                
          "issuerAuth": [                
          << {1: -7} >>, % protected header with the value alg:ES256                    
          {                         
              33: h'30820215308201BCA003020102021404AD30C…'% 33->X5chain:COSE X_509  
          },
          <<                       
              24(<<    
                  {                            
                  "docType": "eu.europa.ec.eudiw.pid.1",                                
                  "version": "1.0",  
                  "validityInfo": {                                
                      "signed": 0("2023-02-22T06:23:56Z"),                                     
                      "validFrom": 0("2023-02-22T06:23:56Z"),                                   
                      "validUntil": 0("2024-02-22T00:00:00Z")                               
                  },
                  "valueDigests": { 
                      "eu.europa.ec.eudiw.pid.1": {        
                          1:h'0F1571A97FFB799CC8FCDF2BA4FC2909929…',                                          
                          2: h'0CDFE077400432C055A2B69596C90…',     
                          3: h'E2382149255AE8E955AF9B8984395…',                                        
                          4: h'BBC77E6CCA981A3AD0C3E544EDF86…',                                     
                          6: h'BB6E6C68D1B4B4EC5A2AE9206F5t4…',
                          7: h'F8A5966E6DAC9970E0334D8F75E25…',              
                          8: h'DEFDF1AA746718016EF1B94BFE5R6…'
                      },
                      "eu.europa.ec.eudiw.pid.it.1": {  
                          9: h'AFC5A127BE44753172844B13491D8…',
                          10: h'AFC5A127BE44753172844B13492H4…',
                          11: h'DJA5A127BE44753172844B13492H4…',
                          12: h'KDL5A127BE44753172844B13492H4…',
                          13: h'F9EE4D36F67DBD75E23311AC1C29…'
                      }
                  },                             
                  "deviceKeyInfo": {                              
                      "deviceKey": {                                  
                          1: 2, % kty:EC2 (Eliptic curves with x and y coordinate pairs)           
                          -1: 1, % crv:p256                     
                          -2: h'B820963964E53AF064686DD9218303494A…', % x-coordiantes                                        
                          -3: h'0A6DA0AF437E2943F1836F31C678D89298E9…'% y-ccordiantes                                     
                      }                            
                  },                             
                  "digestAlgorithm": "SHA-256"    
                  }                       
              >>)                     
          >>,                        
          h'1AD0D6A7313EFDC38FCD765852FA2BD43DEBF48BF5A580D'                 
          ],                 
          "nameSpaces": {
              "eu.europa.ec.eudiw.pid.1": [                         
              24(<<    
                  {      
                  "digestID": 1,                                  
                  "random": h'E0B70BCEFBD43686F345C9ED429343AA',                                 
                  "elementIdentifier": "expiry_date",                                
                  "elementValue": 1004("2024-02-22")                             
                  }                         
              >>), 
              24(<<             
                  {       
                  "digestID": 2,                                  
                  "random": h'AE84834F389EE69888665B90A3E4FCCE', 
                  "elementIdentifier": "issue_date",   
                  "elementValue": 1004("2023-02-22")                                
                  }
              >>),                         
              24(<<   
                  {                              
                  "digestID": 3,                                 
                  "random": h'960CB15A2EA9B68E5233CE902807AA95',                               
                  "elementIdentifier": "issuing_country",                               
                  "elementValue": "IT"                                                    
                  }                       
              >>), 
              24(<<       
                  {                        
                  "digestID": 4,    
                  "random": h'9D3774BD5994CCFED248674B32A4F76A', 
                  "elementIdentifier": "issuing_authority",   
                  "elementValue": "Ministero dell'Interno"  
                  }   
              >>),                 
              24(<<        
                  {                              
                  "digestID": 5,                         
                  "random": h'EB12193DC66C6174530CDC29B274381F', 
                  "elementIdentifier": "given_name",
                  "elementValue": "Mario"                             
                  }                         
              >>)),            
              24(<<                            
                  {                               
                  "digestID": 6,                             
                  "random": h'DB143143538F3C8D41DC024F9CB25C9D',
                  "elementIdentifier": "family_name",  
                  "elementValue": "Rossi"    
                  } 
              >>),                         
              24(<<               
                  {                          
                  "digestID": 7, 
                  "random": h'6059FF1CE27B4997B4ADE1DE7B01DC60',
                  "elementIdentifier": "birth_date",
                  "elementValue": 1004("1956-01-12")% the tag 1004 defines the value    
                                                      is a full date 
                  }  
              >>),         
              24(<<  
                  {                              
                  "digestID": 8,                              
                  "random": h'53C15C57B3B076E788795829190220B4',
                  "elementIdentifier": "unique_id",
                  "elementValue": "xxxxxxxx-xxx-xxxx-xxxxxxxxxxxx" 
                  }   
              >>)
              ],
              "eu.europa.ec.eudiw.pid.it.1": [
                  24(<<  
                      {                               
                      "digestID": 9, 
                      "random": h'CAD1F6A38F603451F1FA653F81FF309D',
                      "elementIdentifier": "verification.evidence",
                      "elementValue": [  
                          {
                          "type": "electronic_record", 
                          "record": {
                              "type": "eidas.it.cie",
                              "source": {         
                                  "organization_name": "eidas.it.cie",
                                  "organization_id":  "m_it",
                                  "country_code": "it",
                              }
                          }   
                          }
                      ]
                      }                       
                  >>),
                  24(<<    
                      {      
                      "digestID": 10,                                  
                      "random": h'CAD1F6A38F603451F1FA653F81FF309D,                                 
                      "elementIdentifier": "status",                                
                      "elementValue": "https://pidprovider.example.it/status"                            
                      }                         
                  >>),
                  24(<<  
                      {                               
                      "digestID": 11, 
                      "random": h'564E3C65D46D06FEDEB0E7293A86GF',
                      "elementIdentifier": "verification.trust_framework",
                      "elementValue": "eidas" 
                      }                       
                  >>),
                  24(<<  
                      {                               
                      "digestID": 12, 
                      "random": h'D884E5D5EF4CFC93FDB1E4EE8F3923',
                      "elementIdentifier": "verification.assurance_level",
                      "elementValue": "high" 
                      }                       
                  >>)  
                  24(<<
                      {
                      "digestID": 13, 
                      "random": h'11aa7273a2d2daa973f5951f0c34c2fbae',
                      "elementIdentifier": "tax_id_number", 
                      "elementValue": "TINIT-XXXXXXXXXXXXXXX"
                      }                         
                  >>)                    
              ]            
          }  
      }           
      }
    ]
  }



