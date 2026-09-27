---
title: Controlling your equipment
description: Open a device's own page to see its live state and drive outlets, pumps, dosing heads and testers.
section: Cora Mobile
reviewed: 2026-09-27
order: 11
group: Equipment
---

Each piece of connected equipment has its own page in Cora. It shows the live state and whatever controls that device supports. Open one from the **Devices** tab.

![A device page](img/mobile-device-detail.webp "Live readings at the top, then the controls that device supports.")

Every device page is laid out the same way. The device's name and details are at the top, then a row of live readings, any state the device reports, and its controls. The bell in the title bar sets alert thresholds for that device, as described in [Consumables](/help/mobile-consumables).

:::warning These controls act on live equipment
There's no preview and no undo. Some controls ask you to confirm first.
:::

## What happens when you send a command

A command doesn't always go through. Cora tells you which of four things happened:

| Outcome | Means |
|---|---|
| **Confirmed** | The equipment accepted the change and reported its new state |
| **Unconfirmed** | The command went out, but nothing reported back. **It means "we don't know". It doesn't mean it worked.** Check the device's own state |
| **Refused** | Something turned it down (a safety rule, a lock or the equipment itself), or no Cora device picked it up in time. It was cancelled and nothing ran |
| **No change** | The equipment was already set the way you asked |

Every outcome is recorded in [Activity](/help/mobile-activity), along with what caused it.

## Neptune Apex

The Apex page lists your probes and outlets.

- **Probes** report into Cora as sources, and you can put them on a dashboard.
- **Outlets** switch between **Auto**, **Off** and **On**. Auto hands control back to your Apex programming.
- **Fitted modules**, such as Trident and DŌS, each have their own page.

## Trident

The Trident page shows the current test state and the reagent and waste-water levels. You can start a test from here.

You can also set an alert for remaining tests, so Cora warns you before the reagent runs out. See [Consumables](/help/mobile-consumables).

## DŌS

A DŌS QD works exactly like a DŌS, and everything here applies to both. When a Cora Max reads your Apex, dosing heads show up on the DŌS page. They never appear in the outlet list.

Each dosing head shows what it's dosing, its schedule, what it has dosed today and how much is left in the container. It also shows the **runway**, which is how many days that will last at the current rate.

For each head you can:

- **Pause** and **Resume** its schedule
- **Fill**, to tell Cora the container is full again or set how much is in it
- **Dose now**, for a measured dose by hand

:::note Edit schedules in Apex Fusion
Cora shows the schedule and tracks what's been dosed, but it doesn't change the schedule. You edit the schedule, dose rate and number of doses in the Apex Fusion app. Pausing, filling and dosing by hand all work here.
:::

:::note Measure a head before you dose by hand
Cora won't dose a head by hand until the head has been measured. **Measure to dose** and **Re-measure** are on the Cora Max that doses for the tank. Cora runs the head for twenty seconds, you measure what came out, and Cora works out the head's real rate. One measurement works for every Cora Max and Cora Mobile. Measure each head once, and again after you change its tubing.
:::

:::warning A DŌS keeps dosing when its container is empty
The unit has no level sensor and won't stop on its own. Set a refill alert from the head's page so Cora warns you before the container runs dry.
:::

### What each head is used for

Give each head a **use type** so Cora knows what it does and talks about it correctly. The choices are **Supplement**, **Water change: new saltwater in**, **Water change: old water out**, **Kalkwasser**, **Calcium reactor**, **Food**, **Top-off** and **Other**. Set it under **Used for** in the head's settings.

The two water-change use types go in **pairs**. Set one head's **Paired head** to the head that moves water the other way, and Cora treats the two as one water-change pair.

Each head also has a **Largest dose by hand** limit, so a typo can't turn a manual dose into something far bigger than you meant. Large hand doses only become available after the head's rate has been measured against a real test at the tank.

## Red Sea ReefBeat

Each unit has a page that fits what it does:

| Unit | Page shows | You can |
|---|---|---|
| **ReefDose** | Each head, its container and what it has dosed | For each head: **Dose per day**, **Remaining in bottle**, **Dose now** and **Activate schedule**. Set refill alerts per head |
| **ReefATO+** | Reservoir level and top-off activity | Set a reservoir alert |
| **ReefMat** | Remaining roll, in days and metres | Advance the roll, set a refill alert |
| **ReefRun** | Return and skimmer pump speed and state | Change speed, switch a pump, adjust skimmer settings |

ReefRun controls return and skimmer pumps. It isn't a wave pump.

A unit can stop itself. A ReefRun pump does this when the skimmer cup fills, for example. When that happens, the page says why and offers the fix:

| Unit | The page says | Tap |
|---|---|---|
| ReefRun | Which pump stopped and why, for example *Full cup. Empty it, then resume.* | **Resume** |
| ReefRun or ReefMat | **Emergency stop** | **Clear emergency** |
| ReefMat | **Mat jammed**, **Installation error** or **Setup error** | **Resume** |
| ReefMat | *Load a new roll, then confirm it in Red Sea's app.* | **I already loaded a new roll** |
| ReefMat | **Sensor needs cleaning** | **Sensor cleaned** |
| ReefDose | **Head malfunction**, with the head's name | **Reset** |
| ReefATO+ | **Clear Fault** | **Resume** |

Some of these ask you to confirm first. When you're away from the unit's network, Cora Mobile sends them through a Cora Max on the tank. If no Cora Max can do it, the page says so and nothing is sent.

## Jecod pumps

The pump page shows the current mode and intensity, and you can change both.

You can also:

- Use **Copy schedule to…** to put this pump's schedule on another pump
- Use **Save schedule as…** and **Saved schedules…** to keep a schedule and apply it again later
- Use **Share this schedule** and **Paste a schedule code…** to move a schedule between systems as a short code

## Maxspect

:::note Maxspect support is in beta
We're still testing and developing Maxspect gyre support. Some controls may be limited, and what you see here may change between updates. If something doesn't work as described, let us know from [Getting help](/help/mobile-support).
:::

The gyre page shows whether the gyre is running, the wave pattern and speed of **Gyre A** and **Gyre B**, and when they were last read. From here you can:

- Switch the gyre on or off with the switch next to its state. Cora asks you to confirm first. Switching off stops both gyres and leaves the schedule alone.
- Tap **Change settings** to set each gyre's wave pattern and pump speed, plus the duration for patterns that have one, and whether the two gyres are linked. Cora lists what will change and asks you to confirm. Alternating is set in the Maxspect app, and a gyre running it keeps its ramps and hold times.
- Tap **Set program** if the program saved on the gyre can't be read. It sets both gyres so the gyre can start again.
- See the gyre's day program on the **Schedule** card. You can only view it here. Set the schedule in the Maxspect app.
- Check **Pump health**. It shows when the pump next needs cleaning (the pump counts this down itself), the current drawn by head A, which heads are fitted and the firmware. Tap **Read** to fetch it.

:::note How Cora Mobile reaches a gyre
If a Cora Max serves the tank, Cora Mobile goes through that Cora Max, even when you're away from home. **Change settings** then starts from that Cora Max's last reading. Otherwise your phone talks to the gyre directly and has to be on the gyre's network. Opening the page reads the gyre. If the page is showing an older stored reading, **Change settings** stays hidden until you tap refresh.
:::

## What happens after you change something

Every change is recorded in [Activity](/help/mobile-activity), with the surface it came from. If a device doesn't accept a change, that's recorded there too.
