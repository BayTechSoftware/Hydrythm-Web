---
title: Configurare Cora Max
description: Associa un nuovo Cora Max a Cora Mobile via Bluetooth, collegalo al Wi-Fi, scegli le sue vasche e spostalo su un'altra vasca più avanti.
section: Cora Max
reviewed: 2026-10-13
order: 1
group: Getting started
twin: mobile-setup
---

Questa pagina ti porta da un Cora Max nuovo a uno schermo a parete funzionante. Lo associ dal telefono via Bluetooth, e non devi scrivere niente sullo schermo stesso.

:::tip Prima configura le vasche sul telefono
Cora Max mostra le vasche e i dispositivi del tuo account, e non può creare una vasca da solo. [Configurale prima in Cora Mobile](/help/mobile-setup). Cora Max le trova appena lo associ.
:::

## Cosa ti serve {#what-you-need}

- Cora Max, collegato alla corrente e acceso. È fatto per restare collegato.
- Cora Mobile sul telefono, con l'accesso fatto e **almeno una vasca** già creata.
- Il Bluetooth del telefono acceso, e il telefono vicino a Cora Max.
- Il nome e la password della tua rete Wi-Fi.

Metti Cora Max dove puoi vederlo dall'altra parte della stanza e parlargli, lontano da spruzzi e incrostazioni di sale.

## Cosa mostra prima lo schermo {#what-the-screen-shows-first}

Accendi Cora Max. Mostra una schermata di associazione che dice **Apri l'app Cora sul tuo telefono**, poi **Tocca Aggiungi dispositivo.** e **Scegli questo Cora Max dall'elenco Dispositivi.** Sotto mostra **Rilevabile come** e il suo nome, che finisce con un breve codice. Se ne stai associando più di uno, quel codice li distingue sul telefono.

![La schermata di associazione di Cora Max, in attesa del telefono](img/max-pairing-screen.webp "In attesa del telefono. La riga in basso mostra il nome che il telefono elencherà.")

La stessa schermata ha un breve avviso sulle integrazioni con l'attrezzatura di altri produttori. I Termini che hai accettato in Cora Mobile valgono anche per Cora Max.

## Associarlo dal telefono {#pairing}

Tutto il resto succede in Cora Mobile. Un pannello ti guida in cinque passi, mostrati in alto: **Connetti · Wi-Fi · Accesso · Vasche · Fatto**.

1. **Trovalo.** Apri la scheda **Dispositivi**, tocca **Aggiungi dispositivo**, poi **Cora**. La schermata **Aggiungi il tuo Cora** elenca i dispositivi Cora sulla tua rete e i dispositivi da configurare trovati nelle vicinanze via Bluetooth. Tocca **Scansiona** se il tuo non c'è ancora, poi tocca il tuo Cora Max.

   ![La schermata Aggiungi il tuo Cora in Cora Mobile, durante la ricerca dei dispositivi](img/mobile-add-device.webp "Aggiungi dispositivo, poi Cora. Cora Mobile cerca sul tuo Wi-Fi e via Bluetooth, con Inserisci l'indirizzo IP manualmente sotto.")

2. **Connetti.** Il telefono si collega a Cora Max via Bluetooth e mostra il suo indirizzo MAC, il firmware, la variante e la revisione hardware. Controlla che sia quello giusto, poi tocca **Continua**.

3. **Wi-Fi.** Scegli la tua rete dall'elenco, oppure tocca **Ripeti scansione**, e scrivi la password sul telefono. Da qui in poi il telefono parla con Cora Max via Wi-Fi, quindi tieni il telefono sulla stessa rete.

4. **Accesso.** Il telefono collega Cora Max al tuo account. Avviene da solo, e Cora Max mostra il suo avanzamento, come **Verifica del tuo account…** e **Configurazione della tua vasca…**.

   ![La schermata di associazione di Cora Max che mostra Verifica del tuo account](img/max-pairing-verifying.webp "Cora Max mostra ogni passo mentre il telefono lo collega al tuo account.")

5. **Vasche.** In **Assegna vasche**, scegli le vasche che questo Cora Max gestirà, **fino a quattro**.

6. **Fatto.** Il telefono dice che Cora Max è configurato e mostra un **PIN di ripristino**. Tocca il pulsante che apre la dashboard della tua vasca, oppure **Vai a Dispositivi**. Cora Max mostra **Associato**, poi **Apertura dashboard…**.

:::warning Annota il PIN di ripristino
Il **PIN di ripristino** ha sei cifre ed è l'unico modo per entrare nel ripristino su quel Cora Max. Per usarlo, tieni cinque dita sull'angolo in alto a destra dello schermo per dieci secondi, poi inserisci il PIN. Il ripristino ti permette di rifare il Wi-Fi, associarlo di nuovo, controllare un aggiornamento o fare il ripristino di fabbrica. Puoi ritrovare il PIN sul telefono in **Dispositivi → il tuo Cora Max → PIN di ripristino**, ma mai su Cora Max stesso.
:::

