---
title: Adding, editing and removing devices
description: How to add equipment to Cora, assign it to a tank, rename it, and remove it cleanly.
section: Cora Mobile
order: 6
---

The **Devices** tab is everything you have connected, grouped by brand. Each group collapses so a reef room full of equipment stays readable.

![The Devices tab](img/mobile-devices.webp "Equipment grouped by brand, each group collapsible.")

## Adding a device

Tap **Add Device** at the bottom of the list and pick what you are adding. What happens next depends on the brand — some connect over your network, some through the manufacturer's account. **[Connecting your gear](/help/mobile-connections)** covers each one.

Two shortcuts sit under the button:

- **Find a pump on your network** scans your local network for pumps that announce themselves, so you don't have to type addresses.
- **Add AquaWiz** goes straight to the AquaWiz sign-in, since that one connects through your AquaWiz account rather than over your network.

:::note Cora and your phone need the same network
Anything discovered locally has to be on the same network as your phone at the moment you add it. Once it is added, Cora keeps talking to it — you don't have to stay on that network.
:::

## Assigning a device to a tank

Every device belongs to a tank. That is what makes its readings appear on that tank's dashboard.

Open the device and choose **Tank**. If you run more than one system, this is the setting that matters most — a heater reporting into the wrong tank will look like a mystery.

:::warning Assign the tank before you rely on the readings
A device with no tank still reports, but its numbers have nowhere to land. If a device you just added isn't showing up on a dashboard, this is the first thing to check.
:::

## Renaming

Open the device and edit its name. Use whatever you call it out loud — "Return", "Left gyre", "Sump heater". The name appears on widgets, in alerts and in anything you ask Cora, so a name that means something to you makes everything downstream clearer.

Renaming is local to Cora. It does not change the name on the manufacturer's own app.

## Checking whether a device is healthy

Each row shows its current state. What you want to see is a recent update time and no warning.

| What you see | What it means |
|---|---|
| A recent update time | Working normally |
| "Updated 3 h ago" on something that reports hourly | Fine |
| "Could not reach…" | A network problem, or the device is off |
| "…refused the sign-in" | The manufacturer's account needs reconnecting — open the device and sign in again |
| Nothing at all | It has never reported; check the tank assignment and the connection |

## Removing a device

Open the device and choose **Remove**. You will be asked to confirm, and told exactly what is being removed.

**Your readings are kept.** Removing a device stops Cora collecting new data from it; the history it already gathered stays on the tank, and any widget pointed at it keeps its past readings.

What you lose is the live link — and, where the device connected through a manufacturer account, the stored sign-in. Adding it back means signing in again.

:::tip Removing is not how you silence an alert
If a device is fine but noisy, change its thresholds or notification settings instead — see **[Alerts and thresholds](/help/mobile-alerts)**. Removing it loses the connection and gains you nothing.
:::
