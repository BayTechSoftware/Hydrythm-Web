---
title: Connecting your equipment
description: How to connect Neptune Apex, Red Sea ReefBeat, Jecod, AquaWiz, GHL and HYDROS equipment to Cora.
section: Cora Mobile
reviewed: 2026-09-30
order: 10
group: Equipment
---

Cora works with equipment you already own. This page covers what's supported and what each connection needs.

They all start the same way: **Devices → Add Device**, then pick the brand. Each one opens exactly what it needs to find your equipment.

| Brand | Opens |
|---|---|
| Cora | A scan for a new Cora Max, over Wi-Fi or Bluetooth |
| Neptune Apex | Its address on your network, sign-in, then which tank it belongs to |
| Red Sea | A scan on your network, then which tank each unit belongs to |
| Jecod / Jebao | A scan on your network, or Bluetooth |
| Maxspect *(beta)* | The same scan as Jecod |
| GHL *(beta)* | Its address, interface and, for a mini, its login |
| HYDROS *(beta)* | A device key from the HYDROS app |
| AquaWiz | Your AquaWiz sign-in |

## Neptune Apex

Cora reads your Apex over your local network, including probes, outlets and any expansion modules you've fitted.

Add it from **Devices → Add Device → Neptune Apex**. You need its address on your network and its sign-in, then you pick which tank it belongs to. An Apex can serve more than one tank.

Once it's connected, every probe your Apex reports becomes a source you can put on a dashboard. Outlets show up as controls, and each fitted expansion module gets its own device tile.

:::note Your Apex keeps its own programming
Cora reads your Apex, shows it next to everything else and can switch outlets when you ask. Your own programming keeps running exactly as you set it up.
:::

## Red Sea ReefBeat

Cora talks to ReefBeat equipment on your local network. It supports **ReefDose**, **ReefATO+**, **ReefMat**, **ReefRun**, and, in beta, **ReefControl**, **ReefControl Power**, **ReefWave** and **ReefLED**.

Before you add a unit, set it up in ReefBeat and make sure it's on the same network as your phone. Add it from **Devices → Add Device → Red Sea**, which scans your network and asks which tank each unit belongs to. A Red Sea unit serves one tank: picking a different one moves it there.

Each unit gets its own device page, and its readings become sources. ReefDose reports its heads and containers. ReefATO+ reports its reservoir and fills. ReefMat reports the days it has left, and ReefRun reports pump state. ReefControl reports its probes the same way. ReefWave and ReefLED *(beta)* show their mode only, for now, view only.

## Jecod / Jebao

Cora connects to Jecod pumps and can read and control them. Add one from **Devices → Add Device → Jecod**. A Jecod pump reaches Cora in one of two ways, and that decides what you can do with it.

![Finding a pump](img/mobile-connections.webp "The scan explains what it needs and why a pump may not appear on the first sweep.")

**Over your network.** The scan finds pumps that announce themselves, so you don't have to type an address. You can read and drive a network pump whenever it's powered **and reachable**. That means your phone is on the same network, or a Cora Max on that network passes your commands on. If you're away from home and there's no Cora Max on site, you can see a network-only pump but you can't control it.

:::note A pump often misses the first scan
Pumps answer one scan and miss the next. If yours isn't listed, scan again before you decide it can't be reached.
:::

If a search finds nothing, the result shows the addresses it checked over Wi-Fi. If the Jebao app shows a different address for your pump, your phone is on another network. A guest or IoT network, or a 5 GHz-only band, won't see these pumps. On iPhone, Cora also needs Local Network access to see pumps on your Wi-Fi. Without it the list stays empty and no error appears, so the result explains this and offers **Open Settings** to turn it back on. You can also get there any time from **Settings → Device access**, described in [Settings](/help/mobile-settings).

**Over Bluetooth.** Some pumps can only be reached from a phone standing near them. The pump's page says so, and shows the last settings it read and how old they are.

Cora needs Bluetooth permission for this. Grant it before you add a Bluetooth pump. Without it, Cora can't find the pump at all.

With either connection you get live state, mode and intensity, a feeding pause and a day program. [Scheduling equipment](/help/mobile-schedules) covers the program.

:::warning You have to be near a Bluetooth pump
Its page shows the last settings Cora read and how long ago. Changing anything, even starting a feeding pause, needs the pump in range. Stand near it and open the page again.
:::

## AquaWiz KH Controller

