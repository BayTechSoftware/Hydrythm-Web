---
title: Dispositivi e salute dei dispositivi
description: Cosa può vedere Cora Max, quale dispositivo interroga ogni vasca, e cosa controllare quando l'interrogazione si ferma.
section: Cora Max
reviewed: 2026-09-27
order: 7
group: Equipment
---

**Impostazioni → Dispositivi** elenca l'equipaggiamento che Cora Max può vedere e riporta come sta andando.

## L'elenco dei dispositivi

![L'elenco dei dispositivi](img/max-devices.webp "Filtra per vasca, poi ogni dispositivo con un riepilogo di una riga di cosa contiene.")

Cora Max vede lo stesso equipaggiamento del tuo telefono, perché entrambi leggono lo stesso account.

I chip di filtro in alto restringono l'elenco a **Tutte le vasche** o a una vasca. Ogni voce porta un punto di stato, un riepilogo di una riga di cosa contiene il dispositivo (*21 prese · 4 alimentazioni*, *19 test rimasti*) e la vasca a cui appartiene.

Aggiungere e configurare l'equipaggiamento è più facile sul telefono; vedi [Aggiungere, modificare e rimuovere dispositivi](/help/mobile-devices).

## Cora Max principale: quale tablet parla con il tuo equipaggiamento

**Cora Max principale** è il tablet (o altro dispositivo Cora) che legge il controller di una vasca e l'altro equipaggiamento per tutto l'account. Solo un dispositivo deve farlo per vasca; ogni altro schermo mostra semplicemente ciò che legge.

Apri **Impostazioni → [la tua vasca] → Cora Max principale** per vederlo o cambiarlo. Ci sono due tipi di scelta:

- **Qualsiasi attivo (automatico)**: ogni dispositivo Cora online che può raggiungere l'equipaggiamento di questa vasca condivide il lavoro, e vince la scrittura più recente. Questa è l'impostazione da usare a meno che tu non abbia un motivo specifico per fissare un dispositivo.
- **Fissa un dispositivo**: interroga solo quello. Se il dispositivo fissato va offline, nulla interroga l'equipaggiamento di questa vasca finché non ne fissi uno diverso, oppure torni a Qualsiasi attivo (automatico).

Questa scelta si fa una volta, per la vasca, non una volta per ogni schermo Cora. Cambiala da qualsiasi Cora Max che mostra quella vasca, oppure da Cora Mobile; vedi [Più di un dispositivo Cora](/help/mobile-multi-device).

:::note Il Cora Max principale non è la stessa cosa di Cora Assistant
Il Cora Max principale decide quale dispositivo **legge il tuo equipaggiamento**. Un'impostazione separata, **Cora Assistant**, decide quale dispositivo **risponde a "Hey Cora"**. Una casa con più di un Cora Max può impostare queste due indipendentemente. Vedi [Parlare con Cora](/help/max-voice).
:::

## Se le letture di una vasca si fermano

Se le letture di una vasca si fermano mentre un'altra vasca sullo stesso schermo continua ad aggiornarsi, inizia con:

1. **Impostazioni → [quella vasca] → Cora Max principale**: conferma che un dispositivo sia effettivamente assegnato, e che sia online.
2. Se un Cora Max secondario per questa vasca mostra la pillola **Cora principale offline** nella sua barra superiore, il principale ha perso la sua connessione; vedi [La schermata Home di Cora Max](/help/max-tour) per cosa significa la pillola di stato.
3. **Impostazioni → Impostazioni Cora Max → Rete e aggiornamenti → Polling dispositivi** mostra ogni quanto questa unità stessa legge i tuoi dispositivi; questo valore è di sola lettura qui e si imposta da Cora Mobile.

**Se non funziona:** vedi [Risoluzione dei problemi](/help/troubleshooting).

## Gestire un Cora Max dal tuo telefono

Apri l'unità dalla scheda **Dispositivi** del tuo telefono per vedere la sua variante, la versione del firmware e quando è stata vista l'ultima volta, e per rinominarla o cambiare alcune delle sue impostazioni senza camminare fino ad essa.

![Impostazioni di Cora Max dal telefono](img/max-from-phone.webp "Intervallo di polling, luminosità, volume, avvisi a schermo e timer di attenuazione.")

Le impostazioni mostrate in questo modo descrivono **solo questo schermo** (la sua luminosità, volume, banner di avviso a schermo e timer di attenuazione), allo stesso modo in cui le cambieresti alla parete. Disattivare gli avvisi a schermo non influisce sullo storico degli avvisi o sulle notifiche push.

Quali vasche mostra un Cora Max, e quale è il suo Cora Max principale per ogni vasca, sono scelte a livello di account; cambiale da entrambi i dispositivi, come descritto sopra.

:::note La salute del dispositivo è prima di lettura
La sezione **Stato** di **Impostazioni → Impostazioni Cora Max** su questo schermo riporta lo stato del polling, l'ultimo orario di polling e l'ultima scrittura cloud per ogni vasca, senza cambiare nulla. Usala per stabilire cosa sta succedendo prima di modificare un'impostazione.
:::
