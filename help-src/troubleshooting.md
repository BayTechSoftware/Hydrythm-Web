---
title: Troubleshooting
description: Fix a stale reading, a device that went offline, a command that didn't go through, a Cora Max that won't pair, or an alert that won't clear.
section: Help
reviewed: 2026-10-18
order: 1
---

Find the family your problem belongs to, then the message or symptom you see. Headings in quotes are the exact words Cora shows you.

- [Readings and widgets](#readings-and-widgets)
- [A device stopped reporting or can't be reached](#device-not-reporting)
- [A command didn't go through](#command-did-not-go-through)
- [Cora Max](#cora-max)
- [Alerts, notifications and the daily briefing](#alerts-and-notifications)
- [Cora Assistant and voice](#cora-assistant-and-voice)
- [Lab results and health reports](#lab-results-and-health-reports)
- [Language, units and signing in](#language-units-and-signing-in)


## Readings and widgets {#readings-and-widgets}

### A widget shows no value {#a-widget-shows-no-value}

Go through these in order.

1. Look at the age on nearby widgets. If they're all old too, it's the connection, not the parameter.
2. Open the **Devices** tab. If a device can't be reached, its row has a red dot or says so.
3. Check which tank the device is on. A device reporting to the wrong tank looks exactly like one that isn't reporting. Open the device and check its tank.
4. Check that something measures it. Nothing reports phosphate unless you have equipment that measures it or you log it by hand.

### A widget is grey {#a-widget-is-grey}

Grey means Cora isn't grading that reading. There are three usual reasons.

1. The alert for it is turned off. Turn it back on in the **Rules** tab of the Alert Center.
2. It has no range to judge it by. Long-press the widget and set a range.
3. The reading is too old. Check the age on the widget, then log a new reading or check the device.

What each colour means is in [Reading your dashboard](/help/mobile-dashboard#colours).

### A reading is stale {#a-reading-is-stale}

The age on the widget is right. Nothing new has come in.

- Hand-logged parameters go stale when nobody has logged a reading. Log one.
- Equipment readings go stale when the device stops reporting. Check its row in **Devices**.
- Some equipment only reports now and then. A titrator that measures hourly usually shows `1h`. That's normal.

### Two sources disagree {#two-sources-disagree}

Nothing is broken. When your probe and your test kit disagree, that tells you something real about your system.

Usually the probe needs calibrating. Sometimes the test kit is old. Calibrate the probe, retest with fresh reagent, and compare the two under the same conditions. If one reading was plainly wrong, you can exclude it. See [Looking into a parameter](/help/mobile-metric-detail).

An [ICP result](/help/mobile-icp-health) gives you a third number to compare, but it won't settle the question by itself. Labs differ from each other, and how a sample is handled and shipped changes the result.

### A widget shows the wrong units {#a-widget-shows-the-wrong-units}

That's the tank's display units. Your data is fine, and values are stored the same way however they're shown.

1. Open **Settings**, open that tank and choose **Units**.
2. Change them there. Every phone and Cora Max showing that tank updates to match.

### A gauge or threshold looks different after changing units {#a-gauge-or-threshold-looks-different-after-changing-display-}

That's expected. Gauges, tiles and history redraw in the unit you picked. The values underneath haven't changed.

### My dashboard looks wrong after editing {#my-dashboard-looks-wrong-after-editing}

Your readings, history and journal are stored apart from the layout, so you haven't lost anything.

- **On your phone**, the editor has no undo or saved designs. Open **Edit dashboard** and put the widgets back. More in [Editing your dashboard](/help/mobile-dashboard-editing).
- **On Cora Max**, load a saved design: open **Dashboard layout**, tap **My dashboards** and pick one. If you haven't saved one, rebuild the layout and tap **Save this design**, so next time it takes one tap. More in [Editing the Cora Max dashboard](/help/max-dashboard-editing#saving-layouts).

### Finding out why something changed {#establishing-why-something-changed}

**Settings → Activity** lists every outlet switch, feed and dose, and what asked for it: Cora Mobile, a Cora Max, voice, the Assistant, an automation or your account. More in [Activity and timeline](/help/mobile-activity).

## A device stopped reporting or can't be reached {#device-not-reporting}

### "[Device]: stopped reporting" {#device-stopped-reporting}

Cora sends this when a device goes quiet. It doesn't mean the device is broken, only that Cora hasn't heard from it for a while. How long Cora waits for each brand is in [Alerts and thresholds](/help/mobile-alerts#stopped-reporting).

1. Check the device's power, and its Wi-Fi or Bluetooth range.
2. Check that the Cora Max reading it is switched on and online. Without a Cora Max, your phone reads a Neptune Apex, Red Sea or Jecod device only while Cora Mobile is open on the same Wi-Fi.
3. Wait for the next reading. You get a second notification once it's reporting again.


### "Device is offline. Showing last known state." {#device-is-offline-showing-last-known-state}

The device stopped reporting, and Cora is showing the last values it had. They aren't current.

1. Check the device's own network connection.
2. Don't treat the values as live until the row stops saying offline.

### A device cannot be reached {#a-device-cannot-be-reached}

It's usually the network.

1. Is the equipment powered on and working in its own app?
2. Is it on the same network you added it on?
3. Has anything changed with your router (new hardware, new network name, guest network isolation)?

Equipment on your local network has to be reachable on that network. Equipment that connects through a manufacturer account doesn't, but that account still has to be valid. If the device's address changed, open it on the **Devices** tab and tap **Edit connection** under **Connection**.

### A device says the sign-in was refused {#a-device-says-the-sign-in-was-refused}

The manufacturer rejected the saved sign-in. Almost always, that's because you changed your password with them. Open the device's row and sign in again.

### "Red Sea readings have stopped updating" {#red-sea-readings-have-stopped-updating}

Nothing on this tank is reading your Red Sea equipment right now, so the readings on screen aren't being refreshed.

1. Open **Settings**, open the tank, then **Primary Cora Max**. Check that a Cora Max is set, or that **Any active (automatic)** is chosen.
2. If you have no Cora Max, open the tank in Cora Mobile while your phone is on the same Wi-Fi as the Red Sea gear.
3. Check that the Red Sea equipment is powered on and online in its own app.

### Some ReefBeat settings are greyed out or missing {#some-reefbeat-settings-are-greyed-out-or-missing}

That's normal. A Red Sea device's own settings only open when your phone is on the same network as the device. Away from that network you only see readings.

1. Join the tank's Wi-Fi to change those settings.
2. Readings and history keep working when you're away.


### An AquaWiz reading is hours old {#an-aquawiz-reading-is-hours-old}

That can be normal. AquaWiz lets Cora read its cloud only every 12 hours, so without a Cora Max a reading can be up to about half a day old. Open the device's page in Cora Mobile: it shows when the reading was measured and where it came from, and **Read now** asks for a fresh one (at most once every 15 minutes).

If you have a Cora Max and the card still says **From AquaWiz cloud, every 12 hours**:

- Check the controller is within Wi-Fi range of the tank's main Cora Max.
- Check the controller's firmware is up to date in the AquaWiz app; older firmware has no local access.
- After two failed reads in a row Cora Max waits until the next day. If it keeps failing, contact support.

## A command didn't go through {#command-did-not-go-through}

Every command ends as **Confirmed**, **Unconfirmed**, **Refused** or **No change**. What each one means is in [Controlling your equipment](/help/mobile-device-control).

### "Could not reach this pump: nothing was sent" {#could-not-reach-this-pump-nothing-was-sent}

A command to your Jecod or Jebao pump never left Cora. On your phone the message reads *"Could not reach this pump. It needs to be on the same Wi-Fi as your phone."* Usually the pump is off or not on its network.

1. Check the pump is powered on.
2. Check it's on the same network you added it on, and that your phone or Cora Max is on that network too.
3. Tap **Retry**.

### "Could not reach this pump over Bluetooth. Stand near it and try again." {#could-not-reach-this-pump-over-bluetooth-stand-near-it-and-t}

Your phone is out of range of a Bluetooth-only Jecod pump. Move closer to the pump and tap **Retry**.


### "Could not reach the Apex: nothing changed" / "nothing was dosed" {#could-not-reach-the-apex-nothing-changed-nothing-was-dosed}

A Neptune Apex, Trident or DŌS head didn't respond to a command or a dose request.

1. Open the Apex's own app and check it's online.
2. Check the network connection on the phone or Cora Max you're using. Changing a DŌS head from your phone needs the phone on the same network as the Apex.
3. Tap **Retry**.

### "… could not be sent: this Cora Max has no Apex details" {#this-could-not-be-sent-no-device-on-this-tank-can-send-it}

Cora Max shows this when it has no way to reach your Apex and no other device on the tank can send the command for it. The message says to add the Apex details in Settings, but they're now set on your phone.

1. On your phone, open **Devices**, then your Apex, and check its address and sign-in under **Connection**. Fix them with **Edit connection**.
2. Or make a working Cora Max the **Primary Cora Max** for this tank: **Settings**, open the tank, then **Primary Cora Max**.

### Feed doesn't start from the phone {#feed-does-not-start}

On your phone, **Feed** only shows on a tank with a Neptune Apex, and it starts one of the feed cycles programmed on the Apex.

- *"No Cora on this tank can reach the Apex, and you're not on its network."* Join the Apex's Wi-Fi, or pair a Cora Max to the tank.
- *"The Apex didn't answer, but it may already be feeding."* Check the controller before you try again.

### A dose stopped partway through and a "restore" alert appeared {#a-dose-stopped-partway-through-and-a-restore-alert-appeared}

The DŌS head lost contact during the dose. Cora tells you so it doesn't have to assume the full dose went in.

1. Open the alert and check how much was dosed before it stopped.
2. Use that amount to decide whether to resume or adjust the dose.

## Cora Max {#cora-max}

### My Cora Max is offline {#my-cora-max-is-offline}

On your phone, its row on the **Devices** tab has a red dot. While it's offline, equipment it reads stops updating, you may get "stopped reporting" alerts for that equipment, and commands sent from away can come back as *"Nothing was sent"*.

1. Check that Cora Max has power and the screen is on.
2. On Cora Max, check **Settings → Cora Max Settings → Wi-Fi**, and that your router is working.
3. If another Cora Max is on the tank, set **Primary Cora Max** to **Any active (automatic)** so it can take over. See [More than one Cora device](/help/mobile-multi-device#primary-cora-max).
4. If it won't start up properly, see [Updates and recovery](/help/max-updates).

:::tip Get told next time
In Cora Mobile, open **Settings → Automations** and make a rule with the trigger **When a device goes offline**, pick your Cora Max, and add the action **Notify Me**. More in [Automations and scenes](/help/mobile-automation).
:::

### Pairing a Cora Max fails {#pairing-a-cora-max-fails}

Cora Mobile finds a new Cora Max over Bluetooth, then gives it your Wi-Fi. Before you start, have at least one tank in Cora Mobile, Bluetooth on, and your phone near the screen. If pairing stops partway, Cora Mobile tells you why, with **Cancel** and **Retry** underneath.

- *"Bluetooth is off. Turn it on, then tap Scan again."* Turn Bluetooth on and scan again.
- *"Bluetooth permission is off for Cora. Enable it in Settings, then tap Scan again."* Allow Bluetooth for Cora in your phone's settings. **Settings → Device access** in Cora Mobile takes you there.
- *"No nearby Cora setup devices were found over Bluetooth."* Stand next to Cora Max, check that it shows its setup screen, and scan again.
- **No Tanks Found**: create a tank in Cora Mobile first, then pair.
- *"Your phone could not reach the Cora Max on your Wi-Fi."* Put your phone and Cora Max on the same Wi-Fi network. On iPhone, also check that Cora has Local Network access (**Settings → Device access**). Then tap **Retry**.
- *"The Cora Max did not accept this pairing session."* Retrying won't help. Close the screen and start again from **Devices → Add Device → Cora**.

For any other message, tap **Retry**. The whole setup is in [Setting up Cora Max](/help/max-setup).

### Cora Max shows old data {#cora-max-shows-old-data}

Look at the status tag in the top bar. **Online** and **Cloud** are both fine. If you have more than one Cora Max, the one that isn't collecting the data shows **Cloud**, and its readings are just as current. **Stale** or **Offline** means Cora Max has lost its source and is showing the last data it got.

- Check Wi-Fi under **Settings → Cora Max Settings → Wi-Fi**.
- Check that your network itself is working.
- If the tag says **Online** or **Cloud** and the data is still old, the problem is before Cora Max. Check the same tank on your phone.

### Cora Max shows "Apex password" {#cora-max-shows-apex-password}

Your Apex turned down the sign-in Cora has saved, usually because the Apex password was changed. On your phone, open **Devices**, then your Apex, and tap **Edit connection** under **Connection** to enter the new one.

### Cora Max shows "Cloud save refused" {#cora-max-shows-cloud-save-refused}

Cora Cloud is refusing to save some of this screen's data. Nothing is wrong with your tank or with Cora Max, and nothing needs changing on the screen. The fix is a Cora Cloud update.

1. Open **Settings → Cora Max Settings** and scroll to **STATUS**. The **Cloud save** line says which data is being refused, for example a device's readings or outlets.
2. [Contact support](/support.html) and tell us what that line says.

Your readings keep showing on Cora Max in the meantime. They just aren't saved to your account until the fix is in.

### A second Cora Max shows "Main Cora offline" {#a-secondary-cora-max-shows-main-cora-offline}

The Primary Cora Max for this tank has gone offline. This screen is showing the last data it received, so it isn't live.

1. Check the primary Cora Max's power and Wi-Fi.
2. Wait for it to reconnect, or change the **Primary Cora Max** to a device that's online.

### Cora Max won't reconnect right away after a Wi-Fi outage {#cora-max-wont-reconnect-right-away-after-a-wi-fi-outage}

After it loses its connection, Cora Max waits a bit longer before each retry so it doesn't flood your network. The wait grows to about a minute.

1. Give it about a minute after your network comes back.
2. If it still hasn't reconnected, check **Settings → Cora Max Settings → Wi-Fi**.

### Cora Max says "Bluetooth stopped working" {#bluetooth-stopped-working}

A card with this title covers the screen: *Cora Max can't reach your Bluetooth devices (lights, pumps, sensors). Restarting Cora Max fixes this.* It appears when Cora Max's Bluetooth has stopped and only a restart brings it back.

1. Tap **Restart now**. Cora Max restarts.
2. If now is a bad time, tap **Later**. The card goes away for 30 minutes and comes back for as long as the problem lasts.
3. If nothing restarts when you tap **Restart now**, restart Cora Max by switching its power off and on.

### Renaming a Cora Max on the phone doesn't change what it shows {#renaming-a-cora-max-on-the-phone-doesnt-change-what-the-tabl}

The name you set on your phone is the account's label for that device. The name Cora Max shows on its own pairing screen can be a different one.

1. Check which name you're looking at: the one in your phone's device list, or the one on Cora Max's pairing screen.
2. To change the account label, rename it from your phone's device list.

### I can't find where to turn off the wake word {#i-cant-find-where-to-turn-off-the-wake-word-on-cora-max}

Wake-word controls are with the sound settings, not the Cora Assistant settings.

1. On Cora Max, go to **Settings → Cora Max Settings**, and find **Wake word** under **SOUND & VOICE**.
2. Turn it off. You can still tap the **Cora Assistant** icon to start talking.

More in [Talking to Cora](/help/max-voice).

### Child lock won't let anyone into Settings {#child-lock-wont-let-anyone-into-settings}

That's what child lock does. After a set time with no touch, it stops anyone switching equipment from this screen, by touch or by voice. Readings keep updating, and you can still ask Cora questions. To unlock:

1. Press **Volume Up** or **Volume Down** three times within two seconds, or
2. Hold five fingers in the top-right corner of the screen for ten seconds.

More in [Cora Max settings](/help/max-settings#child-lock).

### A scene made on the phone isn't editable on Cora Max {#a-scene-made-on-the-phone-doesnt-show-up-as-editable-on-cora}

Only newer Cora Max versions can edit scenes on the screen. Older versions still run scenes you made on your phone, but can't edit them.

1. Update Cora Max ([Updates and recovery](/help/max-updates)), or
2. Keep editing that scene on your phone. It runs on Cora Max either way.

## Alerts, notifications and the daily briefing {#alerts-and-notifications}

### An alert is not clearing {#an-alert-is-not-clearing}

An alert clears when the reading is back in range. If it won't clear, there are three likely reasons.

- The reading really is out of range. Look at the widget's history.
- The range doesn't suit your tank. See [Alerts and thresholds](/help/mobile-alerts).
- The source is off. A probe that needs calibrating reports a number that really is out of range. Fix the probe and leave the range alone.

### An alert won't stop notifying after I acknowledged it {#an-alert-wont-stop-notifying-even-after-ive-acknowledged-it}

**Snooze** and **Dismiss** on Cora Max only quiet that one Cora Max. Your phone keeps getting notifications for as long as the reading is out of range.

1. To hear about it less often, open the alert rule in Cora Mobile and set a longer **Cooldown between alerts** (up to 1 week).
2. If the range doesn't suit your tank, change the range itself.

### I'm not getting notifications {#im-not-getting-notifications}

1. In **Settings → Notifications**, check that the category is allowed to send notifications.
2. Check your phone's own notification permission for Cora.
3. The daily briefing stays quiet on days when nothing changed. If it has stopped altogether, see the next entry.

More in [Notifications](/help/mobile-notifications).

### My daily briefing stopped {#my-daily-briefing-stopped}

- Your trial ended. Reef Buddy is part of the paid plans. After the 30-day trial, a free account stops getting the daily briefing. See [Plans and subscriptions](/help/mobile-plans).
- The tank isn't covered by your plan. Each plan covers a set number of tanks, counted in the order of **Settings → Reorder tanks**. Move a tank up to include it.
- Nothing changed today. The briefing stays quiet on a quiet day.

More in [Reef Buddy](/help/mobile-reef-buddy).

### Alerts keep coming from a tank I removed {#alerts-from-a-removed-tank}

A removed tank is kept for its history, but it sends no alerts or reminders, and its automations stop. If you still get one:

1. Open **Settings → Removed tanks**. If the tank isn't listed, it hasn't been removed.
2. Update Cora Mobile and your Cora Max to the latest version.
3. Still getting alerts? Write to support with the alert text and the time you got it. See [Reporting a problem](/help/mobile-support).

More in [Managing your tanks](/help/mobile-tanks).


## Cora Assistant and voice {#cora-assistant-and-voice}

### Cora Assistant answers about the wrong tank {#cora-assistant-answers-about-the-wrong-tank}

You didn't pick a tank before asking, or the wrong one is selected. Pick the tank you mean, then ask again. More in [Asking Cora](/help/mobile-assistant).

### Cora Assistant refuses to answer, or shows a consent screen again {#cora-assistant-refuses-to-answer-or-shows-a-consent-screen-a}

**Allow Cora Assistant to use saved tank data** is turned off, so it has nothing to answer from. Tap **Agree & Continue** on the consent screen, or turn the switch on in **Settings → Cora Assistant**.

### Cora Max says "Voice needs your OK" {#voice-needs-your-ok}

Voice on Cora Max uses the same data-sharing choice as Cora Assistant on your phone. In Cora Mobile, open **Settings → Cora Assistant** and turn on **Allow Cora Assistant to use saved tank data**, then try again. More in [Talking to Cora](/help/max-voice).

## Lab results and health reports {#lab-results-and-health-reports}

### A lab or emailed ICP result never showed up {#a-lab-or-emailed-icp-result-never-showed-up}

A result only attaches once it has a tank, sometimes Cora also needs to recognise the sender, and Cora needs your OK to read it.

1. If you see *"Cora Assistant needs your OK to read it."*, open **Settings → Cora Assistant** and turn on **Allow Cora Assistant to use saved tank data**. The result comes through once you agree.
2. Check the hint Cora shows the first time you send it a result.
3. When Cora asks, confirm which tank the result belongs to.
4. If you've sent a result before, send this one from the same email address.

More in [ICP and health reports](/help/mobile-icp-health).

### My ICP file won't upload {#my-icp-file-wont-upload}

Cora reads the PDF report your lab sends. Photos and screenshots can't be read. Download the PDF from your lab first, then tap **Upload ICP** again.

### The screen goes black after a health report or ICP upload {#black-screen-after-a-report}

This could happen in Cora Mobile 1.2 and earlier, and Cora Mobile 1.3 fixes it: update Cora Mobile from the App Store or Google Play. If you see it before you update, close Cora Mobile and open it again. The report was saved, and you'll find it under **Intelligence**.

## Language, units and signing in {#language-units-and-signing-in}

### Everything is suddenly in the wrong language {#everything-is-suddenly-in-the-wrong-language}

Someone changed the account language on one of your devices. It's one setting for the whole account.

1. Open **Settings → Language** in Cora Mobile or on Cora Max.
2. Set it back. The change applies everywhere.

### An old alert or report is in a different language after switching {#an-old-alert-or-report-is-still-in-a-different-language-afte}

That's expected. Cora doesn't retranslate anything it already wrote. New alerts, reports and briefings use the new language.

### "Could not reach Cora. Check your Wi-Fi or mobile data, then try again." {#could-not-reach-cora-check-your-wi-fi-or-mobile-data-then-tr}

Your phone can't reach Cora Cloud to sign in. This is about your phone's connection, not your tank equipment.

1. Check that your phone has working Wi-Fi or mobile data.
2. Try a different network if you have one.
3. Tap **Retry**.

Other sign-in problems are in [Signing in and account recovery](/help/mobile-account).

## Still stuck {#still-stuck}

Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)**, or report it from Cora Mobile as described in [Reporting a problem](/help/mobile-support). Tell us which tank, which device, which screen, and what you expected to see.
