---
title: Parameter Mapping and probes
description: See every device's readings in one list, choose which parameter each reading shows as and which device drives it, and record probe calibration and cleaning.
section: Cora Mobile
reviewed: 2026-11-03
order: 15
group: Equipment
---

Use **Parameter Mapping** to tell Cora which parameter each reading shows as and, when two devices report the same thing, which one to trust. Go to **Settings**, open the tank, and tap **Parameter Mapping**.

It sits between **Edit tank** and **Alert thresholds**. The pencil at the top of the dashboard opens **Edit tank**, which doesn't have it. You can also reach it from the Neptune Apex device page.

The screen is one list of devices, with a search field (**Search parameters**) above it. Search looks at parameter names, reading names, devices and brands. The same search field is in every parameter picker.

## One list of devices {#mapping}

Under the search field, Cora explains the screen in one line: each device's readings, and the tank parameter they show as. Tap a reading to change it.

- **Every device appears under the name you gave it.** A device you never named appears under its brand, and two unnamed devices of one brand are numbered ("AquaWiz 1", "AquaWiz 2"). Serial numbers and device IDs are never used as names; they sit behind **Show details** on the device's own page. See [A device's page](/help/mobile-devices#a-devices-page).
- **Every reading is listed under the device that really reports it.** Each row shows the device's own name for the reading, its latest value, and **Shows as**, the tank parameter it feeds. A reading you chose to hide says **Not shown**.
- **A tank has one Neptune Apex**, however many Cora devices read it. Its probes are one list under one **Apex** section (or the name you gave it). An Apex expansion module, such as a DŌS or Trident, is listed under its own name. Its readings can't be re-pointed, so tapping one lets you rename the parameter instead.
- **A device shared with other tanks appears in the list of every tank it is linked to.** Its section says *Also on* and the other tanks' names, followed by *Changes here apply to this tank only.*
- **A device with two readings or fewer starts open**; a longer one starts closed and shows its reading count, unless one of its readings shares a parameter with another device. Tap a device's name to open or close it. While you search, every match is open.

Cora recognises standard reading names on its own, so most rows already show the right parameter. Fix only the few it couldn't place.

A change is saved the moment you choose it, and there is no Save button. It starts working the next time readings come in. Fixing one here doesn't rewrite history: past readings stay where they are, and only what gets saved from then on changes. Mappings you made before this layout carry over unchanged.

:::warning Cora can't see a reading you hid
If a parameter shows no readings but the device is working, check whether its reading says **Not shown**.
:::

:::note A leak sensor can't be reassigned here
A leak sensor's alarm depends on its own name, so its row says *The leak alarm depends on this name, so it can't be changed here.* It works the same as always.
:::

:::note Devices that still need an update
A device that is waiting for a firmware update says *Changes here take effect after this device's firmware update.* Your choice is saved and applies once the update is installed.
:::

## Choosing what a reading shows as {#shows-as}

Tap a reading to open **Show this reading as**. At the top is the reading itself: the device, the reading's name and its value. Below it:

- **Your parameters** lists every parameter this tank has. Each option says where its readings come from, so you never have to guess between two similar names:
  - *Fed by* and the name of the device that feeds it, or *Also fed by* and the name of another device when this reading already shows as that parameter.
  - *No device feeds it now. Last value …* with how long ago, for a parameter whose device has gone quiet.
  - *From your test results* or *From ICP results*, with the last value, for a parameter that only has your own results.
  
  The pencil (**Rename**) beside a parameter gives it your own name, which is what shows on your dashboard, in alerts and in Reef Buddy. Leave the name empty to reset it.
- **More parameters** is folded. It holds the standard parameters this tank doesn't have yet.
- **New parameter…** makes a parameter of its own, kept apart from your other parameters. See below.
- **Don't show this reading** (*Cora ignores it*) stops the reading being recorded as any parameter. A hidden reading doesn't appear on a dashboard and doesn't trigger alerts.

The sheet ends with *Saved as soon as you choose. Past readings stay where they are.*

### New parameter {#new-parameter}

Use **New parameter…** when a reading should not be mixed with another that has the same name, for example a second pH probe in the sump. Cora opens **New parameter** and explains that the reading from that device will show as a parameter of its own and that its unit comes from the device.

1. Type a **Name**. Any name you like, for example *pH sump* or *pH 2*, up to 32 characters.
2. Tap **Create**. **Create** stays greyed out until the name has something in it. **Cancel** closes the dialog and changes nothing.

The reading now feeds the new parameter. The name keeps the spelling you typed. If you type the name of a parameter you already have, the reading joins that one and its name isn't changed. No alert range is copied from another parameter.

## Tests and lab results {#tests-and-lab-results}

Your own test kit results and your ICP results are listed at the bottom, in **Tests and lab results**. The section starts closed, because an ICP report alone has dozens of elements. Tap it to open it. Results are grouped under **ICP results** and **Your test results**.

Each result maps to a parameter the same way a device's reading does. Tap one to open **Show this reading as** and pick the parameter it shows as, for example to keep a test kit's pH apart from a probe's pH. Cora says so in the section: new results follow your choice, and past ones stay where they are. A test or ICP result is never dropped, so **Don't show this reading** isn't offered for it.

Parameters that no device reading above feeds, and that aren't tests, are listed under **Other parameters**. Tap one to rename it.

## Multiple probes for one parameter {#multiple-probes}

If two readings show as the same parameter, whether from two probes on one device or from two different devices, a banner appears at the top of the list. It says, for example, *pH gets readings from 2 devices* (or *2 probes*) and is followed by what Cora is doing: *Showing the newest one.* or *Using* the device you chose. Tap it, or tap **Choose one**, to open the sheet.

- **Newest reading** (*Whichever device reported last*) lets Cora use whichever device reported most recently. The others stay in history.
- Pick a device or probe to follow only that one. Each shows its value and how many minutes ago it reported. Your choice applies to that parameter everywhere in the tank: its tile, chart and alerts, not just one widget.
- **Show one of them separately** (*For example a second probe in the sump*) asks **Which one should show separately?** and then opens **Show this reading as** for the one you pick.

If a device you picked stops reporting, the banner says *Not reporting since* and the time, and offers **Use the newest**, so a dead probe can't leave a reading stuck.

You can compare the sources in [the parameter view](/help/mobile-metric-detail).

When two sources report the same parameter, the newest measurement wins. A value on screen is only replaced by a reading with a later measurement time, whichever device it comes from. An older reading, or a device that re-sends an old one, goes to history and doesn't overwrite the current value. If you picked a device, Cora follows that device instead.

The tank profile also has a **Parameter Sources** section (it's hidden while you create a new tank). It covers the same choice in a shorter form. Use Parameter Mapping when you want every device and reading in one place.

## Recording probe care {#recording-probe-care}

Probes drift. When you calibrate, clean or replace a probe, tell Cora, so it doesn't mistake the jump in the reading for a real change in the tank.

1. Tap the parameter's widget on the dashboard, for example pH, temperature, salinity or ORP.
2. Tap **Record probe care** (the sensor icon) in the top bar.
3. Pick what you did: **Calibrated**, **Cleaned**, **Replaced**, **Repositioned** or **Compared to reference**. You can add a **Reference reading** and a note.
4. Tap **Log probe care**.

The parameter view then shows how long ago that probe was calibrated. Probe care also works well as a recurring [maintenance task](/help/mobile-maintenance).

:::note Calibration dates explain disagreements
When a probe and a test kit disagree, check when you last calibrated the probe. That's usually the answer.
:::
