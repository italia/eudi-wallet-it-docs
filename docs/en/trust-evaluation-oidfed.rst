.. include:: ../common/common_definitions.rst
.. Included via trust-evaluation.rst at title level '-' (level 1).

Trust Evaluation in the National Trust Framework
-----------------------------------------------------

This section defines the trust evaluation procedures of the National Trust Framework.
The Entity Type Identifiers and the metadata of each role, used during these procedures, are defined in :ref:`infrastructure-trust:Entity Type Identifiers and Metadata`, according to that profile.
The selection rules that define when these procedures apply are detailed in :ref:`trust-evaluation:Trust Framework Selection`.

The Trust Artifacts used during these procedures, that is the Entity Configuration, the Subordinate Statements, the Trust Marks, are defined in :ref:`infrastructure-trust:National Trust Artifacts`.

The procedures defined in this section are executed within the operational Issuance and Presentation flows (see :ref:`digital-credential-flows:Digital Credential Flows`).
The parameters they operate on, such as the signed Request Object, the mdoc Request, the Metadata of all Entities involved and the data model of the received Digital Credentials, are defined in the respective sections (see :ref:`entities:Entities`, :ref:`remote-flow:Request Object` for the Remote Flow, and :ref:`credential-data-model:SD-JWT-VC Credential Format` and :ref:`credential-data-model:mdoc-CBOR Credential Format` for the Digital Credential formats).

Trust Evaluation Processes by Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The procedures are defined in a general form, with a **Trust Evaluator** and a **Trust Evaluated Party** and the following table defines which entity acts in which role, when and for which purpose.

.. _table_national_tf_roles:
.. list-table:: Trust Evaluation Processes by Entity and Context in the National Trust Framework
    :class: longtable
    :widths: 12 20 40 28
    :header-rows: 1

    * - **Entity**
      - **Context**
      - **As Trust Evaluator, implements**
      - **As Trust Evaluated Party, provides**
    * - Wallet Unit
      - Issuance of a national only Credential
      - On the Credential Issuer:

        - :ref:`trust-evaluation:Federation Entity Authentication`
        - :ref:`trust-evaluation:Authorization`
        - :ref:`trust-evaluation:Metadata Retrieval and Validation`

        On the received Credential:

        - :ref:`trust-evaluation:Signing Trust Anchor Validation Procedure`
      - The Wallet Instance Attestation with the proof of possession of the attested key, validated as defined in :ref:`trust-evaluation:Wallet Unit Authentication`.
    * - Wallet Unit
      - Remote presentation, ``openid_federation`` prefix
      - On the Relying Party:

        - :ref:`trust-evaluation:Federation Entity Authentication`
        - :ref:`trust-evaluation:Authorization`, including the Overasking Check
        - :ref:`trust-evaluation:Metadata Retrieval and Validation`
      - No entity level artifact is required from the Wallet Unit.
    * - Wallet Unit
      - Proximity presentation
      - On the Relying Party:

        - :ref:`trust-evaluation:Relying Party Proximity Authentication`
        - :ref:`trust-evaluation:Authorization`, including the Overasking Check, on the registration Trust Mark provided by value in the ``requestInfo`` of the ISO ``DeviceRequest``
      - No entity level artifact is required from the Wallet Unit.
    * - Credential Issuer
      - Issuing national only Credentials
      - On the Wallet Unit:

        - :ref:`trust-evaluation:Wallet Unit Authentication`
      - The Entity Configuration (:ref:`infrastructure-trust:Entity Configuration`) with the registration Trust Marks (:ref:`infrastructure-trust:Trust Mark registration-entity`), and the issuance artifacts signed with keys resolvable through the federation, validated as defined in :ref:`trust-evaluation:Federation Entity Authentication`.
        For the mdoc format, the Document Signer certificate in the ``x5chain`` header, validated as defined in :ref:`trust-evaluation:X.509 Certificate Chain Validation`.
    * - Relying Party
      - Remote presentation, ``openid_federation`` prefix
      - On the received Credentials:

        - :ref:`trust-evaluation:Signing Trust Anchor Validation Procedure`

        On the Wallet Provider, to invoke the Wallet through the national discovery mechanism (see the note below):

        - :ref:`trust-evaluation:Metadata Retrieval and Validation`
      - The Entity Configuration (:ref:`infrastructure-trust:Entity Configuration`) with the registration Trust Marks (:ref:`infrastructure-trust:Trust Mark registration-entity`), and the signed Request Object with keys resolvable through the federation, including the ``trust_chain`` header when offline validation is expected, validated as defined in :ref:`trust-evaluation:Federation Entity Authentication` and :ref:`trust-evaluation:Authorization`.
    * - Relying Party Intermediary
      - Remote presentation, as the Federation Intermediate of an affiliated Relying Party
      - It does not act as Trust Evaluator in the operational flows.
      - The Entity Configuration (:ref:`infrastructure-trust:Entity Configuration`) with the ``intermediate`` registration Trust Mark (see :ref:`infrastructure-trust:Trust Mark Types and Schema`), and the Subordinate Statements of its affiliated Relying Parties.
        The Intermediary is validated as part of the affiliated Relying Party's Trust Chain, whose ``authority_hints`` point to it.
        The Wallet Unit MUST verify that the affiliated Relying Party's Trust Chain is validated through a recognized Intermediary or directly through the Federation Trust Anchor, and it informs the User as defined in :ref:`trust-evaluation:User Transparency`.

