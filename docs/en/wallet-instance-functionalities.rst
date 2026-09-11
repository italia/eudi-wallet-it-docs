.. include:: ../common/common_definitions.rst
.. Included via wallet-instance.rst at title level '=' (document title).


Wallet Instance Functionalities
===============================

A Wallet Instance, MUST support the following functionalities:

  - Wallet Registration (detailed in :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`),
  - Wallet Instance Attestation Issuance (detailed in :ref:`wallet-instance-attestation-issuance:Wallet Instance Attestation Issuance`),
  - Key Attestation Issuance (detailed in :ref:`wallet-attestation-issuance:Key Attestation Issuance`),
  - Wallet Revocation (detailed in :ref:`wallet-instance-revocation:Wallet Instance Revocation`) and
  - Deletion of presented attributes (detailed in :ref:`user-attribute-deletion:User's Attributes Deletion`).

Each functionality is described in detail in the following sections.

.. note::
  The details provided below are non-normative and are intended to clarify the functionalities of the Wallet Instance Registration. The actual implementation may vary based on the specific use case and requirements of the Wallet Provider.

.. toctree::
  :caption: Wallet Instance Functionalities Table of Contents
  :maxdepth: 3

  wallet-instance-registration.rst
  wallet-instance-attestation-issuance.rst
  wallet-attestation-issuance.rst
  wallet-instance-revocation.rst
  user-attribute-deletion.rst
  wallet-instance-dashboard.rst


