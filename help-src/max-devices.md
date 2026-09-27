---
title: Devices and device health
description: What Cora Max can see, which device polls each tank, and what to check when polling stops.
section: Cora Max
reviewed: 2026-09-27
order: 7
group: Equipment
---

**Settings → Devices** lists the equipment Cora Max can see and reports how it is doing.

## The device list

![The device list](img/max-devices.webp "Filter by tank, then each device with a one-line summary of what it holds.")

Cora Max sees the same equipment as your phone, because both read the same account.

Filter chips at the top narrow the list to **All tanks** or one tank. Each entry carries a status dot, a one-line summary of what the device holds (*21 outlets · 4 feeds*, *19 tests left*) and the tank it belongs to.

Adding and configuring equipment is easier on the phone; see [Adding, editing and removing devices](/help/mobile-devices).

## Primary Cora Max: which tablet talks to your equipment

**Primary Cora Max** is the tablet (or other Cora device) that reads a tank's controller and other equipment for the whole account. Only one device needs to do this per tank; every other screen simply shows what it reads.

Open **Settings → [your tank] → Primary Cora Max** to see or change it. There are two kinds of choice:

- **Any active (automatic)**: every online Cora device that can reach this tank's equipment shares the work, and the most recent write wins. This is the setting to use unless you have a specific reason to pin one device.
- **Pin one device**: only that device polls. If the pinned device goes offline, nothing polls this tank's equipment until you pin a different one, or switch back to Any active (automatic).

This choice is made once, for the tank, not once per Cora screen. Change it from any Cora Max showing that tank, or from Cora Mobile; see [More than one Cora device](/help/mobile-multi-device).

:::note Primary Cora Max is not the same as Cora Assistant
Primary Cora Max decides which device **reads your equipment**. A separate setting, **Cora Assistant**, decides which device **answers "Hey Cora"**. A household with more than one Cora Max can set these two independently. See [Talking to Cora](/help/max-voice).
:::

## If a tank's readings stop

If one tank's readings stop while another tank on the same screen keeps updating, start with:

1. **Settings → [that tank] → Primary Cora Max**: confirm a device is actually assigned, and that it is online.
2. If a secondary Cora Max for this tank shows the pill **Main Cora offline** in its top bar, the primary has lost its connection; see [The Cora Max home screen](/help/max-tour) for what the status pill means.
3. **Settings → Cora Max Settings → Network & Updates → Device polling** shows how often this unit itself reads your devices; this value is read-only here and is set from Cora Mobile.

**If it does not work:** see [Troubleshooting](/help/troubleshooting).

## Managing a Cora Max from your phone

Open the unit from your phone's **Devices** tab to see its variant, firmware version and when it was last seen, and to rename it or change some of its settings without walking to it.

![Cora Max settings from the phone](img/max-from-phone.webp "Polling interval, brightness, volume, on-screen alerts and dim timer.")

Settings shown this way describe **this screen only** (its brightness, volume, on-screen alert banners and dim timer), the same way they would if you changed them at the wall. Turning off on-screen alerts does not affect alert history or push notifications.

Which tanks a Cora Max shows, and which one is its Primary Cora Max for each tank, are account-wide choices; change them from either device, as described above.

:::note Device health is read-first
The **Status** section of **Settings → Cora Max Settings** on this screen reports polling status, last poll time and last cloud write for each tank, without changing anything. Use it to establish what is happening before altering a setting.
:::