.. note::
  In the remote flow the Relying Party invokes the Wallet through app links (universal links) instead of custom URL schemes.
  This IT-Wallet choice requires the Relying Party to obtain and validate the Wallet Provider metadata beforehand, building the Trust Chain about the Wallet Provider (Metadata Retrieval and Validation), as part of the Wallet Metadata Retrieval Flow (see :ref:`wallet-metadata-retrieval:Wallet Metadata Retrieval Flow` and the Selection Page in :ref:`functionalities:User Experience Design`).
  This mechanism is specific to the remote flow and does not apply to the proximity flow.


Federation Trust Anchor Distribution and Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Federation Trust Anchor Distribution
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The configuration of the federation is published by the Federation Trust Anchor within its Entity Configuration, available at the well-known web path **.well-known/openid-federation**.
All the Entities MUST obtain the federation configuration before entering the operational phase and MUST keep it up to date.
The federation configuration contains the Federation Trust Anchor public keys for signature operations and the federation endpoints (see :ref:`infrastructure-trust:Entity Configuration`).

The Federation Trust Anchor MUST distribute its Federation Public Keys through secure out-of-band mechanisms.
When a Federation Trust Anchor validation is required, all the Entities MUST compare the Federation Trust Anchor public keys with those obtained from the Federation Trust Anchor Entity Configuration, and they MUST discard any key that does not match.

.. note::
  Within IT-Wallet the out-of-band channel is the contact channel established with the Entity during the registration process (see :ref:`onboarding-system:Entity Registration`).

Entities MAY additionally pin the Federation Trust Anchor public keys, in their local configuration.
A pinned configuration MAY be used only while it is valid and MUST be updated when a key rotation occurs.

The Federation Trust Anchor Entity Configuration also provides the Signing Trust Anchors of the X.509 signing PKI, used to verify the Credentials anchored to this framework, and the National Wallet Trust Anchors used to verify Wallet Unit Attestations and Key Attestations.
Their distribution and validation are defined in :ref:`trust-evaluation:Signing Trust Anchor Distribution` and :ref:`trust-evaluation:Wallet Trust Anchor Distribution`, respectively, as they concern the verification of an attestation and not the validation of the Federation Trust Anchor.

Federation Trust Anchor Validation
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Input**

- The Federation Entity Identifier of the Federation Trust Anchor.
- The Federation Trust Anchor public keys obtained out-of-band, or a pinned configuration.

**Outcome**

- The validated set of Federation Trust Anchor Federation Public Keys.
- The federation configuration, including the federation endpoints.

**Process**

The verification of the Entity Configuration is the Entity Statement validation defined in `OID-FED`_ Section 3.2, applied to the self-issued Entity Configuration of the Federation Trust Anchor and completed, within IT-Wallet, with the out-of-band comparison of the keys.

1. Fetch the Entity Configuration from the well-known endpoint of the Federation Trust Anchor, served with the media type ``application/entity-statement+jwt``.
2. Verify that the Entity Configuration is a signed JWT with ``iss`` and ``sub`` equal to the Federation Trust Anchor identifier, and verify its signature with one of the keys contained in its ``jwks``.
   The supported signature algorithms are defined in :ref:`algorithms:Cryptographic Algorithms`.
3. Compare the keys in ``jwks`` with the keys obtained out-of-band or pinned, discarding the keys that do not match.
4. Check the temporal validity of the Entity Configuration through the ``iat`` and ``exp`` claims.
5. Extract the federation endpoints from the ``federation_entity`` metadata, and the ``trust_mark_issuers`` claim (see :ref:`infrastructure-trust:Entity Configuration`).

If any step fails, the federation configuration MUST NOT be used.

Federation Trust Anchor Key Rotation and Historical Verification
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

When it is required to validate a Trust Chain over time, even if the Federation Trust Anchor has changed its cryptographic keys for digital signature, the Federation Historical Keys endpoint always makes the keys no longer used available for historical signature verifications.
This property supports the non-repudiability of the long lived attestations.

When the Federation Trust Anchor rotates its keys, the new keys are distributed with the same out-of-band mechanism used for the initial distribution.
Entities that pin the Federation Trust Anchor keys MUST refresh the pinned material accordingly.

Trust Chain Validation
^^^^^^^^^^^^^^^^^^^^^^^^

Trust Chain Validation is a technical procedure used by the trust evaluation processes defined in this section for different purposes.
Depending on whether an entity is evaluating a federation statement or an artifact carries the X.509 certificate chain used for its signature, two different Trust Chain Validation procedures apply.

Federation Trust Chain
"""""""""""""""""""""""""

The Trust Chain is a sequence of verified statements that validates an Entity compliance with the federation.
It has an expiration date, beyond which it MUST be renewed to obtain fresh and updated metadata.
The expiration date of the Trust Chain is determined by the earliest expiration timestamp among all the statements.
No Entity can force the expiration date of the Trust Chain to be higher than the one configured by the Federation Trust Anchor.

