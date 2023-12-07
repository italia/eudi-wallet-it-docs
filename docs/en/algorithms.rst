.. include:: ../common/common_definitions.rst
  
.. _supported_algs:

Cryptographic algorithms
++++++++++++++++++++++++

The following algorithms MUST be supported:
    
.. list-table:: 
  :widths: 20 20 20
  :header-rows: 1

  * - **Algorithm**
    - **Operations**
    - **References**
  * - **ES256** 
    - Signature
    - :rfc:`7518`.
  * - **ES384** 
    - Signature
    - :rfc:`7518`.
  * - **ES256**
    - Signature
    - :rfc:`7518`.
  * - **RSA-OAEP**
    - Key Encryption
    - :rfc:`7518`.
  * - **RSA-OAEP-256**
    - Key Encryption
    - :rfc:`7516`.
  * - **A128CBC-HS256**
    - Content Encryption 
    - :rfc:`7516`.
  * - **A256CBC-HS512**
    - Content Encryption 
    - :rfc:`7516`.

The following algorithms are RECOMMENDED to be supported:
    
.. list-table:: 
  :widths: 20 20 20
  :header-rows: 1

  * - **Algorithm**
    - **Operations**
    - **References**
  * - **PS256** 
    - Signature
    - :rfc:`7518`.
  * - **PS512**
    - Signature
    - :rfc:`7518`.
  * - **ECDH-ES**
    - Key Encryption
    - :rfc:`7518`.
  * - **ECDH-ES+A128KW**
    - Key Encryption
    - :rfc:`7518`.
  * - **ECDH-ES+A256KW**
    - Key Encryption
    - :rfc:`7518`.

The following algorithms MUST NOT be supported:
    
.. list-table:: 
  :widths: 20 20 20
  :header-rows: 1

  * - **Algorithm**
    - **Operations**
    - **References**
  * - **none** 
    - Signature
    - :rfc:`7518`.
  * - **RSA_1_5**
    - Key Encryption
    - :rfc:`7516`.
  * - **HS256** 
    - Signature
    - :rfc:`7518`.
  * - **HS384** 
    - Signature
    - :rfc:`7518`.
  * - **HS512** 
    - Signature
    - :rfc:`7518`.



