---
title: Mehr als ein Cora-Gerät
description: Wähle, welches Gerät auf Sprache antwortet und welches jedes Becken abfragt.
section: Cora Mobile
reviewed: 2026-09-27
order: 29
group: Account
---

Ein Haushalt kann mehr als ein Cora Max haben. Zwei Einstellungen entscheiden, was welches Gerät tut, damit sie sich nicht doppeln, und eine dritte Sache, die es wert ist zu wissen, ist, was zwischen ihnen überhaupt geteilt wird.

## Was geteilt wird, und was nicht

| Kontoweit geteilt | Gehört zu einem Bildschirm |
|---|---|
| Becken, Messwerte und Historie | Sein Dashboard-Layout |
| Geräte und ihre Einstellungen | WLAN, Helligkeit, Ton |
| Tagebuch, Besatz, Wartung | Wake-Word und Kindersicherung |
| Warnungen, Schwellenwerte, Automationen | Welche Becken dieser Bildschirm zeigt |
| Abos und Nutzung | |

Einen Schwellenwert auf einem Gerät zu ändern, ändert ihn überall. Ein Dashboard umzuordnen tut das nicht; jeder Bildschirm behält sein eigenes Layout, und das Handy und Cora Max teilen sich nie eines.

## Cora Assistant: Antwortgerät

**Einstellungen → Cora Assistant → Antwortgerät** wählt, welches **Cora-Gerät** antwortet, wenn du zum Raum sprichst. Nur eines antwortet, egal wie viele dich hören können; stelle es auf das Gerät, das am nächsten zu deinem üblichen Standort ist.

Das ist eine andere Wahl als Primäres Cora Max unten: Antwortgerät entscheidet, welches Gerät auf deine Sprache antwortet, und Primäres Cora Max entscheidet, welches Gerät die Ausrüstung eines Beckens abfragt. Ein Haushalt mit zwei Tablets möchte diese vielleicht unterschiedlich einstellen.

![Die Sprachantwort-Auswahl](img/mobile-voice-responder.webp "Jedes Gerät zeigt, worauf es hört, und ob es online ist.")

Jedes Gerät in der Liste zeigt die Wake-Phrase, auf die es hört, zusammen mit dem, ob es online ist. **Diese sind nicht alle gleich.** Eine Wake-Phrase ist dem Gerät selbst eintrainiert, daher können unterschiedliche Cora-Modelle auf unterschiedliche hören. Lies die Phrase aus der eigenen Zeile des Geräts, statt anzunehmen, dass sich der Haushalt eine teilt.

:::note Dein Handy ist nicht in dieser Auswahl
Das Handy hört nicht auf eine Wake-Phrase. Du startest ein Gespräch darauf durch Tippen, was immer funktioniert und von dieser Einstellung nicht betroffen ist. Die Auswahl listet nur sprachfähige Cora-Hardware auf.
:::

## Primäres Cora Max

Ausrüstung in deinem Netzwerk wird von einem Cora Max gelesen. Wenn mehr als eines denselben Controller lesen könnte, würden sie ihn sonst parallel abfragen.

**Primäres Cora Max** ist eine Wahl pro Becken, welches Gerät den Controller dieses Beckens liest. Öffne in Cora Mobile das Becken und tippe auf **Primäres Cora Max**.

| Einstellung | Verhalten |
|---|---|
| Ein benanntes Gerät | Es wird das einzige Cora-Gerät, das den Controller abfragt, und bleibt das primäre auch während es offline ist: Andere Cora-Geräte übernehmen nicht. Cora Mobile fragt nur ab, während es offline ist. |
| **Jedes aktive (automatisch)** | Die App und jedes Online-Cora-Gerät teilen sich die Arbeit (der letzte Schreibvorgang gewinnt), sodass ein anderes übernimmt, wenn eines offline geht. Geeignet für einen Haushalt mit einem Gerät, und der sicherere Standard, wenn du dir nicht sicher bist, welches Gerät es besitzen sollte. |

Während ein von dir benanntes Gerät offline ist, läuft ein Befehl, der darüber gehen muss, nicht: Cora sagt dir, dass das Becken auf dieses Gerät eingestellt ist, dass es offline ist, und dass nichts gelaufen ist, damit du es erneut versuchen kannst, sobald es zurück ist. Wenn es länger offline sein wird, wähle ein anderes Gerät oder **Jedes aktive (automatisch)**.

:::note Lege ein primäres fest, wenn zwei Geräte ein Becken beobachten
Ein primäres zu benennen reduziert die Last auf dem Controller und entfernt doppelte Messwerte aus derselben Quelle.
:::

:::note Das ist eine kontoweite Einstellung pro Becken, keine pro Gerät
Primäres Cora Max gehört zum Becken, nicht zum Handy oder Tablet, das du gerade betrachtest. Es von einem beliebigen Gerät zu ändern, ändert es für den ganzen Haushalt.
:::

## Was fern von zu Hause funktioniert

Dein Handy spricht nicht direkt mit deiner Ausrüstung, wenn du fern vom eigenen WLAN deines Beckens bist. Statt dessen reist ein Befehl zu Cora Cloud, das ihn an ein Cora Max am Becken weitergibt; dieses Cora Max ist es, das die Ausrüstung tatsächlich erreicht.

Das bedeutet:

- **Messwerte und Historie** sind immer verfügbar, wo du auch bist, weil sie schon in Cora Cloud gespeichert sind.
- **Ausrüstung steuern** (eine Steckdose schalten, eine Fütterung starten, einen Kopf dosieren, eine Pumpe pausieren) funktioniert auch fern von zu Hause, solange ein Cora Max am Becken online ist und diese Ausrüstung erreichen kann. Ist keines online, kann der Befehl nicht zugestellt werden.
- **Die eigenen nativen Einstellungen eines Geräts** (im Gegensatz zu seinen Messwerten) brauchen manchmal ein Handy im *selben* Netzwerk wie das Gerät selbst, nicht nur ein Cora Max am Becken. Wo das zutrifft, sagt die Seite das.

Zwei Meldungen sagen dir, dass der Befehl nicht einfach gelungen ist:

- **"Nichts wurde gesendet"**: Der Befehl hat dein Handy nie verlassen, oder kein Cora Max am Becken konnte ihn aufnehmen. Nichts ist gelaufen. Das siehst du, wenn das Primäre Cora Max des Beckens offline ist und kein anderes Gerät an diesem Becken einspringen kann.
- **"Es ist möglicherweise schon gelaufen"**: Der Befehl wurde gesendet, aber kein Cora Max hat rechtzeitig geantwortet, um ihn zu bestätigen. Cora weiß wirklich nicht, ob er gelaufen ist. Prüfe den eigenen Zustand der Ausrüstung, bevor du es erneut versuchst, damit du ihn nicht zweimal sendest.

Wenn eine dieser Meldungen immer wieder erscheint, prüfe, ob ein Cora Max am Becken online ist, oder stelle **Primäres Cora Max** auf **Jedes aktive (automatisch)**, damit jedes Online-Gerät den Befehl aufnehmen kann. Siehe [Deine Ausrüstung steuern](/help/mobile-device-control) für die vollständigen Ergebnisse, die ein Befehl haben kann.

## Wo der Zustand jedes Geräts angezeigt wird

Cora Max meldet seine eigene Abfrage- und Sprachzustand unter **Einstellungen → Cora Max → Firmware → Gerätezustand & Steuerung**. Siehe [Geräte und Gerätezustand](/help/max-devices).
