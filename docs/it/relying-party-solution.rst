.. include:: ../common/common_definitions.rst

.. _soluzione-relying-party.rst:

Soluzione Relying Party
+++++++++++++++++++++++

Questo documento definisce l’implementazione del flusso di presentazione online e verifica di una credenziale (PID o (Q)EAA), in conformità alle specifiche “OpenID for Verifiable Credential Presentation - draft 19",  nel contesto di scenario Web di tipo cross-device.

Autenticazione Cross Device
---------------------------

In questa sezione viene riportato un sequence diagram dettagliato del caso d’uso “Autenticazione Cross Device”. L'utente entra nel sito web e presenta il suo PID attraverso il wallet. Una volta autenticato l'utente potrà richiedere le credenziali disponibili sul Wallet.

Nel diagramma sottostante è spiegato il flusso della Autenticazione Cross Device

N.B. Casi d’uso su altre credenziali verranno analizzati e descritti in sprint successivi

.. image:: ../../images/cross_device_auth_seq_diagram.svg
  :align: center
  :target: http://www.plantuml.com/plantuml/umla/TLFDZjem4BxxAKPKgjf3Ns0bgkrIMj5M8eKiU-7Y91DmrnbJ_soMFdtjiCOcY5iqy_rydntV6ykrTPrat5b5hgjGCtRmCr6B0oSBaqU3UWBSW6EiKgymMQ4y2jf1uL772Rpx9NPx-o0TNl8sg4KhKCE7RrgHdLFpSP1fR-8UUFryXbN8a1hmZgCyJrnAjB0W7vrg7C0zOzCfV75sZ-IHt0f50DCfS_3fC_HtmqffyG-X5tOF9mt6QojUk4LmwRDdVU2qU0VhS3PdwY3A6ap8H6gHjHXebQVDD8RP1GzM-DUXIPQXN-Kf9wkuXiVL8hUeecwRT7-lOAQQkEXzpBtg_JGCyngiZ_kQqvaLX_DNgpquDzvIgrMNaB7FztbvXYshF-XPMwgEEVMwLZ0PiKR5Of8Dbw89inzF9Qp5ZhXrEgqBhMeqPfpW_PQowqO8VscAN2pNvTK5c8CYWwCR7EKEz9kH4Y26kccHwxATLku0XP8oF1ld8qlG4TjYEkTHvk6KIyt913b5YwytyiwyakiGDWMKwXafMote9PR9bAwLyvzn-NFK0AbXRq5TzfQQ7DPUr7RitfDS9_y3

.. list-table::
  :widths: 25 25 25 25
  :header-rows: 1

  * - **Id**
    - **Sorgente**
    - **Destinatario**
    - **Descrizione**
  * - **1**
    - **User**
    - **Wallet Instance**
    - Entra sul Sito Web del Verifier e clicca sul pulsante ‘Login con Wallet’
  * - **2**
    - **User**
    - **Wallet Instance**
    - Inizio del flusso di Autorizzazione
  * - **3-4**
    - **Verifier (FE)**
    - **Verifier (BE)**     
    - Richiede la generazione di un Authorization Request contenente la Presentation Definition, i metadati del Verifier e le informazioni necessarie al Wallet per la compilazione della response
  * - **5**
    - **Verifier (FE)**
    - **-**     
    - Inserisce la referenza all’oggetto precedentemente generato all’interno di un QR Code che viene mostrato a schermo
  * - **6**
    - **Verifier (FE)**
    - **Wallet**
    - QR code viene mostrato ed è disponibile alla scansione
  * - **7**
    - **Wallet**
    - **-**
    - Scansione del QR
  * - **8**
    - **Wallet**
    - **-**
    - Estrae la Request URI dal payload del QR Code
  * - **9-10**
    - **Wallet**
    - **Verifier (BE)**          
    - Richiede il contenuto dell’Authorization Request richiamando la Request URI
  * - **11**
    - **Wallet**
    - **-**     
    - Verifica la firma della Request Object (JWT) 
  * - **12**
    - **Wallet**
    - **-**     
    - Processa il contenuto dell’oggetto e procede con l’autenticazione
  * - **13**
    - **Wallet**
    - **Verifier (BE)**     
    - Genera una Authorization Response contenente il VP Token
  * - **14**
    - **Verifier (BE)**
    - **-**     
    - Verifica la firma dell’Authorization Response
  * - **15**
    - **Verifier (BE)**
    - **-**     
    - Processa il contenuto dell’oggetto effettuando controlli di quadratura e manomissione e salva la Response sullo strato di persistenza
  * - **16**
    - **Verifier (FE)**
    - **Verifier (BE)**     
    - Richiede in Polling un Session Cookie, che sarà disponibile a valle dei controlli effettuati nello step precedente.
  * - **17**
    - **Verifier (BE)**
    - **-**     
    - Consuma il VP Token per generare un Session Cookie
  * - **18**
    - **Verifier (BE)**
    - **-**     
    - Richiede la cancellazione della sessione corrente, in quanto la transazione è stata correttamente finalizzata
  * - **19**
    - **Verifier (FE)**
    - **User**     
    - L’utente è correttamente autenticato sul Sito Web del Verifier


