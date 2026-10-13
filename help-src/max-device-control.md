---
title: Controlling equipment from Cora Max
description: Device pages on Cora Max for Neptune Apex, Trident and DŌS, Red Sea ReefBeat, Jecod, AquaWiz and the Beta brands, by brand.
section: Cora Max
reviewed: 2026-10-13
order: 6
group: Equipment
twin: mobile-device-control
---

This page covers what you can see and do on each device's page on Cora Max, brand by brand. Cora Max reaches the same equipment as your phone. Open a device page from the devices icon in the top bar, from **Settings → Devices**, or by tapping a device tile on the dashboard.

![An Apex page on Cora Max with its feed buttons and outlets](img/max-device-control.webp "Feed A to D and Cancel, then the outlets, laid out for a wall screen.")

:::warning These controls act on live equipment
There's no preview and no undo. A command goes out the moment you tap, but sending it doesn't mean it's done. It comes back **Confirmed**, **Unconfirmed**, **Refused** or **No change**, and you can see which in [Activity](/help/max-activity).
:::

You add, assign and remove equipment on your phone. Cora Max shows it once your account has it. See [Connecting your equipment](/help/mobile-connections).

## What has a page {#what-has-a-page}

| Device | Shows |
|---|---|
| **Neptune Apex** | Probes and outlets, and you can switch each outlet |
| **Trident** | Test state, reagent and waste levels, and a button to start a test |
| **DŌS**, including the DŌS QD | Each head's dosing, schedule, runway and container volume (with pause, fill, dose now and a one-time twenty-second measure) |
| **Red Sea ReefBeat** | Whatever the unit has: dosing heads, reservoir, roller days, pump mode, plus a full ReefDose plan and ReefRun program editor and ReefMat settings *(Beta)* |
| **Red Sea ReefControl**, **ReefControl Power**, **ReefWave**, **ReefLED** *(Beta)* | ReefControl's probes. ReefControl Power's sockets as outlets, on or off, no automatic mode yet. ReefWave and ReefLED, view only |
| **Jecod** | Pump mode and intensity, and its day program |
| **AquaWiz** | No page of its own. It's listed in **Devices**, and its readings go on the dashboard |
| **Maxspect** *(Beta)* | Mode and speed for **Gyre A** and **Gyre B**, **Pump health** (cleaning countdown, head A current, fitted heads, firmware), and its schedule, view only |
| **GHL ProfiLux / Mitras** *(Beta)* | Probes, sockets, dosers, level sensors and, on the Director models, KH and ion test results |
| **HYDROS** *(Beta)* | Whatever its device key reports: inputs, and with a write key, outputs, modes, dosing heads and tester commands |
| **Focustronic** *(Beta)* | Status, last test, pumps and vials, plus **Measure now**, **Dose now** or **Test now** depending on the unit |
| **EcoTech** *(Beta)* | Radion lights, VorTech pumps and Versa dosers, each with its own page. Commands to VorTech and Versa aren't proven on hardware yet |
| **Inkbird** *(Beta)* | Room air readings, read only |
| **Camera** *(Beta)* | A picture from your camera, as a tile on the dashboard or on its own page, with Skimmer Watch on paid plans |

:::note Beta
**Beta.** Maxspect, GHL, HYDROS, Focustronic, EcoTech, Inkbird and cameras are in Beta and only open to Beta users. If you are not a Beta user you will not see them in **Add device**. To ask for Beta access, contact [support](/support.html). Some readings or controls may not work yet.
:::

Most device pages have a pencil to rename the device. The new name shows on your phone too. More in [Devices and device health](/help/max-devices).

## Neptune Apex {#neptune-apex}

The Apex page lists your probes and outlets, with your feed cycles at the top. Each outlet switches between **Auto**, **Off** and **On**, and padlocked outlets ask you to confirm. How the three states and feed mode work is in [Outlets and controls](/help/max-controls).

