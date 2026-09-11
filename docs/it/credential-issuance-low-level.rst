.. include:: ../common/common_definitions.rst


Flussi Dettagliati per l'Emissione di Attestati Elettronici
===========================================================

Issuance Flow
-------------

Il flusso di emissione degli Attestati Elettronici (Issuance Flow) è basato su [`OpenID4VCI`_] e i seguenti standard/specifiche di riferimento principali DEVONO essere supportati in aggiunta a `OpenID4VCI`_:

  * **The OAuth 2.0 Authorization Framework** [:rfc:`6749`], come raccomandato nella Sezione 3 di [`OpenID4VCI`_].
  * **Pushed Authorization Requests** (PAR) [:rfc:`9126`], come raccomandato nella Sezione 5 di [`OpenID4VCI`_].
  * **Proof Key for Code Exchange** (PKCE) [:rfc:`7636`], come raccomandato nella Sezione 5 di [`OpenID4VCI`_].
  * **JWT Authorization Requests** (JAR) [:rfc:`9101`].
  * **Rich Authorization Requests** (RAR) [:rfc:`9396`].
  * **OAuth 2.0 Attestation-Based Client Authentication** [`OAUTH-ATTESTATION-CLIENT-AUTH`_].
  * **OpenID Federation 1.0** [`OID-FED`_].

Il Credential Issuer DEVE utilizzare un *OAuth 2.0 Authorization Server* basato su :rfc:`6749` per autorizzare l'Utente a ottenere un Attestato Elettronico. I Credential Issuer DEVONO supportare:

  * **Authorization Code Flow**: Il Credential Issuer richiede l'autenticazione dell'Utente e il consenso all'Authorization Endpoint prima di raccogliere le informazioni dell'Utente per creare e rilasciare un Attestato Elettronico.
  * **Wallet Initiated Flow**: La richiesta dell'Istanza del Wallet viene inviata al Credential Issuer senza alcun input dal Credential Issuer o una terza parte (i.e. tramite supporto al Credential Offer).
  * **Immediate Issuance Flow**: Il Credential Issuer rilascia l'Attestato Elettronico direttamente in risposta alla Credential Request.

In aggiunta, i Credential Issuer POSSONO supportare:

  * **Third-Party Initiated Flow**: L'Istanza del Wallet invia la sua richiesta al Credential Issuer in base all'input fornito dal Credential Issuer o da una terza parte (per esempio una Fonte Autentica) che supporta il meccanismo di Credential Offer definito in [`OpenID4VCI`_]..

    * **Same-device Issuance Flow**: L'Utente riceve l'Attestato Elettronico sullo stesso dispositivo utilizzato per avviare il flusso.
    * **Cross-device Issuance Flow**: L'Utente riceve l'Attestato Elettronico su un dispositivo diverso da quello su cui ha avviato il flusso.

  * **Refresh Token Flow**: L'Istanza del Wallet richiede un nuovo Access Token al Token Endpoint del PID/(Q)EEA Provider.
  * **Re-issuance Flow**: A seguito di aggiornamenti ad un Attestato Elettronico già memorizzato, l'Istanza del Wallet richiede un aggiornamento dell'Attestato Elettronico al Credential Endpoint del Credential Issuer.
  * **Deferred Issuance Flow**: Il Credential Issuer potrebbe impiegare del tempo per emettere l'Attestato Elettronico richiesto, a causa delle regole di provisioning dei dati delle Fonti Autentiche, e consente al Wallet di recuperare l'Attestato Elettronico richiesto in futuro.
  * **Batch Credential Issuance Flow**: Permette l'emissione di un batch di uno o più Attestati Elettronici. Gli Attestati Elettronici emessi in batch DEVONO condividere lo stesso formato e contenere lo stesso set di attributi relativi al Titolare. Ogni Attestato DEVE contenere dati crittografici diversi per impedire la correlabilità tra gli Attestati Elettronici.


.. note::
    **Standard or Batch Credential Issuance:**

    L'Utente può configurare la Wallet Solution per emettere Attestati Elettronici in modalità batch o standard e definire la dimensione preferita del batch.

L'intero Issuance Flow può essere suddiviso in due sotto-flussi:

  - **Flusso di Richiesta dell'Utente**, che descrive le modalità attraverso le quali l'Utente può richiedere l'Attestato Elettronico. Può essere:

      1. Su iniziativa dell'Utente (**Wallet Initiated**).

      2. Su proposta del Credential Issuer (**Issuer Initiated**).

  - **Flusso di Emissione**, che descrive le interazioni tra l'Istanza del Wallet e il Credential Issuer.

Il seguente diagramma mostra il *flusso di richiesta dell'Utente*.

.. _fig_Low-Level-Flow-ITWallet-PID-QEAA-User-Request:
.. plantuml:: plantuml/credential-user-request-flow.puml
    :width: 99%
    :alt: La figura illustra il flusso di richiesta dell'Attestato Elettronico da parte dell'Utente.
    :caption: `Richiesta dell'Attestato Elettronico da parte dell'Utente - Flusso dettagliato. <https://www.plantuml.com/plantuml/svg/hLDDJzjC4BxFhnZ1WHSf8F4USq0KQDL8bTAIL5ouhDTZUyHwrzgFcFpxZjUaSGZgXzIB5Utky_4yCxa9KVcOMWCgHMTJMv37gyihW4xEMNEdRCIJxu7y2Qg02Q1mB-F1MS3GogkkSPPEyFGBrqsyDOaEiRVUzJjuuG_l7fKn575XnORLbD_qGBP4KJcKefT8tYg39MrO3tfBhspzIp7QKnsyMZViI_mgHrjXxga874Tn1b0c8bVuqnf7Lf5A_6HS3v3muXhxEIuxiXWRmZSHK7NTapLEYzCaJb0bUML5MqLs5fIEl14-YTaFL6cEheYABMvTydZFDKU1tdag1vGoW-8ekQK0uAqJiDkGnnvF7pylrXzXcGco6yCXegloxxLFGOnFk70HGY8VXbeo4K1_SIqMjBCL-pR30XdIWrVXESO29B4ZRjmpG4cJE40cqD3SfDsZ-YPRzhzisLWdZtLEWRkXFDd_ZYpCyCEkKrn9QPfc-42r9FVR6LBKb-V0VzCjvsvtavTx5mBUvpKRROzqXQSvDh4rsAcQiEVOuBU7ErVIqD-WmxQUDhQiAl8Wi5SpgyRrkU8HbMdsurrfPUK6yvNaJc6Wqwebhz3vznRj_0ytxGnxF1PvCxxz05UY-Mx-e_YDf-etuL-pQyFwEOVFc2B5A1xp0lopFzImrkFdHZwfDJy0>`_


**Passi 1.1-1.4 (Flusso Avviato dal Wallet):** L'Utente, utilizzando l'Istanza del Wallet, seleziona il Credential Issuer tra quelli elencati nella lista delle entità affidabili.

**Passi 2.1-2.3 (Flusso Avviato da una Terza Parte):** L'Utente, mentre naviga sul sito web del Credential Issuer o di una Terza Parte che supporta il meccanismo di Credential Offer (per esempio una Fonte Autentica), trova un link per ottenere un Attestato Elettronico.

**Passi 2.4-2.6 (Cross-Device):** La Credential Offer viene presentata come un codice QR. L'Utente lo scansiona con la fotocamera del dispositivo o con lo scanner integrato dell'Istanza del Wallet, attivando l'Istanza del Wallet per recuperare i parametri definiti nella :ref:`Tabella dei parametri della Credential Offer <table_credential_offer_claim>` (:ref:`WP_047-048 <wallet-credential-issuance-testcases>`).

**Passi 2.7-2.10 (Same-Device):** La Credential Offer viene presentata come un pulsante href contenente l'URL che consente all'Utente di invocare l'Istanza del Wallet utilizzando il Credential Offer Endpoint.

La Credential Offer può essere inviata per valore (utilizzando il parametro ``credential_offer``) o per riferimento (utilizzando il parametro ``credential_offer_uri``) come definito nella Sezione 4 di [`OpenID4VCI`_]. Ulteriori dettagli ed esempi non normativi sono forniti nella Sezione :ref:`credential-issuance-low-level:Flusso Credential Offer`.


Il seguente diagramma mostra il *flusso di emissione*.

.. _fig_Low-Level-Flow-ITWallet-PID-QEAA-Issuance:
.. plantuml:: plantuml/credential-issuance-flow.puml
    :width: 99%
    :alt: La figura illustra il flusso dettagliato per l'emissione degli Attestati Elettronici.
    :caption: `Emissione degli Attestati Elettronici - Flusso dettagliato. <https://www.plantuml.com/plantuml/svg/nLPVRzis47_NfpYq3xC0kTswFHN8KCVn6cEPwoNkyZB0eEMpJKGcDVwnctxw7K-MoJXAksm55WIMnFl_k-EFV6UTCCvlgqnufvNVBj1aMKrhifIrK0vUVBHeNe2muBDieJyr2zzPi5lIgZTQuGjuUINN6tTUUNneUsxq_cWk7ifkHLMXWx6Y55I9hBFFK2s1efpaC3IuHEMag61ihJzub1dz6QKTWjwXWNqXAPFn-ylP--lHQ98DDrZUmIDRa1Q2Tz0hS1k4NqXkX9DQWQ3eUk64L22TXIqwiHHEXAmu3iNRG_zdsCDRA0qAXp3zTJY2KYyHA0MvacZOo-sWFzNJWxeazUdW6gxnBu_MGUzF1L1M4fMRosKHlamZoY5yxANRm8U1Tvl-aBNw0-T86fDyIXY2WbHSroKAAYm5g0kUGnkcHk_ayelW70oiN2lXlC5MvQIHS98h8xaJbLnATmyfb1BwZ6KBZgsriWYz0nPpRsG1-AcM1krSgZoWpoPUl8K0W3RoCyU9o4PK8N6JPrwmfNosOIOgbyxGsHbCnnSFK2qylBoz7Cz6cRUX_HGWA9SSeMdcKEBu0gxq02vffq3lwiUSiIb3nOh2wpee4vBtj4PubawgDNZUQa7BYTBPFAA7bSMJjCQpVjkARvAVDX0MR_p2Ej546NIO_dOzku0_UFQRvNzJ67onijxl-MWmo9zR5FKf597YyXz1LyjsQhs0qr6A0npee82m1-WXhJsEt_vPHf5hrgZGa00kmlw-m_idPRNHUfKm4AoqwQ10f-zG0TLJQwbSbl3KZ2HnMp2EYMDchhKHoitTVOrCNPHuV9ctBCWh55SQB7ahCRLzKsRB96CGapvYASeIhPrpbM4_hmpQJVl9ZoRzb5qI32PQbNZ4u78scyBqmyqCNgiWIEAoOjh3EMiqJ7LoK4GKktkIhepQnZ3xtD1KLdXg8JWLWDC3gGb1_xMs5gqbx69Yu2qv8n2JKG8u5Xv3T4n02YgtAfsBycWvb_p29w4sa0XAhLPoxPlZX9cMZItq-Fb3dcVDxZyNhjnyhTuu-1FW_gO6L1UvdPoTBOAhkPMVCU-s_OTunIZiEWMDi_sVeJjylobUlNfLyEiapo5ZnZezmQG5iHEo4eiA8NlwVZ2ZefiR8Q6JEB310vL8hfm65xKoKYDqsjJgvagnXCLzrpqXqchSJp58kgbYv0B8u7ZG40wH95FZvBv1O3EdUWjbkBuSz3tf2tl7Ep7SPzip8VC7R-r2AD4wRJ1r7uDsoYADn5oxsIIHzqugAm1tgFX2c0pIW0UfuRlErfrVVHnbrxYMrj4g8SxGHmZx1YlXS0cPL5JybiCn3Bla27zjSASFYK5NezBIOgkujZVV_qHY66hb0g2FpdDfOV9X5aVmAzsNvCPGEmjmHYWhohRpQVM-aDdiyOWL85OCWmAnrLurjrgvHR0rbbH0Cvnj21wM_GOLXPBhDPeuks56-70splB2gj9x46iXrSFhmJlwyTlgRm00>`_


