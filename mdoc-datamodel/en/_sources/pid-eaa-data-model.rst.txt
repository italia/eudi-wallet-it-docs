
.. include:: ../common/common_definitions.rst

.. _pid_eaa_data_model.rst:

PID/(Q)EAA Data Model
+++++++++++++++++++++

The Person Identification Data (PID) is issued by the PID Provider following national laws and allows a natural person to be authenitcated and identified. 
The User attributes carried within the Italian PID are the ones listed below:

    - Current Family Name
    - Current First Name
    - Date of Birth
    - Place of Birth
    - Unique Identifier
    - Taxpayer identification number

The italian PID is extended according to the `OpenID Identity Assurance Profile [OIDC.IDA] <https://openid.net/specs/openid-connect-4-identity-assurance-1_0-13.html>`_, that enables the binding of the PID to a national trust framework, giving all the evidence of the identity proofing procedures underlying the PID issuing in both remote and proximity flows.

The (Q)EAAs are issued by (Q)EAA Issuers to a Wallet Instance and MUST be provided in SD-JWT-VC or mDOC CBOR data format. 

The (Q)EAAs are extended according to the `OpenID Identity Assurance Profile [OIDC.IDA] <https://openid.net/specs/openid-connect-4-identity-assurance-1_0-13.html>`_, that allows the recipients to know the Authentic Sources where the data comes from. 

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

The following claims MUST be in the JWT payload and MUST NOT be included in the disclosures,  i.e. cannot be selectively disclosed. 

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - URL string representing the PID/(Q)EAA Issuer unique identifier.
      - `[RFC7519, Section 4.1.1] <https://www.iana.org/go/rfc7519>`_.
    * - **sub**
      - Thumbprint of the JWK in the ``cnf`` parameter.
      - `[RFC7519, Section 4.1.2] <https://www.iana.org/go/rfc7519>`_.
    * - **jti**
      - Unique Token ID identifier of this JWT. It SHOULD be a String in *uuid4* format.
      - `[RFC7519, Section 4.1.7] <https://www.iana.org/go/rfc7519>`_.
    * - **iat**
      - UNIX Timestamp with the time of JWT issuance, coded as NumericDate as indicated in :rfc:`7519`. 
      - `[RFC7519, Section 4.1.6] <https://www.iana.org/go/rfc7519>`_.
    * - **exp**
      - UNIX Timestamp with the expiry time of the JWT, coded as NumericDate as indicated in :rfc:`7519`.
      - `[RFC7519, Section 4.1.4] <https://www.iana.org/go/rfc7519>`_.
    * - **status**
      - HTTPS URL where the credential validity status is available.
      - `[SD-JWT-VC. Section 4.2.2.2] <https://vcstuff.github.io/draft-terbu-sd-jwt-vc/draft-terbu-sd-jwt-vc.html#section-4.2.2.2>`_.
    * - **cnf**
      - JSON object containing the proof-of-possession key materials. By including a **cnf** (confirmation) claim in a JWT, the issuer of the JWT declares that the Holder is in control of the private key related to the public one defined in the **cnf** parameter. The recipient MUST cryptographically verify that the Holder is in control of that key. 
      - `[RFC7800, Section 3.1] <https://www.iana.org/go/rfc7800>`_.
    * - **vct**
      - Credential type as a string, MUST be set in accordance to the type obtained from the PID/(Q)EAA Issuer metadata. For example, in the case of the PID, it MUST be set to ``PersonIdentificationData``.
      - `[draft-terbu-sd-jwt-vc-latest. Section Type Claim] <https://drafts.oauth.net/oauth-sd-jwt-vc/draft-ietf-oauth-sd-jwt-vc.html#type-claim>`__.
    * - **verified_claims**
      - JSON object containing the following sub-elements: 

            -   **verification**; 
            -   **claims**.
      - `[OIDC.IDA. Section 5] <https://openid.net/specs/openid-connect-4-identity-assurance-1_0-13.html#section-5>`_.


PID/(Q)EAA Verification field 
-----------------------------

The ``verification`` claim contains the information regarding the trust framework used by the PID/(Q)EAA Issuer to provide the User attributes (claims).  Some of these additional claims MAY be selectively disclosed, these are listed in the following tables that specify whether a claim is selectively disclosable (SD) or not (NSD).

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
    * - **birthdate**
      - [SD]. Date of Birth.
      - `[OpenID Connect Core 1.0, Section 5.1] <http://openid.net/specs/openid-connect-core-1_0.html>`_
    * - **place_of_birth**
      - [SD]. Place of Birth. JSON Object with the following subclaims:

        - **country**
        - **locality**
      - `[OpenID Connect for Identity Assurance 1.0, Section 4] <https://openid.net/specs/openid-connect-4-identity-assurance-1_0-13.html#section-4>`_
    * - **unique_id**
      - [SD]. Unique citizen identifier (ID ANPR) given by the National Register of the Resident Population (ANPR). It MUST be set according to `ANPR rules <https://www.anagrafenazionale.interno.it/anpr/notizie/identificativo-unico-nazionale-idanpr/>`_
      - This specification
    * - **tax_id_code**
      - [SD]. National tax identification code of natural person as a String format. It MUST be set according to ETSI EN 319 412-1. For example ``TINIT-<ItalianTaxIdentificationNumber>``
      - This specification



