---
title: Consommables
description: Réglez des alertes de réapprovisionnement pour le réactif, les contenants de dosage, les réservoirs et les médias.
section: Cora Mobile
reviewed: 2026-09-09
order: 14
group: Equipment
---

L’équipement qui consomme quelque chose (réactif, liquide de dosage, eau de complément, média filtrant) peut indiquer à Cora combien il en reste. Cora peut vous avertir avant l’épuisement.

## Régler une alerte de réapprovisionnement

Ouvrez l’appareil (depuis l’onglet **Appareils**, ou en touchant sa tuile sur le tableau de bord), puis utilisez la **cloche** dans la barre supérieure.

![Alertes de réapprovisionnement pour une unité de dosage](img/mobile-consumables.webp "Un seuil par tête, chacun activé ou désactivé indépendamment.")

L’équipement avec plusieurs contenants obtient un seuil par contenant, donc une tête que vous surveillez de près et une tête que vous touchez rarement peuvent être réglées différemment.

**La plupart des seuils sont réglés en jours, pas en volume.** Cora calcule combien de temps ce qui reste va durer, au rythme auquel vous l’utilisez réellement, ce qui est le chiffre sur lequel vous pouvez agir ; « quatre jours de calcium restant » vous dit quelque chose que « 180 mL restants » ne dit pas.

| Appareil | Seuil sur |
|---|---|
| Trident | Tests restants, et le niveau de remplissage de la bouteille de déchets |
| Tête de dosage | Jours de complément restants ; certaines proposent aussi les millilitres restants |
| ATO | Jours de réservoir restants |
| Rouleau de mat | Jours de rouleau restants |

Une alerte de consommable se comporte comme toute autre alerte : elle apparaît dans le [Centre d’alertes](/help/mobile-alerts) et peut être envoyée à votre téléphone. Vous recevez **une** notification quand un niveau est franchi, pas un flux répété, et elle se ferme quand le niveau revient au-dessus du seuil.

## Choisir un seuil

Réglez-le suffisamment en avance pour pouvoir agir. Un seuil qui se déclenche le jour où quelque chose s’épuise ne donne aucun avertissement.

:::warning Certains équipements ne s’arrêtent pas quand ils sont vides
Une tête de dosage avec un contenant vide continue d’exécuter son programme et signale des dosages qu’elle n’a pas délivrés. L’alerte de réapprovisionnement est ce qui empêche cela, réglez-en donc une pour chaque tête à partir de laquelle vous dosez.
:::

## Après le réapprovisionnement

Réinitialisez ou mettez à jour le niveau sur la page de l’appareil pour que l’alerte se ferme et que le prochain avertissement soit calculé correctement.
