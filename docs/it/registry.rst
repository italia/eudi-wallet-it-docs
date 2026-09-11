.. include:: ../common/common_definitions.rst


Infrastruttura del Registro
===========================

L'ecosistema IT-Wallet opera attraverso un'Infrastruttura del Registro che fornisce definizioni standardizzate dei dati, registrazione delle entità e capacità di discovery delle Credenziali. Il sistema di registro è composto da molteplici componenti interconnessi che supportano il ciclo di vita completo delle operazioni sulle Credenziali digitali, dall'onboarding delle entità alla presentazione delle Credenziali.

L'architettura del registro risponde ai requisiti di standardizzazione semantica, gestione della fiducia federata e discovery delle Credenziali attraverso componenti specializzati che garantiscono interoperabilità e conformità nell'intero ecosistema.

Panoramica dell'Architettura di Registro
----------------------------------------

Il Registro di Sistema IT-Wallet comprende sei componenti principali:

1. **Registro dei Claims**: Definizioni semantiche standardizzate per i singoli attributi delle Credenziali, i tipi di dati e le regole di validazione.
2. **Registro delle Fonti Autentiche (FA)**: Catalogo dei fornitori di dati registrati con le loro capacità dichiarate e i claim disponibili.
3. **Registro della Federazione**: Elenco autorevole delle entità fidate che partecipano alla federazione con le loro configurazioni tecniche.
4. **Catalogo delle Credenziali Digitali**: Meccanismo pubblico di discovery per le tipologie di Credenziale disponibili con i loro metadati e le informazioni di emissione.
5. **Registro degli Schemi**: Elenco autorevole degli Schemi di Credenziale.
6. **Tassonomia**: Sistema di classificazione gerarchica che organizza le Credenziali per dominio e finalità.

Questi componenti del registro sono interconnessi e mantenuti dall'Organismo di Vigilanza per garantire coerenza, sicurezza e conformità normativa nell'intero ecosistema.

Endpoint di Discovery del Registro
----------------------------------

Il Trust Anchor DEVE fornire un meccanismo di discovery per tutti i componenti del registro attraverso endpoint *well-known* standardizzati che forniscono metadati e informazioni di discovery REST API per gestire operazioni complesse come paginazione e filtraggio.

Il Trust Anchor DEVE pubblicare i metadati di discovery del registro all'endpoint ``.well-known/it-wallet-registry`` con supporto alla negoziazione del contenuto:

- **Content-Type predefinito**: ``application/jwt`` (JWT firmato che garantisce autenticità e integrità)
- **Content-Type alternativo**: ``application/json`` (JSON semplice per scopi di sviluppo/debug)

Inoltre, il Registro di Sistema IT-Wallet DEVE utilizzare due distinti pattern di accesso:

- **API dei Registri Dati**: DEVONO supportare capacità di paginazione e filtraggio.
- **Infrastruttura di Fiducia della Federazione**: come definito in :ref:`trust-infrastructure:L'Infrastruttura di Trust`.

Di seguito è riportato un esempio non normativo.

.. code-block:: http

    GET /.well-known/it-wallet-registry HTTP/1.1
    Host: trust-anchor.eid-wallet.example.it
    Accept: application/jwt

    HTTP/1.1 200 OK
    Content-Type: application/jwt

    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...

.. code-block:: http

    GET /.well-known/it-wallet-registry HTTP/1.1
    Host: trust-anchor.eid-wallet.example.it
    Accept: application/json

    HTTP/1.1 200 OK
    Content-Type: application/json

Parametri dell'Endpoint di Discovery del Registro
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il payload JWT della risposta dell'Endpoint di Discovery del Registro DEVE contenere i seguenti parametri:

.. list-table:: Endpoint di Discovery del Registro — Parametri del Payload JWT
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Nome Campo**
     - **Descrizione**
   * - **id**
     - OBBLIGATORIO. Identificatore univoco del documento di discovery (es. ``urn:it-wallet-registry:it-wallet``).
   * - **version**
     - OBBLIGATORIO. Versione del formato del documento di discovery (es. ``1.0.0``).
   * - **last_updated**
     - OBBLIGATORIO. Timestamp dell'ultima modifica al documento di discovery (es. ``2024-03-15T10:30:00Z``).
   * - **endpoints**
     - OBBLIGATORIO. Oggetto JSON contenente gli URI di tutti i componenti del registro. DEVONO essere presenti le seguenti chiavi di endpoint:

       * **claims_registry**: URI dell'API del Registro dei Claims.
       * **authentic_sources**: URI dell'API del Registro delle Fonti Autentiche.
       * **credential_catalog**: URI dell'endpoint well-known del Catalogo delle Credenziali Digitali.
       * **taxonomy**: URI della risorsa Tassonomia.
       * **schema_registry**: URI dell'API del Registro degli Schemi.
       * **federation_list**: URI dell'endpoint di listing della federazione (OpenID Federation ``/list``).
       * **federation_fetch**: URI dell'endpoint fetch della federazione (OpenID Federation ``/fetch``).
       * **federation_resolve**: URI dell'endpoint resolve della federazione (OpenID Federation ``/resolve``).
       * **federation_trust_mark_status**: URI dell'endpoint di stato del Trust Mark.
       * **federation_historical_keys**: URI dell'endpoint degli JWK storici.
   * - **content_negotiation**
     - OBBLIGATORIO. Array dei tipi di contenuto supportati dall'endpoint di discovery (es. ``["application/json", "application/jwt"]``).

Struttura del payload JWT (in forma decodificata):

.. code-block:: json

  {
    "id": "urn:it-wallet-registry:it-wallet",
    "version": "1.0.0",
    "last_updated": "2024-03-15T10:30:00Z",
    "endpoints": {
      "claims_registry": "https://trust-anchor.eid-wallet.example.it/api/v1/claims",
      "authentic_sources": "https://trust-anchor.eid-wallet.example.it/api/v1/authentic-sources",
      "credential_catalog": "https://trust-anchor.eid-wallet.example.it/api/v1/.well-known/credential-catalog",
      "taxonomy": "https://trust-anchor.eid-wallet.example.it/api/v1/taxonomy",
      "schema_registry": "https://trust-anchor.eid-wallet.example.it/api/v1/schemas",
      "federation_list_endpoint": "https://trust-anchor.eid-wallet.example.it/list",
      "federation_fetch_endpoint": "https://trust-anchor.eid-wallet.example.it/federation_fetch_endpoint",
      "federation_resolve_endpoint": "https://trust-anchor.eid-wallet.example.it/resolve",
      "federation_trust_mark_status_endpoint": "https://trust-anchor.eid-wallet.example.it/trust_mark_status",
      "federation_trust_mark_list_endpoint": "https://dev.ta.wallet.ipzs.it/trust_mark_listing",
      "federation_trust_mark_endpoint": "https://dev.ta.wallet.ipzs.it/trust_mark",
      "federation_historical_keys_endpoint": "https://trust-anchor.eid-wallet.example.it/federation_historical_keys"
    },
    "content_negotiation": ["application/json", "application/jwt"]
  }

Registro dei Claims
-------------------

Il **Registro dei Claims** fornisce definizioni semantiche standardizzate per i singoli attributi delle Credenziali, i tipi di dati e le regole di validazione. Questo registro funge da fondamento semantico per la standardizzazione degli attributi delle Credenziali nell'intero ecosistema IT-Wallet, operando in coordinamento con il componente Tassonomia per la classificazione gerarchica.

L'Organismo di Vigilanza DEVE mantenere il Registro dei Claims per garantire la coerenza semantica e la conformità normativa nell'intero ecosistema. Il registro DEVE contenere:

  - **Claims Standardizzati**: Definizioni semantiche per tutti gli attributi delle Credenziali con tipi di dati e regole di validazione.
  - **Mappature di Interoperabilità**: Definizioni di alias per i claim che utilizzano terminologie diverse tra gli standard (es. ``place_of_birth`` di ISO18013-5 mappato al canonico ``birth_place``).
  - **Formati dei Dati**: Tipi di dati standardizzati (stringa, data, numerico, booleano, email, url, immagine, array, oggetto) con pattern di validazione.

Il Registro dei Claims DEVE garantire:

  - **Coerenza Semantica**: Previene conflitti tra claim duplicati o sovrapposti nell'intero ecosistema.
  - **Interoperabilità Transfrontaliera**: Garantisce la conformità EU e l'interpretazione coerente dei claim.
  - **Validazione degli Schemi**: Fornisce definizioni autorevoli per la validazione dei claim in tutti gli scenari di Credenziale.
  - **Allineamento Normativo**: Si coordina con il quadro normativo nazionale ed europeo.
  - **Scenari Credential-Agnostic**: Supporta scenari in cui la **comodità dell'utente** e l'**efficienza operativa aziendale** sono prioritarie rispetto alla **conformità normativa** e alle **audit trail**.

.. note::
  Il Registro dei Claims definisce le proprietà semantiche dei singoli attributi, ma NON DEVE specificare le capacità di selective disclosure. La selective disclosure dipende dalle implementazioni del formato della Credenziale (SD-JWT, mDocs), dalle configurazioni tecniche dell'emittente e dal contesto di presentazione. Queste capacità sono specificate a livello di tipologia di Credenziale all'interno del Catalogo delle Credenziali Digitali e implementate durante i flussi di presentazione delle Credenziali.

Utilizzo del Registro dei Claims
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Registro dei Claims DEVE supportare il ciclo di vita completo dell'ecosistema:

**Durante il Processo di Onboarding**:

  - **Registrazione FA**: Le Fonti Autentiche dichiarano i claim disponibili dal registro standardizzato durante la registrazione delle capacità.
  - **Registrazione EI**: Gli Emittenti di Credenziali selezionano le entità FA in base ai claim richiesti e registrano le tipologie di Credenziale per la pubblicazione nel catalogo.
  - **Registrazione RP**: Le Relying Party specificano i requisiti di autorizzazione utilizzando domini/finalità per tipologie specifiche di Credenziale e/o attributi dell'Utente.

**Durante le Attività Operative**:

  - **Emissione di Credenziali**: Le definizioni dei claim garantiscono una rappresentazione coerente dei dati tra le diverse tipologie di Credenziale.
  - **Richieste di Presentazione**: Le RP fanno riferimento ai claim per la validazione degli schemi e la verifica dell'autorizzazione in scenari sia credential-specific che credential-agnostic.
  - **Applicazione delle Politiche**: Le politiche di autorizzazione sfruttano le classificazioni per dominio/finalità per il controllo degli accessi.

Struttura del Registro dei Claims
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Registro dei Claims mantiene definizioni tecniche neutrali rispetto alla lingua per la coerenza semantica nell'intero ecosistema. Le localizzazioni per gli utenti finali dei nomi e delle descrizioni dei claim sono fornite tramite bundle di localizzazione dedicati referenziati attraverso il campo ``localization.base_uri``, abilitando un efficiente supporto multilingue senza compromettere l'integrità strutturale del registro.

