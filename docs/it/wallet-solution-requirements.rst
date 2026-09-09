.. include:: ../common/common_definitions.rst
.. Incluso tramite wallet-solution.rst al livello di titolo '^' (livello 2).

Requisiti della Soluzione Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione elenca i requisiti relativi ai Fornitori di Wallet e alle Soluzioni Wallet con le loro Istanze del Wallet, nonché i corrispondenti Wallet Instance Attestation, Key Attestation e i componenti di archiviazione sicura: il **Keystore** (usato per tutte le Credenziali Digitali) e il **WSCA/Remote WSCD** (usato esclusivamente per il PID a Livello di Garanzia Alto).

- La Soluzione Wallet DEVE aderire alle specifiche stabilite da questo documento per ottenere Attestati Elettronici di Dati di Identificazione Personale (PID) e Attestati Elettronici di Attributi (Q)EAA.
- Il Fornitore di Wallet DEVE esporre un insieme di endpoint, disponibili esclusivamente per le istanze della sua Soluzione Wallet, che supportano le funzionalità principali delle Istanze del Wallet.
- L'Istanza del Wallet DEVE periodicamente ristabilire la trust con il suo Fornitore di Wallet, ottenendo una nuova Wallet Instance Attestation (:ref:`WP_018 <wallet-instance-testcases>`).
- L'istanza del Wallet DEVE stabilire un rapporto di fiducia con gli altri partecipanti dell'ecosistema del Wallet, come i Fornitori di Attributi Elettronici. Nel caso dei Fornitori di Attributi Elettronici, l'istanza del Wallet presenta sia la Wallet Instance Attestation che la Key Attestation.
- L'Istanza del Wallet DEVE essere compatibile e funzionale sia sui sistemi operativi Android che iOS e disponibile rispettivamente sul Play Store e sull'App Store (:ref:`WP_015 <wallet-instance-testcases>`).
- L'Istanza del Wallet DEVE fornire un meccanismo per verificare l'effettivo possesso e il pieno controllo da parte dell'Utente del proprio dispositivo personale.
- L'Istanza del Wallet DEVE fornire agli Utenti un elenco aggiornato delle Relying Party con cui l'Utente ha stabilito una connessione e, ove applicabile, tutti i dati scambiati;
- L'Istanza del Wallet DEVE fornire agli Utenti un meccanismo per richiedere la cancellazione degli attributi personali da parte di una Relying Party ai sensi dell'articolo 17 del Regolamento (UE) 2016/679, e per registrare ogni Richiesta di Cancellazione effettuata.

.. note::
   Non esiste una corrispondenza stretta uno-a-uno tra i requisiti in questa sezione e i casi di test in :ref:`test-plans-wallet-provider:Matrice di Test per Wallet Provider`. Alcuni requisiti sono espressi a un livello troppo alto per poter essere rappresentati come casi di test atomici, mentre altri sono già affrontati in modo più dettagliato all'interno dei flussi correlati (ad es. :ref:`wallet-instance-attestation-issuance:Emissione della Wallet Instance Attestation`).

Requisiti della Wallet Instance Attestation
"""""""""""""""""""""""""""""""""""""""""""

la Wallet Instance Attestation contiene informazioni riguardanti il livello di sicurezza del dispositivo che ospita l'Istanza del Wallet.
Esso dimostra principalmente l'**autenticità**, l'**integrità**, la **sicurezza** e in generale l'**affidabilità** di una particolare Istanza del Wallet.

I requisiti per la Wallet Instance Attestation sono definiti di seguito:

