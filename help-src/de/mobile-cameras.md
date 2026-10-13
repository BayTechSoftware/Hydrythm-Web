---
title: Kameras und Skimmer-Wächter
description: Eine Wyze-, Tapo-, Sonoff- oder andere RTSP-Kamera zu Cora hinzufügen, dein Becken auf einer Kachel oder im Vollbild ansehen und dich vom Skimmer-Wächter warnen lassen, bevor der Abschäumerbecher überläuft.
section: Cora Mobile
reviewed: 2026-10-13
order: 17
group: Equipment
---

:::note Beta
**Beta.** Kameras sind in der Beta und nur für Beta-Nutzer offen. Wenn du kein Beta-Nutzer bist, siehst du sie nicht unter **Gerät hinzufügen**. Für Beta-Zugang wende dich an den [Support](/support.html). Mehr dazu unter [Beta-Funktionen](/help/mobile-beta).
:::

Füg eine Kamera hinzu, um dein Becken in Cora zu sehen, auf dem Handy und auf Cora Max, und damit der Skimmer-Wächter den Abschäumerbecher im Auge behält. Fang bei **Geräte → Gerät hinzufügen → Kamera** an. Eine Kamera braucht ein Cora Max am Becken, deshalb zeigt die Zeile **Kamera** **Erfordert Cora Max**, bis das Becken eins hat.

## Eine Kamera hinzufügen {#adding-a-camera}

1. Geh zu **Geräte → Gerät hinzufügen → Kamera** und dann zu **Kamera hinzufügen**.
2. Wähl den Typ: Wyze, Tapo, Sonoff oder **Andere Kamera (RTSP)**.
3. Folge den Schritten, die Cora für diesen Typ zeigt. Sie sagen dir, was du zuerst in der eigenen App der Kamera einschalten musst.
4. Trag Name, Stream-Adresse, Benutzername, Passwort und Becken ein und tippe auf **Verbindung testen**. Antwortet die Kamera, tippe auf **Kamera hinzufügen**.

Dein Handy muss beim Hinzufügen im selben WLAN sein wie die Kamera. Die Adresse muss in deinem Heimnetz liegen, und Benutzername und Passwort gibst du in ihren eigenen Feldern ein, nicht in der Adresse.

Kameras von Wyze, Tapo und Sonoff wurden getestet (Wyze Cam v4, Tapo C120 und Sonoff Cam S3W). Andere Kameras mit RTSP funktionieren vielleicht auch.

| Kamera | Das zuerst einschalten |
|---|---|
| Wyze | Öffne in der Wyze-App die Kamera, dann Einstellungen, Erweiterte Einstellungen, RTSP. Schalte RTSP ein, wähl einen Benutzernamen und ein Passwort und starte die Kamera dann neu. Die Kamera braucht Firmware 4.52.17 oder neuer. |
| Tapo | Öffne in der Tapo-App Einstellungen, Erweiterte Einstellungen, Kamerakonto und leg einen Benutzernamen und ein Passwort an. Das ist nicht dein TP-Link-Konto. Eine Tapo-Kamera kann von Tapo Care, Aufnahme auf SD-Karte und Streaming an andere Apps nur zwei gleichzeitig. |
| Sonoff | Schalte in eWeLink RTSP für die Kamera ein und leg ihr Konto fest. Cora füllt dir eine Vorgabe **Sonoff-Adresse** aus. |
| Andere Kamera (RTSP) | Schalte RTSP oder ONVIF in der App der Kamera ein, leg ein Kamera-Login fest und gib die Stream-Adresse aus ihrer Anleitung ein. Lass das Login leer, wenn deine Kamera keins hat. |

## Eine Kamera ändern {#changing-a-camera}

Öffne die Kamera und nutze ihr Menü: **Umbenennen**, **Adressen bearbeiten**, **Passwort ändern** oder **Kamera entfernen**. Beim Entfernen wird auch ihr gespeichertes Passwort gelöscht.

## Zuschauen {#watching-it}

![Eine Kameraseite](img/mobile-camera.webp "Die Kameraseite, oben das Bild, darunter die Karte Skimmer-Wächter.")

Eine Kamera kann eine Kachel auf deinem Dashboard sein, bis zu 3×2 groß. Siehe [Dein Dashboard bearbeiten](/help/mobile-dashboard-editing). Öffne sie für **Vollbild** und **Drehen**.

Zu Hause, mit deinem Handy im WLAN der Kamera, spielt Cora **Live-Video** direkt von der Kamera ab. Unterwegs, oder wenn du **Standbilder** wählst, nimmt dein Cora Max Standbilder von der Kamera auf, und Cora zeigt sie fast live, alle paar Sekunden aktualisiert. Schickt Cora Max keine Bilder, sagt das die Kachel.

## Skimmer-Wächter {#skimmer-watch}

:::note Beta
**Beta.** Der Skimmer-Wächter ist in der Beta und nur für Beta-Nutzer offen. Außerdem braucht er ein kostenpflichtiges Abo. Ohne eins sagt die Karte **Skimmer-Wächter gehört zu den kostenpflichtigen Plänen.** und bietet **Pläne ansehen** an. Für Beta-Zugang wende dich an den [Support](/support.html).
:::

Der Skimmer-Wächter beobachtet den Auffangbecher des Abschäumers über eine Kamera und warnt dich, bevor er überläuft. Er sitzt auf der Seite der Kamera, in der Karte **Skimmer-Wächter**.

