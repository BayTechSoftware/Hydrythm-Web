---
title: Troubleshooting
description: Readings stopped, a device went offline, an alert won't clear, or something just looks wrong. Start here.
section: Help
reviewed: 2026-09-27
order: 1
---

Find the symptom that matches yours.

## A widget shows no value

Go through these in order:

1. **Look at the age on nearby widgets.** If they're all old too, it's the connection. The parameter itself is fine.
2. **Open the Devices tab.** If a device can't be reached, its row says so.
3. **Check which tank the device is on.** A device reporting to the wrong tank looks exactly like one that isn't reporting. Open the device and check its tank.
4. **Check that something measures it.** Nothing reports phosphate unless you have equipment that measures it or you log it by hand.

## A reading is stale

The age badge is right. Nothing new has come in.

- **Hand-logged parameters** go stale when nobody has entered a reading. Log one.
- **Equipment readings** go stale when the device stops reporting. Check its row in **Devices**.
- **Some equipment only reports now and then.** A titrator that measures hourly will usually show `1h`. That's normal.

## A device cannot be reached

It's usually the network. Ask yourself:

1. Is the equipment powered on and working in its own app?
2. Is it on the same network you added it on?
3. Has anything changed with your router (new hardware, new network name, guest network isolation)?

Equipment that connects over your local network has to be reachable on that network. Equipment that connects through a manufacturer account doesn't, but that account still has to be valid.

## A device says the sign-in was refused

The manufacturer rejected the saved sign-in. Almost always, that's because you changed your password with them. Open the device's row and sign in again.

## Pairing a Cora Max fails

If adding a Cora Max stops partway, Cora Mobile tells you which step failed and why, with **Cancel** and **Retry** underneath.

- *"Your phone could not reach the Cora Max on your Wi-Fi."* Put your phone and Cora Max on the same Wi-Fi network. On iPhone, also check that Cora has Local Network access. **Settings → Device access** takes you there (see [Settings](/help/mobile-settings)). Then tap **Retry**.
- *"The Cora Max did not accept this pairing session."* Retrying won't help here. Close the screen and start again from **Devices → Add Device**.

For any other message, tap **Retry**.

## Cora Max shows old data

Look at the status tag in the top bar. **Online** and **Cloud** are both fine. If you have more than one Cora, the one that isn't collecting the data shows **Cloud**, and its readings are just as current. **Stale** or **Offline** means Cora Max has lost its source and is showing the last data it got. That's the right behaviour, but the data isn't current.

- Check Wi-Fi under **Settings → Cora Max Settings → Wi-Fi**.
- Check that your network itself is working.
- If the tag says **Online** or **Cloud** and the data is still old, the problem is somewhere before Cora Max. Check the same tank on your phone.

## An alert is not clearing

An alert clears when the reading is back in range. If it won't clear, there are three likely reasons:

- **The reading really is out of range.** Look at the widget's history.
- **The threshold doesn't suit your tank.** See [Alerts and thresholds](/help/mobile-alerts).
- **The source is off.** A probe that needs calibrating will report a number that's really out of range. Fix the probe and leave the threshold alone.

## Two sources disagree

Nothing is broken. When your probe and your test kit disagree, that tells you something real about your system.

Usually the probe needs calibrating. Sometimes the test kit is old. Calibrate the probe, retest with fresh reagent, and compare the two under the same conditions.

An [ICP result](/help/mobile-icp-health) gives you a third number to compare, but it won't settle the question by itself. Labs differ from each other, and how a sample is handled and shipped changes the result. Two tests that agree tell you far more than one.

## I'm not getting notifications

1. In **Settings → Notifications**, check that the category is allowed to send notifications.
2. Check your phone's own notification permission for Cora.
3. Keep in mind that the daily briefing stays quiet on days when nothing changed.

## Establishing why something changed

**Settings → Activity** lists every outlet switch, feed, dose and plug change, and what asked for it. That can be Cora Mobile, a Cora screen, voice, the Assistant, an automation rule, a smart button or your account.

## My dashboard looks wrong after editing

Load a saved design. Open **My dashboards** and pick one.

If you haven't saved one, rebuild the layout and save it as a design. Next time, getting back to it takes one tap.

Your readings, history and journal entries are stored separately from the layout, so you haven't lost anything.

## "Red Sea readings have stopped updating"

Nothing on this tank's network is polling your Red Sea equipment right now, so the readings on screen aren't being refreshed.

1. Open **Settings → Primary Cora Max** and check that a Cora Max is set, or that **Any active (automatic)** is chosen.
2. Open the tank on a device that's on the same Wi-Fi as the Red Sea gear.
3. Check that the Red Sea equipment is powered on and online in its own app.

