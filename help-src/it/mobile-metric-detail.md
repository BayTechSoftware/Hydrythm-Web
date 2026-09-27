---
title: Approfondire un parametro
description: Tocca qualsiasi widget per lo storico completo, ogni fonte che lo riporta, e dove cambiare il suo intervallo.
section: Cora Mobile
reviewed: 2026-09-09
order: 8
group: Your dashboard
---

Un widget ti mostra un numero. Toccarlo ti mostra la storia dietro il numero.

## Cosa ottieni

![Approfondire un parametro](img/mobile-metric-detail.webp "Intervalli in alto, poi le fonti che riportano questo parametro, poi il grafico con la tua fascia di avviso ombreggiata.")

**Un grafico storico**, con il proprio selettore di intervallo: **1h · 6h · 12h · 24h · 3d · 7d** e periodi più lunghi.

**Un filtro per fonte.** Sotto gli intervalli c'è una riga di chip: **Tutte**, più una per ogni fonte che riporta questo parametro, come *Apex*, *Cora*, *Red Sea* o *Manuale*. Selezionane una per vedere solo le sue letture. È così che confronti una sonda con un kit di test direttamente: passa da una all'altra sullo stesso grafico.

**Un link al calcolatore di dosaggio**, per i parametri che dosi. Usa il volume della vasca dal tuo [profilo della vasca](/help/mobile-tank-profile) e le concentrazioni da [Dosaggio](/help/mobile-dosing).

**Una sovrapposizione di confronto.** *Confronta con* traccia un secondo parametro sullo stesso grafico (alcalinità contro calcio, pH contro temperatura), così una relazione che sospetti diventa visibile invece che ricordata.

**Statistiche di riepilogo** per il periodo sullo schermo: **MIN**, **MEDIA** e **MAX**, mostrate come una riga sotto il valore attuale.

**Segnalatori di dosaggio** sul grafico, così un movimento può essere confrontato con ciò che hai effettivamente dosato.

**L'elenco delle letture originali**: ogni singola lettura dietro la linea, con la sua fonte e il suo orario.

**La tua fascia di avviso**, ombreggiata sul grafico, così una lettura viene letta rispetto al suo intervallo invece che isolatamente. Per cambiare l'intervallo stesso, tieni premuto il widget sulla dashboard. Vedi [Avvisi e soglie](/help/mobile-alerts).

**Registra una lettura** a mano.

## Scegliere un intervallo

L'intervallo giusto dipende dal ritmo del parametro:

| Parametro | Periodo utile |
|---|---|
| pH | 24 ore; oscilla su un ciclo giornaliero |
| Temperatura | 24 ore o 7 giorni |
| Alcalinità | 7 o 30 giorni |
| Elementi in traccia | 30 giorni o un anno |

:::note Controlla l'età della lettura su una tendenza piatta
Una linea che non si è mossa può indicare un parametro stabile oppure una fonte che ha smesso di riportare. L'età mostrata accanto al valore distingue i due casi.
:::

## Confrontare le fonti

Quando più di una fonte riporta un parametro, Cora le mantiene separate invece di farne una media. Usa i chip delle fonti per vedere ciascuna a turno.

Uno scostamento persistente tra una sonda e un test registrato a mano di solito indica che la sonda ha bisogno di calibrazione.

Un [risultato ICP](/help/mobile-icp-health) è una terza opinione utile, ma non un arbitro. I laboratori differiscono tra loro, e la manipolazione, la conservazione e il trasporto del campione influenzano tutti il risultato. Tratta un singolo ICP come una prova, non come il valore vero; due test in accordo valgono molto più di uno solo.

## Scegliere quale fonte segue un widget

Se vuoi che un widget segua una fonte particolare, impostalo nelle impostazioni del widget. Vedi **[Modificare la tua dashboard](/help/mobile-dashboard-editing)**.

## Escludere una lettura errata

Una sonda che ha avuto un picco, un test letto male, un campione preso a metà di un cambio d'acqua: una singola lettura sbagliata distorce il grafico, le medie e qualsiasi ragionamento che ne dipende.

![L'elenco delle letture originali](img/mobile-readings.webp "Ogni lettura dietro la linea, con la sua fonte e il suo orario.")

Apri l'elenco delle letture dall'icona nella barra superiore, poi tocca una lettura per escluderla. La schermata lo dice chiaramente: *esclusa dalle medie e dagli insight, ma resta nel tuo registro.* Nulla viene eliminato, e può essere ripristinata.

:::warning Escludi una lettura sbagliata, non una che non ti piace
Escludere serve per le letture che sai essere non valide. Una lettura che non ti piace ma che non puoi contestare è dato, e rimuoverla rende ogni confronto successivo meno onesto.
:::

## Registrare la cura delle sonde

Registrare una calibrazione o una pulizia da qui timbra la data su quella fonte, così un disaccordo successivo può essere letto rispetto a quando la sonda è stata vista l'ultima volta. Vedi [Sonde](/help/mobile-probes).

## Registrare una lettura a mano

Inserisci cosa dice il tuo kit di test. Le letture registrate a mano sono di prima classe: ottengono una propria fonte e orario, appaiono sul grafico, alimentano Reef Buddy, e sono ciò con cui Cora confronta il tuo equipaggiamento.

:::note Cora controlla le voci che sembrano implausibili
Se un valore è molto lontano da ciò che la vasca ha registrato finora, ti viene chiesto di confermarlo prima che venga salvato. Questo intercetta un punto decimale nel posto sbagliato o una lettura inserita nel parametro sbagliato. Confermala e la lettura viene memorizzata normalmente.
:::
