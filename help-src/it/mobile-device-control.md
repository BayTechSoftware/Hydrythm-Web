---
title: Controllare la tua attrezzatura
description: Apri la pagina di un dispositivo per vederne lo stato in tempo reale e comandare prese, pompe, teste di dosaggio e tester, marca per marca.
section: Cora Mobile
reviewed: 2026-10-18
order: 13
group: Equipment
twin: max-device-control
---

Usa la pagina di un dispositivo per vederne lo stato in tempo reale e cambiare quello che sta facendo. Aprila da **Dispositivi** → tocca il dispositivo, oppure tocca il suo riquadro sulla dashboard.

![La pagina di un ReefATO+ in Cora Mobile](img/mobile-device-detail.webp "Lo stato, le letture di oggi e il livello dell'acqua, poi perdite, rabbocchi e calibrazione della sonda.")

Ogni pagina dispositivo è organizzata allo stesso modo. Nome e dettagli sono in alto, poi una fila di letture in tempo reale, gli stati che il dispositivo riporta e i suoi comandi. La campanella nella barra del titolo imposta le soglie di avviso per quel dispositivo, come descritto in [Materiali di consumo](/help/mobile-consumables). Come aggiungere un dispositivo all'inizio è spiegato in [Collegare la tua attrezzatura](/help/mobile-connections).

