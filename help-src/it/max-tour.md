---
title: La schermata principale di Cora Max
description: Cosa vogliono dire su Cora Max la barra in alto, l'etichetta di stato, le etichette degli avvisi, il menu della vasca e la dashboard, e come cambiare vasca e aprire Prese e alimentazione.
section: Cora Max
reviewed: 2026-10-13
order: 2
group: Getting started
twin: mobile-tour
---

Questa pagina spiega cosa vedi su Cora Max. Mostra una vasca alla volta, con le letture in tempo reale che riempiono lo schermo così puoi leggerle dall'altra parte della stanza.

![La schermata principale di Cora Max con indicatori, valori, grafici e riquadri dei dispositivi di una vasca sotto la barra in alto](img/max-home.webp "La dashboard di una vasca riempie lo schermo, con la barra in alto sopra.")

## La barra in alto {#the-top-bar}

![La barra in alto di Cora Max](img/max-topbar.webp "La barra in alto, numerata da sinistra a destra come l'elenco qui sotto.")

Da sinistra a destra:

1. **L'icona a griglia** apre [la Reef Room](/help/max-reef-room), la panoramica di tutte le vasche che mostra questo schermo.
2. **Il nome della vasca**, con una piccola freccia. Toccalo per aprire il **menu della vasca**, che contiene tutte le schermate della vasca che stai guardando. L'elenco completo è più sotto.
3. **Le etichette degli avvisi** mostrano cosa richiede attenzione in questo momento: letture fuori range, guasti dei dispositivi, dosi mancate o scorte basse. Tocca un'etichetta per riportare quell'avviso al centro dello schermo. Se sono più di quelle che ci stanno, vedrai **+2** (o quante sono). Toccalo per vedere tutti gli allarmi attivi.
4. **L'orologio**. Puoi nasconderlo con **Mostra orologio** in **Impostazioni → Impostazioni Cora Max**.
5. **L'etichetta di stato** mostra cosa sta facendo questo schermo in questo momento. Verde vuol dire che va tutto bene, blu che è occupato, ambra che va controllato e rosso che c'è un guasto. Tutti gli stati sono elencati più sotto.
6. **Batteria e Wi-Fi**.
7. **L'icona dei dispositivi** apre **Dispositivi**, filtrato su questa vasca. Una vasca senza dispositivi non la mostra.
8. **L'icona di Reef Buddy** apre il briefing di oggi. Un puntino vuol dire che non l'hai ancora letto.
9. **L'icona di Cora Assistant** avvia una conversazione a voce.
10. **L'ingranaggio** apre le impostazioni.

:::warning Cora Assistant comincia ad ascoltare subito
Toccare l'icona di Cora Assistant avvia una sessione vocale dal vivo. Se volevi le impostazioni, sono l'ingranaggio all'estrema destra.
:::

### Cosa significa l'etichetta di stato {#what-the-status-pill-means}

