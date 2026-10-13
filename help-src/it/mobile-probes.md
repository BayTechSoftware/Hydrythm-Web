---
title: Mappatura parametri e sonde
description: Scegli quale sonda guida ogni lettura, di' a Cora cosa misura ogni sonda e registra calibrazioni e pulizie delle sonde.
section: Cora Mobile
reviewed: 2026-10-13
order: 15
group: Equipment
---

Usa **Mappatura parametri** per dire a Cora cosa misura ogni sonda e, quando due sonde riportano la stessa cosa, di quale fidarsi. Vai in **Impostazioni**, apri la vasca e tocca **Mappatura parametri**.

Si trova tra **Modifica vasca** e **Soglie di avviso**. La matita in alto sulla dashboard apre **Modifica vasca**, che non la contiene. La raggiungi anche dalle pagine dei dispositivi Neptune Apex e GHL (Beta). GHL è disponibile solo per gli utenti Beta. Vedi [Funzioni Beta](/help/mobile-beta).

La schermata ha un campo di ricerca (**Cerca parametri**) e due schede, **Mappatura** e **Fonti**. La ricerca guarda nei nomi dei parametri, nei nomi delle sonde, nei dispositivi e nelle marche. Lo stesso campo di ricerca c'è in ogni selettore di parametri.

## Sonde: dire a Cora cos'è ognuna {#mapping}

![La scheda Mappatura](img/mobile-probe-mapping.webp "Ogni sonda, raggruppata per il dispositivo che la riporta, con il parametro a cui è mappata.")

Si apre per prima la scheda **Mappatura**. Elenca tutte le sonde che Cora conosce, raggruppate per il dispositivo che le riporta, con la lettura attuale. Cora riconosce da sola i nomi standard delle sonde, e ogni riga mostra a cosa le ha associate. Di solito devi correggere solo le poche che non è riuscita a collocare.

Ogni riga ti dà tre scelte.

- **Un parametro Cora** è il valore che misura quella sonda.
- **Personalizzato…** è per una sonda per cui Cora non ha un parametro standard. Scrivi un nome breve in maiuscolo in **Parametro personalizzato (token in MAIUSCOLO)**, e Cora la segue con quel nome.
- **Ignora** è per le sonde che non vuoi registrare per niente.

Una sonda ignorata o non mappata non compare su una dashboard e non fa scattare avvisi.

Una mappatura comincia a funzionare dalle letture successive. Correggerne una qui non riscrive lo storico. Cambia solo quello che viene salvato da quel momento. Tocca **Salva** per applicare le modifiche.

:::warning Cora non vede una sonda non mappata
Se un parametro non mostra letture ma la sonda funziona, controlla per prima cosa la sua mappatura.
:::

## Da dove arriva ogni lettura {#sources}

![La scheda Fonti](img/mobile-probes.webp "Ogni lettura, la sonda che la alimenta e se è Automatico o Scelto da te.")

La scheda **Fonti** elenca ogni parametro che Cora segue per questa vasca, come pH o temperatura, e mostra quale sonda lo sta alimentando in questo momento.

Tocca una lettura per vedere tutte le sonde che la riportano, in tutti i controller che hai collegato. Ognuna mostra la sua marca, il nome che ha per la sonda e il valore in tempo reale. Scegline una per fissarla, oppure scegli **Automatico (vince la lettura più recente)** per lasciare che Cora usi la sonda che ha riportato per ultima. Le altre restano nello storico.

Un'etichetta accanto a ogni lettura mostra quale vale: **Automatico**, oppure **Scelto da te** dopo che hai fissato una sonda. La tua scelta vale per quella lettura in tutta la vasca, non per un solo widget.

Se una sonda fissata smette di riportare, Cora mostra quando l'ha sentita l'ultima volta e offre **Torna ad Automatico**, così una sonda morta non può lasciare una lettura bloccata.

Tocca **Rinomina** per dare a una lettura un nome tutto suo. È separato da qualsiasi nome tu dia alla sonda stessa. È quello che compare sulla dashboard, negli avvisi e in Reef Buddy.

Anche il profilo della vasca ha una sezione **Fonti dei parametri** (è nascosta mentre crei una vasca nuova). Imposta la stessa cosa in forma più breve. Usa Mappatura parametri quando vuoi avere in un unico posto tutte le sonde di tutti i controller.

:::note Un sensore di allagamento qui non si può riassegnare
L'allarme di un sensore di allagamento dipende dal suo nome, quindi è escluso da questa scelta. Funziona come sempre.
:::

## Più sonde per un parametro {#multiple-probes}

Se hai due sonde di temperatura, sullo stesso controller o su due diversi, mappale entrambe. Cora le tiene come fonti separate, e la scheda **Fonti** è dove scegli quale guida la lettura, oppure lasci Automatico. Puoi confrontarle nella [pagina del parametro](/help/mobile-metric-detail).

Quando due fonti riportano lo stesso parametro, vince la misura più recente. Un valore sullo schermo viene sostituito solo da una lettura con un orario di misura successivo, da qualunque dispositivo arrivi. Una lettura più vecchia, o un dispositivo che rimanda una lettura vecchia, va nello storico e non sovrascrive il valore attuale. Se hai fissato una fonte nella scheda **Fonti**, Cora segue invece quella fonte.

## Registrare la cura delle sonde {#recording-probe-care}

Le sonde derivano. Quando calibri, pulisci o sostituisci una sonda, dillo a Cora, così non scambia il salto nella lettura per un vero cambiamento nella vasca.

1. Tocca il widget del parametro sulla dashboard, per esempio pH, temperatura, salinità o ORP.
2. Tocca **Registra cura della sonda** (l'icona del sensore) nella barra in alto.
3. Scegli cosa hai fatto: **Calibrata**, **Pulita**, **Sostituita**, **Riposizionata** o **Confrontata con un riferimento**. Puoi aggiungere una **Lettura di riferimento** e una nota.
4. Tocca **Registra cura della sonda**.

La pagina del parametro mostra poi quanto tempo fa è stata calibrata quella sonda. La cura delle sonde funziona bene anche come [attività di manutenzione](/help/mobile-maintenance) ricorrente.

:::note Le date di calibrazione spiegano le differenze
Quando una sonda e un test non concordano, controlla quando hai calibrato la sonda l'ultima volta. Di solito la risposta è lì.
:::
