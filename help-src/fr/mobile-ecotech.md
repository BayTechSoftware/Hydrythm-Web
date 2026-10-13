---
title: Lampes, pompes et doseurs EcoTech
description: Associez des lampes EcoTech Radion, des pompes VorTech et des doseurs Versa à Cora en Bluetooth, et découvrez ce que vous pouvez en faire.
section: Cora Mobile
reviewed: 2026-10-13
order: 18
group: Equipment
---

:::note Beta
**Beta.** EcoTech est en Beta et n’est ouvert qu’aux utilisateurs Beta. Si vous n’êtes pas un utilisateur Beta, vous ne le verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le [support](/support.html).
:::

Cette page explique comment associer des lampes EcoTech Radion, des pompes VorTech et des doseurs Versa à Cora et les commander. Commencez par **Appareils → Ajouter un appareil → EcoTech**. La même ligne trouve aussi les appareils AquaIllumination, NYOS Quantum, Nero et Orbit qui se trouvent sur le même réseau Bluetooth.

## Ce qu’il vous faut {#what-you-need}

- Un Cora Max à l’aquarium. Il fait la lecture et envoie vos commandes à l’équipement en Bluetooth. Sans lui, la ligne **EcoTech** affiche **Nécessite Cora Max** et reste grisée.
- Le Bluetooth de votre téléphone activé, avec l’autorisation Bluetooth pour Cora. Cora la demande quand vous lancez la recherche.
- Un équipement allumé et à portée du Cora Max.

## L’associer {#linking-it}

1. Allez dans **Appareils → Ajouter un appareil → EcoTech**.
2. Cora recherche les lampes, pompes et doseurs à proximité. Les lampes déjà connectées à l’application Mobius d’EcoTech peuvent ne pas apparaître.
3. Les équipements du même réseau Bluetooth sont regroupés en un seul **Bac Mobius**. Touchez **Lier à…** et choisissez l’aquarium Cora auquel il appartient.
4. Donnez un nom au groupe quand Cora le demande, et c’est associé.

Un appareil marqué **Lecture seule** affiche ses mesures, mais Cora ne peut pas encore le commander. La commande de ce modèle viendra une fois qu’il aura été testé.

Si le même réseau Bluetooth contient aussi des lampes d’un autre aquarium, et que les deux aquariums sont lus par des Cora Max différents, Cora indique **Lu par un seul Cora Max**. Un seul Cora Max lit alors tout le réseau pour les deux aquariums.

Si rien n’est trouvé, vérifiez que le Bluetooth est activé et que l’équipement est alimenté, puis touchez **Nouvelle recherche**.

## Lampes Radion {#radion}

![Une page Radion dans Cora Mobile](img/mobile-radion.webp "L’état, les lampes de ce réseau (toutes ou une seule), puis l’intensité et chaque canal de couleur.")

La page de la lampe a un éditeur de programme et des scènes rapides (**Programme**, **Orage**, **Nuages**, **Couleurs**, **Nourrissage**, **Éteint**). Vous pouvez aussi régler l’acclimatation, le ventilateur, le cycle lunaire et l’horloge.

Dans l’éditeur de programme, **Aperçu de la journée** déroule la journée en accéléré pour que vous la voyiez sans attendre. **Arrêter l'aperçu** remet les lampes comme avant. **Annuler** et **Rétablir** parcourent vos modifications, et **Partir de…** démarre un nouveau programme à partir d’une copie d’un programme existant.

Cora lit les lampes de temps en temps. Dans **Paramètres Radion**, sous **Lecture**, **Lire les lampes toutes les** règle la fréquence. Moins souvent est plus doux pour les lampes. L’ouverture de la page et chaque commande déclenchent quand même une lecture immédiate.

**Paramètres Radion** propose aussi :

- **Régler l'horloge**, pour régler l’horloge de la lampe.
- **Acclimatation**, pour les nouveaux coraux : tout le programme monte progressivement sur le nombre de jours que vous choisissez. L’activer le relance depuis le niveau le plus bas.
- **Alertes** : **La lampe ne répond plus**, **Défaut : chaleur, ventilateur ou LED**, **Horloge décalée de 5 min** et **Température des LED**. Activez celles que vous voulez.

## Pompes VorTech {#vortech}

Une tuile VorTech affiche le mode et la vitesse de la pompe. Vous pouvez changer le mode et la **Vitesse**, modifier son programme et lancer **Nourrissage** pour quelques minutes. Le nourrissage ralentit toutes les VorTech de l’aquarium, et elles reprennent leur programme à la fin. Chaque mode a une courte description à côté, du flux régulier aux poussées de crête de récif, aux houles de marée et aux pulsations. Une pompe ne propose que les modes qu’elle prend en charge.

## Doseurs Versa {#versa}

La page d’un Versa affiche son récipient, ses doses et ses limites. Vous pouvez régler la taille du récipient, toucher **Marquer comme rempli**, lancer **Doser maintenant**, mettre le dosage en **Pause** jusqu’à minuit et modifier le programme. Cora garde un historique des doses pour chaque tête. La cloche règle des alertes de réapprovisionnement en jours restants ou en niveau de remplissage du récipient, comme décrit dans [Consommables](/help/mobile-consumables).

:::warning Pas encore prouvé sur du matériel
Les commandes vers les pompes VorTech et les doseurs Versa n’ont pas encore été prouvées sur du vrai matériel. La lecture fonctionne. Vérifiez l’équipement lui-même les premières fois que vous changez quelque chose, et dites-nous ce que vous voyez depuis [Signaler un problème](/help/mobile-support).
:::

## Alertes {#alerts}

Cora considère un appareil EcoTech comme silencieux après trois lectures manquées à son propre intervalle de lecture. Un réseau composé uniquement de lampes est lu toutes les 30 minutes par défaut, cela prend donc au moins 90 minutes. Voir [Alertes et seuils](/help/mobile-alerts). Les lampes Radion ont aussi leurs propres alertes dans **Paramètres Radion**, décrites plus haut.

## Sur Cora Max {#on-cora-max}

Le même équipement a ses propres pages sur l’écran mural. Plus de détails dans [Contrôler l’équipement depuis Cora Max](/help/max-device-control).
