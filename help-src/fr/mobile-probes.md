---
title: Sondes
description: Voyez quelle sonde alimente chaque mesure sur tous vos contrôleurs, et notez les étalonnages et nettoyages.
section: Cora Mobile
reviewed: 2026-09-30
order: 13
group: Equipment
---

Si vous avez plus d’un contrôleur, ou deux sondes qui mesurent la même chose, Cora doit savoir quelle mesure croire. L’association des sondes est l’endroit où vous réglez cela, et où vous dites aussi à Cora ce qu’est chaque sonde.

Ouvrez le **profil de l’aquarium** (le crayon en haut du tableau de bord) et touchez **Association des sondes**.

## D’où vient chaque mesure

![D’où vient chaque mesure](img/mobile-probes.webp "Chaque paramètre, la sonde qui l’alimente, et un bouton Choisir pour la changer.")

Cette section liste chaque paramètre que Cora suit pour cet aquarium, comme le pH ou la température, et montre quelle sonde l’alimente actuellement.

Touchez une mesure pour voir toutes les sondes qui la signalent, sur tous les contrôleurs que vous avez connectés. Chacune affiche sa marque, son propre nom pour la sonde, et sa valeur en direct. Choisissez-en une pour l’épingler, ou choisissez **Automatique** pour laisser Cora utiliser celle qui transmet.

Une étiquette à côté de chaque mesure indique ce qui est actif : **Automatique**, ou **Choisi par vous** une fois que vous avez épinglé une sonde.

Si une sonde épinglée arrête de transmettre, Cora indique la dernière fois qu’elle a donné signe de vie et propose **Revenir à Automatique**, pour qu’une sonde morte ne puisse pas bloquer une mesure.

Touchez **Renommer** pour donner à une mesure son propre nom d’affichage. C’est indépendant du nom que vous donnez à la sonde elle-même. C’est ce nom qui apparaît sur votre tableau de bord, dans les alertes et dans Reef Buddy.

:::note Un capteur de fuite ne peut pas être réaffecté ici
L’alarme d’un capteur de fuite dépend de son propre nom, il est donc exclu de ce sélecteur. Il fonctionne comme d’habitude.
:::

## Sondes : dire à Cora ce qu’est chacune

Plus bas, vous verrez toutes les sondes que Cora connaît, groupées par l’appareil qui les signale, avec leur mesure actuelle. Cora reconnaît tout seul les noms de sonde standard, et chaque ligne montre ce qu’il a trouvé. En général, il vous reste seulement à corriger celles qu’il n’a pas su placer.

Chaque ligne propose trois choix :

- **Un paramètre Cora** : ce que mesure la sonde.
- **Personnalisé** : pour une sonde qui ne correspond à aucun paramètre standard de Cora. Vous lui donnez un court code en majuscules, et elle est suivie sous ce nom.
- **Ignorer** : pour une sonde que vous ne voulez pas enregistrer du tout.

Une sonde ignorée ou non associée n’apparaît sur aucun tableau de bord et ne déclenche aucune alerte.

Les associations s’appliquent à partir des prochaines mesures enregistrées. Une correction ne réécrit donc pas l’historique. Elle change seulement ce qui sera enregistré ensuite. Touchez **Enregistrer** pour les appliquer.

:::warning Cora ne voit pas une sonde non associée
Si un paramètre n’affiche aucune mesure alors que la sonde fonctionne, vérifiez son association en premier.
:::

## Plusieurs sondes pour un même paramètre

Si vous avez deux sondes de température, sur le même contrôleur ou sur deux contrôleurs différents, associez les deux. Cora les garde comme sources distinctes, et **D’où vient chaque mesure** ci-dessus est l’endroit où vous choisissez laquelle alimente la mesure, ou vous la laissez sur Automatique. Vous pouvez les comparer dans [la page du paramètre](/help/mobile-metric-detail).

## Noter l’entretien des sondes

Les sondes dérivent. Cora peut garder la date du dernier étalonnage ou nettoyage de chacune. Vous saurez ainsi faire la différence entre un vrai changement et une sonde à revoir.

Notez l’étalonnage ou le nettoyage depuis la ligne de la sonde. Vous pouvez aussi en faire une [tâche d’entretien](/help/mobile-maintenance) régulière.

:::note L’historique d’étalonnage explique les désaccords
Quand une sonde et un test en kit ne sont pas d’accord, commencez par regarder la date du dernier étalonnage de la sonde.
:::
