---
title: Lire votre tableau de bord
description: Comment lire le tableau de bord de Cora : widgets, fraîcheur, sources, et ce que signifient les couleurs.
section: Cora Mobile
reviewed: 2026-09-09
order: 5
group: Your dashboard
---

Le tableau de bord est une grille de **widgets**, chacun montrant une chose à propos d’un aquarium. Ce qui s’y trouve dépend entièrement de vous ; voir **[Modifier votre tableau de bord](/help/mobile-dashboard-editing)**.

![Un tableau de bord Cora Mobile](img/mobile-dashboard.webp "Jauges, chiffres, tendances et commandes sur un seul écran.")

## L’en-tête de l’aquarium

En haut de chaque tableau de bord :

- **Le nom de l’aquarium**, avec un petit symbole à côté : celui-là est un **renommage rapide**, rien de plus
- **Nourrir** : met en pause le débit et l’écumage pour un nourrissage, puis remet tout en place
- **Reef Buddy** : ouvre le briefing de ce matin
- **Partager** : envoie un instantané du tableau de bord
- **Le crayon à droite** : ouvre [le profil de l’aquarium](/help/mobile-tank-profile)

:::note Trois commandes similaires, trois destinations
Le symbole près du nom renomme l’aquarium. Le crayon à droite ouvre le **profil** de l’aquarium. Modifier le tableau de bord lui-même n’est ni l’un ni l’autre ; c’est **Modifier le tableau de bord**, au *bas* du tableau de bord, sous les widgets.
:::

Avec plus d’un aquarium, glissez latéralement pour passer de l’un à l’autre.

## La carte Reef Buddy

Sous l’en-tête, une carte résume le briefing le plus récent : un titre, ses scores **Stabilité** et **Données**, et le nombre d’observations. Touchez-la pour ouvrir le briefing complet, ou fermez-la avec **×**. Une nouvelle carte apparaît avec le prochain briefing.

## Comment lire un widget de paramètre

Un widget qui affiche un **paramètre mesuré** porte les mêmes trois choses aux mêmes endroits. Les tuiles d’appareil et de commande (une prise, une unité de dosage, une pompe) affichent leur propre état à la place, car il n’y a pas de mesure unique derrière elles.

**La valeur** est la mesure elle-même, grande et centrale.

**L’ancienneté** se trouve dessous ou à côté : `now`, `1h`, `2d`. C’est depuis combien de temps la mesure a été prise, pas depuis quand l’écran s’est actualisé. Un chiffre qui n’a pas bougé depuis deux jours affiche `2d`, et c’est une information.

**Le badge de source** est la petite marque à côté de l’ancienneté. Il vous dit d’où vient le chiffre : une sonde, un contrôleur, un résultat de laboratoire, ou vous avec un test en kit. Touchez n’importe quel widget pour voir la source détaillée avec son historique récent.

:::note Pourquoi l’ancienneté compte autant
Une mesure d’alcalinité parfaite datant de quatre jours n’est pas une mesure d’alcalinité actuelle. L’ancienneté se trouve à côté de chaque valeur pour que vous puissiez faire la différence d’un coup d’œil.
:::

## Couleurs

Cora utilise la couleur avec parcimonie, et toujours pour signifier la même chose :

| Couleur | Signification |
|---|---|
| Vert | Confortablement dans la plage pour ce paramètre |
| Orange | Proche d’un bord : **généralement toujours dans la plage**, dans le dernier dixième de celle-ci |
| Rouge | Passé le bord, et qui vaut la peine d’agir |
| Gris | Pas de verdict : pas de mesure récente, ou pas de plage utilisable pour juger |

:::note Orange signifie généralement « toujours bien, mais en train d’aller quelque part »
Orange est une *marge*, pas une infraction. Une mesure dans sa plage mais dans les derniers 10 % de celle-ci passe à l’orange délibérément, pour que la dérive soit visible tant qu’il y a encore le temps d’agir plutôt qu’au moment où elle devient un problème.

Deux raffinements en découlent.

**Une plage que vous réglez vous-même est traitée comme une limite déclarée.** La franchir fait passer le widget directement au rouge : pas de marge orange, parce que vous avez tracé cette ligne délibérément. Une plage **fournie par Cora** est une référence plus souple : la franchir affiche l’orange pour les premiers 10 % au-delà du bord, et passe au rouge après cela.

**Une limite à sens unique** (un plafond de contaminant, ou un plancher de nutriment) est graduée sur son bord haut seulement, donc le cuivre à zéro se lit vert plutôt que d’être orangé pour être proche du bas de l’échelle.
:::

Un widget entouré en orange ou en rouge est un widget qui a besoin d’attention. Le contour est sur le widget, pas seulement sur le chiffre, il reste donc visible en faisant défiler.

## Sous les widgets

![Le bas du tableau de bord](img/mobile-dashboard-foot.webp "Modifier le tableau de bord, Enregistrer les paramètres, et raccourcis vers les quatre zones d’enregistrement.")

Au bas du tableau de bord :

- **Modifier le tableau de bord** : ouvre l’[éditeur de tableau de bord](/help/mobile-dashboard-editing)
- **Enregistrer les paramètres** : saisissez des mesures de test en kit à la main
- **Journal · Alertes · Entretien · Population** : raccourcis vers ces zones pour cet aquarium

Une ligne au-dessus d’eux montre quand le tableau de bord s’est mis à jour pour la dernière fois et sur quelles sources il s’est appuyé.

## Toucher pour approfondir

Touchez n’importe quel widget pour ouvrir son détail : l’historique complet en graphique, chaque source qui l’a rapporté, et les seuils actuellement appliqués. De là, vous pouvez enregistrer une nouvelle mesure à la main, changer la plage, ou regarder plus loin en arrière.

## Si un widget n’a aucune valeur

Un widget affiche une valeur une fois qu’il en reçoit une. Quand il est vide, la raison est généralement l’une de celles-ci :

- L’appareil est hors ligne ; vérifiez l’onglet **Appareils**
- Le paramètre n’a pas encore de source ; enregistrez-le à la main, ou connectez un équipement qui le rapporte
- Le paramètre n’a jamais été rapporté ou enregistré ; rien n’a encore été enregistré pour lui

Une mesure ancienne ne disparaît pas parce que la fenêtre du graphique est plus courte que son ancienneté. Elle reste sur le widget avec son ancienneté affichée, donc une valeur périmée se lit comme périmée plutôt que comme manquante.

Voir **[Résolution de problèmes](/help/troubleshooting)** pour tout ce qui va au-delà.
