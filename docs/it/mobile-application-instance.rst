.. include:: ../common/common_definitions.rst


Istanza dell'Applicazione Mobile
================================

Le Istanze del Wallet e delle Relying Party Mobili condividono significative somiglianze, in particolare rispetto ad alcuni aspetti relativi all'inizializzazione e alla validazione dell'integrità. Per eliminare la ridondanza, questa sezione utilizzerà il termine **Istanza dell'Applicazione Mobile** per riferirsi collettivamente a entrambe. All'interno di questo framework, il **Fornitore dell'Applicazione** assume le responsabilità del Fornitore di Wallet o del Backend della Relying Party, a seconda del contesto.


Inizializzazione dell'Istanza dell'Applicazione Mobile
------------------------------------------------------

Il flusso di Inizializzazione consente all'Istanza dell'Applicazione Mobile di registrare una coppia di chiavi a lunga durata, memorizzata in modo sicuro in un'appropriata memoria sicura all'interno del dispositivo, con il Fornitore dell'Applicazione. Questo processo avviene solo dopo che il Fornitore dell'Applicazione verifica la sicurezza e la Key Attestation emessa dal produttore del sistema operativo.

Il flusso è mostrato in :ref:`fig_MobileApplication_Instance_Initialization_Flow`, mentre una descrizione passo-passo è fornita di seguito.

.. _fig_MobileApplication_Instance_Initialization_Flow:
.. plantuml:: plantuml/mobile-app-initialization.puml
    :width: 80%
    :alt: La figura illustra il Diagramma di Sequenza dell'Inizializzazione dell'Istanza dell'Applicazione Mobile.
    :caption: `Diagramma di Sequenza dell'Inizializzazione dell'Istanza dell'Applicazione Mobile. <https://www.plantuml.com/plantuml/svg/VLFBRjiw4DtpAmQyYvi0xWy4Q94qYpPe2mJfOnN0695ZQM29L3b3j-xNbvHToBQ2R0XuT1vd7huLnQHvw0rcZI4F3INJiIVOnAXD_6tC_uy5mOv732e6dSO4zhjGie02MGfXd15WlyI6UuAxSUpPeN8Cy114CJYQ63YESCxuH7kuKoNH0_pkyK4EK5I1_sHC7Des4OLptgd5OuexzfJWFRej1J_n6xSrfYPyywwuti1dpC5re1q1pjpQ4-zGfw8nvJd2xpjoM-3DHF2qOqSm4AbCXO433ta08PSJwnuI_SoSQA2WyXmm-4fzgJV0H80xv1wRdewE9UiDF1M90WLhGwppidEsgPVo794VA52gzHawVJr6dwkUpYJczcQ9-xGVDRO9nuuTVCJaVs6Y6brWH4vmPMrthAwtj5-FkR5s1PVLn3jhhm-jYyRqcZ9ymtQXgzWMWNyPKQKsudgce6kFYkiEfOEtuBabqQkfnHLSIgpWCkprwI2hhZ7rFNgSph8IS5wNjS-XYJbuq0YJtO4vZtb10EFft6lUxxoMrP9QYyjvl782Fx1dlpY1vTUbqIdkQrtKYyQhvx3S-yMTrKq-KSkYQT8kFsICGSXS7fwdnT-iY6IXT0CFWPLBtZy73SdEaSWcz-QMWiz3_nS0>`_


