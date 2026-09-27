---
title: Avvisi e soglie
description: Imposta l'intervallo per ogni parametro, scegli di cosa vuoi essere informato, e capisci perché è scattato un avviso.
section: Cora Mobile
reviewed: 2026-09-27
order: 15
group: Alerts and automation
---

Un avviso viene generato quando una lettura esce dall'intervallo che hai impostato per essa. Imposti tu gli intervalli, e controlli tu quali avvisi arrivano al tuo telefono.

Apri il **Centro avvisi** dalla riga di scorciatoie in fondo alla dashboard.

![Il Centro avvisi](img/mobile-alerts.webp "Avvisi attivi, ciascuno con la sua gravità, cosa lo ha attivato, e quando.")

## Il Centro avvisi

Due schede:

- **Attivi**: avvisi attualmente generati, con un badge del conteggio
- **Regole**: le soglie e le regole di velocità di variazione che li producono

Ogni avviso attivo mostra il parametro e la vasca, la lettura che l'ha attivato, una spiegazione semplice, un chip di gravità, il tipo di regola che è scattata (**Soglia** o **Velocità di variazione**), e l'ora in cui è scattato.

Due azioni su ciascuno:

- **Vedi la regola**: apre la regola che l'ha generato, così puoi correggere l'intervallo
- **Spiega questo avviso**: chiede all'Assistente di interpretarlo rispetto allo storico della tua vasca

## Impostare un intervallo

I parametri che Cora può valutare hanno un intervallo obiettivo, e i valori predefiniti provengono dal tipo e dall'età della tua vasca quando l'hai configurata, di solito un buon punto di partenza. Un parametro senza un intervallo utilizzabile non viene valutato affatto: resta grigio neutro invece di essere indovinato.

Per cambiarne uno: **tieni premuto il suo widget** sulla dashboard, che apre direttamente le soglie di quel parametro. Un tocco semplice apre invece la vista del parametro; i due gesti portano a posti diversi, e la pressione prolungata è la scorciatoia da ricordare.

Se il parametro non ha ancora una regola, i campi partono dal valore predefinito di Cora, e una nota sotto di essi lo indica. Cambia qualsiasi valore per impostare il tuo.

Per vederli tutti insieme, usa **Avvisi** nella riga di pulsanti sotto la dashboard.

Puoi impostare:

- **Un intervallo**: un minimo e un massimo, per cose come alcalinità o temperatura
- **Un tetto**: solo un massimo, per cose dove basso va bene, come nitrati o fosfati
- **Un minimo**: solo un valore basso

:::tip Imposta l'intervallo su cui la tua vasca funziona davvero
I valori predefiniti sono un punto di partenza, non un giudizio. Una vasca a basso contenuto di nutrienti a 6 dKH non è "sbagliata" perché un grafico diceva 8-9. Imposta l'intervallo su cui funzioni davvero, e Cora ti dirà quando sei *tu* a derivare.
:::

## Cosa attiva un avviso

Un avviso scatta quando una lettura supera una soglia. Cora controlla ogni lettura non appena arriva, quindi una singola lettura fuori dal tuo intervallo è sufficiente per generarne uno.

Una volta generato, un avviso non continuerà a notificarti sulla stessa cosa; c'è un'attesa prima che possa scattare di nuovo. E **si chiude da solo** nel momento in cui una lettura torna dentro l'intervallo; non c'è nulla da confermare.

Puoi anche impostare una regola di **velocità di variazione**, che osserva quanto velocemente si muove un parametro invece di dove si trova attualmente. È quella da usare per le cose dove la velocità di un cambiamento conta più del numero.

## Dove appaiono gli avvisi

- **La campana**, in alto a destra di ogni schermata, contiene il tuo storico. Il numero indica quanti non hai letto.
- **Le notifiche push** arrivano al tuo telefono quando le consenti.
- **Il widget** diventa ambra o rosso sulla dashboard.
- **Cora Max** mostra gli stessi avvisi sullo schermo grande.

## Quando l'equipaggiamento ha bisogno di attenzione

Alcuni avvisi riguardano l'equipaggiamento invece di una lettura. Quando un dispositivo come un Trident o una pompa Jecod riporta un guasto, Cora invia una notifica che nomina la vasca e il dispositivo, per esempio *"Vasca Display: la pompa di risalita ha bisogno di attenzione"*, e dice cosa non va, come un rotore inceppato. Quando il guasto si risolve, ne segue una seconda: *"Vasca Display: la pompa di risalita è di nuovo a posto"*. Entrambe rientrano in **Guasti dell'apparecchiatura** in **Impostazioni → Notifiche**.

