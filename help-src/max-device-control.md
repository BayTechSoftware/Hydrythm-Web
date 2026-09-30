---
title: Controlling equipment from Cora Max
description: Device pages on the big screen for probes, outlets, dosing heads, testers and pumps.
section: Cora Max
reviewed: 2026-09-30
order: 6
group: Equipment
---

Cora Max reaches the same equipment as your phone, and each device has its own page. Open one from **Settings → Devices**, or tap a device tile on the dashboard.

![An Apex page on Cora Max](img/max-device-control.webp "Feed cycles and every outlet, laid out for a wall screen.")

:::warning These controls act on live equipment
There's no preview and no undo. A command goes out the moment you tap, but sending it doesn't mean it's done. It comes back **Confirmed**, **Unconfirmed**, **Refused** or **No change**, and you can see which in [Activity](/help/max-activity).
:::

## What has a page

| Device | Shows |
|---|---|
| **Neptune Apex** | Probes and outlets, and you can switch each outlet |
| **Trident** | Test state, reagent and waste levels, and a button to start a test |
| **DŌS**, including the DŌS QD | Each head's dosing, schedule, runway and container volume (with pause, fill, dose now and a one-time twenty-second measure) |
| **Red Sea ReefBeat** | Whatever the unit has: dosing heads, reservoir, roller days, pump mode, plus a full ReefDose plan and ReefRun program editor and ReefMat settings *(beta)* |
| **ReefControl**, **ReefControl Power**, **ReefWave**, **ReefLED** *(beta)* | ReefControl's probes. ReefControl Power's sockets as outlets, on or off, no automatic mode yet. ReefWave and ReefLED, view only |
| **Jecod** | Pump mode and intensity, and its day program |
| **Maxspect** *(beta)* | Mode and speed for **Gyre A** and **Gyre B**, **Pump health** (cleaning countdown, head A current, fitted heads, firmware), and its schedule, view only |
| **GHL ProfiLux / Mitras** *(beta)* | Probes, sockets, dosers, level sensors and, on the Director models, KH and ion test results |
| **HYDROS** *(beta)* | Whatever its device key reports: inputs, and with a write key, outputs, modes, dosing heads and tester commands |

If a Red Sea unit stops itself, its page tells you what's wrong and puts the fix right next to it. That's **Resume**, **Clear emergency**, **Sensor cleaned**, **I already loaded a new roll**, or **Reset** for a dosing head.

A ReefDose plan, a ReefRun speed program and ReefMat's scheduled advance, model, position and New roll all work the same way here as on your phone. [Connecting your equipment](/help/mobile-connections) and [Controlling your equipment](/help/mobile-device-control) have the detail.

## DŌS heads

You have to measure a DŌS head once before Cora will dose with it by hand. **Measure to dose** runs the head for twenty seconds into a measuring container, and you enter how much came out. Cora keeps one measurement per head and uses the newest, whichever Cora Max took it. The head's page shows where and when it was measured.

After a manual dose, a head you'd set to Off in Apex Fusion stays Off. Any other head goes back to Auto.

### What a head is used for

In a head's settings sheet you can set its **use type**. The options are **Supplement**, **Water change: new saltwater in**, **Water change: old water out**, **Kalkwasser**, **Calcium reactor**, **Food** or **Top-off**, and **Other**. The use type changes two things.

- How big a container it can track. A Supplement head tracks up to 20 litres. Every other use type can track a container of up to 500 litres, so a head running a water change or a calcium reactor isn't treated like a small dosing bottle.
- Whether it can take a large dose by hand. Supplement and Food heads keep today's small, careful ceiling. Every other use type can have its own **Largest dose by hand** limit, up to a hard ceiling of 10 litres, and its own **daily limit for automations and the Assistant**. A large hand dose also needs **Large doses (Beta)** turned on in the head's settings, off by default: turn it on only after you've watched the first large dose run at the tank.

You can link a water-change pair (new saltwater in, old water out) as a **Paired head** and set a **Balance warning above** amount. If the two heads' totals for the day drift apart by more than that, Cora warns you. A pair that's out of balance usually means one side isn't pumping as it should.

### If a large dose is interrupted

A large dose changes what the head is doing on the Apex for a while, then puts its normal schedule back. If the connection drops partway through, Cora Max shows a banner on that head's page: *"A large dose on [head] did not finish cleanly. Cora keeps trying to put its program back; check it in Apex Fusion."*

