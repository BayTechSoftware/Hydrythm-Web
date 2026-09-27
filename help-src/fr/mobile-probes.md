---
title: Sondes
description: Faites correspondre les sondes de votre contrôleur aux paramètres de Cora, et notez leurs étalonnages et nettoyages.
section: Cora Mobile
reviewed: 2026-09-09
order: 13
group: Equipment
---

Un contrôleur donne ses propres noms à ses sondes. L’association des sondes indique à Cora laquelle mesure le pH, laquelle mesure la température, etc.

## Associer les sondes

Ouvrez le **profil de l’aquarium** (le crayon en haut du tableau de bord), dépliez la section de votre contrôleur et touchez **Association des sondes**.

![Association des sondes](img/mobile-probes.webp "Chaque sonde signalée par votre contrôleur, sa mesure en direct, et ce que Cora en fait.")

Toutes les sondes de votre contrôleur sont listées, avec leur mesure actuelle. Cora reconnaît tout seul les noms standard, et chaque ligne montre l’association qu’il a trouvée. En général, il vous reste seulement à corriger celles qu’il n’a pas su placer.

Chaque ligne propose trois choix :

- **Un paramètre Cora** : ce que mesure la sonde.
- **Personnalisé** : pour une sonde qui ne correspond à aucun paramètre standard de Cora. Vous lui donnez un court code en majuscules, et elle est suivie sous ce nom.
- **Ignorer** : pour une sonde que vous ne voulez pas enregistrer du tout.

Une sonde ignorée ou non associée n’apparaît sur aucun tableau de bord et ne déclenche aucune alerte.

Les associations s’appliquent à partir des prochaines mesures enregistrées. Une correction ne réécrit donc pas l’historique. Elle change seulement ce qui sera enregistré ensuite. Touchez **Enregistrer** pour les appliquer.

:::warning Cora ne voit pas une sonde non associée
Si un paramètre n’affiche aucune mesure alors que la sonde fonctionne, vérifiez l’association en premier.
:::

## Plusieurs sondes pour un même paramètre

Si vous avez deux sondes de température, vous pouvez associer les deux. Cora les garde comme deux sources distinctes. Le réglage de source de chaque widget choisit celle que la tuile suit, et [la page du paramètre](/help/mobile-metric-detail) vous sert à les comparer.

## Noter l’entretien des sondes

Les sondes dérivent. Cora peut garder la date du dernier étalonnage ou nettoyage de chacune. Vous saurez ainsi faire la différence entre un vrai changement et une sonde à revoir.

Notez l’étalonnage ou le nettoyage depuis la ligne de la sonde. Vous pouvez aussi en faire une [tâche d’entretien](/help/mobile-maintenance) régulière.

:::note L’historique d’étalonnage explique les désaccords
Quand une sonde et un test en kit ne sont pas d’accord, commencez par regarder la date du dernier étalonnage de la sonde.
:::