.. .. figure:: ../../images/Low-Level-Flow-ITWallet-PID-QEAA-Issuance.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/hLPVRo8t47_tfnZb7XeaKAgsJoTTTOJG2sgKq9HJNYeXnpl0A8kzjSTmwQUlFLdmGaYhg9MYxAxd_-ytC-PpOEqvhckb8piRru_ebMhI6Hbgj6Ku-nhGdu4E49LwTDzU3huB4DP9gravYsVmuOQMAxwi8nxQNdgttPlhGzc3hcjacDZ0sXeKdQr2Mq6ASfJ3o6E5badNC0aXjXv9AMyT8xWDUjZsAUKn-N8z-t8_7j-gqGhD4xoo10gGVODR0AyGVabohvcS1PrYkqVMP84um1fPLvfrpadYABM5mS-mXOzWF6f6cFuw6eDn5KBAW1Q4Nfmy30TJDstLAQbFX_TmZtz630pdVrW0KnDQdbFLpr_-HTI3_B4bNi7TCF9gC1AjmP0vIKkERmbpK20hPLsZJdLryJc5Jil1rBiDLV-8JMiGQ6arHu-joix3KOg2tqRNL14_GmT0HJ0G27UOXCRPW73UGZ2Fdlg0tnho6EPaUqfGJ2PHVuHSj_FqbyGfW1OmeUEcfw8MItgteT8rTpldqoUOJguEmEn7-F1mFPcDLGoPzHGWAvkN2CBXY71o1JTk2DTfEk3yviUUO6DonJQ5TqrMJW0-fxC4es6oIuWoNbcBjU7GA-XX7V0ehVFVUkFXiFVUr58r_p4LM-suZ1gE0IwqvjdeG-wCzA0GzgHitsLK1c-95dqIm5LkzYTyVbFMUESMdN64XVCdrW6x9xIGwcaSMLQTePqbIMaMmQtZMCPuwRNbEJytA7ES4YylyzrAQ4Uy8ez66apc_7yTSqM2GKbwZwKs1aEOIvMvonSUmshtAGz9_t3c2WQtpXhSOt0zcqrXUlVx32vi5fIuEyN2uLmqUgzsPWjV-cjS21W2ENkeVgHVC7-3GRC_AJIM2eh-2Igxw0ZcNOABtpd9Y-ntrmquDyukQ1cz42EBH8nVhn0Ae3UQQlrO8wW2N5Ude5SYX3vObqERNOWkf6cEBrvMGDcsgGoPdHZ0v9tTgiUahiEJO9XlyDtigzWwsnq0EmZiF4g3bKnAM14VYKh3b6HFzarNVdvKMXzmWrRkmGv9Go7ffRFLgHljykRhMDtZaWAdKrtNHvaFFDQQiG95DfM_bd02HFAoZt_XSUFQnCgLLPWwAArm9RNzyFrFIGmZPpb3MZPrOV_sRbOwu5_ehr5NSwOrze6zja6R7VVTycEVr2mLUlH3gWzw8JXOq6iNhTpcsHc41arkuWeUds4VGnfckq8Bx6cvH2_o3A7qYInYpq4E5hNRWbvgieTNmUVqBwxhlm40

..     PID/(Q)EAA Issuance - Detailed flow


Una volta completato il *flusso di richiesta dell'Utente*, l'Istanza del Wallet elabora i Metadata del Credential Issuer come definito nella Sezione :ref:`trust-infrastructure:Meccanismo di Trust Evaluation`. Inoltre, in caso di emissione di Credenziali in batch, l'Istanza del Wallet DEVE verificare che venga supportata l'emissione in batch tramite l'oggetto ``batch_credential_issuance`` presente nei metadati del Credential Issuer, da cui l'Istanza del Wallet può ottenere il valore ``batch_size``.

.. note::
  **Controllo della Federazione:** L'Istanza del Wallet deve verificare se il Credential Issuer è membro della Federazione, ottenendo i suoi Metadata specifici per il protocollo (:ref:`WP_046 <wallet-credential-issuance-testcases>`). Un esempio non normativo di una risposta dall'Endpoint **.well-known/openid-federation** con la **Entity Configuration** e i **Metadata** del Credential Issuer è rappresentato nella sezione :ref:`credential-issuer-entity-configuration:Entity Configuration del Fornitore di Attestati Elettronici`.

Nel caso del flusso avviato dall'Issuer, oltre al controllo della federazione definito sopra, l'Istanza del Wallet DEVE eseguire i seguenti controlli sui parametri della Credential Offer:

  * Per ogni identificativo di Attestato Elettronico contenuto nell'array ``credential_configuration_ids``, verificare se è supportato dal Credential Issuer (:ref:`WP_050 <wallet-credential-issuance-testcases>`).
  * L'identificativo dell'Authorization Server (se presente) è contenuto nel parametro ``authorization_servers`` dei Metadata del Credential Issuer (:ref:`WP_049 <wallet-credential-issuance-testcases>`).


**Passi 1-2 (`PAR Request`)**: L'Istanza del Wallet:

  * Crea un nuovo `PKCE code verifier`, una prova di possesso dell'Attestato di Unità di Wallet e un parametro ``state`` per la *Pushed Authorization Request* (:ref:`WP_052 <wallet-credential-issuance-testcases>`).
  * Fornisce al PAR Endpoint del Credential Issuer i parametri precedentemente elencati, utilizzando il parametro ``request`` (di seguito `Request Object`) secondo la Sezione 3 di :rfc:`9126` per prevenire l'attacco di scambio del `Request URI` (:ref:`WP_052 <wallet-credential-issuance-testcases>`). La Pushed Authorization Request consente l'autenticazione del client prima di qualsiasi interazione dell'Utente. Questo passaggio permette il rifiuto anticipato di richieste illegittime, prevenendo efficacemente attacchi di spoofing, manomissione e uso improprio delle richieste di autorizzazione.
  * DEVE creare il ``code_verifier`` con una stringa casuale con sufficiente entropia utilizzando i caratteri non riservati con una lunghezza minima di 43 caratteri e una lunghezza massima di 128 caratteri, rendendo impraticabile per un attaccante indovinarne il valore. Il valore DEVE essere generato seguendo la raccomandazione nella Sezione 4.1 di :rfc:`7636` (:ref:`WP_052a <wallet-credential-issuance-testcases>`).
  * Firma questa richiesta utilizzando la chiave privata creata durante la fase di configurazione per ottenere l'Attestato di Unità di Wallet. La relativa chiave pubblica attestata dal Fornitore di Wallet viene fornita all'interno del claim ``cnf.jwk`` dell'Attestato di Unità di Wallet (:ref:`WP_052c <wallet-credential-issuance-testcases>`).
  * DEVE utilizzare i parametri ``OAuth-Client-Attestation`` e ``OAuth-Client-Attestation-PoP`` secondo OAuth 2.0 Attestation-based Client Authentication [`OAUTH-ATTESTATION-CLIENT-AUTH`_], poiché in questo flusso il Pushed Authorization Endpoint è un endpoint protetto (:ref:`WP_052b <wallet-credential-issuance-testcases>`).
  * Specifica i tipi di Credenziali richieste utilizzando il parametro ``authorization_details`` [RAR :rfc:`9396`] e/o il parametro ``scope`` (:ref:`WP_052d <wallet-credential-issuance-testcases>`).

.. note::
  JAR [:rfc:`9101`] è obbligatorio in questa specifica tecnica per garantire l'integrità end-to-end della richiesta di autorizzazione e di tutti i parametri inclusi nel Request Object.
  Tuttavia, la Wallet Instance può interagire con Credential Issuer cross-border i cui Authorization Server non seguono questa specifica e potrebbero non supportare l'implementazione di JAR.
  Per gestire questo scenario, la Wallet Instance DOVREBBE verificare il parametro `require_signed_request_object` nei metadata dell'Authorization Server e decidere in base ad esso se inviare i parametri nel signed Request Object o meno. Per interoperabilità, la Wallet Instance PUÒ duplicare gli stessi parametri nel corpo della richiesta. La Sezione 10.7 di :rfc:`9101` fornisce i requisiti di sicurezza su come gestire correttamente questa duplicazione.

.. note::
   Per l'Autenticazione eID Substantial con Verifica MRTD, l'oggetto ``authorization_details`` DEVE contenere il valore ``"it_l2+document_proof"``. Per le specifiche complete del protocollo, vedere :ref:`credential-issuance-l2plus:Autenticazione eID Substantial con Verifica MRTD per Emissione IT-Wallet ID`.

Il Credential Issuer esegue i seguenti controlli alla ricezione della `PAR Request`:

    1. DEVE validare la firma del `Request Object` utilizzando l'algoritmo specificato nel parametro ``alg`` dell'header (:rfc:`9126`, :rfc:`9101`) e la chiave pubblica recuperata dall'Attestato di Unità di Wallet (``cnf.jwk``) referenziato nel `Request Object`, utilizzando il parametro ``kid`` dell'header JWT.
    2. DEVE verificare che l'algoritmo utilizzato per firmare la richiesta nell'header ``alg`` sia uno di quelli elencati nella Sezione :ref:`algorithms:Algoritmi Crittografici`.
    3. DEVE verificare che il ``client_id`` nel body della `PAR Request` corrisponda al claim ``client_id`` incluso nel `Request Object`.
    4. DEVE verificare che il claim ``iss`` nel `Request Object` corrisponda al claim ``client_id`` nel `Request Object` (:rfc:`9126`, :rfc:`9101`).
    5. DEVE verificare che il claim ``aud`` nel `Request Object` sia uguale all'identificativo del Credential Issuer (:rfc:`9126`, :rfc:`9101`).
    6. DEVE rifiutare la `PAR Request`, se contiene il parametro ``request_uri`` (:rfc:`9126`).
    7. DEVE verificare che il `Request Object` contenga tutti i parametri obbligatori i cui valori sono validati secondo la :ref:`Tabella dei parametri HTTP <table_request_object_claim>` [derivata da :rfc:`9126`].
    8. DEVE verificare che il `Request Object` non sia scaduto, controllando il claim ``exp``.
    9. DEVE verificare che il `Request Object` sia stato emesso in un momento precedente al valore esposto nel claim ``iat``. DOVREBBE rifiutare la richiesta se il claim ``iat`` è lontano dall'ora corrente (:rfc:`9126`) di più di `5` minuti.
    10. DEVE verificare che il claim ``jti`` nel `Request Object` non sia stato utilizzato in precedenza dall'Istanza del Wallet identificata dal ``client_id``. Ciò consente al Credential Issuer di mitigare gli attacchi di replay (:rfc:`7519`).
    11. DEVE validare il parametro ``OAuth-Client-Attestation-PoP`` in base alla Sezione 5 di [`OAUTH-ATTESTATION-CLIENT-AUTH`_].
    12. DEVE verificare, se presente, la validità dell’``issuer_state`` e la coerenza con il ``credential_configuration_id`` richiesto nel Request Object.


Di seguito un esempio non normativo di `PAR Request`.