Vai alla tua attrezzatura: [Neptune Apex](#neptune-apex) · [Trident](#trident) · [DŌS](#dos) · [Red Sea](#red-sea) · [ReefDose](#reefdose) · [ReefRun](#reefrun) · [ReefMat](#reefmat) · [ReefATO+](#reefato) · [Avvisi della pompa dosometrica](#doser-alerts) · [Jecod](#jecod) · [AquaWiz](#aquawiz)

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

Ogni testa di dosaggio mostra cosa sta dosando, la sua programmazione, quanto ha dosato oggi e quanto resta nel contenitore. Mostra anche l'**autonomia**, cioè quanti giorni durerà al ritmo attuale.

Se il DŌS smette di rispondere sull'AquaBus, la sua pagina mostra **Fuori bus** e una scheda **Richiede attenzione**. I valori sulla pagina sono allora gli ultimi riportati, non quello che sta facendo adesso. Controlla il cavo AquaBus del modulo e l'Apex.

Per ogni testa puoi:

- **Sospendi** e **Riprendi** la sua programmazione
- **Riempi**, per dire a Cora che il contenitore è di nuovo pieno o impostare quanto ne contiene (**Volume totale** è la dimensione del contenitore, **Volume rimanente** è quanto c'è adesso, e **Pieno** imposta l'uno uguale all'altro)
- **Dosa ora**, per una dose misurata a mano

:::note Modifica le programmazioni in Apex Fusion
Cora mostra la programmazione e tiene traccia di quanto è stato dosato, ma non cambia la programmazione. Programmazione, velocità di dosaggio e numero di dosi si modificano nell'app Apex Fusion. Sospendere, riempire e dosare a mano funzionano qui.
:::

:::note Misura una testa prima di dosare a mano
Cora non dosa a mano da una testa finché la testa non è stata misurata. **Misura per dosare** e **Rimisura** sono sul Cora Max che dosa per la vasca. Cora fa funzionare la testa per venti secondi, tu misuri quanto è uscito e Cora calcola la velocità reale della testa. Una misura vale per ogni Cora Max e per Cora Mobile. Misura ogni testa una volta, e di nuovo dopo aver cambiato il tubo.
:::

:::warning Un DŌS continua a dosare quando il contenitore è vuoto
L'unità non ha un sensore di livello e non si ferma da sola. Imposta un avviso di rifornimento per ogni testa in **Avvisi** nella pagina del DŌS, così Cora ti avvisa prima che il contenitore resti a secco. Vedi [Avvisi della pompa dosometrica](#doser-alerts).
:::

### A cosa serve ogni testa {#dos-head-use}

Dai a ogni testa un **tipo di uso** così Cora sa cosa fa e ne parla correttamente. Le scelte sono **Integratore**, **Cambio d'acqua: nuova acqua salata in entrata**, **Cambio d'acqua: acqua vecchia in uscita**, **Kalkwasser**, **Reattore di calcio**, **Alimento**, **Rabbocco** e **Altro**. Impostalo in **Usata per** nelle impostazioni della testa.

I due tipi di uso del cambio d'acqua vanno in **coppia**. Imposta la **Testa abbinata** di una testa sulla testa che sposta l'acqua nel verso opposto, e Cora tratta le due come un'unica coppia per il cambio d'acqua.

Un contenitore può arrivare a 1.000 L, per ogni tipo di uso. L'Apex da solo conta solo fino a 150 L, quindi oltre quel valore Cora segue il contenitore da sé in base a quanto dosa la testa. Inserisci il **Volume totale** quando lo configuri. Cora inoltre ogni tanto azzera il contatore interno dell'Apex, e Attività lo mostra come *Contatore interno dell'Apex reimpostato a 150 L*.

Ogni testa ha anche un limite **Dose massima manuale**, così un errore di battitura non può trasformare una dose manuale in qualcosa di molto più grande di quello che volevi. Le dosi manuali grandi diventano disponibili solo dopo che la velocità della testa è stata misurata con un test reale alla vasca, e dopo che hai attivato **Dosi grandi** nelle impostazioni della testa. È spento di default. Attivalo solo dopo aver guardato la prima dose grande eseguita alla vasca.

## Red Sea ReefBeat {#red-sea}

Ogni unità Red Sea ha una pagina adatta a quello che fa:

| Unità | La pagina mostra | Puoi |
|---|---|---|
| [ReefDose](#reefdose) | Ogni testa, il suo contenitore e quanto ha dosato | Dosare, cambiare la dose giornaliera, modificare il **Piano di dosaggio** |
| [ReefRun](#reefrun) | Velocità e stato delle pompe di risalita e dello schiumatoio | Cambiare la velocità, accendere o spegnere una pompa |
| [ReefMat](#reefmat) | Il rotolo rimanente, in giorni e metri | Far avanzare il tappetino, impostare **Impostazioni ReefMat**, registrare un rotolo nuovo |
| [ReefATO+](#reefato) | Livello del serbatoio e attività di rabbocco | Impostare un avviso per il serbatoio |



Quando sei lontano dalla rete dell'unità, Cora Mobile invia i comandi Red Sea tramite un Cora Max nella vasca. Se nessun Cora Max può farlo, la pagina lo dice e non viene inviato niente.

## ReefDose {#reefdose}

![La pagina di un ReefDose 4 in Cora Mobile](img/mobile-reefdose.webp "Lo stato, le teste e il totale di oggi, Usa la pompa dosometrica per i consumi, poi ogni testa di dosaggio.")

Per ogni testa puoi impostare **Dose al giorno** e **Rimanente nella bottiglia**, usare **Dosa ora** e **Attiva programmazione**. Gli avvisi di rifornimento si impostano per testa con la campanella, come descritto in [Avvisi della pompa dosometrica](#doser-alerts).

La sezione **Dosaggio** mostra le **Prossime dosi**, quanto ha dosato oggi ogni testa (**Dosato oggi finora**) e **Dosato per testa** negli **Ultimi 7 giorni** o in **Totale**. Cora legge questi dati mentre un Cora Max o il tuo telefono è sulla rete di casa.

### Modificare un piano di dosaggio {#reefdose-plan}

Tocca l'icona del calendario nella pagina di un ReefDose per aprire il **Piano di dosaggio**.

Un piano è un totale giornaliero, diviso in un massimo di quattro fasce orarie. Ogni fascia ha un'ora di inizio e di fine, quante dosi deve fare e una velocità: **Silenzioso**, **Normale** o **Rapido**. Aggiungi e togli le fasce, poi salva. Cora ti mostra cosa stai per inviare e ti chiede di confermare prima di sostituire tutto il piano della testa.

L'editor legge prima il piano che c'è già sull'unità, quindi stai modificando quello vero, non un modulo vuoto.

## ReefRun {#reefrun}

ReefRun comanda le pompe di risalita e dello schiumatoio. Non è una pompa di movimento. Puoi cambiare la velocità di una pompa, accenderla o spegnerla e regolare le impostazioni dello schiumatoio.


## ReefMat {#reefmat}

La pagina del ReefMat mostra quanto rotolo resta, in giorni e metri. Tocca **Avanza ora** per far avanzare il tappetino a mano. Cora chiede prima **Avanzare il tappetino ora?** Puoi anche impostare un avviso di rifornimento per il rotolo.

Tocca l'ingranaggio per **Impostazioni ReefMat**:

- **Avanzamento programmato** attiva un avanzamento a orari fissi, separato dal sensore di avanzamento automatico già presente nella pagina. Attivalo e imposta ogni quanto, e di quanto ogni avanzamento sposta il tappetino.
- **Modello ReefMat** e **Posizione motore** (**Sinistra** o **Destra**) dicono a Cora quale unità e quale orientamento hai.

Dopo aver caricato un rotolo nuovo, dillo a Cora con **Nuovo rotolo**: il suo spessore, e il diametro esterno se lo conosci. **Avanza ora** fa solo avanzare il tappetino che hai già caricato.

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

## Avvisi della pompa dosometrica {#doser-alerts}

Un DŌS e un ReefDose tengono i loro avvisi nella loro pagina. La scheda **Regole** del [Centro avvisi](/help/mobile-alerts) ha una riga per pompa dosometrica che la apre, e anche il pulsante **Apri pompa dosometrica** di un avviso della pompa dosometrica ti porta qui.

Nella pagina di un DŌS, tocca la scheda **Avvisi** (o la campanella nella barra del titolo). Il pannello elenca ogni testa, e per ognuna puoi impostare:

- *[testa] · giorni rimanenti*, per esempio *Iodio · giorni rimanenti*: ricevi un avviso sotto questo numero di giorni di scorta
- *[testa] · rimanente*: ricevi un avviso sotto questa quantità rimasta nel contenitore
- **Spazio rimanente nel contenitore dei rifiuti**, per una testa che toglie l'acqua vecchia: ricevi un avviso quando il contenitore dei rifiuti si sta riempiendo
- **Avvisi di dose mancata**: un interruttore che ti avvisa quando la testa salta una dose programmata

Ogni soglia ha il suo interruttore, così puoi spegnerne una e tenerne il valore. Tocca **Salva** quando hai finito.

Nella pagina di un ReefDose, tocca la campanella nella barra del titolo. Ogni testa ha la sua soglia di giorni rimanenti e il suo interruttore.

I valori predefiniti e gli altri materiali di consumo sono in [Materiali di consumo](/help/mobile-consumables).

## Pompe Jecod / Jebao {#jecod}

La pagina della pompa mostra lo schema d'onda attuale (modalità) e l'intensità, e puoi cambiarli entrambi. Il suo stato è nella riga del titolo, accanto al nome della pompa. Un selettore con **Uguale tutto il giorno** e **Programmazione** segna quello in corso con *· in corso*, e la pagina si apre su di esso. Creare una programmazione giornaliera, e copiarla, salvarla o condividerla, è spiegato in [Programmare l'attrezzatura](/help/mobile-schedules).

Se la pompa fa parte di un gruppo, la pagina mostra il suo ruolo, come **Guida il gruppo**, **Segue: in sincrono** o **Segue: alternata**.

### Pausa per l'alimentazione {#jecod-feeding}

Avvia una pausa per l'alimentazione da **Alimentazione** nella pagina della pompa: tocca **5**, **10**, **15** o **30** min. Alcune pompe terminano la pausa da sole, e la pagina dice *La pompa termina questa fase da sola.*

:::warning Tieni aperta la pagina della pompa durante una pausa per l'alimentazione
Alcune pompe non terminano da sole un'alimentazione, e la pagina lo dice. Per queste, e per qualsiasi pompa con una programmazione, Cora Mobile ripristina lo schema d'onda e la programmazione solo finché la pagina della pompa resta aperta. Se lasci la pagina, la pompa resta ferma in modalità alimentazione, o resta fuori dalla sua programmazione, finché non la cambi di nuovo o tocchi **Programmazione**.
:::

Se la tua casa ha un Cora Max, è lui a concludere l'alimentazione e a riportare la pompa al suo programma allo scadere del tempo, anche con Cora Mobile chiuso. L'avviso qui sopra vale quindi solo quando non c'è un Cora Max.

Una pompa Bluetooth deve essere a portata del telefono per avviare un'alimentazione, e una pompa di rete deve essere sulla tua rete.

### Controlli guasti {#jecod-fault-checks}

**Controlli guasti** imposta ogni quanto Cora rilegge la pompa per poterti avvisare di un guasto, come una pompa bloccata o una che gira a secco. Se lo spegni, quegli avvisi si fermano per quella pompa. I controlli guasti richiedono un Cora Max nella vasca. La tua scelta viene salvata e i controlli partono quando ne aggiungi uno. **Usa questo per ogni pompa su questa vasca** copia l'impostazione su tutte.

## AquaWiz {#aquawiz}

La scheda AquaWiz mostra le tue letture di alcalinità, e il pH se la tua unità lo riporta. Mostra anche il tuo KH obiettivo, la concentrazione della dose e, per un'unità con il dosaggio configurato, la dose massima oraria e quanto integratore di alcalinità resta nel contenitore. Questi valori arrivano direttamente dalle tue impostazioni AquaWiz, quindi cambiali nell'app AquaWiz. Cora non può comandare un AquaWiz.

Sotto le letture la scheda dice quando è stata misurata l'ultima (per esempio *Misurato 14:00*) e da dove viene: **Ogni ora dal tuo Cora Max** oppure **Dal cloud AquaWiz, ogni 12 ore**. Mostra anche la **variazione del pH**. Aprire la pagina chiede una lettura fresca, e **Leggi ora** la chiede di nuovo, al massimo una volta ogni 15 minuti. Se una lettura non è cambiata è normale: l'unità misura solo ogni tanto.

Quando un Cora Max legge l'unità ogni ora, la scheda mostra anche pompa, sonda del pH e livello della vaschetta, e Cora ti avvisa quando la pompa segnala un guasto, la sonda del pH si è guastata o sta per finire la sua vita, oppure il livello della vaschetta resta basso o alto per oltre un'ora.

Se la tua unità segue il suo contenitore, Cora ti avvisa quando l'integratore sta finendo, a 100 mL di default. Cambialo dalla sua regola nel [Centro avvisi](/help/mobile-alerts).


## Cosa succede dopo che hai cambiato qualcosa {#what-happens-after-you-change-something}

Ogni modifica viene registrata in [Attività](/help/mobile-activity), con la superficie da cui è arrivata. Se un dispositivo non accetta una modifica, anche questo viene registrato lì.
