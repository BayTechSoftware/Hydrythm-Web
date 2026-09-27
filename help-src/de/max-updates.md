---
title: Updates und Wiederherstellung
description: Wie Cora Max sich selbst aktualisiert, und was passiert, wenn ein Update schiefgeht.
section: Cora Max
reviewed: 2026-09-09
order: 14
group: Settings
---

## Automatische Updates

Cora Max hält sich selbst aktuell. Neue Versionen laden im Hintergrund herunter und installieren sich selbst; dir wird gesagt, was sich geändert hat.

Du musst nichts tun, um aktuell zu bleiben.

## Die Version prüfen

![Geräteeinstellungen](img/max-updates.webp "Firmware-Update und Gerätezustand, oben in den Geräteeinstellungen.")

**Einstellungen → Cora Max → Firmware → Firmware-Update** deckt Prüfen, Installieren, den Update-Kanal und dessen Zeitplan ab. **Gerätezustand & Steuerung** steht direkt daneben in derselben Gruppe **Firmware**, und dort liegt die eigene Diagnose des Geräts: einschließlich primärer Abfrage, Geräteverknüpfungen und Sprachantwortgerät.

## Wenn ein Update verfügbar ist

Ein Hinweis erscheint, der beschreibt, was neu ist, mit zwei Optionen:

- **Jetzt aktualisieren**: installiert sofort und startet neu
- **3 Stunden schlummern**: fragt später erneut

Sich selbst überlassen installiert sich ein Update über Nacht, etwa zwischen 3 und 5 Uhr morgens, sodass der Bildschirm nicht neu startet, während du hinschaust.

:::note Messwerte gehen bei einem Update nicht verloren
Daten leben in deinem Konto, nicht auf dem Bildschirm. Ein Gerät, das neu startet, kommt mit denselben Becken, Dashboards und der Historie zurück.
:::

## Wiederherstellung

Wiederherstellung ist ein Wartungsmodus für den Fall, dass ein Gerät nicht normal startet, oder wenn du seine Einrichtung ohne Laptop reparieren musst.

**Um sie zu betreten:** Halte **fünf Finger** oben rechts auf dem Bildschirm für etwa **zehn Sekunden**, und gib dann die **Wiederherstellungs-PIN** des Geräts ein.

Diese sechsstellige PIN wurde beim Koppeln des Geräts angezeigt, und sie steht auch in den Einstellungen dieses Geräts in Cora Mobile. Sie wird nicht auf Cora Max selbst angezeigt, das ist der Sinn: Die Wiederherstellung kann nicht von einem Gast erreicht werden, oder von einem Kind, das sich an den Bildschirm lehnt.

Von der Wiederherstellung aus kannst du:

- Die **WLAN**-Verbindung reparieren
- Das Gerät **neu koppeln** an dein Konto
- Ein **Firmware-Update** erzwingen
- Das Gerät auf **Werkseinstellungen zurücksetzen**

Ein Gerät, das mehrmals in Folge nicht startet, kann sich außerdem selbst auf die vorherige Version zurücksetzen.

:::warning Ein Bildschirm in der Wiederherstellung steuert nichts
Dein Controller läuft weiterhin nach seiner eigenen Programmierung. Aber eine [Automation](/help/mobile-automation), deren Aktion **von diesem Cora Max** ausgeführt werden muss, kann nicht laufen, während es sich in der Wiederherstellung befindet; die Regel löst aus, und der Schritt erreicht die Hardware nicht.
:::

## Wenn ein Gerät nicht neu startet

Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** mit der auf dem Bildschirm angezeigten Version und dem, was sie sagt. Koppel das Gerät nicht zuerst neu; der Kopplungsstatus ist oft hilfreich dabei, herauszufinden, was passiert ist.
