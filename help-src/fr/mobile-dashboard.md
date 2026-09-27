---
title: Lire votre tableau de bord
description: Les widgets du tableau de bord Cora, l’âge des mesures, leurs sources et le sens des couleurs.
section: Cora Mobile
reviewed: 2026-09-09
order: 5
group: Your dashboard
---

Le tableau de bord est une grille de **widgets**. Chacun affiche une information sur un aquarium. Vous choisissez librement ce qui s’y trouve, comme expliqué dans **[Modifier votre tableau de bord](/help/mobile-dashboard-editing)**.

![Un tableau de bord Cora Mobile](img/mobile-dashboard.webp "Jauges, chiffres, tendances et commandes sur un seul écran.")

## L’en-tête de l’aquarium

En haut de chaque tableau de bord, vous trouvez :

- **le nom de l’aquarium**, avec un petit symbole à côté. Ce symbole sert uniquement à **renommer rapidement** l’aquarium
- **Nourrir**, qui met en pause le brassage et l’écumage le temps du nourrissage, puis remet tout en marche
- **Reef Buddy**, qui ouvre le briefing du matin
- **Partager**, qui envoie une capture du tableau de bord
- **le crayon à droite**, qui ouvre [le profil de l’aquarium](/help/mobile-tank-profile)

:::note Trois boutons proches, trois écrans différents
Le symbole près du nom renomme l’aquarium. Le crayon à droite ouvre le **profil** de l’aquarium. Pour modifier le tableau de bord lui-même, c’est encore ailleurs : touchez **Modifier le tableau de bord**, tout *en bas*, sous les widgets.
:::

Si vous avez plusieurs aquariums, balayez l’écran vers la gauche ou la droite pour passer de l’un à l’autre.

## La carte Reef Buddy

Sous l’en-tête, une carte résume le dernier briefing : un titre, les scores **Stabilité** et **Données**, et le nombre d’observations. Touchez-la pour lire le briefing complet, ou fermez-la avec **×**. Une nouvelle carte arrive avec le briefing suivant.

## Lire un widget de paramètre

Un widget qui affiche un **paramètre mesuré** montre toujours les trois mêmes éléments, aux mêmes endroits. Les tuiles d’appareils et de commandes (une prise, une unité de dosage, une pompe) affichent leur état, car il n’y a pas une mesure unique derrière.

**La valeur**, c’est la mesure elle-même, en grand au centre.

**L’âge** est juste dessous ou à côté : `maintenant`, `1 h`, `2 j`. Il indique quand la mesure a été prise, pas quand l’écran s’est actualisé. Un chiffre qui n’a pas bougé depuis deux jours affiche `2 j`, et c’est une information en soi.

**Le badge de source** est la petite marque à côté de l’âge. Il indique d’où vient le chiffre : une sonde, un contrôleur, un résultat de laboratoire, ou vous avec un test en kit. Touchez un widget pour voir la source en toutes lettres avec son historique récent.

:::note Pourquoi l’âge compte autant
Une mesure d’alcalinité parfaite vieille de quatre jours ne dit rien de l’alcalinité actuelle. L’âge est affiché à côté de chaque valeur pour que vous voyiez la différence d’un coup d’œil.
:::

## Couleurs

Cora utilise peu de couleurs, et chacune veut toujours dire la même chose.

| Couleur | Signification |
|---|---|
| Vert | Bien dans la plage de ce paramètre |
| Orange | Près d’une limite. **En général encore dans la plage**, dans son dernier dixième |
| Rouge | Au-delà de la limite. Il vaut la peine d’agir |
| Gris | Pas d’avis : pas de mesure récente, ou pas de plage utilisable pour juger |

:::note L’orange veut souvent dire « encore bon, mais ça bouge »
L’orange est une *marge*, pas un dépassement. Une mesure dans sa plage mais dans les derniers 10 % passe volontairement à l’orange. Vous voyez ainsi une dérive quand il est encore temps d’agir, avant qu’elle devienne un problème.

Il y a deux nuances.

Une plage que vous avez réglée vous-même compte comme une limite ferme. Si la mesure la franchit, le widget passe directement au rouge, sans marge orange, puisque c’est vous qui avez tracé cette limite. Une plage **fournie par Cora** est une référence plus souple. Au-delà de la limite, le widget reste orange sur les premiers 10 %, puis passe au rouge.

Une limite dans un seul sens (un plafond pour un contaminant, un plancher pour un nutriment) n’est jugée que sur son bord haut. Du cuivre à zéro s’affiche donc en vert. Il ne passe pas à l’orange parce qu’il est en bas de l’échelle.
:::

Un widget entouré d’orange ou de rouge demande votre attention. Le contour entoure tout le widget. Il reste donc visible quand vous faites défiler.

## Sous les widgets

![Le bas du tableau de bord](img/mobile-dashboard-foot.webp "Modifier le tableau de bord, Enregistrer les paramètres, et raccourcis vers les quatre zones d’enregistrement.")

En bas du tableau de bord :

- **Modifier le tableau de bord** ouvre l’[éditeur de tableau de bord](/help/mobile-dashboard-editing)
- **Enregistrer les paramètres** sert à saisir à la main les résultats de vos tests en kit
- **Journal · Alertes · Entretien · Population** mènent à ces pages pour cet aquarium

Juste au-dessus, une ligne indique la dernière mise à jour du tableau de bord et les sources utilisées.

## Toucher pour en savoir plus

Touchez un widget pour ouvrir son détail : l’historique complet en graphique, toutes les sources qui ont fourni ce paramètre et les seuils en vigueur. Depuis cet écran, vous pouvez saisir une nouvelle mesure, changer la plage ou remonter plus loin dans le temps.

## Si un widget reste vide

Un widget affiche une valeur dès qu’il en reçoit une. S’il est vide, c’est en général pour l’une de ces raisons :

- l’appareil est hors ligne. Regardez l’onglet **Appareils**
- le paramètre n’a pas encore de source. Saisissez-le à la main, ou connectez un équipement qui le mesure
- rien n’a encore jamais été mesuré ni saisi pour ce paramètre

Une mesure ancienne ne disparaît pas quand elle est plus vieille que la période du graphique. Elle reste sur le widget avec son âge. Une valeur périmée apparaît donc comme périmée, et non comme absente.

Pour les autres cas, consultez **[Résolution de problèmes](/help/troubleshooting)**.
