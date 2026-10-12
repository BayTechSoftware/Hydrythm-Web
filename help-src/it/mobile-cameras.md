---
title: Telecamere e controllo dello schiumatoio
description: Aggiungi a Cora una telecamera Wyze, Tapo, Sonoff o un'altra RTSP, guardala in un riquadro o a schermo intero e fatti avvisare dal controllo dello schiumatoio prima che il bicchiere trabocchi.
section: Cora Mobile
reviewed: 2026-10-12
order: 35
group: Equipment
---

:::note Beta
**Beta.** Le telecamere sono in Beta e aperte solo agli utenti Beta. Se non sei un utente Beta, non le vedi in **Aggiungi dispositivo**. Per chiedere l'accesso Beta, contatta il [supporto](/support.html).
:::

Aggiungi una telecamera per vedere la tua vasca da Cora, sul telefono e su Cora Max. Una telecamera richiede un Cora Max nella vasca, quindi la riga **Telecamera** mostra **Richiede Cora Max** finché la vasca non ne ha uno.

## Aggiungere una telecamera

1. Vai su **Dispositivi → Aggiungi dispositivo → Telecamera**, poi **Aggiungi una telecamera**.
2. Scegli il tipo: Wyze, Tapo, Sonoff oppure **Altra telecamera (RTSP)**.
3. Segui i passaggi che Cora mostra per quel tipo. Ti dicono cosa attivare prima nell'app della telecamera.
4. Compila nome, indirizzo del flusso, nome utente, password e vasca, poi tocca **Prova la connessione**. Quando la telecamera risponde, tocca **Aggiungi telecamera**.

Mentre la aggiungi, il telefono deve essere sullo stesso Wi-Fi della telecamera. L'indirizzo deve essere sulla tua rete di casa, e nome utente e password vanno nei loro campi, non nell'indirizzo.

Le telecamere Wyze, Tapo e Sonoff sono state provate (Wyze Cam v4, Tapo C120 e Sonoff Cam S3W). Altre telecamere con RTSP possono funzionare.

| Telecamera | Da attivare prima |
|---|---|
| Wyze | Nell'app Wyze apri la telecamera, poi Impostazioni, Impostazioni avanzate, RTSP. Attiva RTSP, scegli un nome utente e una password, poi riavvia la telecamera. La telecamera deve avere il firmware 4.52.17 o più recente. |
| Tapo | Nell'app Tapo apri Impostazioni, Impostazioni avanzate, Account della telecamera e crea un nome utente e una password. Non è il tuo account TP-Link. Una telecamera Tapo può usare in contemporanea solo due tra Tapo Care, registrazione su scheda SD e streaming verso altre app. |
| Sonoff | In eWeLink attiva RTSP per la telecamera e imposta il suo account. Cora compila per te un'impostazione predefinita, **Indirizzo Sonoff**. |
| Altra telecamera (RTSP) | Attiva RTSP o ONVIF nell'app della telecamera, imposta un accesso per la telecamera e inserisci l'indirizzo del flusso che trovi nel manuale. Lascia vuoto l'accesso se la tua telecamera non ne ha uno. |

## Modificare una telecamera

Apri la telecamera e usa il suo menu: **Rinomina**, **Modifica indirizzi**, **Cambia password** o **Rimuovi telecamera**. Rimuoverla cancella anche la sua password salvata.

## Guardarla

Una telecamera può essere un riquadro della dashboard, fino a 3×2, e puoi aprirla a **Schermo intero** e **Ruota**.

A casa, con il telefono sul Wi-Fi della telecamera, Cora riproduce il **Video dal vivo** direttamente dalla telecamera. Fuori casa, o quando scegli **Istantanee**, il tuo Cora Max prende immagini fisse dalla telecamera e Cora le mostra come quasi dal vivo, aggiornate ogni pochi secondi. Se Cora Max non sta mandando immagini, il riquadro lo dice.

## Controllo dello schiumatoio

:::note Beta
**Beta.** Il controllo dello schiumatoio è in Beta e aperto solo agli utenti Beta. Richiede anche un piano a pagamento: **il controllo dello schiumatoio fa parte dei piani a pagamento.** Per chiedere l'accesso Beta, contatta il [supporto](/support.html).
:::

Il controllo dello schiumatoio guarda il bicchiere di raccolta dello schiumatoio con una telecamera e ti avvisa prima che trabocchi. Si trova nella pagina della telecamera, nella scheda **Controllo schiumatoio**.

1. Punta la telecamera sul bicchiere e attiva **Controlla il bicchiere**.
2. Tocca **Segna il bicchiere**. Trascina il riquadro sul bicchiere e tira gli angoli per adattarlo: il bordo inferiore sul fondo del bicchiere, il bordo superiore appena sotto il bordo, dove il bicchiere è pieno.
3. Svuota il bicchiere e tocca **Il bicchiere è vuoto ora**. Cora scatta un'immagine del bicchiere vuoto da usare come confronto. Ci vogliono circa 10 secondi. Se sposti la telecamera o il riquadro, rifallo.
4. Imposta il livello di riempimento che deve avvisarti con **Avviso al …%**. La scheda lo mostra in percentuale.

Cora Max controlla il bicchiere ogni pochi minuti. La scheda mostra l'ultima lettura e quanto tempo fa è stata fatta. **Controlla ora** chiede subito un controllo e richiede circa 10 secondi. **Ultime 24 ore** mostra come si è riempito il bicchiere nel corso della giornata.

Se l'immagine è difficile da leggere, la scheda lo dice, per esempio **Luce troppo forte dietro il bicchiere**.

### Consigli per la videocamera

**Consigli per la videocamera** sulla scheda ti dà gli stessi consigli che trovi qui.

- Imposta la visione notturna della telecamera su On (sempre a infrarossi), non su Auto, così ogni immagine è uguale di giorno e di notte.
- Imposta il faretto della telecamera su Manuale e lascialo spento. Le bolle e l'acqua nella sump contano come movimento e lo accendono di continuo.
- Evita che luci forti puntino dritte verso la telecamera da dietro il bicchiere.

## Cosa succede alle immagini

A casa, il video passa direttamente dalla telecamera e non viene registrato. Fuori casa si conserva una sola immagine fissa per telecamera, e ogni nuova sostituisce la precedente. Il controllo dello schiumatoio conserva l'ultima immagine del bicchiere segnato, le letture di riempimento delle ultime 24 ore (solo numeri) e una piccola immagine del bicchiere vuoto. Vengono cancellate quando rimuovi la telecamera, la vasca o il tuo account. L'[informativa sulla privacy](/privacy-policy.html) ha tutti i dettagli.
