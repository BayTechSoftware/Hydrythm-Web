---
title: Controllare l'equipaggiamento da Cora Max
description: Pagine dei dispositivi sullo schermo grande: sonde, prese, teste di dosaggio, tester e pompe.
section: Cora Max
reviewed: 2026-09-27
order: 6
group: Equipment
---

Cora Max raggiunge lo stesso equipaggiamento del tuo telefono, con una pagina per ogni dispositivo. Apri queste pagine da **Impostazioni → Dispositivi**, oppure toccando un riquadro dispositivo sulla dashboard.

![Una pagina Apex su Cora Max](img/max-device-control.webp "Cicli di alimentazione e ogni presa, disposti per uno schermo a parete.")

:::warning Questi controlli agiscono su equipaggiamento reale
Non c'è anteprima né annullamento. Un comando parte nel momento in cui tocchi, ma *inviato* non è *fatto*: torna **Confermato**, **Non confermato**, **Rifiutato** o **Nessun cambiamento**, e [Attività](/help/max-activity) è dove vedi quale è stato.
:::

## Cosa ha una pagina

| Dispositivo | Mostra |
|---|---|
| **Neptune Apex** | Sonde e prese, con ogni presa commutabile |
| **Trident** | Stato del test, livelli di reagente e reflui, e la possibilità di avviare un test |
| **DŌS**, incluso il DŌS QD | Il dosaggio di ogni testa, il programma, l'autonomia e il volume del contenitore (con sospendi, riempi, dosa ora e una misurazione unica di venti secondi) |
| **Red Sea ReefBeat** | Qualunque cosa sia l'unità: teste di dosaggio, serbatoio, giorni del rullo, modalità pompa |
| **Jecod** | Modalità e intensità della pompa, e il suo programma giornaliero |
| **Maxspect** *(beta)* | Modalità e velocità per **Gyre A** e **Gyre B**, **Stato pompa** (conto alla rovescia per la pulizia, corrente della testa A, teste montate, firmware), e il suo programma, di sola visualizzazione |

Se un'unità Red Sea si ferma da sola, la sua pagina dice cosa non va e mette la soluzione accanto: **Riprendi**, **Elimina emergenza**, **Sensore pulito**, **Ho già caricato un nuovo rotolo**, oppure **Ripristina** per una testa di dosaggio.

## Teste DŌS

Una testa DŌS deve essere misurata una volta prima che Cora la dosi a mano. **Misura per dosare** fa funzionare la testa per venti secondi in un contenitore graduato, e tu inserisci quanto è uscito. Cora conserva una misurazione per testa e usa la più recente, qualunque Cora Max l'abbia presa; la pagina della testa mostra dove e quando è stata misurata.

Dopo un dosaggio manuale, una testa che avevi impostato su Off in Apex Fusion resta Off. Ogni altra testa torna su Auto.

### A cosa serve una testa

Ogni testa può essere impostata su un **tipo di uso**, dal suo foglio di impostazioni: **Integratore**, **Cambio d'acqua: nuova acqua salata in entrata**, **Cambio d'acqua: acqua vecchia in uscita**, **Acqua di calce**, **Reattore di calcio**, **Cibo** o **Rabbocco**, oppure **Altro**. Il tipo di uso cambia due cose:

- **Quanto grande un contenitore può tracciare.** Una testa Integratore traccia fino a 20 litri; ogni altro tipo di uso può tracciare un contenitore molto più grande, fino a 500 litri, così una testa che esegue un cambio d'acqua o un reattore di calcio non viene trattata come se fosse una piccola bottiglia di dosaggio.
- **Se può prendere un dosaggio grande a mano.** Le teste Integratore e Cibo mantengono il limite piccolo e prudente di oggi. Ogni altro tipo di uso può avere il proprio limite di **Dose massima manuale**, fino a un limite massimo di 10 litri, e il proprio **limite giornaliero per le automazioni e l'Assistant**.

