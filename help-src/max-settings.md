---
title: Cora Max settings
description: Every Cora Max setting, from rename, brightness, night dimming, speaker and wake word to child lock, language, Wi-Fi, re-pairing and factory reset.
section: Cora Max
reviewed: 2026-10-13
order: 14
group: Settings and account
twin: mobile-settings
---

Open settings with the **gear** at the far right of the top bar.

![Settings on Cora Max, with the CORA group and one row per tank](img/max-settings.webp "The CORA group (Automations, Devices, Cora Assistant), then one row per tank.")

Settings has three groups. **CORA** holds things that apply to all the Cora devices in your household. **TANKS** has one row per tank. The last row, **Cora Max Settings**, is everything about this screen alone.

:::note Two kinds of setting
Some settings belong to your **account**. They're the same whichever phone or Cora Max you look at, and changing one changes it everywhere. Others belong to **this screen** only, like its brightness or Wi-Fi. The CORA and TANKS groups are account settings. Cora Max Settings holds this screen's own settings.
:::

## CORA

These apply to every Cora device on your account.

| Row | Opens |
|---|---|
| **Automations** | Every scene for all your tanks, with a filter by tank. More in [Scenes on Cora Max](/help/max-automation) |
| **Devices** | The equipment Cora controls, for all your tanks. Tap the pencil to rename a device. More in [Devices and device health](/help/max-devices) |
| **Cora Assistant** | Which device answers when someone says "Hey Cora." More in [Talking to Cora](/help/max-voice) |

## TANKS

Each tank has a row that opens its own settings.

