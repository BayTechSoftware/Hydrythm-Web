---
title: Ajouter, modifier et retirer des appareils
description: Comment ajouter un équipement à Cora, l’attribuer à un aquarium, le renommer, et le retirer proprement.
section: Cora Mobile
reviewed: 2026-09-27
order: 9
group: Equipment
---

L’onglet **Appareils** contient tout ce que vous avez connecté, regroupé par marque. Chaque groupe se replie pour qu’une pièce de récif pleine d’équipement reste lisible.

![L’onglet Appareils](img/mobile-devices.webp "L’équipement est regroupé par marque. Chaque groupe se replie.")

## Ajouter un équipement

Trois boutons se trouvent sous la liste, et ils font des travaux différents :

| Bouton | Ajoute |
|---|---|
| **Ajouter un appareil** | Un Cora Max. Trouve les unités déjà sur votre Wi-Fi, ou les unités proches par Bluetooth. **Saisir l’adresse IP manuellement** se trouve dans cet écran si la découverte ne le trouve pas. |
| **Trouver une pompe sur votre réseau** | Les pompes Jecod qui s’annoncent sur le réseau local |
| **Ajouter AquaWiz** | Un contrôleur AquaWiz, via votre compte AquaWiz |

![Ajouter un Cora Max](img/mobile-add-device.webp "Ajouter un appareil recherche un Cora Max sur le Wi-Fi et le Bluetooth.")

Les autres équipements (Neptune Apex et Red Sea ReefBeat) se connectent depuis l’aquarium plutôt que depuis cette liste. Voir [Connecter votre équipement](/help/mobile-connections).

Ajouter un équipement comme un chauffage, une pompe ou un écumeur propose une **saisie automatique** de marque et de modèle : commencez à taper et Cora suggère à partir d’une longue liste sourcée de marques d’équipement. Si la vôtre n’est pas listée, tapez-la quand même ; Cora garde tout ce que vous saisissez.

:::note Cora et votre téléphone ont besoin du même réseau
L’équipement découvert localement doit être sur le même réseau que votre téléphone quand vous l’ajoutez. **Après la configuration, il n’est toujours accessible que sur ce réseau** (ou par Bluetooth, pour les unités qui l’utilisent), à moins qu’un appareil Cora présent sur les lieux puisse l’atteindre pour vous.

Un équipement qui se lit correctement chez vous peut donc afficher des valeurs plus anciennes pendant que vous êtes absent, à moins qu’un Cora Max sur les lieux puisse l’interroger. Cela reflète depuis où l’équipement est accessible, plutôt qu’un défaut.
:::

## Attribuer un appareil à un aquarium

La plupart des équipements appartiennent exactement à un aquarium, et c’est ce qui fait apparaître leurs mesures sur le tableau de bord de cet aquarium.

**Cora Max est l’exception** : il peut être attribué à jusqu’à quatre aquariums et bascule entre eux à l’écran. Voir [Plus d’un appareil Cora](/help/mobile-multi-device).

Ouvrez l’appareil et choisissez **Aquarium**. Si vous gérez plus d’un système, c’est le réglage qui compte le plus : un chauffage attribué au mauvais aquarium rapporte parfaitement bien au mauvais endroit.

:::warning Attribuez l’aquarium avant de compter sur les mesures
Un appareil sans aquarium rapporte tout de même, mais ses chiffres n’ont nulle part où se poser. Si un appareil que vous venez d’ajouter n’apparaît pas sur un tableau de bord, vérifiez cela d’abord.
:::

## Renommer

Ouvrez l’appareil et modifiez son nom. Utilisez le nom que vous employez pour lui au quotidien : « Remontée », « Pompe de brassage gauche », « Chauffage du sump ». Le nom apparaît sur les widgets, dans les alertes et dans tout ce que vous demandez à Cora, donc un nom qui a un sens pour vous rend tout ce qui en découle plus clair.

Renommer est local à Cora. Cela ne change pas le nom dans l’application propre du fabricant.

## Vérifier si un appareil est en bon état

Chaque ligne affiche son état actuel. Ce que vous voulez voir est une heure de mise à jour récente et aucun avertissement.

| Ce que vous voyez | Ce que cela signifie |
|---|---|
| Une heure de mise à jour récente | Fonctionne normalement |
| « Mis à jour il y a 3 h » sur quelque chose qui rapporte toutes les heures | Normal |
| « Impossible d’atteindre… » | Un problème de réseau, ou l’appareil est éteint |
| « …a refusé la connexion » | Le compte du fabricant doit être reconnecté ; ouvrez l’appareil et reconnectez-vous |
| Rien du tout | Il n’a jamais rapporté ; vérifiez l’attribution de l’aquarium et la connexion |

## Retirer un appareil

Ouvrez l’appareil et choisissez **Retirer**. On vous demandera de confirmer, et on vous dira exactement ce qui est retiré.

**Vos mesures sont conservées.** Retirer un appareil arrête Cora de collecter de nouvelles données depuis celui-ci ; l’historique déjà rassemblé reste sur l’aquarium, et tout widget qui le pointe garde ses mesures passées.

Ce que vous perdez, c’est le lien en direct, et, quand l’appareil se connectait via un compte de fabricant, la connexion enregistrée. L’ajouter à nouveau signifie se reconnecter.

:::tip Faire taire un appareil bruyant sans le retirer
Si un appareil fonctionne correctement mais alerte trop souvent, ajustez ses seuils ou ses réglages de notifications ; voir **[Alertes et seuils](/help/mobile-alerts)**. Cela garde la connexion et les données tout en arrêtant le bruit.
:::