.. .. figure:: ../../images/application_instance_initialization.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/VLFBRjiw4DtpAmQyYvi0xWy4Q94qYpPe2mJfOnN0695ZQM29L3b3j-xNbvHToBQ2R0XuT1vd7huLnQHvw0rcZI4F3INJiIVOnAXD_6tC_uy5mOv732e6dSO4zhjGie02MGfXd15WlyI6UuAxSUpPeN8Cy114CJYQ63YESCxuH7kuKoNH0_pkyK4EK5I1_sHC7Des4OLptgd5OuexzfJWFRej1J_n6xSrfYPyywwuti1dpC5re1q1pjpQ4-zGfw8nvJd2xpjoM-3DHF2qOqSm4AbCXO433ta08PSJwnuI_SoSQA2WyXmm-4fzgJV0H80xv1wRdewE9UiDF1M90WLhGwppidEsgPVo794VA52gzHawVJr6dwkUpYJczcQ9-xGVDRO9nuuTVCJaVs6Y6brWH4vmPMrthAwtj5-FkR5s1PVLn3jhhm-jYyRqcZ9ymtQXgzWMWNyPKQKsudgce6kFYkiEfOEtuBabqQkfnHLSIgpWCkprwI2hhZ7rFNgSph8IS5wNjS-XYJbuq0YJtO4vZtb10EFft6lUxxoMrP9QYyjvl782Fx1dlpY1vTUbqIdkQrtKYyQhvx3S-yMTrKq-KSkYQT8kFsICGSXS7fwdnT-iY6IXT0CFWPLBtZy73SdEaSWcz-QMWiz3_nS0

..     Mobile Application Instance Initialization Sequence Diagram


**Passo 1**: L'Utente avvia l'Istanza dell'Applicazione Mobile per la prima volta.

**Passo 2**: L'Istanza dell'Applicazione Mobile:

  * Verifica se il dispositivo soddisfa i requisiti minimi di sicurezza (:ref:`WP_021 <wallet-instance-testcases>`).
  * Verifica se le API di Key Attestation sono disponibili (:ref:`WP_022 <wallet-instance-testcases>`).

.. note::
  **Controllo della Federazione**: L'Istanza dell'Applicazione Mobile deve verificare se il Fornitore dell'Applicazione fa parte della Federazione, ottenendo i suoi Metadati specifici del protocollo (:ref:`WP_023 <wallet-instance-testcases>`). Esempi non normativi di una risposta dall'endpoint :ref:`wallet-provider-endpoint:Endpoint di Federazione` con la **Entity Configuration** e i **Metadati** del Fornitore dell'Applicazione sono presentati nelle sezioni :ref:`wallet-provider-entity-configuration:Entity Configuration del Fornitore di Wallet` e :ref:`relying-party-entity-configuration:Entity Configuration Relying Party`.

**Passi 3-5 (Recupero del Nonce)**: L'Istanza dell'Applicazione Mobile richiede un ``nonce`` monouso dall'**Endpoint Nonce** del Backend del Fornitore dell'Applicazione (vedi :ref:`wallet-provider-endpoint:Endpoint Nonce della Soluzione Wallet` o :ref:`relying-party-provider-backend-endpoint:Endpoint Nonce della Relying Party`). Questo ``nonce`` DEVE essere imprevedibile per servire come principale difesa contro gli attacchi di replay (:ref:`WP_131 <wallet-instance-optional-testcases>`).