AuthorizationRequest
--------------------

Il FrontEnd che fa da Relying Party, per mostrare il QR Code contentente le credenziali, ha bisogno dell'oggetto AuthorizationRequest.
L'utente scansiona il codice QR utilizzando il Wallet, fornendo così gli attributi al RP (Relying Party).


.. code-block:: javascript
  POST /oid4vp HTTP/1.1
  HOST: <VERIFIER_RELYING_PARTY_HOST>

  HTTP/1.1 201 OK

Di seguito un esempio non normativo di response

.. code-block:: javascript

  {
    "alg": "ES256",
    "typ": "JWT",
    "x5c": [ "MIICajCCAdOgAwIBAgIC...20a" ],
    "kid": "e0bbf2f1-8c3a-4eab-a8ac-2e8f34db8a47",
    "trust_chain":[
      "MIICajCCAdOgAwIBAgIC...awz",
      "MIICajCCAdOgAwIBAgIC...2w3",
      "MIICajCCAdOgAwIBAgIC...sf2"
    ]
  }
  .
  { 
    "transactionId": "e9673f90-a652-4c47-8039-f60096cabafb",
    "state": "a1252f90-a652-4c47-8039-f60096cavzqw",
    "nonce": "o1923f90-a652-4c47-8039-f60096cabcza",
    "requestUri": "oid4vp-wallet://authorize?client_id=https://<VERIFIER_RELYING_PARTY_HOST>&request_uri=https://<VERIFIER_RELYING_PARTY_HOST>/oid4vp/a1252f90-a652-4c47-8039-f60096cavzqw",
    "iat": "1686823112",
    "exp": "1686823812",
    "iss": "https://<VERIFIER_RELYING_PARTY_HOST>",
    "aud": "https://<VERIFIER_RELYING_PARTY_HOST>"
  }
  .
  SIGNATURE

Header
^^^^^^

.. list-table:: 
  :widths: 25 50
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
  * - **alg**
    - Algoritmo usato per firmare il token JWT
  * - **typ**
    - Media Type del JWT
  * - **x5c**
    - Catena di certificati X.509 che contiene la chiave utilizzata per firmare il JWT
  * - **kid**
    - Key ID usata per identificare la chiave usata per firmare il token JWT. Obbligatorio se usata trust_chain
  * - **trust_chain**
    - Sequenza Entità Verificate che convalidano la conformità di un partecipante con la Federazione


Payload
^^^^^^
.. list-table:: 
  :widths: 25 50
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
  * - **transactionId**
    - Identificatore univoco della transazione
  * - **state**
    - Identificatore della AuthorizationRequest
  * - **nonce**
    - Numero casuale criptato usato per ragioni di sicurezza
  * - **requestUri**
    - Il payload del QR Code a partire dal quale il Wallet può ottenere la Request Object contentente i parametri della Authorizzation Request
  * - **iat**
    - Il timestamp di emissione del JWT
  * - **exp**
    - The timestamp di scadenza del JWT
  * - **iss**
    - Ente che ha emesso il token JWT. Verrà popolato con il Verifier URI The entity that issued the JWT. It will be populated with the Verifier URI
  * - **aud**
    - L'audience (aud) del JWT (JSON Web Token) corrisponderà al valore del campo iss (issuer)

RequestObject
-------------

Il claim "requestUri" fornito nell'oggetto AuthorizationRequest sarà il payload del QR code.
Il Wallet chiamerà il Relying Party attraverso il parametro "request_uri" che sarà fornito nel QR Code l' oggetto AuthorizationRequest.

.. code-block:: javascript
  GET /oid4vp/{id} HTTP/1.1
  HOST: <VERIFIER_RELYING_PARTY_HOST>

  HTTP/1.1 200 OK


Di seguito un esempio non normativo di response

