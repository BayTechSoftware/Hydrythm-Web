---
title: Più di un dispositivo Cora
description: Scegli quale dispositivo risponde alla voce e quale interroga ogni vasca.
section: Cora Mobile
reviewed: 2026-09-27
order: 29
group: Account
---

Una casa può avere più di un Cora Max. Due impostazioni decidono chi fa cosa, così non duplicano il lavoro l'uno dell'altro, e una terza cosa che vale la pena sapere è cosa è condiviso tra di essi.

## Cosa è condiviso, e cosa non lo è

| Condiviso su ogni dispositivo | Appartiene a un singolo schermo |
|---|---|
| Vasche, letture e storico | Il suo layout di dashboard |
| Dispositivi e le loro impostazioni | Wi-Fi, luminosità, audio |
| Diario, popolazione, manutenzione | Parola di attivazione e blocco bambini |
| Avvisi, soglie, automazioni | Quali vasche mostra quello schermo |
| Piani e utilizzo | |

Cambiare una soglia su un dispositivo la cambia ovunque. Riorganizzare una dashboard no; ogni schermo mantiene il proprio layout, e il telefono e il Cora Max non ne condividono mai uno.

## Cora Assistant: dispositivo che risponde

**Impostazioni → Cora Assistant → Dispositivo di risposta** scegli quale **dispositivo Cora** risponde quando parli alla stanza. Solo uno risponde, per quanti possano sentirti; impostalo sull'unità più vicina a dove di solito ti trovi.

Questa è una scelta diversa dal Cora Max principale più sotto: il Dispositivo di risposta decide quale dispositivo risponde alla tua voce, e il Cora Max principale decide quale dispositivo interroga l'equipaggiamento di una vasca. Una casa con due tablet potrebbe volerli impostati diversamente.

![Il selettore del dispositivo che risponde](img/mobile-voice-responder.webp "Ogni dispositivo mostra cosa ascolta, e se è online.")

Ogni dispositivo nell'elenco mostra la parola di attivazione che ascolta, insieme a se è online. **Queste non sono tutte uguali.** Una parola di attivazione è addestrata nel dispositivo stesso, quindi diversi modelli Cora possono ascoltarne una diversa. Leggi la parola dalla riga del dispositivo stesso invece di supporre che la casa ne condivida una.

:::note Il tuo telefono non è in questo selettore
Il telefono non ascolta una parola di attivazione. Avvii una conversazione su di esso toccando, il che funziona sempre e non è influenzato da questa impostazione. Il selettore elenca solo l'hardware Cora capace di voce.
:::

## Cora Max principale

L'equipaggiamento sulla tua rete viene letto da un Cora Max. Quando più di uno potrebbe leggere lo stesso controller, altrimenti lo interrogherebbero in parallelo.

Il **Cora Max principale** è una scelta per vasca di quale dispositivo legge il controller di quella vasca. In Cora Mobile, apri la vasca e tocca **Cora Max principale**.

| Impostazione | Comportamento |
|---|---|
| Un dispositivo specifico | Diventa il solo dispositivo Cora che interroga il controller, e resta il principale anche mentre è offline: gli altri dispositivi Cora non prendono il suo posto. Cora Mobile interroga solo mentre è offline. |
| **Qualsiasi attivo (automatico)** | L'app e qualsiasi dispositivo Cora online condividono il lavoro (vince l'ultima scrittura), quindi se uno va offline un altro continua. Adatto a una casa con un solo dispositivo, e l'opzione predefinita più sicura quando non sei sicuro di quale dispositivo dovrebbe possederlo. |

Mentre un dispositivo che hai nominato è offline, un comando che deve passare attraverso di esso non viene eseguito: Cora ti dice che la vasca è impostata per usare quel dispositivo, che è offline, e che nulla è stato eseguito, così puoi riprovare una volta che è di nuovo attivo. Se resterà offline per un po', scegli un altro dispositivo oppure **Qualsiasi attivo (automatico)**.

:::note Imposta un principale quando due dispositivi osservano una vasca
Nominare un principale riduce il carico sul controller ed elimina le letture duplicate dalla stessa fonte.
:::

:::note Questa è un'impostazione per vasca a livello di account, non per dispositivo
Il Cora Max principale appartiene alla vasca, non al telefono o al tablet che stai guardando. Cambiarlo da qualsiasi dispositivo lo cambia per tutta la casa.
:::

## Cosa funziona lontano da casa

Il tuo telefono non parla direttamente con il tuo equipaggiamento quando sei lontano dal Wi-Fi proprio della vasca. Invece, un comando viaggia verso Cora Cloud, che lo passa a un Cora Max presente alla vasca; quel Cora Max è quello che effettivamente raggiunge l'equipaggiamento.

Questo significa:

- **Letture e storico** sono sempre disponibili, ovunque tu sia, perché sono già memorizzati in Cora Cloud.
- **Controllare l'equipaggiamento** (commutare una presa, avviare un'alimentazione, dosare una testa, sospendere una pompa) funziona anche lontano da casa, purché un Cora Max alla vasca sia online e possa raggiungere quell'equipaggiamento. Se nessuno lo è, il comando non può essere consegnato.
- **Le impostazioni native proprie di un dispositivo** (a differenza delle sue letture) a volte richiedono un telefono sulla *stessa* rete del dispositivo stesso, non solo un Cora Max alla vasca. Dove questo si applica, la pagina lo dice.

Due messaggi ti dicono che il comando non è semplicemente riuscito:

- **"Nulla è stato inviato"**: il comando non è mai partito dal tuo telefono, oppure nessun Cora Max alla vasca ha potuto riceverlo. Nulla è stato eseguito. Questo è ciò che vedrai se il Cora Max principale della vasca è offline e nessun altro dispositivo su quella vasca può intervenire.
- **"Potrebbe essere già stato eseguito"**: il comando è stato inviato, ma nessun Cora Max ha risposto in tempo per confermarlo. Cora davvero non sa se è stato eseguito. Controlla lo stato dell'equipaggiamento stesso prima di riprovare, così non lo invii due volte.

Se uno di questi messaggi continua ad apparire, controlla che un Cora Max alla vasca sia online, oppure imposta **Cora Max principale** su **Qualsiasi attivo (automatico)** così qualsiasi dispositivo online possa raccogliere il comando. Vedi [Controllare il tuo equipaggiamento](/help/mobile-device-control) per tutti gli esiti che un comando può avere.

## Dove viene mostrato lo stato di ogni dispositivo

Cora Max riporta il proprio stato di interrogazione e voce sotto **Impostazioni → Cora Max → Firmware → Salute dispositivo e controlli**. Vedi [Dispositivi e salute dei dispositivi](/help/max-devices).
