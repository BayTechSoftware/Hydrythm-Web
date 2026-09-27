---
title: Risoluzione dei problemi
description: Le letture si sono fermate, un dispositivo è andato offline, gli avvisi non si chiudono, o qualcosa non va. Inizia da qui.
section: Help
reviewed: 2026-09-27
order: 1
---

Parti dal sintomo.

## Un widget non mostra nessun valore

Scorri questo elenco:

1. **Controlla l'età dei widget vicini.** Se tutto è obsoleto, il problema è la connessione, non il parametro.
2. **Apri la scheda Dispositivi.** Un dispositivo che non può essere raggiunto lo dice sulla sua riga.
3. **Controlla l'assegnazione della vasca.** Un dispositivo che riporta nella vasca sbagliata sembra esattamente un dispositivo che non riporta affatto. Apri il dispositivo e confermane la vasca.
4. **Controlla che la fonte esista.** Nulla riporta i fosfati a meno che tu non abbia un equipaggiamento che li misura o li registri a mano.

## Una lettura è obsoleta

Il badge dell'età ti sta dicendo la verità: non è arrivato nulla di nuovo.

- **I parametri registrati a mano** diventano obsoleti quando non è stata inserita nessuna lettura. Registrane una.
- **Le letture dell'equipaggiamento** che diventano obsolete significano che il dispositivo ha smesso di riportare; controlla la sua riga in **Dispositivi**.
- **Alcuni equipaggiamenti sono pensati per essere lenti.** Un titolatore che misura ogni ora normalmente mostra `1h`. Non è un guasto.

## Un dispositivo non può essere raggiunto

Di solito è la rete.

1. L'equipaggiamento è acceso e funziona nella sua propria app?
2. È sulla stessa rete su cui è stato aggiunto?
3. Il tuo router è cambiato (nuovo hardware, nuovo nome della rete, isolamento della rete ospiti)?

L'equipaggiamento che si collega tramite la tua rete locale deve essere raggiungibile su quella rete. L'equipaggiamento che si collega tramite un account del produttore no, ma ha bisogno che quell'account sia ancora valido.

## Un dispositivo dice che l'accesso è stato rifiutato

Il produttore ha rifiutato l'accesso memorizzato. Quasi sempre perché hai cambiato la tua password con loro.

Apri la riga del dispositivo ed accedi di nuovo.

## L'associazione di un Cora Max fallisce

Se aggiungere un Cora Max si ferma a metà, Cora Mobile dice quale passaggio è fallito e perché, con **Annulla** e **Riprova** sotto.

- *"Il tuo telefono non è riuscito a raggiungere il Cora Max sul tuo Wi-Fi."* Metti il tuo telefono e il Cora Max sulla stessa rete Wi-Fi. Su iPhone, controlla anche che Cora abbia l'accesso alla Rete locale: **Impostazioni → Accesso dispositivi** ti porta lì (vedi [Impostazioni](/help/mobile-settings)). Poi tocca **Riprova**.
- *"Il Cora Max non ha accettato questa sessione di associazione."* Riprovare non aiuterà. Chiudi la schermata e ricomincia da **Dispositivi → Aggiungi dispositivo**.

Per qualsiasi altro messaggio, tocca **Riprova**.

## Cora Max mostra dati vecchi

Controlla la pillola di stato nella barra superiore. **Online** e **Cloud** sono entrambi sani: con più di un Cora, lo schermo che non sta facendo la raccolta mostra **Cloud**, e le sue letture sono altrettanto attuali. **Non aggiornato** o **Offline** significa che lo schermo ha perso la sua fonte e mostra gli ultimi dati che ha ricevuto (comportamento corretto, ma non attuale).

- Controlla il Wi-Fi sotto **Impostazioni → Cora Max → Rete**
- Controlla che la rete stessa sia attiva
- Se la pillola mostra **Online** o **Cloud** e i dati sono ancora vecchi, il problema è a monte: controlla la stessa vasca sul tuo telefono

## Un avviso non si chiude

Un avviso si chiude quando la lettura torna nell'intervallo. Se non si chiude:

- **La lettura è genuinamente fuori intervallo.** Guarda lo storico del widget.
- **La soglia è sbagliata per la tua vasca.** Vedi [Avvisi e soglie](/help/mobile-alerts).
- **La fonte è sbagliata.** Una sonda che ha bisogno di calibrazione riporta un numero che è genuinamente fuori intervallo. Correggi la sonda invece della soglia.

## Due fonti non sono d'accordo

Questo è Cora che funziona, non Cora che fallisce. Quando la tua sonda e il tuo kit di test non sono d'accordo, questo è un fatto reale sul tuo sistema.

Un risultato ICP è una terza opinione utile qui, ma non risolve la disputa: i laboratori differiscono tra loro, e la manipolazione e il trasporto di un campione spostano il risultato. Due test in accordo valgono molto più di uno solo.

