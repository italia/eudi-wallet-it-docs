.. include:: ../common/common_definitions.rst

Matrice di Test per Wallet Provider
-----------------------------------

Questa sezione fornisce l'insieme di casi di test per verificare la conformità di un'implementazione di Soluzione Wallet e Istanza del Wallet alle regole tecniche definite nell'ecosistema IT-Wallet.
Il piano di test è basato sui requisiti estratti dalle seguenti Sezioni:

- :ref:`trust-infrastructure:L'Infrastruttura di Trust`
- :ref:`wallet-solution:Soluzione Wallet`
- :ref:`credential-issuance:Emissione di Attestati Elettronici`
- :ref:`credential-presentation:Presentazione dell'Attestato Elettronico`
- :ref:`endpoints:Endpoints`
- :ref:`mobile-application-instance:Istanza dell'Applicazione Mobile`


.. note::
   I casi di test in questo elenco variano di ambito: alcuni restano ad alto livello e rimandano al completamento dei flussi utente, alla conformità rispetto ai principi architetturali e di interoperabilità; altri ancora sono di basso livello, mirati a singoli requisiti dettagliati e verificano funzionalità specifiche.

.. _wallet-provider-backend-testcases:

Casi di Test per Backend del Fornitore del Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Questa sezione elenca i casi di test dalle Sezioni:

- :ref:`wallet-solution-requirements:Requisiti della Soluzione Wallet`
- :ref:`wallet-solution-components:Componenti della Soluzione Wallet`
- :ref:`wallet-instance:Istanza del Wallet`
- :ref:`wallet-provider-entity-configuration:Entity Configuration del Fornitore di Wallet`
- :ref:`wallet-solution-metadata:Metadati della Soluzione Wallet`
- `e-Service PDND Wallet Provider Catalogue <wallet-provider-endpoint.html#e-service-pdnd-wallet-provider-catalogue0>`_


.. list-table::
   :class: longtable
   :widths: 15 15 20 55
   :header-rows: 1

   * - ID Caso di Test
     - Scopo
     - Descrizione
     - Risultato Atteso
   * - WP_001
     - Trust, Sicurezza
     - Pubblicazione Entity Configuration
     - Una richiesta HTTP GET all'endpoint ``.well-known/openid-federation`` recupera l'Entity Configuration del Fornitore del Wallet.
   * - WP_002
     - Trust, Sicurezza
     - Firma Entity Configuration
     - L'Entity Configuration del Fornitore del Wallet è un JWT firmato che è conforme a `OID-FED`_.
   * - WP_002a
     - Trust, Interoperabilità
     - Parametro header ``alg`` del JWT Entity Configuration
     - L'header del JWT Entity Configuration contiene un ``alg`` impostato su un algoritmo di firma consentito (es. ``ES256``) e non ``none``.
   * - WP_002b
     - Trust, Interoperabilità
     - Parametro header identificativo chiave del JWT Entity Configuration
     - L'header del JWT Entity Configuration contiene un ``kid`` uguale al thumbprint della chiave pubblica utilizzata per firmare l'Entity Configuration.
   * - WP_002c
     - Trust, Interoperabilità
     - Parametro header tipo del JWT Entity Configuration
     - L'header del JWT Entity Configuration contiene ``typ`` impostato su ``entity-statement+jwt``.
   * - WP_002d
     - Trust, Interoperabilità
     - Claim payload issuer e subject dell'Entity Configuration
     - Il payload del JWT Entity Configuration contiene ``iss`` e ``sub``, entrambi impostati sull'URL pubblico del Fornitore del Wallet.
   * - WP_002e
     - Trust, Interoperabilità
     - Validità Entity Configuration
     - Il payload del JWT Entity Configuration contiene ``iat`` e ``exp`` come timestamp Unix validi.
   * - WP_002f
     - Trust, Interoperabilità
     - Suggerimenti autorità Entity Configuration
     - Il payload del JWT Entity Configuration contiene ``authority_hints`` come array di URL validi di entità superiori immediate.
   * - WP_002g
     - Trust, Interoperabilità
     - Chiavi di firma Entity Configuration
     - Il payload del JWT Entity Configuration contiene il parametro ``jwks`` avente uno o più JWK (:rfc:`7517`) validi, ciascuno contenente chiavi pubbliche di firma del Fornitore del Wallet nel ruolo di Entità della Federazione .
   * - WP_002h
     - Trust, Interoperabilità
     - Metadata Entity Configuration
     - Il payload del JWT Entity Configuration contiene un oggetto ``metadata`` che include il parametro ``wallet_solution`` e opzionalmente il parametro ``federation_entity``, ciascuno valorizzato seguendo il proprio schema.
   * - WP_003
     - Trust, Interoperabilità
     - Utilizzo chiave metadata
     - Le chiavi pubbliche nell'oggetto JSON sono usate esclusivamente per la firma e/o cifratura quando l'Entità agisce come Fornitore del Wallet (es. per emettere la Wallet Attestation).
   * - WP_004
     - Trust, Interoperabilità
     - Riferimento chiave metadata
     - Per riferire le chiavi pubbliche, l'oggetto JSON contiene esattamente uno dei seguenti claim: ``jwks``, ``jwks_uri``, o ``signed_jwks_uri``.
   * - WP_004a
     - Trust, Interoperabilità
     - JWKS per valore
     - Se ``jwks`` è presente, il suo valore contiene un elemento JWK (:rfc:`7517`) valido.
   * - WP_004b
     - Trust, Interoperabilità
     - JWKS per riferimento
     - Se ``jwks_uri`` è presente, il valore è un URL HTTPS a un JWKS che risulta risolvibile e valido.
   * - WP_004c
     - Trust, Interoperabilità
     - URI JWKS firmato
     - Se ``signed_jwks_uri`` è presente, il valore è un URL HTTPS che punta a un JWT. Il payload di tale JWT è un JWK (:rfc:`7517`) ed è firmato con una chiave dell'Entità di Federazione.
       La risorsa specificata da ``signed_jwks_uri`` è servita con il content type ``application/jwk-set+jwt``. Un recupero riuscito di ``signed_jwks_uri`` restituisce lo stato ``HTTP 200``.
   * - WP_005
     - Trust, UX
     - Applicazione 2FA portale
     - Il portale del Fornitore di Wallet applica correttamente l'autenticazione a due fattori (2FA) prima di consentire agli Utenti di eseguire qualsiasi operazione.
   * - WP_006
     - Revoca Wallet, Sicurezza
     - Vista stato Istanze del Wallet del portale
     - Il portale del Fornitore di Wallet consente correttamente agli Utenti di visualizzare lo stato corrente di tutte le Istanze del Wallet collegate al loro Account.
   * - WP_007
     - Revoca Wallet, Sicurezza
     - Trigger revoca avviata dall'utente
     - Il Fornitore di Wallet implementa e supporta richieste di revoca avviate dagli Utenti tramite il suo portale.
   * - WP_007a
     - Revoca Wallet, Sicurezza
     - Revoca istanza portale
     - Il portale del Fornitore di Wallet consente correttamente agli Utenti di revocare un'Istanza del Wallet specifica o tutte le Istanze del Wallet.
   * - WP_008
     - Revoca Wallet, Sicurezza
     - Trigger revoca avviata dal Fornitore di Attestati Elettronici di Dati di Identificazione Personale
     - Il Fornitore di Wallet implementa e supporta richieste di revoca attivate dai Fornitori di Attestati Elettronici di Dati di Identificazione Personale tramite il PDND Endpoint.
   * - WP_009
     - Revoca Wallet, Sicurezza
     - Trigger revoca avviata dalle Autorità Legali
     - Il Fornitore di Wallet implementa e supporta richieste di revoca attivate dalle Autorità Legali o Organi di Supervisione (es. attività illegali).
   * - WP_010
     - Trust, Interoperabilità
     - Meccanismo di revoca Istanza del Wallet
     - Quando il Fornitore di Wallet attiva la revoca per un'Istanza del Wallet specifica, in qualsiasi momento, quell'Istanza viene terminata e non può più eseguire alcuna funzione.
   * - WP_011
     - Trust, Sicurezza
     - Verifica integrità Istanza del Wallet
     - Il Fornitore di Wallet valuta periodicamente l'integrità, l'autenticità e la genuinità dell'Istanza del Wallet utilizzando la Play Integrity API (Android) o App Attest (iOS).
   * - WP_012
     - Ciclo di vita, Interoperabilità
     - Architettura componente backend
     - Il Backend del Fornitore di Wallet supporta tutti i componenti (Frontend, Interfaccia API, Gestione Ciclo di Vita Istanza del Wallet, e Trust & Sicurezza) come mostrato in :ref:`Figure of Wallet Solution High Level Architecture <fig_wallet-solution-high-level-architecture>`.

.. _wallet-instance-testcases:

Casi di Test per Istanza del Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Questa sezione elenca i casi di test dalle Sezioni:

- `Configuration of the Federation <trust.html#configuration-of-the-federation>`_
- `Trust Evaluation Mechanism <trust.html#trust-evaluation-mechanism>`_
- :ref:`wallet-solution-requirements:Requisiti della Soluzione Wallet`
- :ref:`wallet-solution-components:Componenti della Soluzione Wallet`
- :ref:`wallet-instance:Istanza del Wallet`
- `Error Handling for Wallet Instance Management <wallet-provider-endpoint.html#error-handling-for-wallet-instance-management>`__
- `Mobile Application Instance Initialization <mobile-application-instance.html#mobile-application-instance-initialization>`_


