---
title: Connecting your equipment
description: Connect a Neptune Apex, Red Sea ReefBeat, Jecod or AquaWiz unit to Cora, use it without a Cora Max, and fix a connection that stops working.
section: Cora Mobile
reviewed: 2026-10-24
order: 12
group: Equipment
---

This page shows how to connect each brand of equipment to Cora and what each connection needs. They all start the same way: **Devices → Add Device**, then pick the brand.

![The Add Device brand list](img/mobile-add-device-brands.webp "The brand list.")


| Brand | Opens | Without a Cora Max |
|---|---|---|
| Cora | A scan for a new Cora Max, over Wi-Fi or Bluetooth | |
| Neptune Apex | A network scan or its IP address, then which tanks it serves | Local only |
| Red Sea | A scan on your network, then which tank each unit belongs to | Local only |
| Jecod / Jebao | A scan on your network, or Bluetooth | Local only |
| AquaWiz | Your AquaWiz sign-in | Works |

## Without a Cora Max: local only {#local-only}

Neptune Apex, Red Sea and Jecod equipment is on your home network (or Bluetooth). If you have no Cora Max (or none on the tank you're adding to), the add screen for these brands says *This integration works only locally on the Mobile app without Cora Max.* That means:

- Your phone reads and controls the equipment while Cora Mobile is open on the same network, or in Bluetooth range.
- Away from home you see the last readings your phone saved, and you can't control it.

A Cora Max at the tank reads this equipment around the clock and passes on your commands when you're away. AquaWiz is reached through the maker's own service, so it works from anywhere without a Cora Max. More in [More than one Cora device](/help/mobile-multi-device).

## Neptune Apex {#neptune-apex}

Cora reads your Apex over your local network, including probes, outlets and any expansion modules you've fitted.

1. Go to **Devices → Add Device → Neptune Apex**.
2. Tap **Scan Network for APEX** and pick your Apex, or type its address under **Or enter IP manually:**.
3. Fill in **Apex login (only if you set one on the Apex):**. Leave the password blank if you haven't set one.
4. Tap **Load metrics from APEX** and tick the ones you want under **Metrics to track**.
5. Set **Poll Frequency**. Don't leave it off: with polling off, nothing reads the Apex and its readings go stale.
6. Tap **Continue**. Cora tests the login first. If the Apex answers and turns it down, a message says **The Apex refused this login**: tap **Cancel** to fix the username or password, or **Save anyway** to go on. If Cora can't reach the Apex (for example you are away from home), it skips the test. Then tick every tank under **Which tanks does this Apex serve?** and tap **Save**. An Apex can serve more than one tank.

If the scan finds nothing, check that your phone is on the same Wi-Fi as the Apex, or enter the IP address yourself.

Once it's connected, every probe your Apex reports becomes a source you can put on a dashboard. Outlets show up as controls, and each fitted expansion module gets its own device tile. Your own Apex programming keeps running exactly as you set it up. What you can control is in [Controlling your equipment](/help/mobile-device-control#neptune-apex).

## Red Sea ReefBeat {#red-sea-reefbeat}

Cora talks to ReefBeat equipment on your local network. It supports **ReefDose**, **ReefATO+**, **ReefMat** and **ReefRun**.

1. Set the unit up in Red Sea's ReefBeat app first, and check it's on the same network as your phone.
2. Go to **Devices → Add Device → Red Sea**. Cora scans your network.
3. Pick which tank each unit belongs to.

A Red Sea unit serves one tank. Picking a different one moves it there.

Each unit gets its own device page, and its readings become sources. ReefDose reports its heads and containers, ReefATO+ its reservoir and fills, ReefMat the days it has left, and ReefRun its pump state. What each page lets you do is in [Controlling your equipment](/help/mobile-device-control#red-sea).

## Jecod / Jebao {#jecod}

Cora connects to Jecod pumps and can read and control them. Add one from **Devices → Add Device → Jecod**. A Jecod pump reaches Cora in one of two ways, and that decides what you can do with it.

![The Add a pump screen in Cora Mobile, with no pumps found yet](img/mobile-connections.webp "None seen yet: the scan explains what it needs and why a pump can miss a sweep.")

**Over your network.** The scan finds pumps that announce themselves, so you don't have to type an address. You can read and drive a network pump whenever it's powered and reachable. That means your phone is on the same network, or a Cora Max on that network passes your commands on. If you're away from home and there's no Cora Max on site, you can see a network pump but you can't control it.

:::note A pump often misses the first scan
Pumps answer one scan and miss the next. If yours isn't listed, scan again before you decide it can't be reached.
:::

If a search finds nothing, the result shows the addresses it checked over Wi-Fi. If the Jebao app shows a different address for your pump, your phone is on another network. A guest or IoT network, or a 5 GHz-only band, won't see these pumps. On iPhone, Cora also needs Local Network access to see pumps on your Wi-Fi. Without it the list stays empty and no error appears, so the result explains this and offers **Open Settings** to turn it back on. You can also get there any time from **Settings → Device access**, described in [Settings](/help/mobile-settings).

**Over Bluetooth.** Some pumps can only be reached from a phone standing near them. The pump's page says so, and shows the last settings it read and how old they are. Cora needs Bluetooth permission for this. Grant it before you add a Bluetooth pump, or Cora can't find the pump at all.

:::warning You have to be near a Bluetooth pump
Its page shows the last settings Cora read and how long ago. Changing anything, even starting a feeding pause, needs the pump in range. Stand near it and open the page again.
:::

With either connection you get live state, mode and intensity, a feeding pause and a schedule. A feeding pause started from your phone needs the pump's page kept open on some pumps. The details are in [Controlling your equipment](/help/mobile-device-control#jecod), and [Scheduling equipment](/help/mobile-schedules) covers the schedule.

## AquaWiz KH Controller {#aquawiz-kh-controller}

Cora reads alkalinity from an AquaWiz KH controller through AquaWiz's cloud, so it works away from home and doesn't need a Cora Max. A Cora Max adds hourly readings: see [How Cora reads your AquaWiz](#how-cora-reads-aquawiz).

1. Go to **Devices → Add Device → AquaWiz**.
2. Sign in with the AquaWiz account you use in the AquaWiz app and tap **Connect**.
3. Pick the tank, check **Also read its pH** (it starts on for a unit that reports pH), and tap **Link to Cora**.

You sign in once, so Cora can find your controllers. After that Cora keeps only your AquaWiz username: no password and no sign-in token. There is nothing to renew, so Cora never asks you to sign in again, and there is no **Stay connected automatically** switch. If AquaWiz later reports that the username no longer owns the controller, its card turns orange and tells you to link it again: open **Add AquaWiz** and sign in once more.

You get alkalinity as a source, and pH too if your unit reports it and **Also read its pH** is on. Your first reading arrives as soon as you link, together with the last 6 hours of history. After that AquaWiz's Cora service sends a reading every 12 hours, which is AquaWiz's limit, so a reading from there can be up to about half a day old. A Cora Max at the tank can also read the controller itself every hour when it can reach it. Open the device's page to see when each reading was measured and where it came from, and tap **Read now** for a fresh one (at most once every 15 minutes). What the AquaWiz card shows, and its alerts, are in [Controlling your equipment](/help/mobile-device-control#aquawiz).

To move the controller to another tank, open its page in **Devices** and tap **Change** under **Tanks**. You don't have to sign in to AquaWiz again.

:::note Cora keeps only your username
Cora uses your password once, while you link, and does not store it. Changing your AquaWiz password doesn't disconnect Cora. Unlinking stops Cora reading the controller and makes it forget your username; it doesn't sign you out of the AquaWiz app. Your existing readings are kept.
:::

### How Cora reads your AquaWiz {#how-cora-reads-aquawiz}

Cora reaches an AquaWiz in up to three ways, and they work together.

| Route | What it gives Cora | How often |
| --- | --- | --- |
| Your AquaWiz sign-in | Used once, when you link, to find your controllers. Afterwards Cora keeps only your username. | Once |
| AquaWiz's Cora service | The latest KH and pH reading, the last 6 hours of history, and the controller's settings (target KH, dose strength, supplement left, pump and pH probe status, firmware). | When you link, then every 12 hours (the AquaWiz limit), and when you open the device page or tap **Read now** (at most every 15 minutes) |
| A Cora Max at the tank | Reads the controller directly over the controller's own Wi-Fi and adds water box level alerts. | Every hour |

Without a Cora Max, readings come every 12 hours, which is AquaWiz's limit, so one can be up to about half a day old. **Want hourly readings? Add a Cora Max at your tank.** [See Cora Max](https://coraiq.tech/#max) and [set it up](/help/max-setup). It needs the controller within Cora Max's Wi-Fi range and controller firmware with local access. The details are in [Hourly reading from Cora Max](/help/max-device-control#aquawiz-hourly).

The device card shows where each reading came from: **Hourly from your Cora Max** or **From AquaWiz cloud, every 12 hours**.

Cora keeps the full hourly history of your controller. When you link, it back-fills up to 30 days, so your charts don't start empty.


## Logging by hand {#logging-by-hand}

Some parameters come from a test kit, not from equipment. To enter a result, scroll to the bottom of the dashboard and tap **Log Parameters**.

Readings you log by hand count as much as any other. They show on widgets with their own source and age, and they feed Reef Buddy. Cora also checks your probes against them when it tells you two sources disagree.

## If a connection stops working {#if-a-connection-stops-working}

The device row tells you what kind of problem it is. Look it up in the table in [Adding, editing and removing devices](/help/mobile-devices#health). For anything that doesn't cover, see [Troubleshooting](/help/troubleshooting).
