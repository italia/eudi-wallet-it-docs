.. include:: ../common/common_definitions.rst


Definizioni e Acronimi
=======================

Questa sezione mira ad uniformare la terminologia del Sistema IT-Wallet alle definizioni fornite in ARF 2.7.3 (vedere `ARF Annex 1 <https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/annexes/annex-1/annex-1-definitions.md>`_). Per ciascun termine, la definizione di IT-Wallet è stata confrontata e mappata con quella di ARF, includendo note su eventuali differenze o chiarimenti.

Le definizioni di *Utente*, *Servizio Fiduciario*, *Trust Model*, *Trusted List*, *Trust Framework*, *Attributo*, *Fornitore di Attestati Elettronici di Attributi* o *Fornitore di servizi fiduciari (TSP)*, *Person Identification Data (PID)*, *Lista di Revoca*, *Fornitore di Attestati Elettronici di Attributi qualificati* o *Fornitore di servizi fiduciari qualificati (QTSP)*, *Attestato Elettronico di Attributi (EAA)*, sono definite nel documento `EIDAS-ARF`_.

Di seguito le descrizioni di acronimi e definizioni, correlati al presente documento utili ad approfondimenti su tematiche inerenti l' IT-Wallet e i componenti con i quali interagisce.

.. glossary::
    :sorted:

    **Dataset_id**
      Stringa alfanumerica definita dalla Fonte Autentica e che identifica univocamente uno specifico dataset relativo a un Attestato Elettronico di Attributi.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Object_id**
      Stringa alfanumerica definita dalla Fonte Autentica e che identifica univocamente una specifica istanza di Attestato Elettronico di Attributi associata a un determinato Utente.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Processo di Accreditamento**
      Procedura svolta dall'Ente di Accreditamento Nazionale per accreditare gli Organismi di Valutazione della conformità (CABs), che si conclude con il rilascio di un certificato di accreditamento.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Attributi**
    **Attributi dell'Utente**
      Un insieme di caratteristiche, qualità, diritti o autorizzazioni di una persona fisica o giuridica o di un oggetto o anche una sola di queste informazioni.
      Conforme con ARF 2.7.3.

    **Autenticazione**
      Processo elettronico che consente di confermare l'Identificazione di una persona fisica o giuridica, oppure l'origine/integrità dei dati.
      Conforme con ARF 2.7.3.

    **Fonte Autentica**
      Soggetto pubblico o privato responsabile di un archivio o sistema che è considerato fonte primaria per gli Attributi o per i Dati di Identificazione Personale.
      Conforme con ARF 2.7.3.

    **Processo di Certificazione**
      Procedura svolta dagli Organismi di Valutazione della conformità (CABs) per certificare le Soluzioni Wallet, che comprende anche le valutazioni tecniche periodiche.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Organismo di Valutazione della Conformità**
      Organismo accreditato valuta e certifica le Soluzioni di Portafogli o i Fornitori di Servizi Fiduciari.
      Conforme con ARF 2.7.3.

    **Fornitore di Attestati Elettronici**
    **Credential Issuer**
      Soggetto pubblico o privato che fornisce Attestati Elettronici agli Utenti (può essere un fornitore di PID oppure un fornitore di (Q)EAA).
      Conforme con ARF 2.7.3; IT-Wallet aggrega sotto questo termine sia il fornitore di PID che di (Q)EAA.

    **Asset Critici**
      Asset (ad esempio, le chiavi crittografiche) la cui perdita avrebbe gravi ripercussioni sull'Istanza del Wallet.
      Conforme con ARF 2.7.3.

    **Cryptographic Hardware Key Tag**
      Identificativo univoco per le Cryptographic Hardware Keys, utilizzato per accedere alla chiave privata dell'hardware.
      Non presente in ARF 2.7.3.

    **Cryptographic Hardware Keys**
      Coppia di chiavi generata dall'Istanza del Wallet, valida per tutta la sua durata.
      Non presente in ARF 2.7.3.

    **Servizio di Integrità del Dispositivo**
      Servizio fornito dai produttori di dispositivi per verificare l'integrità delle app e l'archiviazione sicura delle chiavi.
      Non presente in ARF 2.7.3.

    **Attestato Elettronico**
    **Attestato**
      Un set firmato di Attributi in un formato specifico (ad esempio mDoc-CBOR, SD-JWT VC), può essere un PID oppure una (Q)EAA.
      Conforme con ARF 2.7.3.

    **Autorità di Federazione**
      Ente di governance pubblica che emana linee guida, regole e gestisce Elenchi di Fiducia e lo stato dei partecipanti.
      Non presente in ARF 2.7.3.

    **Titolare**
    **Holder**
      Persona fisica o giuridica che riceve, gestisce e presenta Attestati Elettronici tramite l'Istanza del Wallet.
      Simile ad ARF 2.7.3. ARF utilizza questo termine solo nei casi di interazione tra Wallet, mentre negli altri casi utilizza il termine *Holder Wallet Unit*.

    **Associazione Crittografica con l'Utente**
    **Holder Key Binding**
      Capacità del Titolare di dimostrare il possesso della chiave privata attestata da una terza parte di fiducia.
      Non presente in ARF 2.7.3.

    **Identity and Access Management**
      Framework per la gestione delle identità digitali e dell'accesso alle informazioni.
      Non presente in ARF 2.7.3.

    **Sistema IT-Wallet**
      Insieme di Soluzioni Tecniche che implementano il Sistema di Wallet Digitale Italiano.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Registro del Sistema IT-Wallet**
      Registro delle entità partecipanti al Sistema IT-Wallet.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Key Attestation APIs (OEM)**
      Meccanismo di attestazione del produttore del dispositivo che conferma se le chiavi crittografiche sono archiviate in modo sicuro nel Keystore supportato dall'hardware. Esempi includono l'Android Key Attestation API per i dispositivi Android e Apple DeviceCheck per i dispositivi iOS. Queste API sono utilizzate dal Wallet Provider per emettere un Key Attestation per le credenziali non-PID.
      Non presente in ARF 2.7.3; specifico dell'IT-Wallet.

    **Keystore**
      Ambiente di archiviazione sicuro hardware-backed fornito dall'OEM del dispositivo per la generazione, l'archiviazione e l'utilizzo di chiavi crittografiche. Sui dispositivi Android, il Keystore si basa sul Trusted Execution Environment (TEE) o Strongbox; sui dispositivi iOS, si basa sul Secure Enclave. Il Keystore è il meccanismo crittografico di default per tutte le operazioni della Wallet Instance e le Credenziali Digitali, ad eccezione del PID che richiede un WSCA/Remote WSCD. Le proprietà del Keystore sono attestate tramite le OEM Key Attestation APIs. Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Livello di Garanzia**
      Nel quadro dell'Unione per l'**identificazione elettronica**, i **livelli di garanzia** esprimono il grado di fiducia nella **correttezza dell'identificazione** delle persone fisiche o giuridiche e nella possibilità di **fare affidamento sui mezzi di identificazione elettronica**. Per gli **schemi di identificazione elettronica notificati**, `EIDAS`_, come modificato (incluso il Quadro europeo di identità digitale codificato dal `EU_2024_1183`_), definisce i livelli **basso (*low*)**, **sostanziale (*substantial*)** e **alto (*high*)**.
      Nelle presenti Specifiche Tecniche il termine **LoA** si impiega anche per i **requisiti minimi di garanzia** riguardanti l'**autenticazione dell'Utente**, il contesto dell'**Istanza del Wallet** e l'**affidabilità degli Attestati Elettronici** (inclusi i metadati di catalogo come il livello minimo di garanzia), che DEVONO restare coerenti con la normativa dell'Unione, con l'attuazione nazionale degli schemi notificati e con le discipline sui **Portafogli di Identità Digitale Europea** e sui **Person Identification Data (PID)** (ivi incluso, ove pertinente, il Regolamento di esecuzione (UE) 2024/2979 della Commissione).
      Non presente con questa formulazione in ARF 2.7.3; allineato al quadro normativo eIDAS / EUDI Wallet.

    **Metadata**
      Artefatto digitale contenente informazioni su un'entità organizzativa (endpoint, chiavi pubbliche, ecc.).
      Non presente in ARF 2.7.3.

    **Enti Nazionali di Accreditamento**
      Organismi che svolgono l'attività di accreditamento su delega di uno Stato membro.
      Conforme con ARF 2.7.3.

    **Gestore di Identità Digitale**
      Entità organizzativa che fornisce mezzi di identificazione elettronica preesistenti notificati utilizzati per l'autenticazione dell'Utente (ad esempio CieID / SPID), distinta dall'attestato **IT-Wallet ID** detenuto nel Wallet.
      Non presente in ARF 2.7.3.

    **National Trust Anchor**
      Entità organizzativa designata a livello nazionale che agisce come radice di fiducia della federazione, operando la PKI nazionale e pubblicando le Trusted List e i metadati di federazione autorevoli per le entità subordinate (ad esempio Intermediari e Foglie).
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Processo di Notifica**
      Procedura per l'invio delle informazioni alla Commissione Europea e l'inserimento all'interno delle Trusted List.
      Conforme con ARF 2.7.3.

    **Entità Organizzativa**
      Persona giuridica (pubblica o privata) riconosciuta per svolgere un ruolo nell'ecosistema IT-Wallet.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Dati di Identificazione Personale**
    **Person Identification Data**
    **PID**
      Insieme di dati rilasciati in conformità al diritto dell'Unione o nazionale che consentono di stabilire l'identità di una persona fisica o giuridica, o di una persona fisica che rappresenta un'altra persona fisica o giuridica.
      Conforme con ARF 2.7.3 / `EU_2024_1183`_. Nelle presenti Specifiche Tecniche, i riferimenti all'emissione, alla presentazione o alla revoca di un PID denotano il PID tecnico (la struttura dati firmata che contiene i Dati di Identificazione Personale), come utilizzato nell'ARF. Il termine italiano «Attestato Elettronico di Dati di Identificazione Personale», ove impiegato come sinonimo di PID, va inteso in questo senso e **non** come Attestato Elettronico di Attributi (EAA).

    **Fornitore di Attestati Elettronici di Dati di Identificazione Personale**
    **PID Provider**
    **Provider of Person Identification Data**
      Persona fisica o giuridica responsabile dell'emissione e della revoca dei Dati di Identificazione Personale e della garanzia che i Dati di Identificazione Personale di un Utente siano associati crittograficamente a una Wallet Unit.
      Conforme con ARF 2.7.3.

    **Policy Language**
      Linguaggio formale per la definizione di policy di sicurezza, privacy e gestione dell'identità.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Attori Primari**
      Entità che realizzano le Soluzioni Tecniche per il funzionamento del Sistema IT-Wallet.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Pseudonimo**
      Identificativo alternativo anonimo che consente l'autenticazione e l'autorizzazione da parte di un entità.
      Conforme con ARF 2.7.3.

    **Attestato Elettronico di Attributi Qualificati**
      Attestazione verificabile digitalmente emessa da un QTSP, che comprova il possesso di attributi.
      Conforme con ARF 2.7.3.

    **Attestato Elettronico di Attributi**
      Attestato verificabile digitalmente in forma elettronica, comprovante il possesso di attributi.
      Conforme con ARF 2.7.3.

    **Attestato Elettronico di Attributi rilasciato da o per conto di un ente pubblico**
    **Attestato Elettronico Pubblico di Attributi**
      Attestato Elettronico di Attributi che contiene Attributi forniti da una Fonte Autentica pubblica.
      Conforme con ARF 2.7.3.

    **Attestato Elettronico di Interesse Pubblico**
      Attestato Elettronico di Attributi che contiene Attributi destinati ad attestare il rilascio, da parte dello Stato o di altre pubbliche amministrazioni, di autorizzazioni, certificazioni, abilitazioni, documenti di identità e riconoscimento, ricevute di introiti, ovvero ad assumere un valore fiduciario e di tutela della fede pubblica in seguito alla loro emissione o alle scritturazioni su di essi effettuate e, in generale, quando sono considerati carte valori ai sensi dell'articolo 2, comma 10-bis, della legge 13 luglio 1966, n. 559.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **IT-Wallet ID**
    **Attestato Elettronico di Dati di Identificazione Personale di ambito nazionale**
      Attestato Elettronico di Attributi (EAA) che contiene dati di identificazione di una persona fisica ed è rilasciato **esclusivamente per usi nazionali**. I termini **IT-Wallet ID** e **Attestato Elettronico di Dati di Identificazione Personale di ambito nazionale** indicano il medesimo EAA nazionale. La qualificazione «di ambito nazionale» distingue questo EAA dai **Dati di Identificazione Personale (PID)** EUDI, che sono un insieme di dati ai sensi del quadro europeo di Identità Digitale e **non** costituiscono un EAA. Consente l'autenticazione e l'identificazione dell'Utente nei confronti delle Relying Party che operano nell'ambito della giurisdizione nazionale. NON DEVE essere utilizzato per interazioni cross-border e **non** costituisce un PID ai sensi di `EU_2024_1183`_ / `EU_2024/2977`_. NON DEVE essere confuso con il **PID** EUDI, né con un **Gestore di Identità Digitale** / schema di eID nazionale (ad esempio CieID / SPID) utilizzato solo per l'autenticazione. Il termine **EID Nazionale** NON DEVE essere usato come sinonimo di IT-Wallet ID, per evitare confusione con tali schemi. Gli identificatori tecnici (``vct`` e ``credential_type``) sono definiti nella sezione :ref:`credential-data-model-it-wallet-id:Modello di Dati dell'IT-Wallet ID`. Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Fornitore di Attestati Elettronici di Attributi Qualificati**
    **QEAA Provider**
      Entità Organizzativa che fornisce QEAAs.
      Conforme con ARF 2.7.3.

    **Fornitore di Attestati Elettronici di Attributi**
    **EAA Provider**
      Entità Organizzativa che fornisce EAAs.
      Conforme con ARF 2.7.3.

    **Fornitore Qualificato di Firme Elettroniche**
      Fornitore di Servizi Fiduciari che rilascia certificati di Firma Elettronica Qualificata.
      Conforme con ARF 2.7.3.

    **Registration Authority**
    **Registrar**
      Soggetto responsabile della registrazione delle Entità Organizzative mediante l'emissione di Attestati di Fiducia.
      Conforme con ARF 2.7.3.

    **Processo di Registrazione**
      Procedura per la verifica dell'idoneità e della conformità delle Entità Organizzative.
      Conforme con ARF 2.7.3.

    **Fornitore di Servizi**
    **Relying Party**
    **Wallet‑Relying Party**
      Entità che si affida all'identificazione elettronica o al Servizio Fiduciario di un'Istanza del Wallet.
      Conforme con ARF 2.7.3.

    **Soluzione di Relying Party**
      Prodotto (software/hardware/cloud) che consente la presentazione degli Attestati Elettronici in vari contesti.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Backend della Relying Party**
      Infrastruttura remota composta da componenti server gestiti da un fornitore di Soluzioni di Relying Party.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Istanza di Relying Party**
    **App di Verifica**
      Istanza specifica di un'applicazione oppure dispositivo in dotazione ad una Relying Party.
      Conforme con ARF 2.7.3.

    **Divulgazione Selettiva**
      Funzionalità che consente all'Utente di inviare un sottoinsieme di dati contenuti in Attestati Elettronici.
      Conforme con ARF 2.7.3.

    **Self-Sovereign Identity**
      Approccio che concede agli individui di avere il pieno controllo sulle informazioni relative alla propria identità digitale.
      Non presente in ARF 2.7.3.

    **Processo di Supervisione**
      Procedimento svolto da parte di un Organismo di Vigilanza per esaminare e garantire il corretto funzionamento del Fornitore di Wallet e di altre entità.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Signal Hub**
      La piattaforma PDND gestita dal Gestore PDND che abilita la raccolta e distribuzione di Segnali. Consiste di due e-Service PDND: Raccolta Segnali e Distribuzione Segnali.

    **Segnale (Signal Hub)**
      Un segnale digitale propagato attraverso Signal Hub PDND. È utilizzato dalle Fonti Autentiche per notificare ai Fornitore di Attestati Elettronici aggiornamenti su stati e/o informazioni all'interno di un dominio gestito dalla Fonte Autentica stessa.

    **Soluzioni Tecniche**
      Insieme dei sistemi hardware/software e dei servizi realizzati dai Fornitori di Wallet, Fornitori di Attestati Elettronici di Dati di Identificazione Personale, ecc.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Specifiche Tecniche**
      Specifiche che forniscono l'architettura tecnica, il quadro implementativo e i requisiti di progettazione.
      Conforme con ARF 2.7.3.

    **Trust**
      Fiducia nell'affidabilità, sicurezza e integrità delle entità e delle loro azioni.
      Non presente in ARF 2.7.3.

    **Trust Attestation**
      Attestazione elettronica di conformità al quadro normativo, verificabile crittograficamente.
      Non presente in ARF 2.7.3.

    **Trust Evaluation**
      Processo di verifica dell'affidabilità delle Entità Organizzative registrate.
      Non presente in ARF 2.7.3.

    **Trust Framework**
      Insieme di regole e accordi giuridicamente vincolanti per un sistema composto da più attori.
      Non presente in ARF 2.7.3.

    **Trust Layer**
      Componente architetturale che consente ai partecipanti di stabilire un rapporto di fiducia.
      Non presente in ARF 2.7.3.

    **Trust Model**
      Insieme di regole che garantiscono la legittimità dei componenti/entità nell'ecosistema IT-Wallet.
      Non presente in ARF 2.7.3.

    **Relazione di Fiducia**
    **Trust Relationship**
      Affidabilità tra Entità Organizzative verificata in seguito alla Trust Evaluation.
      Non presente in ARF 2.7.3.

    **Certificato di Accesso**
    **Access Certificate**
      Certificato di autenticazione e convalida della Wallet Relying Party.
      Conforme con ARF 2.7.3.

    **Access Certificate Authority**
    **Access CA**
      Autorità di Certificazione responsabile dell'emissione dei Certificati di Accesso a PID Provider, Attestation Provider e Relying Party per interazioni sicure all'interno dell'ecosistema IT-Wallet.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Certificato di Registrazione**
    **Registration Certificate**
      Oggetto che indica gli Attributi che la Relying Party ha registrato al fine di richiederli agli Utenti.
      Conforme con ARF 2.7.3.

    **Fornitore di Certificati di Registrazione**
    **Provider of Registration Certificates**
    **Reg. Cert. Provider**
      Entità Organizzativa responsabile dell'emissione dei Certificati di Registrazione che descrivono lo stato di registrazione e i diritti di PID Provider, Attestation Provider e Relying Party.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Federation Registry**
      Componente di registro dell'Infrastruttura del Registro IT-Wallet che mantiene l'elenco autorevole delle entità fidate che partecipano alla federazione, inclusi i relativi metadati di federazione, gli endpoint e le chiavi pubbliche.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Registro delle Fonti Autentiche**
    **Authentic Source Registry**
    **AS Registry**
      Registro contenente le Fonti Autentiche, le loro capacità dichiarate e i claim disponibili, utilizzato dai Fornitori di Attestati Elettronici per individuare e integrare fornitori di dati autorevoli.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Member State Trusted List Provider**
    **MS TLP**
      Entità Organizzativa designata da uno Stato Membro per compilare, firmare e pubblicare le Trusted List nazionali (es. Trusted List dei QTSP, Trusted List dei Fornitori di EAA) e per notificarne la posizione alla Commissione Europea.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Certificate Signing Request**
      Richiesta inviata a una CA contenente la chiave pubblica e le informazioni identificative utili all'emissione di un certificato digitale.
      Non presente in ARF 2.7.3.

    **Trusted List**
      Archivio di informazioni sugli enti autoritativi e sul loro stato.
      Conforme con ARF 2.7.3.

    **eIDAS Trusted List**
      Archivio di informazioni sulle entità autorevoli e sul loro stato utilizzato nel quadro dei servizi fiduciari eIDAS (es. Trusted List dei PID Provider, Trusted List dei Wallet Provider, List of Trusted List che punta alle Trusted List dei QTSP e dei Fornitori di EAA degli Stati Membri, Trusted List delle CA dei Certificati di Accesso e dei Fornitori di Certificati di Registrazione).
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Utente**
      Persona fisica o giuridica che utilizza servizi fiduciari o mezzi di identificazione elettronica.
      Conforme con ARF 2.7.3.

    **Verificatore di Attestati Elettronici**
    **Verificatore di Credenziali**
      Una persona o entità che utilizza un'Istanza di Relying Party.
      Simile ad ARF 2.7.3. ARF utilizza questo termine solo nei casi di interazione tra Wallet.

    **Istanza del Wallet**
      Applicazione installata sul dispositivo di un Utente, parte di un'Istanza del Wallet, che fornisce interfacce utente.
      Conforme con ARF 2.7.3.

    **Fornitore di Wallet**
      Entità organizzativa responsabile della gestione e della fornitura di una Soluzione Wallet.
      Conforme con ARF 2.7.3.

    **Backend del Fornitore di Wallet**
    **Wallet Provider Backend**
      Infrastruttura tecnica e componenti server gestiti da un Fornitore di Wallet.
      Non presente in ARF 2.7.3.

    **Wallet Secure Cryptographic Application**
      Applicazione che gestisce gli asset critici utilizzando le funzioni crittografiche fornite dal WSCD. In IT-Wallet, il WSCA è usato esclusivamente per l'emissione e la gestione del PID a LoA High, operando all'interno di un Remote WSCD basato su un HSM remoto (remote HSM).
      Conforme con ARF 2.7.3.

    **Wallet Secure Cryptographic Device**
      Dispositivo antimanomissione che fornisce un ambiente in cui la WSCA può proteggere gli asset critici. In IT-Wallet, il WSCD è implementato come Remote WSCD, ovvero un Hardware Security Module (HSM) remoto operato lato server, usato esclusivamente per l'emissione e la gestione del PID a LoA High.
      Conforme con ARF 2.7.3.

    **Soluzione Wallet**
      Insieme di Soluzioni Tecniche al fine di garantire il corretto funzionamento delle Istanze del Wallet.
      Conforme con ARF 2.7.3.

    **Wallet Unit**
      Configurazione univoca di una soluzione Wallet per un singolo utente, comprensiva delle funzionalità di sicurezza.
      Unique configuration of a Wallet Solution for an individual User, including security features.
      Conforme con ARF 2.7.3.

    **Key Attestation**
    **KA**
      Oggetto di dati emesso da un Wallet Provider che dimostra che le chiavi utilizzate per il key binding delle credenziali risiedono in un ambiente sicuro affidabile. Per il PID (LoA High), il Key Attestation descrive le proprietà del WSCA e del Remote WSCD (HSM remoto); per tutte le altre Credenziali Digitali device-bound, il Key Attestation descrive le proprietà del Keystore tramite le OEM Key Attestation APIs.
      Allineato alla Technical Specification 3.

    **Wallet Instance Attestation**
    **Wallet Attestation**
      Oggetto emesso da un Fornitore di Wallet che attesta l'integrità dell'Istanza del Wallet.
      Specifico per l'IT-Wallet.

    **Catalogo degli Attestati Elettronici**
      Catalogo elettronico contenente informazioni relative ai formati e agli schemi degli Attestati Elettronici, ai dati in essi contenuti e alle Fonti Autentiche. Il Catalogo contiene informazioni aggiuntive che consentono di stabilire l'autenticità e l'affidabilità delle informazioni in esso contenute.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.

    **Intermediario**
    **Intermediario di Federazione**
      Entità intermedia come definita nella Sezione 1.2 di `OID-FED`_ nella catena di fiducia OpenID Federation tra Trust Anchor ed entità foglia. Tale ruolo di federazione **non** coincide concettualmente con l'**Intermediario di Relying Party** previsto dal quadro europeo di identità digitale (`EU_2024_1183`_); tuttavia, nel profilo implementativo descritto dalle presenti specifiche tecniche, un **Intermediario di Relying Party** è anche realizzato come Intermediario di Federazione (vedi **Intermediario IT-Wallet**).
      Conforme con ARF 2.7.3 per le strutture di federazione.

    **Intermediario di Relying Party**
    **Soggetto Aggregatore**
      Entità Organizzativa che agisce per conto di una o più Relying Party per fornire Soluzioni Tecniche di collegamento alle Istanze del Wallet e per l'autenticazione dell'Utente o la verifica degli Attestati Elettronici. Nel diritto dell'Unione (`EU_2024_1183`_, articolo 5b, paragrafo 8), gli intermediari che agiscono per conto delle Relying Party sono **considerati Relying Party** ai fini della registrazione e dell'autenticazione verso i Portafogli di identità digitale europea e **non devono conservare dati sul contenuto della transazione** tra l'Utente del Portafoglio e la Relying Party intermediata. I requisiti di alto livello sulla registrazione delle Wallet Relying Party, inclusi gli intermediari, i dati minimi di registrazione, la trasparenza e i meccanismi comuni di autenticazione verso i Portafogli, sono trattati nell'Architecture and Reference Framework del Portafoglio EUDI (`ARF`_; *Topic X – Relying Party registration*, `ARF_TOPIC_X_RP`_). IT-Wallet disciplina l'onboarding nell'infrastruttura di fiducia nazionale, i metadati e i controlli tecnici che attuano tali obblighi insieme alle misure nazionali di esecuzione applicabili.

    **Intermediario IT-Wallet**
      Entità Organizzativa che agisce come **Intermediario di Relying Party** e che è tecnicamente realizzata come Intermediario di Federazione (`OID-FED`_, Sezione 1.2). Pertanto, nel profilo implementativo IT-Wallet, un Intermediario di Relying Party è anche un Intermediario di Federazione: pubblica la propria Entity Configuration, emette Subordinate Statement per le Relying Party affiliate ed emette loro il Trust Mark. Nell'infrastruttura di trust IT-Wallet, è registrato dal Trust Anchor con un ``trust_mark_type`` specifico, che consente all'Istanza del Wallet di identificare e mostrare all'Utente che il Relying Party richiedente opera tramite un Intermediario riconosciuto.
      Non presente in ARF 2.7.3; specifico di IT-Wallet.


.. note::
   Qualora un termine non è presente nell'ARF 2.7.3, la definizione fornita in IT-Wallet è da ritenersi valida per il solo contesto italiano.

Di seguito sono riportati i principali termini e definizioni relativi agli aspetti dell'Esperienza Utente:

.. glossary::
    :sorted:

    **Authentication Button**
      Pulsante che consente all'Utente di avviare il processo di Autenticazione e di utilizzare i servizi forniti dai Verificatori di Attestati Elettronici.

    **Brand Identity**
      Insieme di elementi visivi, verbali e strategici che un servizio, un prodotto o un'entità utilizza per presentarsi all'Utente e per distinguersi dagli altri.

    **Brand Manual**
      Documento che definisce le regole e gli standard per l’utilizzo corretto e coerente degli elementi distintivi di un Brand, inclusi gli aspetti visivi, verbali e applicativi, nei diversi Touchpoint.

    **Catalogo**
      Funzionalità dell'Istanza del Wallet in cui viene visualizzato l'elenco di tutti gli Attestati Elettronici disponibili e ottenibili tramite l'Istanza del Wallet, e dalle quali è possibile avviare il processo di emissione.

    **Call To Action**
      Suggerimento chiaro e diretto che incoraggia gli Utenti a intraprendere un'azione specifica. Può essere un pulsante, un link o un altro elemento che guida l'Utente verso un obiettivo specifico.

    **Vista di Dettaglio**
      Modalità di visualizzazione estesa degli Attestati Elettronici, che mostra tutti gli Attributi contenuti.

    **Discovery Page**
      È la pagina presente nel Touchpoint della Relying Party dove l'Utente atterra per accedere alla propria area autenticata e ha lo scopo di mostrare all'Utente tutti i metodi di Autenticazione disponibili.

    **Engagement Button**
      Elemento interattivo dell'interfaccia che consente all'Utente di avviare un processo (ad esempio per autenticarsi, per richiedere il rilascio di un Attestato Elettronico, ecc.).

    **Modello di Interazione**
      Insieme di caratteristiche che definiscono le modalità con cui l'Utente interagisce con l'Interfaccia di uno o più Touchpoint per completare un'attività o un'operazione e conseguire un determinato scopo.

    **Interfaccia**
      L'insieme degli elementi grafici, tipografici e interattivi attraverso i quali l'Utente interagisce con il/i Touchpoint preposto/i all'erogazione di un prodotto o servizio, nel rispetto di [LG_DESIGN].

    **Vista in Anteprima**
      Modalità di visualizzazione compatta dell'Attestato Elettronico che consente di riconoscerla e distinguerla in un elenco di Attestati Elettronici mediante la presenza di dati o elementi minimi.

    **Selection Page**
      È la pagina presente nel Touchpoint della Relying Party o delle terze parti che supportano un Credential Offer dove l'Utente viene a conoscenza di tutte le Soluzioni Wallet presenti nel Registro del Sistema IT-Wallet e può scegliere con quale proseguire il processo di Autenticazione, presentazione o erogazione.

    **Modello di Servizio**
      Insieme di interazioni tra attori e Touchpoint necessari per l'erogazione e la fruizione del servizio.

    **Touchpoint**
      Punto di contatto (digitale e non) tra l'Utente e il prodotto o servizio.

    **Trust Mark**
      Un elemento grafico che fornisce la prova della partecipazione degli Attori Primari al Sistema IT-Wallet e garantisce quindi il rispetto dei suoi standard.

    **Esperienza Utente**
      L'insieme delle percezioni e delle reazioni delle persone derivanti dall'uso e/o dalle aspettative d'uso di un prodotto, sistema o servizio.
      In linea con la norma ISO 9241-210:2010.

    **Visual Identity**
      Insieme coerente di elementi grafici e tipografici che rappresentano visivamente un prodotto o un servizio e lo rendono distinguibile e riconoscibile.

Acronimi
--------

Di seguito gli acronimi usati più di frequente nel documento:

.. list-table::
  :class: longtable
  :widths: 20 80
  :header-rows: 1

  * - **Acronimo**
    - **Description**
  * - **AAL**
    - Authenticator Assurance Level come definito `<https://csrc.nist.gov/glossary/term/authenticator_assurance_level>`_ (Livello di Garanzia dell'Autenticatore)
  * - **ANPR**
    - Anagrafe Nazionale della Popolazione Residente (Italian National Registry of the Resident Population)
  * - **API**
    - Application Programming Interface. Insieme componenti previsti per semplificare gli scenari di integrazione di uno specifico Sistema.
  * - **ARF HLR**
    - EUDI Wallet Architecture and Reference Framework High Level Requirements
  * - **CAB**
    - Conformity Assessment Body (Organismo di Valutazione della Conformità)
  * - **CIE**
    - Carta di Identità Elettronica
  * - **EAA**
    - Electronic Attestation of Attributes (Attestato Elettronico di Attributi)
  * - **EUMS TL**
    - Lista di Fiducia dello Stato membro dell'Unione europea (Trusted List nazionale ai sensi dell'articolo 22 eIDAS)
  * - **NAB**
    - National Accreditation Body (Ente Nazionale di Accreditamento)
  * - **IAM**
    - Identity and Access Management (Gestione dell'Identità e degli Accessi)
  * - **LoA**
    - Level of Assurance (Livello di Garanzia)
  * - **LOTL**
    - List of Trusted Lists (Elenco delle Liste di Fiducia)
  * - **LoTE**
    - List of Trusted Entities (Elenco delle Entità Affidabili)
  * - **OID4VP**
    - OpenID for Verifiable Presentation
  * - **OJEU**
    - Gazzetta ufficiale dell'Unione europea (Official Journal of the European Union)
  * - **PDND**
    - Piattaforma Digitale Nazionale Dati
  * - **PID**
    - Person Identification Data (Dati di Identificazione Personale)
  * - **PII**
    - Personally Identifiable Information (Informazioni di Identificazione Personale)
  * - **QEAA**
    - Qualified Electronic Attestation of Attributes (Attestato Elettronico di Attributi Qualificati)
  * - **Pub-EAA**
    - Electronic Attestation of Attributes issued by or on behalf of a public sector body (Attestato Elettronico di Attributi rilasciato da o per conto di un ente pubblico)
  * - **SSI**
    - Self Sovereign Identity
  * - **VC**
    - Verifiable Credential
  * - **VP**
    - Verifiable Presentation
  * - **WRPAC**
    - Wallet-Relying Party Access Certificate (Certificato di Accesso della Wallet-Relying Party)
  * - **WRPRC**
    - Wallet-Relying Party Registration Certificate (Certificato di Registrazione della Wallet-Relying Party)
  * - **WSCA**
    - Wallet Secure Cryptographic Application (Applicazione Crittografica Sicura per il Wallet)
  * - **WSCD**
    - Wallet Secure Cryptographic Device (Dispositivo Crittografico Sicuro per il Wallet)

Linguaggio Normativo e Convenzioni
==================================

Conformemente agli RFC 2119 e 8174 le seguenti parole chiave solamente quando appaiono con tutte le lettere in maiuscolo assumono i significati di seguito riportati:

  - DEVE/DEVONO: indicano un requisito che è necessario soddisfare.
  - NON DEVE/NON DEVONO: indicano un divieto assoluto.
  - PUÒ/POSSONO: indicano un requisito opzionale, ovvero si può scegliere di soddisfarlo o meno senza alcun tipo di implicazione.
  - DOVREBBE/DOVREBBERO/RACCOMANDATO: indicano un requisito consigliato/raccomandato, ovvero si devono tenere in considerazione tutte le implicazioni derivanti da una eventuale scelta alternativa.
  - NON DOVREBBE/NON DOVREBBERO/NON RACCOMANDATO: indicano un requisito che non è consigliato/raccomandato, ovvero si devono tenere in considerazione tutte le implicazioni derivanti dalla eventuale scelta di applicare comunque il requisito.
  - OBBLIGATORIO: necessario
  - OPZIONALE: facoltativo


