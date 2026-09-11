---
title: Adding, editing and removing devices
description: How to add equipment to Cora, assign it to a tank, rename it, and remove it cleanly.
section: Cora Mobile
reviewed: 2026-09-09
order: 9
group: Equipment
---

The **Devices** tab is everything you have connected, grouped by brand. Each group collapses so a reef room full of equipment stays readable.

![The Devices tab](img/mobile-devices.webp "Equipment is grouped by brand. Each group collapses.")

## Adding equipment

Three buttons sit below the list, and they do different jobs:

| Button | Adds |
|---|---|
| **Add Device** | A Cora Max. Finds units already on your Wi-Fi, or nearby ones over Bluetooth. **Enter IP Address Manually** is inside this screen if discovery does not find it. |
| **Find a pump on your network** | Jecod pumps that advertise themselves on the local network |
| **Add AquaWiz** | An AquaWiz controller, through your AquaWiz account |

![Adding a Cora Max](img/mobile-add-device.webp "Add Device searches Wi-Fi and Bluetooth for a Cora Max.")

Other equipment (Neptune Apex and Red Sea ReefBeat) is connected from the tank rather than from this list. See [Connecting your equipment](/help/mobile-connections).

:::note Cora and your phone need the same network
Equipment discovered locally must be on the same network as your phone when you add it. **After setup it is still only reachable over that network** (or over Bluetooth, for units that use it) unless a Cora device on site can reach it for you.

Equipment that reads correctly at home may therefore show older values while you are away, unless a Cora Max on site can poll it. This reflects where the equipment is reachable from, rather than a fault.
:::

## Assigning a device to a tank

Most equipment belongs to exactly one tank, and that is what makes its readings appear on that tank's dashboard.

**Cora Max is the exception**: it can be assigned up to four tanks and switches between them on screen. See [More than one Cora device](/help/mobile-multi-device).

Open the device and choose **Tank**. If you run more than one system, this is the setting that matters most: a heater assigned to the wrong tank reports perfectly well into the wrong place.

:::warning Assign the tank before you rely on the readings
A device with no tank still reports, but its numbers have nowhere to land. If a device you have just added is not appearing on a dashboard, check this first.
:::

## Renaming

Open the device and edit its name. Use the name you use for it day to day: "Return", "Left gyre", "Sump heater". The name appears on widgets, in alerts and in anything you ask Cora, so a name that means something to you makes everything downstream clearer.

Renaming is local to Cora. It does not change the name on the manufacturer's own app.

## Checking whether a device is healthy

Each row shows its current state. What you want to see is a recent update time and no warning.

| What you see | What it means |
|---|---|
| A recent update time | Working normally |
| "Updated 3 h ago" on something that reports hourly | Fine |
| "Could not reach…" | A network problem, or the device is off |
| "…refused the sign-in" | The manufacturer's account needs reconnecting; open the device and sign in again |
| Nothing at all | It has never reported; check the tank assignment and the connection |

## Removing a device

Open the device and choose **Remove**. You will be asked to confirm, and told exactly what is being removed.

**Your readings are kept.** Removing a device stops Cora collecting new data from it; the history it already gathered stays on the tank, and any widget pointed at it keeps its past readings.

What you lose is the live link, and, where the device connected through a manufacturer account, the stored sign-in. Adding it back means signing in again.

:::tip Quieten a noisy device without removing it
If a device is working correctly but alerting too often, adjust its thresholds or notification settings; see **[Alerts and thresholds](/help/mobile-alerts)**. That keeps the connection and the data while stopping the noise.
:::
