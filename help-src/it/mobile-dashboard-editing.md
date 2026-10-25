---
title: Modificare la dashboard
description: Aggiungi, sposta, ridimensiona e rimuovi i widget sulla dashboard del telefono, imposta il numero di colonne e modifica dal telefono la dashboard di un Cora Max.
section: Cora Mobile
reviewed: 2026-10-18
order: 8
group: Your dashboard
twin: max-dashboard-editing
---

L'editor della dashboard decide quali widget compaiono sulla dashboard di una vasca e come sono disposti. Ogni vasca ha il suo layout, che segue il tuo account su qualsiasi telefono con cui accedi.

## Aprire l'editor {#opening-the-editor}

Scorri la dashboard verso il basso e tocca **Modifica dashboard**, subito sotto i widget. L'editor si apre come **Modifica dashboard**, con il suggerimento **Tocca a lungo un riquadro per spostarlo. Tocca per configurarlo.**

:::note La matita nell'intestazione della vasca apre un'altra cosa
Apre **Modifica vasca**, il profilo della vasca con volume, popolazione, dosaggio, illuminazione e flusso. Ne parliamo in [Il profilo della vasca](/help/mobile-tank-profile).
:::

![La schermata Modifica dashboard in Cora Mobile](img/mobile-edit.webp "Le colonne in alto, poi ogni riquadro con il suo nome e tipo. Tocca una croce rossa per rimuoverlo.")

## Impostare il numero di colonne {#setting-the-column-count}

Scegli **2**, **3** o **4** accanto a **COLONNE** in alto nell'editor. La griglia si allunga verso il basso man mano che aggiungi widget, e la dashboard scorre.

| Colonne | Quando usarle |
|---|---|
| 2 | Segui pochi parametri e vuoi riquadri grandi |
| 3 | L'impostazione predefinita. Va bene per la maggior parte delle vasche |
| 4 | Vuoi una vista fitta, o hai un telefono grande |

## Aggiungere un widget {#adding-a-widget}

1. Tocca **Aggiungi riquadro** sotto la griglia, oppure tocca una cella vuota.
2. In **Aggiungi un riquadro**, scegli di che tipo è. **Parametro** comprende un valore, un indicatore, un grafico o uno stato per un parametro. **Presa** comanda una presa Apex. Le altre righe sono per l'attrezzatura, come **ReefBeat**, **Trident**, **DŌS** o **Jecod**. La maggior parte compare solo quando la vasca ha quell'attrezzatura. **Luce**, **Pompa di movimento** e **Pompa** elencano tutte le luci, le pompe di movimento e le pompe della vasca, di qualsiasi marca, e ciascuna compare solo quando la vasca ne ha una. **ReefBeat** e **Jecod** tengono gli altri dispositivi, come una ReefDose o una pompa dosometrica Jecod.
3. Scegli il parametro, la presa o il dispositivo.
4. Per un parametro, scegli il tipo. La [Guida ai widget](/help/mobile-widgets) li descrive tutti.

Vedi solo i parametri che la vasca ha. Un parametro senza fonte compare quando colleghi un'attrezzatura che lo riporta, oppure registri una lettura a mano.

La griglia contiene fino a 20 righe. Quando è piena, Cora dice **La dashboard è piena: rimuovi prima un riquadro.** Un grafico ha bisogno di due celle libere affiancate.


Quando togli un dispositivo da una vasca, i suoi riquadri lasciano la dashboard da soli, sul telefono e su ogni Cora Max di quella vasca. Un riquadro il cui dispositivo non c'è più dice **Questo dispositivo non è più in questa vasca** e non apre nulla.

## Disporre i widget {#arranging-widgets}

- Per spostare un widget, tienilo premuto e trascinalo. Gli altri si spostano intorno.
- Per rimuovere un widget, tocca la croce rossa nel suo angolo, oppure tocca il widget e poi **Rimuovi**.
- Per cambiare le impostazioni di un widget, toccalo.

## Impostazioni del widget {#widget-settings}

Tocca un widget nell'editor per aprirne le impostazioni. A seconda del widget, puoi impostare:

| Impostazione | Vale per |
|---|---|
| **Tipo** | Widget di parametro: Valore, Indicatore, Grafico o Stato |
| **Parametro** | Widget di parametro: quale parametro mostra |
| La presa o il dispositivo | Riquadri di prese e attrezzatura: quale mostra |
| **Mostra il rimanente come** | Riquadri delle pompe dosometriche: **Giorni** o **Millilitri (mL)** |
| **Larghezza** | Ogni widget: **1×** o **2×**. Un grafico è sempre largo almeno 2 |
| **Altezza** | Ogni widget: **1×** o **2×** |
| **Intervallo di tempo** | Grafico: 1h, 6h, 24h, 7g, 30g o 1a |

Tocca **Fatto** per tenere le impostazioni, oppure **Rimuovi** per togliere il widget.

Un widget non ha un'etichetta, una fonte o un intervallo suoi. Il suo intervallo di avviso viene dalle soglie di avviso della vasca: tieni premuto il widget sulla dashboard, oppure vedi [Avvisi e soglie](/help/mobile-alerts). Quale fonte segue un parametro si imposta per vasca in [Mappatura parametri](/help/mobile-probes).

## Salvare {#saving}

Tocca **Salva** per tenere il layout. Per buttare via le modifiche, tocca l'icona di chiusura. Se hai cambiato qualcosa, Cora chiede **Scartare le modifiche?** Tocca **Scarta**, oppure **Continua a modificare** per tornare indietro.

L'editor del telefono non ha un annulla e non ha design salvati. Letture, storico e voci del diario sono salvati separatamente dal layout, quindi modificare una dashboard non può mai farli perdere.

## Modificare la dashboard di Cora Max {#editing-the-cora-max-dashboard}

La dashboard di Cora Max la modifichi a parte, da **Dispositivi →** il tuo Cora Max **→ Layout dashboard**, sulla scheda della vasca. Usa una griglia fissa che non scorre, e niente arriva su Cora Max finché non tocchi **Salva e pubblica**.

Quell'editor ha tre cose in più rispetto alla dashboard del telefono:

- **Le mie dashboard** conserva fino a 30 design salvati sul tuo account. Qualsiasi Cora Max dell'account può caricarne uno. I riquadri che la destinazione non può riempire sono elencati sotto **Lasciati indietro:** prima del caricamento.
- **Modelli** apre **Modelli di dashboard**: **Panoramica**, **Attrezzatura** e **Parametri**. È disponibile con tutti i piani e non usa l'IA.
- **Progetta con l'IA**, con un piano a pagamento o durante la prova, propone un layout completo in base a quello che la vasca riporta e ha collegato. Puoi fare 5 design per vasca al giorno.

Come funziona ognuno è spiegato in [Modificare la dashboard di Cora Max](/help/max-dashboard-editing).