This procedure verifies the Trust Chain.
The derivation of the final metadata of the subject, obtained applying the metadata policies carried by the statements of the Trust Chain, is defined in :ref:`trust-evaluation:Metadata Retrieval and Validation`.
According to `OID-FED`_, the verification of the chain and the derivation of the final metadata, is referred to as the **resolution of a Trust Chain**.

The Trust Chain is built through the **Federation Entity Discovery** process defined in `OID-FED`_:

- The Trust Evaluator fetches the Entity Configuration of the subject.
- Follows the ``authority_hints`` to collect the Subordinate Statements issued by the superior entities.
- It continues until the Federation Trust Anchor is reached.

The Trust Chain MAY also be kept valid with the **fast renewal method** defined in `OID-FED`_ Section 3.1.3, that avoids a full discovery process by fetching the Subordinate Statements directly through their ``source_endpoint`` claim.

The Trust Chain MAY also be provided statically by the subject within a signed artifact, using the ``trust_chain`` JOSE header parameter defined in `OID-FED`_ Section 4.3.
Within IT-Wallet the ``trust_chain`` header is carried in the Request Object of the presentation flow (see :ref:`remote-flow:Request Object`) and in the signed artifacts of the issuance flow (`OPENID4VCI`_ Appendix F.1 and Section 12.2.3).
A statically provided Trust Chain only requires to be refreshed when an internet connection is available, while it MUST be refreshed when it results as expired.

The revocation of an Entity is made with the unavailability of the Subordinate Statement related to it.
If the Federation Trust Anchor or its Intermediate does not publish a valid Subordinate Statement, or if it publishes an expired or invalid one, the subject of the Subordinate Statement MUST be intended as not valid or revoked.
For the Trust Evaluator, this real-time check of the revocation status is possible only online, by fetching the Subordinate Statement at the moment of the verification.

The Trust Chains can also be verified offline, using one of the Federation Trust Anchor public keys.
In this case the real-time revocation check is not available, and the freshness of the Trust Chain is relied upon.

The maximum validity of a Trust Chain can be enforced by the Federation Trust Anchor, which sets it through the expiration of its own statements, as described above.
Independently of that validity, for the purpose of the revocation status of the Entities a Trust Chain built more than 24 hours before the moment of the verification SHOULD NOT be considered valid.
When the revocation status of an Entity requires to be relied upon and a real-time online check is not available, a Trust Chain older than 24 hours SHOULD be renewed before the interaction can proceed.
This 24 hours limit applies to the age of the Trust Chain, computed from its construction, and is independent of its expiration date.

**Input**

- The Federation Entity Identifier of the subject, or a statically provided Trust Chain.
- The validated Federation Trust Anchor Federation Public Keys (see :ref:`trust-evaluation:Federation Trust Anchor Distribution`).

**Outcome**

- A validated Trust Chain, that is the ordered set of verified statements, with its expiration date.

**Process**

The steps below verify a Trust Chain according to `OID-FED`_, with the pointer to the relevant part of the specification for each step:

1. Obtain the Entity Configuration of the subject, or take the first element of the statically provided Trust Chain.
2. Collect the Subordinate Statements following the ``authority_hints`` up to the Federation Trust Anchor, or take them from the static Trust Chain.
   The Subordinate Statements are obtained from the fetch endpoint (`OID-FED`_ Section 8.1).
3. Validate each statement as an Entity Statement according to `OID-FED`_ Section 3.2, that is verify its signature, the consistency of the ``iss`` and ``sub`` claims, and its temporal validity.
   Each Subordinate Statement is verified with the Federation Entity Keys of its issuer, attested by the superior statement.

   - The statement issued by the Federation Trust Anchor is verified with the validated Federation Trust Anchor keys.
   - The Entity Configuration of the subject is verified with the keys attested in the Subordinate Statement about it.

4. Enforce the constraints carried in the Subordinate Statements along the chain, as defined in `OID-FED`_ Section 6.2.
   In particular, verify that the metadata Entity Types published by the subject are within the ``allowed_entity_types``, considering that the ``federation_entity`` Entity Type is always allowed, and that the number of Intermediates does not exceed the ``max_path_length`` set by the superiors.
5. Compute the Trust Chain expiration as the earliest ``exp`` value among the statements.

If any verification fails, the Trust Chain MUST be considered invalid and the subject MUST NOT be trusted on the basis of it.

X.509 Certificate Chain Validation
"""""""""""""""""""""""""""""""""""""

This variant applies when an artifact is provided along with the X.509 certificate chain used for the signature.
For artifacts in JOSE format the chain is carried in the ``x5c`` header parameter, as defined in :rfc:`7515` and used in IT-Wallet in the Request Object of the presentation flow (see :ref:`remote-flow:Request Object`).
For Credentials in mdoc format the chain is carried in the ``x5chain`` unprotected header (element 33) of the Mobile Security Object, as defined in :rfc:`9360` and in :ref:`credential-data-model:Mobile Security Object`.
The chain contains the Document Signer certificate and any intermediate certificate.
It MUST NOT contain the Signing Trust Anchor certificate, which is distributed as defined in :ref:`trust-evaluation:Signing Trust Anchor Distribution`.

