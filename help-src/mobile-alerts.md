---
title: Alerts and thresholds
description: Set the range for each parameter, choose what you're told about, and see why an alert fired.
section: Cora Mobile
reviewed: 2026-09-27
order: 15
group: Alerts and automation
---

You get an alert when a reading leaves the range you set for it. You set the ranges, and you decide which alerts reach your phone.

Open the **Alert Center** from the shortcut row at the bottom of the dashboard.

![The Alert Center](img/mobile-alerts.webp "Active alerts, each with its severity, what triggered it, and when.")

## The Alert Center

It has two tabs:

- **Active** lists the alerts that are up right now, with a count badge.
- **Rules** holds the thresholds and rate-of-change rules that raise them.

Each active alert shows the parameter and tank, the reading that set it off, a short explanation, a severity chip, the kind of rule that fired (**Threshold** or **Rate of Change**) and when it fired.

Each one has two buttons:

- **View rule** opens the rule behind it, so you can adjust the range.
- **Explain this alert** asks the Assistant to read it against your tank's history.

## Setting a range

Parameters Cora can grade have a target range. The defaults come from your tank type and age when you set the tank up, and they're usually a sensible start. If a parameter has no usable range, Cora doesn't grade it. It stays neutral grey instead of Cora guessing.

To change a range, long-press its widget on the dashboard. That opens the parameter's thresholds. A normal tap opens the parameter view instead, so the long-press is the one to remember.

If the parameter has no rule yet, the fields start on Cora's default and a note underneath says so. Change any value to set your own.

To see all your ranges together, tap **Alerts** in the row of buttons under the dashboard.

You can set:

- A range, with a low and a high, for things like alkalinity or temperature
- A ceiling, with only a high, for things where low is fine, like nitrate or phosphate
- A floor, with only a low

:::tip Set the range your tank really runs at
The defaults are only a starting point. A low-nutrient tank running at 6 dKH isn't "wrong" because a chart says 8–9. Set the range you run, and Cora will tell you when *you* drift.
:::

## What triggers an alert

An alert fires when a reading crosses a threshold. Cora checks each reading as it comes in, so one reading outside your range is enough.

Once an alert is up, it won't keep notifying you about the same thing. There's a cooldown before it can fire again. It clears on its own as soon as a reading is back inside the range, and you don't need to acknowledge it.

You can also set a rate-of-change rule. It watches how fast a parameter moves instead of where it sits. Use it when the speed of a change matters more than the number.

## Where alerts appear

- The bell, top right on every screen, holds your history. The number shows how many you haven't read.
- Push notifications reach your phone if you allow them.
- The widget on the dashboard turns amber or red.
- Cora Max shows the same alerts on the big screen.

## When equipment needs attention

Some alerts are about equipment, not a reading. When a device such as a Trident or a Jecod pump reports a fault, Cora sends a notification naming the tank and the device, for example *"Display tank: Return pump needs attention"*. It also says what's wrong, such as a jammed rotor. When the fault clears, you get a second one: *"Display tank: Return pump is OK again"*. Both fall under **Equipment Faults** in **Settings → Notifications**.

A Maxspect gyre (beta) can raise the same alert. This happens when a Cora Max on its network finds both heads set to 0%, or gets no answer from the gyre twice in a row. Treat it as a warning and don't rely on it as a safeguard. The Cora Max only checks from time to time, and only while it's running and can reach the gyre.

## "Red Sea readings have stopped updating"

You may see this banner on a tank's parameter page:

> Red Sea readings have stopped updating. No device is currently reading this tank's Red Sea devices: check Primary Cora Max in Settings, or open this tank on a device on the same Wi-Fi.

No phone or Cora Max is polling that tank's ReefBeat equipment right now. The readings you see are old, but not necessarily wrong. Tap the banner to open **Primary Cora Max**, then pick a device that's on or choose **Any active (automatic)**. [More than one Cora device](/help/mobile-multi-device) explains how this works. If the banner doesn't go away, try [Troubleshooting](/help/troubleshooting).

## Choosing what reaches you

In **Settings → Notifications** you choose which notification categories can send you a push.

Reef Buddy has no switch of its own. It sends a briefing when there's something worth acting on and stays quiet when there isn't.

:::note Cora stays quiet unless something changed
The daily briefing is one push per tank per day. On a day when nothing needs you, it usually stays silent instead of telling you all is well. If Cora is pushing, something changed.
:::

## Cooldowns: how often the same alert may notify you

Each rule has its own **Cooldown between alerts**. You set it when you add or edit the rule in the **Rules** tab of the Alert Center. The cooldown doesn't hide the alert. It only limits how often Cora pushes about it. The reading is still graded, and the alert stays on the widget and in the bell the whole time.

You can pick 15 min, 30 min, 1 h, 2 h, 4 h, 8 h, 1 day, 3 days or 1 week.

A short cooldown suits a fast-moving reading like temperature. A long one, up to a week, suits something that stays wrong for days while you wait for a part, such as a Trident out of reagent or an empty dosing container. Without it, Cora would push about the same known problem several times a day.

:::note Snooze is on Cora Max
Cora Mobile has no Snooze button on an active alert. Snooze is on the Cora Max screen at the tank, and it mutes the alert for the cooldown you picked here. On your phone, you change how often you hear about something with this per-rule cooldown.
:::

## Clearing an alert

An alert clears when the reading comes back into range. There's nothing to dismiss. It tells you about the tank. It isn't a task.

:::note Short spikes raise alerts too
One out-of-range reading is enough to raise an alert, so a probe that spikes will set one off. If a source is unreliable, recalibrate it or point the widget at a different source. Don't widen the threshold.
:::

Sometimes the reading is wrong and the tank is fine, for example when a probe needs calibrating. Fix the source in that case. If you widen a threshold to silence a bad probe, you'll miss the next real problem too.

## Disabling alerts for a parameter

Open the rule in the **Rules** tab of the Alert Center and turn off its enable switch. Cora keeps the rule and its range, so you can switch it back on without setting it up again.

:::warning Turn a parameter off without deleting its range
Removing a threshold doesn't always stop Cora assessing that reading. Default reference bands still colour the value and can still feed the briefing. Use the rule's enable switch.
:::
