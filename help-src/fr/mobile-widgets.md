---
title: Référence des widgets
description: Chaque type de widget dans Cora (valeur, jauge, graphique, état, prise et les tuiles d’appareil) et quand utiliser chacun.
section: Cora Mobile
reviewed: 2026-09-17
order: 7
group: Your dashboard
---

Un widget est une tuile sur votre tableau de bord qui montre une chose. Cette page couvre chaque type et ce que vous pouvez configurer.

Ajoutez-les et disposez-les dans **[l’éditeur de tableau de bord](/help/mobile-dashboard-editing)** ; touchez un widget là pour ouvrir ses réglages.

![Configurer un widget](img/mobile-widget-config.webp "Type, paramètre, puis largeur et hauteur.")

## Les neuf types

| Type | Affiche |
|---|---|
| **Valeur** | La mesure actuelle, son unité, son ancienneté et sa source |
| **Jauge** | Un arc avec votre plage indiquée par bandes et un repère à la valeur |
| **Graphique** | Une tendance sur une fenêtre que vous choisissez |
| **État** | Un état en texte : en marche, à l’arrêt, fermé |
| **Prise** | Une commande à trois positions : Auto, Éteint, Allumé |
| **ReefBeat** | Une unité Red Sea, avec son propre résumé |
| **Module Apex** | Un module Apex installé, comme un Trident ou un DŌS |
| **Jecod** | Une pompe Jecod, avec son mode et son intensité |
| **Maxspect** *(bêta)* | Une pompe de brassage, avec ses deux moteurs |

Les quatre derniers sont des tuiles d’**appareil** : elles sont liées à un équipement plutôt qu’à un paramètre, et chacune affiche ce que cette unité rapporte.

## Dimensionnement

**Largeur** et **Hauteur** sont chacune **1×** ou **2×**. Un graphique n’est jamais large d’une seule cellule.

## Valeur

Le chiffre simple. Mesure actuelle, son unité, son ancienneté et d’où elle vient.

Utilisez-la pour les paramètres que vous vérifiez numériquement plutôt que par tendance : calcium, magnésium, nitrate.

**Réglages :** étiquette, source, taille.

## Jauge

Un arc avec votre plage cible indiquée par bandes et un repère à la valeur actuelle. La couleur du repère vous dit où vous vous situez : dans la bande, en dérive, ou hors plage.

Utilisez-la pour les paramètres que vous gérez activement : alcalinité, pH, salinité, température.

**Réglages :** étiquette, source, plage (héritée des cibles de votre aquarium à moins que vous ne la remplaciez ici), taille.

:::note Dimensionnez les jauges à deux colonnes ou plus
Sur une seule colonne, l’arc est trop petit pour être lu d’un coup d’œil ; utilisez un widget **valeur** à la place si l’espace est limité.
:::

## Graphique

Une mini-courbe sur une fenêtre que vous choisissez, avec le haut et le bas marqués et la valeur actuelle indiquée.

Pour un paramètre que vous testez (par Trident ou avec un test en kit), la ligne relie vos tests réels. Si la fenêtre ne contient qu’un seul test, la ligne part du test précédent, et aucun haut ni bas n’est marqué. Sans test dans la fenêtre, ou rien de plus tôt pour relier un test unique, la tuile affiche **Collecte en cours…** au lieu d’une ligne.

Utilisez-la pour tout ce qui évolue : le pH au fil de la journée, la température pendant une vague de chaleur, l’alcalinité entre les dosages.

**Réglages :** étiquette, source, **fenêtre temporelle** (1 heure, 6 heures, 24 heures, 7 jours, 30 jours, 1 an), taille.

Une tendance est toujours **large d’au moins deux cellules** ; une mini-courbe compressée dans une seule cellule ne vous dit rien, donc l’éditeur n’en créera pas une.

:::note Choisissez la fenêtre selon le rythme
Le pH varie sur un cycle quotidien, donc 24 heures vous montre la forme. L’alcalinité évolue sur des jours, donc 7 ou 30 vous en dit plus que 24 ne le fera jamais.
:::

## État

Du texte plutôt qu’un chiffre, pour les choses qui sont un état. En marche, à l’arrêt, ouvert, fermé, en train de nourrir.

**Réglages :** étiquette, source, taille.

## Prise

Un commutateur à trois positions pour une prise : **Auto**, **Éteint**, **Allumé**.

- **Auto** rend la prise à ce qui la commande normalement : un programme, une règle, ou le contrôleur auquel elle appartient.
- **Éteint** et **Allumé** sont des dérogations manuelles qui restent jusqu’à ce que vous les changiez à nouveau.

**Réglages :** étiquette, quelle prise, taille.

:::warning Une dérogation manuelle n’expire pas
Éteint signifie éteint jusqu’à ce que vous le remettiez sur Auto. Si vous éteignez une pompe de remontée pour travailler dans l’aquarium, remettez-la sur Auto une fois terminé ; Cora ne le fera pas pour vous.
:::

## ReefBeat

Une tuile pour tout un équipement, montrant son propre résumé plutôt qu’un seul paramètre : l’état et le réservoir d’un ATO, les têtes d’une unité de dosage, les jours restants d’un rouleau de mat.

Quels appareils proposent une tuile dépend de ce que vous avez connecté. Voir **[Connecter votre équipement](/help/mobile-connections)**.

**Réglages :** étiquette, quel appareil, taille.

## Ce qu’affiche un widget de paramètre

Sur un widget adossé à un paramètre mesuré (Valeur, Jauge, Graphique et État), trois choses sont toujours présentes. Les tuiles de prise et d’appareil affichent leur propre état à la place, car aucune mesure unique ne se trouve derrière elles :

- **La valeur**, en grand
- **L’ancienneté** (`now`, `1h`, `2d`) : depuis combien de temps date la mesure, pas depuis quand l’écran s’est actualisé
- **La source** : un petit badge disant d’où vient le chiffre

Touchez n’importe quel widget pour ouvrir son historique complet, chaque source qui le rapporte, et les seuils en vigueur.

## Tailles

Les widgets sont larges d’une ou deux cellules et hauts d’une ou deux cellules, sauf une **tendance**, qui est toujours large d’au moins deux. Sur un tableau de bord à trois colonnes, une jauge large de deux prend les deux tiers de la ligne, ce qui est généralement la bonne forme pour votre paramètre le plus important.