The certification path validation is the standard X.509 path validation defined in :rfc:`5280#section-6`, with the revocation status checking defined in :rfc:`5280` and :rfc:`6960`.
The certificate lifecycle and the revocation mechanisms, including the CRL, are defined in :ref:`infrastructure-trust:Revocation Mechanisms`.
This is the same certification path validation used in the EUDIW Trust Framework (see :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`); the only difference is the origin of the trust anchor and the additional extraction of the Federation Entity Identifier.
In this section, for the National Trust Framework, the algorithm details are not redefined.

Within the National Trust Framework the following applies.

  - The trust anchor of the path validation is the applicable Signing Trust Anchor, obtained as defined in :ref:`trust-evaluation:Signing Trust Anchor Distribution`.
  - The end-entity certificate carries the OpenID Federation Entity Identifier of the subject in the ``subjectAltName`` URI.
    This is the element that links the X.509 signature to the federation identity of the signer.
    Therefore, the validation extracts this identifier so that the calling process can verify that the certificate that signed the artifact belongs to the OpenID Federation entity expected for that artifact.
    The comparison against the expected identifier, for example the ``iss`` of the Credential, is performed by the calling process (see :ref:`trust-evaluation:Signing Trust Anchor Validation Procedure`).
    This variant only produces the identifier and it does not by itself establish which identifier is expected.

.. note::
  The issuance of these X.509 Certificates and the operation of the signing PKI are defined in the onboarding procedure and are out of the scope of this section (see :ref:`onboarding-system:Onboarding Processes`).

**Input**

- The certificate chain extracted from the artifact header, that is the Document Signer certificate and any intermediate certificate.
- The applicable Signing Trust Anchor certificate, obtained as defined in :ref:`trust-evaluation:Signing Trust Anchor Distribution`.

**Outcome**

- The validated end-entity certificate.
- The OpenID Federation Entity Identifier of the signer, extracted from the ``subjectAltName`` URI, to be matched against the expected issuer by the calling process.

**Process**

1. Build the certification path from the end-entity certificate to the Signing Trust Anchor certificate.
2. Execute the path validation defined in :rfc:`5280#section-6`, using the Signing Trust Anchor as the trust anchor input of the algorithm.
3. Verify the revocation status of the certificates in the path, according to :rfc:`5280` and :rfc:`6960`.
4. Extract the OpenID Federation Entity Identifier from the ``subjectAltName`` URI of the end-entity certificate, and return it to the calling process for the match against the expected issuer.

If any step fails, the artifact signature MUST NOT be verified with the presented certificate chain.

Signing Trust Anchor Distribution and Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This process provides and validates the root of trust for the verification of the issuer data authentication of an attestation.

The Signing Trust Anchor is the root of trust of the X.509 PKI used to sign the Digital Credentials whose Rulebook anchors them to the National Trust Framework.

It is distinct from the Federation Trust Anchor of :ref:`trust-evaluation:Federation Trust Anchor Distribution` as the Federation Trust Anchor is the root of the federation statements, while a Signing Trust Anchor is the root of a certification path that validates the signature of an attestation.
The Federation Trust Anchor and a Signing Trust Anchor MAY be operated by the same organization, but they are different trust relationships, with different lifecycles and different revocation channels.

There MAY be more than one Signing Trust Anchor.
Each Credential Issuer that signs Credentials in this framework uses a Signing Trust Anchor as the root of its Document Signer certificates.
Different Credential Issuers MAY rely on different Signing Trust Anchors.

Signing Trust Anchor Distribution
"""""""""""""""""""""""""""""""""

The Signing Trust Anchors are distributed through the Federation Trust Anchor Entity Configuration.
Each Signing Trust Anchor certificate is provided in the ``x5c`` parameter of a dedicated JWK, distinct from the Federation Entity Keys used to sign the federation statements.
This distribution mechanism is an IT-Wallet specific implementation and is not defined by `OID-FED`_.

Entities MAY pin a Signing Trust Anchor in their local configuration.
A pinned Signing Trust Anchor MAY be used only while it is valid and MUST be updated when the Signing Trust Anchor is rotated.

The result of this distribution is, for each Trust Evaluator, the set of validated Signing Trust Anchor certificates, each associated with the Federation Entity Identifier of the Credential Issuers that rely on it.
This set is the trust anchor material consumed by the validation procedure below.

.. note::
  The issuance of the Document Signer certificates and the operation of the signing PKI are defined in the onboarding procedure and are not in the scope of this section (see :ref:`onboarding-system:Onboarding Processes`).

Signing Trust Anchor Validation Procedure
"""""""""""""""""""""""""""""""""""""""""

The procedure depends on the format of the attestation.

For attestations in JOSE format, such as Digital Credentials in SD-JWT VC format and the Wallet Instance Attestation, the issuer is identified by the ``iss`` claim and the signature verification key is referenced by the ``kid`` header parameter.
The key MUST be resolved within the final metadata of the issuer, obtained through the Federation Trust Chain.
The artifact MAY carry the ``trust_chain`` JOSE header to allow the validation without a new discovery process.

For Credentials in mdoc format the Mobile Security Object carries the Document Signer certificate in the ``x5chain`` header.
The signature is verified with that certificate.
The Signing Trust Anchor of the issuer is validated by extracting the OpenID Federation Entity Identifier from the ``subjectAltName`` URI and by validating the certification path against the applicable Signing Trust Anchor obtained as defined in :ref:`trust-evaluation:Signing Trust Anchor Distribution`.

**Input**

- The signed attestation.
- The validated Federation Trust Anchor configuration and the applicable Signing Trust Anchor.

**Outcome**

- The validated trust anchor and the signing key or certificate for the attestation.
- The confirmation that the signing key belongs to the attestation issuer.

**Process**

1. For JOSE artifacts, derive the issuer final metadata from the Federation Trust Chain (see :ref:`trust-evaluation:Federation Trust Chain` and :ref:`trust-evaluation:Metadata Retrieval and Validation`) and select the key referenced by the ``kid`` header.
2. For mdoc artifacts, validate the ``x5chain`` as defined in :ref:`trust-evaluation:X.509 Certificate Chain Validation` and verify that the OpenID Federation Entity Identifier in the ``subjectAltName`` URI corresponds to the expected issuer.
3. Verify the attestation signature with the selected key or certificate.

.. note::
  When required, the Federation Historical Keys endpoint and the published CRLs MUST be used to ensure that the attestation was valid at the time of issuance or presentation (see :ref:`trust-evaluation:Federation Trust Anchor Key Rotation and Historical Verification` for more details).

The lifecycle of the signing certificates MUST be kept aligned with the federation configuration set of the issuer keys.
When a signing key is rotated or is no longer valid, the corresponding JWK MUST be removed from the Entity Configuration or rotated, and the related certificate MUST be revoked accordingly.
Within IT-Wallet, when the federation configuration and the certificate status diverge, the most restrictive state MUST prevail, and therefore a key revoked in either of the two views MUST be considered revoked.

Wallet Trust Anchor Distribution and Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This process establishes and validates the National Wallet Trust Anchor used to validate Wallet Instance Attestations and Key Attestations issued by a Wallet Provider in the National Trust Framework.

The National Wallet Trust Anchor is the root of the X.509 PKI used by the Wallet Provider to sign Wallet Unit Attestations. It is distinct from the Federation Trust Anchor, which is the root of the federation statements, and from the Signing Trust Anchor used by a Credential Issuer for Digital Credentials.

Wallet Trust Anchor Validation
""""""""""""""""""""""""""""""""""""""

For a Wallet Instance Attestation or Key Attestation that carries an X.509 signing certificate chain, the Trust Evaluator MUST validate the chain against the applicable National Wallet Trust Anchor before accepting the attestation signature.

**Input**

- The signed Wallet Instance Attestation or Key Attestation and its signing certificate chain.
- The validated Trust Chain of the Wallet Provider.
- The applicable National Wallet Trust Anchor obtained as defined in :ref:`trust-evaluation:Wallet Trust Anchor Distribution`.

**Outcome**

- The validated Wallet Provider signing certificate and attestation.
- Confirmation that the signing certificate belongs to the Wallet Provider identified by the validated Trust Chain.

**Process**

1. Validate the Trust Chain of the Wallet Provider and derive its final metadata as defined in :ref:`trust-evaluation:Federation Trust Chain` and :ref:`trust-evaluation:Metadata Retrieval and Validation`.
2. Extract the signing certificate chain from the ``x5c`` JOSE header of the Wallet Instance Attestation or Key Attestation. The National Wallet Trust Anchor MUST NOT be included in this chain.
3. Validate the certificate chain against the applicable National Wallet Trust Anchor as defined in :ref:`trust-evaluation:X.509 Certificate Chain Validation`.
4. Verify the attestation signature with the validated end-entity certificate.
5. Verify that the Federation Entity Identifier extracted from the end-entity certificate corresponds to the Wallet Provider identified by the Trust Chain.
6. Check the temporal validity and revocation status of the attestation as required by the applicable attestation profile.

If any step fails, the Wallet Instance Attestation or Key Attestation MUST NOT be considered issued by a trusted Wallet Provider.

Wallet Trust Anchor Distribution
""""""""""""""""""""""""""""""""

The National Wallet Trust Anchor MUST be distributed through the Federation Trust Anchor Entity Configuration. It MUST be represented by a dedicated JWK whose ``x5c`` parameter contains the National Wallet Trust Anchor certificate. The dedicated JWK MUST be distinct from the Federation Entity Keys used to sign federation statements.

The Trust Evaluator MUST validate the Federation Trust Anchor Entity Configuration and the Wallet Provider's Trust Chain before accepting the National Wallet Trust Anchor. The resulting configuration MUST associate the National Wallet Trust Anchor with the Wallet Provider's Federation Entity Identifier.

Entities MAY pin the National Wallet Trust Anchor in their local configuration. A pinned National Wallet Trust Anchor MAY be used only while it is valid and MUST be updated when the National Wallet Trust Anchor is rotated.

When a Wallet Provider operates in both the National Trust Framework and the EUDIW Trust Framework, the National Wallet Trust Anchor MUST be the same certificate as the Trust Anchor notified to the European Commission and published in the Wallet Providers LoTE under the Wallet Provider's ``ServiceDigitalIdentity``.

Authentication Trust Anchor Distribution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Authentication Trust Anchors are distributed through the Federation Trust Anchor Entity Configuration with the same mechanism used for the Signing Trust Anchors.
Each Authentication Trust Anchor certificate is provided in the ``x5c`` parameter of a dedicated JWK, distinct from the Federation Entity Keys.

An Authentication Trust Anchor is the root of the X.509 authentication PKI that issues the Relying Party authentication certificates used in the Proximity Flow.
These certificates follow the same profile as the Wallet-Relying Party Access Certificate (see :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`).

.. note::
  The issuance of the Relying Party authentication certificates and the operation of the authentication PKI are defined in the onboarding procedure and are not in the scope of this section (see :ref:`onboarding-system:Onboarding Processes`).

Authentication
^^^^^^^^^^^^^^^^^^^^

The Authentication process has the aim of asserting the identity of the Trust Evaluated Party.
Three procedures are defined:

- Federation Entity Authentication applies to the entities that publish an Entity Configuration, in the Remote Flow.
- Wallet Unit Authentication applies to the Wallet Unit, which is not a Federation Entity.
- Relying Party Proximity Authentication applies to the Relying Party in the Proximity Flow.

Federation Entity Authentication
"""""""""""""""""""""""""""""""""""

The identity of Trust Evaluated Party and its keys are established through the Trust Chain.
The Trust Evaluated Party authenticates itself in a given interaction by signing the protocol artifact of that interaction with a private key whose public part is published in its final metadata, obtained by resolving the Trust Chain.
The ``kid`` header parameter, as defined in :rfc:`7515`, references a key contained in the final metadata of the Trust Evaluated Party.
The full set of header parameters of each signed artifact is defined in the corresponding protocol section.

**Input**

- The signed protocol artifact.
- The Federation Entity Identifier claimed by the Trust Evaluated Party.
- A Trust Chain about the Trust Evaluated Party, provided statically or built through discovery.

**Outcome**

The Trust Evaluator MUST output ``AUTHENTICATED`` or ``NON_AUTHENTICATED``.
In the second case the Trust Evaluated Party MUST NOT be considered authenticated and the interaction MUST NOT continue.
The User notification and the prohibition of the cross scheme retry are defined in :ref:`trust-evaluation:Failure Handling`.

**Process**

1. Validate the Trust Chain about the Trust Evaluated Party and derive its final metadata (see :ref:`trust-evaluation:Federation Trust Chain` and :ref:`trust-evaluation:Metadata Retrieval and Validation`).
2. Verify that the entity identifier carried by the artifact, for example the ``client_id`` or the ``iss`` claim, matches the subject of the Trust Chain.
3. Select within the final metadata the public key referenced by the ``kid`` header.
4. Verify the artifact signature with the selected key.

The successful verification provides both the authentication of the Trust Evaluated Party and the proof of possession of its private key.

Wallet Unit Authentication
"""""""""""""""""""""""""""""""""""

The Wallet Instance Attestation conveys the Wallet Unit public key which is used to validate the signature over the Wallet Instance Attestation.
The format and the issuance flow are defined in :ref:`wallet-instance-attestation-issuance:Wallet Instance Attestation Issuance`.

The evaluation MUST follow the model defined in OpenID Federation for Wallet Architectures.
The Wallet Unit authenticates with a Client authentication mechanism that provides the Wallet Instance Attestation issued by its Wallet Provider, together with the proof of possession of the attested key.
In the issuance flow this is realized with the OAuth 2.0 Attestation-Based Client Authentication, that is the ``OAuth-Client-Attestation`` and ``OAuth-Client-Attestation-PoP`` parameters (`OAUTH-ATTESTATION-CLIENT-AUTH`_), as described in `OPENID4VCI`_.
To establish trust in the Wallet Unit, the Trust Evaluator MUST:

- Establish trust in the Wallet Provider that issued the Wallet Instance Attestation.
- Validate the Wallet Instance Attestation as defined in :ref:`trust-evaluation:Wallet Trust Anchor Validation` using the National Wallet Trust Anchor.

**Input**

- The Wallet Instance Attestation presented by the Wallet Unit.
- The proof of possession of the key attested in the Wallet Instance Attestation.
- A Trust Chain about the Wallet Provider.

**Outcome**

The Trust Evaluator MUST output ``AUTHENTICATED`` or ``NON_AUTHENTICATED`` for the Wallet Unit.

**Process**

1. Validate the Trust Chain about the Wallet Provider that issued the Wallet Instance Attestation and derive its final metadata (see :ref:`trust-evaluation:Federation Trust Chain` and :ref:`trust-evaluation:Metadata Retrieval and Validation`).
2. Validate the Wallet Instance Attestation as defined in :ref:`trust-evaluation:Wallet Trust Anchor Validation` using the National Wallet Trust Anchor.
3. Check the temporal validity and the revocation status of the Wallet Instance Attestation.
4. Verify the proof of possession of the attested key, according to the protocol in use.

Relying Party Proximity Authentication
"""""""""""""""""""""""""""""""""""""""

In the Proximity Flow the Relying Party is authenticated through the mdoc reader authentication defined in [`ISO18013-5`_].
The Relying Party signs the session transcript with the private key of its authentication certificate and provides the certificate chain in the ``x5chain`` header of the ``ReaderAuth``.
The certification path terminates in an Authentication Trust Anchor distributed as defined in :ref:`trust-evaluation:Authentication Trust Anchor Distribution`.

**Input**

- The ``ReaderAuth`` signed by the Relying Party, with the authentication certificate chain in the ``x5chain`` header.
- The applicable Authentication Trust Anchor.

**Outcome**

The Trust Evaluator MUST output ``AUTHENTICATED`` or ``NON_AUTHENTICATED``.
In the second case the Relying Party MUST NOT be considered authenticated and the interaction MUST NOT continue.

**Process**

1. Extract the certificate chain from the ``x5chain`` header of the ``ReaderAuth``.
2. Validate the certification path against the applicable Authentication Trust Anchor as defined in :ref:`trust-evaluation:X.509 Certificate Chain Validation`.
3. Verify the ``ReaderAuth`` signature over the session transcript with the validated authentication certificate.

The successful verification provides both the authentication of the Relying Party and the proof of possession of the private key of its authentication certificate.

Authorization
^^^^^^^^^^^^^^^^^^

The authorization data of an entity are provided by the registration Trust Mark issued by the Registrar through the Federation Authority.
The registration Trust Mark is functionally analogous to the Wallet-Relying Party Registration Certificate of the EUDIW Trust Framework, and it reuses the same field names for the authorization data.
It attests the registration of the entity and carries its ``entitlements`` and, where applicable, the ``provides_attestations`` or the ``credentials`` it is authorized to issue or to request.
Its structure is defined in :ref:`infrastructure-trust:Trust Mark registration-entity` and the identifiers schema in :ref:`infrastructure-trust:Trust Mark Types and Schema`.

The Authorization process is composed of the following procedures:

1. Trust Mark Validation, which establishes the validity of the registration Trust Mark.
   It applies to all the registered Entities.
2. Entitlement Check, which verifies that the role and, at issuance, the Credential types of the Trust Evaluated Party are authorized.
   It applies to all the Wallet-Relying Parties, that is Credential Issuers and Relying Parties.
3. Overasking Check, which verifies at presentation that a Relying Party requests only the Digital Credentials and the attributes it is authorized to request.
   It applies to Relying Parties.

The role authorization common to both phases is performed by the Entitlement Check; the phase specific checks are the Credential type check at issuance, inside the Entitlement Check, and the attribute level Overasking Check at presentation.

The Trust Evaluator MUST perform the Authorization process only after the Trust Evaluated Party has been successfully authenticated.

Trust Mark Validation
"""""""""""""""""""""""

**Input**

- The *registration-entity* Trust Mark, obtained in the Remote Flow from the ``trust_marks`` claim of the Entity Configuration or from the Federation Trust Mark endpoint (`OID-FED`_ Section 8.6), or provided by value in the ``requestInfo`` of the ISO ``DeviceRequest`` in the Proximity Flow, through the ``euWrprc`` member as defined in the EUDIW Trust Framework.
- The validated Federation Trust Anchor configuration.

**Outcome**

The Trust Evaluator MUST output ``TRUST_MARK_VALID`` or ``TRUST_MARK_INVALID``.
A ``TRUST_MARK_INVALID`` outcome on the registration Trust Mark means that the entity is not authorized to operate.
In this case the Trust Evaluator MUST treat the entity as not authorized and MUST NOT proceed with the Entitlement Check.

**Process**

1. Verify that the issuer of the Trust Mark is authorized for that ``trust_mark_type``, according to the ``trust_mark_issuers`` claim of the Federation Trust Anchor Entity Configuration.
   The registration Trust Mark, that is a Trust Mark whose ``trust_mark_type`` has the ``registration-entity`` purpose, is subject to two additional checks.
   The Trust Mark Validation verifies that the ``trust_mark_type`` matches the expected registration identifier for the role of the subject, and that the issuer is the Federation Trust Anchor, since the registration Trust Mark MUST be issued only by the Federation Trust Anchor (see :ref:`infrastructure-trust:Trust Mark Types and Schema`).
2. Verify the Trust Mark signature with the Federation Entity Keys of its issuer, obtained through the Trust Chain when the issuer is not the Federation Trust Anchor.
3. Check the temporal validity of the Trust Mark through the ``iat`` and ``exp`` claims.
4. When online, check the Trust Mark status through the Federation Trust Mark Status endpoint (`OID-FED`_ Section 8.4).

Entitlement Check
"""""""""""""""""""""

The entitlements define what the entity is authorized to do, such as the Credential types it may issue or the attributes it may request.
Within IT-Wallet these authorization data are carried in the registration Trust Mark, in the ``entitlements``, ``provides_attestations`` and ``credentials`` claims defined in :ref:`infrastructure-trust:Trust Mark Types and Schema`, and MUST NOT be derived from the metadata alone.

**Input**

- The validated Trust Marks of the Trust Evaluated Party.
- The role of the Trust Evaluated Party and the action expected in the current interaction.
  At issuance, the type of Credential Issuer and the Credential types it declares to issue.
  At presentation, the Digital Credentials and the attributes requested by the Relying Party.

**Outcome**

The Trust Evaluator MUST output ``ENTITLEMENT_VALID`` or ``WRONG_ENTITLEMENT``.

**Process**

1. Extract the ``entitlements`` from the validated Trust Marks and verify that they match the role expected in the current interaction, for example that an entity acting as Credential Issuer holds an issuing entitlement of `ETSI TS 119 475`_ Annex A.2.
2. During issuance, verify that the offered Credential type is present in the ``provides_attestations`` of the Trust Mark, comparing the ``format`` and the ``meta`` of the offered Credential against the authorized entries.
3. During presentation, the attribute level check against the ``credentials`` of the Trust Mark is performed by the Overasking Check below.

Overasking Check
"""""""""""""""""

**Input**

- The presentation request.
- The ``credentials`` carried in the validated Trust Mark, that is the Credential queries the Relying Party is authorized to request.

**Outcome**

The Wallet Unit MUST output ``VERIFICATION_PASSED`` or ``OVERASKING_DETECTED``, identifying the unregistered attributes or Digital Credentials.
On ``OVERASKING_DETECTED`` the Wallet Unit MUST NOT disclose the attributes that are not authorized and MUST inform the User of the detected overasking.

**Process**

1. Extract the requested Digital Credentials and attributes from the request, from the DCQL query defined in `OpenID4VP`_ in the remote flow, or from the requested namespaces in the proximity flow.
2. For each requested Credential, select in the ``credentials`` of the Trust Mark the authorized entry with the same ``format`` and ``meta``, for example the same ``vct_values`` or ``doctype_value``.
3. Verify that every requested attribute is present in the ``claim`` paths of the selected authorized entry.
   If the request contains a Credential or an attribute with no corresponding authorized entry, the output is ``OVERASKING_DETECTED``.
4. Matching MUST be exact and case sensitive.

User Transparency
"""""""""""""""""

Beyond the automated checks above, the registration Trust Mark provides claims that are not evaluated as a decision rule but are presented to the User for transparency, to support the decision to proceed with the interaction before any attribute is disclosed.
Before the disclosure, the Wallet Unit MUST inform the User of the identity of the Relying Party and of the Digital Credentials and attributes requested, and it presents the additional transparency claims of the Trust Mark to support the informed decision.
This is consistent with the User approval that concludes the presentation, as defined in :ref:`trust-evaluation:Authorization Decision and Override Rules`.

The transparency claims carried in the Trust Mark are the following:

- ``organization_name``, the legal name of the entity;
- ``srv_description``, the description of the service provided by the entity;
- ``purpose``, the data processing purposes, for a Relying Party that requests Credentials;
- ``privacy_policy``, the URL of the privacy policy, for a Relying Party that requests Credentials;
- ``supervisory_authority``, the Data Protection Authority to which the User can report anomalies;
- ``public_body``, whether the entity is a public sector body;
- ``support_uri``, the contact for requests related to the entity, such as data deletion or portability.

Their definitions are provided in :ref:`infrastructure-trust:Trust Mark Types and Schema`.

When the Relying Party operates through a Relying Party Intermediary, the Wallet Unit MUST also inform the User that the Relying Party operates through that Intermediary, displaying the identity of both.
In the National Trust Framework the Intermediary is the Federation Intermediate in the Trust Chain of the Relying Party, registered with the ``intermediate`` Trust Mark (see :ref:`infrastructure-trust:Trust Mark Types and Schema`), and it is therefore identifiable from the validated Trust Chain without additional artifacts.

Metadata Retrieval and Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The metadata of a Federation Entity MUST be consumed only in their final form, that is the metadata resulting from the application of the metadata policies to the metadata published in the Entity Configuration, along the validated Trust Chain (see :ref:`trust-evaluation:Federation Trust Chain`).
The metadata published in the Entity Configuration MUST NOT be used without this processing.

The metadata types and their parameters are defined in :ref:`infrastructure-trust:Entity Type Identifiers and Metadata` and in the protocol specifications referenced there.

The Wallet Unit configuration is provided by the Wallet Provider within its metadata as defined in :ref:`wallet-solution-metadata:Wallet Solution Metadata`.

**Input**

- A validated Trust Chain about the subject (see :ref:`trust-evaluation:Federation Trust Chain`).

**Outcome**

- The final metadata of the subject, for each metadata type relevant to the interaction.

**Process**

1. Apply the ``metadata_policy`` of the superior statements to the metadata published in the subject Entity Configuration, along the Trust Chain, according to `OID-FED`_ Section 6.1, obtaining the final metadata.
2. Select the metadata type corresponding to the role of the subject in the interaction.
3. Verify the presence of the parameters that are REQUIRED for that metadata type.
4. Use the endpoints, the keys and the algorithms only from the final metadata.

When the metadata are obtained through a statically provided Trust Chain, they MUST be refreshed when the Trust Chain expires, as defined in :ref:`trust-evaluation:Federation Trust Chain`.

.. note::
  Within IT-Wallet the ``metadata_policy`` covers only the technical configuration parameters, such as endpoints, cryptographic keys and supported algorithms.
  Entitlements and authorization policies MUST NOT be expressed through metadata policies; they are carried by the Trust Marks, as defined in :ref:`trust-evaluation:Authorization`.
