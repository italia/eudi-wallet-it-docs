.. include:: ../common/common_definitions.rst


Ciclo di Vita degli Attestati Elettronici
=========================================

Il Fornitore di Attestati Elettronici è responsabile della creazione e del rilascio degli Attestati Elettronici, nonché della gestione del loro ciclo di vita e dello stato di validità.

La Fonte Autentica è l'entità responsabile della gestione e della fornitura degli Attributi dell'Utente ai Fornitori di Attestati Elettronici.
Esiste una relazione tra il ciclo di vita degli attributi gestiti dalla Fonte Autentica e il ciclo di vita degli Attestati Elettronici
gestito dal Fornitore di Attestati Elettronici. Infatti, uno dei motivi per la revoca o la sospensione degli Attestati Elettronici è l'aggiornamento/revoca o
sospensione degli attributi contenuti nell'Attestato Elettronico. In IT Wallet, la fornitura degli Attributi dell'Utente e la notifica di
aggiornamenti o modifiche dei relativi stati vengono gestiti utilizzando l'infrastruttura PDND (vedere le relative sezioni per maggiori dettagli).


La :numref:`fig_DigitalCredential_States` mostra gli stati e le transizioni relativi agli Attestati Elettronici.
Include quattro stati distinti: **Issued**, **Valid**, **Expired** e **Revoked**. Mentre, nel caso degli Attestati Elettronici di Attributi (Q)EAA, c'è uno stato aggiuntivo: **Suspended**.
Indipendentemente dallo stato, un Attestato Elettronico può essere eliminato (**PID/(Q)EAA DEL**) e questo termina il suo ciclo di vita.

.. _fig_DigitalCredential_States:
.. plantuml:: plantuml/credential-states.puml
    :width: 80%
    :alt: La figura illustra gli Stati degli Attestati Elettronici.
    :caption: `Transazioni di Stato degli Attestati Elettronici. <https://www.plantuml.com/plantuml/svg/RP9HRzCm4CVV_IbEtSC0AIAK5Q4ze4Lh2fK6b6MRa807BxwrLXmxifsDWFZks8udjr7xLF_kVtS_dN9XBDMsRmNPSOQ0RMS7O6XgpJlBbIHMTM0Lt2jhLGkCQwm39wUGPV0H9Meg7ATRJLimTX1SRbs9c8RBZdh8y87smgwKj1N_W_1clbUiBBLOQAsUBfLG6ku5hPkZzKz8MUX_EorVSOatErut4es1UNJxJ1k4McbdQ81A1iB539XMARj3VUYeLI_PPGZ3F8VuEmL1zHPr70EQCjwRr1P6sg53w9GO_2EszIOXFzkweqIj9JvuQBou2HB-7nH2L2EY1cRk1UDp1l2Nn4pLcmubGmOdgrMnoFF8h_5HDPuktvqjpXQHbhyxhXEDwsyqbOPRhcHO_ZnwRKoFxAk-euApe30IK1e2cpaD6Ar702Tv_Zvt3Wx_UFKBCistEvjzWDXu3flrylMBRo_BelWfrrK5168jPVsaQVJHCsu729-c8V-SvA5UnjIJTDtf7kVmt5tTLfjft4NZYIQhhiixE1AEbvk4o-yRGjBAhEzSzB0vQTn-yI8fFf7O5vY4qlAznK326T974a_WBp_HN9PNvCADwrln7m00>`_


.. .. figure:: ../../images/DigitalCredential_States.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/png/RP9HRzCm4CVV_IbEtSC0AIAK5Q4ze4Lh2fK6b6MRa807BxwrLXmxifsDWFZks8udjr7xLF_kVtS_dN9XBDMsRmNPSOQ0RMS7O6XgpJlBbIHMTM0Lt2jhLGkCQwm39wUGPV0H9Meg7ATRJLimTX1SRbs9c8RBZdh8y87smgwKj1N_W_1clbUiBBLOQAsUBfLG6ku5hPkZzKz8MUX_EorVSOatErut4es1UNJxJ1k4McbdQ81A1iB539XMARj3VUYeLI_PPGZ3F8VuEmL1zHPr70EQCjwRr1P6sg53w9GO_2EszIOXFzkweqIj9JvuQBou2HB-7nH2L2EY1cRk1UDp1l2Nn4pLcmubGmOdgrMnoFF8h_5HDPuktvqjpXQHbhyxhXEDwsyqbOPRhcHO_ZnwRKoFxAk-euApe30IK1e2cpaD6Ar702Tv_Zvt3Wx_UFKBCistEvjzWDXu3flrylMBRo_BelWfrrK5168jPVsaQVJHCsu729-c8V-SvA5UnjIJTDtf7kVmt5tTLfjft4NZYIQhhiixE1AEbvk4o-yRGjBAhEzSzB0vQTn-yI8fFf7O5vY4qlAznK326T974a_WBp_HN9PNvCADwrln7m00

..     Digital Credential Lifecycle.

.. note::
  Gli Utenti POSSONO presentare un Attestato Elettronico in qualsiasi stato, spetta alla policy della Relying Party accettare un Attestato Elettronico non Valido.
  Un esempio di questo scenario è quando una Relying Party deve verificare che l'Utente non sia minorenne. In questo caso, anche se l'Utente presenta un
  Attestato Elettronico **Issued/Expired/Revoked** o **Suspended**, l'attributo relativo all'età è ancora affidabile.

.. note::
  Mentre **Issued**, **Valid**, **Expired**, **Revoked** sono esplicitamente menzionati nell'ARF (vedi Figura 5 di ARF v1.4),
  **Suspended** è implicitamente presente in `EIDAS-ARF`_. Questa specifica lo considera esplicitamente.

Transizioni degli Attestati Elettronici
---------------------------------------

Transizione dell'Attestato Elettronico a Issued
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Affinché la macchina a stati possa avviarsi, l'Istanza del Wallet DEVE essere nello stato **Operational** o **Valid**, consentendo il rilascio di Attestati Elettronici.
La macchina a stati inizia con lo stato **Issued**, quando viene attivato un processo di emissione e, di conseguenza, un Attestato Elettronico viene rilasciato all'
Istanza del Wallet (**PID/(Q)EAA ISS**). Si prega di fare riferimento a :ref:`credential-issuance:Emissione di Attestati Elettronici`.

Transizione dell'Attestato Elettronico a Valid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un Attestato Elettronico passa allo stato **Valid** quando:

  * raggiunge la sua data di inizio validità;
  * viene attivato un processo di riattivazione se l'Attestato Elettronico di Attributi (Q)EAA è stato sospeso.


Transizione dell'Attestato Elettronico a Expired
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un Attestato Elettronico passa naturalmente allo stato **Expired** quando scade automaticamente al raggiungimento della sua data di fine validità (**PID/(Q)EAA EXP**),
indicando che non è più valido per l'uso.

Se un Attestato Elettronico è **Expired**, l'Istanza del Wallet DOVREBBE notificare all'Utente che l'Attestato Elettronico è scaduto e l'Utente PUÒ eliminarlo (**PID/(Q)EAA DEL**).
Questo termina il suo ciclo di vita.

