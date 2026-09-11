.. include:: ../common/common_definitions.rst
.. Included via trust-evaluation.rst at title level '-' (level 1).

Trust Evaluation in the EUDIW Trust Framework
------------------------------------------------

The procedures defined in this section profile combine the following external specifications.

- `ETSI TS 119 615`_ and `ETSI TS 119 612`_, which define the procedure and the data structures for authenticating and interpreting the List of Trusted Lists and the Member State Trusted Lists, applied here to the Lists of Trusted Entities.
- `ETSI EN 319 102-1`_ and `ETSI TS 119 182-1`_, which define, respectively, the validation of AdES signatures and the JAdES format of the signature of a List of Trusted Entities.
- `ETSI TS 119 411-8`_, `ETSI TS 119 475`_ and `ETSI EN 319 412-1`_, which define, respectively, the Wallet-Relying Party Access Certificate, the Wallet-Relying Party Registration Certificate together with its entitlements, and the certificate subject attributes.
- `ETSI TS 119 472-2`_ and `ETSI TS 119 472-3`_, which profile the Presentation and the Issuance protocols respectively, through which a Wallet-Relying Party is authenticated and its registration information is made available to the Wallet Unit; the latter also defines the Embedded Disclosure Policy.
- IETF RFC 5280 (:rfc:`5280`) and IETF RFC 6960 (:rfc:`6960`), which define the X.509 certification path validation and the Online Certificate Status Protocol.

.. note::

    The data model of the Trust Artifacts referenced by these procedures, together with the specifications that define them, is defined in :ref:`infrastructure-trust:EUDIW Trust Artifacts`.

    The procedures defined in this section are executed within the operational Issuance and Presentation flows (see :ref:`digital-credential-flows:Digital Credential Flows`).
    The parameters they operate on, such as the signed Request Object, the mdoc Request, the Metadata of all Entities involved and the data model of the received Digital Credentials, are defined in the respective sections (see :ref:`entities:Entities`, :ref:`remote-flow:Request Object` for the Remote Flow, :ref:`proximity-flow:mdoc Request` for the Proximity Flow, and :ref:`credential-data-model:SD-JWT-VC Credential Format` and :ref:`credential-data-model:mdoc-CBOR Credential Format` for the Digital Credential formats).

EUDIW Trust Evaluation Processes by Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The procedures are defined in a general form, with a Trust Evaluator and a Trust Evaluated Party, and the following table defines which entity acts in which role, when and for which purpose.

.. _table_eudiw_tf_roles:
.. list-table:: Trust Evaluation Processes by Entity and Context in the EUDIW Trust Framework
    :class: longtable
    :widths: 12 20 34 34
    :header-rows: 1

    * - **Entity**
      - **Context**
      - **As Trust Evaluator, implements**
      - **As Trust Evaluated Party, provides**
    * - Wallet Unit
      - Issuance of a Credential in the EU catalogue
      - On the Credential Issuer:

        - :ref:`trust-evaluation:EUDIW Authentication`
        - :ref:`trust-evaluation:EUDIW Authorization`
        - :ref:`trust-evaluation:EUDIW Metadata Retrieval and Validation`

        On the received Credential:

        - :ref:`trust-evaluation:EUDIW Attestation Signature Validation`
      - The Wallet Instance Attestation, validated against the Wallet Providers List of Trusted Entities.
    * - Wallet Unit
      - Remote presentation, ``x509_hash`` prefix
      - On the Relying Party:

        - :ref:`trust-evaluation:EUDIW Authentication`
        - :ref:`trust-evaluation:EUDIW Authorization`
        - :ref:`trust-evaluation:EUDIW Metadata Retrieval and Validation`
      - No entity level artifact is required from the Wallet Unit.
    * - Wallet Unit
      - Proximity presentation
      - On the Relying Party:

        - :ref:`trust-evaluation:EUDIW Authentication`, based on the mdoc reader authentication
        - :ref:`trust-evaluation:EUDIW Authorization`
      - No entity level artifact is required from the Wallet Unit.
    * - Credential Issuer
      - Issuing Credentials in the EU catalogue
      - On the Wallet Unit:

        - :ref:`trust-evaluation:EUDIW Attestation Signature Validation`, applied to the Wallet Instance Attestation
      - The Wallet-Relying Party Access Certificate and its registration, that is its Register entry and, where issued, the Wallet-Relying Party Registration Certificate.
    * - Relying Party
      - Remote or proximity presentation
      - On the received Credentials:

        - :ref:`trust-evaluation:EUDIW Attestation Signature Validation`
      - The Wallet-Relying Party Access Certificate and its registration, that is its Register entry and, where issued, the Wallet-Relying Party Registration Certificate.
    * - Relying Party Intermediary
      - Presentation, on behalf of an intermediated Relying Party
      - It does not act as Trust Evaluator in the operational flows.
      - Its own Wallet-Relying Party Access Certificate and the registration of the intermediated Relying Party, that is its Register entry and, where issued, the Wallet-Relying Party Registration Certificate.

EUDIW Trust Anchor Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section specifies the **Trust Anchor Validation Process** that a Wallet Unit or Wallet-Relying Party uses to establish the cryptographic integrity and authenticity of a List of Trusted Entities, or a Trusted List, in order to:

- validate the trustworthiness of a Trust Anchor (see :ref:`infrastructure-trust:Trust Anchor Certificate Profile`) to authenticate, authorize or validate an entity or artifact during *runtime*.
- validate the information contained in the List for *historical purposes*.

Depending on the Trust Artifact or Attestation being verified, the Trust Evaluator MUST fetch, download, and validate the List which references the appropriate Trust Anchor:

1. *List of Trusted Entities* MUST be used to retrieve Trust Anchors for validating:

   - **WRPAC** in the Providers of WRPAC LoTE.
   - **WRPRC** in the Providers of WRPRC LoTE.
   - **Wallet Unit Attestation Sign/Seal Certificates** in the Wallet Providers LoTE.
   - **PID Sign/Seal Certificates** in the PID Providers LoTE.
   - **PuB-EAA Sign/Seal Certificates** in the PuB-EAA Providers LoTE.
   - **Registrar Sign/Seal Certificates** in the Registrar LoTE.

2. *Trusted Lists* are used to retrieve Trust Anchors for validating:

   - **QEAA Sign/Seal Certificates** in the corresponding Member State Trusted List.

3. For **PuB-EAA Sign/Seal Certificates**, the corresponding Member State Trusted List MUST be used to establish the qualified status of the issuing CA and certificate. It MUST NOT replace the Trust Anchor's listing in the PuB-EAA Providers LoTE.

To verify the authenticity of the retrieved Lists, the Entity MUST perform the following validations:

- :ref:`trust-evaluation:List of Trusted Entities Validation`: Validate the digital signature of the List of Trusted Entities by verifying it against the List of Trusted Entities Provider certificate.
  This certificate is published in the Official Journal of the European Union.
- :ref:`trust-evaluation:Trusted List Validation`: Validate the digital signature of the TL by verifying it against the corresponding Member State public keys published in the List Of Trusted Lists (LOTL).
  The List Of Trusted Lists (LOTL) itself is authenticated by validating its digital signature against the Official Journal of the European Union.

**Input**

The validating Entity MUST base Trust Anchor validation decisions only on information derived from:

- The Official Journal of the EU (OJEU) anchoring trust in the root certificates that signed the Lists of Trusted Entities and List of Trusted Lists.
  The current version of OJEU can be found `here <https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:C_202601944>`_.
- A validated Lists of Trusted Entities or List of Trusted Lists and Member State level Trusted Lists.

**Outcome**

Each validation procedure (defined in :ref:`trust-evaluation:List of Trusted Entities Validation` and :ref:`trust-evaluation:Trusted List Validation`) gives a granular verification result code when it detects a negative condition.
These codes feed into the final decision:

