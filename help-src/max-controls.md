---
title: Outlets and controls
description: Switching outlets from Cora Max, using feed mode, and what Auto actually means.
section: Cora Max
order: 5
---

Cora Max can switch the equipment on your system — from control widgets on the dashboard, from the Outlets & Feed drawer, or by voice.

:::warning These controls act on your tank
There is no undo. Outlets marked with a padlock ask you to confirm first; the rest apply as soon as you tap. A command can come back **Confirmed**, **Unconfirmed** (sent, nothing reported back), **Refused** or **No change** — see [Controlling your equipment](/help/mobile-device-control).
:::

## The three states

Every outlet is in one of three states.

**Auto** returns the outlet to its Apex programming. This is where an outlet should sit most of the time.

**Off** and **On** are manual overrides. They take effect at once and **stay until you change them back**. They do not expire, and nothing puts them back for you.

:::warning A manual override does not expire
Set it back to **Auto** when you are done; nothing does that for you. It can still be changed later by you, by voice, or by an automation — an override is not a lock.
:::

## Switching from the dashboard

Control widgets show the three states with the current one highlighted. Tap the state you want.

Some outlets are locked — shown with a padlock. That is a safety lock set on the tank, and it exists so a stray tap cannot switch something critical. Unlock it in tank settings if you genuinely need to.

## The Controls drawer

Pull up the tab at the bottom of the dashboard to open **Controls** — every outlet on the system in one place, whether or not it has a widget, plus the feed cycles.

![The Controls drawer](img/max-controls.webp "Feed cycles across the top, then every outlet.")

An outlet carrying a **padlock** requires an explicit confirmation before it changes. Tapping it opens a dialog naming the outlet, its current state, and the override you are about to apply. It is a confirmation step, not a lock to be switched off elsewhere.

## Feed mode

Feed mode is the safe way to pause flow for feeding. It pauses the equipment that should be paused, leaves alone the equipment that should not, and **puts everything back by itself** when the time is up.

Use it instead of switching pumps off by hand. The whole point is that it restores the system without depending on you remembering.

Feed cycles are lettered **A**, **B**, **C** and **D** — the cycles your controller defines, each pausing a different set of equipment. Pick the one that matches what you are doing. **Cancel** ends a running cycle early and restores everything immediately.

Start one from the Controls drawer, or say *"start feed mode"*.

## By voice

You can switch outlets by voice — *"turn the skimmer off"*, *"put the fan back on auto"*.

Anything that reaches your equipment is **confirmed before it happens**: Cora tells you what it is about to do and waits for you to agree. It will not act on an instruction it is not sure about.

See **[Talking to Cora](/help/max-voice)**.

## Seeing what happened

Every switch is recorded, along with what caused it — you, a rule, a schedule, or the Assistant. On your phone that is **Settings → Activity**.

This is the first place to look when something changed and you do not know why.
