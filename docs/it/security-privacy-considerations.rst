.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst

Considerazioni di Sicurezza e Privacy
=====================================

Questa sezione fornisce un'analisi informale della sicurezza della specifica IT-Wallet analizzando la conformità con i requisiti di sicurezza e privacy identificati in [`OpenID4VC-SecTrust`_].

.. note::

  Poiché [`OpenID4VC-SecTrust`_] è ancora in fase di sviluppo, le considerazioni di sicurezza e privacy descritte potrebbero cambiare in futuro.

.. note::
  Il focus dell'analisi è la conformità delle scelte progettuali nella specifica IT-Wallet rispetto ai protocolli OpenID4VC.
  Sono attualmente fuori ambito *(i)* l'analisi della progettazione del flusso di prossimità basato su ISO 18013-5, e *(ii)* l'analisi dell'implementazione;
  di conseguenza 7 requisiti specificamente relativi all'implementazione non sono considerati (ad esempio, SV-00: Il Verificatore deve implementare il protocollo in modo sicuro e corretto).

Come in [`OpenID4VC-SecTrust`_], tutti i requisiti sono numerati per riferimento. Insieme al rispettivo componente che deve implementare il requisito:

* **CF**: Formato della Credenziale;
* **P**: Protocollo;
* **E**: Ecosistema;
* **I**: Fornitore di Credenziali;
* **V**: Verificatore di Attestati Elettronici;
* **W**: Wallet.

Questa specifica aggiunge la categoria del requisito come prefisso:

* **SR**: Requisiti di Sicurezza;
* **PR**: Requisiti di Privacy;
* **SPR**: Requisiti di Sicurezza e Privacy.

L'identificatore finale utilizza il seguente spazio dei nomi: *categoria_requisito-componente-id*.

Per ogni requisito definito di seguito, questa sezione utilizza la descrizione definita in [`OpenID4VC-SecTrust`_], specificando se il requisito è soddisfatto (completamente soddisfatto: |check-icon|, parzialmente soddisfatto: |partially-check-icon|, e non soddisfatto: |uncheck-icon|).
Di seguito, i requisiti sono raggruppati in base alla loro categoria.

Requisiti di Sicurezza
----------------------

SR-CF-10 e SR-E-10
^^^^^^^^^^^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Per qualsiasi presentazione, il formato della Credenziale e il Trust Framework devono essere progettati in modo sicuro per determinare il Fornitore di Credenziali e verificare che la Credenziale originale sia stata emessa da questo Fornitore di Credenziali (ad esempio, utilizzando una firma crittografica).

La specifica IT-Wallet supporta sia il formato di Credenziale SD-JWT VC che mdoc-CBOR. L'autenticità e l'integrità di una Credenziale vengono verificate controllando la firma del Fornitore di Credenziali.

- Per SD-JWT, la verifica viene eseguita utilizzando l'algoritmo specificato nel parametro dell'header **alg** di SD-JWT e un riferimento verificabile alla chiave pubblica che deve essere utilizzata per la verifica della firma. Utilizzando OpenID Federation, il riferimento verificabile al materiale crittografico pubblico è l'header **kid** dell'SD-JWT, dove il materiale crittografico viene ottenuto dalla Trust Chain relativa al Credential Issuer, specificato nel claim **iss**.
- Per mdoc-CBOR, la firma del Fornitore di Credenziali è contenuta nel *Mobile Security Object* (MSO) e deve essere convalidata utilizzando la chiave pubblica del Fornitore di Credenziali attraverso una catena di certificati attendibile contenuta nel parametro dell'header **x5chain**.

SR-CF-20
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Per qualsiasi presentazione, il formato della Credenziale deve garantire che i dati legati alla Credenziale originale non possano essere alterati (ad esempio, utilizzando una firma crittografica).

La firma crittografica inclusa nel formato della Credenziale garantisce che qualsiasi manomissione della Credenziale comporterà una verifica fallita.

SR-CF-21
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Per l'associazione crittografica con l'Utente, il formato di presentazione richiede al Titolare di dimostrare il possesso della chiave privata associata alla Credenziale. Questo viene tipicamente ottenuto facendo firmare al Titolare una sfida, che consiste in un valore nonce e l'identificatore univoco del Verificatore di Attestati Elettronici.

