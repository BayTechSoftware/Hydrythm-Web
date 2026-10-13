---
title: Telecamere e Controllo schiumatoio
description: Aggiungi a Cora una telecamera Wyze, Tapo, Sonoff o un'altra telecamera RTSP, guarda la vasca in un riquadro o a schermo intero e lascia che il Controllo schiumatoio ti avvisi prima che il bicchiere dello schiumatoio trabocchi.
section: Cora Mobile
reviewed: 2026-10-13
order: 17
group: Equipment
---

:::note Beta
**Beta.** Le telecamere sono in Beta e sono disponibili solo per gli utenti Beta. Se non sei un utente Beta non le vedrai in **Aggiungi dispositivo**. Per chiedere l'accesso alla Beta, contatta l'[assistenza](/support.html). Di più in [Funzioni Beta](/help/mobile-beta).
:::

Aggiungi una telecamera per vedere la vasca da Cora, sul telefono e su Cora Max, e per lasciare che il Controllo schiumatoio tenga d'occhio il bicchiere dello schiumatoio. Parti da **Dispositivi → Aggiungi dispositivo → Telecamera**. Una telecamera richiede un Cora Max nella vasca, quindi la riga **Telecamera** mostra **Richiede Cora Max** finché la vasca non ne ha uno.

## Aggiungere una telecamera {#adding-a-camera}

1. Vai in **Dispositivi → Aggiungi dispositivo → Telecamera**, poi **Aggiungi una telecamera**.
2. Scegli il tipo: Wyze, Tapo, Sonoff o **Altra telecamera (RTSP)**.
3. Segui i passaggi che Cora mostra per quel tipo. Ti dicono cosa attivare prima nell'app della telecamera.
4. Compila nome, indirizzo del flusso, nome utente, password e vasca, poi tocca **Prova la connessione**. Quando la telecamera risponde, tocca **Aggiungi telecamera**.

Mentre la aggiungi, il telefono deve essere sullo stesso Wi-Fi della telecamera. L'indirizzo deve essere sulla tua rete di casa, e nome utente e password vanno inseriti nei loro campi, non nell'indirizzo.

Le telecamere Wyze, Tapo e Sonoff sono state provate (Wyze Cam v4, Tapo C120 e Sonoff Cam S3W). Possono funzionare anche altre telecamere che offrono RTSP.

| Telecamera | Attiva prima questo |
|---|---|
| Wyze | Nell'app Wyze, apri la telecamera, poi Impostazioni, Impostazioni avanzate, RTSP. Attiva RTSP, scegli un nome utente e una password, poi riavvia la telecamera. La telecamera deve avere il firmware 4.52.17 o più recente. |
| Tapo | Nell'app Tapo, apri Impostazioni, Impostazioni avanzate, Account della telecamera e crea un nome utente e una password. Non è il tuo account TP-Link. Una telecamera Tapo può fare contemporaneamente solo due cose tra Tapo Care, registrazione su scheda SD e streaming verso altre app. |
| Sonoff | In eWeLink, attiva RTSP per la telecamera e imposta il suo account. Cora compila per te un'impostazione predefinita **Indirizzo Sonoff**. |
| Altra telecamera (RTSP) | Attiva RTSP o ONVIF nell'app della telecamera, imposta un accesso per la telecamera e inserisci l'indirizzo del flusso indicato nel manuale. Lascia vuoto l'accesso se la telecamera non ne ha uno. |

## Modificare una telecamera {#changing-a-camera}

Apri la telecamera e usa il suo menu: **Rinomina**, **Modifica indirizzi**, **Cambia password** o **Rimuovi telecamera**. Rimuoverla elimina anche la sua password salvata.

## Guardarla {#watching-it}

![La pagina di una telecamera](img/mobile-camera.webp "La pagina della telecamera, con l'immagine in alto e la scheda Controllo schiumatoio sotto.")

Una telecamera può essere un riquadro della dashboard, fino a 3×2. Vedi [Modificare la dashboard](/help/mobile-dashboard-editing). Aprila per **Schermo intero** e **Ruota**.

A casa, con il telefono sul Wi-Fi della telecamera, Cora riproduce il **Video dal vivo** direttamente dalla telecamera. Fuori casa, o quando scegli **Istantanee**, il tuo Cora Max prende immagini fisse dalla telecamera e Cora le mostra quasi in tempo reale, aggiornate ogni pochi secondi. Se Cora Max non sta inviando immagini, il riquadro lo dice.

## Controllo schiumatoio {#skimmer-watch}

:::note Beta
**Beta.** Il Controllo schiumatoio è in Beta ed è disponibile solo per gli utenti Beta. Richiede anche un piano a pagamento. Senza, la scheda dice **Il controllo dello schiumatoio fa parte dei piani a pagamento.** e propone **Vedi i piani**. Per chiedere l'accesso alla Beta, contatta l'[assistenza](/support.html).
:::

Il Controllo schiumatoio guarda il bicchiere di raccolta dello schiumatoio attraverso una telecamera e ti avvisa prima che trabocchi. Si trova nella pagina della telecamera, nella scheda **Controllo schiumatoio**.

![Segnare il bicchiere](img/mobile-camera-mark-cup.webp "Trascina il riquadro sul bicchiere: bordo inferiore sul fondo del bicchiere, bordo superiore appena sotto l'orlo.")

