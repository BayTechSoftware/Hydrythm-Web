---
title: Risoluzione dei problemi
description: Le letture si sono fermate, un dispositivo è offline, un avviso non si chiude o qualcosa non ti torna. Parti da qui.
section: Help
reviewed: 2026-09-30
order: 1
---

Parti da quello che vedi.

## Un widget non mostra nessun valore

Controlla in quest'ordine:

1. **Guarda l'età dei widget vicini.** Se sono tutti vecchi, il problema è la connessione, non il parametro.
2. **Apri la scheda Dispositivi.** Se un dispositivo non si raggiunge, lo dice nella sua riga.
3. **Controlla a quale vasca è assegnato.** Un dispositivo che manda i dati alla vasca sbagliata sembra proprio un dispositivo che non manda niente. Apri il dispositivo e controlla la vasca.
4. **Controlla che la fonte esista.** Nessuno manda i fosfati se non hai un'attrezzatura che li misura o se non li registri a mano.

## Una lettura è vecchia

L'età indicata è giusta: non è arrivato niente di nuovo.

- **I parametri registrati a mano** invecchiano quando non inserisci letture nuove. Registrane una.
- **Se invecchiano le letture dell'attrezzatura**, il dispositivo ha smesso di mandare dati. Controlla la sua riga in **Dispositivi**.
- **Alcuni dispositivi sono lenti di natura.** Un titolatore che misura ogni ora di solito mostra `1h`. Non è un guasto.

## Un dispositivo non si raggiunge

Di solito è colpa della rete.

1. L'attrezzatura è accesa e funziona nella sua app?
2. È sulla stessa rete su cui l'hai aggiunta?
3. Hai cambiato qualcosa nel router (router nuovo, nuovo nome della rete, isolamento della rete ospiti)?

L'attrezzatura che si collega dalla rete di casa deve essere raggiungibile su quella rete. Quella che si collega con l'account del produttore non ne ha bisogno, ma l'account deve essere ancora valido.

## Un dispositivo dice che l'accesso è stato rifiutato

Il produttore ha rifiutato l'accesso salvato. Quasi sempre succede perché hai cambiato la password del tuo account da loro.

Apri la riga del dispositivo e accedi di nuovo.

## L'associazione di un Cora Max non riesce

Se l'aggiunta di un Cora Max si blocca a metà, Cora Mobile ti dice quale passo non è riuscito e perché. Sotto trovi **Annulla** e **Riprova**.

- *"Il telefono non è riuscito a raggiungere il Cora Max sulla rete Wi-Fi."* Collega il telefono e Cora Max alla stessa rete Wi-Fi. Su iPhone controlla anche che Cora abbia l'accesso a Rete locale. Ci arrivi da **Impostazioni → Accesso dispositivi** (trovi di più in [Impostazioni](/help/mobile-settings)). Poi tocca **Riprova**.
- *"Il Cora Max non ha accettato questa sessione di associazione."* Riprovare non serve. Chiudi la schermata e ricomincia da **Dispositivi → Aggiungi dispositivo**.

Con qualsiasi altro messaggio, tocca **Riprova**.

## Cora Max mostra dati vecchi

Guarda l'indicatore di stato nella barra in alto. **Online** e **Cloud** vogliono dire tutti e due che va bene. Se hai più di un Cora, lo schermo che non raccoglie i dati mostra **Cloud**, e le sue letture sono aggiornate lo stesso. **Non aggiornato** o **Offline** vuol dire che lo schermo ha perso la sua fonte e mostra gli ultimi dati ricevuti. È il comportamento giusto, ma i dati non sono attuali.

- Controlla il Wi-Fi in **Impostazioni → Impostazioni Cora Max → Wi-Fi**
- Controlla che la rete funzioni
- Se l'indicatore dice **Online** o **Cloud** e i dati sono comunque vecchi, il problema è a monte. Controlla la stessa vasca sul telefono

## Un avviso non si chiude

Un avviso si chiude quando la lettura torna nell'intervallo. Se non si chiude:

