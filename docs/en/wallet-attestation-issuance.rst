.. include:: ../common/common_definitions.rst
.. Included via wallet-instance-functionalities.rst at title level '=' (document title).


Key Attestation Issuance
=================================

This section describes how the Wallet Provider issues Key Attestations.

.. plantuml:: plantuml/wallet-attestation-issuance.puml
    :width: 99%
    :alt: The figure illustrates the Sequence Diagram for Key Attestations acquisition.
    :caption: `Sequence Diagram for Key Attestations acquisition. <https://www.plantuml.com/plantuml/svg/fLNVRoCr47xtNp7oFP1AUvL0WeTAe8jAQIlG4Ltlu86WQ7OzoLhPZ1VRcrB-UcntcztwN7GLBr7i_UR7VDzuvftpQFrmw0GEtl1mgCcALYk2hJ6-DdyByTKg87IZUsJl13RUM92V75a9w61mmQ2V421_nwuZ3xSSN7D32OLz3yzHFzC3BBsd0FBQC2nNjov1z-WTl76zrRpRMI9-RlSZ7NL3mRkddTN-0Ux8nfl90POTPEcjh3bgHHPgRFR4AfdMpLw8MD7R7qB65_21_Xh8UK1WkWVJatrCrhVersp3Lst90K9UJQH97z5Jh5o8y3Dwl6ofsOFUmgLzwBtPMUnRtS0DMdMFbfAZDN_47IoaRCVRpPuUDXvtKfvLK2Ak0cG5EJNf4qIlU4JTOTtHF9LhubWFEJ1CO2mWrEYR5imM6akAs6li8CI67hLTk3Fm1ce2JD59WUOycvXrJBOVwitNKbOm7gq-flFv-Na54uGp28SAXR1iF84vaetiLK4KUFFBxVNDn-iFLrVlnIE5kOpQGPGv9kzRWfz8ZM8bQapjKJDex-107XLw5CGgHHev2M4cmQLa4tjNJaActWW_2JcnDuEchoEvqwsYPovA2WHqqsbYluc9RLfqhKpzU7Up_ERRxnOdPnNyCP5NvlFFCoY6-8z-MvdLccVTvlIEqGys18Jl8PuMYrA65PHRDB-EqeRxfxJGkujonLjZvzth7Dcee8Wce-6SC_q4tU0JLCerrsPW5LiraGR9UfAbQ9GYPtChfDlv-5ANhApH2jv-rkpRpjmdKyAcFJqKCVLCd6LZsVkKVMFf9RqdHwEQGaIRO9dN7R_Zc4QnvcWvrLmmW5E7GExPRRmPmLAEwXSyLEbkabPHLZHrZY9x-jUxaJdy4kPIMg-cwlzrI1B_q_9B6oLYNqrWvgr88h4gZuUyxyOfTI7bpDaOwiLOXUmgAB_w2gQ9i-RI8vyDdSV3VNey6sUw8SRRQ5M-Fv9rftpw3dqWz12ApwYO9l8TiO9PeVb8Vd_Q5U5KGNbPw6t-ka4xqApZXjF_a4fBuXZ-Ap4upJlul6Pn5I1iFCstm6_HvDaMA7_CcO_nfY6yVnp2PTEYccLeISiYSj8knarD7Kr2uMj-gTjcZYuj5TfIp1TWmOlh3JiI-KAS7OEXU4UiXaFtBm00>`_


