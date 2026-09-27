---
title: Sonde
description: Associa le sonde del controller ai parametri di Cora e annota calibrazioni e pulizie.
section: Cora Mobile
reviewed: 2026-09-09
order: 13
group: Equipment
---

Il controller chiama le sonde con nomi suoi. Con la mappatura delle sonde dici a Cora qual è la sonda del pH, quale quella della temperatura e così via.

## Mappare le sonde

Apri il **profilo della vasca** (la matita in alto sulla dashboard), apri la sezione del controller e scegli **Mappatura sonde**.

![Mappatura delle sonde](img/mobile-probes.webp "Ogni sonda riportata dal tuo controller, la sua lettura in tempo reale, e cosa ne fa Cora.")

Vedi tutte le sonde del controller, ognuna con la sua lettura attuale. Cora riconosce da sola i nomi standard e la riga mostra a quale parametro ha associato la sonda. Di solito quindi devi solo correggere quelle che Cora non è riuscita a riconoscere, senza doverle mappare tutte a mano.

Per ogni riga hai tre scelte:

- **Un parametro Cora**: il valore che misura quella sonda.
- **Personalizzato**: per una sonda che non corrisponde a nessun parametro standard di Cora. Le dai un nome breve in maiuscolo e Cora la registra con quel nome.
- **Ignora**: per le sonde che non vuoi registrare.

Una sonda ignorata o non mappata non compare sulla dashboard e non fa scattare avvisi.

La mappatura vale dalla prossima lettura registrata. Una correzione quindi non riscrive lo storico, ma cambia quello che viene salvato da quel momento. Tocca **Salva** per applicarla.

:::warning Una sonda non mappata per Cora non esiste
Se un parametro non ha letture ma la sonda funziona, controlla per prima cosa la mappatura.
:::

## Più sonde per lo stesso parametro

Se hai due sonde di temperatura, puoi mapparle tutte e due. Cora le tiene come fonti separate. Nelle impostazioni del widget scegli quale fonte segue il riquadro, e nella [pagina del parametro](/help/mobile-metric-detail) puoi confrontarle.

## Annotare la cura delle sonde

Con il tempo le sonde perdono precisione. Cora può tenere traccia di quando hai calibrato o pulito ogni sonda l'ultima volta, così capisci se un valore è cambiato davvero o se la sonda ha bisogno di una sistemata.

Registra calibrazione o pulizia dalla voce della sonda. È anche un buon candidato per un [lavoro di manutenzione](/help/mobile-maintenance) ricorrente.

:::note La data di calibrazione spiega le differenze
Quando sonda e test non concordano, la prima cosa da guardare di solito è quando hai calibrato la sonda l'ultima volta.
:::
