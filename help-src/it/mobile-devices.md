---
title: Aggiungere, modificare e rimuovere dispositivi
description: Come aggiungere equipaggiamento a Cora, assegnarlo a una vasca, rinominarlo e rimuoverlo in modo corretto.
section: Cora Mobile
reviewed: 2026-09-27
order: 9
group: Equipment
---

La scheda **Dispositivi** è tutto ciò che hai collegato, raggruppato per marca. Ogni gruppo si chiude così una stanza della vasca piena di equipaggiamento resta leggibile.

![La scheda Dispositivi](img/mobile-devices.webp "L'equipaggiamento è raggruppato per marca. Ogni gruppo si può chiudere.")

## Aggiungere equipaggiamento

Sotto l'elenco ci sono tre pulsanti, e fanno lavori diversi:

| Pulsante | Aggiunge |
|---|---|
| **Aggiungi dispositivo** | Un Cora Max. Trova unità già sul tuo Wi-Fi, o unità vicine via Bluetooth. **Inserisci l'indirizzo IP manualmente** si trova dentro questa schermata se la scoperta automatica non lo trova. |
| **Trova una pompa sulla tua rete** | Pompe Jecod che si annunciano sulla rete locale |
| **Aggiungi AquaWiz** | Un controller AquaWiz, tramite il tuo account AquaWiz |

![Aggiungere un Cora Max](img/mobile-add-device.webp "Aggiungi dispositivo cerca un Cora Max su Wi-Fi e Bluetooth.")

Altri equipaggiamenti (Neptune Apex e Red Sea ReefBeat) si collegano dalla vasca invece che da questo elenco. Vedi [Collegare il tuo equipaggiamento](/help/mobile-connections).

Aggiungere equipaggiamento come un riscaldatore, una pompa o uno schiumatoio offre un **completamento automatico** di marca e modello: inizia a digitare e Cora suggerisce da un ampio elenco verificato alla fonte di marche di equipaggiamento. Se la tua non è elencata, digitala comunque; Cora conserva qualunque cosa tu digiti.

:::note Cora e il tuo telefono hanno bisogno della stessa rete
L'equipaggiamento trovato localmente deve essere sulla stessa rete del tuo telefono quando lo aggiungi. **Dopo la configurazione resta raggiungibile solo su quella rete** (o via Bluetooth, per le unità che lo usano), a meno che un dispositivo Cora sul posto non possa raggiungerlo per tuo conto.

L'equipaggiamento che legge correttamente a casa può quindi mostrare valori più vecchi mentre sei via, a meno che un Cora Max sul posto non possa interrogarlo. Questo riflette da dove è raggiungibile l'equipaggiamento, non un guasto.
:::

## Assegnare un dispositivo a una vasca

La maggior parte dell'equipaggiamento appartiene esattamente a una vasca, ed è questo che fa apparire le sue letture sulla dashboard di quella vasca.

**Cora Max è l'eccezione**: può essere assegnato a fino a quattro vasche e passa da una all'altra sullo schermo. Vedi [Più di un dispositivo Cora](/help/mobile-multi-device).

Apri il dispositivo e scegli **Vasca**. Se gestisci più di un sistema, questa è l'impostazione che conta più di tutte: un riscaldatore assegnato alla vasca sbagliata riporta perfettamente bene nel posto sbagliato.

:::warning Assegna la vasca prima di fare affidamento sulle letture
Un dispositivo senza vasca continua a riportare, ma i suoi numeri non hanno dove finire. Se un dispositivo che hai appena aggiunto non appare su una dashboard, controlla prima questo.
:::

## Rinominare

Apri il dispositivo e modifica il suo nome. Usa il nome che usi per lui giorno per giorno: "Ritorno", "Gyre sinistra", "Riscaldatore sump". Il nome appare sui widget, negli avvisi e in qualsiasi cosa chiedi a Cora, quindi un nome che ha un senso per te rende tutto più chiaro a valle.

Rinominare è locale a Cora. Non cambia il nome nell'app del produttore.

## Controllare se un dispositivo è in salute

Ogni riga mostra il suo stato attuale. Ciò che vuoi vedere è un orario di aggiornamento recente e nessun avviso.

| Cosa vedi | Cosa significa |
|---|---|
| Un orario di aggiornamento recente | Funziona normalmente |
| "Aggiornato 3 h fa" su qualcosa che riporta ogni ora | Va bene |
| "Impossibile raggiungere…" | Un problema di rete, oppure il dispositivo è spento |
| "…ha rifiutato l'accesso" | L'account del produttore ha bisogno di essere riconnesso; apri il dispositivo ed accedi di nuovo |
| Nulla del tutto | Non ha mai riportato; controlla l'assegnazione della vasca e la connessione |

## Rimuovere un dispositivo

Apri il dispositivo e scegli **Rimuovi**. Ti verrà chiesto di confermare, e ti verrà detto esattamente cosa viene rimosso.

**Le tue letture vengono conservate.** Rimuovere un dispositivo interrompe la raccolta di nuovi dati da parte di Cora; lo storico già raccolto resta sulla vasca, e qualsiasi widget puntato su di esso conserva le sue letture passate.

Ciò che perdi è il collegamento in tempo reale, e, dove il dispositivo si collegava tramite un account del produttore, l'accesso memorizzato. Aggiungerlo di nuovo significa accedere di nuovo.

:::tip Rendi silenzioso un dispositivo rumoroso senza rimuoverlo
Se un dispositivo funziona correttamente ma avvisa troppo spesso, correggi le sue soglie o le impostazioni di notifica; vedi **[Avvisi e soglie](/help/mobile-alerts)**. Questo mantiene la connessione e i dati mentre ferma il rumore.
:::
