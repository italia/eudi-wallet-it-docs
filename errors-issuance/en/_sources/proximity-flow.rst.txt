

.. _proximity_flow_sec:

Proximity Flow
==============

This section describes how a Verifier requests the presentation of an *mDoc-CBOR* Credential to a Wallet Instance according to the *ISO 18013-5 Specification*. Only *Supervised Device Retrieval flow* is supported in this technical implementation profile. 

The presentation phase is divided into three sub-phases: 
 
  1. **Device Engagement**: This subphase begins when the User is prompted to disclose certain attributes from the mDoc(s). The objective of this subphase is to establish a secure communication channel between the Wallet Instance and the Verifier App, so that the mDoc requests and responses can be exchanged during the communication subphase.
  The messages exchanged in this subphase are transmitted through short-range technologies to limit the possibility of interception and eavesdropping.
  This technical implementation profile exclusively supports QR code for Device Engagement.

  2. **Session establishment**: During the session establishment phase, the Verifier App sets up a secure connection. All data transmitted over this connection is encrypted using a session key, which is known to both the Wallet Instance and the Verifier at this stage.
  The established session MAY be terminated based on the conditions as detailed in [ISO18013-5#9.1.1.4].

  3. **Communication - Device Retrieval**: The Verifier App encrypts the mDoc request with the appropriate session key and sends it to the Wallet Instance together with its public key in a session establishment message. The mDoc uses the data from the session establishment message to derive the session key and decrypt the mDoc request.
  During the communication subphase, the Verifier App has the option to request information from the Wallet using mDoc requests and responses. The primary mode of communication is the secure channel established during the session setup. The Wallet Instance encrypts the mDoc response using the session key and transmits it to the Verifier App via a session data message. This technical implementation profile only supports Bluetooth Low Energy (BLE) for the communication sub-phase.


The following figure illustrates the flow diagram compliant with ISO 18013-5 for proximity flow.

.. _fig_High-Level-Flow-ITWallet-Presentation-ISO:
.. figure:: ../../images/High-Level-Flow-ITWallet-Presentation-ISO.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/bL9BZnCn3BxFhx3A0H3q3_ImMlOXXBJYqGguzE9ct2RQn0bvJDb_ZoSP3QFI2xab_Xx-xDocZ34NPpiisNDn1ufT1t9GPH_XUw88cA3KjuF_3QlnwNM2dHDYq9vf1Q-Up4ddErkeme9KZ381ESFg9rfB6JwnEB4IiAYTAuou7nN_Al-WQ8xcVzHd2dm8eKeFI-cMfApNDpVd3Nm9n90rmKLBa3s4I8b441dSWrTm7wcNkq7RD3xxJE07CIhlXmqyq624-CWdF94RYQaSWiP4iAweRzjr1vLvRkOVYIcYY32TWO8c9rSBp_GYWKoSe88LzPtsvx5HKO5xtnCSVVpNibA6ATjE8IyfKr7aBgptVDry0WlPXIBOH2aPpoEcbgzDOJTXIEPui2PfrqROZogki56OfNuvcxkdHv5N9H8eZSnaPLRJwUPU95JTn9P-5J60Tn2AcAZQjJ_MiCljxndUN6texN8Dr-ErSjd0roZrNEUjFDSVaJqaZP6gOMpDK0-61UHglkcJjJL75Cx4NHflAKT30xLGH_41wnLQIDb7FD6C7URSAOZCSfCjxyjSWcHEZBb4slCuTQL9FJVsWDRq9akuxfQuByx-0G00

    High-Level Proximity Flow

**Step 1-3**: The Verifier requests the User to reveal certain attributes from their mDoc(s) stored in the Wallet Instance. The User initiates the Wallet Instance. The Wallet Instance MUST create a new temporary key pair (EDeviceKey.Priv, EDeviceKey.Pub), and incorporate the cipher suite identifier, the identifier of the elliptic curve for key agreement, and the EDeviceKey public point into the device engagement structure (refer to [ISO18013-5#9.1.1.4]). This key pair is temporary and MUST be invalidated immediately after the secure channel is established. Finally, the Wallet Instance displays the QR Code for Device Engagement.

Below an example of a device engagement structure that utilizes QR for device engagement and Bluetooth Low Energy (BLE) for data retrieval.

CBOR data:

.. code-block:: 

  a30063312e30018201d818584ba4010220012158205a88d182bce5f42efa59943f33359d2e8a968ff289d93e5fa444b624343167fe225820b16e8cf858ddc7690407ba61d4c338237a8cfcf3de6aa672fc60a557aa32fc670281830201a300f401f50b5045efef742b2c4837a9a3b0e1d05a6917 

In diagnostic notation:

.. code-block:: 

  { 
    0: "1.0", % Version

    1:        % Security
    [ 
        1,     % defines the cipher suite 1 which contains only EC curves
        24(<<  % embedded CBOR data item
          { 
            1: 2, % kty:EC2 (Elliptic curves with x and y coordinate pairs)
          -1: 1, % crv:p256
  -2:h'5A88D182BCE5F42EFA59943F33359D2E8A968FF289D93E5FA444B624343  167FE',% x-coordinate
  -3:h'B16E8CF858DDC7690407BA61D4C338237A8CFCF3DE6AA672FC60A557AA32FC67' % y-coordinate
          }
        >>)
      ],
  
      2: %DeviceRetrievalMethods(Device engagement using QR code)
      [ 
        [
          2, %BLE
          1, % Version
        {    %BLE options
            0: false, % no support for mdoc peripheral server mode
            1: true, % support mdoc central client mode
            11: h'45EFEF742B2C4837A9A3B0E1D05A6917' % UUID of mdoc client central mode
          }
        ]
      ]
  }



**Step 4-6**: The Verifier App scans the QR Code and generates its own ephemeral key pair (EReaderKey.Priv, EReaderKey.Pub). It then calculates the session key, using the public key received in the Engagement Structure and its newly-generated private key, as outlined in [ISO18013-5#9.1.1.5]. Finally, it generates its session key, which must be independently derived by both the Wallet Instance and the Verifier App.

**Step 7**: The Verifier App creates an mDoc request that MUST be encrypted using the relevant session key, and transmits it to the Wallet Instance along with EReaderKey.Pub within a session establishment message. The mDoc request MUST be encoded in CBOR, as demonstrated in the following non-normative example.

CBOR data: 
.. code-block::

  a26776657273696f6e63312e306b646f63526571756573747381a26c6974656d7352657175657374d818590152a267646f6354797065756f72672e69736f2e31383031332e352e312e6d444c6a6e616d65537061636573a2746f72672e69736f2e31383031332e352e312e4954a375766572696669636174696f6e2e65766964656e6365f4781c766572696669636174696f6e2e6173737572616e63655f6c6576656cf4781c766572696669636174696f6e2e74727573745f6672616d65776f726bf4716f72672e69736f2e31383031332e352e31ab76756e5f64697374696e6775697368696e675f7369676ef47264726976696e675f70726976696c65676573f46f646f63756d656e745f6e756d626572f46a69737375655f64617465f46f69737375696e675f636f756e747279f47169737375696e675f617574686f72697479f46a62697274685f64617465f46b6578706972795f64617465f46a676976656e5f6e616d65f468706f727472616974f46b66616d696c795f6e616d65f46a726561646572417574688443a10126a11821590129308201253081cda00302010202012a300a06082a8648ce3d0403023020311e301c06035504030c15536f6d652052656164657220417574686f72697479301e170d3233313132343130323832325a170d3238313132323130323832325a301a3118301606035504030c0f536f6d6520526561646572204b65793059301306072a8648ce3d020106082a8648ce3d03010703420004aa1092fb59e26ddd182cfdbc85f1aa8217a4f0fae6a6a5536b57c5ef7be2fb6d0dfd319839e6c24d087cd26499ec4f87c8c766200ba4c6218c74de50cd1243b1300a06082a8648ce3d0403020347003044022048466e92226e042add073b8cdc43df5a19401e1d95ab226e142947e435af9db30220043af7a8e7d31646a424e02ea0c853ec9c293791f930bf589bee557370a4c97bf6584058a0d421a7e53b7db0412a196fea50ca6d4c8a530a47dd84d88588ab145374bd0ab2a724cf2ed2facf32c7184591c5969efd53f5aba63194105440bc1904e1b9

The above CBOR data is represented in diagnostic notation as follows:
.. code-block::

  {
    "version": "1.0",
    "docRequests": [
    {
      "itemsRequest": 24(<< {
        "docType": "org.iso.18013.5.1.mDL",
        "nameSpaces": {
          "org.iso.18013.5.1.IT": {
            "verification.evidence": false,
            "verification.assurance_level": false,
            "verification.trust_framework": false
          },
          "org.iso.18013.5.1": {
            "un_distinguishing_sign": false,
            "driving_privileges": false,
            "document_number": false,
            "issue_date": false,
            "issuing_country": false,
            "issuing_authority": false,
            "birth_date": false,
            "expiry_date": false,
            "given_name": false,
            "portrait": false,
            "family_name": false
          }
        }
      } >>),
      "readerAuth": [
        h'a10126',
        {
          33: h'308201253081cda00302010202012a300a06082a8648ce3d0403023020311e301c06035504030c15536f6d652052656164657220417574686f72697479301e170d3233313132343130323832325a170d3238313132323130323832325a301a3118301606035504030c0f536f6d6520526561646572204b65793059301306072a8648ce3d020106082a8648ce3d03010703420004aa1092fb59e26ddd182cfdbc85f1aa8217a4f0fae6a6a5536b57c5ef7be2fb6d0dfd319839e6c24d087cd26499ec4f87c8c766200ba4c6218c74de50cd1243b1300a06082a8648ce3d0403020347003044022048466e92226e042add073b8cdc43df5a19401e1d95ab226e142947e435af9db30220043af7a8e7d31646a424e02ea0c853ec9c293791f930bf589bee557370a4c97b'
        },
        null,
        h'58a0d421a7e53b7db0412a196fea50ca6d4c8a530a47dd84d88588ab145374bd0ab2a724cf2ed2facf32c7184591c5969efd53f5aba63194105440bc1904e1b9'
      ]
    }
    ]
  }

**Step 8**: The Wallet Instance uses the session establishment message to derive the session keys and decrypt the mDoc request. It computes the session key using the public key received from the Verifier App and its private key.

**Step 9-10**: When the Wallet Instance receives the mDoc request, it locates the documents that contain the requested attributes and asks the User for permission to provide this information to the Verifier. If the User agrees, the Wallet generates an mDoc response and transmits it to the Verifier App through the secure channel.

**Step 11-12**: If the User gives consent, the Wallet Instance creates an mDoc response and transmits it to the Verifier App via the secure channel. The mDoc response MUST be encoded in CBOR, with its structure outlined in [ISO18013-5#8.3.2.1.2.2]. Below is a non-normative example of an mDoc response.

CBOR Data:
.. code-block::

  a36776657273696f6e63312e3069646f63756d656e747381a367646f6354797065756f72672e69736f2e31383031332e352e312e6d444c6c6973737565725369676e6564a26a6e616d65537061636573a2746f72672e69736f2e31383031332e352e312e495483d81858f7a46864696765737449440b6672616e646f6d506d44f21ee875f2c1d502b43198e5a15271656c656d656e744964656e74696669657275766572696669636174696f6e2e65766964656e63656c656c656d656e7456616c756581a2647479706571656c656374726f6e69635f7265636f7264667265636f7264bf6474797065781f68747470733a2f2f657564692e77616c6c65742e70646e642e676f762e697466736f75726365bf716f7267616e697a6174696f6e5f6e616d65754d6f746f72697a7a617a696f6e6520436976696c656f6f7267616e697a6174696f6e5f6964656d5f696e666c636f756e7472795f636f6465626974ffffd8185866a4686469676573744944046672616e646f6d50185d84dfb71ce9b173010ddd62174fbe71656c656d656e744964656e746966696572781c766572696669636174696f6e2e74727573745f6672616d65776f726b6c656c656d656e7456616c7565656569646173d8185865a4686469676573744944006672616e646f6d50137f903174253c4585358267aae2ea4e71656c656d656e744964656e746966696572781c766572696669636174696f6e2e6173737572616e63655f6c6576656c6c656c656d656e7456616c75656468696768716f72672e69736f2e31383031332e352e318bd8185852a46864696765737449440c6672616e646f6d5053e29d0ddbbc7d2306a32bdbe2e56e5171656c656d656e744964656e7469666965726b66616d696c795f6e616d656c656c656d656e7456616c756563446f65d8185855a4686469676573744944036672616e646f6d50990cba2069fa1b33b8d6ae910b6549dc71656c656d656e744964656e7469666965726a676976656e5f6e616d656c656c656d656e7456616c756567416e746f6e696fd818585ba46864696765737449440a6672616e646f6d504086c1379975f805f1b1f4975e6a126571656c656d656e744964656e7469666965726a69737375655f646174656c656c656d656e7456616c7565d903ec6a323031392d31302d3230d818585ca4686469676573744944016672616e646f6d50ab4ca30c918dd2fd0bf35242c15fa2d871656c656d656e744964656e7469666965726b6578706972795f646174656c656c656d656e7456616c7565d903ec6a323032342d31302d3230d8185855a4686469676573744944076672616e646f6d508d9066f6c8da16619867cd4e2fab0c8871656c656d656e744964656e7469666965726f69737375696e675f636f756e7472796c656c656d656e7456616c7565624954d818587ea4686469676573744944056672616e646f6d5059fe68db795dee4c20976380ea24770571656c656d656e744964656e7469666965727169737375696e675f617574686f726974796c656c656d656e7456616c75657828497374697475746f20506f6c696772616669636f2065205a656363612064656c6c6f20537461746fd818585ba4686469676573744944026672616e646f6d5008b3f1ca5517019767be3dee3bb0614571656c656d656e744964656e7469666965726a62697274685f646174656c656c656d656e7456616c7565d903ec6a313935362d30312d3230d818585ca4686469676573744944096672616e646f6d50a2395ec214350c26066306e23279b3ae71656c656d656e744964656e7469666965726f646f63756d656e745f6e756d6265726c656c656d656e7456616c756569393837363534333231d8185850a4686469676573744944066672616e646f6d50a25e1a5b915d2d6eafee9674e023293971656c656d656e744964656e74696669657268706f7274726169746c656c656d656e7456616c75654420212223d81858eea46864696765737449440d6672616e646f6d50eeed6a3b856563627589a360939d12f771656c656d656e744964656e7469666965727264726976696e675f70726976696c656765736c656c656d656e7456616c756582a37576656869636c655f63617465676f72795f636f646561416a69737375655f64617465d903ec6a323031382d30382d30396b6578706972795f64617465d903ec6a323032342d31302d3230a37576656869636c655f63617465676f72795f636f646561426a69737375655f64617465d903ec6a323031372d30322d32336b6578706972795f64617465d903ec6a323032342d31302d3230d818585ba4686469676573744944086672616e646f6d50c0ef486b2a194ed3cbf7f354fd40092171656c656d656e744964656e74696669657276756e5f64697374696e6775697368696e675f7369676e6c656c656d656e7456616c756561496a697373756572417574688443a10126a118215901423082013e3081e5a00302010202012a300a06082a8648ce3d040302301a3118301606035504030c0f5374617465204f662055746f706961301e170d3233313132343134353430345a170d3238313132323134353430345a30383136303406035504030c2d5374617465204f662055746f7069612049737375696e6720417574686f72697479205369676e696e67204b65793059301306072a8648ce3d020106082a8648ce3d03010703420004c338ec1000b351ce8bcdfc167450aeceb

In diagnostic notation:
.. code-block::

  {
    "version": "1.0",
    "documents": [
    {
      "docType": "org.iso.18013.5.1.mDL",
      "issuerSigned": {
        "nameSpaces": {
          "org.iso.18013.5.1.IT": [
            24(<< {
              "digestID": 11,
              "random": h'6d44f21ee875f2c1d502b43198e5a152',
              "elementIdentifier": "verification.evidence",
              "elementValue": [
                {
                  "type": "electronic_record",
                  "record": {
                    "type": "https://eudi.wallet.pdnd.gov.it",
                    "source": {
                      "organization_name": "Motorizzazione Civile",
                      "organization_id": "m_inf",
                      "country_code": "it"
                    }
                  }
                }
              ]
            } >>),
            24(<< {
              "digestID": 4,
              "random": h'185d84dfb71ce9b173010ddd62174fbe',
              "elementIdentifier": "verification.trust_framework",
              "elementValue": "eidas"
            } >>),
            24(<< {
              "digestID": 0,
              "random": h'137f903174253c4585358267aae2ea4e',
              "elementIdentifier": "verification.assurance_level",
              "elementValue": "high"
            } >>)
          ],
          "org.iso.18013.5.1": [
            24(<< {
              "digestID": 12,
              "random": h'53e29d0ddbbc7d2306a32bdbe2e56e51',
              "elementIdentifier": "family_name",
              "elementValue": "Doe"
            } >>),
            24(<< {
              "digestID": 3,
              "random": h'990cba2069fa1b33b8d6ae910b6549dc',
              "elementIdentifier": "given_name",
              "elementValue": "Antonio"
            } >>),
            24(<< {
              "digestID": 10,
              "random": h'4086c1379975f805f1b1f4975e6a1265',
              "elementIdentifier": "issue_date",
              "elementValue": 1004("2019-10-20")
            } >>),
            24(<< {
              "digestID": 1,
              "random": h'ab4ca30c918dd2fd0bf35242c15fa2d8',
              "elementIdentifier": "expiry_date",
              "elementValue": 1004("2024-10-20")
            } >>),
            24(<< {
              "digestID": 7,
              "random": h'8d9066f6c8da16619867cd4e2fab0c88',
              "elementIdentifier": "issuing_country",
              "elementValue": "IT"
            } >>),
            24(<< {
              "digestID": 5,
              "random": h'59fe68db795dee4c20976380ea247705',
              "elementIdentifier": "issuing_authority",
              "elementValue": "Istituto Poligrafico e Zecca dello Stato"
            } >>),
            24(<< {
              "digestID": 2,
              "random": h'08b3f1ca5517019767be3dee3bb06145',
              "elementIdentifier": "birth_date",
              "elementValue": 1004("1956-01-20")
            } >>),
            24(<< {
              "digestID": 9,
              "random": h'a2395ec214350c26066306e23279b3ae',
              "elementIdentifier": "document_number",
              "elementValue": "987654321"
            } >>),
            24(<< {
              "digestID": 6,
              "random": h'a25e1a5b915d2d6eafee9674e0232939',
              "elementIdentifier": "portrait",
              "elementValue": h'20212223'
            } >>),
            24(<< {
              "digestID": 13,
              "random": h'eeed6a3b856563627589a360939d12f7',
              "elementIdentifier": "driving_privileges",
              "elementValue": [
                {
                  "vehicle_category_code": "A",
                  "issue_date": 1004("2018-08-09"),
                  "expiry_date": 1004("2024-10-20")
                },
                {
                  "vehicle_category_code": "B",
                  "issue_date": 1004("2017-02-23"),
                  "expiry_date": 1004("2024-10-20")
                }
              ]
            } >>),
            24(<< {
              "digestID": 8,
              "random": h'c0ef486b2a194ed3cbf7f354fd400921',
              "elementIdentifier": "un_distinguishing_sign",
              "elementValue": "I"
            } >>)
          ]
        },
        "issuerAuth": [
          h'a10126',
          {
            33: h'3082013e3081e5a00302010202012a300a06082a8648ce3d040302301a3118301606035504030c0f5374617465204f662055746f706961301e170d3233313132343134353430345a170d3238313132323134353430345a30383136303406035504030c2d5374617465204f662055746f7069612049737375696e6720417574686f72697479205369676e696e67204b65793059301306072a8648ce3d020106082a8648ce3d03010703420004c338ec1000b351ce8bcdfc167450aeceb7d518bd9a519583e082d67effff06565804fc09abf0e4a08e699c9dba3796285a15f68e40ac7f9fc7700a15153a4065300a06082a8648ce3d040302034800304502210099b7d62e6bf7b1823db3713df889bf73e70bb4d9c58c21e92c58d2f1beffe932022058d039747a00d70e6d66be4797e6142b3608a014ee09b7b79af2cae2aaf27788'
          },
          24(<< {
        "version": "1.0",
        "digestAlgorithm": "SHA-256",
        "docType": "org.iso.18013.5.1.mDL",
        "valueDigests": {
          "org.iso.18013.5.1": {
          1: h'0E5F0B6B33418E508740771E82F893372EAF5B2445BC4C84DCF08B005E9493FC',
          2: h'DE21BB62FF2897D8B986D2CDA9F9BC5865C02807F7B4D9DD1FA4A79DF4C0D37F',
          3: h'BC5568239E35CE9FF8798C27FFDCD757B134B679F0FE05729AA3491381912E65',
          5: h'E6048BDC7FD6454296F1E3F54536107C9C5B24C4064DE46A98121E3630EECCA2',
          6: h'73690D92DCAA61B0203870F67C6AA9FDFEA889B6F0C720DE757B4B0A8516A206',
          7: h'E353EA0B0FD92B6BE90C64CC3B2EE1284153A8F0F5066B99AAC599200E6EEEB2',
          8: h'29227872CEB49923D267B5F4BADE6D387B42AC2DC4B2AE26C9013067FEE7018A',
          9: h'A6A119F7CACAC0B8C6AACAC747FD3FE7E50B6D9BB8A507FDA79F0DF6646F285D',
          10: h'6D8025D2F02A5E7E1406FB6AAEB67F9EDE9B07191A53F3E23B77C528223A94E2',
          12: h'B0D43E4E2EA534E4D5304E64BCF7A0F13E2C8EE8304B9CD23ABA4909652A4647',
          13: h'FBF4DE318982F2DBAD43C601CAEB22628B301AC18AA8264C5831B2AAAC89C486'
          },
          "org.iso.18013.5.1.IT": {
          0: h'CF57377B675F64F37314739592C1E8A911A7DDAF341CE2902FE877C5A835E4C1',
          4: h'4A4B4CC64EC9299C1A2501EA449F577005E9F7A60408057C07A7C67FB151E5F5',
          11: h'78824FBD6FBBA88A2AAB44DF8B6F5E9759126D87D1F4415995E658FD9239E1FE'
          }
        },
        "deviceKeyInfo": {
          "deviceKey": {
          1: 2,
          -1: 1,
          -2: h'AFD09E720B918CEDC2B8A881950BAB6A1051E18AE16A814D51E609938663D5E1',
          -3: h'61FBC6C8AD24EC86A78BB4E9AC377DD2B7C711D9F2EB9AFD4AA0963662847AED'}},
          "validityInfo": {
            "signed": 0("2023-11-24T14:54:05Z"),
            "validFrom": 0("2023-11-24T14:54:05Z"),
            "validUntil": 0("2024-11-24T14:54:05Z")}
          }  >>),
          h'f2461e4fab69e9f7bcffe552395424514524d1679440036213173101448d1b1ab4a293859b389ffa8b47aeed10e9b0c1545412ac37c51a76482cd9bbbe110152'
        ]
      },
      "deviceSigned": {
        "nameSpaces": 24(<< {} >>),
        "deviceAuth": {
          "deviceSignature": [
            h'a10126',
            {},
            null,
            h'1fed7190d2975ab79c072e6f1d9d52436059d1fc959d55baf74f057d89b10fcc0dc77a50d433d4c76ddf26223c5560c4ab123b5cb5eb805a90036aa147493076'
          ]
        }
      }
    }
    ],
    "status": 0
  }

**Step 13**: The Verifier App is required to validate the signatures in the mDoc's issuerSigned field using the public key of the Credential Issuer specified within the mDoc. Subsequently, the Verifier MUST validate the signature in the deviceSigned field. If these signature checks pass, the Verifier can confidently consider the received information as valid.

Device Engagement
-----------------

The Device Engagement structure MUST be have at least the following components:

  - **Version**: *tstr*. Version of the data structure being used.
  - **Security**: an array that contains two mandatory values
  
    - the cipher identifier: see Table 22 of [ISO18013-5]
    - the mDL public ephemeral key generated by the Wallet Instance and required by the Verifier App to derive the Session Key. The mDL public ephemeral key MUST be of a type allowed by the indicated cipher suite.
  - **transferMethod**: an array that contains one or more transferMethod arrays when performing device engagement using the QR code. This array is for offline data retrieval methods. A transferMethod array holds two mandatory values (type and version). Only the BLE option is supported by this technical implementation profile, then the type value MUST be set to ``2``. 
  - **BleOptions**: this elements MUST provide options for the BLE connection (support for Peripheral Server or Central Client Mode, and the device UUID).


mDoc Request
------------

The messages in the mDoc Request MUST be encoded using CBOR. The resulting CBOR byte string for the mDoc Request MUST be encrypted with the Session Key obtained after the Device Engagement phase and MUST be transmitted using the BLE protocol.
The details on the structure of mDoc Request, including identifier and format of the data elements, are provided below. 

  - **version**: (tstr). Version of the data structure.
  - **docRequests**: Requested DocType, NameSpace and data elements.

    - **itemsRequest**: #6.24(bstr .cbor ItemsRequest).

      - **docType**: (tstr). The DocType element contains the type of document requested. See :ref:`Data Model Section <pid_eaa_data_model.rst>`.
      - **nameSpaces**: (tstr). See :ref:`Data Model Section <pid_eaa_data_model.rst>` for more details.

        - **dataElements**: (tstr). Requested data elements with *Intent to Retain* value for each requested element.

          - **IntentToRetain**: (bool). It indicates that the Verifier App intends to retain the received data element.
    - **readerAuth**: *COSE_Sign1*. It is required for the Verifier App authentication. 

.. note::
  
  The domestic data elements MUST not be returned unless specifically requested by the Verifier App.

mDoc Response
-------------

The messages in the mDoc Response MUST be encoded using CBOR and MUST be encrypted with the Session Key obtained after the Device Engagement phase.
The details on the structure of mDoc Response are provided below. 

  - **version**: (tstr). Version of the data structure.
  - **documents**: Returned *DocType*, and *ResponseData*.

    - **docType**: (tstr). The DocType element contains the type of document returned. See :ref:`Data Model Section <pid_eaa_data_model.rst>`.
    - **ResponseData**:

      - **IssuerSigned**: Responded data elements signed by the issuer.

        - **nameSpaces**: (tstr). See :ref:`Data Model Section <pid_eaa_data_model.rst>` for more details.

          - **IssuerSignedItemBytes**: #6.24(bstr .cbor). 

            - **digestID**: (uint).  Reference value to one of the **ValueDigests** provided in the *Mobile Security Object* (`issuerAuth`).
            - **random**: (bstr). Random byte value used as salt for the hash function. This value SHALL be different for each *IssuerSignedItem* and it SHALL have a minimum length of 16 bytes.
            - **elementIdentifier**: (tstr). Identifier of User attribute name contained in the Credential.
            - **elementValue**: (any). User attribute value
      - **DeviceSigned**: Responded data elements signed by the Wallet Instance.

        - **NameSpaces**: #6.24(bstr .cbor DeviceNameSpaces). The DeviceNameSpaces structure MAY be an empty structure. DeviceNameSpaces contains the data element identifiers and values. It is returned as part of the corresponding namespace in DeviceNameSpace.

          - **DataItemName**: (tstr). The identifier of the element.
          - **DataItemValue**: (any). The value of the element.
        - **DeviceAuth**:  The DeviceAuth structure MUST contain the DeviceSignature elements.

          - **DeviceSignature**: It MUST contain the device signature for the Wallet Instance authentication. 
  - **status**: It contains a status code. For detailed description and action required refer to to Table 8 (ResponseStatus) of the [ISO18013-5]


Session Termination
-------------------

The session MUST be terminated if at least one of the following conditions occur. 

  - After a time-out of no activity of receiving or sending session establishment or session data messages occurs. The time-out for no activity implemented by the Wallet Instance and the Verifier App SHOULD be no less than 300 seconds.
  - When the Wallet Instance doesn't accept any more requests.
  - When the Verifier App does not send any further requests. 

If the Wallet Instance and the Verifier App does not send or receive any further requests, the session termination MUST be initiated as follows. 

 - Send the status code for session termination, or
 - dispatch the "End" command as outlined in [ISO18013-5#8.3.3.1.1.5].

When a session is terminated, the Wallet Instance and the Verifier App MUST perform at least the following actions: 

  - destruction of session keys and related ephemeral key material; 
  - closure of the communication channel used for data retrieval.
