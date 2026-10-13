---
title: ICP and health reports
description: Upload an ICP test PDF or have your lab send it, read the score, track each element over time, and run a Health Report of your whole system.
section: Cora Mobile
reviewed: 2026-10-13
order: 31
group: Intelligence
twin: max-intelligence
---

The **Intelligence** tab is where your lab results and long-term reports live. Pick a tank at the top first. Everything on the screen belongs to that tank.

![The Intelligence tab](img/mobile-intelligence.webp "Upload ICP, run a health report, and see what moved since the last one.")

## Uploading an ICP test

Cora reads the PDF report your lab sends you. Download it from your lab's email or website first. Photos, scans and screenshots can't be read.

1. Tap **Upload ICP**.
2. Pick your lab, or leave it on **Auto: detect the lab**. Cora has tips for ATI, Fauna Marin, Modern Reef, Oceamo, Reef Zlements and Triton.
3. Say what the sample is: **Aquarium water**, **RO/DI water**, **Salt mix** or **Other**. Only aquarium water updates your dashboard and alerts.
4. Check the date the sample was taken. Labs print the date they analysed it, so Cora asks for yours and charts the results against it.
5. Tap **Choose PDF** and pick the file.

It usually takes one to two minutes. Keep the screen open and the report opens as soon as it's ready. You don't have to type anything.

You can also email the PDF to **icp@in.coraiq.tech**. Send it from your sign-in email or a verified lab email (see below), and it arrives like a result from a lab.

If you upload the same report twice, Cora shows you the one you already have and doesn't charge you again.

:::note Cora needs your OK first
ICP analysis sends the report to the AI, so it needs **Allow Cora Assistant to use saved tank data**. If that's off, Cora asks before the upload. See [what the switch covers](/help/mobile-assistant#what-the-switch-covers).
:::

## Which email a lab can use

A lab or an emailed result finds your account by the email address it knows. That is your sign-in email, plus any lab email you add under **Settings → your account card (Account & Subscription) → Lab & ICP emails**.

1. Tap **Add lab email** and type the address your lab uses.
2. Tap **Send code**. Cora sends a 6-digit code to that address. It expires in 10 minutes.
3. Enter the code and tap **Verify**. If you didn't get it, tap **Resend code**.

You can add up to 3 lab emails. Each shows **Verified** or **Waiting for code**, and **Remove** takes one off. After that, results sent to it no longer reach your account. An address that already belongs to another Cora account can't be added.

If you signed in with a hidden Apple email, labs can't find your account. The ICP screen shows a card, **Get lab results automatically**, that takes you to this setting. When you sign in with Apple, choose **Share My Email** to avoid the problem.

## Send to Cora: results a lab or an email delivers for you

Some labs can send a result straight to Cora, and an ICP PDF you email in arrives the same way. You don't have to upload anything yourself.

If you have one tank, a result from a lab you trust, or one you emailed in, goes straight to that tank. With more than one tank, you'll see a banner: *"Lab result from {lab} is waiting."* Tap **Choose tank** and pick the tank it belongs to. Cora can't work that out on its own.

The report shows **Sent by {lab}** near the top, or **Received by email**, so you can tell it from one you uploaded.

If **Allow Cora Assistant to use saved tank data** is off, the result waits with the message *Cora Assistant needs your OK to read it.* Give your OK and it comes in.

:::note The first time
The first time a result arrives this way, Cora shows a short hint about what's going on, so it doesn't look like an error.
:::

### The first result from a new lab

The first time a lab sends you a result, Cora asks you to approve it before adding it anywhere, even if you only have one tank. You'll see who sent it and can tick **Trust this lab** to skip this check next time a result comes from them.

Tap **Approve** to bring it in, or **Decline** to delete it without adding it to any tank.

### Trusted labs and what labs can see {#trusted-labs}

**Settings → Cora Assistant → Trusted labs** lists every lab you've trusted. The list shows up once you've trusted at least one. **Revoke** removes a lab, so its next result needs your approval again.

**Share Cora's analysis with labs**, on the same screen, decides what a lab sees after it sends you a result. On, it can see Cora's scores and written analysis. Off, it only sees that the result was delivered. It's off until you turn it on. The same switch also shows on a report a lab sent you.

If something here doesn't work, see [Troubleshooting](/help/troubleshooting).

## What you get back

![An ICP report](img/mobile-icp-report.webp "Each report carries a score and a summary written for your tank.")

You get a score out of 100 and a plain-language summary of what it means for your system, taking in your tank type, its age and your livestock.

