.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst

L'Infrastruttura di Trust
=========================

L'ecosistema IT-Wallet opera all'interno di un'infrastruttura di trust federata dove le entità partecipanti stabiliscono relazioni di trust crittografiche e mantengono la conformità con standard di sicurezza comuni. Questa infrastruttura fornisce le fondamenta per operazioni sicure di Credenziali Elettroniche tra i partecipanti dell'ecosistema.

Questa sezione definisce l'implementazione del Trust Model in un'infrastruttura che è conforme a OpenID Federation 1.0 `OID-FED`_. Tale infrastruttura nazionale prevede un'API RESTful per la distribuzione di metadati, policy dei metadati, trust mark, chiavi pubbliche crittografiche e certificati X.509, e lo stato di revoca dei partecipanti, chiamati anche Entità di Federazione.

Questa infrastruttura di trust lavora in coordinamento con l'Infrastruttura del Registro (vedi :ref:`registry:Infrastruttura del Registro`) per abilitare i processi di onboarding delle entità dettagliati in :ref:`entity-onboarding:Onboarding delle Entità`. In particolare, abilita l'implementazione tecnica dei processi di onboarding descritti in :ref:`entity-onboarding:Onboarding delle Entità` e supporta gli scenari operativi illustrati in :ref:`onboarding-high-level:Onboarding Journey Maps`.

**Abilitazione dell'Onboarding**: L'Infrastruttura di Trust fornisce i meccanismi crittografici che consentono alle nuove entità (Credential Issuer, Relying Party, Fornitori di Wallet) di stabilire relazioni di trust verificabili durante il loro processo di registrazione. Senza questa infrastruttura, le entità non sarebbero in grado di dimostrare il loro stato di conformità o le capacità operative agli altri partecipanti dell'ecosistema.

**Supporto al Ciclo di Vita delle Entità**: Durante tutto il ciclo di vita operativo di un'entità, l'Infrastruttura di Trust mantiene attestazioni di trust aggiornate, gestisce la rotazione delle chiavi, gestisce scenari di revoca e supporta il monitoraggio della conformità. Questo supporta direttamente le procedure di gestione del ciclo di vita dettagliate in :ref:`entity-onboarding:Onboarding delle Entità`.

**Integrazione con l'Infrastruttura del Registro**: L'Infrastruttura di Trust implementa il componente Federation Registry dell'Infrastruttura del Registro più ampia, fornendo le fondamenta tecniche per la scoperta delle entità e la validazione del trust che sottende tutte le procedure di onboarding.


.. plantuml:: plantuml/trust-roles.puml
   :width: 99%
   :alt: La figura illustra i ruoli di trust.
   :caption: `I ruoli all'interno della Federazione, dove il National Trust Anchor supervisiona i suoi subordinati, che includono uno o più Intermediari e Foglie. <https://www.plantuml.com/plantuml/png/XT1HQy90303Wz_iLcNkMiIAoXo5AtK3OWup17aViPUxmcYkvd29Z_tsjThM2kBSc-P9UCesAegdqviPnuPCbUCn7T_de8m-iw9XaOapSEAvGi8GL5fkrXCGs3pu8g237kaIiFJKJ2RiZMFcwmnYXGf7Ndc3m9YagpBZu2Z80ZA08j_FnqyDpTkOMh2GbMOTA1-TOxplv3ymkZdmXt58y64_u6UjnZPcFhw6iGzTKTwu_3Ty6eDUG2rbYTUXX4MEYu-w5wnvwfj_HUr9OIjWwszfTTTc-ajyxNiCIHVS7AIVvOqpzZs6gXXDGDBkg_MwEQQGNPQOzIQ_UxjypJVeqhKcTeYcnJQN_1G00>`_

In questa rappresentazione, sia il :term:`National Trust Anchor` che gli Intermediari assumono il ruolo di Registration Authority.

Ruoli di Federazione
--------------------

Tutti i partecipanti sono Entità di Federazione che DEVONO essere registrate da un Registration Body, eccetto le Istanze del Wallet che sono dispositivi personali dell'Utente finale autenticati dal loro Fornitore di Wallet.

.. note::
  L'Istanza del Wallet, come dispositivo personale, è considerata affidabile attraverso un'attestazione verificabile rilasciata e firmata da una terza parte fidata.

  Questo è chiamato *Wallet Instance Attestation* ed è documentato nella sezione dedicata :ref:`wallet-instance-attestation-issuance:Emissione della Wallet Instance Attestation`.

**Ruolo nell'Onboarding**: Durante la registrazione dell'entità, il Trust Anchor e gli Intermediate agiscono come Autorità di Federazione. Ciò stabilisce la posizione del partecipante nella gerarchia di fiducia e gli consente di partecipare alle operazioni di credenziali. Le foglie (Emittenti di credenziali, Relying Party, Wallet Provider) si sottopongono a registrazione per dimostrare la propria idoneità e ricevere l'autorizzazione a svolgere le funzioni loro assegnate.

**Ruolo nelle Operazioni**: Durante l'emissione e la presentazione delle Credenziali, questi ruoli abilitano la validazione del trust distribuita senza richiedere la verifica centralizzata per ogni transazione. Le Foglie utilizzano il loro stato registrato per emettere Credenziali, verificare presentazioni o fornire servizi di Wallet agli utenti finali.

Di seguito la tabella con il riepilogo dei ruoli delle Entità di Federazione, mappati sui corrispondenti ruoli EUDI Wallet.

.. list-table::
   :class: longtable
   :widths: 20 20 60
   :header-rows: 1

   * - Ruolo EUDI
     - Ruolo di Federazione
     - Note
   * - Public Key Infrastructure (PKI)
     - :term:`National Trust Anchor`
     - La Federazione ha capacità PKI e utilizza OpenID Federation 1.0 `OID-FED`_. L'Entità che configura l'intera infrastruttura a livello nazionale è il :term:`National Trust Anchor`.
   * - Qualified Trust Service Provider (QTSP)
     - Leaf
     -
   * - Fornitore di Attestati Elettronici di Dati di Identificazione Personale
     - Leaf
     -
   * - Fornitore di Attestati Elettronici di Attributi Qualificati
     - Leaf
     -
   * - Fornitore di Attestati Elettronici di Attributi
     - Leaf
     -
   * - Relying Party
     - Leaf
     -
   * - Trust Service Provider (TSP)
     - Leaf
     -
   * - Fornitore di Wallet
     - Leaf
     -

Integrazione dell'Infrastruttura di Trust e del Registro
--------------------------------------------------------

L'Infrastruttura di Trust implementa il componente Federation Registry dell'Infrastruttura del Registro. Il Federation Registry mantiene l'elenco autorevole delle entità fidate attraverso gli endpoint di federazione definiti in questa sezione, inclusi l'elenco delle entità (/list), le dichiarazioni dei subordinati (/fetch), la validazione dei trust mark (/trust_mark_status), gli eventi sui subordinati (/federation_subordinate_events_endpoint) e la gestione delle chiavi storiche (/historical-jwks).

Questo Federation Registry opera insieme ad altri componenti del registro (Claims Registry, AS Registry, Catalogo degli Attestati Elettronici, Taxonomy) per fornire supporto completo all'ecosistema. Per l'architettura completa del registro e le interazioni dei componenti, vedi :ref:`registry:Infrastruttura del Registro`.

Proprietà Generali
------------------

L'architettura dell'infrastruttura di trust è fondata sui seguenti principi fondamentali:

.. list-table::
   :class: longtable
   :widths: 20 20 80
   :header-rows: 1

   * - Identificatore
     - Proprietà
     - Descrizione
   * - P1
     - **Sicurezza**
     - Incorpora meccanismi per garantire l'integrità, la riservatezza e l'autenticità delle Relazioni di Trust e delle interazioni all'interno della federazione.
   * - P2
     - **Privacy**
     - Progettata per rispettare e proteggere la privacy delle entità coinvolte; la divulgazione minima è parte integrante di questo principio.
   * - P3
     - **Interoperabilità**
     - Supporta l'interazione fluida e la creazione di trust tra sistemi ed entità diverse all'interno della federazione.
   * - P4
     - **Trust Transitivo**
     - Trust stabilita indirettamente attraverso una catena di relazioni fidate, che consente alle entità di fidarsi reciprocamente sulla base di autorità comuni e intermediari fidati.
   * - P5
     - **Delega**
     - Capacità o funzionalità tecnica di delegare autorità o responsabilità ad altre entità, consentendo un meccanismo di trust distribuito.
   * - P6
     - **Scalabilità**
     - Progettata per gestire in modo efficiente un numero crescente di entità o interazioni senza un aumento significativo della complessità di gestione del trust.
   * - P7
     - **Flessibilità**
     - Adattabile a varie esigenze operative e organizzative, consentendo alle entità di definire e adeguare le proprie Relazioni di Trust e policy.
   * - P8
     - **Autonomia**
     - Pur facendo parte di un ecosistema federato, ciascuna entità mantiene il controllo sulle proprie definizioni e configurazioni.
   * - P9
     - **Decentralizzazione**
     - A differenza dei sistemi centralizzati tradizionali, l'infrastruttura di trust consente un approccio decentralizzato.

Requisiti dell'Infrastruttura di Trust
--------------------------------------

Questa sezione include i requisiti necessari per la corretta implementazione e il funzionamento dell'infrastruttura di trust.

