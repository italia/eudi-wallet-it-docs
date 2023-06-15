.. include:: ../common/common_definitions.rst

=============================================
Italian eIDAS Wallet Technical Specifications
=============================================

[TODO INTRO]

Introduzione

cos'è eIDAS

cos’è IT-Wallet

scopo delle regole tecniche


In this documentation you can find the technical specification 
for implementing the following components:

 - Entities of the ecosystem according to `EIDAS-ARF`_.
 - Infrastructure of trust attesting realiability and eligibility of the participants.
 - PID and EAAs data schemes and attribute sets.
 - PID/EAA in MDL CBOR format.
 - PID/EAA in `SD-JWT`_ format.
 - Wallet Solution general architecture.
 - Wallet Instance Attestation data model in `JWS`_ format.
 - Issuance of PID/EAA according to `OpenID4VCI`_.
 - Presentation of PID/EAA according to `OpenID4VP`_.
 - Presentation of pseudonyms according to `SIOPv2`_.
 - PID/EAA backup and restore mechanisms.
 - PID/EAA revocation lists.


Index of content
----------------

.. toctree:: 
   :maxdepth: 2
   
   ssi-introduction.rst
   defined-terms.rst
   trust.rst
   pid-data-model.rst
   pid-issuing.rst
   wallet-solution.rst
   wallet-instance-attestation.rst
   issuance.rst
   presentation.rst
   pseudonyms.rst
   backup-restore.rst
   revocation-lists.rst
   algorithms.rst
   contribute.rst
   standards.rst
