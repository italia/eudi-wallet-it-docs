.. include:: ../common/common_definitions.rst
.. Included via credential-presentation.rst at title level '=' (document title).


Remote Flow
===========

Depending on whether the User is using a mobile device or a workstation, the Relying Party MUST support the following remote flows (:ref:`RPR-84 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`):

* **Same Device**, the Relying Party MUST provide an ``HTTP`` location to the Wallet Instance using a redirect (``302``) or an HTML href in a web page (:ref:`RPR-01 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`);
* **Cross Device**, the Relying Party MUST provide a ``QR Code`` which the User frames with the device camera or with the Wallet Instance (:ref:`RPR-03 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).

To invoke the correct Wallet Instance, the Relying Party SHOULD trigger the Wallet Instance installed on the User's device the User wishes to use.
This information SHOULD be provided by the User using the Selection Page described in :ref:`functionalities:User Experience Design`.

- If the Selection Page is supported, the User selects the Wallet, and then the Relying Party retrieves the Wallet metadata as described in :ref:`wallet-metadata-retrieval:Wallet Metadata Retrieval Flow`. The content of the HTML href or QR Code depends on the ``authorization_endpoint`` parameter in the Wallet metadata:

  - If ``authorization_endpoint`` is available and contains an HTTPS URL (Universal Link), the Relying Party SHOULD use that endpoint.
  - Otherwise, the Relying Party MUST use one of the custom URL schemes: ``openid4vp://`` (as defined in Section 13.1.2 of [`OpenID4VP`_]) or ``haip-vp://`` (as defined in Section 5.1 of [`OPENID4VC-HAIP`_]). The Wallet Instance MUST support both custom URL schemes.

- In the case when the Relying Party does not support the Selection Page, or the retrieval of the Wallet metadata may fail for some reason, the Relying Party invokes the Wallet Instance using the custom URL scheme described above.

After the Wallet Instance invocation, the Wallet Instance establishes the trust with the Relying Party and evaluates the request. If valid, it will ask Users to give their consent for the disclosure of the Digital Credentials, in the form of a Verifiable Presentation.

.. _fig_High-Level-Flow-Presentation:
.. plantuml:: plantuml/credential-presentation-remote-high-level-flow.puml
    :width: 99%
    :alt: The figure illustrates the High Level Remote Protocol Flow.
    :caption: `High Level Remote Protocol Flow. <https://www.plantuml.com/plantuml/svg/TP9FJy904CNl-oacN9GcslZVS30OGWmdQeLmCI5BEz2LTNVTtThKJ-yEGcqndffqthptU-qCdUVMb--IcV0KcJ1SUUWjk9JeOQB2M6NO0-wWwafIbBLG6qZ2otedi8OnQ-3i0Qe1N9n353sMlj1MV74lj88KFqfqFeh05rQNcm8ivi9Yva5RU4uXqpc2oxW2huC6NnN4yG_AYOEksLZbHWlbuvWnBZs8zS4VfgitybpLmN-D5aC1nYhYicO0bmHsaCxJIGlhz6ay8vHa-ZBhxna2GPg4zFP6ExifVFNNrncj799nTGJNPmnLlgSAozUql9Z0gC1iwyB6x-Y6HdE75aRafWYqLUUMnWJS_Jv7wPzcwVKMrL6hHlLFBGgus_LAscXDvtkQTGwXawiDeN0fQwYQVxqihUYpOQWVhkuR>`_


.. .. figure:: ../../images/High-Level-Flow-Presentation.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/TL9TJy8m57tlhpZXHLcYYz-61uCXnF34d11UJCZS6bQPRMtlRF3NspB0JUBJidlEFH-v7LhA3DKV5TF-AtAXCqdeBRAgueI9zB3CUG-PXUjIKbvjX5mXySFDbc0qOqRZx05kW8jpHD5ZJQKouZiZeIHI_bbpIr64KmVJ_2nh8_gWqgXwLVfX8GpF2ShWEKMk2WwRPnAlafHdSSHn4-t4eYi-beLMGb8SC-P21gC7k0mXThQOfvDsXAVnBDWaqvTP7mVrDF7AxOssxg7SrR6krKfQtdJR8zEtTr-cpvZRxLs7lSK4evBdQ-l9lz1DWEQM6uo2a2IFjfhS1ZXa_LExQ_obbwJMN1uNQbZ_D0e6TzjAIJlQeUvzm3htxlWg7QBuispWzYTi3ilOaCl2lwuV

..     High Level Remote Protocol Flow


A High-Level description of the remote flow, from the User's perspective, is given below and shown in :ref:`fig_High-Level-Flow-Presentation`:

  1. *Authorization Request*: the Wallet Instance obtains a ``URL`` in the Same Device flow or a ``QR Code`` in Cross Device flow containing the signed Request Object either

    * directly, by passing a Request Object by value (via ``request`` parameter) or
    * by passing a Request Object by a reference (via ``request_uri`` parameter), where the signed Request Object is available for download. This is the only method permitted for OpenID4VC High Assurance Interoperability Profile (HAIP)-Compliant Relying Parties `OPENID4VC-HAIP`_.

    If by reference, Steps 2 and 3 are performed.

  2. *Request URI Request*: the Wallet Instance extracts from the payload the following parameters: ``client_id``, ``request_uri``, ``request_uri_method``.

    * If ``request_uri_method`` is provided and set with the value ``post``, the Wallet Instance SHOULD transmit its metadata to the Relying Party's ``request_uri`` endpoint using the ``HTTP POST`` method.
    * If ``request_uri_method`` is set with the value ``get`` or not present, the Wallet Instance MUST fetch the signed Request Object using an ``HTTP`` request with method ``GET`` to the endpoint provided in the ``request_uri`` parameter (:ref:`RPR-08 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).

  3. *Request URI Response*: the Relying Party returns a signed Request Object to the Wallet Instance.
  4. *WI Checks*: the Wallet Instance:

    a. verifies the signature of the signed Request Object using the public key identified in the ``JWT`` header of the Request Object. Using that reference, the Wallet Instance is able to select the correct Relying Party's public key for signature verification (:ref:`WP_085 <wallet-credential-presentation-testcases>`).
    b. verifies that the ``client_id`` contained in the Request Object issuer (Relying Party) matches with the one obtained at the Step 2:

       * If ``client_id`` uses the ``openid_federation`` prefix, it MUST match the ``sub`` parameter contained in the Relying Party's Entity Configuration within the Trust Chain (:ref:`WP_086 <wallet-credential-presentation-testcases>`).
       * If ``client_id`` uses the ``x509_hash`` prefix, the Wallet Instance MUST verify that the hash of the Relying Party’s X.509 certificate (in the ``x5c`` request header) matches the hash contained in ``client_id`` from Step 2 (as defined in `OpenID4VP`_, Section 5.9.3).

    c. evaluates the requested Digital Credentials and checks the eligibility of the Relying Party in asking for these by applying the policies related to that specific Relying Party, obtained with the Trust Chain (:ref:`WP_087 <wallet-credential-presentation-testcases>`).

  5. *POST Authorization Response*: the Wallet Instance presents the requested information to the Relying Party.
  6. *RP Checks*: The Relying Party validates the presented Credentials by verifying the trust with their Issuers and checks the respective validity status.
  7. *Relying Party Response*: the Wallet Instance informs the User about the successful authentication with the Relying Party, and the User continues the navigation.

Below is a sequence diagram that details the interactions between all the involved parties.

.. plantuml:: plantuml/credential-presentation-remote-flow.puml
    :width: 99%
    :alt: The figure illustrates the Remote Protocol Flow.
    :caption: `Remote Protocol Flow. <https://www.plantuml.com/plantuml/svg/fLPDRnit4BtpLmpKGssWIPCU3RX8eXgnaxHMBIM-630exaXYJP5RSYX5BVBVEuFHhZwK5W6gcxGpxyrxyx5wLSXcgijWRAKKwtAAsHZpsb7ACFXOC0_05gZ6JDDd_U7x0h_WoZii0_ZkWvylw4seQ5h6ySwtDX8Cxcq8I70J6Juw50nO7uPKXdfcvnX96Qp1s02pRAdkC6nydCE8apR_pdGGzX3FRbzNMi0mU0O-5sHO7MLmILGBC5kR_9QzOC_E7-l8homXowxmx6UezWBkSGfZpA8RebtvkIMVubweDGtk9rh9NE45tE6V5Gl1A2T2HzZmBoNLxD2Ooql-6Gj6iW87euKj29UNFQvKly8EYlri6G9stW5jMdo8bA11GGUNKodyHGg5bA7O9UfN1L8r2re6Q1a1rfxj-lrkc1e9XqN66RZ4zVWejj82eUO0lJWjoMprrGiOBz9QmZeGGHKa5xnxaWUAEQr4AHvuP7SgryRCSwej3BdyRhuWnR0nQ-5PCu-paJb0IAHPHdgZZpuaPmF8R8Ajp1Z9EsrFdtsrig4A4-LQI5Lpf5J9uO-UuMmWyBE-NRVJFyJFwGQuVCmOsK3WppOiQzXZpVvnYRH83NYPeotsw7OyCQ2VTTS-de2LRn2ssy5fjh5aWPBKiW_PJsU7iMy-w6St5ZjnYnwSq4KljZZRsgaFdZmMISLGy1i4lBsQI1TZ8cXrGa_aT4u9Q_7pY4q72adDc-Mq_4zfA7rKBThB3kYm2qORVZI3fyqzE0RmQ-UlZGsqANWd5dH9dp3xsGQ4prBD26dMAJajO9TbWsVCNX57VXgTbNCDg3jJPYdB7ebnH_T4WOOfpdnUOdDuDdfpPO10RbdA_Yyz3dmsMa64XwWzMhMFb9um_W1oq_3aQ9nEXwhsTXhmyF2GuEmblIOI5SECZQoJ3N1JIiKC4zcVXoYUxinuTp-1SMUaedG3xx0KtRGUofWS4sUb5MOEuzD-y_PwylRkwkety_MC2mFFOBX0FYZNAJISzXutyCR7HhejfN1UcaaBHwaK1X1DjSXJaFaIkBPEWtVmn9dJL3d7H_bzNoCbhaV6GhqQgItFZT1VVQPidKvxuuiBgM03bYZxQIKi86KugL6souRG3xvd0j11p0XsPNsG1ZoNeHOdqEnPzh5jjhtIWzQ9ENCfFNc4Ai-nEJVTnHpBWTU3gLF1RCpeI9RDx1RhUZ8P_VZo-KluwSKBk7tFBVnxi1ywaBS2jKNEVGUay_RevAv_sOwuvHgB5dZ0j7VNHTZN3te-AJTL-iQAznTbVNGBz6rKs3zunmQFNVOjQJSkZju9kYkoGsT2q2soIbQJptTY2fgY1LNxlptyeYTi1wr67VnNKB3kbT3s_nco_cSuMVAkjD5fvD7Bzj2nLqnTb-4V>`_


.. .. figure:: ../../images/cross_same_device_auth_seq_diagram.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/fLPDRnit4BtpLmpKGssWIPCU3RX8eXgnaxHMBIM-630exaXYJP5RSYX5BVBVEuFHhZwK5W6gcxGpxyrxyx5wLSXcgijWRAKKwtAAsHZpsb7ACFXOC0_05gZ6JDDd_U7x0h_WoZii0_ZkWvylw4seQ5h6ySwtDX8Cxcq8I70J6Juw50nO7uPKXdfcvnX96Qp1s02pRAdkC6nydCE8apR_pdGGzX3FRbzNMi0mU0O-5sHO7MLmILGBC5kR_9QzOC_E7-l8homXowxmx6UezWBkSGfZpA8RebtvkIMVubweDGtk9rh9NE45tE6V5Gl1A2T2HzZmBoNLxD2Ooql-6Gj6iW87euKj29UNFQvKly8EYlri6G9stW5jMdo8bA11GGUNKodyHGg5bA7O9UfN1L8r2re6Q1a1rfxj-lrkc1e9XqN66RZ4zVWejj82eUO0lJWjoMprrGiOBz9QmZeGGHKa5xnxaWUAEQr4AHvuP7SgryRCSwej3BdyRhuWnR0nQ-5PCu-paJb0IAHPHdgZZpuaPmF8R8Ajp1Z9EsrFdtsrig4A4-LQI5Lpf5J9uO-UuMmWyBE-NRVJFyJFwGQuVCmOsK3WppOiQzXZpVvnYRH83NYPeotsw7OyCQ2VTTS-de2LRn2ssy5fjh5aWPBKiW_PJsU7iMy-w6St5ZjnYnwSq4KljZZRsgaFdZmMISLGy1i4lBsQI1TZ8cXrGa_aT4u9Q_7pY4q72adDc-Mq_4zfA7rKBThB3kYm2qORVZI3fyqzE0RmQ-UlZGsqANWd5dH9dp3xsGQ4prBD26dMAJajO9TbWsVCNX57VXgTbNCDg3jJPYdB7ebnH_T4WOOfpdnUOdDuDdfpPO10RbdA_Yyz3dmsMa64XwWzMhMFb9um_W1oq_3aQ9nEXwhsTXhmyF2GuEmblIOI5SECZQoJ3N1JIiKC4zcVXoYUxinuTp-1SMUaedG3xx0KtRGUofWS4sUb5MOEuzD-y_PwylRkwkety_MC2mFFOBX0FYZNAJISzXutyCR7HhejfN1UcaaBHwaK1X1DjSXJaFaIkBPEWtVmn9dJL3d7H_bzNoCbhaV6GhqQgItFZT1VVQPidKvxuuiBgM03bYZxQIKi86KugL6souRG3xvd0j11p0XsPNsG1ZoNeHOdqEnPzh5jjhtIWzQ9ENCfFNc4Ai-nEJVTnHpBWTU3gLF1RCpeI9RDx1RhUZ8P_VZo-KluwSKBk7tFBVnxi1ywaBS2jKNEVGUay_RevAv_sOwuvHgB5dZ0j7VNHTZN3te-AJTL-iQAznTbVNGBz6rKs3zunmQFNVOjQJSkZju9kYkoGsT2q2soIbQJptTY2fgY1LNxlptyeYTi1wr67VnNKB3kbT3s_nco_cSuMVAkjD5fvD7Bzj2nLqnTb-4V

..     Remote Protocol Flow


The details of each step shown in the previous picture are described below.

**Steps 1-2**: The User requests to access to a protected resource of the Relying Party.

**Step 3**: The Relying Party creates a fresh, cryptographically random state value with sufficient entropy, binds it to the user-agent session (e.g., using an HTTP secured cookie), and stores it server-side with a short expiration time. It then inspects the user-agent to determine whether the flow occurs on the same device as the user-agent.

**Steps 4-7 (Authorization Request)**: The Relying Party provides the user-agent with a JavaScript page inspecting the status endpoint and the Wallet Instance with a URL containing the Authorization Request.

  In the **Cross Device Flow**, the Authorization Request is presented as a QR Code displayed to the User. The User scans the QR Code using the Wallet Instance and retrieves a URL.
  Below is represented a non-normative example of a QR Code issued by the Relying Party.

  .. only:: format_html

    .. figure:: ./images/svg/verifier_qr_code.svg
      :figwidth: 50%
      :align: center

  .. only:: format_latex

    .. figure:: ./images/pdf/verifier_qr_code.pdf
      :width: 50%
      :align: center

  .. note::
    The *error correction level* chosen for the QR Code MUST be Q (Quartily - up to 25%), since it offers a good balance between error correction capability and data density/space. This level of quality and error correction allows the QR Code to remain readable even if it is damaged or partially obscured (:ref:`RPR-77 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).

  If the Request Object is passed by value the URL inside the QR Code contains ``client_id`` and ``request`` parameters.
  Below a non-normative example of the QR Code raw payload with Request Object by value:

  .. code-block:: text

    https://wallet-solution.example.org/authorization?client_id=openid_federation%3Ahttps%3A%2F%2Frelying-party.example.org&request=eyJhbGciOiJFUzI1NiIs...9t2LQ

  While if the Request Object is passed by reference the URL inside the QR Code contains ``client_id``, ``request_uri``, and ``request_uri_method`` parameters (:ref:`WP_076–077 <wallet-credential-presentation-testcases>`).
  Below is represented a non-normative example of the QR Code raw payload with Request Object by reference:

  .. code-block:: text

    https://wallet-solution.example.org/authorization?client_id=openid_federation%3Ahttps%3A%2F%2Frelying-party.example.org&request_uri=https%3A%2F%2Frelying-party.example.org&request_uri_method=post

  An official, self-contained HTML template for this **Cross Device** QR code page—including header, footer, accessibility, multilingual copy, and a configurable demonstrative payload—is provided in the :ref:`official-resources:HTML Components` section (**IT-Wallet Presentation QR Code Page**). It is linked from the wallet cards on the **IT-Wallet Selection Page** in the same section.

  Conversely, in the **Same Device Flow**, the Relying Party uses an HTTP response redirect (with status code set to 302) or an html page with an href button, containing the URL providing the same information as in the Cross-Device Flow (:ref:`WP_076–077 <wallet-credential-presentation-testcases>`).
  Below is a non-normative example with Request Object by reference:

  .. code-block:: http

    HTTP/1.1 302 Found
    Location: https://wallet-solution.digital-strategy.europa.eu?client_id=openid_federation%3Ahttps%3A%2F%2Frelying-party.example.org%2Fcb&request_uri=https%3A%2F%2Frelying-party.example.org%2Frequest_uri&request_uri_method=post


**Step 8**: The Wallet Instance evaluates the trust with the Relying Party (:ref:`WP_078–080 <wallet-credential-presentation-testcases>`).

**Steps 9-11 (Request URI Request)**: The Wallet Instance checks if the Relying Party has provided the ``request_uri_method`` within its signed Request Object (:ref:`WP_083 <wallet-credential-presentation-testcases>`).

  - If it is provided and is equal to ``post``, the Wallet Instance SHOULD provide its metadata to the Relying Party. The Relying Party updates the Request Object according with the Wallet technical capabilities.

    The following is a non-normative example of an HTTP request made by the Wallet Instance to the Relying Party.

    .. code-block:: http

      POST /request HTTP/1.1
      Host: client.example.org
      Content-Type: application/x-www-form-urlencoded
      Accept: application/oauth-authz-req+jwt

      wallet_metadata=%7B%22vp_formats_supported%22%3A%20%7B%22dc%2Bsd-jwt%22%3A%20%7B%22sd-jwt_alg_values%22%3A%20%5B%22ES256%22%2C%20%22ES384%22%5D%7D%2C%22mso_mdoc%22%3A%7B%22issuerauth_alg_values%22%3A%5B-9%2C-51%5D%2C%22deviceauth_alg_values%22%3A%5B-9%2C-51%5D%7D%7D%2C%22request_object_signing_alg_values_supported%22%3A%20%5B%22ES256%22%5D%2C%22client_id_prefixes_supported%22%3A%5B%22openid_federation%22%2C%22x509_hash%22%5D%7D&wallet_nonce=qPmxiNFCR3QTm19POc8u
    
    Where the body of the request prior to being encoded in `application/x-www-form-urlencoded` by the Wallet corresponds to:

    .. code-block:: json

      {
        "wallet_metadata": {
          "vp_formats_supported": {
            "dc+sd-jwt": {
                "sd-jwt_alg_values": ["ES256", "ES384"]
            },
            "mso_mdoc": {
                "issuerauth_alg_values": [-9, -51],
                "deviceauth_alg_values": [-9, -51]
            }
          },
          "request_object_signing_alg_values_supported": ["ES256"],
          "client_id_prefixes_supported": ["openid_federation", "x509_hash"]
        },
        "wallet_nonce": "qPmxiNFCR3QTm19POc8u"
      }

  - When the Wallet Instance capabilities discovery is not supported by Relying Party, the Wallet Instance requests the signed Request Object using the HTTP method GET (:ref:`WP_082 <wallet-credential-presentation-testcases>`).

**Step 12 (Request URI Response)**: The Relying Party issues the Request Object signing it using one of its cryptographic private keys, where their public parts have been published within its Entity Configuration (`metadata.openid_credential_verifier.jwks`) as extracted by Wallet Instance per :ref:`WP_084 <wallet-credential-presentation-testcases>`. The Wallet Instance obtains the signed Request Object.

  Below is a non-normative example of the Redirect URI Response:

  .. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/oauth-authz-req+jwt

    eyJhbGciOiJFUzI1NiIs...9t2LQ

**Steps 13-15 (WI Checks)**: The Wallet Instance verifies the Request Object, which is in the form of a signed JWT (:ref:`WP_085–086 <wallet-credential-presentation-testcases>`).

  A non-normative example of a Request Object in the form of decoded header and payload is shown below:

  .. code-block:: json

    {
      "alg": "ES256",
      "typ": "oauth-authz-req+jwt",
      "kid": "9tjiCaivhWLVUJ3AxwGGz_9",
      "trust_chain": [
        "MIICajCCAdOgAwIBAgIC...awz",
        "MIICajCCAdOgAwIBAgIC...2w3",
        "MIICajCCAdOgAwIBAgIC...sf2"
      ],
      "x5c": [
        "MIIDqjCCApKgAwIBAgIESLNEvDA ...",
        "MIICwzCCAasCCQCKVy9eKjvi+jA ...",
        "MIIDTDCCAjSgAwIBAgIJAPlnQYH..."
      ]
    }

  .. code-block:: json

    {
      "client_id": "openid_federation:https://relying-party.example.org",
      "response_mode": "direct_post.jwt",
      "response_type": "vp_token",
      "dcql_query": {
        "credentials": [
          {
            "id": "personal id data",
            "format": "dc+sd-jwt",
            "meta": {
              "vct_values": [ "urn:eudi:pid:it:1" ]
            },
            "claims": [
              {"path": ["given_name"]},
              {"path": ["family_name"]},
              {"path": ["birthdate"]}
            ]
          },
          {
            "id": "mobile driving license",
            "format": "mso_mdoc",
            "meta": {
              "doctype_value": "org.iso.18013.5.1.mDL"
            },
            "claims": [
              {"path": ["org.iso.18013.5.1", "given_name"]},
              {"path": ["org.iso.18013.5.1", "family_name"]},
              {"path": ["org.iso.18013.5.1", "document_number"]}
            ]
          }
        ]
      },
      "response_uri": "https://relying-party.example.org/response_uri",
      "nonce": "2c128e4d-fc91-4cd3-86b8-18bdea0988cb",
      "wallet_nonce": "qPmxiNFCR3QTm19POc8u",
      "client_metadata": {
          "jwks": {
            "keys": [
              {
                "kty": "EC",
                "use": "enc",
                "crv": "P-256",
                "x": "f83OJ3D2xF1Bg8vub9tLe1gHMzV76e8Tus9uPHvRVEU",
                "y": "x_FEzRu9m36HLN_tue659LNpXW6pCyStikYjKIWI5a0",
                "kid": "20260202-abc123",
                "alg": "ECDH-ES"
              }
            ]
          },
          "encrypted_response_alg_values_supported": ["ECDH-ES"],
          "encrypted_response_enc_values_supported": ["A128GCM", "A256GCM"]
      },
      "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
      "iss": "https://relying-party.example.org",
      "iat": 1672418465,
      "exp": 1672422065
    }

  It then processes the Relying Party metadata and applies the relevant policies to determine which Digital Credentials and User data the Relying Party is authorized to request (:ref:`WP_087 <wallet-credential-presentation-testcases>`).

**Steps 16-17 (User Consent)**: The Wallet Instance requests the User's consent to disclose the requested Credentials by showing the Relying Party's identity and the requested attributes. The User authorizes and consents the presentation of the Credentials by selecting and or deselecting the personal data to release (:ref:`WP_088 <wallet-credential-presentation-testcases>`).

**Step 18 (Authorization Response)**: The Wallet Instance provides the Authorization Response to the Relying Party using an HTTP request with the method POST using response mode "direct_post.jwt".

  Below is a non-normative example of the Authorization Response:

  .. code-block:: http

      POST /response_uri HTTP/1.1
      HOST: relying-party.example.org
      Content-Type: application/x-www-form-urlencoded

      response=eyJhbGciOiJFQ0RILUVTIiwiZW5jIjoiQTI1NkdDTSIsImtpZCI6ImVwaGVtZXJhbC0yMDI2MDIwMi1hYmMxMjMiLCJlcGsiOnsi...fX0..5vL9d2X8fQ..dGhpcy1pcy1hLXNhbXBsZS1jaXBoZXJ0ZXh0.ABCDEFGHIJKLMNOPQRS

  Below is a non-normative example showing the decrypted JWE protected header and the payload of the JWT contained in the response, before base64url encoding. The ``vp_token`` parameter value corresponds to the format used when the DCQL query language is used in the presentation request.

  .. code-block:: json

      {
        "alg": "ECDH-ES",
        "enc": "A256GCM",
        "kid": "20260202-abc123",
        "epk": {
          "kty": "EC",
          "crv": "P-256",
          "x": "f83OJ3D2xF1Bg8vub9tLe1gHMzV76e8Tus9uPHvRVEU",
          "y": "x_FEzRu9m36HLN_tue659LNpXW6pCyStikYjKIWI5a0"
        }
      }

  .. code-block:: json

      {
        "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
        "vp_token": {
          "personal id data": ["eyJhbGciOiJFUzI1NiIs...PT0iXX0"],
          "mobile driving license": ["o2Nkb2N0eXBlb3Jzby4xO...Nib3JfZHVtbXk"]
        }
      }

.. note::
  When returning a requested Credential in ``mso_mdoc`` format in the ``vp_token``, the Wallet MUST cryptographically bind the resulting mdoc presentation to the current OpenID4VP transaction. To achieve this, the Wallet builds the ISO ``SessionTranscript`` used for mdoc device authentication and applies the OpenID4VP profiling rules by setting ``DeviceEngagementBytes`` to ``null`` and ``EReaderKeyBytes`` to ``null``, and sets its ``Handover`` field to an OpenID4VP-defined structure (``OpenID4VPHandover``) derived from the Authorization Request parameters. The Wallet then computes the mdoc device authentication (device signature) over data that includes this ``SessionTranscript``, such that the resulting mdoc presentation is valid only for that specific OpenID4VP transaction. For the normative definition of ``OpenID4VPHandover`` and the corresponding ``SessionTranscript`` profiling rules, see `OpenID4VP`_ Appendix B.2.

**Steps 19-22 (RP Checks)**: The Relying Party verifies the Authorization Response, extracts the ``vp_token``, which contains one or more Digital Credentials presentations, and validates the overall format of the VP Token. For each credential presentation, the Relying Party verifies its integrity according to the DCQL query criteria defined in the Authorization Request. The Relying Party MUST also attest trust with the corresponding Credentials Issuer, and validate the Wallet Instance's proof of possession of each presented Digital Credential. Finally, the Relying Party verifies the revocation status of each presented Digital Credential, as described in :ref:`credential-revocation:Digital Credential Revocation and Suspension`. If all previous verifications yielded positive result, the Relying Party updates the User session.

**Steps 23-24 or 25 (Relying Party Response)**: The Relying Party provides to the Wallet Instance the response about the presentation, which informs the User.

  Upon receiving and validating the Authorization Response at the Response Endpoint, the Relying Party returns to the Wallet Instance an HTTP 200 OK. In particular, in the Same Device Flow, the Relying Party MUST also pass the ``redirect_uri`` parameter in the response to the Wallet Instance. Upon receiving the ``redirect_uri``, the Wallet Instance MUST perform a redirect to the URL specified by the ``redirect_uri``. This redirect allows the Relying Party to seamlessly resume interaction with the User on the device which initiated the flow. When the response does not contain the ``redirect_uri`` parameter, the Wallet Instance is not required to perform any further step. The User should manually close the Wallet Instance and open the user-agent to continue the flow (:ref:`RPR-83 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).

  The following is a non-normative example of the response in the Same Device Flow.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "redirect_uri": "https://relying-party.example.org/cb?response_code=091535f699ea575c7937fa5f0f454aee"
    }

**Steps 26-27**: The JavaScript page is inspecting the status endpoint.

  Below is a non-normative example of the HTTP Request to the status endpoint, where the parameter ``id`` contains an opaque and random value:

  .. code-block:: http

      GET /session-state?id=3be39b69-6ac1-41aa-921b-3e6c07ddcb03 HTTP/1.1
      HOST: relying-party.example.org

  When the Wallet Instance has provided the presentation to the Relying Party's **response_uri** endpoint and, in the Same Device Flow, the user-agent has successfully returned via ``redirect_uri`` within the same user session, the User authentication is successful. The Relying Party updates the session cookie allowing the user-agent to access to the protected resource. A redirect URL is provided carrying the location where the user-agent is intended to navigate.
  The following is a non-normative example of the response with the ``redirect_uri`` from the Relying Party to the user-agent.

  .. code-block:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "redirect_uri": "https://relying-party.example.org/cb?response_code=091535f699ea575c7937fa5f0f454aee"
      }