.. list-table:: Requisiti Funzionali
   :class: longtable
   :widths: 20 80
   :header-rows: 1

   * - ID
     - Descrizione
   * - FR1
     - **Creazione di Trust nella Federazione**: il sistema deve essere in grado di stabilire trust tra diverse entità (Credential Issuer, Relying Party, ecc.) all'interno di una federazione, utilizzando firme crittografiche per lo scambio sicuro di informazioni sui partecipanti all'ecosistema.
   * - FR2
     - **Autenticazione delle Entità**: il sistema deve implementare meccanismi per autenticare le entità all'interno della federazione, garantendone la conformità alle regole condivise.
   * - FR3
     - **Validazione delle Firme**: il sistema deve supportare la creazione, verifica e validazione di firme elettroniche e fornire meccanismi standard e sicuri per ottenere le chiavi pubbliche crittografiche necessarie per la validazione delle firme.
   * - FR4
     - **Marcatura Temporale**: gli artefatti firmati devono contenere marcature temporali per garantire l'integrità e il non-ripudio delle transazioni nel tempo, grazie alle interfacce, ai servizi, al modello di archiviazione e agli approcci definiti all'interno della federazione.
   * - FR5
     - **Validazione dei Certificati**: il sistema richiede trasmissioni riservate, protette tramite TLS su HTTP, e la validazione dei certificati per l'autenticazione dei siti web.
   * - FR6
     - **Interoperabilità e Conformità agli Standard**: garantire l'interoperabilità tra i membri della federazione aderendo agli standard tecnici, facilitando le transazioni elettroniche transfrontaliere.
   * - FR7
     - **Protezione dei Dati e Privacy**: implementare misure di protezione dei dati in conformità con il GDPR, garantendo la privacy e la sicurezza dei dati personali trattati all'interno della federazione.
   * - FR8
     - **Risoluzione delle Controversie e Responsabilità**: stabilire procedure chiare per la risoluzione delle controversie e definire le responsabilità tra i membri della federazione.
   * - FR9
     - **Servizi di Emergenza e Revoca**: implementare meccanismi per la revoca immediata dei partecipanti in caso di violazioni della sicurezza o altre emergenze.
   * - FR10
     - **Infrastruttura di Trust Scalabile**: il sistema deve supportare meccanismi scalabili per la creazione di trust, sfruttando approcci e soluzioni tecniche che complementino gli approcci di delega transitiva per gestire in modo efficiente le Relazioni di Trust man mano che la federazione cresce, eliminando i registri centrali che potrebbero presentare fallimenti tecnici o amministrativi.
   * - FR11
     - **Scalabilità Efficiente dello Storage**: implementare una soluzione di archiviazione che scala orizzontalmente per accogliere volumi di dati crescenti, minimizzando i costi di archiviazione centrale e amministrativi. Il sistema dovrebbe consentire ai membri di archiviare e presentare in modo indipendente attestazioni di trust storiche e artefatti firmati durante le risoluzioni delle controversie, mentre l'infrastruttura della federazione mantiene solo un registro delle chiavi storiche per validare i dati storici, archiviati e forniti dai partecipanti.
   * - FR12
     - **Attestazione Verificabile (Trust Mark)**: incorporare un meccanismo per l'emissione e la verifica di attestazioni verificabili che fungono da prova di conformità a profili o standard specifici. Ciò consente alle entità all'interno della federazione di dimostrare l'aderenza agli standard di sicurezza, privacy e operativi concordati.
   * - FR13
     - **Meccanismo Decentralizzato per la Risoluzione delle Controversie**: progettare un meccanismo decentralizzato per la risoluzione delle controversie che consenta ai membri della federazione di verificare in modo indipendente la creazione di trust storica e gli artefatti firmati, riducendo la dipendenza dalle autorità centrali e semplificando il processo di risoluzione.
   * - FR14
     - **Interoperabilità tra Federazioni**: garantire che il sistema sia in grado di interoperare con altre federazioni o Trust Framework, facilitando transazioni e creazione di trust tra federazioni senza compromettere la sicurezza o la conformità.
   * - FR15
     - **Organismi di Registrazione Autonomi**: il sistema deve facilitare l'integrazione di organismi di registrazione autonomi che operano in conformità con le regole della federazione. Questi organismi hanno il compito di valutare e registrare le entità all'interno della federazione, secondo le regole prestabilite e la loro conformità che deve essere periodicamente attestata.
   * - FR16
     - **Audit Periodico degli Organismi di Registrazione e delle Entità**: implementare meccanismi per l'audit periodico e il monitoraggio dello stato di conformità sia degli organismi di registrazione che delle loro entità registrate.
   * - FR17
     - **Attestazione di Conformità per i Dispositivi Personali**: organismi fidati, in forma di entità di federazione, dovrebbero emettere attestazioni di conformità e fornire prove firmate di tale conformità per l'hardware dei dispositivi personali utilizzati all'interno della federazione. Queste attestazioni dovrebbero essere attestate e periodicamente rinnovate per garantire che i dispositivi soddisfino gli attuali standard di sicurezza.
   * - FR18
     - **Monitoraggio Automatizzato della Conformità**: il sistema dovrebbe includere strumenti automatizzati per il monitoraggio della conformità delle entità agli standard della federazione. Questa automazione aiuta nel rilevamento precoce di potenziali problemi di conformità.
   * - FR19
     - **Binding Sicuro delle Capacità del Protocollo**: il protocollo sicuro deve consentire lo scambio di dati sulle capacità specifiche del protocollo come metadati crittograficamente vincolati allegati a un'identità specifica. Questi metadati dovrebbero definire le capacità tecniche associate all'identità, garantendo prova verificabile e associazione antimanomissione per una robusta creazione di trust e controllo degli accessi.

Endpoint API di Federazione
---------------------------

OpenID Federation 1.0 utilizza Servizi Web RESTful protetti su HTTPs. OpenID Federation 1.0 definisce quali sono gli endpoint web che i partecipanti DEVONO rendere pubblicamente disponibili. La tabella sottostante riassume gli endpoint e i loro ambiti.

Tutti gli endpoint elencati di seguito sono definiti nelle specifiche `OID-FED`_.

.. list-table::
   :class: longtable
   :widths: 20 20 20 20
   :header-rows: 1

   * - nome endpoint
     - richiesta http
     - ambito
     - richiesto per
   * - federation metadata
     - **GET** .well-known/openid-federation
     - Metadati che un'Entità pubblica su se stessa, verificabili con una terza parte fidata (Entità Superiore). È chiamata Entity Configuration.
     - Trust Anchor, Intermediario, Fornitore di Wallet, Relying Party, Credential Issuer
   * - subordinate list endpoint
     - **GET** /list
     - Elenca i Subordinati. Vedi `OID-FED`_ Sezione 8.2
     - Trust Anchor, Intermediario
   * - fetch endpoint
     - **GET** /federation_fetch_endpoint?sub=https://rp.example.org
     - Restituisce un JWT firmato su un soggetto specifico, il suo Subordinato. È chiamato Subordinate Statement. Vedi `OID-FED`_ Sezione 8.1
     - Trust Anchor, Intermediario
   * - trust mark status
     - **POST** /trust_mark_status
     - Restituisce lo stato dell'emissione (validità) di un Trust Mark relativo a un soggetto specifico. Vedi `OID-FED`_ Sezione 8.4
     - Trust Anchor, Intermediario
   * - trust mark  list
     - **GET** /trust_mark_listing?trust_mark_type=...
     - Elenca tutte le entità per le quali sono stati emessi Trust Mark e sono ancora validi. Vedi `OID-FED`_ Sezione 8.5
     - Trust Anchor, Intermediario
   * - trust mark
     - **GET** /trust_mark?trust_mark_type=...
     - Restituisce il Trust Mark relativo a un soggetto specifico. Vedi `OID-FED`_ Sezione 8.6
     - Trust Anchor, Intermediate
   * - historical keys
     - **GET** /federation_historical_keys
     - Elenca le chiavi scadute e revocate, con la motivazione della revoca. Vedi `OID-FED`_ Sezione 8.7
     - Trust Anchor, Intermediario
   * - subordinate events
     - **GET** /federation_subordinate_events_endpoint?sub=https://rp.example.org
     - Restituisce una traccia storica degli eventi di registrazione sui Subordinati Immediati, come registrazione, revoca e aggiornamenti delle loro Chiavi dell'Entità di Federazione. Vedi la sezione :ref:`trust-infrastructure:Federation Subordinate Events Endpoint` per maggiori dettagli.
     - Trust Anchor, Intermediario

Tutte le risposte degli endpoint di federazione sono sotto forma di JWT firmato, ad eccezione dell'endpoint di Elenco Subordinati e dell'endpoint di Stato Trust Mark che sono serviti come JSON semplice per impostazione predefinita. L'Endpoint Eventi Subordinati della Federazione restituisce anche JWT firmati con il tipo di contenuto ``application/entity-events-statement+jwt``.

Configurazione della Federazione
--------------------------------

La configurazione della federazione è pubblicata dal Trust Anchor all'interno della sua Entity Configuration, è disponibile nel path web well-known corrispondente a **.well-known/openid-federation**.

Tutti i partecipanti nella federazione DEVONO ottenere la configurazione di federazione prima di entrare nella fase operativa, e DEVONO mantenerla aggiornata. La configurazione di federazione è l'Entity Configuration del Trust Anchor, contiene le chiavi pubbliche per le operazioni di firma.

Di seguito è riportato un esempio non normativo di un'Entity Configuration del Trust Anchor, dove ogni parametro è documentato nella specifica `OpenID Federation <OID-FED>`_:

.. code-block:: json

    {
        "alg": "ES256",
        "kid": "FifYx03bnosD8m6gYQIfNHNP9cM_Sam9Tc5nLloIIrc",
        "typ": "entity-statement+jwt"
    }

.. code-block:: json

      {
        "exp": 1649375259,
        "iat": 1649373279,
        "iss": "https://trust-anchor.eid-wallet.example.it",
        "sub": "https://trust-anchor.eid-wallet.example.it",
        "jwks": {
            "keys": [
                {

                    "kty": "EC",
                    "kid": "X2ZOMHNGSDc4ZlBrcXhMT3MzRmRZOG9Jd3o2QjZDam51cUhhUFRuOWd0WQ",
                    "crv": "P-256",
                    "x": "1kNR9Ar3MzMokYTY8BRvRIue85NIXrYX4XD3K4JW7vI",
                    "y": "slT14644zbYXYF-xmw7aPdlbMuw3T1URwI4nafMtKrY",
                    "x5c": [
                      // <self-issued X.509 certificate about the Trust Anchor>
                      ]
                }
            ]
        },
        "metadata": {
            "federation_entity": {
                "organization_name": "example TA",
                "contacts":[
                    "tech@eid.trust-anchor.example.eu"
                ],
                "homepage_uri": "https://trust-anchor.eid-wallet.example.it",
                "logo_uri":"https://trust-anchor.eid-wallet.example.it/static/svg/logo.svg",
                "federation_fetch_endpoint": "https://trust-anchor.eid-wallet.example.it/fetch",
                "federation_resolve_endpoint": "https://trust-anchor.eid-wallet.example.it/resolve",
                "federation_list_endpoint": "https://trust-anchor.eid-wallet.example.it/list",
                "federation_trust_mark_status_endpoint": "https://trust-anchor.eid-wallet.example.it/trust_mark_status",
                "federation_trust_mark_list_endpoint": "https://trust-anchor.eid-wallet.example.it/trust_mark_listing",
                "federation_subordinate_events_endpoint": "https://trust-anchor.eid-wallet.example.it/events"
            }
        },
        "trust_mark_issuers": {
            "https://trust-anchor.eid-wallet.example.it/openid_relying_party/public": [
                "https://trust-anchor.eid-wallet.example.it",
                "https://public.intermediary.other.org"
            ],
            "https://trust-anchor.eid-wallet.example.it/openid_relying_party/private": [
                "https://private.other.intermediary.org"
            ]
        }
    }


Entity Configuration
--------------------

L'Entity Configuration è il documento verificabile che ogni Entità di Federazione DEVE pubblicare per proprio conto, nell'endpoint **.well-known/openid-federation**.

La Risposta HTTP dell'Entity Configuration DEVE impostare il tipo di media su `application/entity-statement+jwt`.

L'Entity Configuration DEVE essere firmata crittograficamente. La parte pubblica di questa chiave DEVE essere fornita nell'Entity Configuration e all'interno del Subordinate Statement emesso da un superiore immediato e relativo alla sua Entità di Federazione subordinata.

L'Entity Configuration PUÒ anche contenere uno o più Trust Mark.

**Ruolo nell'Onboarding**: Le nuove entità pubblicano la loro Entity Configuration come parte del loro processo di registrazione, dichiarando le loro capacità, protocolli supportati e stato di conformità alla federazione. La configurazione serve come dichiarazione iniziale dell'entità della sua prontezza tecnica e ambito operativo, consentendo ad altri partecipanti di scoprire e validare il suo stato di registrazione.

**Ruolo nelle Operazioni**: Durante le operazioni di credenziali, le Entity Configuration sono recuperate da wallet, credential issuer e relying party per verificare lo stato operativo corrente, le capacità supportate e le attestazioni di conformità di altre entità. Questo abilita la scoperta dinamica degli endpoint di servizio, delle chiavi crittografiche e delle versioni di protocollo richieste per lo scambio sicuro di credenziali.

I dettagli tecnici sull'Entity Configuration del Fornitore di Wallet, Credential Issuer e Relying Party sono forniti rispettivamente nelle Sezioni :ref:`wallet-provider-entity-configuration:Entity Configuration del Fornitore di Wallet`, :ref:`credential-issuer-entity-configuration:Entity Configuration del Fornitore di Attestati Elettronici` e :ref:`relying-party-entity-configuration:Entity Configuration di una Relying Party`.

