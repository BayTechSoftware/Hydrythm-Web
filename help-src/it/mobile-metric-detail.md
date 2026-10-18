---
title: Approfondire un parametro
description: Tocca un widget per vedere lo storico completo di un parametro, confrontare fonti e parametri, escludere una lettura sbagliata e registrare la cura delle sonde.
section: Cora Mobile
reviewed: 2026-10-17
order: 7
group: Your dashboard
---

Un widget ti mostra un numero. Toccalo per vedere la storia che c'è dietro.

Ci sono due modi per arrivarci. Tocca un widget sulla dashboard, oppure tocca **Storico parametri** nella fila di pulsanti sotto i widget e scegli un parametro. **Storico parametri** elenca ogni parametro che ha dati, anche uno senza widget sulla dashboard.

## Cosa trovi {#what-you-get}

![Approfondire un parametro](img/mobile-metric-detail.webp "I menu a tendina in alto, poi il grafico con la fascia di avviso ombreggiata.")

- Un grafico dello storico. La riga sopra il grafico imposta cosa mostra. **Parametro** passa a qualsiasi altro parametro che ha dati e mantiene il periodo. **Periodo** va da 1h passando per 6h, 12h, 24h, 3d, 7d, 15d, 30d, 90d, 180d e 360d fino a Tutto. **Fonte** parte da **Tutte le fonti** ed elenca le fonti che riportano questo parametro su questa vasca, come *Apex*, *Cora*, *Red Sea* o *Manuale*. Scegline una per vedere solo le sue letture.
- **Confronta**, alla fine della stessa riga, disegna un secondo parametro sul grafico, come alcalinità con calcio o pH con temperatura. Il pulsante diventa allora **vs** seguito dal nome dell'altro parametro. Toccalo di nuovo per togliere la seconda linea.
- Una riga con **Ultimo**, **Min**, **Media** e **Max** per il periodo sullo schermo.
- Icone nella barra in alto: **Letture** apre l'elenco delle letture originali, e **Registra cura della sonda** registra una calibrazione o una pulizia. Per alcalinità, calcio e magnesio c'è anche il calcolatore di dosaggio, che usa il volume della vasca dal [profilo della vasca](/help/mobile-tank-profile) e le concentrazioni da [Dosaggio](/help/mobile-dosing).

La schermata si apre sempre su 24h e **Tutte le fonti**. Non ricorda quello che hai scelto l'ultima volta.

Il peso specifico (SG) mostra sempre tre o quattro decimali, quindi 1,022 non diventa 1,02. È uguale in Cora Mobile e Cora Max, sulla dashboard, nel grafico e nell'elenco delle letture.

## Leggere il grafico {#reading-the-chart}

- La fascia verde è il tuo intervallo di avviso, così vedi ogni lettura rispetto a quello. Per cambiare l'intervallo, tieni premuto il widget sulla dashboard. Di più in [Avvisi e soglie](/help/mobile-alerts).
- Una linea tratteggiata segna una dose registrata, così puoi mettere in relazione un cambiamento con quello che hai dosato.
- **massimo 30g** e **minimo 30g** sono linee tratteggiate con gli estremi degli ultimi 30 giorni.
- Un pallino vuoto è una lettura che hai escluso.
- Con **Confronta** attivo, il secondo parametro usa l'asse di destra.

## Scegliere il periodo {#choosing-a-range}

Scegli il periodo adatto al modo in cui si muove il parametro.

| Parametro | Periodo utile |
|---|---|
| pH | 24 ore, perché oscilla con un ciclo giornaliero |
| Temperatura | 24 ore o 7 giorni |
| Alcalinità | 7 o 30 giorni |
| Elementi in traccia | 30 giorni o un anno |

:::note Linea piatta? Controlla l'età della lettura
Una linea che non si muove può voler dire che il parametro è stabile. Può anche voler dire che la fonte ha smesso di inviare dati. L'età accanto al valore sul widget ti dice quale dei due.
:::

## Confrontare le fonti {#comparing-sources}

