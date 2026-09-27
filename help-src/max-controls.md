---
title: Outlets and controls
description: Switching outlets from Cora Max, using feed mode, and what Auto really means.
section: Cora Max
reviewed: 2026-09-09
order: 5
group: Equipment
---

Cora Max can switch the equipment on your system. You can do it from control widgets on the dashboard, from the Outlets & Feed drawer, or by voice.

:::warning These controls act on your tank
There's no undo. Outlets with a padlock ask you to confirm first. The rest change as soon as you tap. A command can come back **Confirmed**, **Unconfirmed** (sent, but nothing reported back), **Refused** or **No change**. More about this in [Controlling your equipment](/help/mobile-device-control).
:::

## The three states

Every outlet is in one of three states.

**Auto** hands the outlet back to its Apex programming. Most of the time, that's where an outlet should be.

**Off** and **On** are manual overrides. They take effect right away and **stay until you change them back**. They don't expire, and nothing resets them for you.

:::warning A manual override doesn't expire
Set it back to **Auto** when you're done, because nothing else will. An override isn't a lock, though. You, your voice or an automation can still change it later.
:::

## Switching from the dashboard

Control widgets show the three states, with the current one highlighted. Tap the one you want.

Some outlets have a **padlock**. There's nothing to switch off for it. It means the outlet asks you to confirm before it changes, so a stray tap can't switch something critical. There's more on this below.

## The Controls drawer

Pull up the tab at the bottom of the dashboard to open **Controls**. It shows every outlet on the system, with or without a widget, plus the feed cycles.

![The Controls drawer](img/max-controls.webp "Feed cycles across the top, then every outlet.")

An outlet with a **padlock** needs you to confirm before it changes. When you tap it, a dialog shows the outlet, its current state and the override you're about to set. It's a confirmation step, and there's no lock to turn off somewhere else.

## Feed mode

Feed mode is the safe way to pause flow while you feed. It pauses the equipment that should pause, leaves the rest alone, and **puts everything back by itself** when time's up.

Use it instead of switching pumps off by hand. It puts the system back even if you forget.

Feed cycles are lettered **A**, **B**, **C** and **D**. They're the cycles your controller defines, and each one pauses a different set of equipment. Pick the one that fits what you're doing. **Cancel** ends a running cycle early and puts everything back right away.

Start one from the Controls drawer, or say *"start feed mode"*.

## By voice

You can switch outlets by voice, for example *"turn the skimmer off"* or *"put the fan back on auto"*.

Before anything reaches your equipment, Cora **checks with you first**. It tells you what it's about to do and waits for your OK. If it isn't sure what you asked, it won't act.

More about this in [Talking to Cora](/help/max-voice).

## Seeing what happened

Every request is logged, along with what asked for it and how it travelled. The request can come from Cora Mobile, a Cora screen, voice, the Assistant, an automation rule, a smart button or your account. On Cora Max, tap the tank name in the top bar and choose **Activity**. On your phone, you'll find it in **Settings → Activity**.

When something changed and you don't know why, look there first.
