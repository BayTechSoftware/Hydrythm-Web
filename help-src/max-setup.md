---
title: Setting up Cora Max
description: Pair a new Cora Max with Cora Mobile over Bluetooth, connect it to Wi-Fi, pick its tanks, and move it to another tank later.
section: Cora Max
reviewed: 2026-10-13
order: 1
group: Getting started
twin: mobile-setup
---

This page takes you from a new Cora Max to a working wall screen. You pair it from your phone over Bluetooth, and you don't type anything on the screen itself.

:::tip Set your tanks up on your phone first
Cora Max shows the tanks and devices on your account, and it can't create a tank itself. [Set them up in Cora Mobile](/help/mobile-setup) first. Cora Max picks them up as soon as you pair it.
:::

## What you need {#what-you-need}

- Cora Max, plugged in and switched on. It's meant to stay plugged in.
- Cora Mobile on your phone, signed in, with **at least one tank** already created.
- Bluetooth turned on on your phone, and the phone close to Cora Max.
- Your Wi-Fi network name and password.

Put Cora Max where you can see it from across the room and talk to it, away from splashes and salt creep.

## What the screen shows first {#what-the-screen-shows-first}

Turn Cora Max on. It shows a pairing screen that says **Open the Cora app on your phone**, then **Tap Add Device.** and **Pick this Cora Max from the Devices list.** Below that it shows **Discoverable as** and its name, ending in a short code. If you're pairing more than one, that code tells them apart on your phone.

![The Cora Max pairing screen, waiting for your phone](img/max-pairing-screen.webp "Waiting for your phone. The bottom line shows the name your phone will list.")

The same screen has a short notice about integrations with other makers' equipment. The Terms you accepted in Cora Mobile also cover Cora Max.

## Pairing from your phone {#pairing}

Everything else happens in Cora Mobile. A sheet walks you through five steps, shown across its top: **Connect · WiFi · Auth · Tanks · Done**.

1. **Find it.** Open the **Devices** tab, tap **Add Device**, then **Cora**. The **Add Your Cora** screen lists Cora devices on your network and nearby setup devices found over Bluetooth. Tap **Scan** if yours isn't there yet, then tap your Cora Max.

   ![The Add Your Cora screen in Cora Mobile, scanning for devices](img/mobile-add-device.webp "Add Device, then Cora. Cora Mobile looks on your Wi-Fi and over Bluetooth, with Enter IP Address Manually below.")

2. **Connect.** Your phone connects to Cora Max over Bluetooth and shows its MAC address, firmware, variant and hardware revision. Check it's the right one, then tap **Continue**.

3. **WiFi.** Pick your network from the list, or tap **Rescan**, and type the password on your phone. From here on your phone talks to Cora Max over Wi-Fi, so keep the phone on the same network.

4. **Auth.** Your phone links Cora Max to your account. This runs by itself, and Cora Max shows its own progress, such as **Verifying your account…** and **Setting up your tank…**.

   ![The Cora Max pairing screen showing Verifying your account](img/max-pairing-verifying.webp "Cora Max shows each step while your phone links it to your account.")

5. **Tanks.** Under **Assign Tanks**, pick the tanks this Cora Max will manage, **up to four**.

6. **Done.** Your phone says Cora Max is set up and shows a **Recovery PIN**. Tap the button that opens your tank's dashboard, or **Go to Devices**. Cora Max shows **Paired**, then **Opening dashboard…**.

:::warning Write the Recovery PIN down
The **Recovery PIN** has six digits and it's the only way into recovery on that Cora Max. To use it, hold five fingers on the top-right corner of the screen for ten seconds, then enter the PIN. Recovery lets you redo Wi-Fi, pair again, check for an update or factory reset. You can find the PIN again on your phone under **Devices → your Cora Max → Recovery PIN**, but never on Cora Max itself.
:::

### If pairing gets stuck {#if-pairing-gets-stuck}

- **Bluetooth is off. Turn it on, then tap Scan again.** Turn Bluetooth on and scan again.
- **Bluetooth permission is off for Cora.** Allow Bluetooth for Cora in your phone's settings, then tap **Scan**. An iPhone may also ask for local network access. Allow that too.
- **No nearby Cora setup devices were found over Bluetooth.** Stand next to Cora Max, check it still shows the pairing screen, and scan again.
- **No Tanks Found** at the Tanks step. Your account has no tank yet. Create one in Cora Mobile, then retry the step.
- **Not linked to your tank yet** at the end. Cora Max is paired, but the tank link didn't finish. Tap **Retry now**. Until it finishes, alerts for this screen use default ranges.

More fixes in [Troubleshooting](/help/troubleshooting#pairing-a-cora-max-fails).

## After pairing {#after-pairing}

Cora Max now sees the same tanks, devices, readings and records as your phone.

- If one of your tanks had a Cora Max before, Cora Max asks **Restore previous layout for this tank?** **Restore** brings back the display, sound and alert settings the old one saved. **Start fresh** skips them.
- A tank with no readings yet shows **No readings yet** and a **Log your first test** button.
- Cora Max builds a starting dashboard from your tank profile. It doesn't copy the one on your phone.

You can pair more than one Cora Max to the same account, say one in the fish room and one in the living room. Each one can show different tanks and has its own layout. If two show the same tank, [More than one Cora device](/help/mobile-multi-device) explains which one reads the equipment.

## Building the dashboard {#building-the-dashboard}

The big-screen dashboard is a fixed grid, and everything has to fit on one screen. The quickest way to arrange it is from your phone: open the **Devices** tab, tap your Cora Max, then tap **Dashboard layout** on the tank's card. You can also do it at the wall from the tank menu.

To reuse a layout from another Cora Max or another tank, load it from **My dashboards** in the editor. More in [Editing the Cora Max dashboard](/help/max-dashboard-editing).

## Moving Cora Max to another tank {#changing-which-tanks-it-shows}

You change which tanks a Cora Max shows on your phone. Cora Max's own settings can't do it.

1. In Cora Mobile, open the **Devices** tab and tap your Cora Max.
2. Under **Tanks**, tap **Add Tank** and pick the tank. A Cora Max takes up to four. When it already has four, the button is gone, so remove one first.
3. To take a tank off this screen, tap the red remove icon (**Remove tank**) on that tank's card, then tap **Remove**.

To move Cora Max from one tank to another, add the new tank, then remove the old one. The new tank gets a starting dashboard built from its profile. Arrange it with **Dashboard layout**.

If this Cora Max was the pinned Primary Cora Max for the tank you removed, that pin is cleared and the tank goes back to **Any active (automatic)**. More in [Devices and device health](/help/max-devices).

## Updates {#updates}

Cora Max updates itself. A new version downloads in the background and installs at night. Your version is shown at the top of **Settings → Cora Max Settings**. More in [Updates and recovery](/help/max-updates).

## Moving it to a different Wi-Fi network {#moving-it-to-a-different-network}

Go to **Settings → Cora Max Settings → Wi-Fi**, pick the new network and enter the password. Cora Max stays paired, so you don't need to set it up again.
