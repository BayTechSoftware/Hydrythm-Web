---
title: Scenes on Cora Max
description: Building, running and editing scenes right on the Cora Max screen.
section: Cora Max
reviewed: 2026-09-27
order: 15
group: Automation
---

A **scene** is a saved set of equipment actions that run together, either for a set time or until you stop it. Scenes work the same whether you build them on your phone or on Cora Max. This page is about doing it at the wall.

## Where to find scenes

**Settings → Automations** lists every scene for all your tanks. If you have more than one tank, there's a filter chip for each. You'll see the same list whether a scene was built on your phone or on Cora Max.

Tap a scene to edit it, or tap **+** to build a new one. If you have more than one tank and no filter is picked, Cora Max asks which tank the new scene is for.

## Building a scene

1. Give the scene a **name**.
2. Add **steps**. On Cora Max, a step can switch an Apex outlet (**On**, **Off** or **Auto**) or a Zigbee plug (**on**, **off** or **toggle**). Steps for other equipment that were added on your phone still show up here. You can reorder or remove them, but you can't add new ones like them from this screen.
3. Choose how long it runs. Pick a number of minutes, or **permanent** (it runs until you stop it).
4. Choose whether the scene asks for **confirmation** before it runs. Leave this on unless you're sure the scene never touches anything that needs a second look before it changes.
5. Save.

:::note DŌS dosing heads are never a scene step
No scene can switch on a dosing head, whether you build it on Cora Max or on your phone. A dose shouldn't be something a scene can start by accident.
:::

## Running a scene

Scenes show up as tiles on the dashboard. Tap **Run** to start one.

If the scene needs confirmation, Cora Max first lists what it's about to do, one line per step. Read it, then run it or cancel.

While a timed scene runs, its tile counts down to the end and shows a **Stop** button if you want to end it early. A permanent scene's tile shows it as running until you stop it.

Running or stopping a scene always goes through Cora Cloud, like any other command. You'll find the result in [What was changed, and by what](/help/max-activity).

If a scene won't run or won't stop, have a look at [Troubleshooting](/help/troubleshooting).

:::note Child lock covers scenes too
When [Child lock](/help/max-voice) is on, you can't run or stop a scene from this screen, just like every other control. You can still ask about a scene by voice, but you can't start or stop one.
:::

## Editing or deleting a scene

To change a scene's name, steps, duration or confirmation setting, or to delete it, open it from **Settings → Automations** or long-press its tile on the dashboard.

:::note Older Cora Max screens can run a scene but not edit it
Building and editing scenes at the wall is new on Cora Max. An older Cora Max on the same account can still show and run a scene made on your phone or on a newer Cora Max. It just can't change it. If that happens, update Cora Max, or edit the scene on your phone or a newer screen.
:::

There's more on what scenes can do, and how to build them on your phone, in [Scenes and automations](/help/mobile-automation).
