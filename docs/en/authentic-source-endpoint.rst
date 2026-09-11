.. include:: ../common/common_definitions.rst
.. Included via endpoints.rst at title level '-' (level 1).


.. role:: raw-html(raw)
  :format: html

Authentic Source Endpoints
--------------------------

e-Service PDND Authentic Source Catalog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Public Authentic Sources MUST provide the following e-Service through PDND to provide the Credential Issuer with User's attributes required to the issuance of a Digital Credential.

The e-service is described via an OpenAPI definition where the request, response, and error messages are detailed.

.. only:: html

  .. note::
    The base OpenAPI Specification is available :raw-html:`<a href="OAS3-PDND-AS.html" target="_blank">here</a>`.
    This OpenAPI specification can be extended by the Authentic Sources, in fact, the array ``attributeClaims`` MAY contain additional properties specific to a particular Credential. These additional properties, as defined in the OpenAPI specification, will be inserted into the Credential by the Credential Issuer.

.. only:: latex

  .. note::
    The base OpenAPI Specification is available :ref:`e-service-pdnd-template:Authentic Source PDND OpenAPI Specification`.
    This OpenAPI specification can be extended by the Authentic Sources, in fact, the array ``attributeClaims`` MAY contain additional properties specific to a particular Credential. These additional properties, as defined in the OpenAPI specification, will be inserted into the Credential by the Credential Issuer.

Get Attribute Claims
""""""""""""""""""""

.. _table_authentic-source-endpoint-get-attribute-claims:
.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Description**
    - This e-Service provides the Credential Issuer with all attribute claims necessary for the issuance of a Digital Credential.
  * - **Provider**
    - Authentic Source
  * - **Consumer**
    - Credential Issuer

This e-Service MUST be invoked by the Credential Issuer in the following cases:

  - During the Credential issuance flow to retrieve the Digital Credential dataset(s). In this situation, the ``object_id`` claim MUST NOT be used in the e-service request payload, and the e-service response MUST include all Credential datasets that are ``VALID`` state and not administratively expired (i.e., ``expiry_date`` > current date of the e-service request).
  - After receiving an update notification through Signal Hub. In this situation, the ``object_id`` claim MUST be included in the request payload, and the e-service response MUST return only the Credential dataset identified by the ``object_id`` claim independently from its state.

.. note::
  The Authentic Source and the Credential Issuer MUST implement the necessary logic to keep track of the requests and responses exchanged via this e-Service, in order to be able to correlate them with the related issuance of a Digital Credential. In particular,
    - both MUST save the ``object_id`` value in the payload of the response to manage Signals related to the deferred issuance of a Digital Credential (see :ref:`signal-hub-endpoint:Signals Processing`). Any subsequent notification related to a specific dataset MUST be handled via ``object_id``.
    - the Authentic Source MUST record the datetime value provided within the ``last_updated`` parameter, which indicates the last time the User's attributes were updated in the Authentic Source's database;
    - the Credential Issuer MUST read the ``last_updated`` value received in the response to be able to check if the User's attributes have changed since the last issuance of a Digital Credential.

Credential Lifecycle States Mapping
""""""""""""""""""""""""""""""""""""""""""

To ensure consistency between the "Electronic Attestation Lifecycle" documented in :ref:`credential-revocation:Digital Credential Lifecycle` and the OpenAPI status Enum, the following mapping and operational logic MUST be applied for the ``status`` field in the ``attributeClaims``.

**Directionality and Responsibility:**
State changes of a Digital Credential at the Credential Issuer level DO NOT imply a change at the Authentic Source. Conversely, any state change of a dataset at the Authentic Source MUST be processed by the Credential Issuer to update the technical Digital Credential status.

**Operational Guidance:**

* **Technical vs Administrative Validity**: Digital Credentials distinguish between a **technical validity** set by the Credential Issuer (claims ``iat`` and ``exp``) and an **administrative validity** determined by the Authentic Source (claims ``issuance_date`` and ``expiry_date``).
* **Expiry Hierarchy**: The technical expiry (``exp``) MUST NOT be later than the administrative expiry (``expiry_date``). For example, a driver's license may be administratively valid for 10 years, while the issued Digital Credential may have a technical expiry of 1 year.
* **Re-issuance**: If a Digital Credential reaches its technical expiry (``exp``) but the dataset is still administratively valid, the OpenAPI status remains ``VALID``, allowing the Digital Credential to be re-issued multiple times within the administrative timeframe.
* **Metadata Verification**: The Credential Issuer MUST verify the effective usability by checking both the technical claims and the administrative dates.
* **Irreversibility**: After a transition to ``INVALID``, the Digital Credential cannot return to a ``VALID`` state. A new issuance is required for a new dataset. This applies to both explicit revocation and administrative expiry.
* **Signal Processing**: Signals MUST be processed sequentially. If a Signal invalidates a Digital Credential, subsequent correction Signals for the same object are ignored.

