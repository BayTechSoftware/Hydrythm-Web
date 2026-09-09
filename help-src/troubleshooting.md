---
title: Troubleshooting
description: Readings stopped, a device went offline, alerts are not clearing, or something looks wrong — start here.
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

## A device cannot be reached

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

- Check Wi-Fi under **Settings → Cora Max → Network**
- Check the network itself is up
- If the screen is Online but data is still old, the problem is upstream: check the same tank on your phone

## An alert is not clearing

An alert clears when the reading returns to range. If it will not clear:

- **The reading is genuinely out of range.** Look at the widget's history.
- **The threshold is wrong for your tank.** See [Alerts and thresholds](/help/mobile-alerts).
- **The source is wrong.** A probe that needs calibrating reports a number that is genuinely out of range. Fix the probe rather than the threshold.

## Two sources disagree

This is Cora working, not Cora failing. When your probe and your test kit disagree, that is a real fact about your system.

An ICP result is a useful third opinion here, but it does not settle the argument: laboratories differ from one another, and a sample's handling and transit move the result. Two tests agreeing is worth far more than one.

Usually the probe needs calibrating; sometimes the test kit is old. Calibrate the probe, run the test again with fresh reagent, and compare the two under the same conditions. An [ICP result](/help/mobile-icp-health) adds a third data point to that comparison.

## I'm not getting notifications

1. **Settings → Notifications** — check that category is allowed to push
2. Check your phone's own notification permissions for Cora
3. Remember the daily briefing is deliberately quiet on days when nothing changed

## Establishing why something changed

**Settings → Activity** lists every outlet switch, feed, dose and plug change, with what asked for it — this app, a Cora screen, voice, the Assistant, an automation rule, a smart button or your account.

## My dashboard looks wrong after editing

Load a saved design: **My dashboards**, then pick one.

If you have not saved one, rebuild the layout and then save it as a design. From that point on, returning to it is a single tap.

Either way, readings, history and journal entries are stored separately from layout, so nothing behind the dashboard is lost.

## Still stuck

Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**. Tell us which tank, which screen, and what you expected to see — it gets you a useful answer faster.
