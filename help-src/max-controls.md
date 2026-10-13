---
title: Outlets and controls
description: Switch Apex outlets from Cora Max, start or cancel feed mode, use the Outlets & Feed drawer, and what Auto, Off and On mean.
section: Cora Max
reviewed: 2026-10-13
order: 5
group: Equipment
---

This page covers switching outlets and starting feed mode from Cora Max. You can do it from outlet tiles on the dashboard, from the **Outlets & Feed** drawer, or by voice.

:::warning These controls act on your tank
There's no undo. Outlets with a padlock ask you to confirm first. The rest change as soon as you tap. A command can come back **Confirmed**, **Unconfirmed** (sent, but nothing reported back), **Refused** or **No change**. More in [Controlling your equipment](/help/mobile-device-control).
:::

## The three states {#the-three-states}

Every outlet is in one of three states.

**Auto** hands the outlet back to its Apex programming. Most of the time, that's where an outlet should be.

**Off** and **On** are manual overrides. They take effect right away and **stay until you change them back**. They don't expire, and nothing resets them for you.

:::warning A manual override doesn't expire
Set it back to **Auto** when you're done, because nothing else will. An override isn't a lock, though. You, your voice or an automation can still change it later.
:::

## Switching from the dashboard {#switching-from-the-dashboard}

Outlet tiles show the three states, with the current one highlighted. Tap the one you want.

Some outlets have a **padlock**. It means the outlet asks you to confirm before it changes, so a stray tap can't switch something critical. When you tap it, a dialog shows the outlet, its current state, the override you're about to set and what that can do to the tank. There's no lock to turn off somewhere else.

By default the padlock is on heaters, chillers, return pumps, top-off (ATO), feeders and any outlet Cora can't classify. Lights, skimmers, wavemakers, dosing pumps, reactors, UV and fans switch on one tap.

## The Outlets & Feed drawer {#the-controls-drawer}

You'll only see this on a tank with a Neptune Apex. Tap the small **Outlets & Feed** label at the bottom of the dashboard, or swipe up anywhere on the dashboard. It opens **Controls**, with **FEED** across the top and **OUTLETS** below.

![The Controls drawer](img/max-controls.webp "Feed cycles across the top, then the outlets picked for this dashboard.")

It shows the outlets and feed cycles you picked under **Outlets & Feed** in the [dashboard editor](/help/max-dashboard-editing#outlets-feed), or all of them if you haven't picked any. Padlocked outlets ask you to confirm here too. Sockets on other controllers are switched from their own device pages, see [Controlling equipment from Cora Max](/help/max-device-control).

If an outlet tap comes back with *The Apex did not answer: it may have applied*, check the outlet before you try again.

## Feed mode {#feed-mode}

Feed mode is the safe way to pause flow while you feed. Your Apex pauses the equipment that should pause, leaves the rest alone, and **puts everything back by itself** when time's up.

Use it instead of switching pumps off by hand. It puts the system back even if you forget.

Feed cycles are Feed A, Feed B, Feed C and Feed D, shown as **A**, **B**, **C** and **D** under **FEED**. They're the cycles programmed on your Apex, and each one can pause a different set of equipment. Pick the one that fits what you're doing. **Cancel** ends a running cycle early and puts everything back right away.

Start one from the drawer, or say *"start feed mode"*.

If Cora Max says the Apex didn't answer, the feed may already be running. Check the return pump before you start it again.

## By voice {#by-voice}

You can switch outlets by voice, for example *"turn the skimmer off"* or *"put the fan back on auto"*.

Before anything reaches your equipment, Cora **checks with you first**. It tells you what it's about to do and waits for your OK. If it isn't sure what you asked, it won't act.

More in [Talking to Cora](/help/max-voice).

## Seeing what happened {#seeing-what-happened}

Every request is logged, with what asked for it and how it went, whether it came from Cora Mobile, a Cora Max, voice, the Assistant or an automation. On Cora Max, tap the tank name in the top bar and choose **Activity**. On your phone, it's under **Settings → Activity**. More in [Activity on Cora Max](/help/max-activity).

When something changed and you don't know why, look there first.
