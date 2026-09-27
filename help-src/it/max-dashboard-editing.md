---
title: Modificare la dashboard di Cora Max
description: Scegli una griglia, aggiungi widget, e salva layout per lo schermo di Cora Max.
section: Cora Max
reviewed: 2026-09-09
order: 4
group: Your dashboard
---

La dashboard di Cora Max usa una **griglia fissa**. Ogni riquadro deve stare su un solo schermo; il display non scorre. Questa è la differenza principale dalla dashboard del telefono.

Apri l'editor dal **menu della vasca**: tocca il nome della vasca nella barra superiore, poi **Layout dashboard**. Si trova anche sotto **Impostazioni → Impostazioni vasca → [la tua vasca] → Layout dashboard**.

![L'editor della dashboard su Cora Max](img/max-dashboard-editor.webp "Dimensioni della griglia in alto, poi i riquadri. Ognuno mostra il suo tipo e la sua fonte, non una lettura; questa è una schermata di layout. Nulla viene scritto finché non premi Salva.")

:::tip Puoi modificarla anche dal tuo telefono
**Dispositivi → il tuo Cora Max → Modifica Dashboard** crea lo stesso layout da Cora Mobile. È più rapido che disporre riquadri a mano su una parete, e il risultato appare sullo schermo immediatamente.
:::

## Scegliere una griglia

Scegli prima la densità, perché cambiarla riorganizza tutto.

| Griglia | Riquadri | Sembra |
|---|---|---|
| 2×2, 3×2, 3×3 | 4-9 | Grande. Leggibile da tutta la stanza. |
| 4×4, 5×3, 6×4 | 16-24 | La scelta abituale per un sistema completo. |
| 6×5, 8×4, 8×5 | 30-40 | Densa. Un'intera stanza della vasca in una volta. |
| 9×5, 10×5 | 45-50 | Molto densa. Migliore sugli schermi più grandi. |
| **Auto** | fino a 32 | Cora sceglie una forma adatta a quanti riquadri hai aggiunto. |

Una griglia fissa contiene tanti riquadri quante celle ha, fino a 50 su 10×5. **Auto** è la sola opzione con un proprio limite: si ferma a 32 riquadri, perché oltre quello il testo diventa troppo piccolo da leggere a distanza.

:::note Inizia con Auto se non sei sicuro
Aggiungi i riquadri che vuoi e lascia la griglia su **Auto**; Cora sceglie una forma che li adatta. Se ti piace il risultato, fissala in seguito a quella forma fissa.
:::

:::warning Cambiare griglia può far perdere riquadri, ma solo quando non c'è spazio
I riquadri vengono riorganizzati nella nuova forma invece che scartati per posizione: qualsiasi cosa già in una cella valida resta al suo posto, e il resto viene rimesso dentro, in ordine. I riquadri vengono persi solo quando la nuova griglia ha **meno celle di quanti riquadri hai**, e Cora ti dice quanti sono andati persi. Passare da 10×5 (50 celle) a 3×3 (9) ne perderà la maggior parte.
:::

## Aggiungere e disporre

L'editor ti indica i tre gesti in alto: **tocca un riquadro per modificarlo**, **tieni premuto per spostarlo**, e **✕ per rimuoverlo**. I riquadri possono essere larghi una o due celle e alti una o due celle.

**Prese e alimentazione** aggiunge le tue prese controllabili e i cicli di alimentazione in un solo passaggio, invece che un riquadro alla volta. **Svuota tutto** vuota la griglia così puoi ricominciare.

I nove tipi di riquadro (Valore, Indicatore, Grafico, Stato, Presa, ReefBeat, modulo Apex, Jecod e Maxspect *(beta)*) sono descritti nella **[Guida di riferimento ai widget](/help/mobile-widgets)**.

## Progettare per la distanza

Un display a parete si legge da più lontano di un telefono, e di solito con un'occhiata invece che con attenzione.

- **Dai ai tuoi parametri principali due per due.** Alcalinità, temperatura, pH: le cose che vuoi leggere senza camminare fin lì.
- **Metti i controlli ai margini.** I riquadri delle prese sono quelli a cui tendi la mano; sono più facili da colpire ai lati.
- **Raggruppa per argomento, non per tipo.** Tutto ciò che riguarda il dosaggio insieme, tutto ciò che riguarda il flusso insieme. Scandisci una parete per zona.
- **Lascia piccole le tracce.** Gli elementi in traccia e altri numeri lenti sono un riferimento, non un monitoraggio; un riquadro valore uno per uno è più che sufficiente.

## Salvare i layout

Nulla di quello che fai nell'editor ha effetto finché non premi **Salva**. Uscire senza salvare scarta le modifiche.

**Le mie dashboard** conserva i layout a cui vuoi tornare, così puoi passare da uno all'altro invece di ricrearli. Un layout denso quotidiano e un layout a riquadri grandi per quando lavori nella vasca si adattano a momenti diversi, e passare dall'uno all'altro richiede un solo tocco.

## Più vasche

Ogni vasca ha il proprio layout. Modificali separatamente, una vasca alla volta, dalle impostazioni proprie di quella vasca.
