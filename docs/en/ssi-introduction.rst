.. include:: ../common/common_definitions.rst

.. _ssi-introduction.rst:

ssi-introduction.rst
+++++++++++++++++++++++++++

Introduction to SSI
-------------------

**Definition**

Self-Sovereign Identity (SSI) refers to a new paradigm in Identity and Access Management (IAM). It consists of a digital identity model that, unlike existing identity management ecosystems, grants individuals complete control and ownership over their personal data.
Users possess their digital documents and determine to which actors they present these documents, with the ability to revoke the use of said documents, all while maintaining a history of their activities.

SSI is also significant in the field of data exchange and data governance. This is relevant at both national and European levels, including the new eIDAS Regulation. In fact, it envisions a login option designed for European Users - be they citizens, public administrations, or companies - who want to access another Member State's services using their national authentication systems.

The main roles in an SSI ecosystem are as follows:
 - Issuers: parties who can issue attributes or "credentials" about a person;
 - Verifiers: parties who request Holders' attributes because they want to know something about them;
 - Holders: individuals who own a Wallet and have control over the attributes they can acquire, store, and present to Verifiers;
 - Verifiable Data Registries: Authorities that publish certificates, attestations, metadata, and schemes needed for trust establishment between the parties.

**What it is useful for**

In the SSI model, the data source (e.g., an educational institution) provides credentials to the User, who can store them in their digital Wallet.
A secure Self-Sovereign Identity Wallet is crucial, as it allows people to carry their credentials on their digital devices. The Wallet typically comes in the form of an application on the User's mobile phone. Portability is, therefore, one of the principles of SSI.

Other key elements that characterize an SSI system include:
 - Privacy and control: SSI enables individuals to maintain control over their personal data. They can choose what information to release, to whom, and for what purpose. This reduces the risk of personal data being collected, stored, or misused;
 - Security: SSI leverages advanced cryptographic techniques to ensure the integrity and security of identity information. It avoids the risk of identity theft, fraud, and unauthorized access since the data remains under the individual's control and is not stored in a single vulnerable location;
 - Interoperability: SSI promotes interoperability by enabling different systems and organizations to recognize and verify identities without relying on a central authority. This allows for seamless and trusted interactions between individuals, organizations, and even across borders;
 - Efficiency and cost reduction: individuals can manage their own identities with SSI, eliminating the need for multiple identity credentials and repetitive identity verification processes. This can streamline administrative procedures, reduce costs, and enhance the user experience.

**Example**

When a User wants to purchase a service, the service provider asks the User for specific proof. Instead of presenting physical identification documents or disclosing their full data, the individual can use their SSI system.
An example of SSI in action could be a scenario where an individual needs to prove their age to access a restricted service, such as purchasing age-restricted items. They would release only the necessary information, such as a digitally signed proof of being above the legal age, without revealing any other personal details.
The verifier can then cryptographically validate the proof.
    

External references
-------------------

TODO