PID Non-normative Examples
--------------------------

In the following, the non-normative example of a PID.

.. code-block:: JSON

  {
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
                "organization_id": "m_it",
                "country_code": "IT"
              }
            }
          }
        ]
      },
      "claims": {
        "unique_id":
          "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "given_name": "Mario",
        "family_name": "Rossi",
        "birthdate": "1980-01-10",
        "place_of_birth": {
          "country": "IT",
          "locality": "Rome"
        },
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
    "iss": "https://pidprovider.example.org",
    "sub": "NzbLsXh8uDCcd7noWXFZAfHkxZsRGC9Xs...",
    "jti": "urn:uuid:6c5c0a49-b589-431d-bae7-219122a9ec2c",
    "iat": 1541493724,
    "exp": 1541493724,
    "status": "https://pidprovider.example.org/status",
    "cnf": {
      "jwk": {
        "kty": "RSA",
        "use": "sig",
        "n": "1Ta-sE …",
        "e": "AQAB",
        "kid": "YhNFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs"
      }
    },
    "type": "PersonIdentificationData",
    "verified_claims": {
      "verification": {
        "_sd": [
          "OGm7ryXgt5Xzlevp-Hu-UTk0a-TxAaPAobqv1pIWMfw"
        ],
        "trust_framework": "eidas",
        "assurance_level": "high"
      },
      "claims": {
        "_sd": [
          "8JjozBfovMNvQ3HflmPWy4O19Gpxs61FWHjZebU589E",
          "BoMGktW1rbikntw8Fzx_BeL4YbAndr6AHsdgpatFCig",
          "CFLGzentGNRFngnLVVQVcoAFi05r6RJUX-rdbLdEfew",
          "JU_sTaHCngS32X-0ajHrd1-HCLCkpT5YqgcfQme168w",
          "VQI-S1mT1Kxfq2o8J9io7xMMX2MIxaG9M9PeJVqrMcA",
          "zVdghcmClMVWlUgGsGpSkCPkEHZ4u9oWj1SlIBlCc1o"
        ]
      }
    },
    "_sd_alg": "sha-256"
  }

In the following the disclosure list is given

Claim **evidence**:

-  SHA-256 Hash: ``OGm7ryXgt5Xzlevp-Hu-UTk0a-TxAaPAobqv1pIWMfw``
-  Disclosure:
   ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgImV2aWRlbmNlIiwgW3sidHlw``
   ``ZSI6ICJlbGVjdHJvbmljX3JlY29yZCIsICJyZWNvcmQiOiB7InR5cGUiOiAi``
   ``ZWlkYXMuaXQuY2llIiwgInNvdXJjZSI6IHsib3JnYW5pemF0aW9uX25hbWUi``
   ``OiAiTWluaXN0ZXJvIGRlbGwnSW50ZXJubyIsICJvcmdhbml6YXRpb25faWQi``
   ``OiAibV9pdCIsICJjb3VudHJ5X2NvZGUiOiAiSVQifX19XV0``
-  Contents: ``["2GLC42sKQveCfGfryNRN9w", "evidence", [{"type":``
   ``"electronic_record", "record": {"type": "https://eudi.wallet.cie.gov.it",``
   ``"source": {"organization_name": "Ministero dell'Interno",``
   ``"organization_id": "m_it", "country_code": "IT"}}}]]``

Claim **unique_id**:

-  SHA-256 Hash: ``BoMGktW1rbikntw8Fzx_BeL4YbAndr6AHsdgpatFCig``
-  Disclosure:
   ``WyJlbHVWNU9nM2dTTklJOEVZbnN4QV9BIiwgInVuaXF1ZV9pZCIsICJ4eHh4``
   ``eHh4eC14eHh4LXh4eHgteHh4eC14eHh4eHh4eHh4eHgiXQ``
