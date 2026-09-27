---
title: Mises à jour et récupération
description: Comment Cora Max se met à jour tout seul, et que faire si une mise à jour échoue.
section: Cora Max
reviewed: 2026-09-09
order: 14
group: Settings
---

## Mises à jour automatiques

Cora Max se met à jour tout seul. Les nouvelles versions se téléchargent en arrière-plan et s’installent d’elles-mêmes, et Cora Max vous dit ce qui a changé.

Vous n’avez rien à faire pour rester à jour.

## Voir la version

![Réglages de l’appareil](img/max-updates.webp "Mise à jour du micrologiciel, dans la section Réseau et mises à jour des Réglages Cora Max.")

Dans **Réglages → Réglages Cora Max → Mise à jour du micrologiciel** (section **Réseau et mises à jour**), vous pouvez chercher une mise à jour, l’installer, et choisir le canal de mise à jour et son horaire. Plus bas sur le même écran, la section **État** indique pour chaque aquarium l’état de l’interrogation, la dernière interrogation et la dernière écriture dans le cloud.

## Quand une mise à jour est prête

Un message décrit les nouveautés et vous propose deux choix :

- **Mettre à jour maintenant** : l’installation se fait tout de suite, puis Cora Max redémarre
- **Reporter de 3 heures** : le message reviendra plus tard

Si vous ne faites rien, la mise à jour s’installe pendant la nuit, vers 3 à 5 heures du matin. Cora Max ne redémarre donc pas pendant que vous le regardez.

:::note Vos mesures ne se perdent pas pendant une mise à jour
Vos données sont gardées dans votre compte, pas sur l’écran. Après un redémarrage, Cora Max retrouve les mêmes aquariums, tableaux de bord et historique.
:::

## Récupération

La récupération est un mode de maintenance. Elle sert quand Cora Max ne démarre pas normalement, ou quand vous devez réparer sa configuration sans ordinateur.

Pour y entrer, posez **cinq doigts** en haut à droite de l’écran pendant environ **dix secondes**, puis saisissez le **Code PIN de récupération** de l’appareil.

Ce code à six chiffres s’est affiché lors de l’appairage. Vous le retrouvez aussi dans les réglages de cet appareil dans Cora Mobile. Cora Max ne l’affiche jamais, pour qu’un invité ou un enfant appuyé contre l’écran ne puisse pas entrer en récupération.

En récupération, vous pouvez :

- réparer la connexion **Wi-Fi**
- choisir **Réappairer** pour reconnecter l’appareil à votre compte
- forcer une **mise à jour du micrologiciel**
- lancer une **Réinitialisation d’usine**

Si Cora Max n’arrive pas à démarrer plusieurs fois de suite, il peut aussi revenir tout seul à la version précédente.

:::warning En récupération, Cora Max ne commande rien
Votre contrôleur continue de suivre sa propre programmation. Mais si une [automatisation](/help/mobile-automation) doit passer **par ce Cora Max** pour agir, elle ne peut pas s’exécuter tant qu’il est en récupération. La règle se déclenche, mais l’action n’arrive pas jusqu’au matériel.
:::

## Si Cora Max ne redémarre pas

Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** en indiquant la version et ce qui s’affiche à l’écran. Ne réappairez pas l’appareil avant. L’état de l’appairage aide souvent à comprendre ce qui s’est passé.