Sia SD-JWT che mdoc-CBOR supportano l'associazione crittografica con l'Utente definendo come un Titolare può presentare una Credenziale a un Verificatore di Attestati Elettronici, fornendo una prova crittografica del legittimo possesso della Credenziale.

Attualmente, per il flusso remoto, IT-Wallet supporta solo presentazioni SD-JWT. In questo scenario, il parametro KB-JWT (Key-Bound JWT) viene utilizzato per dimostrare che il Titolare possiede la chiave privata associata alla Credenziale. Il Titolare firma il KB-JWT utilizzando un **nonce** e un identificatore del Verificatore di Attestati Elettronici, utilizzando il parametro **aud**, come sfida.

SR-E-20
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il Trust Framework deve garantire che l'identificazione di un Fornitore di Credenziali sia unica e non ambigua. Se ci sono più istanze dello stesso Fornitore di Credenziali che utilizzano lo stesso materiale chiave, il Verificatore di Attestati Elettronici deve fidarsi di tutte le istanze allo stesso modo.

Il Trust Framework IT Wallet garantisce che ogni entità (ad esempio, un Fornitore di Credenziali) sia identificata in modo univoco attraverso chiavi crittografiche e metadati, distribuiti tramite un attestato verificabile, come la Entity Configuration OpenID Federation verificata all'interno di una Trust Chain.

SR-E-30
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il modo in cui il Verificatore di Attestati Elettronici determina l'affidabilità del Fornitore di Credenziali definito nel Trust Framework deve essere protetto dall'influenza di una parte malintenzionata che può, ad esempio, introdurre entità non affidabili in una directory.

I Fornitori di Credenziali sono registrati da un Trust Anchor o dal suo Intermediario. Per verificare l'affidabilità di un Fornitore di Credenziali, un Verificatore di Attestati Elettronici deve verificare che la Trust Chain relativa al Fornitore di Credenziali sia valida e ancora attiva. Questo processo di convalida garantisce che solo entità affidabili siano autorizzate a partecipare al sistema, impedendo l'introduzione di attori non affidabili.

SR-E-40
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il Trust Framework deve garantire che ci sia un modo per i Verificatori di Attestati Elettronici di mantenere aggiornate le loro informazioni sui Fornitori di Credenziali affidabili e che ci sia un modo per revocare la fiducia in un Fornitore di Credenziali.

Se l'Entity Statement di un Fornitore di Credenziali viene revocato o non è disponibile, significa che il Fornitore di Credenziali non è più considerato valido all'interno della federazione. Ciò garantisce che i Verificatori di Attestati Elettronici abbiano accesso in tempo reale allo stato delle entità affidabili e possano revocare la fiducia se necessario. Tuttavia, i Verificatori di Attestati Elettronici devono controllare attivamente lo stato del Fornitore di Credenziali interrogando gli endpoint della federazione (cioè, l'endpoint fetch per ottenere la Subordinate Statement).

SR-I-10
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il Fornitore di Credenziali deve autenticare e identificare l'Utente correttamente secondo le aspettative del Verificatore di Attestati Elettronici (che possono essere definite in una specifica, Trust Framework o per convenzione).

Il processo di emissione utilizza flussi basati su OAuth 2.0, in particolare il flusso Authorization Code, per autenticare in modo sicuro l'Utente. Inoltre, l'autenticazione dell'Utente viene eseguita utilizzando lo schema CieID con alto LoA, l'Autenticazione eID Substantial con Verifica MRTD oppure il PID/IT-Wallet ID.

SR-I-20
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il Fornitore di Credenziali deve utilizzare solo attributi corretti e aggiornati sull'Utente nella Credenziale dove sono previsti dati verificati.

Quando sono previsti dati verificati, il Fornitore di Credenziali ottiene gli attributi corretti e aggiornati dalle relative Fonti Autentiche, garantendone l'accuratezza al momento dell'emissione.

SR-I-30
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il Fornitore di Credenziali deve revocare una Credenziale una volta che il Fornitore di Credenziali viene a conoscenza di un potenziale abuso della Credenziale.

Il Fornitore di Credenziali è l'entità responsabile della revoca di una Credenziale. La specifica descrive diversi casi d'uso che possono attivare un processo di revoca e dettaglia il flusso di revoca in cui il Fornitore di Credenziali revoca le Credenziali su richiesta dell'Utente (attraverso l'Istanza del Wallet) dopo aver verificato il possesso delle Credenziali.