**Steps 28-29**: The user-agent is redirected to the redirect URI to continue the navigation with the protected resource made available to the User (:ref:`WP_094 <wallet-credential-presentation-testcases>`). The Relying Party MUST consider the transaction completed only if the redirect back is received in the same user session in which the flow was initiated; otherwise it MUST reject the presentation.

.. note::
    During each credential presentation transaction executed through the remote flow, the Wallet Instance MUST create and maintain a corresponding transaction record in the transaction log (see :ref:`wallet-instance-dashboard:Wallet Instance Dashboard and Transaction Logging`).

    The transaction record MUST be created once the Wallet Instance has accepted the presentation request for processing (i.e., after request validation and Relying Party trust/policy checks, Steps 13–15). At this point, the record MUST include the transaction metadata and the request context available at that stage (e.g., the requested Credential type(s) and the identifier(s) of the requested attributes), without logging any attribute values.

    The record MUST be updated as the transaction progresses to reflect the evolving transaction state and result context (e.g., what was actually presented after User consent and response preparation/sending, Steps 16–18), without logging any attribute values.

    The record MUST be finalized when the transaction ends, indicating the outcome (e.g., completed, failed, or aborted; Steps 23–29).


Authorization Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The URL parameters contained in the Relying Party Authorization Request are described in the table below.

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **client_id**
    - REQUIRED. Unique identifier of the Relying Party. The value MUST use one of the following Client Identifier Prefixes (as defined in `OpenID4VP`_, Section 5.9): ``openid_federation`` (Relying Party’s Entity Identifier in a Trust Chain) or ``x509_hash`` (base64url-encoded SHA-256 hash of the Relying Party’s X.509 certificate).
  * - **request**
    - CONDITIONAL. REQUIRED unless ``request_uri`` is specified. It contains the base64url-encoded and signed Request Object. For the content of the Request Object see Section :ref:`remote-flow:Request Object`.
  * - **request_uri**
    - CONDITIONAL. REQUIRED unless ``request`` is specified. The HTTP URL where the Relying Party provides the signed Request Object to the Wallet Instance.
  * - **request_uri_method**
    - OPTIONAL only if ``request_uri`` is specified, otherwise MUST NOT be present. The HTTP method MUST be set with ``get`` or ``post`` (:ref:`RPR-07 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`, :ref:`RPR-08 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`, :ref:`RPR-09 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`). The Wallet Instance should use this method to obtain the signed Request Object from the ``request_uri``. If not provided or equal to ``get``, the Wallet Instance SHOULD use the HTTP method ``get``. Otherwise, the Wallet Instance SHOULD provide its metadata within the HTTP POST body encoded in ``application/x-www-form-urlencoded``.

