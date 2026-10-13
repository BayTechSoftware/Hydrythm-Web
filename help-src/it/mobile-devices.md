---
title: Aggiungere, modificare e rimuovere dispositivi
description: Aggiungi attrezzatura a Cora, assegnala a una vasca, rinominala, controlla che funzioni e rimuovila, tutto dalla scheda Dispositivi.
section: Cora Mobile
reviewed: 2026-10-13
order: 11
group: Equipment
twin: max-devices
---

La scheda **Dispositivi** è dove aggiungi, assegni, rinomini, controlli e rimuovi ogni pezzo della tua attrezzatura. I dispositivi sono raggruppati per marca, e puoi chiudere ogni gruppo.

![La scheda Dispositivi](img/mobile-devices.webp "L'attrezzatura è raggruppata per marca. Ogni gruppo si può chiudere.")

## Aggiungere attrezzatura {#adding-equipment}

1. Nella scheda **Dispositivi**, tocca **Aggiungi dispositivo**.
2. Scegli la marca: **Cora**, **Neptune Apex**, **Red Sea**, **Jecod** o **AquaWiz**. Gli utenti Beta vedono anche **Maxspect**, **GHL**, **HYDROS**, **Focustronic**, **EcoTech**, **Inkbird** e **Telecamera**, ognuno con un'etichetta **Beta**.
3. Segui i passaggi della marca. A seconda della marca si tratta di una ricerca in rete, un indirizzo IP, un accesso o una chiave dispositivo. [Collegare la tua attrezzatura](/help/mobile-connections) ha i passaggi per ogni marca.
4. Scegli la vasca a cui appartiene.

