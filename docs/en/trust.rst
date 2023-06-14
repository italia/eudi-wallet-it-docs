.. include:: ../common/common_definitions.rst

.. _trust.rst:

The Infrastructure of Trust
+++++++++++++++++++++++++++

The EUDI Wallet Architecture Reference Framework (`EIDAS-ARF`_) defines 
the Trust Model as 
*"Collection of rules that ensure the legitimacy of the components 
and the entities involved in the EUDI Wallet ecosystem."*.

In this section is defined how the Trust Model is implemented in a 
infrastructure of Trust based on
OpenID Connect Federation 1.0 `OIDC-FED`_, where its Federation API, 
is used for the distribution of metadata, raw public keys, 
metadata policies, X.509 certificates and their revocation status. 

The infrastructure of Trust allows the trust assessment mechanism 
to be applied between the parties defined in the eIDAS ARF `EIDAS-ARF`_.

.. image:: ../../images/trust-roles.svg
    :width: 100%

*The roles of the Federation infrastructure, where a Trust Anchor may 
have one or more Intermediates and Leafs.*

General Properties
------------------

OpenID Federation allows to build an infrastructure that is:

- *Secure and Tamper proof*, entities' attestations of metadata and keys 
are cryptographically signed in the chain of trust, composed by attestation
issued by multiple parties that cannot be forged or tampered by an adversary;

- *Privacy preserving*, The infrastructure is public and only exposes 
public data such as public keys and metadata of the participants for 
interoperability needs, it does not require authentication of the 
requestors therefore it does not track who is assessing trust against 
whom;

- *Guarantor of the non-repudiation of long-lived attestations*, historical 
keys endpoints and historical Trust Chains, saved for years according 
to data retention policy, allow to certify the validity of a historical 
compliance, even in case of revocation, expiration or rotation of the 
keys to be used for signature verification;

- *Dynamic and flexible*, any participant is free to modify parts of its 
metadata in total autonomy, these being published within its domain and 
verified through the Trust Chain. At the same time, an accreditation body 
or the Trust Anchor may publish a metadata policy to dynamically modify 
the metadata of all participants, as for disabling a vulnerable signature 
algorithm, and obtain certainty of propagation within a configured period 
of time, to all the participants;

- *Efficient*, JWT and JSON formats have been adopted on the web for 
years, they are cheap both in terms of storage and processing and there 
is a wide range of solutions, such as libraries and software development 
kits, which allow rapid implementation of the solution.

- *Scalable*, the Trust Model scales to more than a single organization 
by means of intermediates.

- *Simple*, it is based on REST technology and formats widely used on 
the web and have become popular over the years.


This implementation profile
---------------------------

This document uses the OIDC Federation standard in its original state, 
without any substantive changes.

This document establishes the difference between Federation Entities, to
 which all participants belong except for Wallet Instances.

The latter, as personal devices, can be certified as trusted by means of 
a verifiable attestation issued and signed by its Wallet Provider.

This is called *Wallet Instance Attestation* and documented in 
the section dedicated to the Wallet Solution.


Configuration of the Federation 
-------------------------------

The configuration of the Federation is published by the Trust Anchor 
inside its :ref:`Entity Configuration<entity_configuration_ta>`, available 
at a well known web path and corresponding to a 
**.well-known/openid-federation**.

All the entities MUST obtain the Federation configuration before the 
operational phase and they
MUST keep it up-to-date. The Federation configuration contains the 
Trust Anchor
public keys for the signature operations, the maximum number of 
Intermediates allowed between a Leaf and the Trust Anchor (**max_path length**).

Below a non-normative example of Trust Anchor Entity Configuration, where
each parameter is documented in the `OIDC-FED`_ specifications:

