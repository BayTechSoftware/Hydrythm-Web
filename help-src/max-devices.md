---
title: Devices and device health
description: What Cora Max can see, which device reads each tank, and what to check when readings stop.
section: Cora Max
reviewed: 2026-09-27
order: 7
group: Equipment
---

**Settings → Devices** lists the equipment Cora Max can see and how each device is doing.

## The device list

![The device list](img/max-devices.webp "Filter by tank, then each device with a one-line summary of what it holds.")

Cora Max sees the same equipment as your phone, because they both read the same account.

Use the filter chips at the top to show **All tanks** or just one. Each entry has a status dot, a one-line summary of what the device holds (*21 outlets · 4 feeds*, *19 tests left*) and the tank it belongs to.

Adding and setting up equipment is easier on your phone. More about this in [Adding, editing and removing devices](/help/mobile-devices).

## Primary Cora Max: which device talks to your equipment

The **Primary Cora Max** is the Cora Max (or other Cora device) that reads a tank's controller and other equipment for the whole account. Each tank only needs one device doing this. Every other screen shows what it reads.

To see or change it, open **Settings → [your tank] → Primary Cora Max**. You have two options.

- **Any active (automatic)** means every online Cora device that can reach this tank's equipment shares the work, and the latest write wins. Use this unless you have a specific reason to pin one device.
- **Pin one device** means only that device reads the equipment. If it goes offline, nothing reads this tank's equipment until you pin a different one or switch back to Any active (automatic).

You set this once for the tank, and it applies to every Cora screen. You can change it from any Cora Max that shows the tank, or from Cora Mobile. More about this in [More than one Cora device](/help/mobile-multi-device).

:::note Primary Cora Max and Cora Assistant are two separate settings
Primary Cora Max decides which device **reads your equipment**. **Cora Assistant** decides which device **answers "Hey Cora"**. If you have more than one Cora Max, you can set them separately. More about this in [Talking to Cora](/help/max-voice).
:::

## If a tank's readings stop

If one tank's readings stop while another tank on the same screen keeps updating, start here.

1. Open **Settings → [that tank] → Primary Cora Max**. Check that a device is assigned and that it's online.
2. If another Cora Max for this tank shows **Main Cora offline** in its top bar, the primary has lost its connection. What the status tag means is explained in [The Cora Max home screen](/help/max-tour).
3. **Settings → Cora Max Settings → Network & Updates → Device polling** shows how often this Cora Max reads your devices. You can only view it here. It's set from Cora Mobile.

If that doesn't help, have a look at [Troubleshooting](/help/troubleshooting).

## Managing a Cora Max from your phone

Open the Cora Max from the **Devices** tab on your phone. You'll see its variant, firmware version and when it was last seen. You can also rename it or change some of its settings without walking over to it.

![Cora Max settings from the phone](img/max-from-phone.webp "Polling interval, brightness, volume, on-screen alerts and dim timer.")

These settings only affect **that one screen** (its brightness, volume, on-screen alert banners and dim timer), just as if you'd changed them at the wall. Turning off on-screen alerts doesn't change alert history or push notifications.

Which tanks a Cora Max shows, and which device is its Primary Cora Max for each tank, apply to the whole account. You can change them from either device, as described above.

:::note Check device health before changing anything
The **Status** section of **Settings → Cora Max Settings** on this screen shows polling status, last poll time and last cloud write for each tank. It doesn't change anything. Use it to find out what's going on before you change a setting.
:::