.. code-block:: http

    POST /as/par HTTP/1.1
    Host: eaa-provider.example.org
    Content-Type: application/x-www-form-urlencoded
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtpZCI6IjBiNDk4ZGRlMDkxNzJhZGE3MDFkMDdlYjZmOTg2N2FkIiwidHlwIjoib2F1dGgtY2xpZW50LWF0dGVzdGF0aW9uK2p3dCIsIng1YyI6WyJNSUlEcWpDQ0FwS2dBd0lCQWdJRVNMTkV2REEgLi4uIiwiTUlJQ3d6Q0NBYXNDQ1FDS1Z5OWVLanZpK2pBIC4uLiIsIk1JSURURENDQWpTZ0F3SUJBZ0lKQVBsblFZSC4uLiJdfQ.eyJzdWIiOiJodHRwczovL3dhbGxldC1zb2x1dGlvbi5leGFtcGxlLm9yZy9kZDc2MmU2ZjhiNjEzMTkzIiwiY25mIjp7Imp3ayI6eyJjcnYiOiJQLTI1NiIsImt0eSI6IkVDIiwieCI6IjRITnB0SS14cjJwanlSSktHTW56NFdtZG5RRF91SlNxNFI5NU5qOThiNDQiLCJ5IjoiTElablNCMzl2RkpoWWdTM2s3alhFNHIzLUNvR0ZRd1p0UEJJUnFwTmxyZyJ9fSwid2FsbGV0X25hbWUiOiJXYWxsZXRfdjEiLCJ3YWxsZXRfbGluayI6Imh0dHBzOi8vZXhhbXBsZS5jb20vd2FsbGV0L2RldGFpbF9pbmZvLmh0bWwiLCJ3YWxsZXRfdmVyc2lvbiI6IjEuMC4wIiwiY2xpZW50X3N0YXR1cyI6eyJzdGF0dXMiOnsic3RhdHVzX2xpc3QiOnsiaWR4IjoxMzM3LCJ1cmkiOiJodHRwczovL3Jldm9jYXRpb25fdXJsL3dpYS1zdGF0dXNsaXN0cy80MiJ9fSwiZXhwIjoxMzAzNDk3NzgwfSwiZXhwIjoxNzQwMTU4MTY3fQ.XOv01xkHC-_h-bZFcXgkEffs3xk8WezKWs8KA4yZD8aNabDq81Y80wkOuHCM25zSGHbABszaSDsyYaJv9bh40w
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUzI1NiIsInR5cCI6Im9hdXRoLWNsaWVudC1hdHRlc3RhdGlvbi1wb3Arand0In0.ew0KICAiaXNzIjogIiA0N2I5ODIzNjk3OTFkMDgwMDNhNzI4M2YwNTljYjBkMSIsDQogICJhdWQiOiAiaHR0cHM6Ly9hcy5leGFtcGxlLmNvbSIsDQogICJqdGkiOiAiZDI1ZDAwYWItNTUyYi00NmZjLWFlMTktOThmNDQwZjI1MDY0IiwNCiAgImlhdCI6IDE3NDAxNTg2MTcNCn0.B0KOkGi9vMxf3H2Y8rrF-mdLNsuluTvAUbjFfL1Hi-gdaPW7-8ziS9uVh7aTnSAHKWzMfkZLv5q-bxhkglR4PA

    client_id=$thumprint-of-the-jwk-in-the-cnf-wallet-instance-attestation$&
    request=$SIGNED-JWT

Di seguito un esempio non normativo dell'header e del body della prova di possesso dell'Attestato di Unità di Wallet (WIA-PoP):

.. literalinclude:: ../../examples/wa-pop-header.json
  :language: JSON

.. literalinclude:: ../../examples/wa-pop-payload.json
  :language: JSON


Di seguito un esempio non normativo del `Request Object` firmato senza codifica e firma applicata:

.. literalinclude:: ../../examples/request-object-header.json
  :language: JSON

.. literalinclude:: ../../examples/request-object-payload.json
  :language: JSON


.. note::
  **Controllo della Federazione**: Il Credential Issuer DEVE verificare che il Fornitore di Wallet faccia parte della federazione.


.. note::
  Il Credential Issuer DEVE validare la firma dell'Attestato di Unità di Wallet e che non sia scaduto.

**Passo 3 (`PAR Response`)**: Il Credential Issuer fornisce un valore ``request_uri`` monouso. Il valore ``request_uri`` emesso DEVE essere vincolato all'identificativo del client (``client_id``) che è stato fornito nel `Request Object`.


.. note::
  L'entropia del ``request_uri`` DEVE essere sufficientemente grande. L'adeguata brevità della validità e l'entropia del ``request_uri`` dipendono dal calcolo del rischio basato sul valore della risorsa protetta. Il tempo di validità DOVREBBE essere inferiore a un minuto e il ``request_uri`` DEVE includere un valore casuale crittografico di 128 bit o più (:rfc:`9101`). L'intero ``request_uri`` NON DOVREBBE superare i 512 caratteri ASCII per i seguenti due motivi principali (:rfc:`9101`):

    1. Molti telefoni sul mercato ancora non accettano payload di grandi dimensioni. La restrizione è tipicamente di 512 o 1024 caratteri ASCII.
    2. Su una connessione lenta come una connessione mobile 2G, un URL grande causerebbe una risposta lenta; pertanto, l'uso di tale URL non è consigliabile dal punto di vista dell'esperienza utente.

Il Credential Issuer restituisce il ``request_uri`` emesso all'Istanza del Wallet. Un esempio non normativo della risposta è mostrato di seguito.

.. code-block:: http

  HTTP/1.1 201 Created
  Cache-Control: no-cache, no-store
  Content-Type: application/json

.. literalinclude:: ../../examples/par-response.json
  :language: JSON

**Passi 4-5 (`Authorization Request`)**: L'Istanza del Wallet invia una richiesta di autorizzazione all'Authorization Endpoint del Credential Issuer (:ref:`WP_053 <wallet-credential-issuance-testcases>`). Poiché parti del contenuto di questa `Authorization Request`, ad esempio il valore del parametro ``code_challenge``, sono unici per una particolare `Authorization Request`, l'Istanza del Wallet DEVE utilizzare un valore ``request_uri`` una sola volta (:rfc:`9126`) come da (:ref:`WP_053a <wallet-credential-issuance-testcases>`). Il Credential Issuer esegue i seguenti controlli alla ricezione della `Authorization Request`:

    1. DEVE trattare i valori ``request_uri`` come monouso e DEVE rifiutare una richiesta scaduta. Tuttavia, PUÒ consentire richieste duplicate causate da un Utente che ricarica/aggiorna il proprio user-agent (derivato da :rfc:`9126`).
    2. DEVE identificare la richiesta come risultato del PAR inviato (derivato da :rfc:`9126`).
    3. DEVE rifiutare tutte le `Authorization Request` che non contengono il parametro ``request_uri``, poiché il PAR è l'unico modo per passare la `Authorization Request` dall'Istanza del Wallet (derivato da :rfc:`9126`).


.. code-block:: http

    GET /authorize?client_id=$thumprint-of-the-jwk-in-the-cnf-wallet-instance-attestation$&request_uri=urn%3Aietf%3Aparams%3Aoauth%3Arequest_uri%3Abwc4JK-ESC0w8acc191e-Y1LTC2 HTTP/1.1
    Host: eaa-provider.example.org


.. note::
   **Autenticazione dell'Utente e Consenso**: Il PID Provider esegue l'autenticazione dell'Utente basata sullo schema CieID con Livello di Garanzia Alto (CIE L3), mentre l'EAA Provider di IT-Wallet ID, oltre a CieID LoA High, supporta anche l'Autenticazione eID Substantial con Verifica MRTD come definita in :ref:`credential-issuance-l2plus:Autenticazione eID Substantial con Verifica MRTD per Emissione IT-Wallet ID`.
   Il (Q)EAA Provider esegue l'autenticazione dell'Utente richiedendo un PID o un IT-Wallet ID valido all'Istanza del Wallet. Il (Q)EAA Provider DEVE utilizzare [`OpenID4VP`_] per richiedere la presentazione del PID o dell'IT-Wallet ID. In questa circostanza, il (Q)EAA Provider agisce come una Relying Party, fornendo la richiesta di presentazione all'Istanza del Wallet. L'Istanza del Wallet DEVE avere un PID o un IT-Wallet ID valido, ottenuto in precedenza. Durante questo passaggio, i Credential Issuer POSSONO chiedere i dettagli di contatto dell'Utente (ad esempio, il loro indirizzo email) per inviare notifiche sugli Attestati Elettronici emessi.


**Passi 6-7 (`Authorization Response`)**: Il Credential Issuer invia un ``code`` di autorizzazione insieme ai parametri ``state`` e ``iss`` all'Istanza del Wallet. L'Istanza del Wallet esegue i seguenti controlli sulla `Authorization Response`:

    1. DEVE verificare che la `Authorization Response` contenga tutti i parametri definiti secondo la :ref:`Tabella dei parametri della Risposta HTTP <table_http_response_claim>` (:ref:`WP_054 <wallet-credential-issuance-testcases>`).
    2. DEVE verificare che il valore restituito dal Credential Issuer per il parametro ``state`` sia uguale al valore inviato dall'Istanza del Wallet nel `Request Object` (:rfc:`6749`) come specificato in :ref:`WP_054a <wallet-credential-issuance-testcases>`.
    3. DEVE verificare che l'URL del Credential Issuer nel parametro ``iss`` sia uguale all'identificativo URL previsto del Credential Issuer con cui l'Istanza del Wallet ha iniziato la comunicazione (:rfc:`9027`) come specificato in :ref:`WP_054b <wallet-credential-issuance-testcases>`.

.. note::
    L'URI di reindirizzamento dell'Istanza del Wallet è un `universal link` o `app link` registrato con il sistema operativo locale, quindi quest'ultimo lo risolverà e passerà la risposta all'Istanza del Wallet.

.. code-block:: http

    HTTP/1.1 302 Found
    Location: https://start.wallet.example.org?code=SplxlOBeZQQYbYS6WxSbIA&state=fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd&iss=https%3A%2F%2Feaa-provider.example.org

**Passi 8-9 (`DPoP Proof` per il Token Endpoint)**: L'Istanza del Wallet DEVE creare una nuova coppia di chiavi e un nuovo JWT di `DPoP proof` seguendo le istruzioni fornite nella Sezione 4 di (:rfc:`9449`) per la richiesta di token al Credential Issuer (:ref:`WP_055b <wallet-credential-issuance-testcases>`). Il JWT di `DPoP proof` è firmato utilizzando la chiave privata per DPoP creata dall'Istanza del Wallet per questo scopo (:ref:`WP_055c <wallet-credential-issuance-testcases>`). DPoP associa l'Access Token, e opzionalmente il Refresh Token, a una determinata Istanza del Wallet (:rfc:`9449`) e mitiga l'uso improprio di token persi o rubati al Credential Endpoint.

**Passo 10 (`Token Request`):** L'Istanza del Wallet invia una richiesta di token al Token Endpoint del Credential Issuer con un JWT di *DPoP proof* e i parametri: ``code``, ``code_verifier`` e OAuth 2.0 Attestation based Client Authentication (``OAuth-Client-Attestation`` e ``OAuth-Client-Attestation-PoP``) come specificato in :ref:`WP_055 <wallet-credential-issuance-testcases>`.

L'``OAuth-Client-Attestation`` è firmato utilizzando la chiave privata associata all'Istanza del Wallet (:ref:`WP_055a <wallet-credential-issuance-testcases>`). La relativa chiave pubblica attestata dal Fornitore di Wallet è fornita all'interno dell'Attestato di Unità di Wallet (claim ``cnf.jwk``) come specificato in :ref:`WP_055d <wallet-credential-issuance-testcases>`. Il Credential Issuer esegue i seguenti controlli sulla `Token Request`:

   1. DEVE assicurarsi che il ``code`` di autorizzazione sia emesso per l'Istanza del Wallet autenticata (:rfc:`6749`) e non sia stato replicato.
   2. DEVE assicurarsi che il ``code`` di autorizzazione sia valido e non sia stato utilizzato in precedenza (:rfc:`6749`).
   3. DEVE assicurarsi che il ``redirect_uri`` corrisponda al valore incluso nel precedente `Request Object` (vedi Sezione 3.1.3.1. di [`OIDC`_]).
   4. DEVE validare il JWT di `DPoP proof`, secondo la Sezione 4.3 di (:rfc:`9449`).
   5. DEVE verificare il parametro ``code_verifier`` secondo il meccanismo PKCE, assicurandosi che corrisponda al ``code_challenge`` associato al codice di autorizzazione come definito nella Sezione 4.6 di :rfc:`7636`; in caso contrario, la richiesta DEVE essere rifiutata (:ref:`CI_061a <test-plans-credential-issuer:matrice dei test per il credential issuer>`).