.. note::
  **Firma dell'Entity Configuration**

  Tutte le operazioni di controllo della firma riguardanti le Entity Configuration, i Subordinate Statement e i Trust Mark, sono eseguite con le chiavi pubbliche di Federazione. Per gli algoritmi supportati fare riferimento alla Sezione `Algoritmo Crittografico`.

Parametri Comuni delle Entity Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Entity Configuration di tutti i partecipanti nella federazione DEVONO avere in comune i parametri elencati di seguito.


.. list-table::
   :class: longtable
   :widths: 20 60
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
   * - **iss**
     - String. Identificatore dell'Entità emittente.
   * - **sub**
     - String. Identificatore dell'Entità a cui si riferisce. DEVE essere uguale a ``iss``.
   * - **iat**
     - UNIX Timestamp con il tempo di generazione del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
   * - **exp**
     - UNIX Timestamp con il tempo di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
   * - **jwks**
     - Un JSON Web Key Set (JWKS) :rfc:`7517` che rappresenta la parte pubblica delle chiavi di firma dell'Entità in questione. Ogni JWK nel set JWK DEVE avere un ID chiave (claim kid) e PUÒ avere un parametro `x5c`, come definito in :rfc:`7517`. Contiene le Chiavi dell'Entità di Federazione richieste per le operazioni di Trust Evaluation.

       **x5c**: Il parametro `x5c` incluso nel parametro `jwks` dell'Entity Configuration DEVE contenere solo il Certificato X.509 auto-emesso relativo al corrispondente `jwk`.
   * - **metadata**
     - Oggetto JSON. Ogni chiave dell'Oggetto JSON rappresenta un identificatore di tipo di metadati contenente un Oggetto JSON che rappresenta i metadati, secondo lo schema di metadati di quel tipo. Un'Entity Configuration PUÒ contenere più dichiarazioni di metadati, ma solo una per ogni tipo di metadati (<**entity_type**>). i tipi di metadati sono definiti nella sezione `Tipi di Metadati <Metadata Types>`_.


Entity Configuration Trust Anchor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'Entity Configuration del Trust Anchor, oltre ai parametri comuni elencati sopra, utilizza i seguenti parametri:

.. list-table::
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Richiesto**
   * - **trust_mark_issuers**
     - Array JSON che definisce quali autorità di Federazione sono considerate affidabili per l'emissione di Trust Mark specifici, assegnati con i loro identificatori unici.
     - |check-icon|


Trust Mark degli Intermediari di Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nell'ecosistema IT-Wallet, gli Intermediari di Relying Party che agiscono per conto dei Relying Party (ai sensi dell'Art. 5b(8) del Regolamento eIDAS2 `EU_2024_1183`_) sono soggetti a uno specifico regime di Trust Mark che consente al Wallet di riconoscere e mostrare all'Utente che il RP richiedente opera tramite un Intermediario di Relying Party.

**Emissione del Trust Mark all'Intermediario di Relying Party**

Il Trust Anchor DEVE includere gli Intermediari di Relying Party nell'attributo ``trust_mark_issuers`` della propria Entity Configuration, autorizzandoli ad emettere Trust Mark per le Foglie a loro afferenti. Il Trust Anchor emette all'Intermediario di Relying Party un Trust Mark che attesta il suo ruolo, utilizzando ``https://<federation_authority_domain>/trust_marks/federation-entity/openid_credential_verifier_intermediary`` come ``trust_mark_type`` per distinguerlo dalle altre entità presenti nell'ecosistema.

L'Intermediario di Relying Party DEVE includere questo Trust Mark nella propria Entity Configuration come prova del suo ruolo riconosciuto all'interno della Federazione.

**Emissione di Trust Mark alle Foglie afferenti all'Intermediario di Relying Party**

I Trust Mark emessi alle Foglie (Relying Party) afferenti a un Intermediario di Relying Party DEVONO essere emessi dall'Intermediario di Relying Party stesso, e non direttamente dal Trust Anchor.

Un Relying Party afferente a un Intermediario di Relying Party DEVE includere nella propria Entity Configuration:

- Il Trust Mark emesso dall'Intermediario di Relying Party, come prova del completamento del processo di onboarding gestito dall'Intermediario di Relying Party;
- Il proprio ``authority_hints`` contenente l'URL dell'Intermediario di Relying Party (non direttamente del Trust Anchor), indicando così la corretta catena gerarchica.

Di seguito è riportato un esempio non normativo di Entity Configuration del Trust Anchor che mostra la configurazione aggiornata di ``trust_mark_issuers`` con gli Intermediari di Relying Party autorizzati:

.. code-block:: json

    {
      "trust_mark_issuers": {
        "https://trust-anchor.eid-wallet.example.it/trust_marks/federation-entity/openid_credential_verifier": [
          "https://trust-anchor.eid-wallet.example.it",
          "https://intermediary.example.org"
        ],
        "https://trust-anchor.eid-wallet.example.it/trust_marks/federation-entity/openid_credential_verifier_intermediary": [
          "https://trust-anchor.eid-wallet.example.it"
        ],
        "https://trust-anchor.eid-wallet.example.it/trust_marks/federation-entity/openid_credential_issuer": [
          "https://trust-anchor.eid-wallet.example.it"
        ],
        "https://trust-anchor.eid-wallet.example.it/trust_marks/federation-entity/wallet_solution": [
          "https://trust-anchor.eid-wallet.example.it"
        ]
      }
    }

.. note::
  Il Trust Mark con identificativo che termina con ``federation-entity/openid_credential_verifier_intermediary`` è emesso esclusivamente dal Trust Anchor ed è quello che il Wallet utilizza per verificare che un'entità sia un Intermediario di Relying Party riconosciuto. I Trust Mark ``https://<federation_authority_domain>/trust_marks/federation-entity/openid_credential_verifier`` DOVREBBERO invece essere emessi anche dagli Intermediari di Relying Party per le Foglie a loro afferenti.


Entity Configuration Foglie e Intermediari
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Oltre ai claim precedentemente definiti, l'Entity Configuration delle Foglie e delle Entità Intermedie utilizza i seguenti parametri:


.. list-table::
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Richiesto**
   * - **authority_hints**
     - Array di URL (String). Contiene un elenco di URL delle entità superiori immediate, come il Trust Anchor o un Intermediario, che emette un Subordinate Statement relativo a questo soggetto.
     - |check-icon|
   * - **trust_marks**
     - Un Array JSON contenente i Trust Mark.
     - |check-icon|


Tipi di Metadati
^^^^^^^^^^^^^^^^

In questa sezione sono definiti i principali tipi di metadati mappati sui ruoli dell'ecosistema, fornendo i riferimenti del protocollo di metadati per ognuno di questi.


.. note::
  Le voci che non hanno alcun riferimento a una bozza o standard noto sono intese per essere definite in questo riferimento tecnico.

.. list-table::
   :class: longtable
   :widths: 20 20 20 60
   :header-rows: 1

   * - Entità OpenID
     - Entità EUDI
     - Tipo di Metadati
     - Riferimenti
   * - Trust Anchor
     - Trust Anchor
     - ``federation_entity``
     - `OID-FED`_
   * - Intermediario
     - Intermediario
     - ``federation_entity``
     - `OID-FED`_
   * - Fornitore di Wallet
     - Fornitore di Wallet
     - ``federation_entity``, ``wallet_solution``
     - --
   * - Authorization Server
     -
     - ``federation_entity``, ``oauth_authorization_server``
     - `OPENID4VCI`_
   * - Credential Issuer
     - Fornitore PID, Fornitore (Q)EAA
     - ``federation_entity``, ``openid_credential_issuer``, [``oauth_authorization_server``]
     - `OPENID4VCI`_
   * - Relying Party
     - Relying Party
     - ``federation_entity``, ``openid_credential_verifier``
     - `OID-FED`_, `OpenID4VP`_


.. note::
  I metadati del Fornitore di Wallet sono definiti nella sezione sottostante.

  :ref:`wallet-solution:Soluzione Wallet`.


.. note::
  Nei casi in cui un Fornitore PID/EAA implementa sia il Credential Issuer che l'Authorization Server, DEVE incorporare sia ``oauth_authorization_server`` che ``openid_credential_issuer`` all'interno dei suoi tipi di metadati.
  Altre implementazioni possono dividere il Credential Issuer dall'Authorization Server, quando questo accade i metadati del Credential Issuer DEVONO contenere i parametri `authorization_servers`, incluso l'identificatore unico dell'Authorization Server.
  Inoltre, se dovesse esserci la necessità di Autenticazione dell'Utente da parte del Credential Issuer, potrebbe essere necessario includere il tipo di metadati pertinente, sia ``openid_relying_party`` che ``openid_credential_verifier``.


Metadati di federation_entity Foglie
------------------------------------

I metadati *federation_entity* per le Foglie contiene i seguenti claim.


.. list-table::
  :class: longtable
  :widths: 20 60
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
  * - **organization_name**
    - OBBLIGATORIO. Vedi `OID-FED`_ Sezione 5.2.2
  * - **homepage_uri**
    - OBBLIGATORIO. OBBLIGATORIO se ``organization_uri`` è assente.
  * - **organization_uri**
    - CONDIZIONALE. OBBLIGATORIO se ``homepage_uri`` è assente. Vedi `OID-FED`_ Sezione 5.2.2
  * - **policy_uri**
    - OBBLIGATORIO. Vedi `OID-FED`_ Sezione 5.2.2
  * - **logo_uri**
    - OBBLIGATORIO. URL del logo dell'entità; DEVE essere in formato SVG. Vedi `OID-FED`_ Sezione 5.2.2
  * - **contacts**
    - OBBLIGATORIO. Indirizzo email verificato istituzionale (PEC) dell'entità. Vedi `OID-FED`_ Sezione 5.2.2
  * - **federation_resolve_endpoint**
    - OPZIONALE. Vedi `OID-FED`_ Sezione 8.3
  * - **tos_uri**
    - OPZIONALE. Stringa URL che punta a un documento di termini di servizio leggibile dall'uomo per il client che descrive una relazione contrattuale tra l'utente finale e il client che l'utente finale accetta quando autorizza il client. Vedi `OID-FED`_.


I Subordinate Statement
-----------------------

I Trust Anchor e gli Intermediari pubblicano Subordinate Statement relativi ai loro Subordinati immediati.
Il Subordinate Statement PUÒ contenere una policy di metadati e i Trust Mark relativi a un Subordinato.

La policy di metadati, quando applicata, apporta una o più modifiche ai metadati finali della Foglia. I metadati finali di una Foglia sono derivati dalla Trust Chain che contiene tutte le dichiarazioni, a partire dall'Entity Configuration fino al Subordinate Statement emesso dal Trust Anchor.

I Trust Anchor e gli Intermediari DEVONO esporre l'endpoint Federation Fetch, dove i Subordinate Statement sono richiesti per validare la firma dell'Entity Configuration della Foglia.

.. note::
  L'endpoint Federation Fetch PUÒ anche pubblicare certificati X.509 per ognuna delle chiavi pubbliche del Subordinato. Rendendo la distribuzione dei certificati X.509 emessi tramite un servizio RESTful.

**Ruolo nell'Onboarding**: Durante la registrazione delle entità, i Trust Anchor e gli Intermediari emettono Subordinate Statement per attestare formalmente la registrazione e le capacità delle nuove entità. Queste dichiarazioni stabiliscono la relazione di trust gerarchica e applicano eventuali policy di metadati richieste che vincolano o migliorano le capacità dichiarate dell'entità basate sulle policy di federazione.

