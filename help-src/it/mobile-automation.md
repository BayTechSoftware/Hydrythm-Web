---
title: Automazioni e scene
description: Crea regole che si eseguono da sole (trigger, condizioni, azioni) e raggruppale in scene.
section: Cora Mobile
reviewed: 2026-09-27
order: 17
group: Alerts and automation
---

Un'automazione è una regola che Cora esegue per te: *quando succede questo, controlla quest'altro, poi fai questo.* Le scene raggruppano diverse azioni in una sola cosa che puoi eseguire o programmare.

**Impostazioni → Automazione.**

![L'elenco delle automazioni](img/mobile-automation.webp "Automazioni e Scene sono schede separate. Ogni regola ha un interruttore di attivazione.")

La schermata ha due schede (**Automazioni** e **Scena**) e un pulsante **Nuova automazione**. Ogni regola mostra un riassunto di una riga di cosa fa, un interruttore di attivazione, e un menu per modificarla o eliminarla. Una regola che non è ancora stata eseguita è segnata come tale.

:::warning Queste agiscono su equipaggiamento reale
Una regola che commuta una pompa la commuta indipendentemente dal fatto che tu stia guardando. Creane una alla volta e controlla che ognuna faccia ciò che ti aspetti prima di aggiungere la successiva.
:::

## La forma di una regola

Ogni regola ha le stesse tre parti:

**Trigger**: cosa la attiva
**Condizioni**: cosa deve anche essere vero
**Azioni**: cosa fa poi, in ordine

## Cosa può attivare una regola

Quattro cose:

| Trigger | Scatta quando |
|---|---|
| **Parametro** | Un parametro supera un valore che imposti, in una direzione che scegli |
| **Avviso** | Un avviso viene generato, chiuso, o entrambi |
| **Programma** | Un'ora del giorno, nel tuo stesso fuso orario |
| **Stato dispositivo** | Un dispositivo va offline o torna online |

## Condizioni

Le condizioni decidono se le azioni vengono effettivamente eseguite. Hai i confronti abituali (uguale, non uguale, maggiore di, minore di, e così via) e puoi combinarli con **e**, **o** e **non**.

C'è anche una condizione di **passo**, che controlla come è andato il passo *precedente*. È questo che ti permette di scrivere "provo questo; se non ha funzionato, fai quest'altro invece."

## Cosa può fare una regola

Un'azione che richiede equipaggiamento viene offerta solo su una vasca che ha quell'equipaggiamento:

| Azione | Cosa fa |
|---|---|
| **Controlla apparecchiatura Apex** | Commuta una presa |
| **Controlla un'apparecchiatura Red Sea** | Guida un'unità ReefBeat |
| **Controlla una pompa di movimento** | Imposta il flusso, la modalità onda o la potenza di una pompa Jecod, oppure **Pausa per l'alimentazione**: il Cora Max alla vasca riporta la pompa a posto quando l'alimentazione finisce |
| **Controlla un'apparecchiatura Cora** | Commuta una presa intelligente |
| **Controlla dispositivo IR** | Invia un comando infrarossi |
| **Esegui ciclo di alimentazione Apex** | Avvia un'alimentazione |
| **Esegui un test Trident** | Attiva un test |
| **Avvisami** | Invia una notifica push a te stesso |
| **Attendi prima del passo successivo** | Sospende prima di continuare |
| **Esegui una scena** | Esegue un'altra scena dall'interno di questa regola |
| **Gestisci un'automazione** | Attiva o disattiva un'altra regola |
| **Dosa una testa DŌS** | Esegue un dosaggio misurato su una testa DŌS |

:::warning Dosare da una regola è irreversibile e limitato
Un dosaggio non può essere ritirato dalla vasca. La testa deve essere **calibrata** prima che una regola possa dosare da essa, e il dosaggio non sorvegliato è limitato a **10 mL per testa al giorno**; una regola non può superare quel limite comunque sia scritta. Le azioni di dosaggio appaiono solo una volta che le tue teste sono riconosciute come teste di dosaggio.
:::

:::note Usa Attendi per sequenziare i passi in una regola
Una pausa permette a una singola regola di eseguire una procedura ordinata (per esempio spegnere una presa, attendere, poi riaccenderla) senza una seconda regola e un programma.
:::

## Scene

Una scena è un gruppo di azioni con un nome che puoi eseguire su richiesta, da un programma, o dall'interno di un'altra regola: "Cambio d'acqua", "Modalità foto", "Notte".

Una scena può richiamare un'altra scena. Cora si rifiuta di eseguire una scena annidata oltre il suo limite di profondità, e si rifiuta di eseguire una scena che richiamerebbe se stessa, per impedire un ciclo che continuerebbe ad agire sulla vasca indefinitamente.

Dopo che una scena viene eseguita ti viene detto cosa è successo, passo per passo, incluso qualsiasi cosa sia fallita.

Eseguire una scena a mano richiede prima una conferma, poiché una scena può commutare diversi pezzi di equipaggiamento contemporaneamente.

## Scene create su Cora Max

Le scene possono anche essere create e modificate direttamente su un tablet Cora Max, non solo sul telefono: è lo stesso insieme di scene in entrambi i casi, condiviso su tutto l'account. Se una casa ha un Cora Max più vecchio, può comunque eseguire una scena creata sul telefono; solo la modifica sul dispositivo è una funzione più recente, quindi un tablet più vecchio potrebbe mostrare una scena senza permetterti di modificarla lì. Modificala invece dal telefono.

## Disattivare una regola

Ogni regola ha un interruttore di attivazione. Disattivarne una conserva la sua definizione, utile quando la vuoi di nuovo la stagione successiva invece di ricrearla.

## Vedere cosa ha fatto una regola

Ogni azione eseguita da una regola viene registrata con la regola come sua causa. Vedi **[Attività](/help/mobile-activity)**.
