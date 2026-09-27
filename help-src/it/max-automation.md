---
title: Scene su Cora Max
description: Creare, eseguire e modificare scene direttamente sullo schermo di Cora Max.
section: Cora Max
reviewed: 2026-09-27
order: 15
group: Automation
---

Una **scena** è un insieme salvato di azioni sull'equipaggiamento che si esegue insieme, per un tempo fisso oppure finché non la fermi. Le scene funzionano allo stesso modo che tu le crei sul telefono o su Cora Max; questa pagina descrive come farlo alla parete.

## Dove trovare le scene

**Impostazioni → Automazioni** elenca ogni scena su ogni vasca che hai, con un chip di filtro per ogni vasca quando ne hai più di una. Apre lo stesso elenco sia che la scena sia stata creata sul telefono o su Cora Max.

Tocca una scena per modificarla, oppure tocca **+** per crearne una nuova. Se hai più di una vasca e non è scelto nessun filtro, Cora Max chiede a quale vasca appartiene la nuova scena.

## Creare una scena

1. Dai alla scena un **nome**.
2. Aggiungi **passi**. Da Cora Max, un passo può commutare una presa Apex (**ON**, **OFF** o **Auto**) o una presa intelligente Zigbee (**ON**, **OFF** o **Alterna**). I passi aggiunti sul telefono per altri tipi di equipaggiamento appaiono comunque qui, e possono comunque essere riordinati o rimossi, anche se questo schermo non può aggiungerne un altro simile.
3. Scegli quanto dura: un numero fisso di minuti, oppure **Permanente** (continua a funzionare finché non la fermi).
4. Scegli se eseguire la scena richiede un passo di **conferma**. Lascialo attivo a meno che tu non sia certo che la scena non tocchi mai nulla che sarebbe rischioso cambiare senza un secondo controllo.
5. Salva.

:::note Le teste di dosaggio DŌS non sono mai un passo di una scena
Una scena, creata su Cora Max o sul telefono, non può mai accendere una testa di dosaggio. Questo è deliberato: un dosaggio non è il tipo di azione che una scena dovrebbe poter attivare per errore.
:::

## Eseguire una scena

Le scene appaiono come riquadri sulla dashboard. Tocca **Esegui** per avviarne una.

Se la scena richiede conferma, Cora Max elenca esattamente cosa sta per fare, una riga per passo, prima che accada qualcosa. Leggila, poi scegli di eseguirla o di annullare.

Mentre una scena a tempo è in esecuzione, il suo riquadro mostra un conto alla rovescia a quando finisce, e un pulsante **Ferma** per terminarla in anticipo. Il riquadro di una scena permanente resta nel suo stato di esecuzione finché non la fermi.

Eseguire o fermare una scena passa sempre attraverso Cora Cloud, allo stesso modo di qualsiasi altro comando; vedi [Cosa è stato cambiato, e da cosa](/help/max-activity) per dove viene registrato il risultato.

**Se non funziona:** se una scena non si avvia o non si ferma, vedi [Risoluzione dei problemi](/help/troubleshooting).

:::note Il blocco bambini copre anche le scene
Se il [blocco bambini](/help/max-voice) è attivo, eseguire o fermare una scena da questo schermo è bloccato insieme a ogni altro controllo. Le domande su una scena continuano a funzionare a voce; avviarne o fermarne una no.
:::

## Modificare o eliminare una scena

Apri la scena da **Impostazioni → Automazioni**, oppure tieni premuto il suo riquadro sulla dashboard, per cambiare il suo nome, i passi, la durata o l'impostazione di conferma, o per eliminarla.

:::note Gli schermi Cora Max più vecchi possono eseguire una scena ma non modificarla
Creare e modificare scene alla parete è una funzione più recente di Cora Max. Un Cora Max più vecchio sullo stesso account può ancora mostrare ed eseguire una scena creata sul telefono o su un Cora Max più recente; semplicemente non può cambiarla. Aggiorna Cora Max, oppure modifica la scena dal telefono o da uno schermo più recente, se questo si presenta.
:::

Vedi [Scene e automazioni](/help/mobile-automation) per cosa può fare una scena in maggiore dettaglio, e come si creano sul telefono.
