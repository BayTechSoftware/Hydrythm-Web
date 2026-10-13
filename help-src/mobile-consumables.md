---
title: Consumables and refill alerts
description: Set refill alerts for reagent, dosing containers, top-off reservoirs and filter rolls, and tell Cora when you've refilled.
section: Cora Mobile
reviewed: 2026-10-13
order: 16
group: Equipment
---

Use refill alerts so Cora warns you before reagent, dosing liquid, top-off water or filter roll runs out. Open the device from **Devices** (or tap its tile on the dashboard), then tap the **bell** in the top bar.

## Setting a refill alert {#setting-a-refill-alert}

![The Alerts sheet for a ReefDose 4, with a days-left threshold and switch for each head](img/mobile-consumables.webp "One threshold per head, each with its own switch.")

The sheet is called **Alerts:** followed by the device's name. If the equipment has more than one container, each one gets its own threshold and its own switch, so a head you watch closely and one you rarely touch can be set differently. Turning a switch off keeps the value for later.

Where to set it:

- **Most devices**: the bell in the top bar of the device's page.
- **DŌS**: the **Alerts** card on the DŌS page, or the bell. See [Doser alerts](/help/mobile-device-control#doser-alerts).
- **AquaWiz and GHL dosers**: their rule on the **Rules** tab of the [Alert Center](/help/mobile-alerts).

Most thresholds are in days, not volume. Cora works out how long what's left will last at the rate you're using it. "Four days of calcium left" is something you can act on. "180 mL left" isn't.

## What you can be warned about {#thresholds}

| Device | Threshold | Starts at |
|---|---|---|
| Trident | **Tests remaining** (the lowest reagent) | 10 tests |
| Trident | **Waste bottle** (a full bottle fails the next test) | 85% full |
| DŌS head | *[head] · days left* | 7 days |
| DŌS head | *[head] · remaining*, in mL | 100 mL |
| DŌS head that takes old water out | **Waste container space left** | |
| DŌS head | **Missed dose alerts** (a switch) | |
| ReefDose head | Days of supplement left | 7 days |
| ReefATO+ | **Reservoir runway**, estimated from recent top-off use | 2 days |
| ReefMat | **Roll remaining**, estimated from how fast the roller advances | 3 days |
| AquaWiz | Alkalinity supplement left | 100 mL |
| GHL doser *(Beta)* | How full the container is | 20% |
| EcoTech Versa *(Beta)* | Days of supplement left, and how full the container is | 7 days, 10% |

A Focustronic *(Beta)* unit shows its own reagent and buffer warnings on its page.

:::note Beta
**Beta.** GHL, EcoTech and Focustronic are in Beta and only open to Beta users. If you are not a Beta user you will not see them in **Add device**. To ask for Beta access, contact [support](/support.html).
:::

A consumable alert works like any other alert. It shows in the [Alert Center](/help/mobile-alerts) and can push to your phone. You get **one** notification when a level is crossed, and it clears when the level is back above the threshold.

## Choosing a threshold {#choosing-a-threshold}

Set it early enough that you have time to act. If it fires the day something runs out, it's no warning at all.

:::warning Some equipment keeps going when it's empty
A DŌS head with an empty container keeps running its schedule and reports doses it never delivered. It has no low-level warning of its own. A refill alert is how you catch this, so set one for every head you dose from.
:::

## After refilling {#after-refilling}

Tell Cora on the device's page, so the alert clears and the next warning is worked out from the right level.

| Device | Tap |
|---|---|
| DŌS head | **Fill**, then **Full**, or set **Volume Remaining** |
| DŌS waste container | Reset its free space to full after you empty it |
| ReefDose head | **Remaining in bottle** |
| ReefMat | **New roll (Beta)** after you load a new roll |
| EcoTech Versa *(Beta)* | **Mark as refilled** |

Trident, ReefATO+ and AquaWiz report their own levels, so there's nothing to reset in Cora.
