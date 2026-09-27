---
title: Mises à jour et récupération
description: Comment Cora Max se met à jour lui-même, et ce qui se passe si une mise à jour échoue.
section: Cora Max
reviewed: 2026-09-09
order: 14
group: Settings
---

## Mises à jour automatiques

Cora Max se maintient à jour. Les nouvelles versions se téléchargent en arrière-plan et s’installent seules ; on vous dit ce qui a changé.

Rien n’est requis de vous pour rester à jour.

## Vérifier la version

![Réglages de l’appareil](img/max-updates.webp "Mise à jour du micrologiciel et état de l’appareil, en haut des réglages de l’appareil.")

**Réglages → Cora Max → Micrologiciel → Mise à jour du micrologiciel** couvre la vérification, l’installation, le canal de mise à jour et son calendrier. **État et commandes de l’appareil** se trouve juste à côté dans le même groupe **Micrologiciel**, et c’est là que vivent les propres diagnostics de l’unité : l’interrogation principale, les liens vers les appareils et le répondeur vocal inclus.

## Quand une mise à jour est disponible

Un message apparaît décrivant les nouveautés, avec deux choix :

- **Mettre à jour maintenant** : installe immédiatement et redémarre
- **Reporter de 3 heures** : redemande plus tard

Sans intervention, une mise à jour s’installe elle-même pendant la nuit, entre environ 3 et 5 heures du matin, pour que l’écran ne redémarre pas pendant que vous le regardez.

:::note Les mesures ne sont pas perdues pendant une mise à jour
Les données vivent dans votre compte, pas sur l’écran. Une unité qui redémarre revient avec les mêmes aquariums, tableaux de bord et historique.
:::

## Récupération

La Récupération est un mode de maintenance pour quand une unité ne démarre pas normalement, ou quand vous devez réparer sa configuration sans ordinateur portable.

**Pour y entrer :** maintenez **cinq doigts** en haut à droite de l’écran pendant environ **dix secondes**, puis saisissez le **Code PIN de récupération** de l’unité.

Ce code PIN à six chiffres a été affiché lors de l’appairage de l’unité, et il se trouve aussi dans les réglages de cet appareil dans Cora Mobile. Il n’est pas affiché sur le Cora Max lui-même, c’est fait pour ça : la récupération ne peut pas être atteinte par un invité, ou par un enfant qui s’appuie sur l’écran.

Depuis la récupération, vous pouvez :

- Réparer la connexion **Wi-Fi**
- **Réappairer** l’unité à votre compte
- Forcer une **mise à jour du micrologiciel**
- **Réinitialiser aux réglages d’usine** l’unité

Une unité qui échoue à démarrer plusieurs fois de suite peut aussi revenir elle-même à la version précédente.

:::warning Un écran en récupération ne contrôle rien
Votre contrôleur continue d’exécuter sa propre programmation. Mais une [automatisation](/help/mobile-automation) dont l’action doit être exécutée **par ce Cora Max** ne peut pas s’exécuter tant qu’il est en récupération ; la règle se déclenche et l’étape n’atteint pas le matériel.
:::

## Si une unité ne redémarre pas

Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** avec la version affichée à l’écran et ce qu’elle indique. Ne réappairez pas l’unité d’abord ; l’état de l’appairage est souvent utile pour comprendre ce qui s’est passé.
