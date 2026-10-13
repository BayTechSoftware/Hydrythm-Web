---
title: Connecting your equipment
description: How to connect a Neptune Apex, Red Sea ReefBeat, Jecod or AquaWiz unit and, in Beta, Maxspect, GHL, HYDROS, Focustronic and Inkbird equipment to Cora.
section: Cora Mobile
reviewed: 2026-10-13
order: 12
group: Equipment
---

This page shows how to connect each brand of equipment to Cora and what each connection needs. They all start the same way: **Devices → Add Device**, then pick the brand.

![The Add device list for a Beta user](img/mobile-add-device-beta.webp "The brand list. Beta brands carry a Beta chip.")

The brands marked *(Beta)* are only open to Beta users. See [Beta features](/help/mobile-beta).

| Brand | Opens | Without a Cora Max |
|---|---|---|
| Cora | A scan for a new Cora Max, over Wi-Fi or Bluetooth | |
| Neptune Apex | A network scan or its IP address, then which tanks it serves | Local only |
| Red Sea | A scan on your network, then which tank each unit belongs to | Local only |
| Jecod / Jebao | A scan on your network, or Bluetooth | Local only |
| AquaWiz | Your AquaWiz sign-in | Works |
| Maxspect *(Beta)* | The same scan as Jecod | **Requires Cora Max** |
| GHL *(Beta)* | Its address, interface and, for a mini, its login | **Requires Cora Max** |
| HYDROS *(Beta)* | A device key from the HYDROS app | Works |
| Focustronic *(Beta)* | Your Focustronic sign-in, then which tank each device belongs to | Works |
| EcoTech *(Beta)* | A Bluetooth scan for Radion lights, VorTech pumps and Versa dosers. See [EcoTech lights, pumps and dosers](/help/mobile-ecotech) | **Requires Cora Max** |
| Inkbird *(Beta)* | A Bluetooth scan for your room air monitor | **Requires Cora Max** |
| Camera *(Beta)* | Wyze, Tapo, Sonoff or another RTSP camera. See [Cameras and Skimmer Watch](/help/mobile-cameras) | **Requires Cora Max** |

## Without a Cora Max: local only {#local-only}

