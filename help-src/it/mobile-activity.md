---
title: Attività e cronologia
description: Tutto ciò che è successo al tuo equipaggiamento, e cosa lo ha causato.
section: Cora Mobile
reviewed: 2026-09-09
order: 22
group: Records
---

Attività registra ogni **richiesta di azione** (ogni tentativo di cambiare qualcosa) insieme a cosa l'ha richiesta e cosa ne è risultato.

Una richiesta non è la stessa cosa di un cambiamento. Le richieste rifiutate non sono state eseguite, con un'eccezione: una voce che dice *Nessun dispositivo ha risposto in tempo* potrebbe essere comunque stata eseguita, quindi controlla l'equipaggiamento prima di ripeterla. Le richieste senza cambiamento hanno trovato l'equipaggiamento già come richiesto, e una non confermata potrebbe o no essere arrivata affatto al dispositivo. Tutte vengono registrate.

**Impostazioni → Attività.**

![Il registro dell'attività](img/mobile-activity.webp "Ogni azione, con la superficie che l'ha richiesta.")

## Cosa viene registrato

Ogni **richiesta**, non solo quelle che hanno funzionato: commutazioni di prese, cicli di alimentazione, dosaggi, cambi di presa intelligente, e qualsiasi cosa abbia fatto una scena o un'automazione.

Una richiesta che è stata **rifiutata**, che non ha prodotto **nessun cambiamento**, o che è uscita ed è tornata **non confermata** viene registrata proprio come una eseguita. È questo il punto: un comando che silenziosamente non ha fatto nulla è esattamente ciò che vuoi trovare qui.

## Cosa lo ha causato

Ogni voce nomina la sua causa:

| Causa | Significa |
|---|---|
| **Questa app** | L'hai toccato qui |
| **Voce in questa app** | Hai chiesto, su questo telefono |
| **Toccato su un Cora** | Qualcuno ha usato uno schermo Cora; la riga dice quale |
| **Voce su un Cora Max** | Qualcuno ha parlato a uno schermo |
| **Cora Assistant** | Hai chiesto a Cora di farlo |
| **Regola di automazione** | Una regola è scattata |
| **Pulsante smart** | Un pulsante fisico è stato premuto |
| **Inviato da Cora Cloud** | Emesso dal tuo account invece che da un dispositivo davanti a te |
| **Fonte sconosciuta** | Registrato prima che la fonte potesse essere identificata |

## Come è arrivato

Ogni riga porta anche un chip di percorso, perché *come* una richiesta ha raggiunto il tuo equipaggiamento spiega molto di cosa è andato storto quando qualcosa lo ha fatto:

| Chip | Significa |
|---|---|
| **LAN** | Inviato attraverso la tua rete, direttamente all'equipaggiamento |
| **TRAMITE CLOUD** | Inviato tramite il tuo account, per equipaggiamento non raggiungibile direttamente |
| **PERCORSO ?** | Registrato prima che i percorsi venissero tracciati: genuinamente sconosciuto, non presunto |

Su un sistema con più di un Cora, la riga nomina anche quale ha portato fuori la richiesta.

## La cronologia della vasca

Separatamente dalle azioni sull'equipaggiamento, ogni vasca ha una **cronologia**: letture, avvisi, voci di diario, risultati ICP e cambiamenti di popolazione disposti in ordine.

Usa l'attività quando ti stai chiedendo *"cosa ha fatto qualcosa?"* e la cronologia quando ti stai chiedendo *"cosa stava succedendo attorno a questa data?"*

:::note La cronologia e il diario sono complementari
La cronologia contiene ciò che Cora ha registrato; il [diario](/help/mobile-journal) contiene ciò che hai fatto tu. Letti insieme stabiliscono causa ed effetto attorno a una determinata data.
:::