SR-I-40
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il Fornitore di Credenziali deve includere nella Credenziale solo dati di associazione del Titolare che sono legati all'Utente effettivo (e non, ad esempio, includere una chiave crittografica sotto il controllo di una terza parte).

Il processo di emissione lega in modo sicuro la Credenziale all'Utente come segue (vedi :numref:`fig_Low-Level-Flow-ITWallet-PID-QEAA-Issuance`):

* Autorizzazione (Passi 8-10): L'Istanza del Wallet invia una richiesta di autorizzazione, e il Fornitore di Credenziali autentica l'Utente utilizzando uno schema CieID o un PID/IT-Wallet ID valido, fornendo il Token di Accesso all'Utente.
* Prova di Possesso della Chiave (Passi 12-13, 16-17): Il Wallet crea un DPoP Proof JWT, legando il Token di Accesso all'Istanza del Wallet. La stessa chiave viene poi utilizzata successivamente per richiedere la Credenziale, garantendo la continuità della proprietà.
* Emissione della Credenziale (Passi 18-21): La richiesta di Credenziale viene verificata utilizzando la prova di possesso, che è crittograficamente legata all'Utente. L'uso della stessa chiave nel DPoP garantisce che il materiale chiave sia controllato dall'Istanza del Wallet, e non da una terza parte.

SR-I-50
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - (condizionale rispetto a I-10) Il Fornitore di Credenziali deve garantire che la Credenziale sia stata memorizzata in un Wallet sicuro.

Un Wallet Attestation affidabile garantisce che l'Istanza del Wallet sia sicura e soddisfi gli standard di sicurezza richiesti prima che qualsiasi Credenziale venga emessa o memorizzata.
Nei Passi 5-6 di :numref:`fig_Low-Level-Flow-ITWallet-PID-QEAA-Issuance`, l'Istanza del Wallet fornisce una Wallet Attestation, che include una prova di possesso
firmata con la chiave privata del Wallet. Questo attestato conferma che l'Istanza del Wallet è genuina ed è stata verificata dal Fornitore di Wallet.

Il Fornitore di Credenziali verifica questo attestato prima di consentire al Wallet di partecipare al processo di emissione, garantendo che il Wallet aderisca a specifici standard di sicurezza.
Successivamente, tutte le chiavi crittografiche generate e utilizzate nel processo provengono da questa Istanza del Wallet attestata.

.. note::
  C'è attualmente un problema aperto su questo aspetto (https://github.com/openid/OpenID4VCI/issues/355) nella specifica OpenID4VCI.

SR-P-20
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il protocollo deve garantire che nessuna terza parte possa interferire con il processo di emissione in modo tale che il Fornitore di Credenziali emetta Credenziali per la terza parte all'Utente.

Questo requisito è affrontato mediante l'identificazione sicura del Fornitore di Credenziali. Il parametro ^iss^ nella risposta di autorizzazione assicura al Wallet che la risposta provenga dal Fornitore di Credenziali previsto e la verifica crittografica dei token ricevuti garantisce che siano stati emessi dal legittimo Fornitore di Credenziali. Inoltre, l'uso di PKCE evita l'iniezione del codice da un'altra sessione alla sessione dell'Utente.

SR-P-30
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il protocollo deve garantire che l'interazione tra il Wallet e il Verificatore di Attestati Elettronici sia protetta in modo tale che nessuna terza parte possa interferire con l'interazione modificando le informazioni trasmesse.

Il processo di presentazione avviene attraverso diversi flussi, inclusi remoto e di prossimità. Nel caso del flusso remoto, una combinazione di Request Objects firmati, utilizzo di **nonce**, validazione della Trust Chain, Wallet Attestation e associazione del Titolare garantisce che nessuna terza parte possa interferire o modificare le informazioni trasmesse tra il Wallet e il Verificatore di Attestati Elettronici. Questi meccanismi sono allineati con il Requisito di Sicurezza P-30, proteggendo l'interazione da manomissioni o attacchi di iniezione.

SR-P-40
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |partially-check-icon|
     - Il protocollo deve garantire che l'interazione tra un attaccante e un Verificatore di Attestati Elettronici non possa essere inoltrata e completata con successo da un Utente.

