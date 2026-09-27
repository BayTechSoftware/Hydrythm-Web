---
title: Alerts on Cora Max
description: Alert pills in the top bar, the notification inbox, and editing thresholds at the wall.
section: Cora Max
reviewed: 2026-09-27
order: 11
group: Alerts
---

## Alert pills

Anything currently out of range appears as a pill in the top bar, with **+n** when there are more than fit. Tap a pill to see the full list.

The pills are the reason Cora Max works as a wall display: the tank's problems are visible from across the room without touching anything.

## When an alert appears at the wall

When a reading goes out of range, Cora Max shows the full alert in the middle of the screen, not just as a pill. Three buttons sit under it:

1. **Respond by voice**: talk to Cora about the alert without typing or tapping anything else. See [Talking to Cora](/help/max-voice).
2. **Snooze [duration]**: stop the push notifications for this alert for a set time, without turning the alert off. The button's own label shows how long, for example **Snooze 1 h**. This is the same cooldown period set for this alert type in Cora Mobile's alert settings, and it can be as long as **1 week** for something like a low reagent level that will not change for days.
3. **Dismiss**: close the alert now. It stays quiet until the reading returns to its normal range, then re-arms itself, so a repeat of the same problem raises a new alert rather than staying silent forever.

**If it does not work:** if Snooze or Dismiss shows an error, try again once. If it keeps failing, see [Troubleshooting](/help/troubleshooting).

:::note Snoozing does not hide the alert
Snooze and Dismiss only quiet **this Cora Max**. Here, the alert stops popping up, sounding and speaking, and it leaves the list at the top of the screen until the snooze time ends (or, after Dismiss, until the reading is back in its normal range). Your phone still gets its notifications, and any other Cora Max still shows the alert. The alert also stays in **Notification history**, and your alert settings do not change.
:::

## The notification inbox

**Settings → Cora Max Settings → Notifications → Notification history** is the **account-wide** inbox: every briefing, alarm and account notice for your whole system, not just what this screen raised. It includes anything your phone missed.

## Editing thresholds

![Tank settings on Cora Max](img/max-tank-settings.webp "Each tank has its own journal, maintenance, alerts, livestock and briefing.")

Tap the tank name in the top bar and choose **Alerts**, or go to **Settings → [your tank] → Alert thresholds**. Either opens the same ranges as the phone. A change made here applies everywhere.

Individual thresholds can also be edited by opening a widget on the dashboard.

See [Alerts and thresholds](/help/mobile-alerts) for how ranges and rules work.

:::note Alerts are raised once, for the account
An alert is not raised separately by each device. Cora Max, your phone and any other screen show the same alert, and it clears everywhere at once when the reading returns to range.
:::
