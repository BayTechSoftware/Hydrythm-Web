---
title: Alerts and thresholds
description: Set the healthy range for each reading, choose how often an alert can notify you, and find out why a device "stopped reporting".
section: Cora Mobile
reviewed: 2026-10-13
order: 20
group: Alerts and automation
twin: max-alerts
---

You get an alert when a reading leaves the range you set for it. This page covers setting those ranges, what happens when an alert fires, and how long Cora waits before it says a device has stopped reporting.

To open the **Alert Center**, tap **Alerts** in the row of buttons under the dashboard. It's also in Settings → your tank → **Alert thresholds**.

![The Active tab of the Alert Center in Cora Mobile](img/mobile-alerts.webp "Active alerts, each with its severity, what triggered it and when, plus View rule and Explain this alert.")

## The Alert Center {#alert-center}

It has two tabs. **Active** lists the alerts that are up right now, with a count badge. **Rules** holds the rules that raise them.

Each active alert shows the parameter and tank, the reading that set it off, a short explanation, a severity chip, the kind of rule that fired (**Threshold** or **Rate of Change**) and when it fired. It has two buttons:

- **View rule** opens the rule behind it, so you can adjust the range. On a doser alert, such as a DŌS or ReefDose head running low or a missed dose, this button is **Open doser** instead. It opens that doser's page with its alerts.
- **Explain this alert** opens Cora Assistant with a question about the alert ready to send. Check it, change it if you like, then send it.

## The Rules tab {#rules}

![The Rules tab](img/mobile-alert-rules.webp "Rules grouped by parameter, each with its own switch.")

Rules are grouped by parameter. Each rule has its own switch on its row, so you can turn one off without opening it. A row also shows **Firing now** while its alert is up, or when it last fired (or **Never fired**).

A dosing head's rules are named after the head and what they watch, for example *Iodine · days left* or *Iodine · remaining*. A missed dose shows up as *Iodine · missed dose*. Each DŌS and each ReefDose has one row of its own here, and its head alerts aren't listed one by one. Tap the row to open that doser's page. See [Doser alerts](/help/mobile-device-control#doser-alerts).

At the bottom:

- **Add recommended rules** adds any of Cora's recommended rules that are missing. It skips a parameter that already has a rule. On a tank with no rules at all, this button reads **Add Default Rules**.
- **Add Custom Rule** sets up a rule of your own. Pick the parameter and the **Rule type**, **Threshold** or **Rate of Change**. The **Add Rule** button at the bottom right does the same.

### Editing a rule {#editing-a-rule}

Tap a rule's row to open it. You'll find:

- **Alert minimum** and **Alert maximum**, the range itself. Leave one empty for a ceiling or a floor.
- **Recommended**, which puts Cora's suggested range back.
- **Gauge Range (Cora display)**, with **Gauge min** and **Gauge max**. These only set the scale of the gauge on Cora Max. They never raise an alert.
- **Cooldown between alerts**, explained [below](#cooldowns).
- **Enabled**, and a delete button.

A device fault rule, such as a Trident out of reagent, has no range. You only choose its cooldown.

## Setting a range {#setting-a-range}

Parameters Cora can grade have a target range. The defaults come from your tank type and age when you set the tank up, and they're a sensible start. If a parameter has no usable range, Cora doesn't grade it, and its widget stays neutral grey.

The quickest way to change a range is to long-press the parameter's widget on the dashboard. That opens its thresholds. A normal tap opens the parameter view instead.

![The Edit Threshold sheet for pH in Cora Mobile](img/mobile-threshold-sheet.webp "Alert minimum and maximum, the gauge range for Cora Max, and the cooldown between alerts.")

If the parameter has no rule yet, the fields start on Cora's default and a note underneath says so. Change any value to set your own.

You can set:

- a range, with a low and a high, for things like alkalinity or temperature
- a ceiling, with only a high, for things where low is fine, like nitrate or phosphate
- a floor, with only a low

:::tip Set the range your tank really runs at
The defaults are only a starting point. A low-nutrient tank running at 6 dKH isn't "wrong" because a chart says 8–9. Set the range you run, and Cora tells you when *you* drift.
:::

## What triggers an alert {#what-triggers-an-alert}

An alert fires when a reading crosses a threshold. Cora checks each reading as it comes in, so one reading outside your range is enough.

A rate-of-change rule watches how fast a parameter moves instead of where it sits. Use it when the speed of a change matters more than the number.

Once an alert is up, it won't keep notifying you about the same thing. The rule's [cooldown](#cooldowns) decides when it may notify you again.

## Where alerts appear

- The bell, at the top right of the main tabs, keeps your history. The number shows how many you haven't read. More in [Notifications](/help/mobile-notifications).
- A push notification reaches your phone if that category is switched on.
- The widget on the dashboard turns amber or red.
- Cora Max shows the same alerts on its screen.

## When equipment needs attention {#equipment-faults}

Some alerts are about equipment, not a reading. When a device such as a Trident or a Jecod pump reports a fault, Cora sends a notification naming the tank and the device, for example *"Display tank: Return pump needs attention"*. It also says what's wrong, such as a jammed rotor. When the fault clears, you get a second one: *"Display tank: Return pump is OK again"*. Both fall under **Equipment Faults** in **Settings → Notifications**.

A Maxspect gyre (Beta) can raise the same alert. This happens when a Cora Max on its network finds both heads set to 0%, or gets no answer from the gyre twice in a row. Treat it as a warning, not a safeguard. The Cora Max only checks from time to time, and only while it's running and can reach the gyre.

## A device has stopped reporting {#stopped-reporting}

When a connected device goes quiet, Cora sends *"[Device]: stopped reporting"*. It doesn't mean the device is broken, only that Cora hasn't heard from it for a while. You get a second notification, *"[Device]: reporting again"*, when it comes back.

How long Cora waits depends on the device:

| Device | Cora waits |
|---|---|
| Neptune Apex | About 30 minutes without an update |
| Red Sea ReefBeat | About 30 minutes |
| AquaWiz | About 3 hours, because it reports less often |
| Jecod pumps | Three missed readings in a row, on the pump's reading interval (90 minutes at the default 30) |
| Maxspect (Beta) | Three missed readings in a row, like Jecod |
| EcoTech (Beta) | Three missed readings in a row, on the network's reading interval (90 minutes at the default 30). If you set a longer time under **Light stops answering**, Cora waits that long |
| Inkbird room air monitor (Beta) | Three missed readings in a row, on the monitor's own interval (15 minutes at the default 5) |
| Focustronic (Beta) | About 3 hours |
| GHL (Beta) | About 15 minutes. The notification says *"GHL controller not reachable"* |
| HYDROS (Beta) | About 30 minutes. The notification says *"HYDROS controller not reporting"* |

What to check depends on how Cora reads the device.

- Apex, ReefBeat, Jecod, Maxspect and GHL are read by a Cora Max over Wi-Fi. Check the device's power and Wi-Fi, and that the Cora Max that reads it is switched on and online.
- EcoTech and Inkbird are read by a Cora Max over Bluetooth. Check the power, that the device is within Bluetooth range of the Cora Max, and that the Cora Max is on.
- AquaWiz and Focustronic are read through your account with the maker. Check the account connection on the device's page in Cora Mobile.
- For HYDROS, check its power, Wi-Fi and device key.

GHL can also tell you *"GHL API is off"* or that the controller *"rejected the connection"*. If the Cora Max that reads a GHL controller goes quiet, you get *"Cora Max not reporting for"* that controller. The fixes are in [Troubleshooting](/help/troubleshooting).

These notifications fall under **Equipment Faults** in **Settings → Notifications**.

:::note Beta
Maxspect, EcoTech, Inkbird, Focustronic, GHL and HYDROS are in Beta and only open to Beta users. If you are not a Beta user you will not see them in **Add device**. To ask for Beta access, contact [support](/support.html). More in [Beta features](/help/mobile-beta).
:::

A Red Sea tank can also show a banner, *"Red Sea readings have stopped updating"*, when no phone or Cora Max is reading its ReefBeat equipment. Tap it to pick a **Primary Cora Max**. The full fix is in [Troubleshooting](/help/troubleshooting#red-sea-readings-have-stopped-updating).

## Choosing what reaches you {#choosing-what-reaches-you}

In **Settings → Notifications** you choose which categories can send you a push. See [Notifications](/help/mobile-notifications), which also covers [keeping nights quiet](/help/mobile-notifications#quiet-at-night).

Reef Buddy has no switch of its own. Its timing is the **Briefing time** row, just below Notifications in Settings. On the free plan there's no briefing notification.

:::note Cora stays quiet unless something changed
The daily briefing is one push per tank per day. On a day when nothing needs you, it usually stays silent instead of telling you all is well. If Cora is pushing, something changed.
:::

## Cooldowns: how often the same alert may notify you {#cooldowns}

Each rule has its own **Cooldown between alerts**. You set it when you add or edit the rule. A rule that never had one uses 1 h.

The cooldown doesn't hide the alert. It only limits how often Cora pushes about it. The reading is still graded, and the alert stays on the widget and under the bell the whole time.

You can pick 15 min, 30 min, 1 h, 2 h, 4 h, 8 h, 1 day, 3 days or 1 week.

A short cooldown suits a fast-moving reading like temperature. A long one, up to a week, suits something that stays wrong for days while you wait for a part, such as a Trident out of reagent or an empty dosing container.

:::note Snooze is on Cora Max
Cora Mobile has no Snooze button on an active alert. Snooze is on the Cora Max screen at the tank, and it mutes the alert for the cooldown you picked here. On your phone, the per-rule cooldown is how you change how often you hear about something.
:::

## Clearing an alert {#clearing-an-alert}

An alert clears on its own when the reading comes back into range. There's nothing to dismiss. You get one notification when it does, for example *"Display tank: Alkalinity recovered"*. If the problem comes back later, you get a new alert.

:::note Short spikes raise alerts too
One out-of-range reading is enough to raise an alert, so a probe that spikes will set one off. If a source is unreliable, recalibrate it or point the widget at a different source. Don't widen the threshold.
:::

Sometimes the reading is wrong and the tank is fine, for example when a probe needs calibrating. Fix the source in that case. If you widen a threshold to silence a bad probe, you'll miss the next real problem too.

## Turning an alert off {#turning-an-alert-off}

Turn off the switch on the rule's row in the **Rules** tab. Cora keeps the rule and its range, so you can switch it back on without setting it up again.

While a rule is off, Cora doesn't grade that reading. Its widget stays neutral grey and it never raises an alert.

:::warning Turn a parameter off without deleting its range
Deleting a rule doesn't always stop Cora assessing that reading. Default reference bands still colour the value and can still feed the briefing. Use the rule's switch.
:::
