---
title: Mappatura parametri e sonde
description: Vedi le letture di ogni dispositivo in un elenco, scegli il parametro con cui appare ogni lettura e quale dispositivo la alimenta, e registra calibrazione e pulizia.
section: Cora Mobile
reviewed: 2026-11-03
order: 15
group: Equipment
---

Usa **Mappatura parametri** per dire a Cora con quale parametro appare ogni lettura e, quando due dispositivi riportano la stessa cosa, di quale fidarsi. Vai in **Impostazioni**, apri la vasca e tocca **Mappatura parametri**.

![Le impostazioni della vasca in Cora Mobile, con Mappatura parametri e Partner collegati](img/mobile-tank-settings.webp "Impostazioni, poi la tua vasca: Mappatura parametri è la seconda riga.")

Si trova tra **Modifica vasca** e **Soglie di avviso**. La matita in alto sulla dashboard apre **Modifica vasca**, che non la contiene. La raggiungi anche dalle pagine dei dispositivi Neptune Apex.

La schermata è un unico elenco di dispositivi, con un campo di ricerca (**Cerca parametri**) sopra. La ricerca guarda nei nomi dei parametri, nei nomi delle letture, nei dispositivi e nelle marche. Lo stesso campo di ricerca c'è in ogni selettore di parametri.

## Un unico elenco di dispositivi {#mapping}

![Mappatura parametri in Cora Mobile, con un dispositivo aperto](img/mobile-probe-mapping.webp "Un unico elenco di dispositivi. Apri un dispositivo per vedere le sue letture e con quale parametro appare ognuna.")

Sotto il campo di ricerca, Cora spiega la schermata in una riga: le letture di ogni dispositivo e il parametro della vasca con cui vengono mostrate. Tocca una lettura per cambiarla.

