---
title: Updates and recovery
description: How Cora Max updates itself, the install window and update channel, checking the version, the Recovery PIN, and what to do if Cora Max won't start or shows a support code.
section: Cora Max
reviewed: 2026-10-17
order: 15
group: Settings and account
---

Cora Max keeps itself up to date. This page explains when updates install, how to check your version, and how to get Cora Max going again if it won't start normally.

## Automatic updates

New versions download in the background as soon as they're out. They install inside the **Install window**, 3 to 5 in the morning unless you change it, so the screen doesn't restart while you're looking at it. When a version brings release notes, Cora Max shows them.

You don't need to do anything to stay current.

## Checking the version and update settings {#checking-the-version-and-update-settings}

![Network and updates on Cora Max](img/max-updates.webp "Firmware Update, in the NETWORK & UPDATES section of Cora Max Settings.")

Your version is on the card at the top of **Settings → Cora Max Settings** (*Cora Max · firmware 0.28.170*), and under **HELP & ABOUT → About**.

**Settings → Cora Max Settings → Firmware Update** (in **NETWORK & UPDATES**) shows the version you're on and whether an update is waiting. Tap **Check for updates** to look now, or **Download & install** when one is there.

Under **Update settings** on the same screen:

- **Install window** sets the hours updates may install, with a **Start** and **End** time, in this screen's local time. The time zone is set in Cora Mobile, under **Devices →** your Cora Max **→ Time zone**.

To see whether this screen is reading your devices and saving to Cora Cloud, go back to **Cora Max Settings** and scroll to **STATUS**. It shows each tank's **Polling status**, **Last poll**, **Last cloud write** and **Cloud save**.

If an update downloads slowly, check your connection with the **Network speed test** on the same screen. **Run test** downloads up to 16 MB of the update file from Cora Cloud, for 20 seconds at most, and shows the speed in MB/s.

## When an update is available

A prompt tells you what's new and gives you two choices.

- **Update now** installs right away and restarts. It takes about a minute. Keep Cora Max powered.
- **Snooze 24 hours** hides the prompt and asks you again a day later.

While an update is waiting, a small dot shows on the **Settings** icon in the top bar and on the **Firmware Update** row. The dot stays through a snooze, so you can still see an update is there. It goes away while the update installs.

If you leave it, the update installs itself in the **Install window**.

You can also start it from your phone: in Cora Mobile, open **Devices →** your Cora Max and tap **Update to v…**.

:::note You don't lose readings during an update
Your data lives in your account. When Cora Max restarts, it comes back with the same tanks, dashboards and history.
:::

## Recovery {#recovery}

Recovery is a maintenance mode for when Cora Max won't start normally, or when you need to fix its setup without a laptop.

1. Hold **five fingers** in the top-right corner of the screen for **ten seconds**.
2. The **Recovery PIN** box opens. Type the 6-digit PIN and tap **Enter**.

You saw the PIN when you paired Cora Max. You'll also find it in Cora Mobile under **Devices →** your Cora Max **→ Recovery PIN**. Cora Max itself never shows it, so a guest or a child leaning on the screen can't get into recovery.

If you type the wrong PIN three times, recovery locks for 30 seconds, and for longer after each further wrong try. **Too many attempts** tells you how long to wait. If Cora Max has never been online since pairing, it has no PIN yet and shows **Recovery is unavailable**. Connect it to Wi-Fi first.

From **Recovery** you can:

- **Re-do Wi-Fi setup**: pick a new Wi-Fi network and password
- **Re-pair this device**: clear the pairing and set it up again with Cora Mobile
- **Force OTA check**: check for updates now
- **Factory reset**: remove the pairing and every setting on the screen

Tank data already saved to Cora Cloud is kept in every case.

If Cora Max fails to start several times in a row, it can also roll itself back to the previous version.

:::note The same gesture unlocks child lock
If [Child lock](/help/max-settings#child-lock) is on, holding five fingers in the corner also unlocks the screen. Tap **Cancel** in the **Recovery PIN** box if you only wanted to unlock.
:::

:::warning A screen in recovery isn't controlling anything
Your controller keeps running its own programming. But an [automation](/help/mobile-automation) step that **this Cora Max** has to carry out can't run while it's in recovery. The rule fires, but the step never reaches the equipment.
:::

## If Cora Max shows "Cora Max hit a problem"

This screen means something went wrong while Cora Max was starting or running. It shows a **Support code** (it starts with *CXB-*).

1. Write down the support code.
2. Wait. Cora Max restarts itself in about 10 minutes. To restart it now, hold five fingers in the top-right corner for 10 seconds.
3. If it keeps happening, email **[cora@coraiq.tech](mailto:cora@coraiq.tech)** with the support code.

## If a unit does not restart

Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)** with the version shown on screen and the message it shows. Don't re-pair it first. The pairing state often helps work out what happened.