1. Punta la telecamera sul bicchiere e attiva **Controlla il bicchiere**.
2. Tocca **Segna il bicchiere**. Trascina il riquadro sul bicchiere e tira gli angoli per adattarlo: il bordo inferiore sul fondo del bicchiere, il bordo superiore appena sotto l'orlo, dove il bicchiere è pieno. In seguito il pulsante dice **Sposta il riquadro del bicchiere**.
3. Svuota il bicchiere e tocca **Il bicchiere è vuoto ora**. Cora scatta un'immagine del bicchiere vuoto da usare come confronto. Ci vogliono circa 10 secondi. Se sposti la telecamera o il riquadro, rifallo.
4. Trascina il cursore **Avviso al** fino al livello di riempimento che deve avvisarti. Lascia un po' di margine, perché Cora controlla ogni 15 minuti.

![La scheda Controllo schiumatoio nella pagina di una telecamera](img/mobile-skimmer-watch.webp "Il bicchiere è vuoto ora, l'ultima lettura, le ultime 24 ore, Controlla ora e i consigli per la videocamera.")

Cora Max controlla il bicchiere ogni 15 minuti. La scheda mostra l'ultima lettura e quanto tempo fa è stata fatta, e anche il riquadro della telecamera sulla dashboard mostra il livello del bicchiere. **Controlla ora** controlla subito il bicchiere, e ci vogliono circa 10 secondi. **Ultime 24 ore** mostra come si è riempito il bicchiere nel corso della giornata.

Quando il bicchiere raggiunge il tuo livello **Avviso al**, ricevi una notifica. Viene inviata come **Guasti dell'apparecchiatura**, quindi tieni attiva quella categoria in [Notifiche](/help/mobile-notifications). Dopo che hai svuotato il bicchiere, l'avviso è pronto a scattare di nuovo.

### Se la lettura sembra sbagliata {#skimmer-watch-problems}

| La scheda dice | Cosa fare |
|---|---|
| **Luce troppo forte dietro il bicchiere** | Spegni o sposta la luce dietro il bicchiere. Vedi i consigli per la videocamera più sotto |
| **Non sicuro (bassa affidabilità)** | L'immagine era difficile da leggere. Controlla i consigli per la videocamera, poi tocca **Controlla ora** |
| **Segna prima il bicchiere** | Tocca **Segna il bicchiere** e disegna il riquadro |
| **Non calibrato: svuota il bicchiere e tocca Il bicchiere è vuoto ora** | Svuota il bicchiere, poi tocca **Il bicchiere è vuoto ora** |
| **Riquadro spostato: calibra di nuovo** | Hai spostato il riquadro. Svuota il bicchiere e tocca di nuovo **Il bicchiere è vuoto ora** |
| **Cora Max non è riuscito a ottenere un'immagine della videocamera.** | Controlla che la telecamera sia accesa e che il Cora Max della vasca sia online |
| **L'ultimo controllo non è riuscito.** | Tocca **Controlla ora**. Se continua a non riuscire, vedi [Risoluzione dei problemi](/help/troubleshooting) |
| **Nessuna lettura per ora. Cora Max controlla ogni 15 minuti.** | Aspetta il primo controllo, oppure tocca **Controlla ora** |

### Consigli per la videocamera {#camera-tips}

**Consigli per la videocamera** sulla scheda ti dà gli stessi consigli che trovi qui.

- Imposta la visione notturna della telecamera su On (sempre a infrarossi), non su Auto, così ogni immagine è uguale di giorno e di notte.
- Imposta il faretto della telecamera su Manuale e lascialo spento. Le bolle e l'acqua nella sump contano come movimento e continuano ad accenderlo.
- Evita che luci forti puntino dritte verso la telecamera da dietro il bicchiere.

### Su Cora Max {#skimmer-watch-on-cora-max}

![Riquadri delle telecamere su Cora Max, uno con il livello del bicchiere dello schiumatoio](img/max-skimmer-watch.webp "Su Cora Max, il riquadro della telecamera mostra il livello del bicchiere e quanto è vecchia la lettura.")

Su Cora Max, il riquadro della telecamera e la telecamera a schermo intero mostrano **Bicchiere** con il livello di riempimento e quanto è vecchia la lettura. L'etichetta diventa ambra quando il bicchiere è entro 10 punti dal tuo livello di avviso e rossa quando lo raggiunge. Sulla telecamera a schermo intero, il pulsante **Avviso al** apre **Avviso bicchiere dello schiumatoio**, dove puoi cambiare anche il livello. Mentre è in corso un controllo, l'immagine dal vivo può fermarsi per qualche secondo. Di più in [Controllare l'attrezzatura da Cora Max](/help/max-device-control).

## Cosa succede alle immagini {#pictures}

A casa, il video passa direttamente dalla telecamera e non viene registrato. Fuori casa si conserva una sola immagine fissa per telecamera, e ogni nuova sostituisce la precedente. Il Controllo schiumatoio conserva l'ultima immagine del bicchiere segnato, le letture di riempimento delle ultime 24 ore (solo numeri) e una piccola immagine del bicchiere vuoto. Vengono eliminate quando rimuovi la telecamera o elimini il tuo account. L'[informativa sulla privacy](/privacy-policy.html) ha tutti i dettagli.
