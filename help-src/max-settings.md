---
title: Cora Max settings
description: The Settings screen on Cora Max: household settings, each tank, and everything about this screen itself.
section: Cora Max
reviewed: 2026-09-27
order: 13
group: Settings
---

Open settings with the **gear** at the far right of the top bar.

![Cora Max settings](img/max-settings.webp "Cora, then your tanks, then Cora Max Settings.")

Settings is organised into three groups: **CORA** (things that apply to your whole household of Cora devices), **TANKS** (one row per tank), and a single **Cora Max Settings** row for everything about this screen alone.

:::note Two kinds of setting, on purpose
Some settings belong to your **account**: they are the same no matter which phone or Cora Max you look at them from, and changing one changes it everywhere. Others belong to **this screen** only, such as its own brightness or Wi-Fi. The CORA and TANKS groups below are account settings. Cora Max Settings, the third group, is this screen's own settings.
:::

## CORA

Things that apply across every Cora device your account has, not just this one.

| Row | Opens |
|---|---|
| **Automations** | Every scene across every tank, with a filter by tank. See [Scenes on Cora Max](/help/max-automation) |
| **Devices** | The equipment Cora controls, across every tank. See [Devices and device health](/help/max-devices) |
| **Cora Assistant** | Which device answers when someone says "Hey Cora." See [Talking to Cora](/help/max-voice) |

## TANKS

One row per tank, opening that tank's own settings:

- **Alert thresholds**: the healthy band for each metric. See [Alerts and thresholds](/help/mobile-alerts)
- **Units**: which units this tank shows for salinity, temperature, alkalinity, volume, phosphate and nitrate. Choosing **Auto** for a metric shows each reading in the unit its own source recorded it in; picking a specific unit converts everything on this tank to it, on every screen and in what the Assistant speaks
- **Primary Cora Max**: which device polls this tank's equipment. See [Devices and device health](/help/max-devices)
- **Dashboard layout**: this tank's Cora Max layout. See [Editing the Cora Max dashboard](/help/max-dashboard-editing)
- Records and reports for this tank: **Journal**, **Maintenance**, **Livestock**, **Reef Buddy**, **Health Reports** and **ICP Reports**

## Cora Max Settings: everything about this screen

The single row at the bottom of Settings, labelled with this unit's name, opens everything that describes **this screen only**. It is organised into groups:

| Group | Covers |
|---|---|
| **Display** | Brightness, dim-after timer and its brightness, night dimming, showing the clock, and waking the screen on an alarm |
| **Sound & Voice** | Audio output (internal speaker, 3.5 mm or Bluetooth), the audible alert chime and its volume, spoken alerts, and **Wake-word listening** on or off |
| **Reef Buddy** | The hour the daily briefing appears, and whether it is read aloud |
| **Child Lock** | On or off, and the delay before it locks. See [Talking to Cora](/help/max-voice) for how to unlock it |
| **Notifications** | Notification history, the account-wide inbox of every briefing, alarm and account notice |
| **Language** | The one language your whole account uses. See the note below |
| **Network & Updates** | Wi-Fi, firmware updates, and a read-only line showing how often this unit polls your devices (set from Cora Mobile) |
| **Status** | One card per tank this screen shows: polling status, last poll, and last cloud write. Read-only |
| **Help & About** | Help & Support, and About (app version and **Licenses**) |
| **Reset** | Re-pair this device, and factory reset |

:::note Language is an account setting, not a per-screen one
Changing the language in **Language** changes it for your whole account: every phone and every Cora Max switches together. New reports, alerts and briefings follow the new language. Reports and alerts already written stay in the language they were written in; they are not retranslated.
:::

![Notification history on Cora Max](img/max-notifications.webp "Alarms and their recoveries, newest first, across every tank.")

Recoveries are recorded as well as alarms, so a parameter that went out of range and came back reads as a closed pair rather than an unexplained warning.

## Pairing, re-pairing and factory reset

**Cora Max Settings → Reset** shows what this screen is currently bound to, and offers two actions:

**Re-pair this device** clears this screen's pairing and sends it back to the pairing screen.

**Factory reset** also clears every preference stored on this screen. Its confirmation says exactly what is cleared and what is kept.

Both keep the tank data already saved to Cora Cloud. Both also remove this Cora Max from your account and make it forget its Wi-Fi network, so you pair it again from Cora Mobile as you would a new unit. If Cora Max cannot reach Cora Cloud to remove itself, it tells you it is still listed in Cora Mobile: open it there under **Devices** and choose **Remove device**.

![The factory reset confirmation](img/max-factory-reset.webp "The dialog states what is cleared and what survives before you commit.")

:::warning A reset clears the screen, not your data
Factory reset removes the pairing record and every on-device preference, and returns the unit to its pairing screen. **Tank data already saved to your account is kept**; pair the device again to a tank and it reappears. What you lose is this screen's own setup: its Wi-Fi, display, sound and voice settings.
:::

:::note Your layouts may survive after all
Before a reset, Cora Max archives its configuration. If you then pair the unit back to the **same tank**, it offers **Restore previous layout for this tank?** Take it, or choose **Start fresh** if wiping the screen was the point.
:::

## Which tanks this screen shows

A Cora Max can show one tank or several, and you switch between them from the top bar. **The set itself is chosen from your phone**, under **Devices → your Cora Max**, not from this screen.

## Updates

Cora Max keeps itself up to date. New versions download in the background and install themselves, and you are told what changed. If a version has just arrived, the prompt appears on screen. There is nothing you need to do to stay current. See **[Keeping Cora Max updated](/help/max-updates)**.