-  Contents: ``["eluV5Og3gSNII8EYnsxA_A", "unique_id",``
   ``"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]``

Claim **given_name**:

-  SHA-256 Hash: ``zVdghcmClMVWlUgGsGpSkCPkEHZ4u9oWj1SlIBlCc1o``
-  Disclosure:
   ``WyI2SWo3dE0tYTVpVlBHYm9TNXRtdlZBIiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
-  Contents: ``["6Ij7tM-a5iVPGboS5tmvVA", "given_name", "Mario"]``

Claim **family_name**:

-  SHA-256 Hash: ``VQI-S1mT1Kxfq2o8J9io7xMMX2MIxaG9M9PeJVqrMcA``
-  Disclosure:
   ``WyJlSThaV205UW5LUHBOUGVOZW5IZGhRIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
-  Contents: ``["eI8ZWm9QnKPpNPeNenHdhQ", "family_name", "Rossi"]``

Claim **birthdate**:

-  SHA-256 Hash: ``CFLGzentGNRFngnLVVQVcoAFi05r6RJUX-rdbLdEfew``
-  Disclosure:
   ``WyJRZ19PNjR6cUF4ZTQxMmExMDhpcm9BIiwgImJpcnRoZGF0ZSIsICIxOTgw``
   ``LTAxLTEwIl0``
-  Contents: ``["Qg_O64zqAxe412a108iroA", "birthdate", "1980-01-10"]``

Claim **place_of_birth**:

-  SHA-256 Hash: ``JU_sTaHCngS32X-0ajHrd1-HCLCkpT5YqgcfQme168w``
-  Disclosure:
   ``WyJBSngtMDk1VlBycFR0TjRRTU9xUk9BIiwgInBsYWNlX29mX2JpcnRoIiwg``
   ``eyJjb3VudHJ5IjogIklUIiwgImxvY2FsaXR5IjogIlJvbWUifV0``
-  Contents:
   ``["AJx-095VPrpTtN4QMOqROA", "place_of_birth", {"country":``
   ``"IT", "locality": "Rome"}]``

Claim **tax_id_code**:

-  SHA-256 Hash: ``8JjozBfovMNvQ3HflmPWy4O19Gpxs61FWHjZebU589E``
-  Disclosure:
   ``WyJQYzMzSk0yTGNoY1VfbEhnZ3ZfdWZRIiwgInRheF9pZF9jb2RlIiwgIlRJ``
   ``TklULVhYWFhYWFhYWFhYWFhYWFgiXQ``
-  Contents: ``["Pc33JM2LchcU_lHggv_ufQ", "tax_id_code",``
   ``"TINIT-XXXXXXXXXXXXXXXX"]``

The combined format for the PID issuance is given by

.. code-block::

  eyJ0eXAiOiJ2YytzZC1qd3QiLCJhbGciOiJSUzUxMiIsImtpZCI6ImQxMjZhNmE4NTZmNzcyNDU2MDQ4NGZhOWRjNTlkMTk1IiwidHJ1c3RfY2hhaW4iOlsiTkVoUmRFUnBZbmxIWTNNNVdsZFdUV1oyYVVobSAuLi4iLCJleUpoYkdjaU9pSlNVekkxTmlJc0ltdHBaQ0k2IC4uLiIsIklrSllkbVp5Ykc1b1FVMTFTRkl3TjJGcVZXMUIgLi4uIl19.eyJpc3MiOiJodHRwczovL3BpZHByb3ZpZGVyLmV4YW1wbGUub3JnIiwic3ViIjoiTnpiTHNYaDh1RENjZDdub1dYRlpBZkhreFpzUkdDOVhzLi4uIiwianRpIjoidXJuOnV1aWQ6NmM1YzBhNDktYjU4OS00MzFkLWJhZTctMjE5MTIyYTllYzJjIiwiaWF0IjoxNTQxNDkzNzI0LCJleHAiOjE1NDE0OTM3MjQsInN0YXR1cyI6Imh0dHBzOi8vcGlkcHJvdmlkZXIuZXhhbXBsZS5vcmcvc3RhdHVzIiwiY25mIjp7Imp3ayI6eyJrdHkiOiJSU0EiLCJ1c2UiOiJzaWciLCJuIjoiMVRhLXNFIOKApiIsImUiOiJBUUFCIiwia2lkIjoiWWhORlMzWW5DOXRqaUNhaXZoV0xWVUozQXh3R0d6Xzk4dVJGYXFNRUVzIn19LCJ0eXBlIjoiUGVyc29uSWRlbnRpZmljYXRpb25EYXRhIiwidmVyaWZpZWRfY2xhaW1zIjp7InZlcmlmaWNhdGlvbiI6eyJfc2QiOlsiT0dtN3J5WGd0NVh6bGV2cC1IdS1VVGswYS1UeEFhUEFvYnF2MXBJV01mdyJdLCJ0cnVzdF9mcmFtZXdvcmsiOiJlaWRhcyIsImFzc3VyYW5jZV9sZXZlbCI6ImhpZ2gifSwiY2xhaW1zIjp7Il9zZCI6WyI4SmpvekJmb3ZNTnZRM0hmbG1QV3k0TzE5R3B4czYxRldIalplYlU1ODlFIiwiQm9NR2t0VzFyYmlrbnR3OEZ6eF9CZUw0WWJBbmRyNkFIc2RncGF0RkNpZyIsIkNGTEd6ZW50R05SRm5nbkxWVlFWY29BRmkwNXI2UkpVWC1yZGJMZEVmZXciLCJKVV9zVGFIQ25nUzMyWC0wYWpIcmQxLUhDTENrcFQ1WXFnY2ZRbWUxNjh3IiwiVlFJLVMxbVQxS3hmcTJvOEo5aW83eE1NWDJNSXhhRzlNOVBlSlZxck1jQSIsInpWZGdoY21DbE1WV2xVZ0dzR3BTa0NQa0VIWjR1OW9XajFTbElCbENjMW8iXX19LCJfc2RfYWxnIjoic2hhLTI1NiJ9.WzEiFaOjnobQisjTQ92JtKEXRN-2Sgvjklpu4IdC_cT2T6Tm8Z6sqbVy6n94AAEv-HFSv5JoSt6YjPDnGzOxN_W_131rILU8YaiNt8w31nRGIvHjJIC0w-hHIcG1LmvJshSMcT3RHeApRCmsO7xkHWmUsjt37dOzEagEti5i47hnZAbu7vWXsvUlBNNN8v7tJBLspO2Q0vnWhEDX1hQ7IH1b8oKh-_aQrhwVm9Bcs9CG8o6N9iqubCSpFI6Gty4ZZgHEb95knETVhw8IL10Z9P_Hr9twXZQaCCC8xrNh4afwR9TiDQzTr92m7luyvDfmzVgHCponI7VBhqmRqZVYQyDhq6EJbtRtIsYenla5NSKBjV8Etdlec94vJAHZNzue9aNUQeXae55V5m5O9wLoWhgV2vl4xV5C-N5s5Uzs08GAxo-CUaNOD3BQE9vfrT47IBCm4hUCnvDise_aWNCeKOQABV1J9_tV9lWZsECVuUuWWwELHCUXgdyiA3QtUtXz

(Q)EAA Non-normative examples
-----------------------------

In the following, we provide a non-normative example of (Q)EAA in JSON.

.. code-block:: JSON

  {
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
                "organization_name": "Ragioneria Generale dello Stato",
                "organization_id": "urn:eudi:it:organization_id:ipa_code:QLHCFC",
                "country_code": "IT"
              }
            }
          }
        ]
      },
      "claims": {
        "given_name": "Mario",
        "family_name": "Rossi",
        "birthdate": "1980-01-10",
        "place_of_birth": {
          "country": "IT",
          "locality": "Rome"
        },
        "tax_id_code": "TINIT-XXXXXXXXXXXXXXXX"
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
    "iss": "https://issuer.example.org",
    "sub": "NzbLsXh8uDCcd7noWXFZAfHkxZsRGC9Xs...",
    "jti": "urn:uuid:6c5c0a49-b589-431d-bae7-219122a9ec2c",
    "iat": 1541493724,
    "exp": 1541493724,
    "status": "https://issuer.example.org/status",
    "cnf": {
      "jwk": {
        "kty": "RSA",
        "e": "AQAB",
        "use": "sig",
        "kid": "d126a6a856f7724560484fa9dc59d195",
        "alg": "RS256",
        "n": "oians5wYCWk4wFtEStVYcn_xOw9edKMNGH33_q6_pBI0XaTY7P3apUgjO0ivk5c1NQAVY6PZmcPQ8P1Y0cBAC9STRmzvTvDQcOocLhVy2ZlcXTu39oOGLNra8_LQsaMA386lO_qMW4-uY6DbGZY4vHkScvAC9FIZYDPafqWBEQUNV2QOFMH5VPoihCTKHwMGXnZBatYObg57xSOUX-bvhO_sFMm3k4RvsXcr3MFojAhLfwutu_jK9k7N9KR_mNc5IpiOyhZw_sUmF6SamRqsSPp42KD10hPMW0YJTDMYxBdHrMFeSMHYIMY4oBBT43__a55zILI_CnIk4241wOvGvw"
      }
    },
    "type": "HealthInsuranceData",
    "verified_claims": {
      "verification": {
        "_sd": [
          "2jIR18gfeASHYGB27s7sS3S_iQ4xxFIxCRyiohrBfns"
        ],
        "trust_framework": "eidas",
        "assurance_level": "high"
      },
      "claims": {
        "_sd": [
          "1iztq7bov64xTYbDkWFc44_VjWe029hZqXeUIloqUN4",
          "ENNo31jfzFp8Y2DW0R-fIMeWwe7ELGvGoHMwMBpu14E",
          "FV2CDNWuTqTgOHaftvVaumBF0OlmnyxMswyf4uIxrhY",
          "dZWjq7mJSSX-XTI_HWuE8B2x6IdM5lE-doD_yBpKJao",
          "gHYi19frbD_i4BoaWENOjc3lCnMj4pbGNQcsBj_QM4Q"
        ]
      }
    },
    "_sd_alg": "sha-256"
  }