.. code-block:: http

    POST /token HTTP/1.1
    Host: eaa-provider.example.org
    Content-Type: application/x-www-form-urlencoded
    DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6IkVDIiwieCI6IjR2dDhNdEFISmlsMzBDNnpUTmt2c0VVcnlHTEUtQW5BNkc5LV8xa3l5Rk0iLCJ5IjoiTWdiNTFfbjNSRjNtbHNtS3dMd0xtRUFqVmlJM3Q1bTVWNTI2MFA5MzR3RSIsImNydiI6IlAtMjU2In19.eyJqdGkiOiItQndDM0VTYzZhY2MybFRjIiwiaHRtIjoiR0VUIiwiaHR1IjoiaHR0cHM6Ly9yZXNvdXJjZS5leGFtcGxlLm9yZy9wcm90ZWN0ZWRyZXNvdXJjZSIsImlhdCI6MTU2MjI2MjYxOH0.3Tp1ZlZ05PQYeZUHhiZwaQ1etqnwYwoiJHFR_JHb32381lMJL-8o2rE3VZ8X3yuqrGFfCVeP90Ln4J5r8ASIBg
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtpZCI6IjBiNDk4ZGRlMDkxNzJhZGE3MDFkMDdlYjZmOTg2N2FkIiwidHlwIjoib2F1dGgtY2xpZW50LWF0dGVzdGF0aW9uK2p3dCIsIng1YyI6WyJNSUlEcWpDQ0FwS2dBd0lCQWdJRVNMTkV2REEgLi4uIiwiTUlJQ3d6Q0NBYXNDQ1FDS1Z5OWVLanZpK2pBIC4uLiIsIk1JSURURENDQWpTZ0F3SUJBZ0lKQVBsblFZSC4uLiJdfQ.eyJzdWIiOiJodHRwczovL3dhbGxldC1zb2x1dGlvbi5leGFtcGxlLm9yZy9kZDc2MmU2ZjhiNjEzMTkzIiwiY25mIjp7Imp3ayI6eyJjcnYiOiJQLTI1NiIsImt0eSI6IkVDIiwieCI6IjRITnB0SS14cjJwanlSSktHTW56NFdtZG5RRF91SlNxNFI5NU5qOThiNDQiLCJ5IjoiTElablNCMzl2RkpoWWdTM2s3alhFNHIzLUNvR0ZRd1p0UEJJUnFwTmxyZyJ9fSwid2FsbGV0X25hbWUiOiJXYWxsZXRfdjEiLCJ3YWxsZXRfbGluayI6Imh0dHBzOi8vZXhhbXBsZS5jb20vd2FsbGV0L2RldGFpbF9pbmZvLmh0bWwiLCJ3YWxsZXRfdmVyc2lvbiI6IjEuMC4wIiwiY2xpZW50X3N0YXR1cyI6eyJzdGF0dXMiOnsic3RhdHVzX2xpc3QiOnsiaWR4IjoxMzM3LCJ1cmkiOiJodHRwczovL3Jldm9jYXRpb25fdXJsL3dpYS1zdGF0dXNsaXN0cy80MiJ9fSwiZXhwIjoxMzAzNDk3NzgwfSwiZXhwIjoxNzQwMTU4MTY3fQ.XOv01xkHC-_h-bZFcXgkEffs3xk8WezKWs8KA4yZD8aNabDq81Y80wkOuHCM25zSGHbABszaSDsyYaJv9bh40w
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUzI1NiIsInR5cCI6Im9hdXRoLWNsaWVudC1hdHRlc3RhdGlvbi1wb3Arand0In0.ew0KICAiaXNzIjogIiA0N2I5ODIzNjk3OTFkMDgwMDNhNzI4M2YwNTljYjBkMSIsDQogICJhdWQiOiAiaHR0cHM6Ly9hcy5leGFtcGxlLmNvbSIsDQogICJqdGkiOiAiZDI1ZDAwYWItNTUyYi00NmZjLWFlMTktOThmNDQwZjI1MDY0IiwNCiAgImlhdCI6IDE3NDAxNTg2MTcNCn0.B0KOkGi9vMxf3H2Y8rrF-mdLNsuluTvAUbjFfL1Hi-gdaPW7-8ziS9uVh7aTnSAHKWzMfkZLv5q-bxhkglR4PA

    grant_type=authorization_code
    &code=SplxlOBeZQQYbYS6WxSbIA
    &code_verifier=dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk
    &redirect_uri=https://start.wallet.example.org/cb

**Passo 11 (`Token Response`)**: Il Credential Issuer valida la richiesta. In caso di successo, l'Issuer fornisce all'Istanza del Wallet un Access Token e, opzionalmente, un Refresh Token, entrambi associati alla chiave DPoP.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store

.. literalinclude:: ../../examples/token-response.json
  :language: JSON

Un esempio non normativo dell'Access Token DPoP è fornito di seguito.

.. literalinclude:: ../../examples/at-dpop-header.json
  :language: JSON

.. literalinclude:: ../../examples/at-dpop-payload.json
  :language: JSON

Un esempio non normativo del Refresh Token DPoP è fornito di seguito.

.. literalinclude:: ../../examples/rt-dpop-header.json
  :language: JSON

.. literalinclude:: ../../examples/rt-dpop-payload.json
  :language: JSON

**Passo 12 (`Nonce Request`)**: Secondo la Sezione 7.1 di [`OpenID4VCI`_], l'Istanza del Wallet invia una richiesta HTTP POST al Nonce Endpoint per ottenere un nuovo ``c_nonce`` che può essere utilizzato per creare la prova di possesso del materiale crittografico per la successiva richiesta al Credential Endpoint (:ref:`WP_056a <wallet-credential-issuance-testcases>`).

Di seguito è riportato un esempio non normativo di una `Nonce Request`:

.. code-block:: http

    POST /nonce HTTP/1.1
    Host: eaa-provider.example.org
    Content-Length: 0

**Passo 13 (`Nonce Response`)**: Il Credential Issuer fornisce il ``c_nonce`` all'Istanza del Wallet. Il parametro ``c_nonce`` è una stringa, che DEVE essere imprevedibile e viene utilizzata successivamente dall'Istanza del Wallet nel Passo 16 per creare la(e) prova(e) di possesso della chiave (claim ``proofs``) ed è la principale contromisura contro l'attacco di replay della prova della chiave.
Si noti che il valore ``c_nonce`` ricevuto può essere utilizzato per creare la(e) prova(e) finché l'Issuer
fornisce all'Istanza del Wallet un nuovo valore ``c_nonce``.

Di seguito è riportato un esempio non normativo di una `Nonce Response`:

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store

.. literalinclude:: ../../examples/nonce-response.json
  :language: JSON


**Passo 14 (DPoP Proof per il Credential Endpoint)**: L'Istanza del Wallet crea un JWT DPoP Proof utilizzando la stessa chiave del **Passo 8** e secondo la Sezione 4 di (:rfc:`9449`) (:ref:`WP_056b <wallet-credential-issuance-testcases>`).

.. note::
   Se l'Istanza del Wallet richiede l'emissione in batch di Attestati Elettronici, il flusso prosegue con il **Passo 17**. In caso contrario, vengono eseguiti i passi **15-16**.

**Passo 15 (Prova di Possesso della Credenziale)**: L'Istanza del Wallet per la richiesta delle Credenziali Digitali crea una prova di possesso con il ``c_nonce`` ottenuto nel **Passo 13** utilizzando la chiave privata utilizzata per il DPoP. Il valore del ``jwk`` nel parametro proof DEVE essere uguale alla chiave pubblica referenziata nel DPoP (:ref:`WP_056c <wallet-credential-issuance-testcases>`).

**Passo 16 (`Credential Request`)**: L'Istanza del Wallet invia una richiesta per l'Attestato Elettronico al Credential Endpoint. Questa richiesta DEVE includere l'Access Token, il JWT di `DPoP proof`, il tipo di Attestato Elettronico, la prova (che dimostra il possesso del materiale crittografico) come specificato in :ref:`WP_056 <wallet-credential-issuance-testcases>`. Il parametro ``proofs`` DEVE essere un oggetto che contiene la prova di possesso del materiale crittografico a cui sarà associato l'Attestato Elettronico emesso. Per verificare la prova, il Credential Issuer conduce i seguenti controlli al Credential Endpoint:

 1. La prova JWT DEVE includere tutti i claim richiesti come specificato nella tabella della Sezione :ref:`credential-issuance-endpoint:Token Request`.
 2. La prova della chiave DEVE essere esplicitamente tipizzata utilizzando i parametri dell'header come definito per il rispettivo tipo di prova.
 3. Il parametro dell'header ``alg`` DEVE indicare un algoritmo di firma digitale asimmetrica registrato e NON DEVE essere impostato su `none`.
 4. La firma sulla prova della chiave DEVE essere verificata utilizzando la chiave pubblica specificata nel parametro dell'header.
 5. Il parametro dell'header NON DEVE contenere una chiave privata.
 6. La firma sul JWT di Key Attestation, come valore del parametro di intestazione ``key_attestation``, DEVE essere verificata utilizzando la chiave pubblica del Wallet Provider, identificata dal parametro di intestazione kid all’interno del JWT di Key Attestation.
 7. Se un valore ``c_nonce`` è stato precedentemente fornito dal server, il claim ``nonce`` nel JWT DEVE corrispondere a questo valore ``c_nonce``. Inoltre, l'istante di creazione del JWT, come indicato dal claim ``iat`` o da un timestamp gestito dal server tramite il claim ``nonce``, DEVE essere all'interno di una finestra temporale accettabile come determinato dal server.


.. note::
  Il Credential Issuer DEVE registrare tutti gli Attestati Elettronici emessi per la loro successiva revoca, se necessario.


.. note::
  È RACCOMANDATO che la chiave pubblica contenuta nel ``jwt_proof`` sia generata specificamente per l'Attestato Elettronico richiesto (nuova chiave crittografica) per garantire che diversi Attestati Elettronici emessi non condividano la stessa chiave pubblica, rimanendo così non collegabili tra loro.


Un esempio non normativo della `Credential Request` è fornito di seguito.


.. code-block:: http

  POST /credential HTTP/1.1
    Host: eaa-provider.example.org
  Content-Type: application/json
  Authorization: DPoP Kz~8mXK1EalYznwH-LC-1fBAo.4Ljp~zsPE_NeO.gxU
  DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6Ik
      VDIiwieCI6Imw4dEZyaHgtMzR0VjNoUklDUkRZOXpDa0RscEJoRjQyVVFVZldWQVdCR
      nMiLCJ5IjoiOVZFNGpmX09rX282NHpiVFRsY3VOSmFqSG10NnY5VERWclUwQ2R2R
      1JEQSIsImNydiI6IlAtMjU2In19.eyJqdGkiOiJlMWozVl9iS2ljOC1MQUVCIiwiaHRtIj
      oiR0VUIiwiaHR1IjoiaHR0cHM6Ly9yZXNvdXJjZS5leGFtcGxlLm9yZy9wcm90ZWN0Z
      WRyZXNvdXJjZSIsImlhdCI6MTU2MjI2MjYxOCwiYXRoIjoiZlVIeU8ycjJaM0RaNTNF
      c05yV0JiMHhXWG9hTnk1OUlpS0NBcWtzbVFFbyJ9.2oW9RP35yRqzhrtNP86L-Ey71E
      OptxRimPPToA1plemAgR6pxHF8y6-yqyVnmcw6Fy1dqd-jfxSYoMxhAJpLjA

.. literalinclude:: ../../examples/credential-request.json
  :language: JSON

Dove un esempio non normativo del contenuto decodificato del parametro ``jwt`` è rappresentato di seguito, senza codifica e firma.

.. literalinclude:: ../../examples/credential-jwt-proof-header.json
  :language: JSON

.. literalinclude:: ../../examples/credential-jwt-proof-payload.json
  :language: JSON

**Passo 17 (Generazione di nuove chiavi per le Credenziali Digitali)**: L'Istanza del Wallet genera N nuove coppie di chiavi per le Credenziali, dove il numero di coppie di chiavi (N) è determinato dal valore definito in ``batch_size`` (:ref:`WP_058a <wallet-credential-issuance-testcases>`).

