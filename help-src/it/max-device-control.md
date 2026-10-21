---
title: Controllare l'attrezzatura da Cora Max
description: Le pagine dispositivo su Cora Max per Neptune Apex, Trident e DŌS, Red Sea ReefBeat, Jecod e AquaWiz, marca per marca.
section: Cora Max
reviewed: 2026-10-18
order: 6
group: Equipment
twin: mobile-device-control
---

Questa pagina spiega cosa puoi vedere e fare nella pagina di ogni dispositivo su Cora Max, marca per marca. Cora Max raggiunge la stessa attrezzatura del telefono. Apri la pagina di un dispositivo dall'icona dei dispositivi nella barra in alto, da **Impostazioni → Dispositivi**, oppure toccando il riquadro di un dispositivo sulla dashboard.

![La pagina di un Apex su Cora Max con i pulsanti di alimentazione e le prese](img/max-device-control.webp "Da Feed A a Feed D e Annulla, poi le prese, disposte per uno schermo a parete.")

:::warning Questi comandi agiscono sull'attrezzatura in funzione
Non c'è anteprima e non c'è annulla. Un comando parte appena tocchi, ma inviarlo non vuol dire che sia fatto. Torna come **Confermato**, **Non confermato**, **Rifiutato** o **Nessun cambiamento**, e puoi vedere quale in [Attività](/help/max-activity).
:::

L'attrezzatura si aggiunge, si assegna e si rimuove dal telefono. Cora Max la mostra quando il tuo account ce l'ha. Vedi [Collegare la tua attrezzatura](/help/mobile-connections).

## Cosa ha una pagina {#what-has-a-page}

| Dispositivo | Mostra |
|---|---|
| **Neptune Apex** | Sonde e prese, e puoi accendere e spegnere ogni presa |
| **Trident** | Stato del test, livelli di reagente e rifiuti, e un pulsante per avviare un test |
| **DŌS**, compreso il DŌS QD | Il dosaggio, la programmazione, l'autonomia e il volume del contenitore di ogni testa (con pausa, riempimento, dosa ora e una misura di venti secondi da fare una volta) |
| **Red Sea ReefBeat** | Quello che ha l'unità: teste di dosaggio, serbatoio, giorni del rotolo, modalità della pompa, più un editor completo del piano ReefDose e le impostazioni ReefMat |
| **Jecod** | Modalità e intensità della pompa, e la sua programmazione giornaliera |
| **AquaWiz** | Nessuna pagina propria. È elencato in **Dispositivi**, e le sue letture vanno sulla dashboard |

La maggior parte delle pagine dispositivo ha una matita per rinominare il dispositivo. Il nuovo nome compare anche sul telefono. Di più in [Dispositivi e salute dei dispositivi](/help/max-devices).

## Neptune Apex {#neptune-apex}

La pagina dell'Apex elenca sonde e prese, con i cicli di alimentazione in alto. Ogni presa passa tra **Auto**, **Off** e **On**, e le prese con il lucchetto ti chiedono di confermare. Come funzionano i tre stati e la modalità alimentazione è spiegato in [Prese e comandi](/help/max-controls).

Puoi raggiungere le prese anche dal pannello **Prese e alimentazione** in fondo alla dashboard. Elenca le prese attivate per questa dashboard (o tutte, se non ne hai scelte).

Un Apex grande con più moduli mostra tutte le sue prese e sonde. Le teste DŌS non compaiono mai nell'elenco delle prese, quindi non puoi accenderne una lì e lasciarla andare. Dosa dalla pagina della testa.

### Trident {#trident}

La pagina del Trident mostra lo stato del test e i livelli di reagente e rifiuti. Da qui puoi avviare un test, e impostare un avviso di rifornimento con **Impostazioni avvisi**.

## Teste DŌS {#dos-heads}

Devi misurare una testa DŌS una volta prima che Cora la usi per dosare a mano. **Misura per dosare** fa funzionare la testa per venti secondi in un contenitore graduato, e tu inserisci quanto è uscito. Cora tiene una misura per testa e usa la più recente, qualunque Cora Max l'abbia fatta. La pagina della testa mostra dove e quando è stata misurata.

Dopo una dose manuale, una testa che avevi impostato su Off in Apex Fusion resta su Off. Qualsiasi altra testa torna su Auto.