.. code-block:: python

    {
        "alg": "ES256",
        "kid": "FifYx03bnosD8m6gYQIfNHNP9cM_Sam9Tc5nLloIIrc",
        "typ": "entity-statement+jwt"
    }
    .
    {
        "exp": 1649375259,
        "iat": 1649373279,
        "iss": "https://registry.eidas.trust-anchor.example.eu/",
        "sub": "https://registry.eidas.trust-anchor.example.eu/",
        "jwks": {
            "keys": [
                {
                    "kty": "RSA",
                    "n": "3i5vV-_ …",
                    "e": "AQAB",
                    "kid": "FifYx03bnosD8m6gYQIfNHNP9cM_Sam9Tc5nLloIIrc",
                    "x5c": [ <X.509 CA certificate> ]
                },
                {
                    "kty": "EC",
                    "kid": "X2ZOMHNGSDc4ZlBrcXhMT3MzRmRZOG9Jd3o2QjZDam51cUhhUFRuOWd0WQ",
                    "crv": "P-256",
                    "x": "1kNR9Ar3MzMokYTY8BRvRIue85NIXrYX4XD3K4JW7vI",
                    "y": "slT14644zbYXYF-xmw7aPdlbMuw3T1URwI4nafMtKrY",
                    "x5c": [ <X.509 CA certificate> ]
                }
            ]
        },
        "metadata": {
            "federation_entity": {
                "organization_name": "example TA",
                "contacts":[
                    "tech@eidas.trust-anchor.example.eu"
                ],
                "homepage_uri": "https://registry.eidas.trust-anchor.example.eu/",
                "logo_uri":"https://registry.eidas.trust-anchor.example.eu/static/svg/logo.svg",
                "federation_fetch_endpoint": "https://registry.eidas.trust-anchor.example.eu/fetch/",
                "federation_resolve_endpoint": "https://registry.eidas.trust-anchor.example.eu/resolve/",
                "federation_list_endpoint": "https://registry.eidas.trust-anchor.example.eu/list/",
                "federation_trust_mark_status_endpoint": "https://registry.eidas.trust-anchor.example.eu/trust_mark_status/"
            }
        },
        "trust_marks_issuers": {
            "https://registry.eidas.trust-anchor.example.eu/openid_relying_party/public/": [
                "https://registry.spid.eidas.trust-anchor.example.eu/",
                "https://public.intermediary.spid.org/"
            ],
    "https://registry.eidas.trust-anchor.example.eu/openid_relying_party/private/": [
                "https://registry.spid.eidas.trust-anchor.example.eu/",
                "https://private.other.intermediary.org/"
            ]
        },
        "constraints": {
            "max_path_length": 1
        }
    }