**Ruolo nelle Operazioni**: Durante le operazioni di credenziali, i Subordinate Statement sono recuperati per validare le catene di trust e applicare le policy di metadati correnti. Abilitano la verifica in tempo reale dello stato di registrazione di un'entità e garantiscono che le capacità operative siano conformi alle policy a livello di federazione e all'ambito autorizzato dell'entità.

Di seguito è riportato un esempio non normativo di un Subordinate Statement emesso da un Registration Body (come il Trust Anchor o il suo Intermediario) in relazione a uno dei suoi Subordinati.

.. code-block:: json

    {
        "alg": "ES256",
        "kid": "em3cmnZgHIYFsQ090N6B3Op7LAAqj8rghMhxGmJstqg",
        "typ": "entity-statement+jwt"
    }

.. code-block:: json

    {
        "exp": 1649623546,
        "iat": 1649450746,
        "iss": "https://intermediate.example.org",
        "sub": "https://rp.example.it",
        "jwks": {
            "keys": [ // keys about the Subordinate
                {
                    "kty": "EC",
                    "kid": "2HnoFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs",
                    "crv": "P-256",
                    "x": "1kNR9Ar3MzMokYTY8BRvRIue85NIXrYX4XD3K4JW7vI",
                    "y": "slT14644zbYXYF-xmw7aPdlbMuw3T1URwI4nafMtKrY",
                    "x5c": [
                      // <X.509 certificate about the Subordinate>
                      ]
                }
            ]
        },
        "metadata_policy": {
            "openid_credential_verifier": {
                "scope": {
                    "subset_of": [
                         "eu.europa.ec.eudiw.pid.1",
                         "given_name",
                         "family_name",
                         "email"
                      ]
                },
                "vp_formats": {
                    "dc+sd-jwt": {
                        "sd-jwt_alg_values": [
                            "ES256",
                            "ES384"
                        ],
                        "kb-jwt_alg_values": [
                            "ES256",
                            "ES384"
                        ]
                    }
                }
            }
         }
    }


.. note::
  **Firma del Subordinate Statement**

  Le stesse considerazioni e requisiti fatti per l'Entity Configuration e in relazione ai meccanismi di firma DEVONO essere applicati per i Subordinate Statement.


Subordinate Statement
^^^^^^^^^^^^^^^^^^^^^

Il Subordinate Statement emesso dai Trust Anchor e dagli Intermediari contiene i seguenti attributi:

.. list-table::
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Richiesto**
   * - **iss**
     - Vedi `OID-FED`_ Sezione 3 per ulteriori dettagli.
     - |check-icon|
   * - **sub**
     - Vedi `OID-FED`_ Sezione 3 per ulteriori dettagli.
     - |check-icon|
   * - **iat**
     - Vedi `OID-FED`_ Sezione 3 per ulteriori dettagli.
     - |check-icon|
   * - **exp**
     - Vedi `OID-FED`_ Sezione 3 per ulteriori dettagli.
     - |check-icon|
   * - **jwks**
     - JWKS di Federazione dell'entità *sub*. Vedi `OID-FED`_ Sezione 3 per ulteriori dettagli.
     - |check-icon|
   * - **metadata_policy**
     - Oggetto JSON che descrive la policy dei Metadati. Ogni chiave dell'Oggetto JSON rappresenta un identificatore del tipo di metadati e ogni valore DEVE essere un Oggetto JSON che rappresenta la policy dei metadati secondo quel tipo di metadati. Si prega di fare riferimento alle specifiche `OID-FED`_, Sezione 6.1, per i dettagli di implementazione.
     - |uncheck-icon|
   * - **trust_marks**
     - Array JSON contenente i Trust Mark emessi da se stesso per il soggetto subordinato.
     - |uncheck-icon|
   * - **constraints**
     - PUÒ contenere gli **allowed_leaf_entity_types**, che restringe quali tipi di metadati il soggetto è autorizzato a pubblicare. PUÒ contenere il numero massimo di Intermediari consentiti tra se stesso e la Foglia (**max_path_length**)
     - |check-icon|


Discovery della Federazione
---------------------------

La Scoperta di Entità di Federazione è il processo attraverso il quale i partecipanti verificano l'identità e lo stato di altre entità di federazione. Questo comporta l'interrogazione degli endpoint di federazione per confermare lo stato di validità dell'entità e la conformità al Trust Framework.

Il processo di scoperta utilizza l'API di Federazione per raccogliere informazioni sulle entità e produce Trust Chain che validano la conformità e l'autorizzazione dell'entità all'interno della federazione.

Il processo di scoperta stabilisce i concetti fondamentali che vengono poi applicati in scenari operativi specifici come dettagliato nella sezione Meccanismo di Trust Evaluation.

.. note::
  I Trust Anchor DEVONO distribuire le loro Chiavi Pubbliche di Federazione attraverso meccanismi sicuri fuori banda, come pubblicarle su una pagina web verificata o archiviarle in un repository remoto come parte di una lista di trust. La logica dietro questo requisito è che fare affidamento solo sui dati forniti all'interno dell'Entity Configuration del Trust Anchor non mitiga adeguatamente i rischi associati agli attacchi di manipolazione DNS e TLS. Per garantire la sicurezza, tutti i partecipanti DEVONO ottenere le chiavi pubbliche del Trust Anchor utilizzando questi metodi fuori banda. Dovrebbero quindi confrontare queste chiavi con quelle ottenute dall'Entity Configuration del Trust Anchor, scartando qualsiasi chiave che non corrisponda. Questo processo aiuta a garantire l'integrità e l'autenticità delle chiavi pubbliche del Trust Anchor e la sicurezza generale della federazione (:ref:`WP_017 <wallet-instance-testcases>`).

Ogni Subordinate Statement è verificabile nel tempo e DEVE avere una data di scadenza. La revoca di ogni dichiarazione è verificabile in tempo reale e online (solo per flussi remoti) attraverso gli endpoint di federazione.

.. note::
  La revoca di un'Entità è fatta con l'indisponibilità del Subordinate Statement relativo ad essa. Se il Trust Anchor o il suo Intermediario non pubblica un Subordinate Statement valido, o se pubblica un Subordinate Statement scaduto/non valido, il soggetto del Subordinate Statement DEVE essere inteso come non valido o revocato.

La concatenazione delle dichiarazioni, attraverso la combinazione di questi meccanismi di firma e il binding di claim e chiavi pubbliche, forma la Trust Chain.

Le Trust Chain possono anche essere verificate offline, utilizzando una delle chiavi pubbliche del Trust Anchor.

.. note::
  Poiché l'Istanza del Wallet non è un'Entità di Federazione, il Meccanismo di Trust Evaluation relativo ad essa **richiede la presentazione del Wallet Attestation durante le fasi di emissione e presentazione delle credenziali**.

  Il Wallet Attestation trasmette tutte le informazioni richieste riguardanti l'istanza, come la sua chiave pubblica e qualsiasi altra informazione tecnica o amministrativa, senza alcun dato personale dell'Utente.

Trust Chain
-----------

La Trust Chain è una sequenza di dichiarazioni verificate che valida la conformità di un partecipante con la Federazione. Ha una data di scadenza, oltre la quale DEVE essere rinnovata per ottenere i metadati freschi e aggiornati. La data di scadenza della Trust Chain è determinata dal timestamp di scadenza più precoce tra tutti i timestamp di scadenza contenuti nelle dichiarazioni. Nessuna Entità può forzare la data di scadenza della Trust Chain ad essere superiore a quella configurata dal Trust Anchor.

**Ruolo nell'Onboarding**: Durante la registrazione delle entità, le Trust Chain sono costruite per dimostrare la relazione di trust gerarchica completa dal Trust Anchor alla nuova entità. Questo stabilisce la posizione legittima dell'entità nella federazione e valida la sua conformità con tutte le policy e i vincoli applicabili.

**Ruolo nelle Operazioni**: Durante l'emissione e la presentazione delle credenziali, le Trust Chain forniscono prova crittografica della validità dell'entità e dello stato di conformità. Abilitano la verifica offline delle relazioni di trust e supportano scenari dove l'accesso in tempo reale agli endpoint di federazione potrebbe non essere disponibile, garantendo al contempo che le attestazioni di trust rimangano correnti e verificabili.

Di seguito è riportata una rappresentazione astratta di una Trust Chain.

.. code-block:: json

    [
        "EntityConfiguration-as-SignedJWT-selfissued-byLeaf",
        "EntityStatement-as-SignedJWT-issued-byTrustAnchor"
    ]

Di seguito è riportato un esempio non normativo di una Trust Chain, composta da un Array JSON contenente JWT, con un Intermediario coinvolto.

