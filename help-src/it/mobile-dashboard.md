---
title: Leggere la dashboard
description: Come leggere la dashboard di Cora, dai widget, dall'età delle letture e dalle fonti al significato dei colori e alle schede che vanno e vengono.
section: Cora Mobile
reviewed: 2026-10-13
order: 6
group: Your dashboard
---

La dashboard è una griglia di **widget** per una vasca. Ogni widget mostra una cosa. Decidi tu cosa metterci, come spiegato in [Modificare la dashboard](/help/mobile-dashboard-editing).

![Una dashboard di Cora Mobile](img/mobile-dashboard.webp "L'intestazione della vasca e la scheda di Reef Buddy, poi indicatori, valori, grafici e riquadri dei dispositivi.")

## L'intestazione della vasca {#the-tank-header}

Ogni dashboard comincia con:

- Il nome della vasca, con un piccolo simbolo accanto. Tocca il nome per rinominare la vasca. Fa solo questo.
- **Alimenta**, solo su una vasca con un Neptune Apex. Apre la **Modalità alimentazione** con i cicli da **Alimentazione A** ad **Alimentazione D** del tuo Apex. È il tuo Apex a decidere cosa si mette in pausa e quando riparte, come l'hai impostato lì. Mentre un ciclo è in corso, il pulsante mostra quale, per esempio **Alimentazione A**. Toccalo e scegli **Annulla alimentazione** per terminarlo prima. Lontano da casa, un Cora Max nella vasca invia il comando per te.
- L'icona del giornale, che apre l'ultimo briefing di **Reef Buddy**.
- L'icona di condivisione, che crea un'istantanea della vasca. Vedi [Condividere la tua vasca](/help/mobile-sharing).
- Il righello, che apre **Unità** per questa vasca. Vedi [Il profilo della vasca](/help/mobile-tank-profile#units).
- La matita a destra, che apre il [profilo della vasca](/help/mobile-tank-profile).

:::note Tre comandi che si somigliano
Il nome della vasca rinomina la vasca. La matita a destra apre il **profilo** della vasca. Per modificare la dashboard stessa, tocca **Modifica dashboard** subito sotto i widget.
:::

Se hai più di una vasca, scorri di lato per passare dall'una all'altra. Vedi [Gestire le tue vasche](/help/mobile-tanks).

## La scheda di Reef Buddy {#the-reef-buddy-card}

Sopra i widget, una scheda riassume l'ultimo briefing. Mostra il titolo, un punteggio su 100 quando Cora ha abbastanza dati, la data a cui si riferisce e quante osservazioni e letture in deriva ci sono. Toccala per aprire il briefing completo, oppure chiudila con **×**. Con il briefing successivo compare una nuova scheda. Di più in [Reef Buddy](/help/mobile-reef-buddy).

## Come si legge un widget di parametro {#how-to-read-a-parameter-widget}

Un widget per un **parametro misurato** mostra sempre le stesse tre cose negli stessi punti. I riquadri di dispositivi e comandi, come una presa, un'unità di dosaggio o una pompa, mostrano invece il loro stato, perché dietro non c'è una singola lettura.

Il valore è la lettura stessa, grande e al centro.

L'età sta sotto o accanto al valore, come `now`, `1h` o `2d`. Indica quanto tempo fa la fonte ha confermato quel valore l'ultima volta, non quando si è aggiornato lo schermo. Per una sonda è quando il suo dispositivo si è fatto sentire l'ultima volta, quindi una lettura stabile da una sonda funzionante resta fresca anche quando il numero non cambia. Per un test o un risultato ICP è quando hai fatto il test. Un'età che continua a crescere su una sonda vuol dire che il suo dispositivo ha smesso di inviare dati.

Il badge della fonte è il piccolo segno accanto all'età. Mostra da dove arriva il numero: una sonda, un controller, un risultato di laboratorio, oppure tu con un test. Tocca il widget per vedere la fonte per esteso, con lo storico recente.

:::note Perché l'età conta
Una lettura di alcalinità perfetta di quattro giorni fa non è la tua alcalinità di oggi. Ogni valore mostra la sua età, così vedi subito la differenza.
:::

## Colori {#colours}

Cora usa pochi colori, e ognuno significa sempre la stessa cosa:

| Colore | Significato |
|---|---|
| Verde | Ben dentro l'intervallo di questo parametro |
| Ambra | Vicino a un limite. **Di solito ancora dentro l'intervallo**, nell'ultimo decimo |
| Rosso | Oltre il limite, e vale la pena intervenire |
| Grigio | Nessun giudizio. Non c'è una lettura recente, o non c'è un intervallo utile per valutarla |

:::note Ambra di solito vuol dire "a posto per ora, ma in deriva"
L'ambra è un margine. Una lettura dentro il suo intervallo ma nell'ultimo 10% diventa ambra, così vedi la deriva quando c'è ancora tempo per intervenire.

Ci sono due precisazioni.

**Un intervallo impostato da te è un confine netto.** Se lo superi, il widget passa subito al rosso, senza margine ambra. Un intervallo **fornito da Cora** è più morbido. Superarlo mostra ambra per il primo 10% oltre il limite, poi rosso.

**Un limite su un solo lato**, come un tetto per un contaminante o un minimo per un nutriente, viene valutato solo sul lato alto. Quindi il rame a zero è verde e non diventa ambra solo perché sta in fondo alla scala.
:::

Un widget con il bordo ambra o rosso richiede attenzione. Il bordo circonda tutto il widget, quindi lo noti mentre scorri.

Per cambiare un intervallo, tieni premuto il widget. Di più in [Avvisi e soglie](/help/mobile-alerts).

## Schede che vanno e vengono {#cards-that-come-and-go}

Alcune schede compaiono solo quando c'è qualcosa da dire. La maggior parte sta tra l'intestazione e i widget.

| Scheda | Quando compare | Cosa toccare |
|---|---|---|
| **Stai avviando una nuova vasca?** | Su una vasca senza nessuna lettura. Dopo che hai iniziato, diventa **Continua il ciclaggio** | La scheda, per avviare il ciclaggio guidato. Vedi [Percorsi guidati](/help/mobile-journeys) |
| **Parametri della vasca** con *Nessuna lettura ancora* | La vasca non ha ancora letture | **Configura vasca** |
| *Impossibile raggiungere le tue letture: vengono mostrati i dati in cache.* | Cora non riesce a caricare le ultime letture, spesso per mancanza di connessione | **Riprova** |
| **Un risultato di laboratorio da {lab} ti sta aspettando.** | Un laboratorio ha inviato un risultato e Cora deve sapere per quale vasca è | **Scegli vasca**. Vedi [ICP e report di salute](/help/mobile-icp-health) |
| Suggerimento del profilo (**Sblocca approfondimenti più intelligenti**) | Il profilo della vasca è completo per meno dell'80% | La scheda, per continuare con il profilo |
| **Prova Cora Pro: 9 giorni rimanenti** | Gli ultimi giorni della tua prova | La scheda, oppure **Mantieni Pro**. Vedi [Piani e abbonamenti](/help/mobile-plans) |
| **Reef Buddy** | Un briefing è pronto | La scheda |
| **Come nutri di solito?** | Non hai impostato una routine di alimentazione | **Imposta la routine** |
| *I valori Red Sea non si aggiornano più.* | Nessun dispositivo sta leggendo i dispositivi Red Sea di questa vasca | Vedi [Avvisi e soglie](/help/mobile-alerts) |
| **Telecamere** (Beta) | La vasca ha una telecamera, sotto i widget. Le telecamere sono disponibili solo per gli utenti Beta | **Guarda dal vivo** |
| **Registra il tuo primo test dell’acqua** | Nessuna lettura e nessuna attrezzatura collegata, sotto i widget | La scheda. Vedi [Configurare Cora Mobile](/help/mobile-setup#the-first-test-card) |

## Sotto i widget {#below-the-widgets}

![Il fondo della dashboard in Cora Mobile](img/mobile-dashboard-foot.webp "Modifica dashboard, i pulsanti Registra parametri, Storico parametri e Alimentazione, e le scorciatoie alle quattro aree dei registri.")

Dall'alto in basso trovi:

- Una riga che dice quando si è aggiornata la dashboard l'ultima volta e quali fonti ha usato, con **Modifica dashboard** accanto. Apre l'[editor della dashboard](/help/mobile-dashboard-editing).
- La scheda **Registra il tuo primo test dell’acqua**, su una vasca senza letture e senza attrezzatura collegata.
- **Registra parametri**, per inserire a mano le letture dei test.
- **Storico parametri**, per aprire lo storico di qualsiasi parametro che ha dati, anche senza widget. Vedi [Approfondire un parametro](/help/mobile-metric-detail).
- **Alimentazione**, per registrare un pasto diverso dalla tua routine. Vedi [Il diario](/help/mobile-journal).
- **Diario · Avvisi · Manutenzione · Popolazione**, scorciatoie a quelle aree per questa vasca.

## Toccare e tenere premuto {#tapping-through}

Tocca un widget di parametro qualsiasi per aprirne i dettagli. Vedrai lo storico completo in un grafico, tutte le fonti che l'hanno riportato e la tua fascia di avviso. Da lì puoi confrontare le fonti, escludere una lettura sbagliata o registrare la cura della sonda. Vedi [Approfondire un parametro](/help/mobile-metric-detail).

**Tieni premuto** un widget di parametro per impostarne l'intervallo di avviso direttamente dalla dashboard.

## Se un widget non ha un valore {#if-a-widget-has-no-value}

Un widget mostra un valore quando ne riceve uno. Se è vuoto, di solito il motivo è uno di questi:

- Il dispositivo è offline. Controlla la scheda **Dispositivi**.
- Il parametro non ha ancora una fonte. Registralo a mano, oppure collega un'attrezzatura che lo riporta.
- Per il parametro non è mai stato riportato né registrato niente.

Una lettura vecchia non sparisce solo perché è più vecchia del periodo del grafico. Resta sul widget con la sua età, così un valore vecchio sembra vecchio e non sembra mancante.

Per tutto il resto, vedi [Risoluzione dei problemi](/help/troubleshooting#a-widget-shows-no-value).
