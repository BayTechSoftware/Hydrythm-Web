---
title: Controllare l'equipaggiamento da Cora Max
description: Le pagine dei dispositivi sullo schermo grande: sonde, prese, teste di dosaggio, tester e pompe.
section: Cora Max
reviewed: 2026-09-30
order: 6
group: Equipment
---

Da Cora Max arrivi alla stessa attrezzatura che vedi sul telefono, con una pagina per ogni dispositivo. Le apri da **Impostazioni → Dispositivi** oppure toccando il riquadro di un dispositivo sulla dashboard.

![Una pagina Apex su Cora Max](img/max-device-control.webp "I cicli di alimentazione e tutte le prese, sistemati per uno schermo a parete.")

:::warning Questi controlli agiscono su attrezzatura vera
Non c'è anteprima e non si può annullare. Il comando parte appena tocchi, ma *inviato* non vuol dire *fatto*. Torna come **Confermato**, **Non confermato**, **Rifiutato** o **Nessun cambiamento**, e in [Attività](/help/max-activity) vedi com'è andata.
:::

## Quali dispositivi hanno una pagina

| Dispositivo | Cosa mostra |
|---|---|
| **Neptune Apex** | Sonde e prese, e ogni presa si può comandare |
| **Trident** | Stato del test, livello di reagenti e scarico, e un comando per avviare un test |
| **DŌS**, compreso il DŌS QD | Per ogni testa: dosaggio, programma, autonomia e volume del contenitore (con pausa, riempimento, dosa ora e una misura di venti secondi da fare una volta sola) |
| **Red Sea ReefBeat** | Dipende dall'unità: teste di dosaggio, serbatoio, giorni di rotolo, modalità della pompa, più un editor completo del piano ReefDose, del programma ReefRun e delle impostazioni ReefMat *(beta)* |
| **ReefControl**, **ReefControl Power**, **ReefWave**, **ReefLED** *(beta)* | Le sonde di ReefControl. Le prese di ReefControl Power come prese normali, on/off, ancora senza modalità automatica. ReefWave e ReefLED, in sola lettura |
| **Jecod** | Modalità e intensità della pompa, e il suo programma giornaliero |
| **Maxspect** *(beta)* | Modalità e velocità di **Gyre A** e **Gyre B**, **Stato pompa** (conto alla rovescia per la pulizia, corrente della testa A, teste montate, firmware) e il programma, in sola lettura |
| **GHL ProfiLux / Mitras** *(beta)* | Sonde, prese, dosatori, sensori di livello e, sui modelli Director, i risultati dei test di KH e ioni |
| **HYDROS** *(beta)* | Tutto quello che riporta la sua chiave dispositivo: ingressi, e con una chiave di scrittura anche uscite, modalità, teste di dosaggio e comandi tester |

Se un'unità Red Sea si ferma da sola, la sua pagina ti dice cosa c'è che non va e ti mette accanto il pulsante per risolvere: **Riprendi**, **Elimina emergenza**, **Sensore pulito**, **Ho già caricato un nuovo rotolo** oppure **Ripristina** per una testa di dosaggio.

Un piano ReefDose, un programma di velocità ReefRun e l'avanzamento programmato, il modello, la posizione e il Nuovo rotolo di ReefMat funzionano qui allo stesso modo che sul telefono. Trovi i dettagli in [Collegare la tua attrezzatura](/help/mobile-connections) e [Controllare la tua attrezzatura](/help/mobile-device-control).

## Teste DŌS

Prima che Cora possa dosare a mano con una testa DŌS, la testa va misurata una volta. **Misura per dosare** fa girare la testa per venti secondi dentro un contenitore graduato, e tu scrivi quanto liquido è uscito. Cora tiene una misura per ogni testa e usa la più recente, da qualunque Cora Max arrivi. Sulla pagina della testa vedi dove e quando è stata misurata.

Dopo una dose manuale, una testa che avevi messo su Off in Apex Fusion resta su Off. Tutte le altre tornano su Auto.

### A cosa serve una testa

Dal foglio delle impostazioni di ogni testa scegli il **tipo di uso**: **Integratore**, **Cambio d'acqua: nuova acqua salata in entrata**, **Cambio d'acqua: acqua vecchia in uscita**, **Acqua di calce**, **Reattore di calcio**, **Cibo**, **Rabbocco** oppure **Altro**. Il tipo di uso cambia due cose:

- **Quanto può essere grande il contenitore.** Una testa Integratore gestisce fino a 20 litri. Con tutti gli altri tipi il contenitore può essere molto più grande, fino a 500 litri. Così una testa che fa un cambio d'acqua o alimenta un reattore di calcio non viene trattata come una piccola bottiglia di integratore.
- **Se può fare una dose grande a mano.** Le teste Integratore e Cibo mantengono il limite basso e prudente di sempre. Per tutti gli altri tipi puoi impostare una **Dose massima manuale**, fino a un tetto fisso di 10 litri, e un **Limite giornaliero per automazioni e Assistant**. Una dose grande a mano richiede anche **Dosi grandi (Beta)** attivato nelle impostazioni della testa, disattivato per impostazione predefinita: attivalo solo dopo aver osservato la prima dose grande eseguita davanti all'acquario.

Per il cambio d'acqua puoi collegare due teste (nuova acqua salata in entrata, acqua vecchia in uscita) come **Testa abbinata** e impostare un valore in **Avviso di squilibrio sopra**. Se nel corso della giornata i totali delle due teste si allontanano più di quel valore, Cora ti avvisa. Di solito vuol dire che uno dei due lati non pompa come dovrebbe.

### Se una dose grande si interrompe

Durante una dose grande Cora cambia per un po' quello che la testa fa sull'Apex, poi rimette il suo programma normale. Se la connessione cade a metà, Cora Max mostra un banner sulla pagina della testa: *"Una dose grande su [testa] non è terminata correttamente. Cora continua a provare a ripristinare il suo programma: controllalo in Apex Fusion."*

Controlla tu la testa in Apex Fusion, poi tocca **Ho controllato la testa in Fusion** per chiudere il banner. Fallo solo dopo aver verificato che sta girando il programma della testa, e non il programma di dosaggio di Cora.

Se il banner non si chiude o continua a tornare, guarda la pagina [Risoluzione dei problemi](/help/troubleshooting).

## GHL ProfiLux e Mitras

:::note Il supporto GHL è in beta
Il supporto GHL è ancora in fase di test e sviluppo. Alcune letture o alcuni comandi potrebbero non funzionare ancora, e quello che vedi qui potrebbe cambiare da un aggiornamento all'altro.
:::

Collega un controller GHL da **Impostazioni → [la tua vasca] → Controller GHL (Beta)**. Inserisci il suo indirizzo IP sulla tua rete e tocca **Rileva**. Cora prova prima l'API ufficiale del controller, poi le sue altre interfacce, e ti dice quale ha trovato.

Se non risponde niente e il controller è un ProfiLux mini, Cora propone un'alternativa: inserisci il suo accesso e Cora legge le sue sonde, prese, dosatori e sensori di livello. Con **Consenti il controllo da Cora (Beta)** attivo, un mini può anche comandare le sue prese, come qualsiasi altro controller GHL. Tutto il resto, come i setpoint e la pausa alimentazione, richiede un ProfiLux 3, 4 o Mitras.

I comandi restano disattivati finché non attivi **Consenti il controllo da Cora (Beta)** sulla pagina del dispositivo. È disattivato per impostazione predefinita. Una volta attivato, una presa si può impostare su **Sempre acceso**, **Sempre spento** o **Torna ad automatico**, e un setpoint come temperatura o pH mostra il suo intervallo consentito e rifiuta un valore fuori da quell'intervallo. Entrambi i tipi di modifica vengono salvati sul controller stesso e restano lì anche se Cora perde in seguito il contatto con lui. Una modifica che sembra riguardare un riscaldatore o una pompa di risalita ti chiede due conferme.

Se il contenitore di un dosatore sta per finire, Cora ti avvisa come fa per gli altri materiali di consumo. Il valore predefinito è 20% pieno, e lo puoi cambiare dalla regola del dosatore nel [Centro avvisi](/help/mobile-alerts).

Se il controller non accetta una modifica, probabilmente la sua API GHL è disattivata. GHL la disattiva dopo ogni aggiornamento firmware: riattivala da **System → GHL API** in GHL Control Center o GHL Connect. Il resto lo trovi in [Risoluzione dei problemi](/help/troubleshooting).