You can also reach outlets from the **Outlets & Feed** drawer at the bottom of the dashboard. It lists the outlets turned on for this dashboard (or all of them, if you haven't picked any).

A large Apex with several modules shows all of its outlets and probes. DŌS heads never show up in the outlet list, so you can't switch one on there and leave it running. Dose from the head's own page.

### Trident {#trident}

The Trident page shows the test state and the reagent and waste levels. You can start a test from here, and set a refill alert with **Alert settings**.

## DŌS heads {#dos-heads}

You have to measure a DŌS head once before Cora will dose with it by hand. **Measure to dose** runs the head for twenty seconds into a measuring container, and you enter how much came out. Cora keeps one measurement per head and uses the newest, whichever Cora Max took it. The head's page shows where and when it was measured.

After a manual dose, a head you'd set to Off in Apex Fusion stays Off. Any other head goes back to Auto.

A DŌS has no level sensor and keeps dosing from an empty container. Set a refill alert with **Alert settings** on the DŌS page. More in [Doser alerts](/help/mobile-device-control#doser-alerts).

### What a head is used for {#what-a-head-is-used-for}

In a head's settings sheet you can set its **use type**. The options are **Supplement**, **Water change: new saltwater in**, **Water change: old water out**, **Kalkwasser**, **Calcium reactor**, **Food** or **Top-off**, and **Other**. The use type changes two things.

- How big a container it can track. Every use type can track a container of up to 1,000 litres. Above the Apex's own 150 litre counter, Cora tracks the volume itself, and Cora resets the Apex counter every 100 litres.
- Whether it can take a large dose by hand. Supplement and Food heads keep today's small, careful ceiling. Every other use type can have its own **Largest dose by hand** limit, up to a hard ceiling of 10 litres, and its own **daily limit for automations and the Assistant**. A large hand dose also needs **Large doses (Beta)** turned on in the head's settings, off by default. Turn it on only after you've watched the first large dose run at the tank.

You can link a water-change pair (new saltwater in, old water out) as a **Paired head** and set a **Balance warning above** amount. If the two heads' totals for the day drift apart by more than that, Cora warns you. A pair that's out of balance usually means one side isn't pumping as it should.

### If a large dose is interrupted {#if-a-large-dose-is-interrupted}

A large dose changes what the head is doing on the Apex for a while, then puts its normal schedule back. If the connection drops partway through, Cora Max shows a banner on that head's page: *"A large dose on [head] did not finish cleanly. Cora keeps trying to put its program back; check it in Apex Fusion."*

Check the head in Apex Fusion yourself, then tap **I checked the head in Fusion** to clear the banner. Only do this once you've confirmed that the head's own schedule is running, not Cora's dosing program.

If the banner won't clear, or keeps coming back, have a look at [Troubleshooting](/help/troubleshooting).

## Red Sea ReefBeat {#red-sea}

Each Red Sea unit has a page that fits what it does: ReefDose heads and containers, the ReefATO+ reservoir, ReefMat roll days and ReefRun pump speeds. Supply alerts for ReefDose heads, the ReefATO+ reservoir and the ReefMat roll are set with **Alert settings** on the unit's page.

If a Red Sea unit stops itself, its page tells you what's wrong and puts the fix right next to it. That's **Resume**, **Clear emergency**, **Sensor cleaned**, **I already loaded a new roll**, or **Reset** for a dosing head.

A ReefDose plan, a ReefRun speed program and ReefMat's scheduled advance, model, position and New roll all work the same way here as on your phone. [Controlling your equipment](/help/mobile-device-control) has the detail.

ReefControl, ReefControl Power, ReefWave and ReefLED carry *(Beta)* in their name but are open to everyone. ReefControl shows its probes. ReefControl Power's sockets show up as outlets, on or off only. ReefWave and ReefLED are view only for now.

## Jecod {#jecod}

The Jecod page shows the pump's mode and intensity, and you can change both.

You can write Jecod pump day programs at the wall as well as on your phone. The editor is the same, with a day graph, a list of periods and a row of actions. More in [Scheduling equipment](/help/mobile-schedules).

## AquaWiz {#aquawiz}

An AquaWiz KH Controller has no page of its own on Cora Max. It's listed in **Devices**, where you can rename it, and its readings show on the dashboard like any other source. Set it up and manage it on your phone, see [Connecting your equipment](/help/mobile-connections).

## Maxspect {#maxspect}

:::note Beta
**Beta.** Maxspect is in Beta and only open to Beta users. If you are not a Beta user you will not see it in **Add device**. To ask for Beta access, contact [support](/support.html). Some readings or controls may not work yet.
:::

The Maxspect page shows the mode and speed of **Gyre A** and **Gyre B** and its **Pump health**. You can view a gyre's schedule here, but you can't save it. Set it in the Maxspect app.

## GHL ProfiLux and Mitras {#ghl}

:::note Beta
**Beta.** GHL is in Beta and only open to Beta users. If you are not a Beta user you will not see it in **Add device**. To ask for Beta access, contact [support](/support.html). Some readings or controls may not work yet.
:::

Connect a GHL controller from your phone: **Devices → Add Device → GHL**. [Connecting your equipment](/help/mobile-connections) has the steps. Cora Max shows and controls it once a Cora Max on its network has read it, but setup itself happens on the phone.

A ProfiLux mini reads its probes, sockets, dosers and level sensors. With **Allow control from Cora (Beta)** on, a mini can also switch its sockets, the same way as any other GHL controller. Everything else, such as setpoints and feed pause, needs a ProfiLux 3, 4 or Mitras.

Controls stay off until you turn on **Allow control from Cora (Beta)** on the device's page. It's off by default. Once it's on, a socket can be set to **Always on**, **Always off**, or **Back to automatic**, and a setpoint such as temperature or pH shows its allowed range and refuses a value outside it. Both kinds of change are saved on the controller itself and stay there even if Cora later loses touch with it. A change that looks like it touches a heater or return pump asks you to confirm twice.

If a doser's container is running low, Cora warns you the same way it does for other consumables. The default is 20% full, and you can change it from the doser's rule in the [Alert Center](/help/mobile-alerts).

If the controller won't take a change, its GHL API is probably switched off. GHL turns this off after every firmware update. Turn it back on from **System → GHL API** in GHL Control Center or GHL Connect. [Troubleshooting](/help/troubleshooting) has the rest.

## HYDROS {#hydros}

:::note Beta
**Beta.** HYDROS is in Beta and only open to Beta users. If you are not a Beta user you will not see it in **Add device**. To ask for Beta access, contact [support](/support.html). Some readings or controls may not work yet.
:::

HYDROS reaches its controller through the HYDROS cloud, so it works even when Cora Max is on a different network than the controller. It's set up only from your phone: **Devices → Add Device → HYDROS**. [Connecting your equipment](/help/mobile-connections) has the steps.

Reading and controlling it works the same as on your phone. See [Controlling your equipment](/help/mobile-device-control) for outputs, modes, dosing heads and tester commands, and for the per-head dose limits.

## Focustronic {#focustronic}

:::note Beta
**Beta.** Focustronic is in Beta and only open to Beta users. If you are not a Beta user you will not see it in **Add device**. To ask for Beta access, contact [support](/support.html). Some readings or controls may not work yet.
:::

The Focustronic page shows the unit's status, its last test, and its pumps and vials. Under **Controls**:

- An Alkatronic has **Measure now**.
- A Dosetronic has **Dose now** for each pump. Enter the amount, up to 500 mL at once, tap **Review**, then confirm. A dose can't be undone, and Cora never retries it.
- A Mastertronic has a test profile to pick and **Test now**.

These commands go through Focustronic's servers, which Cora doesn't control. Set the unit up on your phone, see [Connecting your equipment](/help/mobile-connections).

## EcoTech, Inkbird and cameras {#ecotech-inkbird-and-cameras}

:::note Beta
**Beta.** EcoTech, Inkbird and cameras are in Beta and only open to Beta users. If you are not a Beta user you will not see them in **Add device**. To ask for Beta access, contact [support](/support.html).
:::

You link these from your phone, and a Cora Max on the tank does the reading.

### EcoTech {#ecotech}

Radion lights, VorTech pumps and Versa dosers each have their own page, with an **Alert settings** button for their supplies. [EcoTech lights, pumps and dosers](/help/mobile-ecotech) has the detail.

### Inkbird {#inkbird}

An Inkbird room air monitor shows its readings and nothing more.

### Cameras and Skimmer Watch {#cameras}

To show a camera on the wall, add a **Camera** tile in the [dashboard editor](/help/max-dashboard-editing). Tap the tile to open the camera full screen. Its buttons fade after a few seconds, and a tap brings them back.

With Skimmer Watch on (paid plans), the camera tile and the full-screen view show the cup level and how old it is, for example *Cup 42% · 5 min ago*. It turns amber within 10 points of your alert level and red at it. On the full-screen camera, **Alert at 80%** (or your level) opens **Skimmer cup alert**, where you set the level. You get one notification when the cup reaches it.

Setting up a camera and Skimmer Watch is covered in [Cameras and Skimmer Watch](/help/mobile-cameras).

## Consumables {#consumables}

You set refill thresholds (reagent, containers, reservoirs) on the device's own page here, the same as on your phone. More in [Consumables](/help/mobile-consumables).

## Logging and calculating at the tank {#logging-and-calculating-at-the-tank}

Two things are often easier at the wall than on a phone.

- **Log parameters** lets you type test results on the on-screen keyboard. It's in the tank menu.
- **Dose calculator** works out a correction from the tank's volume and your product strengths. Open it from a parameter's page. It uses the same volume and product strengths as your phone, so a dose worked out here matches one worked out there. More in [Dosing](/help/mobile-dosing).

## On a second Cora Max {#on-a-second-cora-max}

When more than one Cora Max shows a tank, one of them reads that tank's equipment. The device pages call it the Cora Max at the tank. The others can still open the device pages, and a status tag reading **Cloud** means you're on one of them. They show what the Cora Max at the tank last read and how long ago. Each command goes through Cora Cloud to the Cora Max at the tank, which carries it out.

A few things only work on the Cora Max at the tank.

- **Measure to dose** and **Re-measure** only show up there. Once a head is measured, **Dose now** works from any Cora Max.
- You can change a Jecod schedule from another Cora Max only if the Cora Max at the tank has read the pump in the last hour, and never for a pump that only talks over Bluetooth. One **Apply to the pump** from there sends at most 12 changes, so send a bigger edit in parts.

## What was changed, and by what {#what-was-changed-and-by-what}

Every action is logged along with what caused it. More in [Activity on Cora Max](/help/max-activity).
