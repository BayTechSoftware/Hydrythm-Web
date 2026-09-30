---
title: Collegare la tua attrezzatura
description: Come collegare a Cora l'attrezzatura Neptune Apex, Red Sea ReefBeat, Jecod, AquaWiz, GHL e HYDROS.
section: Cora Mobile
reviewed: 2026-09-30
order: 10
group: Equipment
---

Cora funziona con l'attrezzatura che hai già. Qui trovi cosa è supportato e cosa serve per ogni collegamento.

Iniziano tutte allo stesso modo: **Dispositivi → Aggiungi dispositivo**, poi scegli la marca. Ognuna apre esattamente quello che le serve per trovare la tua attrezzatura.

| Marca | Apre |
|---|---|
| Cora | Una ricerca di un nuovo Cora Max, via Wi-Fi o Bluetooth |
| Neptune Apex | Il suo indirizzo sulla tua rete, l'accesso, poi a quale vasca appartiene |
| Red Sea | Una ricerca sulla tua rete, poi a quale vasca appartiene ogni unità |
| Jecod / Jebao | Una ricerca sulla tua rete, oppure Bluetooth |
| Maxspect *(beta)* | La stessa ricerca di Jecod |
| GHL *(beta)* | Il suo indirizzo, l'interfaccia e, per un mini, il suo accesso |
| HYDROS *(beta)* | Una chiave dispositivo dall'app HYDROS |
| AquaWiz | Il tuo accesso AquaWiz |

## Neptune Apex

Cora legge l'Apex sulla tua rete locale: sonde, prese e gli eventuali moduli di espansione installati.

Aggiungilo da **Dispositivi → Aggiungi dispositivo → Neptune Apex**. Ti servono il suo indirizzo sulla tua rete e i suoi dati di accesso, poi scegli a quale vasca appartiene. Un Apex può servire più di una vasca.

Ogni sonda che l'Apex riporta diventa una fonte da mettere sulla dashboard. Le prese diventano comandi. I moduli di espansione installati hanno un riquadro dispositivo tutto loro.

:::note L'Apex continua con la sua programmazione
Cora legge l'Apex, lo mostra insieme al resto e, se glielo chiedi, accende o spegne le prese. La programmazione dell'Apex continua a funzionare esattamente come l'hai impostata.
:::

## Red Sea ReefBeat

Cora comunica con l'attrezzatura ReefBeat sulla tua rete locale. Le unità supportate sono **ReefDose**, **ReefATO+**, **ReefMat**, **ReefRun** e, in beta, **ReefControl**, **ReefControl Power**, **ReefWave** e **ReefLED**.

Quando la aggiungi, l'attrezzatura deve essere già configurata in ReefBeat e sulla stessa rete del telefono. Aggiungila da **Dispositivi → Aggiungi dispositivo → Red Sea**, che cerca sulla tua rete e chiede a quale vasca appartiene ogni unità. Un'unità Red Sea serve una sola vasca: sceglierne una diversa la sposta lì.

Ogni unità ha la sua pagina dispositivo e le sue letture diventano fonti. ReefDose riporta teste e contenitori. ReefATO+ riporta serbatoio e rabbocchi. ReefMat riporta i giorni rimasti. ReefRun riporta lo stato della pompa. ReefControl riporta le sue sonde allo stesso modo. ReefWave e ReefLED *(beta)* mostrano solo la modalità, per ora, in sola lettura.

## Jecod / Jebao

Cora si collega alle pompe Jecod e può leggerle e comandarle. Aggiungine una da **Dispositivi → Aggiungi dispositivo → Jecod**. Una pompa Jecod arriva a Cora in due modi possibili, e da questo dipende cosa puoi fare.

![Trovare una pompa](img/mobile-connections.webp "La scansione spiega cosa le serve e perché una pompa può non apparire alla prima passata.")

**Sulla rete.** La ricerca trova le pompe che si annunciano da sole, quindi non devi scrivere nessun indirizzo. Una pompa di rete si può leggere e comandare quando è accesa **e raggiungibile**, cioè quando il telefono è sulla stessa rete oppure c'è un Cora Max su quella rete che fa da ponte. Se sei fuori casa e lì non c'è un Cora Max, una pompa solo di rete si vede ma non si può comandare.