.. note::
  IT Wallet specification recommends the use of ``request_uri``, i.e. Request Object by reference.

.. warning::

  For security reasons and to prevent endpoint mix-up attacks, the value contained in the ``request_uri`` parameter MUST be one of those attested by a trusted third party, such as those provided in the ``openid_credential_verifier`` metadata within the ``request_uris`` parameter, obtained from the Trust Chain about the Relying Party (:ref:`WP_081 <wallet-credential-presentation-testcases>` and :ref:`RPR-85 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).

The value corresponding to the ``request_uri`` endpoint SHOULD be randomized, according to `RFC 9101, The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR) <https://www.rfc-editor.org/rfc/rfc9101.html#section-5.2.1>`_ Section 5.2.1.


Request URI Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Relying Party SHOULD provide the POST method with its ``request_uri`` endpoint allowing the Wallet Instance to inform the Relying Party about its technical capabilities.

This feature can be useful when, for example, the Wallet Instance supports a restricted set of features, supported algorithms or a specific url for its ``authorization_endpoint``, and any other information that it deems necessary to provide to the Relying Party for interoperability.

.. warning::
  The Wallet Instance, when providing its technical capabilities to the Relying Party, MUST NOT include any User information or other explicit (:ref:`RPR-86 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`) information regarding the hardware used or usage preferences of its User (:ref:`RPR-86 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).

If both the Relying Party and the Wallet Instance support the ``request_uri_method`` with HTTP POST, the Wallet Instance capabilities (metadata) MUST be provided using an HTTP request to the ``request_uri`` endpoint of the Relying Party, with the method POST and content type set to ``application/x-www-form-urlencoded`` (:ref:`WP_083 <wallet-credential-presentation-testcases>`).
The request and its parameters are defined in Section 5 (Authorization Request) of `OpenID4VP`_. Below are the normative details and references about the parameters to be used by the Wallet Instance in the request (:ref:`WP_083a–083c <wallet-credential-presentation-testcases>`).

.. list-table:: Request URI Endpoint Parameters
   :class: longtable
   :widths: 20 80
   :header-rows: 1

   * - **Parameter**
     - **Description**
   * - `wallet_metadata`
     - OPTIONAL. JSON object with metadata parameters. See `OpenID4VP`_, Section 10.1 and the table below, "Wallet Metadata Parameters".
   * - `wallet_nonce`
     - RECOMMENDED. String used by Wallet Instance to prevent replay of the Relying Party's responses.


.. _table_wallet_metadata_parameters:
.. list-table:: Wallet Metadata Parameters
   :class: longtable
   :widths: 20 80
   :header-rows: 1

   * - **Parameter**
     - **Description**
   * - `vp_formats_supported`
     - REQUIRED. Object containing a list of name/value pairs, where the name is a Credential Format Identifier and the value defines format-specific parameters that a Wallet supports. See `OpenID4VP`_ Appendix B. Wallet Instances MUST support the Credential Format Identifiers required by `OPENID4VC-HAIP`_ (including ``dc+sd-jwt`` and ``mso_mdoc``).
   * - `client_id_prefixes_supported`
     - RECOMMENDED. A non-empty array of the Client Identifier Prefixes that the Wallet Instance supports.  Valid values include ``openid_federation`` and ``x509_hash``; if omitted, the default is ``pre-registered``.
   * - `request_object_signing_alg_values_supported`
     - OPTIONAL. See OpenID Connect Discovery.


.. note::
  In the IT Wallet, legacy Relying Parties using an ``https`` URI as ``client_id`` implicitly follow the OpenID Federation client identifier prefix (``openid_federation``). Their trust is established and validated through trust chain resolution, which is treated as equivalent to that of statically trusted (pre-registered) clients as defined in [:rfc:`6749`], for backward compatibility.

.. note::
  The ``wallet_nonce`` parameter is RECOMMENDED for Wallet Instances that want to prevent reply of their http requests to the Relying Parties.
  When present, the Relying Party MUST evaluate it (:ref:`RPR-81 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).