.. code-block:: javascript

  {
    "alg": "ES256",
    "typ": "JWT",
    "x5c": [ "MIICajCCAdOgAwIBAgIC...20a" ],
    "kid": "e0bbf2f1-8c3a-4eab-a8ac-2e8f34db8a47",
    "trust_chain": [
      "MIICajCCAdOgAwIBAgIC...awz",
      "MIICajCCAdOgAwIBAgIC...2w3",
      "MIICajCCAdOgAwIBAgIC...sf2"
    ]
  }
  .
  { 
    "presentation_definition": null,
    "presentation_definition_uri": null,
    "scope": "eu.europa.ec.eudiw.pid.it.1 eu.europa.ec.eudiw.pid.de.1:give eu.europa.ec.eudiw.pid.de.1:email",
    "client_id_scheme": "entity_id",
    "client_id": "https://<VERIFIER_RELYING_PARTY_HOST>",
    "client_metadata": null,
    "client_metadata_uri": null,
    "response_mode": "direct_post.jwt",
    "response_type": "vp_token",
    "response_uri": "https://<VERIFIER_RELYING_PARTY_HOST>/oid4vp/callback",
    "redirect_uri": null,
    "nonce": "2c128e4d-fc91-4cd3-86b8-18bdea0988cb",
    "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
    "iss": "https://<VERIFIER_RELYING_PARTY_HOST>",
    "aud": "https://<VERIFIER_RELYING_PARTY_HOST>",
    "exp": 1672422065,
    "iat": 1672418465
  }
  .
  SIGNATURE


Header
^^^^^^

.. list-table:: 
  :widths: 25 50
  :header-rows: 1

  * - **Param**
    - **Description**
  * - **alg**
    - Algoritmo usato per firmare il token JWT
  * - **typ**
    - Media Type del JWT
  * - **x5c**
    - Catena di certificati X.509 che contiene la chiave utilizzata per firmare il JWT
  * - **kid**
    - Key ID usata per identificare la chiave usata per firmare il token JWT. Obbligatorio se usata trust_chain
  * - **trust_chain**
    - Sequenza Entità Verificate che convalidano la conformità di un partecipante con la Federazione


Payload
^^^^^^
.. list-table:: 
  :widths: 25 50
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
  * - **presentation_definition**
    - Stringa che contiene un Presentation Definition JSON Object che specifica quali prove richiede un Verifier. Questa stringa sarà null se è presente la presentation_definition_uri o lo scope
  * - **presentation_definition_uri**
    - Una stringa contenente una URL HTTPS che punta a una risorsa da cui è possibile recuperare un Presentation Definition JSON Object. Questo campo sarà null se il campo presentation_definition o scope è presente
  * - **scope**
    - Un alias per una Presentation Definition well-defined. Sarà utilizzato per identificare la PID Presentation Definition Request. Sarà nullo se il campo presentation_definition o presentation_definition_uri è presente
  * - **client_id_scheme**
    - Stringa che identifica lo schema del valore nel client_id. Sarà 'entity_id
  * - **client_id**
    - Identificativo del Client
  * - **client_metadata**
    - Oggetto JSON che contiene i metadati del Verifier. Sarà 'null' poiché utilizzeremo entity_id client_id_scheme. I metadati del client saranno presenti nelle dichiarazioni della trust_chain (trust_chain Statements)
  * - **client_metadata_uri**
    - Stringa contenente una URL HTTPS che punta a una risorsa da cui è possibile recuperare un oggetto JSON con i metadati del Verifier
  * - **response_mode**
    - Utilizzato per chiedere al Wallet in quale modo deve inviare la risposta. Sarà 'direct_post.jwt'
  * - **response_type**
    - Utilizzato per chiedere al Wallet cosa deve fornire nella AuthorizationResponse. Sarà 'vp_token'
  * - **response_uri**
    - URI di risposta a cui il Wallet deve inviare la risposta di autorizzazione utilizzando una richiesta POST HTTPS
  * - **redirect_uri**
    - URI di reindirizzamento a cui il Wallet deve indirizzare la risposta di autorizzazione. Sarà 'null' poiché è presente la response_uri
  * - **nonce**
    - Numero casuale criptato usato per ragioni di sicurezza
  * - **state**
    - Identificatore univoco della AuthorizationRequest
  * - **iss**
    - Ente che ha emesso il token JWT. Verrà popolato con il Verifier URI The entity that issued the JWT. It will be populated with the Verifier URI
  * - **aud**
    - L'audience (aud) del JWT (JSON Web Token) corrisponderà al valore del campo iss (issuer)
  * - **iat**
    - Il timestamp di emissione del JWT
  * - **exp**
    - Il timestamp di scadenza del JWT

