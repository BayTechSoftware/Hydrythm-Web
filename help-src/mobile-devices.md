---
title: Adding, editing and removing devices
description: How to add equipment to Cora, assign it to a tank, rename it, and remove it cleanly.
section: Cora Mobile
reviewed: 2026-09-27
order: 9
group: Equipment
---

The **Devices** tab lists everything you've connected, grouped by brand. You can collapse each group, so even a reef room full of equipment stays easy to read.

![The Devices tab](img/mobile-devices.webp "Equipment is grouped by brand. Each group collapses.")

## Adding equipment

There are three buttons under the list, each for a different job:

| Button | Adds |
|---|---|
| **Add Device** | A Cora Max. It finds units already on your Wi-Fi, or nearby ones over Bluetooth. If it can't find yours, use **Enter IP Address Manually** on the same screen. |
| **Find a pump on your network** | Jecod pumps that announce themselves on the local network |
| **Add AquaWiz** | An AquaWiz controller, through your AquaWiz account |

![Adding a Cora Max](img/mobile-add-device.webp "Add Device searches Wi-Fi and Bluetooth for a Cora Max.")

You connect Neptune Apex and Red Sea ReefBeat equipment from the tank, not from this list. [Connecting your equipment](/help/mobile-connections) explains how.

When you add equipment such as a heater, pump or skimmer, Cora suggests brands and models as you type. The suggestions come from a large, checked list of equipment brands. If yours isn't there, type it in anyway. Cora keeps whatever you enter.

:::note Cora and your phone need the same network
Equipment Cora finds on your network has to be on the same network as your phone when you add it. **After setup, it's still only reachable over that network** (or over Bluetooth, for units that use it), unless a Cora device on site can reach it for you.

So equipment that reads fine at home may show older values while you're away, unless a Cora Max on site can poll it. Nothing's broken. It's about where the equipment can be reached from.
:::

## Assigning a device to a tank

Most equipment belongs to one tank, and that's how its readings end up on that tank's dashboard.

**Cora Max is the exception.** You can assign it up to four tanks, and it switches between them on screen. See [More than one Cora device](/help/mobile-multi-device).

Open the device and choose **Tank**. If you run more than one system, this matters more than any other setting. A heater assigned to the wrong tank reports perfectly well, into the wrong place.

:::warning Assign the tank before you rely on the readings
A device without a tank still reports, but its numbers have nowhere to go. If a device you just added isn't showing on a dashboard, check this first.
:::

## Renaming

Open the device and edit its name. Use what you call it day to day, like "Return", "Left gyre" or "Sump heater". The name shows up on widgets, in alerts and in anything you ask Cora, so a name that means something to you makes all of that clearer.

The new name only applies in Cora. It doesn't change the name in the manufacturer's own app.

## Checking whether a device is healthy

Each row shows the device's current state. You want to see a recent update time and no warning.

| What you see | What it means |
|---|---|
| A recent update time | Working normally |
| "Updated 3 h ago" on something that only reports every few hours | Fine |
| "Could not reach…" | A network problem, or the device is off |
| "…refused the sign-in" | The manufacturer's account needs reconnecting. Open the device and sign in again |
| Nothing at all | It's never reported. Check the tank assignment and the connection |

## Removing a device

Open the device and choose **Remove**. Cora tells you exactly what will be removed and asks you to confirm.

**Your readings are kept.** Removing a device stops Cora collecting new data from it. The history it already gathered stays on the tank, and any widget that used it keeps its past readings.

You lose the live link. If the device connected through a manufacturer account, you also lose the saved sign-in, so you'll need to sign in again if you add it back.

:::tip Quieten a noisy device without removing it
If a device works fine but alerts too often, change its thresholds or notification settings in [Alerts and thresholds](/help/mobile-alerts). You keep the connection and the data, and the noise stops.
:::