Una coppia per cambio d'acqua (nuova acqua salata in entrata, acqua vecchia in uscita) può essere collegata come **Testa abbinata**, con una quantità di **Avviso di squilibrio sopra**: se i totali giornalieri delle due teste si scostano tra loro oltre quella quantità, Cora ti avvisa, poiché una coppia sbilanciata di solito significa che un lato non pompa come previsto.

### Se un dosaggio grande viene interrotto

Un dosaggio grande cambia temporaneamente cosa sta facendo la testa sull'Apex, poi ripristina il suo programma normale dopo. Se la connessione si interrompe a metà, Cora Max mostra un banner sulla pagina di quella testa: *"Un dosaggio grande su [testa] non è terminato correttamente. Cora continua a provare a ripristinare il suo programma; controllalo in Apex Fusion."*

Controlla tu stesso la testa in Apex Fusion, poi tocca **Ho controllato la testa in Fusion** per chiudere il banner. Fallo solo dopo aver confermato che il programma proprio della testa, non il programma di dosaggio di Cora, è ciò che sta effettivamente funzionando.

**Se non funziona:** se il banner non si chiude, o continua a ritornare, vedi [Risoluzione dei problemi](/help/troubleshooting).

## Programmi

I programmi giornalieri delle pompe Jecod possono essere creati alla parete così come sul telefono. L'editor è lo stesso: un grafico giornaliero, un elenco di periodi, e una riga di azioni. Vedi [Pianificare l'equipaggiamento](/help/mobile-schedules).

Il programma di una gyre Maxspect *(beta)* può essere visualizzato qui ma non salvato. Impostalo nell'app Maxspect.

## Prese

Le prese sono raggiungibili anche dal cassetto **Prese e alimentazione** in fondo alla dashboard, che elenca le prese attivate per questa dashboard in un solo posto (tutte, se non ne è stata scelta nessuna). Vedi [Prese e controlli](/help/max-controls).

Le teste DŌS non appaiono mai nell'elenco delle prese, così una testa non può essere accesa lì e lasciata in funzione; dosa dalla sua propria pagina. Un grande Apex con diversi moduli mostra tutte le sue prese e sonde.

## Materiali di consumo

Le soglie di rifornimento (reagente, contenitori, serbatoi) si impostano dalla pagina propria del dispositivo qui, esattamente come sul telefono. Vedi [Materiali di consumo](/help/mobile-consumables).

## Registrare e calcolare alla vasca

Due cose sono spesso più comode alla parete che sul telefono:

- **Registra parametri**: inserisci i risultati del test sulla tastiera a schermo, dal menu della vasca
- **Calcolatore dose**: calcola una correzione usando il volume della vasca e le concentrazioni dei tuoi prodotti, dalla pagina di un parametro. Usa lo stesso volume e le stesse concentrazioni dei prodotti del telefono, così un dosaggio calcolato qui corrisponde a uno calcolato lì. Vedi [Dosaggio](/help/mobile-dosing).

## Su un secondo Cora Max

Quando più di un Cora Max mostra una vasca, uno di essi legge l'equipaggiamento di quella vasca; le pagine dei dispositivi lo chiamano il Cora Max alla vasca. Gli altri aprono comunque le pagine dei dispositivi (una pillola di stato che mostra **Cloud** significa che questo schermo è uno di essi). Mostrano cosa ha letto l'ultima volta il Cora Max alla vasca, e da quanto tempo, e passano ogni comando tramite Cora Cloud a quel Cora Max per eseguirlo.

Alcune cose restano con il Cora Max alla vasca:

- **Misura per dosare** e **Rimisura** appaiono solo lì. Una volta che una testa è misurata, **Dosa ora** funziona da qualsiasi Cora Max.
- Un programma Jecod può essere cambiato da un altro Cora Max solo se il Cora Max alla vasca ha letto la pompa nell'ultima ora, e mai per una pompa che parla solo via Bluetooth. Un solo **Applica alla pompa** da lì invia al massimo 12 cambiamenti, quindi invia una modifica più grande in più parti.

## Cosa è stato cambiato, e da cosa

Ogni azione viene registrata con la sua causa. Vedi [Attività e cronologia](/help/mobile-activity).