**Status Mapping and Case Logic:**

The Credential Issuer MUST update the Digital Credential ``status`` based on Signals received from the Authentic Source via Signal Hub (``signalType=UPDATE``):

* **Revocation**: If a dataset is revoked at the Authentic Source (status ``INVALID``), the Credential Issuer MUST revoke the Digital Credentials that use that dataset (status transition from ``VALID/SUSPENDED`` to ``INVALID``).
* **Suspension**: If a dataset is suspended at the Authentic Source (status ``SUSPENDED``), the Credential Issuer MUST suspend the Digital Credentials (status transition from ``VALID`` to ``SUSPENDED``).
* **Restoration**: If a suspended dataset returns to ``VALID`` at the Authentic Source, the Credential Issuer MUST restore the Digital Credential validity (status transition from ``SUSPENDED`` to ``VALID``).
* **Modification**: If a dataset is modified but remains ``VALID`` at the Authentic Source, the Credential Issuer—detecting the change via the ``last_updated`` field—assigns the technical status ``ATTRIBUTE_UPDATE`` to the Digital Credential. This triggers a re-issuance flow when the Wallet Instance checks the status.
* **Administrative Expiry**:
    * **Scenario A (Metadata-driven)**: If ``expiry_date`` was shared with the Credential Issuer in metadata, the Authentic Source DOES NOT send Signals upon expiry; the Credential Issuer manages the lifecycle independently ensuring technical ``exp`` <= ``expiry_date``.
    * **Scenario B (Signal-driven)**: If ``expiry_date`` is NOT present in metadata and the dataset expires, the Authentic Source MUST set its status to ``INVALID`` and send a Signal via Signal Hub; the Credential Issuer then revokes the Digital Credentials (status transition to ``INVALID``).

Example of Authentic Source response
"""""""""""""""""""""""""""""""""""""

The endpoint response MUST use the HTTP Content-Type set to ``application/json``. Below is a concrete example with fictitious data to clarify the expected shape and content.

.. literalinclude:: ../../examples/credential-claims-response-example.json
  :language: json
  :caption: Example of the response JSON payload (Get Attribute Claims)

In summary:

- **userClaims**: user identity data (first name, family name, date/place of birth, tax id or personal administrative number). At least one of ``tax_id_code`` and ``personal_administrative_number`` is required when providing user claims.
- **attributeClaims**: array of datasets; each element **MUST** contain ``object_id``, ``status`` (VALID | INVALID | SUSPENDED), ``last_updated`` (ISO 8601 format), plus any dataset-specific attributes (e.g. ``nationality``, ``residence_address``).
- **metadataClaims**: array of metadata per dataset (``object_id`` required; ``issuance_date`` and ``expiry_date`` optional).
- **interval**: required when the request does not include a ``claims`` parameter; indicates the number of seconds to wait before repeating the request (e.g. 864000 = 10 days).

The successful response (HTTP 200) returns a ``CredentialClaimsResponse`` object formatted as a **JSON Payload**, accompanied by the ``Agid-JWT-Signature`` and ``Digest`` integrity headers.

Signature Verification and Key Management
'''''''''''''''''''''''''''''''''''''''''

The Credential Issuer (Consumer) MUST verify the integrity and authenticity of the JSON response by validating the ``Agid-JWT-Signature`` and ``Digest`` headers received from the Authentic Source.

The signature verification and key retrieval process MUST strictly follow the **INTEGRITY_REST_02** standard pattern defined for **PDND e-Services**.
Please refer to the Technical Appendix (Section :ref:`e-service-pdnd:e-Service PDND`) for details on JWT signature validation and specifications for retrieving the Provider's public key via the Interoperability API.

.. warning::
  Alternative mechanisms for distributing cryptographic material (e.g., public ``.well-known`` endpoints directly exposed by the Authentic Source or *out-of-band* distribution) are not allowed. Trust management MUST remain centralized within the perimeter of the PDND infrastructure as described in the references cited above.


