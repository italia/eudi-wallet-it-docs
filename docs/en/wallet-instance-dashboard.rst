.. include:: ../common/common_definitions.rst
.. Included via wallet-instance-functionalities.rst at title level '=' (document title).


Wallet Instance Dashboard and Transaction Logging
=================================================

The Wallet Instance MUST maintain a secure, Wallet-local transaction log to ensure transparency, traceability, and User awareness of actions performed through the Wallet Instance as defined in `EIDAS-ARF`_ (Annex 2.02 HLRs, Topic 19). The log MUST cover all transactions (including non-completed) in these categories:

- credential issuance and re-issuance;
- credential presentation to Relying Parties;
- data deletion requests sent to Relying Parties.

For each such transaction, the Wallet Instance MUST create a corresponding transaction record with the data elements specified in the applicable ARF requirements for transaction logging for the corresponding transaction category, and update it with the final outcome where applicable as defined in `EUDI-TS 10`_.

For presentation transactions, attribute values MUST NOT be logged. If a presentation request contains sensitive transactional data (such as a payment or a digital signature), the Wallet Instance MUST log the value of such transactional data only to the extent explicitly required by `EUDI-TS 12`_ associated with the requested attestation and in accordance with data minimization principles. Where no such requirement exists, transactional data values MUST NOT be logged.

To support User access to the transaction log, the Wallet Instance MUST provide a dashboard interface, allowing the User to view an overview of transaction records in the log, access individual record details, export and delete records, and, where a transaction involves a Relying Party, initiate a data deletion request to the corresponding Relying Party (using logged contact information, if available).

The Wallet Provider MUST protect the confidentiality, integrity, and authenticity of the transaction log and of any exported log objects in accordance with `EUDI-TS 10`_; access to the log MUST be restricted to the User and the Wallet Instance.

Records MUST be retained for at least the minimum legal period as defined in :ref:`log-retention-policy:General Log Retention Policies`. If storage limits require automatic deletion, the Wallet Instance MUST notify the User via the dashboard, warn of consequences, and offer export of affected records before deletion.

Export and Deletion of Transaction Records
""""""""""""""""""""""""""""""""""""""""""

**Export**: The dashboard MUST allow the User to export one or more transaction records to a file using the common format and security measures defined in `EUDI-TS 10`_.

The exported file MUST be storable in an external or remote storage location of the User’s choice, from among the storage options supported by the Wallet Instance.

**Deletion**: The dashboard MUST allow the User to delete one or more transaction records from the Wallet Instance at any time.

Before deleting any transaction record, the Wallet Instance MUST display a clear warning to the User about the potential consequences for the User’s data protection rights.

Deletion of transaction records MUST:

- apply only to Wallet-local copies of the records;
- be irreversible for the Wallet Instance once completed.

The Wallet Instance MUST continue to protect any remaining transaction records in accordance with the confidentiality, integrity, and authenticity requirements defined for the transaction log in this section.

No entity other than the User MAY delete transaction records.


