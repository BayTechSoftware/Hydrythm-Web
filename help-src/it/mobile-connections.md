---
title: Collegare la tua attrezzatura
description: Come collegare a Cora un'unità Neptune Apex, Red Sea ReefBeat, Jecod o AquaWiz.
section: Cora Mobile
reviewed: 2026-10-17
order: 12
group: Equipment
---

Questa pagina mostra come collegare a Cora ogni marca di attrezzatura e cosa serve a ogni collegamento. Iniziano tutti allo stesso modo: **Dispositivi → Aggiungi dispositivo**, poi scegli la marca.

![L'elenco delle marche in Aggiungi dispositivo](img/mobile-add-device-brands.webp "L'elenco delle marche.")


| Marca | Apre | Senza un Cora Max |
|---|---|---|
| Cora | Una ricerca di un nuovo Cora Max, via Wi-Fi o Bluetooth | |
| Neptune Apex | Una ricerca in rete o il suo indirizzo IP, poi quali vasche serve | Solo locale |
| Red Sea | Una ricerca sulla tua rete, poi a quale vasca appartiene ogni unità | Solo locale |
| Jecod / Jebao | Una ricerca sulla tua rete, oppure Bluetooth | Solo locale |
| AquaWiz | Il tuo accesso AquaWiz | Funziona |

## Senza un Cora Max: solo locale {#local-only}

L'attrezzatura Neptune Apex, Red Sea e Jecod sta sulla tua rete di casa (o in Bluetooth). Se non hai un Cora Max (o non ce n'è uno sulla vasca a cui stai aggiungendo), la schermata di aggiunta di queste marche dice *Senza Cora Max, questa integrazione funziona solo localmente nell'app Mobile.* Significa che:

- Il telefono legge e comanda l'attrezzatura mentre Cora Mobile è aperta sulla stessa rete, o a portata Bluetooth.
- Lontano da casa vedi le ultime letture che il telefono ha salvato, e non puoi comandarla.

Un Cora Max nella vasca legge questa attrezzatura giorno e notte e le passa i tuoi comandi quando sei via. AquaWiz si raggiunge tramite il servizio del produttore, quindi funziona ovunque senza un Cora Max. Di più in [Più di un dispositivo Cora](/help/mobile-multi-device).

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

Cora comunica con l'attrezzatura ReefBeat sulla tua rete locale. Supporta **ReefDose**, **ReefATO+**, **ReefMat** e **ReefRun**.

1. Configura prima l'unità nell'app ReefBeat di Red Sea, e controlla che sia sulla stessa rete del telefono.
2. Vai in **Dispositivi → Aggiungi dispositivo → Red Sea**. Cora cerca sulla tua rete.
3. Scegli a quale vasca appartiene ogni unità.

Un'unità Red Sea serve una sola vasca. Sceglierne una diversa la sposta lì.

Ogni unità ha la sua pagina dispositivo, e le sue letture diventano fonti. ReefDose riporta le sue teste e i contenitori, ReefATO+ il serbatoio e i rabbocchi, ReefMat i giorni che gli restano e ReefRun lo stato della pompa. Cosa ti permette di fare ogni pagina è spiegato in [Controllare la tua attrezzatura](/help/mobile-device-control#red-sea).

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

Con entrambi i collegamenti hai stato in tempo reale, modalità e intensità, una pausa per l'alimentazione e una programmazione giornaliera. Su alcune pompe, una pausa per l'alimentazione avviata dal telefono richiede che la pagina della pompa resti aperta. I dettagli sono in [Controllare la tua attrezzatura](/help/mobile-device-control#jecod), e [Programmare l'attrezzatura](/help/mobile-schedules) spiega la programmazione giornaliera.

## Controller KH AquaWiz {#aquawiz-kh-controller}

Cora legge l'alcalinità da un controller KH AquaWiz attraverso il tuo account AquaWiz, quindi funziona anche fuori casa e non richiede un Cora Max.

1. Vai in **Dispositivi → Aggiungi dispositivo → AquaWiz**.
2. Inserisci nome utente e password AquaWiz e tocca **Connetti**.
3. Scegli la vasca, controlla **Leggi anche il pH** (parte attivo per un'unità che riporta il pH) e tocca **Collega a Cora**.

Con **Resta connesso automaticamente** attivo, Cora conserva la tua password AquaWiz e rinnova da sola il collegamento. Se è spento, Cora conserva solo un token di accesso, che AquaWiz fa scadere circa ogni 30 giorni, e ti manda una notifica quando è ora di accedere di nuovo.

Ottieni l'alcalinità come fonte, e anche il pH se la tua unità lo riporta e **Leggi anche il pH** è attivo. La prima lettura arriva appena colleghi. Dopo, AquaWiz lascia che Cora legga il suo cloud in automatico solo ogni 12 ore, quindi una lettura da lì può avere anche mezza giornata. Un Cora Max nella vasca può anche leggere il controller da solo ogni ora, quando riesce a raggiungerlo. Apri la pagina del dispositivo per vedere quando è stata misurata ogni lettura e da dove viene, e tocca **Leggi ora** per averne una fresca (al massimo una ogni 15 minuti). Cosa mostra la scheda AquaWiz, e i suoi avvisi, sono in [Controllare la tua attrezzatura](/help/mobile-device-control#aquawiz).

:::warning Cora condivide il tuo accesso AquaWiz
AquaWiz dà un solo accesso per account, quindi Cora usa lo stesso dell'app AquaWiz. Se cambi la password AquaWiz, Cora si scollega. Ricollegala poi dalla riga del dispositivo. Per togliere del tutto l'accesso a Cora, rimuovi il dispositivo in Cora e cambia la password AquaWiz.
:::


## Registrare a mano {#logging-by-hand}

Alcuni parametri arrivano da un test, non dall'attrezzatura. Per inserire un risultato, scorri in fondo alla dashboard e tocca **Registra parametri**.

Le letture che registri a mano contano come tutte le altre. Compaiono sui widget con la loro fonte e la loro età, e alimentano Reef Buddy. Cora le usa anche per controllare le tue sonde quando ti dice che due fonti non concordano.

## Se un collegamento smette di funzionare {#if-a-connection-stops-working}

La riga del dispositivo ti dice che tipo di problema è. Cercalo nella tabella in [Aggiungere, modificare e rimuovere dispositivi](/help/mobile-devices#health). Per tutto quello che non copre, vedi [Risoluzione dei problemi](/help/troubleshooting).
