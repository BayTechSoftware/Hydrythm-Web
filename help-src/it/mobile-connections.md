---
title: Collegare il tuo equipaggiamento
description: Come collegare a Cora l'equipaggiamento Neptune Apex, Red Sea ReefBeat, Jecod e AquaWiz.
section: Cora Mobile
reviewed: 2026-09-17
order: 10
group: Equipment
---

Cora funziona con l'equipaggiamento che già possiedi. Questa pagina descrive cosa è supportato e cosa serve a ogni collegamento.

Ogni marca si collega nel modo che le si adatta meglio, quindi parti dal punto di ingresso per il tuo equipaggiamento:

| Marca | Parti da |
|---|---|
| Neptune Apex | La vasca; il suo profilo contiene il collegamento Apex |
| Red Sea ReefBeat | La vasca |
| Jecod / Jebao | **Dispositivi → Trova una pompa sulla tua rete**, oppure Bluetooth |
| AquaWiz | **Dispositivi → Aggiungi AquaWiz** |
| Maxspect *(beta)* | **Dispositivi → Trova una pompa sulla tua rete** |
| Cora Max | **Dispositivi → Aggiungi dispositivo** |

## Neptune Apex

Cora legge il tuo Apex sulla tua rete locale: sonde, prese e qualsiasi modulo di espansione che hai montato.

**Ti servirà:** l'indirizzo del tuo Apex sulla tua rete, e il suo accesso.

**Cosa ottieni:** ogni sonda riportata dal tuo Apex appare come una fonte che puoi metter su una dashboard. Le prese appaiono come controlli. I moduli di espansione montati ottengono i propri riquadri dispositivo.

:::note Il tuo Apex mantiene la propria programmazione
Cora legge il tuo Apex, lo mostra insieme a tutto il resto, e può commutare le prese quando lo chiedi. La tua stessa programmazione continua a funzionare esattamente come l'hai configurata.
:::

## Red Sea ReefBeat

Cora parla con l'equipaggiamento ReefBeat sulla tua rete locale. Le unità supportate sono **ReefDose**, **ReefATO+**, **ReefMat** e **ReefRun**.

**Ti servirà:** l'equipaggiamento già configurato in ReefBeat e sulla stessa rete del tuo telefono quando lo aggiungi.

**Cosa ottieni:** una pagina del dispositivo per unità, più le letture di ogni unità come fonti. ReefDose riporta le sue teste e i suoi contenitori; ReefATO+ riporta il suo serbatoio e i suoi rabbocchi; ReefMat riporta i giorni rimanenti; ReefRun riporta lo stato della pompa.

## Jecod / Jebao

Cora si collega alle pompe Jecod, e può leggerle e controllarle. Le unità Jecod raggiungono Cora in uno di due modi, e quale usa la tua decide cosa è possibile.

![Trovare una pompa](img/mobile-connections.webp "La scansione spiega cosa le serve e perché una pompa può non apparire alla prima passata.")

**Sulla tua rete.** Usa **Trova una pompa sulla tua rete**; trova le unità che si annunciano da sole, così non c'è nessun indirizzo da inserire. Una pompa di rete può essere letta e guidata ogni volta che è accesa **e raggiungibile**: o il tuo telefono è sulla stessa rete, oppure un Cora Max su quella rete fa da tramite per tuo conto. Lontano da casa senza un Cora Max sul posto, una pompa solo di rete è visibile ma non controllabile.

:::note Una pompa spesso manca la prima passata
Le pompe rispondono a una scansione e mancano la successiva. Se la tua non è elencata, scansiona di nuovo invece di supporre che sia irraggiungibile.
:::

Se una ricerca non trova nulla, il risultato mostra gli indirizzi che ha esaminato sul Wi-Fi. Se la tua pompa ha un indirizzo diverso nell'app Jebao, il tuo telefono è su un'altra rete. Una rete ospiti o IoT, o una banda solo a 5 GHz, non vedrà queste pompe. Su iPhone, Cora ha bisogno anche dell'accesso alla Rete locale per vedere le pompe sul tuo Wi-Fi. Se è disattivato, l'elenco resta vuoto e non appare alcun errore, quindi il risultato lo spiega e offre **Apri Impostazioni** per riattivarlo. **Impostazioni → Accesso dispositivi** apre lo stesso posto in qualsiasi momento; vedi [Impostazioni](/help/mobile-settings).

