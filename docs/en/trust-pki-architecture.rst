.. include:: ../common/common_definitions.rst
.. Included via infrastructure-trust.rst at title level '-' (level 1).

PKI Architecture
----------------

The Trust Artifacts of both Trust Frameworks are signed with keys whose public part is certified by a Certification Authority.
This section provides the architectural view of these Certification Authorities.
It defines which of them are operated within IT-Wallet, which certificates each one issues, and which Trust Anchor is derived from each one and through which channel that Trust Anchor is distributed.

The content of the certificates is not defined here.
The common requirements are defined in :ref:`infrastructure-trust:X.509 Certificate Profile` and the specific requirements of each certificate are defined together with the artifact that uses it.
The issuance of the certificates is part of the onboarding (see :ref:`onboarding-system:Onboarding Processes`).
The use of the Trust Anchors at runtime is defined in :ref:`trust-evaluation:EUDIW Trust Anchor Validation` for the EUDIW Trust Framework and in :ref:`trust-evaluation:Signing Trust Anchor Distribution`, :ref:`trust-evaluation:Wallet Trust Anchor Distribution` and :ref:`trust-evaluation:Authentication Trust Anchor Distribution` for the National Trust Framework.

Certification Hierarchies
^^^^^^^^^^^^^^^^^^^^^^^^^

Within IT-Wallet a single national Root Certification Authority is operated.
It issues the certificates of the subordinate Certification Authorities and it is not used for any other purpose.
Each subordinate Certification Authority serves one service, and its certificate is the Trust Anchor published for that service.

.. _fig_pki_architecture:
.. plantuml:: plantuml/pki-architecture.puml
    :width: 99%
    :align: center
    :alt: The figure illustrates the certification hierarchies of the IT-Wallet ecosystem and the publication channel of the Trust Anchor derived from each Certification Authority.
    :caption: `PKI Architecture of the IT-Wallet Ecosystem. <https://www.plantuml.com/plantuml/svg/dLPHRzis47xNhpYq3tvPx2tOWAqFHHN7NhDagM8xy1u23BHqaeZGP41I3hoW_tqyIYP4EuxRAa02alTztztn8vbFnZ9jcxL81Z16RNd9SsQvab1pr4pdxey19WjuQbPYjvRNJ4eKe4gmDKA1cc-mW8LkZ8LKvhNIPfWavf7B9wRP6apD2lNCPGKb4mPxAmMMh15sggIzPMk4poWsQ9tGwp5p_X_2B-UznLHhzJnMGcbu_wl_UeiQSyja9H1U4e0BbZzMMZMoQEENDRT8yqgx4cAEhpsM9uTZrUiSxwSf_Uop_Eu_D-kJjbk1i5AYSBI9mDA2LQ1vLLieEEN8bKoIdSoxMqOJJ41sVVKEc87RTE744mZrz8DcIbaOfmzoD59bARZ4dq0rrl02_UvicE253tQ5s7eqyfIpBryMUupPrILaMcqSKCESLt8qHoOwwcEBmJDeMcON_wyBdiVSIoO4skFqyVffXMNc-FSaPbawzdHfdgCnaFUGPDLMuso6OajEp9XRTYk1al17UfmsjaPfE_ztEVU9ji3YaFpLjDFxnUU3h6VZWtQ4yK4HJYHqYSOUt-iB3ME56LRSMCqEcnvMJhPxDldpI6ScQNh0UwdoPetI-WNKHthXaCdNdkll6YPSLBX7vgWtFCTGhSVTBUOPlCIv160dV-UOlzr9Ts-JPSt5sNVnPVSNKLcJ-ykhPLVILBCrFYlzw8DTvEGUNeuVGlCWRxY3gRB5Om4JQJcvrXFSq45xyvoTPl07QH1b45TyceDAZhC8K0BvStMImqUzpJ8xoVAc_K-23qp-DwvNjEEMMGmW8Y5ZfDhot4MTdnCbNbscyz6eOrhSH1O8X-M82_pr7ajFqHNkOT6h-Y1zpbiOArdogcb3EjNfXCmWbQMtnbgrTYE0HOtGO-lmrxWrm3IspxgfiI2ElvRN7iEblsTUqp93OjmIbgJWd-5lF_z1eFYcOh888ToOnl6l72Z-7uDW_cfLskaCtH1bqHO0r41we-3ix6DuKleJoomUad-Y6RfhzqDcKGZjU3IcAodfn60u_DYTCA_MZacsFUGqRhTwfqupmSdnPA2X548SfTDcqKrHFdGbHTn1skqlV83mLYwqQNQ-68sIhkAzsF1mnLuA62evXlYtXyjgFpOPzAr5dc-Tw-Q_tsI37p7PuCTCDeXDDWWcInA15Gt2QPahmObIg-SFBQEX7FkgkpVOD2kb2ovfAjAB3Nt9NDc1qjP7WoCDRgAMHLi1N0uJbtMRU_B9_MhMudy0>`_

