---
title: Avvisi e soglie
description: Imposta l'intervallo ideale di ogni lettura, scegli ogni quanto un avviso può notificarti e scopri perché un dispositivo "ha smesso di inviare dati".
section: Cora Mobile
reviewed: 2026-10-18
order: 22
group: Alerts and automation
twin: max-alerts
---

Ricevi un avviso quando una lettura esce dall'intervallo che hai impostato. Questa pagina spiega come impostare quegli intervalli, cosa succede quando scatta un avviso e quanto aspetta Cora prima di dire che un dispositivo ha smesso di inviare dati.

Per aprire il **Centro avvisi**, tocca **Avvisi** nella fila di pulsanti sotto la dashboard. Lo trovi anche in Impostazioni → la tua vasca → **Soglie di avviso**.

![La scheda Attivi del Centro avvisi in Cora Mobile](img/mobile-alerts.webp "Gli avvisi attivi, ognuno con la sua gravità, cosa l'ha fatto scattare e quando, più Vedi la regola e Spiega questo avviso.")

## Il Centro avvisi {#alert-center}

Ha due schede. **Attivi** elenca gli avvisi in corso in questo momento, con un badge con il numero. **Regole** contiene le regole che li fanno scattare.

Ogni avviso attivo mostra il parametro e la vasca, la lettura che l'ha fatto scattare, una breve spiegazione, un'etichetta con la gravità, il tipo di regola che è scattata (**Soglia** o **Velocità di variazione**) e quando è scattata. Ha due pulsanti:

- **Vedi la regola** apre la regola che c'è dietro, così puoi correggere l'intervallo. Su un avviso di una pompa dosometrica, come una testa DŌS o ReefDose quasi vuota o una dose mancata, questo pulsante è invece **Apri pompa dosometrica**. Apre la pagina di quella pompa dosometrica con i suoi avvisi.
- **Spiega questo avviso** apre Cora Assistant con una domanda sull'avviso pronta da inviare. Controllala, cambiala se vuoi, poi inviala.

## La scheda Regole {#rules}

![La scheda Regole](img/mobile-alert-rules.webp "Le regole raggruppate per parametro, ognuna con il suo interruttore.")

Le regole sono raggruppate per parametro. Ogni regola ha il suo interruttore sulla riga, così puoi spegnerne una senza aprirla. Una riga mostra anche **In corso** mentre il suo avviso è attivo, oppure quando è scattato l'ultima volta (o **Mai scattato**).

