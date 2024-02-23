



.. _relying-party-solution:

Relying Party Solution
+++++++++++++++++++++++

This section describes how a remote Relying Party or a Verifier App requests to a Wallet Instance the presentation of the PID/EAAs.

In this section the following flows are described:

- :ref:`Remote Flow <remote_flow_sec>`, where the User presents a Credential to a remote Relying Party according to `OPENID4VP`_. In this scenario the user-agent and the Wallet Instance may be used in the same device (**Same Device Flow**), or in different devices (**Cross Device Flow**).
- :ref:`Proximity Flow <proximity_flow_sec>`, where the User presents a Credential to a Verifier App according to ISO 18013-5. The User interacts with a Verifier using proximity connection technologies such as QR Code and Bluetooth Low Energy (BLE).

.. include:: remote-flow.rst

.. include:: proximity-flow.rst


