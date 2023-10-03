.. include:: ../common/common_definitions.rst

.. _wallet-instance-attestation.rst:

Wallet Instance Attestation
+++++++++++++++++++++++++++

The Wallet Instance Attestation containing details about the Wallet Instance and the device's security level where the Wallet Instance is installed. It generally attests the **authenticity**, **integrity**, **security**, **privacy**, and **trust** of a specific Wallet Instance. The Wallet Instance Attestation MUST contain a Wallet Instance public key.

General Properties
------------------

The Wallet Instance Attestation:

- MUST be issued and MUST be signed by Wallet Provider;
- MUST give all the relevant information to attests the **integrity** and **security** of the device where the Wallet Instance is installed.

It is necessary for each Wallet Instance to obtain an the Wallet Instance Attestation before entering the Operational state.

Requirements
------------

The following requirements for the Wallet Instance Attestation are met:

1. The Wallet Instance Attestation MUST use a signed JSON Web Token (JWT) format.
2. The Wallet Provider MUST offer a RESTful set of services for issuing the Wallet Instance Attestations.
3. The Wallet Instance Attestation MUST be securely bound to the Wallet Instance public key (**Holder Key Binding**).
4. The Wallet Instance Attestation MUST be issued and signed by an accredited and reliable Wallet Provider, thereby providing integrity and authenticity to the attestation.
5. The Wallet Instance Attestation MUST ensure the integrity and authenticity of the Wallet Instance, verifying that it was accurately created and provided by the Wallet Provider.
6. Each Wallet Instance SHOULD be able to request multiple attestations for different public keys associated with it. This requirement provides a privacy-preserving measure, as the public key MAY be used as a tracking tool during the presentation phase (see alos the point number 10, listed below).
7. The Wallet Instance Attestation SHOULD be usable multiple times during its validity period, allowing for repeated authentication and authorization without the need to request new attestations with each interaction.
8. The Wallet Instance Attestation SHOULD have an expiration date time, after which it will no longer be considered valid.
9. When the private key associated with the Wallet Instance is lost or deleted, the attestation MUST become invalid to prevent unauthorized use of the Wallet Instance.


High-level Design
-----------------

Static Component View
~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../images/static_view_wallet_instance_attestation.svg
   :name: Wallet Solution Schema
   :alt: The image illustrates the containment of Wallet Provider and Wallet Instances within the Wallet Solution, managed by the Wallet Provider.
   :target: https://www.plantuml.com/plantuml/uml/XP4nJuSm44VtVehBdxbnPp2iRYx6qTHIjR7SaVQ0-EqzaICDgN4ZBxpqzTUXiCkyJCaupvJXzbH2le4hiCW7A7rsAGM6ETCQn-E7RMSloi0OJzDC691FeL1QE1BMWZBeraW2Mbv4wK8VQayPT5yX9TgCQPclpdy676lnGF0ZN93DyVs3xVsrhOU70hCi0_JshwHXFJp-Rg4dIuECo96moD7xeBQbUKBEbE0EPEwuEWx6N2zj_uXqU8wbhVMhD3tjbAX1BYIl_mq0

Dynamic Component View
~~~~~~~~~~~~~~~~~~~~~~

This section describes the Wallet Instance Attestation format and how the Wallet Provider issues it.

.. figure:: ../../images/dynamic_view_sequence_wallet_instance_attestation.svg
   :name: Sequence Diagram for Wallet Instance Attestation Request
   :alt: The figure illustrates the sequence diagram for issuing a Wallet Instance Attestation, with the steps explained below.
   :target: https://www.plantuml.com/plantuml/ZP91RzH038NlyojCJwr4n7qFgrOSAf2G409wwSL9h60ryGmUpqRRNuyt6qBJe5MlzlFtx3TpcmtLoj27Tqcn6n2CuZEO5WfOB4ePQj8GagkuuOHYSFKZaru1PYZh-WFsFHby4eTAGvDavFzglceyS3jZndgjkKi9q8mSOnm5tEx0Cy_h8HIezaxUkHKROy_F1A_C7oKgAFqkJlcGb38vkL5gIKuJEOnSxSTw1_S-z6ef6CYmHSCmrfMhtEZBN84cYY4BI_U21dPCbD_34nqdJrOQlECLaZP55flzdFJJrtKIRKnDIpQN_RtjdeJKXHCr8MkUcsYsWs_dqq2Y7nky1DLvRguiVX-Lq3RnmDs_V1VMvuVl0HlZmsbWh5SHuGlzzHjWDwVizZwrlNWPwqWA2mdb3DVJsZUdIwh9rML6dR8TeVb5pHCevTAROy_jXPgv4xIYjBIMv53QgNtf-kMDBuishtT1tD8wHUUNBPwNlzi-YXAsHx08iJPa0Q5nzLjlITeoz7y0

