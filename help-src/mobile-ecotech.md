---
title: EcoTech lights, pumps and dosers
description: Link EcoTech Radion lights, VorTech pumps and Versa dosers to Cora over Bluetooth, and what you can do with them.
section: Cora Mobile
reviewed: 2026-10-13
order: 18
group: Equipment
---

:::note Beta
**Beta.** EcoTech is in Beta and only open to Beta users. If you are not a Beta user you will not see it in **Add device**. To ask for Beta access, contact [support](/support.html).
:::

Use this page to link EcoTech Radion lights, VorTech pumps and Versa dosers to Cora and control them. Start from **Devices → Add Device → EcoTech**. The same row also finds the AquaIllumination, NYOS Quantum, Nero and Orbit devices that sit on the same Bluetooth network.

## What you need {#what-you-need}

- A Cora Max in the tank. It does the reading and sends your commands to the equipment over Bluetooth. Without one, the **EcoTech** row shows **Requires Cora Max** and stays greyed out.
- Your phone's Bluetooth turned on, with Bluetooth permission for Cora. Cora asks for it when you scan.
- Equipment that's powered on and in range of the Cora Max.

## Linking it {#linking-it}

1. Go to **Devices → Add Device → EcoTech**.
2. Cora scans for nearby lights, pumps and dosers. Lights already connected to EcoTech's own Mobius app may not show.
3. Equipment on the same Bluetooth network is grouped as one **Mobius tank**. Tap **Link to…** and pick the Cora tank it belongs to.
4. Name the group when Cora asks, and it's linked.

A device marked **Read-only** shows its readings, but Cora can't control it yet. Control for that model comes after it's been tested.

If the same Bluetooth network also has lights on another tank, and the two tanks are read by different Cora Max units, Cora says **Read by one Cora Max**. One Cora Max then reads the whole network for both tanks.

If nothing is found, check Bluetooth is on and the equipment is powered, then tap **Scan again**.

## Radion lights {#radion}

![A Radion page in Cora Mobile](img/mobile-radion.webp "Status, the lights on this network (all of them or one), then intensity and each colour channel.")

The light's page has a schedule editor and quick scenes (**Schedule**, **Storm**, **Clouds**, **Colours**, **Feed**, **Off**). You can also set acclimation, the fan, the lunar cycle and the clock.

In the schedule editor, **Preview day** plays the day through at speed so you can see it without waiting. **Stop preview** puts the lights back. **Undo** and **Redo** step through your edits, and **Start from…** begins a new schedule from a copy of an existing one.

Cora reads the lights every so often. In **Radion settings**, under **Reading**, **Read the lights every** sets how often. Less often is gentler on the lights. Opening the page and every command still read the lights immediately.

**Radion settings** also has:

- **Set clock**, to set the light's clock.
- **Acclimation**, for new corals: the whole schedule ramps up over the days you set. Turning it on starts it again from the lower level.
- **Alerts**: **Light stops answering**, **Fault: heat, fan or LED**, **Clock off by 5 min** and **LED temperature**. Turn on the ones you want.

## VorTech pumps {#vortech}

A VorTech tile shows the pump's mode and speed. You can change the mode and **Speed**, edit its schedule, and start **Feed** for a few minutes. Feed slows every VorTech on the tank and they return to their schedules when it ends. Each mode has a short description next to it, from steady flow to reef-crest surges, tidal swells and pulses. A pump only offers the modes it supports.

## Versa dosers {#versa}

A Versa page shows its container, doses and limits. You can set the container size, tap **Mark as refilled**, run **Dose now**, **Pause** dosing until midnight, and edit the schedule. Cora keeps a dose history for each head. The bell sets refill alerts in days left or how full the container is, as described in [Consumables](/help/mobile-consumables).

:::warning Not proven on hardware yet
Commands to VorTech pumps and Versa dosers haven't been proven on real hardware yet. Reading works. Check the equipment itself the first few times you change something, and tell us what you see from [Reporting a problem](/help/mobile-support).
:::

## Alerts {#alerts}

Cora treats an EcoTech device as quiet after three missed readings of its own reading interval. A light-only network reads every 30 minutes by default, so that takes at least 90 minutes. See [Alerts and thresholds](/help/mobile-alerts). Radion lights also have their own alerts in **Radion settings**, described above.

## On Cora Max {#on-cora-max}

The same equipment has its own pages on the wall screen. More in [Controlling equipment from Cora Max](/help/max-device-control).
