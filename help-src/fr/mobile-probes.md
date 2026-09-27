---
title: Sondes
description: Associez les sondes de votre contrôleur aux paramètres Cora, et enregistrez l’étalonnage et le nettoyage.
section: Cora Mobile
reviewed: 2026-09-09
order: 13
group: Equipment
---

Un contrôleur signale ses sondes avec ses propres noms. L’association des sondes indique à Cora laquelle est votre sonde de pH, laquelle est la température, et ainsi de suite.

## Associer les sondes

Ouvrez votre **profil d’aquarium** (le crayon en haut du tableau de bord), développez la section de votre contrôleur, et choisissez **Association des sondes**.

![Association des sondes](img/mobile-probes.webp "Chaque sonde signalée par votre contrôleur, sa mesure en direct, et ce que Cora en fait.")

Chaque sonde signalée par votre contrôleur est listée avec sa mesure actuelle. Cora détecte automatiquement les noms standards, et la ligne montre celui qu’il a associé, donc le travail ici consiste généralement à corriger celles qu’il n’a pas pu placer plutôt qu’à toutes les associer à la main.

Chaque ligne propose trois choix :

- **Un paramètre Cora** : la mesure que cette sonde relève.
- **Personnalisé** : pour une sonde pour laquelle Cora n’a aucun paramètre standard. Vous lui donnez un court identifiant en majuscules, et elle est suivie sous ce nom.
- **Ignorer** : pour les sondes que vous ne voulez pas enregistrer du tout.

Une sonde ignorée ou non associée n’apparaîtra pas sur un tableau de bord et n’alimentera aucune alerte.

Les associations prennent effet au prochain enregistrement de mesures, donc une correction ici ne réécrit pas l’historique ; elle change ce qui est stocké à partir de ce moment. Appuyez sur **Enregistrer** pour les appliquer.

:::warning Une sonde non associée est invisible pour Cora
Si un paramètre n’affiche aucune mesure bien que la sonde fonctionne, vérifiez l’association avant tout le reste.
:::

## Plusieurs sondes pour un même paramètre

Un système avec deux sondes de température peut associer les deux. Cora les garde comme sources distinctes ; le réglage de source du widget décide laquelle une tuile suit, et [la vue du paramètre](/help/mobile-metric-detail) vous permet de les comparer.

## Enregistrer l’entretien des sondes

Les sondes dérivent. Cora peut suivre quand chacune a été étalonnée ou nettoyée pour la dernière fois, pour que vous puissiez distinguer un vrai changement d’une sonde qui a besoin d’attention.

Enregistrez l’étalonnage ou le nettoyage depuis la fiche de la sonde. Cela convient aussi bien comme [tâche d’entretien](/help/mobile-maintenance) récurrente.

:::note L’historique d’étalonnage explique les désaccords
Quand une sonde et un test en kit ne sont pas d’accord, la date du dernier étalonnage de la sonde est généralement la première chose à vérifier.
:::