Cora reads alkalinity from an AquaWiz KH controller through your AquaWiz account. Add it from **Devices → Add Device → AquaWiz**.

To connect it, you need your AquaWiz username and password. Cora signs in for you and keeps the sign-in so it can go on reading.

You get alkalinity as a source, updated as often as your controller titrates. You can add pH too if your unit reports it.

The device's own card also shows your target KH, your dose strength and, for a unit with dosing set up, its maximum dose per hour and how much alkalinity supplement is left in the container. These come straight from your AquaWiz settings. Change them in the AquaWiz app. If your unit tracks its container, Cora warns you when the supplement is running low, at 100 mL by default.

:::warning Cora shares your AquaWiz sign-in
AquaWiz gives each account one sign-in, so Cora uses the same one as the AquaWiz app. If you change your AquaWiz password, Cora disconnects. Reconnect it from the device row afterwards. To take away Cora's access completely, remove the device in Cora and change your AquaWiz password.
:::

## Maxspect

:::note Maxspect support is in beta
We're still testing and developing Maxspect gyre support. Some controls may be limited, and what you see here may change between updates. If something doesn't work as described, let us know from [Getting help](/help/mobile-support).
:::

Cora connects to Maxspect Gyre pumps and can read and drive them. Add one from **Devices → Add Device → Maxspect**, the same scan Jecod uses.

When you add a gyre, it has to be on the same network as your phone.

You can set wave pattern and speed for **Gyre A** and **Gyre B**. You can see the gyre's schedule (set it in the Maxspect app), **Pump health**, and whether it's running, with when it was last read. [Controlling your equipment](/help/mobile-device-control) has the details.

:::note How Cora Mobile reaches a gyre
If a Cora Max serves the tank, Cora Mobile goes through that Cora Max, even when you're away from home. **Change settings** then starts from that Cora Max's last reading. Otherwise your phone talks to the gyre directly and has to be on the gyre's network. Opening the gyre's page reads it. If the page is showing an older stored reading, **Change settings** stays hidden until you tap refresh.
:::

## GHL ProfiLux and Mitras

:::note GHL support is in beta
We're still testing and developing GHL support. Some readings or controls may not work yet, and what you see here may change between updates. If something doesn't work as described, let us know from [Getting help](/help/mobile-support).
:::

Cora reads a GHL ProfiLux or Mitras controller: probes, sockets, dosers, level sensors and, on the Director models, KH and ion test results.

Add it from **Devices → Add Device → GHL**. Your phone can't scan for it, so enter its address and pick the interface yourself: **Official API**, **HTTP**, or **ProfiLux mini** (which also needs its login). Then pick which tank it belongs to. A GHL controller can serve more than one tank.

A GHL controller doesn't talk to your phone directly. It shows **Waiting for Cora Max** until a Cora Max on its network has read it, then its readings and controls show up everywhere.

The GHL API has to be switched on for Cora to reach the controller at all. GHL turns it off after every firmware update, so this is worth checking first if nothing appears. [Troubleshooting](/help/troubleshooting) covers what to do.

## HYDROS

:::note HYDROS support is in beta
We're still testing and developing HYDROS support. Some readings or controls may not work yet, and what you see here may change between updates. If something doesn't work as described, let us know from [Getting help](/help/mobile-support).
:::

HYDROS is the only integration that doesn't need your Cora and your controller on the same network. Cora reaches it through HYDROS's own cloud, so it keeps working away from home, and even with Cora closed.

To connect it, open the HYDROS app and create a **device key** for the provider **cora-iq**. Choose **Read** if you only want its readings, or **Write** if you also want to control it from Cora. Then go to **Devices → Add Device → HYDROS** and paste the key in.

Once it's linked, Cora imports the last 33 days of its history, then keeps reading forward from there. [Controlling your equipment](/help/mobile-device-control) covers what you can read and, with a write key, control.

## Logging by hand

Some parameters come from a test kit, not from equipment. To enter a result, scroll to the bottom of the dashboard and tap **Log Parameters**.

Readings you log by hand count as much as any other. They show on widgets with their own source and age, and they feed Reef Buddy. Cora also checks your probes against them when it tells you two sources disagree.

## If a connection stops working

The device row tells you what kind of problem it is. Look it up in the table in [Adding, editing and removing devices](/help/mobile-devices). For anything that doesn't cover, see [Troubleshooting](/help/troubleshooting).