:::note Spesso una pompa non risponde alla prima scansione
Le pompe rispondono a una scansione e saltano quella dopo. Se la tua non compare, ripeti la scansione prima di pensare che sia irraggiungibile.
:::

Se la ricerca non trova nulla, il risultato mostra gli indirizzi controllati sul Wi-Fi. Se nell'app Jebao la pompa ha un indirizzo diverso, il telefono è su un'altra rete. Da una rete ospiti o IoT, o da una banda solo 5 GHz, queste pompe non si vedono. Su iPhone Cora ha bisogno anche dell'accesso alla Rete locale per vedere le pompe sul tuo Wi-Fi. Se è spento, l'elenco resta vuoto senza nessun errore. Per questo il risultato lo spiega e ti offre **Apri Impostazioni** per riattivarlo. Puoi arrivare nello stesso punto quando vuoi da **Impostazioni → Accesso dispositivi**, come spiegato in [Impostazioni](/help/mobile-settings).

**Via Bluetooth.** Alcune pompe si raggiungono solo da un telefono vicino. Lo dice la pagina della pompa, che mostra anche le ultime impostazioni lette e quanto sono vecchie.

Per questo Cora ha bisogno del permesso Bluetooth. Dallo prima di aggiungere una pompa Bluetooth. Senza permesso la pompa non viene trovata proprio.

Hai lo stato in tempo reale, modalità e intensità, la pausa per l'alimentazione e un programma giornaliero. Ne parliamo in [Programmare l'attrezzatura](/help/mobile-schedules).

:::warning Una pompa Bluetooth si raggiunge solo da vicino
La sua pagina mostra le ultime impostazioni lette da Cora e quando. Per cambiare qualsiasi cosa, anche per avviare una pausa per l'alimentazione, la pompa deve essere a portata. Avvicinati e riapri la pagina.
:::

## Controller KH AquaWiz

Cora legge l'alcalinità da un controller KH AquaWiz attraverso il tuo account AquaWiz. Aggiungilo da **Dispositivi → Aggiungi dispositivo → AquaWiz**.

Ti servono nome utente e password AquaWiz. Cora accede al posto tuo e resta collegata per continuare a leggere.

L'alcalinità diventa una fonte, aggiornata ogni volta che il controller fa una titolazione. Se la tua unità lo misura, puoi aggiungere anche il pH.

La pagina del dispositivo mostra anche il tuo KH obiettivo, la forza della dose e, per un'unità con il dosaggio configurato, la dose massima oraria e quanto supplemento di alcalinità resta nel contenitore. Questi valori arrivano direttamente dalle impostazioni AquaWiz. Cambiali nell'app AquaWiz. Se la tua unità tiene sotto controllo il contenitore, Cora ti avvisa quando il supplemento sta per finire, di default a 100 mL.

:::warning Un solo accesso, in comune
AquaWiz dà un solo accesso per account. Quello che usa Cora è lo stesso della loro app. Se cambi la password AquaWiz, Cora si scollega e devi ricollegarla dalla riga del dispositivo. Per togliere del tutto l'accesso a Cora, rimuovi il dispositivo in Cora e cambia la password AquaWiz.
:::

## Maxspect

:::note Il supporto Maxspect è in beta
Il supporto per le gyre Maxspect è ancora in fase di test e sviluppo. Alcuni comandi potrebbero essere limitati e quello che vedi potrebbe cambiare da un aggiornamento all'altro. Se qualcosa non funziona come descritto, scrivici da [Ottenere assistenza](/help/mobile-support).
:::

Cora si collega alle pompe Maxspect Gyre e può leggerle e comandarle. Aggiungine una da **Dispositivi → Aggiungi dispositivo → Maxspect**, la stessa ricerca usata per Jecod.

Quando la aggiungi, gyre e telefono devono essere sulla stessa rete.