In the following the disclosure list is given:

Claim **evidence**:

-  SHA-256 Hash: ``2jIR18gfeASHYGB27s7sS3S_iQ4xxFIxCRyiohrBfns``
-  Disclosure:
   ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgImV2aWRlbmNlIiwgW3sidHlw``
   ``ZSI6ICJlbGVjdHJvbmljX3JlY29yZCIsICJyZWNvcmQiOiB7InR5cGUiOiAi``
   ``ZWlkYXMuaXQucGRuZCIsICJzb3VyY2UiOiB7Im9yZ2FuaXphdGlvbl9uYW1l``
   ``IjogIlJhZ2lvbmVyaWEgR2VuZXJhbGUgZGVsbG8gU3RhdG8iLCAib3JnYW5p``
   ``emF0aW9uX2lkIjogIlFMSENGQyIsICJjb3VudHJ5X2NvZGUiOiAiSVQifX19``
   ``XV0``
-  Contents: ``["2GLC42sKQveCfGfryNRN9w", "evidence", [{"type":``
   ``"electronic_record", "record": {"type": "https://eudi.wallet.pdnd.gov.it",``
   ``"source": {"organization_name": "Ragioneria Generale dello Stato",``
   ``"organization_id": "QLHCFC", "country_code":"IT"}}}]]``

