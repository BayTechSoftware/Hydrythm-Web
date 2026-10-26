---
title: Devices and device health
description: See and rename the equipment Cora Max reads, choose which Cora Max reads each tank, fix a tank whose readings stopped, and manage a Cora Max from your phone.
section: Cora Max
reviewed: 2026-10-17
order: 7
group: Equipment
twin: mobile-devices
---

**Settings → Devices** on Cora Max lists the equipment it can see and how each device is doing. The devices icon in the top bar opens the same list, filtered to the tank on screen.

## The device list {#the-device-list}

![The device list on Cora Max, filtered by tank and grouped by brand](img/max-devices.webp "Filter by tank, then each device grouped by brand, with a one-line summary and its tank.")

Cora Max sees the same equipment as your phone, because they both read the same account.

In the list, the Cora families come first, then every brand from A to Z.

Use the filter chips at the top to show **All tanks** or just one. Devices are grouped by brand. Each entry has a status dot (grey when Cora doesn't know yet, green when it's working, orange for a warning or fault, red when it's offline), a one-line summary of what the device holds (*21 outlets · 4 feeds*, *19 tests left*), the tank it belongs to and when it was **Last seen**.

Tap a device to open its page. Every device page opens with a **Status** section. What each page can do is in [Controlling equipment from Cora Max](/help/max-device-control).

If the list says **Still loading some devices: this list may be incomplete.**, give it a moment.


### Renaming a device {#renaming-a-device}

Tap the pencil on a device's row, or on its page, and type the new name. Leave the name empty to go back to the device's own name. The name is shared with your phone, so it changes there too.

### Adding and removing devices {#adding-and-removing-devices}

You add, assign and remove devices on your phone. Cora Max shows and controls them. With no devices yet, this screen says **Add devices in the Cora app.** More in [Adding, editing and removing devices](/help/mobile-devices).

## Primary Cora Max: which device talks to your equipment {#primary-cora-max}

The **Primary Cora Max** is the Cora Max (or other Cora device) that reads a tank's controller and other equipment for the whole account. Each tank only needs one device doing this. Every other screen shows what it reads.

To see or change it, open **Settings → [your tank] → Primary Cora Max**. You have two options.

- **Any active (automatic)** means every online Cora device that can reach this tank's equipment shares the work, and the latest write wins. Use this unless you have a reason to pin one device.
- Pin one device, so only that device reads the equipment. If it goes offline, no other Cora Max takes over. Only Cora Mobile, open on the same Wi-Fi, reads the equipment until you pin a different one or switch back to **Any active (automatic)**.


You set this once for the tank, and it applies to every Cora screen. You can change it from any Cora Max that shows the tank, or from Cora Mobile (**Make Primary Cora Max** on the Cora Max's page). More in [More than one Cora device](/help/mobile-multi-device).

:::note Primary Cora Max and the Answering device are two separate settings
Primary Cora Max decides which device **reads your equipment**. The **Answering device** in Cora Mobile decides which one **answers "Hey Cora"**. If you have more than one Cora Max, you can set them separately. More in [Talking to Cora](/help/max-voice).
:::

## If a tank's readings stop {#if-a-tanks-readings-stop}

If one tank's readings stop while another tank on the same screen keeps updating, start here.

1. Open **Settings → [that tank] → Primary Cora Max**. Check that a device is assigned and that it's online.
2. If another Cora Max for this tank shows **Main Cora offline** in its top bar, the primary has lost its connection. What the status tag means is explained in [The Cora Max home screen](/help/max-tour#what-the-status-pill-means).
3. **Settings → Cora Max Settings → NETWORK & UPDATES → Device polling** shows how often this Cora Max reads your devices. You can only view it here. It's set from Cora Mobile.
4. Check the **Status** section of **Settings → Cora Max Settings**. It shows polling status, last poll time and last cloud write for each tank, without changing anything.

If that doesn't help, have a look at [Troubleshooting](/help/troubleshooting).

## Managing a Cora Max from your phone {#managing-a-cora-max-from-your-phone}

Open the **Devices** tab on your phone and tap the Cora Max. The top card shows its variant, firmware and when it was last seen. From there you can rename it, and when there's a new version, tap **Update to v…** to install it now. The **Recovery PIN** card sits just below.

![A Cora Max's page in Cora Mobile, showing Child lock, Device Polling, Time zone and Assigned Tanks](img/max-from-phone.webp "One Cora Max's own settings on your phone: Child lock, Device Polling and Time zone, then its tanks.")

These settings only affect **that one screen**, just as if you'd changed them at the wall:

| Section | Settings |
|---|---|
| **Display** | **Brightness**, **Dim after** |
| **Sound & Voice** | **Alert sound** turns the alert chime on that screen on or off, and **Alert volume** sets how loud it is. Alerts still show on screen, and alert history and push notifications don't change |
| **Child Lock** | **Child lock** locks that screen's touchscreen and stops it switching equipment by voice |
| **Network & Updates** | **Device Polling** (how often it reads your equipment) and **Time zone** (used for night dimming and the update window) |

Under **Tanks**, each tank this Cora Max shows has a card with **Dashboard layout**, **Edit tank** and its polling device. **Add Tank** and the remove icon change which tanks it shows, and those changes apply to the whole account. You can only make them on your phone. The steps are in [Setting up Cora Max](/help/max-setup#changing-which-tanks-it-shows). Which device is the Primary Cora Max for a tank can be changed from either your phone or Cora Max.

Under **Reset**, **Reset display** sends the screen back to its pairing screen. It stays on your Wi-Fi, so you can pair it again over Bluetooth, and your tank data is kept. **Remove device** takes it off your account. Your tank readings are kept, and you can pair it again later.
