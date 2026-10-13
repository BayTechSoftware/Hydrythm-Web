---
title: Collegare la tua attrezzatura
description: Come collegare a Cora un'unità Neptune Apex, Red Sea ReefBeat, Jecod o AquaWiz e, in Beta, l'attrezzatura Maxspect, GHL, HYDROS, Focustronic e Inkbird.
section: Cora Mobile
reviewed: 2026-10-13
order: 12
group: Equipment
---

Questa pagina mostra come collegare a Cora ogni marca di attrezzatura e cosa serve a ogni collegamento. Iniziano tutti allo stesso modo: **Dispositivi → Aggiungi dispositivo**, poi scegli la marca.

![L'elenco Aggiungi dispositivo per un utente Beta](img/mobile-add-device-beta.webp "L'elenco delle marche. Le marche in Beta hanno un'etichetta Beta.")

Le marche segnate *(Beta)* sono disponibili solo per gli utenti Beta. Vedi [Funzioni Beta](/help/mobile-beta).

| Marca | Apre | Senza un Cora Max |
|---|---|---|
| Cora | Una ricerca di un nuovo Cora Max, via Wi-Fi o Bluetooth | |
| Neptune Apex | Una ricerca in rete o il suo indirizzo IP, poi quali vasche serve | Solo locale |
| Red Sea | Una ricerca sulla tua rete, poi a quale vasca appartiene ogni unità | Solo locale |
| Jecod / Jebao | Una ricerca sulla tua rete, oppure Bluetooth | Solo locale |
| AquaWiz | Il tuo accesso AquaWiz | Funziona |
| Maxspect *(Beta)* | La stessa ricerca di Jecod | **Richiede Cora Max** |
| GHL *(Beta)* | Il suo indirizzo, l'interfaccia e, per un mini, il suo accesso | **Richiede Cora Max** |
| HYDROS *(Beta)* | Una chiave dispositivo dall'app HYDROS | Funziona |
| Focustronic *(Beta)* | Il tuo accesso Focustronic, poi a quale vasca appartiene ogni dispositivo | Funziona |
| EcoTech *(Beta)* | Una ricerca Bluetooth di luci Radion, pompe VorTech e dosatori Versa. Vedi [Luci, pompe e dosatori EcoTech](/help/mobile-ecotech) | **Richiede Cora Max** |
| Inkbird *(Beta)* | Una ricerca Bluetooth del tuo monitor dell'aria della stanza | **Richiede Cora Max** |
| Telecamera *(Beta)* | Wyze, Tapo, Sonoff o un'altra telecamera RTSP. Vedi [Telecamere e Controllo schiumatoio](/help/mobile-cameras) | **Richiede Cora Max** |

## Senza un Cora Max: solo locale {#local-only}

L'attrezzatura Neptune Apex, Red Sea e Jecod sta sulla tua rete di casa (o in Bluetooth). Se non hai un Cora Max (o non ce n'è uno sulla vasca a cui stai aggiungendo), la schermata di aggiunta di queste marche dice *Senza Cora Max, questa integrazione funziona solo localmente nell'app Mobile.* Significa che:

- Il telefono legge e comanda l'attrezzatura mentre Cora Mobile è aperta sulla stessa rete, o a portata Bluetooth.
- Lontano da casa vedi le ultime letture che il telefono ha salvato, e non puoi comandarla.

Un Cora Max nella vasca legge questa attrezzatura giorno e notte e le passa i tuoi comandi quando sei via. AquaWiz, HYDROS e Focustronic si raggiungono tramite il servizio del produttore, quindi funzionano ovunque senza un Cora Max. Le righe con **Richiede Cora Max** restano disattivate finché la vasca non ne ha uno. Di più in [Più di un dispositivo Cora](/help/mobile-multi-device).

## Neptune Apex {#neptune-apex}

Cora legge il tuo Apex sulla rete locale, comprese sonde, prese e gli eventuali moduli di espansione installati.

