---
title: EcoTech-Leuchten, -Pumpen und -Dosierer
description: EcoTech Radion-Leuchten, VorTech-Pumpen und Versa-Dosierer über Bluetooth mit Cora verknüpfen, und was du damit tun kannst.
section: Cora Mobile
reviewed: 2026-10-13
order: 18
group: Equipment
---

:::note Beta
**Beta.** EcoTech ist in der Beta und nur für Beta-Nutzer offen. Wenn du kein Beta-Nutzer bist, siehst du es nicht unter **Gerät hinzufügen**. Für Beta-Zugang wende dich an den [Support](/support.html).
:::

Auf dieser Seite verknüpfst du EcoTech Radion-Leuchten, VorTech-Pumpen und Versa-Dosierer mit Cora und steuerst sie. Fang bei **Geräte → Gerät hinzufügen → EcoTech** an. Dieselbe Zeile findet auch die Geräte von AquaIllumination, NYOS Quantum, Nero und Orbit, die im selben Bluetooth-Netzwerk sitzen.

## Was du brauchst {#what-you-need}

- Ein Cora Max am Becken. Es übernimmt das Abfragen und schickt deine Befehle über Bluetooth an die Ausrüstung. Ohne eins zeigt die Zeile **EcoTech** **Erfordert Cora Max** und bleibt ausgegraut.
- Bluetooth auf deinem Handy eingeschaltet, mit Bluetooth-Berechtigung für Cora. Cora fragt danach, wenn du suchst.
- Ausrüstung, die eingeschaltet und in Reichweite des Cora Max ist.

## Verknüpfen {#linking-it}

1. Geh zu **Geräte → Gerät hinzufügen → EcoTech**.
2. Cora sucht nach Leuchten, Pumpen und Dosierern in der Nähe. Leuchten, die schon mit der eigenen Mobius-App von EcoTech verbunden sind, erscheinen vielleicht nicht.
3. Ausrüstung im selben Bluetooth-Netzwerk wird als ein **Mobius-Becken** zusammengefasst. Tippe auf **Verknüpfen mit…** und wähl das Cora-Becken, zu dem sie gehört.
4. Gib der Gruppe einen Namen, wenn Cora danach fragt, und sie ist verknüpft.

Ein Gerät mit **Nur Anzeige** zeigt seine Messwerte, aber Cora kann es noch nicht steuern. Die Steuerung für dieses Modell kommt, nachdem es getestet wurde.

Hat dasselbe Bluetooth-Netzwerk auch Leuchten an einem anderen Becken, und werden die beiden Becken von verschiedenen Cora Max abgefragt, sagt Cora **Von einem Cora Max gelesen**. Ein Cora Max fragt dann das ganze Netzwerk für beide Becken ab.

Wird nichts gefunden, prüf, ob Bluetooth an ist und die Ausrüstung Strom hat, und tippe dann auf **Erneut suchen**.

## Radion-Leuchten {#radion}

![Eine Radion-Seite in Cora Mobile](img/mobile-radion.webp "Status, die Leuchten in diesem Netzwerk (alle oder eine), dann Intensität und jeder Farbkanal.")

Die Seite der Leuchte hat einen Zeitplan-Editor und schnelle Szenen (**Zeitplan**, **Sturm**, **Wolken**, **Farben**, **Füttern**, **Aus**). Du kannst auch Eingewöhnung, Lüfter, Mondzyklus und Uhr einstellen.

Im Zeitplan-Editor spielt **Tagesablauf ansehen** den Tag im Schnelldurchlauf ab, damit du ihn siehst, ohne zu warten. **Vorschau stoppen** stellt die Leuchten zurück. **Rückgängig** und **Wiederholen** gehen durch deine Änderungen, und **Starten mit…** beginnt einen neuen Zeitplan als Kopie eines bestehenden.

Cora liest die Leuchten von Zeit zu Zeit ab. In den **Radion-Einstellungen** legt unter **Auslesen** die Einstellung **Leuchten auslesen alle** fest, wie oft. Seltener ist schonender für die Leuchten. Das Öffnen der Seite und jeder Befehl lesen die Leuchten trotzdem sofort.

Die **Radion-Einstellungen** haben außerdem:

- **Uhr stellen**, um die Uhr der Leuchte zu stellen.
- **Eingewöhnung**, für neue Korallen: Der ganze Zeitplan steigt über die Tage, die du festlegst, langsam an. Einschalten startet ihn wieder von der niedrigeren Stufe.
- **Warnungen**: **Leuchte antwortet nicht mehr**, **Fehler: Hitze, Lüfter oder LED**, **Uhr um 5 Min. abweichend** und **LED-Temperatur**. Schalte die ein, die du willst.

## VorTech-Pumpen {#vortech}

Eine VorTech-Kachel zeigt Modus und Geschwindigkeit der Pumpe. Du kannst den Modus und die **Geschwindigkeit** ändern, ihren Zeitplan bearbeiten und **Füttern** für ein paar Minuten starten. Füttern bremst jede VorTech am Becken, und am Ende kehren sie zu ihren Zeitplänen zurück. Neben jedem Modus steht eine kurze Beschreibung, von gleichmäßiger Strömung bis zu Riffkamm-Schüben, Gezeitenwellen und Pulsen. Eine Pumpe bietet nur die Modi an, die sie unterstützt.

## Versa-Dosierer {#versa}

Die Seite eines Versa zeigt Behälter, Dosierungen und Grenzen. Du kannst die Behältergröße einstellen, auf **Als nachgefüllt markieren** tippen, **Jetzt dosieren** ausführen, die Dosierung mit **Pause** bis Mitternacht anhalten und den Zeitplan bearbeiten. Cora führt für jeden Kopf einen Dosierverlauf. Die Glocke legt Nachfüllwarnungen in verbleibenden Tagen oder nach Füllstand des Behälters fest, wie unter [Verbrauchsmaterial und Nachfüllwarnungen](/help/mobile-consumables) beschrieben.

:::warning Noch nicht an Hardware erprobt
Befehle an VorTech-Pumpen und Versa-Dosierer sind an echter Hardware noch nicht erprobt. Das Lesen funktioniert. Prüf bei den ersten Änderungen die Ausrüstung selbst und sag uns über [Ein Problem melden](/help/mobile-support), was du siehst.
:::

## Warnungen {#alerts}

Cora behandelt ein EcoTech-Gerät nach drei verpassten Messungen in seinem eigenen Messintervall als still. Ein Netzwerk nur mit Leuchten wird standardmäßig alle 30 Minuten gelesen, das dauert also mindestens 90 Minuten. Siehe [Warnungen und Schwellenwerte](/help/mobile-alerts). Radion-Leuchten haben außerdem ihre eigenen Warnungen in den **Radion-Einstellungen**, wie oben beschrieben.

## Auf Cora Max {#on-cora-max}

Dieselbe Ausrüstung hat auf dem Wandbildschirm ihre eigenen Seiten. Mehr dazu unter [Ausrüstung mit Cora Max steuern](/help/max-device-control).
