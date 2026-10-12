---
title: Approfondire un parametro
description: Tocca un widget per vedere lo storico completo, tutte le fonti che misurano il parametro e dove cambiarne l'intervallo.
section: Cora Mobile
reviewed: 2026-10-12
order: 8
group: Your dashboard
---

Il widget ti mostra un numero. Se lo tocchi, vedi la storia che c'è dietro.

Ci sono due modi per arrivarci. Tocca un widget nella dashboard, oppure tocca **Storico parametri** nella riga di pulsanti sotto i widget e scegli un parametro. **Storico parametri** elenca ogni parametro che ha dati, anche uno senza widget nella dashboard.

## Cosa trovi

![Approfondire un parametro](img/mobile-metric-detail.webp "I menu a tendina in alto, poi il grafico con la tua fascia di avviso ombreggiata.")

**Un grafico dello storico.** Tre menu a tendina sopra il grafico impostano cosa mostra. **Parametro** passa a qualsiasi altro parametro che ha dati e mantiene il periodo. **Periodo** va da 1h a 6h, 12h, 24h, 3d, 7d, 15d, 30d, 90d, 180d e 360d fino a Tutto. **Fonte** parte da **Tutte le fonti** ed elenca le fonti che misurano questo parametro in questa vasca, per esempio *Apex*, *Cora*, *Red Sea* o *Manuale*. Scegline una per vedere solo le sue letture. Così confronti una sonda con un test: passi dall'una all'altro sullo stesso grafico.

La schermata si apre sempre su 24h e **Tutte le fonti**. Non ricorda quello che avevi scelto l'ultima volta.

**Un collegamento al calcolatore di dosaggio**, per i parametri che dosi. Usa il volume indicato nel [profilo della vasca](/help/mobile-tank-profile) e le concentrazioni impostate in [Dosaggio](/help/mobile-dosing).

**Un confronto sovrapposto.** Con **Confronta** disegni un secondo parametro sullo stesso grafico (alcalinità e calcio, pH e temperatura). L'elenco ha tutti i parametri che la vasca possiede. Se sospetti un legame tra i due, lo vedi a colpo d'occhio. Tocca di nuovo il chip per togliere la seconda linea.

**Statistiche del periodo** visualizzato: una riga con **Ultimo**, **Min**, **Media** e **Max**.

**Indicatori di dosaggio** sul grafico, per confrontare un movimento con quello che hai dosato davvero.

**L'elenco delle letture originali**: tutte le singole letture che formano la linea, ciascuna con fonte e orario.

**La fascia di avviso**, ombreggiata sul grafico, così ogni lettura si legge rispetto al suo intervallo. Per cambiare l'intervallo, tieni premuto il widget sulla dashboard. I dettagli sono in [Avvisi e soglie](/help/mobile-alerts).

**Registra una lettura** a mano.

## Scegliere il periodo

Il periodo giusto dipende dal ritmo del parametro:

| Parametro | Periodo utile |
|---|---|
| pH | 24 ore, perché varia nel corso della giornata |
| Temperatura | 24 ore o 7 giorni |
| Alcalinità | 7 o 30 giorni |
| Elementi in traccia | 30 giorni o un anno |

:::note Se la linea è piatta, guarda l'età della lettura
Una linea ferma può voler dire che il parametro è stabile o che la fonte ha smesso di mandare dati. L'età accanto al valore ti dice quale dei due.
:::

## Confrontare le fonti

Quando più fonti misurano lo stesso parametro, Cora le tiene separate e non ne fa la media. Usa il menu a tendina **Fonte** per vederle una alla volta.

Quella che compare nella dashboard è la più recente. Un valore in diretta viene sostituito solo da una lettura con un orario di misura più recente, da qualsiasi fonte. Una lettura più vecchia va nello storico e non sovrascrive quello che c'è sul widget. Se hai fissato una fonte per il widget, Cora segue invece quella fonte.

Se tra una sonda e un test registrato a mano c'è una differenza costante, di solito la sonda va calibrata.

Un [risultato ICP](/help/mobile-icp-health) è un utile terzo parere, ma non un giudice. I laboratori danno risultati diversi tra loro, e il risultato cambia anche in base a come il campione viene trattato, conservato e spedito. Considera un singolo ICP come un indizio e non come il valore vero. Due test che concordano valgono molto più di uno.

## Scegliere la fonte di un widget

Se vuoi che un widget segua una fonte precisa, impostala nelle impostazioni del widget. Vedi **[Modificare la dashboard](/help/mobile-dashboard-editing)**.

## Escludere una lettura sbagliata

Un picco della sonda, un test letto male, un campione preso durante un cambio d'acqua: basta una lettura sbagliata per falsare il grafico, le medie e tutti i ragionamenti basati su di loro.

![L'elenco delle letture originali](img/mobile-readings.webp "Ogni lettura dietro la linea, con la sua fonte e il suo orario.")

Apri l'elenco delle letture dall'icona nella barra in alto e tocca una lettura per escluderla. La schermata lo dice chiaramente: *esclusa dalle medie e dagli insight, ma resta nel tuo registro.* Non viene cancellato nulla e puoi ripristinarla.

:::warning Escludi le letture sbagliate, non quelle che non ti piacciono
L'esclusione serve per le letture che sai essere non valide. Una lettura che non ti piace ma che non ha niente di sbagliato è un dato. Se la togli, tutti i confronti successivi diventano meno onesti.
:::

## Registrare la cura delle sonde

Se registri da qui una calibrazione o una pulizia, la data resta associata a quella fonte. Così, se più avanti le fonti non concordano, sai quando è stata sistemata la sonda l'ultima volta. Vedi [Sonde](/help/mobile-probes).

## Registrare una lettura a mano

Inserisci il risultato del tuo test. L'elenco è raggruppato, e il gruppo **Oligoelementi** comprende iodio, ferro e rame in µg/L, e potassio in mg/L. Le letture inserite a mano valgono come tutte le altre: hanno fonte e orario, compaiono sul grafico, arrivano a Reef Buddy, e Cora le usa come riferimento per la tua attrezzatura.

:::note Cora ricontrolla i valori strani
Se un valore è molto lontano da quelli registrati finora, Cora ti chiede di confermarlo prima di salvarlo. Così intercetta una virgola al posto sbagliato o una lettura inserita nel parametro sbagliato. Se confermi, la lettura viene salvata normalmente.
:::
