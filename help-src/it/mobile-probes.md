---
title: Sonde
description: Vedi quale sonda guida ogni lettura in tutti i controller, e annota calibrazioni e pulizie.
section: Cora Mobile
reviewed: 2026-09-30
order: 13
group: Equipment
---

Se hai più di un controller, o due sonde che misurano la stessa cosa, Cora deve sapere quale lettura considerare valida. La mappatura delle sonde è dove sistemi questo, ed è anche dove dici a Cora cos'è ogni sonda fin dall'inizio.

Apri il **profilo della vasca** (la matita in alto sulla dashboard) e scegli **Mappatura sonde**.

## Da dove arriva ogni lettura

![Da dove arriva ogni lettura](img/mobile-probes.webp "Ogni parametro, quale sonda lo guida e un pulsante Scegli per cambiarla.")

Questa sezione elenca ogni parametro che Cora segue per questa vasca, come pH o temperatura, e mostra quale sonda lo sta alimentando in questo momento.

Tocca una lettura per vedere tutte le sonde che la riportano, in tutti i controller che hai collegato. Ognuna mostra la sua marca, il nome che le ha dato il controller e il suo valore in tempo reale. Scegline una per fissarla, oppure scegli **Automatico** per lasciare che Cora usi qualunque sonda stia riportando.

Un'etichetta accanto a ogni lettura mostra quale sonda è attiva: **Automatico**, oppure **Scelta da te** una volta che ne hai fissata una.

Se una sonda fissata smette di riportare, Cora mostra da quanto tempo non risponde più e offre **Torna ad Automatico**, così una sonda morta non può bloccare una lettura.

Tocca **Rinomina** per dare a una lettura un nome tutto suo. È diverso dal nome che dai alla sonda stessa, ed è quello che compare sulla dashboard, negli avvisi e in Reef Buddy.

:::note Un sensore di allagamento qui non si può riassegnare
L'allarme di un sensore di allagamento dipende dal suo stesso nome, quindi è escluso da questa scelta. Funziona come sempre.
:::

## Sonde: dire a Cora cos'è ognuna

Più in basso trovi tutte le sonde che Cora conosce, raggruppate per dispositivo, ognuna con la sua lettura attuale. Cora riconosce da sola i nomi standard e la riga mostra a quale parametro ha associato la sonda. Di solito quindi devi solo correggere quelle che Cora non è riuscita a riconoscere, senza doverle mappare tutte a mano.

Per ogni riga hai tre scelte:

- **Un parametro Cora**: il valore che misura quella sonda.
- **Personalizzato**: per una sonda che non corrisponde a nessun parametro standard di Cora. Le dai un nome breve in maiuscolo e Cora la registra con quel nome.
- **Ignora**: per le sonde che non vuoi registrare.

Una sonda ignorata o non mappata non compare sulla dashboard e non fa scattare avvisi.

La mappatura vale dalla prossima lettura registrata. Una correzione quindi non riscrive lo storico, ma cambia quello che viene salvato da quel momento. Tocca **Salva** per applicarla.

:::warning Una sonda non mappata per Cora non esiste
Se un parametro non ha letture ma la sonda funziona, controlla per prima cosa la sua mappatura.
:::

## Più sonde per lo stesso parametro

Se hai due sonde di temperatura, sullo stesso controller o su due diversi, mappale entrambe. Cora le tiene come fonti separate, e **Da dove arriva ogni lettura** qui sopra è dove scegli quale delle due guida la lettura, oppure lasci Automatico. Puoi confrontarle in [la pagina del parametro](/help/mobile-metric-detail).

## Annotare la cura delle sonde

Con il tempo le sonde perdono precisione. Cora può tenere traccia di quando hai calibrato o pulito ogni sonda l'ultima volta, così capisci se un valore è cambiato davvero o se la sonda ha bisogno di una sistemata.

Registra calibrazione o pulizia dalla voce della sonda. È anche un buon candidato per un [lavoro di manutenzione](/help/mobile-maintenance) ricorrente.

:::note La data di calibrazione spiega le differenze
Quando sonda e test non concordano, la prima cosa da guardare di solito è quando hai calibrato la sonda l'ultima volta.
:::
