---
title: Controllare la tua attrezzatura
description: Apri la pagina di un dispositivo per vederne lo stato in tempo reale e comandare prese, pompe, teste di dosaggio e tester, marca per marca.
section: Cora Mobile
reviewed: 2026-10-13
order: 13
group: Equipment
twin: max-device-control
---

Usa la pagina di un dispositivo per vederne lo stato in tempo reale e cambiare quello che sta facendo. Aprila da **Dispositivi** → tocca il dispositivo, oppure tocca il suo riquadro sulla dashboard.

![La pagina di un ReefATO+ in Cora Mobile](img/mobile-device-detail.webp "Lo stato, le letture di oggi e il livello dell'acqua, poi perdite, rabbocchi e calibrazione della sonda.")

Ogni pagina dispositivo è organizzata allo stesso modo. Nome e dettagli sono in alto, poi una fila di letture in tempo reale, gli stati che il dispositivo riporta e i suoi comandi. La campanella nella barra del titolo imposta le soglie di avviso per quel dispositivo, come descritto in [Materiali di consumo](/help/mobile-consumables). Come aggiungere un dispositivo all'inizio è spiegato in [Collegare la tua attrezzatura](/help/mobile-connections).

Vai alla tua attrezzatura: [Neptune Apex](#neptune-apex) · [Trident](#trident) · [DŌS](#dos) · [Red Sea](#red-sea) · [ReefDose](#reefdose) · [ReefRun](#reefrun) · [ReefMat](#reefmat) · [ReefATO+](#reefato) · [Avvisi del dosatore](#doser-alerts) · [Jecod](#jecod) · [AquaWiz](#aquawiz) · [Maxspect](#maxspect) · [GHL](#ghl) · [HYDROS](#hydros) · [Focustronic](#focustronic) · [EcoTech, Inkbird e telecamere](#ecotech-inkbird-cameras)

:::warning Questi comandi agiscono sull'attrezzatura in funzione
Non c'è anteprima e non c'è annulla. Alcuni comandi ti chiedono prima di confermare.
:::

## Cosa succede quando invii un comando {#what-happens-when-you-send-a-command}

Un comando non va sempre a buon fine. Cora ti dice quale di quattro cose è successa:

| Esito | Significato |
|---|---|
| **Confermato** | L'attrezzatura ha accettato la modifica e ha riportato il suo nuovo stato |
| **Non confermato** | Il comando è partito, ma non è tornata nessuna risposta. **Vuol dire "non lo sappiamo". Non vuol dire che abbia funzionato.** Controlla lo stato del dispositivo stesso |
| **Rifiutato** | Qualcosa l'ha respinto (una regola di sicurezza, un blocco o l'attrezzatura stessa), oppure nessun dispositivo Cora l'ha preso in tempo. È stato annullato e non è stato eseguito niente |
| **Nessun cambiamento** | L'attrezzatura era già impostata come hai chiesto |

Ogni esito viene registrato in [Attività](/help/mobile-activity), insieme a cosa l'ha causato.

Senza un Cora Max nella vasca, l'attrezzatura Neptune Apex, Red Sea e Jecod funziona solo in locale: il telefono deve essere sulla stessa rete (o a portata Bluetooth) per inviare un comando. Con un Cora Max nella vasca, Cora Mobile lo invia tramite quel Cora Max, anche quando sei fuori casa.

## Neptune Apex {#neptune-apex}

![La pagina di un Apex in Cora Mobile, con lo stato, i moduli Trident e DŌS, Mappatura parametri e la vasca che serve](img/mobile-apex.webp "La pagina dell'Apex: Stato, Moduli, Mappatura parametri e Vasche.")

La pagina dell'Apex mostra lo stato del controller, poi **Moduli**, **Mappatura parametri** e **Vasche**.

