---
title: Ajouter, modifier et retirer des appareils
description: Ajoutez un équipement à Cora, attribuez-le à un aquarium, renommez-le, vérifiez qu’il fonctionne bien et retirez-le, le tout depuis l’onglet Appareils.
section: Cora Mobile
reviewed: 2026-10-13
order: 11
group: Equipment
twin: max-devices
---

L’onglet **Appareils** est l’endroit où vous ajoutez, attribuez, renommez, vérifiez et retirez chaque équipement. Les appareils sont regroupés par marque, et vous pouvez replier chaque groupe.

![L’onglet Appareils](img/mobile-devices.webp "L’équipement est regroupé par marque. Chaque groupe se replie.")

## Ajouter un équipement {#adding-equipment}

1. Dans l’onglet **Appareils**, touchez **Ajouter un appareil**.
2. Choisissez la marque : **Cora**, **Neptune Apex**, **Red Sea**, **Jecod** ou **AquaWiz**.
3. Suivez les étapes de la marque. Selon la marque, c’est une recherche sur le réseau, une adresse IP, une connexion à un compte ou une clé d’appareil. [Connecter votre équipement](/help/mobile-connections) donne les étapes pour chaque marque.
4. Choisissez l’aquarium auquel il appartient.

![La liste des marques dans Ajouter un appareil](img/mobile-add-device-brands.webp "Choisissez la marque de l’appareil que vous ajoutez.")



:::note Sans Cora Max, certains équipements sont uniquement locaux
Les équipements Neptune Apex, Red Sea et Jecod sont joints par votre réseau domestique ou en Bluetooth. Sans Cora Max, l’écran d’ajout indique *Sans Cora Max, cette intégration fonctionne uniquement en local dans l'application Mobile.* Votre téléphone ne le lit et ne le commande que tant qu’il est sur le même réseau (ou à portée Bluetooth). Loin de chez vous, vous voyez les dernières mesures enregistrées par votre téléphone et ne pouvez pas le commander. Un Cora Max à l’aquarium le lit jour et nuit et transmet vos commandes. Plus de détails dans [Connecter votre équipement](/help/mobile-connections#local-only).
:::

Quand vous ajoutez un équipement depuis votre réseau, votre téléphone doit être sur le même réseau que l’équipement.

### Capacité Bluetooth {#bluetooth-capacity}

Un Cora Max partage son Bluetooth entre tous les équipements qu’il lit, il ne peut donc suivre qu’un certain nombre d’appareils. Quand vous ajoutez une pompe Jecod qui se connecte en Bluetooth, Cora vérifie d’abord à quel point le Cora Max de l’aquarium est occupé. En général, vous ne voyez rien. Sinon, l’un de ces deux messages apparaît :

- **Le Bluetooth devient chargé** : *Ce Cora Max approche de sa limite Bluetooth. Davantage d'appareils pourraient être mis à jour moins souvent. Ajoutez un second Cora Max si vous prévoyez d'en ajouter d'autres.* Touchez **Continuer** pour ajouter quand même l’appareil, ou **Annuler**.
- **Limite Bluetooth atteinte** : *Ce Cora Max a atteint sa limite Bluetooth. Ajoutez un second Cora Max pour ces appareils.* L’appareil n’est pas ajouté. Touchez **OK**.

