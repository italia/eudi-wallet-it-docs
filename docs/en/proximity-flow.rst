.. include:: ../common/common_definitions.rst
.. Included via credential-presentation.rst at title level '=' (document title).


Proximity Flow
==============

This section describes how a Relying Party Instance requests the presentation of an *mdoc-CBOR* Credential to a Wallet Instance as specified in the *ISO 18013-5 Specification*.

The high-level presentation phase is structured into three broad sub-phases as depicted in the following figure:

.. plantuml:: plantuml/credential-presentation-high-level-flow.puml
    :width: 90%
    :alt: The figure illustrates the High-Level Presentation Flow in proximity.
    :caption: `High-Level Presentation Flow in proximity. <https://www.plantuml.com/plantuml/svg/VLBHYjim47pNLsppv8CcHzjxBELeOaYXK9DSANqoEccmHMN9bUHSJUc_T-qanWr9zIAyEpCxE_9ZJ3Aahh6qDLMz_8m3B1K14Ix9PBoZefOHufLnodOQz7xzSBz-ADU-QRrZq0SXjfysURb_odVvbwVlHPxT2P5Cig35VpKNGXG8qRkiYmYlQV6LhmNVZVQAQcyrVxAM-EWxfsNeitQcKRQ31gEl2D_HRq5y9fEPni4eb72LhD1mXOblLhGPovHFvM7y7geBe5Zxa9P1kWgal7DGuuHdf1V0qJTfBH99fsa7snjNKS59zeD2pg4-MnDhH3BE92CjnQEggYLBMTwB-5ouZ8XnM0rd_idfsnNjZotAvwrnbbEXRnFqtEIBIJKl80ENJwBq0_rnknIfQyz-CD5FkElEb6-QpXarfimgxrRSd9LeUSvoXnGC3jB-Qsvyqu2V7MAw3uYi6q7ufUenu8EHbmanVSlfMiIPIIsJd5XizOyGd7wvEVr2rvxv-009aU43TfTTGTrAtaBgICbFt1l0otpWk3kEV8JJNMF_0W00>`_