## HYDROS

:::note Il supporto HYDROS è in beta
Il supporto HYDROS è ancora in fase di test e sviluppo. Alcune letture o alcuni comandi potrebbero non funzionare ancora, e quello che vedi qui potrebbe cambiare da un aggiornamento all'altro.
:::

HYDROS è l'unica integrazione che raggiunge il suo controller attraverso il cloud, quindi funziona anche quando Cora Max è su una rete diversa da quella del controller. Collegalo da **Impostazioni → [la tua vasca] → HYDROS (Beta)**.

Nell'app HYDROS crea una chiave dispositivo per il provider **cora-iq**, scegliendo **Read** solo per le letture o **Write** per comandarlo anche. Incolla la chiave, tocca **Convalida**, scegli la vasca, poi **Salva**. Al collegamento vengono importati gli ultimi 33 giorni della sua cronologia.

Leggerlo e comandarlo funziona come sul telefono: vedi [Controllare la tua attrezzatura](/help/mobile-device-control) per uscite, modalità, teste di dosaggio e comandi tester, e per i limiti di dose per testa.

## Programmi

I programmi giornalieri delle pompe Jecod li puoi creare sia sullo schermo a parete sia sul telefono. L'editor è lo stesso: un grafico della giornata, un elenco di periodi e una riga di azioni. Trovi di più in [Programmare l'attrezzatura](/help/mobile-schedules).

Il programma di una gyre Maxspect *(beta)* qui lo puoi vedere ma non salvare. Impostalo nell'app Maxspect.

## Prese

Alle prese arrivi anche dal cassetto **Prese e alimentazione** in fondo alla dashboard. Lì trovi in un unico posto le prese attivate per questa dashboard (tutte, se non ne hai scelta nessuna). Trovi di più in [Prese e controlli](/help/max-controls).

Le teste DŌS non compaiono mai nell'elenco delle prese, così nessuno può accenderne una da lì e lasciarla andare. Per dosare usa la pagina della testa. Un Apex grande con più moduli mostra tutte le sue prese e sonde.

## Materiali di consumo

Le soglie di rifornimento (reagenti, contenitori, serbatoi) si impostano qui dalla pagina del dispositivo, come sul telefono. Trovi di più in [Materiali di consumo](/help/mobile-consumables).

## Registrare e calcolare vicino alla vasca

Due cose spesso sono più comode sullo schermo a parete che sul telefono:

- **Registra parametri**: dal menu della vasca, scrivi i risultati dei test con la tastiera sullo schermo.
- **Calcolatore dose**: dalla pagina di un parametro, calcola una correzione in base al volume della vasca e alla concentrazione dei tuoi prodotti. Usa lo stesso volume e le stesse concentrazioni del telefono, quindi una dose calcolata qui corrisponde a una calcolata lì. Trovi di più in [Dosaggio](/help/mobile-dosing).

## Su un secondo Cora Max

Quando una vasca compare su più di un Cora Max, solo uno legge l'attrezzatura di quella vasca. Nelle pagine dei dispositivi si chiama il Cora Max della vasca. Gli altri aprono lo stesso le pagine dei dispositivi (se l'indicatore di stato dice **Cloud**, questo schermo è uno di loro). Mostrano l'ultima lettura del Cora Max della vasca e quanto tempo fa è stata fatta. Ogni comando passa da Cora Cloud e lo esegue il Cora Max della vasca.

Alcune cose si fanno solo dal Cora Max della vasca:

- **Misura per dosare** e **Rimisura** compaiono solo lì. Una volta misurata la testa, **Dosa ora** funziona da qualsiasi Cora Max.
- Da un altro Cora Max puoi cambiare un programma Jecod solo se il Cora Max della vasca ha letto la pompa nell'ultima ora, e mai per una pompa che comunica solo via Bluetooth. Ogni **Applica alla pompa** da lì invia al massimo 12 modifiche, quindi manda le modifiche più grandi in più volte.

## Cosa è stato cambiato, e da cosa

Ogni azione viene registrata con la sua causa. Trovi di più in [Attività e cronologia](/help/mobile-activity).