![Den Becher markieren](img/mobile-camera-mark-cup.webp "Zieh den Rahmen über den Becher: untere Kante auf den Boden des Bechers, obere Kante knapp unter den Rand.")

1. Richte die Kamera auf den Becher und schalte **Becher überwachen** ein.
2. Tippe auf **Becher markieren**. Zieh den Rahmen über den Becher und pass ihn an den Ecken an: die untere Kante auf den Boden des Bechers, die obere Kante knapp unter den Rand, dort, wo der Becher voll ist. Später heißt die Taste **Becherrahmen anpassen**.
3. Leer den Becher und tippe auf **Becher ist jetzt leer**. Cora macht ein Bild des leeren Bechers zum Vergleich. Das dauert etwa 10 Sekunden. Bewegst du die Kamera oder den Rahmen, mach das noch einmal.
4. Zieh den Schieberegler **Warnung bei** auf den Füllstand, bei dem du gewarnt werden willst. Lass etwas Spielraum, denn Cora prüft alle 15 Minuten.

![Die Karte Skimmer-Wächter auf einer Kameraseite](img/mobile-skimmer-watch.webp "Becher ist jetzt leer, der letzte Messwert, die letzten 24 Stunden, Jetzt prüfen und die Kamera-Tipps.")

Cora Max prüft den Becher alle 15 Minuten. Die Karte zeigt den letzten Messwert und wie lange er her ist, und die Kamerakachel auf deinem Dashboard zeigt den Füllstand ebenfalls. **Jetzt prüfen** prüft den Becher sofort, das dauert etwa 10 Sekunden. **Letzte 24 Stunden** zeigt, wie sich der Becher über den Tag gefüllt hat.

Erreicht der Becher deinen Wert unter **Warnung bei**, bekommst du eine Benachrichtigung. Sie kommt unter **Gerätefehler**, lass diese Kategorie unter [Benachrichtigungen](/help/mobile-notifications) also eingeschaltet. Sobald du den Becher geleert hast, kann die Warnung wieder auslösen.

### Wenn der Messwert falsch aussieht {#skimmer-watch-problems}

| Die Karte sagt | Was du tust |
|---|---|
| **Licht hinter dem Becher zu hell** | Schalte das Licht hinter dem Becher aus oder stell es um. Siehe die Kamera-Tipps unten |
| **Nicht sicher (geringe Sicherheit)** | Das Bild war schwer zu lesen. Prüf die Kamera-Tipps und tippe dann auf **Jetzt prüfen** |
| **Markieren Sie zuerst den Becher** | Tippe auf **Becher markieren** und zeichne den Rahmen |
| **Nicht kalibriert: Becher leeren und auf Becher ist jetzt leer tippen** | Leer den Becher und tippe dann auf **Becher ist jetzt leer** |
| **Rahmen verschoben: erneut kalibrieren** | Du hast den Rahmen verschoben. Leer den Becher und tippe noch einmal auf **Becher ist jetzt leer** |
| **Cora Max konnte kein Bild der Kamera abrufen.** | Prüf, ob die Kamera an ist und ob das Cora Max des Beckens online ist |
| **Die letzte Prüfung ist fehlgeschlagen.** | Tippe auf **Jetzt prüfen**. Schlägt es weiter fehl, siehe [Problembehebung](/help/troubleshooting) |
| **Noch keine Messung. Cora Max prüft alle 15 Minuten.** | Warte auf die erste Prüfung oder tippe auf **Jetzt prüfen** |

### Kamera-Tipps {#camera-tips}

**Kamera-Tipps** auf der Karte gibt dir denselben Rat wie hier.

- Stell die Nachtsicht der Kamera auf An (immer Infrarot), nicht auf Auto, damit jedes Bild bei Tag und Nacht gleich aussieht.
- Stell das Spotlight der Kamera auf Manuell und lass es aus. Blasen und Wasser im Technikbecken zählen als Bewegung und schalten es ständig ein.
- Lass kein starkes Licht von hinter dem Becher direkt auf die Kamera scheinen.

### Auf Cora Max {#skimmer-watch-on-cora-max}

![Kamerakacheln auf Cora Max, eine zeigt den Füllstand des Abschäumerbechers](img/max-skimmer-watch.webp "Auf Cora Max zeigt die Kamerakachel den Füllstand des Bechers und wie alt er ist.")

Auf Cora Max zeigen die Kamerakachel und die Vollbild-Kamera **Becher** mit dem Füllstand und wie alt der Messwert ist. Der Chip wird bernsteinfarben, wenn der Becher bis auf 10 Punkte an deinen Warnwert herankommt, und rot, wenn er ihn erreicht. In der Vollbild-Kamera öffnet die Taste **Alarm bei** das Fenster **Alarm für den Abschäumerbecher**, wo du den Wert ebenfalls ändern kannst. Während eine Prüfung läuft, kann das Live-Bild ein paar Sekunden anhalten. Mehr dazu unter [Ausrüstung mit Cora Max steuern](/help/max-device-control).

## Was mit den Bildern passiert {#pictures}

Zu Hause wird das Video direkt von der Kamera abgespielt und nicht aufgezeichnet. Unterwegs wird pro Kamera nur ein Standbild behalten, und jedes neue ersetzt das letzte. Der Skimmer-Wächter behält das neueste Bild des markierten Bechers, die Füllstände der letzten 24 Stunden (nur Zahlen) und ein kleines Bild des leeren Bechers. Sie werden gelöscht, wenn du die Kamera entfernst oder dein Konto löschst. Alle Details stehen in der [Datenschutzerklärung](/privacy-policy.html).
