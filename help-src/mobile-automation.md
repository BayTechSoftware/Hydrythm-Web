---
title: Automations and scenes
description: Make Cora act on its own when a reading, an alert, a time or a device goes offline, and group actions into scenes you run with one tap.
section: Cora Mobile
reviewed: 2026-10-24
order: 25
group: Alerts and automation
twin: max-automation
---

An automation is a rule Cora runs for you: *when this happens, check that, then do this.* A scene groups several actions into one thing you run when you want.

Go to **Settings → Automations**.

![The Automation screen in Cora Mobile, with the Automations and Scenes tabs](img/mobile-automation.webp "Automations and Scenes are separate tabs. Each rule has its own switch.")

The screen has two tabs, **Automations** and **Scenes**, with a **New automation** or **New scene** button. Each rule shows a one-line summary, an enable switch and a menu to **Edit** or **Delete** it. A rule that hasn't run yet says so.

:::warning Rules act on real equipment
If a rule switches a pump, the pump switches even when you aren't watching. Build one rule at a time and check it does what you expect before you add the next.
:::

## The shape of a rule {#shape}

Every automation has three parts.

- The trigger wakes it up.
- The conditions must also be true.
- The actions are what it then does, in order.

![An empty New automation form in Cora Mobile](img/mobile-rule-builder.webp "A new automation: triggers, If conditions, Then actions, Else-if and Else, then the cooldown and time window.")

## What can wake a rule {#triggers}

Add one or more triggers under **When: any trigger**. Any one of them starts the rule.

| Trigger | Fires when |
|---|---|
| **When a metric changes** | A parameter crosses a value you set. Pick the **Direction**: **Rising**, **Falling** or **Any change** |
| **When an alert fires** | An alert is **Raised**, **Cleared**, or either. You can limit it to **Threshold** or **Rate of change** alerts. |
| **At a time of day** | A time of day, in your own timezone |
| **When a device goes offline** | Your Cora Max goes **Offline**, comes back **Online**, or either way |

:::tip Hear about it when your Cora Max drops off
A rule with **When a device goes offline** and **Notify Me** tells you when the Cora Max that reads your equipment loses power or Wi-Fi.
:::

## Conditions {#conditions}

Conditions decide whether the actions run. Tap **Add condition** and choose:

- **Metric compare**, a reading above, below or equal to a value
- **Metric inside / outside a range**
- **Alert active**
- **Outlet is on / off**, for an Apex outlet
- **Time of day**, a window such as 22:00 to 06:00
- **How an earlier step went**, which checks whether an earlier step went **OK** or was **Skipped**. Use it for "try this, and if it didn't work, do that instead"

With several conditions, set **Match** to **All (AND)** or **Any (OR)**.

## Branches and per-step checks {#branches}

An automation can do different things in different cases. Its first block is **If**. Tap **Else-if** to add another case, or add an **Else** block for everything else. Cora runs the first block whose conditions hold.

You can also gate a single action. Tap **Only if…** on that step and give it its own condition. With no condition, the step always runs.

## When it may run {#when-it-may-run}

- **Cooldown between runs** stops a rule firing again too soon. It starts at 10 min.
- **Only run between** limits the rule to a time window, for example daytime only.
- **Test against live values** checks the rule against your tank's readings right now, without doing anything. It tells you what *would run*, or why nothing would.

## What a rule can do {#actions}

An action that needs equipment only shows up on a tank that has that equipment.

| Action | What it does |
|---|---|
| **Control Apex Equipment** | Switch an outlet |
| **Run Apex Feed Cycle** | Start a feed. The Apex ends it on its own timer |
| **Run a Trident Test** | Start a test. Each run uses reagent |
| **Dose a DŌS Head** | Run a measured dose on a DŌS head |
| **Control a Red Sea Equipment** | Drive a ReefBeat unit |
| **Control a wavemaker** | Set a Jecod pump's flow, wave mode or power, or **Pause for feeding**. The Cora Max at the tank puts the pump back when the feed ends |
| **Notify Me** | Send yourself a push with your own **Title** and **Message** |
| **Wait Before Next Step** | Pause before carrying on |
| **Run a Scene** | Run a scene from inside this rule |
| **Manage an Automation** | Turn another rule on or off |
| **Create a Maintenance Task** | Put a job on the tank's [maintenance](/help/mobile-maintenance) list, for example change the CO2 scrubber media when pH drops below a value |


:::warning A dose can't be undone, and it's capped
You can't take a dose back out of the tank. A rule can only dose from a head that has been measured with **Measure to dose** on a Cora Max. The dose runs on a Cora Max at the tank. Dosing from rules is capped at **10 mL per head per day**, however the rule is written.
:::

:::note What Create a Maintenance Task does
Pick the tank, then **Existing task** (an existing task becomes due now) or **New task** (give it a **Task name**). A new task is a one-off, due right away, and the rule doesn't raise it again while it's still open. You get one notification, and the one-off task leaves the list when you complete it.
:::

:::note Wait is short
**Wait Before Next Step** pauses for up to 60 seconds, and a branch can wait 60 seconds in total. After the pause, the next step sees fresh readings. For a longer hold, like a return pump off for 30 minutes during a water change, use a scene with **Run for** (below).
:::

## Scenes {#scenes}

A scene is a named group of actions, like "Water change", "Photo mode" or "Night". Tap **New automation** or **New scene** and pick **Scene** at the top. A scene has no trigger. You run it with **Run now** in the list, from inside a rule with **Run a Scene**, or on a timetable through a rule with **At a time of day**.

**Run for** sets how long a scene lasts: a number of minutes or hours, or **Until I change it**. When the time is up, Cora switches the scene's outlets back to how they were. Other equipment stays as the scene left it. While a timed scene is running, the list shows a countdown and a **Stop** button that ends it early.

If a scene switches an outlet that matters, such as a heater, chiller, return pump or top-off, Cora asks before running it and lists those steps. You can turn this off with **Ask before running** on the scene.

A scene can call another scene, up to 3 deep. Cora won't run a scene that calls itself, because it could loop and keep acting on the tank.

After a scene runs, you see what happened step by step, including anything that failed or didn't run.

## Scenes made on Cora Max {#scenes-on-cora-max}

You can also build and edit scenes on a Cora Max. It's the same set of scenes, shared across the account. An older Cora Max can still run a scene made on the phone. Editing on the device is newer, though, so an older Cora Max may show a scene without letting you change it. Edit it from the phone instead.

## Turning a rule off {#turning-a-rule-off}

Every rule has an enable switch. Turning a rule off keeps its settings, which helps when you want it back next season.

## Seeing what a rule did {#seeing-what-a-rule-did}

Every action a rule takes is recorded with **Automation rule** as its cause. You'll find it in [Activity](/help/mobile-activity).

A step that fails or has to wait does not stay pending. It expires at once, the run is recorded as failed, and you get a notification that names the automation, the step and why. A step fails when, for example, its device is offline, no Cora Max is available to carry it out, the device refuses it or doesn't answer, or a heater or chiller was switched a moment ago. A step on a removed tank doesn't notify you.