Di solito la sonda ha bisogno di calibrazione; a volte il kit di test è vecchio. Calibra la sonda, esegui di nuovo il test con reagente fresco, e confronta i due nelle stesse condizioni. Un [risultato ICP](/help/mobile-icp-health) aggiunge un terzo dato a quel confronto.

## Non ricevo notifiche

1. **Impostazioni → Notifiche**: controlla che quella categoria sia autorizzata a inviare notifiche push
2. Controlla i permessi di notifica del tuo telefono per Cora
3. Ricorda che il briefing giornaliero è deliberatamente silenzioso nei giorni in cui nulla è cambiato

## Stabilire perché qualcosa è cambiato

**Impostazioni → Attività** elenca ogni commutazione di presa, alimentazione, dosaggio e cambio di presa intelligente, con cosa l'ha richiesto: Cora Mobile, uno schermo Cora, la voce, l'Assistant, una regola di automazione, un pulsante smart o il tuo account.

## La mia dashboard sembra sbagliata dopo la modifica

Carica un design salvato: **Le mie dashboard**, poi scegline uno.

Se non ne hai salvato uno, ricrea il layout e poi salvalo come design. Da quel momento in poi, tornarci è un solo tocco.

In entrambi i casi, letture, storico e voci di diario sono memorizzati separatamente dal layout, quindi nulla dietro la dashboard viene perso.

## "Le letture Red Sea hanno smesso di aggiornarsi"

**Cosa significa:** Nessun dispositivo sulla rete di questa vasca sta attualmente interrogando il tuo equipaggiamento Red Sea, quindi le letture sullo schermo non sono state aggiornate.

**Cosa fare:**
1. Apri **Impostazioni → Cora Max principale** e controlla che sia impostato un Cora Max (oppure che sia scelto **Qualsiasi attivo (automatico)**).
2. Apri la vasca su un dispositivo che è sullo stesso Wi-Fi dell'apparecchiatura Red Sea.
3. Conferma che l'equipaggiamento Red Sea sia acceso e online nella sua propria app.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con il nome della vasca e del dispositivo.

## "Impossibile raggiungere questa pompa: nulla è stato inviato"

**Cosa significa:** Un comando a una pompa Jecod o Jebao non è mai partito dall'app, di solito perché la pompa è spenta o fuori dalla sua rete.

**Cosa fare:**
1. Controlla che la pompa sia accesa.
2. Controlla che sia sulla stessa rete su cui è stata aggiunta.
3. Tocca **Riprova**.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con il nome della vasca e del dispositivo.

## "Impossibile raggiungere questa pompa via Bluetooth. Stai vicino ad essa e riprova."

**Cosa significa:** Un dispositivo Jecod solo Bluetooth è fuori dalla portata del tuo telefono.

**Cosa fare:**
1. Avvicinati alla pompa.
2. Tocca **Riprova**.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con il nome della vasca e del dispositivo.

## "Impossibile raggiungere quella gyre. Nessuna alimentazione è stata avviata."

**Cosa significa:** Una gyre Maxspect (integrazione beta) non ha risposto quando Cora ha provato ad avviare la modalità alimentazione su di essa.

**Cosa fare:**
1. Controlla che la gyre sia accesa e sulla sua rete.
2. Tocca **Riprova**.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con il nome della vasca e del dispositivo.

## "Impossibile raggiungere quella gyre. Il suo programma non è stato cambiato."

**Cosa significa:** Un invio di programma a una gyre Maxspect (integrazione beta) non è riuscito a raggiungerla.

**Cosa fare:**
1. Controlla che il tuo telefono o Cora Max sia sulla rete della gyre.
2. Tocca **Riprova** dalla schermata del programma.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con il nome della vasca e del dispositivo.

## "Impossibile raggiungere l'Apex: nulla è cambiato" / "nulla è stato dosato"

**Cosa significa:** Un Neptune Apex, Trident, o testa DŌS non ha risposto a un comando o a una richiesta di dosaggio.

**Cosa fare:**
1. Apri l'app propria dell'Apex e conferma che sia online.
2. Controlla la connettività di rete sul dispositivo che stai usando.
3. Tocca **Riprova**.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con il nome della vasca e del dispositivo.

## "Questo non può essere inviato: nessun dispositivo su questa vasca può inviarlo"

**Cosa significa:** Nessun dispositivo Cora su questa vasca ha i dettagli di connessione dell'Apex necessari per eseguire il comando, oppure quello che li ha è offline.

**Cosa fare:**
1. Aggiungi i dettagli dell'Apex in **Impostazioni** su un dispositivo che è attualmente online, oppure
2. Imposta un altro Cora Max funzionante come **Cora Max principale** per questa vasca.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con il nome della vasca e del dispositivo.

## Un Cora Max secondario mostra "Cora principale offline"

