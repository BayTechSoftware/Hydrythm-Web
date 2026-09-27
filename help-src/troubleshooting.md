---
title: Troubleshooting
description: Readings stopped, a device went offline, alerts are not clearing, or something looks wrong. Start here.
section: Help
reviewed: 2026-09-27
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
- **Equipment readings** going stale means the device stopped reporting; check its row in **Devices**.
- **Some equipment is meant to be slow.** A titrator that measures hourly will normally read `1h`. That is not a fault.

## A device cannot be reached

Usually the network.

1. Is the equipment powered and working in its own app?
2. Is it on the same network it was added on?
3. Has your router changed (new hardware, new network name, guest network isolation)?

Equipment that connects over your local network needs to be reachable on that network. Equipment that connects through a manufacturer account does not, but needs that account to still be valid.

## A device says the sign-in was refused

The manufacturer rejected the stored sign-in. Almost always because you changed your password with them.

Open the device row and sign in again.

## Pairing a Cora Max fails

If adding a Cora Max stops partway, Cora Mobile says which step failed and why, with **Cancel** and **Retry** below.

- *"Your phone could not reach the Cora Max on your Wi-Fi."* Put your phone and the Cora Max on the same Wi-Fi network. On iPhone, also check that Cora has Local Network access: **Settings → Device access** takes you there (see [Settings](/help/mobile-settings)). Then tap **Retry**.
- *"The Cora Max did not accept this pairing session."* Retrying will not help. Close the screen and start again from **Devices → Add Device**.

For any other message, tap **Retry**.

## Cora Max shows old data

Check the status pill in the top bar. **Online** and **Cloud** are both healthy: with more than one Cora, the screen that is not doing the collecting shows **Cloud**, and its readings are just as current. **Stale** or **Offline** means the screen has lost its source and is showing the last data it received (correct behaviour, but not current).

- Check Wi-Fi under **Settings → Cora Max → Network**
- Check the network itself is up
- If the pill reads **Online** or **Cloud** and the data is still old, the problem is upstream: check the same tank on your phone

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

1. **Settings → Notifications**: check that category is allowed to push
2. Check your phone's own notification permissions for Cora
3. Remember the daily briefing is deliberately quiet on days when nothing changed

## Establishing why something changed

**Settings → Activity** lists every outlet switch, feed, dose and plug change, with what asked for it: Cora Mobile, a Cora screen, voice, the Assistant, an automation rule, a smart button or your account.

## My dashboard looks wrong after editing

Load a saved design: **My dashboards**, then pick one.

If you have not saved one, rebuild the layout and then save it as a design. From that point on, returning to it is a single tap.

Either way, readings, history and journal entries are stored separately from layout, so nothing behind the dashboard is lost.

## "Red Sea readings have stopped updating"

**What it means:** No device on this tank's network is currently polling your Red Sea equipment, so the readings on screen have not been refreshed.

**What to do:**
1. Open **Settings → Primary Cora Max** and check a Cora Max is set (or **Any active (automatic)** is chosen).
2. Open the tank on a device that is on the same Wi-Fi as the Red Sea gear.
3. Confirm the Red Sea equipment is powered and online in its own app.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)** with the tank and device name.

## "Could not reach this pump: nothing was sent"

**What it means:** A command to a Jecod or Jebao pump never left the app, usually because the pump is off or off its network.

**What to do:**
1. Check the pump is powered on.
2. Check it is on the same network it was added on.
3. Tap **Retry**.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)** with the tank and device name.

## "Could not reach this pump over Bluetooth. Stand near it and try again."

**What it means:** A Bluetooth-only Jecod device is out of range of your phone.

**What to do:**
1. Move closer to the pump.
2. Tap **Retry**.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)** with the tank and device name.

## "Could not reach that gyre. No feed was started."

**What it means:** A Maxspect gyre (beta integration) did not respond when Cora tried to start feed mode on it.

**What to do:**
1. Check the gyre is powered on and on its network.
2. Tap **Retry**.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)** with the tank and device name.

## "Could not reach that gyre. Its program was not changed."

**What it means:** A schedule push to a Maxspect gyre (beta integration) failed to reach it.

**What to do:**
1. Check your phone or Cora Max is on the gyre's network.
2. Tap **Retry** from the schedule screen.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)** with the tank and device name.

## "Could not reach the Apex: nothing changed" / "nothing was dosed"

**What it means:** A Neptune Apex, Trident, or DŌS head did not respond to a command or dose request.

**What to do:**
1. Open the Apex's own app and confirm it is online.
2. Check network connectivity on the device you are using.
3. Tap **Retry**.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)** with the tank and device name.

## "This could not be sent: no device on this tank can send it"

**What it means:** No Cora device on this tank has the Apex connection details needed to carry out the command, or the one that does is offline.

**What to do:**
1. Add the Apex details in **Settings** on a device that is currently online, or
2. Set a different, working Cora Max as the **Primary Cora Max** for this tank.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)** with the tank and device name.

## A secondary Cora Max shows "Main Cora offline"

**What it means:** The primary tablet for this tank has gone offline, so this secondary screen is showing the last data it received rather than live data.

**What to do:**
1. Check the primary tablet's power and Wi-Fi.
2. Wait for it to reconnect, or change the **Primary Cora Max** to a device that is currently online.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)** with the tank and device name.

## "Device is offline. Showing last known state."

**What it means:** Normal offline handling: the device stopped reporting, and Cora is showing the last values it had rather than pretending they are current.

**What to do:**
1. Check the device's own network connection.
2. Treat the shown values as not live until the row no longer says offline.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)** with the tank and device name.

## Some ReefBeat settings are greyed out or missing

