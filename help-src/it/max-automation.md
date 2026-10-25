---
title: Scene su Cora Max
description: Crea, avvia, modifica ed elimina scene su Cora Max, da Impostazioni → Automazioni o da un riquadro scena sulla dashboard.
section: Cora Max
reviewed: 2026-10-24
order: 9
group: Alerts and automation
twin: mobile-automation
---

Una **scena** è un insieme salvato di azioni sull'attrezzatura che vengono eseguite insieme, per un tempo stabilito o finché non la fermi. Puoi creare, avviare e modificare scene su Cora Max. Le scene create sul telefono e su Cora Max sono le stesse. Le regole di automazione (del tipo "quando succede questo, fai quello") si impostano sul telefono. Di più in [Automazioni e scene](/help/mobile-automation).

![L'elenco delle scene su Cora Max, con un'etichetta filtro per ogni vasca e un pulsante Nuova scena](img/max-automation.webp "L'elenco delle scene, filtrato per vasca. Se non ci sono ancora scene, lo dice e propone Nuova scena.")

## Dove trovare le scene

**Impostazioni → Automazioni** apre **Scene**, l'elenco di tutte le scene di tutte le tue vasche. Se hai più di una vasca, c'è un'etichetta filtro per ognuna, più **Tutte le vasche**.

Tocca una scena per modificarla, oppure tocca **Nuova scena** per crearne una. Se hai più di una vasca e non è scelto nessun filtro, Cora Max chiede **Per quale vasca è questa scena?**

## Creare una scena

![Un modulo Nuova scena vuoto su Cora Max](img/max-scene-builder.webp "Una nuova scena: un nome, Permanente o A tempo, Chiedi prima di eseguire, poi Aggiungi passo.")

1. Scrivi un **Nome scena**.
2. Tocca **Aggiungi passo** e scegli cosa fa il passo. Vedi solo i tipi di attrezzatura che ha questa vasca:
   - **Presa Apex**: porta una presa Neptune Apex su **ON**, **OFF** o **AUTO**.
   - **Controlla un'apparecchiatura Red Sea**: per esempio **ReefDose: dosa adesso**, **ReefDose: imposta dose giornaliera**, **ReefRun: imposta velocità pompa**, **ATO: avvia un riempimento manuale** o **ReefMat: avanza il rotolo**.
   - **Controlla una pompa di movimento**: imposta flusso o modalità onda di una pompa Jecod, accendila o spegnila, oppure **Pausa per l'alimentazione**.
   - **Avvia un test Trident**: alcalinità, combinato o nutrienti. Ogni esecuzione consuma reagente.
   - **Avvia un ciclo di alimentazione Apex**: scegli il ciclo. L'Apex gestisce il timer e riprende da solo.
3. Aggiungi altri passi allo stesso modo. Puoi riordinarli o toglierli. Un passo che questa schermata non può modificare dice **Non modificabile qui**. Modificalo dal telefono.
4. Scegli quanto dura. **A tempo** dura i minuti che imposti in **Durata (minuti)**. **Permanente** dura finché non la fermi.
5. Lascia attivo **Chiedi prima di eseguire** a meno che tu non sia sicuro che la scena non tocchi mai niente che meriti un secondo controllo.
6. Tocca **Salva**.

:::note Dosi in una scena
Una testa Neptune DŌS non può mai essere un passo di una scena. Un passo **ReefDose: dosa adesso** sì, e ha il suo **Massimo per dose (ml)**. Lascialo vuoto per 10 mL. Una dose sopra quel tetto viene rifiutata, mai ridotta. Tieni attivo **Chiedi prima di eseguire** per qualsiasi scena che dosa.
:::


## Avviare una scena

Le scene compaiono come riquadri sulla dashboard. Tocca **Esegui** per avviarne una.

Se la scena chiede conferma prima di partire, Cora Max elenca prima cosa sta per fare, una riga per passo. Leggila, poi avviala o annulla.

Mentre una scena a tempo è in corso, il suo riquadro fa il conto alla rovescia fino alla fine e mostra **Ferma** se vuoi terminarla prima. Il riquadro di una scena permanente la mostra in corso finché non tocchi **Ferma**. Quando una scena finisce o la fermi, il riquadro mostra **Ripristino…** mentre Cora rimette a posto l'attrezzatura.

Avviare o fermare una scena passa da Cora Cloud, come qualsiasi altro comando. Trovi il risultato in [Attività](/help/max-activity).

Su Cora Max le scene non si possono avviare a voce. Usa il riquadro, **Impostazioni → Automazioni**, oppure il telefono.

Se una scena non parte o non si ferma, dai un'occhiata a [Risoluzione dei problemi](/help/troubleshooting).

:::note Il blocco bambini vale anche per le scene
Mentre il [Blocco bambini](/help/max-settings#child-lock) tiene bloccato lo schermo, non puoi avviare, fermare o modificare una scena da lì, proprio come per tutti gli altri comandi.
:::

Un passaggio che fallisce o che dovrebbe aspettare non resta in sospeso. Scade subito, l'esecuzione viene registrata come non riuscita e ricevi una notifica che indica l'automazione, il passaggio e il motivo. Un passaggio fallisce, per esempio, se il suo dispositivo è offline, se nessun Cora Max può eseguirlo, se il dispositivo lo rifiuta o non risponde, oppure se un riscaldatore o un refrigeratore è stato commutato un attimo fa. Per un passaggio su una vasca rimossa non ricevi notifiche.

## Modificare o eliminare una scena

Per cambiare una scena, aprila da **Impostazioni → Automazioni** oppure tieni premuto il suo riquadro sulla dashboard. Cambia quello che ti serve e tocca **Salva**. Per toglierla, tocca **Elimina scena**. Non si può annullare.

:::note Un Cora Max più vecchio può avviare una scena ma non modificarla
Le versioni più vecchie di Cora Max mostrano e avviano comunque tutte le scene, ma non possono cambiarle. Aggiorna Cora Max ([Aggiornamenti e ripristino](/help/max-updates)), oppure modifica la scena dal telefono.
:::