Claim **given_name**:

-  SHA-256 Hash: ``gHYi19frbD_i4BoaWENOjc3lCnMj4pbGNQcsBj_QM4Q``
-  Disclosure:
   ``WyJlbHVWNU9nM2dTTklJOEVZbnN4QV9BIiwgImdpdmVuX25hbWUiLCAiTWFyaW8iXQ``
-  Contents: ``["eluV5Og3gSNII8EYnsxA_A", "given_name", "Mario"]``

Claim **family_name**:

-  SHA-256 Hash: ``dZWjq7mJSSX-XTI_HWuE8B2x6IdM5lE-doD_yBpKJao``
-  Disclosure:
   ``WyI2SWo3dE0tYTVpVlBHYm9TNXRtdlZBIiwgImZhbWlseV9uYW1lIiwgIlJvc3NpIl0``
-  Contents: ``["6Ij7tM-a5iVPGboS5tmvVA", "family_name", "Rossi"]``

Claim **birthdate**:

-  SHA-256 Hash: ``FV2CDNWuTqTgOHaftvVaumBF0OlmnyxMswyf4uIxrhY``
-  Disclosure:
   ``WyJlSThaV205UW5LUHBOUGVOZW5IZGhRIiwgImJpcnRoZGF0ZSIsICIxOTgwLTAxLTEwIl0``
-  Contents: ``["eI8ZWm9QnKPpNPeNenHdhQ", "birthdate", "1980-01-10"]``

Claim **place_of_birth**:

-  SHA-256 Hash: ``1iztq7bov64xTYbDkWFc44_VjWe029hZqXeUIloqUN4``
-  Disclosure:
   ``WyJRZ19PNjR6cUF4ZTQxMmExMDhpcm9BIiwgInBsYWNlX29mX2JpcnRoIiwg``
   ``eyJjb3VudHJ5IjogIklUIiwgImxvY2FsaXR5IjogIlJvbWUifV0``
-  Contents:
   ``["Qg_O64zqAxe412a108iroA", "place_of_birth", {"country":``
   ``"IT", "locality": "Rome"}]``

Claim **tax_id_code**:

-  SHA-256 Hash: ``ENNo31jfzFp8Y2DW0R-fIMeWwe7ELGvGoHMwMBpu14E``
-  Disclosure:
   ``WyJBSngtMDk1VlBycFR0TjRRTU9xUk9BIiwgInRheF9pZF9jb2RlIiwgIlRJ``
   ``TklULVhYWFhYWFhYWFhYWFhYWFgiXQ``
-  Contents: ``["AJx-095VPrpTtN4QMOqROA", "tax_id_code",``
   ``"TINIT-XXXXXXXXXXXXXXXX"]``

The combined format for the PID issuance is represented below:

