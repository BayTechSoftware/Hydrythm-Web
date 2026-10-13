---
title: Materiali di consumo e avvisi di rifornimento
description: Imposta gli avvisi di rifornimento per reagenti, contenitori di dosaggio, serbatoi di rabbocco e rotoli filtranti, e di' a Cora quando hai rifornito.
section: Cora Mobile
reviewed: 2026-10-13
order: 16
group: Equipment
---

Usa gli avvisi di rifornimento perché Cora ti avvisi prima che finiscano reagente, liquido di dosaggio, acqua di rabbocco o rotolo filtrante. Apri il dispositivo da **Dispositivi** (oppure tocca il suo riquadro sulla dashboard), poi tocca la **campanella** nella barra in alto.

## Impostare un avviso di rifornimento {#setting-a-refill-alert}

![Il pannello Avvisi di un ReefDose 4, con una soglia di giorni rimasti e un interruttore per ogni testa](img/mobile-consumables.webp "Una soglia per testa, ognuna con il suo interruttore.")

Il pannello si chiama **Avvisi:** seguito dal nome del dispositivo. Se l'attrezzatura ha più contenitori, ognuno ha la sua soglia e il suo interruttore, così puoi impostare in modo diverso una testa che tieni d'occhio e una che tocchi di rado. Se spegni un interruttore, il valore resta salvato per dopo.

Dove impostarlo:

- **La maggior parte dei dispositivi**: la campanella nella barra in alto della pagina del dispositivo.
- **DŌS**: la scheda **Avvisi** nella pagina del DŌS, oppure la campanella. Vedi [Avvisi del dosatore](/help/mobile-device-control#doser-alerts).
- **Dosatori AquaWiz e GHL**: la loro regola nella scheda **Regole** del [Centro avvisi](/help/mobile-alerts).

Quasi tutte le soglie sono in giorni, non in volume. Cora calcola quanto durerà quello che resta al ritmo con cui lo stai usando. "Quattro giorni di calcio rimasti" è un dato su cui puoi agire. "180 mL rimasti" no.

## Di cosa puoi essere avvisato {#thresholds}

| Dispositivo | Soglia | Valore iniziale |
|---|---|---|
| Trident | **Test rimanenti** (il reagente più basso) | 10 test |
| Trident | **Flacone dei rifiuti** (con il flacone pieno il test successivo fallisce) | pieno all'85% |
| Testa DŌS | *[testa] · giorni rimanenti* | 7 giorni |
| Testa DŌS | *[testa] · rimanente*, in mL | 100 mL |
| Testa DŌS che toglie l'acqua vecchia | **Spazio rimanente nel contenitore dei rifiuti** | |
| Testa DŌS | **Avvisi di dose mancata** (un interruttore) | |
| Testa ReefDose | Giorni di integratore rimasti | 7 giorni |
| ReefATO+ | **Autonomia del serbatoio**, stimata dal consumo recente di rabbocco | 2 giorni |
| ReefMat | **Rullo rimanente**, stimato dalla velocità con cui avanza il rullo | 3 giorni |
| AquaWiz | Integratore di alcalinità rimasto | 100 mL |
| Dosatore GHL *(Beta)* | Quanto è pieno il contenitore | 20% |
| EcoTech Versa *(Beta)* | Giorni di integratore rimasti, e quanto è pieno il contenitore | 7 giorni, 10% |

Un'unità Focustronic *(Beta)* mostra i propri avvisi su reagente e tampone nella sua pagina.

:::note Beta
**Beta.** GHL, EcoTech e Focustronic sono in Beta e sono disponibili solo per gli utenti Beta. Se non sei un utente Beta non li vedrai in **Aggiungi dispositivo**. Per chiedere l'accesso alla Beta, contatta l'[assistenza](/support.html).
:::

Un avviso sui materiali di consumo funziona come tutti gli altri avvisi. Compare nel [Centro avvisi](/help/mobile-alerts) e può arrivarti come notifica sul telefono. Ricevi **una** notifica quando il livello supera la soglia, e l'avviso si chiude quando il livello torna sopra la soglia.

## Scegliere la soglia {#choosing-a-threshold}

Impostala con abbastanza anticipo da avere il tempo di agire. Se scatta il giorno in cui qualcosa finisce, non è un avviso.

:::warning Alcune attrezzature continuano anche quando sono vuote
Una testa DŌS con il contenitore vuoto continua a seguire il suo programma e registra dosi che non ha mai erogato. Non ha un avviso di livello basso suo. L'avviso di rifornimento è il modo per accorgertene, quindi impostane uno per ogni testa che usi.
:::

## Dopo il rifornimento {#after-refilling}

Diglielo nella pagina del dispositivo, così l'avviso si chiude e il prossimo viene calcolato dal livello giusto.

| Dispositivo | Tocca |
|---|---|
| Testa DŌS | **Riempi**, poi **Pieno**, oppure imposta **Volume rimanente** |
| Contenitore dei rifiuti DŌS | Riporta lo spazio libero al massimo dopo averlo svuotato |
| Testa ReefDose | **Rimanente nella bottiglia** |
| ReefMat | **Nuovo rotolo (Beta)** dopo aver caricato un rotolo nuovo |
| EcoTech Versa *(Beta)* | **Segna come riempito** |

Trident, ReefATO+ e AquaWiz riportano da soli i propri livelli, quindi in Cora non c'è niente da azzerare.