Entity Configuration and Entity Statement
`````````````````````````````````````````

The Entity Configuration is the federation metadata that an Entity 
publishes about itself, that is verifiable with a trusted third party. 
The Entity Configuration is signed and it is verifiable with one of 
the public key contained in it and also in the Entity Statement issued 
by the Trust Anchor or its Intermediate, defined in a parameter called 
authority_hints. The Entity Configuration may also contain one or more 
Trust Marks regarding its issuer.

Trust Anchor and Intermediates publish their Entity Configuration 
containing the public keys and x509 certificates and the 
Federation Entity endpoint (/fetch) where to request the Entity Statements, 
required for the signature validation of the Leafs Entity Configurations.

The Entity Statement may also publish the metadata policies, forcing 
one or more changes to be applied to the final metadata of the Leaf. 
The final metadata of a Leaf is derived from the Trust Chain that 
composes all the Statements starting from the Entity Configuration up 
to the Trust Anchor. 

Below a non-normative example of an Entity Statement issued by an authority,
such as the Trust Anchor or its Intermediate, in relation of one of its
Subordinate:

.. code-block:: python
    {
        "alg": "RS256",
        "kid": "em3cmnZgHIYFsQ090N6B3Op7LAAqj8rghMhxGmJstqg",
        "typ": "entity-statement+jwt"
    }
    .
    {
        "exp": 1649623546,
        "iat": 1649450746,
        "iss": "https://intermediate.eidas.example.org",
        "sub": "https://rp.example.it",
        "jwks": {
            "keys": [
                {
                    "kty": "EC",
                    "kid": "2HnoFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs",
                    "crv": "P-256",
                    "x": "1kNR9Ar3MzMokYTY8BRvRIue85NIXrYX4XD3K4JW7vI",
                    "y": "slT14644zbYXYF-xmw7aPdlbMuw3T1URwI4nafMtKrY",
                    "x5c": [ <X.509 certificate> ]
                }
            ]
        },
           "metadata_policy": {
                "openid_relying_party”: {
                    "scopes": {
                        "subset_of": [
                             "eu.europa.ec.eudiw.pid.1,  eu.europa.ec.eudiw.pid.it.1"
                          ]
                    },
               "request_authentication_methods_supported": {
                "one_of": ["request_object"]
                },
               "request_authentication_signing_alg_values_supported": {
                "subset_of": ["RS256", "RS512", "ES256", "ES512", "PS256", "PS512"]
                  }
                  }
            }
    }


Trust Evaluation Mechanism
--------------------------

The Trust Anchor publishes the list of its intermediates 
(Federation Subordinate Listing endpoint) and the attestations 
of the metadata and public keys of these (Entity Statements). 

Each participant, such as Trust Anchor, Intermediate, Credential Issuer, 
Wallet Provider and Relying Party, publishes its own metadata and public 
keys (Entity Configuration endpoint) on a well known web resource.

Each of these can be verified with the Entity Statements issued by a 
superior, Trust Anchor or Intermediate.

Each published statement is verifiable over time and has an expiration 
date. The revocation of each statement is verifiable in real time and 
online (remote flows) through the federation endpoints.

The concatenation of the statements, through the connection of these 
according to the mechanism of signing and the binding of claims and 
public keys, creates the Trust Chain, this contains the Trust Marks as 
well as the protocol specific metadata, where metadata policies published 
by Trust anchor are applied.

The Trust Chains can also be verified offline, through the sole 
possession of the Trust Anchor's public keys.

.. note::
    Since the Wallet Instance is not a Federation Entity, the 
    Trust Evaluation Mechanism related to it requires the presentation 
    of the Wallet Instance Attestation, during the phases of Credential
    Issuance and presentation. The Wallet Instance Attestation conveys
    all the required information pertaining the instance, such its public
    key and any other technical or administrative information with the
    full respect of the user's privacy.


Relying Party Attestation
`````````````````````````

Relying Party Attestation
The Relying Party that is accredited by a Trust Anchor or its 
Intermediate obtains a Trust Mark to be contained in its Entity Configuration, 
where it also publishes the interoperability metadata to disclose the 
requested user attributes, the signature and encryption algorithms and 
any necessary information in accordance with one or more specific protocols.

Any requests for user attributes, such as PID or (Q)EAA, from the 
Relying Party to Wallet Instances are signed and contain the verifiable 
Trust Chain regarding the Relying Party.

The Wallet Instance verifies the Trust Chain related to the 
Relying Party and the revocation of it, using a HTTP request to the 
federation entity statement related to the Relying Party.

The Trust Chain should be contained within the signed request, in 
the form of a JWS header parameter. 

In offline flows, the verification of the Trust Chain makes it possible 
to verify the reliability of the Trust Marks and the Attestations 
contained therein.


Wallet Instance Attestation
```````````````````````````

The Wallet Provider issues a Wallet Instance Attestation, 
certifying the operational status of its Wallet Instances, 
including one or more of their public keys. 

The Wallet Instance Attestation contains the Trust Chain that attests 
the public key required to validate itself and its issuer (Wallet Provider).

The Wallet Instance in the PID issuance phase presents its own 
Wallet Instance Attestation within the signed request, containing the 
Trust Chain related to the Wallet Provider. The PID Provider issues a 
PID for each public key contained in the Wallet Instance Attestation 
for which it produces the Holder Binding within the issued PID.

Trust Chain
```````````