.. code-block::

  eyJhbGciOiJSUzI1NiIsImtpZCI6Iks2S2hpUDNrOC1XOWVHdk1SVTg0NVVwWVRTdEJsR0g4ejFKZl85czMtUWsifQ.eyJpc3MiOiJodHRwczovL2lzc3Vlci5leGFtcGxlLm9yZyIsInN1YiI6Ik56YkxzWGg4dURDY2Q3bm9XWEZaQWZIa3hac1JHQzlYcy4uLiIsImp0aSI6InVybjp1dWlkOjZjNWMwYTQ5LWI1ODktNDMxZC1iYWU3LTIxOTEyMmE5ZWMyYyIsImlhdCI6MTU0MTQ5MzcyNCwiZXhwIjoxNTQxNDkzNzI0LCJzdGF0dXMiOiJodHRwczovL2lzc3Vlci5leGFtcGxlLm9yZy9zdGF0dXMiLCJjbmYiOnsiandrIjp7Imt0eSI6IlJTQSIsImUiOiJBUUFCIiwidXNlIjoic2lnIiwia2lkIjoiZDEyNmE2YTg1NmY3NzI0NTYwNDg0ZmE5ZGM1OWQxOTUiLCJhbGciOiJSUzI1NiIsIm4iOiJvaWFuczV3WUNXazR3RnRFU3RWWWNuX3hPdzllZEtNTkdIMzNfcTZfcEJJMFhhVFk3UDNhcFVnak8waXZrNWMxTlFBVlk2UFptY1BROFAxWTBjQkFDOVNUUm16dlR2RFFjT29jTGhWeTJabGNYVHUzOW9PR0xOcmE4X0xRc2FNQTM4NmxPX3FNVzQtdVk2RGJHWlk0dkhrU2N2QUM5RklaWURQYWZxV0JFUVVOVjJRT0ZNSDVWUG9paENUS0h3TUdYblpCYXRZT2JnNTd4U09VWC1idmhPX3NGTW0zazRSdnNYY3IzTUZvakFoTGZ3dXR1X2pLOWs3TjlLUl9tTmM1SXBpT3loWndfc1VtRjZTYW1ScXNTUHA0MktEMTBoUE1XMFlKVERNWXhCZEhyTUZlU01IWUlNWTRvQkJUNDNfX2E1NXpJTElfQ25JazQyNDF3T3ZHdncifX0sInR5cGUiOiJIZWFsdGhJbnN1cmFuY2VEYXRhIiwidmVyaWZpZWRfY2xhaW1zIjp7InZlcmlmaWNhdGlvbiI6eyJfc2QiOlsiMmpJUjE4Z2ZlQVNIWUdCMjdzN3NTM1NfaVE0eHhGSXhDUnlpb2hyQmZucyJdLCJ0cnVzdF9mcmFtZXdvcmsiOiJlaWRhcyIsImFzc3VyYW5jZV9sZXZlbCI6ImhpZ2gifSwiY2xhaW1zIjp7Il9zZCI6WyIxaXp0cTdib3Y2NHhUWWJEa1dGYzQ0X1ZqV2UwMjloWnFYZVVJbG9xVU40IiwiRU5ObzMxamZ6RnA4WTJEVzBSLWZJTWVXd2U3RUxHdkdvSE13TUJwdTE0RSIsIkZWMkNETld1VHFUZ09IYWZ0dlZhdW1CRjBPbG1ueXhNc3d5ZjR1SXhyaFkiLCJkWldqcTdtSlNTWC1YVElfSFd1RThCMng2SWRNNWxFLWRvRF95QnBLSmFvIiwiZ0hZaTE5ZnJiRF9pNEJvYVdFTk9qYzNsQ25NajRwYkdOUWNzQmpfUU00USJdfX0sIl9zZF9hbGciOiJzaGEtMjU2In0.vl5ELdx9d7smuDHHDfBGaUySolBe7O3RROqpHDkM3txvXJxgZcCwZQhbWN3sSrBkJgSZ_kFEs2ddYIVKE4bglASlBbSizC8CASdJlyDD3T_dyimA1r2bwSfsHTyrcG_SpoU5Ee9KS-Lr2PCQ3LmTc8_nhaeBGtZCO4B8oZI9bpD6zqms1Zr-ymaE0pYnnQ3aWOclhiLavVudKxLxZvYXTdMStjyNbwBXekVVOnAZuCTuXMsD_jah7_MkmJP_buJgq3u6TthctsORHp4pKuZeI_43Y728-Qg7mIDeL5_-j_vgXdu7FWVa0OSTjZJM27GCDzr2M8LAhApk4aeDoF1Cmw

MDOC-CBOR
=========

The PID/(Q)EAA MDOC-CBOR data model is defined in ISO/IEC 18013-5, the standard born for the the mobile driving license (mDL) use case. 

