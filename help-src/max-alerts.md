---
title: Alerts on Cora Max
description: Alert tags in the top bar, the notification inbox, and changing thresholds at the wall.
section: Cora Max
reviewed: 2026-10-13
order: 11
group: Alerts
---

## Alerts in the top bar

When a reading is out of range, it shows up as a small tag in the top bar, big enough to spot from across the room. If there are more than fit, you'll see **+2** (or however many). Tap a tag to see them all.

## When an alert appears at the wall

When a reading goes out of range, Cora Max also shows the alert in the middle of the screen. There are three buttons under it.

1. **Respond by voice** lets you talk to Cora about the alert without typing or tapping anything else. More about this in [Talking to Cora](/help/max-voice).
2. **Snooze [duration]** silences the alert on this Cora Max for a while. The button shows how long, for example **Snooze 1 h**. That's the cooldown set for this alert in Cora Mobile's alert settings, and it can be as long as 1 week (handy for something like a low reagent level that won't change for days).
3. **Dismiss** closes the alert now. It stays quiet on this screen until the reading is back in range. If the problem comes back later, you'll get a new alert.

When the alert is about a doser, such as a DŌS or ReefDose head running low or a missed dose, the card also has an **Open DŌS** or **Open ReefDose** button. It takes you to that doser's page, where its alerts are set.

If Snooze or Dismiss shows an error, try once more. If it keeps failing, have a look at [Troubleshooting](/help/troubleshooting).

:::note Snooze only affects this Cora Max
While an alert is snoozed or dismissed, this Cora Max stops popping it up, sounding it and speaking it, and it leaves the list in the top bar. Your phone still gets its notifications, other Cora Max screens still show the alert, it stays in **Notification history**, and your alert settings don't change.
:::

## The notification inbox

**Settings → Cora Max Settings → Notifications → Notification history** is the inbox for your whole account. It holds every briefing, alarm and account notice for your system, including the ones this screen didn't raise and anything your phone missed.

## Editing thresholds

![Tank settings on Cora Max](img/max-tank-settings.webp "Each tank has its own journal, maintenance, alerts, livestock and briefing.")

Tap the tank name in the top bar and choose **Alerts**, or go to **Settings → [your tank] → Alert thresholds**. Both open the same ranges you see on your phone, and a change you make here applies everywhere.

You can also change a threshold by long-pressing its widget on the dashboard.

Each parameter in the list has its own switch. An alert you've switched off says **Alert off**. Cora keeps its range, but it doesn't grade that reading while it's off. The widget stays neutral grey and never raises an alert. If a parameter has no alert yet, it says **No alert set**, and **Add alert** sets one up with the range shown.

The threshold sheet has the same switch at the top, next to **Alert on** or **Alert off**. If you save a new range on an alert that's off, Cora asks **Turn this alert on?** Tap **Turn on** to switch it on with the new values, or **Keep off** to save them and leave it off.

How ranges and rules work is explained in [Alerts and thresholds](/help/mobile-alerts).

## Doser alerts

On a DŌS page, each head has an **Alert settings** button. It sets that head's days-left and remaining levels, and has a **Missed dose alerts** switch that tells you when the head misses its scheduled doses.

:::note One alert for the whole account
Each device doesn't raise its own copy of an alert. Cora Max, your phone and any other screen show the same one, and it clears on all of them when the reading is back in range.
:::