- If the validation algorithms terminate with:

    - ``LoTE-Status == LoTE_VERIFICATION_PASSED``, or
    - ``LOTL-Status == LOTL_VERIFICATION_PASSED``, or
    - ``EU-TL-Status == EU-TL_VERIFICATION_PASSED``;

    Then the List of Trusted Entities or Trusted List is valid and the Trust Anchor certificates (see :ref:`infrastructure-trust:Trust Anchor Certificate Profile`) therein MUST be considered trustworthy.

- If the validation algorithms terminate with:

    - ``LoTE-Status == LoTE_VERIFICATION_FAILED``, or
    - ``LOTL-Status == LOTL_VERIFICATION_FAILED``, or
    - ``EU-TL-Status == EU-TL_VERIFICATION_FAILED``;

    Then the List of Trusted Entities or Trusted List is not valid and the Trust Anchor certificates (see :ref:`infrastructure-trust:Trust Anchor Certificate Profile`) therein MUST NOT be considered trustworthy.

.. note::

    Within IT-Wallet, a Wallet Unit is expected to cache validated Lists of Trusted Lists, Lists of Trusted Entities and Member States' Trusted Lists, so that it does not retrieve them at every interaction.
    The frequency of updates and the types of lists to cache represent a trade-off between interoperability and resource utilization.

List Key Rotation and Historical Verification
"""""""""""""""""""""""""""""""""""""""""""""

To support continuous key rotation and regular updates, the LoTE and LOTL implement a *pivoting mechanism*.
This mechanism consists of publishing the most recent version of the List at the primary URI referenced in the Official Journal of the European Union, while archiving earlier versions at other distinct URIs called *pivots*.
Each List version is signed with a public key referenced within the immediately preceding pivot.
The last pivot is signed with the key referenced in the OJEU.
The newest List version explicitly contains the URIs where all historical versions are hosted.

An Entity validates this chain of pivots from the newest version back to the oldest by verifying that each subsequent artifact is correctly signed by the public key authorized in the prior version.
Final validation is achieved by verifying the trustworthiness of the oldest public key, either via a lookup in the OJEU or directly against a cached, previously validated version of the List.
This ensures that an entity possessing the last known valid version can reliably discover the next version and validate it via an unbroken chain of trust rooted in the OJEU.

While the pivoting mechanism enables continuous updates to LoTE parameters, certain updates may require adding a ``ServiceHistory`` object to the LoTE to preserve the historical keys and configurations needed to validate legacy signatures.
The specific scenarios in which an Entity update triggers a migration of its configuration into ``ServiceHistory`` are detailed in :ref:`infrastructure-trust:Trust Management and Lifecycle`.

Regardless of an Entity's objective when validating the LoTE (whether retrieving a current or historical configuration), the validation mechanism MUST strictly follow Section :ref:`trust-evaluation:List of Trusted Entities Validation`.

List of Trusted Entities Validation
"""""""""""""""""""""""""""""""""""

