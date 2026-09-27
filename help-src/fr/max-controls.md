---
title: Prises et commandes
description: Commuter des prises depuis Cora Max, utiliser le mode nourrissage, et ce que signifie réellement Auto.
section: Cora Max
reviewed: 2026-09-09
order: 5
group: Equipment
---

Cora Max peut commuter l’équipement de votre système : depuis les widgets de commande sur le tableau de bord, depuis le tiroir Prises et nourrissage, ou par la voix.

:::warning Ces commandes agissent sur votre aquarium
Il n’y a pas d’annulation. Les prises marquées d’un cadenas vous demandent de confirmer d’abord ; le reste s’applique dès que vous touchez. Une commande peut revenir **Confirmée**, **Non confirmée** (envoyée, rien signalé en retour), **Refusée** ou **Aucun changement** ; voir [Contrôler votre équipement](/help/mobile-device-control).
:::

## Les trois états

Chaque prise est dans l’un de trois états.

**Auto** remet la prise à sa programmation Apex. C’est là qu’une prise devrait se trouver la plupart du temps.

**Éteint** et **Allumé** sont des dérogations manuelles. Elles prennent effet immédiatement et **restent jusqu’à ce que vous les changiez à nouveau**. Elles n’expirent pas, et rien ne les remet en place pour vous.

:::warning Une dérogation manuelle n’expire pas
Remettez-la sur **Auto** quand vous avez terminé ; rien ne le fait pour vous. Elle peut encore être changée plus tard par vous, par la voix, ou par une automatisation ; une dérogation n’est pas un verrou.
:::

## Commuter depuis le tableau de bord

Les widgets de commande affichent les trois états avec celui actuel mis en évidence. Touchez l’état que vous voulez.

Certaines prises portent un **cadenas**. Il n’a pas besoin d’être désactivé ailleurs ; il signifie que la prise vous demande de confirmer avant de changer, pour qu’un appui accidentel ne puisse pas commuter quelque chose de critique. Voir ci-dessous.

## Le tiroir Commandes

Tirez l’onglet en bas du tableau de bord pour ouvrir **Commandes** : chaque prise du système au même endroit, qu’elle ait un widget ou non, plus les cycles de nourrissage.

![Le tiroir Commandes](img/max-controls.webp "Cycles de nourrissage en haut, puis chaque prise.")

Une prise portant un **cadenas** nécessite une confirmation explicite avant de changer. La toucher ouvre une boîte de dialogue nommant la prise, son état actuel, et la dérogation que vous êtes sur le point d’appliquer. C’est une étape de confirmation, pas un verrou à désactiver ailleurs.

## Mode nourrissage

Le mode nourrissage est la façon sûre de mettre le débit en pause pour le nourrissage. Il met en pause l’équipement qui doit l’être, laisse tranquille l’équipement qui ne doit pas l’être, et **remet tout en place lui-même** quand le temps est écoulé.

Utilisez-le de préférence à éteindre les pompes à la main, car il restaure le système sans dépendre du fait que vous vous en souveniez.

Les cycles de nourrissage sont désignés par les lettres **A**, **B**, **C** et **D** : les cycles que votre contrôleur définit, chacun mettant en pause un ensemble différent d’équipement. Choisissez celui qui correspond à ce que vous faites. **Annuler** termine un cycle en cours plus tôt et restaure tout immédiatement.

Démarrez-en un depuis le tiroir Commandes, ou dites *« démarrer le mode nourrissage »*.

## Par la voix

Vous pouvez commuter des prises par la voix : *« éteins l’écumeur »*, *« remets le ventilateur en auto »*.

Tout ce qui atteint votre équipement est **confirmé avant que cela n’arrive** : Cora vous dit ce qu’il est sur le point de faire et attend que vous soyez d’accord. Il n’agira pas sur une instruction dont il n’est pas sûr.

Voir **[Parler à Cora](/help/max-voice)**.

## Voir ce qui s’est passé

Chaque demande est enregistrée, avec ce qui l’a demandée (cette application, un écran Cora, la voix, l’Assistant, une règle d’automatisation, un bouton intelligent ou votre compte) et comment elle a voyagé. Sur votre téléphone, c’est **Réglages → Activité**.

C’est le premier endroit à regarder quand quelque chose a changé et que vous ne savez pas pourquoi.