- **Message 1**: The User starts the Wallet Instance mobile app and gets authenticated in it, a new Wallet Instance Attestation is automatically obtained if the previous one results expired.
- **Message 2-3**: The Wallet Instance retrieves the Wallet Provider metadata, including the list of supported algorithms, public keys, and endpoints.
- **Message 4**: The Wallet Instance verifies the Wallet Provider's trustworthiness by evaluating its Trust Chain.
- **Message 5**: The Wallet Instance generates a new key pair.
- **Message 6-7**: The Wallet Instance requests a ``nonce`` from the App Attestation Service.
- **Message 8**: The Wallet Instance creates a Wallet Instance Attestation Request in JWS format, signed with the private key associated with the public key for which it request the attestation.
- **Message 9-13**: The Wallet Instance provides the Wallet Instance Attestation Request to the Wallet Provider, which validates it and issues a signed attestation to the Wallet Instance.
- **Message 13-14**: The Wallet Instance receives the Wallet Instance Attestation signed by the Wallet Provider and performs security and integrity verifications.
- **Message 15**: The Wallet Instance Attestation is now ready for use.

Detailed Design
---------------

The detailed design is explained below.

Wallet Instance Attestation Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To obtain a Wallet Instance Attestation from the Wallet
Provider it is necessary to send a Wallet Instance Attestation
Request from the Wallet Instance containing the associated public key
, the ``nonce`` value previously requested and a ``jti`` value.

The Wallet Instance MUST do an HTTP request to the Wallet Provider `token endpoint`_,
using the method `POST <https://datatracker.ietf.org/doc/html/rfc6749#section-3.2>`__.

The **token** endpoint (as defined in `RFC 7523 section 4`_) requires the following parameters
encoded in ``application/x-www-form-urlencoded`` format:

* ``grant_type`` set to ``urn:ietf:params:oauth:grant-type:jwt-bearer``;
* ``assertion`` containing the signed JWT defined in the Section `Wallet Instance Attestation Request`_.

Below a non-normative example of the HTTP request.

.. code-block:: http

    POST /token HTTP/1.1
    Host: wallet-provider.example.org
    Content-Type: application/x-www-form-urlencoded

    grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer
    &assertion=eyJhbGciOiJFUzI1NiIsImtpZCI6ImtoakZWTE9nRjNHeGRxd2xVTl9LWl83NTVUT1ZEbmJIaDg2TW1KcHh2a1UifQ.eyJpc3MiOiAidmJlWEprc000NXhwaHRBTm5DaUc2bUN5dVU0amZHTnpvcEd1S3ZvZ2c5YyIsICJhdWQiOiAiaHR0cHM6Ly93YWxsZXQtcHJvdmlkZXIuZXhhbXBsZS5vcmciLCAianRpIjogImY1NjUyMDcyLWFiZWYtNDU5OS1iODYzLTlhNjkwNjA3MzJjYyIsICJub25jZSI6ICIuLi4uLiIsICJjbmYiOiB7Imp3ayI6IHsiY3J2IjogIlAtMjU2IiwgImt0eSI6ICJFQyIsICJ4IjogIjRITnB0SS14cjJwanlSSktHTW56NFdtZG5RRF91SlNxNFI5NU5qOThiNDQiLCAieSI6ICJMSVpuU0IzOXZGSmhZZ1MzazdqWEU0cjMtQ29HRlF3WnRQQklScXBObHJnIiwgImtpZCI6ICJ2YmVYSmtzTTQ1eHBodEFObkNpRzZtQ3l1VTRqZkdOem9wR3VLdm9nZzljIn19LCAiaWF0IjogMTY5MTQ4ODk2MiwgImV4cCI6IDE2OTE0OTYxNjJ9.Dg_yFaiv6lVftR3FFx0v5JW250mBgXLVP1j0ezZcHRyitqSY7xGmx4y-MGur93FAS85vf_Da-L-REVEltwU2Jw

