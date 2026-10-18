---
title: Reef Buddy
description: Your daily Reef Buddy briefing, what it covers, when it arrives, how to read the scores, and why a briefing might not come.
section: Cora Mobile
reviewed: 2026-10-18
order: 31
group: Intelligence
twin: max-intelligence
---

Reef Buddy is a short daily look at your tank. It comes each morning, tells you what changed, and points out anything that needs your attention before you'd notice it yourself.

You'll see it as a card at the top of your dashboard, and as one notification when there's something worth acting on.

![A Reef Buddy briefing](img/mobile-reefbuddy.webp "Stability and Data scores, a summary, then the insights behind them.")

## What is in a briefing

It starts with a headline, one line that sums up the tank today. Then come two scores.

| Score | Means |
|---|---|
| **Stability** | Out of 100. How steady your readings have been over the last 30 days |
| **Data** | A percentage. How complete the data behind the assessment is |

A low Data score means Cora had fewer readings to work with than it wanted. Look at it first. When Data is low, take the Stability number next to it as a first guess.

Next is a summary, a short paragraph that explains the headline using your real values and ranges.

Then come the insights, one for each finding. Each has a category (such as *Water Chemistry*) and a cadence (such as *Daily*), and you can expand it for detail. A chip at the top of the section shows the tank type and how complete its profile is. Both affect what Cora can conclude.


Cora filters insights before they reach you. An insight has to hold up over several readings. One isn't enough. It also has to tell you something a single chart wouldn't already show.

Tap the card on the dashboard to open the full briefing.

## Opening the briefing again {#dismissing-the-card}

Tap **×** to clear today's card from the dashboard. Tomorrow's still comes.

To open today's briefing after you've cleared the card, tap the newspaper button at the top of the dashboard (**Reef Buddy daily health**). An older briefing opens from its notification.

## Updating the briefing with a new test

If you log a test by hand or add an ICP result after the briefing came out, the full briefing shows **New readings since this briefing** with an **Update briefing** button. Tap it and Cora redoes the briefing with the new numbers. It uses one message from your Assistant allowance.

You can do this once a day for your account. After that the button is greyed out and says *You can update the briefing once a day. Next update: tomorrow.*

Probe and controller readings don't trigger this offer, because they come in all day.

## Why you're seeing an insight

Under an insight, tap **Why am I seeing this?** The sheet **Why you're seeing this** lists the **Readings it used**, the **Target it compared against** (your own target, or a reference range), anything **From your journal** that it took into account, and the time window in days it looked at. If the reasoning doesn't fit your tank, answer the insight as described in [Correcting an insight](#correcting-an-insight).

Briefings also draw on more than parameter readings. They can use the light schedules on your lights, the speed of a ReefMat roll, your hand-logged alkalinity next to a device's and the totals of your DŌS heads.


## When it arrives

Once a day for each tank, at the hour you choose. Set it in **Settings → Briefing time**, next to **Notifications**. The briefing arrives within about 15 minutes of that hour, in your own time zone. If you never choose, it comes at 8:00.

Pick an hour after your usual morning test, so today's result is in the briefing.

On a day when nothing needs your attention, Reef Buddy usually stays quiet. It won't push just to say everything's fine. **A push means there's something worth acting on.** That could be a new change, or something that has gone on long enough to mention.

:::note One tank, one briefing
Each tank your plan covers gets its own briefing, and each one is only about that tank. See [Which tanks get a briefing](#availability).
:::

:::note Cora Max has its own Reef Buddy setting
Cora Max has a **Reef Buddy** section in its Settings too. Its **Briefing time** is the same setting as on your phone: change it on either one and both follow. The switch for the on-screen briefing belongs to that Cora Max only. Turning it off there doesn't stop the briefing reaching your phone.
:::

## Reading the scores

**Stability** shows how steady your readings have been over the last 30 days. It measures steadiness only. It doesn't check whether readings are in range, so a tank held steady at the wrong level can still score well. To see how you're doing against your target ranges, run a [Health Report](/help/mobile-icp-health#health-reports). Treat Stability as a trend to watch over time. Compare it with your own earlier scores, and not with someone else's tank.

**Data** shows how much recent information Cora had to work with. It drops when readings get old.

:::note A falling Data score usually means old readings
If you haven't tested anything for a week, the Data score drops and the Stability score becomes less reliable. Log some readings to bring both back up.
:::

## Which tanks get a briefing {#availability}

Reef Buddy is part of the paid plans. It's also included in the 30-day trial that starts when you create your account.

Each plan covers a set number of tanks: 1 on the trial and on Essential, 5 on Advanced and 20 on Expert. Briefings go to the first tanks in the order set in **Settings → Reorder tanks**. To include a tank that's missing out, move it up the list. Removed tanks don't take a place.

After the trial, a free account sees a locked Reef Buddy card with **See plans** where the briefing was, and gets no briefing notification. More in [Plans and subscriptions](/help/mobile-plans).

## If no briefing came

- **Nothing needed your attention.** Reef Buddy stays quiet on a good day. The card is still on the dashboard.
- **Your trial ended.** A free account gets the locked card and no notification.
- **The tank is past your plan's limit.** Move it up in **Settings → Reorder tanks**.
- **Notifications are off.** Check [Notifications](/help/mobile-notifications).

If you turned off **Allow Cora Assistant to use saved tank data**, the briefing still comes, but its summary is a plain fixed text and the AI-written observation is left out. See [Asking Cora](/help/mobile-assistant#consent).

## Correcting an insight

You can respond to each insight in one of four ways.

| Response | Means |
|---|---|
| **Confirmed** | It was right, and useful |
| **Doesn't match** | It doesn't match what you're seeing |
| **Already knew** | Right, but you were aware |
| **Not sure** | You can't judge it yet |

When Reef Buddy flags a drift, it also asks *Was this heads-up useful?* You can answer **Helpful**, **Not helpful**, **This change is expected** or **Reading looks wrong**. Your feedback shapes what shows up first in later briefings. Hiding an insight only lasts for a while. If the problem is still there, the insight comes back.

:::note Serious findings are never hidden
Feedback only quiets lower-severity insights. Warning and critical insights keep showing up, whatever you've answered before.
:::
