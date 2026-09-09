.. include:: ../common/common_definitions.rst
.. Incluso tramite wallet-solution.rst al livello di titolo '^' (livello 2).

Istanza del Wallet
^^^^^^^^^^^^^^^^^^

L'Istanza del Wallet stabilisce un meccanismo forte e affidabile per garantire all'Utente transazioni digitali in modo sicuro e rispettoso della privacy.

L'Istanza del Wallet stabilisce un rapporto di fiducia con i Fornitori di PID e (Q)EAA presentando le Wallet Instance Attestation e Key Attestation durante le interazioni.
Queste attestazioni verificabili, fornite dal Fornitore di Wallet, servono ad autenticare la stessa Istanza del Wallet, assicurando l'affidabilità dell'ambiente di archiviazione sicuro: il **Keystore** per tutte le Credenziali Digitali device-bound, e il **WSCA** operante in un **Remote WSCD** (HSM remoto) esclusivamente per il PID a LoA High. Le attestazioni verificano inoltre che l'Istanza del Wallet non sia stata revocata e ne assicurano l'affidabilità nelle interazioni con gli altri attori dell'ecosistema.


.. toctree::
  :caption: Indice dei Contenuti dell'Istanza del Wallet
  :maxdepth: 3

  wallet-instance-lifecycle.rst
  wallet-instance-functionalities.rst


