---
title: EcoTech lights, pumps and dosers
description: Link EcoTech Radion lights, VorTech pumps and Versa dosers to Cora over Bluetooth, and what you can do with them.
section: Cora Mobile
reviewed: 2026-10-12
order: 36
group: Equipment
---

:::note Beta
**Beta.** EcoTech is in Beta and only open to Beta users. If you are not a Beta user you will not see it in **Add device**. To ask for Beta access, contact [support](/support.html).
:::

Cora connects to EcoTech Radion lights, VorTech pumps and Versa dosers. The same **EcoTech** row also finds the AquaIllumination, NYOS Quantum, Nero and Orbit devices that sit on the same Bluetooth network.

## What you need

- A Cora Max in the tank. It does the reading and sends your commands to the equipment over Bluetooth. Without one, the **EcoTech** row shows **Requires Cora Max** and stays greyed out.
- Your phone's Bluetooth turned on, with Bluetooth permission for Cora. Cora asks for it when you scan.
- Equipment that's powered on and in range of the Cora Max.

## Linking it

1. Go to **Devices → Add Device → EcoTech**.
2. Cora scans for nearby lights, pumps and dosers. Lights already in use by the Mobius app may not show.
3. Equipment on the same Bluetooth network is grouped as one **Mobius tank**. Tap **Link to…** and pick the Cora tank it belongs to.
4. Name the group when Cora asks, and it's linked.

If nothing is found, check Bluetooth is on and the equipment is powered, then tap **Scan again**.

## Radion lights

The light's page has a schedule editor and quick scenes (**Schedule**, **Storm**, **Clouds**, **Colours**, **Feed**, **Off**). You can also set acclimation, the fan, the lunar cycle and the clock.

In the schedule editor, **Preview day** plays the day through at speed so you can see it without waiting. **Stop preview** puts the lights back. **Undo** and **Redo** step through your edits, and **Start from…** begins a new schedule from a copy of an existing one.

Cora reads the lights every so often. Under **Reading**, **Read the lights every** sets how often. Less often is gentler on the lights. Opening the page, **Read now** and every command still read at once.

## VorTech pumps

A VorTech tile shows the pump's mode and speed. You can change the mode and **Speed**, edit its schedule, and start **Feed** for a few minutes. Feed slows every VorTech on the tank and they return to their schedules when it ends. Each mode has a short description next to it, from steady flow to reef-crest surges, tidal swells and pulses. A pump only offers the modes it supports.

## Versa dosers

A Versa page shows its container, doses and limits. You can set the container size, tap **Mark as refilled**, run **Dose now**, **Pause** dosing until midnight, and edit the schedule. Cora keeps a dose history for each head.

:::warning Not proven on hardware yet
Commands to VorTech pumps and Versa dosers haven't been proven on real hardware yet. Reading works. Check the equipment itself the first few times you change something, and tell us what you see from [Getting help](/help/mobile-support).
:::

## Alerts

Cora treats an EcoTech device as quiet after three missed readings of its own reading interval. A light-only network reads every 30 minutes by default, so that takes at least 90 minutes. See [Alerts and thresholds](/help/mobile-alerts).

## On Cora Max

The same equipment has its own pages on the wall screen. More in [Controlling equipment from Cora Max](/help/max-device-control).