**Cosa significa:** Il tablet principale per questa vasca è andato offline, quindi questo schermo secondario mostra gli ultimi dati che ha ricevuto invece di dati in tempo reale.

**Cosa fare:**
1. Controlla l'alimentazione e il Wi-Fi del tablet principale.
2. Aspetta che si riconnetta, oppure cambia il **Cora Max principale** a un dispositivo che è attualmente online.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con il nome della vasca e del dispositivo.

## "Dispositivo offline. Mostra l'ultimo stato conosciuto."

**Cosa significa:** Gestione normale della disconnessione: il dispositivo ha smesso di riportare, e Cora sta mostrando gli ultimi valori che aveva invece di fingere che siano attuali.

**Cosa fare:**
1. Controlla la connessione di rete propria del dispositivo.
2. Tratta i valori mostrati come non in tempo reale finché la riga non dice più offline.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con il nome della vasca e del dispositivo.

## Alcune impostazioni ReefBeat sono disattivate in grigio o mancanti

**Cosa significa:** Questo è per progetto, non un guasto. Le impostazioni native del dispositivo (a differenza delle letture) si aprono solo quando il tuo telefono è sulla stessa rete del dispositivo stesso; lontano da quella rete, si mostrano solo le letture.

**Cosa fare:**
1. Vai sul Wi-Fi proprio della vasca per cambiare quelle impostazioni.
2. Letture e storico continuano a funzionare normalmente lontano dalla vasca.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## "Impossibile raggiungere Cora. Controlla il tuo Wi-Fi o i dati mobili, poi riprova."

**Cosa significa:** Il tuo telefono non ha una connessione utilizzabile a Cora Cloud al momento dell'accesso. Questo riguarda la connettività propria del tuo telefono, non l'equipaggiamento della tua vasca.

**Cosa fare:**
1. Controlla che il tuo telefono abbia una connessione Wi-Fi o dati mobili funzionante.
2. Prova una rete diversa se ne è disponibile una.
3. **Riprova**.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Tutto è improvvisamente nella lingua sbagliata

**Cosa significa:** La lingua dell'account è stata cambiata da qualsiasi dispositivo. La lingua è un'unica impostazione per tutto l'account, non per dispositivo.

**Cosa fare:**
1. Apri **Impostazioni → Lingua** su entrambe le app.
2. Ripristinala se è stata cambiata per errore; il cambiamento si applica ovunque contemporaneamente.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un vecchio avviso o rapporto è ancora in una lingua diversa dopo il cambio

**Cosa significa:** Questo è previsto, non un bug. Cora non ritraduce contenuti già generati; solo i nuovi avvisi, rapporti e briefing seguono la nuova lingua.

**Cosa fare:**
1. Nulla da correggere. Aspetta i nuovi contenuti, che useranno la lingua attuale.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un avviso non smette di notificare anche dopo che l'ho confermato