.. list-table::
   :class: longtable
   :widths: 15 15 20 55
   :header-rows: 1

   * - ID Caso di Test
     - Scopo
     - Descrizione
     - Risultato Atteso
   * - WP_013
     - Ciclo di vita, Interoperabilità
     - Architettura componente frontend
     - Istanza del Wallet supporta tutti i componenti (Interfaccia Utente, Gestione Ciclo di Vita, Fornitore di Attestato Elettronico, Presentazione, Backup/Ripristino, Keystore e WSCA/WSCD Interface per il PID) come mostrato in :ref:`Figure of Wallet Solution High Level Architecture <fig_wallet-solution-high-level-architecture>`.
   * - WP_014
     - Trust, Sicurezza
     - Implementazione Keystore
     - Istanza del Wallet utilizza il Keystore hardware-backed (Strongbox o TEE su Android; Secure Enclave su iOS) per tutte le operazioni crittografiche richieste, come generare firme e gestire le chiavi, per tutte le Credenziali Digitali eccetto il PID. Per l'emissione e la gestione del PID, la Wallet Instance interagisce con il WSCA operante nel Remote WSCD (HSM remoto), per conformarsi ai requisiti di Livello di Garanzia Alto.
   * - WP_015
     - Ciclo di vita, UX
     - Compatibilità Android/iOS
     - Istanza del Wallet si installa e opera con piena funzionalità su dispositivi Android e iOS ed è disponibile su Play Store e App Store.
   * - WP_016
     - Trust, Issuance, Interoperabilità
     - Recupero e gestione metadata Trust Anchor
     - Istanza del Wallet recupera e aggiorna l'Entity Configuration del Trust Anchor prima dell'uso e la mantiene aggiornata.
   * - WP_017
     - Trust, Issuance, Interoperabilità
     - Validare autenticità Trust Anchor
     - Istanza del Wallet confronta le chiavi pubbliche out-of-band con quelle nell'Entity Configuration del Trust Anchor e scarta le chiavi non corrispondenti, registra le discrepanze e utilizza solo le corrispondenze.
   * - WP_018
     - Ciclo di vita, Trust, Sicurezza
     - Ristabilimento periodico del trust
     - Istanza del Wallet ottiene periodicamente e con successo una Wallet Attestation fresca dal suo Fornitore del Wallet.
   * - WP_019
     - Trust, Sicurezza
     - Contenuto Wallet Attestation
     - La Wallet Attestation contiene tutti i claim e punti dati richiesti che attestano l'integrità e lo stato di sicurezza del dispositivo.
   * - WP_019a
     - Trust, Sicurezza
     - Nessun attestato per Istanze del Wallet non verificate
     - Il Fornitore del Wallet rifiuta una richiesta di attestato da un'Istanza del Wallet che non supera i controlli di autenticità, integrità o genuinità.
   * - WP_019b
     - Trust, Sicurezza
     - Associazione attestato-chiave effimera
     - La Wallet Attestation contiene una chiave pubblica effimera generata dall'Istanza del Wallet e Istanza del Wallet è in grado di dimostrare la proprietà della chiave privata corrispondente.
   * - WP_020
     - Trust, Sicurezza
     - Firma Wallet Attestation
     - La Wallet Attestation è firmata digitalmente dal suo Fornitore del Wallet autorizzato, come ufficialmente elencato dall'Autorità di Registrazione supervisore.
   * - WP_021
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Sicurezza
     - Verifica sicurezza dispositivo
     - Istanza del Wallet non può essere attivata su un dispositivo che non soddisfa i requisiti minimi di sicurezza definiti dal Fornitore del Wallet.
   * - WP_022
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Sicurezza
     - Disponibilità API Key Attestation
     - Istanza del Wallet verifica e conferma la disponibilità delle Key Attestation API nel dispositivo (StrongBox/TEE o Secure Enclave/DeviceCheck).
   * - WP_023
     - Inizializzazione / Registrazione Wallet, Rilascio Wallet Attestation, Ciclo di vita, Trust
     - Scoperta federazione Fornitore del Wallet
     - Istanza del Wallet utilizza con successo gli Endpoint di Federation (``.well-known/openid-federation``, ``/fetch``) per recuperare metadata e configurazioni correnti del Fornitore del Wallet.
   * - WP_024
     - Inizializzazione / Attivazione Wallet, Ciclo di vita, Sicurezza
     - Consenso utente
     - Durante l'inizializzazione del Wallet, il Fornitore del Wallet ottiene esplicitamente il consenso dell'Utente prima di creare un account Utente.
   * - WP_025
     - Attivazione Wallet, Ciclo di vita, UX
     - Configurazione metodo sblocco Wallet
     - Istanza del Wallet richiede all'Utente di impostare il proprio metodo di sblocco preferito (PIN o biometrico), e quindi configura con successo il metodo scelto.
   * - WP_026
     - Rilascio Wallet Attestation, Ciclo di vita, Sicurezza
     - Coppia chiavi effimere per attestato
     - Per eseguire una Richiesta di Emissione della Wallet Attestation, Istanza del Wallet genera con successo una nuova coppia di chiavi asimmetriche effimere.
   * - WP_027
     - Rilascio Wallet Attestation, Ciclo di vita, Sicurezza
     - Verifica falla sicurezza dispositivo
     - Il Fornitore del Wallet verifica che il dispositivo soddisfi i suoi requisiti minimi di sicurezza e sia privo di falle di sicurezza note; se non è così, la Richiesta di Emissione della Wallet Attestation viene rifiutata.
   * - WP_028
     - Rilascio Wallet Attestation, Ciclo di vita, Sicurezza
     - Wallet Attestation a tempo limitato
     - quando non sono supportati metodi di controllo revoca, Il Fornitore del Wallet rilascia una Wallet Attestation con un tempo di scadenza definito e un periodo di validità breve.
   * - WP_029
     - Rilascio Wallet Attestation, Modello Dati e Ciclo di vita, Interoperabilità
     - Busta risposta HTTP 200 / JSON
     - Dopo la validazione riuscita della Richiesta di Emissione della Wallet Attestation, il Fornitore del Wallet restituisce un codice di stato 200 OK con Content-Type ``application/json``, nel cui payload si trova l'array ``wallet_attestations`` contenente le Wallet Attestation definite in `Wallet Attestation JWT <wallet-provider-endpoint.html#wallet-attestation-jwt>`_.
   * - WP_029a
     - Rilascio Wallet Attestation, Modello Dati e Ciclo di vita, Sicurezza
     - Formato della Wallet Attestation
     - Il Fornitore del Wallet fornisce la Wallet Attestation formato JWT firmato dal Fornitore del Wallet, come definito in `Wallet Attestation JWT <wallet-provider-endpoint.html#wallet-attestation-jwt>`.
   * - WP_029b
     - Rilascio Wallet Attestation, Modello Dati e Ciclo di vita, Sicurezza
     - Nessun PII nella Wallet Attestation
     - Il payload della Wallet Attestation non contiene informazioni personali sull'Utente.
   * - WP_030
     - Rilascio Wallet Attestation, Ciclo di vita, Sicurezza
     - Verifica integrità Wallet Attestation
     - Istanza del Wallet verifica la firma della Wallet Attestation ricevuta.
   * - WP_031
     - Rilascio Wallet Attestation, Trust, Sicurezza
     - Verifica trust Wallet Attestation
     - Istanza del Wallet verifica e conferma che l'emittente della Wallet Attestation (cioè, Fornitore del Wallet) è un membro fidato della Federazione, altrimenti la rifiuta come non valida.
   * - WP_032
     - Revoca Wallet, Ciclo di vita, Sicurezza
     - Revoca avviata dall'utente
     - L'Utente avvia con successo una revoca tramite la funzione di revoca integrata nell'Istanza del Wallet o tramite uno user agent esterno.
   * - WP_032a
     - Revoca Wallet, Ciclo di vita, Interoperabilità
     - Login utente al portale con 2FA
     - Per eseguire una revoca dell'Istanza del Wallet, l'Utente accede con successo al portale web del Fornitore del Wallet con ``2FA``.
   * - WP_032b
     - Revoca Wallet, Ciclo di vita, UX
     - Selezione utente di un'Istanza del Wallet da revocare
     - L'Utente visualizza lo stato delle proprie Istanze del Wallet e ne sceglie una da revocare.
   * - WP_033
     - Revoca Wallet, Ciclo di vita, Interoperabilità
     - Richiesta di Revoca Istanza del Wallet
     - Istanza del Wallet richiede la revoca di un'istanza specificata inviando una Richiesta di Revoca Istanza del Wallet all'Endpoint di Gestione dell'Istanza del Wallet.
   * - WP_034
     - Revoca Wallet, Ciclo di vita, Sicurezza
     - Avvisi revoca tempestivi
     - Il Fornitore del Wallet informa l'Utente entro 24 ore di una revoca dell'Istanza del Wallet.
   * - WP_034a
     - Revoca Wallet, Ciclo di vita, Sicurezza
     - Avvisi revoca out-of-band
     - Il Fornitore del Wallet notifica all'Utente una revoca dell'Istanza del Wallet attraverso un canale out-of-band (es. email o SMS).
   * - WP_034b
     - Revoca Wallet, Ciclo di vita, Sicurezza
     - Notifica revoca chiara con guida riattivazione
     - La notifica di revoca spiega chiaramente il motivo della revoca e fornisce passaggi attuabili per la riattivazione, se applicabile.
   * - WP_035
     - Ciclo di vita, Sicurezza
     - Gestione errori per gestione Istanza del Wallet
     - Quando si verifica un qualsiasi errore durante il flusso Registrazione/Inizializzazione dell'Istanza del Wallet, o durante richieste Recupero Stato e Revoca, il Fornitore del Wallet restituisce una risposta di errore all'Istanza del Wallet che è conforme agli standard definiti in :rfc:`7231` (per il codice stato HTTP) e :rfc:`7807` (per la descrizione del problema).
   * - WP_035a
     - Ciclo di vita, Interoperabilità
     - Formato risposta errore standard
     - La risposta di errore restituita dal Fornitore del Wallet include un header ``Content-Type`` di ``application/json`` e un corpo JSON contenente i parametri obbligatori ``error`` e ``error_description``.
   * - WP_036
     - Ciclo di vita, Interoperabilità
     - Gestione richieste malformate (400)
     - Quando una richiesta è malformata o mancano parametri richiesti, il Fornitore del Wallet restituisce una risposta con codice stato HTTP (``400 Bad Request``) e con codice errore ``bad_request``.
   * - WP_037
     - Ciclo di vita, Interoperabilità
     - Errore validazione semantica (422)
     - Quando una richiesta è ben formata ma fallisce la validazione semantica, il Fornitore del Wallet restituisce una risposta opzionale con codice stato HTTP (``422 Unprocessable Content``) e con codice errore ``validation_error``.
   * - WP_038
     - Ciclo di vita, Interoperabilità
     - Errore server interno (500)
     - In caso di fallimento interno non gestito, il Fornitore del Wallet restituisce una risposta con codice stato HTTP (``500 Internal Server Error``) e con codice errore ``server_error``.
   * - WP_039
     - Ciclo di vita, Interoperabilità
     - Servizio non disponibile (503)
     - Quando il servizio è temporaneamente offline o incapace di gestire richieste, il Fornitore del Wallet restituisce una risposta con codice stato HTTP (``503 Service Unavailable``) e con codice errore ``temporarily_unavailable``.
   * - WP_040
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Interoperabilità
     - Fallimento inizializzazione (integrità dispositivo)
     - Quando una Richiesta di Inizializzazione Istanza del Wallet proviene da un dispositivo che non soddisfa i requisiti di sicurezza del provider, il provider restituisce una risposta ``403 Forbidden`` con codice errore ``integrity_check_error``.
   * - WP_041
     - Revoca Wallet, Ciclo di vita, Interoperabilità
     - Richiesta recupero non autorizzata (401)
     - Quando una richiesta recupero stato Istanza del Wallet è fatta senza credenziali di autenticazione valide, il Fornitore del Wallet restituisce una risposta con codice stato HTTP (``401 Unauthorized``) e con codice errore ``unauthorized``.
   * - WP_042
     - Revoca Wallet, Ciclo di vita, Interoperabilità
     - Richiesta recupero vietata (403)
     - Quando un Utente tenta di recuperare uno stato Istanza del Wallet per cui non ha permesso, il Fornitore del Wallet restituisce una risposta con codice stato HTTP (``403 Forbidden``) e con codice errore ``forbidden``.
   * - WP_043
     - Revoca Wallet, Ciclo di vita, Interoperabilità
     - Richiesta revoca non autorizzata (401)
     - Quando una Richiesta di Revoca di Istanza del Wallet è fatta senza credenziali di autenticazione valide, il Fornitore del Wallet restituisce una risposta con codice stato HTTP (``401 Unauthorized``) con codice errore ``unauthorized``.
   * - WP_044
     - Revoca Wallet, Ciclo di vita, Interoperabilità
     - Richiesta revoca vietata (403)
     - Quando un Utente tenta di revocare un'Istanza del Wallet per cui non ha permesso, il Fornitore del Wallet restituisce una risposta con codice stato HTTP (``403 Forbidden``) e con codice errore ``invalid_request``.


.. _wallet-credential-issuance-testcases:

Casi di Test per Fase di Issuance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Questa sezione elenca i casi di test dalle Sezioni:

- :ref:`credential-issuance:Emissione di Attestati Elettronici`
- `Trust Evaluation Mechanism <trust.html#trust-evaluation-mechanism>`_
- :ref:`credential-issuer-endpoint:Endpoint del Credential Issuer`


