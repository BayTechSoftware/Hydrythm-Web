---
title: Automazioni e scene
description: Crea regole che partono da sole, con trigger, condizioni e azioni, e raggruppa le azioni in scene.
section: Cora Mobile
reviewed: 2026-09-27
order: 17
group: Alerts and automation
---

Un'automazione è una regola che Cora esegue al posto tuo: *quando succede questo, controlla quello, poi fai quest'altro.* Una scena mette insieme più azioni in un'unica cosa da avviare a mano o da programmare.

**Impostazioni → Automazione.**

![L'elenco delle automazioni](img/mobile-automation.webp "Automazioni e Scene sono schede separate. Ogni regola ha un interruttore di attivazione.")

La schermata ha due schede, **Automazioni** e **Scene**, e il pulsante **Nuova automazione**. Ogni regola ha una riga che riassume cosa fa, un interruttore di attivazione e un menu per modificarla o eliminarla. Le regole mai eseguite sono segnalate.

:::warning Le regole agiscono sull'attrezzatura vera
Una regola che spegne una pompa la spegne anche se non stai guardando. Crea una regola alla volta e controlla che faccia quello che ti aspetti prima di aggiungerne un'altra.
:::

## Com'è fatta una regola

Ogni regola ha tre parti:

**Trigger**: cosa la fa partire
**Condizioni**: cos'altro deve essere vero
**Azioni**: cosa fa poi, nell'ordine

## Cosa fa partire una regola

Ci sono quattro trigger:

| Trigger | Scatta quando |
|---|---|
| **Parametro** | Un parametro supera un valore che hai impostato, nella direzione che scegli |
| **Avviso** | Un avviso scatta, si chiude, o in tutti e due i casi |
| **Programma** | È una certa ora del giorno, nel tuo fuso orario |
| **Stato dispositivo** | Un dispositivo va offline o torna online |

## Condizioni

Le condizioni decidono se le azioni partono davvero. Hai i confronti di sempre (uguale, diverso, maggiore di, minore di e così via) e puoi combinarli con **e**, **o** e **non**.

Esiste anche una condizione **passo**, che guarda com'è andato il passo *precedente*. Con questa puoi scrivere "prova questo e, se non ha funzionato, fai quest'altro".

## Cosa può fare una regola

Le azioni che richiedono un'attrezzatura compaiono solo nelle vasche che ce l'hanno:

| Azione | Cosa fa |
|---|---|
| **Controlla apparecchiatura Apex** | Accende o spegne una presa |
| **Controlla un'apparecchiatura Red Sea** | Comanda un'unità ReefBeat |
| **Controlla una pompa di movimento** | Imposta flusso, modalità onda o potenza di una pompa Jecod, oppure **Pausa per l'alimentazione**. A fine alimentazione il Cora Max vicino alla vasca rimette la pompa com'era |
| **Controlla un'apparecchiatura Cora** | Accende o spegne una presa smart |
| **Controlla dispositivo IR** | Invia un comando a infrarossi |
| **Esegui ciclo di alimentazione Apex** | Avvia l'alimentazione |
| **Esegui un test Trident** | Avvia un test |
| **Avvisami** | Ti manda una notifica push |
| **Attendi prima del passo successivo** | Fa una pausa prima di continuare |
| **Esegui una scena** | Avvia una scena dall'interno di questa regola |
| **Gestisci un'automazione** | Attiva o disattiva un'altra regola |
| **Dosa una testa DŌS** | Dosa una quantità precisa da una testa DŌS |

:::warning Un dosaggio da regola non si annulla ed è limitato
Quello che hai dosato non si può togliere dalla vasca. Una regola può dosare solo da una testa **calibrata**, e senza sorveglianza il limite è **10 mL per testa al giorno**. Nessuna regola può superarlo, comunque sia scritta. Le azioni di dosaggio compaiono solo quando Cora riconosce le tue teste come teste dosatrici.
:::

:::note Con Attendi metti in fila i passi di una regola
Con una pausa, una sola regola può seguire una procedura in ordine: per esempio spegnere una presa, aspettare e poi riaccenderla. Non ti servono una seconda regola e un programma.
:::

## Scene

Una scena è un gruppo di azioni con un nome, come "Cambio d'acqua", "Modalità foto" o "Notte". Puoi avviarla quando vuoi, da un programma o dall'interno di un'altra regola.

Una scena può richiamarne un'altra. Cora non esegue una scena annidata oltre il limite di profondità, né una scena che richiamerebbe se stessa. Così si evita un ciclo che continuerebbe ad agire sulla vasca all'infinito.

Quando una scena finisce, Cora ti dice cosa è successo passo per passo, compreso quello che non è riuscito.

Se avvii una scena a mano, Cora ti chiede prima di confermare, perché una scena può comandare più apparecchi insieme.

## Scene create su Cora Max

Puoi creare e modificare le scene anche direttamente su un tablet Cora Max. Le scene sono le stesse sul telefono e sul Cora Max, condivise in tutto l'account. Un Cora Max più vecchio può comunque eseguire una scena creata sul telefono. La modifica sul dispositivo è arrivata dopo, quindi un tablet più vecchio potrebbe mostrarti la scena senza farti cambiare nulla. In quel caso modificala dal telefono.

## Disattivare una regola

Ogni regola ha un interruttore di attivazione. Se la spegni, la regola resta salvata: comodo se ti servirà di nuovo la prossima stagione e non vuoi rifarla da capo.

## Vedere cosa ha fatto una regola

Ogni azione eseguita da una regola viene registrata con la regola come origine. Vedi **[Attività](/help/mobile-activity)**.