If that doesn't fix it, email [cora@coraiq.tech](mailto:cora@coraiq.tech) with the tank and device name.

## "Could not reach this pump: nothing was sent"

A command to your Jecod or Jebao pump never left Cora. Usually the pump is off or not on its network.

1. Check the pump is powered on.
2. Check it's on the same network you added it on.
3. Tap **Retry**.

Still stuck? Email [cora@coraiq.tech](mailto:cora@coraiq.tech) with the tank and device name.

## "Could not reach this pump over Bluetooth. Stand near it and try again."

Your phone is out of range of a Bluetooth-only Jecod device. Move closer to the pump and tap **Retry**.

If it still fails, email [cora@coraiq.tech](mailto:cora@coraiq.tech) with the tank and device name.

## "Could not reach that gyre. No feed was started."

A Maxspect gyre (a beta integration) didn't respond when Cora tried to start feed mode on it. Check the gyre is powered on and on its network, then tap **Retry**.

If it still fails, email [cora@coraiq.tech](mailto:cora@coraiq.tech) with the tank and device name.

## "Could not reach that gyre. Its program was not changed."

Cora couldn't get a new schedule through to a Maxspect gyre (a beta integration). Make sure your phone or Cora Max is on the gyre's network, then tap **Retry** on the schedule screen.

If it still fails, email [cora@coraiq.tech](mailto:cora@coraiq.tech) with the tank and device name.

## "Could not reach the Apex: nothing changed" / "nothing was dosed"

A Neptune Apex, Trident or DŌS head didn't respond to a command or a dose request.

1. Open the Apex's own app and check it's online.
2. Check the network connection on the device you're using.
3. Tap **Retry**.

Still stuck? Email [cora@coraiq.tech](mailto:cora@coraiq.tech) with the tank and device name.

## "This could not be sent: no device on this tank can send it"

None of the Cora devices on this tank has the Apex connection details it needs to send the command, or the one that does is offline. You can fix it one of two ways:

1. Add the Apex details in **Settings** on a device that's online, or
2. Make a different, working Cora Max the **Primary Cora Max** for this tank.

If neither works, email [cora@coraiq.tech](mailto:cora@coraiq.tech) with the tank and device name.

## A secondary Cora Max shows "Main Cora offline"

The primary Cora Max for this tank has gone offline. This screen is showing the last data it received, so it isn't live.

1. Check the primary Cora Max's power and Wi-Fi.
2. Wait for it to reconnect, or change the **Primary Cora Max** to a device that's online.

Still stuck? Email [cora@coraiq.tech](mailto:cora@coraiq.tech) with the tank and device name.

## "Device is offline. Showing last known state."

The device stopped reporting, and Cora is showing the last values it had. They aren't current.

1. Check the device's own network connection.
2. Don't treat the values as live until the row stops saying offline.

Still stuck? Email [cora@coraiq.tech](mailto:cora@coraiq.tech) with the tank and device name.

## Some ReefBeat settings are greyed out or missing

That's normal. The device's own settings only open when your phone is on the same network as the device. Away from that network you only see readings.

1. Join the tank's Wi-Fi to change those settings.
2. Readings and history keep working when you're away from the tank.

If something else seems wrong, email [cora@coraiq.tech](mailto:cora@coraiq.tech).

## "Could not reach Cora. Check your Wi-Fi or mobile data, then try again."

Your phone can't reach Cora Cloud to sign in. This is about your phone's connection. Your tank equipment isn't involved.

1. Check that your phone has working Wi-Fi or mobile data.
2. Try a different network if you have one.
3. Tap **Retry**.

Still stuck? Email [cora@coraiq.tech](mailto:cora@coraiq.tech).

## Everything is suddenly in the wrong language

Someone changed the account language on one of your devices. It's one setting for the whole account.

1. Open **Settings → Language** in Cora Mobile or on Cora Max.
2. If it was changed by mistake, set it back. The change applies everywhere.

Still stuck? Email [cora@coraiq.tech](mailto:cora@coraiq.tech).

## An old alert or report is still in a different language after switching

That's expected. Cora doesn't retranslate anything it already wrote. Only new alerts, reports and briefings use the new language, so there's nothing to fix. New content will come in the current language.

If something else seems wrong, email [cora@coraiq.tech](mailto:cora@coraiq.tech).

## An alert won't stop notifying even after I've acknowledged it

**Snooze** and **Dismiss** on Cora Max only quiet that one Cora Max. Your phone keeps getting notifications for as long as the reading is out of range.

1. To hear about it less often on your phone, open the alert rule in Cora Mobile and set a longer **Cooldown between alerts** (up to 1 week).
2. If the threshold doesn't suit your tank, change the threshold itself.