The sub-phases are described below:

  1. **Device Engagement**: This subphase begins when the User is prompted to disclose specific attributes from the mdoc(s). The objective of this subphase is to establish a secure communication channel between the Wallet Instance and the Relying Party Instance, so that the mdoc requests and responses can be exchanged during the communication subphase.
  The messages exchanged in this subphase are transmitted through short-range technologies to limit the possibility of interception and eavesdropping. Device Engagement data may be transferred using either QR code or NFC technologies.

  2. **Session Establishment**: During the session establishment phase, the Relying Party Instance sets up a secure connection. All data transmitted over this connection is encrypted using a session key, which is known to both the Wallet Instance and the Relying Party Instance at this stage.
  The established session MAY be later terminated based on the conditions as detailed in [`ISO18013-5`_ #12.2.4].

  3. **Communication - Device Retrieval**: The Relying Party Instance encrypts the mdoc request with the appropriate session key and sends it to the Wallet Instance together with its public key in a session establishment message. The Wallet Instance uses the data from the session establishment message to derive the session key and then to decrypt the mdoc request.
  During the communication subphase, the Relying Party Instance has the option to request information from the Wallet Instance using mdoc requests and responses. The primary mode of communication is the secure channel established during the session setup. The Wallet Instance encrypts the mdoc response using the session key and transmits it to the mobile Relying Party Instance via a session data message.


Relying Party and Wallet Instances registered in the IT-Wallet ecosystem MUST support at least the following flows:


- *Supervised Device Retrieval flow* where a human Relying Party is overseeing the verification process in person, or *unsupervised flow* where verification might happen through automated systems without human oversight (:ref:`WP_095 <wallet-credential-presentation-testcases>`).
- *Relying Party Instance Authentication* following the mechanisms defined in the `ISO18013-5`_ for the *reader authentication* (:ref:`WP_098 <wallet-credential-presentation-testcases>`).
- Domestic *Document Type* and *Namespaces* defined in this technical specification in addition to those already defined in the `ISO18013-5`_ for the mDL (see :ref:`credential-data-model:mdoc-CBOR Credential Format` for more details) (:ref:`WP_099 <wallet-credential-presentation-testcases>`).

The following table shows the supported Device Engagement technologies (:ref:`WP_097 <wallet-credential-presentation-testcases>`), specifying which are mandatory.

.. list-table::
   :class: longtable
   :widths: 20 15 15 25 25
   :header-rows: 2

   * - **Transmission technology**
     - **ISO 18013-5**
     - **ISO 18013-5**
     - **IT Wallet**
     - **IT Wallet**
   * -
     - **Wallet Instance**
     - **RP Instance**
     - **Wallet Instance**
     - **RP Instance**
   * - **QR code**
     - C\ :sup:`a`
     - M
     - MUST
     - C – MUST if the device is equipped with a camera or QR code reader and BLE.
   * - **NFC**
     - C\ :sup:`a`
     - M
     - RECOMMENDED
     - C – MUST if the device is equipped with an NFC reader.

Key: C = Conditional | M = Mandatory | :sup:`a`\ Support for at least one of these methods is mandatory (:ref:`WP_097a <wallet-credential-presentation-testcases>`)

The following table shows the supported Device Retrieval technologies, specifying which are mandatory.

.. list-table::
   :header-rows: 2
   :widths: 20 15 15 25 25
   :class: longtable

   * - **Transmission technology**
     - **ISO 18013-5**
     - **ISO 18013-5**
     - **IT Wallet**
     - **IT Wallet**
   * -
     - **Wallet Instance**
     - **RP Instance**
     - **Wallet Instance**
     - **RP Instance**
   * - **BLE**
     - C\ :sup:`a`
     - M
     - MUST
     - C – MUST if the device is equipped with a camera or QR code reader and BLE.
   * - **NFC**
     - C\ :sup:`a`
     - M
     - RECOMMENDED
     - C – MUST if the device is equipped with an NFC reader.

Key: C = Conditional | M = Mandatory | :sup:`a`\ Support for at least one of these methods is mandatory (:ref:`WP_096b <wallet-credential-presentation-testcases>`)

.. note::
   From the second edition, version 3, `ISO18013-5`_ does not define or support Server Retrieval as a transport option. Only proximity retrieval methods (NFC, BLE, and optionally Wi-Fi Aware) are specified (:ref:`WP_096 <wallet-credential-presentation-testcases>`). Therefore, Server Retrieval is not considered in this flow (:ref:`WP_096a <wallet-credential-presentation-testcases>` and :ref:`PPR-023 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`).


The following figure illustrates the low-level flow compliant with ISO 18013-5 for proximity flow.

.. _fig_High-Level-Flow-ITWallet-Presentation-ISO-updated:
.. plantuml:: plantuml/credential-presentation-flow.puml
    :width: 99%
    :alt: The figure illustrates the Low-Level Presentation Flow in proximity.
    :caption: `Low-Level Presentation Flow in proximity. <https://www.plantuml.com/plantuml/svg/ZLJBRjim4BppAnRgfGQS5kYn28muZki6JTFKJf1BBXIrjeb8IvKFAVxxBacvTLe7oKtIScTsPeSwSrvQ7vfQoE0DXQP4AuHKtbYuSsX1EWX2j7n8AzrAyb3Soxf63tUaVH7h_VFoyWOkYM59OIftGeIJIVyPVhH8uBS80y3-LAJJdVJ8IE4q7StKWGyJ0qkl3K6vEzOCF2XN9DolPjCzKsftMAFoBZMrrZpfHliTFw5Zq0ov3gJYWwov94phuRkaIhBu7UWrh3osy0cq0p8UMhHhOnki8bzYwtdOyEAmwGXI9KIVXbeWeOqg2Nl0TeiDlzRmY3oKr1OUw7rHp2-mqmg_uUx3ZTLTKOpX-STG5iL82CiJiVQEcVjn1--kBXTVRnVB-VnQd9QJwUZqOpdXpjmufutSC1tveW2M9m6Vr5RIPa3ukGHbgcJbzPTPd3d1Yx-BuHrs9vFkhIAMA2kq_uWu-9X5PCIPQTh0W0wTYyunr9xinY8d2tcvJc-8ZUVb09AokzR7D--jBcFl0rdy5T1vOFPL1ffpFifQkstM_QfdvtlFZlT3mv_PnJ_MLHdf_6e--COALE1fOvcmFh1n2C0nfRboWKdJo-HHEBFfDUUI8ntja9x98dJAu7BGBrkEUiSRuQZkiwvfCro6GzFSc6rJXZoVS63MO76ZdRSvlmhvHgzZcd6uKzC1-JKVPzd75Sj_QN4yLcl8uS6sBZYLl2GGlVPR6BRvRDnCADzaU8xFVwvcal5H9sDogtHReDHKiMUZDBNQedg4fZ8AMBokueyYNNmc663X5csZAHadAZouD0SllJZZ-VX7-ni0>`_


**Step 1**: The User opens the Wallet Instance initiating the process.

**Step 2**: The User authenticates itself to the Wallet Instance. This can be done by the Wallet Instance or a Wallet Secure Cryptographic Application (WSCA). It is a prerequisite for accessing sensitive data and presenting attributes  (:ref:`WP_100 <wallet-credential-presentation-testcases>`).

**Step 3**: The User selects the proximity presentation functionality.

**Step 4**: [Optional] If the initial authentication in Step 2 was not done through WSCA, a separate authentication via WSCA MAY be required  (:ref:`WP_100 <wallet-credential-presentation-testcases>`).

**Step 5**: The Wallet Instance generates a new ephemeral Elliptic Curve key pair for secure communication (:ref:`WP_101 <wallet-credential-presentation-testcases>`). The public key (``EDeviceKey.Pub``) will be exchanged with the Relying Party Instance to derive a shared session key, which is then used for session encryption. This is part of the device engagement process.

.. admonition:: Box A

   The Wallet Instance and Relying Party Instance exchange *Device Engagement* data via QR code or via NFC Connection Handover (:ref:`WP_097 <wallet-credential-presentation-testcases>`).

   Refer to:

   - Sec 8.2.2.1 for ``DeviceEngagement`` over QR code
   - Sec 8.2.2.2 for ``DeviceEngagement`` over NFC

**Step 6**: The Relying Party Instance generates its ephemeral key pair (``EReaderKey.Priv``, ``EReaderKey.Pub``). The private key (``EReaderKey.Priv``) MUST be kept secret, and the public key (``EReaderKey.Pub``) MUST be used in establishing the session.

**Step 7**: The Wallet Instance and Relying Party Instance independently MUST derive the session keys using their private ephemeral key and the other party's public ephemeral key through a key agreement protocol. This ensures session encryption. In this particular step, the Relying Party Instance MUST compute its session key  (:ref:`PPR-002 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>` and :ref:`WP_104 <wallet-credential-presentation-testcases>`).

**Step 8**: The Relying Party Instance MUST prepare a ``SessionEstablishment`` message. This message MUST be signed by the Relying Party Instance (mdoc reader authentication as specified in [`ISO18013-5`_ #12.5]) and encrypted using the session keys derived in the previous step. The ``SessionEstablishment`` message MUST include the ``EReaderKey.Pub`` and a request for specific attribute(s) (:ref:`PPR-002 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`).


Below is a non-normative example using the diagnostic notation of a CBOR-encoded ``SessionEstablishment`` message that contains an mdoc request for an mDL Digital Credential.

.. literalinclude:: ../../examples/iso-session-establishment.txt
  :language: text

.. admonition:: Box B

   The Relying Party Instance MUST transmit the encrypted and signed ``SessionEstablishment`` message to the Wallet Instance over an NFC or a BLE secure connection that was established based on the Device Engagement information.
   Refer to:

   - Sec 8.2.2.3 for ``SessionEstablishment`` over BLE, and
   - Sec 8.2.2.5 for ``SessionEstablishment`` over NFC

**Step 9**: The Wallet Instance MUST compute the session key, as described in Step 7.

**Step 10**: Upon receiving the ``SessionEstablishment`` message, the Wallet Instance MUST decrypt it using the shared session key and MUST verify the Relying Party Instance's signature (mdoc reader authentication as specified in [`ISO18013-5`_ #12.5]) to ensure its authenticity (:ref:`PPR-002 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>` and :ref:`WP_105–106 <wallet-credential-presentation-testcases>`).

**Step 11**: The Wallet Instance MUST decrypt the attribute request and MUST prompt the User for their consent to release the requested attributes (:ref:`WP_107 <wallet-credential-presentation-testcases>`). It MUST also display the contents of the Relying Party's Registration Certificate to ensure transparency about the requested attributes and its registered purpose (:ref:`WP_107a <wallet-credential-presentation-testcases>`).

**Step 12**: The User reviews the request and the Relying Party's registration information and then approves the presentation of the requested attributes.


.. admonition:: Box C

   After receiving User approval, the Wallet Instance MUST retrieve the requested mdoc Digital Credentials (:ref:`PPR-006 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>` and :ref:`WP_108 <wallet-credential-presentation-testcases>`). It then MUST prepare a ``SessionData`` message containing these Digital Credentials, and it MUST sign the required authentication data (as part of the mdoc authentication process, as specified in [`ISO18013-5`_ #12.4]) as per (:ref:`WP_109–110 <wallet-credential-presentation-testcases>`). It MUST encrypt it using the established session keys before transmitting it to the Relying Party Instance over the secure channel (:ref:`WP_111 <wallet-credential-presentation-testcases>`). The signing ensures device binding and data integrity. The mdoc response MUST be encoded in CBOR, with its structure outlined in [`ISO18013-5`_ #10.3] (:ref:`PPR-029 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`, :ref:`PPR-030 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`, and :ref:`WP_112 <wallet-credential-presentation-testcases>`).
   Refer to (:ref:`WP_112a–112b <wallet-credential-presentation-testcases>`):

   - Sec 8.2.2.4 for ``SessionData`` over BLE, and
   - Sec 8.2.2.5 for ``SessionData`` over NFC

Below is a non-normative example using the diagnostic notation of a CBOR-encoded ``SessionData`` that contains the mdoc response of an mDL Digital Credential.

.. literalinclude:: ../../examples/iso-session-data.txt
  :language: text

**Step 13**: The Relying Party Instance receives the ``SessionData``, then it MUST decrypt it, and it MUST verify the Wallet Instance's signature to ensure the data's integrity and that it originates from the expected device (device binding). It also MUST check the validity of the mdoc, including its Issuer's signature. In case of long-lived Digital Credentials, it SHOULD also check the revocation status using the `TOKEN-STATUS-LIST`_.

**Step 14**: Once the data exchange is complete, either party can terminate the session. The session can be terminated by sending the status code for session termination in a ``SessionData`` message; this can be sent together with an mdoc request or response [`ISO18013-5`_ #12.2.4] (:ref:`WP_113c <wallet-credential-presentation-testcases>`). If BLE is used, this can involve sending a status code for session termination or the “End” command. In this scenario, the GATT Client (Relying Party Instance) MUST unsubscribe from characteristics and disconnect from the GATT server (Wallet Instance) (:ref:`PPR-007 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`, :ref:`WP_113b <wallet-credential-presentation-testcases>`, and :ref:`WP_114 <wallet-credential-presentation-testcases>`).

**Final Consideration**: The presentation flow focused on the technical data exchange in proximity settings. It is crucial to recognise that supervised proximity flows involving a human verifier play a vital role in many use cases (e.g., age verification at a store, identity check by law enforcement). The human element adds a layer of identity verification through visual inspection and comparison, contributing to User Binding and overall authentication assurance aspects not fully captured in a purely technical presentation flow.

.. note::
    During each credential presentation transaction executed through the proximity flow, the Wallet Instance MUST create and maintain a corresponding transaction record in the transaction log (see :ref:`wallet-instance-dashboard:Wallet Instance Dashboard and Transaction Logging`).

    The transaction record MUST be created once the Wallet Instance has successfully established the session and accepted the reader for processing (i.e., after decrypting the ``SessionEstablishment`` message and verifying reader authentication, Step 10). At this point, the record MUST include the transaction metadata and the request context available at that stage (e.g., requested attestation type(s) such as ``docType``, and the identifier(s) of the requested attributes), without logging any attribute values.

    The record MUST be updated as the transaction progresses to reflect the evolving transaction state and result context (e.g., what was actually presented after User consent and response preparation/sending, Steps 11–12), without logging any attribute values.

    The record MUST be finalized when the transaction ends, indicating the outcome (e.g., completed, failed, or session terminated; Steps 13–14 and Session Termination).

``DeviceEngagement`` over QR Code
----------------------------------
The following figure illustrates the low-level flow compliant with ISO 18013-5 for ``DeviceEngagement`` over QR Code corresponding to Box A in Figure :ref:`fig_High-Level-Flow-ITWallet-Presentation-ISO-updated`.

.. _fig_DeviceEngagement-QR:
.. plantuml:: plantuml/device-engagement-over-qr-code.puml
    :width: 90%
    :alt: The figure illustrates the Device Engagement over QR Code Presentation Flow in proximity.
    :caption: `Device Engagement over QR Code. <https://www.plantuml.com/plantuml/svg/PP0n3i8m34NtdCBAtWimL4Z0m0P5YDaaLcifTQlMIQvFbAK5F5Zoz__Fae-hug9n30QZJXB7Doq6IjKsbnqxdb4Kx0j388Mdi5h05VA_fRl1LGfH75LBCXiBdN92fPghIcxQT837C6NGWU3UmMdo12mkHC_IWxLdIkpe8ZtsD9AejT-iLCVKD6qk98Uo9sstFVqaTa8sHn9VFl01>`_

**Step 1**: The Wallet Instance presents a QR Code to the Relying Party Instance. The QR code MUST contain a URI with “mdoc:” as scheme and the ``DeviceEngagement`` structure specified in Section 9.1 encoded using base64url-without-padding, according to `RFC 4648`_, as path  (:ref:`WP_102a <wallet-credential-presentation-testcases>`).

Non-Normative Example with BLE as Data Retrieval
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Below is a non-normative example using the diagnostic notation of a CBOR-encoded ``DeviceEngagement`` that utilizes QR for Device Engagement and Bluetooth Low Energy (BLE) for data retrieval.

 .. literalinclude:: ../../examples/iso-device-engagement-BLE.txt
  :language: text

Non-Normative Example with NFC as Data Retrieval
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Below is a non-normative example using the diagnostic notation of a CBOR-encoded ``DeviceEngagement`` that utilizes QR for Device Engagement and NFC for data retrieval.

 .. literalinclude:: ../../examples/iso-device-engagement-NFC.txt
  :language: text

**Step 2**: The Relying Party uses its Relying Party Instance to scan the QR code and retrieve the ``DeviceEngagement`` data from the mdoc. It MUST select one of the transmission technologies from the ones provided in the ``DeviceEngagement`` structure.

``DeviceEngagement`` over NFC
------------------------------
The following figure illustrates the low-level flow compliant with ISO 18013-5 for ``DeviceEngagement`` over NFC corresponding to Box A in Figure :ref:`fig_High-Level-Flow-ITWallet-Presentation-ISO-updated` (:ref:`WP_103 <wallet-credential-presentation-testcases>`).

.. _fig_DeviceEngagement-NFC:
.. plantuml:: plantuml/device-engagement-over-nfc.puml
    :width: 90%
    :alt: The figure illustrates the Device Engagement over NFC Presentation Flow in proximity.
    :caption: `Device Engagement over NFC. <https://www.plantuml.com/plantuml/img/dLDDJ-Cm4BtFhtZoXUOGJfooAaA28hWKr7QrPpSUWYNNpjfEilpxdPIIRRLKIEGG9NdpFkObkKbPnzpj7Eak1z_jjXo9g9M7jhQjzXdgbtQECtvwcnLqmd0Ahvxnw4N6rxo7Uo9TPzlhp38wNVPqWR8iiRo_XU7UrWpsZMvunw8o4m6HH8Zmt8HiXMAAaK3Ry0VgKvOYGBkCzJltLNiJUiaFEVgol1ugh5WRF1m0hDbnBMQRjvPnXOrk2XbcbnZBoVLKPn2Tlf8DhQ0Eoxl5FRGHDDl4QPf5uhXFDrDTz9L_gQlagmzK5OTCOwGfpOf_Tvp6tRks3N6qhdMCbcCg3jwZzN_fbRhRDx7uLuI2qLaND6xZ3O7a32bENkN5V0wbrfoI3NuXDM-TJQyVh2vQtnmlFxdDGfk5eLs1-Pn8xhuZ8_vuykuDzWN3-tSqjMTmM1pMuxEbVc2pN3nFrTg4JbYNrAEyXZJvrB8_7JcNSAAinsA-dBfr8PqNEx6aiMeYmqSV-j7DG3U2o__r5m00>`_

``DeviceEngagement`` over NFC is based on the NFC Forum Connection Handover Technical Specification, Version 1.5. Only Reader/ Writer mode using a Type 4 Tag is supported. The Connection Handover protocol is always initiated by the Relying Party Instance, which makes the role of Handover Requester. The Wallet Instance MUST use either Static Handover or Negotiated Handover:
- **Static Handover**: The Relying Party Instance retrieves a Handover Select message directly from the Wallet Instance's Type 4 Tag. This message contains at least one Alternative Carrier Record, each indicating a retrieval method supported by the Wallet Instance (:ref:`WP_103a <wallet-credential-presentation-testcases>`). The Relying Party Instance MUST select one of these transmission technologies. (see Step 1)
- **Negotiated Handover**: The Wallet Instance includes the service ``urn:nfc:sn:handover`` in a Service Parameter Record of the initial NDEF (NFC Data Exchange Format) message  (:ref:`WP_103b <wallet-credential-presentation-testcases>`). Upon selecting this service, the Relying Party Instance sends a Handover Request with an Alternative Carrier Record for each carrier it supports. The Wallet Instance replies with a Handover Select message containing exactly one selected carrier. (See Step 2-4)

**Step 1**: The Relying Party Instance reads the Wallet’s NFC Type 4 Tag to obtain a Handover Select message, which includes:
- Alternative Carrier Record is an NDEF record inside a Handover Select or Handover Request message. It points to one possible communication technology (called a “carrier”), such as NFC or BLE. It tells the reader about the supported carrier and a pointer (Auxiliary Data Reference) to more detailed information. The Alternative Carrier Record for the NFC device retrieval transmission technology MUST reference the Carrier Configuration Record with the ID reference “nfc”.
- Carrier Configuration Record provides the technical parameters needed actually to use that carrier. For NFC device retrieval transmission technology, it MUST have the type “iso.org:18013:nfc” and the ID reference “nfc”. The binary content of the Carrier Configuration Record MUST be encoded according to Table 1 of [`ISO18013-5`_ #9.2.2] (:ref:`WP_103d <wallet-credential-presentation-testcases>`).

For example:
For NFC, this defines maximum APDU (Application Protocol Data Unit) command/response lengths;
For BLE, it defines the Wallet Instance service UUID, characteristic UUIDs, MTU (Maximum Transmission Unit) size, and optional connection parameters;
If early ``SessionEstablishment`` is supported, it also lists the TNEP (Tag NDEF Exchange Protocol) service name used to send the ``SessionEstablishment`` message during handover.

.. note::
   For the NFC device retrieval transmission technology, the contents of the Alternative Carrier Record and Carrier Configuration Record(s) MUST comply with [`ISO18013-5`_ #9.2.2]. For the BLE device retrieval transmission technology, the contents of the Alternative Carrier Record and Carrier Configuration Record(s) MUST comply with [`ISO18013-5`_ #11.1.2].

- Auxiliary Data Record MUST carry the DeviceEngagement structure from the Wallet Instance to the Relying Party Instance as part of the auxiliary NDEF record in the Handover Select message. This record has the type ``iso.org:18013:deviceengagement``, the ID reference “mdoc”, and uses the NFC forum external type format (``0x04``). For each Alternative Carrier record, the Auxiliary Data Reference MUST point to the NDEF record containing the ``DeviceEngagement`` Structure (:ref:`WP_103e <wallet-credential-presentation-testcases>`).

**Step 2**: The Relying Party Instance reads the Wallet Instance's Initial NDEF (NFC Data Exchange Format) message, which contains a service parameter record for ``urn:nfc:sn:handover``, indicating the Wallet supports Negotiated Handover.

**Step 3**: The Relying Party Instance sends a Handover Request to the Wallet Instance listing the supported carriers.

**Step 4**: The Wallet Instance returns Handover Select constructed in response to the received Handover Request message. The contents of the Handover Select message is the same as Step 1 (:ref:`WP_103f <wallet-credential-presentation-testcases>`).

.. note::
   Use of Negotiated Handover for Device Engagement allows negotiation of transfer methods. For BLE, it additionally allows negotiation of keys used by the transmission layer. This provides improved user experience and enhances the security of data transmission [`ISO18013-5`_ #9.2.1].

.. note::
   Proceed only if the ``DeviceEngagement`` Capabilities include ``HandoverSessionEstablishmentSupport`` set to ``true`` (:ref:`WP_103c <wallet-credential-presentation-testcases>`). Otherwise, skip the early ``SessionEstablishment``. The early ``SessionEstablishment`` is sent via a dedicated TNEP service; the same ``SessionEstablishment`` MUST also be sent again during data retrieval and MUST match. If it does not match, the Wallet Instance terminates (:ref:`WP_103g <wallet-credential-presentation-testcases>`). If the early ``SessionEstablishment`` fails to send, proceed as normal (:ref:`WP_103h <wallet-credential-presentation-testcases>`).

**Step 5**: [Optional] Relying Party Instance opens the TNEP service named [urn:placeholder] with the Wallet Instance during the negotiated handover to deliver the early ``SessionEstablishment`` message.

**Step 6**: Relying Party Instance sends ``SessionEstablishment`` (e.g., ``EReaderKey`` + encrypted ``DeviceRequest``). Wallet Instance processes it; data retrieval has not started yet.

**Step 7**: Relying Party Instance closes the TNEP service.

.. note::
  If an optional ``SessionEstablishment`` message is sent during Negotiated Handover (Step 5), the Wallet Instance MUST verify that it matches the ``SessionEstablishment`` message received during Device Retrieval (using BLE or NFC secure channel). This verification is required to ensure a correct Session Binding.

Non-Normative Example
^^^^^^^^^^^^^^^^^^^^^^^
Below is a non-normative example of a ``DeviceEngagement`` structure for Data Retrieval over BLE and NFC.
  .. literalinclude:: ../../examples/iso-device-engagement-NFC-BLE.txt
   :language: text

``SessionEstablishment`` over BLE
----------------------------------
The following figure illustrates the low-level flow compliant with `ISO18013-5`_ for ``SessionEstablishment`` over BLE corresponding to Boxes B in Figure 8.10.

.. _fig_SessionEstablishment-BLE:
.. plantuml:: plantuml/session-establishment-over-ble.puml
    :width: 90%
    :alt: The figure illustrates the Session Establishment over BLE Presentation Flow in proximity.
    :caption: `Session Establishment over BLE. <https://www.plantuml.com/plantuml/svg/ZLHDRzim3BthLn2-r3aaG3PWXs8RYYu15c0PXcRfBhimCki8ioLDakNq5-r_x9UDabitmVeL184Zak_nFLA-y05TwDf6O1UCxjeTEI4idocfBEe0nGzi6WgmrIeKW1xwq_3LDrXfHj6ISZWAWJAeY84uTNpaupFuyDI7OvTVbY2DriGLHWCnvAvHVjyIivGtphImtQuMu4YIYbI1qh2Wg2J1KjTOKqgSF4iYTkO0HIBo53eBfJCDJR7MnhEUII40ullfn_uSblViC6JBpX78FN9xZI1T0IEz9EYQdBgvPKsEMmvWYHn4XR2gaY86SsmEvoHkAF_-cSzdyzdRsPldDMG9zn0aVq7PLaP2J6IAF8GzZPIEi2ANTV7Ns01N-MHeJKbCJdEapve_cTPsF2awM2vcWpFB48xdkVJntYCs7Pt08BirpccewLNOZz0ZCamFmDZbaBDMliKWznFuJgvLEktDwLfm3RlFl_0mXPXfYs93tdFAydXnYW8CM_FO54Nouwu6BfMkbAx5866TcdWQiULZthS7XLNdk1X-QlXAjGaAatkVKLUPEojFO_clZZTu4yZ2Ep4QiRxBUOKLoGXnDWndazn0yAhMZClCR9DqjpOruiXRepr1EIfQOC2Yc737kJb7lpk-Rwao1ATsl0L-z4s8YevkyT6VNbmmBRyx_W40>`_

**Step 1**: The Wallet Instance and Relying Party Instance establish a secure BLE connection [`ISO18013-5`_ #11.1]. The Relying Party Instance (central) connects to the Wallet Instance (peripheral) using the Wallet Instance service UUID provided by DeviceEngagement, then discovers services/characteristics, and enables notifications as needed (:ref:`WP_112c <wallet-credential-presentation-testcases>`).

**Step 2-5**: [Optional] Wallet Instance initiates verification by preparing to check the Relying Party’s identity via the Ident characteristic, that is a BLE GATT characteristic that carries an identifier value as described in [`ISO18013-5`_ #11.1.3.2]. The Wallet Instance derives the expected Ident value and reads the Relying Party's Ident characteristic, comparing it to the expected Ident, and terminating the BLE connection if a mismatch may occur.

.. note::
   The purpose of the Ident characteristic is only to verify whether the Wallet Instance is connected to the correct Relying Party Instance before starting data retrieval. If the Wallet Instance is connected to the wrong Relying Party Instance, session establishment will fail. Connecting and disconnecting to a Relying Party Instance takes a relatively large amount of time; therefore, it is faster to implement methods to identify the correct Relying Party Instance [`ISO18013-5`_ #11.1.3.1] (:ref:`WP_112d <wallet-credential-presentation-testcases>`).

**Step 6**: Relying Party Instance sends the encrypted ``SessionEstablishment`` message (includes ``EReaderKey`` and encrypted ``DeviceRequest``) over the established BLE connection.

**Step 7-8**: [Optional] If the Wallet Unit receives the ``SessionEstablishment`` message during Negotiated Handover, the Wallet Unit MUST verify if this ``SessionEstablishment`` message matches the ``SessionEstablishment`` message received during the data retrieval phase (i.e., Step 6). In the event of a mismatch, the Wallet Unit MUST terminate the BLE connection [`ISO18013-5`_ #9.2.3].

``SessionData`` over BLE
--------------------------
The following figure illustrates the low-level flow compliant with `ISO18013-5`_ for ``SessionData`` over BLE corresponding to Boxes C in Figure 8.10.

.. _fig_SessionData-BLE:
.. plantuml:: plantuml/session-data-over-ble.puml
    :width: 90%
    :alt: The figure illustrates the Session Data over BLE Presentation Flow in proximity.
    :caption: `Session Data over BLE. <https://www.plantuml.com/plantuml/svg/LO-n3i8m34JtV8ML2GP-W05L20Oa1aI5M5ZSr898hLjYfn5_Zs50PRjtT_B9bIWcpNtdCEl0kMyeEJUQ5qCSaHNy5RkE52uSrGCAbF_uV883snKEz8qdvp1ed539gZzfTbbjfZNKn2qWIBmpcJ0W3kargb4Y6GSMWeNtDOd4WNUewFqIRboYFgpnp2IVBggcs6GbWM6Y1DlZthcMPeCpAAwoMNlp3G00>`_

**Step 1**: The Wallet Instance sends the final APDU containing either the last block DeviceResponse (with requested attributes) or a status code, after which the session may end or continue with a new request.


``SessionEstablishment`` over NFC
----------------------------------
.. note::
   If Device Engagement is initiated via a QR code, the Relying Party Instance has no standardised way to signal its intent to use NFC for subsequent data transfer. This could lead to a poor user experience, as the User might not be aware that they need to use NFC. This issue is avoided when NFC is used for the Device Engagement, as it implicitly establishes the data transfer method [`ISO18013-5`_ #8.2.5].

.. note::
   Due to the limited data transfer rate of NFC, if a large amount of data is required for a transaction, it may be neither practical nor reasonable for a User to keep the device within the RF range of the Relying Party Instance for the duration of the transaction. Furthermore, loss of signal when a device leaves the RF field necessitates re-initiating the transaction. This can only be avoided if all necessary User interactions with the Wallet Instance are performed while the device remains in the field, or if no User interaction is required during the active transmission phase [`ISO18013-5`_ #8.2.5].

   The following figure illustrates the low-level flow compliant with `ISO18013-5`_ for ``SessionEstablishment`` over NFC corresponding to Box B in Figure 8.10.

.. _fig_SessionEstablishment-NFC:
.. plantuml:: plantuml/session-establishment-over-nfc.puml
    :width: 90%
    :alt: The figure illustrates the Session Establishment over NFC Presentation Flow in proximity.
    :caption: `Session Establishment over NFC. <https://www.plantuml.com/plantuml/svg/ZP9BJyCm383l-HLMJzjX9pWX3G6b20HxYF6uSCbIRutKE25nM_ZtE6n2GsWIjyJv77-ESv5OH-vSgtJ7dZgtngXKa9WrDcXYA5vrsoB3Crc6qVAkBCS5w0J3R-fn2NSabv51eShh7TGhfGtRNZDAmizImjCfWAkzWSiGMciqMq-mmXRDzsewLJrCpc4uWqL0sg7w07sZLVLGbKzWl7EQQZLal3-3lQxnjB7H9G57Ytlm4IpLEHaJE1yHQiqQsCC6sJJZRw6YM65ASdibZQnRcng7n4LnQ5EHYP-1iJvEHtplCF4RLVENwc6nh8uvHap1Kvt-g-W3mxucN6MMjcgOd8lLJ0jntCX9M6zH2XgqlRZNNPHaUHkOuzQprRcXMr7qFKOOB3V03VxDip8ZnW0dazFSp4TkPZJRKpERNFOOmnD6PobFUdvJvb7GRgmAvH5KZGT_uc3Jgmivbx_u1G00>`_

Definitions (Acronyms and Commands)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::
   :class: longtable
   :widths: 15 85
   :header-rows: 1

   * - **Acronym/Command**
     - **Description**

   * - **PICC**
     - Proximity Integrated Circuit Card, implemented by Wallet Units acting as a NFC tag.

   * - **PCD**
     - Proximity Coupling Device, impletented by Relying Party instances using `APDU` exchanges.

   * - **AID**
     - Application Identifier, unique ID used in SELECT `APDU` command to engage the Wallet Instance.

   * - **APDU**
     - Application Protocol Data Unit, a standard message format for communication between Relying Party Instance (PCD) and Wallet (PICC) consists of Command APDUs (e.g., `SELECT`, `ENVELOPE`, `GET RESPONSE`) from the reader and Response `APDUs` from the wallet, which include data exchange and end exchange using status words (`SW1/SW2`).

   * - **SELECT APDU**
     - Command that opens the Wallet Instance by `AID`.  Response includes File Control Information (FCI) and Status Word (`SW1/SW2`).

   * - **ENVELOPE APDU**
     - Command that carries session messages (e.g., ``SessionEstablishment``).  Response indicates processing status (`OK` or `more data`).

   * - **GET RESPONSE APDU**
     - Command that retrieves additional response data when the Wallet signals "more data" is available (`SW1=61`).

   * - **SW1/SW2**
     - `SW1/SW2` (Status Words) — Two-byte status code at the end of every response.  Common values: `90 00 = success`, `61 XX = more data`, `6A 82 = file/application not found`.


**Step 1**: The Relying Party Instance (PCD) sends a SELECT `APDU` command with the Application Identifier (`AID: A0 00 00 02 48 04 00`) to engage the Wallet Instance.


**Step 2**: The Wallet Instance (PICC) responds with File Control Information (FCI) and status words (SW1/SW2), either confirming success (`90 00`) or indicating that more data (`61 XX`) (:ref:`WP_112e <wallet-credential-presentation-testcases>`).


**Step 3**: The Relying Party Instance sends an ENVELOPE `APDU` carrying the ``SessionEstablishment`` message, which contains the encrypted ``DeviceRequest`` and its ephemeral public key for session setup.


**Step 4**: The Wallet Instance processes ``SessionEstablishment`` and returns an `APDU` response with `SW1/SW2` (`OK` or `more data` to fetch), confirming the start of secure session context (:ref:`WP_112f <wallet-credential-presentation-testcases>`).


**Step 5-6**: [Optional] The Wallet Instance receives the ``SessionEstablishment`` message during Negotiated Handover, the Wallet Instance MUST verify that this ``SessionEstablishment`` message matches the same message received during the data retrieval phase (i.e., Step 3-4). In the event of a mismatch, the Wallet Instance MUST terminate the NFC connection [`ISO18013-5`_ #9.2.3].


``SessionData`` over NFC
--------------------------
The following figure illustrates the low-level flow compliant with `ISO18013-5`_ for ``SessionData`` over NFC corresponding to Box C in Figure 8.10.

.. _fig_SessionData-NFC:
.. plantuml:: plantuml/session-data-over-nfc.puml
    :width: 90%
    :alt: The figure illustrates the Session Data over NFC Presentation Flow in proximity.
    :caption: `Session Data over NFC. <https://www.plantuml.com/plantuml/svg/PP3DJiD038Jl-nIZN4WEl42be4ffGBr0b81wuU8afbrfVyAkavItPn6YAkhDjkORZMSRXOBCrYYQnRlPzXoKcj9D3teY9yWEP0mBtfmMvCs-geeC5B7-LxKDzYwPkO6JgjhzYXQbQ12za702BcCwgxkoH9Pr7AFsRaT2MORwF9p87HbbgOpt4mudRHZM1yQO9D0Hj90sr1jMm8Bx1wmRjFmvSnGuFWi-0XqjfqnuTtYgNz7MNVFotDKOlBNanWIkF-2okGbmONDsG_YQXCT2SKB-W4VjoDnWEOa4tS_24JuWrI1pB9GQ-UhxgsLHssIQMly6>`_

**Step 1-2**: As long as the Wallet Instance signals that more data is available (`61 XX`), the Relying Party Instance issues `GET RESPONSE APDUs` to request the next block.  The Wallet Instance returns encrypted ``SessionData`` fragments until all data is delivered.


**Step 3**: The Wallet Instance sends the final `APDU` containing either the last block DeviceResponse (with requested attributes) or a status code, after which the session may end or continue with a new request.

Device Engagement
------------------

The Device Engagement structure MUST be CBOR encoded and have at least the following components (:ref:`PPR-001 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`, :ref:`PPR-021 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`, :ref:`PPR-022 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`, and :ref:`WP_102 <wallet-credential-presentation-testcases>`):

.. list-table::
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Component**
     - **Description**

   * - **Version**
     - *(tstr)*. Version of the Device Engagement structure.

   * - **Security**
     - *(array)*. Contains two mandatory values:

       - *(int)*. Cipher suite identifier. See Table 22 of `ISO18013-5`_.

       - *(bstr)*. Public ephemeral key generated by the Wallet Instance, used by the Relying Party Instance to derive the Session Key. The key MUST be of a type allowed by the selected cipher suite (:ref:`PPR-022 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`).

   * - **DeviceRetrievalMode-BLEOptions**
     - *(map)*. Provides options for the BLE connection, such as Peripheral Server or Central Client mode, and the device UUID. See Table 2 of `ISO18013-5`_ for the detailed mapping.

       If the Wallet Instance indicates during Device Engagement that it supports both modes, the Relying Party Instance  SHOULD select the mdoc central client mode  [`ISO18013-5`_ #11.1.3.1].

       Only present when performing Device Engagement using the QR code. Absent when using NFC to perform Device Engagement.


   * - **DeviceRetrievalMode-NFCOptions**
     - *(map)*. Provides options for NFC connections, including the supported role (PICC or PCD) and maximum PDU command/response sizes. See Table 2 of `ISO18013-5`_ for the detailed mapping.

       In case NFC is used for Device Retrieval, the Wallet Instance MUST support PICC mode and the Relying Party Instance MUST support PCD mode [`ISO18013-5`_ #11.2].

       Only present when performing Device Engagement using the QR code. Absent when using NFC to perform Device Engagement.

   * - **Capabilities**
     - *(map)*. Declares optional capabilities supported by the mdoc, that are:

       - **HandoverSessionEstablishmentSupport** *(bool)*. If present, it MUST be set to `true`. Indicates support for receiving the `SessionEstablishment` message during Negotiated Handover, as defined in [`ISO18013-5`_ #9.2.3] (:ref:`PPR-024 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`).

       - **ReaderAuthAllSupport** *(bool)*. If present, it MUST be set to `true`. Indicates support for receiving the `ReaderAuthAll` structure in the mdoc request, as defined in [`ISO18013-5`_ #10.2.6] (:ref:`PPR-025 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`).

   * - **OriginInfos**
     - *(array)*. Describes the interface used to receive and deliver the engagement structure.

       `OriginInfos` MAY be an empty array.


mdoc Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


The messages in the mdoc Request MUST be encoded using CBOR. The resulting CBOR byte string for the mdoc Request MUST be encrypted with the Session Key obtained after the Device Engagement phase and MUST be transmitted using the BLE or NFC protocol (:ref:`PPR-026 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`, :ref:`PPR-027 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`, :ref:`PPR-028 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`).

Each mdoc Request MUST be compliant with the following structure, and MUST include the following components, unless otherwise specified:

.. list-table::
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Component**
     - **Description**

   * - **version**
     - *(tstr)*. Version of the mdoc Request structure. Enables compatibility management across different versions or implementation profiles.

   * - **docRequests**
     - *(array)*. Each entry is a `DocRequest` containing:

       - **itemsRequest**. CBOR-encoded `ItemsRequest` structure, formatted as:

         - **docType** *(tstr)*. The type of document requested. See :ref:`credential-data-model:mdoc-CBOR Credential Format`.

         - **nameSpaces** *(map)*. A map of namespace identifiers to requested *DataElements*.

           Each entry in `DataElements` includes:

           - **DataElementIdentifier** *(tstr)*. The identifier of the requested data element.
           - **IntentToRetain** *(bool)*. Indicates whether the Relying Party intends to retain the value of the data element.

       - **readerAuth** *(COSE_Sign1, CONDITIONAL)*. Used to authenticate the Relying Party Instance for each `DocRequest`. The signature is computed over `ReaderAuthentication` data, as defined in [`ISO18013-5`_ #12.5].

         This component MUST be present only if `readerAuthAll` is not used (:ref:`PPR-025 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`).

   * - **readerAuthAll**
     - *(COSE_Sign1, CONDITIONAL)*. Used to authenticate the Relying Party once for all `DocRequest`s. The signature is computed over `ReaderAuthenticationAll` data, as defined in [`ISO18013-5`_ #12.5].

       This component MUST be present only if `ReaderAuthAllSupport` is set to `true` in the DeviceEngagement structure, and individual `readerAuth` fields are not used (:ref:`PPR-025 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`).


mdoc Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The messages in the mdoc Response MUST be encoded using CBOR and MUST be encrypted with the Session Key obtained after the Device Engagement phase (:ref:`PPR-029 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`, :ref:`PPR-030 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`).

Each mdoc Response MUST be compliant with the following structure, and MUST include the following components, unless otherwise specified:

.. _table-mdoc-attributes:
.. list-table::
   :class: longtable
   :widths: 25 75
   :header-rows: 1

   * - **Component**
     - **Description**

   * - **version**
     - *(tstr)*. Version of the mdoc Response structure. Enables tracking changes and maintaining compatibility across versions of the standard or implementation profiles.

   * - **documents**
     - *(array of Documents, OPTIONAL)*. CBOR-encoded collection of documents returned in response to the request. Each document includes `issuerSigned` and `deviceSigned` components, and follows the structure defined in [`ISO18013-5`_ #10.3.3].

   * - **documentErrors**
     - *(map, OPTIONAL)*. A map of error codes for unreturned documents, as defined in [`ISO18013-5`_ #10.3.6]. Each key is a `docType`, and each value is an `ErrorCode` (int) indicating the reason why the document was not returned.

   * - **status**
     - *(uint)*. Status code indicating the outcome of the request. For example, `"status": 0` means successful processing. For details, see Table 3 (ResponseStatus) of [`ISO18013-5`_ #10.3.5].


Each document in **documents** MUST be compliant with the following structure, and it MUST include the following components, unless otherwise specified (:ref:`PPR-029 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>`):

.. _table-mdoc-documents-attributes:
.. list-table::
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Component**
     - **Description**

   * - **docType**
     - *(tstr)*. Document type identifier. For example, for an mDL, the value MUST be ``org.iso.18013.5.1.mDL``.

   * - **issuerSigned**
     - *(bstr)*. Contains the `IssuerNameSpaces` structure, which includes data elements signed by the Issuer, and the `issuerAuth` structure, which ensures their authenticity and integrity using the Mobile Security Object (MSO). See :ref:`credential-data-model:mdoc-CBOR Credential Format`.

   * - **deviceSigned**
     - *(bstr)*. Contains the `DeviceNameSpaces` structure (data elements signed by the Wallet Instance), and the `deviceAuth` structure, which includes the authentication data signed by the Wallet Instance. See the table below for details.

   * - **errors**
     - *(map, OPTIONAL)*. A map of error codes for each unreturned data element grouped by namespace. Each key represents a namespace, and each value is a map of data element identifiers to corresponding error codes. See [`ISO18013-5`_ #10.3.6] for details on the errors structure.


A **deviceSigned** data structure MUST be compliant with the following structure (:ref:`WP_111a <wallet-credential-presentation-testcases>`), and MUST include the following components:

.. list-table::
   :class: longtable
   :widths: 25 75
   :header-rows: 1

   * - **Component**
     - **Description**

   * - **nameSpaces**
     - *(bstr)*. Contains the `DeviceNameSpaces` structure. It MAY be an empty structure. `DeviceNameSpaces` maps namespace identifiers to a set of data elements signed by the Wallet Instance.

       Each namespace contains one or more `DeviceSignedItem`, where each item includes:

       - **DataItemName** *(tstr)*. The identifier of the data element.
       - **DataItemValue** *(any)*. The value of the data element.

   * - **deviceAuth**
     - *(COSE_Sign1)*. Contains the `DeviceAuth` structure, which MUST include the **deviceSignature** for the Wallet Instance authentication. The signature is computed over the `DeviceAuthentication` data, which binds the returned elements to the session and the request. See [`ISO18013-5`_ #12.4] for details on the authentication structure.

Session Termination
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The session MUST be terminated if at least one of the following conditions occur (:ref:`PPR-007 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>` and :ref:`WP_113–113a <wallet-credential-presentation-testcases>`):

- After a time-out of no activity of receiving or sending session establishment or session data messages occurs. The time-out for no activity implemented by the Wallet Instance and the Relying Party Instance SHOULD be no less than 300 seconds;
- When the Wallet Instance does not accept any more requests;
- When the Relying Party Instance does not send any further requests.

If the Wallet Instance and the Relying Party Instance do not send or receive any further requests, the session termination MUST be initiated as follows (:ref:`PPR-007 <test-plans-proximity-presentation:Proximity Credential Verifier Test Matrix>` and :ref:`WP_113 <wallet-credential-presentation-testcases>`):

- Send the status code for session termination, or
- Dispatch the "End" command as outlined in [`ISO18013-5`_ #11.1.3.3].

When a session is terminated, the Wallet Instance and the Relying Party Instance MUST perform at least the following actions (:ref:`WP_114 <wallet-credential-presentation-testcases>`):

- Destruction of session keys and related ephemeral key material;
- Closure of the communication channel used for data retrieval.

.. note::
  See :ref:`credential-data-model:mdoc-CBOR Credential Format` for the meaning of CBOR type acronyms.


