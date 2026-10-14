---
title: ICP e report di salute
description: Carica il PDF di un test ICP o fallo inviare dal tuo laboratorio, leggi il punteggio, segui ogni elemento nel tempo e avvia un Report di salute di tutto l'impianto.
section: Cora Mobile
reviewed: 2026-10-13
order: 33
group: Intelligence
twin: max-intelligence
---

La scheda **Intelligence** è dove stanno i risultati di laboratorio e i report a lungo termine. Prima scegli una vasca in alto. Tutto quello che c'è sullo schermo appartiene a quella vasca.

![La scheda Intelligence](img/mobile-intelligence.webp "Carica un ICP, avvia un report di salute e guarda cosa è cambiato dall'ultimo.")

## Caricare un test ICP

Cora legge il report in PDF che ti manda il laboratorio. Scaricalo prima dall'email o dal sito del tuo laboratorio. Foto, scansioni e screenshot non si possono leggere.

1. Tocca **Carica ICP**.
2. Scegli il tuo laboratorio, oppure lascia **Auto: rileva il laboratorio**. Cora ha consigli per ATI, Fauna Marin, Modern Reef, Oceamo, Reef Zlements e Triton.
3. Indica cos'è il campione: **Acqua di vasca**, **Acqua RO/DI**, **Miscela di sale** o **Altro**. Solo l'acqua di vasca aggiorna la dashboard e gli avvisi.
4. Controlla la data in cui è stato prelevato il campione. I laboratori stampano la data in cui l'hanno analizzato, quindi Cora ti chiede la tua e mette i risultati sul grafico in base a quella.
5. Tocca **Scegli PDF** e scegli il file.

Di solito ci vogliono uno o due minuti. Tieni aperta la schermata e il report si apre appena è pronto. Non devi scrivere niente.

Puoi anche inviare il PDF per email a **icp@in.coraiq.tech**. Invialo dalla tua email di accesso o da un'email di laboratorio verificata (vedi sotto), e arriva come un risultato inviato da un laboratorio.

Se carichi due volte lo stesso report, Cora ti mostra quello che hai già e non te lo addebita di nuovo.

