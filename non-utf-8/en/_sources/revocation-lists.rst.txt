.. include:: ../common/common_definitions.rst

.. _revocation-lists.rst:

revocation-lists.rst
+++++++++++++++++++++++++++

[What is it]
    
[What it is usefull for]
    
[Example]
    
General Properties
------------------
    
The revocation mechanism is designed to ensure privacy and control over the status of digital credentials. The Relying Party (RP) can check the status of the credentials but cannot continuously monitor them without control or limit. This is achieved by using sender-constrained tokens.
    
Requirements
------------

- The RP MUST provide an ephemeral key for each requested credential within the presentation request.
- The Wallet Instance MUST issue a signed status list token, signed using the private key referred to the public one included in the credential cnf.jwk.
- The status list token MUST NOT contain any information about the RP.
- The signed status list token MUST be provided to the RP with a PoP bound to the ephemeral key provided by the RP.
- The RP can only use the status list token to access the RS that hosts the status list by cryptographically proving its possession.
- The RS that provides the status list MUST NOT know the identity of the client that consumes the status list.
- The status token MUST expire in a short period (less than hours), preventing any possibility to grant the access to that anonymous client the status list for that specific credential.
- Each time in the future the RP needs to check the status of a previously obtained digital credential, it MUST ask the Holder for a presentation of that digital credential (by type).

Attributes
----------

[Table with parameters/attributes]
    
.. list-table:: 
   :widths: 20 60
   :header-rows: 1

   * - **Claim**
     - **Description**
   * - key
     - value

          
Implementation considerations
-----------------------------

The implementation of the revocation mechanism should consider the privacy of the user and the control over the status of the digital credentials. The use of sender-constrained tokens ensures that the RP cannot continuously monitor the status of the credentials without control or limit.

Libraries and code snippets
--------------------------- 

TODO


External references
-------------------

TODO