In caso di richiesta riuscita, il Fornitore dell'Applicazione genera e restituisce il valore ``nonce`` all'Istanza dell'Applicazione Mobile, come parte della :ref:`mobile-application-instance:Risposta di Nonce dell'Applicazione Mobile`. Il Fornitore dell'Applicazione DEVE garantire che sia monouso e valido solo entro un periodo di tempo specifico.

**Passo 6**: L'Istanza dell'Applicazione Mobile, attraverso il sistema operativo, crea una coppia di Cryptographic Hardware Keys e memorizza il corrispondente Cryptographic Hardware Key Tag nell'archivio locale una volta soddisfatti i seguenti requisiti (:ref:`WP_132 <wallet-instance-optional-testcases>`):

  1. DEVE assicurarsi che le Cryptographic Hardware Keys non esistano già. Se esistono e l'Istanza dell'Applicazione è nella fase di inizializzazione, DEVONO essere eliminate.
  2. DEVE generare una coppia di chiavi asimmetriche a Curva Ellittica (``hardware_key_pub``, ``hardware_key_priv``) tramite un **Keystore**.
  3. DOVREBBE ottenere un identificatore univoco Cryptographic Hardware Key Tag (``hardware_key_tag``) per le Cryptographic Hardware Keys generate dal sistema operativo. Se il sistema operativo consente di specificare un tag durante la creazione delle chiavi, allora DEVE essere selezionata una stringa casuale per l'``hardware_key_tag``. Questo valore casuale DEVE essere resistente alle collisioni e imprevedibile per garantire la sicurezza. Per raggiungere questo obiettivo, considerare l'utilizzo di una funzione di hash crittografico o un generatore di numeri casuali sicuro fornito dal sistema operativo o da una libreria crittografica affidabile.
  4. Se i punti precedenti sono soddisfatti, DEVE memorizzare l'``hardware_key_tag`` nell'archivio locale.

.. note::
  **Keystore**: L'Istanza dell'Applicazione Mobile utilizza il Keystore per operazioni crittografiche, inclusa la generazione di chiavi, l'archiviazione sicura e l'elaborazione crittografica, su dispositivi che supportano questa funzionalità. Sui dispositivi Android, Strongbox è RACCOMANDATO; Trusted Execution Environment (TEE) PUÒ essere utilizzato solo quando Strongbox non è disponibile. Per i dispositivi iOS, Secure Enclave DEVE essere utilizzato. Dato che ogni OEM offre un SDK distinto per accedere al Keystore, la discussione di seguito affronterà questo argomento in un contesto generale.

  Se il Keystore fallisce durante una qualsiasi di queste operazioni, ad esempio a causa di limitazioni hardware, solleverà una risposta di errore all'Istanza dell'Applicazione Mobile. L'Istanza dell'Applicazione Mobile DEVE gestire questi errori di conseguenza per garantire un funzionamento sicuro. I dettagli sulla gestione degli errori sono lasciati all'implementazione dell'Istanza dell'Applicazione Mobile.

.. note::
  **WSCA/Remote WSCD**: Per l'emissione del PID a LoA High, la Wallet Instance interagisce con un WSCA operante in un Remote WSCD basato su un HSM remoto lato server. Questo fornisce un livello di certificazione superiore rispetto al Keystore locale, soddisfacendo i requisiti per LoA High come definito da eIDAS 2.0.

**Passo 7**: L'Istanza dell'Applicazione Mobile utilizza le API di Key Attestation, fornendo il ``client_data_hash`` per acquisire la Key Attestation (:ref:`WP_133b <wallet-instance-optional-testcases>`).

.. note::
  **API di Key Attestation**: In questa sezione, si presume che le API di Key Attestation siano fornite dai produttori di dispositivi. Questo servizio consente la verifica di una chiave memorizzata in modo sicuro all'interno dell'hardware del dispositivo attraverso un oggetto firmato. Inoltre, offre una prova verificabile che una specifica Istanza dell'Applicazione Mobile sia autentica, inalterata e nel suo stato originale utilizzando un documento firmato specializzato creato per questo scopo.

  Il servizio incorpora anche dettagli nell'oggetto firmato, come il tipo di dispositivo, il modello, la versione dell'app, la versione del sistema operativo, lo stato del bootloader e altre informazioni rilevanti per valutare se il dispositivo è stato compromesso. Inoltre, i dispositivi Android possono possedere l'*API di Key Attestation*, una funzionalità supportata da *StrongBox Keymaster* (un HSM fisico installato direttamente sulla scheda madre) o dal *TEE* (Trusted Execution Environment, un'area sicura del processore principale). *Key Attestation* mira a fornire un modo per determinare con certezza se una coppia di chiavi è supportata dall'hardware, quali sono le proprietà della chiave e quali vincoli sono applicati al suo utilizzo. Per i dispositivi Apple, l'API di Key Attestation è rappresentata da *DeviceCheck*, che fornisce un framework e un'interfaccia server per gestire i dati specifici del dispositivo in modo sicuro. *DeviceCheck* viene utilizzato in combinazione con il *Secure Enclave*, un HSM dedicato integrato nei SoC di Apple. *DeviceCheck* può essere utilizzato per attestare l'integrità del dispositivo, delle app e/o delle chiavi di crittografia generate sul dispositivo, garantendo che siano state create in un ambiente sicuro come *Secure Enclave*. Gli sviluppatori possono sfruttare la funzionalità di *DeviceCheck* utilizzando il framework stesso.
  Questi servizi, sviluppati specificamente dal produttore, sono integrati negli SDK Android o iOS, eliminando la necessità di un endpoint predefinito per accedervi. Inoltre, poiché sono sviluppati specificamente per l'architettura mobile, non hanno bisogno di essere registrati come Entità di Federazione attraverso i sistemi di registrazione nazionali.
  *Secure Enclave* è disponibile sui dispositivi Apple dall'iPhone 5s (2013).
  Per i dispositivi Android, l'inclusione di **Strongbox Keymaster** può variare a seconda del produttore, che decide se includerlo o meno.

Se si verificano errori nel processo delle API di Key Attestation, come la verifica dell'integrità del dispositivo, ad esempio, a causa di API di Key Attestation non disponibili, un errore interno o un nonce non valido nella richiesta di integrità, le API di Key Attestation sollevano una risposta di errore. L'Istanza dell'Applicazione Mobile DEVE elaborare questi errori di conseguenza. I dettagli sulla gestione degli errori sono lasciati all'implementazione dell'Istanza dell'Applicazione Mobile.


**Passo 8**: Le API di Key Attestation eseguono le seguenti azioni:

* Creano una Key Attestation che è collegata con il ``client_data_hash`` fornito e la chiave pubblica dell'Hardware dell'Istanza dell'Applicazione.
* Incorporano informazioni relative alla sicurezza del dispositivo.
* Utilizzano una chiave privata OEM per firmare la Key Attestation, quindi verificabile con il relativo certificato OEM, confermando che le Cryptographic Hardware Keys sono gestite in modo sicuro dal sistema operativo.

**Passo 9 (Richiesta di Inizializzazione dell'Istanza dell'Applicazione Mobile)**: L'Istanza dell'Applicazione Mobile invia una :ref:`mobile-application-instance:Richiesta di Inizializzazione dell'Istanza dell'Applicazione Mobile` al Fornitore dell'Applicazione, per inizializzare l'Istanza dell'Applicazione Mobile, identificata dalla chiave pubblica Cryptographic Hardware. Il corpo della richiesta include i seguenti attributi: il ``nonce``, la Key Attestation (``key_attestation``) e il Cryptographic Hardware Key Tag (``hardware_key_tag``) (:ref:`WP_133 <wallet-instance-optional-testcases>`).

.. note::
  Non è necessario inviare la chiave pubblica dell'Hardware dell'Istanza dell'Applicazione perché è già inclusa nella ``key_attestation``.
  Come visto nei passaggi precedenti, le API di Key Attestation creano una Key Attestation collegata al ``client_data_hash`` fornito, che è il digest del ``nonce`` del Fornitore dell'Applicazione, la chiave pubblica dell'Hardware dell'Istanza dell'Applicazione e il suo Hardware Key Tag (:ref:`WP_133a <wallet-instance-optional-testcases>`).
  Questo processo elimina la necessità di inviare direttamente la chiave pubblica dell'Hardware dell'Istanza dell'Applicazione, poiché è già inclusa nella Key Attestation.

**Passi 10-12 (Risposta di Inizializzazione dell'Istanza dell'Applicazione Mobile)**: Il Fornitore dell'Applicazione convalida il ``nonce`` e la firma ``key_attestation``, quindi (:ref:`WP_135–137 <wallet-instance-optional-testcases>`):

  1. DEVE verificare che il ``nonce`` sia stato generato dal Fornitore dell'Applicazione e non sia già stato utilizzato (:ref:`WP_135a <wallet-instance-optional-testcases>`).
  2. DEVE convalidare la ``key_attestation`` come definito dalle linee guida dei produttori di dispositivi (:ref:`WP_135b <wallet-instance-optional-testcases>`). Il Fornitore dell'Applicazione DEVE anche verificare il legame tra l'``hardware_key_tag`` ricevuto, l'``hardware_key_pub`` e il ``nonce`` con il ``client_data_hash`` fornito nella Key Attestation (:ref:`WP_136 <wallet-instance-optional-testcases>`).
  3. DEVE verificare che il dispositivo in uso non abbia difetti di sicurezza e rifletta i requisiti minimi di sicurezza definiti dal Fornitore dell'Applicazione (:ref:`WP_135b <wallet-instance-optional-testcases>`).
  4. Se questi controlli sono superati, DEVE registrare l'Istanza dell'Applicazione Mobile, conservando il Cryptographic Hardware Key Tag (``hardware_key_tag``), la Public Hardware Key (``hardware_key_pub``) e possibilmente altre informazioni utili relative al dispositivo (:ref:`WP_137 <wallet-instance-optional-testcases>`).

In caso di inizializzazione riuscita dell'Istanza dell'Applicazione Mobile, il Fornitore dell'Applicazione risponde con una conferma di successo (:ref:`mobile-application-instance:Risposta di Inizializzazione dell'Istanza dell'Applicazione Mobile`, :ref:`WP_135 <wallet-instance-optional-testcases>`).

.. note::
  Il Fornitore dell'Applicazione potrebbe associare l'Istanza dell'Applicazione Mobile (attraverso l'identificatore ``hardware_key_tag``) a un Utente o Dispositivo specifico (:ref:`WP_138 <wallet-instance-optional-testcases>`). Questo identifica in modo univoco l'Utente/Dispositivo all'interno dei sistemi del Fornitore dell'Applicazione e può essere utilizzato per future revoche nel ciclo di vita dell'Istanza dell'Applicazione Mobile.

**Passi 13-14**: L'Istanza dell'Applicazione Mobile è stata inizializzata.

.. note::
  **Modello di Minaccia**: mentre l'endpoint di inizializzazione non necessita di autenticare il client, è protetto attraverso l'uso di `key_attestation`. La corretta validazione di questa attestazione permette l'inizializzazione di istanze di app autentiche e inalterate. Qualsiasi altro attributo inviato non sarà sottoposto a validazione, portando l'endpoint a rispondere con un errore. Inoltre, l'inclusione di un nonce aiuta a prevenire gli attacchi di replay. L'autenticità sia del nonce che dell'``hardware_key_tag`` è garantita dalla firma trovata all'interno della ``key_attestation``.

Richiesta di Nonce dell'Applicazione Mobile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La Richiesta di Nonce utilizza il metodo HTTP GET.

Di seguito è riportato un esempio non normativo di una Richiesta di Nonce.

.. code-block:: http

    GET /nonce HTTP/1.1
    Host: application-provider.example.com

Risposta di Nonce dell'Applicazione Mobile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In caso di richiesta riuscita, il Fornitore dell'Applicazione restituisce una Risposta HTTP con un codice di stato ``200 OK``, con ``Content-Type`` impostato su ``application/json``.

Il corpo della Risposta di Nonce contiene il valore ``nonce``.

Di seguito è riportato un esempio non normativo di una Risposta di Nonce.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "nonce": "d2JhY2NhbG91cmVqdWFuZGFt"
    }

Risposta di Errore di Nonce dell'Applicazione Mobile
""""""""""""""""""""""""""""""""""""""""""""""""""""

Se si verificano errori, il Fornitore dell'Applicazione restituisce una risposta di errore. La risposta utilizza ``application/json`` come ``Content-Type`` e include i seguenti parametri:

  - *error*. Il codice di errore.
  - *error_description*. Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.

Di seguito è riportato un esempio non normativo di una Risposta di Errore di Nonce.

.. code-block:: http

    HTTP/1.1 500 Internal Server Error
    Content-Type: application/json

    {
        "error": "server_error",
        "error_description": "The server encountered an unexpected error."
    }

La seguente tabella elenca i Codici di Stato HTTP e i relativi codici di errore supportati per la risposta di errore:

.. list-table::
    :class: longtable
    :widths: 30 20 50
    :header-rows: 1

    * - **Codice di Stato HTTP**
      - **Codice di Errore**
      - **Descrizione**
    * - ``500 Internal Server Error``
      - ``server_error``
      - La richiesta non può essere soddisfatta perché l'Endpoint Nonce ha riscontrato un problema interno.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - La richiesta non può essere soddisfatta perché l'Endpoint Nonce è temporaneamente non disponibile (ad esempio, a causa di manutenzione o sovraccarico).

Richiesta di Inizializzazione dell'Istanza dell'Applicazione Mobile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La Richiesta di Inizializzazione dell'Istanza utilizza il metodo HTTP POST con ``Content-Type`` impostato su ``application/json``.

Il corpo della Richiesta di Inizializzazione dell'Istanza contiene i seguenti attributi:


.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Attributo**
      - **Descrizione**
      - **Riferimento**
    * - **nonce**
      - DEVE essere impostato sul valore ottenuto dal Fornitore dell'Applicazione attraverso l'Endpoint Nonce.
      - Questa specifica.
    * - **hardware_key_tag**
      - L'identificatore univoco delle **Cryptographic Hardware Keys** e codificato in ``base64url``.
      - Questa specifica.
    * - **key_attestation**
      - Un'attestazione che garantisce la generazione, l'archiviazione e l'utilizzo sicuri della coppia di chiavi generata dall'Istanza dell'Applicazione Mobile. Questo può essere un array contenente una catena di certificati il cui certificato foglia è la Key Attestation ottenuta dalle **API di Key Attestation** del dispositivo, firmata con la chiave hardware del dispositivo.
      - Questa specifica.

Di seguito è riportato un esempio non normativo di una Richiesta di Inizializzazione dell'Istanza.

.. code-block:: http

    POST /instance-initialization HTTP/1.1
    Host: application-provider.example.com
    Content-Type: application/json

    {
      "nonce": "d2JhY2NhbG91cmVqdWFuZGFt",
      "key_attestation": "o2NmbXRvYXBwbGUtYXBw... redacted",
      "hardware_key_tag": "WQhyDymFKsP95iFqpzdEDWW4l7aVna2Fn4JCeWHYtbU="
    }


Risposta di Inizializzazione dell'Istanza dell'Applicazione Mobile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Se una Richiesta di Inizializzazione dell'Istanza viene convalidata con successo, il Fornitore dell'Applicazione fornisce una Risposta HTTP con codice di stato ``204 No Content``.

Di seguito è riportato un esempio non normativo di una Risposta di Inizializzazione dell'Istanza.

.. code-block:: http

    HTTP/1.1 204 No content


Risposta di Errore di Inizializzazione dell'Istanza dell'Applicazione Mobile
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Se si verificano errori, il Fornitore dell'Applicazione restituisce una risposta di errore. La risposta utilizza ``application/json`` come ``Content-Type`` e include i seguenti parametri:

  - *error*. Il codice di errore.
  - *error_description*. Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato (:ref:`WP_035 <wallet-instance-testcases>`).

Di seguito è riportato un esempio non normativo di una Risposta di Errore di Inizializzazione dell'Istanza.

.. code-block:: http

    HTTP/1.1 403 Forbidden
    Content-Type: application/json
    Cache-Control: no-store

    {
        "error": "forbidden",
        "error_description": "The provided nonce is invalid, expired, or already used. "
    }

La seguente tabella elenca i Codici di Stato HTTP e i relativi codici di errore supportati per la risposta di errore (:ref:`WP_036–040 <wallet-instance-testcases>`):

.. list-table::
    :class: longtable
    :widths: 20 20 50
    :header-rows: 1

    * - **Codice di Stato HTTP**
      - **Codice di Errore**
      - **Descrizione**
    * - ``400 Bad Request``
      - ``bad_request``
      - La richiesta è malformata, mancano parametri richiesti o include parametri non validi e sconosciuti.
    * - ``403 Forbidden``
      - ``integrity_check_error``
      - Il dispositivo non soddisfa i requisiti minimi di sicurezza del Fornitore dell'Applicazione.
    * - ``403 Forbidden``
      - ``invalid_request``
      - Il nonce fornito non è valido, è scaduto o è già stato utilizzato.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La firma della Key Attestation non è valida.
    * - ``422 Unprocessable Content`` [OPZIONALE]
      - ``validation_error``
      - La richiesta non aderisce al formato richiesto.
    * - ``500 Internal Server Error``
      - ``server_error``
      - Si è verificato un errore interno durante l'elaborazione della richiesta.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - Il servizio non è disponibile. Si prega di riprovare più tardi.


.. Associazione Chiave dell'Applicazione Mobile
.. --------------------------------------------

..  Il flusso di Associazione Chiave consente all'Istanza dell'Applicazione Mobile di associare una coppia di chiavi appena creata all'Istanza dell'Applicazione Mobile, basandosi su una prova di possesso delle Cryptographic Hardware Keys generate durante la fase di :ref:`mobile-application-instance:Inizializzazione dell'Istanza dell'Applicazione Mobile`. Prima di completare il processo, il Fornitore dell'Applicazione deve anche verificare l'integrità dell'Istanza dell'Applicazione Mobile.

 .. Sebbene il flusso esatto differisca a seconda del contesto (vedi le sezioni :ref:`relying-party-instance:App di Verifica Mobile` e :ref:`wallet-attestation-issuance:Emissione della Wallet Attestation`), la Richiesta di Integrità dell'Applicazione Mobile e la Risposta di Errore sono coerenti.


.. Richiesta di Associazione Chiave dell'Applicazione Mobile
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. La Richiesta di Associazione Chiave utilizza il metodo HTTP POST con ``Content-Type`` impostato su ``application/json``.

.. Il corpo della Richiesta di Associazione Chiave contiene un parametro ``assertion`` il cui valore è un JWT firmato che include tutti i parametri di intestazione e gli attributi del corpo descritti di seguito (:ref:`WP_134 <wallet-instance-optional-testcases>`).

.. Di seguito è riportato un esempio non normativo di una Richiesta di Associazione Chiave.

.. .. code-block:: http

 ..   POST /key-binding HTTP/1.1
    Host: application-provider.example.org
    Content-Type: application/json

    {
      "assertion": "eyJhbGciOiJFUzI1NiIsImtpZCI6ImtoakZWTE9nRjNHeG..."
    }

.. In particolare, il JWT della Richiesta di Associazione Chiave include i seguenti parametri di intestazione HTTP:

.. .. _table_key_binding_request_claim:
 .. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

..    * - **Parametro**
      - **Descrizione**
      - **Riferimento**
    * - **alg**
      - Un identificatore di algoritmo di firma digitale come da registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati in :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` o qualsiasi identificatore di algoritmo simmetrico (MAC).
      - [:rfc:`7516#section-4.1.1`]
    * - **kid**
      - Impronta digitale della JWK dell'Istanza dell'Applicazione Mobile contenuta nell'attributo ``cnf``.
      - [:rfc:`7638#section_3`]
    * - **typ**
      - Il tipo del JWT, che può assumere valori diversi a seconda del contesto.
      -