The response is the `Wallet Instance Attestation`_ in JWT format:

.. code-block:: http

    HTTP/1.1 201 OK
    Content-Type: application/jwt

    eyJhbGciOiJFUzI1NiIsInR5cCI6IndhbGxldC1hdHRlc3RhdGlvbitqd3QiLCJraWQiOiI1dDVZWXBCaE4tRWdJRUVJNWlVenI2cjBNUjAyTG5WUTBPbWVrbU5LY2pZIiwidHJ1c3RfY2hhaW4iOlsiZXlKaGJHY2lPaUpGVXouLi42UzBBIiwiZXlKaGJHY2lPaUpGVXouLi5qSkxBIiwiZXlKaGJHY2lPaUpGVXouLi5IOWd3Il19.eyJpc3MiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZyIsInN1YiI6InZiZVhKa3NNNDV4cGh0QU5uQ2lHNm1DeXVVNGpmR056b3BHdUt2b2dnOWMiLCJ0eXBlIjoiV2FsbGV0SW5zdGFuY2VBdHRlc3RhdGlvbiIsInBvbGljeV91cmkiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZy9wcml2YWN5X3BvbGljeSIsInRvc191cmkiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZy9pbmZvX3BvbGljeSIsImxvZ29fdXJpIjoiaHR0cHM6Ly93YWxsZXQtcHJvdmlkZXIuZXhhbXBsZS5vcmcvbG9nby5zdmciLCJhdHRlc3RlZF9zZWN1cml0eV9jb250ZXh0IjoiaHR0cHM6Ly93YWxsZXQtcHJvdmlkZXIuZXhhbXBsZS5vcmcvTG9BL2Jhc2ljIiwiY25mIjp7Imp3ayI6eyJjcnYiOiJQLTI1NiIsImt0eSI6IkVDIiwieCI6IjRITnB0SS14cjJwanlSSktHTW56NFdtZG5RRF91SlNxNFI5NU5qOThiNDQiLCJ5IjoiTElablNCMzl2RkpoWWdTM2s3alhFNHIzLUNvR0ZRd1p0UEJJUnFwTmxyZyIsImtpZCI6InZiZVhKa3NNNDV4cGh0QU5uQ2lHNm1DeXVVNGpmR056b3BHdUt2b2dnOWMifX0sImF1dGhvcml6YXRpb25fZW5kcG9pbnQiOiJldWRpdzoiLCJyZXNwb25zZV90eXBlc19zdXBwb3J0ZWQiOlsidnBfdG9rZW4iXSwidnBfZm9ybWF0c19zdXBwb3J0ZWQiOnsiand0X3ZwX2pzb24iOnsiYWxnX3ZhbHVlc19zdXBwb3J0ZWQiOlsiRVMyNTYiXX0sImp3dF92Y19qc29uIjp7ImFsZ192YWx1ZXNfc3VwcG9ydGVkIjpbIkVTMjU2Il19fSwicmVxdWVzdF9vYmplY3Rfc2lnbmluZ19hbGdfdmFsdWVzX3N1cHBvcnRlZCI6WyJFUzI1NiJdLCJwcmVzZW50YXRpb25fZGVmaW5pdGlvbl91cmlfc3VwcG9ydGVkIjpmYWxzZSwiaWF0IjoxNjg3MjgxMTk1LCJleHAiOjE2ODcyODgzOTV9.tNvCyFPCL5tUi2NakKwdaG9xbrtWWl4djSRYRfHrF8NdmffdT044U55pRn35J2cl0LZxbesEDrfSAz2pllw2Ug


Below are described the JWT headers and the payload claims
of the `assertion` used in the request.