This section defines the validation of a List of Trusted Entities.
The List of Trusted Entities, its data model and the List of Trusted Entities types used within the EUDIW ecosystem, one for each category of notified provider, are defined in :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`.

A List of Trusted Entities is a signed list.
Its authenticity is rooted in the Official Journal of the European Union, and it supports continuous key rotation through the *pivoting mechanism* described in :ref:`trust-evaluation:List Key Rotation and Historical Verification`.
The Trust Anchors it publishes are provided in the ``ServiceDigitalIdentity`` of its trusted entity service entries, as defined in clause 6.6.3 of [`ETSI TS 119 602`_].

The authentication procedure below follows clause 4.1 of [`ETSI TS 119 615`_], which specifies the authentication of the EC compiled List of Trusted Lists (LOTL) with its pivot mechanism.
Here that procedure is applied to the List of Trusted Entities data model of [`ETSI TS 119 602`_] and to its JAdES signature ([`ETSI TS 119 182-1`_]), in place of the XML LOTL.
The variables used below are the List of Trusted Entities analogs of the LOTL variables preconfigured in clause 4.0 (GPR-4.0-02) of [`ETSI TS 119 615`_].
They correspond as follows:

- ``OJEU-LoTE-Loc`` corresponds to ``OJEU-LOTL-Loc``;
- ``OJEU-LoTE-Certs-Set`` corresponds to ``OJEU-LOTL-Certs-Set``;
- ``LoTESO-Cert`` corresponds to ``LOTLSO-Cert``;
- the ``PointersToOtherLoTE`` and ``SchemeInformationURI`` claims correspond to the *Pointers to other TSLs* (clause 6.3.13 of [`ETSI TS 119 602`_]) and *Scheme information URI* (clause 6.3.7) components.

**List of Trusted Entities Validation Algorithm**

The validating Entity initializes the following variables, corresponding to the parameters preconfigured in GPR-4.0-02 of [`ETSI TS 119 615`_] for the LOTL.

**Input Variables**:

- ``OJEU-Loc``: URI of the latest known Official Journal of the European Union publication.
- ``OJEU-LoTE-Loc``: URI of the last processed List of Trusted Entities.
  Defaults to the value in ``OJEU-Loc``.
- ``OJEU-LoTE-Certs-Set``: the set of trusted certificates from the ``OJEU-Loc`` publication.
- ``LoTE``: the List of Trusted Entities JWT currently being processed.
  Initialized as ``NULL``.
- ``LoTE-Signer-Cert``: the certificate extracted from the ``x5c`` header parameter of the List of Trusted Entities.
- ``LoTESO-Cert``: temporary variable for the Scheme Operator certificate being validated.
  Initialized as ``NULL``.
- ``LoTESO-Certs-Set``: trusted certificates extracted from the ``PointersToOtherLoTE`` claim (``SchemeTerritory`` ``EU``, clause 6.3.10 of [`ETSI TS 119 602`_]) of a List of Trusted Entities.

**Output Variables**:

- ``Authenticated-LoTE``: the validated JSON payload.
- ``LoTE-Status``: the validation result (e.g., ``LoTE_VERIFICATION_PASSED``).
- ``LoTE-Sub-Status``: detailed error codes.

**Process**:

The validation MUST perform the following steps.
Each step indicates the corresponding requirement of clause 4.1 of [`ETSI TS 119 615`_].

1. (Initialization) Download the JWT file from ``OJEU-LoTE-Loc`` and assign it to ``LoTE``.
   (PRO-4.1.4-01)
2. (Parsing) Extract the first certificate from the ``x5c`` header of ``LoTE`` and assign it to ``LoTE-Signer-Cert``.
   (PRO-4.1.4-02)
3. (Pivot Discovery) Iterate through the ``uriValue`` claims in the ``SchemeInformationURI`` component (clause 6.3.7 of [`ETSI TS 119 602`_]).
   Count the number of valid URIs preceding the URI matching ``OJEU-Loc`` and assign it to ``n``.
   (PRO-4.1.4-03 for the search of ``OJEU-Loc``, PRO-4.1.4-04 for the count of ``n``)

    - If no URI matches ``OJEU-Loc``: validation MUST fail with ``LoTE-Status`` set to ``LoTE_VERIFICATION_FAILED`` and ``LoTE-Sub-Status`` set to ``OJEU_LOCATION_INPUT_NOT_MATCHING_OJEU_LOCATION_IN_LoTE``.

4. (LoTE Location Conflict) Check the condition ``OJEU-LoTE-Loc != LoTE Location`` AND ``LoTE != Content at LoTE Location``, where ``LoTE Location`` is the ``LoTELocation`` URI in the ``PointersToOtherLoTE`` component of ``LoTE`` with ``SchemeTerritory`` ``EU`` (clause 6.3.13 of [`ETSI TS 119 602`_]).
   (PRO-4.1.4-05)

    - If ``TRUE``: validation MUST stop with ``LoTE-Status`` set to ``LoTE_VERIFICATION_FAILED`` and ``LoTE-Sub-Status`` set to ``LoTE_FILE_CONFLICT``.
    - If ``FALSE``, proceed to the next step.

5. (LoTE Freshness) Check the condition ``OJEU-LoTE-Loc == LoTE Location`` AND ``LoTE != Content at LoTE Location``.
   (PRO-4.1.4-06)

    - If ``TRUE``: set ``OJEU-LoTE-Loc`` to ``LoTE Location`` and restart from Step 1.
    - If ``FALSE``, proceed to the next step.

6. (Digital Signature Validation) Validate the signature of the current ``LoTE`` using the public key from ``LoTE-Signer-Cert`` as a directly trusted certificate, following the basic signature validation of [`ETSI EN 319 102-1`_] as required by PRO-4.1.4-07.
   In particular, the *Country code* and *Organization* fields in the Subject Distinguished Name of the certificate supporting the AdES digital signature shall match respectively the scheme territory and one of the scheme operator name values within the LoTE.
   (PRO-4.1.4-07, PRO-4.1.4-08, clause 6.8.0 of [`ETSI TS 119 602`_])

    - If validation fails: stop with ``LoTE-Status`` set to ``LoTE_VERIFICATION_FAILED`` and ``LoTE-Sub-Status`` set to ``LoTE_SIGNATURE_VERIFICATION_FAILED``.
    - If successful:

        - Set ``LoTESO-Cert`` to ``LoTE-Signer-Cert``.
        - Set ``LoTESO-Certs-Set`` to the certificates found in the ``PointersToOtherLoTE`` claim (scheme territory ``EU``) of the current ``LoTE`` payload.
          (PRO-4.1.4-09)

7. (Intermediate Pivot Validation) (PRO-4.1.4-10 for the case ``n = 0``, PRO-4.1.4-11 for the pivot loop)

    - Case ``n = 0`` (No Pivots): proceed directly to Step 8.
    - Case ``n != 0`` (History Chain):

        - Iterate ``i`` from 1 to ``n`` (from most recent Pivot to oldest).
          Let ``Pivot`` be the file downloaded from the ``i``-th URI.
        - (Link Check) Set ``Pivot-Certs-Set`` to the certificates in the ``PointersToOtherLoTE`` claim (territory ``EU``) of ``Pivot``.
          If ``LoTESO-Cert`` (the signer of the previous file in the chain) is not in ``Pivot-Certs-Set``, validation MUST fail with ``LoTE-Sub-Status`` set to ``PIVOT_i-1_SIGNER_CERT_NOT_AUTHENTICATED_BY_PIVOT_i``.
        - (Update Signer) Set ``LoTESO-Cert`` to the first certificate in the ``x5c`` header parameter of ``Pivot``.
        - (Verify Signature) Validate the signature of ``Pivot`` using ``LoTESO-Cert`` as described in step 6.
          (Digital Signature Validation).
          If it fails, validation MUST fail with ``LoTE-Status`` set to ``LoTE_VERIFICATION_FAILED`` and ``LoTE-Sub-Status`` set to ``PIVOT_i_SIGNATURE_VERIFICATION_FAILED``.
        - The loop continues, walking backwards until ``LoTESO-Cert`` represents the signer of the oldest Pivot.

8. (Trust Root Validation) Verify the end of the chain.
   If ``LoTESO-Cert`` (from the last Pivot, or from the current ``LoTE`` when no Pivot exists) is not in ``OJEU-LoTE-Certs-Set`` (the set of trusted certificates), validation MUST fail with ``LoTE-Sub-Status`` set to ``PIVOT_n_SIGNER_CERT_NOT_AUTHENTICATED_BY_OJEU``.
   (PRO-4.1.4-12)

9. (Expiration) If the current time is greater than the ``NextUpdate`` value of ``LoTE``, or it is set to ``NULL`` (clause 6.3.15 of [`ETSI TS 119 602`_]), validation MUST fail.
   (PRO-4.1.4-13)

10. (Success) Set ``Authenticated-LoTE`` to ``LoTE`` and ``LoTE-Status`` to ``LoTE_VERIFICATION_PASSED``.
    (PRO-4.1.4-14, PRO-4.1.4-15)

11. (Update Bookmark) If ``OJEU-LoTE-Loc`` does not match the ``LoTE Location`` in ``Authenticated-LoTE`` (scheme territory ``EU``), update ``OJEU-LoTE-Loc`` to that value.
    (PRO-4.1.4-16)

12. (Update Trust Root) [Caution: this step modifies the Root of Trust configuration] (PRO-4.1.4-17)

    - If ``OJEU-Loc`` does not match the first URI in ``SchemeInformationURI``, update ``OJEU-LoTE-Loc``.
    - Update ``OJEU-LoTE-Certs-Set`` according to the new set of trusted certificates, either in ``Authenticated-LoTE`` or from a new Official Journal of the European Union publication.

.. note::

    - Steps 4, 5 and 11 allow modifying the location of the List of Trusted Entities file without changing the initial trusted signer public key, as long as both the old and the new location have the same content, otherwise the validation fails with ``LoTE_FILE_CONFLICT``.
      This allows the List of Trusted Entities to be retrieved from different locations without affecting the Trust Anchor validation, as long as the content is the same.
    - In case of ``OJEU_LOCATION_INPUT_NOT_MATCHING_OJEU_LOCATION_IN_LoTE`` error, it is likely that the Official Journal of the European Union publication has been updated with a new location for the List of Trusted Entities.
      The validating Entity SHOULD repeat the validation process after downloading the most recent version of the Official Journal of the European Union.
    - In step 8, the validating Entity establishes the binding of the signer certificate of the ``LoTE`` with the certificate referenced in the Official Journal of the European Union, effectively using the latter as a source of trusted certificates.

Below is a flowchart summarizing the above steps for the validation of the List of Trusted Entities:

.. plantuml:: plantuml/lote-val-alg.puml
    :width: 99%
    :alt: The figure illustrates the Flowchart of the List of Trusted Entities Validation Algorithm.
    :caption: Flowchart of the List of Trusted Entities Validation Algorithm.

Below are listed the Sub-Status error codes of the List of Trusted Entities in tabular format.

.. list-table:: List of Trusted Entities Sub-Status Error Codes
   :class: longtable
   :widths: 38 10 52
   :header-rows: 1

   * - **Code**
     - **Phase**
     - **Meaning**
   * - ``OJEU_LOCATION_INPUT_NOT_MATCHING_OJEU_LOCATION_IN_LoTE``
     - both
     - No URI matches the expected ``OJEU-Loc`` within the ``SchemeInformationURI`` of the List of Trusted Entities.
       This typically implies that a newer version of the Official Journal of the European Union publication is available.
   * - ``LoTE_FILE_CONFLICT``
     - both
     - A location conflict is detected where the tracked List of Trusted Entities location differs from the active one, and the content across these files does not match.
   * - ``LoTE_SIGNATURE_VERIFICATION_FAILED``
     - both
     - The signature validation of the current List of Trusted Entities file failed using the extracted signer certificate, indicating potential tampering or corruption.
   * - ``PIVOT_i-1_SIGNER_CERT_NOT_AUTHENTICATED_BY_PIVOT_i``
     - both
     - The historical chain of trust is broken because the signing certificate of the previous pivot or file (i-1) is not found in the trusted certificate set of the succeeding pivot (i).
   * - ``PIVOT_i_SIGNATURE_VERIFICATION_FAILED``
     - both
     - The signature validation failed for an intermediate pivot file (i) within the historical chain.
   * - ``PIVOT_n_SIGNER_CERT_NOT_AUTHENTICATED_BY_OJEU``
     - both
     - The final certificate at the root of the pivot chain, or the current List of Trusted Entities signer when no pivot exists, is not found in the ``OJEU-LoTE-Certs-Set`` set of trusted certificates.

Trusted List Validation
""""""""""""""""""""""""

This section defines the validation of Trusted List.
In order to validate the Trusted List, the validating Ent MUST:

1. Validate the EU List of Trusted Lists using the algorithm described in section 4.1 of [`ETSI TS 119 615`_].
   If this fails, the validation stops and the Wallet Unit MUST consider the Entity it is interacting with as not trusted.
   The validation process is analogue to the :ref:`trust-evaluation:List of Trusted Entities Validation` except for the LOTL format which is always XML.
2. Parse the validated EU List of Trusted Lists to discover the necessary certificate to validate the relevant Member State Trusted List.
3. Obtain and validate the relevant Trusted List as described in section 4.2 of [`ETSI TS 119 615`_].

X509 Certificate Chain Validation Algorithm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This procedure validates the certification path.
It is invoked by the :ref:`trust-evaluation:EUDIW Authentication` and by the :ref:`trust-evaluation:Authorization Artifacts Validation` to validate the Wallet-Relying Party Access Certificate, the Wallet-Relying Party Registration Certificate and the Registrar Sign/Seal Certificate chains.
The Trust Anchor consumed as ``trust_anchor`` is profiled in :ref:`infrastructure-trust:Trust Anchor Certificate Profile`.

The certification path validation is the standard X.509 path validation defined in :rfc:`5280#section-6`, with the revocation status checking defined in :rfc:`5280` and :rfc:`6960`.
The certificate lifecycle and the revocation mechanisms, including the CRL and the OCSP formats and parameters, are defined in :ref:`infrastructure-trust:Revocation Mechanisms`.
The algorithm details are not redefined here.
This is the same certification path validation used in the National Trust Framework (see :ref:`trust-evaluation:X.509 Certificate Chain Validation`), where the difference is the origin of the trust anchor and the additional extraction of the Federation Entity Identifier.

