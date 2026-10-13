---
title: Aggiornamenti e ripristino
description: Come si aggiorna da solo Cora Max, la finestra di installazione e il canale di aggiornamento, come controllare la versione, il PIN di ripristino e cosa fare se Cora Max non si avvia o mostra un codice di assistenza.
section: Cora Max
reviewed: 2026-10-13
order: 15
group: Settings and account
---

Cora Max si tiene aggiornato da solo. Questa pagina spiega quando si installano gli aggiornamenti, come controllare la tua versione e come rimettere in funzione Cora Max se non si avvia normalmente.

## Aggiornamenti automatici

Le nuove versioni si scaricano in background appena escono. Si installano dentro la **Finestra di installazione**, dalle 3 alle 5 del mattino se non la cambi, così lo schermo non si riavvia mentre lo stai guardando. Quando una versione porta delle note di rilascio, Cora Max le mostra.

Non devi fare niente per restare aggiornato.

## Controllare la versione e le impostazioni di aggiornamento

![Rete e aggiornamenti su Cora Max](img/max-updates.webp "Aggiornamento firmware, nella sezione RETE E AGGIORNAMENTI delle Impostazioni Cora Max.")

La tua versione è nella scheda in cima a **Impostazioni → Impostazioni Cora Max** (*Cora Max · firmware 0.28.170*), e in **AIUTO E INFORMAZIONI → Informazioni**.

**Impostazioni → Impostazioni Cora Max → Aggiornamento firmware** (in **RETE E AGGIORNAMENTI**) mostra la versione che hai e se c'è un aggiornamento in attesa. Tocca **Controlla aggiornamenti** per controllare subito, oppure **Scarica e installa** quando ce n'è uno.

In **Impostazioni aggiornamento** nella stessa schermata:

- **Finestra di installazione** imposta le ore in cui gli aggiornamenti possono installarsi, con un orario di **Inizio** e di **Fine**, nell'ora locale di questo schermo. Il fuso orario si imposta in Cora Mobile, in **Dispositivi →** il tuo Cora Max **→ Fuso orario**.
- **Canale aggiornamento** è **Stabile** o **Beta**. Lascialo su **Stabile** a meno che l'assistenza non ti chieda di cambiarlo. Un Cora Max su **Beta** non riceve le versioni stabili.

Per vedere se questo schermo sta leggendo i tuoi dispositivi e salvando in Cora Cloud, torna in **Impostazioni Cora Max** e scorri fino a **STATO**. Mostra per ogni vasca **Stato polling**, **Ultimo polling**, **Ultima scrittura cloud** e **Salvataggio cloud**.

## Quando c'è un aggiornamento disponibile

Un messaggio ti dice cosa c'è di nuovo e ti dà due scelte.

- **Aggiorna ora** installa subito e riavvia. Ci vuole circa un minuto. Tieni Cora Max alimentato.
- **Rinvia di 24 ore** nasconde il messaggio e te lo richiede un giorno dopo.

Mentre un aggiornamento è in attesa, un puntino compare sull'icona **Impostazioni** nella barra in alto e sulla riga **Aggiornamento firmware**. Il puntino resta anche se rinvii, così vedi comunque che c'è un aggiornamento. Sparisce mentre l'aggiornamento si installa.

Se lo lasci stare, l'aggiornamento si installa da solo nella **Finestra di installazione**.

Puoi anche avviarlo dal telefono: in Cora Mobile, apri **Dispositivi →** il tuo Cora Max e tocca **Aggiorna a v…**.

:::note Durante un aggiornamento non perdi letture
I tuoi dati stanno nel tuo account. Quando Cora Max si riavvia, torna con le stesse vasche, dashboard e storico.
:::

## Ripristino {#recovery}

Il ripristino è una modalità di manutenzione per quando Cora Max non si avvia normalmente, o quando devi sistemare la sua configurazione senza un computer.

1. Tieni **cinque dita** nell'angolo in alto a destra dello schermo per **dieci secondi**.
2. Si apre la casella **PIN di ripristino**. Scrivi il PIN di 6 cifre e tocca **Conferma**.

Hai visto il PIN quando hai associato Cora Max. Lo trovi anche in Cora Mobile in **Dispositivi →** il tuo Cora Max **→ PIN di ripristino**. Cora Max non lo mostra mai, così un ospite o un bambino che si appoggia allo schermo non può entrare nel ripristino.

Se sbagli il PIN tre volte, il ripristino si blocca per 30 secondi, e più a lungo dopo ogni altro tentativo sbagliato. **Troppi tentativi** ti dice quanto aspettare. Se Cora Max non è mai stato online dopo l'associazione, non ha ancora un PIN e mostra **Il ripristino non è disponibile**. Collegalo prima al Wi-Fi.

Da **Ripristino** puoi:

- **Ripeti configurazione Wi-Fi**: scegliere una nuova rete Wi-Fi e una nuova password
- **Ri-accoppia questo dispositivo**: cancellare l'associazione e configurarlo di nuovo con Cora Mobile
- **Forza controllo OTA**: controllare subito gli aggiornamenti
- **Ripristino di fabbrica**: rimuovere l'associazione e ogni impostazione dello schermo

I dati della vasca già salvati in Cora Cloud vengono conservati in ogni caso.

Se Cora Max non riesce ad avviarsi più volte di fila, può anche tornare da solo alla versione precedente.

:::note Lo stesso gesto sblocca il blocco bambini
Se il [Blocco bambini](/help/max-settings#child-lock) è attivo, tenere cinque dita nell'angolo sblocca anche lo schermo. Tocca **Annulla** nella casella **PIN di ripristino** se volevi solo sbloccare.
:::

:::warning Uno schermo in ripristino non comanda niente
Il tuo controller continua a seguire la sua programmazione. Ma un passo di un'[automazione](/help/mobile-automation) che deve eseguire **questo Cora Max** non può essere eseguito mentre è in ripristino. La regola scatta, ma il passo non arriva mai all'attrezzatura.
:::

## Se Cora Max mostra "Cora Max hit a problem"

Questa schermata vuol dire che qualcosa è andato storto mentre Cora Max si avviava o funzionava. Mostra un **Support code** (comincia con *CXB-*).

1. Annota il codice di assistenza.
2. Aspetta. Cora Max si riavvia da solo in circa 10 minuti. Per riavviarlo subito, tieni cinque dita nell'angolo in alto a destra per 10 secondi.
3. Se continua a succedere, scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** indicando il codice di assistenza.

## Se un'unità non si riavvia

Scrivi a **[cora@coraiq.tech](mailto:cora@coraiq.tech)** indicando la versione mostrata sullo schermo e il messaggio che mostra. Non associarla di nuovo prima. Lo stato dell'associazione spesso aiuta a capire cosa è successo.