Transizione dell'Attestato Elettronico a Revoked
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un Attestato Elettronico passa dagli stati **Issued**, **Valid** o **Suspended** allo stato **Revoked** quando viene attivamente revocato dal Fornitore di Attestati Elettronici
tramite un processo di revoca (**PID/(Q)EAA REV**). Le Relying Party NON DOVREBBERO più considerare utilizzabile un particolare Attestato Elettronico quando è **Revoked**, anche se è
ancora temporalmente valido e contiene una firma valida del Fornitore di Attestati Elettronici. La revoca può avvenire nei seguenti casi:

  * per motivi tecnici di sicurezza relativi alla compromissione del materiale crittografico;
  * in caso di richieste esplicite dell'Utente;
  * come conseguenza di un aggiornamento degli attributi da parte delle Fonti Autentiche;
  * in caso di revoca degli attributi contenuti nell'Attestato Elettronico notificata dalla Fonte Autentica;
  * morte dell'Utente;
  * revoca dell'Istanza del Wallet a cui è stato rilasciato l'Attestato Elettronico;
  * attività illegali dell'Utente segnalate da Organi Giudiziari o di Vigilanza.

Nel caso del solo PID e IT-Wallet ID, i seguenti casi si aggiungono a quelli sopra elencati:

  * rilevamento di una violazione dell'identità digitale rilasciata da un Gestore di Identità Digitale e utilizzata per autenticare l'Utente durante il rilascio del PID/IT-Wallet ID;
  * come risultato dell'ottenimento di un nuovo PID/IT-Wallet ID su una nuova Istanza del Wallet dallo stesso Fornitore di Wallet che ha fornito l'Istanza del Wallet contenente un PID/IT-Wallet ID precedentemente rilasciato.

.. note::
  Un Fornitore di Attestati Elettronici di Attributi (Q)EAA PUÒ revocare un Attestato Elettronico di Attributi (Q)EAA in caso di revoca del PID/IT-Wallet ID.

Quando un Attestato Elettronico è **Revoked** non può tornare allo stato **Valid**, l'Istanza del Wallet DOVREBBE notificare all'Utente che l'Attestato Elettronico
è stato revocato e l'Utente PUÒ eliminarlo (**PID/(Q)EAA DEL**). Questo termina il suo ciclo di vita.

Transizione dell'Attestato Elettronico a Suspended
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un Attestato Elettronico di Attributi (Q)EAA passa dagli stati **Issued** o **Valid** allo stato **Suspended** quando viene sospeso dal Fornitore di Attestati Elettronici (**(Q)EAA SUSP**).
L'Attestato Elettronico di Attributi (Q)EAA rimane **Suspended** fino a quando non viene ripristinato allo stato **Issued** o **Valid** (**(Q)EAA UNSUSP**) a seconda dello stato precedente, cioè
le condizioni che hanno portato alla sua sospensione vengono risolte, o passa a **Revoked**, **Expired** o viene eliminato. La sospensione di un Attestato Elettronico di Attributi (Q)EAA PUÒ essere:

  * Guidata dal caso d'uso, basata sullo stato di validità degli attributi contenuti nell'Attestato Elettronico di Attributi (Q)EAA. In questo caso, una Fonte Autentica aderente a PDND DEVONO notificare al Fornitore di Attestati Elettronici qualsiasi cambiamento nello stato degli attributi attestati dall'Attestato Elettronico di Attributi (Q)EAA.
  * Esplicitamente richiesta dall'Utente.


Ciclo di vita degli Attestati Elettronici ottenuti in batch
-----------------------------------------------------------

Ciascuna degli Attestati Elettronici emessi in batch, entra immediatamente nel proprio stato relativo al ciclo di vita. Tutte le transizioni di stato (Emessa → Valida → Scaduta/Sospesa/Revocata) avvengono a livello di singolo Attestato Elettronico, utilizzando i parametri individuali dell'Attestato Elettronico (ad esempio, date di validità, Status List).


Gestione del Ciclo di Vita degli Attestati Elettronici
------------------------------------------------------

Mentre la :numref:`fig_DigitalCredential_States` mostra i diversi stati che un Attestato Elettronico può acquisire durante il suo ciclo di vita,
la :numref:`fig_DigitalCredential_Lifecycle` mostra il punto di vista delle Istanze del Wallet e dei Fornitori di Attestati Elettronici nella gestione del ciclo di vita degli Attestati Elettronici
e l'effetto sul loro storage locale.

.. _fig_DigitalCredential_Lifecycle:
.. plantuml:: plantuml/credential-lifecycle.puml
    :width: 99%
    :alt: La figura illustra il Ciclo di Vita degli Attestati Elettronici.
    :caption: `Gestione del Ciclo di Vita degli Attestati Elettronici. <https://www.plantuml.com/plantuml/svg/ZLDTQnGn57tFhpW-sKAh1VkqzQErYr1GA5Kf8YBfp9sTO3PPSs-whR_U9BiRTvU8teSX8VUSSp_EdBFe875krHFZEXjxmilBq-UNfz-dZqxFJVTQALLobFD226OsYheToK5ZQcP6jCLbe9wSc7HqH3r3FEu8ST5heVu8Cj9spXLpfC3uSF45JAw7Hk8sW-cq6EyIkY0-CmL4Dcu6ZK0pmqA913xAiH-ExtH2Tdu-Zsu3x4Rj7DbdAfFcSfMQ51Q_8CUurTQIuCgnQDVHcO82CBaX2ORk2Hz5IsIyJqBuv7-Gm-13JW6BJyfRFN020qK3bWOfjnlw6KtEM-RnE8zxRKsVdnhKz93EN1vhjVbY1XpyqTa0ZSFNauUJ5qT8txVVtXn2iiR18_5XWO4i4mwSFuJ2Th3uXS9QnWoglcQXYwuZvdL5fTfzvXgLjYhLvqftGqCW7l-F3vYave9W5_NE-kLgk2szTcSbwZuKTcEbeXqSBOltyl8n99tzpAMHiTZkAUCYvhfbOwtjrFsLbQW3Rj_g8HiIqsj_ZPtXYqTO-x2cfdeRlrWTphvLU6MLLyKYVv_x9DkKM4gZfKqVpA_IvLbhtrLg9v-ugR2zMn-ejD0glRtNzcRhBDl0Vokst3-PaYKXB0BT6nzv1wDA0US94kVsDm00>`_

.. .. figure:: ../../images/DigitalCredential_Lifecycle.svg
..     :figwidth: 100%
..     :target: https://www.plantuml.com/plantuml/svg/XP91Yzim48Nl_XMgsOC3sVMbfq9WKzjq0sbZR8UbK0YoDIW2MV9AetL3wN-lvBPkIbro2T7JzvxVY7cqI0swNaPlXEgaOq3EY8DzbwQ6ZWzSuDcrpeBfj49G-D3fFXqaLS5pRv59qQRPs_ioICUF-xId5i5uwPHv1nKApCCGyfzsUN6gcw8g3itdiaXMKLG_7PvFPL7LXq-dyb0rrNRN17tBM0MoeJo9MHkloHt2Lyoqr6OJQqCLXo1AdxqerdYHG3Oaf_OCRE-LPELJtskd63MNnBLh4ZzJAG79JbcagWFo-pPUaMyHYGYfBnQXJsZtukbSS85Kaim00uN2_zrsBqvOWKAhs1Fnwe-7WLpsv23Xok0TyoFbRJ9Qr6OTr_wNSfX3e-_HLVakbB-At5dhmFnTVox2GIqN-G0A35tgRk1rsLB1g-ucI_f5rSuEe6mu79MT3tFOzLZJL6GUwnya6LoupobIKZh3XU8JjBwpWn48czZeLgCtXOUeGFxi-2lsMERRfWY6QL4ejvkmDAi0XkGPp8jzyL-GWvh1h2gM4oToseVn5Xh8QGl6Mr-Vvnbl3VG8YhbU_W00

