.. include:: ../common/common_definitions.rst

.. _pseudonyms.rst:


Pseudonyms
++++++++++


What it is useful for
---------------------
Pseudonyms are useful for:
- Protecting user privacy in online platforms
- Allowing anonymous participation in discussions or transactions
- Maintaining consistent identities across multiple services without revealing personal information
- Compliance with data protection regulations that require data minimization

Example
-------
In a social media platform, a user might choose the pseudonym "SunflowerDreamer"
instead of using their real name "Jane Smith". This allows Jane
to participate in discussions while maintaining her privacy.

General Properties
------------------
- Uniqueness within a given context.
- Consistency (the same entity always uses the same pseudonym in a given context).
- Reversibility (optional, depending on the system's requirements).
- Non-linkability to the real identity (without additional information).

Requirements
------------
- IT-Wallet MUST be able to generate or assign unique pseudonyms.
- The pseudonym SHOULD NOT contain information that directly reveals the entity's real identity.
- The system SHOULD maintain a secure mapping between pseudonyms and real identities (if reversibility is required).
- The pseudonym generation process SHOULD be resistant to guessing attacks.


Implementation Considerations
-----------------------------
- IT-Wallet MUST use a pseudonym format that balances uniqueness, readability, and security.
- IT-Wallet MUST implement a secure method for generating and storing pseudonyms.
- IT-Wallet SHOULD use different pseudonyms for the same entity across different contexts to prevent cross-context linking.
- IT-Wallet SHOULD implement access controls to protect the mapping between pseudonyms and real identities.
- IT-Wallet SHOULD implements policies for pseudonym rotation or expiration.