.. list-table::
   :class: longtable
   :widths: 15 15 20 55
   :header-rows: 1

   * - ID Caso di Test
     - Scopo
     - Descrizione
     - Risultato Atteso
   * - WP_045
     - Issuance, Interoperabilità
     - Scoperta Credential Issuer
     - Istanza del Wallet ottiene con successo la lista dei Credential Issuer fidati utilizzando il Catalogo degli Attestati Elettronici.
   * - WP_045a
     - Trust, Issuance, Interoperabilità
     - Recupero Catalogo degli Attestati Elettronici
     - Istanza del Wallet invia con successo una richiesta HTTP GET al Catalogue Endpoint contenente il Catalogo degli Attestati Elettronici, utilizzando il media type ``application/jose``.
   * - WP_046
     - Issuance, Interoperabilità
     - Scoprire Credential Issuer dinamicamente dai metadata federazione
     - Istanza del Wallet utilizza con successo gli Endpoint di Federazione (``.well-known/openid-federation``, ``/fetch``) per recuperare metadata e configurazioni correnti del Credential Issuer.
   * - WP_046a
     - Trust, Issuance, Sicurezza
     - Validare Trust Chain completa del Credential Issuer al Trust Anchor
     - Istanza del Wallet costruisce e verifica la Trust Chain completa dal Credential Issuer attraverso Intermediari fino al Trust Anchor radice, assicurandosi che ogni firma sia valida.
   * - WP_047
     - Issuance, Interoperabilità
     - Flusso Third-Party-Initiated: scansione e decodifica QR Credential Offer
     - In un flusso cross-device Third-Party-Initiated, l'Istanza del Wallet scansiona con successo il codice QR, e ottiene il parametro ``credential_offer`` o ``credential_offer_uri``.
   * - WP_048
     - Issuance, Interoperabilità
     - Flusso Third-Party-Initiated: parsing Credential Offer
     - In un flusso Third-Party-Initiated, l'Istanza del Wallet estrae e valida tutti i parametri richiesti presenti nell'oggetto Credential Offer.
   * - WP_049
     - Issuance, Interoperabilità
     - Flusso Issuer-Initiated: controllo identificativo dell'Authorization Server
     - Istanza del Wallet legge i metadata ``authorization_servers`` del Credential Issuer e trova l'identificativo dell'Authorization Server configurato in ``authorization_servers``.
   * - WP_050
     - Issuance, Interoperabilità
     - Flusso Issuer-Initiated: validazione ID degli Attestati Elettronici
     - Istanza del Wallet verifica se ogni identificativo di Attestato Elettronico nei ``credential_configuration_ids`` è supportato dal Credential Issuer; qualsiasi identificativo non supportato non viene preso in considerazione.
   * - WP_050a
     - Trust, Issuance, Interoperabilità
     - Applicazione Policy & Trust Marks
     - Istanza del Wallet verifica che il Credential Issuer sia autorizzato a rilasciare l'Attestato Elettronico richiesto attraverso l'applicazione delle policy di metadata e la verifica dei Trust Marks.
   * - WP_050b
     - Trust, Issuance, Interoperabilità
     - Conferma ID supportato
     - Istanza del Wallet verifica che ogni ``credential_configuration_id`` richiesto appaia nei metadata ``credential_configurations_supported`` del Credential Issuer; ID mancanti causano il fallimento dell'offerta.
   * - WP_051
     - Issuance, Interoperabilità
     - Richiesta Attestato Elettronico utilizzando Flusso OAuth 2.0 Code
     - Istanza del Wallet richiede con successo PID/(Q)EAA dal Fornitore PID/(Q)EAA utilizzando il Flusso Authorization Code come in `OpenID4VCI`_.
   * - WP_052
     - Issuance, Interoperabilità
     - Richiesta PAR: costruzione payload
     - Istanza del Wallet genera un nuovo PKCE ``code_verifier``, JWT PoP Wallet Attestation, e valore ``state``, quindi li avvolge in un Request Object firmato con la sua chiave privata (:rfc:`9126`), e lo invia al PAR Endpoint.
   * - WP_052a
     - Issuance, Interoperabilità
     - Generazione sicura ``code_verifier`` PKCE
     - Istanza del Wallet crea il ``code_verifier`` seguendo le raccomandazioni contenute in :rfc:`7636`, come stringa casuale ad alta entropia utilizzando caratteri non riservati con lunghezza tra 43 e 128.
   * - WP_052b
     - Issuance, Interoperabilità
     - Creazione JWT PoP Wallet Attestation
     - Istanza del Wallet genera il JWT PoP Wallet Attestation (per parametri ``OAuth-Client-Attestation-PoP`` come definito in `OAUTH-ATTESTATION-CLIENT-AUTH`_) e include, nel payload, la chiave pubblica effimera referenziata nel ``cnf.jwk`` della Wallet Attestation.
   * - WP_052c
     - Issuance, Sicurezza
     - Firma JWT PoP Wallet Attestation
     - Istanza del Wallet firma il JWT PoP con la chiave privata effimera corrispondente alla chiave pubblica valorizzata nel parametro ``cnf.jwk`` della Wallet Attestation.
   * - WP_052d
     - Issuance, Interoperabilità
     - Specificare tipi degli Attestati Elettronici
     - Istanza del Wallet incorpora i tipi degli Attestati Elettronici nel Request Object utilizzando il parametro ``authorization_details`` (o ``scope``) (per RAR :rfc:`9396`).
   * - WP_053
     - Issuance, Sicurezza
     - Authorization Request
     - Istanza del Wallet invia una PAR all'Authorization Endpoint del Credential Issuer utilizzando il ``request_uri`` e ``client_id`` ricevuti.
   * - WP_053a
     - Issuance, Sicurezza
     - Uso di un unico ``request_uri``
     - Istanza del Wallet invia l'Authorization Request con un ``request_uri`` appena ottenuto, e il Fornitore di Attestati Elettronici verifica che il ``request_uri`` non è stato usato precedentemente.
   * - WP_054
     - Issuance, Interoperabilità
     - Validare l'Authorization Response: parametro richiesto
     - Istanza del Wallet verifica che l'Authorization Response contenga tutti i parametri richiesti (``code``, ``state``, e ``iss``); se vi sono parametri mancanti viene segnalato un errore.
   * - WP_054a
     - Issuance, Sicurezza
     - Validare l'Authorization Response: verificare corrispondenza state
     - Istanza del Wallet confronta il valore ``state`` restituito con quello originariamente inviato nel Request Object (:rfc:`6749`) e continua solo se corrispondono.
   * - WP_054b
     - Issuance, Sicurezza
     - Validare l'Authorization Response: confermare identità Credential Issuer
     - Istanza del Wallet verifica che il parametro ``iss`` nell'Authorization Response corrisponda all'identificativo del Credential Issuer con cui ha iniziato la comunicazione (:rfc:`9207`).
   * - WP_055
     - Issuance, Interoperabilità
     - Inviare una Token Request
     - Istanza del Wallet invia una richiesta POST al Token Endpoint con URL-encoded body, includendo il ``code`` ricevuto (nell'Authorization Response), lo stesso ``redirect_uri`` (nel Request Object), e il ``code_verifier``.
   * - WP_055a
     - Issuance, Interoperabilità
     - Parametri prova Token Request
     - La Token Request porta le prove richieste negli header: un JWT prova DPoP, un JWT Wallet Attestation, e JWT PoP dell'Istanza del Wallet (per ``OAuth-Client-Attestation`` e ``OAuth-Client-Attestation-PoP`` come definito in `OAUTH-ATTESTATION-CLIENT-AUTH`_).
   * - WP_055b
     - Issuance, Interoperabilità
     - Generare coppia chiavi/prova DPoP
     - Istanza del Wallet genera una nuova coppia chiavi DPoP e un DPoP JWT seguendo le istruzioni fornite in :rfc:`9449#section-4` per la Token Request al Credential Issuer.
   * - WP_055c
     - Issuance, Sicurezza
     - Firmare prova DPoP
     - Istanza del Wallet firma il DPoP-JWT con la chiave privata DPoP generata precedentemente.
   * - WP_055d
     - Issuance, Interoperabilità
     - Parametri PoP Wallet Attestation nella Token Request
     - ``OAuth-Client-Attestation-PoP`` è firmato utilizzando la chiave privata associata alIstanza del Wallet, dove la sua chiave pubblica correlata è fornita all'interno del Wallet Attestation (claim ``cnf.jwk``).
   * - WP_056
     - Issuance, Interoperabilità
     - Richiesta Attestato Elettronico
     - Istanza del Wallet invia una richiesta POST al Credential Endpoint includendo l'Access Token, il DPoP-JWT, tipo Attestato Elettronico (``credential_identifier``), e il PoP valido della chiave associata all'Attestato Elettronico.
   * - WP_056a
     - Issuance, Sicurezza
     - Recuperare nonce per la dimostrazione di possesso chiave per Issuance di Attestato Elettronico
     - Istanza del Wallet invia una richiesta POST al Nonce Endpoint del Credential Issuer e ottiene un nuovo nonce, che viene poi utilizzato per generare una PoP del materiale crittografico che verrà associato all'Attestato Elettronico rilasciata.
   * - WP_056b
     - Issuance, Sicurezza
     - Prova DPoP fresca
     - Istanza del Wallet genera una prova DPoP fresca con la stessa chiave utilizzata per il DPoP-JWT della Token Request, e in accordo con :rfc:`9449#section-4`.
   * - WP_056c
     - Issuance, Sicurezza
     - Abbinare la prova chiave Attestato Elettronico alla chiave DPoP
     - Istanza del Wallet include un oggetto JSON come valore del parametro ``proofs`` nella Credential Request. Al suo interno sono è presente l'array ``jwt``. Quest'ultimo è valorizzato con uno o più JWT i cui parametro dell'header ``jwk`` rappresenta la prova il possesso della chiave pubblica referenziata nel DPoP-JWT della Token Request.
   * - WP_057
     - Issuance, Interoperabilità
     - Richiesta di Attestati Elettronici multipli
     - Quando un Credential Issuer offre Attestati Elettronici multipli, Istanza del Wallet fa una Credential Request separata e per ogni Attestato Elettronico che intende ottenere.
   * - WP_058
     - Issuance, Interoperabilità
     - Richiesta Attestato Elettronico in Batch
     - In caso di Batch Issuance, Istanza del Wallet invia una Credential Request in batch al Credential Endpoint che include: l'Access Token, un JWT prova DPoP, il tipo di Attestato Elettronico, e un parametro ``proofs`` contenente tutte le PoP delle chiavi private le cui pubbliche corrispondenti sono da associare all'Attestato Elettronico.
   * - WP_058a
     - Issuance, Sicurezza
     - Batch Issuance: generazione chiavi
     - In caso di Batch Issuance, Istanza del Wallet genera un numero di nuove coppie chiavi uguale al valore ``batch_size``.
   * - WP_058b
     - Issuance, Interoperabilità
     - Batch Issuance: PoP delle chiavi Attestati Elettronici batch
     - In caso di Batch Issuance, Istanza del Wallet genera N prove di possesso (PoP) di chiave utilizzando il ``c_nonce`` fornito, una per ogni Attestato Elettronico nel batch, dove N uguale al valore ``batch_size``.
   * - WP_059
     - Issuance, Interoperabilità
     - Validare la Credential Response per parametri richiesti
     - Istanza del Wallet ispeziona il payload Credential Response, verificando che tutti i parametri PID/(Q)EAA obbligatori siano presenti e validi come definito in :ref:`Table of Credential Response <table_credential_response_claim>`; se qualsiasi parametro è mancante o non valido, rifiuta la risposta con un errore.
   * - WP_060
     - Issuance, Interoperabilità
     - Verificare tipo/schema di un Attestato Elettronico
     - Istanza del Wallet recupera l'Attestato Elettronico rilasciata dal claim ``credential`` della risposta, verifica che il suo tipo corrisponda al tipo richiesto, e valida lo schema contro :ref:`credential-data-model:Modello di Dati degli Attestati Elettronici`; se uno dei controlli fallisce, rifiuta l'Attestato Elettronico.
   * - WP_061
     - Issuance, Sicurezza
     - Validare Trust Chain Credential Issuer
     - Istanza del Wallet verifica la Trust Chain del Fornitore di Attestati che ha emesso l'Attestato Elettronico usando i parametri presenti nel header dell'Attestato Elettronico stesso.
   * - WP_062
     - Issuance, Interoperabilità
     - Verifica Attestato Elettronico per formato
     - Istanza del Wallet verifica se un Attestato Elettronico è in formato SD-JWT VC o mdoc-CBOR, e quindi esegue le verifiche appropriate. Se queste ultime falliscono, Istanza del Wallet rifiuta l'Attestato Elettronico.
   * - WP_062a
     - Issuance, Sicurezza, Interoperabilità
     - Verificare integrità Attestato Elettronico SD-JWT
     - Istanza del Wallet ottiene i valori ``alg`` e ``kid`` dall'header SD-JWT, recupera la chiave pubblica corrispondente, e ne verifica la firma; se la verifica fallisce, l'Attestato Elettronico in formato SD-JWT viene rifiutato.
   * - WP_062b
     - Issuance, Sicurezza, Interoperabilità
     - Verificare integrità Attestato Elettronico mdoc-CBOR
     - Istanza del Wallet estrae l'algoritmo di firma dall'header protetto del ``COSE_Sign1`` mdoc-CBOR, recupera la chiave pubblica del Credential Issuer dal ``kid`` o ``x5chain`` nell'header non protetto, e verifica la firma COSE sull'MSO; se non valida, l'Attestato Elettronico viene rifiutata.
   * - WP_063
     - Issuance, Privacy
     - Consenso utente per archiviazione Attestato Elettronico
     - Istanza del Wallet richiede il consenso dell'Utente e archivia l'Attestato Elettronico solo dopo approvazione esplicita.
   * - WP_064
     - Issuance, Interoperabilità
     - Gestione Notifiche
     - Istanza del Wallet invia una richiesta HTTP POST al Notification Endpoint con ``Content-Type: application/json``.
   * - WP_064a
     - Issuance, Interoperabilità
     - Parametri Notifica
     - Il payload Notification Request contiene il ``notification_id`` dalla Credential Response e il parametro ``event`` valorizzato ``credential_accepted``, ``credential_deleted``, o ``credential_failure``; può anche includere un ``event_description`` ASCII valido.
   * - WP_064b
     - Issuance, Privacy
     - Proteggere privacy Utente nel contenuto notifica
     - L'``event_description`` contiene solo testo generico, neutrale per l'Utente e non rivela comportamento Utente o stato dispositivo.
   * - WP_065
     - Issuance, Sicurezza
     - Gestire defererd Issuance
     - Istanza del Wallet valuta la Credential Response; se contiene sia ``transaction_id`` che ``interval``, Istanza del Wallet riconosce il flusso come defererd Issuance.
   * - WP_066
     - Issuance, Interoperabilità
     - Richiesta defererd Issuance dopo interval
     - Istanza del Wallet invia una Deferred Credential Response solo dopo che il ``interval`` richiesto è passato.
   * - WP_066a
     - Issuance, Interoperabilità
     - Richiesta defererd Issuance con transaction_id
     - Istanza del Wallet invia una Deferred Credential Response come HTTP POST con ``Content-Type: application/json``, e il corpo richiesta contiene il ``transaction_id`` richiesto.
   * - WP_066b
     - Issuance, Interoperabilità
     - Richiesta defererd con Access Token ancora valido
     - Istanza del Wallet include l'Access Token esistente nella richiesta differita se il valore parametro ``interval`` è inferiore al tempo di scadenza impostato per l'Access Token.
   * - WP_066c
     - Issuance, Interoperabilità
     - Nuovo Access Token DPoP-bound tramite Refresh
     - Quando l'Access Token esistente scadrebbe prima che la richiesta differita possa essere fatta, Istanza del Wallet ottiene un nuovo Access Token DPoP-bound tramite il flusso Refresh Token.
   * - WP_067
     - Issuance, Interoperabilità
     - Nuovo flusso Issuance Attestato Elettronico
     - Quando Istanza del Wallet fallisce nel rinnovare un Access Token in scadenza, avvia un flusso Issuance Attestato Elettronico completamente nuovo.
   * - WP_068
     - Issuance, Interoperabilità
     - Richiesta Refresh Token
     - Istanza del Wallet invia una richiesta POST al Token Endpoint del Credential Issuer con ``grant_type=refresh_token``, un ``refresh_token`` valido, un header DPoP contenente un DPoP-JWT fresco, e un ``OAuth-Client-Attestation`` header contenente la Wallet Attestation un header ``OAuth-Client-Attestation-JWT`` contenente la PoP della chiave privata associata alla Wallet Attestation.
   * - WP_068a
     - Issuance, Sicurezza
     - Refresh Token: generare prove
     - Per una richiesta refresh Access Token, Istanza del Wallet genera un nuovo JWT DPoP e un nuovo PoP Wallet Attestation, e li include nella richiesta.
   * - WP_068b
     - Issuance, Interoperabilità
     - Refresh Token: mantenere associazione
     - Istanza del Wallet riutilizza la stessa chiave associata al PoP Wallet Attestation e alla DPoP-JWT dalla richiesta Access Token originale, assicurandosi che l'Access Token rinnovato rimanga crittograficamente associato al DPoP-JWT e valido.
   * - WP_069
     - Issuance, Sicurezza
     - Controllo stato di un Attestato Elettronico
     - Istanza del Wallet verifica lo stato di ogni Attestato Elettronico archiviato recuperando e validando un Status List Token (per :ref:`credential-revocation:Token di Status List`).
   * - WP_070
     - Issuance, Sicurezza
     - Flusso re-Issuance: rilevare necessità re-Issuance (aggiornare stato)
     - Istanza del Wallet aggiorna un Attestato Elettronico quando la Status List mostra ``0x03`` (``UPDATE``) o ``0x0F`` (``ATTRIBUTE_UPDATE``) per quell'Attestato Elettronico.
   * - WP_071
     - Issuance, Sicurezza
     - Flusso re-Issuance: verificare validità Access Token per re-Issuance
     - Quando viene rilevato un aggiornamento per un Attestato Elettronico, Istanza del Wallet verifica la validità dell'Access Token associato. Se il token è valido, Istanza del Wallet procede con la re-Issuance dell'Attestato Elettronico.
   * - WP_071a
     - Issuance, Sicurezza
     - Flusso re-Issuance: rinnovare Access Token scaduto
     - Se l'Access Token è scaduto ma è disponibile un Refresh Token valido, Istanza del Wallet avvia un flusso Refresh Token per ottenere un nuovo Access Token DPoP-bound, seguendo il Flusso Refresh Token.
   * - WP_071b
     - Issuance, Sicurezza
     - Riavviare rilascio su scadenza completa
     - Istanza del Wallet ri-autentica l'Utente quando avvia un nuovo flusso di Issuance.
   * - WP_072
     - Issuance, Sicurezza
     - Recuperare Attestato Elettronico aggiornato
     - Istanza del Wallet, con un Access Token DPoP-bound valido, invia una richiesta al Credential Endpoint e recupera con successo l'Attestato Elettronico aggiornato.
   * - WP_073
     - Issuance, Sicurezza e Privacy
     - Eliminare vecchie Attestati Elettronici
     - Dopo aver archiviato un nuovo Attestato Elettronico, Istanza del Wallet elimina la versione precedente in modo che solo l'ultimo Attestato Elettronico rimanga archiviato.
   * - WP_073a
     - Issuance, Sicurezza e Privacy
     - Eliminare vecchie Attestati Elettronici batch
     - Quando Istanza del Wallet riceve e archivia un nuovo batch dello stesso Attestato Elettronico con gli stessi claim, elimina gli Attestati Elettronici del batch precedente.
   * - WP_074
     - Issuance, UX
     - Consenso su nuovo archivio Attestato Elettronico con aggiornamento ``user_attribute``
     - Se l'aggiornamento Attestato Elettronico coinvolge cambiamenti ai valori degli Attributi dell'Utente (``attribute_update``), Istanza del Wallet richiede il consenso dell'Utente prima di archiviare il nuovo Attestato Elettronico aggiornato.
   * - WP_075
     - Issuance, UX
     - Nessun consenso su nuovo archivio Attestato Elettronico senza aggiornamento ``user_attribute``
     - Se l'aggiornamento Attestato Elettronico riguarda solo dei cambiamenti nei metadata dell'Attestato Elettronico (``update``), Istanza del Wallet archivia automaticamente il nuovo Attestato Elettronico aggiornato senza richiedere consenso aggiuntivo dall'Utente.

.. _wallet-credential-presentation-testcases:

Casi di Test per Fase di Presentazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Questa sezione elenca i casi di test dalla Sezione :ref:`credential-presentation:Presentazione dell'Attestato Elettronico`,
coprendo sia le fasi di presentazione **Flusso Remoto** che **Flusso di Prossimità**.


.. list-table::
   :class: longtable
   :widths: 15 15 20 55
   :header-rows: 1

   * - ID Caso di Test
     - Scopo
     - Descrizione
     - Risultato Atteso
   * - WP_076
     - Flusso-remoto, Presentazione, Interoperabilità
     - Ottenere URL dell'Authorization Request nel flusso Same Device
     - Nel flusso Same Device, Istanza del Wallet ottiene con successo un URL ed estrae i seguenti parametri: ``client_id``, ``request_uri``, ``state``, e ``request_uri_method``.
   * - WP_077
     - Flusso-remoto, Presentazione, Interoperabilità
     - Ottenere URL dell'Authorization Request nel flusso Cross Device
     - Nel flusso Cross Device, Istanza del Wallet scansiona e analizza con successo un Codice QR per estrarre i seguenti parametri: ``client_id``, ``request_uri``, ``state``, e ``request_uri_method``.
   * - WP_078
     - Flusso-remoto, Trust, Presentazione, Interoperabilità
     - Scoperta identità Relying Party
     - Istanza del Wallet utilizza con successo gli Endpoint di Federazione (``.well-known/openid-federation``, ``/fetch``) per recuperare metadata e configurazioni correnti della Relying Party.
   * - WP_079
     - Flusso-remoto, Trust, Presentazione, Interoperabilità
     - Valutazione Trust Chain Relying Party
     - Istanza del Wallet valida con successo la Trust Chain della Relying Party (fornita staticamente o costruita attraverso un processo Federation Entity Discovery) dal Trust Anchor fino alla Relying Party stessa, confermando che la Relying Party è un membro riconosciuto e fidato della Federazione.
   * - WP_080
     - Flusso-remoto, Trust, Presentazione, Interoperabilità
     - Controllo Trust Mark Relying Party
     - Istanza del Wallet valuta con successo qualsiasi Trust Mark incluso nell'Entity Configuration della Relying Party per assicurare che siano validi e indichino conformità alle policy della Federazione.
   * - WP_081
     - Flusso-remoto, Trust, Presentazione, Sicurezza
     - Validare ``request_uri``
     - Istanza del Wallet controlla che il ``request_uri`` sia nella lista di URI consentiti alla Relying Party (dai ``openid_credential_verifier.request_uris`` nella Trust Chain) e procede solo quando trova una corrispondenza esatta; se non viene trovata corrispondenza, rifiuta la richiesta.
   * - WP_082
     - Flusso-remoto, Presentazione, Interoperabilità
     - GET Request Object
     - Se il ``request_uri_method`` nella richiesta iniziale è ``get`` o è assente, Istanza del Wallet invia una richiesta HTTP GET al ``request_uri`` Endopint della Relying Party, e recupera con successo un JWT Request Object firmato.
   * - WP_083
     - Flusso-remoto, Presentazione, Interoperabilità
     - POST Request Object
     - Se il ``request_uri_method`` nella richiesta iniziale è ``post``, Istanza del Wallet invia una richiesta HTTP POST al ``request_uri`` Endpoint della Relying Party, includendo i suoi metadata come parametri ``wallet_metadata`` e ``wallet_nonce``, con content type ``application/x-www-form-urlencoded``, e recupera con successo un JWT Request Object firmato.
   * - WP_083a
     - Flusso-remoto, Presentazione, Interoperabilità
     - Costruire ``wallet_metadata``
     - Istanza del Wallet formatta il ``wallet_metadata`` come oggetto JSON che include ``vp_formats_supported``, opzionalmente ``client_id_prefixes_supported`` e ``request_object_signing_alg_values_supported`` per Sezione 10.1 di [`OpenID4VP`_].
   * - WP_083b
     - Flusso-remoto, Presentazione, Privacy
     - Escludere PII in ``wallet_metadata``
     - Il JSON ``wallet_metadata`` non contiene campi identificabili dall'utente o specifici del dispositivo (es. nomi, dettagli hardware).
   * - WP_083c
     - Flusso-remoto, Presentazione, Sicurezza
     - Generare nonce replay
     - Un nuovo ``wallet_nonce`` viene generato e incluso nel payload della richiesta POST insieme al ``wallet_metadata`` per mitigare attacchi di replay.
   * - WP_084
     - Flusso-remoto, Trust, Presentazione, Sicurezza
     - Recupero chiave pubblica Relying Party
     - Istanza del Wallet recupera la chiave pubblica corretta della Relying Party dal campo ``metadata.openid_credential_verifier.jwks``, situato all'interno dell'Entity Configuration della Relying Party fornita dalla Trust Chain, utilizzando l'identificativo di chiave (``kid``) dall'header del Request Object.
   * - WP_085
     - Flusso-remoto, Presentazione, Sicurezza
     - Verifica firma Request Object
     - Istanza del Wallet conferma l'integrità del Request Object firmato eseguendo con successo la validazione della firma crittografica usando la chiave pubblica della Relying Party.
   * - WP_086
     - Flusso-remoto, Presentazione, Sicurezza
     - Abbinare ``client_id`` tra contesti
     - Istanza del Wallet conferma che il claim ``iss`` nel Request Object firmato abbia lo stesso ``client_id`` che ha originariamente estratto dall'URL dell'Authorization Request che il valore ``sub`` nell'Entity Configuration della Relying Party. Qualsiasi discrepanza causa il rifiuto dell Request Object.
   * - WP_087
     - Flusso-remoto, Presentazione, Sicurezza
     - Controllare idoneità Relying Party
     - Istanza del Wallet autorizza la richiesta e procede con il flusso quando verifica che i metadata, le policy e un Trust Mark valido della Relying Party consentono a quest'ultima di richiedere l'Attestato Elettronico specificato.
   * - WP_088
     - Flusso-remoto, Presentazione, Privacy
     - Consenso utente per divulgazione
     - Istanza del Wallet richiede il consenso dell'Utente presentando una schermata UI che mostra chiaramente l'identità verificata della Relying Party e un elenco di tutti gli Attributi richiesti.
   * - WP_089
     - Flusso-remoto, Presentazione, UX
     - Gestire errori endpoint ``request_uri``
     - Quando l'endpoint ``request_uri`` della Relying Party risponde con un errore, Istanza del Wallet mostra all'Utente un messaggio chiaro e leggibile, spiegando il motivo del fallimento e termina il flusso in modo sicuro.
   * - WP_089a
     - Flusso-remoto, Presentazione, UX
     - Registrare errori ``request_uri``
     - Istanza del Wallet registra internamente le informazioni dettagliate dell'errore.
   * - WP_089b
     - Flusso-remoto, Presentazione, UX
     - Recuperare da errori ``request_uri``
     - Per un errore recuperabile, come ``server_error``, Istanza del Wallet richiede all'Utente un'azione di recupero specifica, come suggerire un retry o opzione "Scansiona QR di nuovo", se possibile.
   * - WP_090
     - Flusso-remoto, Presentazione, Interoperabilità
     - Notificare Relying Party su richiesta non valida
     - Se il Request Object è non valido o ne fallisse la verifica, Istanza del Wallet invia una Authorization Error Response tramite HTTP POST al Response Endpoint (``response_uri``) della Relying Party.
   * - WP_091
     - Flusso-remoto, Presentazione, Interoperabilità
     - Inviare l'Authorization Response
     - Se la verifica Request Object è valida, Istanza del Wallet invia una Authorization Response tramite HTTP POST al Response Endpoint (``response_uri``) della Relying Party.
   * - WP_091a
     - Flusso-remoto, Presentazione, Sicurezza
     - Validare ``response_uri``
     - Prima di inviare l'Authorization Response, Istanza del Wallet conferma che il ``response_uri`` corrisponda esattamente a uno dei ``response_uris`` attestati della Relying Party nei suoi metadata; una mancata corrispondenza interrompe il flusso.
   * - WP_092
     - Flusso-remoto, Presentazione, Sicurezza
     - Cifrare l'Authorization Response
     - Istanza del Wallet cifra il JWT dell'Authorization Response per Sezione 8.3 di [`OpenID4VP`_] utilizzando la chiave pubblica della Relying Party.
   * - WP_093
     - Flusso-remoto, Presentazione, Sicurezza
     - Costruire ``vp_token`` con ``state``
     - Il payload JWT dell'Authorization Response include il valore ``state`` originale e un parametro ``vp_token`` contenetne un oggetto le cui coppie chiave-valore corrispondono agli Attestati Elettronici richiesti.
   * - WP_093a
     - Flusso-remoto, Presentazione, Interoperabilità
     - Includere presentazioni firmate
     - All'interno di quel ``vp_token``, ci sono gli Attestati Elettronici richiesti in formato SD JWT VC.
   * - WP_093b
     - Flusso-remoto, Presentazione, Sicurezza
     - Aggiungere Key Binding JWT
     - Istanza del Wallet genera per ogni singola presentazione SD-JWT all'interno del ``vp_token``, il corrispondente Key Binding JWT.
   * - WP_093c
     - Flusso-remoto, Presentazione, Sicurezza
     - Formato Key Binding JWT
     - L'header JOSE di ogni Key Binding JWT generato includeil parametro ``typ`` valorizzato con ``kb+jwt`` e un parametro ``alg`` valorizzato con uno degli algoritmi di firma supportati. Il payload include i parametri ``iat``, ``aud``, ``nonce``, e ``sd_hash`` come definito in `OpenID4VP`_.
   * - WP_094
     - Flusso-remoto, Presentazione, Interoperabilità
     - Eseguire redirect user-agent
     - Dopo aver ricevuto il ``redirect_uri``, Istanza del Wallet esegue con successo un redirect dello user-agent al ``redirect_uri`` fornito dalla Relying Party, così la Relying Party può riprendere l'interazione sullo stesso dispositivo che ha iniziato il flusso.
   * - WP_094a
     - Flusso-remoto, Trust, Presentazione, Sicurezza
     - Validare ``redirect_uri``
     - Istanza del Wallet verifica che il ``redirect_uri`` corrisponda esattamente a uno degli URI elencati nei metadata ``redirect_uris`` della Relying Party. Se non corrisponde, interrompe il flusso.
   * - WP_095
     - Flusso-prossimità, Presentazione, Sicurezza
     - Supportare recupero supervisionato/non supervisionato
     - Istanza del Wallet supporta una presentazione di Attestato Elettronico utilizzando il metodo Supervised Device Retrieval per uno scenario di verifica in presenza con supervisione umana e tramite Device Retrieval (non supervisionato) per verifica automatizzata senza supervisione umana.
   * - WP_096
     - Flusso-prossimità, Presentazione, Sicurezza
     - Supporto meccanismi Device Retrieval
     - Istanza del Wallet supporta i meccanismi Device Retrieval tramite Bluetooth Low Energy (BLE) o NFC.
   * - WP_096a
     - Flusso-prossimità, Presentazione, Sicurezza
     - Applicare solo device retrieval
     - Istanza del Wallet rifiuta qualsiasi richiesta di iniziare un flusso prossimità utilizzando il meccanismo Server Retrieval.
   * - WP_096b
     - Flusso-prossimità, Presentazione, Sicurezza
     - Supportare device retrieval BLE/NFC (condizionale)
     - Istanza del Wallet completa con successo il flusso di recupero BLE o NFC. Il supporto BLE è obbligatorio, mentre NFC è RACCOMANDATO. Almeno un metodo di device retrieval (BLE o NFC) deve essere supportato; il fallimento costituisce non conformità.
   * - WP_097
     - Flusso-prossimità, Presentazione, UX
     - Meccanismi DeviceEngagement supportati
     - Istanza del Wallet supporta DeviceEngagement basato su codice QR o NFC Connection Handover.
   * - WP_097a
     - Flusso-prossimità, Presentazione, Sicurezza
     - Supporto QR/NFC engagement (condizionale)
     - Istanza del Wallet completa una transazione di recupero dati sia via BLE che via NFC (quando l’hardware è disponibile). Il supporto QR è obbligatorio, mentre NFC è RACCOMANDATO. Almeno un metodo di engagement (QR o NFC) deve essere supportato; il fallimento costituisce non conformità.
   * - WP_098
     - Flusso-prossimità, Presentazione, Sicurezza
     - Autenticazione Relying Party
     - Istanza del Wallet supporta ed esegue l'Autenticazione dell'Istanza Relying Party in conformità al processo di Reader Authentication `ISO18013-5`_.
   * - WP_099
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Supporto mDL domestico
     - Istanza del Wallet supporta e processa senza errore Attestati Elettronici mDL utilizzando le definizioni standard `ISO18013-5`_ ed eventuali aggiunte nel namespace domestico di IT Wallet (vedi `mdoc-CBOR Credential Format <credential-data-model.html#mdoc-cbor-credential-format>`_ per maggiori dettagli).
   * - WP_100
     - Flusso-prossimità, Presentazione, Sicurezza
     - Autenticazione WSCA
     - Istanza del Wallet richiede all'Utente di eseguire un’autenticazione basata su WSCA, direttamente o sbloccando l'applicazione, e non procede con il flusso prossimità finché non ha successo.
   * - WP_101
     - Flusso-prossimità, Presentazione, Sicurezza
     - Generare coppia chiavi EC effimere
     - Istanza del Wallet genera con successo una nuova coppia di chiavi curva ellittica effimere (per la cipher suite `ISO18013-5`_ scelta).
   * - WP_102
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Codifica CBOR dei dati DeviceEngagement
     - DeviceEngagement è codificato CBOR e contiene i parametri ``Version``, ``Security``, ``Capabilities`` e ``OriginInfos`` (può essere vuoto). Per QR engagement include anche ``DeviceRetrievalMode-BLEOptions`` e/o ``DeviceRetrievalMode-NFCOptions``. Per NFC engagement, tali opzioni sono omesse.
   * - WP_102a
     - Flusso-prossimità, Presentazione, Interoperabilità
     - DeviceEngagement via QR
     - L'URI mdoc: QR codifica un DeviceEngagement valido in CBOR (per Sezione 9.1 di [`ISO18013-5`_]) usando base64url-without-padding (:rfc:`4648`).
   * - WP_102b
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Verificare parametro Security
     - Il parametro ``Security`` all'interno dei dati DeviceEngagement contiene un identificativo cipher suite supportato e la chiave pubblica effimera dell'Istanza del Wallet per `ISO18013-5`_ Tabella 22.
   * - WP_102c
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Verificare parametro ``DeviceRetrievalMode-BLEOptions``
     - Il parametro ``DeviceRetrievalMode-BLEOptions`` all'interno dei dati DeviceEngagement indica Central Client Mode e porta l'UUID dispositivo corretto.
   * - WP_102d
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Verificare parametro ``DeviceRetrievalMode-NFCOptions``
     - Il parametro DeviceRetrievalMode-NFCOptions dichiara ruolo supportato (PICC per Istanza del Wallet) e dimensioni massime comando/risposta APDU per mappatura ISO.
   * - WP_102e
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Verificare parametro ``Capabilities``
     - Il parametro ``Capabilities`` all'interno dei dati DeviceEngagement imposta correttamente i parametri ``HandoverSessionEstablishmentSupport`` e ``ReaderAuthAllSupport``.
   * - WP_102f
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Verificare parametro ``OriginInfos``
     - Se presente, il parametro ``OriginInfos`` nei dati DeviceEngagement è correttamente codificato come array (che può essere vuoto).
   * - WP_103
     - Flusso-prossimità, Presentazione, UX
     - DeviceEngagement via NFC (Connection Handover)
     - Istanza del Wallet espone DeviceEngagement tramite NFC Connection Handover (Statico o Negoziato).
   * - WP_103a
     - Flusso-prossimità, Presentazione, Interoperabilità
     - NFC Connection Handover (Statico)
     - Istanza del Wallet agisce come NFC Tag (Tipo 4) e fornisce un Handover Select con almeno un Alternative Carrier Record e relativo Carrier Configuration Record; un Auxiliary Data Record trasporta il DeviceEngagement (tipo ``iso.org:18013:deviceengagement``, id "mdoc").
   * - WP_103b
     - Flusso-prossimità, Presentazione, Interoperabilità
     - NFC Connection Handover (Negoziato)
     - Istanza del Wallet espone il servizio ``urn:nfc:sn:handover``; su Handover Request restituisce un Handover Select con esattamente un carrier selezionato e il DeviceEngagement ausiliario.
   * - WP_103c
     - Flusso-prossimità, Presentazione, Sicurezza, Interoperabilità
     - ``SessionEstablishment`` anticipato via TNEP
     - Se ``HandoverSessionEstablishmentSupport`` è ``true`` nel DeviceEngagement, Istanza del Wallet accetta il ``SessionEstablishment`` anticipato sul servizio TNEP annunciato e successivamente verifica che corrisponda a quello ricevuto durante il recupero dati.
   * - WP_103d
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Codifica Carrier Configuration Record
     - Istanza del Wallet include correttamente un Carrier Configuration Record per ogni carrier supportato: per NFC (tipo ``iso.org:18013:nfc``, ID ``nfc``)  per Sezione 9.2.2 di [`ISO18013-5`_]; per BLE per Sezione 11.1.2 di [`ISO18013-5`_].
   * - WP_103e
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Auxiliary Data Record per DeviceEngagement
     - Istanza del Wallet fornisce un Auxiliary Data Record che trasporta il DeviceEngagement (tipo ``iso.org:18013:deviceengagement``, ID ``mdoc``) utilizzando NFC Forum external type (0x04); ogni Alternative Carrier Record DEVE fare riferimento a questo record.
   * - WP_103f
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Alternative Carrier Records
     - In Static Handover, l’Handover Select include uno o più Alternative Carrier Records; in Negotiated Handover contiene esattamente un carrier selezionato. L’Alternative Carrier NFC referenzia il Carrier Configuration Record ``nfc``.
   * - WP_103g
     - Flusso-prossimità, Presentazione, Sicurezza
     - Mismatch di ``SessionEstablishment`` anticipato
     - Se il ``SessionEstablishment`` anticipato è ricevuto nel Negotiated Handover, Istanza del Wallet verifica la corrispondenza con quello ricevuto nel recupero dati; in caso di mancata corrispondenza termina il flusso.
   * - WP_103h
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Assenza di SessionEstablishment anticipato
     - Se il ``SessionEstablishment`` anticipato non è ricevuto durante il Negotiated Handover, Istanza del Wallet procede con il Device Retrieval normalmente (nessun errore).
   * - WP_104
     - Flusso-prossimità, Presentazione, Sicurezza
     - Derivare chiave di sessione
     - Istanza del Wallet deriva con successo le chiave di sessione eseguendo il key-agreement negoziato con la propria chiave privata effimera e la chiave pubblica effimera della Relying Party.
   * - WP_105
     - Flusso-prossimità, Presentazione, Sicurezza
     - Decifrare & verificare ``SessionEstablishment``
     - Istanza del Wallet decifra il messaggio ``SessionEstablishment`` usando la chiave di sessione derivata e valida la firma della Relying Party nel parametro ``readerAuthAll``.
   * - WP_106
     - Flusso-prossimità, Presentazione, Sicurezza
     - Validare contenuti ``SessionEstablishment``
     - Istanza del Wallet verifica che ``SessionEstablishment`` includa la chiave pubblica della Relying Party e la richiesta di specifici attributi.
   * - WP_107
     - Flusso-prossimità, Presentazione, Privacy
     - Richiedere consenso agli attributi
     - Istanza del Wallet decifra e mostra gli attributi richiesti all'Utente e procede solo dopo approvazione esplicita di quest'ultimo.
   * - WP_107a
     - Flusso-prossimità, Presentazione, Privacy
     - Mostrare certificato Relying Party
     - Istanza del Wallet mostra all'Utente il Certificato di Registrazione della Relying Party prima di ottenere il consenso dell'Utente.
   * - WP_108
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Recuperare Attestati Elettronici mdoc
     - Istanza del Wallet recupera gli Attestati Elettronici richiesti e li prepara per l'mdoc response.
   * - WP_109
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Preparare la risposta mdoc
     - Istanza del Wallet costruisce il messaggio ``SessionData`` (risposta mdoc) in CBOR includendo un array ``documents`` con gli Attestati Elettronici richiesti.
   * - WP_110
     - Flusso-prossimità, Presentazione, Sicurezza, Interoperabilità
     - Autenticazione mdoc
     - Istanza del Wallet firma correttamente i dati di autenticazione ``deviceSigned`` per ogni Attestato Elettronico presentato come spiegato nella Sezione 12.4 di [`ISO18013-5`_].
   * - WP_111
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Validare struttura risposta mdoc
     - La risposta mdoc è un oggetto CBOR con parametro ``version`` alla radice e ogni documento in ``documents`` contenente ``docType``.
   * - WP_111a
     - Flusso-prossimità, Presentazione, Sicurezza
     - Validare parametro ``deviceSigned``
     - Ogni documento include un ``nameSpaces`` (anche vuoto) e un ``deviceAuth``. Quest'ultimo è un JSON struttura avente un parametro ``deviceSignature`` contenente un Array ``COSE_Sign1`` che autentica il dispositivo.
   * - WP_112
     - Flusso-prossimità, Presentazione, Sicurezza
     - Cifrare ``SessionData``
     - Istanza del Wallet cifra il ``SessionData`` con la chiave di sessione derivata.
   * - WP_112a
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Trasmettere messaggi su BLE
     - Su BLE (usando le caratteristiche GATT ISO), Istanza del Wallet riceve correttamente il ``SessionEstablishment`` cifrato dalla Relying Party e trasmette il proprio ``SessionData`` cifrato (e gli eventuali codici di stato/terminazione).
   * - WP_112b
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Trasmettere messaggi su NFC
     - Su NFC (usando il flusso APDU), Istanza del Wallet riceve correttamente il ``SessionEstablishment`` cifrato dalla Relying Party e trasmette il proprio ``SessionData`` cifrato, gestendo senza errori frammentazione e status word.
   * - WP_112c
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Coerenza UUID/MTU BLE
     - Gli UUID di servizio/caratteristiche BLE e l’MTU effettivo sono coerenti con quanto descritto in DeviceEngagement (e/o Carrier Configuration) e i messaggi sono segmentati di conseguenza.
   * - WP_112d
     - Flusso-prossimità, Presentazione, Sicurezza
     - Caratteristica BLE Ident (opzionale)
     - Se implementata, Istanza del Wallet verifica il valore Ident della Relying Party prima del recupero dati e disconnette BLE in caso di mancata corrispondenza, per Sezione 11.1.3 di [`ISO18013-5`_].
   * - WP_112e
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Gestione SELECT AID NFC
     - Istanza del Wallet espone l'`AID` e, su SELECT `APDU`, restituisce `FCI` valido con `SW1/SW2` corretti; seguono scambi ENVELOPE/GET RESPONSE.
   * - WP_112f
     - Flusso-prossimità, Presentazione, Interoperabilità
     - Coerenza dimensioni APDU NFC
     - Le dimensioni comando/risposta `APDU` (inclusa frammentazione e gestione `SW1=61`) sono coerenti con le dimensioni massime descritte (Carrier Configuration / NFCOptions) durante il Device Engagement.
   * - WP_113
     - Flusso-prossimità, Presentazione, Sicurezza
     - Terminare sessione / timeout inattività
     - Istanza del Wallet termina automaticamente la sessione se non vengono inviati/ricevuti messaggi di sessione per l'intervallo di timeout configurato.
   * - WP_113a
     - Flusso-prossimità, Presentazione, Sicurezza
     - Terminare sessione / nessuna ulteriore richiesta
     - Istanza del Wallet termina la sessione quando essa o la Relying Party hanno concluso lo scambio dati.
   * - WP_113b
     - Flusso-prossimità, Presentazione, Sicurezza
     - Inviare segnale di terminazione (BLE)
     - Istanza del Wallet invia il comando End (o codice di terminazione) su BLE per segnalare la chiusura della sessione.
   * - WP_113c
     - Flusso-prossimità, Presentazione, Sicurezza
     - Inviare terminazione su NFC
     - Istanza del Wallet segnala la fine tramite uno status code in ``SessionData`` e/o completa lo scambio APDU secondo ISO; non sono accettate ulteriori APDU per la sessione.
   * - WP_114
     - Flusso-prossimità, Presentazione, Sicurezza
     - Distruggere chiave di sessione
     - Alla chiusura della sessione, Istanza del Wallet cancella chiave di sessione e materiale effimero correlato da memoria e archiviazione.
   * - WP_114a
     - Flusso-prossimità, Presentazione, Sicurezza
     - Chiudere canale di comunicazione
     - Istanza del Wallet chiude il canale attivo disconnettendo il link BLE o terminando lo scambio APDU NFC; non rimangono canali aperti.

.. _user-attribute-deletion-testcases:

Casi di Test per Eliminazione Attributi dell'Utente Lato Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione elenca i casi di test dalle Sezioni:

- :ref:`user-attribute-deletion:Eliminazione degli Attributi dell'Utente`
- `Relying Party Provider Backend Erasure Endpoint <relying-party-provider-backend-endpoint.html#relying-party-provider-backend-erasure-endpoint>`_

.. list-table::
   :class: longtable
   :widths: 15 15 20 55
   :header-rows: 1

   * - ID Caso di Test
     - Scopo
     - Descrizione
     - Risultati Attesi
   * - WP_115
     - Eliminazione Attributi, Ciclo di vita, Privacy
     - Funzione eliminazione attributi
     - L'UI dell'Istanza del Wallet fornisce funzioni per consentire all'Utente di richiedere l'eliminazione di attributi, visualizzare log transazioni, e vedere un elenco delle Relying Party verso le quali ha presentato degli Attributi.
   * - WP_115a
     - Eliminazione Attributi, Ciclo di vita, Privacy
     - Log transazioni per eliminazione attributi
     - La vista dei log delle transazioni mostra le Relying Party in possesso degli attributi dell'Utente.
   * - WP_116
     - Eliminazione Attributi, Ciclo di vita, Sicurezza
     - Validazione metadata Relying Party per eliminazione
     - Quando un Utente seleziona una Relying Party per l'eliminazione degli Attributi, Istanza del Wallet recupera e valida i suoi metadata di Federazione, confermando la presenza di un Endpoint di Cancellazione della Relying Party.
   * - WP_117
     - Eliminazione Attributi, Ciclo di vita, Interoperabilità
     - Richiesta Cancellazione
     - Istanza del Wallet costruisce correttamente, e invia una Richiesta Cancellazione valida destinata all'Endpoint di Cancellazione della Relying Party.
   * - WP_117a
     - Eliminazione Attributi, Ciclo di vita, Privacy
     - Registrazione Richiesta Cancellazione
     - Una voce nel log viene creata per ogni Richiesta Cancellazione, contenente il timestamp, l'identificativo della Relying Party, e gli Attributi specifici la cui eliminazione è richiesta.
   * - WP_118
     - Eliminazione Attributi, Ciclo di vita, UX
     - Reindirizzamento utente e callback per cancellazione
     - Istanza del Wallet reindirizza con successo l'Utente all'Endpoint di Cancellazione della Relying Party e riceve la Risposta Cancellazione tramite un opportuno meccanismo di callback.
   * - WP_119
     - Eliminazione Attributi, Ciclo di vita, Interoperabilità
     - Gestisce risposta eliminazione/errore
     - Istanza del Wallet processa correttamente sia le risposte di successo che di errore per la Risposta Cancellazione dalla Relying Party.
   * - WP_119a
     - Eliminazione Attributi, Ciclo di vita, UX
     - Notifica utente su cancellazione
     - Istanza del Wallet mostra una notifica chiara all'Utente indicando il successo o fallimento della Richiesta di Cancellazione.

.. _credential-backup-testcases:

Casi di Test per Backup e Ripristino degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione elenca i casi di test dalla Sezione :ref:`backup-restore:Backup e Ripristino`.

.. list-table::
   :class: longtable
   :widths: 15 15 20 55
   :header-rows: 1

   * - ID Caso di Test
     - Scopo
     - Descrizione
     - Risultati Attesi
   * - WP_120
     - Backup e Ripristino, UX
     - Avvio backup Attestato Elettronico
     - L'Utente attiva con successo l'operazione backup Attestato Elettronico sull'Istanza del Wallet.
   * - WP_120a
     - Backup e Ripristino, Sicurezza
     - Visualizzazione frase-chiave casuale
     - Istanza del Wallet invoca le API backup, seleziona 10 frasi-chiave casuali da un elenco pre-generato e le mostra all'Utente.
   * - WP_120b
     - Backup e Ripristino, Sicurezza
     - Istruzione archiviazione sicura frase-chiave
     - Istanza del Wallet mostra un'istruzione chiara per l'Utente per archiviare in modo sicuro le frasi-chiave generate.
   * - WP_121
     - Backup e Ripristino, Sicurezza
     - Derivazione chiave da frasi-chiave
     - Istanza del Wallet deriva una chiave crittografica dalle frasi-chiave dell'Utente utilizzando una funzione derivazione chiave (es. ``PBKDF2``, ``Bcrypt``, ``Scrypt``).
   * - WP_121a
     - Backup e Ripristino, Sicurezza
     - Configurazione funzione derivazione chiave
     - Se ``PBKDF2`` con ``SHA-256`` è utilizzato, la funzione è configurata con un conteggio iterazioni di almeno ``600,000``.
   * - WP_122
     - Backup e Ripristino, Interoperabilità
     - Creazione JWT backup firmato
     - Istanza del Wallet crea un file backup contenente un JWT firmato che incapsula i dati backup.
   * - WP_122a
     - Backup e Ripristino, Interoperabilità
     - Header JOSE per JWT backup
     - L'header JWT backup contiene l'``alg`` utilizzato per firmare il backup e un ``typ`` di ``wallet-unit-credentials-backup+jwt``.
   * - WP_122b
     - Backup e Ripristino, Interoperabilità
     - Contenuti payload JWT backup
     - Il payload JWT backup include i claim richiesti: ``timestamp``, ``wallet_provider_id``, ``wallet_instance_version``, ``wallet_attestation``, e ``credentials_backup``.
   * - WP_122c
     - Backup e Ripristino, Sicurezza
     - Cronologia transazioni opzionale nel JWT backup
     - Il claim ``credentials_backup`` contiene la cronologia transazioni per ogni Attestato Elettronico, se supportato.
   * - WP_122d
     - Backup e Ripristino, Sicurezza
     - Identificatori Attestato Elettronico nel JWT backup
     - Il claim ``credentials_backup`` contiene voci chiave dall'identificativo Fornitore di Attestato Elettronico, e ogni voce elenca uno o più ``credential_configuration_ids`` corrispondenti agli Attestati Elettronici rilasciati.
   * - WP_123
     - Backup e Ripristino, Sicurezza
     - Firma JWT backup con chiave attestata
     - Istanza del Wallet firma il JWT backup con la chiave privata corrispondente alla chiave pubblica trovata nel claim ``cnf`` del JWT Wallet Attestation.
   * - WP_123a
     - Backup e Ripristino, Sicurezza
     - Controllo validità attestato per JWT backup
     - Prima di firmare il JWT backup, Istanza del Wallet verifica la validità del proprio Wallet Attestation.
   * - WP_124
     - Backup e Ripristino, Sicurezza
     - Cifratura file backup con chiave Utente
     - Istanza del Wallet cifra il backup utilizzando la chiave derivata dalle frasi-chiave dell'Utente.
   * - WP_125
     - Backup e Ripristino, UX
     - Prompt selezione posizione archiviazione sicura
     - Istanza del Wallet richiede all'Utente di selezionare una posizione per salvare il file backup cifrato, offrendo opzioni come archiviazione locale o cloud.
   * - WP_126
     - Backup e Ripristino, UX
     - Avvio ripristino Attestato Elettronico
     - L'Utente attiva con successo l'operazione ripristino degli Attestati Elettronici sull'Istanza del Wallet.
   * - WP_127
     - Backup e Ripristino, UX
     - Selezione file backup/frase-chiave per ripristino
     - L'Utente seleziona con successo un file backup dall'archiviazione e inserisce le loro frasi-chiave di recupero.
   * - WP_128
     - Backup e Ripristino, Interoperabilità
     - Estrazione Wallet Attestation da JWT backup
     - Istanza del Wallet estrae la Wallet Attestation dal claim ``wallet_attestation`` del JWT backup trovato all'interno del file backup.
   * - WP_128a
     - Backup e Ripristino, Sicurezza
     - Ignorare scadenza Wallet Attestation durante ripristino
     - Il processo ripristino continua con successo anche se la Wallet Attestation nel file backup è scaduto.
   * - WP_129
     - Backup e Ripristino, Sicurezza
     - Verifica firma JWT backup
     - Istanza del Wallet verifica con successo la firma del JWT backup utilizzando la chiave pubblica contenuta nel parametro ``cnf.jwk`` del JWT valorizzato nel parametro ``wallet_attestation``.
   * - WP_130
     - Backup e Ripristino, Interoperabilità
     - Emissione di Attestato Elettronico da backup ripristinato
     - Per ogni voce Attestato Elettronico nel JWT backup, Istanza del Wallet estrae con successo l'URL Fornitore di Attestati, e il ``credential_configuration_id``.
   * - WP_130a
     - Backup e Ripristino, Interoperabilità
     - Recuperare metadata Fornitore di Attestato Elettronico
     - Per ogni URL Fornitore di Attestato Elettronico, Istanza del Wallet recupera con successo i metadata del Fornitore di Attestato Elettronico corrispondenti.
   * - WP_130b
     - Backup e Ripristino, Interoperabilità
     - Richiesta emissione Attestato Elettronico
     - Per ogni Attestato Elettronico, Istanza del Wallet avvia con successo un nuovo Wallet-Initiated Authorization Code Issuance Flow legato alla nuova chiave dell'Istanza del Wallet (nuova Associazione Crittografica con l'Utente), e non un rinnovo del token né una richiesta di Re-issuance Flow.

