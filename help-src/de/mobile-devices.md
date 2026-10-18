---
title: Geräte hinzufügen, bearbeiten und entfernen
description: Ausrüstung zu Cora hinzufügen, einem Becken zuweisen, umbenennen, prüfen, ob sie in Ordnung ist, und entfernen, alles im Tab Geräte.
section: Cora Mobile
reviewed: 2026-10-17
order: 11
group: Equipment
twin: max-devices
---

Im Tab **Geräte** fügst du jedes Stück Ausrüstung hinzu, weist es zu, benennst es um, prüfst es und entfernst es. Die Geräte sind nach Marke gruppiert, und du kannst jede Gruppe zuklappen.

![Der Tab Geräte](img/mobile-devices.webp "Ausrüstung ist nach Marke gruppiert. Jede Gruppe lässt sich zuklappen.")

## Ausrüstung hinzufügen {#adding-equipment}

1. Tippe im Tab **Geräte** auf **Gerät hinzufügen**.
2. Wähl die Marke: **Cora**, **Neptune Apex**, **Red Sea**, **Jecod** oder **AquaWiz**.
3. Folge den Schritten der Marke. Je nach Marke ist das ein Netzwerkscan, eine IP-Adresse, eine Anmeldung oder ein Geräteschlüssel. [Deine Ausrüstung verbinden](/help/mobile-connections) hat die Schritte für jede Marke.
4. Wähl das Becken, zu dem es gehört.

![Die Markenliste unter Gerät hinzufügen](img/mobile-add-device-brands.webp "Wähle die Marke des Geräts, das du hinzufügst.")