- la Wallet Instance Attestation DEVE fornire tutte le informazioni rilevanti per attestare l'**integrità** e la **sicurezza** del dispositivo in cui è installata l'Istanza del Wallet (:ref:`WP_019 <wallet-instance-testcases>`).
- la Wallet Instance Attestation DEVE essere firmato dal Fornitore di Wallet che ha autorità e proprietà sulla Soluzione Wallet, come specificato dalla Registration Authority di supervisione. Questo garantisce che la Wallet Instance Attestation colleghi in modo univoco il Fornitore di Wallet a questa particolare Istanza del Wallet (:ref:`WP_020 <wallet-instance-testcases>`).
- Il Fornitore di Wallet DEVE periodicamente valutare e garantire l'integrità, l'autenticità e la genuinità dell'Istanza del Wallet. Il Fornitore di Wallet verifica l'Istanza del Wallet utilizzando il flusso più sicuro reso disponibile dalle API del Fornitore del Sistema Operativo, come la *Play Integrity API* per Android e *App Attest* per iOS (:ref:`WP_011 <wallet-provider-backend-testcases>`).
- la Wallet Instance Attestation DEVE essere vincolato in modo sicuro alla chiave pubblica effimera dell'Istanza del Wallet (:ref:`WP_019b <wallet-instance-testcases>`).
- la Wallet Instance Attestation PUÒ essere utilizzato più volte durante il suo periodo di validità, consentendo autenticazioni e autorizzazioni ripetute senza la necessità di richiedere nuovi attestati ad ogni interazione. Tuttavia, è RACCOMANDATO che le Istanze del Wallet evitino di utilizzare ripetutamente lo stesso attestato, a causa di preoccupazioni sulla privacy come la possibilità di collegamento tra diverse interazioni.
- La Wallet Instance Attestation DEVE avere una durata limitata e DEVE includere un tempo di scadenza, oltre il quale NON DEVE più essere considerata valida.
- la Wallet Instance Attestation NON DEVE essere rilasciato dal Fornitore di Wallet se l'autenticità, l'integrità e la genuinità dell'Istanza del Wallet che lo richiede non possono essere garantite (:ref:`WP_019a <wallet-instance-testcases>`).
- Ogni Istanza del Wallet DOVREBBE essere in grado di richiedere più Wallet Instance Attestation utilizzando diverse chiavi pubbliche crittografiche associate ad essi.
- la Wallet Instance Attestation NON DEVE contenere informazioni sull'Utente che controlla l'Istanza del Wallet (:ref:`WP_029b <wallet-instance-testcases>`).
- L'Istanza del Wallet DEVE ottenere una Wallet Instance Attestation come prerequisito per passare allo stato Operativo, come definito da `EIDAS-ARF`_.
- Un Wallet Provider DEVE garantire che una Wallet Unit non revocata presenti in ogni momento una Wallet Instance Attestation temporalmente valida e non revocata a un PID Provider o a un Attestation Provider durante il processo di emissione di un PID o di un'attestazione. Nota: questo requisito si applica sia alle attestazioni associate a un dispositivo che a quelle non associate a un dispositivo, come definito da `EIDAS-ARF`_.
- Una Wallet Unit DEVE presentare una Wallet Instance Attestation esclusivamente a un PID Provider o a un Attestation Provider, nell'ambito del processo di emissione di un PID o di un'attestazione, e non a una Relying Party o a qualsiasi altra entità.

