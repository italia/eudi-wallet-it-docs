.. include:: ../common/common_definitions.rst
.. Included via wallet-solution.rst at title level '=' (document title).


Wallet Solution Components
==========================

.. note::
  Tests related to the Wallet Solution components (Wallet Backend, and Wallet Unit) are summarized in :ref:`WP_012 <wallet-provider-backend-testcases>`, and :ref:`WP_013 <wallet-instance-testcases>`, accordingly.

Wallet Backend
--------------

Frontend Component
^^^^^^^^^^^^^^^^^^

The Frontend Component MUST provide a web-based User interface for Wallet Instance management, offering functionality to:

- Display and verify Wallet Instances and their status.
- Manage Wallet Instance lifecycle (e.g., revocation).
- Provide User support and documentation.

API Interface
^^^^^^^^^^^^^

This component MUST:

- forward the request from the Frontend Component or the Wallet Instance to the Wallet Instance Lifecycle Management component.
- use PDND according to rules in Section :ref:`e-service-pdnd:e-Service PDND` to be notified by the PID/IT-Wallet ID Provider of the need to revoke the Wallet Instance and delete the User's account due to the User's death.

Wallet Instance Lifecycle Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This component MUST handle:

- Wallet Instance Registration (detailed in :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`).
- Wallet Instance Attestation Issuance (detailed in :ref:`wallet-instance-attestation-issuance:Wallet Instance Attestation Issuance`)
- Key Attestation Issuance (detailed in :ref:`wallet-attestation-issuance:Key Attestation Issuance`).
- Status management (maintaining and updating validity).
- Revocation processes (implementing mechanisms to revoke Wallet Instances), according to Section :ref:`wallet-instance-revocation:Wallet Instance Revocation`.

Trust & Security Component
^^^^^^^^^^^^^^^^^^^^^^^^^^

This component MUST ensure security through:

- Key and certificate management.
- Audit logging.
- Security monitoring and incident response.
- Compliance with IT-Wallet Federation security requirements.


Wallet Unit
-----------

User Interface
^^^^^^^^^^^^^^

The User Interface is the point of interaction and communication between the User and the Wallet Instance.

Wallet Instance Lifecycle Management Component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Interacting with the Wallet Backend, this component MUST handle:

- Wallet Instance Registration (detailed in :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`).
- Wallet Instance Attestation Issuance (detailed in :ref:`wallet-instance-attestation-issuance:Wallet Instance Attestation Issuance`)
- Key Attestation Issuance (detailed in :ref:`wallet-attestation-issuance:Key Attestation Issuance`).
- Status management (maintaining and updating validity).
- Revocation processes (implementing mechanisms to revoke Wallet Instances), according to Section :ref:`wallet-instance-revocation:Wallet Instance Revocation`.

Based on the status of the Wallet Instance and the User request, this component interact with the other Wallet Instance components.

Issuer Component
^^^^^^^^^^^^^^^^

Following the `OpenID4VCI`_ specification and the implementation profile in Section :ref:`credential-issuance:Digital Credential Issuance`, this component MUST implement the Digital Credential issuance protocols and flows to request Digital Credentials to Credential Issuers.

Presentation Component
^^^^^^^^^^^^^^^^^^^^^^

Following the implementation profile in Section :ref:`credential-presentation:Digital Credential Presentation`, this component MUST be compliant with remote flows based on `OpenID4VP`_ and proximity flow based on `ISO18013-5`_.

Backup and Restore Component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For each Digital Credential that is issued to the Wallet Instance, this component MUST add all data that is necessary to request issuance of that Digital Credential during restore as specified in Section :ref:`backup-restore:Backup and Restore`.

.. note::
   Currently the re-issuance of the PID and IT-Wallet ID is not managed by the Backup and Restore Component.

Dashboard and Transaction Log
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This component MUST provide the Wallet Unit dashboard and transaction log functionality. In particular, this component MUST:

- provide a user-accessible interface enabling the User to access transaction transparency information;
- maintain a transaction log of transactions executed through the Wallet Unit, including non-completed transactions;
- support User interaction with transaction records, including viewing, export, and deletion.

Secure Storage
^^^^^^^^^^^^^^

The Wallet Instance MUST use this component to protect critical assets and to securely execute cryptographic functions.


Wallet Solution Interaction Patterns
====================================

The Wallet Solution supports these interaction patterns:

1. **User to Wallet Backend Frontend**: Web-based interactions for Wallet Instance management.
2. **Wallet Instance to Wallet Backend API**: for Wallet Instance registration, Wallet Instance Attestation and Key Attestation issuance.
3. **PID/IT-Wallet ID Provider to Wallet Backend API**: Secure API calls to request Wallet Instance revocation.
4. **User to Wallet Instance User Interface**: for Digital Credential management (issuance, presentation, backup, restore, deletion).
5. **Wallet Instance to Relying Party**: for Digital Credential presentation.


