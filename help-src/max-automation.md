---
title: Scenes on Cora Max
description: Building, running and editing scenes directly on the Cora Max screen.
section: Cora Max
reviewed: 2026-09-27
order: 15
group: Automation
---

A **scene** is a saved set of equipment actions that runs together, either for a fixed time or until you stop it. Scenes work the same whether you build them on your phone or on Cora Max; this page covers doing it at the wall.

## Where to find scenes

**Settings → Automations** lists every scene across every tank you have, with a filter chip for each tank when you have more than one. It opens the same list whether the scene was built on the phone or on Cora Max.

Tap a scene to edit it, or tap **+** to build a new one. If you have more than one tank and no filter is chosen, Cora Max asks which tank the new scene belongs to.

## Building a scene

1. Give the scene a **name**.
2. Add **steps**. From Cora Max, a step can switch an Apex outlet (**On**, **Off** or **Auto**) or a Zigbee plug (**on**, **off** or **toggle**). Steps added on the phone for other kinds of equipment still show here, and can still be reordered or removed, even though this screen cannot add another one like it.
3. Choose how long it runs: a fixed number of minutes, or **permanent** (it keeps running until you stop it).
4. Choose whether running the scene needs a **confirmation** step. Leave this on unless you are certain the scene never touches anything that would be unsafe to change without a second look.
5. Save.

:::note DŌS dosing heads are never a scene step
A scene, built on Cora Max or on the phone, can never switch on a dosing head. This is deliberate: a dose is not the kind of action a scene should be able to trigger by accident.
:::

## Running a scene

Scenes appear as tiles on the dashboard. Tap **Run** to start one.

If the scene needs confirmation, Cora Max lists exactly what it is about to do, one line per step, before anything happens. Read it, then choose to run it or cancel.

While a timed scene is running, its tile shows a countdown to when it ends, and a **Stop** button to end it early. A permanent scene's tile stays in its running state until you stop it.

Running or stopping a scene always goes through Cora Cloud, the same way any other command does; see [What was changed, and by what](/help/max-activity) for where the result is recorded.

**If it does not work:** if a scene will not run or will not stop, see [Troubleshooting](/help/troubleshooting).

:::note Child lock covers scenes too
If [Child lock](/help/max-voice) is on, running or stopping a scene from this screen is blocked along with every other control. Questions about a scene still work over voice; starting or stopping one does not.
:::

## Editing or deleting a scene

Open the scene from **Settings → Automations**, or long-press its tile on the dashboard, to change its name, steps, duration or confirmation setting, or to delete it.

:::note Older Cora Max screens can run a scene but not edit it
Building and editing scenes at the wall is a newer Cora Max capability. An older Cora Max on the same account can still show and run a scene that was made on the phone or on a newer Cora Max; it simply cannot change it. Update Cora Max, or edit the scene from the phone or from a newer screen, if this comes up.
:::

See [Scenes and automations](/help/mobile-automation) for what a scene can do in more detail, and how they are built on the phone.