More in [Alerts and thresholds](/help/mobile-alerts), or email [cora@coraiq.tech](mailto:cora@coraiq.tech).

## A dose stopped partway through and a "restore" alert appeared

The DŌS head lost contact during the dose. Cora is telling you so it doesn't have to assume the full dose went in.

1. Open the alert and check how much was dosed before it stopped.
2. Use the amount that went in to decide whether to resume or adjust the dose.

Still stuck? Email [cora@coraiq.tech](mailto:cora@coraiq.tech) with the tank and device name.

## A scene made on the phone doesn't show up as editable on Cora Max

Only newer Cora Max versions can edit scenes on the screen itself. Older firmware still runs scenes you made on your phone, but can't edit them.

1. Update Cora Max, or
2. Keep editing that scene on your phone. It runs on Cora Max either way.

See [Updates and recovery](/help/max-updates), or email [cora@coraiq.tech](mailto:cora@coraiq.tech).

## Cora Assistant answers about the wrong tank

You didn't pick a tank before asking, or the wrong one is selected. Pick the tank you mean, then ask again.

More in [The Assistant](/help/mobile-assistant), or email [cora@coraiq.tech](mailto:cora@coraiq.tech).

## Cora Assistant refuses to answer, or shows a consent screen again

"Allow Cora Assistant to use saved tank data" is turned off, so it has nothing to answer from. Tap **Agree & Continue** on the consent screen to turn it back on.

More in [The Assistant](/help/mobile-assistant), or email [cora@coraiq.tech](mailto:cora@coraiq.tech).

## A lab or emailed ICP result never showed up

A result only attaches once it has a tank, and sometimes Cora also needs to recognise the sender.

1. Check the hint Cora shows the first time you send it a result.
2. When Cora asks, confirm which tank the result belongs to.
3. If you've sent a result before, send this one from the same email address.

More in [ICP and health reports](/help/mobile-icp-health), or email [cora@coraiq.tech](mailto:cora@coraiq.tech).

## An emailed ICP notification names no lab

This was a known issue. The "choose tank" notification left out the lab's name, and current builds have fixed it. The result itself was never affected, only the notification text. Update Cora Mobile to the latest version.

If you still see it, email [cora@coraiq.tech](mailto:cora@coraiq.tech).

## A widget shows the wrong units

That's the tank's display units setting. Your data is fine, and values are stored the same way however they're shown.

1. Open **Settings** for that tank and check its display units.
2. Change them there. Every phone and Cora Max showing that tank updates to match.

Still stuck? Email [cora@coraiq.tech](mailto:cora@coraiq.tech).

## A gauge or threshold looks different after changing display units

That's expected. Gauges, tiles and history redraw in the unit you picked. The values underneath haven't changed, so there's nothing to fix.

If something else seems wrong, email [cora@coraiq.tech](mailto:cora@coraiq.tech).

## Cora Max won't reconnect right away after a Wi-Fi outage

After it loses its connection, Cora Max waits a bit longer before each retry so it doesn't flood your network. The wait grows to about a minute.

1. Give it about a minute after your network comes back.
2. If it still hasn't reconnected, check Wi-Fi under **Settings → Cora Max Settings → Wi-Fi**.

See [The Cora Max home screen](/help/max-tour), or email [cora@coraiq.tech](mailto:cora@coraiq.tech).

## Renaming a Cora Max on the phone doesn't change what the tablet shows

The name you set on your phone is the account's label for that device. The name Cora Max shows on its own pairing screen can be a different one.

1. Check which name you're looking at, the one in your phone's device list or the one on Cora Max's pairing screen.
2. If it's the account label you want to change, rename it from your phone's device list.

Still stuck? Email [cora@coraiq.tech](mailto:cora@coraiq.tech) with the device name.

## I can't find where to turn off the wake word on Cora Max

Wake-word controls are under **Sound & Voice**. They aren't part of the Cora Assistant settings.

1. Go to **Settings → Cora Max Settings → Sound & Voice → Wake-word listening**.
2. Turn it off. You can still tap the Cora icon to start talking.

See [Settings on Cora Max](/help/max-settings), or email [cora@coraiq.tech](mailto:cora@coraiq.tech).

## Child lock won't let anyone into Settings

That's what child lock does. After a set time with no touch, it stops anyone switching equipment from this screen, by touch or by voice. Readings keep updating, and you can still ask Cora questions. To unlock:

1. Press **Volume Up** or **Volume Down** three times within two seconds, or
2. Hold five fingers in the top-right corner of the screen for ten seconds.

More in [Voice on Cora Max](/help/max-voice), or email [cora@coraiq.tech](mailto:cora@coraiq.tech).

## Still stuck

Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**. Tell us which tank, which screen, and what you expected to see. It helps us give you a useful answer faster.
