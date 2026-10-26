---
title: Dispositivi e salute dei dispositivi
description: Guarda e rinomina l'attrezzatura che Cora Max legge, scegli quale Cora Max legge ogni vasca e sistema una vasca le cui letture si sono fermate.
section: Cora Max
reviewed: 2026-10-17
order: 7
group: Equipment
twin: mobile-devices
---

**Impostazioni → Dispositivi** su Cora Max elenca l'attrezzatura che vede e come sta ogni dispositivo. L'icona dei dispositivi nella barra in alto apre lo stesso elenco, filtrato sulla vasca sullo schermo.

## L'elenco dei dispositivi {#the-device-list}

![L'elenco dei dispositivi su Cora Max, filtrato per vasca e raggruppato per marca](img/max-devices.webp "Filtra per vasca, poi ogni dispositivo raggruppato per marca, con un riassunto di una riga e la sua vasca.")

Cora Max vede la stessa attrezzatura del telefono, perché entrambi leggono lo stesso account.

Nell'elenco vengono prima le famiglie Cora, poi ogni marchio dalla A alla Z.

Usa le etichette filtro in alto per mostrare **Tutte le vasche** o una sola. I dispositivi sono raggruppati per marca. Ogni voce ha un pallino di stato (grigio quando Cora non lo sa ancora, verde quando funziona, arancione per un avviso o un guasto, rosso quando è offline), un riassunto di una riga di quello che contiene il dispositivo (*21 prese · 4 alimentazioni*, *19 test rimanenti*), la vasca a cui appartiene e il suo **Ultimo contatto**.

Tocca un dispositivo per aprirne la pagina. Ogni pagina dispositivo si apre con una sezione **Stato**. Cosa può fare ogni pagina è spiegato in [Controllare l'attrezzatura da Cora Max](/help/max-device-control).

Se l'elenco dice **Alcuni dispositivi sono ancora in caricamento: questo elenco potrebbe essere incompleto.**, aspetta un attimo.


### Rinominare un dispositivo {#renaming-a-device}

Tocca la matita sulla riga di un dispositivo, o nella sua pagina, e scrivi il nuovo nome. Lascia vuoto il nome per tornare al nome originale del dispositivo. Il nome è condiviso con il telefono, quindi cambia anche lì.

### Aggiungere e rimuovere dispositivi {#adding-and-removing-devices}

I dispositivi si aggiungono, si assegnano e si rimuovono dal telefono. Cora Max li mostra e li comanda. Se non ci sono ancora dispositivi, questa schermata dice **Aggiungi dispositivi nell'app Cora.** Di più in [Aggiungere, modificare e rimuovere dispositivi](/help/mobile-devices).

## Cora Max principale: quale dispositivo parla con la tua attrezzatura {#primary-cora-max}

Il **Cora Max principale** è il Cora Max (o un altro dispositivo Cora) che legge il controller e il resto dell'attrezzatura di una vasca per tutto l'account. A ogni vasca basta un solo dispositivo che lo faccia. Tutti gli altri schermi mostrano quello che legge.

Per vederlo o cambiarlo, apri **Impostazioni → [la tua vasca] → Cora Max principale**. Hai due opzioni.

- **Qualsiasi attivo (automatico)** vuol dire che ogni dispositivo Cora online che può raggiungere l'attrezzatura di questa vasca si divide il lavoro, e vince l'ultima scrittura. Usalo a meno che tu non abbia un motivo per fissare un dispositivo.
- Fissa un dispositivo, così solo quel dispositivo legge l'attrezzatura. Se va offline, nessun altro Cora Max prende il suo posto. Solo Cora Mobile, aperta sullo stesso Wi-Fi, legge l'attrezzatura finché non ne fissi un altro o torni a **Qualsiasi attivo (automatico)**.


Lo imposti una volta per la vasca, e vale per ogni schermo Cora. Puoi cambiarlo da qualsiasi Cora Max che mostra la vasca, oppure da Cora Mobile (**Rendi Cora Max principale** nella pagina del Cora Max). Di più in [Più di un dispositivo Cora](/help/mobile-multi-device).

:::note Cora Max principale e dispositivo di risposta sono due impostazioni separate
Il Cora Max principale decide quale dispositivo **legge la tua attrezzatura**. Il **Dispositivo di risposta** in Cora Mobile decide quale **risponde a "Hey Cora"**. Se hai più di un Cora Max, puoi impostarli separatamente. Di più in [Parlare con Cora](/help/max-voice).
:::

## Se le letture di una vasca si fermano {#if-a-tanks-readings-stop}

Se le letture di una vasca si fermano mentre un'altra vasca sullo stesso schermo continua ad aggiornarsi, parti da qui.

1. Apri **Impostazioni → [quella vasca] → Cora Max principale**. Controlla che sia assegnato un dispositivo e che sia online.
2. Se un altro Cora Max di questa vasca mostra **Cora principale offline** nella sua barra in alto, il principale ha perso la connessione. Cosa significa l'etichetta di stato è spiegato in [La schermata principale di Cora Max](/help/max-tour#what-the-status-pill-means).
3. **Impostazioni → Impostazioni Cora Max → RETE E AGGIORNAMENTI → Polling dispositivi** mostra ogni quanto questo Cora Max legge i tuoi dispositivi. Qui puoi solo vederlo. Si imposta da Cora Mobile.
4. Controlla la sezione **Stato** di **Impostazioni → Impostazioni Cora Max**. Mostra per ogni vasca lo stato del polling, l'ora dell'ultima lettura e l'ultima scrittura nel cloud, senza cambiare niente.

Se non basta, dai un'occhiata a [Risoluzione dei problemi](/help/troubleshooting).

## Gestire un Cora Max dal telefono {#managing-a-cora-max-from-your-phone}

Apri la scheda **Dispositivi** sul telefono e tocca il Cora Max. La scheda in alto mostra la variante, il firmware e l'ultimo contatto. Da lì puoi rinominarlo e, quando c'è una nuova versione, toccare **Aggiorna a v…** per installarla subito. La scheda **PIN di ripristino** si trova subito sotto.

![La pagina di un Cora Max in Cora Mobile, con Blocco bambini, Polling dispositivi, Fuso orario e Vasche assegnate](img/max-from-phone.webp "Le impostazioni di un singolo Cora Max sul telefono: Blocco bambini, Polling dispositivi e Fuso orario, poi le sue vasche.")

Queste impostazioni riguardano solo **quel singolo schermo**, come se le avessi cambiate dallo schermo a parete:

| Sezione | Impostazioni |
|---|---|
| **Schermo** | **Luminosità**, **Attenua dopo** |
| **Audio e voce** | **Suono degli avvisi** accende o spegne il suono degli avvisi su quello schermo, e **Volume degli avvisi** imposta quanto è forte. Gli avvisi compaiono comunque sullo schermo, e la cronologia degli avvisi e le notifiche push non cambiano |
| **Blocco bambini** | **Blocco bambini** blocca il touchscreen di quello schermo e gli impedisce di comandare l'attrezzatura a voce |
| **Rete e aggiornamenti** | **Polling dispositivi** (ogni quanto legge la tua attrezzatura) e **Fuso orario** (usato per l'attenuazione notturna e la fascia degli aggiornamenti) |

In **Vasche**, ogni vasca che questo Cora Max mostra ha una scheda con **Layout dashboard**, **Modifica vasca** e il suo dispositivo di polling. **Aggiungi vasca** e l'icona di rimozione cambiano quali vasche mostra, e queste modifiche valgono per tutto l'account. Puoi farle solo dal telefono. I passaggi sono in [Configurare Cora Max](/help/max-setup#changing-which-tanks-it-shows). Quale dispositivo è il Cora Max principale di una vasca si può cambiare sia dal telefono sia da Cora Max.

In **Ripristino**, **Ripristina display** riporta lo schermo alla sua schermata di associazione. Resta sul tuo Wi-Fi, quindi puoi associarlo di nuovo via Bluetooth, e i dati della vasca vengono conservati. **Rimuovi dispositivo** lo toglie dal tuo account. Le letture della vasca vengono conservate, e puoi associarlo di nuovo più avanti.
