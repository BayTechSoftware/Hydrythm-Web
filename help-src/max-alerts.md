---
title: Alerts on Cora Max
description: What to do when an alert pops up on Cora Max, how to snooze or dismiss it, change alert thresholds at the wall, and set the alert sound.
section: Cora Max
reviewed: 2026-10-13
order: 8
group: Alerts and automation
twin: mobile-alerts
---

This page covers what Cora Max does when something needs your attention, and what you can change at the wall. How ranges, rules and phone notifications work is in [Alerts and thresholds](/help/mobile-alerts).

## When an alert appears

When a reading goes out of range, a device reports a fault, a dose is missed or a supply runs low, Cora Max shows the alert in the middle of the screen. There are three buttons under it.

1. **Respond by voice** starts a conversation with Cora about this alert, so you don't have to tap anything else. More about this in [Talking to Cora](/help/max-voice).
2. **Snooze** silences the alert on this Cora Max for a while. The button shows how long, for example **Snooze 1 h**. That's the cooldown set for this alert in Cora Mobile's alert settings, and it can be as long as 1 week (handy for something like a low reagent level that won't change for days).
3. **Dismiss** closes the alert now. It stays quiet on this screen until the problem is gone. If it comes back later, you'll get a new alert.

When the alert is about a doser, such as a DŌS or ReefDose head running low or a missed dose, the card also has an **Open DŌS** or **Open ReefDose** button (**Open Versa** for an EcoTech Versa). It takes you to that doser's page, where its alerts are set.

If Snooze or Dismiss shows an error, try once more. If it keeps failing, see [An alert is not clearing](/help/troubleshooting#an-alert-is-not-clearing).

:::note Snooze only affects this Cora Max
While an alert is snoozed or dismissed, this Cora Max stops popping it up, sounding it and speaking it, and it leaves the top bar. Your phone still gets its notifications, other Cora Max screens still show the alert, it stays in **Notification history**, and your alert settings don't change.
:::

## Alerts in the top bar

Every active alert also shows up as a small tag in the top bar, big enough to spot from across the room. If there are more than fit, you'll see **+2** (or however many).

- Tap a tag to bring that alert back to the middle of the screen.
- Tap **+2** to open **Active alarms**, the list of everything that's active. Tap one in the list to open it.

## The notification inbox

**Settings → Cora Max Settings → Notification history** is the inbox for your whole account. It holds every briefing, alarm and account notice for your system, including the ones this screen didn't raise and anything your phone missed. When a reading goes out of range and comes back, you see both.

## Editing thresholds

![A tank's settings on Cora Max, with Alert thresholds, Units and Primary Cora Max](img/max-tank-settings.webp "Alert thresholds and Units first, then the Primary Cora Max for this tank.")

Tap the tank name in the top bar and choose **Alert thresholds**, or go to **Settings → [your tank] → Alert thresholds**. Both open the same ranges you see on your phone, and a change you make here applies everywhere.

You can also change a threshold by long-pressing its widget on the dashboard, or by voice: *"Hey Cora, set the pH alert to 7.9 to 8.4."* Cora tells you the change and waits for your OK.

Each parameter in the list has its own switch. An alert you've switched off says **Alert off**. Cora keeps its range, but it doesn't grade that reading while it's off. The widget stays neutral grey and never raises an alert. If a parameter has no alert yet, it says **No alert set**, and **Add alert** sets one up with the range shown.

![The Alert thresholds list on Cora Max](img/max-alerts.webp "Each reading has its own switch. A reading with no alert shows No alert set and an Add alert button.")

The threshold sheet has the same switch at the top, next to **Alert on** or **Alert off**. If you save a new range on an alert that's off, Cora asks **Turn this alert on?** Tap **Turn on** to switch it on with the new values, or **Keep off** to save them and leave it off.

## Device and supply alerts {#doser-alerts}

Equipment with something that runs out has an **Alert settings** button on its page on Cora Max. That's a Trident (reagents and waste), DŌS heads, Red Sea ReefDose, ReefATO+ and ReefMat, and the EcoTech Radion, VorTech and Versa. Pick the level you want to hear about, and you get one notification when it's passed. On a DŌS head, **Missed dose alerts** also tells you when the head misses its scheduled doses.

What each doser alert means is in [Doser alerts](/help/mobile-device-control#doser-alerts).

:::note Beta
**Beta.** EcoTech is in Beta and only open to Beta users. If you are not a Beta user you will not see it in **Add device**. To ask for Beta access, contact [support](/support.html).
:::

## Alert sound, spoken alerts and waking the screen

These belong to this screen only. Find them in **Settings → Cora Max Settings**.

- **Alert sound** (under **SOUND & VOICE**) plays a tone when a new alert arrives. Its slider sets the volume.
- **Spoken alerts** (under **SOUND & VOICE**) has Cora say the alert out loud.
- **Wake screen on alarm** (under **DISPLAY**) lights up a dimmed screen when an alert arrives. Critical alerts always wake it.

To stop a Cora Max showing alerts on its screen at all, open Cora Mobile, go to **Devices →** your Cora Max, and turn off **Alerts**. Notification history and your phone's notifications don't change.

:::note One alert for the whole account
Each device doesn't raise its own copy of an alert. Cora Max, your phone and any other screen show the same one, and it clears on all of them when the reading is back in range.
:::