Assertion Header
^^^^^^^^^^^^^^^^
+-----------------------------------+-----------------------------------+
| **key**                           | **value**                         |
+-----------------------------------+-----------------------------------+
| alg                               | Algorithm to verify the token     |
|                                   | signature (es. ES256).            |
+-----------------------------------+-----------------------------------+
| kid                               | Key id of the public key          |
|                                   | created by the Wallet Instance.   |
+-----------------------------------+-----------------------------------+
| typ                               | Media type, set to                |
|                                   | ``wiar+jwt``.                     |
+-----------------------------------+-----------------------------------+

Assertion Payload
^^^^^^^^^^^^^^^^^

+--------+-------------------------------------------------------------+
| **key**| **value**                                                   |
+--------+-------------------------------------------------------------+
|| iss   || Thumbprint value                                           |
||       || of the JWK of the Wallet Instance                          |
||       || for which the attestation is                               |
||       || being requested.                                           |
+--------+-------------------------------------------------------------+
|| aud   || The public url of the Wallet                               |
||       || Provider.                                                  |
+--------+-------------------------------------------------------------+
|| jti   || Unique identifier of the request, according to             |
||       || `RFC7519 <https://datatracker.ietf.org/doc/html/rfc7519>`_.|
||       ||                                                            |
+--------+-------------------------------------------------------------+
|| nonce || The nonce value obtained from the                          |
||       || App Attestation Service.                                   |
+--------+-------------------------------------------------------------+
|| cnf   || JSON object, according to                                  |
||       || `RFC7800 <https://www.rfc-editor.org/rfc/rfc7800.html>`_   |
||       || containing the public key of the                           |
||       || Wallet Instance.                                           |
+--------+-------------------------------------------------------------+


Below a non-normative example of the Wallet Instance Attestation
request where the decoded JWS headers and payload are separated by a comma:

.. code-block:: javascript

  {
    "alg": "ES256",
    "kid": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "typ": "wiar+jwt"
  }
  .
  {
    "iss": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "aud": "https://wallet-provider.example.org",
    "jti": "6ec69324-60a8-4e5b-a697-a766d85790ea",
    "nonce" : ".....",
    "cnf": {
      "jwk": {
        "crv": "P-256",
        "kty": "EC",
        "x": "4HNptI-xr2pjyRJKGMnz4WmdnQD_uJSq4R95Nj98b44",
        "y": "LIZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg",
        "kid": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"
      }
    },
    "iat": 1686645115,
    "exp": 1686652315
  }

Whose corresponding JWS is verifiable using the public key
of the Wallet Provider corresponding to the `kid` made available
in the header.


Wallet Instance Attestation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Wallet Instance Attestation MUST be provisioned in JWT format, whose
headers and payload claims are listed below.

Header
^^^^^^

+-----------------------------------+-----------------------------------+
| **key**                           | **value**                         |
+-----------------------------------+-----------------------------------+
| alg                               | Algorithm to verify the token     |
|                                   | signature (es. ES256).            |
+-----------------------------------+-----------------------------------+
| kid                               | Key id used by the Wallet         |
|                                   | Provider to sign the attestation. |
+-----------------------------------+-----------------------------------+
| typ                               | Media type, set to                |
|                                   | `wallet-attestation+jwt`,         |
|                                   | according to                      |
|                                   | [`OPENID4VC-HAIP`_]               |
+-----------------------------------+-----------------------------------+
| x5c                               | Array containing the X.509        |
|                                   | chain                             |
|                                   | of certificates used to attest    |
|                                   | the public key of the Wallet      |
|                                   | Provider.                         |
+-----------------------------------+-----------------------------------+
| trust_chain                       | Array containing the Federation   |
|                                   | Trust Chain relating to the       |
|                                   | Wallet Provider.                  |
+-----------------------------------+-----------------------------------+

.. note::

   The claim `trust_chain` or the claim `x5c` MUST be provisioned.
   If these are both provisioned, the related public key contained in
   MUST be the same in both `trust_chain` and `x5c`.

Payload
^^^^^^^

