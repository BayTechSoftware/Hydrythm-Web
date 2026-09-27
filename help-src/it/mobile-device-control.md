---
title: Controllare il tuo equipaggiamento
description: Apri la pagina di un dispositivo per vedere il suo stato in tempo reale e guidarlo: prese, pompe, teste di dosaggio e tester.
section: Cora Mobile
reviewed: 2026-09-27
order: 11
group: Equipment
---

L'equipaggiamento collegato ha la propria pagina in Cora, che mostra lo stato in tempo reale e offre qualunque controllo quel dispositivo supporti. Aprine uno dalla scheda **Dispositivi**.

![La pagina di un dispositivo](img/mobile-device-detail.webp "Letture in tempo reale in alto, poi i controlli che quel dispositivo supporta.")

Ogni pagina di dispositivo segue la stessa forma: identificazione in alto, una riga di letture in tempo reale, qualsiasi stato riportato dal dispositivo, poi i suoi controlli. La campana nella barra del titolo imposta le soglie di avviso per quel dispositivo; vedi [Materiali di consumo](/help/mobile-consumables).

:::warning Questi controlli agiscono su equipaggiamento reale
Non c'è anteprima né annullamento. Alcuni controlli richiedono anche una conferma prima.
:::

## Cosa succede quando invii un comando

Un comando non ha sempre successo, e Cora ti dice quale delle quattro cose è successa invece di supporre:

| Esito | Significa |
|---|---|
| **Confermato** | L'equipaggiamento ha confermato la modifica e riportato il suo nuovo stato |
| **Non confermato** | Il comando è stato inviato, ma non è arrivata nessuna risposta. **Questo significa "non lo sappiamo", non "ha funzionato"**; controlla lo stato del dispositivo stesso |
| **Rifiutato** | Qualcosa lo ha rifiutato (una regola di sicurezza, un blocco, o l'equipaggiamento stesso), oppure nessun dispositivo Cora lo ha raccolto in tempo, quindi è stato annullato e non è stato eseguito nulla |
| **Nessun cambiamento** | L'equipaggiamento era già nello stato che avevi chiesto |

Ogni esito viene registrato in [Attività](/help/mobile-activity) insieme a ciò che lo ha causato.

## Neptune Apex

La pagina dell'Apex elenca le tue sonde e prese.

- Le **sonde** riportano a Cora come fonti e possono essere messe su una dashboard.
- Le **prese** commutano tra **Auto**, **Disattivata** e **On**. Auto restituisce il controllo alla programmazione del tuo Apex.
- I **moduli montati** (Trident, DŌS e altri) hanno ciascuno la propria pagina.

## Trident

Mostra lo stato attuale del test, i livelli rimanenti di reagente e acqua di scarico, e ti permette di avviare un test.

Puoi impostare una soglia di avviso per i test rimanenti da questa pagina, così Cora ti avvisa prima che il reagente finisca. Vedi [Materiali di consumo](/help/mobile-consumables).

## DŌS

Un DŌS QD funziona esattamente come un DŌS, e tutto quanto qui si applica a entrambi. Quando un Cora Max legge il tuo Apex, le teste di dosaggio appaiono nella pagina DŌS, mai nell'elenco delle prese.

Ogni testa di dosaggio mostra cosa sta dosando, il suo programma, cosa ha dosato oggi, quanto resta nel contenitore e la sua **autonomia**: quanti giorni durerà al ritmo attuale.

Per testa puoi:

- **Sospendere** e **Riprendere** il suo programma
- **Riempi**: dire a Cora che il contenitore è di nuovo pieno, o impostare il volume che contiene
- **Dosa ora**: un dosaggio manuale misurato

:::note I programmi si modificano in Apex Fusion, non qui
Cora mostra il programma e traccia cosa è stato dosato, ma non lo cambia. Modificare il programma, il ritmo di dosaggio o il numero di dosi si fa nell'app Apex Fusion. Sospendere, riempire e dosare a mano sono tutti supportati qui.
:::

:::note Misura una testa prima di dosarla a mano
Cora non doserà una testa a mano finché non è stata misurata. **Misura per dosare** e **Rimisura** si trovano sul Cora Max che dosa per la vasca: Cora fa funzionare la testa per venti secondi, tu misuri cosa è uscito, e Cora calcola il ritmo reale della testa. Una sola misurazione serve a ogni Cora Max e Cora Mobile, quindi misura ogni testa una volta, e di nuovo dopo aver cambiato il suo tubo.
:::

:::warning Un DŌS continua a dosare quando il suo contenitore è vuoto
L'unità non ha un sensore di livello e non si ferma da sola. Imposta un avviso di rifornimento dalla pagina della testa così Cora ti avvisa prima che il contenitore si esaurisca.
:::

### A cosa serve ogni testa

Ogni testa è impostata su un **tipo di uso**, così Cora sa cosa fa e può parlarne correttamente: **Integratore**, **Cambio d'acqua: acqua salata nuova in entrata**, **Cambio d'acqua: acqua vecchia in uscita**, **Acqua di calce**, **Reattore di calcio**, **Cibo**, **Rabbocco**, oppure **Altro**. Impostalo sotto **Usata per** nelle impostazioni della testa.

I due tipi di uso per cambio d'acqua sono pensati per essere **abbinati**: imposta la **Testa abbinata** di una testa sull'altra testa che muove l'acqua nella direzione opposta, e Cora le tratterà come una coppia di cambio d'acqua invece che come due teste non collegate.

Ogni testa ha anche un limite di **Dose massima manuale**, per impedire che un dosaggio manuale digitato per errore sia molto più grande del previsto. I dosaggi manuali grandi diventano disponibili solo dopo che il ritmo della testa è stato misurato rispetto a un test reale sulla vasca.

## Red Sea ReefBeat

Ogni unità ha una pagina adatta a ciò che è:

| Unità | La pagina mostra | Puoi |
|---|---|---|
| **ReefDose** | Ogni testa, il suo contenitore e cosa ha dosato | Per ogni testa: **Dose al giorno**, **Rimanente nella bottiglia**, **Dosa ora** e **Attiva programma**. Imposta avvisi di rifornimento per testa |
| **ReefATO+** | Livello del serbatoio e attività di rabbocco | Imposta un avviso per il serbatoio |
| **ReefMat** | Rotolo rimanente, in giorni e metri | Avanza il rotolo, imposta un avviso di rifornimento |
| **ReefRun** | Velocità e stato della pompa di ritorno e dello skimmer | Cambia la velocità, commuta una pompa, correggi le impostazioni dello skimmer |

**ReefRun è un controller per pompa di ritorno e skimmer**, non una pompa di movimento.

Un'unità può fermarsi da sola, per esempio una pompa ReefRun quando la coppa dello skimmer si riempie. Quando succede, la sua pagina dice perché e offre la soluzione:

| Unità | La pagina dice | Tocca |
|---|---|---|
| ReefRun | Quale pompa si è fermata e perché, per esempio *Coppa piena. Vuotala, poi riprendi.* | **Riprendi** |
| ReefRun o ReefMat | **Arresto di emergenza** | **Elimina emergenza** |
| ReefMat | **Tappetino inceppato**, **Errore di installazione** o **Errore di configurazione** | **Riprendi** |
| ReefMat | *Carica un nuovo rotolo, poi confermalo nell'app di Red Sea.* | **Ho già caricato un nuovo rotolo** |
| ReefMat | **Il sensore ha bisogno di essere pulito** | **Sensore pulito** |
| ReefDose | **Guasto della testa**, con il nome della testa | **Ripristina** |
| ReefATO+ | **Elimina guasto** | **Riprendi** |

Alcuni di questi richiedono una conferma prima. Lontano dalla rete dell'unità, Cora Mobile li invia tramite un Cora Max sulla vasca; se nessun Cora Max può farlo, la pagina lo dice e non viene inviato nulla.

## Pompe Jecod

La pagina della pompa mostra la sua modalità e intensità attuali, e ti permette di cambiare entrambe.

Puoi anche:

- **Copia programma su…**: metti il programma di questa pompa su un'altra
- **Salva programma come…** e **Programmi salvati…**: conserva un programma e riapplicalo più avanti
- **Condividi questo programma** e **Incolla un codice programma…**: sposta un programma tra sistemi come un breve codice

## Maxspect

:::note Il supporto Maxspect è in beta
Il supporto della gyre Maxspect è ancora in fase di test e sviluppo, quindi alcuni controlli potrebbero essere limitati, e ciò che vedi qui potrebbe cambiare tra un aggiornamento e l'altro. Se qualcosa non funziona come descritto, faccelo sapere da [Ottenere assistenza](/help/mobile-support).
:::

La pagina della gyre mostra se la gyre è in funzione, lo schema d'onda e la velocità di **Gyre A** e **Gyre B**, e quando è stata letta l'ultima volta. Da qui puoi:

- Accendere o spegnere la gyre con l'interruttore accanto al suo stato. Cora ti chiede prima di confermare. Spegnerla ferma entrambe le gyre e lascia il programma com'è.
- Toccare **Modifica impostazioni** per impostare lo schema d'onda e la velocità della pompa di ogni gyre (e la durata, per uno schema che ne ha una), e se le due gyre sono collegate. Cora elenca cosa cambierà e ti chiede di confermare prima di applicarlo. L'alternanza si imposta nell'app Maxspect: una gyre che la esegue mantiene le sue rampe e i suoi tempi di mantenimento.
- Toccare **Imposta programma** invece quando il programma salvato sulla gyre non può essere letto. Imposta entrambe le gyre così la gyre può ripartire.
- Vedere il programma giornaliero della gyre sulla scheda **Programma**. È di sola visualizzazione: imposta il programma nell'app Maxspect.
- Controllare **Stato pompa**: quando la pompa avrà bisogno di essere pulita la prossima volta (la pompa fa da sola il conto alla rovescia), la corrente assorbita dalla testa A, quali teste sono montate, e il firmware. Tocca **Leggi** per recuperarlo.

:::note Come Cora Mobile raggiunge una gyre
Quando un Cora Max serve la vasca, Cora Mobile lavora attraverso quel Cora Max, anche quando sei lontano da casa, e **Modifica impostazioni** parte dall'ultima lettura di quel Cora Max. Altrimenti il tuo telefono parla direttamente con la gyre e deve essere sulla rete della gyre. Aprire la pagina la legge quindi; se la pagina mostra invece una lettura memorizzata più vecchia, **Modifica impostazioni** resta nascosto finché non tocchi aggiorna.
:::

## Cosa succede dopo aver cambiato qualcosa

Ogni modifica viene registrata in [Attività](/help/mobile-activity) insieme alla superficie che l'ha richiesta. Se un dispositivo non accetta una modifica, anche il fallimento viene registrato lì.
