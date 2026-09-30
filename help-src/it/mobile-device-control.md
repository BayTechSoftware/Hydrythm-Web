---
title: Controllare la tua attrezzatura
description: Apri la pagina di un dispositivo per vederne lo stato in tempo reale e comandarlo: prese, pompe, teste di dosaggio e tester.
section: Cora Mobile
reviewed: 2026-09-30
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

Ogni testa ha anche un limite di **Dose massima manuale**, per evitare che un errore di battitura faccia partire una dose molto più grande del previsto. Le dosi manuali grandi si sbloccano solo dopo che la portata della testa è stata misurata con un test vero sulla vasca, e dopo che attivi **Dosi grandi (Beta)** nelle impostazioni della testa. È disattivato per impostazione predefinita: attivalo solo dopo aver osservato la prima dose grande eseguita davanti all'acquario.

## Red Sea ReefBeat

Ogni unità ha una pagina fatta su misura:

| Unità | Cosa mostra la pagina | Cosa puoi fare |
|---|---|---|
| **ReefDose** | Ogni testa, il suo contenitore e quanto ha dosato | Per ogni testa: **Dose al giorno**, **Rimanente nella bottiglia**, **Dosa ora** e **Attiva programma**, più un editor completo del **Piano di dosaggio** *(beta)*. Avvisi di rifornimento per ogni testa |
| **ReefATO+** | Livello del serbatoio e rabbocchi | Impostare un avviso sul serbatoio. Chiedi all'Assistente quanti giorni restano al serbatoio |
| **ReefMat** | Rotolo rimasto, in giorni e metri | Far avanzare il rotolo, impostare un avviso di rifornimento e, in beta, attivare un avanzamento programmato, impostare modello e posizione del motore, e registrare un nuovo rotolo |
| **ReefRun** | Velocità e stato della pompa di risalita e di quella dello schiumatoio | Cambiare velocità, accendere o spegnere una pompa, regolare lo schiumatoio e modificare un **programma di velocità** completo *(beta)* |
| **ReefControl** *(beta)* | Le sue sonde di temperatura, pH, salinità e ORP | Vedere le letture |
| **ReefWave**, **ReefLED** *(beta)* | La modalità attuale | Solo in sola lettura, per ora |

**ReefRun comanda la pompa di risalita e quella dello schiumatoio.** Non è una pompa di movimento. **ReefControl Power** *(beta)* mette le sue prese fra i normali comandi delle prese, come una presa Apex: solo on/off. Per queste non c'è ancora una modalità automatica.

## Modificare un piano ReefDose o un programma ReefRun *(beta)*

Tocca l'icona del calendario su una pagina ReefDose o ReefRun per aprire il suo piano.

Un piano ReefDose è un totale giornaliero, diviso in massimo quattro fasce orarie. Ogni fascia ha un orario di inizio e fine, quante dosi deve erogare e una velocità: **Silenzioso**, **Normale** o **Rapido**. Aggiungi e togli fasce, poi salva. Cora ti mostra cosa stai per inviare e ti chiede conferma prima di sostituire tutto il piano della testa.

Un programma ReefRun è composto da massimo sei segmenti su una porta pompa. Ogni segmento ha un orario di inizio e una velocità, e può aggiungere un breve impulso. La velocità va da 0 oppure da un minimo del 5% in su. Anche qui il salvataggio chiede conferma e sostituisce tutto il programma della pompa.

Entrambi gli editor leggono prima il piano già presente sull'unità, così stai modificando quello vero e non un modulo vuoto.

## Impostazioni ReefMat *(beta)*

Tocca l'ingranaggio su una pagina ReefMat per altre tre impostazioni.

- **Avanzamento programmato** attiva un avanzamento a orario fisso, separato dal sensore di auto-avanzamento già presente sulla pagina. Attivalo e imposta ogni quanto e di quanto muovere il tappetino a ogni avanzamento.
- **Modello ReefMat** e **Posizione motore** (**Sinistra** o **Destra**) dicono a Cora quale unità e quale orientamento hai.

Dopo aver caricato un nuovo rotolo, dillo a Cora con **Nuovo rotolo**: indica lo spessore e, se lo sai, il diametro esterno. È diverso da **Far avanzare il rotolo**, che si limita a muovere il tappetino già caricato.

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

## GHL ProfiLux e Mitras