.. code-block:: json

    [
      "eyJhbGciOiJFUzI1NiIsImtpZCI6Ik5GTTFXVVZpVWxZelVXcExhbWxmY0VwUFJWWTJWWFpJUmpCblFYWm1SSGhLWVVWWVVsZFRRbkEyTkEiLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk1OTA2MDIsImlhdCI6MTY0OTQxNzg2MiwiaXNzIjoiaHR0cHM6Ly9ycC5leGFtcGxlLm9yZyIsInN1YiI6Imh0dHBzOi8vcnAuZXhhbXBsZS5vcmciLCJqd2tzIjp7ImtleXMiOlt7Imt0eSI6IkVDIiwia2lkIjoiTkZNMVdVVmlVbFl6VVdwTGFtbGZjRXBQUlZZMlZYWklSakJuUVhabVJIaEtZVVZZVWxkVFFuQTJOQSIsImNydiI6IlAtMjU2IiwieCI6InVzbEMzd2QtcFgzd3o0YlJZbnd5M2x6cGJHWkZoTjk2aEwyQUhBM01RNlkiLCJ5IjoiVkxDQlhGV2xkTlNOSXo4a0gyOXZMUjROMThCa3dHT1gyNnpRb3J1UTFNNCJ9XX0sIm1ldGFkYXRhIjp7Im9wZW5pZF9yZWx5aW5nX3BhcnR5Ijp7ImFwcGxpY2F0aW9uX3R5cGUiOiJ3ZWIiLCJjbGllbnRfaWQiOiJodHRwczovL3JwLmV4YW1wbGUub3JnLyIsImNsaWVudF9yZWdpc3RyYXRpb25fdHlwZXMiOlsiYXV0b21hdGljIl0sImp3a3MiOnsia2V5cyI6W3sia3R5IjoiRUMiLCJraWQiOiJORk0xV1VWaVVsWXpVV3BMYW1sZmNFcFBSVlkyVlhaSVJqQm5RWFptUkhoS1lVVllVbGRUUW5BMk5BIiwiY3J2IjoiUC0yNTYiLCJ4IjoidXNsQzN3ZC1wWDN3ejRiUllud3kzbHpwYkdaRmhOOTZoTDJBSEEzTVE2WSIsInkiOiJWTENCWEZXbGROU05JejhrSDI5dkxSNE4xOEJrd0dPWDI2elFvcnVRMU00In1dfSwiY2xpZW50X25hbWUiOiJOYW1lIG9mIGFuIGV4YW1wbGUgb3JnYW5pemF0aW9uIiwiY29udGFjdHMiOlsib3BzQHJwLmV4YW1wbGUuaXQiXSwiZ3JhbnRfdHlwZXMiOlsicmVmcmVzaF90b2tlbiIsImF1dGhvcml6YXRpb25fY29kZSJdLCJyZWRpcmVjdF91cmlzIjpbImh0dHBzOi8vcnAuZXhhbXBsZS5vcmcvb2lkYy9ycC9jYWxsYmFjay8iXSwicmVzcG9uc2VfdHlwZXMiOlsiY29kZSJdLCJzY29wZSI6ImV1LmV1cm9wYS5lYy5ldWRpdy5waWQuMSBldS5ldXJvcGEuZWMuZXVkaXcucGlkLml0LjEgZW1haWwiLCJzdWJqZWN0X3R5cGUiOiJwYWlyd2lzZSJ9LCJmZWRlcmF0aW9uX2VudGl0eSI6eyJmZWRlcmF0aW9uX3Jlc29sdmVfZW5kcG9pbnQiOiJodHRwczovL3JwLmV4YW1wbGUub3JnL3Jlc29sdmUvIiwib3JnYW5pemF0aW9uX25hbWUiOiJFeGFtcGxlIFJQIiwiaG9tZXBhZ2VfdXJpIjoiaHR0cHM6Ly9ycC5leGFtcGxlLml0IiwicG9saWN5X3VyaSI6Imh0dHBzOi8vcnAuZXhhbXBsZS5pdC9wb2xpY3kiLCJsb2dvX3VyaSI6Imh0dHBzOi8vcnAuZXhhbXBsZS5pdC9zdGF0aWMvbG9nby5zdmciLCJjb250YWN0cyI6WyJ0ZWNoQGV4YW1wbGUuaXQiXX19LCJ0cnVzdF9tYXJrcyI6W3siaWQiOiJodHRwczovL3JlZ2lzdHJ5LmVpZGFzLnRydXN0LWFuY2hvci5leGFtcGxlLmV1L29wZW5pZF9yZWx5aW5nX3BhcnR5L3B1YmxpYy8iLCJ0cnVzdF9tYXJrIjoiZXlKaCBcdTIwMjYifV0sImF1dGhvcml0eV9oaW50cyI6WyJodHRwczovL2ludGVybWVkaWF0ZS5laWRhcy5leGFtcGxlLm9yZyJdfQ.Un315HdckvhYA-iRregZAmL7pnfjQH2APz82blQO5S0sl1JR0TEFp5E1T913g8GnuwgGtMQUqHPZwV6BvTLA8g",
      "eyJhbGciOiJFUzI1NiIsImtpZCI6IlNURkRXV2hKY0dWWFgzQjNSVmRaYWtsQ0xUTnVNa000WTNGNlFUTk9kRXRyZFhGWVlYWjJjWGN0UVEiLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk2MjM1NDYsImlhdCI6MTY0OTQ1MDc0NiwiaXNzIjoiaHR0cHM6Ly9pbnRlcm1lZGlhdGUuZWlkYXMuZXhhbXBsZS5vcmciLCJzdWIiOiJodHRwczovL3JwLmV4YW1wbGUub3JnIiwiandrcyI6eyJrZXlzIjpbeyJrdHkiOiJFQyIsImtpZCI6Ik5GTTFXVVZpVWxZelVXcExhbWxmY0VwUFJWWTJWWFpJUmpCblFYWm1SSGhLWVVWWVVsZFRRbkEyTkEiLCJjcnYiOiJQLTI1NiIsIngiOiJ1c2xDM3dkLXBYM3d6NGJSWW53eTNsenBiR1pGaE45NmhMMkFIQTNNUTZZIiwieSI6IlZMQ0JYRldsZE5TTkl6OGtIMjl2TFI0TjE4Qmt3R09YMjZ6UW9ydVExTTQifV19LCJtZXRhZGF0YV9wb2xpY3kiOnsib3BlbmlkX3JlbHlpbmdfcGFydHkiOnsic2NvcGUiOnsic3Vic2V0X29mIjpbImV1LmV1cm9wYS5lYy5ldWRpdy5waWQuMSwgIGV1LmV1cm9wYS5lYy5ldWRpdy5waWQuaXQuMSJdfSwicmVxdWVzdF9hdXRoZW50aWNhdGlvbl9tZXRob2RzX3N1cHBvcnRlZCI6eyJvbmVfb2YiOlsicmVxdWVzdF9vYmplY3QiXX0sInJlcXVlc3RfYXV0aGVudGljYXRpb25fc2lnbmluZ19hbGdfdmFsdWVzX3N1cHBvcnRlZCI6eyJzdWJzZXRfb2YiOlsiUlMyNTYiLCJSUzUxMiIsIkVTMjU2IiwiRVM1MTIiLCJQUzI1NiIsIlBTNTEyIl19fX0sInRydXN0X21hcmtzIjpbeyJpZCI6Imh0dHBzOi8vdHJ1c3QtYW5jaG9yLmV4YW1wbGUuZXUvb3BlbmlkX3JlbHlpbmdfcGFydHkvcHVibGljLyIsInRydXN0X21hcmsiOiJleUpoYiBcdTIwMjYifV19._qt5-T6DahP3TuWa_27klE8I9Z_sPK2FtQlKY6pGMPchbSI2aHXY3aAXDUrObPo4CHtqgg3J2XcrghDFUCFGEQ","eyJhbGciOiJFUzI1NiIsImtpZCI6ImVXa3pUbWt0WW5kblZHMWxhMjU1ZDJkQ2RVZERSazQwUWt0WVlVMWFhRFZYT1RobFpHdFdXSGQ1WnciLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk2MjM1NDYsImlhdCI6MTY0OTQ1MDc0NiwiaXNzIjoiaHR0cHM6Ly90cnVzdC1hbmNob3IuZXhhbXBsZS5ldSIsInN1YiI6Imh0dHBzOi8vaW50ZXJtZWRpYXRlLmVpZGFzLmV4YW1wbGUub3JnIiwiandrcyI6eyJrZXlzIjpbeyJrdHkiOiJFQyIsImtpZCI6IlNURkRXV2hKY0dWWFgzQjNSVmRaYWtsQ0xUTnVNa000WTNGNlFUTk9kRXRyZFhGWVlYWjJjWGN0UVEiLCJjcnYiOiJQLTI1NiIsIngiOiJyQl9BOGdCUnh5NjhVTkxZRkZLR0ZMR2VmWU5XYmgtSzh1OS1GYlQyZkZJIiwieSI6IlNuWVk2Y3NjZnkxcjBISFhLTGJuVFZsamFndzhOZzNRUEs2WFVoc2UzdkUifV19LCJ0cnVzdF9tYXJrcyI6W3siaWQiOiJodHRwczovL3RydXN0LWFuY2hvci5leGFtcGxlLmV1L2ZlZGVyYXRpb25fZW50aXR5L3RoYXQtcHJvZmlsZSIsInRydXN0X21hcmsiOiJleUpoYiBcdTIwMjYifV19.r3uoi-U0tx0gDFlnDdITbcwZNUpy7M2tnh08jlD-Ej9vMzWMCXOCCuwIn0ZT0jS4M_sHneiG6tLxRqj-htI70g"
    ]


.. note::
  L'intera Trust Chain è verificabile possedendo solo le chiavi pubbliche del Trust Anchor.

Ci sono eventi in cui le chiavi non sono disponibili per verificare l'intera catena di trust:

 - **Cambio di Chiave da parte del Credential Issuer**: Il Credential Issuer PUÒ aggiornare le sue chiavi crittografiche. Le chiavi crittografiche DEVONO essere considerate valide se valutate entro il loro periodo di validità originariamente designato a meno che una ragione di sicurezza non le renda inutilizzabili. La ragione di revoca DEVE essere pubblicata. Le chiavi crittografiche storiche, cioè le chiavi crittografiche pubbliche inutilizzate o revocate, DEVONO essere pubblicate utilizzando l'Endpoint delle Chiavi Storiche di Federazione.

 - **Cambio nei Tipi di Credenziali**: Se il Credential Issuer cambia i **tipi** di Credenziali emesse, per esempio decidendo di non emettere più uno o più tipi di Credenziali, le relative chiavi crittografiche pubbliche DEVONO essere disponibili per il periodo di validità originariamente designato.

 - **Fusione di Credential Issuer**: Se un Credential Issuer si fonde con un altro, creando una nuova Entità Organizzativa o lavorando per conto di un'altra utilizzando un hostname o dominio diverso, la configurazione di federazione **precedentemente** disponibile e le chiavi storiche DEVONO essere mantenute disponibili agli endpoint well-known del Credential Issuer originale.

 - **Credential Issuer Diventa Inattivo**: Se un Credential Issuer diventa inattivo, la sua **relativa** Entity Configuration e l'Endpoint di Entità Storica di Federazione DEVONO essere mantenuti disponibili.

Meccanismi di Attestazione di Trust Offline
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I flussi offline non consentono la valutazione in tempo reale dello stato di un'Entità, come la sua revoca. Allo stesso tempo, l'utilizzo di Trust Chain di breve durata consente il raggiungimento di attestazioni di trust compatibili con i protocolli amministrativi di revoca richiesti (ad esempio, una revoca deve essere propagata in meno di 24 ore, quindi la Trust Chain non deve essere valida per più di quel periodo).


Attestazione di Trust del Wallet Offline
""""""""""""""""""""""""""""""""""""""""

Dato che l'Istanza del Wallet non può pubblicare i suoi metadati online all'endpoint *.well-known/openid-federation*, DEVE ottenere un Wallet Attestation emesso dal suo Fornitore di Wallet. Il Wallet Attestation DEVE contenere tutte le informazioni rilevanti riguardanti le capacità di sicurezza dell'Istanza del Wallet e la sua configurazione relativa al protocollo. DOVREBBE contenere la Trust Chain relativa al suo emittente (Fornitore di Wallet).


Metadati del Relying Party Offline
""""""""""""""""""""""""""""""""""

Poiché la Scoperta di Entità di Federazione è applicabile solo in scenari online, è possibile includere la Trust Chain nelle richieste di presentazione che il Relying Party può emettere per un'Istanza del Wallet.

Il Relying Party DEVE firmare la richiesta di presentazione, la richiesta DOVREBBE includere il claim `trust_chain` nei suoi parametri di header JWT, contenente la Trust Chain di Federazione relativa a se stesso.

L'Istanza del Wallet che verifica la richiesta emessa dal Relying Party DEVE utilizzare le chiavi pubbliche del Trust Anchor per validare l'intera Trust Chain relativa al Relying Party prima di attestare la sua affidabilità.

Inoltre, l'Istanza del Wallet applica la policy dei metadati, se presente.

Rinnovo Rapido della Trust Chain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il metodo di rinnovo rapido della Trust Chain offre un modo semplificato per mantenere la validità di una catena di trust senza sottoporsi nuovamente al processo di scoperta completo. È particolarmente utile per aggiornare rapidamente le Trust Relationship quando si verificano cambiamenti minori o quando la Trust Chain è vicina alla scadenza ma la struttura generale della federazione non è cambiata significativamente.

Il processo di rinnovo rapido della Trust Chain è iniziato recuperando nuovamente l'Entity Configuration della foglia. Tuttavia, a differenza del processo di scoperta di federazione che può comportare il recupero delle Entity Configuration a partire dagli authority hint, il rinnovo rapido si concentra sull'ottenere direttamente i Subordinate Statement. Queste dichiarazioni sono richieste utilizzando il `source_endpoint` fornito al loro interno, che punta alla posizione dove le dichiarazioni possono essere recuperate.


Meccanismo di Trust Evaluation
------------------------------

