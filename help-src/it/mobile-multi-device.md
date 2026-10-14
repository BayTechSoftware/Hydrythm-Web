---
title: Più di un dispositivo Cora
description: Con più di un dispositivo Cora, scegli quale risponde alla tua voce e quale legge ogni vasca, e scopri cosa funziona fuori casa.
section: Cora Mobile
reviewed: 2026-10-13
order: 36
group: Settings and account
twin: max-reef-room
---

Questa pagina è per una casa con più di un Cora Max, oppure con un Cora Max e più telefoni. Due impostazioni decidono quale dispositivo fa cosa, così non fanno due volte lo stesso lavoro. Conviene anche sapere cosa condividono.

## Cosa è condiviso e cosa no

| Condiviso su tutti i dispositivi | Appartiene a un singolo Cora Max |
|---|---|
| Vasche, letture e storico | Il layout della sua dashboard |
| Dispositivi e loro impostazioni | Wi-Fi, luminosità, audio |
| Diario, popolazione, manutenzione | Parola di attivazione e blocco bambini |
| Avvisi, soglie, automazioni | Quali vasche mostra quello schermo |
| Piani e utilizzo | |

Se cambi una soglia su un dispositivo, cambia dappertutto. I layout delle dashboard sono diversi. Il layout del telefono segue il tuo account, quindi ogni telefono su cui accedi mostra lo stesso. Ogni Cora Max tiene il suo layout, e telefono e Cora Max non ne condividono mai uno.

## Cora Assistant: dispositivo di risposta {#cora-assistant-answering-device}

**Impostazioni → Cora Assistant → Dispositivo di risposta** sceglie il **dispositivo Cora** che risponde quando parli nella stanza. Per quanti dispositivi ti sentano, ne risponde solo uno. Imposta quello più vicino al punto in cui stai di solito.

Solo il dispositivo di risposta ascolta la frase di attivazione. Un altro Cora Max ascolta al suo posto mentre è offline, o se non si fa vedere da più di 15 minuti, e smette quando torna. Di più in [Parlare con Cora](/help/max-voice).

È una cosa diversa dal Cora Max principale, più avanti. Il dispositivo di risposta decide chi risponde alla tua voce. Il Cora Max principale decide chi legge l'attrezzatura di una vasca. Con due Cora Max in casa, potresti impostarli in modo diverso.

![Il selettore del dispositivo di risposta](img/mobile-voice-responder.webp "Ogni dispositivo mostra cosa ascolta e se è online.")

Ogni dispositivo nell'elenco mostra la sua frase di attivazione e se è online. **Le frasi di attivazione non sono sempre le stesse.** La frase è addestrata nel dispositivo, quindi modelli Cora diversi possono ascoltare frasi diverse. Controlla la riga di ogni dispositivo. Non dare per scontato che tutta la casa usi una sola frase.

:::note Il telefono non è in questo elenco
Il telefono non ascolta una frase di attivazione. Sul telefono avvii una conversazione con un tocco, e questo funziona sempre, qualunque cosa dica questa impostazione. L'elenco mostra solo l'hardware Cora con la voce.
:::

## Cora Max principale

Un Cora Max legge l'attrezzatura sulla tua rete. Se più di uno può raggiungere lo stesso controller, lo leggerebbero tutti in parallelo.

**Cora Max principale** ti fa scegliere, per ogni vasca, quale dispositivo legge il controller di quella vasca. In Cora Mobile, apri la vasca e tocca **Cora Max principale**.

| Impostazione | Comportamento |
|---|---|
| Un dispositivo con nome | È l'unico dispositivo Cora che legge il controller. Resta il principale anche mentre è offline, e gli altri dispositivi Cora non prendono il suo posto. Cora Mobile legge il controller solo mentre quel dispositivo è offline. |
| **Qualsiasi attivo (automatico)** | Cora Mobile e qualsiasi dispositivo Cora online si dividono il lavoro (vince l'ultima scrittura). Se uno va offline, un altro continua. Va bene per una casa con un solo dispositivo, ed è la scelta più sicura se non sai quale dispositivo dovrebbe occuparsi della vasca. |

Mentre il dispositivo che hai scelto è offline, un comando che deve passare da lui non viene eseguito. Cora ti dice che la vasca è impostata per usare quel dispositivo, che è offline e che non è stato eseguito niente. Riprova quando torna. Se resterà offline per un po', scegli un altro dispositivo oppure **Qualsiasi attivo (automatico)**.

:::note Due dispositivi sulla stessa vasca? Imposta un principale
Scegliere un principale alleggerisce il controller ed elimina le letture doppie dalla stessa fonte.
:::

:::note Questa impostazione appartiene alla vasca
Il Cora Max principale si imposta per vasca per tutto l'account. Non appartiene al telefono o al Cora Max che hai in mano. Cambialo da un dispositivo qualsiasi e cambia per tutta la casa.
:::

## Cosa funziona fuori casa

Quando sei lontano dal Wi-Fi della vasca, il telefono non parla direttamente con l'attrezzatura. Un comando va a Cora Cloud, che lo passa a un Cora Max nella vasca. È quel Cora Max a raggiungere l'attrezzatura.

Ecco cosa significa per te.

- **Letture e storico** sono sempre disponibili, ovunque tu sia. Sono già salvati in Cora Cloud.
- **Comandare l'attrezzatura** funziona anche fuori casa, purché un Cora Max nella vasca sia online e possa raggiungere quell'attrezzatura. Vale per cose come accendere o spegnere una presa, avviare un'alimentazione, dosare da una testa o mettere in pausa una pompa. Se nessun Cora Max la raggiunge, il comando non può arrivare.
- **Le impostazioni proprie di un dispositivo** (le sue impostazioni native, non le sue letture) a volte richiedono un telefono sulla *stessa* rete del dispositivo. Un Cora Max nella vasca non basta per quelle. La pagina di quel dispositivo dice quando succede.

Due messaggi ti dicono che un comando non è andato liscio.

- **"Nulla è stato inviato"** vuol dire che il comando non è mai partito dal telefono, oppure che nessun Cora Max nella vasca ha potuto prenderlo. Non è stato eseguito niente. Lo vedi se il Cora Max principale della vasca è offline e nessun altro dispositivo su quella vasca può sostituirlo.
- **"Potrebbe essere già stato eseguito"** vuol dire che il comando è partito, ma nessun Cora Max l'ha confermato in tempo. Cora non sa davvero se è stato eseguito. Controlla l'attrezzatura stessa prima di riprovare, così non lo mandi due volte.

Se uno dei due messaggi continua a comparire, controlla che un Cora Max nella vasca sia online. Puoi anche impostare **Cora Max principale** su **Qualsiasi attivo (automatico)** così qualsiasi dispositivo online può prendere il comando. Tutti gli esiti possibili di un comando sono elencati in [Controllare la tua attrezzatura](/help/mobile-device-control).

## Dove si vede lo stato di ogni dispositivo

Cora Max mostra lo stato di lettura di ogni vasca in **Impostazioni → Impostazioni Cora Max → Stato**. Di più in [Dispositivi e salute dei dispositivi](/help/max-devices).
