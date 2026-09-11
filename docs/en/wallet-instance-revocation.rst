.. include:: ../common/common_definitions.rst
.. Included via wallet-instance-functionalities.rst at title level '=' (document title).


Wallet Instance Revocation
==========================

This section describes the involved entities and modalities to request a Wallet Instance revocation.

The Wallet Provider MUST ensure the security and reliability of Wallet Instances, keeping them updated and compliant with security requirements. When, for technical security reasons (e.g., relating to the compromise of cryptographic material) the security of the Wallet Instance is compromised, the Wallet Provider MUST revoke the Wallet Instance.

As shown in :numref:`fig_Wallet_Instance_Revoc_Entities`, other actors MAY trigger the Wallet Instance revocation process (:ref:`WP_007–009 <wallet-provider-backend-testcases>`):

- **Users**, connecting to the Wallet Provider's web portal from their Wallet Instance or using an external browser.
- **PID Providers and IT-Wallet ID EAA Providers** when notified by the Authentic Source of the PID/IT-Wallet ID (ANPR) of the User's death.
- **Legal Authorities or the Supervisory Body** in cases of proven illegal activities.

.. _fig_Wallet_Instance_Revoc_Entities:
.. plantuml:: plantuml/wallet-instance-revocation-entities.puml
    :width: 99%
    :alt: The figure illustrates the Entities involved in the Wallet Instance revocation process.
    :caption: `Entities involved in the Wallet Instance revocation process. <https://www.plantuml.com/plantuml/svg/fLBDZjCm4BxxAOPUw4gWlUmHeMNRI0JnKxLT8QHAaHiFhKLg5tlS4X3lpjZhR27cjfMgn1D_FpFVt7gIZiAX4y-qQRkW45xDRgvdDytC7exMeA7NGhojvrMpMbVBwjFwowAQNWcnGEUjcGQFxWLCxlanuMTbI5CFzcoqsG7j4JRci-mw9AWDIvaM9mo-iy4ewVhfENrhVEy93upFTrVfFBc2NmBuzsXbkAyp5oF6x5oA_m_Io1rwYFwUUvZhdIRPmSoXOXujEyy-_ijzTFQa5NSrK2zoOQ3EPmyZQP16mHctm98dtM9K-2t4HK06saVnjl4skEJ-pL22LIeL6d6m88cStWRYCzaqrThxW2uf7dAdiNoIdLOn07P4WGrSr9lgnuC3w_HFLCtMgZuP62gGijFe1m-hS8oDUEjwkEFRIUrTKBhbyK46KX_plFIeax7OGJs_hjSlXndDYp6c5lm_BHIO-37duSUZ5MA9NTw_SNJ5Mi0IJxQLfAtXr-yiJ94YCXJOSiSY-1kEyuuc8a5i-QacojLu7EH7I_fh3_SFYxmn2YNjitIHP-aXmskkxs9iBUbJYZbBD-_B2GJ_DtHZBhuPT8j6XKFt1m00>`_


Regardless of who triggered the revocation, the Wallet Provider MUST inform Users when their Wallet Unit is revoked, according to the following requirements (:ref:`WP_034 <wallet-instance-testcases>`):

- Out-of-band alerts (e.g., email or SMS) MUST be sent as the primary notification mechanism alongside the Wallet Unit itself.
- The alert MUST occur within 24 hours from the effective Wallet Unit revocation.
- A user-friendly explanation about the reason of the revocation MUST be provided to the User alongside with the instruction to reactive the Wallet Unit if possible.

.. .. figure:: ../../images/wallet_instance_revocation.svg
..     :figwidth: 80%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/fL9TZn8z5BwVNt5URbusSPSRhxnQ5oOHuog1tHYJJIPbMk74JZksf-1e_E-UKmiguvqafFIXpyVvk8sa0gNELl-XQstI1lP4VNmncmLrlDaXxTCsHHDQxyWukcbzD-kjSiAvZgGjRcVpvzShWHxltymw5Sa4XfgvxthlXDEBVlLgkQYRpKEzhjyzV5ZLqwkgMfaGlPkA_ZEOFF8nuRDsX3I0FpfqEw2zWIVtNbbh29QEyxhMJ9XyvvFJAWpJO_wlYGCxTymlRpVvFhc2RnNmvnpdz1wBbZ0kr1cIxxroQcSYIBx_8ooGsw4ip8FHh8FAHixnL-q--0DghkealIh0IRhS8rnOWt8QZcOBR7d0reZ3zwhwPQ0IxSMyRQ9F8QT_UO9Waw6HXpGM5570RIA-ayzTNSQOJCYENQbKu8Eog6K0d8YI13YxD_MNdmbymAz6Drkl1mbmHY3F3aqyPTYaNWg9FWnmnw-ps-kaiKLbeH1fO9FVQiGSJ2fOBaQTowdZ7wdbcTnBr-Db0wjgRMpPiei1ZOSFQtFmhIBqZdz-PYyI2L4OSSUR9EHFvdAg4a84fB1_3J5UW7Extdh2ZuECMzRroMcZQ5-iHrCRPoZq9UCx6KvBU432dFxME9qw-mC0

