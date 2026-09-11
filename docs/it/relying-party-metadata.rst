.. include:: ../common/common_definitions.rst


Metadati della Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I metadata *openid_credential_verifier* DEVONO contenere il *client_metadata*, come incluso nei parametri mostrati di seguito. (:ref:`test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto`). Si noti che *openid_credential_verifier* è un metadata specifico di OpenID Federation Wallet Architecture (`OID-FED-WALLET`_) utilizzato per OpenID4VP quando il ``client_id`` della Relying Party è impostato con ``openid_federation``. Quando il parametro ``client_id`` della Relying Party è impostato con ``x509_hash``, i metadata vengono invece trasmessi nel parametro ``client_metadata`` fornito all'interno della richiesta.

.. list-table::
  :class: longtable
  :widths: 20 60
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
  * - **client_id**
    - DEVE contenere un URL HTTPS che identifica in modo univoco la RP. Vedi :rfc:`7591#section-3.2.1` e `OpenID Connect Dynamic Client Registration 1.0 <https://openid.net/specs/openid-connect-registration-1_0.html>`_ Sezione 3.2.
  * - **client_name**
    - Stringa leggibile che rappresenta il nome della RP. Vedi :rfc:`7591#section-2`.
  * - **logo_uri**
    - URL del logo dell’entità che verrà mostrato all’Utente durante le interazioni con l’istanza del Wallet. Vedi `OID-FED`_ Sezione 5.2.2. Il MIME type del logo DEVE essere ``application/svg``.
  * - **application_type**
    - Stringa che indica il tipo di applicazione. DEVE essere impostata al valore "*web*". Vedi `OpenID Connect Dynamic Client Registration 1.0 <https://openid.net/specs/openid-connect-registration-1_0.html>`_ Sezione 2.
  * - **request_uris**
    - JSON Array di valori ``request_uri`` che sono pre-registrati dalla RP. Questi URL DEVONO utilizzare lo schema *https*. Vedi `OpenID Connect Dynamic Client Registration 1.0 <https://openid.net/specs/openid-connect-registration-1_0.html>`_ Sezione 2.
  * - **response_uris**
    - JSON Array di stringhe URI di risposta a cui l'Istanza del Wallet DEVE inviare la Risposta di Autorizzazione utilizzando una richiesta HTTP POST come definito dalle Modalità di Risposta ``direct_post`` e ``direct_post.jwt`` (vedi `OpenID4VP`_ Draft 20 Sezioni 6.2 e 6.3).
  * - **encrypted_response_enc_values_supported**
    - Array JSON degli algoritmi di cifratura dei contenuti che il Verifier supporta per cifrare la risposta di autorizzazione quando si utilizza la modalità di risposta ``direct_post.jwt``. Vedi `OpenID4VP`_ §5.1 e §8.3.1.
  * - **vp_formats_supported**
    - Oggetto JSON che definisce i formati e i tipi di prova delle Verifiable Presentations e delle Verifiable Credentials supportati dalla RP. È composto da una lista di coppie nome/valore, dove ogni nome identifica in modo univoco un tipo supportato. La RP DEVE supportare almeno ``dc+sd-jwt``. Per le SD-JWT VC, il valore associato a ciascuna coppia nome/valore DEVE includere ``sd-jwt_alg_values`` che elenca gli algoritmi di firma accettati; per mdoc-CBOR, la valore DEVE includere ``issuerauth_alg_values`` e ``deviceauth_alg_values``. Gli header JOSE/COSE degli artefatti presentati DEVONO corrispondere a uno dei valori dichiarati. Vedi `OpenID4VP`_ Sezione 11 e Appendice B.
  * - **jwks**
    - Documento JSON Web Key Set, passato per valore, contenente le chiavi specifiche del protocollo per la Relying Party. Vedi `OID-FED`_ Sezione 5.2.1 e `JWK`_.
  * - **erasure_endpoint**
    - [CONDIZIONALE] Stringa JSON che rappresenta l'URI a cui l'Istanza del Wallet può richiedere la cancellazione degli attributi degli Utenti. Questo URL DEVE utilizzare lo schema ``https``. Alla ricezione di una richiesta di cancellazione, la Relying Party DEVE individuare univocamente uno o più Attestati Elettronici per i quali l'Utente richiede la rimozione, applicando l'identity matching.


.. note::
  I parametri ``response_uris`` e ``erasure_endpoint`` sono introdotti in questa specifica.


