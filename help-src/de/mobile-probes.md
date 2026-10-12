---
title: Parameterzuordnung
description: Sieh, welche Sonde jeden Messwert liefert, egal bei welchem Controller, und halte Kalibrierung und Reinigung fest.
section: Cora Mobile
reviewed: 2026-10-12
order: 13
group: Equipment
---

Hast du mehr als einen Controller, oder zwei Sonden, die dasselbe messen, muss Cora wissen, welchem Messwert es vertrauen soll. Genau dafür ist die **Parameterzuordnung** da, und dort legst du auch fest, wofür jede Sonde überhaupt steht.

Geh zu **Einstellungen**, öffne das Becken und wähl **Parameterzuordnung**. Sie steht zwischen **Becken bearbeiten** und **Warnschwellen**. Der Stift oben auf dem Dashboard öffnet **Becken bearbeiten**, und dort gibt es sie nicht. Du erreichst sie auch über die Geräteseiten von Neptune Apex und GHL (Beta). GHL steht nur Beta-Nutzern offen. Siehe [Beta-Funktionen](/help/mobile-beta).

Der Bildschirm hat ein Suchfeld (**Parameter suchen**) und zwei Tabs, **Zuordnung** und **Quellen**. Die Suche sieht auf Wasserwertnamen, Sondennamen, Geräte und Marken. Dasselbe Suchfeld gibt es in jeder Wasserwert-Auswahl.

## Woher jeder Messwert kommt

Das ist der Tab **Quellen**.

![Woher jeder Messwert kommt](img/mobile-probes.webp "Jeder Wasserwert, welche Sonde ihn gerade liefert, und eine Schaltfläche zum Ändern.")

In diesem Abschnitt stehen alle Wasserwerte, die Cora für dieses Becken verfolgt, etwa pH oder Temperatur, und dazu, welche Sonde sie gerade liefert.

Tippe auf einen Wasserwert, um jede Sonde zu sehen, die ihn meldet, über alle verbundenen Controller hinweg. Zu jeder stehen ihre Marke, ihr eigener Name für die Sonde und ihr Live-Messwert. Wähl eine aus, um sie festzulegen, oder wähl **Automatisch (neueste Messung gewinnt)**, damit Cora die Sonde nutzt, die zuletzt gemeldet hat. Die anderen bleiben im Verlauf.

Ein Zusatz neben jedem Wasserwert zeigt, was gerade gilt: **Automatisch**, oder **Von dir gewählt**, sobald du eine Sonde festgelegt hast.

Meldet sich eine festgelegte Sonde nicht mehr, zeigt Cora, wann sie zuletzt gemeldet hat, und bietet **Zurück zu Automatisch** an. So kann eine tote Sonde einen Wasserwert nicht dauerhaft blockieren.

Tippe auf **Umbenennen**, um einem Wasserwert einen eigenen Anzeigenamen zu geben. Das ist unabhängig vom Namen, den du der Sonde selbst gibst. Dieser Name erscheint auf deinem Dashboard, in Warnungen und in Reef Buddy.

:::note Ein Lecksensor lässt sich hier nicht neu zuordnen
Der Alarm eines Lecksensors hängt an seinem eigenen Namen, deshalb taucht er in dieser Auswahl nicht auf. Er funktioniert weiterhin wie gewohnt.
:::

## Sonden: Cora sagen, was jede ist

Der Tab **Zuordnung** öffnet zuerst. Er listet alle Sonden, die Cora kennt, gruppiert nach dem Gerät, das sie meldet, mit ihrem aktuellen Messwert. Die Standardnamen erkennt Cora selbst, und in der Zeile siehst du, welchem Wasserwert es die Sonde zugeordnet hat. Meist musst du also nur die Sonden korrigieren, die Cora nicht einordnen konnte, und nicht alle von Hand zuordnen.

In jeder Zeile hast du drei Möglichkeiten:

- **Einen Cora-Wasserwert**, also den Wert, den diese Sonde misst.
- **Eigen** für eine Sonde, für die Cora keinen Standard-Wasserwert kennt. Du gibst ihr ein kurzes Kürzel in Großbuchstaben, und Cora zeichnet sie unter diesem Namen auf.
- **Ignorieren** für Sonden, die Cora gar nicht aufzeichnen soll.

Eine ignorierte oder nicht zugeordnete Sonde erscheint auf keinem Dashboard und löst keine Warnungen aus.

Eine Zuordnung gilt ab dem nächsten Messwert. Korrigierst du hier etwas, bleibt die Historie also, wie sie ist. Nur was ab jetzt gespeichert wird, ändert sich. Tippe auf **Speichern**, um die Zuordnungen zu übernehmen.

:::warning Eine nicht zugeordnete Sonde sieht Cora nicht
Zeigt ein Wasserwert keine Messwerte, obwohl die Sonde funktioniert, prüf als Erstes ihre Zuordnung.
:::

## Mehrere Sonden für einen Wasserwert

Hast du zwei Temperatursonden, egal ob am selben Controller oder an zweien, ordne beide zu. Cora führt sie als getrennte Quellen, und im Tab **Quellen** legst du fest, welche davon den Wasserwert liefert, oder lässt es auf Automatisch. In der [Wasserwert-Ansicht](/help/mobile-metric-detail) kannst du sie vergleichen.

Melden zwei Quellen denselben Wasserwert, gewinnt die neueste Messung. Ein Wert auf dem Bildschirm wird nur durch einen Messwert mit späterem Messzeitpunkt ersetzt, von welchem Gerät auch immer. Ein älterer Messwert oder ein Gerät, das einen alten noch einmal sendet, landet im Verlauf und überschreibt nicht den aktuellen Wert. Hast du eine Quelle festgelegt, folgt Cora stattdessen dieser Quelle.

## Sondenpflege festhalten

Sonden driften mit der Zeit. Cora kann festhalten, wann du jede zuletzt kalibriert oder gereinigt hast. So erkennst du, ob sich wirklich etwas im Becken ändert oder ob eine Sonde Pflege braucht.

Kalibrierung oder Reinigung trägst du beim Eintrag der Sonde ein. Das passt auch gut als wiederkehrende [Wartungsaufgabe](/help/mobile-maintenance).

:::note Die Kalibrierhistorie erklärt Abweichungen
Zeigen Sonde und Testkit unterschiedliche Werte, schau zuerst nach, wann du die Sonde zuletzt kalibriert hast.
:::
