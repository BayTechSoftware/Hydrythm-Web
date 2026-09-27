---
title: La schermata Home di Cora Max
description: Cosa significa ogni cosa sullo schermo di Cora Max: la barra superiore, la griglia della dashboard, e il cassetto delle prese.
section: Cora Max
reviewed: 2026-09-27
order: 2
group: Getting started
---

Cora Max mostra una vasca alla volta, riempiendo lo schermo con letture in tempo reale che puoi leggere da tutta la stanza.

![La schermata Home di Cora Max](img/max-home.webp "Una vasca, che riempie lo schermo.")

## La barra superiore

Da sinistra a destra:

- **L'icona della griglia** apre la Stanza della Vasca, la vista d'insieme di ogni vasca mostrata da questo schermo
- **Il nome della vasca**, con una freccetta. Toccarlo apre il **menu della vasca**: ogni schermata per la vasca in visualizzazione, dal registrare un risultato di test al disporre la dashboard. L'elenco completo è sotto.
- **Pillole di avviso**: qualsiasi cosa attualmente fuori intervallo, con un **+n** quando ce ne sono più di quante ne entrano. Tocca per vederle tutte.
- **L'orologio**
- **La pillola di stato**: cosa sta facendo questo schermo in questo momento. Verde è sano, ambra richiede attenzione, rosso è un guasto. Il vocabolario completo è sotto.
- **Batteria e Wi-Fi**
- **L'icona dei dispositivi**: tutto ciò che è collegato, e come sta andando
- **L'icona di Reef Buddy**: apre il briefing di oggi. Un punto indica che il briefing non è ancora stato letto.
- **L'icona di Cora Assistant**: avvia una conversazione vocale
- **La rotella**: impostazioni

### Cosa significa la pillola di stato

