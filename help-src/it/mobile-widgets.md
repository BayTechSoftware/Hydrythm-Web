---
title: Guida di riferimento ai widget
description: Tutti i tipi di widget di Cora (valore, indicatore, grafico, stato, presa e riquadri dei dispositivi) e quando usarli.
section: Cora Mobile
reviewed: 2026-09-17
order: 7
group: Your dashboard
---

Un widget è un riquadro della dashboard che mostra una cosa sola. Qui trovi tutti i tipi e cosa puoi impostare per ciascuno.

I widget si aggiungono e si dispongono nell'**[editor della dashboard](/help/mobile-dashboard-editing)**. Lì tocca un widget per aprirne le impostazioni.

![Configurazione di un widget](img/mobile-widget-config.webp "Tipo, parametro, poi larghezza e altezza.")

## I nove tipi

| Tipo | Cosa mostra |
|---|---|
| **Valore** | La lettura attuale con unità, età e fonte |
| **Indicatore** | Un arco con il tuo intervallo diviso in fasce e un pallino sul valore |
| **Grafico** | L'andamento nel periodo che scegli |
| **Stato** | Uno stato scritto a parole: in funzione, inattivo, chiuso |
| **Presa** | Un comando a tre posizioni: Auto, Off, On |
| **ReefBeat** | Un'unità Red Sea con il suo riepilogo |
| **Modulo Apex** | Un modulo Apex installato, come un Trident o un DŌS |
| **Jecod** | Una pompa Jecod con modalità e intensità |
| **Maxspect** *(beta)* | Una gyre con entrambi i motori |

Gli ultimi quattro sono riquadri **dispositivo**. Sono legati a un apparecchio e non a un parametro, e mostrano quello che l'unità riporta.

## Dimensioni del riquadro

**Larghezza** e **Altezza** possono essere **1×** o **2×**. Un grafico non è mai largo una sola cella.

## Valore

Il numero e basta: lettura attuale, unità, età e fonte.

Usalo per i parametri di cui ti interessa il numero più dell'andamento: calcio, magnesio, nitrati.

Puoi impostare etichetta, fonte e dimensione.

## Indicatore

Un arco con l'intervallo obiettivo diviso in fasce e un pallino sul valore attuale. Il colore del pallino ti dice come sei messo: dentro la fascia, in deriva o fuori.

Usalo per i parametri che gestisci attivamente: alcalinità, pH, salinità, temperatura.

Puoi impostare etichetta, fonte, intervallo (preso dagli obiettivi della vasca, a meno che tu non lo cambi qui) e dimensione.

:::note Dai agli indicatori almeno due colonne
Su una sola colonna l'arco è troppo piccolo per leggerlo al volo. Se hai poco spazio, usa un widget **valore**.
:::

## Grafico

Una piccola linea dell'andamento nel periodo che scegli, con il massimo e il minimo segnati e il valore attuale in evidenza.

Per un parametro che misuri con i test (con il Trident o con un kit), la linea unisce i test che hai fatto. Se nel periodo c'è un solo test, la linea parte dal test precedente e non vengono segnati massimo e minimo. Se nel periodo non c'è nessun test, o se prima di un test isolato non c'è niente da collegare, al posto della linea compare **Raccolta in corso…**.

Usalo per tutto quello che si muove: il pH durante il giorno, la temperatura durante un'ondata di caldo, l'alcalinità tra un dosaggio e l'altro.

Puoi impostare etichetta, fonte, **intervallo di tempo** (1 ora, 6 ore, 24 ore, 7 giorni, 30 giorni, 1 anno) e dimensione.

Un grafico è sempre largo **almeno due celle**. In una cella sola la linea non direbbe niente, quindi l'editor non lo permette.

:::note Scegli il periodo in base al ritmo del parametro
Il pH varia nel corso della giornata, quindi con 24 ore ne vedi l'andamento. L'alcalinità cambia nell'arco di giorni, quindi 7 o 30 giorni ti dicono molto più di 24 ore.
:::

## Stato

Uno stato scritto a parole, senza numeri: in funzione, inattivo, aperto, chiuso, in alimentazione.

Puoi impostare etichetta, fonte e dimensione.

## Presa

Un interruttore a tre posizioni per una presa: **Auto**, **Disattivata**, **On**.

- **Auto** restituisce la presa a chi la gestisce di solito: un programma, una regola o il controller a cui appartiene.
- **Disattivata** e **On** sono comandi manuali che restano finché non li cambi tu.

Puoi impostare etichetta, presa e dimensione.

:::warning Un comando manuale non scade
Off resta off finché non rimetti Auto. Se spegni la pompa di risalita per lavorare in vasca, rimettila su Auto quando hai finito. Cora non lo fa al posto tuo.
:::

## ReefBeat

Un riquadro per un intero apparecchio, con il suo riepilogo al posto di un singolo parametro: stato e serbatoio di un ATO, teste di un'unità di dosaggio, giorni rimasti di un rullo per tappetino.

I dispositivi che puoi mettere in un riquadro dipendono da cosa hai collegato. Vedi **[Collegare la tua attrezzatura](/help/mobile-connections)**.

Puoi impostare etichetta, dispositivo e dimensione.

## Cosa mostra un widget di parametro

Un widget legato a un parametro misurato (Valore, Indicatore, Grafico e Stato) mostra sempre tre cose. I riquadri di prese e dispositivi mostrano invece il loro stato, perché dietro non c'è una singola lettura:

- **Il valore**, in grande
- **L'età** (`now`, `1h`, `2d`), cioè quanto è vecchia la lettura, non quando si è aggiornato lo schermo
- **La fonte**, un piccolo badge che dice da dove arriva il numero

Tocca un widget per aprire lo storico completo, tutte le fonti che misurano il parametro e le soglie in vigore.

## Misure

I widget sono larghi una o due celle e alti una o due celle. Fa eccezione il **grafico**, che è sempre largo almeno due celle. Su una dashboard a tre colonne un indicatore largo due occupa due terzi della riga, e di solito è la forma giusta per il parametro più importante.
