---
title: Programmare l'attrezzatura
description: Crea nell'editor una programmazione giornaliera per una pompa Jecod, copiala da altre pompe o su altre pompe, salvala e condividila e controlla che la pompa l'abbia ricevuta.
section: Cora Mobile
reviewed: 2026-11-03
order: 14
group: Equipment
---

Usa questa pagina per dare a una pompa Jecod una **programmazione giornaliera**: una serie di fasce, ognuna con la sua intensità, che si ripete ogni giorno. Aprila da **Dispositivi** → tocca la pompa.

Le luci e le pompe di altre marche tengono le loro programmazioni nelle loro pagine: ReefDose di Red Sea in [Controllare la tua attrezzatura](/help/mobile-device-control#red-sea).

![La pagina di una pompa Jecod in Cora Mobile con Programmazione selezionata](img/mobile-schedules.webp "Programmazione selezionata in alto, la pausa per l'alimentazione, poi il grafico della giornata.")

## Manuale o Programmazione {#same-all-day-or-schedule}

Una pompa funziona in una di due modalità. Sceglila con il selettore nella sua pagina. Quella in corso è segnata con *· in corso*, e la pagina si apre su di essa.

- **Manuale** funziona sempre alla stessa intensità.
- **Programmazione** segue una programmazione giornaliera fatta di fasce.

Cora invia la tua scelta direttamente alla pompa quando il telefono è sulla sua rete. Se non lo è, passa dal Cora Max vicino alla vasca. Una pompa Bluetooth deve essere a portata. Finché non lo è, la tua scelta cambia solo quello che vedi sullo schermo.

Una pausa per l'alimentazione toglie la pompa dalla sua programmazione per un po', e sul telefono la programmazione riprende solo finché la pagina della pompa resta aperta. Vedi [Pausa per l'alimentazione](/help/mobile-device-control#jecod-feeding).

## L'editor della programmazione

Ogni schermata della programmazione ha le stesse tre parti.

In alto c'è il grafico della giornata. Mostra tutta la giornata da 0 a 24 ore, e ogni fascia è un blocco alto quanto la sua intensità. È il modo più veloce per controllare che una programmazione faccia quello che pensi.

Sotto il grafico c'è l'elenco delle fasce. Ogni fascia mostra orari, modalità e intensità, per esempio *Casuale, 00:00–03:00, Freq 50%, 40%*. Qui aggiungi, modifichi e togli le fasce.

Ogni modifica a una programmazione passa dall'editor. **Modifica** lo apre sulla giornata della pompa, e lo stesso fa toccare una fascia o **Aggiungi alla programmazione** nella pagina della pompa: l'editor si apre con quella fascia, o una nuova, pronta da modificare. Nell'editor, cambia una fascia e tocca **Salva**, oppure toglila con **Elimina fascia**. **Annulla** torna indietro di un passo. Il menu ⋮ ha **Salva programmazione come…**, **Programmazioni salvate…** e **Copia da…**.

Non viene inviato nulla alla pompa finché non tocchi **Salva sulla pompa**. Cora allora scrive l'intera giornata in una volta. Se non ci riesce, l'editor dice perché e tiene le tue modifiche. Se chiudi l'editor prima di salvare, Cora chiede prima *Scartare queste modifiche?*


:::warning Salva sulla pompa scrive la programmazione sul dispositivo
Quando tocchi **Salva sulla pompa**, Cora invia la programmazione all'attrezzatura, che la segue con il suo orologio. Continua a funzionare che Cora riesca a raggiungerla oppure no.
:::

## Copiare una programmazione tra le pompe {#copying-a-program-between-pumps}

Se hai più pompe che devono comportarsi allo stesso modo, crea una programmazione e copiala. Puoi copiare in entrambe le direzioni, e non viene inviato nulla finché non tocchi **Salva sulla pompa**.

- **Copia da…** (nel menu ⋮ della programmazione e in quello dell'editor) prende la programmazione di un'altra pompa di movimento su una qualsiasi delle tue vasche. Ogni fascia riceve la modalità più vicina che ha questa pompa, le velocità restano entro quelle che può usare, e **Cosa cambia su questa pompa** elenca ogni modifica. **Carica nell’editor** mette la copia nell'editor di questa pompa, dove puoi sistemarla e poi toccare **Salva sulla pompa**. Una pompa di cui Cora non ha ancora letto la programmazione è disattivata, con il motivo.
- **Copia programmazione su…** dà la giornata di questa pompa ad altre pompe di qualsiasi tua vasca, ognuna elencata come *Vasca · Pompa*. Spunta le pompe e tocca **Rivedi**. Non viene ancora inviato nulla. **Rivedi le copie** elenca ogni pompa con il suo stato, **Non salvato**, **Salvato sulla pompa** o **Non riuscito** con il motivo, e quante modifiche riceve. **Apri editor** apre l'editor di quella pompa sulla giornata copiata, con il suo **Salva sulla pompa**, che la invia solo a quella pompa. Se un salvataggio non riesce, la bozza resta così puoi riprovare. Se esci mentre alcune pompe non sono salvate, Cora chiede prima *Scartare le copie non salvate?*

## Conservare e condividere una programmazione

Quando hai una programmazione che ti piace, non devi ricrearla.

- **Salva programmazione come…** la conserva con un nome. **Programmazioni salvate…** la riprende in seguito: **Carica nell’editor** la apre nell'editor, e **Salva sulla pompa** la invia.
- **Condividi questa programmazione** la trasforma in un codice breve. **Incolla un codice di programmazione…** carica nell'editor un codice che ti ha mandato qualcuno, e non viene inviato nulla finché non tocchi **Salva sulla pompa**. È una funzione di Cora Mobile. Il codice contiene solo la programmazione. Non dà a nessuno accesso al tuo account.

## Lontano dalla rete della pompa

Quando il telefono non è sulla rete della pompa, Cora Mobile passa dal Cora Max vicino alla vasca. Alcune cose funzionano in modo diverso.

- **Manuale** e **Programmazione** cambiano la modalità della pompa attraverso quel Cora Max.
- Una programmazione che salvi sulla pompa passa solo se quel Cora Max ha raggiunto la pompa nell'ultima ora. Se no, la programmazione te lo segnala, e da dove sei non puoi modificarla.
- **Copia programmazione su…**, **Salva programmazione come…**, **Programmazioni salvate…**, **Condividi questa programmazione** e **Incolla un codice di programmazione…** richiedono il telefono sulla rete della pompa. Finché non lo è, sono disattivati e il menu ti spiega perché.

Senza un Cora Max nella vasca, puoi cambiare una pompa solo mentre il telefono è sulla sua rete. Di più in [Collegare la tua attrezzatura](/help/mobile-connections#local-only).

Una pompa Bluetooth si raggiunge solo da un telefono vicino. Mettiti a portata per cambiarne la modalità, modificarne la programmazione o usare una di quelle voci del menu.

## Applicare una programmazione

Puoi dare a una pompa una programmazione salvata in un solo passaggio, senza ricreare le fasce. Apri la pompa, tocca **Altro** in alto e scegli **Programmazioni salvate…**. L'elenco contiene tutte le programmazioni salvate su questa vasca, compresi quelli creati su un'altra pompa. Scegline uno e tocca **Carica nell’editor**. Controllala nell'editor, poi tocca **Salva sulla pompa**. Sostituisce l'intera giornata della pompa.

## Controllare che sia arrivato

Dopo il salvataggio, la pagina del dispositivo mostra la programmazione che la pompa sta seguendo. Se non corrisponde a quella che hai salvato, la modifica non è arrivata. Controlla che il dispositivo sia raggiungibile e riprova.
