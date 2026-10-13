---
title: Modificare la dashboard di Cora Max
description: Aggiungi, sposta e togli riquadri sulla dashboard di Cora Max, scegli una griglia, usa i modelli o Progetta con l'IA, e salva layout da riusare su qualsiasi Cora Max.
section: Cora Max
reviewed: 2026-10-13
order: 4
group: Your dashboard
twin: mobile-dashboard-editing
---

Questa pagina mostra come disporre i riquadri sulla dashboard di un Cora Max. Usa una **griglia fissa**: lo schermo non scorre, quindi ogni riquadro deve stare in una sola schermata. È la differenza principale rispetto alla dashboard del telefono.

Apri l'editor dal **menu della vasca**: tocca il nome della vasca nella barra in alto, poi **Layout dashboard**. Lo trovi anche in **Impostazioni → [la tua vasca] → Layout dashboard**.

![L'editor della dashboard su Cora Max](img/max-dashboard-editor.webp "Le dimensioni della griglia in alto, poi i riquadri. È una schermata di layout, quindi ogni riquadro mostra il suo tipo e la sua fonte invece di una lettura. Non viene salvato niente finché non premi Salva.")

:::tip Puoi modificarla anche dal telefono
In Cora Mobile, apri la scheda **Dispositivi**, tocca il tuo Cora Max, poi tocca **Layout dashboard** sulla scheda della vasca. È più veloce che sistemare i riquadri a mano su uno schermo a parete, e il risultato compare su Cora Max appena salvi.
:::

## Scegliere una griglia {#choosing-a-grid}

Scegli prima la dimensione della griglia. Cambiarla dopo sposta tutti i riquadri.

| Griglia | Riquadri | Come risulta |
|---|---|---|
| 2×2, 3×2, 3×3 | 4–9 | Grande. Facile da leggere dall'altra parte della stanza. |
| 4×4, 5×3, 6×4 | 16–24 | La scelta abituale per un impianto completo. |
| 6×5, 8×4, 8×5 | 30–40 | Fitta. Un'intera stanza dell'acquario in una schermata. |
| 9×5, 10×5 | 45–50 | Molto fitta. Rende meglio sugli schermi più grandi. |
| **Auto** | fino a 32 | Cora sceglie una forma adatta a quanti riquadri hai aggiunto. |

Una griglia fissa contiene tanti riquadri quante celle ha, fino a 50 su 10×5. **Auto** ha un suo limite di 32 riquadri. Oltre, il testo diventa troppo piccolo da leggere a distanza.

:::note Non sei sicuro? Parti da Auto
Aggiungi i riquadri che vuoi e lascia la griglia su **Auto**. Cora sceglie una forma adatta. Se ti piace, puoi passare dopo a quella forma fissa.
:::

:::warning Cambiare la griglia toglie riquadri solo quando non ci stanno
Quando cambi la griglia, Cora non butta via i riquadri in base alla posizione. I riquadri che hanno ancora una cella valida restano dove sono, e gli altri vengono risistemati in ordine. Perdi riquadri solo quando la nuova griglia ha **meno celle dei riquadri che hai**, e Cora ti dice quanti sono andati persi. Passare da 10×5 (50 celle) a 3×3 (9) ne fa perdere la maggior parte.
:::

## Aggiungere e disporre i riquadri {#adding-and-arranging}

1. Tocca una cella vuota (mostra un **+**) per aprire **Aggiungi widget**.
2. In **TIPO**, scegli il tipo di riquadro, poi cosa mostra (una lettura, una presa, un dispositivo o una scena).
3. In **DIMENSIONE**, scegli quanto è grande. Un riquadro può essere largo una o due celle e alto una o due celle. Un Grafico ha anche un **INTERVALLO DI TEMPO**. Un riquadro di un dosatore ha **Mostra il rimanente come**, in **Giorni** o **Millilitri (mL)**.
4. Tocca **Aggiungi**.

I gesti sono elencati in alto nell'editor: **tocca un riquadro per modificarlo**, **tieni premuto per spostarlo** e **✕ per rimuoverlo**. **Svuota tutto** svuota la griglia così puoi ricominciare.

I sedici tipi di riquadro sono Valore, Indicatore, Grafico, Stato, Presa, Scena, ReefBeat, Modulo Apex, Jecod, Maxspect *(Beta)*, GHL *(Beta)*, HYDROS *(Beta)*, Radion *(Beta)*, VorTech *(Beta)*, Versa *(Beta)* e Telecamera *(Beta)*. Li trovi nella [Guida ai widget](/help/mobile-widgets). Il riquadro **Scena** esiste solo su Cora Max. Avvia una [scena](/help/max-automation) con un tocco.

:::note Beta
**Beta.** Maxspect, GHL, HYDROS, EcoTech (Radion, VorTech, Versa) e le telecamere sono in Beta e sono disponibili solo per gli utenti Beta. Se non sei un utente Beta non li vedrai in **Aggiungi dispositivo**. Per chiedere l'accesso alla Beta, contatta l'[assistenza](/support.html). I loro riquadri compaiono solo quando hai il dispositivo. Di più in [Funzioni Beta](/help/mobile-beta).
:::

## Prese e alimentazione {#outlets-feed}

**Prese e alimentazione** nell'editor sceglie quali prese e quali cicli di alimentazione compaiono in **Controlli**, il pannello che apri scorrendo verso l'alto dal fondo della dashboard. Non aggiunge riquadri. Se non ne scegli nessuno, Controlli li elenca tutti. Per mettere una presa sulla griglia stessa, aggiungi un riquadro **Presa**. Di più in [Prese e comandi](/help/max-controls).

## Modelli {#templates}

**Modelli** si trova in alto nell'editor, accanto a **Le mie dashboard** e **Progetta con l'IA**. È disponibile con tutti i piani e non usa mai l'IA, quindi funziona anche senza la condivisione dei dati con l'IA.

Apre **Modelli di dashboard**, alcuni layout pronti costruiti in base a quello che questa vasca riporta e ha collegato:

- **Panoramica**: pochi riquadri grandi, con i parametri principali come indicatori e i tuoi dispositivi principali
- **Attrezzatura**: prima un riquadro per dispositivo, poi le prese e i parametri principali
- **Parametri**: prima grafici e letture, con dispositivi e prese per ultimi
- **Fotocamera**: una grande vista in diretta in alto a sinistra con i parametri principali accanto. Compare solo quando la vasca ha una telecamera. Le telecamere sono in Beta e sono disponibili solo per gli utenti Beta.

Ognuno mostra un'anteprima e quanti riquadri ha su quale griglia. Tocca **Usa questo**. Cora chiede prima **Sostituire la dashboard?** Tocca **Salva prima l'attuale come preset** se vuoi tenere il layout che hai, oppure **Sostituisci**. Non viene salvato niente finché non premi **Salva**.

## Progetta con l'IA {#design-with-ai}

L'editor ha un pulsante **Progetta con l'IA**. Funziona con un piano a pagamento e durante la prova. Cora propone un layout completo in base a quello che questa vasca riporta e ha collegato, e mostra quanti riquadri ha e su quale griglia. Tocca **Usa questo** per portarlo nell'editor, oppure **Riprova** per averne un altro. Puoi fare 5 design per vasca al giorno.

Un design dell'IA sostituisce quello che c'è adesso su questa dashboard. Non viene salvato niente finché non premi **Salva**, e puoi prima tenere il layout attuale salvandolo in **Le mie dashboard**. Con il piano gratuito, **Progetta con l'IA** ti rimanda ai piani. Richiede anche la condivisione dei dati con l'IA attiva in Cora Mobile. Di più in [Fare domande a Cora](/help/mobile-assistant).

## Progettare per la distanza {#designing-for-distance}

Uno schermo a parete si legge da più lontano di un telefono, e di solito con un'occhiata veloce.

- Fai i parametri chiave due per due. Alcalinità, temperatura e pH sono cose che vorrai leggere senza avvicinarti.
- Metti i comandi ai bordi. I riquadri delle prese sono quelli che tocchi, e ai lati si raggiungono più facilmente.
- Raggruppa i riquadri per argomento. Tieni insieme tutto il dosaggio e tutto il movimento, perché uno schermo a parete si guarda per zone.
- Tieni piccoli gli elementi in traccia. Loro e gli altri numeri che cambiano lentamente servono da riferimento, quindi basta un riquadro valore uno per uno.

## Salvare e riusare i layout {#saving-layouts}

Niente di quello che fai nell'editor ha effetto finché non premi **Salva**. Se esci con modifiche non salvate, Cora chiede prima **Scartare le modifiche?**

**Le mie dashboard** conserva i design a cui vuoi tornare. Sono salvati nel tuo account, non su questo schermo, quindi qualsiasi Cora Max del tuo account può caricarli, per un'altra vasca o per uno schermo sostitutivo.

- **Salva questo progetto** salva quello che c'è nell'editor. Puoi tenerne fino a 30.
- **Carica** mette un design salvato nell'editor. I design salvati dal telefono sono segnati **Telefono**.
- Prima di caricare, Cora ti dice quanti riquadri verranno portati. Quelli che non possono, come una lettura che questa vasca non riporta o un dispositivo che non è su questa vasca, sono elencati sotto **Lasciati indietro:** con il motivo.

Per esempio, potresti tenere un layout fitto per tutti i giorni e uno a riquadri grandi per quando lavori in vasca.

## Più vasche {#multiple-tanks}

Ogni vasca ha il suo layout. Passa a quella vasca e apri **Layout dashboard** dal suo menu della vasca, oppure usa **Impostazioni → [quella vasca] → Layout dashboard**.