| Pillola | Significato |
|---|---|
| **Online** | Questo schermo sta raccogliendo le tue letture, e sono attuali |
| **Cloud** | Un altro Cora sta raccogliendo le letture di questa vasca e questo schermo le sta mostrando. Altrettanto attuale di **Online**; con più di un Cora, lo schermo che non sta facendo la raccolta mostra questo |
| **Polling Apex**, **Voce attiva** | Sta lavorando su qualcosa in questo momento |
| **Polling disattivato** | La raccolta è disattivata per questa vasca. Puoi riattivarla da Cora Mobile |
| **Aggiornamento in corso** | La raccolta è in pausa mentre si installa un aggiornamento |
| **Non aggiornato** | Le letture hanno smesso di arrivare. Lo schermo mostra l'ultima che ha ricevuto |
| **Apex retry 12s** | Il tuo Apex non ha risposto. Cora Max riprova quando finisce il conto alla rovescia |
| **Sincronizzazione cloud non riuscita** | Il tuo Apex ha risposto, ma le sue letture non hanno potuto essere salvate su Cora Cloud, quindi la dashboard rimane indietro. Cora Max continua a riprovare |
| **Offline** | Nessuna connessione. Lo schermo mostra gli ultimi dati che ha ricevuto |
| **Offline, riprova in 45s** | La tua rete è attiva, ma Cora Cloud è stato irraggiungibile per più di 30 secondi. Cora Max si riconnette da solo; il conto alla rovescia è il tempo fino al prossimo tentativo |
| **Cora principale offline** | Questo schermo è un secondo Cora Max per questa vasca, e il **Cora Max principale** (quello fissato per interrogare l'equipaggiamento di questa vasca) è andato offline. Questo schermo continua a mostrare gli ultimi dati che ha finché il principale non torna, oppure finché non scegli un Cora Max principale diverso. Vedi [Più di un dispositivo Cora](/help/mobile-multi-device) |
| **Password Apex** | Il tuo Apex ha rifiutato la password memorizzata. Vedi [Risoluzione dei problemi](/help/troubleshooting) |

:::note Come funziona il conto alla rovescia dei tentativi
Cora Max cerca di riconnettersi a un ritmo fisso: circa 15 secondi dopo la prima interruzione, 15 secondi dopo quello, poi due volte a 30 secondi, poi una volta al minuto finché non riesce. Non riprova istantaneamente e non si arrende; uno schermo che mostra **Offline, riprova in 45s** sta facendo esattamente ciò che dovrebbe.
:::

:::warning Cora Assistant inizia ad ascoltare immediatamente
Toccare l'icona di Cora Assistant avvia una sessione vocale in tempo reale. Se volevi aprire le impostazioni, quella è la rotella all'estrema destra.
:::

## La dashboard

Il resto dello schermo è la dashboard: una griglia fissa di widget, tutti visibili contemporaneamente. La dashboard di Cora Max non scorre.

I widget funzionano come sul tuo telefono, a una dimensione che puoi leggere stando a distanza. Vedi **[Guida di riferimento ai widget](/help/mobile-widgets)** per cosa mostra ogni forma, e **[Modificare la dashboard di Cora Max](/help/max-dashboard-editing)** per cambiare cosa c'è sopra.

Ogni widget che mostra un parametro misurato porta la sua **età** e la sua **fonte**, proprio come sul telefono. Un numero con `2d` accanto ha due giorni, ed è mostrato come tale. I riquadri di dispositivo e controllo mostrano invece il proprio stato.

## Il menu della vasca

![Il menu della vasca](img/max-menu.webp "Tutto per la vasca attuale, dal nome della vasca nella barra superiore.")

Toccare il nome della vasca apre il menu per la vasca attualmente sullo schermo:

| Voce | Apre |
|---|---|
| **Registra parametri** | Inserisci letture del kit di test sulla tastiera a schermo |
| **Diario** | [Il diario](/help/mobile-journal) per questa vasca |
| **Reef Buddy** | Il [briefing](/help/mobile-reef-buddy) attuale |
| **Report di salute** | Valutazioni di salute |
| **Manutenzione** | L'[elenco delle attività](/help/mobile-maintenance) |
| **Report ICP** | I [risultati di laboratorio](/help/mobile-icp-health) caricati |
| **Avvisi** | La fascia sana per ogni metrica su questa vasca |
| **Popolazione** | L'[inventario](/help/mobile-livestock) di questa vasca, di sola lettura su questo schermo |
| **Attività** | [Ogni presa, alimentazione e dosaggio](/help/max-activity), e cosa ne è risultato |
| **Layout dashboard** | [Disponi i widget su questo schermo](/help/max-dashboard-editing) |
| **Impostazioni vasca** | La schermata completa delle impostazioni per questa vasca |

## Cambiare vasca

Usa **l'icona della griglia** all'estrema sinistra della barra superiore per raggiungere [la Stanza della Vasca](/help/max-reef-room), poi apri la vasca che vuoi. Ogni vasca mantiene il proprio layout di dashboard, quindi l'intero schermo cambia mentre passi da una all'altra.

## Il cassetto Prese e Alimentazione

La scheda in fondo allo schermo tira su un cassetto con ogni presa del sistema e i controlli di alimentazione.

- **Prese**: ognuna commutabile tra Auto, Off e On
- **Alimenta**: sospende l'equipaggiamento giusto per un'alimentazione e ripristina tutto dopo

:::warning Questo cassetto controlla equipaggiamento reale
Tutto quanto contiene agisce su equipaggiamento reale. Un comando viene inviato nel momento in cui tocchi, ma *inviato* non è *fatto*; torna Confermato, Non confermato, Rifiutato o Nessun cambiamento, e [Attività](/help/max-activity) è dove vedi quale. La modalità alimentazione è il modo sicuro per sospendere il flusso per l'alimentazione, perché ripristina tutto da sola; uno spegnimento manuale resta spento finché non lo cambi di nuovo.
:::

## Se qualcosa sembra fuori posto

Se le letture sembrano obsolete, o la pillola di stato è ambra o rossa, inizia con **[Risoluzione dei problemi](/help/troubleshooting)**.
