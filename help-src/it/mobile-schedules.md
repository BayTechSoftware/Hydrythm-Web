---
title: Pianificare l'equipaggiamento
description: Crea un programma giornaliero per una pompa Jecod e copialo tra pompe, e visualizza il programma di una gyre Maxspect (beta).
section: Cora Mobile
reviewed: 2026-09-17
order: 12
group: Equipment
---

Le pompe e le gyre possono eseguire un **programma giornaliero**: un insieme di periodi, ognuno con la propria intensità, che si ripete ogni giorno. Cora può creare questi programmi direttamente per le pompe Jecod. Il programma di una gyre Maxspect *(beta)* può essere solo visualizzato qui: impostalo nell'app Maxspect.

Apri il dispositivo dalla scheda **Dispositivi**.

![Il programma di una pompa](img/mobile-schedules.webp "Il grafico giornaliero da 0 a 24 ore, con ogni periodo elencato sotto di esso.")

## Uguale tutto il giorno, o Programma

Una pompa funziona in una di due modalità, scelta in alto nella sua pagina:

- **Uguale tutto il giorno**: un'intensità, costante
- **Programma**: un programma giornaliero con periodi

La tua scelta viene inviata alla pompa, tramite il Cora Max alla vasca quando il tuo telefono non è sulla rete della pompa. Una pompa Bluetooth deve essere a portata: fino a quando non lo è, scegliere qui cambia solo ciò che stai guardando.

## L'editor del programma

Ogni schermata del programma ha le stesse tre parti:

**Il grafico giornaliero**: l'intera giornata da 0 a 24 ore, con ogni periodo disegnato come un blocco la cui altezza è la sua intensità. È il modo più rapido per vedere se un programma fa quello che pensi.

**L'elenco dei periodi**: ogni periodo sotto il grafico, con le sue ore, la sua modalità e la sua intensità: *Casuale, 00:00–03:00, Freq 50%, 40%*. Aggiungi, modifica e rimuovi periodi qui.

**Aggiungere e cambiare periodi**: **Aggiungi al programma** aggiunge un periodo. Apri un periodo per cambiarlo e tocca **Salva**, oppure **Elimina** per rimuoverlo; ti verrà chiesto di confermare prima che venga rimosso.

Una gyre Maxspect *(beta)* ha due teste, mostrate come Gyre A e Gyre B, quindi il suo grafico giornaliero ha due tracce, una per ciascuna, e i suoi piani sono elencati sotto **GYRE A** e **GYRE B**. Il programma di una gyre è di sola visualizzazione: la sua riga di azioni mostra **Solo visualizzazione**, e il programma si imposta nell'app Maxspect.

:::warning Un programma viene scritto sul dispositivo
Salvare invia il programma all'equipaggiamento, che poi lo esegue con il proprio orologio. Continua a funzionare sia che Cora sia raggiungibile o no.
:::

## Copiare un programma tra pompe

Se gestisci diverse pompe che dovrebbero comportarsi allo stesso modo, crea un programma e copialo.

Apri la pompa il cui programma vuoi, poi **Copia programma su…**, e scegli la pompa su cui copiarlo.

## Conservare e condividere un programma

Un programma di cui sei contento non deve essere ricreato da zero:

- **Salva programma come…** lo conserva sotto un nome, e **Programmi salvati…** lo applica di nuovo più avanti.
- **Condividi questo programma** lo trasforma in un breve codice, e **Incolla un codice programma…** applica uno che qualcuno ti ha inviato. Questa è una funzione di Cora Mobile; il codice porta il programma, non l'accesso al tuo account.

## Lontano dalla rete della pompa

Quando il tuo telefono non è sulla rete della pompa, Cora Mobile lavora tramite il Cora Max alla vasca, con dei limiti:

- **Uguale tutto il giorno** e **Programma** commutano la pompa tramite quel Cora Max.
- Un periodo che aggiungi o cambi passa attraverso di esso solo se ha raggiunto la pompa nell'ultima ora. Se non l'ha fatto, il programma lo dice e non può essere cambiato da dove sei.
- **Copia programma su…**, **Salva programma come…**, **Programmi salvati…**, **Condividi questo programma** e **Incolla un codice programma…** richiedono il tuo telefono sulla rete della pompa. Fino a quel momento sono disattivati in grigio, e il menu dice perché.

Una pompa Bluetooth può essere raggiunta solo da un telefono nelle vicinanze: stai a portata per commutarla, cambiare il suo programma o usare qualsiasi di quelle voci.

## Applicare un programma

A una pompa può anche essere assegnato un programma già pronto in un solo passaggio, invece di crearlo periodo per periodo a mano.

## Verificare che sia stato applicato

Dopo il salvataggio, la pagina del dispositivo mostra il programma che l'unità sta effettivamente eseguendo. Se i due non coincidono, la scrittura non è andata a buon fine; controlla che il dispositivo sia raggiungibile e riprova.
