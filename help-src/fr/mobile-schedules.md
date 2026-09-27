---
title: Programmer l’équipement
description: Créez un programme journalier pour une pompe Jecod et copiez-le entre pompes, et consultez le programme d’une pompe de brassage Maxspect (bêta).
section: Cora Mobile
reviewed: 2026-09-17
order: 12
group: Equipment
---

Les pompes et pompes de brassage peuvent exécuter un **programme journalier** : un ensemble de périodes, chacune avec sa propre intensité, qui se répète chaque jour. Cora peut les créer directement pour les pompes Jecod. Le programme d’une pompe de brassage Maxspect *(bêta)* ne peut être que consulté ici : réglez-le dans l’application Maxspect.

Ouvrez l’appareil depuis l’onglet **Appareils**.

![Le programme d’une pompe](img/mobile-schedules.webp "Le graphique journalier sur 0 à 24 heures, avec chaque période listée en dessous.")

## Constant toute la journée, ou Programme

Une pompe fonctionne selon l’un de deux modes, choisi en haut de sa page :

- **Constant toute la journée** : une intensité, en permanence
- **Programme** : un programme journalier avec des périodes

Votre choix est envoyé à la pompe, via le Cora Max de l’aquarium quand votre téléphone n’est pas sur le réseau de la pompe. Une pompe Bluetooth doit être à portée : jusqu’à ce qu’elle le soit, choisir ici ne change que ce que vous regardez.

## L’éditeur de programme

Chaque écran de programme a les mêmes trois parties :

**Le graphique journalier** : toute la journée de 0 à 24 heures, avec chaque période dessinée comme un bloc dont la hauteur est son intensité. C’est la façon la plus rapide de voir si un programme fait ce que vous pensez.

**La liste des périodes** : chaque période sous le graphique, avec ses heures, son mode et son intensité : *Aléatoire, 00:00–03:00, Fréq 50 %, 40 %*. Ajoutez, modifiez et retirez des périodes ici.

**Ajouter et modifier des périodes** : **Ajouter au programme** ajoute une période. Ouvrez une période pour la modifier et touchez **Enregistrer**, ou **Supprimer**-la ; on vous demande de confirmer avant qu’elle ne parte.

Une pompe de brassage Maxspect *(bêta)* a deux têtes, affichées comme Gyre A et Gyre B, donc son graphique journalier a deux pistes, une pour chacune, et ses plans sont listés sous **GYRE A** et **GYRE B**. Le programme d’une pompe de brassage est en lecture seule : sa ligne d’action indique **Lecture seule**, et le programme se règle dans l’application Maxspect.

:::warning Un programme est écrit sur l’appareil
Enregistrer envoie le programme à l’équipement, qui l’exécute ensuite selon sa propre horloge. Il continue de s’exécuter que Cora soit accessible ou non.
:::

## Copier un programme entre pompes

Si vous gérez plusieurs pompes qui devraient se comporter de la même façon, créez un programme et copiez-le.

Ouvrez la pompe dont vous voulez le programme, puis **Copier le programme vers…**, et choisissez la pompe vers laquelle le copier.

## Garder et partager un programme

Un programme dont vous êtes satisfait n’a pas besoin d’être recréé :

- **Enregistrer le programme sous…** le garde sous un nom, et **Programmes enregistrés…** l’applique à nouveau plus tard.
- **Partager ce programme** le transforme en un code court, et **Coller un code de programme…** applique celui que quelqu’un vous a envoyé. C’est une fonctionnalité de Cora Mobile ; le code porte le programme, pas un accès à votre compte.

## Loin du réseau de la pompe

Quand votre téléphone n’est pas sur le réseau de la pompe, Cora Mobile fonctionne via le Cora Max de l’aquarium, avec des limites :

- **Constant toute la journée** et **Programme** commutent la pompe via ce Cora Max.
- Une période que vous ajoutez ou modifiez passe par lui seulement s’il a atteint la pompe dans la dernière heure. Si ce n’est pas le cas, le programme le dit et ne peut pas être changé de là où vous êtes.
- **Copier le programme vers…**, **Enregistrer le programme sous…**, **Programmes enregistrés…**, **Partager ce programme** et **Coller un code de programme…** nécessitent que votre téléphone soit sur le réseau de la pompe. Jusqu’à ce moment-là, ces options sont grisées, et le menu indique pourquoi.

Une pompe Bluetooth ne peut être atteinte que depuis un téléphone à proximité : restez à portée pour la commuter, changer son programme ou utiliser l’un de ces éléments.

## Appliquer un programme

Une pompe peut aussi recevoir un programme préparé en une seule étape, plutôt qu’en créant des périodes à la main.

## Vérifier que cela a fonctionné

Après l’enregistrement, la page de l’appareil affiche le programme réellement exécuté par l’unité. Si les deux ne correspondent pas, l’écriture n’a pas abouti ; vérifiez que l’appareil est accessible et réessayez.
