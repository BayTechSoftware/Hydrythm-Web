---
title: Controlling equipment from Cora Max
description: Device pages on Cora Max for Neptune Apex, Trident and DŌS, Red Sea ReefBeat, Jecod and AquaWiz, by brand.
section: Cora Max
reviewed: 2026-10-18
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
| **Red Sea ReefBeat** | Whatever the unit has: dosing heads, reservoir, roller days, pump mode, plus a full ReefDose plan editor and ReefMat settings |
| **Jecod** | Pump mode and intensity, and its schedule |
| **AquaWiz** | No page of its own. It's listed in **Devices**, and its readings go on the dashboard |

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
- Whether it can take a large dose by hand. Supplement and Food heads keep today's small, careful ceiling. Every other use type can have its own **Largest dose by hand** limit, up to a hard ceiling of 10 litres, and its own **daily limit for automations and the Assistant**. A large hand dose also needs **Large doses** turned on in the head's settings, off by default. Turn it on only after you've watched the first large dose run at the tank.

You can link a water-change pair (new saltwater in, old water out) as a **Paired head** and set a **Balance warning above** amount. If the two heads' totals for the day drift apart by more than that, Cora warns you. A pair that's out of balance usually means one side isn't pumping as it should.

### If a large dose is interrupted {#if-a-large-dose-is-interrupted}

A large dose changes what the head is doing on the Apex for a while, then puts its normal schedule back. If the connection drops partway through, Cora Max shows a banner on that head's page: *"A large dose on [head] did not finish cleanly. Cora keeps trying to put its program back; check it in Apex Fusion."*

Check the head in Apex Fusion yourself, then tap **I checked the head in Fusion** to clear the banner. Only do this once you've confirmed that the head's own schedule is running, not Cora's dosing program.

If the banner won't clear, or keeps coming back, have a look at [Troubleshooting](/help/troubleshooting).

## Red Sea ReefBeat {#red-sea}

Each Red Sea unit has a page that fits what it does: ReefDose heads and containers, the ReefATO+ reservoir, ReefMat roll days and ReefRun pump speeds. Supply alerts for ReefDose heads, the ReefATO+ reservoir and the ReefMat roll are set with **Alert settings** on the unit's page.

If a Red Sea unit stops itself, its page tells you what's wrong and puts the fix right next to it. That's **Resume**, **Clear emergency**, **Sensor cleaned**, **I already loaded a new roll**, or **Reset** for a dosing head.

A ReefDose plan and ReefMat's scheduled advance, model, position and New roll all work the same way here as on your phone. [Controlling your equipment](/help/mobile-device-control) has the detail.


## Jecod {#jecod}

The Jecod page shows the pump's mode and intensity, and you can change both. Its status sits in the title row, next to the pump's name. The top bar holds the power switch, the pattern running now and **Feeding** with four pills: **5**, **10**, **15** and **30** min. Tap a pill to pause the pump for that long. Below the bar are two cards:

- **Same all day**: tap a setting to run it all day.
- **Schedule**: the day graph and the list of plans, with **now** on the current one. **Edit** opens the editor, and the ⋮ menu holds **Copy schedule to…**, **Save schedule as…** and **Saved schedules…**.

The card that is running has an outline and a **Running** chip. A Jecod pump has no **End feed** button. Every Jecod pump that can pause for feeding shows the **5**, **10**, **15** and **30** min pills. On a Jecod Pro the Feeding tile in the wave patterns does the same, for 10 minutes. Through a Cora Max that is away from the tank, a Jecod pump feeds for 10 minutes only. A pump that cannot feed right now shows the reason in one short line under the pills, and a long press shows the full sentence. A feed started from your phone is ended by Cora Max too: when the time is up, the pump returns to its program.

You can write Jecod pump schedules at the wall as well as on your phone. The editor is the same, with a day graph, a list of periods and a row of actions. More in [Scheduling equipment](/help/mobile-schedules).

## AquaWiz {#aquawiz}

An AquaWiz KH Controller has no page of its own on Cora Max. It's listed in **Devices**, where you can rename it, and its readings show on the dashboard like any other source. Set it up and manage it on your phone, see [Connecting your equipment](/help/mobile-connections).

### Hourly reading from Cora Max {#aquawiz-hourly}

AquaWiz lets Cora read its cloud only every 12 hours. To keep alkalinity current, the tank's main Cora Max also reads the controller directly, once an hour at ten to the hour:

- It joins the controller's own Wi-Fi for a few seconds, reads the latest result, and goes straight back to your home Wi-Fi. Cora Max is offline for about 4 seconds while it does this.
- Your home Wi-Fi password is never saved or sent anywhere by this.
- Only the tank's main Cora Max does it. A second Cora Max on the same tank doesn't.
- It waits while Cora Max is talking to you, updating, pairing or changing Wi-Fi, and tries again the next hour.
- The controller must be within Wi-Fi range of the Cora Max, and its firmware must offer local access. If two reads in a row fail, Cora Max stops trying for the rest of the day and the 12-hour cloud reading carries on.

A reading from Cora Max shows **Hourly from your Cora Max** on the phone's AquaWiz card. It also brings the pump, pH probe and water box alerts described in [Alerts](/help/mobile-alerts#equipment-faults).


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