- **La lettura è davvero fuori intervallo.** Guarda lo storico del widget.
- **La soglia non è adatta alla tua vasca.** Trovi come cambiarla in [Avvisi e soglie](/help/mobile-alerts).
- **La fonte sbaglia.** Una sonda da calibrare manda un numero che è davvero fuori intervallo. Sistema la sonda, non la soglia.

## Due fonti non sono d'accordo

Qui Cora sta facendo il suo lavoro. Se la sonda e il kit di test non sono d'accordo, nel tuo sistema c'è davvero una differenza.

Un risultato ICP è un terzo parere utile, ma non chiude la questione. I laboratori danno risultati diversi tra loro, e il modo in cui il campione viene trattato e spedito cambia il risultato. Due test che concordano valgono molto più di uno solo.

Di solito la sonda va calibrata. A volte il kit di test è vecchio. Calibra la sonda, rifai il test con reagente fresco e confronta i due valori nelle stesse condizioni. Un [risultato ICP](/help/mobile-icp-health) aggiunge un terzo dato al confronto.

## Non mi arrivano le notifiche

1. In **Impostazioni → Notifiche** controlla che quella categoria possa inviare notifiche push
2. Controlla nelle impostazioni del telefono che Cora abbia il permesso per le notifiche
3. Ricorda che il briefing del giorno non manda notifiche nei giorni in cui non è cambiato niente

## Capire perché qualcosa è cambiato

**Impostazioni → Attività** elenca ogni cambio di presa, alimentazione, dose e presa smart, con chi l'ha chiesto: Cora Mobile, uno schermo Cora, la voce, l'Assistant, una regola di automazione, un pulsante smart o il tuo account.

## Dopo le modifiche la dashboard non va bene

Carica un design salvato: apri **Le mie dashboard** e scegline uno.

Se non ne hai salvato nessuno, rifai il layout e salvalo come design. Da lì in poi, per tornarci basta un tocco.

In ogni caso letture, storico e voci del diario sono salvati a parte rispetto al layout, quindi non perdi niente di quello che c'è dietro la dashboard.

## "I valori Red Sea non si aggiornano più"

Nessun dispositivo sulla rete di questa vasca sta leggendo la tua attrezzatura Red Sea, quindi le letture sullo schermo non si sono aggiornate.

Prova così:
1. Apri **Impostazioni → Cora Max principale** e controlla che ci sia un Cora Max impostato (oppure che sia scelto **Qualsiasi attivo (automatico)**).
2. Apri la vasca da un dispositivo collegato allo stesso Wi-Fi dell'attrezzatura Red Sea.
3. Controlla nella sua app che l'attrezzatura Red Sea sia accesa e online.

Se ancora non va, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** indicando il nome della vasca e del dispositivo.

## "API GHL disattivata"

GHL disattiva la sua API ufficiale dopo ogni aggiornamento firmware, quindi è normale dopo un aggiornamento, non un guasto. Riattivala da **System → GHL API** in GHL Control Center o GHL Connect, direttamente sul controller. Cora continua a controllare e si ricollega da sola appena torna attiva.

## "Controller GHL non raggiungibile"

Cora Max non riesce a raggiungere l'indirizzo IP del controller sulla tua rete.

1. Controlla che il controller sia acceso e collegato alla rete.
2. Controlla che il suo indirizzo IP non sia cambiato. Se è cambiato, aggiornalo da **Impostazioni → [la tua vasca] → Controller GHL (Beta)**.
3. Controlla che il Cora Max che legge questa vasca sia sulla stessa rete del controller.

Se ancora non va, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** indicando il nome della vasca e del dispositivo.

## Un controller HYDROS risulta offline o non riporta

HYDROS passa dal suo stesso cloud, quindi di solito vuol dire che il controller ha perso l'alimentazione o la sua connessione di rete, non un problema di Cora. Controllalo nell'app HYDROS. Le letture su Cora si aggiornano appena torna online, e un comando inviato mentre risulta offline non parte affatto.

