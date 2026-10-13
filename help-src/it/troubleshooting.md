---
title: Risoluzione dei problemi
description: Sistema una lettura vecchia, un dispositivo andato offline, un comando che non è arrivato, un Cora Max che non si associa o un avviso che non si chiude.
section: Help
reviewed: 2026-10-13
order: 1
---

Trova la famiglia a cui appartiene il tuo problema, poi il messaggio o il sintomo che vedi. I titoli tra virgolette sono le parole esatte che Cora ti mostra.

- [Letture e widget](#readings-and-widgets)
- [Un dispositivo ha smesso di inviare dati o non si raggiunge](#device-not-reporting)
- [Un comando non è arrivato](#command-did-not-go-through)
- [Cora Max](#cora-max)
- [Avvisi, notifiche e briefing giornaliero](#alerts-and-notifications)
- [Telecamere e Controllo schiumatoio](#cameras-and-skimmer-watch)
- [Cora Assistant e voce](#cora-assistant-and-voice)
- [Risultati di laboratorio e report di salute](#lab-results-and-health-reports)
- [Lingua, unità e accesso](#language-units-and-signing-in)

:::note Integrazioni Beta
Alcune voci qui sotto riguardano integrazioni Beta: Maxspect, GHL, HYDROS, Focustronic, EcoTech, Inkbird e telecamere. **Beta.** Queste integrazioni sono in Beta e sono disponibili solo per gli utenti Beta. Se non sei un utente Beta non le vedrai in **Aggiungi dispositivo**. Per chiedere l'accesso alla Beta, contatta l'assistenza. Di più in [Funzioni Beta](/help/mobile-beta).
:::

## Letture e widget {#readings-and-widgets}

### Un widget non mostra nessun valore {#a-widget-shows-no-value}

Controlla queste cose in ordine.

1. Guarda l'età sui widget vicini. Se sono tutti vecchi anche loro, è la connessione, non il parametro.
2. Apri la scheda **Dispositivi**. Se un dispositivo non si raggiunge, la sua riga ha un pallino rosso o lo dice.
3. Controlla su quale vasca è il dispositivo. Un dispositivo che invia dati alla vasca sbagliata sembra proprio uno che non ne invia. Apri il dispositivo e controlla la sua vasca.
4. Controlla che qualcosa lo misuri. Niente riporta i fosfati a meno che tu non abbia un'attrezzatura che li misura o li registri a mano.

### Un widget è grigio {#a-widget-is-grey}

Grigio vuol dire che Cora non sta valutando quella lettura. Ci sono tre motivi tipici.

1. Il suo avviso è spento. Riattivalo nella scheda **Regole** del Centro avvisi.
2. Non ha un intervallo con cui valutarla. Tieni premuto il widget e imposta un intervallo.
3. La lettura è troppo vecchia. Controlla l'età sul widget, poi registra una nuova lettura o controlla il dispositivo.

Cosa significa ogni colore è spiegato in [Leggere la dashboard](/help/mobile-dashboard#colours).

### Una lettura è vecchia {#a-reading-is-stale}

L'età sul widget è giusta. Non è arrivato niente di nuovo.

- I parametri registrati a mano invecchiano quando nessuno registra una lettura. Registrane una.
- Le letture dell'attrezzatura invecchiano quando il dispositivo smette di inviare dati. Controlla la sua riga in **Dispositivi**.
- Alcune attrezzature inviano dati solo ogni tanto. Un titolatore che misura ogni ora di solito mostra `1h`. È normale.

### Due fonti non concordano {#two-sources-disagree}

Non c'è niente di rotto. Quando la sonda e il test non concordano, ti dicono qualcosa di reale sul tuo impianto.

Di solito la sonda va calibrata. A volte il test è vecchio. Calibra la sonda, rifai il test con reagente nuovo e confronta i due nelle stesse condizioni. Se una lettura era chiaramente sbagliata, puoi escluderla. Vedi [Approfondire un parametro](/help/mobile-metric-detail).

Un [risultato ICP](/help/mobile-icp-health) ti dà un terzo numero da confrontare, ma da solo non chiude la questione. I laboratori differiscono tra loro, e il modo in cui un campione viene trattato e spedito cambia il risultato.

### Un widget mostra le unità sbagliate {#a-widget-shows-the-wrong-units}

Sono le unità di visualizzazione della vasca. I tuoi dati vanno bene, e i valori sono salvati allo stesso modo comunque vengano mostrati.

1. Apri **Impostazioni**, apri quella vasca e scegli **Unità**.
2. Cambiale lì. Ogni telefono e Cora Max che mostra quella vasca si aggiorna di conseguenza.

### Un indicatore o una soglia sembrano diversi dopo il cambio di unità {#a-gauge-or-threshold-looks-different-after-changing-display-}

È normale. Indicatori, riquadri e storico vengono ridisegnati nell'unità che hai scelto. I valori sottostanti non sono cambiati.

### La dashboard sembra sbagliata dopo una modifica {#my-dashboard-looks-wrong-after-editing}

Letture, storico e diario sono salvati separatamente dal layout, quindi non hai perso niente.

- **Sul telefono**, l'editor non ha un annulla né design salvati. Apri **Modifica dashboard** e rimetti a posto i widget. Di più in [Modificare la dashboard](/help/mobile-dashboard-editing).
- **Su Cora Max**, carica un design salvato: apri **Layout dashboard**, tocca **Le mie dashboard** e scegline uno. Se non ne hai salvato uno, ricostruisci il layout e tocca **Salva questo progetto**, così la prossima volta basta un tocco. Di più in [Modificare la dashboard di Cora Max](/help/max-dashboard-editing#saving-layouts).

### Capire perché qualcosa è cambiato {#establishing-why-something-changed}

**Impostazioni → Attività** elenca ogni accensione o spegnimento di una presa, alimentazione e dose, e cosa l'ha chiesto: Cora Mobile, un Cora Max, la voce, l'Assistente, un'automazione o il tuo account. Di più in [Attività e cronologia](/help/mobile-activity).

## Un dispositivo ha smesso di inviare dati o non si raggiunge {#device-not-reporting}

### "[Dispositivo]: ha smesso di inviare dati" {#device-stopped-reporting}

Cora invia questo messaggio quando un dispositivo tace. Non vuol dire che il dispositivo sia rotto, solo che Cora non lo sente da un po'. Quanto aspetta Cora per ogni marca è spiegato in [Avvisi e soglie](/help/mobile-alerts#stopped-reporting).

1. Controlla l'alimentazione del dispositivo, e la sua portata Wi-Fi o Bluetooth.
2. Controlla che il Cora Max che lo legge sia acceso e online. Senza un Cora Max, il telefono legge un dispositivo Neptune Apex, Red Sea o Jecod solo mentre Cora Mobile è aperta sullo stesso Wi-Fi.
3. Aspetta la lettura successiva. Ricevi una seconda notifica quando torna a inviare dati.

GHL e HYDROS hanno i loro messaggi, più avanti in questa pagina.

### "Il dispositivo è offline. Mostra l'ultimo stato conosciuto." {#device-is-offline-showing-last-known-state}

Il dispositivo ha smesso di inviare dati, e Cora mostra gli ultimi valori che aveva. Non sono attuali.

1. Controlla la connessione di rete del dispositivo stesso.
2. Non considerare i valori come attuali finché la riga non smette di dire offline.

### Un dispositivo non si raggiunge {#a-device-cannot-be-reached}

Di solito è la rete.

1. L'attrezzatura è accesa e funziona nella sua app?
2. È sulla stessa rete su cui l'hai aggiunta?
3. È cambiato qualcosa con il router (hardware nuovo, nuovo nome della rete, isolamento della rete ospiti)?

L'attrezzatura sulla rete locale deve essere raggiungibile su quella rete. L'attrezzatura che si collega tramite un account del produttore no, ma quell'account deve comunque essere valido. Se l'indirizzo del dispositivo è cambiato, aprilo nella scheda **Dispositivi** e tocca **Modifica connessione** in **Connessione**.

### Un dispositivo dice che l'accesso è stato rifiutato {#a-device-says-the-sign-in-was-refused}

Il produttore ha respinto l'accesso salvato. Quasi sempre succede perché hai cambiato la password presso di loro. Apri la riga del dispositivo e accedi di nuovo.

### "I valori Red Sea non si aggiornano più" {#red-sea-readings-have-stopped-updating}

In questo momento niente su questa vasca sta leggendo la tua attrezzatura Red Sea, quindi le letture sullo schermo non vengono aggiornate.

1. Apri **Impostazioni**, apri la vasca, poi **Cora Max principale**. Controlla che sia impostato un Cora Max, oppure che sia scelto **Qualsiasi attivo (automatico)**.
2. Se non hai un Cora Max, apri la vasca in Cora Mobile mentre il telefono è sullo stesso Wi-Fi dell'attrezzatura Red Sea.
3. Controlla che l'attrezzatura Red Sea sia accesa e online nella sua app.

### Alcune impostazioni ReefBeat sono disattivate o mancano {#some-reefbeat-settings-are-greyed-out-or-missing}

È normale. Le impostazioni proprie di un dispositivo Red Sea si aprono solo quando il telefono è sulla stessa rete del dispositivo. Lontano da quella rete vedi solo le letture.

1. Collegati al Wi-Fi della vasca per cambiare quelle impostazioni.
2. Letture e storico continuano a funzionare quando sei via.

### "API GHL disattivata" {#ghl-api-is-off}

GHL (Beta) disattiva la sua API ufficiale dopo ogni aggiornamento del firmware, quindi dopo un aggiornamento è normale. Riattivala da **System → GHL API** in GHL Control Center o GHL Connect, sul controller stesso. Cora continua a controllare e si ricollega quando è di nuovo attiva.

### "Controller GHL non raggiungibile" {#ghl-controller-unreachable}

Cora Max non riesce a raggiungere l'indirizzo del controller GHL (Beta) sulla tua rete.

1. Controlla che il controller sia acceso e collegato alla tua rete.
2. Controlla che il suo indirizzo IP non sia cambiato. Se è cambiato, aprilo sul telefono (**Dispositivi**) e aggiornalo in **Connessione**.
3. Controlla che il Cora Max che legge questa vasca sia sulla stessa rete del controller.

### Un controller HYDROS risulta offline o non invia dati {#a-hydros-controller-shows-as-offline-or-not-reporting}

HYDROS (Beta) invia i dati attraverso il suo cloud, quindi di solito vuol dire che il controller ha perso l'alimentazione o la sua connessione. Controllalo nell'app HYDROS. Le letture si rimettono in pari quando torna online. Un comando inviato mentre sembra offline non viene inviato per niente.

Se un dispositivo HYDROS mostra **Chiave revocata**, la sua chiave dispositivo è stata rimossa o sostituita nell'app HYDROS. Crea una nuova chiave e collegalo di nuovo dal telefono da **Dispositivi → Aggiungi dispositivo → HYDROS**.

## Un comando non è arrivato {#command-did-not-go-through}

Ogni comando finisce come **Confermato**, **Non confermato**, **Rifiutato** o **Nessun cambiamento**. Cosa significa ognuno è spiegato in [Controllare la tua attrezzatura](/help/mobile-device-control).

### "Impossibile raggiungere questa pompa: nulla è stato inviato." {#could-not-reach-this-pump-nothing-was-sent}

Un comando alla tua pompa Jecod o Jebao non è mai partito da Cora. Sul telefono il messaggio dice *"Impossibile raggiungere questa pompa. Deve essere sullo stesso Wi-Fi del tuo telefono."* Di solito la pompa è spenta o non è sulla sua rete.

1. Controlla che la pompa sia accesa.
2. Controlla che sia sulla stessa rete su cui l'hai aggiunta, e che anche il telefono o il Cora Max siano su quella rete.
3. Tocca **Riprova**.

### "Impossibile raggiungere questa pompa via Bluetooth. Avvicinati e riprova." {#could-not-reach-this-pump-over-bluetooth-stand-near-it-and-t}

Il telefono è fuori portata di una pompa Jecod solo Bluetooth. Avvicinati alla pompa e tocca **Riprova**.

### "Impossibile raggiungere quel Gyre. Il suo programma non è stato cambiato." {#could-not-reach-that-gyre-its-program-was-not-changed}

Cora non è riuscita a far arrivare un nuovo programma a una gyre Maxspect (Beta). Controlla che la gyre sia accesa e che il telefono o il Cora Max siano sulla sua rete, poi tocca **Riprova** nella schermata del programma.

### "Impossibile raggiungere l'Apex: nulla è cambiato" / "nulla è stato dosato" {#could-not-reach-the-apex-nothing-changed-nothing-was-dosed}

Un Neptune Apex, un Trident o una testa DŌS non ha risposto a un comando o a una richiesta di dose.

1. Apri l'app dell'Apex e controlla che sia online.
2. Controlla la connessione di rete del telefono o del Cora Max che stai usando. Per cambiare una testa DŌS dal telefono, il telefono deve essere sulla stessa rete dell'Apex.
3. Tocca **Riprova**.

### "… non è stato inviato: questo Cora Max non ha i dati Apex" {#this-could-not-be-sent-no-device-on-this-tank-can-send-it}

Cora Max mostra questo messaggio quando non ha modo di raggiungere il tuo Apex e nessun altro dispositivo della vasca può inviare il comando al posto suo. Il messaggio dice di aggiungere i dati Apex nelle Impostazioni, ma ora si impostano sul telefono.

1. Sul telefono, apri **Dispositivi**, poi il tuo Apex, e controlla indirizzo e accesso in **Connessione**. Correggili con **Modifica connessione**.
2. Oppure rendi un Cora Max funzionante il **Cora Max principale** di questa vasca: **Impostazioni**, apri la vasca, poi **Cora Max principale**.

### L'alimentazione non parte dal telefono {#feed-does-not-start}

Sul telefono, **Alimenta** compare solo su una vasca con un Neptune Apex, e avvia uno dei cicli di alimentazione programmati sull'Apex.

- *"Nessun Cora su questa vasca può raggiungere l'Apex, e non sei sulla sua rete."* Collegati al Wi-Fi dell'Apex, oppure associa un Cora Max alla vasca.
- *"L'Apex non ha risposto, ma potrebbe già essere in fase di alimentazione."* Controlla il controller prima di riprovare.

### Una dose si è fermata a metà ed è comparso un avviso di "ripristino" {#a-dose-stopped-partway-through-and-a-restore-alert-appeared}

La testa DŌS ha perso il contatto durante la dose. Cora te lo dice, così non deve dare per scontato che sia entrata tutta la dose.

1. Apri l'avviso e controlla quanto è stato dosato prima che si fermasse.
2. Usa quella quantità per decidere se riprendere o correggere la dose.

## Cora Max {#cora-max}

### Il mio Cora Max è offline {#my-cora-max-is-offline}

Sul telefono, la sua riga nella scheda **Dispositivi** ha un pallino rosso. Mentre è offline, l'attrezzatura che legge smette di aggiornarsi, potresti ricevere avvisi "ha smesso di inviare dati" per quell'attrezzatura, e i comandi inviati da lontano possono tornare come *"Nulla è stato inviato"*.

1. Controlla che Cora Max sia alimentato e che lo schermo sia acceso.
2. Su Cora Max, controlla **Impostazioni → Impostazioni Cora Max → Wi-Fi**, e che il router funzioni.
3. Se sulla vasca c'è un altro Cora Max, imposta **Cora Max principale** su **Qualsiasi attivo (automatico)** così può prendere il suo posto. Vedi [Più di un dispositivo Cora](/help/mobile-multi-device#primary-cora-max).
4. Se non si avvia correttamente, vedi [Aggiornamenti e ripristino](/help/max-updates).

:::tip Fatti avvisare la prossima volta
In Cora Mobile, apri **Impostazioni → Automazioni** e crea una regola con il trigger **Quando un dispositivo va offline**, scegli il tuo Cora Max e aggiungi l'azione **Avvisami**. Di più in [Automazioni e scene](/help/mobile-automation).
:::

### L'associazione di un Cora Max non riesce {#pairing-a-cora-max-fails}

Cora Mobile trova un Cora Max nuovo via Bluetooth, poi gli passa il tuo Wi-Fi. Prima di cominciare, abbi almeno una vasca in Cora Mobile, il Bluetooth acceso e il telefono vicino allo schermo. Se l'associazione si ferma a metà, Cora Mobile ti dice perché, con **Annulla** e **Riprova** sotto.

- *"Il Bluetooth è disattivato. Attivalo, poi tocca di nuovo Scansiona."* Attiva il Bluetooth e cerca di nuovo.
- *"L'autorizzazione Bluetooth per Cora è disattivata. Attivala nelle Impostazioni, poi tocca di nuovo Scansiona."* Consenti il Bluetooth per Cora nelle impostazioni del telefono. **Impostazioni → Accesso dispositivi** in Cora Mobile ti porta lì.
- *"Nessun dispositivo di configurazione Cora trovato nelle vicinanze via Bluetooth."* Mettiti accanto a Cora Max, controlla che mostri la sua schermata di configurazione e cerca di nuovo.
- **Nessuna vasca trovata**: crea prima una vasca in Cora Mobile, poi associa.
- *"Il telefono non è riuscito a raggiungere il Cora Max sulla rete Wi-Fi."* Metti il telefono e Cora Max sulla stessa rete Wi-Fi. Su iPhone, controlla anche che Cora abbia l'accesso alla Rete locale (**Impostazioni → Accesso dispositivi**). Poi tocca **Riprova**.
- *"Il Cora Max non ha accettato questa sessione di associazione."* Riprovare non serve. Chiudi la schermata e ricomincia da **Dispositivi → Aggiungi dispositivo → Cora**.

Per qualsiasi altro messaggio, tocca **Riprova**. Tutta la configurazione è in [Configurare Cora Max](/help/max-setup).

### Cora Max mostra dati vecchi {#cora-max-shows-old-data}

Guarda l'etichetta di stato nella barra in alto. **Online** e **Cloud** vanno entrambi bene. Se hai più di un Cora Max, quello che non sta raccogliendo i dati mostra **Cloud**, e le sue letture sono aggiornate allo stesso modo. **Non aggiornato** o **Offline** vuol dire che Cora Max ha perso la sua fonte e mostra gli ultimi dati ricevuti.

- Controlla il Wi-Fi in **Impostazioni → Impostazioni Cora Max → Wi-Fi**.
- Controlla che la rete stessa funzioni.
- Se l'etichetta dice **Online** o **Cloud** e i dati sono comunque vecchi, il problema è prima di Cora Max. Controlla la stessa vasca sul telefono.

### Cora Max mostra "Password Apex" {#cora-max-shows-apex-password}

Il tuo Apex ha rifiutato l'accesso salvato da Cora, di solito perché la password dell'Apex è stata cambiata. Sul telefono, apri **Dispositivi**, poi il tuo Apex, e tocca **Modifica connessione** in **Connessione** per inserire quella nuova.

### Cora Max mostra "Salvataggio cloud rifiutato" {#cora-max-shows-cloud-save-refused}

Cora Cloud rifiuta di salvare alcuni dati di questo schermo. Non c'è niente che non va nella tua vasca o in Cora Max, e non c'è niente da cambiare sullo schermo. La soluzione è un aggiornamento di Cora Cloud.

1. Apri **Impostazioni → Impostazioni Cora Max** e scorri fino a **STATO**. La riga **Salvataggio cloud** dice quali dati vengono rifiutati, per esempio le letture o le prese di un dispositivo.
2. [Contatta l'assistenza](/support.html) e dicci cosa dice quella riga.

Nel frattempo le tue letture continuano a comparire su Cora Max. Semplicemente non vengono salvate nel tuo account finché non arriva la correzione.

### Un secondo Cora Max mostra "Cora principale offline" {#a-secondary-cora-max-shows-main-cora-offline}

Il Cora Max principale di questa vasca è andato offline. Questo schermo mostra gli ultimi dati ricevuti, quindi non sono in tempo reale.

1. Controlla l'alimentazione e il Wi-Fi del Cora Max principale.
2. Aspetta che si ricolleghi, oppure cambia il **Cora Max principale** con un dispositivo online.

### Cora Max non si ricollega subito dopo un'interruzione del Wi-Fi {#cora-max-wont-reconnect-right-away-after-a-wi-fi-outage}

Dopo aver perso la connessione, Cora Max aspetta un po' di più prima di ogni nuovo tentativo, così non intasa la tua rete. L'attesa cresce fino a circa un minuto.

1. Dagli circa un minuto dopo che la rete è tornata.
2. Se ancora non si è ricollegato, controlla **Impostazioni → Impostazioni Cora Max → Wi-Fi**.

### Rinominare un Cora Max dal telefono non cambia quello che mostra {#renaming-a-cora-max-on-the-phone-doesnt-change-what-the-tabl}

Il nome che imposti sul telefono è l'etichetta dell'account per quel dispositivo. Il nome che Cora Max mostra sulla sua schermata di associazione può essere diverso.

1. Controlla quale nome stai guardando: quello nell'elenco dei dispositivi del telefono, o quello sulla schermata di associazione di Cora Max.
2. Per cambiare l'etichetta dell'account, rinominalo dall'elenco dei dispositivi del telefono.

### Non trovo dove spegnere la parola di attivazione {#i-cant-find-where-to-turn-off-the-wake-word-on-cora-max}

I comandi della parola di attivazione stanno con le impostazioni del suono, non con quelle di Cora Assistant.

1. Su Cora Max, vai in **Impostazioni → Impostazioni Cora Max**, e trova **Parola di attivazione** in **AUDIO E VOCE**.
2. Spegnila. Puoi comunque toccare l'icona di **Cora Assistant** per cominciare a parlare.

Di più in [Parlare con Cora](/help/max-voice).

### Il blocco bambini non lascia entrare nessuno nelle Impostazioni {#child-lock-wont-let-anyone-into-settings}

È proprio quello che fa il blocco bambini. Dopo un certo tempo senza tocchi, impedisce a chiunque di comandare l'attrezzatura da questo schermo, al tocco o a voce. Le letture continuano ad aggiornarsi, e puoi comunque fare domande a Cora. Per sbloccare:

1. Premi **Volume su** o **Volume giù** tre volte entro due secondi, oppure
2. Tieni cinque dita nell'angolo in alto a destra dello schermo per dieci secondi.

Di più in [Impostazioni di Cora Max](/help/max-settings#child-lock).

### Una scena creata sul telefono non si può modificare su Cora Max {#a-scene-made-on-the-phone-doesnt-show-up-as-editable-on-cora}

Solo le versioni più recenti di Cora Max possono modificare le scene sullo schermo. Le versioni più vecchie avviano comunque le scene che hai creato sul telefono, ma non possono modificarle.

1. Aggiorna Cora Max ([Aggiornamenti e ripristino](/help/max-updates)), oppure
2. Continua a modificare quella scena dal telefono. Su Cora Max funziona in ogni caso.

## Avvisi, notifiche e briefing giornaliero {#alerts-and-notifications}

### Un avviso non si chiude {#an-alert-is-not-clearing}

Un avviso si chiude quando la lettura torna nell'intervallo. Se non si chiude, ci sono tre motivi probabili.

- La lettura è davvero fuori intervallo. Guarda lo storico del widget.
- L'intervallo non è adatto alla tua vasca. Vedi [Avvisi e soglie](/help/mobile-alerts).
- La fonte è sballata. Una sonda che va calibrata riporta un numero che è davvero fuori intervallo. Sistema la sonda e lascia stare l'intervallo.

### Un avviso continua a notificarmi anche dopo che l'ho preso in carico {#an-alert-wont-stop-notifying-even-after-ive-acknowledged-it}

**Rinvia** e **Ignora** su Cora Max silenziano solo quel Cora Max. Il telefono continua a ricevere notifiche finché la lettura è fuori intervallo.

1. Per sentirne parlare meno spesso, apri la regola dell'avviso in Cora Mobile e imposta un'**Attesa tra gli avvisi** più lunga (fino a 1 settimana).
2. Se l'intervallo non è adatto alla tua vasca, cambia l'intervallo stesso.

### Non ricevo notifiche {#im-not-getting-notifications}

1. In **Impostazioni → Notifiche**, controlla che la categoria possa inviare notifiche.
2. Controlla il permesso delle notifiche del telefono per Cora.
3. Il briefing giornaliero resta in silenzio nei giorni in cui non è cambiato niente. Se si è fermato del tutto, vedi la voce successiva.

Di più in [Notifiche](/help/mobile-notifications).

### Il mio briefing giornaliero si è fermato {#my-daily-briefing-stopped}

- La tua prova è finita. Reef Buddy fa parte dei piani a pagamento. Dopo la prova di 30 giorni, un account gratuito smette di ricevere il briefing giornaliero. Vedi [Piani e abbonamenti](/help/mobile-plans).
- La vasca non è coperta dal tuo piano. Ogni piano copre un certo numero di vasche, contate nell'ordine di **Impostazioni → Riordina vasche**. Sposta una vasca più in alto per includerla.
- Oggi non è cambiato niente. In una giornata tranquilla il briefing resta in silenzio.

Di più in [Reef Buddy](/help/mobile-reef-buddy).

### Continuano ad arrivare avvisi da una vasca che ho rimosso {#alerts-from-a-removed-tank}

Rimuovere una vasca la nasconde soltanto. I suoi dispositivi restano collegati, e un Cora Max può ancora leggerla, quindi la sua attrezzatura può continuare a inviare dati e avvisi.

1. Ripristinala da **Impostazioni → Vasche rimosse** così puoi vederla di nuovo.
2. Rimuovi o sposta i suoi dispositivi nella scheda **Dispositivi**.
3. Toglila dal tuo Cora Max: sul telefono, apri **Dispositivi**, poi il tuo Cora Max, e in **Vasche** tocca **Rimuovi vasca** accanto a lei.

Poi rimuovi di nuovo la vasca. Di più in [Gestire le tue vasche](/help/mobile-tanks).

## Telecamere e Controllo schiumatoio {#cameras-and-skimmer-watch}

Telecamere e Controllo schiumatoio sono in Beta. La configurazione è spiegata in [Telecamere e Controllo schiumatoio](/help/mobile-cameras).

### Il Controllo schiumatoio mostra un messaggio invece del livello del bicchiere {#skimmer-watch-messages}

- **Segna prima il bicchiere**: il Controllo schiumatoio non sa ancora dov'è il bicchiere. Tocca **Segna il bicchiere** e trascina il riquadro sopra.
- **Non calibrato: svuota il bicchiere e tocca Il bicchiere è vuoto ora**: fai esattamente questo, con il bicchiere vuoto.
- **Riquadro spostato: calibra di nuovo**: hai spostato il riquadro, quindi calibra di nuovo con il bicchiere vuoto.
- **Non sicuro (bassa affidabilità)**: l'immagine non era abbastanza chiara. Leggi i **Consigli per la videocamera** nella schermata del Controllo schiumatoio, poi aspetta il controllo successivo o tocca **Controlla ora**.
- **Luce troppo forte dietro il bicchiere**: spegni la luce dietro il bicchiere, oppure imposta la visione notturna della telecamera sempre attiva.
- **Cora Max non è riuscito a ottenere un'immagine della videocamera.**: controlla che la telecamera sia alimentata e online, e che il Cora Max che la legge sia acceso.
- **L'ultimo controllo non è riuscito.**: tocca **Controlla ora**. Se continua a non riuscire, controlla la telecamera e Cora Max.
- **Nessuna lettura per ora. Cora Max controlla ogni 15 minuti.**: aspetta il primo controllo.
- **Il controllo dello schiumatoio richiede un piano a pagamento.**: il Controllo schiumatoio fa parte dei piani a pagamento.

## Cora Assistant e voce {#cora-assistant-and-voice}

### Cora Assistant risponde sulla vasca sbagliata {#cora-assistant-answers-about-the-wrong-tank}

Non hai scelto una vasca prima di chiedere, oppure è selezionata quella sbagliata. Scegli la vasca che intendi, poi chiedi di nuovo. Di più in [Fare domande a Cora](/help/mobile-assistant).

### Cora Assistant non risponde, o mostra di nuovo una schermata di consenso {#cora-assistant-refuses-to-answer-or-shows-a-consent-screen-a}

**Consenti al Cora Assistant di usare i dati salvati della vasca** è spento, quindi non ha niente da cui partire per rispondere. Tocca **Accetta e continua** nella schermata del consenso, oppure accendi l'interruttore in **Impostazioni → Cora Assistant**.

### Cora Max dice "La voce ha bisogno del tuo consenso" {#voice-needs-your-ok}

La voce su Cora Max usa la stessa scelta di condivisione dei dati di Cora Assistant sul telefono. In Cora Mobile, apri **Impostazioni → Cora Assistant** e attiva **Consenti al Cora Assistant di usare i dati salvati della vasca**, poi riprova. Di più in [Parlare con Cora](/help/max-voice).

## Risultati di laboratorio e report di salute {#lab-results-and-health-reports}

### Un risultato di laboratorio o un ICP inviato per email non è mai arrivato {#a-lab-or-emailed-icp-result-never-showed-up}

Un risultato si aggiunge solo quando ha una vasca, a volte Cora deve anche riconoscere il mittente, e Cora ha bisogno del tuo consenso per leggerlo.

1. Se vedi *"Cora Assistant ha bisogno della tua autorizzazione per leggerlo."*, apri **Impostazioni → Cora Assistant** e attiva **Consenti al Cora Assistant di usare i dati salvati della vasca**. Il risultato arriva quando dai il consenso.
2. Controlla il suggerimento che Cora mostra la prima volta che le invii un risultato.
3. Quando Cora te lo chiede, conferma a quale vasca appartiene il risultato.
4. Se hai già inviato un risultato in passato, invia questo dallo stesso indirizzo email.

Di più in [ICP e report di salute](/help/mobile-icp-health).

### Il mio file ICP non si carica {#my-icp-file-wont-upload}

Cora legge il report in PDF che ti manda il laboratorio. Foto e screenshot non si possono leggere. Scarica prima il PDF dal tuo laboratorio, poi tocca di nuovo **Carica ICP**.

### Lo schermo diventa nero dopo un report di salute o un caricamento ICP {#black-screen-after-a-report}

Poteva succedere in Cora Mobile 1.2 e versioni precedenti, e Cora Mobile 1.3 lo risolve: aggiorna Cora Mobile dall'App Store o da Google Play. Se ti capita prima di aggiornare, chiudi Cora Mobile e riaprila. Il report è stato salvato, e lo trovi in **Intelligence**.

## Lingua, unità e accesso {#language-units-and-signing-in}

### All'improvviso è tutto nella lingua sbagliata {#everything-is-suddenly-in-the-wrong-language}

Qualcuno ha cambiato la lingua dell'account su uno dei tuoi dispositivi. È un'unica impostazione per tutto l'account.

1. Apri **Impostazioni → Lingua** in Cora Mobile o su Cora Max.
2. Rimettila com'era. La modifica vale ovunque.

### Un vecchio avviso o report è in un'altra lingua dopo il cambio {#an-old-alert-or-report-is-still-in-a-different-language-afte}

È normale. Cora non ritraduce niente di quello che ha già scritto. I nuovi avvisi, report e briefing usano la nuova lingua.

### "Impossibile raggiungere Cora. Controlla il Wi-Fi o i dati mobili, poi riprova." {#could-not-reach-cora-check-your-wi-fi-or-mobile-data-then-tr}

Il telefono non riesce a raggiungere Cora Cloud per l'accesso. Riguarda la connessione del telefono, non l'attrezzatura della vasca.

1. Controlla che il telefono abbia il Wi-Fi o i dati mobili funzionanti.
2. Prova un'altra rete se ne hai una.
3. Tocca **Riprova**.

Gli altri problemi di accesso sono in [Accesso e recupero dell'account](/help/mobile-account).

## Ancora bloccato {#still-stuck}

Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**, oppure segnalalo da Cora Mobile come descritto in [Segnalare un problema](/help/mobile-support). Dicci quale vasca, quale dispositivo, quale schermata e cosa ti aspettavi di vedere.
