.. include:: ../common/common_definitions.rst


Revoca dell'Istanza del Wallet
==============================

Questa sezione descrive le entità coinvolte e le modalità per richiedere la revoca di un'Istanza del Wallet.

Il Fornitore di Wallet DEVE garantire la sicurezza e l'affidabilità delle Istanze del Wallet, mantenendole aggiornate e conformi ai requisiti di sicurezza. Quando, per motivi tecnici di sicurezza (ad esempio, relativi alla compromissione del materiale crittografico) la sicurezza dell'Istanza del Wallet è compromessa, il Fornitore di Wallet DEVE revocare l'Istanza del Wallet.

Come mostrato in :numref:`fig_Wallet_Instance_Revoc_Entities`, altri attori POSSONO attivare il processo di revoca dell'Istanza del Wallet (:ref:`WP_007–009 <wallet-provider-backend-testcases>`):

- **Utenti**, collegandosi al portale web del Fornitore di Wallet dalla propria Istanza del Wallet o utilizzando un browser esterno.
- **PID Provider e EAA Provider di IT-Wallet ID** quando notificati dalla Fonte Autentica del PID/IT-Wallet ID (ANPR) del decesso dell'Utente.
- **Autorità Legali o Organismo di Supervisione** in casi di comprovate attività illegali.

.. _fig_Wallet_Instance_Revoc_Entities:
.. plantuml:: plantuml/wallet-instance-revocation-entities.puml
    :width: 99%
    :alt: La figura illustra le Entità coinvolte nel processo di revoca dell'Istanza del Wallet.
    :caption: `Entità coinvolte nel processo di revoca dell'Istanza del Wallet. <https://www.plantuml.com/plantuml/svg/fLBDZjCm4BxxAOPUw4gWlUmHeMNRI0JnKxLT8QHAaHiFhKLg5tlS4X3lpjZhR27cjfMgn1D_FpFVt7gIZiAX4y-qQRkW45xDRgvdDytC7exMeA7NGhojvrMpMbVBwjFwowAQNWcnGEUjcGQFxWLCxlanuMTbI5CFzcoqsG7j4JRci-mw9AWDIvaM9mo-iy4ewVhfENrhVEy93upFTrVfFBc2NmBuzsXbkAyp5oF6x5oA_m_Io1rwYFwUUvZhdIRPmSoXOXujEyy-_ijzTFQa5NSrK2zoOQ3EPmyZQP16mHctm98dtM9K-2t4HK06saVnjl4skEJ-pL22LIeL6d6m88cStWRYCzaqrThxW2uf7dAdiNoIdLOn07P4WGrSr9lgnuC3w_HFLCtMgZuP62gGijFe1m-hS8oDUEjwkEFRIUrTKBhbyK46KX_plFIeax7OGJs_hjSlXndDYp6c5lm_BHIO-37duSUZ5MA9NTw_SNJ5Mi0IJxQLfAtXr-yiJ94YCXJOSiSY-1kEyuuc8a5i-QacojLu7EH7I_fh3_SFYxmn2YNjitIHP-aXmskkxs9iBUbJYZbBD-_B2GJ_DtHZBhuPT8j6XKFt1m00>`_


Indipendentemente da chi ha attivato il processo di revoca, il Wallet Provider DEVE implementare un meccanismo per informare gli Utenti quando la loro Wallet Unit viene revocata (:ref:`WP_034 <wallet-instance-testcases>`):

- Inviando un avviso presso un recapito verificato (ad esempio recapito e-mail o telefonico) e se possibile anche presso l'Istanza del Wallet revocata.
- Inviando la notifica entro massimo 24 ore.
- Includendo una spiegazione chiara e semplice dei motivi della revoca, con eventuali istruzioni per riattivare l'Istanza del Wallet.