Un DŌS non ha un sensore di livello e continua a dosare da un contenitore vuoto. Imposta un avviso di rifornimento con **Impostazioni avvisi** nella pagina del DŌS. Di più in [Avvisi della pompa dosometrica](/help/mobile-device-control#doser-alerts).

### A cosa serve una testa {#what-a-head-is-used-for}

Nel pannello delle impostazioni di una testa puoi impostarne il **tipo di uso**. Le opzioni sono **Integratore**, **Cambio d'acqua: nuova acqua salata in entrata**, **Cambio d'acqua: acqua vecchia in uscita**, **Kalkwasser**, **Reattore di calcio**, **Cibo** o **Rabbocco**, e **Altro**. Il tipo di uso cambia due cose.

- Quanto può essere grande il contenitore che segue. Ogni tipo di uso può seguire un contenitore fino a 1.000 litri. Oltre il contatore dell'Apex da 150 litri, Cora segue il volume da sé, e azzera il contatore dell'Apex ogni 100 litri.
- Se può fare una dose grande a mano. Le teste Integratore e Cibo mantengono l'attuale limite piccolo e prudente. Ogni altro tipo di uso può avere il suo limite di **Dose massima manuale**, fino a un tetto fisso di 10 litri, e il suo **Limite giornaliero per automazioni e Assistant**. Una dose manuale grande richiede anche **Dosi grandi** attivo nelle impostazioni della testa, spento di default. Attivalo solo dopo aver guardato la prima dose grande eseguita alla vasca.

Puoi collegare una coppia per il cambio d'acqua (nuova acqua salata in entrata, acqua vecchia in uscita) come **Testa abbinata** e impostare una quantità per **Avviso di squilibrio sopra**. Se i totali giornalieri delle due teste si allontanano di più di quella quantità, Cora ti avvisa. Una coppia sbilanciata di solito vuol dire che un lato non pompa come dovrebbe.

### Se una dose grande si interrompe {#if-a-large-dose-is-interrupted}

Una dose grande cambia per un po' quello che la testa sta facendo sull'Apex, poi rimette la sua programmazione normale. Se la connessione cade a metà, Cora Max mostra un banner nella pagina di quella testa: *"Una dose grande su [testa] non è terminata correttamente. Cora continua a provare a ripristinare il suo programma: controllalo in Apex Fusion."*

Controlla tu la testa in Apex Fusion, poi tocca **Ho controllato la testa in Fusion** per togliere il banner. Fallo solo dopo aver verificato che sta funzionando la programmazione della testa, non il programma di dosaggio di Cora.

Se il banner non si toglie, o continua a tornare, dai un'occhiata a [Risoluzione dei problemi](/help/troubleshooting).

## Red Sea ReefBeat {#red-sea}

Ogni unità Red Sea ha una pagina adatta a quello che fa: teste e contenitori del ReefDose, il serbatoio del ReefATO+, i giorni del rotolo del ReefMat e le velocità delle pompe ReefRun. Gli avvisi sulle scorte per le teste ReefDose, il serbatoio del ReefATO+ e il rotolo del ReefMat si impostano con **Impostazioni avvisi** nella pagina dell'unità.

Se un'unità Red Sea si ferma da sola, la sua pagina ti dice cosa non va e mette la soluzione proprio accanto. È **Riprendi**, **Elimina emergenza**, **Sensore pulito**, **Ho già caricato un nuovo rotolo**, oppure **Ripristina** per una testa di dosaggio.

Un piano ReefDose e l'avanzamento programmato, il modello, la posizione e il Nuovo rotolo del ReefMat funzionano qui come sul telefono. [Controllare la tua attrezzatura](/help/mobile-device-control) ha i dettagli.


## Jecod {#jecod}

La pagina Jecod mostra la modalità e l'intensità della pompa, e puoi cambiarle entrambe. Il suo stato è nella riga del titolo, accanto al nome della pompa. La barra in alto contiene l'interruttore, lo schema in corso e **Alimentazione** con quattro pulsanti: **5**, **10**, **15** e **30** min. Tocca un pulsante per mettere in pausa la pompa per quel tempo. Sotto la barra ci sono due schede:

- **Uguale tutto il giorno**: tocca un'impostazione per eseguirla tutto il giorno.
- **Programmazione**: il grafico della giornata e l'elenco dei piani, con **ora** su quello attuale. **Modifica** apre l'editor e il menu ⋮ contiene **Copia programmazione su…**, **Salva programmazione come…** e **Programmazioni salvate…**.

La scheda in funzione ha un contorno e un'etichetta **In funzione**. Una pompa Jecod non ha il pulsante **Termina alimentazione**. Ogni pompa Jecod che può mettersi in pausa per l'alimentazione mostra i pulsanti **5**, **10**, **15** e **30** min. Su una Jecod Pro il riquadro Alimentazione tra gli schemi d'onda fa lo stesso, per 10 minuti. Tramite un Cora Max lontano dalla vasca, una pompa Jecod alimenta solo per 10 minuti. Una pompa che non può alimentare in questo momento mostra il motivo in una breve riga sotto i pulsanti, e una pressione lunga mostra la frase completa. Un'alimentazione avviata dal telefono viene conclusa anche dal Cora Max: allo scadere del tempo la pompa torna al suo programma.

Puoi scrivere le programmazioni giornaliere delle pompe Jecod sullo schermo a parete oltre che sul telefono. L'editor è lo stesso, con un grafico della giornata, un elenco di fasce e una fila di azioni. Di più in [Programmare l'attrezzatura](/help/mobile-schedules).