1. Vai in **Dispositivi → Aggiungi dispositivo → Neptune Apex**.
2. Tocca **Scansiona la rete per APEX** e scegli il tuo Apex, oppure scrivi il suo indirizzo in **Oppure inserisci l'IP manualmente:**.
3. Compila **Accesso Apex (solo se ne hai impostato uno sull'Apex):**. Lascia vuota la password se non ne hai impostata una.
4. Tocca **Carica parametri da APEX** e spunta quelli che vuoi in **Parametri da seguire**.
5. Imposta **Frequenza di polling**. Non lasciarla spenta: con il polling spento, nessuno legge l'Apex e le sue letture invecchiano.
6. Tocca **Continua**, spunta ogni vasca in **Quali vasche serve questo Apex?**, poi tocca **Salva**. Un Apex può servire più di una vasca.

Se la ricerca non trova niente, controlla che il telefono sia sullo stesso Wi-Fi dell'Apex, oppure inserisci tu l'indirizzo IP.

Una volta collegato, ogni sonda che l'Apex riporta diventa una fonte da mettere su una dashboard. Le prese compaiono come comandi, e ogni modulo di espansione installato ha il suo riquadro dispositivo. La programmazione del tuo Apex continua a funzionare esattamente come l'hai impostata. Cosa puoi comandare è spiegato in [Controllare la tua attrezzatura](/help/mobile-device-control#neptune-apex).

## Red Sea ReefBeat {#red-sea-reefbeat}

Cora comunica con l'attrezzatura ReefBeat sulla tua rete locale. Supporta **ReefDose**, **ReefATO+**, **ReefMat** e **ReefRun**, più **ReefControl**, **ReefControl Power**, **ReefWave** e **ReefLED**, che hanno *(Beta)* nel nome ma sono disponibili per tutti.

1. Configura prima l'unità nell'app ReefBeat di Red Sea, e controlla che sia sulla stessa rete del telefono.
2. Vai in **Dispositivi → Aggiungi dispositivo → Red Sea**. Cora cerca sulla tua rete.
3. Scegli a quale vasca appartiene ogni unità.

Un'unità Red Sea serve una sola vasca. Sceglierne una diversa la sposta lì.

Ogni unità ha la sua pagina dispositivo, e le sue letture diventano fonti. ReefDose riporta le sue teste e i contenitori, ReefATO+ il serbatoio e i rabbocchi, ReefMat i giorni che gli restano e ReefRun lo stato della pompa. ReefControl riporta le sue sonde allo stesso modo. ReefWave e ReefLED mostrano solo la modalità, per ora. Cosa ti permette di fare ogni pagina è spiegato in [Controllare la tua attrezzatura](/help/mobile-device-control#red-sea).

## Jecod / Jebao {#jecod}

Cora si collega alle pompe Jecod e può leggerle e comandarle. Aggiungine una da **Dispositivi → Aggiungi dispositivo → Jecod**. Una pompa Jecod arriva a Cora in uno di due modi, e questo decide cosa puoi farci.

![La schermata di aggiunta di una pompa in Cora Mobile, senza pompe ancora trovate](img/mobile-connections.webp "Nessuna ancora trovata: la ricerca spiega cosa le serve e perché una pompa può non comparire a un passaggio.")

**Sulla rete.** La ricerca trova le pompe che si annunciano da sole, quindi non devi scrivere un indirizzo. Puoi leggere e comandare una pompa di rete ogni volta che è accesa e raggiungibile. Cioè il telefono è sulla stessa rete, oppure un Cora Max su quella rete passa i tuoi comandi. Se sei fuori casa e sul posto non c'è un Cora Max, puoi vedere una pompa di rete ma non comandarla.

:::note Spesso una pompa non risponde alla prima ricerca
Le pompe rispondono a una ricerca e saltano quella dopo. Se la tua non compare, cerca di nuovo prima di concludere che non sia raggiungibile.
:::

Se una ricerca non trova niente, il risultato mostra gli indirizzi che ha controllato sul Wi-Fi. Se l'app Jebao mostra un indirizzo diverso per la tua pompa, il telefono è su un'altra rete. Una rete ospiti o IoT, o una banda solo 5 GHz, non vede queste pompe. Su iPhone, Cora ha anche bisogno dell'accesso alla Rete locale per vedere le pompe sul tuo Wi-Fi. Senza, l'elenco resta vuoto e non compare nessun errore, quindi il risultato lo spiega e offre **Apri Impostazioni** per riattivarlo. Puoi arrivarci anche in qualsiasi momento da **Impostazioni → Accesso dispositivi**, descritto in [Impostazioni](/help/mobile-settings).

**Via Bluetooth.** Alcune pompe si raggiungono solo da un telefono vicino. La pagina della pompa lo dice, e mostra le ultime impostazioni lette e quanto sono vecchie. Per questo Cora ha bisogno del permesso Bluetooth. Concedilo prima di aggiungere una pompa Bluetooth, altrimenti Cora non trova proprio la pompa.

:::warning Devi essere vicino a una pompa Bluetooth
La sua pagina mostra le ultime impostazioni lette da Cora e quanto tempo fa. Per cambiare qualsiasi cosa, anche per avviare una pausa per l'alimentazione, la pompa deve essere a portata. Avvicinati e riapri la pagina.
:::

Con entrambi i collegamenti hai stato in tempo reale, modalità e intensità, una pausa per l'alimentazione e un programma giornaliero. Su alcune pompe, una pausa per l'alimentazione avviata dal telefono richiede che la pagina della pompa resti aperta. I dettagli sono in [Controllare la tua attrezzatura](/help/mobile-device-control#jecod), e [Programmare l'attrezzatura](/help/mobile-schedules) spiega il programma giornaliero.

## Controller KH AquaWiz {#aquawiz-kh-controller}

Cora legge l'alcalinità da un controller KH AquaWiz attraverso il tuo account AquaWiz, quindi funziona anche fuori casa e non richiede un Cora Max.

1. Vai in **Dispositivi → Aggiungi dispositivo → AquaWiz**.
2. Inserisci nome utente e password AquaWiz e tocca **Connetti**.
3. Scegli la vasca, attiva **Leggi anche il pH** se lo vuoi, e tocca **Collega a Cora**.

Con **Resta connesso automaticamente** attivo, Cora conserva la tua password AquaWiz e rinnova da sola il collegamento. Se è spento, Cora conserva solo un token di accesso, che AquaWiz fa scadere circa ogni 30 giorni, e ti manda una notifica quando è ora di accedere di nuovo.

Ottieni l'alcalinità come fonte, aggiornata ogni volta che il controller fa una titolazione, e anche il pH se l'hai attivato e la tua unità lo riporta. Cosa mostra la scheda AquaWiz, e il suo avviso sull'integratore, sono in [Controllare la tua attrezzatura](/help/mobile-device-control#aquawiz).

:::warning Cora condivide il tuo accesso AquaWiz
AquaWiz dà un solo accesso per account, quindi Cora usa lo stesso dell'app AquaWiz. Se cambi la password AquaWiz, Cora si scollega. Ricollegala poi dalla riga del dispositivo. Per togliere del tutto l'accesso a Cora, rimuovi il dispositivo in Cora e cambia la password AquaWiz.
:::

## Maxspect {#maxspect}

:::note Beta
**Beta.** Maxspect è in Beta ed è disponibile solo per gli utenti Beta. Se non sei un utente Beta non lo vedrai in **Aggiungi dispositivo**. Per chiedere l'accesso alla Beta, contatta l'[assistenza](/support.html). Alcuni comandi potrebbero essere limitati, e quello che vedi qui potrebbe cambiare da un aggiornamento all'altro. Se qualcosa non funziona come descritto, faccelo sapere da [Segnalare un problema](/help/mobile-support).
:::

Cora si collega alle pompe Maxspect Gyre e può leggerle e comandarle. Aggiungine una da **Dispositivi → Aggiungi dispositivo → Maxspect**, la stessa ricerca usata da Jecod. Richiede un Cora Max nella vasca. Senza, la riga mostra **Richiede Cora Max**.

Quando aggiungi una gyre, deve essere sulla stessa rete del telefono. Dopo, Cora Mobile la raggiunge attraverso il Cora Max della vasca, anche quando sei via. Schema d'onda, velocità, il programma e **Stato pompa** sono in [Controllare la tua attrezzatura](/help/mobile-device-control#maxspect).

## GHL ProfiLux e Mitras {#ghl-profilux-and-mitras}

:::note Beta
**Beta.** GHL è in Beta ed è disponibile solo per gli utenti Beta. Se non sei un utente Beta non lo vedrai in **Aggiungi dispositivo**. Per chiedere l'accesso alla Beta, contatta l'[assistenza](/support.html). Alcune letture o alcuni comandi potrebbero non funzionare ancora. Se qualcosa non funziona come descritto, faccelo sapere da [Segnalare un problema](/help/mobile-support).
:::

Cora legge un controller GHL ProfiLux o Mitras: sonde, prese, dosatori, sensori di livello e, sui modelli Director, i risultati dei test di KH e ioni.

1. Vai in **Dispositivi → Aggiungi dispositivo → GHL**. Richiede un Cora Max nella vasca, e senza mostra **Richiede Cora Max**.
2. Il telefono non può cercarlo, quindi inserisci tu il suo indirizzo e scegli l'interfaccia: **API ufficiale**, **HTTP** o **ProfiLux mini** (che richiede anche il suo accesso).
3. Scegli a quale vasca appartiene. Un controller GHL può servire più di una vasca.

Un controller GHL non parla direttamente con il telefono. Mostra **In attesa di Cora Max** finché un Cora Max sulla sua rete non l'ha letto, poi le sue letture e i suoi comandi compaiono ovunque.

L'API GHL deve essere attiva perché Cora possa raggiungere il controller. GHL la disattiva dopo ogni aggiornamento del firmware, quindi controlla prima questo se non compare niente. [Risoluzione dei problemi](/help/troubleshooting) spiega cosa fare. I comandi sono in [Controllare la tua attrezzatura](/help/mobile-device-control#ghl).

## HYDROS {#hydros}

:::note Beta
**Beta.** HYDROS è in Beta ed è disponibile solo per gli utenti Beta. Se non sei un utente Beta non lo vedrai in **Aggiungi dispositivo**. Per chiedere l'accesso alla Beta, contatta l'[assistenza](/support.html). Alcune letture o alcuni comandi potrebbero non funzionare ancora. Se qualcosa non funziona come descritto, faccelo sapere da [Segnalare un problema](/help/mobile-support).
:::

HYDROS non richiede che telefono e controller siano sulla stessa rete, né un Cora Max. Cora lo raggiunge attraverso il cloud di HYDROS, quindi continua a funzionare fuori casa, e anche con Cora Mobile chiusa.

1. Nell'app HYDROS, crea una **chiave dispositivo** per il provider **cora-iq**. Scegli **Read** se vuoi solo le sue letture, o **Write** se vuoi anche comandarlo da Cora.
2. In Cora Mobile, vai in **Dispositivi → Aggiungi dispositivo → HYDROS**. La schermata si chiama **Aggiungi HYDROS (Beta)**.
3. Incolla la chiave in **Chiave del dispositivo HYDROS**, tocca **Verifica chiave**, scegli la vasca e tocca **Collega**.

Una volta collegato, Cora importa gli ultimi 33 giorni del suo storico, poi continua a leggere da lì in avanti. [Controllare la tua attrezzatura](/help/mobile-device-control#hydros) spiega cosa puoi leggere e, con una chiave di scrittura, comandare.

## Focustronic {#focustronic}

:::note Beta
**Beta.** Focustronic è in Beta ed è disponibile solo per gli utenti Beta. Se non sei un utente Beta non lo vedrai in **Aggiungi dispositivo**. Per chiedere l'accesso alla Beta, contatta l'[assistenza](/support.html).
:::

Cora legge i dispositivi Focustronic Alkatronic, Dosetronic e Mastertronic attraverso il tuo account Focustronic, quindi funziona anche fuori casa e non richiede un Cora Max.

1. Vai in **Dispositivi → Aggiungi dispositivo → Focustronic** e accedi con lo stesso account che usi nell'app Focustronic.
2. Scegli a quale vasca appartiene ogni dispositivo, poi tocca **Collega a Cora**.

**Resta connesso** permette a Cora di conservare la tua password Focustronic, cifrata, e di accedere di nuovo da sola. Se lo spegni, Cora conserva solo un accesso temporaneo e ti manda una notifica quando devi accedere di nuovo. Se Focustronic rifiuta l'accesso, apri **Aggiungi Focustronic** e accedi di nuovo.

Cosa mostra ogni dispositivo, e **Misura ora**, **Dosa ora** e **Testa ora**, sono in [Controllare la tua attrezzatura](/help/mobile-device-control#focustronic).

## Monitor dell'aria della stanza Inkbird {#inkbird-room-air-monitor}

:::note Beta
**Beta.** Inkbird è in Beta ed è disponibile solo per gli utenti Beta. Se non sei un utente Beta non lo vedrai in **Aggiungi dispositivo**. Per chiedere l'accesso alla Beta, contatta l'[assistenza](/support.html).
:::

Cora legge un monitor dell'aria della stanza Inkbird IAM-T1 o IAM-T2. Un Cora Max nella vasca lo legge via Bluetooth, e Cora non scrive mai niente sul monitor. La riga mostra **Richiede Cora Max** finché la vasca non ne ha uno.

1. Vai in **Dispositivi → Aggiungi dispositivo → Inkbird**. Cora cerca i monitor nelle vicinanze. Il Bluetooth deve essere attivo, con il permesso per Cora.
2. Scegli il tuo e tocca **Collega alla vasca**. Se non ne compare nessuno, avvicinati e tocca **Cerca di nuovo**.

La pagina del monitor mostra la sua ultima lettura. **Intervallo di campionamento** imposta ogni quanto un Cora Max lo legge. Finché un Cora Max non l'ha letto, la pagina dice **In attesa di Cora Max**. Se tace mostra **Non risponde** e Cora ti avvisa. Le letture della stanza alimentano anche [Reef Buddy](/help/mobile-reef-buddy). Per smettere, tocca **Scollega**. Cora Max smette di leggerlo e lo storico resta.

## Registrare a mano {#logging-by-hand}

Alcuni parametri arrivano da un test, non dall'attrezzatura. Per inserire un risultato, scorri in fondo alla dashboard e tocca **Registra parametri**.

Le letture che registri a mano contano come tutte le altre. Compaiono sui widget con la loro fonte e la loro età, e alimentano Reef Buddy. Cora le usa anche per controllare le tue sonde quando ti dice che due fonti non concordano.

## Se un collegamento smette di funzionare {#if-a-connection-stops-working}

La riga del dispositivo ti dice che tipo di problema è. Cercalo nella tabella in [Aggiungere, modificare e rimuovere dispositivi](/help/mobile-devices#health). Per tutto quello che non copre, vedi [Risoluzione dei problemi](/help/troubleshooting).