.. Il JWT della Richiesta di Associazione Chiave include i seguenti attributi del corpo:

..
  .. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Attributo**
      - **Descrizione**
      - **Riferimento**
    * - **iss**
      - L'identificatore del Fornitore dell'Applicazione concatenato con l'impronta digitale della JWK nell'attributo ``cnf``.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **aud**
      - L'identificatore del Fornitore dell'Applicazione.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **exp**
      - Timestamp UNIX che rappresenta il tempo di scadenza del JWT.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **iat**
      - Timestamp UNIX che rappresenta il tempo di emissione del JWT.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **nonce**
      - Il ``nonce`` ottenuto dall'Endpoint Nonce.
      -
    * - **hardware_signature**
      - La firma di ``client_data`` ottenuta utilizzando la Cryptographic Hardware Key, codificata nel formato ``base64url``.
      -
    * - **integrity_assertion**
      - L'Integrity Assertion ottenuta dalle **API del Servizio di Integrità del Dispositivo** con l'associazione del titolare di ``client_data``.
      -
    * - **hardware_key_tag**
      - Il valore del Cryptographic Hardware Key Tag.
      -
    * - **cnf**
      - Oggetto JSON contenente la parte pubblica di una coppia di chiavi asimmetriche posseduta dall'Istanza dell'Applicazione Mobile.
      - :rfc:`7800`.

