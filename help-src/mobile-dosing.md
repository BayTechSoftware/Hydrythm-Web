---
title: Dosing
description: Tell Cora what you dose so it can turn millilitres into an actual change in your tank.
section: Cora Mobile
order: 17
---

Cora can only do dosing maths if it knows how strong your products are. Set that up once and everything downstream — the calculator, consumption tracking, and what Cora tells you about your dosing — becomes real numbers rather than guesses.

**Settings → Dosing Products.**

![Dosing products](img/mobile-dosing.webp "Products carry the strength Cora uses for dose and consumption calculations.")

## The product library

Cora ships with a library of common products. Search for yours and add it — the strength comes with it.

Each product records how much it raises a parameter per millilitre (or per gram, for dry products) in a fixed volume of water. That is the number that turns "5 ml" into "+0.2 dKH in your tank".

Products can carry alkalinity, calcium, magnesium, nitrate or phosphate values — a two-part carries one each, a balanced product several.

## Adding your own

If your product is not in the library, add it as a custom one and enter its strength. The manufacturer's label almost always states it — "1 ml per 100 litres raises alkalinity by 0.1 dKH", or similar.

:::warning Enter the manufacturer's stated strength
An incorrect strength makes every dose calculation for that product wrong by the same proportion. If the figure is not available, leave the product out rather than estimating.
:::

## The dose calculator

With products set up, Cora can calculate a correction using your tank's actual volume from its profile.

It calculates **increases**: alkalinity, calcium, magnesium, and nitrate or phosphate when you are raising them.

For **reductions** it gives guidance rather than a dose — you cannot dose a parameter downward, and the answer is a water change, a media change or a change in what you are already dosing.

:::warning Large corrections are spread, not dosed at once
Cora caps how much a parameter may be moved in a day and spreads a bigger correction over several. A single large dose is how a tank gets shocked; the calculator will not propose one.
:::

The volume you entered at setup matters here. A stated volume 20% out gives dose figures 20% out.

## Consumption

Once Cora can see both your doses and your readings, it can work out what your tank is actually consuming, and tell you when that changes. A tank whose alkalinity demand climbs is usually a tank that is growing; one whose demand drops suddenly is usually a tank with a problem.

## Dosing equipment

If you have a connected dosing unit, its heads appear as devices with their own readings — what each head has left, and what it has been dosing. See **[Connecting your equipment](/help/mobile-connections)**.
