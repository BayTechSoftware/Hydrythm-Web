---
title: Appareils et état des appareils
description: Ce que Cora Max voit, quel appareil interroge chaque aquarium, et quoi vérifier quand les mesures s’arrêtent.
section: Cora Max
reviewed: 2026-09-30
order: 7
group: Equipment
---

**Réglages → Appareils** liste l’équipement que Cora Max voit et indique comment il se porte.

## La liste des appareils

![La liste des appareils](img/max-devices.webp "Filtrer par aquarium, puis chaque appareil avec un résumé en une ligne de ce qu’il contient.")

Cora Max voit le même équipement que votre téléphone, puisque les deux lisent le même compte.

En haut, des puces filtrent la liste sur **Tous les aquariums** ou sur un seul. Chaque appareil a un point d’état, un résumé en une ligne de ce qu’il contient (*21 prises · 4 nourrissages*, *19 tests restants*) et le nom de son aquarium.

Cora Max affiche et pilote les appareils, mais chacun est ajouté, rattaché et retiré depuis votre téléphone. Tant qu’aucun appareil n’est ajouté, cet écran affiche **Ajoutez des appareils dans l’application Cora.** Plus de détails sur l’ajout d’équipement dans [Ajouter, modifier et retirer des appareils](/help/mobile-devices).

## Cora Max principal

Le **Cora Max principal** est l’appareil Cora (en général un Cora Max) qui lit le contrôleur et les autres équipements d’un aquarium pour tout le compte. Un seul appareil doit le faire par aquarium. Les autres écrans affichent simplement ce qu’il lit.

Ouvrez **Réglages → [votre aquarium] → Cora Max principal** pour le voir ou le changer. Vous avez deux possibilités :

- **Tout appareil actif (automatique)** : chaque appareil Cora en ligne qui peut joindre l’équipement de cet aquarium participe, et la dernière écriture l’emporte. Gardez ce choix, sauf si vous avez une raison précise d’en épingler un.
- **Épingler un appareil** : seul cet appareil interroge l’équipement. S’il passe hors ligne, plus rien n’interroge l’équipement de cet aquarium jusqu’à ce que vous en épingliez un autre ou reveniez à Tout appareil actif (automatique).

Ce choix se fait une seule fois par aquarium, et non sur chaque écran Cora. Vous pouvez le changer depuis n’importe quel Cora Max qui affiche cet aquarium, ou depuis Cora Mobile. Plus de détails dans [Plus d’un appareil Cora](/help/mobile-multi-device).

:::note Cora Max principal et Cora Assistant sont deux réglages différents
Le Cora Max principal décide quel appareil **lit votre équipement**. Un autre réglage, **Cora Assistant**, décide quel appareil **répond à « Hey Cora »**. Si vous avez plusieurs Cora Max, vous pouvez régler les deux séparément. Plus de détails dans [Parler à Cora](/help/max-voice).
:::

## Si les mesures d’un aquarium s’arrêtent

Si un aquarium ne se met plus à jour alors qu’un autre continue sur le même écran, commencez par ceci :

1. Ouvrez **Réglages → [cet aquarium] → Cora Max principal**. Vérifiez qu’un appareil est bien attribué et qu’il est en ligne.
2. Si un Cora Max secondaire de cet aquarium affiche **Cora principal hors ligne** dans sa barre du haut, le principal a perdu sa connexion. Le sens de cette étiquette d’état est expliqué dans [L’écran d’accueil de Cora Max](/help/max-tour).
3. **Réglages → Réglages Cora Max → Réseau et mises à jour → Interrogation des appareils** indique à quelle fréquence cet écran lit vos appareils. Ici, la valeur est en lecture seule. Elle se règle dans Cora Mobile.

Si le problème continue, consultez la page [Résolution de problèmes](/help/troubleshooting).

## Gérer un Cora Max depuis votre téléphone

Ouvrez-le depuis l’onglet **Appareils** de votre téléphone. Vous voyez sa variante, sa version de micrologiciel et sa dernière connexion. Vous pouvez aussi le renommer ou changer certains réglages sans vous déplacer.

![Réglages de Cora Max depuis le téléphone](img/max-from-phone.webp "Intervalle d’interrogation, luminosité, volume, alertes à l’écran et minuteur d’assombrissement.")

Ces réglages ne concernent **que cet écran** : sa luminosité, son volume, ses bannières d’alerte et son délai d’assombrissement. C’est pareil que de les changer sur Cora Max. Couper les alertes à l’écran ne change rien à l’historique des alertes ni aux notifications push.

Les aquariums affichés par un Cora Max, et son Cora Max principal pour chacun, sont réglés pour tout le compte. Changez-les depuis l’un ou l’autre appareil, comme expliqué plus haut.

:::note Regardez l’état avant de changer quoi que ce soit
Sur cet écran, la section **État** de **Réglages → Réglages Cora Max** indique pour chaque aquarium l’état de l’interrogation, la dernière interrogation et le dernier envoi vers le cloud. Elle ne change rien. Consultez-la pour comprendre ce qui se passe avant de modifier un réglage.
:::
