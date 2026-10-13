---
title: Automazioni e scene
description: Fai agire Cora da sola quando cambia una lettura, scatta un avviso, arriva un'ora o un dispositivo va offline, e raggruppa le azioni in scene che avvii con un tocco.
section: Cora Mobile
reviewed: 2026-10-13
order: 22
group: Alerts and automation
twin: max-automation
---

Un'automazione è una regola che Cora esegue per te: *quando succede questo, controlla quello, poi fai quest'altro.* Una scena raggruppa più azioni in un'unica cosa che avvii quando vuoi.

Vai in **Impostazioni → Automazioni**.

![La schermata Automazioni in Cora Mobile, con le schede Automazioni e Scene](img/mobile-automation.webp "Automazioni e Scene sono schede separate. Ogni regola ha il suo interruttore.")

La schermata ha due schede, **Automazioni** e **Scene**, con un pulsante **Nuova automazione** o **Nuova scena**. Ogni regola mostra un riassunto di una riga, un interruttore di attivazione e un menu per **Modifica** o **Elimina**. Una regola che non è ancora stata eseguita lo dice.

:::warning Le regole agiscono sull'attrezzatura vera
Se una regola accende o spegne una pompa, la pompa lo fa anche quando non stai guardando. Crea una regola alla volta e controlla che faccia quello che ti aspetti prima di aggiungere la successiva.
:::

## Com'è fatta una regola {#shape}

Ogni automazione ha tre parti.

- Il trigger la fa partire.
- Le condizioni devono essere anch'esse vere.
- Le azioni sono quello che fa poi, in ordine.

![Un modulo Nuova automazione vuoto in Cora Mobile](img/mobile-rule-builder.webp "Una nuova automazione: trigger, condizioni Se, azioni Allora, Altrimenti-se e Altrimenti, poi l'attesa e la fascia oraria.")

## Cosa può far partire una regola {#triggers}

Aggiungi uno o più trigger in **Quando: qualsiasi trigger**. Uno qualsiasi di questi avvia la regola.

| Trigger | Scatta quando |
|---|---|
| **Quando un parametro cambia** | Un parametro supera un valore che imposti. Scegli la **Direzione**: **In aumento**, **In diminuzione** o **Qualsiasi variazione** |
| **Quando un avviso scatta** | Un avviso è **Generato**, **Risolto**, o entrambi. Puoi limitarlo agli avvisi di **Soglia** o di **Velocità di variazione** |
| **A un'ora del giorno** | Un'ora del giorno, nel tuo fuso orario |
| **Quando un dispositivo va offline** | Il tuo Cora Max va **Offline**, torna **Online**, o in entrambi i casi |

:::tip Fatti avvisare quando il tuo Cora Max si scollega
Una regola con **Quando un dispositivo va offline** e **Avvisami** ti dice quando il Cora Max che legge la tua attrezzatura perde la corrente o il Wi-Fi.
:::

## Condizioni {#conditions}

Le condizioni decidono se le azioni vengono eseguite. Tocca **Aggiungi condizione** e scegli:

- **Confronto parametro**, una lettura sopra, sotto o uguale a un valore
- **Parametro dentro / fuori un intervallo**
- **Avviso attivo**
- **Presa acceso / spento**, per una presa Apex
- **Ora del giorno**, una fascia come dalle 22:00 alle 06:00
- **Come è andato un passo precedente**, che controlla se un passo precedente è andato **OK** o è stato **Saltato**. Usalo per "prova questo, e se non ha funzionato, fai invece quest'altro"

Con più condizioni, imposta **Corrispondenza** su **Tutte (E)** o **Una qualsiasi (O)**.

## Rami e controlli per singolo passo {#branches}

Un'automazione può fare cose diverse in casi diversi. Il suo primo blocco è **Se**. Tocca **Altrimenti-se** per aggiungere un altro caso, oppure aggiungi un blocco **Altrimenti** per tutto il resto. Cora esegue il primo blocco le cui condizioni sono vere.

Puoi anche condizionare una singola azione. Tocca **Solo se…** su quel passo e dagli una condizione sua. Senza condizione, il passo viene sempre eseguito.

## Quando può essere eseguita {#when-it-may-run}

- **Attesa tra le esecuzioni** impedisce a una regola di scattare di nuovo troppo presto. Parte da 10 min.
- **Esegui solo tra** limita la regola a una fascia oraria, per esempio solo di giorno.
- **Testa con i valori in tempo reale** prova la regola sulle letture attuali della vasca, senza fare niente. Ti dice cosa *verrebbe eseguito*, o perché non verrebbe eseguito niente.

## Cosa può fare una regola {#actions}

Un'azione che richiede un'attrezzatura compare solo su una vasca che ha quell'attrezzatura.

