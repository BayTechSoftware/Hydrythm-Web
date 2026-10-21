---
title: Verbrauchsmaterial und Nachfüllwarnungen
description: Nachfüllwarnungen für Reagenz, Dosierbehälter, Reservoirs der Nachfüllanlage und Filterrollen festlegen und Cora sagen, wenn du nachgefüllt hast.
section: Cora Mobile
reviewed: 2026-10-13
order: 16
group: Equipment
---

Mit Nachfüllwarnungen warnt dich Cora, bevor Reagenz, Dosierflüssigkeit, Nachfüllwasser oder die Filterrolle ausgeht. Öffne das Gerät unter **Geräte** (oder tippe auf seine Kachel auf dem Dashboard) und tippe dann oben in der Leiste auf die **Glocke**.

## Eine Nachfüllwarnung festlegen {#setting-a-refill-alert}

![Das Fenster Warnungen für ein ReefDose 4, mit einem Schwellenwert für die verbleibenden Tage und einem Schalter für jeden Kopf](img/mobile-consumables.webp "Ein Schwellenwert pro Kopf, jeder mit seinem eigenen Schalter.")

Das Fenster heißt **Warnungen:** gefolgt vom Namen des Geräts. Hat die Ausrüstung mehr als einen Behälter, bekommt jeder seinen eigenen Schwellenwert und seinen eigenen Schalter, ein Kopf, den du genau beobachtest, und einer, den du kaum anfasst, lassen sich also unterschiedlich einstellen. Schaltest du einen Schalter aus, bleibt der Wert für später erhalten.

Wo du es einstellst:

- **Die meisten Geräte**: die Glocke in der oberen Leiste der Geräteseite.
- **DŌS**: die Karte **Warnungen** auf der DŌS-Seite oder die Glocke. Siehe [Dosierpumpen-Warnungen](/help/mobile-device-control#doser-alerts).
- **AquaWiz-Dosierpumpen**: ihre Regel im Tab **Regeln** der [Warnzentrale](/help/mobile-alerts).

Die meisten Schwellenwerte sind in Tagen, nicht in Volumen. Cora rechnet aus, wie lange der Rest bei deinem Verbrauch noch reicht. "Calcium für vier Tage übrig" ist etwas, womit du arbeiten kannst. "180 ml übrig" nicht.

## Wovor du gewarnt werden kannst {#thresholds}

| Gerät | Schwellenwert | Startet bei |
|---|---|---|
| Trident | **Verbleibende Tests** (das niedrigste Reagenz) | 10 Tests |
| Trident | **Abfallflasche** (eine volle Flasche lässt den nächsten Test scheitern) | 85 % voll |
| DŌS-Kopf | *[Kopf] · Tage übrig* | 7 Tage |
| DŌS-Kopf | *[Kopf] · verbleibend*, in ml | 100 ml |
| DŌS-Kopf, der altes Wasser abpumpt | **Verbleibender Platz im Abfallbehälter** | |
| DŌS-Kopf | **Warnungen bei verpasster Dosierung** (ein Schalter) | |
| ReefDose-Kopf | Tage, die das Supplement noch reicht | 7 Tage |
| ReefATO+ | **Restlaufzeit des Behälters**, geschätzt aus dem jüngsten Nachfüllverbrauch | 2 Tage |
| ReefMat | **Verbleibende Rolle**, geschätzt daraus, wie schnell die Rolle vorrückt | 3 Tage |
| AquaWiz | Verbleibender Alkalinitäts-Zusatz | Die am Controller eingestellte Warnstufe (100 ml, wenn er keine meldet) |


Eine Verbrauchsmaterial-Warnung funktioniert wie jede andere Warnung. Sie erscheint in der [Warnzentrale](/help/mobile-alerts) und kann eine Push-Nachricht an dein Handy schicken. Du bekommst **eine** Benachrichtigung, wenn ein Stand unterschritten wird, und sie verschwindet, wenn der Stand wieder über dem Schwellenwert liegt.

## Einen Schwellenwert wählen {#choosing-a-threshold}

Stell ihn früh genug ein, dass dir Zeit zum Handeln bleibt. Löst er an dem Tag aus, an dem etwas leer wird, ist er gar keine Warnung.

:::warning Manche Ausrüstung läuft weiter, wenn sie leer ist
Ein DŌS-Kopf mit leerem Behälter arbeitet seinen Zeitplan weiter ab und meldet Dosierungen, die er nie abgegeben hat. Er hat keine eigene Warnung bei niedrigem Stand. Eine Nachfüllwarnung ist der Weg, das zu erwischen, leg also für jeden Kopf, aus dem du dosierst, eine fest.
:::

## Nach dem Nachfüllen {#after-refilling}

Sag es Cora auf der Seite des Geräts, damit die Warnung verschwindet und die nächste Warnung vom richtigen Stand aus berechnet wird.

| Gerät | Tippe auf |
|---|---|
| DŌS-Kopf | **Befüllen**, dann **Voll**, oder stell **Verbleibendes Volumen** ein |
| DŌS-Abfallbehälter | Setz seinen freien Platz nach dem Leeren auf voll zurück |
| ReefDose-Kopf | **Rest in der Flasche** |
| ReefMat | **Neue Rolle**, nachdem du eine neue Rolle eingelegt hast |

Trident, ReefATO+ und AquaWiz melden ihren Stand selbst, in Cora musst du also nichts zurücksetzen.
