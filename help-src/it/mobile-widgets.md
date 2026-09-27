---
title: Guida di riferimento ai widget
description: Ogni tipo di widget in Cora (valore, indicatore, grafico, stato, presa e i riquadri dei dispositivi) e quando usare ciascuno.
section: Cora Mobile
reviewed: 2026-09-17
order: 7
group: Your dashboard
---

Un widget è un riquadro sulla tua dashboard che mostra una cosa. Questa pagina descrive ogni tipo e cosa puoi configurare.

Aggiungili e disponili nell'**[editor della dashboard](/help/mobile-dashboard-editing)**; toccane uno lì per aprire le sue impostazioni.

![Configurazione di un widget](img/mobile-widget-config.webp "Tipo, parametro, poi larghezza e altezza.")

## I nove tipi

| Tipo | Mostra |
|---|---|
| **Valore** | La lettura attuale, la sua unità, età e fonte |
| **Indicatore** | Un arco con il tuo intervallo suddiviso in fasce e una lancetta sul valore |
| **Grafico** | Una tendenza nel periodo che scegli |
| **Stato** | Uno stato come testo: in funzione, inattivo, chiuso |
| **Presa** | Un controllo a tre posizioni: Auto, Off, On |
| **ReefBeat** | Un'unità Red Sea, con il suo riepilogo |
| **Modulo Apex** | Un modulo Apex montato, come un Trident o un DŌS |
| **Jecod** | Una pompa Jecod, con la sua modalità e intensità |
| **Maxspect** *(beta)* | Una gyre, con entrambi i motori |

Gli ultimi quattro sono riquadri **dispositivo**: sono legati a un pezzo di equipaggiamento invece che a un parametro, e ciascuno mostra qualunque cosa quell'unità riporti.

## Dimensionamento

**Larghezza** e **Altezza** sono ciascuna **1×** o **2×**. Un grafico non è mai largo una sola cella.

## Valore

Il numero semplice. Lettura attuale, la sua unità, quanto è vecchia e da dove viene.

Usalo per i parametri che controlli numericamente più che per tendenza: calcio, magnesio, nitrati.

**Impostazioni:** etichetta, fonte, dimensione.

## Indicatore

Un arco con il tuo intervallo obiettivo suddiviso in fasce e una lancetta sul valore attuale. Il colore della lancetta ti dice dove ti trovi: dentro la fascia, in deriva, o fuori.

Usalo per i parametri che gestisci attivamente: alcalinità, pH, salinità, temperatura.

**Impostazioni:** etichetta, fonte, intervallo (ereditato dagli obiettivi della tua vasca a meno che non lo sovrascrivi qui), dimensione.

:::note Dimensiona gli indicatori a due colonne o più
Su una singola colonna l'arco è troppo piccolo da leggere a colpo d'occhio; usa invece un widget di **valore** se lo spazio è limitato.
:::

## Grafico

Uno sparkline nel periodo che scegli, con il massimo e il minimo segnati e il valore attuale evidenziato.

Per un parametro che testi (via Trident o con un kit di test), la linea collega i tuoi test effettivi. Se il periodo contiene solo un test, la linea entra dal test precedente, e non viene segnato nessun massimo o minimo. Senza alcun test nel periodo, o senza nulla prima a cui collegare un singolo test, il riquadro mostra **Raccolta in corso…** invece di una linea.

Usalo per qualsiasi cosa che si muove: pH durante il giorno, temperatura durante un'ondata di calore, alcalinità tra un dosaggio e l'altro.

**Impostazioni:** etichetta, fonte, **intervallo di tempo** (1 ora, 6 ore, 24 ore, 7 giorni, 30 giorni, 1 anno), dimensione.

Un grafico di tendenza è sempre largo **almeno due celle**; uno sparkline compresso in una sola cella non ti direbbe nulla, quindi l'editor non ne creerà uno.

:::note Scegli il periodo in base al ritmo
Il pH oscilla su un ciclo giornaliero, quindi 24 ore ti mostra la forma. L'alcalinità si muove nell'arco di giorni, quindi 7 o 30 ti dicono più di quanto potrà mai dirti 24.
:::

## Stato

Testo invece di un numero, per cose che sono uno stato. In funzione, inattivo, aperto, chiuso, in alimentazione.

**Impostazioni:** etichetta, fonte, dimensione.

## Presa

Un interruttore a tre posizioni per una presa: **Auto**, **Disattivata**, **On**.

- **Auto** restituisce la presa a qualunque cosa normalmente la gestisca: un programma, una regola, o il controller a cui appartiene.
- **Disattivata** e **On** sono sovrascritture manuali che restano fino a quando non le cambi di nuovo.

**Impostazioni:** etichetta, quale presa, dimensione.

:::warning Una sovrascrittura manuale non scade
Off significa off finché non lo riporti su Auto. Se spegni una pompa di risalita per lavorare nella vasca, riportala su Auto quando hai finito; Cora non lo farà per te.
:::

## ReefBeat

Un riquadro per un intero pezzo di equipaggiamento, che mostra il proprio riepilogo invece di un singolo parametro: lo stato e il serbatoio di un ATO, le teste di un'unità di dosaggio, i giorni rimanenti di un rullo per il tappetino.

Quali dispositivi offrono un riquadro dipende da cosa hai collegato. Vedi **[Collegare il tuo equipaggiamento](/help/mobile-connections)**.

**Impostazioni:** etichetta, quale dispositivo, dimensione.

## Cosa mostra un widget di parametro

Su un widget basato su un parametro misurato (Valore, Indicatore, Grafico e Stato), sono sempre presenti tre cose. I riquadri di presa e dispositivo mostrano invece il proprio stato, perché non c'è una singola lettura dietro di essi:

- **Il valore**, grande
- **L'età** (`now`, `1h`, `2d`): da quanto tempo è la lettura, non da quanto tempo si è aggiornato lo schermo
- **La fonte**: un piccolo badge che indica da dove viene il numero

Tocca qualsiasi widget per aprire il suo storico completo, ogni fonte che lo riporta, e le soglie in vigore.

## Dimensioni

I widget sono larghi una o due celle e alti una o due celle, eccetto un **grafico di tendenza**, che è sempre largo almeno due. Su una dashboard a tre colonne, un indicatore largo due prende due terzi della riga, che è di solito la forma giusta per il tuo parametro più importante.
