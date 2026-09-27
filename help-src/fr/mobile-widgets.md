---
title: Référence des widgets
description: Tous les types de widgets de Cora (valeur, jauge, graphique, état, prise et tuiles d’appareil), et quand utiliser chacun.
section: Cora Mobile
reviewed: 2026-09-17
order: 7
group: Your dashboard
---

Un widget est une tuile du tableau de bord qui affiche une seule information. Cette page présente chaque type et ses réglages.

Vous ajoutez et placez les widgets dans **[l’éditeur de tableau de bord](/help/mobile-dashboard-editing)**. Dans l’éditeur, touchez un widget pour ouvrir ses réglages.

![Configurer un widget](img/mobile-widget-config.webp "Type, paramètre, puis largeur et hauteur.")

## Les neuf types

| Type | Affiche |
|---|---|
| **Valeur** | La mesure actuelle, avec son unité, son âge et sa source |
| **Jauge** | Un arc où figure votre plage, avec un curseur sur la valeur |
| **Graphique** | Une tendance sur la période de votre choix |
| **État** | Un état en toutes lettres : en marche, à l’arrêt, fermé |
| **Prise** | Une commande à trois positions : Auto, Éteint, Allumé |
| **ReefBeat** | Un appareil Red Sea, avec son propre résumé |
| **Module Apex** | Un module Apex installé, comme un Trident ou un DŌS |
| **Jecod** | Une pompe Jecod, avec son mode et son intensité |
| **Maxspect** *(bêta)* | Une pompe Gyre, avec ses deux moteurs |

Les quatre derniers sont des tuiles d’**appareil**. Elles sont liées à un équipement, pas à un paramètre, et chacune affiche ce que cet appareil transmet.

## Taille

**Largeur** et **Hauteur** valent chacune **1×** ou **2×**. Un graphique ne fait jamais une seule case de large.

## Valeur

Le chiffre, tout simplement : la mesure actuelle, son unité, son âge et sa provenance.

Choisissez-la pour les paramètres dont seul le chiffre vous intéresse : calcium, magnésium, nitrates.

Réglages : étiquette, source, taille.

## Jauge

Un arc où figure votre plage cible, avec un curseur sur la valeur actuelle. La couleur du curseur vous dit où vous en êtes : dans la plage, en train de dériver, ou dehors.

Choisissez-la pour les paramètres que vous suivez de près : alcalinité, pH, salinité, température.

Réglages : étiquette, source, plage (reprise des cibles de votre aquarium, sauf si vous la changez ici), taille.

:::note Donnez au moins deux colonnes à une jauge
Sur une seule colonne, l’arc est trop petit pour être lu d’un coup d’œil. Si la place manque, prenez plutôt un widget **Valeur**.
:::

## Graphique

Une petite courbe sur la période de votre choix. Le plus haut et le plus bas y sont marqués, et la valeur actuelle est mise en avant.

Pour un paramètre que vous testez (avec un Trident ou un test en kit), la courbe relie vos vrais tests. Si la période ne contient qu’un test, la courbe part du test précédent, et aucun plus haut ni plus bas n’est marqué. S’il n’y a aucun test sur la période, ou aucun test plus ancien auquel relier un test isolé, la tuile affiche **Collecte en cours…** à la place de la courbe.

Choisissez-le pour tout ce qui bouge : le pH au fil de la journée, la température pendant une canicule, l’alcalinité entre deux doses.

Réglages : étiquette, source, **période** (1 heure, 6 heures, 24 heures, 7 jours, 30 jours, 1 an), taille.

Un graphique de tendance fait toujours **au moins deux cases de large**. Serrée dans une seule case, une courbe ne dit rien. L’éditeur ne le permet donc pas.

:::note Choisissez la période selon le rythme du paramètre
Le pH varie au fil de la journée. Sur 24 heures, vous voyez la forme de ce cycle. L’alcalinité évolue sur plusieurs jours. Sur 7 ou 30 jours, vous en apprendrez bien plus que sur 24 heures.
:::

## État

Du texte à la place d’un chiffre, pour ce qui est un état : en marche, à l’arrêt, ouvert, fermé, nourrissage en cours.

Réglages : étiquette, source, taille.

## Prise

Un interrupteur à trois positions pour une prise : **Auto**, **Éteint**, **Allumé**.

- **Auto** rend la prise à ce qui la commande d’habitude : un programme, une règle ou son contrôleur.
- **Éteint** et **Allumé** sont des forçages manuels. Ils restent en place jusqu’à ce que vous les changiez.

Réglages : étiquette, prise concernée, taille.

:::warning Un forçage manuel n’expire pas
Éteint reste éteint tant que vous ne repassez pas sur Auto. Si vous coupez la pompe de remontée pour intervenir dans l’aquarium, remettez-la sur Auto quand vous avez fini. Cora ne le fera pas à votre place.
:::

## ReefBeat

Une tuile pour un appareil entier. Elle affiche son propre résumé, pas un paramètre unique : l’état et le réservoir d’un osmolateur, les têtes d’une unité de dosage, les jours restants d’un rouleau de mat.

Les appareils qui proposent une tuile dépendent de ce que vous avez connecté. Voir **[Connecter votre équipement](/help/mobile-connections)**.

Réglages : étiquette, appareil concerné, taille.

## Ce qu’affiche un widget de paramètre

Un widget lié à un paramètre mesuré (Valeur, Jauge, Graphique et État) affiche toujours trois éléments. Les tuiles de prise et d’appareil affichent leur état à la place, car il n’y a pas une mesure unique derrière elles.

- **La valeur**, en grand
- **L’âge** (`maintenant`, `1 h`, `2 j`) : l’ancienneté de la mesure, pas celle du dernier rafraîchissement de l’écran
- **La source** : un petit badge qui indique d’où vient le chiffre

Touchez un widget pour ouvrir tout son historique, toutes les sources qui mesurent ce paramètre et les seuils en vigueur.

## Tailles

Un widget fait une ou deux cases de large, et une ou deux cases de haut. Seule exception, un graphique de **tendance** fait toujours au moins deux cases de large. Sur un tableau de bord à trois colonnes, une jauge de deux cases prend les deux tiers de la ligne. C’est souvent le bon format pour votre paramètre le plus important.
