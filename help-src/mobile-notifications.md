---
title: Notifications
description: Choose which notifications reach your phone, keep nights quiet, read what you missed under the bell, and fix notifications that don't arrive.
section: Cora Mobile
reviewed: 2026-10-13
order: 24
group: Alerts and automation
---

**Settings → Notifications** decides which of Cora's notifications reach your phone. This page also covers the bell, quiet nights, and what to check when nothing arrives.

![Settings, Notifications in Cora Mobile](img/mobile-notifications.webp "Each category has its own switch.")

## What can push {#categories}

The card at the top says whether this phone allows notifications from Cora at all (**Notifications enabled** or **Notifications disabled**). Under **App Notifications**, each category has its own switch:

| Category | Covers |
|---|---|
| **Parameter Alerts** | Water chemistry outside a range you set, and the *recovered* notification when it comes back |
| **Maintenance Reminders** | Tasks you scheduled, like water changes, and a one-time reminder to log your first test when a new tank still has no readings after three days |
| **Equipment Faults** | A device reporting a problem, for example a Trident that has stopped testing. Also a device that [stopped reporting](/help/mobile-alerts#stopped-reporting), a missed dose and an automation that failed |
| **Supplies Running Low** | Reagent, top-off water, dosing containers, and a full waste bottle |
| **ICP Report Ready** | Your ICP results are analysed and ready to read |

When you turn a category off, it stops pushing. Cora still records the event, and you'll still find it under the bell.

These switches belong to your account, so they apply to every phone you're signed in on.

:::warning "Parameter Alerts" is only about chemistry
That switch doesn't cover everything the tank might tell you. A Trident that has stopped testing is an **Equipment Fault**. Reagent running out is **Supplies Running Low**. Each has its own switch. If you've relied on Parameter Alerts for a long time, check the other two.
:::

The waste bottle counts as a supply even though it fills up instead of running down. It's something to empty before it stops the tests.

### Notifications without a switch {#other-notifications}

A few notifications aren't in that list:

- Reef Buddy's daily briefing. You choose when it arrives with **Briefing time**, the row just below Notifications in Settings. On the free plan there's no briefing notification. More in [Reef Buddy](/help/mobile-reef-buddy).
- Plan notifications: trial reminders 7 days and 1 day before the trial ends and when it ends, and a warning when you've used 80% and 100% of your monthly Cora Assistant allowance. See [Plans](/help/mobile-plans).
- Leak alerts from a leak sensor. They always push and can't be switched off, so turning off **Parameter Alerts** never silences them.

## Keeping nights quiet {#quiet-at-night}

Cora Mobile has no quiet hours setting. A parameter alert is sent as soon as the reading crosses your range, day or night. These are the ways to keep a night quiet:

- Use your phone's Focus or Do Not Disturb. Cora's notifications wait silently and you'll find them under the bell in the morning. If you want real emergencies to wake you, allow Cora through.
- Turn off the categories you don't need at night. Supplies and maintenance can usually wait. A switch stays off all day, though.
- Lengthen a rule's cooldown. If one alert keeps waking you about a problem you already know about, raise its **Cooldown between alerts**. See [Cooldowns](/help/mobile-alerts#cooldowns).
- Pick when reminders arrive. Each maintenance task has a **Remind me at** time, and Reef Buddy uses your **Briefing time** (8:00 unless you change it).

On Cora Max, **Night dimming** dims the screen overnight, and in the Sound & Voice section you can switch off **Alert sound** and **Spoken alerts**. Those two stay off until you turn them back on. See [Cora Max settings](/help/max-settings).

:::warning Don't silence what you'd want to hear
A heater sticking on at 3 am is exactly the alert you want. If you silence your phone at night, allow Cora through Focus or Do Not Disturb so an alert like that can still reach you.
:::

## The bell {#the-bell}

The bell sits at the top right of the main tabs. It holds everything Cora has raised, newest first, whether or not it was pushed. The number on it is how many you haven't read.

Inside, notifications are grouped by **Today**, **Yesterday** and earlier dates. Use the tank chips at the top (**All**, or one tank) to narrow the list. **Mark all read** clears the count. **Clear All** empties the inbox after you confirm, and it can't be undone.

Check it after a day away from your phone, or when a category you switched off has raised something.

## If nothing is arriving {#if-nothing-is-arriving}

Go through these in order.

1. Look at the card at the top of **Settings → Notifications**. If it says **Notifications disabled**, this phone blocks Cora. Tap **Open Settings** and allow notifications. While they're blocked, nothing reaches this phone, whatever the switches below say.
2. Check the category's switch under **App Notifications**.
3. Check your phone's Focus or Do Not Disturb.
4. Ask whether there was anything to send. Reef Buddy stays quiet on days when nothing changed, and a free account gets no briefing. An alert that's already up waits for its [cooldown](/help/mobile-alerts#cooldowns) before it notifies you again.

Still nothing? See [Troubleshooting](/help/troubleshooting).

## If too much is arriving {#if-too-much-is-arriving}

Look at your thresholds before you turn notifications off. Too many alerts usually means a range is tighter than the tank really runs, or a source needs calibrating. More in [Alerts and thresholds](/help/mobile-alerts).

Turning a category off silences all of it. If it's one alert pushing too often, change **Cooldown between alerts** on that rule instead. It goes from 15 minutes up to 1 week. The cooldown options, and what Snooze does on Cora Max, are in [Cooldowns](/help/mobile-alerts#cooldowns).
