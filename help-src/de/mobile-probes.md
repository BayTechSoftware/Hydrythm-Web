---
title: Sonden
description: Ordne die Sonden deines Controllers Cora-Wasserwerten zu, und erfasse Kalibrierung und Reinigung.
section: Cora Mobile
reviewed: 2026-09-09
order: 13
group: Equipment
---

Ein Controller meldet Sonden unter seinen eigenen Namen. Die Sondenzuordnung sagt Cora, welche davon deine pH-Sonde ist, welche Temperatur ist, und so weiter.

## Sonden zuordnen

Öffne dein **Beckenprofil** (der Stift oben auf dem Dashboard), erweitere den Bereich deines Controllers, und wähle **Sondenzuordnung**.

![Sondenzuordnung](img/mobile-probes.webp "Jede von deinem Controller gemeldete Sonde, ihr Live-Messwert, und was Cora mit ihr macht.")

Jede von deinem Controller gemeldete Sonde wird mit ihrem aktuellen Messwert aufgelistet. Cora erkennt die Standardnamen automatisch, und die Zeile zeigt, welchen sie zugeordnet hat, daher besteht die Aufgabe hier meist darin, die zu korrigieren, die es nicht einordnen konnte, statt alle von Hand zuzuordnen.

Jede Zeile bietet drei Möglichkeiten:

- **Einen Cora-Wasserwert**: den Wasserwert, den diese Sonde misst.
- **Eigen**: für eine Sonde, für die Cora keinen Standard-Wasserwert hat. Du gibst ihr ein kurzes Kürzel in Großbuchstaben, und sie wird unter diesem Namen verfolgt.
- **Ignorieren**: für Sonden, die du gar nicht erfassen willst.

Eine ignorierte oder nicht zugeordnete Sonde erscheint auf keinem Dashboard und speist keine Warnungen.

Zuordnungen wirken sich ab dem nächsten erfassten Messwert aus, daher schreibt eine Korrektur hier die Historie nicht neu; sie ändert, was ab diesem Zeitpunkt gespeichert wird. Tippe auf **Speichern**, um sie anzuwenden.

:::warning Eine nicht zugeordnete Sonde ist für Cora unsichtbar
Wenn ein Wasserwert keine Messwerte zeigt, obwohl die Sonde funktioniert, prüfe zuerst die Zuordnung.
:::

## Mehrere Sonden für einen Wasserwert

Ein System mit zwei Temperatursonden kann beide zuordnen. Cora behält sie als getrennte Quellen; die Quelleinstellung des Widgets entscheidet, welcher eine Kachel folgt, und [die Wasserwert-Ansicht](/help/mobile-metric-detail) lässt dich sie vergleichen.

## Sondenpflege erfassen

Sonden weichen ab. Cora kann verfolgen, wann jede zuletzt kalibriert oder gereinigt wurde, damit du eine echte Veränderung von einer Sonde unterscheiden kannst, die Aufmerksamkeit braucht.

Erfasse Kalibrierung oder Reinigung über den Eintrag der Sonde. Das passt auch gut als wiederkehrende [Wartungsaufgabe](/help/mobile-maintenance).

:::note Die Kalibrierhistorie erklärt Widersprüche
Wenn sich eine Sonde und ein Testkit widersprechen, ist das Datum der letzten Kalibrierung der Sonde meist das Erste, das es sich zu prüfen lohnt.
:::
