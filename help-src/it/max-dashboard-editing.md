---
title: Modificare la dashboard di Cora Max
description: Scegli una griglia, aggiungi i widget e salva i layout per lo schermo di Cora Max.
section: Cora Max
reviewed: 2026-10-13
order: 4
group: Your dashboard
---

La dashboard di Cora Max usa una **griglia fissa**. Tutti i riquadri devono stare in una sola schermata, perché lo schermo non scorre. È questa la differenza principale rispetto alla dashboard del telefono.

Apri l'editor dal **menu della vasca**: tocca il nome della vasca nella barra in alto, poi **Layout dashboard**. Lo trovi anche in **Impostazioni → Impostazioni vasca → [la tua vasca] → Layout dashboard**.

![L'editor della dashboard su Cora Max](img/max-dashboard-editor.webp "In alto le dimensioni della griglia, sotto i riquadri. Ogni riquadro mostra tipo e fonte, senza letture, perché qui imposti solo il layout. Niente viene salvato finché non premi Salva.")

:::tip Puoi modificarla anche dal telefono
Con **Dispositivi → il tuo Cora Max → Modifica dashboard** crei lo stesso layout da Cora Mobile. Fai prima che sistemare i riquadri a mano sullo schermo a parete, e il risultato compare subito.
:::

## Scegliere la griglia

Scegli prima la densità. Se la cambi dopo, tutti i riquadri vengono ridisposti.

| Griglia | Riquadri | Com'è |
|---|---|---|
| 2×2, 3×2, 3×3 | 4–9 | Grande. Si legge anche dall'altra parte della stanza. |
| 4×4, 5×3, 6×4 | 16–24 | La scelta più comune per un sistema completo. |
| 6×5, 8×4, 8×5 | 30–40 | Fitta. Tutta la stanza della vasca in un colpo d'occhio. |
| 9×5, 10×5 | 45–50 | Molto fitta. Va meglio sugli schermi più grandi. |
| **Auto** | fino a 32 | Cora sceglie una forma adatta al numero di riquadri che hai aggiunto. |

Una griglia fissa contiene tanti riquadri quante sono le sue celle, fino a 50 con 10×5. Solo **Auto** ha un limite suo: si ferma a 32 riquadri, perché oltre il testo diventa troppo piccolo da leggere a distanza.

:::note Nel dubbio, parti da Auto
Aggiungi i riquadri che ti servono e lascia la griglia su **Auto**. Cora sceglie una forma in cui stanno tutti. Se il risultato ti piace, dopo puoi fissare quella forma.
:::

:::warning Cambiando griglia puoi perdere riquadri, ma solo se non c'è posto
I riquadri non vengono scartati in base alla posizione. Quelli che sono già in una cella valida restano dove sono, gli altri vengono rimessi dentro in ordine. Si perdono riquadri solo quando la nuova griglia ha **meno celle dei riquadri che hai**, e Cora ti dice quanti ne sono rimasti fuori. Passando da 10×5 (50 celle) a 3×3 (9) ne perdi quasi tutti.
:::

## Aggiungere e sistemare i riquadri

In alto l'editor ti ricorda i tre gesti: **tocca un riquadro per modificarlo**, **tienilo premuto per spostarlo** e **✕ per toglierlo**. Un riquadro può essere largo una o due celle e alto una o due celle.

**Prese e alimentazione** aggiunge in un colpo solo tutte le prese che puoi comandare e i cicli di alimentazione. **Svuota tutto** libera la griglia, così ricominci da capo.

I sedici tipi di riquadro (Valore, Indicatore, Grafico, Stato, Presa, Scena, ReefBeat, Modulo Apex, Jecod, Maxspect *(Beta)*, GHL *(Beta)*, HYDROS *(Beta)*, Radion *(Beta)*, VorTech *(Beta)*, Versa *(Beta)* e Telecamera *(Beta)*) sono descritti nella [Guida di riferimento ai widget](/help/mobile-widgets).

I riquadri Beta appartengono a integrazioni Beta che solo gli utenti Beta possono aggiungere, e ne vedi uno solo quando hai il dispositivo. Vedi [Funzioni Beta](/help/mobile-beta).

## Modelli

**Modelli** si trova accanto a **Progetta con l'IA**, in alto nell'editor. È disponibile con tutti i piani e non usa mai l'IA, quindi funziona anche senza la condivisione dei dati con l'IA.

Apre **Modelli di dashboard**, alcuni layout già pronti costruiti in base a ciò che questa vasca riporta e ha collegato:

- **Panoramica**: pochi riquadri grandi, con i parametri principali come indicatori e i tuoi dispositivi principali
- **Attrezzatura**: prima un riquadro per ogni dispositivo, poi prese e parametri principali
- **Parametri**: prima grafici e letture, dispositivi e prese in fondo
- **Fotocamera**: una grande vista dal vivo in alto a sinistra, con accanto i parametri principali. Compare solo se la vasca ha una telecamera. Le telecamere sono in Beta e disponibili solo per gli utenti Beta.

Ogni modello mostra un'anteprima e quanti riquadri ha su quale griglia. Tocca **Usa questo**. Prima Cora ti chiede **Sostituire la dashboard?** Tocca **Salva prima l'attuale come preset** se vuoi tenere il layout che hai, oppure **Sostituisci**. Non viene salvato niente finché non premi **Salva**.

## Progetta con l'IA

Con un piano a pagamento, l'editor ha il pulsante **Progetta con l'IA**. Cora propone un layout completo in base a ciò che questa vasca riporta e ha collegato, e mostra quanti riquadri ha e su quale griglia. Tocca **Usa questo** per portarlo nell'editor, oppure **Riprova** per averne un altro. Puoi fare 5 progetti al giorno per vasca.

Un progetto dell'IA sostituisce quello che c'è ora in questa dashboard. Non viene salvato niente finché non premi **Salva**, e puoi tenere prima il layout attuale salvandolo come una delle tue dashboard. Con un piano gratuito, **Progetta con l'IA** ti porta ai piani. Serve anche la condivisione dei dati con l'IA attiva nell'app Cora.

## Pensato per essere letto da lontano

Uno schermo a parete si guarda da più lontano di un telefono, e di solito con un'occhiata veloce.

- **Dai ai parametri principali un riquadro due per due.** Alcalinità, temperatura, pH: quello che vuoi leggere senza avvicinarti.
- **Metti i controlli ai lati.** I riquadri delle prese sono quelli che tocchi di più, e ai lati li raggiungi meglio.
- **Raggruppa per argomento.** Tutto il dosaggio insieme, tutto il movimento dell'acqua insieme. Lo schermo a parete si legge per zone.
- **Tieni piccoli gli elementi in traccia.** Gli elementi in traccia e gli altri valori che cambiano piano ti servono come riferimento. Basta un riquadro valore uno per uno.

## Salvare i layout

Nell'editor non cambia niente finché non premi **Salva**. Se esci senza salvare, le modifiche si perdono.

In **Le mie dashboard** tieni i layout che vuoi riusare, così passi dall'uno all'altro senza rifarli. Per esempio un layout fitto per tutti i giorni e uno a riquadri grandi per quando lavori in vasca. Passare dall'uno all'altro è un tocco.

## Più vasche

Ogni vasca ha il suo layout. Li modifichi separatamente, una vasca alla volta, dalle impostazioni di quella vasca.