**Passo 18 (Prove di possesso delle credenziali)**: L'istanza del Wallet DEVE generare N *key proofs* utilizzando il ``c_nonce`` fornito nel **Passo 13** e una per ogni Credenziale presente nel batch. Il numero di *key proofs* (N) è definito dal valore ``batch_size`` (:ref:`WP_058b <wallet-credential-issuance-testcases>`).

.. note::
  Il valore ``c_nonce`` in tutte le proof jwt è identico e non è necessario ottenere valori del nonce diversi.


**Passo 19 (Batch Credential Request)**: L'Istanza del Wallet invia una richiesta per il batch di Credenziali Digitali al Credential Endpoint. Questa richiesta DEVE includere l'Access Token, il JWT DPoP Proof, il tipo di Credenziale e le proofs (che dimostrano il possesso delle chiavi). Il parametro ``proofs`` DEVE essere impostato utilizzando un oggetto JSON contenente due o più prove di possesso dei materiali crittografici a cui sarà associato il batch di Credenziali Digitali emesso. Per verificare le proofs, il Credential Issuer, oltre ai controlli definiti al **Passo 16**, deve assicurarsi che l'attributo ``jwk`` in ogni proof sia univoco (:ref:`WP_058 <wallet-credential-issuance-testcases>`).


.. code-block:: http

    POST /credential HTTP/1.1
    Host: eaa-provider.example.org
    Content-Type: application/json
    Authorization: DPoP Kz~8mXK1EalYznwH-LC-1fBAo.4Ljp~zsPE_NeO.gxU
    DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6Ik
      VDIiwieCI6Imw4dEZyaHgtMzR0VjNoUklDUkRZOXpDa0RscEJoRjQyVVFVZldWQVdCR
      nMiLCJ5IjoiOVZFNGpmX09rX282NHpiVFRsY3VOSmFqSG10NnY5VERWclUwQ2R2R
      1JEQSIsImNydiI6IlAtMjU2In19.eyJqdGkiOiJlMWozVl9iS2ljOC1MQUVCIiwiaHRtIj
      oiR0VUIiwiaHR1IjoiaHR0cHM6Ly9yZXNvdXJjZS5leGFtcGxlLm9yZy9wcm90ZWN0Z
      WRyZXNvdXJjZSIsImlhdCI6MTU2MjI2MjYxOCwiYXRoIjoiZlVIeU8ycjJaM0RaNTNF
      c05yV0JiMHhXWG9hTnk1OUlpS0NBcWtzbVFFbyJ9.2oW9RP35yRqzhrtNP86L-Ey71E
      OptxRimPPToA1plemAgR6pxHF8y6-yqyVnmcw6Fy1dqd-jfxSYoMxhAJpLjA

.. literalinclude:: ../../examples/batch-credential-request.json
  :language: JSON


Il contenuto decodificato degli elementi ``jwt`` nell'array ``jwt`` è simile a quanto spiegato nel **Passo 16**.


**Passi 20-24 (Credential Response)**: Il Credential Issuer DEVE convalidare il *JWT DPoP Proof* in base alle istruzioni definite all'interno della Sezione 4.3 di (:rfc:`9449`) e verificare se l'*Access Token* è valido e idoneo per la Credenziale richiesta. Il Credential Issuer DEVE convalidare tutte le prove fornite nel parametro ``proofs`` (**Passo 15** e **Passo 18**) a cui le nuove Credenziali DEVONO essere vincolate, secondo quanto riportato nell'Appendice F1 di `OpenID4VCI`_. Se tutti i controlli hanno esito positivo, il Credential Issuer restituisce la Credenziale emessa all'interno del parametro ``credentials``. Il numero di elementi nell'array ``credentials`` corrisponde al numero di chiavi fornite dall'Istanza del Wallet tramite il parametro ``proofs`` (**Passo 16** e **Passo 19**). L'Istanza del Wallet DEVE eseguire i seguenti controlli prima di procedere con l'archiviazione sicura delle Credenziali:

    1. DEVE verificare che il PID/(Q)EAA contenuto nella `Credential Response` contenga tutti i parametri obbligatori e i valori siano validati secondo la :ref:`Tabella dei parametri della Credential Response <table_credential_response_claim>` (:ref:`WP_059 <wallet-credential-issuance-testcases>`).
    2. DEVE verificare l'integrità dell'Attestato Elettronico verificando la firma utilizzando l'algoritmo specificato nel parametro dell'header ``alg`` di SD-JWT (:ref:`credential-data-model:Modello di Dati degli Attestati Elettronici`) e la chiave pubblica che è identificata utilizzando l'header ``kid`` dell'SD-JWT (:ref:`WP_062a <wallet-credential-issuance-testcases>`).
    3. DEVE verificare che l'Attestato o gli Attestati Elettronici ricevuti (nel claim ``credential``) corrispondano al tipo di Attestato Elettronico richiesto e sia conforme allo schema specifico di quell'Attestato Elettronico definito in :ref:`credential-data-model:Modello di Dati degli Attestati Elettronici` (:ref:`WP_060 <wallet-credential-issuance-testcases>`).
    4. DEVE elaborare e verificare l'Attestato Elettronico nel formato SD-JWT VC (secondo la Sezione 4 di `SD-JWT`_) o nel formato mdoc-CBOR (:ref:`WP_062 <wallet-credential-issuance-testcases>`).
    5. DEVE verificare la Trust Chain nell'header dell'SD-JWT VC per verificare che il Credential Issuer sia affidabile (:ref:`WP_061 <wallet-credential-issuance-testcases>`).

Se i controlli sopra hanno successo, l'Istanza del Wallet richiede il consenso dell'Utente per memorizzare l'Attestato o gli Attestati Elettronici. Dopo aver ricevuto il consenso, l'Istanza del Wallet memorizza in modo sicuro l'Attestato Elettronico (:ref:`WP_063 <wallet-credential-issuance-testcases>`).

Di seguito è riportato un esempio non normativo di una risposta di successo contenente un Attestato Elettronico nel formato SD-JWT VC.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store
    Pragma: no-cache

.. literalinclude:: ../../examples/sd-jwt-credential-response.json
  :language: JSON


Di seguito è riportato un esempio non normativo di una risposta di successo contenente un Attestato Elettronico nel formato mdoc.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store
    Pragma: no-cache

.. literalinclude:: ../../examples/mdoc-credential-response.json
  :language: JSON


Di seguito è riportato un esempio non normativo di una risposta di successo contenente un batch di Attestati Elettronici nel formato SD-JWT VC.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store
    Pragma: no-cache

.. literalinclude:: ../../examples/sd-jwt-batch-credential-response.json
  :language: JSON


.. note::
  Quando l'Istanza del Wallet riceve un nuovo batch contentente le stesse credenziali con gli stessi claim, il Wallet DEVE eliminare le Credenziali precedenti (:ref:`WP_073a <wallet-credential-issuance-testcases>`).


.. note::
  Se l'Attestato Elettronico richiesto non può essere emesso immediatamente e richiede più tempo, il Credential Issuer DOVREBBE supportare il Deferred Flow (**passo 27**) come specificato nella Sezione :ref:`credential-issuance-endpoint:Deferred Endpoint` (:ref:`WP_065–067 <wallet-credential-issuance-testcases>`). Inoltre, in caso di emissione in batch, lo stesso ``transaction_id`` si riferisce a tutte le Credenziali richieste nel batch.


**Passo 25 (Notification Request)**: Secondo la Sezione 11.1 di [`OpenID4VCI`_], il Wallet invia una richiesta HTTP POST all'Endpoint di notifica utilizzando il tipo di supporto *application/json* come nel seguente esempio non normativo (:ref:`WP_064 <wallet-credential-issuance-testcases>`).

.. code-block:: http

  POST /notification HTTP/1.1
  Host: eaa-provider.example.org
  Content-Type: application/json
  Authorization: DPoP Kz~8mXK1EalYznwH-LC-1fBAo.4Ljp~zsPE_NeO.gxU
  DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6Ik
      VDIiwieCI6Imw4dEZyaHgtMzR0VjNoUklDUkRZOXpDa0RscEJoRjQyVVFVZldWQVdCR
      nMiLCJ5IjoiOVZFNGpmX09rX282NHpiVFRsY3VOSmFqSG10NnY5VERWclUwQ2R2R
      1JEQSIsImNydiI6IlAtMjU2In19.eyJqdGkiOiJlMWozVl9iS2ljOC1MQUVCIiwiaHRtIj
      oiR0VUIiwiaHR1IjoiaHR0cHM6Ly9yZXNvdXJjZS5leGFtcGxlLm9yZy9wcm90ZWN0Z
      WRyZXNvdXJjZSIsImlhdCI6MTU2MjI2MjYxOCwiYXRoIjoiZlVIeU8ycjJaM0RaNTNF
      c05yV0JiMHhXWG9hTnk1OUlpS0NBcWtzbVFFbyJ9.2oW9RP35yRqzhrtNP86L-Ey71E
      OptxRimPPToA1plemAgR6pxHF8y6-yqyVnmcw6Fy1dqd-jfxSYoMxhAJpLjA
.. literalinclude:: ../../examples/notification-request.json
  :language: JSON


**Passo 26 (`Notification Response`)**: Quando il Credential Issuer ha ricevuto con successo la `Notification Request` dal Wallet, DEVE rispondere con un codice di stato HTTP *204* come raccomandato nella Sezione 11.2 di [`OpenID4VCI`_]. Di seguito è riportato un esempio non normativo di risposta a una `Notification Request` riuscita:


.. code-block:: http

  HTTP/1.1 204 No Content

.. note::
   Nel sistema della Fonte Autentica talvolta sono disponibili molteplici set di dati pertanto l'Utente potrebbe essere interessato a ottenere più di una Credenziale. In questi casi, L'Issuance flow rimane lo stesso descritto in :ref:`credential-issuance-low-level:Flussi Dettagliati per l'Emissione di Attestati Elettronici`. Nella Token Response (**Passo 11**), il Fornitore di Credenziali genera un identificativo univoco (``credential_identifier``) per ciascun set di dati fornito nel parametro ``AttributeClaims`` del servizio PDND :ref:`authentic-source-endpoint:Get Attribute Claims`. Pertanto, l'array ``credential_identifiers`` fornito nel parametro ``authorization_details`` contiene gli identificativi di ciascun set di dati. Successivamente, il Wallet invia una Credential Request (**Passo 16**) per ciascun identificativo, ottenendo più Credenziali distinte che vengono mostrate individualmente all'Utente per la loro accettazione. Infine, il Fornitore di Credenziali viene informato dal Wallet dell'esito tramite il :ref:`credential-issuance-endpoint:Notification Endpoint` (:ref:`WP_057 <wallet-credential-issuance-testcases>`).


.. note::
  Per gli Attestati Elettronici emessi in batch, il ``notification_id`` si riferisce a tutti gli attestati emessi in batch. La Notification Response (ad esempio ``credential_accepted`` o ``credential_stored``) si applica pertanto a tutti gli attestati contenuti nel batch; qualsiasi errore parziale viene trattato come errore dell'intero batch.


Refresh Token Flow
------------------

Per utilizzare gli Endpoint Deferred, Credential Request e Notification, l'Istanza del Wallet DEVE presentare un Access Token DPoP valido al Credential Issuer. Tuttavia, quando questi endpoint sono utilizzati nel Deferred Flow, per la riemissione o la notifica dell'eliminazione di un Attestato Elettronico, l'Access Token potrebbe scadere, poiché è progettato per avere una breve durata e queste azioni POSSONO verificarsi giorni dopo (:ref:`WP_066b <wallet-credential-issuance-testcases>`). Per affrontare questo problema, la specifica RACCOMANDA l'uso dei Refresh Token.

