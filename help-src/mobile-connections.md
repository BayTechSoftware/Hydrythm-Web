---
title: Connecting your equipment
description: How to connect a Neptune Apex, Red Sea ReefBeat, Jecod or AquaWiz unit to Cora.
section: Cora Mobile
reviewed: 2026-10-17
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
6. Tap **Continue**, tick every tank under **Which tanks does this Apex serve?**, then tap **Save**. An Apex can serve more than one tank.

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

Cora reads alkalinity from an AquaWiz KH controller through your AquaWiz account, so it works away from home and doesn't need a Cora Max.

1. Go to **Devices → Add Device → AquaWiz**.
2. Enter your AquaWiz username and password and tap **Connect**.
3. Pick the tank, check **Also read its pH** (it starts on for a unit that reports pH), and tap **Link to Cora**.

With **Stay connected automatically** on, Cora keeps your AquaWiz password and renews the connection on its own. With it off, Cora keeps only a sign-in token, which AquaWiz expires about every 30 days, and sends you a notification when it's time to sign in again.

You get alkalinity as a source, and pH too if your unit reports it and **Also read its pH** is on. Your first reading arrives as soon as you link. After that AquaWiz lets Cora read its cloud automatically only every 12 hours, so a reading from there can be up to about half a day old. A Cora Max at the tank can also read the controller itself every hour when it can reach it. Open the device's page to see when each reading was measured and where it came from, and tap **Read now** for a fresh one (at most once every 15 minutes). What the AquaWiz card shows, and its alerts, are in [Controlling your equipment](/help/mobile-device-control#aquawiz).

:::warning Cora shares your AquaWiz sign-in
AquaWiz gives each account one sign-in, so Cora uses the same one as the AquaWiz app. If you change your AquaWiz password, Cora disconnects. Reconnect it from the device row afterwards. To take away Cora's access completely, remove the device in Cora and change your AquaWiz password.
:::


## Logging by hand {#logging-by-hand}

Some parameters come from a test kit, not from equipment. To enter a result, scroll to the bottom of the dashboard and tap **Log Parameters**.

Readings you log by hand count as much as any other. They show on widgets with their own source and age, and they feed Reef Buddy. Cora also checks your probes against them when it tells you two sources disagree.

## If a connection stops working {#if-a-connection-stops-working}

The device row tells you what kind of problem it is. Look it up in the table in [Adding, editing and removing devices](/help/mobile-devices#health). For anything that doesn't cover, see [Troubleshooting](/help/troubleshooting).
