---
title: Consommables et alertes de réapprovisionnement
description: Réglez des alertes de réapprovisionnement pour le réactif, les bidons de dosage, les réservoirs d’osmolateur et les rouleaux filtrants, et indiquez à Cora quand vous avez rempli.
section: Cora Mobile
reviewed: 2026-10-13
order: 16
group: Equipment
---

Utilisez les alertes de réapprovisionnement pour que Cora vous prévienne avant que le réactif, le liquide de dosage, l’eau d’appoint ou le rouleau filtrant ne s’épuise. Ouvrez l’appareil depuis **Appareils** (ou touchez sa tuile sur le tableau de bord), puis touchez la **cloche** dans la barre du haut.

## Régler une alerte de réapprovisionnement {#setting-a-refill-alert}

![La feuille Alertes d’un ReefDose 4, avec un seuil en jours restants et un interrupteur pour chaque tête](img/mobile-consumables.webp "Un seuil par tête, chacun avec son propre interrupteur.")

La feuille s’appelle **Alertes :** suivi du nom de l’appareil. Si l’équipement a plusieurs récipients, chacun a son propre seuil et son propre interrupteur. Vous pouvez donc régler différemment une tête que vous surveillez de près et une tête à laquelle vous touchez rarement. Désactiver un interrupteur garde la valeur pour plus tard.

Où le régler :

- **La plupart des appareils** : la cloche dans la barre du haut de la page de l’appareil.
- **DŌS** : la carte **Alertes** sur la page du DŌS, ou la cloche. Voir [Alertes des doseurs](/help/mobile-device-control#doser-alerts).
- **AquaWiz** : leur règle dans l’onglet **Règles** du [Centre d’alertes](/help/mobile-alerts).

La plupart des seuils se règlent en jours, pas en volume. Cora calcule combien de temps durera ce qui reste au rythme où vous l’utilisez. « Encore quatre jours de calcium » vous permet d’agir. « Encore 180 mL », non.

## Ce qui peut vous être signalé {#thresholds}

| Appareil | Seuil | Valeur de départ |
|---|---|---|
| Trident | **Tests restants** (le réactif le plus bas) | 10 tests |
| Trident | **Bouteille de déchets** (une bouteille pleine fait échouer le test suivant) | 85 % pleine |
| Tête DŌS | *[tête] · jours restants* | 7 jours |
| Tête DŌS | *[tête] · restant*, en mL | 100 mL |
| Tête DŌS qui retire l’eau usée | **Espace restant dans le récipient de déchets** | |
| Tête DŌS | **Alertes de dose manquée** (un interrupteur) | |
| Tête ReefDose | Jours de produit restants | 7 jours |
| ReefATO+ | **Autonomie du réservoir**, estimée d’après la consommation récente de l’osmolateur | 2 jours |
| ReefMat | **Rouleau restant**, estimé d’après la vitesse d’avancement du rouleau | 3 jours |
| AquaWiz | Produit d’alcalinité restant | 100 mL |


Une alerte de consommable fonctionne comme les autres alertes. Elle apparaît dans le [Centre d’alertes](/help/mobile-alerts) et peut arriver sur votre téléphone. Vous recevez **une seule** notification quand un niveau passe le seuil, et l’alerte se ferme quand le niveau repasse au-dessus du seuil.

## Choisir un seuil {#choosing-a-threshold}

Réglez-le assez tôt pour avoir le temps d’agir. Une alerte qui se déclenche le jour où quelque chose s’épuise ne vous prévient de rien.

:::warning Certains équipements continuent à vide
Une tête DŌS dont le récipient est vide continue son programme et signale des doses qu’elle n’a jamais délivrées. Elle n’a pas d’avertissement de niveau bas à elle. L’alerte de réapprovisionnement est ce qui vous permet de le repérer, alors réglez-en une pour chaque tête que vous utilisez.
:::

## Après le réapprovisionnement {#after-refilling}

Indiquez-le à Cora sur la page de l’appareil, pour que l’alerte se ferme et que le prochain avertissement soit calculé à partir du bon niveau.

| Appareil | Touchez |
|---|---|
| Tête DŌS | **Remplir**, puis **Plein**, ou réglez **Volume restant** |
| Récipient de déchets DŌS | Remettez son espace libre à plein après l’avoir vidé |
| Tête ReefDose | **Restant dans le flacon** |
| ReefMat | **Nouveau rouleau** après avoir mis un nouveau rouleau |

Trident, ReefATO+ et AquaWiz indiquent eux-mêmes leurs niveaux, il n’y a donc rien à réinitialiser dans Cora.
