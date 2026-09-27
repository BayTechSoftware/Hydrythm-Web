---
title: Leggere la dashboard
description: Come leggere la dashboard di Cora: widget, aggiornamenti, fonti e significato dei colori.
section: Cora Mobile
reviewed: 2026-09-09
order: 5
group: Your dashboard
---

La dashboard è una griglia di **widget**. Ogni widget mostra una cosa di una vasca. Cosa metterci lo decidi tu, come spiegato in **[Modificare la dashboard](/help/mobile-dashboard-editing)**.

![Una dashboard di Cora Mobile](img/mobile-dashboard.webp "Indicatori, numeri, tendenze e controlli in un'unica schermata.")

## L'intestazione della vasca

In cima a ogni dashboard trovi:

- **Il nome della vasca** con un piccolo simbolo accanto, che serve solo a **rinominarla al volo**
- **Alimenta**, che ferma movimento e schiumatoio per il pasto e poi rimette tutto com'era
- **Reef Buddy**, che apre il briefing di stamattina
- **Condividi**, che invia un'istantanea della dashboard
- **La matita a destra**, che apre [il profilo della vasca](/help/mobile-tank-profile)

:::note Tre comandi simili, tre schermate diverse
Il simbolo accanto al nome rinomina la vasca. La matita a destra apre il **profilo** della vasca. Per modificare la dashboard invece tocca **Modifica dashboard**, in *fondo* alla dashboard sotto i widget.
:::

Se hai più vasche, scorri di lato per passare dall'una all'altra.

## La scheda di Reef Buddy

Sotto l'intestazione c'è una scheda con il riassunto dell'ultimo briefing: un titolo, i punteggi **Stabilità** e **Dati** e il numero di osservazioni. Toccala per aprire il briefing completo, oppure chiudila con **×**. Con il briefing successivo arriva una nuova scheda.

## Come si legge un widget di parametro

Un widget che mostra un **parametro misurato** ha sempre le stesse tre cose negli stessi punti. I riquadri di dispositivi e comandi (una presa, un'unità di dosaggio, una pompa) mostrano invece il loro stato, perché dietro non c'è una singola lettura.

**Il valore** è la lettura, grande e al centro.

**L'età** è sotto o accanto al valore: `now`, `1h`, `2d`. Indica quanto tempo fa è stata presa la lettura, non quando si è aggiornato lo schermo. Un numero fermo da due giorni mostra `2d`, e anche questo ti dice qualcosa.

**Il badge della fonte** è il piccolo segno vicino all'età. Ti dice da dove arriva il numero: una sonda, un controller, un risultato di laboratorio o un tuo test. Tocca un widget per vedere la fonte per esteso e lo storico recente.

:::note L'età conta
Una lettura di alcalinità perfetta di quattro giorni fa non è una lettura attuale. L'età è accanto a ogni valore, così vedi subito la differenza.
:::

## Colori

Cora usa pochi colori, e ognuno ha sempre lo stesso significato:

| Colore | Significato |
|---|---|
| Verde | Ben dentro l'intervallo del parametro |
| Ambra | Vicino a un limite. **Di solito ancora dentro l'intervallo**, nell'ultimo decimo |
| Rosso | Oltre il limite. Conviene intervenire |
| Grigio | Nessun giudizio: non ci sono letture recenti o manca un intervallo per valutare |

:::note Ambra di solito vuol dire "ancora a posto, ma si sta spostando"
L'ambra è un *margine*: il limite non è ancora superato. Una lettura dentro l'intervallo, ma nell'ultimo 10%, diventa ambra. Così vedi la deriva quando hai ancora tempo per intervenire, prima che diventi un problema.

Ci sono due eccezioni.

**Un intervallo impostato da te vale come confine netto.** Se lo superi, il widget passa subito al rosso senza margine ambra, perché quella linea l'hai tracciata tu. Un intervallo **fornito da Cora** è un riferimento più morbido. Per il primo 10% oltre il limite il widget è ambra, poi diventa rosso.

**Un limite su un solo lato** (un tetto per un contaminante o un minimo per un nutriente) viene valutato solo sul lato alto. Per questo il rame a zero resta verde e non diventa ambra solo perché è in fondo alla scala.
:::

Un widget con il bordo ambra o rosso chiede attenzione. Il bordo circonda tutto il widget, quindi lo noti anche mentre scorri.

## Sotto i widget

![Il fondo della dashboard](img/mobile-dashboard-foot.webp "Modifica dashboard, Registra parametri, e scorciatoie alle quattro aree di registro.")

In fondo alla dashboard trovi:

- **Modifica dashboard**, che apre l'[editor della dashboard](/help/mobile-dashboard-editing)
- **Registra parametri**, per inserire a mano i risultati dei test
- **Diario · Avvisi · Manutenzione · Popolazione**, scorciatoie a queste sezioni per la vasca

Una riga sopra indica quando si è aggiornata la dashboard l'ultima volta e quali fonti ha usato.

## Toccare per i dettagli

Tocca un widget per aprire i dettagli: lo storico completo in un grafico, tutte le fonti che hanno misurato il parametro e le soglie attive. Da lì puoi registrare a mano una nuova lettura, cambiare l'intervallo o guardare più indietro nel tempo.

## Se un widget è vuoto

Un widget mostra un valore quando ne riceve uno. Se è vuoto, di solito il motivo è uno di questi:

- Il dispositivo è offline. Controlla la scheda **Dispositivi**
- Il parametro non ha ancora una fonte. Registralo a mano o collega un'attrezzatura che lo misura
- Il parametro non è mai stato misurato né registrato

Una lettura vecchia non sparisce se il grafico copre un periodo più corto della sua età. Resta sul widget con la sua età, così capisci che è vecchia e non la scambi per un dato mancante.

Per tutto il resto guarda **[Risoluzione dei problemi](/help/troubleshooting)**.
