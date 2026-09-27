---
title: Prese e controlli
description: Commutare le prese da Cora Max, usare la modalità alimentazione, e cosa significa davvero Auto.
section: Cora Max
reviewed: 2026-09-09
order: 5
group: Equipment
---

Cora Max può commutare l'equipaggiamento sul tuo sistema: dai widget di controllo sulla dashboard, dal cassetto Prese e Alimentazione, o a voce.

:::warning Questi controlli agiscono sulla tua vasca
Non c'è annullamento. Le prese contrassegnate con un lucchetto ti chiedono prima di confermare; il resto si applica non appena tocchi. Un comando può tornare **Confermato**, **Non confermato** (inviato, nulla riportato), **Rifiutato** o **Nessun cambiamento**; vedi [Controllare il tuo equipaggiamento](/help/mobile-device-control).
:::

## I tre stati

Ogni presa è in uno dei tre stati.

**Auto** restituisce la presa alla programmazione del suo Apex. Qui è dove una presa dovrebbe stare la maggior parte del tempo.

**Disattivata** e **On** sono sovrascritture manuali. Hanno effetto immediato e **restano finché non le cambi di nuovo**. Non scadono, e nulla le ripristina per te.

:::warning Una sovrascrittura manuale non scade
Riportala su **Auto** quando hai finito; nulla lo fa per te. Può ancora essere cambiata più avanti da te, a voce, o da un'automazione; una sovrascrittura non è un blocco.
:::

## Commutare dalla dashboard

I widget di controllo mostrano i tre stati con quello attuale evidenziato. Tocca lo stato che vuoi.

Alcune prese portano un **lucchetto**. Non deve essere disattivato da nessuna parte; significa che la presa chiede di confermare prima di cambiare, così un tocco accidentale non può commutare qualcosa di critico. Vedi sotto.

## Il cassetto Controlli

Tira su la scheda in fondo alla dashboard per aprire **Controlli**: ogni presa del sistema in un solo posto, che abbia o no un widget, più i cicli di alimentazione.

![Il cassetto Controlli](img/max-controls.webp "Cicli di alimentazione in alto, poi ogni presa.")

Una presa che porta un **lucchetto** richiede una conferma esplicita prima di cambiare. Toccarla apre una finestra che nomina la presa, il suo stato attuale, e la sovrascrittura che stai per applicare. È un passaggio di conferma, non un blocco da disattivare altrove.

## Modalità alimentazione

La modalità alimentazione è il modo sicuro per sospendere il flusso per l'alimentazione. Sospende l'equipaggiamento che dovrebbe essere sospeso, lascia stare quello che non dovrebbe, e **ripristina tutto da sola** quando il tempo è finito.

Usala di preferenza allo spegnere le pompe a mano, perché ripristina il sistema senza dipendere dal fatto che tu te ne ricordi.

I cicli di alimentazione sono contrassegnati con le lettere **A**, **B**, **C** e **D**: i cicli che il tuo controller definisce, ognuno sospendendo un insieme diverso di equipaggiamento. Scegli quello che corrisponde a ciò che stai facendo. **Annulla** termina un ciclo in corso in anticipo e ripristina tutto immediatamente.

Avviane uno dal cassetto Controlli, oppure dì *"avvia modalità alimentazione"*.

## A voce

Puoi commutare le prese a voce: *"spegni lo skimmer"*, *"rimetti la ventola in auto"*.

Qualsiasi cosa che raggiunge il tuo equipaggiamento viene **confermata prima che accada**: Cora ti dice cosa sta per fare e aspetta che tu sia d'accordo. Non agirà su un'istruzione di cui non è sicura.

Vedi **[Parlare con Cora](/help/max-voice)**.

## Vedere cosa è successo

Ogni richiesta viene registrata, insieme a cosa l'ha richiesta (questa app, uno schermo Cora, la voce, l'Assistant, una regola di automazione, un pulsante smart o il tuo account) e come è arrivata. Sul tuo telefono è **Impostazioni → Attività**.

Questo è il primo posto da controllare quando qualcosa è cambiato e non sai perché.