Hai schema d'onda e velocità per **Gyre A** e **Gyre B**, il programma della gyre in sola lettura (lo imposti nell'app Maxspect), **Stato pompa** e se la pompa è in funzione, con l'ora dell'ultima lettura. Altri dettagli in [Controllare la tua attrezzatura](/help/mobile-device-control).

:::note Come Cora Mobile raggiunge una gyre
Se la vasca ha un Cora Max, Cora Mobile passa da quel Cora Max, anche quando sei fuori casa, e **Modifica impostazioni** parte dall'ultima lettura del Cora Max. Altrimenti il telefono parla direttamente con la gyre e deve essere sulla sua rete. In questo caso, quando apri la pagina della gyre Cora la legge. Se la pagina mostra invece una lettura salvata più vecchia, **Modifica impostazioni** resta nascosto finché non tocchi aggiorna.
:::

## GHL ProfiLux e Mitras

:::note Il supporto GHL è in beta
Il supporto GHL è ancora in fase di test e sviluppo. Alcune letture o alcuni comandi potrebbero non funzionare ancora, e quello che vedi qui potrebbe cambiare da un aggiornamento all'altro. Se qualcosa non funziona come descritto, scrivici da [Ottenere assistenza](/help/mobile-support).
:::

Cora legge un controller GHL ProfiLux o Mitras: sonde, prese, dosatori, sensori di livello e, sui modelli Director, i risultati dei test di KH e ioni.

Aggiungilo da **Dispositivi → Aggiungi dispositivo → GHL**. Il telefono non può cercarlo, quindi inserisci tu il suo indirizzo e scegli l'interfaccia: **Official API**, **HTTP** oppure **ProfiLux mini** (che richiede anche il suo accesso). Poi scegli a quale vasca appartiene. Un controller GHL può servire più di una vasca.

Un controller GHL non parla direttamente con il telefono. Mostra **In attesa di Cora Max** finché un Cora Max sulla sua rete non l'ha letto, poi le sue letture e i suoi comandi compaiono ovunque.

L'API GHL deve essere attiva perché Cora possa raggiungere il controller. GHL la disattiva dopo ogni aggiornamento firmware, quindi è la prima cosa da controllare se non compare nulla. [Risoluzione dei problemi](/help/troubleshooting) spiega cosa fare.

## HYDROS

:::note Il supporto HYDROS è in beta
Il supporto HYDROS è ancora in fase di test e sviluppo. Alcune letture o alcuni comandi potrebbero non funzionare ancora, e quello che vedi qui potrebbe cambiare da un aggiornamento all'altro. Se qualcosa non funziona come descritto, scrivici da [Ottenere assistenza](/help/mobile-support).
:::

HYDROS è l'unica integrazione che non richiede che Cora e il controller siano sulla stessa rete. Cora lo raggiunge attraverso il cloud di HYDROS, quindi continua a funzionare anche fuori casa, e persino con Cora chiuso.

Per collegarlo, apri l'app HYDROS e crea una **chiave dispositivo** per il provider **cora-iq**. Scegli **Read** se vuoi solo le sue letture, o **Write** se vuoi anche comandarlo da Cora. Poi vai su **Dispositivi → Aggiungi dispositivo → HYDROS** e incolla la chiave.

Una volta collegato, Cora importa gli ultimi 33 giorni della sua cronologia, poi continua a leggere in avanti da lì. [Controllare la tua attrezzatura](/help/mobile-device-control) spiega cosa puoi leggere e, con una chiave di scrittura, comandare.

## Registrare a mano

Alcuni parametri arrivano da un test e non dall'attrezzatura. Per inserire un risultato, scorri in fondo alla dashboard e tocca **Registra parametri**.

Le letture inserite a mano valgono come tutte le altre. Compaiono sui widget con la loro fonte e la loro età, arrivano a Reef Buddy, e Cora le usa come riferimento per le sonde quando ti dice che due fonti non vanno d'accordo.

## Se un collegamento smette di funzionare

La riga del dispositivo ti dice che tipo di problema c'è. Trovi la tabella in **[Aggiungere, modificare e rimuovere dispositivi](/help/mobile-devices)**. Per tutto il resto c'è **[Risoluzione dei problemi](/help/troubleshooting)**.
