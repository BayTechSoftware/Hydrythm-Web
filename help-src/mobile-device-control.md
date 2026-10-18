---
title: Controlling your equipment
description: Open a device's page to see its live state and switch outlets, pumps, dosing heads and testers, brand by brand.
section: Cora Mobile
reviewed: 2026-10-18
order: 13
group: Equipment
twin: max-device-control
---

Use a device's own page to see its live state and change what it's doing. Open it from **Devices** → tap the device, or tap its tile on the dashboard.

![A ReefATO+ page in Cora Mobile](img/mobile-device-detail.webp "Status, today's readings and the water level, then leak, fills and probe calibration.")

Every device page is laid out the same way. The name and details are at the top, then a row of live readings, any state the device reports, and its controls. The bell in the title bar sets alert thresholds for that device, as described in [Consumables](/help/mobile-consumables). How to add a device in the first place is in [Connecting your equipment](/help/mobile-connections).

Jump to your equipment: [Neptune Apex](#neptune-apex) · [Trident](#trident) · [DŌS](#dos) · [Red Sea](#red-sea) · [ReefDose](#reefdose) · [ReefRun](#reefrun) · [ReefMat](#reefmat) · [ReefATO+](#reefato) · [Doser alerts](#doser-alerts) · [Jecod](#jecod) · [AquaWiz](#aquawiz)

:::warning These controls act on live equipment
There's no preview and no undo. Some controls ask you to confirm first.
:::

## What happens when you send a command {#what-happens-when-you-send-a-command}

A command doesn't always go through. Cora tells you which of four things happened:

| Outcome | Means |
|---|---|
| **Confirmed** | The equipment accepted the change and reported its new state |
| **Unconfirmed** | The command went out, but nothing reported back. **It means "we don't know". It doesn't mean it worked.** Check the device's own state |
| **Refused** | Something turned it down (a safety rule, a lock or the equipment itself), or no Cora device picked it up in time. It was cancelled and nothing ran |
| **No change** | The equipment was already set the way you asked |

Every outcome is recorded in [Activity](/help/mobile-activity), along with what caused it.

Without a Cora Max at the tank, Neptune Apex, Red Sea and Jecod equipment only works locally: your phone has to be on the same network (or in Bluetooth range) to send a command. With a Cora Max at the tank, Cora Mobile sends it through that Cora Max, even when you're away from home.

## Neptune Apex {#neptune-apex}

![An Apex page in Cora Mobile, showing its status, its Trident and DŌS modules, Parameter Mapping and the tank it serves](img/mobile-apex.webp "The Apex page: Status, Modules, Parameter Mapping and Tanks.")

The Apex page shows the controller's status, then **Modules**, **Parameter Mapping** and **Tanks**.

- **Modules** lists each fitted Trident and DŌS. Tap one to open its own page.
- **Parameter Mapping** is where you choose what each probe feeds. Probes report into Cora as sources, and you can put them on a dashboard. See [Parameter Mapping and probes](/help/mobile-probes).
- **Tanks** shows which tanks the Apex serves. Tap **Change** to edit them.
- **Outlets** switch between **Auto**, **Off** and **On** from an **Outlet** widget on the dashboard. Auto hands control back to your Apex programming. See [Widget reference](/help/mobile-widgets#outlet).

Your Apex keeps running its own programming. Cora only changes an outlet when you ask.

## Trident {#trident}

The Trident page shows the current test state and the reagent and waste-water levels. You can start a test from here.

You can also set an alert for remaining tests and for the waste bottle, so Cora warns you before the reagent runs out or the bottle fills. See [Consumables](/help/mobile-consumables).

## DŌS {#dos}

![A DŌS page that says the DŌS is not answering on the AquaBus, with its last runway, today's dose and daily plan, then the Alerts row](img/mobile-dos.webp "A DŌS that is off the AquaBus: the page shows its last known figures, a Needs attention card and the Alerts row.")

A DŌS QD works exactly like a DŌS, and everything here applies to both. When a Cora Max reads your Apex, dosing heads show up on the DŌS page. They never appear in the outlet list.

Each dosing head shows what it's dosing, its schedule, what it has dosed today and how much is left in the container. It also shows the **runway**, which is how many days that will last at the current rate.

If the DŌS stops answering on the AquaBus, its page shows **Off the bus** and a **Needs attention** card. The figures on the page are then the last it reported, not what it's doing now. Check the module's AquaBus cable and the Apex.

For each head you can:

- **Pause** and **Resume** its schedule
- **Fill**, to tell Cora the container is full again or set how much is in it (**Total Volume** is the container's size, **Volume Remaining** is what's in it now, and **Full** sets one to the other)
- **Dose now**, for a measured dose by hand

:::note Edit schedules in Apex Fusion
Cora shows the schedule and tracks what's been dosed, but it doesn't change the schedule. You edit the schedule, dose rate and number of doses in the Apex Fusion app. Pausing, filling and dosing by hand all work here.
:::

:::note Measure a head before you dose by hand
Cora won't dose a head by hand until the head has been measured. **Measure to dose** and **Re-measure** are on the Cora Max that doses for the tank. Cora runs the head for twenty seconds, you measure what came out, and Cora works out the head's real rate. One measurement works for every Cora Max and Cora Mobile. Measure each head once, and again after you change its tubing.
:::

:::warning A DŌS keeps dosing when its container is empty
The unit has no level sensor and won't stop on its own. Set a refill alert for each head under **Alerts** on the DŌS page, so Cora warns you before the container runs dry. See [Doser alerts](#doser-alerts).
:::

### What each head is used for {#dos-head-use}

Give each head a **use type** so Cora knows what it does and talks about it correctly. The choices are **Supplement**, **Water change: new saltwater in**, **Water change: old water out**, **Kalkwasser**, **Calcium reactor**, **Food**, **Top-off** and **Other**. Set it under **Used for** in the head's settings.

The two water-change use types go in **pairs**. Set one head's **Paired head** to the head that moves water the other way, and Cora treats the two as one water-change pair.

A container can be up to 1,000 L, for every use type. The Apex itself only counts up to 150 L, so above that Cora tracks the container itself from what the head doses. Enter the **Total Volume** when you set it up. Cora also resets the Apex's own counter now and then, and Activity shows that as *Reset the Apex's own counter to 150 L*.

Each head also has a **Largest dose by hand** limit, so a typo can't turn a manual dose into something far bigger than you meant. Large hand doses only become available after the head's rate has been measured against a real test at the tank, and after you turn on **Large doses** in the head's settings. It's off by default. Turn it on only after you've watched the first large dose run at the tank.

## Red Sea ReefBeat {#red-sea}

Each Red Sea unit has a page that fits what it does:

| Unit | Page shows | You can |
|---|---|---|
| [ReefDose](#reefdose) | Each head, its container and what it has dosed | Dose, change the daily dose, edit the **Dosing plan** |
| [ReefRun](#reefrun) | Return and skimmer pump speed and state | Change speed, switch a pump |
| [ReefMat](#reefmat) | Remaining roll, in days and metres | Advance the mat, set **ReefMat settings**, register a new roll |
| [ReefATO+](#reefato) | Reservoir level and top-off activity | Set a reservoir alert |



When you're away from the unit's network, Cora Mobile sends Red Sea commands through a Cora Max on the tank. If no Cora Max can do it, the page says so and nothing is sent.

## ReefDose {#reefdose}

![A ReefDose 4 page in Cora Mobile](img/mobile-reefdose.webp "Status, heads and today's total, Use doser for consumption, then each dosing head.")

For each head you can set **Dose per day** and **Remaining in bottle**, run **Dose now**, and **Activate schedule**. Refill alerts are set per head with the bell, as described in [Doser alerts](#doser-alerts).

The **Dosing** section shows **Upcoming doses**, what each head has dosed today (**Dosed today so far**), and **Dosed per head** for the **Last 7 days** or its **Lifetime**. Cora reads this while a Cora Max or your phone is on your home network.

### Editing a dosing plan {#reefdose-plan}

Tap the calendar icon on a ReefDose page to open the **Dosing plan**.

A plan is a daily total, split into up to four time windows. Each window has a start and end time, how many doses it should deliver, and a speed: **Whisper**, **Regular** or **Quick**. Add and remove windows, then save. Cora shows you what you're about to send and asks you to confirm before it replaces the head's whole plan.

The editor reads the plan that's already on the unit first, so you're editing the real one, not a blank form.

## ReefRun {#reefrun}

ReefRun controls return and skimmer pumps. It isn't a wave pump. You can change a pump's speed, switch it on or off, and adjust skimmer settings.


## ReefMat {#reefmat}

The ReefMat page shows how much roll is left, in days and metres. Tap **Advance now** to move the mat on by hand. Cora asks **Advance the mat now?** first. You can also set a refill alert for the roll.

Tap the gear for **ReefMat settings**:

- **Scheduled advance** turns on a fixed-time advance, separate from the auto-advance sensor already on the page. Turn it on and set how often, and how far each advance moves the mat.
- **ReefMat model** and **Motor position** (**Left** or **Right**) tell Cora which unit and orientation you have.

After you load a new roll, tell Cora with **New roll**: its thickness, and its outer diameter if you know it. **Advance now** only moves the mat you already have loaded.

## ReefATO+ {#reefato}

The ReefATO+ page shows the reservoir level and recent top-offs. Set a reservoir alert with the bell. Cora estimates how many days the reservoir has left from recent top-off use, and you can ask the Assistant about it too.

## When a Red Sea unit stops itself {#red-sea-stops}

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

Some of these ask you to confirm first. Away from the unit's network they go through a Cora Max on the tank, as described in [Red Sea ReefBeat](#red-sea).

## Doser alerts {#doser-alerts}

A DŌS and a ReefDose keep their alerts on their own page. The **Rules** tab of the [Alert Center](/help/mobile-alerts) has one row per doser that opens it, and a doser alert's **Open doser** button brings you here too.

On a DŌS page, tap the **Alerts** card (or the bell in the title bar). The sheet lists every head, and for each one you can set:

- *[head] · days left*, for example *Iodine · days left*: you get an alert below this many days of supply
- *[head] · remaining*: you get an alert below this much left in the container
- **Waste container space left**, for a head that takes old water out: you get an alert when the waste container is getting full
- **Missed dose alerts**: a switch that tells you when the head misses a scheduled dose

Each threshold has its own switch, so you can turn one off and keep its value. Tap **Save** when you're done.

On a ReefDose page, tap the bell in the title bar. Each head has its own days-left threshold and switch.

Defaults and other consumables are in [Consumables](/help/mobile-consumables).

## Jecod / Jebao pumps {#jecod}

The pump page shows the current wave pattern (mode) and intensity, and you can change both. Its status sits in the title row, next to the pump's name. A switch with **Same all day** and **Schedule** marks the one that is running with *· running*, and the page opens on it. Building a schedule, and copying, saving or sharing it, is in [Scheduling equipment](/help/mobile-schedules).

If the pump is part of a group, the page shows its role, such as **Leads the group**, **Follows: in step** or **Follows: alternating**.

### Feeding pause {#jecod-feeding}

Start a feeding pause from **Feeding** on the pump's page: tap **5**, **10**, **15** or **30** min. Some pumps end the pause by themselves, and the page says *The pump ends this itself.*

:::warning Keep the pump's page open during a feeding pause
Some pumps don't end a feed by themselves, and the page says so. For those, and for any pump on a schedule, Cora Mobile brings the wave pattern and the schedule back only while the pump's page stays open. If you leave the page, the pump stays stopped in feed mode, or stays off its schedule, until you change it again or tap **Schedule**.
:::

If your household has a Cora Max, it ends the feed and puts the pump back on its program when the time is up, even if Cora Mobile is closed. The warning above then matters only when there is no Cora Max.

A Bluetooth pump has to be in range of your phone to start a feed, and a network pump has to be on your network.

### Fault checks {#jecod-fault-checks}

**Fault checks** sets how often Cora re-reads the pump so it can warn you about a fault, such as a jammed pump or one running dry. If you set it to off, those warnings stop for that pump. Fault checks need a Cora Max on the tank. Your choice is saved and the checks start once one is added. **Use this for every pump on this tank** copies the setting to all of them.

## AquaWiz {#aquawiz}

The AquaWiz card shows your alkalinity readings, and pH if your unit reports it. It also shows your target KH, your dose strength and, for a unit with dosing set up, its maximum dose per hour and how much alkalinity supplement is left in the container. These come straight from your AquaWiz settings, so change them in the AquaWiz app. Cora can't control an AquaWiz.

Under the readings the card shows when the last one was measured (*Measured 2:00 PM*, for example) and where it came from: **Hourly from your Cora Max** or **From AquaWiz cloud, every 12 hours**. It also shows the **pH change**. Opening the page asks for a fresh reading, and **Read now** asks again, at most once every 15 minutes. If a reading hasn't changed, that's normal: the unit only measures now and then.

When a Cora Max reads the unit every hour, the card also shows its pump, pH probe and water box level, and Cora alerts you when the pump reports a fault, the pH probe has failed or is near the end of its life, or the water box level stays low or high for over an hour.

If your unit tracks its container, Cora warns you when the supplement is running low, at 100 mL by default. Change it from its rule in the [Alert Center](/help/mobile-alerts).


## What happens after you change something {#what-happens-after-you-change-something}

Every change is recorded in [Activity](/help/mobile-activity), with the surface it came from. If a device doesn't accept a change, that's recorded there too.
