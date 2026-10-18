---
title: Parameterzuordnung und Sonden
description: Festlegen, welche Sonde jeden Messwert liefert, Cora sagen, was jede Sonde misst, und Kalibrierung und Reinigung von Sonden festhalten.
section: Cora Mobile
reviewed: 2026-10-13
order: 15
group: Equipment
---

Mit der **Parameterzuordnung** sagst du Cora, was jede Sonde misst und, wenn zwei Sonden dasselbe melden, welcher es vertrauen soll. Geh zu **Einstellungen**, öffne das Becken und tippe auf **Parameterzuordnung**.

Sie steht zwischen **Becken bearbeiten** und **Warnschwellen**. Der Stift oben auf dem Dashboard öffnet **Becken bearbeiten**, wo es sie nicht gibt. Du erreichst sie auch über die Geräteseiten von Neptune Apex.

Der Bildschirm hat ein Suchfeld (**Parameter suchen**) und zwei Tabs, **Zuordnung** und **Quellen**. Die Suche durchsucht Namen von Wasserwerten, Namen von Sonden, Geräte und Marken. Dasselbe Suchfeld gibt es in jeder Auswahl von Wasserwerten.

## Sonden: Cora sagen, was jede ist {#mapping}

![Der Tab Zuordnung](img/mobile-probe-mapping.webp "Jede Sonde, gruppiert nach dem Gerät, das sie meldet, mit dem Wasserwert, dem sie zugeordnet ist.")

Der Tab **Zuordnung** öffnet sich zuerst. Er listet jede Sonde auf, die Cora kennt, gruppiert nach dem Gerät, das sie meldet, mit ihrem aktuellen Messwert. Cora erkennt Standardnamen von Sonden selbst, und jede Zeile zeigt, was es zugeordnet hat. Meist musst du nur die paar korrigieren, die es nicht einordnen konnte.

Jede Zeile gibt dir drei Möglichkeiten.

- **Ein Cora-Wasserwert** ist der Wert, den diese Sonde misst.
- **Eigener…** ist für eine Sonde, für die Cora keinen Standard-Wasserwert hat. Gib unter **Eigener Wert (GROSSBUCHSTABEN-Token)** einen kurzen Namen in Großbuchstaben ein, und Cora verfolgt sie unter diesem Namen.
- **Ignorieren** ist für Sonden, die gar nicht aufgezeichnet werden sollen.

Eine ignorierte oder nicht zugeordnete Sonde erscheint auf keinem Dashboard und löst keine Warnungen aus.

Eine Zuordnung wirkt, sobald das nächste Mal Messwerte ankommen. Korrigierst du hier eine, wird der Verlauf nicht umgeschrieben. Es ändert sich nur, was ab dann gespeichert wird. Tippe auf **Speichern**, um deine Änderungen zu übernehmen.

:::warning Eine nicht zugeordnete Sonde sieht Cora nicht
Zeigt ein Wasserwert keine Messwerte, obwohl die Sonde funktioniert, prüf zuerst ihre Zuordnung.
:::

## Woher jeder Messwert kommt {#sources}

![Der Tab Quellen](img/mobile-probes.webp "Jeder Messwert, die Sonde, die ihn liefert, und ob er Automatisch oder Von dir gewählt ist.")

Der Tab **Quellen** listet jeden Wert auf, den Cora für dieses Becken verfolgt, etwa pH oder Temperatur, und zeigt, welche Sonde ihn gerade liefert.

Tippe auf einen Messwert, um jede Sonde zu sehen, die ihn meldet, über alle Controller, die du verbunden hast. Jede zeigt ihre Marke, ihren eigenen Namen für die Sonde und ihren Live-Wert. Wähl eine, um sie festzulegen, oder wähl **Automatisch (neueste Messung gewinnt)**, damit Cora die Sonde nimmt, die zuletzt gemeldet hat. Die anderen bleiben im Verlauf.

Ein Hinweis neben jedem Messwert zeigt, was gilt: **Automatisch** oder **Von dir gewählt**, sobald du eine Sonde festgelegt hast. Deine Wahl gilt für diesen Messwert im ganzen Becken, nicht für ein einzelnes Widget.

Meldet sich eine festgelegte Sonde nicht mehr, zeigt Cora, wann sie zuletzt gehört wurde, und bietet **Zurück zu Automatisch** an, damit eine tote Sonde einen Messwert nicht festhalten kann.

Tippe auf **Umbenennen**, um einem Messwert einen eigenen Anzeigenamen zu geben. Das ist getrennt von jedem Namen, den du der Sonde selbst gibst. Er erscheint auf deinem Dashboard, in Warnungen und in Reef Buddy.

Das Beckenprofil hat außerdem einen Bereich **Wasserwert-Quellen** (er ist ausgeblendet, während du ein neues Becken anlegst). Er legt dasselbe in kürzerer Form fest. Nutze die Parameterzuordnung, wenn du jede Sonde an jedem Controller an einem Ort haben willst.

:::note Ein Lecksensor lässt sich hier nicht neu zuordnen
Der Alarm eines Lecksensors hängt von seinem eigenen Namen ab, deshalb ist er aus dieser Auswahl ausgenommen. Er funktioniert wie immer.
:::

## Mehrere Sonden für einen Wasserwert {#multiple-probes}

Hast du zwei Temperatursonden, egal ob am selben Controller oder an zwei verschiedenen, ordne beide zu. Cora behält sie als getrennte Quellen, und im Tab **Quellen** wählst du, welche den Messwert liefert, oder lässt es auf Automatisch. Vergleichen kannst du sie in [der Wasserwert-Ansicht](/help/mobile-metric-detail).

Melden zwei Quellen denselben Wasserwert, gewinnt die neueste Messung. Ein Wert auf dem Bildschirm wird nur durch einen Messwert mit späterem Messzeitpunkt ersetzt, egal von welchem Gerät. Ein älterer Messwert, oder ein Gerät, das einen alten noch einmal schickt, geht in den Verlauf und überschreibt den aktuellen Wert nicht. Hast du im Tab **Quellen** eine Quelle festgelegt, folgt Cora stattdessen dieser Quelle.

## Sondenpflege erfassen {#recording-probe-care}

Sonden driften. Wenn du eine Sonde kalibrierst, reinigst oder ersetzt, sag es Cora, damit es den Sprung im Messwert nicht für eine echte Änderung im Becken hält.

1. Tippe auf dem Dashboard auf das Widget des Wasserwerts, zum Beispiel pH, Temperatur, Salinität oder ORP.
2. Tippe in der oberen Leiste auf **Sondenpflege erfassen** (das Sensorsymbol).
3. Wähl, was du gemacht hast: **Kalibriert**, **Gereinigt**, **Ersetzt**, **Neu positioniert** oder **Mit Referenz verglichen**. Du kannst einen **Referenzmesswert** und eine Notiz hinzufügen.
4. Tippe auf **Sondenpflege erfassen**.

Die Wasserwert-Ansicht zeigt dann, wie lange es her ist, dass diese Sonde kalibriert wurde. Sondenpflege eignet sich auch gut als wiederkehrende [Wartungsaufgabe](/help/mobile-maintenance).

:::note Kalibrierdaten erklären Abweichungen
Widersprechen sich eine Sonde und ein Testkit, prüf, wann du die Sonde zuletzt kalibriert hast. Das ist meist die Antwort.
:::
