---
title: Cora Max settings
description: Settings on the Cora Max display — the screen itself, devices, tanks, notifications and updates.
section: Cora Max
order: 13
---

Open settings with the **gear** at the far right of the top bar.

![Cora Max settings](img/max-settings.webp "Tank settings first, then devices and notification history.")

## Tank settings

One entry per tank this screen shows, each opening that tank's **journal, maintenance, alerts, livestock, reports and activity**. Thresholds set here are the same ranges you set on your phone — change one anywhere and it applies everywhere. See **[Alerts and thresholds](/help/mobile-alerts)**.

:::note Polling here means *which device*, not *how often*
The polling setting in a tank's settings chooses which Cora device reads that tank's equipment — the **primary poller**. It does not change the interval. See [More than one Cora device](/help/mobile-multi-device).
:::

## Devices

Everything this screen can see and how each one is doing. Cora Max sees the same devices as your phone. Diagnostics for the *unit itself* are not here — they are under **Cora Max → Firmware → Device health & controls**.

You can check state here, but adding and configuring equipment is easier in Cora Mobile — see **[Adding, editing and removing devices](/help/mobile-devices)**.

## Notification history

The **account-wide** inbox — every briefing, alarm and account notice across your whole system, including anything your phone missed.

![Notification history on Cora Max](img/max-notifications.webp "Alarms and their recoveries, newest first, across every tank.")

Recoveries are recorded as well as alarms, so a parameter that went out of range and came back reads as a closed pair rather than an unexplained warning.

## Cora Max — everything about this screen

Everything that describes *this unit* lives behind one row in Settings, under the **DEVICE SETTINGS** heading, labelled **Cora Max**. It opens a screen headed *Device settings*, organised into groups:

| Group | Covers |
|---|---|
| **Firmware** | Firmware Update — install, channel and schedule — and **Device health & controls**, which holds the unit's diagnostics, its polling primary and the voice responder |
| **Network** | Wi-Fi |
| **Audio** | Audio output, and **Wake-word listening** on or off |
| **Alerts** | Audible alert chime, and spoken alerts |
| **Display** | Idle dim after, and night dimming |
| **Experience** | Wake screen on alarm, show clock, **Child lock** and its lock-after delay, briefing time and voice briefing |
| **Device** | Re-pair this device, and factory reset |

:::note Wake-word listening is under Audio, not Voice
The **Voice** group holds diagnostics rather than the on/off switch. If you are looking to stop the screen listening, it is in **Audio**.
:::

:::note These belong to this screen only
Wi-Fi, display, audio, wake word and child lock describe this unit. They are not shared with your phone or another Cora Max.
:::

## Pairing, re-pairing and factory reset

**Device settings** shows what this screen is currently bound to: its firmware version, which tanks it displays, whether an account is signed in, and when it was paired.

![Device settings on Cora Max](img/max-pairing-info.webp "What this screen is bound to — firmware, tanks, account and the date it was paired.")

**Re-pair this device** moves the screen to a different account or tank set without clearing its preferences.

**Factory reset** goes further, and the confirmation says exactly how far.

![The factory reset confirmation](img/max-factory-reset.webp "The dialog states what is cleared and what survives before you commit.")

:::warning A reset clears the screen, not your data
Factory reset removes the pairing record and every on-device preference, and returns the unit to its pairing screen. **Tank data already saved to your account is kept** — pair the device again to a tank and it reappears. What you lose is this screen's own setup: its Wi-Fi, display, audio and voice settings.
:::

:::note Your layouts may survive after all
Before a reset, Cora Max archives its configuration. If you then pair the unit back to the **same tank**, it offers **Restore previous layout for this tank?** — take it, or choose **Start fresh** if wiping the screen was the point.
:::

## Which tanks this screen shows

A Cora Max can show one tank or several, and you switch between them from the top bar. **The set itself is chosen from your phone**, under **Devices → your Cora Max → assigned tanks** — not from this screen.

## Updates

Cora Max keeps itself up to date. New versions download in the background and install themselves, and you are told what changed. If a version has just arrived, the prompt appears on screen. There is nothing you need to do to stay current. See **[Keeping Cora Max updated](/help/max-updates)**.

:::note Settings live in two places, on purpose
Anything about *this screen* — Wi-Fi, brightness, sound — is here. Anything about your *account* — tanks, devices, dosing products, plans — belongs to your account and is easier to change in Cora Mobile, where it applies to every screen at once.
:::
