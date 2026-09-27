---
title: Dosing
description: Tell Cora what you dose so it can turn millilitres into a real change in your tank.
section: Cora Mobile
reviewed: 2026-09-27
order: 18
group: Records
---

Cora can only do dosing maths if it knows how strong your products are. Set that up once, and the calculator, consumption tracking and what Cora tells you about your dosing all use real numbers instead of guesses.

**Settings → Dosing Products.**

![Dosing products](img/mobile-dosing.webp "Products carry the strength Cora uses for dose and consumption calculations.")

## The product library

Cora comes with a library of common products. Search for yours and add it. Its strength comes with it.

Each product records how much it raises a parameter per millilitre (or per gram, for dry products) in a set volume of water. That's the number that turns "5 ml" into "+0.2 dKH in your tank".

A product can carry values for alkalinity, calcium, magnesium, nitrate or phosphate. A two-part carries one each. A balanced product carries several.

## Adding your own

If your product isn't in the library, add it as a custom product and enter its strength. It's almost always on the label, something like "1 ml per 100 litres raises alkalinity by 0.1 dKH".

:::warning Use the strength the manufacturer gives
If the strength is wrong, every dose Cora works out for that product is wrong by the same proportion. If you can't find the figure, leave the product out. Don't guess.
:::

Your tank's **salt mix** isn't a dosing product. You set it on the tank's profile, and Cora has a catalog of common reef salts with their published figures, with sources, to choose from. See [Tank profile](/help/mobile-tank-profile).

## The dose calculator

Once your products are set up, Cora can work out a correction using your tank's volume from its profile.

It works out **increases** for alkalinity, calcium and magnesium, and for nitrate or phosphate when you're raising them.

For **reductions** it gives you guidance instead of a dose. You can't dose a parameter down. The answer is a water change, a media change, or changing what you already dose.

:::warning Cora spreads big corrections over several days
Cora limits how far a parameter can move in a day and spreads a bigger correction over several days. One large dose is how a tank gets shocked, so the calculator won't suggest one.
:::

The volume you entered at setup matters here. If it's 20% out, the doses are 20% out too.

## Consumption

Once Cora can see both your doses and your readings, it can work out what your tank is using and tell you when that changes.

When demand changes, take a closer look before drawing a conclusion. Rising alkalinity demand often means growth, but a sudden move in either direction can also come from a missed dose, a testing error, precipitation, a water change or an equipment change. Check what else changed around that date.

## Dosing equipment

If you have a connected dosing unit, its heads show up as devices with their own readings, including what each head has left and what it's been dosing. See [Connecting your equipment](/help/mobile-connections).
