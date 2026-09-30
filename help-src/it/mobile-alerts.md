---
title: Avvisi e soglie
description: Imposta l'intervallo di ogni parametro, scegli quali avvisi ricevere e capisci perché ne è scattato uno.
section: Cora Mobile
reviewed: 2026-09-30
order: 15
group: Alerts and automation
---

Un avviso scatta quando una lettura esce dall'intervallo che hai impostato. Gli intervalli li decidi tu, e sei sempre tu a scegliere quali avvisi arrivano sul telefono.

Il **Centro avvisi** si apre dalla riga di scorciatoie in fondo alla dashboard.

![Il Centro avvisi](img/mobile-alerts.webp "Avvisi attivi, ciascuno con la sua gravità, cosa lo ha attivato, e quando.")

## Il Centro avvisi

Ha due schede:

- **Attivi**: gli avvisi in corso, con il numero sul badge
- **Regole**: le soglie e le regole sulla velocità di variazione che li fanno scattare

Per ogni avviso attivo vedi parametro e vasca, la lettura che l'ha fatto scattare, una spiegazione semplice, un'etichetta con la gravità, il tipo di regola (**Soglia** o **Velocità di variazione**) e l'ora.

Su ogni avviso puoi fare due cose:

- **Vedi la regola** apre la regola che l'ha fatto scattare, così puoi correggere l'intervallo
- **Spiega questo avviso** chiede all'Assistente di leggerlo alla luce dello storico della tua vasca

## Impostare un intervallo

I parametri che Cora può valutare hanno un intervallo obiettivo. I valori predefiniti dipendono dal tipo e dall'età della vasca che hai indicato alla configurazione, e di solito sono un buon punto di partenza. Se un parametro non ha un intervallo utilizzabile, Cora non lo valuta: resta grigio e Cora non tira a indovinare.

Per cambiarlo, **tieni premuto il widget** sulla dashboard: si aprono direttamente le soglie di quel parametro. Con un tocco normale apri invece la pagina del parametro. Sono due gesti diversi, e la pressione prolungata è la scorciatoia da ricordare.

Se il parametro non ha ancora una regola, i campi partono dal valore predefinito di Cora e una nota sotto lo segnala. Cambia un valore qualsiasi per usare il tuo.

Per vederli tutti insieme, tocca **Avvisi** nella riga di pulsanti sotto la dashboard.

Puoi impostare:

- **Un intervallo**, con minimo e massimo, per esempio per alcalinità o temperatura
- **Un tetto**, solo il massimo, per valori che possono stare bassi come nitrati o fosfati
- **Un minimo**, solo il valore basso

:::tip Imposta l'intervallo in cui gira la tua vasca
I valori predefiniti sono solo un punto di partenza. Una vasca a bassi nutrienti a 6 dKH non è "sbagliata" solo perché una tabella dice 8–9. Imposta l'intervallo in cui tieni davvero la vasca, e Cora ti avvisa quando sei *tu* a spostarti.
:::

## Quando scatta un avviso

Un avviso scatta quando una lettura supera una soglia. Cora controlla ogni lettura appena arriva, quindi basta una sola lettura fuori intervallo.

Una volta scattato, l'avviso non continua a notificarti per la stessa cosa: prima che possa scattare di nuovo passa un periodo di attesa. E **si chiude da solo** appena una lettura torna nell'intervallo. Non devi confermare niente.

Puoi anche impostare una regola sulla **velocità di variazione**, che guarda quanto in fretta si muove un parametro e non il suo valore attuale. Usala quando conta più la velocità del cambiamento del numero in sé.

## Dove compaiono gli avvisi

- **La campanella** in alto a destra in ogni schermata raccoglie lo storico. Il numero indica quanti non hai ancora letto.
- **Le notifiche push** arrivano sul telefono, se le hai permesse.
- **Il widget** sulla dashboard diventa ambra o rosso.
- **Cora Max** mostra gli stessi avvisi sullo schermo grande.

## Quando l'attrezzatura ha un problema

Alcuni avvisi riguardano l'attrezzatura e non una lettura. Quando un dispositivo come un Trident o una pompa Jecod segnala un guasto, Cora ti manda una notifica con il nome della vasca e del dispositivo, per esempio *"Vasca Display: la pompa di risalita ha bisogno di attenzione"*, e ti dice cosa non va, come un rotore bloccato. Quando il guasto si risolve, arriva una seconda notifica: *"Vasca Display: la pompa di risalita è di nuovo a posto"*. Tutte e due rientrano in **Guasti dell'apparecchiatura** in **Impostazioni → Notifiche**.

Una gyre Maxspect (beta) può dare lo stesso avviso quando un Cora Max sulla sua rete trova entrambe le teste impostate a 0% o quando la gyre non risponde per due volte di fila. Consideralo un avvertimento e non una protezione. Il Cora Max controlla ogni tanto e non di continuo, e solo quando è acceso e riesce a raggiungere la gyre.