Neptune Apex, Red Sea and Jecod equipment is on your home network (or Bluetooth). If you have no Cora Max (or none on the tank you're adding to), the add screen for these brands says *This integration works only locally on the Mobile app without Cora Max.* That means:

- Your phone reads and controls the equipment while Cora Mobile is open on the same network, or in Bluetooth range.
- Away from home you see the last readings your phone saved, and you can't control it.

A Cora Max at the tank reads this equipment around the clock and passes on your commands when you're away. AquaWiz, HYDROS and Focustronic are reached through the maker's own service, so they work from anywhere without a Cora Max. Rows marked **Requires Cora Max** are greyed out until the tank has one. More in [More than one Cora device](/help/mobile-multi-device).

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

Cora talks to ReefBeat equipment on your local network. It supports **ReefDose**, **ReefATO+**, **ReefMat** and **ReefRun**, plus **ReefControl**, **ReefControl Power**, **ReefWave** and **ReefLED**, which carry *(Beta)* in their name but are open to everyone.

1. Set the unit up in Red Sea's ReefBeat app first, and check it's on the same network as your phone.
2. Go to **Devices → Add Device → Red Sea**. Cora scans your network.
3. Pick which tank each unit belongs to.

A Red Sea unit serves one tank. Picking a different one moves it there.

Each unit gets its own device page, and its readings become sources. ReefDose reports its heads and containers, ReefATO+ its reservoir and fills, ReefMat the days it has left, and ReefRun its pump state. ReefControl reports its probes the same way. ReefWave and ReefLED show their mode only, for now. What each page lets you do is in [Controlling your equipment](/help/mobile-device-control#red-sea).

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

With either connection you get live state, mode and intensity, a feeding pause and a day program. A feeding pause started from your phone needs the pump's page kept open on some pumps. The details are in [Controlling your equipment](/help/mobile-device-control#jecod), and [Scheduling equipment](/help/mobile-schedules) covers the day program.

## AquaWiz KH Controller {#aquawiz-kh-controller}

Cora reads alkalinity from an AquaWiz KH controller through your AquaWiz account, so it works away from home and doesn't need a Cora Max.

1. Go to **Devices → Add Device → AquaWiz**.
2. Enter your AquaWiz username and password and tap **Connect**.
3. Pick the tank, turn on **Also read its pH** if you want it, and tap **Link to Cora**.

With **Stay connected automatically** on, Cora keeps your AquaWiz password and renews the connection on its own. With it off, Cora keeps only a sign-in token, which AquaWiz expires about every 30 days, and sends you a notification when it's time to sign in again.

You get alkalinity as a source, updated as often as your controller titrates, and pH too if you turned it on and your unit reports it. What the AquaWiz card shows, and its supplement alert, are in [Controlling your equipment](/help/mobile-device-control#aquawiz).

:::warning Cora shares your AquaWiz sign-in
AquaWiz gives each account one sign-in, so Cora uses the same one as the AquaWiz app. If you change your AquaWiz password, Cora disconnects. Reconnect it from the device row afterwards. To take away Cora's access completely, remove the device in Cora and change your AquaWiz password.
:::

## Maxspect {#maxspect}

:::note Beta
**Beta.** Maxspect is in Beta and only open to Beta users. If you are not a Beta user you will not see it in **Add device**. To ask for Beta access, contact [support](/support.html). Some controls may be limited, and what you see here may change between updates. If something doesn't work as described, let us know from [Reporting a problem](/help/mobile-support).
:::

Cora connects to Maxspect Gyre pumps and can read and drive them. Add one from **Devices → Add Device → Maxspect**, the same scan Jecod uses. It needs a Cora Max in the tank. Without one the row shows **Requires Cora Max**.

When you add a gyre, it has to be on the same network as your phone. After that, Cora Mobile reaches it through the tank's Cora Max, even when you're away. Wave pattern, speed, the schedule and **Pump health** are in [Controlling your equipment](/help/mobile-device-control#maxspect).

## GHL ProfiLux and Mitras {#ghl-profilux-and-mitras}

:::note Beta
**Beta.** GHL is in Beta and only open to Beta users. If you are not a Beta user you will not see it in **Add device**. To ask for Beta access, contact [support](/support.html). Some readings or controls may not work yet. If something doesn't work as described, let us know from [Reporting a problem](/help/mobile-support).
:::

Cora reads a GHL ProfiLux or Mitras controller: probes, sockets, dosers, level sensors and, on the Director models, KH and ion test results.

1. Go to **Devices → Add Device → GHL**. It needs a Cora Max in the tank, and shows **Requires Cora Max** without one.
2. Your phone can't scan for it, so enter its address and pick the interface yourself: **Official API**, **HTTP**, or **ProfiLux mini** (which also needs its login).
3. Pick which tank it belongs to. A GHL controller can serve more than one tank.

A GHL controller doesn't talk to your phone directly. It shows **Waiting for Cora Max** until a Cora Max on its network has read it, then its readings and controls show up everywhere.

The GHL API has to be switched on for Cora to reach the controller at all. GHL turns it off after every firmware update, so check this first if nothing appears. [Troubleshooting](/help/troubleshooting) covers what to do. Controls are in [Controlling your equipment](/help/mobile-device-control#ghl).

## HYDROS {#hydros}

:::note Beta
**Beta.** HYDROS is in Beta and only open to Beta users. If you are not a Beta user you will not see it in **Add device**. To ask for Beta access, contact [support](/support.html). Some readings or controls may not work yet. If something doesn't work as described, let us know from [Reporting a problem](/help/mobile-support).
:::

HYDROS doesn't need your phone and your controller on the same network, or a Cora Max. Cora reaches it through HYDROS's own cloud, so it keeps working away from home, and even with Cora Mobile closed.

1. In the HYDROS app, create a **device key** for the provider **cora-iq**. Choose **Read** if you only want its readings, or **Write** if you also want to control it from Cora.
2. In Cora Mobile, go to **Devices → Add Device → HYDROS**. The screen is called **Add HYDROS (Beta)**.
3. Paste the key into **HYDROS device key**, tap **Check key**, pick the tank and tap **Link**.

Once it's linked, Cora imports the last 33 days of its history, then keeps reading forward from there. [Controlling your equipment](/help/mobile-device-control#hydros) covers what you can read and, with a write key, control.

## Focustronic {#focustronic}

:::note Beta
**Beta.** Focustronic is in Beta and only open to Beta users. If you are not a Beta user you will not see it in **Add device**. To ask for Beta access, contact [support](/support.html).
:::

Cora reads Focustronic Alkatronic, Dosetronic and Mastertronic devices through your Focustronic account, so it works away from home and doesn't need a Cora Max.

1. Go to **Devices → Add Device → Focustronic** and sign in with the same account you use in the Focustronic app.
2. Choose which tank each device belongs to, then tap **Link to Cora**.

**Stay signed in** lets Cora keep your Focustronic password, encrypted, and sign in again on its own. If you turn it off, Cora keeps only a temporary sign-in and sends you a notification when you need to sign in again. If Focustronic refuses the sign-in, open **Add Focustronic** and sign in again.

What each device shows, and **Measure now**, **Dose now** and **Test now**, are in [Controlling your equipment](/help/mobile-device-control#focustronic).

## Inkbird room air monitor {#inkbird-room-air-monitor}

:::note Beta
**Beta.** Inkbird is in Beta and only open to Beta users. If you are not a Beta user you will not see it in **Add device**. To ask for Beta access, contact [support](/support.html).
:::

Cora reads an Inkbird IAM-T1 or IAM-T2 room air monitor. A Cora Max in the tank reads it over Bluetooth, and Cora never writes anything to the monitor. The row shows **Requires Cora Max** until the tank has one.

1. Go to **Devices → Add Device → Inkbird**. Cora scans for monitors nearby. Bluetooth has to be on, with permission for Cora.
2. Pick yours and tap **Link to tank**. If none appears, move closer and tap **Scan again**.

The monitor's page shows its last reading. **Sampling interval** sets how often a Cora Max reads it. Until a Cora Max has read it, the page says **Waiting for Cora Max**. If it goes quiet it shows **Not reporting** and Cora warns you. Room readings also feed [Reef Buddy](/help/mobile-reef-buddy). To stop, **Unlink** it. Cora Max stops reading it and the history stays.

## Logging by hand {#logging-by-hand}

Some parameters come from a test kit, not from equipment. To enter a result, scroll to the bottom of the dashboard and tap **Log Parameters**.

Readings you log by hand count as much as any other. They show on widgets with their own source and age, and they feed Reef Buddy. Cora also checks your probes against them when it tells you two sources disagree.

## If a connection stops working {#if-a-connection-stops-working}

The device row tells you what kind of problem it is. Look it up in the table in [Adding, editing and removing devices](/help/mobile-devices#health). For anything that doesn't cover, see [Troubleshooting](/help/troubleshooting).