I Trust Anchor DEVONO distribuire le loro Chiavi Pubbliche di Federazione attraverso meccanismi sicuri fuori banda, come pubblicarle su una pagina web verificata o archiviarle in un repository remoto come parte di una lista di trust. La logica dietro questo requisito è che fare affidamento solo sui dati forniti all'interno dell'Entity Configuration del Trust Anchor non mitiga adeguatamente i rischi associati agli attacchi di manipolazione DNS e TLS. Per garantire la sicurezza, tutti i partecipanti DEVONO ottenere le chiavi pubbliche del Trust Anchor utilizzando questi metodi fuori banda. Dovrebbero quindi confrontare queste chiavi con quelle ottenute dall'Entity Configuration del Trust Anchor, scartando qualsiasi chiave che non corrisponda. Questo processo aiuta a garantire l'integrità e l'autenticità delle chiavi pubbliche del Trust Anchor e la sicurezza generale della federazione.

Il Trust Anchor pubblica l'elenco dei suoi Subordinati (endpoint di Elenco Subordinati di Federazione) e le attestazioni dei loro metadati e chiavi pubbliche (Subordinate Statement).

Ogni partecipante, inclusi Trust Anchor, Intermediario, Credential Issuer, Fornitore di Wallet e Relying Party, pubblica i propri metadati e chiavi pubbliche (endpoint Entity Configuration) nella risorsa web well-known **.well-known/openid-federation**.

Ognuno di questi può essere verificato utilizzando il Subordinate Statement emesso da un superiore, come il Trust Anchor o un Intermediario.

Ogni Subordinate Statement è verificabile nel tempo e DEVE avere una data di scadenza. La revoca di ogni dichiarazione è verificabile in tempo reale e online (solo per flussi remoti) attraverso gli endpoint di federazione.

.. note::
  La revoca di un'Entità è fatta con l'indisponibilità del Subordinate Statement relativo ad essa. Se il Trust Anchor o il suo Intermediario non pubblica un Subordinate Statement valido, o se pubblica un Subordinate Statement scaduto/non valido, il soggetto del Subordinate Statement DEVE essere inteso come non valido o revocato.

La concatenazione delle dichiarazioni, attraverso la combinazione di questi meccanismi di firma e il binding di claim e chiavi pubbliche, forma la Trust Chain.

Le Trust Chain possono anche essere verificate offline, utilizzando una delle chiavi pubbliche del Trust Anchor.

.. note::
  Poiché l'Istanza del Wallet non è un'Entità di Federazione, il Meccanismo di Trust Evaluation relativo ad essa **richiede la presentazione del Wallet Attestation durante le fasi di emissione e presentazione delle credenziali**.

  Il Wallet Attestation trasmette tutte le informazioni richieste riguardanti l'istanza, come la sua chiave pubblica e qualsiasi altra informazione tecnica o amministrativa, senza alcun dato personale dell'Utente.

**Ruolo nell'Onboarding**: I meccanismi di trust evaluation sono essenziali durante la registrazione delle entità e la gestione del ciclo di vita per verificare lo stato di conformità dei nuovi partecipanti e validare i cambiamenti alle entità esistenti. Questo include la validazione delle credenziali di registrazione delle entità che richiedono l'onboarding e garantire che soddisfino le policy di federazione prima di concedere l'autorizzazione operativa.

**Ruolo nelle Operazioni**: Durante le operazioni di emissione e presentazione delle credenziali, la trust evaluation fornisce verifica in tempo reale della validità dell'entità e dello stato di conformità. Questo abilita transazioni di credenziali sicure garantendo che tutte le entità partecipanti (credential issuer, relying party, fornitori di wallet) mantengano il loro stato autorizzato e siano conformi alle policy di federazione correnti.


Stabilire Trust con i Credential Issuer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nel processo di emissione, la Trust Evaluation garantisce l'integrità e l'autenticità delle Credenziali emesse e l'affidabilità dei loro Emittenti. Questa sezione delinea i meccanismi di Trust Evaluation distinti dai flussi di protocollo, implementati dalle Istanze del Wallet e dai Relying Party, come descritto nella sezione dedicata.

Le Trust Evaluation implementano modi diversi, come definito di seguito:

* **Scoperta di Entità di Federazione**: Le Istanze del Wallet e i Relying Party DEVONO verificare l'identità dell'Emittente utilizzando il processo di Scoperta di Entità di Federazione definito in :ref:`trust-infrastructure:Discovery della Federazione`. Questo comporta l'interrogazione degli endpoint di federazione per confermare lo stato di validità dell'Emittente e la conformità al Trust Framework.

* **Trust Chain**: Le Istanze del Wallet e i Relying Party valutano le Trust Chain dell'Emittente utilizzando i meccanismi definiti in :ref:`trust-infrastructure:Trust Chain`. Le Trust Chain possono essere fornite staticamente o costruite attraverso un processo di Scoperta di Entità di Federazione, per garantire che l'entità che richiede la Credenziale faccia parte di una federazione riconosciuta e fidata.

* **Valutazione dei Trust Mark**: I Trust Mark sono valutati per garantire la conformità continua alle policy di federazione. Questi marchi indicano l'aderenza a standard e pratiche specifici richiesti dalla federazione.

* **Valutazione delle Policy**: Le Istanze del Wallet e i Relying Party DEVONO verificare che il Credential Issuer sia autorizzato nell'emissione della Credenziale di loro interesse. Metadati, policy dei metadati e Trust Mark sono utilizzati per l'implementazione di questi controlli (:ref:`WP_050a <wallet-credential-issuance-testcases>`).

Nel processo rappresentato nel diagramma di sequenza sottostante, l'Istanza del Wallet utilizza l'API di Federazione per scoprire e raccogliere tutti i Credential Issuer abilitati all'interno della federazione. Il processo di scoperta produce la Trust Chain. Quando la Trust Chain è fornita staticamente all'interno di una richiesta firmata o Credenziale, RICHIEDE solo di essere aggiornata quando la connessione internet è disponibile, mentre DEVE essere aggiornata quando la Trust Chain fornita staticamente risulta scaduta.

.. plantuml:: plantuml/trust-evaluation-flow.puml
    :width: 99%
    :alt: La figura illustra il Processo di Trust Evaluation.
    :caption: `Processo di Trust Evaluation. <https://www.plantuml.com/plantuml/svg/fPE_Rjmm38TtFGMHfTCrUuOWXwlJ6bs2fd-MB8n5nqHbIg2ek-JjwxFW9XUSkzIJ87_y-AD1tsH3jJ86-Aub6pHx30MDey2TnevoTWdLkEE4Ol0BGo0xkTgrW1akTagUn1W3j3aNqeiJgcrcgXKZ7Sap6btMZblfXZZHhhfXStqzEQ_WbgmRfjE738qOsmlielJyL7IEzo201XyF5CBcjyI3NCP4mdxJawUA08bFaSNShfsrjSCLV2ChAcUrIumJldasnMwAMco8Ugpvmc8PUerZJVZE4M9Cq4S5mcvuL-PWUjuqQPjbrlyUSzLyNnwZUXOqWdj3ev74ghe_0gkAvGlynC3-M6q3GLBQSomPygkgP9Qd-Utjts3BG5_f9Jz8qhXdJnvOZjpvJ8x4E_Ul07LfTWEoE8V1eEtVtW7doWAAXnz2pucL_CfSTSV9mu5jgCbFTvz2fhNQxPJV5h8Q6jMegpDiKmfC6UvYu6uwd6C-aVAUwbBrB1XW94EFXkVepsI0U-I0Zu7WzHVCC07nG7vUGiwve7JaRaXy6SCV>`_

.. note::
  Come mostrato nella figura, il processo di Trust Evaluation è completamente separato e distinto dal flusso specifico del protocollo. Opera in un flusso diverso e utilizza protocolli specializzati progettati specificamente per questo scopo.

Stabilire Trust con il Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nel contesto della valutazione dei Relying Party, la responsabilità per la Trust Evaluation spetta esclusivamente all'Istanza del Wallet.
I meccanismi di Trust Evaluation sono distinti dai flussi di protocollo e sono implementati dall'Istanza del Wallet, come dettagliato nella sezione dedicata.

Le Trust Evaluation sono condotte come segue:

* **Scoperta di Entità di Federazione**: Quando l'Istanza del Wallet riceve una richiesta firmata emessa da un Relying Party, l'Istanza del Wallet DEVE verificare l'identità del Relying Party utilizzando il processo di Scoperta di Entità di Federazione definito in :ref:`trust-infrastructure:Discovery della Federazione`. Questo comporta l'interrogazione degli endpoint di federazione per confermare lo stato di validità del Relying Party e la conformità al Trust Framework e valutare la firma della richiesta utilizzando il materiale crittografico ottenuto dalla Trust Chain.

* **Trust Chain**: L'Istanza del Wallet valuta le Trust Chain del Relying Party utilizzando i meccanismi definiti in :ref:`trust-infrastructure:Trust Chain`. Le Trust Chain possono essere fornite staticamente o costruite attraverso un processo di Scoperta di Entità di Federazione, per garantire che il Relying Party faccia parte di una federazione riconosciuta e fidata (:ref:`WP_079 <wallet-credential-presentation-testcases>`).

* **Valutazione dei Trust Mark**: I Trust Mark sono valutati per garantire la conformità continua alle policy di federazione. Questi marchi indicano l'aderenza a standard e pratiche specifici richiesti dalla federazione. I Relying Party POSSONO includere Trust Mark nella loro Entity Configuration per segnalare proprietà amministrative e conformità a profili specifici, come le concessioni nell'interagire con utenti minorenni (:ref:`WP_080 <wallet-credential-presentation-testcases>`).

* **Valutazione delle Policy**: L'Istanza del Wallet DEVE verificare che il Relying Party sia autorizzato a richiedere la Credenziale di interesse. Metadati, policy dei metadati e Trust Mark sono utilizzati per implementare questi controlli (:ref:`WP_087 <wallet-credential-presentation-testcases>`).

Nel processo raffigurato nel diagramma di sequenza sottostante, l'Istanza del Wallet utilizza l'API di Federazione per scoprire e raccogliere tutti i Relying Party abilitati all'interno della federazione. Il processo di scoperta produce la Trust Chain. Quando la Trust Chain è fornita staticamente all'interno di una richiesta firmata, deve solo essere aggiornata quando una connessione internet è disponibile, ma DEVE essere aggiornata se la Trust Chain fornita staticamente è scaduta.

.. plantuml:: plantuml/trust-rp-discovery-flow.puml
    :width: 99%
    :alt: La figura illustra il Processo di Scoperta del Relying Party.
    :caption: `Trust Evaluation - Processo di Scoperta del Relying Party. <https://www.plantuml.com/plantuml/svg/ZLDFRzi-3BtxKn2z_4xvzTv3qQ1_i64x16dNNGeKgaGdH6NAawYq_lPZvBbD33Tm3ev5Fpw-Hv5NIKoKt7XOe--8Dx3ISmStb6pOOUogLizagJKiyDjuZ_ATDOajWabmreTWY9qTuQyV2-Q8-XZni2o8XvYJm9BjDaGuLpR1sA0Z8yfOZSekBY-L-G8Y_iceQGRQ60IjeDDO2ZbQhBJqGe4ZoHUGQCEAin4Tif3ncen9NurGu85pikQOog4D3i6m0zmPdrLi0jdY9qbblBQcXjxUzTOG0wMzt1qvLV56iYK-p2bi781OC38AsC2CTg-j0ltDaAN_GbQ37QWgSYghL3WKaTF-FWwx_f_AoY-UBBnYbohq2Vk2qxs_Gx5RMAyqxPQ5f8Fhm3LjSYnzV68m0l-_eVUBLmvlV1vQP7AB6Xr6CzXHgaaBQvGSUPAvEgNgzbsYiMefYrhQvtuZbWHr34qHE-8w8M7Ltz6OgY_lGsYX3X7GsEq8KW1VQ7nO3fsRigOGsA30Pu-UwptusRG4lzO_1sQbcPJSCz_dbn0TiH64Uz5dWwT5ZMaU3uUcZRYZa1EaWUg9o_2KhtSVIWT3Fx1BJ_mnuFrmdz24xAggFEOhEnhbhtQiZ7xPfiputb94DtU1zEej_jlEGuibdlhTcCkrLECoPFQCjp66EDlpicqzOO9Ly6JrPKxE3KRQOJ_mDR7nqA0OPyHKLretD_ul>`_