## Un dispositivo ha smesso di comunicare

Se un Neptune Apex, un'unità Red Sea ReefBeat, un AquaWiz, una pompa Jecod o una gyre Maxspect smette di rispondere, Cora ti avvisa: *"[Dispositivo]: ha smesso di comunicare."* Controlla la sua alimentazione e il Wi-Fi, e che il Cora Max che lo legge sia acceso. La maggior parte dell'attrezzatura riceve questo avviso dopo circa 30 minuti senza aggiornamenti. AquaWiz controlla meno spesso, quindi aspetta circa 3 ore. Quando torna a comunicare ricevi una seconda notifica.

Questo rientra in **Guasti dell'apparecchiatura** in **Impostazioni → Notifiche**, insieme agli avvisi di guasto qui sopra.

## "Le letture Red Sea hanno smesso di aggiornarsi"

Nella pagina di un parametro potresti vedere questo banner:

> Le letture Red Sea hanno smesso di aggiornarsi. Nessun dispositivo sta attualmente leggendo i dispositivi Red Sea di questa vasca: controlla il Cora Max principale in Impostazioni, oppure apri questa vasca su un dispositivo sullo stesso Wi-Fi.

Vuol dire che al momento nessun telefono e nessun Cora Max sta leggendo l'attrezzatura ReefBeat di quella vasca. Le letture che vedi sono vecchie, ma non per forza sbagliate. Tocca il banner per aprire **Cora Max principale**, poi scegli un dispositivo acceso oppure **Qualsiasi attivo (automatico)**. Trovi i dettagli in [Più di un dispositivo Cora](/help/mobile-multi-device). Se il banner resta, guarda in [Risoluzione dei problemi](/help/troubleshooting).

## Scegliere cosa ricevere

In **Impostazioni → Notifiche** scegli quali categorie di notifica possono mandarti notifiche push.

Reef Buddy non ha un interruttore suo. Manda un briefing quando c'è qualcosa da fare e resta zitto quando non c'è.

:::note Cora parla solo quando serve
Il briefing giornaliero è al massimo una notifica push per vasca al giorno. Nei giorni in cui non c'è niente da guardare, di solito non arriva proprio: Cora non ti scrive solo per dirti che va tutto bene. Se Cora ti manda una notifica, qualcosa è cambiato.
:::

## Attesa: ogni quanto lo stesso avviso ti può notificare

Ogni regola ha la sua **Attesa tra gli avvisi**, che imposti quando aggiungi o modifichi la regola nella scheda **Regole** del Centro avvisi. L'attesa non nasconde l'avviso. Limita solo quante notifiche push ricevi. La lettura continua a essere valutata e l'avviso resta visibile sul widget e nella campanella.

Puoi scegliere 15 min, 30 min, 1 h, 2 h, 4 h, 8 h, 1 giorno, 3 giorni oppure **1 settimana**.

Un'attesa breve va bene per una lettura che cambia in fretta, come la temperatura. Una lunga, fino a una settimana, serve per un problema che resta per giorni mentre aspetti un ricambio, come un Trident senza reagente o un contenitore di dosaggio vuoto. Con un'attesa breve Cora ti avviserebbe dello stesso problema più volte al giorno.

:::note Il rinvio di un avviso si fa su Cora Max
In Cora Mobile gli avvisi attivi non hanno un pulsante per rinviarli. Quel comando è sullo schermo del Cora Max vicino alla vasca, e silenzia l'avviso per l'attesa che hai scelto qui. Dal telefono decidi ogni quanto sentirne parlare con l'attesa della regola.
:::

## Chiudere un avviso

Un avviso si chiude quando la lettura torna nell'intervallo. Non c'è niente da archiviare: l'avviso descrive lo stato della vasca e non è un compito da spuntare.

:::note Anche una lettura isolata fa scattare un avviso
Basta una lettura fuori intervallo per far scattare un avviso, quindi anche un picco della sonda ne genera uno. Se una fonte non è affidabile, ricalibrala o collega il widget a un'altra fonte. Non allargare la soglia.
:::

Se a essere sbagliata è la lettura e non la vasca (per esempio una sonda da calibrare), sistema la fonte. Se allarghi la soglia per zittire una sonda difettosa, nascondi anche il prossimo problema vero.

## Disattivare gli avvisi di un parametro

Apri la regola nella scheda **Regole** del Centro avvisi e spegni il suo **interruttore di attivazione**. Regola e intervallo restano salvati, così puoi riattivarla senza rifarla da capo.

:::warning Silenzia il parametro senza cancellare l'intervallo
Se elimini una soglia, la lettura può comunque essere valutata. Le fasce di riferimento predefinite continuano a colorare il valore e possono finire nel briefing. Usa l'interruttore di attivazione della regola.
:::
