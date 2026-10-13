---
title: Maintenance
description: Add recurring jobs like cleaning the skimmer or changing filter socks, get reminded when they're due, and mark them done or snooze them.
section: Cora Mobile
reviewed: 2026-10-13
order: 26
group: Records
twin: max-records
---

Maintenance keeps the jobs your tank needs on a regular basis, with a reminder for each one.

Tap **Maintenance** in the row of buttons under the dashboard. It's also in Settings → your tank → **Maintenance**.

![The maintenance list](img/mobile-maintenance.webp "Compliance, overdue count, and each task with its last completion and next due date.")

## The summary {#summary}

At the top you'll see **Maintenance Compliance**, the share of tasks that are on schedule right now, and how many tasks are overdue.

Each task in the list is colour-coded as overdue, due soon or scheduled. It also shows when you last did it and when it's due next.

## Adding a task {#adding-a-task}

Tap **Add Task**, then choose:

- **From Template** for a common job with its interval filled in. Pick it, then set when it's next due and the time you want to be reminded, and tap **Confirm**.
- **Custom Task** for your own. Give it a **Task name**, an **Interval (days)**, a **Category** and a **Next due date**. Turn on **Reminder** and pick **Remind me at** if you want a notification.

Some of the templates, with the interval they start on:

| Task | Interval |
|---|---|
| Change filter socks | 3 days |
| Clean skimmer cup | 7 days |
| Water change | 7 days |
| Test water parameters | 7 days |
| Replace carbon | 30 days |
| Calibrate pH probe | 30 days |
| Clean powerheads | 90 days |
| Upload ICP results | 90 days |

You can change the interval of any task later.

### Tasks Cora adds for Red Sea equipment {#red-sea-tasks}

When you connect a Red Sea ReefDose, ReefATO+, ReefMat or ReefRun, Cora adds the servicing that unit needs, already on the right interval:

| Device | Task | Interval |
|---|---|---|
| ReefATO+ | Replace ReefATO+ EC sensor | 42 days |
| ReefATO+ | Replace ReefATO+ return pump | 135 days |
| ReefMat | Replace ReefMat carbon | 25 days |
| ReefRun | Check ReefRun skimmer venturi | 35 days |
| ReefRun | Replace ReefRun skimmer rotor | 135 days |
| ReefRun | Calibrate ReefRun full-cup sensor | 28 days |
| ReefRun | Calibrate ReefRun overskimming sensor | 28 days |
| ReefRun, per pump | Service ReefRun pump motor | 135 days |
| ReefRun, per pump | Clean ReefRun pump strainer | 42 days |
| ReefDose, per head | Calibrate ReefDose head | 90 days |
| ReefDose, per head | Replace ReefDose head tubing | 450 days |

They work like any task you add yourself. You can rename them, change the interval, snooze them or delete them. If you delete one, Cora won't add it back for that device.

### Test water {#test-water}

If you tap **Remind me to test every week** on the first-test card, Cora adds a weekly task called **Test water**, due on the **Test day** you pick. It works like any other task. See [Setting up Cora Mobile](/help/mobile-setup). You can also add a testing reminder at any time with the **Test water parameters** template.

### From an automation {#from-an-automation}

An [automation](/help/mobile-automation) with the action **Create a Maintenance Task** can put a job on this list when its rule fires, or make an existing task due now. A new one is a **One-off task**, due now, and it shows *Raised by an automation* with the reason. It leaves the list when you complete it. While it's still open, the same automation doesn't add another. You get one notification.

## Reminders {#reminders}

Open a task and turn on **Reminder**, then pick **Remind me at**. You get a notification the day before it's due and one on the day. While it's overdue, you get a reminder every few days. If several tasks on a tank come due together, they arrive as one notification.

Reminders come under **Maintenance Reminders** in [Settings → Notifications](/help/mobile-notifications). If you'd rather just see a task in the list, turn its **Reminder** off.

## Marking a task done {#marking-done}

Swipe the task to the right, or open it and tap **Complete**. If you swiped by mistake, tap **Undo** on the message that appears.

Cora saves the time you finished and counts the next due date from then. So if you do a job three days late, the next one moves out by three days too.

The task's sheet shows its **Completion history**, including how late each one was.

:::note Completing a task also writes a journal entry
Cora adds a short entry to your [journal](/help/mobile-journal) for you, noting if it was late. Add your own entry when there's more to say, for example when the pump was full of sand or the socks were black after one day.
:::

## Editing a task {#editing}

Tap a task to open it. You can change the **Task name**, **Interval (days)**, **Notes (optional)**, **Next due date** and the reminder, then tap **Save**. **Delete** removes it.

## Snoozing {#snoozing}

Can't get to a job right now? Open it, tap **Snooze** and pick **1 Day**, **3 Days**, **1 Week**, **2 Weeks** or **1 Month**. It stays in the list as **Snoozed** with its new date, and you won't be reminded until then.

:::warning Only mark a task done when you've done it
The next due date is counted from the day you mark it done. If you mark an open task as done, every later due date shifts. Snooze it instead.
:::

There's no way to pause a task. For a job that doesn't apply this season, snooze it for **1 Month**, or delete it and add it again later.