:::note Il supporto GHL è in beta
Il supporto GHL è ancora in fase di test e sviluppo. Alcune letture o alcuni comandi potrebbero non funzionare ancora, e quello che vedi qui potrebbe cambiare da un aggiornamento all'altro. Se qualcosa non funziona come descritto, scrivici da [Ottenere assistenza](/help/mobile-support).
:::

La pagina del controller mostra le sue sonde, prese, dosatori e sensori di livello, e sui modelli Director anche i risultati dei test di KH e ioni.

I comandi restano disattivati finché non attivi **Consenti il controllo da Cora (Beta)** sulla pagina del dispositivo. È disattivato per impostazione predefinita, e attivarlo permette a Cora di inviare a quel controller comandi di pausa alimentazione, manutenzione, cambio acqua, temporale, illuminazione, setpoint e prese.

Una volta attivato:

- Una presa si può impostare su **Sempre acceso**, **Sempre spento** o **Torna ad automatico** per restituirla alla programmazione del controller.
- Un setpoint, come temperatura o pH, mostra il suo intervallo consentito e rifiuta un valore fuori da quell'intervallo.

:::warning Una modifica a presa o setpoint viene salvata sul controller stesso
Non resta solo dentro Cora. Impostare una presa su Sempre acceso o Sempre spento sostituisce la programmazione del controller per quella presa, finché non scegli Torna ad automatico.
:::

Se una presa o un setpoint sembra appartenere a un riscaldatore o a una pompa di risalita, Cora ti chiede due conferme prima di inviarlo.

Se il contenitore di un dosatore sta per finire, Cora ti avvisa come fa per gli altri materiali di consumo. Il valore predefinito è 20% pieno, e lo puoi cambiare dalla regola del dosatore nel [Centro avvisi](/help/mobile-alerts).

:::note ProfiLux mini
Un mini può comandare solo le sue prese. Tutto il resto qui, come i setpoint e la pausa alimentazione, richiede un ProfiLux 3, 4 o Mitras.
:::

Se il controller rifiuta la modifica, controlla che la sua API GHL sia attiva con accesso completo. GHL la disattiva dopo ogni aggiornamento firmware. I passaggi sono in [Risoluzione dei problemi](/help/troubleshooting).

## HYDROS

:::note Il supporto HYDROS è in beta
Il supporto HYDROS è ancora in fase di test e sviluppo. Alcune letture o alcuni comandi potrebbero non funzionare ancora, e quello che vedi qui potrebbe cambiare da un aggiornamento all'altro. Se qualcosa non funziona come descritto, scrivici da [Ottenere assistenza](/help/mobile-support).
:::

Quello che vedi qui dipende dalla chiave con cui l'hai collegato. Una chiave **Read** ti dà solo i suoi ingressi. Una chiave **Write** aggiunge uscite, modalità, dosaggio e comandi tester, più un banner in pagina che ti ricorda con quale tipo di chiave stai lavorando.

Con una chiave di scrittura, anche i comandi restano disattivati finché non attivi **Consenti il controllo da Cora (Beta)** sulla pagina del dispositivo. È disattivato per impostazione predefinita.

Una volta attivato, la pagina può mostrare:

- **Uscite**, come un interruttore per un'uscita on/off, uno slider per un livello (una pompa o una luce) o un pulsante per un flag. Un'uscita sostituita mostra **Sovrascritto** con un pulsante **Torna al programma** per restituirla al suo programma.
- **Modalità**, come Alimentazione o Cambio acqua, come una riga di scelte. Toccarne una chiede una conferma.
- **Teste di dosaggio**, ognuna con un pulsante **Dosa** e una voce **Impostazioni testina** dove imposti i suoi limiti: una dose massima manuale e un tetto giornaliero. Chiedere più del limite di una testa, o più di quanto è rimasto del suo tetto giornaliero, viene rifiutato con i numeri nel messaggio.
- **Comandi tester**, per un iV o un Maven collegato, avviati da un pulsante e confermati prima.

Se il controller non risponde da un po', la pagina lo segnala e le letture possono essere non aggiornate. Un comando inviato mentre risulta offline non parte affatto, e la pagina te lo dice.

## Dopo una modifica

Ogni modifica viene registrata in [Attività](/help/mobile-activity) insieme alla superficie da cui è partita. Se un dispositivo non accetta la modifica, anche questo viene registrato lì.
