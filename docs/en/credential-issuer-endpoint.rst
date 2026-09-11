.. include:: ../common/common_definitions.rst
.. Included via endpoints.rst at title level '-' (level 1).

.. role:: raw-html(raw)
  :format: html

Credential Issuer Endpoints
---------------------------

Metadata Endpoints
^^^^^^^^^^^^^^^^^^^^

The Credential Issuers MUST provide an Entity Configuration through the ``/.well-known/openid-federation`` endpoint, according to Section :ref:`infrastructure-trust:Entity Configuration`. Technical details are provided in Section :ref:`credential-issuer-entity-configuration:Credential Issuer Entity Configuration`.

Alternatively the Credential Issuer's Metadata can be retrieved using the Credential Issuer Identifier. The Metadata document MUST be made available in JSON and JWT format through the ``/.well-known/openid-credential-issuer`` endpoint as defined in Section 12.2.2 of `OpenID4VCI`_.

The ``Accept-Language`` header in the HTTP GET request can be used to indicate the language(s) preferred.
In this case the Credential Issuer can send a subset of the metadata containing internationalized display data for one or all of the requested languages and indicate returned languages using the HTTP ``Content-Language`` Header.

Below is a non-normative example.

.. code-block:: http

    GET /.well-known/openid-credential-issuer HTTP/1.1
    Host: issuer.example.com
    Accept: application/json
    Accept-Language: it-IT, it;q=0.9

.. code-block:: http

    GET /.well-known/openid-credential-issuer HTTP/1.1
    Host: issuer.example.com
    Accept: application/jwt
    Accept-Language: it-IT, it;q=0.9

The Credential Issuer MUST respond with HTTP Status Code 200 and return the Credential Issuer Metadata containing:

- the parameters defined in :ref:`credential-issuer-metadata:Metadata for openid_credential_issuer` as an unsigned JSON document using the media type *application/json*.

          or

- the header and payload parameters defined in Section 12.2.3 of `OpenID4VCI`_ in addition to those defined in :ref:`credential-issuer-metadata:Metadata for openid_credential_issuer` as a signed JSON Web Token using the media type *application/jwt*.

Below is a non-normative example of Credential Issuer metadata in signed form:

.. literalinclude:: ../../examples/credential-issuer-metadata.txt
  :language: text

The ``authorization_servers`` entries of the Credential Issuer Metadata can be used to obtain the Authorization Server metadata from the Oauth Authorization Server ``/.well-known/oauth-authorization-server`` as defined in Section 3 of :rfc:`8414`.
In case the ``authorization_servers`` parameter is omitted, the Credential Issuer's identifier can be used to retrieve the Authorization Server metadata.

Below is a non-normative example.

.. code-block:: http

    GET /.well-known/oauth-authorization-server HTTP/1.1
    Host: oauth-authorization-server.example.com

The Oauth Authorization Server MUST respond with HTTP Status Code 200 and return the Oauth Authorization Server Metadata containing the parameters defined in :ref:`credential-issuer-metadata:Metadata for oauth_authorization_server`, using a JSON document with the media type *application/json*.

Credential Issuance Endpoints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: credential-issuance-endpoint.rst

e-Service PDND Credential Issuer Catalog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Credential Issuers MUST provide the following e-services through PDND to:

  - provide statistics about issued Credentials


Get Statistics
""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Description**
    - This service returns statistical data on issued Digital Credentials.
  * - **Provider**
    - Credential Issuer
  * - **Consumer**
    - Authorized Third Party