The Trust Chain is the sequence of the verified statements that proves 
the compliance of a participant to the eIDAS Federation. It has an 
expiration date, beyond which it should be renewed to obtain the 
updated metadata. The expiration date of the Trust Chain is determined 
by the lowest expiration date, among all the expiration dates contained 
in the statements. No Entity can force the expiration date of the 
Trust Chain higher than the one configured by the Trust Anchor.

Below an abstract representation of a Trust Chain.

.. code-block:: python
    [
        "EntityConfiguration-as-SignedJWT-selfissued-byLeaf",
        "EntityStatement-as-SignedJWT-issued-byTrustAnchor",
        "EntityConfiguration-as-SignedJWT-issued-byTrustAncor"
    ]

Below a non-normative example of a Trust Chain in its original format 
(JSON Array or JWS).

.. code-block:: python
    [
    'eyJhbGciOiJFUzI1NiIsImtpZCI6ImVEUkNOSGhWYXpWd01VRlpjMVU0UlRremMxSjRNMGRVYUU4MWVVWk5VMVUyWkdSM1lqRmZTV2h1UVEiLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk1OTA2MDIsImlhdCI6MTY0OTQxNzg2MiwiaXNzIjoiaHR0cHM6Ly9ycC5leGFtcGxlLm9yZyIsInN1YiI6Imh0dHBzOi8vcnAuZXhhbXBsZS5vcmciLCJqd2tzIjp7ImtleXMiOlt7Imt0eSI6IkVDIiwia2lkIjoiZURSQ05IaFZhelZ3TVVGWmMxVTRSVGt6YzFKNE0wZFVhRTgxZVVaTlUxVTJaR1IzWWpGZlNXaHVRUSIsImNydiI6IlAtMjU2IiwieCI6Ik1wVlVHeUhlOGhQVHh5dklZRFd2NnJpZHN5aDFDUFB2TG94ZU0wUWhaN3ciLCJ5IjoidF95ZlBRd1Z1am5oS25fNVZnT05WcW93UzJvZGZwVWxfWnNvV1UzTDRHTSJ9XX0sIm1ldGFkYXRhIjp7Im9wZW5pZF9yZWx5aW5nX3BhcnR5Ijp7ImFwcGxpY2F0aW9uX3R5cGUiOiJ3ZWIiLCJjbGllbnRfaWQiOiJodHRwczovL3JwLmV4YW1wbGUub3JnLyIsImNsaWVudF9yZWdpc3RyYXRpb25fdHlwZXMiOlsiYXV0b21hdGljIl0sImp3a3MiOnsia2V5cyI6W3sia3R5IjoiRUMiLCJraWQiOiJlRFJDTkhoVmF6VndNVUZaYzFVNFJUa3pjMUo0TTBkVWFFODFlVVpOVTFVMlpHUjNZakZmU1dodVFRIiwiY3J2IjoiUC0yNTYiLCJ4IjoiTXBWVUd5SGU4aFBUeHl2SVlEV3Y2cmlkc3loMUNQUHZMb3hlTTBRaFo3dyIsInkiOiJ0X3lmUFF3VnVqbmhLbl81VmdPTlZxb3dTMm9kZnBVbF9ac29XVTNMNEdNIn1dfSwiY2xpZW50X25hbWUiOiJOYW1lIG9mIGFuIGV4YW1wbGUgb3JnYW5pemF0aW9uIiwiY29udGFjdHMiOlsib3BzQHJwLmV4YW1wbGUuaXQiXSwiZ3JhbnRfdHlwZXMiOlsicmVmcmVzaF90b2tlbiIsImF1dGhvcml6YXRpb25fY29kZSJdLCJyZWRpcmVjdF91cmlzIjpbImh0dHBzOi8vcnAuZXhhbXBsZS5vcmcvb2lkYy9ycC9jYWxsYmFjay8iXSwicmVzcG9uc2VfdHlwZXMiOlsiY29kZSJdLCJzY29wZXMiOiJldS5ldXJvcGEuZWMuZXVkaXcucGlkLjEgZXUuZXVyb3BhLmVjLmV1ZGl3LnBpZC5pdC4xIGVtYWlsIiwic3ViamVjdF90eXBlIjoicGFpcndpc2UifSwiZmVkZXJhdGlvbl9lbnRpdHkiOnsiZmVkZXJhdGlvbl9yZXNvbHZlX2VuZHBvaW50IjoiaHR0cHM6Ly9ycC5leGFtcGxlLm9yZy9yZXNvbHZlLyIsIm9yZ2FuaXphdGlvbl9uYW1lIjoiRXhhbXBsZSBSUCIsImhvbWVwYWdlX3VyaSI6Imh0dHBzOi8vcnAuZXhhbXBsZS5pdCIsInBvbGljeV91cmkiOiJodHRwczovL3JwLmV4YW1wbGUuaXQvcG9saWN5IiwibG9nb191cmkiOiJodHRwczovL3JwLmV4YW1wbGUuaXQvc3RhdGljL2xvZ28uc3ZnIiwiY29udGFjdHMiOlsidGVjaEBleGFtcGxlLml0Il19fSwidHJ1c3RfbWFya3MiOlt7ImlkIjoiaHR0cHM6Ly9yZWdpc3RyeS5laWRhcy50cnVzdC1hbmNob3IuZXhhbXBsZS5ldS9vcGVuaWRfcmVseWluZ19wYXJ0eS9wdWJsaWMvIiwidHJ1c3RfbWFyayI6ImV5SmggXHUyMDI2In1dLCJhdXRob3JpdHlfaGludHMiOlsiaHR0cHM6Ly9pbnRlcm1lZGlhdGUuZWlkYXMuZXhhbXBsZS5vcmciXX0.dIRBRyfEsmi_6oGrJAHaYUPCtXSvBZBMdokVZtjyYgzMKEP6eSLixa8nUU9BWBWP_ELNgdKbPquSbWIGx66D5w',
     'eyJhbGciOiJFUzI1NiIsImtpZCI6IlFWUnVXSE5FWTJzMFdHNW5hSHB3VjJKVGRtd3hiRUpVY2pCdk9FeHNWMFExT0dnMFZWQnhhbTUyT0EiLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk2MjM1NDYsImlhdCI6MTY0OTQ1MDc0NiwiaXNzIjoiaHR0cHM6Ly9pbnRlcm1lZGlhdGUuZWlkYXMuZXhhbXBsZS5vcmciLCJzdWIiOiJodHRwczovL3JwLmV4YW1wbGUub3JnIiwiandrcyI6eyJrZXlzIjpbeyJrdHkiOiJFQyIsImtpZCI6ImVEUkNOSGhWYXpWd01VRlpjMVU0UlRremMxSjRNMGRVYUU4MWVVWk5VMVUyWkdSM1lqRmZTV2h1UVEiLCJjcnYiOiJQLTI1NiIsIngiOiJNcFZVR3lIZThoUFR4eXZJWURXdjZyaWRzeWgxQ1BQdkxveGVNMFFoWjd3IiwieSI6InRfeWZQUXdWdWpuaEtuXzVWZ09OVnFvd1Myb2RmcFVsX1pzb1dVM0w0R00ifV19LCJtZXRhZGF0YV9wb2xpY3kiOnsib3BlbmlkX3JlbHlpbmdfcGFydHkiOnsic2NvcGVzIjp7InN1YnNldF9vZiI6WyJldS5ldXJvcGEuZWMuZXVkaXcucGlkLjEsICBldS5ldXJvcGEuZWMuZXVkaXcucGlkLml0LjEiXX0sInJlcXVlc3RfYXV0aGVudGljYXRpb25fbWV0aG9kc19zdXBwb3J0ZWQiOnsib25lX29mIjpbInJlcXVlc3Rfb2JqZWN0Il19LCJyZXF1ZXN0X2F1dGhlbnRpY2F0aW9uX3NpZ25pbmdfYWxnX3ZhbHVlc19zdXBwb3J0ZWQiOnsic3Vic2V0X29mIjpbIlJTMjU2IiwiUlM1MTIiLCJFUzI1NiIsIkVTNTEyIiwiUFMyNTYiLCJQUzUxMiJdfX19LCJ0cnVzdF9tYXJrcyI6W3siaWQiOiJodHRwczovL3RydXN0LWFuY2hvci5leGFtcGxlLmV1L29wZW5pZF9yZWx5aW5nX3BhcnR5L3B1YmxpYy8iLCJ0cnVzdF9tYXJrIjoiZXlKaGIgXHUyMDI2In1dfQ.rIgdHa7CoaP3SO3ZNsjDWt7-8Tea41An3YBw-qaWFNdQMUzcTqRwcD4vtX6TZEEoRO3KEu8bJeaKlikHRHzoBg',
     'eyJhbGciOiJFUzI1NiIsImtpZCI6ImVVRldSakJKYlhVeU5TMHRhV1JrYlhCMWVURlBjazV6UzBGRVFTMWFNVFpEYTNOWk1WUktURTR5Y3ciLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk2MjM1NDYsImlhdCI6MTY0OTQ1MDc0NiwiaXNzIjoiaHR0cHM6Ly90cnVzdC1hbmNob3IuZXhhbXBsZS5ldSIsInN1YiI6Imh0dHBzOi8vaW50ZXJtZWRpYXRlLmVpZGFzLmV4YW1wbGUub3JnIiwiandrcyI6eyJrZXlzIjpbeyJrdHkiOiJFQyIsImtpZCI6IlFWUnVXSE5FWTJzMFdHNW5hSHB3VjJKVGRtd3hiRUpVY2pCdk9FeHNWMFExT0dnMFZWQnhhbTUyT0EiLCJjcnYiOiJQLTI1NiIsIngiOiJCR1VOOXN6ZG0xT1RxVWhUQ3JkcWRmQjhtTUJqb2JCYk5Nd2JxZnd4c3pZIiwieSI6IkdnMUhCNGVJRWJhQjA4NEJiUW5QX0lseFJZYTNhVVRHSTF0aW5qTmVSdmMifV19LCJ0cnVzdF9tYXJrcyI6W3siaWQiOiJodHRwczovL3RydXN0LWFuY2hvci5leGFtcGxlLmV1L2ZlZGVyYXRpb25fZW50aXR5L3RoYXQtcHJvZmlsZSIsInRydXN0X21hcmsiOiJleUpoYiBcdTIwMjYifV19.KR2oBDMfqLGCZ2ZqN0FgOP7cWsW4ClxBaj4-j_c3HC-YEecK6SLlNk00bGqoEe2NCMy2lqk9dYQO1IauB_ZG7A'
    ]