**Cosa significa:** Confusione tra **Ignora** (chiude l'avviso definitivamente) e **Rinvia** (lo silenzia temporaneamente, fino a una settimana).

**Cosa fare:**
1. Se capisci e accetti la condizione, usa **Ignora**.
2. Se vuoi solo silenzio per un po', usa **Rinvia** e scegli una durata.

**Ancora non funziona?** Vedi [Avvisi e soglie](/help/mobile-alerts), oppure scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un dosaggio si è fermato a metà ed è apparso un avviso di "ripristino"

**Cosa significa:** La testa DŌS ha perso il contatto a metà del dosaggio, quindi Cora te lo dice deliberatamente invece di supporre che il dosaggio completo sia entrato.

**Cosa fare:**
1. Apri l'avviso e controlla quanto è stato effettivamente dosato prima che si fermasse.
2. Riprendi o correggi il dosaggio in base a quella quantità, non a quella originariamente programmata.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con il nome della vasca e del dispositivo.

## Una scena creata sul telefono non appare modificabile su Cora Max

**Cosa significa:** Modificare le scene direttamente sul tablet è una funzione più recente di Cora Max. Il firmware più vecchio può ancora eseguire scene create sul telefono, ma non modificarle lì.

**Cosa fare:**
1. Aggiorna Cora Max, oppure
2. Continua a modificare quella scena dal telefono; verrà eseguita comunque sul tablet.

**Ancora non funziona?** Vedi [Aggiornamenti e ripristino](/help/max-updates), oppure scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant risponde sulla vasca sbagliata

**Cosa significa:** Non è stata scelta nessuna vasca prima di chiedere, oppure la vasca sbagliata è attualmente attiva.

**Cosa fare:**
1. Scegli prima la vasca che intendi.
2. Chiedi di nuovo.

**Ancora non funziona?** Vedi [L'Assistant](/help/mobile-assistant), oppure scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant si rifiuta di rispondere, o mostra di nuovo una schermata di consenso

**Cosa significa:** "Consenti al Cora Assistant di usare i dati salvati della vasca" è stato disattivato, quindi non ha nulla da cui rispondere.

**Cosa fare:**
1. Tocca **Accetta e continua** sulla schermata di consenso per riattivarlo.

**Ancora non funziona?** Vedi [L'Assistant](/help/mobile-assistant), oppure scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un risultato ICP di laboratorio o via email non è mai apparso

**Cosa significa:** Far entrare un risultato in Cora richiede che venga scelta una vasca per esso, e a volte un mittente riconosciuto, prima che si attacchi a qualcosa.

**Cosa fare:**
1. Controlla il suggerimento di ingresso mostrato la prima volta che invii un risultato a Cora.
2. Conferma a quale vasca dovrebbe attaccarsi il risultato quando richiesto.
3. Assicurati che l'email sia stata inviata dall'indirizzo che hai usato per inviarla prima, se ne hai inviata una in precedenza.

**Ancora non funziona?** Vedi [ICP e rapporti di salute](/help/mobile-icp-health), oppure scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Una notifica di ICP via email non nomina nessun laboratorio

**Cosa significa:** Un problema conosciuto con la notifica push "scegli vasca" che manca del nome del laboratorio. È stato risolto nelle build attuali.

**Cosa fare:**
1. Assicurati che Cora Mobile sia aggiornato all'ultima versione.
2. Il risultato stesso non è affetto; solo al testo della notifica mancava un nome.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un widget mostra le unità sbagliate

**Cosa significa:** Questa è l'impostazione delle unità di visualizzazione della vasca, non un problema di dati. I valori sono memorizzati nello stesso modo indipendentemente da come vengono visualizzati.

**Cosa fare:**
1. Apri **Impostazioni** per quella vasca e controlla le sue unità di visualizzazione.
2. Cambiale lì; ogni telefono e Cora Max che mostra quella vasca si aggiorna per corrispondere.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un indicatore o una soglia sembrano diversi dopo aver cambiato le unità di visualizzazione

**Cosa significa:** Previsto. Indicatori, riquadri e storico si ridisegnano nell'unità che hai scelto; i valori sottostanti non sono cambiati.

**Cosa fare:**
1. Nulla da correggere; è solo estetico.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Max non si riconnette immediatamente dopo un'interruzione del Wi-Fi

**Cosa significa:** Dopo aver perso la connessione, Cora Max aspetta un po' più a lungo prima di ogni tentativo invece di martellare la rete, arrivando a circa un minuto prima di riprovare.

**Cosa fare:**
1. Aspetta circa un minuto dopo che la tua rete torna.
2. Se ancora non si è riconnesso dopo quello, controlla il Wi-Fi sotto **Impostazioni → Rete**.

**Ancora non funziona?** Vedi [La schermata Home di Cora Max](/help/max-tour), oppure scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Rinominare un Cora Max dal telefono non cambia cosa mostra il tablet

**Cosa significa:** Il nome che impostati dal telefono è un'etichetta a livello di account per quel dispositivo. Il nome mostrato sul tablet stesso durante l'associazione può essere una cosa diversa.

**Cosa fare:**
1. Controlla quale "nome" stai guardando: quello nel tuo elenco dispositivi sul telefono, o quello sulla schermata di associazione propria del tablet.
2. Rinomina dall'elenco dispositivi del telefono se è l'etichetta dell'account che vuoi cambiare.

**Ancora non funziona?** Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con il nome del dispositivo.

## Non trovo dove disattivare la parola di attivazione su Cora Max

**Cosa significa:** L'interruttore della parola di attivazione si trova sotto **Audio**, non sotto il gruppo di impostazioni Cora Assistant, il che sorprende la maggior parte delle persone.

**Cosa fare:**
1. Vai a **Impostazioni → Audio → Ascolto parola di attivazione**.
2. Disattivalo; puoi ancora toccare l'icona Cora per avviare una sessione vocale.

**Ancora non funziona?** Vedi [Impostazioni su Cora Max](/help/max-settings), oppure scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Il blocco bambini non lascia entrare nessuno in Impostazioni

**Cosa significa:** Questo funziona come previsto. Il blocco bambini blocca il touchscreen e i controlli vocali dopo un tempo impostato senza tocchi; le letture continuano ad aggiornarsi sotto di esso.

**Cosa fare:**
1. Premi **Volume su** o **Volume giù** tre volte entro due secondi, oppure
2. Tieni cinque dita nell'angolo in alto a destra dello schermo per dieci secondi.

**Ancora non funziona?** Vedi [La voce su Cora Max](/help/max-voice), oppure scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Ancora bloccato

Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)**. Dicci quale vasca, quale schermata, e cosa ti aspettavi di vedere; ottieni una risposta utile più rapidamente.
