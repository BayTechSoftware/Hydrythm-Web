---
title: Updates und Wiederherstellung
description: Wie sich Cora Max selbst aktualisiert, Installationsfenster und Update-Kanal, die Version prüfen, die Wiederherstellungs-PIN und was du tust, wenn Cora Max nicht startet oder einen Support-Code zeigt.
section: Cora Max
reviewed: 2026-10-13
order: 15
group: Settings and account
---

Cora Max hält sich selbst aktuell. Diese Seite erklärt, wann Updates installiert werden, wie du deine Version prüfst und wie du Cora Max wieder zum Laufen bringst, wenn es nicht normal startet.

## Automatische Updates

Neue Versionen laden im Hintergrund, sobald sie erscheinen. Sie installieren sich im **Installationsfenster**, 3 bis 5 Uhr morgens, außer du änderst es, damit der Bildschirm nicht neu startet, während du draufschaust. Bringt eine Version Versionshinweise mit, zeigt Cora Max sie an.

Du musst nichts tun, um aktuell zu bleiben.

## Die Version und die Update-Einstellungen prüfen

![Netzwerk und Updates auf Cora Max](img/max-updates.webp "Firmware-Update, im Bereich NETZWERK & UPDATES der Cora Max-Einstellungen.")

Deine Version steht auf der Karte oben unter **Einstellungen → Cora Max-Einstellungen** (*Cora Max · Firmware 0.28.170*) und unter **HILFE & ÜBER → Über**.

**Einstellungen → Cora Max-Einstellungen → Firmware-Update** (in **NETZWERK & UPDATES**) zeigt die Version, die du hast, und ob ein Update wartet. Tippe auf **Nach Updates suchen**, um jetzt nachzusehen, oder auf **Herunterladen & installieren**, wenn eins da ist.

Unter **Update-Einstellungen** auf demselben Bildschirm:

- **Installationsfenster** legt die Stunden fest, in denen sich Updates installieren dürfen, mit einer Zeit für **Start** und **Ende**, in der Ortszeit dieses Bildschirms. Die Zeitzone stellst du in Cora Mobile ein, unter **Geräte →** dein Cora Max **→ Zeitzone**.
- **Update-Kanal** ist **Stabil** oder **Beta**. Lass ihn auf **Stabil**, außer der Support bittet dich, zu wechseln. Ein Cora Max auf **Beta** bekommt keine stabilen Versionen.

Um zu sehen, ob dieser Bildschirm deine Geräte abfragt und in Cora Cloud speichert, geh zurück zu **Cora Max-Einstellungen** und scroll zu **STATUS**. Dort stehen für jedes Becken **Abfragestatus**, **Letzte Abfrage**, **Letzter Cloud-Schreibvorgang** und **Cloud-Speichern**.

## Wenn ein Update bereitsteht

Ein Hinweis sagt dir, was neu ist, und gibt dir zwei Möglichkeiten.

- **Jetzt aktualisieren** installiert sofort und startet neu. Das dauert etwa eine Minute. Lass Cora Max am Strom.
- **24 Stunden schlummern** blendet den Hinweis aus und fragt dich einen Tag später noch einmal.

Solange ein Update wartet, zeigt ein kleiner Punkt am Symbol **Einstellungen** in der oberen Leiste und an der Zeile **Firmware-Update**. Der Punkt bleibt auch, wenn du den Hinweis aufschiebst, du siehst also weiter, dass ein Update da ist. Während das Update installiert wird, verschwindet er.

Lässt du es liegen, installiert sich das Update im **Installationsfenster** von selbst.

Du kannst es auch vom Handy aus starten: Öffne in Cora Mobile **Geräte →** dein Cora Max und tippe auf **Auf v… aktualisieren**.

:::note Bei einem Update verlierst du keine Messwerte
Deine Daten liegen in deinem Konto. Wenn Cora Max neu startet, kommt es mit denselben Becken, Dashboards und demselben Verlauf zurück.
:::

## Wiederherstellung {#recovery}

Die Wiederherstellung ist ein Wartungsmodus für den Fall, dass Cora Max nicht normal startet oder du seine Einrichtung ohne Laptop reparieren musst.

1. Halte **fünf Finger** **zehn Sekunden** lang in die obere rechte Ecke des Bildschirms.
2. Das Feld **Wiederherstellungs-PIN** öffnet sich. Gib die 6-stellige PIN ein und tippe auf **Bestätigen**.

Die PIN hast du beim Koppeln von Cora Max gesehen. Du findest sie auch in Cora Mobile unter **Geräte →** dein Cora Max **→ Wiederherstellungs-PIN**. Cora Max selbst zeigt sie nie, damit ein Gast oder ein Kind, das sich an den Bildschirm lehnt, nicht in die Wiederherstellung kommt.

Gibst du dreimal die falsche PIN ein, sperrt sich die Wiederherstellung für 30 Sekunden und nach jedem weiteren falschen Versuch länger. **Zu viele Versuche** sagt dir, wie lange du warten musst. War Cora Max seit dem Koppeln nie online, hat es noch keine PIN und zeigt **Wiederherstellung nicht verfügbar**. Verbinde es zuerst mit dem WLAN.

In der **Wiederherstellung** kannst du:

- **Wi-Fi-Einrichtung wiederholen**: ein neues WLAN und Passwort wählen
- **Dieses Gerät neu koppeln**: die Kopplung löschen und es mit Cora Mobile neu einrichten
- **OTA-Prüfung erzwingen**: jetzt nach Updates suchen
- **Werksreset**: die Kopplung und alle Einstellungen auf dem Bildschirm entfernen

Beckendaten, die schon in Cora Cloud gespeichert sind, bleiben in jedem Fall erhalten.

Startet Cora Max mehrmals hintereinander nicht, kann es sich auch selbst auf die vorherige Version zurücksetzen.

:::note Dieselbe Geste entsperrt die Kindersicherung
Ist die [Kindersicherung](/help/max-settings#child-lock) eingeschaltet, entsperrt das Halten mit fünf Fingern in der Ecke auch den Bildschirm. Tippe im Feld **Wiederherstellungs-PIN** auf **Abbrechen**, wenn du nur entsperren wolltest.
:::

:::warning Ein Bildschirm in der Wiederherstellung steuert nichts
Dein Controller läuft mit seiner eigenen Programmierung weiter. Aber ein Schritt einer [Automation](/help/mobile-automation), den **dieses Cora Max** ausführen muss, kann nicht laufen, solange es in der Wiederherstellung ist. Die Regel löst aus, aber der Schritt erreicht die Ausrüstung nie.
:::

## Wenn Cora Max "Cora Max hit a problem" zeigt

Dieser Bildschirm bedeutet, dass beim Starten oder im Betrieb von Cora Max etwas schiefgegangen ist. Er erscheint auf Englisch und zeigt einen **Support code** (er beginnt mit *CXB-*).

1. Schreib dir den Support-Code auf.
2. Warte. Cora Max startet sich in etwa 10 Minuten selbst neu. Um es sofort neu zu starten, halte fünf Finger 10 Sekunden lang in die obere rechte Ecke.
3. Passiert es immer wieder, schreib eine E-Mail mit dem Support-Code an **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Wenn ein Gerät nicht neu startet

Schreib eine E-Mail an **[cora@coraiq.tech](mailto:cora@coraiq.tech)** mit der Version, die auf dem Bildschirm steht, und der Meldung, die er zeigt. Koppel es vorher nicht neu. Der Kopplungsstatus hilft oft herauszufinden, was passiert ist.
