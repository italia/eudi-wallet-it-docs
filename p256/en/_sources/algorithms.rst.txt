.. include:: ../common/common_definitions.rst
  
.. _supported_algs:

Cryptographic algorithms
++++++++++++++++++++++++

The following algorithms MUST be supported:
    
.. list-table:: 
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Algorithm `alg` parameter value**
    - **Description**
    - **Operations**
    - **References**
  * - **ES256** 
    - Elliptic Curve Digital Signature Algorithm (ECDSA) using one of the enabled curves listed in the section below and SHA256.
    - Signature
    - :rfc:`7518`, `[SOG-IS] <https://www.sogis.eu/documents/cc/crypto/SOGIS-Agreed-Cryptographic-Mechanisms-1.3.pdf>`_, `[ETSI] <https://www.etsi.org/deliver/etsi_ts/119300_119399/119312/01.04.03_60/ts_119312v010403p.pdf>`_ .
  * - **ES384** 
    - Elliptic Curve Digital Signature Algorithm (ECDSA) using one of the enabled curves listed in the section below and SHA384.
    - Signature
    - :rfc:`7518`, `[SOG-IS] <https://www.sogis.eu/documents/cc/crypto/SOGIS-Agreed-Cryptographic-Mechanisms-1.3.pdf>`_, `[ETSI] <https://www.etsi.org/deliver/etsi_ts/119300_119399/119312/01.04.03_60/ts_119312v010403p.pdf>`_ .
  * - **ES512**
    - Elliptic Curve Digital Signature Algorithm (ECDSA) using one of the enabled curves listed in the section below and SHA521.
    - Signature
    - :rfc:`7518`, `[SOG-IS] <https://www.sogis.eu/documents/cc/crypto/SOGIS-Agreed-Cryptographic-Mechanisms-1.3.pdf>`_, `[ETSI] <https://www.etsi.org/deliver/etsi_ts/119300_119399/119312/01.04.03_60/ts_119312v010403p.pdf>`_ .
  * - **RSA-OAEP-256**
    - RSA Encryption Scheme with Optimal Asymmetric Encryption Padding (OAEP) using SHA256 hash function and the MGF1 with SHA-256 mask generation function.
    - Key Encryption
    - :rfc:`7516`, :rfc:`7518`.
  * - **A128CBC-HS256**
    - AES encryption in Cipher Block Chaining mode with 128-bit Initial Vector value, plus HMAC authentication using SHA-256 and truncating HMAC to 128 bits.
    - Content Encryption 
    - :rfc:`7516`, :rfc:`7518`.
  * - **A256CBC-HS512**
    - AES encryption in Cipher Block Chaining mode with 256-bit Initial Vector value, plus HMAC authentication using SHA-512 and truncating HMAC to 256 bits.
    - Content Encryption 
    - :rfc:`7516`, :rfc:`7518`.

The following Elliptic Curves MUST be supported for the Elliptic Curve Digital Signature Algorithm:

.. list-table:: 
  :widths: 20 20 20 
  :header-rows: 1

  * - **Curve Family**
    - **Short Curve Name**
    - **References**
  * - **Brainpool** 
    - brainpoolP256r1, brainpoolP384r1, brainpoolP512r1.
    - :rfc:`5639`, `[ETSI] <https://www.etsi.org/deliver/etsi_ts/119300_119399/119312/01.04.03_60/ts_119312v010403p.pdf>`_ .
  * - **NIST**
    - P-256, P-384, P-521
    - `[ETSI] <https://www.etsi.org/deliver/etsi_ts/119300_119399/119312/01.04.03_60/ts_119312v010403p.pdf>`_, `[FIPS-186-4] <https://www.nist.gov/publications/digital-signature-standard-dss-2>`_, `[ISO/IEC 14888-3] <https://www.iso.org/standard/76382.html>`_.

The following algorithms are RECOMMENDED to be supported:
    
.. list-table:: 
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Algorithm `alg` parameter value**
    - **Description**
    - **Operations**
    - **References**
  * - **PS256** 
    - RSASSA (RSA with Signature Scheme Appendix) with PSS ( Probabilistic Signature Scheme) padding using SHA256 hash function and MGF1 mask generation function with SHA-256.
    - Signature
    - :rfc:`7518`, `[SOG-IS] <https://www.sogis.eu/documents/cc/crypto/SOGIS-Agreed-Cryptographic-Mechanisms-1.3.pdf>`_.
  * - **PS384**
    - RSASSA (RSA with Signature Scheme Appendix) with PSS ( Probabilistic Signature Scheme) padding using SHA384 hash function and MGF1 mask generation function with SHA-384.
    - Signature
    - :rfc:`7518`, `[SOG-IS] <https://www.sogis.eu/documents/cc/crypto/SOGIS-Agreed-Cryptographic-Mechanisms-1.3.pdf>`_.
  * - **PS512**
    - RSASSA (RSA with Signature Scheme Appendix) with PSS ( Probabilistic Signature Scheme) padding using SHA512 hash function and MGF1 mask generation function with SHA-512.
    - Signature
    - :rfc:`7518`, `[SOG-IS] <https://www.sogis.eu/documents/cc/crypto/SOGIS-Agreed-Cryptographic-Mechanisms-1.3.pdf>`_.
  * - **ECDH-ES**
    - Elliptic Curve Diffie-Hellman  (ECDH) Ephemeral Static key agreement using Concat Key Derivation Function (KDF). 
    - Key Encryption
    - :rfc:`7518`.
  * - **ECDH-ES+A128KW**
    - ECDH-ES using Concat KDF and content encryption key (CEK) wrapped using AES with a key length of 128 (A128KW).
    - Key Encryption
    - :rfc:`7518`.
  * - **ECDH-ES+A256KW**
    - ECDH-ES using Concat KDF and content encryption key (CEK) wrapped using AES with a key length of 256 (A256KW).
    - Key Encryption
    - :rfc:`7518`.

The following algorithms MUST NOT be supported:
    
.. list-table:: 
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Algorithm `alg` parameter value**
    - **Description**
    - **Operations**
    - **References**
  * - **none** 
    - -
    - Signature
    - :rfc:`7518`.
  * - **RSA_1_5**
    - RSAES with PKCS1-v1_5 padding scheme. Use of this algorithm is generally not recommended.
    - Key Encryption
    - :rfc:`7516`, `[Security Vulnerability] <https://en.wikipedia.org/wiki/Adaptive_chosen-ciphertext_attack>`_, `[SOG-IS] <https://www.sogis.eu/documents/cc/crypto/SOGIS-Agreed-Cryptographic-Mechanisms-1.3.pdf>`_.
  * - **RSA-OAEP**
    - RSA Encryption Scheme with Optimal Asymmetric Encryption Padding (OAEP) using default parameters.
    - Key Encryption
    - :rfc:`7518`, `[SOG-IS] <https://www.sogis.eu/documents/cc/crypto/SOGIS-Agreed-Cryptographic-Mechanisms-1.3.pdf>`_.
  * - **HS256** 
    - HMAC using SHA256.
    - Signature
    - :rfc:`7518`.
  * - **HS384** 
    - HMAC using SHA384.
    - Signature
    - :rfc:`7518`.
  * - **HS512** 
    - HMAC using SHA512
    - Signature
    - :rfc:`7518`.