![L'elenco Aggiungi dispositivo per un utente Beta](img/mobile-add-device-beta.webp "Le marche in Beta hanno un'etichetta Beta.")

:::note Beta
**Beta.** Le integrazioni Beta sono disponibili solo per gli utenti Beta. Se non sei un utente Beta non le vedrai in **Aggiungi dispositivo**. Per chiedere l'accesso alla Beta, contatta l'[assistenza](/support.html). Di più in [Funzioni Beta](/help/mobile-beta).
:::

Una riga che richiede un Cora Max nella vasca (Maxspect, GHL, EcoTech, Inkbird e Telecamera) è disattivata e dice **Richiede Cora Max** finché la vasca non ne ha uno.

:::note Senza un Cora Max, alcune attrezzature sono solo locali
L'attrezzatura Neptune Apex, Red Sea e Jecod si raggiunge tramite la rete di casa o il Bluetooth. Senza un Cora Max, la schermata di aggiunta dice *Senza Cora Max, questa integrazione funziona solo localmente nell'app Mobile.* Il telefono la legge e la comanda solo mentre è sulla stessa rete (o a portata Bluetooth). Lontano da casa vedi le ultime letture che il telefono ha salvato e non puoi comandarla. Un Cora Max nella vasca la legge giorno e notte e le passa i tuoi comandi. Di più in [Collegare la tua attrezzatura](/help/mobile-connections#local-only).
:::

Quando aggiungi attrezzatura dalla tua rete, il telefono deve essere sulla stessa rete dell'attrezzatura.

## Associare un Cora Max {#pairing-a-cora-max}

![La schermata di aggiunta del tuo Cora in Cora Mobile, durante la ricerca dei dispositivi](img/mobile-add-device.webp "Aggiungi dispositivo, poi Cora. Cora Mobile cerca sul tuo Wi-Fi e via Bluetooth, con Inserisci l'indirizzo IP manualmente sotto.")

**Cora** è il modo per associare un nuovo Cora Max. Trova le unità già sul tuo Wi-Fi, o quelle vicine via Bluetooth. Se non trova il tuo, usa **Inserisci l'indirizzo IP manualmente** nella stessa schermata. La procedura completa è in [Configurare Cora Max](/help/max-setup).

## La pagina di un dispositivo {#a-devices-page}

Tocca un dispositivo qualsiasi nell'elenco per aprirne la pagina. Prima vengono i suoi comandi, poi sezioni che funzionano allo stesso modo per ogni marca.

- **Stato** mostra **Modello**, **Seriale**, **Firmware** e quando Cora l'ha sentito l'ultima volta (**Visto l'ultima volta**).
- **Acquari** mostra a quale vasca (o vasche) è assegnato. Tocca **Modifica** per riassegnarlo.
- **Connessione** è dove modifichi il suo indirizzo IP, l'accesso o la chiave dispositivo.
- **Rimuovi dispositivo**, in fondo.

Cora Max, Neptune Apex e GHL possono servire più di una vasca, quindi il loro selettore di vasca è un elenco a scelta multipla. Cora Max si può assegnare a un massimo di quattro. Vedi [Più di un dispositivo Cora](/help/mobile-multi-device). Tutto il resto, compreso HYDROS, serve una vasca alla volta. Sceglierne una diversa sposta lì il dispositivo e lo toglie da quella vecchia.

:::warning Assegna la vasca prima di fidarti delle letture
Un dispositivo senza vasca continua a inviare dati, ma i suoi numeri non hanno dove andare. Se un dispositivo appena aggiunto non compare su una dashboard, controlla prima questo.
:::

Cosa fanno i comandi di ogni marca è spiegato in [Controllare la tua attrezzatura](/help/mobile-device-control).

## Rinominare {#renaming}

Apri il dispositivo e tocca la matita accanto al nome. Usa il nome con cui lo chiami tutti i giorni, come "Risalita", "Gyre sinistra" o "Riscaldatore sump". Il nome compare sui widget, negli avvisi e in tutto quello che chiedi a Cora.

I nomi possono avere fino a 40 caratteri. Lascia vuoto il nome per tornare al nome originale del dispositivo. Se due dispositivi dello stesso tipo non hanno un nome, Cora li distingue con un breve codice dopo il nome. Cora non usa mai un numero di serie come nome.

Il nuovo nome vale solo in Cora. Non cambia il nome nell'app del produttore.

## Controllare se un dispositivo funziona {#health}

Ogni dispositivo è una riga nella scheda Dispositivi, con la sua icona, il nome, il modello e la vasca. Il pallino sulla riga ne mostra lo stato.

| Pallino | Cosa significa |
|---|---|
| Grigio | Cora non lo sa ancora |
| Verde | Funziona normalmente |
| Arancione | Un avviso o un guasto |
| Rosso | Offline |

Per saperne di più, apri il dispositivo. La sua sezione **Stato** mostra quando Cora l'ha sentito l'ultima volta. Quello che vuoi vedere è un orario recente e nessun avviso.

| Cosa vedi | Cosa significa |
|---|---|
| Un orario di aggiornamento recente | Funziona normalmente |
| "Aggiornato 3 h fa" su un dispositivo che riporta solo ogni poche ore | Va bene |
| "Impossibile raggiungere…" | Un problema di rete, oppure il dispositivo è spento |
| "…ha rifiutato l'accesso" | L'account del produttore va ricollegato. Apri il dispositivo e accedi di nuovo |
| "In attesa di Cora Max" | Un controller GHL o un monitor Inkbird appena aggiunto: compare quando un Cora Max l'ha letto |
| Letture più vecchie mentre sei via | Normale per Apex, Red Sea e Jecod senza un Cora Max nella vasca (vedi sopra) |
| Niente di niente | Non ha mai inviato dati. Controlla la vasca assegnata e la connessione |

Quando un dispositivo smette di inviare dati, Cora può avvisarti. I tempi sono in [Avvisi e soglie](/help/mobile-alerts). Per tutto il resto, vedi [Risoluzione dei problemi](/help/troubleshooting).

## Rimuovere un dispositivo {#removing-a-device}

Apri il dispositivo e tocca **Rimuovi dispositivo**, oppure scorri la sua riga verso sinistra nella scheda Dispositivi. Cora ti chiede di confermare: *"{name} verrà rimosso da Cora. Il dispositivo stesso non viene ripristinato né modificato."*

**Le tue letture restano.** Rimuovere un dispositivo impedisce a Cora di raccogliere nuovi dati da quel dispositivo. Lo storico già raccolto resta sulla vasca, e ogni widget che lo usava mantiene le letture passate.

Perdi il collegamento in tempo reale. Se il dispositivo si collegava tramite un account del produttore, perdi anche l'accesso salvato, quindi dovrai accedere di nuovo se lo aggiungi un'altra volta.

:::tip Zittisci un dispositivo rumoroso senza rimuoverlo
Se un dispositivo funziona bene ma avvisa troppo spesso, cambia le sue soglie o le impostazioni delle notifiche in [Avvisi e soglie](/help/mobile-alerts). Tieni il collegamento e i dati, e il rumore finisce.
:::
