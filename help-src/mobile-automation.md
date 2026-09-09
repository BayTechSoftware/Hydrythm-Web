---
title: Automations and scenes
description: Build rules that run by themselves — triggers, conditions, actions — and group them into scenes.
section: Cora Mobile
reviewed: 2026-09-09
order: 17
group: Alerts and automation
---

An automation is a rule Cora runs for you: *when this happens, check that, then do this.* Scenes group several actions into one thing you can run or schedule.

**Settings → Automation.**

![The automation list](img/mobile-automation.webp "Automations and Scenes are separate tabs. Each rule has an enable switch.")

The screen has two tabs — **Automations** and **Scenes** — and a **New automation** button. Each rule shows a one-line summary of what it does, an enable switch, and a menu for editing or deleting it. A rule that has not run yet is marked as such.

:::warning These act on real equipment
A rule that switches a pump switches it whether or not you are watching. Build one at a time and check each does what you expect before adding the next.
:::

## The shape of a rule

Every rule is the same three parts:

**Trigger** — what wakes it up
**Conditions** — what must also be true
**Actions** — what it then does, in order

## What can wake a rule

Four things:

| Trigger | Fires when |
|---|---|
| **Metric** | A parameter crosses a value you set, in a direction you choose |
| **Alert** | An alert is raised, cleared, or either |
| **Schedule** | A time of day, in your own timezone |
| **Device status** | A device goes offline or comes back |

## Conditions

Conditions decide whether the actions actually run. You get the usual comparisons — equals, not equals, greater than, less than, and so on — and you can combine them with **and**, **or** and **not**.

There is also a **step** condition, which checks how the *previous* step turned out. That is what lets you write "try this; if it did not work, do that instead."

## What a rule can do

Twelve kinds of action:

| Action | What it does |
|---|---|
| **Control Apex Equipment** | Switch an outlet |
| **Control a Red Sea Equipment** | Drive a ReefBeat unit |
| **Control a wavemaker** | Change pump mode or intensity |
| **Control a Cora Equipment** | Switch a smart plug |
| **Control IR Device** | Send an infrared command |
| **Run Apex Feed Cycle** | Start a feed |
| **Run a Trident Test** | Trigger a test |
| **Notify Me** | Send yourself a push |
| **Wait Before Next Step** | Pause before continuing |
| **Run a Scene** | Run another scene from inside this rule |
| **Manage an Automation** | Turn another rule on or off |
| **Dose** | Run a measured dose on a dosing head |

:::warning Dosing from a rule is irreversible and capped
A dose cannot be taken back out of the tank. The head must be **calibrated** before a rule may dose from it, and unattended dosing is capped at **10 mL per head per day** — a rule cannot exceed that however it is written. Dosing actions only appear once your heads are recognised as dosing heads.
:::

:::note Use Wait to sequence steps within one rule
A pause allows a single rule to perform an ordered procedure — for example switching an outlet off, waiting, then switching it on again — without a second rule and a schedule.
:::

## Scenes

A scene is a named group of actions you can run on demand, from a schedule, or from inside another rule — "Water change", "Photo mode", "Night".

A scene may call another scene. Cora refuses to run a scene nested beyond its depth limit, and refuses a scene that would call itself, to prevent a loop that would continue acting on the tank indefinitely.

After a scene runs you are told what happened, step by step, including anything that failed.

## Turning a rule off

Every rule has an enable switch. Turning one off keeps its definition — useful when you want a rule back next season rather than rebuilding it.

## Seeing what a rule did

Every action a rule takes is recorded with the rule as its cause. See **[Activity](/help/mobile-activity)**.