## AquaWiz {#aquawiz}

Un controller KH AquaWiz non ha una pagina propria su Cora Max. È elencato in **Dispositivi**, dove puoi rinominarlo, e le sue letture compaiono sulla dashboard come qualsiasi altra fonte. Configuralo e gestiscilo dal telefono, vedi [Collegare la tua attrezzatura](/help/mobile-connections).

### Lettura oraria da Cora Max {#aquawiz-hourly}

AquaWiz lascia che Cora legga il suo cloud solo ogni 12 ore. Per tenere aggiornata l'alcalinità, il Cora Max principale della vasca legge anche direttamente il controller, una volta all'ora, dieci minuti prima dell'ora piena:

- Si collega per qualche secondo al Wi-Fi del controller, legge l'ultimo risultato e torna subito al tuo Wi-Fi di casa. Il Cora Max resta offline circa 4 secondi.
- La password del tuo Wi-Fi di casa non viene mai salvata né inviata da nessuna parte per questo.
- Lo fa solo il Cora Max principale della vasca. Un secondo Cora Max sulla stessa vasca no.
- Aspetta mentre il Cora Max sta parlando con te, si aggiorna, si associa o cambia Wi-Fi, e riprova l'ora dopo.
- Il controller deve essere nel raggio Wi-Fi del Cora Max e il suo firmware deve offrire l'accesso locale. Se due letture di fila falliscono, il Cora Max smette di provare per il resto della giornata e la lettura dal cloud ogni 12 ore continua.

Una lettura da Cora Max mostra **Ogni ora dal tuo Cora Max** sulla scheda AquaWiz del telefono. Porta anche gli avvisi sul livello del water box descritti in [Avvisi](/help/mobile-alerts#equipment-faults). Gli avvisi di pompa e sonda pH non richiedono un Cora Max.


## Se il Bluetooth smette di funzionare {#bluetooth-stopped}

Cora Max legge luci, pompe e sensori via Bluetooth. Se il suo Bluetooth si ferma e solo un riavvio lo riporta, compare una scheda sullo schermo: **Il Bluetooth ha smesso di funzionare**, con **Riavvia ora** e **Più tardi**. I passaggi sono in [Cora Max dice "Il Bluetooth ha smesso di funzionare"](/help/troubleshooting#bluetooth-stopped-working).

## Materiali di consumo {#consumables}

Le soglie di rifornimento (reagente, contenitori, serbatoi) si impostano qui nella pagina del dispositivo, come sul telefono. Di più in [Materiali di consumo](/help/mobile-consumables).

## Registrare e calcolare alla vasca {#logging-and-calculating-at-the-tank}

Due cose sono spesso più comode sullo schermo a parete che sul telefono.

- **Registra parametri** ti fa scrivere i risultati dei test con la tastiera sullo schermo. È nel menu della vasca.
- **Calcolatore dose** calcola una correzione dal volume della vasca e dalle concentrazioni dei tuoi prodotti. Aprilo dalla pagina di un parametro. Usa lo stesso volume e le stesse concentrazioni del telefono, quindi una dose calcolata qui coincide con una calcolata lì. Di più in [Dosaggio](/help/mobile-dosing).

## Su un secondo Cora Max {#on-a-second-cora-max}

Quando più di un Cora Max mostra una vasca, uno di loro legge l'attrezzatura di quella vasca. Le pagine dispositivo lo chiamano il Cora Max nella vasca. Gli altri possono comunque aprire le pagine dispositivo, e un'etichetta di stato **Cloud** vuol dire che sei su uno di loro. Mostrano quello che il Cora Max nella vasca ha letto l'ultima volta e quanto tempo fa. Ogni comando passa da Cora Cloud al Cora Max nella vasca, che lo esegue.

Alcune cose funzionano solo sul Cora Max nella vasca.

- **Misura per dosare** e **Rimisura** compaiono solo lì. Una volta misurata una testa, **Dosa ora** funziona da qualsiasi Cora Max.
- Puoi cambiare una programmazione Jecod da un altro Cora Max solo se il Cora Max nella vasca ha letto la pompa nell'ultima ora, e mai per una pompa che comunica solo via Bluetooth. Un solo **Applica alla pompa** da lì invia al massimo 12 modifiche, quindi invia una modifica più grande in più parti.

## Cosa è stato cambiato, e da cosa {#what-was-changed-and-by-what}

Ogni azione viene registrata insieme a cosa l'ha causata. Di più in [Attività su Cora Max](/help/max-activity).