Cora vérifie le Cora Max principal de l’aquarium ou, si aucun n’est choisi, le Cora Max qui a le plus de place. Plus de détails dans [Plusieurs appareils Cora](/help/mobile-multi-device#primary-cora-max).

## Associer un Cora Max {#pairing-a-cora-max}

![L’écran Ajoutez votre Cora dans Cora Mobile, en recherche d’appareils](img/mobile-add-device.webp "Ajouter un appareil, puis Cora. Cora Mobile cherche sur votre Wi-Fi et en Bluetooth, avec la saisie manuelle de l’adresse IP en dessous.")

**Cora** est la façon d’associer un nouveau Cora Max. Il trouve les appareils déjà sur votre Wi-Fi, ou ceux à proximité en Bluetooth. S’il ne trouve pas le vôtre, utilisez **Saisir l’adresse IP manuellement** sur le même écran. La procédure complète est dans [Configurer Cora Max](/help/max-setup).

## La page d’un appareil {#a-devices-page}

Touchez n’importe quel appareil de la liste pour ouvrir sa page. Ses commandes viennent en premier, puis des sections qui fonctionnent de la même façon pour toutes les marques.

- **État** affiche le **Modèle**, le **N° de série**, le **Micrologiciel** et la dernière fois que Cora a eu de ses nouvelles (**Dernière connexion**).
- **Aquariums** indique à quel aquarium (ou à quels aquariums) il est attribué. Touchez **Modifier** pour le réattribuer.
- **Connexion** est l’endroit où vous modifiez son adresse IP, ses identifiants ou sa clé d’appareil.
- **Retirer l'appareil**, en bas.

Cora Max et Neptune Apex peuvent servir plusieurs aquariums, leur choix d’aquarium est donc une liste à cocher. Cora Max peut être attribué à quatre aquariums au plus. Voir [Plus d’un appareil Cora](/help/mobile-multi-device). Tout le reste sert un seul aquarium à la fois. En choisir un autre y déplace l’appareil et le retire de l’ancien.

:::warning Attribuez l’aquarium avant de vous fier aux mesures
Un appareil sans aquarium transmet quand même, mais ses chiffres ne vont nulle part. Si un appareil que vous venez d’ajouter n’apparaît sur aucun tableau de bord, vérifiez cela en premier.
:::

Ce que font les commandes de chaque marque est expliqué dans [Contrôler votre équipement](/help/mobile-device-control).

## Renommer {#renaming}

Ouvrez l’appareil et touchez le crayon à côté de son nom. Utilisez le nom que vous lui donnez au quotidien, comme « Remontée », « Gyre gauche » ou « Chauffage décantation ». Le nom apparaît sur les widgets, dans les alertes et dans tout ce que vous demandez à Cora.

Les noms peuvent faire jusqu’à 40 caractères. Laissez le nom vide pour revenir au nom propre de l’appareil. Si deux appareils du même type n’ont pas de nom, Cora les distingue par un code court après le nom. Cora n’utilise jamais un numéro de série comme nom.

Le nouveau nom ne s’applique que dans Cora. Il ne change pas le nom dans l’application du fabricant.

## Vérifier qu’un appareil fonctionne bien {#health}

Chaque appareil est une ligne de l’onglet Appareils, avec son icône, son nom, son modèle et son aquarium. Le point sur la ligne indique son état.

| Point | Signification |
|---|---|
| Gris | Cora ne sait pas encore |
| Vert | Fonctionne normalement |
| Orange | Un avertissement ou une panne |
| Rouge | Hors ligne |

Pour en savoir plus, ouvrez l’appareil. Sa section **État** indique la dernière fois que Cora a eu de ses nouvelles. Vous voulez une heure récente et aucun avertissement.

| Ce que vous voyez | Signification |
|---|---|
| Une heure de mise à jour récente | Fonctionne normalement |
| « Mis à jour il y a 3 h » sur un appareil qui ne transmet que toutes les quelques heures | Rien d’anormal |
| « Impossible de joindre… » | Un problème de réseau, ou l’appareil est éteint |
| « … a refusé la connexion » | Le compte du fabricant doit être reconnecté. Ouvrez l’appareil et reconnectez-vous |
| Des mesures plus anciennes pendant votre absence | Normal pour Apex, Red Sea et Jecod sans Cora Max à l’aquarium (voir plus haut) |
| Rien du tout | Il n’a jamais transmis. Vérifiez l’attribution à l’aquarium et la connexion |

Quand un appareil ne remonte plus de mesures, Cora peut vous alerter. Les délais sont dans [Alertes et seuils](/help/mobile-alerts). Pour tout le reste, voir [Résolution de problèmes](/help/troubleshooting).

## Retirer un appareil {#removing-a-device}

Ouvrez l’appareil et touchez **Retirer l'appareil**, ou balayez sa ligne vers la gauche dans l’onglet Appareils. Cora vous demande de confirmer : *« {name} sera retiré de Cora. L'appareil lui-même n'est ni réinitialisé ni modifié. »*

**Vos mesures sont conservées.** Retirer un appareil arrête la collecte de nouvelles données par Cora. L’historique déjà recueilli reste sur l’aquarium, et tout widget qui l’utilisait garde ses mesures passées.

Vous perdez le lien en direct. Si l’appareil se connectait par un compte de fabricant, vous perdez aussi les identifiants enregistrés : il faudra vous reconnecter si vous l’ajoutez à nouveau.

:::tip Faire taire un appareil bruyant sans le retirer
Si un appareil fonctionne bien mais alerte trop souvent, changez ses seuils ou ses réglages de notification dans [Alertes et seuils](/help/mobile-alerts). Vous gardez la connexion et les données, et le bruit s’arrête.
:::
