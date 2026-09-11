.. include:: ../common/common_definitions.rst
.. Included via test-plans.rst at title level '-' (level 1).


Federation Authority Test Matrix
--------------------------------

This section defines test cases for Federation Authorities (Trust Anchors and Intermediates) responsible for operating the Trust Infrastructure as described in :ref:`infrastructure-trust:Infrastructure of Trust`. Tests focus on correctness and conformance of:

- Entity Configuration (``.well-known/openid-federation``)
- Subordinate Statements returned by ``/fetch``
- Federation registry endpoints (``/list``, ``/fetch``, ``/trust_mark_status``, ``/historical-jwks``)

All validations  align with (`OID-FED`_).


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - **Test Case ID**
    - **Purpose**
    - **Description**
    - **Expected Result**
  * - FA_001
    - Discovery, Interoperability
    - Entity Configuration media type
    - ``GET /.well-known/openid-federation`` returns HTTP 200 with ``Content-Type: application/entity-statement+jwt``.
  * - FA_002
    - Security
    - Entity Configuration signature integrity
    - The Entity Configuration is a signed JWT; signature verifies using one of the Federation Entity public keys contained in the Entity Configuration ``jwks`` per `OID-FED`_.
  * - FA_003
    - Interoperability
    - Entity Configuration JOSE header parameters
    - JOSE header contains ``alg`` (permitted), optional ``kid`` referencing a key in ``jwks``, and ``typ`` set to ``entity-statement+jwt``.
  * - FA_004
    - Security
    - Entity Configuration standard claims
    - Payload includes ``iss`` and ``sub`` both equal to the Federation Authority identifier URL; includes ``iat`` and ``exp`` as valid Unix timestamps; ``exp`` > ``iat`` and current time < ``exp``.
  * - FA_005
    - Security, Interoperability
    - Entity Configuration common parameters
    - Payload contains ``jwks`` and ``metadata`` with ``federation_entity`` object including published Federation endpoints as per :ref:`registry:Registry Integration and Cross-References`.
  * - FA_006
    - Security
    - Entity Configuration key material validity
    - ``jwks.keys[*]`` entries use permitted algorithms and key sizes; keys are not expired or revoked per ``/historical-jwks``; each ``kid`` is unique.
  * - FA_007
    - Security
    - ``exp`` validation tolerance
    - Validation rejects Entity Configuration if ``exp`` is in the past; a maximum clock skew of 120 seconds MAY be applied when comparing current time to ``iat``/``exp``.
  * - FA_008
    - Security
    - Subordinate Statement signature and lifetime
    - ``GET /fetch?sub={entity}`` returns a signed JWT Subordinate Statement; header and payload verify per `OID-FED`_; ``iss`` equals the issuing Federation Authority; ``sub`` equals requested entity; ``iat``/``exp`` valid.
  * - FA_009
    - Interoperability
    - Subordinate Statement schema
    - Subordinate Statement contains the subordinate's public keys (directly or by reference) and applicable metadata policies or metadata, conforming to draft-43 structure.
  * - FA_010
    - Discovery
    - Listing subordinates
    - ``GET /list`` returns a JSON array or JWT-wrapped list of current subordinate identifiers; response format and media type match the published metadata; HTTP 200.
  * - FA_011
    - Security
    - Trust Mark status endpoint
    - ``GET /trust_mark_status?id={tm_id}&sub={entity}`` returns current status with HTTP 200 and an integrity-protected object (JWT if advertised). Unknown Trust Mark IDs or subjects return appropriate 4xx.
  * - FA_012
    - Security
    - Historical keys endpoint
    - ``GET /historical-jwks`` returns revoked/expired keys with revocation reasons. Structure validates as JWKS or JWT-wrapped JWKS per advertised media type.
  * - FA_013
    - Security
    - Key rotation propagation
    - After rotating keys, ``/.well-known/openid-federation`` and ``/historical-jwks`` are updated atomically or within a documented maximum propagation window. Verification with the new key succeeds, and the old key appears in historical.
  * - FA_014
    - Security
    - Disallow ``alg":"none`` and weak algorithms
    - Any Entity Configuration or Subordinate Statement with ``alg": "none"`` or a disallowed algorithm is rejected; endpoint returns appropriate error (e.g., 400/422).
  * - FA_015
    - Security
    - ``kid`` resolution and mismatch handling
    - If JOSE header ``kid`` is present, it matches a key in the current ``jwks``; on mismatch, verification fails with clear error.
  * - FA_016
    - Interoperability
    - Endpoint discovery from metadata
    - ``federation_entity`` metadata in Entity Configuration includes working URLs for ``federation_list_endpoint``, ``federation_fetch_endpoint``, ``federation_trust_mark_status_endpoint``, and ``historical-jwks`` (if published); each resolves and responds per its contract.
  * - FA_017
    - Security
    - Issuer/subject self-consistency
    - For Entity Configuration, ``iss == sub ==`` Authority URL; for Subordinate Statements, ``iss`` is Authority URL and ``sub`` is subordinate URL; any deviation is rejected.
  * - FA_018
    - Interoperability
    - Media type correctness (fetch/list/status)
    - ``/fetch``, ``/list``, ``/trust_mark_status``, and ``/historical-jwks`` return the media types declared in ``federation_entity`` metadata; JWT-wrapped resources use the correct ``Content-Type`` (e.g., ``application/entity-statement+jwt``, ``application/jwk-set+jwt``).
  * - FA_019
    - Security
    - Statement replay prevention (``jti`` optional)
    - If ``jti`` is published, repeated use within the validity window is detected and logged or rejected according to policy; otherwise, uniqueness is not required.
  * - FA_020
    - Security
    - Metadata policy application (if used)
    - When metadata policies are used in Subordinate Statements, the resulting effective metadata computed from policy + source metadata conforms to draft-43 rules; conflicts are resolved deterministically.