.. Di seguito è riportato un esempio non normativo di un'intestazione e un payload JWT di una Richiesta di Associazione Chiave.


..
 .. code-block:: json

 ..   {
      "alg": "ES256",
      "kid": "hT3v7KQjFZy6GvDkYgOZ1u2F6T4Nz5bPjX8o1MZ3dJY",
      "typ": "..."
    }

.. .. code-block:: json

 ..   {
      "iss": "https://application-provider.example.org/instance/hT3v7KQjFZy6GvDkYgOZ1u2F6T4Nz5bPjX8o1MZ3dJY",
      "sub": "https://application-provider.example.org/",
      "nonce": "f3b29a81-45c7-4d12-b8b5-e1f6c9327aef",
      "hardware_signature": "KoZIhvcNAQcCoIAwgAIB...",
      "integrity_assertion": "o2NmbXRvYXBwbGUtYXBwYXNzZXJ0aW9uLXBheWxvYWQtYXBw...",
      "hardware_key_tag": "QW12DylRTmF89iGkpydNDWW7m8bVpa2Fn9KBeXGYtfX"
      "cnf": {
        "jwk": {
          "crv": "P-256",
          "kty": "EC",
          "x": "8FJtI-yr3pjyRKGMnz4WmdnQD_uJSq4R95Nj98b44",
          "y": "MKZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg"
        }
      }
    }