:::note Ohne Cora Max ist manche Ausrüstung nur lokal
Neptune Apex-, Red Sea- und Jecod-Ausrüstung wird über dein Heimnetz oder Bluetooth erreicht. Ohne Cora Max sagt der Bildschirm zum Hinzufügen *Diese Integration funktioniert ohne Cora Max nur lokal in der Mobile-App.* Dein Handy liest und steuert sie nur, solange es im selben Netzwerk (oder in Bluetooth-Reichweite) ist. Unterwegs siehst du die letzten Messwerte, die dein Handy gespeichert hat, und kannst sie nicht steuern. Ein Cora Max am Becken fragt sie rund um die Uhr ab und leitet deine Befehle weiter. Mehr dazu unter [Deine Ausrüstung verbinden](/help/mobile-connections#local-only).
:::

Fügst du Ausrüstung aus deinem Netzwerk hinzu, muss dein Handy im selben Netzwerk sein wie die Ausrüstung.

### Bluetooth-Kapazität {#bluetooth-capacity}

Ein Cora Max teilt sein Bluetooth unter der gesamten Ausrüstung auf, die es liest, und kommt daher nur bis zu einer Grenze mit. Wenn du eine Jecod-Pumpe hinzufügst, die über Bluetooth verbunden ist, prüft Cora zuerst, wie ausgelastet das Cora Max des Beckens ist. Meist siehst du nichts. Sonst erscheint eine von zwei Meldungen:

- **Bluetooth wird stark ausgelastet**: *Dieses Cora Max nähert sich seinem Bluetooth-Limit. Weitere Geräte werden möglicherweise seltener aktualisiert. Füge ein zweites Cora Max hinzu, wenn du mehr Geräte hinzufügen möchtest.* Tippe auf **Weiter**, um das Gerät trotzdem hinzuzufügen, oder auf **Abbrechen**.
- **Bluetooth-Limit erreicht**: *Dieses Cora Max hat sein Bluetooth-Limit erreicht. Füge für diese Geräte ein zweites Cora Max hinzu.* Das Gerät wird nicht hinzugefügt. Tippe auf **OK**.

Cora prüft das primäre Cora Max des Beckens oder, wenn keins gewählt ist, das Cora Max mit dem meisten Platz. Mehr unter [Mehr als ein Cora-Gerät](/help/mobile-multi-device#primary-cora-max).

## Ein Cora Max koppeln {#pairing-a-cora-max}

![Der Bildschirm Füge dein Cora hinzu in Cora Mobile, der nach Geräten sucht](img/mobile-add-device.webp "Gerät hinzufügen, dann Cora. Cora Mobile sucht in deinem WLAN und über Bluetooth, darunter IP-Adresse manuell eingeben.")

Über **Cora** koppelst du ein neues Cora Max. Es findet Geräte, die schon in deinem WLAN sind, oder Geräte in der Nähe über Bluetooth. Findet es deins nicht, nutze **IP-Adresse manuell eingeben** auf demselben Bildschirm. Die vollständige Anleitung steht unter [Cora Max einrichten](/help/max-setup).

## Die Seite eines Geräts {#a-devices-page}

Tippe auf ein beliebiges Gerät in der Liste, um seine Seite zu öffnen. Zuerst kommen seine Steuerungen, dann Bereiche, die bei jeder Marke gleich funktionieren.

- **Status** zeigt **Modell**, **Seriennummer**, **Firmware** und wann Cora zuletzt von ihm gehört hat (**Zuletzt gesehen**).
- **Becken** zeigt, welchem Becken (oder welchen Becken) es zugewiesen ist. Tippe auf **Ändern**, um es neu zuzuweisen.
- **Verbindung** ist, wo du seine IP-Adresse, Anmeldung oder seinen Geräteschlüssel bearbeitest.
- **Gerät entfernen**, ganz unten.

Cora Max und Neptune Apex können mehr als ein Becken versorgen, deshalb ist ihre Beckenauswahl eine Checkliste. Cora Max kann bis zu vier zugewiesen bekommen. Siehe [Mehr als ein Cora-Gerät](/help/mobile-multi-device). Alles andere versorgt immer ein Becken. Wählst du ein anderes, wandert das Gerät dorthin und verschwindet beim alten.

:::warning Weise das Becken zu, bevor du dich auf die Messwerte verlässt
Ein Gerät ohne Becken meldet trotzdem, aber seine Zahlen landen nirgends. Erscheint ein Gerät, das du gerade hinzugefügt hast, auf keinem Dashboard, prüf das zuerst.
:::

Was die Steuerungen jeder Marke tun, steht unter [Deine Ausrüstung steuern](/help/mobile-device-control).

## Umbenennen {#renaming}

Öffne das Gerät und tippe auf den Stift neben seinem Namen. Nimm den Namen, den du im Alltag benutzt, etwa "Rückförderung", "Gyre links" oder "Heizer Technikbecken". Der Name erscheint auf Widgets, in Warnungen und in allem, was du Cora fragst.

Namen können bis zu 40 Zeichen lang sein. Lass den Namen leer, um zum eigenen Namen des Geräts zurückzukehren. Haben zwei Geräte derselben Art keinen Namen, unterscheidet Cora sie mit einem kurzen Code hinter dem Namen. Eine Seriennummer nutzt Cora nie als Namen.

Der neue Name gilt nur in Cora. Den Namen in der eigenen App des Herstellers ändert er nicht.

## Prüfen, ob ein Gerät in Ordnung ist {#health}

Jedes Gerät ist eine Zeile im Tab Geräte, mit Symbol, Name, Modell und Becken. Der Punkt in der Zeile zeigt seinen Zustand.

| Punkt | Was er bedeutet |
|---|---|
| Grau | Cora weiß es noch nicht |
| Grün | Läuft normal |
| Orange | Eine Warnung oder ein Fehler |
| Rot | Offline |

Für mehr öffne das Gerät. Sein Bereich **Status** zeigt, wann Cora zuletzt von ihm gehört hat. Du willst eine aktuelle Zeit und keine Warnung.

| Was du siehst | Was es bedeutet |
|---|---|
| Eine aktuelle Aktualisierungszeit | Läuft normal |
| "Vor 3 Std. aktualisiert" bei etwas, das nur alle paar Stunden meldet | In Ordnung |
| "… nicht erreichbar" oder "… konnte nicht erreicht werden" | Ein Netzwerkproblem, oder das Gerät ist aus |
| "… hat die Anmeldung abgelehnt" | Das Konto beim Hersteller muss neu verbunden werden. Öffne das Gerät und melde dich erneut an |
| Ältere Messwerte, während du unterwegs bist | Normal für Apex, Red Sea und Jecod ohne Cora Max am Becken (siehe oben) |
| Gar nichts | Es hat nie gemeldet. Prüf die Beckenzuweisung und die Verbindung |

Meldet sich ein Gerät nicht mehr, kann Cora dich warnen. Die Zeiten stehen unter [Warnungen und Schwellenwerte](/help/mobile-alerts). Für alles andere siehe [Problembehebung](/help/troubleshooting).

## Ein Gerät entfernen {#removing-a-device}

Öffne das Gerät und tippe auf **Gerät entfernen**, oder wisch seine Zeile im Tab Geräte nach links. Cora bittet um Bestätigung: *"{name} wird aus Cora entfernt. Das Gerät selbst wird dabei nicht zurückgesetzt oder verändert."*

**Deine Messwerte bleiben erhalten.** Ein Gerät zu entfernen beendet, dass Cora neue Daten von ihm sammelt. Der Verlauf, den es schon gesammelt hat, bleibt beim Becken, und jedes Widget, das es genutzt hat, behält seine vergangenen Messwerte.

Du verlierst die Live-Verbindung. War das Gerät über ein Konto beim Hersteller verbunden, verlierst du auch die gespeicherte Anmeldung, du musst dich also neu anmelden, wenn du es wieder hinzufügst.

:::tip Ein lautes Gerät beruhigen, ohne es zu entfernen
Funktioniert ein Gerät gut, warnt aber zu oft, ändere seine Schwellenwerte oder Benachrichtigungseinstellungen unter [Warnungen und Schwellenwerte](/help/mobile-alerts). Du behältst die Verbindung und die Daten, und der Lärm hört auf.
:::