Request URI Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Relying Party issues the signed Request Object using the content type set to ``application/oauth-authz-req+jwt``. For the content of the Request Object see Section :ref:`remote-flow:Request Object`.

Request URI Endpoint Errors
----------------------------

When the Relying Party encounters errors while issuing the Request Object from the ``request_uri`` endpoint, it MUST return an error response with ``application/json`` as the content type and MUST include the following parameters:

* ``error``: The error code.
* ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

The following table lists the HTTP Status Codes and related error codes that MUST be supported for the error response:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **Error Code**
      - **Description**
    * - ``400 Bad Request``
      - ``invalid_request``
      - The Request Object could not be retrieved due to an invalid or malformed request at the ``request_uri`` endpoint. (:rfc:`6749#section-4.1.2.1`).
    * - ``500 Internal Server Error``
      - ``server_error``
      - The request cannot be fulfilled because the Request URI Endpoint encountered an internal problem. (:rfc:`6749#section-4.1.2.1`).
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The request cannot be fulfilled because the Request URI Endpoint is temporarily unavailable (e.g., due to maintenance or overload). (:rfc:`6749#section-4.1.2.1`).


The following is an example of an error response from ``request_uri`` endpoint:

.. code-block:: http

  HTTP/1.1 500 Internal Server Error
  Content-Type: application/json

  {
    "error": "server_error",
    "error_description": "The Request Object cannot be retrieved due to an internal server error."
  }

