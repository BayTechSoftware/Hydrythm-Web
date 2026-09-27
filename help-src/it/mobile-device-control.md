---
title: Controllare la tua attrezzatura
description: Apri la pagina di un dispositivo per vederne lo stato in tempo reale e comandarlo: prese, pompe, teste di dosaggio e tester.
section: Cora Mobile
reviewed: 2026-09-27
order: 11
group: Equipment
---

Ogni apparecchio collegato ha una sua pagina in Cora, con lo stato in tempo reale e i comandi che quel dispositivo supporta. Le pagine si aprono dalla scheda **Dispositivi**.

![La pagina di un dispositivo](img/mobile-device-detail.webp "Letture in tempo reale in alto, poi i controlli che quel dispositivo supporta.")

Tutte le pagine hanno la stessa struttura: in alto il nome del dispositivo, poi una riga di letture in tempo reale, lo stato che il dispositivo riporta e infine i comandi. Con la campanella nella barra del titolo imposti le soglie di avviso del dispositivo, come spiegato in [Materiali di consumo](/help/mobile-consumables).

:::warning Questi comandi agiscono sull'attrezzatura vera
Non c'è anteprima e non si può annullare. Alcuni comandi chiedono anche una conferma.
:::

## Cosa succede quando invii un comando

Un comando non va sempre a buon fine. Cora non tira a indovinare e ti dice quale di questi quattro esiti c'è stato:

| Esito | Significato |
|---|---|
| **Confermato** | L'attrezzatura ha accettato la modifica e ha riportato il nuovo stato |
| **Non confermato** | Il comando è partito ma non è tornata nessuna risposta. **Vuol dire "non lo sappiamo", non "ha funzionato"**. Controlla lo stato sul dispositivo |
| **Rifiutato** | Qualcosa l'ha bloccato (una regola di sicurezza, un blocco o l'attrezzatura stessa), oppure nessun dispositivo Cora l'ha preso in carico in tempo. Il comando è stato annullato e non è partito nulla |
| **Nessun cambiamento** | L'attrezzatura era già nello stato che avevi chiesto |

Ogni esito viene registrato in [Attività](/help/mobile-activity) insieme alla sua origine.

## Neptune Apex

La pagina dell'Apex elenca sonde e prese.

- Le **sonde** diventano fonti in Cora e puoi metterle sulla dashboard.
- Le **prese** passano da **Auto** a **Disattivata** a **On**. Con Auto il controllo torna alla programmazione dell'Apex.
- I **moduli installati** (Trident, DŌS e altri) hanno ciascuno la sua pagina.

## Trident

Mostra lo stato del test in corso e il livello di reagenti e acqua di scarico. Da qui puoi anche avviare un test.

Puoi impostare una soglia di avviso sui test rimasti, così Cora ti avvisa prima che finisca il reagente. Altri dettagli in [Materiali di consumo](/help/mobile-consumables).

## DŌS

Un DŌS QD funziona esattamente come un DŌS e tutto quello che trovi qui vale per entrambi. Quando un Cora Max legge il tuo Apex, le teste di dosaggio compaiono nella pagina DŌS e mai nell'elenco delle prese.

Ogni testa mostra cosa sta dosando, il suo programma, quanto ha dosato oggi, quanto resta nel contenitore e la sua **autonomia**, cioè per quanti giorni basterà al ritmo attuale.

Per ogni testa puoi:

- **Sospendere** e **Riprendere** il programma
- **Riempi**: dire a Cora che il contenitore è di nuovo pieno, o indicare quanto contiene
- **Dosa ora**: fare un dosaggio manuale di una quantità precisa

:::note I programmi si modificano in Apex Fusion
Cora mostra il programma e tiene il conto di quanto è stato dosato, ma non lo modifica. Programma, ritmo di dosaggio e numero di dosi si cambiano nell'app Apex Fusion. Qui puoi sospendere, riempire e dosare a mano.
:::

:::note Misura la testa prima di dosare a mano
Cora non fa dosaggi a mano con una testa che non è stata misurata. **Misura per dosare** e **Rimisura** si trovano sul Cora Max che gestisce il dosaggio della vasca. Cora fa girare la testa per venti secondi, tu misuri quanto liquido è uscito e Cora calcola la portata reale. Una misura vale per tutti i Cora Max e Cora Mobile. Misura quindi ogni testa una volta, e poi di nuovo quando cambi il tubo.
:::

:::warning Un DŌS continua a dosare anche con il contenitore vuoto
L'unità non ha un sensore di livello e non si ferma da sola. Imposta un avviso di rifornimento dalla pagina della testa, così Cora ti avvisa prima che il contenitore si svuoti.
:::

### A cosa serve ogni testa

Ogni testa ha un **tipo di uso**, così Cora sa cosa fa e ne parla nel modo giusto: **Integratore**, **Cambio d'acqua: acqua salata nuova in entrata**, **Cambio d'acqua: acqua vecchia in uscita**, **Acqua di calce**, **Reattore di calcio**, **Cibo**, **Rabbocco** oppure **Altro**. Lo imposti in **Usata per** nelle impostazioni della testa.

I due tipi per il cambio d'acqua vanno **abbinati**. Nella **Testa abbinata** di una testa scegli l'altra, quella che sposta l'acqua nella direzione opposta. Così Cora le tratta come una coppia per il cambio d'acqua e non come due teste separate.

