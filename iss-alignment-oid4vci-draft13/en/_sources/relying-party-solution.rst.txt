



.. _relying-party-solution:

Relying Party Solution
+++++++++++++++++++++++

This section describes how a remote Relying Party or a Verifier App requests to a Wallet Instance the presentation of the PID/EAAs.

In this section the following flows are described:

- :ref:`Remote Flow`, where the User presents a Credential to a remote Relying Party according to `OpenID4VP`_ Draft 20. In this scenario the user-agent and the Wallet Instance can be used in the same device (**Same Device Flow**), or in different devices (**Cross Device Flow**).
- :ref:`Proximity Flow`, where the User presents a Credential to a Verifier App according to ISO 18013-5. The User interacts with a Verifier using proximity connection technologies such as QR Code and Bluetooth Low Energy (BLE).

.. include:: remote-flow.rst

.. include:: proximity-flow.rst