**Via Bluetooth.** Alcune pompe sono raggiungibili solo da un telefono nelle vicinanze. La pagina della pompa lo indica, e mostra le ultime impostazioni che è riuscita a leggere insieme a quanto sono vecchie.

Cora ha bisogno del permesso Bluetooth per questo. Concedilo prima di aggiungere una pompa Bluetooth: senza permesso la pompa non può essere scoperta affatto, non semplicemente impiegare più tempo per apparire.

**Cosa ottieni:** stato in tempo reale, modalità e intensità, pausa per l'alimentazione, e un programma giornaliero. Vedi [Pianificare l'equipaggiamento](/help/mobile-schedules).

:::warning Una pompa Bluetooth è raggiungibile solo quando sei vicino ad essa
La sua pagina mostra le ultime impostazioni che Cora ha letto e da quanto tempo. Cambiare qualsiasi cosa, incluso avviare una pausa per l'alimentazione, richiede la pompa a portata. Stai vicino ad essa e riapri la pagina.
:::

## Controller KH AquaWiz

Cora legge l'alcalinità da un controller KH AquaWiz tramite il tuo account AquaWiz.

**Ti servirà:** il tuo nome utente e la tua password AquaWiz. Cora accede per tuo conto e conserva l'accesso così può continuare a leggere.

**Cosa ottieni:** l'alcalinità come fonte, aggiornata tanto spesso quanto il tuo controller titola. Il pH è disponibile come opzione se la tua unità lo riporta.

:::warning Un solo accesso, condiviso
AquaWiz rilascia un solo accesso per account, quindi quello che Cora conserva è lo stesso che usa la loro stessa app. Cambiare la tua password AquaWiz disconnetterà Cora; riconnettilo in seguito dalla riga del dispositivo. Per revocare completamente l'accesso di Cora, rimuovi il dispositivo in Cora e cambia la tua password AquaWiz.
:::

## Maxspect

:::note Il supporto Maxspect è in beta
Il supporto della gyre Maxspect è ancora in fase di test e sviluppo, quindi alcuni controlli potrebbero essere limitati, e ciò che vedi qui potrebbe cambiare tra un aggiornamento e l'altro. Se qualcosa non funziona come descritto, faccelo sapere da [Ottenere assistenza](/help/mobile-support).
:::

Cora si collega alle pompe Maxspect Gyre e può leggerle e guidarle.

**Ti servirà:** quando la aggiungi, la gyre e il tuo telefono sulla stessa rete. Usa **Dispositivi → Trova una pompa sulla tua rete**.

**Cosa ottieni:** schema d'onda e velocità per **Gyre A** e **Gyre B**, il programma della gyre da visualizzare (impostalo nell'app Maxspect), **Stato pompa**, e se è in funzione, con quando è stata letta l'ultima volta. Vedi [Controllare il tuo equipaggiamento](/help/mobile-device-control).

:::note Come Cora Mobile raggiunge una gyre
Quando un Cora Max serve la vasca, Cora Mobile lavora attraverso quel Cora Max, anche quando sei lontano da casa, e **Modifica impostazioni** parte dall'ultima lettura di quel Cora Max. Altrimenti il tuo telefono parla direttamente con la gyre e deve essere sulla rete della gyre. Aprire la pagina della gyre la legge quindi; se la pagina mostra invece una lettura memorizzata più vecchia, **Modifica impostazioni** resta nascosto finché non tocchi aggiorna.
:::

## Registrare a mano

Alcuni parametri provengono da un kit di test invece che dall'equipaggiamento. Per inserire un risultato, scorri fino in fondo alla dashboard e tocca **Registra parametri**.

Le letture registrate a mano sono di prima classe: appaiono sui widget, portano la propria fonte ed età, alimentano Reef Buddy, e sono ciò con cui Cora confronta le tue sonde quando ti dice che due fonti non sono d'accordo.

## Se un collegamento smette di funzionare

La riga del dispositivo ti dice di che tipo di problema si tratta. Vedi la tabella in **[Aggiungere, modificare e rimuovere dispositivi](/help/mobile-devices)**, e **[Risoluzione dei problemi](/help/troubleshooting)** per qualsiasi cosa che non copre.