- **Moduli** elenca ogni Trident e DŌS installato. Toccane uno per aprire la sua pagina.
- **Mappatura parametri** è dove scegli cosa alimenta ogni sonda. Le sonde arrivano in Cora come fonti, e puoi metterle su una dashboard. Vedi [Mappatura parametri e sonde](/help/mobile-probes).
- **Vasche** mostra quali vasche serve l'Apex. Tocca **Modifica** per cambiarle.
- Le **prese** passano tra **Auto**, **Off** e **On** da un widget **Presa** sulla dashboard. Auto restituisce il controllo alla programmazione del tuo Apex. Vedi [Guida ai widget](/help/mobile-widgets#outlet).

Il tuo Apex continua a seguire la sua programmazione. Cora cambia una presa solo quando glielo chiedi.

## Trident {#trident}

La pagina del Trident mostra lo stato attuale del test e i livelli di reagente e acqua di scarico. Da qui puoi avviare un test.

Puoi anche impostare un avviso per i test rimanenti e per il flacone dei rifiuti, così Cora ti avvisa prima che finisca il reagente o che il flacone si riempia. Vedi [Materiali di consumo](/help/mobile-consumables).

## DŌS {#dos}

![La pagina di un DŌS che dice che il DŌS non risponde sull'AquaBus, con l'ultima autonomia, la dose di oggi e il piano giornaliero, poi la riga Avvisi](img/mobile-dos.webp "Un DŌS fuori dall'AquaBus: la pagina mostra gli ultimi valori noti, una scheda Richiede attenzione e la riga Avvisi.")

Un DŌS QD funziona esattamente come un DŌS, e tutto quello che c'è qui vale per entrambi. Quando un Cora Max legge il tuo Apex, le teste di dosaggio compaiono nella pagina del DŌS. Non compaiono mai nell'elenco delle prese.

Ogni testa di dosaggio mostra cosa sta dosando, il suo programma, quanto ha dosato oggi e quanto resta nel contenitore. Mostra anche l'**autonomia**, cioè quanti giorni durerà al ritmo attuale.

Se il DŌS smette di rispondere sull'AquaBus, la sua pagina mostra **Fuori bus** e una scheda **Richiede attenzione**. I valori sulla pagina sono allora gli ultimi riportati, non quello che sta facendo adesso. Controlla il cavo AquaBus del modulo e l'Apex.

Per ogni testa puoi:

- **Sospendi** e **Riprendi** il suo programma
- **Riempi**, per dire a Cora che il contenitore è di nuovo pieno o impostare quanto ne contiene (**Volume totale** è la dimensione del contenitore, **Volume rimanente** è quanto c'è adesso, e **Pieno** imposta l'uno uguale all'altro)
- **Dosa ora**, per una dose misurata a mano

:::note Modifica i programmi in Apex Fusion
Cora mostra il programma e tiene traccia di quanto è stato dosato, ma non cambia il programma. Programma, velocità di dosaggio e numero di dosi si modificano nell'app Apex Fusion. Sospendere, riempire e dosare a mano funzionano qui.
:::

:::note Misura una testa prima di dosare a mano
Cora non dosa a mano da una testa finché la testa non è stata misurata. **Misura per dosare** e **Rimisura** sono sul Cora Max che dosa per la vasca. Cora fa funzionare la testa per venti secondi, tu misuri quanto è uscito e Cora calcola la velocità reale della testa. Una misura vale per ogni Cora Max e per Cora Mobile. Misura ogni testa una volta, e di nuovo dopo aver cambiato il tubo.
:::

:::warning Un DŌS continua a dosare quando il contenitore è vuoto
L'unità non ha un sensore di livello e non si ferma da sola. Imposta un avviso di rifornimento per ogni testa in **Avvisi** nella pagina del DŌS, così Cora ti avvisa prima che il contenitore resti a secco. Vedi [Avvisi del dosatore](#doser-alerts).
:::

### A cosa serve ogni testa {#dos-head-use}

Dai a ogni testa un **tipo di uso** così Cora sa cosa fa e ne parla correttamente. Le scelte sono **Integratore**, **Cambio d'acqua: nuova acqua salata in entrata**, **Cambio d'acqua: acqua vecchia in uscita**, **Acqua di calce**, **Reattore di calcio**, **Alimento**, **Rabbocco** e **Altro**. Impostalo in **Usata per** nelle impostazioni della testa.

I due tipi di uso del cambio d'acqua vanno in **coppia**. Imposta la **Testa abbinata** di una testa sulla testa che sposta l'acqua nel verso opposto, e Cora tratta le due come un'unica coppia per il cambio d'acqua.

Un contenitore può arrivare a 1.000 L, per ogni tipo di uso. L'Apex da solo conta solo fino a 150 L, quindi oltre quel valore Cora segue il contenitore da sé in base a quanto dosa la testa. Inserisci il **Volume totale** quando lo configuri. Cora inoltre ogni tanto azzera il contatore interno dell'Apex, e Attività lo mostra come *Contatore interno dell'Apex reimpostato a 150 L*.

Ogni testa ha anche un limite **Dose massima manuale**, così un errore di battitura non può trasformare una dose manuale in qualcosa di molto più grande di quello che volevi. Le dosi manuali grandi diventano disponibili solo dopo che la velocità della testa è stata misurata con un test reale alla vasca, e dopo che hai attivato **Dosi grandi (Beta)** nelle impostazioni della testa. È spento di default. Attivalo solo dopo aver guardato la prima dose grande eseguita alla vasca.

## Red Sea ReefBeat {#red-sea}

Ogni unità Red Sea ha una pagina adatta a quello che fa:

| Unità | La pagina mostra | Puoi |
|---|---|---|
| [ReefDose](#reefdose) | Ogni testa, il suo contenitore e quanto ha dosato | Dosare, cambiare la dose giornaliera, modificare il **Piano di dosaggio (Beta)** |
| [ReefRun](#reefrun) | Velocità e stato delle pompe di risalita e dello schiumatoio | Cambiare la velocità, accendere o spegnere una pompa, modificare il **Programma della pompa (Beta)** |
| [ReefMat](#reefmat) | Il rotolo rimanente, in giorni e metri | Far avanzare il tappetino, impostare **Impostazioni ReefMat (Beta)**, registrare un rotolo nuovo |
| [ReefATO+](#reefato) | Livello del serbatoio e attività di rabbocco | Impostare un avviso per il serbatoio |
| **ReefControl** *(Beta)* | Le sue sonde di temperatura, pH, salinità e ORP | Vederne le letture |
| **ReefWave**, **ReefLED** *(Beta)* | La sua modalità attuale | Solo visualizzazione, per ora |

ReefControl, ReefControl Power, ReefWave e ReefLED hanno *(Beta)* nel nome ma sono disponibili per tutti. Vedi [Funzioni Beta](/help/mobile-beta).

Le prese di **ReefControl Power** *(Beta)* compaiono come prese, comandate dallo stesso comando di una presa Apex, solo accese o spente. Per loro non c'è ancora una modalità automatica.

Quando sei lontano dalla rete dell'unità, Cora Mobile invia i comandi Red Sea tramite un Cora Max nella vasca. Se nessun Cora Max può farlo, la pagina lo dice e non viene inviato niente.

## ReefDose {#reefdose}

![La pagina di un ReefDose 4 in Cora Mobile](img/mobile-reefdose.webp "Lo stato, le teste e il totale di oggi, Usa il dosatore per i consumi, poi ogni testa di dosaggio.")

Per ogni testa puoi impostare **Dose al giorno** e **Rimanente nella bottiglia**, usare **Dosa ora** e **Attiva programma**. Gli avvisi di rifornimento si impostano per testa con la campanella, come descritto in [Avvisi del dosatore](#doser-alerts).

La sezione **Dosaggio** mostra le **Prossime dosi**, quanto ha dosato oggi ogni testa (**Dosato oggi finora**) e **Dosato per testa** negli **Ultimi 7 giorni** o in **Totale**. Cora legge questi dati mentre un Cora Max o il tuo telefono è sulla rete di casa.

### Modificare un piano di dosaggio *(Beta)* {#reefdose-plan}

Tocca l'icona del calendario nella pagina di un ReefDose per aprire il **Piano di dosaggio (Beta)**.

Un piano è un totale giornaliero, diviso in un massimo di quattro fasce orarie. Ogni fascia ha un'ora di inizio e di fine, quante dosi deve erogare e una velocità: **Silenzioso**, **Normale** o **Rapido**. Aggiungi e togli le fasce, poi salva. Cora ti mostra cosa stai per inviare e ti chiede di confermare prima di sostituire tutto il piano della testa.

L'editor legge prima il piano che c'è già sull'unità, quindi stai modificando quello vero, non un modulo vuoto.

## ReefRun {#reefrun}

ReefRun comanda le pompe di risalita e dello schiumatoio. Non è una pompa di movimento. Puoi cambiare la velocità di una pompa, accenderla o spegnerla e regolare le impostazioni dello schiumatoio.

Tocca l'icona del calendario per aprire il **Programma della pompa (Beta)**. Un programma ha fino a sei segmenti su una porta della pompa. Ogni segmento ha un'ora di inizio e una velocità, e può aggiungere un breve impulso. La velocità è 0 oppure dal 5% in su. Come il piano del ReefDose, legge prima il programma sull'unità, e **Salva** ti chiede di confermare prima di sostituire tutto il programma della pompa.

## ReefMat {#reefmat}

La pagina del ReefMat mostra quanto rotolo resta, in giorni e metri. Tocca **Avanza ora** per far avanzare il tappetino a mano. Cora chiede prima **Avanzare il tappetino ora?** Puoi anche impostare un avviso di rifornimento per il rotolo.

Tocca l'ingranaggio per **Impostazioni ReefMat (Beta)**:

- **Avanzamento programmato** attiva un avanzamento a orari fissi, separato dal sensore di avanzamento automatico già presente nella pagina. Attivalo e imposta ogni quanto, e di quanto ogni avanzamento sposta il tappetino.
- **Modello ReefMat** e **Posizione motore** (**Sinistra** o **Destra**) dicono a Cora quale unità e quale orientamento hai.

Dopo aver caricato un rotolo nuovo, dillo a Cora con **Nuovo rotolo (Beta)**: il suo spessore, e il diametro esterno se lo conosci. **Avanza ora** fa solo avanzare il tappetino che hai già caricato.

## ReefATO+ {#reefato}

La pagina del ReefATO+ mostra il livello del serbatoio e i rabbocchi recenti. Imposta un avviso per il serbatoio con la campanella. Cora stima quanti giorni restano al serbatoio dal consumo recente di rabbocco, e puoi chiederlo anche all'Assistente.

## Quando un'unità Red Sea si ferma da sola {#red-sea-stops}

Un'unità può fermarsi da sola. Una pompa ReefRun lo fa quando si riempie la coppetta dello schiumatoio, per esempio. Quando succede, la pagina dice perché e propone la soluzione:

| Unità | La pagina dice | Tocca |
|---|---|---|
| ReefRun | Quale pompa si è fermata e perché, per esempio *Coppetta piena. Vuotala, poi riprendi.* | **Riprendi** |
| ReefRun o ReefMat | **Arresto di emergenza** | **Elimina emergenza** |
| ReefMat | **Tappetino inceppato**, **Errore di installazione** o **Errore di configurazione** | **Riprendi** |
| ReefMat | *Carica un nuovo rotolo, poi confermalo nell'app di Red Sea.* | **Ho già caricato un nuovo rotolo** |
| ReefMat | **Il sensore richiede pulizia** | **Sensore pulito** |
| ReefDose | **Malfunzionamento della testa**, con il nome della testa | **Ripristina** |
| ReefATO+ | **Elimina guasto** | **Riprendi** |

Alcuni di questi ti chiedono prima di confermare. Lontano dalla rete dell'unità passano da un Cora Max nella vasca, come descritto in [Red Sea ReefBeat](#red-sea).

## Avvisi del dosatore {#doser-alerts}

Un DŌS e un ReefDose tengono i loro avvisi nella loro pagina. La scheda **Regole** del [Centro avvisi](/help/mobile-alerts) ha una riga per dosatore che la apre, e anche il pulsante **Apri dosatore** di un avviso del dosatore ti porta qui.

Nella pagina di un DŌS, tocca la scheda **Avvisi** (o la campanella nella barra del titolo). Il pannello elenca ogni testa, e per ognuna puoi impostare:

- *[testa] · giorni rimanenti*, per esempio *Iodio · giorni rimanenti*: ricevi un avviso sotto questo numero di giorni di scorta
- *[testa] · rimanente*: ricevi un avviso sotto questa quantità rimasta nel contenitore
- **Spazio rimanente nel contenitore dei rifiuti**, per una testa che toglie l'acqua vecchia: ricevi un avviso quando il contenitore dei rifiuti si sta riempiendo
- **Avvisi di dose mancata**: un interruttore che ti avvisa quando la testa salta una dose programmata

Ogni soglia ha il suo interruttore, così puoi spegnerne una e tenerne il valore. Tocca **Salva** quando hai finito.

Nella pagina di un ReefDose, tocca la campanella nella barra del titolo. Ogni testa ha la sua soglia di giorni rimanenti e il suo interruttore.

I valori predefiniti e gli altri materiali di consumo sono in [Materiali di consumo](/help/mobile-consumables).

## Pompe Jecod / Jebao {#jecod}

La pagina della pompa mostra lo schema d'onda attuale (modalità) e l'intensità, e puoi cambiarli entrambi. Scegli **Uguale tutto il giorno** o **Programma** in alto. Creare un programma giornaliero, e copiarlo, salvarlo o condividerlo, è spiegato in [Programmare l'attrezzatura](/help/mobile-schedules).

Se la pompa fa parte di un gruppo, la pagina mostra il suo ruolo, come **Guida il gruppo**, **Segue: in sincrono** o **Segue: alternata**.

### Pausa per l'alimentazione {#jecod-feeding}

Avvia una pausa per l'alimentazione dalla sezione **Alimentazione** della pagina della pompa. Alcune pompe terminano la pausa da sole, e la pagina dice *La pompa termina questa fase da sola.*

:::warning Tieni aperta la pagina della pompa durante una pausa per l'alimentazione
Alcune pompe non terminano da sole un'alimentazione, e la pagina lo dice. Per queste, e per qualsiasi pompa con un programma, Cora Mobile ripristina lo schema d'onda e il programma solo finché la pagina della pompa resta aperta. Se lasci la pagina, la pompa resta ferma in modalità alimentazione, o resta fuori dal suo programma, finché non la cambi di nuovo o tocchi **Programma**.
:::

Una pompa Bluetooth deve essere a portata del telefono per avviare un'alimentazione, e una pompa di rete deve essere sulla tua rete.

### Controlli guasti {#jecod-fault-checks}

**Controlli guasti** imposta ogni quanto Cora rilegge la pompa per poterti avvisare di un guasto, come una pompa bloccata o una che gira a secco. Se lo spegni, quegli avvisi si fermano per quella pompa. I controlli guasti richiedono un Cora Max nella vasca. La tua scelta viene salvata e i controlli partono quando ne aggiungi uno. **Usa questo per ogni pompa su questa vasca** copia l'impostazione su tutte.

## AquaWiz {#aquawiz}

La scheda AquaWiz mostra le tue letture di alcalinità, e il pH se la tua unità lo riporta. Mostra anche il tuo KH obiettivo, la concentrazione della dose e, per un'unità con il dosaggio configurato, la dose massima oraria e quanto integratore di alcalinità resta nel contenitore. Questi valori arrivano direttamente dalle tue impostazioni AquaWiz, quindi cambiali nell'app AquaWiz. Cora non può comandare un AquaWiz.

Se la tua unità segue il suo contenitore, Cora ti avvisa quando l'integratore sta finendo, a 100 mL di default. Cambialo dalla sua regola nel [Centro avvisi](/help/mobile-alerts).

## Maxspect {#maxspect}

:::note Beta
**Beta.** Maxspect è in Beta ed è disponibile solo per gli utenti Beta. Se non sei un utente Beta non lo vedrai in **Aggiungi dispositivo**. Per chiedere l'accesso alla Beta, [contatta l'assistenza](/support.html). Alcuni comandi potrebbero essere limitati, e quello che vedi qui potrebbe cambiare da un aggiornamento all'altro. Se qualcosa non funziona come descritto, faccelo sapere da [Segnalare un problema](/help/mobile-support). Di più in [Funzioni Beta](/help/mobile-beta).
:::

La pagina della gyre mostra se la gyre è in funzione, lo schema d'onda e la velocità di **Gyre A** e **Gyre B**, e quando sono state lette l'ultima volta. Da qui puoi:

- Accendere o spegnere la gyre con l'interruttore accanto al suo stato. Cora ti chiede prima di confermare. Spegnere ferma entrambe le gyre e lascia stare il programma.
- Toccare **Modifica impostazioni** per impostare lo schema d'onda e la velocità di ogni gyre, più la durata per gli schemi che ne hanno una, e se le due gyre sono collegate. Cora elenca cosa cambierà e ti chiede di confermare. L'alternanza si imposta nell'app Maxspect, e una gyre che la usa mantiene le sue rampe e i suoi tempi di mantenimento.
- Toccare **Imposta programma** se il programma salvato sulla gyre non si può leggere. Imposta entrambe le gyre così la gyre può ripartire.
- Vedere il programma giornaliero della gyre nella scheda **Programma**. Qui puoi solo guardarlo. Il programma si imposta nell'app Maxspect.
- Controllare **Stato pompa**. Mostra quando la pompa dovrà essere pulita la prossima volta (la pompa fa il conto alla rovescia da sola), la corrente assorbita dalla testa A, quali teste sono installate e il firmware. Tocca **Leggi** per recuperarlo.

:::note Come Cora Mobile raggiunge una gyre
Se un Cora Max serve la vasca, Cora Mobile passa da quel Cora Max, anche quando sei fuori casa. **Modifica impostazioni** parte allora dall'ultima lettura di quel Cora Max. Altrimenti il telefono parla direttamente con la gyre e deve essere sulla rete della gyre. Aprire la pagina legge la gyre. Se la pagina mostra una lettura salvata più vecchia, **Modifica impostazioni** resta nascosto finché non tocchi aggiorna.
:::

## GHL ProfiLux e Mitras {#ghl}

:::note Beta
**Beta.** GHL è in Beta ed è disponibile solo per gli utenti Beta. Se non sei un utente Beta non lo vedrai in **Aggiungi dispositivo**. Per chiedere l'accesso alla Beta, [contatta l'assistenza](/support.html). Alcune letture o alcuni comandi potrebbero non funzionare ancora, e quello che vedi qui potrebbe cambiare da un aggiornamento all'altro. Se qualcosa non funziona come descritto, faccelo sapere da [Segnalare un problema](/help/mobile-support). Di più in [Funzioni Beta](/help/mobile-beta).
:::

La pagina del controller mostra sonde, prese, dosatori e sensori di livello e, sui modelli Director, i risultati dei test di KH e ioni.

I comandi restano spenti finché non attivi **Consenti il controllo da Cora (Beta)** nella pagina del dispositivo. È spento di default, e attivarlo permette a Cora di inviare a quel controller comandi di pausa alimentazione, manutenzione, cambio d'acqua, temporale, illuminazione, valori impostati e prese. Una volta che puoi aggiungere il dispositivo, questo interruttore non richiede altri accessi.

Quando è attivo:

- Una presa si può impostare su **Sempre acceso**, **Sempre spento** o **Torna ad automatico** per restituirla alla programmazione del controller.
- Un valore impostato, come temperatura o pH, mostra il suo intervallo consentito e rifiuta un valore fuori da quello.

:::warning La modifica di una presa o di un valore impostato viene salvata sul controller stesso
Non viene salvata solo in Cora. Impostare una presa su Sempre acceso o Sempre spento scavalca la programmazione del controller per quella presa finché non scegli Torna ad automatico.
:::

Se una presa o un valore impostato sembra appartenere a un riscaldatore o a una pompa di risalita, Cora ti chiede di confermare due volte prima di inviarlo.

Se il contenitore di un dosatore sta finendo, Cora ti avvisa come fa per gli altri materiali di consumo. Il valore predefinito è pieno al 20%, e puoi cambiarlo dalla regola del dosatore nel [Centro avvisi](/help/mobile-alerts).

:::note ProfiLux mini
Un mini può solo accendere e spegnere le sue prese. Tutto il resto qui, come i valori impostati e la pausa alimentazione, richiede un ProfiLux 3, 4 o un Mitras.
:::

Se il controller rifiuta la modifica, controlla che la sua API GHL sia attiva con accesso completo. GHL la disattiva dopo ogni aggiornamento del firmware. [Risoluzione dei problemi](/help/troubleshooting) ha i passaggi.

## HYDROS {#hydros}

:::note Beta
**Beta.** HYDROS è in Beta ed è disponibile solo per gli utenti Beta. Se non sei un utente Beta non lo vedrai in **Aggiungi dispositivo**. Per chiedere l'accesso alla Beta, [contatta l'assistenza](/support.html). Alcune letture o alcuni comandi potrebbero non funzionare ancora, e quello che vedi qui potrebbe cambiare da un aggiornamento all'altro. Se qualcosa non funziona come descritto, faccelo sapere da [Segnalare un problema](/help/mobile-support). Di più in [Funzioni Beta](/help/mobile-beta).
:::

Quello che vedi qui dipende dalla chiave con cui hai collegato il controller. Una chiave **Read** ti dà solo i suoi ingressi. Una chiave **Write** aggiunge uscite, modalità, dosaggio e comandi del tester, più un banner nella pagina che ti ricorda che tipo di chiave stai usando.

Con una chiave di scrittura, anche i comandi restano spenti finché non attivi **Consenti il controllo da Cora (Beta)** nella pagina del dispositivo. È spento di default.

Quando è attivo, la pagina può mostrare:

- **Uscite**, come un interruttore per un'uscita acceso/spento, un cursore per un livello come una pompa o una luce, o un pulsante per un indicatore. Un'uscita scavalcata mostra **Sovrascritto** con un pulsante **Torna al programma** per restituirla al suo programma.
- **Modalità**, come Alimentazione o Cambio d'acqua, come una fila di scelte. Toccarne una ti chiede di confermare.
- **Teste di dosaggio**, ognuna con un pulsante **Dosa** e una voce **Impostazioni testa** dove imposti i suoi limiti: una dose manuale massima e un tetto giornaliero. Chiedere più del limite di una testa, o più di quanto resta del suo tetto giornaliero per la giornata, viene rifiutato con i numeri nel messaggio.
- **Comandi del tester**, per un iV o un Maven collegato, avviati da un pulsante e confermati prima.

Se il controller non si fa sentire da un po', la pagina lo dice e le letture potrebbero non essere aggiornate. Un comando inviato mentre sembra offline non viene inviato per niente, e la pagina ti dice anche questo.

## Focustronic {#focustronic}

:::note Beta
**Beta.** Focustronic è in Beta ed è disponibile solo per gli utenti Beta. Se non sei un utente Beta non lo vedrai in **Aggiungi dispositivo**. Per chiedere l'accesso alla Beta, [contatta l'assistenza](/support.html). Di più in [Funzioni Beta](/help/mobile-beta).
:::

Ogni dispositivo mostra il suo stato, il firmware, l'ultimo test e, per un Alkatronic, l'alcalinità e il pH che ha misurato. Vedi anche le pompe con quanto resta in ciascuna, i parametri, le fiale ed eventuali avvisi su reagente o tampone. Cora chiede a Focustronic nuove letture ogni 30 minuti.

In **Controlli** puoi usare **Misura ora**, **Dosa ora** da una pompa (fino a 500 mL alla volta) e, su un Mastertronic, **Testa ora**. Ognuno ti chiede prima di confermare. Cora non ripete mai una dose, quindi se il risultato dice che è sconosciuto, controlla il dispositivo. I comandi passano dai server di Focustronic, che Cora non controlla, e sono disponibili solo mentre il dispositivo è online.

## EcoTech, Inkbird e telecamere {#ecotech-inkbird-cameras}

:::note Beta
**Beta.** EcoTech, Inkbird e le telecamere sono in Beta e sono disponibili solo per gli utenti Beta. Se non sei un utente Beta non li vedrai in **Aggiungi dispositivo**. Per chiedere l'accesso alla Beta, [contatta l'assistenza](/support.html).
:::

Hanno le loro pagine:

- Luci EcoTech Radion, pompe VorTech e dosatori Versa: [Luci, pompe e dosatori EcoTech](/help/mobile-ecotech)
- I monitor dell'aria della stanza Inkbird riportano solo letture, quindi non c'è niente da comandare: [Collegare la tua attrezzatura](/help/mobile-connections#inkbird-room-air-monitor)
- Telecamere e Controllo schiumatoio: [Telecamere e Controllo schiumatoio](/help/mobile-cameras)

## Cosa succede dopo che hai cambiato qualcosa {#what-happens-after-you-change-something}

Ogni modifica viene registrata in [Attività](/help/mobile-activity), con la superficie da cui è arrivata. Se un dispositivo non accetta una modifica, anche questo viene registrato lì.
