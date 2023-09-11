.. include:: ../common/common_definitions.rst

=============================================
Italian EUDI Wallet Technical Specifications
=============================================

Introduction
------------

The European Council requested the update of the 
eIDAS Regulation on electronic identification and trust services by 
implementing a new tool: the `European Digital Identity Wallet <https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/europe-fit-digital-age/european-digital-identity_en>`_.

Italy responded to the input received from the European community by creating the National digital identity Wallet solution, called IT Wallet, to be fully interoperable with all the other solutions made available by other European Member States and in full compliance to the European regulation.

The current Italian scenario counts 3 coexisting digital identity tools that are partially overlapping, sometimes competing, and based on different technologies. This points to a highly fragmented system which yields difficulties for users and service providers. Therefore, the IT Wallet proposes to rationalise the digital identity ecosystem in Italy in order to simplify the experience of citizens, public administrations, and businesses in accessing digital services.

To achieve these objectives and enhance the already active and eIDAS-notified digital identity schemes, the IT Wallet project entails a technological and governance evolution that envisages the progressive migration of the current threefold digital identification solution towards IT Wallet.

The purpose of the following technical rules is to define the technical architecture and reference framework to be used as a guideline by all the parties involved in the development of the IT Wallet project.

This documentation defines the national implementation profile of EUDI Wallet, containing the technical details about components of the Wallet ecosystem, as listed below:

 - Entities of the ecosystem according to `EIDAS-ARF`_.
 - Infrastructure of trust attesting realiability and eligibility of the participants.
 - PID and EAAs data schemes and attribute sets.
 - PID/EAA in MDL CBOR format.
 - PID/EAA in `SD-JWT`_ format.
 - Wallet Solution general architecture.
 - Wallet Instance Attestation.
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
   pid-eaa-data-model.rst
   pid-eaa-issuance.rst
   wallet-solution.rst
   wallet-instance-attestation.rst
   relying-party-solution.rst
   pseudonyms.rst
   backup-restore.rst
   revocation-lists.rst
   algorithms.rst
   contribute.rst
   standards.rst

