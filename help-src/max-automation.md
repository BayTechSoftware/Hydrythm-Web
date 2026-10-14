---
title: Scenes on Cora Max
description: Build, run, edit and delete scenes on Cora Max, from Settings → Automations or a scene tile on the dashboard.
section: Cora Max
reviewed: 2026-10-13
order: 9
group: Alerts and automation
twin: mobile-automation
---

A **scene** is a saved set of equipment actions that run together, either for a set time or until you stop it. You can build, run and edit scenes on Cora Max. Scenes made on your phone and on Cora Max are the same scenes. Automation rules (the "when this happens, do that" kind) are set up on your phone. More in [Scenes and automations](/help/mobile-automation).

![The Scenes list on Cora Max, with a filter chip for each tank and a New Scene button](img/max-automation.webp "The Scenes list, filtered by tank. With no scenes yet, it says so and offers New Scene.")

## Where to find scenes

**Settings → Automations** opens **Scenes**, the list of every scene for all your tanks. If you have more than one tank, there's a filter chip for each, plus **All tanks**.

Tap a scene to edit it, or tap **New Scene** to build one. If you have more than one tank and no filter is picked, Cora Max asks **Which tank is this scene for?**

## Building a scene

![An empty New Scene form on Cora Max](img/max-scene-builder.webp "A new scene: a name, Permanent or Timed, Ask before running, then Add Step.")

1. Type a **Scene name**.
2. Tap **Add Step** and pick what the step does. You only see the kinds of equipment this tank has:
   - **Apex Outlet**: switch a Neptune Apex outlet to **ON**, **OFF** or **AUTO**.
   - **Control a Red Sea device**: for example **ReefDose: dose now**, **ReefDose: set daily dose**, **ReefRun: set pump speed**, **ATO: start a manual fill** or **ReefMat: advance the roll**.
   - **Control a wavemaker**: set a Jecod pump's flow or wave mode, turn it on or off, or **Pause for feeding**.
   - **Run a Trident test**: alkalinity, combined or nutrients. Each run uses reagent.
   - **Run an Apex feed cycle**: pick the cycle. The Apex runs the feed timer and resumes by itself.
3. Add more steps the same way. You can reorder or remove them. A step this screen can't edit says **Not editable here**. Edit that one on your phone.
4. Choose how long it runs. **Timed** runs for the minutes you set in **Run for (minutes)**. **Permanent** runs until you stop it.
5. Leave **Ask before running** on unless you're sure the scene never touches anything that needs a second look.
6. Tap **Save**.

:::note Doses in a scene
A Neptune DŌS head can never be a scene step. A **ReefDose: dose now** step can, and it has its own **Max per dose (mL)**. Leave it empty for 10 mL. A dose above that ceiling is refused, never made smaller. Keep **Ask before running** on for any scene that doses.
:::


## Running a scene

Scenes show up as tiles on the dashboard. Tap **Run** to start one.

If the scene asks before running, Cora Max first lists what it's about to do, one line per step. Read it, then run it or cancel.

While a timed scene runs, its tile counts down to the end and shows **Stop** if you want to end it early. A permanent scene's tile shows it as running until you tap **Stop**. When a scene ends or you stop it, the tile shows **Restoring…** while Cora puts the equipment back.

Running or stopping a scene goes through Cora Cloud, like any other command. You'll find the result in [Activity](/help/max-activity).

Scenes can't be run by voice on Cora Max. Use the tile, **Settings → Automations**, or your phone.

If a scene won't run or won't stop, have a look at [Troubleshooting](/help/troubleshooting).

:::note Child lock covers scenes too
While [Child lock](/help/max-settings#child-lock) has locked the screen, you can't run, stop or edit a scene from it, just like every other control.
:::

## Editing or deleting a scene

To change a scene, open it from **Settings → Automations** or long-press its tile on the dashboard. Change what you need and tap **Save**. To remove it, tap **Delete Scene**. This can't be undone.

:::note An older Cora Max can run a scene but not edit it
Older Cora Max versions still show and run every scene, but can't change one. Update Cora Max ([Updates and recovery](/help/max-updates)), or edit the scene on your phone.
:::
