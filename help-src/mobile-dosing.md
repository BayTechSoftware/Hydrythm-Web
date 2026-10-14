---
title: Dosing products and the dose calculator
description: Check the strength of your alkalinity, calcium and magnesium products, add your own, and use the dose calculator to work out how much to add.
section: Cora Mobile
reviewed: 2026-10-13
order: 27
group: Records
---

Cora can only do dosing maths if it knows how strong your products are. This page covers the product list and the dose calculator that uses it.

Go to **Settings → Dosing Products**.

![Dosing products](img/mobile-dosing.webp "Products carry the strength Cora uses for dose and consumption calculations.")

## The product library {#the-product-library}

The **Dosing products** screen already lists common products, grouped under **Alkalinity (dKH)**, **Calcium (ppm)** and **Magnesium (ppm)**. Find yours and tap it to check its strength.

Each strength is how much 1 ml (or 1 g of a dry product) raises the parameter in a set volume of water. That's the number that turns "5 ml" into "+0.2 dKH in your tank". Switch between **per 100 L** and **per 100 gal** at the top.

Only change a built-in strength if your bottle says something different. Tap the product to open **Adjust strength**. **Reset to default** puts Cora's figure back.

## Adding your own {#adding-your-own}

If your product isn't listed, tap **+** (**Add custom product**). Give it a **Product name**, choose **Liquid (ml)** or **Dry (g)**, and fill in its strength for alkalinity, calcium or magnesium. Leave a field blank if the product doesn't move it. A two-part fills in one each, a balanced product several.

The strength is almost always on the label, something like "1 ml per 100 litres raises alkalinity by 0.1 dKH".

:::warning Use the strength the manufacturer gives
If the strength is wrong, every dose Cora works out for that product is wrong by the same proportion. If you can't find the figure, leave the product out. Don't guess.
:::

Nitrate and phosphate products come from Cora's own list in the calculator. You can't add them here.

Your tank's **salt mix** isn't a dosing product. You set it on the tank's profile, and Cora has a catalog of common reef salts with their published figures, with sources, to choose from. See [Your tank profile](/help/mobile-tank-profile).

## The dose calculator {#the-dose-calculator}

The calculator works out how much product it takes to bring a parameter up to its target. It's there for alkalinity, calcium, magnesium, nitrate and phosphate.

1. On the dashboard, tap the parameter's widget to open it.
2. Tap the calculator icon at the top. A dot on it means the reading is below target.
3. Check the numbers Cora filled in:
   - Current is your latest reading. Update it if you've just tested.
   - Target is the middle of your alert range for that parameter, or the typical reef range if you haven't set one.
   - **Net water volume (L)** is 90% of your tank's volume, to allow for rock and sand. Change it if you know the real figure.
4. Pick the **Product**. Your own products from the tank profile come first, then brand presets. You can also enter a **Custom strength**.

Cora shows the total needed to reach the target.

:::warning Spread a big correction out
The calculator gives the total, not a daily dose. If the total is a bigger jump than is safe in a day, it says so, and you split it over several days. **Ask Cora** opens Cora Assistant with your numbers, if you want help planning how much per day.
:::

When you've dosed, tap **Log the dose you gave**. It adds an entry to your [journal](/help/mobile-journal).

If you're already at or above the target, the calculator tells you there's nothing to add. You can't dose a parameter down. The answer is a water change, a media change, or changing what you already dose.

The volume matters here. If it's 20% out, the doses are 20% out too.

## Consumption {#consumption}

Once Cora can see both your doses and your readings, it can work out what your tank is using and tell you when that changes.

When demand changes, take a closer look before drawing a conclusion. Rising alkalinity demand often means growth, but a sudden move in either direction can also come from a missed dose, a testing error, precipitation, a water change or an equipment change. Check what else changed around that date.

## Dosing equipment {#dosing-equipment}

If you have a connected doser, such as a Neptune DŌS or a Red Sea ReefDose, its heads show up with their own readings, including what each head has left and what it's been dosing. How to run and refill them is in [Controlling your equipment](/help/mobile-device-control), and their low-container and missed-dose alerts are in [Doser alerts](/help/mobile-device-control#doser-alerts).

An automation can also dose from a DŌS head, capped at 10 mL per head per day. See [Automations and scenes](/help/mobile-automation#actions).
