.. include:: ../common/common_definitions.rst


Componenti della Soluzione Wallet
=================================

.. note::
   I test relativi ai componenti della Wallet Solution (Backend del Wallet e Unità di Wallet) sono riassunti in :ref:`WP_012 <wallet-provider-backend-testcases>` e in :ref:`WP_013 <wallet-instance-testcases>`, rispettivamente.

Backend del Wallet
------------------

Componente Frontend
^^^^^^^^^^^^^^^^^^^

Il Componente Frontend DEVE fornire un'interfaccia Utente basata sul web per la gestione dell'Istanza del Wallet, offrendo funzionalità per:

- Visualizzare e verificare le Istanze del Wallet e il loro stato.
- Gestire il ciclo di vita dell'Istanza del Wallet (ad esempio, revoca).
- Fornire supporto e documentazione all'Utente.

Interfaccia API
^^^^^^^^^^^^^^^

Questo componente DEVE:

- inoltrare la richiesta dal Componente Frontend o dall'Istanza del Wallet al componente di Gestione del Ciclo di Vita dell'Istanza del Wallet.
- utilizzare PDND secondo le regole nella Sezione :ref:`e-service-pdnd:e-Service PDND` per essere notificato dal Provider di PID/IT-Wallet ID della necessità di revocare l'Istanza del Wallet e cancellare l'account dell'Utente a causa del decesso dell'Utente.

Gestione del Ciclo di Vita dell'Istanza del Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo componente DEVE gestire:

- Registrazione dell'Istanza del Wallet (dettagliata in :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet`).
- Emissione della Wallet Instance Attestation (dettagliata in :ref:`wallet-instance-attestation-issuance:Emissione della Wallet Instance Attestation`).
- Emissione della Key Attestation (dettagliata in :ref:`wallet-attestation-issuance:Emissione della Key Attestation`).
- Gestione dello stato (mantenimento e aggiornamento della validità).
- Processi di revoca (implementazione di meccanismi per revocare le Istanze del Wallet), secondo la Sezione :ref:`wallet-instance-revocation:Revoca dell'Istanza del Wallet`.

Componente Trust & Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo componente DEVE garantire la sicurezza attraverso:

- Gestione di chiavi e certificati.
- Registrazione degli audit.
- Monitoraggio della sicurezza e risposta agli incidenti.
- Conformità ai requisiti di sicurezza della Federazione IT-Wallet.


Unità di Wallet
---------------

Interfaccia Utente
^^^^^^^^^^^^^^^^^^

L'Interfaccia Utente è il punto di interazione e comunicazione tra l'Utente e l'Istanza del Wallet.

Componente di Gestione del Ciclo di Vita dell'Istanza del Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Interagendo con il Backend del Wallet, questo componente DEVE gestire:

- Registrazione dell'Istanza del Wallet (dettagliata in :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet`).
- Emissione della Wallet Instance Attestation (dettagliata in :ref:`wallet-instance-attestation-issuance:Emissione della Wallet Instance Attestation`).
- Emissione della Key Attestation (dettagliata in :ref:`wallet-attestation-issuance:Emissione della Key Attestation`).
- Gestione dello stato (mantenimento e aggiornamento della validità).
- Processi di revoca (implementazione di meccanismi per revocare le Istanze del Wallet), secondo la Sezione :ref:`wallet-instance-revocation:Revoca dell'Istanza del Wallet`.

In base allo stato dell'Istanza del Wallet e alla richiesta dell'Utente, questo componente interagisce con gli altri componenti dell'Istanza del Wallet.

Componente Issuer
^^^^^^^^^^^^^^^^^

Seguendo la specifica `OpenID4VCI`_ e il profilo di implementazione nella Sezione :ref:`credential-issuance:Emissione di Attestati Elettronici`, questo componente DEVE implementare i protocolli e i flussi di emissione delle Credenziali Elettroniche per richiedere Credenziali Elettroniche ai Credential Issuer.

