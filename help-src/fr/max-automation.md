---
title: Scènes sur Cora Max
description: Créer, lancer et modifier des scènes directement sur Cora Max.
section: Cora Max
reviewed: 2026-09-27
order: 15
group: Automation
---

Une **scène** est un groupe d’actions sur votre équipement, enregistré pour être lancé d’un coup. Elle tourne pendant une durée fixe ou jusqu’à ce que vous l’arrêtiez. Une scène fonctionne de la même façon, qu’elle ait été créée sur le téléphone ou sur Cora Max. Cette page explique comment faire sur Cora Max.

## Où trouver les scènes

**Réglages → Automatisations** liste toutes les scènes de tous vos aquariums. Si vous en avez plusieurs, une puce par aquarium sert de filtre. Vous y voyez la même liste, que la scène vienne du téléphone ou de Cora Max.

Touchez une scène pour la modifier, ou touchez **+** pour en créer une. Si vous avez plusieurs aquariums et qu’aucun filtre n’est choisi, Cora Max vous demande à quel aquarium rattacher la nouvelle scène.

## Créer une scène

1. Donnez un **nom** à la scène.
2. Ajoutez des **étapes**. Depuis Cora Max, une étape peut commander une prise Apex (**Allumé**, **Éteint** ou **Auto**) ou une prise Zigbee (**allumé**, **éteint** ou **basculer**). Les étapes ajoutées sur le téléphone pour d’autres équipements s’affichent aussi ici. Vous pouvez les déplacer ou les retirer, mais pas en ajouter de nouvelles de ce type depuis cet écran.
3. Choisissez combien de temps elle dure : un nombre de minutes, ou **permanente** (elle tourne jusqu’à ce que vous l’arrêtiez).
4. Choisissez si la scène demande une **confirmation** avant de se lancer. Laissez-la activée, sauf si vous êtes certain que la scène ne touche rien qu’il serait risqué de changer sans vérifier.
5. Enregistrez.

:::note Une scène ne peut pas lancer de dosage DŌS
Qu’elle soit créée sur Cora Max ou sur le téléphone, une scène ne peut jamais activer une tête de dosage. Un dosage ne doit pas pouvoir partir par erreur à cause d’une scène.
:::

## Lancer une scène

Les scènes s’affichent comme des tuiles sur le tableau de bord. Touchez **Lancer** pour en démarrer une.

Si la scène demande une confirmation, Cora Max liste d’abord ce qu’elle va faire, une ligne par étape. Rien ne se passe avant. Lisez la liste, puis lancez la scène ou annulez.

Pendant une scène à durée fixe, sa tuile affiche le temps restant et un bouton **Arrêter** pour la terminer plus tôt. La tuile d’une scène permanente reste en cours jusqu’à ce que vous l’arrêtiez.

Lancer ou arrêter une scène passe toujours par Cora Cloud, comme toute autre commande. Le résultat est enregistré dans [Ce qui a été changé, et par quoi](/help/max-activity).

Si une scène refuse de se lancer ou de s’arrêter, consultez la page [Résolution de problèmes](/help/troubleshooting).

:::note Le verrouillage enfant bloque aussi les scènes
Si le [verrouillage enfant](/help/max-voice) est activé, vous ne pouvez pas lancer ni arrêter une scène depuis cet écran, comme pour toute autre commande. Vous pouvez toujours poser des questions sur une scène à la voix, mais pas la lancer ni l’arrêter.
:::

## Modifier ou supprimer une scène

Ouvrez la scène depuis **Réglages → Automatisations**, ou faites un appui long sur sa tuile dans le tableau de bord. Vous pouvez alors changer son nom, ses étapes, sa durée ou sa confirmation, ou la supprimer.

:::note Un Cora Max plus ancien lance les scènes mais ne les modifie pas
La création et la modification de scènes sont arrivées dans une version récente de Cora Max. Un Cora Max plus ancien sur le même compte peut afficher et lancer une scène créée sur le téléphone ou sur un Cora Max plus récent, mais il ne peut pas la modifier. Dans ce cas, mettez Cora Max à jour, ou modifiez la scène depuis le téléphone ou un écran plus récent.
:::

Tout ce qu’une scène peut faire, et comment la créer sur le téléphone, est expliqué dans [Scènes et automatisations](/help/mobile-automation).
