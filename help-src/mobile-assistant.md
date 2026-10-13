---
title: Asking Cora
description: Use Cora Assistant by typing or talking, what it can see, what it can do for you, the data sharing switch, and memory.
section: Cora Mobile
reviewed: 2026-10-13
order: 30
group: Intelligence
twin: max-voice
---

Cora Assistant answers questions about your tank in plain language, and can log things and run your equipment when you ask. It can see your live readings, your history and your lab results, so its answers are about *your* tank.

Open it from the **Assistant** tab.

![A Cora Assistant answer about alkalinity in Cora Mobile](img/mobile-assistant.webp "An answer built from the tank's live data, with this month's message count above the box.")

## Pick a tank first

The tank selector at the top sets what Cora is talking about. The questions you type and the answers you get all belong to that tank.

## Typing

Type in the box at the bottom and send. If you're not sure where to start, tap one of the **Try asking** suggestions. Some things worth asking:

- *"Why is my alkalinity falling?"*
- *"What changed since last week?"*
- *"Is my calcium where it should be for an SPS tank?"*
- *"When did I last do a water change?"*

To keep an answer, tap **Save to journal** under it. It goes into the tank's [journal](/help/mobile-journal).

## Talking

Tap **Start voice conversation** to talk back and forth. Cora listens, answers out loud and keeps listening until you stop it. It's handy when your hands are wet.

While Cora is speaking, tap **Tap to interrupt** to cut in. Tap **Stop conversation** when you're done.

## What Cora can do for you {#what-cora-can-change}

Besides answering, Cora can do things on the tank you picked. Ask in your own words.

| Ask for | For example |
|---|---|
| Log a test you did by hand | *"Log alkalinity 8.1"* |
| Write a journal entry | *"Note that the clownfish is hiding today"* |
| Log a feeding that wasn't the usual one | *"I skipped feeding this morning"* |
| Change an alert range | *"Set the nitrate alert to 2 to 10"* |
| Run one of your automations or scenes | *"Run the water change scene"* |
| Switch an Apex outlet or start a feed | *"Turn the skimmer off"*, *"Start Feed A"* |
| Start a Trident test | *"Start a Trident test"* |
| Dose from a DŌS head | *"Dose 5 mL from the iodine head"* |
| Control Red Sea and Jecod equipment | *"Pause the return pump"* |
| Remember something about your system | *"Remember that I dose two-part"* |

Cora only offers what the tank has. If there's no DŌS on the tank, it can't dose.

Logging a test, a journal entry or a feeding happens when you ask for it. Anything that changes your equipment or an alert range is different: Cora tells you exactly what it's about to change and waits for your yes. It won't act on an unclear instruction. If a command might have run but Cora couldn't confirm it, it says so. Check the equipment before you ask again.

Equipment control works away from home only when a Cora Max at the tank can reach the equipment. See [What works away from home](/help/mobile-multi-device#what-works-away-from-home).

:::note Beta equipment
Cora can also control GHL, HYDROS, Focustronic, Maxspect and EcoTech (Radion, VorTech and Versa) equipment. **Beta.** These integrations are in Beta and only open to Beta users. If you are not a Beta user you will not see them in **Add device**. To ask for Beta access, contact support.
:::

:::warning Cora advises. You decide
Check anything important with your own testing. Treat big changes the way you'd treat advice from anyone else, and sanity-check them before you act. The line under the message box says the same.
:::

## Consent

![Assistant consent](img/mobile-assistant-consent.webp "Two separate permissions, and the memory Cora keeps.")

The first time you open the dashboard, Cora asks **Enable Personalized Reef Guidance?** **Enable** turns on data sharing. **Not Now** leaves it off. If you use guided setup, its last page asks the same question.

You can change it any time in **Settings → Cora Assistant**, which has two separate switches.

- **Allow Cora Assistant to use saved tank data** has to be on for Cora Assistant to answer you. If it's off, Cora shows its consent screen again before your next message or voice conversation. The screen lists what Cora Assistant uses, and **Where your data goes** names the AI provider that writes the replies. **Agree & Continue** turns the switch back on and carries on. **Not now** sends nothing and keeps what you typed.
- **Contribute anonymized tank data** is covered in [Exporting your data and deleting your account](/help/mobile-data-export#contributing-anonymised-data).

### What the switch covers {#what-the-switch-covers}

**Allow Cora Assistant to use saved tank data** isn't only for chat. Every feature that sends your tank data to the AI needs it:

- Cora Assistant, typed or spoken, on your phone and on Cora Max
- ICP uploads and re-running an ICP analysis
- Lab results a lab or an email sends to you
- Health Reports
- Journal dictation and **Analyze** in the journal
- **Design with AI** for dashboards

With it off, the feature asks for your OK first. Reef Buddy briefings still come, but with a plain fixed summary and no AI-written observation. On Cora Max, voice shows *Voice needs your OK* until you turn the switch on in Cora Mobile.

## The language Cora replies in

Cora Assistant uses your account language. That's the one language for the whole household, set in **Settings → Language**. Cora Assistant has no language setting of its own. Change it there, and from your next conversation Cora Assistant writes and speaks in the new language. More in [Cora Mobile settings](/help/mobile-settings#language).

## What Cora can see

The chip above the message box, **Using your tank's live data**, shows what's in scope. Tap it to see what Cora is reading: current values and how old each one is, recent history, your journal and your ICP results.

If your controller can't be reached, the chip says **Live controller offline: using saved data**. Cora then works from the last readings it has.

Cora Assistant can look back over about six months of a parameter's history. So you can ask *"Compare the last six months of my magnesium with my latest ICP."*

:::note It tells you how old the data is
Cora reports the age of the readings it uses. If your latest alkalinity reading is four days old, the answer says so and doesn't pass it off as current.
:::

## Memory

![Settings, Cora Assistant in Cora Mobile](img/mobile-assistant-settings.webp "The two data switches, AI memory, Answering device and Share Cora's analysis with labs.")

Cora remembers things about your tank from one conversation to the next. For example, that you dose two-part, that your frag tank shares a sump, or that you're trying to bring nutrients up. You don't have to explain your system every time.

**Settings → Cora Assistant → AI memory** shows what Cora has recorded about your tank and lets you reset it. Each tank has its own memory, so pick the tank first. The row only shows while **Allow Cora Assistant to use saved tank data** is on.

:::note What clearing memory touches
Clearing removes what Cora has remembered *about your conversations* for one tank. That's its profile of your system, the concerns it was tracking, and every stored session. If any part of that can't be removed, Cora Mobile tells you it failed.

Your **tank data** stays as it is. Clearing memory doesn't remove readings, journal entries, livestock, maintenance or reports.
:::

:::warning Your recent messages stay
The reset doesn't delete the messages you've exchanged with Cora. For about half an hour afterwards, Cora can still see the last few of them when you carry on talking.
:::

## Usage

Your plan includes a monthly allowance of messages. The count sits above the message box. Voice conversations have their own monthly count, and each spoken reply also uses messages. When you run out, Cora shows *You've hit your message limit* with the plans you can move to. The numbers for each plan are in [Plans and subscriptions](/help/mobile-plans).

## If an answer looks wrong

Correct it in the conversation. That's the quickest fix and it usually sticks, though it may not last forever.

If an answer sounds sure of itself but wrong, check the data chip first. Often the answer is right about the data Cora was given. The real problem is a stale reading, or a source assigned to the wrong tank.

Rate an answer with the thumbs under it. A thumbs down asks *What was wrong with it?* Pick a reason, such as **Wrong** or **Missed my tank**, and tap **Send rating**. That's what helps us fix it.