Ogni testa ha anche un limite di **Dose massima manuale**, per evitare che un errore di battitura faccia partire una dose molto più grande del previsto. Le dosi manuali grandi si sbloccano solo dopo che la portata della testa è stata misurata con un test vero sulla vasca.

## Red Sea ReefBeat

Ogni unità ha una pagina fatta su misura:

| Unità | Cosa mostra la pagina | Cosa puoi fare |
|---|---|---|
| **ReefDose** | Ogni testa, il suo contenitore e quanto ha dosato | Per ogni testa: **Dose al giorno**, **Rimanente nella bottiglia**, **Dosa ora** e **Attiva programma**. Avvisi di rifornimento per ogni testa |
| **ReefATO+** | Livello del serbatoio e rabbocchi | Impostare un avviso sul serbatoio |
| **ReefMat** | Rotolo rimasto, in giorni e metri | Far avanzare il rotolo, impostare un avviso di rifornimento |
| **ReefRun** | Velocità e stato della pompa di risalita e di quella dello schiumatoio | Cambiare velocità, accendere o spegnere una pompa, regolare lo schiumatoio |

**ReefRun comanda la pompa di risalita e quella dello schiumatoio.** Non è una pompa di movimento.

Un'unità può fermarsi da sola, per esempio una pompa ReefRun quando si riempie il bicchiere dello schiumatoio. In quel caso la pagina ti dice perché e ti propone la soluzione:

| Unità | La pagina dice | Tocca |
|---|---|---|
| ReefRun | Quale pompa si è fermata e perché, per esempio *Coppa piena. Vuotala, poi riprendi.* | **Riprendi** |
| ReefRun o ReefMat | **Arresto di emergenza** | **Elimina emergenza** |
| ReefMat | **Tappetino inceppato**, **Errore di installazione** o **Errore di configurazione** | **Riprendi** |
| ReefMat | *Carica un nuovo rotolo, poi confermalo nell'app di Red Sea.* | **Ho già caricato un nuovo rotolo** |
| ReefMat | **Il sensore ha bisogno di essere pulito** | **Sensore pulito** |
| ReefDose | **Guasto della testa**, con il nome della testa | **Ripristina** |
| ReefATO+ | **Elimina guasto** | **Riprendi** |

Alcuni di questi comandi chiedono una conferma. Se non sei sulla rete dell'unità, Cora Mobile li invia attraverso un Cora Max della vasca. Se nessun Cora Max può farlo, la pagina te lo dice e non parte nulla.

## Pompe Jecod

La pagina della pompa mostra modalità e intensità attuali, e puoi cambiarle tutte e due.

Puoi anche:

- **Copia programma su…**: copiare il programma di questa pompa su un'altra
- **Salva programma come…** e **Programmi salvati…**: salvare un programma e riapplicarlo in seguito
- **Condividi questo programma** e **Incolla un codice programma…**: passare un programma da un impianto all'altro con un codice breve

## Maxspect

:::note Il supporto Maxspect è in beta
Il supporto per le gyre Maxspect è ancora in fase di test e sviluppo. Alcuni comandi potrebbero essere limitati e quello che vedi potrebbe cambiare da un aggiornamento all'altro. Se qualcosa non funziona come descritto, scrivici da [Ottenere assistenza](/help/mobile-support).
:::

La pagina della gyre mostra se è in funzione, schema d'onda e velocità di **Gyre A** e **Gyre B**, e l'ora dell'ultima lettura. Da qui puoi:

- Accendere o spegnere la gyre con l'interruttore accanto al suo stato. Cora ti chiede prima una conferma. Se la spegni, si fermano tutte e due le gyre e il programma resta com'è.
- Toccare **Modifica impostazioni** per scegliere schema d'onda e velocità di ogni gyre (e la durata, se lo schema ne ha una) e decidere se le due gyre lavorano collegate. Cora elenca cosa cambierà e ti chiede di confermare prima di applicare. L'alternanza si imposta nell'app Maxspect. Una gyre in alternanza mantiene rampe e tempi di mantenimento.
- Toccare **Imposta programma** quando il programma salvato sulla gyre non si riesce a leggere. Imposta entrambe le gyre, così la gyre può ripartire.
- Vedere il programma giornaliero della gyre nella scheda **Programma**. È in sola lettura: il programma si imposta nell'app Maxspect.
- Controllare **Stato pompa**: quando andrà pulita la prossima volta (il conto alla rovescia lo fa la pompa stessa), la corrente assorbita dalla testa A, quali teste sono installate e il firmware. Tocca **Leggi** per aggiornare questi dati.

:::note Come Cora Mobile raggiunge una gyre
Se la vasca ha un Cora Max, Cora Mobile passa da quel Cora Max, anche quando sei fuori casa, e **Modifica impostazioni** parte dall'ultima lettura del Cora Max. Altrimenti il telefono parla direttamente con la gyre e deve essere sulla sua rete. In questo caso, quando apri la pagina Cora legge la gyre. Se la pagina mostra invece una lettura salvata più vecchia, **Modifica impostazioni** resta nascosto finché non tocchi aggiorna.
:::

## Dopo una modifica

Ogni modifica viene registrata in [Attività](/help/mobile-activity) insieme alla superficie da cui è partita. Se un dispositivo non accetta la modifica, anche questo viene registrato lì.
