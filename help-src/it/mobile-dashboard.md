---
title: Leggere la tua dashboard
description: Come leggere la dashboard di Cora: widget, aggiornamento, fonti e cosa significano i colori.
section: Cora Mobile
reviewed: 2026-09-09
order: 5
group: Your dashboard
---

La dashboard è una griglia di **widget**, ognuno dei quali mostra una cosa su una vasca. Cosa c'è sopra dipende interamente da te; vedi **[Modificare la tua dashboard](/help/mobile-dashboard-editing)**.

![Una dashboard di Cora Mobile](img/mobile-dashboard.webp "Indicatori, numeri, tendenze e controlli in un'unica schermata.")

## L'intestazione della vasca

In alto su ogni dashboard:

- **Il nome della vasca**, con un piccolo simbolo accanto: quello è una **rinomina rapida**, niente di più
- **Alimenta**: sospende il flusso e lo skimmer per un'alimentazione, poi ripristina tutto
- **Reef Buddy**: apre il briefing di questa mattina
- **Condividi**: invia uno snapshot della dashboard
- **La matita a destra**: apre [il profilo della vasca](/help/mobile-tank-profile)

:::note Tre controlli simili, tre destinazioni
Il simbolo accanto al nome rinomina la vasca. La matita a destra apre il **profilo** della vasca. Modificare la dashboard stessa non è né l'una né l'altra cosa; è **Modifica dashboard**, in *fondo* alla dashboard, sotto i widget.
:::

Con più di una vasca, scorri lateralmente per passare da una all'altra.

## La scheda di Reef Buddy

Sotto l'intestazione, una scheda riassume il briefing più recente: un titolo, i suoi punteggi **Stabilità** e **Dati**, e il numero di insight. Toccala per aprire il briefing completo, oppure chiudila con **×**. Una nuova scheda apparirà con il briefing successivo.

## Come leggere un widget di parametro

Un widget che mostra un **parametro misurato** porta le stesse tre cose nelle stesse posizioni. I riquadri di dispositivi e controlli (una presa, un'unità di dosaggio, una pompa) mostrano invece il proprio stato, perché non c'è un'unica lettura dietro di essi.

**Il valore** è la lettura stessa, grande e centrale.

**L'età** si trova sotto o accanto ad esso: `now`, `1h`, `2d`. Questo è da quanto tempo è stata presa la lettura, non da quanto tempo si è aggiornato lo schermo. Un numero che non si è mosso in due giorni mostra `2d`, e questa è un'informazione.

**Il badge della fonte** è il piccolo segno accanto all'età. Ti dice da dove viene il numero: una sonda, un controller, un risultato di laboratorio, oppure tu con un kit di test. Tocca qualsiasi widget per vedere la fonte esplicitata insieme al suo storico recente.

:::note Perché l'età conta così tanto
Una lettura perfetta di alcalinità di quattro giorni fa non è una lettura attuale di alcalinità. L'età si trova accanto a ogni valore così puoi cogliere la differenza a colpo d'occhio.
:::

## Colori

Cora usa il colore con parsimonia, e sempre per significare la stessa cosa:

| Colore | Significato |
|---|---|
| Verde | Comodamente dentro l'intervallo per questo parametro |
| Ambra | Vicino a un limite: **di solito ancora dentro l'intervallo**, entro l'ultimo decimo di esso |
| Rosso | Oltre il limite, e da tenere in considerazione |
| Grigio | Nessun giudizio: nessuna lettura recente, oppure nessun intervallo utilizzabile per valutare |

:::note L'ambra di solito significa "ancora a posto, ma in movimento verso qualcosa"
L'ambra è un *margine*, non una violazione. Una lettura dentro il suo intervallo ma entro l'ultimo 10% di esso diventa ambra deliberatamente, così la deriva è visibile mentre c'è ancora tempo per agire invece che nel momento in cui diventa un problema.

Da questo derivano due precisazioni.

**Un intervallo che imposti tu stesso viene trattato come un confine dichiarato.** Superalo e il widget passa direttamente al rosso: nessun margine ambra, perché quella linea l'hai tracciata deliberatamente. Un intervallo **fornito da Cora** è un riferimento più morbido: superarlo mostra l'ambra per il primo 10% oltre il limite, e diventa rosso oltre quello.

**Un limite a un solo lato** (un tetto per un contaminante, o un minimo per un nutriente) viene valutato solo sul suo lato alto, così il rame a zero appare verde invece di diventare ambra per il trovarsi vicino al fondo della scala.
:::

Un widget con contorno ambra o rosso è uno che richiede attenzione. Il contorno è sul widget, non solo sul numero, così è visibile mentre scorri.

## Sotto i widget

![Il fondo della dashboard](img/mobile-dashboard-foot.webp "Modifica dashboard, Registra parametri, e scorciatoie alle quattro aree di registro.")

In fondo alla dashboard:

- **Modifica dashboard**: apre l'[editor della dashboard](/help/mobile-dashboard-editing)
- **Registra parametri**: inserisci a mano le letture del kit di test
- **Diario · Avvisi · Manutenzione · Popolazione**: scorciatoie a quelle aree per questa vasca

Una riga sopra di essi mostra quando la dashboard si è aggiornata l'ultima volta e su quali fonti si è basata.

## Toccare per approfondire

Tocca qualsiasi widget per aprire i suoi dettagli: lo storico completo come grafico, ogni fonte che lo ha riportato, e le soglie attualmente applicate. Da lì puoi registrare a mano una nuova lettura, cambiare l'intervallo, o guardare più indietro nel tempo.

## Se un widget non ha valore

Un widget mostra un valore una volta che ne riceve uno. Quando è vuoto, il motivo di solito è uno di questi:

- Il dispositivo è offline; controlla la scheda **Dispositivi**
- Il parametro non ha ancora una fonte; registralo a mano, oppure collega un equipaggiamento che lo riporta
- Il parametro non è mai stato riportato o registrato; non è stato ancora registrato nulla per esso

Una lettura vecchia non svanisce perché la finestra del grafico è più corta della sua età. Resta sul widget con la sua età mostrata, così un valore obsoleto si legge come obsoleto invece che come mancante.

Vedi **[Risoluzione dei problemi](/help/troubleshooting)** per qualsiasi cosa oltre a queste.
