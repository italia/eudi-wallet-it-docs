.. include:: ../common/common_definitions.rst
.. Included via index.rst at title level '=' (document title).


General Log Retention Policies
=======================================

The retention of logs is a key element for ensuring security, including fraud prevention, incident detection, system integrity, and compliance with applicable legal obligations. It MUST also be aligned with the requirements defined in ISO/IEC 27001, in particular with regard to auditability, access control, and secure storage. As long as log management may involve the processing of personal data, it also constitutes a measure of accountability under the GDPR, with implications for data minimization, storage limitation, and purpose limitation; for these aspects, reference is made to the relevant provisions of the GDPR and sector-specific regulations.

For all matters related to log handling, Wallet Providers, Credential Issuers, Authentic Sources, and Relying Parties are considered Organizational Entities.

Logs related to Wallet data exchange activities (e.g., accesses and transactions for Credential issuance and presentation) concerning the User, as the data subject, MUST be retained for a limited period for security, fraud prevention, dispute resolution, and legal obligations. Logs of Authentic Sources that document the provision of data to Credential Issuers for the issuance of Electronic Attestations of Attributes in the IT-Wallet System MUST be retained for a limited period for the same purposes.

Organizational Entities are responsible for log retention according to their respective roles. Solutions related to Wallet Providers, Credential Issuers, Authentic Sources, and Relying Parties MUST implement audit logging for the activities of administrators and service operators with access to data exchange processes and logs.

Unless specific legal obligations dictate otherwise, and with the definition of sector-specific regulation defining appropriate motivations, **the maximum retention period for data logs is 12 months**. Logs MUST be securely stored to ensure integrity and immutability.

ISO/IEC 27001 Logging General Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Organizational Entities MUST implement appropriate technical and organizational measures in compliance with ISO/IEC 27001 for maintaining an information security management system for monitoring, auditing, and incident response. Key aspects of log handling under ISO/IEC 27001 include the following requirements:

- **A.12.4 Logging and Monitoring**: Organizational Entities MUST produce logs that record exceptions, faults, and information security events. When necessary for security reasons, logs SHOULD capture user activities with a level of detail that is appropriate and sufficient to meet security requirements, ensuring that the data collected is relevant and not excessive. Logs SHOULD be reviewed regularly to ensure that security incidents are identified and addressed promptly.

- **A.12.4.1 Event Logging**: Organizational Entities MUST establish procedures for logging events, including the types of events to be logged, the information to be captured, and the retention period for logs.

- **A.12.4.2 Protection of Log Information**: Log information MUST be protected against unauthorized access and tampering. This includes implementing access controls, encryption, and integrity checks to ensure that log data remains secure and reliable.

- **A.12.4.3 Administrator and Operator Logs**: Activities of system administrators and operators MUST be logged and reviewed regularly. Organizational Entities MUST detect unauthorized activities and ensure accountability for actions taken on critical systems.

- **A.12.4.4 Clock Synchronization**: All Organizational Entities' systems involved in logging MUST be synchronized to a reliable time source, ensuring accurate timestamps for correlating events across different systems and conducting effective forensic investigations.

- **A.16.1.7 Information Security Incident Management**: Organizational Entities MUST ensure that logs are available and reliable to support incident management processes.


Wallet Provider Log Retention Policy
------------------------------------

Information related to the registration and management of Wallet Instances can be retained for up to 12 months after the deactivation/revocation of the Wallet or the associated User account, unless legal obligations require longer retention.


Credential Issuer Log Retention Policy
--------------------------------------

Credential Issuers define the retention period for Credentials based on sector-specific regulations. In the absence of specific regulations, the retention period for Credentials SHOULD NOT exceed 12 months after the date of expiration, configured at time of issuance within the metadata of the Issuer Signed part of the Credential.


Authentic Source Log Retention Policy
-------------------------------------

Authentic Sources are Organizational Entities for the purposes of this chapter: relevant logs cover accesses and transactions on endpoints and services used to provide Credential Issuers with the official data used to generate Electronic Attestations of Attributes in the IT-Wallet System, including—where applicable—e-services exposed via the National Digital Data Platform (`PDND`_).

Unless specific legal obligations or sector-specific regulations require otherwise, the **12-month** maximum retention period stated in the introductory section applies to these logs. GDPR requirements on minimization, storage limitation, and lawful basis for processing remain applicable in all cases.


Relying Party Log Retention Policy
----------------------------------

Relying Parties MAY retain logs related to the processing of data received from the Wallet only for the duration necessary to provide the requested service. The maximum retention period is 24 months after the conclusion of the service or the expiration date of the presented Credentials, unless legal obligations require otherwise.


- Relying Parties SHOULD NOT log Credential presentation disclosure maps, where not necessary.

Wallet Instances Logging Features
---------------------------------

In addition to the requirements included in the Consolidated Regulation (EU) No 910/2014, Art 5a 4(d) and the additional information provided within the Recitals (11) and (13), the Commission Implementing Regulation (EU) 2024/2979 establishes detailed rules for the application of Consolidated Regulation (EU) No 910/2014, including logging in the core functionalities of European Digital Identity Wallets.

Regulation (EU) 2024/2979, Article 9, which define logging obligations about Wallet Solutions and data portability mechanisms.