The following table lists the Certification Authorities, the certificates that are issued by each of them, and the channel through which the derived Trust Anchor is distributed.
The Lists of Trusted Entities and the Trusted Lists named in the table are defined in :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`.

.. _table_pki_certification_authorities:
.. list-table:: Certification Authorities and Derived Trust Anchors
    :class: longtable
    :widths: 24 38 38
    :header-rows: 1

    * - **Certification Authority**
      - **Issued Certificates**
      - **Trust Anchor Distribution**

    * - PID Provider Sign/Seal CA
      - :ref:`infrastructure-trust:PID Provider Sign/Seal Certificate`
      - PID Providers LoTE.

    * - Wallet Provider Sign/Seal CA
      - :ref:`infrastructure-trust:Wallet Provider Sign/Seal Certificate`
      - Wallet Providers LoTE in the EUDIW Trust Framework, and the Federation Trust Anchor Entity Configuration as the distribution channel for the National Wallet Trust Anchor in the National Trust Framework (see :ref:`trust-evaluation:Wallet Trust Anchor Distribution`).

    * - WRPAC CA
      - Access certificates following the :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`, issued to the Wallet-Relying Parties.
      - Providers of WRPAC LoTE.
        The same Trust Anchor is also published in the PID Providers LoTE, because the trust anchors of the Access Certification Authorities for PID Providers are notified within the PID Provider notification, separately from the ones for the Wallet-Relying Parties (see [`EIDAS-ARF`_], Topic 31).

    * - National Authentication CA
      - Relying Party authentication certificates used in the Proximity Flow.
        They follow the same profile as the Wallet-Relying Party Access Certificate.
      - Entity Configuration of the Federation Trust Anchor, as Authentication Trust Anchor (see :ref:`trust-evaluation:Authentication Trust Anchor Distribution`).

    * - WRPRC Sign/Seal CA
      - The Sign/Seal Certificate of the Provider of WRPRC (see :ref:`infrastructure-trust:Wallet-Relying Party Registration Certificate (WRPRC) Profile`).
      - Providers of WRPRC LoTE.

    * - Registrar Sign/Seal CA
      - :ref:`infrastructure-trust:Registrar Sign/Seal Certificate Profile`
      - Registrar LoTE.

    * - National EAA Sign/Seal CA
      - :ref:`infrastructure-trust:(Q)EAA Provider Sign/Seal Certificate`, for the Digital Credentials anchored to the National Trust Framework.
      - Entity Configuration of the Federation Trust Anchor, as Signing Trust Anchor (see :ref:`trust-evaluation:Signing Trust Anchor Distribution`).
        For an EAA issued in the EUDIW Trust Framework the Trust Anchor is referenced in the Attestation Rulebook, as described in :ref:`infrastructure-trust:Trust Anchor Certificate Profile`.

    * - Qualified CA of the QEAA Provider
      - :ref:`infrastructure-trust:(Q)EAA Provider Sign/Seal Certificate`, for the QEAA.
      - Member State Trusted List, published in accordance with Article 22 of [`EIDAS`_].

    * - Qualified CA of the PuB-EAA Provider
      - :ref:`infrastructure-trust:PuB-EAA Provider Sign/Seal Certificate`, the qualified certificate supporting the qualified electronic seal of the public sector body (Article 45f(1)(b) of [`EIDAS`_]).
      - Member State Trusted List, published in accordance with Article 22 of [`EIDAS`_].