Nel caso del flusso sullo stesso dispositivo, questo può essere prevenuto utilizzando e controllando correttamente il valore **nonce**, che viene creato e inviato dal Verificatore di Attestati Elettronici nella richiesta di autorizzazione.
Il Verificatore di Attestati Elettronici dovrebbe mantenere una mappatura tra le sessioni dell'Utente e il **nonce** che è previsto nel flusso. Il Verificatore di Attestati Elettronici dovrebbe accettare una presentazione solo se il **nonce** nella presentazione
corrisponde al **nonce** che è previsto per la sessione dell'Utente. Con questa contromisura, il Verificatore di Attestati Elettronici deve rilevare se viene inviata una presentazione che non era legata alla sessione dell'Utente o se non
esiste affatto una sessione dell'Utente, prevenendo l'attacco.

Per il flusso cross-device il requisito è parzialmente soddisfatto in quanto il flusso è vulnerabile agli attacchi di Cross-Device Consent Phishing (un attaccante potrebbe iniziare il flusso di presentazione,
ottenere il Request Object firmato e il codice QR, e inoltrarlo alla vittima).

Alcune misure di sicurezza sono già in atto, come l'uso di **nonce** e state. Il **nonce** garantisce la freschezza della richiesta, e lo state lega il flusso a una transazione unica,
riducendo così l'opportunità per un attacco di successo.

.. note::
  Altre misure di sicurezza sono attualmente in fase di valutazione nell'issue numero [117](https://github.com/italia/eid-wallet-it-docs/issues/117),
  dove viene discussa una lista di mitigazioni da [`OAuthCrossDeviceSec`_]. Due esempi sono:

  - Codici QR a breve durata/limitati nel tempo: Ridurre la durata del codice QR (ad esempio, 2-3 minuti) è necessario per limitare la finestra temporale disponibile per gli attacchi.
  - Codici QR monouso: I codici QR monouso limitano la possibilità di attacchi quando lo stesso codice QR viene inviato a più vittime.

SR-P-41
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il protocollo deve garantire che un attaccante non possa inoltrare con successo un'interazione tra un Wallet e un Verificatore di Attestati Elettronici a un Verificatore di Attestati Elettronici sotto il controllo dell'attaccante.

Un prerequisito per un attacco di questo tipo è che l'attaccante abbia accesso ad alcuni messaggi tra il Wallet e il Verificatore di Attestati Elettronici, ad esempio,
l'attaccante potrebbe avere accesso alla presentazione contenuta nel Token VP. Dato ciò, la corretta implementazione di TLS garantisce la riservatezza, evitando la fuga della risposta.
Oltre a TLS, l'implementazione esistente dei controlli **nonce** e audience nel protocollo di presentazione dovrebbe aiutare a soddisfare il requisito di sicurezza P-41.
Per quanto riguarda il claim **nonce**, il Verificatore di Attestati Elettronici DEVE verificare che il valore **nonce** nel Token VP corrisponda al valore **nonce** che è creato dal Verificatore di Attestati Elettronici durante la richiesta di autorizzazione.
Per quanto riguarda il valore **aud**, il Verificatore di Attestati Elettronici deve verificare che l'audience della presentazione corrisponda all'identificatore del Verificatore di Attestati Elettronici.

SR-P-50
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |partially-check-icon|
     - Il protocollo deve garantire che terze parti non possano interferire con il processo di associazione.

Nella fase di emissione, l'associazione del Titolare avviene alla richiesta di Credenziale all'endpoint protetto della Credenziale. Ciò significa che l'attaccante deve ottenere il token di accesso
prima e quindi inviare la richiesta all'endpoint della Credenziale e legare le Credenziali alle chiavi sotto il suo controllo. La specifica IT-Wallet richiede l'uso di un
token di accesso vincolato al mittente, il che significa che il token di accesso si lega al dispositivo utilizzando materiali crittografici.