.. .. figure:: ../../images/wallet_instance_revocation.svg
..     :figwidth: 80%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/fL9TZn8z5BwVNt5URbusSPSRhxnQ5oOHuog1tHYJJIPbMk74JZksf-1e_E-UKmiguvqafFIXpyVvk8sa0gNELl-XQstI1lP4VNmncmLrlDaXxTCsHHDQxyWukcbzD-kjSiAvZgGjRcVpvzShWHxltymw5Sa4XfgvxthlXDEBVlLgkQYRpKEzhjyzV5ZLqwkgMfaGlPkA_ZEOFF8nuRDsX3I0FpfqEw2zWIVtNbbh29QEyxhMJ9XyvvFJAWpJO_wlYGCxTymlRpVvFhc2RnNmvnpdz1wBbZ0kr1cIxxroQcSYIBx_8ooGsw4ip8FHh8FAHixnL-q--0DghkealIh0IRhS8rnOWt8QZcOBR7d0reZ3zwhwPQ0IxSMyRQ9F8QT_UO9Waw6HXpGM5570RIA-ayzTNSQOJCYENQbKu8Eog6K0d8YI13YxD_MNdmbymAz6Drkl1mbmHY3F3aqyPTYaNWg9FWnmnw-ps-kaiKLbeH1fO9FVQiGSJ2fOBaQTowdZ7wdbcTnBr-Db0wjgRMpPiei1ZOSFQtFmhIBqZdz-PYyI2L4OSSUR9EHFvdAg4a84fB1_3J5UW7Extdh2ZuECMzRroMcZQ5-iHrCRPoZq9UCx6KvBU432dFxME9qw-mC0

..     Entities involved in the Wallet Instance revocation process.

.. note::
  - Il flusso per la Revoca dell'Istanza del Wallet attivato dall'Utente è dettagliato di seguito.
  - L'endpoint utilizzato dal Provider di PID/IT-Wallet ID è dettagliato nel Catalogo e-Service del Fornitore di Wallet PDND (vedere la Sezione :ref:`wallet-provider-endpoint:Catalogo e-Service PDND del Fornitore di Wallet` per i dettagli tecnici).
  - Il flusso per le Entità Autorizzate (ad esempio, Organismi di Supervisione) è fuori dall'ambito di questa specifica, sarà gestito da ciascun Fornitore di Wallet.


Richiesta di Revoca dell'Istanza del Wallet
"""""""""""""""""""""""""""""""""""""""""""

Gli Utenti POSSONO richiedere la revoca dell'Istanza del Wallet (:ref:`WP_032 <wallet-instance-testcases>`):

- *Selezionando la funzionalità di revoca all'interno dalla propria Istanza del Wallet*: questa funzionalità può essere utilizzata dagli Utenti prima di cambiare il proprio telefono.
- *Utilizzando un user agent esterno*: questo copre i casi in cui gli Utenti perdono il loro dispositivo e quindi l'accesso alla loro Istanza del Wallet.

In entrambi i casi, utilizzando il portale del Fornitore di Wallet (:ref:`WP_005–006 <wallet-provider-backend-testcases>`):

- Gli Utenti DEVONO autenticarsi con almeno un meccanismo di autenticazione a due fattori, o avere una sessione attiva che soddisfi questo requisito.
- Il Fornitore di Wallet DEVE consentire agli Utenti di visualizzare lo stato delle loro Istanze del Wallet associate alla loro sessione autenticata e chiedere la revoca, inviando una Richiesta di Recupero o Revoca dell'Istanza del Wallet (:ref:`WP_033 <wallet-instance-testcases>`, e :ref:`WP_145 <wallet-instance-optional-testcases>`), a seconda dei casi, all'endpoint :ref:`wallet-provider-endpoint:Endpoint di Gestione dell'Istanza di Wallet` del Backend del Fornitore del Wallet.

Di seguito è riportato un esempio non normativo di una Richiesta di Recupero delle Istanze del Wallet.

.. code-block:: http

   GET /wallet-instances HTTP/1.1
   Host: walletprovider.example.com

In caso di recupero riuscito, il Fornitore di Wallet DEVE restituire una risposta di conferma, con lo stato di tutte le Istanze del Wallet associate all'Utente (:ref:`WP_146 <wallet-instance-optional-testcases>`).
Di seguito è riportato un esempio non normativo di una Risposta di Recupero delle Istanze del Wallet.