.. note:
    The entire Trust Chain is verifiable having only the 
    Trust Anchor’s public key.


Offline Trust Attestation Mechanisms
------------------------------------

In this section are described the implementation requirements to enable
offline trust evaluation mechanisms.

.. note::
  The offline flows doesn't allow a realtime evaluation of the status of
  an Entity, such as its revocation. At the same time, using short-lived 
  Trust Chains allows obtaining attestation of trust compatible with the 
  required revocation administative protocols (eg: a revocation must be 
  propagated in less than 24 hours, then the Trust Chain must not be 
  valid for more than that period).

Offline EUDI Wallet Trust Attestation
`````````````````````````````````````

Considering that a mobile device should not publish its metadata online, 
at the *.well-known/openid-federation* endpoint, or differently, that 
is not required that the EUDI Wallet has to publish its metadata if its 
User doesn’t want this, it’s not required that the EUDI Wallet 
publishes its federation metadata online. 

EUDI Wallet is anyway able to get a Wallet Attestation Instance 
issued by its Wallet Provider, and the Wallet Attestation Instance 
should contain a Trust Chain related to its issuer (Wallet Provider).

Offline Relying Party Metadata
``````````````````````````````

Considering that the Federation Entity Discovery is applicable only 
in online scenarios, is possible to include the Trust Chain 
in the presentation requests that a Relying Party may issue 
for an EUDI Wallet. 

The Relying Party should sign the presentation request, 
containing in its header parameter the trust_chain claim, containing 
the Federation Trust Chain related to itself.

The Wallet Instance that verifies the request issued by the 
Relying Party, is then able to use the Trust Anchor public keys to 
verify the entire Trust Chain related to the Relying Party and attests 
the reliability of this.

The Wallet Instance, by applying the metadata policy if available, 
filters out from the Relying Party’s request all the user attributes 
not attested in the trusted metadata, obtained from the Trust Chain.

Privacy considerations
----------------------

- The EUDI Wallet Instances don’t publish their metadata in an online service;
- The Federation endpoints are public and not protected by a client 
authentication, the Relying Party that looks for the Entity Statement 
of a Wallet is anonymous;
- The infrastructure of trust should be public, and all its endpoints 
publicly accessible, without any client credentials that may disclose 
who are requesting access;
- When a Wallet asks the Entity Statements to build the Trust Chain for 
a specific Relying Party, or validates online a Trust Mark, issued to a 
specific Relying Party, the Trust Anchor or its Intermediate doesn’t know 
that a specific Wallet is asking for a specific Relying Party, but only 
serve the statements related to that Relying Party, as a public resource.
- The metadata of the EUDI Wallet instance must not contain any 
information that may disclose technical information about the hardware used.
- Leaf entity, Intermediate and Trust Anchor metadata may contain the 
necessary amount data, as part of administrative, technical and security 
contact information. As a general rule it is not recommended to use personal 
contact details in such cases. From a legal perspective the publication of 
such information is needed in operational support of technical and security 
matters and hence in line with GDPR.

Considerations about Decentralization
-------------------------------------

- There should be more than a single Trust Anchor.
- There may be some cases where a trust verifier trusts an Intermediate, 
considering that an Intermediate may represent itself as a Trust Anchor 
in a specific perimeter, such cases where the Leafs are both in the 
same perimeter like a Member State giurisdiction.
- The Wallet Instance doesn’t have to publish its Entity Configuration 
(.well-known/openid-federation) since its attestation of reliability is 
contained in the Wallet Instance Attestation, issued by its Wallet Provider. 
The Wallet Provider must publish its Entity Configuration.
- The trust attestations (Trust Chain) should be contained in the JWS 
issued by Credential Issuers, as well the Presentation Requests of the 
RPs should contain the Trust Chain related to them 
(issuers of the presentation requests) and the presentation must be signed. 
The Wallet Instance by saving the signed presentation requests and the 
obtained credentials, having the Trust Chain contained in these, it has 
for each signed artifact the snapshot of the federation configuration 
(Trust Anchor Entity Configuration in the Trust Chain) and the verifiable 
reliability of the RP it has interacted with. These informations must 
be stored in the Wallet Device and backuped in a remote and secure cloud 
storage under the sole explicit will of its User (owner).
- Each signed attestation is long-lived, since it can be cryptographically 
validated even when the federation configuration changes or the keys of 
its issuers will be renewed.
- Each participant should be able to update its Entity Configuration 
without notifying the changes to any third party. The Metadata Policy of a 
Trust Chain must be applied to overload whatever related to protocol 
metadata and allowed grants of the participants.