.. note::
  Come mostrato nella figura, è richiesta una connessione internet per aggiornare la Trust Chain su un RP e controllare il suo stato di revoca.

Stabilire Trust con il Relying Party che opera tramite Intermediario
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Quando un Relying Party opera tramite un Intermediario di Relying Party, l'Istanza del Wallet DEVE eseguire un processo di Trust Evaluation esteso che include la validazione del Trust Mark dell'Intermediario di Relying Party. Questo processo si svolge durante la fase di costruzione e validazione della Trust Chain e consente al Wallet di presentare all'Utente informazioni trasparenti sull'entità che ha registrato e garantisce il RP.

Il processo si articola nei seguenti passi:

1. **Download dell'Entity Configuration del RP**: L'Istanza del Wallet scarica l'Entity Configuration del Relying Party dall'endpoint ``/.well-known/openid-federation`` del RP. L'EC del RP contiene il claim ``authority_hints`` che punta all'URL dell'Intermediario di Relying Party (non direttamente al Trust Anchor).

2. **Identificazione dell'Intermediario di Relying Party**: Tramite il claim ``authority_hints`` nell'EC del RP, l'Istanza del Wallet identifica l'Intermediario di Relying Party e ne scarica l'Entity Configuration.

3. **Validazione del Trust Mark dell'Intermediario di Relying Party**: L'Istanza del Wallet verifica che l'Entity Configuration dell'Intermediario di Relying Party contenga un Trust Mark valido per il ruolo di Intermediario di Relying Party, emesso dal Trust Anchor. La validità del Trust Mark DEVE essere verificata tramite l'endpoint ``/trust_mark_status`` del Trust Anchor.

4. **Costruzione della Trust Chain tramite l'Intermediario di Relying Party**: L'Istanza del Wallet costruisce la Trust Chain completa: Entity Configuration del RP → Subordinate Statement emesso dall'Intermediario di Relying Party per il RP → Subordinate Statement emesso dal Trust Anchor per l'Intermediario di Relying Party → Entity Configuration del Trust Anchor. Questa catena attesta che il RP è una Foglia riconosciuta dall'Intermediario di Relying Party e che l'Intermediario di Relying Party è a sua volta riconosciuto dal Trust Anchor.

5. **Presentazione all'Utente**: Una volta completata la validazione, l'Istanza del Wallet DEVE indicare all'Utente che il Relying Party richiedente opera tramite un Intermediario di Relying Party riconosciuto, mostrando le informazioni identificative dell'Intermediario di Relying Party (ad esempio ``organization_name``) ottenute dalla sua Entity Configuration.

.. note::
  La presenza del Trust Mark con identificativo che termina con ``federation-entity/openid_credential_verifier_intermediary`` nell'EC dell'Intermediario di Relying Party costituisce la prova crittograficamente verificabile che l'entità è stata riconosciuta dal Trust Anchor come Intermediario di Relying Party autorizzato. L'Istanza del Wallet DEVE rifiutare la richiesta del RP se la Trust Chain non può essere costruita e validata tramite un Intermediario di Relying Party riconosciuto o direttamente tramite il Trust Anchor.

Valutare Trust con i Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Fornitore di Wallet emette il Wallet Attestation, certificando lo stato operativo delle sue Istanze del Wallet e includendo una delle loro chiavi pubbliche.

Il Wallet Attestation PUÒ contenere la Trust Chain che attesta l'affidabilità per il suo emittente (Fornitore di Wallet) al momento dell'emissione.

L'Istanza del Wallet fornisce il suo Wallet Attestation all'interno della richiesta firmata durante la fase di emissione PID/IT-Wallet ID. Il Credential Issuer DEVE valutare la Trust Chain sull'emittente del Wallet Attestation (formalmente, il Fornitore di Wallet).

Non-ripudio delle Attestazioni di Lunga Durata
----------------------------------------------

Il Trust Anchor e i suoi Intermediari DEVONO esporre l'endpoint delle Chiavi Storiche di Federazione, dove sono pubblicate tutte le parti pubbliche delle Chiavi dell'Entità di Federazione che non sono più utilizzate, sia scadute che revocate.

I dettagli di questo endpoint sono definiti nella `OID-FED`_ Sezione 8.7.

Ogni JWT contenente una Trust Chain negli header JWT può essere verificato nel tempo, poiché l'intera Trust Chain è verificabile utilizzando la chiave pubblica del Trust Anchor.

Anche se il Trust Anchor ha cambiato le sue chiavi crittografiche per la firma digitale, l'endpoint delle Chiavi Storiche di Federazione rende sempre disponibili le chiavi non più utilizzate per le verifiche di firma storiche.

X.509 PKI
---------

L'Infrastruttura a Chiave Pubblica (PKI) X.509 è un framework progettato per creare, gestire, distribuire, utilizzare, archiviare e revocare certificati digitali X.509. Al centro della PKI X.509 c'è il concetto di Autorità di Certificazione (CA), che emette certificati digitali alle entità. Questi certificati sono richiesti per stabilire comunicazioni sicure su reti, incluso internet, abilitando funzionalità di crittografia e firma digitale. La gerarchia PKI tipicamente coinvolge una CA radice in cima, con una o più CA subordinate sotto, formando una catena di trust. Le entità si affidano a questa catena di trust per verificare l'autenticità dei certificati. Gli standard X.509 definiscono il formato dei certificati a chiave pubblica.

L'integrazione di OpenID Federation 1.0 con la PKI tradizionale basata su X.509 (rfc:5280), completata da un'API RESTful, mira a migliorare l'infrastruttura con funzionalità aggiuntive, rendendola navigabile e trasparente.

Questo approccio sfrutta la natura dinamica e flessibile di OpenID Federation insieme al requisito dei Certificati X.509 per applicazioni legacy e scopi di interoperabilità, mirando ad affrontare le esigenze in evoluzione di verifica dello stato di registrazione dei partecipanti alla federazione, la loro conformità alle regole condivise e la gestione generale e interoperabile del trust in ecosistemi digitali multilaterali.

**Ruolo nell'Onboarding**: Durante la registrazione delle entità, i certificati X.509 completano i meccanismi di OpenID Federation fornendo interoperabilità con sistemi legacy e abilitando l'integrazione con infrastrutture PKI esistenti. Le entità auto-emettono certificati X.509 utilizzando le loro chiavi di federazione, estendendo le relazioni di trust ai sistemi tradizionali basati su certificati.

**Ruolo nelle Operazioni**: Durante le operazioni di credenziali, i certificati X.509 abilitano comunicazioni sicure con sistemi legacy e forniscono percorsi di verifica alternativi per entità che richiedono validazione PKI tradizionale. Questo approccio duale garantisce che l'infrastruttura IT-Wallet possa interoperare con sistemi legacy esistenti mantenendo meccanismi di trust moderni basati su federazione.

OpenID Federation e PKI basata su X.509 condividono diverse cose in comune, come elencato di seguito:

- **Approccio Gerarchico**: entrambi utilizzano un Trust Model gerarchico con una singola terza parte fidata sovrastante, nota come Trust Anchor, che è fidata sopra tutte le altre.
- **Decentralizzazione con Multipli Trust Anchor e Intermediari**: nonostante un modello gerarchico unico, la possibilità di avere multipli Trust Anchor e Intermediari, sotto uno o più Trust Anchor, introduce un livello di decentralizzazione.
- **Estensioni Personalizzate**: entrambi i sistemi consentono estensioni personalizzate per soddisfare requisiti specifici o per migliorare la funzionalità. I Certificati X.509 supportano estensioni personalizzate, OpenID Federation consente la definizione di metadati specifici del protocollo personalizzati, Trust Mark e policy utilizzando un Policy Language.
- **Catena di Trust/Certificato**: si affidano a una prova concatenata di trust, dove il trust è passato dall'autorità radice (Trust Anchor) attraverso Intermediari all'entità finale (Foglia).
- **Vincoli nella Catena**: i vincoli possono essere applicati all'interno della Trust Chain riguardo aspetti critici come la delegazione del trust, il numero di intermediari e i domini coinvolti.
- **Distribuzione di Chiavi Pubbliche**: Entrambi i sistemi coinvolgono la distribuzione della chiave pubblica del Trust Anchor per garantire che le entità possano verificare la catena di trust.
- **Registro di Chiavi Scadute**: Mantenere un registro di chiavi scadute è cruciale per entrambi, garantendo il non-ripudio delle firme passate anche quando le chiavi cambiano.


Trust Anchor di Federazione e CA X.509
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nel contesto di OpenID Federation, il Trust Anchor gioca un ruolo simile a quello di un'Autorità di Certificazione (CA) nelle Infrastrutture a Chiave Pubblica (PKI) basate su X.509. Entrambi servono come elementi fondamentali di trust all'interno dei loro rispettivi sistemi. In questo documento, il termine "Trust Anchor" è spesso utilizzato per comprendere entrambi i concetti. L'infrastruttura di trust descritta qui allinea il Trust Anchor di OpenID Federation con l'Autorità di Certificazione PKI X.509, rendendoli quindi un'unica entità unica che supporta sia `RFC 5280`_ che OpenID Federation 1.0.

Emissione di Certificati X.509
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In una Federazione OpenID, ogni partecipante è richiesto di auto-emettere la sua Entity Configuration, firmandola con una delle sue chiavi crittografiche che sono attestate dai Superiori Immediati.

Allo stesso modo, ogni Entità di federazione ha l'autonomia di emettere una dichiarazione firmata su se stessa sotto forma di un Certificato X.509.
I partecipanti alla federazione che hanno bisogno di emettere Certificati X.509 su se stessi e per i loro scopi specifici, possono emettere e firmare Certificati X.509 utilizzando una delle loro Chiavi dell'Entità di Federazione attestate dalle loro Autorità di Federazione (Superiore Immediato). Questo processo allinea l'emissione di Certificati X.509 con il paradigma di delegazione della federazione.

Questo è fattibile perché il Certificato X.509 può essere verificato utilizzando una Catena di Certificati X.509, simile all'approccio utilizzato per le Entity Configuration in OpenID Federation.

Le Foglie di Federazione non sono Autorità di Certificazione (CA) o intermediari CA autorizzati a emettere certificati X.509 per i loro subordinati. Invece, le Foglie di Federazione agiscono come intermediari per l'emissione di certificati esclusivamente su se stesse. Questo è realizzato applicando vincoli di denominazione appropriati per garantire che i certificati X.509 siano correttamente delimitati.
I vincoli di denominazione sono applicati dai Superiori Immediati all'interno dei certificati emessi all'entità Foglia, specificamente riguardo alle Chiavi dell'Entità di Federazione della Foglia. Di conseguenza, la Foglia può emettere certificati X.509 solo su se stessa, mantenendo così l'integrità della Trust Chain.

Quando un partecipante auto-emette un Certificato X.509, aderisce ai seguenti requisiti:

