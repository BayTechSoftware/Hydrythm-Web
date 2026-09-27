---
title: Geräte und Gerätezustand
description: Was Cora Max sehen kann, welches Gerät jedes Becken abfragt, und was zu prüfen ist, wenn die Abfrage stoppt.
section: Cora Max
reviewed: 2026-09-27
order: 7
group: Equipment
---

**Einstellungen → Geräte** listet die Ausrüstung, die Cora Max sehen kann, und meldet, wie es ihr geht.

## Die Geräteliste

![Die Geräteliste](img/max-devices.webp "Nach Becken filtern, dann jedes Gerät mit einer einzeiligen Zusammenfassung dessen, was es enthält.")

Cora Max sieht dieselbe Ausrüstung wie dein Handy, weil beide dasselbe Konto lesen.

Filter-Chips oben grenzen die Liste auf **Alle Becken** oder ein Becken ein. Jeder Eintrag trägt einen Statuspunkt, eine einzeilige Zusammenfassung dessen, was das Gerät enthält (*21 Steckdosen · 4 Fütterungen*, *19 Tests übrig*), und das Becken, zu dem es gehört.

Ausrüstung hinzuzufügen und zu konfigurieren ist auf dem Handy einfacher; siehe [Geräte hinzufügen, bearbeiten und entfernen](/help/mobile-devices).

## Primäres Cora Max: welches Tablet mit deiner Ausrüstung spricht

**Primäres Cora Max** ist das Tablet (oder andere Cora-Gerät), das den Controller und andere Ausrüstung eines Beckens für das ganze Konto liest. Nur ein Gerät muss das pro Becken tun; jeder andere Bildschirm zeigt einfach, was es liest.

Öffne **Einstellungen → [dein Becken] → Primäres Cora Max**, um es zu sehen oder zu ändern. Es gibt zwei Arten von Wahl:

- **Jedes aktive (automatisch)**: Jedes Online-Cora-Gerät, das die Ausrüstung dieses Beckens erreichen kann, teilt sich die Arbeit, und der neueste Schreibvorgang gewinnt. Das ist die Einstellung, die du nutzen solltest, sofern du keinen bestimmten Grund hast, ein Gerät festzulegen.
- **Ein Gerät festlegen**: Nur dieses Gerät fragt ab. Geht das festgelegte Gerät offline, fragt nichts die Ausrüstung dieses Beckens ab, bis du ein anderes festlegst, oder zurück auf Jedes aktive (automatisch) wechselst.

Diese Wahl wird einmal getroffen, für das Becken, nicht einmal pro Cora-Bildschirm. Ändere sie von jedem Cora Max aus, das dieses Becken zeigt, oder von Cora Mobile; siehe [Mehr als ein Cora-Gerät](/help/mobile-multi-device).

:::note Primäres Cora Max ist nicht dasselbe wie Cora Assistant
Primäres Cora Max entscheidet, welches Gerät **deine Ausrüstung liest**. Eine getrennte Einstellung, **Cora Assistant**, entscheidet, welches Gerät **auf "Hey Cora" antwortet**. Ein Haushalt mit mehr als einem Cora Max kann diese beiden unabhängig festlegen. Siehe [Mit Cora sprechen](/help/max-voice).
:::

## Wenn die Messwerte eines Beckens stoppen

Wenn die Messwerte eines Beckens stoppen, während ein anderes Becken auf demselben Bildschirm weiter aktualisiert, beginne mit:

1. **Einstellungen → [dieses Becken] → Primäres Cora Max**: bestätige, dass tatsächlich ein Gerät zugewiesen ist, und dass es online ist.
2. Wenn ein sekundäres Cora Max für dieses Becken die Pille **Haupt-Cora offline** in seiner oberen Leiste zeigt, hat das primäre seine Verbindung verloren; siehe [Der Cora Max Startbildschirm](/help/max-tour) für das, was die Status-Pille bedeutet.
3. **Einstellungen → Cora Max-Einstellungen → Netzwerk & Updates → Geräteabfrage** zeigt, wie oft dieses Gerät selbst deine Geräte liest; dieser Wert ist hier nur zur Ansicht und wird von Cora Mobile aus festgelegt.

**Wenn es nicht funktioniert:** siehe [Problembehebung](/help/troubleshooting).

## Ein Cora Max von deinem Handy aus verwalten

Öffne das Gerät im Tab **Geräte** deines Handys, um seine Variante, Firmware-Version und den Zeitpunkt zu sehen, an dem es zuletzt gesehen wurde, und um es umzubenennen oder einige seiner Einstellungen zu ändern, ohne zu ihm zu gehen.

![Cora Max-Einstellungen vom Handy aus](img/max-from-phone.webp "Abfrageintervall, Helligkeit, Lautstärke, Warnungen auf dem Bildschirm und Dimmer-Timer.")

So angezeigte Einstellungen beschreiben **nur diesen Bildschirm** (seine Helligkeit, Lautstärke, Warnbanner auf dem Bildschirm und Dimmer-Timer), genauso, wie sie es täten, wenn du sie an der Wand geändert hättest. Warnungen auf dem Bildschirm auszuschalten hat keinen Einfluss auf die Warnhistorie oder Push-Benachrichtigungen.

Welche Becken ein Cora Max zeigt, und welches sein Primäres Cora Max für jedes Becken ist, sind kontoweite Entscheidungen; ändere sie von jedem der beiden Geräte aus, wie oben beschrieben.

:::note Gerätezustand ist zuerst zum Lesen da
Der Abschnitt **Status** von **Einstellungen → Cora Max-Einstellungen** auf diesem Bildschirm meldet den Abfragestatus, die letzte Abfragezeit und den letzten Cloud-Schreibvorgang für jedes Becken, ohne irgendetwas zu ändern. Nutze ihn, um festzustellen, was passiert, bevor du eine Einstellung änderst.
:::
