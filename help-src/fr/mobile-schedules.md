---
title: Programmer l’équipement
description: Créez le programme d’une pompe Jecod dans l’éditeur, copiez-le depuis ou vers d’autres pompes, enregistrez-le, partagez-le et vérifiez que la pompe l’a pris.
section: Cora Mobile
reviewed: 2026-11-03
order: 14
group: Equipment
---

Cette page explique comment donner à une pompe Jecod un **programme journalier** : un ensemble de périodes, chacune avec sa propre intensité, qui se répète tous les jours. Ouvrez-le depuis **Appareils** → touchez la pompe.

Les lampes et pompes d’autres marques gardent leurs programmes sur leurs propres pages : les ReefDose de Red Sea dans [Contrôler votre équipement](/help/mobile-device-control#red-sea).

![La page d’une pompe Jecod dans Cora Mobile avec Programme choisi](img/mobile-schedules.webp "Programme choisi en haut, la pause nourrissage, puis le graphique de la journée.")

## Manuel, ou Programme {#same-all-day-or-schedule}

Une pompe fonctionne dans l’un de ces deux modes. Choisissez-en un avec le sélecteur de sa page. Celui qui fonctionne est marqué *· en cours*, et la page s’ouvre dessus.

- **Manuel** tourne à une seule intensité en continu.
- **Programme** suit un programme journalier fait de périodes.

Cora envoie votre choix directement à la pompe quand votre téléphone est sur son réseau. Sinon, il passe par le Cora Max de l’aquarium. Une pompe Bluetooth doit être à portée. Tant qu’elle ne l’est pas, votre choix ne change que ce que vous voyez à l’écran.

Une pause nourrissage sort la pompe de son programme pendant un moment, et sur votre téléphone le programme ne reprend que tant que la page de la pompe reste ouverte. Voir [Pause nourrissage](/help/mobile-device-control#jecod-feeding).

## L’éditeur de programme

Chaque écran de programme a les trois mêmes parties.

En haut se trouve le graphique de la journée. Il montre toute la journée de 0 à 24 heures, et chaque période y forme un bloc dont la hauteur correspond à l’intensité. C’est le moyen le plus rapide de vérifier qu’un programme fait bien ce que vous pensez.

Sous le graphique se trouve la liste des périodes. Chacune indique ses horaires, son mode et son intensité, par exemple *Aléatoire, 00:00–03:00, Fréq 50 %, 40 %*. C’est ici que vous ajoutez, modifiez et retirez des périodes.

Toute modification d’un programme passe par l’éditeur. **Modifier** l’ouvre sur la journée de la pompe, tout comme toucher une période ou **Ajouter au programme** sur la page de la pompe : l’éditeur s’ouvre avec cette période, ou une nouvelle, prête à être modifiée. Dans l’éditeur, changez une période et touchez **Enregistrer**, ou retirez-la avec **Supprimer la plage**. **Annuler** revient en arrière. Le menu ⋮ contient **Enregistrer le programme sous…**, **Programmes enregistrés…** et **Copier depuis…**.

Rien n’est envoyé à la pompe avant que vous touchiez **Enregistrer sur la pompe**. Cora écrit alors toute la journée d’un coup. S’il n’y parvient pas, l’éditeur en donne la raison et garde vos modifications. Si vous fermez l’éditeur avant d’enregistrer, Cora demande d’abord *Abandonner ces changements ?*


:::warning Enregistrer sur la pompe écrit le programme dans l’appareil
Quand vous touchez **Enregistrer sur la pompe**, Cora envoie le programme à l’équipement, qui l’exécute avec sa propre horloge. Il continue de tourner, que Cora puisse le joindre ou non.
:::

## Copier un programme d’une pompe à l’autre {#copying-a-program-between-pumps}

Si plusieurs pompes doivent se comporter de la même façon, créez un programme et copiez-le. Vous pouvez copier dans les deux sens, et rien n’est envoyé avant que vous touchiez **Enregistrer sur la pompe**.

- **Copier depuis…** (dans le menu ⋮ du programme et dans celui de l’éditeur) reprend le programme d’une autre pompe de brassage, sur n’importe lequel de vos aquariums. Chaque période reçoit le mode le plus proche dont dispose cette pompe, les vitesses sont limitées à ce qu’elle peut faire, et **Ce qui change sur cette pompe** liste chaque changement. **Charger dans l’éditeur** place la copie dans l’éditeur de cette pompe, où vous pouvez l’ajuster puis toucher **Enregistrer sur la pompe**. Une pompe dont Cora n’a pas encore lu le programme est grisée, avec la raison.
- **Copier le programme vers…** donne la journée de cette pompe à d’autres pompes de n’importe lequel de vos aquariums, chacune listée sous la forme *Aquarium · Pompe*. Cochez les pompes et touchez **Vérifier**. Rien n’est encore envoyé. **Vérifier les copies** liste chaque pompe avec son état, **Non enregistré**, **Enregistré sur la pompe** ou **Échec** avec la raison, et le nombre de changements qu’elle reçoit. **Ouvrir l'éditeur** ouvre l’éditeur propre de cette pompe sur la journée copiée, avec son propre **Enregistrer sur la pompe**, qui l’envoie à cette pompe seulement. Si un enregistrement échoue, le brouillon est gardé pour que vous puissiez réessayer. Si vous partez alors que certaines pompes ne sont pas enregistrées, Cora demande d’abord *Abandonner les copies non enregistrées ?*

## Garder et partager un programme

Une fois que vous avez un programme qui vous plaît, vous n’avez pas à le refaire.

- **Enregistrer le programme sous…** le garde sous un nom. **Programmes enregistrés…** le retrouve plus tard : **Charger dans l’éditeur** l’ouvre dans l’éditeur, et **Enregistrer sur la pompe** l’envoie.
- **Partager ce programme** le transforme en code court. **Coller un code de programme…** charge dans l’éditeur un code qu’on vous a envoyé, et rien n’est envoyé avant que vous touchiez **Enregistrer sur la pompe**. C’est une fonction de Cora Mobile. Le code ne contient que le programme. Il ne donne à personne l’accès à votre compte.

## Loin du réseau de la pompe

Quand votre téléphone n’est pas sur le réseau de la pompe, Cora Mobile passe par le Cora Max de l’aquarium. Quelques points fonctionnent différemment.

- **Manuel** et **Programme** changent le mode de la pompe par ce Cora Max.
- Un programme que vous enregistrez sur la pompe ne passe que si ce Cora Max a joint la pompe dans la dernière heure. Sinon, le programme vous le dit, et vous ne pouvez pas le changer d’où vous êtes.
- **Copier le programme vers…**, **Enregistrer le programme sous…**, **Programmes enregistrés…**, **Partager ce programme** et **Coller un code de programme…** demandent que votre téléphone soit sur le réseau de la pompe. En attendant, ils sont grisés et le menu vous explique pourquoi.

Sans Cora Max à l’aquarium, vous ne pouvez changer une pompe que lorsque votre téléphone est sur son réseau. Plus de détails dans [Connecter votre équipement](/help/mobile-connections#local-only).

Une pompe Bluetooth n’est joignable que depuis un téléphone proche. Restez à portée pour changer son mode, modifier son programme ou utiliser l’un de ces éléments de menu.

## Appliquer un programme

Vous pouvez donner à une pompe un programme enregistré en une seule étape, sans recréer les périodes. Ouvrez la pompe, touchez **Plus** en haut et choisissez **Programmes enregistrés…**. La liste contient tous les programmes enregistrés pour cet aquarium, y compris ceux créés sur une autre pompe. Choisissez-en un et touchez **Charger dans l’éditeur**. Vérifiez-le dans l’éditeur, puis touchez **Enregistrer sur la pompe**. Il remplace toute la journée de la pompe.

## Vérifier que c’est passé

Après l’enregistrement, la page de l’appareil affiche le programme que la pompe exécute. S’il ne correspond pas à ce que vous avez enregistré, le changement n’est pas passé. Vérifiez que l’appareil est joignable et réessayez.
