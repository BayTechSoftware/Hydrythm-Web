---
title: Updates und Wiederherstellung
description: Wie sich Cora Max selbst aktualisiert und was passiert, wenn ein Update schiefgeht.
section: Cora Max
reviewed: 2026-09-09
order: 14
group: Settings
---

## Automatische Updates

Cora Max hält sich selbst auf dem neuesten Stand. Neue Versionen laden im Hintergrund, installieren sich selbst, und du erfährst, was sich geändert hat.

Du musst dafür nichts tun.

## Die Version prüfen

![Geräteeinstellungen](img/max-updates.webp "Firmware-Update, im Abschnitt Netzwerk & Updates der Cora Max-Einstellungen.")

Unter **Einstellungen → Cora Max-Einstellungen → Firmware-Update** (im Bereich **Netzwerk & Updates**) suchst du nach Updates, installierst sie und wählst den Update-Kanal und seinen Zeitplan. Weiter unten auf derselben Seite zeigt der Bereich **Status** für jedes Becken den Abfragestatus, die letzte Abfrage und das letzte Schreiben in die Cloud.

## Wenn ein Update bereitsteht

Es erscheint ein Hinweis, was neu ist, mit zwei Möglichkeiten:

- **Jetzt aktualisieren**: installiert sofort und startet neu
- **3 Stunden schlummern**: fragt später noch einmal

Tust du nichts, installiert sich das Update über Nacht, etwa zwischen 3 und 5 Uhr morgens. So startet der Bildschirm nicht neu, während du davorstehst.

:::note Bei einem Update gehen keine Messwerte verloren
Deine Daten liegen in deinem Konto und nicht auf dem Bildschirm. Nach dem Neustart sind dieselben Becken, Dashboards und Verläufe wieder da.
:::

## Wiederherstellung

Die Wiederherstellung ist ein Wartungsmodus. Du brauchst ihn, wenn das Gerät nicht normal startet oder du seine Einrichtung ohne Laptop reparieren willst.

Um hineinzukommen, hältst du **fünf Finger** etwa **zehn Sekunden** lang oben rechts auf den Bildschirm und gibst dann die **Wiederherstellungs-PIN** des Geräts ein.

Die sechsstellige PIN wurde beim Koppeln angezeigt. Du findest sie auch in den Einstellungen des Geräts in Cora Mobile. Auf Cora Max selbst steht sie nirgends, und das ist Absicht. So kommen weder Gäste noch ein Kind, das sich an den Bildschirm lehnt, in die Wiederherstellung.

In der Wiederherstellung kannst du:

- die **WLAN**-Verbindung reparieren
- das Gerät **neu** mit deinem Konto **koppeln**
- ein **Firmware-Update** erzwingen
- das Gerät auf **Werkseinstellungen zurücksetzen**

Startet ein Gerät mehrmals hintereinander nicht, kann es auch von selbst zur vorherigen Version zurückkehren.

:::warning In der Wiederherstellung steuert der Bildschirm nichts
Dein Controller läuft mit seiner eigenen Programmierung weiter. Eine [Automation](/help/mobile-automation), deren Aktion **dieses Cora Max** ausführen muss, kann aber nicht laufen, solange es in der Wiederherstellung ist. Die Regel löst aus, doch der Schritt kommt nicht bei der Hardware an.
:::

## Wenn ein Gerät nicht neu startet

Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** mit der Version, die auf dem Bildschirm steht, und dem, was dort angezeigt wird. Kopple das Gerät vorher nicht neu. Am Kopplungsstatus lässt sich oft ablesen, was passiert ist.
