---
title: Adding, editing and removing devices
description: Add equipment to Cora, assign it to a tank, rename it, check it's healthy and remove it, all from the Devices tab.
section: Cora Mobile
reviewed: 2026-10-13
order: 11
group: Equipment
twin: max-devices
---

The **Devices** tab is where you add, assign, rename, check and remove every piece of equipment. Devices are grouped by brand, and you can collapse each group.

![The Devices tab](img/mobile-devices.webp "Equipment is grouped by brand. Each group collapses.")

## Adding equipment {#adding-equipment}

1. On the **Devices** tab, tap **Add Device**.
2. Pick the brand: **Cora**, **Neptune Apex**, **Red Sea**, **Jecod** or **AquaWiz**. Beta users also see **Maxspect**, **GHL**, **HYDROS**, **Focustronic**, **EcoTech**, **Inkbird** and **Camera**, each with a **Beta** chip.
3. Follow the brand's steps. Depending on the brand that's a network scan, an IP address, a sign-in or a device key. [Connecting your equipment](/help/mobile-connections) has the steps for each brand.
4. Choose the tank it belongs to.

![The Add device list for a Beta user](img/mobile-add-device-beta.webp "Beta brands carry a Beta chip.")

:::note Beta
**Beta.** The Beta integrations are only open to Beta users. If you are not a Beta user you will not see them in **Add device**. To ask for Beta access, contact [support](/support.html). More in [Beta features](/help/mobile-beta).
:::

A row that needs a Cora Max in the tank (Maxspect, GHL, EcoTech, Inkbird and Camera) is greyed out and says **Requires Cora Max** until the tank has one.

:::note Without a Cora Max, some equipment is local only
Neptune Apex, Red Sea and Jecod equipment is reached over your home network or Bluetooth. Without a Cora Max, the add screen says *This integration works only locally on the Mobile app without Cora Max.* Your phone reads and controls it only while it's on the same network (or in Bluetooth range). Away from home you see the last readings your phone saved and can't control it. A Cora Max at the tank reads it around the clock and passes your commands on. More in [Connecting your equipment](/help/mobile-connections#local-only).
:::

When you add equipment from your network, your phone has to be on the same network as the equipment.

## Pairing a Cora Max {#pairing-a-cora-max}

![The Add Your Cora screen in Cora Mobile, scanning for devices](img/mobile-add-device.webp "Add Device, then Cora. Cora Mobile looks on your Wi-Fi and over Bluetooth, with Enter IP Address Manually below.")

**Cora** is how you pair a new Cora Max. It finds units already on your Wi-Fi, or nearby ones over Bluetooth. If it can't find yours, use **Enter IP Address Manually** on the same screen. The full walk-through is in [Setting up Cora Max](/help/max-setup).

## A device's page {#a-devices-page}

Tap any device in the list to open its page. Its controls come first, then sections that work the same way for every brand.

- **Status** shows the **Model**, **Serial**, **Firmware** and when Cora last heard from it (**Last seen**).
- **Tanks** shows which tank (or tanks) it's assigned to. Tap **Change** to reassign it.
- **Connection** is where you edit its IP address, sign-in or device key.
- **Remove device**, at the bottom.

Cora Max, Neptune Apex and GHL can serve more than one tank, so their tank picker is a checklist. Cora Max can be assigned up to four. See [More than one Cora device](/help/mobile-multi-device). Everything else, including HYDROS, serves one tank at a time. Picking a different one moves the device there and takes it off the old one.

:::warning Assign the tank before you rely on the readings
A device without a tank still reports, but its numbers have nowhere to go. If a device you just added isn't showing on a dashboard, check this first.
:::

What each brand's controls do is in [Controlling your equipment](/help/mobile-device-control).

## Renaming {#renaming}

Open the device and tap the pencil beside its name. Use what you call it day to day, like "Return", "Left gyre" or "Sump heater". The name shows up on widgets, in alerts and in anything you ask Cora.

Names can be up to 40 characters. Leave the name empty to go back to the device's own name. If two devices of the same kind have no name, Cora tells them apart with a short code after the name. Cora never uses a serial number as a name.

The new name only applies in Cora. It doesn't change the name in the manufacturer's own app.

## Checking whether a device is healthy {#health}

Each device is one row on the Devices tab, with its icon, name, model and tank. The dot on the row shows its state.

| Dot | What it means |
|---|---|
| Grey | Cora doesn't know yet |
| Green | Working normally |
| Orange | A warning or a fault |
| Red | Offline |

For more, open the device. Its **Status** section shows when Cora last heard from it. You want a recent time and no warning.

| What you see | What it means |
|---|---|
| A recent update time | Working normally |
| "Updated 3 h ago" on something that only reports every few hours | Fine |
| "Could not reach…" | A network problem, or the device is off |
| "…refused the sign-in" | The manufacturer's account needs reconnecting. Open the device and sign in again |
| "Waiting for Cora Max" | A GHL controller or Inkbird monitor you just added: it shows up once a Cora Max has read it |
| Older readings while you're away | Normal for Apex, Red Sea and Jecod without a Cora Max at the tank (see above) |
| Nothing at all | It's never reported. Check the tank assignment and the connection |

When a device stops reporting, Cora can alert you. The timings are in [Alerts and thresholds](/help/mobile-alerts). For anything else, see [Troubleshooting](/help/troubleshooting).

## Removing a device {#removing-a-device}

Open the device and tap **Remove device**, or swipe its row to the left on the Devices tab. Cora asks you to confirm: *"{name} will be removed from Cora. It is not reset or changed on the device itself."*

**Your readings are kept.** Removing a device stops Cora collecting new data from it. The history it already gathered stays on the tank, and any widget that used it keeps its past readings.

You lose the live link. If the device connected through a manufacturer account, you also lose the saved sign-in, so you'll need to sign in again if you add it back.

:::tip Quieten a noisy device without removing it
If a device works fine but alerts too often, change its thresholds or notification settings in [Alerts and thresholds](/help/mobile-alerts). You keep the connection and the data, and the noise stops.
:::
