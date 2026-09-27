---
title: Programmer l’équipement
description: Créez un programme journalier pour une pompe Jecod, copiez-le vers d’autres pompes, et consultez le programme d’une pompe Maxspect (bêta).
section: Cora Mobile
reviewed: 2026-09-17
order: 12
group: Equipment
---

Les pompes, dont les pompes Gyre, peuvent suivre un **programme journalier**. C’est une suite de périodes, chacune avec sa propre intensité, qui se répète tous les jours. Cora peut créer ces programmes directement pour les pompes Jecod. Pour une pompe Maxspect *(bêta)*, vous pouvez seulement consulter le programme ici. Il se règle dans l’application Maxspect.

Ouvrez l’appareil depuis l’onglet **Appareils**.

![Le programme d’une pompe](img/mobile-schedules.webp "Le graphique journalier sur 0 à 24 heures, avec chaque période listée en dessous.")

## Constant toute la journée, ou Programme

Une pompe fonctionne dans l’un de ces deux modes, à choisir en haut de sa page :

- **Constant toute la journée** : une seule intensité, en continu
- **Programme** : un programme journalier découpé en périodes

Votre choix est envoyé à la pompe. Si votre téléphone n’est pas sur le réseau de la pompe, il passe par le Cora Max de l’aquarium. Une pompe Bluetooth doit être à portée. Tant qu’elle ne l’est pas, votre choix ne change que l’affichage.

## L’éditeur de programme

Chaque écran de programme a trois parties.

**Le graphique de la journée** couvre les 24 heures. Chaque période y forme un bloc dont la hauteur correspond à l’intensité. C’est le moyen le plus rapide de vérifier qu’un programme fait bien ce que vous pensez.

**La liste des périodes**, sous le graphique, indique pour chacune ses horaires, son mode et son intensité, par exemple *Aléatoire, 00:00–03:00, Fréq 50 %, 40 %*. C’est ici que vous ajoutez, modifiez et retirez des périodes.

Pour **ajouter ou modifier une période**, touchez **Ajouter au programme** pour en créer une. Ouvrez une période pour la modifier, puis touchez **Enregistrer**, ou **Supprimer** pour la retirer. Cora vous demande de confirmer avant de la supprimer.

Une pompe Maxspect *(bêta)* a deux têtes, Gyre A et Gyre B. Son graphique a donc deux pistes, une par tête, et ses plans sont listés sous **GYRE A** et **GYRE B**. Son programme est en lecture seule. La ligne d’action indique **Lecture seule**, et le programme se règle dans l’application Maxspect.

:::warning Le programme est écrit dans l’appareil
Quand vous enregistrez, le programme est envoyé à l’équipement, qui le suit ensuite avec sa propre horloge. Il continue de tourner, que Cora soit joignable ou non.
:::

## Copier un programme vers une autre pompe

Si plusieurs pompes doivent se comporter de la même façon, créez un programme puis copiez-le.

Ouvrez la pompe dont vous voulez reprendre le programme, touchez **Copier le programme vers…**, puis choisissez la pompe de destination.

## Garder et partager un programme

Un programme qui vous convient n’est pas à refaire.

- **Enregistrer le programme sous…** le garde sous un nom. Vous le réappliquez plus tard depuis **Programmes enregistrés…**.
- **Partager ce programme** le transforme en code court. **Coller un code de programme…** applique un code qu’on vous a envoyé. Cette fonction est propre à Cora Mobile. Le code contient le programme, et ne donne aucun accès à votre compte.

## Loin du réseau de la pompe

Quand votre téléphone n’est pas sur le réseau de la pompe, Cora Mobile passe par le Cora Max de l’aquarium, avec quelques limites.

- **Constant toute la journée** et **Programme** changent le mode de la pompe par ce Cora Max.
- Une période ajoutée ou modifiée ne passe par lui que s’il a joint la pompe dans la dernière heure. Sinon, le programme l’indique, et vous ne pouvez pas le modifier d’où vous êtes.
- **Copier le programme vers…**, **Enregistrer le programme sous…**, **Programmes enregistrés…**, **Partager ce programme** et **Coller un code de programme…** demandent que votre téléphone soit sur le réseau de la pompe. En attendant, ces options sont grisées et le menu explique pourquoi.

Une pompe Bluetooth n’est joignable que depuis un téléphone proche. Restez à portée pour changer son mode, modifier son programme ou utiliser l’une de ces options.

## Appliquer un programme

Vous pouvez donner à une pompe un programme enregistré en une seule étape, sans recréer les périodes. Ouvrez la pompe, touchez **Plus** en haut et choisissez **Programmes enregistrés…**. La liste contient tous les programmes enregistrés pour cet aquarium, y compris ceux créés sur une autre pompe. Choisissez-en un et touchez **Appliquer**. Il remplace toute la journée de la pompe.

## Vérifier que le programme est passé

Après l’enregistrement, la page de l’appareil affiche le programme que la pompe exécute vraiment. S’il ne correspond pas au vôtre, l’écriture a échoué. Vérifiez que l’appareil est joignable et réessayez.
