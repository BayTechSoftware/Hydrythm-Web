---
title: Association des paramètres et sondes
description: Choisissez quelle sonde alimente chaque mesure, dites à Cora ce que mesure chaque sonde, et notez l’étalonnage et le nettoyage des sondes.
section: Cora Mobile
reviewed: 2026-10-13
order: 15
group: Equipment
---

Utilisez **Association des paramètres** pour dire à Cora ce que mesure chaque sonde et, quand deux sondes mesurent la même chose, laquelle croire. Allez dans **Paramètres**, ouvrez l’aquarium et touchez **Association des paramètres**.

Elle se trouve entre **Modifier l’aquarium** et **Seuils d’alerte**. Le crayon en haut du tableau de bord ouvre **Modifier l’aquarium**, qui ne la contient pas. Vous pouvez aussi y accéder depuis les pages d’appareil Neptune Apex.

L’écran a un champ de recherche (**Rechercher un paramètre**) et deux onglets, **Association** et **Sources**. La recherche porte sur les noms de paramètres, les noms de sondes, les appareils et les marques. Le même champ de recherche se trouve dans chaque sélecteur de paramètre.

## Sondes : dire à Cora ce qu’est chacune {#mapping}

![L’onglet Association](img/mobile-probe-mapping.webp "Chaque sonde, regroupée par l’appareil qui la signale, avec le paramètre auquel elle est associée.")

L’onglet **Association** s’ouvre en premier. Il liste toutes les sondes que Cora connaît, regroupées par l’appareil qui les signale, avec leur mesure actuelle. Cora reconnaît tout seul les noms de sonde standard, et chaque ligne montre ce qu’il a trouvé. En général, il vous reste seulement à corriger les quelques sondes qu’il n’a pas su placer.

Chaque ligne vous propose trois choix.

- **Un paramètre Cora** est le paramètre que mesure cette sonde.
- **Personnalisé…** sert pour une sonde qui n’a pas de paramètre standard dans Cora. Tapez un nom court en majuscules dans **Paramètre personnalisé (jeton en MAJUSCULES)**, et Cora la suit sous ce nom.
- **Ignorer** sert pour les sondes que vous ne voulez pas enregistrer du tout.

Une sonde ignorée ou non associée n’apparaît sur aucun tableau de bord et ne déclenche aucune alerte.

Une association prend effet à l’arrivée des mesures suivantes. En corriger une ici ne réécrit pas l’historique. Cela change seulement ce qui est enregistré à partir de là. Touchez **Enregistrer** pour appliquer vos changements.

:::warning Cora ne voit pas une sonde non associée
Si un paramètre n’affiche aucune mesure alors que la sonde fonctionne, vérifiez d’abord son association.
:::

## D’où vient chaque mesure {#sources}

![L’onglet Sources](img/mobile-probes.webp "Chaque mesure, la sonde qui l’alimente, et si elle est Automatique ou Choisi par vous.")

L’onglet **Sources** liste chaque paramètre que Cora suit pour cet aquarium, comme le pH ou la température, et montre quelle sonde l’alimente actuellement.

Touchez une mesure pour voir toutes les sondes qui la signalent, sur tous les contrôleurs que vous avez connectés. Chacune affiche sa marque, son propre nom pour la sonde et sa valeur en direct. Choisissez-en une pour l’épingler, ou choisissez **Automatique (la mesure la plus récente l’emporte)** pour laisser Cora utiliser la sonde qui a transmis en dernier. Les autres restent dans l’historique.

Une étiquette à côté de chaque mesure indique ce qui est actif : **Automatique**, ou **Choisi par vous** une fois que vous avez épinglé une sonde. Votre choix s’applique à cette mesure dans tout l’aquarium, pas à un seul widget.

Si une sonde épinglée arrête de transmettre, Cora indique la dernière fois qu’elle a donné signe de vie et propose **Revenir à Automatique**, pour qu’une sonde morte ne puisse pas bloquer une mesure.

Touchez **Renommer** pour donner à une mesure son propre nom d’affichage. C’est indépendant du nom que vous donnez à la sonde elle-même. C’est ce nom qui apparaît sur votre tableau de bord, dans les alertes et dans Reef Buddy.

Le profil de l’aquarium a aussi une section **Sources des paramètres** (elle est masquée pendant la création d’un nouvel aquarium). Elle règle la même chose sous une forme plus courte. Utilisez l’Association des paramètres quand vous voulez voir toutes les sondes de tous les contrôleurs au même endroit.

:::note Un capteur de fuite ne peut pas être réaffecté ici
L’alarme d’un capteur de fuite dépend de son propre nom, il est donc exclu de ce sélecteur. Il fonctionne comme d’habitude.
:::

## Plusieurs sondes pour un même paramètre {#multiple-probes}

Si vous avez deux sondes de température, sur le même contrôleur ou sur deux contrôleurs différents, associez les deux. Cora les garde comme sources distinctes, et l’onglet **Sources** est l’endroit où vous choisissez laquelle alimente la mesure, ou la laissez sur Automatique. Vous pouvez les comparer dans [la page du paramètre](/help/mobile-metric-detail).

Quand deux sources signalent le même paramètre, la mesure la plus récente l’emporte. Une valeur à l’écran n’est remplacée que par une mesure dont l’heure de mesure est plus tardive, quel que soit l’appareil d’où elle vient. Une mesure plus ancienne, ou un appareil qui renvoie une ancienne mesure, va dans l’historique et n’écrase pas la valeur actuelle. Si vous avez épinglé une source dans l’onglet **Sources**, Cora suit cette source à la place.

## Noter l’entretien des sondes {#recording-probe-care}

Les sondes dérivent. Quand vous étalonnez, nettoyez ou remplacez une sonde, dites-le à Cora, pour qu’il ne prenne pas le saut de la mesure pour un vrai changement dans l’aquarium.

1. Touchez le widget du paramètre sur le tableau de bord, par exemple le pH, la température, la salinité ou l’ORP.
2. Touchez **Enregistrer l’entretien de la sonde** (l’icône de capteur) dans la barre du haut.
3. Choisissez ce que vous avez fait : **Étalonnée**, **Nettoyée**, **Remplacée**, **Repositionnée** ou **Comparée à une référence**. Vous pouvez ajouter une **Mesure de référence** et une note.
4. Touchez **Enregistrer l’entretien de la sonde**.

La page du paramètre indique ensuite depuis combien de temps cette sonde a été étalonnée. L’entretien des sondes fait aussi une bonne [tâche d’entretien](/help/mobile-maintenance) régulière.

:::note Les dates d’étalonnage expliquent les désaccords
Quand une sonde et un kit de test ne sont pas d’accord, regardez quand vous avez étalonné la sonde pour la dernière fois. C’est en général la réponse.
:::