.. code-block:: http

   HTTP/1.1 200 OK
   Content-Type: application/json
   Cache-Control: no-store

   [
     {
       "id": "f7b2a8d9",
       "status": "ACTIVE",
       "issued_at": "2024-03-12T10:00:00Z"
     },
     {
       "id": "g8b235c4",
       "status": "REVOKED",
       "issued_at": "2024-02-28T15:30:00Z"
     }
   ]

Una volta che l'Utente identifica l'Istanza del Wallet da revocare, può essere inviata una Richiesta di Revoca dell'Istanza del Wallet all'endpoint, includendo l'ID dell'Istanza del Wallet come parametro di percorso (:ref:`WP_147 <wallet-instance-optional-testcases>`).
Di seguito è riportato un esempio non normativo di una Richiesta di Revoca dell'Istanza del Wallet (:ref:`WP_148 <wallet-instance-optional-testcases>`).

.. code-block:: http

    PATCH /wallet-instances/{f7b2a8d9} HTTP/1.1
    Host: wallet-provider.example.org
    Content-Type: application/json

    {
      "status": "REVOKED"
    }


Risposta alla Revoca dell'Istanza del Wallet
""""""""""""""""""""""""""""""""""""""""""""

In caso di revoca riuscita, il Fornitore di Wallet DEVE restituire una risposta di conferma.
Di seguito è riportato un esempio non normativo di una Risposta di Revoca dell'Istanza del Wallet.


.. code-block:: http

   HTTP/1.1 204 No Content


Meccanismi di Verifica della Revoca
"""""""""""""""""""""""""""""""""""

La verifica della validità dell'Istanza del Wallet DEVE essere eseguita:

- **Durante l'emissione dell’Attestato Elettronico di Attributi** da parte dei Fornitori di Attestati. Solo le istanze del Wallet in stato Operativo o Valido possiedono una Wallet Instance Attestation e una Key Attestation valide. La verifica della validità di un'Istanza del Wallet viene eseguita indirettamente dai Fornitori di Attestati tramite il controllo della presenza di una Wallet Instance Attestation valida (ossia non scaduta, non revocata — verificando la Wallet Instance Attestation Status List — e firmata da un Fornitore di Portafoglio fidato).

- **Durante il periodo di validità dell’Attestato Elettronico di Attributi** da parte dei Fornitori di Attestati, ogni 24 ore mediante la verifica della Wallet Instance Attestation Status List del dell’istanza del Wallet che detiene il PID e la lista di stato della Key Attestation. Infatti, se la Wallet Instance Attestation o Key Attestation viene revocata, il PID in essa contenuto DEVE essere revocato. Di conseguenza, qualsiasi altro Attestato Elettronico ottenuto attraverso la presentazione del PID DEVE anch'esso essere revocato.

- **Durante il ciclo di vita dell'Istanza del Wallet** da parte dell'Istanza del Wallet. Ogni Fornitore di Wallet può implementare metodi diversi per consentire a un'Istanza del Wallet di verificarne il suo stato. La specifica IT Wallet RACCOMANDA di utilizzare la Status List della Wallet Instance Attestation.


.. note::
  Se i Credential Issuer rilasciano credenziali con un periodo di validità inferiore a 24 ore, devono verificare il periodo di validità della WIA e della KA solo al momento del rilascio, come indicato in `EUDI-TS 3`_.

.. note::
  Nell'attuale versione della specifica, i Fornitori di Attestati vengono notificati direttamente della revoca di un'Istanza del Wallet dal Fornitore di Wallet tramite un servizio e-service PDND.

.. note::
  Durante la fase di presentazione degli Attestati Elettronici, una Relying Party può verificare indirettamente la revoca dell'Istanza del Wallet verificando la revoca degli Attestati Elettronici. Quando un'Istanza del Wallet viene revocata, il Fornitore di Wallet revoca le corrispondenti Wallet Instance Attestation, innescando la revoca degli Attestati Elettronici da parte del Fornitore di Attestati Elettronici.