Un Access Token ottenuto come risultato di un Refresh Token Flow DEVE essere limitato al:

  - Deferred Endpoint, per ottenere un nuovo Attestato Elettronico dopo il tempo impostato nel parametro ``interval`` o quando viene notificato come pronto per essere emesso (:ref:`WP_066 <wallet-credential-issuance-testcases>`);
  - Notification Endpoint, per notificare l'eliminazione di un Attestato Elettronico al Credential Issuer;
  - Credential Endpoint, per aggiornare un Attestato Elettronico che è già presente nell'Istanza del Wallet (chiamato anche riemissione dell'Attestato Elettronico, vedi sezione :ref:`credential-issuance-low-level:Re-issuance Flow`).

Per mitigare l'impatto di un Refresh Token rubato, i Refresh Token DEVONO essere DPoP. Questi aspetti sono dettagliati e discussi nella Sezione :ref:`credential-issuance-low-level:Considerazioni di Sicurezza`.

La figura seguente mostra come ottenere un nuovo Access Token DPoP e un nuovo Refresh Token DPoP dal Token Endpoint.

.. _fig_refresh_token_flow:
.. plantuml:: plantuml/pid-issuance-high-level-flow.puml
    :width: 99%
    :alt: La figura illustra il Refresh Token Flow.
    :caption: `Refresh Token Flow. <https://www.plantuml.com/plantuml/svg/TPBDQkim48NtUef3xYQ1cEpleYIaXMRLK0BP588gZ-EXpiYLnhXz-yfoJ1jAbvwVpzySj8vgWtQNnjXElNINLmh6jAd6ZbihYjdHDWqfTf96nT4CDgA_7Ta6AacKRODTZ1s5FCJ6z2ZkqEC_pYGKh1BkztwFDdXVmKg9uwOO2fKF-0M1-ZSIa9IjPz4hZHFja1lFzDvHLFIizK_k_4M0Sx2Y9_riQJby1ge2nVgKaGkaKjvwsdHQ5zk6IRJOg2QSLVQItVvgPcCMQ4seoPP3OZmTEgd5raiapArp5EFut-Mjnd8yS9G4VRISUYUMXJ6rU2LO5toC-7Tyt1qU4hecL8tluRmeIxfzFC8YN9DGdwLAgYW4AbU9mXMxRBrot_bEaKun34j2_HZYQ3owcNKQJQ_Z2m00>`_

.. .. figure:: ../../images/Refresh-Token-Flow.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/TPBDQkim48NtUef3xYQ1cEpleYIaXMRLK0BP588gZ-EXpiYLnhXz-yfoJ1jAbvwVpzySj8vgWtQNnjXElNINLmh6jAd6ZbihYjdHDWqfTf96nT4CDgA_7Ta6AacKRODTZ1s5FCJ6z2ZkqEC_pYGKh1BkztwFDdXVmKg9uwOO2fKF-0M1-ZSIa9IjPz4hZHFja1lFzDvHLFIizK_k_4M0Sx2Y9_riQJby1ge2nVgKaGkaKjvwsdHQ5zk6IRJOg2QSLVQItVvgPcCMQ4seoPP3OZmTEgd5raiapArp5EFut-Mjnd8yS9G4VRISUYUMXJ6rU2LO5toC-7Tyt1qU4hecL8tluRmeIxfzFC8YN9DGdwLAgYW4AbU9mXMxRBrot_bEaKun34j2_HZYQ3owcNKQJQ_Z2m00

..     Refresh Token Flow

.. note::
  L'aggiornamento di un Token può essere attivato da diverse azioni (ad esempio, l'eliminazione di un Attestato Elettronico da parte dell'Utente). In ogni caso, si suppone che le Istanze del Wallet siano in esecuzione e che il relativo materiale crittografico sia sbloccato.

**Passo 1**: L'Istanza del Wallet DEVE creare un nuovo JWT di `DPoP proof` e una nuova prova di possesso dell'Attestato di Unità di Wallet per la richiesta di token del Credential Issuer (:ref:`WP_068a <wallet-credential-issuance-testcases>`).

**Passo 2**: Per aggiornare un Access Token vincolato a DPoP, l'Istanza del Wallet invia una richiesta di token utilizzando il parametro ``grant_type`` impostato su ``refresh_token``, includendo l'header DPoP e gli header di OAuth Client Attestation (:ref:`WP_068 <wallet-credential-issuance-testcases>`).
Un esempio non normativo della richiesta di token per un Access Token DPoP utilizzando un Refresh Token è mostrato di seguito.

.. code-block:: http

  POST /token HTTP/1.1
  Host: eaa-provider.example.org
  Content-Type: application/x-www-form-urlencoded
  DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6IkVDIiwieCI6IjR2dDhNdEFISmlsMzBDNnpUTmt2c0VVcnlHTEUtQW5BNkc5LV8xa3l5Rk0iLCJ5IjoiTWdiNTFfbjNSRjNtbHNtS3dMd0xtRUFqVmlJM3Q1bTVWNTI2MFA5MzR3RSIsImNydiI6IlAtMjU2In19.eyJqdGkiOiItQndDM0VTYzZhY2MybFRjIiwiaHRtIjoiR0VUIiwiaHR1IjoiaHR0cHM6Ly9yZXNvdXJjZS5leGFtcGxlLm9yZy9wcm90ZWN0ZWRyZXNvdXJjZSIsImlhdCI6MTU2MjI2MjYxOH0.3Tp1ZlZ05PQYeZUHhiZwaQ1etqnwYwoiJHFR_JHb32381lMJL-8o2rE3VZ8X3yuqrGFfCVeP90Ln4J5r8ASIBg
  OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtpZCI6IjBiNDk4ZGRlMDkxNzJhZGE3MDFkMDdlYjZmOTg2N2FkIiwidHlwIjoib2F1dGgtY2xpZW50LWF0dGVzdGF0aW9uK2p3dCIsIng1YyI6WyJNSUlEcWpDQ0FwS2dBd0lCQWdJRVNMTkV2REEgLi4uIiwiTUlJQ3d6Q0NBYXNDQ1FDS1Z5OWVLanZpK2pBIC4uLiIsIk1JSURURENDQWpTZ0F3SUJBZ0lKQVBsblFZSC4uLiJdfQ.eyJzdWIiOiJodHRwczovL3dhbGxldC1zb2x1dGlvbi5leGFtcGxlLm9yZy9kZDc2MmU2ZjhiNjEzMTkzIiwiY25mIjp7Imp3ayI6eyJjcnYiOiJQLTI1NiIsImt0eSI6IkVDIiwieCI6IjRITnB0SS14cjJwanlSSktHTW56NFdtZG5RRF91SlNxNFI5NU5qOThiNDQiLCJ5IjoiTElablNCMzl2RkpoWWdTM2s3alhFNHIzLUNvR0ZRd1p0UEJJUnFwTmxyZyJ9fSwid2FsbGV0X25hbWUiOiJXYWxsZXRfdjEiLCJ3YWxsZXRfbGluayI6Imh0dHBzOi8vZXhhbXBsZS5jb20vd2FsbGV0L2RldGFpbF9pbmZvLmh0bWwiLCJ3YWxsZXRfdmVyc2lvbiI6IjEuMC4wIiwiY2xpZW50X3N0YXR1cyI6eyJzdGF0dXMiOnsic3RhdHVzX2xpc3QiOnsiaWR4IjoxMzM3LCJ1cmkiOiJodHRwczovL3Jldm9jYXRpb25fdXJsL3dpYS1zdGF0dXNsaXN0cy80MiJ9fSwiZXhwIjoxMzAzNDk3NzgwfSwiZXhwIjoxNzQwMTU4MTY3fQ.XOv01xkHC-_h-bZFcXgkEffs3xk8WezKWs8KA4yZD8aNabDq81Y80wkOuHCM25zSGHbABszaSDsyYaJv9bh40w
  OAuth-Client-Attestation-PoP: eyJhbGciOiJFUzI1NiIsInR5cCI6Im9hdXRoLWNsaWVudC1hdHRlc3RhdGlvbi1wb3Arand0In0.ew0KICAiaXNzIjogIiA0N2I5ODIzNjk3OTFkMDgwMDNhNzI4M2YwNTljYjBkMSIsDQogICJhdWQiOiAiaHR0cHM6Ly9hcy5leGFtcGxlLmNvbSIsDQogICJqdGkiOiAiZDI1ZDAwYWItNTUyYi00NmZjLWFlMTktOThmNDQwZjI1MDY0IiwNCiAgImlhdCI6IDE3NDAxNTg2MTcNCn0.B0KOkGi9vMxf3H2Y8rrF-mdLNsuluTvAUbjFfL1Hi-gdaPW7-8ziS9uVh7aTnSAHKWzMfkZLv5q-bxhkglR4PA

  grant_type=refresh_token
  &refresh_token=eyJ0eXAiOiJydCtqd3QiLCJhbGciOiJFUzI1NiIsImtpZCI6ImM5NTBjMGU2ZmRlYjVkZTUwYTUwMDk2YjI0N2FmMDNjIn0.eyJpc3MiOiJodHRwczovL2VhYS1wcm92aWRlci53YWxsZXQuaXB6cy5pdCIsImNsaWVudF9pZCI6IjQ3Yjk4MjM2OTc5MWQwODAwM2E3MjgzZjA1OWNiMGQxIiwiYXVkIjoiaHR0cHM6Ly9lYWEtcHJvdmlkZXIud2FsbGV0LmlwenMuaXQiLCJpYXQiOjE3Mzk5NTI5NDgsIm5iZiI6MTczOTk1MzU0OCwiZXhwIjoxNzQyMzcyNzQ4LCJhdGgiOiJmVUh5TzJyMlozRFo1M0VzTnJXQmIweFdYb2FOeTU5SWlLQ0Fxa3NtUUVvIiwianRpIjoiYzY5NTVjZWItYzY1Zi00MDI1LTkzNzgtYjY2NzJiNjE0NWNmIiwiY25mIjp7ImprdCI6Ijk1MTU3NGFlZTFiYjc5MDdhZTFlYzMxMDlkYjJiMjI1In19.qiGM6E-7zci2-3Nnk4OMD7Tv_leUcRPsFsqaBHDHxEEzsGXLNh9qDbLIBk9sujZGVT9xs-28jZhwD6VT-MGTGw

**Passaggio 3**: Il Credential Issuer valida la richiesta sulla base dei seguenti controlli:

  - DEVE validare il parametro OAuth-Client-Attestation-PoP in base alla Sezione 5 di [OAUTH-ATTESTATION-CLIENT-AUTH].
  - DEVE validare il JWT di `DPoP proof`, secondo la Sezione 4.3 di (RFC 9449).
  - DEVE verificare che il Refresh Token non sia scaduto, non sia revocato e sia associato allo stesso set di chiavi DPoP di quelle utilizzate nel JWT di `DPoP proof`.

Se i controlli della richiesta hanno successo, il Credential Issuer genera un nuovo Access Token e un nuovo Refresh Token e questi DEVONO essere entrambi associati alla chiave DPoP. Sia l'Access Token che il Refresh Token vengono quindi inviati all'Istanza del Wallet.

Un esempio non normativo di una risposta di successo è mostrato di seguito.

.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json
  Cache-Control: no-store

  {
      "access_token": "eyJ0eXAiOiJhdCtqd3QiLCJhbGciOiJFU..",
      "refresh_token": "eyC3fiLdCtqd3QiLCJhbGciOiCL3..",
      "token_type": "DPoP",
      "expires_in": 3600
  }

Se il Refresh Token è scaduto o non valido, il Credential Issuer DEVE emettere un errore, utilizzando il claim `error type` impostato su ``invalid_grant``. Pertanto, per ottenere l'Attestato Elettronico è necessario un flusso di emissione che autentichi l'Utente, come definito nella Sezione :ref:`credential-issuance-low-level:Issuance Flow`.

