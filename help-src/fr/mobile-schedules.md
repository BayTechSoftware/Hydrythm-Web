---
title: Programmer l’équipement
description: Créez un programme journalier pour une pompe Jecod, copiez-le d’une pompe à l’autre, enregistrez-le et partagez-le, et vérifiez que la pompe l’a pris en compte.
section: Cora Mobile
reviewed: 2026-10-17
order: 14
group: Equipment
---

Cette page explique comment donner à une pompe Jecod un **programme journalier** : un ensemble de périodes, chacune avec sa propre intensité, qui se répète tous les jours. Ouvrez-le depuis **Appareils** → touchez la pompe.

Les lampes et pompes d’autres marques gardent leurs programmes sur leurs propres pages : les ReefDose de Red Sea dans [Contrôler votre équipement](/help/mobile-device-control#red-sea).

![La page d’une pompe Jecod dans Cora Mobile avec Programme choisi](img/mobile-schedules.webp "Programme choisi en haut, la pause nourrissage, puis le graphique de la journée.")

## Identique toute la journée, ou Programme {#same-all-day-or-schedule}

Une pompe fonctionne dans l’un de ces deux modes. Choisissez-en un avec le sélecteur de sa page. Celui qui fonctionne est marqué *· en cours*, et la page s’ouvre dessus.

- **Identique toute la journée** tourne à une seule intensité en continu.
- **Programme** suit un programme journalier fait de périodes.

Cora envoie votre choix directement à la pompe quand votre téléphone est sur son réseau. Sinon, il passe par le Cora Max de l’aquarium. Une pompe Bluetooth doit être à portée. Tant qu’elle ne l’est pas, votre choix ne change que ce que vous voyez à l’écran.

Une pause nourrissage sort la pompe de son programme pendant un moment, et sur votre téléphone le programme ne reprend que tant que la page de la pompe reste ouverte. Voir [Pause nourrissage](/help/mobile-device-control#jecod-feeding).

## L’éditeur de programme

Chaque écran de programme a les trois mêmes parties.

En haut se trouve le graphique de la journée. Il montre toute la journée de 0 à 24 heures, et chaque période y forme un bloc dont la hauteur correspond à l’intensité. C’est le moyen le plus rapide de vérifier qu’un programme fait bien ce que vous pensez.

Sous le graphique se trouve la liste des périodes. Chacune indique ses horaires, son mode et son intensité, par exemple *Aléatoire, 00:00–03:00, Fréq 50 %, 40 %*. C’est ici que vous ajoutez, modifiez et retirez des périodes.

Touchez **Ajouter au programme** pour ajouter une période. Pour en changer une, ouvrez-la et touchez **Enregistrer**. Pour la retirer, touchez **Supprimer** et confirmez.


:::warning Enregistrer écrit le programme dans l’appareil
Quand vous enregistrez, Cora envoie le programme à l’équipement, qui l’exécute avec sa propre horloge. Il continue de tourner, que Cora puisse le joindre ou non.
:::

## Copier un programme d’une pompe à l’autre

Si plusieurs pompes doivent se comporter de la même façon, créez un programme et copiez-le.

Ouvrez la pompe qui a le programme voulu, touchez **Copier le programme vers…** et choisissez la pompe de destination.

## Garder et partager un programme

Une fois que vous avez un programme qui vous plaît, vous n’avez pas à le refaire.

- **Enregistrer le programme sous…** le garde sous un nom. **Programmes enregistrés…** le réapplique plus tard.
- **Partager ce programme** le transforme en code court. **Coller un code de programme…** applique un code qu’on vous a envoyé. C’est une fonction de Cora Mobile. Le code ne contient que le programme. Il ne donne à personne l’accès à votre compte.

## Loin du réseau de la pompe

Quand votre téléphone n’est pas sur le réseau de la pompe, Cora Mobile passe par le Cora Max de l’aquarium. Quelques points fonctionnent différemment.

- **Identique toute la journée** et **Programme** changent le mode de la pompe par ce Cora Max.
- Une période que vous ajoutez ou modifiez ne passe que si ce Cora Max a joint la pompe dans la dernière heure. Sinon, le programme vous le dit, et vous ne pouvez pas le changer d’où vous êtes.
- **Copier le programme vers…**, **Enregistrer le programme sous…**, **Programmes enregistrés…**, **Partager ce programme** et **Coller un code de programme…** demandent que votre téléphone soit sur le réseau de la pompe. En attendant, ils sont grisés et le menu vous explique pourquoi.

Sans Cora Max à l’aquarium, vous ne pouvez changer une pompe que lorsque votre téléphone est sur son réseau. Plus de détails dans [Connecter votre équipement](/help/mobile-connections#local-only).

Une pompe Bluetooth n’est joignable que depuis un téléphone proche. Restez à portée pour changer son mode, modifier son programme ou utiliser l’un de ces éléments de menu.

## Appliquer un programme

Vous pouvez donner à une pompe un programme enregistré en une seule étape, sans recréer les périodes. Ouvrez la pompe, touchez **Plus** en haut et choisissez **Programmes enregistrés…**. La liste contient tous les programmes enregistrés pour cet aquarium, y compris ceux créés sur une autre pompe. Choisissez-en un et touchez **Appliquer**. Il remplace toute la journée de la pompe.

## Vérifier que c’est passé

Après l’enregistrement, la page de l’appareil affiche le programme que la pompe exécute. S’il ne correspond pas à ce que vous avez enregistré, le changement n’est pas passé. Vérifiez que l’appareil est joignable et réessayez.
