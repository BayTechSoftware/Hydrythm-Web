---
title: Prodotti di dosaggio e calcolatore di dosaggio
description: Controlla la concentrazione dei tuoi prodotti per alcalinità, calcio e magnesio, aggiungi i tuoi e usa il calcolatore di dosaggio per sapere quanto aggiungere.
section: Cora Mobile
reviewed: 2026-10-13
order: 27
group: Records
---

Cora può fare i calcoli di dosaggio solo se sa quanto sono concentrati i tuoi prodotti. Questa pagina parla dell'elenco dei prodotti e del calcolatore di dosaggio che lo usa.

Vai in **Impostazioni → Prodotti di dosaggio**.

![Prodotti di dosaggio](img/mobile-dosing.webp "I prodotti portano la concentrazione che Cora usa per i calcoli di dosaggio e consumo.")

## La libreria dei prodotti {#the-product-library}

La schermata **Prodotti di dosaggio** elenca già i prodotti più diffusi, raggruppati sotto **Alcalinità (dKH)**, **Calcio (ppm)** e **Magnesio (ppm)**. Trova il tuo e toccalo per controllarne la concentrazione.

Ogni concentrazione indica di quanto 1 ml (o 1 g di un prodotto in polvere) alza il parametro in un volume d'acqua fisso. È il numero che trasforma "5 ml" in "+0,2 dKH nella tua vasca". In alto puoi passare tra **per 100 L** e **per 100 gal**.

Cambia una concentrazione predefinita solo se la tua bottiglia dice qualcosa di diverso. Tocca il prodotto per aprire **Modifica concentrazione**. **Ripristina predefinito** rimette il valore di Cora.

## Aggiungere un prodotto tuo {#adding-your-own}

Se il tuo prodotto non è in elenco, tocca **+** (**Aggiungi prodotto personalizzato**). Dagli un **Nome del prodotto**, scegli **Liquido (ml)** o **Secco (g)** e inserisci la sua concentrazione per alcalinità, calcio o magnesio. Lascia vuoto un campo se il prodotto non influisce su quel parametro. Un due componenti ne compila uno per parte, un prodotto bilanciato ne compila diversi.

La concentrazione è quasi sempre sull'etichetta, con una frase come "1 ml ogni 100 litri alza l'alcalinità di 0,1 dKH".

:::warning Usa la concentrazione indicata dal produttore
Se la concentrazione è sbagliata, ogni dose che Cora calcola per quel prodotto è sbagliata nella stessa proporzione. Se non trovi il dato, lascia fuori il prodotto. Non tirare a indovinare.
:::

I prodotti per nitrati e fosfati vengono dall'elenco di Cora nel calcolatore. Non puoi aggiungerli qui.

La **miscela di sale** della tua vasca non è un prodotto di dosaggio. La imposti nel profilo della vasca, e Cora ha un catalogo dei sali per reef più diffusi con i valori pubblicati, con le fonti, da cui scegliere. Vedi [Il profilo della vasca](/help/mobile-tank-profile).

## Il calcolatore di dosaggio {#the-dose-calculator}

Il calcolatore calcola quanto prodotto serve per portare un parametro al suo valore obiettivo. È disponibile per alcalinità, calcio, magnesio, nitrati e fosfati.

1. Sulla dashboard, tocca il widget del parametro per aprirlo.
2. Tocca l'icona del calcolatore in alto. Un puntino sull'icona significa che la lettura è sotto l'obiettivo.
3. Controlla i numeri che Cora ha inserito:
   - Il valore attuale è la tua lettura più recente. Aggiornalo se hai appena fatto un test.
   - L'obiettivo è il centro del tuo intervallo di avviso per quel parametro, oppure l'intervallo tipico da reef se non ne hai impostato uno.
   - **Volume d'acqua netto (L)** è il 90% del volume della vasca, per tenere conto di rocce e sabbia. Cambialo se conosci il valore reale.
4. Scegli il **Prodotto**. Prima vengono i tuoi prodotti dal profilo della vasca, poi i preset delle marche. Puoi anche inserire una **Concentrazione personalizzata**.

Cora mostra il totale necessario per raggiungere l'obiettivo.

:::warning Distribuisci una correzione grande
Il calcolatore dà il totale, non una dose giornaliera. Se il totale è un salto più grande di quanto sia sicuro in un giorno, te lo dice, e lo dividi su più giorni. **Chiedi a Cora** apre Cora Assistant con i tuoi numeri, se vuoi aiuto per decidere quanto dare al giorno.
:::

Quando hai dosato, tocca **Registra la dose che hai dato**. Aggiunge una voce al tuo [diario](/help/mobile-journal).

Se sei già all'obiettivo o sopra, il calcolatore ti dice che non c'è niente da aggiungere. Un parametro non si abbassa dosando. La soluzione è un cambio d'acqua, un cambio dei materiali filtranti o una modifica a quello che già dosi.

Qui conta il volume. Se è sbagliato del 20%, anche le dosi sono sbagliate del 20%.

## Consumi {#consumption}

Quando Cora vede sia i tuoi dosaggi sia le tue letture, può calcolare quanto consuma la vasca e dirti quando il consumo cambia.

Quando il consumo cambia, guarda meglio prima di trarre conclusioni. Un maggiore consumo di alcalinità spesso significa crescita, ma uno spostamento improvviso in un senso o nell'altro può venire anche da una dose saltata, un errore nel test, una precipitazione, un cambio d'acqua o una modifica all'attrezzatura. Controlla cos'altro è cambiato intorno a quella data.

## Attrezzatura di dosaggio {#dosing-equipment}

Se hai una pompa dosometrica collegata, come un Neptune DŌS o un Red Sea ReefDose, le sue teste compaiono con le loro letture, compreso quanto resta a ogni testa e quanto ha dosato. Come farle funzionare e rifornirle è spiegato in [Controllare la tua attrezzatura](/help/mobile-device-control), e i loro avvisi di contenitore quasi vuoto e di dose mancata sono in [Avvisi della pompa dosometrica](/help/mobile-device-control#doser-alerts).

Anche un'automazione può dosare da una testa DŌS, con un limite di 10 mL per testa al giorno. Vedi [Automazioni e scene](/help/mobile-automation#actions).