Considerazioni di Sicurezza
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per mitigare i rischi di compromissione del Refresh Token, sono richieste le seguenti protezioni:

  - La **riservatezza** dei Refresh Token DEVE essere garantita in transito e archiviazione.
  - Per la trasmissione dei token, DEVONO essere utilizzate connessioni **protette da TLS**.
  - I Refresh Token DEVONO essere **non indovinabili e sicuri da modifiche**.
  - Gli Authorization Server DEVONO implementare il seguente meccanismo per **rilevare gli attacchi di replay**:

    - **Sender-Constrained Tokens**: Vincolare crittograficamente il Refresh Token all'Istanza del Wallet secondo :rfc:`9449`. Gli Access Token e i Refresh Token DEVONO essere vincolati alla stessa chiave DPoP. La `DPoP proof` del Refresh Token è richiesta per aggiornare un Access Token. La stessa chiave DPoP DEVE essere utilizzata per generare le `DPoP proof` dell'Access Token in tutte le `Credential Request`.

  - **Limitazione dell'uso del Refresh Token**: Come specificato in `OPENID4VC-HAIP`_: "Credential Issuers should be mindful of how long the usage of the refresh token is allowed to refresh a Credential, as opposed to starting the issuance flow from the beginning. For example, if the User is trying to refresh a Credential more than a year after its original issuance, the usage of the refresh tokens is NOT RECOMMENDED." In questa specifica, un nuovo Attestato Elettronico ottenuto eseguendo il Re-issuance Flow DOVREBBE avere la stessa scadenza di quello aggiornato. Pertanto, questa specifica non consente l'aggiornamento infinito dell'Attestato Elettronico con un Refresh Token. Una volta che un Attestato Elettronico scade, l'Utente DEVE completare nuovamente l'intero processo di emissione per ottenere un nuovo Attestato Elettronico. Questa specifica raccomanda di impostare una durata di scadenza del Refresh Token, in base alla sensibilità del grant associato.

.. note::
  *Attestati di Unità di Wallet e DPoP di breve durata*: Seguendo la bozza di specifica *OAuth 2.0 Attestation Based Client Authentication* (`OAUTH-ATTESTATION-CLIENT-AUTH`_), l'Authorization Server DEVE associare il Refresh Token alla Client Instance. Per dimostrare questa associazione, la Client Instance DEVE utilizzare il meccanismo di Client Attestation quando aggiorna l'Access Token e la Client Instance DEVE utilizzare la stessa chiave che è stata presentata nel claim ``cnf.jwk`` della Client Attestation che è stata utilizzata quando il Refresh Token è stato emesso. Tuttavia, ciò richiede che tutti le Client Attestation emesse DEVONO essere associati alla stessa chiave, aprendo così a problemi di non collegabilità. In questa specifica, sia `OAUTH-ATTESTATION-CLIENT-AUTH`_ che *OAuth 2.0 Demonstrating Proof of Possession (DPoP)* (:rfc:`9449`) DEVONO essere utilizzati. L'uso di DPoP garantisce l'associazione del Refresh Token con la Client Instance come indicato nella sezione 5 di :rfc:`9449` *"the Refresh Token MUST be bound to the respective public key [...] a Client MUST present a DPoP proof for the same key that was used to obtain the Refresh Token each time that Refresh Token is used to obtain a new Access Token"*. DPoP garantisce che il Refresh Token sia associato all'Istanza del Wallet (:ref:`WP_068b <wallet-credential-issuance-testcases>`). DPoP ensures that the Refresh Token is bound to the Wallet Instance.


Re-issuance Flow
----------------

La riemissione comporta la sostituzione degli Attestati Elettronici già memorizzati in un'Istanza del Wallet con nuovi dello stesso tipo di documento. I nuovi Attestati Elettronici DEVONO essere emessi dagli stessi Credential Issuer che hanno originariamente fornito quelli esistenti alla stessa Istanza del Wallet.

Per facilitare questo, in particolare in scenari in cui l'autenticazione dell'Utente non è strettamente richiesta, PUÒ essere utilizzato un Refresh Token Flow (RT) (vedi Sezione :ref:`credential-issuance-low-level:Refresh Token Flow` per maggiori dettagli). Un Access Token ottenuto come risultato di un Refresh Token Flow NON DEVE essere utilizzato per emettere un Attestato Elettronico che non è presente nell'Istanza del Wallet (prima emissione). Il meccanismo del Refresh Token consente la sostituzione automatica degli Attestati Elettronici, semplificando il processo sia per il Credential Issuer che per l'Utente.

Il Re-issuance Flow delineato in questa sezione è limitato ai seguenti scenari:

  - Aggiornamento tecnico del modello/formato dei dati;
  - Aggiornamento dell'insieme di attributi dell'Utente.

Questo flusso non si applica alla migrazione di dispositivo o al ripristino da backup. In tali casi l'Istanza del Wallet DEVE eseguire un Wallet-Initiated Authorization Code Issuance Flow come definito nella Sezione :ref:`credential-issuance-low-level:Issuance Flow` (vedere Sezione :ref:`backup-restore:Flusso di ripristino per Credenziale con associazione hardware`).

Nel primo caso, l'insieme di attributi dell'Utente del nuovo Attestato Elettronico corrisponderà a quello originale. Ad esempio, un Credential Issuer potrebbe dover aggiornare i Metadata dell'Attestato Elettronico o il formato dei dati senza modificare l'insieme di attributi dell'Utente. In questo caso, il coinvolgimento diretto dell'Utente non è obbligatorio per la sostituzione e l'archiviazione di un Attestato Elettronico.

Nel secondo caso, i Credential Issuer potrebbero anche dover modificare uno o più valori degli attributi dell'Utente durante la riemissione. In questo caso, l'Istanza del Wallet DEVE informare l'Utente che l'insieme di dati degli attributi è stato modificato e DEVE quindi richiedere l'autorizzazione dell'Utente per memorizzare il nuovo Attestato Elettronico.

In entrambi i casi, l'Attestato Elettronico appena emesso DEVE avere la stessa data di scadenza di quello precedente.

La riemissione dopo la scadenza dell'Attestato Elettronico DEVE sempre richiedere l'autenticazione dell'Utente.

Il seguente diagramma descrive il Re-issuance Flow dell'Attestato Elettronico.

.. _fig_reissuance_flow:
.. plantuml:: plantuml/credential-reissuance-flow.puml
    :width: 99%
    :alt: La figura illustra il Re-issuance Flow.
    :caption: `Re-issuance Flow. <https://www.plantuml.com/plantuml/svg/ZLFVYnCn47xFN_6zsSAT7FYsXtZL8Xme75KvH7p8xSvsWsbICvEs-jURfEtQbOZEmp93vfjlVdnxnwA3n8rLnL7E2o6OzI3gSI07ZQLP6z4MRm9rvCGarn5r3F5u8iHjfuMwAyX0bpdtp942u_tYCvXS1urKs_IcrMAyI-Y2-CGK4DcuDJG2hGqBfIBmKQvzV_sa4xBrcqrqPs0xQEV8FbUvQ6vNgQPKyLjoZ4TjBGdk7OjsBTqgA03DYYGOsX4-Y9R8U9U8yD5_8uVUXvm25f-OBsRW10OA1oprKg8LVOycv-tpUfp7JblJvQTAQJeadylZs6qEJ8_PRvupq3XykJdSlBX2-hx--ceEoHop7yJp0WDP9ioSdqFXqbZyLk54OtfL_3FHecs9-THHwRPI-MGbk6GQdyToA-e3yV1_zO0c3HS4KzHRw_V7vTRuwfCL6--XCBKZYtPmj2_QoyT7dtZ-pDmR6OhidZ4MCVSjPsbDKwSdApOkk1wDJXOabW_-0PFbYqSuwN1CJVrMVh7ZSYfIuQDKNXQ9_7tlJPOfiPH1ovW-c9zbojlQlKUgIJvnXM5wMn-eZ51hlNxN-cN7NTQ1_sQigRzPaYKXR0FjZ8yymQZIm5s2n8tz1G00>`_


.. .. figure:: ../../images/Re-Issuance-Flow.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/ZLJRRXen47ttLqoVcaXS8ZLFH553GoeX9HMYqAXAAcHsPrchNfjwPY7frtTjBiAuJV73QctFcSlncRaXbexhIejtocIwpX5AvYNrkbqdrvs5uhAUruGkiuRHS2UpLNUffV6ODd6krRnxUzaU-QFfmtstaiJecgFPuDN8IcMTfVVUh1196Ci8JYrA5eyb6f0mK4qKgU7MOOw6LVDh47C2jZ17g9UvPCnRm2KUsWo9QdG43_tlG6Xoa60igq9bafKr7kqHKq87DIcp00aE5ygdXpdOcjksQCzbWsnggcgp0sQbD0PrHtYdFbqXUi6BNQ8XU9HQ8yFG44kJuPKGge2pCQxi5b-Xzw2eWcS3r_2L9TS4zueOFfu3-wBFNf7E1GW0w8sHdS8LHeOJ-nCD5DPv4o2s3lE3ukagd0SkDHOSTcFyLIjlj_OXZ8MLr2eFLwbhV6d-ALpko_GRNyi1oLkWCl1qyNBneGNDz_B7KHb-eIQ4CsFFGS3X8hPB0TimgX2HhV3Rb84-4JfF9Pt6W5VJAHJ4llzAmHiSNCFmoxV-_N2GLhy3PNlGZ09ebYDBfJj-Xw3CtlffEXhq9tSjw4ycu-6dwUHkjZb9kJs9tfZXqvzZyusAw6SP4crb4lXBKjgl9B_uUjCOXKCgJ_C7q6lOTWmnwhEswyrxln4lvGDWBn41yTf4aGOChiCayQqCHHFds7Ajk0n3v3r1l_PvysvGnAPn7wLlakxsFtwym61aHn2HpnRSjZNsfZxVT61koKcrIplj-hvjWNNmRFwZqkj4a_z-hvvlE2GE10Lwh5E_0pjNXtQ9AY9xf2J2iIQiGrzwNFBRUeWLaRv80Zmzub7Nz0QeaH6M3bVArXHXH4ZWfe7KbVu3

..     Re-Issuance Flow Diagram


**Passo 1**: Il flusso inizia quando l'Utente apre l'Istanza del Wallet: questo passaggio PUÒ essere attivato da una notifica inviata dal Credential Issuer (utilizzando ad esempio uno dei contatti di comunicazione out-of-band registrati durante il flusso di emissione).

**Passo 2**: L'Istanza del Wallet DEVE controllare lo stato di ogni Attestato Elettronico memorizzato, recuperando — se non disponibile — un Token di Stato valido (seguendo il flusso descritto nella Sezione :ref:`credential-revocation:Token di Status List`) come da (:ref:`WP_069 <wallet-credential-issuance-testcases>`).
L'Istanza del Wallet DEVE poi verificare (:ref:`WP_070 <wallet-credential-issuance-testcases>`) se un Attestato Elettronico ha lo stato impostato su ``0x03`` - ``UPDATE`` o ``0x0F`` - ``ATTRIBUTE_UPDATE``.

Se le condizioni non sono soddisfatte, il flusso DEVE essere interrotto.

Altrimenti, l'Istanza del Wallet DEVE verificare i relativi Access Token. Se sono ancora validi, il Passo 3 PUÒ essere saltato (:ref:`WP_071 <wallet-credential-issuance-testcases>`).

**Passo 3**: Se l'Access Token è scaduto e l'Istanza del Wallet ha ancora un Refresh Token valido, l'Istanza del Wallet DEVE ottenere un nuovo Access Token avviando un Refresh Token Flow, secondo la Sezione :ref:`credential-issuance-low-level:Refresh Token Flow` (:ref:`WP_071a <wallet-credential-issuance-testcases>`).
Il Refresh Token Flow consente all'Istanza del Wallet di ottenere un nuovo Refresh Token e un nuovo Access Token DPoP per aggiornare l'Attestato Elettronico. Se il Refresh Token è scaduto, è necessario un nuovo flusso di emissione che autentichi l'Utente (:ref:`WP_067 <wallet-credential-issuance-testcases>` e :ref:`WP_071b <wallet-credential-issuance-testcases>`).

