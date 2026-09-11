.. include:: ../common/common_definitions.rst
.. Included via digital-credential-flows.rst at title level '=' (document title).


Wallet Metadata Retrieval Flow
==============================

There are Digital Credential flows that require retrieving Wallet information before interacting with the Wallet itself. For example, to enable the Wallet Solution selection option during a Credential Offer flow or a Presentation flow.
To do so, the third parties offering the Credential Offer (e.g., Authentic Source, Registry, Catalogue) and the Relying Parties consult the IT-Wallet System Register, in particular the Federation Registry, via the Trust Anchor's endpoints.

First, using the Immediate Subordinate Listing endpoint they obtain the list of all subordinates of the Trust Anchor identified by their ``entity_id``. To obtain only the Wallet Provider ``entity_id``, a query parameter ``entity_type`` set with ``wallet_solution`` MAY be used.
If the responder does not support this feature, it MUST use the HTTP status code 400 and the content type ``application/json``, with the error code ``unsupported_parameter``.

Then, given the ``entity_id``, they fetch the corresponding Entity Configuration for each Wallet Provider using the federation metadata endpoint (GET .well-known/openid-federation)
and obtain the Wallet Solution metadata (see :ref:`wallet-solution-metadata:Wallet Solution Metadata`). More details on the use of the Trust Anchor's endpoints are provided in :ref:`infrastructure-trust:Infrastructure of Trust`.

Inside the metadata, the third parties offering the Credential Offer and the Relying Parties retrieve the necessary information for the Selection Page, i.e. the logo and name in full of the Wallet Solutions.
More details on the design of the Selection Page are provided in :ref:`functionalities:User Experience Design`.


