.. include:: ../common/common_definitions.rst
.. Incluso tramite endpoints.rst al livello di titolo '-' (livello 1).

.. role:: raw-html(raw)
  :format: html


Endpoint del Fornitore di Wallet
--------------------------------

Il Fornitore di Wallet, responsabile della fornitura di una Soluzione Wallet, DEVE esporre gli endpoint per supportare l'instaurazione della fiducia e le funzionalità essenziali dell'Istanza di Wallet. Questi includono l'endpoint di Federazione ``/.well-known/openid-federation`` che DEVE aderire alla specifica OpenID Federation 1.0 per stabilire in modo affidabile la fiducia con il Fornitore di Wallet, nonché endpoint per la registrazione dell'Istanza di Wallet, la generazione di nonce (richiesta per la registrazione), l'emissione di attestati e la revoca. A parte l'endpoint di Federazione, i dettagli di implementazione degli altri sono lasciati alla discrezione del Fornitore di Wallet.

.. note::
   I test relativi all'uso degli endpoint del Wallet Provider sono definiti in
   :ref:`test-plans-wallet-provider:Matrice di Test per Wallet Provider`, in particolare in
   :ref:`wallet-provider-backend-testcases`,
   :ref:`wallet-instance-testcases` e
   :ref:`wallet-instance-optional-testcases`.

Endpoint di Federazione
^^^^^^^^^^^^^^^^^^^^^^^

L'endpoint ``/.well-known/openid-federation`` serve come meccanismo di discovery per l'instaurazione della fiducia recuperando la Entity Configuration del Fornitore di Wallet.

Vedere la Sezione :ref:`wallet-provider-entity-configuration:Entity Configuration del Fornitore di Wallet` per i dettagli tecnici (:ref:`WP_001–004 <wallet-provider-backend-testcases>`).


Endpoint Nonce della Soluzione Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo è un endpoint API RESTful che consente all'Istanza di Wallet di richiedere un nonce crittografico dal Fornitore di Wallet. Il nonce serve come sfida imprevedibile, monouso per garantire la freschezza e prevenire attacchi di replay.

Vedere :ref:`mobile-application-instance:Richiesta di Nonce dell'Applicazione Mobile` e :ref:`mobile-application-instance:Risposta di Nonce dell'Applicazione Mobile` per i dettagli sulla Richiesta di Nonce e sulla Risposta di Nonce (:ref:`WP_131 <wallet-instance-optional-testcases>`).