La seconda superficie per l'attacco è correlata alla gestione delle chiavi. Nel caso di utilizzo di chiavi basate su software, è possibile clonare le chiavi e spostarle su un dispositivo sotto
il controllo dell'attaccante, e nel caso di furto delle Credenziali, l'attaccante può facilmente creare una prova di possesso delle chiavi. IT-Wallet è meno vulnerabile a questi attacchi in quanto supporta
un Keystore hardware-backed che utilizza chiavi basate su hardware. Tuttavia, la mancanza di un
profilo di certificazione che certifichi il Keystore (TEE) contro attaccanti altamente capaci (la certificazione per le attuali soluzioni TEE sul mercato raggiunge al massimo AVA_VAN.3
come mostrato ad esempio in questo `Rapporto di Certificazione <https://www.tuv-nederland.nl/assets/files/cerfiticaten/2021/08/nscib-cc-0244671-cr-1.0.pdf>`_ o `sito Global Platform <https://globalplatform.org/specs-library/tee-protection-profile-v1-3/>`_ rende il requisito solo parzialmente soddisfatto per le Credenziali Digitali standard. Per il PID, questa limitazione è superata richiedendo un WSCA operante in un Remote WSCD (HSM remoto lato server), che fornisce certificazione a un livello più elevato.

SR-V-10
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |partially-check-icon|
     - (condizionale rispetto a I-50+V-20) Il Verificatore di Attestati Elettronici deve garantire che la Credenziale sia memorizzata in un Wallet sicuro.

Il Verificatore di Attestati Elettronici controlla la Wallet Attestation durante gli scambi (inviato con la risposta di autorizzazione), garantendo che soddisfi i criteri di sicurezza richiesti dal Verificatore di Attestati Elettronici e sia sotto la sola responsabilità del suo emittente, il Fornitore di Wallet affidabile.

.. note::
  Attualmente, non sono specificate misure di sicurezza e privacy esplicite relative a questo requisito in [`OpenID4VC-SecTrust`_] e non è chiaramente definito cosa significhi ^memorizzato in un Wallet sicuro^. Senza questo dettaglio, questo requisito è considerato solo parzialmente soddisfatto. Infatti, la Wallet Attestation garantisce
  che l'Istanza del Wallet stia operando su un dispositivo sicuro e affidabile e aderisca alle rigorose politiche di sicurezza stabilite dal Fornitore di Wallet. Tuttavia, l'attestato non garantisce direttamente che ogni
  Credenziale all'interno del Wallet sia memorizzata in modo sicuro; verifica la sicurezza complessiva dell'ambiente del Wallet, all'interno del quale risiedono le Credenziali. Pertanto, mentre l'attestato supporta la
  fiducia del Verificatore di Attestati Elettronici che la Credenziale provenga da una fonte sicura, è in definitiva una garanzia ampia della sicurezza del Wallet, piuttosto che una convalida specifica della memorizzazione individuale della Credenziale.

SR-V-20
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - (condizionale rispetto a I-10) Il Verificatore di Attestati Elettronici deve garantire che la Credenziale sia stata emessa da un Fornitore di Credenziali che emette Credenziali solo a Wallet affidabili.

Controllando l'affidabilità del Fornitore di Credenziali, il Verificatore di Attestati Elettronici garantisce che la Credenziale sia stata emessa da un Fornitore di Credenziali affidabile impegnato a emettere Credenziali solo a Wallet sicuri (come per SR-I-50).

.. note::
  Attualmente, non sono specificate misure di sicurezza e privacy esplicite relative a questo requisito in [`OpenID4VC-SecTrust`_], configurando questo elemento come qualcosa che richiede ulteriori sviluppi e chiarimenti.

SR-W-20
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il Wallet deve fornire informazioni affidabili e complete sui Fornitori di Credenziali all'Utente.

L'Istanza del Wallet scopre i Fornitori di Credenziali affidabili utilizzando risorse di terze parti affidabili, come l'API di Federazione (ad esempio, utilizzando l'Endpoint di Elenco Subordinato del Trust Anchor e dei suoi Intermediari), ispezionando i metadati del Fornitore di Credenziali e i Trust Mark per filtrare il Fornitore di PID.

Le informazioni del Fornitore di Credenziali vengono visualizzate all'Utente durante il processo di emissione e possono essere successivamente lette dall'Utente in quanto sono all'interno della Credenziale emessa.
Oltre alle informazioni del Fornitore di Credenziali, il *Type Metadata* dell'Attestato Elettronico contiene anche informazioni sulla Fonte Autentica.

SR-W-30
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il Wallet deve fornire informazioni affidabili e complete sui Verificatori di Attestati Elettronici all'Utente.

Il Wallet convalida la Trust Chain relativa al Verificatore di Attestati Elettronici e le sue informazioni vengono visualizzate all'Utente prima della presentazione.

Requisiti di Privacy
--------------------

PR-CF-30
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il Formato della Credenziale deve garantire che ci sia un meccanismo robusto per garantire che i dati che non devono essere rilasciati a un Verificatore di Attestati Elettronici non possano essere estratti dal Verificatore di Attestati Elettronici (Divulgazione Selettiva).

Sia SD-JWT che mdoc-CBOR forniscono la capacità di Divulgazione Selettiva, permettendo ai Titolari di rivelare solo campi specifici al Verificatore di Attestati Elettronici.

PR-CF-40
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |partially-check-icon|
     - Il Formato della Credenziale deve supportare la protezione dalla correlazione.

Mentre la Divulgazione Selettiva è uno strumento forte per prevenire la correlazione, la completa non collegabilità non è garantita in tutti i casi. Possono sorgere problemi come la collusione del Verificatore di Attestati Elettronici o il tracciamento del Fornitore di Credenziali.

.. tip::
  L'emissione in batch, utilizzando diverse chiavi di associazione e salt per ogni Credenziale, può mitigare i rischi di non collegabilità Verificatore di Attestati Elettronici/Verificatore di Attestati Elettronici e di presentazione.

PR-E-60
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il Trust Framework deve garantire che il Fornitore di Credenziali non possa sapere dove l'Utente utilizza la Credenziale.

Il Verificatore di Attestati Elettronici che esegue la Trust Evaluation sul Fornitore di Credenziali di una Credenziale non deve rilasciare alcuna informazione al Fornitore di Credenziali sull'Istanza del Wallet con cui sta interagendo. Utilizzando [`OID-FED`_] il Fornitore di Credenziali non sa chi è l'Utente che presenta la Credenziale.
Inoltre, la privacy è protetta anche durante il controllo dello stato della Credenziale. Utilizzando Status List [`TOKEN-STATUS-LIST`_], la specifica IT-Wallet garantisce che mentre il Verificatore di Attestati Elettronici controlla la validità della Credenziale, il Fornitore di Credenziali non apprende dove o quando la Credenziale viene utilizzata.

PR-E-70
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |partially-check-icon|
     - Il Trust Framework deve supportare la protezione dalla correlazione.

I seguenti meccanismi possono essere implementati per ridurre la correlazione:

- *Verificatore di Attestati Elettronici-Verificatore di Attestati Elettronici*: meccanismi di valutazione per garantire che un Verificatore di Attestati Elettronici richieda solo le informazioni che è autorizzato a ottenere dal Wallet. Questo approccio minimizza lo scambio di dati e aiuta a prevenire la profilazione dell'Utente attraverso potenziali collusioni tra Verificatori di Attestati Elettronici.
- *Fornitore di Credenziali-Verificatore di Attestati Elettronici*: Il Fornitore di Credenziali non richiede l'autenticazione del Verificatore di Attestati Elettronici durante la Trust Evaluation. In linea di principio, il Fornitore di Credenziali non sa quali Verificatori di Attestati Elettronici l'Utente sta accedendo e eviterà la profilazione dell'attività dell'Utente basata sull'accesso del Verificatore di Attestati Elettronici.

.. tip::
 I Trust Mark di OpenID Federation consentono la definizione di politiche personalizzate adatte alla soddisfazione di questo requisito.

PR-W-40
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il Wallet deve chiedere all'Utente un consenso significativo prima che una Credenziale venga utilizzata. Il Wallet deve fornire all'Utente l'opportunità di rivedere qualsiasi dato che viene rilasciato a un Verificatore di Attestati Elettronici.

Dopo aver stabilito la fiducia con il Verificatore di Attestati Elettronici, il Wallet chiede il consenso dell'Utente e fornisce all'Utente l'opportunità di rivedere e selezionare i dati da presentare al Verificatore di Attestati Elettronici.

PR-W-60
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il Wallet deve garantire che il Fornitore di Credenziali non possa sapere dove l'Utente utilizza la Credenziale.

Come per SR-P-80.

PR-W-70
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |uncheck-icon|
     - Il Wallet deve garantire che il Verificatore di Attestati Elettronici non possa sapere che lo stesso Utente sta utilizzando altri Verificatori di Attestati Elettronici.

Per mitigare la collegabilità Verificatore di Attestati Elettronici/Verificatore di Attestati Elettronici per le Credenziali SD-JWT, una soluzione proposta è l'emissione in batch, che prevede l'utilizzo di diverse chiavi crittografiche utilizzate nell'associazione delle chiavi e salt per ogni Credenziale emessa. Tuttavia, l'efficacia di questi metodi non è stata ancora valutata a fondo, anche in considerazione degli impatti che questi potrebbero avere sull'esperienza dell'utente, e non è ancora disponibile per IT-Wallet.

Requisiti di Sicurezza e Privacy
--------------------------------

SPR-E-50
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il Trust Framework deve garantire che i cicli di vita delle chiavi, dei certificati e delle Credenziali siano progettati in modo tale da minimizzare l'impatto di una compromissione.

Il ciclo di vita della Credenziale include un meccanismo di revoca della Credenziale basato su Status List [`TOKEN-STATUS-LIST`_] che garantisce che le Credenziali siano correttamente revocate quando compromesse o obsolete.

La revoca di un'Entità di Federazione (cioè, Fornitore di Credenziali, Verificatore di Attestati Elettronici, Fornitore di Wallet) è invece possibile non emettendo la corrispondente Subordinate Statement su quell'Entità e impostando una breve scadenza della Trust Chain, impedendo così l'uso improprio durante la compromissione.

.. tip::
  Inoltre, [`OID-FED`_] supporta un endpoint delle chiavi storiche per recuperare l'elenco delle chiavi scadute e revocate, con la motivazione della revoca.

SPR-P-10
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il protocollo deve garantire che nessuna terza parte possa leggere la Credenziale emessa dal Fornitore di Credenziali.

Per mitigare questa minaccia, la specifica IT-Wallet richiede i seguenti meccanismi di sicurezza nel processo di emissione:

- *TLS*: Utilizzato in tutte le comunicazioni tra il Wallet e il Fornitore di Credenziali, garantendo che i dati in transito siano crittografati e protetti dall'intercettazione da parte di attaccanti.
- *Wallet Attestation*: Garantisce che il Wallet operi su un dispositivo sicuro e affidabile e rispetti gli standard di sicurezza richiesti dal Fornitore di Credenziali, fornendo ulteriore garanzia che il Fornitore di Credenziali stia interagendo con un'Istanza del Wallet legittima.
- *DPoP*: Garantisce che il Titolare del token di accesso possieda la chiave privata associata ad esso, impedendo agli attaccanti di riutilizzare token intercettati.
- *Associazione del Titolare*: Lega la Credenziale a un Titolare specifico, garantendo che solo il legittimo Titolare possa utilizzare una Credenziale per autenticarsi con il Fornitore di Credenziali.
- *validazione redirect_uri*: Questa validazione garantisce che la risposta di autorizzazione sia inviata all'endpoint corretto e autorizzato, impedendo così l'intercettazione non autorizzata da parte di attori malintenzionati. Garantire l'integrità del **redirect_uri** è fondamentale per evitare qualsiasi manipolazione o reindirizzamento dell'URI.
- *PKCE*: Evita l'iniezione di un **code** di autorizzazione legittimo in un'altra sessione.

SPR-P-60
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il protocollo deve garantire che durante un'interazione con un Verificatore di Attestati Elettronici, un attaccante non possa leggere PII.

L'IT Wallet è conforme ai requisiti di P-60 garantendo che tutte le connessioni di rete siano protette da TLS.

Inoltre, poiché la Risposta di Autorizzazione contiene PII è importante che non venga inviata a un endpoint controllato dall'attaccante.
Nella specifica IT Wallet il **response_uri**, che è l'endpoint dove il Wallet invia la Risposta di Autorizzazione, è incluso nel Request Object firmato,
che viene verificato dal Wallet utilizzando la chiave pubblica del Verificatore di Attestati Elettronici e la Trust Chain. Questo garantisce che la Risposta di Autorizzazione venga inviata all'endpoint corretto.
Inoltre, la Risposta di Autorizzazione è crittografata con la chiave pubblica del Verificatore di Attestati Elettronici, garantendo che solo il destinatario previsto possa decrittografare e leggere le informazioni sensibili,
proteggendo ulteriormente la trasmissione.

Un altro endpoint da validare è il **redirect_uri**, che viene utilizzato per reindirizzare l'Utente al Verificatore di Attestati Elettronici dopo che la presentazione della Credenziale è completata.
Nella specifica IT-Wallet, il **redirect_uri** è registrato e validato in anticipo durante l'onboarding del Verificatore di Attestati Elettronici utilizzando OpenID Federation. Durante la fase di presentazione, il Wallet deve validare questo valore verificando la fiducia con il Verificatore di Attestati Elettronici secondo la Sezione `Meccanismo di Valutazione della Fiducia <trust.html#trust-evaluation-mechanism>`_


Per essere sicuri che il **redirect_uri** sia ricevuto da un Wallet legittimo e non dall'attaccante, l'endpoint di risposta del Verificatore di Attestati Elettronici al ricevimento di una risposta di autorizzazione valida crea un valore crittografico fresco che è collegato alla risposta di autorizzazione e lo allega al **redirect_uri** che viene inviato al Wallet.
Quando il Verificatore di Attestati Elettronici riceve il reindirizzamento, può estrarre il codice di risposta e verificare con il suo endpoint di risposta se il codice di risposta era associato a questa Risposta di Autorizzazione. (Vedi :ref:`remote-flow:URI di Reindirizzamento`).

SPR-P-70
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il protocollo deve garantire che durante un'interazione con un Fornitore di Credenziali, un attaccante non possa leggere PII.

Nel processo di emissione, poiché la Credenziale all'interno di una Risposta di Credenziale contiene PII, è necessario che la Credenziale non venga inviata o intercettata da un attaccante.
Per mitigare queste minacce, la specifica IT-Wallet richiede i seguenti meccanismi di sicurezza:

- *TLS*: Utilizzato in tutte le comunicazioni tra il Wallet e il Fornitore di Credenziali, garantendo che i dati in transito siano crittografati e protetti dall'intercettazione da parte di attaccanti.
- *Attestato dell'Istanza del Wallet*: Garantisce che il Wallet operi su un dispositivo sicuro e affidabile e rispetti gli standard di sicurezza richiesti dal Fornitore di Credenziali, fornendo ulteriore garanzia che il Fornitore di Credenziali stia interagendo con un'Istanza del Wallet legittima.
- *DPoP*: Garantisce che il Titolare del token di accesso possieda la chiave privata associata ad esso, impedendo agli attaccanti di riutilizzare token intercettati.
- *Associazione del Titolare*: Lega la Credenziale a un Titolare specifico, garantendo che solo il legittimo Titolare possa utilizzare una Credenziale per autenticarsi con il Fornitore di Credenziali.
- *validazione redirect_uri*: Questa validazione garantisce che la risposta di autorizzazione sia inviata all'endpoint corretto e autorizzato, impedendo così l'intercettazione non autorizzata da parte di attori malintenzionati. Garantire l'integrità del **redirect_uri** è fondamentale per evitare qualsiasi manipolazione o reindirizzamento dell'URI.
- *PKCE*: Evita l'iniezione di un **code** di autorizzazione legittimo in un'altra sessione.

.. tip::
  Un ulteriore miglioramento della sicurezza che potrebbe essere applicato per aggiungere un ulteriore livello di protezione per le informazioni sensibili dell'Utente è la crittografia delle risposte di Credenziale.
  Lo standard OpenID4VCI fornisce l'opzione per il Wallet di richiedere Credenziali crittografate contenenti PII includendo un oggetto **credential_response_encryption** nella sua richiesta.

.. note::
  Attualmente, non sono specificate misure di sicurezza e privacy esplicite relative a questo requisito in [`OpenID4VC-SecTrust`_], rimane un lavoro in corso.

SPR-P-80
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il protocollo deve garantire che il Fornitore di Credenziali non possa sapere dove l'Utente utilizza la Credenziale.

Il protocollo di scambio non richiede alcuna interazione tra Verificatori di Attestati Elettronici e Fornitori di Credenziali.
Inoltre, Status List che preserva la privacy, garantisce che mentre il Verificatore di Attestati Elettronici controlla la validità della Credenziale, il Fornitore di Credenziali non apprende dove o quando la Credenziale viene utilizzata.

SPR-W-50
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - Il Wallet deve garantire che le Credenziali e le chiavi private siano protette da accessi non autorizzati.

Per prevenire l'accesso non autorizzato al Wallet, viene sbloccato sul dispositivo dell'Utente inserendo un numero di identificazione personale (PIN) o utilizzando l'autenticazione biometrica, come l'impronta digitale o il riconoscimento facciale, in base alle preferenze dell'Utente e alle capacità del dispositivo. Inoltre, le chiavi crittografiche sono memorizzate in modo sicuro all'interno del Keystore (o del WSCA/Remote WSCD per il PID), garantendo che solo l'Utente possa accedervi, impedendo così l'uso non autorizzato o la manomissione.


