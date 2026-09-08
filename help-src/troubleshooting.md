---
title: Troubleshooting
description: Readings stopped, a device went offline, alerts won't clear, or something looks wrong — start here.
section: Help
order: 1
---

Start with the symptom.

## A widget shows no value

Work down this list:

1. **Check the age on nearby widgets.** If everything is stale, the problem is the connection, not the parameter.
2. **Open the Devices tab.** A device that cannot be reached says so on its row.
3. **Check the tank assignment.** A device reporting into the wrong tank looks exactly like a device that is not reporting. Open the device and confirm its tank.
4. **Check the source exists.** Nothing reports phosphate unless you have equipment that measures it or you log it by hand.

## A reading is stale

The age badge is telling you the truth: nothing new has arrived.

- **Hand-logged parameters** go stale when no reading has been entered. Log one.
- **Equipment readings** going stale means the device stopped reporting — check its row in **Devices**.
- **Some equipment is meant to be slow.** A titrator that measures hourly will normally read `1h`. That is not a fault.

## A device says it can't be reached

Usually the network.

1. Is the equipment powered and working in its own app?
2. Is it on the same network it was added on?
3. Has your router changed — new hardware, new network name, guest network isolation?

Equipment that connects over your local network needs to be reachable on that network. Equipment that connects through a manufacturer account does not, but needs that account to still be valid.

## A device says the sign-in was refused

The manufacturer rejected the stored sign-in. Almost always because you changed your password with them.

Open the device row and sign in again.

## Cora Max shows old data

Check the top bar. If it does not say **Online**, the screen has lost its connection and is showing the last data it had — which is the correct behaviour, but not current.

- Check Wi-Fi under **Settings → Cora Max**
- Check the network itself is up
- If the screen is Online but data is still old, the problem is upstream: check the same tank on your phone

## An alert won't clear

An alert clears when the reading returns to range. If it will not clear:

- **The reading really is out of range.** Look at the widget's history.
- **The threshold is wrong for your tank.** See [Alerts and thresholds](/help/mobile-alerts).
- **The source is wrong.** A probe that needs calibrating reports a number that is genuinely out of range. Fix the probe rather than the threshold.

## Two sources disagree

This is Cora working, not Cora failing. When your probe and your test kit disagree, that is a real fact about your system.

Usually the probe needs calibrating. Sometimes the test kit is old. An ICP result is the tiebreaker — see [ICP and health reports](/help/mobile-icp-health).

## I'm not getting notifications

1. **Settings → Notifications** — check the alert type is allowed to push
2. Check quiet hours
3. Check your phone's own notification permissions for Cora
4. Remember the daily briefing is deliberately quiet on days when nothing changed

## Establishing why something changed

**Settings → Activity** lists every outlet switch, feed, dose and plug change, with what caused it — you, a rule, a schedule, or the Assistant.

## My dashboard looks wrong after editing

**Presets → Reset to default** rebuilds it from your tank profile. Readings, history and journal entries are stored separately from layout, so nothing is lost.

## Still stuck

Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**. Tell us which tank, which screen, and what you expected to see — it gets you a useful answer faster.
