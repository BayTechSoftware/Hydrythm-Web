---
title: Notifications
description: Choose what reaches your phone, when it may arrive, and where to read what you missed.
section: Cora Mobile
order: 15
---

**Settings → Notifications** controls everything Cora may send you.

![Notification settings](img/mobile-notifications.webp "Each category can push independently.")

## What can push

Each category is switched independently:

| Category | Covers |
|---|---|
| **Parameter Alerts** | Water chemistry outside a range you set |
| **Maintenance Reminders** | Tasks you scheduled, like water changes |
| **Equipment Faults** | A device reporting a problem — a Trident that has stopped testing, for example |
| **Supplies Running Low** | Reagent, top-off water, dosing containers — and a full waste bottle |
| **ICP Report Ready** | Your ICP results are analysed and ready to read |

Turning a category off stops the push. The event is still recorded and still appears in the bell.

:::warning "Parameter Alerts" means chemistry, and only chemistry
It is natural to read that switch as covering everything the tank might tell you. It does not. A Trident that has stopped testing is an **Equipment Fault**, and reagent running out is **Supplies Running Low** — each has its own switch. If you have had Parameter Alerts on for a long time and assumed it covered the rest, check the other two.
:::

**Supplies Running Low includes the waste bottle**, which fills up rather than runs down. It is in this category because the action it needs is the same: something to empty or replace before it stops the tests.

Equipment faults can be narrowed further. A separate set of switches covers the individual fault types — **Stall Detected**, **Encoder Error**, **Power Instability** and **Home Timeout** — for when you want the category on but one noisy fault off.

## The bell

Top right of every screen. It holds everything Cora has raised, newest first, whether or not it pushed. The number is what you have not read.

This is the right place to check after a day away from your phone, or after a category you switched off raised something.

## If nothing is arriving

Work down this list:

1. **Settings → Notifications** — is that category allowed to push?
2. Your phone's own settings — is Cora allowed to notify at all? A permission denied at install time overrides everything here.
3. Is there actually anything to send? Reef Buddy stays quiet on days when nothing changed.

## If too much is arriving

Review your thresholds before disabling notifications. Excessive alerts usually indicate a range set tighter than the tank runs, or a source requiring calibration. See [Alerts and thresholds](/help/mobile-alerts).