.. Risposta di Associazione Chiave dell'Applicazione Mobile
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. La Risposta di Associazione Chiave dipende strettamente dal contesto della richiesta; ulteriori dettagli sono forniti nelle sezioni :ref:`relying-party-provider-backend-endpoint:Risposta di Associazione Chiavi della Relying Party` e :ref:`wallet-provider-endpoint:Risposta all'Emissione della Wallet Attestation`.


.. Risposta di Errore di Associazione Chiave dell'Applicazione Mobile
.. """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. Se si verificano errori, il Fornitore dell'Applicazione restituisce una risposta di errore. La risposta utilizza ``application/json`` come ``Content-Type`` e include i seguenti parametri:

  .. - *error*. Il codice di errore.
  - *error_description*. Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato (:ref:`WP_035 <wallet-instance-testcases>`).

.. Di seguito è riportato un esempio non normativo di una Risposta di Errore di Associazione Chiave.

.. .. code-block:: http
..
    HTTP/1.1 403 Forbidden
    Content-Type: application/json

    {
      "error": "invalid_request",
      "error_description": "The provided challenge is invalid, expired, or already used."
    }

.. La seguente tabella elenca i Codici di Stato HTTP e i relativi codici di errore supportati per la risposta di errore, se non diversamente specificato (:ref:`WP_036–0339 <wallet-instance-testcases>` and :ref:`WP_150–155 <wallet-instance-optional-testcases>`):
..
 .. list-table::
    :class: longtable
    :widths: 30 20 50
    :header-rows: 1

    * - **Codice di Stato HTTP**
      - **Codice di Errore**
      - **Descrizione**
    * - ``400 Bad Request``
      - ``bad_request``
      - La richiesta è malformata, mancano parametri richiesti (ad esempio, parametri di intestazione o Integrity Assertion) o include parametri non validi e sconosciuti.
    * - ``403 Forbidden``
      - ``invalid_request``
      - L'Istanza dell'Applicazione Mobile è stata revocata.
    * - ``403 Forbidden``
      - ``integrity_check_error``
      - Il dispositivo non soddisfa i requisiti minimi di sicurezza del Fornitore dell'Applicazione.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La firma della Richiesta di Integrità non è valida o non corrisponde alla chiave pubblica associata (JWK).
    * - ``403 Forbidden``
      - ``invalid_request``
      - La validazione dell'Integrity Assertion è fallita; l'Integrity Assertion è manomessa o firmata impropriamente.
    * - ``403 Forbidden``
      - ``invalid_request``
      - Il ``nonce`` fornito non è valido, è scaduto o è già stato utilizzato.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La Prova di Possesso (``hardware_signature``) non è valida.
    * - ``403 Forbidden``
      - ``invalid_request``
      - Il parametro ``iss`` non corrisponde all'identificatore URL previsto del Fornitore dell'Applicazione.
    * - ``404 Not Found``
      - ``not_found``
      - L'Istanza dell'Applicazione Mobile non è stata trovata.
    * - ``422 Unprocessable Content`` [OPZIONALE]
      - ``validation_error``
      - La richiesta non aderisce al formato richiesto.
    * - ``500 Internal Server Error``
      - ``server_error``
      - Si è verificato un errore interno del server durante l'elaborazione della richiesta.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - Il servizio non è disponibile. Si prega di riprovare più tardi.


