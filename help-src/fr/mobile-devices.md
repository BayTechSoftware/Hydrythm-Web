---
title: Ajouter, modifier et retirer des appareils
description: Ajouter un équipement à Cora, le rattacher à un aquarium, le renommer et le retirer proprement.
section: Cora Mobile
reviewed: 2026-09-27
order: 9
group: Equipment
---

L’onglet **Appareils** réunit tout ce que vous avez connecté, classé par marque. Chaque groupe peut se replier, pour que la liste reste lisible même avec beaucoup d’équipement.

![L’onglet Appareils](img/mobile-devices.webp "L’équipement est regroupé par marque. Chaque groupe se replie.")

## Ajouter un équipement

Sous la liste, trois boutons servent à des choses différentes.

| Bouton | Ajoute |
|---|---|
| **Ajouter un appareil** | Un Cora Max. Cherche les appareils déjà sur votre Wi-Fi, ou ceux à proximité en Bluetooth. Si la recherche ne trouve rien, **Saisir l’adresse IP manuellement** se trouve sur cet écran. |
| **Trouver une pompe sur votre réseau** | Les pompes Jecod qui se signalent sur le réseau local |
| **Ajouter AquaWiz** | Un contrôleur AquaWiz, par votre compte AquaWiz |

![Ajouter un Cora Max](img/mobile-add-device.webp "Ajouter un appareil recherche un Cora Max sur le Wi-Fi et le Bluetooth.")

Les autres équipements (Neptune Apex et Red Sea ReefBeat) se connectent depuis l’aquarium, pas depuis cette liste. Voir [Connecter votre équipement](/help/mobile-connections).

Quand vous ajoutez un équipement comme un chauffage, une pompe ou un écumeur, la marque et le modèle se **complètent automatiquement**. Commencez à taper, et Cora propose des noms tirés d’une longue liste de marques vérifiée à la source. Si la vôtre n’y est pas, tapez-la quand même. Cora garde ce que vous saisissez.

:::note Cora et votre téléphone doivent être sur le même réseau
Un équipement trouvé sur le réseau local doit être sur le même réseau que votre téléphone au moment de l’ajout. **Après l’installation, il reste joignable uniquement sur ce réseau** (ou en Bluetooth pour les appareils qui l’utilisent), sauf si un appareil Cora sur place peut le joindre pour vous.

Un équipement qui s’affiche bien à la maison peut donc montrer des valeurs plus anciennes quand vous êtes absent, sauf si un Cora Max sur place peut l’interroger. Ce n’est pas une panne. Cela dépend simplement de l’endroit d’où l’équipement est joignable.
:::

## Rattacher un appareil à un aquarium

La plupart des équipements appartiennent à un seul aquarium. C’est ce rattachement qui fait apparaître leurs mesures sur le tableau de bord de cet aquarium.

**Cora Max fait exception.** Il peut être rattaché à quatre aquariums au plus et passe de l’un à l’autre à l’écran. Voir [Plus d’un appareil Cora](/help/mobile-multi-device).

Ouvrez l’appareil et choisissez **Aquarium**. Si vous avez plusieurs bacs, c’est le réglage le plus important. Un chauffage rattaché au mauvais aquarium envoie des mesures parfaitement justes… au mauvais endroit.

:::warning Choisissez l’aquarium avant de vous fier aux mesures
Un appareil sans aquarium envoie quand même ses mesures, mais elles ne s’affichent nulle part. Si un appareil que vous venez d’ajouter n’apparaît sur aucun tableau de bord, vérifiez d’abord ce point.
:::

## Renommer

Ouvrez l’appareil et modifiez son nom. Donnez-lui le nom que vous utilisez tous les jours : « Remontée », « Brassage gauche », « Chauffage décantation ». Ce nom apparaît sur les widgets, dans les alertes et dans vos échanges avec Cora. Un nom parlant rend donc tout le reste plus clair.

Le nouveau nom ne vaut que dans Cora. Il ne change pas dans l’application du fabricant.

## Vérifier qu’un appareil va bien

Chaque ligne affiche l’état de l’appareil. Ce que vous voulez voir, c’est une mise à jour récente et aucun avertissement.

| Ce que vous voyez | Ce que cela veut dire |
|---|---|
| Une heure de mise à jour récente | Tout fonctionne |
| « Mis à jour il y a 3 h » sur un appareil qui n’envoie ses mesures qu’à quelques heures d’intervalle | Normal |
| « Impossible d’atteindre… » | Un problème de réseau, ou l’appareil est éteint |
| « …a refusé la connexion » | Le compte du fabricant doit être reconnecté. Ouvrez l’appareil et reconnectez-vous |
| Rien du tout | L’appareil n’a jamais rien envoyé. Vérifiez l’aquarium choisi et la connexion |

## Retirer un appareil

Ouvrez l’appareil et choisissez **Retirer**. Cora vous demande de confirmer et vous indique exactement ce qui sera retiré.

**Vos mesures sont conservées.** Une fois l’appareil retiré, Cora arrête d’en recevoir de nouvelles données. L’historique déjà recueilli reste sur l’aquarium, et les widgets liés à cet appareil gardent ses anciennes mesures.

Vous perdez le lien en direct. Si l’appareil passait par un compte de fabricant, vous perdez aussi la connexion enregistrée. Pour le rajouter, il faudra vous reconnecter.

:::tip Calmer un appareil trop bavard sans le retirer
Si un appareil fonctionne bien mais envoie trop d’alertes, ajustez ses seuils ou ses réglages de notification. Tout est expliqué dans **[Alertes et seuils](/help/mobile-alerts)**. Vous gardez la connexion et les données, sans le bruit.
:::
