---
title: Mehr als ein Cora-Gerät
description: Leg fest, welches Gerät auf Sprache antwortet und welches jedes Becken abfragt.
section: Cora Mobile
reviewed: 2026-09-27
order: 29
group: Account
---

In einem Haushalt kann es mehr als ein Cora Max geben. Zwei Einstellungen legen fest, welches Gerät was übernimmt, damit sie sich nicht in die Quere kommen. Außerdem lohnt es sich zu wissen, was die Geräte überhaupt miteinander teilen.

## Was geteilt wird und was nicht

| Gilt für alle Geräte im Konto | Gehört zu einem Bildschirm |
|---|---|
| Becken, Messwerte und Historie | das Dashboard-Layout |
| Geräte und ihre Einstellungen | WLAN, Helligkeit, Ton |
| Tagebuch, Besatz, Wartung | Weckwort und Kindersicherung |
| Warnungen, Schwellenwerte, Automationen | welche Becken dieser Bildschirm zeigt |
| Abos und Nutzung | |

Änderst du einen Schwellenwert auf einem Gerät, gilt er überall. Ein umgebautes Dashboard gilt dagegen nur dort. Jeder Bildschirm behält sein eigenes Layout, und Handy und Cora Max teilen sich nie eins.

## Cora Assistant: Antwortgerät

Unter **Einstellungen → Cora Assistant → Antwortgerät** legst du fest, welches **Cora-Gerät** antwortet, wenn du in den Raum sprichst. Es antwortet immer nur eins, egal wie viele dich hören. Wähl das Gerät, das deinem üblichen Standort am nächsten ist.

Das ist nicht dasselbe wie das Primäre Cora Max weiter unten. Das Antwortgerät bestimmt, welches Gerät auf deine Stimme antwortet. Das Primäre Cora Max bestimmt, welches Gerät die Ausrüstung eines Beckens abfragt. Hast du zwei Cora Max, stellst du die beiden vielleicht unterschiedlich ein.

![Die Sprachantwort-Auswahl](img/mobile-voice-responder.webp "Jedes Gerät zeigt, worauf es hört, und ob es online ist.")

Zu jedem Gerät in der Liste siehst du, auf welches Weckwort es hört und ob es online ist. **Die Weckwörter sind nicht überall gleich.** Das Wort ist fest im Gerät trainiert, und verschiedene Cora-Modelle können auf verschiedene Wörter hören. Lies das Wort in der Zeile des jeweiligen Geräts nach und geh nicht davon aus, dass im ganzen Haushalt dasselbe gilt.

:::note Dein Handy steht nicht in dieser Liste
Das Handy hört auf kein Weckwort. Dort startest du ein Gespräch per Tippen. Das klappt immer, egal wie diese Einstellung steht. In der Liste stehen nur Cora-Geräte, die Sprache verstehen.
:::

## Primäres Cora Max

Die Ausrüstung in deinem Netzwerk liest ein Cora Max aus. Könnten mehrere Cora Max denselben Controller lesen, würden sie ihn sonst alle gleichzeitig abfragen.

Mit **Primäres Cora Max** legst du für jedes Becken fest, welches Gerät seinen Controller ausliest. Öffne dazu in Cora Mobile das Becken und tippe auf **Primäres Cora Max**.

| Einstellung | Verhalten |
|---|---|
| ein bestimmtes Gerät | Nur dieses Cora-Gerät fragt den Controller ab. Es bleibt auch dann primär, wenn es offline ist, und kein anderes Cora-Gerät springt ein. Cora Mobile fragt nur ab, solange es offline ist. |
| **Jedes aktive (automatisch)** | Cora Mobile und alle Cora-Geräte, die online sind, teilen sich die Arbeit (der letzte Schreibvorgang gilt). Fällt eins aus, macht ein anderes weiter. Das passt für einen Haushalt mit einem Gerät und ist die sicherere Wahl, wenn du nicht weißt, welches Gerät zuständig sein soll. |

Ist das Gerät, das du festgelegt hast, offline, laufen Befehle nicht, die darüber gehen müssen. Cora sagt dir dann, dass das Becken auf dieses Gerät eingestellt ist, dass es offline ist und dass nichts passiert ist. Du kannst es erneut versuchen, sobald das Gerät wieder da ist. Bleibt es länger offline, wähl ein anderes Gerät oder **Jedes aktive (automatisch)**.

:::note Leg ein primäres Gerät fest, wenn zwei Geräte ein Becken im Blick haben
Mit einem primären Gerät wird der Controller weniger belastet, und doppelte Messwerte aus derselben Quelle fallen weg.
:::

:::note Die Einstellung gilt pro Becken für das ganze Konto
Das Primäre Cora Max gehört zum Becken und nicht zu dem Handy oder Cora Max, auf das du gerade schaust. Änderst du es auf irgendeinem Gerät, gilt die Änderung für den ganzen Haushalt.
:::

## Was unterwegs funktioniert

Bist du nicht im WLAN deines Beckens, spricht dein Handy nicht direkt mit deiner Ausrüstung. Ein Befehl geht dann an Cora Cloud, und Cora Cloud gibt ihn an ein Cora Max am Becken weiter. Erst dieses Cora Max erreicht die Ausrüstung.

Das bedeutet:

- **Messwerte und Historie** siehst du immer, egal wo du bist. Sie liegen ja schon in Cora Cloud.
- **Ausrüstung steuern** kannst du auch unterwegs, also eine Steckdose schalten, eine Fütterung starten, einen Kopf dosieren oder eine Pumpe pausieren. Dafür muss ein Cora Max am Becken online sein und die Ausrüstung erreichen. Ist keins online, kommt der Befehl nicht an.
- **Die eigenen Einstellungen eines Geräts** (nicht seine Messwerte) brauchen manchmal ein Handy im *selben* Netzwerk wie das Gerät. Ein Cora Max am Becken reicht dann nicht. Wo das so ist, steht es auf der Seite.

Zwei Meldungen zeigen dir, dass ein Befehl nicht einfach geklappt hat:

- **"Es wurde nichts gesendet"**: Der Befehl hat dein Handy nie verlassen, oder kein Cora Max am Becken konnte ihn übernehmen. Es ist nichts passiert. Das siehst du, wenn das Primäre Cora Max des Beckens offline ist und kein anderes Gerät an diesem Becken einspringen kann.
- **"Es ist möglicherweise schon gelaufen"**: Der Befehl wurde gesendet, aber kein Cora Max hat rechtzeitig bestätigt. Cora weiß wirklich nicht, ob er ausgeführt wurde. Schau direkt an der Ausrüstung nach, bevor du es noch einmal versuchst. Sonst schickst du ihn womöglich doppelt.

Taucht eine dieser Meldungen immer wieder auf, prüf, ob ein Cora Max am Becken online ist. Oder stell **Primäres Cora Max** auf **Jedes aktive (automatisch)**, dann kann jedes Gerät, das online ist, den Befehl übernehmen. Alle möglichen Ergebnisse eines Befehls findest du unter [Deine Ausrüstung steuern](/help/mobile-device-control).

## Wo du den Zustand jedes Geräts siehst

Cora Max zeigt den Abfragestatus jedes Beckens unter **Einstellungen → Cora Max-Einstellungen → Status**. Mehr dazu unter [Geräte und Gerätezustand](/help/max-devices).
