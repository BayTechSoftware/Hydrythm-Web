---
title: Kameras und Skimmer-Wächter
description: Füge eine Wyze-, Tapo-, Sonoff- oder andere RTSP-Kamera zu Cora hinzu, sieh sie als Kachel oder im Vollbild an und lass dich vom Skimmer-Wächter warnen, bevor der Skimmerbecher überläuft.
section: Cora Mobile
reviewed: 2026-10-12
order: 35
group: Equipment
---

:::note Beta
**Beta.** Kameras sind in der Beta und nur für Beta-Nutzer offen. Bist du keiner, siehst du sie nicht unter **Gerät hinzufügen**. Für Beta-Zugang wende dich an den [Support](/support.html).
:::

Füg eine Kamera hinzu, um dein Becken in Cora zu sehen, auf dem Handy und auf dem Cora Max. Eine Kamera braucht ein Cora Max am Becken, deshalb zeigt die Zeile **Kamera** **Erfordert Cora Max**, bis das Becken eines hat.

## Eine Kamera hinzufügen

1. Geh zu **Geräte → Gerät hinzufügen → Kamera**, dann **Kamera hinzufügen**.
2. Wähl den Typ: Wyze, Tapo, Sonoff oder **Andere Kamera (RTSP)**.
3. Folge den Schritten, die Cora für diesen Typ zeigt. Sie sagen dir, was du zuerst in der App der Kamera einschalten musst.
4. Trag Name, Stream-Adresse, Benutzername, Passwort und Becken ein und tippe auf **Verbindung testen**. Antwortet die Kamera, tippe auf **Kamera hinzufügen**.

Dein Handy muss beim Hinzufügen im selben WLAN sein wie die Kamera. Die Adresse muss in deinem Heimnetz liegen, und Benutzername und Passwort trägst du in ihre eigenen Felder ein, nicht in die Adresse.

Kameras von Wyze, Tapo und Sonoff wurden getestet (Wyze Cam v4, Tapo C120 und Sonoff Cam S3W). Andere Kameras mit RTSP funktionieren vielleicht auch.

| Kamera | Das zuerst einschalten |
|---|---|
| Wyze | Öffne in der Wyze-App die Kamera, dann Einstellungen, Erweiterte Einstellungen, RTSP. Schalte RTSP ein, wähl einen Benutzernamen und ein Passwort und starte die Kamera neu. Die Kamera braucht Firmware 4.52.17 oder neuer. |
| Tapo | Öffne in der Tapo-App Einstellungen, Erweiterte Einstellungen, Kamerakonto und leg einen Benutzernamen und ein Passwort an. Das ist nicht dein TP-Link-Konto. Eine Tapo-Kamera kann von Tapo Care, SD-Karten-Aufnahme und Streaming zu anderen Apps nur zwei gleichzeitig nutzen. |
| Sonoff | Schalte in eWeLink RTSP für die Kamera ein und lege ihr Konto fest. Cora füllt dir eine Vorlage **Sonoff-Adresse** aus. |
| Andere Kamera (RTSP) | Schalte RTSP oder ONVIF in der App der Kamera ein, leg ein Kamera-Login fest und trag die Stream-Adresse aus ihrer Anleitung ein. Lass das Login leer, wenn deine Kamera keins hat. |

## Eine Kamera ändern

Öffne die Kamera und nutze ihr Menü: **Umbenennen**, **Adressen bearbeiten**, **Passwort ändern** oder **Kamera entfernen**. Beim Entfernen wird auch ihr gespeichertes Passwort gelöscht.

## Zuschauen

Eine Kamera kann eine Kachel auf deinem Dashboard sein, bis zu 3×2 groß, und du kannst sie für **Vollbild** und **Drehen** öffnen.

Zu Hause, mit deinem Handy im WLAN der Kamera, spielt Cora **Live-Video** direkt von der Kamera ab. Unterwegs, oder wenn du **Standbilder** wählst, nimmt dein Cora Max Standbilder von der Kamera auf, und Cora zeigt sie als fast live, alle paar Sekunden aktualisiert. Schickt Cora Max keine Bilder, sagt das die Kachel.

## Skimmer-Wächter

:::note Beta
**Beta.** Der Skimmer-Wächter ist in der Beta und nur für Beta-Nutzer offen. Außerdem braucht er einen kostenpflichtigen Tarif: **Skimmer-Wächter gehört zu den kostenpflichtigen Plänen.** Für Beta-Zugang wende dich an den [Support](/support.html).
:::

Der Skimmer-Wächter beobachtet den Auffangbecher des Skimmers mit einer Kamera und warnt dich, bevor er überläuft. Du findest ihn auf der Seite der Kamera, in der Karte **Skimmer-Wächter**.

1. Richte die Kamera auf den Becher und schalte **Becher überwachen** ein.
2. Tippe auf **Becher markieren**. Zieh den Rahmen über den Becher und passe ihn an den Ecken an: die untere Kante auf den Boden des Bechers, die obere Kante knapp unter den Rand, dort, wo der Becher voll ist.
3. Leere den Becher und tippe auf **Becher ist jetzt leer**. Cora macht ein Bild des leeren Bechers als Vergleich. Das dauert etwa 10 Sekunden. Bewegst du die Kamera oder den Rahmen, mach es noch einmal.
4. Stell **Warnung bei** auf den Füllstand ein, bei dem du gewarnt werden willst. Die Karte zeigt ihn in Prozent.

Cora Max prüft den Becher alle paar Minuten. Die Karte zeigt den letzten Messwert und wie lange er her ist. **Jetzt prüfen** fordert sofort eine Prüfung an, das dauert etwa 10 Sekunden. **Letzte 24 Stunden** zeigt, wie sich der Becher über den Tag gefüllt hat.

Ist das Bild schwer zu lesen, sagt das die Karte, zum Beispiel **Licht hinter dem Becher zu hell**.

### Kamera-Tipps

**Kamera-Tipps** auf der Karte gibt dir denselben Rat wie hier.

- Stell die Nachtsicht der Kamera auf An (immer Infrarot), nicht auf Auto, damit jedes Bild bei Tag und Nacht gleich aussieht.
- Stell den Scheinwerfer der Kamera auf Manuell und lass ihn aus. Blasen und Wasser im Technikbecken zählen als Bewegung und schalten ihn ständig ein.
- Lass starkes Licht nicht von hinter dem Becher direkt auf die Kamera scheinen.

## Was mit den Bildern passiert

Zu Hause wird das Video direkt von der Kamera abgespielt und nicht aufgezeichnet. Unterwegs wird pro Kamera nur ein einziges Standbild gespeichert, und jedes neue ersetzt das letzte. Der Skimmer-Wächter speichert das neueste Bild des markierten Bechers, die Füllstände der letzten 24 Stunden (nur Zahlen) und ein kleines Bild des leeren Bechers. Sie werden gelöscht, wenn du die Kamera, das Becken oder dein Konto entfernst. Alle Details stehen in der [Datenschutzrichtlinie](/privacy-policy.html) (auf Englisch).