.. list-table:: Campi di Primo Livello del Registro dei Claims
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Nome Campo**
     - **Descrizione**
   * - **id**
     - OBBLIGATORIO. Identificatore univoco del Registro dei Claims (es. ``urn:claims:it-wallet``).
   * - **version**
     - OBBLIGATORIO. La versione del Registro dei Claims (es. ``1.0.0``).
   * - **last_modified**
     - OBBLIGATORIO. Il timestamp che indica quando il registro è stato aggiornato l'ultima volta (es. ``2026-03-06T00:00:00Z``).
   * - **localization**
     - OBBLIGATORIO. Oggetto di configurazione della localizzazione contenente:

       * **default_locale**: Codice locale predefinito (es. ``it``).
       * **available_locales**: Array dei codici locale supportati (es. ``["en", "it"]``).
       * **base_uri**: URI base per il recupero del bundle di localizzazione (es. ``https://trust-registry.eid-wallet.example.it/.well-known/l10n/claims/``).
       * **version**: Versione del formato del bundle di localizzazione.
   * - **claims**
     - OBBLIGATORIO. Un Oggetto JSON in cui ogni chiave è il nome di un claim e ogni valore è un Oggetto JSON che descrive tale claim. Ogni oggetto claim contiene i parametri definiti nella tabella "Parametri di una Voce di Claim" di seguito.

.. list-table:: Parametri di una Voce di Claim
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Nome Campo**
     - **Descrizione**
   * - **description_l10n_id**
     - OBBLIGATORIO. Chiave di localizzazione che fa riferimento alla descrizione leggibile del claim nel bundle di localizzazione (es. ``claim.given_name.description``).
   * - **type**
     - OBBLIGATORIO. Tipo di dato del claim. Valori supportati: ``string``, ``boolean``, ``array``, ``object``.
   * - **format**
     - OPZIONALE. Qualificatore di formato semantico per i tipi stringa (es. ``date`` per le date ISO 8601, ``uri``, ``data`` per dati binari Base64-encoded).
   * - **encoding**
     - OPZIONALE. Codifica applicata al valore (es. ``base64``). Presente quando ``format`` è ``data``.
   * - **aliases**
     - OPZIONALE. Array di nomi alternativi del claim utilizzati in altri standard che si mappano su questo claim canonico (es. ``["birthdate"]`` per ``birth_date``, ``["date_of_expiry"]`` per ``expiry_date``).
   * - **nested_claims**
     - OPZIONALE. Array di nomi di claim che costituiscono le proprietà di un claim di tipo ``object`` (es. ``["country", "locality", "region"]`` per ``place_of_birth``).
   * - **nested_item_claims**
     - OPZIONALE. Array di nomi di claim che rappresentano le proprietà di ogni elemento in un claim di tipo ``array`` (es. ``["vehicle_category_code", "issue_date", "expiry_date", "codes"]`` per ``driving_privileges``).
   * - **items**
     - OPZIONALE. Oggetto JSON che descrive lo schema di ogni elemento in un claim di tipo ``array`` semplice (es. ``{"type": "string"}`` per ``nationalities``).

Di seguito è fornito un esempio non normativo della struttura del Registro dei Claims:

.. literalinclude:: ../../examples/claims-registry-example.json
  :language: JSON

.. note::
  Per una gestione migliore e più efficiente della localizzazione delle informazioni contenute nel Registro dei Claims, un'Entità che lo consulta DOVREBBE:

  - Scaricare la versione base del Registro dei Claims (compatta, senza localizzazioni) utilizzando l'endpoint ``.well-known/claims``.
  - Determinare la lingua preferita dall'Utente.
  - Scaricare solo i bundle di localizzazione necessari.
  - Unire dinamicamente il contenuto localizzato con la struttura del Registro dei Claims.

Di seguito è fornito un esempio non normativo dell'output di un bundle di localizzazione:

.. code-block:: json

  {
    "claim.given_name.description": "Person's given name(s) as they appear on official documents.",
    "claim.birth_date.description": "Date of birth, in ISO 8601 format (YYYY-MM-DD). Also known as birthdate.",
    "claim.driving_privileges.description": "Array of authorized vehicle categories with details.",
    "...": "..."
  }

I bundle di localizzazione DEVONO essere disponibili all'URI composto aggiungendo il codice locale e ``.json`` al valore ``localization.base_uri`` (es. ``https://trust-registry.eid-wallet.example.it/.well-known/l10n/claims/it.json``).

Registro delle Fonti Autentiche
-------------------------------

L'Organismo di Vigilanza DEVE mantenere il Registro delle Fonti Autentiche per abilitare l'accesso coordinato ai dati e l'emissione di Credenziali nell'intero ecosistema. Il Registro FA DEVE contenere almeno:

  - **Informazioni sull'Organizzazione**: Dettagli della persona giuridica, stato normativo e ruolo autorevole in domini specifici.
  - **Capacità sui Dati**: Disponibilità dei claim dichiarati facendo riferimento alle definizioni standardizzate del Registro dei Claims con le corrispondenti classificazioni della Tassonomia.
  - **Metodi di Integrazione**: Meccanismi tecnici di accesso (PDND).
  - **Finalità Previste**: Tipologie di Credenziale supportate e contesti aziendali per il coordinamento FA-EI.
  - **Garanzia della Qualità dei Dati**: Stato autorevole, frequenza di aggiornamento e capacità di audit trail.

Il Registro FA DEVE garantire:

  - **Accesso Coordinato ai Dati**: Consente agli EI di scoprire i dati appropriati dalle Fonti Autentiche per l'emissione delle Credenziali.
  - **Integrazione FA-EI**: Facilita i flussi di approvazione e il coordinamento dell'accesso ai dati tra le entità.
  - **Garanzia della Qualità**: Mantiene lo stato autorevole e l'affidabilità dei dati nei diversi domini.
  - **Conformità Normativa**: Supporta i requisiti di trasparenza della pubblica amministrazione e di coordinamento del settore privato.

.. note::
   Il Registro delle Fonti Autentiche è un registro tecnico e non pubblico che fornisce orientamento all'Emittente di Credenziali per il provisioning delle Credenziali.

Utilizzo del Registro delle Fonti Autentiche
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Registro FA supporta il coordinamento dell'ecosistema durante l'intero ciclo di vita operativo:

**Durante il Processo di Onboarding**:
  - **Auto-Dichiarazione FA**: Le Fonti Autentiche registrano le capacità prima che esistano tipologie di Credenziale nel catalogo.
  - **Discovery EI**: Gli Emittenti di Credenziali ricercano le entità FA in base ai claim richiesti e alle tipologie di Credenziale previste.
  - **Coordinamento delle Approvazioni**: Le entità FA valutano e approvano le richieste di accesso degli EI per la fornitura dei dati.

**Durante le Attività Operative**:
  - **Risoluzione delle Sorgenti Dati**: I sistemi EI fanno riferimento al Registro FA per l'accesso in tempo reale ai dati durante l'emissione delle Credenziali.
  - **Validazione della Qualità**: Le informazioni del Registro FA supportano la verifica dell'origine dei dati e i requisiti di audit.
  - **Gestione dell'Integrazione**: Gli endpoint tecnici e i metodi di accesso consentono la comunicazione standardizzata FA-EI.

Coordinamento FA Pubblica vs FA Privata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'architettura del Registro FA supporta diversi pattern di coordinamento che riflettono distinte esigenze operative:

  1. **FA della Pubblica Amministrazione** (Integrazione Standardizzata): Gli enti pubblici forniscono dati autorevoli attraverso meccanismi regolamentati:

    - **Integrazione PDND**: ``"integration_method": "pdnd"`` per l'accesso standardizzato ai dati pubblici.
    - **Conformità Normativa**: Requisiti di piena trasparenza con pubblicazione pubblica nel catalogo.
    - **Requisiti di Audit**: Tracciabilità completa per i processi di emissione di Credenziali pubbliche.

  2. **FA del Settore Privato** (Integrazione Flessibile): Le entità private forniscono dati specializzati tramite accordi personalizzati:

    - **API Personalizzate**: ``"integration_method": "pdnd"`` per l'accesso ai dati specifici del business.
    - **Conformità Normativa**: Requisiti di piena trasparenza con pubblicazione pubblica nel catalogo.
    - **Selective Disclosure**: Visibilità pubblica limitata con flussi di approvazione specifici per EI.
    - **Flessibilità Aziendale**: Integrazione su misura a supporto di casi d'uso diversificati del settore privato.

Questo approccio consente sia la **trasparenza normativa** per la pubblica amministrazione sia la **flessibilità aziendale** per le entità del settore privato, mantenendo al contempo un accesso coordinato ai dati nell'intero ecosistema.

Struttura del Registro FA
^^^^^^^^^^^^^^^^^^^^^^^^^

Durante la registrazione, le Fonti Autentiche dichiarano le proprie capacità prima che le tipologie di Credenziale esistano nel catalogo. Questa dichiarazione costituisce la base per la successiva registrazione degli EI e la creazione delle tipologie di Credenziale.

Schema di Identificazione Univoca delle FA
""""""""""""""""""""""""""""""""""""""""""

A ciascuna Fonte Autentica DEVE essere assegnato un identificatore univoco che segue lo schema URL HTTPS definito di seguito. Questo identificatore è utilizzato per referenziare le entità FA nell'intero sistema di registro e nel Catalogo delle Credenziali Digitali, garantendo la coerenza con i pattern di identificazione delle entità di OpenID Federation.

**Schema di Identificazione FA:**

.. code-block:: text

  https://{organization_domain}[/{optional_path}]

**Componenti dello Schema:**

- **organization_domain**: Dominio DNS controllato dall'organizzazione
- **optional_path**: Componente di percorso aggiuntivo per servizi o dipartimenti specifici

L'identificatore FA DEVE seguire le seguenti regole normative:

1. **Protocollo HTTPS**: DEVE utilizzare lo schema HTTPS per sicurezza e verifica della fiducia
2. **Proprietà del Dominio**: L'organizzazione DEVE controllare il dominio DNS utilizzato nell'identificatore
3. **Unicità**: Garantita attraverso l'unicità del namespace DNS
4. **Stabilità**: DOVREBBE rimanere stabile nel tempo per evitare la rottura dei riferimenti
5. **Risolvibilità**: L'URL DOVREBBE essere risolvibile (ma non è obbligatorio che restituisca contenuto)

**Esempi di identificatori FA conformi:**

- ``https://motorizzazione.gov.example``: Pubblico - Ministero dei Trasporti, Direzione Motorizzazione
- ``https://registry.anpr.example``: Pubblico - Anagrafe Nazionale della Popolazione Residente
- ``https://api.bank.example/auth-source``: Privato - Servizi Finanziari Banca Esempio

Parametri del Registro delle Fonti Autentiche
"""""""""""""""""""""""""""""""""""""""""""""

Il Registro delle Fonti Autentiche DEVE contenere i seguenti parametri per ciascuna Fonte Autentica registrata:

.. list-table:: Campi di Primo Livello del Registro delle Fonti Autentiche
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Nome Campo**
     - **Descrizione**
   * - **id**
     - OBBLIGATORIO. Identificatore univoco del Registro delle Fonti Autentiche (es. ``urn:authentic-sources:it-wallet``).
   * - **version**
     - OBBLIGATORIO. La versione del Registro delle Fonti Autentiche (es. ``1.0.0``).
   * - **last_modified**
     - OBBLIGATORIO. Il timestamp che indica quando l'elenco è stato aggiornato l'ultima volta (es. ``2025-03-15T12:00:00Z``).
   * - **localization**
     - OBBLIGATORIO. Oggetto di configurazione della localizzazione contenente:

       * **default_locale**: Codice locale predefinito (es. ``it``).
       * **available_locales**: Array dei codici locale supportati (es. ``["en", "it"]``).
       * **base_uri**: URI base per il recupero del bundle di localizzazione (es. ``https://trust-registry.eid-wallet.example.it/.well-known/l10n/authentic-sources/``).
       * **version**: Versione del formato del bundle di localizzazione.
   * - **authentic_sources**
     - OBBLIGATORIO. Un Array JSON in cui ogni voce è un Oggetto JSON che rappresenta un'entità Fonte Autentica. Ogni oggetto contiene i parametri definiti nella tabella "Parametri delle Fonti Autentiche" di seguito, inclusi identificazione dell'entità, informazioni organizzative, capacità sui dati e metodi di integrazione.

.. list-table:: Parametri delle Fonti Autentiche
   :class: longtable
   :widths: 25 15 60
   :header-rows: 1

   * - **Parametro**
     - **Tipo**
     - **Descrizione**
   * - **entity_id**
     - string
     - OBBLIGATORIO. Identificatore univoco che segue lo schema normativo: ``https://{organization_domain}[/{optional_path}]``.
   * - **organization_info**
     - oggetto JSON
     - OBBLIGATORIO. Dettagli della persona giuridica e metadati organizzativi.
   * - **organization_info.organization_name_l10n_id**
     - string
     - OBBLIGATORIO. Chiave di localizzazione che fa riferimento al nome localizzato dell'organizzazione nel bundle di localizzazione (es. ``authentic_source1.name``).
   * - **organization_info.organization_type**
     - string
     - OBBLIGATORIO. Classificazione dell'entità: ``"public"`` o ``"private"``.
   * - **organization_info.ipa_code**
     - string
     - OBBLIGATORIO solo per FA Pubbliche. Codice di registrazione IPA per gli enti pubblici.
   * - **organization_info.legal_identifier**
     - string
     - OBBLIGATORIO. Identificativo di registrazione legale (Codice Fiscale/Partita IVA, o equivalente identificativo nazionale per entità straniere).
   * - **organization_info.homepage_uri**
     - string
     - OBBLIGATORIO. URL della homepage dell'organizzazione.
   * - **organization_info.contacts**
     - Array di stringhe
     - OBBLIGATORIO. Array di indirizzi email di contatto per almeno un referente di supporto utenti, uno applicativo e uno sistemistico.
   * - **organization_info.dpa_contact**
     - string
     - OBBLIGATORIO. Indirizzo email del DPA della Fonte Autentica.
   * - **organization_info.policy_uri**
     - string
     - OBBLIGATORIO. URL del documento di informativa sulla privacy.
   * - **organization_info.tos_uri**
     - string
     - OPZIONALE. URL del documento dei termini di servizio.
   * - **organization_info.organization_country**
     - string
     - OBBLIGATORIO. Codice paese ISO 3166-1 alpha-2 a due lettere dell'organizzazione.
   * - **organization_info.logo_uri**
     - string
     - OPZIONALE. URL dell'immagine del logo dell'organizzazione.
   * - **organization_info.logo_uri#integrity**
     - string
     - CONDIZIONALE. Digest crittografico della risorsa immagine del logo per la verifica dell'integrità. OBBLIGATORIO se ``logo_uri`` è presente. Formato: ``{digest_method}-{digest_value}`` (es. ``"sha-256-abc123..."``).
   * - **organization_info.logo_alt_text_l10n_id**
     - string
     - OPZIONALE. Testo alternativo per l'immagine del logo dell'organizzazione.
   * - **organization_info.logo_extended_uri**
     - string
     - OPZIONALE. URL dell'immagine del logo esteso dell'organizzazione.
   * - **organization_info.logo_extended_uri#integrity**
     - string
     - CONDIZIONALE. Digest crittografico della risorsa immagine del logo esteso per la verifica dell'integrità. OBBLIGATORIO se ``logo_extended_uri`` è presente. Formato: ``{digest_method}-{digest_value}`` (es. ``"sha-256-abc123..."``).
   * - **organization_info.logo_extended_alt_text_l10n_id**
     - string
     - OPZIONALE. Testo alternativo per l'immagine del logo esteso dell'organizzazione.
   * - **data_capabilities**
     - Array di oggetti JSON
     - OBBLIGATORIO. Array contenente le specifiche delle capacità sui dati.
   * - **data_capabilities[].dataset_id**
     - string
     - OBBLIGATORIO. Il :term:`Dataset_id` nell'ambito della Fonte Autentica, che PUÒ essere utilizzato come parametro di query per il servizio ``GetAttributeClaims``.
   * - **data_capabilities[].data_origin_l10n_id**
     - string
     - OBBLIGATORIO. Chiave di localizzazione che fa riferimento al nome leggibile dell'origine o del dipartimento che fornisce i dati (es. ``authentic_source1.dataset1.origin``).
   * - **data_capabilities[].intended_purposes**
     - Array di stringhe
     - OBBLIGATORIO. Finalità aziendali soddisfatte, utilizzando gli identificatori di finalità della tassonomia (es. ``["IDENTITY_VERIFICATION", "DRIVING_RIGHTS_VERIFICATION"]``).
   * - **data_capabilities[].available_claims**
     - Array di stringhe
     - OBBLIGATORIO. Claim disponibili da questa capacità dati.
   * - **data_capabilities[].available_claims.claim_name**
     - string
     - OBBLIGATORIO. Contiene il nome del claim.
   * - **data_capabilities[].available_claims.order**
     - number
     - OBBLIGATORIO. Definisce l'ordine in cui le informazioni vengono mostrate.
   * - **data_capabilities[].available_claims.mandatory**
     - boolean
     - OBBLIGATORIO. Definisce se un claim è sempre disponibile o meno.
   * - **data_capabilities[].integration_method**
     - string
     - OBBLIGATORIO. Framework di autorizzazione utilizzato per l'accesso ai dati. DEVE essere ``"pdnd"``.
   * - **data_capabilities[].integration_endpoint**
     - string
     - OPZIONALE. Punto di accesso al servizio (endpoint PDND).
   * - **data_capabilities[].api_specification**
     - string
     - OPZIONALE. URL del documento di specifica `OAS3`_ per questa capacità dati.
   * - **data_capabilities[].data_provision**
     - oggetto JSON
     - OPZIONALE. Capacità di fornitura dei dati e specifiche temporali.
   * - **data_capabilities[].data_provision.immediate_flow**
     - boolean
     - OBBLIGATORIO. Indica se la Fonte Autentica supporta la fornitura immediata dei dati.
   * - **data_capabilities[].data_provision.deferred_flow**
     - boolean
     - OBBLIGATORIO. Indica se la Fonte Autentica supporta la fornitura differita dei dati.
   * - **data_capabilities[].data_provision.max_response_time_minutes**
     - integer
     - CONDIZIONALE. Tempo massimo in minuti per la risposta della Fonte Autentica a una richiesta di fornitura dati differita. OBBLIGATORIO se ``deferred_flow`` è ``true``.
   * - **data_capabilities[].data_provision.notification_methods**
     - Array di stringhe
     - CONDIZIONALE. Array dei metodi di notifica supportati dalla Fonte Autentica per la fornitura dati differita, come ``"push"``, ``"poll"``. OBBLIGATORIO se ``deferred_flow`` è ``true``.
   * - **data_capabilities[].user_information_l10n_id**
     - string
     - OPZIONALE. Chiave di localizzazione che fa riferimento a una stringa in formato Markdown con informazioni leggibili sulla capacità dati rilevanti per l'Utente (es. ``authentic_source1.dataset1.userinfo``). Questa stringa DEVE essere fornita dalla Fonte Autentica al Trust Anchor durante l'onboarding. La formattazione Markdown può essere testo semplice o una combinazione di testo e link. Ad esempio, se il database della Fonte Autentica contiene solo dati registrati *dopo* una data specifica, questa informazione DEVE essere comunicata tramite questa chiave.
   * - **data_capabilities[].service_documentation_uri**
     - string
     - OPZIONALE. URL che punta alla documentazione del servizio della Fonte Autentica.
   * - **data_capabilities[].update_frequency**
     - string
     - OPZIONALE. Indica la frequenza con cui la Fonte Autentica aggiorna i propri dati. Valori possibili: ``"real_time"`` (aggiornamenti quasi in tempo reale, tipicamente entro minuti), ``"daily"``, ``"weekly"``, ``"monthly"``, ``"on_demand"``.
   * - **data_capabilities[].logo_uri**
     - string
     - OPZIONALE. URL dell'immagine del logo relativa ai dati.
   * - **data_capabilities[].logo_uri#integrity**
     - string
     - CONDIZIONALE. Digest crittografico della risorsa immagine del logo per la verifica dell'integrità. OBBLIGATORIO se ``logo_uri`` è presente. Formato: ``{digest_method}-{digest_value}`` (es. ``"sha-256-abc123..."``).
   * - **data_capabilities[].logo_alt_text_l10n_id**
     - string
     - OPZIONALE. Testo alternativo per l'immagine del logo dell'organizzazione.
   * - **data_capabilities[].background_color**
     - string
     - OPZIONALE. Valore stringa del colore di sfondo da visualizzare insieme ai dati.
   * - **data_capabilities[].contacts**
     - Array di stringhe
     - OPZIONALE. Array di indirizzi email di contatto del servizio clienti o dei canali di supporto per gli utenti.

.. note::
  Per ulteriori dettagli sulle funzionalità richieste e sul risultato atteso in termini di esperienza utente, si rimanda alla Sezione :ref:`functionalities:Ottenimento degli Attestati Elettronici di Attributi` per il parametro ``data_capabilities.user_information`` e alla Sezione :ref:`functionalities:Focus sugli Attestati Elettronici di Attributi` per i parametri ``organization_info.logo_uri``, ``organization_info.logo_extended_uri``, ``data_capabilities.logo_uri``, ``data_capabilities.background_color`` e ``data_capabilities.available_claims.order``.

Esempio di Registro FA
""""""""""""""""""""""

Di seguito è fornito un esempio non normativo della struttura del Registro FA:

.. literalinclude:: ../../examples/as-registry-example.json
  :language: JSON

.. note::
  Per una gestione migliore e più efficiente della localizzazione delle informazioni contenute nel Registro delle Fonti Autentiche, un'Entità che lo consulta DOVREBBE:

  - Scaricare la versione base del Registro delle Fonti Autentiche (compatta, senza localizzazioni) utilizzando l'endpoint ``.well-known/authentic-sources``.
  - Determinare la lingua preferita dall'Utente.
  - Scaricare solo i bundle di localizzazione necessari.
  - Unire dinamicamente il contenuto localizzato con la struttura del Registro delle Fonti Autentiche.

Di seguito è fornito un esempio non normativo dell'output di un bundle di localizzazione:

.. code-block:: json

  {
    "authentic_source1.name": "Ministero delle infrastrutture e dei trasporti",
    "authentic_source1.dataset1.origin": "MIT -- Direzione Generale per la Motorizzazione",
    "authentic_source1.dataset1.userinfo": "###### Patente di Guida\nSono disponibili le patenti rilasciate dopo il 1° gennaio 2020. Per le patenti più vecchie, contattare l'ufficio motorizzazione locale.",
    "authentic_source2.name": "Banca Esempio SpA",
    "authentic_source2.dataset1.origin": "Esempio origine dei dati 1",
    "authentic_source2.dataset1.userinfo": "###### Informazioni sulla disponibilità dei dati\nL'accesso ai dati finanziari richiede il consenso del cliente ed è soggetto alla normativa PSD2. Le informazioni sui conti sono disponibili solo per i conti attivi.",
    "...": "..."
  }

I bundle di localizzazione DEVONO essere disponibili all'URI composto aggiungendo il codice locale e ``.json`` al valore ``localization.base_uri`` definito nel registro. Ciascun bundle locale DEVE essere accessibile seguendo il pattern di denominazione **{locale_code}.json**, dove **{locale_code}** è sostituito con il codice locale corrispondente dall'array **available_locales**.

Un esempio non normativo dell'URI di localizzazione italiana per il bundle sarebbe **https://trust-registry.eid-wallet.example.it/.well-known/l10n/authentic-sources/it.json**.

Coordinamento FA-EI
^^^^^^^^^^^^^^^^^^^

A seguito della registrazione FA, il Registro FA consente agli Emittenti di Credenziali di individuare entità FA idonee e richiedere l'approvazione dell'integrazione. Questo processo di coordinamento è descritto in dettaglio in :ref:`entity-onboarding:Processo di Autorizzazione dalla Fonte Autentica all'Emittente di Credenziali`.

Registro della Federazione
--------------------------

Il **Registro della Federazione** fornisce l'infrastruttura di fiducia crittografica per tutti i partecipanti all'ecosistema IT-Wallet. Il Registro della Federazione mantiene l'elenco autorevole delle entità fidate e il loro stato operativo utilizzando endpoint specifici della federazione come definito in :ref:`trust-infrastructure:Endpoint API di Federazione`.

Ruolo di Integrazione del Registro
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All'interno dell'architettura del Registro di Sistema IT-Wallet, il Registro della Federazione funge da **livello di validazione della fiducia** per:

1. **Autenticazione delle Entità**: Valida l'identità crittografica di tutti i partecipanti prima delle operazioni di registro
2. **Verifica della Catena di Fiducia**: Fornisce il fondamento crittografico per la validazione delle entità Emittenti di Credenziali, Relying Party e Fornitori di Wallet
3. **Verifica della Conformità**: Mantiene i Trust Mark che attestano la conformità normativa e lo stato operativo

Accesso al Registro della Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le operazioni del Registro della Federazione sono accessibili attraverso gli endpoint di federazione del Trust Anchor come dettagliato in :ref:`trust-infrastructure:Endpoint API di Federazione`. L'architettura di discovery del registro fornisce informazioni sugli endpoint di federazione tramite l'endpoint di discovery del registro descritto in `Endpoint di Discovery del Registro`_.

.. note::
   Gli endpoint di federazione sono disponibili sia attraverso il meccanismo di discovery del registro (per l'accesso unificato al registro) sia attraverso la Configurazione dell'Entità del Trust Anchor all'indirizzo ``.well-known/openid-federation`` (per operazioni specifiche della federazione). Entrambe le sorgenti forniscono gli stessi URL degli endpoint ma servono diversi pattern di discovery: la discovery del registro per l'orientamento iniziale nell'ecosistema, la Configurazione dell'Entità per la conformità standard a OpenID Federation 1.0.

   Per le specifiche tecniche complete dei protocolli di federazione, le configurazioni delle entità, i meccanismi di valutazione della fiducia e la validazione della catena di fiducia, vedere :ref:`trust-infrastructure:L'Infrastruttura di Trust`.

Catalogo degli Attestati Elettronici
------------------------------------

Il Catalogo delle Credenziali Digitali è il registro di tutte le Credenziali Digitali disponibili riconosciute nell'ecosistema IT-Wallet. È pubblicato dal Trust Anchor ed è pubblicamente disponibile per tutte le Entità tramite un endpoint specializzato della Federazione. Funge da unico punto di riferimento per tutti gli attori coinvolti nel processo di emissione, verifica e utilizzo delle Credenziali Digitali.

Il Catalogo delle Credenziali Digitali si prefigge di:

  1. Facilitare la discovery delle Credenziali Digitali per gli Utenti.
  2. Standardizzare la descrizione tecnica e funzionale delle Credenziali Digitali.
  3. Abilitare l'interoperabilità tra diversi Emittenti e Relying Party.
  4. Semplificare il processo di integrazione per i Fornitori di Wallet e le Relying Party.
  5. Garantire la fiducia nell'ecosistema attraverso informazioni verificabili e attendibili.
  6. Fornire trasparenza sull'ecosistema delle Credenziali Digitali disponibili.

Le principali Entità coinvolte nel Catalogo delle Credenziali Digitali sono:

  - **Trust Anchor**: Gestisce e mantiene il Catalogo delle Credenziali Digitali, garantendone l'autenticità e l'integrità.
  - **Organismo di Vigilanza**: Interagisce con il Trust Anchor e il Catalogo delle Credenziali Digitali per monitorare la fase di registrazione garantendo sicurezza e privacy secondo la normativa nazionale/europea, mantenendo tutte le informazioni affidabili e aggiornate.
  - **Emittenti di Credenziali Digitali**: Le entità autorizzate a emettere Credenziali Digitali, registrandole nel Catalogo.
  - **Relying Party**: Utilizzano il Catalogo delle Credenziali Digitali per raccogliere tutte le informazioni necessarie sulle Credenziali Digitali che intendono richiedere durante la fase di presentazione.
  - **Fornitori di Wallet**: Accedono al Catalogo delle Credenziali Digitali per identificare le Credenziali Digitali disponibili e recuperare tutte le informazioni necessarie per integrarle nelle proprie Soluzioni Wallet.
  - **Utenti**: Gli Utenti che utilizzano indirettamente il Catalogo delle Credenziali Digitali attraverso le proprie Istanze Wallet per scoprire e richiedere Credenziali Digitali.
  - **Fonti Autentiche**: Le Entità che detengono i dati originali attestati nelle Credenziali Digitali. Forniscono supporto agli Emittenti nella registrazione delle Credenziali Digitali nel Catalogo.

.. _fig_catalog:
.. plantuml:: plantuml/credential-catalog-entities.puml
    :width: 99%
    :alt: La figura illustra le Entità delle Credenziali Digitali.
    :caption: `Diagramma Entità-Relazione del Catalogo delle Credenziali Digitali. <https://www.plantuml.com/plantuml/svg/ZLJ1Rkis4BpxAxP6WQP00X-QtjeWgPEsFXGmuXGz6ZIvbeb8fCfTEbM__YrDELAUb6ST34khuSnmESjxOXKuLYKysiAoAc4PqA1ZcnwL57mH4Pwam1Pfzfrrkem6uPVbxM9vkrtwglPEy7UpsG_mY7lh43RhvzNBqwO7vbWh4tvQQ5zLtjsDVDbxnpVg3SbNUFFpGcDWkxTQCKv06p6wKpG5MdhzEW4M2GDDyUcBAJ1XEsAO07p5PgAx2J1hjbe5Cm69_-c3SWLkLSbJ-etqohwUW7nJPOaNAHVM4LkER5CuPhFtL5tfSmIlOJvCA7KHdGlW6GjB79hql1H4471eQ-3t85v07PKjrQv46A6JXTzJ7IpZh_DpfkO_Yg4r1lBkAlLTkF-MlvE6PVi_EeAtWmTZINivP53EYEg_4OalQIG-uU-soo4IFpXzy4dd9Rr1VarwwVUNSgf0EgbKoZgM7m4Vy9i3t1ULY8dcfY76wefYBT6qv4FpcpUD26ow2gJIITGxopxGkPig7HJK1qK8w2W6wmeWrFB0pScQQ1sLRlgwlP7kz2rHn42Zfmkh_34vU8WiJP1k6y3sBf9DAuP4SF4isq7eP0EMZNXUgv2OKdHo0ThAF9_ogQ_l4GJsK2Wf1R1kxqELsw1sFZBeSUN-O7NoUIhMmH-joRl_vrI1jjJkMMia6dgmZh48Yh4lcgeUCl471xdKQIlfP5gZDpu64KX2vnAqjQJ-foyD-22DTTBOD0sWc54uZ6XTx7Wtq6c0fBqVijrjg8lqTPVd7A6uAoqTiflVHQMD7JfJUm4Ahz0E4_nnXbQEPQ5c6LBBX_4rVJkVXZtuT1gPe8jjVs6-VZ2CzGQiQvSE-tyc6pSxo6fVyezFuZXc8TCDizVnTP7pO4_BzatlmjG3hdmV3XZJw12qaLuvOkKqGfq11dPDNhvzR0dw3bREs82Qo-RzHgN-bKfVsRYNECIg_080>`_

La seguente tabella riepiloga le principali informazioni che DEVONO essere fornite dal Catalogo delle Credenziali Digitali:

.. list-table:: Catalogo delle Credenziali Digitali - Informazioni principali
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Informazioni relative a**
     - **Descrizione**
   * - Metadati della Credenziale Digitale
     - Informazioni identificative essenziali e caratteristiche della Credenziale Digitale, tra cui:

       - **Identificatore univoco della Credenziale**: Una stringa identificativa univoca per ciascuna Credenziale Digitale.
       - **Metodi di autenticazione dell'Utente**: Meccanismi di autenticazione dell'Utente utilizzati per richiedere la Credenziale Digitale, se richiesti dagli Emittenti o dalle Fonti Autentiche.
       - **Livello Minimo di Garanzia**: Il Livello Minimo di Garanzia richiesto per l'affidabilità della Credenziale Digitale. DEVE tener conto del Livello di Garanzia dell'autenticazione dell'Utente, ove applicabile, e dell'Istanza Wallet.
   * - Emittenti della Credenziale Digitale
     - Dettagli sull'organizzazione autorizzata a emettere la Credenziale Digitale, quali:

       - **Identificatori dell'Emittente**: Identificatore univoco dell'emittente della Credenziale Digitale.
       - **Tipologia dell'Emittente**: Classificazione come fornitore PID, (Q)EAA o Pub-EAA.
       - **Informazioni aggiuntive**: Dettagli organizzativi inclusi nome, codice e informazioni di contatto.
   * - Fonti Autentiche
     - Informazioni sulla fonte di dati autorevole.
   * - Specifica Tecnica
     - Dettagli tecnici, tra cui:

       - **Schemi della Credenziale Digitale**: Specifiche del framework e della struttura.
       - **Formati della Credenziale Digitale**: Standard di formato e codifica dei dati.
       - **Politica di autenticazione**: Metodi e requisiti per la verifica.
   * - Termini di Utilizzo
     - Condizioni e limitazioni per l'utilizzo della Credenziale Digitale, quali:

       - **Validità della Credenziale**: Periodo di tempo durante il quale la Credenziale Digitale è valida e, ove applicabile, meccanismi e dettagli tecnici per invalidare le Credenziali Digitali (metodi di revoca/sospensione).
       - **Politica di restrizione**: Se applicabile, regole che disciplinano l'utilizzo e le limitazioni della Credenziale Digitale secondo la normativa nazionale. Viene utilizzata, ad esempio, per specificare se solo specifiche tipologie di entità legali, come i Fornitori Pub-EAA e le Soluzioni Wallet pubbliche, sono autorizzate a emettere e ottenere la Credenziale Digitale.
       - **Politica di prezzo**: Informazioni relative ai modelli di prezzo della Credenziale Digitale, come `free`, `issuance_based`, `verification_based`.
       - **Finalità della Credenziale Digitale**: Informazioni relative alle finalità consentite per cui la Credenziale Digitale può essere utilizzata. Ogni tipologia di Credenziale Digitale può essere utilizzata per più finalità.

Il Trust Anchor DEVE pubblicare e mantenere aggiornate tutte le informazioni all'endpoint `.well-known` del Catalogo delle Credenziali Digitali garantendo affidabilità, autenticità e integrità dei dati. In particolare, il Catalogo delle Credenziali Digitali DEVE essere disponibile attraverso l'endpoint ``.well-known/credential-catalog``. DEVE supportare ``application/jose`` come content-type.

Di seguito è riportato un esempio non normativo.

.. code-block:: http

    GET /.well-known/credential-catalog HTTP/1.1
    Host: trust-anchor.eid-wallet.example.it
    Accept: application/jose

    HTTP/1.1 200 OK
    Content-Type: application/jose

    eyJhbGciOiJSUzI1NiIsImtpZCI6ImV4YW1w...

Nella sezione :ref:`registry:Struttura del Catalogo degli Attestati Elettronici` è fornito un esempio del Catalogo delle Credenziali Digitali decodificato in JSON.

Gerarchia delle Credenziali Digitali
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Credenziali Digitali riconosciute nell'ecosistema IT-Wallet sono classificate e standardizzate secondo il seguente modello gerarchico multilivello, progettato per migliorare la chiarezza semantica, la discovery delle credenziali e la compatibilità con i flussi di verifica sia credential-specific che claim-based.

La gerarchia è definita come segue:

**Dominio**

Un **Dominio** rappresenta un'area tematica di alto livello che raggruppa famiglie di Credenziali afferenti allo stesso contesto generale (es. Identità, Salute, Istruzione, Mobilità).
I Domini forniscono un livello organizzativo di primo piano.

**Classe di Credenziale**

Una **Classe di Credenziale** rappresenta una famiglia di Credenziali che condividono natura, funzione o struttura simili (es. Documenti di Identità, Certificati di Stato Civile).

Ogni Classe DOVREBBE definire:

- un identificatore di Classe stabile (URI),
- la semantica attesa della Famiglia di Credenziali.

Le Classi consentono alle Relying Party e alle Soluzioni Wallet di richiedere o abbinare le Credenziali in base alla loro categoria tipologica.

**Tipologia di Credenziale**

Una **Tipologia di Credenziale** rappresenta una Credenziale specifica all'interno di una Classe (es. Credenziale di Viaggio Digitale, Certificato di Nascita, Patente di Guida Mobile).
Ogni Tipologia di Credenziale DEVE includere:

- un identificatore univoco,
- l'identificatore dell'Emittente della Credenziale,
- l'insieme degli Attributi che possono essere inclusi nelle presentazioni.

Le Tipologie di Credenziale consentono il targeting preciso per i flussi di verifica conformi o normativamente mandatati.

**Finalità (Intento di Verifica)**

Una **Finalità (Intento di Verifica)** descrive *perché* una credenziale può essere richiesta da una Relying Party (es. Verifica dell'Identità, Verifica dell'Età, Idoneità a servizi specifici).
Le Finalità DEVONO descrivere **gli esiti della verifica**.
Ogni Tipologia di Credenziale DEVE dichiarare il proprio Dominio, Classe e Finalità supportate.

Le tabelle seguenti forniscono esempi non esaustivi che illustrano le relazioni tra Domini, Classi di Credenziale e Tipologie di Credenziale, seguiti dalla loro mappatura sulle Finalità di verifica.
Domini, Classi, Credenziali specifiche e Finalità di verifica aggiuntive **POSSONO** essere aggiunti nel tempo con l'evolversi dell'ecosistema IT-Wallet.

.. list-table:: Tassonomia delle Credenziali Digitali: Gerarchia e Classificazione
   :class: longtable
   :header-rows: 1
   :widths: 15 25 30 30

   * - **Dominio**
     - **Descrizione**
     - **Classe di Credenziale**
     - **Tipologia di Credenziale**

   * - *IDENTITÀ*
     - Credenziali che stabiliscono o confermano l'identità legale di una persona e il suo status personale, civile o giuridico.
     -
       * Documenti di Identità
       * Certificati Anagrafici e di Stato Civile
       * Stato Economico e Giuridico
     -
       * Credenziale di Viaggio Digitale
       * Patente di Guida Mobile (solo Italia)
       * Codice Fiscale / Tessera Sanitaria
       * Certificazione dell'Età
       * Certificato di Nascita
       * Certificato di Residenza
       * Certificato di Stato di Famiglia
       * Certificato di Matrimonio
       * Certificato di Cittadinanza
       * ISEE (Indicatore della Situazione Economica Equivalente)
       * Permesso di Soggiorno
       * Certificato dei Carichi Pendenti
       * Certificato del Casellario Giudiziale

   * - *CASA E FAMIGLIA*
     - Credenziali che attestano la composizione del nucleo familiare, la residenza e i rapporti giuridici o fiscali legati all'abitazione.
     -
       * Documenti Catastali e Immobiliari
       * Documenti Familiari
       * Documenti Tributari Locali
     -
       * Atto di Compravendita
       * Visura Catastale
       * Planimetria Catastale
       * Certificato Catastale
       * Codice Fiscale/Tessera Sanitaria dei Figli
       * Certificato di Nascita
       * Certificato di Stato di Famiglia
       * IMU (Imposta Municipale Propria)
       * TARI (Tassa sui Rifiuti)

   * - *ISTRUZIONE*
     - Credenziali che attestano risultati scolastici, titoli accademici e formazione professionale.
     -
       * Titoli di Studio
       * Certificazioni Professionali
     -
       * Diploma di Licenza Media
       * Diploma di Istruzione Secondaria Superiore
       * Laurea Triennale
       * Laurea Magistrale
       * Master Universitario
       * Dottorato di Ricerca
       * Albi Professionali (es. architetto, avvocato)
       * Attestati di Formazione Professionale
       * Certificazioni Linguistiche (es. IELTS)
       * Qualifiche Accademiche (es. Europass)

   * - *SALUTE*
     - Credenziali relative alla copertura sanitaria, allo stato di salute e a certificazioni di carattere sanitario.
     -
       * Certificazioni e Idoneità
       * Cartelle Cliniche
     -
       * Tessera Sanitaria (TEAM)
       * Tessera Europea di Assicurazione Malattia (CED)
       * Certificato di Disabilità
       * Certificato di Vaccinazione
       * Certificato di Idoneità Sportiva
       * Certificato di Idoneità al Lavoro
       * Prescrizioni Mediche
       * Referto Medico Digitale

   * - *FINANZIARIO*
     - Credenziali relative a strumenti di pagamento, autorizzazioni finanziarie e prove di pagamento.
     -
       * Strumenti di Pagamento
       * Credenziali e Autorizzazioni di Pagamento
       * Pagamenti e Tributi Pubblici
       * Pagamenti Ricorrenti e Abbonamenti
     -
       * Carta di Pagamento Digitale (debito / credito / prepagata)
       * Carta Virtuale
       * Conto Bancario (IBAN)
       * Credenziale di Strong Customer Authentication (SCA)
       * Ricevuta di Pagamento
       * Bollo Digitale
       * Certificato di Pagamento di Tasse e Tributi
       * Mandato di Abbonamento
       * Credenziale di Pagamento Ricorrente

   * - *CULTURA E TEMPO LIBERO*
     - Credenziali che attestano l'appartenenza, l'affiliazione o la partecipazione a programmi culturali o ricreativi.
     -
       * Carte e Benefici Culturali
       * Programmi di Fidelizzazione e Associativi
     -
       * Carta della Cultura
       * Abbonamenti Annuali ai Musei
       * Carta Cinema
       * Carta Museo
       * Tessere di Associazione
       * Tessera Bibliotecaria
       * City Pass

   * - *LAVORO*
     - Credenziali che attestano rapporti di lavoro, status professionale e contribuzione previdenziale.
     -
       * Documenti di Lavoro
       * Stato Occupazionale
       * Accesso
     -
       * Contratto di Lavoro Digitale
       * Curriculum Vitae (CV)
       * Permesso di Soggiorno
       * Certificato di Stato Occupazionale
       * Estratto Contributivo INPS
       * Badge di Accesso Fisico

   * - *MOBILITÀ E VIAGGI*
     - Credenziali che attestano diritti di mobilità, stato del veicolo e titolarità in ambito di viaggio.
     -
       * Patenti e Autorizzazioni
       * Documenti del Veicolo
       * Abbonamenti al Trasporto
       * Documenti di Viaggio
       * Assicurazione Viaggio
       * Prenotazioni
       * Sconti e Agevolazioni
     -
       * Patente di Guida Mobile
       * Patente Nautica
       * Certificato di Proprietà del Veicolo
       * Assicurazione RCA Digitale
       * Certificato di Revisione del Veicolo
       * Carta Verde / Assicurazione Internazionale
       * Abbonamento ai Trasporti Pubblici
       * Abbonamento Pedaggi Stradali
       * Credenziale di Viaggio Digitale
       * Biglietti di Viaggio (aereo, treno, ecc.)
       * Polizza di Assicurazione Viaggio
       * Prenotazione Hotel
       * Carte Sconto
       * Agevolazioni Turistiche

   * - *BONUS*
     - Credenziali che attestano il diritto a benefici economici, incentivi o voucher.
     -
       * Benefici Economici e Sussidi
       * Incentivi e Voucher
       * Bonus Salute e Benessere
     -
       * Credenziale Assegno Familiare
       * Credenziale Indennità di Disoccupazione
       * Voucher Digitale
       * Credenziale Incentivo all'Acquisto
       * Credenziale Idoneità Cashback
       * Credenziale Bonus Sanitario
       * Voucher Supporto Salute Mentale
       * Bonus Sport e Attività Fisica

.. list-table:: Tabella 2: Mappatura tra Classi di Credenziale e Finalità
   :class: longtable
   :header-rows: 1
   :widths: 40 60

   * - **Classe di Credenziale**
     - **Finalità Supportate**

   * - Documenti di Identità
     -
       * Verifica dell'identità
       * Verifica dell'età
       * Identificazione della persona
   * - Certificati Anagrafici e di Stato Civile
     -
       * Verifica dello stato civile
       * Diritto di residenza
       * Verifica della composizione del nucleo familiare
   * - Stato Economico e Giuridico
     -
       * Idoneità a servizi o benefici
       * Verifica dello stato giuridico
       * Verifica del casellario giudiziale
   * - Documenti Catastali e Immobiliari
     -
       * Verifica di residenza e nucleo familiare
       * Verifica della proprietà immobiliare
       * Conformità urbanistica e catastale
   * - Documenti Familiari
     -
       * Verifica della composizione del nucleo familiare
       * Idoneità ai servizi sociali basati sul nucleo familiare
   * - Documenti Tributari Locali
     -
       * Conformità agli obblighi tributari locali
       * Verifica dello stato dell'imposta sulla proprietà
   * - Titoli di Studio
     -
       * Verifica del titolo e del grado accademico
       * Idoneità ai percorsi formativi
   * - Certificazioni Professionali
     -
       * Verifica dell'abilitazione professionale
       * Valutazione delle competenze ai fini lavorativi
   * - Certificazioni e Idoneità
     -
       * Verifica dello stato vaccinale
       * Verifica dello stato di idoneità
       * Accesso ad aree con restrizioni sanitarie
   * - Cartelle Cliniche
     -
       * Accesso ai servizi sanitari
       * Condivisione della documentazione medica
       * Validazione della storia clinica
   * - Strumenti di Pagamento
     -
       * Autorizzazione al pagamento
       * Esecuzione del pagamento
       * Prova di pagamento
   * - Credenziali e Autorizzazioni di Pagamento
     -
       * Gestione delle autorizzazioni finanziarie
       * Strong Customer Authentication (SCA)
   * - Pagamenti e Tributi Pubblici
     -
       * Prova di pagamento delle tasse
       * Prova di pagamento dei tributi
       * Validazione del bollo digitale
   * - Pagamenti Ricorrenti e Abbonamenti
     -
       * Gestione dei pagamenti ricorrenti
       * Verifica del mandato di abbonamento
   * - Carte e Benefici Culturali
     -
       * Accesso ai servizi culturali
       * Accesso ai servizi ricreativi
       * Applicazione degli sconti per i soci
   * - Programmi di Fidelizzazione e Associativi
     -
       * Verifica dell'affiliazione
       * Verifica della partecipazione
       * Utilizzo dei benefici fedeltà
   * - Documenti di Lavoro
     -
       * Verifica dello stato occupazionale
       * Validazione del profilo professionale
   * - Stato Occupazionale
     -
       * Verifica dei contributi previdenziali
       * Idoneità ai benefici correlati all'occupazione
   * - Patenti e Autorizzazioni
     -
       * Verifica dei diritti di guida
       * Verifica dei diritti di navigazione
       * Controlli delle forze dell'ordine
   * - Documenti del Veicolo
     -
       * Verifica dell'immatricolazione del veicolo
       * Verifica della revisione del veicolo
       * Verifica dello stato assicurativo
   * - Abbonamenti al Trasporto
     -
       * Accesso ai servizi di trasporto
       * Verifica dell'abbonamento al trasporto pubblico
   * - Documenti di Viaggio
     -
       * Diritto di viaggio o circolazione
       * Verifica dell'identità per la mobilità transfrontaliera
   * - Assicurazione Viaggio e Prenotazioni
     -
       * Verifica della copertura assicurativa di viaggio
       * Verifica della prenotazione alloggio
       * Verifica della prenotazione di trasporto
   * - Sconti e Agevolazioni
     -
       * Applicazione degli sconti per i soci
       * Accesso alle agevolazioni turistiche
   * - Benefici Economici e Sussidi
     -
       * Verifica dell'idoneità ai benefici familiari
       * Verifica dell'idoneità ai sussidi di disoccupazione
       * Erogazione del supporto economico
   * - Incentivi e Voucher
     -
       * Utilizzo dei voucher digitali
       * Utilizzo degli incentivi all'acquisto
       * Verifica dell'idoneità al cashback
   * - Bonus Salute e Benessere
     -
       * Accesso ai bonus sanitari
       * Utilizzo dei voucher per la salute mentale
       * Utilizzo dei voucher per lo sport
   * - Affiliazione Lavorativa
     -
       * Verifica del permesso di accesso

Ogni Credenziale DEVE specificare domini, classi e finalità per abilitare sia gli **Scenari Credential-Specific** che gli **Scenari Credential-Agnostic** in base ai requisiti della Relying Party e ai pattern di richiesta di presentazione, come definito nelle tabelle di mappatura sopra.

  1. **Scenari Credential-Specific** (Primari per il settore governativo/regolamentato): Le RP richiedono tipologie specifiche di Credenziale per requisiti di conformità e audit, inclusi ad esempio:

    - **Servizi Governativi**: ``"credential_type":"pid"`` per la verifica dell'identità specifica con PID oppure ``"credential_type":"eid"`` per la verifica dell'identità specifica con IT-Wallet ID.
    - **Controlli di Polizia**: ``"credential_type":"mDL"`` per la verifica della patente di guida.
    - **KYC Bancario**: Tipologie specifiche di credenziale previste dalla normativa finanziaria.
    - **Servizi Sanitari**: ``"credential_type":"european_disability_card"`` per l'accesso ai benefici per disabilità conformi EU.

  2. **Scenari Credential-Agnostic** (Tipici per le aziende private): Le RP richiedono claim specifici indipendentemente dalla fonte della Credenziale per l'efficienza operativa, quali:

    - **Consegna E-commerce**: Qualsiasi credenziale, tra quelle a cui è autorizzato ad accedere, contenente ``given_name``, ``family_name``, ``address`` per la spedizione.
    - **Abbonamenti**: Qualsiasi credenziale, tra quelle a cui è autorizzato ad accedere, con ``given_name``, ``email`` per la personalizzazione.
    - **Personalizzazione del Servizio**: Applicazioni aziendali che richiedono dati personali di base senza forti requisiti sulla fonte.

Questo approccio consente:

  - **Autorizzazione basata su politiche** tramite mappature **Dominio / Classe / Tipologia di Credenziale / Finalità**.
  - **Registrazione flessibile delle RP** a supporto sia delle esigenze di conformità governativa che dei requisiti operativi aziendali.

Struttura del Catalogo degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il contenuto del Catalogo delle Credenziali Digitali è protetto in un JWS che contiene i seguenti parametri dell'intestazione JOSE:

.. _table_catalog_parameters:
.. list-table::
   :class: longtable
   :header-rows: 1
   :widths: 25 50 25

   * - **Intestazione JOSE**
     - **Descrizione**
     - **Riferimento**
   * - **typ**
     - OBBLIGATORIO. DEVE essere impostato su ``JOSE``.
     - [:rfc:`7515` Section 4.1.9].
   * - **alg**
     - OBBLIGATORIO. Identificatore di algoritmo di firma digitale come da registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` né con un identificatore di algoritmo simmetrico (MAC).
     - [:rfc:`7515` Section 4.1.1].
   * - **kid**
     - OBBLIGATORIO. Identificatore univoco della chiave pubblica.
     - [:rfc:`7515` Section 4.1.4].
   * - **x5c**
     - OPZIONALE. Contiene il Certificato X.509 della chiave pubblica o la catena di certificati [:rfc:`5280`] corrispondente alla chiave utilizzata per firmare digitalmente il JWS. Quando il parametro di intestazione `kid` è presente, DEVE fare riferimento alla stessa chiave pubblica crittografica foglia utilizzata con il Certificato X.509.
     - [:rfc:`7515` Section 4.1.6.].
   * - **cty**
     - OBBLIGATORIO. DEVE essere impostato su ``application/json``.
     - [:rfc:`7515` Section 4.1.6.].

Il payload JWS contiene i seguenti parametri:

.. list-table:: Campi di Primo Livello del Catalogo delle Credenziali Digitali
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - **Nome Campo**
     - **Descrizione**
   * - **id**
     - OBBLIGATORIO. Identificatore univoco del Catalogo delle Credenziali Digitali (es. ``urn:credential-catalog:it-wallet``).
   * - **version**
     - OBBLIGATORIO. Versione del formato del Catalogo delle Credenziali Digitali.
   * - **last_modified**
     - OBBLIGATORIO. Timestamp dell'ultima modifica al Catalogo delle Credenziali Digitali.
   * - **iss**
     - OBBLIGATORIO. Identificatore dell'emittente del Catalogo delle Credenziali Digitali.
   * - **credentials**
     - OBBLIGATORIO. Array contenente le definizioni delle Credenziali Digitali.

Ogni elemento dell'array ``credentials`` contiene almeno le seguenti informazioni:

.. _table_catalog_parameters_first_level:
.. list-table:: Campi di Primo Livello di Ogni Voce di Credenziale
  :class: longtable
  :header-rows: 1
  :widths: 30 70

  * - **Nome Campo**
    - **Descrizione**
  * - **version**
    - OBBLIGATORIO. Versione della definizione della Credenziale Digitale.
  * - **credential_type**
    - OBBLIGATORIO. Identificatore univoco della tipologia di Credenziale Digitale. Per il PID DEVE essere ``pid`` e per l'IT-Wallet ID DEVE essere ``eid``.
  * - **credential_name_l10n_id**
    - OBBLIGATORIO. Chiave di localizzazione che fa riferimento al nome leggibile della Credenziale Digitale nel bundle di localizzazione (es. ``mDL.name``).
  * - **legal_type**
    - OBBLIGATORIO. Classificazione legale della Credenziale (es. ``pub-eaa``, ``qeaa``, ``eaa``).
  * - **restriction_policy**
    - OPZIONALE. Restrizioni legali sulle Soluzioni Wallet e/o sugli Emittenti di Credenziali autorizzati a richiedere/emettere la Credenziale Digitale.

      * **allowed_wallet_ids**: Elenco degli identificatori delle Soluzioni Wallet consentite.
      * **allowed_issuer_ids**: Elenco degli identificatori degli Emittenti di Credenziali consentiti. Se presente, rappresenta una whitelist di Emittenti di Credenziali che possono essere aggiunti dal Trust Anchor nel campo **issuers** della corrispondente Credenziale Digitale.
      * **presentation_flows**: Tipo di flussi di presentazione supportati; flusso remoto e/o di prossimità.
  * - **pricing_policy**
    - OPZIONALE. Informazioni sul prezzo della Credenziale Digitale, inclusi:

      * **models**: OBBLIGATORIO. Array di modelli di prezzo applicabili alla Credenziale Digitale, ciascuno contenente

        - **pricing_type**: Tipo di modello di prezzo, come ``issuance_based``, ``verification_based``, ``subscription_based``, ``other``.
        - **price**: Costo associato al modello.
        - **currency**: Valuta del prezzo.

      * **pricing_model_uri**: URI alla documentazione dettagliata del modello di prezzo.
  * - **validity_info**
    - Informazioni sulla validità della Credenziale Digitale, inclusi almeno:

      * **max_validity_days**: Periodo massimo di validità in giorni.
      * **status_methods**: Metodi di verifica dello stato supportati (es. ``status_list``).
      * **allowed_states**: Array di oggetti che rappresentano gli stati consentiti della Credenziale Digitale. Ogni oggetto contiene un codice di stato esadecimale (es. ``0x00`` per ``VALID``, ``0x01`` per ``INVALID``, ``0x02`` per ``SUSPENDED``, ``0x03`` per ``UPDATE``, ``0x0F`` per ``ATTRIBUTE_UPDATE``), una chiave di localizzazione ``title_l10n_id`` e una chiave di localizzazione ``description_l10n_id`` per la visualizzazione nell'interfaccia utente.
      * **administrative_expiration_user_info**: OPZIONALE. Oggetto contenente chiavi ``title_l10n_id`` e ``description_l10n_id`` per visualizzare le informazioni sulla scadenza amministrativa all'Utente.
  * - **authentication**
    - OBBLIGATORIO. Requisiti di autenticazione della Credenziale Digitale.

      * **user_auth_required**: OBBLIGATORIO. Flag che indica se l'autenticazione dell'Utente è richiesta durante l'emissione della Credenziale Digitale.
      * **min_loa**: OBBLIGATORIO. Livello Minimo di Garanzia richiesto per l'autenticazione della Credenziale Digitale. DEVE includere il Livello di Garanzia dell'autenticazione dell'Utente e dell'Istanza Wallet che richiede la Credenziale Digitale.
      * **supported_schemes**: OBBLIGATORIO se ``user_auth_required`` è ``true``. Schemi di autenticazione dell'identità digitale supportati (es. ``["it_wallet"]``).
  * - **domains**
    - OBBLIGATORIO. Array contenente gli ID dei domini a cui appartiene la Credenziale Digitale (es. ``"IDENTITY"``, ``"MOBILITY_TRAVEL"``).
  * - **classes**
    - OBBLIGATORIO. Array contenente gli ID delle classi a cui appartiene la Credenziale Digitale (es. ``"IDENTIFICATION_DOCUMENTS"``, ``"LICENSES_AUTHORIZATIONS"``).
  * - **purposes**
    - OBBLIGATORIO. Array contenente gli ID delle finalità (definita nella Tassonomia) di utilizzo per cui la Credenziale Digitale può essere impiegata, definendo contesti d'uso specifici e claim richiesti per ciascuna finalità (es. ``"IDENTITY_VERIFICATION"``, ``"AGE_VERIFICATION"``, ``"DRIVING_RIGHTS_VERIFICATION"``).
  * - **issuers**
    - OBBLIGATORIO. Array di informazioni rilevanti sugli Emittenti di Credenziali autorizzati, inclusi dati amministrativi e tecnici quali nome dell'organizzazione, riferimento al documento di specifica API e meccanismi di emissione supportati. Ogni elemento dell’array contiene:

       * **entity_id**: OBBLIGATORIO. Stringa. Identificativo univoco del Credential Issuer. DEVE corrispondere al valore contenuto nel parametro ``iss`` dell’Entity Configuration del Credential Issuer.
       * **organization_name_l10n_id**: OBBLIGATORIO. Stringa. Chiave di localizzazione che fa riferimento al nome localizzato dell’organizzazione nel bundle di localizzazione (es. ``issuer1.name``).
       * **organization_code**: OBBLIGATORIO. Stringa. Codice IPA del Credential Issuer per enti pubblici oppure partita IVA per soggetti privati.
       * **organization_country**: OBBLIGATORIO. Stringa. Codice paese dell’organizzazione a due lettere conforme allo standard ISO 3166-1 alpha-2.
       * **contacts**: OBBLIGATORIO. Stringa. Array di indirizzi email di contatto per almeno un referente di supporto utenti, uno applicativo e uno specialista di sistemi.
       * **legal_type**: OBBLIGATORIO. Stringa. Classificazione giuridica del Credential Issuer (es. pub-eaa, qeaa, eaa).
       * **homepage_uri**: OBBLIGATORIO. Stringa. URL che punta alla homepage dell’organizzazione.
       * **logo_uri**: OPZIONALE. Stringa. URL dell’immagine del logo dell’organizzazione.
       * **policy_uri**: OBBLIGATORIO. Stringa. URL al documento di privacy policy.
       * **tos_uri**: OPZIONALE. Stringa. URL al documento di termini di servizio.
       * **service_documentation_uri**: OPZIONALE. Stringa. URL che punta alla documentazione del servizio del Credential Issuer.
       * **issuance_flows**: OBBLIGATORIO. Oggetto. Contiene i seguenti parametri:

          * **deferred_flow**: OBBLIGATORIO. Booleano. Indica se è supportata l’emissione differita.
          * **immediate_flow**: OBBLIGATORIO. Booleano. Indica se è supportata l’emissione immediata.
          * **wallet_initiated**: OBBLIGATORIO. Booleano. Indica se è supportato il flusso Wallet-Initiated.
          * **issuer_initiated**: OBBLIGATORIO. Booleano. Indica se è supportata il flusso Issuer-Initiated (Third Party Initiated Flow).
          * **max_deferred_issuance_time_minutes**: CONDIZIONALE. Intero. Tempo massimo, in minuti, per la disponibilità dell’emissione della credenziale. OBBLIGATORIO se ``deferred_flow`` è impostato a ``true``.
          * **notification_methods**: CONDIZIONALE. Array di stringhe. Contiene i metodi di notifica supportati dal Credential Issuer per l’emissione differita, come ``"push"``, ``"poll"``. OBBLIGATORIO se ``deferred_flow`` è impostato a ``true``.

  * - **localization**
    - OBBLIGATORIO. Oggetto di configurazione della localizzazione contenente:

       * **default_locale**: Codice locale predefinito (es. ``it``).
       * **available_locales**: Array dei codici locale supportati (es. ``["en", "it"]``).
       * **base_uri**: URI base per il recupero del bundle di localizzazione (es. ``https://trust-registry.eid-wallet.example.it/.well-known/l10n/credential-catalog/``).
       * **version**: Versione del formato del bundle di localizzazione.
  * - **authentic_sources**
    - CONDIZIONALE. È OBBLIGATORIO solo se ``parent_credentials`` è assente. Array di oggetti JSON delle Fonti Autentiche che fanno riferimento alle Fonti Autentiche autorizzate. Ogni oggetto DEVE contenere l'identificatore dell'entità FA e l'identificatore specifico della capacità dati:

      * **id**: Identificatore stringa che fa riferimento all'entity_id della Fonte Autentica come registrato in :ref:`registry:Registro delle Fonti Autentiche`.
      * **dataset_id**: Identificatore stringa della specifica capacità dati/dataset utilizzato dall'Emittente dalla FA.
  * - **parent_credentials**
    - CONDIZIONALE. È OBBLIGATORIO solo se ``authentic_sources`` è assente. Array degli identificativi di ``credential_type`` relativi a Credenziali designate come fonti dei dati. Ogni elemento identifica una Credenziale che funge da Fonte Autentica durante il processo di emissione della Credenziale Digitale.

.. note::
  L'unione di ``credential_type`` e ``version`` DEVE essere univoca nel Catalogo delle Credenziali.

Il corrispondente esempio di Catalogo delle Credenziali Digitali decodificato in JSON sia per l'intestazione che per il payload è il seguente:

.. literalinclude:: ../../examples/catalog-example-header.json
  :language: JSON

.. literalinclude:: ../../examples/catalog-example-payload.json
  :language: JSON

.. note::
  Per una gestione migliore e più efficiente della localizzazione delle informazioni contenute nel Catalogo delle Credenziali Digitali, un'Entità che lo consulta DOVREBBE:

  - Scaricare la versione base del Catalogo delle Credenziali Digitali (compatta, senza localizzazioni) utilizzando l'endpoint ``.well-known/credential-catalog``.
  - Determinare la lingua preferita dall'Utente.
  - Scaricare solo i bundle di localizzazione necessari.
  - Unire dinamicamente il contenuto localizzato con la Struttura del Catalogo degli Attestati Elettronici.

Di seguito è fornito un esempio non normativo dell'output di un bundle di localizzazione:

.. code-block:: json

  {
    "mDL.name": "Patente di Guida",
    "mDL.issuer1.name": "Esempio di Credential Issuer",
    "...": "..."
  }

I bundle di localizzazione DEVONO essere disponibili all'URI composto aggiungendo il codice locale e ``.json`` al valore ``localization.base_uri`` definito nel catalogo. Ciascun bundle locale DEVE essere accessibile seguendo il pattern di denominazione **{locale_code}.json**, dove **{locale_code}** è sostituito con il codice locale corrispondente dall'array **available_locales**.

Un esempio non normativo dell'URI di localizzazione italiana per il bundle sarebbe **https://trust-registry.eid-wallet.example.it/.well-known/l10n/credential-catalog/it.json**.

Decentralizzazione delle Informazioni di Visualizzazione e dei Claims
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La fonte canonica per le caratteristiche di visualizzazione e la struttura dei claim è determinata dai **Metadati dell'Emittente di Credenziali (Configurazione dell'Entità)**.

La logica complessiva per la presentazione di una Credenziale è:

1. Il Wallet/Relying Party recupera il **Catalogo delle Credenziali Digitali** leggero per scoprire la ``credential_type`` disponibile e l'``entity_id`` dei relativi Emittenti di Credenziali.
2. Recupera i **Metadati dell'Emittente di Credenziali** completi (Configurazione dell'Entità) dall'``entity_id`` rilevato.
3. I Metadati dell'Emittente di Credenziali DEVONO contenere le caratteristiche di visualizzazione complete (logo, colori) e le informazioni dettagliate sullo schema (tramite link ai Metadati di Tipo appropriati o direttamente nella configurazione). L'Emittente costruisce questi metadati sulla base dei suggerimenti forniti dalla Fonte Autentica (tramite il Registro FA) e delle specifiche di schema standard (tramite il Registro degli Schemi).

Tassonomia
----------

La **Tassonomia** fornisce il fondamento semantico per l'interoperabilità delle Credenziali Digitali mantenendo il vocabolario autorevole per l'organizzazione delle Credenziali all'interno dell'ecosistema IT-Wallet. La tassonomia è neutrale rispetto al formato della Credenziale.

La Tassonomia fornisce, in un'unica risorsa, il sistema di classificazione gerarchica che organizza Domini, Classi e Finalità applicabili alle Tipologie di Credenziale, supportando la valutazione delle politiche di autorizzazione e la standardizzazione a livello di ecosistema.

**Obiettivi della Tassonomia:**

1. **Fondamento Semantico**: Stabilire un vocabolario standardizzato per domini e finalità nell'intero ecosistema
2. **Framework per le Politiche**: Abilitare decisioni di autorizzazione strutturate basate sulla classificazione gerarchica
3. **Interoperabilità**: Garantire un'interpretazione coerente delle classificazioni delle credenziali
4. **Estensibilità**: Supportare l'evoluzione dell'ecosistema con nuovi Domini, Classi, Tipologie di Credenziale e Finalità
5. **Conformità Transfrontaliera**: Allineamento con i requisiti normativi EU e gli standard internazionali

**Struttura della Tassonomia:**

La tassonomia mantiene una struttura gerarchica a quattro livelli:

- **Domini**: Classificazione di primo livello che rappresenta ampie aree funzionali (es. IDENTITY, HEALTH, FINANCIAL, AUTHENTICATION)
- **Classe (Famiglia di Credenziali)**: Famiglia di Credenziali che condividono funzione, struttura o significato giuridico simili (es. Documenti di Identità, Certificati di Stato Civile, Albi Professionali, Accesso)
- **Tipologia di Credenziale**: Definizione specifica di Credenziale emessa da un'autorità (es. Credenziale di Viaggio Digitale, Certificato di Nascita, Patente di Guida Mobile).
- **Finalità (Intento di Verifica)**: Obiettivi di verifica che una Credenziale può soddisfare (es. Verifica dell'Identità, Verifica dell'Età, Idoneità a servizi specifici, Verifica del permesso di accesso).

.. note::
  La Tipologia di Credenziale è un concetto definito a livello del Catalogo delle Credenziali Digitali, non all'interno della Tassonomia. La Tassonomia fornisce il vocabolario di classificazione (Domini, Classi, Finalità) a cui le Tipologie di Credenziale nel Catalogo fanno riferimento.

**Supporto alla Localizzazione:**

La tassonomia supporta ambienti multilingue tramite il pattern con suffisso ``_l10n_id``, abilitando una gestione efficiente della localizzazione per le interfacce utente e le implementazioni transfrontaliere.

**Utilizzo della Tassonomia:**

- **Registro dei Claims**: Catalogo dei singoli claim
- **Registro FA**: Le Fonti Autentiche dichiarano le capacità utilizzando le classificazioni della tassonomia
- **Catalogo delle Credenziali Digitali**: Le Tipologie di Credenziale specificano Domini, Classi e Finalità
- **Politiche di Autorizzazione**: La valutazione delle politiche sfrutta la struttura della tassonomia per le decisioni di controllo degli accessi

La Tassonomia è accessibile attraverso l'endpoint dedicato alla tassonomia come definito nel meccanismo di discovery del registro ed è mantenuta dall'Organismo di Vigilanza per garantire la conformità normativa e la coerenza semantica.

**Struttura JSON della Tassonomia:**

.. list-table:: Campi di Primo Livello della Tassonomia
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Nome Campo**
     - **Descrizione**
   * - **id**
     - OBBLIGATORIO. Identificatore univoco della Tassonomia (es. ``urn:taxonomy:it-wallet``).
   * - **version**
     - OBBLIGATORIO. La versione della Tassonomia (es. ``1.0.0``).
   * - **last_modified**
     - OBBLIGATORIO. Il timestamp che indica quando la Tassonomia è stata aggiornata l'ultima volta (es. ``2026-03-11T00:00:00Z``).
   * - **name_l10n_id**
     - OBBLIGATORIO. Chiave di localizzazione che fa riferimento al nome leggibile della Tassonomia (es. ``taxonomy.name``).
   * - **description_l10n_id**
     - OBBLIGATORIO. Chiave di localizzazione che fa riferimento alla descrizione leggibile della Tassonomia (es. ``taxonomy.description``).
   * - **localization**
     - OBBLIGATORIO. Oggetto di configurazione della localizzazione contenente:

       * **default_locale**: Codice locale predefinito (es. ``it``).
       * **available_locales**: Array dei codici locale supportati (es. ``["en", "it"]``).
       * **base_uri**: URI base per il recupero del bundle di localizzazione (es. ``https://trust-registry.eid-wallet.example.it/.well-known/l10n/taxonomy/``).
       * **version**: Versione del formato del bundle di localizzazione.
   * - **domains**
     - OBBLIGATORIO. Array di oggetti Dominio, ciascuno contenente:

       * **id**: Identificatore univoco del Dominio in SCREAMING_SNAKE_CASE (es. ``IDENTITY``).
       * **name_l10n_id**: Chiave di localizzazione per il nome del dominio (es. ``domain.identity.name``).
       * **description_l10n_id**: Chiave di localizzazione per la descrizione del dominio (es. ``domain.identity.description``).
       * **classes**: Array di oggetti Classe. Ogni classe contiene ``id``, ``name_l10n_id`` e ``supported_purposes`` (array di stringhe di ID finalità).
   * - **purposes**
     - OBBLIGATORIO. Array piatto di tutti gli oggetti Finalità definiti nella tassonomia, ciascuno contenente:

       * **id**: Identificatore univoco della Finalità in SCREAMING_SNAKE_CASE (es. ``IDENTITY_VERIFICATION``, ``ACCESS_PERMIT``).
       * **name_l10n_id**: Chiave di localizzazione per il nome della finalità (es. ``purpose.identity_verification.name``).

Di seguito è fornito un esempio non normativo della struttura della Tassonomia:

.. literalinclude:: ../../examples/taxonomy-example.json
  :language: JSON

.. note::
  Per una gestione migliore e più efficiente della localizzazione della Tassonomia, un'Entità che la consulta DOVREBBE:

  - Scaricare la versione base della Tassonomia (compatta, senza localizzazioni) utilizzando l'endpoint ``.well-known/taxonomy``.
  - Determinare la lingua preferita dall'Utente.
  - Scaricare solo i bundle di localizzazione necessari.
  - Unire dinamicamente il contenuto localizzato con la struttura della Tassonomia.

Di seguito è fornito un esempio non normativo dell'output di un bundle di localizzazione:

.. code-block:: json

  {
    "taxonomy.name": "IT-Wallet Taxonomy",
    "taxonomy.description": "Hierarchical classification system for Digital Credentials in the IT-Wallet ecosystem",
    "domain.identity.name": "Identity",
    "domain.identity.description": "Credentials that establish or confirm a person's legal identity and personal, civil or legal status.",
    "class.identification_documents.name": "Identification Documents",
    "purpose.identity_verification.name": "Identity verification",
    "domain.authentication.name": "Authentication",
    "domain.authentication.description": "Credentials that attest authorisation to access restricted physical or digital spaces, services or resources.",
    "class.access.name": "Access",
    "purpose.access_permit.name": "Access permit verification",
    "...": "..."
  }

I bundle di localizzazione DEVONO essere disponibili all'URI composto aggiungendo il codice locale e ``.json`` al valore ``localization.base_uri`` definito nella tassonomia. Ciascun bundle locale DEVE essere accessibile seguendo il pattern di denominazione **{locale_code}.json**, dove **{locale_code}** è sostituito con il codice locale corrispondente dall'array **available_locales**.

Un esempio non normativo dell'URI di localizzazione italiana per il bundle sarebbe **https://trust-registry.eid-wallet.example.it/.well-known/l10n/taxonomy/it.json**.

Registro degli Schema
---------------------

Il **Registro degli Schemi** è l'inventario autorevole di tutti gli **Schemi di Credenziale** (JSON Schema per SD-JWT, CBOR Schema per mDOC) noti e accettati nell'ecosistema IT-Wallet. È gestito dal Trust Anchor e fornisce un'unica fonte verificabile per il recupero delle specifiche tecniche necessarie per il parsing, la validazione e la visualizzazione delle Credenziali Digitali.

**Obiettivi del Registro degli Schemi:**

1. **Centralizzazione degli Schemi**: Fornire un punto di accesso centralizzato per tutti gli schemi tecnici utilizzati dalle Credenziali Digitali.
2. **Integrità e Autenticità**: Garantire l'integrità e l'autenticità dei documenti di schema tramite digest crittografici.
3. **Interoperabilità**: Facilitare l'integrazione senza soluzione di continuità dei Fornitori di Wallet e delle Relying Party fornendo versioni di schema coerenti.
4. **Supporto al Ciclo di Vita della Credenziale**: Fungere da punto di riferimento verificabile per la validazione degli schemi durante l'emissione e la presentazione.

**Struttura e Accesso al Registro degli Schemi:**

Il Registro degli Schemi è accessibile tramite l'endpoint di discovery ``.well-known/it-wallet-registry`` nel campo `schema_registry`. Consente la discovery degli URI degli schemi e i relativi controlli di integrità crittografica.

.. list-table:: Campi di Primo Livello del Registro degli Schemi
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Nome Campo**
     - **Descrizione**
   * - **version**
     - OBBLIGATORIO. La versione del Registro degli Schemi (es. ``1.0.0``).
   * - **last_updated**
     - OBBLIGATORIO. Il timestamp che indica quando l'elenco è stato aggiornato l'ultima volta (es. ``2025-03-15T12:00:00Z``).
   * - **schemas**
     - OBBLIGATORIO. Un Array JSON in cui ogni voce è un Oggetto JSON che rappresenta una definizione di Schema di Credenziale. Ogni oggetto contiene i parametri definiti nella tabella "Parametri di Definizione dello Schema" di seguito, inclusi identificazione dello schema, specifiche del formato, URI e dati di verifica dell'integrità.

.. list-table:: Parametri di Definizione dello Schema
   :widths: 25 75
   :header-rows: 1

   * - **Nome Campo**
     - **Descrizione**
   * - **id**
     - OBBLIGATORIO. L'identificatore univoco dello schema (es. ``mDL+mso_mdoc+org.iso.18013.5.1.mDL``).
   * - **version**
     - OBBLIGATORIO. La versione della definizione dello schema (es. ``1.0.0``).
   * - **credential_type**
     - OBBLIGATORIO. L'identificatore univoco della tipologia di Credenziale Digitale (es. ``mDL``, ``pid``, ``eid``).
   * - **format**
     - OBBLIGATORIO. Il formato tecnico dello schema (es. ``mso_mdoc``, ``dc+sd-jwt``).
   * - **vct**
     - CONDIZIONALE. È OBBLIGATORIO se il ``format`` è ``dc+sd-jwt``, indicando il Tipo di Credenziale Verificabile (es. ``urn:eudi:mDL:it:1``).
   * - **docType**
     - CONDIZIONALE. È OBBLIGATORIO se il ``format`` è ``mso_mdoc``, indicando il tipo di documento utilizzato (es. ``org.iso.18013.5.1.mDL``).
   * - **schema_uri**
     - OBBLIGATORIO. L'URI dove è possibile recuperare il documento dello schema (es. ``https://trust-registry.it-wallet.example.it/.well-known/schemas/mdoc/mDL``).
   * - **schema_uri#integrity**
     - OBBLIGATORIO. Digest crittografico del documento di schema per la verifica dell'integrità. Formato: ``{digest_method}-{digest_value}`` (es. ``sha256-c8b708728e4c5756e35c03aeac257ca878d1f717d7b61f621be4d36dbd9b9c16``).
   * - **description**
     - OPZIONALE. Una descrizione leggibile dello schema, che può essere localizzata (es. "Schema tecnico per la mobile Driving License in formato mdoc.").

**Esempio di Registro degli Schemi:**

Un esempio non normativo del payload del Registro degli Schemi:

.. literalinclude:: ../../examples/schema-registry-example-payload.json
  :language: JSON

Registro delle WRP
------------------

Il **Registro delle WRP** è il registro delle entità del modello di trust **EUDIW**.
Ciascuno Stato membro lo istituisce e lo gestisce ai sensi del `CIR2025/848`_ (articolo 3), tramite il **Registrar**.
Il Registrar conserva i *record di registrazione* delle Wallet-Relying Party (identificazione, uso previsto, entitlements e materiale crittografico) che guidano l'emissione di WRPAC e WRPRC e supportano l'autorizzazione della Relying Party.

Il Registrar scrive un record quando una WRP completa la registrazione tecnica durante l'onboarding; ciascun record è firmato o sigillato elettronicamente per conto del Registrar, così che i provider dei certificati e il Wallet possano farvi affidamento.
Nel modello di trust duale questa registrazione **EUDIW** è additiva rispetto all'identità nazionale OID Federation dell'entità.

Il modello dati completo e le API pubbliche di lettura sono specificati nelle sezioni dedicate dell'infrastruttura di trust e non sono ripresi qui.

Cataloghi EUDIW
---------------

A livello UE la Commissione europea mantiene due cataloghi **EUDIW** che sono le controparti transfrontaliere dei registri semantici nazionali, definiti in ARF TS11 (`EUDI-TS 11`_) (Interfacce e formati per il Catalogue of Attributes e il Catalogue of Schemes).
Una tipologia di Credenziale presente in questi cataloghi è riconosciuta tra gli Stati membri ed è valutata nel Trust Framework **EUDIW**, mentre una Credenziale presente solo nei registri nazionali è valutata nel Trust Framework **Nazionale**.

Catalogue of Attributes
^^^^^^^^^^^^^^^^^^^^^^^

Il **Catalogue of Attributes** è il catalogo a livello UE delle definizioni standardizzate di attributi e dei namespace utilizzati nelle attestazioni.
Il :ref:`registry:Registro dei Claims` nazionale allinea i propri identificatori di claim a questo catalogo, affinché gli attributi definiti a livello nazionale restino interoperabili a livello transfrontaliero.

Catalogue of Schemes
^^^^^^^^^^^^^^^^^^^^

Il **Catalogue of Schemes** è il catalogo a livello UE degli schemi di attestazione (``SchemaMeta``): i metadati machine-readable che legano una tipologia di attestazione al relativo Rulebook e schema.
Il Registro degli Schemi nazionale si allinea a esso, e uno schema ivi referenziato ancora un'attestazione agli ancoraggi di trust EUDIW piuttosto che all'Attestation Rulebook nazionale.

Integrazione del Registro e Riferimenti Incrociati
--------------------------------------------------

I componenti del registro sono interconnessi e operano congiuntamente per supportare il completo ecosistema delle Credenziali:

1. **Registro FA** ↔ **Tassonomia**: Le entità FA dichiarano le capacità utilizzando le classificazioni della tassonomia per una categorizzazione standardizzata.
2. **Registro FA** ↔ **Catalogo**: Le tipologie di Credenziale fanno riferimento alle capacità FA per la validazione della fonte dati.
3. **Catalogo** ↔ **Tassonomia**: Le voci del Catalogo specificano domini e finalità della tassonomia per la discovery e l'autorizzazione.
4. **Registro della Federazione** ↔ **Tutti i Componenti**: Fornisce la validazione crittografica della fiducia per tutte le operazioni di registro e l'autenticazione delle entità.
5. **Registro degli Schemi** ↔ **Emittenti/RP**: Fornisce il collegamento verificabile a tutte le specifiche di formato delle Credenziali note nell'ecosistema.

Percorsi di Utilizzo dell'Infrastruttura del Registro
-----------------------------------------------------

I componenti dell'Infrastruttura del Registro sono progettati per supportare diverse fasi operative dell'ecosistema IT-Wallet, ciascuna con specifiche interazioni tra le entità.
I principali Percorsi di seguito illustrano le interazioni con l'Infrastruttura del Registro.

Navigazione del Catalogo
^^^^^^^^^^^^^^^^^^^^^^^^

Questo percorso di *Navigazione del Catalogo* supporta gli Utenti (sia utenti umani tramite un'**Istanza Wallet** che sistemi automatizzati come **Relying Party** o portali web) nella discovery e nella selezione delle Credenziali Digitali disponibili.

1.  **Accesso all'Endpoint di Discovery**: L'entità (es. un Fornitore di Wallet o un portale informativo) accede all'`Endpoint di Discovery del Registro` (``.well-known/it-wallet-registry``) per ottenere l'URI del **Catalogo delle Credenziali Digitali** e della **Tassonomia**.

2.  **Navigazione e Selezione**:

  * **Discovery delle Credenziali**: L'entità naviga l'elenco delle Credenziali (campo ``credentials``) per identificare le tipologie di Credenziale rilevanti (es. ``pid``, ``eid``, ``mDL``) e, se necessario, utilizza le informazioni sulla **Tassonomia** per navigare la gerarchia e fornire diverse localizzazioni.
  * **Metadati dell'Emittente**: L'entità estrae l'**Identificatore dell'Emittente** (`entity_id` nel campo `issuers`) associato alla Credenziale desiderata.
  * **Consultazione dei Dettagli**: Per ottenere informazioni complete e requisiti tecnici specifici, l'entità accede alla **Configurazione dell'Entità** (Metadati dell'Emittente) utilizzando l'identificatore recuperato.

3.  **Azione Finale**: L'entità può quindi utilizzare i metadati per mostrare le informazioni del catalogo a un Utente (o utilizzare le informazioni in altro modo).

Emissione di Credenziali
^^^^^^^^^^^^^^^^^^^^^^^^

Questo percorso definisce come un Emittente di Credenziali utilizza l'Infrastruttura del Registro per preparare ed emettere una Credenziale Digitale conforme.

1.  **Identificazione dei Requisiti**: L'EI consulta il **Catalogo delle Credenziali Digitali** per i requisiti tecnici della tipologia di Credenziale da emettere (es. ``max_validity_days``, ``min_loa``).

2.  **Risoluzione di Schemi e Claims**:

  * L'EI consulta il **Registro degli Schemi** per recuperare la specifica tecnica del formato e dello schema (es. JSON Schema per SD-JWT) richiesta dal Catalogo, verificandone la validità e l'integrità tramite l'hash (`schema_uri#integrity`).
  * L'EI accede al **Registro dei Claims** per recuperare le definizioni semantiche standardizzate e i formati dei dati (tipi di dati) degli attributi (claim) necessari.

3.  **Recupero dei Dati Autentici**:

  * L'EI consulta il **Registro delle Fonti Autentiche (FA)** per identificare la **Fonte Autentica** (FA) autorizzata per il dataset richiesto. Il Registro FA fornisce l'``entity_id`` della FA e i dettagli tecnici dell'interfaccia (`integration_endpoint`, `integration_method`).
  * L'EI consulta la specifica dell'endpoint FA per implementare l'integrazione necessaria al recupero dei dati dell'Utente per popolare la Credenziale Digitale.

4.  **Emissione della Credenziale**: L'EI utilizza i dati recuperati, gli schemi validati e i formati specificati per generare e firmare la Credenziale Digitale nel formato corretto (es. SD-JWT o mDOC).

Presentazione e Verifica delle Credenziali
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo percorso descrive come un'**Istanza Wallet** e una **Relying Party (RP)** interagiscono con l'Infrastruttura del Registro quando una Credenziale Digitale deve essere presentata da un Utente.

1.  **Autorizzazione e Selezione del Wallet**:

  * Il Wallet riceve una Richiesta di Presentazione dalla RP, verifica la validità della richiesta confrontando i *claim* richiesti con le *Politiche di Autorizzazione* relative alla RP.
  * Il Wallet consulta il **Catalogo delle Credenziali Digitali** e la **Tassonomia** per verificare i *Domini*, le *Classi* e le *Finalità* associate alle tipologie di Credenziale in suo possesso, valutando quali Credenziali sono adatte alla richiesta.
  * Il Wallet verifica se gli attributi richiesti (claim) sono disponibili e autorizzati alla divulgazione in base alla politica della richiesta (scenari **Credential-Specific** o **Credential-Agnostic**).
  * L'Utente autorizza il rilascio degli attributi selettivamente divulgati selezionati. Il Wallet quindi confeziona e presenta la Credenziale Digitale alla RP.

2.  **Discovery e Integrità**:

  * La RP riceve la Credenziale Digitale dall'Utente.
  * La RP consulta il **Registro della Federazione** tramite l'endpoint del Trust Anchor (`federation_resolve`, `federation_trust_mark_status`) per verificare la **fiducia crittografica** (Trust Mark) dell'Emittente e del Fornitore di Wallet come definito nella Sezione :ref:`trust-infrastructure:L'Infrastruttura di Trust`.
  * La RP consulta il **Registro degli Schemi** per scaricare lo schema della Credenziale presentata (`schema_uri`), verificandone l'integrità (`schema_uri#integrity`).

3.  **Validazione dello Schema e della Politica Finale**:

  * La RP utilizza lo schema recuperato per validare la struttura della Credenziale e i tipi di dati degli attributi rivelati.
  * La RP esegue la verifica finale per assicurarsi che gli attributi presentati siano conformi ai requisiti specifici della richiesta iniziale e alla politica di autorizzazione.

4.  **Accettazione o Rifiuto**: Sulla base della validazione crittografica, della conformità allo schema e dell'autorizzazione basata su politiche, la RP accetta o rifiuta la Credenziale per l'accesso al servizio.