Se un dispositivo HYDROS mostra **Chiave revocata**, la sua chiave dispositivo è stata rimossa o sostituita nell'app HYDROS. Crea una nuova chiave e collegala di nuovo da **Dispositivi → Aggiungi HYDROS (Beta)**, oppure dalle impostazioni della vasca su Cora Max.

## "Impossibile raggiungere questa pompa: nulla è stato inviato."

Il comando a una pompa Jecod o Jebao non è mai partito. Di solito la pompa è spenta o non è sulla sua rete.

Prova così:
1. Controlla che la pompa sia accesa.
2. Controlla che sia sulla stessa rete su cui l'hai aggiunta.
3. Tocca **Riprova**.

Se ancora non va, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** indicando il nome della vasca e del dispositivo.

## "Impossibile raggiungere questa pompa via Bluetooth. Avvicinati e riprova."

Un dispositivo Jecod solo Bluetooth è troppo lontano dal telefono.

Prova così:
1. Avvicinati alla pompa.
2. Tocca **Riprova**.

Se ancora non va, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** indicando il nome della vasca e del dispositivo.

## "Impossibile raggiungere quel Gyre. Nessuna alimentazione è stata avviata."

Una gyre Maxspect (integrazione in beta) non ha risposto quando Cora ha provato ad avviare la modalità alimentazione.

Prova così:
1. Controlla che la gyre sia accesa e sulla sua rete.
2. Tocca **Riprova**.

Se ancora non va, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** indicando il nome della vasca e del dispositivo.

## "Impossibile raggiungere quel Gyre. Il suo programma non è stato cambiato."

Il programma inviato a una gyre Maxspect (integrazione in beta) non l'ha raggiunta.

Prova così:
1. Controlla che il telefono o Cora Max siano sulla rete della gyre.
2. Tocca **Riprova** dalla schermata del programma.

Se ancora non va, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** indicando il nome della vasca e del dispositivo.

## "Impossibile raggiungere l'Apex: nulla è cambiato" / "nulla è stato dosato"

Un Neptune Apex, un Trident o una testa DŌS non ha risposto a un comando o a una richiesta di dose.

Prova così:
1. Apri l'app dell'Apex e controlla che sia online.
2. Controlla la connessione di rete del dispositivo che stai usando.
3. Tocca **Riprova**.

Se ancora non va, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** indicando il nome della vasca e del dispositivo.

## "Non è stato inviato: nessun altro dispositivo di questa vasca può inviarlo"

Nessun dispositivo Cora di questa vasca ha i dati di collegamento dell'Apex che servono per il comando, oppure quello che li ha è offline.

Prova così:
1. Aggiungi i dati dell'Apex in **Impostazioni** su un dispositivo che è online adesso, oppure
2. Imposta come **Cora Max principale** di questa vasca un altro Cora Max che funziona.

Se ancora non va, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** indicando il nome della vasca e del dispositivo.

## Un Cora Max secondario mostra "Cora principale offline"

Il Cora Max principale di questa vasca è andato offline. Questo schermo secondario mostra quindi gli ultimi dati ricevuti, non quelli in tempo reale.

Prova così:
1. Controlla alimentazione e Wi-Fi del Cora Max principale.
2. Aspetta che si ricolleghi, oppure scegli come **Cora Max principale** un dispositivo che è online adesso.

Se ancora non va, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** indicando il nome della vasca e del dispositivo.

## "Il dispositivo è offline. Mostra l'ultimo stato conosciuto."

È il normale comportamento quando un dispositivo si scollega. Il dispositivo ha smesso di mandare dati, e Cora mostra gli ultimi valori che aveva senza farli passare per attuali.

Prova così:
1. Controlla la connessione di rete del dispositivo.
2. Considera i valori mostrati come non aggiornati finché la riga dice offline.

Se ancora non va, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** indicando il nome della vasca e del dispositivo.

## Alcune impostazioni ReefBeat sono grigie o mancano

Non è un guasto. Le impostazioni proprie del dispositivo (non le letture) si aprono solo quando il telefono è sulla stessa rete del dispositivo. Lontano da quella rete vedi solo le letture.

