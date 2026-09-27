---
title: Aggiornamenti e ripristino
description: Come si aggiorna da solo Cora Max, e cosa succede se un aggiornamento va male.
section: Cora Max
reviewed: 2026-09-09
order: 14
group: Settings
---

## Aggiornamenti automatici

Cora Max si mantiene aggiornato da solo. Le nuove versioni si scaricano in background e si installano da sole; ti viene detto cosa è cambiato.

Non è richiesto nulla da parte tua per restare aggiornato.

## Controllare la versione

![Impostazioni del dispositivo](img/max-updates.webp "Aggiornamento firmware e salute del dispositivo, in alto nelle impostazioni del dispositivo.")

**Impostazioni → Cora Max → Firmware → Aggiornamento firmware** riguarda il controllo, l'installazione, il canale di aggiornamento e la sua pianificazione. **Salute dispositivo e controlli** sta proprio accanto, nello stesso gruppo **Firmware**, ed è dove vive la diagnostica propria dell'unità: polling principale, collegamenti dei dispositivi e dispositivo di risposta inclusi.

## Quando è disponibile un aggiornamento

Appare un avviso che descrive cosa c'è di nuovo, con due scelte:

- **Aggiorna ora**: installa immediatamente e riavvia
- **Rinvia 3 ore**: chiede di nuovo più avanti

Lasciato in pace, un aggiornamento si installa da solo durante la notte, tra circa le 3 e le 5 del mattino, così lo schermo non si riavvia mentre lo stai guardando.

:::note Le letture non vengono perse durante un aggiornamento
I dati vivono nel tuo account, non sullo schermo. Un'unità che si riavvia torna con le stesse vasche, dashboard e storico.
:::

## Ripristino

Il ripristino è una modalità di manutenzione per quando un'unità non si avvia normalmente, oppure quando devi riparare la sua configurazione senza un computer.

**Per entrarci:** tieni **cinque dita** in alto a destra dello schermo per circa **dieci secondi**, poi inserisci il **PIN di ripristino** dell'unità.

Quel PIN di sei cifre è stato mostrato quando l'unità è stata associata, ed è anche nelle impostazioni di quel dispositivo in Cora Mobile. Non viene mostrato su Cora Max stesso, che è il punto: il ripristino non può essere raggiunto da un ospite, o da un bambino che si appoggia allo schermo.

Dal ripristino puoi:

- Riparare la connessione **Wi-Fi**
- **Ri-accoppiare** l'unità al tuo account
- Forzare un **aggiornamento firmware**
- Eseguire un **ripristino di fabbrica** dell'unità

Un'unità che non riesce ad avviarsi diverse volte di seguito può anche tornare da sola alla versione precedente.

:::warning Uno schermo in ripristino non controlla nulla
Il tuo controller continua a eseguire la propria programmazione. Ma un'[automazione](/help/mobile-automation) la cui azione deve essere eseguita **da questo Cora Max** non può funzionare mentre è in ripristino; la regola scatta e il passo non raggiunge l'hardware.
:::

## Se un'unità non si riavvia

Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** con la versione mostrata sullo schermo e cosa dice. Non ri-accoppiare l'unità prima; lo stato dell'associazione è spesso utile per capire cosa è successo.