Check the head in Apex Fusion yourself, then tap **I checked the head in Fusion** to clear the banner. Only do this once you've confirmed that the head's own schedule is running, not Cora's dosing program.

If the banner won't clear, or keeps coming back, have a look at [Troubleshooting](/help/troubleshooting).

## GHL ProfiLux and Mitras

:::note GHL support is in beta
We're still testing and developing GHL support. Some readings or controls may not work yet, and what you see here may change between updates.
:::

Connect a GHL controller from **Settings → [your tank] → GHL controller (Beta)**. Enter its IP address on your network and tap **Detect**. Cora tries the controller's official API first, then its other interfaces, and tells you which one it found.

If nothing answers and the controller is a ProfiLux mini, Cora offers a fallback: enter its login and Cora reads its probes, sockets, dosers and level sensors read-only. Nothing about a mini can be controlled yet.

Controls stay off until you turn on **Allow control from Cora (Beta)** on the device's page. It's off by default. Once it's on, a socket can be set to **Always on**, **Always off**, or **Back to automatic**, and a setpoint such as temperature or pH shows its allowed range and refuses a value outside it. Both kinds of change are saved on the controller itself and stay there even if Cora later loses touch with it. A change that looks like it touches a heater or return pump asks you to confirm twice.

If a doser's container is running low, Cora warns you the same way it does for other consumables. The default is 20% full, and you can change it from the doser's rule in the [Alert Center](/help/mobile-alerts).

If the controller won't take a change, its GHL API is probably switched off. GHL turns this off after every firmware update; turn it back on from **System → GHL API** in GHL Control Center or GHL Connect. [Troubleshooting](/help/troubleshooting) has the rest.

## HYDROS

:::note HYDROS support is in beta
We're still testing and developing HYDROS support. Some readings or controls may not work yet, and what you see here may change between updates.
:::

HYDROS is the only integration that reaches its controller through the cloud, so it works even when Cora Max is on a different network than the controller. Link it from **Settings → [your tank] → HYDROS (Beta)**.

In the HYDROS app, create a device key for the provider **cora-iq**, choosing **Read** for readings only or **Write** to also control it. Paste the key in, tap **Validate**, pick the tank, then **Save**. The last 33 days of its history are imported once it's linked.

Reading and controlling it works the same as on your phone; see [Controlling your equipment](/help/mobile-device-control) for outputs, modes, dosing heads and tester commands, and for the per-head dose limits.

## Schedules

You can write Jecod pump day programs at the wall as well as on your phone. The editor is the same, with a day graph, a list of periods and a row of actions. More about this in [Scheduling equipment](/help/mobile-schedules).

You can view a Maxspect gyre's schedule *(beta)* here, but you can't save it. Set it in the Maxspect app.

## Outlets

You can also reach outlets from the **Outlets & Feed** drawer at the bottom of the dashboard. It lists the outlets turned on for this dashboard (or all of them, if you haven't picked any). More about this in [Outlets and controls](/help/max-controls).

DŌS heads never show up in the outlet list, so you can't switch one on there and leave it running. Dose from the head's own page. A large Apex with several modules shows all of its outlets and probes.

## Consumables

You set refill thresholds (reagent, containers, reservoirs) on the device's own page here, the same as on your phone. More about this in [Consumables](/help/mobile-consumables).

## Logging and calculating at the tank

Two things are often easier at the wall than on a phone.

- **Log parameters** lets you type test results on the on-screen keyboard. It's in the tank menu.
- **Dose calculator** works out a correction from the tank's volume and your product strengths. Open it from a parameter's page. It uses the same volume and product strengths as your phone, so a dose worked out here matches one worked out there. More about this in [Dosing](/help/mobile-dosing).

## On a second Cora Max

When more than one Cora Max shows a tank, one of them reads that tank's equipment. The device pages call it the Cora Max at the tank. The others can still open the device pages, and a status tag reading **Cloud** means you're on one of them. They show what the Cora Max at the tank last read and how long ago. Each command goes through Cora Cloud to the Cora Max at the tank, which carries it out.

A few things only work on the Cora Max at the tank.

- **Measure to dose** and **Re-measure** only show up there. Once a head is measured, **Dose now** works from any Cora Max.
- You can change a Jecod schedule from another Cora Max only if the Cora Max at the tank has read the pump in the last hour, and never for a pump that only talks over Bluetooth. One **Apply to the pump** from there sends at most 12 changes, so send a bigger edit in parts.

## What was changed, and by what

Every action is logged along with what caused it. More about this in [Activity and timeline](/help/mobile-activity).
