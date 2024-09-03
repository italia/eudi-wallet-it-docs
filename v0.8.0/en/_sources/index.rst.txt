.. include:: ../common/common_definitions.rst

==============================================
The Italian EUDI Wallet implementation profile
==============================================

Introduction
------------

The European Parliament `has adopted <https://www.europarl.europa.eu/doceo/document/A-9-2023-0038_EN.html#_section1>`_ the revision of the eIDAS Regulation concerning electronic identification and trust services, introducing a significant innovation: the `European Digital Identity Wallet <https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/europe-fit-digital-age/european-digital-identity_en>`_. This update marks a pivotal advancement in the EU's digital strategy, aiming to enhance the security, interoperability, and usability of digital identities across Member States. For further details, resources, and notes on this legislative development, please refer to the official EU Commission and Parliament websites.

Italy has launched the National digital identity Wallet solution, known as IT-Wallet, established by the Legislative Decree of March 2, 2024, No. 19 (commonly referred to as the PNRR Decree)., in direct response to the European community's directives. This initiative ensures full interoperability with the digital identity solutions provided by other European Member States, aligning with European regulations.

The purpose of the following technical rules is to define the technical architecture and reference framework to be used as a guideline by all the parties involved in the development of the IT-Wallet project.

This documentation defines the national implementation profile of IT-Wallet, containing the technical details about components of the Wallet ecosystem, as listed below:

 - Entities of the ecosystem according to `EIDAS-ARF`_.
 - Infrastructure of trust attesting realiability and eligibility of the participants.
 - PID and EAAs data schemes and attribute sets.
 - PID/EAA in MDL CBOR format.
 - PID/EAA in `SD-JWT`_ format.
 - Wallet Solution general architecture.
 - Wallet Attestation.
 - Issuance of PID/EAA according to `OpenID4VCI`_.
 - Presentation of PID/EAA according to `OpenID4VP`_.
 - Presentation of pseudonyms according to `SIOPv2`_.
 - PID/EAA backup and restore mechanisms.
 - PID/EAA revocation lists.

Index of content
----------------

.. toctree:: 
   :maxdepth: 3
   
   ssi-introduction.rst
   defined-terms.rst
   trust.rst
   wallet-solution.rst
   wallet-attestation.rst
   pid-eaa-data-model.rst
   pid-eaa-issuance.rst
   pid-eaa-entity-configuration.rst
   authentic-sources.rst
   relying-party-solution.rst
   relying-party-entity-configuration.rst
   revocation-lists.rst
   pseudonyms.rst
   backup-restore.rst
   algorithms.rst
   contribute.rst
   standards.rst