.. .. figure:: ../../images/wallet_instance_acquisition.svg
..   :figwidth: 100%
..   :align: center
..   :target: https://www.plantuml.com/plantuml/svg/XLHDRnCn4BtxLupS0waKBaXmg0HgL4fRWL3K5hX4YYRhoUue6tknPxU4Nu-zJRFRui1b5TjlFjwRUJaFWbxQRQsm5MVRxOgygjWGh9sJbVkbNZKHm0KtQ4KfBCHvqDy2UGqOe0qHFqA0_e5rJG8tDWZQWdeKDWqyHtsaZWkAAA7Ii-pWZdn_CvlVXCSOb00deV5ioz8JsMoPkNST6_Ammc93rlIXgsAZb4gjlVuGIv_1BVriAGWWM7e0rv17OMT1AfI5zV6LFGL0s6UTnNvd8XIanoNMtA5G8g9K_EppNbHKR83NSE5tZRZIOrDn0TVepGDwWi-qWuMznn8cMbVxs-M6Tal1KkjJu03O8TUugacDCr-HJKscfYnGKz4s7ck8eT0W-vJlSDidRDgLrbFuwzfp5mifvQqJ0jUHJoIcKI8u-N9pTNr_TNjv-LKzCdafAWT8eeDRWrG4dyWyAOVMW5i9iWMM05iID2Yeo9fKwK0crXdarzgwj19w4BGVLVpqo84sh3s5QXJGO_RQ3BU6neco0aPqKJDPMQR-bXM6IlTBSdSzU_FstUIGR0fPIK-pIVynxxcRB-nese5BYz9wYcNVGpfD9hcUff1TaV7rCD6XBPHmbkMeqjCW6JyvROaXa4z3r3hBBU-1mn0VMAfZ-QQG9pw5GUQ5pV4yedwl5vc-wCW6-IqVRTmTMVCV8iztSB17EkRjaOp-ujyjEOGj2sFDlydqjkZYRwFQmBRCZdJmoB3ttrCC2WqwPH_pgkUXkJdaaJdTunQFm1UUZc_6o9h79G-Diu5U6dPyZl7gdAnfj_KV

..   Sequence Diagram for Wallet App Attestation acquisition

**Step 1**: The User initiates a new operation that necessitates the acquisition of a Key Attestation.

**Steps 2-3**: The Wallet Instance MUST:

  1. Verify the existence of Cryptographic Hardware Keys. If none exist, Wallet Instance re-initialization is required (:ref:`WP_140a <wallet-instance-optional-testcases>`).
  2. Generate one or batch of asymmetric Credential key pair(s) to be attested in Key Attestation (``key_pub_1``, ``key_priv_1``, ..., ``key_pub_n``, ``key_priv_n``).
  3. Verify the Wallet Provider's federation membership and retrieve its metadata (:ref:`WP_023 <wallet-instance-testcases>`).

**Steps 4-6 (Nonce Retrieval)**: The Wallet Instance requests a ``nonce`` value from the :ref:`wallet-provider-endpoint:Wallet Solution Nonce Endpoint` of the Wallet Provider Backend (:ref:`WP_140b <wallet-instance-optional-testcases>`). The ``nonce`` is required to be unpredictable and serves as the main defense against replay attacks.

The ``nonce`` MUST ensure single-use within a predetermined time frame.

Upon a successful request, the Wallet Provider generates and returns the nonce value to the Wallet Instance.

**Step 7**: The Wallet Instance performs the following actions (:ref:`WP_140c <wallet-instance-optional-testcases>`):

* Creates ``client_data``, a JSON object that includes the ``nonce`` and a ``jwk_thumbprints`` field containing a JSON array of the JWK thumbprints corresponding to the public keys ``(key_pub_1,...,key_pub_n)``.
* Computes ``client_data_hash`` by applying the ``SHA256`` algorithm to the ``client_data``.

Below is a non-normative example of the ``client_data`` JSON object.

.. code-block:: json

  {
    "nonce": "i4ThI2Jhbu81i8mqyWEuDG5t",
    "jwk_thumbprints": ["vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"]
  }


**Steps 8-11**: The Wallet Instance:

* produces an ``hardware_signature`` value by signing the ``client_data_hash``  with the Wallet Hardware's private key, serving as a proof of possession for the Cryptographic Hardware Keys (:ref:`WP_140d <wallet-instance-optional-testcases>`).
* requests the Device Integrity Service to create an ``integrity_assertion`` value linked to the ``client_data_hash``.
* receives a signed ``integrity_assertion`` value for Wallet Instance from the Device Integrity Service, authenticated by the OEM (:ref:`WP_140e <wallet-instance-optional-testcases>`).

.. note::
  ``integrity_assertion`` is a custom payload generated by Device Integrity Service, signed by device OEM and encoded in base64 to have uniformity between different devices.

.. note::
   In the case of Android OS, the flow continues based on **Steps 12-15**, otherwise for the case of iOS, the flow continues based on **Steps 16-19**.

**Steps 12-15**: The Wallet Instance:

*  requests the Key Attestation API to create an ``key_attestation`` value for each ``client_data_hash`` per each ``key_pub``.
*  receives a signed ``key_attestation`` value from the Key Attestation API, authenticated by the OEM.
*  generate ``keys_to_attest`` value by signing the ``key_attestation`` using the private key of the initially generated credential key pair (``priv_key``).

**Steps 16-19**: The Wallet Instance:

