---
title: Référence des widgets
description: Chaque type de widget du tableau de bord de Cora Mobile, de la valeur, la jauge, le graphique, l’état et la prise aux tuiles d’appareils, et quand utiliser chacun.
section: Cora Mobile
reviewed: 2026-10-13
order: 9
group: Your dashboard
---

Un widget est une tuile de votre tableau de bord, et il affiche une seule chose. Cette page passe en revue chaque type et ce que vous pouvez y régler.

Vous ajoutez et disposez les widgets dans [l’éditeur de tableau de bord](/help/mobile-dashboard-editing). Touchez-y un widget pour ouvrir ses réglages : **Type** et **Paramètre** pour un paramètre, la prise ou l’appareil pour les autres, puis **Largeur** et **Hauteur**, et **Plage de temps** pour un graphique.

![La feuille de réglages d’un widget dans Cora Mobile](img/mobile-widget-config.webp "La moitié inférieure des réglages d’un widget : le paramètre, la largeur, la hauteur et la plage de temps, puis Retirer et Terminé.")

## Les quinze types {#the-fifteen-types}

| Type | Affiche |
|---|---|
| **Valeur** | La mesure actuelle, son unité, son âge et sa source |
| **Jauge** | Un arc avec votre plage marquée dessus et un curseur sur la valeur |
| **Graphique** | Une tendance sur une plage de temps que vous choisissez |
| **État** | La mesure en texte simple avec un point de couleur |
| **Prise** | Une commande à trois positions : Auto, Off, On |
| **ReefBeat** | Un appareil Red Sea, avec son propre résumé |
| **Module Apex** | Un module Apex installé, comme un Trident ou un DŌS |
| **Jecod** | Une pompe Jecod, avec son mode et son intensité |
| **Maxspect** *(Beta)* | Une Gyre, avec ses deux moteurs |
| **GHL** *(Beta)* | Un contrôleur ProfiLux ou Mitras, avec son propre résumé |
| **HYDROS** *(Beta)* | Un contrôleur HYDROS, avec son propre résumé |
| **Radion** *(Beta)* | Une lampe EcoTech Radion, ou un réseau maillé Radion associé |
| **VorTech** *(Beta)* | Une pompe EcoTech VorTech, avec son mode et sa vitesse |
| **Versa** *(Beta)* | Un doseur EcoTech Versa, avec ses têtes |
| **Caméra** *(Beta)* | Une vue en direct de l’une de vos caméras, jusqu’à trois colonnes de large et deux lignes de haut |

Tout ce qui suit Prise est une tuile d’**appareil**. Chacune appartient à un équipement plutôt qu’à un paramètre, et affiche ce que cet appareil remonte. Cora Max a aussi une tuile **Scène**, que vous ajoutez sur Cora Max. Voir [Modifier le tableau de bord Cora Max](/help/max-dashboard-editing).

:::note Tuiles Beta
Maxspect, GHL, HYDROS, EcoTech (Radion, VorTech et Versa) et Caméra sont des intégrations Beta, ouvertes uniquement aux utilisateurs Beta. Vous ne voyez ces tuiles qu’une fois l’appareil ajouté. Voir [Fonctions Beta](/help/mobile-beta).
:::

## Taille {#sizing}

**Largeur** et **Hauteur** peuvent chacune valoir **1×** ou **2×** : un widget fait donc une ou deux cases de large et une ou deux cases de haut. Une caméra peut faire jusqu’à **3×** de large. Un graphique ne fait jamais une seule case de large. Sur un tableau de bord à trois colonnes, une jauge de deux cases de large occupe les deux tiers de la rangée. C’est en général une bonne forme pour votre paramètre le plus important.

## Ce qu’affiche un widget de paramètre {#what-a-parameter-widget-shows}

Les widgets Valeur, Jauge, Graphique et État affichent tous un paramètre mesuré, et ils montrent toujours trois choses. Les tuiles de prises et d’appareils affichent leur propre état, car il n’y a pas une seule mesure derrière elles.