..     Digital Credential Lifecycle Management.

Un Utente, attraverso l'Istanza del Wallet, è in grado di acquisire un nuovo Attestato Elettronico (**Credential Acquisition**) eseguendo il processo **PID/(Q)EAA ISS**. Questo DEVE risultare nella memorizzazione di un
Attestato Elettronico nello stato **Issued/Valid**, ed sua eliminazione quando non è più necessario o è **Expired/Revoked** (**Credential Deletion**).
Fino alla **Credential Deletion**, un Attestato Elettronico può essere presentato alle Relying Party, questa operazione non influenzerà il suo ciclo di vita.

Un Fornitore di Attestati Elettronici invece è responsabile per:

  * **Generazione dell'Attestato Elettronico**: l'Attestato Elettronico viene generato come conseguenza di una richiesta di emissione e DEVE essere aggiunto allo storage locale del Fornitore di Attestati Elettronici dopo l'emissione riuscita.
  * **Revoca/Sospensione/Riattivazione dell'Attestato Elettronico** (**PID/(Q)EAA REV** e **(Q)EAA SUSP/UNSUSP**): per motivi di sicurezza tecnici o richiesti da entità esterne (ad esempio, Utenti e Fonti Autentiche) lo stato dell'Attestato Elettronico DEVE essere aggiornato localmente.
  * **Eliminazione dei Dati**: dopo aver raggiunto lo stato **Expired**, e in base alle politiche di conservazione del Fornitore di Attestati Elettronici, gli Attestati Elettronici DEVONO essere rimossi dallo storage locale del Fornitore di Attestati Elettronici.

Revoca e Sospensione degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione descrive i flussi per richiedere un aggiornamento dello stato di un Attestato Elettronico (cioè revoca o sospensione), le entità coinvolte e i meccanismi di validazione per gli Attestati Elettronici nel sistema IT-Wallet.

Come evidenziato nella Sezione :ref:`credential-revocation:Ciclo di Vita degli Attestati Elettronici`, il ciclo di vita di un Attestato Elettronico è influenzato da:

  - Il ciclo di vita della sua Istanza del Wallet
  - La validità degli Attributi gestiti dalle Fonti Autentiche
  - Solo per i PID, lo stato dell'Identità Digitale utilizzata per l'autenticazione dell'Utente

Fattori esterni relativi all'utente possono anche influenzare il ciclo di vita di un Attestato Elettronico, come:

  - Richiesta esplicita dal titolare dell'Attestato Elettronico
  - Morte dell'Utente
  - Attività illegali

Entità Coinvolte
^^^^^^^^^^^^^^^^

Mentre il Fornitore di Attestati Elettronici DEVE gestire direttamente lo stato di validità degli Attestati Elettronici che ha emesso, altri attori POSSONO attivare il processo di revoca/sospensione dell'Attestato Elettronico:

  - Utenti, attraverso:

    - La loro Istanza del Wallet
    - Servizio web fornito dal Fornitore di Attestati Elettronici

  - La Fonte Autentica quando gli attributi dell'Attestato Elettronico vengono aggiornati o cambiano stato di validità
  - Il Fornitore di Wallet quando revoca un'Istanza del Wallet
  - Il Gestore di Identità Digitale se l'Identità Digitale utilizzata per il rilascio del PID/IT-Wallet ID è stata rubata o compromessa
  - Autorità legali o l'Organo di Vigilanza in caso di attività illegali comprovate

La seguente figura mostra un diagramma delle relazioni tra entità relative al flusso di aggiornamento dello stato.

.. _fig_entity-relation-credential-revocation:
.. plantuml:: plantuml/credential-revocation-entities.puml
    :width: 99%
    :alt: La figura illustra le Entità coinvolte nel Flusso di Revoca degli Attestati Elettronici.
    :caption: `Entità coinvolte nel Flusso di Revoca degli Attestati Elettronici. <https://www.plantuml.com/plantuml/svg/RPJDZjCm4CVlUOgX5ne9QIzxH6ZPR1150gfs4U8KkV5GHgHsv8-KW7XtngcJXhYLAjUJcVd_vYDzi4uOvqyDbCgH8xH0gjDDXv9_G65G8ZyG3UomqxLmf1MyQ_GvUq6gRhn4U5tStnNtLQ5FhLRi_2RBtc-Uoch_NExApy_VjkKwpx8j6glLsbiqhs3rXOyLduDe3_giI1r1qf4SIzMJgbrnwAFsIWhJhy-YQT1LjhSEJnpzTRZ3VhYlSlYJ0NycaD6V51UfQhn6RA8b88JlHw744Iq4kfSMdY97CUUudRirkYF9DOsfjz4mfevt2mjf44h26G_0aXtL61J-PjbLG7Zt8uZNbTNU3FHlHnFi1rEY4TeAmZb31-_uxZHm16oizMW6nLEiD9WxqP0CxMSYvmF0f5wLlou4sj1lbDL1opu0J9PfNKQ6lMz38LQR_d5m_k0brM5nOf1ZsqRYPU1Jb_9voJHmSh9huoFxg3BSx7-LfCCQ7iV1s6MFPt9ntQhhkh52ccxKBhHoWfITDpWefMtCiXqsSTMNUmAhy2BzH5YkOfu6pHRt2Tc0SwgvVspSbFj64Va5Ai59fMxpsIYO-4_QdxIZx_sjUSW0Jrg552b3cc8X3MRwwubb92z7ccCs9DzA4SurJyhpgSroPdaaIpP-cNN3OCUmqxMZxhB_aIXwfZirTVHkxssBIdB40n_-rFm3>`_


.. .. figure:: ../../images/entity-involved-credential-revocation.svg
..   :figwidth: 100%
..   :align: center
..   :target: https://www.plantuml.com/plantuml/svg/RPFFRjGm4CRlUOfXBsmasbmuSIhTHc8HXLMt5U8KUMEpjN3io1xl4X3lpjXrcYZUI9NhgUVxVlEdDmwPHT-fedWZTQiy5_2CsBiFLMNP-VeeyTaVl1EsDHg5nklMT5Mlc0v9LmwvaeTgy_vg5q9Fzr-gZZaKbaBDndIzqI6dZmQVjdTrit-i7-flZpzszReiYfsmpkXrq7y7goSwLdJM6YKEOCvQwYDmIH1CGMi59p79b5jHwgtncZCxhCzCAO6D6yYte-plyGxxU5-LyBS0-bvXnlTIEsIw5LF6DaK2GlYvPveTXOD0zzR1NUBOp3akQ_VMd2IdcaRfNGgCqkdkO64DJ7CuYmEGvKcs8ZZyAuh9W7by3kPjuuotaVxZ689z36KUeQt04AqyUAGx6g0Cs3hdXOsENQeqX4zCIHxQJqJe2M1oR-hVBmJ6oZ-2DmV3XmWmHY1EJWetCknz7mfnnWwtyV5dpsKhcOAKX1JRSX47FdMfd9Si8oU9JOrFxADBlBbP9PU65V-S1kEMFPxPfNLhfdKZXrnkzDuOZKngDszmSChRM1GFGgLLN-u9h1x4oVmIi5p5SfQKB-wTe82OKytVXyRDjIyKKRv0PJYvrMK-bmoNxoVlhmRbp-7IF7Y0bqO7YPmXarXQWoMYbYM5897zSsGQyo7vdhDmhcbIdavZbpCh4rcsyKlLBO4TmqwtA4zn_qUYz3BVgTUELdllUg5vo0ZV3VtkE_KV

