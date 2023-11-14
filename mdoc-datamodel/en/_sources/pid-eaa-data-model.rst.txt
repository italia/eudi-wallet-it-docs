
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

The (Q)EAAs are issued by (Q)EAA Issuers to a Wallet Instance and MUST be provided in SD-JWT-VC or MDOC-CBOR data format. 

The (Q)EAAs are extended according to `OpenID Identity Assurance Profile [OIDC.IDA] <https://openid.net/specs/openid-connect-4-identity-assurance-1_0-13.html>`_, that allows the recipients to know the Authentic Sources where the data comes from. 

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

.. _sec-pid-eaa-verification-field:

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
      - **birth_place**
      - *tstr (text string)*. See :ref:`PID Claims fields Section <sec-pid-user-claims>`.
    * - **eu.europa.ec.eudiw.pid.1**
      - **birth_country**
      - *tstr (text string)*. See :ref:`PID Claims fields Section <sec-pid-user-claims>`.
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
    
  A366737461747573006776657273696F6E63312E3069646F63756D656E747381A267646F6354797065781865752E6575726F70612E65632E65756469772E7069642E316C6973737565725369676E6564A26A697373756572417574688443A10126A1182159021930820215308201BCA003020102021404AD06A30C1A6DC6E93BE0E2E8F78DCAFA7907C2300A06082A8648CE3D040302305B310B3009060355040613025A45312E302C060355040A0C25465053204D6F62696C69747920616E64205472616E73706F7274206F66205A65746F706961311C301A06035504030C1349414341205A65746573436F6E666964656E73301E170D3231303932393033333034355A170D3232313130333033333034345A3050311A301806035504030C114453205A65746573436F6E666964656E7331253023060355040A0C1C5A65746F70696120436974792044657074206F662054726166666963310B3009060355040613025A453059301306072A8648CE3D020106082A8648CE3D030107034200047C5545E9A0B15F4FF3CE5015121E8AD3257C28D541C1CD0D604FC9D1E352CCC38ADEF5F7902D44B7A6FC1F99F06EEDF7B0018FD9DA716AEC2F1FFAC173356C7DA3693067301F0603551D23041830168014BBA2A53201700D3C97542EF42889556D15B7AC4630150603551D250101FF040B3009060728818C5D050102301D0603551D0E04160414CE5FD758A8E88563E625CF056BFE9F692F4296FD300E0603551D0F0101FF040403020780300A06082A8648CE3D0403020347003044022012B06A3813FFEC5679F3B8CDDB51EAA4B95B0CBB1786B09405E2000E9C46618C02202C1F778AD252285ED05D9B55469F1CB78D773671F30FE7AB815371942328317C59032AD818590325A667646F6354797065781865752E6575726F70612E65632E65756469772E7069642E316776657273696F6E63312E306C76616C6964697479496E666FA3667369676E6564C074323032332D30322D32325430363A32333A35365A6976616C696446726F6DC074323032332D30322D32325430363A32333A35365A6A76616C6964556E74696CC074323032342D30322D32325430303A30303A30305A6C76616C756544696765737473A2781865752E6575726F70612E65632E65756469772E7069642E31AC015820A7FFC6F8BF1ED76651C14756A061D662F580FF4DE43B49FA82D80A4B80F8434A025820CD372FB85148700FA88095E3492D3F9F5BEB43E555E5FF26D95F5A6ADC36F8E6035820E67E72111B363D80C8124D28193926000980E1211C7986CACBD26AACC5528D48045820F7D062D662826ED95869851DB06BB539B402047BAEE53A00E0AA35BFBE98265D0658202A132DBFE4784627B86AA3807CD19CFEFF487AAB3DD7A60D0AB119A72E736936075820BDCA9E8DBCA354E824E67BFE1533FA4A238B9EA832F23FB4271EBEB3A5A8F7200858202C0EAEC2F05B6C7FE7982683E3773B5D8D7A01E33D04DFCB162ADD8BD99BEE9A095820BFE220D85657CCEC3C67E7DB1DF747E9148A152334BB6D4B65B273279BCC36EC0A582018E38144F5044301D6A0B4EC9D5F98D4CD950E6EA2C29B849CBD457DA29B6AD30B58203C71D2F0EFA09D9E3FBBDFFD29204F6B292C9F79570AEF72DD86C91F7A3AA5C50C582065743D58D89D45E52044758F546034FD13A4F994BC270CDFA7844F74EB3F4B6E0D5820B4A8EB5D523BFFA17B41BDA12DDC7DA32AE1E5F7FF3DCC394A35401F16919BBF781B65752E6575726F70612E65632E65756469772E7069642E69742E31A10E58209D6C11644651126C94ACDAF0803E86D4C71D15D3B2712A14295416734EFD514D6D6465766963654B6579496E666FA1696465766963654B6579A401022001215820BA01AEA44EEE1E338EB2F04E279DBD51B34655783EE185150838C9A7A7C4DB7122582025BA0044439A3871A7B975A0994A85E79B705A9AC263B3FE899B0A93412EE8C96F646967657374416C676F726974686D675348412D32353658400813C28FD62F2602CBC14724E5865733C44A0FCA589B55C085EC9D5C725D6CCE25BA0044439A3871A7B975A0994A85E79B705A9AC263B3FE899B0A93412EE8C96A6E616D65537061636573A2781865752E6575726F70612E65632E65756469772E7069642E318DD818586DA4686469676573744944016672616E646F6D5820156DF9227AD341EAA61AABD301106FD21BDC18820E01DFC16BCF5FECC447111B71656C656D656E744964656E7469666965726B6578706972795F646174656C656C656D656E7456616C7565D903EC6A323032342D30322D3232D818586FA4686469676573744944026672616E646F6D5820A3A1F13F05544D03A5B50B5FDB78465808393BCF3B7953A345FE28F820C7BE0D71656C656D656E744964656E7469666965726D69737375616E63655F646174656C656C656D656E7456616C7565D903EC6A323032332D30322D3232D8185866A4686469676573744944036672616E646F6D5820852591F90F2C9DED57A03632E2C1322AB52A082A431E71A4149A6830C8F1AD0C71656C656D656E744964656E7469666965726F69737375696E675F636F756E7472796C656C656D656E7456616C7565624954D818587CA4686469676573744944046672616E646F6D5820D1D587B3512ACCE15C4F6B20944CEB002A464E4A158389788563408873C3FCE571656C656D656E744964656E7469666965727169737375696E675F617574686F726974796C656C656D656E7456616C7565764D696E69737465726F2064656C6C27496E7465726E6FD8185864A4686469676573744944056672616E646F6D582094FDD7609C0E73DC8589B5CAB11E1D9058CF8BFF8A336DA5F81FCBA055396A0F71656C656D656E744964656E7469666965726A676976656E5F6E616D656C656C656D656E7456616C7565654D6172696FD8185865A4686469676573744944066672616E646F6D5820660C0A7BF79E0E0261CA1547A4294FB808AA70738F424B13AB1B9440B566AE1371656C656D656E744964656E7469666965726B66616D696C795F6E616D656C656C656D656E7456616C756565526F737369D818586BA4686469676573744944076672616E646F6D5820315C53491286488FA07F5C2CE67135EF5C9959C3469C99A14E9B6DC924F9EBA571656C656D656E744964656E746966696572696269727468646174656C656C656D656E7456616C7565D903EC6A313935362D30312D3132D818587AA4686469676573744944086672616E646F6D582081C5CC04FBDF78E0F84DF72FDB87028ADE08E66DC5F31084826EBAD7AE70D84671656C656D656E744964656E7469666965726B62697274685F706C6163656C656C656D656E7456616C756581A267636F756E747279624954686C6F63616C69747964526F6D65D818587DA4686469676573744944096672616E646F6D5820764EF39C9D01F3AA6A87F441603CFE853FBA3CEE3BC2C168BCC9E96271D6E06371656C656D656E744964656E74696669657269756E697175655F69646C656C656D656E7456616C7565781E78787878787878782D7878782D787878782D787878787878787878787878D81858E8A46864696765737449440A6672616E646F6D5820AD20B3B9C67AED8089FF33ECDC108781C3B49B81CD7A3F059D2FE236977037B271656C656D656E744964656E74696669657275766572696669636174696F6E2E65766964656E63656C656C656D656E7456616C756581A2647479706571656C656374726F6E69635F7265636F7264667265636F7264A264747970656C65696461732E69742E63696566736F75726365A3716F7267616E697A6174696F6E5F6E616D656C65696461732E69742E6369656F6F7267616E697A6174696F6E5F6964646D5F69746C636F756E7472795F636F6465626974D8185879A46864696765737449440B6672616E646F6D5820C12314B3695D1401505187E2113115E2F7B4A14B135DEE320F5E6DF81275F17671656C656D656E744964656E746966696572667374617475736C656C656D656E7456616C7565781D68747470733A2F2F70696470726F76696465722E69742F737461747573D8185877A46864696765737449440C6672616E646F6D5820A7B6A9027ED97F25DF96DD0EAB8093B264A3BD6A1D5B24228F3FC5B18EF835FB71656C656D656E744964656E746966696572781C766572696669636174696F6E2E74727573745F6672616D65776F726B6C656C656D656E7456616C7565656569646173D8185876A46864696765737449440D6672616E646F6D5820C76CE2AE4E9BE1DB07A5CB397B54ACE3ECCC786D3F85E4348B923DEE059783DB71656C656D656E744964656E746966696572781C766572696669636174696F6E2E6173737572616E63655F6C6576656C6C656C656D656E7456616C75656468696768781B65752E6575726F70612E65632E65756469772E7069642E69742E3181D8185877A46864696765737449440E6672616E646F6D5820717DF3F583B1484366C33A1F869F2B5D201D466A8B589C79AB1A2D85E595432571656C656D656E744964656E7469666965726D7461785F69645F6E756D6265726C656C656D656E7456616C75657554494E49542D585858585858585858585858585858

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
                          8: h'EAD5E8B5E543BD31F3BE57DE4ED45…',                 
                          9: h'DEFDF1AA746718016EF1B94BFE5R6…'
                      },
                      "eu.europa.ec.eudiw.pid.it.1": {  
                          10: h'AFC5A127BE44753172844B13491D8…',
                          11: h'AFC5A127BE44753172844B13492H4…',
                          12: h'DJA5A127BE44753172844B13492H4…',
                          13: h'KDL5A127BE44753172844B13492H4…',
                          14: h'F9EE4D36F67DBD75E23311AC1C29…'
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
                  "elementIdentifier": "birthdate",
                  "elementValue": 1004("1956-01-12")% the tag 1004 defines the value    
                                                      is a full date 
                  }  
              >>), 
              24(<<  
                  {                               
                  "digestID": 8, 
                  "random": h'CAD1F6A38F603451F1FA653F81FF309D',
                  "elementIdentifier": "birth_place",
                  "elementValue": [
                      {  
                          "country": "IT" , 
                          "locality": "Rome"
                      }      
                  ]  
                  }                       
              >>),           
              24(<<  
                  {                              
                  "digestID": 9,                              
                  "random": h'53C15C57B3B076E788795829190220B4',
                  "elementIdentifier": "unique_id",
                  "elementValue": "xxxxxxxx-xxx-xxxx-xxxxxxxxxxxx" 
                  }   
              >>)
              ],
              "eu.europa.ec.eudiw.pid.it.1": [
                  24(<<  
                      {                               
                      "digestID": 10, 
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
                      "digestID": 11,                                  
                      "random": h'CAD1F6A38F603451F1FA653F81FF309D,                                 
                      "elementIdentifier": "status",                                
                      "elementValue": "https://pidprovider.example.it/status"                            
                      }                         
                  >>),
                  24(<<  
                      {                               
                      "digestID": 12, 
                      "random": h'564E3C65D46D06FEDEB0E7293A86GF',
                      "elementIdentifier": "verification.trust_framework",
                      "elementValue": "eidas" 
                      }                       
                  >>),
                  24(<<  
                      {                               
                      "digestID": 13, 
                      "random": h'D884E5D5EF4CFC93FDB1E4EE8F3923',
                      "elementIdentifier": "verification.assurance_level",
                      "elementValue": "high" 
                      }                       
                  >>)  
                  24(<<
                      {
                      "digestID": 14, 
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



