---
title: Scènes sur Cora Max
description: Créer, exécuter et modifier des scènes directement sur l’écran Cora Max.
section: Cora Max
reviewed: 2026-09-27
order: 15
group: Automation
---

Une **scène** est un ensemble enregistré d’actions d’équipement qui s’exécutent ensemble, soit pendant une durée fixe, soit jusqu’à ce que vous l’arrêtiez. Les scènes fonctionnent de la même façon que vous les créiez sur votre téléphone ou sur Cora Max ; cette page couvre comment le faire au mur.

## Où trouver les scènes

**Réglages → Automatisations** liste chaque scène de chacun de vos aquariums, avec une puce de filtre par aquarium quand vous en avez plus d’un. Elle ouvre la même liste, que la scène ait été créée sur le téléphone ou sur Cora Max.

Touchez une scène pour la modifier, ou touchez **+** pour en créer une nouvelle. Si vous avez plus d’un aquarium et qu’aucun filtre n’est choisi, Cora Max demande à quel aquarium la nouvelle scène appartient.

## Créer une scène

1. Donnez un **nom** à la scène.
2. Ajoutez des **étapes**. Depuis Cora Max, une étape peut commuter une prise Apex (**Allumé**, **Éteint** ou **Auto**) ou une fiche Zigbee (**allumé**, **éteint** ou **basculer**). Les étapes ajoutées sur le téléphone pour d’autres types d’équipement s’affichent toujours ici, et peuvent toujours être réordonnées ou retirées, même si cet écran ne peut pas en ajouter une autre du même type.
3. Choisissez sa durée d’exécution : un nombre fixe de minutes, ou **permanente** (elle continue de s’exécuter jusqu’à ce que vous l’arrêtiez).
4. Choisissez si exécuter la scène nécessite une étape de **confirmation**. Laissez-la activée sauf si vous êtes certain que la scène ne touche jamais rien qu’il serait risqué de changer sans un second regard.
5. Enregistrez.

:::note Les têtes de dosage DŌS ne sont jamais une étape de scène
Une scène, créée sur Cora Max ou sur le téléphone, ne peut jamais allumer une tête de dosage. C’est délibéré : un dosage n’est pas le genre d’action qu’une scène devrait pouvoir déclencher par accident.
:::

## Exécuter une scène

Les scènes apparaissent comme des tuiles sur le tableau de bord. Touchez **Lancer** pour en démarrer une.

Si la scène nécessite une confirmation, Cora Max liste exactement ce qu’elle est sur le point de faire, une ligne par étape, avant que rien ne se produise. Lisez-la, puis choisissez de l’exécuter ou d’annuler.

Pendant qu’une scène chronométrée s’exécute, sa tuile affiche un compte à rebours jusqu’à sa fin, et un bouton **Arrêter** pour la terminer plus tôt. La tuile d’une scène permanente reste dans son état d’exécution jusqu’à ce que vous l’arrêtiez.

Lancer ou arrêter une scène passe toujours par Cora Cloud, comme toute autre commande ; voir [Ce qui a été changé, et par quoi](/help/max-activity) pour où le résultat est enregistré.

**Si cela ne fonctionne pas :** si une scène ne veut pas s’exécuter ou ne veut pas s’arrêter, voir [Résolution de problèmes](/help/troubleshooting).

:::note Le verrouillage enfant couvre aussi les scènes
Si le [verrouillage enfant](/help/max-voice) est activé, lancer ou arrêter une scène depuis cet écran est bloqué comme toute autre commande. Les questions sur une scène fonctionnent toujours par la voix ; en démarrer ou en arrêter une ne fonctionne pas.
:::

## Modifier ou supprimer une scène

Ouvrez la scène depuis **Réglages → Automatisations**, ou appuyez longuement sur sa tuile sur le tableau de bord, pour changer son nom, ses étapes, sa durée ou son réglage de confirmation, ou pour la supprimer.

:::note Les écrans Cora Max plus anciens peuvent exécuter une scène mais pas la modifier
Créer et modifier des scènes au mur est une capacité plus récente de Cora Max. Un Cora Max plus ancien sur le même compte peut toujours afficher et exécuter une scène créée sur le téléphone ou sur un Cora Max plus récent ; il ne peut simplement pas la changer. Mettez à jour Cora Max, ou modifiez la scène depuis le téléphone ou depuis un écran plus récent, si cela se présente.
:::

Voir [Scènes et automatisations](/help/mobile-automation) pour ce qu’une scène peut faire plus en détail, et comment elles sont créées sur le téléphone.
