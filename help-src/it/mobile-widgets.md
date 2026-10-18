---
title: Guida ai widget
description: Tutti i tipi di widget della dashboard di Cora Mobile, da valore, indicatore, grafico, stato e presa ai riquadri dei dispositivi, e quando usare ognuno.
section: Cora Mobile
reviewed: 2026-10-13
order: 9
group: Your dashboard
---

Un widget è un riquadro della dashboard e mostra una cosa sola. Questa pagina passa in rassegna ogni tipo e cosa puoi impostarci.

I widget si aggiungono e si dispongono nell'[editor della dashboard](/help/mobile-dashboard-editing). Lì tocca un widget per aprirne le impostazioni: **Tipo** e **Parametro** per un parametro, la presa o il dispositivo per gli altri, poi **Larghezza** e **Altezza**, e **Intervallo di tempo** per un grafico.

![Il pannello delle impostazioni di un widget in Cora Mobile](img/mobile-widget-config.webp "La metà inferiore delle impostazioni di un widget: parametro, larghezza, altezza e intervallo di tempo, poi Rimuovi e Fatto.")

## I quindici tipi {#the-fifteen-types}

| Tipo | Cosa mostra |
|---|---|
| **Valore** | La lettura attuale, con unità, età e fonte |
| **Indicatore** | Un arco con il tuo intervallo segnato in fasce e un pallino sul valore |
| **Grafico** | Una tendenza nel periodo che scegli |
| **Stato** | La lettura scritta a parole con un pallino colorato |
| **Presa** | Un comando a tre posizioni: Auto, Off, On |
| **ReefBeat** | Un'unità Red Sea, con il suo riepilogo |
| **Modulo Apex** | Un modulo Apex installato, come un Trident o un DŌS |
| **Jecod** | Una pompa Jecod, con modalità e intensità |

Tutto quello che viene dopo Presa è un riquadro **dispositivo**. Ognuno appartiene a un apparecchio invece che a un parametro, e mostra quello che l'unità riporta. Cora Max ha anche un riquadro **Scena**, che aggiungi su Cora Max. Vedi [Modificare la dashboard di Cora Max](/help/max-dashboard-editing).


## Dimensioni {#sizing}

**Larghezza** e **Altezza** possono essere ciascuna **1×** o **2×**, quindi un widget è largo una o due celle e alto una o due celle. Un grafico non è mai largo una sola cella. Su una dashboard a tre colonne, un indicatore largo due occupa due terzi della riga. Di solito è una buona forma per il tuo parametro più importante.

## Cosa mostra un widget di parametro {#what-a-parameter-widget-shows}

I widget Valore, Indicatore, Grafico e Stato mostrano tutti un parametro misurato, e mostrano sempre tre cose. I riquadri di prese e dispositivi mostrano il loro stato, perché dietro non c'è una singola lettura.

- **Il valore**, in grande
- **L'età** (`now`, `1h`, `2d`), cioè quanto tempo fa la fonte ha confermato il valore l'ultima volta. Per una sonda è quando il suo dispositivo si è fatto sentire l'ultima volta, quindi una lettura stabile resta fresca. Per un test o un risultato ICP è quando hai fatto il test. Di più in [Leggere la dashboard](/help/mobile-dashboard#how-to-read-a-parameter-widget).
- **La fonte**, un piccolo badge che dice da dove arriva il numero

Un widget di parametro non ha un'impostazione di intervallo o di fonte sua. L'intervallo viene dalle soglie di avviso della vasca (tieni premuto il widget sulla dashboard), e la fonte da [Mappatura parametri](/help/mobile-probes). Tocca il widget sulla dashboard per vedere lo storico completo, tutte le fonti che lo riportano e la tua fascia di avviso.

## Valore {#value}

È il numero puro. Mostra la lettura attuale, l'unità, quanto è vecchia e da dove arriva.

