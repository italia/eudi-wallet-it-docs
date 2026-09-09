.. include:: ../common/common_definitions.rst
.. Included via wallet-solution.rst at title level '^' (level 2).

Wallet Instance
^^^^^^^^^^^^^^^

The Wallet Instance establishes a strong and reliable mechanism for the User to engage in various digital transactions in a secure and privacy-preserving manner.

The Wallet Instance establishes trust with PID and (Q)EAA Providers by consistently presenting Wallet Instance and Key Attestations during interactions.
These verifiable attestations, provided by the Wallet Provider, serve to authenticate the Wallet Instance itself, ensuring the trustworthiness of the secure storage environment: the **Keystore** for all device-bound Digital Credentials, and the **WSCA** operating within a **Remote WSCD** (remote HSM) exclusively for the PID at Level of Assurance High. They also verify that the Wallet Instance has not been revoked and ensure its reliability when engaging with other ecosystem actors.


.. toctree::
  :caption: Wallet Instance Table of Contents
  :maxdepth: 3

  wallet-instance-lifecycle.rst
  wallet-instance-functionalities.rst