..   Entities involved in Credential Revocation Flow


Flussi di Aggiornamento dello Stato
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione descrive i principali flussi per la gestione degli Aggiornamenti di Stato degli Attestati Elettronici da parte del Fornitore di Attestati Elettronici, in particolare l'Aggiornamento di Stato:

  - relativo all'Utente;
  - attivato da un'Istanza del Wallet;
  - attivato da un Fornitore di Wallet;
  - attivato da una Fonte Autentica.

.. note::
  I Flussi dettagliati di Aggiornamento dello Stato per i Gestori di Identità Digitale, le autorità legali e l'Organo di Vigilanza saranno trattati nelle versioni future della specifica tecnica.

Aggiornamento dello Stato relativo all'Utente
"""""""""""""""""""""""""""""""""""""""""""""

Gli Utenti POSSONO modificare lo stato di validità del loro Attestato Elettronico:

  1. Eliminando l'Attestato Elettronico dalla propria Istanza del Wallet: l'Istanza del Wallet DOVREBBE proporre all'Utente un prompt per notificare opzionalmente al Fornitore di Attestati Elettronici il desiderio da parte dell'Utente di richiedere la revoca della Credenziale. Quando l'Utente utilizza questa funzionalità, la notifica da inviare al Fornitore di Attestati Elettronici DEVE utilizzare il Notification Endpoint messo a disposizione dal Fornitore di Attestati Elettronici, come descritto nella Sezione :ref:`credential-revocation:Aggiornamento dello Stato da parte dell'Istanza del Wallet`.
  2. Utilizzando il portale web del Fornitore di Attestati Elettronici:

    a. Gli Utenti POSSONO accedere ad un'area sicura con almeno lo stesso Livello di Garanzia utilizzato durante la fase di emissione.
    b. Il Fornitore di Attestati Elettronici DEVE consentire agli Utenti di:

      - Visualizzare tutti i loro Attestati Elettronici contenuti nel database del Fornitore di Attestati Elettronici.
      - Verificare l'autenticità dei dati.
      - Visualizzare e aggiornare lo stato di validità (revocare i loro Attestati Elettronici e, se supportato dal Fornitore di Attestati Elettronici, sospenderle).

Inoltre, quando gli Utenti rilevano dati non corretti in un Attestato Elettronico rilasciato, l'Istanza del Wallet DOVREBBE avviare una richiesta di correzione dati tramite il Notification Endpoint come specificato in :ref:`credential-issuance-endpoint:Correzione dati usando credential_failure`. A seguito della conferma della discrepanza, il Fornitore di Attestati Elettronici DOVREBBE seguire il :ref:`credential-issuance-low-level:Re-Issuance Flow`.

.. note::
  Se l'Utente attiva un'altra Istanza del Wallet dello stesso Fornitore di Wallet e utilizzando la stessa Soluzione di Wallet e ottiene un nuovo PID/IT-Wallet ID, il precedente PID/IT-Wallet ID DEVE essere revocato. In caso di revoca del PID la precedente Istanza del Wallet DEVE passare allo stato operativo.

In caso di morte dell'Utente, i Fornitori di Attestati Elettronici DEVONO garantire che gli Attestati Elettronici e le Istanze del Wallet di proprietà dell'Utente siano revocati.
La morte dell'Utente comporta una modifica dello stato di validità degli attributi identificativi dell'Utente contenuti nel registro pubblico (ANPR). La morte dell'Utente DEVE produrre la revoca del PID/IT-Wallet ID. Pertanto, la Fonte Autentica del PID/IT-Wallet ID (ANPR) DEVE notificare al PID/EAA Provider che gli attributi dell'Utente non sono più validi a causa della morte dell'Utente. La Fonte Autentica e il PID/EAA Provider DEVONO utilizzare i meccanismi previsti nella Sezione :ref:`credential-revocation:Aggiornamento dello Stato da parte delle Fonti Autentiche`.

.. note::
  Le versioni future della presente specifica tecnica definiranno come le informazioni verso i Fornitori di (Q)EAA vengono propagate, in accordo alla normativa nazionale. Inoltre, saranno definite procedure automatizzate per la revoca degli Attestati dovuta ad attività illecite.

Aggiornamento dello Stato da parte dell'Istanza del Wallet
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Quando l'Utente elimina un Attestato Elettronico dall'Istanza del Wallet, per impostazione predefinita l'Istanza del Wallet NON DEVE notificare questo evento al Fornitore di Attestati Elettronici. L'eliminazione dall'Istanza del Wallet rimuove solo la copia locale e non modifica lo stato di validità presso il Fornitore di Attestati Elettronici.

L'Istanza del Wallet PUÒ informare l'Utente, prima dell'eliminazione, che l'eliminazione è un'azione locale e non implica la revoca presso il Fornitore di Attestati Elettronici, e PUÒ implementare, con il consenso esplicito dell’Utente al momento dell’eliminazione, una funzionalità di notifica per informare il Fornitore di Attestati Elettronici dell’intenzione dell’Utente di revocare l’Attestato Elettronico.

Se l'Utente desidera che il Fornitore di Attestati Elettronici revochi un Attestato Elettronico, DOVREBBE confermare esplicitamente tale intenzione tramite il prompt di eliminazione dell’Istanza del Wallet (quando disponibile), che a sua volta DEVE notificare il Fornitore di Attestati Elettronici; in alternativa, l'Utente PUÒ utilizzare il portale web del Fornitore di Attestati Elettronici o altri canali messi a disposizione.

Quando l'Attestato Elettronico revocato è il PID/IT-Wallet ID, il Fornitore di Attestati Elettronici DEVE inviare una notifica di questo evento all'Utente entro 24 ore.
Per qualsiasi altro Attestato Elettronico diverso dal PID/IT-Wallet ID, il Fornitore di Attestati Elettronici DOVREBBE inviare una notifica di questo evento all'Utente. La notifica all'Utente PUÒ essere implementata in diversi modi, ad esempio utilizzando l'indirizzo email dell'Utente, il numero di telefono o qualsiasi altro canale di comunicazione verificato e sicuro. La notifica all'Utente DEVE includere anche tutte le informazioni sullo stato di revoca dell'Attestato Elettronico. Il metodo utilizzato per la notifica all'Utente è fuori dallo scopo del presente profilo tecnico di implementazione. Quando la revoca avviene, il Fornitore di Attestati Elettronici DEVE aggiornare di conseguenza lo stato dell'Attestato Elettronico. Quando la Notification Response inviata dal Fornitore di Attestati Elettronici viene ricevuta con successo dall'Istanza del Wallet, l'Istanza del Wallet DEVE eliminare l'Attestato Elettronico.

Aggiornamento dello Stato da parte dei Fornitori di Wallet
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

In caso di smarrimento o furto del dispositivo, oppure in presenza di una vulnerabilità generale, il Wallet Provider DEVE revocare la Wallet Instance. Pertanto, il Wallet Provider DEVE garantire che lo stato aggiornato sia riportato nella status list della relativa Wallet Instance Attestation. In caso di vulnerabilità della WSCD, il Wallet Provider DEVE revocare la relativa Key Attestation.
In aggiunta a quanto già definito in :ref:`credential-revocation:Ciclo di Vita degli Attestati Elettronici`, il Credential Issuer DEVE implementare un meccanismo di monitoraggio degli stati correnti di tutte le Wallet Instance Attestation e Key Attestation associate alle Wallet Instance alle quali sono state rilasciate le Credenziali.
Dopo la revoca della Wallet Instance Attestation, il Credential Issuer procede alla revoca di tutti gli Attestati Elettronici emessi per la Wallet Instance.

Aggiornamento dello Stato da parte delle Fonti Autentiche
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Le Fonti Autentiche gestiscono gli attributi separatamente dagli Attestati Elettronici, i quali verificano l’autenticità in modo analogo ai documenti fisici. La perdita di un documento fisico non implica la perdita dei diritti che rappresenta; significa solo che l’Utente non può dimostrarli. Tuttavia, se un Utente perde determinati diritti a causa di una grave infrazione, la Fonte Autentica revocherà gli attributi correlati. In tali casi, quando gli attributi di un Utente vengono aggiornati, le Fonti Autentiche DEVONO notificare ai Fornitori di Attestati Elettronici di aggiornare lo stato di validità di qualsiasi Attestato Elettronico che contenga tali attributi.

Le Fonti Autentiche che utilizzano PDND DEVONO usare Signal Hub come unico meccanismo di notifica degli aggiornamenti. In questo caso, le Fonti Autentiche DEVONO depositare un Signal tramite il :ref:`signal-hub-endpoint:e-Service di Raccolta Segnali` nei seguenti casi:

  - Il valore di uno o più Attributi contenuti nel database della Fonte Autentica è cambiato;
  - Lo stato di validità degli Attributi è aggiornato (revoca o sospensione).

In entrambi i casi, il Signal DEVE avere ``signalType`` impostato a ``UPDATE``.

I Fornitori di Attestati Elettronici DEVONO controllare periodicamente il PDND Signal Hub :ref:`signal-hub-endpoint:e-Service di Distribuzione Segnali` per nuovi Signal. Per il flusso di processamento dei Signal, fare riferimento alla Sezione :ref:`signal-hub-endpoint:Elaborazione dei Segnali`. Il Fornitore di Attestati Elettronici è in grado di identificare la natura del ``UPDATE`` Signal interrogando la API `get attribute` della Fonte Autentica e ispezionando il payload della risposta, come descritto nella Sezione :ref:`authentic-source-endpoint:Get Attribute Claims`.

La seguente figura illustra ad alto livello il processo di aggiornamento dello stato da parte delle Fonti Autentiche.

.. only:: format_html

  .. figure:: ./images/svg/status-update-as.svg
    :alt: Processo di aggiornamento dello stato per le Fonti Autentiche
    :width: 100%

    Processo di aggiornamento dello stato delle Fonti Autentiche

.. only:: format_latex

  .. figure:: ./images/pdf/status-update-as.pdf
    :alt: Processo di aggiornamento dello stato per le Fonti Autentiche
    :width: 100%

Il processo inizia con modifiche ai dati o alla validità dei dati che avvengono presso la Fonte Autentica. Le modifiche possono anche essere avviate da entità terze diverse dalla Fonte Autentica, ad esempio quando le autorità giudiziarie segnalano attività illecite.

Una volta che i dati cambiano, la Fonte Autentica notifica i Fornitori di Attestati Elettronici che hanno ricevuto i dati originali utilizzando il Signal Hub. La Fonte Autentica deposita un Signal nel Signal Collection e-Service. :ref:`signal-hub-endpoint:e-Service di Raccolta Segnali`.

Il Fornitore di Attestati Elettronici interroga periodicamente il Signal Hub :ref:`signal-hub-endpoint:e-Service di Distribuzione Segnali` per nuovi Signal. Quando viene trovato un nuovo Signal, il Fornitore di Attestati Elettronici lo recupera e lo processa come descritto in :ref:`signal-hub-endpoint:Elaborazione dei Segnali`. Quindi, il Fornitore di Attestati Elettronici aggiorna lo Stato dell’Attestato secondo la modalità definita dal meccanismo di validità. Il Fornitore di Attestati Elettronici PUÒ notificare l’Utente tramite un canale di comunicazione registrato e out-of-band.

L’Istanza del Wallet, a seguito di controlli periodici dello stato di validità degli Attestati Elettronici memorizzati, riceve lo stato aggiornato. Quando lo Stato dell’Attestato viene modificato in ``INVALID``, il Fornitore di Attestati Elettronici DEVE informare l’Utente di tale cambiamento. Nel caso in cui lo stato dell’Attestato venga modificato in ``UPDATE`` (risp. 0x03) o ``ATTRIBUTE_UPDATE`` (risp. 0x0F), l’Istanza del Wallet DOVREBBE procedere alla riemissione dell’Attestato Elettronico, come descritto in :ref:`credential-issuance-low-level:Re-Issuance Flow`.


Gestione del ciclo di vita delle Credenziali in batch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quando più Attestati Elettronici vengono emessi insieme in un singolo batch, il loro ciclo di vita rimane completamente granulare:

  * **Trigger raggruppati, aggiornamenti indipendenti**: indipendentemente dall'attore che ha innescato la variazione di stato del batch (ad esempio, la Wallet Instance tramite il Notification Endpoint con ``event=credential_deleted``, un Wallet Provider tramite l'aggiornamento della Status List della Wallet Instance e Key Attestations) l'aggiornamento viene gestito come una o più modifiche di stato separate. Il Fornitore di Attestati Elettronici aggiorna lo stato di ciascun Attestato Elettronico singolarmente (ad esempio, impostando il bit della status-list su ``INVALID`` o ``SUSPENDED``). Un'Istanza del Wallet NON DEVE attivare aggiornamenti di stato del batch quando l'Utente elimina Attestati Elettronici localmente. In fase di eliminazione, l’Istanza del Wallet PUÒ, con il consenso esplicito dell’Utente, notificare al Fornitore di Attestati Elettronici l’intenzione dell’Utente di revocare gli Attestati Elettronici interessati.

.. note::
  Poiché l'interfaccia utente del Wallet in genere visualizza un batch come un singolo Attestato Elettronico (ad esempio, con 3 utilizzi rimanenti), un'eliminazione da parte dell'utente rimuove l'intero batch localmente. Per impostazione predefinita non richiede la revoca presso il Fornitore di Attestati Elettronici. L’Istanza del Wallet PUÒ offrire all’Utente un prompt opzionale per richiedere la revoca presso il Fornitore di Attestati Elettronici nell’ambito del flusso di eliminazione.


Meccanismi di Verifica della Validità
-------------------------------------

Per la verifica dello stato di validità di un Attestato Elettronico a lunga durata, Token Status List (`TOKEN-STATUS-LIST`_) DEVE essere supportato sia per lo scenario remoto che per quello di prossimità. La seguente tabella riassume i meccanismi di revoca richiesti per verificare lo stato degli Attestati Elettronici a lunga durata.

.. _table_revocation_mechanisms:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Flusso**
    - **Meccanismo di Revoca**
    - **Riferimento**
  * - Remoto
    -
      - [OBBLIGATORIO] Token Status List.
    - `TOKEN-STATUS-LIST`_.
  * - Prossimità
    - [OBBLIGATORIO] Token Status List.
    - `TOKEN-STATUS-LIST`_.


Token Status Lists
^^^^^^^^^^^^^^^^^^

Questa sezione definisce una struttura di dati Status List, che viene utilizzata per trasmettere informazioni riguardanti gli stati individuali di più Attestati Elettronici. Gli Attestati Elettronici possono essere di qualsiasi formato, come SD-JWT o mdoc ISO/IEC 18013-5. Una Status List descrive lo stato degli Attestati Elettronici codificando la loro validità in un array di bit. A ciascun Attestato Elettronico viene assegnato un indice durante l'emissione; questo indice rappresenta la sua posizione all'interno dell'array di bit. Il valore del bit o dei bit in questo indice corrisponde allo stato degli Attestati Elettronici. Una Status List viene fornita all'interno di un Token di Status List firmato crittograficamente in formato JWT. Per i dettagli, vedere `TOKEN-STATUS-LIST`_.

In questa specifica, i ruoli di Fornitore di Attestati Elettronici e Status Issuer (cioè, l'entità che emette il Token di Status List sulle informazioni di stato dell'Attestato Elettronico) coincidono, mentre lo Status Provider (cioè, l'entità che fornisce il Token di Status List su un endpoint pubblico) PUÒ essere il Fornitore di Attestati Elettronici stesso o un'altra entità.

Il Fornitore di Attestati Elettronici DEVE

  - definire un numero di bit, k, (1, 2, 4 o 8) che rappresenta la quantità di bit utilizzati per descrivere lo stato di ciascun Attestato Elettronico all'interno di questa Status List. Il Fornitore di Attestati Elettronici DEVE configurare il numero di bit. Ogni Attestato Elettronico avrà quindi 2^k (dove k è il numero di bit scelto) possibili stati.
  - creare un array di byte di dimensione = (quantità di Attestati Elettronici) * k / 8 o maggiore. A seconda di k, ogni byte nell'array corrisponde a 8/k stati (8 se k=1, 4 se k=2, 2 se k=1, o 1 se k=8). Ogni volta che viene emesso un Attestato Elettronico, il Fornitore di Attestati Elettronici lo assegna a una posizione nell'array.
  - impostare i valori di stato per tutti gli Attestati Elettronici emessi all'interno dell'array di byte. Lo stato di ciascun Attestato Elettronico viene identificato utilizzando un indice che mappa a uno o più bit specifici all'interno dell'array di byte. L'indice inizia a contare da 0 e termina con (quantità di Attestati Elettronici) - 1 (essendo l'ultima voce valida). I bit all'interno di un array vengono contati dal bit meno significativo ("0") al bit più significativo ("7"). Tutti i bit dell'array di byte a un particolare indice sono impostati su un valore di stato.
  - comprimere l'array di byte utilizzando DEFLATE [:rfc:`1951`] con il formato dati ZLIB [:rfc:`1950`]. Si RACCOMANDA alle implementazioni di utilizzare il livello di compressione più alto disponibile.
  - rendere disponibile alle Relying Party e alle Istanze del Wallet un endpoint per richiedere le Status Lists.

Il Fornitore di Attestati Elettronici DEVE utilizzare i seguenti valori per i possibili Stati degli Attestati Elettronici emessi:

  - 0x00 - ``VALID`` - L'Attestato Elettronico è valido.
  - 0x01 - ``INVALID`` - L'Attestato Elettronico è revocato.
  - 0x02 - ``SUSPENDED`` - L'Attestato Elettronico è temporaneamente non valido, sospeso. Questo stato è solitamente temporaneo.
  - 0x03 - ``UPDATE`` - I parametri dei metadata dell'Attestato Elettronico sono cambiati.
  - 0x0F - ``ATTRIBUTE_UPDATE`` - Gli attributi dell'Attestato Elettronico sono cambiati.

Ad esempio, se sono possibili cinque stati per un certo Attestato Elettronico, allora k=4. Se il Fornitore di Attestati Elettronici crea un array per memorizzare gli stati di 6 Attestati Elettronici, i cui stati di validità sono 0, 0, 0, 3, 1, 2, rispettivamente; farà:

  - creare l'array di bit ``[0, 0, 0, 0, 0, 0, 0, 0; 0, 0, 1, 1, 0, 0, 0, 0; 0, 0, 1, 0, 0, 0, 0, 1]`` che in notazione esadecimale genera l'array di byte ``[0x00, 0x30, 0x21]``.
  - comprimere l'array utilizzando DEFLATE.

.. note::
  Quando il Fornitore di Attestati Elettronici sceglie il numero di bit per trasmettere gli stati degli Attestati Elettronici che emette, PUÒ aggiungere altri stati oltre a quelli descritti sopra. L'aggiunta di molti stati diversi per il ciclo di vita di un Attestato Elettronico deve tuttavia essere attentamente ponderata poiché rivela informazioni alle Relying Party.

.. note::
  La principale considerazione sulla privacy per una Status List è impedire al Fornitore di Attestati Elettronici di tracciare l'uso dell'Attestato Elettronico quando lo stato viene controllato. Se un Fornitore di Attestati Elettronici offre informazioni sullo stato facendo riferimento a un token specifico, ciò consentirebbe al Fornitore di Attestati Elettronici di creare un profilo per il token emesso correlando la data e l'identità delle Relying Party che richiedono lo stato. Le implementazioni DEVONO quindi integrare le informazioni sullo stato di molti Attestati Elettronici nella stessa lista. Di conseguenza, il Fornitore di Attestati Elettronici non apprende per quale Attestato Elettronico la Relying Party sta richiedendo la Status List. La privacy dell'Utente è protetta dall'anonimato all'interno dell'insieme degli Attestati Elettronici nella Status List, questo limita le possibilità di tracciamento da parte del Fornitore di Attestati Elettronici.
  Questo effetto di privacy di gruppo dipende dal numero di entità all'interno della Status List. Una maggiore quantità di Attestati Elettronici referenziati in essa risulta in una migliore privacy ma influisce anche sulle prestazioni poiché più dati devono essere trasferiti per leggere la Status List. A seconda dei parametri della Status List (ad esempio la quantità di bit che designano i valori dell'Attestato Elettronico), i Fornitori di Attestati Elettronici devono trovare un equilibrio appropriato tra privacy e prestazioni.

Una volta che la Relying Party riceve un Attestato Elettronico, questo le consente di richiedere la Status List per validare il suo stato attraverso il parametro URI fornito e cercare l'indice corrispondente. Tuttavia, la Relying Party è in grado di memorizzare l'URI e l'indice dell'Attestato Elettronico per richiedere nuovamente la Status List in un momento successivo. Facendolo regolarmente, la Relying Party può creare un profilo dello stato di validità dell'Attestato Elettronico. Questo comportamento potrebbe anche essere abusato in casi in cui non è intenzionale e sconosciuto all'Utente, ad esempio profilando la sospensione di una patente di guida. Questo comportamento potrebbe essere mitigato, ad esempio, con la regolare riemissione dell'Attestato Elettronico.

Token di Status List
""""""""""""""""""""

Il Token di Status List è disponibile all'Endpoint di Status List e contiene i seguenti parametri.


.. _table_status_list_endpoint_parameters:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Header**
    - **Descrizione**
    - **Riferimento**
  * - **alg**
    - OBBLIGATORIO. Un identificatore di algoritmo di firma digitale come per il registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` o su un identificatore di algoritmo simmetrico (MAC).
    - [:rfc:`7515`], [:rfc:`7517`].
  * - **typ**
    - OBBLIGATORIO. DEVE corrispondere al valore ``statuslist+jwt``.
    - `TOKEN-STATUS-LIST`_
  * - **kid**
    - OBBLIGATORIO. Identificatore univoco della chiave pubblica del Fornitore di Attestati Elettronici che firma il Token di Status.
    - :rfc:`7638#section_3`.
  * - **x5c**
    - OBBLIGATORIO. Certificato di chiave pubblica X.509 o catena di certificati corrispondente alla chiave utilizzata per firmare il Token di Status List.
    - :rfc:`5280`

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Payload**
    - **Descrizione**
    - **Riferimento**
  * - **sub**
    - OBBLIGATORIO. Il claim del soggetto DEVE specificare l'URI del Token di Status List. Il valore DEVE essere uguale a quello del claim ``uri`` contenuto nel claim ``status_list`` dell'Attestato Elettronico.
    - [:rfc:`7519`]
  * - **iat**
    - OBBLIGATORIO. Il claim issued at DEVE specificare l'ora in cui è stato emesso il Token di Status List.
    - [:rfc:`7519`]
  * - **exp**
    - RACCOMANDATO. Il claim expiration time, se presente, DEVE specificare l'ora in cui il Token di Status List è considerato scaduto dal Fornitore di Attestati Elettronici.
    - [:rfc:`7519`]
  * - **ttl**
    - RACCOMANDATO. Il claim time to live, se presente, DEVE specificare la quantità massima di tempo, in secondi, che il Token di Status List può essere memorizzato nella cache da un consumatore prima che una copia aggiornata DOVREBBE essere recuperata. Il valore del claim DEVE essere un numero positivo codificato in JSON come un numero. Questa quantità di tempo NON DOVREBBE superare il tempo di scadenza definito nel claim **exp**.
    - `TOKEN-STATUS-LIST`_
  * - **status_list**
    - OBBLIGATORIO. Oggetto JSON che contiene una Status List.
    - `TOKEN-STATUS-LIST`_

.. note::
  Si RACCOMANDA che il Fornitore di Attestati Elettronici imposti il claim ``exp`` in modo che il Token di Status List abbia una breve durata. In genere, questo comporta che il claim ``exp`` non superi il claim ``iat`` di più di 24 ore.

Una Status List codificata in JSON ha la seguente struttura:

.. _table_status_list_structure:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
    - **Riferimento**
  * - **bits**
    - OBBLIGATORIO. Intero JSON che specifica il numero di bit per Attestato Elettronico nell'array di byte compresso (`lst`). I valori consentiti per bits sono 1,2,4 e 8.
    - `TOKEN-STATUS-LIST`_
  * - **lst**
    - OBBLIGATORIO. Stringa JSON che contiene i valori di stato per tutti gli Attestato Elettronici di cui trasmette gli stati. Il valore DEVE essere l'array di byte compresso codificato in base64url.
    - `TOKEN-STATUS-LIST`_
  * - **aggregation_uri**
    - OPZIONALE. Stringa JSON che contiene un URI per recuperare l'Aggregazione di Status List per questo tipo di Attestato Elettronico o Fornitore di Attestati Elettronici.
    - `TOKEN-STATUS-LIST`_

Di seguito è riportato un esempio di Token di Status List prima di applicare la firma e la codifica:

.. code-block:: json

  {
    "alg": "ES256",
    "kid": "$KID",
    "typ": "statuslist+jwt",
    "x5c": [
      "MIIDqjCCApKgAwIBAgIESLNEvDA ...",
      "MIICwzCCAasCCQCKVy9eKjvi+jA ...",
      "MIIDTDCCAjSgAwIBAgIJAPlnQYH..."
    ]
  }

.. code-block:: json

  {
    "exp": 2291720170,
    "iat": 1686920170,
    "status_list": {
      "bits": 1,
      "lst": "eNrbuRgAAhcBXQ"
    },
    "sub": "https://example-issuer.com/statuslists/",
    "ttl": 43200
  }


Gestione dello Stato degli Attestati Elettronici con Token di Status List
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

I Fornitori di Attestati Elettronici, una volta che un Attestato Elettronico è stato generato, DEVONO:

  - Memorizzarlo localmente con il set minimo di dati necessari per gestire il suo ciclo di vita, incluso lo stato di validità di quell'Attestato Elettronico;
  - Includere un claim ``status_list`` all'interno dell'Oggetto JSON ``status`` claim dell'Attestato Elettronico.

Il valore del claim ``status_list`` DEVE essere a sua volta un Oggetto JSON con i seguenti parametri

.. _table_status_list_parameters:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
    - **Riferimento**
  * - **idx**
    - OBBLIGATORIO. Il claim idx (indice) DEVE specificare un Intero che rappresenta l'indice da controllare per le informazioni sullo stato nella Status List per l'Attestato Elettronico corrente. Il valore di idx DEVE essere un numero non negativo, contenente il valore zero o maggiore.
    - `TOKEN-STATUS-LIST`_
  * - **uri**
    - OBBLIGATORIO. Il claim uri (URI) DEVE specificare un valore String che identifica il Token di Status List contenente le informazioni sullo stato per l'Attestato Elettronico. Il valore di uri DEVE essere un URI conforme a [:rfc:`3986`].
    - `TOKEN-STATUS-LIST`_


Verifica degli Stati degli Attestati Elettronici
""""""""""""""""""""""""""""""""""""""""""""""""

Il recupero, l'elaborazione e la verifica di un Token di Status List possono essere effettuati sia dall'Istanza del Wallet che da una Relying Party. Di seguito viene descritto per la Wallet Instance, tuttavia, le stesse regole si applicherebbero anche al Relying Party.

.. _fig_entity-relation-credential-revocation-SL:
.. plantuml:: plantuml/status-list-flow.puml
    :width: 80%
    :alt: La figura illustra il Flusso di Status List.
    :caption: `Flusso di Status List. <https://www.plantuml.com/plantuml/svg/RS-n2i8m4CRnFKzn15TVm44AWbfm42suk9pj3OVf9UOkvFMDEXMS_p_u-3erp5Rc05T3AmedLeDzYDLXiIXbVb1sgHaUEQ4O-1k6G0QzgA6Cv04LAY_DBjD4Oem1UjL2-QlOkSgmtW9lu42sc3mEmnakz2gavXfggZRsXsYAeWHt0R_wvKyTufF4kuvaQc_U>`_


.. .. figure:: ../../images/High-Level-Flow-Status-List.svg
..   :figwidth: 100%
..   :align: center
..   :target: https:https://www.plantuml.com/plantuml/svg/TOv1IyD048Nl-oiUYyUQ7z23L4Im9uiDU50fOpk7XSqapioIl--IQ27GdERmllU-sPcJUkboeEAzbEwRDGoadivf8774TygP7Nkff9mvWWnZMZ9FoXSMJvInDoki4vL261Fk7v2sEBmUMnoTl1WUpRYMUy5BsnxmnZ-5pV4fY3OH9_edJZg75h75HoM0ktdbEl9NtqnXqpJrVeKGghYQnwfUizhGY_6QTaujhcjdukhTtCIULNjT_hPZkPGk_m80

..   Status List Flow

Richiesta HTTP di Status List
.............................

Per ottenere il Token di Status List, la Relying Party DEVE inviare una richiesta HTTP GET al valore ``status.status_list.uri`` fornito all'interno dell'Attestato Elettronico.

La Relying Party DOVREBBE inviare l'Accept-Header ``application/statuslist+jwt`` per indicare che il tipo di risposta richiesto per il Token di Status List è il formato JWT.

Di seguito è riportato un esempio non normativo di una richiesta per un Token di Status List:

.. code-block:: http

  GET /statuslists HTTP/1.1
  Host: example-issuer.com
  Accept: application/statuslist+jwt


Risposta HTTP di Status List
............................

L'Endpoint di Status List risponde con un Token di Status List e DEVE utilizzare un codice di stato HTTP nell'intervallo 2xx. In caso di risposta andata a buon fine, lo Status Provider DEVE utilizzare il content-type ``application/statuslist+jwt`` per il Token di Status List in formato JWT.

La risposta HTTP DOVREBBE utilizzare la Content-Encoding gzip come definito in [:rfc:`9110`].

Se gli header HTTP relativi alla cache sono presenti nella risposta HTTP, le Relying Party DOVREBBERO dare priorità ai claim ``exp`` e ``ttl`` all'interno del Token di Status List rispetto agli header HTTP per determinare il comportamento della cache.

Di seguito è riportato un esempio non normativo di una risposta per un Token di Status List con tipo ``application/statuslist+jwt``:

.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/statuslist+jwt

  eyJhbGciOiJFUzI1NiIsImtpZCI6IjEyIiwidHlwIjoic3RhdHVzbGlzdCtqd3QifQ.eyJleHAiOjIyOTE3MjAxNzAsImlhdCI6MTY4NjkyMDE3MCwiaXNzIjoiaHR0cHM6Ly9leGFtcGxlLmNvbSIsInN0YXR1c19saXN0Ijp7ImJpdHMiOjEsImxzdCI6ImVOcmJ1UmdBQWhjQlhRIn0sInN1YiI6Imh0dHBzOi8vZXhhbXBsZS5jb20vc3RhdHVzbGlzdHMvMSIsInR0bCI6NDMyMDB9.SSdg3AnTHsyRtCHziLy-QnXg-YRldMEXkdEgDXgE_ZvIvjM0eULQlzEbLBLfCeGhlqKJSReC-m85K79CTjJDzg

Al ricevimento di un Attestato Elettronico, una Relying Party DEVE prima eseguire la validazione dell'Attestato Elettronico stesso (ad esempio, controllando gli attributi previsti, la firma valida e il tempo di scadenza). Se questa validazione non ha successo, l'Attestato Elettronico DEVE essere rifiutata. Se la validazione ha avuto successo, la Relying Party DEVE eseguire i seguenti passaggi di validazione per valutare lo stato dell'Attestato Elettronico:

- Controllare l'esistenza di un claim ``status``, controllare l'esistenza di un claim ``status_list`` all'interno del claim ``status`` e validare che il contenuto di ``status_list`` aderisca alle regole definite nella Sezione :ref:`credential-revocation:Gestione dello Stato degli Attestati Elettronici con Token di Status List`.
- Risolvere il Token di Status List dall'URI fornito.
- Validare il Token di Status List:

  - Validare la firma del Token di Status List seguendo le regole definite nella sezione 7.2 di [:rfc:`7519`]. Questo passaggio richiede la risoluzione di una chiave pubblica come descritto in :ref:`trust-infrastructure:L'Infrastruttura di Trust`.

  - Controllare l'esistenza dei claim richiesti come definito nella Sezione :ref:`credential-revocation:Token di Status List`.

- Tutti i claim esistenti nel Token di Status List DEVONO essere controllati secondo :ref:`credential-revocation:Token di Status List`.

  - Il claim subject del Token di Status List DEVE essere uguale al claim ```uri``` nell'oggetto ``status_list`` dell'Attestato Elettronico.
  - Se la Relying Party ha politiche personalizzate riguardanti la freschezza del Token di Status List, DOVREBBE controllare il claim ``iat``.
  - Se il tempo di scadenza è definito, DEVE essere controllato se il Token di Status List è scaduto.
  - Se la Relying Party sta utilizzando un sistema per memorizzare nella cache il Token di Status List, DOVREBBE controllare il claim ``ttl`` del Token di Status List e recuperare una copia aggiornata se (tempo in cui lo stato è stato risolto + `ttl` < tempo corrente).

- Decomprimere la Status List con un decompressore compatibile con DEFLATE [:rfc:`1951`] e ZLIB [:rfc:`1950`].
- Recuperare il valore di stato dell'indice specificato nell'Attestato Elettronico come descritto in :ref:`credential-revocation:Verifica degli Stati degli Attestati Elettronici`. Fallire se l'indice fornito è fuori dai limiti della Status List.
- Controllare il valore di stato come descritto in :ref:`credential-revocation:Verifica degli Stati degli Attestati Elettronici`.

Se uno di questi controlli fallisce, non è possibile fare alcuna dichiarazione sullo stato dell'Attestato Elettronico e l'Attestato Elettronico DOVREBBE essere rifiutato.

Se, ad esempio, l'array di byte decompresso è ``[0x00, 0x40, 0x21]``, corrisponde all'array di bit ``[0, 0, 0, 0, 0, 0, 0, 0; 0, 1, 0, 0, 0, 0, 0, 0; 0, 0, 1, 0, 0, 0, 0, 1]``. Lo Stato dell'Attestato Elettronico il cui valore del claim ``idx`` è ``5`` in questo array si riferisce all'ultima coppia di 4 bit (cioè, ``[0, 0, 1, 0] = 0x02``) il cui valore di stato è ``SUSPENDED``.

In caso di errore durante la generazione della risposta da parte dell'Endpoint del Token di Status, DEVONO essere supportati i seguenti Codici di Stato HTTP:

.. list-table::
  :class: longtable
  :widths: 20 80
  :header-rows: 1

  * - **Codice di Stato**
    - **Descrizione**
  * - *500 Internal Server Error* [OBBLIGATORIO]
    - Il Provider di Status List ha riscontrato un problema interno.
  * - *503 Service Unavailable* [OBBLIGATORIO]
    - Il Provider di Status List è temporaneamente non disponibile.
  * - *504 Gateway Timeout* [OPZIONALE]
    - Il Provider di Status List non può soddisfare la richiesta entro l'intervallo di tempo definito.