- **Ogni dispositivo compare con il nome che gli hai dato.** Un dispositivo senza nome compare con la sua marca, e due dispositivi senza nome della stessa marca vengono numerati ("AquaWiz 1", "AquaWiz 2"). I numeri di serie e gli ID dei dispositivi non sono mai usati come nomi; stanno dietro **Mostra dettagli** nella pagina del dispositivo. Vedi [La pagina di un dispositivo](/help/mobile-devices#a-devices-page).
- **Ogni lettura è elencata sotto il dispositivo che la riporta davvero.** Ogni riga mostra il nome che il dispositivo dà alla lettura, il suo ultimo valore e **Mostrata come**, il parametro della vasca che alimenta. Una lettura che hai nascosto dice **Non mostrata**.
- **Una vasca ha un solo Neptune Apex**, per quanti dispositivi Cora lo leggano. Le sue sonde sono un unico elenco sotto un'unica sezione **Apex** (o sotto il nome che gli hai dato). Un modulo di espansione Apex, come un DŌS o un Trident, è elencato con il proprio nome. Le sue letture non si possono reindirizzare; toccarne una ti permette invece di rinominare il parametro.
- **Un dispositivo condiviso con altre vasche compare nell'elenco di ogni vasca a cui è collegato.** La sua sezione dice *Anche su* e i nomi delle altre vasche, seguiti da *Le modifiche qui valgono solo per questa vasca.*
- **Un dispositivo con due letture o meno si apre da solo**; uno più lungo parte chiuso e mostra il numero delle sue letture, a meno che una delle sue letture condivida un parametro con un altro dispositivo. Tocca il nome di un dispositivo per aprirlo o chiuderlo. Mentre cerchi, tutti i risultati sono aperti.

Cora riconosce da sola i nomi standard delle letture, quindi la maggior parte delle righe mostra già il parametro giusto. Correggi solo le poche che non è riuscita a collocare.

Una modifica viene salvata nel momento in cui la scegli, e non c'è alcun pulsante Salva. Comincia a funzionare dalle letture successive. Correggerne una qui non riscrive lo storico: le letture passate restano dove sono, e cambia solo quello che viene salvato da quel momento. Le mappature fatte prima di questa schermata restano invariate.

:::warning Cora non vede una lettura nascosta
Se un parametro non mostra letture ma il dispositivo funziona, controlla se la sua lettura dice **Non mostrata**.
:::

:::note Un sensore di allagamento qui non si può riassegnare
L'allarme di un sensore di allagamento dipende dal suo nome, quindi la sua riga dice *L'allarme perdite dipende da questo nome, quindi non può essere modificato qui.* Funziona come sempre.
:::

:::note Dispositivi che aspettano ancora un aggiornamento
Un dispositivo che aspetta un aggiornamento del firmware dice *Le modifiche qui hanno effetto dopo l'aggiornamento del firmware di questo dispositivo.* La tua scelta viene salvata e si applica una volta installato l'aggiornamento.
:::

## Scegliere con quale parametro appare una lettura {#shows-as}

Per cambiare con quale parametro appare una lettura:

1. Vai in **Impostazioni**, tocca la tua vasca sotto **Vasche**, poi tocca **Mappatura parametri**.
2. Tocca il nome di un dispositivo per aprirlo. Per trovare più in fretta una lettura, scrivi una parte del suo nome in **Cerca parametri**.
3. Tocca la lettura. Si apre **Mostra questa lettura come**.
4. Tocca il parametro con cui deve apparire. La tua scelta viene salvata subito e il foglio si chiude.
5. Controlla l'etichetta **Mostrata come** della lettura nell'elenco. Ora indica il parametro che hai scelto.

![Mostra questa lettura come, con l'elenco dei tuoi parametri e da dove arrivano le letture di ciascuno](img/mobile-probes-shows-as.webp "Ogni parametro dice da dove arrivano le sue letture: un dispositivo, nessuno al momento, oppure i tuoi risultati dell'ICP.")

Tocca una lettura per aprire **Mostra questa lettura come**. In alto c'è la lettura stessa: il dispositivo, il nome della lettura e il suo valore. Sotto:

- **I tuoi parametri** elenca ogni parametro di questa vasca. Ogni opzione dice da dove arrivano le sue letture, così non devi mai indovinare tra due nomi simili:
  - *Arriva da* e il nome del dispositivo che lo alimenta, oppure *Arriva anche da* e il nome di un altro dispositivo quando questa lettura appare già come quel parametro.
  - *Nessun dispositivo lo alimenta ora. Ultimo valore …* con quanto tempo fa, per un parametro il cui dispositivo si è zittito.
  - *Dai tuoi risultati dei test* oppure *Dai risultati dell'ICP*, con l'ultimo valore, per un parametro che ha solo i tuoi risultati.

  La matita (**Rinomina**) accanto a un parametro gli dà un nome tutto tuo. È quello che compare sulla dashboard, negli avvisi e in Reef Buddy. Lascia vuoto il nome per ripristinarlo.
- **Altri parametri** è ripiegato. Contiene i parametri standard che questa vasca non ha ancora.
- **Nuovo parametro…** crea un parametro a sé, separato dagli altri parametri. Vedi sotto.
- **Non mostrare questa lettura** (*Cora la ignora*) impedisce che la lettura venga registrata come un qualsiasi parametro. Una lettura nascosta non compare su nessuna dashboard e non fa scattare avvisi.

Il foglio finisce con *Salvato appena scegli. Le letture passate restano dove sono.*

![La fine di Mostra questa lettura come, con Altri parametri, Nuovo parametro e Non mostrare questa lettura](img/mobile-probes-shows-as-end.webp "Scorri fino in fondo per trovare Altri parametri, Nuovo parametro… e Non mostrare questa lettura.")

### Nuovo parametro {#new-parameter}

Usa **Nuovo parametro…** quando una lettura non deve essere mescolata con un'altra dello stesso nome, per esempio una seconda sonda del pH nella sump. Cora apre **Nuovo parametro** e spiega che la lettura di quel dispositivo verrà mostrata come un parametro a sé e che la sua unità arriva dal dispositivo.

1. In **Mostra questa lettura come**, scorri fino in fondo e tocca **Nuovo parametro…**.
2. Scrivi un **Nome**. Qualsiasi nome, per esempio *pH sump* o *pH 2*, fino a 32 caratteri.
3. Tocca **Crea**. **Crea** resta grigio finché il nome è vuoto. **Annulla** chiude la finestra e non cambia nulla.

![La finestra Nuovo parametro](img/mobile-probes-new-parameter.webp "Nuovo parametro: la lettura ottiene un parametro tutto suo, con l'unità che arriva dal dispositivo.")

La lettura ora alimenta il nuovo parametro. Il nome mantiene la grafia che hai scritto. Se scrivi il nome di un parametro che hai già, la lettura si unisce a quello e il suo nome non viene modificato. Nessun intervallo di avviso viene copiato da un altro parametro.

## Test e risultati di laboratorio {#tests-and-lab-results}

I risultati dei tuoi test e i tuoi risultati dell'ICP sono elencati in fondo, in **Test e risultati di laboratorio**. La sezione parte chiusa, perché un solo rapporto ICP ha decine di elementi. Toccala per aprirla. I risultati sono raggruppati sotto **Risultati dell'ICP** e **I tuoi risultati dei test**.

Ogni risultato si mappa su un parametro come la lettura di un dispositivo. Toccane uno per aprire **Mostra questa lettura come** e scegliere il parametro con cui appare, per esempio per tenere il pH di un test separato da quello di una sonda. Cora lo dice nella sezione: i nuovi risultati seguono la tua scelta, quelli passati restano dove sono. Un risultato di test o ICP non viene mai scartato, quindi **Non mostrare questa lettura** non è offerto per lui.

I parametri che nessuna lettura qui sopra alimenta, e che non sono test, sono elencati sotto **Altri parametri della vasca**. Toccane uno per rinominarlo.

## Più sonde per un parametro {#multiple-probes}

Se due letture appaiono come lo stesso parametro, che vengano da due sonde di un dispositivo o da due dispositivi diversi, in cima all'elenco compare un banner. Dice per esempio *pH riceve letture da 2 dispositivi* (o *2 sonde*), seguito da cosa sta facendo Cora: *Viene mostrata la più recente.* oppure *Usa* il dispositivo che hai scelto. Toccalo, o tocca **Scegline una**, per aprire il foglio.

- **Lettura più recente** (*Il dispositivo che ha inviato per ultimo*) lascia che Cora usi il dispositivo che ha riportato per ultimo. Gli altri restano nello storico.
- Scegli un dispositivo o una sonda per seguire solo quello. Ognuno mostra il suo valore e quanti minuti fa ha riportato. La tua scelta vale per quel parametro ovunque nella vasca: riquadro, grafico e avvisi, non un solo widget.
- **Mostrane una a parte** (*Per esempio una seconda sonda nella sump*) chiede **Quale mostrare a parte?** e poi apre **Mostra questa lettura come** per quella che scegli.

Se un dispositivo che hai scelto smette di riportare, il banner dice *Non segnala più dal* e l'ora, e offre **Usa la più recente**, così una sonda morta non può lasciare una lettura bloccata.

Puoi confrontare le fonti nella [pagina del parametro](/help/mobile-metric-detail).

Quando due fonti riportano lo stesso parametro, vince la misura più recente. Un valore sullo schermo viene sostituito solo da una lettura con un orario di misura successivo, da qualunque dispositivo arrivi. Una lettura più vecchia, o un dispositivo che rimanda una lettura vecchia, va nello storico e non sovrascrive il valore attuale. Se hai scelto un dispositivo, Cora segue invece quel dispositivo.

Anche il profilo della vasca ha una sezione **Fonti dei parametri** (è nascosta mentre crei una vasca nuova). Imposta la stessa cosa in forma più breve. Usa Mappatura parametri quando vuoi avere in un unico posto tutti i dispositivi e tutte le letture.

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