Upon receiving an error response, the Wallet Instance SHOULD inform the User of the error condition in an appropriate manner (:ref:`WP_089 <wallet-credential-presentation-testcases>`). The Wallet Instance SHOULD log the error and MAY attempt to recover from certain errors if feasible (:ref:`WP_089a <wallet-credential-presentation-testcases>`). For example, if the error is ``server_error``, the Wallet Instance SHOULD prompt the User to re-enter or scan a new QR code, if applicable (:ref:`WP_089b <wallet-credential-presentation-testcases>`).

Request Object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The JWT header parameters are described below:

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **alg**
    - REQUIRED. Algorithm used to sign the JWT, according to [:rfc:`7516#section-4.1.1`]. It MUST be one of the supported algorithms in Section :ref:`algorithms:Cryptographic Algorithms` and MUST NOT be set to ``none`` or to a symmetric algorithm (MAC) identifier (:ref:`RPR-88 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).
  * - **typ**
    - REQUIRED. Media Type of the JWT, as defined in [:rfc:`7519`] and [:rfc:`9101`]. It SHOULD be set to the value ``oauth-authz-req+jwt`` (:ref:`RPR-89 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).
  * - **kid**
    - REQUIRED when ``client_id`` uses the ``openid_federation`` scheme. OPTIONAL when ``client_id`` uses an ``x509_hash`` prefix scheme. Key ID of the public key needed to verify the JWT signature, as defined in [:rfc:`7517`].
  * - **trust_chain**
    - OPTIONAL. It is a sequence of Entity Statements that composes the Trust Chain related to the Relying Party, as defined in `OID-FED`_ Section 4.3 *Trust Chain Header Parameter*.
  * - **x5c**
    - REQUIRED when ``client_id`` uses an ``x509_hash`` prefix scheme. OPTIONAL when ``client_id`` uses the ``openid_federation`` scheme. It contains the X.509 certificate chain about the Relying Party, excluding the Trust Anchor certificate. This certificate MUST be used to verify the JWT signature. The Relying Party’s certificate in ``x5c`` asserts the Relying Party identity information along with the network endpoints used in the presentation flow, including the endpoints Authorization Request and Response endpoints (``response_uri`` and ``redirect_uri``). All the endpoints used in the presentation flow MUST be bound to the FQDN and any further webpath provided in the Relying Party’s certificate, in the form of URI-type SAN for full-URI matching, or a DNSName SAN for host-name matching.