1. **Nome del Soggetto**: Il nome del soggetto del Certificato X.509 DEVE corrispondere all'identità del partecipante. Il nome del soggetto degli Intermediari e delle Foglie DEVE includere i seguenti attributi:

   .. list-table::
      :widths: 30 70
      :header-rows: 1

      * - Attributo
        - Requisito
      * - ``Country Name (C)``
        - DEVE contenere il codice paese ISO a due lettere.
      * - ``State or Province Name (ST)``
        - DEVE contenere la regione o stato dove l'entità è localizzata.
      * - ``Locality Name (L)``
        - DEVE contenere la città dove l'entità è localizzata.
      * - ``Organization Name (O)``
        - DEVE contenere il nome legale dell'organizzazione.
      * - ``Organizational Unit Name (OU)``
        - PUÒ contenere il nome del dipartimento all'interno dell'organizzazione (opzionale).
      * - ``Common Name (CN)``
        - DEVE contenere il nome DNS dell'identificatore unico dell'Entità di Federazione, che è incluso nel valore ``sub`` (soggetto) nella sua Entity Configuration di federazione, rimuovendo ``https://`` e qualsiasi path web.
      * - ``Email Address``
        - DEVE contenere l'indirizzo email di contatto dell'organizzazione.
      * - ``organizationIdentifier``
        - DEVE contenere il numero di registrazione che identifica univocamente l'organizzazione all'interno del servizio di registrazione, utilizzando il valore OID ``2.5.4.97`` come definito in ``ITU-T X.500``.

2. **Subject Alternative Name (SAN)**: Il Certificato X.509 DEVE includere un ``SAN URI`` che DEVE corrispondere ai valori **sub** e **iss** della sua Entity Configuration di federazione.
3. **Nome DNS**: Il Certificato X.509 DEVE includere un Nome DNS nel SAN che corrisponde al nome DNS contenuto all'interno dei valori **sub** e **iss** della sua Entity Configuration, rimuovendo ``https://`` e qualsiasi path web.
4. **Certificate Revocation List (CRL)**: Se il Certificato X.509 emesso ha un tempo di scadenza superiore a 24 ore, l'Emittente X.509 DEVE pubblicare una CRL per i Certificati X.509 emessi. Questo elenco DEVE essere accessibile e regolarmente aggiornato per garantire che qualsiasi Certificato X.509 compromesso o non valido sia prontamente revocato con la motivazione della revoca, se presente.
5. **Basic Constraints**: Il Certificato X.509 DEVE includere un'estensione ``Basic Constraints`` con ``CA:TRUE`` e una lunghezza massima del path di 1 se l'emittente del certificato è un Intermediario di Federazione. Se è una Foglia, la lunghezza massima del path DEVE essere impostata a 0. Questo indica che il Subordinato a cui il certificato si riferisce, può emettere Certificati X.509 solo su se stesso. L'estensione ``BasicConstraints`` DEVE essere impostata ``critical``.
6. **Key Usage**: ``Digital Signature``, ``Key Encipherment``, ``Certificate Sign``, ``CRL Sign`` DEVONO essere inclusi. L'estensione ``KeyUsage`` DEVE essere impostata ``critical``.
7. **Name Constraints**: Il Certificato X.509 DEVE includere ``Name Constraints`` per specificare domini e URI permessi ed esclusi. Per esempio:

   - Permessi:
     - ``URI.1=https://leaf.example.com``
     - ``DNS.1=leaf.example.com``
   - Esclusi:
     - ``DNS=localhost``
     - ``DNS=localhost.localdomain``
     - ``DNS=127.0.0.1``
     - ``DNS=example.com``
     - ``DNS=example.org``
     - ``DNS=example.net``
     - ``DNS=*.example.org``

8. **AuthorityKeyIdentifier**: Il Certificato X.509 DEVE includere un'estensione ``AuthorityKeyIdentifier``. Il campo ``keyIdentifier`` dell'estensione ``AuthorityKeyIdentifier`` DEVE essere presente e DEVE essere identico al campo ``SubjectKeyIdentifier`` del certificato dell'emittente. Questo consolida la costruzione e validazione della catena di certificati.

Di seguito è riportato un esempio non normativo, in testo semplice (formato OpenSSL), di una catena di certificati X.509 con una CA intermedia, a partire dal certificato Foglia.

.. literalinclude:: ../../examples/x5c.json
  :language: text

Utilizzando il livello sottostante stabilito con OpenID Federation 1.0, tutti i certificati X.509 sono emessi in modo propriamente decentralizzato utilizzando il pattern di delegazione.


Revoca di Certificati X.509
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un Certificato X.509 può essere revocato dal suo Emittente.
Le liste di revoca, e/o qualsiasi altro meccanismo di controllo della revoca, sono particolarmente richieste per i Certificati X.509 con un tempo di scadenza superiore a 24 ore; altrimenti, non sono richieste.

Quando l'emittente del Certificato X.509 è la Foglia e quindi il Certificato X.509 si riferisce a se stesso, se il tempo di scadenza del certificato è superiore a 24 ore dal tempo ``X509_NOT_VALID_BEFORE``, DEVE implementare una CRL relativa al certificato emesso e mantenerla aggiornata.
Quando l'emittente del Certificato X.509 è un Superiore immediato, come il Trust Anchor o un Intermediario, e revoca il certificato relativo alla Foglia, cioè il Certificato X.509 relativo a una delle Chiavi dell'Entità di Federazione della Foglia, questa azione invalida l'intera Trust Chain associata a quella chiave pubblica crittografica della Foglia, rimuovendo effettivamente la sua capacità di emettere ulteriori Certificati X.509 su se stessa. Questo meccanismo di revoca gerarchico garantisce che qualsiasi compromissione o comportamento scorretto da parte di un'entità Foglia possa essere rapidamente affrontato.

Di seguito è riportato un esempio non normativo, in testo semplice, che illustra il contenuto di una CRL.

.. code-block:: text

    Certificate Revocation List (CRL):
    Version: 2 (0x1)
    Signature Algorithm: sha256WithRSAEncryption
    Issuer: CN=leaf.example.org, O=Leaf, C=IT
    Last Update: Sep 1 00:00:00 2023 GMT
    Next Update: Sep 8 00:00:00 2023 GMT
    Revoked Certificates:
        Serial Number: 987654320
            Revocation Date: Aug 25 12:00:00 2023 GMT
            CRL Entry Extensions:
                Reason Code: Key Compromise
        Serial Number: 987654321
            Revocation Date: Aug 30 15:00:00 2023 GMT
            CRL Entry Extensions:
                Reason Code: Cessation of Operation
    Signature Algorithm: sha256WithRSAEncryption
    Signature:
        5c:4f:3b:...

Federation Subordinate Events Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'Endpoint Eventi Subordinati della Federazione è definito in `OID-FED-SUBORDINATE-EVENTS`_. Questo endpoint fornisce un meccanismo per Trust Anchor e Intermediari per pubblicare eventi storici relativi ai loro Subordinati Immediati. Fornisce trasparenza e responsabilità all'interno della federazione fornendo un record storico completo di eventi significativi che influenzano i partecipanti della federazione.

Per i dettagli completi della specifica, inclusi la posizione dell'endpoint, il formato della richiesta, il formato della risposta, i claim JWT, i parametri degli oggetti evento e i tipi di evento supportati, fare riferimento a `OID-FED-SUBORDINATE-EVENTS`_.

Di seguito è riportato un esempio non normativo di una richiesta e risposta dell'Endpoint Eventi Subordinati della Federazione:

**Esempio di Richiesta**:

.. code-block:: http

   GET /federation_subordinate_events_endpoint?sub=https%3A%2F%2Frp%2Eexample%2Eorg HTTP/1.1
   Host: immediate-superior.example.org

**Esempio di Risposta**:

.. code-block:: json

   {
     "iss": "https://immediate-superior.example.org",
     "sub": "https://rp.example.org",
     "iat": 1590000000,
     "federation_registration_events": [
       {
         "iat": 1590000000,
         "event": "registration"
       },
       {
         "iat": 1590000000,
         "event": "jwks_update"
       },
       {
         "iat": 1600000000,
         "event": "revocation",
         "event_description": "compromised node"
       },
       {
         "iat": 1610000000,
         "event": "registration"
       }
     ]
   }

**Integrazione con la Gestione del Ciclo di Vita delle Entità**:

Questo endpoint completa le procedure di gestione del ciclo di vita delle entità definite in :ref:`entity-onboarding:Onboarding delle Entità` fornendo un tracciamento dettagliato di tutti gli eventi significativi che influenzano i partecipanti della federazione. Supporta sia il monitoraggio automatizzato della conformità che i processi di audit manuale.

Osservazioni sulla Privacy
--------------------------

- Le Istanze del Wallet NON DEVONO pubblicare i loro metadati attraverso un servizio online.
- L'infrastruttura di trust DEVE essere pubblica, con tutti gli endpoint pubblicamente accessibili senza alcuna credenziale client che possa rivelare chi sta richiedendo l'accesso.
- Quando un'Istanza del Wallet richiede i Subordinate Statement per costruire la Trust Chain per un Relying Party specifico o valida un Trust Mark online, emesso per un Relying Party specifico, il Trust Anchor o il suo Intermediario non sanno che una particolare Istanza del Wallet sta indagando su un Relying Party specifico; invece, servono solo le dichiarazioni relative a quel Relying Party come risorsa pubblica.
- I metadati dell'Istanza del Wallet NON DEVONO contenere informazioni che possano rivelare informazioni tecniche sull'hardware utilizzato.
- I metadati dell'entità Foglia, Intermediario e Trust Anchor possono includere la quantità necessaria di dati come parte delle informazioni di contatto amministrative, tecniche e di sicurezza. Generalmente non è raccomandato utilizzare dettagli di contatto personali in tali casi. Dal punto di vista legale, la pubblicazione di tali informazioni è necessaria per il supporto operativo riguardante questioni tecniche e di sicurezza e la regolamentazione GDPR.


Considerazioni sulla Decentralizzazione
---------------------------------------

- Ci può essere più di un singolo Trust Anchor.
- In alcuni casi, un verificatore di trust può fidarsi di un Intermediario, specialmente quando l'Intermediario agisce come Trust Anchor all'interno di un perimetro specifico, come casi dove le Foglie sono entrambe nello stesso perimetro come una giurisdizione di Stato Membro (ad esempio: un Relying Party italiano con un'Istanza del Wallet italiana può considerare l'Intermediario italiano come Trust Anchor per gli scopi delle loro interazioni).
- Le attestazioni di trust (Trust Chain) dovrebbero essere incluse nei JWT emessi dai Credential Issuer, e le Richieste di Presentazione degli RP dovrebbero contenere la Trust Chain relativa a loro (emittenti delle richieste di presentazione).
- Poiché la presentazione delle credenziali deve essere firmata, memorizzando le richieste e risposte di presentazione firmate, che includono la Trust Chain, l'Istanza del Wallet può avere lo snapshot della configurazione di federazione (Entity Configuration del Trust Anchor nella Trust Chain) e l'affidabilità verificabile del Relying Party con cui ha interagito.
- Ogni attestazione firmata è di lunga durata poiché può essere validata crittograficamente anche quando la configurazione di federazione cambia o le chiavi dei suoi emittenti sono rinnovate.
- Ogni partecipante dovrebbe essere in grado di aggiornare la sua Entity Configuration senza notificare i cambiamenti a qualsiasi terza parte. La policy dei metadati contenuta all'interno di una Trust Chain deve essere applicata per sovrascrivere qualsiasi informazione relativa ai metadati specifici del protocollo.