Componente di Presentazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Seguendo il profilo di implementazione nella Sezione :ref:`credential-presentation:Presentazione dell'Attestato Elettronico`, questo componente DEVE essere conforme ai flussi remoti basati su `OpenID4VP`_ e ai flussi di prossimità basati su `ISO18013-5`_.

Componente di Backup e Ripristino
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per ogni Credenziale Elettronica emessa all'Istanza del Wallet, questo componente DEVE aggiungere tutti i dati necessari per richiedere l'emissione di quella Credenziale Elettronica durante il ripristino come specificato nella Sezione :ref:`backup-restore:Backup e Ripristino`.

.. note::
   Attualmente la riemissione del PID e dell'IT-Wallet ID non è gestita dal Componente di Backup e Ripristino.

Dashboard e Registro delle Transazioni
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Questo componente DEVE fornire le funzionalità di dashboard e di registro delle transazioni della Wallet Unit. In particolare, questo componente DEVE:

- fornire un’interfaccia accessibile all’Utente che consenta all’Utente di accedere alle informazioni di trasparenza delle transazioni;
- mantenere un registro delle transazioni eseguite tramite la Wallet Unit, incluse le transazioni non completate;
- supportare l’interazione dell’Utente con i record di transazione, inclusa la visualizzazione, l’esportazione e la cancellazione.

Keystore
^^^^^^^^

L'Istanza del Wallet DEVE utilizzare questo componente per generare, archiviare e utilizzare in modo sicuro le chiavi crittografiche per tutte le Credenziali Digitali. Il Keystore si basa sull'ambiente crittografico hardware-backed fornito dall'OEM del dispositivo (Strongbox o TEE su Android; Secure Enclave su iOS) ed è attestato tramite le OEM Key Attestation APIs. Il Keystore è il meccanismo di archiviazione sicura di default per tutte le operazioni della Wallet Instance e per tutte le Credenziali Digitali.


WSCA/WSCD Interface
^^^^^^^^^^^^^^^^^^^

Per l'emissione e la gestione del PID a Livello di Garanzia Alto, l'Istanza del Wallet DEVE interagire con un **WSCA operante in un Remote WSCD** implementato come Hardware Security Module (HSM) remoto operato lato server. Questo componente fornisce l'interfaccia verso il WSCA e il Remote WSCD, e garantisce che le chiavi private del PID siano generate e gestite in un ambiente hardware remoto antimanomissione conforme ai requisiti per il Livello di Garanzia Alto. La WSCA/WSCD Interface è utilizzata esclusivamente per il PID.

L'attestazione delle chiavi nel contesto del Remote WSCD è eseguita dal Wallet Provider: dopo che il WSCA genera la coppia di chiavi del PID all'interno del Remote WSCD (HSM remoto), il Wallet Provider attesta le proprietà del WSCA e del Remote WSCD ed emette un Key Attestation (KA) che viene presentato al PID Provider durante l'emissione del PID. Il KA per il Remote WSCD descrive le proprietà di sicurezza dell'HSM remoto (anziché dell'hardware OEM del dispositivo), fornendo il livello di certificazione superiore richiesto per il Livello di Garanzia Alto.


Modelli di Interazione della Soluzione Wallet
=============================================

La Soluzione Wallet supporta questi modelli di interazione:

1. **Utente verso Frontend del Backend del Wallet**: Interazioni basate sul web per la gestione dell'Istanza del Wallet.
2. **Istanza del Wallet verso API del Backend del Wallet**: per la registrazione dell'Istanza del Wallet e l'emissione della Wallet Instance e key Attestation.
3. **Provider di PID/IT-Wallet ID verso API del Backend del Wallet**: Chiamate API sicure per richiedere la revoca dell'Istanza del Wallet.
4. **Utente verso Interfaccia Utente dell'Istanza del Wallet**: per la gestione delle Credenziali Elettroniche (emissione, presentazione, backup, ripristino, eliminazione).
5. **Istanza del Wallet verso Relying Party**: per la presentazione delle Credenziali Elettroniche.


