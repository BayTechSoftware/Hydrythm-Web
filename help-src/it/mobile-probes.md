---
title: Sonde
description: Mappa le sonde del tuo controller sui parametri di Cora, e registra calibrazione e pulizia.
section: Cora Mobile
reviewed: 2026-09-09
order: 13
group: Equipment
---

Un controller riporta le sonde con i propri nomi. La mappatura delle sonde dice a Cora quale di esse è la tua sonda di pH, quale è la temperatura, e così via.

## Mappare le sonde

Apri il tuo **profilo della vasca** (la matita in alto sulla dashboard), espandi la sezione del tuo controller, e scegli **Mappatura sonde**.

![Mappatura delle sonde](img/mobile-probes.webp "Ogni sonda riportata dal tuo controller, la sua lettura in tempo reale, e cosa ne fa Cora.")

Ogni sonda riportata dal tuo controller è elencata con la sua lettura attuale. Cora rileva automaticamente i nomi standard, e la riga mostra quale ha associato, quindi il lavoro qui è di solito correggere quelle che non è riuscita a collocare invece di mapparle tutte a mano.

Ogni riga offre tre scelte:

- **Un parametro Cora**: la metrica misurata da quella sonda.
- **Personalizzato**: per una sonda per cui Cora non ha un parametro standard. Le dai un breve nome in lettere maiuscole, e viene tracciata sotto quel nome.
- **Ignora**: per le sonde che non vuoi registrare affatto.

Una sonda ignorata o non mappata non apparirà su una dashboard e non alimenterà gli avvisi.

Le mappature entrano in vigore alla prossima registrazione delle letture, quindi una correzione qui non riscrive lo storico; cambia cosa viene memorizzato da quel momento in poi. Premi **Salva** per applicarle.

:::warning Una sonda non mappata è invisibile a Cora
Se un parametro non mostra letture anche se la sonda funziona, controlla prima di tutto la mappatura.
:::

## Più sonde per un parametro

Un sistema con due sonde di temperatura può mappare entrambe. Cora le mantiene come fonti separate; l'impostazione della fonte del widget decide quale segue un riquadro, e [la vista del parametro](/help/mobile-metric-detail) ti permette di confrontarle.

## Registrare la cura delle sonde

Le sonde derivano. Cora può tracciare quando ognuna è stata calibrata o pulita l'ultima volta, così puoi distinguere un cambiamento reale da una sonda che ha bisogno di attenzione.

Registra la calibrazione o la pulizia dalla voce della sonda. Si adatta bene anche come [attività di manutenzione](/help/mobile-maintenance) ricorrente.

:::note Lo storico di calibrazione spiega i disaccordi
Quando una sonda e un kit di test non sono d'accordo, la data dell'ultima calibrazione della sonda è di solito la prima cosa che vale la pena controllare.
:::
