.. include:: ../common/common_definitions.rst
.. Included via index.rst at title level '=' (document title).


Cryptographic Algorithms
========================
This section lists cryptographic algorithms used in the IT Wallet ecosystem. Algorithm identifiers are primarily expressed as JOSE ``alg`` values; when COSE is used, the corresponding COSE algorithms are explicitly marked (e.g., ESP256 vs ES256).

The following algorithms MUST be supported:

.. list-table::
  :class: longtable
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Algorithm `alg` parameter value**
    - **Description**
    - **Operations**
    - **References**
  * - **ES256**
    - Elliptic Curve Digital Signature Algorithm (ECDSA) using P-256 and SHA-256.
    - Signature
    - :rfc:`7518`.
  * - **ES384**
    - ECDSA using P-384 and SHA-384.
    - Signature
    - :rfc:`7518`.
  * - **ES512**
    - ECDSA using P-521 and SHA-512.
    - Signature
    - :rfc:`7518`.
  * - **ESP256** (COSE, ``-9``)
    - ECDSA using P-256 and SHA-256.
    - Signature
    - :rfc:`9864`.
  * - **ESP384** (COSE, ``-51``)
    - ECDSA using P-384 and SHA-384.
    - Signature
    - :rfc:`9864`.
  * - **ESP512** (COSE, ``-52``)
    - ECDSA using P-521 and SHA-512.
    - Signature
    - :rfc:`9864`.
  * - **RSA-OAEP-256**
    - RSA Encryption Scheme with Optimal Asymmetric Encryption Padding (OAEP) using SHA-256 hash function and the MGF1 with SHA-256 mask generation function.
    - Key Encryption
    - :rfc:`7516`, :rfc:`7518`.
  * - **ECDH-ES**
    - Elliptic Curve Diffie-Hellman (ECDH) Ephemeral-Static key agreement.
    - Key Agreement
    - :rfc:`7516`, :rfc:`7518`.
  * - **A128CBC-HS256**
    - AES encryption in Cipher Block Chaining mode with 128-bit Initial Vector value, plus HMAC authentication using SHA-256 and truncating HMAC to 128 bits.
    - Content Encryption
    - :rfc:`7516`, :rfc:`7518`.
  * - **A256CBC-HS512**
    - AES encryption in Cipher Block Chaining mode with 256-bit Initial Vector value, plus HMAC authentication using SHA-512 and truncating HMAC to 256 bits.
    - Content Encryption
    - :rfc:`7516`, :rfc:`7518`.
  * - **A128GCM**
    - AES encryption with Galois/Counter Mode and a key length of 128.
    - Content Encryption
    - :rfc:`7516`, :rfc:`7518`.
  * - **A256GCM**
    - AES encryption with Galois/Counter Mode and a key length of 256.
    - Content Encryption
    - :rfc:`7516`, :rfc:`7518`.

For Credentials issued in mdoc format, the following algorithms MUST be supported:

.. list-table::
  :class: longtable
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Algorithm**
    - **Description**
    - **Operations**
    - **References**
  * - **ECKA-DH**
    - Elliptic Curve Key Agreement Algorithm – Diffie-Hellman.
    - Key agreement
    - BSI TR-03111.
  * - **HKDF**
    - HMAC-based Key Derivation Function.
    - Session key derivation
    - :rfc:`5869`.
  * - **AES-256-GCM**
    - Advanced Encryption Standard with Galois/Counter Mode and a key length of 256.
    - Session encryption
    - NIST SP 800-38D.

The following algorithms are RECOMMENDED to be supported:

.. list-table::
  :class: longtable
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Algorithm `alg` parameter value**
    - **Description**
    - **Operations**
    - **References**
  * - **PS256**
    - RSASSA (RSA with Signature Scheme Appendix) with PSS ( Probabilistic Signature Scheme) padding using SHA-256 hash function and MGF1 mask generation function with SHA-256.
    - Signature
    - :rfc:`7518`.
  * - **PS384**
    - RSASSA with PSS padding using SHA-384 hash function and MGF1 mask generation function with SHA-384.
    - Signature
    - :rfc:`7518`.
  * - **PS512**
    - RSASSA with PSS padding using SHA-512 hash function and MGF1 mask generation function with SHA-512.
    - Signature
    - :rfc:`7518`.
  * - **ECDH-ES**
    - Elliptic Curve Diffie-Hellman (ECDH) Ephemeral Static key agreement using Concat Key Derivation Function (KDF).
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
  :class: longtable
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
    - HMAC using SHA-256.
    - Signature
    - :rfc:`7518`.
  * - **HS384**
    - HMAC using SHA-384.
    - Signature
    - :rfc:`7518`.
  * - **HS512**
    - HMAC using SHA-512.
    - Signature
    - :rfc:`7518`.


