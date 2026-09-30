---
title: Ajouter, modifier et retirer des appareils
description: Ajouter un équipement à Cora, le rattacher à un aquarium et le retirer proprement, le tout depuis un seul endroit.
section: Cora Mobile
reviewed: 2026-09-30
order: 9
group: Equipment
---

Ajoutez, modifiez, rattachez et retirez chaque appareil depuis l’onglet **Appareils**, classé par marque. Chaque groupe peut se replier, pour que la liste reste lisible même avec beaucoup d’équipement.

![L’onglet Appareils](img/mobile-devices.webp "L’équipement est regroupé par marque. Chaque groupe se replie.")

## Ajouter un équipement

Touchez **Ajouter un appareil**, puis choisissez la marque\xa0: **Cora**, **Neptune Apex**, **Red Sea**, **Jecod**, **Maxspect**, **GHL** *(bêta)*, **HYDROS** *(bêta)* ou **AquaWiz**. Chacune ouvre exactement ce dont elle a besoin pour trouver votre équipement\xa0: une recherche sur le réseau, une adresse IP, une connexion ou une clé d’appareil. [Connecter votre équipement](/help/mobile-connections) détaille ce qu’il faut pour chaque marque.

**Cora** sert à appairer un nouveau Cora Max. Cherche les appareils déjà sur votre Wi-Fi, ou ceux à proximité en Bluetooth. Si la recherche ne trouve rien, **Saisir l’adresse IP manuellement** se trouve sur le même écran.

Quand vous ajoutez un équipement comme un chauffage, une pompe ou un écumeur, la marque et le modèle se **complètent automatiquement**. Commencez à taper, et Cora propose des noms tirés d’une longue liste de marques vérifiée à la source. Si la vôtre n’y est pas, tapez-la quand même. Cora garde ce que vous saisissez.

:::note Cora et votre téléphone doivent être sur le même réseau
Un équipement trouvé sur le réseau local doit être sur le même réseau que votre téléphone au moment de l’ajout. **Après l’installation, il reste joignable uniquement sur ce réseau** (ou en Bluetooth pour les appareils qui l’utilisent), sauf si un appareil Cora sur place peut le joindre pour vous.

Un équipement qui s’affiche bien à la maison peut donc montrer des valeurs plus anciennes quand vous êtes absent, sauf si un Cora Max sur place peut l’interroger. Ce n’est pas une panne. Cela dépend simplement de l’endroit d’où l’équipement est joignable.
:::

## La page d’un appareil

Ouvrez n’importe quel appareil depuis la liste. Ses commandes viennent en premier, puis trois sections qui fonctionnent de la même façon pour toutes les marques.

- **Aquariums** indique à quel aquarium (ou à quels aquariums) il est rattaché. Touchez **Modifier** pour changer le rattachement.
- **Connexion** sert à modifier son adresse IP, sa connexion ou sa clé d’appareil.
- **Retirer l'appareil**, tout en bas.

Cora Max, Neptune Apex et GHL peuvent desservir plusieurs aquariums, si bien que leur sélecteur d’aquarium est une liste à cocher. Cora Max peut être rattaché à quatre aquariums au plus. Voir [Plus d’un appareil Cora](/help/mobile-multi-device). Tout le reste, y compris HYDROS, dessert un seul aquarium à la fois\xa0: en choisir un autre y déplace l’appareil et l’enlève de l’ancien.

:::warning Choisissez l’aquarium avant de vous fier aux mesures
Un appareil sans aquarium envoie quand même ses mesures, mais elles ne s’affichent nulle part. Si un appareil que vous venez d’ajouter n’apparaît sur aucun tableau de bord, vérifiez d’abord ce point.
:::

## Renommer

Ouvrez l’appareil et modifiez son nom. Donnez-lui le nom que vous utilisez tous les jours\xa0: « Remontée », « Brassage gauche », « Chauffage décantation ». Ce nom apparaît sur les widgets, dans les alertes et dans vos échanges avec Cora. Un nom parlant rend donc tout le reste plus clair.

Le nouveau nom ne vaut que dans Cora. Il ne change pas dans l’application du fabricant.

## Vérifier qu’un appareil va bien

Chaque ligne affiche l’état de l’appareil. Ce que vous voulez voir, c’est une mise à jour récente et aucun avertissement.

| Ce que vous voyez | Ce que cela veut dire |
|---|---|
| Une heure de mise à jour récente | Tout fonctionne |
| « Mis à jour il y a 3 h » sur un appareil qui n’envoie ses mesures qu’à quelques heures d’intervalle | Normal |
| « Impossible d’atteindre… » | Un problème de réseau, ou l’appareil est éteint |
| « …a refusé la connexion » | Le compte du fabricant doit être reconnecté. Ouvrez l’appareil et reconnectez-vous |
| « En attente de Cora Max » | Un contrôleur GHL que vous venez d’ajouter\xa0: il apparaît dès qu’un Cora Max sur son réseau l’a lu |
| Rien du tout | L’appareil n’a jamais rien envoyé. Vérifiez l’aquarium choisi et la connexion |

## Retirer un appareil

Ouvrez l’appareil et touchez **Retirer l'appareil**. Cora vous demande de confirmer\xa0: *« {name} sera retiré de Cora. L'appareil lui-même n'est ni réinitialisé ni modifié. »*

**Vos mesures sont conservées.** Une fois l’appareil retiré, Cora arrête d’en recevoir de nouvelles données. L’historique déjà recueilli reste sur l’aquarium, et les widgets liés à cet appareil gardent ses anciennes mesures.

Vous perdez le lien en direct. Si l’appareil passait par un compte de fabricant, vous perdez aussi la connexion enregistrée. Pour le rajouter, il faudra vous reconnecter.

:::tip Calmer un appareil trop bavard sans le retirer
Si un appareil fonctionne bien mais envoie trop d’alertes, ajustez ses seuils ou ses réglages de notification. Tout est expliqué dans **[Alertes et seuils](/help/mobile-alerts)**. Vous gardez la connexion et les données, sans le bruit.
:::