Le regole di una testa di dosaggio prendono il nome dalla testa e da quello che controllano, per esempio *Iodio · giorni rimanenti* o *Iodio · rimanente*. Una dose mancata compare come *Iodio · dose mancata*. Ogni DŌS e ogni ReefDose ha qui una sola riga, e gli avvisi delle sue teste non sono elencati uno per uno. Tocca la riga per aprire la pagina di quella pompa dosometrica. Vedi [Avvisi della pompa dosometrica](/help/mobile-device-control#doser-alerts).

In fondo:

- **Aggiungi le regole consigliate** aggiunge le regole consigliate da Cora che mancano. Salta un parametro che ha già una regola. Su una vasca senza nessuna regola, questo pulsante dice **Aggiungi regole predefinite**.
- **Aggiungi regola personalizzata** crea una regola tua. Scegli il parametro e il **Tipo di regola**, **Soglia** o **Velocità di variazione**. Il pulsante **Aggiungi regola** in basso a destra fa la stessa cosa.

### Modificare una regola {#editing-a-rule}

Tocca la riga di una regola per aprirla. Trovi:

- **Minimo dell'avviso** e **Massimo dell'avviso**, l'intervallo vero e proprio. Lasciane uno vuoto per un tetto o un minimo.
- **Consigliato**, che rimette l'intervallo suggerito da Cora.
- **Intervallo indicatore (display Cora)**, con **Minimo indicatore** e **Massimo indicatore**. Impostano solo la scala dell'indicatore su Cora Max. Non fanno mai scattare un avviso.
- **Attesa tra gli avvisi**, spiegata [più sotto](#cooldowns).
- **Attivato**, e un pulsante per eliminare.

Una regola per un guasto di un dispositivo, come un Trident senza reagente, non ha un intervallo. Scegli solo la sua attesa.

## Impostare un intervallo {#setting-a-range}

I parametri che Cora può valutare hanno un intervallo obiettivo. I valori predefiniti vengono dal tipo e dall'età della vasca quando la configuri, e sono un punto di partenza sensato. Se un parametro non ha un intervallo utilizzabile, Cora non lo valuta, e il suo widget resta grigio neutro.

Il modo più veloce per cambiare un intervallo è tenere premuto il widget del parametro sulla dashboard. Si aprono le sue soglie. Un tocco normale apre invece la pagina del parametro.

![Il pannello Modifica soglia per il pH in Cora Mobile](img/mobile-threshold-sheet.webp "Minimo e massimo dell'avviso, l'intervallo dell'indicatore per Cora Max e l'attesa tra gli avvisi.")

Se il parametro non ha ancora una regola, i campi partono dal valore predefinito di Cora e una nota sotto lo dice. Cambia un valore qualsiasi per impostare il tuo.

Puoi impostare:

- un intervallo, con un minimo e un massimo, per cose come alcalinità o temperatura
- un tetto, solo con il massimo, per cose per cui un valore basso va bene, come nitrati o fosfati
- un minimo, solo con il valore basso

:::tip Imposta l'intervallo in cui gira davvero la tua vasca
I valori predefiniti sono solo un punto di partenza. Una vasca a bassi nutrienti a 6 dKH non è "sbagliata" perché una tabella dice 8–9. Imposta l'intervallo in cui la tieni, e Cora ti avvisa quando sei *tu* a spostarti.
:::

## Cosa fa scattare un avviso {#what-triggers-an-alert}

Un avviso scatta quando una lettura supera una soglia. Cora controlla ogni lettura appena arriva, quindi basta una sola lettura fuori dal tuo intervallo.

Una regola sulla velocità di variazione guarda quanto in fretta si muove un parametro invece di dove si trova. Usala quando la velocità di un cambiamento conta più del numero.

Una volta attivo, un avviso non continua a notificarti per la stessa cosa. L'[attesa](#cooldowns) della regola decide quando può notificarti di nuovo.

## Dove compaiono gli avvisi

- La campanella, in alto a destra nelle schede principali, tiene lo storico. Il numero indica quanti non hai letto. Di più in [Notifiche](/help/mobile-notifications).
- Una notifica push arriva sul telefono se quella categoria è attiva.
- Il widget sulla dashboard diventa ambra o rosso.
- Cora Max mostra gli stessi avvisi sul suo schermo.

## Quando l'attrezzatura richiede attenzione {#equipment-faults}

Alcuni avvisi riguardano l'attrezzatura, non una lettura. Quando un dispositivo come un Trident o una pompa Jecod segnala un guasto, Cora invia una notifica con il nome della vasca e del dispositivo, per esempio *"Vasca Display: la pompa di risalita richiede attenzione"*. Dice anche cosa non va, come un rotore bloccato. Quando il guasto si risolve, ne ricevi una seconda: *"Vasca Display: la pompa di risalita è di nuovo a posto"*. Entrambe rientrano in **Guasti dell'apparecchiatura** in **Impostazioni → Notifiche**.

Un controller KH AquaWiz letto ogni ora dal tuo Cora Max dà lo stesso tipo di avviso quando:

- la sua pompa dosometrica segnala un guasto;
- la sua sonda pH si è guastata o è vicina a fine vita;
- il livello del suo contenitore dell'acqua resta basso o alto per più di un'ora.

Servono la lettura oraria da Cora Max (vedi [Controllare l'attrezzatura da Cora Max](/help/max-device-control#aquawiz-hourly)): la lettura dal cloud AquaWiz ogni 12 ore non li porta.


## Un dispositivo ha smesso di inviare dati {#stopped-reporting}

Quando un dispositivo collegato tace, Cora invia *"[Dispositivo]: ha smesso di inviare dati"*. Non vuol dire che il dispositivo sia rotto, solo che Cora non lo sente da un po'. Ricevi una seconda notifica, *"[Dispositivo]: invia di nuovo dati"*, quando torna.

Quanto aspetta Cora dipende dal dispositivo:

| Dispositivo | Cora aspetta |
|---|---|
| Neptune Apex | Circa 30 minuti senza un aggiornamento |
| Red Sea ReefBeat | Circa 30 minuti |
| AquaWiz | Circa 25 ore, perché AquaWiz lascia leggere il suo cloud a Cora solo ogni 12 ore |
| Pompe Jecod | Tre letture mancate di fila, sull'intervallo di lettura della pompa (90 minuti con il valore predefinito di 30) |
| Presa Zigbee | Non è tornata 30 minuti dopo il riavvio dell'hub. Dalle un nome con **Rinomina** perché l'avviso la indichi |

Cosa controllare dipende da come Cora legge il dispositivo.

- Apex, ReefBeat e Jecod sono letti da un Cora Max via Wi-Fi. Controlla l'alimentazione e il Wi-Fi del dispositivo, e che il Cora Max che lo legge sia acceso e online.
- AquaWiz è letto tramite il tuo account presso il produttore. Controlla la connessione dell'account nella pagina del dispositivo in Cora Mobile.


Queste notifiche rientrano in **Guasti dell'apparecchiatura** in **Impostazioni → Notifiche**.


Una vasca Red Sea può anche mostrare un banner, *"I valori Red Sea non si aggiornano più"*, quando nessun telefono e nessun Cora Max sta leggendo la sua attrezzatura ReefBeat. Toccalo per scegliere un **Cora Max principale**. La soluzione completa è in [Risoluzione dei problemi](/help/troubleshooting#red-sea-readings-have-stopped-updating).

## Scegliere cosa ti arriva {#choosing-what-reaches-you}

In **Impostazioni → Notifiche** scegli quali categorie possono mandarti una notifica push. Vedi [Notifiche](/help/mobile-notifications), che spiega anche come [tenere tranquille le notti](/help/mobile-notifications#quiet-at-night).

Reef Buddy non ha un interruttore suo. Il suo orario è la riga **Orario del riepilogo**, subito sotto Notifiche nelle Impostazioni. Con il piano gratuito non c'è la notifica del briefing.

:::note Cora resta in silenzio a meno che qualcosa non sia cambiato
Il briefing giornaliero è una notifica per vasca al giorno. In un giorno in cui niente richiede la tua attenzione, di solito resta in silenzio invece di dirti che va tutto bene. Se Cora ti manda notifiche, qualcosa è cambiato.
:::

## Attese: ogni quanto lo stesso avviso può notificarti {#cooldowns}

Ogni regola ha la sua **Attesa tra gli avvisi**. La imposti quando aggiungi o modifichi la regola. Una regola che non ne ha mai avuta una usa 1 h.

L'attesa non nasconde l'avviso. Limita solo quanto spesso Cora ti manda notifiche. La lettura continua a essere valutata, e l'avviso resta sul widget e nella campanella per tutto il tempo.

Puoi scegliere 15 min, 30 min, 1 h, 2 h, 4 h, 8 h, 1 giorno, 3 giorni o 1 settimana.

Un'attesa breve va bene per una lettura che si muove in fretta, come la temperatura. Una lunga, fino a una settimana, va bene per qualcosa che resta sbagliato per giorni mentre aspetti un ricambio, come un Trident senza reagente o un contenitore di dosaggio vuoto.

:::note Rinvia è su Cora Max
Cora Mobile non ha un pulsante Rinvia su un avviso attivo. Rinvia è sullo schermo del Cora Max vicino alla vasca, e silenzia l'avviso per l'attesa che hai scelto qui. Sul telefono, l'attesa di ogni regola è il modo per cambiare quanto spesso ne senti parlare.
:::

## Chiudere un avviso {#clearing-an-alert}

Un avviso si chiude da solo quando la lettura torna nell'intervallo. Non c'è niente da archiviare. Quando succede ricevi una notifica, per esempio *"Vasca Display: alcalinità tornata nella norma"*. Se il problema ritorna più avanti, ricevi un nuovo avviso.

:::note Anche i picchi brevi fanno scattare avvisi
Basta una lettura fuori intervallo per far scattare un avviso, quindi una sonda che ha un picco ne fa scattare uno. Se una fonte non è affidabile, ricalibrala o fai seguire al parametro una fonte diversa. Non allargare la soglia.
:::

A volte la lettura è sbagliata e la vasca sta bene, per esempio quando una sonda va calibrata. In quel caso sistema la fonte. Se allarghi una soglia per zittire una sonda difettosa, perderai anche il prossimo problema vero.

## Spegnere un avviso {#turning-an-alert-off}

Spegni l'interruttore sulla riga della regola nella scheda **Regole**. Cora conserva la regola e il suo intervallo, così puoi riattivarla senza reimpostarla.

Finché una regola è spenta, Cora non valuta quella lettura. Il suo widget resta grigio neutro e non fa mai scattare un avviso.

:::warning Spegni un parametro senza eliminare il suo intervallo
Eliminare una regola non sempre impedisce a Cora di valutare quella lettura. Le fasce di riferimento predefinite continuano a colorare il valore e possono ancora finire nel briefing. Usa l'interruttore della regola.
:::