**Passo 4**: L'Istanza del Wallet DEVE utilizzare un Access Token DPoP valido per recuperare il nuovo Attestato Elettronico, richiedendolo al Credential Endpoint seguendo i passi da 12 a 22 della Figura 9 nella Sezione :ref:`credential-issuance-low-level:Issuance Flow` (:ref:`WP_072 <wallet-credential-issuance-testcases>`).
Quando il nuovo Attestato Elettronico è memorizzato con successo nel secure storage, l'Istanza del Wallet DEVE eliminare quello precedente (:ref:`WP_073 <wallet-credential-issuance-testcases>`).

.. note::
  Indipendentemente dal meccanismo di revoca supportato, se lo stato dell'Attestato Elettronico è impostato su ``ATTRIBUTE_UPDATE``, l'insieme di attributi dell'Utente nell'Attestato aggiornato non corrisponde a quello memorizzato. In questo caso, l'Istanza del Wallet DEVE richiedere l'autorizzazione dell'Utente per memorizzare il nuovo Attestato aggiornato (:ref:`WP_074 <wallet-credential-issuance-testcases>`).

  Se invece lo stato è impostato su ``UPDATE``, solo i parametri dei Metadata sono cambiati. In questo caso, l'Istanza del Wallet DOVREBBE memorizzare il nuovo Attestato senza richiedere autorizzazione o consenso esplicito dell'Utente (:ref:`WP_075 <wallet-credential-issuance-testcases>`).


Re-issuance Flow: Considerazioni di Sicurezza
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per garantire l'integrità e la sicurezza del Re-issuance Flow, si applicano le seguenti considerazioni di sicurezza.

  - Limitazioni dell'Access Token: Un Access Token ottenuto come risultato di un Refresh Token Flow NON DEVE essere utilizzato per l'emissione per la prima volta di un Attestato Elettronico. Ciò garantisce che vengano aggiornati solo gli Attestati Elettronici esistenti nell'Istanza del Wallet.
  - Scadenza dell'Attestato Elettronico: Il Credential Issuer DEVE impostare per l'Attestato Elettronico riemesso la stessa data di scadenza del precedente. Ciò impedisce rinnovi indefiniti dell'Attestato Elettronico senza una corretta autenticazione dell'Utente.
  - Consenso dell'Utente: Per i Re-issuance Flow attivati da modifiche agli attributi, il consenso dell'Utente DEVE essere ottenuto prima di memorizzare il nuovo Attestato Elettronico.
  - Refresh Token vincolato al mittente: I Refresh Token DEVONO essere crittograficamente vincolati all'Istanza del Wallet utilizzando il protocollo DPoP. Ciò mitiga il rischio di uso improprio del token, garantendo che solo l'Istanza del Wallet prevista possa utilizzarlo.

.. note::
    Durante ogni transazione di emissione di un Attestato Elettronico e, ove supportato, ogni transazione di riemissione/aggiornamento eseguita tramite i flussi descritti in questa sezione, l'Istanza del Wallet DEVE creare e mantenere un corrispondente record di transazione nel registro delle transazioni dell'Istanza del Wallet (vedi :ref:`wallet-instance-dashboard:Dashboard dell’Istanza del Wallet e Registrazione delle Transazioni`).

    L'Istanza del Wallet DEVE creare un record di transazione per ogni processo di emissione. Il record DEVE acquisire le informazioni di contesto rilevanti necessarie a garantire tracciabilità e responsabilizzazione della transazione.

    Il record DEVE essere aggiornato man mano che il flusso progredisce per riflettere lo stato della transazione e l'esito (ad es., il/i tipo/i di Attestato emesso/i e la quantità). Nei casi in cui la transazione non si completi con successo, il record DEVE indicare la corrispondente motivazione della mancata conclusione.


Flusso Credential Offer
-----------------------

Un Credential Issuer o una terza parte (ad esempio, Authentic Source, Registro, Catalogo) avvia l'emissione di Attestati Elettronici inviando una Credential Offer all'Istanza del Wallet.

Per richiamare l'Istanza del Wallet corretta, è necessario sapere quale Istanza del Wallet è installata sul dispositivo dell'Utente e quale l'Utente desidera utilizzare.
Queste informazioni DOVREBBERO essere ottenute utilizzando la Selection Page descritta in :ref:`functionalities:Design dell'Esperienza Utente`.

-  Se la Selection Page è disponibile, l'utente seleziona l'Istanza del Wallet, quindi il Credential Issuer o una terza parte recupera i Wallet metadata come descritto in :ref:`wallet-metadata-retrieval:Flusso di Recupero dei Wallet Metadata`. Il meccanismo di invocazione dell'Istanza del Wallet dipende dal parametro ``credential_offer_endpoint`` nei Wallet metadata:

  - Se ``credential_offer_endpoint`` è disponibile e contiene un URL HTTPS (Universal Link), il Credential Issuer o la terza parte DOVREBBE utilizzare quell'endpoint.
  - Altrimenti, il Credential Issuer o la terza parte DEVE utilizzare uno degli schemi URL personalizzati: ``openid-credential-offer://`` (come definito nella Sezione 4 di [`OpenID4VCI`_]) o ``haip-vci://`` (come definito nella Sezione 4.2 di [`OPENID4VC-HAIP`_]). L'Istanza del Wallet DEVE supportare entrambi gli schemi URL personalizzati.

-  Nel caso in cui il Credential Issuer o la terza non supporti la Selection Page o il recupero dei Wallet metadata fallisce per qualche motivo,  il Credential Issuer o la terza richiamerà l'Istanza del Wallet utilizzando uno degli schemi URL personalizzati descritti precedentemente.

La Credential Offer può essere trasmessa per valore o per riferimento:

- **Per valore** (parametro ``credential_offer``): l'oggetto Credential Offer è incorporato direttamente nell'URI come stringa codificata JSON.
- **Per riferimento** (parametro ``credential_offer_uri``): l'URI punta a una risorsa ospitata dal Credential Issuer o dalla terza parte. L'Istanza del Wallet recupera l'oggetto Credential Offer inviando una richiesta HTTP GET a quell'URI.

L'oggetto Credential Offer è un oggetto JSON contenente i parametri definiti nella Sezione 4.1.1 di [`OpenID4VCI`_]. La tabella seguente specifica i parametri con requisiti specifici IT-Wallet:

.. _table_credential_offer_claim:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **credential_issuer**
    - DEVE essere impostato con un URL HTTPS che identifica univocamente il Credential Issuer. Il Wallet utilizza questo valore del parametro per ottenere i metadata del Credential Issuer.
    - Sezione 4.1.1 di [`OpenID4VCI`_].
  * - **credential_configuration_ids**
    - Array di stringhe, ciascuna delle quali specifica un identificatore univoco dell'Attestato Elettronico descritto nella mappa ``credential_configurations_supported`` nei Metadata del Credential Issuer (:ref:`WP_050b <wallet-credential-issuance-testcases>`).
    - Sezione 4.1.1 di [`OpenID4VCI`_].
  * - **grants**
    - OBBLIGATORIO. DEVE contenere l'oggetto ``authorization_code`` con i seguenti parametri:

        - **issuer_state**: OPZIONALE. Stringa opaca utilizzata per associare la successiva Authorization Request con il Credential Isser. PUO' essere associata a un determinato Credential Dataset fornito da una specifica Fonte Autentica. Il Wallet DEVE includerlo nella successiva Authorization Request quando presente. Deve essere un’URN e contenere le seguenti informazioni:

            - *authenticSourceId*: OBBLIGATORIO. DEVE corrispondere al valore ``entity_id`` della Fonte Autentica che fornisce i Credential Dataset, come indicato nel :ref:`registry:Registro delle Fonti Autentiche`.

            - *datasetId*: OBBLIGATORIO. Identificativo univoco del dataset fornito dalla Fonte Autentica, come indicato nel :ref:`registry:Registro delle Fonti Autentiche`.

            - *objectId*: OPZIONALE. Identificativo univoco del Credential Dataset disponibile presso la Fonte Autentica.

        Il parametro ``issuer_state`` DEVE seguire la seguente struttura: ``urn:it-wallet:credential-offer:{authenticSourceId}:{datasetId}`` se ``objectId`` è assente oppure ``urn:it-wallet:credential-offer:{authenticSourceId}:{datasetId}:{objectId}`` nel caso in cui ``objectId`` è presente. Il segmento opzionale ``objectId`` DEVE essere omesso quando non disponibile; NON DEVE essere utilizzato un segmento finale vuoto. Il valore di questo URN DEVE essere cifrato utilizzando la chiave pubblica PDND relativa al Consumer dell’e-service ``GetAttributeClaims``.

        - **authorization_server**: OBBLIGATORIO quando il Credential Issuer utilizza più di un authorization server nella sua soluzione. Stringa che identifica l'Authorization Server da utilizzare. Il valore DEVE corrispondere a uno dei valori mappati nell'array ``authorization_servers`` dei metadata del Credential Issuer. NON DEVE essere utilizzato se ``authorization_servers`` è assente o non ha voci multiple.
    - Sezione 4.1.1 di [`OpenID4VCI`_] e Sezione 4.1 di [`OPENID4VC-HAIP`_].

.. note::
  Quando si utilizza ``credential_offer_uri`` (per riferimento), il Credential Issuer o la terza parte DOVREBBE utilizzare un URI univoco per ogni Credential Offer o altrimenti prevenire il caching dell'URI, come raccomandato nella Sezione 4.1.3 di [`OpenID4VCI`_].

Esempi non normativi
^^^^^^^^^^^^^^^^^^^^

**Esempio 1: Credential Offer per valore**

La Credential Offer può essere trasmessa per valore utilizzando qualsiasi metodo di invocazione supportato (schema URL personalizzato o Universal Link):

.. code-block:: text

  openid-credential-offer://?credential_offer=%7B%22credential_issuer%22%3A%22https%3A//credential-issuer.example.org%22%2C%22credential_configuration_ids%22%3A%5B%22dc_sd_jwt_Education_degree%22%5D%2C%22grants%22%3A%7B%22authorization_code%22%3A%7B%22issuer_state%22%3A%22eyJhbGciOiJSU0Et...F77QK8%22%7D%7D%7D

L'oggetto Credential Offer decodificato:

.. code-block:: json

  {
    "credential_issuer": "https://credential-issuer.example.org",
    "credential_configuration_ids": ["dc_sd_jwt_Education_degree"],
    "grants": {
      "authorization_code": {
        "issuer_state": "eyJhbGciOiJSU0Et...F77QK8",
      }
    }
  }

**Esempio 2: Credential Offer per riferimento da Credential Issuer**

Il codice QR o il pulsante href contiene:

.. code-block:: text

  openid-credential-offer://?credential_offer_uri=https%3A%2F%2Fcredential-issuer.example.org%2Foffers%2F8f3a2b1c

L'Istanza del Wallet invia una richiesta HTTP GET:

.. code-block:: http

  GET /offers/8f3a2b1c HTTP/1.1
  Host: credential-issuer.example.org
  Accept: application/json

Il Credential Issuer risponde:

.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json
  Cache-Control: no-store

  {
    "credential_issuer": "https://credential-issuer.example.org",
    "credential_configuration_ids": ["dc_sd_jwt_EuropeanDisabilityCard"],
    "grants": {
      "authorization_code": {
        "issuer_state": "eyJhbGciOiJSU0Et...F77QK8",
      }
    }
  }

**Esempio 3: Credential Offer per riferimento da terza parte**

Una terza parte, come un'Authentic Source, genera una Credential Offer per un Credential Issuer.

Il codice QR contiene:

.. code-block:: text

  openid-credential-offer://?credential_offer_uri=https%3A%2F%2Fauthentic-source.gov.example%2Fcredential-offers%2Fabc123

L'Istanza del Wallet invia:

.. code-block:: http

  GET /credential-offers/abc123 HTTP/1.1
  Host: authentic-source.gov.example
  Accept: application/json

L'Authentic Source risponde:

.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json
  Cache-Control: no-store

  {
    "credential_issuer": "https://credential-issuer.example.org",
    "credential_configuration_ids": ["mso_mdoc_mDL"],
    "grants": {
      "authorization_code": {
       "issuer_state": "eyJhbGciOiJSU0Et...F77QK8",
      }
    }
  }