Quando più di una fonte riporta un parametro, Cora le tiene separate e non ne fa la media. Usa il menu a tendina **Fonte** per guardarle una alla volta. È il modo più veloce per confrontare una sonda con un test.

Quella che compare sulla dashboard è la più recente. Un valore in tempo reale viene sostituito solo da una lettura con un orario di misura successivo, da qualsiasi fonte. Una lettura più vecchia va nello storico e non sovrascrive quello che c'è sul widget. Se hai fissato una fonte in **Mappatura parametri**, Cora segue invece quella fonte.

Se una sonda e i tuoi test registrati a mano restano distanti della stessa quantità, di solito la sonda va calibrata.

Un [risultato ICP](/help/mobile-icp-health) è un utile terzo parere, ma non chiude la questione. I laboratori differiscono tra loro, e il modo in cui il campione è stato trattato, conservato e spedito cambia il risultato. Considera un ICP come un indizio. Due test che concordano valgono molto più di uno.

## Scegliere quale fonte segue una lettura {#choosing-which-source-a-widget-trusts}

La fonte si imposta per vasca e per parametro, non per widget. Vai in **Impostazioni**, tocca la vasca, tocca **Mappatura parametri**, poi la scheda **Fonti**. Scegli una sonda, oppure **Automatico (vince la lettura più recente)**. La scelta vale per quel parametro ovunque nella vasca. Di più in [Mappatura parametri](/help/mobile-probes).

## Escludere una lettura sbagliata {#excluding-a-bad-reading}

Magari una sonda ha avuto un picco, hai letto male un test o hai preso il campione nel mezzo di un cambio d'acqua. Una sola lettura sbagliata falsa il grafico, le medie e tutto quello che ne deriva.

![L'elenco delle letture del pH in Cora Mobile](img/mobile-readings.webp "Ogni lettura dietro la linea, con il suo orario e la sua fonte. Toccane una per escluderla.")

Tocca **Letture** nella barra in alto, poi tocca una lettura. Cora chiede **Escludere questa lettura?** e spiega che resta nel tuo registro ma smette di contare per medie, tendenze, approfondimenti e per l'assistente. Tocca **Escludi**. Non viene cancellato niente, e puoi ripristinarla allo stesso modo.

Le letture più vecchie di 90 giorni non si possono escludere né ripristinare.

:::warning Escludi le letture sbagliate, non quelle sgradite
Escludi solo una lettura che sai essere non valida. Se una lettura semplicemente non ti piace ma non trovi niente di sbagliato, è un dato reale. Toglierla rende meno onesti tutti i confronti successivi.
:::

## Registrare la cura delle sonde {#recording-probe-care}

Tocca **Registra cura della sonda** (l'icona del sensore nella barra in alto) e scegli cosa hai fatto: calibrare, pulire, sostituire, spostare o confrontare. Cora mette la data su quella fonte, così una calibrazione appena fatta non viene scambiata per una deriva. Più avanti, se la sonda non concorda con qualcosa, puoi vedere quando è stata curata l'ultima volta. Di più in [Mappatura parametri](/help/mobile-probes).

## Registrare una lettura a mano {#logging-a-reading-by-hand}

Le letture si registrano dalla dashboard, non da questa schermata. Tocca **Registra parametri** sotto i widget e inserisci quello che dice il tuo test. L'elenco è raggruppato, e il gruppo **Oligoelementi** comprende iodio, ferro e rame in µg/L, e potassio in mg/L. Le letture registrate a mano contano come tutte le altre. Hanno una fonte e un orario propri, compaiono sul grafico e alimentano Reef Buddy. Sono anche il riferimento con cui Cora controlla la tua attrezzatura.

:::note Cora ricontrolla i valori strani
Se un valore è molto lontano da quelli della vasca finora, Cora ti chiede di confermarlo prima di salvarlo. Così intercetta una virgola al posto sbagliato, o una lettura inserita nel parametro sbagliato. Quando confermi, la lettura viene salvata come al solito.
:::