:::note Cora ha prima bisogno del tuo consenso
L'analisi ICP invia il report all'IA, quindi richiede **Consenti al Cora Assistant di usare i dati salvati della vasca**. Se è spento, Cora te lo chiede prima del caricamento. Vedi [cosa copre l'interruttore](/help/mobile-assistant#what-the-switch-covers).
:::

## Quale email può usare un laboratorio

Un laboratorio o un risultato inviato per email trova il tuo account dall'indirizzo email che conosce. È la tua email di accesso, più qualsiasi email di laboratorio che aggiungi in **Impostazioni → la scheda del tuo account (Account e abbonamento) → Email laboratorio e ICP**.

1. Tocca **Aggiungi email del laboratorio** e scrivi l'indirizzo che usa il tuo laboratorio.
2. Tocca **Invia codice**. Cora invia un codice di 6 cifre a quell'indirizzo. Scade dopo 10 minuti.
3. Inserisci il codice e tocca **Verifica**. Se non l'hai ricevuto, tocca **Invia di nuovo il codice**.

Puoi aggiungere fino a 3 email di laboratorio. Ognuna mostra **Verificata** o **In attesa del codice**, e **Rimuovi** ne toglie una. Da quel momento i risultati inviati a quell'indirizzo non arrivano più al tuo account. Un indirizzo che appartiene già a un altro account Cora non si può aggiungere.

Se hai effettuato l'accesso con un'email Apple nascosta, i laboratori non possono trovare il tuo account. La schermata ICP mostra una scheda, **Ricevi automaticamente i risultati del laboratorio**, che ti porta a questa impostazione. Quando accedi con Apple, scegli **Condividi la mia email** per evitare il problema.

## Invia a Cora: risultati che un laboratorio o un'email consegnano per te

Alcuni laboratori possono inviare un risultato direttamente a Cora, e un PDF ICP che invii per email arriva allo stesso modo. Non devi caricare niente tu.

Se hai una sola vasca, un risultato da un laboratorio di cui ti fidi, o uno che hai inviato per email, va direttamente a quella vasca. Con più di una vasca, vedrai un banner: *"Un risultato di laboratorio da {lab} ti sta aspettando."* Tocca **Scegli vasca** e scegli la vasca a cui appartiene. Cora non può capirlo da sola.

Il report mostra **Inviato da {lab}** in alto, oppure **Ricevuto via e-mail**, così lo distingui da uno che hai caricato tu.

Se **Consenti al Cora Assistant di usare i dati salvati della vasca** è spento, il risultato aspetta con il messaggio *Cora Assistant ha bisogno della tua autorizzazione per leggerlo.* Dai il tuo consenso e il risultato entra.

:::note La prima volta
La prima volta che un risultato arriva in questo modo, Cora mostra un breve suggerimento su cosa sta succedendo, così non sembra un errore.
:::

### Il primo risultato da un nuovo laboratorio

La prima volta che un laboratorio ti manda un risultato, Cora ti chiede di approvarlo prima di aggiungerlo da qualche parte, anche se hai una sola vasca. Vedi chi l'ha inviato e puoi spuntare **Fidati di questo laboratorio** per saltare questo controllo la prossima volta che arriva un risultato da quel laboratorio.

Tocca **Approva** per farlo entrare, oppure **Rifiuta** per eliminarlo senza aggiungerlo a nessuna vasca.

### Laboratori affidabili e cosa vedono i laboratori {#trusted-labs}

**Impostazioni → Cora Assistant → Laboratori affidabili** elenca ogni laboratorio di cui ti sei fidato. L'elenco compare dopo che ti sei fidato di almeno uno. **Revoca** toglie un laboratorio, così il suo prossimo risultato ha di nuovo bisogno della tua approvazione.

**Condividi l'analisi di Cora con i laboratori**, nella stessa schermata, decide cosa vede un laboratorio dopo che ti ha inviato un risultato. Se è attivo, vede i punteggi e l'analisi scritta di Cora. Se è spento, vede solo che il risultato è stato consegnato. È spento finché non lo accendi. Lo stesso interruttore compare anche su un report che ti ha inviato un laboratorio.

Se qualcosa qui non funziona, vedi [Risoluzione dei problemi](/help/troubleshooting).

## Cosa ricevi

![Un report ICP](img/mobile-icp-report.webp "Ogni report ha un punteggio e un riassunto scritto per la tua vasca.")

Ricevi un punteggio su 100 e un riassunto con parole semplici di cosa significa per il tuo impianto, tenendo conto del tipo di vasca, della sua età e della tua popolazione.

Il punteggio confronta i tuoi risultati con i loro intervalli obiettivo, compresi quelli che hai impostato tu. Se un risultato è fuori dal suo intervallo, il punteggio non può superare 70, quindi non può risultare **Sano**. Se uno è molto fuori, non può superare 40, per quanto buoni siano gli altri. L'etichetta sotto il punteggio dice **Sano** da 71 a 100, **Richiede attenzione** da 40 a 70 e **Critico** da 0 a 39. I report di salute hanno lo stesso punteggio.

Ogni elemento viene seguito, compresi elementi in traccia e contaminanti oltre ai parametri principali. Cora registra tutti i 71 elementi che un laboratorio può riportare, e la riga che alcuni laboratori chiamano *Acidity* è il pH.

Su ogni riga di elemento vedi l'intervallo stampato dal laboratorio, indicato come *Intervallo del laboratorio*, accanto all'intervallo di Cora per quell'elemento. Un elemento per cui Cora non ha un intervallo di riferimento ha l'etichetta **Nessun intervallo Cora**. Il report dice quanti elementi hanno un intervallo Cora e valuta gli altri in base alla conoscenza generale del reef. Cora Assistant commenta ogni elemento testato, e il suo commento vale anche quando non c'è un intervallo Cora.

Se il laboratorio stampa *n.d.*, o *not detected*, per un elemento, Cora lo registra come 0 e dice che non è stato rilevato.

:::note La CO2 disciolta non è la CO2 della stanza
La **CO₂ disciolta** in un report ICP è la CO2 nell'acqua, in mg/L. È una lettura diversa dalla CO2 dell'aria della stanza. Le due hanno intervalli diversi e non vengono mai mescolate.
:::

La scheda **Dal tuo ultimo ICP** mostra cosa è cambiato di più dall'ultima volta. Di solito è il modo più veloce per entrare in un nuovo report.

Tocca **Tendenze** per vedere un elemento in tutti i test che hai caricato. È qui che l'ICP diventa davvero utile.

:::tip Dal secondo test diventa interessante
Un ICP ti dice dove sei. Il secondo ti dice in che direzione stai andando, ed è su questo che puoi agire. Fai i test con un ritmo regolare, e non aspettare che qualcosa vada storto.
:::

## Un test dell'acqua RO/DI o dell'acqua di partenza

Se carichi acqua RO/DI o un'altra acqua di partenza, scegli **Acqua RO/DI** al caricamento. Cora non la valuta rispetto agli obiettivi della tua vasca. Dà un giudizio semplice su quanto l'acqua è abbastanza pulita da usare, e tiene quei numeri fuori dalle letture della vasca. Viene salvata come report separato. Cora fa lo stesso per **Miscela di sale** o **Altro**: dice a cosa assomiglia il campione e non lo valuta come se fosse la tua vasca.

## Report di salute

Un **Report di salute** è un controllo più approfondito di tutto l'impianto, da fare ogni tanto. Guarda insieme ogni parametro, ogni fonte, il dosaggio, lo storico e i risultati ICP recenti.

Tocca **Report di salute**, poi **Genera**. Di solito ci vogliono una ventina di secondi. Come l'analisi ICP, richiede **Consenti al Cora Assistant di usare i dati salvati della vasca**.

Usalo quando vuoi uno sguardo attento alla vasca. I momenti buoni sono prima di un grande cambiamento, dopo un problema, o ogni qualche settimana come controllo.

Un report aperto ha dei pulsanti in alto per esportarlo come PDF, condividere un'istantanea della vasca o eliminarlo.

## ICP e sonde a confronto

Cora confronta i tuoi risultati di laboratorio con quello che riporta la tua attrezzatura. Se la sonda di alcalinità dice 8,4 e l'ICP dice 7,6, vorrai saperlo, e Cora te lo mostra senza scegliere in silenzio uno dei due.

È una delle cose più utili che fa un ICP in Cora. Consideralo un **terzo parere**. Non è la parola definitiva. I laboratori differiscono, e il modo in cui un campione viene trattato, conservato e spedito sposta il risultato. Un singolo ICP è un indizio, e due test che concordano contano molto più di uno. Se la differenza persiste, controlla la sonda. Non dimostra che la sonda sia sbagliata.

:::tip Cambiare laboratorio o metodo di test
Se cambi laboratorio, o passi tra i test ICP-OES e ICP-MS di un laboratorio, i risultati possono spostarsi anche se in vasca non è cambiato niente. Cora lo segnala quando li confronta. L'ICP-OES non misura livelli molto bassi di cromo, stagno, nichel, rame, cobalto o selenio. Quindi un risultato **Sotto il limite di rilevamento** per questi elementi in un test ICP-OES non vuol dire che la tua vasca non ne abbia.
:::

## La tua quota

Il tuo piano decide quante analisi ICP e quanti report di salute hai ogni mese. La riga sotto i pulsanti mostra quanti ne hai usati. I numeri di ogni piano sono in [Piani e abbonamenti](/help/mobile-plans).

Quando le analisi ICP sono finite, Cora mostra prima i piani a cui puoi passare. Se preferisci non passare a un piano superiore, chiede **Salvare i risultati senza l'analisi IA?** Tocca **Salva i miei risultati** e Cora legge comunque il report e salva ogni valore, così tendenze, storico e letture si aggiornano come al solito. Il punteggio e l'analisi scritta restano bloccati. Puoi avviarli più tardi dal report stesso quando hai un'analisi ICP da usare.

Oltre al limite del tuo piano, Cora accetta fino a 10 caricamenti ICP al giorno. Un caricamento rifiutato per questo motivo non consuma nessuna delle analisi ICP del tuo piano. Cora Mobile però mostra solo un errore di caricamento generico, quindi se i caricamenti iniziano a fallire dopo molti in un giorno, riprova domani.

## Dove stanno i report

La schermata Intelligence tiene separati i due tipi. I risultati di laboratorio sono sotto **RAPPORTI ICP** e le valutazioni generate sotto **RAPPORTI DI SALUTE**. Ogni elenco mostra prima il più recente, con il suo punteggio. Toccane uno per riaprirlo per intero.

Ci arrivi anche dalle **Impostazioni**: apri una vasca, poi **Report ICP** o **Report di salute**.