The MDOC data elements MUST be encoded as defined in `RFC 8949 - Concise Binary Object Representation (CBOR) <RFC 8949 - Concise Binary Object Representation (CBOR)>`_.

The PID MDOC-CBOR document type uses the namespace `eu.europa.ec.eudiw.pid.1`, according to the reverse domain approach defined in the 
`EIDAS-ARF`_ and in fully harmonization with the ISO/IEC 18013-5 standard.

The the data elements contained in the document, use the same namespace for the required PID attributes, while the national PID attributes use the domestic namespace `eu.europa.ec.eudiw.pid.it.1`, defined in this implementation profile.

According to ISO/IEC 18013-5, the structure of mdoc response that is encoded in CBOR MUST be as the following:

.. list-table:: 
    :widths: 20 20 60
    :header-rows: 1

    * - **Attribute name**
      - **Description**
      - **Reference**
    * - **version**
      - *tstr (text string)*. Version of the PID/(Q)EAA structures. For example, ``"version":"1.0"`` means that this is the first version of PID/(Q)EAA ISO-compliant attestation.
      - [ISO 18013-5#8.3.2.1.2]
    * - **status**
      - *uint (unsigned int)*. Status code. For example ``"status":0`` means OK (normal processing).
      - [ISO 18013-5#8.3.2.1.2.3]
    * - **documents**
      - Returned documents. For example, PID/(Q)EAA.
      - [ISO 18013-5#8.3.2.1.2]

The ``documents`` object contains the Digital Credential and it MUST have the following structure:

.. list-table:: 
    :widths: 20 20 60
    :header-rows: 1

    * - **Attribute name**
      - **Description**
      - **Reference**
    * - **docType**
      - *tstr (text string)*. Document type returned. For example for the PID, the value MUST be ``eu.europa.ec.eudiw.pid.1.`` For an mDL, the value MUST be ``org.iso.18013-5.1.mDL``.
      - [ISO 18013-5#8.3.2.1.2]
    * - **issuerSigned**
      - *bstr (byte string)*. Returned data elements signed by the Issuer.
      - [ISO 18013-5#8.3.2.1.2]

The ``issuerSigned`` object MUST have the following structure:

.. list-table:: 
    :widths: 20 20 60
    :header-rows: 1

    * - **Attribute name**
      - **Description**
      - **Reference**
    * - **nameSpaces** 
      - *bstr (byte string)* with *tag* 24 and *major type* 6. Returned data elements for the namespaces. It MAY be possible to have one or more namespaces. The nameSpaces MUST use the same value for the document type. However, it MAY have a domestic namespace to include attributes defined in this implementation profile. In this case, it MUST append the applicable *ISO 3166-1 alpha-2 country code*. For example, in the case of Italy, the value MUST be: ``eu.europa.ec.eudiw.pid.it.1``
      - [ISO 18013-5#8.3.2.1.2]
    * - **issuerAuth**
      - *bstr (byte string)*. Contains *Mobile Security Object* (MSO) for issuer data authentication
      - [ISO 18013-5#9.1.2.4]

During the presentation of a credential in mDOC-CBOR format, in addition to the objects in the table above, a ``deviceSigner`` object MUST also be added and MUST NOT be present in the issued credential provided by a PID/(Q)EAA Issuer.

.. list-table:: 
    :widths: 20 20 60
    :header-rows: 1

    * - **Attribute name**
      - **Description**
      - **Reference**
    * - **deviceSigned**
      - *bstr (byte string)*. Data elements signed by the Wallet Instance during the presentation phase.
      - [ISO 18013-5#8.3.2.1.2]

Where the ``deviceSigned`` MUST have the following structure:

.. list-table:: 
    :widths: 20 20 60
    :header-rows: 1

    * - **Attribute name**
      - **Description**
      - **Reference**
    * - **nameSpaces**
      - *tstr (text string)*. It MUST be an empty structure.
      - [ISO 18013-5#8.3.2.1.2], PID Rule Book
    * - **deviceAuth**
      - *bstr (byte string)*. Contains the device authentication for mDoc data authentication
      - [ISO 18013-5#8.3.2.1.2]


.. note::
  
  A ``deviceSigned`` object given during the presentation phase has two purposes:

    1. Provide Optional self-attested claims in the ``nameSpaces`` object. Even if no self-attested claims are provided by the Wallet Instance, the ``nameSpaces`` object MUST be included with an empty structure.
    2. Provide a cryptographic proof that the Holder is the legitimate owner of the Credential by means of a ``deviceAuth`` object. 


.. note::

    The ``issuerSigned`` and the ``deviceSigned`` objects contain the ``nameSpaces`` object and the *Mobile Security Object*. The latter is the only signed object, while the ``nameSpaces`` object is not signed.



nameSpaces
----------

The `nameSpaces` object contains one or more *IssuerSignedItemBytes* that are encoded using CBOR bitsring 24 tag (#6.24(bstr .cbor), Marked with 24(<<... >>) in the example), representing the disclosure information for each digest within the `Mobile Security Object`. It MUST contain  the following attributes:

.. list-table:: 
    :widths: 20 20 60
    :header-rows: 1

    * - **Name**
      - **Encoding**
      - **Description**
    * - **digestID**
      - integer
      - This value is a reference to the equivalent hash value within ``ValueDigests`` in the *Mobile Security Object*.
    * - **random**
      - bstr (byte string)
      - Random byte value used as salt for the hash function. This value shall be different for each *IssuerSignedItem* and shall have a minimum length of 16 bytes.
    * - **elementIdentifier**
      - tstr (text string)
      - Data element identifier.
    * - **elementValue**
      - depends by the value, see the next table.
      - Data element value.

The `elementIdentifier` data that MUST be included in a PID/(Q)EAA are: 

.. list-table:: 
    :widths: 20 20 20
    :header-rows: 1

    * - **Namespace**
      - **Element identifier**
      - **Description**
    * - **eu.europa.ec.eudiw.pid.1**
      - **issuance_date**
      - full-date (CBORTag 1004). Date when the PID/(Q)EAA was issued.
    * - **eu.europa.ec.eudiw.pid.1**
      - **expiry_date**
      - full-date (CBORTag 1004). Date when the PID/(Q)EAA will expire.
    * - **eu.europa.ec.eudiw.pid.1**
      - **issuing_authority**
      - tstr (text string). Name of administrative authority that has issued the PID/(Q)EAA.
    * - **eu.europa.ec.eudiw.pid.1**
      - **issuing_country**
      - tstr (text string). Alpha-2 country code as defined in [ISO 3166]


Depending on the Digital Credential type, additional `elementIdentifier` data MAY be added. For the PID it MUST support the following data:

.. list-table:: 
    :widths: 20 20 20
    :header-rows: 1

    * - **eu.europa.ec.eudiw.pid.1**
      - **given_name**
      - tstr (text string).
    * - **eu.europa.ec.eudiw.pid.1**      
      - **family_name**
      - tstr (text string).
    * - **eu.europa.ec.eudiw.pid.1**
      - **birth_date**
      - full-date (CBORTag 1004).
    * - **eu.europa.ec.eudiw.pid.1**
      - **birth_place**
      - tstr (text string).
    * - **eu.europa.ec.eudiw.pid.1**
      - **birth_country**
      - tstr (text string).
    * - **eu.europa.ec.eudiw.pid.1**
      - **unique_id**
      - tstr (text string).
    * - **eu.europa.ec.eudiw.pid.it.1**
      - **tax_id_code**
      - tstr (text string).


Mobile Security Object
----------------------

The `issuerAuth` MUST contain a `Mobile Security Object` which is an untagged value containing a `COSE Sign1 Document`, as defined in `RFC 9052 - CBOR Object Signing and Encryption (COSE): Structures and Process <https://www.rfc-editor.org/rfc/rfc9052.html>`_. It MUST be composed by:

* protected header
* unprotected header
* payload
* signature.

The protected header MUST contain the following parameter encoded in CBOR format:

.. list-table:: 
    :widths: 20 20 60
    :header-rows: 1

    * - **Element**
      - **Description**
      - **Reference**
    * - **Signature algorithm**
      - `-7` means ES256, SHA-256. 
      - RFC8152

.. note::
    Only the Signature Algorithm MUST be present in the protected headers, other elements SHOULD not be present in the protected header.


The unprotected header MUST contain the following parameter:

.. list-table:: 
    :widths: 20 20 60
    :header-rows: 1

    * - **Element**
      - **Description**
      - **Reference**
    * - **x5chain**
      - Identified with the label 33
      - `RFC 9360 CBOR Object Signing and Encryption (COSE) - Header Parameters for Carrying and Referencing X.509 Certificates <RFC 9360 CBOR Object Signing and Encryption (COSE) - Header Parameters for Carrying and Referencing X.509 Certificates>`_.

.. note::
    The `x5chain` is included in the unprotected header with the aim to make the Holder able to update the X.509 certificate chain, related to the `Mobile Security Object` issuer, without breaking the signature.

The payload must contain the following parameter:

.. list-table:: 
    :widths: 20 20 60
    :header-rows: 1

    * - **Element**
      - **Encoding**
      - **Description**
    * - **MobileSecurityObjectBytes**
      - CBORTag(24) 
      - object, without any `content-type` definition, containing the following attributes:

        * version
        * digestAlgorithm
        * valueDigests
        * deviceKeyInfo