- **La valeur**, en grands caractères
- **L’âge** (`maintenant`, `1 h`, `2 j`), c’est-à-dire depuis combien de temps la source a confirmé la valeur pour la dernière fois. Pour une sonde, c’est le dernier contact de son appareil, donc une mesure stable reste fraîche. Pour un résultat de kit de test ou d’ICP, c’est le moment où vous avez fait le test. Plus de détails dans [Lire votre tableau de bord](/help/mobile-dashboard#how-to-read-a-parameter-widget).
- **La source**, un petit badge qui indique d’où vient le chiffre

Un widget de paramètre n’a pas de réglage de plage ni de source à lui. La plage vient des seuils d’alerte de l’aquarium (appui long sur le widget dans le tableau de bord), et la source de l’[Association des paramètres](/help/mobile-probes). Touchez le widget dans le tableau de bord pour voir tout son historique, chaque source qui le signale et votre plage d’alerte.

## Valeur {#value}

C’est le chiffre brut. Il affiche la mesure actuelle, son unité, son âge et sa provenance.

Utilisez-le pour les paramètres que vous suivez par leur chiffre plus que par leur tendance, comme le calcium, le magnésium ou les nitrates.

## Jauge {#gauge}

Une jauge est un arc avec votre plage d’alerte marquée dessus, et un curseur sur la valeur actuelle. La couleur du curseur vous dit où vous en êtes : dans la plage, en dérive ou hors plage.

Utilisez-la pour les paramètres que vous gérez activement, comme l’alcalinité, le pH, la salinité ou la température.

:::note Faites des jauges d’au moins deux colonnes de large
Sur une seule colonne, l’arc est trop petit pour être lu rapidement. Si vous manquez de place, utilisez un widget **Valeur**.
:::

## Graphique {#graph}

Un graphique est une mini-courbe sur une plage de temps que vous choisissez : 1 h, 6 h, 24 h, 7 j, 30 j ou 1 an. Il marque le haut et le bas et indique la valeur actuelle.

Pour un paramètre que vous testez (avec un Trident ou un kit de test), la courbe relie vos vrais tests. S’il n’y a qu’un test dans la période, la courbe part du test précédent, et il n’y a ni haut ni bas. S’il n’y a aucun test dans la période, ou rien d’antérieur à relier à un test unique, la tuile affiche **Collecte en cours…** à la place d’une courbe.

Utilisez-le pour tout ce qui bouge, comme le pH au fil de la journée, la température pendant une canicule ou l’alcalinité entre deux doses.

Un graphique fait toujours **au moins deux cases de large**. Une mini-courbe serrée dans une seule case ne vous apprend rien, donc l’éditeur ne vous laisse pas en créer une.

:::note Choisissez la plage adaptée au paramètre
Le pH oscille sur un cycle quotidien, donc 24 heures vous montrent le schéma. L’alcalinité évolue sur plusieurs jours, donc 7 ou 30 jours vous en disent bien plus.
:::

## État {#status}

Il affiche la mesure en texte simple, avec un point de couleur pour dans la plage, en dérive ou hors plage. Utilisez-le pour un paramètre qui n’a pas de plage de jauge utile.

## Prise {#outlet}

C’est un interrupteur à trois positions pour une prise Apex : **Auto**, **Off** et **On**. Vous choisissez la prise qu’il commande.

- **Auto** rend la prise à ce qui la pilote normalement. Ce peut être un programme, une règle ou le contrôleur auquel elle appartient.
- **Off** et **On** sont des forçages manuels. Ils restent en place jusqu’à ce que vous les changiez.

:::warning Les forçages manuels ne s’arrêtent pas tout seuls
Off veut dire éteint jusqu’à ce que vous remettiez sur Auto. Si vous éteignez une pompe de remontée pour travailler dans l’aquarium, remettez-la sur Auto quand vous avez fini. Cora ne le fera pas pour vous.
:::

## ReefBeat {#reefbeat}

C’est une seule tuile pour tout un équipement. Elle affiche le résumé propre de l’appareil plutôt qu’un seul paramètre, par exemple l’état et le réservoir d’un osmolateur, les têtes d’un doseur ou le nombre de jours restants d’un rouleau filtrant. Vous choisissez l’appareil qu’elle affiche.

Les appareils qui peuvent avoir une tuile dépendent de ce que vous avez connecté. Voir [Connecter votre équipement](/help/mobile-connections).

## Tuiles de doseur {#doser-tiles}

Une tuile de doseur (un DŌS Apex, un ReefDose ou un EcoTech Versa) affiche une ligne par tête. Un nom de tête n’est jamais réduit en dessous d’une taille lisible. Sur une tuile haute, la ligne prend deux lignes, avec le nom sur la première et ce qui reste sur la seconde, par exemple *40 j* et *2,8 L*. Sur une tuile basse, la ligne de détail disparaît et le nom reste lisible.

Choisissez ce qui vient en premier avec **Afficher le reste en** : **Jours** ou **Millilitres (mL)**. Une tête ReefDose sans nom propre est affichée avec le nom de l’appareil suivi de « tête » et de son numéro. Une tuile de doseur Jecod est en lecture seule et affiche le plan quotidien, car Jecod n’indique pas combien il reste dans le flacon.