- **Alert thresholds** sets the healthy range for each reading. More in [Alerts on Cora Max](/help/max-alerts#editing-thresholds).
- **Units** picks the units this tank uses for salinity, temperature, alkalinity, volume, phosphate and nitrate. With **Auto**, each reading shows in the unit its source recorded it in. If you pick a specific unit, everything on this tank is converted to it, on every screen and when the Assistant speaks.
- **Primary Cora Max** is the device that reads this tank's equipment. More in [Devices and device health](/help/max-devices).
- **Dashboard layout** is this tank's Cora Max layout. More in [Editing the Cora Max dashboard](/help/max-dashboard-editing).
- Under **RECORDS & REPORTS**: **Log parameters**, **Journal**, **Maintenance**, **Livestock**, **Reef Buddy**, **Health Reports**, **ICP Reports** and **Activity**. More in [Journal, livestock and maintenance](/help/max-records) and [Reef Buddy and reports](/help/max-intelligence).

## Cora Max Settings: everything about this screen

The last row in Settings carries this Cora Max's name. It opens everything that applies to **this screen only**.

At the top is a card with this screen's name and its firmware version (*Cora Max · firmware 0.28.170*).

- Tap the pencil (**Rename this device**) to give it a new name, for example "Living room".
- **Show details** lists its **Cora ID**, **MAC address**, **Wi-Fi network**, **IP address**, its tanks and the account it's paired to. Support may ask you for these.

Below the card are these sections.

| Section | Covers |
|---|---|
| **DISPLAY** | **Brightness**. **Dim after** and **Dim level**: how long with no touch before the screen dims, and how dim it gets. **Night dimming**, with **From**, **To** and **Night brightness**. **Show clock** in the top bar. **Wake screen on alarm** |
| **SOUND & VOICE** | **Speaker** (**Internal**, **3.5 mm** or **BT**), **Alert sound** and its volume, **Spoken alerts**, and **Wake word** on or off. More in [Talking to Cora](/help/max-voice#sound-and-wake-word-settings) |
| **REEF BUDDY** | **Reef Buddy briefing** reads the morning briefing aloud. **Briefing time** is when it arrives, the same on every device |
| **CHILD LOCK** | **Child lock** on or off, and **Lock after**. See [Child lock](#child-lock) below |
| **NOTIFICATIONS** | **Notification history**, the inbox for your whole account with every briefing, alarm and account notice |
| **LANGUAGE** | The one language your whole account uses: English, Deutsch, Español, Français, Italiano, Polski or Türkçe. See the note below |
| **NETWORK & UPDATES** | **Wi-Fi**, **Firmware Update**, and **Device polling**, which shows how often this Cora Max reads your devices (you change it in Cora Mobile) |
| **STATUS** | One card for each tank this screen shows, with **Polling status**, **Last poll**, **Last cloud write** and **Cloud save**. View only |
| **HELP & ABOUT** | **Help & Support** (contact support or report a problem) and **About** (version and licenses) |
| **RESET** | **Re-pair this device** and **Factory reset**. See below |

When the screen has dimmed, your first tap only wakes it. It doesn't press anything.

:::note Language applies to your whole account
When you change **Language**, every phone and every Cora Max on your account switches with it. New reports, alerts and briefings come in the new language. Reports and alerts you already have stay in the language they were written in and aren't translated again.
:::

![Notification history on Cora Max, listing alarms and recoveries](img/max-notifications.webp "Alarms and their recoveries, newest first, each with its tank name.")

Recoveries are logged as well as alarms. So when a parameter goes out of range and comes back, you see both halves.

## Child lock {#child-lock}

Child lock stops small hands from changing anything on a screen that children or visitors can reach. Readings, charts and alerts keep updating. Only the controls stop.

To turn it on, go to **Settings → Cora Max Settings → CHILD LOCK**, turn on **Child lock**, and pick **Lock after**. The choices are 30 seconds, 1, 2, 5, 15 or 30 minutes (1 minute unless you change it).

Cora Max then locks itself after the **Lock after** time with no touch. Every touch resets that time. While it's locked:

- Every tap is ignored, and **Locked** shows in the middle of the screen for a few seconds. A tap still wakes a dimmed screen.
- The volume keys stop changing the volume.
- Cora still answers questions by voice, but refuses anything that changes your equipment.

To unlock, do either of these:

1. Press **Volume Up** or **Volume Down** three times within two seconds. The two seconds start at the first press.
2. Hold five fingers in the top-right corner of the screen for ten seconds.

**Unlocked** shows for a moment. The lock comes back after the **Lock after** time with no touch. To turn child lock off for good, unlock, then turn off **Child lock** in Settings.

:::warning The five-finger hold also opens the Recovery PIN box
Holding five fingers in the corner is also how you get into [Recovery](/help/max-updates#recovery). So after the screen unlocks, a **Recovery PIN** box opens as well. Tap **Cancel** to go back to the unlocked screen. Cancelling doesn't count as a wrong PIN. If Cora Max has no PIN yet, you see **Recovery is unavailable** instead. Tap **OK**. The volume-key unlock doesn't open recovery.
:::

Child lock isn't a security lock. Anyone who sees how you unlock it can do the same.

## Pairing, re-pairing and factory reset

**Cora Max Settings → RESET** has two options.

**Re-pair this device** clears this screen's pairing and takes it back to the pairing screen.

**Factory reset** also clears every preference saved on this screen. Its confirmation tells you what's cleared and what's kept.

Neither one touches the tank data already saved to Cora Cloud. Both remove this Cora Max from your account and make it forget its Wi-Fi network, so you pair it again from Cora Mobile like a new one. If Cora Max can't reach Cora Cloud to remove itself, it says *This Cora Max is still listed in the Cora app. Remove it from there too.* Open it in Cora Mobile under **Devices** and choose **Remove device**.

![The HELP & ABOUT and RESET sections of Cora Max Settings](img/max-factory-reset.webp "The RESET section, with Re-pair this device and Factory reset.")

You can also reset a Cora Max from your phone, in Cora Mobile under **Devices →** your Cora Max **→ Danger zone**. That helps when the screen is out of reach or locked.

| Option | Where | Wi-Fi | What happens |
|---|---|---|---|
| **Re-pair this device** | On Cora Max | Forgotten | Back to the pairing screen. Pair it from Cora Mobile |
| **Factory reset** | On Cora Max | Forgotten | Pairing and every on-screen setting cleared. Pair it from Cora Mobile |
| **Reset display** | Cora Mobile, **Danger zone** | Kept | Back to the setup screen the next time it's online. Pair it again over Bluetooth |
| **Remove device** | Cora Mobile, **Danger zone** | | Removed from your account and its tanks. It can be paired again later |

In every case, tank data already saved to your account is kept. Pair the device to a tank again and it comes back. What you lose is the screen's own setup, like its display, sound and voice settings.

:::note You may get your layouts back
Before a reset, Cora Max saves a copy of its configuration. If you pair it back to the **same tank**, it offers **Restore previous layout for this tank?** Take it, or choose **Start fresh** if you wanted a clean screen.
:::

## Which tanks this screen shows

A Cora Max can show one tank or several, and you switch between them from the top bar. You choose which tanks it shows **on your phone**, under **Devices →** your Cora Max. More in [Changing which tanks it shows](/help/max-setup#changing-which-tanks-it-shows).

## Updates

Cora Max keeps itself up to date. Updates download in the background and install inside the update window. More in [Updates and recovery](/help/max-updates).