..     Entities involved in the Wallet Instance revocation process.

.. note::
  - The flow for the Wallet Instance Revocation triggered by the User is detailed below.
  - The endpoint used by the PID/IT-Wallet ID Provider is detailed in the Wallet Provider Catalog of e-Service PDND Catalog (see Section :ref:`wallet-provider-endpoint:e-Service PDND Wallet Provider Catalog` for technical details).
  - The flow for Authorized Entities (e.g., Supervisory Bodies) is out of scope of this specification, it will be managed by each Wallet Provider.


Wallet Instance Revocation Request
""""""""""""""""""""""""""""""""""

Users MAY request the Wallet Instance revocation (:ref:`WP_032 <wallet-instance-testcases>`) by:

- *Selecting the revocation functionality from their Wallet Instance*: this functionality may be used by Users before changing their phone.
- *Using an external user agent*: this covers cases where Users lose their device, and so their access to their Wallet Instance.

In both cases, by using the Wallet Provider portal (:ref:`WP_005–006 <wallet-provider-backend-testcases>`):

- Users MUST authenticate with at least a second-factor authentication mechanism, or have an active session that meets this requirement.
- The Wallet Provider MUST allow Users to view the state of their Wallet Instances associated with their authenticated session and ask for revocation, sending a Wallet Instance Retrieval or Revocation Request (:ref:`WP_033 <wallet-instance-testcases>`, and :ref:`WP_145 <wallet-instance-optional-testcases>`), as applicable, to the :ref:`wallet-provider-endpoint:Wallet Instance Management endpoint` of the Wallet Provider Backend.

Below is a non-normative example of a Wallet Instances Retrieval Request.

.. code-block:: http

   GET /wallet-instances HTTP/1.1
   Host: walletprovider.example.com

Upon a successful retrieval, the Wallet Provider MUST return a confirmation response, with the status of all Wallet Instances associated with the User (:ref:`WP_146 <wallet-instance-optional-testcases>`).
Below is a non-normative example of a Wallet Instances Retrieval Response.

.. code-block:: http

   HTTP/1.1 200 OK
   Content-Type: application/json
   Cache-Control: no-store

   [
     {
       "id": "f7b2a8d9",
       "status": "ACTIVE",
       "issued_at": "2024-03-12T10:00:00Z"
     },
     {
       "id": "g8b235c4",
       "status": "REVOKED",
       "issued_at": "2024-02-28T15:30:00Z"
     }
   ]

Once the User identifies the Wallet Instance to be revoked, a Wallet Instance Revocation Request can be sent to the endpoint, including the Wallet Instance ID as a path parameter (:ref:`WP_147 <wallet-instance-optional-testcases>`).
Below is a non-normative example of a Wallet Instance Revocation Request.

.. code-block:: http

    PATCH /wallet-instances/{f7b2a8d9} HTTP/1.1
    Host: wallet-provider.example.org
    Content-Type: application/json

    {
      "status": "REVOKED"
    }


Wallet Instance Revocation Response
"""""""""""""""""""""""""""""""""""

Upon a successful revocation, the Wallet Provider MUST return a confirmation response  (:ref:`WP_148 <wallet-instance-optional-testcases>`).
Below is a non-normative example of a Wallet Instance Revocation Response.


.. code-block:: http

   HTTP/1.1 204 No Content


Revocation Check Mechanisms
"""""""""""""""""""""""""""

The verification of the Wallet Instance validity MUST be performed:

- **During Digital Credential issuance** by the Credential Issuers. Only Wallet Instances in Operational or Valid state have valid Wallet Instance Attestation and Key Attestation. The verification of the validity of a Wallet Instance is indirectly performed by Credential Issuers by checking the presence of a valid Wallet Instance Attestation (i.e., not expired, not revoked checking the Wallet Instance Attestation Status List, and signed by a trusted Wallet Provider).

- **During the validity period of the Digital Credential** by the Credential Issuers every 24 hours by checking the Wallet Instance Attestation Status List of the Wallet Instance holding the PID, and the Key Attestation Status List. Indeed, if the Wallet Instance or the Key Attestation is revoked, the PID hosted within it MUST be revoked. Any other Digital Credential obtained through the presentation of the PID MUST therefore be revoked too.

- **During the Wallet Instance lifecycle** by the Wallet Instance. Each Wallet Provider may implement different methods to allow a Wallet Instance to check its status. The IT Wallet specification RECOMMENDS to use the Status List of the Wallet Instance Attestation.


.. note::
   If Credential Issuers issue credentials with a validity period of less than 24 hours, they only need to verify the validity period of the WIA and KA upon issuance as stated in `EUDI-TS 3`_.

.. note::
  In the current version of the specification, Credential Issuers are directly notified of a Wallet Instance revocation by the Wallet Provider using a PDND e-service.

.. note::
  During the Digital Credential presentation phase, a Relying Party can indirectly check the Wallet Instance revocation by checking the Digital Credential revocation. When a Wallet Instance is revoked, the Wallet Provider revokes the corresponding Wallet Instance Attestations, triggering the revocation of the Digital Credential by Credential Issuer.



