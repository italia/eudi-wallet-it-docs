.. include:: ../common/common_definitions.rst
.. Included via entities.rst at title level '=' (document title).


Authentic Sources
=================

Authentic Sources provide Users attributes to the Credential Issuers enabling them in the issuance of the Digital Credentials. During the Issuance Flow, Credential Issuers request from Authentic Sources the attributes required to provide the requested Credential. Authentic Sources MAY also provide a Credential Offer related to their Credential Issuers as defined in Section :ref:`credential-issuance-low-level:Credential Offer Flow`.

Public Authentic Sources MUST interact with Credential Issuers via PDND according to the rules defined in Section :ref:`e-service-pdnd:e-Service PDND` and in Section :ref:`credential-revocation:Status Update by Authentic Sources`. See also Section :ref:`authentic-source-endpoint:e-Service PDND Authentic Source Catalog` for additional details.

Authentic Sources MUST:

  - provide User's attributes when requested by the Credential Issuer authorized to issue the related Digital Credential attesting the attributes. Public Authentic Sources MUST use PDND to send User's attributes to their Credential Issuers. When the User's attributes is not available during the Issuance Flow, Authentic Sources MUST provide Credential Issuers with an estimated time when the User's data will be available. Authentic Sources MAY require an evidence that:

    - the request for Users attributes is related to data about themselves;
    - the request for User attributes comes from a valid Wallet Instance;

  - cooperate with their Credential Issuers so that the attributes attested in a Digital Credential are always kept up to date. Public Authentic Sources MUST use PDND Signal Hub to notify their Credential Issuers of any update regarding attributes that have changed or are no longer valid.