Prova così:
1. Collegati al Wi-Fi della vasca per cambiare quelle impostazioni.
2. Lontano dalla vasca, letture e storico funzionano normalmente.

Se ancora non va, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## "Impossibile raggiungere Cora. Controlla il Wi-Fi o i dati mobili, poi riprova."

Al momento dell'accesso il telefono non riesce a collegarsi a Cora Cloud. Il problema è la connessione del telefono, non l'attrezzatura della vasca.

Prova così:
1. Controlla che il telefono abbia una connessione Wi-Fi o dati mobili funzionante.
2. Se puoi, prova un'altra rete.
3. Tocca **Riprova**.

Se ancora non va, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## All'improvviso è tutto nella lingua sbagliata

Qualcuno ha cambiato la lingua dell'account da un dispositivo. La lingua è una sola per tutto l'account, non si imposta per dispositivo.

Prova così:
1. Apri **Impostazioni → Lingua** su Cora Mobile o su Cora Max.
2. Se è stata cambiata per sbaglio, rimetti quella giusta. Il cambio vale subito ovunque.

Se ancora non va, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Dopo il cambio di lingua, un vecchio avviso o rapporto è ancora nella lingua di prima

È normale, non è un errore. Cora non traduce di nuovo quello che esiste già. Solo i nuovi avvisi, rapporti e briefing seguono la nuova lingua.

Non c'è niente da sistemare. I contenuti nuovi arriveranno nella lingua attuale.

Se hai altri dubbi, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un avviso continua a mandare notifiche anche dopo che l'ho visto

**Rinvia** e **Ignora** su Cora Max zittiscono solo quel Cora Max. Il telefono continua a ricevere notifiche finché la lettura resta fuori intervallo.

Prova così:
1. Per ricevere notifiche meno spesso sul telefono, apri la regola di avviso in Cora Mobile e imposta un'**Attesa tra gli avvisi** più lunga (fino a 1 settimana).
2. Se la soglia non va bene per la tua vasca, cambia la soglia stessa.

Se ancora non va, guarda [Avvisi e soglie](/help/mobile-alerts) oppure scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Una dose si è fermata a metà ed è comparso un avviso di "ripristino"

La testa DŌS ha perso il contatto durante la dose. Cora te lo segnala apposta, senza dare per scontato che la dose sia stata erogata tutta.

Prova così:
1. Apri l'avviso e guarda quanto è stato dosato davvero prima dell'interruzione.
2. Riprendi o correggi la dose in base a quella quantità, non a quella programmata all'inizio.

Se ancora non va, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** indicando il nome della vasca e del dispositivo.

## Una scena creata sul telefono non si può modificare su Cora Max

Modificare le scene direttamente sullo schermo a parete è una novità di Cora Max. Le versioni più vecchie avviano le scene create sul telefono, ma non le modificano.

Prova così:
1. Aggiorna Cora Max, oppure
2. Continua a modificare quella scena dal telefono. Su Cora Max si avvia comunque.

Se ancora non va, guarda [Aggiornamenti e ripristino](/help/max-updates) oppure scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant risponde sulla vasca sbagliata

Prima della domanda non è stata scelta nessuna vasca, oppure è attiva la vasca sbagliata.

Prova così:
1. Scegli prima la vasca giusta.
2. Fai di nuovo la domanda.