The score compares your results with their target ranges, including any ranges you've set yourself. If any result is outside its range, the score can't go above 70, so it can't read **Healthy**. If one is far outside, it can't go above 40, however good the rest are. The label under the score reads **Healthy** from 71 to 100, **Needs Attention** from 40 to 70 and **Critical** from 0 to 39. Health Reports are scored the same way.

Every element is tracked, including trace elements and contaminants as well as the main parameters. Cora records all 71 elements a lab can report, and the line some labs call *Acidity* is pH.

On each element row you'll see the range the lab printed, shown as *Lab range*, next to Cora's own range for that element. An element Cora has no reference range for carries the tag **No Cora range**. The report says how many elements have a Cora range and assesses the rest from general reef knowledge. Cora Assistant comments on every element that was tested, and its comment stands even when there's no Cora range.

If the lab prints *n.d.*, or *not detected*, for an element, Cora records it as 0 and says it wasn't detected.

:::note Dissolved CO2 is not room CO2
**Dissolved CO₂** in an ICP report is the CO2 in the water, in mg/L. It is a different reading from the CO2 of the air in your room, which an Inkbird room air monitor measures. The two have different ranges and are never mixed. **Beta.** Inkbird is in Beta and only open to Beta users. If you are not a Beta user you will not see it in **Add device**. To ask for Beta access, contact support.
:::

The **Since your last ICP** card shows what changed most since last time. It's usually the quickest way into a new report.

Tap **Trends** to see any element across every test you've uploaded. This is where ICP becomes really useful.

:::tip The second test is where it gets interesting
One ICP tells you where you are. The second tells you which way you're heading, and that's what you can act on. Test on a regular rhythm, and don't wait for something to go wrong.
:::

## An RO/DI or source-water test

If you upload RO/DI or other source water, pick **RO/DI water** when you upload. Cora doesn't score it against your tank's targets. It gives a plain verdict on whether the water is clean enough to use, and it keeps those numbers out of your tank readings. It's saved as a separate report. Cora does the same for **Salt mix** or **Other**: it says what the sample looks like and doesn't score it as your tank.

## Health reports

A **Health Report** is a deeper check of the whole system, done from time to time. It looks at every parameter, every source, your dosing, your history and your recent ICP results together.

Tap **Health Report**, then **Generate**. It usually takes about twenty seconds. Like ICP analysis, it needs **Allow Cora Assistant to use saved tank data**.

Use it when you want a careful look at the tank. Good times are before a big change, after a problem, or every few weeks as a check-in.

An open report has buttons at the top to export it as a PDF, share a snapshot of the tank, or delete it.

## ICP against your probes

Cora compares your lab results with what your equipment reports. If your alkalinity probe says 8.4 and your ICP says 7.6, you'll want to know, and Cora shows you without quietly picking one.

This is one of the most useful things an ICP does in Cora. Treat it as a **third opinion**. It isn't the final word. Labs differ, and how a sample is handled, stored and shipped all move the result. A single ICP is evidence, and two tests that agree count for much more than one. If the gap persists, check the probe. It doesn't prove the probe is wrong.

:::tip Changing labs or test methods
If you change labs, or switch between a lab's ICP-OES and ICP-MS tests, your results can move even though nothing changed in your tank. Cora points this out when it compares them. ICP-OES can't measure very low chromium, tin, nickel, copper, cobalt or selenium. So a **Below detection** result for those on an ICP-OES test doesn't mean your tank has none.
:::

## Your allowance

Your plan sets how many ICP analyses and Health Reports you get each month. The line under the buttons shows what you've used. The numbers for each plan are in [Plans and subscriptions](/help/mobile-plans).

When your ICP analyses are used up, Cora first shows the plans you can move to. If you'd rather not upgrade, it asks **Save results without the AI analysis?** Tap **Save my results** and Cora still reads the report and saves every value, so trends, history and your readings update as normal. The score and the written analysis stay locked. You can run them later from the report itself once you have an ICP analysis to spend.

On top of your plan's limit, Cora accepts up to 10 ICP uploads a day. An upload turned down for that reason doesn't use up any of your plan's ICP analyses. Cora Mobile only shows a general upload error, though, so if uploads start failing after a lot in one day, try again tomorrow.

## Where reports live

The Intelligence screen keeps the two kinds apart. Lab results are under **ICP REPORTS** and generated reviews under **HEALTH REPORTS**. Each list shows the newest first, with its score. Tap one to open it again in full.

You can also get to them from **Settings**: open a tank, then **ICP Reports** or **Health Reports**.
