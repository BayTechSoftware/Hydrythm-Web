---
title: Automations and scenes
description: Build rules that run on their own with triggers, conditions and actions, and group actions into scenes.
section: Cora Mobile
reviewed: 2026-09-27
order: 17
group: Alerts and automation
---

An automation is a rule Cora runs for you: *when this happens, check that, then do this.* A scene groups several actions into one thing you can run or schedule.

**Settings → Automation.**

![The automation list](img/mobile-automation.webp "Automations and Scenes are separate tabs. Each rule has an enable switch.")

The screen has two tabs, **Automations** and **Scenes**, and a **New automation** button. Each rule shows a one-line summary, an enable switch and a menu to edit or delete it. A rule that hasn't run yet says so.

:::warning Rules act on real equipment
If a rule switches a pump, the pump switches even when you aren't watching. Build one rule at a time and check it does what you expect before you add the next.
:::

## The shape of a rule

Every rule has three parts.

- The trigger wakes it up.
- The conditions must also be true.
- The actions are what it then does, in order.

## What can wake a rule

There are four triggers:

| Trigger | Fires when |
|---|---|
| **Metric** | A parameter crosses a value you set, in the direction you choose |
| **Alert** | An alert is raised, cleared, or either |
| **Schedule** | A time of day, in your own timezone |
| **Device status** | A device goes offline or comes back |

## Conditions

Conditions decide whether the actions run. You get the usual comparisons, like equals, not equals, greater than and less than, and you can combine them with **and**, **or** and **not**.

There's also a **step** condition. It checks how the *previous* step went, so you can write "try this, and if it didn't work, do that instead."

## What a rule can do

Actions that need equipment only show up on a tank that has that equipment:

| Action | What it does |
|---|---|
| **Control Apex Equipment** | Switch an outlet |
| **Control a Red Sea Equipment** | Drive a ReefBeat unit |
| **Control a wavemaker** | Set a Jecod pump's flow, wave mode or power, or **Pause for feeding**. The Cora Max at the tank puts the pump back when the feed ends |
| **Control a Cora Equipment** | Switch a smart plug |
| **Control IR Device** | Send an infrared command |
| **Run Apex Feed Cycle** | Start a feed |
| **Run a Trident Test** | Start a test |
| **Notify Me** | Send yourself a push |
| **Wait Before Next Step** | Pause before carrying on |
| **Run a Scene** | Run a scene from inside this rule |
| **Manage an Automation** | Turn another rule on or off |
| **Dose a DŌS Head** | Run a measured dose on a DŌS head |

:::warning A dose can't be undone, and it's capped
You can't take a dose back out of the tank. A head has to be **calibrated** before a rule can dose from it. Unattended dosing is capped at **10 mL per head per day**, however the rule is written. Dosing actions only show up once Cora recognises your heads as dosing heads.
:::

:::note Use Wait to run steps in order
With a pause, one rule can run a sequence, for example switching an outlet off, waiting, then switching it back on. You don't need a second rule and a schedule.
:::

## Scenes

A scene is a named group of actions, like "Water change", "Photo mode" or "Night". You can run it when you want, on a schedule, or from inside another rule.

A scene can call another scene. Cora won't run a scene nested deeper than its limit, and it won't run a scene that calls itself. Either could loop and keep acting on the tank.

After a scene runs, you see what happened step by step, including anything that failed.

When you run a scene by hand, Cora asks you to confirm first, because a scene can switch several pieces of equipment together.

## Scenes made on Cora Max

You can also build and edit scenes on a Cora Max. It's the same set of scenes, shared across the account. An older Cora Max can still run a scene made on the phone. Editing on the device is newer, though, so an older Cora Max may show a scene without letting you change it. Edit it from the phone instead.

## Turning a rule off

Every rule has an enable switch. Turning a rule off keeps its settings, which helps when you want it back next season.

## Seeing what a rule did

Every action a rule takes is recorded with the rule as its cause. You'll find it in [Activity](/help/mobile-activity).
