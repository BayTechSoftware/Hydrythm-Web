---
title: Aggiungere, modificare e rimuovere dispositivi
description: Come aggiungere attrezzatura a Cora, assegnarla a una vasca, rinominarla e rimuoverla nel modo giusto.
section: Cora Mobile
reviewed: 2026-09-27
order: 9
group: Equipment
---

Nella scheda **Dispositivi** trovi tutto quello che hai collegato, diviso per marca. Ogni gruppo si può chiudere, così l'elenco resta leggibile anche con una stanza piena di attrezzatura.

![La scheda Dispositivi](img/mobile-devices.webp "L'attrezzatura è raggruppata per marca. Ogni gruppo si può chiudere.")

## Aggiungere attrezzatura

Sotto l'elenco ci sono tre pulsanti, ognuno con il suo compito:

| Pulsante | Cosa aggiunge |
|---|---|
| **Aggiungi dispositivo** | Un Cora Max. Trova le unità già sul tuo Wi-Fi o quelle vicine via Bluetooth. Se la ricerca non lo trova, in questa schermata c'è anche **Inserisci l'indirizzo IP manualmente**. |
| **Trova una pompa sulla tua rete** | Le pompe Jecod che si annunciano sulla rete locale |
| **Aggiungi AquaWiz** | Un controller AquaWiz, attraverso il tuo account AquaWiz |

![Aggiungere un Cora Max](img/mobile-add-device.webp "Aggiungi dispositivo cerca un Cora Max su Wi-Fi e Bluetooth.")

Neptune Apex e Red Sea ReefBeat si collegano dalla vasca e non da questo elenco. Trovi come fare in [Collegare la tua attrezzatura](/help/mobile-connections).

Quando aggiungi un riscaldatore, una pompa o uno schiumatoio, marca e modello si **completano da soli**. Inizia a scrivere e Cora ti suggerisce le marche da un lungo elenco verificato. Se la tua non c'è, scrivila lo stesso: Cora salva quello che scrivi.

:::note Cora e il telefono devono essere sulla stessa rete
Quando aggiungi un'attrezzatura trovata in rete locale, deve essere sulla stessa rete del telefono. **Anche dopo la configurazione si raggiunge solo da quella rete** (o via Bluetooth, per le unità che lo usano), a meno che un dispositivo Cora sul posto non la raggiunga per te.

Quindi un'attrezzatura che a casa legge bene può mostrare valori più vecchi quando sei fuori, a meno che sul posto non ci sia un Cora Max che la legge. Non è un guasto: dipende da dove si può raggiungere l'attrezzatura.
:::

## Assegnare un dispositivo a una vasca

Quasi tutta l'attrezzatura appartiene a una sola vasca. È questa assegnazione che fa comparire le letture sulla dashboard di quella vasca.

**Cora Max fa eccezione**: si può assegnare fino a quattro vasche e passa dall'una all'altra sullo schermo. Ne parliamo in [Più di un dispositivo Cora](/help/mobile-multi-device).

Apri il dispositivo e scegli **Vasca**. Se hai più impianti, è l'impostazione più importante: un riscaldatore assegnato alla vasca sbagliata funziona benissimo, ma i dati finiscono nel posto sbagliato.

:::warning Assegna la vasca prima di fidarti delle letture
Un dispositivo senza vasca continua a mandare dati, ma i numeri non finiscono da nessuna parte. Se un dispositivo appena aggiunto non compare su nessuna dashboard, controlla prima questo.
:::

## Rinominare

Apri il dispositivo e cambia il nome. Usa il nome con cui lo chiami tutti i giorni: "Risalita", "Gyre sinistra", "Riscaldatore sump". Il nome compare sui widget, negli avvisi e in tutto quello che chiedi a Cora, quindi un nome che per te ha senso rende tutto più chiaro.

Il nuovo nome vale solo in Cora. Nell'app del produttore il nome resta quello di prima.

## Controllare se un dispositivo funziona

Ogni riga mostra lo stato attuale. Quello che vuoi vedere è un aggiornamento recente e nessun avviso.

| Cosa vedi | Cosa significa |
|---|---|
| Un aggiornamento recente | Funziona normalmente |
| "Aggiornato 3 h fa" su un dispositivo che riporta solo ogni poche ore | Va bene |
| "Impossibile raggiungere…" | C'è un problema di rete o il dispositivo è spento |
| "…ha rifiutato l'accesso" | L'account del produttore va ricollegato. Apri il dispositivo e accedi di nuovo |
| Niente | Non ha mai mandato dati. Controlla la vasca assegnata e il collegamento |

## Rimuovere un dispositivo

Apri il dispositivo e scegli **Rimuovi**. Cora ti chiede di confermare e ti dice esattamente cosa viene rimosso.

**Le letture restano.** Dopo la rimozione Cora non raccoglie più nuovi dati da quel dispositivo, ma lo storico già raccolto resta nella vasca e i widget collegati mantengono le letture passate.

Perdi il collegamento in tempo reale e, se il dispositivo passava da un account del produttore, anche l'accesso salvato. Per aggiungerlo di nuovo dovrai accedere un'altra volta.

:::tip Zittisci un dispositivo troppo insistente senza rimuoverlo
Se un dispositivo funziona bene ma ti avvisa troppo spesso, cambia le soglie o le impostazioni delle notifiche, come spiegato in **[Avvisi e soglie](/help/mobile-alerts)**. Collegamento e dati restano, e le notifiche inutili finiscono.
:::