| Azione | Cosa fa |
|---|---|
| **Controlla apparecchiatura Apex** | Accende o spegne una presa |
| **Esegui ciclo di alimentazione Apex** | Avvia un'alimentazione. L'Apex la termina con il suo timer |
| **Esegui un test Trident** | Avvia un test. Ogni esecuzione consuma reagente |
| **Dosa una testa DŌS** | Esegue una dose misurata su una testa DŌS |
| **Controlla un'apparecchiatura Red Sea** | Comanda un'unità ReefBeat |
| **Controlla una pompa di movimento** | Imposta flusso, modalità onda o potenza di una pompa Jecod, oppure **Pausa per l'alimentazione**. Il Cora Max nella vasca rimette la pompa com'era quando l'alimentazione finisce |
| **Controlla un’apparecchiatura GHL (Beta)** | Mette in pausa un programma di alimentazione, avvia la modalità manutenzione o cambio d'acqua, imposta una scena o la luminosità delle luci, e altro |
| **Controlla un'apparecchiatura HYDROS (Beta)** | Imposta un'uscita, la riporta al suo programma, cambia modalità, esegue un comando del tester o dosa da una testa |
| **Controlla un dispositivo EcoTech (Beta)** | Imposta intensità o scena di una Radion, avvia un'alimentazione o una modalità VorTech, dosa da un Versa, o riporta uno qualsiasi di questi al suo programma |
| **Avvisami** | Ti invia una notifica push con il tuo **Titolo** e **Messaggio** |
| **Attendi prima del passo successivo** | Fa una pausa prima di continuare |
| **Esegui una scena** | Avvia una scena dall'interno di questa regola |
| **Gestisci un'automazione** | Attiva o disattiva un'altra regola |
| **Crea un'attività di manutenzione** | Mette un lavoro nell'elenco della [manutenzione](/help/mobile-maintenance) della vasca, per esempio cambiare il materiale dello scrubber di CO2 quando il pH scende sotto un valore |

:::note Beta
GHL, HYDROS ed EcoTech sono in Beta e sono disponibili solo per gli utenti Beta. Se non sei un utente Beta non li vedrai in **Aggiungi dispositivo**. Per chiedere l'accesso alla Beta, contatta l'[assistenza](/support.html). Di più in [Funzioni Beta](/help/mobile-beta).
:::

:::warning Una dose non si può annullare, ed è limitata
Non puoi togliere una dose dalla vasca. Una regola può dosare solo da una testa che è stata misurata con **Misura per dosare** su un Cora Max. La dose viene eseguita da un Cora Max nella vasca. Il dosaggio dalle regole è limitato a **10 mL per testa al giorno**, comunque sia scritta la regola.
:::

:::note Cosa fa Crea un'attività di manutenzione
Scegli la vasca, poi **Attività esistente** (un'attività esistente diventa subito in scadenza) o **Nuova attività** (dagli un **Nome attività**). Una nuova attività è una tantum, in scadenza subito, e la regola non la ricrea finché è ancora aperta. Ricevi una sola notifica, e l'attività una tantum esce dall'elenco quando la completi.
:::

:::note L'attesa è breve
**Attendi prima del passo successivo** fa una pausa fino a 60 secondi, e un ramo può aspettare 60 secondi in totale. Dopo la pausa, il passo successivo vede letture fresche. Per una pausa più lunga, come una pompa di risalita spenta per 30 minuti durante un cambio d'acqua, usa una scena con **Esegui per** (sotto).
:::

## Scene {#scenes}

Una scena è un gruppo di azioni con un nome, come "Cambio d'acqua", "Modalità foto" o "Notte". Tocca **Nuova automazione** o **Nuova scena** e scegli **Scena** in alto. Una scena non ha trigger. La avvii con **Esegui ora** nell'elenco, dall'interno di una regola con **Esegui una scena**, oppure secondo un orario tramite una regola con **A un'ora del giorno**.

**Esegui per** imposta quanto dura una scena: un numero di minuti o di ore, oppure **Finché non lo cambio**. Allo scadere del tempo, Cora rimette le prese della scena com'erano. L'altra attrezzatura resta come l'ha lasciata la scena. Mentre una scena a tempo è in corso, l'elenco mostra un conto alla rovescia e un pulsante **Ferma** che la termina prima.

Se una scena accende o spegne una presa importante, come un riscaldatore, un refrigeratore, una pompa di risalita o il rabbocco, Cora chiede conferma prima di eseguirla ed elenca quei passi. Puoi disattivarlo con **Chiedi prima di eseguire** sulla scena.

Una scena può richiamarne un'altra, fino a 3 livelli. Cora non esegue una scena che richiama se stessa, perché potrebbe andare in loop e continuare ad agire sulla vasca.

Dopo che una scena è stata eseguita, vedi cosa è successo passo per passo, compreso quello che non è riuscito o non è stato eseguito.

## Scene create su Cora Max {#scenes-on-cora-max}

Puoi creare e modificare scene anche su un Cora Max. È lo stesso insieme di scene, condiviso in tutto l'account. Un Cora Max più vecchio può comunque eseguire una scena creata sul telefono. La modifica sul dispositivo però è più recente, quindi un Cora Max più vecchio potrebbe mostrare una scena senza permetterti di cambiarla. Modificala invece dal telefono.

## Disattivare una regola {#turning-a-rule-off}

Ogni regola ha un interruttore di attivazione. Disattivare una regola ne conserva le impostazioni, il che è comodo quando la vuoi di nuovo la prossima stagione.

## Vedere cosa ha fatto una regola {#seeing-what-a-rule-did}

Ogni azione eseguita da una regola viene registrata con **Regola di automazione** come origine. La trovi in [Attività](/help/mobile-activity).
