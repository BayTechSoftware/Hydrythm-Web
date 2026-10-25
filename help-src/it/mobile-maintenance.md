---
title: Manutenzione
description: Aggiungi lavori ricorrenti come pulire lo schiumatoio o cambiare le calze filtranti, ricevi un promemoria quando scadono e segnali come fatti o rinviali.
section: Cora Mobile
reviewed: 2026-10-17
order: 29
group: Records
twin: max-records
---

Manutenzione tiene i lavori che la tua vasca richiede a intervalli regolari, con un promemoria per ognuno.

Tocca **Manutenzione** nella fila di pulsanti sotto la dashboard. La trovi anche in Impostazioni → la tua vasca → **Manutenzione**.

![L'elenco della manutenzione](img/mobile-maintenance.webp "Conformità, numero di attività in ritardo e ogni attività con l'ultimo completamento e la prossima scadenza.")

## Il riepilogo {#summary}

In alto vedi **Conformità manutenzione**, la quota di attività in regola in questo momento, e quante attività sono in ritardo.

Ogni attività nell'elenco ha un colore: in ritardo, in scadenza a breve o in programma. Mostra anche quando l'hai fatta l'ultima volta e quando scade la prossima.

## Aggiungere un'attività {#adding-a-task}

Tocca **Aggiungi attività**, poi scegli:

- **Da modello** per un lavoro comune con l'intervallo già inserito. Sceglilo, poi imposta quando scade la prossima volta e l'ora in cui vuoi il promemoria, e tocca **Conferma**.
- **Attività personalizzata** per un lavoro tuo. Dagli un **Nome attività**, un **Intervallo (giorni)**, una **Categoria** e una **Prossima data di scadenza**. Attiva **Promemoria** e scegli **Ricordamelo alle** se vuoi una notifica.

Alcuni dei modelli, con l'intervallo da cui partono:

| Attività | Intervallo |
|---|---|
| Cambia i calzini filtranti | 3 giorni |
| Pulisci la coppetta dello schiumatoio | 7 giorni |
| Cambio d'acqua | 7 giorni |
| Testa i parametri dell'acqua | 7 giorni |
| Sostituisci il carbone | 30 giorni |
| Calibra la sonda pH | 30 giorni |
| Pulisci le pompe di movimento | 90 giorni |
| Carica i risultati ICP | 90 giorni |

Puoi cambiare l'intervallo di qualsiasi attività in seguito.

### Attività che Cora aggiunge per l'attrezzatura Red Sea {#red-sea-tasks}

Quando colleghi un ReefDose, ReefATO+, ReefMat o ReefRun Red Sea, Cora aggiunge la manutenzione di cui ha bisogno quell'unità, già con l'intervallo giusto:

| Dispositivo | Attività | Intervallo |
|---|---|---|
| ReefATO+ | Replace ReefATO+ EC sensor | 42 giorni |
| ReefATO+ | Replace ReefATO+ return pump | 135 giorni |
| ReefMat | Replace ReefMat carbon | 25 giorni |
| ReefRun | Check ReefRun skimmer venturi | 35 giorni |
| ReefRun | Replace ReefRun skimmer rotor | 135 giorni |
| ReefRun | Calibrate ReefRun full-cup sensor | 28 giorni |
| ReefRun | Calibrate ReefRun overskimming sensor | 28 giorni |
| ReefRun, per pompa | Service ReefRun pump motor | 135 giorni |
| ReefRun, per pompa | Clean ReefRun pump strainer | 42 giorni |
| ReefDose, per testa | Calibrate ReefDose head | 90 giorni |
| ReefDose, per testa | Replace ReefDose head tubing | 450 giorni |

Funzionano come qualsiasi attività che aggiungi tu. Puoi rinominarle, cambiare l'intervallo, rinviarle o eliminarle. Se ne elimini una, Cora non la aggiunge di nuovo per quel dispositivo.

### Testare l'acqua {#test-water}

Se tocchi **Ricordami di testare ogni settimana** sulla scheda del primo test, Cora aggiunge un'attività settimanale chiamata **Testare l’acqua**, in scadenza nel **Giorno del test** che scegli. Funziona come qualsiasi altra attività. Vedi [Configurare Cora Mobile](/help/mobile-setup). Puoi anche aggiungere un promemoria per i test in qualsiasi momento con il modello **Testa i parametri dell'acqua**.

### Da un'automazione {#from-an-automation}

Un'[automazione](/help/mobile-automation) con l'azione **Crea un'attività di manutenzione** può mettere un lavoro in questo elenco quando la sua regola scatta, oppure rendere subito in scadenza un'attività esistente. Una nuova è un'**Attività una tantum**, in scadenza subito, e mostra *Creata da un'automazione* con il motivo. Esce dall'elenco quando la completi. Finché è ancora aperta, la stessa automazione non ne aggiunge un'altra. Ricevi una sola notifica.

## Promemoria {#reminders}

Apri un'attività e attiva **Promemoria**, poi scegli **Ricordamelo alle**. Ricevi una notifica il giorno prima della scadenza e una il giorno stesso. Finché è in ritardo, ricevi un promemoria ogni pochi giorni. Se più attività di una vasca scadono insieme, arrivano in un'unica notifica.

I promemoria rientrano in **Promemoria di manutenzione** in [Impostazioni → Notifiche](/help/mobile-notifications). Se per un'attività ti basta vederla nell'elenco, spegni il suo **Promemoria**.

## Segnare un'attività come fatta {#marking-done}

Scorri l'attività verso destra, oppure aprila e tocca **Completa**. Se hai scorso per errore, tocca **Annulla** nel messaggio che compare.

Cora salva l'ora in cui hai finito e calcola la prossima scadenza da quel momento. Quindi se fai un lavoro con tre giorni di ritardo, anche il prossimo slitta di tre giorni. Se l'attività è in ritardo, Cora chiede prima **Quando l'hai fatto?** Scegli **Proprio ora**, oppure **Scegli data e ora** se l'hai fatto prima (vedi sotto).

Il pannello dell'attività mostra la sua **Cronologia completamenti**, compreso quanto in ritardo è stata fatta ogni volta.

:::note Completare un'attività scrive anche una voce nel diario
Cora aggiunge per te una breve voce nel tuo [diario](/help/mobile-journal), indicando se eri in ritardo. Aggiungi una voce tua quando c'è altro da dire, per esempio se la pompa era piena di sabbia o le calze erano nere dopo un giorno.
:::

## Segnare un'attività come fatta prima {#done-earlier}

Hai fatto il lavoro ieri e ti sei scordato di spuntarlo? Apri l'attività, tocca **Fatto prima…** e scegli data e ora. Cora data il completamento, la voce del diario e la prossima scadenza da quell'ora: la prossima scadenza è quindi l'ora scelta più l'intervallo.

Puoi tornare indietro fino a un anno, ma non prima dell'ultima volta in cui hai completato l'attività. Se scegli un'ora che non è ancora arrivata, o una precedente all'ultimo completamento, Cora te lo dice e non salva nulla.

## Modificare un'attività {#editing}

Tocca un'attività per aprirla. Puoi cambiare **Nome attività**, **Intervallo (giorni)**, **Note (opzionale)**, **Prossima data di scadenza** e il promemoria, poi tocca **Salva**. **Elimina** la rimuove.

## Rinviare {#snoozing}

Non riesci a fare un lavoro adesso? Aprilo, tocca **Rinvia** e scegli **1 giorno**, **3 giorni**, **1 settimana**, **2 settimane** o **1 mese**. Resta nell'elenco come **Rinviata** con la nuova data, e non ricevi promemoria fino ad allora.

:::warning Segna un'attività come fatta solo quando l'hai fatta
La prossima scadenza viene calcolata dall'ora in cui hai fatto l'attività. Se segni come fatta un'attività ancora aperta, tutte le scadenze successive si spostano. Se l'hai fatta prima, usa **Fatto prima…** e scegli l'ora reale. Se non l'hai fatta, rinviala invece.
:::

Non c'è modo di mettere in pausa un'attività. Per un lavoro che in questa stagione non serve, rinvialo di **1 mese**, oppure eliminalo e aggiungilo di nuovo più avanti.
