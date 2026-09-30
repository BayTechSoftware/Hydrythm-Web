---
title: Adding, editing and removing devices
description: How to add equipment to Cora, assign it to a tank, and remove it cleanly, all from one place.
section: Cora Mobile
reviewed: 2026-09-30
order: 9
group: Equipment
---

Add, edit, assign and remove every device from the **Devices** tab, grouped by brand. You can collapse each group, so even a reef room full of equipment stays easy to read.

![The Devices tab](img/mobile-devices.webp "Equipment is grouped by brand. Each group collapses.")

## Adding equipment

Tap **Add Device**, then pick the brand: **Cora**, **Neptune Apex**, **Red Sea**, **Jecod**, **Maxspect**, **GHL** *(beta)*, **HYDROS** *(beta)* or **AquaWiz**. Each one opens exactly what it needs to find your equipment: a network scan, an IP address, a sign-in or a device key. [Connecting your equipment](/help/mobile-connections) covers what each brand needs.

**Cora** is how you pair a new Cora Max. It finds units already on your Wi-Fi, or nearby ones over Bluetooth. If it can't find yours, use **Enter IP Address Manually** on the same screen.

When you add equipment such as a heater, pump or skimmer, Cora suggests brands and models as you type. The suggestions come from a large, checked list of equipment brands. If yours isn't there, type it in anyway. Cora keeps whatever you enter.

:::note Cora and your phone need the same network
Equipment Cora finds on your network has to be on the same network as your phone when you add it. **After setup, it's still only reachable over that network** (or over Bluetooth, for units that use it), unless a Cora device on site can reach it for you.

So equipment that reads fine at home may show older values while you're away, unless a Cora Max on site can poll it. Nothing's broken. It's about where the equipment can be reached from.
:::

## A device's page

Open any device from the list. Its controls come first, then three sections that work the same way for every brand.

- **Tanks** shows which tank (or tanks) it's assigned to. Tap **Change** to reassign it.
- **Connection** is where you edit its IP address, sign-in or device key.
- **Remove device**, at the bottom.

Cora Max, Neptune Apex and GHL can serve more than one tank, so their tank picker is a checklist. Cora Max can be assigned up to four. See [More than one Cora device](/help/mobile-multi-device). Everything else, including HYDROS, serves one tank at a time: picking a different one moves the device there and takes it off the old one.

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
| "Waiting for Cora Max" | A GHL controller you just added: it shows up once a Cora Max on its network has read it |
| Nothing at all | It's never reported. Check the tank assignment and the connection |

## Removing a device

Open the device and tap **Remove device**. Cora asks you to confirm: *"{name} will be removed from Cora. It is not reset or changed on the device itself."*

**Your readings are kept.** Removing a device stops Cora collecting new data from it. The history it already gathered stays on the tank, and any widget that used it keeps its past readings.

You lose the live link. If the device connected through a manufacturer account, you also lose the saved sign-in, so you'll need to sign in again if you add it back.

:::tip Quieten a noisy device without removing it
If a device works fine but alerts too often, change its thresholds or notification settings in [Alerts and thresholds](/help/mobile-alerts). You keep the connection and the data, and the noise stops.
:::
