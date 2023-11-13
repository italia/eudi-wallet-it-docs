.. include:: ../common/common_definitions.rst

.. _backup-restore.rst:

EUDI Wallet Backup & Recovery
+++++++++++++++++++++++++++++

Introduction
------------

Section 4.2.4 of the eIDAS ARF v1 (EUDI Wallet Instance Lifecycle) states that the EUDI Wallet Instance becomes valid once it receives a valid PID. From this point, the User can receive and store one or more (Q)EAAs in the Wallet. Therefore, it is crucial to have a backup and recovery strategy for the Wallet Solution. Backup and recovery are distinct phases that occur during different parts of the Wallet Instance lifecycle and should be almost transparent to the User.

This document proposes a technical solution for the backup and restoration of digital credentials.

What data can be backed up
--------------------------

The ARF differentiates between Type 1 and Type 2 configurations. Type 1 is designed for PID and (Q)EAA with LoA High, while Type 2 may be used for QEAAs and EAAs. The primary difference between the two configurations is that Type 1 must use the holder key binding. A proof of possession - such as the one described in RFC7800[1] - is included in the PID; it consists of the User's device public key signed by the PID Provider. The corresponding User's device private key should be securely stored in the Secure Element[2] of the User's device (or a remote HSM when the SE is not available). By signing typically random information during the presentation phase to a Relying Party, the device can thus prove the legitimate possession of the PID.

Type 2 (Q)EAA, on the other hand, may include a public key for proof of possession, and, if it does, the corresponding private key may be exported if it is not stored on the Secure Element. A credential should either be holder-bound with a non-exportable key or not holder-bound at all.

Since the secure storage prevents the exportation of the private keys, it is mandatory not to export the Type 1 digital credentials outside the mobile device. Therefore, the data intended for backup considered in this document are the following:

* credential type;
* credential Issuer.

Type 2 credentials without holder key binding may be exported along with their serialized private key.

Backup methods
--------------

Given the sensitive nature of the data, backups must be encrypted. When encryption is applied, it should be done with a User-provided passphrase or any other means that the User has sole control over. 

The backup should be stored as a serialized file (hereafter referred to as the "Backup File") in an open format. The Backup File should include a timestamp in its name to facilitate chronological sorting, as illustrated in the non-normative example below: 

eudiwallet-backup-2023-02-01T08:03:11Z.eudiwb

The Wallet Solution could provide various methods for exporting the backup, including:

* a physically attached USB device (where available);
* a Wallet Solution integrated cloud backup;
* local saving on the device.

The User should have the ability to manually initiate a backup. Additionally, the Wallet Instance should periodically create these backups and save them locally. The operating system's backup mechanism will ensure the preservation of this data. As the backup is encrypted, the user can choose to move the locally saved file anywhere they wish, but should be warned of possible risks if the passphrase they chose is not secure enough[b].

Backup and Restore Approaches Comparison
----------------------------------------

The table below compares the different credential types with their Level of Assurance and their backup and restore methods. Each row has a unique identifier for referencing in the use cases.

.. list-table:: 
   :widths: 20 60
   :header-rows: 1

   * - **Credential Type**
     - **Holder Key Binding**
     - **LoA**
     - **Approach[d][f][g]**
     - **Unique ID**
   * - Type 1
     - True
     - High
     - Reissuance[h]
     - ID1
   * - Type 2
     - True
     - High
     - Reissuance
     - ID2
   * - Type 2
     - True
     - Substantial
     - Reissuance
     - ID3
   * - Type 2
     - -
     - Low
     - Copy credential and private key export/import
     - ID4
   * - Type 2
     - -
     - Low
     - Copy credential export/import
     - ID5

Backup content
---------------

The backup file consists of a structured document. The schema should contain at least:

* metadata
   * date and time of the backup  (using ISO8601 - simplified for the web[3])

   * content:
   * for each fully exportable Type 2 credential:
   * full credential content;
   * serialized holder private key in JSON Web Key[4] format.
   * for each Type 1 credential and for the non-exportable Type 2 credentials, the following references are exported:
   * credential type;
   * credential issuer.

The content should be encrypted and protected by a passphrase or other mechanisms. Below is a non-normative example of the content of a Backup payload, where the first entry must be the reference to the User's PID (its type and its issuer). 

Recover
-------

Recovering an EUDI Wallet from a Backup File may follow different flows depending on the backup method and configuration types. Each recovery always begins with the issuance of a new PID. Once the new Wallet Instance is in the valid state, the User is prompted for a recovery from a backup. The User chooses a backup recovery method (USB device, cloud[5], ...), the Wallet Instance then asks the User for the passphrase to unlock the Backup File, and analyze the content inside it.

When a Type 2 credential has a Cryptographic Holder Key Binding and the private key is backed up, the credential can simply be copied over on the new device together with its key, and continues to be valid and possession-provable.

Type 1 credentials for which the Backup File needs to be reissued.

Under the condition that at least one fresh PID has been reissued to the Wallet using the User authentication, a semi-automatic process follows the User for requesting and obtaining all the imported credentials.

User Experience
---------------

TBD

Here are a few notes:

   * the user must be prompted about which credential to export (interesting for the sharing use cases where me share the export of my Type 2 credential with LoA low, the laundry ticket, to Matteo)
________________
[1] https://datatracker.ietf.org/doc/html/rfc7800
[2] Any other alternative to the Secure Element, if approved in the ARF, must then be considered.
[3] https://www.w3.org/TR/NOTE-datetime
[4] https://datatracker.ietf.org/doc/html/rfc7517
[5] The authentication with the cloud storage backend should be based on Identity Linking and PID proof of possession as it happens with any other Relying Party during the presentation phase.