+---------------------------+------------------------------------------------+
| **key**                   | **value**                                      |
+---------------------------+------------------------------------------------+
|| iss                      || The public url of the Wallet Provider         |
+---------------------------+------------------------------------------------+
|| sub                      || Thumbprint value                              |
||                          || of the JWK of the Wallet Instance             |
||                          || for which the attestation is                  |
||                          || being issued.                                 |
+---------------------------+------------------------------------------------+
|| iat                      || Unix timestamp of attestation                 |
||                          || issuance time.                                |
+---------------------------+------------------------------------------------+
|| exp                      || Unix timestamp regarding the                  |
||                          || expiration date time.                         |
||                          || A good practice to avoid security             |
||                          || problems is to have a limited                 |
||                          || duration of the attestation.                  |
+---------------------------+------------------------------------------------+
|| attested_security_context|| Attested security context:                    |
||                          || Represents the level of "security"            |
||                          || attested by the Wallet Provider.              |
+---------------------------+------------------------------------------------+
|| cnf                      || This parameter contains the ``jwk``           |
||                          || parameter                                     |
||                          || with the public key of the Wallet Instance    |
||                          || necessary for the Holder Key Binding.         |
+---------------------------+------------------------------------------------+
|| authorization_endpoint   || URL of the SIOPv2                             |
||                          || Authorization Endpoint.                       |
+---------------------------+------------------------------------------------+
|| response_types_supported || JSON array containing a list of               |
||                          || the OAuth 2.0 ``response_type`` values.       |
+---------------------------+------------------------------------------------+
|| response_modes_supported || JSON array containing a list of the OAuth 2.0 |
||                          || "response_mode" values that this              |
||                          || authorization server supports.                |
||                          || `RFC 8414 <https://www.rfc-editor.org/rfc/    |
||                          || rfc8414.html>`_                               |
+---------------------------+------------------------------------------------+
|| vp_formats_supported     || JSON object containing                        |
||                          || ``jwt_vp_json`` and ``jwt_vc_json``           |
||                          || supported algorithms array.                   |
+---------------------------+------------------------------------------------+
|| request_object_signing   || JSON array containing a list of the           |
|| _alg_values_supported    || JWS signing algorithms (alg values)           |
||                          || supported.                                    |
+---------------------------+------------------------------------------------+
|| presentation_definition  || Boolean value specifying whether the          |
|| _uri_supported           || Wallet Instance supports the transfer of      |
||                          || ``presentation_definition`` by                |
||                          || reference. MUST set to `false`.               |
+---------------------------+------------------------------------------------+

.. note::
   The claim ``attested_security_context`` (Attested Security Context) is under discussion
   and MUST be intended as experimental.

Below is an example of Wallet Instance Attestation:

.. code-block:: javascript

  {
    "alg": "ES256",
    "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
    "trust_chain": [
      "eyJhbGciOiJFUz...6S0A",
      "eyJhbGciOiJFUz...jJLA",
      "eyJhbGciOiJFUz...H9gw",
    ],
    "typ": "wallet-attestation+jwt",
  }
  .
  {
    "iss": "https://wallet-provider.example.org",
    "sub": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "attested_security_context": "https://wallet-provider.example.org/LoA/basic",
    "cnf":
    {
      "jwk":
      {
        "crv": "P-256",
        "kty": "EC",
        "x": "4HNptI-xr2pjyRJKGMnz4WmdnQD_uJSq4R95Nj98b44",
        "y": "LIZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg",
        "kid": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"
      }
    },
    "authorization_endpoint": "eudiw:",
    "response_types_supported": [
      "vp_token"
    ],
    "response_modes_supported": [
      "form_post.jwt"
    ],
    "vp_formats_supported": {
      "jwt_vp_json": {
        "alg_values_supported": ["ES256"]
      },
      "jwt_vc_json": {
        "alg_values_supported": ["ES256"]
      }
    },
    "request_object_signing_alg_values_supported": [
      "ES256"
    ],
    "presentation_definition_uri_supported": false,
    "iat": 1687281195,
    "exp": 1687288395
  }


.. _token endpoint: wallet-solution.html#wallet-instance-attestation
.. _Wallet Instance Attestation Request: wallet-instance-attestation.html#format-of-the-wallet-instance-attestation-request
.. _Wallet Instance Attestation: wallet-instance-attestation.html#format-of-the-wallet-instance-attestation
.. _RFC 7523 section 4: https://www.rfc-editor.org/rfc/rfc7523.html#section-4