### Se l'associazione si blocca {#if-pairing-gets-stuck}

- **Il Bluetooth è disattivato. Attivalo, poi tocca di nuovo Scansiona.** Attiva il Bluetooth e cerca di nuovo.
- **L'autorizzazione Bluetooth per Cora è disattivata.** Consenti il Bluetooth per Cora nelle impostazioni del telefono, poi tocca **Scansiona**. Un iPhone potrebbe chiedere anche l'accesso alla rete locale. Consenti anche quello.
- **Nessun dispositivo di configurazione Cora trovato nelle vicinanze via Bluetooth.** Mettiti accanto a Cora Max, controlla che mostri ancora la schermata di associazione e cerca di nuovo.
- **Nessuna vasca trovata** al passo Vasche. Il tuo account non ha ancora una vasca. Creane una in Cora Mobile, poi riprova il passo.
- **Non ancora collegato alla tua vasca** alla fine. Cora Max è associato, ma il collegamento alla vasca non è finito. Tocca **Riprova ora**. Finché non finisce, gli avvisi di questo schermo usano gli intervalli predefiniti.

Altre soluzioni in [Risoluzione dei problemi](/help/troubleshooting#pairing-a-cora-max-fails).

## Dopo l'associazione {#after-pairing}

Ora Cora Max vede le stesse vasche, gli stessi dispositivi, le stesse letture e gli stessi registri del telefono.

- Se una delle tue vasche aveva già un Cora Max, Cora Max chiede **Ripristinare il layout precedente per questa vasca?** **Ripristina** riporta le impostazioni di schermo, suono e avvisi che aveva salvato quello vecchio. **Inizia da zero** le salta.
- Una vasca ancora senza letture mostra **Nessuna lettura ancora** e un pulsante **Registra il tuo primo test**.
- Cora Max crea una dashboard iniziale dal profilo della vasca. Non copia quella del telefono.

Puoi associare più di un Cora Max allo stesso account, per esempio uno nella stanza dell'acquario e uno in soggiorno. Ognuno può mostrare vasche diverse e ha il suo layout. Se due mostrano la stessa vasca, [Più di un dispositivo Cora](/help/mobile-multi-device) spiega quale legge l'attrezzatura.

## Costruire la dashboard {#building-the-dashboard}

La dashboard del grande schermo è una griglia fissa, e tutto deve stare in una schermata. Il modo più veloce per sistemarla è dal telefono: apri la scheda **Dispositivi**, tocca il tuo Cora Max, poi tocca **Layout dashboard** sulla scheda della vasca. Puoi farlo anche dallo schermo a parete dal menu della vasca.

Per riusare un layout di un altro Cora Max o di un'altra vasca, caricalo da **Le mie dashboard** nell'editor. Di più in [Modificare la dashboard di Cora Max](/help/max-dashboard-editing).

## Spostare Cora Max su un'altra vasca {#changing-which-tanks-it-shows}

Quali vasche mostra un Cora Max si cambia dal telefono. Le impostazioni di Cora Max non possono farlo.

1. In Cora Mobile, apri la scheda **Dispositivi** e tocca il tuo Cora Max.
2. In **Vasche**, tocca **Aggiungi vasca** e scegli la vasca. Un Cora Max ne accetta fino a quattro. Quando ne ha già quattro, il pulsante non c'è, quindi togline prima una.
3. Per togliere una vasca da questo schermo, tocca l'icona rossa di rimozione (**Rimuovi vasca**) sulla scheda di quella vasca, poi tocca **Rimuovi**.

Per spostare Cora Max da una vasca all'altra, aggiungi la vasca nuova, poi togli quella vecchia. La vasca nuova riceve una dashboard iniziale costruita dal suo profilo. Sistemala con **Layout dashboard**.

Se questo Cora Max era il Cora Max principale fissato per la vasca che hai tolto, quella scelta viene cancellata e la vasca torna a **Qualsiasi attivo (automatico)**. Di più in [Dispositivi e salute dei dispositivi](/help/max-devices).

## Aggiornamenti {#updates}

Cora Max si aggiorna da solo. Una nuova versione si scarica in background e si installa di notte. La tua versione è mostrata in cima a **Impostazioni → Impostazioni Cora Max**. Di più in [Aggiornamenti e ripristino](/help/max-updates).

## Spostarlo su un'altra rete Wi-Fi {#moving-it-to-a-different-network}

Vai in **Impostazioni → Impostazioni Cora Max → Wi-Fi**, scegli la nuova rete e inserisci la password. Cora Max resta associato, quindi non devi configurarlo di nuovo.