*  requests the Device Integrity Service to create an ``integrity_assertion`` value for each ``client_data_hash`` per each ``key_pub``.
*  receives a signed ``integrity_assertion`` value from the Device Integrity Service, authenticated by the OEM.
*  generate ``keys_to_attest`` value by signing the ``integrity_assertion`` that is obtained for the Key Attestation using the private key of the initially generated credential key pair (``priv_key``).

**Steps 20-21 (Key Attestation Issuance Request)**: The Wallet Instance:

* Constructs the Key Attestation Request in the form of a JWT. This JWT includes the ``integrity_assertion``, ``keys_to_attest``, ``hardware_signature``, ``nonce``, ``hardware_key_tag``, ``cnf``, ``platform`` and other configuration related parameters (see :ref:`Table of the Key Attestation Request Body <table_ka_request_claim>`). The Key Attestation Request MUST be signed using the private key related to the public key included in the request, using the ``cnf`` parameter (first element of ``keys_to_attest``) (:ref:`WP_140–141 <wallet-instance-optional-testcases>`).
* Submits the Key Attestation Request to the :ref:`wallet-provider-endpoint:Key Attestation Issuance Endpoint` of the Wallet Provider Backend.

.. note::
  ``keys_to_attest`` contains a ``key_attestation`` object in case of Android and ``integrity_assertion`` in case of iOS.

The Wallet Instance MUST send the signed Key Attestation Request JWT as an ``assertion`` parameter in the body of an HTTP request to the Wallet Provider's :ref:`wallet-provider-endpoint:Key Attestation Issuance Endpoint` (:ref:`WP_142 <wallet-instance-optional-testcases>`).

**Steps 22-27**: The Wallet Provider Backend evaluates the Key Attestation Request and MUST perform the following checks (:ref:`WP_143 <wallet-instance-optional-testcases>`):

  1. The request MUST include all required HTTP header parameters as defined in :ref:`wallet-provider-endpoint:Key Attestation Issuance Request` (:ref:`WP_143a <wallet-instance-optional-testcases>`).
  2. The signature of the Key Attestation Request MUST be valid and verifiable using the provided ``jwk`` (:ref:`WP_143b <wallet-instance-optional-testcases>`).
  3. The ``nonce`` value MUST have been generated by the Wallet Provider and not previously used (:ref:`WP_143c <wallet-instance-optional-testcases>`).
  4. A valid and currently registered Wallet Instance associated with the provided ``hardware_key_tag`` MUST exist (:ref:`WP_143d <wallet-instance-optional-testcases>`).
  5. The signature of the ``keys_to_attest`` parameter Must be first validated using the provided ``jwk`` and its value (``key_attestation`` in case of Android or ``integrity_assertion`` in case of iOS) MUST be validated according to the device manufacturer's guidelines.
  6. The ``client_data`` MUST be reconstructed using the ``nonce`` and their respective thumbprint JWKs ``[key_pub_1,...,key_pub_n]``. The ``hardware_signature`` parameter value is then validated using the registered Cryptographic Hardware Key's public key associated with the Wallet Instance (:ref:`WP_143e <wallet-instance-optional-testcases>`).
  7. The ``integrity_assertion`` MUST be validated according to the device manufacturer's guidelines. The specific checks performed by the Wallet Provider are detailed in the operating system manufacturer's documentation (:ref:`WP_143f <wallet-instance-optional-testcases>`).
  8. The device in use MUST be free of known security flaws and meet the minimum security requirements defined by the Wallet Provider.
  9. The URL in the ``iss`` parameter MUST match the Wallet Provider's URL identifier (:ref:`WP_143g <wallet-instance-optional-testcases>`).

Upon successful completion of all checks, the Wallet Provider issues a Key Attestation valid for at least one month.

**Step 28 (Key Attestation Issuance Response)**: Upon successful completion, the Wallet Provider MUST return a confirmation response using status code set with ``200`` and Content-Type ``application/json``. The response MUST contain the Key Attestations signed by the Wallet Provider using the JWT format. The Wallet Instance MUST perform security and integrity verification of the Key Attestations received, along with the trust verification already evaluated about the Issuer (:ref:`WP_030–031 <wallet-instance-testcases>`).


Below is a non-normative example of the response.

.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json

  {
    "key_attestation": "omppc3N1ZXJBdXRohEOhASaiBE...dElEAnFlbGVtZW50SWRl"
  }