Within the EUDIW Trust Framework the following applies.

  - The ``trust_anchor`` is the trusted certificate obtained from the ``ServiceDigitalIdentity`` component of the applicable, validated List of Trusted Entities (see :ref:`trust-evaluation:List of Trusted Entities Validation`) or Trusted List (see :ref:`trust-evaluation:Trusted List Validation`), that is the Provider of WRPAC LoTE for the Wallet-Relying Party Access Certificate, the Provider of WRPRC LoTE for the Wallet-Relying Party Registration Certificate, and the Registrar LoTE for the Registrar Sign/Seal Certificate.
  - The revocation status checking MAY be skipped for a certificate that carries both the ``noRevAvail`` and the ``ETSIValAssuredCertMod`` extensions (see :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`), whose status is then determined solely by its validity period.

.. note::

  As defined in :ref:`infrastructure-trust:Revocation Trust Anchors`, the Trust Anchor retrieved from the applicable LoTE or Trusted List is the notified Trust Anchor for the corresponding certificate chain. The same Trust Anchor MUST be used to validate the signatures of CRLs or OCSP responses used for revocation checking, as specified in :rfc:`5280#section-6` and :rfc:`6960`.

**Input**

- ``path``: the sequence of ``n`` certificates ``C_1, ..., C_n`` provided by the Entity, where ``C_1`` is the first certificate of the chain and ``C_n`` is the end-entity certificate.
  For any ``i`` in ``1, ..., n-1``, ``C_i`` is the issuer of ``C_i+1``.
- ``trust_anchor``: the trusted certificate obtained from the ``ServiceDigitalIdentity`` of the validated List of Trusted Entities or Trusted List.
  It MUST contain the public key used to sign ``C_1``.
  Implementations MUST support both self-signed and non-self-signed Trust Anchor certificates.
- ``current_time``: the current date and time.

**Outcome**

- The validated end-entity certificate ``C_n``, or a failure.

**Process**

1. Build the certification path from the end-entity certificate ``C_n`` to the ``trust_anchor``.
2. Execute the path validation defined in :rfc:`5280#section-6`, using the ``trust_anchor`` as the trust anchor input of the algorithm and ``current_time`` as the validation time.
3. Verify the revocation status of the certificates in the path according to :rfc:`5280` and :rfc:`6960`, unless the check is skipped as described above.

If any step fails, the certification path MUST be considered invalid and the artifact signature MUST NOT be verified with the presented certificate chain.

EUDIW Attestation Signature Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This process validates the signature on an Attestation (Digital Credential or Wallet Instance Attestation) using the appropriate Sign/Seal Certificate as profiled in :ref:`infrastructure-trust:Entity Sign/Seal Certificate Profile`.
It is invoked during the issuance and presentation flows to validate the signature on the Attestation.

The process MUST be structured as follows:

- If the Attestation whose signature is being checked is a Digital Credential having a Trust Anchor referenced within a LoTE or Trusted List (i.e., a PID, PuB-EAA, QEAA), or is a Wallet Instance Attestation, then one of the following cases applies:

  - **Base Signature Validation**: Executed when the Attestation contains the Sign/Seal Certificate and the associated X.509 trust chain, and the Trust Anchor is present in the relevant LoTE (only for PID, WIA or PuB-EAA) or Trusted List (only for QEAA).

  - **Fallback Signature Validation**: Executed when the Attestation does not contain the Sign/Seal Certificate, which is instead directly attested as a Trust Anchor in the LoTE (only for PID or WIA).

- If the Attestation whose signature is being checked is a non-qualified EAA, then information regarding trust evaluation is governed by the corresponding Rulebook.

The **Base Signature Validation** is structured as follows:

**Input**

- The received Attestation and the signer certificate chain carried within it.
- The type of artifact (i.e., the Digital Credential type or Wallet Instance Attestation) used to select the applicable List of Trusted Entities or Trusted List.

**Outcome**

- The validated Attestation, or a validation failure.

**Process**

This process depends on the Attestation type:

- **PID** or **WIA**.
  
  1. Verify the Attestation signature with the Sign/Seal certificate provided in the Attestation.
  2. Select the applicable List of Trusted Entities according to the type of the received Attestation, validate it as defined in :ref:`trust-evaluation:List of Trusted Entities Validation`, and extract the appropriate Trust Anchor from the relevant Entity's ``ServiceDigitalIdentity`` field.
  3. Extract the Sign/Seal certificate chain from the Attestation and validate it against the obtained Trust Anchor, as defined in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`.

- **QEAA**.

  1. Verify the Attestation signature using the Sign/Seal certificate provided in the Attestation. For a QEAA, the qualified electronic signature or seal MUST be validated in accordance with Article 32 of [`EIDAS`_].
  2. Fetch the appropriate Trusted List according to the nationality of the Credential Issuer, validate it as defined in :ref:`trust-evaluation:Trusted List Validation`, and extract the appropriate Trust Anchor from the relevant Entity's ``ServiceDigitalIdentity`` field.
  3. Extract the signer certificate chain from the Attestation and validate it against the obtained Trust Anchor, as defined in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`.

- **PuB-EAA**.

  1. Verify the Attestation signature with the Sign/Seal Certificate provided in the Attestation. A qualified electronic signature MUST be validated in accordance with Article 32 of [`EIDAS`_]; where the Provider is a legal person using an electronic seal, Articles 37 and 40 apply.
  2. Fetch and validate the PuB-EAA Providers LoTE as defined in :ref:`trust-evaluation:List of Trusted Entities Validation`, match the Provider and its Sign/Seal Certificate with the relevant ``TrustedEntityList`` object, and extract its Trust Anchor.
  3. Extract the signer certificate chain from the Attestation and validate it against the Trust Anchor obtained from the LoTE, as defined in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`.
  4. Fetch the Member State Trusted List corresponding to the issuing CA, validate it as defined in :ref:`trust-evaluation:Trusted List Validation`, and establish the qualified status of the issuing CA and Sign/Seal Certificate.

.. note:: 

  In each of the above cases, for an Attestation in mdoc format, the Mobile Security Object carries the Document Signer certificate in the ``x5chain`` header, as defined in [`ISO18013-5`_]. For an Attestation in SD-JWT VC format, the issuer certificate chain is carried in the ``x5c`` header of the JOSE signature.

If **Base Signature Validation** results in failure, the Entity validating the Attestation MUST execute **Fallback Signature Validation** as follows:

.. warning::
  
  This process only applies to **PID** and **WIA** Attestation types.

**Input**

- The received Attestation.
- The type of artifact (i.e., the Digital Credential type or Wallet Instance Attestation) used to select the applicable List of Trusted Entities.

**Outcome**

- The validated Attestation, or a validation failure.

**Process**

1. Fetch the applicable List of Trusted Entities according to the type of Attestation, validate it as defined in :ref:`trust-evaluation:List of Trusted Entities Validation`, and extract the appropriate Trust Anchor from the relevant Entity's ``ServiceDigitalIdentity`` field.
2. Verify the Attestation signature directly using the validated Trust Anchor acting as the signer certificate.

.. warning::

   Although the IT Wallet specification requires the Trust Anchor certificates notified to the Commission and included in the LoTE to be *different* from the Sign/Seal Certificates of the related Entities, Clause 4.2 of [`ETSI TS 119 412-6`_] allows LoTE Trust Anchors to serve directly as Sign/Seal Certificates.
   In this case, these certificates MUST NOT be included in the Attestation, forcing the verification process to adhere to the **Fallback Signature Validation** procedure.
   To ensure interoperability, EUDIW Attestation Signature Validation implementations MUST support both validation mechanisms.

.. note::

  When verifiying signatures or seals made by historical keys, the same process applies albeit with the following difference: the Trust Anchor is retrieved from the `ServiceHistory.ServiceDigitalIdentity` element instead of the `ServiceInformation.ServiceDigitalIdentity` element.

If both **Base Signature Validation** and **Fallback Signature Validation** fail, the Attestation MUST NOT be considered as issued by a trusted Entity.

EUDIW Authentication
^^^^^^^^^^^^^^^^^^^^

The Authentication Process enables the Wallet Unit to authenticate a Wallet-Relying Party during an interaction.
It establishes trust by validating the Wallet-Relying Party X.509 certificate chain, from a trusted Provider of Wallet-Relying Party Access Certificate down to the presented Wallet-Relying Party Access Certificate, and by verifying that the Wallet-Relying Party possesses the corresponding private key.
The Wallet-Relying Party Access Certificate is profiled in :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`.

For the verification of the access certificate, the Wallet Unit MUST accept only the Trust Anchors published in the Lists of Trusted Entities of the Providers of Wallet-Relying Party Access Certificate notified by the Member States (see :ref:`trust-evaluation:List of Trusted Entities Validation`).

**Input**

The Authentication outcome MUST be based only on information derived from:

- the appropriate Trust Anchor obtained from a valid instance of the Provider of Wallet-Relying Party Access Certificate List of Trusted Entities;
- the X.509 certificate path terminating with the Wallet-Relying Party Access Certificate end-entity certificate;
- a Wallet-Relying Party signature over the artifact of the interaction, carrying the proof of possession of the private key referenced in the Wallet-Relying Party Access Certificate.

**Outcome**

The Wallet Unit MUST output a decision: the Wallet-Relying Party is either ``AUTHENTICATED`` or ``NON_AUTHENTICATED``.
If ``AUTHENTICATED``, the Wallet Unit proceeds in the interaction flow.
If ``NON_AUTHENTICATED``, the Wallet Unit MUST inform the User that the identity of the Wallet-Relying Party could not be verified and MUST stop the interaction, as the entity is not trustworthy.

**Process**

The Wallet Unit MUST verify the authenticity and integrity of the presented Wallet-Relying Party Access Certificate as follows:

1. **Retrieve the Trust Anchor**: obtain the entry of the Provider of Wallet-Relying Party Access Certificate from the validated List of Trusted Entities (see :ref:`trust-evaluation:List of Trusted Entities Validation`).
   To select the correct entry, match the ``issuer.organizationIdentifier`` of the first certificate of the chain, whose semantics are defined in clause 5.1.4 of [`ETSI EN 319 412-1`_], with the ``TrustedEntitiesList[].TrustedEntity.TETradeName`` of the List of Trusted Entities.
   The certificates in the ``TrustedEntityServices[].ServiceInformation.ServiceDigitalIdentity`` field constitute the Trust Anchor.

2. **Construct the Certification Path**: build a path starting from the Wallet-Relying Party Access Certificate presented by the Wallet-Relying Party (``C_1``) and ending with the certificate issued by the Provider of Wallet-Relying Party Access Certificate (``C_n``).
   The simplest path consists of a single certificate, where ``n = 1``.

3. **Execute Path Validation**: validate the certification path as defined in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`, using the Trust Anchor retrieved at step 1, as described in :ref:`trust-evaluation:Wallet-Relying Party Access Certificate Validation`.

4. **Verify the Signature**: use the public key of the validated Wallet-Relying Party Access Certificate to verify the Wallet-Relying Party signature over the artifact it signs in the specific interaction.
   The certificate chain and the signed artifact depend on the flow:

    - **Remote Flow**: the chain is carried in the ``x5c`` header of the Wallet-Relying Party signed Request Object, and the Relying Party is authenticated through the ``x509_hash`` Client Identifier Prefix, as defined in [`OpenID4VP`_] and [`OPENID4VC-HAIP`_].
    - **Proximity Flow**: the chain is carried in the mdoc reader authentication (``ReaderAuth``) signed by the Wallet-Relying Party, in the COSE ``x5chain`` header (label ``33``), as defined in [`ISO18013-5`_].
    - **Issuance Flow**: the chain is carried in the ``x5c`` header of the Wallet-Relying Party signed Credential Issuer Metadata, as defined in [`OpenID4VCI`_].

.. warning::

    A Wallet-Relying Party MUST distinguish between transient authentication (e.g., access control) and content commitment (non-repudiation).
    To prevent an attacker from disguising a legal commitment as a protocol nonce, the Wallet-Relying Party MUST NOT use the Wallet-Relying Party Access Certificate private key to sign arbitrary data that could be controlled by an external party.

Wallet-Relying Party Access Certificate Validation
"""""""""""""""""""""""""""""""""""""""""""""""""""

The Entity performing Wallet-Relying Party Access Certificate validation initializes the algorithm in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm` with the ``path`` and ``trust_anchor`` defined there.
The inputs are the following:

- ``C_n`` is the first certificate of the chain provided by the Wallet-Relying Party;
- ``C_1`` is the Wallet-Relying Party Access Certificate;
- ``trust_anchor`` is a certificate of the Provider of Wallet-Relying Party Access Certificate obtained from the List of Trusted Entities.

.. warning::

  As described in Section 6.1.1 of `OPENID4VC-HAIP`_ the Trust Anchor Certificate needed for the validation of the WRPAC MUST NOT be included in the certificate chain and MUST be always retrieved in the appropriate LoTE.

EUDIW Authorization
^^^^^^^^^^^^^^^^^^^

This section specifies the EUDIW Authorization Process that a Wallet Unit MUST execute to determine whether an interaction with a Wallet-Relying Party is allowed within the EUDI Wallet ecosystem.
The EUDIW Authorization Process MUST start only *after* the Wallet-Relying Party has been successfully authenticated according to :ref:`trust-evaluation:EUDIW Authentication`.
If the Wallet-Relying Party has not been authenticated, the EUDIW Authorization Process MUST NOT start.

The authorization data of a Wallet-Relying Party is carried by the Wallet-Relying Party Registration Certificate or, equivalently, by the Register Response.
Both are profiled in [`ETSI TS 119 475`_] and their data model is described in :ref:`infrastructure-trust:Register Open APIs`.

The EUDIW Authorization Process is split into:

- :ref:`trust-evaluation:Authorization Artifacts Validation`, which validates integrity and authenticity of the Trust Artifact carrying the authorization data; and
- :ref:`trust-evaluation:Authorization Validation`, which validates the information content of the validated artifact.
  In particular this validation covers:

    - **Issuance authorization**: determines whether a Credential Issuer is registered for the relevant role and authorized to issue the specific Digital Credential.
      This applies to PID, QEAA, PuB-EAA and EAA Providers operating within the EUDIW ecosystem.
    - **Presentation authorization**: determines whether a Relying Party request falls within its registered scope, whether an Embedded Disclosure Policy permits the disclosure, and whether the User approves.
      This applies to interactions involving both Relying Parties and Relying Party Intermediaries, across both Remote and Proximity Flows.

- :ref:`trust-evaluation:Authorization Decision and Override Rules`, which outputs an *Authorization Decision* expressed as ``AUTHORIZED`` or ``NOT_AUTHORIZED`` on the base of the Authorization Artifacts Validation and Authorization Validation results.
  Depending on the Flow type the User MAY *override* the Authorization Decision.

Within the *Authorization Validation*, the Wallet Unit MUST distinguish between the authenticated Wallet-Relying Party and the *Authorization Subject*, that is the entity whose authorization is being evaluated:

- During Issuance, the Authorization Subject is the Credential Issuer.
- During *direct* presentation, the Authorization Subject is the Relying Party.
- During *intermediated* presentation, the authenticated Wallet-Relying Party is the Relying Party Intermediary, while the Authorization Subject for the data request is the *intermediated Relying Party*, whose registered scope governs the request.
  The Relying Party Intermediary is itself a registered entity, and its authorization to act as an intermediary is established through the ``intermediary`` binding declared in the intermediated Relying Party authorization data (see the Binding verification below).

The Wallet Unit MUST support authorization-context resolution from both a Wallet-Relying Party Registration Certificate, where available, and the Register, where a Wallet-Relying Party Registration Certificate is not available or cannot be relied upon.
The substantive authorization logic MUST NOT change based on the data source.
Where both sources are available, the Wallet Unit MUST normalize both into the same internal authorization model before applying the rules.

Authorization Artifacts Validation
"""""""""""""""""""""""""""""""""""

The artifacts that carry the authorization data of an entity are the Wallet-Relying Party Registration Certificate and the Register Response.
Both carry equivalent information, in the JWT and CWT profiles defined in Section 5.2.1 of [`ETSI TS 119 475`_].
The Wallet Unit MUST support the validation of both and MUST validate at least one of the two.

Each validation procedure specifies its inputs, its processing logic and its output, a verification result code.
The result MAY be overridden by the User under the conditions detailed in :ref:`trust-evaluation:Authorization Decision and Override Rules`.

The validation flow depends on the availability of the Wallet-Relying Party Registration Certificate in the interaction.

- During the Presentation flow the Relying Party MAY convey the Wallet-Relying Party Registration Certificate by value:

    - in the ``verifier_info`` parameter of the Request Object, in the Remote Flow, as defined in [`ETSI TS 119 472-2`_] and Section 5.1 of [`OpenID4VP`_];
    - in the ``euWrprc`` member of ``requestInfo`` in the ISO ``DeviceRequest``, in the Proximity Flow, as defined in Section 5.3 of [`ETSI TS 119 472-2`_] and in [`ISO18013-5`_].

- During the Issuance flow the Credential Issuer conveys the authorization data in the Credential Issuer Metadata through the ``issuer_info`` array, as defined in Section 4.2.3 of [`ETSI TS 119 472-3`_].
  The array MAY contain a ``registration_cert`` element with the Wallet-Relying Party Registration Certificate by value, and MUST contain a ``registrar_dataset`` element with the registration information.
  The Embedded Disclosure Policy is distributed through the Credential Issuer Metadata within the ``credential_configurations_supported`` field, as defined in [`OpenID4VCI`_].

In case the Wallet-Relying Party Registration Certificate is not available, or its validation fails, the Wallet Unit MUST query the Register as described in :ref:`Register Query Validation <register-query-validation>`.
The Register Response provides the same authorization-relevant data as the Wallet-Relying Party Registration Certificate.
Each Registrar exposes an online service through the API described in :ref:`infrastructure-trust:Register Open APIs`.
When using this service the Wallet Unit SHOULD inform the User that an external query will be made.

**Wallet-Relying Party Registration Certificate Validation**

When a Wallet-Relying Party Registration Certificate is available, the Wallet Unit MUST validate it before relying on it:

1. **Format verification**: confirm that ``typ`` is ``rc-wrp+jwt`` in the Remote Flow, or ``rc-wrp+cwt`` in the Proximity Flow, as defined in Section 5.2.1 of [`ETSI TS 119 475`_].
2. **Algorithm verification**: verify that the signature algorithm is conformant, that is ``alg`` is neither ``none`` nor a deprecated algorithm.
3. **Signature validation**: verify that the Wallet-Relying Party Registration Certificate signature is valid.
4. **Trust Anchor validation**: validate the Providers of WRPRC LoTE (see :ref:`trust-evaluation:List of Trusted Entities Validation`) and retrieve the Trust Anchor from its ``TrustedEntitiesList.ServiceDigitalIdentity`` field.
5. **Path validation**: validate the Wallet-Relying Party Registration Certificate chain as defined in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`, using the ``trust_anchor`` obtained in the previous step. For the WRPRC, the Trust Anchor used for signature validation, certificate path validation, and revocation checking MUST be retrieved from the applicable service entry in the Providers of WRPRC LoTE (i.e., under the ``ServiceDigitalIdentity`` corresponding to the ``ServiceTypeIdentifier`` with value ``http://uri.etsi.org/19602/SvcType/WRPRC/Issuance``).
6. **Temporal validity**: check ``iat`` and ``exp`` if present.
7. **Status verification**: check the revocation status through the ``status`` field of the Wallet-Relying Party Registration Certificate, as defined in [`ETSI TS 119 475`_]:

   - fetch the SLT (see :ref:`infrastructure-trust:Token Status List (WRPRC Profile)`) at the URI specified by the WRPRC's ``status.status_list.uri`` member;
   - validate the SLT signing certificate chain as defined in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`, using the Trust Anchor retrieved from the applicable service entry in the Providers of WRPRC LoTE (i.e., under the ``ServiceDigitalIdentity`` corresponding to the ``ServiceTypeIdentifier`` with value ``http://uri.etsi.org/19602/SvcType/WRPRC/Revocation`` for the service provided by the Provider of WRPRC);
   - validate the SLT signature using the validated signing certificate chain, following :ref:`trust-evaluation:EUDIW Attestation Signature Validation`;
   - validate the SLT data model according to :ref:`infrastructure-trust:Token Status List (WRPRC Profile)`;
   - decompress the ``status_list.lst`` value, retrieve the one-bit entry corresponding to the WRPRC's ``status.status_list.idx`` member, and interpret ``0x00`` as ``VALID`` and ``0x01`` as ``INVALID``.

8. **Consistency check**: verify that the subject and the fields of the Wallet-Relying Party Registration Certificate are consistent with the interaction.

.. note::

   In Step 5 (**Path validation**), the Trust Anchor Certificate needed to validate the WRPRC MUST NOT be included in the certificate chain and MUST always be retrieved from the appropriate LoTE.

**Outcome**

- If all the steps succeed and the Wallet-Relying Party Registration Certificate is in the ``VALID`` state, the Wallet Unit MUST set ``authz_art_state`` to ``CERTIFICATE_VALID``.
- If any step fails, the Wallet Unit MUST set ``authz_art_state`` to ``CERTIFICATE_INVALID``.
  This is not a final authorization decision: it triggers :ref:`Register Query Validation <register-query-validation>` as fallback.

.. _register-query-validation:

**Register Query Validation**

When the Wallet-Relying Party Registration Certificate is not available or its validation has failed, the Wallet Unit MUST query the Register API:

1. **Extract the Registrar URL** from the Presentation Request, that is the ``verifier_info`` in the Remote Flow or the ``requestInfo`` in the Proximity Flow, or from the Credential Issuer Metadata, that is ``issuer_info[].registry_uri``, during Issuance.
2. **Connect** to the Registrar online service over HTTPS.
3. **Query** the service with the entity identifier and, optionally, the ``intended_use_id``.
   The entity identifier is the ``verifier_info[].data.identifier`` in the Remote Flow, the ``docRequest.itemsRequest[].requestInfo.EUWrpRegistrarInfo.identifier`` in the Proximity Flow, or the ``issuer_info[].data.identifier`` during Issuance.
4. **Format verification**: confirm that ``typ`` is ``jwt``, as defined in Section 5.2.1 of [`ETSI TS 119 475`_].
5. **Verify pertinence**: verify that the response pertains to the relevant Authorization Subject and intended use.
6. **Verify the response signature**: verify the Registrar signature using the Sign/Seal Certificate carried in the ``x5c`` claim of the response.
7. **Trust Anchor validation**: validate the Registrars List of Trusted Entities (see :ref:`trust-evaluation:List of Trusted Entities Validation`) and retrieve the Registrar Trust Anchor from its ``TrustedEntitiesList.ServiceDigitalIdentity`` field.
8. **Path validation**: validate the Registrar Sign/Seal Certificate chain as defined in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`, where ``C_1`` is the Registrar Sign/Seal Certificate, and the ``trust_anchor`` is the Trust Anchor obtained at the previous step.
9. **Normalize** the Register-derived data into the same internal model used for the Wallet-Relying Party Registration Certificate.

.. note::

    Even when the Relying Party requesting the presentation is a Relying Party Intermediary, the Presentation Request MUST carry the intermediated Relying Party data, as defined in [`ETSI TS 119 475`_].

**Outcome**

- If all the steps succeed, the Wallet Unit MUST set ``authz_art_state`` to ``REGISTER_VALID``.
- If any step fails, the Wallet Unit MUST set ``authz_art_state`` to ``FAILED``.

During Issuance only, the ``registrar_dataset`` data MAY be used as a further fallback, as advisory information only, and MUST NOT be presented to the User as verified.
In Step 8.
**Path Validation**, the Trust Anchor Certificate needed for the validation of the Registrar Sign/Seal Certificate MUST NOT be included in the certificate chain Register's response and MUST be always retrieved in the appropriate LoTE.

Authorization Validation
"""""""""""""""""""""""""""""

The Authorization Validation MUST follow the Authorization Artifacts Validation when ``authz_art_state == REGISTER_VALID`` or ``authz_art_state == CERTIFICATE_VALID``.
If ``authz_art_state == FAILED`` the Wallet Unit SHOULD NOT execute any Authorization Validation, as it cannot change the final Authorization Decision.

**Input**

The Wallet Unit MUST base the Authorization Validation only on:

- the authenticated Wallet-Relying Party and the interaction context, authoritative only for the identity of the Wallet-Relying Party;
- a validated Authorization Artifact, that is a Wallet-Relying Party Registration Certificate or a Register Response, authoritative for the subject identity, entitlements, intended use, registered scope, intermediary relationships, issuance-specific data and privacy policy references, as defined in [`ETSI TS 119 475`_];
- explicitly identified fallback information, non-authoritative;
- a verified Embedded Disclosure Policy, REQUIRED when provided by the Attestation Provider during Credential Issuance, authoritative when present.

Where authoritative sources conflict with non-authoritative sources, the authoritative sources MUST supersede.
Where the authenticated Wallet-Relying Party context conflicts with the identity or the intermediary binding in the verified authorization context, the Wallet Unit MUST produce ``NOT_AUTHORIZED``, non-overridable.
A request-carried Registrar URL MUST NOT be treated as sufficient proof of registered information by itself; it MAY be used only as a discovery hint unless confirmed by an authoritative source.

**Outcome**

The Wallet Unit MUST output the ``authz_val_state`` and ``edp_state`` variables, both initialized to ``none``.

**Process**

1. **Binding verification**.
   The Wallet Unit MUST ensure that the authenticated entity is the same as the entity described in the authorization data.
   The Wallet-Relying Party identity is the ``organizationIdentifier`` of the Wallet-Relying Party Access Certificate subject (clause 5.1.4 of [`ETSI EN 319 412-1`_]; the Wallet-Relying Party Access Certificate profile is defined in [`ETSI TS 119 411-8`_]).

    - **Credential Issuance**.
      The Wallet Unit MUST match the Credential Issuer identifier with the ``sub`` of the Wallet-Relying Party Registration Certificate or, if no Wallet-Relying Party Registration Certificate is available, with the ``identifier`` used in the Register query, and with the ``issuer_info.data.identifier`` of the Credential Issuer Metadata.
    - **Credential Presentation**.
      The Wallet Unit MUST first assume the **direct** scenario and match the Relying Party identifier with the ``sub`` of the Wallet-Relying Party Registration Certificate or, if not available, the ``identifier`` used in the Register query, and with the ``verifier_info.data.identifier`` of the Request Object in the Remote Flow or the ``docRequest.itemsRequest[].requestInfo.EUWrpRegistrarInfo.identifier`` in the Proximity Flow.
      If the match fails, the Wallet Unit MUST attempt the **intermediated** scenario and match the identifier against the ``intermediary.sub`` field carried in the Wallet-Relying Party Registration Certificate or in the Register Response.

    If the Binding verification fails, the Wallet Unit MUST stop the Authorization Validation and set ``authz_val_state`` to ``BINDING_FAILED``.
    If it succeeds, the Wallet Unit MUST make available to the User the identity of the Relying Party Intermediary, the identity or service description of the intermediated Relying Party, and the intended use of the request; how this information is presented is defined in the relevant User interaction sections of the IT-Wallet specification.

    .. note::

        If the Wallet Unit used only the Wallet-Relying Party Registration Certificate ``sub`` for the Binding verification and the outcome is ``BINDING_FAILED``, the Wallet-Relying Party Registration Certificate is not valid for this Relying Party.
        The Wallet Unit MUST query the Register, validate the response as described in :ref:`Register Query Validation <register-query-validation>`, and repeat the Binding verification.

2. **Entitlement verification**.
   The Wallet Unit MUST verify that the entitlements of the Authorization Subject match the expected role.
   The Wallet Unit MUST parse the ``entitlements`` field of the Wallet-Relying Party Registration Certificate or of the Register Response and check that it contains the entitlement URI expected for the interaction, among those defined in Annex A.2 of [`ETSI TS 119 475`_]:

    - ``https://uri.etsi.org/19475/Entitlement/PID_Provider`` for PID Providers, during PID Issuance;
    - ``https://uri.etsi.org/19475/Entitlement/QEAA_Provider`` for QEAA Providers, during QEAA Issuance;
    - ``https://uri.etsi.org/19475/Entitlement/PUB_EAA_Provider`` for PuB-EAA Providers, during PuB-EAA Issuance;
    - ``https://uri.etsi.org/19475/Entitlement/Non_Q_EAA_Provider`` for EAA Providers, during EAA Issuance;
    - ``https://uri.etsi.org/19475/Entitlement/Service_Provider`` for Relying Parties, during Credential Presentation.

    If the expected entitlement is not present, the Wallet Unit MUST set ``authz_val_state`` to ``WRONG_ENTITLEMENT``.

3. **Attestation Type verification**.
   During Credential Issuance, the Wallet Unit MUST verify that the PID or the Attestation Type being issued is registered for the Credential Issuer.
   A PID Provider issuing PIDs MAY skip this step.
   Otherwise the Wallet Unit MUST match the ``provides_attestations`` array of the Wallet-Relying Party Registration Certificate or of the Register Response (defined in Table 8 of [`ETSI TS 119 475`_]) against the ``credential_configurations_supported`` keys of the Credential Issuer Metadata ([`OpenID4VCI`_]).
   The match MUST be exact and case sensitive, on ``vct`` for SD-JWT VC and on ``docType`` for mdoc.
   If not found, the Wallet Unit MUST set ``authz_val_state`` to ``ATTESTATION_TYPE_NOT_REGISTERED``.

4. **Scope Comparison**.
   During Credential Presentation, the Wallet Unit MUST verify that the requested Digital Credentials and attributes fall within the registered scope, carried in the ``credentials`` array of the Wallet-Relying Party Registration Certificate or of the Register Response (defined in Table 9 of [`ETSI TS 119 475`_]).

    - **Remote Flow**: extract the requested Digital Credentials and attributes from the ``dcql_query`` of the Request Object ([`OpenID4VP`_]) and match them against the ``credentials`` entries, comparing ``format`` and ``meta`` (``vct_values`` for SD-JWT VC) and the requested attributes against the ``claim`` paths.
    - **Proximity Flow**: extract the ``docType`` and the ``nameSpaces`` from the ``docRequests`` of the mdoc Request ([`ISO18013-5`_]) and match them against ``credentials[].meta.doctype_value`` and ``credentials[].claim`` respectively.

    The match MUST be exact and case sensitive.
    If any requested Digital Credential or attribute is not registered, the Wallet Unit MUST set ``authz_val_state`` to ``OVERASKING_DETECTED`` and identify the unregistered attributes or Digital Credentials.

    If all the checks above that apply to the interaction are satisfied, the Wallet Unit MUST set ``authz_val_state`` to ``VERIFICATION_PASSED``.

5. **Embedded Disclosure Policy evaluation**.
   During Credential Presentation, for each Digital Credential matching the Presentation Request, the Wallet Unit MUST check for a locally stored Embedded Disclosure Policy.
   If none exists, this check is superseded.
   Otherwise, according to the ``policy_type`` defined in Section 4.2.5 of [`ETSI TS 119 472-3`_]:

    - ``no_policy``: no restriction applies.
    - ``authorized_rp_only``: only the Relying Parties in the ``authorized_parties`` list are authorized.
      The Wallet Unit MUST compare the Relying Party subject DN of the Wallet-Relying Party Access Certificate against the ``subject_dn`` entries, and the Relying Party entitlements or sub-entitlements of the Wallet-Relying Party Registration Certificate against the ``entitlement_uri`` entries.
      A match on either criterion is sufficient.
    - ``specific_root_of_trust``: only the Relying Parties whose Wallet-Relying Party Access Certificate chain contains one of the ``trusted_roots`` are authorized.
      The Wallet Unit MUST match ``issuer_dn`` using LDAP DN comparison and ``serial_number`` using integer comparison.

    If the applicable check is satisfied, or no Embedded Disclosure Policy is present, the Wallet Unit MUST set ``edp_state`` to ``EDP_SATISFIED``; otherwise it MUST set ``edp_state`` to ``EDP_NOT_SATISFIED``.

**Outcome**

At the end of the Authorization Validation the Wallet Unit MUST output the ``authz_val_state`` and ``edp_state`` values.
The table below summarizes the codes.

.. _table_authz_state_codes:
.. list-table:: Authorization Validation State Codes
   :class: longtable
   :widths: 18 26 12 44
   :header-rows: 1

   * - **Variable**
     - **Code**
     - **Phase**
     - **Meaning**
   * - ``authz_art_state``
     - ``CERTIFICATE_VALID``
     - both
     - The Wallet-Relying Party Registration Certificate format, signature, trust anchor and status are successfully verified.
   * - ``authz_art_state``
     - ``CERTIFICATE_INVALID``
     - both
     - A format, signature, trust anchor or status check fails on the presented registration certificate.
   * - ``authz_art_state``
     - ``REGISTER_VALID``
     - both
     - The online Registrar query completed, and the response signature, pertinence and trust anchor passed.
   * - ``authz_art_state``
     - ``FAILED``
     - both
     - The online Registrar query or response verification failed during the fallback procedures.
   * - ``authz_val_state``
     - ``WRONG_ENTITLEMENT``
     - both
     - The entitlements of the Authorization Subject do not match the expected role for the active context.
   * - ``authz_val_state``
     - ``BINDING_FAILED``
     - both
     - The identity binding between the authenticated Wallet-Relying Party and the authorization data fails.
   * - ``authz_val_state``
     - ``ATTESTATION_TYPE_NOT_REGISTERED``
     - issuance
     - The Attestation Type being issued is not found in the Credential Issuer registered profiles.
   * - ``authz_val_state``
     - ``OVERASKING_DETECTED``
     - presentation
     - The Relying Party requests Digital Credentials, formats or namespaces that exceed its registered scope.
   * - ``authz_val_state``
     - ``VERIFICATION_PASSED``
     - both
     - Identity binding, entitlement verification, attestation matching and scope checking all passed.
   * - ``edp_state``
     - ``EDP_SATISFIED``
     - presentation
     - No Embedded Disclosure Policy restriction applies, or the Relying Party satisfies the local policy.
   * - ``edp_state``
     - ``EDP_NOT_SATISFIED``
     - presentation
     - The Relying Party does not satisfy any locally stored Embedded Disclosure Policy.

The final Authorization Decision, ``AUTHORIZED`` or ``NOT_AUTHORIZED``, is elaborated from the ``authz_art_state``, ``authz_val_state`` and ``edp_state`` values, as defined in :ref:`trust-evaluation:Authorization Decision and Override Rules`.

.. plantuml:: plantuml/eudiw-authz-eval.puml
    :width: 99%
    :alt: Flowchart of the EUDIW Authorization Algorithm.
    :caption: Flowchart of the EUDIW Authorization Algorithm.

EUDIW Metadata Retrieval and Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Within the EUDIW Trust Framework the metadata of a Wallet-Relying Party are obtained through the protocol flow and their authenticity is established through the Wallet-Relying Party Access Certificate.
This applies to Credential Issuance and to Credential Presentation in the Remote Flow.
In the Proximity Flow no separate metadata retrieval is performed: the Relying Party identity is established through the mdoc reader authentication (see :ref:`trust-evaluation:EUDIW Authentication`).

**Metadata Retrieval**

The Wallet Unit obtains the metadata of the Wallet-Relying Party according to the interaction:

- During Credential Issuance, the Credential Issuer Metadata is obtained from the Credential Issuer well-known metadata endpoint, as defined in [`OpenID4VCI`_] (see :ref:`credential-issuer-endpoint:Metadata Endpoints`).
- During Credential Presentation in the Remote Flow, the Relying Party metadata is carried in the Request Object of the authorization request, as defined in [`OpenID4VP`_] (see :ref:`remote-flow:Request Object`).

**Metadata Validation**

The authenticity of the retrieved metadata is established through the Wallet-Relying Party Access Certificate.
During Credential Issuance, the Credential Issuer Metadata is signed by the Attestation Provider as defined in Section 12.2.3 of [`OpenID4VCI`_], providing the Wallet-Relying Party Access Certificate chain in the ``x5c`` header of the JOSE signature.
During Credential Presentation in the Remote Flow, the Request Object is signed by the Relying Party and provides the same ``x5c`` header.
In both cases the Wallet Unit validates the signature and the certificate chain as defined in :ref:`trust-evaluation:EUDIW Authentication`, and MUST use only the metadata whose signature is verified against the authenticated Wallet-Relying Party Access Certificate.
