.. include:: ../common/common_definitions.rst
.. Included via entities.rst at title level '-' (level 1).

Wallet Solution
---------------

The Wallet Solution is issued by the Wallet Provider in the form of a mobile app and services, such as web interfaces. The mobile app serves as the primary interface for Users, allowing them to hold their Digital Credentials and interact with other participants of the ecosystem, such as Credential Issuers and Relying Parties. These Digital Credentials are a set of data that can uniquely identify a natural or legal person, along with other Qualified and non-qualified Electronic Attestations of Attributes, also known as QEAAs and EAAs respectively, or (Q)EAAs for short. Once a User installs the mobile app on their device, such an installation is referred to as a Wallet Instance for the User. By supporting the mobile app, the Wallet Provider ensures the security and reliability of the entire Wallet Solution, as it is responsible for issuing the Wallet Instance Attestation (WIA) and Key Attestation (KA). WIA proves the authenticity and integrity of the Wallet Instance, while KA provides evidence that the keys used for Credential key binding are securely stored in a trustworthy hardware-backed environment (Keystore for standard Digital Credentials; WSCA operating within a Remote WSCD / remote HSM for the PID at Level of Assurance High). Additionally, KA confirms that the Wallet Unit has not been revoked.

The following diagram depicts the Wallet Solution High Level Architecture.

.. _fig_wallet-solution-high-level-architecture:
.. plantuml:: plantuml/wallet-solution-architecture.puml
    :width: 99%
    :alt: The image illustrates the Wallet Solution and its relations and interactions within the ecosystem.
    :caption: `Wallet Solution High Level Architecture. <https://www.plantuml.com/plantuml/svg/nLVHRzks4txtNy6V-yEM0ixSr4xX0cjHnsun0orgr6dtAD3aMI8YaHf9nV66_UyZAIgKHSTLzx8y9F7nxhkFnxkFz3kbiTHLaG_-npZ9AmheryLql9Wc2r6KWWFNRmU3dz4ITem3sgo_h6xVRrhEkYenbPCn4KKX-DiJApl1zINUWn85N5wF2KZDTenW3JsySq7kUhXL2gJgaroaVTmCsZt87ewC9WHBsiCJ7aY6UGe9pdKFTmhgJekoXsSXjYp_RYd7Z2lDTAMPuEv05vNIea1A7t9GWpcbxtCeWEjRd5uCuK63v3WVZj3_j-b2v4A-6JvxxNwipI9xwpvZ6foVa1IajwOI3iFdNTXIiWBBmp7grTMhsPRsGdtsOZkTpQOni08YE8sWNv7jPBBh1pt5iydBrp6qbfNInx2p-UJrx4C_sElhbvFhkO4DCwGpG9Xe8HN2dAAcraWTb8P23TOWbU0NjgL7QFZL_36mmzgACf5JnbEqP2dJ9cWXWGBN3EVA9bUcn1hU3DqycAmRXvcyVz0NRYC9vYGJ5lVMVaHpzz7YVn528x53sjbtGZgUgzlBtt6UWqOVW8B4jdri7erJzQRL9Y5pQxoFyvD7fWbJgWAfJDP07wrge-LoFeEVkMDq2Vd1r2KfiKaFocwejg2ri_J13HDoZ4qLCy5Bk6V4L8HhI4t00Mr0MiiF0KUDuAkx4RbRHrjHkKOUtFX_BlRE8r7UmsGBCHuJ_NKQTIt5FQCWqGqcTy3fq-ZRsY60TqFh98ztmiM-J7PIS5q7VV3_eaU7eOM2BL9raUfMjxsCcZ3huREOLKgPtGlEGuJEfAZI365aWLmiCv5oXmcW2zkXy82BCWUqoSHUZR-1D8q7Qlm9Svo2QggmuafZRX2VXsFoIjG-9Q-uveJ2BalAQG8D8qDulbuPF4zYw0rmsNWuIwKp8TcVG17rGngAGCnlPRgokGviWrAiyI-1Mj2o5hdsxN74SC-IdEs074WE9dbdo-XZiuRgeXJ-Q5gz-nlcD8-hXIIaJ6c9wwOpHbsfaJj62VU2TAJ0osHWR6_QDbElFmf8PQVdKO5-GXjlyiqJCspEymuEXa5BO3oV1XCLWZCjf2dg6MBsHM68_NrwPBuQXAV7f3AhlihUryr5vCTy4UCJSVwXA1LBV7DugG_TTRPPwql_gBwrgBRWQa4zhkhd4lXgEVssM3dDXpygK5gTkasG5YXMv_Dj6XzwAK6PlwvPMjJMBVDfWkiHMcq-NyrUN4qkhuSXv4ckaTp_654hW5NPedZZ3BQ_3BJIGa8W-gFW5AjiAx2aBVnbO_ltiFlGFF_5v7zlzCs8TSXg8N5goRgH1xIf3PrROxEOZv3vlHoXJr08UUXgWAD2ml7t6VPetYNaRYCgOwKQ34px-1TN-sPpCsdtOfQJZnsnZIu7DxgOQ8NsJ6SXAW3s2RfXbalNhttMKGnocRvs-4M2Q_VYNdP47aejKedBZ14aIl-mynljm535VEoJvAAdtScDXH9tLSzrYyVkobWVx11zMc_Yns4Cu4iOg9slUMY9u1DNwcWv4kXOoPpCsXay2T3Ut7cOjhwUX3edTzBBNOnxUb-nkZNZYhJ4N67YP5u24PA6OOgkog0G_NeL3GRDiSMFvCwt7V_jnRz3nLPZa_T8wDhl2lj6BGpHTy1fLUJ_0000>`_


.. toctree::
  :caption: Wallet Solution Table of Contents
  :maxdepth: 2

  wallet-solution-requirements.rst
  wallet-solution-components.rst
  wallet-instance.rst
  backup-restore.rst
  wallet-provider-entity-configuration.rst
  wallet-solution-metadata.rst