Una gyre Maxspect (beta) può generare lo stesso avviso quando un Cora Max sulla sua rete trova entrambe le teste impostate a 0%, oppure non ottiene risposta dalla gyre due volte di fila. Trattalo come un avvertimento, non come una garanzia: il Cora Max controlla di tanto in tanto invece che continuamente, e solo mentre è in funzione e può raggiungere la gyre.

## "Le letture Red Sea hanno smesso di aggiornarsi"

Potresti vedere questo banner sulla pagina di un parametro di una vasca:

> Le letture Red Sea hanno smesso di aggiornarsi. Nessun dispositivo sta attualmente leggendo i dispositivi Red Sea di questa vasca: controlla il Cora Max principale in Impostazioni, oppure apri questa vasca su un dispositivo sullo stesso Wi-Fi.

Significa che nessun telefono o Cora Max sta attualmente interrogando l'equipaggiamento ReefBeat di quella vasca, quindi le letture mostrate sono vecchie, non necessariamente sbagliate. Tocca il banner per aprire **Cora Max principale** e scegli un dispositivo che è attivo, oppure impostalo su **Qualsiasi attivo (automatico)**. Vedi [Più di un dispositivo Cora](/help/mobile-multi-device). Se non si chiude, vedi [Risoluzione dei problemi](/help/troubleshooting).

## Scegliere cosa ti raggiunge

**Impostazioni → Notifiche.** Puoi controllare:

- Quali delle categorie di notifica possono inviare notifiche push

Reef Buddy non ha un proprio interruttore: invia un briefing quando c'è qualcosa che vale la pena affrontare e resta silenzioso quando non c'è.

:::note Cora è progettato per restare silenzioso
Il briefing giornaliero è una notifica push per vasca al giorno, e in un giorno in cui nulla richiede la tua attenzione di solito resta in silenzio invece di dirti che tutto va bene. Se Cora invia una notifica, qualcosa è cambiato.
:::

## Attese: quanto spesso lo stesso avviso può notificarti

Ogni regola ha la propria **Attesa tra gli avvisi**, impostata quando aggiungi o modifichi la regola (nella scheda **Regole** del Centro avvisi). L'attesa non nasconde l'avviso stesso: limita solo quanto spesso Cora ti invia una notifica push su di esso. La lettura resta valutata e l'avviso resta visibile sul widget e nella campana per tutto il tempo.

Puoi scegliere tra: 15 min, 30 min, 1 h, 2 h, 4 h, 8 h, 1 giorno, 3 giorni, oppure **1 settimana**.

Un'attesa breve è adatta a una lettura che si muove rapidamente come la temperatura. Una lunga, fino a una settimana, è adatta a qualcosa che resta sbagliato per giorni mentre aspetti un pezzo di ricambio, come un Trident senza reagente o un contenitore di dosaggio vuoto: senza un'attesa lunga, Cora ti invierebbe notifiche sullo stesso problema noto più volte al giorno.

:::note Rinviare un avviso attivo vive su Cora Max
Cora Mobile non ha un proprio pulsante Rinvia su un avviso attivo; quel controllo si trova sullo schermo del Cora Max alla vasca, e silenzia lo stesso avviso per la durata di attesa che hai scelto qui. Dal telefono, il modo per cambiare quanto spesso senti parlare di qualcosa è questa attesa per regola, non un rinvio per singolo avviso.
:::

## Chiudere un avviso

Un avviso si chiude quando la lettura torna nell'intervallo. Non c'è nulla da ignorare; è un'affermazione sulla vasca, non un compito.

:::note Le letture transitorie generano avvisi
Una singola lettura fuori intervallo è sufficiente per generare un avviso, quindi una sonda che ha un picco ne attiverà uno. Se una fonte non è affidabile, calibrala di nuovo o punta il widget su una fonte diversa invece di allargare la soglia.
:::

Se una lettura è sbagliata invece che la vasca sia sbagliata (una sonda che ha bisogno di calibrazione, per esempio), correggi la fonte. Allargare una soglia per silenziare una sonda difettosa nasconde anche il prossimo problema reale.

## Disattivare gli avvisi per un parametro

Apri la regola nella scheda **Regole** del Centro avvisi e disattiva il suo **interruttore di attivazione**. La regola e il suo intervallo vengono conservati, così puoi riattivarla senza ricrearla.

:::warning Silenzia un parametro senza eliminare il suo intervallo
Rimuovere una soglia non necessariamente ferma ogni valutazione di quella lettura; le fasce di riferimento predefinite continuano a colorare il valore e possono ancora alimentare il briefing. Usa l'interruttore di attivazione della regola.
:::
