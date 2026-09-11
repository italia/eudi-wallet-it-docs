.. include:: ../common/common_definitions.rst
.. Included via index.rst at title level '=' (document title).


Introduction
============

Over the last decade, digitalization has radically transformed the way citizens and businesses interact with public and private services, introducing new secure, accessible and user-friendly forms of service access.

In Italy, Decree-Law No. 19 of 2 March 2024, converted, with amendments, by Law No. 56 of 29 April 2024, introduced Article 64-quater of Legislative Decree No. 82 of 7 March 2005, establishing the Italian Digital Wallet System - IT-Wallet System. The IT-Wallet System allows natural or legal persons to access public and private services through the secure presentation of Digital Credential, attesting to entitlements, delegations, characteristics, licenses or qualifications. Article 64-quater also provides for the adoption of one or more implementing decrees (decreti attuativi) to define the rules governing the operation of the IT-Wallet System, including the roles of the entities involved, technical and security requirements, and principles of economic sustainability, of which these Technical Specifications – drafted through an open and collaborative process – form an integral part.

Thanks to the IT-Wallet System, natural and legal persons can directly provide, via their Wallet, the information required for accessing services provided by public and private entities in the form of Digital Credentials.
Similarly to a physical wallet, the IT-Wallet can contain identity or document-related data, such as a driver's license or health card, as well as a wide range of verifiable digital information, such as a professional qualification, educational diploma, licence or verifiable attribute.

The main roles in the Wallet ecosystem are listed as follow:

- **Credential Issuers**: parties who issue Digital Credentials to Users;
- **Relying Parties**: parties who request Digital Credentials presentations to the User, for Authentication and authorization purposes;
- **Users**: individuals who own a Wallet Instance and have control over the Digital Credentials they can request, acquire, store, and present to Relying Parties;

In this model, the Credential Issuer (e.g., an educational institution) provides Digital Credentials to the User, who can store them in their Wallet Instance.
The Wallet Instance is typically provided as a mobile application on the User's smartphone.

What distinguishes this new approach from previous identity access management systems is that Digital Credentials refer to characteristics, qualities or properties, already authenticated at source. These Digital Credentials can be used by the User without the Credential Issuers being aware of their use. During the use of the Digital Credentials, no usage information is released to third parties as the relationship is exclusive between the User and the Relying Party, in a transparent and informed manner.
The development of the IT-Wallet System includes a phased experimentation process, aimed at testing the Wallet and assessing its impact in real-world contexts. This process is designed to validate technical components, user experience elements, and interoperability mechanisms, while ensuring a progressive and controlled adoption of the System. Moreover, it supports the continuous improvement of the IT-Wallet and its gradual alignment with the European Digital Identity Wallet (EUDI Wallet), both in terms of architecture and compliance with evolving European specifications.

Other key elements that characterize this new Digital Identity Wallet paradigm include:

- **Confidentiality and control**: Wallets enable individuals to maintain control over the information provided within the presented Credentials. They can choose what attributes or Credentials to present and to whom;
- **Security**: Wallets leverage cryptographic mechanism for the integrity and the security of exchanged data. This avoids identity theft, fraud, and unauthorized access;
- **Interoperability**: Wallets promote interoperability by enabling different systems and organizations to recognize and verify identities, enabling trusted interactions between individuals, organizations, and even across borders;
- **Efficiency and cost reduction**: Individuals can easily manage their own Credentials, avoid handling multiple identity tokens, and reduce repetitive identity verification processes.

Scope
-----

These Technical Specifications are intended to complement the Guidelines provided for in Article 64-quater of Legislative Decree No. 82/2005 (CAD). Both the Guidelines and these Technical Specifications, once formally adopted, will become part of the regulatory framework for the IT-Wallet System. They will be periodically updated, where necessary, in light of the results of the experimentation phase, the adoption of new national or European legislative acts, and evolving requirements in terms of security and interoperability. These Technical Specifications pursue two main objectives and represent a core component of the implementation framework for the IT-Wallet System.

The first one is to provide a clear and structured set of recommendations, resources and design requirements related to the IT-Wallet System elements that impact on the User Experience.
The document, by distinguishing between mandatory regulatory aspects and good design practices, aims to provide to public entities and private entities interested in taking part in the IT-Wallet System what is necessary to:

- facilitate the understanding and adoption of the Service Model, increasing the number of potential services and usage opportunities for the User;
- adopt the IT-Wallet System's Visual Identity in order to enhance its reliability and recognizability for the User;
- ensure design consistency across macro-functionalities and single interactions between the User and the service Touchpoints;
- maintain an adequate level of quality, promoting the principles of usability, accessibility and inclusivity.


The second focus is to define the technical architecture and reference framework that will serve as a guideline for all the parties involved in the development of the IT-Wallet System.

Additional documentation, tools and resources - hereinafter defined Official Resources - for the design and development of the IT-Wallet System Technical Solutions will be soon available in the :ref:`official-resources:Official Resources` section and will be periodically updated.

Normative Language and Conventions
----------------------------------

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.

.. include:: how-to-read-spec.rst


