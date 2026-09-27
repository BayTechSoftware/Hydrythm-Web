---
title: Notifications
description: Choose what reaches your phone, when it can arrive, and where to read what you missed.
section: Cora Mobile
reviewed: 2026-09-27
order: 16
group: Alerts and automation
---

**Settings → Notifications** controls everything Cora can send you.

![Notification settings](img/mobile-notifications.webp "Each category can push independently.")

## What can push

Each category has its own switch.

| Category | Covers |
|---|---|
| **Parameter Alerts** | Water chemistry outside a range you set |
| **Maintenance Reminders** | Tasks you scheduled, like water changes |
| **Equipment Faults** | A device reporting a problem, for example a Trident that has stopped testing |
| **Supplies Running Low** | Reagent, top-off water, dosing containers, and a full waste bottle |
| **ICP Report Ready** | Your ICP results are analysed and ready to read |

When you turn a category off, it stops pushing. Cora still records the event, and you'll still find it under the bell.

:::warning "Parameter Alerts" is only about chemistry
It's easy to think that switch covers everything the tank might tell you. It doesn't. A Trident that has stopped testing is an **Equipment Fault**. Reagent running out is **Supplies Running Low**. Each has its own switch. If you've relied on Parameter Alerts for a long time, check the other two.
:::

**Supplies Running Low includes the waste bottle**, even though it fills up instead of running down. You deal with it the same way. It's something to empty or replace before it stops the tests.

## The bell

The bell sits at the top right of every screen. It holds everything Cora has raised, newest first, whether or not it was pushed. The number on it is how many you haven't read.

Check it after a day away from your phone, or when a category you switched off has raised something.

## If nothing is arriving

Go through these in order.

1. Open **Settings → Notifications**. Is that category allowed to push?
2. Check your phone's own settings. Is Cora allowed to send notifications at all? If you said no when you installed it, that overrides everything here.
3. Is there anything to send? Reef Buddy stays quiet on days when nothing changed.

## If too much is arriving

Look at your thresholds before you turn notifications off. Too many alerts usually means a range is tighter than the tank really runs, or a source needs calibrating. More in [Alerts and thresholds](/help/mobile-alerts).

Turning a category off silences all of it. If it's one alert pushing too often, change **Cooldown between alerts** on that rule instead. It goes from 15 minutes up to 1 week. The cooldown options, and what "snooze" means on Cora Max, are in [Alerts and thresholds](/help/mobile-alerts).
