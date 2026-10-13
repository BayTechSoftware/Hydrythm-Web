---
title: Luci, pompe e dosatori EcoTech
description: Collega a Cora via Bluetooth le luci EcoTech Radion, le pompe VorTech e i dosatori Versa, e scopri cosa puoi farci.
section: Cora Mobile
reviewed: 2026-10-13
order: 18
group: Equipment
---

:::note Beta
**Beta.** EcoTech è in Beta ed è disponibile solo per gli utenti Beta. Se non sei un utente Beta non lo vedrai in **Aggiungi dispositivo**. Per chiedere l'accesso alla Beta, contatta l'[assistenza](/support.html).
:::

Usa questa pagina per collegare a Cora le luci EcoTech Radion, le pompe VorTech e i dosatori Versa e per comandarli. Parti da **Dispositivi → Aggiungi dispositivo → EcoTech**. La stessa riga trova anche i dispositivi AquaIllumination, NYOS Quantum, Nero e Orbit che si trovano sulla stessa rete Bluetooth.

## Cosa ti serve {#what-you-need}

- Un Cora Max nella vasca. Fa la lettura e invia i tuoi comandi all'attrezzatura via Bluetooth. Senza, la riga **EcoTech** mostra **Richiede Cora Max** e resta disattivata.
- Il Bluetooth del telefono acceso, con il permesso Bluetooth per Cora. Cora lo chiede quando avvii la ricerca.
- Attrezzatura accesa e a portata del Cora Max.

## Collegarla {#linking-it}

1. Vai in **Dispositivi → Aggiungi dispositivo → EcoTech**.
2. Cora cerca luci, pompe e dosatori nelle vicinanze. Le luci già collegate all'app Mobius di EcoTech potrebbero non comparire.
3. L'attrezzatura sulla stessa rete Bluetooth viene raggruppata come un'unica **Vasca Mobius**. Tocca **Collega a…** e scegli la vasca Cora a cui appartiene.
4. Dai un nome al gruppo quando Cora te lo chiede, e il collegamento è fatto.

Un dispositivo segnato **Solo lettura** mostra le sue letture, ma Cora non può ancora comandarlo. Il controllo per quel modello arriva dopo che è stato provato.

Se sulla stessa rete Bluetooth ci sono anche luci di un'altra vasca, e le due vasche sono lette da Cora Max diversi, Cora mostra **Letto da un solo Cora Max**. A quel punto un solo Cora Max legge tutta la rete per entrambe le vasche.

Se non si trova niente, controlla che il Bluetooth sia acceso e l'attrezzatura alimentata, poi tocca **Scansiona di nuovo**.

## Luci Radion {#radion}

![La pagina di una Radion in Cora Mobile](img/mobile-radion.webp "Lo stato, le luci su questa rete (tutte o una sola), poi l'intensità e ogni canale di colore.")

La pagina della luce ha un editor del programma e scene rapide (**Programma**, **Tempesta**, **Nuvole**, **Colori**, **Alimentazione**, **Spento**). Puoi anche impostare l'acclimatazione, la ventola, il ciclo lunare e l'orologio.

Nell'editor del programma, **Anteprima giornata** riproduce la giornata in accelerato così la vedi senza aspettare. **Interrompi anteprima** rimette le luci come prima. **Annulla** e **Ripeti** scorrono le tue modifiche, e **Parti da…** comincia un nuovo programma da una copia di uno esistente.

Cora legge le luci a intervalli regolari. In **Impostazioni Radion**, sotto **Lettura**, **Leggi le luci ogni** imposta quanto spesso. Leggere più di rado è più delicato per le luci. Aprire la pagina e ogni comando leggono comunque subito le luci.

**Impostazioni Radion** ha anche:

- **Imposta orologio**, per impostare l'orologio della luce.
- **Acclimatazione**, per i coralli nuovi: tutto il programma sale gradualmente nei giorni che imposti. Se la attivi, riparte dal livello più basso.
- **Avvisi**: **La luce smette di rispondere**, **Guasto: calore, ventola o LED**, **Orologio sfasato di 5 min** e **Temperatura dei LED**. Attiva quelli che vuoi.

## Pompe VorTech {#vortech}

Un riquadro VorTech mostra la modalità e la velocità della pompa. Puoi cambiare la modalità e la **Velocità**, modificare il suo programma e avviare l'**Alimentazione** per qualche minuto. L'alimentazione rallenta tutte le VorTech della vasca, che tornano ai loro programmi quando finisce. Accanto a ogni modalità c'è una breve descrizione, dal flusso costante alle ondate da cresta di barriera, alle maree e agli impulsi. Una pompa offre solo le modalità che supporta.

## Dosatori Versa {#versa}

La pagina di un Versa mostra il contenitore, le dosi e i limiti. Puoi impostare la dimensione del contenitore, toccare **Segna come riempito**, usare **Eroga ora**, mettere in **Pausa** il dosaggio fino a mezzanotte e modificare il programma. Cora tiene una cronologia delle dosi per ogni testa. La campanella imposta gli avvisi di rifornimento in giorni rimasti o in quanto è pieno il contenitore, come descritto in [Materiali di consumo](/help/mobile-consumables).

:::warning Non ancora provato su hardware reale
I comandi alle pompe VorTech e ai dosatori Versa non sono ancora stati provati su hardware reale. La lettura funziona. Le prime volte che cambi qualcosa controlla direttamente l'attrezzatura, e dicci cosa vedi da [Segnalare un problema](/help/mobile-support).
:::

## Avvisi {#alerts}

Cora considera silenzioso un dispositivo EcoTech dopo tre letture mancate rispetto al suo intervallo di lettura. Una rete con sole luci viene letta ogni 30 minuti per impostazione predefinita, quindi ci vogliono almeno 90 minuti. Vedi [Avvisi e soglie](/help/mobile-alerts). Le luci Radion hanno anche i loro avvisi in **Impostazioni Radion**, descritti sopra.

## Su Cora Max {#on-cora-max}

La stessa attrezzatura ha le sue pagine sullo schermo a parete. Di più in [Controllare l'attrezzatura da Cora Max](/help/max-device-control).