| Etichetta | Significato |
|---|---|
| **Online** | Questo schermo sta raccogliendo le tue letture, e sono aggiornate |
| **Cloud** | Un altro Cora sta raccogliendo le letture di questa vasca e questo schermo le mostra. Sono aggiornate quanto con **Online**. Se hai più di un Cora, quello che non sta raccogliendo mostra questa etichetta |
| **Polling Apex**, **Voce attiva** | Occupato con qualcosa in questo momento (blu) |
| **Polling disattivato** | La raccolta è spenta per questa vasca. Puoi riattivarla in Cora Mobile |
| **Aggiornamento in corso** | La raccolta è in pausa mentre si installa un aggiornamento |
| **Non aggiornato** | Le letture hanno smesso di arrivare. Lo schermo mostra le ultime ricevute |
| **Nuovo tentativo Apex 12s** | Il tuo Apex non ha risposto. Cora Max riprova quando finisce il conto alla rovescia |
| **Sincronizzazione cloud non riuscita** | Il tuo Apex ha risposto, ma le sue letture non si sono potute salvare in Cora Cloud, quindi la dashboard resta indietro. Cora Max continua a provare |
| **Salvataggio cloud rifiutato** | Cora Cloud rifiuta di salvare alcuni dati di questo schermo. Non c'è niente che non va nella tua vasca o in Cora Max, e non c'è niente da cambiare su questo schermo. La soluzione è un aggiornamento di Cora Cloud. Apri **Impostazioni → Impostazioni Cora Max** e scorri fino alla sezione **Stato**, dove la riga **Salvataggio cloud** dice quali dati sono coinvolti. Poi [contatta l'assistenza](/support.html) |
| **Offline** | Nessuna connessione. Lo schermo mostra gli ultimi dati ricevuti |
| **Offline, nuovo tentativo in 45s** | La tua rete funziona, ma Cora Cloud è irraggiungibile da più di 30 secondi. Cora Max si ricollega da solo, e il conto alla rovescia mostra quando riprova |
| **Cora principale offline** | Questo schermo è un secondo Cora Max per questa vasca, e il **Cora Max principale** (quello fissato per leggere l'attrezzatura di questa vasca) è andato offline. Questo schermo continua a mostrare gli ultimi dati che ha finché il principale non torna o non scegli un altro Cora Max principale. Di più in [Più di un dispositivo Cora](/help/mobile-multi-device) |
| **Password Apex** | Il tuo Apex ha rifiutato la password salvata. Dai un'occhiata a [Risoluzione dei problemi](/help/troubleshooting) |

:::note Come funziona il conto alla rovescia dei tentativi
Cora Max prova a ricollegarsi a un ritmo regolare. Aspetta circa 15 secondi dopo la prima interruzione, poi di nuovo 15 secondi, poi 30 secondi due volte, poi una volta al minuto finché non ci riesce. Non si arrende mai. **Offline, nuovo tentativo in 45s** è normale.
:::

## La dashboard {#the-dashboard}

Il resto dello schermo è la dashboard, una griglia fissa che tiene visibile ogni widget. Non scorre.

I widget funzionano come sul telefono, ma abbastanza grandi da leggerli da qualche passo di distanza. Cosa mostra ogni forma è nella [Guida ai widget](/help/mobile-widgets). Per cambiare cosa c'è sulla dashboard, vedi [Modificare la dashboard di Cora Max](/help/max-dashboard-editing).

Ogni widget con un parametro misurato mostra la sua **età** e la sua **fonte**, proprio come sul telefono. Un numero con `2d` accanto ha due giorni. I riquadri di dispositivi e comandi mostrano invece il loro stato.

### Quando lo schermo è attenuato {#when-the-screen-is-dimmed}

Dopo il tempo di **Attenua dopo** senza tocchi, lo schermo si attenua. Il primo tocco lo risveglia soltanto, così non può premere un comando per sbaglio. Tocca di nuovo per usare lo schermo.

## Il menu della vasca {#the-tank-menu}

![Il menu della vasca aperto sopra la dashboard, con Registra parametri, Diario, Reef Buddy e le altre schermate della vasca](img/max-menu.webp "Il menu della vasca, aperto dal nome della vasca nella barra in alto.")

Tocca il nome della vasca per aprire il menu della vasca sullo schermo.

| Voce | Apre |
|---|---|
| **Registra parametri** | Inserisci le letture dei test con la tastiera sullo schermo |
| **Diario** | [Il diario](/help/max-records) di questa vasca |
| **Reef Buddy** | L'ultimo [briefing](/help/max-intelligence) |
| **Report di salute** | Le valutazioni della salute |
| **Manutenzione** | L'[elenco delle attività](/help/max-records) |
| **Report ICP** | I [risultati di laboratorio](/help/max-intelligence) caricati |
| **Storico parametri** | Scegli un parametro qualsiasi che ha dati e apri il suo [grafico](/help/max-intelligence) |
| **Soglie di avviso** | L'[intervallo ideale](/help/max-alerts) di ogni parametro di questa vasca |
| **Popolazione** | L'inventario di questa vasca, in sola visualizzazione su questo schermo |
| **Attività** | [Ogni presa, alimentazione e dose](/help/max-activity), e cosa è successo |
| **Layout dashboard** | [Disponi i widget su questo schermo](/help/max-dashboard-editing) |
| **Unità** | Le unità di visualizzazione delle letture di questa vasca |
| **Impostazioni vasca** | La schermata completa delle impostazioni di questa vasca |

## Cambiare vasca {#switching-tanks}

Tocca l'**icona a griglia** all'estrema sinistra della barra in alto per andare alla [Reef Room](/help/max-reef-room), poi apri la vasca che vuoi. Puoi anche scorrere di lato sulla dashboard. Ogni vasca ha il suo layout della dashboard, quindi tutto lo schermo cambia quando passi da una all'altra.

## Il pannello Prese e alimentazione {#the-outlets-feed-drawer}

Su una vasca con un Neptune Apex, una piccola etichetta **Prese e alimentazione** si trova in fondo alla dashboard. Toccala, oppure scorri verso l'alto in qualsiasi punto della dashboard, per aprire **Controlli**.

- **ALIMENTAZIONE** avvia uno dei cicli di alimentazione del tuo Apex con **A**, **B**, **C** o **D**. **Annulla alimentazione** lo termina prima.
- Ogni presa in **PRESE** può passare tra Auto, Off e On.

Elenca le prese e i cicli di alimentazione che hai scelto per questa dashboard, oppure tutti se non ne hai scelti. Di più in [Prese e comandi](/help/max-controls).

:::warning Questo pannello comanda attrezzatura vera
Un comando parte appena tocchi, ma inviarlo non vuol dire che sia fatto. Torna come Confermato, Non confermato, Rifiutato o Nessun cambiamento, e puoi vedere quale in [Attività](/help/max-activity). La modalità alimentazione è il modo sicuro per mettere in pausa il movimento per l'alimentazione, perché rimette tutto a posto da sola. Un Off manuale resta spento finché non lo cambi.
:::

## Se qualcosa sembra fuori posto {#if-something-looks-out-of-place}

Se le letture sembrano vecchie, o l'etichetta di stato è ambra o rossa, parti da [Risoluzione dei problemi](/help/troubleshooting).