Se ancora non va, guarda [L'Assistant](/help/mobile-assistant) oppure scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant non risponde, o mostra di nuovo la schermata del consenso

L'opzione **Consenti al Cora Assistant di usare i dati salvati della vasca** è stata spenta, quindi l'Assistant non ha dati da cui rispondere.

Per riattivarla, tocca **Accetta e continua** nella schermata del consenso.

Se ancora non va, guarda [L'Assistant](/help/mobile-assistant) oppure scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un risultato ICP dal laboratorio o per email non è mai arrivato

Perché un risultato entri in Cora bisogna scegliere la vasca a cui collegarlo, e a volte serve anche un mittente riconosciuto.

Prova così:
1. Rileggi le istruzioni che compaiono la prima volta che invii un risultato a Cora.
2. Quando te lo chiede, conferma a quale vasca collegare il risultato.
3. Se hai già mandato un risultato in passato, invia l'email dallo stesso indirizzo di quella volta.

Se ancora non va, guarda [ICP e rapporti di salute](/help/mobile-icp-health) oppure scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Una notifica di ICP via email non dice il nome del laboratorio

È un problema noto: nella notifica push "scegli vasca" mancava il nome del laboratorio. Nelle versioni attuali è stato risolto.

Prova così:
1. Aggiorna Cora Mobile all'ultima versione.
2. Il risultato non ha nessun problema. Mancava solo il nome nel testo della notifica.

Se ancora non va, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un widget mostra le unità sbagliate

Dipende dalle unità di visualizzazione impostate per la vasca, non dai dati. I valori vengono salvati sempre allo stesso modo, comunque tu li veda.

Prova così:
1. Apri le **Impostazioni** di quella vasca e controlla le unità di visualizzazione.
2. Cambiale lì. Tutti i telefoni e i Cora Max che mostrano quella vasca si aggiornano.

Se ancora non va, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Dopo il cambio di unità un indicatore o una soglia sembrano diversi

È normale. Indicatori, riquadri e storico vengono ridisegnati nell'unità che hai scelto. I valori veri non sono cambiati.

Non c'è niente da sistemare: cambia solo l'aspetto.

Se hai altri dubbi, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Dopo un'interruzione del Wi-Fi Cora Max non si ricollega subito

Quando perde la connessione, Cora Max aspetta un po' di più prima di ogni nuovo tentativo, così non sovraccarica la rete. Arriva ad aspettare circa un minuto tra un tentativo e l'altro.

Prova così:
1. Quando la rete torna, aspetta circa un minuto.
2. Se dopo non si è ancora ricollegato, controlla il Wi-Fi in **Impostazioni → Impostazioni Cora Max → Wi-Fi**.

Se ancora non va, guarda [La schermata Home di Cora Max](/help/max-tour) oppure scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Ho rinominato un Cora Max dal telefono, ma sullo schermo non cambia

Il nome che imposti dal telefono è un'etichetta dell'account per quel dispositivo. Il nome che Cora Max mostra durante l'associazione può essere un'altra cosa.

Prova così:
1. Controlla quale "nome" stai guardando: quello nell'elenco dei dispositivi sul telefono, o quello nella schermata di associazione di Cora Max.
2. Se vuoi cambiare l'etichetta dell'account, rinominalo dall'elenco dei dispositivi sul telefono.

Se ancora non va, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** indicando il nome del dispositivo.

## Non trovo dove spegnere la parola di attivazione su Cora Max

L'interruttore della parola di attivazione è nella sezione **Audio e voce**. Non si trova nelle impostazioni di Cora Assistant.

Prova così:
1. Vai in **Impostazioni → Impostazioni Cora Max → Audio e voce → Ascolto parola di attivazione**.
2. Spegnilo. Puoi comunque toccare l'icona di Cora per avviare una conversazione a voce.

Se ancora non va, guarda [Impostazioni su Cora Max](/help/max-settings) oppure scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Con il blocco bambini nessuno riesce a entrare in Impostazioni

Funziona così. Dopo un certo tempo senza tocchi, il blocco bambini impedisce a chiunque di accendere o spegnere l'attrezzatura da questo schermo, sia al tocco sia a voce. Le letture continuano ad aggiornarsi, e puoi comunque fare domande a Cora.

Per sbloccare:
1. Premi **Volume Su** o **Volume Giù** tre volte entro due secondi, oppure
2. Tieni cinque dita nell'angolo in alto a destra dello schermo per dieci secondi.

Se ancora non va, guarda [La voce su Cora Max](/help/max-voice) oppure scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Ancora bloccato?

Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**. Dicci quale vasca, quale schermata e cosa ti aspettavi di vedere. Così ti rispondiamo prima e meglio.