.. _wallet-instance-optional-testcases:

Casi di Test Opzionali per Istanza del Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione elenca i casi di test dalle Sezioni:

- :ref:`wallet-instance:Istanza del Wallet`
- `Request-Specific Error Responses <wallet-provider-endpoint.html#request-specific-error-responses>`_
- `Mobile Application Instance Initialization <mobile-application-instance.html#mobile-application-instance-initialization>`_

Questi casi di test sono opzionali e sono stati progettati per l'implementazione IT Wallet, gestita da PagoPA. Sono destinati agli implementatori che devono verificare la compatibilità con le caratteristiche specifiche di questo modello di riferimento.

.. list-table::
   :class: longtable
   :widths: 15 15 20 55
   :header-rows: 1

   * - ID Caso di Test
     - Scopo
     - Descrizione
     - Risultati Attesi
   * - WP_131
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Sicurezza
     - Richiesta nonce per protezione da replay attack
     - Istanza del Wallet richiede e riceve un nonce monouso, di breve durata dal Nonce Endpoint del Fornitore del Wallet.
   * - WP_132
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Interoperabilità
     - Generazione/archiviazione coppia chiavi EC hardware-backed
     - Istanza del Wallet genera con successo una coppia chiavi crittografiche hardware-backed fresca e archivia il suo ``hardware_key_tag`` associato nell'archiviazione sicura locale.
   * - WP_132a
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Sicurezza
     - Eliminazione chiave pre-esistente durante inizializzazione
     - Istanza del Wallet controlla la presenza di Cryptographic Hardware Keys pre-esistenti durante l'inizializzazione, se presenti, le elimina con successo.
   * - WP_133
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Interoperabilità
     - Invio Richiesta di Inizializzazione Wallet
     - Istanza del Wallet invia con successo al Fornitore del Wallet una richiesta di Inizializzazione con i parametri richiesti ``nonce``, ``key_attestation``, e ``hardware_key_tag``.
   * - WP_133a
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Interoperabilità
     - Calcolo hash SHA-256
     - Istanza del Wallet calcola con successo un digest SHA-256 (``client_data_hash``) sul ``nonce``, il ``hardware_key_pub``, e il ``hardware_key_tag``,
   * - WP_133b
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Interoperabilità
     - Key Attestation
     - Istanza del Wallet invoca con successo l'API Key Attestation con il ``client_data_hash`` e ottiene un attestato firmato dalla Key Attestation API.
   * - WP_134
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Sicurezza
     - Richiesta Key Binding
     - Istanza del Wallet invia una richiesta Key Binding che contiene un parametro ``assertion`` il cui valore è un JWT firmato.
   * - WP_134a
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Sicurezza
     - Firma JWT Key Binding
     - Istanza del Wallet firma con successo il JWT richiesta Key Binding con la chiave pubblica Wallet Hardware.
   * - WP_135
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Sicurezza
     - Validazione Richiesta di Inizializzazione Wallet
     - Il Fornitore del Wallet controlla con successo i parametri della Richiesta di Inizializzazione: il ``nonce`` e ``key_attestation``. Se validi, restituisce una risposta di conferma.
   * - WP_135a
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Sicurezza
     - Verifica unicità nonce
     - Il Fornitore del Wallet rifiuta qualsiasi Richiesta di Inizializzazione contenente un nonce che non ha generato o che è già stato utilizzato.
   * - WP_135b
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Sicurezza
     - Validazione Key Attestation per linee guida
     - Il Fornitore del Wallet valida il ``key_attestation`` usando le linee guida produttore e conferma che il dispositivo soddisfa i suoi requisiti minimi sicurezza.
   * - WP_136
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Sicurezza
     - Verifica associazione crittografica
     - Il Fornitore del Wallet verifica con successo l'associazione crittografica tra il ``hardware_key_tag``, ``hardware_key_pub``, il nonce, e il ``client_data_hash`` fornito nel parametro ``key_attestation``.
   * - WP_137
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Interoperabilità
     - Registrazione Istanza del Wallet
     - Il Fornitore del Wallet registra con successo Istanza del Wallet, archiviando il suo ``hardware_key_tag``, ``hardware_key_pub``, e altre informazioni dispositivo.
   * - WP_138
     - Inizializzazione / Attivazione Wallet, Ciclo di vita, Sicurezza
     - Creazione account utente
     - Il Fornitore del Wallet crea un account Utente associato al ``hardware_key_tag`` dell'Istanza del Wallet.
   * - WP_139
     - Disinstallazione Wallet, Ciclo di vita, Sicurezza
     - Eliminazione chiave/stato su disinstallazione
     - Istanza del Wallet si disinstalla e rimuove tutte le chiavi locali e dati applicazione.
   * - WP_140
     - Rilascio Wallet Attestation, Ciclo di vita, Sicurezza
     - Richiesta di Emissione della Wallet Attestation
     - Istanza del Wallet costruisce con successo il JWT Richiesta di Emissione della Wallet Attestation con i claim richiesti: ``integrity_assertion``, ``hardware_signature``, ``nonce``, ``hardware_key_tag``, ``cnf``, e altri parametri correlati alla configurazione.
   * - WP_140a
     - Rilascio Wallet Attestation, Ciclo di vita, Sicurezza
     - Controllo esistenza chiave hardware/ri-inizializzazione
     - Istanza del Wallet controlla l'esistenza di Cryptographic Hardware Keys; se non vengono trovate, attiva il processo ri-inizializzazione.
   * - WP_140b
     - Rilascio Wallet Attestation, Ciclo di vita, Interoperabilità
     - Richiede nonce per Richiesta di Emissione della Wallet Attestation
     - Istanza del Wallet richiede con successo e riceve un nuovo nonce dal Nonce Endpoint del Fornitore del Wallet, prima di richiedere la Wallet Attestation.
   * - WP_140c
     - Rilascio Wallet Attestation, Ciclo di vita, Interoperabilità
     - Calcola hash per Richiesta di Emissione della Wallet Attestation
     - Istanza del Wallet calcola un digest SHA-256 (``client_data_hash``) del nonce e del thumbprint del JWK ``ephemeral_key_pub``.
   * - WP_140d
     - Rilascio Wallet Attestation, Ciclo di vita, Interoperabilità
     - Firma hash con chiave privata hardware
     - Istanza del Wallet firma il ``client_data_hash`` con la chiave privata hardware e produce un ``hardware_signature`` valido.
   * - WP_140e
     - Rilascio Wallet Attestation, Ciclo di vita, Interoperabilità
     - Ottiene Integrity Assertion firmato dal Servizio di Integrità del Dispositivo.
     - Istanza del Wallet richiede con e riceve con successo una ``integrity_assertion`` firmata dal Servizio di Integrità del Dispositivo che è associato al ``client_data_hash``.
   * - WP_140f
     - Rilascio Wallet Attestation, Ciclo di vita, Sicurezza
     - Includere claim ``cnf``
     - Il claim ``cnf`` nel payload del JWT Richiesta di Emissione della Wallet Attestation contiene la chiave pubblica effimera, collegando la chiave all'attestato.
   * - WP_141
     - Rilascio Wallet Attestation, Ciclo di vita, Sicurezza
     - Firma della Richiesta di Emissione della Wallet Attestation
     - Istanza del Wallet firma il JWT Richiesta di Emissione della Wallet Attestation con la chiave privata effimera.
   * - WP_142
     - Rilascio Wallet Attestation, Ciclo di vita, Sicurezza
     - Invio del JWT Richiesta di Emissione della Wallet Attestation al Fornitore del Wallet
     - Istanza del Wallet invia il JWT richiesta firmato come parametro ``assertion`` all'Endpoint di Issuance degli Attestati Elettronici del Fornitore del Wallet.
   * - WP_143
     - Rilascio Wallet Attestation, Ciclo di vita, Sicurezza
     - Verifica JWT Richiesta Attestato
     - Il Fornitore del Wallet esegue con successo una validazione completa della Richiesta di Emissione della Wallet Attestation, inclusa la sua firma, i suoi parametri, e le verifiche crittografiche associate.
   * - WP_143a
     - Rilascio Wallet Attestation, Ciclo di vita, Sicurezza
     - Validazione header HTTP per Richiesta di Emissione della Wallet Attestation
     - Il Fornitore del Wallet valida con successo l'header del JWT Richiesta di Emissione della Wallet Attestation per contenere parametri ``alg``, ``kid``, e ``typ`` validi.
   * - WP_143b
     - Rilascio Wallet Attestation, Ciclo di vita, Sicurezza
     - Verifica firma JWT in Richiesta di Emissione della Wallet Attestation
     - Il Fornitore del Wallet verifica con successo la firma del JWT Richiesta di Emissione della Wallet Attestation utilizzando la chiave pubblica nel JWK fornito.
   * - WP_143c
     - Rilascio Wallet Attestation, Ciclo di vita, Sicurezza
     - Verifica unicità nonce per Wallet Attestation
     - Il Fornitore del Wallet rifiuta il JWT Richiesta di Emissione della Wallet Attestation se il nonce non è stato generato da esso stesso o è stato precedentemente utilizzato.
   * - WP_143d
     - Rilascio Wallet Attestation, Ciclo di vita, Sicurezza
     - Verifica Istanza del Wallet registrata
     - Il Fornitore del Wallet conferma che la Richiesta di Emissione della Wallet Attestation provenga da un'Istanza del Wallet valida e attualmente registrata; se non rifiuta la richiesta.
   * - WP_143e
     - Rilascio Wallet Attestation, Ciclo di vita, Interoperabilità
     - Validazione firma hardware
     - Il Fornitore del Wallet ricostruisce con successo i client_data, e valida l'``hardware_signature`` utilizzando la chiave pubblica Hardware dell'Istanza del Wallet registrata precedentemente.
   * - WP_143f
     - Rilascio Wallet Attestation, Ciclo di vita, Sicurezza
     - Validazione Integrity Assertion per linee guida
     - Il Fornitore del Wallet valida con successo l'``integrity_assertion`` secondo le linee guida del produttore dispositivo.
   * - WP_143g
     - Rilascio Wallet Attestation, Ciclo di vita, Sicurezza
     - Verifica parametro ``iss``
     - Il Fornitore del Wallet verifica che il parametro ``iss`` nel JWT Richiesta di Emissione della Wallet Attestation corrisponda al suo identificativo URL.
   * - WP_144
     - Rilascio Wallet Attestation, Ciclo di vita, Sicurezza
     - Rilascio Attestato
     - Dopo un validazione riuscita della Richiesta di Emissione della Wallet Attestation, il Fornitore del Wallet rilascia una Wallet Attestation con scadenza non superiore a 24 ore dal rilascio.
   * - WP_145
     - Revoca Wallet, Ciclo di vita, Interoperabilità
     - Recupero stato Istanza del Wallet
     - Istanza del Wallet invia una Richiesta di Recupero Istanze del Wallet all'Endpoint di Gestione dell'Istanza del Wallet del Fornitore del Wallet.
   * - WP_146
     - Revoca Wallet, Ciclo di vita, Interoperabilità
     - Risposta stato Istanza del Wallet
     - Il Fornitore del Wallet valida la richiesta e restituisce all'Istanza del Wallet un elenco delle Istanze del Wallet collegate dell'Utente autenticato, inclusi i campi ``ID``, ``status``, e ``issued_at`` di ogni istanza.
   * - WP_147
     - Revoca Wallet, Ciclo di vita, Interoperabilità
     - Corpo Richiesta di Revoca Istanza del Wallet
     - La Richiesta di Revoca Istanza del Wallet include nel body un oggetto con chiave ``status`` e valore ``REVOKED``.
   * - WP_148
     - Revoca Wallet, Ciclo di vita, Interoperabilità
     - Risposta Revoca Istanza del Wallet
     - Il Fornitore del Wallet aggiorna lo stato dell'Istanza del Wallet a ``REVOKED`` e restituisce una conferma.
   * - WP_149
     - Revoca Wallet, Ciclo di vita, Sicurezza
     - Cancella chiavi su revoca
     - Nella revoca, Istanza del Wallet rimuove tutte le Cryptographic Hardware Key associate dal dispositivo all'Istanza stessa.
   * - WP_150
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Interoperabilità
     - Fallimento inizializzazione (nonce non valido)
     - Quando una Richiesta di Inizializzazione Istanza del Wallet contiene un nonce non valido, scaduto, o già utilizzato, il Fornitore del Wallet restituisce una risposta ``403 Forbidden`` con codice errore ``invalid_request``.
   * - WP_151
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Interoperabilità
     - Fallimento inizializzazione (firma Key Attestation)
     - Quando una Richiesta di Inizializzazione Istanza del Wallet contiene una firma Key Attestation non valida, il Fornitore del Wallet restituisce una risposta ``403 Forbidden`` con codice errore ``invalid_request``.
   * - WP_152
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Interoperabilità
     - Fallimento Key Binding (Istanza del Wallet non trovata)
     - Quando una richiesta Key Binding riferisce un'Istanza del Wallet che non viene trovata, il Fornitore del Wallet restituisce una risposta ``404 Not Found`` con codice errore ``not_found``.
   * - WP_153
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Interoperabilità
     - Fallimento Key Binding (Istanza del Wallet revocata)
     - Quando una richiesta Key Binding è fatta per un'Istanza del Wallet che è stata revocata, il Fornitore del Wallet restituisce una risposta ``403 Forbidden`` con codice errore ``invalid_request``.
   * - WP_154
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Interoperabilità
     - Fallimento Key Binding (PoP non valido)
     - Quando una richiesta Key Binding contiene una Proof of Possession non valida (``hardware_signature``), il Fornitore del Wallet restituisce una risposta ``403 Forbidden`` con codice errore ``invalid_request``.
   * - WP_155
     - Inizializzazione / Registrazione Wallet, Ciclo di vita, Interoperabilità
     - Fallimento Key Binding (fallimento Integrity Assertion)
     - Quando l'Integrity Assertion in una richiesta Key Binding non passa la validazione (es. il dispositivo è manomesso), il Fornitore del Wallet restituisce una risposta ``403 Forbidden`` con codice errore ``invalid_request``.


