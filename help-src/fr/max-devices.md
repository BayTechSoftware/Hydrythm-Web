---
title: Appareils et état des appareils
description: Ce que Cora Max peut voir, quel appareil interroge chaque aquarium, et quoi vérifier quand l’interrogation s’arrête.
section: Cora Max
reviewed: 2026-09-27
order: 7
group: Equipment
---

**Réglages → Appareils** liste l’équipement que Cora Max peut voir et signale comment il se comporte.

## La liste des appareils

![La liste des appareils](img/max-devices.webp "Filtrer par aquarium, puis chaque appareil avec un résumé en une ligne de ce qu’il contient.")

Cora Max voit le même équipement que votre téléphone, car les deux lisent le même compte.

Des puces de filtre en haut réduisent la liste à **Tous les aquariums** ou à un seul. Chaque entrée porte un point d’état, un résumé en une ligne de ce que l’appareil contient (*21 prises · 4 nourrissages*, *19 tests restants*) et l’aquarium auquel il appartient.

Ajouter et configurer un équipement est plus facile sur le téléphone ; voir [Ajouter, modifier et retirer des appareils](/help/mobile-devices).

## Cora Max principal : quelle tablette parle à votre équipement

**Cora Max principal** est la tablette (ou autre appareil Cora) qui lit le contrôleur d’un aquarium et son autre équipement pour tout le compte. Un seul appareil doit faire cela par aquarium ; tout autre écran affiche simplement ce qu’il lit.

Ouvrez **Réglages → [votre aquarium] → Cora Max principal** pour le voir ou le changer. Il y a deux types de choix :

- **Tout appareil actif (automatique)** : chaque appareil Cora en ligne qui peut atteindre l’équipement de cet aquarium partage le travail, et la dernière écriture l’emporte. C’est le réglage à utiliser à moins que vous n’ayez une raison spécifique d’en épingler un.
- **Épingler un appareil** : seul cet appareil interroge. Si l’appareil épinglé passe hors ligne, rien n’interroge l’équipement de cet aquarium jusqu’à ce que vous en épingliez un autre, ou reveniez à Tout appareil actif (automatique).

Ce choix se fait une fois, pour l’aquarium, pas une fois par écran Cora. Changez-le depuis n’importe quel Cora Max affichant cet aquarium, ou depuis Cora Mobile ; voir [Plus d’un appareil Cora](/help/mobile-multi-device).

:::note Cora Max principal n’est pas la même chose que Cora Assistant
Cora Max principal détermine quel appareil **lit votre équipement**. Un réglage séparé, **Cora Assistant**, détermine quel appareil **répond à « Hey Cora »**. Un foyer avec plus d’un Cora Max peut régler ces deux indépendamment. Voir [Parler à Cora](/help/max-voice).
:::

## Si les mesures d’un aquarium s’arrêtent

Si les mesures d’un aquarium s’arrêtent alors qu’un autre aquarium sur le même écran continue de se mettre à jour, commencez par :

1. **Réglages → [cet aquarium] → Cora Max principal** : confirmez qu’un appareil est réellement attribué, et qu’il est en ligne.
2. Si un Cora Max secondaire pour cet aquarium affiche la pastille **Cora principal hors ligne** dans sa barre supérieure, le principal a perdu sa connexion ; voir [L’écran d’accueil de Cora Max](/help/max-tour) pour ce que signifie la pastille d’état.
3. **Réglages → Réglages Cora Max → Réseau et mises à jour → Interrogation des appareils** montre à quelle fréquence cette unité elle-même lit vos appareils ; cette valeur est en lecture seule ici et se règle depuis Cora Mobile.

**Si cela ne fonctionne pas :** voir [Résolution de problèmes](/help/troubleshooting).

## Gérer un Cora Max depuis votre téléphone

Ouvrez l’unité depuis l’onglet **Appareils** de votre téléphone pour voir sa variante, sa version de micrologiciel et quand elle a été vue pour la dernière fois, et pour la renommer ou changer certains de ses réglages sans vous déplacer jusqu’à elle.

![Réglages de Cora Max depuis le téléphone](img/max-from-phone.webp "Intervalle d’interrogation, luminosité, volume, alertes à l’écran et minuteur d’assombrissement.")

Les réglages affichés ainsi décrivent **cet écran seul** (sa luminosité, son volume, ses bannières d’alerte à l’écran et son minuteur d’assombrissement), de la même façon que si vous les changiez au mur. Désactiver les alertes à l’écran n’affecte pas l’historique des alertes ni les notifications push.

Quels aquariums un Cora Max affiche, et lequel est son Cora Max principal pour chaque aquarium, sont des choix à l’échelle du compte ; changez-les depuis l’un ou l’autre appareil, comme décrit ci-dessus.

:::note L’état de l’appareil est en lecture d’abord
La section **État** de **Réglages → Réglages Cora Max** sur cet écran signale l’état d’interrogation, la dernière interrogation et la dernière écriture cloud pour chaque aquarium, sans rien changer. Utilisez-la pour établir ce qui se passe avant de modifier un réglage.
:::