Endpoint di Gestione dell'Istanza di Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questi endpoint API RESTful sono forniti dal Fornitore di Wallet e consentono la gestione dell'Istanza di Wallet, inclusa la registrazione, il recupero dello stato, la revoca su richiesta (ad esempio, da parte dell'Utente) e l'eliminazione.
Le seguenti sezioni descrivono le richieste di registrazione, recupero dello stato e revoca, insieme alle relative risposte, gestite da questo endpoint, che sono necessarie per le funzionalità di base dell':ref:`wallet-instance-functionalities:Funzionalità dell'Istanza del Wallet`.

Richiesta di Registrazione dell'Istanza di Wallet
"""""""""""""""""""""""""""""""""""""""""""""""""

Per registrare un'Istanza di Wallet, la richiesta al Fornitore di Wallet DEVE utilizzare il metodo HTTP POST con ``Content-Type`` impostato su `application/json`. Il corpo della richiesta DEVE contenere i claim descritti in :ref:`mobile-application-instance:Richiesta di Inizializzazione dell'Istanza dell'Applicazione Mobile` (:ref:`WP_131–134 <wallet-instance-optional-testcases>`).

Risposta alla Registrazione dell'Istanza di Wallet
""""""""""""""""""""""""""""""""""""""""""""""""""

Se una Richiesta di Registrazione dell'Istanza di Wallet viene convalidata con successo, il Fornitore di Wallet fornisce una Risposta HTTP con codice di stato 204 (No Content). Per i dettagli vedere :ref:`mobile-application-instance:Risposta di Inizializzazione dell'Istanza dell'Applicazione Mobile` (:ref:`WP_135–137 <wallet-instance-optional-testcases>`).

Richiesta di Recupero dell'Istanza di Wallet
""""""""""""""""""""""""""""""""""""""""""""

Per recuperare tutte le Istanze di Wallet associate a un Utente, una richiesta DEVE essere inviata utilizzando il metodo HTTP GET al Fornitore di Wallet (:ref:`WP_145 <wallet-instance-optional-testcases>`).

.. note::
  Per recuperare una specifica Istanza di Wallet, la richiesta DEVE includere l'ID dell'Istanza di Wallet come parametro di percorso.


Risposta al Recupero dell'Istanza di Wallet
"""""""""""""""""""""""""""""""""""""""""""

Se una Richiesta di Recupero dell'Istanza di Wallet viene elaborata con successo, il Fornitore di Wallet DEVE restituire una Risposta HTTP con un codice di stato 200 (OK).
Il corpo della risposta DEVE essere in formato JSON e includere le informazioni rilevanti dell'Istanza di Wallet, come il suo ID univoco, lo stato e la data di emissione.
Quando si recuperano tutte le Istanze di Wallet, la risposta DEVE restituire un array contenente i dettagli di tutte le istanze associate (:ref:`WP_146 <wallet-instance-optional-testcases>`).

Se si verificano errori durante il processo di recupero, DEVE essere restituita una risposta di errore. Fare riferimento a :ref:`wallet-provider-endpoint:Gestione degli Errori per la Gestione dell'Istanza di Wallet` per i dettagli sui codici di errore e le descrizioni.

Di seguito è riportato un esempio non normativo di una risposta di errore:

.. code-block:: http

   HTTP/1.1 403 Forbidden
   Content-Type: application/json
   Cache-Control: no-store

   {
     "error": "forbidden",
     "error_description": "User is not authorized to retrieve Wallet Instances."
   }


Richiesta di Revoca dell'Istanza di Wallet
""""""""""""""""""""""""""""""""""""""""""

Per revocare un'Istanza di Wallet attiva, una richiesta di revoca DEVE essere inviata utilizzando il metodo HTTP PATCH con Content-Type impostato su ``application/json``. Il corpo della richiesta DEVE contenere un parametro ``status`` impostato su ``REVOKED`` (:ref:`WP_147 <wallet-instance-optional-testcases>`).

.. note::
  Mentre PATCH è il metodo consigliato, la richiesta di revoca PUÒ anche essere inviata utilizzando il metodo POST, a seconda delle preferenze di implementazione.

Risposta alla Revoca dell'Istanza di Wallet
"""""""""""""""""""""""""""""""""""""""""""

Se una Richiesta di Revoca dell'Istanza di Wallet viene elaborata con successo, il Fornitore di Wallet fornisce una Risposta HTTP con un codice di stato 204 (No Content) come specificato in :ref:`WP_148 <wallet-instance-optional-testcases>`.

Se si verificano errori durante la Revoca dell'Istanza di Wallet, DEVE essere restituita una risposta di errore. Fare riferimento a :ref:`wallet-provider-endpoint:Gestione degli Errori per la Gestione dell'Istanza di Wallet` per i dettagli sui codici di errore e le descrizioni (:ref:`WP_035–039, WP_043–044 <wallet-instance-testcases>`).

Di seguito è riportato un esempio non normativo di una risposta di errore:

.. code-block:: http

   HTTP/1.1 400 Bad Request
   Content-Type: application/json
   Cache-Control: no-store

   {
     "error": "bad_request",
     "error_description": "The request is missing status parameter."
   }

Gestione degli Errori per la Gestione dell'Istanza di Wallet
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Per garantire robustezza e sicurezza, il Fornitore di Wallet DEVE gestire gli errori in modo coerente in tutte le richieste di Gestione dell'Istanza di Wallet, incluse Registrazione, Recupero e Revoca (:ref:`WP_035–044 <wallet-instance-testcases>`, e :ref:`WP_150–155 <wallet-instance-optional-testcases>`).

In caso di errore, il Fornitore di Wallet DEVE restituire una risposta di errore come definito in :rfc:`7231`, con ulteriori dettagli disponibili in :rfc:`7807`. La risposta DEVE utilizzare il Content-Type impostato su ``application/json`` e DEVE includere i seguenti parametri:

- *error*. Il codice di errore.
- *error_description*. Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.

Le seguenti sezioni classificano gli errori in **errori comuni**, che si applicano a tutte le richieste, ed **errori specifici della richiesta**, che sono rilevanti per operazioni particolari.

Risposte di Errore Comuni
"""""""""""""""""""""""""

I seguenti errori si applicano a tutte le operazioni di Gestione dell'Istanza di Wallet (Registrazione, Recupero e Revoca) e DEVONO essere supportati per la risposta di errore, se non diversamente specificato (:ref:`WP_035–039 <wallet-instance-testcases>`):

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
   * - ``422 Unprocessable Content`` [OPZIONALE]
     - ``validation_error``
     - La richiesta non aderisce al formato richiesto.
   * - ``500 Internal Server Error``
     - ``server_error``
     - Si è verificato un errore interno durante l'elaborazione della richiesta.
   * - ``503 Service Unavailable``
     - ``temporarily_unavailable``
     - Il servizio non è disponibile. Si prega di riprovare più tardi.

Risposte di Errore Specifiche della Richiesta
"""""""""""""""""""""""""""""""""""""""""""""

Gli errori in :ref:`mobile-application-instance:Risposta di Errore di Inizializzazione dell'Istanza dell'Applicazione Mobile` DEVONO essere supportati per le risposte di errore relative alla **Registrazione dell'Istanza di Wallet**.

I seguenti errori DEVONO essere supportati per le risposte di errore relative al **Recupero dell'Istanza di Wallet** (:ref:`WP_041–042 <wallet-instance-testcases>`):

.. list-table::
   :class: longtable
   :widths: 20 20 50
   :header-rows: 1

   * - **Codice di Stato HTTP**
     - **Codice di Errore**
     - **Descrizione**
   * - ``403 Forbidden``
     - ``forbidden``
     - L'Utente non ha il permesso di recuperare questa Istanza di Wallet.
   * - ``401 Unauthorized``
     - ``unauthorized``
     - La richiesta manca di Credenziali di autenticazione valide.

I seguenti errori DEVONO essere supportati per le risposte di errore relative alla **Revoca dell'Istanza di Wallet** (:ref:`WP_043–044 <wallet-instance-testcases>`):

.. list-table::
   :class: longtable
   :widths: 20 20 50
   :header-rows: 1

   * - **Codice di Stato HTTP**
     - **Codice di Errore**
     - **Descrizione**
   * - ``403 Forbidden``
     - ``invalid_request``
     - L'Utente non ha il permesso di revocare questa Istanza di Wallet.
   * - ``401 Unauthorized``
     - ``unauthorized``
     - La richiesta non può essere autenticata o autorizzata.

Endpoint di Emissione della Wallet Instance Attestation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo è un endpoint API RESTful fornito dal Fornitore di Wallet che consente all'Istanza di Wallet di ottenere una Wallet Instance Attestation, inviando una Richiesta di Emissione della Wallet Instance Attestation.

Richiesta di Emissione della Wallet Instance Attestation
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

La richiesta di emissione della Wallet Instance Attestation utilizza il metodo HTTP POST con il ``Content-Type`` impostato su ``application/json`` (:ref:`WP_026 <wallet-instance-testcases>` e :ref:`WP_140–142 <wallet-instance-optional-testcases>`).

L'intestazione ``typ`` del JWT della richiesta di emissione della Wallet Instance Attestation assume il valore ``wia-request+jwt``.

Il body della richiesta di emissione della Wallet Instance Attestation contiene un parametro ``assertion`` il cui valore è un JWT firmato che include tutti i parametri di intestazione e le claim descritti di seguito.

Di seguito è riportato un esempio non normativo di una richiesta di emissione della Wallet Instance Attestation.

.. code-block:: http

    POST /wallet-instance-attestation HTTP/1.1
    Host: application-provider.example.org
    Content-Type: application/json

    {
      "assertion": "eyJpc3MiOiJPbnNpYW5kcklqcDdJbU55ZGlJNklsQ..."
    }

In particolare, il JWT della richiesta di emissione della Wallet Instance Attestation include i seguenti parametri di intestazione HTTP:

.. _table_wia_request_claim:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parametro**
      - **Descrizione**
      - **Riferimento**
    * - **alg**
      - Identificatore dell'algoritmo di firma digitale, come definito nel registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati in :ref:`algorithms:Algoritmi Crittografici` e non DEVE essere impostato su ``none`` né su alcun identificatore di algoritmo simmetrico (MAC).
      - [:rfc:`7516#section-4.1.1`]
    * - **kid**
      - thumbprint della JWK dell'Istanza del Wallet contenuta nella dichiarazione ``cnf``.
      - [:rfc:`7638#section_3`]
    * - **typ**
      - Il tipo del JWT, che DEVE essere impostato su ``wia-request+jwt``.
      -

Il JWT della richiesta include le seguenti claim nel body:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **iss**
      - Stringa contenente l'identificativo univoco della Wallet Instance.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **exp**
      - UNIX timestamp che rappresenta il tempo di scadenza del JWT.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **iat**
      - UNIX timestamp che rappresenta il tempo di emissione del JWT.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **nonce**
      - Il ``nonce`` ottenuto dal Nonce Endpoint.
      -
    * - **hardware_signature**
      - la firma di ``client_data_hash`` ottenuta utilizzando la Chiave Crittografica Hardware, codificata nel formato ``base64url``.
      -
    * - **integrity_assertion**
      - L'Integrity Assertion per la Wallet Instance Attestation ottenuta dalle **Device Integrity Service APIs** con il binding di ``client_data_hash``.
      -
    * - **hardware_key_tag**
      - Il valore del Tag della Chiave Crittografica Hardware.
      -
    * - **cnf**
      - Oggetto JSON contenente la parte pubblica di una coppia di chiavi asimmetriche posseduta dall'istanza del Wallet.
      - :rfc:`7800`.
    * - **platform**
      - Stringa contenente il valore del sistema operativo del dispositivo.
      -
    * - **wallet_solution_id**
      - Stringa contenente l'identificatore della Wallet Solution.
      -
    * - **wallet_solution_version**
      - Stringa contenente la versione della Wallet Solution.
      -


Di seguito è riportato un esempio non normativo dell'intestazione e del payload del JWT della Wallet Instance Attestation Request.

.. code-block:: json

    {
      "alg": "ES256",
      "kid": "OnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiL",
      "typ": "wia-request+jwt"
    }

.. code-block:: json

    {
      "iss": "OnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiL",
      "nonce": "f3b29a81-45c7-4d12-b8b5-e1f6c9327aef",
      "hardware_signature": "KoZIhvcNAQcCoIAwgAIB...",
      "integrity_assertion": "o2NmbXRvYXBwbGUtYXBwYXNzZXJ0aW9uLXBheWxvYWQtYXBw...",
      "hardware_key_tag": "QW12DylRTmF89iGkpydNDWW7m8bVpa2Fn9KBeXGYtfX",
      "cnf": {
        "jwk": {
          "crv": "P-256",
          "kty": "EC",
          "x": "8FJtI-yr3pjyRKGMnz4WmdnQD_uJSq4R95Nj98b44",
          "y": "MKZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg"
        }
      },
      "platform": "iOS",
      "wallet_solution_id": "Wallet-mobile",
      "wallet_solution_version": "1.1.0"
    }


Risposta all'Emissione della Wallet Instance Attestation
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Se la Richiesta di Emissione della Wallet Instance Attestation viene convalidata con successo, il Fornitore di Wallet restituisce una risposta HTTP con un codice di stato ``200 OK`` e Content-Type ``application/json``. L'Oggetto JSON restituito DEVE possedere il parametro ``wallet_instance-attestations`` (vedi :ref:`wallet-instance-attestation-issuance:Emissione della Wallet Instance Attestation`). ``wallet_insatnce_attestation`` sono oggetti JSON che contengono rispettivamente la Wallet Instance Attestation. Entrambe le attestazioni sono firmate dal Fornitore di Wallet (:ref:`WP_027–029 <wallet-instance-testcases>` e :ref:`WP_143–144 <wallet-instance-optional-testcases>`). La Wallet Instance Attestation JWT deve essere utilizzato per la fase di Emissione di un Attestato Elettronico, come OAuth Client Attestation, e sarà inviato al Fornitore di Attestati Elettronici come discusso in :ref:`credential-issuance:Emissione di Attestati Elettronici`.


L'Oggetto JSON restituito nella risposta ha il seguente claim:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parametro**
      - **Descrizione**
      - **Riferimento**
    * - **wallet_instance-attestation**
      - OBBLIGATORIO. Una stringa contenente una Wallet Instance Attestation.
      - Questa specifica.

I valori di ``wallet_instance_attestation`` sono stringha che contenente rispettivamento la Wallet Instance Attestation in formato JWT.

Se si verifica un errore durante il processo, viene restituita una risposta di errore. La risposta utilizza ``application/json`` come ``Content-Type`` e include i seguenti parametri:

  - *error*: il codice di errore.
  - *error_description*: testo in formato leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato (:ref:`WP_035 <wallet-instance-testcases>`).

Di seguito è riportato un esempio non normativo di una Wallet Instance Attestation Issuance Response.

.. code-block:: http

    HTTP/1.1 403 Forbidden
    Content-Type: application/json

    {
      "error": "invalid_request",
      "error_description": "The provided challenge is invalid, expired, or already used."
    }

La seguente tabella elenca i codici di stato HTTP e i relativi codici di errore supportati per la risposta di errore, salvo diversa indicazione (:ref:`WP_036–039 <wallet-instance-testcases>` e :ref:`WP_150–155 <wallet-instance-optional-testcases>`):

.. list-table::
    :class: longtable
    :widths: 30 20 50
    :header-rows: 1

    * - **HTTP Status Code**
      - **Error Code**
      - **Descrizione**
    * - ``400 Bad Request``
      - ``bad_request``
      - La richiesta è malformata, mancano parametri obbligatori (ad esempio parametri di intestazione, o Integrity Assertion), oppure include parametri non validi o sconosciuti.
    * - ``403 Forbidden``
      - ``invalid_request``
      - L'istanza del Wallet è stata revocata.
    * - ``403 Forbidden``
      - ``integrity_check_error``
      - Il dispositivo non soddisfa i requisiti minimi di sicurezza del Fornitore di Wallet.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La firma della Wallet Instance Attestation Request non è valida oppure non corrisponde alla chiave pubblica (JWK) associata.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La validazione della Integrity Assertion non è riuscita; la Integrity Assertion è stata manomessa o firmata in modo non corretto.
    * - ``403 Forbidden``
      - ``invalid_request``
      - Il ``nonce`` fornito non è valido, è scaduto oppure è già stato utilizzato.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La Proof of Possession (``hardware_signature``) non è valida.
    * - ``403 Forbidden``
      - ``invalid_request``
      - Il parametro ``iss`` non corrisponde all'identificatore URL previsto dal Fornitore di Wallet.
    * - ``404 Not Found``
      - ``not_found``
      - L'istanza del Wallet non è stata trovata.
    * - ``422 Unprocessable Content`` [OPZIONALE]
      - ``validation_error``
      - La richiesta non rispetta il formato richiesto.
    * - ``500 Internal Server Error``
      - ``server_error``
      - Si è verificato un errore interno del server durante l'elaborazione della richiesta.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - Il servizio non è disponibile. Si prega di riprovare più tardi.


JWT della Wallet Instance Attestation
"""""""""""""""""""""""""""""""""""""

L'header JOSE del JWT della Wallet Instance Attestation contiene i seguenti parametri:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Header JOSE**
      - **Descrizione**
      - **Riferimento**
    * - **alg**
      - OBBLIGATORIO. Un identificatore di algoritmo di firma digitale come da registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` o qualsiasi identificatore di algoritmo simmetrico (MAC).
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      - OBBLIGATORIO. Identificatore univoco della chiave pubblica associata alla chiave privata che il Fornitore di Wallet ha utilizzato per firmare la Wallet Instance Attestation.
      - :rfc:`7638#section_3`.
    * - **typ**
      - OBBLIGATORIO. DEVE essere impostato su ``oauth-client-attestation+jwt``
      - `OPENID4VC-HAIP`_.
    * - **trust_chain**
      - OPZIONALE. Sequenza di Entity Statement che compone la Catena di Fiducia relativa al Fornitore di Wallet.
      - `OID-FED`_ Sezione 4.3 *Trust Chain Header Parameter*.
    * - **x5c**
      - OBBLIGATORIO. Contiene il certificato di chiave pubblica X.509 o la catena di certificati (:rfc:`5280`) corrispondente alla chiave utilizzata per firmare digitalmente il JWT.
      - :rfc:`7515` Sezione 4.1.8, `SD-JWT-VC`_ Sezione 3.5 e  `OPENID4VC-HAIP`_.

Il corpo del JWT della Wallet Instance Attestation contiene i seguenti claim:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **exp**
      - OBBLIGATORIO. Timestamp UNIX con il tempo di scadenza del JWT. Questo dovrebbe essere impostato a un massimo di 24 ore.
      - :rfc:`9126` e :rfc:`7519` e `EUDI-TS 3`_.
    * - **nbf**
      - OPZIONALE. Timestamp UNIX con data e orario prima del quale il JWT NON DEVE essere accettato.
      - :rfc:`9126` e :rfc:`7519`.
    * - **cnf**
      - OBBLIGATORIO. Oggetto JSON, contenente la parte pubblica di una coppia di chiavi asimmetriche posseduta dall'Istanza di Wallet.
      - :rfc:`7800`.
    * - **wallet_link**
      - OBBLIGATORIO. Stringa contenente un URL per ottenere ulteriori informazioni sul Wallet e sul Fornitore di Wallet.
      - `OpenID4VCI`_.
    * - **wallet_name**
      - OBBLIGATORIO. Stringa contenente un nome leggibile dall'uomo del Wallet.
      - `OpenID4VCI`_.
    * - **wallet_version**
      - OBBLIGATORIO. Valore stringa della versione della Wallet Solution.
      - `OpenID4VCI`_ e `EUDI-TS 3`_.
    * - **wallet_solution_certification_information**
      - OPZIONALE. Valore stringa che contiene un URL che rimanda alla certificazione della Wallet Solution.
      - `EUDI-TS 3`_.
    * - **client_status**
      - OBBLIGATORIO. Meccanismo di stato per la Wallet Attestation.

        - **status**: OBBLIGATORIO. un riferimento alla lista di stato, come specificato nell’Appendice E di `OpenID4VCI`_. Il valore rappresenta lo stato di revoca dell’istanza del Wallet.
        - **exp**: OBBLIGATORIO. Timestamp UNIX che specifica il momento fino al quale il Wallet Provider si impegna a mantenere lo stato di revoca nell’indice della lista di stato referenziato in ``status``.
      - `EUDI-TS 3`_.
    * - **sub**
      - OBBLIGATORIO. Identificatore dell’istanza del Wallet, che è l’identificatore univoco della Wallet Solution in formato URL.
      - `EUDI-TS 3`_.


Di seguito è riportato un esempio non normativo dell'header e del payload della Wallet Instance Attestation JWT senza codifica e firma applicata:

.. literalinclude:: ../../examples/wa-jwt_example_header.json
  :language: JSON

.. literalinclude:: ../../examples/wa-jwt_example_payload.json
  :language: JSON


.. note::
    Poiché lo schema di certificazione non è ancora stato definito, il contenuto esatto di ``wallet_solution_certification_information`` è indefinito. Questo contenuto sarà definito in un aggiornamento futuro.

.. note::
    Come meccanismo di revoca per la WIA, è preferita l’opzione di riutilizzo per emittente descritta nella Sezione 2.5.1 di `EUDI-TS 3`_.


.. note::
    Il claim ``iss`` non è più necessario nel corpo della WIA, poiché l’identità del Wallet Provider viene ora dedotta dal certificato di firma nel parametro di intestazione JOSE ``x5c``.





Endpoint di Emissione della Key Attestation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo è un endpoint API RESTful fornito dal Wallet Provider che consente alla Wallet Instance di ottenere una Key Attestation, inviando una Richiesta di Emissione della Key Attestation.

Richiesta di Emissione della Key Attestation
"""""""""""""""""""""""""""""""""""""""""""""""""""""

La  richiesta di emissione della Key Attestation utilizza il metodo HTTP POST con ``Content-Type`` impostato a ``application/json``. (:ref:`WP_026 <wallet-instance-testcases>` e :ref:`WP_140–142 <wallet-instance-optional-testcases>`).

L'header ``typ`` del JWT della richiesta di emissione Key Attestation Issuance assume il valore ``ka-request+jwt``.

Il body della richiesta di emissione Key Attestation contiene un parametro ``assertion`` il cui valore è un JWT firmato che include tutti i parametri di header e i claim del body descritti di seguito.

Di seguito è riportato un esempio non normativo di una Key Attestation Request.

.. code-block:: http

    POST /key-attestation HTTP/1.1
    Host: application-provider.example.org
    Content-Type: application/json

    {
      "assertion": "eyJpc3MiOiJPbnNpYW5kcklqcDdJbU55ZGlJNklsQ..."
    }

In particolare, il JWT della Key Attestation Issuance include i seguenti parametri di header HTTP:

.. _table_ka_request_claim:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **alg**
      - Identificatore di algoritmo di firma digitale, come definito dal registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati in :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato a ``none`` né a un identificatore di algoritmo simmetrico (MAC).
      - [:rfc:`7516#section-4.1.1`]
    * - **kid**
      - Thumbprint della JWK della Wallet Instance contenuta nel claim ``cnf``.
      - [:rfc:`7638#section_3`]
    * - **typ**
      - Il tipo del JWT; DEVE essere impostato a ``ka-request+jwt``.
      -

Il JWT della Key Attestation Request include i seguenti claim nel body:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - Stringa contenente l'identificativo univoco della Wallet Instance.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **exp**
      - Timestamp UNIX che rappresenta il tempo di scadenza del JWT.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **iat**
      - Timestamp UNIX che rappresenta il tempo di emissione del JWT.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **nonce**
      - Il ``nonce`` ottenuto dal Nonce Endpoint.
      -
    * - **keys_to_attest**
      - Array JSON di stringhe JWT, ciascuna delle quali rappresenta una ``Key_Attestation_Requests``.
      -
    * - **hardware_signature**
      - La firma di ``client_data_hash`` ottenuta utilizzando la Cryptographic Hardware Key, codificata nel formato ``base64url``.
      -
    * - **integrity_assertion**
      - L'Integrity Assertion per la Wallet Instance Attestation ottenuta dalle **Device Integrity Service APIs** con holder binding di ``client_data_hash``.
      -
    * - **hardware_key_tag**
      - Il valore del Cryptographic Hardware Key Tag.
      -
    * - **cnf**
      - Oggetto JSON contenente la parte pubblica della prima coppia di chiavi asimmetriche (primo elemento di ``keys_to_attest``) posseduta dalla Wallet Instance.
      - :rfc:`7800`.
    * - **platform**
      - Stringa contenente il valore del sistema operativo del dispositivo.
      -
    * - **wallet_solution_id**
      - Stringa contenente l'identificatore della Wallet Solution.
      -
    * - **wallet_solution_version**
      - Stringa contenente la versione della Wallet Solution.
      -


Di seguito è riportato un esempio non normativo dell'header e del payload JWT di una Key Attestation Request.


.. code-block:: json

    {
      "alg": "ES256",
      "kid": "OnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiL",
      "typ": "ka-request+jwt"
    }

.. code-block:: json

    {
      "iss": "OnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiL",
      "nonce": "f3b29a81-45c7-4d12-b8b5-e1f6c9327aef",
      "hardware_signature": "KoZIhvcNAQcCoIAwgAIB...",
      "integrity_assertion": "o2NmbXRvYXBwbGUtYXBwYXNzZXJ0aW9uLXBheWxvYWQtYXBw...",
      "hardware_key_tag": "QW12DylRTmF89iGkpydNDWW7m8bVpa2Fn9KBeXGYtfX",
      "cnf": {
        "jwk": {
          "crv": "P-256",
          "kty": "EC",
          "x": "8FJtI-yr3pjyRKGMnz4WmdnQD_uJSq4R95Nj98b44",
          "y": "MKZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg"
        }
      },
      "keys_to_attest": [
        "eyJ0eXAiOiJrZXktYXR0ZXN0YXRpb24tcmVxdWVzdCtqd3QiLCJhbGciOiJFUzI1NiIsImtpZCI6Ik9LSEhrVk5PckthUFZKdWZsREt3MVNRSEZOWTVpeTlPaXdBdHBBMGNvSUEifQ.eyJ3c2NkX2tleV9hdHRlc3RhdGlvbiI6eyJzdG9yYWdlX3R5cGUiOiJMT0NBTF9OQVRJVkUifSwiY25mIjp7Imp3ayI6eyJrdHkiOiJFQyIsIngiOiJ4QUg5U05mYXE5SjVkbWt6WFlRTGVrNVlmcFBjOGlfUHBNUlQzMTVoak1rIiwieSI6IlBFMlhMY3BXNmVYSDRGbFlHTlA5Qmh3UVFkRWlaRTF0QWRULUVpaEFDQzgiLCJjcnYiOiJQLTI1NiIsImtpZCI6Ik9LSEhrVk5PckthUFZKdWZsREt3MVNRSEZOWTVpeTlPaXdBdHBBMGNvSUEifX0sImlhdCI6MTc3MzA1Mzg2MSwiZXhwIjoxNzczMDU3NDYxfQ.Rn3D0GwYYZJaupzJ6617V0xav_HH6bGnttoGrD4lwY8ICPH9NiEbTF9ZBYD3aHh20Z9GCjQ8Fhit5Fbps8v9Aw",
        "eyJ0eXAiOiJrZXktYXR0ZXN0YXRpb24tcmVxdWVzdCtqd3QiLCJhbGciOiJFUzI1NiIsImtpZCI6IkViUUJSQ2dLNWJrVzlZNU1idGEwZlpzMVdhVTBLZVpiek9iTXVvY2NLb28ifQ.eyJ3c2NkX2tleV9hdHRlc3RhdGlvbiI6eyJzdG9yYWdlX3R5cGUiOiJMT0NBTF9OQVRJVkUifSwiY25mIjp7Imp3ayI6eyJrdHkiOiJFQyIsIngiOiJEVVFWTGhLMUtRUmQtZ3g3UU5jYVNhWENnOXg0S3R6QmstNWIxWTNkeWU0IiwieSI6IkZxVjk0TWVrVm5fQ05mNTIxdm1vLVFIcWZObk12eGdIR3NFeDlCTlc4aFEiLCJjcnYiOiJQLTI1NiIsImtpZCI6IkViUUJSQ2dLNWJrVzlZNU1idGEwZlpzMVdhVTBLZVpiek9iTXVvY2NLb28ifX0sImlhdCI6MTc3MzA1Mzg2MSwiZXhwIjoxNzczMDU3NDYxfQ.wIYOmX8-dmuRnuaCVg1kFoTHhsvv01vbapQ8-3er-HIiAF819Kt3Uy0PUN_WgxP7eWMGwhkn_9tQnnhdgXLYyw"
      ],
      "platform": "iOS",
      "wallet_solution_id": "Wallet-mobile",
      "wallet_solution_version": "1.1.0"
    }


Risposta all'Emissione della Key Attestation
"""""""""""""""""""""""""""""""""""""""""""""""""""""

Se la Key Attestation Issuance Request viene validata con successo, il Wallet Provider restituisce una risposta HTTP con codice di stato ``200 OK`` e ``Content-Type`` ``application/json``. L'oggetto JSON restituito include ``key_attestation`` (si veda :ref:`wallet-attestation-issuance:Emissione della Key Attestation`). ``key_attestation`` è firmata dal Wallet Provider (:ref:`WP_027–029 <wallet-instance-testcases>` e :ref:`WP_143–144 <wallet-instance-optional-testcases>`). La Key Attestation JWT deve essere utilizzata nella fase di Emissione di un Attestato Elettronico, come intestazione JOSE ``key_attestation`` nel JWT di tipo ``proof``, e verrà inviata al Fornitore di Attestati Elettronici come discusso in :ref:`credential-issuance:Emissione di Attestati Elettronici`.


L'oggetto JSON restituito nella risposta contiene il seguente parametro:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **key_attestation**
      - OBBLIGATORIO. Una stringa che rappresenta la Key Attestation rilasciata.
      - Questa specifica.

Il valore del parametro ``key_attestation`` è una stringa che rappresenta la Key Attestation in formato JWT.

Se durante il processo si verificano errori, viene restituita una risposta di errore come definito nella sezione precedente.


La tabella seguente elenca i codici di stato HTTP e i relativi codici di errore per i casi che differiscono da quanto già riportato:

.. list-table::
    :class: longtable
    :widths: 30 20 50
    :header-rows: 1

    * - **HTTP Status Code**
      - **Error Code**
      - **Description**
    * - ``400 Bad Request``
      - ``bad_request``
      - La richiesta è malformata, mancano parametri obbligatori (ad esempio parametri di header, Integrity Assertion o ``keys_to_attest``), oppure include parametri non validi o sconosciuti.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La validazione dell'Integrity Assertion o della Key Attestation (``keys_to_attest``) non è riuscita; l'Integrity Assertion o la Key Attestation (``keys_to_attest``) è stata manomessa oppure firmata in modo non corretto.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La firma della key Attestation Request non è valida oppure non corrisponde alla chiave pubblica associata (JWK).








Key Attestation JWT
""""""""""""""""""""""""""""

L'intestazione JOSE del Key Attestation JWT contiene i seguenti parametri:


.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Descrizione**
      - **Riferimento**
    * - **alg**
      - OBBLIGATORIO. Un identificatore di algoritmo di firma digitale come da registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati in :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` o qualsiasi identificatore di algoritmo simmetrico (MAC).
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      - OBBLIGATORIO. Identificatore univoco della chiave pubblica associata alla chiave privata che il Fornitore di Wallet ha utilizzato per firmare la Key Attestation.
      - :rfc:`7638#section_3`.
    * - **typ**
      - OBBLIGATORIO. DEVE essere impostato su ``key-attestation+jwt``
      - `OPENID4VC-HAIP`_.
    * - **trust_chain**
      - OPZIONALE. Sequenza di Entity Statement che compone la Catena di Fiducia relativa al Fornitore di Wallet.
      - `OID-FED`_ Sezione 4.3 *Trust Chain Header Parameter*.
    * - **x5c**
      - OBBLIGATORIO. Contiene il certificato di chiave pubblica X.509 o la catena di certificati (:rfc:`5280`) corrispondente alla chiave utilizzata per firmare digitalmente il JWT.
      - :rfc:`7515` Sezione 4.1.8 e `SD-JWT-VC`_ Sezione 3.5.

Il corpo del Key Attestation JWT contiene le seguenti dichiarazioni (claims):

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **exp**
      - OBBLIGATORIO. Timestamp UNIX con il tempo di scadenza del JWT.
      - :rfc:`9126` e :rfc:`7519`.
    * - **iat**
      - OBBLIGATORIO. Timestamp UNIX con il tempo di emissione del JWT.
      - :rfc:`9126` e :rfc:`7519`.
    * - **attested_keys**
      - OBBLIGATORIO. Un array non vuoto di chiavi attestate provenienti dallo stesso componente di archiviazione delle chiavi, utilizzando la sintassi JWK, contenente la parte pubblica di una coppia di chiavi asimmetriche posseduta dall'istanza del Wallet.
      - :rfc:`7517`.
    * - **key_storage**
      - OBBLIGATORIO. Un array non vuoto di stringhe sensibili alle maiuscole che dichiarano la resistenza al potenziale di attacco del componente di archiviazione delle chiavi e delle chiavi attestate nel parametro ``attested_keys``. I seguenti valori sono definiti come possibili valori per questa dichiarazione claim:

        - ``iso_18045_high``: DEVE essere utilizzato quando l'archiviazione delle chiavi è resistente ad attacchi con potenziale di attacco ``High``.
        - ``iso_18045_moderate``: DEVE essere utilizzato quando l'archiviazione delle chiavi è resistente ad attacchi con potenziale di attacco  ``Moderate``.
        - ``iso_18045_enhanced-basic``: DEVE essere utilizzato quando l'archiviazione delle chiavi è resistente ad attacchi con potenziale di attacco  ``Enhanced-Basic``.
        - ``iso_18045_basic``: DEVE essere utilizzato quando l'archiviazione delle chiavi è resistente ad attacchi con potenziale di attacco  ``Basic``.
      - `OpenID4VCI`_.
    * - **user_authentication**
      - OBBLIGATORIO. Un array non vuoto di stringhe sensibili alle maiuscole che dichiarano la resistenza al potenziale di attacco dei metodi di autenticazione utente autorizzati ad accedere alle chiavi private dal parametro attested_keys. I seguenti valori sono definiti come possibili valori per questa dichiarazione claim:

        - ``iso_18045_high``: DEVE essere utilizzato quando l'autenticazione dell'utente è resistente ad attacchi con potenziale di attacco ``High``.
        - ``iso_18045_moderate``: DEVE essere utilizzato quando l'autenticazione dell'utente è resistente ad attacchi con potenziale di attacco ``Moderate``.
        - ``iso_18045_enhanced-basic``: DEVE essere utilizzato quando l'autenticazione dell'utente è resistente ad attacchi con potenziale di attacco ``Enhanced-Basic``.
        - ``iso_18045_basic``: DEVE essere utilizzato quando l'autenticazione dell'utente è resistente ad attacchi con potenziale di attacco ``Basic``.
      - `OpenID4VCI`_.
    * - **key_storage_status**
      - OBBLIGATORIO. Meccanismo di stato per la Key Attestation.

        - **status**: OBBLIGATORIO. un riferimento alla lista di stato, come specificato nell’Appendice D di `OpenID4VCI`_. Il valore rappresenta lo stato di revoca del WSCD o del Keystore.
        - **exp**: OBBLIGATORIO. Timestamp UNIX che specifica il momento fino al quale il Wallet Provider si impegna a mantenere lo stato di revoca nell’indice della lista di stato referenziato in ``status``.
      - `EUDI-TS 3`_.
    * - **certification**
      - OPZIONALE. Una stringa che contiene un URL che rimanda alla certificazione del componente di archiviazione delle chiavi.
      - `OpenID4VCI`_.



Di seguito è riportato un esempio non normativo dell'intestazione e del payload del Key Attestation JWT, senza codifica né firma applicata:

.. literalinclude:: ../../examples/ka-jwt_example_header.json
  :language: JSON

.. literalinclude:: ../../examples/ka-jwt_example_payload.json
  :language: JSON


.. note::
    Poiché lo schema di certificazione non è ancora stato definito, il contenuto esatto di ``certification`` non è definito e sarà specificato in un futuro aggiornamento.


.. note::
    Come meccanismo di revoca per la KA, è preferito l'indice condiviso per tipo descritto nella Sezione 2.5.2 di `EUDI-TS 3`_.

.. note::
    Un fornitore di Wallet DEVE scegliere il periodo di validità tecnica della KA e DEVE mantenere l'elenco degli stati di revoca per l'intero periodo di validità di tale elenco, come indicato nel claim ``key_storage_status.exp``.




Catalogo e-Service PDND del Fornitore di Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La morte dell'Utente porta alla revoca delle Istanze di Wallet dell'Utente e all'eliminazione dell'account dell'Utente presso il Fornitore di Wallet. Per questo motivo, il Fornitore di Wallet fornisce il seguente e-service tramite PDND.
Un Provider di PID/IT-Wallet ID che è stato notificato dalla Fonte Autentica del PID/IT-Wallet ID della morte dell'Utente DEVE inviare una notifica ai Fornitori di Wallet utilizzando questo endpoint.

.. only:: html

  .. note::
    Una Specifica OpenAPI completa è disponibile :raw-html:`<a href="OAS3-PDND-WP.html" target="_blank">qui</a>`.

.. only:: latex

  .. note::
    Una Specifica OpenAPI completa è disponibile :ref:`appendix-oas-pdnd-wp:Specifica OpenAPI del Fornitore di Wallet PDND`.

Notifica Morte Utente
"""""""""""""""""""""

.. list-table::
    :class: longtable
    :widths: 20 80
    :stub-columns: 1

    * - **Descrizione**
      - Questo servizio viene utilizzato per notificare al Fornitore di Wallet la necessità di revocare l'Istanza di Wallet ed eliminare l'account dell'Utente a causa della morte dell'Utente.
    * - **Fornitore**
      - Fornitore di Wallet
    * - **Consumatore**
      - Fornitore di Attestati Elettronici di Dati di Identificazione Personale