.. note::
  In questa sezione, i servizi utilizzati per attestare la genuinità dell'Istanza del Wallet e del dispositivo in cui è installata sono indicati come **API del Servizio di Integrità del Dispositivo**. L'API del Servizio di Integrità del Dispositivo è considerata in modo astratto e si presume sia un servizio fornito da una terza parte affidabile (cioè, l'API del Fornitore del Sistema Operativo) in grado di eseguire controlli di integrità sull'Istanza del Wallet e sul dispositivo in cui è installata.


Requisiti della Key Attestation
""""""""""""""""""""""""""""""""""""""""

La Key Attestation contiene informazioni che garantiscono che le chiavi utilizzate per il key binding delle Credenziali Digitali siano generate e archiviate in modo sicuro in un ambiente hardware affidabile: un **Keystore** per le Credenziali Digitali device-bound standard, oppure un **WSCA** operante in un **Remote WSCD** (HSM remoto) esclusivamente per il PID a Livello di Garanzia Alto. Inoltre, fornisce un metodo per autenticare il componente di archiviazione sicura presso il Credential Issuer e verifica che la Wallet Unit non sia stata revocata.

I requisiti per la Key Attestation sono definiti di seguito:

- La Key Attestation DEVE fornire al PID Provider o all'Attestation Provider informazioni sulle proprietà del Keystore o del WSCA/Remote WSCD della Wallet Unit, in modo che possano prendere una decisione ben fondata sull'opportunità di emettere un PID o un'attestazione per tale Wallet Unit.
- La Key Attestation DEVE consentire ai PID Provider e agli Attestation Provider di verificare l'autenticità e lo stato di revoca della Wallet Unit.
- Un Wallet Provider DEVE garantire che una Wallet Unit non revocata possa in ogni momento presentare una Key Attestation, quando richiesto da un PID Provider o da un Attestation Provider.
- Durante l'emissione di un PID, la Wallet Unit DEVE fornire al PID Provider una Key Attestation (KA) valida che descriva il WSCA e il Remote WSCD che ha generato la nuova chiave privata del PID. Nota: una chiave privata del PID è sempre generata e gestita dal WSCA operante nel Remote WSCD (HSM remoto), che per definizione è conforme ai requisiti per il Livello di Garanzia Alto.
- Durante l'emissione di un'attestazione device-bound diversa dal PID, la Wallet Unit DEVE fornire all'Attestation Provider una Key Attestation (KA) valida che descriva il Keystore in cui è stata generata e archiviata la nuova chiave privata della credenziale. La Wallet Unit DEVE recuperare dai metadati dell'Emittente (come specificato in `OpenID4VCI`_) i requisiti dell'Attestation Provider riguardanti l'archiviazione delle chiavi, e DEVE determinare quale dei propri Keystore, se presente, soddisfi tali requisiti. Nota: una KA per un'attestazione device-bound descrive le proprietà del Keystore come attestate dalle OEM Key Attestation APIs, e contiene una o più chiavi pubbliche corrispondenti a chiavi private generate e archiviate in tale Keystore.
- Se una Wallet Unit contiene più Keystore o WSCA, essa DEVE, in modo interno e sicuro, tenere traccia di quali PID e attestazioni sono associati a ciascun Keystore o WSCA.
- Una Wallet Unit DEVE presentare una Key Attestation solo come parte del processo di emissione di un PID o di un'attestazione.
- La Key Attestation DEVE consentire ai PID Provider di richiedere a un Wallet Provider la revoca di una Wallet Unit, includendo un identificatore per la Wallet Unit all'interno della KA (ad esempio, un URI e un indice a una Attestation Status List). Il Wallet Provider DEVE garantire che tale identificatore della Wallet Unit non consenta il tracciamento dell'utente.
- La Key Attestation DEVE contenere una o più chiavi pubbliche di credenziali attestate associate allo stesso Keystore o WSCA/Remote WSCD.
- La Key Attestation DEVE essere firmata dal Wallet Provider che ha autorità e proprietà sulla Wallet Solution, come specificato dall'Autorità di Registrazione di riferimento. I Wallet Provider DEVONO garantire che i certificati utilizzati per firmare le KA e le WIA siano conformi a tutti i requisiti applicabili della `ETSI TS 119 412-6`_, in particolare alla Clausola 5.
- Un Attestation Provider che emette attestazioni non vincolate al dispositivo DEVE indicare nei propri metadati di Credential Issuer che non necessita di una KA. Una Wallet Unit NON DEVE inviare una KA a un Attestation Provider quando richiede un'attestazione non vincolata al dispositivo. Nota: una Wallet Unit invia una WIA all'Attestation Provider indipendentemente dal fatto che le attestazioni da esso emesse siano vincolate al dispositivo o meno.
- Un Wallet Provider DEVE garantire che la presentazione di una KA sia crittograficamente vincolata allo specifico contesto in cui è destinata a essere utilizzata. Nota: come specificato in OpenID4VCI_, ciò si ottiene facendo sì che la KA firmata contenga essa stessa un nonce fornito dal PID Provider o dall'Attestation Provider durante il processo di emissione. In alternativa, la Wallet Unit presenta la KA insieme a una Proof-of-Possession costituita da una firma su tale nonce, creata dalla chiave privata corrispondente a una delle chiavi pubbliche attestate nella KA.
- Durante l'emissione di un PID o di un'attestazione vincolata al dispositivo, il PID Provider o l'Attestation Provider DEVE verificare la KA in conformità ai requisiti dell'Appendice F.4 di OpenID4VCI_.
- Durante l'emissione di un PID o di un'attestazione vincolata al dispositivo, il PID Provider o l'Attestation Provider DEVE ricevere una prova che la Wallet Unit possiede le chiavi private corrispondenti a tutte le chiavi pubbliche presenti nella KA.
- Se il Keystore o il WSCA/Remote WSCD è in grado di esportare una chiave privata, il Wallet Provider DEVE specificare questa capacità come attributo nella KA.
- Un Wallet Provider DEVE considerare tutti i fattori rilevanti, inclusi l'uso offline, l'interoperabilità e il rischio che una KA diventi un vettore per tracciare l'Utente, nel decidere il periodo di validità di una KA.
- La Key Attestation NON DEVE essere emessa dal Wallet Provider se l'affidabilità del Keystore o del WSCA/Remote WSCD non è garantita. In tal caso, l'Istanza del Wallet DEVE essere revocata.


Requisiti del Keystore
""""""""""""""""""""""

Il Keystore è il meccanismo di archiviazione sicuro hardware-backed di default per tutte le operazioni crittografiche della Wallet Unit e per tutte le Credenziali Digitali, ad eccezione del PID che richiede un WSCA/Remote WSCD.

I requisiti del Keystore sono definiti di seguito:

- Su dispositivi Android, il Keystore DOVREBBE utilizzare Strongbox; il Trusted Execution Environment (TEE) PUÒ essere utilizzato come fallback quando Strongbox non è disponibile.
- Su dispositivi iOS, il Keystore DEVE utilizzare il Secure Enclave.
- Le proprietà del Keystore DEVONO essere attestate tramite le OEM Key Attestation APIs (Android Key Attestation API per Android, Apple DeviceCheck per iOS).
- Il Wallet Provider DEVE utilizzare il Keystore per generare, archiviare e utilizzare tutte le chiavi crittografiche della Wallet Instance, ad eccezione delle chiavi del PID a LoA High.
- Il Keystore DEVE fornire protezione hardware contro l'estrazione e la manipolazione non autorizzata delle chiavi private.

Per informazioni più dettagliate, fare riferimento a :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet`, :ref:`wallet-instance-attestation-issuance:Emissione della Wallet Instance Attestation` e :ref:`wallet-attestation-issuance:Emissione della Key Attestation` di questo documento.


Requisiti WSCA/WSCD
"""""""""""""""""""

Il WSCA/Remote WSCD è usato esclusivamente per l'emissione e la gestione del PID a LoA High. In IT-Wallet, il WSCD è implementato come Remote WSCD, ovvero un Hardware Security Module (HSM) remoto operato lato server.

I requisiti WSCA/WSCD sono definiti di seguito:

- La chiave privata del PID DEVE essere generata e gestita dal WSCA operante nel Remote WSCD (HSM remoto).
- Il Remote WSCD DEVE soddisfare i requisiti per il Livello di Garanzia Alto (LoA High) come definito da eIDAS 2.0.
- Il WSCA DEVE operare all'interno di un Remote WSCD basato su un HSM remoto, fornendo un livello di certificazione superiore rispetto al Keystore locale.
- Il Wallet Provider DEVE garantire che solo il WSCA possa accedere alla chiave privata del PID memorizzata nel Remote WSCD.

.. note::
  In futuro, il WSCA/Remote WSCD potrebbe essere esteso ad altre credenziali che richiedono LoA High.

Per informazioni più dettagliate, fare riferimento a :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet`, :ref:`wallet-instance-attestation-issuance:Emissione della Wallet Instance Attestation` e :ref:`wallet-attestation-issuance:Emissione della Key Attestation` di questo documento.