**What it means:** This is by design, not a fault. Device-native settings (as opposed to readings) only open when your phone is on the same network as the device itself; away from that network, only readings show.

**What to do:**
1. Visit the tank's own Wi-Fi to change those settings.
2. Readings and history still work normally away from the tank.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## "Could not reach Cora. Check your Wi-Fi or mobile data, then try again."

**What it means:** Your phone has no usable connection to Cora Cloud at sign-in. This is about your phone's own connectivity, not your tank equipment.

**What to do:**
1. Check your phone has a working Wi-Fi or mobile data connection.
2. Try a different network if one is available.
3. **Retry**.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Everything is suddenly in the wrong language

**What it means:** The account language was changed from any device. Language is one setting for the whole account, not per device.

**What to do:**
1. Open **Settings → Language** on either app.
2. Set it back if it was changed by mistake; the change applies everywhere at once.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## An old alert or report is still in a different language after switching

**What it means:** This is expected, not a bug. Cora does not retranslate content that was already generated; only new alerts, reports and briefings follow the new language.

**What to do:**
1. Nothing to fix. Wait for new content, which will use the current language.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## An alert won't stop notifying even after I've acknowledged it

**What it means:** Confusion between **Dismiss** (closes the alert for good) and **Snooze** (mutes it temporarily, for up to a week).

**What to do:**
1. If you understand and accept the condition, use **Dismiss**.
2. If you only want quiet for a while, use **Snooze** and pick a length.

**Still not working?** See [Alerts and thresholds](/help/mobile-alerts), or email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## A dose stopped partway through and a "restore" alert appeared

**What it means:** The DŌS head lost contact mid-dose, so Cora is telling you deliberately rather than assuming the full dose went in.

**What to do:**
1. Open the alert and check how much was actually dosed before it stopped.
2. Resume or adjust the dose based on that amount, not the amount originally scheduled.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)** with the tank and device name.

## A scene made on the phone doesn't show up as editable on Cora Max

**What it means:** Editing scenes directly on the tablet is a newer Cora Max capability. Older firmware can still run phone-made scenes, just not edit them there.

**What to do:**
1. Update Cora Max, or
2. Keep editing that scene from the phone; it will still run on the tablet either way.

**Still not working?** See [Updates and recovery](/help/max-updates), or email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant answers about the wrong tank

**What it means:** No tank was picked before asking, or the wrong tank is currently active.

**What to do:**
1. Pick the tank you mean first.
2. Ask again.

**Still not working?** See [The Assistant](/help/mobile-assistant), or email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant refuses to answer, or shows a consent screen again

**What it means:** "Allow Cora Assistant to use saved tank data" was turned off, so it has nothing to answer from.

**What to do:**
1. Tap **Agree & Continue** on the consent screen to turn it back on.

**Still not working?** See [The Assistant](/help/mobile-assistant), or email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## A lab or emailed ICP result never showed up

**What it means:** Getting a result into Cora needs a tank chosen for it, and sometimes a recognized sender, before it attaches anywhere.

**What to do:**
1. Check the intake hint shown the first time you send a result to Cora.
2. Confirm which tank the result should attach to when prompted.
3. Make sure the email was sent from the address you used to send it before, if you have sent one previously.

**Still not working?** See [ICP and health reports](/help/mobile-icp-health), or email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## An emailed ICP notification names no lab

**What it means:** A known issue with the "choose tank" push notification missing the lab's name. It has been fixed in current builds.

**What to do:**
1. Make sure Cora Mobile is updated to the latest version.
2. The result itself is unaffected; only the notification text was missing a name.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## A widget shows the wrong units

**What it means:** This is the tank's display units setting, not a data problem. Values are stored the same way regardless of how they are displayed.

**What to do:**
1. Open **Settings** for that tank and check its display units.
2. Change them there; every phone and Cora Max showing that tank updates to match.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## A gauge or threshold looks different after changing display units

**What it means:** Expected. Gauges, tiles and history redraw in the unit you chose; the underlying values have not changed.

**What to do:**
1. Nothing to fix; this is cosmetic only.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Max won't reconnect right away after a Wi-Fi outage

**What it means:** After losing its connection, Cora Max waits a little longer before each retry rather than hammering the network, backing off to roughly a minute before it tries again.

**What to do:**
1. Wait about a minute after your network comes back.
2. If it still has not reconnected after that, check Wi-Fi under **Settings → Network**.

**Still not working?** See [The Cora Max home screen](/help/max-tour), or email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Renaming a Cora Max on the phone doesn't change what the tablet shows

**What it means:** The name you set from the phone is an account-level label for that device. The name shown on the tablet itself during pairing can be a different thing.

**What to do:**
1. Check which "name" you are looking at: the one in your device list on the phone, or the one on the tablet's own pairing screen.
2. Rename from the phone's device list if it's the account label you want to change.

**Still not working?** Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)** with the device name.

## I can't find where to turn off the wake word on Cora Max

**What it means:** The wake-word toggle lives under **Audio**, not under the Cora Assistant settings group, which surprises most people.

**What to do:**
1. Go to **Settings → Audio → Wake-word listening**.
2. Turn it off; you can still tap the Cora icon to start a voice session.

**Still not working?** See [Settings on Cora Max](/help/max-settings), or email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Child lock won't let anyone into Settings

**What it means:** This is working as intended. Child lock locks the touchscreen and voice controls after a set time with no touch; readings keep updating underneath it.

**What to do:**
1. Press **Volume Up** or **Volume Down** three times within two seconds, or
2. Hold five fingers in the top-right corner of the screen for ten seconds.

**Still not working?** See [Voice on Cora Max](/help/max-voice), or email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Still stuck

Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**. Tell us which tank, which screen, and what you expected to see; it gets you a useful answer faster.
