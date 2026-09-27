---
title: Più di un dispositivo Cora
description: Scegli quale dispositivo risponde alla voce e quale legge l'attrezzatura di ogni vasca.
section: Cora Mobile
reviewed: 2026-09-27
order: 29
group: Account
---

In una casa ci possono essere più Cora Max. Due impostazioni decidono chi fa cosa, così i dispositivi non fanno due volte lo stesso lavoro. Conviene anche sapere cosa hanno in comune.

## Cosa è in comune e cosa no

| In comune su tutti i dispositivi | Proprio di ogni schermo |
|---|---|
| Vasche, letture e storico | Il layout della dashboard |
| Dispositivi e loro impostazioni | Wi-Fi, luminosità, audio |
| Diario, popolazione, manutenzione | Parola di attivazione e blocco bambini |
| Avvisi, soglie, automazioni | Le vasche mostrate su quello schermo |
| Piani e utilizzo | |

Se cambi una soglia su un dispositivo, cambia dappertutto. Se risistemi una dashboard, no: ogni schermo ha il suo layout, e telefono e Cora Max non ne condividono mai uno.

## Cora Assistant: dispositivo che risponde

In **Impostazioni → Cora Assistant → Dispositivo di risposta** scegli quale **dispositivo Cora** risponde quando parli nella stanza. Risponde uno solo, anche se ti sentono in tanti. Scegli quello più vicino al punto in cui ti trovi di solito.

Non è la stessa cosa del Cora Max principale, spiegato più avanti. Il dispositivo di risposta decide chi risponde alla tua voce. Il Cora Max principale decide chi legge l'attrezzatura di una vasca. In una casa con due tablet può avere senso impostarli in modo diverso.

![Il selettore del dispositivo che risponde](img/mobile-voice-responder.webp "Ogni dispositivo mostra cosa ascolta, e se è online.")

Per ogni dispositivo l'elenco mostra la parola di attivazione che ascolta e se è online. **Le parole di attivazione non sono tutte uguali.** Ogni parola è addestrata nel dispositivo, quindi modelli Cora diversi possono ascoltare parole diverse. Leggi la parola nella riga di ogni dispositivo e non dare per scontato che in casa sia la stessa per tutti.

:::note Il telefono non è in questo elenco
Il telefono non ascolta nessuna parola di attivazione. Sul telefono avvii una conversazione con un tocco, e questo funziona sempre, qualunque sia l'impostazione. L'elenco mostra solo i dispositivi Cora con la voce.
:::

## Cora Max principale

L'attrezzatura sulla tua rete viene letta da un Cora Max. Se più Cora Max possono leggere lo stesso controller, senza questa impostazione lo leggerebbero tutti insieme.

Il **Cora Max principale** si sceglie per ogni vasca e decide quale dispositivo legge il controller di quella vasca. In Cora Mobile apri la vasca e tocca **Cora Max principale**.

| Impostazione | Cosa succede |
|---|---|
| Un dispositivo preciso | Diventa l'unico dispositivo Cora che legge il controller e resta il principale anche quando è offline. Gli altri dispositivi Cora non prendono il suo posto. Cora Mobile legge il controller solo mentre quel dispositivo è offline. |
| **Qualsiasi attivo (automatico)** | Cora Mobile e tutti i dispositivi Cora online si dividono il lavoro (vale l'ultima scrittura). Se uno va offline, un altro continua. Va bene per una casa con un solo dispositivo ed è la scelta più sicura se non sai quale dispositivo dovrebbe occuparsene. |

Se il dispositivo che hai scelto è offline, i comandi che devono passare da lui non partono. Cora ti dice che la vasca usa quel dispositivo, che è offline e che non è stato eseguito nulla, così puoi riprovare quando torna online. Se resterà offline per un po', scegli un altro dispositivo oppure **Qualsiasi attivo (automatico)**.

:::note Con due dispositivi sulla stessa vasca, scegli un principale
Con un principale il controller lavora meno e sparisce il doppione delle letture dalla stessa fonte.
:::

:::note L'impostazione vale per la vasca, in tutto l'account
Il Cora Max principale appartiene alla vasca, non al telefono o al tablet che stai usando. Se lo cambi da un dispositivo qualsiasi, cambia per tutta la casa.
:::

## Cosa funziona fuori casa

Quando non sei sul Wi-Fi della vasca, il telefono non parla direttamente con l'attrezzatura. Il comando va a Cora Cloud, che lo passa a un Cora Max vicino alla vasca. È quel Cora Max a raggiungere davvero l'attrezzatura.

In pratica:

- **Letture e storico** sono sempre disponibili, ovunque tu sia, perché sono già salvati in Cora Cloud.
- **Comandare l'attrezzatura** (accendere o spegnere una presa, avviare l'alimentazione, dosare da una testa, mettere in pausa una pompa) funziona anche fuori casa, purché un Cora Max vicino alla vasca sia online e raggiunga quell'attrezzatura. Se non ce n'è nessuno, il comando non può arrivare.
- **Le impostazioni proprie di un dispositivo** (diverse dalle sue letture) a volte richiedono un telefono sulla *stessa* rete del dispositivo, e non basta un Cora Max vicino alla vasca. Quando è così, la pagina lo dice.

Ci sono due messaggi che ti avvisano che il comando non è andato semplicemente a buon fine:

- **"Nulla è stato inviato"**: il comando non è mai partito dal telefono, oppure nessun Cora Max vicino alla vasca ha potuto riceverlo. Non è stato eseguito nulla. È il messaggio che vedi se il Cora Max principale della vasca è offline e nessun altro dispositivo su quella vasca può sostituirlo.
- **"Potrebbe essere già stato eseguito"**: il comando è partito, ma nessun Cora Max ha risposto in tempo per confermarlo. Cora non sa davvero se è stato eseguito. Controlla lo stato dell'attrezzatura prima di riprovare, così non lo mandi due volte.

Se uno dei due messaggi continua a comparire, controlla che un Cora Max vicino alla vasca sia online, oppure imposta **Cora Max principale** su **Qualsiasi attivo (automatico)**, così qualsiasi dispositivo online può prendere il comando. Tutti i possibili esiti di un comando sono in [Controllare la tua attrezzatura](/help/mobile-device-control).

## Dove vedi lo stato di ogni dispositivo

Cora Max mostra lo stato di lettura di ogni vasca in **Impostazioni → Impostazioni Cora Max → Stato**. Vedi [Dispositivi e salute dei dispositivi](/help/max-devices).