The Qualified CA of the QEAA Provider and the PuB-EAA Provider Sign/Seal CA are not subordinate to the national Root Certification Authority.
Both belong to the perimeter of a Qualified Trust Service Provider and follow its own supervision and publication regime.
The Sign/Seal Certificate of a PuB-EAA Provider is a qualified electronic seal issued by a Qualified Trust Service Provider (Article 45f of [`EIDAS`_]).

Revocation Trust Anchors
""""""""""""""""""""""""""

Within these specifications, the following additional conditions apply regarding revocation Trust Anchors:

- Within the EUDIW Trust Framework, the Trust Anchors used to validate the revocation mechanisms for WRPRC, PID and PuB-EAA certificate chains are the same notified Trust Anchors used by the corresponding signing PKIs.
- Within the National Trust Framework, the Signing Trust Anchors of EAA Providers are also the Trust Anchors used to validate the revocation status of EAA signing certificate chains.
- For Wallet Instance Attestations and Key Attestations, the Wallet Provider MUST use the same Trust Anchor for signature validation and for validation of the applicable status or revocation information. In the EUDIW Trust Framework, this Trust Anchor is published in the Wallet Providers LoTE; in the National Trust Framework, the same key material is distributed as the National Wallet Trust Anchor through the Federation Trust Anchor Entity Configuration (see :ref:`trust-evaluation:Wallet Trust Anchor Distribution`).
- When a Wallet Provider operates in both Trust Frameworks, its National Wallet Trust Anchor MUST be the same certificate as the Trust Anchor notified to the European Commission and published in the Wallet Providers LoTE under the Wallet Provider's ``ServiceDigitalIdentity``. The national Entity Configuration is an additional distribution channel and MUST NOT introduce a second Trust Anchor.

.. note::
  The Certification Authority that issues the Wallet-Relying Party Access Certificates and the Certification Authority that issues the Relying Party authentication certificates of the National Trust Framework use the same certificate profile.

.. note::
  The Federation Entity Keys are not certified by the Certification Authorities described in this section.
  The binding between a Federation Entity and its keys is provided by the Entity Configuration and by the Subordinate Statement issued by its superior, which are validated through the Federation Trust Chain and not with a certification path (see :ref:`infrastructure-trust:National Trust Artifacts`).
  The Entity Configuration of the Federation Trust Anchor is used as a distribution channel for the Trust Anchors of the X.509 hierarchies.

Design Principles
^^^^^^^^^^^^^^^^^

The hierarchies described above follow the principles listed below.

- **One Sign/Seal Certification Authority per notified role.** Each role that signs or seals an artifact has a distinct Sign/Seal Certification Authority.
- **A single WRPAC Certification Authority.** Within IT-Wallet the access certificates are issued by a single Certification Authority, both to the Wallet-Relying Parties and to the PID Providers, as they follow the same profile and certificate policy.
  The Relying Party authentication certificates of the National Trust Framework are issued by a distinct Certification Authority.
- **No Trust Anchor without a consumer.** Within IT-Wallet a Trust Anchor is published in a distribution channel only when a trust evaluation procedure defined in this specification obtains it from that channel.
- **The Root Certification Authority is outside the validation path.** The Trust Anchor certificate is the trust termination point of the path validation (see :ref:`infrastructure-trust:Trust Anchor Certificate Profile`), therefore the Root Certification Authority is never evaluated at runtime and its certificate is not published in any List.
  It provides a common governance to the subordinate Certification Authorities and no trust relationship by itself.
  A compromise of the Root Certification Authority is not detected by the ordinary path validation, and within IT-Wallet it is managed by re-issuing and re-notifying the affected Trust Anchors.
- **Only end entities below a published Trust Anchor.** Within IT-Wallet the published Trust Anchor is the subordinate Certification Authority of the service, and no further Certification Authority layer is issued below it.
  This is consistent with the ``pathLenConstraint`` recommendation of :ref:`infrastructure-trust:Trust Anchor Certificate Profile`.
- **Separation of the keys by purpose.** A Trust Anchor published for one purpose is not used to certify the artifacts of another purpose.
  A verifying entity has to be able to distinguish which Trust Anchors are usable for which category of Attestation, as required by [`EIDAS-ARF`_].
