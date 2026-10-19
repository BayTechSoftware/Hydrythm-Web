---
title: Prises et commandes
description: Commandez les prises Apex depuis Cora Max, lancez ou annulez le mode nourrissage, utilisez le tiroir Prises et nourrissage, et ce que veulent dire Auto, Off et On.
section: Cora Max
reviewed: 2026-10-13
order: 5
group: Equipment
---

Cette page explique comment commander les prises et lancer le mode nourrissage depuis Cora Max. Vous pouvez le faire depuis les tuiles de prises du tableau de bord, depuis le tiroir **Prises et nourrissage**, ou par la voix.

:::warning Ces commandes agissent sur votre aquarium
On ne peut pas annuler. Les prises avec un cadenas vous demandent d’abord de confirmer. Les autres changent dès que vous touchez. Une commande peut revenir **Confirmé**, **Non confirmé** (envoyé, mais rien n’est revenu), **Refusé** ou **Aucun changement**. Plus de détails dans [Contrôler votre équipement](/help/mobile-device-control).
:::

## Les trois états {#the-three-states}

Chaque prise est dans l’un de ces trois états.

**Auto** rend la prise à sa programmation Apex. La plupart du temps, c’est là qu’une prise doit être.

**Off** et **On** sont des forçages manuels. Ils agissent tout de suite et **restent en place jusqu’à ce que vous les changiez**. Ils n’expirent pas, et rien ne les annule à votre place.

:::warning Un forçage manuel n’expire pas
Remettez la prise sur **Auto** quand vous avez fini, car rien d’autre ne le fera. Un forçage n’est pas un verrou pour autant. Vous, votre voix ou une automatisation pouvez encore le changer plus tard.
:::

## Depuis le tableau de bord {#switching-from-the-dashboard}

Les tuiles de prises affichent les trois états, avec l’état actuel mis en avant. Touchez celui que vous voulez.

Certaines prises ont un **cadenas**. Il veut dire que la prise vous demande de confirmer avant de changer, pour qu’un appui par erreur ne puisse pas couper un équipement essentiel. Quand vous la touchez, une fenêtre affiche la prise, son état actuel, le forçage que vous allez appliquer et ce qu’il peut faire à l’aquarium. Il n’y a pas de verrou à désactiver ailleurs.

Par défaut, le cadenas est sur les chauffages, les groupes froids, les pompes de remontée, l’osmolateur (ATO), les nourrisseurs et toute prise que Cora ne sait pas classer. L’éclairage, les écumeurs, les pompes de brassage, les pompes doseuses, les réacteurs, les UV et les ventilateurs changent d’un seul appui.

## Le tiroir Prises et nourrissage {#the-controls-drawer}

Vous ne le voyez que sur un aquarium équipé d’un Neptune Apex. Touchez la petite étiquette **Prises et nourrissage** en bas du tableau de bord, ou balayez vers le haut n’importe où sur le tableau de bord. Cela ouvre **Commandes**, avec **NOURRISSAGE** en haut et **PRISES** en dessous.

![Le tiroir Commandes](img/max-controls.webp "Les cycles de nourrissage en haut, puis les prises choisies pour ce tableau de bord.")

Il affiche les prises et les cycles de nourrissage que vous avez choisis sous **Prises et nourrissage** dans l’[éditeur du tableau de bord](/help/max-dashboard-editing#outlets-feed), ou tous s’il n’y en a aucun de choisi. Les prises avec un cadenas demandent aussi une confirmation ici. Les prises d’autres contrôleurs se commandent depuis la page de leur appareil, voir [Contrôler l’équipement depuis Cora Max](/help/max-device-control).

Si un appui sur une prise revient avec *L’Apex n’a pas répondu : l’action a peut-être été appliquée*, vérifiez la prise avant de réessayer.

## Mode nourrissage {#feed-mode}

Le mode nourrissage est la façon sûre de couper le brassage pendant que vous nourrissez. Votre Apex met en pause l’équipement qui doit l’être, laisse le reste tranquille, et **remet tout en marche tout seul** à la fin du temps.

Utilisez-le plutôt que d’éteindre les pompes à la main. Il remet le système en route même si vous oubliez.

Les cycles de nourrissage sont Feed A, Feed B, Feed C et Feed D, affichés **A**, **B**, **C** et **D** sous **NOURRISSAGE**. Ce sont les cycles programmés sur votre Apex, et chacun peut mettre en pause un groupe d’équipements différent. Choisissez celui qui correspond à ce que vous faites. **Annuler** arrête un cycle en cours avant la fin et remet tout en marche aussitôt.

Lancez-en un depuis le tiroir, ou dites *« démarre le mode nourrissage »*.

Si Cora Max indique que l’Apex n’a pas répondu, le nourrissage est peut-être déjà en cours. Vérifiez la pompe de remontée avant de le relancer.

## Par la voix {#by-voice}

Vous pouvez commander les prises à la voix, par exemple *« éteins l’écumeur »* ou *« remets le ventilateur en auto »*.

Avant que quoi que ce soit n’atteigne votre équipement, Cora **vérifie d’abord avec vous**. Il vous dit ce qu’il va faire et attend votre accord. S’il n’est pas sûr de ce que vous avez demandé, il ne fait rien.

Plus de détails dans [Parler à Cora](/help/max-voice).

## Voir ce qui s’est passé {#seeing-what-happened}

Chaque demande est enregistrée, avec ce qui l’a demandée et comment elle s’est passée, qu’elle vienne de Cora Mobile, d’un Cora Max, de la voix, de l’Assistant ou d’une automatisation. Sur Cora Max, touchez le nom de l’aquarium dans la barre du haut et choisissez **Activité**. Sur votre téléphone, c’est dans **Paramètres → Activité**. Plus de détails dans [Activité sur Cora Max](/help/max-activity).

Quand quelque chose a changé sans que vous sachiez pourquoi, regardez là en premier.