Usalo per i parametri che controlli più dal numero che dalla tendenza, come calcio, magnesio o nitrati.

## Indicatore {#gauge}

Un indicatore è un arco con il tuo intervallo di avviso segnato sopra e un pallino sul valore attuale. Il colore del pallino ti dice dove sei: dentro l'intervallo, in deriva o fuori.

Usalo per i parametri che gestisci attivamente, come alcalinità, pH, salinità o temperatura.

:::note Dai agli indicatori almeno due colonne
Su una sola colonna l'arco è troppo piccolo per leggerlo al volo. Se hai poco spazio, usa un widget **Valore**.
:::

## Grafico {#graph}

Un grafico è una piccola linea di andamento nel periodo che scegli: 1h, 6h, 24h, 7g, 30g o 1a. Segna il massimo e il minimo e indica il valore attuale.

Per un parametro che misuri con i test (con un Trident o un kit), la linea unisce i tuoi test reali. Se nel periodo c'è un solo test, la linea arriva dal test precedente, e non ci sono massimo e minimo. Se nel periodo non c'è nessun test, o non c'è niente di precedente a cui collegare un test isolato, il riquadro mostra **Raccolta in corso…** al posto della linea.

Usalo per tutto quello che si muove, come il pH durante il giorno, la temperatura in un'ondata di caldo o l'alcalinità tra un dosaggio e l'altro.

Un grafico è sempre largo **almeno due celle**. Una linea schiacciata in una cella non dice niente, quindi l'editor non te lo permette.

:::note Scegli il periodo adatto al parametro
Il pH oscilla con un ciclo giornaliero, quindi con 24 ore ne vedi l'andamento. L'alcalinità si muove nell'arco di giorni, quindi 7 o 30 giorni ti dicono molto di più.
:::

## Stato {#status}

Mostra la lettura scritta a parole, con un pallino colorato per dentro l'intervallo, in deriva o fuori. Usalo per un parametro che non ha un intervallo utile per un indicatore.

## Presa {#outlet}

È un interruttore a tre posizioni per una presa Apex: **Auto**, **Off** e **On**. Scegli tu quale presa comanda.

- **Auto** restituisce la presa a quello che la gestisce di solito. Può essere una programmazione, una regola o il controller a cui appartiene.
- **Off** e **On** sono comandi manuali. Restano finché non li cambi tu.

:::warning I comandi manuali non scadono
Off vuol dire spento finché non la rimetti su Auto. Se spegni una pompa di risalita per lavorare in vasca, rimettila su Auto quando hai finito. Cora non lo fa al posto tuo.
:::

## ReefBeat {#reefbeat}

È un riquadro per un intero apparecchio. Mostra il riepilogo dell'unità invece di un singolo parametro, per esempio stato e serbatoio di un ATO, le teste di una pompa dosometrica o quanti giorni restano al rotolo di un ReefMat. Scegli tu quale dispositivo mostra.

Quali dispositivi possono avere un riquadro dipende da cosa hai collegato. Vedi [Collegare la tua attrezzatura](/help/mobile-connections).

## Riquadri delle pompe dosometriche {#doser-tiles}

Il riquadro di una pompa dosometrica (un Apex DŌS o un ReefDose) mostra una riga per testa. Il nome di una testa non viene mai rimpicciolito sotto una dimensione leggibile. Su un riquadro alto la riga occupa due linee, con il nome sulla prima e quello che resta sulla seconda, per esempio *40g* e *2,8 L*. Su un riquadro basso la linea di dettaglio viene tolta e il nome resta leggibile.

Imposta cosa viene prima con **Mostra il rimanente come**: **Giorni** o **Millilitri (mL)**. Una testa ReefDose senza un nome suo viene mostrata con il nome del dispositivo seguito da "testa" e dal suo numero. Il riquadro di una pompa dosometrica Jecod è in sola lettura e mostra il piano giornaliero, perché Jecod non riporta quanto resta nel flacone.