.. note::
   The ``x5c`` header MUST NOT include the root certificate, as required by `OPENID4VC-HAIP`_. The ``x5c`` certificate chain MUST validate to a preconfigured root certificate; see Section :ref:`infrastructure-trust:X.509 Certificate Profile` for background on X.509 certificate chain validation.

The JWT payload parameters are described herein:

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **client_id**
    - REQUIRED. Unique Identifier of the Relying Party.
  * - **client_metadata**
    - REQUIRED. A JSON object containing the Relying Party metadata values as defined in Section 5.1 of `OpenID4VP`_, that SHOULD include the following parameters:
        - **vp_formats_supported**. Used by the Wallet Instance to determine the supported Verifiable Presentation formats.
        - **encrypted_response_enc_values_supported**. JSON array listing the supported JWE ``enc`` algorithms for encrypted Authorization Responses in ``direct_post.jwt``.
        - **jwks**. JSON Web Key Set used by the Wallet Instance for encrypting the Authorization Response or for key agreement. Keys contained in this set are request-specific and identified by their ``kid`` value.
        - **client_name** and **logo_uri**. OPTIONAL. Used for user consent display and to show the Relying Party identity in the Wallet Instance interface.
  * - **response_mode**
    - REQUIRED. It MUST be set to ``direct_post.jwt`` in both Same Device and Cross Device flows (:ref:`RPR-90 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).
  * - **dcql_query**
    - REQUIRED. Object representing a request for a presentation of Credentials, according to the DCQL query language defined in Section 6 of `OpenID4VP`_.
  * - **transaction_data**
    - OPTIONAL. Non-empty array of JSON objects, each describing a transaction that the Relying Party requests the User to authorize. Each transaction object includes:
        - **type**.  String that identifies the transaction data type.
        - **credential_ids**. Array referencing one or more Credentials from the ``dcql_query`` that can authorize the transaction.
  * - **transaction_data_hashes_alg**
    - OPTIONAL. Array of strings, each representing a hash algorithm identifier, corresponding to a hash algorithm name listed in the `IANA <https://www.iana.org/assignments/named-information/named-information.xhtml#hash-alg>`_.  One of these algorithms MUST be used to calculate the hashes in the ``transaction_data_hashes`` response parameter.  If omitted, the default hash algorithm is ``sha-256``.
  * - **response_type**
    - REQUIRED. It MUST be set to ``vp_token`` (:ref:`RPR-91 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).
  * - **wallet_nonce**
    - REQUIRED if previously provided by Wallet Instance (:ref:`RPR-81 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`). String value used to mitigate replay attacks of the response, as defined in Section 5.10 (Request URI Method) of `OpenID4VP`_.
  * - **response_uri**
    - REQUIRED. The Response URI to which the Wallet Instance MUST send the Authorization Response using an HTTP request using the method POST (:ref:`RPR-92 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).
  * - **nonce**
    - REQUIRED. Fresh cryptographically random number with sufficient entropy, which length MUST be at least 32 digits (:ref:`RPR-93 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).
  * - **state**
    - RECOMMENDED. Unique identifier of the Authorization Request, its value SHOULD be opaque to the Wallet Instance.
  * - **iss**
    - REQUIRED. The entity that has issued the JWT. It will be populated with the Relying Party client id.
  * - **iat**
    - REQUIRED. Unix Timestamp, representing the time at which the JWT was issued.
  * - **exp**
    - REQUIRED. Unix Timestamp, representing the expiration time on or after which the JWT MUST NOT be valid anymore (:ref:`RPR-94 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).

.. warning::

  For security reasons and to prevent endpoint mix-up attacks, the value contained in the ``response_uri`` parameter MUST be one of those attested by a trusted third party, such as those provided in the ``openid_credential_verifier`` metadata within the ``response_uris`` parameter, obtained from the Trust Chain about the Relying Party (:ref:`WP_091a <wallet-credential-presentation-testcases>` and :ref:`RPR-95 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).

.. note::
  The ``transaction_data`` parameter is intended for use cases where the Wallet Instance MUST authorize a specific transaction, such as payment initiation or digital signing. In these high-sensitivity scenarios, the goal is to bind the transaction details to the Authorization Response so that integrity is preserved and the User’s approval can be proven afterwards (non-repudiation).

  The binding mechanism depends on the Credential Format:

  - **dc+sd-jwt**: the Wallet binds the transaction data by returning ``transaction_data_hashes`` (and, when applicable, ``transaction_data_hashes_alg``) inside the Key Binding JWT (KB-JWT). See `OpenID4VP`_, Appendix B.3.3 for further details.
  - **mso_mdoc**: transaction data is bound through mdoc device authentication. For this format, the Wallet MUST check that the requested transaction data ``type`` is supported by the document type and authorized by the issuer (KeyAuthorizations). If it is not authorized, the Wallet MUST reject the request due to an unsupported transaction data type. See `OpenID4VP`_, Appendix B.2.1 for further details.

.. note::
  The ``state`` parameter in an OAuth request is optional, but it is highly recommended. It is primarily used to prevent Cross-Site Request Forgery (CSRF) attacks by including a unique and unpredictable value that the Relying Party can verify upon receiving the response. Additionally, it helps maintain the state between the request and response, such as session information or other data the Relying Party needs after the authorization process.

.. note::
  The ``client_metadata`` parameter usage is conditional. If ``client_id`` uses the ``x509_hash`` prefix, all the Relying Party metadata, other than its public key used for signing the Request Object, MUST be provided in ``client_metadata``. However, if it is present and ``client_id`` uses the ``openid_federation`` prefix, the Wallet Instance MUST obtain the Relying Party metadata through the OpenID Federation Trust Chain (:ref:`RPR-96 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`), and MUST NOT use ``client_metadata`` to override or replace resolved metadata. The only exception is ``client_metadata.jwks`` (and related encrypted-response capability parameters such as ``encrypted_response_enc_values_supported``), which MAY be used exclusively to carry request-specific (ephemeral) public keys for encrypting the Authorization Response in ``direct_post.jwt`` (see `OpenID4VP`_ Section 8.3).

Authorization Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
After obtaining the User authorization and consent for the presentation of the Digital Credentials, the Wallet Instance sends the Authorization Response to the Relying Party ``response_uri`` endpoint using an HTTP request with the method POST (:ref:`WP_091 <wallet-credential-presentation-testcases>`). The response content MUST be encrypted following the high-assurance profile defined in `OPENID4VC-HAIP`_, utilizing response mode ``direct_post.jwt`` per `OpenID4VP`_ Section 8.3.  This encryption requires the use of ECDH-ES key agreement on P-256 curve and AES-GCM content encryption (``A128GCM`` or ``A256GCM``, preferring ``A256GCM`` when both available), and using the request-specific public key of Relying Party selected from ``client_metadata.jwks``, that is identified by its ``kid`` (:ref:`WP_092 <wallet-credential-presentation-testcases>`). The Verifier’s public key used to encrypt the Authorization Response is retrieved by the Wallet from the JWKs in the ``client_metadata``. According to Section 14.5 of `OpenID4VP`_ it is RECOMMENDED the usage of ephemeral keys.

.. note::
    **Why the response is encrypted?**

    The response sent from the Wallet Instance to the Relying Party is encrypted to prevent a malicious agent from gaining access to the plaintext information transmitted within the Relying Party's network. This is only possible if the network environment of the Relying Party employs `TLS termination <https://www.f5.com/glossary/ssl-termination>`_. Such technique employs a termination proxy that acts as an intermediary between the client and the webserver and handles all TLS-related operations. In this manner, the proxy deciphers the transmission's content and either forwards it in plaintext or by negotiates an internal TLS session with the actual webserver's intended target. In the first scenario, any malicious actor within the network segment could intercept the transmitted data and obtain sensitive information, such as an unencrypted response, by sniffing the transmitted data.

Where the following parameters are used (:ref:`WP_093 <wallet-credential-presentation-testcases>`):

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **vp_token**

    - This object MUST contain the presented Digital Credential(s), keyed by the Credential ``id`` values from the ``dcql_query`` in the Authorization Request.

      The ``vp_token`` MUST be a JSON Object where each key corresponds to a requested Credential id, and each value is either a single presentation or an array of one or more presentations for that Credential. The encoding of each presentation depends on the Credential format, for example:

      - **dc+sd-jwt**: an SD-JWT VC string (including the appended Key Binding JWT) (:ref:`WP_093a <wallet-credential-presentation-testcases>`).
      - **mso_mdoc**: a base64url-encoded CBOR ``DeviceResponse`` corresponding to the requested mdoc presentation (see `OpenID4VP`_ Appendix B.2). When multiple mdoc presentations are returned, each MUST be carried in a separate ``DeviceResponse`` aligned with the corresponding DCQL query item; in this case, the ``vp_token`` value for that Credential id MUST be an array of ``DeviceResponse`` values.

  * - **state**
    - Unique identifier provided by the Relying Party within the Authorization Request.

.. note::
  Although `OpenID4VP`_ considers SD-JWT-based Verifiable Credentials (SD-JWT VC) draft -10, the IT Wallet specification considers SD-JWT VC draft -11 (`SD-JWT-VC`_) to be in line with the version identified in `OpenID4VCI`_.

SD-JWT defines how a Holder can present a Digital Credential to a Relying Party, proving the legitimate possession of the Digital Credential. To do this, the Holder MUST include the ``KB-JWT`` in the SD-JWT by appending the ``KB-JWT`` at the end of the SD-JWT (:ref:`WP_093b <wallet-credential-presentation-testcases>`), as represented in the example below

.. code-block:: text

  <Issuer-Signed-JWT>~<Disclosure 1>~<Disclosure 2>~...~<Disclosure N>~<KB-JWT>

To validate the signature on the Key Binding JWT, the Relying Party MUST use the key material included in the Issuer-Signed-JWT. The Key Binding JWT (KB-JWT) signature validation MUST use the public key included in the SD-JWT, using the cnf parameter contained in the Issuer-Signed-JWT.

When an SD-JWT is presented, its KB-JWT MUST contain the following parameters in the JWT header (:ref:`WP_093c <wallet-credential-presentation-testcases>`):

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Claim**
    - **Description**
  * - **typ**
    - REQUIRED. MUST be ``kb+jwt``, which explicitly types the Key Binding JWT as recommended in Section 3.11 of :rfc:`8725`.
  * - **alg**
    - REQUIRED. Signature Algorithm using one of the specified in the Section :ref:`algorithms:Cryptographic Algorithms`.

When an SD-JWT is presented, the KB-JWT signature MUST be verified by the same public key included in the SD-JWT within the `cnf` parameter. The KB-JWT MUST contain the following parameters in the JWT payload:

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Claim**
    - **Description**
  * - **iat**
    - REQUIRED. The value of this claim MUST be the time at which the Key Binding JWT was issued, using the syntax defined in :rfc:`7519`.
  * - **aud**
    - REQUIRED. The intended receiver of the Key Binding JWT. The value of this parameter MUST match the Relying Party unique entity identifier.
  * - **nonce**
    - REQUIRED. Ensures the freshness of the signature. The value type of this claim MUST be a string. The value MUST match with the one provided in the request object.
  * - **sd_hash**
    - REQUIRED. The base64url-encoded hash digest over the Issuer-signed JWT and the selected disclosures.
  * - **transaction_data_hashes**
    - CONDITIONAL. REQUIRED when the request includes ``transaction_data``. Non-empty array of base64url-encoded hashes. Each hash is computed over the exact string value of the corresponding ``transaction_data`` item.
  * - **transaction_data_hashes_alg**
    - CONDITIONAL. REQUIRED only if the request included ``transaction_data_hashes_alg``. String naming the hash algorithm actually used to compute ``transaction_data_hashes``; if that parameter was not provided, the hash function MUST be ``sha-256``.


Authorization Response Errors
-----------------------------

There are cases where the Wallet Instance cannot validate the Request Object or the Request Object results invalid. This error occurs if the Request Object is successfully fetched from the url provided in the parameter ``request_uri`` but fails the validation checks. This could be due to incorrect signatures, malformed claims, or other validation failures, such as the revocation of the Relying Party.

If the Wallet Instance encounters any such errors during the evaluation of the Authorization Request, it MUST notify the Relying Party by sending an Authorization Error Response (:ref:`WP_090 <wallet-credential-presentation-testcases>`).
The Wallet Instance sends the Authorization Error Response to the Relying Party ``response_uri`` endpoint using an HTTP POST request (:ref:`WP_090 <wallet-credential-presentation-testcases>`).
The Authorization Error Response MUST be encoded in the request body using the format defined by the ``application/x-www-form-urlencoded`` content type.

Below is a non-normative example of an Authorization Error Response.

.. code-block:: http

  POST /response_uri HTTP/1.1
  HOST: relying-party.example.org
  Content-Type: application/x-www-form-urlencoded

  state=3be39b69-6ac1-41aa-921b-3e6c07ddcb03&
  error=invalid_request&
  error_description=...

.. warning::
  The current OpenID4VP specification outlines various error responses that a Wallet Instance may return to the Relying Party (Verifier) in case of faulty requests. For privacy enhancement, Wallet Instances SHOULD NOT notify the Relying Party of faulty requests in certain scenarios. This is to prevent any potential misuse of error responses that could lead to gather information that could be exploited.

In the following table are listed error codes and descriptions that are supported for the Authorization Error Response:

.. list-table::
   :class: longtable
   :widths: 20 60
   :header-rows: 1

   * - **Error Code**
     - **Description**
   * - ``invalid_request_uri``
     - The `request_uri` in the authorization request returns an error, contains invalid data, or is otherwise malformed. :rfc:`9101`
   * - ``vp_formats_not_supported``
     - The Wallet Instance does not support any of the vp formats required by the Relying Party. `OpenID4VP`_
   * - ``invalid_request_uri_method``
     - The value of the ``request_uri_method`` parameter is neither ``get`` nor ``post``. `OpenID4VP`_
   * - ``invalid_request``
     - The request is malformed or inconsistent (e.g., it uses the ``vp_token`` Response Type but it does not include a ``dcql_query`` parameter), the Client Identifier Prefix is unsupported, or requirements of a prefix are violated (e.g., ``client_id`` with the ``x509_hash`` prefix without the required ``client_metadata``). `OpenID4VP`_
   * - ``access_denied``
     - The Wallet did not have the requested credential, the User did not consent, or the Wallet failed to authenticate the User. `OpenID4VP`_
   * - ``invalid_client``
     - The Relying Party’s metadata has been resolved based on the Client Identifier (using the ``openid_federation`` or ``x509_hash`` prefix), but cannot be authorized due to trust validation failures or is not a valid participant of the federation. `OID-FED`_ and `OpenID4VP`_
   * - ``invalid_transaction_data``
     - One or more objects in the ``transaction_data`` structure are invalid. For instance, those objects contain unknown or unsupported types, malformed (e.g., it is an object of a known type but containing unknown fields or contains fields of the wrong type for the transaction data type) or missing fields, invalid values (e.g., the ``credential_ids`` does not match), or references to unavailable Credentials. `OpenID4VP`_

Relying Party Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As defined in Section 8.2. (Response Mode ``direct_post``) of the `OpenID4VP`_ specification, if the Response URI has successfully processed the Authorization Response or Authorization Error Response, it MUST respond with an HTTP status code of 200 with ``Content-Type`` of ``application/json`` and a JSON object in the response body.

In the **Same Device Flow**, the Relying Party MUST add the ``redirect_uri`` parameter to the JSON object in the response body. Upon receiving the ``redirect_uri``, the Wallet Instance MUST perform a redirect to the URL specified by the ``redirect_uri``.
This redirect allows the Relying Party to seamlessly resume interaction with the User on the device which initiated the flow, after the Wallet Instance has transmitted the Authorization Response to the designated ``response_uri``.

The Relying Party MUST include a response code within the ``redirect_uri``. The response code is a fresh, cryptographically random number used to ensure only the receiver of the redirect can fetch and process the Authorization Response. The number could be added as a path component, as a parameter or as a fragment to the URL. It is RECOMMENDED to use a cryptographic random value of 128 bits or more at the time of the writing of this specification.
Even if an adversary manages to steal the random value used in the request to the status endpoint, their user-agent would be rejected due to the missing cookie in the request.

.. warning::

  For security reasons and to prevent endpoint mix-up attacks, the value contained in the ``redirect_uri`` parameter MUST be one of those attested by a trusted third party, such as those provided in the ``openid_credential_verifier`` metadata within the ``redirect_uris`` parameter, obtained from the Trust Chain about the Relying Party (:ref:`WP_094a <wallet-credential-presentation-testcases>`).

Relying Party Response Errors
--------------------------------

If any validation check, performed by the Relying Party on the Authorization Response from the Wallet Instance, fails; the Response URI endpoint MUST return an error response. The structure of this error response should be determined by the specific nature of the error encountered. The response MUST use ``application/json`` as the content type and MUST include the following parameters:

* ``error``: The error code.
* ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

The following table lists the HTTP Status Codes and related error codes that MUST be supported for the error response:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **Error Code**
      - **Description**
    * - ``400 Bad Request``
      - ``invalid_request``
      - The response cannot be processed because it is missing required parameters, contains invalid parameters or is otherwise malformed.
    * - ``400 Bad Request``
      - ``invalid_request``
      - The Credentials presented are malformed, invalid or revoked.
    * - ``400 Bad Request``
      - ``invalid_request``
      - The credential presentation, contained in the ``vp_token`` object, is malformed, doesn't have the required parameters or is incorrectly formatted.
    * - ``400 Bad Request``
      - ``invalid_request``
      - The "sd-jwt" returned is malformed, missing required parameters or incorrectly formatted.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The signature of the KB-JWT is invalid or does not match the associated public key (JWK) referenced in the Issuer signed SD-JWT.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The nonce value provided is incorrect or otherwise malformed.
    * - ``403 Forbidden``
      - ``invalid_request``
      - Trust could not be established with the Credential Issuer.
    * - ``500 Internal Server Error``
      - ``server_error``
      - The request cannot be fulfilled because the Response URI Endpoint encountered an internal problem.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The request cannot be fulfilled because the Response URI Endpoint is temporarily unavailable (e.g., due to maintenance or overload).

Below there are two examples of HTTP responses using ``application/json`` that include both the ``error`` and ``error_description`` members:

.. code-block:: http

  HTTP/1.1 403 Forbidden
  Content-Type: application/json

  {
    "error": "invalid_request",
    "error_description": "Trust cannot be established with the issuer: https://issuer.example.com"
  }


.. code-block:: http

  HTTP/1.1 400 Bad Request
  Content-Type: application/json

  {
    "error": "invalid_request",
    "error_description": "The vp_token is malformed, missing required parameters or incorrectly formatted"
  }


Status Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This specification introduces the Relying Party Status Endpoint for implementations that choose to use it. This endpoint is an internal security feature of the implementation and is not required for interoperability.

Whether the flow is Same Device or Cross Device, the user-agent needs to check the session status at the endpoint made available by the Relying Party (status endpoint).
This check MAY be implemented in the form of JavaScript code, within the page that shows the QRCode or the href button pointing to the request URL.
The JavaScript code makes the user-agent check the status endpoint using either a polling strategy (in seconds) or a push strategy (e.g., WebSocket).

Since the HTML page and the status endpoint are implemented by the Relying Party, the implementation details of this solution are the responsibility of the Relying Party, as this is related to the Relying Party's internal API. However, the text below describes an example implementation.

The Relying Party binds the request of the user-agent, with a session cookie marked as ``Secure`` and ``HttpOnly``, with the issued request.
The request url SHOULD include a parameter with a random value. The HTTP response returned by this status endpoint MAY contain the HTTP status codes listed below:

* **201 Created**. The signed Request Object was issued by the Relying Party that waits to be downloaded by the Wallet Instance at the ``request_uri`` endpoint.
* **202 Accepted**. This response is given when the signed Request Object was obtained by the Wallet Instance.
* **200 OK**. The Wallet Instance has provided the presentation to the Relying Party's ``response_uri`` endpoint and the User authentication is successful. The Relying Party updates the session cookie allowing the user-agent to access to the protected resource. A redirect URL is provided carrying the location where the user-agent is intended to navigate.

Status Endpoint Errors
------------------------

If instead any validation check performed by the Relying Party fails, the QRCode page SHOULD be updated with an error message. Moreover, the status endpoint MUST return an error response, whose structure depends on the nature of the error. The response MUST use ``application/json`` as the content type and MUST include the following parameters:

* ``error``: The error code.
* ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

The following table lists the HTTP Status Codes and related error codes that MUST be supported for the error response:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **Error Code**
      - **Description**
    * - ``401 Unauthorized``
      - ``authentication_failed``
      - The Wallet Instance or its User have rejected the request, the request is expired, or other errors prevented the authentication.
    * - ``403 Forbidden``
      - ``invalid_session``
      - Either the session id provided in the request is invalid.


Redirect URI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The ``redirect_uri`` value MUST be used with an HTTP method GET by the user-agent to redirect the User to a specific Relying Party's endpoint in order to complete the process.


Redirect URI Errors
-----------------------------

When the user-agent is redirected to the Redirect URI provided by the Relying Party, several errors may occur that prevent the successful completion of the process. These errors are critical as they directly impact the User experience by hindering the seamless flow of information between the Wallet Instance and the Relying Party. Handling these errors requires clear communication to the User within the returned navigation web page. Relying Party MUST implement the error handling and validation mechanisms for Redirect URIs defined in this specification. Below are potential errors related to the Redirect URI, the error response MUST use ``application/json`` as the content type and MUST include the following parameters:

    - ``error``: The error code.
    - ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

The following table lists the HTTP Status Codes and related error codes that MUST be supported for the error response:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **Error Code**
      - **Description**
    * - ``403 Forbidden``
      - ``invalid_request``
      - The Redirect URI provided by the Relying Party does not match any of the URIs linked with the User session. (:rfc:`6749#section-4.1.2.1`)
    * - ``403 Forbidden``
      - ``invalid_request``
      - The User session is invalid or expired.
    * - ``500 Internal Server Error``
      - ``server_error``
      - The request cannot be fulfilled due to an internal server error. (:rfc:`6749#section-4.1.2.1`).
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The request cannot be fulfilled because the service is temporarily unavailable (e.g., due to maintenance or overload). (:rfc:`6749#section-4.1.2.1`).


