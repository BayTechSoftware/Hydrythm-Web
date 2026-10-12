---
title: Aggiungere, modificare e rimuovere dispositivi
description: Come aggiungere attrezzatura a Cora, assegnarla a una vasca e rimuoverla nel modo giusto, tutto da un unico posto.
section: Cora Mobile
reviewed: 2026-10-12
order: 9
group: Equipment
---

Aggiungi, modifica, assegna e rimuovi ogni dispositivo dalla scheda **Dispositivi**, divisa per marca. Ogni gruppo si può chiudere, così l'elenco resta leggibile anche con una stanza piena di attrezzatura.

![La scheda Dispositivi](img/mobile-devices.webp "L'attrezzatura è raggruppata per marca. Ogni gruppo si può chiudere.")

## Aggiungere attrezzatura

Tocca **Aggiungi dispositivo**, poi scegli la marca: **Cora**, **Neptune Apex**, **Red Sea**, **Jecod** oppure **AquaWiz**. Gli utenti Beta vedono anche **Maxspect**, **GHL**, **HYDROS**, **Focustronic**, **EcoTech**, **Inkbird** e **Telecamera**, ognuno con un'etichetta **Beta**. Ognuna apre esattamente quello che le serve per trovare la tua attrezzatura: una ricerca in rete, un indirizzo IP, un accesso o una chiave dispositivo. [Collegare la tua attrezzatura](/help/mobile-connections) spiega cosa serve per ogni marca.

:::note Beta
**Beta.** Le integrazioni Beta sono aperte solo agli utenti Beta. Se non sei un utente Beta, non le vedi in **Aggiungi dispositivo**. Per chiedere l'accesso Beta, contatta il [supporto](/support.html). Trovi di più in [Funzioni Beta](/help/mobile-beta).
:::

Una riga che richiede un Cora Max nella vasca (Maxspect, GHL, EcoTech, Inkbird e Telecamera) è disattivata e dice **Richiede Cora Max** finché la vasca non ne ha uno.

**Cora** è come associ un nuovo Cora Max. Trova le unità già sul tuo Wi-Fi, o quelle vicine via Bluetooth. Se la ricerca non lo trova, in questa schermata c'è anche **Inserisci l'indirizzo IP manualmente**.

Quando aggiungi un riscaldatore, una pompa o uno schiumatoio, marca e modello si **completano da soli**. Inizia a scrivere e Cora ti suggerisce le marche da un lungo elenco verificato. Se la tua non c'è, scrivila lo stesso: Cora salva quello che scrivi.

:::note Cora e il telefono devono essere sulla stessa rete
Quando aggiungi un'attrezzatura trovata in rete locale, deve essere sulla stessa rete del telefono. **Anche dopo la configurazione si raggiunge solo da quella rete** (o via Bluetooth, per le unità che lo usano), a meno che un dispositivo Cora sul posto non la raggiunga per te.

Quindi un'attrezzatura che a casa legge bene può mostrare valori più vecchi quando sei fuori, a meno che sul posto non ci sia un Cora Max che la legge. Non è un guasto: dipende da dove si può raggiungere l'attrezzatura.
:::

## La pagina di un dispositivo

Apri un dispositivo qualsiasi dall'elenco. Prima trovi i suoi comandi, poi tre sezioni che funzionano allo stesso modo per ogni marca.

- **Acquari** mostra a quale vasca (o vasche) è assegnato. Tocca **Modifica** per riassegnarlo.
- **Connessione** è dove modifichi il suo indirizzo IP, l'accesso o la chiave dispositivo.
- **Rimuovi dispositivo**, in fondo.

Cora Max, Neptune Apex e GHL possono servire più di una vasca, quindi il loro selettore di vasca è un elenco a scelta multipla. Cora Max si può assegnare fino a quattro vasche. Vedi [Più di un dispositivo Cora](/help/mobile-multi-device). Tutto il resto, incluso HYDROS, serve una vasca alla volta: sceglierne una diversa sposta lì il dispositivo e lo toglie da quella vecchia.

:::warning Assegna la vasca prima di fidarti delle letture
Un dispositivo senza vasca continua a mandare dati, ma i numeri non finiscono da nessuna parte. Se un dispositivo appena aggiunto non compare su nessuna dashboard, controlla prima questo.
:::

## Rinominare

Apri il dispositivo e tocca la matita accanto al nome. Usa il nome con cui lo chiami tutti i giorni: "Risalita", "Gyre sinistra", "Riscaldatore sump". Il nome compare sui widget, negli avvisi e in tutto quello che chiedi a Cora, quindi un nome che per te ha senso rende tutto più chiaro.

I nomi possono avere fino a 40 caratteri. Se due dispositivi dello stesso tipo non hanno un nome, Cora li distingue con un breve codice dopo il nome. Cora non usa mai un numero di serie come nome.

Il nuovo nome vale solo in Cora. Nell'app del produttore il nome resta quello di prima.

## Controllare se un dispositivo funziona

Ogni dispositivo è una riga nella scheda Dispositivi, con la sua icona, il nome, il modello e la vasca. Il pallino sulla riga ne mostra lo stato.

| Pallino | Cosa significa |
|---|---|
| Grigio | Cora non lo sa ancora |
| Verde | Funziona normalmente |
| Arancione | Un avviso o un guasto |
| Rosso | Offline |

Le letture, le modalità, lo scollegamento e l'indirizzo IP sono nella pagina dei dettagli del dispositivo, che si apre con una sezione **Stato**. Quello che vuoi vedere è un aggiornamento recente e nessun avviso.

| Cosa vedi | Cosa significa |
|---|---|
| Un aggiornamento recente | Funziona normalmente |
| "Aggiornato 3 h fa" su un dispositivo che riporta solo ogni poche ore | Va bene |
| "Impossibile raggiungere…" | C'è un problema di rete o il dispositivo è spento |
| "…ha rifiutato l'accesso" | L'account del produttore va ricollegato. Apri il dispositivo e accedi di nuovo |
| "In attesa di Cora Max" | Un controller GHL appena aggiunto: compare una volta che un Cora Max sulla sua rete l'ha letto |
| Niente | Non ha mai mandato dati. Controlla la vasca assegnata e il collegamento |

## Rimuovere un dispositivo

Apri il dispositivo e tocca **Rimuovi dispositivo**. Cora ti chiede di confermare: *"{name} verrà rimosso da Cora. Il dispositivo stesso non viene ripristinato né modificato."*

**Le letture restano.** Dopo la rimozione Cora non raccoglie più nuovi dati da quel dispositivo, ma lo storico già raccolto resta nella vasca e i widget collegati mantengono le letture passate.

Perdi il collegamento in tempo reale e, se il dispositivo passava da un account del produttore, anche l'accesso salvato. Per aggiungerlo di nuovo dovrai accedere un'altra volta.

:::tip Zittisci un dispositivo troppo insistente senza rimuoverlo
Se un dispositivo funziona bene ma ti avvisa troppo spesso, cambia le soglie o le impostazioni delle notifiche, come spiegato in **[Avvisi e soglie](/help/mobile-alerts)**. Collegamento e dati restano, e le notifiche inutili finiscono.
:::
