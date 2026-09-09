.. include:: ../common/common_definitions.rst
.. Incluso tramite entities.rst al livello di titolo '-' (livello 1).

Soluzione Wallet
----------------

La Wallet Solution è emessa dal Fornitore di Wallet sotto forma di applicazione mobile e servizi, come interfacce web. L'applicazione mobile funge da interfaccia principale per gli Utenti, consentendo loro di conservare i propri Attestati Elettronici e di interagire con altri partecipanti dell'ecosistema, come i Fornitori di Attributi Elettronici e le Relying Party. Questi Attestati Elettronici costituiscono un insieme di dati che possono identificare in modo univoco una persona fisica o giuridica, insieme ad altre Attestazioni Elettroniche Qualificate e non Qualificate di Attributi, note rispettivamente come QEAAs ed EAAs, o più brevemente (Q)EAAs. Una volta che un utente installa l'applicazione mobile sul proprio dispositivo, tale installazione viene definita come istanza del Wallet per quell'utente. Supportando l'applicazione mobile, il Fornitore di Wallet garantisce la sicurezza e l'affidabilità dell'intera Wallet Solution, poiché è responsabile dell'emissione della Wallet Instance Attestation (WIA) e della Key Attestation (KA). La WIA dimostra l'autenticità e l'integrità dell'istanza del Wallet, mentre la KA fornisce la prova che le chiavi utilizzate per il collegamento crittografico delle credenziali sono archiviate in modo sicuro: il Keystore per le Credenziali Digitali standard; il WSCA operante in un Remote WSCD (HSM remoto) per il PID a LoA High. Inoltre, la KA conferma che la Wallet Unit non è stata revocata.

Il seguente diagramma illustra l'Architettura di Alto Livello della Soluzione Wallet.

.. _fig_wallet-solution-high-level-architecture:
.. plantuml:: plantuml/wallet-solution-architecture.puml
    :width: 99%
    :alt: L'immagine illustra la Soluzione Wallet e le sue relazioni e interazioni all'interno dell'ecosistema.
    :caption: `Architettura di Alto Livello della Soluzione Wallet. <https://www.plantuml.com/plantuml/svg/nLVHRzks4txtNy6V-yEM0ixSr4xX0cjHnsun0orgr6dtAD3aMI8YaHf9nV66_UyZAIgKHSTLzx8y9F7nxhkFnxkFz3kbiTHLaG_-npZ9AmheryLql9Wc2r6KWWFNRmU3dz4ITem3sgo_h6xVRrhEkYenbPCn4KKX-DiJApl1zINUWn85N5wF2KZDTenW3JsySq7kUhXL2gJgaroaVTmCsZt87ewC9WHBsiCJ7aY6UGe9pdKFTmhgJekoXsSXjYp_RYd7Z2lDTAMPuEv05vNIea1A7t9GWpcbxtCeWEjRd5uCuK63v3WVZj3_j-b2v4A-6JvxxNwipI9xwpvZ6foVa1IajwOI3iFdNTXIiWBBmp7grTMhsPRsGdtsOZkTpQOni08YE8sWNv7jPBBh1pt5iydBrp6qbfNInx2p-UJrx4C_sElhbvFhkO4DCwGpG9Xe8HN2dAAcraWTb8P23TOWbU0NjgL7QFZL_36mmzgACf5JnbEqP2dJ9cWXWGBN3EVA9bUcn1hU3DqycAmRXvcyVz0NRYC9vYGJ5lVMVaHpzz7YVn528x53sjbtGZgUgzlBtt6UWqOVW8B4jdri7erJzQRL9Y5pQxoFyvD7fWbJgWAfJDP07wrge-LoFeEVkMDq2Vd1r2KfiKaFocwejg2ri_J13HDoZ4qLCy5Bk6V4L8HhI4t00Mr0MiiF0KUDuAkx4RbRHrjHkKOUtFX_BlRE8r7UmsGBCHuJ_NKQTIt5FQCWqGqcTy3fq-ZRsY60TqFh98ztmiM-J7PIS5q7VV3_eaU7eOM2BL9raUfMjxsCcZ3huREOLKgPtGlEGuJEfAZI365aWLmiCv5oXmcW2zkXy82BCWUqoSHUZR-1D8q7Qlm9Svo2QggmuafZRX2VXsFoIjG-9Q-uveJ2BalAQG8D8qDulbuPF4zYw0rmsNWuIwKp8TcVG17rGngAGCnlPRgokGviWrAiyI-1Mj2o5hdsxN74SC-IdEs074WE9dbdo-XZiuRgeXJ-Q5gz-nlcD8-hXIIaJ6c9wwOpHbsfaJj62VU2TAJ0osHWR6_QDbElFmf8PQVdKO5-GXjlyiqJCspEymuEXa5BO3oV1XCLWZCjf2dg6MBsHM68_NrwPBuQXAV7f3AhlihUryr5vCTy4UCJSVwXA1LBV7DugG_TTRPPwql_gBwrgBRWQa4zhkhd4lXgEVssM3dDXpygK5gTkasG5YXMv_Dj6XzwAK6PlwvPMjJMBVDfWkiHMcq-NyrUN4qkhuSXv4ckaTp_654hW5NPedZZ3BQ_3BJIGa8W-gFW5AjiAx2aBVnbO_ltiFlGFF_5v7zlzCs8TSXg8N5goRgH1xIf3PrROxEOZv3vlHoXJr08UUXgWAD2ml7t6VPetYNaRYCgOwKQ34px-1TN-sPpCsdtOfQJZnsnZIu7DxgOQ8NsJ6SXAW3s2RfXbalNhttMKGnocRvs-4M2Q_VYNdP47aejKedBZ14aIl-mynljm535VEoJvAAdtScDXH9tLSzrYyVkobWVx11zMc_Yns4Cu4iOg9slUMY9u1DNwcWv4kXOoPpCsXay2T3Ut7cOjhwUX3edTzBBNOnxUb-nkZNZYhJ4N67YP5u24PA6OOgkog0G_NeL3GRDiSMFvCwt7V_jnRz3nLPZa_T8wDhl2lj6BGpHTy1fLUJ_0000>`_


.. toctree::
  :caption: Indice dei Contenuti della Soluzione Wallet
  :maxdepth: 2

  wallet-solution-requirements.rst
  wallet-solution-components.rst
  wallet-instance.rst
  backup-restore.rst
  wallet-provider-entity-configuration.rst
  wallet-solution-metadata.rst


